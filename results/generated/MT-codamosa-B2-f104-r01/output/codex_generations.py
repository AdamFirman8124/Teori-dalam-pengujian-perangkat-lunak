

# Generated at 2026-11-02 08:18:39.423743
# Unit test for function unique_digits
def test_unique_digits():
    # Test with mixed numbers: all-odd-digit numbers should be kept and sorted
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    
    # Test with no all-odd-digit numbers
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    
    # Test with empty list
    assert module_0.unique_digits([]) == []
    
    # Test with single all-odd-digit number
    assert module_0.unique_digits([135]) == [135]
    
    # Test with single even-digit number
    assert module_0.unique_digits([246]) == []
    
    # Test that results are sorted ascending
    assert module_0.unique_digits([931, 7, 31, 123, 75]) == [7, 31, 75, 931]
    
    # Test with duplicate all-odd-digit numbers
    assert module_0.unique_digits([33, 33, 5]) == [5, 33, 33]
    
    # Test with negative number (digits of absolute value considered)
    assert module_0.unique_digits([-13, 15, 24]) == [15]
    
    # Test with zero (0 is even, so excluded)
    assert module_0.unique_digits([0, 1]) == [1]
    
    # Test with large all-odd-digit numbers
    assert module_0.unique_digits([111111, 999999, 123]) == [111111, 999999]
    
    print("All tests passed!")


test_unique_digits()

# Generated at 2026-11-02 08:19:32.553565
# Unit test for function unique_digits
def test_unique_digits():
    # Basic case: mix of numbers with all odd digits and some with even digits
    assert module_0.unique_digits([15, 33, 1422, 1, 15]) == [1, 15, 15, 33]

    # Numbers with even digits are excluded
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty input list
    assert module_0.unique_digits([]) == []

    # All elements have odd digits
    assert module_0.unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

    # Result should be sorted even if input is unsorted
    assert module_0.unique_digits([33, 1, 5]) == [1, 5, 33]

    # Zero contains an even digit, so it is excluded
    assert module_0.unique_digits([0, 11, 22, 13]) == [11, 13]

    # Single element with all odd digits
    assert module_0.unique_digits([7]) == [7]

    # Single element with an even digit
    assert module_0.unique_digits([8]) == []

    # Multi-digit numbers where only one digit is even
    assert module_0.unique_digits([111, 112, 131, 222]) == [111, 131]

    # Large numbers
    assert module_0.unique_digits([13579, 24680, 99999, 12345]) == [13579, 99999]

    print("All tests passed!")


test_unique_digits()

# Generated at 2026-11-02 08:20:09.830099
# Unit test for function unique_digits
def test_unique_digits():
    # Elements with only odd digits are kept and sorted ascending
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # All elements contain at least one even digit -> empty result
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Multi-digit filtering with sorted output
    assert module_0.unique_digits([12345, 2033, 111, 151]) == [111, 151]

    # Sorting matters regardless of input order
    assert module_0.unique_digits([135, 103, 31]) == [31, 135]

    # Empty input yields empty output
    assert module_0.unique_digits([]) == []

    # Single odd-digit element
    assert module_0.unique_digits([7]) == [7]

    # Single even digit is excluded
    assert module_0.unique_digits([8]) == []

    # Zero anywhere disqualifies the number
    assert module_0.unique_digits([0, 13]) == [13]

    # Even digit in the middle disqualifies the number
    assert module_0.unique_digits([19, 21, 31]) == [19, 31]

    # Duplicates are preserved (function only filters and sorts)
    assert module_0.unique_digits([3, 3, 2]) == [3, 3]

    # Output is sorted even when input is reverse-ordered
    assert module_0.unique_digits([99, 1, 13]) == [1, 13, 99]

# Generated at 2026-11-02 08:20:35.330848
# Unit test for function unique_digits
def test_unique_digits():
    # Basic mixed case
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    # All digits odd, unsorted input
    assert module_0.unique_digits([311, 13, 111]) == [111, 311, 13] or module_0.unique_digits([311, 13, 111]) == [13, 111, 311]
    # Empty list
    assert module_0.unique_digits([]) == []
    # No elements with all odd digits
    assert module_0.unique_digits([2, 4, 6, 8]) == []
    # Single element with all odd digits
    assert module_0.unique_digits([135]) == [135]
    # Single element with an even digit
    assert module_0.unique_digits([1357]) == [1357]
    # Contains zero (even digit)
    assert module_0.unique_digits([101, 111]) == [111]
    # Duplicates preserved
    assert module_0.unique_digits([11, 11, 33]) == [11, 11, 33]
    # Single-digit numbers
    assert module_0.unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
    # Result is sorted regardless of input order
    assert module_0.unique_digits([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
    # Larger numbers with all odd digits
    assert module_0.unique_digits([111, 133, 155, 122]) == [111, 133, 155]
    # Mixed with multi-digit and single-digit
    assert module_0.unique_digits([12, 31, 45, 57, 99]) == [31, 57, 99]
    print("All tests passed!")


class TestUniqueDigits(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(module_0.unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_empty(self):
        self.assertEqual(module_0.unique_digits([]), [])

    def test_no_odd_digits(self):
        self.assertEqual(module_0.unique_digits([2, 4, 6, 8]), [])

    def test_all_odd(self):
        self.assertEqual(module_0.unique_digits([9, 7, 5, 3, 1]), [1, 3, 5, 7, 9])

    def test_zero_is_even(self):
        self.assertEqual(module_0.unique_digits([101, 111]), [111])

    def test_duplicates(self):
        self.assertEqual(module_0.unique_digits([11, 11, 33]), [11, 11, 33])

    def test_sorted_output(self):
        self.assertEqual(module_0.unique_digits([99, 13, 5]), [5, 13, 99])

    def test_single_element(self):
        self.assertEqual(module_0.unique_digits([13579]), [13579])


if __name__ == "__main__":
    test_unique_digits()
    unittest.main()

# Generated at 2026-11-02 08:21:56.018896
# Unit test for function unique_digits
def test_unique_digits():
    # Basic case: mixed numbers, only odd-digit elements kept, sorted
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No elements with all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty input list
    assert module_0.unique_digits([]) == []

    # Single element with all odd digits
    assert module_0.unique_digits([135]) == [135]

    # Duplicates are preserved and sorted
    assert module_0.unique_digits([11, 11, 13]) == [11, 11, 13]

    # Zero is an even digit, so 0 is excluded
    assert module_0.unique_digits([0, 1, 3]) == [1, 3]

    # Unsorted input returns sorted output
    assert module_0.unique_digits([31, 57, 13]) == [13, 31, 57]

    # Larger numbers
    assert module_0.unique_digits([999999, 2468, 13579]) == [13579, 999999]

    # Single-digit numbers
    assert module_0.unique_digits([2, 4, 6, 8]) == []
    assert module_0.unique_digits([9, 7, 5]) == [5, 7, 9]


if __name__ == "__main__":
    test_unique_digits()
    print("All tests passed!")