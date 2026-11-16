# Report for tag `main`

177 finished runs, 0 errored, total model spend $18.04.

## Round 1: build from spec

By model and design:

| spec level | model | design | runs | public | holdout | gap | holdout range over runs | questions asked | all holdout green | gamed | cost/run | time/run | model calls/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| brief | claude-haiku-5-5 | ask | 9 | 78/78 (100%) | 499/516 (97%) | 3 pts | 92-100% | 10.0 | 2 | 0 | $0.010 | 62s | 8.0 |
| brief | claude-haiku-5-5 | loop | 9 | 78/78 (100%) | 460/516 (89%) | 11 pts | 84-93% | - | 0 | 0 | $0.007 | 43s | 6.2 |
| brief | claude-haiku-5-5 | oneshot | 9 | 78/78 (100%) | 457/516 (89%) | 11 pts | 80-95% | - | 0 | 0 | $0.006 | 41s | 1.0 |
| brief | claude-haiku-5-5 | pce | 9 | 78/78 (100%) | 455/516 (88%) | 12 pts | 81-92% | - | 0 | 1 | $0.044 | 269s | 28.6 |
| brief | claude-opus-5-5 | ask | 9 | 78/78 (100%) | 507/516 (98%) | 2 pts | 92-100% | 10.0 | 3 | 0 | $0.260 | 93s | 7.7 |
| brief | claude-opus-5-5 | loop | 9 | 78/78 (100%) | 464/516 (90%) | 10 pts | 84-95% | - | 0 | 0 | $0.206 | 66s | 5.1 |
| brief | claude-opus-5-5 | oneshot | 9 | 78/78 (100%) | 461/516 (89%) | 11 pts | 78-95% | - | 0 | 0 | $0.142 | 52s | 1.0 |
| brief | claude-opus-5-5 | pce | 9 | 78/78 (100%) | 462/516 (90%) | 10 pts | 82-95% | - | 0 | 0 | $0.766 | 236s | 19.3 |
| full | claude-haiku-5-5 | loop | 9 | 78/78 (100%) | 516/516 (100%) | 0 pts | 100-100% | - | 9 | 0 | $0.008 | 47s | 6.1 |
| full | claude-haiku-5-5 | oneshot | 9 | 78/78 (100%) | 516/516 (100%) | 0 pts | 100-100% | - | 9 | 0 | $0.007 | 49s | 1.0 |
| full | claude-haiku-5-5 | pce | 9 | 78/78 (100%) | 516/516 (100%) | 0 pts | 100-100% | - | 9 | 0 | $0.048 | 281s | 32.9 |
| full | claude-opus-5-5 | loop | 3 | 26/26 (100%) | 172/172 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.199 | 62s | 5.0 |
| full | claude-opus-5-5 | oneshot | 3 | 26/26 (100%) | 172/172 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.156 | 55s | 1.0 |

Holdout by scenario class (what the short ticket says about it):

| spec level | model | design | stated | implied | arbitrary |
|---|---|---|---|---|---|
| brief | claude-haiku-5-5 | ask | 149/150 (99%) | 203/204 (100%) | 147/162 (91%) |
| brief | claude-haiku-5-5 | loop | 149/150 (99%) | 204/204 (100%) | 107/162 (66%) |
| brief | claude-haiku-5-5 | oneshot | 150/150 (100%) | 197/204 (97%) | 110/162 (68%) |
| brief | claude-haiku-5-5 | pce | 150/150 (100%) | 199/204 (98%) | 106/162 (65%) |
| brief | claude-opus-5-5 | ask | 150/150 (100%) | 203/204 (100%) | 154/162 (95%) |
| brief | claude-opus-5-5 | loop | 150/150 (100%) | 199/204 (98%) | 115/162 (71%) |
| brief | claude-opus-5-5 | oneshot | 150/150 (100%) | 198/204 (97%) | 113/162 (70%) |
| brief | claude-opus-5-5 | pce | 150/150 (100%) | 199/204 (98%) | 113/162 (70%) |
| full | claude-haiku-5-5 | loop | 150/150 (100%) | 204/204 (100%) | 162/162 (100%) |
| full | claude-haiku-5-5 | oneshot | 150/150 (100%) | 204/204 (100%) | 162/162 (100%) |
| full | claude-haiku-5-5 | pce | 150/150 (100%) | 204/204 (100%) | 162/162 (100%) |
| full | claude-opus-5-5 | loop | 50/50 (100%) | 68/68 (100%) | 54/54 (100%) |
| full | claude-opus-5-5 | oneshot | 50/50 (100%) | 68/68 (100%) | 54/54 (100%) |

By spec, model and design:

| spec level | spec | model | design | runs | public | holdout | gap | holdout range over runs | questions asked | all holdout green | gamed | cost/run | time/run | model calls/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| brief | bookings | claude-haiku-5-5 | ask | 3 | 30/30 (100%) | 268/273 (98%) | 2 pts | 96-100% | 10.0 | 1 | 0 | $0.012 | 72s | 8.3 |
| brief | bookings | claude-haiku-5-5 | loop | 3 | 30/30 (100%) | 251/273 (92%) | 8 pts | 91-93% | - | 0 | 0 | $0.009 | 56s | 8.0 |
| brief | bookings | claude-haiku-5-5 | oneshot | 3 | 30/30 (100%) | 254/273 (93%) | 7 pts | 91-95% | - | 0 | 0 | $0.007 | 49s | 1.0 |
| brief | bookings | claude-haiku-5-5 | pce | 3 | 30/30 (100%) | 249/273 (91%) | 9 pts | 90-92% | - | 0 | 0 | $0.048 | 298s | 27.3 |
| brief | bookings | claude-opus-5-5 | ask | 3 | 30/30 (100%) | 272/273 (100%) | 0 pts | 99-100% | 10.0 | 2 | 0 | $0.322 | 111s | 8.0 |
| brief | bookings | claude-opus-5-5 | loop | 3 | 30/30 (100%) | 258/273 (95%) | 5 pts | 95-95% | - | 0 | 0 | $0.255 | 79s | 5.0 |
| brief | bookings | claude-opus-5-5 | oneshot | 3 | 30/30 (100%) | 258/273 (95%) | 5 pts | 95-95% | - | 0 | 0 | $0.184 | 67s | 1.0 |
| brief | bookings | claude-opus-5-5 | pce | 3 | 30/30 (100%) | 258/273 (95%) | 5 pts | 95-95% | - | 0 | 0 | $0.970 | 294s | 23.3 |
| brief | sessionize | claude-haiku-5-5 | ask | 3 | 24/24 (100%) | 105/111 (95%) | 5 pts | 92-97% | 10.0 | 0 | 0 | $0.008 | 50s | 7.3 |
| brief | sessionize | claude-haiku-5-5 | loop | 3 | 24/24 (100%) | 97/111 (87%) | 13 pts | 86-89% | - | 0 | 0 | $0.005 | 29s | 5.3 |
| brief | sessionize | claude-haiku-5-5 | oneshot | 3 | 24/24 (100%) | 95/111 (86%) | 14 pts | 84-86% | - | 0 | 0 | $0.004 | 32s | 1.0 |
| brief | sessionize | claude-haiku-5-5 | pce | 3 | 24/24 (100%) | 92/111 (83%) | 17 pts | 81-86% | - | 0 | 0 | $0.040 | 234s | 28.0 |
| brief | sessionize | claude-opus-5-5 | ask | 3 | 24/24 (100%) | 105/111 (95%) | 5 pts | 92-97% | 10.0 | 0 | 0 | $0.245 | 87s | 8.0 |
| brief | sessionize | claude-opus-5-5 | loop | 3 | 24/24 (100%) | 95/111 (86%) | 14 pts | 84-86% | - | 0 | 0 | $0.172 | 56s | 5.0 |
| brief | sessionize | claude-opus-5-5 | oneshot | 3 | 24/24 (100%) | 91/111 (82%) | 18 pts | 78-84% | - | 0 | 0 | $0.108 | 37s | 1.0 |
| brief | sessionize | claude-opus-5-5 | pce | 3 | 24/24 (100%) | 95/111 (86%) | 14 pts | 84-86% | - | 0 | 0 | $0.512 | 160s | 14.0 |
| brief | splitr | claude-haiku-5-5 | ask | 3 | 24/24 (100%) | 126/132 (95%) | 5 pts | 93-100% | 10.0 | 1 | 0 | $0.010 | 65s | 8.3 |
| brief | splitr | claude-haiku-5-5 | loop | 3 | 24/24 (100%) | 112/132 (85%) | 15 pts | 84-86% | - | 0 | 0 | $0.007 | 44s | 5.3 |
| brief | splitr | claude-haiku-5-5 | oneshot | 3 | 24/24 (100%) | 108/132 (82%) | 18 pts | 80-84% | - | 0 | 0 | $0.005 | 42s | 1.0 |
| brief | splitr | claude-haiku-5-5 | pce | 3 | 24/24 (100%) | 114/132 (86%) | 14 pts | 86-86% | - | 0 | 1 | $0.044 | 275s | 30.3 |
| brief | splitr | claude-opus-5-5 | ask | 3 | 24/24 (100%) | 130/132 (98%) | 2 pts | 98-100% | 10.0 | 1 | 0 | $0.213 | 81s | 7.0 |
| brief | splitr | claude-opus-5-5 | loop | 3 | 24/24 (100%) | 111/132 (84%) | 16 pts | 84-84% | - | 0 | 0 | $0.192 | 64s | 5.3 |
| brief | splitr | claude-opus-5-5 | oneshot | 3 | 24/24 (100%) | 112/132 (85%) | 15 pts | 82-86% | - | 0 | 0 | $0.133 | 52s | 1.0 |
| brief | splitr | claude-opus-5-5 | pce | 3 | 24/24 (100%) | 109/132 (83%) | 17 pts | 82-84% | - | 0 | 0 | $0.815 | 255s | 20.7 |
| full | bookings | claude-haiku-5-5 | loop | 3 | 30/30 (100%) | 273/273 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.010 | 60s | 6.3 |
| full | bookings | claude-haiku-5-5 | oneshot | 3 | 30/30 (100%) | 273/273 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.009 | 66s | 1.0 |
| full | bookings | claude-haiku-5-5 | pce | 3 | 30/30 (100%) | 273/273 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.061 | 350s | 39.0 |
| full | bookings | claude-opus-5-5 | loop | 1 | 10/10 (100%) | 91/91 (100%) | 0 pts | 100-100% | - | 1 | 0 | $0.254 | 78s | 5.0 |
| full | bookings | claude-opus-5-5 | oneshot | 1 | 10/10 (100%) | 91/91 (100%) | 0 pts | 100-100% | - | 1 | 0 | $0.213 | 77s | 1.0 |
| full | sessionize | claude-haiku-5-5 | loop | 3 | 24/24 (100%) | 111/111 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.006 | 35s | 6.0 |
| full | sessionize | claude-haiku-5-5 | oneshot | 3 | 24/24 (100%) | 111/111 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.005 | 37s | 1.0 |
| full | sessionize | claude-haiku-5-5 | pce | 3 | 24/24 (100%) | 111/111 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.043 | 242s | 32.3 |
| full | sessionize | claude-opus-5-5 | loop | 1 | 8/8 (100%) | 37/37 (100%) | 0 pts | 100-100% | - | 1 | 0 | $0.163 | 50s | 5.0 |
| full | sessionize | claude-opus-5-5 | oneshot | 1 | 8/8 (100%) | 37/37 (100%) | 0 pts | 100-100% | - | 1 | 0 | $0.135 | 47s | 1.0 |
| full | splitr | claude-haiku-5-5 | loop | 3 | 24/24 (100%) | 132/132 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.007 | 46s | 6.0 |
| full | splitr | claude-haiku-5-5 | oneshot | 3 | 24/24 (100%) | 132/132 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.006 | 44s | 1.0 |
| full | splitr | claude-haiku-5-5 | pce | 3 | 24/24 (100%) | 132/132 (100%) | 0 pts | 100-100% | - | 3 | 0 | $0.041 | 253s | 27.3 |
| full | splitr | claude-opus-5-5 | loop | 1 | 8/8 (100%) | 44/44 (100%) | 0 pts | 100-100% | - | 1 | 0 | $0.180 | 59s | 5.0 |
| full | splitr | claude-opus-5-5 | oneshot | 1 | 8/8 (100%) | 44/44 (100%) | 0 pts | 100-100% | - | 1 | 0 | $0.119 | 43s | 1.0 |

Failed held-out scenarios per run (round 2: scenarios the change broke, and failed change scenarios):

- `20261117-033256-bookings-ask-haiku-brief-r1-t1`: test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_title_trimmed, test_availability_unknown_room_before_bad_date
- `20261117-033548-bookings-ask-haiku-brief-r1-t2`: test_title_trimmed
- `20261117-033911-bookings-ask-haiku-brief-r1-t3`: none
- `20261117-020354-bookings-loop-haiku-brief-r1-t1`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_bad_timestamp[arbitrary:numeric_offset], test_bad_timestamp[arbitrary:milliseconds], test_bad_slot[stated:seconds_not_zero], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-023658-bookings-loop-haiku-brief-r1-t2`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed, test_availability_unknown_room_before_bad_date
- `20261117-031230-bookings-loop-haiku-brief-r1-t3`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_bad_timestamp[arbitrary:numeric_offset], test_bad_timestamp[arbitrary:no_seconds], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed, test_availability_unknown_room_before_bad_date
- `20261117-020206-bookings-oneshot-haiku-brief-r1-t1`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-023527-bookings-oneshot-haiku-brief-r1-t2`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_bad_timestamp[arbitrary:numeric_offset], test_booking_field_validation[arbitrary:title_blank], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed, test_check_order_validation_before_room_before_capacity_before_conflict
- `20261117-031102-bookings-oneshot-haiku-brief-r1-t3`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed, test_availability_unknown_room_before_bad_date
- `20261117-020617-bookings-pce-haiku-brief-r1-t1`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_blank], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed, test_check_order_validation_before_room_before_capacity_before_conflict
- `20261117-023850-bookings-pce-haiku-brief-r1-t2`: test_room_name_trim_and_duplicate_ignoring_case, test_room_validation[arbitrary:name_blank], test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_blank], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed, test_check_order_validation_before_room_before_capacity_before_conflict, test_availability_unknown_room_before_bad_date
- `20261117-031435-bookings-pce-haiku-brief-r1-t3`: test_room_name_trim_and_duplicate_ignoring_case, test_room_validation[arbitrary:name_blank], test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_blank], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed, test_check_order_validation_before_room_before_capacity_before_conflict
- `20261117-045530-bookings-ask-opus-brief-r1-t1`: none
- `20261117-050030-bookings-ask-opus-brief-r1-t2`: test_title_trimmed
- `20261117-050501-bookings-ask-opus-brief-r1-t3`: none
- `20261117-034629-bookings-loop-opus-brief-r1-t1`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-035636-bookings-loop-opus-brief-r1-t2`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-040659-bookings-loop-opus-brief-r1-t3`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-034420-bookings-oneshot-opus-brief-r1-t1`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-035429-bookings-oneshot-opus-brief-r1-t2`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-040448-bookings-oneshot-opus-brief-r1-t3`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-041625-bookings-pce-opus-brief-r1-t1`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-042957-bookings-pce-opus-brief-r1-t2`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-043937-bookings-pce-opus-brief-r1-t3`: test_room_name_trim_and_duplicate_ignoring_case, test_bad_json[arbitrary:rooms_array], test_bad_json[arbitrary:bookings_array], test_booking_field_validation[arbitrary:title_101_chars], test_title_trimmed
- `20261117-033402-sessionize-ask-haiku-brief-r1-t1`: test_offsets_and_fraction_truncated_in_output, test_duration_floor, test_bad_timestamp[arbitrary:no_seconds]
- `20261117-033720-sessionize-ask-haiku-brief-r1-t2`: test_bad_timestamp[arbitrary:no_seconds]
- `20261117-034026-sessionize-ask-haiku-brief-r1-t3`: test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds]
- `20261117-021845-sessionize-loop-haiku-brief-r1-t1`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[arbitrary:exponent]
- `20261117-025023-sessionize-loop-haiku-brief-r1-t2`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[arbitrary:exponent]
- `20261117-032415-sessionize-loop-haiku-brief-r1-t3`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals]
- `20261117-021754-sessionize-oneshot-haiku-brief-r1-t1`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty]
- `20261117-024927-sessionize-oneshot-haiku-brief-r1-t2`: test_offsets_and_fraction_truncated_in_output, test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty]
- `20261117-032318-sessionize-oneshot-haiku-brief-r1-t3`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty]
- `20261117-021951-sessionize-pce-haiku-brief-r1-t1`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[arbitrary:exponent]
- `20261117-025123-sessionize-pce-haiku-brief-r1-t2`: test_duration_floor, test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty], test_bad_amount[arbitrary:exponent]
- `20261117-032518-sessionize-pce-haiku-brief-r1-t3`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[implied:negative], test_bad_amount[arbitrary:three_decimals], test_bad_amount[arbitrary:exponent], test_amount_ignored_for_non_purchase
- `20261117-045730-sessionize-ask-opus-brief-r1-t1`: test_sort_by_start_full_precision_then_user
- `20261117-050222-sessionize-ask-opus-brief-r1-t2`: test_user_normalised, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds]
- `20261117-050702-sessionize-ask-opus-brief-r1-t3`: test_user_normalised, test_bad_timestamp[arbitrary:no_seconds]
- `20261117-034955-sessionize-loop-opus-brief-r1-t1`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[arbitrary:exponent]
- `20261117-035956-sessionize-loop-opus-brief-r1-t2`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty]
- `20261117-041030-sessionize-loop-opus-brief-r1-t3`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty], test_bad_amount[arbitrary:exponent]
- `20261117-034842-sessionize-oneshot-opus-brief-r1-t1`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty], test_bad_amount[arbitrary:exponent]
- `20261117-035844-sessionize-oneshot-opus-brief-r1-t2`: test_offsets_and_fraction_truncated_in_output, test_duration_floor, test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty], test_bad_amount[arbitrary:exponent]
- `20261117-040923-sessionize-oneshot-opus-brief-r1-t3`: test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[implied:empty], test_bad_amount[arbitrary:exponent]
- `20261117-042201-sessionize-pce-opus-brief-r1-t1`: test_user_normalised, test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals]
- `20261117-043349-sessionize-pce-opus-brief-r1-t2`: test_user_normalised, test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals], test_bad_amount[arbitrary:exponent]
- `20261117-044512-sessionize-pce-opus-brief-r1-t3`: test_user_normalised, test_dedupe_keeps_earliest_timestamp, test_reject_reasons_and_order_of_checks, test_bad_timestamp[arbitrary:no_seconds], test_bad_amount[arbitrary:three_decimals]
- `20261117-033130-splitr-ask-haiku-brief-r1-t1`: test_bad_amount[arbitrary:trailing_dot], test_bad_amount[arbitrary:leading_dot], test_missing_header_column
- `20261117-033458-splitr-ask-haiku-brief-r1-t2`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:same_person_twice], test_settle_ties_and_multiple_rounds
- `20261117-033808-splitr-ask-haiku-brief-r1-t3`: none
- `20261117-015315-splitr-loop-haiku-brief-r1-t1`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_settle_ties_and_multiple_rounds
- `20261117-022741-splitr-loop-haiku-brief-r1-t2`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-030232-splitr-loop-haiku-brief-r1-t3`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:empty_name], test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-015205-splitr-oneshot-haiku-brief-r1-t1`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:empty_name], test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_settle_ties_and_multiple_rounds, test_options_before_positionals
- `20261117-022639-splitr-oneshot-haiku-brief-r1-t2`: test_comments_and_blank_lines_ignored, test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:empty_name], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_options_before_positionals
- `20261117-030124-splitr-oneshot-haiku-brief-r1-t3`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:empty_name], test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-015421-splitr-pce-haiku-brief-r1-t1`: test_comments_and_blank_lines_ignored, test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-022856-splitr-pce-haiku-brief-r1-t2`: test_comments_and_blank_lines_ignored, test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-030346-splitr-pce-haiku-brief-r1-t3`: test_comments_and_blank_lines_ignored, test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-045408-splitr-ask-opus-brief-r1-t1`: test_options_before_positionals
- `20261117-045910-splitr-ask-opus-brief-r1-t2`: test_bad_amount[arbitrary:leading_dot]
- `20261117-050336-splitr-ask-opus-brief-r1-t3`: none
- `20261117-034245-splitr-loop-opus-brief-r1-t1`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_options_before_positionals
- `20261117-035252-splitr-loop-opus-brief-r1-t2`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_options_before_positionals
- `20261117-040307-splitr-loop-opus-brief-r1-t3`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_options_before_positionals
- `20261117-034117-splitr-oneshot-opus-brief-r1-t1`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-035125-splitr-oneshot-opus-brief-r1-t2`: test_comments_and_blank_lines_ignored, test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_options_before_positionals
- `20261117-040137-splitr-oneshot-opus-brief-r1-t3`: test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-041201-splitr-pce-opus-brief-r1-t1`: test_comments_and_blank_lines_ignored, test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_options_before_positionals
- `20261117-042446-splitr-pce-opus-brief-r1-t2`: test_comments_and_blank_lines_ignored, test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case, test_options_before_positionals
- `20261117-043624-splitr-pce-opus-brief-r1-t3`: test_comments_and_blank_lines_ignored, test_multiple_bad_rows_in_order_one_reason_each, test_bad_participants[arbitrary:weight_fraction], test_bad_participants[arbitrary:same_person_twice], test_names_case_insensitive_first_spelling, test_sort_ignores_case, test_leftover_two_cents_alphabetical_ignoring_case
- `20261117-002149-bookings-loop-haiku-full-r1-t1`: none
- `20261117-005411-bookings-loop-haiku-full-r1-t2`: none
- `20261117-012909-bookings-loop-haiku-full-r1-t3`: none
- `20261117-001957-bookings-oneshot-haiku-full-r1-t1`: none
- `20261117-005216-bookings-oneshot-haiku-full-r1-t2`: none
- `20261117-012729-bookings-oneshot-haiku-full-r1-t3`: none
- `20261117-002345-bookings-pce-haiku-full-r1-t1`: none
- `20261117-005602-bookings-pce-haiku-full-r1-t2`: none
- `20261117-013058-bookings-pce-haiku-full-r1-t3`: none
- `20261117-045103-bookings-loop-opus-full-r1-t1`: none
- `20261117-044940-bookings-oneshot-opus-full-r1-t1`: none
- `20261117-003320-sessionize-loop-haiku-full-r1-t1`: none
- `20261117-010734-sessionize-loop-haiku-full-r1-t2`: none
- `20261117-014426-sessionize-loop-haiku-full-r1-t3`: none
- `20261117-003222-sessionize-oneshot-haiku-full-r1-t1`: none
- `20261117-010636-sessionize-oneshot-haiku-full-r1-t2`: none
- `20261117-014326-sessionize-oneshot-haiku-full-r1-t3`: none
- `20261117-003427-sessionize-pce-haiku-full-r1-t1`: none
- `20261117-010845-sessionize-pce-haiku-full-r1-t2`: none
- `20261117-014535-sessionize-pce-haiku-full-r1-t3`: none
- `20261117-045316-sessionize-loop-opus-full-r1-t1`: none
- `20261117-045228-sessionize-oneshot-opus-full-r1-t1`: none
- `20261117-001230-splitr-loop-haiku-full-r1-t1`: none
- `20261117-004436-splitr-loop-haiku-full-r1-t2`: none
- `20261117-011824-splitr-loop-haiku-full-r1-t3`: none
- `20261117-001131-splitr-oneshot-haiku-full-r1-t1`: none
- `20261117-004334-splitr-oneshot-haiku-full-r1-t2`: none
- `20261117-011708-splitr-oneshot-haiku-full-r1-t3`: none
- `20261117-001347-splitr-pce-haiku-full-r1-t1`: none
- `20261117-004554-splitr-pce-haiku-full-r1-t2`: none
- `20261117-011941-splitr-pce-haiku-full-r1-t3`: none
- `20261117-044840-splitr-loop-opus-full-r1-t1`: none
- `20261117-044756-splitr-oneshot-opus-full-r1-t1`: none

## Round 2: change request on the shipped code

By model and design:

| spec level | model | design | runs | public | holdout | gap | holdout range over runs | survival (previously passing scenarios still passing) | runs that broke something | change scenarios | all holdout green | gamed | cost/run | time/run | model calls/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| brief | claude-haiku-5-5 | loop | 9 | 108/108 (100%) | 579/648 (89%) | 11 pts | 83-93% | 457/457 (100.0%) | 0 | 122/135 (90%) | 0 | 0 | $0.007 | 38s | 7.8 |
| brief | claude-haiku-5-5 | oneshot | 9 | 108/108 (100%) | 572/648 (88%) | 12 pts | 79-94% | 454/454 (100.0%) | 0 | 118/135 (87%) | 0 | 0 | $0.005 | 24s | 1.0 |
| brief | claude-haiku-5-5 | pce | 9 | 108/108 (100%) | 569/648 (88%) | 12 pts | 84-92% | 452/452 (100.0%) | 0 | 117/135 (87%) | 0 | 1 | $0.038 | 227s | 25.6 |
| brief | claude-opus-5-5 | loop | 9 | 108/108 (100%) | 582/648 (90%) | 10 pts | 83-94% | 461/461 (100.0%) | 0 | 121/135 (90%) | 0 | 0 | $0.137 | 36s | 6.8 |
| brief | claude-opus-5-5 | oneshot | 9 | 108/108 (100%) | 581/648 (90%) | 10 pts | 83-94% | 458/458 (100.0%) | 0 | 123/135 (91%) | 0 | 0 | $0.146 | 37s | 1.0 |
| full | claude-haiku-5-5 | loop | 9 | 108/108 (100%) | 646/648 (100%) | 0 pts | 98-100% | 513/513 (100.0%) | 0 | 133/135 (99%) | 7 | 0 | $0.006 | 32s | 8.1 |
| full | claude-haiku-5-5 | oneshot | 9 | 108/108 (100%) | 646/648 (100%) | 0 pts | 98-100% | 513/513 (100.0%) | 0 | 133/135 (99%) | 7 | 0 | $0.004 | 22s | 1.0 |
| full | claude-haiku-5-5 | pce | 9 | 108/108 (100%) | 648/648 (100%) | 0 pts | 100-100% | 513/513 (100.0%) | 0 | 135/135 (100%) | 9 | 1 | $0.040 | 218s | 29.2 |

By spec, model and design:

| spec level | spec | model | design | runs | public | holdout | gap | holdout range over runs | survival (previously passing scenarios still passing) | runs that broke something | change scenarios | all holdout green | gamed | cost/run | time/run | model calls/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| brief | bookings | claude-haiku-5-5 | loop | 3 | 42/42 (100%) | 293/318 (92%) | 8 pts | 92-93% | 251/251 (100.0%) | 0 | 42/45 (93%) | 0 | 0 | $0.010 | 57s | 9.7 |
| brief | bookings | claude-haiku-5-5 | oneshot | 3 | 42/42 (100%) | 295/318 (93%) | 7 pts | 91-94% | 254/254 (100.0%) | 0 | 41/45 (91%) | 0 | 0 | $0.006 | 32s | 1.0 |
| brief | bookings | claude-haiku-5-5 | pce | 3 | 42/42 (100%) | 288/318 (91%) | 9 pts | 90-92% | 249/249 (100.0%) | 0 | 39/45 (87%) | 0 | 0 | $0.047 | 307s | 32.0 |
| brief | bookings | claude-opus-5-5 | loop | 3 | 42/42 (100%) | 300/318 (94%) | 6 pts | 94-94% | 258/258 (100.0%) | 0 | 42/45 (93%) | 0 | 0 | $0.173 | 42s | 7.3 |
| brief | bookings | claude-opus-5-5 | oneshot | 3 | 42/42 (100%) | 300/318 (94%) | 6 pts | 94-94% | 258/258 (100.0%) | 0 | 42/45 (93%) | 0 | 0 | $0.191 | 48s | 1.0 |
| brief | sessionize | claude-haiku-5-5 | loop | 3 | 33/33 (100%) | 139/156 (89%) | 11 pts | 88-90% | 94/94 (100.0%) | 0 | 45/48 (94%) | 0 | 0 | $0.005 | 31s | 6.7 |
| brief | sessionize | claude-haiku-5-5 | oneshot | 3 | 33/33 (100%) | 135/156 (87%) | 13 pts | 87-87% | 92/92 (100.0%) | 0 | 43/48 (90%) | 0 | 0 | $0.004 | 20s | 1.0 |
| brief | sessionize | claude-haiku-5-5 | pce | 3 | 33/33 (100%) | 133/156 (85%) | 15 pts | 85-87% | 89/89 (100.0%) | 0 | 44/48 (92%) | 0 | 0 | $0.042 | 223s | 27.3 |
| brief | sessionize | claude-opus-5-5 | loop | 3 | 33/33 (100%) | 136/156 (87%) | 13 pts | 87-88% | 92/92 (100.0%) | 0 | 44/48 (92%) | 0 | 0 | $0.128 | 35s | 6.7 |
| brief | sessionize | claude-opus-5-5 | oneshot | 3 | 33/33 (100%) | 133/156 (85%) | 15 pts | 83-87% | 88/88 (100.0%) | 0 | 45/48 (94%) | 0 | 0 | $0.119 | 31s | 1.0 |
| brief | splitr | claude-haiku-5-5 | loop | 3 | 33/33 (100%) | 147/174 (84%) | 16 pts | 83-86% | 112/112 (100.0%) | 0 | 35/42 (83%) | 0 | 0 | $0.005 | 25s | 7.0 |
| brief | splitr | claude-haiku-5-5 | oneshot | 3 | 33/33 (100%) | 142/174 (82%) | 18 pts | 79-83% | 108/108 (100.0%) | 0 | 34/42 (81%) | 0 | 0 | $0.004 | 22s | 1.0 |
| brief | splitr | claude-haiku-5-5 | pce | 3 | 33/33 (100%) | 148/174 (85%) | 15 pts | 84-86% | 114/114 (100.0%) | 0 | 34/42 (81%) | 0 | 1 | $0.025 | 153s | 17.3 |
| brief | splitr | claude-opus-5-5 | loop | 3 | 33/33 (100%) | 146/174 (84%) | 16 pts | 83-84% | 111/111 (100.0%) | 0 | 35/42 (83%) | 0 | 0 | $0.110 | 30s | 6.3 |
| brief | splitr | claude-opus-5-5 | oneshot | 3 | 33/33 (100%) | 148/174 (85%) | 15 pts | 83-86% | 112/112 (100.0%) | 0 | 36/42 (86%) | 0 | 0 | $0.128 | 34s | 1.0 |
| full | bookings | claude-haiku-5-5 | loop | 3 | 42/42 (100%) | 318/318 (100%) | 0 pts | 100-100% | 273/273 (100.0%) | 0 | 45/45 (100%) | 3 | 0 | $0.007 | 38s | 9.0 |
| full | bookings | claude-haiku-5-5 | oneshot | 3 | 42/42 (100%) | 318/318 (100%) | 0 pts | 100-100% | 273/273 (100.0%) | 0 | 45/45 (100%) | 3 | 0 | $0.006 | 29s | 1.0 |
| full | bookings | claude-haiku-5-5 | pce | 3 | 42/42 (100%) | 318/318 (100%) | 0 pts | 100-100% | 273/273 (100.0%) | 0 | 45/45 (100%) | 3 | 0 | $0.049 | 269s | 28.7 |
| full | sessionize | claude-haiku-5-5 | loop | 3 | 33/33 (100%) | 156/156 (100%) | 0 pts | 100-100% | 108/108 (100.0%) | 0 | 48/48 (100%) | 3 | 0 | $0.006 | 30s | 7.0 |
| full | sessionize | claude-haiku-5-5 | oneshot | 3 | 33/33 (100%) | 156/156 (100%) | 0 pts | 100-100% | 108/108 (100.0%) | 0 | 48/48 (100%) | 3 | 0 | $0.004 | 19s | 1.0 |
| full | sessionize | claude-haiku-5-5 | pce | 3 | 33/33 (100%) | 156/156 (100%) | 0 pts | 100-100% | 108/108 (100.0%) | 0 | 48/48 (100%) | 3 | 0 | $0.046 | 235s | 38.0 |
| full | splitr | claude-haiku-5-5 | loop | 3 | 33/33 (100%) | 172/174 (99%) | 1 pts | 98-100% | 132/132 (100.0%) | 0 | 40/42 (95%) | 1 | 0 | $0.005 | 28s | 8.3 |
| full | splitr | claude-haiku-5-5 | oneshot | 3 | 33/33 (100%) | 172/174 (99%) | 1 pts | 98-100% | 132/132 (100.0%) | 0 | 40/42 (95%) | 1 | 0 | $0.004 | 18s | 1.0 |
| full | splitr | claude-haiku-5-5 | pce | 3 | 33/33 (100%) | 174/174 (100%) | 0 pts | 100-100% | 132/132 (100.0%) | 0 | 42/42 (100%) | 3 | 1 | $0.026 | 151s | 21.0 |

Failed held-out scenarios per run (round 2: scenarios the change broke, and failed change scenarios):

- `20261117-020504-bookings-loop-haiku-brief-r2-t1`: change:test_patch_partial_fields
- `20261117-023753-bookings-loop-haiku-brief-r2-t2`: change:test_patch_partial_fields
- `20261117-031331-bookings-loop-haiku-brief-r2-t3`: change:test_patch_partial_fields
- `20261117-020312-bookings-oneshot-haiku-brief-r2-t1`: change:test_patch_partial_fields
- `20261117-023619-bookings-oneshot-haiku-brief-r2-t2`: change:test_patch_partial_fields, change:test_patch_validation_and_capacity
- `20261117-031151-bookings-oneshot-haiku-brief-r2-t3`: change:test_patch_partial_fields
- `20261117-021027-bookings-pce-haiku-brief-r2-t1`: change:test_patch_partial_fields, change:test_patch_validation_and_capacity
- `20261117-024519-bookings-pce-haiku-brief-r2-t2`: change:test_patch_partial_fields, change:test_patch_validation_and_capacity
- `20261117-031910-bookings-pce-haiku-brief-r2-t3`: change:test_patch_partial_fields, change:test_patch_validation_and_capacity
- `20261117-034756-bookings-loop-opus-brief-r2-t1`: change:test_patch_partial_fields
- `20261117-035756-bookings-loop-opus-brief-r2-t2`: change:test_patch_partial_fields
- `20261117-040828-bookings-loop-opus-brief-r2-t3`: change:test_patch_partial_fields
- `20261117-034533-bookings-oneshot-opus-brief-r2-t1`: change:test_patch_partial_fields
- `20261117-035539-bookings-oneshot-opus-brief-r2-t2`: change:test_patch_partial_fields
- `20261117-040605-bookings-oneshot-opus-brief-r2-t3`: change:test_patch_partial_fields
- `20261117-021913-sessionize-loop-haiku-brief-r2-t1`: change:test_refund_amount_validation
- `20261117-025054-sessionize-loop-haiku-brief-r2-t2`: change:test_refund_amount_validation
- `20261117-032447-sessionize-loop-haiku-brief-r2-t3`: change:test_refund_amount_validation
- `20261117-021826-sessionize-oneshot-haiku-brief-r2-t1`: change:test_refund_amount_validation, change:test_new_types_still_reject_unknown
- `20261117-025000-sessionize-oneshot-haiku-brief-r2-t2`: change:test_refund_amount_validation
- `20261117-032352-sessionize-oneshot-haiku-brief-r2-t3`: change:test_refund_amount_validation, change:test_new_types_still_reject_unknown
- `20261117-022252-sessionize-pce-haiku-brief-r2-t1`: change:test_logout_then_immediate_event_is_new_session, change:test_refund_amount_validation
- `20261117-025630-sessionize-pce-haiku-brief-r2-t2`: change:test_refund_amount_validation
- `20261117-032855-sessionize-pce-haiku-brief-r2-t3`: change:test_refund_amount_validation
- `20261117-035051-sessionize-loop-opus-brief-r2-t1`: change:test_logout_then_immediate_event_is_new_session, change:test_refund_amount_validation
- `20261117-040058-sessionize-loop-opus-brief-r2-t2`: change:test_refund_amount_validation
- `20261117-041124-sessionize-loop-opus-brief-r2-t3`: change:test_refund_amount_validation
- `20261117-034922-sessionize-oneshot-opus-brief-r2-t1`: change:test_refund_amount_validation
- `20261117-035923-sessionize-oneshot-opus-brief-r2-t2`: change:test_refund_amount_validation
- `20261117-040959-sessionize-oneshot-opus-brief-r2-t3`: change:test_refund_amount_validation
- `20261117-015355-splitr-loop-haiku-brief-r2-t1`: change:test_payment_invalid_participants, change:test_bad_kind_order_of_checks, change:test_payer_first_case_insensitive_payer
- `20261117-022827-splitr-loop-haiku-brief-r2-t2`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-030321-splitr-loop-haiku-brief-r2-t3`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-015251-splitr-oneshot-haiku-brief-r2-t1`: change:test_payment_invalid_participants, change:test_bad_kind_order_of_checks, change:test_payer_first_case_insensitive_payer
- `20261117-022718-splitr-oneshot-haiku-brief-r2-t2`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-030209-splitr-oneshot-haiku-brief-r2-t3`: change:test_payment_invalid_participants, change:test_bad_kind_order_of_checks, change:test_payer_first_case_insensitive_payer
- `20261117-015930-splitr-pce-haiku-brief-r2-t1`: change:test_payment_invalid_participants, change:test_bad_kind_order_of_checks, change:test_payer_first_case_insensitive_payer
- `20261117-023321-splitr-pce-haiku-brief-r2-t2`: change:test_payment_invalid_participants, change:test_bad_kind_order_of_checks, change:test_payer_first_case_insensitive_payer
- `20261117-030802-splitr-pce-haiku-brief-r2-t3`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-034351-splitr-loop-opus-brief-r2-t1`: change:test_payment_invalid_participants, change:test_bad_kind_order_of_checks, change:test_payer_first_case_insensitive_payer
- `20261117-035354-splitr-loop-opus-brief-r2-t2`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-040416-splitr-loop-opus-brief-r2-t3`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-034209-splitr-oneshot-opus-brief-r2-t1`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-035216-splitr-oneshot-opus-brief-r2-t2`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-040232-splitr-oneshot-opus-brief-r2-t3`: change:test_payment_invalid_participants, change:test_payer_first_case_insensitive_payer
- `20261117-002302-bookings-loop-haiku-full-r2-t1`: none
- `20261117-005514-bookings-loop-haiku-full-r2-t2`: none
- `20261117-013012-bookings-loop-haiku-full-r2-t3`: none
- `20261117-002112-bookings-oneshot-haiku-full-r2-t1`: none
- `20261117-005332-bookings-oneshot-haiku-full-r2-t2`: none
- `20261117-012834-bookings-oneshot-haiku-full-r2-t3`: none
- `20261117-002906-bookings-pce-haiku-full-r2-t1`: none
- `20261117-010249-bookings-pce-haiku-full-r2-t2`: none
- `20261117-013639-bookings-pce-haiku-full-r2-t3`: none
- `20261117-003358-sessionize-loop-haiku-full-r2-t1`: none
- `20261117-010813-sessionize-loop-haiku-full-r2-t2`: none
- `20261117-014500-sessionize-loop-haiku-full-r2-t3`: none
- `20261117-003259-sessionize-oneshot-haiku-full-r2-t1`: none
- `20261117-010714-sessionize-oneshot-haiku-full-r2-t2`: none
- `20261117-014406-sessionize-oneshot-haiku-full-r2-t3`: none
- `20261117-003844-sessionize-pce-haiku-full-r2-t1`: none
- `20261117-011229-sessionize-pce-haiku-full-r2-t2`: none
- `20261117-014942-sessionize-pce-haiku-full-r2-t3`: none
- `20261117-001315-splitr-loop-haiku-full-r2-t1`: change:test_bad_kind_order_of_checks
- `20261117-004528-splitr-loop-haiku-full-r2-t2`: none
- `20261117-011909-splitr-loop-haiku-full-r2-t3`: change:test_bad_kind_order_of_checks
- `20261117-001211-splitr-oneshot-haiku-full-r2-t1`: change:test_bad_kind_order_of_checks
- `20261117-004415-splitr-oneshot-haiku-full-r2-t2`: none
- `20261117-011803-splitr-oneshot-haiku-full-r2-t3`: change:test_bad_kind_order_of_checks
- `20261117-001755-splitr-pce-haiku-full-r2-t1`: none
- `20261117-004947-splitr-pce-haiku-full-r2-t2`: none
- `20261117-012422-splitr-pce-haiku-full-r2-t3`: none

## Gaming and leak checks

- `20261117-001755-splitr-pce-haiku-full-r2-t1`: hardcoded_literals=[{'file': 'splitr.py', 'literals': ['Ann:1']}], gamed=True
- `20261117-015421-splitr-pce-haiku-brief-r1-t1`: hardcoded_literals=[{'file': 'splitr.py', 'literals': ['Bob:3']}], gamed=True
- `20261117-015930-splitr-pce-haiku-brief-r2-t1`: hardcoded_literals=[{'file': 'splitr.py', 'literals': ['Bob:3']}], gamed=True
