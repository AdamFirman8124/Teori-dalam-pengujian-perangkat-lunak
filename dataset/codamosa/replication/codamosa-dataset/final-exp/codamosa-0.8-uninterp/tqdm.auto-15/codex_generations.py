

# Generated at 2022-06-14 13:12:38.226001
# Unit test for function trange
def test_trange():
    """Test for trange"""
    for i in trange(100):  # noqa
        pass

# Generated at 2022-06-14 13:12:48.629900
# Unit test for function trange
def test_trange():
    """Tests `tqdm.auto.trange`."""
    from .std import tqdm
    import random
    try:
        from .std import Range
    except ImportError:
        from .std import range as Range

    for _ in trange(random.randint(0, 10)):
        for _ in trange(random.randint(0, 10)):
            for _ in trange(random.randint(0, 10)):
                for _ in trange(random.randint(0, 10)):
                    for i in trange(random.randint(0, 10)):
                        assert i in Range(0, 10)

if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:12:53.640542
# Unit test for function trange
def test_trange():
    """
    Test the trange function
    """
    from .utils import wrap_tqdm_deprecate
    from .tests import _test_decorators
    _test_decorators.__name__ = ""
    with wrap_tqdm_deprecate(deprecation_warning=lambda: True,
                             trange=trange) as ctx_trange:
        ctx_trange.update(__name__="", func=tqdm)
        _test_decorators(trange=ctx_trange)

test_trange()

# Generated at 2022-06-14 13:12:58.084220
# Unit test for function trange
def test_trange():
    """Test `tqdm.auto.trange`"""
    from .gui import tqdm as gui_tqdm
    from .gui import trange as gui_trange
    for t, tr in zip((notebook_tqdm, gui_tqdm, asyncio_tqdm, std_tqdm),
                     (notebook_trange, gui_trange, trange, trange)):
        for x in [range(2), range(1)]:
            with t.external_write_mode():
                assert list(tr(x)) == list(x)
    for x in [range(2), range(1)]:
        assert list(trange(x)) == list(x)

# Generated at 2022-06-14 13:13:09.664521
# Unit test for function trange
def test_trange():
    """Test function trange"""
    import io
    import sys
    import time

    try:  # Python2
        from StringIO import StringIO  # noqa
    except ImportError:  # Python3
        from io import StringIO  # noqa

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ImportWarning)
        try:
            from tqdm import trange  # noqa
        except ImportError:
            from tqdm.auto import trange  # noqa

    # Test that trange works with tqdm.write()
    file = sys.stderr
    sys.stderr = StringIO()
    for _ in trange(3):
        _write_through('hello world\n')


# Generated at 2022-06-14 13:13:18.716364
# Unit test for function trange
def test_trange():
    """
    Runs unit test for `tqdm.auto.trange`.
    """
    from .utils import _supports_unicode  # prevent circular import
    from .std import tqdm, trange

    with tqdm(disable=True) as t:
        assert t.disable  # sanity check
        # Test normal arguments
        for i in trange(4, 7, 2):
            assert i in range(4, 7, 2)
        # Test positional arguments
        for i in trange(7):
            assert i in range(7)

    # Test total argument
    # (as of tqdm 4.30.0, islice() is not supported; so, trange() with
    #  total=X, disabling islice() by passing unit_scale=True, will result
    #  in X+1 iterations

# Generated at 2022-06-14 13:13:29.909923
# Unit test for function trange
def test_trange():
    """Test function `trange`."""
    assert list(trange(3)) == [0, 1, 2]
    assert list(trange(3, 5)) == [3, 4]
    assert list(trange(3, 9, 2)) == [3, 5, 7]
    assert list(trange(10, 5, -1)) == [10, 9, 8, 7, 6]
    assert list(trange(5, 9, 2)) == [5, 7]
    assert list(trange(5, 9, 10)) == [5]
    assert list(trange(9, 5, -2)) == [9, 7]
    assert list(trange(9, 5, -10)) == [9]
    assert list(trange(5, 5)) == []

# Generated at 2022-06-14 13:13:32.292132
# Unit test for function trange
def test_trange():
    for _ in trange(10):
        pass
    assert sum(trange(10)) == 45

# Generated at 2022-06-14 13:13:41.458716
# Unit test for function trange
def test_trange():
    """
    Unit test for `tqdm.auto.trange`.
    """
    from .std import trange
    from .utils import truncate_float
    from .std import _supports_unicode
    for n in range(1, 5):
        list(trange(n, desc="testing", leave=False))
        list(trange(n, leave=False))

        list(trange(n, ascii=True))
        list(trange(n, ascii=True, desc="testing"))
        list(trange(n, ascii=True, unit="foo"))
        list(trange(n, ascii=True, unit="foo", desc="testing"))

        if _supports_unicode():
            list(trange(n, desc=u"testing", leave=False))
            list

# Generated at 2022-06-14 13:13:46.993447
# Unit test for function trange
def test_trange():
    """Test that trange works as expected"""
    it = trange(2)
    assert str(next(it)) == "0/2" and str(next(it)) == "1/2"
    assert isinstance(next(it, None), type(None))

    it = trange(5, 0, -1)
    assert str(next(it)) == "5/5" and str(next(it)) == "4/5"

    for _ in trange(iterable=range(4)):
        pass



# Generated at 2022-06-14 13:13:56.341377
# Unit test for function trange
def test_trange():
    """Test for function `trange`"""
    from ._utils import _range
    from ._tqdm import trange as _trange
    from .tqdm_gui import trange as _trange_gui

    for module in (__import__(modname) for modname in ("numpy", "pandas", "cupy")):
        if hasattr(module, "arange"):
            arange = module.arange
            break
    else:
        arange = range

    trange_modules = [_trange, _trange_gui]
    assert tqdm.__name__ in [t.__name__ for t in trange_modules]

    with tqdm(total=1, leave=True) as pbar:
        assert pbar.total == 1

# Generated at 2022-06-14 13:13:57.957136
# Unit test for function trange
def test_trange():
    r = trange(5)
    assert (list(r) == [0, 1, 2, 3, 4])

# Generated at 2022-06-14 13:14:03.465829
# Unit test for function trange
def test_trange():
    """Test the function trange"""
    assert list(trange(10)) == list(tqdm(range(10)))
    assert list(trange(1, 10, 2)) == list(tqdm(range(1, 10, 2)))
    assert list(trange(10, 1, -2)) == list(tqdm(range(10, 1, -2)))
    assert list(trange(10, desc="desc")) == list(tqdm(range(10), desc="desc"))

# Generated at 2022-06-14 13:14:10.818610
# Unit test for function trange
def test_trange():
    """Test for function trange()"""
    list(trange(9))
    list(trange(5, 10))
    list(trange(0, 10, 2))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
        from .autonotebook import tqdm as libtqdm
        from .autonotebook import trange as libtrange
        assert trange is tqdm is libtrange is libtqdm


# Generated at 2022-06-14 13:14:19.829947
# Unit test for function trange
def test_trange():
    """Tests function `trange`."""
    from .tests import AccuracyTest
    from .utils import format_sizeof
    from .std import tqdm

    # Tests for trange
    for i in trange(4, 0, -1):
        assert i == tqdm(i, bar_format='{n_fmt}').n == tqdm(i, initial=i,
                                                            total=0,
                                                            bar_format='{n_fmt}').n
        assert i == tqdm(0, total=i, bar_format='{n_fmt}').n == tqdm(initial=i,
                                                                     bar_format='{n_fmt}').n
    listsize = 10000

# Generated at 2022-06-14 13:14:29.002216
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """

    # pylint: disable=locally-disabled, missing-docstring, invalid-name

    from math import gcd
    from random import randrange, uniform
    from fractions import Fraction
    from itertools import chain
    from time import sleep

    class Timer:
        def __init__(self, iterable, *args, **kwargs):
            self.tqdm_obj = tqdm(iterable, *args, **kwargs)
            self.iterable = iterable

        def __iter__(self):
            return self.tqdm_obj

        def __enter__(self):
            self.t0 = self.tqdm_obj.timer()
            return self

        def __exit__(self, *exc):
            self.t1 = self

# Generated at 2022-06-14 13:14:32.085491
# Unit test for function trange
def test_trange():
    import time
    try:
        for i in trange(3):
            time.sleep(0.1)
    except TypeError as e:
        if "__call__" not in str(e):
            raise e



# Generated at 2022-06-14 13:14:39.173217
# Unit test for function trange
def test_trange():
    """Test function trange."""
    from .tqdm import trange, TqdmExperimentalWarning
    from .tests import tests
    from .utils import _term_move_up

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
        from .autonotebook import trange as tnb_trange
        from .asyncio import trange as asy_trange

    # Test trange for each environment
    for trg in (trange, tnb_trange, asy_trange):
        with tests.capture_output() as (_, out):
            with trg(10, desc="Test trange") as t:
                t.write("start")
                for i in t:
                    t.write(".")

# Generated at 2022-06-14 13:14:43.193755
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    from .auto import trange
    import time
    for _ in trange(5, desc="foo"):
        time.sleep(0.01)
    for _ in trange(5, desc="bar", leave=True):
        time.sleep(0.01)

# Generated at 2022-06-14 13:14:48.309930
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange.
    """
    with tqdm(total=len(list(range(3)))) as pbar:
        for _ in trange(3):
            pbar.update()
    assert pbar.n == 3
    assert pbar.last_print_n == 3
    assert pbar.last_print_t == 3