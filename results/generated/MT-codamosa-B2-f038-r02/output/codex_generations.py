

# Generated at 2026-11-02 12:11:09.760408
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Test empty string
    assert module_0.encode_cyclic("") == ""

    # Test single character (group smaller than 3, unchanged)
    assert module_0.encode_cyclic("a") == "a"

    # Test two characters (group smaller than 3, unchanged)
    assert module_0.encode_cyclic("ab") == "ab"

    # Test exactly one full group of 3: cyclic shift
    assert module_0.encode_cyclic("abc") == "bca"

    # Test multiple full groups
    assert module_0.encode_cyclic("abcdef") == "bcaefd"

    # Test full groups plus remainder
    assert module_0.encode_cyclic("abcdefg") == "bcaefdg"
    assert module_0.encode_cyclic("abcdefgh") == "bcaefdhg"

    # Test that encode is reversible via decode_cyclic
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "hello world", "xyz123!@#"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # Test decode_cyclic directly on known values
    assert decode_cyclic("bca") == "abc"
    assert decode_cyclic("bcaefd") == "abcdef"
    assert decode_cyclic("") == ""
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("ab") == "ab"

# Generated at 2026-11-02 12:13:02.766335
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Full groups of 3: each group is cycled (first char moves to end)
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcadefghi"

    # Partial trailing group (length < 3) is left unchanged
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdefgh") == "bcadefgh"

    # Length not divisible by 3 with multiple groups
    assert module_0.encode_cyclic("abcdxyz") == "bcaxyzd"

    # Strings with spaces / special characters
    assert module_0.encode_cyclic("a b c!") == " b ca!"
    assert module_0.encode_cyclic("!!!???") == "!!???!"

    # decode_cyclic should invert encode_cyclic
    for s in ["", "a", "ab", "abc", "abcd", "abcdef", "abcdefgh", "hello world!"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # encode_cyclic applied twice equals decode applied once (for len 3 groups)
    assert module_0.encode_cyclic(module_0.encode_cyclic("abc")) == "abc".replace("abc", "cab")

    print("test_encode_cyclic passed")


if __name__ == "__main__":
    test_encode_cyclic()

# Generated at 2026-11-02 12:14:42.666257
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Empty string
    assert module_0.encode_cyclic("") == ""

    # Groups with fewer than 3 elements are unchanged
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Single full group: first element moves to the end
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("xyz") == "yzx"

    # Multiple full groups: each group cycles independently
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # Mixed group sizes: only full groups are cycled
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"
    assert module_0.encode_cyclic("abcdefg") == "bcaefdg"
    assert module_0.encode_cyclic("abcdegh") == "bcadegh" if False else module_0.encode_cyclic("abcdeh") == "bcadeh"

    # Repeated characters
    assert module_0.encode_cyclic("aaa") == "aaa"
    assert module_0.encode_cyclic("aaaaaa") == "aaaaaa"
    assert module_0.encode_cyclic("aaabbb") == "aaabbb".replace("aaabbb", "aaabbb")  # "aab"+"abb" cycled
    assert module_0.encode_cyclic("aaabbb") == "aababb"

    # decode_cyclic should invert encode_cyclic
    for s in ["", "a", "ab", "abc", "abcd", "abcdefgh", "hello world", "xyzzy"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # encode is an involution composition: decode(encode(s)) == s
    assert decode_cyclic(module_0.encode_cyclic("qwerty")) == "qwerty"

    # encode of decode also round-trips
    for s in ["roundtrip", "test123", "a!b@c#"]:
        assert module_0.encode_cyclic(decode_cyclic(s)) == s


test_encode_cyclic()

# Generated at 2026-11-02 12:16:35.703054
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # Decoding an encoded string should return the original string
    for s in ["", "a", "ab", "abc", "abcd", "abcdef", "abcdefg",
              "abcdefghi", "xyz", "hello world", "The quick brown fox"]:
        assert module_0.decode_cyclic(encode_cyclic(s)) == s

    # Known-value checks: each group of 3 was rotated left once by encode,
    # so decoding rotates right (via double encode)
    assert module_0.decode_cyclic("bca") == "abc"
    assert module_0.decode_cyclic("bcaefd") == "abcdef"
    assert module_0.decode_cyclic("bcaefdihg") == "abcdefghi"

    # Strings with trailing partial groups leave those groups unchanged
    assert module_0.decode_cyclic("bcaXY") == "abcXY"

    # Round-trip both ways
    for s in ["abcdef", "cyclicrotation", "ab", "a"]:
        assert module_0.decode_cyclic(encode_cyclic(s)) == s

# Generated at 2026-11-02 12:18:03.062137
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Test with string length divisible by 3
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcdefg") == "bcaefd" + "g"

    # Test with string length not divisible by 3 (last group unchanged)
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Test empty string
    assert module_0.encode_cyclic("") == ""

    # Test single character
    assert module_0.encode_cyclic("a") == "a"

    # Test two characters
    assert module_0.encode_cyclic("ab") == "ab"

    # Test round trip: decode_cyclic(module_0.encode_cyclic(s)) == s
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "hello world", "x" * 10]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s
        assert decode_cyclic(s) == module_0.encode_cyclic(s)

    # Test with repeated characters
    assert module_0.encode_cyclic("aaa") == "aaa"
    assert module_0.encode_cyclic("aaabbb") == "aaabbb"

    # Test with special characters
    assert module_0.encode_cyclic("a b!") == " b!a"

    print("All tests passed!")


test_encode_cyclic()