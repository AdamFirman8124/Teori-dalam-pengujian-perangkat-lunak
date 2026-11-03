

# Generated at 2026-11-02 12:50:40.397591
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # No pair sums to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False

    # Pair sums to zero
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert module_0.pairs_sum_to_zero([1]) == False

    # Negative and positive pairs
    assert module_0.pairs_sum_to_zero([5, -5]) == True
    assert module_0.pairs_sum_to_zero([1, -1, 2, 3]) == True
    assert module_0.pairs_sum_to_zero([-3, 1, 2, 4]) == False

    # Zero cases
    assert module_0.pairs_sum_to_zero([0, 0]) == True
    assert module_0.pairs_sum_to_zero([0]) == False
    assert module_0.pairs_sum_to_zero([0, 1, 2]) == False

    # Empty list
    assert module_0.pairs_sum_to_zero([]) == False

    # Duplicates without a zero pair
    assert module_0.pairs_sum_to_zero([3, 3, 3]) == False

    # Larger mixed list
    assert module_0.pairs_sum_to_zero([10, -10, 20, -20, 30]) == True
    assert module_0.pairs_sum_to_zero([10, 20, 30, 40]) == False

# Generated at 2026-11-02 12:51:52.143727
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Basic test cases
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == False
    assert module_0.pairs_sum_to_zero([1]) == False

    # Cases where a valid pair exists
    assert module_0.pairs_sum_to_zero([-3, 9, -1, 4, 2, 31]) == True
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([5, 3, -5, 2]) == True

    # Edge cases: empty list and single element
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([0]) == False  # cannot pair an element with itself

    # Zero pairs
    assert module_0.pairs_sum_to_zero([0, 0]) == True  # two distinct zeros sum to zero
    assert module_0.pairs_sum_to_zero([1, 0]) == False

    # Duplicates that don't form a pair
    assert module_0.pairs_sum_to_zero([2, 2, 2]) == False
    assert module_0.pairs_sum_to_zero([-2, -2]) == False

    # Larger mixed list
    assert module_0.pairs_sum_to_zero([-10, 20, 30, -30, 5]) == True
    assert module_0.pairs_sum_to_zero([-10, 20, 31, -29, 5]) == False

    print("All tests passed!")


# Run the tests
test_pairs_sum_to_zero()

# Generated at 2026-11-02 12:52:59.586101
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # No pair sums to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False

    # Pair exists that sums to zero
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert module_0.pairs_sum_to_zero([1, -1, 2]) == True
    assert module_0.pairs_sum_to_zero([5, -5]) == True
    assert module_0.pairs_sum_to_zero([-3, 1, 2, 3]) == True

    # Edge cases: empty list, single element
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([1]) == False

    # Duplicated zero (distinct indices)
    assert module_0.pairs_sum_to_zero([0, 0]) == True

    # Float values
    assert module_0.pairs_sum_to_zero([1.5, -1.5]) == True
    assert module_0.pairs_sum_to_zero([1.5, 1.5]) == False

    # Negative only, no zero-sum pair
    assert module_0.pairs_sum_to_zero([-1, -2, -3]) == False

    print("All test_pairs_sum_to_zero tests passed!")


if __name__ == "__main__":
    test_pairs_sum_to_zero()

# Generated at 2026-11-02 12:54:10.189314
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Pair exists: 1 + (-1) == 0
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    # Pair exists among larger list
    assert module_0.pairs_sum_to_zero([2, 4, -2, 8]) == True
    # No pair sums to zero
    assert module_0.pairs_sum_to_zero([1, 2, 3, 4]) == False
    # Empty list
    assert module_0.pairs_sum_to_zero([]) == False
    # Single element cannot form a pair
    assert module_0.pairs_sum_to_zero([1]) == False
    # Single zero cannot pair with itself
    assert module_0.pairs_sum_to_zero([0]) == False
    # Two distinct zeros sum to zero
    assert module_0.pairs_sum_to_zero([0, 0]) == True
    # All negatives, no opposite pair
    assert module_0.pairs_sum_to_zero([-1, -2, -3]) == False
    # Large values
    assert module_0.pairs_sum_to_zero([1000000, -1000000]) == True
    # Pair not adjacent
    assert module_0.pairs_sum_to_zero([5, 3, 2, -5]) == True
    # Repeated value with no zero-sum pair
    assert module_0.pairs_sum_to_zero([3, 3, 3]) == False
    # Float pair
    assert module_0.pairs_sum_to_zero([1.5, -1.5]) == True
    # Mixed positives without opposites
    assert module_0.pairs_sum_to_zero([10, 20, 30]) == False

# Generated at 2026-11-02 12:55:19.075929
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Empty list - no pairs exist
    assert module_0.pairs_sum_to_zero([]) == False

    # Single element - no pair possible
    assert module_0.pairs_sum_to_zero([1]) == False
    assert module_0.pairs_sum_to_zero([0]) == False

    # Simple true case
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([2, 3, -3]) == True

    # Simple false case
    assert module_0.pairs_sum_to_zero([1, 2, 3]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 4]) == False

    # Two zeros form a pair summing to zero
    assert module_0.pairs_sum_to_zero([0, 0]) == True

    # Pair exists later in the list
    assert module_0.pairs_sum_to_zero([1, 5, 3, -5]) == True
    assert module_0.pairs_sum_to_zero([7, 8, 9, 10, -7]) == True

    # Negative numbers without opposite pair
    assert module_0.pairs_sum_to_zero([-1, -2, -3]) == False

    # Pair with zero in the middle
    assert module_0.pairs_sum_to_zero([5, 0, -5]) == True

    # Larger mixed list without a valid pair
    assert module_0.pairs_sum_to_zero([1, 2, 3, 4, 5, 6]) == False

    # Larger mixed list with a valid pair
    assert module_0.pairs_sum_to_zero([1, 2, 3, 4, 5, -4]) == True

    # Duplicates that do not sum to zero
    assert module_0.pairs_sum_to_zero([3, 3, 3]) == False

    # Order matters: pair in reversed positions
    assert module_0.pairs_sum_to_zero([-2, 10, 2]) == True


# nonce:70f16120