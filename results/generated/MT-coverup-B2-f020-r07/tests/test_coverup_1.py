# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

from f020 import find_closest_elements


def test_find_closest_elements_updates_to_nearest_pair():
    assert find_closest_elements([10.0, 0.0, 1.0]) == (0.0, 1.0)


def test_find_closest_elements_with_fewer_than_two_numbers():
    assert find_closest_elements([]) is None
    assert find_closest_elements([5.0]) is None
