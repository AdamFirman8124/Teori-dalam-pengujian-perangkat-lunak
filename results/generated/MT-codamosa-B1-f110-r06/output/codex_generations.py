

# Generated at 2026-10-24 22:54:37.065404
# Unit test for function exchange
def test_exchange():
    assert module_0.exchange([1, 2, 3, 4], [2, 4]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([-3, -2, -1], [-4, 1]) == "NO"

# Generated at 2026-10-24 22:54:44.749299
# Unit test for function exchange
def test_exchange():
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4, 7]) == "NO"
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([], []) == "YES"

# Generated at 2026-10-24 22:54:50.774432
# Unit test for function exchange
def test_exchange():
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 7, 9]) == "NO"
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([], []) == "YES"

# Generated at 2026-10-24 22:54:57.021987
# Unit test for function exchange
def test_exchange():
    assert module_0.exchange([1, 2, 3], [4, 5, 6]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 7, 9]) == "NO"
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([-1, -2, -3], [-4, -6]) == "YES"

# Generated at 2026-10-24 22:55:03.474604
# Unit test for function exchange
def test_exchange():
    assert module_0.exchange([1, 2, 3, 4], [5, 6, 7, 8]) == "YES"
    assert module_0.exchange([1, 2, 3, 4], [5, 5, 6, 7]) == "NO"
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    assert module_0.exchange([], []) == "YES"