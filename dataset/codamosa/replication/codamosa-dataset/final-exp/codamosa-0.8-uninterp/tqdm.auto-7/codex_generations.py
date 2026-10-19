

# Generated at 2022-06-14 13:12:24.744853
# Unit test for function trange
def test_trange():
    """Unit test for function trange"""
    import gc
    for _ in range(5):
        list(trange(3))
        gc.collect()

# Generated at 2022-06-14 13:12:32.729885
# Unit test for function trange
def test_trange():
    """
    Test for trange function
    """
    from .std import tqdm as sync_tqdm

    # Test basic functionality
    assert sum(trange(10)) == sum(range(10)) == 45, "trange(10) != range(10)"

    if sys.version_info[:2] < (3, 6):
        # Test `asyncio_tqdm` is not imported
        assert trange != asyncio_tqdm
        assert tqdm != asyncio_tqdm
    else:
        assert trange == asyncio_tqdm

# Generated at 2022-06-14 13:12:40.112335
# Unit test for function trange
def test_trange():
    """Test for function trange"""
    assert isinstance(list(trange(1)), list)
    assert isinstance(trange(1).__iter__(), tqdm)
    assert isinstance(trange(1).__aiter__(), tqdm)
    assert isinstance(trange(1).__aiter__().__aiter__(), tqdm)
    assert isinstance(trange(1, as_aiter=True), tqdm)



# Generated at 2022-06-14 13:12:42.431275
# Unit test for function trange
def test_trange():
    """Test that trange() works."""
    with trange(5) as t:
        for _ in t:
            pass


if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:12:45.679197
# Unit test for function trange
def test_trange():
    """
    Tests that trange is working correctly
    """
    from tqdm import trange
    from time import sleep
    for _ in trange(2, desc='trange test'):
        sleep(.1)

# Generated at 2022-06-14 13:12:48.263534
# Unit test for function trange
def test_trange():
    """Test the function trange"""
    a = trange(10, desc="trange", leave=True)
    assert len(list(a)) == 10

# Generated at 2022-06-14 13:12:54.927424
# Unit test for function trange
def test_trange():
    iterable = list(trange(0))
    assert not iterable

    iterable = list(trange(5))
    assert iterable == [0, 1, 2, 3, 4]

    iterable = list(trange(10, 15))
    assert iterable == [10, 11, 12, 13, 14]

    iterable = list(trange(10, 20, 2))
    assert iterable == [10, 12, 14, 16, 18]

    if sys.version_info[:2] < (3, 6):
        pass
    else:
        import asyncio
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(asyncio_tqdm(iterable))
        loop.run_until_complete(future)
        assert future.result() == iterable

# Generated at 2022-06-14 13:13:01.082369
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    from .std import reset_tqdm_state

    reset_tqdm_state()

    list(trange(2, 3))  # pylint: disable=expression-not-assigned
    list(trange(2, 3, desc="desc"))  # pylint: disable=expression-not-assigned

# Generated at 2022-06-14 13:13:10.353545
# Unit test for function trange
def test_trange():
    """
    Unit test for function `trange`.
    """
    from .std import tqdm, trange, __version__

    s = sum(trange(10, desc='foo', leave=True))
    assert s == 45

    s = sum(trange(10, desc='bar', leave=False))
    assert s == 45

    s = sum(trange(10, desc='bar', leave=False))
    assert s == 45

    if __version__ > '4.30.0':
        import time
        for _ in trange(10, mininterval=0.01):
            time.sleep(0.1)

# Generated at 2022-06-14 13:13:19.195260
# Unit test for function trange
def test_trange():
    from .utils import StatusPrinter
    from .std import FormatCustomTextType, FormatCustomTextExt, RawFormatCustomText

    class NewTqdm(tqdm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def format_dict(self):
            return {"n": self.n}

    # Check progressbar looks like trange's
    pbar = trange(0, 0)
    assert isinstance(pbar, tqdm)
    assert pbar.format_num_pos == 0  # default format_num_pos
    # Check bar string
    pbar = trange(0, 0, bar_format='{l_bar}{bar}{r_bar}')

# Generated at 2022-06-14 13:13:26.650974
# Unit test for function trange
def test_trange():
    from .std import tqdm
    import sys
    import re

    def strfdelta(seconds, fmt="%H:%M:%S"):
        d = datetime.timedelta(seconds=seconds)
        return d.days, d.seconds, d.microseconds

    class unit_test(object):
        """decorator for unit tests:
        run unit tests with -q flag to disable all print() calls"""
        def __init__(self, f):
            self.f = f

        def __call__(self, *args, **kwargs):
            if '-q' in sys.argv:
                with tqdm(total=1, disable=True) as t:
                    t.update(1)
                return
            return self.f(*args, **kwargs)


# Generated at 2022-06-14 13:13:33.360074
# Unit test for function trange
def test_trange():
    """Test for trange docstring"""
    assert trange(5) == list(tqdm(range(5)))
    assert trange(1, 5) == list(tqdm(range(1, 5)))
    assert trange(1, 5, 2) == list(tqdm(range(1, 5, 2)))
    assert trange(1, 5, 2, desc='desc', leave=True) == \
        list(tqdm(range(1, 5, 2), desc='desc', leave=True))
    for i in trange(4, desc='TrangeF', leave=True, ascii=True, unit='i'):
        assert i in range(4)



# Generated at 2022-06-14 13:13:38.322825
# Unit test for function trange
def test_trange():
    """ Unit tests for trange """
    from .std import tqdm
    assert tqdm is tqdm
    range_size = 7
    with tqdm(total=range_size, disable=None) as progressbar:
        for _ in progressbar:
            progressbar.update()
    assert progressbar.n == range_size

if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:13:41.308844
# Unit test for function trange
def test_trange():
    """Test trange works as expected."""
    from .std import tqdm

    with tqdm(total=10) as pbar:
        for _ in trange(10):
            pbar.update()

# Generated at 2022-06-14 13:13:47.130985
# Unit test for function trange
def test_trange():
    """Test function trange"""
    # Check that "desc" is inherited with trange
    assert trange(2, 3, desc="desc").desc == "desc"
    # Check that trange has iterable attributes
    tr = trange(2, 3)
    assert tr.start == 2
    assert tr.stop == 3
    assert tr.step == 1
    # Check that trange calls tqdm
    assert next(tr) == 2
    assert next(tr) == 3
    with pytest.raises(StopIteration):
        next(tqdm)



# Generated at 2022-06-14 13:13:55.659267
# Unit test for function trange
def test_trange():
    """
    Unit test function for function `trange`
    """
    from .auto import trange
    from .tests import common
    from .tqdm import CloseableFile, NullMonitor
    from .utils import _range

    # add `file` as cli for `sys.stderr`
    fout = CloseableFile(sys.stderr.buffer)

    for _ in trange(4, file=fout):
        for _ in trange(7, desc='BAR', leave=False, file=fout):
            for _ in trange(5):
                pass


# Generated at 2022-06-14 13:14:02.418335
# Unit test for function trange
def test_trange():
    """
    Unit test for `trange`.
    """
    from .utils import _term_move_up
    from .std import format_interval

    total = 10

    with trange(total) as t:
        for i in t:
            t.set_postfix(i=i)
            t.update()
        assert t.total == total
        assert t.n == total

        elapsed = t.elapsed
        assert elapsed > 0
        assert format_interval(elapsed)

        assert _term_move_up()
        t.close()



# Generated at 2022-06-14 13:14:04.222518
# Unit test for function trange
def test_trange():
    assert list(trange(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-14 13:14:10.816421
# Unit test for function trange
def test_trange():
    """
    Tests for function `trange`
    """
    for _ in trange(10):
        assert 1
    for _ in trange(10, desc="desc"):
        assert 1
    for _ in trange(10, desc="desc", bar_format="{l_bar} {bar} {r_bar}"):
        assert 1
    for _ in trange(10, desc="desc", total=100):
        assert 1



# Generated at 2022-06-14 13:14:12.364515
# Unit test for function trange
def test_trange():
    """Test for function trange"""
    for _ in trange(3, desc='trange'):
        pass