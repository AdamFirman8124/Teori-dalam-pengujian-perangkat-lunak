

# Generated at 2026-11-03 04:08:15.260545
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("ab") == ["a", "ab"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("xyz") == ["x", "xy", "xyz"]
    assert module_0.all_prefixes("1") == ["1"]
    assert module_0.all_prefixes(" a") == [" ", " a"]
    assert module_0.all_prefixes("aa") == ["a", "aa"]

# Generated at 2026-11-03 04:09:46.396432
# Unit test for function all_prefixes
def test_all_prefixes():
    # nonce:6659828b

    # Test basic string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Test single character
    assert module_0.all_prefixes("a") == ["a"]

    # Test empty string
    assert module_0.all_prefixes("") == []

    # Test longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # Test string with spaces
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]

    # Test string with special characters
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]

    # Test string with digits
    assert module_0.all_prefixes("123") == ["1", "12", "123"]

    # Test result is a list
    assert isinstance(module_0.all_prefixes("test"), list)

    # Test result length matches input length
    test_string = "python"
    result = module_0.all_prefixes(test_string)
    assert len(result) == len(test_string)

    # Test last prefix is the full string
    assert result[-1] == test_string

    # Test each prefix matches expected slice
    for i, prefix in enumerate(result):
        assert len(prefix) == i + 1
        assert prefix == test_string[:i + 1]

    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-03 04:11:51.633348
# Unit test for function all_prefixes
def test_all_prefixes():
    # Test with a typical string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Test with empty string
    assert module_0.all_prefixes("") == []

    # Test with single character
    assert module_0.all_prefixes("a") == ["a"]

    # Test with string containing spaces
    assert module_0.all_prefixes("hi ") == ["h", "hi", "hi "]

    # Test with numeric-like string
    assert module_0.all_prefixes("123") == ["1", "12", "123"]

    # Test result length matches input length
    s = "hello"
    result = module_0.all_prefixes(s)
    assert len(result) == len(s)

    # Test last prefix equals the full string
    assert result[-1] == s

    # Test each element is a genuine prefix of the original
    for prefix in result:
        assert s.startswith(prefix)

    # Test prefixes are ordered by increasing length
    lengths = [len(p) for p in result]
    assert lengths == sorted(lengths)

    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-03 04:12:51.741455
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("ab") == ["a", "ab"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("xyz") == ["x", "xy", "xyz"]
    assert module_0.all_prefixes("aa") == ["a", "aa"]
    assert module_0.all_prefixes(" ") == [" "]
    assert module_0.all_prefixes("123") == ["1", "12", "123"]
    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-03 04:14:19.352890
# Unit test for function all_prefixes
def test_all_prefixes():assert module_0.all_prefixes("") == []