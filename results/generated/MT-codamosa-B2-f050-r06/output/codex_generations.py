

# Generated at 2026-11-02 14:30:21.409115
# Unit test for function encode_shift
def test_encode_shift():
    # Basic shift of 5 letters forward
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("hello") == "mjqqt"
    # Wrap-around: letters near end of alphabet
    assert module_0.encode_shift("vwxyz") == "abcde"
    # Empty string
    assert module_0.encode_shift("") == ""
    # Single characters
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("z") == "e"
    # Repeated characters
    assert module_0.encode_shift("aaaa") == "ffff"
    # decode_shift must reverse encode_shift
    for s in ["", "a", "hello", "abcdefghijklmnopqrstuvwxyz", "xyzabc"]:
        assert decode_shift(module_0.encode_shift(s)) == s
        assert module_0.encode_shift(decode_shift(s)) == s

# Generated at 2026-11-02 14:33:15.640075
# Unit test for function decode_shift
def test_decode_shift():import unittest


class TestDecodeShift(unittest.TestCase):

    def test_roundtrip(self):
        # decode(encode(s)) == s for various strings
        for s in ["hello", "world", "python", "abcdefghijklmnopqrstuvwxyz"]:
            from __main__ import encode_shift
            self.assertEqual(module_0.decode_shift(encode_shift(s)), s)

    def test_basic_shift(self):
        self.assertEqual(module_0.decode_shift("f"), "a")
        self.assertEqual(module_0.decode_shift("g"), "b")
        self.assertEqual(module_0.decode_shift("mjqqt"), "hello")

    def test_wraparound(self):
        # 'a' shifted back 5 wraps to 'v'
        self.assertEqual(module_0.decode_shift("a"), "v")
        self.assertEqual(module_0.decode_shift("e"), "z")
        self.assertEqual(module_0.decode_shift("abc"), "vwx")

    def test_empty_string(self):
        self.assertEqual(module_0.decode_shift(""), "")

    def test_full_alphabet(self):
        self.assertEqual(
            module_0.decode_shift("fghijklmnopqrstuvwxyzabcde"),
            "abcdefghijklmnopqrstuvwxyz"
        )


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 14:35:32.252519
# Unit test for function encode_shift
def test_encode_shift():import unittest


class TestEncodeShift(unittest.TestCase):
    def test_basic_shift(self):
        self.assertEqual(module_0.encode_shift("abc"), "fgh")

    def test_wraparound(self):
        self.assertEqual(module_0.encode_shift("vwxyz"), "abcdef")

    def test_hello(self):
        self.assertEqual(module_0.encode_shift("hello"), "mjqqt")

    def test_empty_string(self):
        self.assertEqual(module_0.encode_shift(""), "")

    def test_decode_reverses_encode(self):
        self.assertEqual(decode_shift(module_0.encode_shift("hello")), "hello")

    def test_roundtrip_random(self):
        original = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(decode_shift(module_0.encode_shift(original)), original)


if __name__ == "__main__":
    unittest.main()