

# Generated at 2026-10-25 02:37:20.609154
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # vowel sandwiched between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"          # case-sensitive vowels set
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("beautiful") == "u"

    # no qualifying vowel
    assert module_0.get_closest_vowel("quick") == ""          # vowels adjacent to vowels don't count
    assert module_0.get_closest_vowel("rhythm") == ""         # 'y' is not in the vowel set
    assert module_0.get_closest_vowel("aei") == ""            # all vowels, no consonant neighbors

    # length guard
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    print("All tests passed.")

test_get_closest_vowel()

# Generated at 2026-10-25 02:37:21.925562
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # vowel sandwiched between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"          # case-sensitive vowels set
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("beautiful") == "u"

    # no qualifying vowel
    assert module_0.get_closest_vowel("quick") == ""          # vowels adjacent to vowels don't count
    assert module_0.get_closest_vowel("rhythm") == ""         # 'y' is not in the vowel set
    assert module_0.get_closest_vowel("aei") == ""            # all vowels, no consonant neighbors

    # length guard
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    print("All tests passed.")

test_get_closest_vowel()

# Generated at 2026-10-25 02:37:23.244117
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # vowel sandwiched between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"          # case-sensitive vowels set
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("beautiful") == "u"

    # no qualifying vowel
    assert module_0.get_closest_vowel("quick") == ""          # vowels adjacent to vowels don't count
    assert module_0.get_closest_vowel("rhythm") == ""         # 'y' is not in the vowel set
    assert module_0.get_closest_vowel("aei") == ""            # all vowels, no consonant neighbors

    # length guard
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    print("All tests passed.")

test_get_closest_vowel()

# Generated at 2026-10-25 02:37:24.583017
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # vowel sandwiched between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"          # case-sensitive vowels set
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("beautiful") == "u"

    # no qualifying vowel
    assert module_0.get_closest_vowel("quick") == ""          # vowels adjacent to vowels don't count
    assert module_0.get_closest_vowel("rhythm") == ""         # 'y' is not in the vowel set
    assert module_0.get_closest_vowel("aei") == ""            # all vowels, no consonant neighbors

    # length guard
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    print("All tests passed.")

test_get_closest_vowel()

# Generated at 2026-10-25 02:37:25.906012
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # vowel sandwiched between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"          # case-sensitive vowels set
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("beautiful") == "u"

    # no qualifying vowel
    assert module_0.get_closest_vowel("quick") == ""          # vowels adjacent to vowels don't count
    assert module_0.get_closest_vowel("rhythm") == ""         # 'y' is not in the vowel set
    assert module_0.get_closest_vowel("aei") == ""            # all vowels, no consonant neighbors

    # length guard
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    print("All tests passed.")

test_get_closest_vowel()