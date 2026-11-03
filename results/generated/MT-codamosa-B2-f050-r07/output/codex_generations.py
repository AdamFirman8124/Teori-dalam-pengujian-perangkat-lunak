

# Generated at 2026-11-02 16:48:19.580475
# Unit test for function decode_shift
def test_decode_shift():
    # nonce:83ec3f60
    # Basic decoding (shift back by 5)
    assert module_0.decode_shift("f") == "a"
    assert module_0.decode_shift("g") == "b"

    # Wrap-around cases (mod 26)
    assert module_0.decode_shift("a") == "v"
    assert module_0.decode_shift("e") == "z"

    # Multi-character strings
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift("ymjxjhwjy") == "thesecret"

    # Empty string
    assert module_0.decode_shift("") == ""

    # Round-trip: decode_shift inverts encode_shift
    for s in ["", "a", "hello", "xyz", "abcdefghijklmnopqrstuvwxyz"]:
        assert module_0.decode_shift(encode_shift(s)) == s

    # Full alphabet decode check
    assert module_0.decode_shift("fghijklmnopqrstuvwxyzabcde") == "abcdefghijklmnopqrstuvwxyz"


test_decode_shift()

# Generated at 2026-11-02 16:51:16.490557
# Unit test for function encode_shift
def test_encode_shift():
    # Basic shift: each letter shifts forward by 5
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("b") == "g"
    assert module_0.encode_shift("z") == "e"  # wraps around

    # Multi-character strings
    assert module_0.encode_shift("hello") == "mjqqt"
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("xyz") == "cde"  # wrap-around across alphabet

    # Empty string
    assert module_0.encode_shift("") == ""

    # Round-trip with decode_shift
    for s in ["hello", "world", "python", "abcdefghijklmnopqrstuvwxyz"]:
        assert decode_shift(module_0.encode_shift(s)) == s

    # Verify every letter maps correctly
    for ch in "abcdefghijklmnopqrstuvwxyz":
        expected = chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a"))
        assert module_0.encode_shift(ch) == expected

# Generated at 2026-11-02 16:53:30.276583
# Unit test for function encode_shift
def test_encode_shift():
    # Basic shift of 5 letters forward
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("b") == "g"
    assert module_0.encode_shift("hello") == "mjqqt"

    # Wrap-around from end of alphabet
    assert module_0.encode_shift("z") == "e"
    assert module_0.encode_shift("xyz") == "cde"

    # Empty string
    assert module_0.encode_shift("") == ""

    # Shift is reversible with decode_shift
    for s in ["abc", "test", "python", "zzz", "aquickbrownfox"]:
        assert decode_shift(module_0.encode_shift(s)) == s

    # Single characters across the alphabet
    assert module_0.encode_shift("u") == "z"
    assert module_0.encode_shift("v") == "a"

    print("All tests passed!")


test_encode_shift()

# Generated at 2026-11-02 16:54:34.956323
# Unit test for function decode_shift
def test_decode_shift():
    # Basic decoding: each character shifts back by 5 positions
    assert module_0.decode_shift("f") == "a"
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift("u") == "p"

    # Wrap-around cases (cyclic behavior of modulo 26)
    assert module_0.decode_shift("e") == "z"
    assert module_0.decode_shift("d") == "y"
    assert module_0.decode_shift("j") == "e"

    # Empty string
    assert module_0.decode_shift("") == ""

    # Round-trip: module_0.decode_shift(encode_shift(s)) == s
    for s in ["a", "abc", "hello", "xyz", "python", "abcdefghijklmnopqrstuvwxyz"]:
        assert module_0.decode_shift(encode_shift(s)) == s

    # Known encode/decode pair
    assert module_0.decode_shift(encode_shift("test")) == "test"
    assert module_0.decode_shift("ymjxvznwwjq") == "test"

    # All letters decode correctly
    encoded_alphabet = encode_shift("abcdefghijklmnopqrstuvwxyz")
    assert module_0.decode_shift(encoded_alphabet) == "abcdefghijklmnopqrstuvwxyz"

    print("All tests passed!")

# Generated at 2026-11-02 16:55:59.012728
# Unit test for function decode_shift
def test_decode_shift():
    # Decoding a known encoded string
    assert module_0.decode_shift(encode_shift("hello")) == "hello"
    assert module_0.decode_shift(encode_shift("world")) == "world"

    # Direct known values: decode_shift shifts each letter back by 5
    assert module_0.decode_shift("f") == "a"
    assert module_0.decode_shift("a") == "v"
    assert module_0.decode_shift("e") == "z"
    assert module_0.decode_shift("mjqqt") == "hello"

    # Wrap-around behavior
    assert module_0.decode_shift("v") == "q"
    assert module_0.decode_shift("z") == "u"

    # Empty string
    assert module_0.decode_shift("") == ""

    # Round-trip property over all lowercase letters
    for ch in string.ascii_lowercase:
        assert module_0.decode_shift(encode_shift(ch)) == ch

    # Round-trip on a longer mixed string
    original = "thequickbrownfoxjumpsoverthelazydog"
    assert module_0.decode_shift(encode_shift(original)) == original

    # Decoding is the inverse of encoding for every letter
    for ch in string.ascii_lowercase:
        encoded = encode_shift(ch)
        assert module_0.decode_shift(encoded) == ch