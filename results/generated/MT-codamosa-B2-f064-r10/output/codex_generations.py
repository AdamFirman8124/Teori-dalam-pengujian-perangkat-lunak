

# Generated at 2026-11-02 08:16:58.342249
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting (case-insensitive)
    assert module_0.vowels_count("abcde") == 2          # a, e
    assert module_0.vowels_count("Alone") == 3          # A, o, e
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AbEcIdOfUx") == 5

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("acy") == 2            # a + y
    assert module_0.vowels_count("acY") == 2            # a + Y
    assert module_0.vowels_count("my") == 1             # just y
    assert module_0.vowels_count("Y") == 1              # just Y

    # 'y' not at the end does not count as a vowel
    assert module_0.vowels_count("yellow") == 2         # e, o
    assert module_0.vowels_count("yay") == 2            # a + final y
    assert module_0.vowels_count("y") == 1              # y alone is last char

    # No vowels present
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("rhythm") == 0         # y not at end

    # Mixed content
    assert module_0.vowels_count("hello world") == 3    # e, o, o
    assert module_0.vowels_count("Python") == 2         # o + y
    assert module_0.vowels_count("a1e!i") == 3          # ignores non-letters

    # Repeated vowels
    assert module_0.vowels_count("aaa") == 3
    assert module_0.vowels_count("EEEeee") == 6

# Generated at 2026-11-02 08:18:47.993163
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2  # a, e
    assert module_0.vowels_count("ABCDE") == 2  # case insensitive
    assert module_0.vowels_count("ACEDY") == 3  # A, E + Y at end
    assert module_0.vowels_count("Alone") == 3  # A, o, e

    # 'y'/'Y' at the end counts as an extra vowel
    assert module_0.vowels_count("hey") == 2    # e + y
    assert module_0.vowels_count("busy") == 2   # u + y
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("EASY") == 3   # E, A + Y

    # 'y'/'Y' NOT at the end does not count
    assert module_0.vowels_count("yellow") == 2  # e, o
    assert module_0.vowels_count("myth") == 0

    # No vowels / non-letter characters
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("12345") == 0
    assert module_0.vowels_count("Hello, World!") == 2  # e, o

    # Mixed case and repeats
    assert module_0.vowels_count("AbE") == 2
    assert module_0.vowels_count("aeiouAEIOU") == 10

    print("All vowels_count tests passed!")


test_vowels_count()

# Generated at 2026-11-02 08:19:46.110715
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2, "Expected 2 vowels in 'abcde'"
    assert module_0.vowels_count("Alone") == 3, "Expected 3 vowels in 'Alone'"
    assert module_0.vowels_count("hello world") == 3, "Expected 3 vowels in 'hello world'"
    
    # No vowels
    assert module_0.vowels_count("bcdfg") == 0, "Expected 0 vowels in 'bcdfg'"
    assert module_0.vowels_count("rhythm") == 0, "Expected 0 vowels in 'rhythm'"
    
    # Ends with 'y' or 'Y' — counts as vowel
    assert module_0.vowels_count("key") == 2, "'e' plus ending 'y' should give 2"
    assert module_0.vowels_count("keY") == 2, "'e' plus ending 'Y' should give 2"
    assert module_0.vowels_count("happy") == 2, "'a' plus ending 'y' should give 2"
    assert module_0.vowels_count("HAPPY") == 2, "'A' plus ending 'Y' should give 2"
    assert module_0.vowels_count("y") == 1, "Single 'y' should count as 1"
    assert module_0.vowels_count("Y") == 1, "Single 'Y' should count as 1"
    assert module_0.vowels_count("xyz") == 1, "Ending 'y' only should give 1"
    
    # 'y' not at end should not count
    assert module_0.vowels_count("yellow") == 2, "'y' at start should not count"
    assert module_0.vowels_count("beyond") == 2, "internal 'y' should not count"
    
    # Uppercase and lowercase vowels
    assert module_0.vowels_count("aeiou") == 5, "All lowercase vowels"
    assert module_0.vowels_count("AEIOU") == 5, "All uppercase vowels"
    assert module_0.vowels_count("aEiOu") == 5, "Mixed case vowels"
    
    # Repeated vowels
    assert module_0.vowels_count("aaa") == 3, "Repeated vowels should each count"
    
    # Single characters
    assert module_0.vowels_count("a") == 1
    assert module_0.vowels_count("b") == 0
    
    # Digits, punctuation, spaces
    assert module_0.vowels_count("a1b2c!") == 1, "Non-letters should be ignored"
    assert module_0.vowels_count("   ") == 0, "Whitespace only has no vowels"
    
    # Empty string raises IndexError (s[-1] fails)
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass


# Run tests
if __name__ == "__main__":
    test_vowels_count()
    print("All tests passed!")

# Generated at 2026-11-02 08:20:17.205097
# Unit test for function vowels_count
def test_vowels_count():
    # Basic cases
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("Alone") == 3
    assert module_0.vowels_count("key") == 2  # 'e' + trailing 'y'
    assert module_0.vowels_count("bY") == 1   # trailing 'Y'
    assert module_0.vowels_count("aked") == 2
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("12345!@#") == 0

    # All vowels, mixed case
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aEiOu") == 5

    # Ends with 'y'/'Y' with other vowels present
    assert module_0.vowels_count("happy") == 2   # 'a' + trailing 'y'
    assert module_0.vowels_count("HAPPY") == 2   # 'A' + trailing 'Y'
    assert module_0.vowels_count("busy") == 2    # 'u' + trailing 'y'

    # 'y' in the middle does not count
    assert module_0.vowels_count("yellow") == 2  # 'e', 'o'
    assert module_0.vowels_count("syntax") == 2  # 'a' + trailing... no, 'a' only? 'a' + trailing 'x' -> 1
    # correction:
    assert module_0.vowels_count("syntax") == 1

    # Repeated vowels
    assert module_0.vowels_count("aaa") == 3

    # Empty string raises IndexError (s[-1] fails)
    with pytest.raises(IndexError):
        module_0.vowels_count("")

# Generated at 2026-11-02 08:20:54.742018
# Unit test for function vowels_count
def test_vowels_count():# Basic cases
    assert module_0.vowels_count("abcde") == 2, "Expected 2 vowels in 'abcde'"
    assert module_0.vowels_count("ACEDY") == 3, "Expected 3 vowels in 'ACEDY'"
    assert module_0.vowels_count("Alone") == 3, "Expected 3 vowels in 'Alone'"

    # Ending in 'y' / 'Y' counts as an extra vowel
    assert module_0.vowels_count("happy") == 2, "Expected 2 vowels in 'happy'"
    assert module_0.vowels_count("my") == 1, "Expected 1 vowel in 'my'"
    assert module_0.vowels_count("busy") == 2, "Expected 2 vowels in 'busy'"
    assert module_0.vowels_count("SKY") == 1, "Expected 1 vowel in 'SKY'"
    assert module_0.vowels_count("y") == 1, "Expected 1 vowel in 'y'"
    assert module_0.vowels_count("Y") == 1, "Expected 1 vowel in 'Y'"

    # 'y' in middle or start should NOT be counted
    assert module_0.vowels_count("yellow") == 2, "Expected 2 vowels in 'yellow'"
    assert module_0.vowels_count("syzygy") == 1, "Expected 1 vowel in 'syzygy'"

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0, "Expected 0 vowels in 'bcdfg'"
    assert module_0.vowels_count("h3llo w0rld!") == 1, "Expected 1 vowel in 'h3llo w0rld!'"

    # All vowels, both cases
    assert module_0.vowels_count("aeiou") == 5, "Expected 5 vowels in 'aeiou'"
    assert module_0.vowels_count("AEIOU") == 5, "Expected 5 vowels in 'AEIOU'"
    assert module_0.vowels_count("aEiOu") == 5, "Expected 5 vowels in 'aEiOu'"

    # Repeated vowels
    assert module_0.vowels_count("aaa") == 3, "Expected 3 vowels in 'aaa'"
    assert module_0.vowels_count("queueing") == 5, "Expected 5 vowels in 'queueing'"

    # Mixed case with trailing Y
    assert module_0.vowels_count("AbEcIdY") == 4, "Expected 4 vowels in 'AbEcIdY'"

    # Empty string raises IndexError (s[-1] on empty string)
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass

test_vowels_count()