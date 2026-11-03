

# Generated at 2026-11-01 23:36:16.167013
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaa', 'aaaa') == 1

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaaa', 'aa') == 4
    assert module_0.how_many_times('ababa', 'aba') == 2

    # No occurrences
    assert module_0.how_many_times('abc', 'xyz') == 0
    assert module_0.how_many_times('hello', 'world') == 0
    assert module_0.how_many_times('abc', 'abcd') == 0

    # Single character
    assert module_0.how_many_times('banana', 'a') == 3
    assert module_0.how_many_times('banana', 'n') == 2

    # Multi-character substrings
    assert module_0.how_many_times('hello world hello', 'hello') == 2
    assert module_0.how_many_times('mississippi', 'iss') == 2
    assert module_0.how_many_times('abcabcabc', 'abc') == 3

    # Empty substring matches at every position (len + 1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Case sensitivity
    assert module_0.how_many_times('AbcAbc', 'abc') == 0
    assert module_0.how_many_times('AbcAbc', 'Abc') == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_how_many_times()

# Generated at 2026-11-01 23:36:52.874055
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string, non-empty substring
    assert module_0.how_many_times('', 'a') == 0
    # Single character occurrences
    assert module_0.how_many_times('aaa', 'a') == 3
    # Overlapping substring matches
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('abab', 'ab') == 2
    # Exact full match
    assert module_0.how_many_times('abc', 'abc') == 1
    # Substring longer than string
    assert module_0.how_many_times('abc', 'abcd') == 0
    # No match found
    assert module_0.how_many_times('abc', 'd') == 0
    assert module_0.how_many_times('hello', 'world') == 0
    # Empty substring matches at every position (len + 1)
    assert module_0.how_many_times('', '') == 1
    assert module_0.how_many_times('abc', '') == 4
    # Case sensitivity
    assert module_0.how_many_times('AAA', 'a') == 0
    assert module_0.how_many_times('aAa', 'A') == 1
    # Multiple overlapping complex cases
    assert module_0.how_many_times('ababa', 'aba') == 2
    assert module_0.how_many_times('mississippi', 'issi') == 2

# Generated at 2026-11-01 23:37:16.828163
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases: substring appears once
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('a', 'a') == 1
    assert module_0.how_many_times('abc', 'a') == 1

    # Substring appears multiple times (non-overlapping)
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aaa') == 2
    assert module_0.how_many_times('aaaaa', 'aaa') == 3
    assert module_0.how_many_times('ababab', 'aba') == 2

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0
    assert module_0.how_many_times('', 'abc') == 0

    # Substring equal to string
    assert module_0.how_many_times('hello', 'hello') == 1

    # Substring not present
    assert module_0.how_many_times('hello', 'world') == 0
    assert module_0.how_many_times('hello', 'xyz') == 0

    # Empty substring matches at every position (len(string) + 1 times)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1
    assert module_0.how_many_times('Hello hello', 'Hello') == 1

    # Substring at boundaries
    assert module_0.how_many_times('abcde', 'ab') == 1
    assert module_0.how_many_times('abcde', 'de') == 1
    assert module_0.how_many_times('abcabc', 'abc') == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_how_many_times()

# Generated at 2026-11-01 23:37:59.579673
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string cases
    assert module_0.how_many_times('', 'x') == 0
    assert module_0.how_many_times('', 'abc') == 0

    # No occurrences
    assert module_0.how_many_times('abc', 'x') == 0
    assert module_0.how_many_times('hello', 'world') == 0

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Exact match (substring equals string)
    assert module_0.how_many_times('hello', 'hello') == 1

    # Single occurrence
    assert module_0.how_many_times('hello world', 'hello') == 1
    assert module_0.how_many_times('hello world', 'world') == 1

    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('abcabc', 'abc') == 2
    assert module_0.how_many_times('a b a b', 'a b') == 2

    # Overlapping occurrences
    assert module_0.how_many_times('aaa', 'aa') == 2
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaaa', 'aaa') == 3

    # Single character substring
    assert module_0.how_many_times('banana', 'a') == 3
    assert module_0.how_many_times('banana', 'n') == 2

    # Case sensitivity
    assert module_0.how_many_times('Hello', 'hello') == 0
    assert module_0.how_many_times('Hello Hello', 'Hello') == 2

    # Empty substring edge case (matches at every position)
    assert module_0.how_many_times('', '') == 1
    assert module_0.how_many_times('abc', '') == 4

    # Substring at start/end of string
    assert module_0.how_many_times('abcde', 'ab') == 1
    assert module_0.how_many_times('abcde', 'de') == 1

# Generated at 2026-11-01 23:38:32.349197
# Unit test for function how_many_times
def test_how_many_times():
    # Basic non-overlapping matches
    assert module_0.how_many_times('hello world', 'o') == 2
    assert module_0.how_many_times('hello world', 'world') == 1
    assert module_0.how_many_times('hello world', 'hello') == 1

    # Overlapping matches
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaaaa', 'aaa') == 4

    # No matches
    assert module_0.how_many_times('abc', 'xyz') == 0
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('abc', 'abcd') == 0  # substring longer than string

    # Empty substring edge cases
    assert module_0.how_many_times('', '') == 1
    assert module_0.how_many_times('abc', '') == 4  # len(string) + 1 empty matches

    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1

    # Substring equals string
    assert module_0.how_many_times('abc', 'abc') == 1

    # Repeated pattern
    assert module_0.how_many_times('ababab', 'ab') == 3
    assert module_0.how_many_times('ababab', 'aba') == 2

    print("All tests passed!")


test_how_many_times()