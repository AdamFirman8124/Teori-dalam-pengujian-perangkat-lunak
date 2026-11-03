

# Generated at 2026-11-03 05:45:17.945253
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # Decoding an encoded string should return the original string
    assert module_0.decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
    assert module_0.decode_cyclic(encode_cyclic("")) == ""
    assert module_0.decode_cyclic(encode_cyclic("a")) == "a"
    assert module_0.decode_cyclic(encode_cyclic("ab")) == "ab"
    assert module_0.decode_cyclic(encode_cyclic("abc")) == "abc"
    assert module_0.decode_cyclic(encode_cyclic("hello world")) == "hello world"
    assert module_0.decode_cyclic(encode_cyclic("abcdefgh")) == "abcdefgh"

    # Direct behavior: decode is encode applied twice
    assert module_0.decode_cyclic("abcdef") == "cabfde"
    assert module_0.decode_cyclic("abcdefg") == "cabfdeg"
    assert module_0.decode_cyclic("abc") == "cab"
    assert module_0.decode_cyclic("ab") == "ab"  # group shorter than 3 is unchanged

    # Decoding is an involution on arbitrary strings of multiple-of-3 length
    for s in ["xyzxyz", "aaa", "123456789"]:
        assert module_0.decode_cyclic(module_0.decode_cyclic(s)) == encode_cyclic(s)

# Generated at 2026-11-03 05:47:54.006412
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # decode_cyclic should invert encode_cyclic
    assert module_0.decode_cyclic(encode_cyclic("")) == ""
    assert module_0.decode_cyclic(encode_cyclic("a")) == "a"
    assert module_0.decode_cyclic(encode_cyclic("ab")) == "ab"
    assert module_0.decode_cyclic(encode_cyclic("abc")) == "abc"
    assert module_0.decode_cyclic(encode_cyclic("abcd")) == "abcd"
    assert module_0.decode_cyclic(encode_cyclic("abcde")) == "abcde"
    assert module_0.decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
    assert module_0.decode_cyclic(encode_cyclic("abcdefg")) == "abcdefg"
    assert module_0.decode_cyclic(encode_cyclic("abcdefgh")) == "abcdefgh"
    assert module_0.decode_cyclic(encode_cyclic("abcdefghi")) == "abcdefghi"

    # direct decode of a known encoded string:
    # encode_cyclic("abcdef") == "bcaefd", so decoding "bcaefd" must yield "abcdef"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"
    # encode_cyclic("abcdefghij") == "bcaefdihg"... verify via encode first
    assert module_0.decode_cyclic(encode_cyclic("abcdefghij")) == "abcdefghij"

    # groups shorter than 3 are left unchanged by encode, decode must handle them
    assert module_0.decode_cyclic("xy") == "xy"
    assert module_0.decode_cyclic("x") == "x"

    # randomized round-trip tests
    import random
    import string
    for _ in range(100):
        s = "".join(random.choices(string.ascii_letters + string.digits,
                                   k=random.randint(0, 50)))
        assert module_0.decode_cyclic(encode_cyclic(s)) == s

# Generated at 2026-11-03 05:50:06.062216
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Empty string
    assert module_0.encode_cyclic("") == ""

    # Strings shorter than 3 are unchanged
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Single full group: cycle first element to the end
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("xyz") == "yzx"

    # Group of 3 plus remainder (remainder unchanged)
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Multiple full groups
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdihg".replace("ihg", "ifg")

    # Known example
    assert module_0.encode_cyclic("hello") == "ellho"

    # Encoding is invertible via decode_cyclic
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefgh",
              "python", "qwertyuiop", "The quick brown fox"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # Double encoding is identity (encode applied twice restores original)
    for s in ["abc", "abcdef", "abcdefghi", "hello world"]:
        assert module_0.encode_cyclic(module_0.encode_cyclic(s)) == s

# Generated at 2026-11-03 05:51:21.359376
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Test string with a single complete group of 3: first char moves to end
    assert module_0.encode_cyclic("abc") == "bca"

    # Test string with multiple complete groups
    assert module_0.encode_cyclic("abcdef") == "bcaefd"

    # Test string with complete groups and a trailing group of length 1 (unchanged)
    assert module_0.encode_cyclic("abcdefg") == "bcaefdg"

    # Test string with trailing group of length 2 (unchanged)
    assert module_0.encode_cyclic("abcdefxy") == "bcaefdxy"

    # Test empty string
    assert module_0.encode_cyclic("") == ""

    # Test single character (group smaller than 3, unchanged)
    assert module_0.encode_cyclic("a") == "a"

    # Test two characters (group smaller than 3, unchanged)
    assert module_0.encode_cyclic("ab") == "ab"

    # Test group of exactly 3 with distinct characters
    assert module_0.encode_cyclic("xyz") == "yzx"

    # Test string with repeated characters
    assert module_0.encode_cyclic("aaa") == "aaa"

    # Test round trip: decoding an encoded string returns the original
    for s in ["", "a", "ab", "abc", "abcd", "abcdef", "abcdefgh"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

# Generated at 2026-11-03 05:52:09.151082
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Empty string stays empty
    assert module_0.encode_cyclic("") == ""

    # Single character: group has fewer than 3 elements, unchanged
    assert module_0.encode_cyclic("a") == "a"

    # Two characters: group has fewer than 3 elements, unchanged
    assert module_0.encode_cyclic("ab") == "ab"

    # Exact group of 3: first element cycles to the end
    assert module_0.encode_cyclic("abc") == "bca"

    # Group of 3 plus remainder of 1 (remainder unchanged)
    assert module_0.encode_cyclic("abcd") == "bcad"

    # Group of 3 plus remainder of 2 (remainder unchanged)
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Two full groups, each cycled independently
    assert module_0.encode_cyclic("abcdef") == "bcaefd"

    # Multiple groups with a partial trailing group
    assert module_0.encode_cyclic("abcdefgh") == "bcaefdh"

    # Round trip: decoding an encoded string restores the original
    for s in ["", "a", "ab", "abc", "abcd", "hello world", "Python!"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # Encoding is an involution via decode: encode(encode(s)) == s
    for s in ["abcdef", "testing", "xyz"]:
        assert module_0.encode_cyclic(module_0.encode_cyclic(s)) == s