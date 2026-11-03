

# Generated at 2026-11-02 06:48:06.145756
# Unit test for function same_chars
def test_same_chars():import unittest


class TestSameChars(unittest.TestCase):

    def test_identical_strings(self):
        self.assertTrue(module_0.same_chars("hello", "hello"))

    def test_same_chars_different_order(self):
        self.assertTrue(module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc"))

    def test_same_chars_subset_order(self):
        self.assertTrue(module_0.same_chars("abcd", "dcba"))

    def test_different_chars(self):
        self.assertFalse(module_0.same_chars("eabcd", "ddddddd"))

    def test_extra_char(self):
        self.assertFalse(module_0.same_chars("eabcd", "dddddddabc"))

    def test_empty_strings(self):
        self.assertTrue(module_0.same_chars("", ""))

    def test_one_empty_string(self):
        self.assertFalse(module_0.same_chars("", "a"))
        self.assertFalse(module_0.same_chars("a", ""))

    def test_single_chars(self):
        self.assertTrue(module_0.same_chars("a", "a"))
        self.assertFalse(module_0.same_chars("a", "b"))

    def test_repeated_chars(self):
        self.assertTrue(module_0.same_chars("aaa", "a"))
        self.assertTrue(module_0.same_chars("abcabc", "cab"))

    def test_case_sensitivity(self):
        self.assertFalse(module_0.same_chars("abc", "ABC"))

    def test_spaces_count(self):
        self.assertTrue(module_0.same_chars("a b", "ab "))
        self.assertFalse(module_0.same_chars("a b", "ab"))

    def test_special_characters(self):
        self.assertTrue(module_0.same_chars("a!b@", "@!ba"))
        self.assertFalse(module_0.same_chars("a!b", "a?b"))

    def test_digits(self):
        self.assertTrue(module_0.same_chars("123", "321"))
        self.assertFalse(module_0.same_chars("123", "1234"))

    def test_unicode(self):
        self.assertTrue(module_0.same_chars("héllo", "olléh"))
        self.assertFalse(module_0.same_chars("héllo", "hello"))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 06:48:12.489253
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") is True
    # Same characters, different order
    assert module_0.same_chars("abc", "cba") is True
    # Same characters, repeated
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    # Different characters
    assert module_0.same_chars("abcd", "adc") is False
    assert module_0.same_chars("eabcd", "dddddddabc") is False
    assert module_0.same_chars("abcd", "dddddddabce") is False
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzabcdcab") is True
    # Single characters
    assert module_0.same_chars("a", "a") is True
    assert module_0.same_chars("a", "b") is False
    # Empty strings
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("", "a") is False
    assert module_0.same_chars("a", "") is False
    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") is False
    assert module_0.same_chars("AbC", "AbC") is True
    # Spaces and special characters count as characters
    assert module_0.same_chars("a b c", "cba ") is True
    assert module_0.same_chars("a!b?", "?!a") is True
    assert module_0.same_chars("a!b", "?!a") is False
    # Unicode characters
    assert module_0.same_chars("héllo", "olléh") is True
    assert module_0.same_chars("héllo", "hello") is False
    # Long strings with same set
    assert module_0.same_chars("a" * 1000 + "b", "b" * 1000 + "a") is True

# Generated at 2026-11-02 06:48:19.676350
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("hello", "hello") is True
    
    # Same characters, different order and counts
    assert module_0.same_chars("eabcdzzzz", "dddzzzzbbcdcba") is True
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    
    # Different character sets
    assert module_0.same_chars("abcd", "adc") is False
    assert module_0.same_chars("abc", "ab") is False
    assert module_0.same_chars("abc", "abcd") is False
    
    # Empty strings
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("", "a") is False
    assert module_0.same_chars("a", "") is False
    
    # Single characters
    assert module_0.same_chars("a", "a") is True
    assert module_0.same_chars("a", "b") is False
    
    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") is False
    assert module_0.same_chars("aA", "Aa") is True
    
    # Special characters and digits
    assert module_0.same_chars("a1!", "1!a") is True
    assert module_0.same_chars("a b", "ab") is False
    
    # Duplicates don't matter
    assert module_0.same_chars("aaabbbccc", "abc") is True
    assert module_0.same_chars("xyz", "xxyyzz") is True

# Generated at 2026-11-02 06:48:23.566443
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("hello", "hello") is True
    # Same characters, different order
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    # Same characters despite repetition differences
    assert module_0.same_chars("abcd", "dddddddabc") is True
    assert module_0.same_chars("abcddd", "abc") is True
    # Different character sets
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabcf") is False
    assert module_0.same_chars("abc", "abd") is False
    # Empty strings
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("", "a") is False
    assert module_0.same_chars("a", "") is False
    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") is False
    assert module_0.same_chars("aAbB", "abAB") is True
    # Single characters
    assert module_0.same_chars("a", "a") is True
    assert module_0.same_chars("a", "b") is False
    # Special characters and digits
    assert module_0.same_chars("a!1", "1!a") is True
    assert module_0.same_chars("a!1", "a!2") is False
    # Unicode characters
    assert module_0.same_chars("héllo", "olléh") is True
    assert module_0.same_chars("héllo", "hello") is False

    print("All tests passed!")


if __name__ == "__main__":
    test_same_chars()

# Generated at 2026-11-02 06:48:29.677469
# Unit test for function same_chars
def test_same_chars():
    # Same characters, different order
    assert module_0.same_chars("abc", "cba") == True
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True
    
    # Different characters
    assert module_0.same_chars("abcd", "adc") == False
    assert module_0.same_chars("abcd", "adcde") == False
    
    # Duplicates in one string don't affect result
    assert module_0.same_chars("aabbcc", "abc") == True
    assert module_0.same_chars("aaa", "a") == True
    
    # Identical strings
    assert module_0.same_chars("hello", "hello") == True
    
    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    assert module_0.same_chars("a", "") == False
    
    # Single characters
    assert module_0.same_chars("x", "x") == True
    assert module_0.same_chars("x", "y") == False
    
    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") == False
    
    # Special characters and digits
    assert module_0.same_chars("a1!", "!1a") == True
    assert module_0.same_chars("123", "321") == True
    assert module_0.same_chars("python", "typhon") == True