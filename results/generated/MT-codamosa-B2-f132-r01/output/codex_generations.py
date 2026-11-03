

# Generated at 2026-11-02 14:28:37.396761
# Unit test for function is_nested

# Generated at 2026-11-02 14:32:13.468127
# Unit test for function is_nested
def test_is_nested():
    # Nested: '[[]]' has two matched pairs
    assert module_0.is_nested('[[]]') is True
    # Deeply nested
    assert module_0.is_nested('[[[]]]') is True
    # Unclosed extra opening still yields two valid pairs
    assert module_0.is_nested('[[[]]') is True
    # Single pair only -> False
    assert module_0.is_nested('[]') is False
    # Sequential (non-nested) pairs -> False
    assert module_0.is_nested('[][]') is False
    # Empty string -> False
    assert module_0.is_nested('') is False
    # Only opening brackets -> False
    assert module_0.is_nested('[[[') is False
    # Only closing brackets -> False
    assert module_0.is_nested(']]]') is False
    # Closing before opening, only one valid pair -> False
    assert module_0.is_nested('][[]') is False