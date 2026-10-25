

# Generated at 2026-10-24 16:01:50.167052
# Unit test for function same_chars
def test_same_chars():
    # same characters, different order
    assert module_0.same_chars("abc", "cba")
    assert module_0.same_chars("hello", "olleh")

    # duplicates and order don't matter - only set matters
    assert module_0.same_chars("aabbcc", "abc")
    assert module_0.same_chars("abc", "aabbcc")
    assert module_0.same_chars("aaa", "a")

    # empty strings
    assert module_0.same_chars("", "")

    # different characters
    assert not module_0.same_chars("abc", "abd")
    assert not module_0.same_chars("abc", "abcd")
    assert not module_0.same_chars("abcd", "abc")
    assert not module_0.same_chars("", "a")
    assert not module_0.same_chars("a", "")

    # case-sensitive
    assert not module_0.same_chars("a", "A")
    assert not module_0.same_chars("Abc", "abc")

# Generated at 2026-10-24 16:02:16.178238
# Unit test for function same_chars
def test_same_chars():
    # same characters, different order
    assert module_0.same_chars("abc", "cba")
    assert module_0.same_chars("hello", "olleh")

    # duplicates and order don't matter - only set matters
    assert module_0.same_chars("aabbcc", "abc")
    assert module_0.same_chars("abc", "aabbcc")
    assert module_0.same_chars("aaa", "a")

    # empty strings
    assert module_0.same_chars("", "")

    # different characters
    assert not module_0.same_chars("abc", "abd")
    assert not module_0.same_chars("abc", "abcd")
    assert not module_0.same_chars("abcd", "abc")
    assert not module_0.same_chars("", "a")
    assert not module_0.same_chars("a", "")

    # case-sensitive
    assert not module_0.same_chars("a", "A")
    assert not module_0.same_chars("Abc", "abc")

# Generated at 2026-10-24 16:02:23.754054
# Unit test for function same_chars
def test_same_chars():
    # same characters, different order
    assert module_0.same_chars("abc", "cba")
    assert module_0.same_chars("hello", "olleh")

    # duplicates and order don't matter - only set matters
    assert module_0.same_chars("aabbcc", "abc")
    assert module_0.same_chars("abc", "aabbcc")
    assert module_0.same_chars("aaa", "a")

    # empty strings
    assert module_0.same_chars("", "")

    # different characters
    assert not module_0.same_chars("abc", "abd")
    assert not module_0.same_chars("abc", "abcd")
    assert not module_0.same_chars("abcd", "abc")
    assert not module_0.same_chars("", "a")
    assert not module_0.same_chars("a", "")

    # case-sensitive
    assert not module_0.same_chars("a", "A")
    assert not module_0.same_chars("Abc", "abc")

# Generated at 2026-10-24 16:02:26.840767
# Unit test for function same_chars
def test_same_chars():
    # same characters, different order
    assert module_0.same_chars("abc", "cba")
    assert module_0.same_chars("hello", "olleh")

    # duplicates and order don't matter - only set matters
    assert module_0.same_chars("aabbcc", "abc")
    assert module_0.same_chars("abc", "aabbcc")
    assert module_0.same_chars("aaa", "a")

    # empty strings
    assert module_0.same_chars("", "")

    # different characters
    assert not module_0.same_chars("abc", "abd")
    assert not module_0.same_chars("abc", "abcd")
    assert not module_0.same_chars("abcd", "abc")
    assert not module_0.same_chars("", "a")
    assert not module_0.same_chars("a", "")

    # case-sensitive
    assert not module_0.same_chars("a", "A")
    assert not module_0.same_chars("Abc", "abc")

# Generated at 2026-10-24 16:02:50.173461
# Unit test for function same_chars
def test_same_chars():
    # same characters, different order
    assert module_0.same_chars("abc", "cba")
    assert module_0.same_chars("hello", "olleh")

    # duplicates and order don't matter - only set matters
    assert module_0.same_chars("aabbcc", "abc")
    assert module_0.same_chars("abc", "aabbcc")
    assert module_0.same_chars("aaa", "a")

    # empty strings
    assert module_0.same_chars("", "")

    # different characters
    assert not module_0.same_chars("abc", "abd")
    assert not module_0.same_chars("abc", "abcd")
    assert not module_0.same_chars("abcd", "abc")
    assert not module_0.same_chars("", "a")
    assert not module_0.same_chars("a", "")

    # case-sensitive
    assert not module_0.same_chars("a", "A")
    assert not module_0.same_chars("Abc", "abc")