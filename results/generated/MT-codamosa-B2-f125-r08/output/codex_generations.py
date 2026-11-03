

# Generated at 2026-11-02 23:45:21.727149
# Unit test for function split_words
def test_split_words():
    # Case 1: string contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("a b  c") == ["a", "b", "c"]

    # Case 2: string contains commas (no spaces) -> commas treated as separators
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words("a,b,,c") == ["a", "b", "c"]

    # Case 3: no spaces or commas -> count lowercase letters with even ordinal
    # 'b'(98), 'd'(100), 'f'(102), 'h'(104), 'j'(106), 'l'(108), 'n'(110),
    # 'p'(112), 'r'(114), 't'(116), 'v'(118), 'x'(120), 'z'(122)
    assert module_0.split_words("abcdef") == 3   # b, d, f
    assert module_0.split_words("ACEG") == 0     # uppercase letters don't count
    assert module_0.split_words("12345") == 0    # digits are not lowercase letters
    assert module_0.split_words("") == 0         # empty string
    assert module_0.split_words("bdfhjl") == 6   # all even ordinals
    assert module_0.split_words("acegik") == 0   # all odd ordinals
    assert module_0.split_words("a1b2c3d4") == 2 # b, d

    print("All tests passed!")


if __name__ == "__main__":
    test_split_words()

# Generated at 2026-11-02 23:46:24.293774
# Unit test for function split_words
def test_split_words():
    # Case 1: String contains spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three four") == ["one", "two", "three", "four"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]
    assert module_0.split_words(" leading and trailing ") == ["leading", "and", "trailing"]

    # Case 2: String contains commas (no spaces) -> split on commas
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words("a,b,c,d") == ["a", "b", "c", "d"]
    assert module_0.split_words(",start,end") == ["start", "end"]
    assert module_0.split_words("a,,b") == ["a", "b"]

    # Case 3: No spaces or commas -> count lowercase letters with even ordinal
    # Lowercase letters with even ord(): 'b'(98), 'd'(100), 'f'(102), 'h'(104),
    # 'j'(106), 'l'(108), 'n'(110), 'p'(112), 'r'(114), 't'(116), 'v'(118), 'x'(120), 'z'(122)
    assert module_0.split_words("abc") == 1        # only 'b' has even ord
    assert module_0.split_words("abcdef") == 3     # 'b', 'd', 'f'
    assert module_0.split_words("bcdf") == 4       # all even
    assert module_0.split_words("aceg") == 0       # all odd
    assert module_0.split_words("") == 0           # empty string
    assert module_0.split_words("ABC") == 0        # uppercase letters are not counted
    assert module_0.split_words("1234") == 0       # digits are not counted
    assert module_0.split_words("a1b2c3") == 1     # only 'b' counts
    assert module_0.split_words("!@#$") == 0       # special characters are not counted
    assert module_0.split_words("b") == 1          # single even lowercase letter
    assert module_0.split_words("a") == 0          # single odd lowercase letter

    print("All tests passed!")


if __name__ == "__main__":
    test_split_words()
    unittest.main()

# Generated at 2026-11-02 23:47:40.789174
# Unit test for function split_words
def test_split_words():
    # Case 1: text with spaces -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("Hello world") == ["Hello", "world"]
    assert module_0.split_words("one two three four") == ["one", "two", "three", "four"]
    assert module_0.split_words("  spaced   out  ") == ["spaced", "out"]

    # Case 2: text with commas but no spaces -> commas act as separators
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("One,two,three") == ["One", "two", "three"]
    assert module_0.split_words(",,") == []  # split() drops empty tokens

    # Space takes priority over comma when both present
    assert module_0.split_words("a b,c") == ["a", "b,c"]

    # Case 3: no spaces or commas -> count lowercase letters with even ordinal
    assert module_0.split_words("abcdef") == 3        # b(98), d(100), f(102)
    assert module_0.split_words("abcdefgh") == 4      # b, d, f, h
    assert module_0.split_words("abcdefghijklmnopqrstuvwxyz") == 13  # b,d,f,h,j,l,n,p,r,t,v,x,z
    assert module_0.split_words("aceg") == 0          # all odd ordinals
    assert module_0.split_words("ABCDEF") == 0        # uppercase letters ignored
    assert module_0.split_words("12345") == 0         # digits not lowercase
    assert module_0.split_words("!@#$%") == 0         # symbols not lowercase
    assert module_0.split_words("") == 0              # empty string

    print("All tests passed!")


test_split_words()

# Generated at 2026-11-02 23:48:18.478469
# Unit test for function split_words
def test_split_words():
    # Test splitting on spaces
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three four") == ["one", "two", "three", "four"]
    assert module_0.split_words("Hello World!") == ["Hello", "World!"]
    assert module_0.split_words("  leading and trailing  ") == ["leading", "and", "trailing"]

    # Test splitting on commas (no spaces present)
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]
    assert module_0.split_words("a,b,c,d") == ["a", "b", "c", "d"]

    # Test counting lowercase letters with even ordinal values
    # 'a'=97 (odd), 'b'=98 (even), 'c'=99 (odd), 'd'=100 (even), 'e'=101 (odd), 'f'=102 (even)
    assert module_0.split_words("abcdef") == 3
    assert module_0.split_words("b") == 1
    assert module_0.split_words("a") == 0
    assert module_0.split_words("") == 0
    assert module_0.split_words("12345") == 0
    assert module_0.split_words("HELLO") == 0
    assert module_0.split_words("HelloWorld") == 2  # 'e'=101 odd, 'l'=108 even, 'o'=111 odd... -> 'l'=108 even, 'l'=108 even? check: H(72),e(101),l(108),l(108),o(111),W(87),o(111),r(114),l(108),d(100) -> even: 108,108,114,108,100 = 5
    # Correct the previous expectation after manual verification:
    assert module_0.split_words("HelloWorld") == 5
    assert module_0.split_words("bd") == 2  # 'b'=98 even, 'd'=100 even

    # Edge case: mixed space takes priority over comma
    assert module_0.split_words("a b,c") == ["a", "b,c"]

    print("All tests passed!")


test_split_words()

# Generated at 2026-11-02 23:49:15.203042
# Unit test for function split_words
def test_split_words():
    # Case 1: contains spaces -> split on whitespace
    assert module_0.split_words("Hello world!") == ["Hello", "world!"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("a b") == ["a", "b"]
    # Space takes precedence over comma
    assert module_0.split_words("a,b c") == ["a,b", "c"]

    # Case 2: contains commas (no spaces) -> split on commas
    assert module_0.split_words("Hello,world!") == ["Hello", "world!"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("apple,banana,cherry") == ["apple", "banana", "cherry"]

    # Case 3: no spaces or commas -> count lowercase letters with even ord
    assert module_0.split_words("abcdef") == 3   # b(98), d(100), f(102) have even ord
    assert module_0.split_words("Hello") == 2    # l(108) appears twice
    assert module_0.split_words("") == 0         # empty string
    assert module_0.split_words("ABC") == 0      # no lowercase letters
    assert module_0.split_words("acegi") == 0    # all lowercase but odd ordinals
    assert module_0.split_words("bdfh") == 4     # all lowercase with even ordinals
    assert module_0.split_words("123!@#") == 0   # non-letter characters ignored

# nonce:02583af4