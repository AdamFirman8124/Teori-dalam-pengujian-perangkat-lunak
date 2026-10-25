

# Generated at 2026-10-24 11:27:27.034517
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

# Generated at 2026-10-24 11:27:29.665849
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:32.080175
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:34.501014
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:37.072460
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:39.495139
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:41.919225
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:44.330260
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:46.752267
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:49.170488
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:51.591989
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:54.009271
# Unit test for function string_to_md5

# Generated at 2026-10-24 11:27:56.431864
# Unit test for function string_to_md5