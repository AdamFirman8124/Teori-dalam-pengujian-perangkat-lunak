

# Generated at 2026-11-02 16:24:03.301859
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Words shorter than 3 characters return ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("At") == ""

    # Vowel sandwiched between consonants
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("CONSONANT") == "A"
    assert module_0.get_closest_vowel("xax") == "a"
    assert module_0.get_closest_vowel("xuX") == "u"

    # Scan from the right: rightmost qualifying vowel wins
    assert module_0.get_closest_vowel("rapid") == "i"
    assert module_0.get_closest_vowel("ABECEDO") == "E"  # 'E' at index 4: neighbors 'C','D' consonants... check 'O' first

    # Adjacent vowels disqualify a vowel
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("book") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("aax") == ""

    # No qualifying vowel at all
    assert module_0.get_closest_vowel("bcdfg") == ""
    assert module_0.get_closest_vowel("AbE") == ""
    assert module_0.get_closest_vowel("xxa") == ""  # trailing vowel never checked

    # Mixed-case vowel matching
    assert module_0.get_closest_vowel("xOx") == "O"
    assert module_0.get_closest_vowel("xIx") == "I"

    print("All tests passed!")

test_get_closest_vowel()

# Generated at 2026-11-02 16:24:52.993551
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("ab,") == ""
    assert module_0.get_closest_vowel("ae") == ""
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("Umm") == ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("q") == ""
    assert module_0.get_closest_vowel("full") == "u"
    assert module_0.get_closest_vowel("b") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("o") == ""
    assert module_0.get_closest_vowel(" spoon") == ""
    assert module_0.get_closest_vowel("spoon") == "o"

# Generated at 2026-11-02 16:25:50.894727
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic cases: vowel between two consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("full") == "u"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("bake") == "a"
    assert module_0.get_closest_vowel("bAke") == "A"

    # No vowel between consonants
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("great") == ""
    assert module_0.get_closest_vowel("apple") == ""

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("aa") == ""
    assert module_0.get_closest_vowel("O") == ""

    # Closest vowel found from the right side
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("lemon") == "o"

    # No vowels at all
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("xyz") == ""

    # Vowels at edges don't count (need consonant on both sides)
    assert module_0.get_closest_vowel("Eva") == ""
    assert module_0.get_closest_vowel("Umm") == ""
    assert module_0.get_closest_vowel("Ice") == ""

    print("All tests passed!")


if __name__ == "__main__":
    test_get_closest_vowel()

# Generated at 2026-11-02 16:27:49.263796
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Standard examples
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""   # vowels are adjacent to other vowels
    assert module_0.get_closest_vowel("ab") == ""      # too short

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("Ay") == ""
    assert module_0.get_closest_vowel("xo") == ""

    # Single vowel between consonants (qualifies)
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("full") == "u"
    assert module_0.get_closest_vowel("bAc") == "A"    # uppercase vowel handled
    assert module_0.get_closest_vowel("xEz") == "E"

    # No vowels at all
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("xyz") == ""
    assert module_0.get_closest_vowel("BCDFG") == ""

    # Adjacent vowels disqualify each other
    assert module_0.get_closest_vowel("AEIOU") == ""
    assert module_0.get_closest_vowel("aei") == ""
    assert module_0.get_closest_vowel("boat") == ""    # 'o' and 'a' adjacent to vowels/consonant chain
    assert module_0.get_closest_vowel("team") == ""    # 'e' next to 'a'

    # Rightmost qualifying vowel wins (search proceeds from the end)
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("CEQAZ") == "A"
    assert module_0.get_closest_vowel("instantiation") == "a"

    # Vowel at the very start or end cannot qualify (loop range excludes edges)
    assert module_0.get_closest_vowel("axb") == "a"    # wait: 'a' at index 0 not checked; index 1 is 'x'
    # correction: index 1 is 'x' (not a vowel), so result is ""
    assert module_0.get_closest_vowel("axb") == ""
    assert module_0.get_closest_vowel("bxa") == ""     # trailing vowel at last index not checked

    print("All tests passed!")


if __name__ == "__main__":
    test_get_closest_vowel()

# Generated at 2026-11-02 16:28:43.167031
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # word with vowel between two consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("bAc") == "A"
    # words shorter than 3 characters
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""
    # no vowel surrounded by consonants
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("spa") == ""
    # closest from the right wins
    assert module_0.get_closest_vowel("bAced") == "e"
    assert module_0.get_closest_vowel("banana") == ""
    assert module_0.get_closest_vowel("happy") == "a"