

# Generated at 2026-11-03 05:53:08.644628
# Unit test for function rolling_max
def test_rolling_max():
    # Test with an empty list
    assert module_0.rolling_max([]) == []

    # Test with a single element
    assert module_0.rolling_max([5]) == [5]

    # Test with an increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Test with a decreasing sequence
    assert module_0.rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]

    # Test with a mixed sequence
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # Test with negative numbers
    assert module_0.rolling_max([-1, -5, -3, -2]) == [-1, -1, -1, -1]

    # Test with duplicates
    assert module_0.rolling_max([2, 2, 2, 2]) == [2, 2, 2, 2]

    # Test with mixed positive and negative numbers
    assert module_0.rolling_max([-2, 1, -3, 4, -1, 2]) == [-2, 1, 1, 4, 4, 4]

    # Test with a large jump
    assert module_0.rolling_max([1, 100, 2, 50]) == [1, 100, 100, 100]

    print("All tests passed!")


if __name__ == "__main__":
    test_rolling_max()

# Generated at 2026-11-03 05:53:32.049320
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

    # Mixed sequence
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # With duplicates
    assert module_0.rolling_max([2, 2, 2, 2]) == [2, 2, 2, 2]

    # Negative numbers
    assert module_0.rolling_max([-3, -1, -5, -2]) == [-3, -1, -1, -1]

    # Mixed positive and negative
    assert module_0.rolling_max([-1, 0, -2, 3]) == [-1, 0, 0, 3]

    # Large values
    assert module_0.rolling_max([100, 50, 200, 150]) == [100, 100, 200, 200]

    print("All test cases passed!")


test_rolling_max()

# Generated at 2026-11-03 05:54:03.224589
# Unit test for function rolling_max
def test_rolling_max():
    # Empty list
    assert module_0.rolling_max([]) == []

    # Single element
    assert module_0.rolling_max([5]) == [5]

    # Increasing sequence - running max equals input
    assert module_0.rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Decreasing sequence - running max stays at first element
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    # Mixed values
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]

    # Classic example
    assert module_0.rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]

    # Duplicates
    assert module_0.rolling_max([2, 2, 2, 2]) == [2, 2, 2, 2]

    # Negative numbers
    assert module_0.rolling_max([-5, -3, -8, -1, -4]) == [-5, -3, -3, -1, -1]

    # Mix of negative and positive
    assert module_0.rolling_max([-2, 0, -1, 3, -5]) == [-2, 0, 0, 3, 3]

    # Zeros
    assert module_0.rolling_max([0, -1, 0, 1]) == [0, 0, 0, 1]

    print("All rolling_max tests passed!")


if __name__ == "__main__":
    test_rolling_max()

# Generated at 2026-11-03 05:55:18.798949
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

    # Test with duplicates
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

    # Test with negative numbers
    assert module_0.rolling_max([-3, -1, -2, -5]) == [-3, -1, -1, -1]

    # Test with zeros mixed in
    assert module_0.rolling_max([0, -1, 1, 0]) == [0, 0, 1, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test_rolling_max()

# Generated at 2026-11-03 05:55:52.901676
# Unit test for function rolling_max
def test_rolling_max():
    # Basic case with mixed values
    assert module_0.rolling_max([1, 2, 3, 2, 1]) == [1, 2, 3, 3, 3]

    # Strictly increasing sequence
    assert module_0.rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Strictly decreasing sequence
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    # Single element
    assert module_0.rolling_max([7]) == [7]

    # Empty list
    assert module_0.rolling_max([]) == []

    # All equal elements
    assert module_0.rolling_max([4, 4, 4, 4]) == [4, 4, 4, 4]

    # Negative numbers
    assert module_0.rolling_max([-5, -3, -10, -1]) == [-5, -3, -3, -1]

    # Mix of negative and positive
    assert module_0.rolling_max([-2, 0, -5, 3, 1]) == [-2, 0, 0, 3, 3]

    # Duplicates interleaved
    assert module_0.rolling_max([2, 1, 2, 3, 3, 1]) == [2, 2, 2, 3, 3, 3]

    # Large values
    assert module_0.rolling_max([10**9, -10**9, 10**9]) == [10**9, 10**9, 10**9]

    # Result length matches input length
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    assert len(module_0.rolling_max(numbers)) == len(numbers)
    assert module_0.rolling_max(numbers) == [3, 3, 4, 4, 5, 9, 9, 9]

    # Input list is not mutated
    original = [3, 1, 2]
    snapshot = list(original)
    module_0.rolling_max(original)
    assert original == snapshot


test_rolling_max()
print("All tests passed!")