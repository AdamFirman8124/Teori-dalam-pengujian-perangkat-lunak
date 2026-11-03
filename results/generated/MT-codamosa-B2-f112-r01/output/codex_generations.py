

# Generated at 2026-11-02 10:39:05.679777
# Unit test for function reverse_delete
def test_reverse_delete():
    # Test basic case: remove 'a' and 'e' from "abcde"
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)

    # Test removing single character 'b' from "abcdef"
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)

    # Test palindrome after deletion
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # Test removing all characters results in empty string (palindrome)
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # Test empty character set - string unchanged
    assert module_0.reverse_delete("abcde", "") == ("abcde", False)

    # Test removing all characters from string with duplicates
    assert module_0.reverse_delete("aabbcc", "abc") == ("", True)

    # Test string becomes palindrome after deletion
    assert module_0.reverse_delete("aba", "a") == ("b", True)

    # Test single character string
    assert module_0.reverse_delete("a", "a") == ("", True)
    assert module_0.reverse_delete("a", "b") == ("a", True)

    # Test string with repeated characters
    assert module_0.reverse_delete("hello", "l") == ("heo", False)

    # Test case where result is palindrome with multiple chars
    assert module_0.reverse_delete("racecar", "r") == ("aceca", True)

    # Test no characters removed
    assert module_0.reverse_delete("xyz", "abc") == ("xyz", False)

    print("All tests passed!")

if __name__ == "__main__":
    test_reverse_delete()

# Generated at 2026-11-02 10:40:54.323629
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic cases
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # Single character removal
    assert module_0.reverse_delete("dwik", "w") == ("dik", False)

    # Resulting in empty string (palindrome)
    assert module_0.reverse_delete("a", "a") == ("", True)

    # No characters removed (empty c)
    assert module_0.reverse_delete("abcdedcba", "") == ("abcdedcba", True)

    # Removing all characters
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # Case sensitivity check
    assert module_0.reverse_delete("Aba", "a") == ("Ab", False)

    # Repeated characters in c
    assert module_0.reverse_delete("hello", "l") == ("heo", False)

    print("All tests passed!")


if __name__ == "__main__":
    test_reverse_delete()

# Generated at 2026-11-02 10:42:37.818919
# Unit test for function reverse_delete
def test_reverse_delete():
    # Test case 1: Delete 'a' and 'e' from "abcde" -> "bcd", not a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)

    # Test case 2: Delete 'b' from "abcdef" -> "acdef", not a palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)

    # Test case 3: Delete 'a' and 'b' from "abcdedcba" -> "cdedc", a palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # Test case 4: Delete 'x' from "abcde" -> "abcde", not a palindrome
    assert module_0.reverse_delete("abcde", "x") == ("abcde", False)

    # Test case 5: Delete all characters -> empty string, which is a palindrome
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # Test case 6: Empty string input -> empty string, a palindrome
    assert module_0.reverse_delete("", "a") == ("", True)

    # Test case 7: Empty deletion set -> string unchanged, not a palindrome
    assert module_0.reverse_delete("abc", "") == ("abc", False)

    # Test case 8: Single character string is a palindrome after deletion
    assert module_0.reverse_delete("a", "b") == ("a", True)

    # Test case 9: Result becomes a palindrome after deletion
    assert module_0.reverse_delete("abccba", "a") == ("bccb", True)

    # Test case 10: Case sensitivity check
    assert module_0.reverse_delete("aA", "a") == ("A", True)

# Generated at 2026-11-02 10:44:04.689763
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic case: delete chars, result not palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)

    # Delete single char, result not palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)

    # Delete chars, result is palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # Result becomes palindrome after deletion
    assert module_0.reverse_delete("abba", "a") == ("bb", True)

    # No chars deleted (c not in s)
    assert module_0.reverse_delete("abc", "xyz") == ("abc", False)

    # Empty c deletes nothing, odd-length string not palindrome
    assert module_0.reverse_delete("abc", "") == ("abc", False)

    # Empty c, string already palindrome
    assert module_0.reverse_delete("aba", "") == ("aba", True)

    # All characters deleted, empty string is a palindrome
    assert module_0.reverse_delete("aabbcc", "abc") == ("", True)

    # Empty s and empty c
    assert module_0.reverse_delete("", "") == ("", True)

    # Case sensitivity check
    assert module_0.reverse_delete("aA", "a") == ("A", False)

    print("All test_reverse_delete tests passed!")


if __name__ == "__main__":
    test_reverse_delete()

# Generated at 2026-11-02 10:46:13.715464
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic case: delete vowels, result is not a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)

    # Deleting characters results in a palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # Delete all characters -> empty string is a palindrome
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # No characters to delete -> unchanged string, not a palindrome
    assert module_0.reverse_delete("abc", "xyz") == ("abc", False)

    # Deletion is case-sensitive
    assert module_0.reverse_delete("aA", "a") == ("A", True)

    # Empty source string
    assert module_0.reverse_delete("", "a") == ("", True)

    # Empty deletion set
    assert module_0.reverse_delete("abc", "") == ("abc", False)

    # Single character string is a palindrome
    assert module_0.reverse_delete("a", "b") == ("a", True)

    # Deleting repeated characters
    assert module_0.reverse_delete("aaabbbccc", "ab") == ("ccc", True)

    # Result is palindrome after deletions
    assert module_0.reverse_delete("abccba", "x") == ("abccba", True)

    print("All tests passed!")


if __name__ == "__main__":
    test_reverse_delete()