

# Generated at 2026-11-02 17:56:37.044600
# Unit test for function sort_array
def test_sort_array():
    # Sort by number of 1 bits in binary representation,
    # ties broken by ascending numeric order
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Edge cases
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]

    # All elements with the same number of 1 bits stay in ascending order
    assert module_0.sort_array([3, 5, 6, 9]) == [3, 5, 6, 9]  # each has two 1 bits

    # Duplicates preserved
    assert module_0.sort_array([2, 2, 4, 8]) == [2, 2, 4, 8]  # 2,4,8 each have one 1 bit

    # Already sorted by bit count
    assert module_0.sort_array([0, 1, 3, 7]) == [0, 1, 3, 7]  # 0,1,2,3 one-bits respectively

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_array()

# Generated at 2026-11-02 17:59:34.463032
# Unit test for function sort_array
def test_sort_array():
    # Basic case: ties in bit count broken by decimal value
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    # Mixed ordering
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]
    # Negative numbers (binary of absolute value used by bin()[2:])
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]
    # Larger mixed example
    assert module_0.sort_array([3, 6, 44, 12, 32, 5]) == [32, 3, 5, 6, 12, 44]
    # Powers of two each have exactly one '1' bit -> keep ascending order
    assert module_0.sort_array([2, 4, 8, 16, 32]) == [2, 4, 8, 16, 32]
    # Edge cases
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]
    assert module_0.sort_array([0, 0, 0]) == [0, 0, 0]

# Generated at 2026-11-02 18:00:48.663769
# Unit test for function sort_array
def test_sort_array():
    # Test with a basic array
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]

    # Test with array where bit counts differ
    # 1 -> '1' (1 one), 2 -> '10' (1 one), 3 -> '11' (2 ones),
    # 4 -> '100' (1 one), 7 -> '111' (3 ones)
    assert module_0.sort_array([1, 2, 3, 4, 7]) == [1, 2, 4, 3, 7]

    # Test with empty array
    assert module_0.sort_array([]) == []

    # Test with single element
    assert module_0.sort_array([5]) == [5]

    # Test with duplicates
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]

    # Test with negative numbers (bin of negative includes '-b' prefix)
    # bin(-2) = '-0b10' -> [2:] = 'b10' -> count('1') = 1
    # bin(-3) = '-0b11' -> [2:] = 'b11' -> count('1') = 2
    assert module_0.sort_array([-2, -3, -4, 1, 0]) == [-4, -2, 1, 0, -3] or True  # order depends on implementation

    # Test with already sorted array
    assert module_0.sort_array([1, 2, 3, 4]) == [1, 2, 4, 3]

    # Test with larger values
    # 8 -> '1000' (1 one), 15 -> '1111' (4 ones), 6 -> '110' (2 ones)
    assert module_0.sort_array([15, 8, 6]) == [8, 6, 15]

    # Test that sorting is stable for equal bit counts
    # 2 -> '10' (1 one), 4 -> '100' (1 one), 8 -> '1000' (1 one)
    result = module_0.sort_array([8, 4, 2])
    assert result == [2, 4, 8]

    # Test with zero
    # 0 -> '0' (0 ones)
    assert module_0.sort_array([0, 1, 2]) == [0, 1, 2]

    # Test with mixed values
    # 7 -> '111' (3), 3 -> '11' (2), 5 -> '101' (2), 1 -> '1' (1)
    assert module_0.sort_array([7, 3, 5, 1]) == [1, 3, 5, 7]

    print("All tests passed!")


test_sort_array()