

# Generated at 2026-11-02 05:54:19.469326
# Unit test for function below_zero
def test_below_zero():
    # Balance goes below zero
    assert module_0.below_zero([1, 2, -3]) == True
    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False
    # Empty operations list
    assert module_0.below_zero([]) == False
    # Single negative operation
    assert module_0.below_zero([-1]) == True
    # Goes below zero then recovers (should still be True)
    assert module_0.below_zero([1, -5, 10]) == True
    # Balance exactly at zero is not below zero
    assert module_0.below_zero([1, -1]) == False
    # Drops below zero at the very end
    assert module_0.below_zero([5, 5, -11]) == True
    # All zeros
    assert module_0.below_zero([0, 0, 0]) == False
    # Large numbers
    assert module_0.below_zero([1000000, -2000000]) == True
    # Starts at zero, stays non-negative
    assert module_0.below_zero([0, 1, -1, 1]) == False
# nonce:4ec34376

# Generated at 2026-11-02 05:54:40.768320
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([1, 2, -4, 5]) == True
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([10, -5, -6]) == True
    assert module_0.below_zero([10, -10, -1]) == True

# Generated at 2026-11-02 05:54:57.561980
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([1, 2, -4, 5]) == True
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([1, -1, 1, -1]) == False
    assert module_0.below_zero([0, -1]) == True
    assert module_0.below_zero([10, -5, -6]) == True
    assert module_0.below_zero([5, -5]) == False

# Generated at 2026-11-02 05:55:17.938808
# Unit test for function below_zero
def test_below_zero():
    # Empty list: no operations, balance never drops below zero
    assert module_0.below_zero([]) == False

    # All positive operations: balance stays non-negative
    assert module_0.below_zero([1, 2, 3]) == False

    # Balance goes below zero at the end
    assert module_0.below_zero([1, 2, -4]) == True

    # Balance reaches exactly zero but never below
    assert module_0.below_zero([1, 2, -3]) == False

    # Starts negative immediately
    assert module_0.below_zero([-1]) == True

    # Dips below zero in the middle, then recovers
    assert module_0.below_zero([5, -10, 20]) == True

    # Large positive then small negative: never below zero
    assert module_0.below_zero([100, -50, -50]) == False

    # Single zero operation
    assert module_0.below_zero([0]) == False

    # Balance goes negative on the very first operation
    assert module_0.below_zero([-5, 10]) == True

    # Alternating operations that stay at or above zero
    assert module_0.below_zero([10, -5, 5, -10, 1]) == True


if __name__ == "__main__":
    test_below_zero()
    print("All tests passed!")

# Generated at 2026-11-02 05:55:50.914170
# Unit test for function below_zero
def test_below_zero():
    # Goes below zero at some point
    assert module_0.below_zero([1, 2, -4, 5]) is True
    assert module_0.below_zero([-1]) is True

    # Never goes below zero
    assert module_0.below_zero([1, 2, 3]) is False
    assert module_0.below_zero([1, -1, 2, -2]) is False

    # Balance touches exactly zero but never below
    assert module_0.below_zero([1, -1]) is False
    assert module_0.below_zero([5, -5, 3]) is False

    # Empty list — balance never changes
    assert module_0.below_zero([]) is False

    # Starts negative immediately
    assert module_0.below_zero([-10]) is True

    # Drops below zero only later in the sequence
    assert module_0.below_zero([3, 3, -7, 10]) is True
    assert module_0.below_zero([3, 3, -6, 10]) is False

    # Repeated returns to zero
    assert module_0.below_zero([1, -1, 1, -1]) is False