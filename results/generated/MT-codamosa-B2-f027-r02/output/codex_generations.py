

# Generated at 2026-11-02 09:51:24.890467
# Unit test for function flip_case
def test_flip_case():
    # Test mixed case string
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    
    # Test all lowercase string
    assert module_0.flip_case("hello") == "HELLO"
    
    # Test all uppercase string
    assert module_0.flip_case("WORLD") == "world"
    
    # Test empty string
    assert module_0.flip_case("") == ""
    
    # Test string with numbers and symbols (should remain unchanged)
    assert module_0.flip_case("abc123!@#") == "ABC123!@#"
    
    # Test single character lowercase
    assert module_0.flip_case("a") == "A"
    
    # Test single character uppercase
    assert module_0.flip_case("A") == "a"
    
    # Test string with spaces only
    assert module_0.flip_case("   ") == "   "
    
    # Test already flipped string returns original
    assert module_0.flip_case(module_0.flip_case("Python")) == "Python"
    
    print("All test cases passed!")


# Run the test
test_flip_case()

# Generated at 2026-11-02 09:53:14.814912
# Unit test for function flip_case
def test_flip_case():
    # Basic mixed case
    assert module_0.flip_case("Hello") == "hELLO"
    assert module_0.flip_case("Python") == "pYTHON"

    # Already swapped
    assert module_0.flip_case("hELLO") == "Hello"

    # All lowercase
    assert module_0.flip_case("abc") == "ABC"

    # All uppercase
    assert module_0.flip_case("ABC") == "abc"

    # Empty string
    assert module_0.flip_case("") == ""

    # No letters (digits, symbols, spaces)
    assert module_0.flip_case("12345!@# ") == "12345!@# "

    # Mixed with numbers and punctuation
    assert module_0.flip_case("PyThOn 3.12!") == "pYtHoN 3.12!"

    # Single character
    assert module_0.flip_case("a") == "A"
    assert module_0.flip_case("Z") == "z"

    # Unicode letters
    assert module_0.flip_case("ÑoÑo") == "ñOñO"

    # Palindromic swap (input equals output)
    assert module_0.flip_case("aBcDe") == "AbCdE"

    # Double application returns original
    s = "RandomString123"
    assert module_0.flip_case(module_0.flip_case(s)) == s

    # Non-ASCII mixed
    assert module_0.flip_case("Grüße") == "gRÜßE"

# Generated at 2026-11-02 09:54:43.872370
# Unit test for function flip_case
def test_flip_case():
    # Basic mixed case
    assert module_0.flip_case("Hello") == "hELLO"
    assert module_0.flip_case("hElLo") == "HeLlO"

    # All lowercase -> all uppercase
    assert module_0.flip_case("hello") == "HELLO"

    # All uppercase -> all lowercase
    assert module_0.flip_case("WORLD") == "world"

    # Empty string
    assert module_0.flip_case("") == ""

    # Single character
    assert module_0.flip_case("a") == "A"
    assert module_0.flip_case("A") == "a"

    # Non-alphabetic characters unchanged
    assert module_0.flip_case("Hello, World! 123") == "hELLO, wORLD! 123"
    assert module_0.flip_case("!@#$%") == "!@#$%"

    # Unicode characters
    assert module_0.flip_case("ñÁç") == "ÑáÇ"

    # Already-swapped string returns original (involution)
    s = "PyThOn 3.9"
    assert module_0.flip_case(module_0.flip_case(s)) == s

    # Whitespace preserved
    assert module_0.flip_case("a b\tc\nd") == "A B\tC\nD"

    print("All tests passed!")


test_flip_case()

# Generated at 2026-11-02 09:57:38.874901
# Unit test for function flip_case
def test_flip_case():
    # Test mixed case string
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    
    # Test all lowercase
    assert module_0.flip_case("hello") == "HELLO"
    
    # Test all uppercase
    assert module_0.flip_case("WORLD") == "world"
    
    # Test empty string
    assert module_0.flip_case("") == ""
    
    # Test string with numbers and special characters
    assert module_0.flip_case("Python 3.9!") == "pYTHON 3.9!"
    
    # Test single character
    assert module_0.flip_case("a") == "A"
    assert module_0.flip_case("B") == "b"
    
    # Test string with no letters
    assert module_0.flip_case("12345 !@#") == "12345 !@#"
    
    # Test double flip returns original
    s = "MiXeD CaSe StRiNg"
    assert module_0.flip_case(module_0.flip_case(s)) == s
    
    print("All tests passed!")


if __name__ == "__main__":
    test_flip_case()

# Generated at 2026-11-02 09:58:22.949167
# Unit test for function flip_case
def test_flip_case():
    assert module_0.flip_case("hello") == "HELLO"
    assert module_0.flip_case("WORLD") == "world"
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    assert module_0.flip_case("") == ""
    assert module_0.flip_case("PyThOn 123!") == "pYtHoN 123!"
    assert module_0.flip_case("aBcDeF") == "AbCdEf"
    assert module_0.flip_case("12345!@#") == "12345!@#"