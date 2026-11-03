

# Generated at 2026-11-01 21:48:32.472195
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # nonce:ec4b8e73
    # empty string
    assert module_0.encode_cyclic("") == ""
    # groups smaller than 3 remain unchanged
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    # single full group: cyclic shift left by one
    assert module_0.encode_cyclic("abc") == "bca"
    # mixed full and partial groups
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefg") == "bcaefdg"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"
    # only the full groups are cycled, trailing partial group untouched
    assert module_0.encode_cyclic("xy") == "xy"
    assert module_0.encode_cyclic("xyz1") == "yzx1"
    # round trip through decode must restore the original
    assert decode_cyclic(module_0.encode_cyclic("hello world")) == "hello world"
    assert decode_cyclic(module_0.encode_cyclic("ab")) == "ab"


def test_decode_cyclic():
    # decoding is inverse of encoding
    assert decode_cyclic("bca") == "abc"
    assert decode_cyclic("bcad") == "abcd"
    assert decode_cyclic("bcaefd") == "abcdef"
    assert decode_cyclic("bcaefdhig") == "abcdefghi"
    # short groups pass through unchanged
    assert decode_cyclic("") == ""
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("ab") == "ab"


def test_encode_decode_roundtrip_random():
    import random
    import string
    alphabet = string.ascii_letters + string.digits
    for _ in range(200):
        n = random.randint(0, 40)
        s = "".join(random.choices(alphabet, k=n))
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

# Generated at 2026-11-01 21:48:46.275197
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Test empty string
    assert module_0.encode_cyclic("") == ""

    # Test strings shorter than 3 characters (unchanged)
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Test single group of exactly 3 characters (cycle: first char moves to end)
    assert module_0.encode_cyclic("abc") == "bca"

    # Test multiple full groups
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # Test trailing group with fewer than 3 characters (left unchanged)
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Test with repeated characters
    assert module_0.encode_cyclic("aaa") == "aaa"
    assert module_0.encode_cyclic("aaabbb") == "aaabbb"

    # Test round-trip property via decode_cyclic
    for s in ["", "a", "ab", "abc", "hello", "world!", "pytest tests"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    print("All tests passed!")


if __name__ == "__main__":
    test_encode_cyclic()

# Generated at 2026-11-01 21:49:22.118402
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # Direct known-value checks
    # encode_cyclic("abc") == "bca", so decoding "bca" yields "abc"
    assert module_0.decode_cyclic("bca") == "abc"
    # encode_cyclic("abcdef") == "bcadef", decoding restores "abcdef"
    assert module_0.decode_cyclic("bcadef") == "abcdef"

    # Decoding must invert encoding (round-trip) for various lengths
    assert module_0.decode_cyclic(encode_cyclic("")) == ""                     # empty
    assert module_0.decode_cyclic(encode_cyclic("a")) == "a"                   # length 1 (< 3, untouched by cycling)
    assert module_0.decode_cyclic(encode_cyclic("ab")) == "ab"                 # length 2 (< 3, untouched)
    assert module_0.decode_cyclic(encode_cyclic("abc")) == "abc"               # exactly one full group
    assert module_0.decode_cyclic(encode_cyclic("abcd")) == "abcd"             # full group + remainder
    assert module_0.decode_cyclic(encode_cyclic("abcdef")) == "abcdef"         # two full groups
    assert module_0.decode_cyclic(encode_cyclic("abcdefgh")) == "abcdefgh"     # groups + partial tail
    assert module_0.decode_cyclic(encode_cyclic("hello world")) == "hello world"

    # Randomized round-trip property test
    alphabet = string.ascii_letters + string.digits + " .,!?"
    for _ in range(200):
        n = random.randint(0, 60)
        s = "".join(random.choice(alphabet) for _ in range(n))
        assert module_0.decode_cyclic(encode_cyclic(s)) == s

    print("All decode_cyclic tests passed.")


if __name__ == "__main__":
    test_decode_cyclic()

# Generated at 2026-11-01 21:49:39.999754
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # decode_cyclic should invert encode_cyclic (round-trip property)
    assert module_0.decode_cyclic(encode_cyclic("abc")) == "abc"
    assert module_0.decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
    assert module_0.decode_cyclic(encode_cyclic("hello world")) == "hello world"
    assert module_0.decode_cyclic(encode_cyclic("a")) == "a"
    assert module_0.decode_cyclic(encode_cyclic("ab")) == "ab"
    assert module_0.decode_cyclic(encode_cyclic("abcd")) == "abcd"
    assert module_0.decode_cyclic(encode_cyclic("abcdefghij")) == "abcdefghij"
    assert module_0.decode_cyclic(encode_cyclic("")) == ""

    # Specific known decodings
    # "bca" encodes to "cab", which encodes back to "abc"
    assert module_0.decode_cyclic("bca") == "abc"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"
    # Trailing partial group (length < 3) is left untouched
    assert module_0.decode_cyclic("bcad") == "abcd"

    # Strings shorter than 3 characters pass through unchanged
    assert module_0.decode_cyclic("") == ""
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"

    # Randomized round-trip test
    import random
    import string
    for _ in range(100):
        length = random.randint(0, 50)
        s = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        assert module_0.decode_cyclic(encode_cyclic(s)) == s

# Generated at 2026-11-01 21:49:47.253116
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Test with empty string
    assert module_0.encode_cyclic("") == ""

    # Test with a single character (group shorter than 3, unchanged)
    assert module_0.encode_cyclic("a") == "a"

    # Test with two characters (group shorter than 3, unchanged)
    assert module_0.encode_cyclic("ab") == "ab"

    # Test with exactly three characters (cycled once)
    assert module_0.encode_cyclic("abc") == "bca"

    # Test with four characters (one full group + leftover)
    assert module_0.encode_cyclic("abcd") == "bcad"

    # Test with five characters (one full group + leftover of 2)
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Test with six characters (two full groups)
    assert module_0.encode_cyclic("abcdef") == "bcaefd"

    # Test with longer string mixing full groups and leftovers
    assert module_0.encode_cyclic("abcdefgh") == "bcaefdh"

    # Test decode_cyclic reverses encode_cyclic
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefghij"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # Test that encode is applied twice by decode (property check)
    for s in ["hello", "world!", "pytest"]:
        assert decode_cyclic(s) == module_0.encode_cyclic(module_0.encode_cyclic(s))