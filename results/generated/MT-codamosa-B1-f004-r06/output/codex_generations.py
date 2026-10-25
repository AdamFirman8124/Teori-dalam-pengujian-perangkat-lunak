

# Generated at 2026-10-24 21:20:09.461053
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-24 21:20:11.879194
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-24 21:20:14.301254
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-24 21:20:16.717153
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-24 21:20:19.135460
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-24 21:20:21.554355
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-24 21:20:23.973509
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-24 21:20:26.388399
# Unit test for function mean_absolute_deviation

# Generated at 2026-10-24 21:20:32.124674
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

# Generated at 2026-10-24 21:20:38.269262
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)
    assert module_0.mean_absolute_deviation([2, 2, 2]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-1, 0, 1]) == pytest.approx(2 / 3)
    assert module_0.mean_absolute_deviation([10]) == pytest.approx(0.0)

# Generated at 2026-10-24 21:20:43.946815
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4]) == pytest.approx(1.0)
    assert module_0.mean_absolute_deviation([5]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([2, 2, 2]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-2, 0, 2]) == pytest.approx(4 / 3)

    with pytest.raises(ZeroDivisionError):
        module_0.mean_absolute_deviation([])