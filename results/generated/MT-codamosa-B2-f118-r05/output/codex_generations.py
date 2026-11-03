

# Generated at 2026-11-03 03:33:40.412091
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Closest vowel between two consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("rhythm") == ""   # no vowels
    assert module_0.get_closest_vowel("quick") == ""    # vowels not between consonants
    assert module_0.get_closest_vowel("ab") == ""       # word too short
    assert module_0.get_closest_vowel("") == ""         # empty string
    assert module_0.get_closest_vowel("a") == ""        # single character
    assert module_0.get_closest_vowel("aeiou") == ""    # all vowels, none qualifies
    assert module_0.get_closest_vowel("bcbcbc") == ""   # no vowels at all
    assert module_0.get_closest_vowel("banana") == ""   # no vowel between consonants
    assert module_0.get_closest_vowel("jump") == "u"
    assert module_0.get_closest_vowel("ABeZI") == "E"   # mixed case, find rightmost qualifying
    print("All tests passed!")

# Generated at 2026-11-03 03:36:16.682158
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic cases from problem spec
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("ab") == ""

    # Words shorter than 3
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ax") == ""

    # Vowel found between two consonants
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("bAc") == "A"
    assert module_0.get_closest_vowel("XaY") == "a"

    # Rightmost qualifying vowel wins
    assert module_0.get_closest_vowel("catDog") == "o"

    # Vowels adjacent to vowels do not qualify
    assert module_0.get_closest_vowel("AEIOU") == ""
    assert module_0.get_closest_vowel("baE") == ""
    assert module_0.get_closest_vowel("bEa") == ""

    # No vowel between consonants
    assert module_0.get_closest_vowel("apple") == ""
    assert module_0.get_closest_vowel("aXb#") == ""
    assert module_0.get_closest_vowel("xyz") == ""

    # Non-letter characters count as non-vowels
    assert module_0.get_closest_vowel("x1o3x") == "o"

    # Vowel at edge positions (index 0 or last) cannot qualify
    assert module_0.get_closest_vowel("aXe") == ""
    assert module_0.get_closest_vowel("Xab") == ""

# Generated at 2026-11-03 03:38:01.489481
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Standard cases: vowel between two consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("hEllo") == "E"
    assert module_0.get_closest_vowel("beautiful") == "u"

    # No valid vowel (vowel adjacent to another vowel or at edges)
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aei") == ""
    assert module_0.get_closest_vowel("boa") == ""      # vowel at last index is never checked
    assert module_0.get_closest_vowel("xYz") == ""      # 'y' is not treated as a vowel
    assert module_0.get_closest_vowel("bcdfg") == ""    # no vowels at all

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("bc") == ""

    # Case sensitivity checks
    assert module_0.get_closest_vowel("YES") == "E"
    assert module_0.get_closest_vowel("tEsT") == "E"

    # Picks the closest (rightmost qualifying) vowel between consonants
    assert module_0.get_closest_vowel("bora") == "o"

# Generated at 2026-11-03 03:39:19.668123
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Word with vowel between consonants
    assert module_0.get_closest_vowel("yogurt") == "U"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("happy") == "a"

    # No vowel between consonants
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("baa") == ""

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("Ae") == ""

# Generated at 2026-11-03 03:40:39.744530
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Words with a vowel between two consonants
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("yog") == "o"
    assert module_0.get_closest_vowel("PAN") == "A"
    assert module_0.get_closest_vowel("FULL") == "U"

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    # No qualifying vowel (consecutive vowels or no vowels)
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""
    assert module_0.get_closest_vowel("bOok") == ""

    # Vowel at the edge does not count (needs consonant on both sides)
    assert module_0.get_closest_vowel("abo") == ""
    assert module_0.get_closest_vowel("oba") == ""