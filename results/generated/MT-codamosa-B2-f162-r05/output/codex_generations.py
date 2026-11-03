

# Generated at 2026-11-03 06:12:16.970549
# Unit test for function string_to_md5
def test_string_to_md5():
    # Known MD5 hash values
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == "9e107d9d372bb6826bd81d3542a419d6"

    # Empty string returns None
    assert module_0.string_to_md5("") is None

    # Result is a 32-character lowercase hex string
    result = module_0.string_to_md5("Test Input!")
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Matches hashlib reference implementation
    assert module_0.string_to_md5("Test Input!") == hashlib.md5(b"Test Input!").hexdigest()

    # Special characters (ASCII-safe)
    assert module_0.string_to_md5(" !@#$%^&*()") == hashlib.md5(" !@#$%^&*()".encode("ascii")).hexdigest()

    # Consistency: same input yields same hash
    assert module_0.string_to_md5("repeat") == module_0.string_to_md5("repeat")

    # Whitespace matters
    assert module_0.string_to_md5("a b") != module_0.string_to_md5("ab")

    # Case sensitivity
    assert module_0.string_to_md5("Hello") != module_0.string_to_md5("hello")

# Generated at 2026-11-03 06:13:42.063742
# Unit test for function string_to_md5
def test_string_to_md5():import unittest


class TestStringToMd5(unittest.TestCase):

    def test_string_to_md5(self):
        # Test normal string
        self.assertEqual(module_0.string_to_md5('hello'), '5d41402abc4b2a76b9719d911017c592')

        # Test another known value
        self.assertEqual(module_0.string_to_md5('test'), '098f6bcd4621d373cade4e832627b4f6')

        # Test string with spaces
        self.assertEqual(module_0.string_to_md5('Hello World'), 'b10a8db164e0754105b7a99be72e3fe5')

        # Test short string
        self.assertEqual(module_0.string_to_md5('abc'), '900150983cd24fb0d6963f7d28e17f72')

        # Test empty string returns None
        self.assertIsNone(module_0.string_to_md5(''))

        # Test None input returns None
        self.assertIsNone(module_0.string_to_md5(None))

        # Test result is a 32-character hex string
        result = module_0.string_to_md5('python')
        self.assertEqual(len(result), 32)
        self.assertRegex(result, r'^[0-9a-f]{32}$')

        # Test same input produces same output (deterministic)
        self.assertEqual(module_0.string_to_md5('hello'), module_0.string_to_md5('hello'))

        # Test different inputs produce different outputs
        self.assertNotEqual(module_0.string_to_md5('hello'), module_0.string_to_md5('world'))


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-03 06:14:49.547454
# Unit test for function string_to_md5
def test_string_to_md5():
    # Known MD5 test vector (RFC 1321)
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'

    # Another well-known MD5 hash
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

    # Empty string returns None
    assert module_0.string_to_md5('') is None

    # None input returns None
    assert module_0.string_to_md5(None) is None

    # Result is a 32-character lowercase hex digest
    result = module_0.string_to_md5('Hello world')
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Deterministic behavior
    assert module_0.string_to_md5('Hello world') == module_0.string_to_md5('Hello world')

    # Different inputs produce different hashes (case sensitivity)
    assert module_0.string_to_md5('Hello') != module_0.string_to_md5('hello')

    print('All tests passed!')

if __name__ == '__main__':
    test_string_to_md5()

# Generated at 2026-11-03 06:15:55.183256
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with a simple string
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

    # Test with the classic pangram
    assert module_0.string_to_md5('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'

    # Test with an empty string (should return None)
    assert module_0.string_to_md5('') is None

    # Test with None (should return None)
    assert module_0.string_to_md5(None) is None

    # Test with a string containing spaces and punctuation
    assert module_0.string_to_md5('Hello, World!') == module_0.string_to_md5('Hello, World!')

    # Test that non-ASCII input raises an error
    try:
        module_0.string_to_md5('héllo')
        assert False, "Expected UnicodeEncodeError for non-ASCII input"
    except UnicodeEncodeError:
        pass

    # Test result is a valid 32-character lowercase hex digest
    result = module_0.string_to_md5('test')
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    print("All tests passed!")

test_string_to_md5()

# Generated at 2026-11-03 06:17:53.869203
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Test with a non-empty string: verify against hashlib directly
    text = "hello"
    expected = hashlib.md5(text.encode('ascii')).hexdigest()
    assert module_0.string_to_md5(text) == expected
    assert module_0.string_to_md5(text) == '5d41402abc4b2a76b9719d911017c592'

    # Test with another known string
    assert module_0.string_to_md5("Hello World") == 'b10a8db164e0754105b7a99be72e3fe5'

    # Test with empty string -> should return None
    assert module_0.string_to_md5('') is None

    # Test with None -> should return None
    assert module_0.string_to_md5(None) is None

    # Test that result is a 32-character lowercase hex string
    result = module_0.string_to_md5("abc123")
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Test deterministic behavior: same input yields same output
    assert module_0.string_to_md5("test") == module_0.string_to_md5("test")

    # Test different inputs yield different outputs
    assert module_0.string_to_md5("test") != module_0.string_to_md5("Test")

    # Test with digits and special characters
    assert module_0.string_to_md5("12345") == '827ccb0eea8a706c4c34a16891f84e7b'
    assert module_0.string_to_md5("!@#$%") == 'a4dd0ef2c148a1e2dbdb9efea11c4a41'