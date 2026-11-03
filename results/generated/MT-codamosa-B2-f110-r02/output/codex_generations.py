

# Generated at 2026-11-03 04:54:17.556092
# Unit test for function exchange
def test_exchange():
    # Both lists have enough evens to swap out odds
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 2, 3], [1, 5, 3, 4]) == "NO"
    assert module_0.exchange([1, 2, 3, 4], [2, 4]) == "YES"

    # Edge cases with empty lists
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([1], []) == "NO"
    assert module_0.exchange([2], []) == "YES"

    # All even in lst1 (no exchange needed)
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([], [1, 3, 5]) == "YES"

    # Not enough evens in lst2
    assert module_0.exchange([1, 3, 5], [2]) == "NO"
    assert module_0.exchange([1, 3], [2, 4, 6]) == "YES"

    # Zero counts as even
    assert module_0.exchange([0, 2], [1]) == "YES"
    assert module_0.exchange([1], [0]) == "YES"

    # Negative numbers: -1 % 2 == 1 (odd), -2 % 2 == 0 (even)
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3], [-1]) == "NO"

    # Larger counts
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8]) == "YES"
    assert module_0.exchange([1, 3, 5, 7, 9], [2, 4, 6, 8]) == "NO"

    print("All test_exchange tests passed!")


if __name__ == "__main__":
    test_exchange()

# Generated at 2026-11-03 04:56:03.472022
# Unit test for function exchange
def test_exchange():
    # lst1 has all even numbers -> no exchange needed -> YES
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # lst1 has odd numbers, lst2 has enough even numbers to cover them -> YES
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"

    # lst1 has odd numbers, lst2 lacks enough even numbers -> NO
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"

    # exact equal count of odd in lst1 and even in lst2 -> YES
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # one more even in lst2 than odd in lst1 -> YES
    assert module_0.exchange([1, 3, 5], [2, 4, 6, 8]) == "YES"

    # lst2 has no even numbers and lst1 has odd numbers -> NO
    assert module_0.exchange([1], [1, 3, 5]) == "NO"

    # empty lst1 -> zero odd count -> YES
    assert module_0.exchange([], [1, 3]) == "YES"

    # both lists empty -> YES
    assert module_0.exchange([], []) == "YES"

    # negative numbers: -3 is odd, -2 is even
    assert module_0.exchange([-3, -5], [-2, -4]) == "YES"
    assert module_0.exchange([-3, -5, -7], [-2]) == "NO"

    # zero is even in lst2
    assert module_0.exchange([1], [0]) == "YES"

    # mixed case: more even in lst2 than odd in lst1
    assert module_0.exchange([1, 2, 3], [2, 4, 6, 8, 10]) == "YES"

    print("test_exchange: all tests passed")


if __name__ == "__main__":
    test_exchange()

# Generated at 2026-11-03 04:58:49.710286
# Unit test for function exchange
def test_exchange():
    # Enough even numbers in lst2 to exchange for all odd numbers in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    # Not enough even numbers in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    # Exactly enough even numbers
    assert module_0.exchange([1, 3], [2, 4]) == "YES"
    # No odd numbers in lst1 (nothing to exchange)
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    # All odd in lst1, all even in lst2
    assert module_0.exchange([1, 3, 5], [2, 4, 6, 8]) == "YES"
    # All odd in lst1, no even in lst2
    assert module_0.exchange([1, 3, 5], [1, 3, 5]) == "NO"
    # Empty lst1 (no odd numbers to exchange)
    assert module_0.exchange([], [1, 2, 3]) == "YES"
    # Empty lst2 with odd numbers in lst1
    assert module_0.exchange([1, 3], []) == "NO"
    # Both lists empty
    assert module_0.exchange([], []) == "YES"
    # Even == odd count boundary case
    assert module_0.exchange([1, 2, 3], [4, 5, 6]) == "YES"
    # One more odd than even available
    assert module_0.exchange([1, 3, 5], [2, 4, 7]) == "NO"
    # Negative numbers: -1 is odd, -2 is even
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3, -5], [-2]) == "NO"
    # Zero is even
    assert module_0.exchange([1], [0]) == "YES"
    # Duplicates
    assert module_0.exchange([1, 1, 1], [2, 2, 2]) == "YES"
    assert module_0.exchange([1, 1, 1], [2, 2]) == "NO"

if __name__ == "__main__":
    test_exchange()
    print("All tests passed!")