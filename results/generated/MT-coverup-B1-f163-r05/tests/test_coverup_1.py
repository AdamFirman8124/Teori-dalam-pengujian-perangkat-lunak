# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

from f163 import generate_integers


def test_normal_range_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_normal_range_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_clamped_below_and_above():
    assert generate_integers(0, 10) == [2, 4, 6, 8]
    assert generate_integers(-5, 20) == [2, 4, 6, 8]


def test_odd_only_range_filters_all():
    assert generate_integers(3, 3) == []
    assert generate_integers(3, 5) == [4]


def test_single_even():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(2, 3) == [2]
    assert generate_integers(7, 8) == [8]


def test_empty_when_lower_gt_upper():
    assert generate_integers(1, 1) == []
    assert generate_integers(10, 10) == []
    assert generate_integers(9, 9) == []


def test_mixed_even_odd_filtering():
    assert generate_integers(3, 7) == [4, 6]
    assert generate_integers(4, 6) == [4, 6]
