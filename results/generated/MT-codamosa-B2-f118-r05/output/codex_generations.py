

# Generated at 2026-10-24 07:44:08.576208
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Standard cases: vowel between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"        # uppercase preserved
    assert module_0.get_closest_vowel("full") == "u"
    assert module_0.get_closest_vowel("cat") == "a"

    # No vowel between two consonants
    assert module_0.get_closest_vowel("quick") == ""        # vowels only at edges
    assert module_0.get_closest_vowel("aeiou") == ""        # all vowels, none isolated

    # Too short
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""

    # Exactly 3 chars: only index 1 can qualify
    assert module_0.get_closest_vowel("bat") == "a"
    assert module_0.get_closest_vowel("bbc") == ""

    # Rightmost match wins
    assert module_0.get_closest_vowel("bottle") == "l" or module_0.get_closest_vowel("bottle") == ""
    # careful: "bottle" has no isolated vowel -> ""
    assert module_0.get_closest_vowel("bottle") == ""

    # Mixed case
    assert module_0.get_closest_vowel("BaT") == "a"

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-10-24 07:44:09.880419
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Standard cases: vowel between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"        # uppercase preserved
    assert module_0.get_closest_vowel("full") == "u"
    assert module_0.get_closest_vowel("cat") == "a"

    # No vowel between two consonants
    assert module_0.get_closest_vowel("quick") == ""        # vowels only at edges
    assert module_0.get_closest_vowel("aeiou") == ""        # all vowels, none isolated

    # Too short
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""

    # Exactly 3 chars: only index 1 can qualify
    assert module_0.get_closest_vowel("bat") == "a"
    assert module_0.get_closest_vowel("bbc") == ""

    # Rightmost match wins
    assert module_0.get_closest_vowel("bottle") == "l" or module_0.get_closest_vowel("bottle") == ""
    # careful: "bottle" has no isolated vowel -> ""
    assert module_0.get_closest_vowel("bottle") == ""

    # Mixed case
    assert module_0.get_closest_vowel("BaT") == "a"

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-10-24 07:44:11.200722
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Standard cases: vowel between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"        # uppercase preserved
    assert module_0.get_closest_vowel("full") == "u"
    assert module_0.get_closest_vowel("cat") == "a"

    # No vowel between two consonants
    assert module_0.get_closest_vowel("quick") == ""        # vowels only at edges
    assert module_0.get_closest_vowel("aeiou") == ""        # all vowels, none isolated

    # Too short
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""

    # Exactly 3 chars: only index 1 can qualify
    assert module_0.get_closest_vowel("bat") == "a"
    assert module_0.get_closest_vowel("bbc") == ""

    # Rightmost match wins
    assert module_0.get_closest_vowel("bottle") == "l" or module_0.get_closest_vowel("bottle") == ""
    # careful: "bottle" has no isolated vowel -> ""
    assert module_0.get_closest_vowel("bottle") == ""

    # Mixed case
    assert module_0.get_closest_vowel("BaT") == "a"

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-10-24 07:44:12.510558
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Standard cases: vowel between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"        # uppercase preserved
    assert module_0.get_closest_vowel("full") == "u"
    assert module_0.get_closest_vowel("cat") == "a"

    # No vowel between two consonants
    assert module_0.get_closest_vowel("quick") == ""        # vowels only at edges
    assert module_0.get_closest_vowel("aeiou") == ""        # all vowels, none isolated

    # Too short
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""

    # Exactly 3 chars: only index 1 can qualify
    assert module_0.get_closest_vowel("bat") == "a"
    assert module_0.get_closest_vowel("bbc") == ""

    # Rightmost match wins
    assert module_0.get_closest_vowel("bottle") == "l" or module_0.get_closest_vowel("bottle") == ""
    # careful: "bottle" has no isolated vowel -> ""
    assert module_0.get_closest_vowel("bottle") == ""

    # Mixed case
    assert module_0.get_closest_vowel("BaT") == "a"

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-10-24 07:44:13.830120
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Standard cases: vowel between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"        # uppercase preserved
    assert module_0.get_closest_vowel("full") == "u"
    assert module_0.get_closest_vowel("cat") == "a"

    # No vowel between two consonants
    assert module_0.get_closest_vowel("quick") == ""        # vowels only at edges
    assert module_0.get_closest_vowel("aeiou") == ""        # all vowels, none isolated

    # Too short
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""

    # Exactly 3 chars: only index 1 can qualify
    assert module_0.get_closest_vowel("bat") == "a"
    assert module_0.get_closest_vowel("bbc") == ""

    # Rightmost match wins
    assert module_0.get_closest_vowel("bottle") == "l" or module_0.get_closest_vowel("bottle") == ""
    # careful: "bottle" has no isolated vowel -> ""
    assert module_0.get_closest_vowel("bottle") == ""

    # Mixed case
    assert module_0.get_closest_vowel("BaT") == "a"

    print("All tests passed!")


test_get_closest_vowel()