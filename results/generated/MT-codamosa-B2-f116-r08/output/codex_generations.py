

# Generated at 2026-11-02 15:54:35.496211
# Unit test for function sort_array
def test_sort_array():
    # Sorted by count of 1-bits in binary representation; ties broken by value
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

    # Edge cases
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]
    assert module_0.sort_array([0]) == [0]

    # Duplicates
    assert module_0.sort_array([2, 2, 1, 1]) == [1, 1, 2, 2]

    # Powers of two each have exactly one 1-bit
    assert module_0.sort_array([8, 4, 2, 1]) == [1, 2, 4, 8]

    # Mixed values
    assert module_0.sort_array([3, 8, 7, 6, 4]) == [4, 8, 3, 6, 7]
    assert module_0.sort_array([10, 15, 7, 1]) == [1, 10, 7, 15]

    # Negative numbers (bin(-n)[2:] yields 'b...' so key counts magnitude bits)
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    print("test_sort_array passed")

# Generated at 2026-11-02 15:56:52.786451
# Unit test for function sort_array
def test_sort_array():
    # Sorts by number of 1 bits in binary; ties broken by numeric value (stable sort)
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

# Generated at 2026-11-02 15:57:55.466780
# Unit test for function sort_array
def test_sort_array():
    # Basic sorting by number of 1s in binary representation
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    # 1->1, 2->1, 4->1 (stable order kept), 3->2, 5->2

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # All elements with a single 1-bit stay in ascending order
    assert module_0.sort_array([16, 2, 8, 4]) == [2, 4, 8, 16]

    # Already sorted input
    assert module_0.sort_array([1, 2, 3]) == [1, 2, 3]

    # Ties resolved by numeric order (stable sort after initial sort)
    assert module_0.sort_array([5, 3, 6, 1]) == [1, 3, 5, 6]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [1, 1, 3, 3]

    # Zero has zero 1-bits, comes first
    assert module_0.sort_array([1, 0, 3]) == [0, 1, 3]

    # Negative numbers: bin(-n)[2:] drops the sign, e.g. bin(-2) -> 'b10'
    assert module_0.sort_array([-2, -3, -4]) == [-4, -2, -3]

    # Larger mixed case
    assert module_0.sort_array([10, 1, 7, 15, 2]) == [1, 2, 10, 7, 15]
    # 1->1, 2->1, 10(1010)->2, 7(111)->3, 15(1111)->4

    print("All tests passed!")


test_sort_array()

# Generated at 2026-11-02 16:00:05.208219
# Unit test for function sort_array
def test_sort_array():
    # Sorts primarily by number of ones in binary representation
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Negative numbers: ones counted from magnitude's binary form
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # Ties in ones count broken by numeric value (stable pre-sort)
    assert module_0.sort_array([2, 1]) == [1, 2]
    assert module_0.sort_array([4, 2, 1]) == [1, 2, 4]

    # Zero has zero ones in binary, comes first
    assert module_0.sort_array([1, 0, 3]) == [0, 1, 3]

    # Duplicates preserved
    assert module_0.sort_array([3, 3, 1]) == [1, 3, 3]

    # Larger range: 0,1,2,4,8 have <=1 one; 3,5,6 have two; 7 has three
    assert module_0.sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]

    # Already sorted input remains sorted
    assert module_0.sort_array([1, 2, 3]) == [1, 2, 3]

    # Unsorted input with equal ones counts
    assert module_0.sort_array([9, 6, 3, 5]) == [3, 5, 6, 9]

# Generated at 2026-11-02 16:01:50.190993
# Unit test for function sort_array
def test_sort_array():
    # Sorted by number of 1-bits; ties broken by ascending value
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

    # Empty list
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # All elements have the same bit count -> plain ascending sort
    assert module_0.sort_array([9, 5, 6, 3]) == [3, 5, 6, 9]  # each has two 1-bits

    # Powers of two all have exactly one 1-bit
    assert module_0.sort_array([8, 4, 2, 1]) == [1, 2, 4, 8]

    # Input already in expected order
    assert module_0.sort_array([0, 1, 2, 4, 3]) == [0, 1, 2, 4, 3]

    # Mixed values requiring reordering by bit count
    assert module_0.sort_array([31, 1, 7, 3]) == [1, 3, 7, 31]
    # 31='11111' (5 ones), 1='1' (1), 7='111' (3), 3='11' (2)