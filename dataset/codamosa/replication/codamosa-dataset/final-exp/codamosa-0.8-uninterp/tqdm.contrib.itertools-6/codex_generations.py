

# Generated at 2022-06-14 13:12:39.745781
# Unit test for function product
def test_product():
    """Test for function product"""
    from .testit import testit

    def checkit(iterables, total, rst):
        assert list(product(*iterables, total=total)) == rst

    checkit([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], None,
            [('a', '1'), ('a', '2'), ('a', '3'), ('a', '4'),
             ('b', '1'), ('b', '2'), ('b', '3'), ('b', '4'),
             ('c', '1'), ('c', '2'), ('c', '3'), ('c', '4'),
             ('d', '1'), ('d', '2'), ('d', '3'), ('d', '4')]
            )

# Generated at 2022-06-14 13:12:43.843548
# Unit test for function product
def test_product():
    """Test function product"""
    import numpy.random as r
    iterables = (r.randint(100, size=1000),) * 2
    iterable = product(*iterables)
    assert len(list(iterable)) == len(list(itertools.product(*iterables)))


if __name__ == "__main__":
    # Unit test
    test_product()

# Generated at 2022-06-14 13:12:49.973171
# Unit test for function product
def test_product():
    assert list(
        product(
            [0, 1], [0, 1], tqdm_class=tqdm_auto, desc="test_product", leave=True
        )
    ) == [(0, 0), (0, 1), (1, 0), (1, 1)]

    # Check for error if `len` doesn't work on a nested `itertools.product`
    gen = product(range(2), product(range(2), range(2)), tqdm_class=tqdm_auto)
    next(gen)
    next(gen)
    next(gen)
    next(gen)

# Generated at 2022-06-14 13:12:57.096295
# Unit test for function product
def test_product():
    """
    Test product() on a simple example
    """
    from .._tqdm import trange
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    pro_list = [i + j for i in list1 for j in list2]
    prod = product(list1, list2, tqdm_class=trange)
    assert list(prod) == pro_list

# Generated at 2022-06-14 13:13:03.341472
# Unit test for function product
def test_product():
    """Unit test for function product"""
    it = product('abcd', 'xy', tqdm_class=tqdm_auto)
    assert isinstance(it, tqdm_auto)
    assert list(it) == [('a', 'x'), ('a', 'y'),
                        ('b', 'x'), ('b', 'y'),
                        ('c', 'x'), ('c', 'y'),
                        ('d', 'x'), ('d', 'y')]

# Generated at 2022-06-14 13:13:13.933100
# Unit test for function product
def test_product():
    """Test function `product`."""
    assert list(product(range(3), repeat=3, tqdm_class=None)) == \
        list(itertools.product(range(3), repeat=3))
    assert list(product(range(3), repeat=3)) == \
        list(itertools.product(range(3), repeat=3))
    assert list(product((1, 2, 3), repeat=2)) == \
        list(itertools.product((1, 2, 3), repeat=2))
    assert list(product(('a', 1, (1, 2), []), repeat=5)) == \
        list(itertools.product(('a', 1, (1, 2), []), repeat=5))

# Generated at 2022-06-14 13:13:15.554951
# Unit test for function product
def test_product():
    a = range(10)
    b = list('abc')
    c = [True, False]
    for A in product(a, b, c):
        pass


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:13:20.721191
# Unit test for function product
def test_product():
    import numpy as np
    from numpy.testing import assert_array_equal
    N = 10
    iterables = [[1, 2, 3, 4], list('abcd'), np.arange(N)]
    ref = list(itertools.product(*iterables))
    val = list(tqdm.product(*iterables))
    assert_array_equal(ref, val)

# Generated at 2022-06-14 13:13:23.625577
# Unit test for function product
def test_product():
    for i in product((1, 2, 3), (4, 5, 6), tqdm_class=tqdm_auto):
        assert i

# Generated at 2022-06-14 13:13:32.437419
# Unit test for function product
def test_product():
    """
    Unit test for product
    """
    from ..tests import dummy_iterable

    for _ in range(5):
        for x in product(dummy_iterable((2, 3, 2)), repeat=2):
            pass
        for x in product(dummy_iterable((2, 3, 2)), dummy_iterable((2, 3, 2))):
            pass
    # use list to "consume" iterator
    assert list(product(dummy_iterable([3]))) == [(3,)]
    assert list(product(dummy_iterable([3]), repeat=0)) == []
    assert list(product(dummy_iterable([3]), repeat=1)) == [(3,)]
    assert list(product(dummy_iterable([3]), repeat=2)) == [(3, 3)]
    # test reusage


# Generated at 2022-06-14 13:13:39.787754
# Unit test for function product
def test_product():
    r = 0
    for p in product('abcd', 'xy', total=None):
        r += 1
    assert r == 24
    with tqdm_auto(unit='pair') as t:
        for p in product('abcd', 'xy', total=None, unit='pairs'):
            t.set_postfix(abcxy=p)
            r += 1
        assert r == 48

# Generated at 2022-06-14 13:13:43.605629
# Unit test for function product
def test_product():
    """ Unit tests for function product """
    assert set(product([1, 2, 3], [4, 5])) == set([(1, 4), (1, 5),
        (2, 4), (2, 5), (3, 4), (3, 5)])
    # TODO: write more tests

# Generated at 2022-06-14 13:13:49.935073
# Unit test for function product
def test_product():
    """Tests `itertools.product`"""
    for i in product('ABC', 'XYZ', tqdm_class=tqdm_auto):
        assert True
    for i in product('ABC', repeat=5, tqdm_class=tqdm_auto):
        assert True

# Generated at 2022-06-14 13:13:54.046802
# Unit test for function product
def test_product():
    from .tests_tqdm import with_setup, pretest_posttest, _range

    @with_setup(pretest_posttest)
    def test():
        # should display
        list(product(_range(100), tqdm_class=tqdm_auto))
        # should not display
        list(product(_range(100), tqdm_class=tqdm_auto, total=0))

    test()

# Generated at 2022-06-14 13:13:59.015992
# Unit test for function product
def test_product():
    from itertools import product
    assert list(product([1, 2, 3], [4, 5])) == list(tqdm_product([1, 2, 3], [4, 5]))
    assert list(product([1, 2, 3], [4, 5])) == list(tqdm_product([1, 2, 3], [4, 5], tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:14:04.272228
# Unit test for function product
def test_product():
    """Unit test for function product"""

    from . import Trange

    with Trange(1) as t:
        [i for i in product("abcdefghijklmnopqrstuvwxyz",
                            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                            "0123456789",
                            total=10)]
        assert t.n == 10
        assert t.total == 10

# Generated at 2022-06-14 13:14:12.980051
# Unit test for function product
def test_product():
    """Test function `product`."""
    assert (list(product(['a', 'b'], [1, 2]))
            == list(itertools.product(['a', 'b'], [1, 2])))
    assert (list(product(['a', 'b'], [1, 2], tqdm_class=tqdm_auto))
            == list(itertools.product(['a', 'b'], [1, 2])))
    assert (list(product(['a', 'b'], tqdm_class=tqdm_auto))
            == list(itertools.product(['a', 'b'])))

# Generated at 2022-06-14 13:14:20.188072
# Unit test for function product
def test_product():
    from numpy import random
    random.seed(0)
    for n_rows in [10, 100]:
        for n_cols in [3, 8]:
            for n_iters in [5, 50]:
                for n_streams in [1, 3]:
                    m = random.rand(n_rows, n_cols)
                    res = list(product(m, range(n_iters),
                                       tqdm_class=tqdm_auto, total=n_rows *
                                       n_cols * n_iters))
                    assert res == list(itertools.product(m, range(n_iters)))

# Generated at 2022-06-14 13:14:29.356927
# Unit test for function product
def test_product():
    from ..utils import format_sizeof
    from time import time
    from datetime import timedelta
    from numpy import product

    # With no total in kwargs
    p = product(range(1000), repeat=3)
    t = product(tqdm_auto(range(1000), leave=False), repeat=3)
    assert sum(p) == sum(t)

    # With total in kwargs
    p = product(range(1000), repeat=3)
    t = product(tqdm_auto(range(1000), leave=False), repeat=3, total=1000**3)
    assert sum(p) == sum(t)

    # With total in kwargs and dynamic total
    # See https://github.com/tqdm/tqdm/issues/412

# Generated at 2022-06-14 13:14:34.129943
# Unit test for function product
def test_product():
    """
    Unit test for function :func:`tqdm.itertools.product`.
    """
    from ..utils import closing, format_sizeof
    import tempfile
    with closing(tempfile.NamedTemporaryFile()) as tmpfile:
        for n in product(range(2),
                         range(100),
                         range(10000),
                         range(100000),
                         range(50000),
                         tqdm_class=tqdm_auto,
                         file=tmpfile) :
            pass
        tmpfile.seek(0)
        res = tmpfile.read()
        # test number of lines
        res = res.splitlines()
        assert len(res) == 2000000

# Generated at 2022-06-14 13:14:43.837656
# Unit test for function product
def test_product():
    from ..wrappers import _format_sizeof

    N = 10**6  # 1M
    # list(range(N))  # force to not be generator
    val = list(product(range(N), repeat=2))
    assert len(val) == N**2
    print(_format_sizeof(val))


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:14:52.916970
# Unit test for function product
def test_product():
    """Test for product"""
    import numpy as np
    from numpy.testing import assert_equal
    from tqdm import trange

    for A, B, C in zip(
            product(range(3), trange),
            product(range(3), total=3),
            product(range(3), tqdm=trange)):
        assert_equal(A, B)
        assert_equal(A, C)

    for A, B, C in zip(
            product(range(3), trange),
            product(range(3), total=3),
            product(range(3), tqdm=trange)):
        assert_equal(A, B)
        assert_equal(A, C)


# Generated at 2022-06-14 13:14:59.929539
# Unit test for function product
def test_product():
    from ._utils import _random_data
    from ._utils import _range

    data = _random_data()

    for t in [list, set, tuple]:
        l_data = t(data)
        assert (list(product(l_data, l_data))
                == list(itertools.product(l_data, l_data)))
        assert (list(product(l_data, l_data, repeat=3))
                == list(itertools.product(l_data, l_data, repeat=3)))
    assert (list(zip(*_range(len(data)**2)))
            == list(product(data, data)))


if __name__ == "__main__":
    from ._utils import _tee_data
    for i in product(_tee_data(4), repeat=4):
        pass

# Generated at 2022-06-14 13:15:03.565676
# Unit test for function product
def test_product():
    import sys
    mod = sys.modules[__name__]
    len_mod = len(mod)
    assert callable(product)
    p = product("AB", "12")
    assert hasattr(p, '__iter__')
    assert len(mod) == len_mod

# Generated at 2022-06-14 13:15:14.410457
# Unit test for function product
def test_product():
    """ Test tqdm's product function """
    from .utils import dec, byteunit, FakeTqdmFile


# Generated at 2022-06-14 13:15:17.286196
# Unit test for function product
def test_product():
    from numpy.testing import assert_equal

    with tqdm_auto(unit="unit") as t:
        assert_equal(list(product(range(2), range(2), tqdm=t)),
                     list(itertools.product(range(2), range(2))))

# Generated at 2022-06-14 13:15:19.493105
# Unit test for function product
def test_product():
    for i in product(range(5000), range(5000)):
        pass
    for i in product(range(5000), range(5000), tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:15:29.760499
# Unit test for function product
def test_product():
    """
    Test iterable-consuming function `product`,
    with known good inputs.
    """
    assert list(product(range(1), range(1))) == [(0, 0)]
    assert list(product(range(1), range(1), repeat=3)) == [(0, 0, 0)]
    assert list(product(range(3), repeat=2)) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Generated at 2022-06-14 13:15:40.846140
# Unit test for function product
def test_product():
    from .tqdm_test_cases import get_kwargs, tqdm_class, disc_it_class
    kwargs = get_kwargs()
    # Test first without tqdm
    it = product(disc_it_class(), **kwargs)
    assert next(it) == (1, 1)
    assert next(it) == (1, 2)
    assert next(it) == (1, 3)
    assert next(it) == (2, 1)
    assert next(it) == (2, 2)
    assert next(it) == (2, 3)
    # Test with tqdm
    it = product(disc_it_class(), tqdm_class=tqdm_class, **kwargs)
    assert next(it) == (1, 1)

# Generated at 2022-06-14 13:15:48.652543
# Unit test for function product
def test_product():
    from . import _deprecate_new_kwargs
    _deprecate_new_kwargs(product, "tqdm_class")

    with tqdm_auto() as t:
        tmp = list(product(range(1000), tqdm_class=tqdm_auto))
    assert tmp == list(itertools.product(range(1000)))
    assert t.n == len(tmp)

    with tqdm_auto() as t:
        tmp = list(product(range(10), range(100), tqdm_class=tqdm_auto))
    assert tmp == list(itertools.product(range(10), range(100)))
    assert t.n == len(tmp)


# Generated at 2022-06-14 13:16:08.803636
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from .tests import closing, closing_wrap_attr
    from .tests import islice, izip
    from .tests import StringIO
    from .tests import pytest_make_called_notifications

    def _test(n, k, **kwargs):
        test_input = list(range(n)) ** k
        t = product(test_input, tqdm_class=tqdm_auto)
        if kwargs:
            t.set_description("custom_desc")
        for i, e in izip(t, test_input):
            assert i == e
        called = pytest_make_called_notifications(t)
        if kwargs:
            assert t.desc == "custom_desc"
        assert t.total == n ** k

# Generated at 2022-06-14 13:16:15.813668
# Unit test for function product
def test_product():
    """
    Unit test for `product`.
    """
    import tqdm
    assert ([s1, s2] == list(product(s1, s2, tqdm_class=tqdm.tqdm))
            for s1, s2 in [('ABC', '123'), ('AB', '1234567890')])
    assert ([s1, s2] == list(product(s1, s2, tqdm_class=tqdm.tqdm))
            for s1, s2 in [('ABC', '123'), ('AB', '1234567890')])

# Generated at 2022-06-14 13:16:26.470215
# Unit test for function product
def test_product():
    """Unit test for function product"""
    import pytest
    from tqdm import tqdm
    # Basic tests
    assert list(product([1], repeat=2)) == [(1, 1)]
    assert list(product([1, 2], repeat=2)) == [(1, 1), (1, 2), (2, 1), (2, 2)]
    # Identity tests
    for i in range(5):
        # -- check_itertools
        it = product(*[
            range(j) for j in range(i + 1)], tqdm_class=None)
        assert list(it) == list(
            itertools.product(*[range(j) for j in range(i + 1)]))
        # -- check_auto
        it = product(*[range(j) for j in range(i + 1)])


# Generated at 2022-06-14 13:16:32.388406
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import sys
    result = list(product(range(3), range(3), tqdm_class=tqdm_auto,
                          file=sys.stdout))
    assert result == [(0, 0), (0, 1), (0, 2),
                      (1, 0), (1, 1), (1, 2),
                      (2, 0), (2, 1), (2, 2)]


# Generated at 2022-06-14 13:16:42.692950
# Unit test for function product
def test_product():
    """ Run unit tests for product. """
    from .tests import TqdmDeprecationWarning, close_to
    from .tqdm_tests_python2 import StringIO

    # Test regular usage
    out = StringIO()
    with tqdm_auto(['a', 'b'], file=out) as t:
        for i in product(['a', 'b'], ['1', '2']):
            t.update()
    close_to(t.total, 4)
    close_to(t.n, 4)
    assert (t.last_print_n == 4)

    # Test tuple
    with tqdm_auto(['a', 'b'], file=out) as t:
        for i in product(['a', 'b'], ['1', '2']):
            pass

# Generated at 2022-06-14 13:16:51.083899
# Unit test for function product
def test_product():
    """
    Test function product
    """
    import sys
    import subprocess

    # Prepare two lists of integers and one list of alphabets
    N = 200
    a = list(range(N//2))
    b = list(range(N))
    s = list('abcdefg')

    # Test if list comprehension of the two lists of integers is equal to `product`
    assert a*b == [a*b for a,b in product(a,b)]
    # Test if list comprehension of the list of alphabets is equal to `product`
    assert s == [c for c in product(s)]
    # Test if `product` raises error when string is passed as argument
    with pytest.raises(Exception):
        list(product('abc'))
    # Test if `product` does not raise error when str and

# Generated at 2022-06-14 13:16:56.900227
# Unit test for function product
def test_product():
    """Test `tqdm.itertools.product`"""
    from sys import version_info

    if version_info[:2] == (3, 3):
        # Test with repeated
        assert list(product(range(100), repeat=2)) == list(itertools.product(
            range(100), repeat=2))
        # Test without repeated
        assert list(product(range(100), range(100))) == list(itertools.product(
            range(100), range(100)))

# Generated at 2022-06-14 13:17:01.100819
# Unit test for function product
def test_product():
    from ..utils import chunkate
    for length in range(4):
        for chunk_size in range(4):
            l = list(range(length))
            assert length == sum(1 for _ in product(l, chunk_size=chunk_size))
            assert length == sum(1 for _ in product(l, tqdm_class=None,
                                                    chunk_size=chunk_size))
            assert length == sum(1 for _ in
                                 product(chunkate(l, chunk_size),
                                         tqdm_class=tqdm_auto,
                                         chunk_size=chunk_size))
            assert length == sum(1 for _ in product(l,
                                                    tqdm_class=tqdm_auto,
                                                    chunk_size=chunk_size))



# Generated at 2022-06-14 13:17:07.773862
# Unit test for function product
def test_product():
    """Unit test of product"""
    assert list(product([1, 2, 3], [4, 5])) == \
        [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
    assert list(product([1, 2, 3], repeat=2)) == \
        [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# Generated at 2022-06-14 13:17:16.116637
# Unit test for function product
def test_product():
    import numpy as np
    A = [range(3), range(3), range(3)]
    B = list(product(*A))

# Generated at 2022-06-14 13:17:22.522026
# Unit test for function product
def test_product():
    # product is a generator, so it cannot be tested
    pass

# Generated at 2022-06-14 13:17:27.962709
# Unit test for function product
def test_product():
    assert list(product(["", "1", "12"], repeat=2)) == [
        ('', ''),
        ('', '1'),
        ('', '12'),
        ('1', ''),
        ('1', '1'),
        ('1', '12'),
        ('12', ''),
        ('12', '1'),
        ('12', '12')]

if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:17:36.000397
# Unit test for function product
def test_product():
    from .tests.test_tqdm_itertools import TestProduct
    from .tests.test_tqdm import with_setup, _range

    for T in [tqdm_auto, TestProduct]:
        # Used to prevent "too many files open"
        with_setup(TestProduct.setup, TestProduct.teardown)
        with T(10) as t:
            T.write = t.write
            T.flush = t.flush
            assert t.total == 10
            assert not t.disable
            product(range(3), range(3), range(3),
                    tqdm_class=T)
            # test reset
            product(range(3), range(3), range(3),
                    tqdm_class=T)
            assert t.n == 9

            t.total = None

# Generated at 2022-06-14 13:17:44.185927
# Unit test for function product
def test_product():
    """Test product wrapping"""
    from pytest import raises
    # Very basic test
    saved_stdout = None
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO

    with tqdm_auto.__test__.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        for i, j in product(range(2), range(4)):
            pass
        assert mock_stdout.getvalue() == "\r|0/8 [00:00<?, ?it/s]\r|1/8 [00:00<?, ?it/s]"


# Generated at 2022-06-14 13:17:54.439332
# Unit test for function product
def test_product():
    """ Unit test for function product """
    kwargs = dict(tqdm_class=tqdm_auto.tqdm)
    assert list(product(range(3), repeat=2, **kwargs)) == \
        [(i, j) for i in range(3) for j in range(3)]
    assert list(product(range(3), range(3), **kwargs)) == \
        [(i, j) for i in range(3) for j in range(3)]
    # Test `total`.
    assert list(product(range(3), range(3), tqdm_class=tqdm_auto.tqdm)) == \
        [(i, j) for i in range(3) for j in range(3)]

# Generated at 2022-06-14 13:18:00.522922
# Unit test for function product
def test_product():
    "Testing function product()"
    
    l = ['a', 'b', 'c']
    r = [1, 2, 3]
    
    try:
        import numpy as np
    except ImportError:
        answer = list(itertools.product(l, r))
    else:
        answer = np.array(list(itertools.product(l, r)))
    
    for i, x in enumerate(product(l, r, tqdm_class=tqdm_auto)):
        assert answer[i] == x
        assert hasattr(x, '__iter__')

# Generated at 2022-06-14 13:18:03.526152
# Unit test for function product
def test_product():
    import io
    import sys
    out = io.BytesIO()
    sys.stdout = out
    for i in product(range(10), range(5)):
        pass
    sys.stdout = sys.__stdout__
    assert "100%" in out.getvalue().decode()

# Generated at 2022-06-14 13:18:10.541705
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import types
    import sys

    if sys.version_info[0] == 3:
        import io as StringIO
    else:
        import StringIO
    tqdm_test = StringIO.StringIO()
    itr = product(range(3), range(3), range(3), tqdm_class=tqdm_auto,
                  file=tqdm_test)
    assert '{:.2f}'.format(next(itr)[0]) in tqdm_test.getvalue()

# Generated at 2022-06-14 13:18:14.629772
# Unit test for function product
def test_product():
    """Unit test for `itertools.product`."""
    # Unit test for function product
    [_ for _ in product(range(10), range(10), range(10),
                        tqdm_class=tqdm_auto)]

# Generated at 2022-06-14 13:18:22.964151
# Unit test for function product
def test_product():
    import numpy as np
    assert (list(product(range(10), range(10), range(10)))
            == list(itertools.product(range(10), range(10), range(10))))
    assert (list(product(range(5), range(5), range(5)))
            == list(itertools.product(range(5), range(5), range(5))))
    n = 100
    arraylist = [np.arange(n) for i in range(5)]

# Generated at 2022-06-14 13:18:31.421682
# Unit test for function product
def test_product():
    with tqdm_auto(total=10, unit='foo') as t:
        for _ in product(range(3), range(3), tqdm_class=tqdm_auto):
            t.update()

# Generated at 2022-06-14 13:18:34.844611
# Unit test for function product
def test_product():
    it = product('ABC', [1, 2])
    assert list(it) == [(a, b) for a in 'ABC' for b in [1, 2]]

    it = product('ABC', [1, 2], tqdm_class=lambda x: x, total=None)
    assert list(it) == [(a, b) for a in 'ABC' for b in [1, 2]]

# Generated at 2022-06-14 13:18:40.351624
# Unit test for function product
def test_product():
    from .itertools import test_itertools
    for total, *leftovers in test_itertools:
        for tqdm_class in [tqdm_auto]:
            for i in product(*leftovers, tqdm_class=tqdm_class):
                pass


# Generated at 2022-06-14 13:18:49.137821
# Unit test for function product
def test_product():
    """
    Doctest for itertools.product.
    """
    from collections import Counter
    from random import random
    with tqdm_auto(unit='', leave=False, disable=True) as trange:
        for i in trange(2, 10, 2):
            for _ in product(range(2),
                             repeat=i,
                             tqdm_class=tqdm_auto):
                pass
            for _ in product(range(2),
                             repeat=i,
                             tqdm_class=tqdm_auto,
                             unit='cm'):
                pass
            for _ in product(range(2),
                             repeat=i,
                             tqdm_class=tqdm_auto,
                             unit_scale=True,
                             unit='cm'):
                pass

# Generated at 2022-06-14 13:18:57.171436
# Unit test for function product
def test_product():
    """Test function product."""
    import numpy as np
    import warnings
    try:
        import scipy
        import scipy.sparse
        sparse = True
    except ImportError:
        sparse = False

    from ..utils import numpy, PY36
    numpy.random.seed(12345)

    for remove in (False, True):
        for N in (3, 5):
            for m in range(N + 1):
                for n in range(N + 1):
                    for vmax in (None, 1, 1.5, 2):
                        for sparse in (False, True):
                            if sparse:
                                # LIL is fastest to iterate over
                                a = numpy.random.randint(0, vmax, size=(m, n))
                                A = scipy.sparse

# Generated at 2022-06-14 13:19:06.893099
# Unit test for function product
def test_product():
    from .__init__ import tnrange, trange
    from .tests import TRAVIS, PY3

    # regular test
    for i in product("AB", range(3), tqdm_class=tqdm_auto):
        break

    # test, "total=unknown"
    for i in product("AB", tqdm_class=tqdm_auto, total=None):
        break

    # test, known total
    for i in product("AB", range(3), tqdm_class=tqdm_auto, total=6):
        break

    # test, known total, update
    for i in product("AB", range(3), tqdm_class=tqdm_auto, total=6):
        break

    # test nested tqdm

# Generated at 2022-06-14 13:19:16.137601
# Unit test for function product
def test_product():
    # Testing with a class with __len__
    class A(object):
        def __len__(self):
            return 3

# Generated at 2022-06-14 13:19:24.899411
# Unit test for function product
def test_product():
    import random
    import string

    for t in (tqdm, tqdm_gui, tqdm_notebook):
        assert [x for x in t.product("ABCD", repeat=2)] == list(
            itertools.product("ABCD", "ABCD"))
        assert [x for x in t.product("ABCD", repeat=3)] == list(
            itertools.product("ABCD", "ABCD", "ABCD"))
        assert [x for x in t.product("ABCD", repeat=4)] == list(
            itertools.product("ABCD", "ABCD", "ABCD", "ABCD"))

# Generated at 2022-06-14 13:19:32.487472
# Unit test for function product
def test_product():
    FORMAT = '%s\t' * 3

    def check(iterables, expected):
        with tqdm_auto(unit='B') as t:
            out = list(product(*iterables, tqdm_class=t.__class__))
        assert out == expected, FORMAT % (out, expected, iterables)

    check([], [()])
    check([[]], [()])
    check([[], []], [()])
    check([[1, 2], [3, 4], [5, 6]],
          [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6),
           (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)])

# Generated at 2022-06-14 13:19:40.605942
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    # Test default total=None
    a = list(product([1, 2], [3, 4]))
    assert a == [(1, 3), (1, 4), (2, 3), (2, 4)]
    # Test total
    b = list(product([1, 2], [3, 4], tqdm_class=tqdm_auto, total=None))
    assert a == b

    # Test default total=None
    a = list(product([1, 2], [3, 4], [5, 6]))

# Generated at 2022-06-14 13:19:55.711726
# Unit test for function product
def test_product():
    import pandas as pd
    for i, j in tqdm_auto.itertools.product(range(10), range(10)):
        assert (i, j) == (i, j)



# Generated at 2022-06-14 13:19:57.851110
# Unit test for function product
def test_product():
    """Test that imap behaves the same as map"""
    def _test():
        yield 2
        yield 2
        raise ValueError()

    assert list(product([2], _test(), tqdm_class=None)) == [(2, 2, 2)]

# Generated at 2022-06-14 13:20:03.607958
# Unit test for function product
def test_product():
    "Test function product"
    test_list = [0, 1]
    test_size = 0
    for i in product(test_list, test_list, test_list, test_list):
        assert len(i) == 4
        test_size += 1
    assert test_size == min(16, test_list)

# Generated at 2022-06-14 13:20:10.377971
# Unit test for function product
def test_product():
    """Unit test for function `product`."""
    # Test exceptions
    try:
        for _ in product(2, 3):
            pass
    except TypeError:
        pass
    else:
        raise AssertionError("product did not raise a TypeError")

    # Test callback
    def callback(bar):
        bar.update(1)
    for _ in product(range(4), tqdm_class=callback):
        pass

    # Test basic operation
    ret = product(range(5), range(5))
    assert list(ret) == list(itertools.product(range(5), range(5)))

# Generated at 2022-06-14 13:20:17.410291
# Unit test for function product
def test_product():
    import numpy as np
    from numpy.testing import assert_array_equal
    from .tqdm_pandas import tqdm_pandas
    from .tqdm_gui import tqdm_gui

    for tqdm_class in [tqdm_gui, tqdm_auto, tqdm_pandas]:
        a = np.array([1, 2], int)
        b = np.array([10, 20], int)
        c = np.array([100, 200], int)
        d = np.array([1000, 2000], int)
        # product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

# Generated at 2022-06-14 13:20:26.393399
# Unit test for function product
def test_product():
    """
    Unit test for `tqdm.py` (`tqdm(*, total=None, tqdm_class=tqdm.auto.tqdm)`).
    """
    try:
        input = xrange(100)  # Python 2
    except NameError:
        input = range(100)   # Python 3
    r = product(input, input, 'abc', ['a', 'b', 'c'])
    assert len(list(r)) == 100 ** 3 * 3
    r = product(input, input, 'abc', ['a', 'b', 'c'],
                tqdm_class=tqdm_auto.tqdm)
    assert len(list(r)) == 100 ** 3 * 3


# Aliases
# NOTE: Avoid circular imports (``from . import trange``) if possible


# Generated at 2022-06-14 13:20:36.387691
# Unit test for function product
def test_product():
    from numpy.testing import assert_equal
    from nose.tools import assert_not_equal

    n = 5
    tqdm_kwargs = dict(tqdm_class=tqdm_auto)
    for i, j in product(range(n), range(n), **tqdm_kwargs):
        assert_not_equal(i, j)
    for i, j in product(range(n), **tqdm_kwargs):
        assert_equal(i, j)
    for i, j in product(range(n), range(1, n), **tqdm_kwargs):
        assert_not_equal(i, j)

if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:20:45.807989
# Unit test for function product
def test_product():
    '''Test for itertools.product'''
    from .main import _range
    from .main import _zip
    from .main import _map

    assert list(product(_range(2), _range(3), _range(2))) == \
        [(0, 0, 0),
         (0, 0, 1),
         (0, 1, 0),
         (0, 1, 1),
         (0, 2, 0),
         (0, 2, 1),
         (1, 0, 0),
         (1, 0, 1),
         (1, 1, 0),
         (1, 1, 1),
         (1, 2, 0),
         (1, 2, 1)]


# Generated at 2022-06-14 13:20:48.940990
# Unit test for function product
def test_product():
    """Test the `product` wrapper."""
    it = product(range(3), range(3), range(3))
    assert len(list(it)) == 27

    it = product(range(3), range(3), range(3),
                 tqdm_class=tqdm_auto.tqdm_gui, leave=False)
    assert len(list(it)) == 27

if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:20:53.124812
# Unit test for function product
def test_product():
    with tqdm_auto(unit=" char", desc="testing") as t:
        for i in product(list(range(2)), list(range(2)), list(range(2)),
                         list(range(2)), tqdm_class=tqdm_auto):
            assert isinstance(i, tuple)