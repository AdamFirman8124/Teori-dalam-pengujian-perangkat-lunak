

# Generated at 2022-06-14 13:12:27.431638
# Unit test for function trange
def test_trange():
    """Test whether trange arguments are correctly passed to tqdm"""
    try:
        from IPython import get_ipython  # NOQA

        ipy = True
    except ImportError:
        ipy = False

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
        try:
            import asyncio  # NOQA
        except ImportError:
            asyncio = None

    # Base case
    t = trange(10, desc="Ordinary trange", ncols=100, leave=False)
    for i in t:
        assert i == t.n
        t.set_postfix(refresh=ipy)
    assert t.total == 10
    assert t.desc == "Ordinary trange"
    assert t.ncols == 100


# Generated at 2022-06-14 13:12:31.971922
# Unit test for function trange
def test_trange():
    """Test for trange function for trange(10) and trange(0)"""
    # Check position count
    for i in trange(10):
        pass
    assert i == 9

    # Check position count
    for i in trange(0):
        pass
    assert i == 0

# Generated at 2022-06-14 13:12:33.724256
# Unit test for function trange
def test_trange():
    """test trange"""
    assert list(trange(3)) == [0, 1, 2]

# Generated at 2022-06-14 13:12:45.381062
# Unit test for function trange
def test_trange():
    """ Test trange() function """
    # Test with only one arg
    a = trange(2)
    assert a.miniters == 1
    assert a.maxiters == 2
    assert a.mininterval == 0.1
    assert list(a) == [0, 1]

    # Test with two args
    a = trange(2, 4)
    assert a.miniters == 1
    assert a.maxiters == 2
    assert a.mininterval == 0.1
    assert list(a) == [2, 3]

    # Test with three args
    a = trange(3, 6, 2)
    assert a.miniters == 1
    assert a.maxiters == 3
    assert a.mininterval == 0.1
    assert list(a) == [3, 5]



# Generated at 2022-06-14 13:12:53.108169
# Unit test for function trange
def test_trange():
    "Test trange"
    from .std import _range
    # Explicit special case for 0
    assert not list(trange(0))
    # Explicitly test for trange
    assert list(trange(5)) == list(range(5))
    assert list(trange(5, 0)) == list(_range(5, 0, -1))
    assert list(trange(5, 1, -1)) == list(_range(5, 1, -1))
    assert list(trange(5, -1, -1)) == list(_range(5, -1, -1))
    assert list(trange(5, 10)) == list(range(5, 10))

test_trange()

# Generated at 2022-06-14 13:12:56.796458
# Unit test for function trange
def test_trange():
    """Testing trange"""
    trange(0)


if __name__ == '__main__':  # pragma: no cover
    test_trange()

# Generated at 2022-06-14 13:12:59.930331
# Unit test for function trange
def test_trange():
    """
    Simple unit test for ``tqdm.auto.trange``.
    """
    assert list(trange(3)) == [0, 1, 2]



# Generated at 2022-06-14 13:13:02.501499
# Unit test for function trange
def test_trange():
    assert list(trange(0)) == []
    assert list(trange(1)) == [0]
    assert list(trange(2)) == [0, 1]



# Generated at 2022-06-14 13:13:13.889357
# Unit test for function trange
def test_trange():  # pragma: no cover
    """
    Ensure that `trange` generates the same thing as `tqdm(range(...))`.
    """
    with tqdm(total=10) as t:
        for i in range(10):
            t.update()
            time.sleep(0.1)

    with trange(10) as t:
        for i in t:
            time.sleep(0.1)

    assert t.n == 10
    assert t.total == 10
    assert t.smoothing == 0
    assert t.last_print_n == 10

    with tqdm(total=10) as t:
        for i in range(10):
            t.update(i)
            time.sleep(0.1)


# Generated at 2022-06-14 13:13:15.062603
# Unit test for function trange
def test_trange():
    """Test for function `trange`"""
    from .tests import test_trange
    return test_trange(trange)


# Unit tests for function tqdm

# Generated at 2022-06-14 13:13:29.219096
# Unit test for function trange
def test_trange():
    """Test function trange"""
    import sys
    import time
    import argparse
    from random import random

    parser = argparse.ArgumentParser()
    parser.add_argument('--iters', default=10, type=int, help='Number of iterations')
    arguments = parser.parse_args()

    for i in trange(arguments.iters, desc='1st loop'):
        if i < arguments.iters / 2:
            j = i / 30
        else:
            j = (arguments.iters - i) / 30
        t = random() / 2
        time.sleep(t)

    for i in trange(arguments.iters, desc='2nd loop'):
        for _ in range(arguments.iters):
            for _ in range(50):
                t = random() / 50

# Generated at 2022-06-14 13:13:34.025487
# Unit test for function trange
def test_trange():
    """Test class functionality"""
    from .gui import tgrange

    assert trange(1, 2) == list(range(1, 2))
    assert trange(1, 2, desc="prefix") == list(tgrange(1, 2, desc="prefix"))

# Generated at 2022-06-14 13:13:42.022189
# Unit test for function trange
def test_trange():
    """Test if trange works fine"""
    from .std import format_interval
    assert (
        format_interval(
            trange(
                3,
                desc="(testing tqdm.auto.trange)",
                leave=False,
                mininterval=0.01,
            ).__iter__(),
            0,
        )
        == "[  0%|          | 0/3 [00:00<?, ?it/s]\n(testing tqdm.auto.trange)]"
    )

# Generated at 2022-06-14 13:13:52.076644
# Unit test for function trange
def test_trange():
    """
    Testing tqdm_gui.autogui.trange().
    """
    trange(1)
    trange(1, 2)
    trange(1, 2, 3)
    trange(1, 2, 3, 4)
    trange(1, 2, 3, 4, 5)
    trange(1, 2, 3, 4, 5, 6)
    trange(1, 2, 3, 4, 5, 6, 7)
    trange(1, 2, 3, 4, 5, 6, 7, 8)
    trange(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Generated at 2022-06-14 13:14:00.173747
# Unit test for function trange
def test_trange():
    """
    Unit test for trange
    """
    from .std import tqdm
    list(tqdm(range(1)))
    list(tqdm(range(1)))

try:
    import unittest

    class TqdmAutoTest(unittest.TestCase):
        def test_synonym(self):
            """
            Unit test for synonym
            """
            import tqdm.auto
            self.assertIs(tqdm.auto.tqdm, tqdm.auto.trange)

    if __name__ == "__main__":
        unittest.main(argv=[sys.argv[0]])
except ImportError:
    pass

# Generated at 2022-06-14 13:14:09.226587
# Unit test for function trange
def test_trange():
    """Test for function trange"""
    from .utils import _version

    start, stop, step = 0, 10, 1
    if _version >= (3,):
        # On Python 3, `range` returns an iterable of integers
        range_ = range(start, stop, step)
    else:
        # On Python 2, range returns a list
        range_ = list(range(start, stop, step))
    list(trange(start, stop, step, leave=True))
    list(trange(len(range_), leave=True))
    list(trange(range_, leave=True))


test_trange()

# Generated at 2022-06-14 13:14:15.443623
# Unit test for function trange
def test_trange():
    """Tests trange function defined in tqdm.auto"""
    from .auto import trange
    from .std import trange as _trange

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
        for i in trange(10):
            assert i in range(10), "{} not in range [0, 10)".format(i)

    for i in _trange(10):
        assert i in range(10), "{} not in range [0, 10)".format(i)

# Generated at 2022-06-14 13:14:20.383775
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange
    """
    if sys.version_info[:2] < (3, 6):
        assert trange is notebook_trange
    else:
        assert trange(10) == list(range(10))
        assert trange(2, 3) == list(range(2, 3))
        assert trange(2, 4, 0.5) == list(range(2, 4, 0.5))

# Generated at 2022-06-14 13:14:26.100812
# Unit test for function trange
def test_trange():
    """Test for function trange"""
    from .std import trange
    try:
        from tqdm import tqdm
    except ImportError:
        try:
            from tqdm import tqdm_gui
        except ImportError:
            raise ImportError("tqdm.auto not available - please install tqdm")
        else:
            tqdm = tqdm_gui

    for on_stdout in [False, True]:
        for i in trange(1, 4, desc="Test", ncols=None, ascii=None,
                        unit_scale=True, unit="it", dynamic_ncols=False,
                        file=None if on_stdout else sys.stdout):
            pass

# Generated at 2022-06-14 13:14:32.956700
# Unit test for function trange
def test_trange():
    from ._utils import _range
    from ._tqdm import _test_short_iter
    for n in _range(10, 500, 100):
        list(trange(n, mininterval=0.001))
        list(trange(n, mininterval=0.001, desc="hi"))
        list(trange(n, mininterval=0.001, leave=True))
    _test_short_iter(lambda: trange(1, 2, 0.0001, mininterval=0.001,
                                    miniters=1, maxinterval=1))