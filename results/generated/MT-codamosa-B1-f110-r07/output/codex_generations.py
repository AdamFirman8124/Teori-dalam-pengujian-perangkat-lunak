

# Generated at 2026-10-25 06:53:59.231945
# Unit test for function exchange

# Generated at 2026-10-25 06:54:01.836177
# Unit test for function exchange

# Generated at 2026-10-25 06:54:06.980818
# Unit test for function exchange
def test_exchange():
    # lst1 has 1 odd element, lst2 has 2 even elements -> enough evens to swap
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    # lst1 has 2 odd elements, lst2 has 1 even element -> not enough evens
    assert module_0.exchange([1, 2, 3], [4, 5, 6]) == "NO"
    # lst1 already all even -> YES regardless of lst2
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    # lst1 all odd, lst2 all even -> YES
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    # empty lst1 needs no swaps -> YES
    assert module_0.exchange([], [1, 3]) == "YES"
    # counts equal: 1 odd in lst1, 1 even in lst2 -> YES
    assert module_0.exchange([1], [2]) == "YES"
    # negative numbers: -3 is odd, 0 is even
    assert module_0.exchange([-3, 4], [0]) == "YES"
    assert module_0.exchange([-3, -5], [0, 6, 8]) == "YES"
    assert module_0.exchange([-3, -5, 7], [2]) == "NO"

# Generated at 2026-10-25 06:54:08.413674
# Unit test for function exchange
def test_exchange():
    # Enough even numbers in lst2 to swap for all odd numbers in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"   # 2 odds, 2 evens
    assert module_0.exchange([1, 5, 3, 7], [2, 4, 6, 8]) == "YES"   # 4 odds, 4 evens
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"    # 2 odds, only 1 even
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"         # 0 odds needed
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"         # exact match 3 vs 3
    assert module_0.exchange([], []) == "YES"                       # nothing to exchange

test_exchange()
print("All tests passed.")

# Generated at 2026-10-25 06:54:09.852609
# Unit test for function exchange
def test_exchange():
    # Enough even numbers in lst2 to swap for all odd numbers in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"   # 2 odds, 2 evens
    assert module_0.exchange([1, 5, 3, 7], [2, 4, 6, 8]) == "YES"   # 4 odds, 4 evens
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"    # 2 odds, only 1 even
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"         # 0 odds needed
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"         # exact match 3 vs 3
    assert module_0.exchange([], []) == "YES"                       # nothing to exchange

test_exchange()
print("All tests passed.")

# Generated at 2026-10-25 06:54:11.369874
# Unit test for function exchange
def test_exchange():
    # Enough even numbers in lst2 to swap for all odd numbers in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"   # 2 odds, 2 evens
    assert module_0.exchange([1, 5, 3, 7], [2, 4, 6, 8]) == "YES"   # 4 odds, 4 evens
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"    # 2 odds, only 1 even
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"         # 0 odds needed
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"         # exact match 3 vs 3
    assert module_0.exchange([], []) == "YES"                       # nothing to exchange

test_exchange()
print("All tests passed.")

# Generated at 2026-10-25 06:54:12.798346
# Unit test for function exchange
def test_exchange():
    # Enough even numbers in lst2 to swap for all odd numbers in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"   # 2 odds, 2 evens
    assert module_0.exchange([1, 5, 3, 7], [2, 4, 6, 8]) == "YES"   # 4 odds, 4 evens
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"    # 2 odds, only 1 even
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"         # 0 odds needed
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"         # exact match 3 vs 3
    assert module_0.exchange([], []) == "YES"                       # nothing to exchange

test_exchange()
print("All tests passed.")