

# Generated at 2026-11-02 19:54:42.154857
# Unit test for function flip_case
def test_flip_case():
    # Mixed case string
    assert module_0.flip_case("Hello") == "hELLO"
    # All lowercase
    assert module_0.flip_case("hello") == "HELLO"
    # All uppercase
    assert module_0.flip_case("WORLD") == "world"
    # Empty string
    assert module_0.flip_case("") == ""
    # String with digits and symbols (unchanged)
    assert module_0.flip_case("PyThOn3.8!") == "pYtHoN3.8!"
    # Single character lowercase
    assert module_0.flip_case("a") == "A"
    # Single character uppercase
    assert module_0.flip_case("Z") == "z"
    # String with spaces
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    # Double flip returns original
    s = "MiXeD Case 123"
    assert module_0.flip_case(module_0.flip_case(s)) == s
    print("All tests passed!")


if __name__ == "__main__":
    test_flip_case()

# Generated at 2026-11-02 19:56:58.265923
# Unit test for function flip_case
def test_flip_case():
# nonce:9fd990d0
    # Test mixed case string
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    
    # Test all lowercase
    assert module_0.flip_case("hello") == "HELLO"
    
    # Test all uppercase
    assert module_0.flip_case("WORLD") == "world"
    
    # Test empty string
    assert module_0.flip_case("") == ""
    
    # Test single character lowercase
    assert module_0.flip_case("a") == "A"
    
    # Test single character uppercase
    assert module_0.flip_case("A") == "a"
    
    # Test string with numbers and special characters
    assert module_0.flip_case("PyThOn 123!@#") == "pYtHoN 123!@#"
    
    # Test string with spaces only
    assert module_0.flip_case("   ") == "   "
    
    # Test string with mixed alphanumeric
    assert module_0.flip_case("abc123XYZ") == "ABC123xyz"
    
    # Test double flip returns original
    original = "MiXeD CaSe StRiNg"
    assert module_0.flip_case(module_0.flip_case(original)) == original
    
    print("All tests passed!")


if __name__ == "__main__":
    test_flip_case()

# Generated at 2026-11-02 19:58:17.026412
# Unit test for function flip_case
def test_flip_case():
    # Test basic mixed-case string
    assert module_0.flip_case('Hello') == 'hELLO'
    
    # Test all lowercase
    assert module_0.flip_case('hello') == 'HELLO'
    
    # Test all uppercase
    assert module_0.flip_case('WORLD') == 'world'
    
    # Test empty string
    assert module_0.flip_case('') == ''
    
    # Test string with no letters
    assert module_0.flip_case('123!@#') == '123!@#'
    
    # Test single character lowercase
    assert module_0.flip_case('a') == 'A'
    
    # Test single character uppercase
    assert module_0.flip_case('A') == 'a'
    
    # Test string with spaces and punctuation
    assert module_0.flip_case('Hello, World! 123') == 'hELLO, wORLD! 123'
    
    # Test double flip returns original
    original = 'PyThOn 3.12'
    assert module_0.flip_case(module_0.flip_case(original)) == original
    
    # Test mixed alphanumeric
    assert module_0.flip_case('aBc123XyZ') == 'AbC123xYz'
    
    print("All test_flip_case tests passed!")


if __name__ == "__main__":
    test_flip_case()

# Generated at 2026-11-02 20:00:09.124199
# Unit test for function flip_case
def test_flip_case():
    assert module_0.flip_case("hello") == "HELLO"
    assert module_0.flip_case("HELLO") == "hello"
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    assert module_0.flip_case("") == ""
    assert module_0.flip_case("123!@#") == "123!@#"
    assert module_0.flip_case("aBcDe") == "AbCdE"
    assert module_0.flip_case("PyThOn") == "pYtHoN"
    print("All tests passed!")

# Generated at 2026-11-02 20:02:32.237861
# Unit test for function flip_case
def test_flip_case():import unittest


def module_0.flip_case(string: str) -> str:
    return string.swapcase()


class TestFlipCase(unittest.TestCase):
    def test_basic_lowercase(self):
        self.assertEqual(module_0.flip_case("hello"), "HELLO")

    def test_basic_uppercase(self):
        self.assertEqual(module_0.flip_case("WORLD"), "world")

    def test_mixed_case(self):
        self.assertEqual(module_0.flip_case("Hello World"), "hELLO wORLD")

    def test_empty_string(self):
        self.assertEqual(module_0.flip_case(""), "")

    def test_no_letters(self):
        self.assertEqual(module_0.flip_case("123!@#"), "123!@#")

    def test_single_char(self):
        self.assertEqual(module_0.flip_case("a"), "A")
        self.assertEqual(module_0.flip_case("A"), "a")

    def test_unicode(self):
        self.assertEqual(module_0.flip_case("Ñoño"), "ñOÑO")

    def test_involution(self):
        s = "PyThOn 3.12!"
        self.assertEqual(module_0.flip_case(module_0.flip_case(s)), s)


if __name__ == "__main__":
    unittest.main()