

# Generated at 2026-11-02 21:57:19.858855
# Unit test for function split_words
def test_split_words():
    # Case 1: text contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]
    assert module_0.split_words("one two  three") == ["one", "two", "three"]

    # Case 2: no spaces but contains commas -> commas treated as separators
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,,three") == ["one", "two", "", "three"]

    # Case 3: no spaces or commas -> count lowercase letters with even ordinal
    # lowercase letters with even ord: b(98), d(100), f(102), h(104), j(106), etc.
    assert module_0.split_words("abcdef") == 3      # b, d, f
    assert module_0.split_words("ghij") == 2        # h, j
    assert module_0.split_words("AAAA") == 0        # uppercase ignored
    assert module_0.split_words("1234!@#") == 0     # no lowercase letters
    assert module_0.split_words("") == 0            # empty string
    assert module_0.split_words("bdfhj") == 5       # all even-ordinal lowercase

# Generated at 2026-11-02 21:58:29.793585
# Unit test for function split_words
def test_split_words():
    # Case 1: text contains spaces -> split on whitespace
    assert module_0.split_words("Hello World") == ["Hello", "World"]
    assert module_0.split_words("one  two   three") == ["one", "two", "three"]
    assert module_0.split_words("a b c d") == ["a", "b", "c", "d"]

    # Case 2: text contains commas (no spaces) -> commas treated as delimiters
    assert module_0.split_words("Hello,World") == ["Hello", "World"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three,four") == ["one", "two", "three", "four"]

    # Case 3: both spaces and commas -> space branch takes precedence
    assert module_0.split_words("Hello, World") == ["Hello", "World"]

    # Case 4: no spaces or commas -> count lowercase chars with even ord
    # 'b'(98), 'd'(100), 'f'(102) are even; 'a'(97), 'c'(99), 'e'(101) are odd
    assert module_0.split_words("abcdef") == 3
    assert module_0.split_words("bBdDfF") == 3          # uppercase excluded
    assert module_0.split_words("1234567") == 0         # no lowercase letters
    assert module_0.split_words("ACEGIK") == 0          # uppercase only
    assert module_0.split_words("") == 0                # empty string
    assert module_0.split_words("acegik") == 0          # all odd ord values
    assert module_0.split_words("bdfhjlnp") == 8        # all even ord values
    assert module_0.split_words("xyz") == 2             # 'x'(120), 'z'(122) even; 'y'(121) odd

    print("All tests passed!")


test_split_words()

# Generated at 2026-11-02 22:00:01.868950
# Unit test for function split_words
def test_split_words():
    # Branch 1: contains a space -> split on whitespace
    assert module_0.split_words("Hello world!") == ["Hello", "world!"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  extra   spaces  ") == ["extra", "spaces"]
    assert module_0.split_words("a,b c") == ["a,b", "c"]      # space takes priority over comma
    assert module_0.split_words(" ") == []                    # whitespace-only string
    assert module_0.split_words("word ") == ["word"]

    # Branch 2: no spaces, contains commas -> commas act as separators
    assert module_0.split_words("Hello,world!") == ["Hello", "world!"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words(",") == []                    # comma-only string
    assert module_0.split_words(",a,") == ["a"]
    assert module_0.split_words("Hello,world,foo") == ["Hello", "world", "foo"]

    # Branch 3: no spaces or commas -> count lowercase letters with even ord
    # even-ord lowercase letters: b(98), d(100), f(102), h(104), j(106),
    # l(108), n(110), p(112), r(114), t(116), v(118), x(120), z(122)
    assert module_0.split_words("abcdef") == 3      # b, d, f
    assert module_0.split_words("bcdf") == 4        # all even-ord letters
    assert module_0.split_words("aeiou") == 0       # all odd ord values
    assert module_0.split_words("") == 0            # empty string
    assert module_0.split_words("z") == 1           # z = 122 (even)
    assert module_0.split_words("a") == 0           # a = 97 (odd)
    assert module_0.split_words("ABC") == 0         # uppercase not counted
    assert module_0.split_words("1b2d") == 2        # non-letters ignored
    assert module_0.split_words("a1b2c3d4") == 2    # only b and d counted

    print("All tests passed!")


if __name__ == "__main__":
    test_split_words()

# Generated at 2026-11-02 22:03:00.441836
# Unit test for function split_words
def test_split_words():
    # Case 1: text with spaces -> split on whitespace
    assert module_0.split_words("Hello World!") == ["Hello", "World!"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  spaced   out  ") == ["spaced", "out"]

    # Case 2: text with commas (no spaces) -> split on commas
    assert module_0.split_words("Hello,World!") == ["Hello", "World!"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,,three") == ["one", "two", "", "three"]

    # Case 3: no spaces or commas -> count lowercase letters with even ordinal
    # ord('a')=97 odd, ord('b')=98 even, ord('c')=99 odd, ord('d')=100 even, ...
    assert module_0.split_words("abcdef") == 3          # b, d, f have even ordinals
    assert module_0.split_words("ABCDEF") == 0          # no lowercase letters
    assert module_0.split_words("") == 0                # empty string
    assert module_0.split_words("12345") == 0           # digits are not lowercase
    assert module_0.split_words("b") == 1               # single even-ordinal lowercase
    assert module_0.split_words("a") == 0               # single odd-ordinal lowercase

    print("All tests passed!")


test_split_words()

# Generated at 2026-11-02 22:05:12.743677
# Unit test for function split_words
def test_split_words():
    # Case 1: text contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  leading and trailing  ") == ["leading", "and", "trailing"]
    # Space takes priority even if commas are present
    assert module_0.split_words("a,b c") == ["a,b", "c"]

    # Case 2: no spaces but contains commas -> commas treated as separators
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words(",comma,leading") == ["", "comma", "leading"]

    # Case 3: no spaces or commas -> count lowercase letters with even ordinal
    # 'a'=97 (odd), 'b'=98 (even), 'c'=99 (odd), 'd'=100 (even), etc.
    assert module_0.split_words("abcdef") == 3      # b, d, f have even ordinals
    assert module_0.split_words("aaaa") == 0        # 'a' has odd ordinal (97)
    assert module_0.split_words("AbCdEf") == 3      # uppercase letters ignored
    assert module_0.split_words("Hello,World") == 1  # comma branch: only 'H','e','l','l'... count 'e'... check: e=101 odd, l=108 even -> 'l' appears twice... see below
    assert module_0.split_words("") == 0            # empty string
    assert module_0.split_words("12345") == 0       # digits are not lowercase letters
    assert module_0.split_words("bdfhjlnp") == 8    # all even-ordinal lowercase letters
    assert module_0.split_words("z") == 1           # 'z' = 122 (even)
    assert module_0.split_words("y") == 0           # 'y' = 121 (odd)