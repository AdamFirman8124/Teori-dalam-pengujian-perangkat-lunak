

# Generated at 2022-06-14 13:12:42.190032
# Unit test for function trange
def test_trange():
    """Runs trange unit tests"""
    from .utils import _range
    from .std import format_interval
    from .std import sleep as std_sleep
    try:
        from time import monotonic  # Python3.3+
    except ImportError:
        from time import time as monotonic
    try:
        from math import isclose
    except ImportError:  # Python<3.5
        def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
            return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

    # Test trange
    list(trange(3))

    # Test dynamic format_interval
    tlast = monotonic()

# Generated at 2022-06-14 13:12:51.751492
# Unit test for function trange
def test_trange():
    """Test that trange is properly replaced by tqdm"""
    global trange, tqdm  # pylint: disable=global-statement
    from tqdm.std import tqdm as std_tqdm, trange as std_trange
    from tqdm.auto import tqdm as auto_tqdm, trange as auto_trange
    from tqdm import auto as orig_auto
    from io import StringIO
    save_tqdm = tqdm

    tqdm = std_tqdm
    trange = std_trange
    out = StringIO()
    trange(0)
    assert "Range\n|0/0 [00:00<" in out.getvalue()
    out = StringIO()
    trange(0, bar_format="{l_bar}")
   

# Generated at 2022-06-14 13:12:57.095562
# Unit test for function trange
def test_trange():
    """Test for function `trange`."""
    with trange(10) as t:
        for _ in t:
            pass
    assert '10it' in repr(t)


# Test autonotebook vs asyncio

# Generated at 2022-06-14 13:12:58.719131
# Unit test for function trange
def test_trange():
    """
    Unit tests for function trange.
    """
    trange(10)

# Generated at 2022-06-14 13:13:03.914428
# Unit test for function trange
def test_trange():  # pragma: no cover
    """
    Tests trange.
    """
    from .std import trange as std_trange
    from .asyncio import trange as asyncio_trange

    if sys.version_info[:2] >= (3, 6):
        assert trange == asyncio_trange
    else:
        assert trange == std_trange

# Generated at 2022-06-14 13:13:06.378473
# Unit test for function trange
def test_trange():
    """Test for trange function"""
    for _ in trange(4):
        pass

# Generated at 2022-06-14 13:13:16.624445
# Unit test for function trange
def test_trange():
    """
    Unit test for trange()
    """
    from .std import format_interval as fmt_intv
    from .std import tqdm_total_seconds as ts

    def deque(maxlen=None):
        """Deque implementation for Python2.6"""
        return [], 0, 0, maxlen

    def append(it, x):
        """Append to deque implementation for Python2.6"""
        it[0].append(x)
        it[1] += 1

    def extend(it, iterable):
        """Extend deque implementation for Python2.6"""
        it[0].extend(iterable)
        it[1] += len(iterable)

    def popleft(it):
        """Pop left (head) from deque implementation for Python2.6"""
        x = it

# Generated at 2022-06-14 13:13:18.920714
# Unit test for function trange
def test_trange():
    """Unit test for `trange`"""
    trange(3)

# Generated at 2022-06-14 13:13:30.024595
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    from .std import tqdm

    # Null case
    list(trange(0, 0))

    # Basic case
    t = trange(3)
    assert len([x for x in t]) == 3
    t.close()

    # Check bar_format propagates
    bf = '{l_bar}{bar}| {n_fmt}/{total_fmt} ['
    t = trange(4, bar_format=bf)
    for i, j in zip(t, range(4)):
        assert t.format_dict["l_bar"] == bf[:-2]
    t.close()

    return tqdm.__test__  # for nose tests


if tqdm.__test__:
    test_trange()

# Generated at 2022-06-14 13:13:36.096936
# Unit test for function trange
def test_trange():
    """
    Tests `trange` function.
    """
    assert list(trange(10, desc='1st loop')) == list(range(10))
    assert list(trange(10, desc='2nd loop', leave=True)) == list(range(10))
    assert list(trange(10, desc='3nd loop')) == list(range(10))

# Generated at 2022-06-14 13:13:43.922872
# Unit test for function trange
def test_trange():
    """Test trange function"""
    assert list(trange(0)) == []
    assert list(trange(1)) == [0]
    assert list(trange(3, 1)) == []
    assert list(trange(1, 3)) == [1, 2]
    assert list(trange(1, 4, 2)) == [1, 3]
    assert list(trange(10, 0, -1)) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Generated at 2022-06-14 13:13:52.509002
# Unit test for function trange
def test_trange():
    """Test function trange"""
    from .auto import trange

    def func():
        for _ in trange(3, desc='1st loop'):
            for _ in trange(5, desc='2nd loop', leave=False):
                for _ in trange(7, desc='3rd loop'):
                    for _ in trange(11, desc='4th loop', leave=False):
                        yield  # Do an actual task during the test

    progress_generator = func()
    for _ in progress_generator:
        pass

# Generated at 2022-06-14 13:13:54.964608
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """

    for i in trange(4):
        assert i in [0, 1, 2, 3]

# Generated at 2022-06-14 13:13:59.017841
# Unit test for function trange
def test_trange():
    """Test trange function"""
    assert list(trange(10)) == list(range(10))
    assert list(trange(10, 1)) == list(range(10, 1))
    assert list(trange(1, 10, 2)) == list(range(1, 10, 2))


# Test tqdm against trange

# Generated at 2022-06-14 13:14:04.527193
# Unit test for function trange
def test_trange():
    """Test function `trange`."""
    from .std import format_interval
    from .tqdm import tnrange
    range_it = trange(10)
    assert isinstance(range_it, tnrange)
    assert range_it.__length_hint__() == 10
    list(range_it)  # consume iterator
    assert isinstance(range_it.miniters, int)
    list(trange(10, miniters=10))
    assert format_interval(0.000123456789) == "0.000123"
    assert format_interval(0.000000123456789) == "1.23e-07"
    list(trange(10, leave=True))
    assert "ms" in format_interval(0.3)

# Generated at 2022-06-14 13:14:09.320348
# Unit test for function trange
def test_trange():
    assert list(trange(4)) == list(range(4))
    assert list(trange(4, 4)) == list(range(4, 4))
    assert list(trange(4, 4, 1)) == list(range(4, 4, 1))



# Generated at 2022-06-14 13:14:10.212941
# Unit test for function trange
def test_trange():
    assert isinstance(trange(3), tqdm)

# Generated at 2022-06-14 13:14:14.412223
# Unit test for function trange
def test_trange():
    """ Test trange """
    import os
    try:
        with open(os.devnull, 'w') as fout:
            for _ in trange(1, 4):
                fout.write('testing')
    except Exception as e:
        raise type(e)(e.message).with_traceback(sys.exc_info()[2])

# Generated at 2022-06-14 13:14:15.340642
# Unit test for function trange
def test_trange():
    from ._utils import _range, _suppress_stderr
    with _suppress_stderr():
        for _ in trange(_range()):
            pass

# Generated at 2022-06-14 13:14:21.878600
# Unit test for function trange
def test_trange():
    """Test trange"""
    from .utils import _range
    # Setup
    control = notebook_tqdm(range(2))
    test = tqdm(range(2))
    # Test
    assert str(control) == str(test)
    # Cleanup
    control.close()
    test.close()
    del control, test
    # Test trange
    control = notebook_tqdm(_range(3))
    test = trange(3)
    assert str(control) == str(test)
    control.close()
    test.close()
    del control, test