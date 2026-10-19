

# Generated at 2022-06-14 13:12:29.373249
# Unit test for function product
def test_product():
    with tqdm_auto(total=24, ncols=100) as t:
        try:
            for i, j in product(range(4), range(6)):
                t.update()
            else:
                assert t.total == 24
                assert t.n == 24
        except:
            assert False
            raise

# Generated at 2022-06-14 13:12:32.345693
# Unit test for function product
def test_product():
    """test_product"""
    assert sum(list(map(sum, product([0, 1, 2], [0, 1, 2], [0, 1, 2])))) == 27

# Generated at 2022-06-14 13:12:43.928276
# Unit test for function product
def test_product():
    try:
        from nose import tools as nt
    except ImportError:
        return
    nt.assert_equal(
        list(
            product(
                [x for x in range(7)],
                [x for x in range(7)],
                tqdm_class=tqdm_auto,
            )
        ),
        list(itertools.product([x for x in range(7)], [x for x in range(7)])))

# Generated at 2022-06-14 13:12:49.098566
# Unit test for function product
def test_product():
    assert list(product(range(5), ["a", "b", "c"])) == \
        [(0, 'a'), (0, 'b'), (0, 'c'),
         (1, 'a'), (1, 'b'), (1, 'c'),
         (2, 'a'), (2, 'b'), (2, 'c'),
         (3, 'a'), (3, 'b'), (3, 'c'),
         (4, 'a'), (4, 'b'), (4, 'c')]

# Generated at 2022-06-14 13:12:54.792852
# Unit test for function product
def test_product():
    # Test 1
    import numpy as np
    with tqdm_auto(total=28, leave=False) as t:
        for i in product(range(3), range(3), range(3)):
            assert i in itertools.product(range(3), range(3), range(3))
            t.update()

if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:13:06.938029
# Unit test for function product
def test_product():
    """Test for function product"""
    import os
    import sys
    from .tqdm import trange, tqdm

    unit_test = (__name__ == "__main__")
    # Run function tests
    iterable = [('a', 'b'), range(3), (1j, 2j, 3j)]

# Generated at 2022-06-14 13:13:17.022321
# Unit test for function product
def test_product():
    import sys
    import six
    import numpy as np
    from nose.tools import raises

    # Test basic
    l = list(range(10))
    prod = list(product(l, repeat=0))
    assert prod == [()]
    prod = list(product(l, repeat=1))
    assert prod == [(i,) for i in l]
    prod = list(product(l, repeat=3))
    assert prod == [(i, j, k) for i in l for j in l for k in l]
    prod = list(product(l, repeat=-1))
    assert prod == []

    # Test product within tqdm context
    prod = list(product(l, repeat=0, ascii=True, file=sys.stdout))
    assert prod == [()]

# Generated at 2022-06-14 13:13:29.431001
# Unit test for function product
def test_product():
    try:
        from collections import Iterator
    except ImportError:
        from collections.abc import Iterator
    assert issubclass(product([]), Iterator)

    for tt in map(tuple, product(
            [1, 2, 3],
            [4, 5],
            (6.0, 7),
            range(8, 9),
            "ab")):
        assert tt == (1, 4, 6.0, 8, 'a')
        break

    actual_list = list(product(
        [1, 2, 3],
        [4, 5],
        (6.0, 7),
        range(8, 9),
        "ab"))

# Generated at 2022-06-14 13:13:35.431125
# Unit test for function product
def test_product():
    X = [0, 1, 2, 3]
    Y = ['a', 'b', 'c', 'd']
    Z = ['A', 'B', 'C', 'D']
    assert len(list(product(X, Y, Z))) == len(list(
        itertools.product(X, Y, Z))) == len(X) * len(Y) * len(Z)

# Generated at 2022-06-14 13:13:42.808312
# Unit test for function product
def test_product():
    from ..tests import closing, closing_iter, TestCase
    from itertools import cycle
    from random import randint

    class TestProduct(TestCase):

        def test_smoke(self):
            for iterable in ("Hello, world!",
                             (1, 2, 3, 4, 5),
                             [0.] * 10000,
                             range(100)):
                with closing(tqdm_auto(iterable)) as pbar:
                    for i in pbar:
                        pass

        def test_multi(self):
            with closing(tqdm_auto(["a", "b", "c"], total=15)) as pbar:
                for i, j in zip(pbar, range(5)):
                    pass

# Generated at 2022-06-14 13:13:54.948932
# Unit test for function product
def test_product():
    from .utils import FormatMixin
    try:
        from pandas import DataFrame
        from pandas import Series
        from numpy import float32
    except (ImportError, RuntimeError):
        return

    for t in [int, float32, float, FormatMixin, DataFrame, Series]:
        _t = t()
        try:
            _t.__length_hint__
        except AttributeError:
            pass
        else:
            def length_hint(x):
                return x.__length_hint__()
            product(t(), t(), t(), t(), t(), t(), t())

    assert list(product([1, 2], [3, 4])) == [
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4)
    ]

# Generated at 2022-06-14 13:14:04.017558
# Unit test for function product
def test_product():
    with tqdm_auto.tqdm(unit='foo') as t:
        it = product(t, enumerate('abcd'))
        tt = list(it)
    assert tt == [(0, 'a'), (0, 'b'), (0, 'c'), (0, 'd')]

    with tqdm_auto.tqdm(unit='foo') as t:
        it = product(t, [1, 2], "abcd")
        tt = list(it)
    assert tt == [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'),
                  (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd')]


# Generated at 2022-06-14 13:14:06.085519
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    # TODO

# Generated at 2022-06-14 13:14:15.971946
# Unit test for function product
def test_product():
    try:
        import numpy as np
    except ImportError:
        pass
    else:
        for tqdm_class in (tqdm_auto, tqdm_auto.tqdm):
            assert np.array_equal(
                np.array(tuple(product(np.arange(10),
                                       tqdm_class=tqdm_class))),
                np.array(
                    ((i, j)
                     for i in range(10)
                     for j in range(10))
                )
            )

# Generated at 2022-06-14 13:14:18.880509
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from .utils import FormatWrapIter
    from .utils import TerminalSize
    from . import tqdm
    from numpy.random import random


# Generated at 2022-06-14 13:14:24.941705
# Unit test for function product
def test_product():
    from numpy.testing import assert_equal
    p = product([1, 2, 3], ['a', 'b', 'c'], tqdm_class=None)
    assert_equal(list(p), list(itertools.product([1, 2, 3], ['a', 'b', 'c'])))

    p = product([1, 2, 3], ['a', 'b', 'c'])
    assert_equal(list(p), list(itertools.product([1, 2, 3], ['a', 'b', 'c'])))

# Generated at 2022-06-14 13:14:27.936858
# Unit test for function product
def test_product():
    it = product(range(3), range(3), tqdm_class=tqdm_auto)
    assert list(it) == list(itertools.product(range(3), range(3)))

# Generated at 2022-06-14 13:14:35.897342
# Unit test for function product
def test_product():
    try:
        list(product([1, 2], "ab"))
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")

    # Check if returned iterator is equivalent to the itertools version
    assert list(product([1, 2], [1, 2, 3], tqdm_class=None)) == list(itertools.product([1, 2], [1, 2, 3]))

    # Check if iterator yields the same items as the list version
    assert list(product([1, 2], [1, 2, 3], tqdm_class=tqdm_auto)) == \
        list(product([1, 2], [1, 2, 3], tqdm_class=None))

# Generated at 2022-06-14 13:14:45.871150
# Unit test for function product
def test_product():
    from .tests import _test_it
    from .tests import TEST_ITERABLES

# Generated at 2022-06-14 13:14:50.859988
# Unit test for function product
def test_product():
    """Unit test for function `tqdm.itertools.product`"""
    from . import trange
    for i in product(range(10000), trange(5)):
        pass
    for i in product(trange(5), range(10000)):
        pass
    for i in product(trange(5), trange(10)):
        pass
    for i in product(range(100), trange(100), range(100)):
        pass

# Generated at 2022-06-14 13:14:57.975306
# Unit test for function product
def test_product():
    """
    Test for function product
    """
    for _ in product(range(100), range(100), range(100),
                     tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:15:05.995460
# Unit test for function product
def test_product():
    """
    Unit test
    """
    from ..utils import FormatBytes
    import io, sys
    out = io.BytesIO()
    save_stdout = sys.stdout
    try:
        sys.stdout = out
        prod = product(range(100), range(100), tqdm_class=FormatBytes)
        for _ in prod:
            pass
        replaced_lines = out.getvalue().replace(b'\r', b'').replace(b'\n', b'')
        assert replaced_lines == b'|#                                                                 100%||  100/100 [00:00<00:00, 999979.38it/s]|'
    finally:
        sys.stdout = save_stdout

# Generated at 2022-06-14 13:15:10.193365
# Unit test for function product
def test_product():
    """Test the product function"""
    res = list(product(range(10), range(5), tqdm_class=tqdm_auto))
    assert res == [i for i in itertools.product(range(10), range(5))]

# Generated at 2022-06-14 13:15:18.973477
# Unit test for function product
def test_product():
    from .utils import BinaryCounter

    p = [(x, y) for x in range(3) for y in range(3)]
    for i, (x, y) in enumerate(product(range(3), range(3))):
        assert (x, y) == p[i]
        assert i in (x * 3 + y,)
    assert list(product(range(3))) == [(0,), (1,), (2,)]

    p = [x / 10.0 for x in range(6)]
    for i, x in enumerate(product(range(6))):
        assert x == (i,)
    assert list(product(range(6))) == [(x,) for x in range(6)]

    p = [x / 10.0 for x in range(6)]

# Generated at 2022-06-14 13:15:25.026965
# Unit test for function product
def test_product():
    """Test for product function"""
    from .utils import FormatCustom
    r = list(product(range(4), range(4)))
    assert r == [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1),
                 (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3),
                 (3, 0), (3, 1), (3, 2), (3, 3)]
    r = list(product(range(4), range(4), tqdm_class=FormatCustom))

# Generated at 2022-06-14 13:15:28.760184
# Unit test for function product
def test_product():
    """Test nested `tqdm` usage via `grouper` and `chain.from_iterable`"""
    list(product(range(3), range(3)))


if __name__ == '__main__':
    import pytest
    pytest.main(args=["--pyargs", __name__])

# Generated at 2022-06-14 13:15:31.918975
# Unit test for function product
def test_product():
    for i in product([1, 2, 3, 4], range(10)):
        pass
    assert i == (4, 9)

# Generated at 2022-06-14 13:15:36.760211
# Unit test for function product
def test_product():
    """
    Test function product
    """
    from ..utils import FormatCustomText as FT
    kwargs = dict(desc='test_product', total=10**5, unit='test')

    with tqdm_auto(**kwargs) as t:
        for i in product(range(1000), range(1000), tqdm_class=t.__class__):
            continue

    with tqdm_auto(**kwargs) as t:
        for i in product(range(1000), range(1000),
                         tqdm_class=t.__class__, ascii=True):
            continue

    with tqdm_auto(**kwargs) as t:
        for i in product(range(1000), range(1000), bar_format=None):
            continue

    ft = tqdm_auto()._format_meter

# Generated at 2022-06-14 13:15:46.020559
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    import sys
    from .utils import FormatWrapIter

    for n, i in enumerate(product(range(1), range(2), range(3), tqdm_class=None)):
        sys.stdout.write(str(n))
        assert n == sum(i), str(i)

    for n, i in enumerate(product(['a', 'b'], ['a', 'b'], tqdm_class=FormatWrapIter)):
        sys.stdout.write(str(n))
        assert n == sum(map(ord, i)), str(i)

    for n, i in enumerate(product(range(3), tqdm_class=FormatWrapIter)):
        sys.stdout.write(str(n))
        assert n

# Generated at 2022-06-14 13:15:49.986608
# Unit test for function product
def test_product():
    from .tests import pretest_posttest_in_tmpdir
    from .tests import test_product as _test_product
    import numpy as np
    pretest_posttest_in_tmpdir(_test_product, np.random.rand)

# Generated at 2022-06-14 13:16:10.069387
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from .common import closing, setup, teardown

    setup()

# Generated at 2022-06-14 13:16:15.082515
# Unit test for function product
def test_product():
    """
    Unit test for tqdm.itertools.product

    """
    # Regression test for issue #275
    def f():
        for i in product(range(100), range(100), range(100),
                         tqdm_class=tqdm_auto, leave=False, ncols=80):
            pass
    assert f() is None

# Generated at 2022-06-14 13:16:21.780169
# Unit test for function product
def test_product():
    res = [i for i in product(range(3), 'abc', tqdm_class=tqdm_auto)]
    assert len(res) == 9
    assert res[0] == (0, 'a')

    res = [i for i in product(range(3), "abcd", tqdm_class=tqdm_auto)]
    assert len(res) == 12
    assert res[0] == (0, 'a')

# Generated at 2022-06-14 13:16:31.525268
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    import sys
    import shutil
    import atexit
    from .tqdm import tqdm

    old_stderr = sys.stderr
    sys.stderr = open("test_product.txt", "w")
    tnrange = lambda *a, **k: tqdm(xrange(*a), **k)

# Generated at 2022-06-14 13:16:37.756529
# Unit test for function product
def test_product():
    """
    Unit test for function `tqdm.itertools.product`.
    """
    from .tests import _test_equality
    from .tests import _test_exception_type
    from tqdm import tnrange

    # Check equality of `product` with `itertools.product`
    for A, B in zip(
            product(range(10), range(10), range(10),
                    tqdm_class=tnrange),
            itertools.product(range(10), range(10), range(10))):
        assert A == B

    # Check exception types
    _test_exception_type(lambda: product(1), TypeError)

    # Check that `total` is at least equal to `len(iterable)`

# Generated at 2022-06-14 13:16:47.845114
# Unit test for function product
def test_product():
    """
    Unit test for `product`.
    """
    from numpy.testing import assert_equal
    from ..utils import TestBuffer as Buffer

    out = []
    for i in product(range(10), range(10), tqdm_class=Buffer):
        out.append(i)

# Generated at 2022-06-14 13:16:51.468701
# Unit test for function product
def test_product():
    """Unit test for function product"""
    test_list = range(10)
    with tqdm_auto(total=10 ** 2) as t:
        for i, j in product(test_list, test_list):
            assert i == j
            t.update()

# Generated at 2022-06-14 13:16:59.235233
# Unit test for function product
def test_product():
    """
    Unit test for product.
    """
    import pandas as pd

    assert list(product(range(1))) == list(itertools.product(range(1)))
    assert list(product(range(2))) == list(itertools.product(range(2)))
    assert list(product(range(2), range(3))) == list(
        itertools.product(range(2), range(3))
    )
    assert list(product(range(2), range(3), range(4))) == list(
        itertools.product(range(2), range(3), range(4))
    )

# Generated at 2022-06-14 13:17:06.331824
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    a = ["a", "b", "c"]
    b = [1, 2, 3]
    c = list(product(a, b, tqdm_class=tqdm_auto, mininterval=0.1, miniters=1))
    d = [(i, j) for i in a for j in b]
    assert sorted(c) == sorted(d)

# Generated at 2022-06-14 13:17:14.939260
# Unit test for function product
def test_product():
    """ Unit test for function :func:`product` """
    import pytest
    try:
        import numpy as np
    except ImportError:
        pytest.skip("numpy not available")
    from ..utils import FreezableClass
    from ..tqdm import trange
    from .itertools import product as product_

    z = FreezableClass(lambda: list(range(5))).freeze()
    z1 = FreezableClass(lambda: list(range(5))).freeze()
    z2 = FreezableClass(lambda: list(range(5))).freeze()

    z.append(None)  # noqa

    kwargs = dict(miniters=1, ascii=True)

# Generated at 2022-06-14 13:17:34.944119
# Unit test for function product
def test_product():
    from .tests import test_product as _test_product
    _test_product(product)

# Generated at 2022-06-14 13:17:43.177856
# Unit test for function product
def test_product():
    from .tests import util
    from .tests.py26_tests import product_py2
    from .tests.py27_tests import product_py3

    # Equivalent of `itertools.product`
    # (not using itertools.product for testing)
    def itertools_product(*args, **kwargs):
        for i in itertools.product(*iterables, **kwargs):
            yield i

    # Test all versions of Python, with and without optional arguments

# Generated at 2022-06-14 13:17:51.176856
# Unit test for function product
def test_product():
    it = product([0, 1], [None, 0, 1], tqdm_class=tqdm_auto)
    result = list(it)
    assert result == [(0, None), (1, None), (0, 0), (1, 0), (0, 1), (1, 1)]
    assert len(result) == 6

    it = product([0, 1], [None, 0, 1])
    result = list(it)
    assert result == [(0, None), (1, None), (0, 0), (1, 0), (0, 1), (1, 1)]
    assert len(result) == 6

# Generated at 2022-06-14 13:17:53.283221
# Unit test for function product
def test_product():
    """Unit test for function product"""
    # dummy test
    list(itertools.islice(product('ab', '12', 'xy'), 5))

# Generated at 2022-06-14 13:18:01.154342
# Unit test for function product
def test_product():
    assert list(product(range(3))) == [(0,), (1,), (2,)]
    assert list(product(range(2), range(5))) == [(0, 0), (0, 1), (0, 2),
                                                 (0, 3), (0, 4), (1, 0),
                                                 (1, 1), (1, 2), (1, 3),
                                                 (1, 4)]

# Generated at 2022-06-14 13:18:10.260315
# Unit test for function product
def test_product():
    """Test `itertools.product`."""
    # Define all functions
    def pos(*iterables):
        """Product function."""
        return set(itertools.product(*iterables))

    def neg(*iterables):
        """Product function."""
        return set(itertools.product(*(map(lambda x: x, iterables))))

    def tup(*iterables):
        """Product function."""
        return set(itertools.product(*(tuple(map(lambda x: x, iterables)))))

    def list_up(*iterables):
        """Product function."""
        return set(itertools.product(*(list(map(lambda x: x, iterables)))))

    def iset(*iterables):
        """Product function."""

# Generated at 2022-06-14 13:18:20.629110
# Unit test for function product
def test_product():
    """Unit test for `tqdm.itertools.product`"""
    from .guessing import format_sizeof, sizeof_fmt
    import numpy as np

    # Test product
    assert list(product(range(3), repeat=3)) == list(itertools.product(
        range(3), repeat=3))
    assert list(product(range(3), repeat=1)) == list(itertools.product(
        range(3), repeat=1))
    assert list(product(range(3), repeat=0)) == list(itertools.product(
        range(3), repeat=0))
    assert list(product(range(3), repeat=-1)) == list(itertools.product(
        range(3), repeat=-1))

# Generated at 2022-06-14 13:18:29.120722
# Unit test for function product
def test_product():  # NOQA
    from ..std import time
    start_time = time.perf_counter()
    list(product('ABCD', 'xy', tqdm_class=tqdm_auto, desc="outer"))
    list(product('ABCD', 'xy', tqdm_class=tqdm_auto, desc="outer", total=9))
    end_time = time.perf_counter()
    assert (end_time - start_time) < 0.5, \
        "Took {:.1f}s, expected < 0.5s".format(end_time - start_time)

# Generated at 2022-06-14 13:18:37.353349
# Unit test for function product
def test_product():
    """Unit test for `tqdm.tqdm.product`"""
    import sys
    if sys.version_info < (2, 7):
        return
    import tqdm
    import numpy as np

    # Pure-python
    assert list(tqdm.tqdm.product(
        ['a', 'b', 'c'], repeat=2)) == [('a', 'a'), ('a', 'b'),
                                        ('a', 'c'), ('b', 'a'),
                                        ('b', 'b'), ('b', 'c'),
                                        ('c', 'a'), ('c', 'b'),
                                        ('c', 'c')]
    # Numpy

# Generated at 2022-06-14 13:18:47.350685
# Unit test for function product
def test_product():
    """Test for `itertools.product`"""
    from .tqdm import trange

    for X, Y in product(range(3), trange(4)):
        pass
    for X, Y in trange(2, 3, desc="product(range(2), range(3))"):
        for _ in range(X + Y):
            pass
    for x, y in product([1, 3, 2], range(2)):
        pass
    c = 0
    for x, y in trange(5):
        c += x + y
    assert c == 30

    for x, y in trange(3, desc="product(range(3), repeat=2)"):
        for _ in range(x + y):
            pass

# Generated at 2022-06-14 13:19:32.424446
# Unit test for function product
def test_product():
    """Test for function product"""
    # Test for kwargs
    for kw in ('total', 'smoothing', 'leave', 'ascii', 'unit', 'unit_scale',
               'unit_divisor', 'miniters', 'mininterval', 'maxinterval',
               'file', 'dynamic_ncols', 'smoothing', 'bar_format',
               'initial', 'position', 'postfix', 'desc', 'ncols'):
        product(*((1, 2, 3),) * 10, **{kw: kw})
        product(*((1, 2, 3),) * 10, **{kw: -10 if kw == 'total' else 0})
    # Test for outputs

# Generated at 2022-06-14 13:19:40.543210
# Unit test for function product

# Generated at 2022-06-14 13:19:46.427974
# Unit test for function product
def test_product():
    import numpy as np

    # Basic usage
    expected = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3)]
    expected = list(map(tuple, expected))
    assert list(product(range(3), range(4))) == expected
    assert list(product(range(3), range(4), tqdm_class=None)) == expected

    # Numpy array
    expected = [(0, 0), (0, 1), (1, 0), (1, 1)]
    expected = list(map(tuple, expected))
    assert list(product(np.array([0, 1]), np.array([0, 1])))

# Generated at 2022-06-14 13:19:50.525049
# Unit test for function product
def test_product():
    from .tqdm_gui import tqdm
    from .utils import format_sizeof
    assert format_sizeof(next(product(
        range(1000000),
        range(1000000),
        tqdm_class=tqdm,
        leave=True
    ))) == "8.00 MB"

# Generated at 2022-06-14 13:19:57.735170
# Unit test for function product
def test_product():
    from .utils import format_sizeof
    from .utils import is_iterable
    from .utils import console_width
    from .utils import _term_move_up
    from .utils import _format_time

    from .utils import FormatWarn

    from .utils import format_interval
    from .utils import format_meter
    from .utils import format_size
    from .utils import format_line
    from .utils import format_sizeof
    from .utils import format_timesofar
    from .utils import format_naturalsize
    from .utils import format_number

    import time
    import numpy as np

    #########################################################################
    # Evaluation
    #########################################################################

    # Tests
    assert not is_iterable([1, 2])
    assert not is_iterable(1)
    assert is_iter

# Generated at 2022-06-14 13:20:07.117136
# Unit test for function product
def test_product():
    """
    Ensure that product works without crashing.
    """
    import numpy as np
    from numpy.testing import assert_array_equal
    from .utils import BaseTestCase, silence
    with silence():
        for _ in product(*[np.arange(1), 'ABC'],
                         **dict(tqdm_class=BaseTestCase.mock_tqdm(['1', '2', '3']))):
            pass
        for _ in product(*[np.arange(1), 'ABC'],
                         **dict(tqdm_class=BaseTestCase.mock_tqdm(['1', '2', '3']),
                                total=3)):
            pass

# Generated at 2022-06-14 13:20:12.150839
# Unit test for function product
def test_product():
    """ Test for tqdm.product """
    from ..utils import FormatMixin
    with tqdm_auto(total=10, ascii=True) as t:
        assert FormatMixin.unicode(t) == "[0/10]"
        for i in product(range(40), range(50),
                         tqdm_class=tqdm_auto):
            pass
        assert FormatMixin.unicode(t) == "[10/10]"

# Generated at 2022-06-14 13:20:18.577885
# Unit test for function product
def test_product():
    """
    Unit test for product().
    """
    from ..utils import format_sizeof
    import random
    try:
        import numpy
    except ImportError:
        pass
    else:
        numpy.random.seed(0)
        for i in product(numpy.random.random((100,100)), repeat=10,
                         tqdm_class=tqdm_auto):
            pass
    for _ in product(range(100), range(100), tqdm_class=tqdm_auto):
        pass
    iter_value = ([1, 2, 3], [4, 5, 6])
    count = 0

# Generated at 2022-06-14 13:20:28.089198
# Unit test for function product
def test_product():
    """
    Testing with 1dim, 2dim and 3dim iterables.
    """
    for iterable in (
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            ['1', '2', '3'],
    ):
        total = 1
        for i in range(len(iterable)):
            total *= len(iterable[i])
        iterable2 = []
        for i in iterable:
            iterable2.append(i)
        with tqdm_auto(total=total) as t:
            tmp = 0
            for i in product(*iterable2):
                tmp += 1
               

# Generated at 2022-06-14 13:20:34.993506
# Unit test for function product
def test_product():
    """
    Test for products
    """
    from ..utils import freeze_support
    freeze_support()
    for i in product('ABC', 'xy', tqdm_class=tqdm_auto):
        pass
    for i in product('ABC', 'xy'):
        pass
    for i in product('ABC', 'xy', tqdm_class=tqdm_auto, total=1000):
        pass
    for i in product('ABC', 'xy'):
        pass

# Generated at 2022-06-14 13:21:59.286377
# Unit test for function product
def test_product():
    """Test `itertools.product` wrapper"""
    import numpy as np
    from ..utils import FormatCustomText
    from ..utils import nullcontext

    tqdm_ = tqdm_auto(ascii=True)
    tqdm_.write = lambda s, **kw: None
    tqdm_.pandas = None


# Generated at 2022-06-14 13:22:03.338131
# Unit test for function product
def test_product():
    """Unit test for product"""

# Generated at 2022-06-14 13:22:04.893807
# Unit test for function product
def test_product():
    for d in product((0, 1), (2, 3), tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:22:13.606617
# Unit test for function product
def test_product():
    """Test function product"""
    # It's a wrapper, no need to test too much
    a = product(list(range(4)),
                list("abc"),
                tqdm_class=tqdm_auto,
                total=None)
    assert(list(a) == [(0, 'a'), (0, 'b'), (0, 'c'), (1, 'a'), (1, 'b'),
                       (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'),
                       (3, 'b'), (3, 'c')])


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:22:17.589196
# Unit test for function product
def test_product():
    """
    Unit-test the `tqdm.itertools.product` function.
    """
    it = product('ABCD', 'xy', tqdm_class=tqdm_auto)
    assert isinstance(it, tqdm_auto)

# Generated at 2022-06-14 13:22:25.043633
# Unit test for function product
def test_product():
    from numpy import allclose
    from numpy.random import randint, rand
    assert allclose(
        [(i, j) for i in tqdm_auto(range(5)) for j in tqdm_auto(range(5))],
        list(tqdm_auto.product(range(5), range(5))))
    assert allclose(
        [(i, j) for i in range(5) for j in range(5)],
        list(tqdm_auto.product(range(5), range(5), leave=True)))