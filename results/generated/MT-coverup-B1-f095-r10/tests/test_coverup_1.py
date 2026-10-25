# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

import pytest

from f095 import check_dict_case


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ({}, False),
        ({1: "non-string key"}, False),
        ({"": "caseless key"}, False),
        ({"A": 1}, True),
        ({"a": 1}, True),
        ({"A": 1, "B": 2}, True),
        ({"a": 1, "b": 2}, True),
        ({"A": 1, "b": 2}, False),
        ({"a": 1, "B": 2}, False),
    ],
)
def test_check_dict_case_covers_all_key_cases(value, expected):
    original = value.copy()

    assert check_dict_case(value) is expected
    assert value == original
