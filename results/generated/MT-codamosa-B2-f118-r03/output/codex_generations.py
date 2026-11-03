

# Generated at 2026-11-02 19:06:43.489234
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Vowel between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("bag") == "a"
    assert module_0.get_closest_vowel("bAcUse") == "U"

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    # No vowel between two consonants
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("boot") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""

    # Case sensitivity check
    assert module_0.get_closest_vowel("FuLl") == "u"

    # Vowel at the edge (not between two consonants) should not count
    assert module_0.get_closest_vowel("at") == ""
    assert module_0.get_closest_vowel("ta") == ""

# Generated at 2026-11-02 19:08:53.142742
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("bAt") == "A"
    assert module_0.get_closest_vowel("beautiful") == "u"
    assert module_0.get_closest_vowel("bcdfghjkl") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("Apple") == ""

# Generated at 2026-11-02 19:10:44.788270
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic cases: vowel between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("bace") == "a"
    assert module_0.get_closest_vowel("stem") == "e"
    assert module_0.get_closest_vowel("Alone") == "o"
    assert module_0.get_closest_vowel("Amendment") == "e"

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("q") == ""
    assert module_0.get_closest_vowel("") == ""

    # No vowel surrounded by consonants
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("easy") == ""
    assert module_0.get_closest_vowel("head") == ""

    # Vowel at boundary positions (not between consonants)
    assert module_0.get_closest_vowel("way") == "a"
    assert module_0.get_closest_vowel("cat") == "a"

    # Mixed case handling
    assert module_0.get_closest_vowel("FuLL") == "u"
    assert module_0.get_closest_vowel("bAcE") == "A"

    # Multiple candidates: rightmost valid vowel wins
    assert module_0.get_closest_vowel("batman") == "a"
    assert module_0.get_closest_vowel("minimum") == "u"

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-11-02 19:13:23.693175
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Words shorter than 3 characters return ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    # Basic cases: vowel between two consonants
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("xox") == "o"
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("bEt") == "E"
    assert module_0.get_closest_vowel("bOt") == "O"

    # Adjacent vowels disqualify candidates
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("book") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("EARTH") == ""

    # No vowels at all
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""

    # First and last characters are never checked (loop runs i in [1, len-2])
    assert module_0.get_closest_vowel("axe") == ""

    # Scanning right-to-left: the rightmost qualifying vowel wins
    assert module_0.get_closest_vowel("cotXet") == "e"

    # Mixed case word
    assert module_0.get_closest_vowel("UppErCaSe") == "a"

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-11-02 19:15:26.972214
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Words shorter than 3 characters return ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("Ye") == ""

    # A vowel flanked by consonants is returned
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"

    # Scans from the right, so the last qualifying vowel wins
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("anime") == "i"

    # Vowels adjacent to other vowels do not qualify
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("AgOe") == ""

    # First and last characters are never considered
    assert module_0.get_closest_vowel("abc") == ""
    assert module_0.get_closest_vowel("cba") == ""

    # Uppercase vowels are recognized
    assert module_0.get_closest_vowel("bAc") == "A"

    # No vowels at all
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""

    print("All tests passed!")


test_get_closest_vowel()