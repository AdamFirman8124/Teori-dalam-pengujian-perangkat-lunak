

# Generated at 2026-10-24 14:38:01.924654
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

# Generated at 2026-10-24 14:38:03.527000
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

# Generated at 2026-10-24 14:38:46.380780
# Unit test for function encode_cyclic
def test_encode_cyclic():
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcdea"
    assert module_0.encode_cyclic("abcdef") == "bcadef"
    assert module_0.encode_cyclic("abcdefg") == "bcadefg"
    # round-trip property: decode(encode(s)) == s for many random strings
    import random
    import string
    for _ in range(100):
        s = "".join(random.choice(string.ascii_lowercase)
                    for _ in range(random.randint(0, 30)))
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

# Generated at 2026-10-24 14:39:11.624088
# Unit test for function decode_cyclic
def test_decode_cyclic():
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"
    assert module_0.decode_cyclic("bca") == "abc"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"

    for s in ["", "a", "ab", "abc", "abcd", "abcdefg", "hello world", "123456789"]:
        assert module_0.decode_cyclic(encode_cyclic(s)) == s
        assert encode_cyclic(module_0.decode_cyclic(s)) == s

# Generated at 2026-10-24 14:39:14.039864
# Unit test for function decode_cyclic

# Generated at 2026-10-24 14:39:16.456070
# Unit test for function decode_cyclic

# Generated at 2026-10-24 14:39:18.961582
# Unit test for function decode_cyclic