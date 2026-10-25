

# Generated at 2026-10-24 23:14:09.231987
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-10.0, 0.0, 10.0, 20.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 1 / 3, 2 / 3, 1.0])

# Generated at 2026-10-24 23:14:15.067262
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [10.0, 20.0, 30.0, 40.0]
    expected = [0.0, 1 / 3, 2 / 3, 1.0]

    assert module_0.rescale_to_unit(numbers) == pytest.approx(expected)

# Generated at 2026-10-24 23:14:21.314739
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == pytest.approx([0.0, 0.5, 1.0])
    assert module_0.rescale_to_unit([-10.0, 0.0, 10.0]) == pytest.approx([0.0, 0.5, 1.0])
    assert module_0.rescale_to_unit([5.0, 0.0, 10.0]) == pytest.approx([0.5, 0.0, 1.0])

# Generated at 2026-10-24 23:14:27.255613
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-5.0, 0.0, 5.0, 10.0]
    expected = [0.0, 1 / 3, 2 / 3, 1.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == pytest.approx(expected)
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)

# Generated at 2026-10-24 23:14:34.321730
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-5.0, 0.0, 5.0, 10.0]
    expected = [0.0, 1 / 3, 2 / 3, 1.0]

    assert module_0.rescale_to_unit(numbers) == pytest.approx(expected)