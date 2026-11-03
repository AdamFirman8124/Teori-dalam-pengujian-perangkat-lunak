

# Generated at 2026-11-02 14:09:43.016825
# Unit test for function count_upper
def test_count_upper():
    # Basic cases with mixed characters
    assert module_0.count_upper('aBCdEf') == 1   # 'E' at index 4 is an uppercase vowel
    assert module_0.count_upper('abcdefg') == 0  # no uppercase vowels at even indices
    assert module_0.count_upper('dBBE') == 0     # 'E' is at odd index 3
    assert module_0.count_upper('AEIOU') == 3    # 'A', 'I', 'U' at even indices

    # Edge cases
    assert module_0.count_upper('') == 0         # empty string
    assert module_0.count_upper('A') == 1        # single uppercase vowel
    assert module_0.count_upper('B') == 0        # single consonant
    assert module_0.count_upper('a') == 0        # lowercase vowel is not counted

    # Vowels at alternating positions
    assert module_0.count_upper('AoAoAo') == 3   # 'A' at 0, 2, 4
    assert module_0.count_upper('AoA') == 2      # 'A' at 0 and 2
    assert module_0.count_upper('AAAA') == 2     # indices 0 and 2 only

    # Only odd-indexed uppercase vowels
    assert module_0.count_upper('aEaE') == 0
    assert module_0.count_upper('bAbAbA') == 0

    # Repetitive uppercase vowels
    assert module_0.count_upper('UUUUUU') == 3

    print("All test cases passed!")

# Generated at 2026-11-02 14:11:23.715878
# Unit test for function count_upper
def test_count_upper():import unittest


def module_0.count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in "AEIOU":
            count += 1
    return count


class TestCountUpper(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(module_0.count_upper(""), 0)

    def test_single_upper_vowel_even_index(self):
        self.assertEqual(module_0.count_upper("A"), 1)

    def test_single_lower_vowel_even_index(self):
        self.assertEqual(module_0.count_upper("a"), 0)

    def test_mixed_case_vowels(self):
        self.assertEqual(module_0.count_upper("aBCdEf"), 1)

    def test_alternating_upper_vowels(self):
        self.assertEqual(module_0.count_upper("abcdefg"), 0)

    def test_all_upper_vowels_even_indices(self):
        self.assertEqual(module_0.count_upper("AEIOU"), 3)  # A, I, U at even indices

    def test_vowels_at_odd_indices(self):
        self.assertEqual(module_0.count_upper("bAcEdIfOgU"), 0)  # vowels at odd indices only

    def test_no_vowels(self):
        self.assertEqual(module_0.count_upper("bcdfg"), 0)

    def test_upper_vowels_mixed_positions(self):
        self.assertEqual(module_0.count_upper("AbE"), 1)  # A at index 0

    def test_string_with_digits_and_vowels(self):
        self.assertEqual(module_0.count_upper("A1E3I5O7U"), 3)

    def test_long_string(self):
        self.assertEqual(module_0.count_upper("AEIOU" * 3), 9)

    def test_only_consonants_upper(self):
        self.assertEqual(module_0.count_upper("BCDFG"), 0)

    def test_y_is_not_counted(self):
        self.assertEqual(module_0.count_upper("Y"), 0)

    def test_upper_vowels_second_half(self):
        self.assertEqual(module_0.count_upper("xyzAEIOU"), 1)  # only A at index 3? no—E at index 4 counts

    def test_whitespace_string(self):
        self.assertEqual(module_0.count_upper(" "), 0)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 14:13:16.385821
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("aBCdEf") == 1   # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels at even indices
    assert module_0.count_upper("dBBE") == 0     # no uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3    # 'A' at 0, 'I' at 2, 'U' at 4
    assert module_0.count_upper("") == 0         # empty string
    assert module_0.count_upper("U") == 1        # single uppercase vowel
    assert module_0.count_upper("x") == 0        # single non-vowel char
    assert module_0.count_upper("a") == 0        # lowercase vowel at even index doesn't count
    assert module_0.count_upper("OaAaEaIaUaO") == 5  # O,A,E,I,U at even indices
    assert module_0.count_upper("BCDFG") == 0    # no vowels at all
    print("All test cases passed!")

test_count_upper()

# Generated at 2026-11-02 14:15:05.439721
# Unit test for function count_upper
def test_count_upper():
    # Empty string
    assert module_0.count_upper("") == 0
    # All uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)
    # No vowels at all
    assert module_0.count_upper("bcdfg") == 0
    # Lowercase vowels should not count
    assert module_0.count_upper("aeiou") == 0
    # Mixed case: only uppercase vowels at even indices count
    assert module_0.count_upper("aBCdEf") == 1  # E at index 4
    assert module_0.count_upper("abcdefg") == 0
    # Uppercase vowel at odd index should not count
    assert module_0.count_upper("aEIOU") == 1  # I(2), U(4); E at index 1 skipped
    # Single characters
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("B") == 0
    assert module_0.count_upper("a") == 0
    # Uppercase non-vowels should not count
    assert module_0.count_upper("BBBEB") == 0
    # Longer mixed string
    assert module_0.count_upper("AbEcIdOfU") == 0  # vowels at even indices are lowercase
    assert module_0.count_upper("AAAA") == 2  # A(0), A(2)
    # String with digits and symbols
    assert module_0.count_upper("A1E2I") == 3  # A(0), E(2), I(4)

# Generated at 2026-11-02 14:16:41.545982
# Unit test for function count_upper
def test_count_upper():
    # Basic cases
    assert module_0.count_upper("aBCdEf") == 1
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)
    
    # Empty string
    assert module_0.count_upper("") == 0
    
    # Single character
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("B") == 0
    
    # Vowels at odd indices should not count
    assert module_0.count_upper("xAEI") == 1  # A at index 1, E at index 2
    assert module_0.count_upper("xE") == 0    # E at index 1 (odd)
    
    # Uppercase vowels only
    assert module_0.count_upper("aeiou") == 0  # lowercase vowels don't count
    
    # All uppercase vowels at even indices
    assert module_0.count_upper("AEAEAE") == 3  # indices 0, 2, 4
    
    # Consonants only
    assert module_0.count_upper("BCDFG") == 0
    
    # 'Y' is not a vowel
    assert module_0.count_upper("Y") == 0
    
    # Mixed content with special characters
    assert module_0.count_upper("A!B#C$D") == 1  # only A at index 0
    assert module_0.count_upper(" A E ") == 2    # A at 0, E at 2
    
    # Long string
    assert module_0.count_upper("AEIOU" * 10) == 30  # 3 vowels per 5 chars * 10
    
    # Vowel at last even index
    assert module_0.count_upper("xxU") == 1
    assert module_0.count_upper("xxUx") == 1  # U at index 2, length 4 means last even index is 2