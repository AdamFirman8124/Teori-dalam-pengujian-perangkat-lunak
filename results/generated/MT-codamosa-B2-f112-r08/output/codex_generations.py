

# Generated at 2026-11-03 04:30:24.410482
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic deletion, result not a palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)

    # Multiple characters deleted, result not a palindrome
    assert module_0.reverse_delete("abcdef", "bce") == ("adf", False)

    # Delete 'd' and 'e', result not a palindrome
    assert module_0.reverse_delete("abcded", "de") == ("abc", False)

    # Delete 'a' and 'b', result is a palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # Delete most characters, result not a palindrome
    assert module_0.reverse_delete("abcdedcba", "abcd") == ("edc", False)

    # Delete all characters, empty string is a palindrome
    assert module_0.reverse_delete("abcdedcba", "abcdedcba") == ("", True)

    # Delete 'a' and 'e', result not a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)

    # Delete everything from a plain string, empty string is a palindrome
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # Delete characters not present in s, string unchanged
    assert module_0.reverse_delete("hello", "xyz") == ("hello", False)

    # Result is a palindrome after deletion
    assert module_0.reverse_delete("racecar", "e") == ("raccar", False)
    assert module_0.reverse_delete("abba", "c") == ("abba", True)

    # Empty source string
    assert module_0.reverse_delete("", "a") == ("", True)

    # Empty deletion set, string unchanged
    assert module_0.reverse_delete("abcba", "") == ("abcba", True)

    print("All tests passed!")


if __name__ == "__main__":
    test_reverse_delete()

# Generated at 2026-11-03 04:33:53.743686
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic deletion cases
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcd", "b") == ("acd", False)

    # Deleting everything results in an empty palindrome
    assert module_0.reverse_delete("aaaa", "a") == ("", True)
    assert module_0.reverse_delete("aabba", "ab") == ("", True)

    # Resulting string is a palindrome
    assert module_0.reverse_delete("abcba", "ab") == ("c", True)
    assert module_0.reverse_delete("abacaba", "b") == ("aacaa", True)

    # No characters removed
    assert module_0.reverse_delete("abc", "xyz") == ("abc", False)

    # Empty input string
    assert module_0.reverse_delete("", "abc") == ("", True)

    # Empty deletion set
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)

    print("All test_reverse_delete tests passed!")


if __name__ == "__main__":
    test_reverse_delete()

# Generated at 2026-11-03 04:37:11.600480
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic cases
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # Deleting all characters yields empty string, which is a palindrome
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # No characters deleted (empty c)
    assert module_0.reverse_delete("abc", "") == ("abc", False)
    assert module_0.reverse_delete("aba", "") == ("aba", True)

    # Empty string input
    assert module_0.reverse_delete("", "abc") == ("", True)
    assert module_0.reverse_delete("", "") == ("", True)

    # Case sensitivity
    assert module_0.reverse_delete("Aba", "a") == ("Ab", False)

    # Repeated characters in c
    assert module_0.reverse_delete("hello", "l") == ("heo", False)
    assert module_0.reverse_delete("racecar", "r") == ("aceca", True)

    print("test_reverse_delete passed")


test_reverse_delete()

# Generated at 2026-11-03 04:39:38.635059
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic deletion, not a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    # Single character deleted
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    # Deletion results in a palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    # Deleting repeated characters
    assert module_0.reverse_delete("aabbcc", "cc") == ("aabb", False)
    # Empty strings
    assert module_0.reverse_delete("", "") == ("", True)
    # No characters deleted, string is a palindrome
    assert module_0.reverse_delete("madam", "") == ("madam", True)
    # All characters deleted
    assert module_0.reverse_delete("abc", "abc") == ("", True)
    # Case sensitivity check
    assert module_0.reverse_delete("Abc", "a") == ("Abc", False)
    # Deleting all but one character (single char is palindrome)
    assert module_0.reverse_delete("abab", "ab") == ("", True)
    # Mixed deletion resulting in palindrome
    assert module_0.reverse_delete("racecar", "x") == ("racecar", True)

    print("All tests passed!")

if __name__ == "__main__":
    test_reverse_delete()