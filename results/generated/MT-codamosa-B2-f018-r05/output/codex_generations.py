

# Generated at 2026-11-03 01:28:43.060685
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aaa') == 2
    assert module_0.how_many_times('abcabc', 'abc') == 2
    assert module_0.how_many_times('ababab', 'abab') == 2

    # Substring not present
    assert module_0.how_many_times('hello', 'world') == 0
    assert module_0.how_many_times('abc', 'xyz') == 0

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Exact match (whole string)
    assert module_0.how_many_times('hello', 'hello') == 1

    # Case sensitivity
    assert module_0.how_many_times('Hello', 'hello') == 0
    assert module_0.how_many_times('HeLLo', 'LL') == 1

    # Empty substring counts len(string) + 1 times
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Multiple occurrences with mixed overlaps
    assert module_0.how_many_times('aaaaaa', 'aaa') == 4
    assert module_0.how_many_times('mississippi', 'issi') == 2

    print("All tests passed!")


test_how_many_times()

# Generated at 2026-11-03 01:30:27.491290
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('hello', 'l') == 2
    assert module_0.how_many_times('hello', 'll') == 1
    assert module_0.how_many_times('hello', 'z') == 0

    # Overlapping matches
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaaaa', 'aaa') == 4

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Substring equal to string
    assert module_0.how_many_times('abc', 'abc') == 1

    # Empty substring: every position (len + 1) matches
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Empty string with non-empty substring
    assert module_0.how_many_times('', 'a') == 0

    # Multi-character patterns with overlaps
    assert module_0.how_many_times('abababab', 'abab') == 3
    assert module_0.how_many_times('mississippi', 'issi') == 2

    # Case sensitivity
    assert module_0.how_many_times('AbcAbc', 'abc') == 0

    print("All tests passed!")

# Generated at 2026-11-03 01:32:17.155752
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string with a non-empty substring
    assert module_0.how_many_times('', 'a') == 0

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaa', 'aa') == 2
    assert module_0.how_many_times('xyxyxyx', 'xyx') == 3

    # Substring equals the whole string
    assert module_0.how_many_times('abc', 'abc') == 1
    assert module_0.how_many_times('aaaa', 'aaaa') == 1

    # No occurrences
    assert module_0.how_many_times('abc', 'x') == 0
    assert module_0.how_many_times('abc', 'abcd') == 0  # substring longer than string

    # Single character substring
    assert module_0.how_many_times('hello', 'l') == 2
    assert module_0.how_many_times('hello', 'h') == 1

    # Multi-word / realistic case
    assert module_0.how_many_times('mississippi', 'issi') == 2

    # Empty substring matches at every position (len + 1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

# Generated at 2026-11-03 01:33:30.555628
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('', '') == 1

    # Single character substring
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('abc', 'a') == 1
    assert module_0.how_many_times('abc', 'd') == 0

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaaa', 'aa') == 4
    assert module_0.how_many_times('ababab', 'aba') == 2

    # Substring equal to string
    assert module_0.how_many_times('hello', 'hello') == 1

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('abcabcabc', 'abc') == 3

    # Occurrence at start, middle, and end
    assert module_0.how_many_times('xayxbyx', 'x') == 3

    # Case sensitivity
    assert module_0.how_many_times('AaAa', 'aa') == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_how_many_times()

# Generated at 2026-11-03 01:34:53.560006
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('', 'abc') == 0

    # Single character substring
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('abc', 'b') == 1
    assert module_0.how_many_times('abc', 'x') == 0

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('ababab', 'abab') == 2

    # Exact match / whole string
    assert module_0.how_many_times('hello', 'hello') == 1

    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('abcabc', 'abc') == 2
    assert module_0.how_many_times('mississippi', 'iss') == 2

    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Substring equal to string length
    assert module_0.how_many_times('abc', 'abc') == 1

    print("All tests passed!")


test_how_many_times()