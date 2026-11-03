

# Generated at 2026-11-02 12:45:26.257269
# Unit test for function is_nested
def test_is_nested():
    # Simple non-nested pair
    assert module_0.is_nested('[]') == False
    # Single nesting level
    assert module_0.is_nested('[[]]') == True
    # Two separate (non-nested) pairs
    assert module_0.is_nested('[][]') == False
    # Deeply nested
    assert module_0.is_nested('[[][]]') == True
    assert module_0.is_nested('[[[[[]]]]]') == True
    # Unclosed nesting still counts as nested
    assert module_0.is_nested('[[]][[') == True
    assert module_0.is_nested('[[][][') == True
    # Closing brackets before opening brackets
    assert module_0.is_nested(']]][[[') == False
    # Closing brackets first, then openings
    assert module_0.is_nested('[]]]]]]][[[[[]') == False
    # Edge cases
    assert module_0.is_nested('') == False
    assert module_0.is_nested('[[[[[') == False
    assert module_0.is_nested(']]]]]') == False
    # Interleaved case that does not nest twice
    assert module_0.is_nested('[]][[]]') == False
    # Nested with extra closing brackets
    assert module_0.is_nested('[[]]]]') == True

# Generated at 2026-11-02 12:48:31.187547
# Unit test for function is_nested
def test_is_nested():
    # Basic cases from the specification
    assert module_0.is_nested('[[]]') == True          # single nesting
    assert module_0.is_nested('[]]]]]]][[[[[]') == False
    assert module_0.is_nested('[][]') == False         # no nesting, just sequential
    assert module_0.is_nested('[]') == False           # single pair, no nesting
    assert module_0.is_nested('[[][]]') == True        # nested inside
    assert module_0.is_nested('[[]][[') == True        # nested pair plus unmatched opens

    # Edge cases
    assert module_0.is_nested('') == False             # empty string
    assert module_0.is_nested('[[[') == False          # only opening brackets
    assert module_0.is_nested(']]]') == False          # only closing brackets
    assert module_0.is_nested('[[]') == False          # unmatched opening bracket
    assert module_0.is_nested('[]]') == False          # extra closing bracket
    assert module_0.is_nested('[') == False            # single open
    assert module_0.is_nested(']') == False            # single close

    # Deeper nesting
    assert module_0.is_nested('[[[]]]') == True        # triple nesting
    assert module_0.is_nested('[][[[]]]') == True      # sequential then nested
    assert module_0.is_nested('[[[[[]]]]]') == True    # deep nesting
    assert module_0.is_nested('[]][[]') == False       # two separate non-nested pairs

test_is_nested()
print("All tests passed!")