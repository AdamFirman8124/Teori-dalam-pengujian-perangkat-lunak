

# Generated at 2026-10-24 06:00:09.154761
# Unit test for function string_to_md5
def test_string_to_md5():
    # Normal string
    assert module_0.string_to_md5('hello world') == hashlib.md5('hello world'.encode('ascii')).hexdigest()
    assert module_0.string_to_md5('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'

    # Empty string returns None
    assert module_0.string_to_md5('') is None

    # Single character
    assert module_0.string_to_md5('a') == hashlib.md5(b'a').hexdigest()

    # String with digits and symbols
    assert module_0.string_to_md5('abc123!@#') == hashlib.md5('abc123!@#'.encode('ascii')).hexdigest()

    # Case sensitivity: different cases give different hashes
    assert module_0.string_to_md5('Hello') != module_0.string_to_md5('hello')

    # Whitespace matters
    assert module_0.string_to_md5('hello ') != module_0.string_to_md5('hello')

    # Long string still works
    long_text = 'x' * 10000
    assert module_0.string_to_md5(long_text) == hashlib.md5(long_text.encode('ascii')).hexdigest()

    print("All tests passed!")

# Generated at 2026-10-24 06:00:11.684557
# Unit test for function string_to_md5

# Generated at 2026-10-24 06:00:14.099780
# Unit test for function string_to_md5

# Generated at 2026-10-24 06:00:16.609244
# Unit test for function string_to_md5

# Generated at 2026-10-24 06:00:19.488780
# Unit test for function string_to_md5

# Generated at 2026-10-24 06:00:21.903794
# Unit test for function string_to_md5

# Generated at 2026-10-24 06:00:25.737368
# Unit test for function string_to_md5
def test_string_to_md5():assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

# Generated at 2026-10-24 06:00:27.383547
# Unit test for function string_to_md5
def test_string_to_md5():
    # Normal string
    assert module_0.string_to_md5('hello world') == hashlib.md5('hello world'.encode('ascii')).hexdigest()
    assert module_0.string_to_md5('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'

    # Empty string returns None
    assert module_0.string_to_md5('') is None

    # Single character
    assert module_0.string_to_md5('a') == hashlib.md5(b'a').hexdigest()

    # String with digits and symbols
    assert module_0.string_to_md5('abc123!@#') == hashlib.md5('abc123!@#'.encode('ascii')).hexdigest()

    # Case sensitivity: different cases give different hashes
    assert module_0.string_to_md5('Hello') != module_0.string_to_md5('hello')

    # Whitespace matters
    assert module_0.string_to_md5('hello ') != module_0.string_to_md5('hello')

    # Long string still works
    long_text = 'x' * 10000
    assert module_0.string_to_md5(long_text) == hashlib.md5(long_text.encode('ascii')).hexdigest()

    print("All tests passed!")

# Generated at 2026-10-24 06:00:28.694891
# Unit test for function string_to_md5
def test_string_to_md5():
    # Normal string
    assert module_0.string_to_md5('hello world') == hashlib.md5('hello world'.encode('ascii')).hexdigest()
    assert module_0.string_to_md5('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'

    # Empty string returns None
    assert module_0.string_to_md5('') is None

    # Single character
    assert module_0.string_to_md5('a') == hashlib.md5(b'a').hexdigest()

    # String with digits and symbols
    assert module_0.string_to_md5('abc123!@#') == hashlib.md5('abc123!@#'.encode('ascii')).hexdigest()

    # Case sensitivity: different cases give different hashes
    assert module_0.string_to_md5('Hello') != module_0.string_to_md5('hello')

    # Whitespace matters
    assert module_0.string_to_md5('hello ') != module_0.string_to_md5('hello')

    # Long string still works
    long_text = 'x' * 10000
    assert module_0.string_to_md5(long_text) == hashlib.md5(long_text.encode('ascii')).hexdigest()

    print("All tests passed!")