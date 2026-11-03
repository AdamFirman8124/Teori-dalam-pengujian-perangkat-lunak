

# Generated at 2026-11-01 23:28:08.469116
# Unit test for function decode_shift
def test_decode_shift():import unittest


class TestDecodeShift(unittest.TestCase):

    def test_decode_single_letter(self):
        # 'f' was encoded from 'a'
        self.assertEqual(module_0.decode_shift("f"), "a")

    def test_decode_word(self):
        # encode_shift("hello") -> "mjqqt"
        self.assertEqual(module_0.decode_shift("mjqqt"), "hello")

    def test_decode_wraparound(self):
        # 'a' was encoded from 'v' (wraparound at end of alphabet)
        self.assertEqual(module_0.decode_shift("a"), "v")
        # 'b' was encoded from 'w'
        self.assertEqual(module_0.decode_shift("b"), "w")

    def test_decode_empty_string(self):
        self.assertEqual(module_0.decode_shift(""), "")

    def test_decode_full_alphabet(self):
        self.assertEqual(module_0.decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyz")), "abcdefghijklmnopqrstuvwxyz")

    def test_roundtrip_various_strings(self):
        for s in ["abc", "xyz", "python", "zzz", "a", "hello world"]:
            self.assertEqual(module_0.decode_shift(encode_shift(s)), s)

    def test_decode_known_values(self):
        # Each decoded char is 5 positions back in the alphabet (mod 26)
        self.assertEqual(module_0.decode_shift("mjqqt"), "hello")
        self.assertEqual(module_0.decode_shift("btwqi"), "world")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 23:28:17.858246
# Unit test for function decode_shift
def test_decode_shift():
    # Basic decoding: each character shifted back by 5
    assert module_0.decode_shift("f") == "a"
    assert module_0.decode_shift("a") == "v"
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift("btwqi") == "world"

    # Round-trip: decode(encode(s)) == s
    for s in ["abc", "hello", "world", "xyz", "python", "testcase", "zzzzz"]:
        assert module_0.decode_shift(encode_shift(s)) == s

    # Wrap-around behavior
    assert module_0.decode_shift("e") == "z"
    assert module_0.decode_shift("d") == "y"
    assert module_0.decode_shift("fgh") == "abc"

    # Empty string
    assert module_0.decode_shift("") == ""

    # All lowercase letters round-trip
    import string
    all_letters = string.ascii_lowercase
    assert module_0.decode_shift(encode_shift(all_letters)) == all_letters

    assert module_0.decode_shift(encode_shift("mjqqt btwqi")) == "hello world".replace(" ", "")

# Generated at 2026-11-01 23:28:29.825766
# Unit test for function encode_shift
def test_encode_shift():
    # Basic shift of +5 within alphabet bounds
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("hello") == "mjqqt"

    # Wraparound cases (x, y, z wrap to beginning)
    assert module_0.encode_shift("xyz") == "cde"
    assert module_0.encode_shift("vwxyz") == "abcde"

    # Single characters
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("z") == "e"

    # Empty string
    assert module_0.encode_shift("") == ""

    # Round-trip property with decode_shift
    for s in ["apple", "banana", "zebra", "quickbrownfox"]:
        assert decode_shift(module_0.encode_shift(s)) == s

# Generated at 2026-11-01 23:28:45.687121
# Unit test for function decode_shift
def test_decode_shift():
    # Basic known mappings (encode shifts +5, so decode shifts back -5)
    assert module_0.decode_shift("f") == "a"
    assert module_0.decode_shift("a") == "v"  # wrap-around
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift("cde") == "xyz"
    assert module_0.decode_shift("btwqi") == "world"

    # Empty string
    assert module_0.decode_shift("") == ""

    # Full alphabet round-trip through encode_shift
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded = "fghijklmnopqrstuvwxyzabcde"
    assert module_0.decode_shift(encoded) == alphabet

    # Round-trip property: decode(encode(s)) == s for lowercase input
    for s in ["", "a", "z", "abc", "xyz", "hello", alphabet]:
        assert module_0.decode_shift(encode_shift(s)) == s

# Generated at 2026-11-01 23:29:10.325670
# Unit test for function decode_shift
def test_decode_shift():
    # Single characters, including wraparound
    assert module_0.decode_shift("a") == "v"
    assert module_0.decode_shift("e") == "z"
    assert module_0.decode_shift("f") == "a"

    # Common words
    assert module_0.decode_shift("mjqqt") == "hello"
    assert module_0.decode_shift("btwqi") == "world"

    # Full alphabet shift wrap
    assert module_0.decode_shift("fghijklmnopqrstuvwxyzabcde") == "abcdefghijklmnopqrstuvwxyz"

    # Round-trip with encode_shift
    for s in ["", "a", "z", "hello", "python", "abcdefghijklmnopqrstuvwxyz"]:
        assert module_0.decode_shift(encode_shift(s)) == s