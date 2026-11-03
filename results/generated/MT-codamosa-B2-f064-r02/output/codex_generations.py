

# Generated at 2026-11-02 23:55:22.000562
# Unit test for function vowels_count
def test_vowels_count():
    # Basic cases with vowels
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("Alone") == 3
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aeiou") == 5

    # Words ending in 'y' should count the 'y' as a vowel
    assert module_0.vowels_count("acy") == 2
    assert module_0.vowels_count("ACY") == 2
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("HAPPY") == 2
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1

    # Words ending in other consonants
    assert module_0.vowels_count("xyz") == 0
    assert module_0.vowels_count("rhythm") == 0
    assert module_0.vowels_count("sky") == 1
    assert module_0.vowels_count("bcdfg") == 0

    # Mixed case vowels
    assert module_0.vowels_count("aEiOu") == 5
    assert module_0.vowels_count("AbCdEf") == 2

    # Vowels in the middle and end
    assert module_0.vowels_count("bAnAnA") == 3
    assert module_0.vowels_count("Python") == 1
    assert module_0.vowels_count("PYTHON") == 1

    # String with no vowels at all
    assert module_0.vowels_count("bcdfghjklmnpqrstvwxz") == 0
    assert module_0.vowels_count("12345") == 0
    assert module_0.vowels_count("!@#$%") == 0

    # Strings with spaces and mixed characters
    assert module_0.vowels_count("hello world") == 3
    assert module_0.vowels_count("a b c d e") == 2

    # Single character cases
    assert module_0.vowels_count("a") == 1
    assert module_0.vowels_count("b") == 0
    assert module_0.vowels_count("E") == 1

    # Empty-ish edge: single 'y'
    assert module_0.vowels_count("my") == 1

    print("All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_vowels_count()

# Generated at 2026-11-02 23:55:57.533722
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2, "Expected 2 vowels in 'abcde'"
    assert module_0.vowels_count("Alone") == 3, "Expected 3 vowels in 'Alone'"
    assert module_0.vowels_count("hello") == 2, "Expected 2 vowels in 'hello'"
    assert module_0.vowels_count("AEIOU") == 5, "Expected 5 vowels in 'AEIOU'"
    assert module_0.vowels_count("aeiou") == 5, "Expected 5 vowels in 'aeiou'"

    # No vowels
    assert module_0.vowels_count("xyz") == 0, "Expected 0 vowels in 'xyz'"
    assert module_0.vowels_count("bcd") == 0, "Expected 0 vowels in 'bcd'"
    assert module_0.vowels_count("rhythm") == 0, "Expected 0 vowels in 'rhythm' (y not at end)"

    # Trailing 'y' / 'Y' counts as a vowel
    assert module_0.vowels_count("y") == 1, "Single 'y' should count as 1"
    assert module_0.vowels_count("Y") == 1, "Single 'Y' should count as 1"
    assert module_0.vowels_count("ACEDY") == 3, "Expected 3 (A, E + trailing Y)"
    assert module_0.vowels_count("day") == 2, "Expected 2 (a + trailing y)"
    assert module_0.vowels_count("aeiouy") == 6, "Expected 6 (5 vowels + trailing y)"
    assert module_0.vowels_count("syzygy") == 1, "Expected 1 (only trailing y)"

    # 'y' in the middle does not count
    assert module_0.vowels_count("Python") == 1, "Expected 1 (only 'o'; y is not at end)"
    assert module_0.vowels_count("yellow") == 2, "Expected 2 (e, o; y not at end)"

    # Mixed case
    assert module_0.vowels_count("AbCdEfG") == 2, "Expected 2 (A, E)"
    assert module_0.vowels_count("Yes") == 1, "Expected 1 (e; Y not at end)"

    print("All tests passed!")


if __name__ == "__main__":
    test_vowels_count()

# Generated at 2026-11-02 23:56:53.240149
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("Alone") == 3
    assert module_0.vowels_count("key") == 2
    assert module_0.vowels_count("bye") == 1
    assert module_0.vowels_count("keY") == 2
    assert module_0.vowels_count("bYe") == 1
    assert module_0.vowels_count("ACEDY") == 3
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("xyz") == 1
    assert module_0.vowels_count("rhythm") == 0
    assert module_0.vowels_count("AEIOUaeiou") == 10
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("HAPPY") == 2
    assert module_0.vowels_count("b") == 0
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1

# Generated at 2026-11-02 23:57:52.541610
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2  # 'a' and 'e'
    assert module_0.vowels_count("Alone") == 3  # 'A', 'o', 'e'
    assert module_0.vowels_count("AEIOU") == 5  # all uppercase vowels
    assert module_0.vowels_count("aeiou") == 5  # all lowercase vowels

    # 'y' at the end counts as a vowel
    assert module_0.vowels_count("academy") == 4  # a, a, e + ending 'y'
    assert module_0.vowels_count("acY") == 2      # 'a' + ending 'Y'

    # 'y' not at the end does not count
    assert module_0.vowels_count("yellow") == 2   # 'e', 'o' only
    assert module_0.vowels_count("syzygy") == 1   # ending 'y' only

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("rhythm") == 0   # no standard vowels, 'y' not at end

    # Mixed case
    assert module_0.vowels_count("PyThOn") == 2   # 'O' and ending... 'n' not y
    assert module_0.vowels_count("PythonY") == 2  # 'o' + ending 'Y'

    # Single character strings
    assert module_0.vowels_count("a") == 1
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("b") == 0

    print("All tests passed!")


test_vowels_count()

# Generated at 2026-11-02 23:59:42.203014
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2, "Test 1 failed"
    assert module_0.vowels_count("Alone") == 3, "Test 2 failed"

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("key") == 2, "Test 3 failed"
    assert module_0.vowels_count("keY") == 2, "Test 4 failed"
    assert module_0.vowels_count("ACEDY") == 3, "Test 5 failed"
    assert module_0.vowels_count("yyy") == 1, "Test 6 failed"

    # 'y' not at the end does not count
    assert module_0.vowels_count("bye") == 1, "Test 7 failed"
    assert module_0.vowels_count("bYe") == 1, "Test 8 failed"
    assert module_0.vowels_count("yellow") == 2, "Test 9 failed"

    # No vowels at all
    assert module_0.vowels_count("bcdfg") == 0, "Test 10 failed"
    assert module_0.vowels_count("xyz") == 0, "Test 11 failed"

    # All vowels, mixed case
    assert module_0.vowels_count("aeiouAEIOU") == 10, "Test 12 failed"

    # Single characters
    assert module_0.vowels_count("a") == 1, "Test 13 failed"
    assert module_0.vowels_count("y") == 1, "Test 14 failed"
    assert module_0.vowels_count("Y") == 1, "Test 15 failed"
    assert module_0.vowels_count("b") == 0, "Test 16 failed"

    print("All tests passed!")


if __name__ == "__main__":
    test_vowels_count()