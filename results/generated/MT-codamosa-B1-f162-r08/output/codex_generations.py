

# Generated at 2026-10-24 07:33:20.252123
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

# Generated at 2026-10-24 07:33:21.571520
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

# Generated at 2026-10-24 07:33:22.897165
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

# Generated at 2026-10-24 07:33:24.212205
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

# Generated at 2026-10-24 07:33:25.521551
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