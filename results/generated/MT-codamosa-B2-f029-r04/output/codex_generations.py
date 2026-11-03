

# Generated at 2026-11-02 08:02:42.984948
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test with no matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Test with an empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with an empty prefix (all strings should match)
    assert module_0.filter_by_prefix(['abc', 'bcd'], '') == ['abc', 'bcd']

    # Test with prefix matching entire string
    assert module_0.filter_by_prefix(['abc'], 'abc') == ['abc']

    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc', 'abcd'], 'abc') == ['abc', 'abcd']

    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']

    # Test with duplicate strings
    assert module_0.filter_by_prefix(['dog', 'dog', 'cat'], 'dog') == ['dog', 'dog']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 08:03:17.697942
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with multiple matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test with no matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []
    
    # Test with empty string list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test where prefix matches entire string
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple', 'APPLE'], 'a') == ['apple']
    
    # Test with single character strings
    assert module_0.filter_by_prefix(['a', 'b', 'ab'], 'a') == ['a', 'ab']
    
    # Test with duplicate strings
    assert module_0.filter_by_prefix(['abc', 'abc', 'xyz'], 'abc') == ['abc', 'abc']
    
    # Test with prefix longer than strings
    assert module_0.filter_by_prefix(['a', 'ab'], 'abc') == []
    
    # Test with special characters
    assert module_0.filter_by_prefix(['!test', '#tag', '!temp'], '!') == ['!test', '!temp']
    
    # Test order preservation
    result = module_0.filter_by_prefix(['banana', 'apple', 'avocado', 'cherry'], 'a')
    assert result == ['apple', 'avocado']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 08:03:39.191668
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with basic filtering
    assert module_0.filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap') == ['apple', 'apricot']
    
    # Test with no matches
    assert module_0.filter_by_prefix(['apple', 'banana', 'cherry'], 'z') == []
    
    # Test with empty list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['apple', 'banana', 'cherry'], '') == ['apple', 'banana', 'cherry']
    
    # Test where all strings match the prefix
    assert module_0.filter_by_prefix(['abc', 'abd', 'abe'], 'ab') == ['abc', 'abd', 'abe']
    
    # Test where prefix equals the full string
    assert module_0.filter_by_prefix(['apple', 'banana'], 'apple') == ['apple']
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple', 'APPLE'], 'app') == ['apple']
    
    # Test preserving original order
    assert module_0.filter_by_prefix(['cat', 'car', 'dog', 'cab'], 'ca') == ['cat', 'car', 'cab']
    
    # Test with single character prefix
    assert module_0.filter_by_prefix(['one', 'two', 'three'], 't') == ['two', 'three']
    
    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['a', 'ab', 'abc'], 'abc') == ['abc']
    
    # Test with duplicate strings
    assert module_0.filter_by_prefix(['dog', 'dog', 'cat'], 'dog') == ['dog', 'dog']
    
    # Test with strings containing special characters
    assert module_0.filter_by_prefix(['#hash', '@mention', '#tag'], '#') == ['#hash', '#tag']
    
    # Test with strings containing spaces
    assert module_0.filter_by_prefix(['hello world', 'hello there', 'goodbye'], 'hello ') == ['hello world', 'hello there']
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 08:04:14.626409
# Unit test for function filter_by_prefix
def test_filter_by_prefix():import unittest


class TestFilterByPrefix(unittest.TestCase):

    def test_filter_by_prefix(self):
        # Basic filtering
        result = module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        self.assertEqual(result, ['abc', 'array'])

        # Empty prefix returns all strings
        result = module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '')
        self.assertEqual(result, ['abc', 'bcd', 'cde'])

        # Prefix matches nothing
        result = module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z')
        self.assertEqual(result, [])

        # Empty input list
        result = module_0.filter_by_prefix([], 'a')
        self.assertEqual(result, [])

        # Exact match
        result = module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc')
        self.assertEqual(result, ['abc', 'abcd', 'abcde'])

        # Case sensitivity check
        result = module_0.filter_by_prefix(['Apple', 'apple'], 'a')
        self.assertEqual(result, ['apple'])


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 08:04:31.323281
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering with a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']

    # Prefix matches nothing
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Empty list input
    assert module_0.filter_by_prefix([], 'a') == []

    # Empty prefix returns all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Multi-character prefix
    assert module_0.filter_by_prefix(['apple', 'application', 'banana', 'app'], 'app') == ['apple', 'application', 'app']

    # Exact match only
    assert module_0.filter_by_prefix(['abc'], 'abc') == ['abc']

    # Case sensitivity check
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'a') == ['abc']
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'A') == ['ABC']

    # Prefix longer than string yields no match
    assert module_0.filter_by_prefix(['a', 'ab'], 'abc') == []

    # Duplicates preserved
    assert module_0.filter_by_prefix(['ab', 'ab', 'ba'], 'ab') == ['ab', 'ab']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()