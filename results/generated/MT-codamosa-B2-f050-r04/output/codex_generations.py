

# Generated at 2026-11-02 17:22:12.836784
# Unit test for function encode_shift
def test_encode_shift():
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("b") == "g"
    assert module_0.encode_shift("z") == "e"
    assert module_0.encode_shift("xyz") == "cde"
    assert module_0.encode_shift("hello") == "mjqqt"
    assert module_0.encode_shift("") == ""
    assert module_0.encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"
    # Round-trip property: decoding an encoded string returns the original
    for s in ["", "a", "hello", "xyz", "shiftthisstring"]:
        assert decode_shift(module_0.encode_shift(s)) == s

# Generated at 2026-11-02 17:23:44.813118
# Unit test for function decode_shift
def test_decode_shift():
    # Basic known-value cases: encode shifts forward by 5, decode shifts back by 5
    assert module_0.decode_shift("f") == "a"
    assert module_0.decode_shift("m") == "h"
    assert module_0.decode_shift("a") == "v"
    
    # Wraparound case: 'e' is index 4, 4 - 5 wraps to 25 -> 'z'
    assert module_0.decode_shift("e") == "z"
    assert module_0.decode_shift("d") == "y"
    
    # Empty string
    assert module_0.decode_shift("") == ""
    
    # Decoding an encoded string returns the original
    assert module_0.decode_shift(encode_shift("hello")) == "hello"
    assert module_0.decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"
    assert module_0.decode_shift(encode_shift("")) == ""
    
    # Round-trip property on random-ish inputs
    for original in ["python", "xyz", "test", "zzzzz", "aaaaa"]:
        assert module_0.decode_shift(encode_shift(original)) == original
    
    # Direct decode of known encoded values
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift("twenzym") == "python"

# Generated at 2026-11-02 17:26:08.411993
# Unit test for function decode_shift
def test_decode_shift():
    # Round-trip: decode(encode(x)) == x
    assert module_0.decode_shift(encode_shift("hello")) == "hello"
    assert module_0.decode_shift(encode_shift("worldxyz")) == "worldxyz"

    # Known values
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift("f") == "a"

    # Wrap-around behavior
    assert module_0.decode_shift("a") == "v"
    assert module_0.decode_shift("b") == "w"
    assert module_0.decode_shift("fghij") == "abcde"

    # Empty string
    assert module_0.decode_shift("") == ""

    # Full alphabet round-trip
    import string
    alphabet = string.ascii_lowercase
    assert module_0.decode_shift(encode_shift(alphabet)) == alphabet

# Generated at 2026-11-02 17:27:54.077173
# Unit test for function encode_shift
def test_encode_shift():
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("hello") == "mjqqt"
    assert module_0.encode_shift("xyz") == "cde"  # wrap-around
    assert module_0.encode_shift("") == ""
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("z") == "e"  # wrap-around
    # round trip: decode(encode(s)) == s
    for s in ["abc", "hello", "world", "xyz", "quickbrownfox"]:
        assert decode_shift(module_0.encode_shift(s)) == s
    # decode_shift correctness
    assert decode_shift("fgh") == "abc"
    assert decode_shift("mjqqt") == "hello"
    assert decode_shift("cde") == "xyz"  # wrap-around
    assert decode_shift("") == ""

# Generated at 2026-11-02 17:29:13.060159
# Unit test for function encode_shift
def test_encode_shift():
    # Basic shift: each letter moves forward by 5
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("hello") == "mjqqt"
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("xyz") == "cde"  # wrap-around: x->c, y->d, z->e
    assert module_0.encode_shift("vwxyz") == "abcde"
    assert module_0.encode_shift("") == ""
    assert module_0.encode_shift("python") == "udymts"
    # Round-trip: decoding an encoded string returns the original
    assert decode_shift(module_0.encode_shift("hello")) == "hello"
    assert decode_shift(module_0.encode_shift("xyz")) == "xyz"