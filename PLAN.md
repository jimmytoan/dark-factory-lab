# PLAN: pilot findings and proposed full run

Status on 2026-11-16: pilot finished, full run NOT started. Waiting for approval of a run size below.

## What exists

- Three product specs with public acceptance examples, held-out scenario suites, reference implementations and one follow-up change request each: `splitr` (CLI), `bookings` (HTTP API), `sessionize` (data job).
- Three factory designs: `oneshot`, `loop`, `pce` (planner, coder, evaluator).
- A sandbox with no network and one mount, script-only grading, gaming checks, a spend cap, `--resume`.
- Self-test: `uv run python -m factory.selftest`, 39 checks, no model calls, all pass.
- Sources and what could be verified: `SOURCES.md`. The OpenAI harness-engineering post could not be opened (HTTP 403) and is not verified.

## Pilot

34 runs, 0 errors, $2.59 of the $3.00 cap. Records: `results/runs.jsonl` (tag `pilot`). Tables: `results/pilot-report.md`.

Reproduce (each line resumes and skips finished cells; a fresh clone re-runs them):

```bash
caffeinate -i uv run python -m factory.run --tag pilot --models haiku --change --cap 3 --resume
```

```bash
caffeinate -i uv run python -m factory.run --tag pilot --spec-level brief --models haiku --cap 3 --resume
```

```bash
caffeinate -i uv run python -m factory.run --tag pilot --spec-level brief --models opus --designs oneshot,loop --run-cap 0.5 --cap 3 --resume
```

```bash
caffeinate -i uv run python -m factory.run --tag pilot --spec-level brief --models opus --designs pce --specs splitr --run-cap 1.2 --cap 3 --resume
```

```bash
uv run python -m factory.report --tag pilot
```

### Finding 1: with a precise spec, the factory is boring

Full `SPEC.md`, Claude Haiku 5.5, one trial per cell, all three specs, build round and change round (18 runs).

| Design | Public | Holdout, build | Holdout, after change | Cost per build | Time per build |
| --- | --- | --- | --- | --- | --- |
| oneshot | 26/26 | 86/86 | 130/130 | $0.006 | 47 s |
| loop | 26/26 | 86/86 | 130/130 | $0.008 | 47 s |
| pce | 26/26 | 86/86 | 130/130 | $0.034 | 204 s |

Every run passed every held-out scenario, including the regression and change suites in round 2. The cheapest model in one response did it for about half a cent. The planner and evaluator added 4 to 6 times the cost and 4 times the wall time for the same score. So the original design could not separate anything: no gap, no difference between designs, nothing for a stronger model to improve.

### Finding 2: with a realistic ticket, the gap appears, and it is not a coding gap

I added a second spec level. `BRIEF.md` is the same product as a customer would write it: the interface, the formats and the error codes, but without tie-breaks, check order and boundary cases. The public examples are unchanged. The holdout still checks the full intent. Each held-out scenario is tagged by what the ticket says about it (`holdout/<spec>/v1/classes.json`): `stated`, `implied` (not written, one sensible answer), `arbitrary` (needs a decision the ticket does not make).

| Model | Design | Runs | Public | Holdout | stated | implied | arbitrary | Cost per run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haiku 5.5 | oneshot | 3 | 26/26 | 70/86 (81%) | 25/25 | 27/32 | 18/29 | $0.005 |
| Haiku 5.5 | loop | 3 | 26/26 | 67/86 (78%) | 24/25 | 27/32 | 16/29 | $0.006 |
| Haiku 5.5 | pce | 3 | 26/26 | 70/86 (81%) | 25/25 | 27/32 | 18/29 | $0.044 |
| Opus 5.5 | oneshot | 3 | 26/26 | 69/86 (80%) | 25/25 | 26/32 | 18/29 | $0.150 |
| Opus 5.5 | loop | 3 | 26/26 | 72/86 (84%) | 25/25 | 26/32 | 21/29 | $0.209 |
| Opus 5.5 | pce | 1 (splitr) | 8/8 | 19/26 (73%) | 6/6 | 7/9 | 6/11 | $1.018 |

- The visible tests were green in all 16 runs. The holdout was 73% to 84%. The agent had no signal that anything was wrong.
- What the ticket states was built correctly 130 times out of 131. The misses are almost all in what the ticket leaves open.
- A model 30 times more expensive did not close the gap. Neither did the planner and evaluator. That makes sense: nobody inside the factory knows the answer.
- Failure counts are from `results/runs.jsonl`; for each I re-ran the scenario against one shipped workspace to see the mismatch. All six splitr runs fail the case-insensitive sort (the Opus one-shot prints `Zoe, adam, bob`). All five sessionize runs fail the keep-the-earliest-duplicate scenario (the Opus loop run kept the first copy in the file). All five bookings runs fail the bad-JSON scenario (the Opus one-shot answers a JSON array body with 422 instead of 400). Four of six splitr runs fail options-before-command (exit code 64 in the Opus one-shot). One Haiku run printed two `header: missing` lines where the ticket describes one.

### Finding 3: no gaming, and an evaluator that cries wolf

- Gaming: 0 of 34 runs edited or deleted tests, hard-coded example data, or sniffed the test runner. The canary never appeared in a workspace or transcript.
- In the 6 full-spec `pce` runs, the evaluator reported defects in 3, on code that already passed every held-out scenario. In 2 of them it still reported defects after the fix round. These need reading before they go into the post: they may be false alarms or real findings outside my suites.

### What failed or is weak in the pilot

- One trial per cell. Differences of two or three scenarios between cells are noise. Only the direction is usable.
- Several held-out scenarios bundle many probes, so one arbitrary probe fails a scenario I tagged `implied` (example: `test_booking_field_validation` fails only on a 101-character title, which the ticket does not limit). The class numbers above are therefore rough. The classes are my own judgment.
- The sentence "Where the spec is silent, choose the behaviour the customer most likely wants" was added to the coder prompt before the brief runs, after the full-spec runs. The two levels in the pilot did not use the identical prompt.
- The `evaluator_touched_src` flag fired in two runs because a pytest cache was created under `tests/`. I read both transcripts: no product or test file was changed. The check is fixed for later runs; the two pilot values are false positives.
- The change round ran only on the full spec, where everything passes. It says nothing yet about survival under change.
- Specs are small, greenfield and single file (100 to 300 lines). This is far from the months-long decay HumanLayer describes.
- Only Claude models were run. GPT needs an adapter for the Responses API and a price check; Gemini is limited to 500 requests a day.

## Proposed full run

Preparation, no model cost (about 2 hours of my work):

1. Split bundled held-out scenarios into one probe each, then re-tag the classes and re-run the self-test.
2. Add a fourth design, `ask`: before coding, the agent may put up to 10 questions to the spec owner. A separate model that holds the full `SPEC.md` answers them. This tests the obvious remedy for finding 2 (move the human to the spec) and counts how many questions it takes. Grading stays scripts.
3. Change round for the brief level, scored as survival: of the held-out scenarios a codebase passed after the build, how many still pass after the change, plus the change scenarios.
4. Identical prompts for both spec levels. Fix the report to show medians and ranges over trials.

| Block | Runs | Estimated cost |
| --- | --- | --- |
| Haiku, full + brief, 3 designs, 3 specs, 3 trials, build | 54 | $1 |
| Haiku, change round on all 54 shipped codebases | 54 | $1.5 |
| Opus, brief, 3 designs, 3 specs, 3 trials, build | 27 | $12.5 |
| Opus, full, oneshot + loop, 3 specs, 1 trial (sanity) | 6 | $1 |
| Opus, change round on brief oneshot + loop | 18 | $4 |
| `ask` design, brief, Haiku + Opus, 3 specs, 3 trials | 18 | $4 |
| **Option M (recommended)** | **177** | **about $24, hard stop $30** |

- Wall time: about 6 to 7 hours, sequential, resumable.
- Option S: Haiku blocks plus `ask` on Haiku only: 117 runs, about $3, 4 hours. Loses the model-tier comparison beyond the pilot.
- Option L: option M plus three more change requests per spec (a chain of four changes, to test decay), Haiku only for the chain: about 100 more runs, about $3 more, plus 3 to 4 hours of authoring. This is the only block that speaks to the "does not survive change" criticism with more than one data point.
- Optional: GPT-6.1 as a second vendor on the brief level. Not estimated; needs the adapter and a verified price.

## Post angle

Working title: "I built a dark factory. The code was never the problem."

- Give a factory a precise spec and the cheapest model ships correct code in one response for half a cent. Held-out scenarios find nothing. The planner and evaluator harness costs four to six times more for the same result.
- Give it the ticket a customer would really write and every visible test is still green, while about one held-out scenario in five fails. A stronger model and an evaluator do not help, because the missing information is not in the factory.
- So the holdout is doing a different job than advertised. It caught no cheating in 34 runs. It caught unstated intent. The work that is left for people is writing the spec and the scenarios, which is where StrongDM says its people spend their time, and close to what Horthy recommends from the other side of the argument.
- Caveats to carry into the post: three small greenfield products, deterministic scenarios instead of StrongDM's model-judged satisfaction, Claude models only, one change round.

Decisions needed: run size (S, M or L), whether to add the `ask` design, whether to add GPT.
