# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

from f163 import generate_integers


def test_generate_integers_full_range():
    """Both bounds within [2, 8]: all even numbers in between are returned."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_generate_integers_reversed_args():
    """Argument order must not matter (min/max are used)."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_generate_integers_lower_clamped():
    """A lower bound below 2 is clamped up to 2."""
    assert generate_integers(1, 5) == [2, 4]


def test_generate_integers_upper_clamped():
    """An upper bound above 8 is clamped down to 8."""
    assert generate_integers(7, 10) == [8]


def test_generate_integers_empty_when_both_above():
    """When both values exceed 8, lower > upper and the result is empty."""
    assert generate_integers(10, 20) == []


def test_generate_integers_single_odd_value():
    """A single odd value in range yields no even numbers (false branch of i % 2 == 0)."""
    assert generate_integers(3, 3) == []


def test_generate_integers_single_even_value():
    """A single even value in range is returned (true branch of i % 2 == 0)."""
    assert generate_integers(2, 2) == [2]
