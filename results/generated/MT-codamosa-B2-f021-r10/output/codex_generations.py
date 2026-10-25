

# Generated at 2026-10-24 15:51:30.566599
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 15:51:38.834364
# Unit test for function rescale_to_unit
def test_rescale_to_unit():assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]

# Generated at 2026-10-24 15:52:06.321653
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    result = module_0.rescale_to_unit([10.0, 20.0, 30.0])

    assert result == [0.0, 0.5, 1.0]


def test_rescale_to_unit_preserves_order():
    result = module_0.rescale_to_unit([30.0, 10.0, 20.0])

    assert result == [1.0, 0.0, 0.5]


def test_rescale_to_unit_with_negative_numbers():
    result = module_0.rescale_to_unit([-10.0, 0.0, 10.0])

    assert result == [0.0, 0.5, 1.0]


def test_rescale_to_unit_with_constant_numbers():
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([5.0, 5.0, 5.0])

# Generated at 2026-10-24 15:52:22.252813
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # 1. Basic increasing list
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # 2. Positive integers
    assert module_0.rescale_to_unit([0, 5, 10]) == [0.0, 0.5, 1.0]

    # 3. With negative numbers
    assert module_0.rescale_to_unit([-10, 0, 10]) == [0.0, 0.5, 1.0]

    # 4. Unsorted with duplicates
    assert module_0.rescale_to_unit([3, 1, 2, 1, 3]) == [1.0, 0.0, 0.5, 0.0, 1.0]

    # 5. Two elements
    assert module_0.rescale_to_unit([100.0, 200.0]) == [0.0, 1.0]

    # 6. Property: min -> 0.0, max -> 1.0
    result = module_0.rescale_to_unit([4.2, -1.5, 7.7, 7.7, 0.0])
    assert min(result) == 0.0
    assert max(result) == 1.0
    assert len(result) == 5

# Generated at 2026-10-24 15:52:23.613843
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # 1. Basic increasing list
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # 2. Positive integers
    assert module_0.rescale_to_unit([0, 5, 10]) == [0.0, 0.5, 1.0]

    # 3. With negative numbers
    assert module_0.rescale_to_unit([-10, 0, 10]) == [0.0, 0.5, 1.0]

    # 4. Unsorted with duplicates
    assert module_0.rescale_to_unit([3, 1, 2, 1, 3]) == [1.0, 0.0, 0.5, 0.0, 1.0]

    # 5. Two elements
    assert module_0.rescale_to_unit([100.0, 200.0]) == [0.0, 1.0]

    # 6. Property: min -> 0.0, max -> 1.0
    result = module_0.rescale_to_unit([4.2, -1.5, 7.7, 7.7, 0.0])
    assert min(result) == 0.0
    assert max(result) == 1.0
    assert len(result) == 5

# Generated at 2026-10-24 15:52:34.116755
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [10.0, 20.0, 30.0, 40.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == [0.0, 1 / 3, 2 / 3, 1.0]