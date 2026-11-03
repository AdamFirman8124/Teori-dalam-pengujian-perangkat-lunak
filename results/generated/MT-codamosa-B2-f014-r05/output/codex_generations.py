

# Generated at 2026-11-02 06:41:25.876104
# Unit test for function all_prefixes
def test_all_prefixes():
    # Test with a basic string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    
    # Test with a single character
    assert module_0.all_prefixes("a") == ["a"]
    
    # Test with an empty string
    assert module_0.all_prefixes("") == []
    
    # Test with a longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    
    # Test with string containing spaces
    assert module_0.all_prefixes("ab c") == ["a", "ab", "ab ", "ab c"]
    
    # Test with special characters
    assert module_0.all_prefixes("!@") == ["!", "!@"]
    
    # Test with numbers
    assert module_0.all_prefixes("123") == ["1", "12", "123"]
    
    # Test with repeated characters
    assert module_0.all_prefixes("aaa") == ["a", "aa", "aaa"]
    
    # Test result length matches string length
    s = "python"
    assert len(module_0.all_prefixes(s)) == len(s)
    
    # Test each prefix is progressively longer
    prefixes = module_0.all_prefixes("test")
    for i, p in enumerate(prefixes):
        assert p == "test"[:i+1]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-02 06:42:57.074724
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes('') == []
    assert module_0.all_prefixes('a') == ['a']
    assert module_0.all_prefixes('ab') == ['a', 'ab']
    assert module_0.all_prefixes('abc') == ['a', 'ab', 'abc']
    assert module_0.all_prefixes('asdf') == ['a', 'as', 'asd', 'asdf']
    assert module_0.all_prefixes('xyz') == ['x', 'xy', 'xyz']
    assert module_0.all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
    assert module_0.all_prefixes(' ') == [' ']
    assert module_0.all_prefixes('aa') == ['a', 'aa']

# Generated at 2026-11-02 06:44:21.190105
# Unit test for function all_prefixes
def test_all_prefixes():
    # Test with a simple string
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # Test with a single character string
    assert module_0.all_prefixes("a") == ["a"]

    # Test with an empty string
    assert module_0.all_prefixes("") == []

    # Test with a longer string
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

    # Test with a string containing spaces
    assert module_0.all_prefixes("ab cd") == ["a", "ab", "ab ", "ab c", "ab cd"]

    # Test with numeric characters
    assert module_0.all_prefixes("123") == ["1", "12", "123"]

    # Test with special characters
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]

    # Test result length matches string length
    assert len(module_0.all_prefixes("python")) == 6

    # Test last prefix equals the full string
    assert module_0.all_prefixes("test")[-1] == "test"

    # Test first prefix is a single character
    assert module_0.all_prefixes("test")[0] == "t"

    print("All tests passed!")


if __name__ == "__main__":
    test_all_prefixes()

# Generated at 2026-11-02 06:46:03.248006
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("xyz") == ["x", "xy", "xyz"]
    assert module_0.all_prefixes("aa") == ["a", "aa"]
    assert module_0.all_prefixes("ab cd") == ["a", "ab", "ab ", "ab c", "ab cd"]
    assert module_0.all_prefixes("!@#") == ["!", "!@", "!@#"]
    assert module_0.all_prefixes("1") == ["1"]

# Generated at 2026-11-02 06:46:50.230263
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes('') == []
    assert module_0.all_prefixes('a') == ['a']
    assert module_0.all_prefixes('ab') == ['a', 'ab']
    assert module_0.all_prefixes('abc') == ['a', 'ab', 'abc']
    assert module_0.all_prefixes('asdf') == ['a', 'as', 'asd', 'asdf']
    assert module_0.all_prefixes('xyz') == ['x', 'xy', 'xyz']
    assert module_0.all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
    assert len(module_0.all_prefixes('python')) == 6
    assert module_0.all_prefixes('aa') == ['a', 'aa']