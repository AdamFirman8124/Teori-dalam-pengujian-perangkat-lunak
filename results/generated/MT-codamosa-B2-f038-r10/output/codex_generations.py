

# Generated at 2026-10-24 23:09:49.442176
# Unit test for function decode_cyclic
def test_decode_cyclic():
    test_cases = [
        ("", ""),
        ("a", "a"),
        ("ab", "ab"),
        ("abc", "cab"),
        ("abcdef", "cabfde"),
        ("abcdefg", "cabfdeg"),
    ]

    for encoded, expected in test_cases:
        assert module_0.decode_cyclic(encoded) == expected

    # Verify that decoding reverses encoding.
    originals = ["", "a", "ab", "abc", "hello", "abcdefghijkl"]
    for original in originals:
        assert module_0.decode_cyclic(encode_cyclic(original)) == original

# Generated at 2026-10-24 23:09:55.995288
# Unit test for function decode_cyclic
def test_decode_cyclic():
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"
    assert module_0.decode_cyclic("bca") == "abc"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"
    assert module_0.decode_cyclic("bcaefdg") == "abcdefg"

    # Verify decoding reverses encoding.
    for original in ["abc", "abcdef", "abcdefg", "Hello, world!"]:
        assert module_0.decode_cyclic(encode_cyclic(original)) == original

# Generated at 2026-10-24 23:09:57.318698
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

# Generated at 2026-10-24 23:09:58.645626
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

# Generated at 2026-10-24 23:10:00.002456
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