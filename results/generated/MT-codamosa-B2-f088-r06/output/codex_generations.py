

# Generated at 2026-11-02 23:44:46.398146
# Unit test for function sort_array
def test_sort_array():import pytest


def test_empty_array():
    """Empty array returns empty list."""
    assert module_0.sort_array([]) == []


def test_single_element():
    """Single element array returns itself."""
    assert module_0.sort_array([5]) == [5]


def test_odd_sum_sorts_ascending():
    """First + last odd -> ascending sort."""
    # 2 + 5 = 7 (odd) -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]


def test_even_sum_sorts_descending():
    """First + last even -> descending sort."""
    # 2 + 4 = 6 (even) -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [5, 4, 3, 2, 1, 0]


def test_even_sum_example_two():
    # 1 + 3 = 4 (even) -> descending
    assert module_0.sort_array([1, 0, 2, 3]) == [3, 2, 1, 0]


def test_negative_numbers():
    """Works with negative numbers."""
    # -1 + 1 = 0 (even) -> descending
    assert module_0.sort_array([-1, 5, 0, 1]) == [5, 1, 0, -1]
    # -2 + -1 = -3 (odd) -> ascending
    assert module_0.sort_array([-2, 3, -5, -1]) == [-5, -2, -1, 3]


def test_all_equal_elements():
    """All same elements returns same list either way."""
    assert module_0.sort_array([7, 7, 7, 7]) == [7, 7, 7, 7]


def test_original_not_modified():
    """Input array is not mutated."""
    arr = [3, 1, 2]
    module_0.sort_array(arr)
    assert arr == [3, 1, 2]


def test_duplicates():
    """Handles duplicate values correctly."""
    # 2 + 2 = 4 (even) -> descending
    assert module_0.sort_array([2, 1, 2, 3]) == [3, 2, 2, 1]


def test_two_elements():
    """Two element arrays follow the parity rule."""
    # 1 + 2 = 3 (odd) -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]
    # 1 + 1 = 2 (even) -> descending
    assert module_0.sort_array([1, 1]) == [1, 1]


def test_large_numbers():
    """Handles large integer values."""
    arr = [10**9, -10**9, 0]
    # 10**9 + 0 is even -> descending
    assert module_0.sort_array(arr) == [10**9, 0, -10**9]

# Generated at 2026-11-02 23:46:01.253675
# Unit test for function sort_array
def test_sort_array():
    # Empty input returns an empty list
    assert module_0.sort_array([]) == []

    # Single-element arrays
    assert module_0.sort_array([1]) == [1]
    assert module_0.sort_array([7]) == [7]

    # First + last is odd -> ascending sort
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]      # 2+5=7 (odd)
    assert module_0.sort_array([1, 2, 4]) == [1, 2, 4]                        # 1+4=5 (odd)

# Generated at 2026-11-02 23:47:14.882063
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []
    
    # Single element array (first + last = same element, even sum -> descending)
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]
    
    # Sum of first and last is odd -> ascending sort
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]  # 2+5=7 odd
    assert module_0.sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]  # 1+4=5 odd
    assert module_0.sort_array([10, 1, 9, 2, 8]) == [1, 2, 8, 9, 10]  # 10+8=18... even -> descending
    
    # Sum of first and last is even -> descending sort
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]  # 5+1=6 even
    assert module_0.sort_array([10, 1, 9, 2, 7]) == [10, 9, 7, 2, 1]  # 10+7=17 odd -> ascending
    
    # Negative numbers
    assert module_0.sort_array([-2, -4, -3, 0]) == [0, -2, -3, -4]  # -2+0=-2 even -> descending
    assert module_0.sort_array([-1, -3, -2, 4]) == [-3, -2, -1, 4]  # -1+4=3 odd -> ascending
    
    # Duplicates
    assert module_0.sort_array([3, 3, 3, 3]) == [3, 3, 3, 3]  # 3+3=6 even -> descending
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_sort_array()

# nonce:04adad6d

# Generated at 2026-11-02 23:48:01.366450
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element array
    assert module_0.sort_array([5]) == [5]

    # First + last is odd -> sorted ascending
    # e.g., [2, 4, 3, 0, 1, 5] -> 2 + 5 = 7 (odd)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # First + last is even -> sorted descending
    # e.g., [2, 4, 3, 0, 1, 5, 6] -> 2 + 6 = 8 (even)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    # Odd sum with negative numbers -> ascending
    # e.g., [3, 1, 2] -> 3 + 2 = 5 (odd)
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]

    # Even sum with negative numbers -> descending
    # e.g., [-2, -3, -4] -> -2 + -4 = -6 (even)
    assert module_0.sort_array([-2, -3, -4]) == [-2, -3, -4]

    # Odd sum with negatives -> ascending
    # e.g., [-2, -3, -5] -> -2 + -5 = -7 (odd)
    assert module_0.sort_array([-2, -3, -5]) == [-5, -3, -2]

    # Array with duplicates, even sum -> descending
    # e.g., [1, 3, 1] -> 1 + 1 = 2 (even)
    assert module_0.sort_array([1, 3, 1]) == [3, 1, 1]

    # Already sorted input, odd sum -> stays ascending
    assert module_0.sort_array([1, 2, 3]) == [1, 2, 3]

    # Already sorted descending, even sum -> stays descending
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]

    print("All tests passed!")

# Generated at 2026-11-02 23:48:58.306988
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([5]) == [5]

    # First + last is odd -> sorted ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 (odd)
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]                     # 3+2=5 (odd)

    # First + last is even -> sorted descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 (even)
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]                     # 1+3=4 (even)

    # Duplicates
    assert module_0.sort_array([2, 2, 2]) == [2, 2, 2]

    # Negative numbers
    assert module_0.sort_array([-2, -3, -1]) == [-3, -2, -1]               # -2+(-1)=-3 (odd)
    assert module_0.sort_array([-2, -5, -4]) == [-2, -4, -5]               # -2+(-4)=-6 (even)
# nonce:6d44cb95