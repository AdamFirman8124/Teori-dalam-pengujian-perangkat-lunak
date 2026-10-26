

# Generated at 2026-10-25 07:13:42.029043
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

# Generated at 2026-10-25 07:13:43.360201
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

# Generated at 2026-10-25 07:13:44.696285
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

# Generated at 2026-10-25 07:13:46.039851
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

# Generated at 2026-10-25 07:13:47.445250
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