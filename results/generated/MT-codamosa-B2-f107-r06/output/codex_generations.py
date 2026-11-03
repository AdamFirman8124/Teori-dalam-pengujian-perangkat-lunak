

# Generated at 2026-11-02 09:39:07.102595
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Test with small values where all numbers are single-digit palindromes
    assert module_0.even_odd_palindrome(1) == (0, 1)   # 1 is odd palindrome
    assert module_0.even_odd_palindrome(3) == (1, 2)   # 2 even, 1 and 3 odd
    assert module_0.even_odd_palindrome(9) == (4, 5)   # 2,4,6,8 even; 1,3,5,7,9 odd

    # Test with values including non-palindromes and multi-digit palindromes
    assert module_0.even_odd_palindrome(12) == (4, 6)  # 11 is an odd palindrome, 10 and 12 are not
    assert module_0.even_odd_palindrome(22) == (5, 6)  # 11 odd, 22 even

    # Test edge case: n = 0 (empty range)
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # Test larger value
    assert module_0.even_odd_palindrome(100) == (18, 31)

    print("All tests passed!")


test_even_odd_palindrome()

# Generated at 2026-11-02 09:40:53.497778
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
# nonce:8259abee
    assert module_0.even_odd_palindrome(0) == (0, 0)
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(2) == (1, 1)
    assert module_0.even_odd_palindrome(3) == (1, 2)
    assert module_0.even_odd_palindrome(5) == (2, 3)
    assert module_0.even_odd_palindrome(9) == (4, 5)
    assert module_0.even_odd_palindrome(10) == (4, 5)
    assert module_0.even_odd_palindrome(11) == (4, 6)
    assert module_0.even_odd_palindrome(22) == (5, 7)
    assert module_0.even_odd_palindrome(100) == (8, 10)
    assert module_0.even_odd_palindrome(123) == (8, 13)
    assert module_0.even_odd_palindrome(999) == (44, 45)
    print("All test cases passed!")

test_even_odd_palindrome()

# Generated at 2026-11-02 09:42:19.409344
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # nonce:dd095cd1
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(2) == (1, 1)
    assert module_0.even_odd_palindrome(3) == (1, 2)
    assert module_0.even_odd_palindrome(4) == (2, 2)
    assert module_0.even_odd_palindrome(5) == (2, 3)
    assert module_0.even_odd_palindrome(9) == (4, 5)
    assert module_0.even_odd_palindrome(12) == (4, 6)
    assert module_0.even_odd_palindrome(0) == (0, 0)
    assert module_0.even_odd_palindrome(100) == (18, 21)
    assert module_0.even_odd_palindrome(11) == (4, 6)

test_even_odd_palindrome()

# Generated at 2026-11-02 09:43:24.956338
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Single digit cases
    assert module_0.even_odd_palindrome(1) == (0, 1)      # only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(2) == (1, 1)      # 1 (odd), 2 (even)
    assert module_0.even_odd_palindrome(3) == (1, 2)      # 1, 3 odd; 2 even
    assert module_0.even_odd_palindrome(9) == (4, 5)      # evens: 2,4,6,8; odds: 1,3,5,7,9

    # Non-palindrome boundary
    assert module_0.even_odd_palindrome(10) == (4, 5)     # 10 is not a palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)     # 11 is an odd palindrome

    # Mixed multi-digit palindromes
    assert module_0.even_odd_palindrome(22) == (5, 6)     # 22 is an even palindrome
    assert module_0.even_odd_palindrome(33) == (5, 7)     # 33 is an odd palindrome

    # Larger range
    assert module_0.even_odd_palindrome(100) == (8, 10)   # 11,22,...,99 plus single digits

    # Edge cases: empty range
    assert module_0.even_odd_palindrome(0) == (0, 0)
    assert module_0.even_odd_palindrome(-5) == (0, 0)

    print("All tests passed!")


test_even_odd_palindrome()

# Generated at 2026-11-02 09:44:39.148912
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Single-digit palindromes: 1..9 are all palindromes
    assert module_0.even_odd_palindrome(1) == (0, 1)   # only 1 (odd)
    assert module_0.even_odd_palindrome(2) == (1, 1)   # 2 even, 1 odd
    assert module_0.even_odd_palindrome(3) == (1, 2)   # 2 even; 1, 3 odd
    assert module_0.even_odd_palindrome(5) == (2, 3)   # 2,4 even; 1,3,5 odd
    assert module_0.even_odd_palindrome(9) == (4, 5)   # 2,4,6,8 even; 1,3,5,7,9 odd

    # Multi-digit palindromes included
    assert module_0.even_odd_palindrome(12) == (4, 6)  # adds 11 (odd)
    assert module_0.even_odd_palindrome(22) == (5, 6)  # adds 11 (odd), 22 (even)
    assert module_0.even_odd_palindrome(100) == (8, 10)  # evens: 2,4,6,8,22,44,66,88; odds: 1,3,5,7,9,11,33,55,77,99
    assert module_0.even_odd_palindrome(123) == (8, 13)  # adds 101, 111, 121 (odd)

    # Edge cases: empty range yields zero counts
    assert module_0.even_odd_palindrome(0) == (0, 0)
    assert module_0.even_odd_palindrome(-5) == (0, 0)

    # Result is always a tuple of two non-negative ints
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2
    even_count, odd_count = result
    assert even_count >= 0 and odd_count >= 0

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()