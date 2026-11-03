

# Generated at 2026-11-02 12:29:53.170506
# Unit test for function histogram
def test_histogram():
    # All words appear exactly once -> all included with count 1
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}

    # Two words tied at maximum count
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}

    # Mixed counts, max is 2
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}

    # Single dominant word
    assert module_0.histogram("b b b b a") == {"b": 4}

    # Single word input
    assert module_0.histogram("hello") == {"hello": 1}

    # Empty string -> no valid words -> empty dict
    assert module_0.histogram("") == {}

    # Only spaces -> empty strings are ignored -> empty dict
    assert module_0.histogram("   ") == {}

    print("All histogram tests passed!")


if __name__ == "__main__":
    test_histogram()

# Generated at 2026-11-02 12:31:05.873915
# Unit test for function histogram
def test_histogram():
    assert module_0.histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    assert module_0.histogram('a b b a') == {'a': 2, 'b': 2}
    assert module_0.histogram('a b c a b') == {'a': 2, 'b': 2}
    assert module_0.histogram('b b b b a') == {'b': 4}
    assert module_0.histogram('') == {}
    assert module_0.histogram('hello') == {'hello': 1}
    assert module_0.histogram('x y x y z') == {'x': 2, 'y': 2}
    assert module_0.histogram('apple banana apple cherry banana apple') == {'apple': 3}

# Generated at 2026-11-02 12:33:23.180824
# Unit test for function histogram
def test_histogram():
    # Test empty string
    assert module_0.histogram("") == {}, "Empty string should return empty dict"

    # Test single word
    assert module_0.histogram("a") == {"a": 1}, "Single word should return dict with count 1"

    # Test all words tied at count 1
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}, "All tied words should appear"

    # Test tied maximum greater than 1
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}, "Tied maximum should include all max words"

    # Test single repeated word
    assert module_0.histogram("b b b b") == {"b": 4}, "Repeated word should count all occurrences"

    # Test mixed counts, only maximum returned
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}, "Only max-count words should be returned"

    # Test extra spaces (empty tokens ignored)
    assert module_0.histogram("a  b a") == {"a": 2}, "Empty strings from extra spaces should be ignored"

    # Test words with different lengths
    assert module_0.histogram("cat dog cat") == {"cat": 2}, "Unique maximum should be returned"

    print("All tests passed!")


test_histogram()

# Generated at 2026-11-02 12:36:30.855145
# Unit test for function histogram
def test_histogram():
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}
    assert module_0.histogram("b b b b a") == {"b": 4}
    assert module_0.histogram("a b c a b a") == {"a": 3}
    assert module_0.histogram("") == {}
    assert module_0.histogram("word") == {"word": 1}
    assert module_0.histogram("x x y y z z") == {"x": 2, "y": 2, "z": 2}