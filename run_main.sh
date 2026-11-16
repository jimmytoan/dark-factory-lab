#!/bin/bash
# Option M from PLAN.md. Sequential, resumable: re-run this script to continue after a stop.
set -u
cd "$(dirname "$0")"
R="uv run python -m factory.run --tag main --cap 30 --resume"
$R --models haiku --spec-level full  --trials 3 --change
$R --models haiku --spec-level brief --trials 3 --change
$R --models haiku --spec-level brief --trials 3 --designs ask
$R --models opus  --spec-level brief --trials 3 --designs oneshot,loop --change --run-cap 1.0
$R --models opus  --spec-level brief --trials 3 --designs pce --run-cap 2.0
$R --models opus  --spec-level full  --trials 1 --designs oneshot,loop --run-cap 1.0
$R --models opus  --spec-level brief --trials 3 --designs ask --run-cap 1.0
