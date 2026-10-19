

# Generated at 2022-06-14 13:12:37.754623
# Unit test for function trange
def test_trange():
    """Smoke test for trange"""
    list(trange(3))

# Generated at 2022-06-14 13:12:48.141167
# Unit test for function trange
def test_trange():
    """
    Tests whether trange() is called correctly and returns tqdm.
    """
    assert trange(1) == tqdm(range(1))
    assert trange(2, 3) == tqdm(range(2, 3))
    assert trange(4, 5, 6) == tqdm(range(4, 5, 6))
    assert trange(7, 8, 9, 10) == tqdm(range(7, 8, 9, 10))  # pylint: disable=E1123
    assert trange(11, 12, 13, 14, 15) == tqdm(range(11, 12, 13, 14, 15))  # pylint: disable=E1123

# Generated at 2022-06-14 13:12:59.210098
# Unit test for function trange
def test_trange():
    """
    Tests trange().
    """
    assert len(list(trange(0))) == 0
    assert len(list(trange(4))) == 4
    assert len(list(trange(4, 0))) == 0
    assert len(list(trange(4, -4))) == 0
    assert len(list(trange(4, -2))) == 2
    assert len(list(trange(4, -3))) == 1
    assert len(list(trange(4, -4, -1))) == 4
    assert len(list(trange(4, -4, 2))) == 0
    assert len(list(trange(4, -4, -2))) == 2
    assert len(list(trange(0, 10, 3))) == 4

# Generated at 2022-06-14 13:13:07.850207
# Unit test for function trange
def test_trange():
    for _ in range(3):
        assert list(trange(3)) == [0, 1, 2]
        assert list(trange(1, 3)) == [1, 2]
        assert list(trange(1, 3, 2)) == [1]
        assert list(trange(3, 1)) == []
        assert list(trange(3, 1, -1)) == [3, 2, 1]
        assert list(trange(3, 1, -2)) == [3]

if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:13:16.583217
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange.
    """
    for _ in trange(3, leave=False):
        pass
    assert _ == 2
    for _ in trange(3):
        pass
    assert _ == 2

    # Check limits
    i = 0
    for _ in trange(10, mininterval=0.01, miniters=1, leave=True):
        i += 1
        if i > 100:
            break

    # Check limits + mininterval
    i = 0
    for _ in trange(10, mininterval=0.05, miniters=1, leave=True):
        i += 1
        if i > 100:
            break
    assert _ == 99

# Generated at 2022-06-14 13:13:19.974799
# Unit test for function trange
def test_trange():
    """Test that trange works"""
    with tqdm(trange(16), unit='B', unit_scale=True) as bar:
        for _ in bar:
            pass

# Generated at 2022-06-14 13:13:26.287013
# Unit test for function trange
def test_trange():
    """Test trange"""
    # Test trange initialisation
    with trange(10) as t:
        assert len(t) == 10
    # Test trange repr
    assert repr(t) == "trange(10)"
    # Test trange iteration
    i = 0
    for _ in trange(10):
        i += 1
    assert i == 10



# Generated at 2022-06-14 13:13:33.773666
# Unit test for function trange
def test_trange():  # pragma: no cover
    """
    Unit tests for function trange.
    """
    import sys
    from .autonotebook import trange as _trange
    l = list(trange(7))
    assert l == list(_trange(7)) == list(range(7))
    l = list(trange(sys.maxsize))
    assert l == list(_trange(sys.maxsize)) == list(range(sys.maxsize))
    l = list(trange(1, sys.maxsize))
    assert l == list(_trange(1, sys.maxsize)) == list(range(1, sys.maxsize))
    l = list(trange(1, sys.maxsize, 2))

# Generated at 2022-06-14 13:13:36.002339
# Unit test for function trange
def test_trange():
    """Test for trange."""
    expected = list(range(5))
    got = list(trange(5))
    assert got == expected

# Generated at 2022-06-14 13:13:37.527097
# Unit test for function trange
def test_trange():
    """ Unit tests for function trange """
    # nosec
    for _ in trange(10):
        pass