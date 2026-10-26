

# Generated at 2026-10-25 10:18:17.975629
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

# Generated at 2026-10-25 10:18:34.620033
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

# Generated at 2026-10-25 10:18:51.247054
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

# Generated at 2026-10-25 10:19:07.707057
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

# Generated at 2026-10-25 10:19:09.176211
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