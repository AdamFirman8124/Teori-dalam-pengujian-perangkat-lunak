

# Generated at 2026-10-24 14:41:32.657215
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

# Generated at 2026-10-24 14:41:34.022998
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

# Generated at 2026-10-24 14:41:35.497482
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

# Generated at 2026-10-24 14:41:36.931314
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

# Generated at 2026-10-24 14:41:49.117520
# Unit test for function select_words
def test_select_words():
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 2) == ["had"]
    assert module_0.select_words("Mary had a little lamb", 0) == ["a"]
    assert module_0.select_words("Mary had a little lamb", 1) == []
    assert module_0.select_words("", 3) == []
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert module_0.select_words("AEIOU xyz BC", 0) == ["AEIOU"]
    assert module_0.select_words("AEIOU xyz BC", 3) == ["xyz"]
    assert module_0.select_words("AEIOU xyz BC", 2) == ["BC"]
    assert module_0.select_words("simple white space", 4) == ["simple"]
    assert module_0.select_words("simple white space", 3) == ["white", "space"]
    assert module_0.select_words("hello world", 3) == ["hello"]
    assert module_0.select_words("hello world", 4) == ["world"]
    assert module_0.select_words("HELLO World", 3) == ["HELLO"]
    assert module_0.select_words("HELLO World", 4) == ["World"]