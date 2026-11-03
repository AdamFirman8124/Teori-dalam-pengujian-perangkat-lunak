

# Generated at 2026-11-02 12:25:37.360738
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Single digit cases
    assert module_0.even_odd_palindrome(1) == (0, 1)      # only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(2) == (1, 1)      # 1 (odd), 2 (even)
    assert module_0.even_odd_palindrome(3) == (1, 2)      # 1, 3 (odd); 2 (even)
    assert module_0.even_odd_palindrome(9) == (4, 5)      # 2,4,6,8 (even); 1,3,5,7,9 (odd)

    # Boundary around two-digit numbers
    assert module_0.even_odd_palindrome(10) == (4, 5)     # 10 is not a palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)     # 11 is an odd palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)     # 12 is not a palindrome

    # Two-digit palindromes
    assert module_0.even_odd_palindrome(22) == (5, 7)     # adds 11 (odd), 22 (even)

    # Larger range
    assert module_0.even_odd_palindrome(100) == (9, 10)   # evens: 2,4,6,8,22,44,66,88; odds: 1,3,5,7,9,11,33,55,77,99

    # Edge case: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)

# Generated at 2026-11-02 12:26:55.124770
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 0: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # n = 1: only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 3: 1, 3 odd palindromes; 2 even palindrome
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # n = 9: single digits 1-9 are all palindromes
    # even: 2, 4, 6, 8 (4); odd: 1, 3, 5, 7, 9 (5)
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 12: adds 11 (odd palindrome); 10 and 12 are not palindromes
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 100: single digits (4 even, 5 odd) + two-digit palindromes 11..99
    # (22, 44, 66, 88 even; 11, 33, 55, 77, 99 odd); 100 not a palindrome
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # n = 123: adds three-digit palindromes 101, 111, 121 (all odd)
    assert module_0.even_odd_palindrome(123) == (8, 13)

    # Result type check
    result = module_0.even_odd_palindrome(5)
    assert isinstance(result, tuple)
    assert len(result) == 2

# Generated at 2026-11-02 12:27:40.977284
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(5) == (0, 5)
    assert module_0.even_odd_palindrome(9) == (0, 9)
    assert module_0.even_odd_palindrome(10) == (0, 9)
    assert module_0.even_odd_palindrome(12) == (0, 10)
    assert module_0.even_odd_palindrome(22) == (1, 10)
    assert module_0.even_odd_palindrome(100) == (4, 10)
    assert module_0.even_odd_palindrome(0) == (0, 0)
    print("All tests passed!")

test_even_odd_palindrome()

# Generated at 2026-11-02 12:28:33.852121
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Single element: only 1, which is an odd palindrome
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # Digits 1-9 are all palindromes: 4 even (2,4,6,8), 5 odd (1,3,5,7,9)
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # 10 is not a palindrome, so result is unchanged
    assert module_0.even_odd_palindrome(10) == (4, 5)

    # 11 is an odd palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)

    # 22 is an even palindrome
    assert module_0.even_odd_palindrome(22) == (5, 6)

    # Up to 100: two-digit palindromes add 4 even and 5 odd
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # No range at all
    assert module_0.even_odd_palindrome(0) == (0, 0)

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()

# Generated at 2026-11-02 12:30:17.223979
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():assert module_0.even_odd_palindrome(1) == (0, 1)