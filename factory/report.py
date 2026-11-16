"""Aggregate results/runs.jsonl into markdown tables.   uv run python -m factory.report --tag pilot"""
import argparse
from collections import defaultdict

from .run import load_runs


def pct(p, t):
    return f"{100 * p / t:.0f}%" if t else "-"


def table(rows, header):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def agg(runs, keyf, change):
    groups = defaultdict(list)
    for r in runs:
        groups[keyf(r)].append(r)
    rows = []
    for key in sorted(groups):
        rs = groups[key]
        s = lambda suite, f: sum(r["grade"][suite][f] for r in rs)
        row = list(key) + [len(rs), f"{s('public', 'passed')}/{s('public', 'total')} ({pct(s('public', 'passed'), s('public', 'total'))})",
                           f"{s('holdout', 'passed')}/{s('holdout', 'total')} ({pct(s('holdout', 'passed'), s('holdout', 'total'))})",
                           f"{100 * (s('public', 'passed') / s('public', 'total') - s('holdout', 'passed') / s('holdout', 'total')):.0f} pts"]
        if change:
            row += [f"{s('regression', 'passed')}/{s('regression', 'total')}", f"{s('change', 'passed')}/{s('change', 'total')}"]
        row += [sum(1 for r in rs if r["grade"]["holdout"]["passed"] == r["grade"]["holdout"]["total"]),
                sum(1 for r in rs if r["gaming"]["gamed"]),
                f"${sum(r['usage']['cost_usd'] for r in rs) / len(rs):.3f}",
                f"{sum(r['elapsed_s'] for r in rs) / len(rs):.0f}s",
                f"{sum(r['factory']['iterations'] for r in rs) / len(rs):.1f}"]
        rows.append(row)
    return rows


def class_table(rs):
    groups = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for r in rs:
        for cls, v in r["grade"]["holdout"].get("by_class", {}).items():
            g = groups[(r.get("spec_level", "full"), r["model"], r["design"])][cls]
            g[0] += v["passed"]
            g[1] += v["total"]
    rows = [list(k) + [f"{g[c][0]}/{g[c][1]} ({pct(*g[c])})" for c in ("stated", "implied", "arbitrary")] for k, g in sorted(groups.items())]
    return table(rows, ["spec level", "model", "design", "stated", "implied", "arbitrary"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    a = ap.parse_args()
    allr = [r for r in load_runs() if r["tag"] == a.tag]
    runs = [r for r in allr if r["error"] is None]
    print(f"# Report for tag `{a.tag}`\n\n{len(runs)} finished runs, {len(allr) - len(runs)} errored, "
          f"total model spend ${sum(r['usage']['cost_usd'] for r in allr):.2f}.\n")
    tail = ["all holdout green", "gamed", "cost/run", "time/run", "model calls/run"]
    for rnd, title in ((1, "Round 1: build from spec"), (2, "Round 2: change request on the shipped code")):
        rs = [r for r in runs if r["round"] == rnd]
        if not rs:
            continue
        mid = ["public", "holdout", "gap"] + (["regression", "change"] if rnd == 2 else [])
        print(f"## {title}\n\nBy model and design:\n")
        print(table(agg(rs, lambda r: (r.get("spec_level", "full"), r["model"], r["design"]), rnd == 2), ["spec level", "model", "design", "runs"] + mid + tail))
        if rnd == 1:
            print("\nHoldout by scenario class (what the short ticket says about it):\n")
            print(class_table(rs))
        print("\nBy spec, model and design:\n")
        print(table(agg(rs, lambda r: (r.get("spec_level", "full"), r["spec"], r["model"], r["design"]), rnd == 2), ["spec level", "spec", "model", "design", "runs"] + mid + tail))
        print("\nFailed held-out scenarios per run:\n")
        for r in sorted(rs, key=lambda r: (r.get("spec_level", "full"), r["spec"], r["model"], r["design"], r["trial"])):
            failed = []
            for suite in ("holdout", "regression", "change"):
                failed += [f"{suite}:{n}" for n in r["grade"].get(suite, {}).get("failed", [])]
            print(f"- `{r['run_id']}`: " + (", ".join(failed) if failed else "none"))
        print()
    gamed = [r for r in runs if r["gaming"]["gamed"] or r["gaming"]["canary_in_workspace"] or r["gaming"]["canary_in_transcript"]]
    print("## Gaming and leak checks\n")
    if not gamed:
        print("No run modified or deleted its tests, hard-coded example data, sniffed the test runner, or contained the holdout canary.")
    for r in gamed:
        print(f"- `{r['run_id']}`: " + ", ".join(f"{k}={v}" for k, v in r["gaming"].items() if v))


if __name__ == "__main__":
    main()
