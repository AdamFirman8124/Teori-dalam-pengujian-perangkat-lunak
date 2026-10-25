

# Generated at 2026-10-25 02:33:56.643218
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

# Generated at 2026-10-25 02:33:58.015874
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

# Generated at 2026-10-25 02:34:05.609765
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # Empty and incomplete groups remain unchanged
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"

    # Complete groups are cycled backward
    assert module_0.decode_cyclic("abc") == "cab"
    assert module_0.decode_cyclic("abcdef") == "cabfde"
    assert module_0.decode_cyclic("abcdefg") == "cabfdeg"

    # Decoding an encoded string restores the original
    for original in ("abc", "abcdef", "abcdefg", "Hello, world!"):
        assert module_0.decode_cyclic(encode_cyclic(original)) == original

# Generated at 2026-10-25 02:34:07.084430
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

# Generated at 2026-10-25 02:34:08.517958
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