

# Generated at 2026-11-02 10:34:58.385105
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    from typing import List

    # Basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Prefix matching multiple strings
    assert module_0.filter_by_prefix(['apple', 'banana', 'avocado', 'cherry'], 'a') == ['apple', 'avocado']

    # Empty prefix should return all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Empty input list
    assert module_0.filter_by_prefix([], 'a') == []

    # No matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Prefix equal to entire string (exact match)
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']

    # Prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc'], 'abc') == ['abc']

    # Case sensitivity check
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']

    # Prefix matching single string
    assert module_0.filter_by_prefix(['hello', 'world'], 'wor') == ['world']

    # Order preservation
    assert module_0.filter_by_prefix(['xyz', 'x', 'xz'], 'x') == ['xyz', 'x', 'xz']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 10:35:40.979131
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with empty list
    assert module_0.filter_by_prefix([], "a") == []

    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(["abc", "def", "abd"], "") == ["abc", "def", "abd"]

    # Test with matching prefix
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]

    # Test with no matches
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "z") == []

    # Test with prefix matching all strings
    assert module_0.filter_by_prefix(["abcd", "abce", "abcf"], "abc") == ["abcd", "abce", "abcf"]

    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(["ab", "abc", "abcd"], "abcd") == ["abcd"]

    # Test with exact match
    assert module_0.filter_by_prefix(["hello", "world"], "hello") == ["hello"]

    # Test preserves original order
    assert module_0.filter_by_prefix(["a1", "b1", "a2", "b2"], "a") == ["a1", "a2"]

    # Test case sensitivity
    assert module_0.filter_by_prefix(["Apple", "apple"], "a") == ["apple"]

    print("All tests passed!")


test_filter_by_prefix()

# Generated at 2026-11-02 10:36:57.475418
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Prefix matches all elements
    assert module_0.filter_by_prefix(['abc', 'abd', 'abe'], 'ab') == ['abc', 'abd', 'abe']

    # No matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Empty input list
    assert module_0.filter_by_prefix([], 'a') == []

    # Empty prefix returns all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Full-string prefix matches only exact string
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']

    # Case sensitivity check
    assert module_0.filter_by_prefix(['Apple', 'apple', 'banana'], 'A') == ['Apple']

    # Prefix longer than strings matches nothing
    assert module_0.filter_by_prefix(['a', 'ab'], 'abc') == []

    # Duplicated strings are preserved
    assert module_0.filter_by_prefix(['abc', 'abc', 'xyz'], 'abc') == ['abc', 'abc']

    # Order is preserved
    assert module_0.filter_by_prefix(['b1', 'a1', 'b2', 'a2'], 'a') == ['a1', 'a2']

    print("All test cases passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 10:38:16.320268
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Empty prefix matches all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # No matches found
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []
    
    # Empty input list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Exact match equals prefix
    assert module_0.filter_by_prefix(['abc'], 'abc') == ['abc']
    
    # Prefix longer than the string itself
    assert module_0.filter_by_prefix(['ab'], 'abc') == []
    
    # Case sensitivity check
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']
    
    # Order of matches is preserved
    assert module_0.filter_by_prefix(['a1', 'b1', 'a2', 'b2', 'a3'], 'a') == ['a1', 'a2', 'a3']
    
    # Multiple strings with same prefix
    assert module_0.filter_by_prefix(['apple', 'apricot', 'banana'], 'ap') == ['apple', 'apricot']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 10:39:17.664275
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with empty list
    assert module_0.filter_by_prefix([], "a") == []

    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "") == ["abc", "bcd", "cde", "array"]

    # Test with normal prefix matches
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]

    # Test with prefix matching multiple strings
    assert module_0.filter_by_prefix(["apple", "apply", "banana", "app"], "app") == ["apple", "apply", "app"]

    # Test with prefix matching no strings
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "z") == []

    # Test with prefix equal to a full string
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "abc") == ["abc"]

    # Test with prefix longer than strings in list
    assert module_0.filter_by_prefix(["a", "b"], "abc") == []

    # Test case sensitivity
    assert module_0.filter_by_prefix(["Apple", "apple", "APple"], "a") == ["apple"]

    # Test with duplicate strings
    assert module_0.filter_by_prefix(["abc", "abc", "xyz"], "abc") == ["abc", "abc"]

    # Test with single character prefix
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "c") == ["cde"]

    # Test with strings containing spaces
    assert module_0.filter_by_prefix(["hello world", "hello there", "goodbye"], "hello ") == ["hello world", "hello there"]

    # Test with special characters
    assert module_0.filter_by_prefix(["#tag", "tag", "#mention"], "#") == ["#tag", "#mention"]

    print("All tests passed!")


# Run the test
if __name__ == "__main__":
    test_filter_by_prefix()