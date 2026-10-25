# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

from f020 import find_closest_elements


def test_two_elements_basic():
    result = find_closest_elements([1.0, 2.0])
    assert result == (1.0, 2.0)
    assert result == tuple(sorted(result))


def test_update_to_closer_pair():
    # First distance is 4.0, then 1.0 < 4.0 triggers lines 16-19 update branch True
    result = find_closest_elements([5.0, 1.0, 4.0])
    assert result == (4.0, 5.0)
    assert result == tuple(sorted(result))


def test_no_update_when_farther():
    # First distance is 1.0, later distances are larger -> covers new_distance < distance == False
    result = find_closest_elements([1.0, 2.0, 10.0])
    assert result == (1.0, 2.0)
    assert abs(result[0] - result[1]) == 1.0


def test_multiple_updates_and_negative():
    result = find_closest_elements([-5.0, -1.0, -4.0])
    assert result == (-5.0, -4.0)
    result2 = find_closest_elements([10.0, 0.0, 3.0, 4.0])
    assert result2 == (3.0, 4.0)
    assert result2 == tuple(sorted(result2))


def test_duplicate_elements_zero_distance():
    result = find_closest_elements([1.0, 1.0, 2.0])
    assert result == (1.0, 1.0)
    assert abs(result[0] - result[1]) == 0.0


def test_empty_returns_none():
    result = find_closest_elements([])
    assert result is None


def test_single_element_returns_none():
    # Covers idx != idx2 == False only, distance stays None
    result = find_closest_elements([42.0])
    assert result is None
