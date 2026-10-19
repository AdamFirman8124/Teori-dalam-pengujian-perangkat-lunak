

# Generated at 2022-06-14 13:12:38.179451
# Unit test for function trange
def test_trange():
    """Tests that trange produces the same output as tqdm(range)"""
    from .tests_tqdm import _range
    from .utils import _supports_unicode
    from .std import format_interval, format_sizeof

    if sys.version_info[:2] < (3, 6):
        assert tqdm == notebook_tqdm
        assert trange == notebook_trange
    assert tqdm != notebook_tqdm

    t, n = tqdm(), 10
    assert len(t.format_number()) == len(str(n))
    assert t.format_interval(123456) == format_interval(123456)


# Generated at 2022-06-14 13:12:41.043987
# Unit test for function trange
def test_trange():
    """
    Test for trange()
    """
    from .auto import trange
    for _ in trange(10):
        pass

# Generated at 2022-06-14 13:12:44.355524
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange.
    """
    from .tests import TestTrangeNoTqdm
    TestTrangeNoTqdm.test_func_trange()

# Generated at 2022-06-14 13:12:45.940249
# Unit test for function trange
def test_trange():
    """Test for function trange"""
    for i in trange(10):
        list(range(100))

# Generated at 2022-06-14 13:12:49.449067
# Unit test for function trange
def test_trange():
    """Test trange function."""
    assert trange(1)
    assert isinstance(trange(1), tqdm)
    assert trange(1, 2)
    assert isinstance(trange(1, 2), tqdm)

# Generated at 2022-06-14 13:12:57.835120
# Unit test for function trange
def test_trange():
    "Test function `trange` (pylint must pass)"
    assert list(trange(5)) == list(range(5))
    assert list(trange(1, 6)) == list(range(1, 6))
    assert list(trange(1, 8, 2)) == list(range(1, 8, 2))
    assert list(trange(0)) == list(range(0))
    assert list(trange(1, -6, -2)) == list(range(1, -6, -2))



# Generated at 2022-06-14 13:13:01.888948
# Unit test for function trange
def test_trange():
    """Test trange"""
    assert trange(10)._total == 10
    assert trange(2, 7)._total == 5
    assert trange(2, 7, 1)._total == 5
    assert trange(2, 7, 3)._total == 2

# Generated at 2022-06-14 13:13:12.555693
# Unit test for function trange
def test_trange():
    """
    Unit tests for function `tqdm.auto.trange`.
    """
    # pylint: disable=redefined-outer-name
    import time
    import random
    from .std import tqdm as std_tqdm  # pylint: disable=unused-variable

    # Force tqdm to use tqdm.auto.trange instead of tqdm.std.trange
    import tqdm.std as tqdm

    for _ in trange(3, desc='Trange'):
        for _ in tqdm.trange(random.randint(1, 100)):
            time.sleep(0.01)

if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:13:15.614571
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    N = 1000
    assert list(trange(N)) == list(range(N))
    assert list(trange(N, N + 10)) == list(range(N, N + 10))

# Generated at 2022-06-14 13:13:17.741499
# Unit test for function trange
def test_trange():
    """Test for function trange (unit tests for function tqdm
    are done in asyncio and autonotebook modules"""
    assert list(trange(3)) == list(range(3))