

# Generated at 2026-11-02 07:46:36.627570
# Unit test for function incr_list
def test_incr_list():
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]
    assert module_0.incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert module_0.incr_list([]) == []
    assert module_0.incr_list([0]) == [1]
    assert module_0.incr_list([-1, -5, -100]) == [0, -4, -99]
    assert module_0.incr_list([1.5, 2.5]) == [2.5, 3.5]
    assert module_0.incr_list([999999]) == [1000000]
    # Verify original list is not mutated
    original = [1, 2, 3]
    module_0.incr_list(original)
    assert original == [1, 2, 3]

# Generated at 2026-11-02 07:46:41.050483
# Unit test for function incr_list
def test_incr_list():
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]
    assert module_0.incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert module_0.incr_list([]) == []
    assert module_0.incr_list([0]) == [1]
    assert module_0.incr_list([-1, -2, -3]) == [0, -1, -2]
    assert module_0.incr_list([1000000]) == [1000001]
    assert module_0.incr_list([1, 1, 1]) == [2, 2, 2]

# Generated at 2026-11-02 07:46:47.290822
# Unit test for function incr_list
def test_incr_list():
    """Test basic incrementing of a list of positive integers."""
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]


def test_incr_list_empty():
    """Test that an empty list returns an empty list."""
    assert module_0.incr_list([]) == []


def test_incr_list_negative():
    """Test incrementing negative numbers."""
    assert module_0.incr_list([-1, -2, -3]) == [0, -1, -2]


def test_incr_list_mixed():
    """Test incrementing a mix of positive, negative, and zero."""
    assert module_0.incr_list([-1, 0, 1]) == [0, 1, 2]


def test_incr_list_single():
    """Test a single-element list."""
    assert module_0.incr_list([5]) == [6]


def test_incr_list_zeros():
    """Test a list of zeros."""
    assert module_0.incr_list([0, 0, 0]) == [1, 1, 1]


def test_incr_list_large_numbers():
    """Test with very large numbers."""
    assert module_0.incr_list([10**18, -10**18]) == [10**18 + 1, -10**18 + 1]


def test_incr_list_floats():
    """Test that floats are incremented correctly."""
    assert module_0.incr_list([1.5, -0.5]) == [2.5, 0.5]


def test_incr_list_does_not_mutate_input():
    """Test that the original list is not modified."""
    original = [1, 2, 3]
    module_0.incr_list(original)
    assert original == [1, 2, 3]


def test_incr_list_returns_new_list():
    """Test that a new list object is returned."""
    original = [1, 2, 3]
    result = module_0.incr_list(original)
    assert result is not original


def test_incr_list_duplicates():
    """Test a list with duplicate values."""
    assert module_0.incr_list([2, 2, 2]) == [3, 3, 3]

# Generated at 2026-11-02 07:47:03.665749
# Unit test for function incr_list
def test_incr_list():
    # Test with positive numbers
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]

    # Test with empty list
    assert module_0.incr_list([]) == []

    # Test with negative numbers
    assert module_0.incr_list([-1, -2, -3]) == [0, -1, -2]

    # Test with mixed positive, negative, and zero
    assert module_0.incr_list([0, -1, 5, -10, 100]) == [1, 0, 6, -9, 101]

    # Test with single element
    assert module_0.incr_list([5]) == [6]

    # Test with large numbers
    assert module_0.incr_list([999999, 1000000]) == [1000000, 1000001]

    # Test with floats
    assert module_0.incr_list([1.5, -2.5]) == [2.5, -1.5]

    # Test that original list is not modified
    original = [1, 2, 3]
    result = module_0.incr_list(original)
    assert original == [1, 2, 3]
    assert result == [2, 3, 4]

    # Test that result is a list
    assert isinstance(module_0.incr_list([1, 2]), list)

# Generated at 2026-11-02 07:47:36.738888
# Unit test for function incr_list
def test_incr_list():
    # Test with a basic list of positive integers
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]

    # Test with an empty list
    assert module_0.incr_list([]) == []

    # Test with negative numbers
    assert module_0.incr_list([-1, -2, -3]) == [0, -1, -2]

    # Test with zero
    assert module_0.incr_list([0]) == [1]

    # Test with a single element
    assert module_0.incr_list([5]) == [6]

    # Test with large numbers
    assert module_0.incr_list([999999, 1000000]) == [1000000, 1000001]

    # Test with floats
    assert module_0.incr_list([1.5, 2.5]) == [2.5, 3.5]

    # Test that original list is not modified
    original = [1, 2, 3]
    result = module_0.incr_list(original)
    assert original == [1, 2, 3]
    assert result == [2, 3, 4]

    # Test that a new list object is returned
    lst = [1, 2, 3]
    result = module_0.incr_list(lst)
    assert result is not lst

    # Test with mixed ints and floats
    assert module_0.incr_list([1, 2.5, -3]) == [2, 3.5, -2]

    # Test result correctness element-wise
    input_list = [10, 20, 30, 40]
    result = module_0.incr_list(input_list)
    for orig, inc in zip(input_list, result):
        assert inc == orig + 1

    print("All tests passed!")