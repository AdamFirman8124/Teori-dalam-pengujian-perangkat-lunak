

# Generated at 2026-11-02 07:58:41.319326
# Unit test for function encode_shift
def test_encode_shift():
    # Basic shift of lowercase letters by 5 positions
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("hello") == "mjqqt"

    # Wrap-around behavior at end of alphabet
    assert module_0.encode_shift("z") == "e"
    assert module_0.encode_shift("vwxyz") == "abcde"

    # Empty string
    assert module_0.encode_shift("") == ""

    # Single character
    assert module_0.encode_shift("a") == "f"

    # decode_shift inverts encode_shift
    assert decode_shift(module_0.encode_shift("roundtrip")) == "roundtrip"
    assert decode_shift(module_0.encode_shift("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"

# Generated at 2026-11-02 07:59:28.377886
# Unit test for function decode_shift
def test_decode_shift():
    # Roundtrip: decoding an encoded string returns the original
    assert module_0.decode_shift(encode_shift("hello")) == "hello"
    assert module_0.decode_shift(encode_shift("python")) == "python"
    assert module_0.decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"

    # Known values
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift("v") == "a"      # wraparound: 'a' shifted back 5
    assert module_0.decode_shift("a") == "v"      # wraparound: 'v' shifted back 5
    assert module_0.decode_shift("f") == "a"      # no wraparound
    assert module_0.decode_shift("e") == "z"      # wraparound boundary

    # Edge cases
    assert module_0.decode_shift("") == ""
    assert module_0.decode_shift("z") == "u"
    assert module_0.decode_shift("uvwxy") == "pqrs"

    # Property: decode_shift is the inverse of encode_shift
    for ch in "abcdefghijklmnopqrstuvwxyz":
        assert module_0.decode_shift(encode_shift(ch)) == ch
        assert encode_shift(module_0.decode_shift(ch)) == ch

    # Verify shift amount is 5
    for ch in "abcdefghijklmnopqrstuvwxyz":
        expected = chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a"))
        assert module_0.decode_shift(ch) == expected


test_decode_shift()
print("All tests passed!")

# Generated at 2026-11-02 08:00:13.728493
# Unit test for function encode_shift
def test_encode_shift():import unittest


def module_0.encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


class TestEncodeShift(unittest.TestCase):

    def test_basic_shift(self):
        self.assertEqual(module_0.encode_shift("abc"), "fgh")

    def test_single_character(self):
        self.assertEqual(module_0.encode_shift("a"), "f")
        self.assertEqual(module_0.encode_shift("z"), "e")

    def test_wraparound(self):
        # 'v' + 5 wraps past 'z' back to 'a'
        self.assertEqual(module_0.encode_shift("vwxyz"), "abcde")

    def test_empty_string(self):
        self.assertEqual(module_0.encode_shift(""), "")

    def test_full_alphabet(self):
        self.assertEqual(module_0.encode_shift("abcdefghijklmnopqrstuvwxyz"), "fghijklmnopqrstuvwxyzabcde")

    def test_roundtrip(self):
        for s in ["hello", "world", "python", "xyz", "aaa", "zzz"]:
            self.assertEqual(decode_shift(module_0.encode_shift(s)), s)

    def test_decode_basic(self):
        self.assertEqual(decode_shift("fgh"), "abc")

    def test_decode_wraparound(self):
        self.assertEqual(decode_shift("abcde"), "vwxyz")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 08:01:29.048912
# Unit test for function encode_shift
def test_encode_shift():
    # Test basic forward shift by 5
    assert module_0.encode_shift("abc") == "fgh"
    
    # Test wraparound (letters near end of alphabet)
    assert module_0.encode_shift("vwxyz") == "abcde"
    
    # Test empty string
    assert module_0.encode_shift("") == ""
    
    # Test single characters
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("z") == "e"
    
    # Test a common word
    assert module_0.encode_shift("hello") == "mjqqt"
    
    # Test encode then decode round-trip returns original
    original = "helloworld"
    assert decode_shift(module_0.encode_shift(original)) == original
    
    # Test string with repeated characters
    assert module_0.encode_shift("aaa") == "fff"
    
    # Test full alphabet
    assert module_0.encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"
    
    print("test_encode_shift passed!")


test_encode_shift()

# Generated at 2026-11-02 08:01:51.076996
# Unit test for function decode_shift
def test_decode_shift():
    # Decoding should reverse encoding
    original = "hello"
    assert module_0.decode_shift(encode_shift(original)) == original

    original = "abcdefghijklmnopqrstuvwxyz"
    assert module_0.decode_shift(encode_shift(original)) == original

    # Known value: 'f' shifted back by 5 is 'a'
    assert module_0.decode_shift("f") == "a"

    # Wrap-around: 'a' shifted back by 5 wraps to 'v'
    assert module_0.decode_shift("a") == "v"
    assert module_0.decode_shift("e") == "z"

    # Full alphabet round trip
    assert module_0.decode_shift("mjqqt") == "hello"

    # Empty string
    assert module_0.decode_shift("") == ""

    # Decoding an encoded string letter by letter
    encoded = encode_shift("xyz")
    assert module_0.decode_shift(encoded) == "xyz"