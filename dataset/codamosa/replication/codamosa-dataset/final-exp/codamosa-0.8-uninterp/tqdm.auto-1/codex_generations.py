

# Generated at 2022-06-14 13:12:33.098743
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    with trange(3) as t:
        assert len(t) == 3

# Generated at 2022-06-14 13:12:38.074024
# Unit test for function trange
def test_trange():
    """Test for trange"""
    trange_test = trange(0, 1, ncols=75, mininterval=0.1)
    for _ in trange_test:
        trange_test.update(1)
    assert trange_test.n == 1
    assert trange_test.miniters == 1
    assert trange_test.mininterval == 0.1
    assert trange_test.ncols == 75



# Generated at 2022-06-14 13:12:49.143409
# Unit test for function trange
def test_trange():
    from .std import _range
    from .utils import _term_move_up

    class UnicodeIOWrapper():  # pylint: disable=too-few-public-methods
        """
        Simple wrapper around StringIO class to simulate stdout or
        stderr file object
        """

        def __init__(self):
            self._string = unicode()

        def write(self, x):
            self._string += x

        def flush(self):
            return

        def getvalue(self):
            return self._string

    # Initialize variables needed for testing
    range_it = _range(1, 101, unit_scale=True)
    monitor_it = _range(1, 101, unit_scale=False)
    # Range is 101 because each element takes a newline in the loop
    with_ascii_

# Generated at 2022-06-14 13:12:56.741309
# Unit test for function trange
def test_trange():
    """
    Tests `tqdm.auto.trange`
    """
    from .std import tqdm

    assert tqdm(trange(5)).__iter__() is tqdm(range(5)).__iter__()
    assert tqdm(trange(5)).__next__() == tqdm(range(5)).__next__()
    assert tqdm(trange(5)).__getattr__('reset') == tqdm(range(5)).__getattr__('reset')

# Generated at 2022-06-14 13:13:00.693694
# Unit test for function trange
def test_trange():
    """
    Test function trange
    """
    all_ = []
    for _ in trange(10):
        all_.append(1)
    assert sum(all_) == 10
    assert len(all_) == 10

# Generated at 2022-06-14 13:13:12.064475
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange.
    """
    # Check that trange works with no kwargs
    list(trange(3))
    # Check that trange works with kwarg
    list(trange(3, leave=True))

    if sys.version_info[:2] >= (3, 6):
        from .asyncio import tqdm as asyncio_tqdm  # pylint: disable=reimported
        from .std import tqdm as std_tqdm  # pylint: disable=reimported

        # Check that trange works with asyncio_tqdm
        list(trange(3, tqdm=asyncio_tqdm))
        # Check that trange works with std_tqdm

# Generated at 2022-06-14 13:13:19.706447
# Unit test for function trange
def test_trange():
    """Unit test for function trange"""

    with tqdm(total=2) as pbar:
        assert not pbar.disable
        with trange(2) as pbar2:
            assert not pbar2.disable
            assert len(pbar2) == 2
            assert pbar2.total == 2
            assert len(pbar2) == pbar2.total
            assert not pbar2.desc
            assert not pbar2.total
            assert pbar2.miniters == 1
            assert pbar2.unit_scale is False
            assert pbar2.unit == ''
            assert pbar2.postfix == {}
            assert pbar2.file.name == sys.stdout.name
            assert pbar2.leave is False

# Generated at 2022-06-14 13:13:29.765451
# Unit test for function trange
def test_trange():
    """
    Simple unit test for `tqdm.auto.trange`
    """
    assert list(trange(100)) == list(range(100))
    assert tuple(trange(10, 20, 2)) == tuple(range(10, 20, 2))
    assert tuple(trange(20, 10, -2)) == tuple(range(20, 10, -2))
    assert tuple(trange(1, 10, 5)) == tuple(range(1, 10, 5))
    assert list(trange(1, 2, 0.5)) == [1.0, 1.5]
    assert tuple(trange(0, 10, 0.5, dtype=int)) == tuple(range(0, 20, 1))

# Generated at 2022-06-14 13:13:35.519332
# Unit test for function trange
def test_trange():
    from .std import trange
    actual = list(trange(10))
    assert actual == list(range(10))
    actual = list(trange(0))
    assert actual == list(range(0))
    actual = list(trange(10, 1000, 100))
    assert actual == list(range(10, 1000, 100))

# Generated at 2022-06-14 13:13:37.900686
# Unit test for function trange
def test_trange():
    from .tests import test_range

    test_range(trange, "auto")


if __name__ == "__main__":
    test_trange()