

# Generated at 2026-10-25 04:09:39.289924
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("a[b[c]d]e") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("") is False
    assert module_0.is_nested("abc") is False

    # Malformed bracket sequences
    assert module_0.is_nested("[[]") is False
    assert module_0.is_nested("[]]") is False
    assert module_0.is_nested("][") is False

# Generated at 2026-10-25 04:09:48.782110
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("") is False

# Generated at 2026-10-25 04:10:04.447945
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[][[]]") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("") is False

    assert module_0.is_nested("[[]") is False
    assert module_0.is_nested("[]]") is False
    assert module_0.is_nested("][[]") is False
    assert module_0.is_nested("[a]") is False

# Generated at 2026-10-25 04:10:06.866145
# Unit test for function is_nested

# Generated at 2026-10-25 04:10:09.288534
# Unit test for function is_nested

# Generated at 2026-10-25 04:10:11.700083
# Unit test for function is_nested

# Generated at 2026-10-25 04:10:14.115217
# Unit test for function is_nested

# Generated at 2026-10-25 04:10:16.530239
# Unit test for function is_nested

# Generated at 2026-10-25 04:10:18.947528
# Unit test for function is_nested