

# Generated at 2026-11-01 21:09:31.364300
# Unit test for function histogram
def test_histogram():
    # All words appear once
    assert module_0.histogram("a b c") == {'a': 1, 'b': 1, 'c': 1}, "Failed on all unique words"

    # Tie between two most frequent words
    assert module_0.histogram("a b b a") == {'a': 2, 'b': 2}, "Failed on tie between two words"

    # Single most frequent word
    assert module_0.histogram("a b c a") == {'a': 2}, "Failed on single most frequent word"

    # Multiple repeats, one winner
    assert module_0.histogram("b b b b a b") == {'b': 5}, "Failed on dominant word"

    # Words with different lengths
    assert module_0.histogram("apple banana apple banana orange") == {'apple': 2, 'banana': 2}, \
        "Failed on multi-char words"

    # Single word input
    assert module_0.histogram("hello") == {'hello': 1}, "Failed on single word"

    # Empty string
    assert module_0.histogram("") == {}, "Failed on empty string"

    # Only spaces
    assert module_0.histogram("   ") == {}, "Failed on whitespace-only string"

    print("All tests passed!")


test_histogram()

# Generated at 2026-11-01 21:09:58.799713
# Unit test for function histogram
def test_histogram():
    # Empty string returns an empty dictionary
    assert module_0.histogram('') == {}

    # Single word
    assert module_0.histogram('a') == {'a': 1}

    # All words appear once
    assert module_0.histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}

    # Ties: multiple words share the maximum count
    assert module_0.histogram('a b b a') == {'a': 2, 'b': 2}
    assert module_0.histogram('a b c a b') == {'a': 2, 'b': 2}

    # Single word dominates
    assert module_0.histogram('b b b b a') == {'b': 4}

    # Repeated multi-character word
    assert module_0.histogram('aa aa aa') == {'aa': 3}

    # Word appearing only once among others with higher counts
    assert module_0.histogram('a a b c') == {'a': 2}

    # Longer mixed case
    assert module_0.histogram('x y z x y x') == {'x': 3}

    print("All histogram tests passed!")


if __name__ == "__main__":
    test_histogram()

# Generated at 2026-11-01 21:10:33.150971
# Unit test for function histogram
def test_histogram():
    # Test empty string
    assert module_0.histogram("") == {}, "Failed: empty string should return {}"

    # Test single word
    assert module_0.histogram("a") == {"a": 1}, "Failed: single word"

    # Test multiple unique words (all tie at count 1)
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}, "Failed: all unique words"

    # Test words with tied maximum counts
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}, "Failed: tied max counts"

    # Test mixed frequencies (only max-count words kept)
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}, "Failed: mixed frequencies"

    # Test one dominant word
    assert module_0.histogram("b b b b a") == {"b": 4}, "Failed: dominant word"

    # Test longer words
    assert module_0.histogram("apple banana apple banana cherry") == {"apple": 2, "banana": 2}, \
        "Failed: longer words with ties"

    # Verify result type
    assert isinstance(module_0.histogram("x y z"), dict), "Failed: result must be a dict"

    print("All histogram tests passed!")


if __name__ == "__main__":
    test_histogram()

# Generated at 2026-11-01 21:11:25.235174
# Unit test for function histogram
def test_histogram():
    # Empty string returns empty dict
    assert module_0.histogram("") == {}

    # Single word
    assert module_0.histogram("a") == {"a": 1}

    # Tied maximum counts
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}

    # Single dominant word
    assert module_0.histogram("b b b b a") == {"b": 4}

    # All words appear once
    assert module_0.histogram("a b c d g") == {"a": 1, "b": 1, "c": 1, "d": 1, "g": 1}
    assert module_0.histogram("r t g") == {"r": 1, "t": 1, "g": 1}
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}

    # Only the most frequent word(s) are kept
    assert module_0.histogram("hello world hello") == {"hello": 2}
    assert module_0.histogram("x y x z z") == {"x": 2, "z": 2}

    # Longer words
    assert module_0.histogram("cat dog cat") == {"cat": 2}
    assert module_0.histogram("apple banana apple banana cherry") == {"apple": 2, "banana": 2}

# Generated at 2026-11-01 21:12:17.220399
# Unit test for function histogram
def test_histogram():
    # Test with a single word
    assert module_0.histogram("a") == {'a': 1}

    # Test with multiple words, some repeated
    assert module_0.histogram("a b b a c") == {'a': 2, 'b': 2}

    # Test with all identical words
    assert module_0.histogram("b b b b") == {'b': 4}

    # Test with empty string
    assert module_0.histogram("") == {}

    # Test with all unique words (each appears once)
    assert module_0.histogram("a b c") == {'a': 1, 'b': 1, 'c': 1}

    # Test with multiple words tied for max frequency
    assert module_0.histogram("two two three three four") == {'two': 2, 'three': 2}

    # Test with a longer sentence
    assert module_0.histogram("the quick brown fox the lazy dog the end") == {'the': 3}

    # Test with mixed repeated words
    assert module_0.histogram("x y z x y z x") == {'x': 3}

    print("All tests passed!")


test_histogram()