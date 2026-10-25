

# Generated at 2026-10-24 22:45:55.939351
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)
    assert module_0.mean_absolute_deviation([10, 10, 10]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-2, 0, 2]) == pytest.approx(4 / 3)
    assert module_0.mean_absolute_deviation([5]) == pytest.approx(0.0)

# Generated at 2026-10-24 22:46:00.752456
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3]) == pytest.approx(2 / 3)
    assert module_0.mean_absolute_deviation([5]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-2, 0, 2]) == pytest.approx(4 / 3)
    assert module_0.mean_absolute_deviation([1.5, 2.5, 3.5]) == pytest.approx(2 / 3)

    with pytest.raises(ZeroDivisionError):
        module_0.mean_absolute_deviation([])

# Generated at 2026-10-24 22:46:06.690013
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert math.isclose(
        module_0.mean_absolute_deviation([1, 2, 3, 4, 5]),
        1.2,
    )
    assert math.isclose(
        module_0.mean_absolute_deviation([-1, -2, -3]),
        2 / 3,
    )
    assert module_0.mean_absolute_deviation([2, 2, 2]) == 0.0
    assert module_0.mean_absolute_deviation([10]) == 0.0

# Generated at 2026-10-24 22:46:12.718217
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3]) == pytest.approx(2 / 3)
    assert module_0.mean_absolute_deviation([1, 1, 1]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-1, 1]) == pytest.approx(1.0)
    assert module_0.mean_absolute_deviation([1, 2, 4]) == pytest.approx(10 / 9)
    assert module_0.mean_absolute_deviation([42]) == pytest.approx(0.0)

# Generated at 2026-10-24 22:46:19.286227
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4]) == pytest.approx(1.0)
    assert module_0.mean_absolute_deviation([1, 2, 3]) == pytest.approx(2 / 3)
    assert module_0.mean_absolute_deviation([-2, 0, 2]) == pytest.approx(4 / 3)
    assert module_0.mean_absolute_deviation([5]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([3, 3, 3]) == pytest.approx(0.0)