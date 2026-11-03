

# Generated at 2026-11-02 21:39:33.759495
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("hello", "hello") is True
    
    # Same characters, different order
    assert module_0.same_chars("listen", "silent") is True
    assert module_0.same_chars("abc", "cba") is True
    
    # Repeated characters still compare as sets
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("aaa", "a") is True
    
    # Different characters
    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("hello", "world") is False
    
    # One is subset of the other
    assert module_0.same_chars("abc", "ab") is False
    assert module_0.same_chars("ab", "abc") is False
    
    # Empty strings
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("", "a") is False
    assert module_0.same_chars("a", "") is False
    
    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") is False
    assert module_0.same_chars("aA", "Aa") is True
    
    # Single characters
    assert module_0.same_chars("x", "x") is True
    assert module_0.same_chars("x", "y") is False
    
    # Strings with spaces and special characters
    assert module_0.same_chars("a b!", "b! a") is True
    assert module_0.same_chars("a b", "ab") is False
    
    # Unicode characters
    assert module_0.same_chars("héllo", "olléh") is True
    assert module_0.same_chars("héllo", "hello") is False
    
    # Numbers as strings
    assert module_0.same_chars("123", "321") is True
    assert module_0.same_chars("123", "1234") is False

# Generated at 2026-11-02 21:40:54.143618
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("hello", "hello") == True

    # Same characters, different order
    assert module_0.same_chars("abc", "cba") == True

    # Same characters with duplicates
    assert module_0.same_chars("aabbcc", "abc") == True
    assert module_0.same_chars("abc", "aabbcc") == True

    # Different characters
    assert module_0.same_chars("abc", "abd") == False
    assert module_0.same_chars("hello", "world") == False

    # One is subset of the other
    assert module_0.same_chars("abc", "abcd") == False
    assert module_0.same_chars("abcd", "abc") == False

    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    assert module_0.same_chars("a", "") == False

    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") == False
    assert module_0.same_chars("aA", "Aa") == True

    # Single characters
    assert module_0.same_chars("a", "a") == True
    assert module_0.same_chars("a", "b") == False

    # Special characters and digits
    assert module_0.same_chars("a1!", "!1a") == True
    assert module_0.same_chars("a b", "b a") == True
    assert module_0.same_chars("a b", "ab") == False

    # Unicode characters
    assert module_0.same_chars("héllo", "olléh") == True
    assert module_0.same_chars("héllo", "hello") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_same_chars()

# Generated at 2026-11-02 21:42:03.611491
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") is True
    # Same characters, different order
    assert module_0.same_chars("abc", "cba") is True
    # Same characters with duplicates
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("abc", "aabbcc") is True
    # Different characters
    assert module_0.same_chars("abc", "abd") is False
    # One empty string
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("", "a") is False
    assert module_0.same_chars("a", "") is False
    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") is False
    # Special characters and digits
    assert module_0.same_chars("a1!", "1!a") is True
    assert module_0.same_chars("a1!", "a1?") is False
    # Single characters
    assert module_0.same_chars("x", "x") is True
    assert module_0.same_chars("x", "y") is False
    # Subset is not equal
    assert module_0.same_chars("abc", "ab") is False

# Generated at 2026-11-02 21:43:24.732029
# Unit test for function same_chars
def test_same_chars():
    # Classic cases: same set of chars despite different counts/order
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True
    assert module_0.same_chars("abcd", "dddddddabc") == True

    # Different sets of characters
    assert module_0.same_chars("abcd", "dddddddabcf") == False
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddddabc") == False
    assert module_0.same_chars("abcd", "abcde") == False

    # Identical strings
    assert module_0.same_chars("abc", "abc") == True

    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    assert module_0.same_chars("a", "") == False

    # Duplicates are ignored
    assert module_0.same_chars("aabbcc", "abc") == True
    assert module_0.same_chars("aaa", "a") == True

    # Single characters
    assert module_0.same_chars("x", "x") == True
    assert module_0.same_chars("x", "y") == False

    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") == False

    # Special characters and whitespace
    assert module_0.same_chars("a b!", "!ba ") == True

    # Unicode characters
    assert module_0.same_chars("héllo", "olléh") == True
    assert module_0.same_chars("héllo", "hello") == False

    print("All test_same_chars tests passed!")


if __name__ == "__main__":
    test_same_chars()

# Generated at 2026-11-02 21:45:27.759928
# Unit test for function same_chars
def test_same_chars():
    # Same set of characters, different order
    assert module_0.same_chars("abc", "cba") == True
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True
    assert module_0.same_chars("abcd", "dddddddabc") == True
    assert module_0.same_chars("abcd", "dddddddabce") == False
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddddabc") == False

    # Identical strings
    assert module_0.same_chars("hello", "hello") == True

    # Repeated characters still compare by unique set
    assert module_0.same_chars("aabbcc", "abc") == True
    assert module_0.same_chars("aabbcc", "ab") == False

    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    assert module_0.same_chars("a", "") == False

    # Single characters
    assert module_0.same_chars("a", "a") == True
    assert module_0.same_chars("a", "b") == False

    # Case sensitivity
    assert module_0.same_chars("abc", "ABC") == False
    assert module_0.same_chars("aA", "Aa") == True

    # Strings with spaces and special characters
    assert module_0.same_chars("a b!", "b! a") == True
    assert module_0.same_chars("a b", "ab") == False

    # Unicode characters
    assert module_0.same_chars("héllo", "olléh") == True
    assert module_0.same_chars("héllo", "hello") == False

    print("All test_same_chars tests passed!")


if __name__ == "__main__":
    test_same_chars()