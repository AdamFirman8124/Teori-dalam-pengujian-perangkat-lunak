

# Generated at 2026-10-25 02:12:14.005909
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[[][]]") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("") is False

    # Invalid/unbalanced strings
    assert module_0.is_nested("[[]") is False
    assert module_0.is_nested("[[]]]") is False
    assert module_0.is_nested("][[]") is False
    assert module_0.is_nested("[a]") is False

# Generated at 2026-10-25 02:12:29.326559
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[][]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[[]][") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("[") is False
    assert module_0.is_nested("]") is False
    assert module_0.is_nested("") is False
    assert module_0.is_nested("[[[[[[") is False
    assert module_0.is_nested("]]]]]]") is False
    assert module_0.is_nested("[]]]]]]][[[[[]") is False

# Generated at 2026-10-25 02:12:42.264686
# Unit test for function is_nested
def test_is_nested():assert module_0.is_nested("[[]]") is True

# Generated at 2026-10-25 02:12:54.654430
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[][[]]") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("") is False

    # Invalid bracket strings
    assert module_0.is_nested("][") is False
    assert module_0.is_nested("[[]") is False
    assert module_0.is_nested("[[]]]") is False

# Generated at 2026-10-25 02:13:11.003222
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[][[]]") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("") is False
    assert module_0.is_nested("[[") is False
    assert module_0.is_nested("]]") is False