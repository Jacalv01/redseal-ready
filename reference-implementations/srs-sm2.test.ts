/**
 * Quick vitest/jest test suite for the SRS module.
 * Rork can run this to verify the algorithm before shipping.
 */

import {
  initState,
  review,
  isDue,
  computeSubTaskStats,
  getWeakSubTasks,
} from './srs-sm2';

const NOW = 1700000000000; // frozen
const DAY = 86400000;

describe('SRS SM-2', () => {
  test('initState: never reviewed, due now', () => {
    const s = initState('Q1', NOW);
    expect(s.repetitions).toBe(0);
    expect(s.next_due_at).toBe(NOW);
    expect(isDue(s, NOW)).toBe(true);
  });

  test('perfect answer sequence: 1 day → 6 days → ~15 days', () => {
    let s = initState('Q1', NOW);
    s = review(s, 5, NOW);
    expect(s.interval_days).toBe(1);
    expect(s.repetitions).toBe(1);
    expect(s.next_due_at).toBe(NOW + DAY);

    s = review(s, 5, s.next_due_at);
    expect(s.interval_days).toBe(6);
    expect(s.repetitions).toBe(2);

    s = review(s, 5, s.next_due_at);
    expect(s.interval_days).toBeGreaterThanOrEqual(15);
    expect(s.interval_days).toBeLessThan(17); // ~6 * 2.6
    expect(s.repetitions).toBe(3);
  });

  test('wrong answer resets to 1 day', () => {
    let s = initState('Q1', NOW);
    s = review(s, 5, NOW);            // repetitions=1
    s = review(s, 5, s.next_due_at);  // repetitions=2, interval=6
    s = review(s, 1, s.next_due_at);  // wrong
    expect(s.repetitions).toBe(0);
    expect(s.interval_days).toBe(1);
    expect(s.ease_factor).toBeLessThan(2.5); // ease penalized
  });

  test('ease factor never goes below 1.3', () => {
    let s = initState('Q1', NOW);
    for (let i = 0; i < 20; i++) s = review(s, 0, NOW + i * DAY);
    expect(s.ease_factor).toBeGreaterThanOrEqual(1.3);
  });

  test('sub-task stats aggregation', () => {
    const qMap = {
      'D-13.02-Q001': 'D-13.02',
      'D-13.02-Q002': 'D-13.02',
      'D-14.01-Q001': 'D-14.01',
    };
    let s1 = initState('D-13.02-Q001', NOW);
    s1 = review(s1, 5, NOW);        // correct
    s1 = review(s1, 1, NOW + DAY);  // wrong

    let s2 = initState('D-13.02-Q002', NOW);
    s2 = review(s2, 5, NOW);        // correct
    s2 = review(s2, 5, NOW + DAY);  // correct

    let s3 = initState('D-14.01-Q001', NOW);
    s3 = review(s3, 1, NOW);        // wrong
    s3 = review(s3, 1, NOW + DAY);  // wrong
    s3 = review(s3, 1, NOW + 2*DAY); // wrong

    const stats = computeSubTaskStats(
      { 'D-13.02-Q001': s1, 'D-13.02-Q002': s2, 'D-14.01-Q001': s3 },
      qMap
    );

    expect(stats['D-13.02'].attempts).toBe(4);
    expect(stats['D-13.02'].correct).toBe(3);
    expect(stats['D-13.02'].accuracy).toBeCloseTo(0.75);
    expect(stats['D-13.02'].mastery).toBe('developing');

    expect(stats['D-14.01'].mastery).toBe('weak');

    const weakest = getWeakSubTasks(stats, 5);
    expect(weakest[0].sub_task_id).toBe('D-14.01');
  });
});
