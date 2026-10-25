# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

from f163 import generate_integers


def test_basic_range_inclusive():
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_arguments_in_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_partial_overlap_with_bounds():
    # lower = max(2, min(1, 3)) = 2, upper = min(8, max(1, 3)) = 3
    assert generate_integers(1, 3) == [2]


def test_no_even_numbers_in_range():
    # lower = max(2, 7) = 7, upper = min(8, 7) = 7 -> only 7, which is odd
    assert generate_integers(7, 7) == []


def test_empty_range_when_lower_exceeds_upper():
    # lower = max(2, 10) = 10, upper = min(8, 12) = 8 -> empty range
    assert generate_integers(10, 12) == []


def test_single_value_range():
    # lower = max(2, 4) = 4, upper = min(8, 4) = 4 -> [4]
    assert generate_integers(4, 4) == [4]


def test_result_is_list_of_ints():
    result = generate_integers(2, 8)
    assert isinstance(result, list)
    assert all(isinstance(i, int) for i in result)
    assert all(i % 2 == 0 for i in result)
