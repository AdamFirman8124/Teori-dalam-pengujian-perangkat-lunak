

# Generated at 2026-11-03 04:13:37.127654
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('', 'abc') == 0

    # Single character substring
    assert module_0.how_many_times('abc', 'a') == 1
    assert module_0.how_many_times('aaa', 'a') == 3

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaaa', 'aa') == 4
    assert module_0.how_many_times('ababab', 'abab') == 2

    # Substring equals string
    assert module_0.how_many_times('abc', 'abc') == 1

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Substring not present
    assert module_0.how_many_times('hello world', 'xyz') == 0

    # Multiple separated occurrences
    assert module_0.how_many_times('xabcxabcx', 'abc') == 2

    # Empty substring edge case
    assert module_0.how_many_times('abc', '') == 4

    # Case sensitivity
    assert module_0.how_many_times('AbcABC', 'abc') == 1

    print("All tests passed!")


test_how_many_times()

# Generated at 2026-11-03 04:16:41.107238
# Unit test for function how_many_times
def test_how_many_times():
    # Basic single occurrence
    assert module_0.how_many_times('hello', 'll') == 1
    assert module_0.how_many_times('abc', 'b') == 1

    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('abcabc', 'abc') == 2
    assert module_0.how_many_times('ababab', 'ab') == 3

    # Overlapping occurrences
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaa', 'aaa') == 2

    # Substring equals the whole string
    assert module_0.how_many_times('abc', 'abc') == 1

    # No occurrences
    assert module_0.how_many_times('abc', 'xyz') == 0

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Empty string
    assert module_0.how_many_times('', 'a') == 0

    # Empty substring edge cases
    # Every position (len(string) + 1) matches an empty substring
    assert module_0.how_many_times('', '') == 1
    assert module_0.how_many_times('abc', '') == 4

    # Case sensitivity
    assert module_0.how_many_times('AbcABC', 'abc') == 0

    print("All tests passed!")


test_how_many_times()

# Generated at 2026-11-03 04:18:40.801964
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('hello', 'll') == 1
    assert module_0.how_many_times('hello', 'world') == 0

    # Substring equals string
    assert module_0.how_many_times('abc', 'abc') == 1

    # Overlapping matches (key behavior of this function)
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaaa', 'aaa') == 3
    assert module_0.how_many_times('xyxyxyx', 'xyx') == 3

    # Multiple non-overlapping matches
    assert module_0.how_many_times('ababc', 'ab') == 2

    # Substring longer than string
    assert module_0.how_many_times('abc', 'abcd') == 0

    # Empty substring edge cases
    assert module_0.how_many_times('', '') == 1
    assert module_0.how_many_times('abc', '') == 4  # matches at len(string) + 1 positions

# Generated at 2026-11-03 04:20:01.813457
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('ababab', 'abab') == 2
    assert module_0.how_many_times('aaa', 'aa') == 2

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # No match
    assert module_0.how_many_times('hello', 'world') == 0

    # Empty substring matches at every position
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Case sensitivity
    assert module_0.how_many_times('Hello', 'hello') == 0
    assert module_0.how_many_times('Hello', 'Hello') == 1

    # Whole string match
    assert module_0.how_many_times('abc', 'abc') == 1

    # Multiple disjoint matches
    assert module_0.how_many_times('abcabcabc', 'abc') == 3

    # Single character string
    assert module_0.how_many_times('a', 'a') == 1
    assert module_0.how_many_times('a', 'b') == 0

    print("All tests passed!")


test_how_many_times()

# Generated at 2026-11-03 04:22:18.345313
# Unit test for function how_many_times
def test_how_many_times():
    assert module_0.how_many_times('', 'x') == 0
    assert module_0.how_many_times('xyxyxyx', 'x') == 4
    assert module_0.how_many_times('cacacac', 'cac') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3  # overlapping matches
    assert module_0.how_many_times('hello', 'world') == 0
    assert module_0.how_many_times('abc', 'abc') == 1
    assert module_0.how_many_times('ab', 'abc') == 0  # substring longer than string
    assert module_0.how_many_times('abc', '') == 4    # empty substring: len+1 matches