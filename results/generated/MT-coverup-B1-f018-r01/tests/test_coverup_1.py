# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

from f018 import how_many_times


def test_how_many_times_counts_overlapping_matches() -> None:
    assert how_many_times("ababa", "aba") == 2
