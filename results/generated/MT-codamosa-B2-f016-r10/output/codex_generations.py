

# Generated at 2026-11-01 20:55:44.916202
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Basic cases
    assert module_0.count_distinct_characters("") == 0
    assert module_0.count_distinct_characters("a") == 1
    assert module_0.count_distinct_characters("abc") == 3

    # Repeated characters
    assert module_0.count_distinct_characters("aaa") == 1
    assert module_0.count_distinct_characters("banana") == 3  # b, a, n

    # Case insensitivity
    assert module_0.count_distinct_characters("abcABC") == 3
    assert module_0.count_distinct_characters("Jerry jERRY JeRRRY") == 4  # j, e, r, y
    assert module_0.count_distinct_characters("aA") == 1

    # Strings with spaces and punctuation
    assert module_0.count_distinct_characters("a b c") == 4  # a, space, b, c
    assert module_0.count_distinct_characters("Hello, World!") == 10  # h, e, l, o, ',', ' ', w, r, d, '!'

    # Digits and special characters
    assert module_0.count_distinct_characters("112233!!") == 4  # 1, 2, 3, !
    assert module_0.count_distinct_characters("!@# $%^") == 7

    # Unicode characters
    assert module_0.count_distinct_characters("ñáéíóú") == 6
    assert module_0.count_distinct_characters("Ññ") == 1

    print("All tests passed!")


# Run the test
test_count_distinct_characters()

# Generated at 2026-11-01 20:56:12.328340
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Basic cases
    assert module_0.count_distinct_characters("") == 0
    assert module_0.count_distinct_characters("a") == 1
    assert module_0.count_distinct_characters("aaa") == 1

    # Case insensitivity
    assert module_0.count_distinct_characters("xyzXYZ") == 3
    assert module_0.count_distinct_characters("Jerry") == 4
    assert module_0.count_distinct_characters("AAAAaaaa") == 1
    assert module_0.count_distinct_characters("AbCdEfG") == 7

    # Mixed characters (spaces, digits, punctuation count too)
    assert module_0.count_distinct_characters("a b c") == 4
    assert module_0.count_distinct_characters("a1b2a1") == 4
    assert module_0.count_distinct_characters("Hello, World!") == 10

    # Unicode letters
    assert module_0.count_distinct_characters("Ää") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_count_distinct_characters()

# Generated at 2026-11-01 20:56:29.531820
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no distinct characters
    assert module_0.count_distinct_characters("") == 0

    # Single character
    assert module_0.count_distinct_characters("a") == 1

    # Simple distinct characters
    assert module_0.count_distinct_characters("xy") == 2
    assert module_0.count_distinct_characters("xyz") == 3

    # Case insensitivity: 'X' and 'x' count as one
    assert module_0.count_distinct_characters("xyzXYZ") == 3
    assert module_0.count_distinct_characters("AaBbCc") == 3

    # Repeated characters
    assert module_0.count_distinct_characters("aaaa") == 1

    # Mixed case word (from canonical examples)
    assert module_0.count_distinct_characters("Jerry") == 4

    # Spaces and punctuation count as distinct characters
    assert module_0.count_distinct_characters("a b c!") == 5  # {a, b, c, ' ', '!'}

    # Digits are counted as characters
    assert module_0.count_distinct_characters("abc123") == 6

    # Unicode characters are handled
    assert module_0.count_distinct_characters("éÉ") == 1

    print("All tests passed!")

# Generated at 2026-11-01 20:56:55.746680
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Nonce: 5a180fc4
    # Basic cases
    assert module_0.count_distinct_characters("") == 0
    assert module_0.count_distinct_characters("abcde") == 5
    assert module_0.count_distinct_characters("abcdecade") == 5

    # Case insensitivity check
    assert module_0.count_distinct_characters("Jerry JERRY Werry FRErRy") == 6
    assert module_0.count_distinct_characters("aAbBcC") == 3
    assert module_0.count_distinct_characters("XYxY") == 2

    # Single character and repeated identical characters
    assert module_0.count_distinct_characters("A") == 1
    assert module_0.count_distinct_characters("aaaa") == 1
    assert module_0.count_distinct_characters("zzZZ") == 1

    # Spaces and punctuation count as distinct characters
    assert module_0.count_distinct_characters("hello world!") == 9  # h,e,l,o,' ',w,r,d,!
    assert module_0.count_distinct_characters("!!!???") == 1
    assert module_0.count_distinct_characters("a b c d e") == 6     # letters + space

    # Digits mixed with letters
    assert module_0.count_distinct_characters("112233") == 1
    assert module_0.count_distinct_characters("a1b2A1B2") == 4

# Generated at 2026-11-01 20:57:22.483612
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
# nonce:e4e3ba66
    # Empty string has zero distinct characters
    assert module_0.count_distinct_characters("") == 0

    # Simple string with all unique characters
    assert module_0.count_distinct_characters("abcde") == 5

    # String with duplicate characters
    assert module_0.count_distinct_characters("abcdec") == 5
    assert module_0.count_distinct_characters("aaaa") == 1

    # Case insensitivity: uppercase and lowercase are treated the same
    assert module_0.count_distinct_characters("ABC") == 3
    assert module_0.count_distinct_characters("aA") == 1
    assert module_0.count_distinct_characters("xyzXYZ") == 3

    # Single character
    assert module_0.count_distinct_characters("x") == 1

    # String with spaces and punctuation
    assert module_0.count_distinct_characters("a b c") == 4
    assert module_0.count_distinct_characters("Hello, World!") == 10

    # Digits
    assert module_0.count_distinct_characters("12321") == 3

    # Special characters
    assert module_0.count_distinct_characters("!@#!@#") == 3

    # Unicode characters
    assert module_0.count_distinct_characters("ñáéñÁ") == 4

    print("All test cases passed!")


if __name__ == "__main__":
    test_count_distinct_characters()