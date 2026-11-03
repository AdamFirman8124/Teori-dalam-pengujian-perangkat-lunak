

# Generated at 2026-11-02 11:20:58.393879
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic cases
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    
    # Result becomes empty string (empty is a palindrome)
    assert module_0.reverse_delete("abc", "abc") == ("", True)
    assert module_0.reverse_delete("aabbcc", "abc") == ("", True)
    
    # No characters removed
    assert module_0.reverse_delete("abccba", "xyz") == ("abccba", True)
    assert module_0.reverse_delete("hello", "xyz") == ("hello", False)
    
    # Partial removal resulting in palindrome
    assert module_0.reverse_delete("abab", "a") == ("bb", True)
    assert module_0.reverse_delete("madam", "m") == ("ada", True)
    
    # Removing one character
    assert module_0.reverse_delete("hello", "l") == ("heo", False)
    assert module_0.reverse_delete("racecar", "r") == ("aceca", True)
    
    # Empty string input
    assert module_0.reverse_delete("", "a") == ("", True)
    assert module_0.reverse_delete("", "") == ("", True)
    
    # Empty character set
    assert module_0.reverse_delete("level", "") == ("level", True)
    
    # Case sensitivity
    assert module_0.reverse_delete("AaBb", "A") == ("aBb", False)
    
    # Repeated characters in c
    assert module_0.reverse_delete("abca", "aa") == ("bc", False)
    
    print("All tests passed!")

test_reverse_delete()

# Generated at 2026-11-02 11:23:22.925378
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic cases
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("abccba", "ab") == ("cc", True)

    # Result is a palindrome
    assert module_0.reverse_delete("abcdef", "bdf") == ("ace", True)

    # Deleting all characters results in empty string (a palindrome)
    assert module_0.reverse_delete("abcde", "abcde") == ("", True)

    # Empty string input
    assert module_0.reverse_delete("", "abc") == ("", True)

    # No characters deleted (c has no matching chars)
    assert module_0.reverse_delete("hello", "xyz") == ("hello", False)

    # Deleting one character makes it a palindrome
    assert module_0.reverse_delete("racecar", "x") == ("racecar", True)

    # Case sensitivity check
    assert module_0.reverse_delete("Aa", "a") == ("A", False)

    # Palindrome with repeated deletions
    assert module_0.reverse_delete("madamimadam", "m") == ("adaiada", True)

    print("All tests passed!")

test_reverse_delete()

# Generated at 2026-11-02 11:26:06.993856
# Unit test for function reverse_delete
def test_reverse_delete():
    # Characters deleted, result is a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)

    # No characters deleted
    assert module_0.reverse_delete("hello", "") == ("hello", False)
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)

    # All characters deleted
    assert module_0.reverse_delete("aaaa", "a") == ("", True)
    assert module_0.reverse_delete("abc", "abc") == ("", True)

    # Deletion results in palindrome
    assert module_0.reverse_delete("abccba", "x") == ("abccba", True)
    assert module_0.reverse_delete("abab", "a") == ("bb", True)

    # Case sensitivity check
    assert module_0.reverse_delete("Madam", "M") == ("adam", False)
    assert module_0.reverse_delete("Madam", "m") == ("Mada", False)

    # Empty input string
    assert module_0.reverse_delete("", "abc") == ("", True)

    # Repeated characters in c
    assert module_0.reverse_delete("banana", "an") == ("b", False)

    print("All tests passed!")


test_reverse_delete()

# Generated at 2026-11-02 11:29:08.851544
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic case: delete chars, result is not a palindrome
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    
    # Delete one char, result not a palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    
    # Result is a palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    
    # All chars deleted, empty string is a palindrome
    assert module_0.reverse_delete("abc", "abc") == ("", True)
    
    # No chars deleted (c has no matching chars)
    assert module_0.reverse_delete("hello", "xyz") == ("hello", False)
    
    # Empty c: string unchanged, palindrome check on original
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("hello", "") == ("hello", False)
    
    # Deleting chars results in a palindrome
    assert module_0.reverse_delete("abccba", "a") == ("bccb", True)
    assert module_0.reverse_delete("abaacdedcaba", "ab") == ("cdedc", True)
    
    # Single character result
    assert module_0.reverse_delete("aaa", "a") == ("", True)
    assert module_0.reverse_delete("aba", "b") == ("aa", True)
    
    # Case sensitivity check
    assert module_0.reverse_delete("AbA", "a") == ("AbA", False)
    
    # Duplicates in c should not affect the result
    assert module_0.reverse_delete("abcde", "aae") == ("bcd", False)
    
    # Numeric strings
    assert module_0.reverse_delete("12321", "1") == ("232", True)
    assert module_0.reverse_delete("12321", "2") == ("131", True)
    
    # String with special characters
    assert module_0.reverse_delete("a!b!c!", "!") == ("abc", False)
    
    # Both strings empty
    assert module_0.reverse_delete("", "") == ("", True)
    
    # s empty, c non-empty
    assert module_0.reverse_delete("", "abc") == ("", True)