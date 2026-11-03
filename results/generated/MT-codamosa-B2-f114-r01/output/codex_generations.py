

# Generated at 2026-11-02 16:31:45.752747
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # nonce:57c6c72c
    # All-positive array: min subarray is the single smallest element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([1, 2, 3]) == 1
    assert module_0.minSubArraySum([0, 10, 20, 1000000]) == 0
    assert module_0.minSubArraySum([5]) == 5

    # All-negative array: min subarray is the entire array
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-5]) == -5
    assert module_0.minSubArraySum([0, -10, -20]) == -30

    # Mixed positive/negative arrays
    assert module_0.minSubArraySum([-1, -2, -3, 4, 5, 6]) == -6
    assert module_0.minSubArraySum([100, -100, 100]) == -100
    assert module_0.minSubArraySum([3, -4, 1, 2, -1]) == -4
    assert module_0.minSubArraySum([1, -1]) == -1
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -6

# Generated at 2026-11-02 16:32:43.821458
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # nonce:9f81dd9e
    # All positive numbers: minimum subarray is the smallest single element
    assert module_0.minSubArraySum([2, 3, 4, 1, 5]) == 1
    assert module_0.minSubArraySum([1, 2, 3]) == 1
    assert module_0.minSubArraySum([5]) == 5

    # All negative numbers: minimum subarray is the entire array
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-5]) == -5

    # Mixed positive/negative values
    assert module_0.minSubArraySum([-2, 3, 4, 1, 5]) == -2
    assert module_0.minSubArraySum([1, -1, 1]) == -1
    assert module_0.minSubArraySum([3, -4, 2, -3, -1]) == -6
    assert module_0.minSubArraySum([2, -1, 2, -1, 2]) == -1

    # Arrays containing zeros
    assert module_0.minSubArraySum([0, 0, 0]) == 0
    assert module_0.minSubArraySum([2, 0, 3]) == 0
    assert module_0.minSubArraySum([0, -1, 2]) == -1

    # Float values
    assert module_0.minSubArraySum([1.5, -0.5]) == -0.5
    assert module_0.minSubArraySum([-1.5, 2.5]) == -1.5

    # Cross-check against brute force on additional arrays
    def brute(nums):
        return min(sum(nums[i:j])
                   for i in range(len(nums))
                   for j in range(i + 1, len(nums) + 1))

    for arr in ([4, -5, 2, 1, -1, 3],
                [-1, 2, -3, 4],
                [10, -3, 4, -2, -1, 8]):
        assert module_0.minSubArraySum(arr) == brute(arr), arr

    # Empty input raises ValueError
    try:
        module_0.minSubArraySum([])
        assert False, "Expected ValueError for empty input"
    except ValueError:
        pass

# Generated at 2026-11-02 16:33:48.800099
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # Test with mixed positive and negative numbers
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-1, -2, 4, 5]) == -3
    assert module_0.minSubArraySum([1, 2, 3, 4]) == 1
    assert module_0.minSubArraySum([5, -3, 5]) == -3
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -6

    # Test with single element
    assert module_0.minSubArraySum([7]) == 7
    assert module_0.minSubArraySum([-7]) == -7
    assert module_0.minSubArraySum([0]) == 0

    # Test with all zeros
    assert module_0.minSubArraySum([0, 0, 0]) == 0

    # Test with two elements
    assert module_0.minSubArraySum([-1, 1]) == -1
    assert module_0.minSubArraySum([1, -1]) == -1
    assert module_0.minSubArraySum([-5, -10]) == -15

    # Test where minimum is the whole array
    assert module_0.minSubArraySum([-3, -1, -2]) == -6

    # Test where minimum is a middle segment
    assert module_0.minSubArraySum([10, -20, 10]) == -20
    assert module_0.minSubArraySum([3, -7, 2, -4, 6]) == -7

    # Test large numbers
    assert module_0.minSubArraySum([1000000, -2000000, 1000000]) == -2000000

    print("All test cases passed!")


if __name__ == "__main__":
    test_minSubArraySum()

# Generated at 2026-11-02 16:35:09.467063
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # Test with all positive numbers - minimum is the smallest single element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    
    # Test with all negative numbers - minimum is the sum of all elements
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    
    # Test with mixed positive and negative numbers
    assert module_0.minSubArraySum([5, -3, 5]) == -3
    assert module_0.minSubArraySum([2, -5, 3, -1, 2]) == -5
    
    # Test with a single element
    assert module_0.minSubArraySum([-1]) == -1
    assert module_0.minSubArraySum([10]) == 10
    
    # Test with zeros and negatives
    assert module_0.minSubArraySum([0, -1, 2, -1, -5]) == -6
    
    # Test with a single negative element among positives
    assert module_0.minSubArraySum([1, 2, -10, 4]) == -10
    
    # Test subarray that includes multiple negatives
    assert module_0.minSubArraySum([1, -2, -3, 4]) == -5
    
    # Test with two negative elements
    assert module_0.minSubArraySum([-1, -1]) == -2

# Generated at 2026-11-02 16:36:34.533481
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # Single element arrays
    assert module_0.minSubArraySum([5]) == 5
    assert module_0.minSubArraySum([-5]) == -5
    assert module_0.minSubArraySum([0]) == 0

    # All positive elements - minimum subarray is the smallest single element
    assert module_0.minSubArraySum([2, 3, 4, 1, 5]) == 1
    assert module_0.minSubArraySum([10, 20, 30]) == 10

    # All negative elements - minimum subarray is the sum of all elements
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-5, -2, -3, -4]) == -14
    assert module_0.minSubArraySum([-1]) == -1

    # Mixed positive and negative elements
    assert module_0.minSubArraySum([1, -2, 3]) == -2
    assert module_0.minSubArraySum([3, -1, -4, 2, 5]) == -5
    assert module_0.minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5

    # Arrays containing zero
    assert module_0.minSubArraySum([0, 1, 2, 3]) == 0
    assert module_0.minSubArraySum([1, 0, -1]) == -1

    # Duplicate values
    assert module_0.minSubArraySum([2, 2, 2]) == 2

# nonce:8dfb8ae1