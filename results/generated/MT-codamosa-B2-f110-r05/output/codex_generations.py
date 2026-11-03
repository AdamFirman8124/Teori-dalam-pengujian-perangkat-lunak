

# Generated at 2026-11-03 02:33:46.543103
# Unit test for function exchange
def test_exchange():
    # Basic examples: enough even numbers in lst2 to swap for odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"

    # lst1 already all even — no swaps needed
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # Single elements
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1, 3], [2]) == "NO"

    # Empty lists: zero odds, zero evens
    assert module_0.exchange([], []) == "YES"

    # All odd in lst1, exactly enough evens in lst2
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    # Not enough evens
    assert module_0.exchange([1, 3, 5], [1, 4, 6]) == "NO"

    # Zero is even
    assert module_0.exchange([1, 0], [0]) == "YES"

    # Negative numbers: -1 % 2 == 1 (odd), -2 % 2 == 0 (even) in Python
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3], [-2]) == "NO"

    # More evens in lst2 than odds in lst1
    assert module_0.exchange([1], [2, 4, 6]) == "YES"

# Generated at 2026-11-03 02:34:44.198128
# Unit test for function exchange
def test_exchange():
    # Basic YES case: enough even numbers in lst2 to swap for odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"

    # Basic NO case: not enough even numbers in lst2
    assert module_0.exchange([1, 3, 5], [1, 2]) == "NO"

    # lst1 has no odd numbers — no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # lst1 all odd, lst2 has enough evens
    assert module_0.exchange([1, 3], [2, 4, 6]) == "YES"

    # lst1 all odd, lst2 has no evens
    assert module_0.exchange([1, 3, 5], [1, 3, 5]) == "NO"

    # Exactly enough evens
    assert module_0.exchange([1, 3], [2, 5]) == "YES"

    # Empty lst1: zero odds needed
    assert module_0.exchange([], [1, 3]) == "YES"

    # Empty lst2: cannot swap any odds
    assert module_0.exchange([1], []) == "NO"

    # Both empty
    assert module_0.exchange([], []) == "YES"

    # Negative numbers: -3 is odd, -2 is even
    assert module_0.exchange([-3, 1], [-2, 3]) == "YES"
    assert module_0.exchange([-3, 1, 5], [-2]) == "NO"

    # Zero counts as even
    assert module_0.exchange([1], [0]) == "YES"

    # Larger uneven lists
    assert module_0.exchange([1, 3, 5, 7], [2, 4]) == "NO"
    assert module_0.exchange([1, 3], [2, 4, 6, 8]) == "YES"

test_exchange()

# Generated at 2026-11-03 02:35:49.362310
# Unit test for function exchange
def test_exchange():
# nonce:74a873c0
    # lst1 already all even
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    # enough even numbers in lst2 to swap out odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6]) == "YES"
    # not enough even numbers in lst2
    assert module_0.exchange([1, 3, 5], [2]) == "NO"
    # lst2 has no even numbers to offer
    assert module_0.exchange([1, 3], [1, 3, 5]) == "NO"
    # exactly equal counts
    assert module_0.exchange([1, 3], [2, 4]) == "YES"
    # empty lists
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([1], []) == "NO"
    assert module_0.exchange([], [2]) == "YES"
    # zero is even
    assert module_0.exchange([0, 1], [0]) == "YES"
    # negative numbers: -1 is odd, -2 is even
    assert module_0.exchange([-1, -3], [-2, 4]) == "YES"
    assert module_0.exchange([-1, -3], [-1]) == "NO"
    # large numbers
    assert module_0.exchange([1000001, 1000003], [1000000, 1000002]) == "YES"
    assert module_0.exchange([1000001], [1000001]) == "NO"

# Generated at 2026-11-03 02:36:38.434372
# Unit test for function exchange
def test_exchange():
    # Exchange possible: enough even numbers in lst2 to swap for odd numbers in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 5, 3, 7], [2, 4, 6, 8]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"

    # Exchange not possible: not enough even numbers in lst2
    assert module_0.exchange([1, 3, 5, 7], [1, 2, 3, 4]) == "NO"
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 7]) == "NO"
    assert module_0.exchange([1, 3], [1]) == "NO"

    # lst1 has no odd numbers - no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([0, 2, 4], []) == "YES"

    # lst2 has no even numbers
    assert module_0.exchange([1, 3], [1, 3, 5]) == "NO"
    assert module_0.exchange([], [1, 3]) == "YES"

    # Empty lists
    assert module_0.exchange([], []) == "YES"

    # Exact match: even count equals odd count
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # More even numbers than needed
    assert module_0.exchange([1], [2, 2, 2, 2]) == "YES"

    # Negative numbers: negative odds are odd, negative evens are even
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3, -5], [-2]) == "NO"
    assert module_0.exchange([-2, -4], [-1, -3]) == "YES"

    # Zero is even
    assert module_0.exchange([1, 3], [0, 0]) == "YES"
    assert module_0.exchange([1, 3, 5], [0]) == "NO"

# Generated at 2026-11-03 02:37:24.863637
# Unit test for function exchange
def test_exchange():
    # lst1 already all even — no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # lst1 has odd numbers, lst2 has enough evens to swap
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"

    # equal number of odds in lst1 and evens in lst2
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # more odds in lst1 than evens in lst2 — cannot fix
    assert module_0.exchange([1, 3, 5], [2]) == "NO"

    # lst2 has no even numbers to offer
    assert module_0.exchange([1, 2], [1, 3, 5]) == "NO"

    # empty lst1 — trivially satisfiable
    assert module_0.exchange([], [1, 2, 3]) == "YES"

    # empty lst2 but lst1 needs exchanges
    assert module_0.exchange([1, 3], []) == "NO"

    # both empty
    assert module_0.exchange([], []) == "YES"

    # negative numbers: -1 % 2 == 1 (odd), -2 % 2 == 0 (even)
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3, -5], [-2]) == "NO"

    # zero counts as even
    assert module_0.exchange([0, 2], [1]) == "YES"
    assert module_0.exchange([1], [0]) == "YES"

    # single element lists
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [3]) == "NO"

    # larger mixed case
    assert module_0.exchange([1, 2, 3, 5, 7], [2, 4, 6, 8, 10]) == "YES"
    assert module_0.exchange([1, 2, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == "NO"

    print("All test_exchange tests passed!")


if __name__ == "__main__":
    test_exchange()