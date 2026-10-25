# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

import pytest

from f018 import how_many_times


@pytest.mark.parametrize(
    ("string", "substring", "expected"),
    [
        ("banana", "ana", 2),
        ("abc", "x", 0),
        ("ab", "abcd", 0),
        ("abc", "", 4),
    ],
)
def test_how_many_times(string, substring, expected):
    assert how_many_times(string, substring) == expected
