

# Generated at 2026-10-24 12:31:04.247367
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 12:31:06.660609
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 12:31:09.076711
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 12:31:11.486601
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 12:31:13.900864
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 12:31:16.314538
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 12:31:18.727928
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 12:31:21.141449
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 12:31:29.509043
# Unit test for function get_closest_vowel
def test_get_closest_vowel():# Vowel between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"      # 'u' at index 3, between 'g' and 'r'
    assert module_0.get_closest_vowel("FULL") == "U"        # uppercase vowel, between 'F' and 'L'
    assert module_0.get_closest_vowel("quick") == ""        # 'i' is between vowels, no valid vowel
    assert module_0.get_closest_vowel("ab") == ""           # too short (< 3 chars)
    assert module_0.get_closest_vowel("") == ""             # empty string
    assert module_0.get_closest_vowel("cat") == "a"         # 'a' between 'c' and 't'
    assert module_0.get_closest_vowel("full") == "u"        # lowercase: 'u' between 'f' and 'l'
    assert module_0.get_closest_vowel("bcdfg") == ""        # no vowels at all
    assert module_0.get_closest_vowel("aeiou") == ""        # every vowel sits between vowels
    assert module_0.get_closest_vowel("racecar") == "e"     # rightmost valid vowel wins: 'e' before 'a'

# Generated at 2026-10-24 12:31:35.160205
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Vowel between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == "i"
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("quickly") == ""   # 'i' has 'u' before it â skip; no candidate after
    assert module_0.get_closest_vowel("body") == "o"
    assert module_0.get_closest_vowel("rhythm") == ""    # no vowels at all
    assert module_0.get_closest_vowel("a") == ""         # too short
    assert module_0.get_closest_vowel("aei") == ""       # vowels adjacent to vowels don't count
    assert module_0.get_closest_vowel("cat") == "a"      # index 1: 'a' between 'c' and 't'
    print("All tests passed!")

test_get_closest_vowel()

# Generated at 2026-10-24 12:31:36.881202
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Vowel between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == "i"
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("quickly") == ""   # 'i' has 'u' before it â skip; no candidate after
    assert module_0.get_closest_vowel("body") == "o"
    assert module_0.get_closest_vowel("rhythm") == ""    # no vowels at all
    assert module_0.get_closest_vowel("a") == ""         # too short
    assert module_0.get_closest_vowel("aei") == ""       # vowels adjacent to vowels don't count
    assert module_0.get_closest_vowel("cat") == "a"      # index 1: 'a' between 'c' and 't'
    print("All tests passed!")

test_get_closest_vowel()