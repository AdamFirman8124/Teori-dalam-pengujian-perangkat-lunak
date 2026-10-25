

# Generated at 2026-10-24 04:32:53.410518
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("yogurt") == "u"  # Rightmost qualifying vowel
    assert module_0.get_closest_vowel("hello") == "e"   # Final vowel is not considered
    assert module_0.get_closest_vowel("bAc") == "A"     # Uppercase vowel
    assert module_0.get_closest_vowel("baeiq") == ""    # No isolated vowel
    assert module_0.get_closest_vowel("abc") == ""
    assert module_0.get_closest_vowel("ae") == ""       # Fewer than three characters
    assert module_0.get_closest_vowel("") == ""

# Generated at 2026-10-24 04:33:00.881301
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("banana") == "a"  # Rightmost qualifying vowel
    assert module_0.get_closest_vowel("abecidofu") == "o"
    assert module_0.get_closest_vowel("bOb") == "O"     # Uppercase vowel
    assert module_0.get_closest_vowel("baab") == ""     # Vowels are adjacent
    assert module_0.get_closest_vowel("apple") == ""    # Edge vowels are ignored
    assert module_0.get_closest_vowel("rhythm") == ""   # No vowels
    assert module_0.get_closest_vowel("at") == ""       # Fewer than three characters
    assert module_0.get_closest_vowel("") == ""

# Generated at 2026-10-24 04:33:10.352489
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("test") == "e"
    assert module_0.get_closest_vowel("bAc") == "A"
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("") == ""

# Generated at 2026-10-24 04:33:18.083859
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("at") == ""

    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("hello") == "e"
    assert module_0.get_closest_vowel("banana") == "a"  # Closest valid vowel to the end
    assert module_0.get_closest_vowel("abide") == "i"

    assert module_0.get_closest_vowel("apple") == ""    # Vowels only at the boundaries
    assert module_0.get_closest_vowel("audio") == ""    # No vowel surrounded by non-vowels
    assert module_0.get_closest_vowel("rhythm") == ""

    assert module_0.get_closest_vowel("CAT") == "A"
    assert module_0.get_closest_vowel("BANANA") == "A"

# Generated at 2026-10-24 04:33:29.102327
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Returns the rightmost qualifying vowel
    assert module_0.get_closest_vowel("abidef") == "e"
    assert module_0.get_closest_vowel("yogurt") == "u"

    # Supports uppercase vowels
    assert module_0.get_closest_vowel("bAcEd") == "E"

    # Adjacent vowels do not qualify
    assert module_0.get_closest_vowel("boat") == ""

    # Vowels at the beginning or end do not qualify
    assert module_0.get_closest_vowel("abc") == ""
    assert module_0.get_closest_vowel("bca") == ""

    # Words shorter than three characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("at") == ""

    # No vowels
    assert module_0.get_closest_vowel("rhythm") == ""