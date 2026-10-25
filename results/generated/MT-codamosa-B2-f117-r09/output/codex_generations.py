

# Generated at 2026-10-24 11:29:47.740513
# Unit test for function select_words
def test_select_words():
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert module_0.select_words("", 4) == []
    # regression: punctuation/digits are not consonants
    assert module_0.select_words("it's 3rd", 2) == ["it's", "3rd"]

# Generated at 2026-10-24 11:29:50.300986
# Unit test for function select_words

# Generated at 2026-10-24 11:29:52.722766
# Unit test for function select_words

# Generated at 2026-10-24 11:29:55.292767
# Unit test for function select_words

# Generated at 2026-10-24 11:29:57.710851
# Unit test for function select_words

# Generated at 2026-10-24 11:30:00.129971
# Unit test for function select_words

# Generated at 2026-10-24 11:30:02.545984
# Unit test for function select_words

# Generated at 2026-10-24 11:30:04.965898
# Unit test for function select_words

# Generated at 2026-10-24 11:30:07.379700
# Unit test for function select_words

# Generated at 2026-10-24 11:30:09.797503
# Unit test for function select_words

# Generated at 2026-10-24 11:30:12.217744
# Unit test for function select_words

# Generated at 2026-10-24 11:30:14.635590
# Unit test for function select_words

# Generated at 2026-10-24 11:30:17.085431
# Unit test for function select_words