#!/usr/bin/env python3
"""
Generate voice narration for every lesson.

Two backends supported:
  --backend elevenlabs  → ElevenLabs API (paid, best quality)
  --backend kokoro      → Kokoro-82M local (free, offline, MIT license, ~good enough)
  --backend coqui       → Coqui TTS local (free, offline, older)

Output:
  assets/audio/period{N}/section{M}/topic-{letter}.mp3
  assets/audio/manifest.json (lesson_id → {path, duration_seconds, checksum})

Usage:
  # Dry run — show what would be generated
  python3 bin/generate-narration.py --dry-run

  # Real run with Kokoro
  python3 bin/generate-narration.py --backend kokoro --voice af_bella

  # ElevenLabs (requires ELEVENLABS_API_KEY env)
  python3 bin/generate-narration.py --backend elevenlabs --voice-id 21m00Tcm4TlvDq8ikWAM

This is a build-time tool. Do NOT invoke at runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
AUDIO_ROOT = ROOT / "assets" / "audio"
MANIFEST = AUDIO_ROOT / "manifest.json"


def extract_narratable_text(md: str) -> str:
    """Strip markdown to prose suitable for TTS.
    Removes: YAML frontmatter, code blocks, tables, image alts, footnote refs.
    Keeps: paragraph text, headings (spoken slower), list items.
    """
    # Strip YAML frontmatter
    md = re.sub(r"^---\n.*?\n---\n", "", md, count=1, flags=re.DOTALL)
    # Strip fenced code blocks
    md = re.sub(r"```.*?```", "", md, flags=re.DOTALL)
    # Strip tables (any line with pipes)
    md = "\n".join(l for l in md.split("\n") if not re.match(r"^\s*\|", l))
    # Strip images
    md = re.sub(r"!\[.*?\]\(.*?\)", "", md)
    # Strip footnote refs like [^1]
    md = re.sub(r"\[\^\d+\]", "", md)
    # Strip footnote definitions like [^1]: text
    md = re.sub(r"^\[\^\d+\]:.*$", "", md, flags=re.MULTILINE)
    # Convert markdown headings to spoken pauses
    md = re.sub(r"^(#+)\s+(.+)$", r"\2.", md, flags=re.MULTILINE)
    # Convert bullet points
    md = re.sub(r"^[\-\*]\s+", "", md, flags=re.MULTILINE)
    # Collapse whitespace
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r" +", " ", md)
    return md.strip()


def scan_lessons():
    lessons = []
    for md_path in sorted(CONTENT.glob("period*/section*/*.md")):
        rel = md_path.relative_to(CONTENT)
        # rel = period1/section3/topic-a-smaw-equipment.md
        parts = rel.parts
        period_num = int(parts[0].replace("period", ""))
        section_num = int(parts[1].replace("section", ""))
        topic_letter = parts[2].split("-")[1] if "-" in parts[2] else "x"
        lessons.append({
            "id": f"p{period_num}-s{section_num}-{topic_letter}",
            "md_path": md_path,
            "audio_rel_path": f"period{period_num}/section{section_num}/{md_path.stem}.mp3",
        })
    return lessons


def tts_kokoro(text: str, out_path: Path, voice: str = "af_bella") -> None:
    """Requires: pip install kokoro-onnx soundfile"""
    try:
        from kokoro_onnx import Kokoro  # type: ignore
        import soundfile as sf  # type: ignore
    except ImportError:
        raise RuntimeError("Kokoro backend needs: pip install kokoro-onnx soundfile")
    # Load once per process; cache would be nice
    if not hasattr(tts_kokoro, "_engine"):
        model_path = os.environ.get("KOKORO_MODEL", "kokoro-v1.0.onnx")
        voices_path = os.environ.get("KOKORO_VOICES", "voices-v1.0.bin")
        tts_kokoro._engine = Kokoro(model_path, voices_path)  # type: ignore
    samples, sr = tts_kokoro._engine.create(text, voice=voice, speed=1.0)  # type: ignore
    # Save as MP3 via ffmpeg for smaller file size
    tmp_wav = out_path.with_suffix(".wav")
    sf.write(str(tmp_wav), samples, sr)
    subprocess.run(["ffmpeg", "-y", "-i", str(tmp_wav), "-codec:a", "libmp3lame",
                    "-qscale:a", "4", str(out_path)], check=True, capture_output=True)
    tmp_wav.unlink()


def tts_elevenlabs(text: str, out_path: Path, voice_id: str) -> None:
    import urllib.request
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError("ELEVENLABS_API_KEY not set")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    body = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }).encode()
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"xi-api-key": api_key,
                                          "Content-Type": "application/json",
                                          "Accept": "audio/mpeg"})
    with urllib.request.urlopen(req) as resp:
        out_path.write_bytes(resp.read())


def get_duration_seconds(mp3_path: Path) -> float:
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(mp3_path)],
            check=True, capture_output=True, text=True
        )
        return round(float(out.stdout.strip()), 1)
    except Exception:
        return 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=["kokoro", "elevenlabs", "coqui"], default="kokoro")
    ap.add_argument("--voice", default="af_bella", help="Kokoro voice name")
    ap.add_argument("--voice-id", default="21m00Tcm4TlvDq8ikWAM", help="ElevenLabs voice ID")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="Regenerate even if audio exists")
    ap.add_argument("--limit", type=int, help="Only process first N lessons (for testing)")
    args = ap.parse_args()

    lessons = scan_lessons()
    if args.limit:
        lessons = lessons[: args.limit]

    print(f"Found {len(lessons)} lessons to narrate.")

    manifest: dict[str, dict] = {}
    if MANIFEST.exists() and not args.force:
        manifest = json.loads(MANIFEST.read_text())

    for lesson in lessons:
        text = extract_narratable_text(lesson["md_path"].read_text())
        text_hash = hashlib.sha256(text.encode()).hexdigest()[:16]

        existing = manifest.get(lesson["id"])
        if existing and existing.get("text_hash") == text_hash and not args.force:
            print(f"[skip] {lesson['id']} — unchanged")
            continue

        out_path = AUDIO_ROOT / lesson["audio_rel_path"]
        out_path.parent.mkdir(parents=True, exist_ok=True)

        chars = len(text)
        print(f"[gen ] {lesson['id']} — {chars} chars, ~{chars // 15}s speech")
        if args.dry_run:
            continue

        try:
            if args.backend == "kokoro":
                tts_kokoro(text, out_path, voice=args.voice)
            elif args.backend == "elevenlabs":
                tts_elevenlabs(text, out_path, voice_id=args.voice_id)
            else:
                print(f"[err ] {args.backend} not implemented in this stub", file=sys.stderr)
                return 1
        except Exception as e:
            print(f"[err ] {lesson['id']}: {e}", file=sys.stderr)
            continue

        manifest[lesson["id"]] = {
            "path": lesson["audio_rel_path"],
            "duration_seconds": get_duration_seconds(out_path),
            "text_hash": text_hash,
            "backend": args.backend,
            "voice": args.voice if args.backend == "kokoro" else args.voice_id,
        }

    if not args.dry_run:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps(manifest, indent=2))
        print(f"Wrote manifest with {len(manifest)} entries.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
