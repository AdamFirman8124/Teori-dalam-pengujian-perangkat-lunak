

# Generated at 2026-11-01 20:53:02.727830
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 0: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # n = 1: only 1, which is an odd palindrome
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 2: 1 (odd), 2 (even) are both palindromes
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # n = 3: 1, 2, 3 all palindromes
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # n = 5: 1..5 all palindromes
    assert module_0.even_odd_palindrome(5) == (2, 3)

    # n = 9: single digits 1-9 all palindromes
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 10: 10 is not a palindrome
    assert module_0.even_odd_palindrome(10) == (4, 5)

    # n = 11: 11 is an odd palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)

    # n = 22: adds even palindrome 22
    assert module_0.even_odd_palindrome(22) == (5, 6)

    # n = 99: all two-digit palindromes included
    assert module_0.even_odd_palindrome(99) == (8, 10)

    # n = 100: 100 is not a palindrome
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # n = 101: adds odd palindrome 101
    assert module_0.even_odd_palindrome(101) == (8, 11)

    # n = 123: known result (8 even, 13 odd)
    assert module_0.even_odd_palindrome(123) == (8, 13)

    # Result should be a tuple
    assert isinstance(module_0.even_odd_palindrome(50), tuple)

    # Sum of counts equals total palindromes from 1..n
    even, odd = module_0.even_odd_palindrome(200)
    assert even + odd == 28  # 9 + 9 two-digit + 10 three-digit palindromes <= 200

# Generated at 2026-11-01 20:53:27.843714
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():assert module_0.even_odd_palindrome(1) == (0, 1)

# Generated at 2026-11-01 20:54:10.203855
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 1: only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 2: 1 (odd), 2 (even)
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # n = 3: 1, 3 odd palindromes; 2 even palindrome
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # n = 5: even: 2, 4; odd: 1, 3, 5
    assert module_0.even_odd_palindrome(5) == (2, 3)

    # n = 9: even: 2, 4, 6, 8; odd: 1, 3, 5, 7, 9
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 12: adds 11 (odd palindrome); 10, 12 are not palindromes
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 100: single digit palindromes (4 even, 5 odd) plus 11,22,...,99 (all odd counts? no: 22,44,66,88 even; 11,33,55,77,99 odd)
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # Edge case: n = 0, no numbers considered
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # Result is a tuple
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2

# Generated at 2026-11-01 20:54:43.021624
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Known expected values
    assert module_0.even_odd_palindrome(1) == (0, 1)      # only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(2) == (1, 1)      # 1 (odd), 2 (even)
    assert module_0.even_odd_palindrome(3) == (1, 2)      # 1, 3 odd; 2 even
    assert module_0.even_odd_palindrome(5) == (2, 3)      # 1,3,5 odd; 2,4 even
    assert module_0.even_odd_palindrome(9) == (4, 5)      # 1-9 all palindromes
    assert module_0.even_odd_palindrome(10) == (4, 5)     # 10 is not a palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)     # 11 is an odd palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)     # 12 is not a palindrome
    assert module_0.even_odd_palindrome(0) == (0, 0)      # empty range
    assert module_0.even_odd_palindrome(100) == (8, 10)   # even: 2,4,6,8,22,44,66,88; odd: 1,3,5,7,9,11,33,55,77,99

    # Cross-check against a brute-force reference for a range of inputs
    for n in range(0, 60):
        even = sum(1 for i in range(1, n + 1) if i % 2 == 0 and str(i) == str(i)[::-1])
        odd = sum(1 for i in range(1, n + 1) if i % 2 == 1 and str(i) == str(i)[::-1])
        assert module_0.even_odd_palindrome(n) == (even, odd), f"Failed for n={n}"

# Generated at 2026-11-01 20:55:18.977440
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Basic small input
    assert module_0.even_odd_palindrome(1) == (0, 1)      # 1 is an odd palindrome
    assert module_0.even_odd_palindrome(2) == (1, 1)      # adds 2 (even palindrome)
    assert module_0.even_odd_palindrome(3) == (1, 2)      # adds 3 (odd palindrome)

    # Single digits 1-9: even palindromes {2,4,6,8}, odd {1,3,5,7,9}
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # Two-digit palindromes 11..99 add 4 even (22,44,66,88) and 5 odd (11,33,55,77,99)
    assert module_0.even_odd_palindrome(10) == (4, 5)     # 10 is not a palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)     # 11 is an odd palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)     # 12 is not a palindrome
    assert module_0.even_odd_palindrome(22) == (5, 6)     # 22 is an even palindrome
    assert module_0.even_odd_palindrome(99) == (8, 10)    # all one/two-digit palindromes counted

    # Non-palindrome boundary values don't change counts
    assert module_0.even_odd_palindrome(100) == (8, 10)   # 100 is not a palindrome
    assert module_0.even_odd_palindrome(101) == (8, 11)   # 101 is an odd palindrome
    assert module_0.even_odd_palindrome(123) == (8, 13)   # adds 101, 111, 121 (all odd)

    # Edge cases
    assert module_0.even_odd_palindrome(0) == (0, 0)      # no numbers in range
    assert module_0.even_odd_palindrome(-5) == (0, 0)     # negative input -> empty range