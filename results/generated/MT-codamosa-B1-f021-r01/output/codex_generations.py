

# Generated at 2026-10-24 13:33:04.450612
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

# Generated at 2026-10-24 13:33:05.768999
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

# Generated at 2026-10-24 13:33:07.100357
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

# Generated at 2026-10-24 13:33:08.422131
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

# Generated at 2026-10-24 13:33:09.958445
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