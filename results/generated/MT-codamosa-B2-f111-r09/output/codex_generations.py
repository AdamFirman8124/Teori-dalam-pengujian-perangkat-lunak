

# Generated at 2026-11-03 03:10:58.890225
# Unit test for function histogram
def test_histogram():
    # All words appear once -> all included
    assert module_0.histogram("a b c") == {'a': 1, 'b': 1, 'c': 1}
    # Tie between two words
    assert module_0.histogram("a b b a") == {'a': 2, 'b': 2}
    assert module_0.histogram("a b c a b") == {'a': 2, 'b': 2}
    # Single word with max count
    assert module_0.histogram("b b b b a") == {'b': 4}
    # Empty string -> empty dict
    assert module_0.histogram("") == {}
    # Single word input
    assert module_0.histogram("a") == {'a': 1}
    # Mixed counts
    assert module_0.histogram("cat dog cat dog bird") == {'cat': 2, 'dog': 2}
    # Extra spaces produce empty tokens that are ignored
    assert module_0.histogram("a  a b") == {'a': 2}
    # Longest max count word only
    assert module_0.histogram("x y y z z z") == {'z': 3}

test_histogram()
print("All tests passed!")

# Generated at 2026-11-03 03:12:56.963595
# Unit test for function histogram
def test_histogram():
    # Single word repeated
    assert module_0.histogram("a b b") == {"b": 2}
    # All words appear once
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    # Tie for maximum count
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}
    # One dominant word
    assert module_0.histogram("b b b b a") == {"b": 4}
    # Empty string input
    assert module_0.histogram("") == {}
    # Only whitespace
    assert module_0.histogram("   ") == {}
    # Single word input
    assert module_0.histogram("hello") == {"hello": 1}
    # Three occurrences of one word
    assert module_0.histogram("a a a b b c") == {"a": 3}
    # Alternating words
    assert module_0.histogram("x y x y x") == {"x": 3}
    # Multiple words tied at higher count
    assert module_0.histogram("cat dog cat dog bird") == {"cat": 2, "dog": 2}
    # Longer string with clear winner
    assert module_0.histogram("one two one three one") == {"one": 3}

# Generated at 2026-11-03 03:13:35.054539
# Unit test for function histogram
def test_histogram():
    # Test with all unique words (equal counts)
    assert module_0.histogram("a b c") == {'a': 1, 'b': 1, 'c': 1}

    # Test with two words tied at max count
    assert module_0.histogram("a b b a") == {'a': 2, 'b': 2}

    # Test with mixed counts, tie at top
    assert module_0.histogram("a b c a b") == {'a': 2, 'b': 2}

    # Test with single dominant word
    assert module_0.histogram("b b b b a") == {'b': 4}

    # Test with empty string
    assert module_0.histogram("") == {}

    # Test with single word
    assert module_0.histogram("a") == {'a': 1}

    # Test with words and repeated pattern
    assert module_0.histogram("cat dog cat dog bird") == {'cat': 2, 'dog': 2}

    # Test with larger counts
    assert module_0.histogram("x y x y x") == {'x': 3}

    print("All histogram tests passed!")


test_histogram()

# Generated at 2026-11-03 03:14:30.234393
# Unit test for function histogram
def test_histogram():
    # Empty string returns empty dict
    assert module_0.histogram('') == {}

    # All words appear once -> all included with count 1
    assert module_0.histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}

    # Two words tied for max count
    assert module_0.histogram('a b b a') == {'a': 2, 'b': 2}
    assert module_0.histogram('a b c a b') == {'a': 2, 'b': 2}

    # Single word repeated
    assert module_0.histogram('b b b b a') == {'b': 4}

    # One word clearly has max count
    assert module_0.histogram('a b c a a') == {'a': 3}
    assert module_0.histogram('hello') == {'hello': 1}

    # Words with more than one character
    assert module_0.histogram('cat dog cat dog bird') == {'cat': 2, 'dog': 2}
    assert module_0.histogram('apple banana apple') == {'apple': 2}

    # Multiple spaces leading to empty string tokens
    assert module_0.histogram('a  b') == {'a': 1, 'b': 1}

    print("All histogram tests passed!")


if __name__ == "__main__":
    test_histogram()

# Generated at 2026-11-03 03:15:04.448094
# Unit test for function histogram
def test_histogram():
    # Test with empty string
    assert module_0.histogram("") == {}

    # Test with single word
    assert module_0.histogram("a") == {"a": 1}

    # Test with all unique words (all tie with count 1)
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}

    # Test with two words tied for max count
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}

    # Test with mixed counts, ties at the top
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}

    # Test with one dominant word
    assert module_0.histogram("b b b b") == {"b": 4}

    # Test with a word appearing more than others
    assert module_0.histogram("apple banana apple cherry banana apple") == {"apple": 3}

    # Test with extra spaces (empty strings ignored)
    assert module_0.histogram("a  a  b") == {"a": 2}

    # Test with repeated spaces only
    assert module_0.histogram("   ") == {}

    print("All tests passed!")


test_histogram()