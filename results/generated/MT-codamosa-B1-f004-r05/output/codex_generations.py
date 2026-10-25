

# Generated at 2026-10-24 21:36:40.015835
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)
    assert module_0.mean_absolute_deviation([10, 10, 10]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-1, -2, -3]) == pytest.approx(2 / 3)
    assert module_0.mean_absolute_deviation([42]) == pytest.approx(0.0)

    with pytest.raises(ZeroDivisionError):
        module_0.mean_absolute_deviation([])

# Generated at 2026-10-24 21:36:45.954266
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    numbers = [1, 2, 3, 4, 5]
    expected = 1.2

    assert abs(module_0.mean_absolute_deviation(numbers) - expected) < 1e-9

# Generated at 2026-10-24 21:36:53.330473
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert math.isclose(
        module_0.mean_absolute_deviation([1, 2, 3, 4, 5]),
        1.2,
    )
    assert math.isclose(
        module_0.mean_absolute_deviation([-1, 0, 1]),
        2 / 3,
    )
    assert module_0.mean_absolute_deviation([5, 5, 5]) == 0.0
    assert module_0.mean_absolute_deviation([10]) == 0.0

# Generated at 2026-10-24 21:36:58.334259
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert math.isclose(
        module_0.mean_absolute_deviation([1, 2, 3, 4, 5]),
        1.2,
    )
    assert math.isclose(
        module_0.mean_absolute_deviation([10, 10, 10]),
        0.0,
    )
    assert math.isclose(
        module_0.mean_absolute_deviation([-2, 0, 2]),
        4 / 3,
    )

# Generated at 2026-10-24 21:37:04.565130
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)
    assert module_0.mean_absolute_deviation([5, 5, 5]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-2, 0, 2]) == pytest.approx(4 / 3)
    assert module_0.mean_absolute_deviation([10]) == pytest.approx(0.0)