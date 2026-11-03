

# Generated at 2026-11-02 07:47:00.385230
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

# Generated at 2026-11-02 07:47:34.075098
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element array
    assert module_0.sort_array([5]) == [5]

    # First + last is odd -> ascending sort
    # [2, 4, 3, 0, 1, 5]: first=2, last=5, sum=7 (odd) -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # First + last is even -> descending sort
    # [2, 4, 3, 0, 1, 5, 6]: first=2, last=6, sum=8 (even) -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    # Already sorted ascending where sum of first and last is odd
    # [1, 2, 3]: first=1, last=3, sum=4 (even) -> descending
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]

    # Sum odd -> ascending even if input is descending
    # [5, 3, 1]: first=5, last=1, sum=6 (even) -> descending
    assert module_0.sort_array([5, 3, 1]) == [5, 3, 1]

    # Two elements, odd sum -> ascending
    # [3, 2]: first=3, last=2, sum=5 (odd) -> ascending
    assert module_0.sort_array([3, 2]) == [2, 3]

    # Two elements, even sum -> descending
    # [4, 2]: first=4, last=2, sum=6 (even) -> descending
    assert module_0.sort_array([4, 2]) == [4, 2]

    # Negative numbers, odd sum -> ascending
    # [-1, -5, 2]: first=-1, last=2, sum=1 (odd) -> ascending
    assert module_0.sort_array([-1, -5, 2]) == [-5, -1, 2]

    # Negative numbers, even sum -> descending
    # [-2, -5, 2]: first=-2, last=2, sum=0 (even) -> descending
    assert module_0.sort_array([-2, -5, 2]) == [2, -2, -5]

    # Duplicates, even sum -> descending
    # [1, 1, 3]: first=1, last=3, sum=4 (even) -> descending
    assert module_0.sort_array([1, 1, 3]) == [3, 1, 1]

    # Duplicates, odd sum -> ascending
    # [1, 3, 2]: first=1, last=2, sum=3 (odd) -> ascending
    assert module_0.sort_array([1, 3, 2]) == [1, 2, 3]

# Generated at 2026-11-02 07:48:33.735320
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

    # Single element (sum is even -> descending, but only one element)
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Odd sum of first and last -> ascending sort
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert module_0.sort_array([2, 4, 1, 3]) == [1, 2, 3, 4]
    assert module_0.sort_array([1, 0, 2]) == [0, 1, 2]

    # Even sum of first and last -> descending sort
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]
    assert module_0.sort_array([5, 1, 3]) == [5, 3, 1]
    assert module_0.sort_array([0, 1, 2, 3, 4]) == [4, 3, 2, 1, 0]
    assert module_0.sort_array([1, 3, 5, 7]) == [7, 5, 3, 1]

    # Negative numbers
    assert module_0.sort_array([-2, -1, 0, 1, 2]) == [2, 1, 0, -1, -2]
    assert module_0.sort_array([-3, -2, -1]) == [-1, -2, -3]
    assert module_0.sort_array([-1, 1]) == [1, -1]  # sum = 0 (even) -> descending

    # Duplicates
    assert module_0.sort_array([1, 1, 1]) == [1, 1, 1]
    assert module_0.sort_array([3, 1, 2, 1]) == [3, 2, 1, 1]  # sum = 4 (even) -> descending

    # Input array is not modified
    original = [3, 1, 2]
    assert module_0.sort_array(original) == [1, 2, 3]  # sum = 5 (odd) -> ascending
    assert original == [3, 1, 2]

# Generated at 2026-11-02 07:48:49.292857
# Unit test for function sort_array
def test_sort_array():
    # Test empty array
    assert module_0.sort_array([]) == []
    
    # Test single element array
    assert module_0.sort_array([5]) == [5]
    
    # Test odd sum of first and last -> ascending order
    # 2 + 5 = 7 (odd)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    
    # Test even sum of first and last -> descending order
    # 2 + 4 = 6 (even)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 4]) == [5, 4, 4, 3, 2, 1, 0]
    
    # Test with negative numbers, even sum -> descending
    # -1 + 3 = 2 (even)
    assert module_0.sort_array([-1, 0, 2, 3]) == [3, 2, 0, -1]
    
    # Test with negative numbers, odd sum -> ascending
    # -2 + 3 = 1 (odd)
    assert module_0.sort_array([-2, 5, 3]) == [-2, 3, 5]
    
    # Test first element equals last element -> even sum -> descending
    # 5 + 5 = 10 (even)
    assert module_0.sort_array([5, 1, 3, 5]) == [5, 5, 3, 1]
    
    # Test already sorted array with odd sum
    # 1 + 9 = 10 (even) -> descending
    assert module_0.sort_array([1, 2, 3, 9]) == [9, 3, 2, 1]
    
    # Test with duplicates
    # 3 + 2 = 5 (odd) -> ascending
    assert module_0.sort_array([3, 1, 2, 2, 3, 2]) == [1, 2, 2, 2, 3, 3]
    
    print("All tests passed!")

if __name__ == "__main__":
    test_sort_array()

# Generated at 2026-11-02 07:49:16.679853
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single-element array returns the same single element
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Sum of first and last element is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert module_0.sort_array([5, 1, 3, 2, 4]) == [1, 2, 3, 4, 5]
    assert module_0.sort_array([1, 2]) == [1, 2]          # 1+2=3 (odd)
    assert module_0.sort_array([2, 1]) == [1, 2]          # 2+1=3 (odd)

    # Sum of first and last element is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]    # 1+3=4 (even)
    assert module_0.sort_array([2, 4]) == [4, 2]          # 2+4=6 (even)

    # Arrays with duplicates
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]   # 3+2=5 (odd)
    assert module_0.sort_array([2, 2, 4, 4]) == [4, 4, 2, 2]   # 2+4=6 (even)

    # Negative numbers
    assert module_0.sort_array([-2, -4, -3, 0]) == [0, -2, -3, -4]  # -2+0=-2 (even)
    assert module_0.sort_array([-1, 5, -3, 2]) == [-3, -1, 2, 5]    # -1+2=1 (odd)

    # Result is a list and input array is not modified
    arr = [3, 1, 2]
    result = module_0.sort_array(arr)
    assert isinstance(result, list)
    assert arr == [3, 1, 2]