

# Generated at 2026-11-01 23:22:36.381862
# Unit test for function sort_array
def test_sort_array():
    # Sort by number of 1s in binary representation; ties broken by value
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([0, 1, 2, 3, 4]) == [0, 1, 2, 4, 3]
    # All elements have exactly one '1' bit -> stays ascending
    assert module_0.sort_array([8, 4, 2, 1]) == [1, 2, 4, 8]
    # Increasing counts of 1 bits
    assert module_0.sort_array([15, 7, 3, 1]) == [1, 3, 7, 15]
    # Empty array
    assert module_0.sort_array([]) == []
    # Single element
    assert module_0.sort_array([7]) == [7]
    # Duplicates preserved
    assert module_0.sort_array([3, 3, 3]) == [3, 3, 3]
    # Negative numbers (sign stripped by slicing, magnitude bits counted)
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]
    # Mixed positive numbers
    assert module_0.sort_array([2, 4, 8, 16, 32, 15]) == [2, 4, 8, 16, 32, 15]
    assert module_0.sort_array([10, 6, 12, 14]) == [10, 12, 6, 14]

# Generated at 2026-11-01 23:22:53.277209
# Unit test for function sort_array
def test_sort_array():
    # Basic case: ties in bit-count keep numeric order (stable sort)
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Zero has zero set bits, comes first
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

    # Empty list
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # Mixed values with differing popcounts
    # 1->1, 3->2, 6->2, 44->3, 900->4, 199->5
    assert module_0.sort_array([3, 6, 44, 199, 900, 1]) == [1, 3, 6, 44, 900, 199]

    # Duplicates preserved
    assert module_0.sort_array([2, 2, 3]) == [2, 2, 3]

    # Already ordered by both criteria
    assert module_0.sort_array([1, 2, 4, 8]) == [1, 2, 4, 8]

    print("All tests passed!")

if __name__ == "__main__":
    test_sort_array()

# Generated at 2026-11-01 23:23:05.466379
# Unit test for function sort_array
def test_sort_array():
    # Basic case: sorted numerically first, then by count of 1-bits
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # Already sorted input
    assert module_0.sort_array([1, 2, 4]) == [1, 2, 4]

    # Duplicates preserved
    assert module_0.sort_array([3, 3, 1]) == [1, 3, 3]

    # Negative numbers: bin(-n)[2:] skips sign/0b prefix correctly
    # -4 -> 'b100' (1 bit), -2 -> 'b10' (1 bit), -6/-5/-3 -> 2 bits
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Mixed values
    assert module_0.sort_array([0, 8, 15, 7, 3]) == [0, 8, 3, 7, 15]


test_sort_array()
print("All tests passed!")

# Generated at 2026-11-01 23:23:45.575889
# Unit test for function sort_array

# Generated at 2026-11-01 23:23:57.489820
# Unit test for function sort_array
def test_sort_array():assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

# Generated at 2026-11-01 23:24:42.947738
# Unit test for function sort_array

# Generated at 2026-11-01 23:24:56.426271
# Unit test for function sort_array
def test_sort_array():assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]