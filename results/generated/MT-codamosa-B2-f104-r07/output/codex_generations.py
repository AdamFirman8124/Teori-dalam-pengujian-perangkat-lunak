

# Generated at 2026-11-02 19:50:48.771251
# Unit test for function unique_digits
def test_unique_digits():
    # Basic case: mixed numbers, only those with all odd digits are kept
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No numbers with all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty list
    assert module_0.unique_digits([]) == []

    # Single element with odd digits
    assert module_0.unique_digits([7]) == [7]

    # Result should be sorted regardless of input order
    assert module_0.unique_digits([135, 31, 9, 57]) == [9, 31, 57, 135]

    # Duplicates are preserved
    assert module_0.unique_digits([11, 11, 3]) == [3, 11, 11]

    # Zero contains the even digit 0, so it is excluded
    assert module_0.unique_digits([0, 1, 2]) == [1]

    # Larger multi-digit numbers
    assert module_0.unique_digits([13579, 2468, 111, 97531]) == [111, 13579, 97531]

    print("All tests passed!")


test_unique_digits()

# Generated at 2026-11-02 19:52:36.877874
# Unit test for function unique_digits
def test_unique_digits():
    # Basic mixed case: only elements with all odd digits are kept, sorted
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # Empty input list
    assert module_0.unique_digits([]) == []

    # All elements have even digits -> filtered out entirely
    assert module_0.unique_digits([2, 4, 2222, 80]) == []

    # All elements have odd digits -> all kept
    assert module_0.unique_digits([1, 3, 57, 135]) == [1, 3, 57, 135]

    # Unsorted input produces sorted output
    assert module_0.unique_digits([111, 31, 15, 3]) == [3, 15, 31, 111]

    # Duplicates are preserved
    assert module_0.unique_digits([11, 11, 3]) == [3, 11, 11]

    # Multi-digit numbers with mixed parity are excluded
    assert module_0.unique_digits([123, 135, 246, 579]) == [135, 579]

    # Single element list
    assert module_0.unique_digits([7]) == [7]

    # Zero is even, so it's excluded
    assert module_0.unique_digits([0, 9]) == [9]

    # Result is always sorted ascending
    result = module_0.unique_digits([99, 13, 5, 71])
    assert result == sorted(result)

    print("All tests passed!")

test_unique_digits()

# Generated at 2026-11-02 19:54:38.502512
# Unit test for function unique_digits
def test_unique_digits():
# nonce:9f564a18
    # Basic case: mix of all-odd-digit and even-containing numbers
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No elements with all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty list returns empty list
    assert module_0.unique_digits([]) == []

    # Single element with all odd digits
    assert module_0.unique_digits([7]) == [7]

    # Single element with an even digit
    assert module_0.unique_digits([24]) == []

    # Result must be sorted even if input is unsorted
    assert module_0.unique_digits([31, 13, 5, 57]) == [5, 13, 31, 57]

    # Duplicates are preserved
    assert module_0.unique_digits([11, 11, 3]) == [3, 11, 11]

    # Zero contains an even digit, so excluded
    assert module_0.unique_digits([0]) == []

    # Multi-digit numbers with all odd digits
    assert module_0.unique_digits([135, 975, 246]) == [135, 975]

    # Input order should not affect sorted output
    assert module_0.unique_digits([99, 1, 555, 2]) == [1, 99, 555]

    print("All tests passed!")


if __name__ == "__main__":
    test_unique_digits()

# Generated at 2026-11-02 19:56:50.867973
# Unit test for function unique_digits
def test_unique_digits():
    # Elements with all odd digits, sorted ascending
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # No elements with all odd digits
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Empty input
    assert module_0.unique_digits([]) == []

    # Single digits: odd ones kept, even ones (including 0) excluded
    assert module_0.unique_digits([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]

    # Result is sorted even when input is unsorted
    assert module_0.unique_digits([99, 11, 55]) == [11, 55, 99]

    # Duplicates are preserved
    assert module_0.unique_digits([11, 11, 13]) == [11, 11, 13]

    # Multi-digit numbers with any even digit are excluded
    assert module_0.unique_digits([13579, 24680, 111, 100]) == [111, 13579]

    # All elements qualify
    assert module_0.unique_digits([7, 5, 3]) == [3, 5, 7]

    # Large numbers with all odd digits
    assert module_0.unique_digits([97531, 1357, 11111]) == [1357, 11111, 97531]

# Generated at 2026-11-02 19:58:13.400685
# Unit test for function unique_digits
def test_unique_digits():import unittest


class TestUniqueDigits(unittest.TestCase):

    def test_mixed_odd_and_even_digits(self):
        self.assertEqual(module_0.unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_all_odd_digits(self):
        self.assertEqual(module_0.unique_digits([135, 379, 11]), [11, 135, 379])

    def test_no_odd_digit_elements(self):
        self.assertEqual(module_0.unique_digits([152, 323, 1422, 10]), [])

    def test_empty_list(self):
        self.assertEqual(module_0.unique_digits([]), [])

    def test_single_element_odd(self):
        self.assertEqual(module_0.unique_digits([7]), [7])

    def test_single_element_even(self):
        self.assertEqual(module_0.unique_digits([8]), [])

    def test_result_is_sorted(self):
        self.assertEqual(module_0.unique_digits([31, 13, 5, 571, 111]), [5, 13, 31, 111, 571])

    def test_duplicates_preserved(self):
        self.assertEqual(module_0.unique_digits([13, 13, 5]), [5, 13, 13])

    def test_zero_excluded(self):
        self.assertEqual(module_0.unique_digits([0, 1]), [1])

    def test_multi_digit_with_zero(self):
        self.assertEqual(module_0.unique_digits([101, 111]), [111])

    def test_large_numbers(self):
        self.assertEqual(module_0.unique_digits([13579, 24680, 97531]), [13579, 97531])

    def test_return_type_is_list(self):
        self.assertIsInstance(module_0.unique_digits([1, 2, 3]), list)

    def test_input_not_modified(self):
        original = [15, 33, 1422, 1]
        copy = list(original)
        module_0.unique_digits(original)
        self.assertEqual(original, copy)


if __name__ == "__main__":
    unittest.main()