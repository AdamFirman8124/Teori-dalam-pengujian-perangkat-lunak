

# Generated at 2026-11-03 01:19:47.884499
# Unit test for function median
def test_median():
    # Odd-length list
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([10, 20, 30, 40, 50]) == 30

    # Even-length list
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([10, 2]) == 6.0

    # Single element
    assert module_0.median([5]) == 5

    # Unsorted input
    assert module_0.median([9, 1, 5, 3, 7]) == 5

    # Negative numbers
    assert module_0.median([-1, -5, -3]) == -3
    assert module_0.median([-2, -4]) == -3.0

    # Duplicates
    assert module_0.median([1, 1, 1]) == 1
    assert module_0.median([2, 2, 3, 3]) == 2.5

    # Floats
    assert module_0.median([1.5, 2.5, 0.5]) == 1.5
    assert module_0.median([1.1, 2.2, 3.3, 4.4]) == 2.75

    # Result should not modify original list order semantics (sorted copy used)
    data = [3, 1, 2]
    assert module_0.median(data) == 2
    assert data == [3, 1, 2]  # original unchanged

    # Mixed ints and floats
    assert module_0.median([1, 2.5, 3]) == 2.5

    # Even-length returning float type
    result = module_0.median([1, 2, 3, 4])
    assert isinstance(result, float)

    print("All median tests passed!")


if __name__ == "__main__":
    test_median()

# Generated at 2026-11-03 01:20:50.740493
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([5, 3, 8, 1, 9]) == 5


def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([10, 20]) == 15.0


def test_median_single_element():
    assert module_0.median([7]) == 7


def test_median_unsorted_input():
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([9, -2, 5, 1]) == 3.0


def test_median_negative_numbers():
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([-10, -20]) == -15.0


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1.1, 2.2]) == pytest.approx(1.65)


def test_median_duplicates():
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0


def test_median_does_not_modify_input():
    data = [3, 1, 2]
    module_0.median(data)
    assert data == [3, 1, 2]


def test_median_empty_list_raises():
    with pytest.raises(IndexError):
        module_0.median([])


def test_median_result_type():
    assert isinstance(module_0.median([1, 2, 3]), int)
    assert isinstance(module_0.median([1, 2, 3, 4]), float)


def run_tests():
    test_median_odd_length()
    test_median_even_length()
    test_median_single_element()
    test_median_unsorted_input()
    test_median_negative_numbers()
    test_median_floats()
    test_median_duplicates()
    test_median_does_not_modify_input()
    test_median_empty_list_raises()
    test_median_result_type()
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()

# Generated at 2026-11-03 01:22:15.841324
# Unit test for function median
def test_median():
    # Odd-length list
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([5, 3, 1, 4, 2]) == 3
    assert module_0.median([10]) == 10

    # Even-length list
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([1, 2]) == 1.5

    # Unsorted input
    assert module_0.median([9, 7, 5, 3, 1]) == 5
    assert module_0.median([-1, -3, -2]) == -2

    # Negative and mixed numbers
    assert module_0.median([-5, 5, 0]) == 0
    assert module_0.median([-10, -20, -30]) == -20

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0

    # Floats
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1.0, 2.0]) == 1.5

    # Empty list raises IndexError
    with pytest.raises(IndexError):
        module_0.median([])

# Generated at 2026-11-03 01:23:33.987918
# Unit test for function median
def test_median():
    # Odd-length list
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([10, 20, 30, 40, 50]) == 30

    # Even-length list (average of two middle elements)
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([10, 2]) == 6.0

    # Single element
    assert module_0.median([5]) == 5

    # Unsorted input should be handled
    assert module_0.median([9, 1, 5, 3, 7]) == 5
    assert module_0.median([4, 1, 3, 2]) == 2.5

    # Negative numbers
    assert module_0.median([-1, -5, -3]) == -3
    assert module_0.median([-10, 10]) == 0.0

    # Floats
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert abs(module_0.median([1.1, 2.2, 3.3, 4.4]) - 2.75) < 1e-9

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0

    # Original list should not be mutated by sorting
    data = [3, 1, 2]
    module_0.median(data)
    assert data == [3, 1, 2]

    print("All median tests passed!")


if __name__ == "__main__":
    test_median()

# Generated at 2026-11-03 01:25:27.505587
# Unit test for function median
def test_median():import pytest
from solution import median


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


def test_median_mixed_sign():
    assert module_0.median([-10, 4, 6, 1000, 10, 20]) == 10


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_with_duplicates():
    assert module_0.median([1, 2, 2, 3]) == 2.0


def test_median_two_elements():
    assert module_0.median([1, 2]) == 1.5


def test_median_does_not_modify_original():
    lst = [3, 1, 2]
    module_0.median(lst)
    assert lst == [3, 1, 2]


def test_median_empty_list_raises():
    with pytest.raises(IndexError):
        module_0.median([])