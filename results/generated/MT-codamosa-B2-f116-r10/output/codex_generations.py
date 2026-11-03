

# Generated at 2026-11-03 04:31:31.305311
# Unit test for function sort_array
def test_sort_array():
    # nonce:abb2b72f
    # Basic case: sort by number of 1s in binary, ties broken by numeric order
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    # Includes zero
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]
    # Empty list
    assert module_0.sort_array([]) == []
    # Single element
    assert module_0.sort_array([7]) == [7]
    # Mixed values with differing bit counts
    assert module_0.sort_array([3, 6, 44, 12, 32, 5]) == [32, 3, 5, 6, 12, 44]
    # Powers of two all have exactly one '1' bit; stay in sorted order
    assert module_0.sort_array([2, 4, 8, 16, 32]) == [2, 4, 8, 16, 32]
    # Already sorted by both criteria
    assert module_0.sort_array([1, 2, 4, 8]) == [1, 2, 4, 8]

# Generated at 2026-11-03 04:34:36.422967
# Unit test for function sort_array
def test_sort_array():
    # Basic case: ties broken by numeric order (stable sort)
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Zero has zero set bits, comes first
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # All elements have the same number of set bits -> stays numerically sorted
    assert module_0.sort_array([2, 4, 8, 16]) == [2, 4, 8, 16]

    # Duplicates
    assert module_0.sort_array([3, 3, 1]) == [1, 3, 3]

    # Unsorted input with mixed bit counts
    assert module_0.sort_array([6, 1, 7, 3]) == [1, 6, 3, 7]  # 1:'1'(1), 6:'110'(2), 3:'11'(2), 7:'111'(3)

    # Negative numbers: bin(-x)[2:] includes 'b' prefix, count('1') still based on magnitude
    # -4 -> 'b100' (1), -2 -> 'b10' (1), -6 -> 'b110' (2), -5 -> 'b101' (2), -3 -> 'b11' (2)
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Input should not be mutated
    data = [3, 1, 2]
    module_0.sort_array(data)
    assert data == [3, 1, 2]

    # Result is sorted by (bit count, value) pairs
    result = module_0.sort_array([9, 1, 8, 2, 7, 3])
    assert result == [1, 2, 8, 3, 9, 7]  # counts: 1,1,1,2,2,3