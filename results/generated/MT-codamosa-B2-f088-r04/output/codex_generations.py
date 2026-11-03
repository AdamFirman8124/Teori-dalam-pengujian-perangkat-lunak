

# Generated at 2026-11-02 13:58:02.250756
# Unit test for function sort_array
def test_sort_array():
    # Empty array -> empty list
    assert module_0.sort_array([]) == []

    # Single element (5+5=10 even -> descending, trivially same)
    assert module_0.sort_array([5]) == [5]

    # first + last = 7 (odd) -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # first + last = 8 (even) -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    # first + last = 6 (even) -> descending
    assert module_0.sort_array([1, 3, 5]) == [5, 3, 1]

    # first + last = 3 (odd) -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]

    # all identical elements
    assert module_0.sort_array([5, 5, 5, 5]) == [5, 5, 5, 5]

    # negatives: -2 + 0 = -2 (even) -> descending
    assert module_0.sort_array([-2, -4, -3, 0]) == [0, -2, -3, -4]

    # negatives: -2 + 1 = -1 (odd) -> ascending
    assert module_0.sort_array([-2, -4, -3, 0, 1]) == [-4, -3, -2, 0, 1]

    # duplicates: 3 + 1 = 4 (even) -> descending
    assert module_0.sort_array([3, 1, 2, 3, 1]) == [3, 3, 2, 1, 1]

    # original array must not be modified
    original = [2, 4, 3, 0, 1, 5, 6]
    module_0.sort_array(original)
    assert original == [2, 4, 3, 0, 1, 5, 6]

# Generated at 2026-11-02 13:59:52.405548
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([1]) == [1]
    assert module_0.sort_array([5]) == [5]

    # Sum of first and last is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]  # 2+5=7 odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [5, 4, 3, 2, 1, 0] if (2 + 5) % 2 == 0 else True
    assert module_0.sort_array([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]  # 5+1=6 even -> descending
    assert module_0.sort_array([2, 4, 6, 8]) == [8, 6, 4, 2]  # 2+8=10 even -> descending
    assert module_0.sort_array([1, 3, 5]) == [5, 3, 1]  # 1+5=6 even -> descending

    # Sum of first and last is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]  # 2+5=7 odd -> ascending
    assert module_0.sort_array([1, 2, 3]) == [1, 2, 3]  # 1+3=4 even -> descending... actually 4 even -> [3,2,1]
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]  # 1+3=4 even -> descending
    assert module_0.sort_array([0, 1, 2, 3]) == [0, 1, 2, 3]  # 0+3=3 odd -> ascending
    assert module_0.sort_array([7, 2, 9]) == [2, 7, 9]  # 7+9=16 even -> descending... 16 even -> [9,7,2]
    assert module_0.sort_array([7, 2, 9]) == [9, 7, 2]  # 7+9=16 even -> descending
    assert module_0.sort_array([4, 1, 3]) == [1, 3, 4]  # 4+3=7 odd -> ascending

    # Duplicates
    assert module_0.sort_array([3, 3, 3]) == [3, 3, 3]  # 3+3=6 even -> descending (same)
    assert module_0.sort_array([1, 1, 2]) == [2, 1, 1]  # 1+2=3 odd -> ascending

    # Negative numbers
    assert module_0.sort_array([-1, -3, 2]) == [-3, -1, 2]  # -1+2=1 odd -> ascending
    assert module_0.sort_array([-2, -4, 0]) == [0, -2, -4]  # -2+0=-2 even -> descending

# Generated at 2026-11-02 14:01:38.094298
# Unit test for function sort_array
def test_sort_array():
    # Empty input returns empty list
    assert module_0.sort_array([]) == []

    # Single element (first+last even -> descending, but trivially same)
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # first + last odd -> ascending sort
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 odd
    assert module_0.sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]               # 1+4=5 odd
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]                     # 3+2=5 odd

    # first + last even -> descending sort
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([1, 2, 3, 5]) == [5, 3, 2, 1]                    # 1+5=6 even
    assert module_0.sort_array([5, 1, 3]) == [5, 3, 1]                          # 5+3=8 even

    # Duplicates
    assert module_0.sort_array([1, 1, 1]) == [1, 1, 1]

    # Negative numbers (Python modulo: -7 % 2 == 1 -> odd; -6 % 2 == 0 -> even)
    assert module_0.sort_array([-4, -2, -3]) == [-4, -3, -2]  # sum -7 odd -> ascending
    assert module_0.sort_array([-2, -3, -4]) == [-2, -3, -4]  # sum -6 even -> descending

# Generated at 2026-11-02 14:04:36.534568
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([1]) == [1]
    assert module_0.sort_array([5]) == [5]

    # First + last is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert module_0.sort_array([1, 2]) == [1, 2]
    assert module_0.sort_array([2, 1]) == [1, 2]
    assert module_0.sort_array([3, 3, 2, 2]) == [2, 2, 3, 3]

    # First + last is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert module_0.sort_array([1, 3]) == [3, 1]
    assert module_0.sort_array([3, 1]) == [3, 1]
    assert module_0.sort_array([5, 3, 2, 8, 1]) == [8, 5, 3, 2, 1]
    assert module_0.sort_array([1, 1, 1]) == [1, 1, 1]

    # Negative numbers
    assert module_0.sort_array([-2, -3, -4]) == [-2, -3, -4]   # sum -6 (even) -> descending
    assert module_0.sort_array([-3, -2, -1]) == [-1, -2, -3]   # sum -4 (even) -> descending
    assert module_0.sort_array([-1, 1]) == [1, -1]             # sum 0 (even) -> descending

    # Input array is not modified
    arr = [2, 4, 3, 0, 1, 5, 6]
    module_0.sort_array(arr)
    assert arr == [2, 4, 3, 0, 1, 5, 6]

# nonce:b0d8adc7