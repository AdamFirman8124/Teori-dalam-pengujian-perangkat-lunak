

# Generated at 2026-10-24 04:34:24.864495
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]

    assert module_0.rescale_to_unit(numbers) == pytest.approx(expected)

# Generated at 2026-10-24 04:34:34.270472
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-5.0, 0.0, 5.0, 10.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 1 / 3, 2 / 3, 1.0])
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)

# Generated at 2026-10-24 04:34:41.132794
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [2.0, 4.0, 6.0]
    result = module_0.rescale_to_unit(numbers)

    assert result == [0.0, 0.5, 1.0]

# Generated at 2026-10-24 04:34:46.353666
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-5.0, 0.0, 5.0]
    expected = [0.0, 0.5, 1.0]

    assert module_0.rescale_to_unit(numbers) == expected

# Generated at 2026-10-24 04:34:51.779989
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-10.0, 0.0, 10.0, 30.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 0.25, 0.5, 1.0])