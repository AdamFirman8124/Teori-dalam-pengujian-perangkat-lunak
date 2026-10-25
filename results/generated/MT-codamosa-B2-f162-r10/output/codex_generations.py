

# Generated at 2026-10-24 20:53:25.058986
# Unit test for function string_to_md5

# Generated at 2026-10-24 20:53:27.475154
# Unit test for function string_to_md5

# Generated at 2026-10-24 20:53:29.892956
# Unit test for function string_to_md5

# Generated at 2026-10-24 20:53:32.309284
# Unit test for function string_to_md5

# Generated at 2026-10-24 20:53:34.726791
# Unit test for function string_to_md5

# Generated at 2026-10-24 20:53:37.142395
# Unit test for function string_to_md5

# Generated at 2026-10-24 20:53:38.566578
# Unit test for function string_to_md5
def test_string_to_md5():
    # Known vectors
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"

    # Falsy input -> None per implementation
    assert module_0.string_to_md5("") is None
    assert module_0.string_to_md5(None) is None

    # Output format: 32-char lowercase hex
    result = module_0.string_to_md5("test")
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Deterministic
    assert module_0.string_to_md5("hello") == module_0.string_to_md5("hello")
    assert module_0.string_to_md5("hello") != module_0.string_to_md5("Hello")

    # Non-ascii fails because of .encode('ascii')
    try:
        module_0.string_to_md5("cafÃ©")
        assert False, "Expected UnicodeEncodeError for non-ascii input"
    except UnicodeEncodeError:
        pass

# Generated at 2026-10-24 20:53:40.160721
# Unit test for function string_to_md5
def test_string_to_md5():
    # Known vectors
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"

    # Falsy input -> None per implementation
    assert module_0.string_to_md5("") is None
    assert module_0.string_to_md5(None) is None

    # Output format: 32-char lowercase hex
    result = module_0.string_to_md5("test")
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Deterministic
    assert module_0.string_to_md5("hello") == module_0.string_to_md5("hello")
    assert module_0.string_to_md5("hello") != module_0.string_to_md5("Hello")

    # Non-ascii fails because of .encode('ascii')
    try:
        module_0.string_to_md5("cafÃ©")
        assert False, "Expected UnicodeEncodeError for non-ascii input"
    except UnicodeEncodeError:
        pass

# Generated at 2026-10-24 20:53:41.570506
# Unit test for function string_to_md5
def test_string_to_md5():
    # Known vectors
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"

    # Falsy input -> None per implementation
    assert module_0.string_to_md5("") is None
    assert module_0.string_to_md5(None) is None

    # Output format: 32-char lowercase hex
    result = module_0.string_to_md5("test")
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)

    # Deterministic
    assert module_0.string_to_md5("hello") == module_0.string_to_md5("hello")
    assert module_0.string_to_md5("hello") != module_0.string_to_md5("Hello")

    # Non-ascii fails because of .encode('ascii')
    try:
        module_0.string_to_md5("cafÃ©")
        assert False, "Expected UnicodeEncodeError for non-ascii input"
    except UnicodeEncodeError:
        pass