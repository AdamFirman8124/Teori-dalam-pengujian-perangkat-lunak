

# Generated at 2026-11-02 18:01:14.169301
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Basic small cases
    assert module_0.even_odd_palindrome(1) == (0, 1), "Test n=1 failed"
    assert module_0.even_odd_palindrome(3) == (1, 2), "Test n=3 failed"
    assert module_0.even_odd_palindrome(9) == (4, 5), "Test n=9 failed"
    assert module_0.even_odd_palindrome(12) == (4, 6), "Test n=12 failed"

    # Larger cases
    assert module_0.even_odd_palindrome(100) == (8, 10), "Test n=100 failed"
    assert module_0.even_odd_palindrome(123) == (8, 13), "Test n=123 failed"

    # Edge cases
    assert module_0.even_odd_palindrome(0) == (0, 0), "Test n=0 failed"
    assert module_0.even_odd_palindrome(-5) == (0, 0), "Test negative n failed"

    # Verify return type is a tuple of two ints
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2, "Return type failed"
    even_count, odd_count = result
    assert even_count + odd_count == 17, "Total palindrome count for n=50 failed"

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()

# Generated at 2026-11-02 18:03:48.407039
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # n = 0: no numbers to check
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # n = 1: only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # n = 2: 1 (odd), 2 (even)
    assert module_0.even_odd_palindrome(2) == (1, 1)

    # n = 9: single digits 1-9, odd: 1,3,5,7,9 (5), even: 2,4,6,8 (4)
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 12: adds 11 (odd palindrome)
    assert module_0.even_odd_palindrome(12) == (4, 6)

    # n = 22: adds 22 (even palindrome)
    assert module_0.even_odd_palindrome(22) == (5, 6)

    # n = 100: 1-9, 11,22,...,99 -> even: 2,4,6,8,22,44,66,88 (8), odd: 1,3,5,7,9,11,33,55,77,99 (10)
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # n = 123: adds 101, 111 (odd), 121 (odd)
    assert module_0.even_odd_palindrome(123) == (8, 13)

    # Ensure result is a tuple of two integers
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2
    assert isinstance(result[0], int) and isinstance(result[1], int)

    # Sum of counts should equal total number of palindromes up to n
    even_count, odd_count = module_0.even_odd_palindrome(200)
    total_palindromes = sum(1 for i in range(1, 201) if str(i) == str(i)[::-1])
    assert even_count + odd_count == total_palindromes

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()

# Generated at 2026-11-02 18:05:26.383140
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

    # n = 5: odd palindromes 1,3,5; even palindromes 2,4
    assert module_0.even_odd_palindrome(5) == (2, 3)

    # n = 9: single digits 1-9 (5 odd, 4 even)
    assert module_0.even_odd_palindrome(9) == (4, 5)

    # n = 10: 10 is not a palindrome, count unchanged
    assert module_0.even_odd_palindrome(10) == (4, 5)

    # n = 11: 11 is an odd palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)

    # n = 22: 22 is an even palindrome (11, 22 both palindromic)
    assert module_0.even_odd_palindrome(22) == (5, 6)

    # n = 100: single-digit (4 even, 5 odd) + two-digit palindromes
    # 22,44,66,88 (4 even) and 11,33,55,77,99 (5 odd); 100 not a palindrome
    assert module_0.even_odd_palindrome(100) == (8, 10)

    # Return type is a tuple
    assert isinstance(module_0.even_odd_palindrome(10), tuple)

# Generated at 2026-11-02 18:07:22.894981
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(2) == (1, 1)
    assert module_0.even_odd_palindrome(9) == (4, 5)
    assert module_0.even_odd_palindrome(10) == (4, 5)
    assert module_0.even_odd_palindrome(11) == (4, 6)
    assert module_0.even_odd_palindrome(12) == (4, 6)
    assert module_0.even_odd_palindrome(22) == (5, 6)
    assert module_0.even_odd_palindrome(100) == (8, 12)
    assert module_0.even_odd_palindrome(123) == (8, 13)
    assert module_0.even_odd_palindrome(0) == (0, 0)
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2
    print("All tests passed!")

test_even_odd_palindrome()

# Generated at 2026-11-02 18:08:57.071201
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Edge cases
    assert module_0.even_odd_palindrome(0) == (0, 0)
    assert module_0.even_odd_palindrome(1) == (0, 1)      # only 1 (odd palindrome)
    assert module_0.even_odd_palindrome(2) == (1, 1)      # 1 odd, 2 even
    assert module_0.even_odd_palindrome(3) == (1, 2)

    # Known values
    assert module_0.even_odd_palindrome(9) == (4, 5)      # 1-9 all palindromes
    assert module_0.even_odd_palindrome(10) == (4, 5)     # 10 not a palindrome
    assert module_0.even_odd_palindrome(11) == (4, 6)     # 11 is odd palindrome
    assert module_0.even_odd_palindrome(12) == (4, 6)
    assert module_0.even_odd_palindrome(99) == (8, 10)    # 11,33,55,77,99 odd; 22,44,66,88 even
    assert module_0.even_odd_palindrome(100) == (8, 10)   # 100 not a palindrome
    assert module_0.even_odd_palindrome(123) == (8, 13)   # + 101,111,121 (odd)
    assert module_0.even_odd_palindrome(1000) == (48, 60)


def test_even_odd_palindrome_matches_brute_force():
    import random

    def brute_force(n):
        even = odd = 0
        for i in range(1, n + 1):
            if str(i) == str(i)[::-1]:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return (even, odd)

    random.seed(42)
    for _ in range(100):
        n = random.randint(0, 500)
        assert module_0.even_odd_palindrome(n) == brute_force(n), f"Mismatch for n={n}"


def test_even_odd_palindrome_counts_sum():
    # Even + odd counts must equal total number of palindromes in range
    for n in range(0, 200):
        even, odd = module_0.even_odd_palindrome(n)
        total = sum(1 for i in range(1, n + 1) if str(i) == str(i)[::-1])
        assert even + odd == total
        assert even >= 0 and odd >= 0