

# Generated at 2026-11-02 00:47:15.807455
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic ascending list
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Unsorted input
    assert module_0.rescale_to_unit([5.0, 3.0, 1.0]) == [1.0, 0.5, 0.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-2.0, 0.0, 2.0]) == [0.0, 0.5, 1.0]

    # All negative numbers
    assert module_0.rescale_to_unit([-5.0, -3.0, -1.0]) == [0.0, 0.5, 1.0]

    # Two elements
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]

    # Floating point precision check
    result = module_0.rescale_to_unit([0.0, 1.0, 2.0, 3.0])
    expected = [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0]
    for actual, exp in zip(result, expected):
        assert math.isclose(actual, exp, rel_tol=1e-9)

    # Min maps to 0 and max maps to 1 for arbitrary input
    numbers = [3.7, 1.2, 9.4, -2.5, 5.1]
    result = module_0.rescale_to_unit(numbers)
    assert math.isclose(result[0], (3.7 + 2.5) / (9.4 + 2.5), rel_tol=1e-9)
    assert result[2] == 1.0
    assert result[3] == 0.0

# Generated at 2026-11-02 00:48:24.084411
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic linear scaling between min=1 and max=5
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Simple two-element case
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]

    # Order doesn't matter: each value scaled by its position between min and max
    assert module_0.rescale_to_unit([10.0, 0.0, 5.0]) == [1.0, 0.0, 0.5]

    # Works with negative numbers
    assert module_0.rescale_to_unit([-2.0, -1.0, 0.0]) == [0.0, 0.5, 1.0]

    # Mixed negative and positive values
    assert module_0.rescale_to_unit([-1.0, 1.0]) == [0.0, 1.0]

    # All values below 1
    assert module_0.rescale_to_unit([0.1, 0.2, 0.3]) == [0.0, 0.5, 1.0]

    # Result is always within [0, 1] and preserves list length
    data = [3.5, -2.0, 7.25, 0.0, 4.1]
    result = module_0.rescale_to_unit(data)
    assert len(result) == len(data)
    assert all(0.0 <= v <= 1.0 for v in result)
    assert min(result) == 0.0
    assert max(result) == 1.0

    # Empty range boundaries map correctly when min equals one element
    single_range = module_0.rescale_to_unit([5.0, 5.0 + 1e-9, 5.0 - 1e-9])
    assert abs(single_range[0] - 0.5) < 1e-3

# Generated at 2026-11-02 00:49:46.178743
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: values spanning 1 to 5
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_rescale_to_unit_two_elements():
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]


def test_rescale_to_unit_negative_numbers():
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]


def test_rescale_to_unit_all_negative():
    assert module_0.rescale_to_unit([-4.0, -2.0]) == [0.0, 1.0]


def test_rescale_to_unit_preserves_order():
    numbers = [10.0, 3.0, 7.0, 1.0]
    result = module_0.rescale_to_unit(numbers)
    assert result[0] == 1.0
    assert result[3] == 0.0
    assert abs(result[1] - 2.0 / 9.0) < 1e-9
    assert abs(result[2] - 6.0 / 9.0) < 1e-9


def test_rescale_to_unit_min_max_bounds():
    numbers = [3.5, 1.2, 9.8, 4.4]
    result = module_0.rescale_to_unit(numbers)
    assert min(result) == 0.0
    assert max(result) == 1.0


def test_rescale_to_unit_length_preserved():
    numbers = [1.0, 2.0, 3.0]
    assert len(module_0.rescale_to_unit(numbers)) == len(numbers)


def test_rescale_to_unit_constant_values_raises():
    # Division by zero when max == min
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([5.0, 5.0, 5.0])


def test_rescale_to_unit_empty_raises():
    with pytest.raises(ValueError):
        module_0.rescale_to_unit([])

# Generated at 2026-11-02 00:50:49.915293
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: values spanning a range
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]
    assert module_0.rescale_to_unit([-5.0, -3.0]) == [0.0, 1.0]

    # Values already within [0, 1]
    assert module_0.rescale_to_unit([0.0, 0.5, 1.0]) == [0.0, 0.5, 1.0]

    # Two elements
    assert module_0.rescale_to_unit([10.0, 20.0]) == [0.0, 1.0]

    # Duplicates and unsorted input
    assert module_0.rescale_to_unit([6.0, 4.0, 2.0, 4.0]) == [1.0, 0.5, 0.0, 0.5]

    # General properties: length preserved, min -> 0, max -> 1, all in [0, 1]
    numbers = [3.5, -2.1, 7.8, 0.0, 5.5]
    result = module_0.rescale_to_unit(numbers)
    assert len(result) == len(numbers)
    assert abs(min(result) - 0.0) < 1e-9
    assert abs(max(result) - 1.0) < 1e-9
    assert all(0.0 <= x <= 1.0 for x in result)

    # Single-element list: min == max leads to division by zero
    try:
        module_0.rescale_to_unit([4.0])
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

# Generated at 2026-11-02 00:52:00.723444
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # nonce:9021b351
    # Basic range [1..5] scales linearly
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == pytest.approx(
        [0.0, 0.25, 0.5, 0.75, 1.0]
    )

    # Two-element list spans the full [0, 1] range
    assert module_0.rescale_to_unit([2.0, 49.9]) == pytest.approx([0.0, 1.0])
    assert module_0.rescale_to_unit([49.9, 2.0]) == pytest.approx([1.0, 0.0])

    # Minimum maps to 0, maximum maps to 1
    result = module_0.rescale_to_unit([-10.0, 0.0, 10.0])
    assert result[0] == pytest.approx(0.0)
    assert result[-1] == pytest.approx(1.0)

    # Negative numbers handled correctly
    assert module_0.rescale_to_unit([-2.0, -1.0, 0.0]) == pytest.approx([0.0, 0.5, 1.0])

    # Unsorted input preserves original ordering
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == pytest.approx([1.0, 0.0, 0.5])

    # Duplicated values receive identical scaled output
    assert module_0.rescale_to_unit([1.0, 1.0, 2.0]) == pytest.approx([0.0, 0.0, 1.0])

    # Fractional midpoint values scale proportionally
    assert module_0.rescale_to_unit([0.0, 10.0, 5.0]) == pytest.approx([0.0, 1.0, 0.5])

    # Input length is preserved
    nums = [3.1, 7.2, 11.4, 15.8, 19.9, 23.3]
    assert len(module_0.rescale_to_unit(nums)) == len(nums)

    # Single-element list causes division by zero (degenerate range)
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([7.0])

    # Empty list fails inside min()/max()
    with pytest.raises(ValueError):
        module_0.rescale_to_unit([])