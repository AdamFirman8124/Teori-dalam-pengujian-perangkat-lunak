

# Generated at 2026-11-02 13:10:48.400353
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max sort
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

    # Unsorted input
    assert module_0.strange_sort_list([3, 1, 2]) == [1, 3, 2]
    assert module_0.strange_sort_list([7, 2, 9, 4, 1]) == [1, 9, 2, 7, 4]

    # Single element
    assert module_0.strange_sort_list([42]) == [42]

    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Two elements
    assert module_0.strange_sort_list([2, 1]) == [1, 2]

    # Negative numbers
    assert module_0.strange_sort_list([-5, 3, -1, 0]) == [-5, 3, -1, 0]

    # Duplicates mixed with distinct values
    assert module_0.strange_sort_list([1, 2, 2, 3]) == [1, 3, 2, 2]

    # Already sorted input
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

    # Reverse sorted input
    assert module_0.strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]

    # Result contains same elements as original
    original = [10, 3, 7, 1, 9]
    result = module_0.strange_sort_list(original[:])
    assert sorted(result) == sorted(original)
    assert len(result) == len(original)

    print("All tests passed!")


test_strange_sort_list()

# Generated at 2026-11-02 13:11:57.078970
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max sorting
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([7]) == [7]

    # Unsorted input
    assert module_0.strange_sort_list([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 9, 1, 6, 2, 5, 3, 4]

    # Negative numbers
    assert module_0.strange_sort_list([-1, -5, 0, 3]) == [-5, 3, -1, 0]

    # Duplicates
    assert module_0.strange_sort_list([2, 2, 1, 3]) == [1, 3, 2, 2]

    # Two elements
    assert module_0.strange_sort_list([10, -10]) == [-10, 10]

    # Floats
    assert module_0.strange_sort_list([1.5, 0.5, 2.5]) == [0.5, 2.5, 1.5]

    # Result length preserved
    original = [4, 1, 7, 3, 9]
    result = module_0.strange_sort_list(original[:])
    assert len(result) == len(original)
    assert sorted(result) == sorted(original)

# Generated at 2026-11-02 13:13:20.861252
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max sorting
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    
    # Single element list
    assert module_0.strange_sort_list([7]) == [7]
    
    # Empty list
    assert module_0.strange_sort_list([]) == []
    
    # Two elements
    assert module_0.strange_sort_list([3, 1]) == [1, 3]
    
    # Unsorted input
    assert module_0.strange_sort_list([10, -2, 7, 0, 15]) == [-2, 15, 0, 10, 7]
    
    # List with negative numbers
    assert module_0.strange_sort_list([-5, -1, -10, -3]) == [-10, -1, -5, -3]
    
    # List with duplicates
    assert module_0.strange_sort_list([2, 2, 1, 3, 1]) == [1, 3, 1, 2, 2]
    
    # Odd number of elements
    assert module_0.strange_sort_list([4, 1, 7]) == [1, 7, 4]
    
    # Already result-like input
    assert module_0.strange_sort_list([1, 9, 2, 8]) == [1, 9, 2, 8]
    
    # Large numbers
    assert module_0.strange_sort_list([1000000, 1, 999999]) == [1, 1000000, 999999]
    
    # Floats
    assert module_0.strange_sort_list([1.5, 0.5, 2.5]) == [0.5, 2.5, 1.5]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_strange_sort_list()

# Generated at 2026-11-02 13:15:08.194612
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max ordering
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

    # Single element
    assert module_0.strange_sort_list([7]) == [7]

    # Two elements
    assert module_0.strange_sort_list([3, 1]) == [1, 3]

    # Duplicates mixed with other values
    assert module_0.strange_sort_list([2, 2, 1, 3]) == [1, 3, 2, 2]

    # Negative numbers
    assert module_0.strange_sort_list([-5, -1, -3, -2]) == [-5, -1, -3, -2]
    assert module_0.strange_sort_list([-2, 5, -8, 0]) == [-8, 5, -2, 0]

    # Already sorted input
    assert module_0.strange_sort_list([1, 2, 3]) == [1, 3, 2]

    # Reverse sorted input
    assert module_0.strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]

    # Floats
    assert module_0.strange_sort_list([1.5, 0.5, 2.5]) == [0.5, 2.5, 1.5]

    # Result is a permutation of the input (same multiset)
    import itertools
    original = [4, 1, 3, 2, 2]
    result = module_0.strange_sort_list(original[:])
    assert sorted(result) == sorted(original)
    assert len(result) == len(original)

    # Input list must not be mutated by the call
    data = [3, 1, 2]
    snapshot = data[:]
    module_0.strange_sort_list(data)
    assert data == snapshot

    # Verify alternating pattern explicitly for a known case
    out = module_0.strange_sort_list([10, 11, 12, 13, 14, 15])
    assert out == [10, 15, 11, 14, 12, 13]

    # Check all permutations produce the correct strange sort
    for perm in itertools.permutations([1, 2, 3, 4]):
        assert module_0.strange_sort_list(list(perm)) == [1, 4, 2, 3]

# Generated at 2026-11-02 13:17:47.464632
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Empty list
    assert module_0.strange_sort_list([]) == []
    
    # Single element
    assert module_0.strange_sort_list([1]) == [1]
    
    # Two elements
    assert module_0.strange_sort_list([1, 2]) == [1, 2]
    assert module_0.strange_sort_list([2, 1]) == [1, 2]
    
    # Multiple elements
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    
    # Unsorted input
    assert module_0.strange_sort_list([3, 1, 4, 2, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([10, -5, 3, 7, 0]) == [-5, 10, 0, 7, 3]
    
    # Negative numbers
    assert module_0.strange_sort_list([-1, -5, -3]) == [-5, -1, -3]
    
    # Duplicates
    assert module_0.strange_sort_list([2, 2, 1, 3]) == [1, 3, 2, 2]
    
    # Already sorted / reverse sorted
    assert module_0.strange_sort_list([1, 2, 3]) == [1, 3, 2]
    assert module_0.strange_sort_list([3, 2, 1]) == [1, 3, 2]
    
    # Floats
    assert module_0.strange_sort_list([1.5, 0.5, 2.5]) == [0.5, 2.5, 1.5]
    
    # Result length preserved
    original = [4, 1, 3, 2]
    assert len(module_0.strange_sort_list(original)) == len(original)