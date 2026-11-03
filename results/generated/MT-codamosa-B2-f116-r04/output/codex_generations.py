

# Generated at 2026-11-02 23:54:04.177324
# Unit test for function sort_array
def test_sort_array():
    # nonce:21f6404d
    # Basic case: primary sort by count of 1-bits, ties broken by value
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Contains zero (zero has zero 1-bits, comes first)
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # All elements have the same bit count -> stays value-sorted
    assert module_0.sort_array([3, 6, 9]) == [3, 6, 9]

    # Powers of two all have exactly one 1-bit
    assert module_0.sort_array([16, 4, 1, 2]) == [1, 2, 4, 16]

    # Larger bit count sorts later even if its value is smaller
    assert module_0.sort_array([7, 8]) == [8, 7]

    # D

# Generated at 2026-11-02 23:54:48.927443
# Unit test for function sort_array
def test_sort_array():
    # Basic case: sorted by number of 1s in binary, ties broken by value
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # 0 comes first (zero 1s in binary)
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]

    # Negative numbers: bin(x)[2:] skips sign, counts 1 bits
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # Duplicates preserved
    assert module_0.sort_array([3, 3, 3]) == [3, 3, 3]

    # Already sorted input stays stable
    assert module_0.sort_array([1, 2, 4, 8]) == [1, 2, 4, 8]

    # Powers of two all have one 1-bit; sorted ascending
    assert module_0.sort_array([8, 4, 2, 1]) == [1, 2, 4, 8]

    # Mixed case with ties: 7 (111, three 1s) comes after 5 (101, two 1s)
    assert module_0.sort_array([7, 5, 6]) == [5, 6, 7]

# Generated at 2026-11-02 23:55:30.910219
# Unit test for function sort_array
def test_sort_array():
    # Basic case: sorted by value first, then by count of 1s in binary
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Negative numbers: bin(-x)[2:] includes 'b' prefix, count of '1' still works
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # Already sorted by both criteria
    assert module_0.sort_array([0, 1, 2, 3]) == [0, 1, 2, 3]

    # Duplicates preserved
    assert module_0.sort_array([2, 2, 1]) == [1, 2, 2]

    # Larger values
    assert module_0.sort_array([8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 4, 8, 3, 5, 6, 7]

    # Mixed positive numbers
    assert module_0.sort_array([10, 15, 7, 3]) == [3, 10, 7, 15]

# Generated at 2026-11-02 23:56:27.027881
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([1]) == [1]
    assert module_0.sort_array([0]) == [0]

    # Basic case: sorted by number of 1s in binary, ties broken by value
    # 1->'1'(1), 2->'10'(1), 3->'11'(2), 4->'100'(1), 5->'101'(2)
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Consecutive values 0-7
    # ones: 0->0, 1->1, 2->1, 3->2, 4->1, 5->2, 6->2, 7->3
    assert module_0.sort_array([0, 1, 2, 3, 4, 5, 6, 7]) == [0, 1, 2, 4, 3, 5, 6, 7]

    # Negative numbers: bin(-n)[2:] counts ones in magnitude
    # -2->'10'(1), -3->'11'(2), -4->'100'(1), -5->'101'(2), -6->'110'(2)
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Duplicates
    assert module_0.sort_array([3, 3, 1]) == [1, 3, 3]
    assert module_0.sort_array([5, 5, 5]) == [5, 5, 5]

    # Powers of two (single bit set) keep numeric order
    assert module_0.sort_array([8, 16, 15]) == [8, 16, 15]
    assert module_0.sort_array([2, 4, 8]) == [2, 4, 8]

    # Mixed with zero (zero has zero ones, sorts first)
    assert module_0.sort_array([7, 0, 5]) == [0, 5, 7]

    # Larger numbers
    # 1023->'1111111111'(10), 256->'100000000'(1), 255->'11111111'(8)
    assert module_0.sort_array([1023, 256, 255]) == [256, 255, 1023]

    # Already sorted input
    assert module_0.sort_array([1, 2, 4, 8]) == [1, 2, 4, 8]

    # Result is a list
    assert isinstance(module_0.sort_array([3, 1, 2]), list)

    print("All sort_array tests passed!")


if __name__ == "__main__":
    test_sort_array()

# Generated at 2026-11-02 23:59:28.786482
# Unit test for function sort_array

# Generated at 2026-11-03 00:01:13.033222
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([1, 5, 0, 3, 2]) == [0, 1, 2, 3, 5]
    assert module_0.sort_array([2, 3, 4, 5, 6]) == [2, 4, 3, 5, 6]
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]
    assert module_0.sort_array([0, 0, 1]) == [0, 0, 1]
    assert module_0.sort_array([8, 4, 2, 1]) == [8, 4, 2, 1]
    assert module_0.sort_array([6, 3, 5, 12]) == [3, 5, 6, 12]