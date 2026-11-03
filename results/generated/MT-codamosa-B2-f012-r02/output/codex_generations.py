

# Generated at 2026-11-01 20:51:09.509844
# Unit test for function longest
def test_longest():
    # Empty list should return None
    assert module_0.longest([]) is None

    # Single string list returns that string
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings with a unique longest
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["x", "yy", "zzz", "w"]) == "zzz"

    # Ties: first occurrence of max length wins
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"

    # All strings same length: returns first
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["xx", "yy"]) == "xx"

    # Strings with empty string present
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest([""]) == ""

    # Long strings
    assert module_0.longest(["short", "a much longer string here"]) == "a much longer string here"

# Generated at 2026-11-01 20:52:04.419623
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple elements with distinct lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["bb", "ccc", "a"]) == "ccc"

    # Test ties: first occurrence of max length should be returned
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["abc", "de", "xyz"]) == "abc"

    # Test all elements of equal length
    assert module_0.longest(["x", "y", "z"]) == "x"
    assert module_0.longest(["aa", "bb"]) == "aa"

    # Test empty string among values
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

    # Test longer lists
    assert module_0.longest(["one", "two", "three", "four", "five"]) == "three"
    assert module_0.longest(["cat", "dog", "mouse", "bird"]) == "mouse"


if __name__ == "__main__":
    test_longest()
    print("All tests passed!")

# Generated at 2026-11-01 20:52:57.824154
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Returns the longest string among multiple
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"

    # Multiple strings with same max length returns the first one
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["xx", "yy", "zz"]) == "xx"

    # Returns first occurrence when duplicates of longest exist
    assert module_0.longest(["abc", "de", "abc"]) == "abc"

    # Longest at the end of the list
    assert module_0.longest(["a", "ab", "abc", "abcd"]) == "abcd"

    # Longest at the beginning of the list
    assert module_0.longest(["abcdef", "a", "ab"]) == "abcdef"

    # Strings with spaces count their full length
    assert module_0.longest(["a b", "abc"]) == "a b"

    # Empty string in list is handled
    assert module_0.longest(["", "a"]) == "a"

# Generated at 2026-11-01 20:53:24.626937
# Unit test for function longest
def test_longest():
    # Test with empty list returns None
    assert module_0.longest([]) is None

    # Test with single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test with multiple elements of different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Test tie-breaking: first longest string should be returned
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"
    assert module_0.longest(["x", "yy", "z", "ww"]) == "yy"

    # Test with mixed-length strings where max appears later
    assert module_0.longest(["one", "two", "three", "four"]) == "three"

    # Test with all same-length strings
    assert module_0.longest(["cat", "dog", "fox"]) == "cat"

    # Test with empty strings in list
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest(["", "a", ""]) == "a"

    # Test with longer realistic strings
    assert module_0.longest(["apple", "banana", "cherry"]) == "banana"
    assert module_0.longest(["hi", "hello", "hey", "greetings"]) == "greetings"

    # Test with whitespace strings
    assert module_0.longest(["a b", "ab", " abc "]) == " abc "

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 20:54:06.110696
# Unit test for function longest
def test_longest():
    # Empty list should return None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings with different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["one", "two", "three"]) == "three"

    # Tie in length: first occurrence should be returned
    assert module_0.longest(["ab", "cd", "efg"]) == "ab"
    assert module_0.longest(["abc", "def", "ghi"]) == "abc"
    assert module_0.longest(["xx", "yy"]) == "xx"

    # All strings same length: first one returned
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["same", "size", "word"]) == "same"

    # Empty string in list
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest([""]) == ""

    # Strings with spaces and special characters
    assert module_0.longest(["a b", "ab!", "long string"]) == "long string"

    # Longer list
    assert module_0.longest(["x", "yy", "zzz", "w", "wwww"]) == "wwww"

    # Case sensitivity does not affect length
    assert module_0.longest(["ABC", "a"]) == "ABC"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 20:54:37.100935
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element
    assert module_0.longest(['x']) == 'x'
    assert module_0.longest(['']) == ''

    # Multiple elements, unique longest
    assert module_0.longest(['a', 'bb', 'ccc']) == 'ccc'
    assert module_0.longest(['abc', 'de', 'fghi']) == 'fghi'
    assert module_0.longest(['one', 'two', 'three', 'four']) == 'three'

    # Ties: first occurrence of the max length is returned
    assert module_0.longest(['a', 'b', 'c']) == 'a'
    assert module_0.longest(['aa', 'bb', 'cc']) == 'aa'
    assert module_0.longest(['abc', 'de', 'xyz']) == 'abc'

    # Empty strings mixed with non-empty
    assert module_0.longest(['', 'a', '']) == 'a'
    assert module_0.longest(['', '']) == ''

    # Longer strings later in the list
    assert module_0.longest(['short', 'a much longer string']) == 'a much longer string'

    # Whitespace counts toward length
    assert module_0.longest(['ab', 'a b']) == 'a b'

# Generated at 2026-11-01 20:55:14.870515
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single string returns that string
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple strings with different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["bb", "ccc", "a"]) == "ccc"

    # Test tie: first longest string is returned
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"

    # Test all strings of equal length: first is returned
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["xx", "yy", "zz"]) == "xx"

    # Test with empty strings
    assert module_0.longest(["", ""]) == ""
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["a", ""]) == "a"

    # Test longest string at the end
    assert module_0.longest(["a", "ab", "abc", "abcd"]) == "abcd"

    # Test with longer realistic strings
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 20:55:41.385334
# Unit test for function longest
def test_longest():
    # Empty list should return None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple elements, unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"

    # Multiple elements with same max length: return the first one
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["ab", "cd", "ef"]) == "ab"
    assert module_0.longest(["xy", "abc", "def"]) == "abc"

    # Longest element at various positions
    assert module_0.longest(["short", "longest_one", "mid"]) == "longest_one"
    assert module_0.longest(["mid", "short", "longest_one"]) == "longest_one"

    # Strings with spaces and special characters
    assert module_0.longest(["a b", "abc!@#", "x"]) == "abc!@#"

    # Empty string in list
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-11-01 20:56:08.037658
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single-element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple strings with different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["ab", "abc", "a"]) == "abc"

    # Test ties: first occurrence of the longest length is returned
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["abc", "def", "ghi"]) == "abc"

    # Test strings with empty strings
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest(["", "a"]) == "a"

    # Test strings with spaces and special characters
    assert module_0.longest([" ", "  "]) == "  "
    assert module_0.longest(["hello world", "hi"]) == "hello world"

    # Test unicode strings
    assert module_0.longest(["héllo", "hi"]) == "héllo"

    # Test long list
    assert module_0.longest(["x" * i for i in range(100)]) == "x" * 99

# Generated at 2026-11-01 20:56:25.026063
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple strings with a clear maximum
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Test tie case: first longest string wins
    assert module_0.longest(["one", "two", "three", "four"]) == "three"
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"

    # Test all strings of equal length
    assert module_0.longest(["x", "y", "z"]) == "x"
    assert module_0.longest(["cat", "dog", "pig"]) == "cat"

    # Test unsorted input preserves original order
    assert module_0.longest(["longer", "short", "medium"]) == "longer"
    assert module_0.longest(["a", "abcde", "abcd"]) == "abcde"

    # Test strings with spaces and special characters
    assert module_0.longest(["hi there", "ok", "!@#$%"]) == "hi there"

    # Test unicode strings
    assert module_0.longest(["héllo", "wörld!", "hi"]) == "wörld!"

    # Test empty string among non-empty strings
    assert module_0.longest(["", "b", "cc"]) == "cc"

    # Test list containing only an empty string
    assert module_0.longest([""]) == ""

if __name__ == "__main__":
    test_longest()
    print("All tests passed!")

# Generated at 2026-11-01 20:56:50.527281
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings with unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Ties: returns the first occurrence of the longest string
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["xx", "yy", "zz"]) == "xx"

    # Mixed lengths with duplicate max length
    assert module_0.longest(["one", "two", "three", "four"]) == "three"
    assert module_0.longest(["cat", "dog", "bird", "fish"]) == "bird"

    # Empty strings in list
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest(["", "a", ""]) == "a"

    # Long strings
    assert module_0.longest(["a" * 100, "b" * 99]) == "a" * 100

    # Unicode strings
    assert module_0.longest(["héllo", "hi", "wörld!"]) == "wörld!"

    print("All tests passed!")

# Generated at 2026-11-01 20:57:16.984667
# Unit test for function longest
def test_longest():
    # Test with an empty list
    assert module_0.longest([]) is None

    # Test with a single-element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test with multiple elements of different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Test when multiple strings share the maximum length (first one wins)
    assert module_0.longest(["one", "two", "three"]) == "three"
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"
    assert module_0.longest(["x", "yy", "zz", "w"]) == "yy"

    # Test with all strings of equal length
    assert module_0.longest(["ab", "cd", "ef"]) == "ab"

    # Test with empty strings in the list
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["a", ""]) == "a"

    # Test with longer realistic strings
    assert module_0.longest(["apple", "banana", "cherry"]) == "banana"
    assert module_0.longest(["a" * 100, "b" * 50]) == "a" * 100

    # Verify result type
    result = module_0.longest(["cat", "dog"])
    assert isinstance(result, str)


test_longest()
print("All tests passed!")

# Generated at 2026-11-01 20:58:02.166220
# Unit test for function longest
def test_longest():
    # Test with an empty list
    assert module_0.longest([]) is None

    # Test with a single element
    assert module_0.longest(['a']) == 'a'
    assert module_0.longest(['hello']) == 'hello'

    # Test with multiple elements of different lengths
    assert module_0.longest(['a', 'bb', 'ccc']) == 'ccc'
    assert module_0.longest(['ccc', 'bb', 'a']) == 'ccc'
    assert module_0.longest(['abc', 'ab', 'a']) == 'abc'

    # Test with multiple elements of the same max length (should return first)
    assert module_0.longest(['a', 'b', 'c']) == 'a'
    assert module_0.longest(['ab', 'cd', 'efg']) == 'efg'
    assert module_0.longest(['one', 'two', 'three']) == 'three'

    # Test with duplicates
    assert module_0.longest(['abc', 'abc', 'ab']) == 'abc'

    # Test with strings of same length throughout
    assert module_0.longest(['x', 'y']) == 'x'

    # Test with longer strings
    assert module_0.longest(['short', 'medium size', 'the longest string here']) == 'the longest string here'

    # Test with empty strings in list
    assert module_0.longest(['', 'a']) == 'a'
    assert module_0.longest(['', '']) == ''

    # Test with unicode strings
    assert module_0.longest(['héllo', 'hi']) == 'héllo'

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 20:58:43.371028
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple elements with unique max length
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"

    # Test ties - first occurrence should be returned
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["x", "yy", "zz"]) == "yy"

    # Test all elements same length - returns first
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["same", "size", "word"]) == "same"

    # Test with longer realistic strings
    assert module_0.longest(["apple", "banana", "kiwi"]) == "banana"
    assert module_0.longest(["", "a", ""]) == "a"

    # Test with empty strings only
    assert module_0.longest(["", "", ""]) == ""

    # Test order preservation for first max
    assert module_0.longest(["short", "longest!!", "medium", "longest??"]) == "longest!!"


test_longest()
print("All tests passed!")

# Generated at 2026-11-01 20:59:19.311833
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple elements with clear longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["abc", "ab", "abcd"]) == "abcd"

    # Test ties - first occurrence of max length wins
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["xx", "yy", "z"]) == "xx"
    assert module_0.longest(["one", "two", "ten"]) == "one"

    # Test all elements same length - returns first
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"

    # Test with empty strings mixed in
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", "", ""]) == ""
    assert module_0.longest([""]) == ""

    # Test longer lists
    assert module_0.longest(["short", "tiny", "moderate!", "big"]) == "moderate!"
    assert module_0.longest(list("abcdef")) == "a"  # all length 1, first wins

# Generated at 2026-11-01 20:59:28.007023
# Unit test for function longest
def test_longest():
    # Test with an empty list - should return None
    assert module_0.longest([]) is None

    # Test with a single-element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test with multiple elements where one is clearly the longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["x", "yyy", "zz"]) == "yyy"

    # Test when multiple strings share the maximum length - first occurrence wins
    assert module_0.longest(["aa", "bb", "cc"]) == "aa"
    assert module_0.longest(["one", "two", "ten"]) == "one"

    # Test with mixed lengths and ties
    assert module_0.longest(["a", "bb", "c", "dd"]) == "bb"

    # Test with longer realistic strings
    assert module_0.longest(["apple", "banana", "kiwi"]) == "banana"
    assert module_0.longest(["cat", "dog", "elephant", "fox"]) == "elephant"

    # Test with strings containing spaces / special characters
    assert module_0.longest(["", " ", "  "]) == "  "
    assert module_0.longest(["!@#", "abcd$%^"]) == "abcd$%^"

    # Test that result is one of the input strings
    strings = ["ab", "cd", "efg"]
    result = module_0.longest(strings)
    assert result in strings

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 20:59:53.505957
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test multiple strings with distinct lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Test ties - should return the first occurrence of max length
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["xx", "yy", "z"]) == "xx"
    assert module_0.longest(["aaa", "bbb", "ccc"]) == "aaa"

    # Test all strings same length
    assert module_0.longest(["x", "y", "z"]) == "x"
    assert module_0.longest(["ab", "cd", "ef"]) == "ab"

    # Test with longer realistic strings
    assert module_0.longest(["apple", "banana", "kiwi"]) == "banana"
    assert module_0.longest(["", "a", ""]) == "a"

    # Test empty strings only
    assert module_0.longest(["", "", ""]) == ""

    # Test whitespace strings
    assert module_0.longest(["  ", " ", "   "]) == "   "

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-01 21:00:38.162672
# Unit test for function longest
def test_longest():
    # Empty list should return None
    assert module_0.longest([]) is None

    # Single string list should return that string
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Multiple strings with a unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"

    # Ties: should return the first occurrence of the max length
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["x", "yy", "zz"]) == "yy"
    assert module_0.longest(["ab", "cd", "ef"]) == "ab"

    # Longest string appears later in the list
    assert module_0.longest(["short", "tiny", "a much longer string"]) == "a much longer string"

    # Empty string handling
    assert module_0.longest([""]) == ""
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

    # Strings with spaces and special characters
    assert module_0.longest(["hi there", "hi", "hello world!"]) == "hello world!"

    # Unicode strings
    assert module_0.longest(["héllo", "wörld"]) == "héllo"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()