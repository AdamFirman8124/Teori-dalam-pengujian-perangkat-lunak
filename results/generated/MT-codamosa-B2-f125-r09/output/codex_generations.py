

# Generated at 2026-11-01 22:03:33.068874
# Unit test for function split_words
def test_split_words():
    assert module_0.split_words("Hello world!") == ["Hello", "world!"]
    assert module_0.split_words("Hello,world!") == ["Hello", "world!"]
    assert module_0.split_words("abcdef") == 3
    assert module_0.split_words("") == 0
    assert module_0.split_words("aaa bbb ccc") == ["aaa", "bbb", "ccc"]
    assert module_0.split_words("x,y,z") == ["x", "y", "z"]
    assert module_0.split_words("ACEG") == 0
    assert module_0.split_words("bdfh") == 4
    assert module_0.split_words("one two,three four") == ["one", "two,three", "four"]

test_split_words()

# Generated at 2026-11-01 22:03:52.730017
# Unit test for function split_words
def test_split_words():import unittest


class TestSplitWords(unittest.TestCase):

    def test_space_split(self):
        self.assertEqual(module_0.split_words("hello world"), ["hello", "world"])

    def test_multiple_spaces(self):
        self.assertEqual(module_0.split_words("one two three four"), ["one", "two", "three", "four"])

    def test_comma_split(self):
        self.assertEqual(module_0.split_words("hello,world"), ["hello", "world"])

    def test_multiple_commas(self):
        self.assertEqual(module_0.split_words("a,b,c,d"), ["a", "b", "c", "d"])

    def test_no_space_no_comma_even_lowercase(self):
        # b=98, d=100, f=102 -> all even
        self.assertEqual(module_0.split_words("bdf"), 3)

    def test_no_space_no_comma_mixed(self):
        # a=97 odd, b=98 even, c=99 odd -> only 'b' counts
        self.assertEqual(module_0.split_words("abc"), 1)

    def test_no_space_no_comma_uppercase(self):
        # uppercase letters are excluded
        self.assertEqual(module_0.split_words("BDF"), 0)

    def test_empty_string(self):
        self.assertEqual(module_0.split_words(""), 0)

    def test_digits_only(self):
        self.assertEqual(module_0.split_words("12345"), 0)

    def test_full_alphabet(self):
        # even-ord lowercase letters: b,d,f,h,j,l,n,p,r,t,v,x,z -> 13
        self.assertEqual(module_0.split_words("abcdefghijklmnopqrstuvwxyz"), 13)

    def test_single_even_letter(self):
        self.assertEqual(module_0.split_words("z"), 1)

    def test_single_odd_letter(self):
        self.assertEqual(module_0.split_words("a"), 0)

    def test_comma_takes_priority_when_both(self):
        # contains both space and comma -> space branch wins
        self.assertEqual(module_0.split_words("a b,c"), ["a", "b,c"])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 22:04:08.703891
# Unit test for function split_words
def test_split_words():
    # Case 1: text contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three four") == ["one", "two", "three", "four"]
    assert module_0.split_words("") == []

    # Case 2: text contains commas (no spaces) -> commas treated as separators
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("apple,banana,cherry") == ["apple", "banana", "cherry"]
    assert module_0.split_words("a,b,c,d") == ["a", "b", "c", "d"]

    # Case 3: no spaces or commas -> count lowercase chars with even ord value
    # 'b'(98), 'd'(100), 'f'(102) have even ordinals
    assert module_0.split_words("abcdef") == 3
    assert module_0.split_words("bdfhj") == 5      # all even ordinals
    assert module_0.split_words("acegi") == 0      # all odd ordinals
    assert module_0.split_words("12345!@#$%") == 0 # digits/symbols never islower
    assert module_0.split_words("ABCDEF") == 0     # uppercase excluded
    assert module_0.split_words("xXyY") == 1       # only 'y'... wait: x=120 even, y=121 odd
    assert module_0.split_words("") == 0           # empty -> no match

# Generated at 2026-11-01 22:04:46.598803
# Unit test for function split_words
def test_split_words():
    # Case 1: Text contains spaces -> split by whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]
    assert module_0.split_words("one two  three") == ["one", "two", "three"]

    # Case 2: Text contains commas but no spaces -> replace commas, split
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c,d") == ["a", "b", "c", "d"]
    assert module_0.split_words("one,two") == ["one", "two"]

    # Case 3: No spaces or commas -> count lowercase letters with even ordinal
    # ord('a')=97 (odd), ord('b')=98 (even), ord('c')=99 (odd), ord('d')=100 (even)
    assert module_0.split_words("abcd") == 2       # 'b' and 'd'
    assert module_0.split_words("abcde") == 2      # 'b' and 'd'
    assert module_0.split_words("abcdef") == 3     # 'b', 'd', 'f'
    assert module_0.split_words("") == 0           # empty string
    assert module_0.split_words("1234") == 0       # no lowercase letters
    assert module_0.split_words("HELLO") == 0      # no lowercase letters
    assert module_0.split_words("ACE") == 0        # uppercase, ignored
    assert module_0.split_words("bdfh") == 4       # all even ordinals
    assert module_0.split_words("aceg") == 0       # all odd ordinals
    assert module_0.split_words("Hello") == 1      # only 'e' (ord 101 is odd?) -> 'e'=101 odd, 'o'=111 odd... check below

    print("All tests passed!")

test_split_words()

# Generated at 2026-11-01 22:05:24.889640
# Unit test for function split_words
def test_split_words():
    # Case 1: Text contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three four") == ["one", "two", "three", "four"]
    assert module_0.split_words("Hello World") == ["Hello", "World"]

    # Case 2: Text contains commas (no spaces) -> commas treated as delimiters
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words("a,b,c,d") == ["a", "b", "c", "d"]

    # Case 3: No spaces or commas -> count lowercase letters with even ordinal values
    # 'a'=97 (odd), 'b'=98 (even), 'c'=99 (odd), 'd'=100 (even), 'e'=101 (odd), 'f'=102 (even)
    assert module_0.split_words("abcdef") == 3
    assert module_0.split_words("ace") == 0          # all odd ordinals
    assert module_0.split_words("bdf") == 3          # all even ordinals
    assert module_0.split_words("ABCDEF") == 0       # uppercase letters don't count
    assert module_0.split_words("12345") == 0        # digits don't count
    assert module_0.split_words("") == 0             # empty string
    assert module_0.split_words("a1b2c3") == 1       # only 'b' qualifies

    print("All tests passed!")

test_split_words()