

# Generated at 2026-11-02 09:03:59.588652
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # nonce:426a7207
    # Basic positive array: minimum is the smallest single element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    # All negative: minimum is the sum of the whole array
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    # All positive strictly increasing
    assert module_0.minSubArraySum([1, 2, 3]) == 1
    # Single element cases
    assert module_0.minSubArraySum([5]) == 5
    assert module_0.minSubArraySum([-5]) == -5
    # All zeros
    assert module_0.minSubArraySum([0, 0, 0]) == 0
    # Mixed values: min subarray is [-4, 2, -3, -1] = -6
    assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6
    # Mixed values: min subarray is [-3] or [-1, -2] = -3
    assert module_0.minSubArraySum([2, -3, 4, -1, -2, 1, 5, -3]) == -3
    # Negative in middle
    assert module_0.minSubArraySum([10, -3, 4]) == -3
    # Classic mixed case: min is [-5] = -5
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5
    # Whole array is the minimum subarray
    assert module_0.minSubArraySum([-2, -3, 4]) == -5
    # Pair with canceling values
    assert module_0.minSubArraySum([1, -1]) == -1

# Generated at 2026-11-02 09:04:32.170385
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # Mixed positive numbers: minimum subarray is the smallest single element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1

    # All negative numbers: min sum is the whole array
    assert module_0.minSubArraySum([-1, -2, -3]) == -6

    # Negative prefix is the minimum
    assert module_0.minSubArraySum([-1, -2, -3, 4]) == -6

    # All positive numbers: min subarray is the smallest element
    assert module_0.minSubArraySum([1, 2, 3]) == 1

    # Single element arrays
    assert module_0.minSubArraySum([10]) == 10
    assert module_0.minSubArraySum([-5]) == -5
    assert module_0.minSubArraySum([0]) == 0

    # Negative element between positives
    assert module_0.minSubArraySum([1, -2, 3]) == -2

    # Contains zeros
    assert module_0.minSubArraySum([0, 1, 2]) == 0

    # Multiple negative segments
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -6

    # Array with a large negative subarray in the middle
    assert module_0.minSubArraySum([5, -10, 5]) == -10

    # Alternating signs
    assert module_0.minSubArraySum([-1, 2, -3, 4, -5]) == -5

    # Two elements
    assert module_0.minSubArraySum([-1, 3]) == -1
    assert module_0.minSubArraySum([3, -1]) == -1

# Generated at 2026-11-02 09:05:04.840264
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # Typical positive-only arrays: min subarray is the smallest single element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([1, 2, 3]) == 1
    assert module_0.minSubArraySum([10]) == 10

    # All-negative arrays: min subarray is the whole array sum
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-3, -1, -4]) == -8

    # Mixed positive/negative arrays
    assert module_0.minSubArraySum([-1, -2, -3, 4]) == -6
    assert module_0.minSubArraySum([1, -1]) == -1
    assert module_0.minSubArraySum([4, -1, -2, 1, 2, -5, 3]) == -5
    assert module_0.minSubArraySum([2, -5, 3, -1, 4]) == -5
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5

    # Single element edge cases
    assert module_0.minSubArraySum([0]) == 0
    assert module_0.minSubArraySum([-7]) == -7
    assert module_0.minSubArraySum([5, -2]) == -2

# nonce:c9543b92

# Generated at 2026-11-02 09:06:08.006248
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # All positive numbers: minimum subarray is the smallest single element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    
    # All negative numbers: minimum subarray is the entire array
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    
    # Negative prefix dominates over positive tail
    assert module_0.minSubArraySum([-1, -2, -3, 4]) == -6
    
    # Mixed: single negative among positives
    assert module_0.minSubArraySum([1, -1]) == -1
    
    # Single positive element
    assert module_0.minSubArraySum([1]) == 1
    
    # Single negative element
    assert module_0.minSubArraySum([-5]) == -5
    
    # Mixed array with multiple negative runs
    assert module_0.minSubArraySum([2, -3, 4, -1, -2, 5]) == -3
    
    # All zeros
    assert module_0.minSubArraySum([0, 0, 0]) == 0
    
    # Negatives separated by a zero
    assert module_0.minSubArraySum([-2, 0, -3]) == -5
    
    # Negative run interrupted by a small positive
    assert module_0.minSubArraySum([-4, 1, -5]) == -5
    
    print("All test cases passed!")


test_minSubArraySum()

# Generated at 2026-11-02 09:07:16.300867
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # Typical mixed arrays
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([100, 1, 1, 1]) == 1
    assert module_0.minSubArraySum([3, -4, 1, 2, -1, 5]) == -4
    assert module_0.minSubArraySum([1, 2, -3, 4]) == -3
    assert module_0.minSubArraySum([1, -2, 3, -4, 5]) == -3

    # Arrays containing negatives -> minimum subarray may span negatives
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-1, -2, -3, 1]) == -6
    assert module_0.minSubArraySum([-1, -2, 1]) == -3
    assert module_0.minSubArraySum([-5]) == -5

    # All non-negative -> minimum is the smallest single element
    assert module_0.minSubArraySum([1, 2, 3]) == 1
    assert module_0.minSubArraySum([2, 2, 2, 2]) == 2
    assert module_0.minSubArraySum([0, 1, 2, 3]) == 0
    assert module_0.minSubArraySum([0, 0, 0]) == 0

    # Single element and mixed with zero
    assert module_0.minSubArraySum([1]) == 1
    assert module_0.minSubArraySum([1, -1]) == -1


if __name__ == "__main__":
    test_minSubArraySum()
    print("All tests passed.")