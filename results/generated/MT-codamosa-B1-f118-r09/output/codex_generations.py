

# Generated at 2026-10-25 11:51:47.261683
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:51:50.004212
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:51:52.417994
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:51:54.832321
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:52:19.021267
# Unit test for function get_closest_vowel
def test_get_closest_vowel():assert module_0.get_closest_vowel("yogurt") == "u"

# Generated at 2026-10-25 11:52:22.223624
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic: rightmost interior vowel surrounded by consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("string") == "i"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("cupid") == "i"  # rightmost wins over "u"

    # Too short
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    # No qualifying vowel
    assert module_0.get_closest_vowel("quick") == ""  # adjacent vowels
    assert module_0.get_closest_vowel("queue") == ""  # adjacent vowels
    assert module_0.get_closest_vowel("apple") == ""  # vowels only at edges
    assert module_0.get_closest_vowel("bcdfg") == ""  # no vowels

# Generated at 2026-10-25 11:52:25.046359
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:52:27.494276
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:52:29.883089
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:52:32.294683
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:52:34.929308
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 11:52:37.344320
# Unit test for function get_closest_vowel