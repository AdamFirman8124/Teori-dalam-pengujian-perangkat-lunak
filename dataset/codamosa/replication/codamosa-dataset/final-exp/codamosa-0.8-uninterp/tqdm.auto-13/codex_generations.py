

# Generated at 2022-06-14 13:12:39.423013
# Unit test for function trange
def test_trange():
    from .std import tqdm
    from .autonotebook import trange
    from .asyncio import trange as atrange
    from .gui import trange as gtrange
    from .utils import _range
    for tr in (trange, atrange, gtrange):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
            l = list(tr(5, 0, -1))
        assert l == [4, 3, 2, 1, 0]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
            l = list(tr(5, 0, -1))
        assert l == [4, 3, 2, 1, 0]
        with warnings.catch_warnings():
            warnings

# Generated at 2022-06-14 13:12:48.868938
# Unit test for function trange
def test_trange():
    """Test trange"""
    from ._utils import _term_move_up
    with tqdm(total=0) as pbar:
        trange(1, miniters=1)
        trange(1, mininterval=0.01)
        trange(5)
        assert pbar.n == 1
        trange(5)
        assert pbar.n == 6

        # Test leave and disable
        trange(6, leave=False)
        assert pbar.n == 12
        trange(6, disable=True)
        assert pbar.n == 18

        pbar.write("\n" + _term_move_up())
        trange(1)
        trange(0)

# Generated at 2022-06-14 13:12:51.469948
# Unit test for function trange
def test_trange():
    """
    Unit test for `trange()`.
    """
    assert list(trange(10)) == list(range(10))


if __name__ == "__main__":
    test_trange()
    print("All tests passed")

# Generated at 2022-06-14 13:12:54.421527
# Unit test for function trange
def test_trange():
    """Test function `trange`"""
    assert list(trange(10)) == list(range(10))

# Generated at 2022-06-14 13:12:56.957994
# Unit test for function trange
def test_trange():
    """Test trange()"""
    assert list(trange(5)) == list(range(5))

# Generated at 2022-06-14 13:13:00.020644
# Unit test for function trange
def test_trange():
    """
    Test for function trange()
    """
    with tqdm(total=10) as t:
        for i in trange(5):
            t.update(1)

# Generated at 2022-06-14 13:13:03.775496
# Unit test for function trange
def test_trange():
    for i in trange(4):
        pass
    for i in trange(4, 7):
        pass
    for i in trange(4, -1):
        pass
    for i in trange(4, 7, -1):
        pass

# Generated at 2022-06-14 13:13:12.116941
# Unit test for function trange
def test_trange():
    """Test if trange functions correctly"""
    import sys
    try:
        if sys.version_info[:2] >= (3, 6):
            from .asyncio import tqdm as asyncio_tqdm
            assert trange == asyncio_tqdm
        else:
            from .autonotebook import trange as notebook_trange
            assert trange == notebook_trange
    except (ImportError, AssertionError):
        raise AssertionError("tests.test_auto.test_trange() failed")

# Generated at 2022-06-14 13:13:15.348475
# Unit test for function trange
def test_trange():
    """Test function trange"""

    assert next(iter(trange(0))) == 0
    assert next(iter(trange(0, 1))) == 0
    assert sum(trange(0, 1)) == 0
    assert sum(trange(2, 3)) == 5
    assert sum(trange(3, 10, 2)) == 24
    assert sum(trange(5, 0, -1)) == 15

# Generated at 2022-06-14 13:13:19.229129
# Unit test for function trange
def test_trange():
    import sys
    import time

    assert trange is not None
    try:
        iter(trange(5))
        out = []
        for _ in trange(5):
            time.sleep(0.01)
            out.append(0)
        assert len(out) == 5
        assert not sys.flags.interactive
    except TypeError:
        pass

# Generated at 2022-06-14 13:13:30.943458
# Unit test for function trange
def test_trange():
    from .std import format_interval, elapsed_time
    from .autojs import tqdm as tqdm_js

    for i in trange(5, desc='Trange'):
        pass

    for i in trange(5, position=4, desc='Trange'):
        pass

    for i in trange(5, position=3, desc='Trange'):
        pass

    for i in trange(5, position=2, desc='Trange'):
        pass

    # test position reset
    for i in trange(5, position=1, desc='Trange'):
        pass
    try:
        import ipywidgets
    except ImportError:
        pass
    else:
        ipywidgets.Widget.close_all()

# Generated at 2022-06-14 13:13:32.535907
# Unit test for function trange
def test_trange():
    from .utils import _range  # pylint: disable=unused-variable

# Generated at 2022-06-14 13:13:39.314598
# Unit test for function trange
def test_trange():
    import time
    # Basic
    assert trange(1)
    # Verbose
    assert trange(2, desc="my_trange", ncols=50)
    time.sleep(0.1)
    # Positional arguments
    assert trange(2, leave=False, position=1)
    time.sleep(0.1)
    # tqdm like arguments
    assert trange(2, bar_format="{l_bar}")  # pylint: disable=no-member



# Generated at 2022-06-14 13:13:47.344249
# Unit test for function trange
def test_trange():
    """Test trange"""
    from .std import TqdmTypeError, TqdmDeprecationWarning

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmDeprecationWarning)
        assert list(trange(2)) == list(range(2))
        assert isinstance(trange(2), tqdm)  # pylint: disable=c-extension-no-member
        assert isinstance(trange(2)[0], int)  # pylint: disable=c-extension-no-member
        assert list(trange(3)) == list(range(3))
        assert isinstance(trange(3), tqdm)  # pylint: disable=c-extension-no-member
        assert isinstance(trange(3)[0], int)  # p

# Generated at 2022-06-14 13:13:52.640481
# Unit test for function trange
def test_trange():
    """
    Tests that trange is not just an alias for tqdm.
    """
    from .std import trange as std_trange

    my_trange = globals()["trange"]  # pylint: disable=undefined-variable

    for i in my_trange(1):  # i.e. tqdm(range(1))
        assert i == 0

    for i in std_trange(1):  # i.e. tqdm(range(1))
        assert i == 0

# Generated at 2022-06-14 13:14:02.377147
# Unit test for function trange
def test_trange():
    """
    Test function trange()
    """
    assert list(tqdm(range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(tqdm(list(range(10)))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(tqdm(tuple(range(10)))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert list(trange(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(trange(10, 0, -1)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-14 13:14:03.867749
# Unit test for function trange
def test_trange():
    """Test trange()"""
    assert sum(trange(100)) == sum(range(100))

# Generated at 2022-06-14 13:14:14.410131
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    from sys import version_info

    if version_info[:2] >= (3, 6):
        from unittest.mock import patch
        with patch("tqdm.auto.asyncio.tqdm") as aio_tqdm, \
                patch("tqdm.auto.notebook.trange") as nb_trange:
            # tqdm should be asyncio for Python >= 3.6
            dummy = trange(5)
            assert aio_tqdm.called
            assert not nb_trange.called
    else:
        from mock import patch

# Generated at 2022-06-14 13:14:23.186855
# Unit test for function trange
def test_trange():
    """Test for trange"""
    from .std import PY3, IS_WINDOWS

    list(trange(0))
    list(trange(1, 0))
    list(trange(1, 1, -1))
    list(trange(1, 1, 0))
    list(trange(1, 1, 0.1))
    list(trange(1, 1, -0.1))
    list(trange(1, 1, 0.9))
    list(trange(1, 1, -0.9))
    try:
        # Should print "Warning: Input value is too small", and stop
        list(trange(1, 1, 1e-8))
    except AssertionError:
        pass

# Generated at 2022-06-14 13:14:25.608231
# Unit test for function trange
def test_trange():
    """
    Ensures that trange is not broken on 2.7/3.6
    """
    assert trange(7).__class__.__name__ == "tqdm"
    assert trange(7)._instances is None