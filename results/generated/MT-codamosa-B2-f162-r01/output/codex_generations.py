

# Generated at 2026-10-24 14:38:16.239421
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

# Generated at 2026-10-24 14:38:21.754655
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

# Generated at 2026-10-24 14:38:29.611141
# Unit test for function string_to_md5
def test_string_to_md5():
    # known-value checks (precomputed md5 digests)
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == \
        "9e107d9d372bb6826bd81d3542a419d6"

    # falsy input -> None (empty string and None both hit the `if text else None`)
    assert module_0.string_to_md5("") is None
    assert module_0.string_to_md5(None) is None

    # output shape: always 32 lowercase hex chars
    out = module_0.string_to_md5("x")
    assert len(out) == 32 and all(c in "0123456789abcdef" for c in out)

    # non-ASCII raises (encode('ascii') is strict)
    try:
        module_0.string_to_md5("cafÃ©")
    except UnicodeEncodeError:
        pass
    else:
        raise AssertionError("expected UnicodeEncodeError for non-ASCII input")

    print("all string_to_md5 tests passed")

# Generated at 2026-10-24 14:38:31.259684
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

# Generated at 2026-10-24 14:38:32.711616
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