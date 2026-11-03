

# Generated at 2026-11-02 20:18:49.068537
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with a single element
    assert module_0.sum_product([5]) == (5, 5)

    # Test with multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([1, -2, 3]) == (2, -6)

    # Test with zeros
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)

    # Test with duplicates
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    # Test with large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 20:21:10.356475
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
    assert module_0.sum_product([-1, 2, -3, 4]) == (2, 24)

    # Test with zeros
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)

    # Test with all zeros
    assert module_0.sum_product([0, 0, 0]) == (0, 0)

    # Test with large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    # Test with duplicates
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 20:23:05.277102
# Unit test for function sum_product
def test_sum_product():
    # Empty list: sum is 0, product is 1 (multiplicative identity)
    assert module_0.sum_product([]) == (0, 1)

    # Single element
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([-3]) == (-3, -3)

    # Multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)
    assert module_0.sum_product([2, 5]) == (7, 10)

    # Contains zero: product becomes zero
    assert module_0.sum_product([1, 0, 5]) == (6, 0)
    assert module_0.sum_product([0]) == (0, 0)

    # Negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)
    assert module_0.sum_product([-1, 2, 3]) == (4, -6)

    # Larger values
    assert module_0.sum_product([10, 20, 30]) == (60, 6000)

    # Duplicates
    assert module_0.sum_product([3, 3, 3]) == (9, 27)

    # Result is a tuple
    result = module_0.sum_product([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 20:24:32.587613
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with single element
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([0]) == (0, 0)
    assert module_0.sum_product([-3]) == (-3, -3)

    # Test with multiple positive elements
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)
    assert module_0.sum_product([1, 2, 3]) == (6, 6)
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)
    assert module_0.sum_product([-1, 2, 3]) == (4, -6)

    # Test with zero in the list (product should be zero)
    assert module_0.sum_product([1, 0, 5]) == (6, 0)
    assert module_0.sum_product([0, 0, 0]) == (0, 0)

    # Test with large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()