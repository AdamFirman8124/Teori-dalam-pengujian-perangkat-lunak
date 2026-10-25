

# Generated at 2026-10-25 04:46:11.651893
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    assert module_0.rescale_to_unit([0.0, 5.0, 10.0]) == [0.0, 0.5, 1.0]
    assert module_0.rescale_to_unit([-10.0, 0.0, 10.0]) == [0.0, 0.5, 1.0]
    assert module_0.rescale_to_unit([20.0, 10.0, 15.0]) == [1.0, 0.0, 0.5]

# Generated at 2026-10-25 04:46:17.486957
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [2.0, 4.0, 6.0, 8.0]
    expected = [0.0, 1 / 3, 2 / 3, 1.0]

    result = module_0.rescale_to_unit(numbers)

    assert len(result) == len(expected)
    assert all(abs(actual - target) < 1e-9
               for actual, target in zip(result, expected))

# Generated at 2026-10-25 04:46:24.554804
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

# Generated at 2026-10-25 04:46:30.094628
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [-5.0, 0.0, 5.0, 10.0]

    result = module_0.rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 1 / 3, 2 / 3, 1.0])
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)

# Generated at 2026-10-25 04:46:32.512113
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 04:46:35.074722
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 04:46:37.498037
# Unit test for function rescale_to_unit