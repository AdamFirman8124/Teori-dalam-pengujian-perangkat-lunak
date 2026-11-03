

# Generated at 2026-11-03 00:27:21.402767
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Test with all distinct characters
    assert module_0.count_distinct_characters("abc") == 3
    
    # Test with repeated characters
    assert module_0.count_distinct_characters("aabbcc") == 3
    
    # Test with mixed case (should be case-insensitive)
    assert module_0.count_distinct_characters("AaBb") == 2
    
    # Test with empty string
    assert module_0.count_distinct_characters("") == 0
    
    # Test with single character
    assert module_0.count_distinct_characters("x") == 1
    
    # Test with spaces and punctuation
    assert module_0.count_distinct_characters("a b!a") == 4  # a, space, b, !
    
    # Test with numbers
    assert module_0.count_distinct_characters("1122") == 2
    
    # Test longer string with mixed case and duplicates
    assert module_0.count_distinct_characters("Hello World") == 8  # h,e,l,o,space,w,r,d
    
    print("All tests passed!")


# Run the test
test_count_distinct_characters()

# Generated at 2026-11-03 00:28:30.853895
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no distinct characters
    assert module_0.count_distinct_characters("") == 0

    # All distinct characters
    assert module_0.count_distinct_characters("abcde") == 5

    # Duplicated characters are counted once
    assert module_0.count_distinct_characters("abcabc") == 3

    # Case insensitivity: 'A' and 'a' are the same character
    assert module_0.count_distinct_characters("abcAa") == 3
    assert module_0.count_distinct_characters("AAAaaa") == 1
    assert module_0.count_distinct_characters("AaBbCc") == 3

    # Mixed letters and digits
    assert module_0.count_distinct_characters("a1b2c3") == 6
    assert module_0.count_distinct_characters("112233") == 3

    # Spaces count as characters
    assert module_0.count_distinct_characters("a b c") == 5  # a, b, c, space
    assert module_0.count_distinct_characters("   ") == 1

    # Punctuation and special characters
    assert module_0.count_distinct_characters("Hello, World!") == 10  # h,e,l,o,comma,space,w,r,d,!

    # Repeated pattern
    assert module_0.count_distinct_characters("xyzXYZ") == 3

    # Single character
    assert module_0.count_distinct_characters("z") == 1
    assert module_0.count_distinct_characters("Z") == 1

    # Unicode characters
    assert module_0.count_distinct_characters("éàé") == 2

    # Long repetitive string
    assert module_0.count_distinct_characters("a" * 100) == 1

    print("All tests passed!")


# Run the test
test_count_distinct_characters()

# Generated at 2026-11-03 00:29:36.573745
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no distinct characters
    assert module_0.count_distinct_characters("") == 0

    # All unique characters
    assert module_0.count_distinct_characters("xyz") == 3
    assert module_0.count_distinct_characters("abcde") == 5

    # Repeated characters are counted once
    assert module_0.count_distinct_characters("jerry") == 4
    assert module_0.count_distinct_characters("hello") == 4
    assert module_0.count_distinct_characters("aaa") == 1

    # Case insensitivity
    assert module_0.count_distinct_characters("Jerry") == 4
    assert module_0.count_distinct_characters("aA") == 1
    assert module_0.count_distinct_characters("AbCdEfF") == 6

    # Spaces and punctuation count as characters
    assert module_0.count_distinct_characters("a b c") == 5
    assert module_0.count_distinct_characters("!?!") == 2

    # Mixed case with repeats
    assert module_0.count_distinct_characters("AlphaBETA") == 7

    print("All tests passed!")


# Run the test
if __name__ == "__main__":
    test_count_distinct_characters()

# Generated at 2026-11-03 00:30:52.861364
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no distinct characters
    assert module_0.count_distinct_characters("") == 0

    # Single character
    assert module_0.count_distinct_characters("a") == 1

    # All same characters (case-insensitive)
    assert module_0.count_distinct_characters("aaaaAAAA") == 1

    # Mixed case letters count as one distinct character
    assert module_0.count_distinct_characters("xyzXYZ") == 3

    # Classic example
    assert module_0.count_distinct_characters("Jerry") == 4

    # Spaces and punctuation are counted as characters too
    assert module_0.count_distinct_characters("a b c") == 5  # a, space, b, c -> {a, ' ', b, c} = 4? no:
    # Recomputed: "a b c" -> {'a', ' ', 'b', 'c'} = 4
    assert module_0.count_distinct_characters("a b c") == 4

    # Digits and symbols are included
    assert module_0.count_distinct_characters("123!@#123") == 5

    # Case-insensitivity with full words
    assert module_0.count_distinct_characters("Hello, World!") == 10  # h,e,l,o,',',' ',w,r,d,! -> 10

    # Unicode characters
    assert module_0.count_distinct_characters("ñÑéÉ") == 2

    # Long repeated string
    assert module_0.count_distinct_characters("abcabcABC" * 100) == 3


if __name__ == "__main__":
    test_count_distinct_characters()
    print("All tests passed!")

# Generated at 2026-11-03 00:31:56.249223
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no distinct characters
    assert module_0.count_distinct_characters("") == 0

    # Single character
    assert module_0.count_distinct_characters("a") == 1

    # Repeated same character
    assert module_0.count_distinct_characters("aaaa") == 1

    # All distinct characters
    assert module_0.count_distinct_characters("abcdef") == 6

    # Repeated characters count once
    assert module_0.count_distinct_characters("abcabc") == 3

    # Case insensitivity: 'x' and 'X' are the same
    assert module_0.count_distinct_characters("xyzXYZ") == 3

    # Example from typical test cases
    assert module_0.count_distinct_characters("Jerry") == 4

    # Mixed case with repeats
    assert module_0.count_distinct_characters("aAbBcC") == 3

    # Spaces count as characters
    assert module_0.count_distinct_characters("a a") == 2

    # Digits and punctuation are characters too
    assert module_0.count_distinct_characters("1231!") == 4

    # Unicode characters
    assert module_0.count_distinct_characters("éÉé") == 1

    # Sentence with mixed content
    assert module_0.count_distinct_characters("Hello, World!") == 10  # h,e,l,o,',',space,w,r,d,!  -> h,e,l,o, ',', ' ', w, r, d, '!'

    print("All tests passed!")


if __name__ == "__main__":
    test_count_distinct_characters()