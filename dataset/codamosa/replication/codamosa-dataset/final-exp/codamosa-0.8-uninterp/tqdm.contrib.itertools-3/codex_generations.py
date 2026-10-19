

# Generated at 2022-06-14 13:12:41.477616
# Unit test for function product
def test_product():
    r = product(range(30), range(20), range(10))
    assert (len(list(r)) == 30 * 20 * 10)
    assert (len(list(r)) == 0)


if __name__ == "__main__":
    import nose
    nose.runmodule(argv=[__file__, '-vvs', '-x', '--pdb', '--pdb-failure'],
                   exit=False)

# Generated at 2022-06-14 13:12:45.241695
# Unit test for function product
def test_product():
    """Unit test for function product"""
    it = product(range(10), range(20, 30), range(1, 7))
    assert list(it) == list(itertools.product(range(10),
                                              range(20, 30),
                                              range(1, 7)))

# Generated at 2022-06-14 13:12:54.516281
# Unit test for function product

# Generated at 2022-06-14 13:13:01.889317
# Unit test for function product
def test_product():
    from ..utils import format_sizeof
    from ..utils import format_interval as format_time
    import time
    import os
    t = time.time()
    for i in product(range(10000), range(10000)):
        pass
    with open(os.devnull, 'w') as devnull:
        print(format_time(time.time() - t), file=devnull)
        # print(format_sizeof(memory_usage()), file=devnull)

# Generated at 2022-06-14 13:13:13.332198
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from .tests_tqdm_w_len import mp_map
    from .tests_tqdm import closing, presence

    def checker(a, b, c):
        """Check if a == b, yield a for c"""
        assert a == b
        return a

    # 1-d
    presence(range, 1)
    presence(range, 3)

    # 2-d
    a = product(range(3), range(4), tqdm_class=tqdm_auto)
    presence(a, 12)
    presence(lambda: list(a), 12)

    b = product(range(3), range(4))
    presence(b, 12)
    presence(lambda: list(b), 12)

    # 2-d with length

# Generated at 2022-06-14 13:13:17.295816
# Unit test for function product
def test_product():
    # Complete coverage
    itertools.product([1, 2], repeat=2)
    itertools.product([1, 2], repeat=4)

    for i in product([1, 2], repeat=4):
        pass
    for i in product([1, 2], repeat=4, tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:13:29.511787
# Unit test for function product
def test_product():
    """Unit test for itertools.product (and tqdm.itertools.product)"""
    from ..__init__ import tqdm
    from random import shuffle, seed

    # Test inner-loop evaluation
    for length in [0, 1, 2, 10]:  #, 100, 1e3, 1e4, 1e5, 1e6]:
        seed(length)
        f = list(range(length))
        b = list(tqdm.itertools.product(f, repeat=3))
        shuffle(b)
        for _ in tqdm.itertools.product(f, repeat=3):
            a = b.pop()
            assert a == _
        assert len(b) == 0
        
        # Test total=evaluation

# Generated at 2022-06-14 13:13:36.693418
# Unit test for function product
def test_product():
    """
    Simple unit test for tqdm(itertools.product)
    """
    from .utils import FormatTelegram

    assert list(product([2, 3], [5, 7])) == list(itertools.product([2, 3], [5, 7]))

    actual = list(product([2, 3], [5, 7], tqdm_class=FormatTelegram))
    assert actual == list(itertools.product([2, 3], [5, 7]))

# Generated at 2022-06-14 13:13:46.357855
# Unit test for function product
def test_product():
    import numpy as np
    from ..std import product as tqdm_product
    from random import random, seed
    # Test 1 (number of updates)
    seed(10)
    for i in range(2, 16):
        for _ in tqdm_product(range(i), range(i), range(i),
                              tqdm_class=tqdm_auto.tqdm, leave=False):
            pass
        for _ in tqdm_product(iter(lambda: random(), ''), repeat=i,
                              tqdm_class=tqdm_auto.tqdm, leave=False):
            pass

    # Test 2 (values)

# Generated at 2022-06-14 13:13:51.562894
# Unit test for function product
def test_product():
    """Equivalent of `itertools.product`."""
    iterables = [["a", "b"], [1, 2]]
    res = set(map(lambda x: "".join(map(str, x)), itertools.product(*iterables)))
    assert res == set(product(*iterables, tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:14:03.385690
# Unit test for function product
def test_product():
    import numpy as np
    from numpy.testing import assert_array_equal

    # Test product_kwargs
    product_kwargs = {
        "a": range(3),
        "b": "abcd",
        "c": np.arange(6).reshape((3, 2))}
    assert_array_equal(
        list(product(**product_kwargs)),
        list(itertools.product(**product_kwargs)))

    # Test product_iterables
    product_iterables = (range(3), "abcd", np.arange(6).reshape((3, 2)))
    assert_array_equal(
        list(product(*product_iterables)),
        list(itertools.product(*product_iterables)))

    # Test product_args

# Generated at 2022-06-14 13:14:13.906054
# Unit test for function product
def test_product():
    from numpy import random
    import numpy as np
    import math

    # Create random string arrays
    def randomword(length):
        s = ''
        for i in range(length):
            # Generate a random ASCII number
            s += chr(random.randint(33, 126))
        return s

    u = []
    for i in range(10):
        u.append(randomword(random.randint(1, 10)))

    u = np.array(u)
    tu = tqdm_auto(u, external=True)

    # Create random number arrays
    v = []
    for i in range(10):
        v.append(random.randint(0, 10))

    v = np.array(v)
    tv = tqdm_auto(v, external=True)

    # Create

# Generated at 2022-06-14 13:14:16.012299
# Unit test for function product
def test_product():
    with tqdm_auto(product(range(5), range(5))) as p:
        for _ in p:
            pass

# Generated at 2022-06-14 13:14:21.999629
# Unit test for function product
def test_product():
    """ Test for function product """
    TEST_PRODUCT = product(range(10), range(10), range(10), range(10),
                           tqdm_class=None)
    TEST_PRODUCT_LIST = list(TEST_PRODUCT)
    assert (len(TEST_PRODUCT_LIST) == 10000)
    for i, j in zip(
            TEST_PRODUCT,
            list(itertools.product(range(10), range(10), range(10), range(10)))
    ):
        assert (i == j)

# Generated at 2022-06-14 13:14:22.796443
# Unit test for function product
def test_product():
    assert list(product(range(10), range(50), range(70)))

# Generated at 2022-06-14 13:14:29.327017
# Unit test for function product
def test_product():
    """Unit tests"""
    try:
        from ...tests.test_tqdm import pretest_posttest
        pretest_posttest()
    except (ImportError, TypeError):
        pass
    else:
        from nose.tools import assert_raises

        with assert_raises(ValueError):
            product("abc", "def")
        with assert_raises(ValueError):
            product("abc", [1, 2, 3])
        it = product()
        assert next(it) == ()
        with assert_raises(StopIteration):
            next(it)
        it = product("abc", "def")
        assert next(it) == ('a', 'd')
        assert next(it) == ('a', 'e')
        assert next(it) == ('b', 'd')
        assert next(it)

# Generated at 2022-06-14 13:14:35.331830
# Unit test for function product
def test_product():
    """
    Test of `tqdm.itertools.product`
    """
    try:
        iter(tqdm_auto)
    except TypeError:
        # `tqdm_auto` is a function
        tqdm_class = tqdm_auto
    else:
        # `tqdm_auto` is a class
        tqdm_class = tqdm_auto()
    test = []
    for _ in product(range(3), 'ab', [0.0, 1.0], tqdm_class=tqdm_class):
        test.append(_)
    with tqdm_auto(total=18) as t:
        for i in itertools.product(range(3), 'ab', [0.0, 1.0]):
            t.update()

# Generated at 2022-06-14 13:14:45.067798
# Unit test for function product
def test_product():
    from .utils import has_subsequence
    from .utils import _range
    from .utils import format_sizeof

    for a, b, c in product(_range(90), _range(90), _range(90),
                           tqdm_class=tqdm_auto,
                           desc="test_product",
                           total=7290):
        pass
    # Check that the description is being properly overwritten
    for a, b, c in product(_range(90), _range(90), _range(90),
                           tqdm_class=tqdm_auto,
                           desc="test_product",
                           total=7290):
        break

# Generated at 2022-06-14 13:14:53.436824
# Unit test for function product
def test_product():
    import numpy as np
    from ..std import numpy as tqdm_numpy
    from ..std import pandas as tqdm_pandas

    # Standard usage
    iterables = [range(4), range(4), range(4), range(4)]
    assert (list(product(*iterables)) ==
            list(itertools.product(*iterables)))

    # Test tqdm_class kwarg
    iterables = [range(4), range(4), range(4), range(4)]
    assert (list(product(*iterables, tqdm_class=tqdm_pandas)) ==
            list(itertools.product(*iterables)))

    # Test total kwarg
    iterables = [range(4), range(4), range(4), range(4)]

# Generated at 2022-06-14 13:15:00.296763
# Unit test for function product
def test_product():
    """Test for :class:`tqdm.itertools`.

    Note:
        Must be run with ``--verbose`` flag for coverage report.
    """
    from tqdm import trange
    assert list(product(range(10), repeat=2)) == list(
        trange(100, leave=False))
    assert list(product(range(10), repeat=3)) == list(
        trange(1000, leave=False))
    assert list(product(range(10), repeat=4)) == list(
        trange(10000, leave=False))
    assert list(product(range(10), repeat=5)) == list(
        trange(100000, leave=False))
    assert list(product(range(10), repeat=6)) == list(
        trange(1000000, leave=False))
    assert list

# Generated at 2022-06-14 13:15:46.798549
# Unit test for function product
def test_product():
    """
    Test function `~tqdm.itertools.itertools.product`.
    """
    import numpy as np
    from .tests import pretest_posttest
    with pretest_posttest() as (pre, _):
        assert next(tqdm_auto(range(3), disable=pre)) == next(range(3))
        assert next(tqdm_auto(range(3), ascii=True, disable=pre)) == next(range(3))
    n = 3
    for a, b in zip(
            product(range(n), repeat=2),
            np.ndindex((n, n))):
        assert a == b
    for a, b in zip(
            product(range(1, 4), repeat=2),
            np.ndindex((3, 3))):
        assert a

# Generated at 2022-06-14 13:15:57.215157
# Unit test for function product
def test_product():
    from os import getpid
    from random import seed
    from .utils import FormatCustomText


# Generated at 2022-06-14 13:16:01.106364
# Unit test for function product
def test_product():
    with tqdm_auto(total=3, leave=False) as t:
        assert t.n == 0
        for i in product(range(3), repeat=2):
            t.update()
        assert t.n == 3


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:16:11.645462
# Unit test for function product
def test_product():
    """Test for function product"""
    import re
    from ..utils import _range
    from unittest import TestCase, main

    class TestProd(TestCase):
        def test_base(self):
            """Tests basic behaviour"""
            l = list(_range(10))
            res = list(product(l, repeat=2))
            self.assertEqual(len(res), len(l)**2)
            for i in res:
                self.assertEqual(len(i), 2)
                self.assertIn(i[0], l)
                self.assertIn(i[1], l)
            res = list(product("123", "456"))

# Generated at 2022-06-14 13:16:14.363048
# Unit test for function product
def test_product():
    """Simple test"""
    for n in product(range(1000), tqdm_class=tqdm_auto, desc="Euler"):
        pass

# Generated at 2022-06-14 13:16:24.825912
# Unit test for function product
def test_product():
    from random import random
    for product in [itertools.product, product]:
        for a, b in product([1, 2, 3], [4, 5]):
            assert all(isinstance(e, int)
                       for e in [a, b]), [a, b]
        assert list(product([], [], [1])) == []
        k = 0
        for i in product([], range(1000)):
            k += 1
        assert k == 1000
        k = 0
        for i in product(range(1000), []):
            k += 1
        assert k == 0
        k = 0
        for i in product([1, 2], [1, 2], [1, 2], [1, 2]):
            k += 1

# Generated at 2022-06-14 13:16:33.994070
# Unit test for function product
def test_product():
    """Unit test for function product"""
    import sys
    import numpy as np
    assert (np.array(list(product(range(4), repeat=0))) == []).all()
    assert (np.array(list(product(range(4), repeat=1)))
            == np.array([(0,), (1,), (2,), (3,)])).all()
    assert (np.array(list(product(range(1), repeat=2)))
            == np.array([(0, 0)])).all()
    assert (np.array(list(product(range(2), repeat=2)))
            == np.array([(0, 0), (0, 1), (1, 0), (1, 1)])).all()

# Generated at 2022-06-14 13:16:43.353416
# Unit test for function product
def test_product():
    """Test for product()"""
    for case, expected in [(
            (1, 2, 3),
            [(1, 2, 3)]
    ), (
            (1, 1),
            [(1, 1)]
    ), (
            (1, 2),
            [(1, 1), (1, 2)]
    ), (
            (1, 2, 3),
            [(1, 2, 1), (1, 2, 2), (1, 2, 3)]
    )]:
        assert list(product(*case)) == list(itertools.product(*case))
        assert list(product(*case, tqdm_class=tqdm_auto)) == expected

# Generated at 2022-06-14 13:16:49.731613
# Unit test for function product
def test_product():
    for tqdm_class in (tqdm_auto,):
        for data in [list(range(n)) for n in range(1, 5)]:
            for kwargs in [{"miniters": 0}, {"miniters": 1}, {"miniters": 2}]:
                for _ in product(*data, tqdm_class=tqdm_class, **kwargs):
                    pass
                for _ in product(*data, tqdm_class=tqdm_class, **kwargs):
                    pass
    assert tqdm_class._instances  # must be > 0

# Generated at 2022-06-14 13:16:56.438213
# Unit test for function product
def test_product():
    """
    Unit testing.
    """
    import sys
    import numpy as np

    if sys.version_info[0] == 3:
        import unittest
        import io as StringIO
        StringIO = StringIO.StringIO
    else:
        import StringIO
        import unittest2 as unittest

    class TestProduct(unittest.TestCase):
        def test_prod(self):
            with tqdm_auto(unit="it") as t:
                a = np.prod([i for i in t(range(1, 31))])
                self.assertEqual(a, 265252859812191058636308480000000)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestProduct)
    unittest.TextTestRunner(verbosity=2).run

# Generated at 2022-06-14 13:18:38.640812
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from numpy.random import randint

    def imap(a, b):
        for i, j in zip(a, b):
            assert i == j

    def my_product(n, m, tqdm_class=tqdm_auto):
        """Equivalent of `itertools.product` for n, m"""
        for i in product(range(n), range(m), tqdm_class=tqdm_class):
            assert i[0] < n
            assert i[1] < m
            yield i

    randint(0, 10, 20)
    imap(my_product(10, 20), itertools.product(range(10), range(20)))

# Generated at 2022-06-14 13:18:42.959953
# Unit test for function product
def test_product():
    from .pandas import pandas
    for x, y in product(range(4), range(4),
                        tqdm_class=tqdm_auto,
                        total=16):
        assert (x, y) == pandas(x, y)

# Generated at 2022-06-14 13:18:45.398858
# Unit test for function product
def test_product():
    import tqdm
    for i in tqdm.tqdm.product(range(10000), range(1000), tqdm_class=tqdm.tqdm):
        pass

# Generated at 2022-06-14 13:18:50.802685
# Unit test for function product
def test_product():
    """Test for function product"""
    for iter1 in [range(5), range(5), range(5)]:
        for iter2 in [range(5), range(5), range(5)]:
            for iter3 in [range(5), range(5), range(5)]:
                lst1 = list(product(iter1, iter2, iter3))
                lst2 = list(itertools.product(iter1, iter2, iter3))
                assert lst1 == lst2

# Generated at 2022-06-14 13:18:59.232684
# Unit test for function product
def test_product():
    from ..std import numpy as np
    from ..std import six as six
    assert list(product([1, 2, 3], ['a', 'b'])) == [
        (1, 'a'),
        (1, 'b'),
        (2, 'a'),
        (2, 'b'),
        (3, 'a'),
        (3, 'b')]
    assert list(product(['a', 'b'], [1, 2, 3])) == [
        ('a', 1),
        ('a', 2),
        ('a', 3),
        ('b', 1),
        ('b', 2),
        ('b', 3)]