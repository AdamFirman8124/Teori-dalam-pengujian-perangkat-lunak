

# Generated at 2026-11-02 23:56:10.950550
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element: sum with itself is even, but only one element
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Odd sum of first and last -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]  # 2+5=7 odd
    assert module_0.sort_array([1, 3, 2]) == [1, 2, 3]                    # 1+2=3 odd
    assert module_0.sort_array([7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7]  # 7+1=8? no: 7+1=8 even -> descending
    # Correction for the case above: 7+1=8 is even -> descending
    assert module_0.sort_array([7, 6, 5, 4, 3, 2, 1]) == [7, 6, 5, 4, 3, 2, 1]

    # Even sum of first and last -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]                          # 1+3=4 even
    assert module_0.sort_array([4, 2, 8, 6]) == [8, 6, 4, 2]                    # 4+6=10 even

    # Duplicates handled correctly
    assert module_0.sort_array([3, 1, 3, 2]) == [1, 2, 3, 3]  # 3+2=5 odd -> ascending
    assert module_0.sort_array([2, 2, 2]) == [2, 2, 2]        # 2+2=4 even -> descending (same)

    # Negative numbers
    assert module_0.sort_array([-1, -3, -2]) == [-1, -2, -3]   # -1+-2=-3 odd -> ascending
    assert module_0.sort_array([-2, -4, -6]) == [-2, -4, -6]   # -2+-6=-8 even -> descending

# Generated at 2026-11-02 23:57:00.307488
# Unit test for function sort_array
def test_sort_array():
    # Test with empty array
    assert module_0.sort_array([]) == []

    # Test with single element array
    assert module_0.sort_array([5]) == [5]

    # Test with even sum of first and last elements -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [5, 4, 3, 2, 1, 0]
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    # Test with odd sum of first and last elements -> ascending order
    assert module_0.sort_array([1, 3, 5, 2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert module_0.sort_array([2, 1]) == [1, 2]

    # Test with negative numbers
    assert module_0.sort_array([-2, -4, -3, 0]) == [0, -2, -3, -4]
    assert module_0.sort_array([-2, -4, -3, -1]) == [-4, -3, -2, -1]

    # Test with duplicates
    assert module_0.sort_array([3, 3, 3]) == [3, 3, 3]
    assert module_0.sort_array([1, 2, 2, 3]) == [1, 2, 2, 3]

    # Test with two elements
    assert module_0.sort_array([4, 2]) == [4, 2]  # sum even -> descending
    assert module_0.sort_array([1, 2]) == [1, 2]  # sum odd -> ascending

    print("All tests passed!")

# Run the test
test_sort_array()

# Generated at 2026-11-02 23:58:27.440032
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns an empty list
    assert module_0.sort_array([]) == []

    # Single element: 5+5=10 (even) -> descending, result unchanged
    assert module_0.sort_array([5]) == [5]

    # First + last is odd (2+5=7) -> sorted ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # First + last is even (2+6=8) -> sorted descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]                    # 1+3=4 (even)
    assert module_0.sort_array([2, 1, 3]) == [1, 2, 3]                    # 2+3=5 (odd)
    assert module_0.sort_array([3, 6, 44, 10, 1]) == [44, 10, 6, 3, 1]    # 3+1=4 (even)
    assert module_0.sort_array([-2, -4, -3, 0]) == [0, -2, -3, -4]        # -2+0=-2 (even)

    # Original array must not be modified
    original = [3, 1, 2]
    result = module_0.sort_array(original)
    assert result == [1, 2, 3]      # 3+2=5 (odd) -> ascending
    assert original == [3, 1, 2]

test_sort_array()

# Generated at 2026-11-02 23:59:45.069748
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([5]) == [5]

    # Sum of first and last is odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]  # 2+5=7 (odd)

    # Sum of first and last is even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 4]) == [4, 3, 2, 1, 0]  # 2+4=6 (even)

    # Odd sum edge case
    assert module_0.sort_array([1, 3, 5]) == [1, 3, 5]  # 1+5=6 (even) -> descending
    assert module_0.sort_array([1, 3, 6]) == [1, 3, 6]  # 1+6=7 (odd) -> ascending

    # Duplicates
    assert module_0.sort_array([3, 3, 3]) == [3, 3, 3]  # 3+3=6 (even) -> descending

    # Negative numbers, odd sum -> ascending
    assert module_0.sort_array([-2, -5, 0, 3]) == [-5, -2, 0, 3]  # -2+3=1 (odd)

    # Negative numbers, even sum -> descending
    assert module_0.sort_array([-2, -5, 0, 4]) == [4, 0, -2, -5]  # -2+4=2 (even)

    # Already sorted inputs
    assert module_0.sort_array([1, 2, 3]) == [1, 2, 3]  # 1+3=4 (even) -> descending
    assert module_0.sort_array([1, 2, 4]) == [1, 2, 4]  # 1+4=5 (odd) -> ascending

    print("All test_sort_array tests passed!")


if __name__ == "__main__":
    test_sort_array()

# Generated at 2026-11-03 00:01:24.631956
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element array
    assert module_0.sort_array([5]) == [5]

    # Sum of first and last is odd -> ascending sort
    # 2 + 5 = 7 (odd)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # Sum of first and last is even -> descending sort
    # 2 + 6 = 8 (even)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    # Already sorted array with odd sum -> stays ascending
    # 1 + 7 = 8 (even) -> descending
    assert module_0.sort_array([1, 2, 3, 4, 5, 7]) == [7, 5, 4, 3, 2, 1]

    # Already sorted array with even sum -> reversed to descending
    # 1 + 6 = 7 (odd) -> ascending
    assert module_0.sort_array([1, 6, 5, 4, 3, 2]) == [1, 2, 3, 4, 5, 6]

    # Array with duplicates
    # 3 + 3 = 6 (even) -> descending
    assert module_0.sort_array([3, 1, 3, 2, 3]) == [3, 3, 3, 2, 1]

    # Negative numbers
    # -1 + 4 = 3 (odd) -> ascending
    assert module_0.sort_array([-1, 4, -3, 2]) == [-3, -1, 2, 4]

    # Negative numbers with even sum
    # -1 + 3 = 2 (even) -> descending
    assert module_0.sort_array([-1, 4, -3, 3]) == [4, 3, -1, -3]

    # Two elements, odd sum -> ascending
    # 1 + 2 = 3 (odd)
    assert module_0.sort_array([2, 1]) == [1, 2]

    # Two elements, even sum -> descending
    # 1 + 1 = 2 (even)
    assert module_0.sort_array([1, 1]) == [1, 1]

    print("All tests passed!")

if __name__ == "__main__":
    test_sort_array()