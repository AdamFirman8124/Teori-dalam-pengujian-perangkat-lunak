

# Generated at 2026-11-03 04:32:12.662459
# Unit test for function median
def test_median():
    # Odd number of elements
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([5]) == 5
    assert module_0.median([10, 20, 30, 40, 50]) == 30

    # Even number of elements (average of middle two)
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([1, 2]) == 1.5
    assert module_0.median([4, 2]) == 3.0

    # Unsorted input should be handled
    assert module_0.median([9, 1, 5, 3, 7]) == 5
    assert module_0.median([10, 2, 8, 4]) == 6.0

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3, 4]) == 2

    # Negative numbers and floats
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([-1.5, 2.5]) == 0.5
    assert module_0.median([1.1, 2.2, 3.3]) == 2.2

    # Even-length list with duplicates around the middle
    assert module_0.median([1, 2, 2, 3]) == 2.0

    print("All median tests passed!")


if __name__ == "__main__":
    test_median()

# Generated at 2026-11-03 04:35:41.458931
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


def test_median_mixed_positive_negative():
    assert module_0.median([-10, 10, 0]) == 0


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_even_with_floats():
    assert module_0.median([1.0, 2.0, 3.0, 4.0]) == 2.5


def test_median_duplicates():
    assert module_0.median([2, 2, 2, 2]) == 2


def test_median_duplicates_odd():
    assert module_0.median([7, 7, 1]) == 7


def test_median_two_elements():
    assert module_0.median([1, 3]) == 2.0


def test_median_does_not_modify_original():
    lst = [3, 1, 2]
    module_0.median(lst)
    assert lst == [3, 1, 2]


def test_median_large_odd_list():
    assert module_0.median(list(range(101))) == 50


def test_median_large_even_list():
    assert module_0.median(list(range(100))) == 49.5


def test_median_empty_list_raises():
    with pytest.raises(IndexError):
        module_0.median([])

# Generated at 2026-11-03 04:38:51.225882
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([3, 1, 2]) == 2


def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5


def test_median_single_element():
    assert module_0.median([5]) == 5


def test_median_two_elements():
    assert module_0.median([1, 3]) == 2.0


def test_median_unsorted_input():
    assert module_0.median([10, 2, 8, 4, 6]) == 6


def test_median_negative_numbers():
    assert module_0.median([-5, -1, -3]) == -3


def test_median_mixed_positive_negative():
    assert module_0.median([-10, 4, 6, 1000, 10, 20]) == 8.0


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_duplicates():
    assert module_0.median([1, 2, 2, 3]) == 2.0


def test_median_all_same_values():
    assert module_0.median([7, 7, 7, 7]) == 7.0


def test_median_even_result_is_float():
    result = module_0.median([1, 2, 3, 4])
    assert isinstance(result, float)


def test_median_odd_returns_element():
    result = module_0.median([1, 2, 3, 4, 5])
    assert result == 3


def test_median_does_not_modify_original():
    original = [3, 1, 2]
    module_0.median(original)
    assert original == [3, 1, 2]


def test_median_sorted_input():
    assert module_0.median([1, 2, 3, 4, 5, 6]) == 3.5


def test_median_large_list():
    assert module_0.median(list(range(101))) == 50


def test_median_large_even_list():
    assert module_0.median(list(range(100))) == 49.5