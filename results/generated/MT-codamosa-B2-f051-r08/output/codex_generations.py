

# Generated at 2026-10-25 01:12:16.174500
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

# Generated at 2026-10-25 01:12:18.699059
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:21.215320
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:23.630220
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:26.052323
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:28.466422
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:30.877924
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:33.292973
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:35.709347
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:38.125574
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:40.549224
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:42.964701
# Unit test for function remove_vowels

# Generated at 2026-10-25 01:12:45.378464
# Unit test for function remove_vowels