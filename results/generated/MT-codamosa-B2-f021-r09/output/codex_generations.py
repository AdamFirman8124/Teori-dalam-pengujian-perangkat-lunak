

# Generated at 2026-10-24 06:21:45.238755
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [1.0, 2.0, 3.0, 4.0]
    expected = [0.0, 1 / 3, 2 / 3, 1.0]

    assert module_0.rescale_to_unit(numbers) == pytest.approx(expected)

# Generated at 2026-10-24 06:21:50.970543
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-5.0, 0.0, 5.0, 15.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == [0.0, 0.25, 0.5, 1.0]
    assert min(result) == 0.0
    assert max(result) == 1.0

# Generated at 2026-10-24 06:21:56.808475
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [10.0, 20.0, 30.0, 40.0]
    expected = [0.0, 1 / 3, 2 / 3, 1.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == pytest.approx(expected)

# Generated at 2026-10-24 06:21:59.226859
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 06:22:01.640948
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 06:22:04.057381
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 06:22:09.813824
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [2.0, 4.0, 6.0]
    expected = [0.0, 0.5, 1.0]

    assert module_0.rescale_to_unit(numbers) == expected