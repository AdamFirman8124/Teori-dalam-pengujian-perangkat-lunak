

# Generated at 2026-11-03 02:52:14.156494
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
    assert module_0.sum_product([1, -2, 3]) == (2, -6)

    # Test with zeros in the list
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)

    # Test with all zeros
    assert module_0.sum_product([0, 0, 0]) == (0, 0)

    # Test with large numbers
    assert module_0.sum_product([100, 200, 300]) == (600, 6000000)

    # Test with duplicate values
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    # Test with one negative one positive
    assert module_0.sum_product([-5, 5]) == (0, -25)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-03 02:53:05.215395
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
    assert module_0.sum_product([1, -2, 3]) == (2, -6)

    # Test with zero in the list
    assert module_0.sum_product([1, 0, 3]) == (4, 0)

    # Test with large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    # Test with duplicate values
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-03 02:55:55.000312
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with single element
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([0]) == (0, 0)
    assert module_0.sum_product([-3]) == (-3, -3)

    # Test with multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)
    assert module_0.sum_product([1, 5, 7, -1, 5]) == (17, -175)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with zero in the list
    assert module_0.sum_product([1, 0, 5]) == (6, 0)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([2, -4, 6]) == (4, -48)

    # Test with large numbers
    assert module_0.sum_product([1000, 2000, 3000]) == (6000, 6000000000)

    # Test return type is a tuple
    result = module_0.sum_product([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("All tests passed!")

# Generated at 2026-11-03 02:57:41.593664
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
    assert module_0.sum_product([-2, 3, 4]) == (5, -24)

    # Test with zero in the list
    assert module_0.sum_product([1, 0, 5]) == (6, 0)

    # Test with all zeros
    assert module_0.sum_product([0, 0, 0]) == (0, 0)

    # Test with large numbers
    assert module_0.sum_product([100, 200, 300]) == (600, 6000000)

    # Test result type is a tuple
    result = module_0.sum_product([1, 2, 3])
    assert isinstance(result, tuple)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-03 02:59:51.647325
# Unit test for function sum_product
def test_sum_product():
    # Empty list: sum is 0, product is 1 (multiplicative identity)
    assert module_0.sum_product([]) == (0, 1)

    # Single element
    assert module_0.sum_product([5]) == (5, 5)

    # Multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # List with zero
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)

    # Negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Mixed positive and negative
    assert module_0.sum_product([-2, 3, 4]) == (5, -24)

    # Duplicates
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    # Large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()