

# Generated at 2026-10-24 20:24:55.253195
# Unit test for function max_element
def test_max_element():
    assert module_0.max_element([1, 2, 3, 4]) == 4
    assert module_0.max_element([-5, -2, -10]) == -2
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([3, 9, 9, 2]) == 9

# Generated at 2026-10-24 20:25:00.042733
# Unit test for function max_element
def test_max_element():
    assert module_0.max_element([1, 2, 3, 4]) == 4
    assert module_0.max_element([-5, -2, -10]) == -2
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([3, 3, 2, 1]) == 3

# Generated at 2026-10-24 20:25:04.954229
# Unit test for function max_element
def test_max_element():
    assert module_0.max_element([1, 3, 2]) == 3
    assert module_0.max_element([-5, -2, -10]) == -2
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([4, 4, 4]) == 4

# Generated at 2026-10-24 20:25:09.337755
# Unit test for function max_element
def test_max_element():
    assert module_0.max_element([1, 2, 3, 4]) == 4
    assert module_0.max_element([-5, -2, -10]) == -2
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([3, 9, 9, 2]) == 9

    with pytest.raises(IndexError):
        module_0.max_element([])

# Generated at 2026-10-24 20:25:13.326518
# Unit test for function max_element
def test_max_element():
    assert module_0.max_element([1, 3, 2, 5, 4]) == 5
    assert module_0.max_element([-10, -3, -20, -4]) == -3
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([2, 2, 2]) == 2