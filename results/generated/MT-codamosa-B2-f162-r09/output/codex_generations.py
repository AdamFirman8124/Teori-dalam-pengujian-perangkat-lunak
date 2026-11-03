

# Generated at 2026-11-02 10:31:01.939603
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Test with a known string
    assert module_0.string_to_md5("Hello world") == hashlib.md5(b"Hello world").hexdigest()
    assert module_0.string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    # Test with another known string
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    # Test with a longer sentence
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == "9e107d9d372bb6826bd81d3542a419d6"

    # Test with empty string (should return None)
    assert module_0.string_to_md5('') is None

    # Test with strings containing special characters
    assert module_0.string_to_md5("!@#$%^&*()") == hashlib.md5("!@#$%^&*()".encode('ascii')).hexdigest()

    # Test with numbers as string
    assert module_0.string_to_md5("123456") == hashlib.md5(b"123456").hexdigest()

    # Test with whitespace
    assert module_0.string_to_md5("   ") == hashlib.md5(b"   ").hexdigest()

    # Test that the result is a 32-character hexadecimal string
    result = module_0.string_to_md5("test")
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    print("All tests passed!")


if __name__ == "__main__":
    test_string_to_md5()

# Generated at 2026-11-02 10:32:07.574358
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with a known string
    assert module_0.string_to_md5("Hello world") == "b10a8db164e0754105b7a99be72e3fe5"

    # Test with a single word
    assert module_0.string_to_md5("Hello") == "8b1a9953c4611296a827abf8c47804d7"

    # Test with another known string
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"

    # Test with an empty string -> should return None
    assert module_0.string_to_md5("") is None

    # Test that result is a 32-character hex string for non-empty input
    result = module_0.string_to_md5("test input")
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Test consistency: same input yields same output
    assert module_0.string_to_md5("repeat") == module_0.string_to_md5("repeat")

    # Test that different inputs yield different outputs
    assert module_0.string_to_md5("input1") != module_0.string_to_md5("input2")

    # Test with a longer sentence
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == \
        "9e107d9d372bb6826bd81d3542a419d6"

    # Test with digits and special characters
    assert module_0.string_to_md5("12345!@#$%") == hashlib.md5(b"12345!@#$%").hexdigest()

    print("All tests passed!")


if __name__ == "__main__":
    test_string_to_md5()

# Generated at 2026-11-02 10:33:16.902723
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Test with a simple string
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    # Test with a string containing spaces
    assert module_0.string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    # Test with an empty string (should return None)
    assert module_0.string_to_md5("") is None

    # Test with a longer string
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == "9e107d9d372bb6826bd81d3542a419d6"

    # Test with numbers as string
    assert module_0.string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

    # Test with special characters
    assert module_0.string_to_md5("!@#$%^&*()") == hashlib.md5("!@#$%^&*()".encode('ascii')).hexdigest()

    # Test with a single character
    assert module_0.string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

    # Test that None input returns None (falsy check)
    assert module_0.string_to_md5(None) is None

    # Verify result is 32-character hex string for non-empty input
    result = module_0.string_to_md5("test")
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    print("All tests passed!")


if __name__ == "__main__":
    test_string_to_md5()

# Generated at 2026-11-02 10:34:12.844182
# Unit test for function string_to_md5
def test_string_to_md5():
    # nonce:5d04518a
    import hashlib

    # Known MD5 test vectors for non-empty strings
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert module_0.string_to_md5('message digest') == 'f96b697d7cb7938d525a2f31aaf161d0'
    assert module_0.string_to_md5('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'
    assert module_0.string_to_md5('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'

    # Empty string (falsy input) should return None
    assert module_0.string_to_md5('') is None

    # Output should be a 32-character lowercase hex digest
    result = module_0.string_to_md5('some text')
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)
    assert result == hashlib.md5(b'some text').hexdigest()

    # Different inputs should produce different hashes
    assert module_0.string_to_md5('a') != module_0.string_to_md5('b')

    # Non-ASCII input cannot be ascii-encoded, so should raise UnicodeEncodeError
    try:
        module_0.string_to_md5('héllo')
        assert False, "Expected UnicodeEncodeError for non-ASCII input"
    except UnicodeEncodeError:
        pass

# Generated at 2026-11-02 10:35:17.424954
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Test with a normal string (known MD5 hash)
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    # Test with another known hash
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"

    # Test with spaces and mixed case
    assert module_0.string_to_md5("Hello world") == "b10a8db164e0754105b7a99be72e3fe5"

    # Test with empty string -> should return None
    assert module_0.string_to_md5("") is None

    # Test with None input -> should return None
    assert module_0.string_to_md5(None) is None

    # Test consistency: same input produces same output
    assert module_0.string_to_md5("test") == module_0.string_to_md5("test")

    # Test output matches hashlib directly
    assert module_0.string_to_md5("test123") == hashlib.md5(b"test123").hexdigest()

    # Test output is a 32-character hex string
    result = module_0.string_to_md5("some text")
    assert isinstance(result, str) and len(result) == 32

    print("All tests passed!")


test_string_to_md5()