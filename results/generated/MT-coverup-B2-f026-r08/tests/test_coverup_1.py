# file: project/f026/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

from f026 import remove_duplicates


def test_remove_duplicates_keeps_only_values_occurring_once():
    # Values that appear more than once are removed entirely;
    # values that appear exactly once are kept in original order.
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1]


def test_remove_duplicates_all_unique():
    # Every element occurs exactly once, so all are kept (true branch of c[n] <= 1).
    assert remove_duplicates([4, 5, 6]) == [4, 5, 6]


def test_remove_duplicates_all_duplicates():
    # Every element occurs more than once, so all are removed (false branch of c[n] <= 1).
    assert remove_duplicates([7, 7, 7]) == []


def test_remove_duplicates_empty_list():
    # Empty input yields empty output; still exercises lines 6-8.
    assert remove_duplicates([]) == []


def test_remove_duplicates_preserves_order_and_does_not_mutate_input():
    numbers = [9, 1, 9, 2, 1, 3]
    original = list(numbers)
    result = remove_duplicates(numbers)
    # Only the singletons (2 and 3) survive, in their original relative order.
    assert result == [2, 3]
    # The input list is not mutated (no state pollution).
    assert numbers == original
