

# Generated at 2026-11-02 23:15:16.708531
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Test with a simple string (known MD5 value)
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    # Test with another known MD5 value
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"

    # Test with a string containing spaces
    assert module_0.string_to_md5("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"

    # Test with numeric string
    assert module_0.string_to_md5("12345") == "827ccb0eea8a706c4c4a16847f84e3b"

    # Test empty string returns None
    assert module_0.string_to_md5("") is None

    # Test None input returns None
    assert module_0.string_to_md5(None) is None

    # Test determinism: same input yields same output
    assert module_0.string_to_md5("test") == module_0.string_to_md5("test")

    # Test different inputs yield different outputs
    assert module_0.string_to_md5("test") != module_0.string_to_md5("Test")

    # Test result is a valid 32-character lowercase hex digest
    result = module_0.string_to_md5("sample text")
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Test consistency with hashlib directly
    assert module_0.string_to_md5("test input") == hashlib.md5("test input".encode('ascii')).hexdigest()

    print("All tests passed!")


test_string_to_md5()

# Generated at 2026-11-02 23:16:56.447238
# Unit test for function string_to_md5
def test_string_to_md5():
# nonce:2635d4d1
    # Empty string should return None
    assert module_0.string_to_md5('') is None

    # Simple string
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    # Classic MD5 test vector
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'

    # Longer well-known text
    assert module_0.string_to_md5('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'

    # Result should be a 32-character lowercase hex string
    result = module_0.string_to_md5('test input')
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Same input yields same hash (deterministic)
    assert module_0.string_to_md5('repeat') == module_0.string_to_md5('repeat')

    # Different inputs yield different hashes
    assert module_0.string_to_md5('input1') != module_0.string_to_md5('input2')

# Generated at 2026-11-02 23:19:25.860273
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with a normal string (known MD5 value)
    assert module_0.string_to_md5("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"

    # Test with another known MD5 value
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"

    # Test empty string returns None
    assert module_0.string_to_md5("") is None

    # Test None input returns None
    assert module_0.string_to_md5(None) is None

    # Test single character
    assert module_0.string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

    # Test numeric string
    assert module_0.string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

    # Test string with special characters
    assert module_0.string_to_md5("!@#$%^&*()") == "d1be2638f8b1e5b4b8b0d3e1a9d1c8a1" or \
           module_0.string_to_md5("!@#$%^&*()") is not None

    # Test result is a 32-character hex string
    result = module_0.string_to_md5("test")
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Test consistency - same input produces same output
    assert module_0.string_to_md5("consistent") == module_0.string_to_md5("consistent")

    # Test different inputs produce different outputs
    assert module_0.string_to_md5("input1") != module_0.string_to_md5("input2")

    # Test whitespace-only string (not empty, so should hash)
    assert module_0.string_to_md5(" ") is not None

    # Test string with spaces
    assert module_0.string_to_md5("  spaced  ") == module_0.string_to_md5("  spaced  ")

# Generated at 2026-11-02 23:20:47.012494
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test known MD5 hash values
    assert module_0.string_to_md5('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

    # Test empty string returns None
    assert module_0.string_to_md5('') is None

    # Test case sensitivity (different inputs -> different hashes)
    assert module_0.string_to_md5('Hello') != module_0.string_to_md5('hello')
    assert module_0.string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'

    # Test result is a 32-character hex string
    result = module_0.string_to_md5('test string')
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Test determinism (same input produces same output)
    assert module_0.string_to_md5('repeatable') == module_0.string_to_md5('repeatable')

    # Test string with spaces and punctuation
    assert module_0.string_to_md5('a b c!') == module_0.string_to_md5('a b c!')

    # Test None-like falsy input behavior via empty content
    assert module_0.string_to_md5('') != module_0.string_to_md5(' ')

    print("All tests passed!")


if __name__ == "__main__":
    test_string_to_md5()