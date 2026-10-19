

# Generated at 2022-06-14 13:12:33.157016
# Unit test for function trange
def test_trange():  # pragma: no cover
    with trange(10) as t:
        for i in t:
            pass

# Generated at 2022-06-14 13:12:35.667607
# Unit test for function trange
def test_trange():
    """
    Tests that `trange = tqdm(range)`.
    """
    assert trange(3) == tqdm(range(3))

# Generated at 2022-06-14 13:12:36.694638
# Unit test for function trange
def test_trange():
    list(trange(3))

# Generated at 2022-06-14 13:12:44.872810
# Unit test for function trange
def test_trange():
    """
    Unit test for the function ``trange``.
    """
    from .utils import _range
    assert list(trange(0)) == []
    assert list(trange(1)) == [0]
    assert list(trange(2)) == [0, 1]

    assert list(trange(10, 0, -1)) == list(reversed(_range(10)))

    assert list(trange(1, 3)) == [1, 2]
    assert list(trange(1, 3, 2)) == [1]
    assert list(trange(3, 1, 2)) == []
    assert list(trange(3, 1, -2)) == [3]
    assert list(trange(1, 3, -2)) == []


# Generated at 2022-06-14 13:12:53.157099
# Unit test for function trange
def test_trange():
    """Test for the trange() function"""
    # from tqdm import trange
    from ._utils import _range

    # Test ManualRange
    out = trange(10)
    assert isinstance(out, tqdm)
    for i in out:
        assert i in list(_range(10))

    # Test ManualRange
    out = trange(3, 10)
    assert isinstance(out, tqdm)
    for i in out:
        assert i in list(_range(3, 10))

    # Test ManualRange
    out = trange(3, 10, 2)
    assert isinstance(out, tqdm)
    for i in out:
        assert i in list(_range(3, 10, 2))

    # Test ManualRange
    out = trange(10, 3, -2)

# Generated at 2022-06-14 13:12:57.539425
# Unit test for function trange
def test_trange():
    """Test function `trange`"""
    with trange(1) as t:
        assert isinstance(t, tqdm)
        t.update(0)
        t.update(1)


# Generated at 2022-06-14 13:13:00.837723
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange.
    """
    with tqdm(total=5, disable=True) as pbar:
        for i in trange(5):
            pbar.update()

# Generated at 2022-06-14 13:13:05.902817
# Unit test for function trange
def test_trange():
    from .utils import _test_python_versions
    for python_version in _test_python_versions():  # pragma: nobranch
        with python_version:
            from tqdm.auto import trange
            assert trange(5) == range(5)
            assert trange(3, 5) == range(3, 5)



# Generated at 2022-06-14 13:13:16.378892
# Unit test for function trange
def test_trange():
    """run `python -m tqdm.auto`"""
    from .utils import _term_move_up, _range
    from .std import TqdmDeprecationWarning
    import sys

    # Test that the display is updatable, e.g. for AsyncIO
    for _ in trange(3, leave=False, file=sys.stdout):
        print("test")
        sys.stdout.flush()

    # Test that leave=True doesn't create multilines
    for _ in trange(3, leave=True, file=sys.stdout):
        print("test")
        sys.stdout.flush()
        _term_move_up()
        sys.stdout.flush()

    # Test that leave=True doesn't break on a single line
    for _ in trange(3):
        pass

   

# Generated at 2022-06-14 13:13:28.475548
# Unit test for function trange
def test_trange():
    from ._tqdm import TqdmTypeError

    test_value = 100
    with trange(test_value) as t:
        assert t.total == test_value

        for _ in t:
            pass

    t2 = trange(test_value)
    assert t2.total == test_value
    for _ in t2:
        pass

    try:
        trange(0, -1, -1)
    except TypeError as e:
        assert str(e) == TqdmTypeError.neg_step_size.format(0, -1, -1)
    else:
        assert False, "trange(0, -1, -1) did not raise TypeError"

    try:
        trange(0, 1, -1)
    except ValueError as e:
        assert str(e)