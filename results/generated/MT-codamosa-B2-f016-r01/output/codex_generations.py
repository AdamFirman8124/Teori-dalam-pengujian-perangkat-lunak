

# Generated at 2026-11-02 20:05:51.559545
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no characters
    assert module_0.count_distinct_characters("") == 0

    # Same letters in different cases count once
    assert module_0.count_distinct_characters("xyzXYZ") == 3
    assert module_0.count_distinct_characters("aA") == 1

    # Classic example
    assert module_0.count_distinct_characters("Jerry") == 4

    # Repeated characters are counted once
    assert module_0.count_distinct_characters("abcabc") == 3
    assert module_0.count_distinct_characters("aaaa") == 1

    # Handles spaces, punctuation, and mixed case
    assert module_0.count_distinct_characters("Hello, World!") == 10

    # Handles digits and symbols
    assert module_0.count_distinct_characters("123!@#123") == 7

    # Case-insensitivity with mixed content
    assert module_0.count_distinct_characters("AbCaBc") == 3

    # Single character
    assert module_0.count_distinct_characters("z") == 1
    assert module_0.count_distinct_characters("Z") == 1

    # Long string with many duplicates
    assert module_0.count_distinct_characters("mississippi") == 4  # m, i, s, p

    print("All tests passed!")

# Generated at 2026-11-02 20:06:45.015998
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string
    assert module_0.count_distinct_characters("") == 0

    # String with all distinct characters
    assert module_0.count_distinct_characters("abc") == 3

    # String with repeated characters
    assert module_0.count_distinct_characters("aaa") == 1

    # Mixed characters with repeats
    assert module_0.count_distinct_characters("ababab") == 2
    assert module_0.count_distinct_characters("hello") == 4

    # Case insensitivity
    assert module_0.count_distinct_characters("AaBb") == 2
    assert module_0.count_distinct_characters("XYZxyz") == 3
    assert module_0.count_distinct_characters("Jerry jERRY JeRRRY") == 5

    # String with spaces and special characters
    assert module_0.count_distinct_characters("a b c") == 4  # a, space, b, c
    assert module_0.count_distinct_characters("!@#!@#") == 3  # !, @, #

    # Numbers and symbols
    assert module_0.count_distinct_characters("1231") == 3

    # Mixed alphanumeric
    assert module_0.count_distinct_characters("abcABC123") == 6

    # Unicode characters
    assert module_0.count_distinct_characters("éÉ") == 1

    print("All tests passed!")


test_count_distinct_characters()

# Generated at 2026-11-02 20:07:59.690323
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no distinct characters
    assert module_0.count_distinct_characters("") == 0

    # Single character
    assert module_0.count_distinct_characters("a") == 1

    # All same characters
    assert module_0.count_distinct_characters("aaaa") == 1

    # Case insensitivity: 'x', 'y', 'z'
    assert module_0.count_distinct_characters("xyzXYZ") == 3

    # Mixed case with repeats: 'j', 'e', 'r', 'y'
    assert module_0.count_distinct_characters("Jerry") == 4

    # Repeated characters in different cases
    assert module_0.count_distinct_characters("abcABC") == 3

    # Includes spaces and digits as characters
    assert module_0.count_distinct_characters("a b c 123") == 7

    # Punctuation counts as distinct characters
    assert module_0.count_distinct_characters("!!!") == 1

    # Long mixed string
    assert module_0.count_distinct_characters("Hello, World!") == 10

    print("All tests passed!")


test_count_distinct_characters()

# Generated at 2026-11-02 20:09:26.304299
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Basic cases
    assert module_0.count_distinct_characters("") == 0
    assert module_0.count_distinct_characters("a") == 1
    assert module_0.count_distinct_characters("xy") == 2
    assert module_0.count_distinct_characters("xyy") == 2

    # Case insensitivity
    assert module_0.count_distinct_characters("Aa") == 1
    assert module_0.count_distinct_characters("aAbB") == 2
    assert module_0.count_distinct_characters("Jerry") == 4
    assert module_0.count_distinct_characters("JERRY") == 4

    # Repeated characters
    assert module_0.count_distinct_characters("aaaa") == 1
    assert module_0.count_distinct_characters("abcabcabc") == 3

    # Mixed case with duplicates
    assert module_0.count_distinct_characters("Mississippi") == 4  # m, i, s, p
    assert module_0.count_distinct_characters("Hello, World!") == 10  # h,e,l,o,',',' ',w,r,d,'!'

    # Digits and special characters
    assert module_0.count_distinct_characters("123321") == 3
    assert module_0.count_distinct_characters("!@#!@#") == 2

    # Whitespace counts as a character
    assert module_0.count_distinct_characters("a b") == 3  # 'a', ' ', 'b'

    print("All tests passed!")


if __name__ == "__main__":
    test_count_distinct_characters()

# Generated at 2026-11-02 20:10:56.084999
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Case insensitivity: same letters in different cases count once
    assert module_0.count_distinct_characters('xyzXYZ') == 3
    # Repeated letters count once
    assert module_0.count_distinct_characters('Jerry') == 4
    # Empty string has zero distinct characters
    assert module_0.count_distinct_characters('') == 0
    # Single character
    assert module_0.count_distinct_characters('a') == 1
    # All identical characters
    assert module_0.count_distinct_characters('aaaaAAAA') == 1
    # Mixed case with repeats
    assert module_0.count_distinct_characters('Abcabc') == 3
    # Digits and symbols are characters too
    assert module_0.count_distinct_characters('aA1!a1') == 4
    # Uppercase and lowercase mixed
    assert module_0.count_distinct_characters('MiXeDcAsE') == 9

    print("All tests passed!")


if __name__ == "__main__":
    test_count_distinct_characters()