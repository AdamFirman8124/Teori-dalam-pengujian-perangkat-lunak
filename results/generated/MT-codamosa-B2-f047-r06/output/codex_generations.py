

# Generated at 2026-11-01 20:10:05.966805
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([1, 2, 3]) == 2


def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5


def test_median_single_element():
    assert module_0.median([5]) == 5


def test_median_two_elements():
    assert module_0.median([3, 1]) == 2.0


def test_median_unsorted_input():
    assert module_0.median([3, 1, 2]) == 2


def test_median_negative_numbers():
    assert module_0.median([-1, -2, -3]) == -2


def test_median_mixed_signs():
    assert module_0.median([-1, 0, 1]) == 0


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_even_floats():
    assert module_0.median([1.0, 2.0, 3.0, 4.0]) == 2.5


def test_median_duplicates():
    assert module_0.median([2, 2, 2, 2]) == 2.0


def test_median_duplicates_odd():
    assert module_0.median([5, 5, 5]) == 5


def test_median_large_unsorted():
    assert module_0.median([10, 2, 8, 4, 6]) == 6


def test_median_even_unsorted():
    assert module_0.median([7, 1, 3, 5]) == 4.0


def test_median_returns_float_for_even():
    result = module_0.median([1, 2])
    assert isinstance(result, float)
    assert result == 1.5


def test_median_returns_int_for_odd():
    result = module_0.median([1, 2, 3])
    assert result == 2

# Generated at 2026-11-01 20:10:27.575655
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([3, 1, 2]) == 2


def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5


def test_median_single_element():
    assert module_0.median([5]) == 5


def test_median_unsorted_input():
    assert module_0.median([10, 2, 8, 4, 6]) == 6


def test_median_negative_numbers():
    assert module_0.median([-5, -1, -3]) == -3


def test_median_mixed_sign_numbers():
    assert module_0.median([-1, 0, 1]) == 0


def test_median_float_values():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_with_duplicates():
    assert module_0.median([1, 2, 2, 3]) == 2.0


def test_median_two_elements():
    assert module_0.median([1, 3]) == 2.0


def test_median_does_not_modify_original():
    lst = [3, 1, 2]
    module_0.median(lst)
    assert lst == [3, 1, 2]


def test_median_all_same_values():
    assert module_0.median([7, 7, 7, 7]) == 7


def test_median_large_range():
    assert module_0.median([100, -100, 50, -50, 0]) == 0

# Generated at 2026-11-01 20:10:51.646500
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([1, 2, 3]) == 2


def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5


def test_median_single_element():
    assert module_0.median([5]) == 5


def test_median_unsorted_input():
    assert module_0.median([3, 1, 2]) == 2


def test_median_unsorted_even():
    assert module_0.median([4, 1, 3, 2]) == 2.5


def test_median_negative_numbers():
    assert module_0.median([-1, -2, -3]) == -2


def test_median_mixed_sign():
    assert module_0.median([-1, 0, 1]) == 0


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_duplicates():
    assert module_0.median([1, 2, 2, 3]) == 2.0


def test_median_all_same():
    assert module_0.median([7, 7, 7, 7]) == 7.0


def test_median_two_elements():
    assert module_0.median([10, 20]) == 15.0


def test_median_returns_float_for_even():
    result = module_0.median([1, 3])
    assert isinstance(result, float)


def test_median_does_not_modify_original():
    lst = [3, 1, 2]
    module_0.median(lst)
    assert lst == [3, 1, 2]

# Generated at 2026-11-01 20:11:18.303725
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([3, 1, 2]) == 2


def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5


def test_median_single_element():
    assert module_0.median([5]) == 5


def test_median_two_elements():
    assert module_0.median([3, 1]) == 2.0


def test_median_unsorted_input():
    assert module_0.median([10, 2, 8, 4, 6]) == 6


def test_median_negative_numbers():
    assert module_0.median([-5, -1, -3]) == -3


def test_median_mixed_positive_negative():
    assert module_0.median([-1, 1, 0]) == 0


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_even_floats():
    assert module_0.median([1.0, 2.0, 3.0, 10.0]) == 2.5


def test_median_with_duplicates():
    assert module_0.median([2, 2, 2, 2]) == 2.0


def test_median_returns_float_for_even():
    result = module_0.median([1, 2, 3, 4])
    assert isinstance(result, float)


def test_median_does_not_modify_original():
    original = [3, 1, 2]
    module_0.median(original)
    assert original == [3, 1, 2]


def test_median_large_list():
    l = list(range(101, 0, -1))  # 101 down to 1
    assert module_0.median(l) == 51


def test_median_even_large_list():
    l = list(range(100, 0, -1))  # 100 down to 1
    assert module_0.median(l) == 50.5

# Generated at 2026-11-01 20:11:34.337721
# Unit test for function median
def test_median():
    # Odd-length list
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([5]) == 5
    assert module_0.median([10, 20, 30, 40, 50]) == 30

    # Even-length list
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([1, 2]) == 1.5
    assert module_0.median([10, 2, 8, 4]) == 6.0

    # Unsorted input
    assert module_0.median([9, 1, 5, 3, 7]) == 5
    assert module_0.median([4, 1, 3, 2]) == 2.5

    # Negative numbers
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([-10, 10]) == 0.0
    assert module_0.median([-1, -2, -3, -4]) == -2.5

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0
    assert module_0.median([7, 7, 7]) == 7

    # Floats
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1.1, 2.2]) == 1.65

    # Already sorted lists
    assert module_0.median([1, 2, 3, 4, 5]) == 3

    # Mixed positive/negative with floats
    assert abs(module_0.median([-1.5, 0.5, 2.5]) - 0.5) < 1e-9