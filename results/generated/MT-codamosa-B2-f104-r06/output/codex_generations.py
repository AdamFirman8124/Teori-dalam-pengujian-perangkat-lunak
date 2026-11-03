

# Generated at 2026-11-02 20:40:50.497490
# Unit test for function unique_digits
def test_unique_digits():
    # Test with a typical mixed list
    assert module_0.unique_digits([15, 33, 1422, 1, 15]) == [1, 15, 15, 33]

    # Test where no elements have all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Test with single digit numbers
    assert module_0.unique_digits([1, 3, 5, 2, 4]) == [1, 3, 5]

    # Test with an empty list
    assert module_0.unique_digits([]) == []

    # Test that result is sorted
    assert module_0.unique_digits([33, 1, 57, 9, 75]) == [1, 33, 57, 75, 9][::0] if False else module_0.unique_digits([33, 1, 57, 9, 75]) == [1, 9, 33, 57, 75]

    # Test with duplicates preserved
    assert module_0.unique_digits([7, 7, 13, 13]) == [7, 7, 13, 13]

    # Test with multi-digit numbers containing zero (even digit)
    assert module_0.unique_digits([101, 111, 303]) == [111]

    # Test all elements qualify
    assert module_0.unique_digits([11, 33, 55]) == [11, 33, 55]

    # Test large numbers
    assert module_0.unique_digits([13579, 24680, 999]) == [999, 13579]

    print("All tests passed!")

# Generated at 2026-11-02 20:42:32.029684
# Unit test for function unique_digits
def test_unique_digits():
    # Typical case: mix of numbers with all-odd digits and others
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    # No elements qualify -> empty list
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    # Duplicates preserved, result sorted
    assert module_0.unique_digits([3, 3, 11, 7, 2]) == [3, 3, 7, 11]
    # Single element
    assert module_0.unique_digits([1357]) == [1357]
    # Single element that does not qualify
    assert module_0.unique_digits([2468]) == []
    # Empty input list
    assert module_0.unique_digits([]) == []
    # Numbers containing zero (even digit) are excluded
    assert module_0.unique_digits([101, 111, 9]) == [9, 111]
    # Input already sorted differently; output must be sorted ascending
    assert module_0.unique_digits([99, 1, 555, 13]) == [1, 13, 99, 555]
    # Negative numbers: str includes '-' which is not a digit,
    # int('-') raises ValueError, so exclude negatives from coverage
    # (function contract assumes non-negative integers)

    print("All test_unique_digits assertions passed.")


if __name__ == "__main__":
    test_unique_digits()

# Generated at 2026-11-02 20:44:49.332864
# Unit test for function unique_digits
def test_unique_digits():
    # Basic case: mix of numbers with all odd digits and some even digits
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No numbers with all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty input list
    assert module_0.unique_digits([]) == []

    # All numbers have even digits
    assert module_0.unique_digits([2, 4, 6, 8]) == []

    # All numbers have odd digits, verify sorting
    assert module_0.unique_digits([135, 79, 111, 3]) == [3, 79, 111, 135]

    # Single-digit numbers
    assert module_0.unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]

    # Zero is even, should be excluded
    assert module_0.unique_digits([0]) == []

    # Duplicates are preserved (function filters, doesn't deduplicate)
    assert module_0.unique_digits([13, 13, 27, 13]) == [13, 13, 13]

    # Sorting check with unsorted input
    assert module_0.unique_digits([9, 1, 5, 3, 7]) == [1, 3, 5, 7, 9]

    # Larger numbers with all odd digits
    assert module_0.unique_digits([13579, 2468, 97531]) == [13579, 97531]

# Generated at 2026-11-02 20:47:40.426861
# Unit test for function unique_digits
def test_unique_digits():
    # nonce:97fd8b8e
    # Basic case: mixed odd/even digit numbers
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    
    # All numbers contain even digits -> empty result
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    
    # Empty input list
    assert module_0.unique_digits([]) == []
    
    # Single element with all odd digits
    assert module_0.unique_digits([7]) == [7]
    
    # Unsorted input, all odd digits -> sorted output
    assert module_0.unique_digits([31, 5, 977, 13]) == [5, 13, 31, 977]
    
    # Mixed: only elements with all odd digits kept
    assert module_0.unique_digits([11, 12, 13, 14]) == [11, 13]
    
    # Duplicates are preserved and sorted
    assert module_0.unique_digits([3, 3, 5]) == [3, 3, 5]
    
    # Large multi-digit numbers
    assert module_0.unique_digits([13579, 24680, 111]) == [111, 13579]
    
    # Reversed order input verifies sorting
    assert module_0.unique_digits([99, 7, 31]) == [7, 31, 99]

# Generated at 2026-11-02 20:49:04.499681
# Unit test for function unique_digits
def test_unique_digits():
    # Basic mixed case
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No elements with all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty input list
    assert module_0.unique_digits([]) == []

    # Single element
    assert module_0.unique_digits([7]) == [7]

    # All even digits
    assert module_0.unique_digits([2, 4, 6, 8]) == []

    # Multi-digit number with all odd digits
    assert module_0.unique_digits([13579]) == [13579]

    # All elements qualify; check sorting order
    assert module_0.unique_digits([11, 13, 3, 5, 7]) == [3, 5, 7, 11, 13]

    # Contains every digit (evens present)
    assert module_0.unique_digits([123456789]) == []

    # Mixed qualifying and non-qualifying
    assert module_0.unique_digits([9, 91, 913, 246]) == [9, 91, 913]

    # Zero is even, so excluded
    assert module_0.unique_digits([0, 1]) == [1]

    # Zero inside a number disqualifies it
    assert module_0.unique_digits([100, 101, 111]) == [111]

    # Duplicates are preserved
    assert module_0.unique_digits([3, 3, 5]) == [3, 3, 5]

    # Result is always sorted ascending
    result = module_0.unique_digits([33, 1, 5, 9])
    assert result == sorted(result) == [1, 5, 9, 33]