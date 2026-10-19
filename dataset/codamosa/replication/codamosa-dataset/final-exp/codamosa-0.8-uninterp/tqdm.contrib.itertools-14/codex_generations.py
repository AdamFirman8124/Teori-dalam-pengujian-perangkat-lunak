

# Generated at 2022-06-14 13:12:32.198321
# Unit test for function product
def test_product():  # pragma: no cover
    from ..pandas import tqdm
    for i in tqdm.product(range(4)):
        pass
    for i in tqdm.product([1, 2, 3], ['a', 'b', 'c'], total=6):
        pass

# Generated at 2022-06-14 13:12:37.374774
# Unit test for function product
def test_product():
    """Unit test."""
    from nose.tools import assert_equal
    from os import getpid, listdir
    temp_list = listdir(b".") + [b"hello", b"world"]
    assert_equal(list(product(temp_list, r=getpid())),
                 list(itertools.product(temp_list)))



# Generated at 2022-06-14 13:12:45.808327
# Unit test for function product
def test_product():
    from ..utils import SimpleNamespace

    iterables = [[1, 2, 3] for _ in range(2)]
    with SimpleNamespace(tqdm_class=tqdm_auto) as tqdm_kwargs:
        for _ in product(*iterables, **vars(tqdm_kwargs)):
            pass


if __name__ == "__main__":
    from ._tqdm_testsuite import _test_itertools_wrapper
    _test_itertools_wrapper(product, n_samples=5, min_iters=2)

# Generated at 2022-06-14 13:12:48.709803
# Unit test for function product
def test_product():
    """Test function `product`."""
    return sum(product(range(n)) for n in tqdm_auto(range(1, 6)))


# Generated at 2022-06-14 13:13:00.262327
# Unit test for function product
def test_product():
    from .._tqdm_test_include import tqdm_assert_equal
    from ..utils import FormatCustomText, _range
    for i in product(_range(4), repeat=4):
        pass
    with FormatCustomText(t=True):
        for i in product(_range(4), repeat=4):
            pass
    tqdm_assert_equal(t.format_dict['rate'], 4)
    tqdm_assert_equal(t.format_dict['rate_noinv'], 1.0 / 4.0)


# Add auto detection of tqdm_gui
if tqdm_auto.gui.is_notebook():
    from ..gui import tqdm as tqdm_gui


# Generated at 2022-06-14 13:13:11.715352
# Unit test for function product
def test_product():
    from .. import trange
    from .utils import TestCase

    class TestProduct(TestCase):
        def test_product_list(self):
            import sys
            results = list(product(list(range(7)), list(range(11))))
            self.assertEqual(len(results), 77)

        def test_product_generator(self):
            import sys
            results = list(product(range(7), range(11)))
            self.assertEqual(len(results), 77)

        def test_product_product_caching_not_lazy(self):
            import sys
            if sys.version_info.major < 3:
                results = list(product(list(range(7)), range(11)))
            else:
                results = list(product(range(7), range(11)))
            self.assertEqual

# Generated at 2022-06-14 13:13:19.976231
# Unit test for function product
def test_product():
    """ Unit test for function product """
    if __name__ == "__main__":
        # 2D-product
        iterable = product(range(3), range(3))
        assert list(iterable) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1),
                                  (1, 2), (2, 0), (2, 1), (2, 2)]
        # 3D-product
        iterable = product(range(2), range(2), range(2))
        assert list(iterable) == [(0, 0, 0), (0, 0, 1),
                                  (0, 1, 0), (0, 1, 1),
                                  (1, 0, 0), (1, 0, 1),
                                  (1, 1, 0), (1, 1, 1)]

# Generated at 2022-06-14 13:13:27.869536
# Unit test for function product
def test_product():
    """
    Test `itertools.product`
    """
    from numpy.random import randint
    from numpy.testing import assert_array_equal
    r = randint(0, 5, size=10)
    a = list(product([0, 1, 2, 3, 4], repeat=len(r)))
    b = [list(r) for r in itertools.product([0, 1, 2, 3, 4], repeat=len(r))]
    assert_array_equal(a, b)

# Generated at 2022-06-14 13:13:32.872480
# Unit test for function product
def test_product():
    import pytest
    from ..std import all
    iterables = [[-1, 1, 1], [-1, -1, 1, 1], [-1, 1, 1]]
    itr = product(*iterables, total=2**3, tqdm_class=tqdm_auto)
    tests = all(
        [p[0]**2 + p[1]**2 + p[2]**2 == 1 for p in itr])
    assert tests


if __name__ == "__main__":
    pytest.main([__file__])

# Generated at 2022-06-14 13:13:41.643224
# Unit test for function product
def test_product():
    assert list(product([1, 2, 3])) == [(1,), (2,), (3,)]
    assert list(product([1, 2, 3], [4, 5, 6])) == [
        (1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

# Generated at 2022-06-14 13:13:54.730529
# Unit test for function product
def test_product():
    """
    Unit testing function. See:
        `$ nosetests --verbose --with-coverage --cover-erase --cover-package=utils.itertools.itertools_tqdm`
    """
    from nose.tools import assert_equal
    from .itertools import product
    from .itertools import range, repeat
    from ..miscs import naturalsize
    from .test_misc import tqdm_test_cls
    irange = range(5)
    irepeat = repeat(irange)

# Generated at 2022-06-14 13:14:01.875742
# Unit test for function product
def test_product():
    """Test for function product"""
    for a, b in product([1, 2, 3], ["a", "b", "c"], tqdm_class=tqdm_auto):
        pass
    for a, b, c in product(["a", "b", "c"], [1, 2, 3], ["A", "B", "C"],
                           tqdm_class=tqdm_auto):
        pass


if __name__ == '__main__':
    try:
        test_product()
    except KeyboardInterrupt:
        pass
    finally:
        print('\n')

# Generated at 2022-06-14 13:14:07.184397
# Unit test for function product
def test_product():
    from .utils import n_samples, list_lossless
    expected_size = 100
    _ = list(product(range(expected_size), range(expected_size),
                     tqdm_class=tqdm_auto))
    assert n_samples(_) == expected_size ** 2
    assert len(_) == expected_size ** 2
    assert list_lossless(_)

# Generated at 2022-06-14 13:14:12.689978
# Unit test for function product
def test_product():
    from .tests import TestCase

    with TestCase() as testcase:
        for i in product(range(10), range(10), range(10),
                         tqdm_class=testcase.default_wrapper):
            assert isinstance(i, tuple)
            assert len(i) == 3

if __name__ == '__main__':
    from .tests import _test_functions

    _test_functions(globals(), verbose=True)

# Generated at 2022-06-14 13:14:16.525409
# Unit test for function product
def test_product():
    """Unit test for function product"""
    it1 = iter([1, 2, 3])
    it2 = iter(['a', 'b', 'c'])
    it3 = iter(['A', 'B', 'C'])
    for i in product(it1, it2, it3):
        pass

# Generated at 2022-06-14 13:14:25.285642
# Unit test for function product
def test_product():
    from itertools import izip, product
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    len1 = 4
    len2 = 2
    total = len1 * len2

    def to_str(a):
        return list(map(str, a))

    with StringIO() as s:
        # test using lists
        a = [0, 1, 2, 3]
        b = [10, 11]
        gen = itertools.izip(product(a, b, tqdm_class=tqdm_auto, file=s,
                                     leave=False, disable=False),
                             product(a, b))
        for a, b in gen:
            assert to_str(a) == to_str(b)
        assert s.getvalue

# Generated at 2022-06-14 13:14:34.578107
# Unit test for function product
def test_product():
    """ Test function `tqdm.itertools.product` """
    import sys
    import random
    # pylint: disable=protected-access
    from tqdm._utils import _term_move_up
    # pylint: enable=protected-access
    with open(__file__, 'rb') as fd:
        bin_data = fd.read()

    def randbytes(n):
        """ Generate random bytes """
        return bytes(random.getrandbits(8) for _ in range(n))

    rounds = 20

# Generated at 2022-06-14 13:14:43.571080
# Unit test for function product
def test_product():
    from sys import version_info
    for tqdm_cls in [tqdm, tqdm_gui, tqdm_notebook, tqdm_pandas, tqdm_wget]:
        for n in range(2):
            for i in product(range(3), repeat=n, tqdm_class=tqdm_cls):
                pass
            for i in product(range(10**n), repeat=n, tqdm_class=tqdm_cls):
                pass
        for i in product(range(3), range(2), tqdm_class=tqdm_cls):
            pass
        # test Unicode

# Generated at 2022-06-14 13:14:52.683076
# Unit test for function product
def test_product():
    """
    Unit test for product
    """
    from .utils import FormatWrapBase
    from .utils import FakeTqdmFile

    class FormatWrap(FormatWrapBase):
        """
        Wrap format function
        """
        def __init__(self, format_str):
            self.format_str = format_str
        def __enter__(self):
            return self
        def __exit__(self, *exc):
            return False  # True = suppress exception

    check_str = "abcdefghijklmnopqrstuvwxyz"
    n = 2

# Generated at 2022-06-14 13:14:58.436097
# Unit test for function product
def test_product():
    """Sample usage of `product`."""
    import numpy as np
    import tqdm

    range_ = [tuple(np.arange(i)) for i in [10, 3, 5]]

    # First, testing using a simple wrapper
    res = []
    for i in tqdm.product(*range_):
        res.append(i)
    assert len(res) == 10 * 3 * 5

    # Then, testing with "no bar mode"
    res = []
    for i in tqdm.product(*range_, disable=True):
        res.append(i)
    assert len(res) == 10 * 3 * 5

# Generated at 2022-06-14 13:15:10.192849
# Unit test for function product
def test_product():
    for n in (1, 2, 5, 10):
        for m in range(2, n + 1):
            for i in product(range(n), range(m)):
                assert sum(i) < n + m

# Generated at 2022-06-14 13:15:18.973201
# Unit test for function product
def test_product():
    import numpy as np
    assert list(product([1, 2, 3], [10, 20, 30, 40])) == list(itertools.product([1, 2, 3], [10, 20, 30, 40]))
    assert list(product('ABCD', 'xy')) == list(itertools.product('ABCD', 'xy'))
    assert list(map(sum, product(range(4), repeat=2))) == [0, 0, 0, 1, 0, 2, 0, 3, 1, 1, 1, 2, 1, 3, 2, 2, 2, 3, 3, 3]

# Generated at 2022-06-14 13:15:28.217682
# Unit test for function product
def test_product():
    import numpy as np
    from numpy.testing import assert_array_equal

    # Test 1
    a = product(range(5), repeat=5)
    b = itertools.product(*(range(5),)*5)
    assert_array_equal(np.array(list(a)), np.array(list(b)))

    # Test 2
    a = product(range(5), repeat=5, tqdm_class=tqdm_auto.tqdm_notebook)
    b = itertools.product(*(range(5),)*5)
    assert_array_equal(np.array(list(a)), np.array(list(b)))

# Generated at 2022-06-14 13:15:40.358773
# Unit test for function product
def test_product():
    import sys
    # Test product
    n = 1000
    x, y = list(range(n)), list(range(n))
    z = list(itertools.product(x, y))
    assert list(product(x, y)) == z, "itertools.product is broken!"
    if sys.version_info[0] >= 3:
        assert list(product(x, y, tqdm_class=tqdm_auto)) == z, \
            "tqdm.product is broken!"
    assert list(product(x, y, tqdm_class=None)) == z, \
        "tqdm.product is broken!"
    # Test product with exception
    try:
        next(product([1], range(10)))
    except TypeError:
        pass

# Generated at 2022-06-14 13:15:44.757161
# Unit test for function product
def test_product():
    from ._utils import _assert_iterable_equal
    iterables = [["a", "b", "c"], range(3)]
    _assert_iterable_equal(
        product(*iterables), itertools.product(*iterables))
    _assert_iterable_equal(
        product(*iterables, total=1), itertools.product(*iterables))

# Generated at 2022-06-14 13:15:51.073884
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from .tests import closing, closing_to_filelike
    from .utils import TestCase, StringIO

    with TestCase(tqdm_class=tqdm_auto) as tc:
        # Named args
        closing(lambda: list(tc.tqdm(product(
            range(10), tqdm_class=tc.tqdm_cls))))
        # Normal use case
        closing(lambda: list(tc.tqdm(product(
            range(10), range(10), range(10), range(10), range(10),
            tqdm_class=tc.tqdm_cls))))
        # Indexable iterables

# Generated at 2022-06-14 13:16:00.731256
# Unit test for function product
def test_product():
    """
    It tests the basic functionality of the product wrapper.
    """
    l = [("a", "b"), [1, 2, 3], ["A", "B", "C"]]

    assert list(product("abc", [1, 2, 3])) == [("a", 1), ("a", 2), ("a", 3),
                                               ("b", 1), ("b", 2), ("b", 3),
                                               ("c", 1), ("c", 2), ("c", 3)]
    assert list(product(*l)) == list(itertools.product(*l))
    assert list(product("abc", repeat=2)) == list(itertools.product("abc",
                                                                     repeat=2))

# Generated at 2022-06-14 13:16:11.268484
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from ._tqdm import trange
    for a in product(range(10), range(2)):
        pass
    for a in product(range(10), range(10)):
        pass
    for a in product(range(10), range(10), range(10), range(5)):
        pass
    for a in product(range(10), range(10), range(10), 
                     range(10), range(0)):
        pass

# Generated at 2022-06-14 13:16:17.172217
# Unit test for function product
def test_product():
    for i in product([1,2,3], [4,5,6], [7,8,9], tqdm_class=tqdm_auto):
        print (i)
    for i in product([1,2,3], [4,5,6], [7,8,9], tqdm_class=tqdm_auto, postfix="Woop!"):
        print (i)

# Generated at 2022-06-14 13:16:27.599404
# Unit test for function product
def test_product():
    """Test product"""
    # Setup
    from ..utils import sizeof_fmt
    values = [
        ["value_" + str(i) for i in range(10)],
        ["value_" + str(i) for i in range(100)],
        ["value_" + str(i) for i in range(1000)],
        ["value_" + str(i) for i in range(10000)],
    ]

    # Tests
    for k in values:
        l = [x for x in product(k)]
        assert k == l

    print("mem usage:", sizeof_fmt(product.__code__.co_sizeof()))
    return True

# Test
if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:18:23.347734
# Unit test for function product
def test_product():
    """
    Tests `tqdm.itertools.product` (via `test_itertools.main`).
    """
    from tqdm.tests import main
    main(globals())

# Generated at 2022-06-14 13:18:32.008648
# Unit test for function product
def test_product():
    """Unit test for function product."""
    from numpy import prod
    import sys

    def prod_it(iterables, ttotal=None, **tqdm_kwargs):
        """Calculate product of iterables items."""
        t = tqdm_kwargs.setdefault('tqdm_class', tqdm_auto)(
            total=ttotal, disable=not tqdm_kwargs.get('disable', False)
        )
        for _ in product(iterables, **tqdm_kwargs):
            pass
        return t.total

    for n in (1, 4, 16, 128):
        rng = range(n)
        assert prod([rng, rng]) == prod_it(
            rng, ttotal=n * n, disable=False
        )

# Generated at 2022-06-14 13:18:34.126432
# Unit test for function product
def test_product():
    list(product([1, 2], ["a", "b"], tqdm_class=tqdm_auto.tqdm_gui))


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:18:40.171386
# Unit test for function product
def test_product():
    """Unit test for function product"""

    assert list(product([1])) == [(1,)]
    assert list(product([1, 2, 3], repeat=2)) == [(1, 1), (1, 2), (1, 3),
                                                  (2, 1), (2, 2), (2, 3),
                                                  (3, 1), (3, 2), (3, 3)]
    assert list(product([1, 2, 3], [3, 4, 5, 6])) == [(1, 3), (1, 4),
                                                      (1, 5), (1, 6),
                                                      (2, 3), (2, 4),
                                                      (2, 5), (2, 6),
                                                      (3, 3), (3, 4),
                                                      (3, 5), (3, 6)]

# Generated at 2022-06-14 13:18:49.020750
# Unit test for function product
def test_product():
    # Test with one iterable
    if next(product(['a', 'b', 'c'])) != ('a',):
        print('FAIL', 'product 1')

    # Test with two iterables
    if (next(product(['a', 'b', 'c'], [1, 2, 3])) != ('a', 1) or
            next(product(['a', 'b', 'c'], [1, 2, 3])) != ('a', 2)):
        print('FAIL', 'product 2')

    # Test with two iterables and total
    if next(product(['a', 'b', 'c'], [1, 2, 3], total=6)) != ('a', 1):
        print('FAIL', 'product 3')

# Generated at 2022-06-14 13:18:53.553424
# Unit test for function product
def test_product():
    "Test that product(a, b, ...) is equivalent to itertools.product(a, b, ...)"
    inp = (range(3), range(3), range(3))
    tqdm_prod = product(*inp, tqdm_class=None)
    it_prod = itertools.product(*inp)
    for i, j in zip(tqdm_prod, it_prod):
        assert i == j

# Generated at 2022-06-14 13:19:03.826485
# Unit test for function product
def test_product():
    """Tests `.product`"""
    # Basic test
    assert list(product([1, 2, 3], [4, 5])) == [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

    # Test that tqdm_class works
    try:
        from tqdm import tqdm
    except ImportError:
        pass
    else:
        assert [i for i in product([1, 2, 3], [4, 5], tqdm_class=tqdm(leave=False))] == [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

    # Test that total keyword works

# Generated at 2022-06-14 13:19:13.434453
# Unit test for function product
def test_product():
    import numpy as np
    import sys
    arr = np.linspace(1, 10, num=10)
    # Unpack/reorder the results of itertools.product
    x, y, z, t = np.array(list(itertools.product(arr, arr, arr, arr))) \
        .T[::-1].T.reshape(4, 10, 10, 10, 10).T
    arr = np.array(list(product(arr, arr, arr, arr)))
    assert (arr.T[3] == x).all()
    assert (arr.T[2] == y).all()
    assert (arr.T[1] == z).all()
    assert (arr.T[0] == t).all()
    # Check that the unit test itself is not broken

# Generated at 2022-06-14 13:19:22.382674
# Unit test for function product
def test_product():
    import operator
    from ..std import numpy as np

    assert set(product(range(3), range(3))) == set(
        product(np.arange(3), range(3))) == set(product(range(3), np.arange(3)))

# Generated at 2022-06-14 13:19:30.149713
# Unit test for function product
def test_product():
    from ._utils import _range, format_sizeof
    try:
        from numpy import arange
    except ImportError:  # pragma: no cover
        # TODO (experimental): update to use `compat`
        from ._compat import arange
    for N in _range(1, 9):
        print("-" * 100)
        dims = [10] * N
        print(format_sizeof(product(*(range(i) for i in dims),
                                     tqdm_class=tqdm_auto)))
        print(format_sizeof(itertools.product(*(range(i) for i in dims))))
        print(format_sizeof(arange(10 ** N).reshape(dims)))

# Generated at 2022-06-14 13:22:03.068493
# Unit test for function product
def test_product():
    """Test tqdm(iterable, unit='iter', nrows=1e6, leave=True)"""
    from .utils import FormatWarn
    from .std import tqdm

    # Test base exception
    with FormatWarn(('\n'
                     '\t| {0}(*iterables, tqdm_class=<default>, '
                     'total=None)\n'
                     '\tUse `tqdm.auto.tqdm(**kwargs)` '
                     'instead of `tqdm(iterable, **kwargs)` '
                     'to hide this warning\n').format("tqdm.product"),
                    category=DeprecationWarning,
                    ):
        tqdm.product([1, 2, 3], unit='iter')

# Generated at 2022-06-14 13:22:12.720751
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from .tests import closing, pretest_posttest

    with closing(pretest_posttest()) as (t, _io):
        for _i in product(tqdm_class=t.__class__, iterable=range(1000),
                          iterable2=range(1000), disable=True):
            pass
        assert t.n == 1000
        t.close()
        assert t.n == 1000  # make sure closing doesn't blow up


# Generated at 2022-06-14 13:22:20.191046
# Unit test for function product
def test_product():
    import sys
    from .trange import trange

    for args in [[], ['123'], ['1', '', '3'],
                 ['a', 'b'], ['a', 'b', 'c'], ['a', 'b', '', 'd']]:
        for out in [sys.stdout, None]:
            for tqdm_class in [trange, tqdm_auto]:
                l = list(product(*args, tqdm_class=tqdm_class, file=out))
                assert l == list(itertools.product(*args))

# Generated at 2022-06-14 13:22:26.624115
# Unit test for function product
def test_product():
    for i in product("abc", tqdm_class=tqdm_auto):
        pass
    for i in product("abc", "def", tqdm_class=tqdm_auto, total=None):
        pass
    for i in product("abc", "def", tqdm_class=tqdm_auto, total=None):
        pass
    for i in product("abc", "def", tqdm_class=tqdm_auto, total=12):
        pass
    for i in product("abc", "def", tqdm_class=tqdm_auto, total=13):
        pass
    for i in product("abc", "def", tqdm_class=tqdm_auto, total=13):
        pass