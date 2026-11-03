

# Generated at 2026-11-01 19:37:59.487075
# Unit test for function longest
def test_longest():
    # Test with empty list
    assert module_0.longest([]) is None
    
    # Test with single element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"
    
    # Test with multiple elements of different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["x", "xyz", "xy"]) == "xyz"
    
    # Test tie-breaking: first occurrence of max length wins
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"
    assert module_0.longest(["two", "one", "ten"]) == "two"
    
    # Test with longer strings mixed in
    assert module_0.longest(["short", "a very long string here", "medium"]) == "a very long string here"
    
    # Test with duplicate max-length strings
    assert module_0.longest(["cat", "dog", "elephant", "bird"]) == "elephant"
    
    # Test with all same-length strings
    assert module_0.longest(["one", "two"]) == "one"
    
    # Test with whitespace strings
    assert module_0.longest(["", " ", "  "]) == "  "
    assert module_0.longest(["", "", ""]) == ""

# Generated at 2026-11-01 19:38:47.822688
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings, longest is unique
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["x", "yz", "abcde", "wxyz"]) == "abcde"

    # Tie case: first occurrence of the max length is returned
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"

    # All strings same length: first one returned
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"

    # Empty string in list
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""
    assert module_0.longest([""]) == ""

    # Strings with spaces and special characters
    assert module_0.longest(["hi", "hello world", "hey"]) == "hello world"

    # Longer list
    assert module_0.longest(["one", "two", "three", "four", "five"]) == "three"

    # Order preservation check with duplicates of max length
    assert module_0.longest(["cat", "dog", "bird", "fish"]) == "bird"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 19:39:35.947544
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["abc"]) == "abc"

    # Multiple elements, unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["x", "yyy", "zz"]) == "yyy"

    # Ties: returns the first string with maximum length
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["abc", "de", "xyz"]) == "abc"
    assert module_0.longest(["aa", "bb", "cc", "dd"]) == "aa"

    # All elements same length returns first
    assert module_0.longest(["x", "x", "x"]) == "x"

    # Longest appears in the middle
    assert module_0.longest(["a", "longest", "b"]) == "longest"

# Generated at 2026-11-01 19:40:09.146801
# Unit test for function longest
def test_longest():
    from typing import List, Optional

    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single string
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple strings with clear longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Test ties - should return the first one with max length
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"

    # Test all strings same length
    assert module_0.longest(["x", "y", "z"]) == "x"

    # Test with empty strings in list
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest(["", "a", ""]) == "a"

    # Test longer list
    assert module_0.longest(["one", "two", "three", "four", "five"]) == "three"

    # Test strings with special characters
    assert module_0.longest(["!!!", "hello world", "12345"]) == "hello world"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 19:40:36.773807
# Unit test for function longest
def test_longest():
    # Test with empty list
    assert module_0.longest([]) is None

    # Test with single element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test with multiple elements of different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["apple", "banana", "kiwi"]) == "banana"

    # Test with ties - should return the first one
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"
    assert module_0.longest(["abc", "de", "fgh"]) == "abc"
    assert module_0.longest(["x", "yy", "zz"]) == "yy"

    # Test with all same length
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["same", "size", "word"]) == "same"

    # Test with empty strings
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest(["", "a"]) == "a"

    # Test with long strings
    assert module_0.longest(["short", "a very long string here", "medium"]) == "a very long string here"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 19:41:45.863209
# Unit test for function longest
def test_longest():
    # Empty list should return None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple elements - longest wins
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["x", "yy", "zzz", "w"]) == "zzz"

    # Longest appears first in the list
    assert module_0.longest(["abcdef", "abc", "ab"]) == "abcdef"

    # Ties: first occurrence of max length is returned
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["one", "two", "ten"]) == "one"
    assert module_0.longest(["abc", "def", "ghi"]) == "abc"

    # All same length
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["xx", "yy"]) == "xx"

    # Strings with spaces / special characters count their full length
    assert module_0.longest(["a b c", "abc"]) == "a b c"
    assert module_0.longest(["!!!", "?"]) == "!!!"

    # Empty strings mixed with non-empty ones
    assert module_0.longest(["", "", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""  # all empty: first (only) max-length is ""

# Generated at 2026-11-01 19:42:23.580301
# Unit test for function longest
def test_longest():
    # Test with empty list
    assert module_0.longest([]) is None

    # Test with single element
    assert module_0.longest(['a']) == 'a'
    assert module_0.longest(['']) == ''

    # Test with unique longest string
    assert module_0.longest(['a', 'bb', 'ccc']) == 'ccc'
    assert module_0.longest(['a', 'ab', 'abc', 'cd']) == 'abc'

    # Test with ties - first occurrence of max length should be returned
    assert module_0.longest(['a', 'bb', 'cc']) == 'bb'
    assert module_0.longest(['abc', 'de', 'xyz']) == 'abc'

    # Test with all strings of same length
    assert module_0.longest(['x', 'y', 'z']) == 'x'

    # Test with empty strings mixed in
    assert module_0.longest(['', 'a', '']) == 'a'
    assert module_0.longest(['', '']) == ''

    # Test with longer strings
    assert module_0.longest(['hello', 'hi', 'hey']) == 'hello'
    assert module_0.longest(['one', 'two', 'three', 'four']) == 'three'

# Generated at 2026-11-01 19:42:51.928290
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single string returns that string
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings with a clear longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["apple", "banana", "kiwi"]) == "banana"
    assert module_0.longest(["abc", "abcdef", "ab"]) == "abcdef"

    # Longest string appears first
    assert module_0.longest(["longest", "a", "bb"]) == "longest"

    # Ties: first occurrence of the maximum length is returned
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["x", "yy", "zz"]) == "yy"
    assert module_0.longest(["abc", "def", "ghi"]) == "abc"

    # All strings the same length
    assert module_0.longest(["a", "b", "c"]) == "a"

    # Empty strings in the list
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

    # Strings with spaces and special characters
    assert module_0.longest(["a b", "ab", "abc!"]) == "abc!"

    # Unicode strings
    assert module_0.longest(["héllo", "hi", "wörld!!"]) == "wörld!!"

    # Long strings
    assert module_0.longest(["short", "much much longer string"]) == "much much longer string"

    # Large input list
    big_list = ["x" * i for i in range(100)]
    assert module_0.longest(big_list) == "x" * 99

# Generated at 2026-11-01 19:43:20.924700
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple elements with unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"

    # Test tie returns first occurrence of max length
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["x", "yy", "zz", "w"]) == "yy"

    # Test all elements same length (returns first)
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["ab", "cd", "ef"]) == "ab"

    # Test with empty strings in the list
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest(["", "a", ""]) == "a"

    # Test longer realistic strings
    assert module_0.longest(["apple", "banana", "cherry"]) == "banana"
    assert module_0.longest(["short", "longer string here", "medium"]) == "longer string here"

# Generated at 2026-11-01 19:44:12.430399
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple elements with one clearly longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Ties: first longest element in list is returned
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"

    # All elements same length: returns first
    assert module_0.longest(["x", "y", "z"]) == "x"
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"

    # Strings with whitespace count toward length
    assert module_0.longest(["a b", "ab"]) == "a b"

    # Empty string among non-empty strings
    assert module_0.longest(["", "a", ""]) == "a"

    # All empty strings: returns first empty string
    assert module_0.longest(["", "", ""]) == ""

# Generated at 2026-11-01 19:45:05.380410
# Unit test for function longest
def test_longest():
    # Empty list should return None
    assert module_0.longest([]) is None

    # Single string list returns that string
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings, unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["x", "yyy", "zz"]) == "yyy"

    # Longest string at the beginning
    assert module_0.longest(["longest", "short", "mid"]) == "longest"

    # Longest string at the end
    assert module_0.longest(["a", "ab", "abcd"]) == "abcd"

    # Ties: first occurrence of max length wins
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["ab", "cd", "efg", "hij"]) == "efg"
    assert module_0.longest(["same", "size", "word"]) == "same"

    # Strings with empty strings
    assert module_0.longest(["", ""]) == ""
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["a", ""]) == "a"

    # All empty strings list
    assert module_0.longest(["", "", ""]) == ""

    # Whitespace and special characters
    assert module_0.longest(["  ", "a b c", "!"]) == "a b c"

    # Unicode strings
    assert module_0.longest(["héllo", "hi", "wörld!"]) == "wörld!"

    # Very long string
    assert module_0.longest(["a", "x" * 1000]) == "x" * 1000

# Generated at 2026-11-01 19:45:29.136853
# Unit test for function longest
def test_longest():
    # Test with empty list
    assert module_0.longest([]) is None

    # Test with single element
    assert module_0.longest(["a"]) == "a"

    # Test with multiple elements of different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"

    # Test where first occurrence of max length should be returned
    assert module_0.longest(["ab", "cd", "efg", "hij"]) == "efg"

    # Test with all same length - returns first one
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["xy", "zw"]) == "xy"

    # Test with empty strings
    assert module_0.longest([""]) == ""
    assert module_0.longest(["", "a", ""]) == "a"

    # Test with longer strings
    assert module_0.longest(["hello", "world", "python"]) == "python"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"

    # Test with duplicate long strings - first wins
    assert module_0.longest(["aa", "bbb", "bbb"]) == "bbb"

    # Test case sensitivity doesn't matter for length
    assert module_0.longest(["A", "BBB", "cc"]) == "BBB"

# Generated at 2026-11-01 19:45:36.913994
# Unit test for function longest
def test_longest():
    # Test with empty list
    assert module_0.longest([]) is None

    # Test with single string
    assert module_0.longest(["a"]) == "a"

    # Test with multiple strings of different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["ab", "abc", "a"]) == "abc"

    # Test with ties - first longest string should be returned
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"

    # Test with all strings same length
    assert module_0.longest(["x", "y", "z"]) == "x"

    # Test with empty strings in list
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

    # Test with longer realistic strings
    assert module_0.longest(["hello", "world!", "hi"]) == "world!"

    # Test with unicode strings
    assert module_0.longest(["héllo", "wörld", "hi"]) == "héllo"

    # Test that result is None type for empty input
    result = module_0.longest([])
    assert result is None

# Generated at 2026-11-01 19:46:13.956446
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list returns that element
    assert module_0.longest(['a']) == 'a'
    assert module_0.longest(['hello']) == 'hello'

    # Test list with multiple elements of different lengths
    assert module_0.longest(['a', 'bb', 'ccc']) == 'ccc'
    assert module_0.longest(['ccc', 'bb', 'a']) == 'ccc'
    assert module_0.longest(['abc', 'ab', 'a']) == 'abc'

    # Test list where multiple strings share the max length - first one wins
    assert module_0.longest(['a', 'bb', 'cc']) == 'bb'
    assert module_0.longest(['xx', 'yy', 'zz']) == 'xx'

    # Test all strings same length
    assert module_0.longest(['a', 'b', 'c']) == 'a'

    # Test with empty strings in list
    assert module_0.longest(['', 'a', '']) == 'a'
    assert module_0.longest(['', '']) == ''

    # Test with longer strings
    assert module_0.longest(['short', 'medium_size', 'longest_string_here']) == 'longest_string_here'

    # Test with duplicate longest strings
    assert module_0.longest(['abc', 'def', 'ab']) == 'abc'

# Generated at 2026-11-01 19:46:27.202892
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple elements with different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"

    # Test ties: should return the first occurrence of max length
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["x", "yy", "zz"]) == "yy"
    assert module_0.longest(["aaa", "bbb", "ccc"]) == "aaa"

    # Test all elements same length
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["same", "size", "word"]) == "same"

    # Test with empty strings
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest(["", "a"]) == "a"

    # Test longer realistic input
    assert module_0.longest(["apple", "banana", "cherry", "watermelon"]) == "watermelon"

# Generated at 2026-11-01 19:46:52.495850
# Unit test for function longest
def test_longest():
    # Empty list should return None
    assert module_0.longest([]) is None

    # Single string list returns that string
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings with a clear longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Longest string appears first
    assert module_0.longest(["longest", "short", "mid"]) == "longest"

    # Longest string appears last
    assert module_0.longest(["short", "mid", "longest"]) == "longest"

    # Tie in length: returns the first one with max length
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["a", "bb", "cc", "dd"]) == "bb"

    # All strings same length: returns the first
    assert module_0.longest(["xx", "yy", "zz"]) == "xx"

    # Strings with empty strings mixed in
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

    # Strings with spaces and special characters
    assert module_0.longest(["a b", "abc!"]) == "abc!"
    assert module_0.longest(["  ", "x"]) == "  "
# nonce:c216f2ba

# Generated at 2026-11-01 19:47:24.028739
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings, returns the longest one
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["x", "yyy", "zz"]) == "yyy"

    # Ties: returns the first string with max length
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["a", "bb", "cc", "dd"]) == "bb"

    # All strings have the same length: returns the first
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["one", "two", "six"]) == "one"

    # Longest string appears later in the list
    assert module_0.longest(["short", "tiny", "a much longer string"]) == "a much longer string"

    # Empty strings in the list
    assert module_0.longest(["", ""]) == ""
    assert module_0.longest(["", "a"]) == "a"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()