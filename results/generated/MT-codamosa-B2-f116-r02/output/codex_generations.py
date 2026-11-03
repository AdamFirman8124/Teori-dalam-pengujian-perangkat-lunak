

# Generated at 2026-11-02 11:35:58.685134
# Unit test for function sort_array
def test_sort_array():
    # Empty list
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([1]) == [1]

    # Basic case: sorted first, then by number of 1s in binary
    # 1->1, 2->1, 4->1 (one '1'); 3->2, 5->2 (two '1's)
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Includes zero (bin '0' has zero '1's)
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

    # All powers of two keep sorted order
    assert module_0.sort_array([2, 4, 8, 16]) == [2, 4, 8, 16]

    # Duplicates
    assert module_0.sort_array([7, 7, 7]) == [7, 7, 7]

    # Mixed values: 3->'11'(2), 6->'110'(2), 7->'111'(3), 9->'1001'(2)
    assert module_0.sort_array([3, 6, 7, 9]) == [3, 6, 9, 7]

    # Negative numbers: bin(-n)[2:] includes 'b' prefix; counts computed accordingly
    # -2->'b10'(1), -4->'b100'(1), -3->'b11'(2), -5->'b101'(2), -6->'b110'(2)
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Already sorted by both criteria
    assert module_0.sort_array([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 4, 3, 5, 6, 7]

    # Larger range sanity check
    assert module_0.sort_array([10, 15, 7, 1, 0]) == [0, 1, 10, 7, 15]

# Generated at 2026-11-02 11:38:09.893731
# Unit test for function sort_array
def test_sort_array():
    # Basic case: numbers sorted first, then by count of 1s in binary
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    # 1=1(one 1), 2=10(one 1), 4=100(one 1), 3=11(two 1s), 5=101(two 1s)

    # Ties in bit count preserve ascending numeric order (stable sort)
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    # -6=110(two 1s), -5=101(two 1s), -4=100(one 1), -3=11(two 1s), -2=10(one 1)

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # Already sorted by bit count
    assert module_0.sort_array([2, 4, 8]) == [2, 4, 8]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [1, 1, 3, 3]

    # Mixed values: 0 has zero 1-bits and comes first
    assert module_0.sort_array([0, 1, 2, 3]) == [0, 1, 2, 3]

    # Powers of two all have a single 1-bit, so order stays numeric
    assert module_0.sort_array([16, 1, 8, 2, 4]) == [1, 2, 4, 8, 16]

    # Larger example
    assert module_0.sort_array([10, 15, 7, 8]) == [8, 10, 7, 15]
    # 8=1000(1), 10=1010(2), 7=111(3), 15=1111(4)

    print("All sort_array tests passed!")


if __name__ == "__main__":
    test_sort_array()