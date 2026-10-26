

# Generated at 2026-10-25 14:18:30.759894
# Unit test for function histogram
def test_histogram():
    assert module_0.histogram("apple banana apple") == {"apple": 2}
    assert module_0.histogram("cat dog cat dog bird") == {"cat": 2, "dog": 2}
    assert module_0.histogram("hello") == {"hello": 1}
    assert module_0.histogram("") == {}
    assert module_0.histogram("   ") == {}
    assert module_0.histogram("apple  banana apple") == {"apple": 2}

# Generated at 2026-10-25 14:18:53.833454
# Unit test for function histogram
def test_histogram():
    # single winner
    assert module_0.histogram("a b b c") == {"b": 2}
    # tie: every word with the max count is returned
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    assert module_0.histogram("a a b b") == {"a": 2, "b": 2}
    # one word
    assert module_0.histogram("dog") == {"dog": 1}
    # empty / all-space input -> empty dict
    assert module_0.histogram("") == {}
    assert module_0.histogram("   ") == {}
    # repeated spaces are ignored (empty tokens skipped)
    assert module_0.histogram("a  b") == {"a": 1, "b": 1}

# Generated at 2026-10-25 14:19:10.252410
# Unit test for function histogram
def test_histogram():
    # single winner
    assert module_0.histogram("a b b c") == {"b": 2}
    # tie: every word with the max count is returned
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    assert module_0.histogram("a a b b") == {"a": 2, "b": 2}
    # one word
    assert module_0.histogram("dog") == {"dog": 1}
    # empty / all-space input -> empty dict
    assert module_0.histogram("") == {}
    assert module_0.histogram("   ") == {}
    # repeated spaces are ignored (empty tokens skipped)
    assert module_0.histogram("a  b") == {"a": 1, "b": 1}

# Generated at 2026-10-25 14:19:26.874025
# Unit test for function histogram
def test_histogram():
    # most frequent single word
    assert module_0.histogram("a b a c a b") == {"a": 3}

    # tie for most frequent
    assert module_0.histogram("dog cat dog cat bird") == {"dog": 2, "cat": 2}

    # all words unique -> all returned with count 1
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}

    # single word
    assert module_0.histogram("hello") == {"hello": 1}

    # empty string -> empty dict
    assert module_0.histogram("") == {}

    # only spaces -> empty dict
    assert module_0.histogram("   ") == {}

    # extra spaces are ignored
    assert module_0.histogram("a  a b") == {"a": 2}

    # case-sensitive
    assert module_0.histogram("A a A") == {"A": 2}

# Generated at 2026-10-25 14:19:43.461875
# Unit test for function histogram
def test_histogram():
    # single winner
    assert module_0.histogram("a b b c") == {"b": 2}
    # tie: every word with the max count is returned
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    assert module_0.histogram("a a b b") == {"a": 2, "b": 2}
    # one word
    assert module_0.histogram("dog") == {"dog": 1}
    # empty / all-space input -> empty dict
    assert module_0.histogram("") == {}
    assert module_0.histogram("   ") == {}
    # repeated spaces are ignored (empty tokens skipped)
    assert module_0.histogram("a  b") == {"a": 1, "b": 1}