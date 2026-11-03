

# Generated at 2026-11-02 15:42:44.491873
# Unit test for function exchange
def test_exchange():
    # All even in lst1 -> no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([], []) == "YES"

    # Odd count in lst1 <= even count in lst2 -> YES
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"
    assert module_0.exchange([1, 2, 3], [2, 4]) == "YES"
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1, 3], [2, 4, 6]) == "YES"

    # Odd count in lst1 > even count in lst2 -> NO
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    assert module_0.exchange([1, 3], [2]) == "NO"
    assert module_0.exchange([1], []) == "NO"
    assert module_0.exchange([1, 2, 3, 5], [4, 6, 8]) == "NO"

    # Zero counts as even
    assert module_0.exchange([1], [0]) == "YES"
    assert module_0.exchange([0], [1]) == "YES"

    # Negative numbers: -1 is odd, -2 is even
    assert module_0.exchange([-1], [-2]) == "YES"
    assert module_0.exchange([-1, -3], [-2]) == "NO"
    assert module_0.exchange([-2, -4], [1]) == "YES"

    # Exact equality of counts -> YES
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"

    print("All test_exchange tests passed!")


test_exchange()

# Generated at 2026-11-02 15:45:02.370258
# Unit test for function exchange
def test_exchange():
    # Case 1: lst1 has no odd numbers -> always "YES"
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([], [1, 2, 3]) == "YES"

    # Case 2: enough even numbers in lst2 to cover odd numbers in lst1
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"

    # Case 3: equal counts -> "YES" (even >= odd)
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # Case 4: not enough even numbers in lst2 -> "NO"
    assert module_0.exchange([1, 3, 5], [2]) == "NO"
    assert module_0.exchange([1, 2, 3], [4, 5, 6]) == "NO"

    # Case 5: both lists empty
    assert module_0.exchange([], []) == "YES"

    # Case 6: lst1 empty but lst2 has no evens either
    assert module_0.exchange([], [1, 3]) == "YES"

    # Case 7: zero counts as even
    assert module_0.exchange([1], [0]) == "YES"
    assert module_0.exchange([1, 3], [0]) == "NO"

    # Case 8: negative numbers (Python: -3 % 2 == 1, -2 % 2 == 0)
    assert module_0.exchange([-3, -5], [-2, -4]) == "YES"
    assert module_0.exchange([-3, -5, -7], [-2]) == "NO"

    # Case 9: mixed values
    assert module_0.exchange([1, 2, 3, 5], [2, 4, 6, 8, 10]) == "YES"
    assert module_0.exchange([7, 9, 11, 13], [2, 3, 5]) == "NO"

    # Case 10: large lists
    assert module_0.exchange(list(range(1, 101, 2)), list(range(0, 100, 2))) == "YES"
    assert module_0.exchange(list(range(1, 101, 2)), [0]) == "NO"

    print("All test_exchange tests passed!")


if __name__ == "__main__":
    test_exchange()

# Generated at 2026-11-02 15:47:22.953976
# Unit test for function exchange
def test_exchange():
    # All even in lst1 -> trivially YES
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    # Equal counts of odd in lst1 and even in lst2 -> YES
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    # More odds in lst1 than evens in lst2 -> NO
    assert module_0.exchange([1, 5, 3, 0, 2, 7, 9], [2, 6, 4]) == "NO"
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    # Enough evens in lst2 to cover odds in lst1 -> YES
    assert module_0.exchange([1, 1], [2, 2, 2]) == "YES"
    assert module_0.exchange([1, 3], [2, 4, 6, 8]) == "YES"
    # Empty lists
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([], [2, 4]) == "YES"
    assert module_0.exchange([1], []) == "NO"
    # Zero is even
    assert module_0.exchange([0], [1]) == "YES"
    assert module_0.exchange([0, 1], [0, 2]) == "YES"
    # Negative numbers: odd negatives count as odd, even negatives as even
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3, -5], [-2]) == "NO"
    # Single element cases
    assert module_0.exchange([2], [1]) == "YES"
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [1]) == "NO"

test_exchange()

# Generated at 2026-11-02 15:48:58.708437
# Unit test for function exchange
def test_exchange():
    # Odd count in lst1 <= even count in lst2 -> "YES"
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    # Not enough evens in lst2 -> "NO"
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert module_0.exchange([1, 2, 3, 4], [2, 1, 4, 5]) == "YES"
    # Empty lists: 0 odd, 0 even -> "YES"
    assert module_0.exchange([], []) == "YES"
    # All odd in lst1, enough evens in lst2
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    # Too few evens in lst2
    assert module_0.exchange([1, 3, 5], [2]) == "NO"
    # lst1 all even -> always "YES"
    assert module_0.exchange([2, 4, 6], []) == "YES"
    assert module_0.exchange([2, 4, 6], [1, 3]) == "YES"
    # Single elements
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [3]) == "NO"
    # Zero is even
    assert module_0.exchange([0], []) == "YES"
    assert module_0.exchange([0, 1], []) == "NO"
    # Negative numbers: -1 % 2 == 1 (odd), -2 % 2 == 0 (even)
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -2], [3]) == "NO"
    # Equal counts -> "YES" (even >= odd)
    assert module_0.exchange([1, 3], [2, 4]) == "YES"