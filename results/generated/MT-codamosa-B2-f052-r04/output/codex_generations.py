

# Generated at 2026-11-02 15:04:09.287506
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3, 4], 5) == True
    # Element equal to threshold should return False
    assert module_0.below_threshold([1, 2, 5], 5) == False
    # Element above threshold should return False
    assert module_0.below_threshold([1, 6, 3], 5) == False
    # Empty list should return True (vacuously true)
    assert module_0.below_threshold([], 5) == True
    # Single element below threshold
    assert module_0.below_threshold([4], 5) == True
    # Single element equal to threshold
    assert module_0.below_threshold([5], 5) == False
    # Negative numbers below threshold
    assert module_0.below_threshold([-10, -5, 0], 1) == True
    # Negative threshold cases
    assert module_0.below_threshold([-10, -5], -3) == True
    assert module_0.below_threshold([-10, -2], -3) == False
    # First element already fails
    assert module_0.below_threshold([100, 1, 2], 5) == False
    # Last element fails
    assert module_0.below_threshold([1, 2, 100], 5) == False
    # Large numbers
    assert module_0.below_threshold([10**9], 10**9 + 1) == True
    print("All tests passed!")


if __name__ == "__main__":
    test_below_threshold()

# Generated at 2026-11-02 15:05:42.528471
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 10) == True
    assert module_0.below_threshold([1, 2, 9], 10) == True
    
    # An element equals the threshold -> False
    assert module_0.below_threshold([1, 10, 3], 10) == False
    
    # An element above the threshold -> False
    assert module_0.below_threshold([1, 2, 15], 10) == False
    
    # Empty list -> True (vacuously true)
    assert module_0.below_threshold([], 10) == True
    
    # Negative numbers
    assert module_0.below_threshold([-5, -1, 0], 1) == True
    assert module_0.below_threshold([-5, -1, 2], 1) == False
    
    # Threshold is 0
    assert module_0.below_threshold([-3, -1], 0) == True
    assert module_0.below_threshold([0, -1], 0) == False
    
    # Single element list
    assert module_0.below_threshold([5], 6) == True
    assert module_0.below_threshold([6], 6) == False
    
    # First element fails
    assert module_0.below_threshold([100, 1, 2], 10) == False
    
    # Last element fails
    assert module_0.below_threshold([1, 2, 100], 10) == False

# Generated at 2026-11-02 15:10:23.294436
# Unit test for function below_threshold
def test_below_threshold():assert module_0.below_threshold([1, 2, 4, 10], 100) == True

# Generated at 2026-11-02 15:12:09.273776
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 4) == True
    # Element equal to threshold (should be False, since e >= t)
    assert module_0.below_threshold([1, 2, 4], 4) == False
    # Element above threshold
    assert module_0.below_threshold([1, 5, 3], 4) == False
    # Empty list trivially satisfies condition
    assert module_0.below_threshold([], 10) == True
    # Negative numbers below threshold
    assert module_0.below_threshold([-5, -1, 0], 1) == True
    # Negative threshold
    assert module_0.below_threshold([-10, -3], -1) == True
    assert module_0.below_threshold([-10, 0], -1) == False
    # Single element cases
    assert module_0.below_threshold([9], 10) == True
    assert module_0.below_threshold([10], 10) == False
    # Large list all below
    assert module_0.below_threshold(list(range(100)), 100) == True
    assert module_0.below_threshold(list(range(100)), 99) == False
    # Floats in list against int threshold
    assert module_0.below_threshold([0.5, 1.5, 2.5], 3) == True
    assert module_0.below_threshold([0.5, 3.0, 2.5], 3) == False