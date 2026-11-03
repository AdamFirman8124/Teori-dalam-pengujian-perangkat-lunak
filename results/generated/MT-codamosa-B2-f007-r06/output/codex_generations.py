

# Generated at 2026-11-02 23:05:19.197466
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test basic filtering with matches
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

    # Test filtering with a multi-character substring
    assert module_0.filter_by_substring(['hello', 'world', 'help', 'shell'], 'hel') == ['hello', 'help', 'shell']

    # Test no matches
    assert module_0.filter_by_substring(['abc', 'def'], 'xyz') == []

    # Test empty input list
    assert module_0.filter_by_substring([], 'a') == []

    # Test empty substring (matches everything)
    assert module_0.filter_by_substring(['a', 'b', 'c'], '') == ['a', 'b', 'c']

    # Test substring equal to full string
    assert module_0.filter_by_substring(['abc'], 'abc') == ['abc']

    # Test case sensitivity
    assert module_0.filter_by_substring(['ABC', 'abc'], 'abc') == ['abc']

    # Test duplicate strings
    assert module_0.filter_by_substring(['aa', 'aa', 'ab'], 'aa') == ['aa', 'aa']

    # Test substring at start and end
    assert module_0.filter_by_substring(['prefix_suffix', 'suffix', 'prefix'], 'fix') == ['prefix_suffix', 'suffix', 'prefix']

    # Test with numbers as strings
    assert module_0.filter_by_substring(['123', '456', '124'], '12') == ['123', '124']

# Generated at 2026-11-02 23:07:27.405553
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with multiple matches
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    
    # Test with no matches
    assert module_0.filter_by_substring(['abc', 'def', 'ghi'], 'xyz') == []
    
    # Test with empty input list
    assert module_0.filter_by_substring([], 'a') == []
    
    # Test with empty substring (should match all strings)
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']
    
    # Test with substring matching all elements
    assert module_0.filter_by_substring(['hello', 'hell', 'helium'], 'hel') == ['hello', 'hell', 'helium']
    
    # Test case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']
    
    # Test with substring equal to full string
    assert module_0.filter_by_substring(['test'], 'test') == ['test']
    
    # Test with single character substring
    assert module_0.filter_by_substring(['cat', 'dog', 'bird'], 'o') == ['dog']
    
    # Test preserving order of elements
    assert module_0.filter_by_substring(['xyzabc', 'abcxyz', 'abc'], 'abc') == ['xyzabc', 'abcxyz', 'abc']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-02 23:10:12.273694
# Unit test for function filter_by_substring
def test_filter_by_substring():import unittest


class TestFilterBySubstring(unittest.TestCase):

    def test_basic_filter(self):
        self.assertEqual(module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_no_matches(self):
        self.assertEqual(module_0.filter_by_substring(['abc', 'def', 'ghi'], 'xyz'), [])

    def test_all_matches(self):
        self.assertEqual(module_0.filter_by_substring(['aaa', 'aaaa', 'aa'], 'a'), ['aaa', 'aaaa', 'aa'])

    def test_empty_list(self):
        self.assertEqual(module_0.filter_by_substring([], 'a'), [])

    def test_empty_substring(self):
        self.assertEqual(module_0.filter_by_substring(['abc', 'def'], ''), ['abc', 'def'])

    def test_case_sensitivity(self):
        self.assertEqual(module_0.filter_by_substring(['ABC', 'abc', 'Abc'], 'abc'), ['abc'])

    def test_substring_at_edges(self):
        self.assertEqual(module_0.filter_by_substring(['prefix_x', 'x_suffix', 'middle'], 'x_'), ['prefix_x', 'x_suffix'])

    def test_single_character_substring(self):
        self.assertEqual(module_0.filter_by_substring(['hello', 'world'], 'o'), ['hello', 'world'])

    def test_substring_longer_than_strings(self):
        self.assertEqual(module_0.filter_by_substring(['a', 'ab'], 'abc'), [])

    def test_result_preserves_order(self):
        self.assertEqual(module_0.filter_by_substring(['a1', 'b1', 'a2', 'c1', 'a3'], 'a'), ['a1', 'a2', 'a3'])


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 23:12:33.991436
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test case 1: Basic filtering - substring present in some strings
    assert module_0.filter_by_substring(['apple', 'banana', 'cherry'], 'an') == ['banana']

    # Test case 2: Substring present in multiple strings
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'abcde'], 'bc') == ['abc', 'abcde']

    # Test case 3: Empty input list
    assert module_0.filter_by_substring([], 'a') == []

    # Test case 4: No matches found
    assert module_0.filter_by_substring(['hello', 'world'], 'xyz') == []

    # Test case 5: Empty substring matches all strings
    assert module_0.filter_by_substring(['a', 'b', 'c'], '') == ['a', 'b', 'c']

    # Test case 6: Substring equals the entire string
    assert module_0.filter_by_substring(['test', 'other'], 'test') == ['test']

    # Test case 7: Case sensitivity check
    assert module_0.filter_by_substring(['Apple', 'apple'], 'Apple') == ['Apple']

    # Test case 8: Substring appears multiple times in a string
    assert module_0.filter_by_substring(['aaa', 'aba'], 'aa') == ['aaa']

    # Test case 9: Order of original list is preserved
    assert module_0.filter_by_substring(['xxa', 'axx', 'xa'], 'a') == ['xxa', 'axx', 'xa']

    # Test case 10: Single element list with match
    assert module_0.filter_by_substring(['python'], 'py') == ['python']

    print("All test cases passed!")


if __name__ == "__main__":
    test_filter_by_substring()