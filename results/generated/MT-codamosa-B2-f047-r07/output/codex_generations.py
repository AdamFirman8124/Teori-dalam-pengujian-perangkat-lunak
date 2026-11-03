

# Generated at 2026-11-01 21:18:06.441270
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([1, 2, 3, 4, 5]) == 3

def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5

def test_median_single_element():
    assert module_0.median([42]) == 42

def test_median_unsorted_input():
    assert module_0.median([5, 1, 3]) == 3

def test_median_two_elements():
    assert module_0.median([10, 20]) == 15.0

def test_median_with_negatives():
    assert module_0.median([-5, -1, -3]) == -3

def test_median_mixed_positives_negatives():
    assert module_0.median([-10, 4, 6, 1000, 10, 20]) == 8.0

def test_median_with_duplicates():
    assert module_0.median([1, 2, 2, 3]) == 2.0

def test_median_all_same_values():
    assert module_0.median([7, 7, 7, 7]) == 7.0

def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5

def test_median_returns_float_for_even():
    result = module_0.median([1, 2])
    assert isinstance(result, float)

def test_median_does_not_modify_original():
    lst = [3, 1, 2]
    module_0.median(lst)
    assert lst == [3, 1, 2]

def test_median_large_list():
    data = list(range(1000, 0, -1))
    assert module_0.median(data) == 500.5

def test_median_sorted_result_correctness():
    assert module_0.median([3, 1, 4, 1, 5, 9, 2, 6]) == 3.5

# Generated at 2026-11-01 21:18:15.760723
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


def test_median_mixed_sign():
    assert module_0.median([-1, 0, 1]) == 0


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_duplicates():
    assert module_0.median([2, 2, 2, 2]) == 2.0


def test_median_does_not_modify_order_result():
    result = module_0.median([9, 1, 5])
    assert result == 5


def test_median_even_float_result():
    assert module_0.median([1, 2]) == 1.5


def test_median_large_numbers():
    assert module_0.median([1000000, 999999, 1000001]) == 1000000

# Generated at 2026-11-01 21:18:23.021438
# Unit test for function median
def test_median():
    # Odd-length lists
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([3, 1, 2]) == 2  # unsorted input
    assert module_0.median([5]) == 5  # single element
    assert module_0.median([10, 20, 30, 40, 50]) == 30

    # Even-length lists
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([4, 1, 3, 2]) == 2.5  # unsorted input
    assert module_0.median([1, 2]) == 1.5
    assert module_0.median([10, 20]) == 15.0

    # Negative numbers
    assert module_0.median([-1, -2, -3]) == -2
    assert module_0.median([-1, -2, -3, -4]) == -2.5
    assert module_0.median([-5, 5]) == 0.0

    # Mixed signs and floats
    assert module_0.median([-1, 0, 1]) == 0
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1.1, 2.2]) == 1.65

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 1, 2, 2, 3]) == 2
    assert module_0.median([5, 5, 5]) == 5

    # Result should not modify original list order semantics (median works on sorted copy)
    data = [3, 1, 2]
    assert module_0.median(data) == 2
    assert data == [3, 1, 2]  # original list unchanged

    # Error case: empty list should raise IndexError
    try:
        module_0.median([])
        assert False, "Expected IndexError for empty list"
    except IndexError:
        pass

    print("All median tests passed!")


test_median()

# Generated at 2026-11-01 21:18:28.449596
# Unit test for function median
def test_median():
    # Odd-length list
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([10, 20, 30, 40, 50]) == 30
    assert module_0.median([5]) == 5

    # Even-length list
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([10, 20]) == 15.0
    assert module_0.median([4, 1, 3, 2]) == 2.5

    # Unsorted input should be handled
    assert module_0.median([9, 1, 5, 3, 7]) == 5
    assert module_0.median([100, -100, 0]) == 0

    # Negative numbers
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([-2, -4]) == -3.0

    # Floats
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1.1, 2.2]) == 1.65

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0

    # Two elements
    assert module_0.median([1, 3]) == 2.0

    # Mixed ints and floats
    assert module_0.median([1, 2.0, 3]) == 2.0

    print("All median tests passed!")


if __name__ == "__main__":
    test_median()

# Generated at 2026-11-01 21:18:33.466914
# Unit test for function median
def test_median():
    # Odd number of elements
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([5, 3, 8, 1, 9]) == 5

    # Even number of elements
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([10, 20]) == 15.0

    # Single element
    assert module_0.median([7]) == 7

    # Two elements
    assert module_0.median([4, 2]) == 3.0

    # Unsorted input gets sorted
    assert module_0.median([9, 1, 5, 3]) == 4.0

    # Negative numbers
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([-10, 10]) == 0.0

    # Floats
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert abs(module_0.median([1.1, 2.2, 3.3, 4.4]) - 2.75) < 1e-9

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0

    # Mixed ints and floats
    assert module_0.median([1, 2.5, 3]) == 2.5

    print("All tests passed!")


if __name__ == "__main__":
    test_median()