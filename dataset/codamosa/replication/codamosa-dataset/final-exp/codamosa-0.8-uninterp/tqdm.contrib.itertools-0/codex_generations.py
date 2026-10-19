

# Generated at 2022-06-14 13:12:25.378358
# Unit test for function product
def test_product():
    import numpy as np
    from ..utils import format_sizeof
    from .. import trange

    np.random.seed(0)

    def test_product_generator():
        for _ in product([1, 2, 3],
                         ["a", "b", "c"],
                         [10, 20, 30],
                         tqdm_class=tqdm_auto):
            pass

    def test_itertools_product():
        for _ in itertools.product([1, 2, 3],
                                   ["a", "b", "c"],
                                   [10, 20, 30]):
            pass


# Generated at 2022-06-14 13:12:30.805177
# Unit test for function product
def test_product():
    """
    Test function product.
    """
    assert list(product(range(5), repeat=2, total=5*5)) == [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
    assert list(product(*[range(5), range(5)])) == [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]

# Generated at 2022-06-14 13:12:32.992745
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from .tests import test_product
    test_product(product)

# Generated at 2022-06-14 13:12:41.189887
# Unit test for function product
def test_product():
    from .tests_tqdm import with_setup, _range

    @with_setup(pretest=lambda: None, posttest=lambda: None)
    def wrapper():
        l = []

        with tqdm_auto(total=20) as t:
            for i in product(_range(7), _range(3)):
                l.append(i)
                t.update()
        return l

    assert wrapper() == [(i, j) for i, j in itertools.product(_range(7),
                                                              _range(3))]

# Generated at 2022-06-14 13:12:50.985752
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from ..utils import format_sizeof
    from .tqdm import trange

    for i, p in enumerate(trange(product(range(4), repeat=3))):
        # test nested and manual update
        assert i == sum([x*(4**i) for i, x in enumerate(reversed(p))])

    # test parallel nested
    assert sum(1 for _ in product(trange(10), repeat=5)) == 10 ** 5

    # test ascii/unicode
    assert u"\u2588" in format_sizeof(product(range(4), repeat=10))

    try:
        import socket
        socket._socket.__len__
    except AttributeError:
        pass

# Generated at 2022-06-14 13:13:00.984928
# Unit test for function product
def test_product():
    """Simple unit tests for product()"""
    # pylint: disable=maybe-no-member
    assert list(product('ab', '12')) == list(itertools.product('ab', '12'))
    assert list(product('ab', '12', repeat=2)) == \
        list(itertools.product('ab', '12', repeat=2))
    assert list(product(range(3))) == list(itertools.product(range(3)))
    assert list(product(range(3), tqdm_class=None)) == \
        list(itertools.product(range(3)))

# Generated at 2022-06-14 13:13:12.368832
# Unit test for function product
def test_product():
    """
    Unit test for `tqdm.iterable.product`.
    """
    import pytest

    a = [1, 2, 3]
    b = ['a', 'b', 'c', 'd']
    c = range(2, 9)

    # Default
    assert list(product(a, b, c, tqdm_class=tqdm_auto)) == \
        list(itertools.product(a, b, c))
    # `total`
    assert list(product(a, b, c, total=10, tqdm_class=tqdm_auto)) == \
        list(itertools.product(a, b, c))
    # `total` not given

# Generated at 2022-06-14 13:13:17.483747
# Unit test for function product
def test_product():
    """Test that product() gives the same results as itertools.product()"""
    it = [3]
    jt = ['a', 'b', 'c']
    kt = ['d', 'e']
    expected = itertools.product(it, jt, kt)
    # Test normal use
    for i in product(it, kt, jt, tqdm_class=tqdm_auto):
        assert next(expected) == i
    # Test tqdm_class override
    for i in product(it, kt, jt, tqdm_class=None):
        assert next(expected) == i
    # Test dynamic total
    for i in product(it, kt, jt, tqdm_class=tqdm_auto, total=None):
        assert next(expected) == i

# Generated at 2022-06-14 13:13:29.524033
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from .formatters import format_dict, format_interval
    from .utils import PrintTestCase

    with PrintTestCase(__file__):
        with tqdm_auto(desc="product(range(5), repeat=3)", unit="it") as t:
            for i in product(range(5), repeat=3):
                t.update(1)
                if t.n >= 30:
                    t.close()
                    break
        ok = all(i >= 0 for i in t.__dict__.values())

# Generated at 2022-06-14 13:13:40.064339
# Unit test for function product
def test_product():
    import pandas as pd
    import numpy as np
    from itertools import product
    import string
    import random
    import time

    random.seed(1234)
    a = list(map(str, range(10)))
    b = list(string.ascii_uppercase)
    c = list(range(100))
    x = list(product(a, b, c))
    t0 = time.time()

    # Check that the results are identical
    assert all([i == j for i, j in zip(product(a, b, c),
                                       tqdm.product(a, b, c))])
    assert tqdm.product(a, b, c), list(product(a, b, c))

    # Check dynamic length

# Generated at 2022-06-14 13:13:46.823221
# Unit test for function product
def test_product():
    with tqdm_auto(unit='i') as t:
        for i in tqdm.product(range(3), range(3)):
            assert i == (i[0], i[1])
            t.update()
    assert t.n == 9
    assert t.total == 9
    assert t.last_print_n == 8

if __name__ == "__main__":
    from ..utils import test_python_version
    test_python_version()
    test_product()

# Generated at 2022-06-14 13:13:55.530586
# Unit test for function product
def test_product():
    from .utils import _range
    from . import trange
    from .std import OKGREEN
    from time import sleep

    print(OKGREEN, "Testing `product`", end=' ', flush=True)
    assert list(product(_range(10), tqdm=lambda x: x)) == \
        list(itertools.product(_range(10)))
    assert list(product(_range(10), _range(10), tqdm=lambda x: x)) == \
        list(itertools.product(_range(10), _range(10)))
    assert list(product(_range(10), _range(10), tqdm=lambda x: x)) == \
        list(itertools.product(_range(10), _range(10)))

# Generated at 2022-06-14 13:14:04.665115
# Unit test for function product
def test_product():
    """
    Simple unit test for function product
    """
    total = 1
    for i in map(len, [range(4), 'ABCD', range(5), range(6), range(7), range(8),
                      range(9), range(10), range(11), range(12), range(13),
                      range(14), range(15), range(16), range(17), range(18),
                      range(19), range(20), range(21), range(22), range(23),
                      range(24), range(25)]):
        total *= i

# Generated at 2022-06-14 13:14:10.044895
# Unit test for function product
def test_product():
    """Unit test for function product."""
    from .tests_tqdm import StringIO, closing, _range


# Generated at 2022-06-14 13:14:17.883022
# Unit test for function product
def test_product():
    """Test `product` function."""
    # pylint: disable=C0103
    def compare_product(a, b):
        p = product(a, b, total=len(a)*len(b),
                    tqdm_class=tqdm_auto, leave=False)
        assert isinstance(p, tqdm_auto)
        assert len(list(p)) == len(a)*len(b)

    compare_product(range(10), range(20))
    compare_product(range(100), range(200))
    compare_product(range(1000), range(2000))
    compare_product(range(10000), range(20000))

# Generated at 2022-06-14 13:14:26.743259
# Unit test for function product
def test_product():
    assert list(product('ABCD', repeat=2)) == [('A', 'A'), ('A', 'B'),
                                               ('A', 'C'), ('A', 'D'),
                                               ('B', 'A'), ('B', 'B'),
                                               ('B', 'C'), ('B', 'D'),
                                               ('C', 'A'), ('C', 'B'),
                                               ('C', 'C'), ('C', 'D'),
                                               ('D', 'A'), ('D', 'B'),
                                               ('D', 'C'), ('D', 'D')]


# Generated at 2022-06-14 13:14:35.683427
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from ..pandas import pandas_apply
    import random
    import pandas as pd
    random.seed(0)
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    rs1 = list(itertools.product(df.x.values, df.y.values))
    rs2 = list(product(df.x.values, df.y.values))
    assert rs1 == rs2

    def myproduct(x, y):
        return list(itertools.product(x, y))
    rs1 = pandas_apply(df, myproduct, axis=1)
    rs2 = pandas_apply(df, lambda x, y: list(product(x, y)), axis=1)


# Generated at 2022-06-14 13:14:45.617506
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    import sys
    import warnings
    from shutil import rmtree
    from tempfile import mkdtemp
    from os import mkdir, chdir
    from os.path import join
    from itertools import product, islice
    import numpy as np

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        try:
            import scipy
            if int(scipy.__version__.split('.', 1)[0]) < 1:
                raise ImportError
        except ImportError:
            scipy = None

# Generated at 2022-06-14 13:14:53.864080
# Unit test for function product
def test_product():
    """Test module."""
    from . import trange
    # Tests
    with trange(0) as t:
        assert list(product("abc", repeat=0)) == [("",) * 0]
    assert list(product("abc", repeat=1)) == [("a",), ("b",), ("c",)]
    assert list(product("abc", repeat=2)) == [("a", "a"), ("a", "b"),
                                              ("a", "c"), ("b", "a"),
                                              ("b", "b"), ("b", "c"),
                                              ("c", "a"), ("c", "b"),
                                              ("c", "c")]

# Generated at 2022-06-14 13:15:00.531882
# Unit test for function product
def test_product():
    from .utils import format_sizeof
    import random
    import time

    def xinterleave(*iterables):
        """
        'interleave' comes from functional programming
        """
        iters = [iter(it) for it in iterables]
        while iters:
            for i, it in enumerate(iters):
                try:
                    yield next(it)
                except StopIteration:
                    iters.pop(i)
                    break

    def xproduct(*iterables):
        """
        Equivalent of `itertools.product`, but with nested
        rather than chain calls to `xrange`

        :param iterables: (list of iterables) The iterables to sum together.
        """
        # In case of an empty iterable, we return an *empty* itertools.product
        # instead of an *inf

# Generated at 2022-06-14 13:15:13.581780
# Unit test for function product
def test_product():
    """Test the `product` function"""
    from tqdm import trange
    from itertools import product
    from random import shuffle, random

    total = 20
    for _ in trange(100):
        expect = list(product(range(total), repeat=3))
        expect.sort()
        for _ in trange(10):
            shuffle(expect)
            result = list(product(range(total), repeat=3))
            result.sort()
            assert expect == result


if __name__ == '__main__':
    from multiprocessing import Pool
    from tqdm import trange
    from itertools import product

    total = 20

# Generated at 2022-06-14 13:15:21.290708
# Unit test for function product
def test_product():
    from ._utils import _sizeof, closing
    from .utils import format_sizeof
    from .utils import FormatCustomTextTest
    from .utils import FormatCustomTextTestBar
    from .contrib.concurrent import thread_map
    import random

    with closing(tqdm_auto(total=_sizeof(range(10)),
                           ascii=True, unit='B', unit_scale=True,
                           dynamic_ncols=True)) as t:
        for i in product(range(10)):
            t.update(_sizeof(i))  # calls t.update(sum([_sizeof(i) for i in obj]))


# Generated at 2022-06-14 13:15:28.926008
# Unit test for function product
def test_product():
    for i in product([], tqdm_class=tqdm_auto):
        pass
    for i in product(range(3), range(3), range(3),
                     tqdm_class=tqdm_auto):
        pass
    assert i == (2, 2, 2)
    for i in product(xrange(3), xrange(3), xrange(3),
                     tqdm_class=tqdm_auto):
        pass
    assert i == (2, 2, 2)

# Generated at 2022-06-14 13:15:39.980288
# Unit test for function product
def test_product():
    """Unit test for function product"""
    assert len(list(product("ABC", range(2), tqdm_class=None))) == 6
    assert len(list(product("ABC", range(2), tqdm_class=tqdm_auto))) == 6
    assert len(list(product("ABC", range(2), tqdm_class=tqdm_auto, miniters=1))) == 6
    assert len(list(product("ABC", range(2), tqdm_class=tqdm_auto, miniters=10))) == 6
    assert list(product("ABC", range(2), tqdm_class=None)) == \
        list(product("ABC", range(2), tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:15:43.021304
# Unit test for function product
def test_product():
    """
    Simple unit test to check that `product` actually works!
    """
    from tqdm._tqdm_test_external import _test_product
    assert _test_product(product) == _test_product(itertools.product)

# Generated at 2022-06-14 13:15:50.037649
# Unit test for function product
def test_product():
    from random import randint
    from random import choice
    from .itertools import detect_interval
    from .post import _enumerate
    for iterables in [[[randint(0, 5)] for _ in range(10)],
                      [[randint(0, 7)] for _ in range(20)],
                      [[randint(-5, 40)] for _ in range(15)],
                      [[randint(-100, -50)] for _ in range(13)],
                      [[randint(-100, 100)] for _ in range(15)]]:
        for i in range(5):
            rnd = choice([True, False])
            n = randint(5, 15)

# Generated at 2022-06-14 13:15:53.195783
# Unit test for function product
def test_product():
    """Test product"""
    iterables = [range(10), range(5)]
    assert product(*iterables) == itertools.product(*iterables)
    for a, b in zip(product(*iterables), itertools.product(*iterables)):
        assert a == b

# Generated at 2022-06-14 13:16:03.966860
# Unit test for function product
def test_product():
    """Test basic functionality of product."""
    list(product("a", "b", "c", tqdm_class=tqdm_auto,
                 desc="Testing product("))
    list(product("a", "b", "c", total=3,
                 desc="Testing product(", tqdm_class=tqdm_auto))
    assert tqdm_auto(product("a", "b", "c")).n == 3  # ensure iterator
    assert tqdm_auto(product("a", "b", "c")).smoothing == 1.0
    assert tqdm_auto(product("a", "b", "c", smoothing=0)).smoothing == 0
    assert tqdm_auto(product("a", "b", "c", smoothing=0)).n == 3  # ensure iterator
    assert t

# Generated at 2022-06-14 13:16:13.007581
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from ..utils import FormatWarnWrap, format_sizeof
    from sys import getsizeof
    from time import sleep, time
    from random import randint

    for i in FormatWarnWrap(range(3), tqdm_class=tqdm_auto):
        sleep(0.2)

    for i in product(range(10), range(10)):
        pass

    for i in product(range(10), range(10), tqdm_class=tqdm_auto):
        pass

    z = product(range(10), range(10))
    print(type(z))

    # Test with a Generator function
    def fun():
        for i in range(10):
            for j in range(10):
                yield (i, j)

# Generated at 2022-06-14 13:16:23.550170
# Unit test for function product
def test_product():
    from .main import tqdm
    from .std import iterable_to_str

    # Test without total
    ans = iterable_to_str(product(range(3), range(3), range(3)))

# Generated at 2022-06-14 13:16:35.667964
# Unit test for function product
def test_product():
    "Test tqdm.product"
    # pylint: disable=unbalanced-tuple-unpacking
    # pylint: disable=unpacking-non-sequence
    # pylint: disable=unused-variable
    a, b = [], []
    with product(range(5), range(10), range(1000000),
                 tqdm_class=tqdm_auto, desc="product") as T:
        for _, _, _ in T:
            pass
        assert T.n == T.total
        assert T.n == 5 * 10 * 1000000
        assert T.pos == T.n

    a, b = [], []
    for _ in product(range(5), range(10), range(1000000),
                     tqdm_class=tqdm_auto):
        pass
    assert T

# Generated at 2022-06-14 13:16:44.542020
# Unit test for function product
def test_product():
    from .utils import TestingIO
    obj = TestingIO()
    for i in product(range(3), range(3), tqdm=obj.write):
        pass
    result = '\r|##     |'
    assert obj.string == result, 'Got: {}\nExpected: {}'.format(obj.string, result)
    obj.close()

    obj = TestingIO()
    for i in product(range(3), range(3), tqdm_class=obj.write):
        pass
    result = '\r|##     |'
    assert obj.string == result, 'Got: {}\nExpected: {}'.format(obj.string, result)
    obj.close()

# Generated at 2022-06-14 13:16:46.240199
# Unit test for function product
def test_product():
    iterable = product('ABC', 'xy', tqdm_class=tqdm_auto)
    for i in iterable:
        pass
    assert iterable.n == 6

# Generated at 2022-06-14 13:16:52.960042
# Unit test for function product
def test_product():
    from . import _utils

    # no error
    _utils.test_enter_leave(
        product, iterable=[range(25), range(20)] + [range(18)] * 9)

    # test kwargs
    try:
        _utils.test_enter_leave(
            product, iterable=[range(25), range(20)], total=500)
        _utils.test_enter_leave(
            product, iterable=[range(25), range(20)], total=499)
    except AssertionError:
        pass
    else:
        raise AssertionError("No error in product unit test")

    # test infinite
    _utils.test_enter_leave(
        product, iterable=[range(1)] * 3)

# Generated at 2022-06-14 13:16:59.876714
# Unit test for function product
def test_product():
    from .tests_tqdm import with_setup, PretendMapping, FakeFile, closing

    @with_setup(PretendMapping().__enter__, PretendMapping().__exit__)
    def inner():
        """
        Tests `product`.
        """

        def dummy_iter(x, y=None):
            for i in x:
                yield i

        with closing(FakeFile()) as fake:
            assert list(product(dummy_iter([]))) == []
            assert list(product(dummy_iter(range(10)))) == list(
                itertools.product(dummy_iter(range(10))))

# Generated at 2022-06-14 13:17:03.701916
# Unit test for function product
def test_product():
    import numpy as np

    a = np.arange(100).reshape(10, 10)
    assert (np.array(list(product(a.shape)))
            == np.array(list(itertools.product(a.shape)))).all()

# Generated at 2022-06-14 13:17:13.176095
# Unit test for function product
def test_product():
    import nose.tools as nt
    from tqdm import tqdm

    try:
        from itertools import product
    except ImportError:
        # Python 2.x (see https://github.com/tqdm/tqdm/issues/26)
        def product(*args, **kwds):
            pools = map(tuple, args) * kwds.get('repeat', 1)
            result = [[]]
            for pool in pools:
                result = [x + [y] for x in result for y in pool]
            for prod in result:
                yield tuple(prod)

    nt.assert_equal(
        list(product(range(10), range(5))),
        list(product(range(10), range(5), tqdm_class=tqdm)))
    nt.assert_equal

# Generated at 2022-06-14 13:17:16.323396
# Unit test for function product
def test_product():
    testdata = [0, 10, 50, 100, 500]
    for total in testdata:
        for i in product(range(total), tqdm_class=tqdm_auto, desc="test_product"):
            pass


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:17:22.435903
# Unit test for function product
def test_product():
    from tqdm import tqdm

    for a, b in tqdm(product('abcd', '1234')):
        pass
    for a, b in tqdm(product(['abcd'], ['1234'])):
        pass
    for a, b in tqdm(product('abcd', '1234'), desc='abc'):
        pass
    for a, b in tqdm(product('abcd', '1234'), total=1):
        pass

# Generated at 2022-06-14 13:17:29.376367
# Unit test for function product
def test_product():
    import os
    iterables = [
        ['casperdcl', 'csdn', 'github'],
        ['python', 'c++', 'c'],
        ['算法', '设计模式', '数据结构'],
    ]
    for element in product(iterables, total=32, unit='items'):
        os.system('clear')
        print(*element)
        input('next: ')

if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:17:41.266699
# Unit test for function product
def test_product():
    import sys
    from ..utils import freeze_support
    freeze_support()
    A = list(tqdm_tqdm(product(range(3), range(3), range(3)),
                       file=sys.stdout))
    assert len(A) == 3**3
    assert sum(A, []) == list(range(3**3))

# Generated at 2022-06-14 13:17:51.597806
# Unit test for function product
def test_product():
    """Unit test for function product"""
    # pylint: disable=import-outside-toplevel
    import numpy as np
    from .utils import numpy_to_tqdm_kwargs
    from .utils import filename_tqdm, NoOpTqdmFile
    with open(filename_tqdm, mode='rb') as fi:
        for n in (0, 1, 2, 10):
            for i, prod in zip(
                    product(range(n), range(n), tqdm_class=NoOpTqdmFile),
                    itertools.product(range(n), range(n))):
                assert np.array_equal(i, prod)

# Generated at 2022-06-14 13:17:56.837596
# Unit test for function product
def test_product():
    from ..utils import AverageMeter
    from ..tqdm import tqdm
    from ..tests import tqdm_tests
    tqdm_tests.test_product()
    # Test AverageMeter
    with tqdm(product(range(20), range(20)), ncols=70) as pbar:
        am = AverageMeter()
        for i in pbar:
            am.update(len(i))
    assert am.avg == 20, am

# Generated at 2022-06-14 13:17:59.936031
# Unit test for function product
def test_product():
    for _ in product(range(2), range(3), range(4)):
        pass
    for _ in product(range(2), total=6):
        pass
    for _ in product(list(range(2))):
        pass
    for _ in product(list(range(2)), tqdm_class=tqdm_auto):
        pass


if __name__ == "__main__":  # pragma: no cover
    test_product()

# Generated at 2022-06-14 13:18:04.148595
# Unit test for function product
def test_product():
    # Test case with no integer sizes
    products = [0]
    for _ in product(products, [1, 2], [3, 4]):
        pass
    assert products == [2]
    # Test case with integer sizes
    products = [0]
    for _ in product(products, [1, 2], [3, 4], tqdm_class=tqdm_auto, total=4):
        pass
    assert products == [4]

# Generated at 2022-06-14 13:18:15.047617
# Unit test for function product
def test_product():
    """
    Unit test for tqdm.compat.itertools.product
    """
    import numpy as np
    import time
    with tqdm_auto(total=None) as t:
        for i in product([1, 2, 3], ['a', 'b']):
            time.sleep(0.01)
            t.update()
    assert t.n == 6
    with tqdm_auto(total=None, mininterval=0, leave=True) \
        as t:
        for i in product([1, 2, 3], ['a', 'b']):
            time.sleep(0.01)
            t.update()
    assert t.n == 6

# Generated at 2022-06-14 13:18:23.431457
# Unit test for function product
def test_product():
    import numpy as np
    import pandas as pd
    from pandas.testing import assert_frame_equal

    p1 = np.array([1, 2, 4])
    p2 = pd.DataFrame([2, 3, 4], index=['a', 'b', 'c'])
    p3 = ['x', 'y']

    p = list(product(p1, p2, p3))
    df = pd.DataFrame(p, columns="a b c".split(" "))
    df["d"] = df["a"] * df["b"]


# Generated at 2022-06-14 13:18:27.612766
# Unit test for function product
def test_product():
    l_a = [1, 2, 3]
    l_b = [1, 2, 3, 4]
    pr = product(l_a, l_b, tqdm_class=tqdm_auto)
    assert len(list(pr)) == len(l_a) * len(l_b)

# Generated at 2022-06-14 13:18:34.924596
# Unit test for function product
def test_product():
    assert list(product(range(0))) == [()]
    assert list(product(range(1))) == [(0,)]
    assert list(product(range(2))) == [(0, 0), (0, 1), (1, 0), (1, 1)]

# Generated at 2022-06-14 13:18:42.245338
# Unit test for function product
def test_product():
    import numpy as np

    L = list(product(np.arange(1000), np.arange(1000), tqdm_class=tqdm_auto))
    assert len(L) == 1000**2
    assert L[-1] == (999, 999)
    L = list(product(np.arange(1000), np.arange(1000)))
    assert len(L) == 1000**2
    assert L[-1] == (999, 999)

# Generated at 2022-06-14 13:18:58.548113
# Unit test for function product
def test_product():
    """Tests the `product` function."""
    a = range(3)
    b = range(4)
    c = []
    for u in product(a, b):
        c.append(u)
    assert c == list(itertools.product(a, b))

# Generated at 2022-06-14 13:19:03.775000
# Unit test for function product
def test_product():
    for x in product(range(10), range(10), tqdm_class=tqdm_auto):
        pass
    for x in product(range(10), range(10), tqdm_class=tqdm_auto):
        pass
    for x in product(range(10), range(10), tqdm_class=tqdm_auto):
        pass



# Generated at 2022-06-14 13:19:11.702304
# Unit test for function product
def test_product():
    """Unit test for product()"""
    from .utils import closing
    from .std import StringIO as py3compat

    try:
        from subprocess import getoutput  # py3
    except ImportError:
        from commands import getoutput  # py2

    with closing(py3compat.StringIO()) as our_file:
        for _ in product(range(3), repeat=3, tqdm_class=tqdm_auto,
                         file=our_file):
            pass
    # NOTE: getoutput() already uses universal_newlines=True
    assert getoutput("tail -n 1 '{f}'".format(f=our_file.name)) == '2 2 2:'

# Generated at 2022-06-14 13:19:17.224929
# Unit test for function product
def test_product():
    """Use the following to test:
    python tqdm/tqdm_itertools.py"""
    import sys

    for i in product(range(10 ** 2), range(10 ** 1),
                     tqdm_class=tqdm_auto, mininterval=0.1):
        sys.stderr.write("\r" + str(i))


if __name__ == "__main__":
    # run test_product
    test_product()

# Generated at 2022-06-14 13:19:26.034718
# Unit test for function product
def test_product():
    from numpy.testing import assert_array_equal
    p1 = product(['a', 'b'], repeat=3)
    p2 = product(['a', 'b'], ['a', 'b'], ['a', 'b'])
    assert_array_equal(list(p1), list(p2))
    p3 = product('abc', repeat=2)
    assert list(p3) == [('a', 'a'),
                        ('a', 'b'),
                        ('a', 'c'),
                        ('b', 'a'),
                        ('b', 'b'),
                        ('b', 'c'),
                        ('c', 'a'),
                        ('c', 'b'),
                        ('c', 'c')]
    p4 = product(range(4), repeat=3)

# Generated at 2022-06-14 13:19:29.366223
# Unit test for function product
def test_product():
    """Unit test for function product"""
    assert list(product(range(3), range(3))) == [
        (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Generated at 2022-06-14 13:19:32.617811
# Unit test for function product
def test_product():
    import numpy
    assert numpy.array_equal(numpy.fromiter(
        product([[0, 1], [0, 1]], tqdm_class=None), dtype="i,i"),
        numpy.array([(0, 0), (0, 1), (1, 0), (1, 1)], dtype="i,i"))

# Generated at 2022-06-14 13:19:40.665864
# Unit test for function product
def test_product():
    import math
    import os
    from .utils import FormatWrapBase, _range

    class FormatWrap(FormatWrapBase):
        def __len__(self):
            return len(self._iterable)

        def __iter__(self):
            for i in _range(len(self)):
                yield self[i]

        def __getitem__(self, key):
            return self._iterable[key]

    def bar(total=None, **kwargs):
        kwargs.setdefault("unit_scale", True)
        return FormatWrap(**kwargs)


# Generated at 2022-06-14 13:19:43.482675
# Unit test for function product
def test_product():
    import numpy as np

    for data in ((), (1,), (1, 2, 3)):
        np.testing.assert_equal([i for i in product(*data, **dict(tqdm_class=None))],
                                [i for i in itertools.product(*data)])

# Generated at 2022-06-14 13:19:53.923976
# Unit test for function product
def test_product():
    import sys
    import io

    def _test(args, itr, length, result_str):
        # Restore stdout
        sys.stdout = old_stdout
        # Check that tqdm does not output anything
        out = result.getvalue()
        assert out == result_str
        # Check that iterator works
        it = product(*args)
        assert len(list(it)) == length
        for x, y in zip(itr, it):
            assert x == y
        # Redirect stdout
        result = io.StringIO()
        sys.stdout = result

    old_stdout = sys.stdout
    result = io.StringIO()
    sys.stdout = result

    _test(([1, 2],), (1, 2,), 2, "")

# Generated at 2022-06-14 13:20:54.943624
# Unit test for function product
def test_product():
    """
    Unit test for `tqdm.utils.itertools.product`.
    """
    from nose.tools import assert_equal, assert_raises
    from numpy.random import randint

    with tqdm_auto(total=21 * 21 * 21, file=None) as t:
        assert_equal(t.total, 21 * 21 * 21)
        for _ in product(range(21), range(21), range(21)):
            t.update()

    with tqdm_auto(total=None, file=None) as t:
        assert_equal(t.total, None)
        for _ in product(range(1)):
            t.update()


# Generated at 2022-06-14 13:21:03.483746
# Unit test for function product
def test_product():
    def _test(a=None, b=None, tqdm_class=tqdm_auto):
        res = product(a, b, tqdm_class=tqdm_class)
        return list(res)
    assert _test(a='ab', b=range(3)) == \
        [('a', 0), ('a', 1), ('a', 2), ('b', 0), ('b', 1), ('b', 2)]
    assert _test(a='ab', b=None) == \
        [('a', None), ('b', None)]
    assert _test(a=None, b=None) == \
        [(None, None)]
    assert _test(a=None, b=None, tqdm_class=None) == \
        [(None, None)]

# Generated at 2022-06-14 13:21:14.084669
# Unit test for function product
def test_product():
    from .tqdm import tqdm_py_class
    # init counters
    lst = list(range(10))
    pl = []
    kwargs = {"tqdm_class": tqdm_py_class, "total": 10}

    # test <function product>
    for i in product(lst, tqdm_kwargs=kwargs):
        pl.append(i)
    assert pl == [(i,) for i in lst]

    # test <function product>
    pl = []
    for i in product(lst, lst, tqdm_kwargs=kwargs):
        pl.append(i)
    assert pl == [(i, j) for i, j in itertools.product(lst, lst)]

    # test <function product>
    pl = []

# Generated at 2022-06-14 13:21:22.193711
# Unit test for function product
def test_product():
    import numpy as np

    assert list(product([1,2,3], [4,5], [6,7,8])) == [(1,4,6), (1,4,7), (1,4,8), (1,5,6),
                                                     (1,5,7), (1,5,8), (2,4,6), (2,4,7),
                                                     (2,4,8), (2,5,6), (2,5,7), (2,5,8),
                                                     (3,4,6), (3,4,7), (3,4,8), (3,5,6),
                                                     (3,5,7), (3,5,8)]

# Generated at 2022-06-14 13:21:28.165698
# Unit test for function product
def test_product():
    from numpy import product
    for N in (1, 2, 3):
        for M in (1, 2, 3):
            p = product(range(N), range(M))
            p1 = [i for i in product(range(N), range(M))]
            p2 = [i for i in product(range(N), range(M),
                                     tqdm_class=tqdm_auto)]
            assert p1 == p2
            assert list(p) == p1

# Generated at 2022-06-14 13:21:38.265998
# Unit test for function product
def test_product():
    from random import randint
    from .utils import FormatTestCounter
    from .utils import format_meter, freeze_attr
    from .utils import ClosingContext, closing
    from .utils import SimpleTimer

    from . import _tqdm  # isort:skip # noqa: E402
    tqdm = _tqdm.tqdm
    _tqdm.set_slower_interval()

    try:
        import numpy as np
        assert(np)
        has_np = True
    except ImportError:
        has_np = False

    def test(iterables, total, nb_it=2000):
        """
        Unit test for function `product`:
        product(*iterables, tqdm_class=tqdm_class,
                total=total) = iterable
        """

# Generated at 2022-06-14 13:21:40.583310
# Unit test for function product
def test_product():
    from ._utils import _test_iterator_eq
    _test_iterator_eq(product(-3, 2, tqdm_class=tqdm_auto),
                      itertools.product(-3, 2))


# Test export

# Generated at 2022-06-14 13:21:49.106251
# Unit test for function product
def test_product():
    list(product(range(3), repeat=3))
    list(product(range(3), range(3), repeat=3))
    list(product(range(3), range(3), range(3), repeat=3))
    list(product(range(3), repeat=1))
    list(product(range(3), range(3), repeat=1))
    list(product(range(3), range(3), range(3), repeat=1))
    list(product(range(3), range(3), range(3), repeat=4))
    list(product(range(3), range(1)))
    list(product(range(3), range(2), range(5), range(1)))

# Generated at 2022-06-14 13:21:51.270499
# Unit test for function product
def test_product():
    for i in product(range(4), range(3), range(3)):
        pass

# Generated at 2022-06-14 13:22:00.242091
# Unit test for function product
def test_product():
    """ Unit test for function 'product' """

    def _test_product_spec(iterables_spec, total_spec, dtype):
        """
        Perform unit test for function "product" with additional arguments as
        specified.

        Args:
            iterables_spec (Iterable[Iterable]): Input iterables spec
            total_spec (int): Expected total value
            dtype (str): Type of the iterable
        """
        iterables = [np.arange(spec) for spec in iterables_spec]
        total = total_spec
        actual_total = 0
        for _ in product(*iterables):
            actual_total += 1
        assert total == actual_total

    # Test without any iterables
    _test_product_spec([], 1, 'int')

    # Test with empty iterables
    _test_