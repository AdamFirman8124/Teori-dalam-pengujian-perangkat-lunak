# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

import pytest

from f137 import compare_one


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ("1,5", "1.5", None),
        (2, "1,5", 2),
        ("1,5", 2, 2),
        (1, 2, 2),
    ],
)
def test_compare_one_handles_strings_numbers_and_all_outcomes(a, b, expected):
    assert compare_one(a, b) == expected
