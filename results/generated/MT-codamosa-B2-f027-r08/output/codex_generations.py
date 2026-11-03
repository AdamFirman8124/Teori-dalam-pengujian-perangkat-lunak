

# Generated at 2026-11-02 16:33:54.267292
# Unit test for function flip_case
def test_flip_case():
    # Test basic mixed case string
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    
    # Test all lowercase string
    assert module_0.flip_case("python") == "PYTHON"
    
    # Test all uppercase string
    assert module_0.flip_case("PYTHON") == "python"
    
    # Test empty string
    assert module_0.flip_case("") == ""
    
    # Test string with numbers and symbols (unchanged)
    assert module_0.flip_case("abc123!@#") == "ABC123!@#"
    
    # Test single character lowercase
    assert module_0.flip_case("a") == "A"
    
    # Test single character uppercase
    assert module_0.flip_case("A") == "a"
    
    # Test string with mixed alphanumeric
    assert module_0.flip_case("PyThOn3.9") == "pYtHoN3.9"
    
    # Test string with spaces only
    assert module_0.flip_case("   ") == "   "
    
    # Test double flip returns original
    s = "Hello, World!"
    assert module_0.flip_case(module_0.flip_case(s)) == s
    
    # Test unicode characters
    assert module_0.flip_case("Ñoño") == "ñOÑO"
    
    print("All tests passed!")


# Run tests
if __name__ == "__main__":
    test_flip_case()

# Generated at 2026-11-02 16:35:22.320475
# Unit test for function flip_case
def test_flip_case():
    # Mixed case string
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    
    # All lowercase
    assert module_0.flip_case("hello") == "HELLO"
    
    # All uppercase
    assert module_0.flip_case("WORLD") == "world"
    
    # Empty string
    assert module_0.flip_case("") == ""
    
    # String with digits and symbols (unchanged)
    assert module_0.flip_case("PyThOn 123!@#") == "pYtHoN 123!@#"
    
    # Applying twice returns original (involution property)
    s = "MiXeD CaSe StRiNg"
    assert module_0.flip_case(module_0.flip_case(s)) == s
    
    # Single characters
    assert module_0.flip_case("a") == "A"
    assert module_0.flip_case("Z") == "z"
    
    # Whitespace only
    assert module_0.flip_case("   ") == "   "
    
    print("All tests passed!")


test_flip_case()

# Generated at 2026-11-02 16:36:48.423872
# Unit test for function flip_case
def test_flip_case():
    # Basic mixed case
    assert module_0.flip_case('Hello World') == 'hELLO wORLD'
    assert module_0.flip_case('Hello') == 'hELLO'
    
    # All lowercase input
    assert module_0.flip_case('hello') == 'HELLO'
    
    # All uppercase input
    assert module_0.flip_case('WORLD') == 'world'
    
    # Empty string
    assert module_0.flip_case('') == ''
    
    # Single characters
    assert module_0.flip_case('a') == 'A'
    assert module_0.flip_case('A') == 'a'
    
    # Non-alphabetic characters remain unchanged
    assert module_0.flip_case('123!@#') == '123!@#'
    assert module_0.flip_case('a1B2c3') == 'A1b2C3'
    
    # String with spaces and special characters
    assert module_0.flip_case('PyThOn 3.8!') == 'pYtHoN 3.8!'
    
    # Already flipped string returns original
    assert module_0.flip_case(module_0.flip_case('TestCase')) == 'TestCase'

# Generated at 2026-11-02 16:38:17.426876
# Unit test for function flip_case
def test_flip_case():
    # Basic uppercase to lowercase
    assert module_0.flip_case("HELLO") == "hello"
    # Basic lowercase to uppercase
    assert module_0.flip_case("world") == "WORLD"
    # Mixed case
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    # Empty string
    assert module_0.flip_case("") == ""
    # String with digits and punctuation (unchanged)
    assert module_0.flip_case("PyThOn 3.9!") == "pYtHoN 3.9!"
    # Single character
    assert module_0.flip_case("a") == "A"
    assert module_0.flip_case("A") == "a"
    # Involution: flipping twice returns original
    s = "AbCdEf"
    assert module_0.flip_case(module_0.flip_case(s)) == s
    # Unicode letters
    assert module_0.flip_case("ñÑçÇ") == "ÑñÇÇ"

# Generated at 2026-11-02 16:40:21.832218
# Unit test for function flip_case
def test_flip_case():
    # Basic cases
    assert module_0.flip_case("Hello") == "hELLO"
    assert module_0.flip_case("WORLD") == "world"
    assert module_0.flip_case("PyThOn") == "pYtHoN"

    # Mixed with digits and punctuation
    assert module_0.flip_case("Hello, World! 123") == "hELLO, wORLD! 123"

    # Edge cases
    assert module_0.flip_case("") == ""
    assert module_0.flip_case("a") == "A"
    assert module_0.flip_case("A") == "a"
    assert module_0.flip_case("12345") == "12345"
    assert module_0.flip_case("!@#$%") == "!@#$%"

    # Unicode characters
    assert module_0.flip_case("ÑOño") == "ñOÑO"
    assert module_0.flip_case("ÜBER") == "über"

    # Double flip returns original
    for s in ["Hello", "WORLD", "PyThOn 123"]:
        assert module_0.flip_case(module_0.flip_case(s)) == s

    # Whitespace preservation
    assert module_0.flip_case(" a B c ") == " A b C "

    print("All tests passed!")


class TestFlipCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(module_0.flip_case("Hello"), "hELLO")
        self.assertEqual(module_0.flip_case("WORLD"), "world")
        self.assertEqual(module_0.flip_case("PyThOn"), "pYtHoN")

    def test_empty(self):
        self.assertEqual(module_0.flip_case(""), "")

    def test_single_char(self):
        self.assertEqual(module_0.flip_case("a"), "A")
        self.assertEqual(module_0.flip_case("A"), "a")

    def test_non_alpha(self):
        self.assertEqual(module_0.flip_case("123!@#"), "123!@#")

    def test_mixed(self):
        self.assertEqual(module_0.flip_case("Hello, World! 123"), "hELLO, wORLD! 123")

    def test_whitespace(self):
        self.assertEqual(module_0.flip_case(" a B c "), " A b C ")

    def test_unicode(self):
        self.assertEqual(module_0.flip_case("ÑOño"), "ñOÑO")

    def test_involution(self):
        for s in ["Hello", "WORLD", "PyThOn 123"]:
            self.assertEqual(module_0.flip_case(module_0.flip_case(s)), s)


# nonce:4948833f
if __name__ == "__main__":
    test_flip_case()
    unittest.main()