

# Generated at 2026-10-24 11:22:04.343055
# Unit test for function exchange
def test_exchange():
    # basic cases: enough evens in lst2 to replace odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"  # 2 odds, 2 evens
    assert module_0.exchange([1, 2, 3, 4], [1, 1, 1, 1]) == "NO"   # 2 odds, 0 evens

    # lst1 already all even - no exchange needed
    assert module_0.exchange([2, 4, 6, 8], [1, 3, 5, 7]) == "YES"  # 0 odds, 0 evens
    assert module_0.exchange([2, 4], [1, 3]) == "YES"
    assert module_0.exchange([], []) == "YES"

    # lst1 all odd
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8]) == "YES"  # 4 odds, 4 evens
    assert module_0.exchange([1, 3, 5, 7], [1, 3, 5, 7]) == "NO"   # 4 odds, 0 evens
    assert module_0.exchange([1, 3, 5], [2, 4, 6, 8, 10]) == "YES" # 3 odds, 5 evens
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"            # 3 odds, 2 evens

    # single element
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [1]) == "NO"
    assert module_0.exchange([2], [1]) == "YES"

# Generated at 2026-10-24 11:22:06.769550
# Unit test for function exchange

# Generated at 2026-10-24 11:22:09.181980
# Unit test for function exchange

# Generated at 2026-10-24 11:22:11.607190
# Unit test for function exchange

# Generated at 2026-10-24 11:22:14.068784
# Unit test for function exchange

# Generated at 2026-10-24 11:22:16.489027
# Unit test for function exchange

# Generated at 2026-10-24 11:22:18.910848
# Unit test for function exchange

# Generated at 2026-10-24 11:22:21.331686
# Unit test for function exchange

# Generated at 2026-10-24 11:22:23.748689
# Unit test for function exchange

# Generated at 2026-10-24 11:22:26.166063
# Unit test for function exchange

# Generated at 2026-10-24 11:22:35.905144
# Unit test for function exchange

# Generated at 2026-10-24 11:22:41.538561
# Unit test for function exchange
def test_exchange():
    # lst1 all odd, lst2 has enough evens -> YES
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"

    # lst1 has 3 odds, lst2 has only 1 even -> NO
    assert module_0.exchange([1, 3, 5], [2, 7, 9]) == "NO"

    # lst1 already all even (0 odds), any lst2 -> YES
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # equal counts: 1 odd in lst1, 1 even in lst2 -> YES
    assert module_0.exchange([1, 2], [4, 7]) == "YES"

    # empty lst1 (0 odds), empty lst2 -> YES
    assert module_0.exchange([], []) == "YES"

    # negative numbers: -3 is odd, -2 is even
    assert module_0.exchange([-3], [-2]) == "YES"
    assert module_0.exchange([-3, -5], [-2, 1]) == "NO"

    # zero counts as even in lst2
    assert module_0.exchange([1], [0]) == "YES"