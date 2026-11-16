# Report for tag `pilot`

34 finished runs, 0 errored, total model spend $2.59.

## Round 1: build from spec

By model and design:

| spec level | model | design | runs | public | holdout | gap | all holdout green | gamed | cost/run | time/run | model calls/run |
|---|---|---|---|---|---|---|---|---|---|---|---|
| brief | claude-haiku-5-5 | loop | 3 | 26/26 (100%) | 67/86 (78%) | 22 pts | 0 | 0 | $0.006 | 39s | 6.0 |
| brief | claude-haiku-5-5 | oneshot | 3 | 26/26 (100%) | 70/86 (81%) | 19 pts | 0 | 0 | $0.005 | 39s | 1.0 |
| brief | claude-haiku-5-5 | pce | 3 | 26/26 (100%) | 70/86 (81%) | 19 pts | 0 | 0 | $0.044 | 260s | 31.0 |
| brief | claude-opus-5-5 | loop | 3 | 26/26 (100%) | 72/86 (84%) | 16 pts | 0 | 0 | $0.209 | 69s | 5.3 |
| brief | claude-opus-5-5 | oneshot | 3 | 26/26 (100%) | 69/86 (80%) | 20 pts | 0 | 0 | $0.150 | 56s | 1.0 |
| brief | claude-opus-5-5 | pce | 1 | 8/8 (100%) | 19/26 (73%) | 27 pts | 0 | 0 | $1.018 | 306s | 28.0 |
| full | claude-haiku-5-5 | loop | 3 | 26/26 (100%) | 86/86 (100%) | 0 pts | 3 | 0 | $0.008 | 47s | 5.7 |
| full | claude-haiku-5-5 | oneshot | 3 | 26/26 (100%) | 86/86 (100%) | 0 pts | 3 | 0 | $0.006 | 47s | 1.0 |
| full | claude-haiku-5-5 | pce | 3 | 26/26 (100%) | 86/86 (100%) | 0 pts | 3 | 0 | $0.034 | 204s | 21.7 |

Holdout by scenario class (what the short ticket says about it):

| spec level | model | design | stated | implied | arbitrary |
|---|---|---|---|---|---|
| brief | claude-haiku-5-5 | loop | 24/25 (96%) | 27/32 (84%) | 16/29 (55%) |
| brief | claude-haiku-5-5 | oneshot | 25/25 (100%) | 27/32 (84%) | 18/29 (62%) |
| brief | claude-haiku-5-5 | pce | 25/25 (100%) | 27/32 (84%) | 18/29 (62%) |
| brief | claude-opus-5-5 | loop | 25/25 (100%) | 26/32 (81%) | 21/29 (72%) |
| brief | claude-opus-5-5 | oneshot | 25/25 (100%) | 26/32 (81%) | 18/29 (62%) |
| brief | claude-opus-5-5 | pce | 6/6 (100%) | 7/9 (78%) | 6/11 (55%) |

By spec, model and design:

| spec level | spec | model | design | runs | public | holdout | gap | all holdout green | gamed | cost/run | time/run | model calls/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| brief | bookings | claude-haiku-5-5 | loop | 1 | 10/10 (100%) | 28/35 (80%) | 20 pts | 0 | 0 | $0.008 | 45s | 7.0 |
| brief | bookings | claude-haiku-5-5 | oneshot | 1 | 10/10 (100%) | 31/35 (89%) | 11 pts | 0 | 0 | $0.007 | 46s | 1.0 |
| brief | bookings | claude-haiku-5-5 | pce | 1 | 10/10 (100%) | 28/35 (80%) | 20 pts | 0 | 0 | $0.051 | 300s | 28.0 |
| brief | bookings | claude-opus-5-5 | loop | 1 | 10/10 (100%) | 32/35 (91%) | 9 pts | 0 | 0 | $0.277 | 90s | 6.0 |
| brief | bookings | claude-opus-5-5 | oneshot | 1 | 10/10 (100%) | 30/35 (86%) | 14 pts | 0 | 0 | $0.204 | 75s | 1.0 |
| brief | sessionize | claude-haiku-5-5 | loop | 1 | 8/8 (100%) | 21/25 (84%) | 16 pts | 0 | 0 | $0.004 | 28s | 5.0 |
| brief | sessionize | claude-haiku-5-5 | oneshot | 1 | 8/8 (100%) | 21/25 (84%) | 16 pts | 0 | 0 | $0.005 | 38s | 1.0 |
| brief | sessionize | claude-haiku-5-5 | pce | 1 | 8/8 (100%) | 22/25 (88%) | 12 pts | 0 | 0 | $0.037 | 204s | 29.0 |
| brief | sessionize | claude-opus-5-5 | loop | 1 | 8/8 (100%) | 21/25 (84%) | 16 pts | 0 | 0 | $0.163 | 54s | 5.0 |
| brief | sessionize | claude-opus-5-5 | oneshot | 1 | 8/8 (100%) | 19/25 (76%) | 24 pts | 0 | 0 | $0.118 | 42s | 1.0 |
| brief | splitr | claude-haiku-5-5 | loop | 1 | 8/8 (100%) | 18/26 (69%) | 31 pts | 0 | 0 | $0.007 | 44s | 6.0 |
| brief | splitr | claude-haiku-5-5 | oneshot | 1 | 8/8 (100%) | 18/26 (69%) | 31 pts | 0 | 0 | $0.004 | 33s | 1.0 |
| brief | splitr | claude-haiku-5-5 | pce | 1 | 8/8 (100%) | 20/26 (77%) | 23 pts | 0 | 0 | $0.046 | 278s | 36.0 |
| brief | splitr | claude-opus-5-5 | loop | 1 | 8/8 (100%) | 19/26 (73%) | 27 pts | 0 | 0 | $0.187 | 62s | 5.0 |
| brief | splitr | claude-opus-5-5 | oneshot | 1 | 8/8 (100%) | 20/26 (77%) | 23 pts | 0 | 0 | $0.129 | 52s | 1.0 |
| brief | splitr | claude-opus-5-5 | pce | 1 | 8/8 (100%) | 19/26 (73%) | 27 pts | 0 | 0 | $1.018 | 306s | 28.0 |
| full | bookings | claude-haiku-5-5 | loop | 1 | 10/10 (100%) | 35/35 (100%) | 0 pts | 1 | 0 | $0.011 | 65s | 8.0 |
| full | bookings | claude-haiku-5-5 | oneshot | 1 | 10/10 (100%) | 35/35 (100%) | 0 pts | 1 | 0 | $0.009 | 65s | 1.0 |
| full | bookings | claude-haiku-5-5 | pce | 1 | 10/10 (100%) | 35/35 (100%) | 0 pts | 1 | 0 | $0.036 | 202s | 20.0 |
| full | sessionize | claude-haiku-5-5 | loop | 1 | 8/8 (100%) | 25/25 (100%) | 0 pts | 1 | 0 | $0.005 | 31s | 5.0 |
| full | sessionize | claude-haiku-5-5 | oneshot | 1 | 8/8 (100%) | 25/25 (100%) | 0 pts | 1 | 0 | $0.005 | 36s | 1.0 |
| full | sessionize | claude-haiku-5-5 | pce | 1 | 8/8 (100%) | 25/25 (100%) | 0 pts | 1 | 0 | $0.037 | 218s | 29.0 |
| full | splitr | claude-haiku-5-5 | loop | 1 | 8/8 (100%) | 26/26 (100%) | 0 pts | 1 | 0 | $0.007 | 46s | 4.0 |
| full | splitr | claude-haiku-5-5 | oneshot | 1 | 8/8 (100%) | 26/26 (100%) | 0 pts | 1 | 0 | $0.005 | 41s | 1.0 |
| full | splitr | claude-haiku-5-5 | pce | 1 | 8/8 (100%) | 26/26 (100%) | 0 pts | 1 | 0 | $0.029 | 191s | 16.0 |

Failed held-out scenarios per run:

- `20261116-225632-bookings-loop-haiku-brief-r1-t1`: holdout:test_room_name_trim_and_duplicate_ignoring_case, holdout:test_bad_json_and_non_object, holdout:test_timestamp_format_strict, holdout:test_booking_field_validation, holdout:test_title_trimmed, holdout:test_check_order_validation_before_room_before_capacity_before_conflict, holdout:test_availability_errors
- `20261116-225542-bookings-oneshot-haiku-brief-r1-t1`: holdout:test_room_name_trim_and_duplicate_ignoring_case, holdout:test_bad_json_and_non_object, holdout:test_booking_field_validation, holdout:test_title_trimmed
- `20261116-225719-bookings-pce-haiku-brief-r1-t1`: holdout:test_room_name_trim_and_duplicate_ignoring_case, holdout:test_room_validation_cases, holdout:test_bad_json_and_non_object, holdout:test_booking_field_validation, holdout:test_title_trimmed, holdout:test_check_order_validation_before_room_before_capacity_before_conflict, holdout:test_availability_errors
- `20261116-231024-bookings-loop-opus-brief-r1-t1`: holdout:test_bad_json_and_non_object, holdout:test_booking_field_validation, holdout:test_title_trimmed
- `20261116-230906-bookings-oneshot-opus-brief-r1-t1`: holdout:test_room_name_trim_and_duplicate_ignoring_case, holdout:test_bad_json_and_non_object, holdout:test_timestamp_format_strict, holdout:test_booking_field_validation, holdout:test_title_trimmed
- `20261116-230301-sessionize-loop-haiku-brief-r1-t1`: holdout:test_dedupe_keeps_earliest_timestamp, holdout:test_reject_reasons_and_order_of_checks, holdout:test_bad_timestamps, holdout:test_bad_amounts
- `20261116-230222-sessionize-oneshot-haiku-brief-r1-t1`: holdout:test_dedupe_keeps_earliest_timestamp, holdout:test_reject_reasons_and_order_of_checks, holdout:test_bad_timestamps, holdout:test_bad_amounts
- `20261116-230331-sessionize-pce-haiku-brief-r1-t1`: holdout:test_dedupe_keeps_earliest_timestamp, holdout:test_reject_reasons_and_order_of_checks, holdout:test_bad_timestamps
- `20261116-231240-sessionize-loop-opus-brief-r1-t1`: holdout:test_dedupe_keeps_earliest_timestamp, holdout:test_reject_reasons_and_order_of_checks, holdout:test_bad_timestamps, holdout:test_bad_amounts
- `20261116-231157-sessionize-oneshot-opus-brief-r1-t1`: holdout:test_offsets_and_fraction_truncated_in_output, holdout:test_duration_floor, holdout:test_dedupe_keeps_earliest_timestamp, holdout:test_reject_reasons_and_order_of_checks, holdout:test_bad_timestamps, holdout:test_bad_amounts
- `20261116-225018-splitr-loop-haiku-brief-r1-t1`: holdout:test_multiple_bad_rows_in_order_one_reason_each, holdout:test_bad_participants_forms, holdout:test_names_case_insensitive_first_spelling, holdout:test_sort_ignores_case, holdout:test_leftover_two_cents_alphabetical_ignoring_case, holdout:test_settle_ties_and_multiple_rounds, holdout:test_options_before_positionals, holdout:test_missing_header_column
- `20261116-224944-splitr-oneshot-haiku-brief-r1-t1`: holdout:test_comments_and_blank_lines_ignored, holdout:test_multiple_bad_rows_in_order_one_reason_each, holdout:test_bad_amounts, holdout:test_bad_participants_forms, holdout:test_names_case_insensitive_first_spelling, holdout:test_sort_ignores_case, holdout:test_leftover_two_cents_alphabetical_ignoring_case, holdout:test_settle_ties_and_multiple_rounds
- `20261116-225103-splitr-pce-haiku-brief-r1-t1`: holdout:test_comments_and_blank_lines_ignored, holdout:test_multiple_bad_rows_in_order_one_reason_each, holdout:test_bad_participants_forms, holdout:test_names_case_insensitive_first_spelling, holdout:test_sort_ignores_case, holdout:test_leftover_two_cents_alphabetical_ignoring_case
- `20261116-230803-splitr-loop-opus-brief-r1-t1`: holdout:test_comments_and_blank_lines_ignored, holdout:test_multiple_bad_rows_in_order_one_reason_each, holdout:test_bad_participants_forms, holdout:test_names_case_insensitive_first_spelling, holdout:test_sort_ignores_case, holdout:test_leftover_two_cents_alphabetical_ignoring_case, holdout:test_options_before_positionals
- `20261116-230710-splitr-oneshot-opus-brief-r1-t1`: holdout:test_multiple_bad_rows_in_order_one_reason_each, holdout:test_bad_participants_forms, holdout:test_names_case_insensitive_first_spelling, holdout:test_sort_ignores_case, holdout:test_leftover_two_cents_alphabetical_ignoring_case, holdout:test_options_before_positionals
- `20261116-231343-splitr-pce-opus-brief-r1-t1`: holdout:test_comments_and_blank_lines_ignored, holdout:test_multiple_bad_rows_in_order_one_reason_each, holdout:test_bad_participants_forms, holdout:test_names_case_insensitive_first_spelling, holdout:test_sort_ignores_case, holdout:test_leftover_two_cents_alphabetical_ignoring_case, holdout:test_options_before_positionals
- `20261116-222303-bookings-loop-haiku-r1-t1`: none
- `20261116-222119-bookings-oneshot-haiku-r1-t1`: none
- `20261116-222501-bookings-pce-haiku-r1-t1`: none
- `20261116-223727-sessionize-loop-haiku-r1-t1`: none
- `20261116-223624-sessionize-oneshot-haiku-r1-t1`: none
- `20261116-223832-sessionize-pce-haiku-r1-t1`: none
- `20261116-221335-splitr-loop-haiku-r1-t1`: none
- `20261116-221253-splitr-oneshot-haiku-r1-t1`: none
- `20261116-221538-splitr-pce-haiku-r1-t1`: none

## Round 2: change request on the shipped code

By model and design:

| spec level | model | design | runs | public | holdout | gap | regression | change | all holdout green | gamed | cost/run | time/run | model calls/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| full | claude-haiku-5-5 | loop | 3 | 36/36 (100%) | 130/130 (100%) | 0 pts | 85/85 | 45/45 | 3 | 0 | $0.006 | 33s | 6.7 |
| full | claude-haiku-5-5 | oneshot | 3 | 36/36 (100%) | 130/130 (100%) | 0 pts | 85/85 | 45/45 | 3 | 0 | $0.005 | 27s | 1.0 |
| full | claude-haiku-5-5 | pce | 3 | 36/36 (100%) | 130/130 (100%) | 0 pts | 85/85 | 45/45 | 3 | 0 | $0.051 | 291s | 36.7 |

By spec, model and design:

| spec level | spec | model | design | runs | public | holdout | gap | regression | change | all holdout green | gamed | cost/run | time/run | model calls/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| full | bookings | claude-haiku-5-5 | loop | 1 | 14/14 (100%) | 50/50 (100%) | 0 pts | 35/35 | 15/15 | 1 | 0 | $0.008 | 43s | 9.0 |
| full | bookings | claude-haiku-5-5 | oneshot | 1 | 14/14 (100%) | 50/50 (100%) | 0 pts | 35/35 | 15/15 | 1 | 0 | $0.006 | 30s | 1.0 |
| full | bookings | claude-haiku-5-5 | pce | 1 | 14/14 (100%) | 50/50 (100%) | 0 pts | 35/35 | 15/15 | 1 | 0 | $0.079 | 469s | 47.0 |
| full | sessionize | claude-haiku-5-5 | loop | 1 | 11/11 (100%) | 40/40 (100%) | 0 pts | 24/24 | 16/16 | 1 | 0 | $0.005 | 28s | 5.0 |
| full | sessionize | claude-haiku-5-5 | oneshot | 1 | 11/11 (100%) | 40/40 (100%) | 0 pts | 24/24 | 16/16 | 1 | 0 | $0.004 | 22s | 1.0 |
| full | sessionize | claude-haiku-5-5 | pce | 1 | 11/11 (100%) | 40/40 (100%) | 0 pts | 24/24 | 16/16 | 1 | 0 | $0.047 | 260s | 38.0 |
| full | splitr | claude-haiku-5-5 | loop | 1 | 11/11 (100%) | 40/40 (100%) | 0 pts | 26/26 | 14/14 | 1 | 0 | $0.005 | 26s | 6.0 |
| full | splitr | claude-haiku-5-5 | oneshot | 1 | 11/11 (100%) | 40/40 (100%) | 0 pts | 26/26 | 14/14 | 1 | 0 | $0.005 | 29s | 1.0 |
| full | splitr | claude-haiku-5-5 | pce | 1 | 11/11 (100%) | 40/40 (100%) | 0 pts | 26/26 | 14/14 | 1 | 0 | $0.027 | 144s | 25.0 |

Failed held-out scenarios per run:

- `20261116-222411-bookings-loop-haiku-r2-t1`: none
- `20261116-222228-bookings-oneshot-haiku-r2-t1`: none
- `20261116-222828-bookings-pce-haiku-r2-t1`: none
- `20261116-223802-sessionize-loop-haiku-r2-t1`: none
- `20261116-223703-sessionize-oneshot-haiku-r2-t1`: none
- `20261116-224212-sessionize-pce-haiku-r2-t1`: none
- `20261116-221510-splitr-loop-haiku-r2-t1`: none
- `20261116-221438-splitr-oneshot-haiku-r2-t1`: none
- `20261116-221852-splitr-pce-haiku-r2-t1`: none

## Gaming and leak checks

No run modified or deleted its tests, hard-coded example data, sniffed the test runner, or contained the holdout canary.
