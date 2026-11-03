

# Generated at 2026-11-01 23:16:42.482950
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Single digit case
    assert module_0.even_odd_palindrome(1) == (0, 1)
    # All single-digit numbers: evens 2,4,6,8; odds 1,3,5,7,9
    assert module_0.even_odd_palindrome(9) == (4, 5)
    # Includes non-palindrome 10 and palindrome 11
    assert module_0.even_odd_palindrome(12) == (4, 6)
    # Includes even palindrome 22
    assert module_0.even_odd_palindrome(22) == (5, 6)
    # Zero boundary - no numbers considered
    assert module_0.even_odd_palindrome(0) == (0, 0)
    # Larger mixed case
    assert module_0.even_odd_palindrome(123) == (8, 13)


if __name__ == "__main__":
    test_even_odd_palindrome()
    print("All tests passed!")

# Generated at 2026-11-01 23:17:20.883392
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Basic cases
    assert module_0.even_odd_palindrome(1) == (0, 1)      # only 1 is an odd palindrome
    assert module_0.even_odd_palindrome(3) == (1, 2)      # 1,3 odd palindromes; 2 even
    assert module_0.even_odd_palindrome(9) == (4, 5)      # 2,4,6,8 even; 1,3,5,7,9 odd
    assert module_0.even_odd_palindrome(12) == (4, 6)     # adds 11 as odd palindrome
    assert module_0.even_odd_palindrome(19) == (4, 6)
    assert module_0.even_odd_palindrome(25) == (5, 6)     # adds 22 as even palindrome
    assert module_0.even_odd_palindrome(63) == (6, 8)
    assert module_0.even_odd_palindrome(123) == (8, 13)   # includes 101, 111, 121

    # Edge cases
    assert module_0.even_odd_palindrome(0) == (0, 0)      # no numbers in range
    assert module_0.even_odd_palindrome(-5) == (0, 0)     # negative input yields no iterations

    # Verify tuple structure
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2
    assert result[0] >= 0 and result[1] >= 0

    print("All tests passed!")

# Generated at 2026-11-01 23:17:57.143541
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 1: only palindrome is 1 (odd)
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 2: palindromes 1 (odd), 2 (even)
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # n = 3: palindromes 1, 2, 3 -> one even, two odd
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # n = 12: single-digit palindromes 1-9 plus 11
    # even: 2, 4, 6, 8 -> 4 ; odd: 1, 3, 5, 7, 9, 11 -> 6
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 100: single digits + two-digit palindromes 11..99 (all odd)
    # even: 2, 4, 6, 8 -> 4 ; odd: 1,3,5,7,9 + 11..99 -> 5 + 9 = 14
    assert module_0.even_odd_palindrome(100) == (4, 14)

    # n = 0: no numbers checked
    assert module_0.even_odd_palindrome(0) == (0, 0)

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()

# Generated at 2026-11-01 23:18:41.166491
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # nonce:1b2f7a90
    # Edge case: no numbers checked
    assert module_0.even_odd_palindrome(0) == (0, 0), "Expected (0, 0) for n=0"

    # Smallest input: only 1, an odd palindrome
    assert module_0.even_odd_palindrome(1) == (0, 1), "Expected (0, 1) for n=1"

    # Single-digit numbers 1-9: 5 odd palindromes, 4 even palindromes
    assert module_0.even_odd_palindrome(9) == (4, 5), "Expected (4, 5) for n=9"

    # 10 is not a palindrome, so result unchanged from n=9
    assert module_0.even_odd_palindrome(10) == (4, 5), "Expected (4, 5) for n=10"

    # 11 is an odd palindrome: odd count becomes 6
    assert module_0.even_odd_palindrome(11) == (4, 6), "Expected (4, 6) for n=11"

    # Example from problem statement
    assert module_0.even_odd_palindrome(12) == (4, 6), "Expected (4, 6) for n=12"

    # Up to 100: even palindromes {2,4,6,8,22,44,66,88} -> 8,
    #             odd palindromes {1,3,5,7,9,11,33,55,77,99} -> 10
    assert module_0.even_odd_palindrome(100) == (8, 10), "Expected (8, 10) for n=100"

    # Cross-check against an independent brute-force computation
    def reference(n):
        evens = odds = 0
        for i in range(1, n + 1):
            if str(i) == str(i)[::-1]:
                if i % 2 == 0:
                    evens += 1
                else:
                    odds += 1
        return (evens, odds)

    for n in [0, 1, 2, 13, 50, 121, 999]:
        assert module_0.even_odd_palindrome(n) == reference(n), f"Mismatch at n={n}"

    print("All tests passed!")


test_even_odd_palindrome()

# Generated at 2026-11-01 23:19:19.262912
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Basic cases
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(3) == (1, 2)
    assert module_0.even_odd_palindrome(12) == (4, 6)
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # Edge cases
    assert module_0.even_odd_palindrome(0) == (0, 0)
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # Palindromes up to 21: 1-9 (odd:5, even:4), 11 (odd), 22 (even)
    assert module_0.even_odd_palindrome(21) == (4, 6)
    assert module_0.even_odd_palindrome(22) == (5, 6)

    # Larger case check against manual computation
    # Palindromes up to 999:
    #   1-digit: odd 5, even 4
    #   2-digit: odd 5 (11,33,55,77,99), even 4 (22,44,66,88)
    #   3-digit: aba where a in 1-9, b in 0-9 -> parity determined by last digit a
    #     odd when a odd: 5*10 = 50; even when a even: 4*10 = 40
    total_even = 4 + 4 + 40
    total_odd = 5 + 5 + 50
    assert module_0.even_odd_palindrome(999) == (total_even, total_odd)

    print("All tests passed!")


test_even_odd_palindrome()