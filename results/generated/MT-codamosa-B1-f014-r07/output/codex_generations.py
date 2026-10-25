

# Generated at 2026-10-24 14:09:51.154573
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("") == []


if __name__ == "__main__":
    test_all_prefixes()
    print("All tests passed.")

# Generated at 2026-10-24 14:10:10.511368
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

# Generated at 2026-10-24 14:10:27.000627
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

# Generated at 2026-10-24 14:10:33.650867
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

# Generated at 2026-10-24 14:10:40.510862
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("") == []