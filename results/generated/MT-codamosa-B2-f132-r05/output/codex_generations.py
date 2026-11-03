

# Generated at 2026-11-02 17:28:13.833516
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested('[[]]') == True
    assert module_0.is_nested('[]]]]]]][[[[[]') == False
    assert module_0.is_nested('[][]') == False
    assert module_0.is_nested('[]') == False
    assert module_0.is_nested('[[[[]]]]') == True
    assert module_0.is_nested('[]]]]]]]]]]') == False
    assert module_0.is_nested('[][][[]]') == True
    assert module_0.is_nested('[[]') == False
    assert module_0.is_nested('[]]') == False
    assert module_0.is_nested('[[]][[') == True
    assert module_0.is_nested('[[') == False
    assert module_0.is_nested('') == False

# Generated at 2026-11-02 17:29:43.191713
# Unit test for function is_nested
def test_is_nested():
    # Nested brackets present
    assert module_0.is_nested('[[]]') == True
    assert module_0.is_nested('[[][]]') == True
    assert module_0.is_nested('[[]][[') == True

    # No nesting (only sequential/mismatched brackets)
    assert module_0.is_nested('[]') == False
    assert module_0.is_nested('[][]') == False
    assert module_0.is_nested('[][') == False
    assert module_0.is_nested('[]]]]]]][[[[[]') == False
    assert module_0.is_nested('[]][[]') == False

    # Only one kind of bracket
    assert module_0.is_nested('[[[') == False
    assert module_0.is_nested(']]]') == False

    # Empty string
    assert module_0.is_nested('') == False

test_is_nested()

# Generated at 2026-11-02 17:31:50.826583
# Unit test for function is_nested
def test_is_nested():
    # Simple non-nested cases
    assert module_0.is_nested('[]') == False
    assert module_0.is_nested('[]]') == False
    assert module_0.is_nested('[][]') == False
    assert module_0.is_nested('[]]]]]]][[[[[]') == False

    # Nested cases
    assert module_0.is_nested('[[]]') == True
    assert module_0.is_nested('[[[]]]') == True
    assert module_0.is_nested('[[][]]') == True
    assert module_0.is_nested('[[[[]]]]') == True
    assert module_0.is_nested('[[]][[') == True
    assert module_0.is_nested('[[]][][[]]') == True
    assert module_0.is_nested('[][[[]]]') == True

    # Unbalanced / degenerate cases
    assert module_0.is_nested('') == False
    assert module_0.is_nested('[') == False
    assert module_0.is_nested(']') == False
    assert module_0.is_nested('][') == False
    assert module_0.is_nested('[[[[]') == False
    assert module_0.is_nested(']]]][[[') == False

# Generated at 2026-11-02 17:34:56.902100
# Unit test for function is_nested
def test_is_nested():
    # Standard nested cases -> True
    assert module_0.is_nested("[[]]") is True
    assert module_0.is_nested("[[[[]]]]") is True
    assert module_0.is_nested("[[][]]") is True
    assert module_0.is_nested("[[[[[[]]]]]]") is True

    # Multiple pairs but no nesting -> True (count >= 2 matched pairs)
    assert module_0.is_nested("[][][[]]") is True
    assert module_0.is_nested("[[]][[") is True

    # Single pair only -> False
    assert module_0.is_nested("[]") is False
    assert module_0.is_nested("[[]") is False
    assert module_0.is_nested("[]]") is False

    # Flat / unbalanced sequences -> False
    assert module_0.is_nested("[][]") is False
    assert module_0.is_nested("[]]]]]]][[") is False
    assert module_0.is_nested("[]]]]]]]]]]") is False
    assert module_0.is_nested("][") is False
    assert module_0.is_nested("") is False

    print("All tests passed!")


test_is_nested()