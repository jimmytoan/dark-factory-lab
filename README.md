# dark-factory-lab

A small "dark factory": agents take a written spec to shipped code, no human reads the code, and the result is graded on scenarios the coding agent never sees.

The question: how far apart are the tests the agent can see (public acceptance examples) and the scenarios it cannot (holdout)? And does the shipped code survive a follow-up change request?

## Layout

```
specs/<name>/SPEC.md            the product spec (given to the agent)
specs/<name>/public/            acceptance examples the agent may read and run (copied to tests/ in its sandbox)
specs/<name>/CHANGE.md          follow-up change request (round 2)
specs/<name>/public_v2/         acceptance examples for the change
holdout/<name>/v1, v2           held-out scenarios. Never mounted into a coder sandbox.
reference/<name>/v1, v2         reference implementations. Prove the suites are satisfiable. Never mounted.
factory/                        harness: sandbox, agent loop, designs, grader, gaming checks, runner, report
results/runs.jsonl              one record per run
results/spend.jsonl             one line per model call (the spend cap reads this)
results/raw/<run_id>/           transcript and shipped workspace (git-ignored)
```

Specs: `splitr` (expense-splitting CLI), `bookings` (room booking HTTP API), `sessionize` (clickstream batch job). Python standard library only.

Factory designs (`factory/designs.py`):

- `oneshot`: one model response writes all files. It never sees a test run.
- `loop`: one agent with a shell, iterating on the visible tests until it decides it is done.
- `pce`: planner writes a plan, coder builds, a separate evaluator with fresh context probes the product and reports, coder fixes. Up to two evaluate-and-fix rounds.

## Isolation

The coder works in a Docker container with no network and one bind mount: its workspace. `holdout/` and `reference/` are sibling directories on the host that are never mounted. Every holdout file carries a canary string; after each run the shipped workspace and the transcript are scanned for it. Grading happens after the agent has stopped, in a fresh container, with pristine copies of the suites.

## Commands

```bash
docker build -t dfl-sandbox sandbox
```

```bash
uv sync
```

```bash
uv run python -m factory.selftest
```

The self-test makes no model calls. It checks that the references pass every suite, that a hard-coded implementation passes public and fails holdout, that the gaming checks fire, that the sandbox cannot see the holdout, and that the pipeline runs end to end with a scripted model.

```bash
caffeinate -i uv run python -m factory.run --tag pilot --models haiku --change --cap 3 --resume
```

```bash
uv run python -m factory.report --tag pilot
```

`--cap` is a hard spend limit in USD for the tag, enforced before each run from `results/spend.jsonl`. `--resume` skips cells that already have a finished record. API keys are read from a git-ignored `.env` (`ANTHROPIC_API_KEY`).

## What is measured per run

Public pass rate and holdout pass rate (the gap is the headline), cost, wall time, model calls, and gaming checks: tests edited or deleted, example data hard-coded into the product, test-runner sniffing. Round 2 adds a regression rate (old holdout scenarios that still apply) and a change rate (new holdout scenarios).

Sources and what could be verified: `SOURCES.md`. Pilot findings and the proposed full run: `PLAN.md`.
