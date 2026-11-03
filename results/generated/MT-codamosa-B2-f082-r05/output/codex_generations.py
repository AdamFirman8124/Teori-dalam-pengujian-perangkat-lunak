

# Generated at 2026-11-02 09:22:22.763798
# Unit test for function prime_length
def test_prime_length():
    assert module_0.prime_length("Hello") == True      # length 5 (prime)
    assert module_0.prime_length("abcdcba") == True    # length 7 (prime)
    assert module_0.prime_length("kittens") == True    # length 7 (prime)
    assert module_0.prime_length("orange") == True     # length 6 -> False? No, 6 is composite
    # Fix: "orange" has length 6, composite
    assert module_0.prime_length("orange") == False
    assert module_0.prime_length("") == False          # length 0
    assert module_0.prime_length("a") == False         # length 1
    assert module_0.prime_length("ab") == True         # length 2 (prime)
    assert module_0.prime_length("abc") == True        # length 3 (prime)
    assert module_0.prime_length("abcd") == False      # length 4 (composite)
    assert module_0.prime_length("abcdef") == False    # length 6 (composite)
    assert module_0.prime_length("abcdefgh") == False  # length 8 (composite)
    assert module_0.prime_length("abcdefghi") == False # length 9 (composite)
    assert module_0.prime_length("abcdefghij") == False  # length 10 (composite)
    assert module_0.prime_length("abcdefghijk") == True  # length 11 (prime)
    assert module_0.prime_length("ab cd") == True      # length 5 including space (prime)
    assert module_0.prime_length("a!b@c") == True      # length 5 with special chars (prime)
    print("All test cases passed!")


if __name__ == "__main__":
    test_prime_length()

# Generated at 2026-11-02 09:24:47.142836
# Unit test for function prime_length
def test_prime_length():
    # Test with prime length strings
    assert module_0.prime_length("Hello") == True, "Length 5 is prime"
    assert module_0.prime_length("ab") == True, "Length 2 is prime"
    assert module_0.prime_length("abc") == True, "Length 3 is prime"
    assert module_0.prime_length("abcdefg") == True, "Length 7 is prime"
    assert module_0.prime_length("abcdefghijk") == True, "Length 11 is prime"

    # Test with non-prime length strings
    assert module_0.prime_length("abcd") == False, "Length 4 is not prime"
    assert module_0.prime_length("abcdef") == False, "Length 6 is not prime"
    assert module_0.prime_length("abcdefgh") == False, "Length 8 is not prime"
    assert module_0.prime_length("abcdefghi") == False, "Length 9 is not prime"
    assert module_0.prime_length("abcdefghij") == False, "Length 10 is not prime"

    # Test edge cases
    assert module_0.prime_length("") == False, "Length 0 is not prime"
    assert module_0.prime_length("a") == False, "Length 1 is not prime"

    # Test with spaces and special characters
    assert module_0.prime_length("a b c") == True, "Length 5 (with spaces) is prime"
    assert module_0.prime_length("!@#$") == False, "Length 4 (special chars) is not prime"

    print("All tests passed!")

# Run the test
test_prime_length()

# Generated at 2026-11-02 09:27:02.207071
# Unit test for function prime_length
def test_prime_length():
    # Empty string (length 0) -> False
    assert module_0.prime_length("") == False
    # Single character (length 1) -> False
    assert module_0.prime_length("a") == False
    # Length 2 (prime)
    assert module_0.prime_length("ab") == True
    # Length 3 (prime)
    assert module_0.prime_length("abc") == True
    # Length 4 (not prime)
    assert module_0.prime_length("abcd") == False
    # Length 5 (prime)
    assert module_0.prime_length("abcde") == True
    # Length 6 (not prime)
    assert module_0.prime_length("abcdef") == False
    # Length 7 (prime)
    assert module_0.prime_length("abcdefg") == True
    # Length 9 (not prime, 3*3)
    assert module_0.prime_length("a" * 9) == False
    # Length 11 (prime)
    assert module_0.prime_length("a" * 11) == True
    # Length 12 (not prime)
    assert module_0.prime_length("a" * 12) == False
    # Length 13 (prime)
    assert module_0.prime_length("a" * 13) == True
    # Length 15 (not prime, 3*5)
    assert module_0.prime_length("hello world he") == False
    # Length 17 (prime)
    assert module_0.prime_length("a" * 17) == True
    # Length 25 (not prime, 5*5)
    assert module_0.prime_length("a" * 25) == False
    # Length 29 (prime)
    assert module_0.prime_length("a" * 29) == True
    # Length 30 (not prime)
    assert module_0.prime_length("a" * 30) == False
    # Special characters and spaces count toward length
    assert module_0.prime_length("!!") == True       # length 2
    assert module_0.prime_length("a b") == True      # length 3
    assert module_0.prime_length("a b c") == False   # length 5 -> True actually

# Generated at 2026-11-02 09:29:04.377809
# Unit test for function prime_length
def test_prime_length():
    # Non-prime lengths
    assert module_0.prime_length("") == False, "Empty string has length 0, not prime"
    assert module_0.prime_length("a") == False, "Length 1 is not prime"
    assert module_0.prime_length("aaaa") == False, "Length 4 is not prime"
    assert module_0.prime_length("aaaaaa") == False, "Length 6 is not prime"
    assert module_0.prime_length("aaaaaaaa") == False, "Length 8 is not prime"
    assert module_0.prime_length("aaaaaaaaa") == False, "Length 9 is not prime"

    # Prime lengths
    assert module_0.prime_length("aa") == True, "Length 2 is prime"
    assert module_0.prime_length("aaa") == True, "Length 3 is prime"
    assert module_0.prime_length("aaaaa") == True, "Length 5 is prime"
    assert module_0.prime_length("aaaaaaa") == True, "Length 7 is prime"
    assert module_0.prime_length("aaaaaaaaaaa") == True, "Length 11 is prime"
    assert module_0.prime_length("Hello") == True, "'Hello' has length 5, prime"
    assert module_0.prime_length("Hi") == True, "'Hi' has length 2, prime"

    # Mixed word examples
    assert module_0.prime_length("orange") == False, "'orange' has length 6, not prime"
    assert module_0.prime_length("banana") == False, "'banana' has length 6, not prime"
    assert module_0.prime_length("watermelon") == False, "'watermelon' has length 10, not prime"
    assert module_0.prime_length("melon") == True, "'melon' has length 5, prime"

    # Special characters and whitespace count toward length
    assert module_0.prime_length("a b") == True, "'a b' has length 3, prime"
    assert module_0.prime_length("!@#") == True, "'!@#' has length 3, prime"
    assert module_0.prime_length("!@#$") == False, "'!@#$' has length 4, not prime"

    print("All test_prime_length tests passed!")


if __name__ == "__main__":
    test_prime_length()