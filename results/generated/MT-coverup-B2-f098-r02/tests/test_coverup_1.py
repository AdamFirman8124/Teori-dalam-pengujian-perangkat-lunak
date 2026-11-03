# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f098 import count_upper


@pytest.mark.parametrize(
    "s, expected",
    [
        # Empty string: exercises line 3/4/7 with the loop body never running.
        ("", 0),
        # Single character, vowel at index 0: covers loop entry, True branch, increment.
        ("A", 1),
        # Single character, consonant: covers False branch of the membership test.
        ("B", 0),
        # All even-index characters are uppercase vowels.
        ("AEIOU", 3),
        # Even-index characters are lowercase/consonants: False branch taken every time.
        ("abcdefg", 0),
        # Mixed case: only 'E' at an even index is an uppercase vowel.
        ("aBCdEf", 1),
        # All uppercase vowels sit at odd positions, so none are counted.
        ("xExIxOxU", 0),
        # Even indices hold 'A', 'E', 'x', 'x' -> two vowels counted.
        ("AxEIxIxO", 2),
        # Even indices hold 'A', 'E', 'A' -> three vowels counted.
        ("AxEIAO", 3),
    ],
)
def test_count_upper(s, expected):
    """Exercise every line and both branches of count_upper."""
    result = count_upper(s)
    assert isinstance(result, int)
    assert result == expected


def test_count_upper_counts_only_even_index_vowels():
    """Postcondition: only even indices are inspected, and only uppercase vowels count."""
    # 'A' at index 0 counts; 'E' at index 1 does not; 'I' at index 2 counts.
    assert count_upper("AEI") == 2
    # Same vowels shifted to odd positions: only 'E' at index 2 is counted.
    assert count_upper("xAEIxI") == 1


def test_count_upper_is_pure():
    """Postcondition: calling the function does not mutate its input."""
    s = "AbEcIdO"
    before = str(s)
    # Even indices hold 'A', 'E', 'I', 'O' -> all four are counted.
    assert count_upper(s) == 4
    assert s == before
