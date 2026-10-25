

# Generated at 2026-10-24 04:45:50.194284
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:45:52.611494
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:45:55.023216
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:45:57.439930
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:45:59.849232
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:02.260655
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:04.677208
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:07.116211
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:09.504870
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:11.920082
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:14.335146
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:16.749062
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:19.163719
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:21.577248
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:23.997972
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:26.405942
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:28.818295
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:31.230856
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:33.642951
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:36.055055
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:38.470064
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:46:45.512963
# Unit test for function get_closest_vowel
def test_get_closest_vowel():assert module_0.get_closest_vowel("yogurt") == "u"

# Generated at 2026-10-24 04:47:02.000161
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL STACK") == "A"
    assert module_0.get_closest_vowel("hello") == "e"
    assert module_0.get_closest_vowel("anime") == "i"

    # Vowels at the beginning or end do not qualify
    assert module_0.get_closest_vowel("apple") == ""
    assert module_0.get_closest_vowel("Asia") == ""

    # Adjacent vowels do not qualify
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("eeeee") == ""

    # Words shorter than three characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

# Generated at 2026-10-24 04:47:10.604975
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("ABIDE") == "I"
    assert module_0.get_closest_vowel("boat") == ""       # Adjacent vowels
    assert module_0.get_closest_vowel("apple") == ""      # Vowel only at the boundary
    assert module_0.get_closest_vowel("rhythm") == ""     # No vowels
    assert module_0.get_closest_vowel("at") == ""         # Fewer than three characters
    assert module_0.get_closest_vowel("") == ""

# Generated at 2026-10-24 04:47:19.817429
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("baced") == "e"  # Closest qualifying vowel to the end
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("CAT") == "A"
    assert module_0.get_closest_vowel("book") == ""   # Adjacent vowels do not qualify
    assert module_0.get_closest_vowel("apple") == ""  # Vowels at either end are ignored
    assert module_0.get_closest_vowel("aei") == ""
    assert module_0.get_closest_vowel("at") == ""
    assert module_0.get_closest_vowel("") == ""

# Generated at 2026-10-24 04:47:22.361377
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:24.777032
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:27.283657
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:29.697382
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:32.109550
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:34.527224
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:36.941635
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:39.353582
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:41.764436
# Unit test for function get_closest_vowel

# Generated at 2026-10-24 04:47:50.737733
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Rightmost vowel surrounded by consonants
    assert module_0.get_closest_vowel("yogurt") == "u"

    # Select the qualifying vowel closest to the end
    assert module_0.get_closest_vowel("planet") == "e"
    assert module_0.get_closest_vowel("banana") == "a"

    # Uppercase vowels
    assert module_0.get_closest_vowel("FULL") == "U"

    # Adjacent vowels do not qualify
    assert module_0.get_closest_vowel("boat") == ""

    # First and last characters are not considered
    assert module_0.get_closest_vowel("apple") == ""

    # Words shorter than three characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("at") == ""

    # No vowels
    assert module_0.get_closest_vowel("rhythm") == ""