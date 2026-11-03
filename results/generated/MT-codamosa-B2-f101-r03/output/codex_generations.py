

# Generated at 2026-11-03 02:31:11.870460
# Unit test for function words_string
def test_words_string():
    # Empty string returns empty list
    assert module_0.words_string("") == []

    # Simple comma-separated string
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

    # Commas replacing spaces
    assert module_0.words_string("One,Two,Three") == ["One", "Two", "Three"]

    # Mixed commas and spaces
    assert module_0.words_string("One, Two, Three") == ["One", "Two", "Three"]

    # Single word, no separators
    assert module_0.words_string("Hello") == ["Hello"]

    # Only a comma
    assert module_0.words_string(",") == []

    # Multiple consecutive commas
    assert module_0.words_string("a,,b") == ["a", "b"]

    # Extra whitespace is handled
    assert module_0.words_string("  spaced   out  words ") == ["spaced", "out", "words"]

    # Comma with surrounding whitespace
    assert module_0.words_string("apple, banana ,cherry") == ["apple", "banana", "cherry"]

    # String with only whitespace
    assert module_0.words_string("   ") == []

    # Numbers as words
    assert module_0.words_string("1,2,3") == ["1", "2", "3"]

    print("All tests passed!")

# Generated at 2026-11-03 02:32:48.383040
# Unit test for function words_string
def test_words_string():
    # Test empty string
    assert module_0.words_string("") == []

    # Test simple string with spaces
    assert module_0.words_string("Hello World") == ["Hello", "World"]

    # Test string with commas as separators
    assert module_0.words_string("Hello,World") == ["Hello", "World"]

    # Test string with comma followed by space
    assert module_0.words_string("Hello, World") == ["Hello", "World"]

    # Test string with comma and no space
    assert module_0.words_string("One,Two,Three,Four,Five") == ["One", "Two", "Three", "Four", "Five"]

    # Test string with multiple spaces
    assert module_0.words_string("One   Two  Three") == ["One", "Two", "Three"]

    # Test string with mixed commas and spaces
    assert module_0.words_string("Hi, my name, is John") == ["Hi", "my", "name", "is", "John"]

    # Test leading and trailing commas
    assert module_0.words_string(",Hello,World,") == ["Hello", "World"]

    # Test leading and trailing spaces
    assert module_0.words_string("  Hello World  ") == ["Hello", "World"]

    # Test string with only a comma
    assert module_0.words_string(",") == []

    # Test string with only spaces
    assert module_0.words_string("   ") == []

    # Test single word
    assert module_0.words_string("Hello") == ["Hello"]

    # Test string with only commas and spaces
    assert module_0.words_string(", , ,") == []

# Generated at 2026-11-03 02:34:22.078796
# Unit test for function words_string
def test_words_string():
    # Test with empty string
    assert module_0.words_string("") == []
    
    # Test with commas as separators
    assert module_0.words_string("Hi, my name, is, John") == ["Hi", "my", "name", "is", "John"]
    
    # Test with spaces as separators
    assert module_0.words_string("Hi my name is John") == ["Hi", "my", "name", "is", "John"]
    
    # Test with mixed commas and spaces
    assert module_0.words_string("One,, two, three") == ["One", "", "two", "three"]
    
    # Test with only commas
    assert module_0.words_string(",") == []
    
    # Test with a single word
    assert module_0.words_string("hello") == ["hello"]
    
    # Test with a single comma-separated word
    assert module_0.words_string("hello,") == ["hello"]
    
    # Test with leading and trailing spaces
    assert module_0.words_string("  hello world  ") == ["hello", "world"]
    
    # Test with newline characters
    assert module_0.words_string("hello\nworld") == ["hello", "world"]
    
    # Test with tab characters
    assert module_0.words_string("hello\tworld") == ["hello", "world"]
    
    # Test with numbers
    assert module_0.words_string("1, 2, 3") == ["1", "2", "3"]
    
    # Test with special characters
    assert module_0.words_string("!@#, $%^, &*()") == ["!@#", "$%^", "&*()"]
    
    # Test with multiple consecutive commas and spaces
    assert module_0.words_string("a,  , b") == ["a", "b"]
    
    # Test with very long string
    assert module_0.words_string("a,b,c,d,e,f,g") == ["a", "b", "c", "d", "e", "f", "g"]
    
    print("All test cases passed!")

test_words_string()

# Generated at 2026-11-03 02:35:02.135325
# Unit test for function words_string
def test_words_string():
    # Empty string returns empty list
    assert module_0.words_string("") == []

    # Single word, no separators
    assert module_0.words_string("hello") == ["hello"]

    # Words separated by spaces
    assert module_0.words_string("hello world") == ["hello", "world"]

    # Words separated by commas
    assert module_0.words_string("hello,world") == ["hello", "world"]

    # Comma-separated with spaces
    assert module_0.words_string("one, two, three") == ["one", "two", "three"]

    # Multiple consecutive commas
    assert module_0.words_string("a,,b") == ["a", "b"]

    # Leading and trailing separators
    assert module_0.words_string(",hello,world,") == ["hello", "world"]

    # Comma-only string
    assert module_0.words_string(",,,") == []

    # Whitespace-only string
    assert module_0.words_string("   ") == []

    # Mixed separators with punctuation in words
    assert module_0.words_string("Hi, my name, is John") == ["Hi", "my", "name", "is", "John"]

    print("All tests passed!")


if __name__ == "__main__":
    test_words_string()

# Generated at 2026-11-03 02:36:07.519932
# Unit test for function words_string
def test_words_string():import unittest


class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(module_0.words_string(""), [])

    def test_single_word(self):
        self.assertEqual(module_0.words_string("hello"), ["hello"])

    def test_comma_separated(self):
        self.assertEqual(module_0.words_string("one,two,three"), ["one", "two", "three"])

    def test_space_separated(self):
        self.assertEqual(module_0.words_string("one two three"), ["one", "two", "three"])

    def test_mixed_commas_and_spaces(self):
        self.assertEqual(module_0.words_string("one, two, three"), ["one", "two", "three"])

    def test_comma_no_space(self):
        self.assertEqual(module_0.words_string("Hi,my,name,is,John"), ["Hi", "my", "name", "is", "John"])

    def test_comma_with_space(self):
        self.assertEqual(module_0.words_string("Hi, my, name, is, John"), ["Hi", "my", "name", "is", "John"])

    def test_leading_and_trailing_commas(self):
        self.assertEqual(module_0.words_string(",hello,world,"), ["hello", "world"])

    def test_only_commas(self):
        self.assertEqual(module_0.words_string(",,,,"), [])

    def test_only_spaces(self):
        self.assertEqual(module_0.words_string("   "), [])

    def test_multiple_consecutive_commas(self):
        self.assertEqual(module_0.words_string("a,,b"), ["a", "b"])

    def test_single_comma(self):
        self.assertEqual(module_0.words_string(","), [])

    def test_numbers_as_string(self):
        self.assertEqual(module_0.words_string("1,2,3"), ["1", "2", "3"])

    def test_words_with_punctuation(self):
        self.assertEqual(module_0.words_string("Hello, world!"), ["Hello", "world!"])

    def test_tab_and_newline_separators(self):
        self.assertEqual(module_0.words_string("one\ttwo\nthree"), ["one", "two", "three"])


if __name__ == "__main__":
    unittest.main()