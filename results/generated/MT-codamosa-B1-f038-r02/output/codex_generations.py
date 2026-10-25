

# Generated at 2026-10-24 07:07:14.589695
# Unit test for function encode_cyclic

# Generated at 2026-10-24 07:07:17.008374
# Unit test for function encode_cyclic

# Generated at 2026-10-24 07:07:19.424922
# Unit test for function encode_cyclic

# Generated at 2026-10-24 07:07:21.843157
# Unit test for function decode_cyclic

# Generated at 2026-10-24 07:07:24.262622
# Unit test for function decode_cyclic

# Generated at 2026-10-24 07:07:29.077306
# Unit test for function decode_cyclic
def test_decode_cyclic():assert module_0.decode_cyclic("") == ""

# Generated at 2026-10-24 07:07:30.471381
# Unit test for function encode_cyclic
def test_encode_cyclic():
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefgh") == "bcaefdgh"

    # encoding twice then decoding returns original
    for s in ["", "a", "ab", "abc", "abcd", "hello", "abcdefghi"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        assert module_0.encode_cyclic(module_0.encode_cyclic(module_0.encode_cyclic(s))) == s

# Generated at 2026-10-24 07:07:31.873361
# Unit test for function encode_cyclic
def test_encode_cyclic():
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefgh") == "bcaefdgh"

    # encoding twice then decoding returns original
    for s in ["", "a", "ab", "abc", "abcd", "hello", "abcdefghi"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        assert module_0.encode_cyclic(module_0.encode_cyclic(module_0.encode_cyclic(s))) == s

# Generated at 2026-10-24 07:07:33.231874
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # empty and short strings (no full group of 3, unchanged)
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"

    # full group of 3: encode is left-rotate once,
    # decode is left-rotate twice (right-rotate once)
    assert encode_cyclic("abc") == "bca"
    assert module_0.decode_cyclic("abc") == "cab"
    assert module_0.decode_cyclic("bca") == "abc"

    # multiple full groups
    assert encode_cyclic("abcdef") == "bcaefd"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"

    # trailing incomplete group is left as-is
    assert encode_cyclic("abcd") == "bcad"
    assert module_0.decode_cyclic("bcad") == "abcd"

    # decode inverts encode, and encode inverts decode
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "hello world"]:
        assert module_0.decode_cyclic(encode_cyclic(s)) == s
        assert encode_cyclic(module_0.decode_cyclic(s)) == s