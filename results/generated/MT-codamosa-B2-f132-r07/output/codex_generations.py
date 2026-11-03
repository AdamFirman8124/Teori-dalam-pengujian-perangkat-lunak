

# Generated at 2026-11-01 21:11:59.232068
# Unit test for function is_nested
def test_is_nested():
    # Nested brackets -> True
    assert module_0.is_nested('[[]]') == True
    assert module_0.is_nested('[[][]]') == True
    assert module_0.is_nested('[[]][[') == True
    assert module_0.is_nested('[[[[[[[]]]]]]]') == True

    # No nesting (only sequential pairs) -> False
    assert module_0.is_nested('[]') == False
    assert module_0.is_nested('[][]') == False
    assert module_0.is_nested('[]][[]') == False
    assert module_0.is_nested('[]]]]]]][[[[[]') == False

    # Unbalanced / degenerate cases -> False
    assert module_0.is_nested('') == False
    assert module_0.is_nested('[') == False
    assert module_0.is_nested(']') == False
    assert module_0.is_nested('[[[[[[[[[') == False
    assert module_0.is_nested(']]]]]]]]]') == False
    assert module_0.is_nested('][') == False
    assert module_0.is_nested('][') == False

    # More nesting checks
    assert module_0.is_nested('[][[[[]]]]') == True
    assert module_0.is_nested('[[]][[]]') == True
    assert module_0.is_nested('][[][') == False
    assert module_0.is_nested('[[]') == False
    assert module_0.is_nested('[]]') == False

# Generated at 2026-11-01 21:12:50.533602
# Unit test for function is_nested
def test_is_nested():
    # nonce:3482cb85
    assert module_0.is_nested('[[]]') == True          # simple nesting
    assert module_0.is_nested('[]]]]]]][[)[[') == False
    assert module_0.is_nested('[][]') == False         # no nesting
    assert module_0.is_nested('[]') == False           # single pair
    assert module_0.is_nested('[[][[]]]') == True
    assert module_0.is_nested('[]]]]]]]]]]') == False
    assert module_0.is_nested('[][][[]]') == True
    assert module_0.is_nested('[[') == False           # unmatched opening
    assert module_0.is_nested(']]') == False           # unmatched closing
    assert module_0.is_nested('[[][]]') == True
    assert module_0.is_nested('') == False             # empty string
    assert module_0.is_nested('[[[]]]') == True        # deep nesting
    assert module_0.is_nested('][') == False           # reversed order
    print("All test_is_nested tests passed!")


if __name__ == "__main__":
    test_is_nested()

# Generated at 2026-11-01 21:13:36.305035
# Unit test for function is_nested
def test_is_nested():
# nonce:ebd71698
    assert module_0.is_nested('[[]]') == True
    assert module_0.is_nested('[]]]]]]][[[[[]') == False
    assert module_0.is_nested('[][]') == False
    assert module_0.is_nested('[]') == False
    assert module_0.is_nested('[[][]]') == True
    assert module_0.is_nested('[[]][[') == True
    assert module_0.is_nested('[[[]]]') == True
    assert module_0.is_nested('') == False
    assert module_0.is_nested('][') == False
    assert module_0.is_nested('[[[[[') == False
    assert module_0.is_nested(']]]]]') == False
    assert module_0.is_nested('[][[[[]]]]') == True


if __name__ == "__main__":
    test_is_nested()
    print("All tests passed!")

# Generated at 2026-11-01 21:14:42.078068
# Unit test for function is_nested
def test_is_nested():
    # No nesting possible
    assert module_0.is_nested('') == False
    assert module_0.is_nested('[]') == False
    assert module_0.is_nested('[][]') == False
    assert module_0.is_nested('][') == False
    assert module_0.is_nested(']]]][[[' ) == False

    # Nested patterns
    assert module_0.is_nested('[[]]') == True
    assert module_0.is_nested('[[[]]]') == True
    assert module_0.is_nested('[[[[]]]]') == True
    assert module_0.is_nested('[]][[]]') == True

    # Non-bracket characters are treated like closers
    assert module_0.is_nested(' [] ') == False
    assert module_0.is_nested(' [ [] ] ') == True

    # Complex mixed cases
    assert module_0.is_nested('[]]]]]]][[[[[]') == False
    assert module_0.is_nested('[[[[]]]][[[]]]') == True


if __name__ == "__main__":
    test_is_nested()
    print("All tests passed!")

# Generated at 2026-11-01 21:16:32.543233
# Unit test for function is_nested

# Generated at 2026-11-01 21:17:07.163337
# Unit test for function is_nested
def test_is_nested():
    assert module_0.is_nested('[[]]') is True
    assert module_0.is_nested('[[][]]') is True
    assert module_0.is_nested('[[]][[') is True
    assert module_0.is_nested('[]') is False
    assert module_0.is_nested('[][]') is False
    assert module_0.is_nested('[]]]]]]][[[[[]') is False
    assert module_0.is_nested('') is False
    assert module_0.is_nested('[') is False
    assert module_0.is_nested(']') is False
    assert module_0.is_nested('][') is False
    assert module_0.is_nested('[[[[[]]]]]') is True
    assert module_0.is_nested('][' * 5) is False