

# Generated at 2026-11-02 15:08:10.196289
# Unit test for function exchange
def test_exchange():
    # nonce:0d5b8014
    # Equal counts of odds in lst1 and evens in lst2
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    # Not enough even numbers in lst2 to replace odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    # More even numbers in lst2 than odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [2, 1, 2, 2, 1]) == "YES"
    # Single odd can be exchanged
    assert module_0.exchange([1], [2]) == "YES"
    # No even number available to exchange
    assert module_0.exchange([1], [1]) == "NO"
    # Empty lists
    assert module_0.exchange([], []) == "YES"
    # lst1 has no odd numbers, no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    # All odd in lst1, only one even in lst2
    assert module_0.exchange([1, 3, 5, 7], [2]) == "NO"
    # Even count exactly matches odd count
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    # Negative numbers: -3 is odd, -2 is even
    assert module_0.exchange([-3, -1], [-2, -4]) == "YES"
    assert module_0.exchange([-3, -1], [-1, -5]) == "NO"

# Generated at 2026-11-02 15:10:39.547373
# Unit test for function exchange
def test_exchange():
    # lst1 has odds, lst2 has enough evens to swap
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 5, 3], [2, 4, 6]) == "YES"
    # lst1 has more odds than lst2 has evens
    assert module_0.exchange([1, 3, 5], [1, 2, 3]) == "NO"
    assert module_0.exchange([1, 3], [2]) == "NO"
    # lst1 all even, no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 7]) == "YES"
    # equal counts of odds in lst1 and evens in lst2
    assert module_0.exchange([1, 3], [2, 4]) == "YES"
    # empty lists
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([1], []) == "NO"
    assert module_0.exchange([], [2]) == "YES"
    # zero is even
    assert module_0.exchange([1], [0]) == "YES"
    # negative numbers: -1 % 2 == 1 (odd), -2 % 2 == 0 (even)
    assert module_0.exchange([-1, -3], [2, 4]) == "YES"
    assert module_0.exchange([-2, -4], [1]) == "YES"
    assert module_0.exchange([-1, 1, 3], [-2]) == "NO"
    # mixed cases
    assert module_0.exchange([1, 2, 3], [4, 5, 6]) == "YES"
    assert module_0.exchange([7, 9, 11], [8]) == "NO"

test_exchange()
print("All tests passed!")

# Generated at 2026-11-02 15:12:12.727693
# Unit test for function exchange
def test_exchange():
    # All elements in lst1 are even -> no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    
    # Single odd in lst1, enough even in lst2
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"
    
    # More odds in lst1 than evens in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    
    # Equal counts -> exchange possible
    assert module_0.exchange([1, 3], [2, 4]) == "YES"
    
    # Empty lst1 -> trivially yes
    assert module_0.exchange([], [1, 2, 3]) == "YES"
    
    # Empty lst2, lst1 has odds -> cannot exchange
    assert module_0.exchange([1, 2], []) == "NO"
    
    # Both empty
    assert module_0.exchange([], []) == "YES"
    
    # lst1 all odd, lst2 all even
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8]) == "YES"
    
    # lst1 all odd, lst2 all odd
    assert module_0.exchange([1, 3], [1, 3]) == "NO"
    
    # Zero is even
    assert module_0.exchange([1], [0]) == "YES"
    
    # Negative numbers: -1 is odd, -2 is even
    assert module_0.exchange([-1], [-2]) == "YES"
    assert module_0.exchange([-1, -3], [-2]) == "NO"
    
    # Large numbers
    assert module_0.exchange([1000001], [1000000]) == "YES"
    
    # Mixed case with exact match
    assert module_0.exchange([2, 1, 4], [3, 5, 6, 7]) == "YES"
    
    # One odd needs one even, but lst2 has none
    assert module_0.exchange([1], [3]) == "NO"

# Generated at 2026-11-02 15:13:58.704834
# Unit test for function exchange
def test_exchange():
    # lst1 already all even -> YES
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    
    # lst1 has odds, lst2 has enough evens to swap -> YES
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 5, 7], [2, 4, 6]) == "YES"
    
    # lst1 has more odds than lst2 has evens -> NO
    assert module_0.exchange([1, 3, 5], [1, 2, 3]) == "NO"
    assert module_0.exchange([1, 3], [2]) == "NO"
    assert module_0.exchange([1], [1, 3, 5]) == "NO"
    
    # equal counts -> YES
    assert module_0.exchange([1, 3], [2, 4]) == "YES"
    
    # empty lists -> YES (no odds to fix)
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([], [1, 3]) == "YES"
    assert module_0.exchange([1, 3], []) == "NO"
    
    # zero is even, negatives work with modulo
    assert module_0.exchange([0, 1], [2, -4]) == "YES"
    assert module_0.exchange([-1, -3], [-2, 4, 6]) == "YES"
    assert module_0.exchange([-1], [1]) == "NO"
    
    # larger lists
    assert module_0.exchange([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == "YES"
    assert module_0.exchange([1, 3, 5, 7, 9], [2, 4]) == "NO"

# Generated at 2026-11-02 15:15:56.467359
# Unit test for function exchange
def test_exchange():
    # lst1 already all even -> YES
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # enough even numbers in lst2 to swap for odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"

    # exactly as many even numbers in lst2 as odds in lst1
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # not enough even numbers in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"

    # no even numbers in lst2 at all
    assert module_0.exchange([1, 2], [1, 3]) == "NO"

    # empty lst1 -> always YES
    assert module_0.exchange([], [1, 3]) == "YES"

    # both empty -> YES
    assert module_0.exchange([], []) == "YES"

    # zero counts as even in lst2
    assert module_0.exchange([1], [0]) == "YES"

    # negative odd/even handling
    assert module_0.exchange([-1, -3], [2, 4]) == "YES"
    assert module_0.exchange([-1, -3, -5], [2]) == "NO"
    assert module_0.exchange([-2, -4], [1]) == "YES"

    # mixed values with duplicates
    assert module_0.exchange([1, 1, 1], [2, 2, 2]) == "YES"
    assert module_0.exchange([1, 1, 1], [2, 2]) == "NO"