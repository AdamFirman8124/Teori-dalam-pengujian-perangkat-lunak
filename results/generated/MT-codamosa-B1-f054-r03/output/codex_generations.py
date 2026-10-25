

# Generated at 2026-10-24 13:30:05.531074
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") == True
    # Same chars, different order
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True
    # Same chars, different counts
    assert module_0.same_chars("abcd", "dddddddabc") == True
    # One extra unique char
    assert module_0.same_chars("eabcd", "dddddddabc") == False
    # Single characters
    assert module_0.same_chars("a", "a") == True
    assert module_0.same_chars("a", "b") == False
    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    # With spaces and punctuation
    assert module_0.same_chars("a b!", "b! a") == True
    assert module_0.same_chars("a b", "a") == False
    # Case sensitivity: 'A' != 'a'
    assert module_0.same_chars("ABC", "abc") == False
    print("All tests passed!")

# Generated at 2026-10-24 13:30:06.963978
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") == True
    # Same chars, different order
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True
    # Same chars, different counts
    assert module_0.same_chars("abcd", "dddddddabc") == True
    # One extra unique char
    assert module_0.same_chars("eabcd", "dddddddabc") == False
    # Single characters
    assert module_0.same_chars("a", "a") == True
    assert module_0.same_chars("a", "b") == False
    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    # With spaces and punctuation
    assert module_0.same_chars("a b!", "b! a") == True
    assert module_0.same_chars("a b", "a") == False
    # Case sensitivity: 'A' != 'a'
    assert module_0.same_chars("ABC", "abc") == False
    print("All tests passed!")

# Generated at 2026-10-24 13:30:08.398266
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") == True
    # Same chars, different order
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True
    # Same chars, different counts
    assert module_0.same_chars("abcd", "dddddddabc") == True
    # One extra unique char
    assert module_0.same_chars("eabcd", "dddddddabc") == False
    # Single characters
    assert module_0.same_chars("a", "a") == True
    assert module_0.same_chars("a", "b") == False
    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    # With spaces and punctuation
    assert module_0.same_chars("a b!", "b! a") == True
    assert module_0.same_chars("a b", "a") == False
    # Case sensitivity: 'A' != 'a'
    assert module_0.same_chars("ABC", "abc") == False
    print("All tests passed!")

# Generated at 2026-10-24 13:30:09.719573
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") == True
    # Same chars, different order
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True
    # Same chars, different counts
    assert module_0.same_chars("abcd", "dddddddabc") == True
    # One extra unique char
    assert module_0.same_chars("eabcd", "dddddddabc") == False
    # Single characters
    assert module_0.same_chars("a", "a") == True
    assert module_0.same_chars("a", "b") == False
    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    # With spaces and punctuation
    assert module_0.same_chars("a b!", "b! a") == True
    assert module_0.same_chars("a b", "a") == False
    # Case sensitivity: 'A' != 'a'
    assert module_0.same_chars("ABC", "abc") == False
    print("All tests passed!")

# Generated at 2026-10-24 13:30:11.060049
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") == True
    # Same chars, different order
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") == True
    # Same chars, different counts
    assert module_0.same_chars("abcd", "dddddddabc") == True
    # One extra unique char
    assert module_0.same_chars("eabcd", "dddddddabc") == False
    # Single characters
    assert module_0.same_chars("a", "a") == True
    assert module_0.same_chars("a", "b") == False
    # Empty strings
    assert module_0.same_chars("", "") == True
    assert module_0.same_chars("", "a") == False
    # With spaces and punctuation
    assert module_0.same_chars("a b!", "b! a") == True
    assert module_0.same_chars("a b", "a") == False
    # Case sensitivity: 'A' != 'a'
    assert module_0.same_chars("ABC", "abc") == False
    print("All tests passed!")