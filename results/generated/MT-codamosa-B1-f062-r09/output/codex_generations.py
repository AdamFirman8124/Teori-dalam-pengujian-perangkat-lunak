

# Generated at 2026-10-25 00:21:35.423617
# Unit test for function derivative

# Generated at 2026-10-25 00:21:37.839220
# Unit test for function derivative

# Generated at 2026-10-25 00:21:41.926141
# Unit test for function derivative
def test_derivative():
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    assert module_0.derivative([3.5, 2.0, 4.0]) == [2.0, 8.0]
    assert module_0.derivative([5]) == []
    assert module_0.derivative([]) == []

# Generated at 2026-10-25 00:21:43.255661
# Unit test for function derivative
def test_derivative():
    assert module_0.derivative([3, 1, 2, 4]) == [1, 4, 12]
    assert module_0.derivative([1, 2]) == [2]
    assert module_0.derivative([5]) == []          # constant -> empty
    assert module_0.derivative([]) == []           # empty stays empty

# Generated at 2026-10-25 00:21:44.583557
# Unit test for function derivative
def test_derivative():
    assert module_0.derivative([3, 1, 2, 4]) == [1, 4, 12]
    assert module_0.derivative([1, 2]) == [2]
    assert module_0.derivative([5]) == []          # constant -> empty
    assert module_0.derivative([]) == []           # empty stays empty

# Generated at 2026-10-25 00:21:45.958125
# Unit test for function derivative
def test_derivative():
    assert module_0.derivative([3, 1, 2, 4]) == [1, 4, 12]
    assert module_0.derivative([1, 2]) == [2]
    assert module_0.derivative([5]) == []          # constant -> empty
    assert module_0.derivative([]) == []           # empty stays empty

# Generated at 2026-10-25 00:21:47.306957
# Unit test for function derivative
def test_derivative():
    assert module_0.derivative([3, 1, 2, 4]) == [1, 4, 12]
    assert module_0.derivative([1, 2]) == [2]
    assert module_0.derivative([5]) == []          # constant -> empty
    assert module_0.derivative([]) == []           # empty stays empty