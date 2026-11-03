

# Generated at 2026-11-02 23:08:31.097707
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
# nonce:7a6cc791
    # Single-digit numbers: all are palindromes
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(2) == (1, 1)
    assert module_0.even_odd_palindrome(3) == (1, 2)
    assert module_0.even_odd_palindrome(4) == (2, 2)
    assert module_0.even_odd_palindrome(5) == (2, 3)
    assert module_0.even_odd_palindrome(6) == (3, 3)
    assert module_0.even_odd_palindrome(7) == (3, 4)
    assert module_0.even_odd_palindrome(8) == (4, 4)
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # 10 is not a palindrome, 11 is (odd)
    assert module_0.even_odd_palindrome(10) == (4, 5)
    assert module_0.even_odd_palindrome(11) == (4, 6)
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # Larger range: two-digit palindromes 11..99 plus 101, 111, 121
    assert module_0.even_odd_palindrome(22) == (5, 6)
    assert module_0.even_odd_palindrome(99) == (8, 10)
    assert module_0.even_odd_palindrome(100) == (8, 10)
    assert module_0.even_odd_palindrome(123) == (8, 13)

    # Edge cases: empty range
    assert module_0.even_odd_palindrome(0) == (0, 0)
    assert module_0.even_odd_palindrome(-5) == (0, 0)

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()

# Generated at 2026-11-02 23:11:06.909198
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(2) == (1, 1)
    assert module_0.even_odd_palindrome(3) == (1, 2)
    assert module_0.even_odd_palindrome(4) == (2, 2)
    assert module_0.even_odd_palindrome(5) == (2, 3)
    assert module_0.even_odd_palindrome(6) == (3, 3)
    assert module_0.even_odd_palindrome(7) == (3, 4)
    assert module_0.even_odd_palindrome(8) == (4, 4)
    assert module_0.even_odd_palindrome(9) == (4, 5)
    assert module_0.even_odd_palindrome(12) == (4, 6)
    assert module_0.even_odd_palindrome(22) == (5, 6)
    assert module_0.even_odd_palindrome(100) == (8, 10)
    assert module_0.even_odd_palindrome(123) == (8, 13)
    assert module_0.even_odd_palindrome(0) == (0, 0)
    print("All tests passed!")

test_even_odd_palindrome()

# Generated at 2026-11-02 23:13:12.598035
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 1: only palindrome is 1 (odd)
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 3: palindromes are 1, 2, 3 -> odd: 1,3 (2), even: 2 (1)
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # n = 9: 1-9 are all palindromes -> odd: 1,3,5,7,9 (5), even: 2,4,6,8 (4)
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 10: 10 is not a palindrome, same as n = 9
    assert module_0.even_odd_palindrome(10) == (4, 5)

    # n = 12: adds 11 (odd palindrome); 12 is not a palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 22: adds 22 (even palindrome)
    assert module_0.even_odd_palindrome(22) == (5, 6)

    # n = 0: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # n = 99: all two-digit palindromes 11..99
    # odd palindromes: 11,33,55,77,99 -> 5 (plus 1,3,5,7,9 = 5) => 10
    # even palindromes: 22,44,66,88 -> 4 (plus 2,4,6,8 = 4) => 8
    assert module_0.even_odd_palindrome(99) == (8, 10)

    # n = 100: 100 is not a palindrome, same as n = 99
    assert module_0.even_odd_palindrome(100) == (8, 10)

    print("All tests passed!")


test_even_odd_palindrome()

# Generated at 2026-11-02 23:14:51.209069
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 0: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)
    # n = 1: only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(1) == (0, 1)
    # n = 3: 1, 3 odd palindromes; 2 even palindrome
    assert module_0.even_odd_palindrome(3) == (1, 2)
    # n = 9: single digit palindromes 1-9
    assert module_0.even_odd_palindrome(9) == (4, 5)
    # n = 10: 10 is not a palindrome
    assert module_0.even_odd_palindrome(10) == (4, 5)
    # n = 11: 11 is an odd palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)
    # n = 12: 12 is not a palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)
    # n = 22: 22 is an even palindrome
    assert module_0.even_odd_palindrome(22) == (5, 6)
    # n = 100: palindromes 1-9, 11-99 (all two-digit palindromes)
    assert module_0.even_odd_palindrome(100) == (8, 10)
    # n = 123: adds 101, 111, 121 (odd palindromes)
    assert module_0.even_odd_palindrome(123) == (8, 13)