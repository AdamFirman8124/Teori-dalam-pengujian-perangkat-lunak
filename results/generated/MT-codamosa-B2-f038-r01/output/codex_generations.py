

# Generated at 2026-11-02 16:44:51.440222
# Unit test for function encode_cyclic
def test_encode_cyclic():
    from random import randint, choice

    # Deterministic cases
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"

    # Partial trailing group must remain untouched
    assert module_0.encode_cyclic("abcdefg") == "bcaefdg"
    assert module_0.encode_cyclic("xyz") == "yzx"

    # Round-trip property: decoding an encoded string restores the original
    chars = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(100):
        s = "".join(choice(chars) for _ in range(randint(1, 30)))
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        # Encoding twice then once more returns the original (encode^3 == id on full groups)
        assert module_0.encode_cyclic(module_0.encode_cyclic(module_0.encode_cyclic(s))) == s

# Generated at 2026-11-02 16:47:02.609203
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Single full group of 3: first char moves to end
    assert module_0.encode_cyclic("abc") == "bca"

    # Multiple full groups: each group cycled independently
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # Trailing group with fewer than 3 chars remains unchanged
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcaed"

    # Groups of length 1 or 2 are unchanged
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Verify decode_cyclic inverts encode_cyclic
    for s in ["", "a", "ab", "abc", "abcd", "hello", "world!", "abcdefg"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # Length is preserved
    for s in ["", "x", "xy", "xyz", "xyzw", "xyzwv"]:
        assert len(module_0.encode_cyclic(s)) == len(s)

    # Characters are preserved (permutation only)
    assert sorted(module_0.encode_cyclic("abcdef")) == sorted("abcdef")


test_encode_cyclic()
print("All tests passed!")

# Generated at 2026-11-02 16:48:30.612869
# Unit test for function encode_cyclic
def test_encode_cyclic():
# nonce:977e5a0b
    # Single complete group of 3 characters gets cycled
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("xyz") == "yzx"

    # Groups shorter than 3 characters remain unchanged
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Multiple groups: each full group cycled, trailing remainder untouched
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefg") == "bcaefdg"
    assert module_0.encode_cyclic("abcdefgh") == "bcaefdh"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdgih"

    # Round-trip property: decode(encode(s)) == s for strings of all lengths
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef",
              "abcdefghi", "hello world", "The quick brown fox"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        assert module_0.encode_cyclic(decode_cyclic(s)) == s

    # Encoding twice is NOT identity (since 3-cycles applied once are not identity)
    assert module_0.encode_cyclic(module_0.encode_cyclic("abc")) == "cab"
    assert decode_cyclic(module_0.encode_cyclic(module_0.encode_cyclic("abc"))) == "abc"


test_encode_cyclic()

# Generated at 2026-11-02 16:51:41.236723
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # Decoding an encoded string should return the original string
    assert module_0.decode_cyclic(encode_cyclic("abc")) == "abc"
    assert module_0.decode_cyclic(encode_cyclic("")) == ""
    assert module_0.decode_cyclic(encode_cyclic("a")) == "a"
    assert module_0.decode_cyclic(encode_cyclic("ab")) == "ab"
    assert module_0.decode_cyclic(encode_cyclic("abcd")) == "abcd"
    assert module_0.decode_cyclic(encode_cyclic("abcde")) == "abcde"
    assert module_0.decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
    assert module_0.decode_cyclic(encode_cyclic("abcdefghi")) == "abcdefghi"
    assert module_0.decode_cyclic(encode_cyclic("hello world")) == "hello world"
    assert module_0.decode_cyclic(encode_cyclic("The quick brown fox jumps over the lazy dog")) == "The quick brown fox jumps over the lazy dog"

    # Decoding a known encoded value
    assert module_0.decode_cyclic("bca") == "abc"
    assert module_0.decode_cyclic("bcadef") == "abcdef"

    # Decoding twice-encoded string equals original
    for s in ["", "x", "xy", "xyz", "xyzw", "xyzwv", "aaa", "ababab", "!@#$%^&*()"]:
        assert module_0.decode_cyclic(encode_cyclic(encode_cyclic(s))) == s

    # module_0.decode_cyclic(encode_cyclic(s)) == s for random-ish strings of many lengths
    import string
    for n in range(0, 30):
        s = "".join(string.ascii_letters[i % len(string.ascii_letters)] for i in range(n))
        assert module_0.decode_cyclic(encode_cyclic(s)) == s