

# Generated at 2026-10-24 06:04:17.668981
# Unit test for function words_string
def test_words_string():
    assert module_0.words_string("") == []
    assert module_0.words_string("hello") == ["hello"]
    assert module_0.words_string("hello,world") == ["hello", "world"]
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]
    assert module_0.words_string("one, two, three") == ["one", "two", "three"]
    assert module_0.words_string("one,,three") == ["one", "three"]

# Generated at 2026-10-24 06:04:21.857201
# Unit test for function words_string
def test_words_string():
    assert module_0.words_string("") == []
    assert module_0.words_string("hello") == ["hello"]
    assert module_0.words_string("hello,world") == ["hello", "world"]
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]
    assert module_0.words_string("one, two, three") == ["one", "two", "three"]
    assert module_0.words_string(",hello,,world,") == ["hello", "world"]

# Generated at 2026-10-24 06:04:27.713965
# Unit test for function words_string
def test_words_string():
    assert module_0.words_string("hello,world") == ["hello", "world"]
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]
    assert module_0.words_string("single") == ["single"]
    assert module_0.words_string("") == []
    assert module_0.words_string("hello, world") == ["hello", "world"]
    assert module_0.words_string("one,,two") == ["one", "two"]

# Generated at 2026-10-24 06:04:33.009067
# Unit test for function words_string
def test_words_string():
    assert module_0.words_string("") == []
    assert module_0.words_string("hello") == ["hello"]
    assert module_0.words_string("hello,world") == ["hello", "world"]
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]
    assert module_0.words_string("one,,two") == ["one", "two"]
    assert module_0.words_string(",one,two,") == ["one", "two"]
    assert module_0.words_string("hello world,test") == ["hello", "world", "test"]

# Generated at 2026-10-24 06:04:38.162498
# Unit test for function words_string
def test_words_string():
    assert module_0.words_string("hello,world") == ["hello", "world"]
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]
    assert module_0.words_string("single") == ["single"]
    assert module_0.words_string("") == []
    assert module_0.words_string("one, two,  three") == ["one", "two", "three"]
    assert module_0.words_string("one,,three") == ["one", "three"]