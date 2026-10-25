

# Generated at 2026-10-24 11:53:27.179335
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # standard spread
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0, 8.0, 10.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # negatives
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]

    # already in [0, 1]
    assert module_0.rescale_to_unit([0.0, 0.5, 1.0]) == [0.0, 0.5, 1.0]

    # single element -> ZeroDivisionError (current behavior)
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([3.0])

    # all equal -> ZeroDivisionError (current behavior)
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([1.0, 1.0, 1.0])

# Generated at 2026-10-24 11:53:29.600458
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:32.017989
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:34.439736
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:36.856853
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:39.272138
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:41.692598
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:44.114549
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:46.534766
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:49.088038
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:51.508075
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:53.927875
# Unit test for function rescale_to_unit

# Generated at 2026-10-24 11:53:56.348082
# Unit test for function rescale_to_unit