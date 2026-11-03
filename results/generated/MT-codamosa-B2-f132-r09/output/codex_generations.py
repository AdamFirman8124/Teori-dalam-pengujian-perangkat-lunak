

# Generated at 2026-11-02 22:03:28.908399
# Unit test for function is_nested
def test_is_nested():
    # Nested brackets -> True
    assert module_0.is_nested('[[]]') == True
    assert module_0.is_nested('[[[]]]') == True
    assert module_0.is_nested('[[[[]]]]') == True
    assert module_0.is_nested('[]][[]]') == True
    assert module_0.is_nested('[][[]]') == True

    # Single pair or unmatched brackets -> False
    assert module_0.is_nested('[]') == False
    assert module_0.is_nested('[][]') == False
    assert module_0.is_nested('[]]]') == False
    assert module_0.is_nested('[[[]') == False
    assert module_0.is_nested('][') == False

    # Degenerate inputs -> False
    assert module_0.is_nested('[') == False
    assert module_0.is_nested(']') == False
    assert module_0.is_nested('') == False


test_is_nested()

# Generated at 2026-11-02 22:09:05.296701
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
    assert module_0.is_nested('[[][]]') == True
    assert module_0.is_nested('') == False
    assert module_0.is_nested('[[[[[[[[') == False
    assert module_0.is_nested(']]]]]]]]') == False
    assert module_0.is_nested('[[[]]]') == True
    assert module_0.is_nested('[[]][[]]') == True
    print("All test cases passed!")