

# Generated at 2026-10-24 23:17:43.116657
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:17:45.532979
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:17:47.950604
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:17:50.368673
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:17:52.784428
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:17:55.201102
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:17:57.616651
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:18:00.037380
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:18:02.448523
# Unit test for function remove_vowels

# Generated at 2026-10-24 23:18:08.995664
# Unit test for function remove_vowels
def test_remove_vowels():assert module_0.remove_vowels("hello world") == "hll wrld"

# Generated at 2026-10-24 23:18:10.322039
# Unit test for function remove_vowels
def test_remove_vowels():
    # basic
    assert module_0.remove_vowels("hello world") == "hll wrld"
    # all five vowels, lowercase
    assert module_0.remove_vowels("aeiou") == ""
    # uppercase vowels removed too
    assert module_0.remove_vowels("AEIOU") == ""
    # mixed case preserved on consonants
    assert module_0.remove_vowels("StackOverflow") == "Stckvrflw"
    # no vowels -> unchanged
    assert module_0.remove_vowels("rhythm") == "rhythm"
    # empty string
    assert module_0.remove_vowels("") == ""
    # only non-vowel chars (digits, spaces, punctuation)
    assert module_0.remove_vowels("123 !?") == "123 !?"
    # y is NOT a vowel here
    assert module_0.remove_vowels("my gym") == "my gym"
    # vowels interleaved with spaces
    assert module_0.remove_vowels("a e i o u") == "    "
    # unicode vowels (not in the list) pass through
    assert module_0.remove_vowels("cafÃ©") == "cfÃ©"