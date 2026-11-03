

# Generated at 2026-11-02 00:34:59.250095
# Unit test for function rolling_max
def test_rolling_max():
    # Increasing sequence - each element becomes the new max
    assert module_0.rolling_max([1, 2, 3]) == [1, 2, 3]

    # Decreasing sequence - first element stays the max
    assert module_0.rolling_max([3, 2, 1]) == [3, 3, 3]

    # Mixed sequence
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # Empty list
    assert module_0.rolling_max([]) == []

    # Single element
    assert module_0.rolling_max([5]) == [5]

    # Negative numbers (decreasing)
    assert module_0.rolling_max([-1, -2, -3]) == [-1, -1, -1]

    # Negative numbers (increasing)
    assert module_0.rolling_max([-3, -2, -1]) == [-3, -2, -1]

    # All equal values
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

    # Duplicates with mixed order
    assert module_0.rolling_max([4, 1, 4, 0, 7, 7]) == [4, 4, 4, 4, 7, 7]

    # Large values
    assert module_0.rolling_max([1000000, 999999, 1000001]) == [1000000, 1000000, 1000001]

    print("All test_rolling_max tests passed!")


if __name__ == "__main__":
    test_rolling_max()

# Generated at 2026-11-02 00:35:31.265554
# Unit test for function rolling_max
def test_rolling_max():
    # Test with strictly increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test with strictly decreasing sequence
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    # Test with mixed values
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # Test with empty list
    assert module_0.rolling_max([]) == []

    # Test with single element
    assert module_0.rolling_max([7]) == [7]

    # Test with negative numbers
    assert module_0.rolling_max([-5, -3, -4, -1]) == [-5, -3, -3, -1]

    # Test with all duplicates
    assert module_0.rolling_max([2, 2, 2, 2]) == [2, 2, 2, 2]

    # Test with negative and positive mixed
    assert module_0.rolling_max([-1, 0, -2, 3, -4]) == [-1, 0, 0, 3, 3]

# Generated at 2026-11-02 00:36:28.514578
# Unit test for function rolling_max
def test_rolling_max():
    # Typical increasing/decreasing mix
    assert module_0.rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]

    # Empty list returns empty list
    assert module_0.rolling_max([]) == []

    # Single element
    assert module_0.rolling_max([5]) == [5]

    # Strictly increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Strictly decreasing sequence (running max stays at first element)
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    # All identical elements
    assert module_0.rolling_max([7, 7, 7, 7]) == [7, 7, 7, 7]

    # Negative numbers
    assert module_0.rolling_max([-3, -1, -7, -2]) == [-3, -1, -1, -1]

    # Mix of negative and positive
    assert module_0.rolling_max([-5, 0, -10, 10, 3]) == [-5, 0, 0, 10, 10]

    # Two elements
    assert module_0.rolling_max([2, 1]) == [2, 2]
    assert module_0.rolling_max([1, 2]) == [1, 2]


if __name__ == "__main__":
    test_rolling_max()
    print("All tests passed!")

# Generated at 2026-11-02 00:37:26.362197
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([1, 2, 3]) == [1, 2, 3]
    assert module_0.rolling_max([3, 2, 1]) == [3, 3, 3]
    assert module_0.rolling_max([1, 3, 2]) == [1, 3, 3]
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([5]) == [5]
    assert module_0.rolling_max([-1, -3, -2]) == [-1, -1, -1]
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]
    assert module_0.rolling_max([1, 5, 3, 7, 2]) == [1, 5, 5, 7, 7]
    assert module_0.rolling_max([10, 4, 8, 12, 6]) == [10, 10, 10, 12, 12]
    assert module_0.rolling_max([-5, -10, -1, -3]) == [-5, -5, -1, -1]

# Generated at 2026-11-02 00:38:51.502233
# Unit test for function rolling_max
def test_rolling_max():
    # Test with empty list
    assert module_0.rolling_max([]) == []

    # Test with single element
    assert module_0.rolling_max([1]) == [1]

    # Test with increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test with decreasing sequence
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    # Test with mixed sequence (from original example)
    assert module_0.rolling_max([1, 2, 4, 1, 5, 8, 2, 3]) == [1, 2, 4, 4, 5, 8, 8, 8]

    # Test with duplicates
    assert module_0.rolling_max([3, 3, 3, 3]) == [3, 3, 3, 3]

    # Test with negative numbers
    assert module_0.rolling_max([-5, -3, -10, -1]) == [-5, -3, -3, -1]

    # Test with negative and positive numbers
    assert module_0.rolling_max([-2, 0, -5, 3, 1]) == [-2, 0, 0, 3, 3]

    # Test with zero
    assert module_0.rolling_max([0, -1, 1, 0]) == [0, 0, 1, 1]

    # Test with large numbers
    assert module_0.rolling_max([1000000, 999999, 1000001]) == [1000000, 1000000, 1000001]

    # Test that input list is not modified
    original = [3, 1, 2]
    module_0.rolling_max(original)
    assert original == [3, 1, 2]

    # Test result length matches input length
    test_input = [7, 2, 9, 4, 6]
    assert len(module_0.rolling_max(test_input)) == len(test_input)


if __name__ == "__main__":
    test_rolling_max()
    print("All tests passed!")