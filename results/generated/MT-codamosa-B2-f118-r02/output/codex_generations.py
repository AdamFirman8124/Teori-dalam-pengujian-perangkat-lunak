

# Generated at 2026-11-01 22:31:57.217091
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic cases from specification
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("EE") == ""

    # Vowel surrounded by consonants
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("chart") == "a"
    assert module_0.get_closest_vowel("banana") == "a"

    # No qualifying vowel (vowel adjacent to another vowel)
    assert module_0.get_closest_vowel("book") == ""
    assert module_0.get_closest_vowel("aei") == ""
    assert module_0.get_closest_vowel("spoon") == ""

    # No vowels at all
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""

    # Uppercase vowel in the middle
    assert module_0.get_closest_vowel("wOrld") == "O"

    # Vowel at edge positions should not count (range excludes index 0 and len-1)
    assert module_0.get_closest_vowel("ape") == ""
    assert module_0.get_closest_vowel("UUm") == ""


if __name__ == "__main__":
    test_get_closest_vowel()
    print("All tests passed!")

# Generated at 2026-11-01 22:32:15.648996
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    # Vowel between consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("gully") == "u"
    assert module_0.get_closest_vowel("amends") == "e"
    assert module_0.get_closest_vowel("Above") == "o"
    assert module_0.get_closest_vowel("bathe") == "a"

    # No qualifying vowel (adjacent vowels or vowel at edge)
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("easy") == ""
    assert module_0.get_closest_vowel("head") == ""
    assert module_0.get_closest_vowel("chair") == ""
    assert module_0.get_closest_vowel("aaa") == ""
    assert module_0.get_closest_vowel("aRe") == ""

    # No vowels at all
    assert module_0.get_closest_vowel("bcdfg") == ""


test_get_closest_vowel()
print("All tests passed!")

# Generated at 2026-11-01 22:32:36.135033
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic cases where a qualifying vowel exists between consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("cat") == "a"

    # No vowel found between two consonants
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""

    # Vowel at edge positions does not count (needs neighbors inside loop bounds)
    assert module_0.get_closest_vowel("apple") == ""   # candidates blocked by adjacent vowels
    assert module_0.get_closest_vowel("aeiou") == ""   # consecutive vowels never qualify

    # Rightmost qualifying vowel wins (search starts from the end)
    assert module_0.get_closest_vowel("banana") == "a"  # 'a' between 'n' and 'n'
    assert module_0.get_closest_vowel("open") == "e"

    # Mixed case handling
    assert module_0.get_closest_vowel("fUlL") == "U"
    assert module_0.get_closest_vowel("OtHer") == "e"  # checks right-to-left: 'e' qualifies first

# Generated at 2026-11-01 22:33:00.702105
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic cases: vowel surrounded by consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("yes") == "e"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("bed") == "e"

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("Au") == ""

    # Adjacent vowels disqualify each other
    assert module_0.get_closest_vowel("head") == ""
    assert module_0.get_closest_vowel("book") == ""
    assert module_0.get_closest_vowel("school") == ""
    assert module_0.get_closest_vowel("dream") == ""

    # Vowel only at edges (index 0 or last index) -> not eligible
    assert module_0.get_closest_vowel("aba") == ""
    assert module_0.get_closest_vowel("act") == ""
    assert module_0.get_closest_vowel("Apple") == ""

    # Multiple candidates: rightmost qualifying vowel wins
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("strongest") == "e"

    # No vowels / consonant-only words
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""

    # Mixed case handling
    assert module_0.get_closest_vowel("BAt") == "A"
    assert module_0.get_closest_vowel("cAt") == "A"

# Generated at 2026-11-01 22:33:43.553845
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("ae") == ""
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("bAc") == "A"
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""
    assert module_0.get_closest_vowel("bEAd") == ""  # vowel adjacent to another vowel
    assert module_0.get_closest_vowel("xIz") == "I"
    print("All tests passed!")


if __name__ == "__main__":
    test_get_closest_vowel()