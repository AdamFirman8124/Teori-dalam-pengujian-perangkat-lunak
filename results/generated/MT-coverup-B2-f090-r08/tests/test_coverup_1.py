# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f090 import next_smallest


def test_next_smallest_with_at_least_two_distinct_values():
    """Covers lines 3-4 and the False branch (len >= 2): returns second smallest distinct value."""
    original = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = next_smallest(original)
    # distinct sorted values are [1, 2, 3, 4, 5, 6, 9] -> second smallest is 2
    assert result == 2
    # duplicates are deduplicated before sorting
    assert next_smallest([5, 5, 1, 1, 3]) == 3
    # exactly two distinct values
    assert next_smallest([10, 20, 10]) == 20
    # input list must not be mutated
    assert original == [3, 1, 4, 1, 5, 9, 2, 6, 5]


def test_next_smallest_with_fewer_than_two_distinct_values():
    """Covers lines 3-4 and the True branch (len < 2): returns None."""
    assert next_smallest([]) is None
    assert next_smallest([7]) is None
    # duplicates collapse to a single distinct value
    assert next_smallest([4, 4, 4]) is None
    # input list must not be mutated
    original = [4, 4, 4]
    assert next_smallest(original) is None
    assert original == [4, 4, 4]
