

# Generated at 2022-06-14 13:12:26.963042
# Unit test for function trange
def test_trange():
    """Test trange function"""
    _ = trange(3, desc='Test', leave=True)


if __name__ == '__main__':
    test_trange()

# Generated at 2022-06-14 13:12:38.487331
# Unit test for function trange
def test_trange():
    """
    Unit test for function trange.
    """
    import os
    import tempfile
    import time
    import subprocess

    sleep_time = 0.03
    n = 5

    saved_env = os.environ.get("TEST_TRANGE", None)

# Generated at 2022-06-14 13:12:44.633101
# Unit test for function trange
def test_trange():
    """Test function"""
    # pylint: disable=no-member
    assert sum(trange(100)) == sum(range(100))
    assert sum(notebook_trange(100)) == sum(range(100))
    assert sum(tqdm(range(100))) == sum(range(100))


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:12:47.947084
# Unit test for function trange
def test_trange():
    """
    Tests that `tqdm.auto.trange` is functionally equivalent to
    `tqdm.auto.tqdm(range(...))`.
    """
    reference = notebook_tqdm(range(0, 10))
    duplicate = trange(0, 10)
    assert reference == duplicate

# Generated at 2022-06-14 13:12:49.487537
# Unit test for function trange
def test_trange():
    """
    Smoke test trange
    """
    total = 10
    try:
        for i in trange(total):
            pass
        assert i + 1 == total
    except Exception:
        print('trange not defined'
              ' or not functioning as expected')
        raise

test_trange()

# Generated at 2022-06-14 13:13:01.368313
# Unit test for function trange
def test_trange():
    from .asyncio import trange  # pylint: disable=unused-import
    from .std import trange  # pylint: disable=unused-import
    from .autonotebook import trange  # pylint: disable=unused-import
    from .gui import trange  # pylint: disable=unused-import

    tranges = (trange,  # pylint: disable=unused-variable
               lambda *a, **kw: trange(*a, **kw),
               lambda *a, **kw: trange(*a, **kw))

    for trange in tranges:
        list(trange(1))
        list(trange(0))
        list(trange(-1))


if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:13:05.703022
# Unit test for function trange
def test_trange():
    """ Test trange """
    import sys
    import sysconfig
    if sys.version_info >= (3, 6):
        from .asyncio import _trange
    for k in _trange(10):
        assert k == list(_trange(10))[k]

# Generated at 2022-06-14 13:13:16.181949
# Unit test for function trange
def test_trange():
    """
    >>> from tqdm.auto import trange
    >>> for _ in trange(3):
    ...     pass
    """
    for _ in trange(3):
        pass
    for _ in trange(3, desc="Desc"):
        pass
    for _ in trange(3, leave=True):
        pass
    for _ in trange(3, total=3):
        pass
    for _ in trange(3, miniters=2):
        pass
    for _ in trange(3, mininterval=0.01):
        pass
    for _ in trange(3, mininterval=0.01, miniters=2, maxinterval=0.1):
        pass

# Generated at 2022-06-14 13:13:18.847064
# Unit test for function trange
def test_trange():
    with tqdm(total=5) as pbar:
        for _ in trange(5):
            pbar.update(1)

# Generated at 2022-06-14 13:13:20.939607
# Unit test for function trange
def test_trange():
    """Makes sure trange works."""
    assert list(trange(4)) == [0, 1, 2, 3]