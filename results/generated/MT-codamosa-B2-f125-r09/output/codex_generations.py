

# Generated at 2026-10-24 16:08:50.214519
# Unit test for function split_words
def test_split_words():
    # whitespace branch
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]
    assert module_0.split_words("hello   world") == ["hello", "world"]
    # space takes precedence over comma
    assert module_0.split_words("hello, world") == ["hello,", "world"]

    # comma branch - no spaces
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("a,,b") == ["a", "b"]

    # count branch: no space, no comma -> count lowercase with even ord()
    # b,d,f

# Generated at 2026-10-24 16:08:51.584791
# Unit test for function split_words
def test_split_words():
    # whitespace branch
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]
    assert module_0.split_words("hello   world") == ["hello", "world"]
    # space takes precedence over comma
    assert module_0.split_words("hello, world") == ["hello,", "world"]

    # comma branch - no spaces
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("a,,b") == ["a", "b"]

    # count branch: no space, no comma -> count lowercase with even ord()
    # b,d,f

# Generated at 2026-10-24 16:08:52.977693
# Unit test for function split_words
def test_split_words():
    # whitespace branch
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]
    assert module_0.split_words("hello   world") == ["hello", "world"]
    # space takes precedence over comma
    assert module_0.split_words("hello, world") == ["hello,", "world"]

    # comma branch - no spaces
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("a,,b") == ["a", "b"]

    # count branch: no space, no comma -> count lowercase with even ord()
    # b,d,f

# Generated at 2026-10-24 16:08:54.514081
# Unit test for function split_words
def test_split_words():
    # whitespace branch
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]
    assert module_0.split_words("hello   world") == ["hello", "world"]
    # space takes precedence over comma
    assert module_0.split_words("hello, world") == ["hello,", "world"]

    # comma branch - no spaces
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("a,,b") == ["a", "b"]

    # count branch: no space, no comma -> count lowercase with even ord()
    # b,d,f

# Generated at 2026-10-24 16:08:55.864793
# Unit test for function split_words
def test_split_words():
    # whitespace branch
    assert module_0.split_words("hello world") == ["hello", "world"]
    assert module_0.split_words("a b c") == ["a", "b", "c"]
    assert module_0.split_words("hello   world") == ["hello", "world"]
    # space takes precedence over comma
    assert module_0.split_words("hello, world") == ["hello,", "world"]

    # comma branch - no spaces
    assert module_0.split_words("hello,world") == ["hello", "world"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]
    assert module_0.split_words("a,,b") == ["a", "b"]

    # count branch: no space, no comma -> count lowercase with even ord()
    # b,d,f