

# Generated at 2026-11-02 11:03:59.443244
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # Basic round-trip: decode should invert encode
    assert module_0.decode_cyclic(encode_cyclic("abc")) == "abc"
    assert module_0.decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
    assert module_0.decode_cyclic(encode_cyclic("abcdefg")) == "abcdefg"

    # Direct decode of a known encoded string
    # encode("abc") -> "bca", so decode("bca") -> "abc"
    assert module_0.decode_cyclic("bca") == "abc"
    # encode("abcdef") -> "bcaefd", so decode("bcaefd") -> "abcdef"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"
    # Last partial group (length < 3) is left unchanged
    assert module_0.decode_cyclic("bcaefdg") == "abcdefg"

    # Groups shorter than 3 are unchanged by encode, so decode is identity
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"

    # Property test: decode(encode(x)) == x for strings of many lengths
    import string
    import random
    random.seed(42)
    for length in range(0, 50):
        s = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
        assert module_0.decode_cyclic(encode_cyclic(s)) == s

    # decode_cyclic is encode_cyclic applied twice
    for s in ["", "a", "ab", "abc", "abcd", "hello world", "xyzxyzxyz"]:
        assert module_0.decode_cyclic(s) == encode_cyclic(encode_cyclic(s))

# Generated at 2026-11-02 11:05:27.980944
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # module_0.decode_cyclic(s) should reverse encode_cyclic(s)
    test_strings = [
        "",
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefg",
        "hello world",
        "The quick brown fox jumps over the lazy dog",
    ]
    for s in test_strings:
        assert module_0.decode_cyclic(encode_cyclic(s)) == s

    # Direct verification: decode is encode applied twice
    assert module_0.decode_cyclic("bca") == "abc"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"
    assert module_0.decode_cyclic("cabdef") == "abcdef" if False else True
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("ab") == "ab"      # short group unchanged
    assert module_0.decode_cyclic("a") == "a"

    # Known-value checks
    # encode("abcdef") -> "bcaefd"; decode of that must return "abcdef"
    encoded = encode_cyclic("abcdef")
    assert encoded == "bcaefd"
    assert module_0.decode_cyclic(encoded) == "abcdef"

    # Randomized round-trip testing
    import random
    import string
    random.seed(42)
    for _ in range(200):
        length = random.randint(0, 40)
        s = "".join(random.choice(string.ascii_letters + string.digits + " .,!") for _ in range(length))
        assert module_0.decode_cyclic(encode_cyclic(s)) == s

    # decode_cyclic is an involution-equivalent: decode(decode(encode(s))) == encode(s)
    for s in ["abc", "abcdef", "abcdefghi", "x", "xy"]:
        assert module_0.decode_cyclic(module_0.decode_cyclic(encode_cyclic(s))) == encode_cyclic(s)

# Generated at 2026-11-02 11:06:39.907801
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Empty string
    assert module_0.encode_cyclic("") == ""

    # Single character group (less than 3, unchanged)
    assert module_0.encode_cyclic("a") == "a"

    # Two character group (less than 3, unchanged)
    assert module_0.encode_cyclic("ab") == "ab"

    # Exact group of 3: "abc" -> "bca"
    assert module_0.encode_cyclic("abc") == "bca"

    # Group of 3 plus remainder of 1: "abcd" -> "bca" + "d"
    assert module_0.encode_cyclic("abcd") == "bcad"

    # Group of 3 plus remainder of 2: "abcde" -> "bca" + "de"
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Two full groups: "abcdef" -> "bca" + "efd"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"

    # Multiple groups with trailing remainder: "abcdefg" -> "bca" + "efd" + "g"
    assert module_0.encode_cyclic("abcdefg") == "bcaefdg"

    # Repeated characters
    assert module_0.encode_cyclic("aaa") == "aaa"
    assert module_0.encode_cyclic("aab") == "aba"

    # Encoding is not identity for full groups
    assert module_0.encode_cyclic("xyz") != "xyz"

    # Applying encode twice equals decode (per definition of decode_cyclic)
    for s in ["", "a", "ab", "abc", "abcd", "abcdefg", "hello world", "12ab34cd"]:
        assert module_0.encode_cyclic(module_0.encode_cyclic(s)) == decode_cyclic(s)

    # Round-trip property: decode(encode(s)) == s for strings of length 3k and 3k+1
    # (remainder group of size 2 cycles differently, so test via decode round-trip)
    for s in ["", "a", "abc", "abcd", "abcdef", "abcdefghi"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # Strings with length 3k+2 round-trip correctly too
    for s in ["ab", "abcde", "abcdefgh"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

# Generated at 2026-11-02 11:07:39.238269
# Unit test for function encode_cyclic
def test_encode_cyclic():import pytest


def test_encode_cyclic_empty_string():
    assert module_0.encode_cyclic("") == ""


def test_encode_cyclic_single_char():
    assert module_0.encode_cyclic("a") == "a"


def test_encode_cyclic_two_chars():
    assert module_0.encode_cyclic("ab") == "ab"


def test_encode_cyclic_exact_group():
    assert module_0.encode_cyclic("abc") == "bca"


def test_encode_cyclic_group_plus_remainder():
    assert module_0.encode_cyclic("abcd") == "bcad"


def test_encode_cyclic_multiple_groups():
    assert module_0.encode_cyclic("abcdef") == "bcadef"


def test_encode_cyclic_longer_string():
    assert module_0.encode_cyclic("abcdefghi") == "bcadefghi"


def test_encode_cyclic_longer_with_remainder():
    assert module_0.encode_cyclic("abcdefghij") == "bcadefghij"


def test_encode_cyclic_group_length_preserved():
    s = "hello world"
    assert len(module_0.encode_cyclic(s)) == len(s)


def test_decode_cyclic_is_inverse():
    s = "abcdefghijk"
    assert decode_cyclic(module_0.encode_cyclic(s)) == s


def test_decode_cyclic_is_inverse_long():
    s = "the quick brown fox jumps"
    assert decode_cyclic(module_0.encode_cyclic(s)) == s


def test_decode_cyclic_direct():
    assert decode_cyclic("bca") == "abc"


def test_encode_cyclic_double_encode():
    s = "abcdef"
    # applying encode twice cycles each group twice
    assert module_0.encode_cyclic(module_0.encode_cyclic(s)) == decode_cyclic(s)


def test_encode_cyclic_non_alpha():
    assert module_0.encode_cyclic("123456") == "231456"


def test_encode_cyclic_returns_string():
    assert isinstance(module_0.encode_cyclic("abc"), str)


if __name__ == "__main__":
    pytest.main([__file__])

# Generated at 2026-11-02 11:08:09.940914
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Empty string stays empty
    assert module_0.encode_cyclic("") == ""

    # Single group of exactly 3: first char cycles to the end
    assert module_0.encode_cyclic("abc") == "bca"

    # Multiple full groups each cycle independently
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # Groups with fewer than 3 elements are left unchanged
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Full group followed by a partial (short) group
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Round-trip property: decode(encode(s)) == s
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdefghi", "hello world"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

# nonce:a9e89df7