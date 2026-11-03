

# Generated at 2026-11-03 01:30:50.277863
# Unit test for function vowels_count
def test_vowels_count():
    # nonce:38c591fe
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("Alone") == 3
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("aEiOu") == 5

    # Words ending in 'y' or 'Y' count as an extra vowel
    assert module_0.vowels_count("key") == 2
    assert module_0.vowels_count("keY") == 2
    assert module_0.vowels_count("bY") == 1
    assert module_0.vowels_count("ACEDY") == 3
    assert module_0.vowels_count("happy") == 2

    # 'y' not at the end is not a vowel
    assert module_0.vowels_count("yellow") == 2
    assert module_0.vowels_count("syzygy") == 1

    # No vowels present
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("xyz") == 0
    assert module_0.vowels_count("1234!@#") == 0

    # Single characters
    assert module_0.vowels_count("a") == 1
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("b") == 0

# Generated at 2026-11-03 01:32:20.383435
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2        # a, e
    assert module_0.vowels_count("Alone") == 3        # A, o, e
    assert module_0.vowels_count("hello") == 2        # e, o
    assert module_0.vowels_count("AEIOU") == 5        # all uppercase vowels
    assert module_0.vowels_count("aeiou") == 5        # all lowercase vowels

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("xyz") == 0          # y only counts at the end

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("key") == 2          # e + y
    assert module_0.vowels_count("keY") == 2          # e + Y
    assert module_0.vowels_count("ACEDY") == 3        # A, E + Y
    assert module_0.vowels_count("y") == 1            # single y
    assert module_0.vowels_count("Y") == 1            # single Y

    # 'y' not at the end does not count
    assert module_0.vowels_count("yellow") == 2       # e, o (y is not at end)
    assert module_0.vowels_count("bye") == 1          # e only

    # Mixed case and repeated vowels
    assert module_0.vowels_count("AaEeIiOoUu") == 10
    assert module_0.vowels_count("Python") == 1       # o only (n at end)

    print("All vowels_count tests passed!")


if __name__ == "__main__":
    test_vowels_count()

# Generated at 2026-11-03 01:33:44.274664
# Unit test for function vowels_count
def test_vowels_count():
    # Basic cases: count standard vowels
    assert module_0.vowels_count("abcde") == 2       # 'a' and 'e'
    assert module_0.vowels_count("hello") == 2       # 'e' and 'o'
    assert module_0.vowels_count("AEIOU") == 5       # all uppercase vowels
    assert module_0.vowels_count("aeiou") == 5       # all lowercase vowels
    assert module_0.vowels_count("aeiouAEIOU") == 10 # mixed case, all vowels

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("rhythm") == 0      # no vowels, 'y' not at end

    # Trailing 'y' / 'Y' counts as a vowel
    assert module_0.vowels_count("ACEDY") == 3       # 'A', 'E', plus trailing 'Y'
    assert module_0.vowels_count("happy") == 2       # 'a', plus trailing 'y'
    assert module_0.vowels_count("xyz") == 1         # only trailing 'y'
    assert module_0.vowels_count("XYZ") == 1         # only trailing 'Y'

    # 'y' in the middle does NOT count as a vowel
    assert module_0.vowels_count("Python") == 1      # only 'o'
    assert module_0.vowels_count("yellow") == 2      # 'e' and 'o', 'y' at start

    # Single character strings
    assert module_0.vowels_count("a") == 1
    assert module_0.vowels_count("y") == 1           # single trailing 'y'
    assert module_0.vowels_count("b") == 0

    # Strings with digits, spaces, punctuation
    assert module_0.vowels_count("a1e2i3!") == 3
    assert module_0.vowels_count(" ") == 0

    print("All tests passed!")

# Generated at 2026-11-03 01:35:04.259493
# Unit test for function vowels_count
def test_vowels_count():
    # Standard vowel counting
    assert module_0.vowels_count("abcde") == 2, "Expected 2 vowels in 'abcde'"
    assert module_0.vowels_count("Alone") == 3, "Expected 3 vowels in 'Alone'"
    assert module_0.vowels_count("hello world") == 3, "Expected 3 vowels in 'hello world'"
    assert module_0.vowels_count("AEIOU") == 5, "Expected 5 vowels in 'AEIOU'"
    assert module_0.vowels_count("aeiou") == 5, "Expected 5 vowels in 'aeiou'"

    # No vowels present
    assert module_0.vowels_count("bcdfg") == 0, "Expected 0 vowels in 'bcdfg'"
    assert module_0.vowels_count("TV") == 0, "Expected 0 vowels in 'TV'"

    # Trailing 'y'/'Y' counts as an extra vowel
    assert module_0.vowels_count("key") == 2, "'e' plus trailing 'y' -> 2"
    assert module_0.vowels_count("sky") == 1, "Only trailing 'y' -> 1"
    assert module_0.vowels_count("HAPPY") == 2, "'A' plus trailing 'Y' -> 2"
    assert module_0.vowels_count("y") == 1, "Single 'y' -> 1"
    assert module_0.vowels_count("Y") == 1, "Single 'Y' -> 1"
    assert module_0.vowels_count("xyz") == 1, "Only trailing 'y' -> 1"

    # 'y'/'Y' not at the end does not count
    assert module_0.vowels_count("bye") == 1, "'y' in middle not counted, only 'e'"
    assert module_0.vowels_count("Python") == 1, "Only 'o' counts, ends in 'n'"
    assert module_0.vowels_count("yellow") == 2, "'e' and 'o' count, 'y' at start ignored"

    # Mixed digits and punctuation
    assert module_0.vowels_count("a1e2i3") == 3, "Digits ignored, 3 vowels"
    assert module_0.vowels_count("!!!") == 0, "No vowels in punctuation"

    print("All vowels_count tests passed!")


if __name__ == "__main__":
    test_vowels_count()
# nonce:fa61c25a

# Generated at 2026-11-03 01:36:41.133217
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2          # a, e
    assert module_0.vowels_count("Alone") == 3          # A, o, e
    assert module_0.vowels_count("hello") == 2          # e, o
    assert module_0.vowels_count("AEIOU") == 5          # all uppercase vowels
    assert module_0.vowels_count("aeiou") == 5          # all lowercase vowels

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("acy") == 2            # a, y at end
    assert module_0.vowels_count("ACy") == 2            # A, y at end
    assert module_0.vowels_count("happy") == 2          # a, y at end
    assert module_0.vowels_count("y") == 1              # single 'y'
    assert module_0.vowels_count("Y") == 1              # single 'Y'

    # 'y' not at the end does not count
    assert module_0.vowels_count("yellow") == 2         # e, o (y at start ignored)
    assert module_0.vowels_count("syzygy") == 2         # y at end + first y? no: y,y,g,y -> only last y counts, plus none other -> 1... 
    # Correction: "syzygy" has vowels: y(start, ignored), y(mid, ignored), y(end, counted) = 1
    assert module_0.vowels_count("syzygy") == 1

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("xyz") == 0            # y not at end
    assert module_0.vowels_count("12345!@#") == 0

    # Mixed case and punctuation
    assert module_0.vowels_count("Hello, World!") == 3  # e, o, o
    assert module_0.vowels_count("Python Y") == 2       # o, Y at end