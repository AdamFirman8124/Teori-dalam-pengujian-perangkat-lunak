

# Generated at 2026-11-02 19:35:14.808069
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3, 4], 5) == True
    
    # One element equal to threshold (should be False)
    assert module_0.below_threshold([1, 2, 5, 3], 5) == False
    
    # One element above threshold
    assert module_0.below_threshold([1, 2, 6, 3], 5) == False
    
    # All elements above threshold
    assert module_0.below_threshold([6, 7, 8], 5) == False
    
    # Empty list - vacuously true
    assert module_0.below_threshold([], 5) == True
    
    # Single element below threshold
    assert module_0.below_threshold([4], 5) == True
    
    # Single element equal to threshold
    assert module_0.below_threshold([5], 5) == False
    
    # Negative numbers
    assert module_0.below_threshold([-3, -2, -1], 0) == True
    assert module_0.below_threshold([-3, 0, -1], 0) == False
    
    # Threshold is negative
    assert module_0.below_threshold([-10, -5], -4) == True
    assert module_0.below_threshold([-10, -3], -4) == False
    
    # Large numbers
    assert module_0.below_threshold([10**9, 10**9 - 1], 10**9) == True
    assert module_0.below_threshold([10**9], 10**9) == False
    
    print("All test_below_threshold tests passed!")


if __name__ == "__main__":
    test_below_threshold()

# Generated at 2026-11-02 19:36:59.623924
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 10) == True
    # Element equal to threshold (not below)
    assert module_0.below_threshold([1, 2, 10], 10) == False
    # Element above threshold
    assert module_0.below_threshold([1, 2, 11, 4], 10) == False
    # Empty list (vacuously true)
    assert module_0.below_threshold([], 5) == True
    # Single element below
    assert module_0.below_threshold([4], 5) == True
    # Single element equal
    assert module_0.below_threshold([5], 5) == False
    # Negative thresholds and values
    assert module_0.below_threshold([-10, -5, -1], 0) == True
    assert module_0.below_threshold([-10, 0, -1], 0) == False
    assert module_0.below_threshold([-10, -5], -3) == True
    # First element already exceeds threshold
    assert module_0.below_threshold([100, 1, 2], 10) == False
    # Last element exceeds threshold
    assert module_0.below_threshold([1, 2, 3, 100], 10) == False
    # All elements just below threshold
    assert module_0.below_threshold([8, 9], 10) == True

# Generated at 2026-11-02 19:38:28.206241
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 4, 10], 100) == True
    # Element equal to threshold should fail
    assert module_0.below_threshold([1, 20, 4, 10], 20) == False
    # Single element above threshold
    assert module_0.below_threshold([1, 2, 4, 10], 5) == False
    # Empty list returns True
    assert module_0.below_threshold([], 0) == True
    # Single element below threshold
    assert module_0.below_threshold([3], 5) == True
    # Single element equal to threshold
    assert module_0.below_threshold([5], 5) == False
    # Negative numbers and negative threshold
    assert module_0.below_threshold([-10, -5, -1], 0) == True
    assert module_0.below_threshold([-10, -5, -1], -5) == False
    # All elements equal to threshold
    assert module_0.below_threshold([2, 2, 2], 2) == False
    # Duplicated values below threshold
    assert module_0.below_threshold([7, 7, 7], 8) == True

# Generated at 2026-11-02 19:40:02.005010
# Unit test for function below_threshold
def test_below_threshold():
# nonce:69e5d1e7
    # All elements strictly below threshold
    assert module_0.below_threshold([1, 2, 3], 4) == True
    assert module_0.below_threshold([1, 2, 3], 10) == True
    assert module_0.below_threshold([0, -1, -2], 1) == True

    # Element equal to threshold (boundary: >= triggers False)
    assert module_0.below_threshold([1, 2, 4], 4) == False
    assert module_0.below_threshold([4], 4) == False

    # Element above threshold
    assert module_0.below_threshold([1, 5, 3], 4) == False
    assert module_0.below_threshold([10, 2, 3], 5) == False

    # Failing element at various positions
    assert module_0.below_threshold([100, 1, 2], 50) == False  # first
    assert module_0.below_threshold([1, 100, 2], 50) == False  # middle
    assert module_0.below_threshold([1, 2, 100], 50) == False  # last

    # Empty list is vacuously True
    assert module_0.below_threshold([], 0) == True
    assert module_0.below_threshold([], -100) == True

    # Single element list
    assert module_0.below_threshold([5], 10) == True
    assert module_0.below_threshold([5], 5) == False
    assert module_0.below_threshold([5], 4) == False

    # Negative numbers and negative threshold
    assert module_0.below_threshold([-10, -5, -1], 0) == True
    assert module_0.below_threshold([-10, 0, -1], 0) == False
    assert module_0.below_threshold([-5], -3) == True
    assert module_0.below_threshold([-5], -5) == False
    assert module_0.below_threshold([-10, -6], -5) == True

    print("All test_below_threshold tests passed!")


if __name__ == "__main__":
    test_below_threshold()

# Generated at 2026-11-02 19:42:02.467226
# Unit test for function below_threshold
def test_below_threshold():
    # nonce:8c9e6b2f
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 5) == True
    # Element equal to threshold should return False (>= check)
    assert module_0.below_threshold([1, 2, 5], 5) == False
    # Element above threshold
    assert module_0.below_threshold([1, 6, 3], 5) == False
    # Empty list vacuously true
    assert module_0.below_threshold([], 5) == True
    # Single element below
    assert module_0.below_threshold([4], 5) == True
    # Single element equal
    assert module_0.below_threshold([5], 5) == False
    # Negative numbers below positive threshold
    assert module_0.below_threshold([-10, -5, 0], 1) == True
    # Negative threshold
    assert module_0.below_threshold([-10, -5], -1) == True
    assert module_0.below_threshold([-10, 0], -1) == False
    # All elements equal to threshold
    assert module_0.below_threshold([3, 3, 3], 3) == False
    # Large list all below
    assert module_0.below_threshold(list(range(100)), 100) == True
    # Large list with one violation at the end
    assert module_0.below_threshold(list(range(99)) + [100], 100) == False
    # First element violates
    assert module_0.below_threshold([10, 1, 2], 5) == False
    # Zero threshold
    assert module_0.below_threshold([-1, -2], 0) == True
    assert module_0.below_threshold([0], 0) == False