

# Generated at 2026-11-01 20:10:48.873617
# Unit test for function split_words
def test_split_words():
    # Whitespace splitting
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  spaced   out  ") == ["spaced", "out"]

    # Space takes priority over comma
    assert module_0.split_words("hello world,foo") == ["hello", "world,foo"]

    # Comma splitting
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words(",leading,trailing,") == ["leading", "trailing"]

    # Counting lowercase letters with even ordinal values
    assert module_0.split_words("abcdef") == 3      # b(98), d(100), f(102)
    assert module_0.split_words("bdfh") == 4        # all even ordinals
    assert module_0.split_words("aceg") == 0        # all odd ordinals
    assert module_0.split_words("ABC") == 0         # uppercase ignored
    assert module_0.split_words("") == 0            # empty string
    assert module_0.split_words("123!@#") == 0      # no lowercase letters
    assert module_0.split_words("z") == 0           # z is 122 (even) -> wait, 122 % 2 == 0
    assert module_0.split_words("z") == 1           # z(122) is even

# Generated at 2026-11-01 20:11:15.090376
# Unit test for function split_words
def test_split_words():
    # Test splitting on spaces
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three four") == ["one", "two", "three", "four"]

    # Test splitting on commas (space takes precedence)
    assert module_0.split_words("hello,world,dog") == ["hello", "world", "dog"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]

    # Test counting lowercase letters with even ordinal values
    # 'b'=98, 'd'=100, 'f'=102 are even; 'a'=97, 'c'=99 are odd
    assert module_0.split_words("abcdef") == 3      # b, d, f
    assert module_0.split_words("aceg") == 0        # all odd ordinals
    assert module_0.split_words("bdfh") == 4        # all even ordinals
    assert module_0.split_words("") == 0            # empty string
    assert module_0.split_words("1234!@#$") == 0    # no lowercase letters
    assert module_0.split_words("HELLO WORLD") == 0  # uppercase only

    print("All tests passed!")


if __name__ == "__main__":
    test_split_words()

# Generated at 2026-11-01 20:11:30.855905
# Unit test for function split_words
def test_split_words():
    # Words separated by spaces -> list of words
    assert module_0.split_words("Hello World") == ["Hello", "World"]

    # Words separated by commas -> commas treated as separators
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]

    # No spaces or commas -> count of lowercase chars with even ordinal
    assert module_0.split_words("abcdef") == 3      # 'b'(98), 'd'(100), 'f'(102) are even
    assert module_0.split_words("aaaa") == 0        # 'a'(97) is odd
    assert module_0.split_words("BBBB") == 0        # uppercase ignored
    assert module_0.split_words("zzzz") == 4        # 'z'(122) is even
    assert module_0.split_words("") == 0            # empty string

    # Mixed digits/symbols without separators
    assert module_0.split_words("123!@#bd") == 2    # only 'b' and 'd' count

# Generated at 2026-11-01 20:11:53.079296
# Unit test for function split_words
def test_split_words():
    # Case 1: text with spaces should split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("Hello World Foo") == ["Hello", "World", "Foo"]
    assert module_0.split_words("  leading and trailing  ") == ["leading", "and", "trailing"]

    # Case 2: text with commas (no spaces) should split on commas
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words("a,b,c,d") == ["a", "b", "c", "d"]
    assert module_0.split_words("comma,only") == ["comma", "only"]

    # Case 3: no spaces or commas -> count lowercase chars with even ord
    # 'b'=98, 'd'=100, 'f'=102 are even; 'a'=97, 'c'=99, 'e'=101 are odd
    assert module_0.split_words("abcdef") == 3
    assert module_0.split_words("bdf") == 3
    assert module_0.split_words("ace") == 0
    assert module_0.split_words("Hello") == 0  # 'e'=101 odd, 'l'=108 even, 'l'=108 even, 'o'=111 odd -> wait
    # Recheck: H(72 upper), e(101 odd), l(108 even), l(108 even) -> 2
    assert module_0.split_words("Hello") == 2
    assert module_0.split_words("") == 0
    assert module_0.split_words("12345!@#") == 0
    assert module_0.split_words("z") == 0  # 'z'=122 even but is one char -> 1

    # Edge: single lowercase char with even ord
    assert module_0.split_words("b") == 1
    assert module_0.split_words("a") == 0

    # Mixed: space takes priority over comma
    assert module_0.split_words("a,b c") == ["a,b", "c"]

    print("All tests passed!")


test_split_words()

# Generated at 2026-11-01 20:12:26.548054
# Unit test for function split_words
def test_split_words():
    # Case 1: text containing spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  multiple   spaces  ") == ["multiple", "spaces"]

    # Case 2: no spaces but contains commas -> commas treated as delimiters
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words("a,b,,c") == ["a", "b", "", "c"]

    # Case 3: no spaces or commas -> count lowercase letters with even ord
    # 'b' (98), 'd' (100), 'f' (102) are lowercase with even ord values
    assert module_0.split_words("abcdef") == 3
    assert module_0.split_words("abc") == 1          # only 'b'
    assert module_0.split_words("ACE") == 0          # no lowercase letters
    assert module_0.split_words("") == 0             # empty string
    assert module_0.split_words("b1b!") == 2         # only lowercase 'b' chars count
    assert module_0.split_words("hello") == 2        # 'h'(104) and 'l'(108) are even

    print("All tests passed!")


test_split_words()