

# Generated at 2026-10-25 12:36:40.457014
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:36:42.869748
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:36:45.283187
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:36:47.699462
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:36:50.113601
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:36:52.528563
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:36:54.942850
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:36:57.357078
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:36:59.768601
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:37:15.436514
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:37:50.457661
# Unit test for function get_closest_vowel
def test_get_closest_vowel():assert module_0.get_closest_vowel("yogurt") == "u"

# Generated at 2026-10-25 12:37:52.873715
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:37:55.683932
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:37:58.097001
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:38:00.511611
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:38:02.927014
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:38:05.956145
# Unit test for function get_closest_vowel
def test_get_closest_vowel():assert module_0.get_closest_vowel("yogurt") == "u"

# Generated at 2026-10-25 12:38:07.378133
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

# Generated at 2026-10-25 12:38:08.891241
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

# Generated at 2026-10-25 12:38:17.184385
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

# Generated at 2026-10-25 12:38:18.723809
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

# Generated at 2026-10-25 12:38:20.256361
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

# Generated at 2026-10-25 12:38:23.443750
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

# Generated at 2026-10-25 12:38:31.523435
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

# Generated at 2026-10-25 12:38:33.056862
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

# Generated at 2026-10-25 12:38:35.582760
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:38:38.289393
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 12:38:40.829572
# Unit test for function get_closest_vowel