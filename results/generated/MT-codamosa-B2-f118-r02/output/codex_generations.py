

# Generated at 2026-10-25 02:26:13.821722
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:16.235970
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:18.650780
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:21.068016
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:23.485843
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:25.903701
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:28.319944
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:30.734765
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:33.150102
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:35.565833
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:37.980661
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:40.395282
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:42.809869
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:45.225190
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 02:26:52.064977
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Vowel between two consonants, found from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""
    # Vowel adjacent to another vowel doesn't count
    assert module_0.get_closest_vowel("quickly") == ""
    assert module_0.get_closest_vowel("bca") == ""
    assert module_0.get_closest_vowel("bAcA") == ""
    assert module_0.get_closest_vowel("cat") == ""
    assert module_0.get_closest_vowel("rhythm") == ""