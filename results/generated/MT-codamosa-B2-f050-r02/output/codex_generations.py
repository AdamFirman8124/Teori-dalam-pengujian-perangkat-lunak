

# Generated at 2026-11-03 05:08:41.138620
# Unit test for function decode_shift
def test_decode_shift():
    # Decodes a known encoded string
    assert module_0.decode_shift("mjqqt") == "hello"

    # Individual letter shifts (back by 5, wrapping around)
    assert module_0.decode_shift("f") == "a"
    assert module_0.decode_shift("e") == "z"
    assert module_0.decode_shift("a") == "v"
    assert module_0.decode_shift("z") == "u"

    # Empty string stays empty
    assert module_0.decode_shift("") == ""

    # Round-trip: decode(encode(s)) == s
    for s in ["abc", "xyz", "python", "testcase", "abcdefghijklmnopqrstuvwxyz"]:
        assert module_0.decode_shift(encode_shift(s)) == s

    # Decoding twice shifts letters back by 10 total
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift(module_0.decode_shift("hello")) == "xubbe"

# Generated at 2026-11-03 05:11:38.943290
# Unit test for function decode_shift
def test_decode_shift():
    # Decoding a simple string
    assert module_0.decode_shift("fgh") == "abc"
    assert module_0.decode_shift("f") == "a"

    # Wraparound: 'a' shifted back by 5 wraps to 'v'
    assert module_0.decode_shift("a") == "v"
    assert module_0.decode_shift("e") == "z"
    assert module_0.decode_shift("abc") == "vwx"

    # Empty string
    assert module_0.decode_shift("") == ""

    # Round-trip: decode(encode(x)) == x
    for original in ["hello", "world", "xyz", "abcdefghijklmnopqrstuvwxyz"]:
        encoded = "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in original])
        assert module_0.decode_shift(encoded) == original

    # Full alphabet round-trip
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    assert module_0.decode_shift(encode_shift(alphabet)) == alphabet

    print("test_decode_shift passed")


test_decode_shift()

# Generated at 2026-11-03 05:14:28.867869
# Unit test for function encode_shift
def test_encode_shift():
    # Basic forward shift by 5
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("b") == "g"
    assert module_0.encode_shift("m") == "r"
    assert module_0.encode_shift("z") == "e"

    # Wraparound cases
    assert module_0.encode_shift("v") == "a"
    assert module_0.encode_shift("w") == "b"
    assert module_0.encode_shift("x") == "c"
    assert module_0.encode_shift("y") == "d"

    # Multiple characters
    assert module_0.encode_shift("hello") == "mjqqt"
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("python") == "udymts"

    # Empty string
    assert module_0.encode_shift("") == ""

    # Full alphabet
    assert module_0.encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"

    # Round-trip with decode_shift
    assert decode_shift(module_0.encode_shift("testingroundtrip")) == "testingroundtrip"
    assert decode_shift(module_0.encode_shift("xyz")) == "xyz"
    assert decode_shift(module_0.encode_shift("wraparoundvectors")) == "wraparoundvectors"

    print("All encode_shift tests passed!")


test_encode_shift()