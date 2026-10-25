

# Generated at 2026-10-24 06:03:57.316517
# Unit test for function minSubArraySum

# Generated at 2026-10-24 06:03:58.663731
# Unit test for function minSubArraySum
def test_minSubArraySum():
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-1, -2, -3, 4]) == -6
    assert module_0.minSubArraySum([4, -1, -2, -3]) == -6
    assert module_0.minSubArraySum([5]) == 5
    assert module_0.minSubArraySum([-5]) == -5
    assert module_0.minSubArraySum([4, -2, -8, 5, -2, 7, 7, 2, -10, 1]) == -10
    assert module_0.minSubArraySum([1, -1, 1, -1]) == -1
    assert module_0.minSubArraySum([0, 0, 0]) == 0
    assert module_0.minSubArraySum([-10, 3, -1, -5, 2]) == -12

# Generated at 2026-10-24 06:04:00.084199
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # All positive numbers
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # Single element
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([5]) == 5
    # Mixed positive/negative
    assert module_0.minSubArraySum([1, -1, -2, 2]) == -3
    # All negative
    assert module_0.minSubArraySum([-1, -2, -3, -4]) == -10
    # Zeros mixed in
    assert module_0.minSubArraySum([0, 1, 0, -1, 0]) == -1
    # Single negative among positives
    assert module_0.minSubArraySum([10, 20, -5, 30]) == -5
    # Empty check: min subarray sum of all-negatives with negatives at edges
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5
    print("All tests passed!")

# Generated at 2026-10-24 06:04:01.405796
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # All positive numbers
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # Single element
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([5]) == 5
    # Mixed positive/negative
    assert module_0.minSubArraySum([1, -1, -2, 2]) == -3
    # All negative
    assert module_0.minSubArraySum([-1, -2, -3, -4]) == -10
    # Zeros mixed in
    assert module_0.minSubArraySum([0, 1, 0, -1, 0]) == -1
    # Single negative among positives
    assert module_0.minSubArraySum([10, 20, -5, 30]) == -5
    # Empty check: min subarray sum of all-negatives with negatives at edges
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5
    print("All tests passed!")

# Generated at 2026-10-24 06:04:02.794182
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # All positive numbers
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # Single element
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([5]) == 5
    # Mixed positive/negative
    assert module_0.minSubArraySum([1, -1, -2, 2]) == -3
    # All negative
    assert module_0.minSubArraySum([-1, -2, -3, -4]) == -10
    # Zeros mixed in
    assert module_0.minSubArraySum([0, 1, 0, -1, 0]) == -1
    # Single negative among positives
    assert module_0.minSubArraySum([10, 20, -5, 30]) == -5
    # Empty check: min subarray sum of all-negatives with negatives at edges
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5
    print("All tests passed!")

# Generated at 2026-10-24 06:04:04.129906
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # All positive numbers
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # Single element
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([5]) == 5
    # Mixed positive/negative
    assert module_0.minSubArraySum([1, -1, -2, 2]) == -3
    # All negative
    assert module_0.minSubArraySum([-1, -2, -3, -4]) == -10
    # Zeros mixed in
    assert module_0.minSubArraySum([0, 1, 0, -1, 0]) == -1
    # Single negative among positives
    assert module_0.minSubArraySum([10, 20, -5, 30]) == -5
    # Empty check: min subarray sum of all-negatives with negatives at edges
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5
    print("All tests passed!")