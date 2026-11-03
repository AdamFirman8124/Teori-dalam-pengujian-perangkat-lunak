

# Generated at 2026-11-02 17:54:26.310620
# Unit test for function sum_product
def test_sum_product():
    # Test with empty list: sum is 0, product is 1 (multiplicative identity)
    assert module_0.sum_product([]) == (0, 1)

    # Test with a single element
    assert module_0.sum_product([5]) == (5, 5)

    # Test with multiple positive integers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([2, -3, 4]) == (3, -24)

    # Test with zero in the list (product should be 0)
    assert module_0.sum_product([0, 5, 7]) == (12, 0)

    # Test with duplicates
    assert module_0.sum_product([3, 3, 3]) == (9, 27)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 17:55:42.796057
# Unit test for function sum_product
def test_sum_product():
    from typing import List, Tuple

    # Test with empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with single element
    assert module_0.sum_product([5]) == (5, 5)

    # Test with multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with zero in list
    assert module_0.sum_product([1, 2, 0, 4]) == (7, 0)

    # Test with mixed positive and negative
    assert module_0.sum_product([2, -3, 4]) == (3, -24)

    # Test return type
    result = module_0.sum_product([1, 2, 3])
    assert isinstance(result, tuple) and len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 17:56:55.488577
# Unit test for function sum_product
def test_sum_product():
    # Empty list: sum is 0, product is 1 (multiplicative identity)
    assert module_0.sum_product([]) == (0, 1)

    # Single element
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([-3]) == (-3, -3)

    # Multiple positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Contains zero: product should be 0
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)

    # Negative numbers
    assert module_0.sum_product([-1, 2, 3]) == (4, -6)
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Mixed positive and negative
    assert module_0.sum_product([2, -3, 4]) == (3, -24)

    # Duplicates
    assert module_0.sum_product([7, 7, 7]) == (21, 343)

    # Larger values
    assert module_0.sum_product([100, 200, 300]) == (600, 6000000)

    # Result is a tuple
    result = module_0.sum_product([1, 2, 3])
    assert isinstance(result, tuple) and len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 17:58:26.448986
# Unit test for function sum_product
def test_sum_product():
    # Test with an empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with a single element list
    assert module_0.sum_product([5]) == (5, 5)

    # Test with multiple positive integers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([1, -2, 3]) == (2, -6)

    # Test with zero in the list
    assert module_0.sum_product([1, 0, 3]) == (4, 0)

    # Test with large numbers
    assert module_0.sum_product([100, 200, 300]) == (600, 6000000)

    # Test with duplicate values
    assert module_0.sum_product([2, 2, 2]) == (6, 8)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()

# Generated at 2026-11-02 18:00:03.687449
# Unit test for function sum_product
def test_sum_product():
    # Test with an empty list
    assert module_0.sum_product([]) == (0, 1)

    # Test with a single element
    assert module_0.sum_product([5]) == (5, 5)

    # Test with positive numbers
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)

    # Test with negative numbers
    assert module_0.sum_product([-1, -2, -3]) == (-6, -6)

    # Test with mixed positive and negative numbers
    assert module_0.sum_product([2, -3, 4]) == (3, -24)

    # Test with zeros
    assert module_0.sum_product([0, 1, 2]) == (3, 0)

    # Test with large numbers
    assert module_0.sum_product([100, 200]) == (300, 20000)

    # Test with duplicate values
    assert module_0.sum_product([3, 3, 3]) == (9, 27)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_product()