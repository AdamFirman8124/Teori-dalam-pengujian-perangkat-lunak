

# Generated at 2026-10-25 04:38:10.505920
# Unit test for function is_nested

# Generated at 2026-10-25 04:38:12.909359
# Unit test for function is_nested

# Generated at 2026-10-25 04:38:15.324610
# Unit test for function is_nested

# Generated at 2026-10-25 04:38:17.841425
# Unit test for function is_nested

# Generated at 2026-10-25 04:38:20.255916
# Unit test for function is_nested

# Generated at 2026-10-25 04:38:22.670325
# Unit test for function is_nested

# Generated at 2026-10-25 04:38:25.188844
# Unit test for function is_nested

# Generated at 2026-10-25 04:38:27.603704
# Unit test for function is_nested

# Generated at 2026-10-25 04:38:32.079729
# Unit test for function is_nested
def test_is_nested():assert module_0.is_nested("[[]]") is True

# Generated at 2026-10-25 04:38:44.366425
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[[][]]") is True

    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("") is False
    assert module_0.is_nested("[") is False
    assert module_0.is_nested("]") is False

# Generated at 2026-10-25 04:38:59.111967
# Unit test for function is_nested
def test_is_nested():
    # Nested brackets
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[]]]") is True
    assert module_0.is_nested("[][[]]") is True
    assert module_0.is_nested("[[][]]") is True

    # Not nested
    assert module_0.is_nested("") is False
    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("[][][]") is False

    # Unbalanced strings
    assert module_0.is_nested("[") is False
    assert module_0.is_nested("]") is False
    assert module_0.is_nested("[[]") is False
    assert module_0.is_nested("[]]") is False