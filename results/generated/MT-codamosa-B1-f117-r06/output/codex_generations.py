

# Generated at 2026-10-24 13:25:56.655501
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

# Generated at 2026-10-24 13:25:57.979698
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

# Generated at 2026-10-24 13:25:59.373060
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

# Generated at 2026-10-24 13:26:00.796710
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

# Generated at 2026-10-24 13:26:02.123134
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