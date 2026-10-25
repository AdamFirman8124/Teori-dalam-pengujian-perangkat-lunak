# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

from f018 import how_many_times


def test_counts_overlapping_occurrences() -> None:
    assert how_many_times("banana", "ana") == 2


def test_returns_zero_when_substring_is_longer() -> None:
    assert how_many_times("abc", "abcd") == 0
