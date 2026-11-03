

# Generated at 2026-11-02 23:42:02.354446
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # All positive numbers: minimum sub-array is the smallest single element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([1, 2, 3, 4, 5]) == 1
    assert module_0.minSubArraySum([10, 20, 30]) == 10

    # All negative numbers: minimum sub-array is the sum of all elements
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-2, -2, -2]) == -6
    assert module_0.minSubArraySum([-1]) == -1

    # Mixed positive and negative numbers
    assert module_0.minSubArraySum([-1, -2, -3, 2, -10, 14]) == -10
    assert module_0.minSubArraySum([1, -1]) == -1
    assert module_0.minSubArraySum([10, -5, 2]) == -5
    assert module_0.minSubArraySum([-5, 10, -5]) == -5
    assert module_0.minSubArraySum([2, -3, 4, -1, 5]) == -3
    assert module_0.minSubArraySum([3, -4, 1, 2, -1]) == -4

    # Single element lists
    assert module_0.minSubArraySum([1]) == 1
    assert module_0.minSubArraySum([0]) == 0
    assert module_0.minSubArraySum([-100]) == -100

    # Contains zero
    assert module_0.minSubArraySum([0, 1, 2]) == 0
    assert module_0.minSubArraySum([1, 0, -2]) == -2
    assert module_0.minSubArraySum([0, 0, 0]) == 0

    # Larger mixed example
    assert module_0.minSubArraySum([1, -2, 3, -4, 5, -6]) == -6
    assert module_0.minSubArraySum([5, -3, 5]) == -3

# Generated at 2026-11-02 23:43:25.038134
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([2, 3, 4, 1, 2, -4, 2]) == -4

# Generated at 2026-11-02 23:44:59.916772
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # Test with mixed positive numbers (single smallest element)
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # Test with all negative numbers (whole array is the minimum subarray)
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    # Test with negatives followed by positives
    assert module_0.minSubArraySum([-1, -2, -3, 4, 5, 6]) == -6
    # Test with single negative element
    assert module_0.minSubArraySum([-1]) == -1
    # Test with single positive element
    assert module_0.minSubArraySum([1]) == 1
    # Test with large mixed numbers
    assert module_0.minSubArraySum([10, 20, 30, 40, 100, -10, 200]) == -10
    # Test with all zeros
    assert module_0.minSubArraySum([0, 0, 0]) == 0
    # Test with all positive numbers (single smallest element is minimum)
    assert module_0.minSubArraySum([3, 4, 5]) == 3
    # Test with negative then positive (negative alone is smaller)
    assert module_0.minSubArraySum([-5, 10]) == -5
    # Test with two negative elements (sum of both is minimum)
    assert module_0.minSubArraySum([-2, -3]) == -5
    # Test with positive then negative (negative alone is smaller)
    assert module_0.minSubArraySum([10, -5]) == -5
    # Test with alternating signs
    assert module_0.minSubArraySum([1, -1, 1, -1]) == -1

# Generated at 2026-11-02 23:46:17.258337
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # Basic positive-only array: min subarray is the smallest element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # All negative numbers: min subarray is the whole array
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    # Mixed values
    assert module_0.minSubArraySum([3, -4, 1]) == -4
    assert module_0.minSubArraySum([1, -1]) == -1
    # Longer mixed array
    assert module_0.minSubArraySum([1, -4, -2, -1, -1, 3, 5, -7, 3, 9]) == -8
    # Single element
    assert module_0.minSubArraySum([1]) == 1
    assert module_0.minSubArraySum([-5]) == -5
    # Contains zero
    assert module_0.minSubArraySum([0, 10, 20]) == 0
    assert module_0.minSubArraySum([5, -3, -3, 2, 3, -1]) == -6
    # Two negative elements
    assert module_0.minSubArraySum([-2, -3]) == -5
    # Positive followed by negative
    assert module_0.minSubArraySum([10, -20]) == -20
    # All zeros
    assert module_0.minSubArraySum([0, 0, 0]) == 0
    # Large values
    assert module_0.minSubArraySum([1000000, -2000000, 3000000]) == -2000000

# nonce:c02b04d3

test_minSubArraySum()
print("All tests passed!")

# Generated at 2026-11-02 23:47:31.674072
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # nonce:5c50f8bc
    # Basic case: minimum comes from a single small element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # All negative numbers: minimum is the sum of the whole array
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    # All positive numbers: minimum is the smallest element
    assert module_0.minSubArraySum([1, 2, 3]) == 1
    assert module_0.minSubArraySum([10, 20, 30, 40]) == 10
    # Single element array
    assert module_0.minSubArraySum([0]) == 0
    assert module_0.minSubArraySum([5]) == 5
    assert module_0.minSubArraySum([-7]) == -7
    # Mixed positive and negative values
    assert module_0.minSubArraySum([5, -3, 5]) == -3
    assert module_0.minSubArraySum([3, -1, 2, -4, 3]) == -4
    assert module_0.minSubArraySum([1, -2, 3, -4, 5]) == -4
    # Minimum spans multiple elements
    assert module_0.minSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]) == -5
    # Contains zeros
    assert module_0.minSubArraySum([0, 0, 0]) == 0
    assert module_0.minSubArraySum([1, 0, -1, 0]) == -1
    # Negative then positive mix
    assert module_0.minSubArraySum([-5, 2, 3]) == -5
    assert module_0.minSubArraySum([2, -5, 3]) == -5
    print("All tests passed!")


if __name__ == "__main__":
    test_minSubArraySum()