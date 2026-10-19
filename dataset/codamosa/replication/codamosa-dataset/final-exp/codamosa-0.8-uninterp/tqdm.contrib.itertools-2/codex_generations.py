

# Generated at 2022-06-14 13:12:47.445600
# Unit test for function product
def test_product():
    """Test function product(iterables)"""
    import numpy as np
    import math

    n1, n2, n3 = 3, 4, 5
    l1, l2, l3 = range(n1), range(n2), range(n3)
    for iterable in (l3, l2, l1):
        for i in iterable:
            assert i == next(iterable)

    for iterables in (l1, l2, l3, l1, l2, l3), (l3, l2, l1, l1):
        for i in product(*iterables):
            assert i == next(iterables)

    for i in product(range(n1), range(n2), range(n3)):
        assert i == next(i)

# Generated at 2022-06-14 13:12:50.268365
# Unit test for function product
def test_product():
    """Run doctest on function product"""
    import doctest
    import sys
    if sys.version_info[:2] < (2, 7):
        res = doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
    else:
        res = doctest.testmod(verbose=True)
    if res[0] == 0:
        print("Doctest of function product: Success!")


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:12:56.112792
# Unit test for function product
def test_product():
    from itertools import product as it_product
    assert [i for i in product([1, 2, 3], repeat=3, tqdm_class=None)] == \
        list(it_product([1, 2, 3], repeat=3))


if __name__ == "__main__":  # pragma: no cover
    test_product()

# Generated at 2022-06-14 13:13:00.168498
# Unit test for function product
def test_product():
    """
    >>> from tqdm import trange
    >>> for _ in trange(10):
    ...    for _ in trange(10):
    ...        list(product('abc', repeat=2))
    """
    pass

# Generated at 2022-06-14 13:13:01.226748
# Unit test for function product
def test_product():
    from .utils import FormatTe

# Generated at 2022-06-14 13:13:11.392999
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from .main_classes import _test_exception
    for tqdm_cls in [None, tqdm_auto, _test_exception]:
        # success
        list(product(range(2), repeat=2, tqdm_class=tqdm_cls))
        # success (iterable)
        list(product([list(range(2)), list(range(2))], tqdm_class=tqdm_cls))
        # failure (non-iterable)
        try:
            list(product(3, tqdm_class=tqdm_cls))
        except Exception:
            pass
        else:
            raise ValueError("should fail!")

# Generated at 2022-06-14 13:13:16.042983
# Unit test for function product
def test_product():
    """Test for `tqdm.itertools.product`"""
    for _ in product([1, 2, 3]):
        pass
    for _ in product([1, 2, 3], [4, 5, 6]):
        pass
    for _ in product([1, 2, 3], [4, 5, 6], [7, 8, 9]):
        pass

# Generated at 2022-06-14 13:13:22.725450
# Unit test for function product
def test_product():
    """ Test for function product """
    for _ in product([4, 5], [6, 7], tqdm_class=tqdm_auto):
        pass
    for _ in product([4, 5], [6], tqdm_class=tqdm_auto):
        pass
    for _ in product([4, 5], [], tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:13:31.995581
# Unit test for function product
def test_product():
    from numpy.random import randint
    from numpy.testing import assert_raises
    from numpy import prod, array
    for iterables in [randint(1, 5, (3, 5)), randint(1, 7, (5, 3)),
                      randint(1, 9, (2, 3, 2, 3))]:
        res = list(prod(iterables, 0))
        res_prod = prod([len(x) for x in iterables])
        res_tqdm = list(product(*iterables, tqdm_class=None))
        print(res)
        print(res_tqdm)
        print(len(res_tqdm))
        print(res_prod)
        assert ((len(res) == res_prod) and (res == res_tqdm))
   

# Generated at 2022-06-14 13:13:37.403293
# Unit test for function product
def test_product():
    assert list(product(["a", "b", "c"], repeat=2)) == [("a", "b"), ("a", "c"), ("b", "c")]
    assert list(product(["a", "b"], ["1", "2"], tqdm_class=None)) == [("a", "1"), ("a", "2"), ("b", "1"), ("b", "2")]

# Generated at 2022-06-14 13:13:47.788637
# Unit test for function product
def test_product():
    """
    Unit test for function product.

    Returns
    -------
    True if tests pass.

    Raises
    ------
    AssertionError
        If any test fails.
    """
    from random import shuffle
    from ..utils import _range
    from .tests import _check_iterable_progress

    _it = iter(product(_range(1, 2), _range(1, 4, 2)))
    _it2 = iter(product(tqdm_auto(), _range(1, 2), _range(1, 4, 2)))
    _it3 = iter(product(_range(1, 2), _range(1, 4, 2), tqdm_auto()))

    # The order of the iterables matters (the first iterable is
    # responsible for the number of iterations, so the tqdm object
    # must be the

# Generated at 2022-06-14 13:13:55.823448
# Unit test for function product
def test_product():
    import collections
    import operator
    import subprocess
    from .utils import format_sizeof

    cntlist = [10, 3, 5]
    n = reduce(operator.mul, cntlist, 1)
    for cnt in cntlist:
        assert len(list(product(range(cnt)))) == cnt

    # Taken from https://docs.python.org/2/library/itertools.html
    def chain(*iterables):
        # chain('ABC', 'DEF') --> A B C D E F
        for it in iterables:
            for element in it:
                yield element


# Generated at 2022-06-14 13:14:05.028063
# Unit test for function product
def test_product():
    from operator import mul
    from functools import reduce
    from ..utils import FormatCustomTextExt
    from .monitor import new_total
    from .tests.test_itertools import itertools_test_products

    _product = itertools.product
    iterables = (range(3), range(3), range(3))

    assert list(product(*iterables)) == list(_product(*iterables))
    assert list(product(*iterables, tqdm_class=FormatCustomTextExt)) == \
        list(_product(*iterables))


# Generated at 2022-06-14 13:14:14.367073
# Unit test for function product
def test_product():
    from .utils import FormatTestCounter

    assert list(product(range(5), repeat=2,
                        tqdm_class=FormatTestCounter,
                        tqdm_kwargs={"ascii": True})) == list(itertools.product(
                            range(5), repeat=2))

    try:
        import numpy as np
        nums = np.linspace(0, 1, 5)
        assert (list(product(nums, nums,
                             tqdm_class=FormatTestCounter,
                             tqdm_kwargs={"ascii": True})) ==
                list(itertools.product(nums, nums)))
    except ImportError:
        pass

# Generated at 2022-06-14 13:14:18.518064
# Unit test for function product
def test_product():
    try:
        itertools.product([], [])  # Python 2
    except TypeError:
        pass
    else:
        try:
            from ..std import product
            assert list(product((0, 1), (0, 1))) == list(itertools.product((0, 1), (0, 1)))
        except ImportError:
            pass

# Generated at 2022-06-14 13:14:27.429162
# Unit test for function product
def test_product():
    """
    Test function product.
    """
    import numpy as np
    import operator

    expected = np.array([[1, 1],
                         [1, 2],
                         [1, 3],
                         [2, 1],
                         [2, 2],
                         [2, 3]])
    actual = tqdm_auto(list(product(range(2), range(3))), total=6)
    np.testing.assert_array_equal(actual, expected)


# Generated at 2022-06-14 13:14:30.909133
# Unit test for function product
def test_product():
    expected_data = [
        (0, 0), (0, 1), (1, 0), (1, 1)
    ]
    data = list(product(range(2), range(2), tqdm_class=tqdm_auto))
    assert data == expected_data

# Generated at 2022-06-14 13:14:36.901888
# Unit test for function product
def test_product():
    """Test for product"""
    from ..utils import format_sizeof

    iterables = [[9, 2, 1], [1, 2, 3], [1, 1, 2]]
    total = 1
    for i in map(len, iterables):
        total *= i
    with tqdm_auto(total=total, unit="product", unit_scale=True) as t:
        for i in product(*iterables):
            t.update()
    print(format_sizeof(iterables))
    print(format_sizeof(product(*iterables)))
    assert True

# Generated at 2022-06-14 13:14:46.059617
# Unit test for function product
def test_product():
    """ Test function product
    """
    iterable = product([1, 2], repeat=2, tqdm_class=tqdm_auto)
    assert iterable.__next__() == (1, 1)
    assert iterable.__next__() == (1, 2)
    assert iterable.__next__() == (2, 1)
    assert iterable.__next__() == (2, 2)
    try:
        iterable.__next__()
    except StopIteration:
        pass
    else:
        raise AssertionError("iterator should be consumed")
    try:
        iterable.__next__()
    except StopIteration:
        pass
    else:
        raise AssertionError("iterator should be consumed")

# Generated at 2022-06-14 13:14:53.933880
# Unit test for function product
def test_product():
    a = [0, 1, 2]
    b = [10, 20]
    n = len(a) * len(b)
    assert n == 6
    p = product(a, b)
    assert list(p) == [(0, 10), (0, 20), (1, 10), (1, 20), (2, 10), (2, 20)]

    p = product(a, b, total=None)
    assert list(p) == [(0, 10), (0, 20), (1, 10), (1, 20), (2, 10), (2, 20)]

    p = product(a, b, total=n)
    assert list(p) == [(0, 10), (0, 20), (1, 10), (1, 20), (2, 10), (2, 20)]

# Generated at 2022-06-14 13:14:59.920190
# Unit test for function product
def test_product():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    from ..std import StringIO

    with StringIO() as f:
        with patch('sys.stderr', f):
            for _ in product(range(10), range(100)):
                pass


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:15:07.369504
# Unit test for function product
def test_product():
    """Test function `product`"""
    # pylint: disable=protected-access,missing-docstring
    import sys
    import random
    if sys.version_info[:2] < (2, 7):
        return None
    from numpy.random import randint
    from numpy.testing import assert_array_equal
    from .utils import _range
    from .std import _product
    from .gui import _product

    for size in _range(3):
        for i in _range(100):
            iterables = tuple(randint(2, 5, size=(size,)))

# Generated at 2022-06-14 13:15:17.112344
# Unit test for function product
def test_product():
    """Unit test for function product"""

# Generated at 2022-06-14 13:15:28.036186
# Unit test for function product
def test_product():
    """
    `test_product`: Test that `itertools.product`
    behaves like `tqdm.itertools.product (CI test)
    """
    # Copied from https://github.com/tqdm/tqdm/commit/dbcb2e2
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['e', 'f', 'g', 'h']
    list3 = ['i', 'j', 'k', 'l']

    for prod in itertools.product(list1, list2, list3):
        pass
    for prod in product(list1, list2, list3):
        pass

    for prod in product(list1, list2, list3):
        pass

# Generated at 2022-06-14 13:15:35.596494
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    a = list(range(5))
    b = list(range(5))
    c = list(range(5))
    d = list(zip(
        product(a, b, c, tqdm_class=tqdm_auto),
        itertools.product(a, b, c)))
    for i in d:
        assert (i[0] == i[1])

# Generated at 2022-06-14 13:15:38.020630
# Unit test for function product
def test_product():
    """Test `tqdm.itertools.product()`"""
    from tqdm.tests import tests
    tests.test_product(product)()

# Generated at 2022-06-14 13:15:46.917494
# Unit test for function product
def test_product():
    """
    Test for `tqdm.iterables.product`
    """
    from .tests import pretest_posttest
    from .tester import iterable_eq

    test_inputs = [
        (range(3), range(3), range(3)),
        ([], range(3), range(3)),
        (range(1), range(1), range(1)),
        (range(10), range(20), range(30)),
        (range(1000), range(500), range(200))]
    test_answers = [tuple(itertools.product(*i)) for i in test_inputs]

    pretest_posttest(test_inputs, list(test_answers), product)

    for inp_answ in zip(test_inputs, test_answers):
        iterable

# Generated at 2022-06-14 13:15:48.905920
# Unit test for function product
def test_product():
    """Unit test for product"""
    for i in product([1, 2, 3]):
        pass

# Generated at 2022-06-14 13:15:58.692642
# Unit test for function product
def test_product():
    """Unit test for function product"""
    assert list(product('ABCD', 'xy', tqdm_class=tqdm_auto, total=8)) == \
        [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'),
         ('C', 'y'), ('D', 'x'), ('D', 'y')]
    assert (
        list(product(
            range(2), repeat=3, tqdm_class=tqdm_auto, total=8)) ==
        [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0),
         (1, 0, 1), (1, 1, 0), (1, 1, 1)])

# Generated at 2022-06-14 13:16:09.374400
# Unit test for function product
def test_product():
    import sys
    with tqdm_auto(range(6), file=sys.stdout) as t:
        for i, j in product(range(100), range(100),
                            tqdm_class=tqdm_auto, total=10**6):
            pass
    with tqdm_auto(range(6), file=sys.stdout) as t:
        for i, j in product(range(100), range(100),
                            tqdm_class=tqdm_auto, total=10**6):
            pass
    with tqdm_auto(range(6), file=sys.stdout) as t:
        for i, j in product(range(100), range(100),
                            tqdm_class=tqdm_auto, total=10**6):
            pass
    # Unit

# Generated at 2022-06-14 13:16:22.714964
# Unit test for function product
def test_product():
    """Unit test for function product"""
    assert list(product([])) == []
    assert list(product([0])) == [(0,)]
    assert list(product([1, 2])) == [(1,), (2,)]
    assert list(product([0], [0])) == [(0, 0)]
    assert list(product([1, 2], [3, 4])) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert list(product([1, 2], [3, 4], [5, 6])) == \
        [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6),
         (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

# Generated at 2022-06-14 13:16:32.238775
# Unit test for function product
def test_product():
    for tqdm in [tqdm_auto, None]:
        assert ([i for i in product(range(5), tqdm_class=tqdm)]
                == list(itertools.product(range(5))))
        assert ([i for i in product(range(5), range(5), tqdm_class=tqdm)]
                == list(itertools.product(range(5), range(5))))
        assert ([i for i in product(range(5), range(5), range(5), tqdm_class=tqdm)]
                == list(itertools.product(range(5), range(5), range(5))))

# Generated at 2022-06-14 13:16:34.573043
# Unit test for function product
def test_product():
    '''Test for function product'''
    a = product([1, 2], [3, 4])
    b = [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert(list(a) == b)

# Generated at 2022-06-14 13:16:44.751323
# Unit test for function product
def test_product():
    import re
    import inspect
    from contextlib import redirect_stdout
    from io import StringIO
    from .utils import _range

    test_iterables = [[1, 2], [3, 4], [5]]

    # Verify manual tqdm
    f = StringIO()
    with redirect_stdout(f):
        for _ in tqdm_auto(product(*test_iterables),
                           leave=False):
            pass
    captured = f.getvalue()
    assert re.sub(r'\s+', '', captured).rstrip() == \
        "|#####-----|0/6[00:00<?,?]"

    # Verify tqdm as context manager
    f = StringIO()

# Generated at 2022-06-14 13:16:51.348690
# Unit test for function product
def test_product():
    for iter1 in (list(range(16)), range(16)):
        for iter2 in (list(range(16)), range(16)):
            for iterable_len in (None, 'auto', 16 * 16):
                for ascii in (True, False):
                    s = ''
                    for i in product(iter1, iter2, ascii=ascii, desc='testing', total=iterable_len):
                        s += '%d,%d\n' % i
                    assert s == ''.join('%d,%d\n' % i for i in itertools.product(iter1, iter2))

# Generated at 2022-06-14 13:16:59.153471
# Unit test for function product
def test_product():
    import numpy as np
    from ..utils import format_sizeof
    from ..contrib.concurrency import thread_map
    from ..contrib.concurrency import multiprocessing
    from ..auto import tqdm

    total = 0

    def test_it(total):
        # actual calculation function
        def calc():
            # totals around 100^100 memory
            return np.prod([np.arange(99, dtype=np.int64)
                            for _ in range(100)])
        pbar = tqdm(total=total)
        for chunk in product(range(total // 10), tqdm_kwargs={"total": total}):
            # wait for the number of iterations to be updated
            for i in range(10):
                pbar.update()
            # do nothing
            pass
        pbar

# Generated at 2022-06-14 13:17:10.235083
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from .tests_class import CommonTestCases

    CommonTestCases.test_class(tqdm_class=tqdm_auto, total=None)
    CommonTestCases.test_class(tqdm_class=tqdm_auto, total=7)

    # Test product(..., total=None)
    CommonTestCases.test_class(tqdm_class=tqdm_auto, total=None,
                               func=product,
                               islice_start=None,
                               args=([1, 2, 3], [4, 5])
                               )

# Generated at 2022-06-14 13:17:17.873263
# Unit test for function product
def test_product():
    """Examples from python documentation"""
    import math  # NOQA
    R = range
    assert list(product(R(3), repeat=2)) == list(product(R(3), R(3)))  # NOQA
    assert list(product(R(2), repeat=3)) == list(product(R(2), R(2), R(2)))  # NOQA
    assert list(product(R(2), repeat=1)) == list(product(R(2),))  # NOQA

    A = [1, 2, 3]
    B = [4, 5]
    assert list(product(A, B)) == [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]  # NOQA


# Generated at 2022-06-14 13:17:27.852908
# Unit test for function product
def test_product():
    from tqdm import tqdm
    from .tests_tqdm import with_setup, pretest_posttest

    def test_product_basic():
        """
        Test that simple product is ok
        """
        with tqdm(total=1) as t:
            for _ in product([1, 2], [3, 4]):
                t.update()

    @with_setup(pretest=pretest_posttest)
    def test_product_len_prog():
        """
        Test that len is ok
        """
        with tqdm(total=1, ncols=100) as t:
            for _ in product([1, 2], [3, 4]):
                t.update()


# Generated at 2022-06-14 13:17:35.966432
# Unit test for function product
def test_product():
    """
    UnitTest for function product
    """
    from numpy import product as nproduct

    for _ in product(range(30), repeat=4):
        pass

    for _ in product(range(30), range(30), total=40):
        pass

    for _ in product(range(30), range(30), range(30),
                     total=40, tqdm_class=tqdm_auto):
        pass

    assert sum(1 for _ in product(range(10), range(10))) == nproduct([10, 10])
    try:
        assert sum(1 for _ in product(range(10), repeat=1)) == \
            nproduct(10, repeat=1)
    except TypeError:
        pass
    assert sum(1 for _ in product(range(10), repeat=2)) == \
        nproduct

# Generated at 2022-06-14 13:17:44.362896
# Unit test for function product
def test_product():
    from .utils import TestCase

    class TestProduct(TestCase):
        def test_product(self):
            from random import randint

            def rand_list(max_list_len):
                list_len = randint(0, max_list_len)
                return list(range(list_len))

            # test empty iterables
            p1 = list(product([], [], tqdm_class=tqdm_auto))
            self.assertEqual(p1, [])

            # test single iterable
            p1 = list(product([1, 2, 3], tqdm_class=tqdm_auto))
            self.assertEqual(p1, [(1,), (2,), (3,)])

            # test product of two ranges

# Generated at 2022-06-14 13:17:53.201429
# Unit test for function product
def test_product():
    from collections import Counter
    for k in range(4):
        for j in range(4):
            c = Counter()
            for i in product(range(k), range(j), tqdm_class=tqdm_auto.tqdm):
                c[i] += 1
            assert c == Counter(itertools.product(range(k), range(j)))
            # Test with `total` keyword argument to check its compatibility
            c = Counter()
            for i in product(range(k), range(j), total=k * j):
                c[i] += 1
            assert c == Counter(itertools.product(range(k), range(j)))

# Generated at 2022-06-14 13:17:59.398549
# Unit test for function product
def test_product():
    """
    Unit test for `itertools.product` function

    Make sure it works on all versions of `itertools`
    """
    # itertools.product is not re-exportable
    import itertools

    x = list(range(10))
    y = list(range(20))
    z = list(range(30))
    prod = list(itertools.product(x, y, z))
    prod2 = list(product(x, y, z))
    assert len(prod) == 6000
    assert len(prod2) == 6000
    assert prod == prod2

# Generated at 2022-06-14 13:18:04.880010
# Unit test for function product
def test_product():
    from .tests_tqdm import with_unit_option

    p = list(product(range(10), ['hello', 'world'], tqdm_class=tqdm_auto))
    assert (p == [(0, 'hello'), (0, 'world'), (1, 'hello'), (1, 'world'),
                  (2, 'hello'), (2, 'world'), (3, 'hello'), (3, 'world'),
                  (4, 'hello'), (4, 'world'), (5, 'hello'), (5, 'world'),
                  (6, 'hello'), (6, 'world'), (7, 'hello'), (7, 'world'),
                  (8, 'hello'), (8, 'world'), (9, 'hello'), (9, 'world')])


# Generated at 2022-06-14 13:18:15.843092
# Unit test for function product
def test_product():
    import random
    import string
    import sys
    import threading
    import time

    def random_string_generator(min_chars=0, max_chars=8192):
        chars = string.ascii_uppercase + string.digits
        while True:
            yield "".join(random.choice(chars)
                          for _ in range(random.randrange(min_chars,
                                                          max_chars)))

    # Generators
    rand_ints = (random.randint(0, sys.maxsize) for _ in itertools.count())
    rand_strings = random_string_generator()

    # List of generators
    iterables_list = [rand_ints, rand_strings]

    # Number of itertools.product calls
    num_products = 10

    #

# Generated at 2022-06-14 13:18:23.974064
# Unit test for function product
def test_product():
    "Tests function product"
    assert (list(product(range(3), repeat=2))
            == list(itertools.product(range(3), repeat=2)))


# try:
#     from itertools import product  # NOQA
#     __all__ = []
# except ImportError:
#     _product = product  # NOQA

    # def product(*iterables, **tqdm_kwargs):
    #     """
    #     Equivalent of `itertools.product`.
    #     """
    #     def _product(*iterables):
    #         """
    #         This function is the equivalent of itertools.product
    #         It is called recursively to implement the product.
    #         To avoid recursion limit issues,
    #         a recursive call will not exceed 1000 calls deep.

# Generated at 2022-06-14 13:18:27.723190
# Unit test for function product
def test_product():
    """Tests for `product`"""
    in_a = ['a', 'b', 'c']
    in_b = ['x', 'y', 'z']
    for i, j in product(in_a, in_b):
        print(i, j)

# Generated at 2022-06-14 13:18:35.098597
# Unit test for function product
def test_product():
    "Test product"
    from ..pandas import tqdm_pandas, tqdm_gui
    from .tests import tqdm_tests as tt

    # Test as an iterator
    assert tt.test_iterator(tqdm_auto(product, total=5), 5,
                            rampup=False, leave=False) == 5
    # Test as a container
    assert tt.test_container(tqdm_auto(product, total=7), 7) == 7
    assert tt.test_len(lambda: tqdm_auto(product, total=7)) == 7
    # Test as a generator
    assert tt.test_generator(tqdm_auto(product, total=9), 9, leave=False) == 9
    # Test as a context manager
    assert tt.test_context

# Generated at 2022-06-14 13:18:38.752420
# Unit test for function product
def test_product():
    total = 0
    for i in product(*[list('abc')] * 2,
                     tqdm_class=tqdm_auto,
                     desc="Description"):
        total += 1

    assert total == 9

# Generated at 2022-06-14 13:18:47.679596
# Unit test for function product
def test_product():
    def f(x, y):
        assert x + y == 10
        return x * y

    for _ in product([1, 2, 3], [5, 3, 2], tqdm_class=None):
        pass
    for _ in product([1, 2, 3], [5, 3, 2], tqdm_class=tqdm_auto):
        pass

    assert sum(
        f(*x) for x in product([1, 2, 3], [5, 3, 2], tqdm_class=None)) == 32
    assert sum(
        f(*x) for x in product([1, 2, 3], [5, 3, 2], tqdm_class=tqdm_auto)) == 32

# Generated at 2022-06-14 13:20:19.115957
# Unit test for function product
def test_product():
    from .utils import FormatWrapBase
    from .utils import format_meter
    from .utils import format_sizeunit
    from .utils import format_time
    from .utils import format_speed
    from .utils import format_number

    class Dummy(FormatWrapBase):
        def __init__(self):
            super(Dummy, self).__init__()
            self.x = 0

        def update(self, n=1):
            self.x += n
            super(Dummy, self).update(n)

    # test dummy
    dummy = Dummy()
    assert dummy.n == 0
    dummy.update()
    assert dummy.n == 1
    dummy.update(3)
    assert dummy.n == 4

    # test format_meter

# Generated at 2022-06-14 13:20:28.608191
# Unit test for function product
def test_product():
    import numpy as np

    def prod(iterable):
        p = 1
        for n in iterable:
            p *= n
        return p

    for n, nb_iters in [(2, 3), (6, 2), (10, 1), (0, 3)]:
        p = prod(range(n))
        assert p == np.prod(range(n))
        assert p == np.prod([x for x in product(range(n))])
        assert p == np.prod([x for x in product(range(n), tqdm_class=None)])
        assert p == np.prod([x for x in product(range(n), total=nb_iters)])

    # testing the combination of total and iterable

# Generated at 2022-06-14 13:20:34.577726
# Unit test for function product
def test_product():
    for tqdm_class in [None, tqdm_auto]:
        for kwargs in [dict(), dict(tqdm_class=tqdm_class)]:
            for iterables in [['asdf', 'fds'], []]:
                assert list(product(*iterables, **kwargs)) == \
                       list(itertools.product(*iterables))

# Generated at 2022-06-14 13:20:36.979652
# Unit test for function product
def test_product():
    from ..tqdm_gui import tqdm
    list(product(range(10), range(3), tqdm_class=tqdm))


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:20:43.525385
# Unit test for function product
def test_product():
    import numpy
    from ..std import numpy as tqdm_numpy

    a = list(range(5 ** 4))
    b = list(range(5 ** 4))
    for p, p_tqdm in zip(
            product(a, b, tqdm_class=tqdm_numpy),
            product(a, b, tqdm_class=tqdm_numpy)):
        numpy.testing.assert_equal(p, p_tqdm)

# Generated at 2022-06-14 13:20:46.258726
# Unit test for function product
def test_product():
    """
    Unit test for `tqdm.itertools.product`.
    """
    val = 0
    for i in product(range(5), range(5), range(5),
                     tqdm_class=tqdm_auto,
                     desc='test_product'):
        val += i[0]
    assert val == 20 * 19 / 2 * 3 * 4

# Generated at 2022-06-14 13:20:48.645524
# Unit test for function product
def test_product():
    a = list(range(3))
    b = list(range(2))
    c = list(range(1))

    p1 = itertools.product(a, b, c)
    p2 = product(a, b, c)

    assert (list(p1) == list(p2))

# Generated at 2022-06-14 13:20:59.699601
# Unit test for function product
def test_product():
    from ._utils import compare_product, TestWarnings
    from tqdm import tqdm, trange
    from .utils import FormatStall

# Generated at 2022-06-14 13:21:06.050841
# Unit test for function product
def test_product():
    iterables = [range(1000), range(100000), range(10)]

    # Test normal
    p = product(*iterables)
    try:
        i = None
        for i in p:
            assert tuple(i[i]) == tuple(i)
        total = sum(i for i in map(len, iterables))
    except AssertionError:
        # Test tqdm progress bar
        p = product(*iterables, tqdm_class=tqdm_auto)
        total = None
        for i in p:
            assert tuple(i[i]) == tuple(i)

    # Assert function returns same results as itertools
    assert list(p) == list(itertools.product(*iterables))

# Generated at 2022-06-14 13:21:15.740670
# Unit test for function product
def test_product():
    # Smoke test, same as itertools.product
    assert list(product([], repeat=3)) == []
    assert list(product([], repeat=3)) == list(itertools.product([], repeat=3))
    assert list(product([1, 2], [3, 4])) == list(itertools.product([1, 2], [3, 4]))
    assert list(product([1, 2], [3, 4], [5, 6])) == list(itertools.product([1, 2], [3, 4], [5, 6]))
    assert list(product(["A", "B"], repeat=4)) == list(itertools.product(["A", "B"], repeat=4))
    # Function of the same name, unlike itertools.product