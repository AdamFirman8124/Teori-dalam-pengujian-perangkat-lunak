

# Generated at 2026-11-02 20:39:18.492306
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Pair that sums to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert module_0.pairs_sum_to_zero([1]) == False
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([-3, 3]) == True
    assert module_0.pairs_sum_to_zero([0, 0]) == True
    assert module_0.pairs_sum_to_zero([0]) == False
    assert module_0.pairs_sum_to_zero([5, -5, 10, -10]) == True
    assert module_0.pairs_sum_to_zero([2, 2, -2]) == True
    assert module_0.pairs_sum_to_zero([1, 2, 3, -4]) == False
    print("All tests passed!")


if __name__ == "__main__":
    test_pairs_sum_to_zero()

# Generated at 2026-11-02 20:40:41.162024
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Test with empty list
    assert module_0.pairs_sum_to_zero([]) == False

    # Test with single element (no pair possible)
    assert module_0.pairs_sum_to_zero([1]) == False

    # Test with a pair that sums to zero
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([1, 2, 3, -3]) == True
    assert module_0.pairs_sum_to_zero([5, -5]) == True

    # Test with no pair summing to zero
    assert module_0.pairs_sum_to_zero([1, 2, 3, 4]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 5, 7]) == False

    # Test where same value appears but no zero-sum pair
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 9, 7]) == False

    # Test with zero (zero pairs with another zero)
    assert module_0.pairs_sum_to_zero([0]) == False
    assert module_0.pairs_sum_to_zero([0, 0]) == True

    # Test with negatives only, no matching positives
    assert module_0.pairs_sum_to_zero([-1, -2, -3]) == False

    # Test with mixed values and a zero-sum pair at the end
    assert module_0.pairs_sum_to_zero([10, 20, 30, -30]) == True

# Generated at 2026-11-02 20:41:57.462096
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Basic cases with no pair summing to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False

    # Cases where a pair sums to zero
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([-1, 1]) == True
    assert module_0.pairs_sum_to_zero([3, -3, 4, -4]) == True
    assert module_0.pairs_sum_to_zero([0, 1, -1]) == True

    # Zero handling: two zeros count as a pair, one zero does not
    assert module_0.pairs_sum_to_zero([0, 0]) == True
    assert module_0.pairs_sum_to_zero([0]) == False

    # Edge cases: empty list and single element
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([1]) == False

    # Larger values
    assert module_0.pairs_sum_to_zero([1000000, 999999, -1000000]) == True
    assert module_0.pairs_sum_to_zero([1000000, 999999, -999998]) == False

    # Duplicates that don't form a zero pair
    assert module_0.pairs_sum_to_zero([2, 2, 2, 2]) == False

    print("All tests passed!")


test_pairs_sum_to_zero()

# Generated at 2026-11-02 20:44:30.309232
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Test with pairs that sum to zero
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1, -1]) == True
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([5, -5, 10]) == True

    # Test with no pairs summing to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 6, 7]) == False

    # Test with single zero (cannot pair with itself)
    assert module_0.pairs_sum_to_zero([0]) == False
    assert module_0.pairs_sum_to_zero([1, 0]) == False

    # Test with two zeros (they sum to zero)
    assert module_0.pairs_sum_to_zero([0, 0]) == True

    # Test edge cases: empty list and single element
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([1]) == False
    assert module_0.pairs_sum_to_zero([-3]) == False

    # Test with negative numbers only
    assert module_0.pairs_sum_to_zero([-1, -2, -3]) == False

    # Test with mixed positive/negative numbers
    assert module_0.pairs_sum_to_zero([10, -10, 20, -20]) == True
    assert module_0.pairs_sum_to_zero([10, 20, -30, 40]) == False

    # Test with duplicates
    assert module_0.pairs_sum_to_zero([3, 3, -3]) == True
    assert module_0.pairs_sum_to_zero([3, 3, 3]) == False

    print("All tests passed!")


# Run the test
test_pairs_sum_to_zero()

# Generated at 2026-11-02 20:47:31.111170
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Test with empty list
    assert module_0.pairs_sum_to_zero([]) == False

    # Test with single element
    assert module_0.pairs_sum_to_zero([1]) == False

    # Test with pair that sums to zero
    assert module_0.pairs_sum_to_zero([1, -1]) == True

    # Test with pair not summing to zero
    assert module_0.pairs_sum_to_zero([1, 2]) == False

    # Test with multiple elements, pair exists later in list
    assert module_0.pairs_sum_to_zero([1, 3, 5, 7, -7]) == True

    # Test with multiple elements, no pair sums to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 7]) == False

    # Test with negative numbers only, no pair sums to zero
    assert module_0.pairs_sum_to_zero([-1, -3, -5]) == False

    # Test with negative numbers, pair sums to zero
    assert module_0.pairs_sum_to_zero([-2, -4, 4, -8]) == True

    # Test with zero - single zero cannot pair with itself
    assert module_0.pairs_sum_to_zero([0]) == False

    # Test with two zeros - they sum to zero
    assert module_0.pairs_sum_to_zero([0, 0]) == True

    # Test with zero and non-zero
    assert module_0.pairs_sum_to_zero([0, 5]) == False

    # Test with duplicate non-zero values (same value can't pair with itself)
    assert module_0.pairs_sum_to_zero([2, 2, 2]) == False

    # Test with mixed positive/negative, no zero-sum pair
    assert module_0.pairs_sum_to_zero([3, 5, -7, 11]) == False

    # Test with mixed positive/negative, zero-sum pair exists
    assert module_0.pairs_sum_to_zero([3, 5, -3, 11]) == True

    print("All tests passed!")


test_pairs_sum_to_zero()