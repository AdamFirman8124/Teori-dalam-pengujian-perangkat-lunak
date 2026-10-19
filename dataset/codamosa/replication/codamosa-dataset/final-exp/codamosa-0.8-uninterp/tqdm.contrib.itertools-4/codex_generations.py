

# Generated at 2022-06-14 13:12:35.137160
# Unit test for function product
def test_product():
    """
    Python version of:
    ```python
    import itertools

    for i in tqdm.tqdm(itertools.product([1, 2, 3], [4, 5, 6]),
                                                        total=9):
        pass
    ```
    """
    for i in product([1, 2, 3], [4, 5, 6]):
        pass

# Generated at 2022-06-14 13:12:46.229699
# Unit test for function product
def test_product():
    from .common import closing
    import types

    for kwargs in [{}, {'smoothing': 0}]:
        with closing(tqdm_auto(**kwargs)) as t:
            for i in map(types.MethodType, t, ['set_description', 'disable']):
                i('spam')

        with closing(tqdm_auto(**kwargs)) as t:
            assert t.disable is False
            t.disable = True
            assert t.disable is True
            assert t.smoothing == kwargs.get('smoothing', 0.3)
            t.disable = False
            assert t.disable is False
            t.set_description('spam')
            t.close()
            t.update(10)

        # vals = product(range(1000), repeat=1, **kw

# Generated at 2022-06-14 13:12:49.411276
# Unit test for function product
def test_product():
    import nose.tools as nt
    data = list(product(range(3), [3, 2, 1], ['a', 'b', 'c']))
    nt.assert_equal(len(data), 27)

# Generated at 2022-06-14 13:13:01.277989
# Unit test for function product
def test_product():
    """
    Unit tests for function product
    """
    import numpy.testing as npt
    from tqdm import trange

    def product0(*args):
        return itertools.product(*args)

    def product1(*args):
        with trange(min([len(arg) for arg in args])) as t:
            for i in product(*args, tqdm_class=t):
                yield i

    def product2(*args):
        for i in product(*args, tqdm_class=trange):
            yield i

    def product3(args, total):
        for i in product(*args, tqdm_class=trange, total=total):
            yield i

    args = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    npt.assert_all

# Generated at 2022-06-14 13:13:12.700719
# Unit test for function product
def test_product():
    from .tests import closing, closing_to_result, IS_PYPY
    # simple
    with closing(tqdm_auto(total=5)) as t:
        for x in (tqdm_auto.itertools_ext.product(range(5), repeat=2)):
            t.update()
    # no sizelimit
    with closing_to_result() as out:
        with tqdm_auto(
                total=None, miniters=0, file=out, dynamic_ncols=True) as t:
            for x in (tqdm_auto.itertools_ext.product(range(5), repeat=2)):
                t.update()
    assert ("|0/0" in out.getvalue() or "itn 0" in out.getvalue())
    # with inst

# Generated at 2022-06-14 13:13:15.686713
# Unit test for function product
def test_product():
    import sys
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO
    list1 = range(30)
    list2 = range(10)
    out_str = StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = out_str
        for _ in product(list1, list2):
            pass
    finally:
        sys.stdout = old_stdout
    assert out_str.getvalue().strip().split()[-1] == "100%"

# Generated at 2022-06-14 13:13:23.241697
# Unit test for function product
def test_product():
    """Test the function product"""
    import numpy as np
    test_arr = np.arange(5)
    test_out = product(test_arr, test_arr)
    test_list = [i for i in test_out if i]
    expected = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2],
                [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0],
                [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3],
                [4, 4]]
    assert test

# Generated at 2022-06-14 13:13:29.553115
# Unit test for function product
def test_product():
    import numpy as np
    from ..auto import tqdm
    a = [1, 2, 3]
    b = ['a', 'b']
    actual = list(product(a, b, tqdm=tqdm))
    assert all(tuple(i) in actual for i in itertools.product(a, b)), \
        "`product` function doesn't return correct results"

if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:13:37.403780
# Unit test for function product
def test_product():
    try:
        itertools.product = tqdm_auto(range(10), tqdm_class=tqdm_auto)
    except NameError:
        pass
    for _ in tqdm_auto(tqdm_auto(range(10)), ascii=True, unit="B",
                       unit_scale=True, unit_divisor=1024,
                       leave=False, mininterval=2,
                       miniters=2, maxiters=20, file=open(os.devnull, "w")):
        pass

# Generated at 2022-06-14 13:13:43.235208
# Unit test for function product
def test_product():
    def f(i):
        return i**i

    total = 2**2 * 3**3
    with tqdm_auto(total=total) as t:
        for i in product([2, 3], [2, 3, 3], tqdm_class=tqdm_auto):
            assert f(i[0]) * f(i[1]) == t.n
            t.update()
        assert t.n == total

# Generated at 2022-06-14 13:13:54.181753
# Unit test for function product
def test_product():
    # Here we test the default ``None`` iteration (test speed)
    from ..utils import FormatWrapBase
    from ..main import tqdm

    for tqdm_cls in (tqdm, tqdm.tqdm):
        for n in range(2, 6):
            with tqdm_cls(
                total=None,
                miniters=1,
                mininterval=0.25,
                smoothing=1e-9,
                file=FormatWrapBase(None)
            ) as t:
                for _ in product(*[range(n)] * n, tqdm_class=tqdm_cls):
                    t.update()

# Generated at 2022-06-14 13:14:03.426036
# Unit test for function product
def test_product():
    """Tests for `itertools.product` wrapper."""
    import io
    from .utils import format_sizeof
    from .utils import is_within_tolerance
    from .utils import process_obj
    from .utils import ProcessableMixin
    from .utils import UnicodeMixin
    from .utils import WriteFileMixin

    class UnicodeMixinTqdm(ProcessableMixin, UnicodeMixin, WriteFileMixin):

        def __init__(self, **kwargs):
            self.update_interval = kwargs.pop("update_interval", 0.1)
            ProcessableMixin.__init__(self, **kwargs)
            UnicodeMixin.__init__(self, **kwargs)
            WriteFileMixin.__init__(self, **kwargs)


# Generated at 2022-06-14 13:14:13.949730
# Unit test for function product
def test_product():
    import numpy as np
    from ..utils import format_sizeof

    print('Testing function `product`')
    print('Simple test:')
    for c, r in product(range(2), range(2)):
        print(c, r)

    # Nested test
    print("Nested test:")
    for c, r in product(range(3), range(3), range(3), range(3), range(3)):
        print(c, r)

    # Speed test
    from ..utils import format_interval
    from time import time
    data = [(2 ** i, 2 ** j) for i in range(4, 8) for j in range(4, 8)]

    print("Speed test ({} different sizes):".format(len(data)))
    for i, j in data:
        start = time()


# Generated at 2022-06-14 13:14:22.770796
# Unit test for function product
def test_product():
    from sys import stdout
    assert [i for i in product('AB', '12', 'ab', tqdm_class=tqdm_auto)] == [
        ('A', '1', 'a'), ('A', '1', 'b'), ('A', '2', 'a'), ('A', '2', 'b'),
        ('B', '1', 'a'), ('B', '1', 'b'), ('B', '2', 'a'), ('B', '2', 'b')]
    with tqdm_auto(unit='B', unit_scale=True, leave=False, miniters=1,
                   desc='', mininterval=0, file=stdout) as t:
        for i in product('AB', '12', 'ab', tqdm=t):
            pass
    # Test disable output

# Generated at 2022-06-14 13:14:29.303272
# Unit test for function product
def test_product():
    from numpy import all
    from numpy.random import shuffle
    from numpy.testing import assert_allclose
    from .utils import closing, FakeDict, FakeSequence

    for it in [itertools, FakeDict(), FakeSequence()]:
        with closing(itertools.product) as P:
            assert_allclose(
                list(product(range(3), range(2), tqdm_class=P)),
                [[x, y] for x in range(3) for y in range(2)])
    # Shuffle range to catch possible index-related bugs
    r = list(range(10))
    shuffle(r)
    p = product(r)
    assert_allclose(p, range(10))

# Generated at 2022-06-14 13:14:34.362208
# Unit test for function product
def test_product():
    it = product([1, 2, 3], [4, 5, 6])
    assert next(it) == (1, 4)
    assert next(it) == (1, 5)
    assert next(it) == (1, 6)
    assert next(it) == (2, 4)
    assert next(it) == (2, 5)
    assert next(it) == (2, 6)
    assert next(it) == (3, 4)
    assert next(it) == (3, 5)
    assert next(it) == (3, 6)
    try:
        next(it)
    except StopIteration:
        pass
    else:
        assert False, "Should have raised StopIteration"

# Generated at 2022-06-14 13:14:35.392386
# Unit test for function product
def test_product():
    from .utils import _range
    list(product(_range(3), _range(3)))

# Generated at 2022-06-14 13:14:45.147779
# Unit test for function product
def test_product():
    """Unit test for function product"""
    # string => bytes conversion for Python 2
    def u(s):
        if hasattr(s, "decode"):
            return s.decode()
        return s

    from ..utils import removed_keys
    from .pandas import pandas_dicts  # NOQA

    iterables = [[1, 2, 3], [4, 5], [6, 7]]
    assert list(product(*iterables)) == list(itertools.product(*iterables))
    assert list(product(*iterables, tqdm_class=lambda x: x)) == list(itertools.product(*iterables))

    # Compare iterators
    def f(x, y):
        return x * 2 + y

# Generated at 2022-06-14 13:14:48.744670
# Unit test for function product
def test_product():
    assert list(product(range(3), range(3))) == [(0, 0), (0, 1), (0, 2),
                                                (1, 0), (1, 1), (1, 2),
                                                (2, 0), (2, 1), (2, 2)]

# Generated at 2022-06-14 13:14:53.848065
# Unit test for function product
def test_product():
    """ Unit test for function product """
    # Test not args
    assert list(product()) == [()]
    # Test 1 iterable
    assert list(product([1, 2])) == [(1,), (2,)]
    # Test 2 iterables
    assert list(product([1, 2], [3, 4])) == [(1, 3), (1, 4), (2, 3), (2, 4)]

# Test unit
if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:15:05.085522
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from textwrap import dedent
    from ..utils import FormatCustomTextTest
    from ..httpserver import TqdmHttpServer
    with TqdmHttpServer(port=8080) as server:
        kwargs = {
            "desc": "Testing",
            "total": 3,
            "unit_scale": True,
            "unit": "B",
            "unit_divisor": 1024,
        }
        expected = dedent("""\
            Testing: 100%|██████████| 3.0B/3.0B [00:00<00:00,  ?B/s]
        """)

# Generated at 2022-06-14 13:15:15.780190
# Unit test for function product
def test_product():
    "Check that product() behaves correctly on test inputs"

    def _check(func, *args, **kwargs):
        it = func(*args, **kwargs)
        assert next(it) == ("a", "b", "c", "d")
        assert next(it) == ("a", "b", "c", "e")
        assert next(it) == ("a", "b", "d", "e")
        assert next(it) == ("a", "c", "d", "e")
        for rest in it:
            pass
        try:
            next(it)
            assert False, "iterator did not terminate"
        except StopIteration:
            pass


# Generated at 2022-06-14 13:15:26.610873
# Unit test for function product
def test_product():
    """Test for function product"""
    from .._utils import format_sizeof, import_matplotlib
    from .tests_tqdm import with_setup, pretest_posttest, _range

    @with_setup(pretest=pretest_posttest[0], posttest=pretest_posttest[1])
    def inner_test():
        """Test for function product"""
        # 1.
        list_it = list(product(_range(100000)))
        print(list_it[-10:])

    inner_test()

    # 2.

# Generated at 2022-06-14 13:15:28.925435
# Unit test for function product
def test_product():
    "Test tqdm.product"
    items = range(600)
    result = list(product(items, items))
    assert result == list(itertools.product(items, items))

# Generated at 2022-06-14 13:15:34.986216
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    for i in product(range(4), range(3)):
        assert len(i) == 2
        for j in i:
            assert 0 <= j < 4
    for i in product(range(4), repeat=3):
        assert len(i) == 3
        for j in i:
            assert 0 <= j < 4

# Generated at 2022-06-14 13:15:38.328470
# Unit test for function product
def test_product():
    from itertools import product as p
    a = range(5000)
    for i, j in zip(p(a, repeat=2), product(a, repeat=2)):
        assert i == j

# Generated at 2022-06-14 13:15:47.039523
# Unit test for function product
def test_product():
    try:
        from collections import Counter
    except ImportError:
        return

    assert Counter(list(product(range(5)))) == Counter(range(5))
    assert Counter(list(product(range(5), range(5)))) == Counter(
        (i, j) for i in range(5) for j in range(5))
    assert Counter(list(product(range(5), range(5), range(5)))) == Counter(
        (i, j, k) for i in range(5) for j in range(5) for k in range(5))

# Generated at 2022-06-14 13:15:57.301950
# Unit test for function product
def test_product():
    """Unit test for function `product`"""
    import numpy as np
    from ..utils import format_sizeof

    def f(*args):
        args = list(map(np.array, args))
        return np.sum(args)

    for x, y, z in product(range(6), range(6), range(6)):
        assert f(x, y, z) == x + y + z
    assert not any(x != y for x, y in zip(range(6), product(range(6))))

    # test zip
    assert not any(x != y for x, y in zip(range(6), product(range(6), repeat=1)))
    assert not any(x != y for x, y in zip(range(6), product(range(6), repeat=2)))

# Generated at 2022-06-14 13:16:01.461800
# Unit test for function product
def test_product():
    """Unit test for function product"""
    import pytest
    from ..std import list_, map_

    def gen():
        yield 'a'
        yield 'b'
        yield 'c'

    assert (list(product(gen())) ==
            list(product(gen(), tqdm_class=tqdm_auto)))
    assert (list(product('abc')) ==
            list(product('abc', tqdm_class=tqdm_auto)))

    assert list_ == list
    assert map_ == map

    with pytest.raises(AssertionError,
                       match='For nested tqdm call, use .close() .'):
        list(product(('abc',), tqdm_class=tqdm_auto))

if __name__ == "__main__":
    from doctest import testmod

# Generated at 2022-06-14 13:16:04.602075
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    from . import _test_itertools
    _test_itertools.test_product(product)

# Generated at 2022-06-14 13:16:15.149256
# Unit test for function product
def test_product():
    import nose.tools as nt
    from .tqdm import trange
    from .utils import FormatCustom
    from . import main
    import operator

    list(product([1, 2, 3], repeat=2))
    nt.assert_equal(operator.mul(*map(len, [1, 2, 3])),
                    trange(operator.mul(*map(len, [1, 2, 3]))))
    with main.wrapattr(FormatCustom, 'format_updatable', '{n}'):
        list(product([1, 2, 3], repeat=2))
    from .gui import trange
    try:
        list(product([1, 2, 3], repeat=2))
    except NotImplementedError:
        pass

# Generated at 2022-06-14 13:16:25.847064
# Unit test for function product
def test_product():
    """Test that tqdm.itertools.product is identical to itertools.product"""
    # Test case with ndim < 5
    ndim = 3
    dims = list(range(1, ndim + 1))
    arg = list(map(lambda x: list(range(x)), dims))
    a = itertools.product(*arg)
    b = product(*arg)
    for i, j in zip(a, b):
        assert(i == j)
    # Test case with ndim > 5
    ndim = 6
    dims = list(range(1, ndim + 1))
    arg = list(map(lambda x: list(range(x)), dims))
    a = itertools.product(*arg)
    b = product(*arg)

# Generated at 2022-06-14 13:16:34.607390
# Unit test for function product
def test_product():
    """ Unit test for function product """
    from ..utils import format_sizeof
    from .std import KerasCallback
    from .std import KerasCallbackList
    from .std import KerasCallbackManager
    from .std import KerasGenerator
    from .std import KerasModel
    from .std import KerasModelCheckpoint
    from .std import KerasModelManager
    from .std import KerasSequence
    from .std import KerasSequenceList
    from .std import KerasSequenceManager
    from .std import KerasSequenceManagerPlus
    from .std import KerasSequenceReshaper
    from .std import KerasThinSequence
    from .std import KerasThinSequenceManager
    from .std import Sequence
    from .std import ThinSequence
    from .std import ThinSequenceManager

# Generated at 2022-06-14 13:16:41.150727
# Unit test for function product
def test_product():
    """Test for product."""
    import time
    import numpy as np
    from ..auto import tqdm

    with tqdm(product([1, 2], [5, 6, 7])) as pbar:
        for _ in pbar:
            time.sleep(0.1)

    with tqdm(product(np.arange(3), np.arange(3))) as pbar:
        for _ in pbar:
            time.sleep(0.1)

# Generated at 2022-06-14 13:16:49.994083
# Unit test for function product
def test_product():
    """
    Unit test to check the correct functionality of function product.
    """
    import numpy as np
    from ..tqdm import trange
    items = ['a', 'b', 'c']
    for _ in trange(10, desc='1st loop'):
        for _ in trange(7, desc='2nd loop'):
            for i in product(items, tqdm_class=tqdm_auto):
                assert i[0] in items, 'item not in list'

    items = [100, 101, 102]

# Generated at 2022-06-14 13:16:58.823211
# Unit test for function product
def test_product():
    """ Test function 'product'."""
    # Test without tqdm
    l = list(product([1, 2, 3], [7, 8, 9], repeat=1, tqdm_class=None))
    assert l == [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8),
                 (3, 9)]
    l = list(product([1, 2, 3], [7, 8, 9], repeat=2, tqdm_class=None))

# Generated at 2022-06-14 13:17:10.116106
# Unit test for function product
def test_product():
    """Test function 'product'"""
    from ..utils import format_sizeof

    tqdm_kwargs = dict(
        bar_format="{l_bar}{bar} [ time left: {remaining} "
        "{postfix}, rate: {rate_fmt}{postfix} ]",
        ascii=True,
        smoothing=0.1)
    for t in product("abc", "123", tqdm_class=tqdm_auto, **tqdm_kwargs):
        pass

    tqdm_kwargs = dict(
        bar_format="{l_bar}{bar} [ time left: {remaining} "
        "{postfix}, rate: {rate_fmt}{postfix} ]",
        ascii=True,
        smoothing=0.1)

# Generated at 2022-06-14 13:17:17.778799
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import nose
    iterables_list = [range(10), [0.1, 0.2, 0.3], ["a", "b", "c"]]
    iterables_total = 1
    for i in iterables_list:
        iterables_total *= len(i)
    iterables_list_zip = list(zip(*iterables_list))
    iterable = product(*iterables_list)
    total = 0
    for _ in iterable:
        total += 1
    nose.tools.assert_equal(total, iterables_total)
    with tqdm_auto(total=iterables_total) as t:
        for _ in product(*iterables_list):
            t.update()
            total -= 1

# Generated at 2022-06-14 13:17:20.418862
# Unit test for function product
def test_product():
    """Test product"""
    with tqdm_auto(total=3) as t:
        for i in product(range(2), repeat=2):
            t.update()

# Generated at 2022-06-14 13:17:26.661941
# Unit test for function product
def test_product():
    """Test for product"""
    from ._utils import _range
    for i in _range(3):
        for j in _range(3):
            for p in product(
                    _range(10**i),
                    _range(10**j),
                    tqdm_class=tqdm_auto,
                    desc=str((i, j))):
                assert (p[0] in _range(10**i))
                assert (p[1] in _range(10**j))

# Generated at 2022-06-14 13:17:40.265150
# Unit test for function product
def test_product():
    from .utils import formatted_size
    import numpy as np
    for n, n_iter in zip(range(1, 10), (1, 4, 10, 20, 35, 56, 84, 120, 165)):
        l = list(range(n))
        # correct result
        c = list(map(list, itertools.product(l, repeat=n)))
        # tqdm result
        t = list(product(l, repeat=n, leave=False, tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:17:51.097307
# Unit test for function product
def test_product():
    """Test for function product"""
    # noqa
    from ..tqdm import trange

    assert list(product("123", "ab", "x", tqdm=trange)) == \
        [("1", "a", "x"), ("1", "b", "x"), ("2", "a", "x"), ("2", "b", "x"),
         ("3", "a", "x"), ("3", "b", "x")]

    assert list(product("123", "ab", "x", total=5, tqdm=trange)) == \
        [("1", "a", "x"), ("1", "b", "x"), ("2", "a", "x"), ("2", "b", "x"),
         ("3", "a", "x"), ("3", "b", "x")]

    import numpy

# Generated at 2022-06-14 13:17:55.490729
# Unit test for function product
def test_product():
    """
    Unit test for the :func:`~tqdm.itertools.product` function.
    """
    result = list(product(range(3), repeat=2))
    assert result == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Generated at 2022-06-14 13:18:02.858905
# Unit test for function product
def test_product():
    """Unit test for function product"""
    import re
    import sys

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    tqdm_class = tqdm_auto
    saved_stdout = sys.stdout
    try:
        out = sys.stdout = StringIO()
        for _ in product(*[range(4)] * 3, tqdm_class=tqdm_class,
                         desc="TEST PRODUCT"):
            pass
        # The total and iteration info should be printed
        assert re.findall(r"TEST PRODUCT: *\d+it/s",
                          out.getvalue())[0].startswith("TEST PRODUCT: ")
    finally:
        sys.stdout = saved_stdout



# Generated at 2022-06-14 13:18:12.974433
# Unit test for function product
def test_product():
    """Test function `product`."""
    assert list(product((0, 1), repeat=2)) == list(itertools.product((0, 1), repeat=2))
    assert list(product(range(20))) == list(itertools.product(range(20)))
    assert list(product(range(3), range(3), range(3))) == list(itertools.product(range(3), range(3), range(3)))
    assert list(product(range(5), range(5), range(5), range(5))) == list(itertools.product(range(5), range(5), range(5), range(5)))


if __name__ == '__main__':
    from . import setup_environment
    setup_environment()

    test_product()

# Generated at 2022-06-14 13:18:19.817842
# Unit test for function product
def test_product():
    import numpy as np
    out1 = sorted(product([1, 2], [3, 4], [5, 6]))
    out2 = sorted(np.array((1, 3, 5))
                  * np.array((1, 1, 1))[:, np.newaxis, np.newaxis]
                  + np.array((0, 0, 0))[:, np.newaxis, np.newaxis]
                  + np.array((0, 1, 2))[:, np.newaxis, np.newaxis])
    assert (out1 == out2).all()

# Generated at 2022-06-14 13:18:23.695718
# Unit test for function product
def test_product():
    """Test that .product works as expected"""
    from pytest import approx
    from .tests_itertools import test_product
    test_product(tqdm_product)

# Generated at 2022-06-14 13:18:32.269977
# Unit test for function product
def test_product():
    """
    Test the product function.
    """
    try:
        from itertools import product as it_product
    except ImportError:
        return
    from .tests_tqdm import with_setup, pretest_posttest, _range, closing

    @pretest_posttest
    def inner(iterables, ascii, total, tqdm_cls):
        for product_func in (product, it_product):
            for args in iterables:
                r = list(product_func(*args, tqdm_class=tqdm_cls))

                assert r == [(i, j, k) for i in _range(2) for j in _range(3
                                                                           ) for k in _range(4)]
                assert r[-1] == (1, 2, 3)

# Generated at 2022-06-14 13:18:42.286447
# Unit test for function product
def test_product():
    """Unit test for function product"""
    # Check results
    total = 0
    for i in product(range(3), range(3), range(3)):
        total += 1
        assert i[0] in range(3)
        assert i[1] in range(3)
        assert i[2] in range(3)
    assert total == 3 * 3 * 3  # Check number of iterations
    assert "Done" in "\n".join(
        [l for l in product(range(3), range(3), range(3))])  # Test bar
    # Check total and dynamic_ncols
    assert "3 of 3" in "\n".join(
        [l for l in product(range(3), range(3), range(3), dynamic_ncols=True)])
    # Check iterable exhaustion

# Generated at 2022-06-14 13:18:50.645857
# Unit test for function product
def test_product():
    from .._utils import _decode_html

    for i, _ in enumerate(product(range(15), "abcd", tqdm_class=tqdm_auto)):
        pass
    assert i == 15 * 4

    for _ in product(range(4), range(4), tqdm_class=tqdm_auto,
                     bar_format="{l_bar}{bar}{r_bar}"):
        pass

    for _ in product(range(4), range(4), tqdm_class=tqdm_auto,
                     bar_format=
                     "{desc}: {percentage:3.0f}%|{bar}|"):
        pass


# Generated at 2022-06-14 13:19:08.780336
# Unit test for function product
def test_product():
    # Simple test
    expected = [
        (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3),
        (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3)]
    assert list(product([1, 2], [1, 2], [1, 2, 3])) == expected
    tqdm_product_list = list(product([1, 2], [1, 2], [1, 2, 3], tqdm_class=None))
    assert tqdm_product_list == expected
    assert tqdm_product_list == expected

# Generated at 2022-06-14 13:19:17.750499
# Unit test for function product
def test_product():
    from numpy import array
    import os
    import sys
    import re
    import subprocess

    if os.name != 'posix':
        print("SKIP: requires posix")
        return

    try:
        p = subprocess.Popen(["python", "-m", "tqdm._tqdm_test"],
                             stdout=subprocess.PIPE)
    except OSError:
        print("SKIP: requires python -m tqdm._tqdm_test")
        return

    # Suppress tqdm's default stderr output
    devnull = open(os.devnull, 'w')
    orig_stderr = sys.stderr
    sys.stderr = devnull


# Generated at 2022-06-14 13:19:20.330058
# Unit test for function product
def test_product():
    with tqdm_auto(total=8) as pbar:
        for i in product([0, 1], [0, 1], [0, 1], [0, 1]):
            pass
        pbar.update()

# Generated at 2022-06-14 13:19:28.971838
# Unit test for function product
def test_product():
    import sys
    from ..utils import Timer
    from .utils import FormatMixin

    class T(FormatMixin, Timer):
        def __init__(self, **kwargs):
            self.iterations = 0
            super(T, self).__init__(**kwargs)

        def has_finished(self):
            self.iterations += 1
            return self.iterations > 3

    with tqdm_auto(total=None, desc="Testing product") as t:
        for (a, b) in product(T(leave=True), range(3), tqdm_class=T):
            print("\r" + t.format_meter(1), end="")
            sys.stdout.flush()


# Generated at 2022-06-14 13:19:35.242127
# Unit test for function product
def test_product():
    # Test without total
    r = list(product(range(4)))
    assert r == [(0, 0), (0, 1), (0, 2), (0, 3),
                 (1, 0), (1, 1), (1, 2), (1, 3),
                 (2, 0), (2, 1), (2, 2), (2, 3),
                 (3, 0), (3, 1), (3, 2), (3, 3)]
    # Test with total
    r = list(product(range(4), tqdm_class=tqdm_auto, total=16))

# Generated at 2022-06-14 13:19:39.483559
# Unit test for function product
def test_product():
    """
    Unit test function product.
    """
    from ._deprecate import TqdmDeprecationWarning, deprecated
    with deprecated(TqdmDeprecationWarning):
        from tqdm import product
    try:
        iterable = range(100)
    except NameError:
        iterable = range(100)  # Python 3
    for a, b in product(iterable, iterable):
        pass

# Generated at 2022-06-14 13:19:43.867560
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    assert list(product(range(2), range(2))) == [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert list(product(range(3), range(3))) == [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
    ]

# Generated at 2022-06-14 13:19:54.239147
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from nose.tools import assert_equal, assert_raises

    assert_equal(list(product([1, 2], [])), [])
    assert_equal(list(product([1, 2])), [(1,), (2, )])
    assert_equal(list(product([1, 2], [3, 4])), [(1, 3), (1, 4), (2, 3), (2, 4)])
    assert_equal(list(product([1, 2, 3], repeat=2)),
                 [(1, 1), (1, 2), (1, 3),
                  (2, 1), (2, 2), (2, 3),
                  (3, 1), (3, 2), (3, 3)])


# Generated at 2022-06-14 13:20:01.309688
# Unit test for function product
def test_product():
    from .utils import StringIO, _range
    from .tqdm import trange
    with trange(100) as t:
        for i in product(t, _range(10)):
            pass
    assert len(t) == 100
    with trange(100) as t:
        for i in product(t, _range(10), tqdm_class=t.__class__):
            pass
    assert len(t) == 1000 * 100 / 10

# Generated at 2022-06-14 13:20:04.752463
# Unit test for function product
def test_product():
    """
    Unit tests for function product.
    """
    for i in product(list(range(4)), list("abcd"), list("xyz"),
                     tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:20:28.088464
# Unit test for function product
def test_product():
    from .tests_tqdm import with_setup, _range

    @with_setup(pretest=lambda: None, posttest=lambda: None)
    def unit_test():
        for i in product([1, 2, 3]):
            assert i <= 3

        for i in product([1, 2, 3], [4, 5]):
            assert i[0] in [1, 2, 3]
            assert i[1] in [4, 5]

        for i in product(_range(4), repeat=2):
            assert i[0] < 4
            assert i[1] < 4

        for i in product(*[_range(4), _range(6), _range(8)]):
            assert i[0] < 4
            assert i[1] < 6
            assert i[2] < 8


# Generated at 2022-06-14 13:20:37.285469
# Unit test for function product
def test_product():
    from ._pandas import DataFrame
    for i in product(['a', 'b', 'c'], [1, 2]):
        print(i)
    for i in product({'a': 1, 'b': 2}, {'c': 3, 'd': 4}):
        print(i)
    for i in product({'a': 1, 'b': 2}):
        print(i)
    try:
        for i in product(DataFrame(a=[1, 2, 3], b=[4, 5, 6])):
            print(i)
    except TypeError:
        pass
    else:
        assert False, "product allowed DataFrame input!"
    for i in product([1, 2, 3], total=3):
        print(i)

# Generated at 2022-06-14 13:20:46.415585
# Unit test for function product
def test_product():
    import sys
    from random import random

    from .utils import HiddenPrints

    with HiddenPrints():
        m = 10
        n = 5
        k = 0
        assert list(product(range(m), range(n))) == list(itertools.product(range(m), range(n)))
        assert list(product(range(m), repeat=2)) == list(itertools.product(range(m), repeat=2))
        assert list(product(range(m), range(n), random, random)) == list(itertools.product(range(m), range(n), random, random))
        assert list(product(range(n), repeat=3)) == list(itertools.product(range(n), repeat=3))

# Generated at 2022-06-14 13:20:57.302733
# Unit test for function product
def test_product():
    """Unit test for function `product`."""
    from numpy import prod
    import sys

    def test_bar(iterables, desc, **tqdm_kwargs):
        """Internal test bar."""
        if sys.version_info[0] < 3:
            range_gen = xrange
        else:
            range_gen = range
        for i in range_gen(10):
            list(product(iterables, desc=desc, **tqdm_kwargs))

    def test_range_len():
        """Unit test for function `test_range_len`."""
        lens = []
        for i in range(1, 8):
            lens.extend(list(range(i)))
        for i in lens:
            test_bar(range(i), "Testing range() (len=%i)" % i)

# Generated at 2022-06-14 13:21:04.598638
# Unit test for function product
def test_product():
    # Test product
    import numpy as np
    for i in product((4, 2, 3), name="Test product", unit="i"):
        np.prod(i) == 24
    for i in product((4, 2, 3), tqdm_class=None):
        np.prod(i) == 24
    if __name__ == '__main__':
        tol = 1e-3
        n = int(1e6)
        a = np.random.rand(n)
        b = np.random.rand(n)
        c = a * b
        c_ = sum(map(np.prod, product(a, b)))
        assert abs(c_.sum() - c.sum()) < tol

# Generated at 2022-06-14 13:21:14.599260
# Unit test for function product
def test_product():
    from .tests import closing, closing_iter
    import numpy as np
    with closing(product(range(2), range(2))) as p:
        assert p.total == 4
        for i, a in zip(range(4), p):
            assert i == 0 <= a[0] < 2 and 0 <= a[1] < 2
    with closing_iter(product(range(3), range(3), range(3))) as p:
        assert p.total == 27
        for i, a in zip(range(27), p):
            assert i == 0 <= a[0] < 3 and 0 <= a[1] < 3 and 0 <= a[2] < 3
    assert closing(product(range(2), range(2), tqdm_class=None)).total is None

# Generated at 2022-06-14 13:21:16.415050
# Unit test for function product
def test_product():
    iterables = [range(5), range(5)]
    assert (list(product(*iterables)) ==
            list(itertools.product(*iterables)))

# Generated at 2022-06-14 13:21:19.657401
# Unit test for function product
def test_product():
    import numpy as np
    it = product(range(10), range(10), tqdm=None)
    assert np.all(np.array(list(it)) == np.array(list(itertools.product(range(10), range(10)))))


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:21:26.258708
# Unit test for function product
def test_product():
    try:
        from numpy import product as np_product
    except ImportError:
        raise ImportError("requires numpy")
    try:
        from itertools import izip as zip
    except ImportError:
        pass   # python 3
    from random import shuffle, randint
    L = (randint(1, 10) for _ in range(randint(1, 8)))
    for x in product(L):
        pass

    def assert_total(total, **tqdm_kwargs):
        for i in range(2):  # ensure no false positive
            for j in range(10):
                args = [range(randint(1, 10)) for _ in range(randint(1, 5))]
                if total is None:
                    continue
                assert np_product(list(map(len, args))) == total

# Generated at 2022-06-14 13:21:34.597724
# Unit test for function product
def test_product():
    """Unit test for function product."""
    try:
        import numpy as np  # NOQA
    except ImportError:
        pass
    else:
        print('\n\n== Testing np.ndindex(3, 2, 1) ==\n')
        for _ in product(range(3), range(2), range(1)):
            pass
        print('\n\n== Testing np.ndindex(3) ==\n')
        for _ in product(range(3)):
            pass
        print('\n\n== Testing np.ndindex(4) ==\n')
        for _ in product(range(4)):
            pass

# Generated at 2022-06-14 13:22:12.344624
# Unit test for function product
def test_product():
    import numpy as np
    from .tests_tqdm import with_setup, pretest, posttest, _range

    @with_setup(pretest, posttest)
    def unit():
        # Test nested list
        vals = [
            np.random.rand(x) for x in _range(1, 5)] + [
            np.random.rand(x, x) for x in _range(1, 5)] + [
            np.random.rand(x, x, x) for x in _range(1, 5)] + [
            np.random.rand(x, x, x, x) for x in _range(1, 5)]
        import operator
        for v in vals:
            for i in product(v):
                assert i == v

# Generated at 2022-06-14 13:22:18.398562
# Unit test for function product
def test_product():
    assert list(product("ABC", repeat=2)) == [("A", "A"), ("A", "B"),
                                              ("A", "C"), ("B", "A"),
                                              ("B", "B"), ("B", "C"),
                                              ("C", "A"), ("C", "B"),
                                              ("C", "C")]

if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:22:23.001826
# Unit test for function product
def test_product():
    import numpy as np
    np.random.seed(0)
    random_data = np.random.rand(3)
    random_sum = 0
    for i in tqdm.product(random_data, random_data, random_data):
        random_sum += i[0] * i[1] * i[2]
    assert random_sum == pytest.approx(1.0787248346548016)

# Generated at 2022-06-14 13:22:32.407271
# Unit test for function product
def test_product():
    from numpy.random import randint
    from numpy.testing import assert_array_equal, assert_equal
    for total in [None, 10**randint(5)]:
        for k in [1, randint(5) + 1]:
            for i in range(k + randint(10) + 1):
                a = randint(10, size=(i, i))
                b = randint(10, size=(i, i))
                assert_equal(len(list(product(a, b, total=total))),
                             len(list(itertools.product(a, b))))
                assert_array_equal(list(product(a, b)),
                                   list(itertools.product(a, b)))