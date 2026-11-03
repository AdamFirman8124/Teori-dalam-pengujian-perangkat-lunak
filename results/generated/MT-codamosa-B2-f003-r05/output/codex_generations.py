

# Generated at 2026-11-01 20:11:20.410631
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([1, 2, -4, 5]) == True
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([0]) == False
    assert module_0.below_zero([5, -10, 20]) == True
    assert module_0.below_zero([10, -5, 3, -8]) == False

# Generated at 2026-11-01 20:11:37.730968
# Unit test for function below_zero
def test_below_zero():
    # Empty list: balance never goes below zero
    assert module_0.below_zero([]) == False

    # Single positive operation
    assert module_0.below_zero([1]) == False

    # Single negative operation drops balance below zero
    assert module_0.below_zero([-1]) == True

    # Balance stays non-negative throughout
    assert module_0.below_zero([1, 2, 3]) == False

    # Balance drops below zero after starting positive
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Balance touches zero but never goes below
    assert module_0.below_zero([1, -1, 1, -1]) == False

    # Balance drops below zero on the last operation
    assert module_0.below_zero([5, -6]) == True

    # Large positive then large negative
    assert module_0.below_zero([100, -101]) == True

    # Multiple ups and downs, never below zero
    assert module_0.below_zero([10, -5, 3, -8, 2]) == False

    # Multiple ups and downs, goes below zero midway
    assert module_0.below_zero([10, -5, 3, -9, 20]) == True

    # Zero operations do not affect balance
    assert module_0.below_zero([0, 0, 0]) == False

    # Exactly zero balance then negative
    assert module_0.below_zero([0, -1]) == True

    # Negative first, then recovery (should still return True)
    assert module_0.below_zero([-2, 5]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-01 20:11:56.048095
# Unit test for function below_zero
def test_below_zero():
    # Balance goes below zero
    assert module_0.below_zero([1, 2, -4, 5]) == True
    
    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False
    
    # Empty list, no operations performed
    assert module_0.below_zero([]) == False
    
    # Single negative operation drops balance immediately
    assert module_0.below_zero([-1]) == True
    
    # Balance hits exactly zero, which is not below zero
    assert module_0.below_zero([1, -1]) == False
    
    # Starts negative right away then recovers
    assert module_0.below_zero([5, -10, 20]) == True
    
    # All positive operations
    assert module_0.below_zero([10, 20, 30]) == False
    
    # Drops below zero only at the very end
    assert module_0.below_zero([100, -101]) == True
    
    # Zero as an operation does not affect outcome
    assert module_0.below_zero([0, 0, 0]) == False

# Generated at 2026-11-01 20:12:29.740481
# Unit test for function below_zero
def test_below_zero():
    # Empty list: no operations, balance stays at zero
    assert module_0.below_zero([]) == False

    # All positive operations: balance never drops below zero
    assert module_0.below_zero([1, 2, 3, 4]) == False

    # Balance drops below zero after some deposits/withdrawals
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Balance hits exactly zero but never goes below
    assert module_0.below_zero([1, 2, -3]) == False

    # Single negative operation immediately goes below zero
    assert module_0.below_zero([-1]) == True

    # Single positive operation stays above zero
    assert module_0.below_zero([1]) == False

    # Large deposit followed by larger withdrawal dips below zero
    assert module_0.below_zero([100, -150]) == True

    # Dips below zero mid-sequence even though it recovers later
    assert module_0.below_zero([10, -20, 50, -30]) == True

    # Reaches zero multiple times without going negative
    assert module_0.below_zero([5, -5, 5, -5]) == False

    print("All below_zero tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-01 20:13:08.547250
# Unit test for function below_zero
def test_below_zero():
    # Balance never drops below zero
    assert module_0.below_zero([1, 2, 3]) is False
    # Balance drops below zero mid-sequence
    assert module_0.below_zero([1, 2, -4, 5]) is True
    # Empty list: no operations, never below zero
    assert module_0.below_zero([]) is False
    # Balance hits exactly zero: not below
    assert module_0.below_zero([1, -1]) is False
    # First operation immediately makes balance negative
    assert module_0.below_zero([-1]) is True
    # Late large withdrawal causes negative balance
    assert module_0.below_zero([10, 20, -35]) is True
    # Withdrawal brings balance to zero, then recovers
    assert module_0.below_zero([5, -5, 3]) is False
    # Multiple dips below zero across the sequence
    assert module_0.below_zero([2, -5, 10, -12]) is True