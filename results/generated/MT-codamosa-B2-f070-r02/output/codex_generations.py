

# Generated at 2026-11-02 13:00:03.477616
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max ordering
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([3, 1, 2]) == [1, 3, 2]
    assert module_0.strange_sort_list([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
    assert module_0.strange_sort_list([-5, -1, -3, -2, -4]) == [-5, -1, -4, -2, -3]
    assert module_0.strange_sort_list([10, -10, 0]) == [-10, 10, 0]
    assert module_0.strange_sort_list([2, 2, 1, 1]) == [1, 2, 1, 2]

    print("All test cases passed!")


if __name__ == "__main__":
    test_strange_sort_list()

# Generated at 2026-11-02 13:02:03.848059
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Test with typical sorted list
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    # Test with unsorted list
    assert module_0.strange_sort_list([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
    # Test with single element
    assert module_0.strange_sort_list([1]) == [1]
    # Test with empty list
    assert module_0.strange_sort_list([]) == []
    # Test with duplicates
    assert module_0.strange_sort_list([2, 2, 2, 2]) == [2, 2, 2, 2]
    # Test with negative numbers
    assert module_0.strange_sort_list([-1, -5, -3, -2]) == [-5, -1, -3, -2]
    # Test with mixed values including duplicates
    assert module_0.strange_sort_list([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 9, 1, 6, 2, 5, 3, 4]
    # Test with two elements
    assert module_0.strange_sort_list([10, 1]) == [1, 10]
    # Test with three elements
    assert module_0.strange_sort_list([7, 3, 5]) == [3, 7, 5]
    # Test with odd number of elements
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    # Test with floats
    assert module_0.strange_sort_list([1.5, 0.5, 2.5]) == [0.5, 2.5, 1.5]

# Generated at 2026-11-02 13:04:46.800724
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([3, 1, 2]) == [1, 3, 2]
    assert module_0.strange_sort_list([-2, -5, -1, -3]) == [-5, -1, -3, -2]
    assert module_0.strange_sort_list([10, 0, 10, 0]) == [0, 10, 0, 10]

# Generated at 2026-11-02 13:06:44.834839
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Alternates min, max, min, max... of remaining elements
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, -1, 2, -2, 3, -3]) == [-3, 3, -2, 2, -1, 1]
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([2, 1]) == [1, 2]
    assert module_0.strange_sort_list([3, 1, 2]) == [1, 3, 2]
    assert module_0.strange_sort_list([10, 20, 30, 40, 50]) == [10, 50, 20, 40, 30]
    assert module_0.strange_sort_list([-5, -1, -3]) == [-5, -1, -3]
    assert module_0.strange_sort_list([0, 0, 1, 1]) == [0, 1, 0, 1]
    print("All tests passed!")