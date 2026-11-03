

# Generated at 2026-11-01 22:04:13.314340
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with a normal string
    assert module_0.string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'
    
    # Test with another known string
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
    
    # Test with a simple word
    assert module_0.string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    
    # Test empty string returns None
    assert module_0.string_to_md5('') is None
    
    # Test None returns None
    assert module_0.string_to_md5(None) is None
    
    # Test with numbers as string
    assert module_0.string_to_md5('12345') == '827ccb0eea8a706c4c34a16891f84e7b'
    
    # Test with special characters
    assert module_0.string_to_md5('!@#$%') is not None
    
    # Test result is a 32-character hex string
    result = module_0.string_to_md5('hello')
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

test_string_to_md5()

# Generated at 2026-11-01 22:04:50.281621
# Unit test for function string_to_md5
def test_string_to_md5():import unittest


class TestStringToMd5(unittest.TestCase):

    def test_empty_string_returns_none(self):
        self.assertIsNone(module_0.string_to_md5(""))

    def test_known_hash_abc(self):
        self.assertEqual(module_0.string_to_md5("abc"), "900150983cd24fb0d6963f7d28e17f72")

    def test_known_hash_hello(self):
        self.assertEqual(module_0.string_to_md5("hello"), "5d41402abc4b2a76b9719d911017c592")

    def test_known_hash_hello_world(self):
        self.assertEqual(
            module_0.string_to_md5("hello world"),
            "5eb63bbbe01eeed093cb22bb8f5acdc3",
        )

    def test_case_sensitivity(self):
        # Same letters, different case -> different hashes
        self.assertNotEqual(module_0.string_to_md5("Hello"), module_0.string_to_md5("hello"))

    def test_result_is_32_char_hex(self):
        result = module_0.string_to_md5("some random text")
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 32)
        int(result, 16)  # raises ValueError if not valid hex

    def test_deterministic_output(self):
        self.assertEqual(module_0.string_to_md5("repeat"), module_0.string_to_md5("repeat"))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 22:05:28.953034
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Non-empty strings return the correct MD5 hex digest
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert module_0.string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert module_0.string_to_md5(' ') == '7215ee9c7d9dc229d2921a40e17d9f35'

    # Empty string returns None
    assert module_0.string_to_md5('') is None

    # None input (falsy) returns None
    assert module_0.string_to_md5(None) is None

    # Result matches hashlib directly and is a 32-char lowercase hex string
    result = module_0.string_to_md5('Python 3.8')
    assert result == hashlib.md5(b'Python 3.8').hexdigest()
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

# Generated at 2026-11-01 22:06:15.475847
# Unit test for function string_to_md5
def test_string_to_md5():
    # Known MD5 hashes for common inputs
    assert module_0.string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"
    assert module_0.string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

    # Empty / falsy input returns None
    assert module_0.string_to_md5("") is None

    # Strings with spaces and special (ASCII) characters
    assert module_0.string_to_md5(" ") == "7215ee9c7d9dc229d2921a40e1789964"
    assert module_0.string_to_md5("!@#$%^&*()") == "b63050d31ca4aeffdb40e03be05ea92d"

    # Result properties: 32-char lowercase hex string
    result = module_0.string_to_md5("Python")
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Matches hashlib reference implementation
    assert module_0.string_to_md5("unittest") == hashlib.md5(b"unittest").hexdigest()

    # Deterministic behavior
    assert module_0.string_to_md5("repeat") == module_0.string_to_md5("repeat")

    print("All tests passed!")


if __name__ == "__main__":
    test_string_to_md5()

# Generated at 2026-11-01 22:06:42.919345
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Test normal string
    assert module_0.string_to_md5("hello") == hashlib.md5(b"hello").hexdigest()
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    # Test another known value
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"

    # Test string with spaces and punctuation
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == "9e107d9d372bb6826bd81d3542a419d6"

    # Test empty string returns None
    assert module_0.string_to_md5("") is None

    # Test None input returns None
    assert module_0.string_to_md5(None) is None

    # Test result is a 32-character lowercase hex string
    result = module_0.string_to_md5("test input")
    assert isinstance(result, str)
    assert len(result) == 32
    assert result == result.lower()
    assert all(c in "0123456789abcdef" for c in result)

    # Test consistency: same input yields same output
    assert module_0.string_to_md5("repeat") == module_0.string_to_md5("repeat")

    # Test different inputs yield different outputs
    assert module_0.string_to_md5("input1") != module_0.string_to_md5("input2")

    # Test whitespace-only string is truthy and hashed (not None)
    assert module_0.string_to_md5(" ") == hashlib.md5(b" ").hexdigest()

    print("All tests passed!")


if __name__ == "__main__":
    test_string_to_md5()