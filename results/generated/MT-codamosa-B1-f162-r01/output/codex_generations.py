

# Generated at 2026-10-25 08:05:53.698747
# Unit test for function string_to_md5

# Generated at 2026-10-25 08:05:56.225363
# Unit test for function string_to_md5

# Generated at 2026-10-25 08:05:58.749713
# Unit test for function string_to_md5

# Generated at 2026-10-25 08:06:01.167250
# Unit test for function string_to_md5

# Generated at 2026-10-25 08:06:03.839600
# Unit test for function string_to_md5

# Generated at 2026-10-25 08:06:06.308611
# Unit test for function string_to_md5

# Generated at 2026-10-25 08:06:07.676732
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

# Generated at 2026-10-25 08:06:09.030866
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

# Generated at 2026-10-25 08:06:10.436014
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