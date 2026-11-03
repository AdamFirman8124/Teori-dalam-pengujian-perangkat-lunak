

# Generated at 2026-11-01 22:00:13.796678
# Unit test for function words_string
def test_words_string():
    # Basic case with commas
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    # Commas replacing spaces
    assert module_0.words_string("One,Two,Three") == ["One", "Two", "Three"]
    # Empty string
    assert module_0.words_string("") == []
    # Single word without separator
    assert module_0.words_string("Hello") == ["Hello"]
    # Only spaces
    assert module_0.words_string("   ") == []
    # Mixed commas and spaces
    assert module_0.words_string("apple, banana cherry,orange") == ["apple", "banana", "cherry", "orange"]
    # Consecutive commas
    assert module_0.words_string("a,,b,c") == ["a", "b", "c"]
    # Leading/trailing separators
    assert module_0.words_string(",start,end,") == ["start", "end"]
    # Only commas
    assert module_0.words_string(",,,") == []
    # Numbers and punctuation as tokens
    assert module_0.words_string("42, x9, hello!") == ["42", "x9", "hello!"]
    # Tab characters treated as whitespace
    assert module_0.words_string("one\ttwo,three") == ["one", "two", "three"]

test_words_string()
print("All tests passed!")

# Generated at 2026-11-01 22:00:59.776371
# Unit test for function words_string
def test_words_string():
    # Basic cases
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert module_0.words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

    # Commas without spaces
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]

    # No commas at all
    assert module_0.words_string("hello world") == ["hello", "world"]
    assert module_0.words_string("single") == ["single"]

    # Empty string
    assert module_0.words_string("") == []

    # Only commas / whitespace
    assert module_0.words_string(", , , ") == []
    assert module_0.words_string("   ") == []

    # Mixed separators (commas + spaces)
    assert module_0.words_string("a,b c,d  e") == ["a", "b", "c", "d", "e"]

    # Leading/trailing commas and spaces
    assert module_0.words_string(",start,end,") == ["start", "end"]
    assert module_0.words_string("  leading and trailing  ") == ["leading", "and", "trailing"]

    # Single character
    assert module_0.words_string("a") == ["a"]
    assert module_0.words_string(",") == []

    print("All tests passed!")


if __name__ == "__main__":
    test_words_string()

# Generated at 2026-11-01 22:01:52.512483
# Unit test for function words_string
def test_words_string():
    # Test empty string
    assert module_0.words_string("") == []

    # Test single word
    assert module_0.words_string("hello") == ["hello"]

    # Test words separated by commas
    assert module_0.words_string("one,two,three") == ["one", "two", "three"]

    # Test words separated by spaces
    assert module_0.words_string("one two three") == ["one", "two", "three"]

    # Test mixed commas and spaces
    assert module_0.words_string("one, two, three") == ["one", "two", "three"]

    # Test comma with no space after
    assert module_0.words_string("Hi,my,name,is,John") == ["Hi", "my", "name", "is", "John"]

    # Test sentence with commas (classic example)
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

    # Test leading/trailing whitespace
    assert module_0.words_string("  hello world  ") == ["hello", "world"]

    # Test only commas
    assert module_0.words_string(",,,") == []

    # Test string with only whitespace
    assert module_0.words_string("   ") == []

    # Test consecutive commas
    assert module_0.words_string("a,,b") == ["a", "b"]

    # Test single character
    assert module_0.words_string("a") == ["a"]

    # Test comma at start and end
    assert module_0.words_string(",hello,world,") == ["hello", "world"]

    # Test numbers as words
    assert module_0.words_string("1,2,3") == ["1", "2", "3"]

    print("All test cases passed!")


if __name__ == "__main__":
    test_words_string()

# Generated at 2026-11-01 22:02:45.918552
# Unit test for function words_string
def test_words_string():
    # Test empty string
    assert module_0.words_string("") == []
    
    # Test simple sentence with spaces
    assert module_0.words_string("Hello world") == ["Hello", "world"]
    
    # Test comma-separated words
    assert module_0.words_string("One,two,three") == ["One", "two", "three"]
    
    # Test mixed commas and spaces
    assert module_0.words_string("One, two, three") == ["One", "two", "three"]
    
    # Test multiple consecutive commas
    assert module_0.words_string("a,,b,c") == ["a", "b", "c"]
    
    # Test single word no separator
    assert module_0.words_string("hello") == ["hello"]
    
    # Test single word with trailing comma
    assert module_0.words_string("hello,") == ["hello"]
    
    # Test leading comma
    assert module_0.words_string(",hello") == ["hello"]
    
    # Test only commas
    assert module_0.words_string(",,,") == []
    
    # Test only spaces
    assert module_0.words_string("   ") == []
    
    # Test comma as space replacement preserves other punctuation
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    
    # Test numbers as words
    assert module_0.words_string("1,2,3") == ["1", "2", "3"]
    
    print("All tests passed!")

# Generated at 2026-11-01 22:03:07.161313
# Unit test for function words_string
def test_words_string():
    # Empty string returns empty list
    assert module_0.words_string("") == []

    # None input returns empty list
    assert module_0.words_string(None) == []

    # Single word with no separators
    assert module_0.words_string("hello") == ["hello"]

    # Words separated by spaces
    assert module_0.words_string("hello world foo") == ["hello", "world", "foo"]

    # Words separated by commas
    assert module_0.words_string("hello,world,foo") == ["hello", "world", "foo"]

    # Mixed commas and spaces
    assert module_0.words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

    # Classic example from spec
    assert module_0.words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

    # Consecutive commas collapse into whitespace
    assert module_0.words_string("One,, two, three") == ["One", "two", "three"]

    # String with only commas/spaces yields empty list
    assert module_0.words_string(" , , ") == []

    # Comma-separated with no spaces
    assert module_0.words_string("One,two,three,four,five") == ["One", "two", "three", "four", "five"]

    # Leading/trailing separators are ignored by split()
    assert module_0.words_string(",start middle end,") == ["start", "middle", "end"]