

# Generated at 2026-11-02 19:16:36.215750
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([5]) == [5]

    # First + last is odd -> ascending order
    # [2, 4, 3, 0, 1, 5] -> 2 + 5 = 7 (odd) -> sorted ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # First + last is even -> descending order
    # [2, 4, 3, 0, 1, 6] -> 2 + 6 = 8 (even) -> sorted descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 6]) == [6, 4, 3, 2, 1, 0]

    # First + last is odd -> ascending
    # [1, 3, 5] -> 1 + 5 = 6 (even) -> descending
    assert module_0.sort_array([1, 3, 5]) == [5, 3, 1]

    # First + last is odd -> ascending
    # [1, 2, 3] -> 1 + 3 = 4 (even) -> descending
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]

    # First + last is odd -> ascending
    # [2, 1, 3] -> 2 + 3 = 5 (odd) -> ascending
    assert module_0.sort_array([2, 1, 3]) == [1, 2, 3]

    # Negative numbers: first + last odd -> ascending
    assert module_0.sort_array([-2, 5, -1, 4]) == [-2, -1, 4, 5]

    # Negative numbers: first + last even -> descending
    assert module_0.sort_array([-2, 5, -1, 3]) == [5, 3, -1, -2]

    # Already sorted input, odd sum -> unchanged
    assert module_0.sort_array([1, 2, 4]) == [1, 2, 4]

    # Already sorted input, even sum -> reversed
    assert module_0.sort_array([1, 2, 5]) == [5, 2, 1]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [1, 1, 3, 3]  # 3+1=4 even -> descending
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]  # 3+2=5 odd -> ascending

# Generated at 2026-11-02 19:17:25.404230
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

    # Single element (first + last is the same element)
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Sum of first and last is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 (odd)
    assert module_0.sort_array([0, 1, 2, 3]) == [0, 1, 2, 3]               # 0+3=3 (odd)
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]                     # 3+2=5 (odd)

    # Sum of first and last is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 (even)
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]                     # 1+3=4 (even)
    assert module_0.sort_array([3, 1, 2, 1]) == [3, 2, 1, 1]               # 3+1=4 (even)

    # Negative numbers
    assert module_0.sort_array([-2, -1, 0, 1]) == [-2, -1, 0, 1]           # -2+1=-1 (odd)
    assert module_0.sort_array([-2, 0, 2]) == [2, 0, -2]                   # -2+2=0 (even)

    # Duplicates
    assert module_0.sort_array([1, 1, 1]) == [1, 1, 1]                     # 1+1=2 (even)

    # Original array should not be modified
    original = [2, 4, 3, 0, 1, 5]
    snapshot = list(original)
    module_0.sort_array(original)
    assert original == snapshot

# Generated at 2026-11-02 19:18:17.342746
# Unit test for function sort_array
def test_sort_array():
# nonce:d96a952c
    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Odd sum of first and last -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert module_0.sort_array([2, 1, 3]) == [1, 2, 3]
    assert module_0.sort_array([7, 1, 5, 3]) == [1, 3, 5, 7]

    # Even sum of first and last -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    assert module_0.sort_array([2, 2, 2]) == [2, 2, 2]

    # Negative numbers (Python: -3 % 2 == 1 -> odd -> ascending)
    assert module_0.sort_array([-1, -3, -2]) == [-3, -2, -1]
    assert module_0.sort_array([-2, -3, -1]) == [-3, -2, -1]
    # -1 + -1 = -2 (even) -> descending
    assert module_0.sort_array([-1, -3, -1]) == [-1, -1, -3]

    # Input array is not modified
    arr = [3, 1, 2]
    module_0.sort_array(arr)
    assert arr == [3, 1, 2]


if __name__ == "__main__":
    test_sort_array()
    print("All tests passed!")

# Generated at 2026-11-02 19:19:12.600725
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element: first+last is even -> sorted descending (same result)
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # first + last odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert module_0.sort_array([1, 4, 2, 3, 5, 6]) == [1, 2, 3, 4, 5, 6]  # 1+6=7 odd
    assert module_0.sort_array([3, 1, 2, 4, 6]) == [1, 2, 3, 4, 6]        # 3+6=9 odd

    # first + last even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]                          # 1+3=4 even
    assert module_0.sort_array([5, 1, 4, 2]) == [5, 4, 2, 1]                    # 5+2=7? no, 5+2=7 odd -> ascending check below
    # Correction: [5, 1, 4, 2]: 5+2=7 odd -> ascending
    assert module_0.sort_array([5, 1, 4, 2]) == [1, 2, 4, 5]

    assert module_0.sort_array([7, 1]) == [7, 1]   # 7+1=8 even -> descending
    assert module_0.sort_array([1, 7]) == [7, 1]   # 1+7=8 even -> descending

    # Duplicates and negatives
    assert module_0.sort_array([0, 0, 0]) == [0, 0, 0]                    # 0+0 even -> descending
    assert module_0.sort_array([-3, 2, -1, 4]) == [-3, -1, 2, 4]          # -3+4=1 odd -> ascending
    assert module_0.sort_array([-2, 3, 1]) == [3, 1, -2]                  # -2+1=-1 odd -> ascending? -1 % 2 == 1 in Python
    # Correction: (-2+1) = -1, and (-1) % 2 == 1 in Python -> odd -> ascending
    assert module_0.sort_array([-2, 3, 1]) == [-2, 1, 3]
    assert module_0.sort_array([-4, 2, 0]) == [2, 0, -4]                  # -4+0=-4, even -> descending

# Generated at 2026-11-02 19:19:57.326798
# Unit test for function sort_array
def test_sort_array():
    # Empty input
    assert module_0.sort_array([]) == []

    # Sum of first and last element is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert module_0.sort_array([2, 1]) == [1, 2]
    assert module_0.sort_array([15, 42, 87, 32, 11, 0]) == [0, 11, 15, 32, 42, 87]

    # Sum of first and last element is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert module_0.sort_array([21, 14, 23, 11]) == [23, 21, 14, 11]
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]

    # Single element (first == last, even sum -> descending, but unchanged)
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Duplicates
    assert module_0.sort_array([3, 3, 3]) == [3, 3, 3]
    assert module_0.sort_array([2, 2, 1, 1]) == [1, 1, 2, 2]