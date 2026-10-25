

# Generated at 2026-10-24 07:05:30.689483
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True

    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("", "a") is False
    assert module_0.same_chars("abc", "ABC") is False

# Generated at 2026-10-24 07:05:35.401270
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True

    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "") is False
    assert module_0.same_chars("abc", "abcd") is False

# Generated at 2026-10-24 07:05:40.210309
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cab") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True

    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "") is False
    assert module_0.same_chars("abc", "ABC") is False  # Case-sensitive

# Generated at 2026-10-24 07:05:45.331954
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "") is False
    assert module_0.same_chars("A", "a") is False

# Generated at 2026-10-24 07:05:50.273911
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True

    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "ab") is False
    assert module_0.same_chars("abc", "ABC") is False
    assert module_0.same_chars("", "a") is False