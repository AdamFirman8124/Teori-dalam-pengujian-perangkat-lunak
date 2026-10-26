

# Generated at 2026-10-25 09:38:45.615534
# Unit test for function histogram

# Generated at 2026-10-25 09:38:48.028974
# Unit test for function histogram

# Generated at 2026-10-25 09:38:50.442983
# Unit test for function histogram

# Generated at 2026-10-25 09:38:52.857504
# Unit test for function histogram

# Generated at 2026-10-25 09:38:55.272645
# Unit test for function histogram

# Generated at 2026-10-25 09:38:57.685791
# Unit test for function histogram

# Generated at 2026-10-25 09:39:00.100733
# Unit test for function histogram

# Generated at 2026-10-25 09:39:02.515685
# Unit test for function histogram

# Generated at 2026-10-25 09:39:16.786629
# Unit test for function histogram
def test_histogram():
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    assert module_0.histogram("a a b") == {"a": 2}
    assert module_0.histogram("") == {}
    assert module_0.histogram("a b b a c") == {"a": 2, "b": 2}

# Generated at 2026-10-25 09:39:18.130392
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

# Generated at 2026-10-25 09:39:19.497894
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