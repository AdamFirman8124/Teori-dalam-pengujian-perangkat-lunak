

# Generated at 2026-11-02 08:17:04.277889
# Unit test for function rolling_max
def test_rolling_max():
    # Empty list
    assert module_0.rolling_max([]) == []

    # Single element
    assert module_0.rolling_max([5]) == [5]

    # Increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Decreasing sequence
    assert module_0.rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]

    # Mixed sequence
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # Duplicates
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

    # Negative numbers
    assert module_0.rolling_max([-5, -1, -3, -2]) == [-5, -1, -1, -1]

    # Mix of negative and positive
    assert module_0.rolling_max([-3, 0, -2, 7, 1]) == [-3, 0, 0, 7, 7]

    # Same value as running max reappears later
    assert module_0.rolling_max([10, 5, 10, 3]) == [10, 10, 10, 10]

    # Large numbers
    assert module_0.rolling_max([1000000, 999999, 1000001]) == [1000000, 1000000, 1000001]

    # Result length matches input length
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    assert len(module_0.rolling_max(numbers)) == len(numbers)

    # Running max never decreases
    result = module_0.rolling_max([5, 1, 8, 2, 9, 0])
    assert result == sorted(result)
    assert result == [5, 5, 8, 8, 9, 9]

    # Original input is not modified
    original = [4, 2, 7]
    module_0.rolling_max(original)
    assert original == [4, 2, 7]

# Generated at 2026-11-02 08:18:52.097939
# Unit test for function rolling_max
def test_rolling_max():
    # Empty list
    assert module_0.rolling_max([]) == []

    # Single element
    assert module_0.rolling_max([5]) == [5]

    # Increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Decreasing sequence
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    # Mixed values
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # Negative numbers
    assert module_0.rolling_max([-5, -2, -8, -1]) == [-5, -2, -2, -1]

    # Duplicates
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

    # All zeros
    assert module_0.rolling_max([0, 0, 0]) == [0, 0, 0]

    # Large values
    assert module_0.rolling_max([10**9, -10**9, 10**9]) == [10**9, 10**9, 10**9]

    # Spike pattern
    assert module_0.rolling_max([3, 1, 4, 1, 5, 9, 2, 6]) == [3, 3, 4, 4, 5, 9, 9, 9]

    print("All tests passed!")


if __name__ == "__main__":
    test_rolling_max()

# Generated at 2026-11-02 08:19:56.313808
# Unit test for function rolling_max
def test_rolling_max():
    # Basic increasing sequence
    assert module_0.rolling_max([1, 2, 3]) == [1, 2, 3]

    # Decreasing sequence - running max stays the same
    assert module_0.rolling_max([3, 2, 1]) == [3, 3, 3]

    # Mixed sequence
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # Empty list
    assert module_0.rolling_max([]) == []

    # Single element
    assert module_0.rolling_max([5]) == [5]

    # Negative numbers
    assert module_0.rolling_max([-5, -2, -10, -3]) == [-5, -2, -2, -2]

    # All duplicates
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

    # Zero and negatives mixed
    assert module_0.rolling_max([0, -1, 1]) == [0, 0, 1]

    # Large values
    assert module_0.rolling_max([100, 50, 200, 150]) == [100, 100, 200, 200]

    # Verify result length matches input length
    nums = [7, 1, 9, 4, 9, 2]
    result = module_0.rolling_max(nums)
    assert len(result) == len(nums)

    print("All rolling_max tests passed!")


if __name__ == "__main__":
    test_rolling_max()

# Generated at 2026-11-02 08:20:26.827959
# Unit test for function rolling_max
def test_rolling_max():
    # Basic case with mixed values
    assert module_0.rolling_max([1, 2, 3, 2, 1]) == [1, 2, 3, 3, 3]

    # Increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Decreasing sequence
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    # Single element
    assert module_0.rolling_max([7]) == [7]

    # Empty list
    assert module_0.rolling_max([]) == []

    # All equal elements
    assert module_0.rolling_max([4, 4, 4, 4]) == [4, 4, 4, 4]

    # Negative numbers
    assert module_0.rolling_max([-5, -3, -8, -1]) == [-5, -3, -3, -1]

    # Mixed positive and negative
    assert module_0.rolling_max([-1, 3, -2, 5, 0]) == [-1, 3, 3, 5, 5]

    # Two elements
    assert module_0.rolling_max([10, 1]) == [10, 10]
    assert module_0.rolling_max([1, 10]) == [1, 10]

    # Duplicates interspersed
    assert module_0.rolling_max([2, 1, 2, 3, 3, 1, 3]) == [2, 2, 2, 3, 3, 3, 3]

    # Large numbers
    assert module_0.rolling_max([1000000, 999999, 1000000]) == [1000000, 1000000, 1000000]

    # Zero values
    assert module_0.rolling_max([0, -1, 0, 1]) == [0, 0, 0, 1]

    print("All tests for rolling_max passed!")


# Run the tests
if __name__ == "__main__":
    test_rolling_max()

# Generated at 2026-11-02 08:21:00.710096
# Unit test for function rolling_max
def test_rolling_max():
    # Test with typical increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Test with mixed values
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # Test with decreasing sequence
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    # Test with negative numbers
    assert module_0.rolling_max([-1, -3, -2, -5]) == [-1, -1, -1, -1]

    # Test with single element
    assert module_0.rolling_max([7]) == [7]

    # Test with empty list
    assert module_0.rolling_max([]) == []

    # Test with duplicate values
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

    # Test with negative then positive
    assert module_0.rolling_max([-5, 0, 10, 3]) == [-5, 0, 10, 10]

    print("All test cases passed!")


if __name__ == "__main__":
    test_rolling_max()