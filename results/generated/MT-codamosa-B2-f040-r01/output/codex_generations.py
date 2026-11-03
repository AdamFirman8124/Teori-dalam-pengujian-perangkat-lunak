

# Generated at 2026-11-03 03:47:26.173546
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # Triple exists that sums to zero
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([1, 2]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([0, 0, 1]) == False
    assert module_0.triples_sum_to_zero([-1, 0, 1]) == True
    assert module_0.triples_sum_to_zero([-1, -2, -3]) == False
    assert module_0.triples_sum_to_zero([5, -5, 10, -10, 0]) == True
    assert module_0.triples_sum_to_zero([3, -1, -2]) == True
    # Duplicate values used at distinct indices
    assert module_0.triples_sum_to_zero([2, 2, -4]) == True
    assert module_0.triples_sum_to_zero([2, 2, 2]) == False

# Generated at 2026-11-03 03:49:08.163573
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # Triple exists: 1 + (-2) + 1 = 0
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True

    # No triple sums to zero
    assert module_0.triples_sum_to_zero([1, 2, 3]) == False

    # Exactly three elements that sum to zero
    assert module_0.triples_sum_to_zero([1, 2, -3]) == True

    # Exactly three elements that don't sum to zero
    assert module_0.triples_sum_to_zero([1, 2, 3]) == False

    # Two elements only (no triple possible)
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # Empty list
    assert module_0.triples_sum_to_zero([]) == False

    # Single element
    assert module_0.triples_sum_to_zero([0]) == False

    # Three zeros
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True

    # Two zeros and a nonzero (0 + 0 + 5 != 0)
    assert module_0.triples_sum_to_zero([0, 0, 5]) == False

    # Negative and positive mix: -1 + 2 + (-1) = 0
    assert module_0.triples_sum_to_zero([-1, 2, -1]) == True

    # Larger list with triple: 5 + (-3) + (-2) = 0
    assert module_0.triples_sum_to_zero([5, 10, -3, -2, 7]) == True

    # Larger list with no triple
    assert module_0.triples_sum_to_zero([1, 1, 1, 1, 1]) == False

    # All negatives
    assert module_0.triples_sum_to_zero([-1, -2, -3]) == False

    # Mixed: 100 + (-50) + (-50) = 0
    assert module_0.triples_sum_to_zero([100, -50, -50, 20]) == True

    # Duplicates that don't form a zero triple
    assert module_0.triples_sum_to_zero([2, 2, 2]) == False

    # Zero triple with mixed values: 0 + 5 + (-5) = 0
    assert module_0.triples_sum_to_zero([0, 5, -5]) == True

# Generated at 2026-11-03 03:51:12.276836
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # Basic cases with triples that sum to zero
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False

    # Edge cases
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False  # fewer than 3 elements
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True  # three zeros
    assert module_0.triples_sum_to_zero([0, 0, 1]) == False
    assert module_0.triples_sum_to_zero([0, 0, 1, 0]) == True  # three zeros present

    # Negative and positive combinations
    assert module_0.triples_sum_to_zero([-1, -2, 3]) == True
    assert module_0.triples_sum_to_zero([-1, -2, -3]) == False
    assert module_0.triples_sum_to_zero([5, -5, 0]) == True
    assert module_0.triples_sum_to_zero([10, -10, 1, -1]) == True

    # Duplicates by position are allowed
    assert module_0.triples_sum_to_zero([1, 1, -2]) == True
    assert module_0.triples_sum_to_zero([2, 2, 2]) == False

    # Larger lists
    assert module_0.triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, -6]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False

    # Floats
    assert module_0.triples_sum_to_zero([1.5, -0.5, -1.0]) == True
    assert module_0.triples_sum_to_zero([0.1, 0.2, -0.3]) == False  # floating point precision

    print("All tests passed!")


test_triples_sum_to_zero()

# Generated at 2026-11-03 03:53:12.400721
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
# nonce:96a828a5
    # No triple sums to zero
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    # Triple exists: 1 + (-2) + 1 = 0
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    # Triple exists: 2 + (-5) + 3 = 0
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True

    # Fewer than three elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # All zeros
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    # Only two zeros — cannot form a triple
    assert module_0.triples_sum_to_zero([0, 0, 5]) == False

    # Negative triple
    assert module_0.triples_sum_to_zero([-1, -2, 3]) == True
    # Same value at different indices may be combined
    assert module_0.triples_sum_to_zero([5, 5, -10]) == True
    # Same value cannot be reused from a single element
    assert module_0.triples_sum_to_zero([5, -10]) == False
    assert module_0.triples_sum_to_zero([5, 5, 5]) == False

    # Works with floats
    assert module_0.triples_sum_to_zero([1.5, 2.5, -4.0]) == True
    assert module_0.triples_sum_to_zero([1.5, 2.5, -3.0]) == False

    # Larger list with a triple near the end
    assert module_0.triples_sum_to_zero([10, 20, 30, 40, -70]) == True
    # Larger list with no triple
    assert module_0.triples_sum_to_zero([10, 20, 30, 40, 50]) == False

# Generated at 2026-11-03 03:55:14.440258
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # Test case with a triple that sums to zero
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    
    # Test case with exactly three elements summing to zero
    assert module_0.triples_sum_to_zero([1, -1, 0]) == True
    assert module_0.triples_sum_to_zero([2, 4, -5]) == False
    
    # Test case with all zeros
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    
    # Test case with negative numbers
    assert module_0.triples_sum_to_zero([-1, -2, 3]) == True
    assert module_0.triples_sum_to_zero([-1, -2, -3]) == False
    
    # Test case with duplicates
    assert module_0.triples_sum_to_zero([2, 2, -4]) == True
    assert module_0.triples_sum_to_zero([2, 2, 2]) == False
    
    # Test case with fewer than three elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False
    
    # Test case with larger list
    assert module_0.triples_sum_to_zero([1, 2, 3, 4, 5, -6]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 4, 5, 6]) == False
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_triples_sum_to_zero()