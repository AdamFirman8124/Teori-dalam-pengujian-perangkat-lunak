

# Generated at 2026-11-02 14:07:14.146072
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with a simple string
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    # Test with another known MD5 value
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'

    # Test with 'hello'
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

    # Test with empty string - should return None
    assert module_0.string_to_md5('') is None

    # Test with a string containing spaces
    assert module_0.string_to_md5('a b c') == '820f6e5b2da3389f33f653b3d8505868'

    # Test that result is a 32-character hex string
    result = module_0.string_to_md5('test')
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Test consistency - same input gives same output
    assert module_0.string_to_md5('consistent') == module_0.string_to_md5('consistent')

    # Test different inputs give different outputs
    assert module_0.string_to_md5('input1') != module_0.string_to_md5('input2')

    print("All tests passed!")


if __name__ == "__main__":
    test_string_to_md5()

# Generated at 2026-11-02 14:08:57.459634
# Unit test for function string_to_md5
def test_string_to_md5():
    import pytest

    # Test with known MD5 hash values
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"
    assert module_0.string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

    # Test empty string returns None
    assert module_0.string_to_md5("") is None

    # Test None input returns None
    assert module_0.string_to_md5(None) is None

    # Test result format: 32 lowercase hex characters
    result = module_0.string_to_md5("test")
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Test consistency: same input yields same output
    assert module_0.string_to_md5("consistent") == module_0.string_to_md5("consistent")

    # Test strings with spaces, digits, and punctuation
    assert module_0.string_to_md5("a b c!") == module_0.string_to_md5("a b c!")

    # Test non-ascii characters raise UnicodeEncodeError (encodes as ascii)
    with pytest.raises(UnicodeEncodeError):
        module_0.string_to_md5("héllo")

    # Test whitespace-only string (truthy, so it hashes)
    assert module_0.string_to_md5(" ") == "7215ee9c7d9dc229d2921a40e1789961"

# Generated at 2026-11-02 14:10:38.215751
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with a simple string
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

    # Test with a string containing spaces
    assert module_0.string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'

    # Test with a string containing numbers
    assert module_0.string_to_md5('abc123') == 'e99a18c428cb38d5f260853678922e03'

    # Test with an empty string (should return None)
    assert module_0.string_to_md5('') is None

    # Test with None (should return None)
    assert module_0.string_to_md5(None) is None

    # Test with a longer string
    assert module_0.string_to_md5('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'

    # Test with special characters
    assert module_0.string_to_md5('!@#$%^&*()') == 'a3c65c2974270fd0971b7d5e6e4258e6'

    # Test that result is a 32-character hex string
    result = module_0.string_to_md5('test')
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Test consistency: same input produces same output
    assert module_0.string_to_md5('consistent') == module_0.string_to_md5('consistent')

    # Test different inputs produce different outputs
    assert module_0.string_to_md5('input1') != module_0.string_to_md5('input2')

    # Verify against hashlib directly
    text = 'verification'
    assert module_0.string_to_md5(text) == hashlib.md5(text.encode('ascii')).hexdigest()

    print("All tests passed!")

test_string_to_md5()

# Generated at 2026-11-02 14:12:12.557495
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with a non-empty string (known MD5 value)
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    # Test with another known MD5 value
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'

    # Test with an empty string -> should return None
    assert module_0.string_to_md5('') is None

    # Test with None -> should return None
    assert module_0.string_to_md5(None) is None

    # Test with a string containing spaces and punctuation
    text = 'The quick brown fox jumps over the lazy dog!'
    assert module_0.string_to_md5(text) == hashlib.md5(text.encode('ascii')).hexdigest()

    # Test with digits and special characters
    text = '12345!@#$%'
    assert module_0.string_to_md5(text) == hashlib.md5(text.encode('ascii')).hexdigest()

    # Test result format: 32-character lowercase hex string
    result = module_0.string_to_md5('test')
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Test consistency: same input yields same output
    assert module_0.string_to_md5('consistent') == module_0.string_to_md5('consistent')

    # Test different inputs yield different outputs
    assert module_0.string_to_md5('input1') != module_0.string_to_md5('input2')

    # Test single character
    assert module_0.string_to_md5('a') == hashlib.md5(b'a').hexdigest()

    # Test non-ascii input raises an error (ascii encoding enforced)
    try:
        module_0.string_to_md5('héllo')
        assert False, "Expected UnicodeEncodeError for non-ascii input"
    except UnicodeEncodeError:
        pass

# Generated at 2026-11-02 14:13:54.339858
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Empty/falsy input returns None
    assert module_0.string_to_md5('') is None
    assert module_0.string_to_md5(None) is None

    # Known MD5 hash values
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert module_0.string_to_md5('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert module_0.string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'

    # Consistency with hashlib directly
    assert module_0.string_to_md5('test123') == hashlib.md5(b'test123').hexdigest()
    assert module_0.string_to_md5('Python 3.9!') == hashlib.md5(b'Python 3.9!').hexdigest()

    # Same input yields same output (deterministic)
    assert module_0.string_to_md5('repeat') == module_0.string_to_md5('repeat')

    # Different inputs yield different hashes
    assert module_0.string_to_md5('input1') != module_0.string_to_md5('input2')

    # Result is a 32-character lowercase hex string
    result = module_0.string_to_md5('some random text')
    assert len(result) == 32
    assert result == result.lower()
    assert all(c in '0123456789abcdef' for c in result)