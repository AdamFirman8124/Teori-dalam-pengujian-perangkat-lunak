

# Generated at 2026-10-25 09:22:38.800774
# Unit test for function string_to_md5
def test_string_to_md5():
    # Normal string
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    # Empty string returns None
    assert module_0.string_to_md5('') is None
    # None input returns None
    assert module_0.string_to_md5(None) is None
    # String with spaces
    assert module_0.string_to_md5(' ') == hashlib.md5(b' ').hexdigest()
    # Unicode input (non-ascii) should raise
    try:
        module_0.string_to_md5('hÃ©llo')
        assert False, "Expected UnicodeEncodeError"
    except UnicodeEncodeError:
        pass

test_string_to_md5()
print("All tests passed")

# Generated at 2026-10-25 09:22:41.216804
# Unit test for function string_to_md5

# Generated at 2026-10-25 09:22:43.635095
# Unit test for function string_to_md5

# Generated at 2026-10-25 09:22:46.050948
# Unit test for function string_to_md5

# Generated at 2026-10-25 09:22:48.466967
# Unit test for function string_to_md5

# Generated at 2026-10-25 09:22:50.878570
# Unit test for function string_to_md5

# Generated at 2026-10-25 09:23:00.302232
# Unit test for function string_to_md5
def test_string_to_md5():assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

# Generated at 2026-10-25 09:23:01.640382
# Unit test for function string_to_md5
def test_string_to_md5():
    # Normal string
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    # Empty string returns None
    assert module_0.string_to_md5('') is None
    # None input returns None
    assert module_0.string_to_md5(None) is None
    # String with spaces
    assert module_0.string_to_md5(' ') == hashlib.md5(b' ').hexdigest()
    # Unicode input (non-ascii) should raise
    try:
        module_0.string_to_md5('hÃ©llo')
        assert False, "Expected UnicodeEncodeError"
    except UnicodeEncodeError:
        pass

test_string_to_md5()
print("All tests passed")

# Generated at 2026-10-25 09:23:02.972620
# Unit test for function string_to_md5
def test_string_to_md5():
    # Normal string
    assert module_0.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    # Empty string returns None
    assert module_0.string_to_md5('') is None
    # None input returns None
    assert module_0.string_to_md5(None) is None
    # String with spaces
    assert module_0.string_to_md5(' ') == hashlib.md5(b' ').hexdigest()
    # Unicode input (non-ascii) should raise
    try:
        module_0.string_to_md5('hÃ©llo')
        assert False, "Expected UnicodeEncodeError"
    except UnicodeEncodeError:
        pass

test_string_to_md5()
print("All tests passed")