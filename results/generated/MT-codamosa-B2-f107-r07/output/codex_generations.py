

# Generated at 2026-11-01 19:31:19.132540
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 1: only 1, which is an odd palindrome
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 2: 1 (odd palindrome), 2 (even palindrome)
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # n = 9: single digits 1-9 are all palindromes
    # odd: 1,3,5,7,9 -> 5 ; even: 2,4,6,8 -> 4
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 12: adds 11 (odd palindrome); 10 is not a palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 0: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # n = 100: two-digit palindromes 11..99 (5 odd, 4 even) plus single digits
    # even: 4 + 4 = 8 ; odd: 5 + 5 = 10 ; 100 is not a palindrome
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # Result must be a tuple of two integers
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2
    assert all(isinstance(x, int) for x in result)

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()

# Generated at 2026-11-01 19:32:00.776328
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 1: only palindrome is 1 (odd)
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 2: 1 (odd), 2 (even)
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # n = 3: 1, 2, 3 all palindromes
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # n = 9: single digits 1-9 all palindromes (4 even, 5 odd)
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 10: 10 is not a palindrome
    assert module_0.even_odd_palindrome(10) == (4, 5)

    # n = 12: adds 11 (odd palindrome); 10, 12 are not
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 100: 11,22,...,99 plus 1-9; evens: 2,4,6,8,22,44,66,88 = 8; odds: 1,3,5,7,9,11,33,55,77,99 = 10
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # n = 0: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # result types are a tuple of ints
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2
    assert all(isinstance(x, int) for x in result)

    # consistency check: total count equals sum of parts for a larger range
    even_count, odd_count = module_0.even_odd_palindrome(500)
    assert even_count + odd_count == sum(
        1 for i in range(1, 501) if str(i) == str(i)[::-1]
    )

    print("All tests passed!")


test_even_odd_palindrome()

# Generated at 2026-11-01 19:32:37.020744
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 1: only 1, which is odd palindrome
    assert module_0.even_odd_palindrome(1) == (0, 1)
    
    # n = 3: 1, 3 are odd palindromes; 2 is even palindrome
    assert module_0.even_odd_palindrome(3) == (1, 2)
    
    # n = 9: 1-9 are all palindromes (5 odd, 4 even)
    assert module_0.even_odd_palindrome(9) == (4, 5)
    
    # n = 12: adds 11 (odd palindrome); 10 and 12 are not palindromes
    assert module_0.even_odd_palindrome(12) == (4, 6)
    
    # n = 100: single digits 1-9 plus 11,22,...,99
    # odd: 1,3,5,7,9,11,33,55,77,99 -> 10
    # even: 2,4,6,8,22,44,66,88 -> 8
    assert module_0.even_odd_palindrome(100) == (8, 10)
    
    # Edge case: n = 0 yields no numbers
    assert module_0.even_odd_palindrome(0) == (0, 0)
    
    # Edge case: negative n yields empty range
    assert module_0.even_odd_palindrome(-5) == (0, 0)
    
    # Non-palindrome even/odd numbers are skipped correctly
    # n = 21: palindromes 1-9, 11; 22 excluded (n=21)
    # odd: 1,3,5,7,9,11 -> 6 ; even: 2,4,6,8 -> 4
    assert module_0.even_odd_palindrome(21) == (4, 6)
    
    # Check return type is a tuple
    result = module_0.even_odd_palindrome(10)
    assert isinstance(result, tuple) and len(result) == 2
    
    print("All tests passed!")

# Generated at 2026-11-01 19:33:11.639908
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(2) == (1, 1)
    assert module_0.even_odd_palindrome(3) == (1, 2)
    assert module_0.even_odd_palindrome(5) == (2, 3)
    assert module_0.even_odd_palindrome(9) == (4, 5)
    assert module_0.even_odd_palindrome(10) == (4, 5)
    assert module_0.even_odd_palindrome(12) == (5, 6)
    assert module_0.even_odd_palindrome(0) == (0, 0)
    assert module_0.even_odd_palindrome(100) == (18, 11)
    print("All tests passed!")

test_even_odd_palindrome()

# Generated at 2026-11-01 19:34:02.332771
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Single number, odd palindrome
    assert module_0.even_odd_palindrome(1) == (0, 1)
    # Numbers 1-9: all are palindromes; odd: 1,3,5,7,9 even: 2,4,6,8
    assert module_0.even_odd_palindrome(9) == (4, 5)
    # 10 not a palindrome, 11 is an odd palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)
    # n = 0 edge case: no numbers checked
    assert module_0.even_odd_palindrome(0) == (0, 0)
    # Includes two-digit even palindrome 22
    assert module_0.even_odd_palindrome(22) == (5, 6)
    # Larger known case
    assert module_0.even_odd_palindrome(100) == (49, 50)