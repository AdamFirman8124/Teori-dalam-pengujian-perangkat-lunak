

# Generated at 2022-06-14 13:12:33.181784
# Unit test for function trange
def test_trange():
    """Test the trange function"""
    expected_output = list(range(5))
    output = list(trange(5))
    assert ou

# Generated at 2022-06-14 13:12:40.840552
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    from ._utils import _range as range
    assert list(trange(0)) == []
    assert list(trange(1, 0)) == []
    assert list(trange(0, 1)) == [0]
    assert list(trange(1, 2)) == [1]
    assert list(trange(-1, 2)) == [0, 1]
    assert list(trange(-1, -2, -1)) == [-1]
    assert list(trange(-1, -2)) == []
    assert list(trange(-1, -2, -2)) == []
    assert list(trange(-2, -1, -2)) == []
    assert list(trange(-2, -1)) == []

# Generated at 2022-06-14 13:12:50.734990
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    # no tqdm
    assert list(trange(4, disable=True)) == list(range(4))
    assert list(trange(0)) == list(range(0))

    # Regular version
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
        assert list(trange(4)) == list(range(4))
        assert list(trange(0)) == list(range(0))

    # Async version
    if sys.version_info[:2] >= (3, 6):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=TqdmExperimentalWarning)

# Generated at 2022-06-14 13:12:55.829360
# Unit test for function trange
def test_trange():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
        assert sum(trange(100)) == sum(range(100))


if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:13:05.749867
# Unit test for function trange
def test_trange():  # pragma: no cover
    """Unit test for function trange"""
    assert list(trange(2, 3)) == [2]
    assert list(trange(2, 3, 1)) == [2]
    assert list(trange(3, 2, -1)) == [3]
    assert list(trange(2, 3, 0.5)) == [2.0, 2.5]
    assert list(trange(2, 3, 0.75)) == [2.0, 2.75]
    assert list(trange(2, 3, 0.2)) == [2.0, 2.2, 2.4, 2.6, 2.8]

# Generated at 2022-06-14 13:13:11.865295
# Unit test for function trange
def test_trange():
    """
    Tests `trange(...)`
    """
    # Check if trange is iterable
    assert sum(trange(10)) == 45

    # Test negative (non-unit) step
    assert sum(trange(10, 0, -2)) == 25
    assert list(trange(10, 0, -2)) == [10, 8, 6, 4, 2]



# Generated at 2022-06-14 13:13:20.078944
# Unit test for function trange
def test_trange():
    """Test trange"""
    # Test if iterable or int
    list(tqdm(range(3), desc='0'))
    list(tqdm(3, desc='1'))

    # Test if retval and position are not changed
    assert trange(3, position=0, desc='2') == range(3)
    assert trange(3, position=1, desc='3') == range(3)
    assert trange(3, position=2, desc='4') == range(3)

    # Test if desc is copied
    assert trange(3, desc='5') == tqdm(range(3), desc='5')

    # Test if all other kwargs are forwarded to tqdm

# Generated at 2022-06-14 13:13:24.151548
# Unit test for function trange
def test_trange():
    """
    Simple test to verify that `trange` works as expected.
    """
    assert list(trange(1)) == [0]
    assert list(trange(2)) == [0, 1]

# Generated at 2022-06-14 13:13:26.475557
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    from .std import total
    assert total(trange(5)) == 5

# Generated at 2022-06-14 13:13:30.285059
# Unit test for function trange
def test_trange():
    from .autonotebook import trange as _trange
    from .asyncio import trange as _trange_asyncio

    for _trange_func in [_trange, _trange_asyncio]:
        assert list(_trange_func(10)) == list(trange(10))