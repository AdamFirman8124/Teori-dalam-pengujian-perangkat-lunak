

# Generated at 2026-11-02 23:00:02.604568
# Unit test for function below_zero
def test_below_zero():
    # Test with empty list - balance never changes, stays at 0
    assert module_0.below_zero([]) == False

    # Test with all positive operations - never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Test with a single positive operation
    assert module_0.below_zero([5]) == False

    # Test with a single negative operation - immediately below zero
    assert module_0.below_zero([-1]) == True

    # Test where balance reaches exactly zero - should NOT return True
    assert module_0.below_zero([1, 2, -3]) == False

    # Test where balance goes to exactly zero and back up
    assert module_0.below_zero([10, -5, -5, 3]) == False

    # Test where balance goes below zero after positive operations
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Test where balance goes below zero at the very end
    assert module_0.below_zero([10, 20, 30, -61]) == True

    # Test where balance goes below zero in the middle and recovers
    assert module_0.below_zero([5, 5, -20, 15]) == True

    # Test starting with a negative operation
    assert module_0.below_zero([-5, 10, 20]) == True

    # Test with zero-valued operations only
    assert module_0.below_zero([0, 0, 0]) == False

    # Test with large numbers
    assert module_0.below_zero([1000000, -2000000]) == True
    assert module_0.below_zero([1000000, -500000]) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-02 23:02:46.708676
# Unit test for function below_zero
def test_below_zero():
    """Test cases for below_zero function."""

    # Balance goes below zero at some point
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Balance drops exactly to zero (not below)
    assert module_0.below_zero([1, 2, -3]) == False

    # Balance goes below zero on the first operation
    assert module_0.below_zero([-1]) == True

    # Empty list — no operations, never below zero
    assert module_0.below_zero([]) == False

    # Balance ends at exactly zero after dipping
    assert module_0.below_zero([5, -10, 5]) == True

    # Large positive start, never negative
    assert module_0.below_zero([100, -50, -50]) == False

    # Repeated dips below zero
    assert module_0.below_zero([1, -2, 3, -4]) == True

    # All zeros — never below zero
    assert module_0.below_zero([0, 0, 0]) == False

    # Negative result only at the very last step
    assert module_0.below_zero([1, 1, 1, -5]) == True

    # Single positive operation
    assert module_0.below_zero([10]) == False

    # Large numbers
    assert module_0.below_zero([1000000, -2000000]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-02 23:04:51.857269
# Unit test for function below_zero
def test_below_zero():
    # Test case: balance goes below zero
    assert module_0.below_zero([1, 2, -3]) == True

    # Test case: balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Test case: empty list, balance stays at zero
    assert module_0.below_zero([]) == False

    # Test case: single negative operation drops below zero immediately
    assert module_0.below_zero([-1]) == True

    # Test case: balance drops below zero then recovers
    assert module_0.below_zero([1, -5, 10]) == True

    # Test case: balance goes exactly to zero, not below
    assert module_0.below_zero([1, -1]) == False

    # Test case: balance goes exactly to zero, then negative
    assert module_0.below_zero([1, -1, -1]) == True

    # Test case: large positive numbers keeping balance above zero
    assert module_0.below_zero([1000000, -999999, -1]) == False

    # Test case: negative result only at the very end
    assert module_0.below_zero([5, 5, -11]) == True

    # Test case: all zeros, never below zero
    assert module_0.below_zero([0, 0, 0]) == False

# Generated at 2026-11-02 23:06:56.283088
# Unit test for function below_zero
def test_below_zero():
    # Test with empty list - balance never changes
    assert module_0.below_zero([]) is False

    # Test with all positive operations - never goes below zero
    assert module_0.below_zero([1, 2, 3]) is False

    # Test with a single negative operation
    assert module_0.below_zero([-1]) is True

    # Test with operations that dip below zero
    assert module_0.below_zero([1, 2, -4, 5]) is True

    # Test with operations that reach exactly zero but not below
    assert module_0.below_zero([1, 2, -3]) is False

    # Test with operations that end positive but dip below zero midway
    assert module_0.below_zero([5, -10, 10]) is True

    # Test with operations that stay exactly at zero boundary
    assert module_0.below_zero([1, -1, 1, -1]) is False

    # Test with large values
    assert module_0.below_zero([1000000, -2000000]) is True
    assert module_0.below_zero([1000000, -1000000]) is False

    # Test with first operation negative
    assert module_0.below_zero([-5, 10]) is True

    # Test with zero operations only
    assert module_0.below_zero([0, 0, 0]) is False


test_below_zero()
print("All tests passed!")