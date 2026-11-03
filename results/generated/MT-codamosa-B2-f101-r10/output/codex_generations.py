

# Generated at 2026-11-02 21:39:52.413025
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
    
    # Comma with no space after
    assert module_0.words_string("Hi,my,name,is,John") == ["Hi", "my", "name", "is", "John"]
    
    # Leading/trailing whitespace gets stripped by split
    assert module_0.words_string("  hello world  ") == ["hello", "world"]
    
    # String of only commas acts as whitespace separators
    assert module_0.words_string(",,,") == []
    
    # Consecutive commas collapse into separators
    assert module_0.words_string("a,,b") == ["a", "b"]
    
    # Single word followed by comma
    assert module_0.words_string("hello,") == ["hello"]

# Generated at 2026-11-02 21:41:13.394639
# Unit test for function words_string
def test_words_string():
    # Test empty string
    assert module_0.words_string("") == []
    
    # Test None-like empty check
    assert module_0.words_string("") != None
    
    # Test simple sentence with spaces
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    
    # Test sentence with commas only
    assert module_0.words_string("Hi,my,name,is,John") == ["Hi", "my", "name", "is", "John"]
    
    # Test single word
    assert module_0.words_string("Hello") == ["Hello"]
    
    # Test single word followed by comma
    assert module_0.words_string("Hello,") == ["Hello"]
    
    # Test comma at the beginning
    assert module_0.words_string(",Hello") == ["Hello"]
    
    # Test multiple consecutive commas
    assert module_0.words_string("one,,two,,,three") == ["one", "two", "three"]
    
    # Test mixed commas and spaces
    assert module_0.words_string("apple, banana cherry,date , elderberry") == ["apple", "banana", "cherry", "date", "elderberry"]
    
    # Test string with only commas
    assert module_0.words_string(",,,") == []
    
    # Test string with only spaces
    assert module_0.words_string("   ") == []
    
    # Test one-word comma-separated
    assert module_0.words_string("One,") == ["One"]
    
    print("All test cases passed!")

# Generated at 2026-11-02 21:42:38.387964
# Unit test for function words_string
def test_words_string():
    # Test with empty string
    assert module_0.words_string("") == []
    
    # Test with simple comma-separated words
    assert module_0.words_string("One, two, three") == ["One", "two", "three"]
    
    # Test with commas only (no spaces)
    assert module_0.words_string("One,two,three") == ["One", "two", "three"]
    
    # Test with spaces only
    assert module_0.words_string("One two three") == ["One", "two", "three"]
    
    # Test with mixed commas and spaces
    assert module_0.words_string("Hi, my name,is John") == ["Hi", "my", "name", "is", "John"]
    
    # Test with multiple consecutive commas
    assert module_0.words_string("One,,two,,,three") == ["One", "two", "three"]
    
    # Test with single word
    assert module_0.words_string("hello") == ["hello"]
    
    # Test with single word followed by comma
    assert module_0.words_string("hello,") == ["hello"]
    
    # Test with leading/trailing spaces
    assert module_0.words_string("  hello   world  ") == ["hello", "world"]
    
    # Test with only commas
    assert module_0.words_string(",,,") == []
    
    # Test with tabs and newlines as whitespace
    assert module_0.words_string("one,\ttwo\nthree") == ["one", "two", "three"]
    
    print("All tests passed!")

# Generated at 2026-11-02 21:44:26.904333
# Unit test for function words_string
def test_words_string():
    # Test with spaces as delimiters
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    # Test with commas as delimiters
    assert module_0.words_string("One,,Two,Three") == ["One", "Two", "Three"]
    # Test with commas and spaces mixed
    assert module_0.words_string("Hello, world, foo, bar") == ["Hello", "world", "foo", "bar"]
    # Test with single word
    assert module_0.words_string("Python") == ["Python"]
    # Test with empty string
    assert module_0.words_string("") == []
    # Test with only delimiters
    assert module_0.words_string(", , ,") == []
    # Test with leading/trailing delimiters
    assert module_0.words_string(",start,end,") == ["start", "end"]
    print("All tests passed!")

test_words_string()

# Generated at 2026-11-02 21:46:25.003140
# Unit test for function words_string
def test_words_string():
    # Test empty string
    assert module_0.words_string("") == []
    assert module_0.words_string("") == []

    # Test string with commas as separators
    assert module_0.words_string("Hi, my, name, is, John") == ["Hi", "my", "name", "is", "John"]

    # Test string with spaces only
    assert module_0.words_string("Hello world") == ["Hello", "world"]

    # Test string with only commas
    assert module_0.words_string("apple,banana,cherry") == ["apple", "banana", "cherry"]

    # Test mixed commas and spaces
    assert module_0.words_string("one, two three, four") == ["one", "two", "three", "four"]

    # Test single word
    assert module_0.words_string("hello") == ["hello"]

    # Test string with only whitespace
    assert module_0.words_string("   ") == []

    # Test string with only commas
    assert module_0.words_string(",,,") == []

    # Test leading/trailing commas
    assert module_0.words_string(",start,end,") == ["start", "end"]

    # Test consecutive commas
    assert module_0.words_string("a,,b") == ["a", "b"]

    # Test comma adjacent to words without spaces
    assert module_0.words_string("Hi,my,name,is,John") == ["Hi", "my", "name", "is", "John"]

    print("All tests passed!")


if __name__ == "__main__":
    test_words_string()