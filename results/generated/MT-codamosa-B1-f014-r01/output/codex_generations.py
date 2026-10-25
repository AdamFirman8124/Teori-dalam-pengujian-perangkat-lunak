

# Generated at 2026-10-24 23:14:59.101413
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

# Generated at 2026-10-24 23:15:02.996448
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

# Generated at 2026-10-24 23:15:06.975527
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("123") == ["1", "12", "123"]

# Generated at 2026-10-24 23:15:10.263152
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

# Generated at 2026-10-24 23:15:16.202585
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("abcd") == ["a", "ab", "abc", "abcd"]
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("") == []