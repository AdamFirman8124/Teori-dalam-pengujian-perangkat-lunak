

# Generated at 2026-11-02 23:14:14.142790
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string
    assert module_0.count_distinct_characters("") == 0

    # Single character
    assert module_0.count_distinct_characters("a") == 1

    # Basic distinct characters
    assert module_0.count_distinct_characters("abc") == 3
    assert module_0.count_distinct_characters("abcdef") == 6

    # Repeated characters
    assert module_0.count_distinct_characters("aaaa") == 1
    assert module_0.count_distinct_characters("banana") == 3  # b, a, n
    assert module_0.count_distinct_characters("hello") == 4   # h, e, l, o
    assert module_0.count_distinct_characters("Jerry") == 4   # j, e, r, y

    # Case insensitivity
    assert module_0.count_distinct_characters("Aa") == 1
    assert module_0.count_distinct_characters("aAaA") == 1
    assert module_0.count_distinct_characters("AbC") == 3
    assert module_0.count_distinct_characters("xyzXYZ") == 3
    assert module_0.count_distinct_characters("HeLLo") == 4

    # Strings with spaces
    assert module_0.count_distinct_characters("a b c") == 4   # a, ' ', b, c
    assert module_0.count_distinct_characters("   ") == 1     # only spaces

    # Strings with digits and special characters
    assert module_0.count_distinct_characters("12345") == 5
    assert module_0.count_distinct_characters("!@#$%") == 5
    assert module_0.count_distinct_characters("1122!!") == 3  # 1, 2, !

    # Mixed alphanumeric and symbols
    assert module_0.count_distinct_characters("aA1!") == 3    # a, 1, !
    assert module_0.count_distinct_characters("Hello, World!") == 10

    print("All tests passed!")


test_count_distinct_characters()

# Generated at 2026-11-02 23:16:42.005906
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    assert module_0.count_distinct_characters('') == 0
    assert module_0.count_distinct_characters('abc') == 3
    assert module_0.count_distinct_characters('aaaa') == 1
    assert module_0.count_distinct_characters('xyzXYZ') == 3
    assert module_0.count_distinct_characters('Jerry') == 4
    assert module_0.count_distinct_characters('abcde') == 5
    assert module_0.count_distinct_characters('aAbBcC') == 3
    assert module_0.count_distinct_characters('hello world') == 8
    assert module_0.count_distinct_characters('123321') == 3
    assert module_0.count_distinct_characters('!@#!@#') == 3
    assert module_0.count_distinct_characters('AlphaBeta') == 7

# Generated at 2026-11-02 23:19:15.660901
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no distinct characters
    assert module_0.count_distinct_characters("") == 0

    # Single character
    assert module_0.count_distinct_characters("a") == 1

    # All unique characters
    assert module_0.count_distinct_characters("abc") == 3

    # Repeated identical characters count once
    assert module_0.count_distinct_characters("aaaa") == 1

    # Case insensitivity: upper and lower count as the same character
    assert module_0.count_distinct_characters("AaBbCc") == 3
    assert module_0.count_distinct_characters("xyzXYZ") == 3

    # Mixed letters with duplicates
    assert module_0.count_distinct_characters("Jerry") == 4  # j, e, r, y
    assert module_0.count_distinct_characters("Jerry jerry") == 5  # j, e, r, y, space

    # Spaces and punctuation are counted as characters
    assert module_0.count_distinct_characters("abc def") == 7  # a, b, c, space, d, e, f

    # Digits and special characters
    assert module_0.count_distinct_characters("a1!a1!") == 3  # a, 1, !

    # Unicode characters are handled (case-folded where applicable)
    assert module_0.count_distinct_characters("ÅÄÖåäö") == 3

# Generated at 2026-11-02 23:20:34.148248
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Test with empty string
    assert module_0.count_distinct_characters("") == 0

    # Test with simple string, all unique characters
    assert module_0.count_distinct_characters("abcde") == 5

    # Test with repeated characters
    assert module_0.count_distinct_characters("abcdea") == 5

    # Test case insensitivity (mixed case should be counted once)
    assert module_0.count_distinct_characters("abcdeA") == 5
    assert module_0.count_distinct_characters("aAaA") == 1

    # Test with spaces and repeated characters
    assert module_0.count_distinct_characters("Jerry jerry Jerry") == 5  # j, e, r, y, space
    assert module_0.count_distinct_characters("xyXXXXX yyy") == 4  # x, y, space

    # Test with digits and special characters
    assert module_0.count_distinct_characters("a1b2c3!@#") == 9
    assert module_0.count_distinct_characters("!!!") == 1

    # Test with single character
    assert module_0.count_distinct_characters("z") == 1
    assert module_0.count_distinct_characters("Z") == 1

    # Test with numbers only
    assert module_0.count_distinct_characters("112233") == 3

    # Test with mixed alphanumeric and symbols
    assert module_0.count_distinct_characters("Hello, World!") == 10  # h,e,l,o,',',space,w,r,d,! -> 10

    print("All tests passed!")


if __name__ == "__main__":
    test_count_distinct_characters()