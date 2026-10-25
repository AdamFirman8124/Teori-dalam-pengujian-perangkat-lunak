

# Generated at 2026-10-24 23:10:17.396835
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "") is False
    assert module_0.same_chars("abc", "ABC") is False  # Case-sensitive

# Generated at 2026-10-24 23:10:23.335775
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aab", "ba") is True
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "") is False
    assert module_0.same_chars("abc", "ABC") is False

# Generated at 2026-10-24 23:10:28.046358
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True

    assert module_0.same_chars("abc", "abcd") is False
    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "ABC") is False
    assert module_0.same_chars("", "a") is False

# Generated at 2026-10-24 23:10:31.937642
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cab") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True

    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "ab") is False
    assert module_0.same_chars("abc", "ABC") is False
    assert module_0.same_chars("", "a") is False

# Generated at 2026-10-24 23:10:36.340387
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "bca") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True

    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "") is False
    assert module_0.same_chars("abc", "ABC") is False