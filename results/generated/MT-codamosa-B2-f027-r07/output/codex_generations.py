

# Generated at 2026-10-24 12:31:46.966340
# Unit test for function flip_case
def test_flip_case():
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    assert module_0.flip_case("Python123!") == "pYTHON123!"
    assert module_0.flip_case("") == ""
    assert module_0.flip_case("12345") == "12345"
    assert module_0.flip_case("aBcXyZ") == "AbCxYz"

# Generated at 2026-10-24 12:32:00.091216
# Unit test for function flip_case
def test_flip_case():
    assert module_0.flip_case("Hello World!") == "hELLO wORLD!"
    assert module_0.flip_case("Python123") == "pYTHON123"
    assert module_0.flip_case("already LOWER") == "ALREADY lower"
    assert module_0.flip_case("") == ""

# Generated at 2026-10-24 12:32:13.438762
# Unit test for function flip_case
def test_flip_case():
    assert module_0.flip_case("Hello World!") == "hELLO wORLD!"
    assert module_0.flip_case("Python123") == "pYTHON123"
    assert module_0.flip_case("ABC xyz") == "abc XYZ"
    assert module_0.flip_case("") == ""
    assert module_0.flip_case("123!@#") == "123!@#"

# Generated at 2026-10-24 12:32:21.122168
# Unit test for function flip_case
def test_flip_case():
    # Basic mixed case
    assert module_0.flip_case("Hello World") == "hELLO wORLD"
    # All lowercase
    assert module_0.flip_case("abc") == "ABC"
    # All uppercase
    assert module_0.flip_case("ABC") == "abc"
    # Empty string
    assert module_0.flip_case("") == ""
    # No letters (digits/punctuation unchanged)
    assert module_0.flip_case("123 !@#") == "123 !@#"
    # Single character
    assert module_0.flip_case("a") == "A"
    # Already flipped round-trips back
    assert module_0.flip_case(module_0.flip_case("PyThOn 3.12")) == "PyThOn 3.12"

test_flip_case()
print("All tests passed")

# Generated at 2026-10-24 12:32:23.771905
# Unit test for function flip_case

# Generated at 2026-10-24 12:32:42.827763
# Unit test for function flip_case
def test_flip_case():assert module_0.flip_case("Hello, World! 123") == "hELLO, wORLD! 123"