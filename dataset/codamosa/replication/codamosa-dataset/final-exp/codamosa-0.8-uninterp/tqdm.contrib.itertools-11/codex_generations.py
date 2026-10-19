

# Generated at 2022-06-14 13:12:27.869615
# Unit test for function product
def test_product():
    """
    Unit test for the product function.

    Returns
    -------
    result  : [boolean]
        True, if unit test passes, else False.
    """
    from tqdm.contrib.concurrent import process_map
    import sys

    def unit_test(q, i, j):
        """
        Fold function for the unit test.

        Parameters
        ----------
        q   : [Queue object]
        i,j : [int]
         """
        q.put(i * j)

    q = process_map(unit_test, zip(product([1, 2], repeat=2),
                                   product([3, 4], repeat=2)))
    result = [q.get() for _ in range(4)]

# Generated at 2022-06-14 13:12:39.680841
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from . import trange
    from .utils import format_sizeof
    import time

    for _ in range(3):
        for klass in [tqdm_auto, trange]:
            with klass(10, smoothing=0) as t:
                for _ in product(
                        range(3),
                        range(3),
                        range(3),
                        range(3),
                        range(3),
                        range(3),
                        tqdm_class=klass):
                    t.update()
                    time.sleep(0.01)


# Generated at 2022-06-14 13:12:49.898284
# Unit test for function product
def test_product():
    import random
    import string
    import sys
    import time
    s = list(string.ascii_lowercase)
    l = [random.randint(0, 10) for i in range(len(s))]
    l2 = list(itertools.product(s, l))
    l3 = list(product(s, l))
    assert (l2 == l3), "product does not yield same results as itertools.product"
    for x in range(2, 10):
        l = [random.randint(0, 10) for i in range(len(s))]
        l2 = list(itertools.product(s, *l))
        l3 = list(product(s, *l))
        assert (l2 == l3), "product does not yield same results as itertools.product"

# Generated at 2022-06-14 13:13:01.936361
# Unit test for function product
def test_product():
    """Tests for `tqdm.itertools.product`"""
    product = tqdm_auto.itertools.product
    product_ = itertools.product
    assert list(product([1, 2, 3])) == list(product_([1, 2, 3]))
    assert list(product([1, 2, 3], [4, 5])) == list(product_([1, 2, 3], [4, 5]))
    assert list(product([1, 2, 3], repeat=1)) == list(product_([1, 2, 3], repeat=1))
    assert list(product([1, 2, 3], repeat=2)) == list(product_([1, 2, 3], repeat=2))

# Generated at 2022-06-14 13:13:13.377087
# Unit test for function product
def test_product():
    """
    Tests product
    """
    assert list(product("ABC", repeat=2)) == list(itertools.product("ABC", repeat=2))
    assert list(product("ABC", repeat=2)) == [("A", "A"), ("A", "B"), ("A", "C"),
                                              ("B", "A"), ("B", "B"), ("B", "C"),
                                              ("C", "A"), ("C", "B"), ("C", "C")]
    assert list(product("ABC", "DEF", repeat=2)) == list(itertools.product("ABC", "DEF", repeat=2))

# Generated at 2022-06-14 13:13:20.908949
# Unit test for function product
def test_product():
    """Test `product`."""
    from ..utils import FormatCustomText
    with FormatCustomText(desc='task'):
        for i in product('ABC', 'DEF', tqdm_class=tqdm_auto):
            pass
        for i in product('ABC', 'DEF', tqdm_class=tqdm_auto,
                         bar_format='{desc}: {percentage:3.0f}%|{bar}| '):
            pass
        for i in product('ABC', 'DEF', tqdm_class=tqdm_auto,
                         bar_format='{desc}: {percentage:3.0f}%|{bar}|, {n_fmt}/{total_fmt}'):
            pass

# Generated at 2022-06-14 13:13:31.216366
# Unit test for function product
def test_product():
    result = list(product(range(5), repeat=2, tqdm_class=tqdm_auto))
    assert result == list(itertools.product(range(5), repeat=2))

    def product_range(n):
        return list(product(range(n), repeat=2, tqdm_class=tqdm_auto))

    assert product_range(0) == []
    assert product_range(1) == []
    assert product_range(2) == [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert product_range(3) == [(0, 0), (0, 1), (0, 2),
                                (1, 0), (1, 1), (1, 2),
                                (2, 0), (2, 1), (2, 2)]
   

# Generated at 2022-06-14 13:13:34.119907
# Unit test for function product
def test_product():
    for i in product(['a', 'b', 'c'], [1, 2]):
        pass
    assert i == ('c', 2)

# Generated at 2022-06-14 13:13:42.069188
# Unit test for function product
def test_product():
    # test empty case
    assert list(product()) == [()]  # yields tuple
    assert list(product([])) == [()]  # yields tuple
    assert list(product([], [])) == [()]  # yields tuple

    # test non-empty case
    assert list(product([1, 2, 3])) == [(1,), (2,), (3,)]  # yields tuple
    assert list(product([1, 2, 3], repeat=1)) == [(1,), (2,), (3,)]  # yields tuple
    assert list(product([1, 2, 3], repeat=2)) == [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]  # yields tuple
    assert list

# Generated at 2022-06-14 13:13:53.593362
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    import numpy as np
    # Ensure product of 3 lists of 2, 3, and 4 elements
    res = list(product([0, 1], [0, 1, 2], [0, 1, 2, 3],
                       tqdm_class=tqdm_auto))
    assert len(res) == 24
    assert isinstance(res[11], tuple)
    assert res[11] == (1, 1, 2)
    # Ensure product of 3 iterators
    res = list(product(range(2), range(3), range(4),
                       tqdm_class=tqdm_auto))
    assert len(res) == 24
    assert isinstance(res[11], tuple)
    assert res[11] == (1, 1, 2)
    # Ensure product

# Generated at 2022-06-14 13:13:58.827978
# Unit test for function product
def test_product():
    """Run function product and compare result with itertools.product"""
    for input in [[range(0, 20, 2)] * 10]:
        assert list(product(*input)) == list(itertools.product(*input))
        assert list(product(*input, total=10)) == list(itertools.product(*input))

# Generated at 2022-06-14 13:14:09.405145
# Unit test for function product
def test_product():
    import sys
    import random

    # Create a product with a random range length
    rlen = random.randint(1, 10)
    in_args = []
    ranges = []
    for _ in range(rlen):
        rlen = random.randint(1, 10)
        ranges.append(rlen)
        i = range(rlen)
        in_args.append(i)

    # Create product, and check number of iterations
    t = 0
    for i in product(*in_args, tqdm_class=lambda x, total=None: x):
        t += 1

# Generated at 2022-06-14 13:14:18.239037
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    listproduct = list(product(range(4), repeat=3))
    assert len(listproduct) == 4 ** 3
    assert list(product(range(4), repeat=3, tqdm_class=None)) == listproduct
    assert list(product(range(4), repeat=3, tqdm_class=lambda x: x)) == \
        listproduct
    # Avoid "TypeError: object() takes no parameters" in python 3.x
    # See https://github.com/tqdm/tqdm/issues/313
    try:
        object()
    except TypeError:
        pass
    else:
        assert list(product(range(4), repeat=3, tqdm_class=object)) == \
            listproduct

# Generated at 2022-06-14 13:14:27.147268
# Unit test for function product
def test_product():
    from .utils import FakeTqdmFile
    from .gui import tnrange
    from .std import tqdm
    from .utils import format_sizeof
    from .utils import _term_move_up
    for tqdm_cls in [tnrange, tqdm]:
        f = FakeTqdmFile()
        for i in tqdm_cls(product(range(10), repeat=2), ascii=True,
                          file=f):
            pass
        assert "\r100%|" in f.getvalue()

        f = FakeTqdmFile()
        for i in tqdm_cls(product(range(100), repeat=2), desc="test",
                          ascii=True, file=f):
            pass
        assert "\r100%|" in f.getvalue()



# Generated at 2022-06-14 13:14:29.857191
# Unit test for function product
def test_product():
    with product(range(0, 3), range(0, 3)) as it:
        assert tuple(it) == tuple((i, j) for i in range(0, 3) for j in range(0, 3))

# Generated at 2022-06-14 13:14:37.711251
# Unit test for function product
def test_product():
    """Test for tqdm.itertools.product"""
    from ..tqdm import trange
    from itertools import product as it_product
    for obj in [itertools, trange]:
        for args in [('ab', 'cd'), ('ab', 'cd', 'ef'), ('ab',) * 10]:
            th = obj.product(*args)
            it = it_product(*args)
            assert next(th) == next(it)
            assert next(th) == next(it)
            assert hasattr(th, 'n')


# TODO?: rename to itertools.permutations(iterable, r=None, tqdm=None) and
# TODO?: permutations(iterable, r=None, tqdm=None)



# Generated at 2022-06-14 13:14:47.674279
# Unit test for function product
def test_product():
    """
    Unit test for `itertools.product`.
    """
    from .tests import _test_iter
    from .tests import format_sizeof

    _test_iter(itertools.product(*[range(10)] * 10))
    for t in (0, 100):
        for i in range(1, 10):
            # Here we are testing that `product` yields the same as `itertools`
            # as well as testing `product` itself and `_test_iter`.
            _test_iter(itertools.product(*[range(i)] * i),
                       product(*[range(i)] * i))
        _test_iter(itertools.product(*[range(10)] * 10),
                   product(*[range(10)] * 10, total=t))

    # Test that `product` doesn't crash on

# Generated at 2022-06-14 13:14:55.430972
# Unit test for function product
def test_product():
    from .tqdm_gui import tqdm
    from collections import namedtuple
    from random import random
    from time import sleep
    vals = list(range(1, 10))
    Param = namedtuple('Param', ['a', 'b'])
    for p in tqdm(list(product(vals, vals)), desc='test_product'):
        sleep(random())
    for p in tqdm(list(product(vals, vals)), desc='test_product', total=81):
        sleep(random())
    for p in tqdm(list(product(Param(a, b) for a in vals for b in vals)),
                  desc='test_product'):
        sleep(random())

# Generated at 2022-06-14 13:15:04.701415
# Unit test for function product
def test_product():
    from numpy.testing import assert_raises
    import numpy as np

    def my_float_range(x, y, z):
        i = x
        while i < z:
            yield i
            i += y

    x = my_float_range(0, .25, 3.2)
    x2 = list(x)

    y = my_float_range(0, .5, 5)
    y2 = list(y)

    list_x_y = []
    for i in product(x, y):
        list_x_y.append(i)

    assert_raises(TypeError, product)
    assert_raises(TypeError, product, 3)
    assert_raises(TypeError, product, 3, 3)

# Generated at 2022-06-14 13:15:12.894682
# Unit test for function product
def test_product():
    """ Unit test for function `product` """
    assert list(product(range(3), [1, 2])) \
        == list(itertools.product(range(3), [1, 2]))

    assert list(product(range(3), [1, 2], tqdm_class=None)) \
        == list(itertools.product(range(3), [1, 2]))

    assert list(product(range(3), [1, 2], tqdm_class=None,
                        desc="test_product")) \
        == list(itertools.product(range(3), [1, 2]))

# Generated at 2022-06-14 13:15:26.134818
# Unit test for function product
def test_product():
    from .tqdm_test import with_setup_args
    from .tests_tqdm import _range
    import sys


# Generated at 2022-06-14 13:15:32.409565
# Unit test for function product
def test_product():
    """Test that itertools.product with wrapper gives same results"""
    from numpy.random import randint
    from numpy import prod
    n = 20
    s = list(product(range(n), range(n * 2), range(n * 3)))
    assert len(list(product([(), ()], [(), ()]))) == 4
    assert len(s) == prod([n, n * 2, n * 3])
    assert s == itertools.product(range(n), range(n * 2), range(n * 3))
    assert list(product(range(n))) == list(range(n))
    assert isinstance(product(range(n)), itertools.product)
    r = randint(0, 2, 5)
    assert len(list(product(*[{0, 1} for _ in range(5)])))

# Generated at 2022-06-14 13:15:40.919960
# Unit test for function product
def test_product():
    from .tests import BaseTestMixin
    import numpy as np
    class Test(BaseTestMixin):
        def test_product(self):
            for a in [0, 1, 2]:
                for b in [0, 1]:
                    for c in [2, 3, 4, 5]:
                        for x, y, z in product(*(range(i) for i in [a, b, c]),
                                               tqdm_class=self.tqdm):
                            self.sp(x)
                            self.sp(y)
                            self.sp(z)

    Test().test_product()

# Generated at 2022-06-14 13:15:46.205012
# Unit test for function product
def test_product():
    """Sample function with PEP 484 type annotations.

    Args:
        iterables ([type]): [description]

    Returns:
        [type]: [description]
    """
    from random import randint
    from random import uniform
    from math import ceil
    from time import sleep
    def rand_iter(N):
        for _ in tqdm_auto(range(randint(1, N))):
            yield uniform(1, 100)

    list(product(rand_iter(3), rand_iter(2), rand_iter(3)))
    list(product(range(10), range(20), range(30)))
    list(product("abcd", "xy", "12345"))
    list(product("abcdef", repeat=randint(1, 3)))

# Generated at 2022-06-14 13:15:56.776626
# Unit test for function product
def test_product():
    import numpy as np
    import pandas as pd
    import random
    import six
    import sys
    import time
    import unittest
    from ..tests import TestCase


    class TestProduct(TestCase):
        def test_draw(self):
            """Test sample product call"""
            with tqdm_auto(range(5), desc="draw", leave=False) as t:
                for i in t:
                    time.sleep(.1)
            time.sleep(0.1)
            self.assertIn("draw", self.get_state().get_description())
            self.assertIn("draw", self.get_state(stdout=0).get_description())
            self.assertIn("draw", self.get_state(stdout=1).get_description())

# Generated at 2022-06-14 13:16:01.207577
# Unit test for function product
def test_product():
    from ..utils import format_sizeof
    from ..utils import format_interval
    import time
    import sys
    I = 6  # number of iterations
    assert (list(product(range(I), repeat=3)) ==
            list(itertools.product(range(I), repeat=3)))

    t = time.time()
    it = product(range(I), repeat=3)
    print(format_interval(time.time() - t))
    t = time.time()
    list(it)
    print(format_interval(time.time() - t))
    for i in it:
        pass
    print(format_interval(time.time() - t))
    it = product(range(I), repeat=3)

# Generated at 2022-06-14 13:16:04.763112
# Unit test for function product
def test_product():
    for i in product('AB', 'xy', '123'):
        pass
    assert i == ('B', 'y', '1'), i

if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:16:13.603624
# Unit test for function product
def test_product():
    import operator
    import sys
    import time
    from .utils import FormatMixin
    from .std import tqdm

    class FakeTTY(FormatMixin):
        file = None

        def __init__(self, file):
            self.file = file

        def isatty(self):
            return True

    @tqdm(ascii=True, file=FakeTTY(sys.stdout))
    def my_prod():
        for _ in product('abcd', repeat=4):
            time.sleep(0.01)

    my_prod()


# Generated at 2022-06-14 13:16:22.628624
# Unit test for function product
def test_product():
    for i in test_product.iterables:
        for j in product(*i):
            pass
        for j in product(*i, tqdm_class=tqdm_auto):
            pass
    # Advanced test
    test_product.iterables = [iter([1, 2]), iter([3])]
    for i in test_product.iterables:
        for j in product(*i, tqdm_class=None):
            pass
        for j in product(*i, tqdm_class=lambda x: x):
            pass
    test_product.iterables = [iter(range(k)) for k in (3, 2, 4, 5)]

# Generated at 2022-06-14 13:16:32.172796
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    from .tests_tqdm import pretest_posttest

    # Using strings
    # NB: strings are iterable in python2
    @pretest_posttest
    def test_product_string():
        for i in product(['a', 'b', 'c', 'd'], repeat=2):
            pass

    # Using lists
    # NB: strings are iterable in python2
    @pretest_posttest
    def test_product_list():
        for i in product([1, 2, 3, 4], repeat=2):
            pass

    # Using tuples
    @pretest_posttest
    def test_product_tuple():
        for i in product(range(10), repeat=2):
            pass

    # Testing keyword argument `tqdm_

# Generated at 2022-06-14 13:16:47.186494
# Unit test for function product
def test_product():
    from ..utils import format_sizeof
    from .tqdm import trange
    from .trange import (
        trange_progress, trange_pbar, trange_notebook, trange_ascii,
        trange_write, trange_len, trange_wrap, trange_custom)
    from .std import tqdm, tqdm_pandas
    import pandas as pd

    # Monkeypatching the trange (to test trange_len)
    def trange_monkey(start, stop=None, step=1):
        """
        Fake trange with progress bar and customisation
        """
        x = trange_pbar(start, stop, step)
        x.desc = "Monkey-patched desc"
        return x


# Generated at 2022-06-14 13:16:54.250730
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import numpy as np
    # testing product
    a = range(0, 5)
    b = range(5, 10)
    c = range(10, 15)
    z = range(15, 20)

    with tqdm_auto(total=5*5*5) as t:
        for i, j, k in product(a, b, c, tqdm_class=tqdm_auto.tqdmbase):
            assert (i, j, k) == (i, j, k)

# Generated at 2022-06-14 13:17:00.607547
# Unit test for function product
def test_product():
    """Test function product"""
    from .utils import FreezableClass
    from .std import tqdm
    from .utils import format_interval as fi

    def iter_():
        for _ in product([1, 2, 3], ['a', 'b', 'c'], tqdm=tqdm):
            yield FreezableClass()

    for i in iter_():
        assert i.frozen()

    # Test with total None
    def iter_():
        for _ in product(iter(range(1000)), tqdm=tqdm):
            yield FreezableClass()

    # Test with total 0
    def iter_():
        for _ in product(iter([]), tqdm=tqdm):
            yield FreezableClass()

    # Test iterator with len

# Generated at 2022-06-14 13:17:03.462631
# Unit test for function product
def test_product():
    from .tests import tests
    res = list(product(range(10), repeat=2))
    with tests.compare_prod(res):
        return res

# Generated at 2022-06-14 13:17:13.061345
# Unit test for function product
def test_product():
    from random import shuffle
    from .utils import FormatCustomText
    from .std import AllMethodsMixin

    for mode in [tqdm_auto, tqdm_gui, tqdm, tqdm_notebook, tqdm_pandas]:
        with mode(total=8) as pbar:
            for _ in product('ABC', '1234', tqdm=pbar, tqdm_class=mode):
                pass
        assert pbar.n == pbar.total
        assert pbar.last_print_n == pbar.n
        # Test custom classes
        pbar = mode(total=8)
        for x in product('ABC', '1234', tqdm=pbar, tqdm_class=FormatCustomText):
            pass
        pbar.close()
        # Test AllMethodsMixin,

# Generated at 2022-06-14 13:17:19.807739
# Unit test for function product
def test_product():
    """Test function `product`."""
    # Test against itertools
    def product_itertools(*args, **kwargs):
        return list(itertools.product(*args))
    assert product('ABCD', 'xy') == product_itertools('ABCD', 'xy')
    assert product('ABCD', 'xy', tqdm_class=None) == product_itertools('ABCD', 'xy')

    # Test against itertools for kwargs
    def product_itertools_kwargs(*args, **kwargs):
        return list(itertools.product(*args, **kwargs))
    assert product('ABCD', 'x', repeat=4) == product_itertools_kwargs('ABCD', 'x', repeat=4)

# Generated at 2022-06-14 13:17:24.865138
# Unit test for function product
def test_product():
    """Test for itertools.product"""
    for _ in product(range(10)):
        pass
    for _ in product(range(10), (1, 2, 3)):
        pass


if __name__ == '__main__':
    from utils import _test_itertools
    _test_itertools(test_product, "product")

# Generated at 2022-06-14 13:17:33.750026
# Unit test for function product
def test_product():
    a = [1]
    b = [i for i in range(3)]
    c = [[1], [1, 2], [1, 2, 3]]
    d = [[1, 2, 3], [1, 2]]

    cd = list(itertools.product(c, d))
    assert [len(i) for i in cd] == [3, 3]
    assert len(cd[0]) == 2
    assert len(cd[1]) == 2

    # check for bug:
    for i, j in product(c, d):
        pass

    # check for bug:
    for i, j in product(d, c):
        pass

    # check for bug:
    for i, j in product(a, b):
        pass

    # check for bug and total calculation:

# Generated at 2022-06-14 13:17:37.071874
# Unit test for function product
def test_product():
    """Test for `product`"""
    from ._version import get_versions
    if tqdm_auto.__version__ < get_versions()["version"]:
        for i, _ in enumerate(product("abc", repeat=4)):
            if i == 1:
                break

# Generated at 2022-06-14 13:17:45.890095
# Unit test for function product
def test_product():
    from .tests import pretest_posttest_testsuite
    from .utils import format_sizeof
    from .utils import SimpleNamespace
    import pickle
    import operator
    res = list(product(range(10), "abc", ['a', 'b', 'c']))
    assert len(res) == 10 * 3 * 3
    assert res == list(itertools.product(range(10), "abc", ['a', 'b', 'c']))
    assert res[3] == (3, 'c', 'b')
    assert len(list(product(range(10), repeat=2))) == 10 ** 2
    assert len(list(product(range(10), repeat=3))) == 10 ** 3
    assert (len(list(product(range(10), repeat=4)))
            == 10 ** 4)

# Generated at 2022-06-14 13:18:02.888186
# Unit test for function product
def test_product():
    """
    Simple unit tests.
    """
    import numpy as np
    from collections import defaultdict
    from .tqdm_gui import tqdm as tqdm_gui
    from .std import tqdm as tqdm_std
    from .std import trange

    def _each(tqdm, total):
        for i in tqdm(range(total)):
            pass

    for tqdm in [tqdm_auto, tqdm_gui, tqdm_std]:
        def _func():
            return tqdm(range(5))
        assert list(_func()) == [0, 1, 2, 3, 4]
        assert list(_func()) == [0, 1, 2, 3, 4]
        assert list(tqdm(None)) == []

# Generated at 2022-06-14 13:18:13.356502
# Unit test for function product
def test_product():
    from .tests import TestCase
    from .tests import StringIO


# Generated at 2022-06-14 13:18:18.127322
# Unit test for function product
def test_product():
    """Test for function product"""
    iterables = [range(100), [1, 2, 3]]
    total = len(iterables[0]) * len(iterables[1])
    # Sum of each
    s = sum([j * i for i, j in product(*iterables)])
    assert s == total * len(iterables[0])

# Generated at 2022-06-14 13:18:23.460136
# Unit test for function product
def test_product():
    from ._utils import closing
    # 200-D space is too hard to test by brute-force, so just test it doesn't crash
    iterables = [range(i) for i in [3, 5, 7, 11, 13]]
    for i in closing(product(*iterables)):
        pass
    for i in closing(product(*iterables, ascii=True)):
        pass
    from io import StringIO
    file = StringIO()
    for i in closing(product(*iterables, file=file)):
        pass



# Generated at 2022-06-14 13:18:32.040481
# Unit test for function product
def test_product():
    # Test with a single iterator
    iterable = range(10)
    results = []
    for v in product(iterable):
        assert v[0] in iterable
        results.append(v)
    assert len(results) == 10
    assert results == sorted(results)
    # Test with two iterables
    iterable2 = range(10)
    results = []
    for v in product(iterable, iterable2):
        assert v[0] in iterable
        assert v[1] in iterable2
        results.append(v)
    assert len(results) == len(iterable) * len(iterable2)
    assert results == sorted(results)
    # Test with three iterables
    iterable3 = range(3)
    results = []

# Generated at 2022-06-14 13:18:42.007939
# Unit test for function product
def test_product():
    """Unit test for product"""
    from ..main import tqdm
    from numpy.random import randint
    from time import sleep

    # Test basic functionality
    for _ in tqdm(product(range(3), repeat=3), desc='connectivity'):
        sleep(0.01)

    # Test dynamic total
    for _ in tqdm(product(range(10), repeat=randint(2, 10)), desc='dynamic_total'):
        sleep(0.01)

    # Test utf8 desc
    for _ in tqdm(product(range(10), repeat=randint(2, 10)), desc='desc_\xe9_\xe9'):
        sleep(0.01)

    # Test dynamic total with ascii desc

# Generated at 2022-06-14 13:18:46.666634
# Unit test for function product
def test_product():
    """Test that tqdm(...).update() == len(...)"""
    with tqdm_auto(total=0) as t:
        t.update(sum(1 for _ in product(
            range(10), range(10), range(10),
            tqdm_class=tqdm_auto,
            mininterval=0, miniters=1, maxiters=0)))

# Generated at 2022-06-14 13:18:53.062084
# Unit test for function product
def test_product():
    """Test that product behaves correctly"""
    # Test tqdm(product(...)) == product(tqdm(...))
    product_ = lambda *args: [tuple(x) for x in product(*args)]
    assert product_(range(100), range(100)) == product_(tqdm_auto(range(100)),
                                                        tqdm_auto(range(100)))
    assert product_(range(100), range(100)) == product_(range(100),
                                                        range(100),
                                                        tqdm_class=tqdm_auto)

if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:19:02.284029
# Unit test for function product
def test_product():
    with tqdm_auto(leave=True) as t:
        assert list(product(range(1), 'abc', tqdm_class=t.__class__)) \
            == [(0, 'a'), (0, 'b'), (0, 'c')]
    with tqdm_auto(leave=True) as t:
        assert list(product(range(2), 'ab', tqdm_class=t.__class__)) \
            == [(0, 'a'), (0, 'b'), (1, 'a'), (1, 'b')]

# Generated at 2022-06-14 13:19:10.651797
# Unit test for function product
def test_product():
    import numpy as np
    from ..numpy import tqdm
    with tqdm(total=128) as bar:
        result = {
            (a, b, c): None
            for (a, b, c) in product(
                range(2),
                range(4),
                range(8),
                tqdm_class=tqdm,
                dynamic_ncols=True,
                desc="blah",
                leave=None,
                bar_format="{l_bar}{bar}|",
            )
        }
    assert len(result) == 2 * 4 * 8
    assert list(result) == list(itertools.product(range(2), range(4), range(8)))

# Generated at 2022-06-14 13:19:41.890340
# Unit test for function product
def test_product():
    """Test product"""
    pr = product([10, 20, 30], [2, 3], tqdm_class=tqdm_auto)
    assert hasattr(pr, '__iter__')
    res = [i for i in pr]
    assert res == list(itertools.product([10, 20, 30], [2, 3]))


if __name__ == '__main__':
    from ..utils import TestCase
    with TestCase():
        test_product()

# Generated at 2022-06-14 13:19:44.043511
# Unit test for function product
def test_product():
    product(['a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h'],
            ['i', 'j', 'k', 'l'],
            ['m', 'n', 'o', 'p'])

# Generated at 2022-06-14 13:19:52.046747
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from ._deprecate import TEST_ITERATIONS
    assert list(product(
        list(range(TEST_ITERATIONS)),
        list(range(TEST_ITERATIONS)),
        list(range(TEST_ITERATIONS)),
        tqdm_class=tqdm_auto
    )) == list(itertools.product(list(range(TEST_ITERATIONS)),
                                 list(range(TEST_ITERATIONS)),
                                 list(range(TEST_ITERATIONS))))

# Generated at 2022-06-14 13:19:53.636438
# Unit test for function product
def test_product():
    for i in product('ABCD', 'xy', tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:19:58.799944
# Unit test for function product
def test_product():
    """Unit test for function product"""
    assert list(product(range(3), range(3))) == [
        (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Generated at 2022-06-14 13:20:07.495812
# Unit test for function product
def test_product():
    """Test product"""
    # Test triviality
    assert list(product((), (), ()) == [])
    # Test normal operation
    assert list(product(range(2), range(2), range(2))) == [(0, 0, 0),
                                                          (0, 0, 1),
                                                          (0, 1, 0),
                                                          (0, 1, 1),
                                                          (1, 0, 0),
                                                          (1, 0, 1),
                                                          (1, 1, 0),
                                                          (1, 1, 1)]


# Generated at 2022-06-14 13:20:15.363476
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    # Test 1
    import sys
    import six
    import tempfile
    import tqdm_test_package.tqdm_test_package_itertools as test_itertools
    iterables = (range(100), 'abc', [1., 2., 3.])
    assert sum(i**2 for i in range(100)) == 328350
    assert "".join(chr(i) for i in range(ord('a'), ord('z')+1)) == tqdm_auto.alphabet[:26]
    if six.PY2:
        assert sum(map(float, range(1, 4))) == 6
    else:
        assert sum(list(map(float, range(1, 4)))) == 6
    assert list(product(*iterables))

# Generated at 2022-06-14 13:20:23.766051
# Unit test for function product
def test_product():
    """ Test itertools_ext.product """
    import numpy as np
    assert list(product([1, 2, 3], [4, 5, 6], tqdm_class=None)) == list(itertools.product([1, 2, 3], [4, 5, 6]))
    assert list(product([1, 2, 3], [4, 5, 6])) == list(itertools.product([1, 2, 3], [4, 5, 6]))
    prod_return = list(product([[1, 2], [3, 4]], [4, 5, 6], [7, 8]))
    prod_return.sort()

# Generated at 2022-06-14 13:20:30.182301
# Unit test for function product
def test_product():
    from .tests_tqdm import _check_tqdm_closure
    _check_tqdm_closure(product, range(3), range(3), tqdm_class=tqdm_auto)
    _check_tqdm_closure(product, range(3), range(3), tqdm_class=tqdm_auto,
                        leave=True)

# Generated at 2022-06-14 13:20:35.622435
# Unit test for function product
def test_product():
    from numpy import prod
    from numpy.testing import assert_equal
    from numpy.random import randint

    for i in range(5):
        a = randint(1, 4)
        b = randint(1, 4)
        c = randint(1, 7)
        d = randint(1, 7)
        assert_equal(prod([a, b, c, d]),
                     (a * b * c) * d)

# Generated at 2022-06-14 13:21:00.122533
# Unit test for function product
def test_product():
    with tqdm_auto(total=2) as t:
        for i in product(range(2), range(2)):
            assert len(i) == 2
            t.update()

# Generated at 2022-06-14 13:21:06.729841
# Unit test for function product
def test_product():
    """Test for `tqdm.std.itertools.product`"""
    import os
    from time import sleep
    from .monitor import TMonitor
    from .utils import FormatCustomText, _version2tuple
    from .std import product

    # Test parametrization of `itertools.product`
    assert (list(product(range(2), repeat=3)) ==
            list(itertools.product(range(2), repeat=3)))

    # Test override of `itertools.product` with `total`
    assert (list(product(range(2), repeat=3)) ==
            list(itertools.product(range(2), repeat=3)))

    # Test parametrization of `itertools.product`

# Generated at 2022-06-14 13:21:16.216121
# Unit test for function product
def test_product():
    # TypeError: object of type 'int' has no len()
    import numpy as np
    assert list(product(np.linspace(0, 1, 11))) == list(np.linspace(0, 1, 11))
    # mpy on 32bit can't calculate product(xrange(10000), range(10000))
    assert list(product(range(10), range(10))) == list(itertools.product(range(10), range(10)))
    assert list(product(range(100), range(100))) == list(itertools.product(range(100), range(100)))
    assert list(product('ab', 'cd')) == list(itertools.product('ab', 'cd'))
    try:
        assert list(itertools.product())
    except:
        pass
    else:
        raise Assert

# Generated at 2022-06-14 13:21:17.288934
# Unit test for function product
def test_product():
    from .tests import trial_product
    trial_product(product)()

# Generated at 2022-06-14 13:21:20.925905
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    from .tqdm_gui import tqdm
    for i in product(range(10), range(2), range(3), tqdm_class=tqdm):
        pass

if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:21:31.727413
# Unit test for function product
def test_product():
    """
    Unit test for `product`.
    """
    from .tqdm import trange
    from .utils import FormatTe
    from .std import tqdm_stdout_redirected

    # w/o `total` argument
    for i in trange(10, desc='1st loop'):
        for j in product(range(1000000), leave=False):
            pass
    # w/ `total` argument
    with tqdm_stdout_redirected():
        for j in product(range(100), total=100):
            pass
    with tqdm_stdout_redirected():
        for j in product(range(50), range(20), total=1000):
            pass

# Generated at 2022-06-14 13:21:40.097037
# Unit test for function product
def test_product():
    """Test for function product"""
    from ..utils import _range

    import copy
    import itertools
    import sys

    iters = [_range(10), _range(6)]
    with tqdm_auto(iters[0] * iters[1]) as pbar:
        res0 = list(product(*iters))
        res0_t = [el for el in product(*iters)]
        res1 = list(itertools.product(*iters))
        progress = pbar.n
    assert (res0 == res1 == res0_t) and (progress == 60)

    with tqdm_auto(10) as pbar:
        res0 = list(product(*[tqdm(iters[0])] * 2))
        res1 = list(itertools.product(*iters))
       

# Generated at 2022-06-14 13:21:50.579339
# Unit test for function product
def test_product():
    """
    Test for the `itertools.product` function.
    """
    p = "product"
    # noinspection PyUnresolvedReferences
    import itertools as it
    for T in (tqdm_auto, tqdm_auto):
        for args in [
                (range(1, 4),),
                (range(1, 4), range(4, 7)),
                (range(1, 4), range(4, 7), range(7, 10)),
                (xrange(1, 4), xrange(4, 7)),
                (xrange(1, 4), xrange(4, 7), xrange(7, 10))]:
            assert list(T.__dict__[p](*args)) == list(it.__dict__[p](*args))

# Generated at 2022-06-14 13:21:58.091061
# Unit test for function product
def test_product():
    import random
    import string
    chars = string.ascii_uppercase

    def rng(n):
        return ''.join(random.choice(chars) for _ in range(n))
    a = [rng(random.randint(3, 10)) for _ in range(10)]
    b = [rng(random.randint(3, 10)) for _ in range(10)]
    c = [rng(random.randint(3, 10)) for _ in range(10)]
    d = [rng(random.randint(3, 10)) for _ in range(10)]

    for i in product(a, b, c, d):
        pass

# Generated at 2022-06-14 13:22:05.068717
# Unit test for function product
def test_product():
    # Test that it has the same output as itertools
    import itertools as it
    first = list(product(range(2), repeat=2))
    second = list(it.product(range(2), repeat=2))
    assert first == second

    first = list(product(range(3), repeat=3))
    second = list(it.product(range(3), repeat=3))
    assert first == second

    # Test that the total keyword of tqdm is correct
    from tqdm.utils import _term_move_up
    n = (2,) * 3
    with tqdm_auto(total=None) as t:
        for i in it.product(*n):
            pass
    first = t.total