

# Generated at 2026-11-02 17:34:31.462487
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Test with n = 1: only 1, an odd palindrome
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # Test with n = 2: 1 (odd pal), 2 (even pal)
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # Test with n = 3: 1, 2, 3 are all palindromes
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # Test with n = 4
    assert module_0.even_odd_palindrome(4) == (2, 2)

    # Test with n = 9: single digits 1-9; odd: 1,3,5,7,9 (5), even: 2,4,6,8 (4)
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # Test with n = 10: adds 10, which is not a palindrome
    assert module_0.even_odd_palindrome(10) == (4, 5)

    # Test with n = 12: adds 11 (odd palindrome), 12 is not a palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # Test with n = 0: no numbers in range
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # Test with a larger value, n = 100:
    # Palindromes 1-9 and 11,22,...,99.
    # Even palindromes: 2,4,6,8 (4) + 22,44,66,88 (4) = 8
    # Odd palindromes: 1,3,5,7,9 (5) + 11,33,55,77,99 (5) = 10
    assert module_0.even_odd_palindrome(100) == (8, 10)

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()

# Generated at 2026-11-02 17:36:04.003371
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 1: only 1, an odd palindrome
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 3: palindromes 1, 2, 3 -> even: 2, odd: 1, 3
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # n = 9: all single digits are palindromes -> even: 2,4,6,8; odd: 1,3,5,7,9
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 12: adds 11 (odd palindrome); 10 and 12 are not palindromes
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 22: adds 11 (odd) and 22 (even)
    assert module_0.even_odd_palindrome(22) == (5, 6)

    # n = 45: adds 11, 33 (odd) and 22, 44 (even)
    assert module_0.even_odd_palindrome(45) == (6, 7)

    # n = 100: single digits (4 even, 5 odd) + two-digit palindromes
    # 22,44,66,88 (even) and 11,33,55,77,99 (odd)
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # n = 0: no numbers in range
    assert module_0.even_odd_palindrome(0) == (0, 0)

# Generated at 2026-11-02 17:37:42.401499
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # nonce:6bccc1dd
    # Single element cases
    assert module_0.even_odd_palindrome(1) == (0, 1)   # only 1: odd palindrome
    assert module_0.even_odd_palindrome(2) == (1, 1)   # 1 (odd), 2 (even)

    # Small ranges
    assert module_0.even_odd_palindrome(3) == (1, 2)   # 1, 3 odd pals; 2 even pal
    assert module_0.even_odd_palindrome(4) == (2, 2)
    assert module_0.even_odd_palindrome(5) == (2, 3)
    assert module_0.even_odd_palindrome(9) == (4, 5)   # all single digits are palindromes

    # Non-palindromes beyond 9
    assert module_0.even_odd_palindrome(10) == (4, 5)  # 10 is not a palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)  # 11 is an odd palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)
    assert module_0.even_odd_palindrome(20) == (4, 6)  # only 11 in 10..20 is a palindrome
    assert module_0.even_odd_palindrome(22) == (5, 6)  # 22 is an even palindrome

    # Larger range up to 100
    # one-digit pals: even {2,4,6,8}=4, odd {1,3,5,7,9}=5
    # two-digit pals: even {22,44,66,88}=4, odd {11,33,55,77,99}=5
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # Edge case: no range at all
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # Verify return type is a tuple
    result = module_0.even_odd_palindrome(15)
    assert isinstance(result, tuple) and len(result) == 2

# Generated at 2026-11-02 17:38:29.664239
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 0: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # n = 1: only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 2: 1 (odd), 2 (even)
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # n = 3: 1, 3 odd; 2 even
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # n = 5: even {2,4}, odd {1,3,5}
    assert module_0.even_odd_palindrome(5) == (2, 3)

    # n = 9: all single digits are palindromes
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 10: same as 9 (10 is not a palindrome)
    assert module_0.even_odd_palindrome(10) == (4, 5)

    # n = 12: adds 11 (odd palindrome)
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 22: adds 11, 22
    assert module_0.even_odd_palindrome(22) == (5, 7)

    # n = 100: two-digit palindromes 11..99 plus single digits
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # Verify return type is a tuple
    assert isinstance(module_0.even_odd_palindrome(10), tuple)

    print("All tests passed!")


test_even_odd_palindrome()

# Generated at 2026-11-02 17:39:18.722855
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():assert module_0.even_odd_palindrome(0) == (0, 0)