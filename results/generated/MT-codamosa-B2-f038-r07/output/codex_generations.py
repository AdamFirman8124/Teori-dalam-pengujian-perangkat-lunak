

# Generated at 2026-11-02 17:52:21.785777
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Groups of exactly 3 characters are cycled (first char moved to end)
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcdef") == "bcaefd"
    assert module_0.encode_cyclic("abcdefghi") == "bcaefdhig"

    # Trailing group with fewer than 3 characters is left unchanged
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Strings shorter than 3 characters are unchanged
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Encoding three times restores the original string
    for s in ["", "a", "ab", "abc", "abcd", "abcdef", "hello world"]:
        assert module_0.encode_cyclic(module_0.encode_cyclic(module_0.encode_cyclic(s))) == s

    # Decoding an encoded string restores the original
    for s in ["", "a", "ab", "abc", "abcd", "abcdef", "hello world"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # Property-based check with random strings
    import random
    import string
    random.seed(42)
    for _ in range(100):
        length = random.randint(0, 50)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

# Generated at 2026-11-02 17:53:17.081947
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Empty string
    assert module_0.encode_cyclic("") == ""

    # Strings shorter than 3 are unchanged
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Exactly one full group: cycle the 3 characters
    assert module_0.encode_cyclic("abc") == "bca"

    # Two full groups: each group cycles independently
    assert module_0.encode_cyclic("abcdef") == "bcaefd"

    # Full group followed by a partial group (partial group unchanged)
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Three full groups plus partial
    assert module_0.encode_cyclic("abcdefgh") == "bcaefdgh"

    # Encoding twice returns the original string (basis of decode_cyclic)
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "hello world", "xyzxyz"]:
        assert module_0.encode_cyclic(module_0.encode_cyclic(s)) == s

    # Round-trip property via decode_cyclic
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefghi", "The quick brown fox"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # Output must be a permutation of the input (same characters)
    s = "abcdefgh"
    assert sorted(module_0.encode_cyclic(s)) == sorted(s)

    # Length is preserved
    assert len(module_0.encode_cyclic("ab")) == len("ab")
    assert len(module_0.encode_cyclic("abcdefg")) == len("abcdefg")

# Generated at 2026-11-02 17:54:47.951856
# Unit test for function encode_cyclic
def test_encode_cyclic():
    # Empty string
    assert module_0.encode_cyclic("") == ""

    # Strings shorter than 3 remain unchanged
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"

    # Single full group: first element moves to end
    assert module_0.encode_cyclic("abc") == "bca"

    # Full group + partial group (partial group unchanged)
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcade"

    # Two full groups
    assert module_0.encode_cyclic("abcdef") == "bcaefd"

    # Multiple groups with trailing partial group
    assert module_0.encode_cyclic("abcdefgh") == "bcaefdhg"[:3] + "efdhg"[0:3] if False else module_0.encode_cyclic("abcdefgh") == "bcaefdhg"
    assert module_0.encode_cyclic("alphabet") == "lphaalpbet"

    # Roundtrip: encoding three times returns original
    for s in ["", "a", "ab", "abc", "abcd", "hello", "world!!"]:
        assert decode_cyclic(module_0.encode_cyclic(s)) == s

    # decode_cyclic inverts encode_cyclic for full groups
    assert decode_cyclic("bcaefd") == "abcdef"

# Generated at 2026-11-02 17:56:31.383078
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # decode_cyclic should invert encode_cyclic for strings of various lengths
    test_strings = [
        "",               # empty string
        "a",              # group shorter than 3 (unchanged by cycling)
        "ab",             # partial group
        "abc",            # exactly one full group
        "abcdef",         # two full groups
        "abcdefgh",       # full groups + partial group
        "hello world",    # longer string with spaces
        "xyz123!@#",      # mixed characters
    ]
    for s in test_strings:
        assert module_0.decode_cyclic(encode_cyclic(s)) == s, f"Failed round-trip for input: {s!r}"

    # Direct decode checks (decode applies encode twice):
    # encode("abc") == "bca", so decoding "bca" must return "abc"
    assert module_0.decode_cyclic("bca") == "abc"
    # encode("abcd") == "bcad", so decoding "bcad" must return "abcd"
    assert module_0.decode_cyclic("bcad") == "abcd"
    # Strings with no full groups pass through unchanged
    assert module_0.decode_cyclic("ab") == "ab"
    assert module_0.decode_cyclic("") == ""


test_decode_cyclic()

# Generated at 2026-11-02 17:57:38.338241
# Unit test for function decode_cyclic
def test_decode_cyclic():
    # Empty string
    assert module_0.decode_cyclic("") == ""

    # Strings shorter than 3: no complete group, unchanged
    assert module_0.decode_cyclic("a") == "a"
    assert module_0.decode_cyclic("ab") == "ab"

    # Single complete group: two left-cycles equal one right-cycle
    assert module_0.decode_cyclic("abc") == "cab"
    assert module_0.decode_cyclic("aaa") == "aaa"

    # Multiple complete groups
    assert module_0.decode_cyclic("abcdefghi") == "cabfdeigh"

    # Trailing incomplete group (length 1 and 2) is left untouched
    assert module_0.decode_cyclic("abcd") == "cabd"
    assert module_0.decode_cyclic("abcde") == "cabde"
    assert module_0.decode_cyclic("abcdefg") == "cabfdeg"

    # Repeated characters
    assert module_0.decode_cyclic("aaabbbccc") == "aaabbbccc"

    # Roundtrip property: decode(encode(s)) == s
    for s in ["", "a", "ab", "abc", "abcd", "hello world",
              "The quick brown fox", "xyz" * 7, "ab" * 5 + "c"]:
        assert module_0.decode_cyclic(encode_cyclic(s)) == s