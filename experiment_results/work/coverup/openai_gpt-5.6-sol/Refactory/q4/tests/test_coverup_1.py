# file: script_q4.py:3-10
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 10], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 10], [5, 4], [5, 6], [6, 5], [6, 7]]}

from script_q4 import sort_age


def test_sort_age_sorts_records_in_descending_age_order():
    records = [
        ("Alice", 25),
        ("Bob", 40),
        ("Carol", 30),
    ]

    result = sort_age(records)

    assert result == [
        ("Bob", 40),
        ("Carol", 30),
        ("Alice", 25),
    ]
    assert result is records


def test_sort_age_leaves_already_sorted_records_unchanged():
    records = [
        ("Bob", 40),
        ("Carol", 30),
        ("Alice", 25),
    ]

    result = sort_age(records)

    assert result == records
    assert result is records


def test_sort_age_handles_empty_and_single_record_lists():
    empty_records = []
    single_record = [("Alice", 25)]

    assert sort_age(empty_records) == []
    assert sort_age(single_record) == [("Alice", 25)]
