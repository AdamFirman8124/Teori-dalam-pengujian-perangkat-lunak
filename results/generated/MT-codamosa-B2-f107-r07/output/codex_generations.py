

# Generated at 2026-10-25 01:28:02.659447
# Unit test for function even_odd_palindrome

# Generated at 2026-10-25 01:28:05.193199
# Unit test for function even_odd_palindrome

# Generated at 2026-10-25 01:28:07.716075
# Unit test for function even_odd_palindrome

# Generated at 2026-10-25 01:28:10.131745
# Unit test for function even_odd_palindrome

# Generated at 2026-10-25 01:28:12.546895
# Unit test for function even_odd_palindrome

# Generated at 2026-10-25 01:28:14.961886
# Unit test for function even_odd_palindrome

# Generated at 2026-10-25 01:28:22.104159
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    # Test case 1: n = 1
    # Only palindrome in range [1, 1] is 1 (odd)
    assert module_0.even_odd_palindrome(1) == (0, 1)

    # Test case 2: n = 12
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9 (odd), 11 (odd)
    assert module_0.even_odd_palindrome(12) == (0, 10)

    # Test case 3: n = 22
    # Adds 22 (even) to the previous count
    assert module_0.even_odd_palindrome(22) == (1, 10)

    # Test case 4: n = 100
    # Odd palindromes: 1-9, 11, 33, 55, 77, 99 -> 14
    # Even palindromes: 22, 44, 66, 88 -> 4
    assert module_0.even_odd_palindrome(100) == (4, 14)

    # Test case 5: n = 9
    # Single-digit palindromes 1-9, all odd
    assert module_0.even_odd_palindrome(9) == (0, 9)

    # Test case 6: n = 10
    # Same as n = 9, since 10 is not a palindrome
    assert module_0.even_odd_palindrome(10) == (0, 9)

    # Test case 7: n = 0 (empty range)
    assert module_0.even_odd_palindrome(0) == (0, 0)

    # Test case 8: verify tuple structure and order
    result = module_0.even_odd_palindrome(50)
    assert isinstance(result, tuple) and len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_palindrome()

# Generated at 2026-10-25 01:28:23.439302
# Unit test for function even_odd_palindrome

# Generated at 2026-10-25 01:28:24.765501
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(9) == (0, 5)
    assert module_0.even_odd_palindrome(12) == (1, 5)
    assert module_0.even_odd_palindrome(100) == (9, 9)
    assert module_0.even_odd_palindrome(0) == (0, 0)

# Generated at 2026-10-25 01:28:26.211258
# Unit test for function even_odd_palindrome

# Generated at 2026-10-25 01:28:27.533241
# Unit test for function even_odd_palindrome
def test_even_odd_palindrome():
    assert module_0.even_odd_palindrome(1) == (0, 1)
    assert module_0.even_odd_palindrome(9) == (0, 5)
    assert module_0.even_odd_palindrome(12) == (1, 5)
    assert module_0.even_odd_palindrome(100) == (9, 9)
    assert module_0.even_odd_palindrome(0) == (0, 0)