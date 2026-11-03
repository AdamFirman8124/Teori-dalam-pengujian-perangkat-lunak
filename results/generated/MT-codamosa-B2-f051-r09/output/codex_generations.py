

# Generated at 2026-11-02 17:52:02.730967
# Unit test for function remove_vowels
def test_remove_vowels():
    # Empty string returns empty string
    assert module_0.remove_vowels("") == ""

    # String with mixed letters and newline
    assert module_0.remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"

    # Simple lowercase vowels removed
    assert module_0.remove_vowels("abcdef") == "bcdf"

    # String containing only vowels
    assert module_0.remove_vowels("aaaaa") == ""

    # Uppercase vowels are also removed
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("AEIOUaeiou") == ""

    # String with no vowels remains unchanged
    assert module_0.remove_vowels("zbcd") == "zbcd"
    assert module_0.remove_vowels("xyz") == "xyz"

    # Numbers, punctuation, and spaces are preserved
    assert module_0.remove_vowels("hello world! 123") == "hll wrld! 123"

    # Mixed case string
    assert module_0.remove_vowels("ThIs Is A tEsT") == "Ths s  tst"

# Generated at 2026-11-02 17:53:09.911963
# Unit test for function remove_vowels
def test_remove_vowels():
    # Basic vowel removal
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("hello world") == "hll wrld"

    # All vowels removed
    assert module_0.remove_vowels("aeiou") == ""
    assert module_0.remove_vowels("AEIOU") == ""

    # Empty string
    assert module_0.remove_vowels("") == ""

    # No vowels present
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("bcdfg") == "bcdfg"

    # Mixed case vowels
    assert module_0.remove_vowels("AbCdEf") == "bCdF"
    assert module_0.remove_vowels("aEiOu") == ""

    # Uppercase vowels
    assert module_0.remove_vowels("APPLE") == "PPL"
    assert module_0.remove_vowels("Orange") == "rng"

    # Special characters, digits, and whitespace preserved
    assert module_0.remove_vowels("a1b2c3") == "1b2c3"
    assert module_0.remove_vowels("hello, world!") == "hll, wrld!"
    assert module_0.remove_vowels("  a b  ") == "  b  "

    # Repeated vowels
    assert module_0.remove_vowels("aaaeeeiiiooouuu") == ""
    assert module_0.remove_vowels("queueing") == "qng"

    # Y is not a vowel
    assert module_0.remove_vowels("rhythm") == "rhythm"
    assert module_0.remove_vowels("why") == "why"

    # Long mixed string
    assert module_0.remove_vowels("The quick brown fox jumps over the lazy dog") == \
        "Th qck brwn fx jmps vr th lzy dg"

    print("All tests passed!")


test_remove_vowels()

# Generated at 2026-11-02 17:54:43.117731
# Unit test for function remove_vowels
def test_remove_vowels():
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("hello world") == "hll wrld"
    assert module_0.remove_vowels("AEIOUaeiou") == ""
    assert module_0.remove_vowels("Python!") == "Pythn!"
    assert module_0.remove_vowels("12345") == "12345"
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("bAnAnA") == "bnn"
    print("All tests passed!")


test_remove_vowels()

# Generated at 2026-11-02 17:56:19.333375
# Unit test for function remove_vowels
def test_remove_vowels():
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("Python") == "Pythn"
    assert module_0.remove_vowels("AEIOUaeiou") == ""
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("Hello, World!") == "Hll, Wrld!"

# Generated at 2026-11-02 17:57:32.203396
# Unit test for function remove_vowels
def test_remove_vowels():
    # Empty string
    assert module_0.remove_vowels("") == ""

    # Basic cases
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"

    # Mixed case vowels should be removed
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("Hello World") == "Hll Wrld"

    # Newlines and whitespace preserved
    assert module_0.remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert module_0.remove_vowels("one two three") == "n tw thr"

    # Digits and punctuation preserved
    assert module_0.remove_vowels("a1b2c3!") == "1b2c3!"
    assert module_0.remove_vowels("!@#$%^&*()") == "!@#$%^&*()"

    # 'y' is not a vowel
    assert module_0.remove_vowels("xyzzy") == "xyzzy"

    # Unicode / non-ASCII characters preserved
    assert module_0.remove_vowels("café") == "cfé"

    # String with only vowels (mixed case)
    assert module_0.remove_vowels("AEIOUaeiou") == ""

    # Long sentence
    assert module_0.remove_vowels("The quick brown fox jumps over the lazy dog") == "Th qck brwn fx jmps vr th lzy dg"

    print("All tests passed!")


test_remove_vowels()