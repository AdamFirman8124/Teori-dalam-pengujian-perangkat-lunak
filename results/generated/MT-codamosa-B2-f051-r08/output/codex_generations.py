

# Generated at 2026-11-02 08:50:29.697937
# Unit test for function remove_vowels
def test_remove_vowels():
    # Basic cases
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"

    # Uppercase vowels should also be removed
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("AEIOU") == ""
    assert module_0.remove_vowels("aeiou") == ""

    # Mixed case and content
    assert module_0.remove_vowels("Hello, World!") == "Hll, Wrld!"
    assert module_0.remove_vowels("Testing 123") == "Tstng 123"

    # No vowels at all
    assert module_0.remove_vowels("rhythm") == "rhythm"
    assert module_0.remove_vowels("xyz") == "xyz"

    # Vowels at boundaries
    assert module_0.remove_vowels("apple") == "ppl"
    assert module_0.remove_vowels("orange") == "rng"

    # Special characters and digits remain untouched
    assert module_0.remove_vowels("!@#$%") == "!@#$%"
    assert module_0.remove_vowels("a1e2i3") == "123"

    # Whitespace preserved
    assert module_0.remove_vowels("a b c d e") == " b c d "

    print("All tests passed!")


if __name__ == "__main__":
    test_remove_vowels()

# Generated at 2026-11-02 08:50:41.987938
# Unit test for function remove_vowels
def test_remove_vowels():
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("Python is fun!") == "Pythn s fn!"
    assert module_0.remove_vowels("AEIOUaeiou") == ""
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("a1e2i3o4u5") == "12345"

# Generated at 2026-11-02 08:50:51.192154
# Unit test for function remove_vowels
def test_remove_vowels():
    # Basic cases
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"

    # Mixed case vowels
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("hello") == "hll"
    assert module_0.remove_vowels("AbEcIdOfU") == "bcd"

    # Uppercase and lowercase mixed
    assert module_0.remove_vowels("Python is Awesome") == "Pythn s wsm"

    # No vowels
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("12345") == "12345"
    assert module_0.remove_vowels("!@#$%") == "!@#$%"

    # Only vowels
    assert module_0.remove_vowels("AEIOUaeiou") == ""

    # Spaces and punctuation preserved
    assert module_0.remove_vowels("The quick brown fox!") == "Th qck brwn fx!"

    # Single character
    assert module_0.remove_vowels("a") == ""
    assert module_0.remove_vowels("b") == "b"

    # 'y' should not be treated as a vowel
    assert module_0.remove_vowels("why") == "why"

    print("All tests passed!")


# Run the test
if __name__ == "__main__":
    test_remove_vowels()

# Generated at 2026-11-02 08:50:59.611793
# Unit test for function remove_vowels
def test_remove_vowels():
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("Python Programming") == "Pythn Prgrmmng"
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("AEIOUaeiou") == ""
    assert module_0.remove_vowels("b") == "b"
    assert module_0.remove_vowels("a") == ""
    print("All tests passed!")


test_remove_vowels()

# Generated at 2026-11-02 08:51:20.223270
# Unit test for function remove_vowels
def test_remove_vowels():
    # Basic cases
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"

    # Mixed case vowels are removed
    assert module_0.remove_vowels("AbEcIdOfU") == ""
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("hello world") == "hll wrld"

    # Non-letter characters are preserved
    assert module_0.remove_vowels("12345") == "12345"
    assert module_0.remove_vowels("!@#$%") == "!@#$%"
    assert module_0.remove_vowels("a1e2i3") == "123"

    # 'y' is not a vowel and should be kept
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("rhythm") == "rhythm"

    # Spaces and punctuation preserved
    assert module_0.remove_vowels("This is a test.") == "Ths s  tst."

    # Unicode / non-ASCII characters preserved
    assert module_0.remove_vowels("café") == "cfé"
    assert module_0.remove_vowels("你好") == "你好"

    print("All tests passed!")


test_remove_vowels()