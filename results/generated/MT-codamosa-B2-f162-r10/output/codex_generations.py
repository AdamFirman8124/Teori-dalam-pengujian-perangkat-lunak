

# Generated at 2026-11-02 06:52:03.599527
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Test with a known string
    assert module_0.string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    # Test with another known string
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"

    # Test empty string returns None
    assert module_0.string_to_md5("") is None

    # Test None input returns None
    assert module_0.string_to_md5(None) is None

    # Test result matches hashlib directly
    text = "test input"
    expected = hashlib.md5(text.encode('ascii')).hexdigest()
    assert module_0.string_to_md5(text) == expected

    # Test whitespace-only string (non-empty, so it hashes)
    assert module_0.string_to_md5(" ") == hashlib.md5(b" ").hexdigest()

    # Test string containing digits and symbols
    text = "123!@#$%"
    assert module_0.string_to_md5(text) == hashlib.md5(text.encode('ascii')).hexdigest()

    # Test non-ascii input raises UnicodeEncodeError
    try:
        module_0.string_to_md5("héllo")
        assert False, "Expected UnicodeEncodeError for non-ascii input"
    except UnicodeEncodeError:
        pass

    print("All tests passed!")


if __name__ == "__main__":
    test_string_to_md5()

# Generated at 2026-11-02 06:53:25.103680
# Unit test for function string_to_md5
def test_string_to_md5():
    # Empty string returns None
    assert module_0.string_to_md5("") is None

    # Known MD5 values
    assert module_0.string_to_md5("Hello world") == "b10a8db164e0754105b7a99be72e3fe5"
    assert module_0.string_to_md5("password") == "5f4dcc3b5aa765d61d8327deb882cf99"

    # Whitespace is significant
    assert module_0.string_to_md5("Hello world ") == hashlib.md5(b"Hello world ").hexdigest()

    # Consistency
    assert module_0.string_to_md5("test") == module_0.string_to_md5("test")

# Generated at 2026-11-02 06:55:57.691347
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with empty string - should return None
    assert module_0.string_to_md5('') is None

    # Test with None - should return None
    assert module_0.string_to_md5(None) is None

    # Test with a known string - verify against known MD5 hash
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'

    # Test with another known string
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

    # Test with a string containing spaces
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    # Test with a single character
    assert module_0.string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

    # Test that result is a 32-character hex string
    result = module_0.string_to_md5('test')
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Test consistency - same input gives same output
    assert module_0.string_to_md5('consistent') == module_0.string_to_md5('consistent')

    # Test that different inputs give different outputs
    assert module_0.string_to_md5('input1') != module_0.string_to_md5('input2')

    print("All tests passed!")


if __name__ == '__main__':
    test_string_to_md5()

# Generated at 2026-11-02 06:57:22.479834
# Unit test for function string_to_md5
def test_string_to_md5():
    # Test with a well-known string and its expected MD5 hash
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

    # Test with another known value
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'

    # Test with a string containing spaces
    assert module_0.string_to_md5('Hello world') == 'b10a8db164e0754105b7a99be72e3fe5'

    # Test that empty string returns None
    assert module_0.string_to_md5('') is None

    # Test that None input returns None
    assert module_0.string_to_md5(None) is None

    # Test result is a 32-character lowercase hex string
    result = module_0.string_to_md5('test')
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Test consistency: same input yields same hash
    assert module_0.string_to_md5('test') == module_0.string_to_md5('test')

    # Test different inputs yield different hashes
    assert module_0.string_to_md5('test1') != module_0.string_to_md5('test2')

    # Test special characters (ASCII-safe)
    assert module_0.string_to_md5('!@#$%^&*()') == module_0.string_to_md5('!@#$%^&*()')
    assert module_0.string_to_md5('!@#$%^&*()') != module_0.string_to_md5('test')

    # Test whitespace-only string is truthy, so it gets hashed
    assert module_0.string_to_md5(' ') is not None
    assert module_0.string_to_md5(' ') == module_0.string_to_md5(' ')

# Generated at 2026-11-02 06:59:39.183435
# Unit test for function string_to_md5
def test_string_to_md5():
    import hashlib

    # Empty string returns None
    assert module_0.string_to_md5('') is None

    # None input returns None
    assert module_0.string_to_md5(None) is None

    # Non-empty strings return correct MD5 hex digests
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert module_0.string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
    assert module_0.string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'
    assert module_0.string_to_md5('123') == '202cb962ac59075b964b07152d234b70'

    # Result matches direct hashlib computation
    assert module_0.string_to_md5('test') == hashlib.md5('test'.encode('ascii')).hexdigest()

    # Result is a 32-character lowercase hex string
    result = module_0.string_to_md5('example')
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)

    # Non-ASCII input raises UnicodeEncodeError
    try:
        module_0.string_to_md5('héllo')
        assert False, "Expected UnicodeEncodeError"
    except UnicodeEncodeError:
        pass

    print("All tests passed!")


test_string_to_md5()