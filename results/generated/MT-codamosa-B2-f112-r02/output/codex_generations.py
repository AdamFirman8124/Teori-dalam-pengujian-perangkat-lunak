

# Generated at 2026-11-02 18:28:48.399122
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic case: delete chars, result is not a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    
    # Delete one char, result is not a palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    
    # Result after deletion is a palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    
    # All characters deleted -> empty string is a palindrome
    assert module_0.reverse_delete("abc", "abc") == ("", True)
    
    # No characters to delete, string is not a palindrome
    assert module_0.reverse_delete("abc", "xyz") == ("abc", False)
    
    # No characters to delete, string is already a palindrome
    assert module_0.reverse_delete("abccba", "xyz") == ("abccba", True)
    
    # Empty input string
    assert module_0.reverse_delete("", "abc") == ("", True)
    
    # Empty character set, string unchanged and not a palindrome
    assert module_0.reverse_delete("hello", "") == ("hello", False)
    
    # Deleting repeated characters
    assert module_0.reverse_delete("aaabbb", "b") == ("aaa", True)
    
    # Case sensitivity check
    assert module_0.reverse_delete("aA", "a") == ("A", True)

test_reverse_delete()
print("All tests passed!")

# Generated at 2026-11-02 18:31:34.000960
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic cases
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    
    # Result is a palindrome after deletion
    assert module_0.reverse_delete("abccba", "ab") == ("cc", True)
    assert module_0.reverse_delete("hello", "l") == ("heo", False)
    assert module_0.reverse_delete("abab", "a") == ("bb", True)
    
    # Deleting all characters
    assert module_0.reverse_delete("aaaa", "a") == ("", True)
    assert module_0.reverse_delete("abc", "abc") == ("", True)
    
    # No characters deleted
    assert module_0.reverse_delete("abc", "xyz") == ("abc", False)
    assert module_0.reverse_delete("aba", "xyz") == ("aba", True)
    
    # Empty string input
    assert module_0.reverse_delete("", "abc") == ("", True)
    
    # Empty character set
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    
    # Single character cases
    assert module_0.reverse_delete("a", "a") == ("", True)
    assert module_0.reverse_delete("a", "b") == ("a", True)
    
    # Repeated characters in c
    assert module_0.reverse_delete("mississippi", "sis") == ("mippi", False)
    
    print("All tests passed!")

test_reverse_delete()

# Generated at 2026-11-02 18:33:59.627791
# Unit test for function reverse_delete
def test_reverse_delete():
    # Test basic deletion, result not palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    # Test deletion, result not palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    # Test deletion, result is palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    # Test deleting all characters -> empty string is palindrome
    assert module_0.reverse_delete("ab", "ab") == ("", True)
    # Test empty deletion set -> string unchanged
    assert module_0.reverse_delete("abc", "") == ("abc", False)
    # Test single character not deleted -> palindrome
    assert module_0.reverse_delete("a", "b") == ("a", True)
    # Test single character deleted -> empty palindrome
    assert module_0.reverse_delete("a", "a") == ("", True)
    # Test no characters match deletion set
    assert module_0.reverse_delete("hello", "xyz") == ("hello", False)
    # Test already palindrome with no deletions
    assert module_0.reverse_delete("abccba", "x") == ("abccba", True)
    # Test empty input string
    assert module_0.reverse_delete("", "a") == ("", True)
    # Test case sensitivity
    assert module_0.reverse_delete("Aa", "a") == ("A", True)
    # Test repeated characters in deletion set
    assert module_0.reverse_delete("banana", "an") == ("b", False)
    # Test palindrome formed after deletion
    assert module_0.reverse_delete("abacaba", "x") == ("abacaba", True)
    assert module_0.reverse_delete("racecar", "e") == ("raccar", False)

# Generated at 2026-11-02 18:36:01.595242
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic case: delete chars, result is not a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)

    # Result is a palindrome after deletion
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # All characters deleted -> empty string is a palindrome
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # No characters deleted
    assert module_0.reverse_delete("abc", "xyz") == ("abc", False)

    # Single character not deleted
    assert module_0.reverse_delete("a", "b") == ("a", True)

    # Single character deleted
    assert module_0.reverse_delete("a", "a") == ("", True)

    # Empty input string
    assert module_0.reverse_delete("", "abc") == ("", True)

    # Empty deletion string (nothing removed)
    assert module_0.reverse_delete("aba", "") == ("aba", True)

    # Case sensitivity: 'A' is not removed when 'a' is in c
    assert module_0.reverse_delete("Aba", "a") == ("Ab", False)

    # Repeated characters
    assert module_0.reverse_delete("mississippi", "is") == ("mpp", False)

    # Result palindrome with even length
    assert module_0.reverse_delete("abccba", "b") == ("acca", True)

    print("All tests passed!")


if __name__ == "__main__":
    test_reverse_delete()