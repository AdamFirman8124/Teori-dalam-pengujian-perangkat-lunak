

# Generated at 2026-11-03 00:02:36.900717
# Unit test for function how_many_times
def test_how_many_times():
    # Basic cases
    assert module_0.how_many_times('', 'a') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3

    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aaa') == 2
    assert module_0.how_many_times('ababab', 'abab') == 2

    # Substring appears once
    assert module_0.how_many_times('hello', 'hello') == 1
    assert module_0.how_many_times('hello world', 'world') == 1

    # Substring not present
    assert module_0.how_many_times('hello', 'xyz') == 0
    assert module_0.how_many_times('abc', 'abcd') == 0

    # Empty substring matches at every position (len + 1)
    assert module_0.how_many_times('abc', '') == 4
    assert module_0.how_many_times('', '') == 1

    # Case sensitivity
    assert module_0.how_many_times('Hello', 'hello') == 0

    # Substring at boundaries
    assert module_0.how_many_times('xabcx', 'x') == 2
    assert module_0.how_many_times('abcabc', 'abc') == 2

    print("All tests passed!")


test_how_many_times()

# Generated at 2026-11-03 00:03:22.160567
# Unit test for function how_many_times
def test_how_many_times():
    # Empty string
    assert module_0.how_many_times('', 'a') == 0
    # Single character occurrences
    assert module_0.how_many_times('aaa', 'a') == 3
    # Overlapping occurrences
    assert module_0.how_many_times('aaaa', 'aa') == 3
    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('ababab', 'ab') == 3
    # Substring not present
    assert module_0.how_many_times('hello', 'xyz') == 0
    # Substring equals whole string
    assert module_0.how_many_times('abc', 'abc') == 1
    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0
    # Occurrence in middle of string
    assert module_0.how_many_times('xyabcz', 'abc') == 1
    # Multiple scattered occurrences
    assert module_0.how_many_times('a man, a plan', 'a ') == 2

# Generated at 2026-11-03 00:03:55.953025
# Unit test for function how_many_times
def test_how_many_times():
    # nonce:9c27f589
    # Empty string
    assert module_0.how_many_times('', 'x') == 0

    # Single character occurring multiple times
    assert module_0.how_many_times('xyxyxyx', 'x') == 4

    # Overlapping occurrences are counted
    assert module_0.how_many_times('cacac', 'cac') == 2
    assert module_0.how_many_times('aaaaaa', 'aa') == 5
    assert module_0.how_many_times('aaaa', 'aa') == 3

    # No match found
    assert module_0.how_many_times('abcdef', 'xyz') == 0

    # Substring equals the whole string
    assert module_0.how_many_times('hello', 'hello') == 1

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Single occurrence in middle of string
    assert module_0.how_many_times('hello world', 'o w') == 1

    # Whole string of repeated single character
    assert module_0.how_many_times('aaaa', 'aaaa') == 1

# Generated at 2026-11-03 00:04:31.692600
# Unit test for function how_many_times
def test_how_many_times():import unittest


class TestHowManyTimes(unittest.TestCase):
    def test_empty_string_empty_substring(self):
        self.assertEqual(module_0.how_many_times('', 'a'), 0)

    def test_empty_substring(self):
        self.assertEqual(module_0.how_many_times('abc', ''), 4)

    def test_single_character_match(self):
        self.assertEqual(module_0.how_many_times('aaa', 'a'), 3)

    def test_overlapping_matches(self):
        self.assertEqual(module_0.how_many_times('aaaa', 'aa'), 3)

    def test_multiple_overlapping(self):
        self.assertEqual(module_0.how_many_times('aaaa', 'aaa'), 2)

    def test_no_match(self):
        self.assertEqual(module_0.how_many_times('hello', 'xyz'), 0)

    def test_substring_longer_than_string(self):
        self.assertEqual(module_0.how_many_times('ab', 'abc'), 0)

    def test_exact_match(self):
        self.assertEqual(module_0.how_many_times('abc', 'abc'), 1)

    def test_multiple_non_overlapping(self):
        self.assertEqual(module_0.how_many_times('abcabcabc', 'abc'), 3)

    def test_mixed_overlapping(self):
        self.assertEqual(module_0.how_many_times('ababa', 'aba'), 2)

    def test_single_char_string(self):
        self.assertEqual(module_0.how_many_times('x', 'x'), 1)

    def test_special_characters(self):
        self.assertEqual(module_0.how_many_times('a.b.a.b', 'a.b'), 2)


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-03 00:06:14.192674
# Unit test for function how_many_times
def test_how_many_times():
    # Basic single occurrence
    assert module_0.how_many_times('', 'x') == 0
    assert module_0.how_many_times('hello', 'x') == 0
    assert module_0.how_many_times('hello', 'hello') == 1
    assert module_0.how_many_times('hello', 'ell') == 1

    # Multiple non-overlapping occurrences
    assert module_0.how_many_times('abcabcabc', 'abc') == 3
    assert module_0.how_many_times('aaaa', 'a') == 4

    # Overlapping occurrences
    assert module_0.how_many_times('aaa', 'aa') == 2
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('aaaaa', 'aaa') == 3
    assert module_0.how_many_times('ababab', 'abab') == 2

    # Single character string
    assert module_0.how_many_times('a', 'a') == 1
    assert module_0.how_many_times('a', 'b') == 0

    # Substring longer than string
    assert module_0.how_many_times('ab', 'abc') == 0

    # Empty substring counts at every position (len(string) + 1)
    assert module_0.how_many_times('', '') == 1
    assert module_0.how_many_times('abc', '') == 4

    # Case sensitivity
    assert module_0.how_many_times('Hello hello', 'hello') == 1
    assert module_0.how_many_times('Hello hello', 'Hello') == 1

    # Substring at start, middle, and end
    assert module_0.how_many_times('xayx', 'x') == 2
    assert module_0.how_many_times('abcde', 'cde') == 1