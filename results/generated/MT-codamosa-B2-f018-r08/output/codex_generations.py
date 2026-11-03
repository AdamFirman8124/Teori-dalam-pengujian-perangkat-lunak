

# Generated at 2026-11-02 22:32:06.620654
# Unit test for function how_many_times
def test_how_many_times():
    # nonce:a2cf836d
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('abc', 'x') == 0
    assert module_0.how_many_times('abcabc', 'abc') == 2

    # Overlapping matches
    assert module_0.how_many_times('aaaa', 'aaa') == 2
    assert module_0.how_many_times('abab', 'ab') == 2
    assert module_0.how_many_times('mississippi', 'issi') == 2

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Empty substring matches at every position
    assert module_0.how_many_times('', '') == 1
    assert module_0.how_many_times('abc', '') == 4

    # Case sensitivity
    assert module_0.how_many_times('AbcA', 'a') == 1

# Generated at 2026-11-02 22:33:51.717238
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('abc', 'abc') == 1
    assert module_0.how_many_times('abc', 'xyz') == 0

    # Edge cases
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1
    assert module_0.how_many_times('hello', 'll') == 1

    # Overlapping occurrences
    assert module_0.how_many_times('ababab', 'ab') == 3
    assert module_0.how_many_times('ababab', 'aba') == 2

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Longer sentence
    assert module_0.how_many_times('long substring that does not contain the target', 'target') == 1

# Generated at 2026-11-02 22:35:00.975039
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3  # positions 0, 1, 2
    assert module_0.how_many_times('ababa', 'aba') == 2  # positions 0, 2
    assert module_0.how_many_times('xxx', 'xx') == 2  # positions 0, 1

    # Substring longer than string
    assert module_0.how_many_times('abc', 'abcd') == 0
    assert module_0.how_many_times('a', 'aa') == 0

    # Substring equal to string
    assert module_0.how_many_times('hello', 'hello') == 1

    # No match
    assert module_0.how_many_times('hello', 'world') == 0
    assert module_0.how_many_times('abc', 'z') == 0

    # Empty substring matches at every position (len + 1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1
    assert module_0.how_many_times('Hello hello', 'Hello') == 1

    # Multiple words
    assert module_0.how_many_times('one two one two one', 'one') == 3
    assert module_0.how_many_times('banana', 'ana') == 2  # overlapping

    # Single character string
    assert module_0.how_many_times('x', 'x') == 1
    assert module_0.how_many_times('x', 'y') == 0

    print("All tests passed!")


# nonce:1b467ad3

# Generated at 2026-11-02 22:36:28.414691
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3  # overlapping occurrences
    assert module_0.how_many_times('abc', 'abc') == 1
    assert module_0.how_many_times('abcde', 'abcde') == 1

    # Substring not present
    assert module_0.how_many_times('abc', 'xyz') == 0
    assert module_0.how_many_times('abc', 'abcd') == 0

    # Repeated patterns
    assert module_0.how_many_times('ababab', 'ab') == 3
    assert module_0.how_many_times('abcabc', 'abc') == 2
    assert module_0.how_many_times('mississippi', 'issi') == 2  # overlapping

    # Single character string
    assert module_0.how_many_times('a', 'a') == 1
    assert module_0.how_many_times('a', 'b') == 0

# Generated at 2026-11-02 22:38:02.219267
# Unit test for function how_many_times
def test_how_many_times():
    # Basic non-overlapping matches
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('hello', 'a') == 0
    assert module_0.how_many_times('hello', 'e') == 1
    assert module_0.how_many_times('hello', 'l') == 2

    # Substring equal to string
    assert module_0.how_many_times('hello', 'hello') == 1

    # No match
    assert module_0.how_many_times('hello', 'xyz') == 0

    # Case sensitivity
    assert module_0.how_many_times('Hello', 'hello') == 0

    # Overlapping matches
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaa', 'aaa') == 2
    assert module_0.how_many_times('xAAAAx', 'AA') == 2

    # Repeated pattern
    assert module_0.how_many_times('abcabc', 'abc') == 2
    assert module_0.how_many_times('abcabcabc', 'abc') == 3

    # Overlapping pattern
    assert module_0.how_many_times('ababa', 'aba') == 2

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Empty substring matches at every position (len + 1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1