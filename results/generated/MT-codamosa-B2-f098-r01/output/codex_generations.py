

# Generated at 2026-11-01 20:32:55.478198
# Unit test for function count_upper
def test_count_upper():
    # Uppercase vowel at even index
    assert module_0.count_upper('aBCdEf') == 1
    # No uppercase vowels at even indices
    assert module_0.count_upper('abcdefg') == 0
    # Uppercase consonant at even index doesn't count
    assert module_0.count_upper('dBBE') == 0
    # All uppercase vowels at even indices
    assert module_0.count_upper('AEIOU') == 3
    # Empty string
    assert module_0.count_upper('') == 0
    # Single uppercase vowel
    assert module_0.count_upper('A') == 1
    # Single lowercase vowel
    assert module_0.count_upper('a') == 0
    # Uppercase vowels only at odd indices
    assert module_0.count_upper('bAeIo') == 0
    # Mixed case with multiple matches
    assert module_0.count_upper('AbEdIfOgU') == 0
    assert module_0.count_upper('aEiOu') == 1
    # Uppercase vowel at index 0
    assert module_0.count_upper('Ebcdef') == 1
    # Non-letter characters
    assert module_0.count_upper('1E3I5U') == 3

test_count_upper()
print("All tests passed!")

# Generated at 2026-11-01 20:33:31.628141
# Unit test for function count_upper
def test_count_upper():
    # Basic cases from examples
    assert module_0.count_upper("aBCdEf") == 1   # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0     # 'E' at odd index 3

    # Edge cases
    assert module_0.count_upper("") == 0         # empty string
    assert module_0.count_upper("B") == 0        # single consonant
    assert module_0.count_upper("A") == 1        # single uppercase vowel at index 0
    assert module_0.count_upper("a") == 0        # single lowercase vowel

    # All uppercase vowels
    assert module_0.count_upper("AEIOU") == 3    # A(0), I(2), U(4)
    assert module_0.count_upper("aEIOU") == 2    # I(2), U(4) — 'a' lowercase doesn't count

    # Lowercase vowels at even indices don't count
    assert module_0.count_upper("aeiou") == 0
    assert module_0.count_upper("bEiOu") == 0    # even indices: 'b','i','u' — none uppercase vowels

    # Multiple uppercase vowels at even indices
    assert module_0.count_upper("EVEN") == 2     # E(0), E(2)
    assert module_0.count_upper("UAEIOU") == 3   # U(0), E(2), O(4)

    # 'Y' is not a vowel
    assert module_0.count_upper("AY") == 1       # only A(0) counts
    assert module_0.count_upper("YE") == 0       # E at index 1 (odd)

    # Uppercase consonants at even indices don't count
    assert module_0.count_upper("BCDF") == 0

    # Longer mixed string
    assert module_0.count_upper("AbEcEdEf") == 2 # E(2), E(6)

    print("All test_count_upper tests passed!")


test_count_upper()

# Generated at 2026-11-01 20:33:51.186211
# Unit test for function count_upper
def test_count_upper():import unittest


class TestCountUpper(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(module_0.count_upper(""), 0)

    def test_no_vowels(self):
        self.assertEqual(module_0.count_upper("bcdfg"), 0)

    def test_all_vowels(self):
        self.assertEqual(module_0.count_upper("AEIOU"), 3)

    def test_lowercase_vowels_ignored(self):
        self.assertEqual(module_0.count_upper("aeiou"), 0)

    def test_mixed_case(self):
        self.assertEqual(module_0.count_upper("aBCdEf"), 1)

    def test_vowels_at_odd_indices(self):
        self.assertEqual(module_0.count_upper("xAeIoU"), 0)

    def test_single_char(self):
        self.assertEqual(module_0.count_upper("A"), 1)
        self.assertEqual(module_0.count_upper("B"), 0)

    def test_longer_string(self):
        self.assertEqual(module_0.count_upper("AbEdIfOhU"), 5)

    def test_consonants_only_even_indices(self):
        self.assertEqual(module_0.count_upper("AEIOUXYZ"), 3)

    def test_alternating(self):
        self.assertEqual(module_0.count_upper("U"), 1)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 20:34:22.110180
# Unit test for function count_upper
def test_count_upper():
    # Basic cases with uppercase vowels at even indices
    assert module_0.count_upper("aBCdEf") == 1, "Expected 1: 'E' at index 4"
    assert module_0.count_upper("abcdefg") == 0, "No uppercase vowels at even indices"
    assert module_0.count_upper("dBBE") == 0, "Uppercase vowel 'E' at odd index should not count"

    # Multiple uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3, "A(0), I(2), U(4) counted"
    assert module_0.count_upper("AbEcIdOfU") == 5, "All uppercase vowels at even indices"
    assert module_0.count_upper("AEBCEO") == 4, "A(0), E(2), E(4), O(6) counted"

    # Lowercase vowels should never count
    assert module_0.count_upper("aeiou") == 0, "Lowercase vowels not counted"
    assert module_0.count_upper("aEiOu") == 0, "Case-sensitive match required"

    # Edge cases
    assert module_0.count_upper("") == 0, "Empty string returns 0"
    assert module_0.count_upper("A") == 1, "Single uppercase vowel at index 0"
    assert module_0.count_upper("B") == 0, "Single consonant"
    assert module_0.count_upper("BCDFG") == 0, "No vowels at all"

    # Uppercase vowels only at odd indices
    assert module_0.count_upper("aEbEcEd") == 0, "Vowels at odd indices not counted"
    assert module_0.count_upper("xExExE") == 0, "Consonants at even indices"

    print("All test_count_upper tests passed!")


if __name__ == "__main__":
    test_count_upper()

# Generated at 2026-11-01 20:35:02.665555
# Unit test for function count_upper
def test_count_upper():
    # Empty string
    assert module_0.count_upper("") == 0
    # No vowels at all
    assert module_0.count_upper("bcdfg") == 0
    # Uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3      # A(0), I(2), U(4)
    # Uppercase vowels at odd indices only
    assert module_0.count_upper("aAeEiIoOuU") == 0 # vowels only at odd indices
    # Lowercase vowels at even indices
    assert module_0.count_upper("aeiou") == 0      # lowercase doesn't count
    # Mixed case
    assert module_0.count_upper("aBCdEf") == 1     # E at index 4
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0       # E at index 3 (odd)
    assert module_0.count_upper("B") == 0
    assert module_0.count_upper("A") == 1
    # Repeated uppercase vowels at even positions
    assert module_0.count_upper("AEIOUAEIOU") == 5 # indices 0,2,4,6,8
    # Vowel at index 0 counts
    assert module_0.count_upper("AbCdEf") == 2     # A(0), E(4)
    # Consonants only
    assert module_0.count_upper("BCDFG") == 0
    # Y is not a vowel
    assert module_0.count_upper("YY") == 0
    # Numbers and symbols
    assert module_0.count_upper("A1E3I5O7U9") == 3 # A(0), I(4), O(6)... actually E(2) too
    # Check: indices 0:A,1:1,2:E,3:3,4:I,5:5,6:O,7:7,8:U,9:9 -> A,E,I,O,U = 5
    assert module_0.count_upper("A1E3I5O7U9") == 5

test_count_upper()
print("All tests passed!")