

# Generated at 2026-11-02 15:20:16.119807
# Unit test for function words_string
def test_words_string():
    # Test empty string
    assert module_0.words_string("") == []
    
    # Test string with commas and spaces
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    
    # Test string with consecutive commas and no spaces
    assert module_0.words_string("One,, two, 3,") == ["One", "two", "3"]
    
    # Test string with commas only, no spaces
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]
    
    # Test string without commas
    assert module_0.words_string("hello world") == ["hello", "world"]
    
    # Test single word
    assert module_0.words_string("hello") == ["hello"]
    
    # Test string with mixed commas, newlines, and spaces
    assert module_0.words_string("One,\ntwo,\nthree") == ["One", "two", "three"]
    
    # Test string of only commas/spaces yields no words
    assert module_0.words_string(" , , ") == []
    
    # Test string with multiple spaces
    assert module_0.words_string("a  b   c") == ["a", "b", "c"]

# Generated at 2026-11-02 15:23:37.528136
# Unit test for function words_string
def test_words_string():
    assert module_0.words_string("") == []
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert module_0.words_string("One,, two, three") == ["One", "two", "three"]
    assert module_0.words_string("Hello World") == ["Hello", "World"]
    assert module_0.words_string("a,b,c") == ["a", "b", "c"]
    assert module_0.words_string(",") == []
    assert module_0.words_string("word") == ["word"]
    assert module_0.words_string("  spaced   out  ") == ["spaced", "out"]
    assert module_0.words_string("one,two three,four") == ["one", "two", "three", "four"]
    assert module_0.words_string(",,,") == []

# Generated at 2026-11-02 15:25:44.978009
# Unit test for function words_string
def test_words_string():
    # Empty string returns empty list
    assert module_0.words_string("") == []
    
    # Single word, no commas
    assert module_0.words_string("hello") == ["hello"]
    
    # Words separated by commas
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]
    
    # Words separated by spaces
    assert module_0.words_string("one two three") == ["one", "two", "three"]
    
    # Mixed commas and spaces
    assert module_0.words_string("one, two, three") == ["one", "two", "three"]
    
    # Comma-space separated (classic example)
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    
    # Consecutive commas act as single separator
    assert module_0.words_string("a,,b") == ["a", "b"]
    
    # Leading and trailing commas
    assert module_0.words_string(",hello,world,") == ["hello", "world"]
    
    # Only commas yields empty list
    assert module_0.words_string(",,,") == []
    
    # Only spaces yields empty list
    assert module_0.words_string("   ") == []
    
    # Single character
    assert module_0.words_string("a") == ["a"]
    
    # Single comma
    assert module_0.words_string(",") == []
    
    # Numbers as words
    assert module_0.words_string("1,2,3") == ["1", "2", "3"]
    
    # Tab and newline separated
    assert module_0.words_string("one\ttwo\nthree") == ["one", "two", "three"]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_words_string()

# Generated at 2026-11-02 15:28:03.241736
# Unit test for function words_string
def test_words_string():import unittest


class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(module_0.words_string(""), [])

    def test_simple_sentence(self):
        self.assertEqual(module_0.words_string("Hi, my name is John"),
                         ["Hi", "my", "name", "is", "John"])

    def test_commas_without_spaces(self):
        self.assertEqual(module_0.words_string("Hi,my,name,is,John"),
                         ["Hi", "my", "name", "is", "John"])

    def test_multiple_consecutive_commas(self):
        self.assertEqual(module_0.words_string("One,, Two, Three"),
                         ["One", "Two", "Three"])

    def test_single_word(self):
        self.assertEqual(module_0.words_string("Hello"), ["Hello"])

    def test_single_comma(self):
        self.assertEqual(module_0.words_string(","), [])

    def test_leading_and_trailing_commas(self):
        self.assertEqual(module_0.words_string(",start,end,"),
                         ["start", "end"])

    def test_only_spaces(self):
        self.assertEqual(module_0.words_string("   "), [])

    def test_mixed_separators(self):
        self.assertEqual(module_0.words_string("a b,c  d, e"), ["a", "b", "c", "d", "e"])


if __name__ == "__main__":
    unittest.main()