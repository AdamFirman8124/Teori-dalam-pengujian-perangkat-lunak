

# Generated at 2026-11-02 10:33:12.087733
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic case: filter strings by a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Prefix matches all strings
    assert module_0.filter_by_prefix(['apple', 'apply', 'applesauce'], 'app') == ['apple', 'apply', 'applesauce']

    # Prefix matches none
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Empty prefix matches everything
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Empty input list
    assert module_0.filter_by_prefix([], 'a') == []

    # Exact match prefix equal to full string
    assert module_0.filter_by_prefix(['abc', 'abcd', 'ab'], 'abc') == ['abc', 'abcd']

    # Case sensitivity check
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'a') == ['apple']

    # Prefix longer than some strings
    assert module_0.filter_by_prefix(['a', 'ab', 'abc'], 'abc') == ['abc']

    # Duplicates preserved
    assert module_0.filter_by_prefix(['dog', 'dog', 'cat'], 'dog') == ['dog', 'dog']

    # Order preserved
    assert module_0.filter_by_prefix(['x1', 'y1', 'x2'], 'x') == ['x1', 'x2']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 10:34:01.545423
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with a normal list and prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test with empty list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test with prefix matching nothing
    assert module_0.filter_by_prefix(['abc', 'bcd'], 'z') == []
    
    # Test with prefix matching entire string
    assert module_0.filter_by_prefix(['abc'], 'abc') == ['abc']
    
    # Test with empty strings in list
    assert module_0.filter_by_prefix(['', 'abc'], 'a') == ['abc']
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'A') == ['ABC']
    
    # Test with duplicate strings
    assert module_0.filter_by_prefix(['apple', 'apple', 'banana'], 'app') == ['apple', 'apple']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 10:35:03.511723
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with a non-empty list and matching prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test with a prefix that matches nothing
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Test with an empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with an empty prefix (should match all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd'], '') == ['abc', 'bcd']

    # Test where prefix equals full string
    assert module_0.filter_by_prefix(['abc', 'abcd'], 'abc') == ['abc', 'abcd']

    # Test with duplicate strings
    assert module_0.filter_by_prefix(['ab', 'ab', 'cd'], 'ab') == ['ab', 'ab']

    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'a') == ['apple']

    # Test preserving input order
    assert module_0.filter_by_prefix(['ax', 'ay', 'ab'], 'a') == ['ax', 'ay', 'ab']


if __name__ == "__main__":
    test_filter_by_prefix()
    print("All tests passed!")

# Generated at 2026-11-02 10:35:56.543348
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test with prefix matching all strings
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    
    # Test with no matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []
    
    # Test with empty list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test with exact match prefix
    assert module_0.filter_by_prefix(['abc', 'abcd'], 'abcd') == ['abcd']
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'A') == ['ABC']
    
    # Test with duplicate strings
    assert module_0.filter_by_prefix(['abc', 'abc', 'bcd'], 'abc') == ['abc', 'abc']
    
    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc'], 'abc') == ['abc']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 10:37:21.137642
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with a prefix that matches some strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test with a prefix that matches a single string
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    
    # Test with a prefix that matches nothing
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []
    
    # Test with an empty list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test with an empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test with an empty prefix and empty list
    assert module_0.filter_by_prefix([], '') == []
    
    # Test with a prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc', 'abcd'], 'abc') == ['abc', 'abcd']
    
    # Test exact match (string equals prefix)
    assert module_0.filter_by_prefix(['abc', 'abcd'], 'abc') == ['abc', 'abcd']
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple', 'APple'], 'A') == ['Apple', 'APple']
    
    # Test with duplicate strings
    assert module_0.filter_by_prefix(['abc', 'abc', 'bcd'], 'a') == ['abc', 'abc']
    
    # Test with multi-character prefix
    assert module_0.filter_by_prefix(['hello', 'help', 'world', 'hell'], 'hel') == ['hello', 'help', 'hell']
    
    # Test with special characters in prefix
    assert module_0.filter_by_prefix(['a-b', 'a_b', 'ab'], 'a-') == ['a-b']
    
    # Test with strings containing spaces
    assert module_0.filter_by_prefix(['hello world', 'hello there', 'hi'], 'hello ') == ['hello world', 'hello there']
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_filter_by_prefix()