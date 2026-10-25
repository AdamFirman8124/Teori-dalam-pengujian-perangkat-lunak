

# Generated at 2026-10-25 00:45:14.968018
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[][]]") is True
    assert module_0.is_nested("[[[]]]") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("[][][]") is False
    assert module_0.is_nested("") is False

    # Unbalanced strings are not nested
    assert module_0.is_nested("[[]") is False
    assert module_0.is_nested("[[]]]") is False
    assert module_0.is_nested("][[]") is False

# Generated at 2026-10-25 00:45:24.480204
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
    assert module_0.is_nested("][[]") is False
    assert module_0.is_nested("[[]") is False

# Generated at 2026-10-25 00:45:34.224429
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[][]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[][[]]") is True

    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("") is False

# Generated at 2026-10-25 00:45:48.953780
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[][]]") is True
    assert module_0.is_nested("[[]][[") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("[]]") is False
    assert module_0.is_nested("") is False

# Generated at 2026-10-25 00:45:58.067976
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[][]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[[]][[") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("") is False
    assert module_0.is_nested("[]]]]]]][[[[[]") is False
    assert module_0.is_nested("]][[") is False