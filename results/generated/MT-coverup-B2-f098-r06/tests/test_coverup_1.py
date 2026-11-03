# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f098 import count_upper


@pytest.mark.parametrize(
    "s, expected",
    [
        # Empty string: loop body never runs, returns 0
        ("", 0),
        # Single character, uppercase vowel at index 0
        ("A", 1),
        # Single character, not a vowel
        ("B", 0),
        # Lowercase vowels at even indices must NOT be counted
        ("aeiou", 0),
        # Uppercase vowels at even indices are counted
        ("AEIOU", 3),          # A(0), I(2), U(4)
        # Uppercase vowels at odd indices must NOT be counted
        ("aEiOuX", 0),         # E(1), O(3) are at odd positions
        # Mixed case, mixed content
        ("aBCdEf", 1),         # only E(4) qualifies
        ("AbCdEfG", 2),        # A(0) and E(4) qualify
        # Consonants only
        ("dBBE", 0),
        # Non-letter characters at even positions; vowels at odd positions
        ("!E@U#", 0),          # E(1) and U(3) are at odd indices
        # Non-letter characters at odd positions; vowels at even positions
        ("A!E@U", 3),          # A(0), E(2), U(4) qualify
    ],
)
def test_count_upper(s, expected):
    assert count_upper(s) == expected


def test_count_upper_returns_int():
    result = count_upper("AEIOUX")
    assert isinstance(result, int)
    assert result == 3  # A(0), I(2), U(4); X(6) is not a vowel
