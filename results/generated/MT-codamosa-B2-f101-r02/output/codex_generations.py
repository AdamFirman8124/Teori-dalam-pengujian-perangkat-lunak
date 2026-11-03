

# Generated at 2026-11-03 04:50:14.838219
# Unit test for function words_string
def test_words_string():
    assert module_0.words_string("") == []
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert module_0.words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert module_0.words_string("one two three") == ["one", "two", "three"]
    assert module_0.words_string(",") == []
    assert module_0.words_string(",, ,") == []
    assert module_0.words_string("word") == ["word"]
    assert module_0.words_string("a,b,c") == ["a", "b", "c"]
    assert module_0.words_string("  spaced   out  ") == ["spaced", "out"]

# Generated at 2026-11-03 04:52:10.750528
# Unit test for function words_string
def test_words_string():
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert module_0.words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert module_0.words_string("") == []
    assert module_0.words_string("Hello") == ["Hello"]
    assert module_0.words_string("Hello,World") == ["Hello", "World"]
    assert module_0.words_string("Hello, World!") == ["Hello", "World!"]
    assert module_0.words_string("a,b,,c") == ["a", "b", "c"]
    assert module_0.words_string(",") == []
    assert module_0.words_string("  spaces   everywhere  ") == ["spaces", "everywhere"]
    assert module_0.words_string("one,two\nthree") == ["one", "two", "three"]

# Generated at 2026-11-03 04:54:40.055835
# Unit test for function words_string
def test_words_string():
    # Test empty string
    assert module_0.words_string("") == []

    # Test string with commas separating words
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

    # Test string with commas and no spaces
    assert module_0.words_string("One,two,three,four,five,six") == ["One", "two", "three", "four", "five", "six"]

    # Test string with commas and spaces mixed
    assert module_0.words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

    # Test string with no commas
    assert module_0.words_string("Hello World") == ["Hello", "World"]

    # Test string with multiple consecutive commas
    assert module_0.words_string("Hi,,my,,,,name,is,John") == ["Hi", "my", "name", "is", "John"]

    # Test single word
    assert module_0.words_string("Hello") == ["Hello"]

    # Test single word with trailing comma
    assert module_0.words_string("Hello,") == ["Hello"]

    # Test string with only commas
    assert module_0.words_string(",,,,") == []

    # Test string with only spaces
    assert module_0.words_string("   ") == []

    # Test string with mixed separators
    assert module_0.words_string("apple, banana cherry, date") == ["apple", "banana", "cherry", "date"]

    print("All tests passed!")


if __name__ == "__main__":
    test_words_string()

# Generated at 2026-11-03 04:56:36.280254
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

    def test_mixed_separators(self):
        self.assertEqual(module_0.words_string("one, two, three"), ["one", "two", "three"])

    def test_comma_no_spaces(self):
        self.assertEqual(module_0.words_string("Hi,my,name,is,John"), ["Hi", "my", "name", "is", "John"])

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(module_0.words_string("  hello world  "), ["hello", "world"])

    def test_leading_and_trailing_commas(self):
        self.assertEqual(module_0.words_string(",hello,world,"), ["hello", "world"])

    def test_only_commas(self):
        self.assertEqual(module_0.words_string(",,,,"), [])

    def test_only_spaces(self):
        self.assertEqual(module_0.words_string("     "), [])

    def test_consecutive_commas(self):
        self.assertEqual(module_0.words_string("a,,b"), ["a", "b"])

    def test_special_characters(self):
        self.assertEqual(module_0.words_string("a1,b2,c3"), ["a1", "b2", "c3"])

    def test_numbers_as_string(self):
        self.assertEqual(module_0.words_string("1,2,3"), ["1", "2", "3"])

    def test_comma_with_space_after(self):
        self.assertEqual(module_0.words_string("apple, banana, cherry"), ["apple", "banana", "cherry"])


if __name__ == "__main__":
    unittest.main()