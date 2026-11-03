

# Generated at 2026-11-02 10:11:25.191103
# Unit test for function unique_digits
def test_unique_digits():
# nonce:32336080
    # Test with mixed odd and even digit numbers
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    
    # Test with all even digit numbers (should return empty list)
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    
    # Test with empty list
    assert module_0.unique_digits([]) == []
    
    # Test with single digit numbers
    assert module_0.unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]
    
    # Test with all odd digit numbers
    assert module_0.unique_digits([135, 357, 579]) == [135, 357, 579]
    
    # Test result is sorted even when input is unsorted
    assert module_0.unique_digits([579, 135, 357]) == [135, 357, 579]
    
    # Test with duplicates
    assert module_0.unique_digits([11, 11, 22, 33]) == [11, 11, 33]
    
    # Test with multi-digit numbers containing zero or even digits
    assert module_0.unique_digits([101, 111, 202, 999]) == [111, 999]
    
    # Test with large numbers
    assert module_0.unique_digits([13579, 24680, 113355]) == [113355, 13579]
    
    print("All tests passed!")

if __name__ == "__main__":
    test_unique_digits()

# Generated at 2026-11-02 10:12:37.955512
# Unit test for function unique_digits
def test_unique_digits():
    # Basic case: mixed numbers, only all-odd-digit numbers kept, result sorted
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No elements with all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty input list
    assert module_0.unique_digits([]) == []

    # All even digits -> empty result
    assert module_0.unique_digits([2, 4, 6, 222]) == []

    # Single odd digits
    assert module_0.unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

    # Multi-digit odd numbers, verify sorting of unsorted input
    assert module_0.unique_digits([979, 135, 3, 11]) == [3, 11, 135, 979]

    # Zero contains an even digit -> excluded
    assert module_0.unique_digits([0]) == []

    # Numbers containing 0 as a digit are excluded
    assert module_0.unique_digits([101, 303, 13]) == [13]

    # Duplicates are preserved (function does not deduplicate)
    assert module_0.unique_digits([1, 1, 3, 3]) == [1, 1, 3, 3]

    # Sorting check with varied lengths
    assert module_0.unique_digits([333, 1, 57, 9]) == [1, 9, 57, 333]

    # Large numbers with all odd digits
    assert module_0.unique_digits([111111, 2468, 97531]) == [111111, 97531]

    # Negative numbers raise ValueError ('-' cannot be converted to int)
    try:
        module_0.unique_digits([-13])
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass


if __name__ == "__main__":
    test_unique_digits()
    print("All tests passed!")

# Generated at 2026-11-02 10:13:08.774537
# Unit test for function unique_digits
def test_unique_digits():
    # Test with a typical list containing mixed odd/even digits
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    
    # Test with all elements having only odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    
    # Test with single-digit numbers
    assert module_0.unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    
    # Test with even single-digit numbers (should be excluded)
    assert module_0.unique_digits([0, 2, 4, 6, 8]) == []
    
    # Test with an empty list
    assert module_0.unique_digits([]) == []
    
    # Test that results are sorted
    assert module_0.unique_digits([931, 7, 135, 15]) == [7, 15, 135, 931]
    
    # Test with duplicates
    assert module_0.unique_digits([11, 11, 13]) == [11, 11, 13]
    
    # Test with multi-digit numbers containing zero (even digit)
    assert module_0.unique_digits([101, 111, 909]) == [111]
    
    # Test with larger numbers
    assert module_0.unique_digits([13579, 24680, 11111, 97531]) == [11111, 13579, 97531]
    
    print("All tests passed!")


test_unique_digits()

# Generated at 2026-11-02 10:14:42.519012
# Unit test for function unique_digits
def test_unique_digits():
    # Basic case: mixed odd and even digit numbers
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # All numbers contain even digits except one
    assert module_0.unique_digits([152, 3231, 103, 555]) == [555]

    # Empty input list
    assert module_0.unique_digits([]) == []

    # No elements have all odd digits
    assert module_0.unique_digits([2, 4, 6, 20, 84]) == []

    # All elements have odd digits, already sorted
    assert module_0.unique_digits([11, 13, 15, 17]) == [11, 13, 15, 17]

    # Single element with odd digits
    assert module_0.unique_digits([1]) == [1]

    # Single element with an even digit
    assert module_0.unique_digits([12]) == []

    # Duplicates are preserved
    assert module_0.unique_digits([15, 15, 1]) == [1, 15, 15]

    # Result is sorted regardless of input order
    assert module_0.unique_digits([331, 15, 1]) == [1, 15, 331]

    # Multi-digit numbers with all odd digits
    assert module_0.unique_digits([135, 246, 579, 8, 97531]) == [135, 579, 97531]

    # Large numbers
    assert module_0.unique_digits([111111, 222222, 999999]) == [111111, 999999]

    # Unsorted input with mixed values
    assert module_0.unique_digits([999, 888, 777, 666]) == [777, 999]

# Generated at 2026-11-02 10:15:29.066191
# Unit test for function unique_digits
def test_unique_digits():
    # Basic mixed case: only elements with all odd digits are kept, sorted
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No elements with all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty input list
    assert module_0.unique_digits([]) == []

    # Single element with odd digits
    assert module_0.unique_digits([1]) == [1]

    # All elements have odd digits, verify sorted order
    assert module_0.unique_digits([111, 11, 1111]) == [11, 111, 1111]

    # All elements contain even digits
    assert module_0.unique_digits([2, 4, 6, 8]) == []

    # Multi-digit odd-digit numbers sorted ascending
    assert module_0.unique_digits([135, 79, 357, 9]) == [9, 79, 135, 357]

    # Already sorted input stays sorted
    assert module_0.unique_digits([13, 15, 17, 19]) == [13, 15, 17, 19]

    # Zero is an even digit, so excluded
    assert module_0.unique_digits([0, 2, 20]) == []

    # Repeated odd digits across multiple elements
    assert module_0.unique_digits([999, 111, 333]) == [111, 333, 999]

    # Large numbers with all odd digits
    assert module_0.unique_digits([13579, 97531, 11111]) == [11111, 13579, 97531]

    # Mixed single and multi-digit results
    assert module_0.unique_digits([3, 12, 35, 44, 57]) == [3, 35, 57]