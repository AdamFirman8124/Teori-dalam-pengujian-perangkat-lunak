

# Generated at 2026-11-02 23:04:49.195181
# Unit test for function encode_shift
def test_encode_shift():
    # Basic shift forward by 5
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("hello") == "mjqqt"

    # Wrap-around cases
    assert module_0.encode_shift("xyz") == "cde"
    assert module_0.encode_shift("vwxyz") == "abcde"

    # Edge cases
    assert module_0.encode_shift("") == ""
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("z") == "e"

    # Round-trip property with decode_shift
    for s in ["", "a", "abc", "hello", "xyz", "abcdefghijklmnopqrstuvwxyz"]:
        assert decode_shift(module_0.encode_shift(s)) == s


def test_decode_shift():
    # Basic shift backward by 5
    assert decode_shift("fgh") == "abc"
    assert decode_shift("mjqqt") == "hello"

    # Wrap-around cases
    assert decode_shift("cde") == "xyz"
    assert decode_shift("abcde") == "vwxyz"

    # Edge cases
    assert decode_shift("") == ""
    assert decode_shift("a") == "v"
    assert decode_shift("e") == "z"

    # Round-trip property with encode_shift
    for s in ["", "a", "abc", "hello", "xyz", "abcdefghijklmnopqrstuvwxyz"]:
        assert module_0.encode_shift(decode_shift(s)) == s

# Generated at 2026-11-02 23:06:53.206661
# Unit test for function encode_shift
def test_encode_shift():
    # Basic shift: each letter moves forward by 5
    assert module_0.encode_shift("a") == "f"
    assert module_0.encode_shift("b") == "g"
    assert module_0.encode_shift("hello") == "mjqqt"

    # Wrap-around behavior at end of alphabet
    assert module_0.encode_shift("v") == "a"
    assert module_0.encode_shift("w") == "b"
    assert module_0.encode_shift("z") == "e"
    assert module_0.encode_shift("xyz") == "cde"

    # Empty string
    assert module_0.encode_shift("") == ""

    # Full alphabet
    assert module_0.encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"

    # Round-trip: decode_shift(module_0.encode_shift(s)) == s
    for s in ["hello", "world", "python", "abcdefghijklmnopqrstuvwxyz", ""]:
        assert decode_shift(module_0.encode_shift(s)) == s

    # module_0.encode_shift(decode_shift(s)) == s
    for s in ["mjqqt", "fghij", "abc"]:
        assert module_0.encode_shift(decode_shift(s)) == s

    print("All encode_shift tests passed!")


test_encode_shift()

# Generated at 2026-11-02 23:09:54.510588
# Unit test for function encode_shift
def test_encode_shift():
    # Empty string
    assert module_0.encode_shift("") == ""

    # Basic lowercase shift by 5
    assert module_0.encode_shift("abc") == "fgh"
    assert module_0.encode_shift("hello") == "mjqqt"

    # Wrap-around cases
    assert module_0.encode_shift("v") == "a"
    assert module_0.encode_shift("w") == "b"
    assert module_0.encode_shift("x") == "c"
    assert module_0.encode_shift("y") == "d"
    assert module_0.encode_shift("z") == "e"

    # Full alphabet wraps correctly
    assert module_0.encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"

    # Repeated letters
    assert module_0.encode_shift("aaa") == "fff"
    assert module_0.encode_shift("zzz") == "eee"

    # Round-trip with decode_shift
    for s in ["", "a", "hello", "world", "abcdefghijklmnopqrstuvwxyz"]:
        assert decode_shift(module_0.encode_shift(s)) == s


# Unit test for function decode_shift
def test_decode_shift():
    # Empty string
    assert decode_shift("") == ""

    # Basic lowercase shift back by 5
    assert decode_shift("fgh") == "abc"
    assert decode_shift("mjqqt") == "hello"

    # Wrap-around cases
    assert decode_shift("a") == "v"
    assert decode_shift("b") == "w"
    assert decode_shift("c") == "x"
    assert decode_shift("d") == "y"
    assert decode_shift("e") == "z"

    # Full alphabet wraps correctly
    assert decode_shift("fghijklmnopqrstuvwxyzabcde") == "abcdefghijklmnopqrstuvwxyz"

    # Repeated letters
    assert decode_shift("fff") == "aaa"
    assert decode_shift("eee") == "zzz"

    # Round-trip with encode_shift
    for s in ["", "a", "python", "xyz", "abcdefghijklmnopqrstuvwxyz"]:
        assert module_0.encode_shift(decode_shift(s)) == s


if __name__ == "__main__":
    test_encode_shift()
    test_decode_shift()
    print("All tests passed!")

# Generated at 2026-11-02 23:12:10.133598
# Unit test for function encode_shift
def test_encode_shift():import unittest


def module_0.encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


class TestEncodeShift(unittest.TestCase):

    def test_single_letter(self):
        self.assertEqual(module_0.encode_shift("a"), "f")

    def test_simple_word(self):
        self.assertEqual(module_0.encode_shift("hello"), "mjqqt")

    def test_wraparound(self):
        self.assertEqual(module_0.encode_shift("xyz"), "cde")
        self.assertEqual(module_0.encode_shift("vw"), "ab")

    def test_empty_string(self):
        self.assertEqual(module_0.encode_shift(""), "")

    def test_full_alphabet(self):
        self.assertEqual(module_0.encode_shift("abcdefghijklmnopqrstuvwxyz"), "fghijklmnopqrstuvwxyzabcde")

    def test_decode_inverts_encode(self):
        original = "pythonunittests"
        self.assertEqual(decode_shift(module_0.encode_shift(original)), original)

    def test_decode_known_values(self):
        self.assertEqual(decode_shift("mjqqt"), "hello")
        self.assertEqual(decode_shift("f"), "a")


if __name__ == "__main__":
    unittest.main()