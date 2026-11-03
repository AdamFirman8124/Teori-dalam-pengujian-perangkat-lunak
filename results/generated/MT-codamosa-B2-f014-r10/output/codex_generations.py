

# Generated at 2026-11-02 11:56:59.515088
# Unit test for function all_prefixes
def test_all_prefixes():
    # nonce:d9964e12
    # Empty string -> no prefixes
    assert module_0.all_prefixes("") == []

    # Single character
    assert module_0.all_prefixes("a") == ["a"]

    # Typical case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # Repeated characters
    assert module_0.all_prefixes("aaa") == ["a", "aa", "aaa"]

    # Spaces and special characters
    assert module_0.all_prefixes("a b!") == ["a", "a ", "a b", "a b!"]

    # Structural checks: length, prefix property, last element
    s = "prefix"
    prefixes = module_0.all_prefixes(s)
    assert len(prefixes) == len(s)
    for i, p in enumerate(prefixes):
        assert p == s[:i+1]
        assert s.startswith(p)
    assert prefixes[-1] == s

    # Result is ordered from shortest to longest
    assert prefixes == sorted(prefixes, key=len)

    print("All tests passed!")


test_all_prefixes()

# Generated at 2026-11-02 11:59:22.901190
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
    assert module_0.all_prefixes("ab c") == ["a", "ab", "ab ", "ab c"]
    
    # Test with numeric characters
    assert module_0.all_prefixes("123") == ["1", "12", "123"]
    
    # Test that result length matches input length
    assert len(module_0.all_prefixes("python")) == 6
    
    # Test that last prefix equals the full string
    assert module_0.all_prefixes("test")[-1] == "test"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-02 12:01:09.557278
# Unit test for function all_prefixes
def test_all_prefixes():
    # Basic case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Single character
    assert module_0.all_prefixes("a") == ["a"]

    # Empty string
    assert module_0.all_prefixes("") == []

    # Longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # String with spaces
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]

    # Result count equals string length
    s = "prefix"
    result = module_0.all_prefixes(s)
    assert len(result) == len(s)

    # Last prefix is the full string
    assert result[-1] == s

    # Each prefix extends the previous one
    for i in range(1, len(result)):
        assert result[i] == result[i - 1] + s[i - 1]

    # Repeated characters
    assert module_0.all_prefixes("aaa") == ["a", "aa", "aaa"]

    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-02 12:04:11.207620
# Unit test for function all_prefixes

# Generated at 2026-11-02 12:05:48.907118
# Unit test for function all_prefixes

# Generated at 2026-11-02 12:06:17.511779
# Unit test for function all_prefixes