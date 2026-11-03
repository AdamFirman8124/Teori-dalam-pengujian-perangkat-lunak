

# Generated at 2026-11-03 05:27:06.889653
# Unit test for function below_zero
def test_below_zero():
    # Test with empty list - balance never changes
    assert module_0.below_zero([]) == False

    # Test with all positive operations - never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Test with operations that go below zero
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Test with single negative operation
    assert module_0.below_zero([-1]) == True

    # Test with single positive operation
    assert module_0.below_zero([1]) == False

    # Test balance reaching exactly zero - not below zero
    assert module_0.below_zero([1, -1]) == False

    # Test balance going negative then positive - returns True at first drop
    assert module_0.below_zero([1, -2, 10, 20]) == True

    # Test large positive balance then large withdrawal
    assert module_0.below_zero([100, 200, -350]) == True

    # Test large positive balance with withdrawal not exceeding balance
    assert module_0.below_zero([100, 200, -300]) == False

    # Test alternating operations staying non-negative
    assert module_0.below_zero([5, -3, 2, -4, 1]) == True

    # Test zero operations included
    assert module_0.below_zero([0, 0, 0]) == False

    # Test negative result only at the very end
    assert module_0.below_zero([10, 10, 10, -31]) == True

# Generated at 2026-11-03 05:29:13.801783
# Unit test for function below_zero
def test_below_zero():
    # Test with operations that dip below zero
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([1, 2, -4, 5]) == True
    assert module_0.below_zero([1, -1, 2, -2]) == False
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([10, -20]) == True
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([5, -3, 2, -4]) == True
    assert module_0.below_zero([3, -3, -1]) == True
    assert module_0.below_zero([100]) == False


def test_below_zero_negative_start():
    # First operation immediately goes negative
    assert module_0.below_zero([-5]) == True
    assert module_0.below_zero([-1, 10]) == True


def test_below_zero_zero_boundary():
    # Balance reaching exactly zero is not below zero
    assert module_0.below_zero([5, -5]) == False
    assert module_0.below_zero([2, -2, -1]) == True


def test_below_zero_large_values():
    assert module_0.below_zero([10**9, -(10**9) - 1]) == True
    assert module_0.below_zero([10**9, -(10**9)]) == False


def test_below_zero_returns_bool():
    result = module_0.below_zero([1, -2])
    assert isinstance(result, bool)
    result = module_0.below_zero([1, 2])
    assert isinstance(result, bool)

# Generated at 2026-11-03 05:31:59.041261
# Unit test for function below_zero
def test_below_zero():
    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Balance goes below zero at some point
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Starts below zero immediately
    assert module_0.below_zero([-1]) == True

    # Empty list - balance stays at zero
    assert module_0.below_zero([]) == False

    # Balance touches exactly zero but not below
    assert module_0.below_zero([1, -1]) == False

    # Goes below zero then comes back up
    assert module_0.below_zero([5, -10, 20]) == True

    # Single positive operation
    assert module_0.below_zero([10]) == False

    # Reaches exactly negative after multiple steps
    assert module_0.below_zero([2, 2, 2, -7]) == True

# Generated at 2026-11-03 05:33:32.642502
# Unit test for function below_zero
def test_below_zero():
    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Balance goes below zero mid-sequence
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Empty operations list
    assert module_0.below_zero([]) == False

    # Balance drops below zero then recovers — still True
    assert module_0.below_zero([5, -10, 20]) == True

    # Balance hits exactly zero — not below zero
    assert module_0.below_zero([1, -1]) == False

    # Single negative operation
    assert module_0.below_zero([-1]) == True

    # Single positive operation
    assert module_0.below_zero([10]) == False

    # Balance goes negative immediately after starting positive
    assert module_0.below_zero([2, -3, 2]) == True

    # Large values
    assert module_0.below_zero([1000000, -2000000]) == True
    assert module_0.below_zero([1000000, -1000000, 5]) == False

# Generated at 2026-11-03 05:34:43.022224
# Unit test for function below_zero
def test_below_zero():
    # Test case where balance goes below zero
    assert module_0.below_zero([1, 2, -4, 5]) == True
    
    # Test case where balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False
    
    # Test case with empty list
    assert module_0.below_zero([]) == False
    
    # Test case with single negative operation
    assert module_0.below_zero([-1]) == True
    
    # Test case with single positive operation
    assert module_0.below_zero([1]) == False
    
    # Test case where balance drops to exactly zero (not below)
    assert module_0.below_zero([1, 2, -3]) == False
    
    # Test case where balance goes below zero only at the end
    assert module_0.below_zero([5, 3, -10]) == True
    
    # Test case with all negative operations
    assert module_0.below_zero([-1, -2, -3]) == True
    
    # Test case where balance dips below zero then recovers
    assert module_0.below_zero([10, -15, 20]) == True
    
    # Test case with large positive numbers keeping balance positive
    assert module_0.below_zero([100, -50, -49]) == False
    
    # Test case starting with zero operations
    assert module_0.below_zero([0, 0, 0]) == False
    
    # Test case where balance goes below zero midway through
    assert module_0.below_zero([3, 3, -7, 10, 10]) == True
    
    print("All tests passed!")


test_below_zero()