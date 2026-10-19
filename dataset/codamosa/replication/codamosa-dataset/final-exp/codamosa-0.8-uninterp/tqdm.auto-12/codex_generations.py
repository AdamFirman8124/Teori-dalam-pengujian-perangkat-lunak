

# Generated at 2022-06-14 13:12:40.111460
# Unit test for function trange
def test_trange():
    """Test trange by comparing with tqdm"""
    from time import sleep

    r = range(10)
    with tqdm(r) as t:
        for _ in trange(10):
            assert t.n == t.n + 1  # always true, so no progress made
            sleep(0.5)

# Generated at 2022-06-14 13:12:50.184609
# Unit test for function trange
def test_trange():
    """Test function trange"""
    import shutil
    from .std import format_sizeof

    assert shutil.get_terminal_size()[0] > 35  # check width > 35

    it = trange(10)
    for i in it:
        assert i == next(it.__iter__())
        if i == 3:
            break
    # check format_sizeof
    assert format_sizeof(0) == "0 B"
    assert format_sizeof(1) == "1 B"
    assert format_sizeof(1000) == "1000 B"
    assert format_sizeof(1024) == "1.0 KiB"
    assert format_sizeof(1500) == "1.5 KiB"
    assert format_sizeof(10000) == "9.8 KiB"
    assert format_sizeof

# Generated at 2022-06-14 13:12:59.259149
# Unit test for function trange
def test_trange():
    trange(0, 10)
    trange(1, 10)
    trange(10, 1)
    trange(10, 1, -1)
    trange(10, 0, -1)
    trange(10, -1, -1)
    trange(0, 10, 2)
    trange(0, 10, 3)
    trange(10, 0, -2)
    trange(10, 0, -3)
    trange(10, -1, -2)
    trange(10, -1, -3)

# Generated at 2022-06-14 13:13:10.452528
# Unit test for function trange
def test_trange():
    """Test for trange"""
    from .std import trange
    with trange(3) as t:
        for _ in t:
            pass
    with trange(3, desc='Custom trange', unit='i') as t:
        for _ in t:
            pass
    with trange(1, 3, desc='Custom trange', unit='i') as t:
        for _ in t:
           pass
    with trange(1, 3, 1, desc='Custom trange', unit='i') as t:
       for _ in t:
           pass
    if sys.version_info[:2] >= (3, 6):  # Python3.6+
        with trange(3, dynamic_ncols=True) as t:
            for _ in t:
                pass

# Generated at 2022-06-14 13:13:19.263797
# Unit test for function trange
def test_trange():
    """Test for function trange"""
    from ._test_subprocess import _test_keyboard_interrupt

    from .std import _range as range

    # Test range wrapper
    for s in [1, 2, 3, 1000]:
        assert list(trange(s, desc='range')) == list(range(s))

    # Test multi-wrapper
    assert tqdm(range(4)) != notebook_tqdm(range(4))
    assert tqdm(range(4)) != asyncio_tqdm(range(4))

    # Test default values
    t = tqdm()
    assert next(t) == 0
    t.close()

    t = tqdm(10, ncols=150)
    assert len(str(t)) > 150
    t.close()


# Generated at 2022-06-14 13:13:24.709764
# Unit test for function trange
def test_trange():
    """
    Tests that `trange` function is actually an alias.
    """
    assert tqdm.__base__ == notebook_tqdm
    assert tqdm.__base__ is not std_tqdm
    assert tqdm(range(3)) is not None
    assert trange(3) is not None

# Generated at 2022-06-14 13:13:29.176780
# Unit test for function trange
def test_trange():
    """
    Unit tests for function trange
    """
    trange_output = list(trange(3))
    assert (trange_output == [0, 1, 2]), \
        "trange(3) failed: {}".format(trange_output)

if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:13:39.718791
# Unit test for function trange
def test_trange():
    # Test trange(1, 2) returns [1]
    # Test trange(2, 4) returns [2, 3]
    # Test trange(0, 4, 2) returns [0, 2]
    assert list(trange(1, 2)) == [1]
    assert list(trange(2, 4)) == [2, 3]
    assert list(trange(0, 4, 2)) == [0, 2]
    # Test trange(0, 0, 2) returns []
    assert list(trange(0, 0, 2)) == []
    # Test trange(0) returns []
    assert list(trange(0)) == []
    # Test trange(0, -4, -2) returns [0, -2]

# Generated at 2022-06-14 13:13:43.566926
# Unit test for function trange
def test_trange():
    """Simple sanity check."""
    return trange(3)


if __name__ == "__main__":
    from ._utils import _test_env  # noqa: F401
    _test_env()
    from ._utils.report import Report
    Report().plot(tests=[test_trange])

# Generated at 2022-06-14 13:13:50.983156
# Unit test for function trange
def test_trange():
    """Test for trange like range"""
    for func in (tqdm, trange):
        a = func(100)
        assert isinstance(a, tqdm)
        next(a)
        assert a.n == 1
        a.update(100)
        assert a.n == 101
        a.update()
        assert a.n == 102
        a.close()