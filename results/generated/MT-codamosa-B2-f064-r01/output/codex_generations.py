

# Generated at 2026-11-02 18:41:34.393841
# Unit test for function vowels_count
def test_vowels_count():
    # Basic cases
    assert module_0.vowels_count("abcde") == 2, "abcde should have 2 vowels"
    assert module_0.vowels_count("Alone") == 3, "Alone should have 3 vowels"
    
    # Trailing 'y' counts as a vowel
    assert module_0.vowels_count("key") == 2, "key should have 2 vowels (e + trailing y)"
    assert module_0.vowels_count("keY") == 2, "keY should have 2 vowels (e + trailing Y)"
    assert module_0.vowels_count("bye") == 1, "bye should have 1 vowel (y not at end)"
    assert module_0.vowels_count("bYe") == 1, "bYe should have 1 vowel (Y not at end)"
    assert module_0.vowels_count("ACEDY") == 3, "ACEDY should have 3 vowels"
    
    # 'y' in middle does not count
    assert module_0.vowels_count("Python") == 1, "Python should have 1 vowel"
    assert module_0.vowels_count("xyz") == 1, "xyz should have 1 vowel (trailing y)"
    
    # Uppercase vowels
    assert module_0.vowels_count("AEIOU") == 5, "AEIOU should have 5 vowels"
    assert module_0.vowels_count("aeiouAEIOU") == 10, "Mixed case vowels should all count"
    
    # No vowels
    assert module_0.vowels_count("bcdfg") == 0, "bcdfg should have 0 vowels"
    assert module_0.vowels_count("BCDFG") == 0, "BCDFG should have 0 vowels"
    
    # Single character strings
    assert module_0.vowels_count("a") == 1, "'a' should have 1 vowel"
    assert module_0.vowels_count("y") == 1, "'y' should have 1 vowel (trailing y)"
    assert module_0.vowels_count("Y") == 1, "'Y' should have 1 vowel (trailing Y)"
    assert module_0.vowels_count("b") == 0, "'b' should have 0 vowels"
    
    # All vowels plus trailing y
    assert module_0.vowels_count("aeiouy") == 6, "aeiouy should have 6 vowels"
    
    # Empty string raises IndexError (s[-1] fails)
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass

# Generated at 2026-11-02 18:42:58.440098
# Unit test for function vowels_count
def test_vowels_count():
    # Basic cases with vowels
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("Alone") == 3
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aeiou") == 5

    # Strings ending in 'y' or 'Y' get +1
    assert module_0.vowels_count("acy") == 1
    assert module_0.vowels_count("abcdeY") == 3
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("HURRAY") == 3

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("xyz") == 1  # ends in y
    assert module_0.vowels_count("12345!@#") == 0

    # Mixed case vowels
    assert module_0.vowels_count("aEiOu") == 5
    assert module_0.vowels_count("AbCdEfG") == 1

    # Single characters
    assert module_0.vowels_count("a") == 1
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("b") == 0

    # Vowels in middle don't count as ending y
    assert module_0.vowels_count("eye") == 2  # e, e are vowels, ends in 'e' not 'y'

    # Empty string raises IndexError
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass

    # Longer sentences
    assert module_0.vowels_count("The quick brown fox") == 5
    assert module_0.vowels_count("Programming is fun") == 5

    print("All test_vowels_count tests passed!")


if __name__ == "__main__":
    test_vowels_count()

# Generated at 2026-11-02 18:44:37.797509
# Unit test for function vowels_count
def test_vowels_count():import unittest


class TestVowelsCount(unittest.TestCase):

    def test_no_vowels(self):
        self.assertEqual(module_0.vowels_count("bcdfg"), 0)

    def test_all_vowels(self):
        self.assertEqual(module_0.vowels_count("aeiou"), 5)

    def test_uppercase_vowels(self):
        self.assertEqual(module_0.vowels_count("AEIOU"), 5)

    def test_mixed_case(self):
        self.assertEqual(module_0.vowels_count("AbEcIdOfU"), 5)

    def test_word_with_vowels(self):
        self.assertEqual(module_0.vowels_count("hello"), 2)

    def test_y_at_end(self):
        self.assertEqual(module_0.vowels_count("happy"), 2)

    def test_uppercase_y_at_end(self):
        self.assertEqual(module_0.vowels_count("HAPPY"), 2)

    def test_y_in_middle_not_counted(self):
        self.assertEqual(module_0.vowels_count("yellow"), 2)

    def test_single_vowel(self):
        self.assertEqual(module_0.vowels_count("a"), 1)

    def test_y_only(self):
        self.assertEqual(module_0.vowels_count("y"), 1)

    def test_uppercase_y_only(self):
        self.assertEqual(module_0.vowels_count("Y"), 1)

    def test_empty_vowel_string_with_y(self):
        self.assertEqual(module_0.vowels_count("bcdfgy"), 1)

    def test_numbers_and_special_chars(self):
        self.assertEqual(module_0.vowels_count("123!@#"), 0)

    def test_sentence(self):
        self.assertEqual(module_0.vowels_count("This is a test"), 4)

    def test_vowel_then_y(self):
        self.assertEqual(module_0.vowels_count("aye"), 2)

    def test_empty_string_raises_index_error(self):
        with self.assertRaises(IndexError):
            module_0.vowels_count("")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 18:46:08.342819
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2, "Failed for 'abcde'"
    assert module_0.vowels_count("Alone") == 3, "Failed for 'Alone'"
    assert module_0.vowels_count("hello") == 2, "Failed for 'hello'"

    # All vowels, upper and lower case
    assert module_0.vowels_count("AEIOU") == 5, "Failed for 'AEIOU'"
    assert module_0.vowels_count("aeiou") == 5, "Failed for 'aeiou'"
    assert module_0.vowels_count("aEiOu") == 5, "Failed for 'aEiOu'"

    # No vowels present
    assert module_0.vowels_count("bcdfg") == 0, "Failed for 'bcdfg'"
    assert module_0.vowels_count("BCDFG") == 0, "Failed for 'BCDFG'"

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("happy") == 2, "Failed for 'happy'"
    assert module_0.vowels_count("MY") == 1, "Failed for 'MY'"
    assert module_0.vowels_count("y") == 1, "Failed for 'y'"
    assert module_0.vowels_count("Y") == 1, "Failed for 'Y'"

    # 'y' in the middle does NOT count as a vowel
    assert module_0.vowels_count("yellow") == 2, "Failed for 'yellow'"
    assert module_0.vowels_count("Python") == 1, "Failed for 'Python'"

    # Single characters
    assert module_0.vowels_count("a") == 1, "Failed for 'a'"
    assert module_0.vowels_count("b") == 0, "Failed for 'b'"

    # Digits and symbols (no vowels)
    assert module_0.vowels_count("12345!@#") == 0, "Failed for '12345!@#'"

    print("All tests passed!")


test_vowels_count()

# Generated at 2026-11-02 18:47:20.946375
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2, "Expected 2 vowels in 'abcde'"
    assert module_0.vowels_count("hello") == 2, "Expected 2 vowels in 'hello'"
    assert module_0.vowels_count("Alone") == 3, "Expected 3 vowels in 'Alone'"

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("key") == 2, "'y' at end should count as vowel"
    assert module_0.vowels_count("y") == 1, "Single 'y' should count"
    assert module_0.vowels_count("Y") == 1, "Single 'Y' should count"
    assert module_0.vowels_count("ACEDY") == 3, "A, E plus 'Y' at end"

    # 'y'/'Y' NOT at the end should not count
    assert module_0.vowels_count("bye") == 1, "'y' mid-string shouldn't count"
    assert module_0.vowels_count("Yellow") == 2, "Y at start doesn't count; e, o do"

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0, "No vowels expected"
    assert module_0.vowels_count("!!!") == 0, "Symbols only, no vowels"

    # All vowels, mixed case
    assert module_0.vowels_count("aeiou") == 5, "All lowercase vowels"
    assert module_0.vowels_count("AEIOU") == 5, "All uppercase vowels"
    assert module_0.vowels_count("aEiOu") == 5, "Mixed case vowels"

    # Vowels mixed with digits
    assert module_0.vowels_count("a1e2i3") == 3, "Digits ignored"

    # Empty string raises IndexError (s[-1] on empty string)
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass

    print("All tests passed!")