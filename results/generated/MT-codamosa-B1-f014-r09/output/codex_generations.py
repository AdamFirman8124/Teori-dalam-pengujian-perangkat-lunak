

# Generated at 2026-10-24 14:39:25.303051
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:39:27.716344
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:39:30.129316
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:39:38.145105
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("") == []

# Generated at 2026-10-24 14:39:45.108118
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

# Generated at 2026-10-24 14:39:46.543913
# Unit test for function all_prefixes
def test_all_prefixes():
    # Empty string
    assert module_0.all_prefixes("") == []

    # Single character
    assert module_0.all_prefixes("a") == ["a"]

    # Typical case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # String with spaces
    assert module_0.all_prefixes("hi!") == ["h", "hi", "hi!"]

    # Longer string
    assert module_0.all_prefixes("abcd") == ["a", "ab", "abc", "abcd"]

    # Verify count matches length
    s = "hello"
    assert len(module_0.all_prefixes(s)) == len(s)

    # Verify each prefix is a prefix of the original
    for p in module_0.all_prefixes("world"):
        assert "world".startswith(p)

    print("All tests passed!")


test_all_prefixes()

# Generated at 2026-10-24 14:39:47.864925
# Unit test for function all_prefixes
def test_all_prefixes():
    # Empty string
    assert module_0.all_prefixes("") == []

    # Single character
    assert module_0.all_prefixes("a") == ["a"]

    # Typical case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # String with spaces
    assert module_0.all_prefixes("hi!") == ["h", "hi", "hi!"]

    # Longer string
    assert module_0.all_prefixes("abcd") == ["a", "ab", "abc", "abcd"]

    # Verify count matches length
    s = "hello"
    assert len(module_0.all_prefixes(s)) == len(s)

    # Verify each prefix is a prefix of the original
    for p in module_0.all_prefixes("world"):
        assert "world".startswith(p)

    print("All tests passed!")


test_all_prefixes()