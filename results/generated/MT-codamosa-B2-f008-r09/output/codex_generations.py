

# Generated at 2026-11-02 09:59:35.815311
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with single element
    assert module_0.sum_product([5]) == (5, 5)

    # Test with multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with zeros
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([2, -3, 4]) == (3, -24)

    # Test with large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    # Test with duplicate values
    assert module_0.sum_product([3, 3, 3]) == (9, 27)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 10:00:32.999395
# Unit test for function sum_product
def test_sum_product():
    assert module_0.sum_product([]) == (0, 1)
    assert module_0.sum_product([1, 2, 3]) == (6, 6)
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)
    assert module_0.sum_product([2, -3]) == (-1, -6)
    assert module_0.sum_product([10, 20, 30]) == (60, 6000)
    assert module_0.sum_product([100]) == (100, 100)
    assert module_0.sum_product([1, 1, 1, 1]) == (4, 1)

# Generated at 2026-11-02 10:01:48.105877
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with single element
    assert module_0.sum_product([5]) == (5, 5)

    # Test with multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([-1, 2, 3]) == (4, -6)

    # Test with zero in the list
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)

    # Test with duplicates
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    # Test with large numbers
    assert module_0.sum_product([100, 200, 300]) == (600, 6000000)

    # Test with all zeros
    assert module_0.sum_product([0, 0, 0]) == (0, 0)

    # Test result is a tuple
    result = module_0.sum_product([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 10:02:35.114816
# Unit test for function sum_product
def test_sum_product():
    # Empty list: sum is 0, product is 1 (multiplicative identity)
    assert module_0.sum_product([]) == (0, 1)

    # Single element
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([-3]) == (-3, -3)

    # Multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # List containing zero (product should be 0)
    assert module_0.sum_product([1, 2, 0, 4]) == (7, 0)

    # Negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)
    assert module_0.sum_product([-1, 2, 3]) == (4, -6)

    # Mixed positive and negative
    assert module_0.sum_product([2, -5, 10]) == (7, -100)

    # Duplicates
    assert module_0.sum_product([3, 3, 3]) == (9, 27)

    # Larger values
    assert module_0.sum_product([100, 200]) == (300, 20000)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 10:03:49.573219
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with single element
    assert module_0.sum_product([5]) == (5, 5)

    # Test with multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with identical values
    assert module_0.sum_product([3, 3, 3]) == (9, 27)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([-1, 2, -3]) == (-2, 6)

    # Test with zero in the list
    assert module_0.sum_product([1, 2, 0, 4]) == (7, 0)

    # Test with large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()