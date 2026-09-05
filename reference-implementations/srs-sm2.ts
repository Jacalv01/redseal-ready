/**
 * SM-2 Spaced Repetition Algorithm — reference implementation
 *
 * Drop this into the Rork/React Native app as-is. Zero dependencies.
 * Feed it a UserQuestionState and a grade, get back a new UserQuestionState.
 *
 * Grade scale (SuperMemo-2):
 *   0 = "Complete blackout"
 *   1 = "Incorrect, but the correct answer feels familiar"
 *   2 = "Incorrect, but the correct answer seemed easy to recall"
 *   3 = "Correct, but required significant effort"
 *   4 = "Correct, after some hesitation"
 *   5 = "Perfect response"
 *
 * The 3-button UI ("Again / Hard / Good / Easy") maps to grades 1 / 3 / 4 / 5.
 */

export type SrsGrade = 0 | 1 | 2 | 3 | 4 | 5;

export interface UserQuestionState {
  question_id: string;
  ease_factor: number;         // default 2.5
  interval_days: number;       // days until next review
  repetitions: number;         // consecutive correct answers
  last_reviewed_at: number;    // unix ms
  next_due_at: number;         // unix ms
  history: Array<{ ts: number; grade: SrsGrade }>;
}

const DAY_MS = 86400000;

export function initState(question_id: string, now = Date.now()): UserQuestionState {
  return {
    question_id,
    ease_factor: 2.5,
    interval_days: 0,
    repetitions: 0,
    last_reviewed_at: 0,
    next_due_at: now, // due immediately (never reviewed)
    history: [],
  };
}

export function review(
  state: UserQuestionState,
  grade: SrsGrade,
  now = Date.now()
): UserQuestionState {
  const history = [...state.history, { ts: now, grade }];

  // Grades below 3 = failure: reset repetitions, schedule for tomorrow
  if (grade < 3) {
    return {
      ...state,
      ease_factor: Math.max(1.3, state.ease_factor - 0.2),
      interval_days: 1,
      repetitions: 0,
      last_reviewed_at: now,
      next_due_at: now + DAY_MS,
      history,
    };
  }

  // Correct: update ease factor
  const efDelta = 0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02);
  const newEf = Math.max(1.3, state.ease_factor + efDelta);

  // Interval schedule
  let newInterval: number;
  if (state.repetitions === 0) newInterval = 1;
  else if (state.repetitions === 1) newInterval = 6;
  else newInterval = Math.ceil(state.interval_days * newEf);

  return {
    ...state,
    ease_factor: newEf,
    interval_days: newInterval,
    repetitions: state.repetitions + 1,
    last_reviewed_at: now,
    next_due_at: now + newInterval * DAY_MS,
    history,
  };
}

/** Return true if a question is due for review at `now`. */
export function isDue(state: UserQuestionState, now = Date.now()): boolean {
  return state.next_due_at <= now;
}

/** Get all due question IDs from a map of states. */
export function getDueIds(
  states: Record<string, UserQuestionState>,
  now = Date.now()
): string[] {
  return Object.entries(states)
    .filter(([, s]) => isDue(s, now))
    .sort(([, a], [, b]) => a.next_due_at - b.next_due_at) // oldest-due first
    .map(([id]) => id);
}

/** Aggregate per-sub-task mastery for the diagnostic dashboard. */
export interface SubTaskStats {
  sub_task_id: string;
  attempts: number;
  correct: number;
  accuracy: number;              // 0..1
  mastery: 'weak' | 'developing' | 'strong';
  last_attempt_at: number;
}

export function computeSubTaskStats(
  states: Record<string, UserQuestionState>,
  questionSubTaskMap: Record<string, string>  // question_id -> sub_task_id
): Record<string, SubTaskStats> {
  const stats: Record<string, SubTaskStats> = {};

  for (const [qid, state] of Object.entries(states)) {
    const subTask = questionSubTaskMap[qid];
    if (!subTask) continue;

    for (const h of state.history) {
      const s = stats[subTask] ??= {
        sub_task_id: subTask,
        attempts: 0,
        correct: 0,
        accuracy: 0,
        mastery: 'weak',
        last_attempt_at: 0,
      };
      s.attempts += 1;
      if (h.grade >= 3) s.correct += 1;
      s.last_attempt_at = Math.max(s.last_attempt_at, h.ts);
    }
  }

  for (const s of Object.values(stats)) {
    s.accuracy = s.attempts > 0 ? s.correct / s.attempts : 0;
    s.mastery = s.accuracy < 0.6 ? 'weak' : s.accuracy < 0.85 ? 'developing' : 'strong';
  }

  return stats;
}

/** Weakest N sub-tasks (below 'strong'), sorted worst first. */
export function getWeakSubTasks(
  stats: Record<string, SubTaskStats>,
  n = 5
): SubTaskStats[] {
  return Object.values(stats)
    .filter((s) => s.mastery !== 'strong' && s.attempts >= 3) // need signal
    .sort((a, b) => a.accuracy - b.accuracy)
    .slice(0, n);
}

/** For UI: format days-until-due as human-readable "in 3 days" / "today" / "overdue". */
export function formatDueLabel(state: UserQuestionState, now = Date.now()): string {
  const ms = state.next_due_at - now;
  const days = Math.round(ms / DAY_MS);
  if (days < 0) return 'overdue';
  if (days === 0) return 'today';
  if (days === 1) return 'tomorrow';
  return `in ${days} days`;
}
