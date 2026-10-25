

# Generated at 2026-10-24 22:39:47.292297
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

# Generated at 2026-10-24 22:39:54.092450
# Unit test for function decode_cyclic
def test_decode_cyclic():
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"
    assert module_0.decode_cyclic("abc") == "cab"
    assert module_0.decode_cyclic("abcdef") == "cabfde"
    assert module_0.decode_cyclic("abcdefg") == "cabfdeg"

    # Verify decoding reverses encoding.
    for original in ["", "a", "ab", "abc", "abcdef", "abcdefg", "Hello, world!"]:
        assert module_0.decode_cyclic(encode_cyclic(original)) == original

# Generated at 2026-10-24 22:40:01.963485
# Unit test for function decode_cyclic
def test_decode_cyclic():
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"
    assert module_0.decode_cyclic("bca") == "abc"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"
    assert module_0.decode_cyclic("bcaefdg") == "abcdefg"

    # Verify that decoding reverses encoding.
    for original in ["abc", "abcdef", "abcdefg", "Hello, world!"]:
        assert module_0.decode_cyclic(encode_cyclic(original)) == original

# Generated at 2026-10-24 22:40:10.337430
# Unit test for function decode_cyclic
def test_decode_cyclic():
    test_cases = [
        ("", ""),
        ("a", "a"),
        ("ab", "ab"),
        ("bca", "abc"),
        ("bcad", "abcd"),
        ("bcaefd", "abcdef"),
        ("bcaefdg", "abcdefg"),
    ]

    for encoded, expected in test_cases:
        assert module_0.decode_cyclic(encoded) == expected

    # Verify decoding reverses encoding.
    for original in ["hello", "Python", "123456789", "a longer string!"]:
        assert module_0.decode_cyclic(encode_cyclic(original)) == original

# Generated at 2026-10-24 22:40:12.763991
# Unit test for function decode_cyclic

# Generated at 2026-10-24 22:40:15.181422
# Unit test for function decode_cyclic

# Generated at 2026-10-24 22:40:19.862374
# Unit test for function decode_cyclic
def test_decode_cyclic():assert module_0.decode_cyclic("") == ""