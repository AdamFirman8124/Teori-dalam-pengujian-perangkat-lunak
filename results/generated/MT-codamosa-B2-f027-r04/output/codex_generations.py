

# Generated at 2026-11-02 18:36:31.872377
# Unit test for function flip_case
def test_flip_case():
    # Basic case flip
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    assert module_0.flip_case("hello") == "HELLO"
    assert module_0.flip_case("WORLD") == "world"

    # Mixed case
    assert module_0.flip_case("PyThOn") == "pYtHoN"

    # String with no letters
    assert module_0.flip_case("12345!@#") == "12345!@#"

    # Empty string
    assert module_0.flip_case("") == ""

    # Single character
    assert module_0.flip_case("a") == "A"
    assert module_0.flip_case("B") == "b"

    # Already alternating case
    assert module_0.flip_case("aBcDeF") == "AbCdEf"

# Generated at 2026-11-02 18:39:03.830740
# Unit test for function flip_case
def test_flip_case():
    # Basic mixed case
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    
    # All lowercase
    assert module_0.flip_case("hello") == "HELLO"
    
    # All uppercase
    assert module_0.flip_case("WORLD") == "world"
    
    # Empty string
    assert module_0.flip_case("") == ""
    
    # Single character lowercase
    assert module_0.flip_case("a") == "A"
    
    # Single character uppercase
    assert module_0.flip_case("A") == "a"
    
    # String with digits and punctuation (unchanged)
    assert module_0.flip_case("Python 3.9!") == "pYTHON 3.9!"
    
    # String with special characters and spaces
    assert module_0.flip_case("aBc DeF!@#") == "AbC dEf!@#"
    
    # Repeated application returns original string
    original = "MiXeD CaSe StRiNg"
    assert module_0.flip_case(module_0.flip_case(original)) == original

# Generated at 2026-11-02 18:41:24.167931
# Unit test for function flip_case
def test_flip_case():
    # Basic mixed case
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    # All uppercase
    assert module_0.flip_case("ABC") == "abc"
    # All lowercase
    assert module_0.flip_case("abc") == "ABC"
    # Empty string
    assert module_0.flip_case("") == ""
    # String with digits and punctuation unchanged
    assert module_0.flip_case("PyThOn3.9!") == "pYtHoN3.9!"
    # Single character lower
    assert module_0.flip_case("a") == "A"
    # Single character upper
    assert module_0.flip_case("Z") == "z"
    # Already flipped string is idempotent
    assert module_0.flip_case(module_0.flip_case("MiXeD CaSe 123")) == "MiXeD CaSe 123"

# Generated at 2026-11-02 18:42:48.828264
# Unit test for function flip_case
def test_flip_case():
    assert module_0.flip_case('Hello') == 'hELLO'
    assert module_0.flip_case('These dolls should be preserved.') == 'tHESE DOLLS SHOULD BE PRESERVED.'
    assert module_0.flip_case('') == ''
    assert module_0.flip_case('Python123') == 'pYTHON123'
    assert module_0.flip_case('already lower') == 'ALREADY LOWER'
    assert module_0.flip_case('ALREADY UPPER') == 'already upper'


if __name__ == "__main__":
    test_flip_case()
    print("All tests passed!")

# Generated at 2026-11-02 18:44:34.533561
# Unit test for function flip_case
def test_flip_case():
    # Basic mixed case
    assert module_0.flip_case('Hello') == 'hELLO'
    assert module_0.flip_case('Hello World') == 'hELLO wORLD'

    # All lowercase
    assert module_0.flip_case('python') == 'PYTHON'

    # All uppercase
    assert module_0.flip_case('PYTHON') == 'python'

    # Empty string
    assert module_0.flip_case('') == ''

    # Single character
    assert module_0.flip_case('a') == 'A'
    assert module_0.flip_case('A') == 'a'

    # Non-alphabetic characters remain unchanged
    assert module_0.flip_case('abc123!@#') == 'ABC123!@#'

    # Mixed with spaces and punctuation
    assert module_0.flip_case('PyThOn 3.9!') == 'pYtHoN 3.9!'

    # Involution: flipping twice returns original
    s = 'MiXeD CaSe StRiNg'
    assert module_0.flip_case(module_0.flip_case(s)) == s

    print("All tests passed!")


if __name__ == "__main__":
    test_flip_case()