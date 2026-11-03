

# Generated at 2026-11-03 01:03:44.388425
# Unit test for function unique_digits
def test_unique_digits():
    # Basic mixed case with odd and even digit numbers
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # Empty list input
    assert module_0.unique_digits([]) == []

    # All elements consist of odd digits only
    assert module_0.unique_digits([11, 13, 15, 17]) == [11, 13, 15, 17]

    # No elements consist of odd digits only
    assert module_0.unique_digits([2, 4, 6, 8]) == []

    # Single digit odd numbers
    assert module_0.unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

    # Single digit even numbers (including zero)
    assert module_0.unique_digits([0, 2, 4]) == []

    # Numbers containing a zero digit are excluded
    assert module_0.unique_digits([101, 135, 246]) == [135]

    # Input order should not matter - result is sorted
    assert module_0.unique_digits([33, 1, 15]) == [1, 15, 33]

    # Duplicates are preserved
    assert module_0.unique_digits([3, 3, 7, 7]) == [3, 3, 7, 7]

    # Large multi-digit numbers
    assert module_0.unique_digits([111111, 13579, 24680]) == [111111, 13579]

    # Mixed with repeated odd digits
    assert module_0.unique_digits([111, 222, 333, 444]) == [111, 333]

    print("All tests passed!")


# Run the test
test_unique_digits()

# Generated at 2026-11-03 01:04:56.375692
# Unit test for function unique_digits
def test_unique_digits():
    # Test with mixed even and odd digit numbers
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # Test with some numbers containing even digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Test with single digit numbers
    assert module_0.unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]

    # Test with empty list
    assert module_0.unique_digits([]) == []

    # Test that results are sorted
    assert module_0.unique_digits([57, 31, 9, 71]) == [9, 31, 57, 71]

    # Test with all numbers having odd digits
    assert module_0.unique_digits([135, 13, 79]) == [13, 79, 135]

    # Test with all numbers containing even digits
    assert module_0.unique_digits([24, 46, 80, 2]) == []

    # Test with duplicate values
    assert module_0.unique_digits([11, 11, 13, 11]) == [11, 11, 11, 13]

    # Test with zero (contains even digit 0)
    assert module_0.unique_digits([0, 1]) == [1]

# Generated at 2026-11-03 01:06:59.468847
# Unit test for function unique_digits
def test_unique_digits():
    # Test with mixed numbers: some all-odd digits, some containing even digits
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    
    # Test where no element has all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    
    # Test that output is sorted even when input is unsorted
    assert module_0.unique_digits([33, 1, 15]) == [1, 15, 33]
    
    # Test with empty list
    assert module_0.unique_digits([]) == []
    
    # Test with single-digit numbers
    assert module_0.unique_digits([7, 4, 9, 2]) == [7, 9]
    
    # Test with duplicates
    assert module_0.unique_digits([11, 11, 22, 13]) == [11, 11, 13]
    
    # Test with multi-digit all-odd numbers
    assert module_0.unique_digits([135, 579, 246, 111]) == [111, 135, 579]
    
    # Test preserving multiplicity and ordering together
    assert module_0.unique_digits([9, 3, 5, 1]) == [1, 3, 5, 9]
    
    print("All tests passed!")


test_unique_digits()

# Generated at 2026-11-03 01:10:43.744660
# Unit test for function unique_digits
def test_unique_digits():
    # Test with mixed elements: some with all odd digits, some with even digits
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # Test with all elements containing even digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Test with empty list
    assert module_0.unique_digits([]) == []

    # Test with all elements having odd digits
    assert module_0.unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

    # Test sorting behavior: input unsorted, output must be sorted
    assert module_0.unique_digits([33, 1, 15, 111]) == [1, 15, 33, 111]

    # Test with duplicates
    assert module_0.unique_digits([3, 3, 5, 5]) == [3, 3, 5, 5]

    # Test with single element
    assert module_0.unique_digits([13579]) == [13579]

    # Test with multi-digit numbers where one digit is even
    assert module_0.unique_digits([13, 24, 35, 46]) == [13, 35]

    # Test with zero (contains even digit 0)
    assert module_0.unique_digits([0]) == []

    # Test with large numbers
    assert module_0.unique_digits([999999, 1000000, 111111]) == [111111, 999999]

    print("All tests passed!")


if __name__ == "__main__":
    test_unique_digits()

# Generated at 2026-11-03 01:12:24.801372
# Unit test for function unique_digits
def test_unique_digits():
    # Basic case: mix of numbers with all odd digits and others
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No elements have all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty input list
    assert module_0.unique_digits([]) == []

    # All elements have only odd digits
    assert module_0.unique_digits([13, 57, 9]) == [9, 13, 57]

    # Single-digit numbers: odd kept, even filtered out
    assert module_0.unique_digits([2, 3, 4, 5, 7]) == [3, 5, 7]

    # Input order is not preserved; result must be sorted
    assert module_0.unique_digits([111, 31, 15]) == [15, 31, 111]

    # Duplicates are preserved
    assert module_0.unique_digits([11, 11, 22, 13]) == [11, 11, 13]

    # Numbers containing zero are excluded (0 is even)
    assert module_0.unique_digits([0, 10, 101, 135]) == [135]

    # Large numbers with all odd digits
    assert module_0.unique_digits([13579, 24680, 97531]) == [13579, 97531]

    # Multi-digit number where one even digit disqualifies it
    assert module_0.unique_digits([123, 135]) == [135]

    print("All tests passed!")


if __name__ == "__main__":
    test_unique_digits()