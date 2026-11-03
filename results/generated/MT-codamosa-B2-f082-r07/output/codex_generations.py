

# Generated at 2026-11-03 02:42:07.643967
# Unit test for function prime_length
def test_prime_length():
    # Empty string (length 0) -> False
    assert module_0.prime_length("") == False

    # Single character (length 1) -> False
    assert module_0.prime_length("a") == False

    # Length 2 is prime -> True
    assert module_0.prime_length("ab") == True

    # Length 3 is prime -> True
    assert module_0.prime_length("abc") == True

    # Length 4 is not prime -> False
    assert module_0.prime_length("abcd") == False

    # Length 5 is prime -> True
    assert module_0.prime_length("abcde") == True

    # Length 6 is not prime -> False
    assert module_0.prime_length("abcdef") == False

    # Length 7 is prime -> True
    assert module_0.prime_length("abcdefg") == True

    # Length 8 is not prime -> False
    assert module_0.prime_length("abcdefgh") == False

    # Length 9 is not prime -> False
    assert module_0.prime_length("abcdefghi") == False

    # Length 10 is not prime -> False
    assert module_0.prime_length("abcdefghij") == False

    # Length 11 is prime -> True
    assert module_0.prime_length("abcdefghijk") == True

    # Length 13 is prime -> True
    assert module_0.prime_length("abcdefghijklm") == True

    # Length 25 (5*5) is not prime -> False
    assert module_0.prime_length("a" * 25) == False

    # Length 29 is prime -> True
    assert module_0.prime_length("a" * 29) == True

    print("All tests passed!")


test_prime_length()

# Generated at 2026-11-03 02:44:53.073957
# Unit test for function prime_length
def test_prime_length():
    # Prime lengths
    assert module_0.prime_length("Hello") == True      # length 5 (prime)
    assert module_0.prime_length("ab") == True         # length 2 (prime)
    assert module_0.prime_length("abc") == True        # length 3 (prime)
    assert module_0.prime_length("abcedf") == True     # length 6 -> False
    assert module_0.prime_length("a") == False         # length 1 (not prime)
    assert module_0.prime_length("") == False          # length 0 (not prime)
    assert module_0.prime_length("aaaa") == False      # length 4 (not prime)
    assert module_0.prime_length("aaaaaaaaaa") == False  # length 10 (not prime)
    assert module_0.prime_length("aabbccdd") == False  # length 8 (not prime)
    assert module_0.prime_length("aabbcc") == False    # length 6 (not prime)
    assert module_0.prime_length("aabb") == False      # length 4 (not prime)
    assert module_0.prime_length("aaaaaaaaaaa") == True  # length 11 (prime)
    assert module_0.prime_length("x") == False         # length 1
    assert module_0.prime_length("xyzzy") == True      # length 5 (prime)
    assert module_0.prime_length("xy") == True         # length 2 (prime)
    assert module_0.prime_length("xyzz") == False      # length 4 (not prime)
    assert module_0.prime_length("zzzzzzz") == True    # length 7 (prime)
    assert module_0.prime_length("zzzzzzzzzzzzz") == True  # length 13 (prime)

    print("All test cases passed!")


if __name__ == "__main__":
    test_prime_length()

# Generated at 2026-11-03 02:47:23.501489
# Unit test for function prime_length
def test_prime_length():
    # Test empty string (length 0 -> False)
    assert module_0.prime_length("") == False

    # Test single character (length 1 -> False)
    assert module_0.prime_length("a") == False

    # Test length 2 (prime -> True)
    assert module_0.prime_length("ab") == True

    # Test length 3 (prime -> True)
    assert module_0.prime_length("abc") == True

    # Test length 4 (composite -> False)
    assert module_0.prime_length("abcd") == False

    # Test length 5 (prime -> True)
    assert module_0.prime_length("abcde") == True

    # Test length 6 (composite -> False)
    assert module_0.prime_length("abcdef") == False

    # Test length 7 (prime -> True)
    assert module_0.prime_length("abcdefg") == True

    # Test length 8 (composite -> False)
    assert module_0.prime_length("abcdefgh") == False

    # Test length 9 (composite, divisible by 3 -> False)
    assert module_0.prime_length("abcdefghi") == False

    # Test length 11 (prime -> True)
    assert module_0.prime_length("hello world") == True

    # Test length 10 (composite -> False)
    assert module_0.prime_length("0123456789") == False

    # Test string with special characters (length 13 -> True)
    assert module_0.prime_length("Hello, World!") == True

    # Test string with whitespace only (length 4 -> False)
    assert module_0.prime_length("    ") == False

    # Test string with unicode characters (length 5 -> True)
    assert module_0.prime_length("héllo") == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_prime_length()

# Generated at 2026-11-03 02:49:46.983691
# Unit test for function prime_length
def test_prime_length():
    # Length 0 -> False
    assert module_0.prime_length("") is False
    # Length 1 -> False
    assert module_0.prime_length("a") is False
    # Length 2 (prime) -> True
    assert module_0.prime_length("ab") is True
    assert module_0.prime_length("hi") is True
    # Length 3 (prime) -> True
    assert module_0.prime_length("abc") is True
    # Length 4 (2*2) -> False
    assert module_0.prime_length("abcd") is False
    assert module_0.prime_length("test") is False
    # Length 5 (prime) -> True
    assert module_0.prime_length("Hello") is True
    assert module_0.prime_length("abcde") is True
    # Length 6 (2*3) -> False
    assert module_0.prime_length("abcdef") is False
    # Length 7 (prime) -> True
    assert module_0.prime_length("a" * 7) is True
    # Length 8 -> False
    assert module_0.prime_length("a" * 8) is False
    # Length 9 (3*3) -> False
    assert module_0.prime_length("a" * 9) is False
    # Length 10 -> False
    assert module_0.prime_length("a" * 10) is False
    # Length 11 (prime) -> True
    assert module_0.prime_length("hello world") is True
    assert module_0.prime_length("a" * 11) is True
    # Length 12 -> False
    assert module_0.prime_length("a" * 12) is False
    # Length 13 (prime) -> True
    assert module_0.prime_length("a" * 13) is True
    # Larger primes -> True
    assert module_0.prime_length("a" * 17) is True
    assert module_0.prime_length("a" * 19) is True
    assert module_0.prime_length("a" * 23) is True
    # Larger composites -> False
    assert module_0.prime_length("a" * 25) is False   # 5*5
    assert module_0.prime_length("a" * 49) is False   # 7*7
    assert module_0.prime_length("a" * 100) is False