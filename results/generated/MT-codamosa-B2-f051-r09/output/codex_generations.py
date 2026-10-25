

# Generated at 2026-10-24 22:24:41.944695
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

# Generated at 2026-10-24 22:24:44.462038
# Unit test for function remove_vowels

# Generated at 2026-10-24 22:24:46.878722
# Unit test for function remove_vowels

# Generated at 2026-10-24 22:24:49.297595
# Unit test for function remove_vowels

# Generated at 2026-10-24 22:24:50.663485
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

# Generated at 2026-10-24 22:24:51.991073
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

# Generated at 2026-10-24 22:24:53.339759
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