

# Generated at 2026-11-02 12:21:52.892386
# Unit test for function split_words
def test_split_words():
    # Case 1: text contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("Hello World") == ["Hello", "World"]
    assert module_0.split_words("one two  three") == ["one", "two", "three"]
    assert module_0.split_words("a b c d") == ["a", "b", "c", "d"]
    assert module_0.split_words(" leading and trailing ") == ["leading", "and", "trailing"]

    # Case 2: no spaces but contains commas -> commas replaced by spaces, then split
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words(",") == ["", ""]

    # Case 3: no spaces or commas -> count lowercase chars with even ord
    # even-ord lowercase letters: b, d, f, h, j, l, n, p, r, t, v, x, z
    assert module_0.split_words("abcdef") == 3      # b, d, f
    assert module_0.split_words("bdfh") == 4        # all even
    assert module_0.split_words("aceg") == 0        # all odd (a=97, c=99, e=101, g=103)
    assert module_0.split_words("") == 0            # empty string
    assert module_0.split_words("12345") == 0       # digits are not lowercase
    assert module_0.split_words("HELLO") == 0       # uppercase excluded
    assert module_0.split_words("HelloWorld") == 4  # e, l, o, o
    assert module_0.split_words("xyz") == 2         # x(120), z(122)
    assert module_0.split_words("!") == 0           # punctuation excluded
    assert module_0.split_words("Hello,World Test") == ["Hello", "World", "Test"]  # space takes priority

# Generated at 2026-11-02 12:22:35.088505
# Unit test for function split_words
def test_split_words():
    # Case 1: string contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]

    # Case 2: string contains commas but no spaces -> replace commas and split
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]

    # Case 3: no spaces or commas -> count lowercase letters with even ordinal
    # ord('a')=97 (odd), ord('b')=98 (even), ord('c')=99 (odd),
    # ord('d')=100 (even), ord('e')=101 (odd), ord('f')=102 (even)
    assert module_0.split_words("abcdef") == 3
    assert module_0.split_words("bdf") == 3
    assert module_0.split_words("ace") == 0
    assert module_0.split_words("ACE") == 0          # uppercase letters excluded
    assert module_0.split_words("") == 0             # empty string
    assert module_0.split_words("1234!@#") == 0      # no lowercase letters
    assert module_0.split_words("bb") == 2           # multiple even-ordinal letters

    print("All tests passed!")


test_split_words()

# Generated at 2026-11-02 12:23:47.224944
# Unit test for function split_words
def test_split_words():
    # Case 1: txt contains spaces -> split by whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words(" single ") == ["single"]

    # Case 2: txt contains commas (no spaces) -> replace commas with spaces and split
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]

    # Case 3: no spaces or commas -> count lowercase letters with even ord values
    # lowercase letters with ord % 2 == 0 are: b(98), d(100), f(102), h(104), j(106), l(108), n(110), p(112), r(114), t(116), v(118), x(120), z(122)
    assert module_0.split_words("abcdef") == 3   # b, d, f
    assert module_0.split_words("HelloWorld!") == 2  # H,W are uppercase; e(101) odd, l(108) even x2, o(111) odd, r(114) even, d(100) even -> l, l, r, d -> wait recount
    assert module_0.split_words("") == 0
    assert module_0.split_words("1234") == 0
    assert module_0.split_words("bdfh") == 4  # all even-ord lowercase

    print("All tests passed!")


# Correcting the tricky case: "HelloWorld!"
# H(72) upper, e(101) odd, l(108) even, l(108) even, o(111) odd, W(87) upper,
# o(111) odd, r(114) even, l(108) even, d(100) even, !(33) not lower
# -> l, l, r, l, d = 5? Wait: H e l l o W o r l d !
# letters: e(odd), l(even), l(even), o(odd), o(odd), r(even), l(even), d(even) = 5 even lowercase
assert module_0.split_words("HelloWorld!") == 5

if __name__ == "__main__":
    test_split_words()

# Generated at 2026-11-02 12:24:50.569980
# Unit test for function split_words
def test_split_words():
    # Case 1: Text with spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]

    # Case 2: Text with commas (no spaces) -> commas treated as separators
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("apple,banana,cherry") == ["apple", "banana", "cherry"]

    # Case 3: No spaces or commas -> count lowercase letters with even ord
    # 'b'=98, 'd'=100, 'f'=102, 'h'=104, 'j'=106, 'l'=108, 'n'=110,
    # 'p'=112, 'r'=114, 't'=116, 'v'=118, 'x'=120, 'z'=122 (all even)
    # 'a'=97, 'c'=99, 'e'=101, ... (all odd)
    assert module_0.split_words("abcde") == 2   # b, d
    assert module_0.split_words("abcdef") == 3  # b, d, f
    assert module_0.split_words("bdfhjlnprtvxz") == 13  # all even-ord lowercase letters
    assert module_0.split_words("xyz") == 2     # x(120), z(122); y(121) is odd
    assert module_0.split_words("") == 0        # empty string
    assert module_0.split_words("12345") == 0   # no lowercase letters
    assert module_0.split_words("HELLO") == 0   # no lowercase letters
    assert module_0.split_words("Hello World") == ["Hello", "World"]  # space takes priority
    assert module_0.split_words("a,b c") == ["a,b", "c"]  # space takes priority over comma

    print("All test_split_words tests passed!")


if __name__ == "__main__":
    test_split_words()

# Generated at 2026-11-02 12:26:20.062848
# Unit test for function split_words
def test_split_words():import unittest


class TestSplitWords(unittest.TestCase):

    def test_space_split(self):
        self.assertEqual(module_0.split_words("hello world"), ["hello", "world"])

    def test_multiple_spaces(self):
        self.assertEqual(module_0.split_words("one two three"), ["one", "two", "three"])

    def test_comma_split(self):
        self.assertEqual(module_0.split_words("hello,world"), ["hello", "world"])

    def test_multiple_commas(self):
        self.assertEqual(module_0.split_words("a,b,c,d"), ["a", "b", "c", "d"])

    def test_comma_and_space_prefers_space(self):
        self.assertEqual(module_0.split_words("a b,c"), ["a", "b,c"])

    def test_even_lowercase_count(self):
        # b(98), d(100), f(102) have even ordinals
        self.assertEqual(module_0.split_words("abcdef"), 3)

    def test_odd_lowercase_count(self):
        # a(97), c(99), e(101) have odd ordinals
        self.assertEqual(module_0.split_words("ace"), 0)

    def test_mixed_even_odd(self):
        # only 'b' and 'd' qualify
        self.assertEqual(module_0.split_words("abdc"), 2)

    def test_uppercase_not_counted(self):
        # uppercase letters excluded even with even ordinals (B=66, D=68)
        self.assertEqual(module_0.split_words("BDF"), 0)

    def test_digits_not_counted(self):
        self.assertEqual(module_0.split_words("2468"), 0)

    def test_empty_string(self):
        self.assertEqual(module_0.split_words(""), 0)

    def test_repeated_even_letters(self):
        # b(98) appears three times
        self.assertEqual(module_0.split_words("bbbx"), 3)

    def test_no_delimiter_no_lower(self):
        self.assertEqual(module_0.split_words("123!@#"), 0)


if __name__ == "__main__":
    unittest.main()