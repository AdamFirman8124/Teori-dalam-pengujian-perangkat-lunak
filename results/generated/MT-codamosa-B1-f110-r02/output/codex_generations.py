

# Generated at 2026-10-25 09:47:13.048218
# Unit test for function exchange

# Generated at 2026-10-25 09:47:15.463290
# Unit test for function exchange

# Generated at 2026-10-25 09:47:17.875232
# Unit test for function exchange

# Generated at 2026-10-25 09:47:20.478815
# Unit test for function exchange

# Generated at 2026-10-25 09:47:22.895181
# Unit test for function exchange

# Generated at 2026-10-25 09:47:25.312936
# Unit test for function exchange

# Generated at 2026-10-25 09:47:27.731075
# Unit test for function exchange

# Generated at 2026-10-25 09:47:30.144570
# Unit test for function exchange

# Generated at 2026-10-25 09:47:32.562136
# Unit test for function exchange

# Generated at 2026-10-25 09:47:34.976331
# Unit test for function exchange

# Generated at 2026-10-25 09:47:37.395380
# Unit test for function exchange

# Generated at 2026-10-25 09:47:39.814775
# Unit test for function exchange

# Generated at 2026-10-25 09:47:42.276359
# Unit test for function exchange

# Generated at 2026-10-25 09:47:44.690961
# Unit test for function exchange

# Generated at 2026-10-25 09:47:47.104978
# Unit test for function exchange

# Generated at 2026-10-25 09:47:49.516739
# Unit test for function exchange

# Generated at 2026-10-25 09:47:51.931789
# Unit test for function exchange

# Generated at 2026-10-25 09:47:54.353718
# Unit test for function exchange

# Generated at 2026-10-25 09:47:56.766493
# Unit test for function exchange

# Generated at 2026-10-25 09:47:59.179199
# Unit test for function exchange

# Generated at 2026-10-25 09:48:01.592765
# Unit test for function exchange

# Generated at 2026-10-25 09:48:04.006701
# Unit test for function exchange

# Generated at 2026-10-25 09:48:06.422791
# Unit test for function exchange

# Generated at 2026-10-25 09:48:08.834952
# Unit test for function exchange

# Generated at 2026-10-25 09:48:11.249258
# Unit test for function exchange

# Generated at 2026-10-25 09:48:13.662727
# Unit test for function exchange

# Generated at 2026-10-25 09:48:16.081213
# Unit test for function exchange

# Generated at 2026-10-25 09:48:18.490229
# Unit test for function exchange

# Generated at 2026-10-25 09:48:20.907133
# Unit test for function exchange

# Generated at 2026-10-25 09:48:38.464984
# Unit test for function exchange
def test_exchange():assert module_0.exchange([1, 3], [2, 4]) == "YES"

# Generated at 2026-10-25 09:48:39.807940
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

# Generated at 2026-10-25 09:48:41.278580
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

# Generated at 2026-10-25 09:48:42.657363
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

# Generated at 2026-10-25 09:48:44.090001
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

# Generated at 2026-10-25 09:48:45.835254
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