

# Generated at 2026-10-25 10:18:14.009444
# Unit test for function exchange
def test_exchange():
    # YES: enough evens in lst2 to replace odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"  # odd=2, even=2
    assert module_0.exchange([1, 3, 5], [2, 4, 6, 8]) == "YES"  # odd=3, even=4
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8, 10]) == "YES"  # odd=4, even=5
    assert module_0.exchange([1], [2]) == "YES"  # odd=1, even=1

    # NO: not enough evens in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"  # odd=3, even=2
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6]) == "NO"  # odd=4, even=3
    assert module_0.exchange([1], []) == "NO"  # odd=1, even=0
    assert module_0.exchange([1, 3], [1, 3, 5]) == "NO"  # odd=2, even=0

    # Edge cases: zero odds needed -> always YES
    assert module_0.exchange([], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([], [1, 3, 5]) == "YES"  # odd=0, even=0

# Generated at 2026-10-25 10:18:15.388485
# Unit test for function exchange
def test_exchange():
    # YES: enough evens in lst2 to replace odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"  # odd=2, even=2
    assert module_0.exchange([1, 3, 5], [2, 4, 6, 8]) == "YES"  # odd=3, even=4
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8, 10]) == "YES"  # odd=4, even=5
    assert module_0.exchange([1], [2]) == "YES"  # odd=1, even=1

    # NO: not enough evens in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"  # odd=3, even=2
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6]) == "NO"  # odd=4, even=3
    assert module_0.exchange([1], []) == "NO"  # odd=1, even=0
    assert module_0.exchange([1, 3], [1, 3, 5]) == "NO"  # odd=2, even=0

    # Edge cases: zero odds needed -> always YES
    assert module_0.exchange([], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([], [1, 3, 5]) == "YES"  # odd=0, even=0

# Generated at 2026-10-25 10:18:16.851424
# Unit test for function exchange
def test_exchange():
    # YES: enough evens in lst2 to replace odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"  # odd=2, even=2
    assert module_0.exchange([1, 3, 5], [2, 4, 6, 8]) == "YES"  # odd=3, even=4
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8, 10]) == "YES"  # odd=4, even=5
    assert module_0.exchange([1], [2]) == "YES"  # odd=1, even=1

    # NO: not enough evens in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"  # odd=3, even=2
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6]) == "NO"  # odd=4, even=3
    assert module_0.exchange([1], []) == "NO"  # odd=1, even=0
    assert module_0.exchange([1, 3], [1, 3, 5]) == "NO"  # odd=2, even=0

    # Edge cases: zero odds needed -> always YES
    assert module_0.exchange([], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([], [1, 3, 5]) == "YES"  # odd=0, even=0

# Generated at 2026-10-25 10:18:18.281673
# Unit test for function exchange
def test_exchange():
    # YES: enough evens in lst2 to replace odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"  # odd=2, even=2
    assert module_0.exchange([1, 3, 5], [2, 4, 6, 8]) == "YES"  # odd=3, even=4
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8, 10]) == "YES"  # odd=4, even=5
    assert module_0.exchange([1], [2]) == "YES"  # odd=1, even=1

    # NO: not enough evens in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"  # odd=3, even=2
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6]) == "NO"  # odd=4, even=3
    assert module_0.exchange([1], []) == "NO"  # odd=1, even=0
    assert module_0.exchange([1, 3], [1, 3, 5]) == "NO"  # odd=2, even=0

    # Edge cases: zero odds needed -> always YES
    assert module_0.exchange([], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([], [1, 3, 5]) == "YES"  # odd=0, even=0

# Generated at 2026-10-25 10:18:19.715271
# Unit test for function exchange
def test_exchange():
    # YES: enough evens in lst2 to replace odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"  # odd=2, even=2
    assert module_0.exchange([1, 3, 5], [2, 4, 6, 8]) == "YES"  # odd=3, even=4
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8, 10]) == "YES"  # odd=4, even=5
    assert module_0.exchange([1], [2]) == "YES"  # odd=1, even=1

    # NO: not enough evens in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"  # odd=3, even=2
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6]) == "NO"  # odd=4, even=3
    assert module_0.exchange([1], []) == "NO"  # odd=1, even=0
    assert module_0.exchange([1, 3], [1, 3, 5]) == "NO"  # odd=2, even=0

    # Edge cases: zero odds needed -> always YES
    assert module_0.exchange([], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"  # odd=0, even=0
    assert module_0.exchange([2, 4, 6], []) == "YES"  # odd=0, even=0
    assert module_0.exchange([], [1, 3, 5]) == "YES"  # odd=0, even=0