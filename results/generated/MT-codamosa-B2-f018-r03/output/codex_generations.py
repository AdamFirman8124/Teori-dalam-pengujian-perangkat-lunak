

# Generated at 2026-11-02 18:40:42.555976
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('a', 'a') == 1
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3  # overlapping counts

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Substring equals string
    assert module_0.how_many_times('hello', 'hello') == 1

    # Multiple separated occurrences
    assert module_0.how_many_times('abcabcabc', 'abc') == 3
    assert module_0.how_many_times('abcabcabc', 'abcabc') == 2  # overlapping

    # No occurrence
    assert module_0.how_many_times('hello world', 'xyz') == 0

    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1

    # Empty substring matches at every position (len+1 positions)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Single character string and substring
    assert module_0.how_many_times('x', 'x') == 1
    assert module_0.how_many_times('x', 'y') == 0

# Generated at 2026-11-02 18:42:28.018258
# Unit test for function how_many_times
def test_how_many_times():
    # Basic non-overlapping matches
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3   # overlapping occurrences counted
    assert module_0.how_many_times('hello', 'll') == 1
    assert module_0.how_many_times('hello world', 'o') == 2
    assert module_0.how_many_times('abc', 'xyz') == 0   # no match
    assert module_0.how_many_times('abc', 'abc') == 1   # exact match of whole string
    assert module_0.how_many_times('ababc', 'ab') == 2
    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0
    # Empty substring matches at every position (len(string) + 1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1
    # Case sensitivity
    assert module_0.how_many_times('AaAa', 'aa') == 1
    assert module_0.how_many_times('AaAa', 'Aa') == 2
    # Overlapping single character repeats
    assert module_0.how_many_times('xabxxabx', 'ab') == 2
    assert module_0.how_many_times('aaaaaa', 'aaa') == 4
    # Special characters and spaces
    assert module_0.how_many_times('a b a b', 'a b') == 2
    assert module_0.how_many_times('!!!', '!!') == 2

# Generated at 2026-11-02 18:44:11.541598
# Unit test for function how_many_times
def test_how_many_times():
    # Basic substring counting
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('hello', 'll') == 1
    assert module_0.how_many_times('hello', 'x') == 0
    assert module_0.how_many_times('abc', 'abc') == 1

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaaa', 'aaa') == 3
    assert module_0.how_many_times('ababab', 'abab') == 2

    # Substring at edges
    assert module_0.how_many_times('abcde', 'ab') == 1
    assert module_0.how_many_times('abcde', 'de') == 1
    assert module_0.how_many_times('abcde', 'cd') == 1

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Empty substring matches at every position
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Case sensitivity
    assert module_0.how_many_times('aAaA', 'aA') == 2

    # Repeated characters
    assert module_0.how_many_times('x', 'x') == 1
    assert module_0.how_many_times('xx', 'xx') == 1

    print("test_how_many_times passed")


test_how_many_times()

# Generated at 2026-11-02 18:45:11.296436
# Unit test for function how_many_times
def test_how_many_times():
    # nonce:aaf621ba
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaa', 'aaaa') == 1
    assert module_0.how_many_times('abc', 'x') == 0
    assert module_0.how_many_times('abc', 'abc') == 1
    assert module_0.how_many_times('abcabc', 'abc') == 2

    # Overlapping matches
    assert module_0.how_many_times('aaaa', 'aaa') == 2
    assert module_0.how_many_times('ababab', 'abab') == 2

    # Case sensitivity
    assert module_0.how_many_times('Abc', 'abc') == 0
    assert module_0.how_many_times('ABC', 'ABC') == 1

    # Empty substring counts at every position (including end)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Special characters and spaces
    assert module_0.how_many_times('a b a b', 'a b') == 2
    assert module_0.how_many_times('!!??!!', '!!') == 3

    print("All tests passed!")


if __name__ == "__main__":
    test_how_many_times()

# Generated at 2026-11-02 18:46:48.487942
# Unit test for function how_many_times
def test_how_many_times():
    # Basic non-overlapping occurrences
    assert module_0.how_many_times('abcabc', 'abc') == 2
    assert module_0.how_many_times('hello world hello', 'hello') == 2

    # Single character repeated
    assert module_0.how_many_times('aaa', 'a') == 3

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('ababa', 'aba') == 2

    # Substring not present
    assert module_0.how_many_times('hello', 'xyz') == 0
    assert module_0.how_many_times('', 'a') == 0

    # Substring equal to the string
    assert module_0.how_many_times('abc', 'abc') == 1

    # Substring longer than the string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Empty substring counts at every position (len(string) + 1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1

    # Substring at start, middle, and end
    assert module_0.how_many_times('xayxbyx', 'x') == 3
    assert module_0.how_many_times('axxa', 'xx') == 1