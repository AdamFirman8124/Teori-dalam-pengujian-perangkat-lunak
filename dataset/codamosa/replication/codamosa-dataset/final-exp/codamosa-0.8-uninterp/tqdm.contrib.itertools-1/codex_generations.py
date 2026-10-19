

# Generated at 2022-06-14 13:12:47.278225
# Unit test for function product
def test_product():
    from .utils import closing, format_sizeof
    import sys

    # Moved outside the function to avoid reinitialising the generators
    # every time the function is called (for profiling purposes).
    g1 = (i for i in range(10))
    g2 = (i for i in range(100))

    # Force unit test in Python 2
    if sys.version_info[:2] == (2, 6):
        tqdm_auto._instances.clear()
        tqdm_auto.tqdm.monitor_interval = 0
    with closing(product(
            range(20),
            g1,
            g2,
            total=20 * 10 * 100,
            leave=True)) as pbar:
        for _ in pbar:
            pass

    # Make sure that the right number of iterations was counted
   

# Generated at 2022-06-14 13:12:50.042827
# Unit test for function product
def test_product():
    sl = list(product(range(3), range(3), range(3),
                      tqdm_class=tqdm_auto, desc="Test",
                      leave=True))
    assert sl == list(itertools.product(range(3), range(3), range(3)))

# Generated at 2022-06-14 13:12:52.399508
# Unit test for function product
def test_product():
    """Unit test for function product"""
    iterables = [range(5), range(5)]
    for result in product(*iterables, desc='Test'):
        pass

# Generated at 2022-06-14 13:13:04.807227
# Unit test for function product
def test_product():
    ''' Test product method against manual total count '''
    import sys
    import random
    from ..std import six
    import mock

    t = mock.MagicMock()
    t.total = 0
    t.update = mock.MagicMock(side_effect=lambda _: t.total.__iadd__(1))

    iterables = [range(random.randint(1,4)) for _ in range(4)]

    for _ in product(*iterables, tqdm_class=lambda _: t):
        continue

    if six.PY2:
        product = itertools.product
    else:
        product = itertools.product

    # Check update count

# Generated at 2022-06-14 13:13:11.918828
# Unit test for function product
def test_product():
    """
    unit test for `tqdm.contrib.itertools.product`
    """
    from tqdm.auto import trange
    list1 = range(5)
    list2 = range(2, 7)
    prod = product(list1, list2, tqdm_class=trange)
    assert list(prod) == list(itertools.product(list1, list2))


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:13:20.092824
# Unit test for function product
def test_product():
    from ..utils import FormatCustomText
    from .leave import LeaveOneOut
    from .wrap import format_interval
    import math

    n = 10
    for n_iter in range(n):
        for x in product(range(n_iter), range(n_iter), tqdm_class=FormatCustomText):
            pass

    loo = LeaveOneOut(n)
    for n_iter in range(n):
        for train_index, test_index in product(loo.split(range(n_iter)), tqdm_class=FormatCustomText):
            pass

    for n_iter in range(n):
        for x in product(range(n_iter), range(n_iter), tqdm_class=lambda **k: format_interval(**k)):
            pass


# Generated at 2022-06-14 13:13:30.871785
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import numpy as np
    res = product(range(10), range(30))
    res_comp = [[x, y] for x in range(10) for y in range(30)]
    assert list(res) == res_comp
    assert np.sum([1 for x in res]) == len(res_comp)

    res = product(range(10), range(30), tqdm_class=tqdm_auto)
    assert list(res) == res_comp
    assert np.sum([1 for x in res]) == len(res_comp)

    res = product(range(10), range(30), tqdm_class=None)
    assert list(res) == res_comp
    assert np.sum([1 for x in res]) == len(res_comp)

# Generated at 2022-06-14 13:13:40.804025
# Unit test for function product
def test_product():
    import numpy as np
    n = 3
    np.random.seed(1)
    a = np.random.randint(0, 5, (n, n))
    b = np.random.randint(0, 5, (n, n))
    c = np.random.randint(0, 5, (n, n))
    d = np.random.randint(0, 5, (n, n))
    e = np.random.randint(0, 5, (n, n))
    p = list(product(a, b, c, d, e))
    assert p == list(itertools.product(a, b, c, d, e))
    p = list(product(a, b, c, d, e, tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:13:48.377406
# Unit test for function product
def test_product():
    """
    Unit test for function `itertools.product`.
    """
    from ..utils import _range as trange
    for _range in trange, range:
        for cls in [tqdm_auto, tqdm_auto.tqdm]:
            with cls(unit="it") as t:
                t.monitor_interval = 0
                prod = product(_range(2), _range(2), tqdm_class=cls)
                assert len(list(prod)) == 4
                prod = product(_range(10), _range(10), tqdm_class=cls)
                assert len(list(prod)) == 100
                assert t.n == 100
                assert t.total == 100

# Generated at 2022-06-14 13:13:56.273288
# Unit test for function product
def test_product():
    from os import cpu_count
    from ..utils import format_sizeof
    from ..utils import SimpleNamespace
    from time import time

    # Test basics
    sizes = (5, 5, 5)
    total_size = 1
    for s in sizes:
        total_size *= s
    tot_size_str = format_sizeof(total_size)

    # Test with simple lambda
    s = SimpleNamespace(last=0, total=0)
    with tqdm_auto(desc='product_1', leave=False) as t:
        for el in product(range(sizes[0]), range(sizes[1]), range(sizes[2])):
            assert (el[0] < sizes[0] and
                    el[1] < sizes[1] and
                    el[2] < sizes[2])


# Generated at 2022-06-14 13:14:09.620909
# Unit test for function product
def test_product():
    import random
    import time

    a = [' ', "0", ".", "-", ",", "=", "a", "b",
         "c", "d", "e", "f", "g", "h", "i", "j",
         "k", "l", "m", "n", "o", "p", "q", "r",
         "s", "t", "u", "v", "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H",
         "I", "J", "K", "L", "M", "N", "O", "P",
         "Q", "R", "S", "T", "U", "V", "W", "X",
         "Y", "Z"]
    b

# Generated at 2022-06-14 13:14:16.053148
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    T = None
    for i in product(['a', 'b', 'c'], repeat=2, tqdm_class=tqdm_auto):
        T = i
    assert T == ('c', 'c')
    T = None
    for i in product(['a', 'b', 'c'], ['d', 'e'], repeat=2, tqdm_class=tqdm_auto):
        T = i
    assert T == ('c', 'e', 'e', 'e')

# Generated at 2022-06-14 13:14:22.313634
# Unit test for function product
def test_product():
    # This test is adapted from the one in itertools
    assert list(product('ABCD', 'xy')) == [('A', 'x'), ('A', 'y'),
                                           ('B', 'x'), ('B', 'y'),
                                           ('C', 'x'), ('C', 'y'),
                                           ('D', 'x'), ('D', 'y')]
    assert list(product(range(2), repeat=3)) == [(0, 0, 0), (0, 0, 1),
                                                 (0, 1, 0), (0, 1, 1),
                                                 (1, 0, 0), (1, 0, 1),
                                                 (1, 1, 0), (1, 1, 1)]

if __name__ == "__main__":
    import pytest

# Generated at 2022-06-14 13:14:28.112130
# Unit test for function product
def test_product():
    """
    Test function `itertools_recipes.product`.
    """
    from .tests_tqdm import StringIO
    from .tests_tqdm_gui import gui_sleep

    # Test simple example
    str_result = ''
    out = StringIO()
    for _ in product([1, 2, 3], tqdm_class=tqdm_auto, file=out):
        str_result += out.getvalue() + '\n'
        out.seek(0)
        out.truncate(0)
    assert str_result == ('1/6\n' * 6)

    # Test iterator error
    str_result = ''
    out = StringIO()

# Generated at 2022-06-14 13:14:35.465005
# Unit test for function product
def test_product():
    for c in [tqdm_auto.tqdm, tqdm_auto.tqdm_notebook]:
        assert len(list(product(range(10), range(10), tqdm_class=c))) == 100
        assert list(product(range(3), range(3), tqdm_class=c)) == [(0, 0),
                                                                   (0, 1),
                                                                   (0, 2),
                                                                   (1, 0),
                                                                   (1, 1),
                                                                   (1, 2),
                                                                   (2, 0),
                                                                   (2, 1),
                                                                   (2, 2)]

# Generated at 2022-06-14 13:14:41.403217
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    try:
        iter(product(range(3), range(3)))
    except TypeError:
        raise AssertionError("product(range(3), range(3))")
    try:
        iter(product(range(3), range(3), tqdm_class=tqdm_auto))
    except TypeError:
        raise AssertionError("product(range(3), range(3), tqdm_class=tqdm_auto)")

# Generated at 2022-06-14 13:14:48.073725
# Unit test for function product
def test_product():
    """Test function product()"""
    it = product([1, 2, 3], [4, 5], [6, 7],
                 tqdm=lambda x: x, total=8)
    # itertools.product() returns tuples
    assert (next(it), next(it)) == ((1, 4, 6), (1, 4, 7))
    # Ensure correct total was passed, and total=None still works
    assert next(product([1, 2, 3], total=None)) == 1

# Generated at 2022-06-14 13:14:54.041827
# Unit test for function product
def test_product():
    with tqdm_auto(desc="products", leave=True) as t:
        assert list(product([1, 2, 3], [4, 5, 6], tqdm_class=t.__class__)) \
            == list(itertools.product([1, 2, 3], [4, 5, 6]))
        assert list(product(iter([1, 2, 3]), iter([4, 5, 6]),
                            tqdm_class=t.__class__)) \
            == list(itertools.product(iter([1, 2, 3]), iter([4, 5, 6])))

# Generated at 2022-06-14 13:14:55.671728
# Unit test for function product
def test_product():
    with tqdm_auto(product(range(3), range(3), range(3))) as t:
        for i in t:
            pass

# Generated at 2022-06-14 13:14:58.054775
# Unit test for function product
def test_product():
    import sys
    with tqdm_auto(leave=True, file=sys.stderr, mininterval=0) as t:
        list(product(range(100), range(100), tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:15:04.802904
# Unit test for function product
def test_product():
    """Unit test for function product"""
    iterables = [list(range(10))] * 3
    product(*iterables, tqdm_class=tqdm_auto)
    product(*iterables, tqdm_class=tqdm_auto, total=10)


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:15:07.940056
# Unit test for function product
def test_product():
    for i in product([range(2)], [range(2)], [range(2)], [range(2)], [range(2)]):
        pass



# Generated at 2022-06-14 13:15:16.007842
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    ans = [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'b', 'e'), ('a', 'c', 'd'), ('a', 'c', 'e'), ('a', 'd', 'e'), ('b', 'c', 'd'), ('b', 'c', 'e'), ('b', 'd', 'e'), ('c', 'd', 'e')]
    assert list(product("abcd", repeat=3)) == ans
    assert list(product("abcd", repeat=3, tqdm_class=tqdm_auto)) == ans

# Generated at 2022-06-14 13:15:22.696099
# Unit test for function product
def test_product():
    from ..utils import _terminal_len

    def _assert_tqdm(tqdm_class, iter_size, desc=None, leave=False,
                     ascii=None, min_iters=1):
        with tqdm_class(desc=desc, total=min_iters, ascii=ascii,
                        leave=leave, miniters=min_iters) as t:
            tres = [i for i in product(range(10), range(5), range(3),
                                       tqdm_class=tqdm_class)]
        assert len(tres) == iter_size

        # Check that miniters was respected
        if min_iters > 1:
            assert len(t.format_meter(t.n)) == 0

# Generated at 2022-06-14 13:15:28.577060
# Unit test for function product
def test_product():
    """Test for `itertools.product`"""
    for i in product(range(3), range(2), range(4), tqdm_class=tqdm_auto):
        pass  # just iterate
    assert i == (2, 1, 3)


if __name__ == "__main__":
    """Test `itertools.product`"""
    test_product()

# Generated at 2022-06-14 13:15:36.832390
# Unit test for function product
def test_product():
    """
    Unit test of :func:`tqdm.itertools.product`.
    """
    from tqdm.tests import dummy_iterator
    a = [1, 2, 3]
    b = ['x', 'y']

    assert list(product(dummy_iterator([1, 2, 3]), dummy_iterator(['x', 'y']))) == list(itertools.product(a, b))
    assert list(product(a, b)) == list(itertools.product(a, b))

# Generated at 2022-06-14 13:15:46.092405
# Unit test for function product
def test_product():
    from ..utils import format_sizeof
    import random
    import time
    random.seed(0)
    m = random.randint(1, 10)
    n = random.randint(1, 10)
    o = random.randint(1, 10)
    iterables = [range(m), range(n), range(o)]
    print("m={}, n={}, o={}".format(m, n, o))
    tstart = time.time()
    total_size = 0
    iterator1 = product(*iterables, tqdm_class=tqdm_auto)
    iterator2 = product(*iterables, tqdm_class=tqdm_auto, total=None)
    for i in iterator1:
        total_size += format_sizeof(i)

# Generated at 2022-06-14 13:15:56.649037
# Unit test for function product
def test_product():
    from itertools import product
    from random import randint
    from numpy.testing import assert_array_equal as assert_a_eq
    from numpy.testing import assert_array_almost_equal as assert_a_aeq
    for i in range(200):
        total1 = randint(1, 100)
        total2 = randint(1, 100)
        total3 = randint(1, 100)
        p1 = tuple([[j] * randint(1, 100) for j in range(total1)])
        p2 = tuple([[j] * randint(1, 100) for j in range(total2)])
        p3 = tuple([[j] * randint(1, 100) for j in range(total3)])

# Generated at 2022-06-14 13:16:00.994883
# Unit test for function product
def test_product():
    """
    $ python -m tqdm.utils.itertools_recipes test_product
    """
    from numpy.random import randint, seed
    import time
    seed(0)

    for product in [
            itertools.product,
            lambda *a, **kw: product(*a, **kw)]:
        for kwargs in [{}, {"total": None}]:
            for _ in range(3):
                ret = list(product(
                    range(3),
                    randint(10, size=3),
                    randint(5, size=(3, 2)),
                    randint(8, size=(3, 3, 4)),
                    **kwargs))
                time.sleep(.1)


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:16:11.501219
# Unit test for function product
def test_product():
    import sys
    if sys.version_info < (3, 0, 0):
        from cStringIO import StringIO
    else:
        from io import StringIO
    import os

    out = StringIO()
    with tqdm_auto(total=24, file=out, leave=False) as t:
        for i in product(range(4), repeat=3):
            t.update()
    assert t.n == t.total == 24


# Generated at 2022-06-14 13:16:27.474718
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    # Test simple case
    r = []
    for i in product([1, 2, 3], [4, 5, 6], tqdm_class=None):
        r.append(i)
    assert r == [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4),
                 (3, 5), (3, 6)]
    # Test duplicates case
    r = []
    for i in product(["a", "b"], ["c", "c"], ["d", "d"], tqdm_class=None):
        r.append(i)

# Generated at 2022-06-14 13:16:35.406292
# Unit test for function product
def test_product():
    for a in product(range(0), range(0), tqdm_class=tqdm_auto):
        assert False
    for a in product(range(0), range(1), tqdm_class=tqdm_auto):
        assert False
    for a in product(range(1), range(0), tqdm_class=tqdm_auto):
        assert False

    assert list(product(range(0), range(0))) == []
    assert list(product(range(0), range(1))) == []
    assert list(product(range(1), range(0))) == []

    assert list(product(range(1), range(1))) == [(0, 0)]
    assert list(product(range(1), range(1), range(1))) == [(0, 0, 0)]


# Generated at 2022-06-14 13:16:42.186018
# Unit test for function product
def test_product():
    import random
    iterables = [[random.randint(0, 10) for _ in range(random.randint(0, 10))]
                 for _ in range(random.randint(1, 10))]
    assert (list(product(*iterables)) ==
            list(itertools.product(*iterables)))
    # Test tqdm
    assert (list(product(*iterables, tqdm_class=tqdm_auto)) ==
            list(itertools.product(*iterables)))

# Generated at 2022-06-14 13:16:43.458453
# Unit test for function product
def test_product():
    from .tests import test_product

    test_product(product)

# Generated at 2022-06-14 13:16:48.273818
# Unit test for function product
def test_product():
    """Test function product"""
    # With total
    with tqdm_auto(total=3) as t:
        for _ in product('ABC', 'xy', tqdm=t):
            pass
    assert t.n == 3
    # Without total
    with tqdm_auto() as t:
        for _ in product('ABC', 'xy', tqdm=t):
            pass
    assert t.n == 6

# Generated at 2022-06-14 13:16:53.836378
# Unit test for function product
def test_product():
    from .._utils import _range
    assert set(product('ABCD', 'xy')) == set(itertools.product('ABCD', 'xy'))
    assert list(product(_range(0), _range(0))) == list(itertools.product(_range(0), _range(0)))
    assert set(product(_range(0))) == set(itertools.product(_range(0)))
    assert list(product(bar=_range(3))) == list(itertools.product(bar=_range(3)))
    assert list(product(_range(3), repeat=3)) == list(itertools.product(_range(3), repeat=3))

# Generated at 2022-06-14 13:16:57.432133
# Unit test for function product
def test_product():
    a = range(4)
    b = range(4, 10)
    for i, j in product(a, b):
        assert i in a
        assert j in b
    for i, j in product(a, b, tqdm_class=tqdm_auto):
        assert i in a
        assert j in b

# Generated at 2022-06-14 13:17:06.671424
# Unit test for function product
def test_product():
    from tqdm import trange
    for i in product(range(10), trange,
                      total=20, miniters=10, mininterval=0.1,
                      ascii=True, file=None, dynamic_ncols=False,
                      leave=True, smoothing=0.1):
        pass
    for i in product(range(10), trange, total=None,
                      bar_format="{l_bar}{bar}{r_bar}",
                      ascii=True, file=None, dynamic_ncols=False,
                      leave=True, smoothing=0.1):
        pass

# Generated at 2022-06-14 13:17:15.225620
# Unit test for function product
def test_product():
    """
    Tests `product` function.
    """
    import numpy as np
    from ._utils import _range

    np.random.seed(12345)

    # check that itertools.product is equivalent
    for total in _range(0, 5):
        for ranges in list(itertools.product(
                *[list(_range(0, i)) for i in _range(0, total)])):
            it = product(*[list(_range(0, i)) for i in ranges],
                         tqdm_class=tqdm_auto)
            np.testing.assert_array_equal(
                next(it), next(itertools.product(*[list(_range(0, i))
                                                   for i in ranges])))


# Generated at 2022-06-14 13:17:22.877814
# Unit test for function product
def test_product():
    assert [i for i in product([3, 4])] == [(3,), (4,)]
    assert [i for i in product([3, 4], [1, 2])] == [(3, 1), (3, 2), (4, 1), (4, 2)]
    assert [i for i in product([3, 4], [1, 2], [6, 7])] == \
        [(3, 1, 6), (3, 1, 7), (3, 2, 6), (3, 2, 7), (4, 1, 6), (4, 1, 7), (4, 2, 6), (4, 2, 7)]

# Generated at 2022-06-14 13:17:41.714273
# Unit test for function product
def test_product():
    # Without total
    p = product(list(range(10)), list(range(10)))
    assert list(p) == [(i, j) for i in range(10) for j in range(10)]
    p = product(list(range(10)), list(range(10)), tqdm_class=None)
    assert list(p) == [(i, j) for i in range(10) for j in range(10)]
    # With total
    p = product(list(range(10)), list(range(10)), ncols=1)
    assert list(p) == [(i, j) for i in range(10) for j in range(10)]
    p = product(list(range(10)), list(range(10)), ncols=1, tqdm_class=None)

# Generated at 2022-06-14 13:17:48.394140
# Unit test for function product
def test_product():
    """Unit test for function `product`"""
    import numpy as np
    sz = 2
    # Generate random example
    a = np.random.randint(sz, size=sz)
    b = np.random.randint(sz, size=sz)
    c = np.random.randint(sz, size=sz)
    # Generate answer
    p = list(product(a, b, c))
    assert np.all(p == list(itertools.product(a, b, c)))

# Generated at 2022-06-14 13:17:57.752483
# Unit test for function product
def test_product():
    from .tqdm import _range as trange
    assert [i for i in product(trange(3), trange(3))] == \
        [j for j in itertools.product(range(3), range(3))]
    assert [i for i in product(trange(3))] == \
        [j for j in itertools.product(range(3))]
    assert [i for i in product(trange(3), trange(3), tqdm_class=lambda x: x)] == \
        [j for j in itertools.product(range(3), range(3))]
    assert [i for i in product(trange(3), tqdm_class=lambda x: x)] == \
        [j for j in itertools.product(range(3))]


del absolute_

# Generated at 2022-06-14 13:18:04.348480
# Unit test for function product
def test_product():
    from ..__init__ import tqdm
    from .tests_tqdm import pretest_posttest, with_unit_option

    total = 9  # len(range(3))**2

# Generated at 2022-06-14 13:18:06.970865
# Unit test for function product
def test_product():
    prod = product(range(10), range(10), range(10), range(10))
    prod = list(prod)
    assert len(prod) == 10000

# Generated at 2022-06-14 13:18:10.018350
# Unit test for function product
def test_product():
    """Unit test for function product"""
    assert 1 == sum(1 for _ in product(range(100), range(100), range(100),
                    tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:18:20.082615
# Unit test for function product
def test_product():
    # Move to nose test
    from numpy.random import randint

    a = randint(0, 9, size=20)
    b = ['abc', 'xyz', '123']
    ab = list(itertools.product(a, b))

    p = tqdm.product(a, b)
    assert p is not None
    pab = list(p)
    assert pab is not None
    assert ab == pab

    # Make sure that the iterator is consumed
    p = tqdm.product(a)
    assert p is not None
    assert len(list(p)) == len(a)

    # Assert total=None doesn't fail
    p = tqdm.product(a, total=None)
    assert p is not None

# Generated at 2022-06-14 13:18:30.511382
# Unit test for function product
def test_product():
    from operator import mul
    from .tests import closing_returned
    from numpy.random import randint, permutation

    def prod(iterable):
        """ Return the product of an iterable, e.g. prod([1,2,3]) = 6 """
        return reduce(mul, iterable, 1)

    def _test(a, b, c, total=None):
        # NB: _test is called within closing_returned
        a = list(a)
        b = list(b)
        c = list(c)
        assert list(product(a, b, c)) == [
            (i, j, k) for i in a for j in b for k in c]
        assert list(product(a, repeat=5)) == list(
            itertools.product(a, repeat=5))

# Generated at 2022-06-14 13:18:35.770673
# Unit test for function product
def test_product():
    """Test product on normal and 0-length input"""
    assert list(product(range(3), range(4), range(5))) == list(itertools.product(range(3), range(4), range(5)))
    assert list(product()) == list(itertools.product())
    assert list(product(*[[]] * 4, tqdm_class=None)) == list(itertools.product(*[[]] * 4))
    assert list(product(range(0), range(4), range(5))) == list(itertools.product(range(0), range(4), range(5)))

# Generated at 2022-06-14 13:18:46.663313
# Unit test for function product
def test_product():
    # Confirm that product is equivalent to itertools.product
    assert list(product('ABCD', 'xy')) == list(itertools.product('ABCD', 'xy'))
    # Confirm that tqdm is used for iterators over iterators of sufficient length
    assert len(list(product(range(1000), range(1000)))) == 1000000
    assert len(list(product(range(1000), range(0)))) == 0
    # Confirm that only one argument is required
    assert list(product(range(10))) == list(itertools.product(range(10)))
    # Confirm that short iterables with no total are not iterated
    assert list(product(range(10), range(100), range(100), range(100),
                        range(100), range(100), range(100), range(100))) != []
   

# Generated at 2022-06-14 13:19:08.609700
# Unit test for function product
def test_product():
    """
    Test function product.
    """
    import tqdm

    prod = list(tqdm.tqdm_product(
        [list(range(100000))], show_n=10000, file=tqdm.tqdm.write))
    assert len(prod) == 100000
    assert prod[9999] == (9999,)

    prod = list(tqdm.tqdm_product(
        [list(range(10)), list(range(20))], show_n=10000, file=tqdm.tqdm.write))
    assert len(prod) == 200
    assert prod[19] == (0, 19)


# Generated at 2022-06-14 13:19:12.392210
# Unit test for function product
def test_product():
    """Test for function product"""
    expected = [
        (0, 'a'), (0, 'b'),
        (1, 'a'), (1, 'b'),
        (2, 'a'), (2, 'b')]
    assert (list(product(range(3), ['a', 'b'])) == expected)

# Generated at 2022-06-14 13:19:17.130629
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import numpy as np
    from ..utils import _range

    for i in _range(100):
        a = np.random.random_integers(1, 100)
        b = np.random.random_integers(1, 100)
        c = np.random.random_integers(1, 100)

        t1 = np.prod(a, b, c)
        assert t1 == np.prod(product(range(a), range(b), range(c)))

# Generated at 2022-06-14 13:19:21.193646
# Unit test for function product
def test_product():
    from random import seed, random
    seed(1)
    for i in product(range(20), range(20), range(20),
                     tqdm_class=tqdm_auto):
        assert len(i) == 3
        assert min(i) == 0
        assert max(i) == 19
        assert 0.01 <= random() <= 0.9

# Generated at 2022-06-14 13:19:23.377054
# Unit test for function product
def test_product():
    for i in product(['a', 'b', 'c'], [1, 2], tqdm_class=None):
        pass
    assert i == ('c', 2)

# Generated at 2022-06-14 13:19:26.682818
# Unit test for function product
def test_product():
    for i in product([1, 2, 3],
                     # note: does not support more than 1 "elements" argument
                     ("foo", "bar", "baz"),  # noqa: E131
                     tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:19:32.331286
# Unit test for function product
def test_product():
    from .tests_itertools import product as tp

    for t in [tqdm_auto, tqdm_gui, tqdm_notebook]:
        for args in [('abc', 'def'),
                     (range(2), 'abc', range(3)),
                     (range(3), 'ab')]:
            list_a = list(tp(*args))
            list_t = list(t.product(*args))
            assert len(list_a) == len(list_t)
            assert len(list_a) == len(list(tp(*args)))
            assert list_a == list_t

# Generated at 2022-06-14 13:19:35.269820
# Unit test for function product
def test_product():
    res = list(product(range(4), repeat=2))
    assert (res[0] == (0, 0))
    assert (len(res) == 4 * 4)
    assert (res[-1] == (3, 3))

# Generated at 2022-06-14 13:19:41.968894
# Unit test for function product
def test_product():
    from .itertools import product
    assert list(product([3, 4], [5, 6])) == [
        (3, 5), (3, 6), (4, 5), (4, 6)]
    assert list(product(range(3), [3, 4])) == [(0, 3), (0, 4), (1, 3), (1, 4),
                                               (2, 3), (2, 4)]
    assert list(product('ab', [5, 6])) == [('a', 5), ('a', 6), ('b', 5),
                                           ('b', 6)]


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:19:48.738454
# Unit test for function product
def test_product():
    assert list(product("ABC", "123")) == [("A", "1"),
                                           ("A", "2"),
                                           ("A", "3"),
                                           ("B", "1"),
                                           ("B", "2"),
                                           ("B", "3"),
                                           ("C", "1"),
                                           ("C", "2"),
                                           ("C", "3")]