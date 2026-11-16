# DFL-HOLDOUT-CANARY-7c1e4b9a2f6d — held-out scenarios for bookings v1. Never mounted into a coder sandbox.
from helpers import api, code, ts  # noqa: F401


def post_booking(api, **over):
    body = {"room_id": "r1", "start": ts("09:00"), "end": ts("10:00"), "title": "x", "attendees": 1}
    body.update(over)
    body = {k: v for k, v in body.items() if v is not ...}
    return api.call("POST", "/bookings", body)


def test_room_name_trim_and_duplicate_ignoring_case(api):
    s, b, _ = api.call("POST", "/rooms", {"name": "  Atlas ", "capacity": 8})
    assert s == 201 and b["name"] == "Atlas"
    s, b, _ = api.call("POST", "/rooms", {"name": "ATLAS  ", "capacity": 3})
    assert s == 409 and code(b) == "room_exists"


def test_room_validation_cases(api):
    for body in ({"name": "A"}, {"capacity": 3}, {"name": "A", "capacity": 0}, {"name": "A", "capacity": 501},
                 {"name": "A", "capacity": "8"}, {"name": "A", "capacity": True}, {"name": "A", "capacity": 2.5},
                 {"name": 7, "capacity": 2}, {"name": "x" * 51, "capacity": 2}, {"name": "   ", "capacity": 2}):
        s, b, _ = api.call("POST", "/rooms", body)
        assert s == 422 and code(b) == "validation_error", body
    assert api.call("POST", "/rooms", {"name": "x" * 50, "capacity": 500})[0] == 201


def test_get_room_and_unknown_room(api):
    r = api.room("Atlas", 8)
    s, b, _ = api.call("GET", f"/rooms/{r}")
    assert s == 200 and b["name"] == "Atlas" and b["capacity"] == 8 and b["id"] == r
    s, b, _ = api.call("GET", "/rooms/r99")
    assert s == 404 and code(b) == "not_found"


def test_bad_json_and_non_object(api):
    for path in ("/rooms", "/bookings"):
        s, b, _ = api.call("POST", path, raw=b"{not json")
        assert s == 400 and code(b) == "bad_json", path
        s, b, _ = api.call("POST", path, raw=b"[1,2]")
        assert s == 400 and code(b) == "bad_json", path


def test_method_not_allowed(api):
    api.room()
    for method, path in (("DELETE", "/rooms"), ("PUT", "/rooms/r1"), ("POST", "/rooms/r1/availability"),
                         ("PUT", "/bookings"), ("POST", "/bookings/b1")):
        s, b, _ = api.call(method, path, {} if method in ("PUT", "POST") else None)
        assert s == 405 and code(b) == "method_not_allowed", (method, path)


def test_error_content_type(api):
    s, b, h = api.call("GET", "/nope")
    assert s == 404 and h["content-type"].startswith("application/json")


def test_unknown_fields_ignored(api):
    s, b, _ = api.call("POST", "/rooms", {"name": "Atlas", "capacity": 8, "color": "red"})
    assert s == 201


def test_timestamp_format_strict(api):
    api.room()
    for start in ("2026-03-02 09:00:00Z", "2026-03-02T09:00:00", "2026-03-02T09:00:00+00:00", "2026-03-02T09:00Z",
                  "2026-03-02T09:00:00.000Z", "2026-02-30T09:00:00Z", "2026-03-02T24:00:00Z", 1772442000):
        s, b, _ = post_booking(api, start=start)
        assert s == 422 and code(b) == "validation_error", start


def test_alignment_and_duration(api):
    api.room()
    bad = [("09:05", "10:00"), ("09:00", "09:50"), ("10:00", "09:00"), ("09:00", "09:00"),
           ("2026-03-02T09:00:30Z", "2026-03-02T10:00:00Z"), ("08:00", "16:15")]
    for a, b_ in bad:
        s, b, _ = post_booking(api, start=ts(a), end=ts(b_))
        assert s == 422 and code(b) == "validation_error", (a, b_)
    assert post_booking(api, start=ts("08:00"), end=ts("16:00"))[0] == 201
    assert post_booking(api, start=ts("16:00"), end=ts("16:15"))[0] == 201


def test_booking_field_validation(api):
    api.room()
    for over in ({"title": "  "}, {"title": "x" * 101}, {"title": 5}, {"attendees": 0}, {"attendees": "2"},
                 {"attendees": True}, {"room_id": 1}, {"title": ...}, {"end": ...}, {"room_id": ...}):
        s, b, _ = post_booking(api, **over)
        assert s == 422 and code(b) == "validation_error", over


def test_title_trimmed(api):
    api.room()
    s, b, _ = post_booking(api, title="  Weekly  ")
    assert s == 201 and b["title"] == "Weekly"


def test_check_order_validation_before_room_before_capacity_before_conflict(api):
    api.room(capacity=2)
    # invalid body and unknown room -> validation wins
    s, b, _ = post_booking(api, room_id="r99", title="")
    assert s == 422 and code(b) == "validation_error"
    # unknown room with otherwise valid body
    s, b, _ = post_booking(api, room_id="r99", attendees=99)
    assert s == 404 and code(b) == "not_found"
    # capacity is checked before conflict
    assert post_booking(api)[0] == 201
    s, b, _ = post_booking(api, attendees=3)
    assert s == 422 and code(b) == "over_capacity"


def test_overlap_variants(api):
    r = api.room()
    assert api.book(r, "10:00", "11:00")[0] == 201
    for a, b_ in (("09:00", "10:15"), ("10:45", "12:00"), ("10:15", "10:45"), ("09:00", "12:00"), ("10:00", "11:00")):
        s, b, _ = api.book(r, a, b_)
        assert s == 409 and code(b) == "conflict", (a, b_)
    assert api.book(r, "09:00", "10:00")[0] == 201
    assert api.book(r, "11:00", "12:00")[0] == 201


def test_other_room_does_not_conflict(api):
    r1, r2 = api.room("A"), api.room("B")
    assert api.book(r1, "09:00", "10:00")[0] == 201
    assert api.book(r2, "09:00", "10:00")[0] == 201


def test_booking_across_midnight(api):
    r = api.room()
    s, b, _ = api.call("POST", "/bookings", {"room_id": r, "start": "2026-03-02T22:00:00Z", "end": "2026-03-03T02:00:00Z",
                                             "title": "night", "attendees": 1})
    assert s == 201
    s, b, _ = api.call("POST", "/bookings", {"room_id": r, "start": "2026-03-03T01:00:00Z", "end": "2026-03-03T03:00:00Z",
                                             "title": "night2", "attendees": 1})
    assert s == 409


def test_ids_not_reused_after_delete(api):
    r = api.room()
    api.book(r, "09:00", "10:00")
    assert api.call("DELETE", "/bookings/b1")[0] == 204
    s, b, _ = api.book(r, "09:00", "10:00")
    assert s == 201 and b["id"] == "b2"
    s, b, _ = api.call("GET", "/bookings/b1")
    assert s == 404 and code(b) == "not_found"


def test_delete_twice_and_unknown(api):
    r = api.room()
    api.book(r, "09:00", "10:00")
    assert api.call("DELETE", "/bookings/b1")[0] == 204
    s, b, _ = api.call("DELETE", "/bookings/b1")
    assert s == 404 and code(b) == "not_found"
    assert api.call("DELETE", "/bookings/b77")[0] == 404


def test_idempotent_replay_returns_original(api):
    r = api.room()
    h = {"Idempotency-Key": "k1"}
    s1, b1, _ = api.book(r, "09:00", "10:00", headers=h)
    s2, b2, _ = api.book(r, "09:00", "10:00", headers=h)
    assert (s1, s2) == (201, 201) and b1 == b2
    s, b, _ = api.call("GET", "/bookings")
    assert len(b["bookings"]) == 1


def test_idempotent_body_equality_ignores_key_order(api):
    r = api.room()
    h = {"Idempotency-Key": "k1", "Content-Type": "application/json"}
    raw1 = ('{"room_id":"%s","start":"%s","end":"%s","title":"t","attendees":1}' % (r, ts("09:00"), ts("10:00"))).encode()
    raw2 = ('{ "attendees": 1, "title": "t", "end": "%s", "start": "%s", "room_id": "%s" }' % (ts("10:00"), ts("09:00"), r)).encode()
    s1, b1, _ = api.call("POST", "/bookings", raw=raw1, headers=h)
    s2, b2, _ = api.call("POST", "/bookings", raw=raw2, headers=h)
    assert (s1, s2) == (201, 201) and b1["id"] == b2["id"] == "b1"


def test_idempotency_mismatch(api):
    r = api.room()
    h = {"Idempotency-Key": "k1"}
    assert api.book(r, "09:00", "10:00", headers=h)[0] == 201
    s, b, _ = api.book(r, "11:00", "12:00", headers=h)
    assert s == 422 and code(b) == "idempotency_mismatch"


def test_idempotency_failed_request_not_remembered(api):
    r = api.room()
    h = {"Idempotency-Key": "k1"}
    assert api.book(r, "09:00", "10:00")[0] == 201
    assert api.book(r, "09:00", "10:00", headers=h)[0] == 409
    assert api.call("DELETE", "/bookings/b1")[0] == 204
    s, b, _ = api.book(r, "09:00", "10:00", headers=h)
    assert s == 201 and b["id"] == "b2"


def test_idempotent_replay_after_delete_still_returns_original(api):
    r = api.room()
    h = {"Idempotency-Key": "k1"}
    s1, b1, _ = api.book(r, "09:00", "10:00", headers=h)
    api.call("DELETE", "/bookings/b1")
    s2, b2, _ = api.book(r, "09:00", "10:00", headers=h)
    assert s2 == 201 and b2 == b1
    assert api.call("GET", "/bookings")[1]["bookings"] == []


def test_list_filter_by_room_and_unknown_room(api):
    r1, r2 = api.room("A"), api.room("B")
    api.book(r1, "09:00", "10:00")
    api.book(r2, "09:00", "10:00")
    s, b, _ = api.call("GET", f"/bookings?room_id={r2}")
    assert [x["id"] for x in b["bookings"]] == ["b2"]
    s, b, _ = api.call("GET", "/bookings?room_id=r99")
    assert s == 200 and b["bookings"] == [] and b["next_cursor"] is None


def test_list_order_same_start_by_creation(api):
    r1, r2, r3 = api.room("A"), api.room("B"), api.room("C")
    api.book(r3, "09:00", "10:00")
    api.book(r1, "09:00", "10:00")
    api.book(r2, "08:00", "09:00")
    s, b, _ = api.call("GET", "/bookings")
    assert [x["id"] for x in b["bookings"]] == ["b3", "b1", "b2"]


def test_list_window_half_open(api):
    r = api.room()
    api.book(r, "09:00", "10:00")
    api.book(r, "10:00", "11:00")
    api.book(r, "11:00", "12:00")
    q = "/bookings?from=2026-03-02T10:00:00Z&to=2026-03-02T11:00:00Z"
    assert [x["id"] for x in api.call("GET", q)[1]["bookings"]] == ["b2"]
    q = "/bookings?from=2026-03-02T10:59:59Z"
    assert [x["id"] for x in api.call("GET", q)[1]["bookings"]] == ["b2", "b3"]
    q = "/bookings?to=2026-03-02T10:00:01Z"
    assert [x["id"] for x in api.call("GET", q)[1]["bookings"]] == ["b1", "b2"]


def test_list_invalid_params(api):
    for q in ("limit=0", "limit=101", "limit=abc", "limit=2.5", "from=yesterday", "to=2026-03-02", "cursor=%21%21garbage"):
        s, b, _ = api.call("GET", "/bookings?" + q)
        assert s == 422 and code(b) == "validation_error", q
    assert api.call("GET", "/bookings?limit=100")[0] == 200


def test_pagination_walks_everything_once(api):
    r1, r2 = api.room("A"), api.room("B")
    expected = []
    for hour in (8, 9, 10, 11, 12):
        for r in (r2, r1):
            s, b, _ = api.book(r, f"{hour:02d}:00", f"{hour + 1:02d}:00")
            expected.append(b["id"])
    seen, cursor, pages = [], None, 0
    while True:
        q = "/bookings?limit=3" + (f"&cursor={cursor}" if cursor else "")
        s, b, _ = api.call("GET", q)
        assert s == 200 and len(b["bookings"]) <= 3
        seen += [x["id"] for x in b["bookings"]]
        pages += 1
        cursor = b["next_cursor"]
        if cursor is None:
            break
        assert isinstance(cursor, str) and pages < 10
    assert seen == expected and pages == 4


def test_pagination_exact_page_has_null_cursor(api):
    r = api.room()
    api.book(r, "09:00", "10:00")
    api.book(r, "10:00", "11:00")
    s, b, _ = api.call("GET", "/bookings?limit=2")
    assert len(b["bookings"]) == 2 and b["next_cursor"] is None


def test_pagination_with_filter(api):
    r1, r2 = api.room("A"), api.room("B")
    for hour in (8, 9, 10):
        api.book(r1, f"{hour:02d}:00", f"{hour + 1:02d}:00")
        api.book(r2, f"{hour:02d}:00", f"{hour + 1:02d}:00")
    s, b, _ = api.call("GET", f"/bookings?room_id={r2}&limit=2")
    assert [x["id"] for x in b["bookings"]] == ["b2", "b4"] and b["next_cursor"]
    s, b, _ = api.call("GET", f"/bookings?room_id={r2}&limit=2&cursor={b['next_cursor']}")
    assert [x["id"] for x in b["bookings"]] == ["b6"] and b["next_cursor"] is None


def test_default_limit_is_20(api):
    rooms = [api.room(f"R{i}") for i in range(3)]
    for r in rooms:
        for hour in range(8, 16):
            api.book(r, f"{hour:02d}:00", f"{hour + 1:02d}:00")
    s, b, _ = api.call("GET", "/bookings")
    assert len(b["bookings"]) == 20 and b["next_cursor"] is not None


def test_availability_empty_day_and_full_day(api):
    r = api.room()
    s, b, _ = api.call("GET", f"/rooms/{r}/availability?date=2026-03-02")
    assert b["free"] == [{"start": ts("08:00"), "end": ts("18:00")}]
    api.book(r, "08:00", "13:00")
    api.book(r, "13:00", "18:00")
    s, b, _ = api.call("GET", f"/rooms/{r}/availability?date=2026-03-02")
    assert s == 200 and b["free"] == []


def test_availability_clipping_and_adjacent(api):
    r = api.room()
    api.book(r, "06:00", "08:30")
    api.book(r, "10:00", "11:00")
    api.book(r, "11:00", "11:30")
    api.book(r, "17:00", "20:00")
    api.book(r, "20:00", "21:00")
    s, b, _ = api.call("GET", f"/rooms/{r}/availability?date=2026-03-02")
    assert b["free"] == [{"start": ts("08:30"), "end": ts("10:00")}, {"start": ts("11:30"), "end": ts("17:00")}]


def test_availability_other_days_and_rooms_ignored(api):
    r1, r2 = api.room("A"), api.room("B")
    api.book(r2, "09:00", "10:00")
    api.call("POST", "/bookings", {"room_id": r1, "start": "2026-03-03T09:00:00Z", "end": "2026-03-03T10:00:00Z",
                                   "title": "t", "attendees": 1})
    s, b, _ = api.call("GET", f"/rooms/{r1}/availability?date=2026-03-02")
    assert b["free"] == [{"start": ts("08:00"), "end": ts("18:00")}]


def test_availability_overnight_booking_clipped(api):
    r = api.room()
    api.call("POST", "/bookings", {"room_id": r, "start": "2026-03-01T23:00:00Z", "end": "2026-03-02T07:00:00Z",
                                   "title": "t", "attendees": 1})
    api.call("POST", "/bookings", {"room_id": r, "start": "2026-03-02T16:00:00Z", "end": "2026-03-03T00:00:00Z",
                                   "title": "t", "attendees": 1})
    s, b, _ = api.call("GET", f"/rooms/{r}/availability?date=2026-03-02")
    assert b["free"] == [{"start": ts("08:00"), "end": ts("16:00")}]


def test_availability_errors(api):
    r = api.room()
    for q in ("", "?date=", "?date=2026-02-30", "?date=02-03-2026", "?date=20260302"):
        s, b, _ = api.call("GET", f"/rooms/{r}/availability{q}")
        assert s == 422 and code(b) == "validation_error", q
    s, b, _ = api.call("GET", "/rooms/r99/availability?date=bad")
    assert s == 404 and code(b) == "not_found"
