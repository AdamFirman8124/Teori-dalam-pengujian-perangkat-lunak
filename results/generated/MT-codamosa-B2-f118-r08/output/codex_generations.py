

# Generated at 2026-10-24 23:43:55.281114
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

# Generated at 2026-10-24 23:43:56.656010
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

# Generated at 2026-10-24 23:43:57.988996
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

# Generated at 2026-10-24 23:43:59.335658
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

# Generated at 2026-10-24 23:44:00.675540
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