

# Generated at 2026-11-02 12:55:39.912417
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with single element
    assert module_0.sum_product([5]) == (5, 5)

    # Test with multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with list containing zero
    assert module_0.sum_product([1, 2, 0, 4]) == (7, 0)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([-1, 2, -3]) == (-2, 6)

    # Test with large numbers
    assert module_0.sum_product([100, 200, 300]) == (600, 6000000)

    # Test with duplicate values
    assert module_0.sum_product([3, 3, 3]) == (9, 27)

    # Verify return type is a tuple
    result = module_0.sum_product([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 12:56:48.341358
# Unit test for function sum_product
def test_sum_product():
    assert module_0.sum_product([]) == (0, 1)
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([1, 2, 3, 4, 5]) == (15, 120)
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)
    assert module_0.sum_product([2, 3]) == (5, 6)
    assert module_0.sum_product([10]) == (10, 10)

# Generated at 2026-11-02 12:57:48.195714
# Unit test for function sum_product
def test_sum_product():# Empty list: identity values
    assert module_0.sum_product([]) == (0, 1)

    # Single element
    assert module_0.sum_product([5]) == (5, 5)

    # Multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Includes zero (product becomes zero)
    assert module_0.sum_product([1, 0, 5]) == (6, 0)

    # Negative numbers
    assert module_0.sum_product([-1, -2, 3]) == (0, 6)

    # Mixed positive and negative
    assert module_0.sum_product([-2, 3, 4]) == (5, -24)

    # Larger numbers
    assert module_0.sum_product([10, 20, 30]) == (60, 6000)

    # Duplicates
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    print("All tests passed!")

# Generated at 2026-11-02 12:59:29.243243
# Unit test for function sum_product
def test_sum_product():
    # Empty list: identity values
    assert module_0.sum_product([]) == (0, 1)

    # Single element
    assert module_0.sum_product([5]) == (5, 5)

    # Multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Includes zero (product should be zero)
    assert module_0.sum_product([1, 0, 5]) == (6, 0)

    # Negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Mixed positive and negative
    assert module_0.sum_product([2, -3, 4]) == (3, -24)

    # Duplicates
    assert module_0.sum_product([3, 3, 3]) == (9, 27)

    # Large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    print("All tests passed!")

# Generated at 2026-11-02 13:01:09.576075
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list: sum is 0, product is 1 (identity)
    assert module_0.sum_product([]) == (0, 1)

    # Test with a single element
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([0]) == (0, 0)
    assert module_0.sum_product([-7]) == (-7, -7)

    # Test with multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)
    assert module_0.sum_product([2, 3, 4]) == (9, 24)
    assert module_0.sum_product([10, 20, 30]) == (60, 6000)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)
    assert module_0.sum_product([-1, 2, 3]) == (4, -6)
    assert module_0.sum_product([-2, 4, -5]) == (-3, 40)

    # Test with zero in the list (product should be zero)
    assert module_0.sum_product([1, 0, 5]) == (6, 0)
    assert module_0.sum_product([0, 0, 0]) == (0, 0)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([-3, 3]) == (0, -9)

    # Test with larger values
    assert module_0.sum_product([100, 200, 300]) == (600, 6000000)

    # Test tuple unpacking of result
    s, p = module_0.sum_product([1, 2, 3, 4, 5])
    assert s == 15
    assert p == 120

    # Test return type is a tuple
    result = module_0.sum_product([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2