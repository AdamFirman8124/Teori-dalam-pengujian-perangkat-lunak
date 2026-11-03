

# Generated at 2026-11-02 07:24:26.462208
# Unit test for function all_prefixes
def test_all_prefixes():
    # Empty string returns empty list
    assert module_0.all_prefixes("") == []

    # Single character string
    assert module_0.all_prefixes("a") == ["a"]

    # Two character string
    assert module_0.all_prefixes("ab") == ["a", "ab"]

    # Three character string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # String with spaces
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]

    # Result length equals input string length
    assert len(module_0.all_prefixes("test")) == 4

    # Last prefix equals the full string
    result = module_0.all_prefixes("prefix")
    assert result[-1] == "prefix"

    # Prefixes are ordered from shortest to longest
    lengths = [len(p) for p in module_0.all_prefixes("chain")]
    assert lengths == sorted(lengths)

# Generated at 2026-11-02 07:24:32.747189
# Unit test for function all_prefixes
def test_all_prefixes():
    # Test with a simple string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Test with single character
    assert module_0.all_prefixes("a") == ["a"]

    # Test with empty string
    assert module_0.all_prefixes("") == []

    # Test with a longer string containing repeated characters
    assert module_0.all_prefixes("aaa") == ["a", "aa", "aaa"]

    # Test with string containing spaces and special characters
    assert module_0.all_prefixes("a b!") == ["a", "a ", "a b", "a b!"]

    # Test with numbers in string
    assert module_0.all_prefixes("123") == ["1", "12", "123"]


# Run tests
if __name__ == "__main__":
    test_all_prefixes()
    print("All tests passed!")

# Generated at 2026-11-02 07:24:39.128928
# Unit test for function all_prefixes
def test_all_prefixes():
    # Empty string should return an empty list
    assert module_0.all_prefixes("") == []

    # Single character
    assert module_0.all_prefixes("a") == ["a"]

    # Two characters
    assert module_0.all_prefixes("ab") == ["a", "ab"]

    # Basic case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # String with spaces
    assert module_0.all_prefixes("ab c") == ["a", "ab", "ab ", "ab c"]

    # String with digits
    assert module_0.all_prefixes("123") == ["1", "12", "123"]

    # String with special characters
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]

    # Repeated characters
    assert module_0.all_prefixes("aaa") == ["a", "aa", "aaa"]

    # Verify order is shortest to longest
    result = module_0.all_prefixes("python")
    assert result == sorted(result, key=len)
    assert len(result) == len("python")

# Generated at 2026-11-02 07:24:55.428371
# Unit test for function all_prefixes
def test_all_prefixes():
    # Basic case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Empty string returns empty list
    assert module_0.all_prefixes("") == []

    # Single character
    assert module_0.all_prefixes("a") == ["a"]

    # Longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # String containing spaces (prefixes must include them)
    assert module_0.all_prefixes("ab cd") == ["a", "ab", "ab ", "ab c", "ab cd"]

    # Special characters
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]

    # Numeric characters
    assert module_0.all_prefixes("123") == ["1", "12", "123"]

    # Result length equals input string length
    assert len(module_0.all_prefixes("python")) == 6

    # Prefixes are ordered from shortest to longest
    result = module_0.all_prefixes("prefixes")
    lengths = [len(p) for p in result]
    assert lengths == sorted(lengths)

    # First prefix is the first char, last prefix is the full string
    for s in ["abc", "hello", "x"]:
        prefixes = module_0.all_prefixes(s)
        assert prefixes[0] == s[0]
        assert prefixes[-1] == s

    # Each prefix is a prefix of the next one
    prefixes = module_0.all_prefixes("chain")
    for i in range(len(prefixes) - 1):
        assert prefixes[i + 1].startswith(prefixes[i])

# Generated at 2026-11-02 07:24:59.737259
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes('') == []
    assert module_0.all_prefixes('a') == ['a']
    assert module_0.all_prefixes('ab') == ['a', 'ab']
    assert module_0.all_prefixes('abc') == ['a', 'ab', 'abc']
    assert module_0.all_prefixes('asdf') == ['a', 'as', 'asd', 'asdf']
    assert module_0.all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
    assert module_0.all_prefixes('xyz') == ['x', 'xy', 'xyz']
    assert module_0.all_prefixes(' ') == [' ']
    assert module_0.all_prefixes('a b') == ['a', 'a ', 'a b']
    assert module_0.all_prefixes('123') == ['1', '12', '123']


test_all_prefixes()
print("All tests passed!")