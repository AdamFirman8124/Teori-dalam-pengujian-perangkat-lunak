

# Generated at 2026-10-25 09:51:30.390243
# Unit test for function encode_cyclic
def test_encode_cyclic():
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # length is preserved and short groups are unchanged
    assert len(module_0.encode_cyclic("Hello, World!")) == len("Hello, World!")

    # encode + decode round-trip
    for s in ["", "a", "ab", "abc", "abcd", "Hello, World!", "123456789"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        assert module_0.encode_cyclic(decode_cyclic(s)) == s

# Generated at 2026-10-25 09:51:31.824217
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # decode is inverse of encode for full 3-char groups
    assert module_0.decode_cyclic("bca") == "abc"
    assert module_0.decode_cyclic("cab") == "bca"
    assert module_0.decode_cyclic("abc") == "cab"

    # groups with < 3 chars are unchanged
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"

    # round-trip: decode(encode(s)) == s
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "hello", "abcdef", "123456789"]:
        assert module_0.decode_cyclic(encode_cyclic(s)) == s
        assert encode_cyclic(module_0.decode_cyclic(s)) == s

# Generated at 2026-10-25 09:51:34.589205
# Unit test for function encode_cyclic
def test_encode_cyclic():
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # length is preserved and short groups are unchanged
    assert len(module_0.encode_cyclic("Hello, World!")) == len("Hello, World!")

    # encode + decode round-trip
    for s in ["", "a", "ab", "abc", "abcd", "Hello, World!", "123456789"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        assert module_0.encode_cyclic(decode_cyclic(s)) == s

# Generated at 2026-10-25 09:51:36.124603
# Unit test for function encode_cyclic
def test_encode_cyclic():
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # length is preserved and short groups are unchanged
    assert len(module_0.encode_cyclic("Hello, World!")) == len("Hello, World!")

    # encode + decode round-trip
    for s in ["", "a", "ab", "abc", "abcd", "Hello, World!", "123456789"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        assert module_0.encode_cyclic(decode_cyclic(s)) == s

# Generated at 2026-10-25 09:51:37.561070
# Unit test for function encode_cyclic
def test_encode_cyclic():
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # length is preserved and short groups are unchanged
    assert len(module_0.encode_cyclic("Hello, World!")) == len("Hello, World!")

    # encode + decode round-trip
    for s in ["", "a", "ab", "abc", "abcd", "Hello, World!", "123456789"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        assert module_0.encode_cyclic(decode_cyclic(s)) == s