

# Generated at 2026-10-25 01:53:59.955899
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") is True
    # Same characters, different order
    assert module_0.same_chars("abc", "cba") is True
    # Duplicates don't matter
    assert module_0.same_chars("aabbcc", "abc") is True
    # Different characters
    assert module_0.same_chars("abc", "abd") is False
    # Different lengths, same char set
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    # Subset is not equal
    assert module_0.same_chars("abcd", "dddddddabc") is False
    # Empty vs non-empty
    assert module_0.same_chars("", "a") is False
    # Both empty
    assert module_0.same_chars("", "") is True
    # Case sensitivity
    assert module_0.same_chars("ABC", "abc") is False
    # Special characters and spaces count
    assert module_0.same_chars("a b!", "b! a") is True
    assert module_0.same_chars("a b", "ab") is False


if __name__ == "__main__":
    test_same_chars()
    print("All tests passed.")

# Generated at 2026-10-25 01:54:01.375884
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") is True
    # Same characters, different order
    assert module_0.same_chars("abc", "cba") is True
    # Duplicates don't matter
    assert module_0.same_chars("aabbcc", "abc") is True
    # Different characters
    assert module_0.same_chars("abc", "abd") is False
    # Different lengths, same char set
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    # Subset is not equal
    assert module_0.same_chars("abcd", "dddddddabc") is False
    # Empty vs non-empty
    assert module_0.same_chars("", "a") is False
    # Both empty
    assert module_0.same_chars("", "") is True
    # Case sensitivity
    assert module_0.same_chars("ABC", "abc") is False
    # Special characters and spaces count
    assert module_0.same_chars("a b!", "b! a") is True
    assert module_0.same_chars("a b", "ab") is False


if __name__ == "__main__":
    test_same_chars()
    print("All tests passed.")

# Generated at 2026-10-25 01:54:02.717456
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") is True
    # Same characters, different order
    assert module_0.same_chars("abc", "cba") is True
    # Duplicates don't matter
    assert module_0.same_chars("aabbcc", "abc") is True
    # Different characters
    assert module_0.same_chars("abc", "abd") is False
    # Different lengths, same char set
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    # Subset is not equal
    assert module_0.same_chars("abcd", "dddddddabc") is False
    # Empty vs non-empty
    assert module_0.same_chars("", "a") is False
    # Both empty
    assert module_0.same_chars("", "") is True
    # Case sensitivity
    assert module_0.same_chars("ABC", "abc") is False
    # Special characters and spaces count
    assert module_0.same_chars("a b!", "b! a") is True
    assert module_0.same_chars("a b", "ab") is False


if __name__ == "__main__":
    test_same_chars()
    print("All tests passed.")

# Generated at 2026-10-25 01:54:04.044790
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") is True
    # Same characters, different order
    assert module_0.same_chars("abc", "cba") is True
    # Duplicates don't matter
    assert module_0.same_chars("aabbcc", "abc") is True
    # Different characters
    assert module_0.same_chars("abc", "abd") is False
    # Different lengths, same char set
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    # Subset is not equal
    assert module_0.same_chars("abcd", "dddddddabc") is False
    # Empty vs non-empty
    assert module_0.same_chars("", "a") is False
    # Both empty
    assert module_0.same_chars("", "") is True
    # Case sensitivity
    assert module_0.same_chars("ABC", "abc") is False
    # Special characters and spaces count
    assert module_0.same_chars("a b!", "b! a") is True
    assert module_0.same_chars("a b", "ab") is False


if __name__ == "__main__":
    test_same_chars()
    print("All tests passed.")

# Generated at 2026-10-25 01:54:05.484603
# Unit test for function same_chars
def test_same_chars():
    # Identical strings
    assert module_0.same_chars("abc", "abc") is True
    # Same characters, different order
    assert module_0.same_chars("abc", "cba") is True
    # Duplicates don't matter
    assert module_0.same_chars("aabbcc", "abc") is True
    # Different characters
    assert module_0.same_chars("abc", "abd") is False
    # Different lengths, same char set
    assert module_0.same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    # Subset is not equal
    assert module_0.same_chars("abcd", "dddddddabc") is False
    # Empty vs non-empty
    assert module_0.same_chars("", "a") is False
    # Both empty
    assert module_0.same_chars("", "") is True
    # Case sensitivity
    assert module_0.same_chars("ABC", "abc") is False
    # Special characters and spaces count
    assert module_0.same_chars("a b!", "b! a") is True
    assert module_0.same_chars("a b", "ab") is False


if __name__ == "__main__":
    test_same_chars()
    print("All tests passed.")