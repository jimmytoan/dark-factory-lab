# Sources: what was checked, and how

Checked on 2026-11-16. "Primary" means the page itself was fetched and read; "secondary" means only reporting about it was seen.

| Claim | Status | Source |
| --- | --- | --- |
| "Dark factory" as the top level of AI-assisted programming comes from Dan Shapiro's essay "The Five Levels: from Spicy Autocomplete to the Dark Factory", dated 2026-01-23. Level 5 is "a black box that turns specs into software"; the factory is dark because humans are "neither needed nor welcome". He says it is done by "small teams, less than five people" and that 90% of "AI-native" developers are at level 2. | Primary | https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ |
| The essay does not name StrongDM and does not itself say that humans do not review code at level 5 (it only talks about review at level 3). | Primary | same |
| StrongDM's AI team (Justin McCarthy, Jay Taylor, Navan Chauhan, founded 2025-07-14) works under two rules: code must not be written by humans, and code must not be reviewed by humans. | Primary | https://factory.strongdm.ai/ |
| StrongDM validates with "scenarios": end-to-end user stories "often stored outside the codebase (similar to a 'holdout' set in model training)", scored by "satisfaction", the share of observed trajectories that likely satisfy the user. They also build a "Digital Twin Universe" of third-party services. | Primary | same |
| StrongDM: "If you haven't spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement." | Primary | same |
| "Three person team" is Simon Willison's description after visiting in October 2025, not a number on StrongDM's page. Willison also questions the no-review rule and the cost. | Primary (Willison's post) | https://simonwillison.net/2026/Feb/7/software-factory/ |
| Dex Horthy (HumanLayer), "Why Software Factories Fail (or: harness engineering is not enough)": "the lights off factory does not work"; models erode maintainability because "there is no penalty" for it in training. HumanLayer went lights-off in July 2025, hit repeated incidents, and decided on a rewrite in November 2025. Recommendation: keep reading the code, front-load planning, build in reviewed vertical slices. | Primary (no date on the page; codebase size not stated there) | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md |
| The "30,000 to 40,000 line codebase" figure for HumanLayer. | Secondary only, not verified | search results summarising interviews |
| Anthropic, "Harness design for long-running application development" (Prithvi Rajasekaran, 2026-03-24): planner, generator, evaluator. Agents grading their own work "confidently praise" it; a separate, skeptical evaluator is the stronger lever. Solo run 20 min / $9, full harness 6 hr / $200 (Opus 4.5); a later run 3 hr 50 min / $124.70 (Opus 4.6). | Primary | https://www.anthropic.com/engineering/harness-design-long-running-apps |
| OpenAI, "Harness engineering: leveraging Codex in an agent-first world" (Ryan Lopopolo, 2026-02-11), about a product of roughly a million lines with no hand-written code. | NOT verified: the page returned HTTP 403 to the fetch tool. Only titles and secondary summaries were seen. Do not quote numbers from it without opening it in a browser. | https://openai.com/index/harness-engineering/ |

Differences between this lab and the real thing, to state in any write-up:

- StrongDM's scenarios are judged probabilistically by a model ("satisfaction"). Here the holdout is deterministic pytest scenarios, because the task was grading by script.
- The specs here are small (100 to 300 lines of product code), greenfield, single file. Horthy's criticism is about months of change on a large codebase. One change round is a weak proxy for that.
- No digital twins: the products have no third-party dependencies.
