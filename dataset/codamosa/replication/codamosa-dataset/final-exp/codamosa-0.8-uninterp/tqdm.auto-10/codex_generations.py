

# Generated at 2022-06-14 13:12:36.547576
# Unit test for function trange
def test_trange():
    """
    Test tqdm.tauto.trange.
    """
    assert list(trange(5)) == [0, 1, 2, 3, 4]

# Generated at 2022-06-14 13:12:38.548961
# Unit test for function trange
def test_trange():
    """
    >>> list(trange(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    pass

# Generated at 2022-06-14 13:12:49.374310
# Unit test for function trange
def test_trange():
    """
    Tests that function trange works as expected.
    """

# Generated at 2022-06-14 13:13:01.226945
# Unit test for function trange
def test_trange():  # pragma: no cover
    from inspect import signature
    from .utils import Range
    assert trange in (notebook_trange, asyncio_tqdm.__base__.trange)
    assert len(signature(Range).parameters) == len(signature(trange).parameters)
    assert list(trange(3)) == list(range(3))
    assert list(trange(3, 1)) == list(range(3, 1))
    assert "unit" in signature(trange).parameters
    assert trange(3, unit="foos")[0].unit == "foos"
    assert trange(3, unit="foos")[0].total == 3
    assert trange(3, unit="foos")[-1].n == 2

# Generated at 2022-06-14 13:13:12.601670
# Unit test for function trange
def test_trange():
    from ._monitoring import B; from .gui import tqdm

    import time
    for i in trange(4, desc='1st loop'):
        for j in trange(5, desc='2nd loop', leave=False):
            for k in trange(50, desc='3nd loop'):
                time.sleep(0.01)

    tqdm.clear()
    with tqdm(total=100, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
        pbar.update(1)
        pbar.update(1)
        pbar.update(1)
        pbar.update(1)
        pbar.update(1)
        pbar.update(1)
        pbar.update(1)
        pbar.update(1)
        p

# Generated at 2022-06-14 13:13:18.158184
# Unit test for function trange
def test_trange():  # pragma: no cover
    from numpy.random import rand
    from time import sleep

    total = 100
    with trange(total) as t:
        for i in t:
            sleep(rand()/10)
            t.set_description("Step %i" % (i+1))
    print("\n")

    total = 10
    for x in trange(total, desc='1st loop', leave=True):
        for y in trange(total, desc='2nd loop', leave=False):
            for z in trange(total, desc='3nd loop', leave=False):
                sleep(rand()/100)

    # empty
    for _ in trange(0):  # pragma: no cover
        pass

    # check for incorrect use cases

# Generated at 2022-06-14 13:13:22.820790
# Unit test for function trange
def test_trange():
    """
    Tests that `trange` is functional.
    """
    assert trange(0)
    assert trange(0, 1)
    assert trange(5, 6)
    assert trange(5, 7, 2)



# Generated at 2022-06-14 13:13:31.313827
# Unit test for function trange
def test_trange():
    """Ensure trange works as expected"""
    expected = list(range(10))
    assert list(trange(len(expected))) == expected
    assert list(trange(len(expected), desc='foo')) == expected
    assert list(trange(len(expected), 0)) == expected
    assert list(trange(len(expected), total=0)) == expected
    assert list(trange(len(expected), 1, 0.01)) == expected
    assert list(trange(len(expected), ncols=0)) == expected
    assert list(trange(len(expected), miniters=0)) == expected
    assert list(trange(len(expected), mininterval=0)) == expected

# Generated at 2022-06-14 13:13:41.007907
# Unit test for function trange
def test_trange():
    """Test the function trange"""
    # Note: The following test functions are duplicated in trange.py
    def _assert_wrapped_range(t, n=None, **kwargs):
        """Check that t is wrapper of range(n, **kwargs)"""
        if n is None:
            n = next(t)
        assert t.n == n
        assert list(t) == list(range(n, **kwargs))

    def _assert_trange_is_tqdm_class(t, *args, **kwargs):
        """Check that t is an instance of the tqdm class"""
        assert isinstance(t, tqdm)
        t(*args, **kwargs)


# Generated at 2022-06-14 13:13:42.733638
# Unit test for function trange
def test_trange():
    """Unit test for trange"""
    from .std import tqdm
    list(tqdm(trange(10)))

# Generated at 2022-06-14 13:13:50.737031
# Unit test for function trange
def test_trange():
    assert list(trange(1000)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(trange(1000, 100)) == list(range(1000, 100))
    assert list(trange(1000, 0, -1)) == list(range(1000, 0, -1))

# Generated at 2022-06-14 13:13:56.196234
# Unit test for function trange
def test_trange():
    """
    Test if trange is behaving as expected.
    """
    for lo in range(5):
        for hi in range(lo, 5):
            for step in range(1, 3):
                out = list(trange(lo, hi, step))
                assert out == list(range(lo, hi, step))
                assert len(out) == len(trange(lo, hi, step, leave=True))


test_trange()

# Generated at 2022-06-14 13:13:59.090554
# Unit test for function trange
def test_trange():  # pragma: no cover
    from .std import tqdm
    import time

    for i in trange(100):
        time.sleep(0.01)
    assert tqdm(range(100), desc="trange unit test").total == 100

# Generated at 2022-06-14 13:14:02.468393
# Unit test for function trange
def test_trange():  # pragma: no cover
    for _ in trange(4):
        for _ in trange(4, 8):
            for _ in trange(8, 12):
                pass


if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:14:07.094428
# Unit test for function trange
def test_trange():
    for _ in trange(10):
        pass
    for _ in trange(10, desc='foo'):
        pass
    for _ in trange(10, desc='foo', leave=False):
        pass
    for _ in trange(10, desc='foo', leave=True):
        pass

# Generated at 2022-06-14 13:14:09.447064
# Unit test for function trange
def test_trange():
    """
    Unit test for `trange` function.
    """
    assert list(trange(5)) == [0, 1, 2, 3, 4]

# Generated at 2022-06-14 13:14:13.651270
# Unit test for function trange
def test_trange():
    """Test that trange works identical to tqdm"""
    from .std import tqdm
    for islice in [slice(None), slice(1, 10, 2), slice(10, 0, -2)]:
        assert list(trange(20)[islice]) == list(tqdm(range(20))[islice])

# Generated at 2022-06-14 13:14:14.355279
# Unit test for function trange
def test_trange():
    """
    Test for function trange
    """
    for _ in trange(10):
        pass

# Generated at 2022-06-14 13:14:19.116282
# Unit test for function trange
def test_trange():
    """ Test function trange """
    with trange(10) as t:
        [t.update() for _ in t]
    with trange(10, desc="test", leave=False) as t:
        [t.update() for _ in t]
    with tqdm(range(10), desc="test", leave=False) as t:
        [t.update() for _ in t]

# Generated at 2022-06-14 13:14:28.298138
# Unit test for function trange
def test_trange():
    """Test Shortcut `tqdm.auto.trange`"""
    import sys
    from .std import _term_move_up

    stdout, sys.stdout = sys.stdout, sys.__stdout__