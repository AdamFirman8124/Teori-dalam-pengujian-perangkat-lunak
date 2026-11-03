

# Generated at 2026-11-02 07:37:22.136343
# Unit test for function all_prefixes
def test_all_prefixes():
    # nonce:51741567
    # Edge case: empty string should return an empty list
    assert module_0.all_prefixes("") == []

    # Single character string
    assert module_0.all_prefixes("a") == ["a"]

    # Typical case: two characters
    assert module_0.all_prefixes("ab") == ["a", "ab"]

    # Typical case: three characters
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # String with spaces
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]

    # String with special characters
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]

    # Result length matches string length
    assert len(module_0.all_prefixes("python")) == 6

    # Last prefix is always the full string
    for s in ["abc", "hello", "x"]:
        assert module_0.all_prefixes(s)[-1] == s

    # First prefix is always a single character (for non-empty strings)
    for s in ["abc", "hello", "x"]:
        assert module_0.all_prefixes(s)[0] == s[0]

    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-02 07:37:41.286173
# Unit test for function all_prefixes
def test_all_prefixes():
    # nonce:85a9eb3d
    # Test with a simple string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Test with a single character string
    assert module_0.all_prefixes("a") == ["a"]

    # Test with an empty string
    assert module_0.all_prefixes("") == []

    # Test with a longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # Test with a string containing spaces
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]

    # Test with numeric characters
    assert module_0.all_prefixes("123") == ["1", "12", "123"]

    # Verify result is a list
    assert isinstance(module_0.all_prefixes("xyz"), list)

    # Verify the last prefix equals the full string
    s = "python"
    assert module_0.all_prefixes(s)[-1] == s

    # Verify the number of prefixes equals string length
    assert len(module_0.all_prefixes("test")) == 4

    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-02 07:37:58.894368
# Unit test for function all_prefixes
def test_all_prefixes():
    # Test with a simple string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    
    # Test with single character
    assert module_0.all_prefixes("a") == ["a"]
    
    # Test with empty string
    assert module_0.all_prefixes("") == []
    
    # Test with longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    
    # Test with string containing spaces
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]
    
    # Test with special characters
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]
    
    # Test result is a list
    assert isinstance(module_0.all_prefixes("test"), list)
    
    # Test number of prefixes equals string length
    assert len(module_0.all_prefixes("python")) == 6
    
    # Test last prefix equals full string
    s = "complete"
    result = module_0.all_prefixes(s)
    assert result[-1] == s
    
    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-02 07:39:04.425106
# Unit test for function all_prefixes
def test_all_prefixes():
    # Test with a simple string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Test with a single character
    assert module_0.all_prefixes("a") == ["a"]

    # Test with an empty string
    assert module_0.all_prefixes("") == []

    # Test with a longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # Test with a string containing spaces
    assert module_0.all_prefixes("ab cd") == ["a", "ab", "ab ", "ab c", "ab cd"]

    # Test with numeric characters
    assert module_0.all_prefixes("123") == ["1", "12", "123"]

    # Test with special characters
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]

    # Test that result has correct length
    assert len(module_0.all_prefixes("python")) == 6

    # Test that the last prefix equals the full string
    s = "testing"
    result = module_0.all_prefixes(s)
    assert result[-1] == s

    # Test that prefixes are in increasing order of length
    assert all(len(result[i]) < len(result[i + 1]) for i in range(len(result) - 1))

# Generated at 2026-11-02 07:40:23.952113
# Unit test for function all_prefixes
def test_all_prefixes():
    # Basic case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    
    # Empty string should return an empty list
    assert module_0.all_prefixes("") == []
    
    # Single character
    assert module_0.all_prefixes("a") == ["a"]
    
    # Longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    
    # String containing spaces
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]
    
    # String with digits and symbols
    assert module_0.all_prefixes("x1!") == ["x", "x1", "x1!"]
    
    # Verify length and final prefix properties
    test_str = "testing"
    result = module_0.all_prefixes(test_str)
    assert len(result) == len(test_str)
    assert result[-1] == test_str
    assert result[0] == test_str[0]
    
    # Ensure order is progressive (each prefix grows by one char)
    for i in range(1, len(result)):
        assert result[i] == result[i - 1] + test_str[i]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()