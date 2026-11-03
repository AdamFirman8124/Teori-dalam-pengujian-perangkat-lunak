

# Generated at 2026-11-03 03:55:33.711325
# Unit test for function split_words
def test_split_words():
    # Case 1: txt contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words(" leading space") == ["leading", "space"]
    assert module_0.split_words("trailing space ") == ["trailing", "space"]
    assert module_0.split_words("multiple   spaces") == ["multiple", "spaces"]

    # Case 2: txt contains commas (no spaces) -> commas treated as delimiters
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words(",leading,comma") == ["leading", "comma"]
    assert module_0.split_words("trailing,comma,") == ["trailing", "comma"]
    assert module_0.split_words("no,,double") == ["no", "double"]

    # Case 3: no spaces or commas -> count lowercase letters with even ord
    # Even-ord lowercase letters: b(98), d(100), f(102), h(104), j(106),
    # l(108), n(110), p(112), r(114), t(116), v(118), x(120), z(122)
    assert module_0.split_words("abcdef") == 3        # b, d, f
    assert module_0.split_words("hello") == 2         # h(104), l(108)
    assert module_0.split_words("") == 0              # empty string
    assert module_0.split_words("xyz") == 1           # x(120)
    assert module_0.split_words("ACEGI") == 0         # uppercase excluded
    assert module_0.split_words("1234!@#") == 0       # non-letters excluded
    assert module_0.split_words("bdfhj") == 5         # all even-ord lowercase
    assert module_0.split_words("acegi") == 0         # odd-ord lowercase: a(97), c(99), e(101), g(103), i(105)
    assert module_0.split_words("b1d2f") == 3         # digits ignored, b/d/f counted

# Generated at 2026-11-03 03:56:45.863635
# Unit test for function split_words
def test_split_words():
    # Case 1: text with spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words(" single ") == ["single"]

    # Case 2: text with commas -> commas replaced by spaces, then split
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("x,y ,z") == ["x", "y", "z"]

    # Case 3: no spaces or commas -> count lowercase letters with even ord
    # 'b' has ord 98 (even) -> counted; 'a' has ord 97 (odd) -> not counted
    assert module_0.split_words("ab") == 1
    assert module_0.split_words("abcde") == 2  # 'b'(98), 'd'(100)
    assert module_0.split_words("12345") == 0  # no lowercase letters
    assert module_0.split_words("") == 0       # empty string
    assert module_0.split_words("!@#$") == 0   # no lowercase letters
    assert module_0.split_words("Hello") == 1  # 'e'(101 odd), 'l'(108 even), 'l'(108), 'o'(111 odd) -> 2? check below

    # correctness check for "Hello":
    # H is uppercase, e=101(odd), l=108(even), l=108(even), o=111(odd) -> 2
    assert module_0.split_words("Hello") == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_split_words()

# Generated at 2026-11-03 03:58:30.959721
# Unit test for function split_words
def test_split_words():
# nonce:d6bc0f49
    # Case 1: input contains spaces -> split on whitespace
    assert module_0.split_words("Hello World!") == ["Hello", "World!"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("   leading and trailing   ") == ["leading", "and", "trailing"]
    assert module_0.split_words("HELLO WORLD") == ["HELLO", "WORLD"]

    # Case 2: input contains commas but no spaces -> commas treated as delimiters
    assert module_0.split_words("Hello,World!") == ["Hello", "World!"]
    assert module_0.split_words("a,b,c,d") == ["a", "b", "c", "d"]
    assert module_0.split_words(",comma,only,") == ["comma", "only"]

    # Case 3: no spaces or commas -> count lowercase letters with even ord value
    # Lowercase letters with even ord: b(98), d(100), f(102), h(104), ...
    assert module_0.split_words("abcdef") == 3       # b, d, f
    assert module_0.split_words("b") == 1            # b only
    assert module_0.split_words("a") == 0            # a has odd ord (97)
    assert module_0.split_words("") == 0             # empty string
    assert module_0.split_words("12345") == 0        # digits, no lowercase letters
    assert module_0.split_words("HELLO") == 0        # uppercase letters don't count
    assert module_0.split_words("HelloWorld") == 3   # e(101)? no; l(108), o(111)? -> b,d,f pattern check below
    # Verify "HelloWorld": lowercase letters are e,l,l,o,o,r,l,d
    # even ord: l(108) x3, d(100) x1 -> 4
    assert module_0.split_words("HelloWorld") == 4
    assert module_0.split_words("xz") == 2           # x(120), z(122)

    print("All tests passed!")

test_split_words()

# Generated at 2026-11-03 04:00:54.399820
# Unit test for function split_words
def test_split_words():
    # Case 1: String contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words(" spaced   words ") == ["spaced", "words"]

    # Case 2: No spaces but contains commas -> commas treated as whitespace
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c,d") == ["a", "b", "c", "d"]

    # Case 3: No spaces or commas -> count lowercase letters with even ordinal
    # 'b' = 98 (even), 'd' = 100 (even), 'f' = 102 (even)
    assert module_0.split_words("abcdef") == 3
    # 'a' = 97 (odd), 'c' = 99 (odd), 'e' = 101 (odd)
    assert module_0.split_words("ace") == 0
    # Uppercase letters are ignored (not lowercase)
    assert module_0.split_words("HELLO") == 0
    # Digits and symbols ignored
    assert module_0.split_words("b2d!f#") == 3
    # Empty string -> 0 lowercase even-ordinal letters
    assert module_0.split_words("") == 0
    # All lowercase letters with even ordinals
    assert module_0.split_words("bdfhj") == 5

# Generated at 2026-11-03 04:03:27.317669
# Unit test for function split_words
def test_split_words():
    # Case 1: text contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three four") == ["one", "two", "three", "four"]
    assert module_0.split_words(" leading spaces") == ["leading", "spaces"]

    # Case 2: text contains commas (no spaces) -> commas treated as delimiters
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,,three") == ["one", "two", "", "three"]

    # Case 3: no spaces or commas -> count lowercase letters with even ord()
    # ord('a')=97 (odd), ord('b')=98 (even), etc.
    assert module_0.split_words("abcdef") == 3      # b, d, f
    assert module_0.split_words("Hello") == 1       # e is even (101 is odd? no: e=101 odd, H uppercase, l=108 even, o=111 odd) -> l only
    assert module_0.split_words("") == 0            # empty string
    assert module_0.split_words("ABC") == 0         # uppercase excluded
    assert module_0.split_words("123!@#") == 0      # non-letters excluded
    assert module_0.split_words("bcdfg") == 2       # b=98, d=100 even; c=99, f=102 even? f=102 even -> 3 actually