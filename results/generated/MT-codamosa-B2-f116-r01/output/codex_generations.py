

# Generated at 2026-11-03 00:19:13.053755
# Unit test for function sort_array

# Generated at 2026-11-03 00:20:59.765919
# Unit test for function sort_array
def test_sort_array():assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

# Generated at 2026-11-03 00:22:52.808516
# Unit test for function sort_array
def test_sort_array():
    # Basic case: sort by number of 1 bits, ties broken by numeric order
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    # 1 -> 1 one, 2 -> 1 one, 4 -> 1 one, 3 -> 2 ones, 5 -> 2 ones

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # Already sorted by bit count
    assert module_0.sort_array([0, 1, 3, 7]) == [0, 1, 3, 7]
    # 0 -> 0 ones, 1 -> 1 one, 3 -> 2 ones, 7 -> 3 ones

    # Reverse input order
    assert module_0.sort_array([7, 3, 1, 0]) == [0, 1, 3, 7]

    # Duplicates
    assert module_0.sort_array([2, 2, 1, 1]) == [1, 1, 2, 2]

    # Larger numbers
    # 8 -> 1000 (1 one), 6 -> 110 (2 ones), 15 -> 1111 (4 ones)
    assert module_0.sort_array([15, 6, 8]) == [8, 6, 15]

    # Stability check: equal bit counts keep numeric ascending order
    assert module_0.sort_array([9, 5, 3]) == [3, 5, 9]
    # 9 -> 1001 (2 ones), 5 -> 101 (2 ones), 3 -> 11 (2 ones)

    print("All tests passed!")

if __name__ == "__main__":
    test_sort_array()