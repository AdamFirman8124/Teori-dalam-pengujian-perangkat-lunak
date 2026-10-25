

# Generated at 2026-10-24 14:54:20.409981
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

# Generated at 2026-10-24 14:54:21.817810
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

# Generated at 2026-10-24 14:54:23.178834
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

# Generated at 2026-10-24 14:54:24.557751
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

# Generated at 2026-10-24 14:54:25.991867
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