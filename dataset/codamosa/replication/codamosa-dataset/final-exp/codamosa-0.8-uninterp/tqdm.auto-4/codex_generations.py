

# Generated at 2022-06-14 13:12:47.826366
# Unit test for function trange
def test_trange():
    """
    Unit test for `tqdm.auto.trange`
    """
    # test notebook_trange
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
        assert trange(5) == notebook_trange(5)

    # test asyncio_trange
    if sys.version_info < (3, 6):
        return  # no trange() here (fallback to notebook's)

    # test std_trange
    assert trange(5) == tqdm(range(5)) == list(range(5))
    assert trange(3, 7) == tqdm(range(3, 7)) == list(range(3, 7))
    assert trange(1, 10, 3) == tqdm(range(1, 10, 3))

# Generated at 2022-06-14 13:12:51.242944
# Unit test for function trange
def test_trange():
    """Unit test for function trange"""
    from pytest import raises

    with raises(TypeError):
        trange(3, 4, 5, 6, range_step=3)
    with raises(ValueError):
        trange(3, 4, 5, 6, -7)
    assert list(trange(1)) == [0]
    assert list(trange(1, 2)) == [1]
    assert list(trange(1, 2, 3)) == [1]
    assert list(trange(1, 2, 3, 4)) == [1]
    assert list(trange(1, 2, 3, 4, 5)) == [1]
    assert list(trange(1, 2, 3, 4, 5, 6)) == [1, 4]

# Generated at 2022-06-14 13:12:55.670452
# Unit test for function trange
def test_trange():
    """Test for trange"""
    from .std import tqdm as std_tqdm

    with std_tqdm(desc="test_trange") as t:
        for _ in t:
            pass

# Generated at 2022-06-14 13:12:56.996373
# Unit test for function trange
def test_trange():
    """Test function trange"""
    return 0

# Generated at 2022-06-14 13:13:08.811243
# Unit test for function trange
def test_trange():
    from .std import tqdm, trange
    for t in [tqdm, trange]:
        for t in [tqdm, trange]:
            L = []
            for _ in t(range(10)):
                L.append(None)
            assert len(L) == 10
            L = []
            for _ in t(iterable=range(5), total=5):
                L.append(None)
            assert len(L) == 5
            L = []
            for _ in t(iterable=range(5), total=10):
                L.append(None)
            assert len(L) == 5
            L = []
            for _ in t(iterable=range(10), total=5):
                L.append(None)
            assert len(L) == 5
            L = []

# Generated at 2022-06-14 13:13:18.111142
# Unit test for function trange
def test_trange():
    """Tests trange function"""
    from .utils import _range, FormatLabel
    # Range
    assert list(trange(4)) == list(_range(4))
    assert list(trange(5)) == list(_range(5))
    assert list(trange(6)) == list(_range(6))
    assert list(trange(7)) == list(_range(7))
    assert list(trange(8)) == list(_range(8))
    assert list(trange(9)) == list(_range(9))
    assert list(trange(10)) == list(_range(10))
    assert list(trange(20)) == list(_range(20))
    assert list(trange(30)) == list(_range(30))
    # Args

# Generated at 2022-06-14 13:13:29.724283
# Unit test for function trange
def test_trange():  # pylint: disable=missing-docstring
    from .std import NatTqdmDeprecationWarning

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=NatTqdmDeprecationWarning)

        # Test default values
        assert list(trange(0)) == []
        assert list(trange(0, 0)) == []
        assert list(trange(0, 1)) == []
        assert list(trange(1, 0)) == []
        assert list(trange(3)) == [0, 1, 2]
        assert list(trange(3, 3)) == []
        assert list(trange(3, 5)) == [3, 4]
        assert list(trange(5, 3)) == []
        assert list(trange(5, 4, -1)) == [5]


# Generated at 2022-06-14 13:13:34.733125
# Unit test for function trange
def test_trange():
    trange(4)

    for _ in trange(4):
        pass

    for _ in trange(4, 0, -1):
        pass

    for _ in trange(4, 0, -1, leave=True):
        pass


# Generated at 2022-06-14 13:13:42.342562
# Unit test for function trange
def test_trange():
    from .gui import tqdm
    from .std import format_sizeof

    # Test 1
    total = 10000
    r = trange(total, desc='Test 1')
    for i in r:
        if i == total / 2:
            r.set_description_str('Half-time!')
    assert r.n == total

    # Test 2
    total = 10000
    # Test dynamic_ncols=True
    r = trange(total, total=total, desc='Test 2')
    for i in r:
        if i == total / 2:
            r.set_description_str('Half-time!')
    assert r.n == total

    # Test 3
    total = 10000
    # Test dynamic_ncols=True
    r = trange(total, total=total, desc='Test 3')


# Generated at 2022-06-14 13:13:46.005882
# Unit test for function trange
def test_trange():
    list(trange(0))
    list(trange(1))
    list(trange(2))
    assert tqdm.__name__ in repr(trange(0))
    assert "0/1" in repr(trange(1))
    assert "0/2" in repr(trange(2))