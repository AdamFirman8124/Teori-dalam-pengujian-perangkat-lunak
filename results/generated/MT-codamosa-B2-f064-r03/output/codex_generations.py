

# Generated at 2026-11-02 10:12:53.107674
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2          # 'a', 'e'
    assert module_0.vowels_count("hello") == 2          # 'e', 'o'
    assert module_0.vowels_count("Alone") == 3          # 'A', 'o', 'e'

    # All vowels, both cases
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aEiOu") == 5

    # Trailing 'y'/'Y' counts as an extra vowel
    assert module_0.vowels_count("ACEDY") == 3          # 'A', 'E' + trailing 'Y'
    assert module_0.vowels_count("xyz") == 1            # only trailing 'y'
    assert module_0.vowels_count("happy") == 2          # 'a' + trailing 'y'
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1

    # Non-trailing 'y'/'Y' is not counted
    assert module_0.vowels_count("yellow") == 2         # 'e', 'o'
    assert module_0.vowels_count("Yoyo") == 2           # 'o', 'o'
    assert module_0.vowels_count("rhythm") == 0         # internal 'y' ignored, no trailing 'y'

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0

    # Digits, spaces, and punctuation are ignored
    assert module_0.vowels_count("a1e2i3") == 3
    assert module_0.vowels_count("Hello, World!") == 3  # 'e', 'o', 'o'


def test_vowels_count_empty_string():
    # Empty string has no last character, so an IndexError is raised
    with pytest.raises(IndexError):
        module_0.vowels_count("")

# Generated at 2026-11-02 10:14:18.301679
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("Alone") == 3
    assert module_0.vowels_count("ACEDY") == 3
    assert module_0.vowels_count("abcd") == 1

    # 'y'/'Y' at the end counts as an additional vowel
    assert module_0.vowels_count("key") == 2
    assert module_0.vowels_count("keY") == 2
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("aeiouy") == 6

    # 'y' not at the end does not count
    assert module_0.vowels_count("bye") == 1
    assert module_0.vowels_count("bYe") == 1
    assert module_0.vowels_count("yellow") == 2

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("xyz") == 0

    # All vowels, mixed case
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("aEiOu") == 5

    # Repeated vowels
    assert module_0.vowels_count("aaa") == 3

    # Empty string raises IndexError (s[-1] on empty string)
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass

# Generated at 2026-11-02 10:15:08.378470
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("Alone") == 3

    # 'y'/'Y' at end counts as a vowel
    assert module_0.vowels_count("key") == 2
    assert module_0.vowels_count("keY") == 2
    assert module_0.vowels_count("ACEDY") == 3

    # 'y'/'Y' not at end does not count
    assert module_0.vowels_count("bye") == 1
    assert module_0.vowels_count("yellow") == 2
    assert module_0.vowels_count("Yy") == 1

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("xyz") == 0

    # All vowels, mixed case
    assert module_0.vowels_count("aEiOu") == 5
    assert module_0.vowels_count("AEIOU") == 5

    # Repeated vowels
    assert module_0.vowels_count("aaa") == 3

    # Single characters
    assert module_0.vowels_count("a") == 1
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("b") == 0

    # Empty string raises IndexError (s[-1] fails)
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass

    print("All tests passed!")


if __name__ == "__main__":
    test_vowels_count()

# Generated at 2026-11-02 10:15:45.904101
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2, "Test case 'abcde' failed"
    assert module_0.vowels_count("Alone") == 3, "Test case 'Alone' failed"
    
    # Uppercase vowels
    assert module_0.vowels_count("ABCDE") == 2, "Test case 'ABCDE' failed"
    assert module_0.vowels_count("AEIOU") == 5, "Test case 'AEIOU' failed"
    assert module_0.vowels_count("aeiou") == 5, "Test case 'aeiou' failed"
    
    # Ending with 'y' or 'Y' counts as a vowel
    assert module_0.vowels_count("key") == 2, "Test case 'key' failed"
    assert module_0.vowels_count("keY") == 2, "Test case 'keY' failed"
    assert module_0.vowels_count("ACEDY") == 3, "Test case 'ACEDY' failed"
    assert module_0.vowels_count("xyz") == 1, "Test case 'xyz' failed"
    assert module_0.vowels_count("y") == 1, "Test case 'y' failed"
    assert module_0.vowels_count("Y") == 1, "Test case 'Y' failed"
    
    # 'y' not at the end does not count
    assert module_0.vowels_count("yellow") == 2, "Test case 'yellow' failed"
    assert module_0.vowels_count("bye") == 1, "Test case 'bye' failed"
    assert module_0.vowels_count("bcdfg") == 0, "Test case 'bcdfg' failed"
    
    # No vowels at all
    assert module_0.vowels_count("bcdfgh") == 0, "Test case 'bcdfgh' failed"
    
    # Empty string raises IndexError due to s[-1]
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_vowels_count()

# Generated at 2026-11-02 10:17:18.328634
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2, "Test case 1 failed"  # 'a' and 'e'
    assert module_0.vowels_count("Alone") == 3, "Test case 2 failed"  # 'A', 'o', 'e'
    assert module_0.vowels_count("hello") == 2, "Test case 3 failed"  # 'e', 'o'

    # 'y'/'Y' at end counts as a vowel
    assert module_0.vowels_count("key") == 2, "Test case 4 failed"    # 'e' + trailing 'y'
    assert module_0.vowels_count("HAPPY") == 2, "Test case 5 failed"  # 'A' + trailing 'Y'
    assert module_0.vowels_count("xyz") == 1, "Test case 6 failed"    # trailing 'y' only

    # 'y'/'Y' NOT at end does not count
    assert module_0.vowels_count("bye") == 1, "Test case 7 failed"    # only 'e'
    assert module_0.vowels_count("yellow") == 2, "Test case 8 failed" # 'e', 'o'
    assert module_0.vowels_count("Yy") == 1, "Test case 9 failed"     # trailing 'y' only

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0, "Test case 10 failed"
    assert module_0.vowels_count("1234!@#") == 0, "Test case 11 failed"

    # All vowels, both cases
    assert module_0.vowels_count("aeiou") == 5, "Test case 12 failed"
    assert module_0.vowels_count("AEIOU") == 5, "Test case 13 failed"
    assert module_0.vowels_count("aeiouAEIOU") == 10, "Test case 14 failed"

    # Single character strings
    assert module_0.vowels_count("a") == 1, "Test case 15 failed"
    assert module_0.vowels_count("y") == 1, "Test case 16 failed"
    assert module_0.vowels_count("b") == 0, "Test case 17 failed"

    # Empty string raises IndexError (s[-1] on empty string)
    try:
        module_0.vowels_count("")
        assert False, "Test case 18 failed: expected IndexError"
    except IndexError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_vowels_count()