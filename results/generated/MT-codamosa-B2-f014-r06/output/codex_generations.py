

# Generated at 2026-11-03 05:13:55.640375
# Unit test for function all_prefixes
def test_all_prefixes():
    # Test with a simple string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    
    # Test with a single character
    assert module_0.all_prefixes("a") == ["a"]
    
    # Test with an empty string
    assert module_0.all_prefixes("") == []
    
    # Test with a string containing spaces and punctuation
    assert module_0.all_prefixes("hi!") == ["h", "hi", "hi!"]
    
    # Test with a longer string
    assert module_0.all_prefixes("abcd") == ["a", "ab", "abc", "abcd"]
    
    # Test that result length matches input string length
    string = "hello"
    result = module_0.all_prefixes(string)
    assert len(result) == len(string)
    
    # Test that the last prefix is the full string
    assert result[-1] == "hello"
    
    # Test that each prefix is one character longer than the previous
    for i in range(1, len(result)):
        assert len(result[i]) == len(result[i - 1]) + 1
    
    # Test with a string containing repeated characters
    assert module_0.all_prefixes("aab") == ["a", "aa", "aab"]
    
    # Test with numeric characters
    assert module_0.all_prefixes("123") == ["1", "12", "123"]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-03 05:16:53.932653
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("ab") == ["a", "ab"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("xyz") == ["x", "xy", "xyz"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("aAbB") == ["a", "aA", "aAb", "aAbB"]
    assert module_0.all_prefixes(" ") == [" "]
    assert module_0.all_prefixes("123") == ["1", "12", "123"]
# nonce:5ef45ac0

# Generated at 2026-11-03 05:19:54.536397
# Unit test for function all_prefixes
def test_all_prefixes():
    # Empty string has no prefixes
    assert module_0.all_prefixes("") == []

    # Single character string
    assert module_0.all_prefixes("a") == ["a"]

    # Multiple character strings
    assert module_0.all_prefixes("ab") == ["a", "ab"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # String with spaces and special characters
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]

    # Structural properties
    s = "python"
    prefixes = module_0.all_prefixes(s)
    assert len(prefixes) == len(s)
    for i, prefix in enumerate(prefixes):
        assert prefix == s[:i + 1]
        assert s.startswith(prefix)

    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-03 05:21:45.789654
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("ab") == ["a", "ab"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("xyz") == ["x", "xy", "xyz"]

    # Check result length matches string length
    s = "python"
    result = module_0.all_prefixes(s)
    assert len(result) == len(s)

    # Check each prefix is in order and correct
    for i, prefix in enumerate(result):
        assert prefix == s[:i + 1]

    # Check all prefixes end at the full string
    assert result[-1] == s

    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()