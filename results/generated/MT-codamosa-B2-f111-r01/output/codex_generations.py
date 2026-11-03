

# Generated at 2026-11-02 17:59:09.738629
# Unit test for function histogram
def test_histogram():
    # All unique words with count 1
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    
    # Multiple words tied at max count
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}
    
    # Single word dominating
    assert module_0.histogram("b b b b a") == {"b": 4}
    assert module_0.histogram("x x y") == {"x": 2}
    
    # Single word input
    assert module_0.histogram("a") == {"a": 1}
    assert module_0.histogram("hello") == {"hello": 1}
    
    # Empty string and whitespace-only input
    assert module_0.histogram("") == {}
    assert module_0.histogram("   ") == {}
    
    # Mixed words with ties
    assert module_0.histogram("cat dog cat dog bird") == {"cat": 2, "dog": 2}
    assert module_0.histogram("apple banana apple banana cherry") == {"apple": 2, "banana": 2}
    
    # Leading/trailing spaces create empty entries that are ignored
    assert module_0.histogram(" a b ") == {"a": 1, "b": 1}
    
    # Repeated pattern
    assert module_0.histogram("a a a b c c c") == {"a": 3, "c": 3}
    
    # Long repeated single word
    assert module_0.histogram("z z z z z") == {"z": 5}

# Generated at 2026-11-02 18:00:36.783053
# Unit test for function histogram
def test_histogram():
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}
    assert module_0.histogram("b b b b a") == {"b": 4}
    assert module_0.histogram("") == {}
    assert module_0.histogram("hello") == {"hello": 1}
    assert module_0.histogram("a a a b b c") == {"a": 3}
    assert module_0.histogram("x y") == {"x": 1, "y": 1}
    assert module_0.histogram("word word word") == {"word": 3}
    assert module_0.histogram("cat dog bird cat dog") == {"cat": 2, "dog": 2}

# Generated at 2026-11-02 18:02:53.815614
# Unit test for function histogram
def test_histogram():import unittest


class TestHistogram(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(module_0.histogram(""), {})

    def test_single_word(self):
        self.assertEqual(module_0.histogram("a"), {"a": 1})

    def test_all_unique_words(self):
        self.assertEqual(module_0.histogram("a b c"), {"a": 1, "b": 1, "c": 1})

    def test_two_words_equal_max(self):
        self.assertEqual(module_0.histogram("a b b a"), {"a": 2, "b": 2})

    def test_two_max_words_uneven(self):
        self.assertEqual(module_0.histogram("a b c a b"), {"a": 2, "b": 2})

    def test_single_repeated_word(self):
        self.assertEqual(module_0.histogram("b b"), {"b": 2})

    def test_word_with_higher_count(self):
        self.assertEqual(module_0.histogram("hello world hello"), {"hello": 2})

    def test_extra_spaces(self):
        # Empty strings from double spaces are ignored
        self.assertEqual(module_0.histogram("a  b"), {"a": 1, "b": 1})

    def test_three_occurrences(self):
        self.assertEqual(module_0.histogram("x y x z x"), {"x": 3})

    def test_only_spaces(self):
        self.assertEqual(module_0.histogram("   "), {})

    def test_returns_dict_type(self):
        self.assertIsInstance(module_0.histogram("a b"), dict)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 18:05:01.833851
# Unit test for function histogram
def test_histogram():import unittest


class TestHistogram(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(module_0.histogram("a"), {"a": 1})

    def test_all_unique(self):
        self.assertEqual(module_0.histogram("a b c"), {"a": 1, "b": 1, "c": 1})

    def test_tie_between_words(self):
        self.assertEqual(module_0.histogram("a b b a"), {"a": 2, "b": 2})

    def test_mixed_counts(self):
        self.assertEqual(module_0.histogram("a b c a b"), {"a": 2, "b": 2})

    def test_single_word_repeated(self):
        self.assertEqual(module_0.histogram("b b b b"), {"b": 4})

    def test_max_wins(self):
        self.assertEqual(module_0.histogram("a b c c b b"), {"b": 3})

    def test_empty_string(self):
        self.assertEqual(module_0.histogram(""), {})

    def test_three_way_tie(self):
        self.assertEqual(module_0.histogram("x y z x y z"), {"x": 2, "y": 2, "z": 2})

    def test_words_with_numbers(self):
        self.assertEqual(module_0.histogram("1 2 3 2"), {"2": 2})

    def test_longer_sentence(self):
        self.assertEqual(module_0.histogram("apple banana apple cherry banana apple"),
                         {"apple": 3})


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 18:06:54.020236
# Unit test for function histogram
def test_histogram():
    # Single word repeated
    assert module_0.histogram("b b") == {"b": 2}

    # All words appear once
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}

    # Tie for maximum count
    assert module_0.histogram("a b b a") == {"a": 2, "b": 2}

    # One word dominates the count
    assert module_0.histogram("b b b b a") == {"b": 4}

    # Mixed duplicates with a max tie
    assert module_0.histogram("a b c a b") == {"a": 2, "b": 2}

    # Single occurrence of one word
    assert module_0.histogram("hello") == {"hello": 1}

    # Empty string returns empty dict
    assert module_0.histogram("") == {}

    # Whitespace-only string returns empty dict
    assert module_0.histogram("   ") == {}

    # Longer sentence with repeated word
    assert module_0.histogram("the cat and the dog and the bird") == {"the": 3, "and": 2}

    # Three-way tie
    assert module_0.histogram("x y z x y z") == {"x": 2, "y": 2, "z": 2}