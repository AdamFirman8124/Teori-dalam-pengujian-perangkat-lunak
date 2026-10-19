

# Generated at 2022-06-14 13:12:29.463897
# Unit test for function trange
def test_trange():
    """Unit test for trange"""
    from .autonotebook import trange
    for _ in trange(4, desc='outer loop', leave=True):
        for i in trange(4, desc='inner loop', leave=True):
            for j in trange(4, desc='jth loop of inner loop', leave=True):
                assert i == j


# Generated at 2022-06-14 13:12:41.142543
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange.
    """
    from tqdm.contrib.test_utils import DiscreteTestWatcher
    import pytest  # noqa
    watcher = DiscreteTestWatcher()

    # Test trange
    # with (Watcher(total=100)) as watcher:

# Generated at 2022-06-14 13:12:50.951795
# Unit test for function trange
def test_trange():
    """
    Unit test for trange()

    >>> test_trange()
    """
    from .auto import trange
    from .utils import _version
    from .std import tqdm
    from . import _tqdm_gui, _tqdm_notebook

    for module in (_tqdm_gui, _tqdm_notebook):
        if module is not None:
            print("Testing trange with", module.__name__)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=UserWarning)
                assert trange(3, module=module) == list(tqdm(
                    range(3), module=module))

    try:
        import asyncio
    except ImportError:
        pass

# Generated at 2022-06-14 13:13:02.833946
# Unit test for function trange
def test_trange():
    list(trange(10))
    list(trange(10, desc="custom desc"))
    list(trange(10, position=42))
    list(trange(10, position=42, desc="custom desc"))
    list(trange(10, position=42, desc="custom desc", ascii=True))
    list(trange(10, position=42, desc="custom desc", ascii=True, leave=True))
    list(trange(10, position=42, desc="custom desc", ascii=True, leave=True,
                mininterval=0.5))
    list(trange(10, position=42, desc="custom desc", ascii=True, leave=True,
                mininterval=0.5, smoothing=0.1))

# Generated at 2022-06-14 13:13:05.657815
# Unit test for function trange
def test_trange():
    """Test unit for function trange"""
    trange_list = list(trange(2))
    assert trange_list == [0, 1]

# Generated at 2022-06-14 13:13:16.128968
# Unit test for function trange
def test_trange():
    """Test function trange()"""
    from .std import trange
    from .std import format_sizeof

    from .utils import _range
    from .utils import format_interval
    from .utils import time_interval

    n = 3
    tup = trange(n, bar_format="{r_bar}{bar}|", leave=True)
    assert next(tup) == 0
    assert next(tup) == 1
    assert next(tup) == 2
    with tup:
        pass
    try:
        next(tup)
    except StopIteration:
        pass
    else:
        assert False

    # Test 100%

# Generated at 2022-06-14 13:13:28.002465
# Unit test for function trange
def test_trange():
    """Test function: trange()"""
    # pylint: disable=star-args,protected-access
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("quiet", TqdmExperimentalWarning)
        from .std import tqdm as _tqdm

    list(trange(3))
    list(trange(2, 3))
    list(trange(4, 2, -1))
    list(trange(5, 2, -1, leave=True))
    list(trange(5, 2, -1, leave=True, unit_scale=True))
    list(trange(5, 2, -1, unit_scale=True))
    list(trange(5, 2, -1, unit='s'))

# Generated at 2022-06-14 13:13:32.666872
# Unit test for function trange
def test_trange():
    """
    Tests `trange` function.
    """
    from .std import tqdm
    for i in trange(10):
        pass
    assert tqdm.write.call_args[0][0] == ": |#    | [elapsed: 00:00:00]\r"

# Generated at 2022-06-14 13:13:41.645892
# Unit test for function trange
def test_trange():
    """Test function trange()."""
    # Smooth
    list(trange(3))
    list(trange(0))
    list(trange(1))
    list(tqdm([]))

    kwargs = {"total": 3}
    list(trange(0, **kwargs))
    list(trange(1, **kwargs))
    list(trange(2, **kwargs))
    list(trange(3, **kwargs))

    kwargs = {"total": 0}
    list(trange(0, **kwargs))

    # Uneven
    list(trange(3, 0))
    list(trange(3, 1))
    list(trange(3, 2))
    list(trange(3, 3))

    kwargs = {"total": 3}


# Generated at 2022-06-14 13:13:48.843255
# Unit test for function trange
def test_trange():
    """
    Tests function `trange()` and `tqdm()`.
    """
    assert list(trange(5)) == list(range(5))
    assert list(tqdm(range(5))) == list(range(5))
    assert list(tqdm(list(range(5)))) == list(range(5))
    assert list(trange(0)) == list(range(0))
    assert list(tqdm(range(0))) == list(range(0))
    assert list(tqdm(list(range(0)))) == list(range(0))
    assert list(tqdm(range(10), desc="desc")) == list(range(10))
    assert list(tqdm(range(10), desc="desc", leave=True)) == list(range(10))