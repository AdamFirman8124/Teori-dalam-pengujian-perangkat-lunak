

# Generated at 2026-11-01 22:46:16.061054
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string, non-empty substring
    assert module_0.how_many_times('', 'x') == 0
    # Single character occurrences
    assert module_0.how_many_times('xyxyxyx', 'x') == 4
    # Overlapping occurrences
    assert module_0.how_many_times('cacac', 'cac') == 2
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaa', 'aaaa') == 1
    # Exact single occurrence
    assert module_0.how_many_times('abcdefg', 'abc') == 1
    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('abcabcx', 'abc') == 2
    # Substring not present
    assert module_0.how_many_times('hello', 'xyz') == 0
    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0
    # Substring equals string
    assert module_0.how_many_times('abc', 'abc') == 1
    # Empty substring counts at every position (len+1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1
    # Case sensitivity
    assert module_0.how_many_times('AaAa', 'aa') == 1
    # Repeated single char
    assert module_0.how_many_times('aaa', 'a') == 3

# Generated at 2026-11-01 22:46:25.889519
# Unit test for function how_many_times
def test_how_many_times():
    # Exact match
    assert module_0.how_many_times('hello', 'hello') == 1
    # Empty string
    assert module_0.how_many_times('', 'a') == 0
    # Empty substring matches at every position
    assert module_0.how_many_times('abc', '') == 4
    # Both empty
    assert module_0.how_many_times('', '') == 1
    # No occurrence
    assert module_0.how_many_times('abc', 'x') == 0
    # Single character occurrences
    assert module_0.how_many_times('aaa', 'a') == 3
    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaa', 'aaa') == 2
    assert module_0.how_many_times('aaaa', 'aaaa') == 1
    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0
    # Multiple separated occurrences
    assert module_0.how_many_times('abcabcabc', 'abc') == 3
    assert module_0.how_many_times('abcabcabc', 'abcabc') == 2
    # Case sensitivity
    assert module_0.how_many_times('AbcAbc', 'abc') == 0
    # Overlapping with mixed characters
    assert module_0.how_many_times('abababab', 'abab') == 3

# Generated at 2026-11-01 22:46:40.020403
# Unit test for function how_many_times
def test_how_many_times():
    # Single occurrence
    assert module_0.how_many_times('hello', 'ell') == 1

    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('abcabc', 'abc') == 2

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('mississippi', 'issi') == 2

    # Substring not present
    assert module_0.how_many_times('abc', 'xyz') == 0

    # Substring equals the whole string
    assert module_0.how_many_times('abc', 'abc') == 1

    # Substring longer than the string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Empty string with non-empty substring
    assert module_0.how_many_times('', 'a') == 0

    # Empty substring matches at every position
    assert module_0.how_many_times('ab', '') == 3
    assert module_0.how_many_times('', '') == 1

    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1

    print("All tests passed!")

# Generated at 2026-11-01 22:46:50.669891
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string, non-empty substring
    assert module_0.how_many_times('', 'x') == 0
    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0
    # Exact match
    assert module_0.how_many_times('hello', 'hello') == 1
    # Substring not present
    assert module_0.how_many_times('hello', 'world') == 0
    # Single occurrence in middle
    assert module_0.how_many_times('hello', 'ell') == 1
    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('ababab', 'ab') == 3
    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaa', 'aa') == 2
    # Single character repeated
    assert module_0.how_many_times('banana', 'a') == 3
    assert module_0.how_many_times('banana', 'an') == 2
    # Empty substring matches at every position (len + 1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1
    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1
    # Overlapping pattern with mixed characters
    assert module_0.how_many_times('ababa', 'aba') == 2


class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(module_0.how_many_times('', 'x'), 0)

    def test_substring_longer_than_string(self):
        self.assertEqual(module_0.how_many_times('ab', 'abc'), 0)

    def test_exact_match(self):
        self.assertEqual(module_0.how_many_times('hello', 'hello'), 1)

    def test_no_occurrence(self):
        self.assertEqual(module_0.how_many_times('hello', 'world'), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(module_0.how_many_times('ababab', 'ab'), 3)

    def test_overlapping_occurrences(self):
        self.assertEqual(module_0.how_many_times('aaaa', 'aa'), 3)
        self.assertEqual(module_0.how_many_times('aaa', 'aa'), 2)

    def test_single_char(self):
        self.assertEqual(module_0.how_many_times('banana', 'a'), 3)

    def test_empty_substring(self):
        self.assertEqual(module_0.how_many_times('abc', ''), 4)
        self.assertEqual(module_0.how_many_times('', ''), 1)


if __name__ == '__main__':
    test_how_many_times()
    print("All tests passed!")
    unittest.main()

# Generated at 2026-11-01 22:47:16.065354
# Unit test for function how_many_times
def test_how_many_times():
    # nonce:80fd6066
    # Basic single occurrence
    assert module_0.how_many_times('hello', 'l') == 2
    assert module_0.how_many_times('hello', 'll') == 1
    assert module_0.how_many_times('hello', 'hello') == 1

    # No occurrences
    assert module_0.how_many_times('hello', 'xyz') == 0
    assert module_0.how_many_times('', 'a') == 0

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaaa', 'aaa') == 3
    assert module_0.how_many_times('ababa', 'aba') == 2

    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('abcabcabc', 'abc') == 3

    # Case sensitivity
    assert module_0.how_many_times('Hello', 'hello') == 0
    assert module_0.how_many_times('Hello', 'Hello') == 1

    # Empty substring edge case (matches at every position including end)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Single character string
    assert module_0.how_many_times('a', 'a') == 1
    assert module_0.how_many_times('a', 'b') == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_how_many_times()