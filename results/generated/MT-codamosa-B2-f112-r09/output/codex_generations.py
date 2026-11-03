

# Generated at 2026-11-01 19:47:46.306515
# Unit test for function reverse_delete
def test_reverse_delete():
    # Test case 1: Deleting 'a' and 'e' leaves non-palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    
    # Test case 2: Deleting 'b' leaves non-palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    
    # Test case 3: Deleting 'a' and 'b' leaves palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    
    # Test case 4: No characters deleted, already palindrome
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    
    # Test case 5: All characters deleted, empty string is palindrome
    assert module_0.reverse_delete("aaaa", "a") == ("", True)
    
    # Test case 6: Single character remains
    assert module_0.reverse_delete("abca", "bc") == ("aa", True)
    
    # Test case 7: Delete all but one character
    assert module_0.reverse_delete("hello", "hell") == ("o", True)
    
    # Test case 8: Deleting vowels creates palindrome
    assert module_0.reverse_delete("madamimadam", "x") == ("madamimadam", True)
    
    # Test case 9: Delete repeated characters
    assert module_0.reverse_delete("mississippi", "is") == ("mpp", False)
    
    # Test case 10: Deletion results in palindrome check
    assert module_0.reverse_delete("abcba", "cb") == ("aa", True)
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_reverse_delete()

# Generated at 2026-11-01 19:48:26.649631
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic cases: returns (filtered string, is_palindrome)
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("abcdedcba", "abcd") == ("edc", False)
    assert module_0.reverse_delete("hello", "l") == ("heo", False)

    # Deleting all characters leaves an empty string (a palindrome)
    assert module_0.reverse_delete("aaaa", "a") == ("", True)
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # Single character strings are palindromes
    assert module_0.reverse_delete("a", "b") == ("a", True)

    # Empty string input
    assert module_0.reverse_delete("", "a") == ("", True)

    # Deleting nothing (c contains no chars from s)
    assert module_0.reverse_delete("abc", "xyz") == ("abc", False)
    assert module_0.reverse_delete("aba", "xyz") == ("aba", True)

    # Palindrome formed after deletion
    assert module_0.reverse_delete("abccba", "a") == ("bccb", True)

    # Case sensitivity check
    assert module_0.reverse_delete("Aa", "A") == ("a", True)

    # Digits and special characters
    assert module_0.reverse_delete("12321", "1") == ("232", True)
    assert module_0.reverse_delete("a!b!a", "!") == ("aba", True)

    # Verify return type is a tuple
    result = module_0.reverse_delete("abc", "b")
    assert isinstance(result, tuple) and len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_reverse_delete()

# Generated at 2026-11-01 19:48:50.256645
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic case: delete characters, result is not a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    
    # Delete one character, result is not a palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    
    # Deletion results in a palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    
    # Deleting a middle character, result not a palindrome
    assert module_0.reverse_delete("dwik", "w") == ("dik", False)
    
    # Deleting the only character results in empty string (palindrome)
    assert module_0.reverse_delete("a", "a") == ("", True)
    
    # Empty deletion string leaves s unchanged (and it's a palindrome)
    assert module_0.reverse_delete("abcdedcba", "") == ("abcdedcba", True)
    
    # No characters to delete, non-palindrome remains non-palindrome
    assert module_0.reverse_delete("abc", "xyz") == ("abc", False)
    
    # Delete all characters
    assert module_0.reverse_delete("aaaa", "a") == ("", True)
    
    # Deleting characters from an empty string
    assert module_0.reverse_delete("", "a") == ("", True)
    
    # Case sensitivity check
    assert module_0.reverse_delete("Aba", "a") == ("Ab", False)

# Generated at 2026-11-01 19:49:17.901888
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic deletion and palindrome checks
    assert module_0.reverse_delete("abcde", "ae") == ('bcd', False)
    assert module_0.reverse_delete("abcdef", "b") == ('acdef', False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert module_0.reverse_delete("dwik", "w") == ('dik', False)

    # Deleting all characters yields an empty palindrome
    assert module_0.reverse_delete("a", "a") == ('', True)
    assert module_0.reverse_delete("abcdef", "abcdef") == ('', True)

    # Deleting everything except a single character is a palindrome
    assert module_0.reverse_delete("abcdedcba", "abcd") == ('e', True)

    # No characters to delete
    assert module_0.reverse_delete("hello", "") == ('hello', False)
    assert module_0.reverse_delete("racecar", "") == ('racecar', True)

    # Characters in c that don't appear in s have no effect
    assert module_0.reverse_delete("abc", "xyz") == ('abc', False)

    # Deleting from an already-palindromic string may break the palindrome
    assert module_0.reverse_delete("madamimadam", "mad") == ('im', False)

    # Result is always a (string, bool) tuple
    result = module_0.reverse_delete("abba", "a")
    assert isinstance(result, tuple) and len(result) == 2
    assert isinstance(result[0], str) and isinstance(result[1], bool)

# Generated at 2026-11-01 19:49:31.212957
# Unit test for function reverse_delete
def test_reverse_delete():import unittest


class TestReverseDelete(unittest.TestCase):

    def test_basic_non_palindrome(self):
        # Remove 'a' from "abcde" -> "bcde", not a palindrome
        self.assertEqual(module_0.reverse_delete("abcde", "a"), ("bcde", False))

    def test_remove_vowels(self):
        # Remove vowels from "abcdef" -> "bcdf", not a palindrome
        self.assertEqual(module_0.reverse_delete("abcdef", "aeiou"), ("bcdf", False))

    def test_palindrome_result(self):
        # Remove 'b' from "abcdedcba" -> "cdedc", which is a palindrome
        self.assertEqual(module_0.reverse_delete("abcdedcba", "b"), ("cdedc", True))

    def test_remove_all_characters(self):
        # Removing every character yields an empty string, trivially a palindrome
        self.assertEqual(module_0.reverse_delete("aaaa", "a"), ("", True))
        self.assertEqual(module_0.reverse_delete("abc", "abc"), ("", True))

    def test_empty_input_string(self):
        # Empty string stays empty and is a palindrome
        self.assertEqual(module_0.reverse_delete("", "abc"), ("", True))

    def test_no_matching_characters(self):
        # Characters to delete don't appear in s; result unchanged
        self.assertEqual(module_0.reverse_delete("xyz", "abc"), ("xyz", False))
        self.assertEqual(module_0.reverse_delete("aa", "b"), ("aa", True))

    def test_empty_delete_set(self):
        # Nothing to delete, original returned with its palindrome status
        self.assertEqual(module_0.reverse_delete("racecar", ""), ("racecar", True))
        self.assertEqual(module_0.reverse_delete("hello", ""), ("hello", False))

    def test_repeated_chars_in_c(self):
        # Duplicate characters in c should be handled correctly
        self.assertEqual(module_0.reverse_delete("banana", "nn"), ("baaaa", False))

    def test_case_sensitivity(self):
        # Deletion is case-sensitive
        self.assertEqual(module_0.reverse_delete("AaBbCc", "ABC"), ("ac", False))


if __name__ == "__main__":
    unittest.main()