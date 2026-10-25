

# Generated at 2026-10-24 07:44:04.504224
# Unit test for function split_words
def test_split_words():
    # Branch 1: contains space -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  hello   world  ") == ["hello", "world"]
    assert module_0.split_words("hello, world") == ["hello,", "world"]  # space takes priority

    # Branch 2: no space, contains comma -> split on commas
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]

    # Branch 3: no space/comma -> count lowercase letters with even ord()
    assert module_0.split_words("abcd") == 2    # b (98), d (100)
    assert module_0.split_words("hello") == 3   # h (104), l (108), l (108)
    assert module_0.split_words("bdf") == 3     # 98, 100, 102
    assert module_0.split_words("ABC") == 0     # uppercase ignored
    assert module_0.split_words("123") == 0     # digits ignored
    assert module_0.split_words("") == 0

# Generated at 2026-10-24 07:44:05.810633
# Unit test for function split_words
def test_split_words():
    # Branch 1: contains space -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  hello   world  ") == ["hello", "world"]
    assert module_0.split_words("hello, world") == ["hello,", "world"]  # space takes priority

    # Branch 2: no space, contains comma -> split on commas
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]

    # Branch 3: no space/comma -> count lowercase letters with even ord()
    assert module_0.split_words("abcd") == 2    # b (98), d (100)
    assert module_0.split_words("hello") == 3   # h (104), l (108), l (108)
    assert module_0.split_words("bdf") == 3     # 98, 100, 102
    assert module_0.split_words("ABC") == 0     # uppercase ignored
    assert module_0.split_words("123") == 0     # digits ignored
    assert module_0.split_words("") == 0

# Generated at 2026-10-24 07:44:07.130674
# Unit test for function split_words
def test_split_words():
    # Branch 1: contains space -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  hello   world  ") == ["hello", "world"]
    assert module_0.split_words("hello, world") == ["hello,", "world"]  # space takes priority

    # Branch 2: no space, contains comma -> split on commas
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]

    # Branch 3: no space/comma -> count lowercase letters with even ord()
    assert module_0.split_words("abcd") == 2    # b (98), d (100)
    assert module_0.split_words("hello") == 3   # h (104), l (108), l (108)
    assert module_0.split_words("bdf") == 3     # 98, 100, 102
    assert module_0.split_words("ABC") == 0     # uppercase ignored
    assert module_0.split_words("123") == 0     # digits ignored
    assert module_0.split_words("") == 0

# Generated at 2026-10-24 07:44:08.438865
# Unit test for function split_words
def test_split_words():
    # Branch 1: contains space -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  hello   world  ") == ["hello", "world"]
    assert module_0.split_words("hello, world") == ["hello,", "world"]  # space takes priority

    # Branch 2: no space, contains comma -> split on commas
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]

    # Branch 3: no space/comma -> count lowercase letters with even ord()
    assert module_0.split_words("abcd") == 2    # b (98), d (100)
    assert module_0.split_words("hello") == 3   # h (104), l (108), l (108)
    assert module_0.split_words("bdf") == 3     # 98, 100, 102
    assert module_0.split_words("ABC") == 0     # uppercase ignored
    assert module_0.split_words("123") == 0     # digits ignored
    assert module_0.split_words("") == 0

# Generated at 2026-10-24 07:44:09.747107
# Unit test for function split_words
def test_split_words():
    # Branch 1: contains space -> split on whitespace
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]
    assert module_0.split_words("  hello   world  ") == ["hello", "world"]
    assert module_0.split_words("hello, world") == ["hello,", "world"]  # space takes priority

    # Branch 2: no space, contains comma -> split on commas
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("one,two,three") == ["one", "two", "three"]

    # Branch 3: no space/comma -> count lowercase letters with even ord()
    assert module_0.split_words("abcd") == 2    # b (98), d (100)
    assert module_0.split_words("hello") == 3   # h (104), l (108), l (108)
    assert module_0.split_words("bdf") == 3     # 98, 100, 102
    assert module_0.split_words("ABC") == 0     # uppercase ignored
    assert module_0.split_words("123") == 0     # digits ignored
    assert module_0.split_words("") == 0