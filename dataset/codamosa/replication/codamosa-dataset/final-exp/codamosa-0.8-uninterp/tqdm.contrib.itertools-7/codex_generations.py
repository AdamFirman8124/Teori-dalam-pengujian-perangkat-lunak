

# Generated at 2022-06-14 13:12:42.191150
# Unit test for function product
def test_product():
    from .tests import closing, mock

    with closing(mock.MagicMock()) as t:
        for _ in product("ab", "cdef", total=100, desc="test", tqdm_class=t):
            pass
        t.assert_called_with("test", total=100)
        assert t.return_value.write.call_count == 24

# Generated at 2022-06-14 13:12:51.751893
# Unit test for function product
def test_product():
    from .tests import TestCase, closing
    from .utils import FormatCustom as fc

    with closing(TestCase()) as tc:

        with tqdm_auto(run=False) as t:
            tc.assertEqual(list(product(['red', 'green'], range(2),
                                        tqdm=t)),
                           [('red', 0), ('red', 1), ('green', 0),
                            ('green', 1)])
            tc.assertTrue(t.total == 4)
            tc.assertEqual(t.format_dict, fc.get_format_dict(
                'red/2|green/2', pos=1, len=4, rate=0, rate_fmt=''))

        with tqdm_auto(run=False, total=8) as t:
            tc.assertE

# Generated at 2022-06-14 13:13:04.298847
# Unit test for function product
def test_product():
    from .utils import FormatMixin

    class Test(FormatMixin):
        def test_basic(self):
            """
            Basic `product` usage.
            """
            a = range(3)
            b = range(2)
            c = range(4)
            counter = 0
            total = 0
            for cnt, x in enumerate(product(a, b, c)):
                self.to_str(x)
                counter += 1
                total += x[0] * x[1] * x[2]
            assert counter == len(a) * len(b) * len(c)
            assert total == (len(a) * (len(a) - 1) * len(b) * len(c) *
                             (len(c) - 1) * (len(c) - 2)) / 6



# Generated at 2022-06-14 13:13:08.861609
# Unit test for function product
def test_product():
    from math import factorial
    assert sum(1 for _ in product(
        range(2), range(2), range(2), range(2), range(2),
        tqdm_class=tqdm_auto)) == factorial(6)

# Generated at 2022-06-14 13:13:16.623803
# Unit test for function product
def test_product():

    import numpy as np

    for i in product(range(10), range(5), range(2), tqdm_class=tqdm_auto):
        pass
    np.testing.assert_equal(i, (9, 4, 1))
    np.testing.assert_equal(i, (9, 4, 1))

    i = None
    for i in product(range(10), range(5), range(2), tqdm_class=tqdm_auto):
        pass
    np.testing.assert_equal(i, (9, 4, 1))
    np.testing.assert_equal(i, (9, 4, 1))

# Generated at 2022-06-14 13:13:28.870331
# Unit test for function product
def test_product():
    from .tests_tqdm import with_setup, _range, pretest_posttest

    @with_setup(pretest_posttest)
    def product_test_1():
        from random import randint as ri, random as rf

        for _ in product(_range(10), repeat=5, desc="1", leave=False):
            assert 1 == 1, "unexpected iteration"

        for i in product(_range(10), repeat=5,
                         miniters=1, mininterval=0,
                         desc="1", leave=False):
            assert 1 == 1, "unexpected iteration"
            if ri(1, 20) == 1:
                break


# Generated at 2022-06-14 13:13:39.467358
# Unit test for function product
def test_product():
    from .misc import IS_PYPY
    import numpy as np

    for i in product(range(1000), repeat=3):
        pass
    for i in product(range(100), range(100), range(100)):
        pass
    for i in product(range(100), range(100), range(100)):
        pass
    with tqdm_auto(unit="B", unit_scale=True, miniters=1) as t:
        for i in product(range(1000), repeat=3):
            t.update(123)
    with tqdm_auto(unit="B", unit_scale=True, miniters=1, smoothing=1) as t:
        for i in product(range(1000), repeat=3):
            t.update(123)

# Generated at 2022-06-14 13:13:47.454533
# Unit test for function product
def test_product():
    import gc
    from copy import copy
    from operator import mul
    from itertools import accumulate

    so_large = 1e4  # Large enough for PyPy to not rely on iter to create a list
    so_small = 100  # Small enough for all Python versions to use a list, even PyPy

    def check(p, n):
        """
        Checks that product(range(n), ..., range(n)) has len(p) elements,
        and that they are all in the range(n)² set.
        """
        c = accumulate(p, mul)  # product(range(n), ..., range(n)) length
        assert c == n ** n
        s = set(p)
        assert len(s) == c
        assert s == set(range(n))


# Generated at 2022-06-14 13:13:56.074328
# Unit test for function product
def test_product():
    """Test product()."""
    from .utils import StripIO
    import sys
    import io
    import sys
    import random

    # Test internals
    assert sum(1 for _ in product([1, 2, 3], [4, 5, 6])) == 9
    assert sum(1 for _ in product([1, 2, 3], [4, 5, 6])) == 9
    assert sum(1 for _ in product([1, 2, 3], [4])) == 3
    assert sum(1 for _ in product([1], [4, 5, 6])) == 3
    assert sum(1 for _ in product([1], [4])) == 1
    assert sum(1 for _ in product([], [4])) == 0

# Generated at 2022-06-14 13:14:05.608069
# Unit test for function product
def test_product():
    from random import random
    from collections import namedtuple
    from itertools import product as itertools_product
    from ..utils import FormatCustomText
    T = namedtuple("T", ["a", "b", "x", "y", "z"])

    for tqdm_class in [tqdm_auto, FormatCustomText(desc="Test", ascii=True)]:
        p0 = product([1, 2, 5], [1, 6], [0, 2], tqdm_class=tqdm_class)
        p1 = product([1, 2, 5], [1, 6], [0, 2], tqdm_class=tqdm_class,
                     ascii=False)
        p2 = itertools_product([1, 2, 5], [1, 6], [0, 2])


# Generated at 2022-06-14 13:14:15.769130
# Unit test for function product
def test_product():
    """
    Unit test
    """
    assert list(product([1, 2, 3], [4, 5], [6, 7])) == [
        (1, 4, 6), (1, 4, 7), (1, 5, 6), (1, 5, 7),
        (2, 4, 6), (2, 4, 7), (2, 5, 6), (2, 5, 7),
        (3, 4, 6), (3, 4, 7), (3, 5, 6), (3, 5, 7)]


if __name__ == "__main__":
    from . import main
    main(__file__)

# Generated at 2022-06-14 13:14:18.924817
# Unit test for function product
def test_product():
    try:
        from .tqdm_gui import tqdm
    except ImportError:
        from .tqdm import tqdm
    for _ in range(5):
        for _ in product(range(10), range(10), tqdm_class=tqdm):
            pass

# Generated at 2022-06-14 13:14:28.099741
# Unit test for function product
def test_product():
    """
    Test a few things about the product function.
    - Total count is correct
    - Position of 'out' is correct
    - The `tqdm` bar works
    - The `tqdm` bar works even when total is None
    - The `tqdm_class` kwarg works
    - `total` kwarg works
    """
    import sys
    import math
    from unittest import TestCase
    from tqdm import tqdm as tqdm_lib

    class mock_tqdm(tqdm_lib):
        def __init__(self, *args, **kwargs):
            self.total = kwargs['total'] if 'total' in kwargs else None
            self.count = 0

        def update(self, count=1):
            self.count += count


# Generated at 2022-06-14 13:14:36.570040
# Unit test for function product
def test_product():
    """
    Unit test of function product
    """
    import numpy as np

    # Test without total
    it = product(range(2), range(2), range(2), tqdm_class=tqdm_auto)
    assert type(it).__name__ == "tqdm_wrapper"
    assert list(it) == list(itertools.product(range(2), range(2), range(2)))

    # Test with total
    it = product(range(2), range(2), range(2), total=8, tqdm_class=tqdm_auto)
    assert type(it).__name__ == "tqdm_wrapper"
    assert list(it) == list(itertools.product(range(2), range(2), range(2)))

    # Test with automatic total
    it = product

# Generated at 2022-06-14 13:14:44.484593
# Unit test for function product
def test_product():
    """Test function product"""
    assert list(product(range(2), repeat=4)) == list(itertools.product(range(2), repeat=4))
    assert list(product(range(3))) == list(itertools.product(range(3)))
    assert list(product(range(2), range(3))) == list(itertools.product(range(2), range(3)))
    assert list(product(range(2), [])) == list(itertools.product(range(2), []))
    assert list(product(range(2), "a")) == list(itertools.product(range(2), "a"))

# Generated at 2022-06-14 13:14:53.084646
# Unit test for function product
def test_product():
    import numpy as np

# Generated at 2022-06-14 13:14:58.023296
# Unit test for function product
def test_product():
    from contextlib import suppress

    with suppress(ModuleNotFoundError):
        from tqdm import tqdm_gui as tqdm

    from .tests_tqdm import pretest_posttest_noloop

    for kwargs in [{}, {'leave': True, 'smoothing': 0}]:
        for args in [['ABC', range(4)]]:
            pretest_posttest_noloop(product, args=args, kwargs=kwargs,
                                    progress_bar=(tqdm, {'disable': False}))

# Generated at 2022-06-14 13:15:04.835927
# Unit test for function product
def test_product():
    """Test for product"""
    import numpy as np

    for i in product([1, 2, 3], range(10), "abc"):
        # print(i)
        pass

    def pbar(iterable):
        return product(iterable, tqdm_class=tqdm_auto.tqdm, leave=False)

    for i in pbar([1, 2, 3, 4, 5]):
        pass

    for i in pbar(range(10)):
        pass

    for i in pbar(np.linspace(0, 1, 100)):
        pass

# Generated at 2022-06-14 13:15:15.468565
# Unit test for function product
def test_product():
    import operator
    import functools

    def list_product(arrays):
        return list(product(*arrays))

    def prod(iterable):
        return functools.reduce(operator.mul, iterable, 1)

    def combinations(arrays):
        """Generate all the combinations of the elements in arrays.
        For example, arrays = [[1, 2], ['a', 'b']] would yield
        (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')
        """
        arrays = [list(x) for x in arrays]
        num_arrays = len(arrays)
        num_elements = [len(x) for x in arrays]

# Generated at 2022-06-14 13:15:26.212911
# Unit test for function product
def test_product():
    from .main import tqdm_pandas
    from .main import tqdm_notebook

    tqdm_kwargs = {"leave": False, "ascii": True}

    n_columns_i, n_columns_r = 0, 0
    for tqdm_class in [tqdm_auto, tqdm_pandas.tqdm_pandas,
                       tqdm_notebook.tqdm_notebook]:
        for n_columns in range(1, 4):
            iterables = [range(10) for _ in range(n_columns)]
            for _ in product(*iterables, tqdm_class=tqdm_class,
                             **tqdm_kwargs):
                n_columns_i += 1
                n_columns_r += n

# Generated at 2022-06-14 13:15:41.823570
# Unit test for function product
def test_product():
    import sys
    from .utils import StringIO
    from .main import TqdmKeyError

    with StringIO() as our_file:
        for _ in product(range(3), repeat=2, file=our_file):
            pass

# Generated at 2022-06-14 13:15:51.022628
# Unit test for function product
def test_product():
    from .main import trange
    from .utils import FormatCustomText

    total = 1
    lens = []
    for i in range(10, 1, -2):
        lens.append(i)
        total *= i

    # Test all possible environments

# Generated at 2022-06-14 13:16:00.559881
# Unit test for function product
def test_product():
    """
        Unit test for function product
        Will not work if the itertools import fails
    """
    from .tqdm_gui import trange
    from .tqdm_pandas import tqdm_pandas
    from .tqdm import tqdm

    for k in [tqdm, trange, tqdm_pandas]:
        for n in [None, 42, 'foo']:
            for i in [1, 2, 3]:
                for j in [1, 2, 3]:
                    out = list(product("abcde", repeat=i, tqdm_class=k, total=n))
                    assert len(out) == 5 ** i
                    out = list(product("abcde", "ABCDE", repeat=j, tqdm_class=k))
                    assert len(out) == 5

# Generated at 2022-06-14 13:16:11.114106
# Unit test for function product
def test_product():
    import numpy as np
    try:
        import hypothesis
        hypothesis  # workaround for flake8 issue #1344
    except ImportError:
        return
    try:
        with tqdm_auto.disable:
            assert (list(product(range(5), repeat=5, tqdm_class=None))
                    == list(itertools.product(range(5), repeat=5)))
    except hypothesis.errors.InvalidArgument:
        # hypothesis >= 3.11.0
        pass
    for tqdm_class in (tqdm_auto, tqdm_auto.tqdm, tqdm_auto.tqdm_gui, None):
        # Special cases
        with tqdm_auto.disable:
            assert list(product([], tqdm_class=tqdm_class)) == [()]

# Generated at 2022-06-14 13:16:18.409027
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    assert list(product(
        range(10),
        tqdm_class=None)) == list(
            itertools.product(range(10)))
    try:
        from IPython.lib.pretty import pretty  # NOQA
    except ImportError:
        pass
    else:
        with tqdm_auto(range(10), leave=False) as t:
            for _ in product(range(100), tqdm=t):
                pass

# Generated at 2022-06-14 13:16:29.278131
# Unit test for function product
def test_product():
    "Test function product"
    inputs = range(10), range(1, 10), range(2, 10), range(3, 10)
    # test identity
    assert list(product(*inputs)) == list(itertools.product(*inputs))
    # test progress bar
    outputs = []
    for _ in product(*inputs,
                     tqdm_class=tqdm_auto.tqdm_gui,
                     desc="test_product()"):
        outputs.append(_)
    assert outputs == list(itertools.product(*inputs))
    # test iteration stop
    for _ in product(*inputs, tqdm_class=tqdm_auto.tqdm_gui):
        if _ == (9, 8, 7, 6):
            break
    assert _ == (9, 8, 7, 6)

# Generated at 2022-06-14 13:16:35.404112
# Unit test for function product
def test_product():
    from . import setup_class

    test_product = False
    # test_product = True
    if test_product:
        with setup_class(leave=False) as t:
            for _i in product('abcdefghijklm', repeat=2,
                              tqdm_class=t.tqdm_class):
                pass
            t.assert_eq(t.t.dynamic_messages,
                        [
                            'a|b',
                            'c|d',
                            'e|f',
                            'g|h',
                            'i|j',
                            'k|l',
                        ])

# Generated at 2022-06-14 13:16:40.158350
# Unit test for function product
def test_product():
    for args in [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]],
            [
                range(3),
                range(4),
                range(5),
                range(6)]]:
        assert list(product(*args)) == list(itertools.product(*args))

# Generated at 2022-06-14 13:16:44.459257
# Unit test for function product
def test_product():
    from ..utils import EnsureIterableEqual
    EnsureIterableEqual(
        tqdm(
            product('ABCD', 'xy', tqdm_class=tqdm_gui),
            tqdm_class=tqdm_gui,
        ),
        itertools.product('ABCD', 'xy'),
    )

# Generated at 2022-06-14 13:16:52.694573
# Unit test for function product
def test_product():
    """Unit test for product"""
    from ..utils import format_sizeof
    n = 10
    list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    c = itertools.product(*list_of_list)
    for _ in tqdm_auto(c):
        pass
    c = product(*list_of_list)
    for _ in tqdm_auto(c):
        pass
    c = product(*list_of_list, desc="Looping")
    for _ in tqdm_auto(c):
        pass
    c = product(*list_of_list, desc="Looping", leave=True)
    for _ in tqdm_auto(c):
        pass

# Generated at 2022-06-14 13:17:02.456483
# Unit test for function product
def test_product():
  iterables = [[0, 1], [0, 1]]
  res = product(*iterables, total=2)
  assert list(res) == [(0, 0), (1, 0), (0, 1), (1, 1)]

# Generated at 2022-06-14 13:17:07.613177
# Unit test for function product
def test_product():
    from .utils import closing
    from ..auto import tqdm
    with closing(tqdm(["a", "b", "c"])) as t:
        assert list(product(t, [1, 2])) == [
            ("a", 1), ("a", 2), ("b", 1), ("b", 2), ("c", 1), ("c", 2)
        ]

# Generated at 2022-06-14 13:17:12.944257
# Unit test for function product
def test_product():
    """Test function `product`"""
    import numpy as np
    from ..utils import RunningStats

    rs = RunningStats()
    for i in product(np.arange(20), np.arange(100), tqdm_class=tqdm_auto):
        rs.push(i)
    assert rs.popcount == 2000

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:17:14.715360
# Unit test for function product
def test_product():
    for i in product(range(100), range(100), range(100),
                     tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:17:20.526510
# Unit test for function product
def test_product():
    # https://github.com/tqdm/tqdm/issues/636
    import io
    from .utils import disc_move
    from .tests import TestCase
    with disc_move(TestCase) as td:
        # test tqdm_class argument
        td.write("test_product_a.txt", "")
        with io.open("test_product_a.txt", "r", encoding="utf-8") as f:
            it = product(range(7), tqdm_class=tqdm_auto,
                         file=f, desc="testing product")
            assert list(it) == list(itertools.product(range(7)))
        # test total argument
        td.write("test_product_b.txt", "")

# Generated at 2022-06-14 13:17:30.076147
# Unit test for function product
def test_product():
    """test function product() against itertools.product for some cases"""
    # Basic tests
    # only one iterable
    assert list(product(range(5))) == list(itertools.product(range(5)))
    # multiple iterables
    assert list(product(range(5), range(5), range(5))) == \
        list(itertools.product(range(5), range(5), range(5)))
    # empty iterable
    assert list(product()) == list(itertools.product())
    # 1d iterables
    assert list(product(range(5))) == list(itertools.product(range(5)))

    # Advanced input, empty iterable

# Generated at 2022-06-14 13:17:35.272275
# Unit test for function product
def test_product():
    from numpy import prod as np_prod
    from numpy.random import randint
    for n in range(4):
        a = randint(1, 4, size=n)
        b = randint(1, 4, size=n)
        prod = product(a, b)
        prod = list(prod)
        assert prod == [(a[i], b[i]) for i in range(n)]
        assert len(prod) == np_prod(a) * np_prod(b)

# Generated at 2022-06-14 13:17:42.474169
# Unit test for function product
def test_product():
    """Equivalent of `itertools.product`"""
    from ..std import numpy
    numpy.random.seed(0)
    nums = numpy.random.randint(0, 5, size=[10])
    prods = list(product(nums))
    nums.sort(kind='mergesort')
    val = numpy.array([numpy.array(p) for p in
                       itertools.product(*[nums] * 10)])
    val.sort(kind='mergesort', axis=0)
    assert numpy.all(val == prods)


if __name__ == "__main__":
    from .. import __main__ as main
    main.main()

# Generated at 2022-06-14 13:17:46.491791
# Unit test for function product
def test_product():
    from .._tqdm import trange, tqdm
    a = product(trange(5), repeat=2, tqdm_class=tqdm)
    assert list(a) == [(i, j) for i in range(5) for j in range(5)]

# Generated at 2022-06-14 13:17:55.836067
# Unit test for function product
def test_product():
    from .utils import TestCase

    class TestProduct(TestCase):
        def test_range(self):
            list_ = [range(3), range(5)]
            expected_result = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                               (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]
            self.assertEqual(list(product(*list_)), expected_result)

        def test_empty(self):
            list_ = []
            expected_result = [()]
            self.assertEqual(list(product(*list_)), expected_result)


# Generated at 2022-06-14 13:18:17.241327
# Unit test for function product
def test_product():
    import sys

    # Functional
    assert list(product(['a', 'b'], repeat=2)) == [
        ('a', 'a'), ('b', 'a'), ('a', 'b'), ('b', 'b')]

    # Coverage
    assert list(product(['a', 'b'], repeat=0)) == [()]
    assert list(product(['a', 'b'], repeat=-1)) == []

    list(product(['a', 'b'], repeat=2, tqdm_class=None))
    with tqdm_auto(disable=True) as t:
        assert not t.disable

    # Correctness
    p = product([1, 2, 3], repeat=2, tqdm_class=tqdm_auto)
    assert not tqdm_auto._instances

    assert p.__

# Generated at 2022-06-14 13:18:21.230825
# Unit test for function product
def test_product():
    """Unit test for product"""
    assert list(product([1, 2],
                        [5, 6],
                        [9, 8, 7],
                        total=24,
                        miniters=1,
                        mininterval=0.1)) ==\
        list(itertools.product([1, 2],
                               [5, 6],
                               [9, 8, 7]))

# Generated at 2022-06-14 13:18:30.900928
# Unit test for function product
def test_product():
    from .utils import FormatMixin
    from .tests_tqdm import pretest_posttest_stuff

    class Append(FormatMixin):
        def __init__(self, cnt=None):
            self.cnt = cnt
            self.dynamic_messages = ['msg{}'.format(i) for i in range(10)]
            self.set_description('description')

        def get_result(self):
            if self.cnt is None:
                return self.dynamic_messages.pop()
            else:
                return self.dynamic_messages[self.cnt]

        def __iter__(self):
            yield 'a'

    def check_product(cnt=None):
        expected = Append(cnt).get_result()
        a = Append(cnt)
       

# Generated at 2022-06-14 13:18:40.160157
# Unit test for function product
def test_product():
    import random
    # get the same random numbers as in `test_itertools_test`
    random.seed(8921)
    sizes = [random.randint(1, 3) for i in range(10)]
    # basic unit test
    assert list(product(*[range(1)] * 2)) == [
        (0, 0), (0, 1), (1, 0), (1, 1)]
    # medium unit test
    assert sizes == list(map(len, list(product(*[range(4)] * 10))))
    assert sizes == list(map(len, list(product({0: 5}) * 10)))
    # test total (should be the same as no total)
    assert sizes == list(map(len, list(
        product({0: 5}, total=1) * 10)))

# Generated at 2022-06-14 13:18:45.261693
# Unit test for function product
def test_product():
    from .tests import common_kwargs, closing_attr, wrapped_fp_write_clean
    for kwargs in common_kwargs:
        for total in [9999, None]:
            with closing_attr(tqdm_auto) as fp:
                list(
                    product(*range(10), tqdm_class=tqdm_auto, total=total,
                            **kwargs))
                assert wrapped_fp_write_clean(fp)

# Generated at 2022-06-14 13:18:53.354792
# Unit test for function product
def test_product():
    """
    Unit test for the `product` function.
    """
    import tqdm

    assert list(product()) == list(itertools.product())
    assert list(product([1], [2], [3])) == list(itertools.product([1], [2], [3]))
    assert list(product([1], [], [1])) == list(
        itertools.product([1], [], [1]))

    for is_tqdm in [False, True]:
        for t in [tqdm, tqdm_auto]:
            for ntotal in [None, 10]:
                for kwargs in [{}, {'miniters': 1}]:
                    kwargs['total'] = ntotal

# Generated at 2022-06-14 13:19:02.592649
# Unit test for function product
def test_product():
    from numpy import prod
    from random import randint
    from time import sleep
    from tqdm.auto import trange
    len_x, len_y = 10, 100
    x_iter, y_iter = range(len_x), range(len_y)
    xy_total = len_x * len_y
    for x, y in product(x_iter, y_iter, total=xy_total, desc='product'):
        sleep(0.01 * randint(0, 10 - 1))
    assert trange(xy_total).n == xy_total
    for x, y in product(x_iter, y_iter, desc='product'):
        sleep(0.01 * randint(0, 10 - 1))

# Generated at 2022-06-14 13:19:03.889349
# Unit test for function product
def test_product():
    from ..tests.itertool_tests import test_product
    test_product(product)

# Generated at 2022-06-14 13:19:13.360481
# Unit test for function product
def test_product():
    """
    Unit test to verify the product function
    """
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    list3 = [6, 7, 8]

# Generated at 2022-06-14 13:19:22.181778
# Unit test for function product
def test_product():
    from itertools import product
    from random import randint as ri
    from sys import version as python_version
    from re import sub as re_sub

    python_version = (ri(0, 4), ri(0, 10))
    if python_version >= (3, 4):
        from importlib import reload
    else:
        def reload(mod):
            from imp import reload as _reload
            return _reload(mod)

    # Importing tqdm and checking function product
    # to assert its availability
    import tqdm

    assert hasattr(tqdm, 'product')

    # Importing tqdm.tqdm and checking function product
    # to assert its availability
    from tqdm import tqdm as _tqdm

    assert hasattr(_tqdm, 'product')

    # Import

# Generated at 2022-06-14 13:20:04.336624
# Unit test for function product
def test_product():
    from numpy import arange
    arange(27).reshape((3, 3, 3)) == [i for i in product(
        arange(3), arange(3), arange(3))]

# Generated at 2022-06-14 13:20:13.061987
# Unit test for function product
def test_product():
    import sys
    from .tests import pretest_posttest

    @pretest_posttest
    def testing():
        L = list(product(range(3), ['a', 'b'], tqdm_class=tqdm.TqdmTypeError))
        assert L == [(0, 'a'), (0, 'b'), (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

    @pretest_posttest
    def testing2():
        L = list(product(range(3), ['a', 'b'],
                         tqdm_class=tqdm.TqdmKeyError,
                         foo='bar'))

# Generated at 2022-06-14 13:20:17.323528
# Unit test for function product
def test_product():
    """Test whether tqdm(itertools.product()) works as same as tqdm(range(123))"""
    from .std import range
    from .tests import pretest_posttest

    pretest_posttest()
    assert list(product(range(1), range(123))) == \
           list(itertools.product(range(1), range(123)))
    assert list(product("abc", range(5))) == \
           list(itertools.product("abc", range(5)))

# Generated at 2022-06-14 13:20:26.431603
# Unit test for function product
def test_product():
    """
    Unit test for function :func:`tqdm.itertools.product`.

    Returns
    -------
    summary : bool
        Whether all tests passed.
    """
    from numpy import prod
    from pytest import approx
    from .tests_tqdm import closing, fname, _range, pretest

    with closing(tqdm_auto(total=prod(list(map(len, _range(3, 4)))))) as pbar:
        for i in product(*_range(3, 4)):
            assert len(i) == 3 and i == tuple(i)
            pbar.update()


# Generated at 2022-06-14 13:20:31.083285
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    assert list(product(range(10), range(10), range(10))) == \
           list(itertools.product(range(10), range(10), range(10)))

# Generated at 2022-06-14 13:20:34.725228
# Unit test for function product
def test_product():
    for x in product([1, 2, 3]):
        pass
    for x in product([1, 2, 3], repeat=2):
        pass
    for x in product([1, 2, 3], repeat=2, tqdm_class=None):
        pass

# Generated at 2022-06-14 13:20:37.076294
# Unit test for function product
def test_product():
    """Test function product"""
    n = 5
    a = list(range(n))
    b = list(range(n))
    res = list(product(a, b))
    assert len(res) == n * n

# Generated at 2022-06-14 13:20:46.299981
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from random import randint
    try:
        import numpy as np
    except ImportError:
        pass
    else:
        from numpy import product
        from itertools import product as it_product

        s = np.random.randint(2, 3, size=4)
        p = product(*(range(i) for i in s))
        assert type(p) is np.ndarray
        p = it_product(*(range(i) for i in s))
        assert type(p) is not np.ndarray
        p = list(product(*(range(i) for i in s)))
        p = zip(*list(it_product(*(range(i) for i in s))))

# Generated at 2022-06-14 13:20:57.031542
# Unit test for function product
def test_product():
    """Unit test for function product"""
    try:
        import pandas as pd
        pd.set_option('display.max_columns', None)  # or 1000
        pd.set_option('display.max_rows', None)  # or 1000
        pd.set_option('display.max_colwidth', -1)  # or 199
    except:
        pass
    import numpy as np
    R = 1000
    C = 100
    e = np.linspace(10, 20, C)
    A = np.random.randint(1, 10, R)
    print('A')
    print(A)
    i = 0
    for r, c in itertools.product(A, e):
        i += 1
    assert i==R*C

    i = 0

# Generated at 2022-06-14 13:21:03.220969
# Unit test for function product
def test_product():
    """
    Test `tqdm.itertools.product`.
    """
    from .tests import bloops
    from pandas import DataFrame
    from pandas.util.testing import assert_frame_equal

    for t in (tqdm_auto, tqdm_auto.tqdm):
        assert_frame_equal(DataFrame({"a": list(product(range(10),
                                                        tqdm_class=t)),
                                      "b": list(itertools.product(range(10))),
                                      "c": range(10)}),
                          bloops())

# Generated at 2022-06-14 13:21:38.897516
# Unit test for function product
def test_product():
    from ._utils import _range

    assert list(product(_range(3), _range(2))) == list(itertools.product(_range(3), _range(2)))
    assert list(product(_range(3), _range(2))) == [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    assert list(product(_range(3), _range(2))) == [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    assert list(zip(_range(3), _range(2))) == [(0, 0), (1, 1), (2, 2)]

# Generated at 2022-06-14 13:21:46.251679
# Unit test for function product
def test_product():
    v = product([1, 2, 3], [4, 5], [6, 7], tqdm_class=tqdm_auto)
    assert list(v) == [(1, 4, 6), (1, 4, 7), (1, 5, 6), (1, 5, 7),
                       (2, 4, 6), (2, 4, 7), (2, 5, 6), (2, 5, 7),
                       (3, 4, 6), (3, 4, 7), (3, 5, 6), (3, 5, 7)]

# Generated at 2022-06-14 13:21:56.358278
# Unit test for function product
def test_product():
    import numpy as np
    from numpy.testing import assert_array_equal
    from ..auto import tqdm
    import time

    # Test when iterators can be "consumed"
    for iterable in ([1, 2], (n for n in [1, 2]),
                     np.array([1, 2])):
        assert_array_equal([t for t in tqdm.tqdm(
            itertools.product(iterable, repeat=2), total=4)],
            list(itertools.product(iterable, repeat=2)))
        assert_array_equal(
            [t for t in tqdm.tqdm(itertools.product([1, 2], repeat=3), total=8)],
            list(itertools.product([1, 2], repeat=3)))

    # Test when

# Generated at 2022-06-14 13:21:58.675259
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    # Test tqdm_iterator
    from ..tests import test_product as mtp
    mtp.test_product()

# Generated at 2022-06-14 13:22:05.333095
# Unit test for function product
def test_product():
    """Test for the `itertools.product` wrapper"""
    from ..utils import PY3
    if not PY3:  # pragma: no cover
        from itertools import product as itertools_product

        def product20(*args):
            for x in itertools_product(*args):
                yield x
        for t in [tqdm_auto, tqdm]:
            assert list(t.product(range(10), range(10), range(10),
                                  tqdm_class=t)) == list(product20(
                                      range(10), range(10), range(10)))

        def product22(*args):
            for x in itertools_product(*[i for i in args]):
                yield x

# Generated at 2022-06-14 13:22:14.921216
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    # Default total argument
    with tqdm_auto(unit_scale=True) as t:
        for _ in product(range(3), range(3)):
            t.update()
        assert t.total == 9

    # Custom total argument, nested loops
    for i in range(4):
        with tqdm_auto(0, total=(i + 1)**2, unit_scale=True) as t:
            for _ in product(*[range(i + 1)] * 2):
                t.update()
            assert t.total == (i + 1) ** 2

    # Test different iterables types

# Generated at 2022-06-14 13:22:24.010515
# Unit test for function product
def test_product():
    import sys
    from ..tests._utils import _random_data, closing

    if sys.version_info[0] == 2:
        from itertools import imap as map

    def _map_nested(x, *args):
        return list(map(x, *args))

    for i in range(5):
        for n in range(1, 5):
            _nested = list(range(n))
            _nested[-1] = list(range(_nested[-1]))
            inst = product(*_nested)
            assert list(inst) == _map_nested(list, itertools.product(*_nested))

    # Test that product doesn't raise StopIteration prematurely

# Generated at 2022-06-14 13:22:26.546833
# Unit test for function product
def test_product():
    """test for function product"""
    for i in product(list(range(i)) for i in [2, 3, 5]):
        pass

# Generated at 2022-06-14 13:22:30.140949
# Unit test for function product
def test_product():
    from .tests import pretest_posttest_private_testfunc
    pretest_posttest_private_testfunc(product)
    from .tests import pretest_posttest_private_testgen
    pretest_posttest_private_testgen(product)

# Generated at 2022-06-14 13:22:40.088233
# Unit test for function product
def test_product():
    from .._utils import format_sizeof
    for islice in [2, 4, None]:
        for itpl in [
                ((2, 3, 5), (7, 11)),
                (range(10), range(-5, 0)),
                (range(10), range(-5, 100), [1, 10, 100, 1000, 10000], "abcd"),
        ]:
            sizes = []
            for i in product(*itpl, tqdm_class=tqdm_auto, islice=islice):
                sizes.append(i.size)
            if islice is None:
                min_size = min(itpl[0].size, itpl[1].size)
                assert sizes == list(range(min_size))