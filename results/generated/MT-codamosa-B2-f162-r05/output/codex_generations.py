

# Generated at 2026-10-24 11:39:01.203273
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:39:03.622660
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:39:06.039279
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:39:08.465310
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:39:10.888016
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:39:27.919113
# Unit test for function string_to_md5
def test_string_to_md5():assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"

# Generated at 2026-10-24 11:39:29.238913
# Unit test for function string_to_md5
def test_string_to_md5():
    # known MD5 vectors
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == \
        "9e107d9d372bb6826bd81d3542a419d6"

    # falsy input -> None (empty string, None)
    assert module_0.string_to_md5("") is None
    assert module_0.string_to_md5(None) is None

    # non-ascii raises UnicodeEncodeError
    with pytest.raises(UnicodeEncodeError):
        module_0.string_to_md5("hÃ©llo")

    # output shape: 32 lowercase hex chars
    out = module_0.string_to_md5("x")
    assert len(out) == 32
    assert all(c in "0123456789abcdef" for c in out)

# Generated at 2026-10-24 11:39:30.652774
# Unit test for function string_to_md5
def test_string_to_md5():
    # known MD5 vectors
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == \
        "9e107d9d372bb6826bd81d3542a419d6"

    # falsy input -> None (empty string, None)
    assert module_0.string_to_md5("") is None
    assert module_0.string_to_md5(None) is None

    # non-ascii raises UnicodeEncodeError
    with pytest.raises(UnicodeEncodeError):
        module_0.string_to_md5("hÃ©llo")

    # output shape: 32 lowercase hex chars
    out = module_0.string_to_md5("x")
    assert len(out) == 32
    assert all(c in "0123456789abcdef" for c in out)

# Generated at 2026-10-24 11:39:31.998068
# Unit test for function string_to_md5
def test_string_to_md5():
    # known MD5 vectors
    assert module_0.string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert module_0.string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
    assert module_0.string_to_md5("The quick brown fox jumps over the lazy dog") == \
        "9e107d9d372bb6826bd81d3542a419d6"

    # falsy input -> None (empty string, None)
    assert module_0.string_to_md5("") is None
    assert module_0.string_to_md5(None) is None

    # non-ascii raises UnicodeEncodeError
    with pytest.raises(UnicodeEncodeError):
        module_0.string_to_md5("hÃ©llo")

    # output shape: 32 lowercase hex chars
    out = module_0.string_to_md5("x")
    assert len(out) == 32
    assert all(c in "0123456789abcdef" for c in out)