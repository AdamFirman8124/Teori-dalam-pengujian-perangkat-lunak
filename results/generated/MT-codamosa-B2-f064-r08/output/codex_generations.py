

# Generated at 2026-11-03 06:08:18.081585
# Unit test for function vowels_count
def test_vowels_count():
    # Basic lowercase vowels
    assert module_0.vowels_count("abcde") == 2, "Expected 2 vowels in 'abcde'"
    assert module_0.vowels_count("hello") == 2, "Expected 2 vowels in 'hello'"

    # Uppercase vowels
    assert module_0.vowels_count("AEIOU") == 5, "Expected 5 vowels in 'AEIOU'"
    assert module_0.vowels_count("AbCdE") == 2, "Expected 2 vowels in 'AbCdE'"

    # Mixed case vowels
    assert module_0.vowels_count("aEiOu") == 5, "Expected 5 vowels in 'aEiOu'"

    # Ending with 'y' counts as an extra vowel
    assert module_0.vowels_count("acy") == 2, "'y' at end should add 1 vowel"
    assert module_0.vowels_count("acY") == 2, "'Y' at end should add 1 vowel"
    assert module_0.vowels_count("y") == 1, "Single 'y' should count as 1"

    # 'y' not at the end should not be counted
    assert module_0.vowels_count("yellow") == 2, "'y' inside word should not count"
    assert module_0.vowels_count("syzygy") == 1, "Only trailing 'y' counts"

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0, "Expected 0 vowels in 'bcdfg'"

    # Vowels with 'y' ending and mixed case
    assert module_0.vowels_count("AbEY") == 3, "Expected 3 (A, e, trailing Y)"

    # Repeated vowels
    assert module_0.vowels_count("aaa") == 3, "Expected 3 vowels in 'aaa'"

    # Digits and symbols are not vowels
    assert module_0.vowels_count("a1e2i!") == 3, "Non-letters should be ignored"

    print("All tests passed!")

# Generated at 2026-11-03 06:10:01.289814
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2       # a, e
    assert module_0.vowels_count("ACEDY") == 3       # A, E + trailing Y
    assert module_0.vowels_count("abe") == 2         # a, e
    assert module_0.vowels_count("hello") == 2       # e, o
    assert module_0.vowels_count("bcdfgh") == 0      # no vowels
    assert module_0.vowels_count("AEIOU") == 5       # all uppercase vowels
    assert module_0.vowels_count("aeiou") == 5       # all lowercase vowels

    # Trailing 'y' / 'Y' counts as a vowel
    assert module_0.vowels_count("key") == 2         # e + y
    assert module_0.vowels_count("tY") == 1          # trailing Y
    assert module_0.vowels_count("y") == 1           # single trailing y
    assert module_0.vowels_count("Y") == 1           # single trailing Y
    assert module_0.vowels_count("aeiouy") == 6      # 5 vowels + trailing y
    assert module_0.vowels_count("xy") == 1          # only trailing y counts

    # 'y' not at the end does not count
    assert module_0.vowels_count("yellow") == 2      # e, o (y at start ignored)
    assert module_0.vowels_count("xyz") == 0         # y not at end, no vowels

    # Mixed case and repeated vowels
    assert module_0.vowels_count("AeIoUy") == 6      # 5 vowels + trailing y
    assert module_0.vowels_count("banana") == 3      # a, a, a

# Generated at 2026-11-03 06:11:40.286870
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aEiOu") == 5

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("123!@#") == 0
    assert module_0.vowels_count("rhythm") == 0

    # Mixed consonants and vowels
    assert module_0.vowels_count("Hello World") == 3
    assert module_0.vowels_count("Python") == 2  # o + trailing... no, ends with 'n'
    assert module_0.vowels_count("Programming") == 3  # o, a, i

    # Trailing 'y' or 'Y' counts as a vowel
    assert module_0.vowels_count("acy") == 2      # a + y
    assert module_0.vowels_count("abcY") == 2     # a + Y
    assert module_0.vowels_count("y") == 1        # y alone counts once
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("busy") == 2     # u + y
    assert module_0.vowels_count("BAY") == 2      # A + Y

    # 'y' not at the end does not count
    assert module_0.vowels_count("yellow") == 2   # e, o
    assert module_0.vowels_count("syzygy") == 1   # y at end only
    assert module_0.vowels_count("yay") == 2      # a + trailing y

    # Vowels followed by trailing y
    assert module_0.vowels_count("aeiouy") == 6
    assert module_0.vowels_count("aeioyY") == 6   # a,e,i,o + trailing Y

    # Whitespace and punctuation
    assert module_0.vowels_count("a b c!") == 1
    assert module_0.vowels_count("  ") == 0

    # Empty string raises IndexError (s[-1] on empty string)
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass

    print("All vowels_count tests passed!")


if __name__ == "__main__":
    test_vowels_count()

# Generated at 2026-11-03 06:13:15.952492
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("Alone") == 3      # A, o, e
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("AEIOU") == 5      # all uppercase vowels
    assert module_0.vowels_count("aeiou") == 5      # all lowercase vowels

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("key") == 2        # e, y
    assert module_0.vowels_count("keY") == 2        # e, Y
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y
    assert module_0.vowels_count("my") == 1         # y only

    # 'y' in the middle does not count as a vowel
    assert module_0.vowels_count("bye") == 1        # e only
    assert module_0.vowels_count("bYe") == 1        # e only
    assert module_0.vowels_count("yellow") == 2     # e, o

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("xyz") == 0

    # Mixed case and digits/symbols
    assert module_0.vowels_count("aEiOu1!") == 5
    assert module_0.vowels_count("1234!@#") == 0

    # Ends with y after no other vowels
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("y") == 1

# Generated at 2026-11-03 06:14:22.718157
# Unit test for function vowels_count
def test_vowels_count():
    # Basic cases with lowercase vowels
    assert module_0.vowels_count("abcde") == 2, "Expected 2 vowels in 'abcde'"
    assert module_0.vowels_count("Alone") == 3, "Expected 3 vowels in 'Alone'"

    # Uppercase vowels should be counted too
    assert module_0.vowels_count("ACEDY") == 3, "Expected 3 (A, E, and trailing Y) in 'ACEDY'"

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("happy") == 2, "Expected 2 (a + trailing y) in 'happy'"
    assert module_0.vowels_count("bY") == 1, "Expected 1 (trailing Y) in 'bY'"
    assert module_0.vowels_count("y") == 1, "Expected 1 for single 'y'"

    # 'y' in the middle does not count as a vowel
    assert module_0.vowels_count("yellow") == 2, "Expected 2 (e, o) in 'yellow'"
    assert module_0.vowels_count("syzygy") == 1, "Expected 1 (trailing y) in 'syzygy'"

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0, "Expected 0 vowels in 'bcdfg'"

    # Mixed case vowels
    assert module_0.vowels_count("AbEcEdY") == 4, "Expected 4 (A, E, E, trailing Y) in 'AbEcEdY'"

    # String ending with 'Y' after other vowels
    assert module_0.vowels_count("KEY") == 2, "Expected 2 (E + trailing Y) in 'KEY'"

    # Vowels with digits/symbols around
    assert module_0.vowels_count("a1e2i3o4u5") == 5, "Expected 5 vowels in 'a1e2i3o4u5'"

    # Repeated vowels
    assert module_0.vowels_count("aaaa") == 4, "Expected 4 vowels in 'aaaa'"