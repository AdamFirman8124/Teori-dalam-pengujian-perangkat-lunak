

# Generated at 2026-10-25 00:18:50.105490
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == pytest.approx(
        [0.0, 0.5, 1.0]
    )

    assert module_0.rescale_to_unit([-10.0, 0.0, 10.0]) == pytest.approx(
        [0.0, 0.5, 1.0]
    )

    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == pytest.approx(
        [1.0, 0.0, 0.5]
    )

    assert module_0.rescale_to_unit([2.5, 7.5]) == pytest.approx(
        [0.0, 1.0]
    )

# Generated at 2026-10-25 00:18:55.504341
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [2.0, 4.0, 6.0, 8.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 1 / 3, 2 / 3, 1.0])

# Generated at 2026-10-25 00:19:00.757521
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [1.0, 2.0, 3.0, 4.0]
    expected = [0.0, 1 / 3, 2 / 3, 1.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == expected

# Generated at 2026-10-25 00:19:05.594265
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-5.0, 0.0, 5.0, 15.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == [0.0, 0.25, 0.5, 1.0]

# Generated at 2026-10-25 00:19:11.019124
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-5.0, 0.0, 5.0, 15.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 0.25, 0.5, 1.0])