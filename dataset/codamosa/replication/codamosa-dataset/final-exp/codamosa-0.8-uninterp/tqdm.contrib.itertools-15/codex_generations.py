

# Generated at 2022-06-14 13:12:45.030936
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import numpy.random
    numpy.random.seed(123)
    rands = numpy.random.randint(1, 100, size=10)
    for args in [
            [xrange(4), xrange(4)],
            [xrange(10), xrange(10)],
            [xrange(11), xrange(8)]]:
        ans = list(itertools.product(*args))
        numpy.random.shuffle(ans)

# Generated at 2022-06-14 13:12:53.270226
# Unit test for function product
def test_product():
    import numpy as np
    np.testing.assert_equal(
        list(product(
            np.arange(10),
            np.arange(10),
            tqdm_class=lambda _: _)),
        list(
            itertools.product(
                np.arange(10),
                np.arange(10))))
    np.testing.assert_equal(
        list(product(
            np.arange(10),
            np.arange(10),
            tqdm_class=tqdm_auto)),
        list(
            itertools.product(
                np.arange(10),
                np.arange(10))))

# Generated at 2022-06-14 13:13:05.611688
# Unit test for function product
def test_product():
    # test for degenerate case
    for i in product(range(0)):
        raise Exception("Should not get here (1)")

    # test for different combinations of inputs
    for i in product(range(2), range(2)):
        assert i
    for i in product(range(2), range(2), range(2)):
        assert i
    for i in product(range(2), range(1), range(2)):
        assert i
    for i in product(range(2), range(1), range(1)):
        assert i

    # test for empty iterator
    test = range(10)
    for i in product(test, test, range(0)):
        raise Exception("Should not get here (2)")

    # test for correct output

# Generated at 2022-06-14 13:13:16.085364
# Unit test for function product
def test_product():
    from random import randint
    from time import sleep
    from numpy import allclose
    from numpy.random import rand

    import pandas as pd
    from pandas import DataFrame
    from pandas.util.testing import assert_frame_equal

    from .trange import trange
    from .tqdm import tqdm

    # Test basic functionality
    assert list(product(range(3), range(4))) == [
        (0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2), (2, 3)
    ]

    # Test nested tqdm objects

# Generated at 2022-06-14 13:13:24.709751
# Unit test for function product
def test_product():
    """Tests that the `tqdm.itertools.product` wrapper works"""
    import numpy as np
    from ..auto import trange

    np.testing.assert_array_equal(
        list(product(
            trange(5),
            'abc',
            ['XY'],
            tqdm_class=tqdm_auto)
        ),
        list(itertools.product(
            range(5),
            'abc',
            ['XY']
        ))
    )


# List comprehensions

# Generated at 2022-06-14 13:13:27.079785
# Unit test for function product
def test_product():
    li = list(product(*[[1,3,5],[2,4],[6,7]]))
    assert li == [(1,2,6), (1,2,7), (1,4,6), (1,4,7),
                  (3,2,6), (3,2,7), (3,4,6), (3,4,7),
                  (5,2,6), (5,2,7), (5,4,6), (5,4,7)]

# Generated at 2022-06-14 13:13:32.249926
# Unit test for function product
def test_product():
    """Unit test for function `product`"""
    from ..std import _range, list
    assert list(product(_range(2), _range(2))) == [(0, 0), (0, 1), (1, 0),
                                                   (1, 1)]

# Needed for `setup.py test`
# (Otherwise, `python -m unittest tqdm` does not catch it)
try:
    from .tests import test_product
    test_product()
except (NameError, ImportError):
    pass

# Generated at 2022-06-14 13:13:41.459012
# Unit test for function product
def test_product():
    from random import randint, shuffle
    from itertools import chain
    for i in range(0, 10):
        for _ in range(0, 10):
            nb_iterables = randint(1, 5)
            iterables = []
            for _ in range(0, nb_iterables):
                it = []
                for _ in range(0, randint(1, 5)):
                    it.append(randint(0, 1000))
                shuffle(it)
                iterables.append(it)
            assert list(product(*iterables, desc='product')) == \
                list(itertools.product(*iterables))
            assert list(product(*iterables, desc='product', total=0)) == \
                list(itertools.product(*iterables))

# Generated at 2022-06-14 13:13:48.762154
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from ..utils import format_sizeof
    print('Testing function product...')


# Generated at 2022-06-14 13:13:55.340104
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    seq1 = (1, 2)
    seq2 = ('red', 'white', 'blue')
    seq3 = ("johnny", "mike")

    def _test_prod(prod):
        """
        Test all values of product
        """
        for a, b, c in prod:
            assert a in seq1 and b in seq2 and c in seq3

    from ..main import tqdm
    _test_prod(product(seq1, seq2, seq3))
    _test_prod(product(seq1, seq2, seq3, tqdm_class=tqdm))

# Generated at 2022-06-14 13:13:58.585475
# Unit test for function product
def test_product():
    """Test for itertools.product wrapper"""
    for i in product(range(4), range(4)):
        pass

# Generated at 2022-06-14 13:14:09.021903
# Unit test for function product
def test_product():
    assert list(product("ABC", repeat=2, desc="Test Product")) == [('A', 'A'),
                                                                  ('A', 'B'),
                                                                  ('A', 'C'),
                                                                  ('B', 'A'),
                                                                  ('B', 'B'),
                                                                  ('B', 'C'),
                                                                  ('C', 'A'),
                                                                  ('C', 'B'),
                                                                  ('C', 'C')]
    assert list(product("ABC", repeat=2, total=5, desc="Test Product")) == [('A', 'A'),
                                                                           ('A', 'B'),
                                                                           ('A', 'C'),
                                                                           ('B', 'A'),
                                                                           ('B', 'B')]

# Generated at 2022-06-14 13:14:13.610729
# Unit test for function product
def test_product():
    """
    Test that both `product`s produce the same result.
    """
    from .utils import FakeTqdm
    a = [["a 1", "a 2"], ["b 1", "b 2", "b 3"], ["c 1", "c 2"]]
    assert list(itertools.product(*a)) == list(product(*a, tqdm_class=FakeTqdm))

# Generated at 2022-06-14 13:14:22.462268
# Unit test for function product
def test_product():
    """
    Check that product works as expected.
    """
    from ..tqdm import trange

    def run(data, total, dynamic_total=None, **tqdm_kwargs):
        """
        Run the generator and check whether the results are correct.
        """
        assert sum(1 for _ in data) == total
        bar = trange(total, **tqdm_kwargs)
        for _ in data:
            bar.update()

        if dynamic_total is not None:
            assert bar.total == dynamic_total
        else:
            assert bar.total == total

    run(product([1, 2]), total=2,
        desc="Testing product([1, 2])")
    run(product([1, 2]), total=2,
        desc="Testing product([1, 2])", dynamic_total=2)

# Generated at 2022-06-14 13:14:28.152217
# Unit test for function product
def test_product():
    from .utils import StringIO
    from .tests import pretest, posttest
    from .tests import FormattedTqdmTestCase, closing

    @closing
    def check(**kwargs):
        s = StringIO()
        with pretest(s, False, **kwargs) as t:
            for i in product('ABC', repeat=2,
                             tqdm_class=t.__class__,
                             #monitor=s
                             ):
                pass
        # Post-test processing
        with posttest(t, s, **kwargs) as (passed, failed):
            return passed, failed

    class TestProduct(FormattedTqdmTestCase):
        def test_product(self):
            self.start()
            p1, p2 = check()
            self.check(p1, p2)



# Generated at 2022-06-14 13:14:36.613015
# Unit test for function product
def test_product():
    import random
    from itertools import repeat, chain

    from ..main import tnrange
    from .gui import tqdm
    from .utils import _term_move_up
    from .std import trange, tqdm as tqdm_std

    def product_simple():
        return list(product(range(1, 6), repeat=3))

    def product_inf():
        return list(product(range(1, 6), repeat=float('inf')))

    def product_range(n, iterable):
        return list(product(iterable, repeat=n))

    def product_range_lens():
        return list(product(range(2), repeat=5))

    def product_range_10_2():
        return list(product(range(10), repeat=2, tqdm_class=tqdm))

# Generated at 2022-06-14 13:14:46.729218
# Unit test for function product
def test_product():
    import pytest
    from .._tqdm_test_helper import _runner

    def test_gen_1(*args, **kwargs):
        return product(*args, **kwargs)

    with pytest.raises(TypeError):
        _runner(test_gen_1, range(5), range(5), [1, 2, 3])

    with pytest.raises(TypeError):
        _runner(test_gen_1, (i for i in range(5)), tqdm_class=tqdm_auto)

    assert "total" in _runner(test_gen_1, [1, 2, 3, 4], ['a', 'b', 'c']).stats

    assert _runner(test_gen_1, [1, 2, 3, 4], ['a', 'b', 'c']).pos == 12



# Generated at 2022-06-14 13:14:53.758126
# Unit test for function product
def test_product():
    from random import randrange
    for cls in [tqdm_auto, None]:  # Run with and without tqdm
        for iterables in [
                [(randrange(100), randrange(100)) for _ in range(3)],
                ['abc', 'def', 'ghi'],
                [chr(ord('a') + i) for i in range(randrange(1, 10))],
        ]:
            res = list(product(*iterables, tqdm_class=cls))
            assert res == list(itertools.product(*iterables))
            res = list(product(tqdm_class=cls, *iterables))
            assert res == list(itertools.product(*iterables))

# Generated at 2022-06-14 13:14:56.485575
# Unit test for function product
def test_product():
    from ..tests.test_utils import TestCase

    with TestCase(tqdm=tqdm_auto, unit=" it"):
        for _ in product(["a", "b"], ["1", "2", "3"], tqdm_class=tqdm_auto):
            pass

# Generated at 2022-06-14 13:15:02.675131
# Unit test for function product
def test_product():
    import itertools
    import numpy as np
    import pandas as pd
    from ..tqdm import trange

    for J in trange(10, desc="With native Python iterables"):
        for i in product(range(10), repeat=J):
            assert isinstance(i, tuple)
        for i in product(range(10), repeat=J):
            assert isinstance(i, tuple)

    for J in trange(10, desc="With lazy iterables"):
        for i in product(zip(range(10), range(10)), repeat=J):
            assert isinstance(i, tuple)
        for i in product(zip(range(10), range(10)), repeat=J):
            assert isinstance(i, tuple)


# Generated at 2022-06-14 13:15:15.195061
# Unit test for function product
def test_product():
    from .__init__ import TqdmDeprecationWarning
    import warnings
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=TqdmDeprecationWarning)
        from .tests_tqdm import with_base_config, pretest, posttest
        pretest()

        # Note that `test_product()` is itself a unit-test of `product()`
        def list_product(a, b, c=0, d=0):
            """
            Equivalent of `itertools.product`:
            - without tqdm
            - only with list(...) (i.e. eager)
            """
            out = []

# Generated at 2022-06-14 13:15:25.831986
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import math
    list_of_lists = [[1, 2, 3], [4], [5, 6]]
    out = list(product(*list_of_lists))

    assert len(out) == len(list_of_lists[0]) * len(list_of_lists[1]) * len(list_of_lists[2])
    assert out[0] == (1,4,5)
    assert out[-1] == (3,4,6)

    out = list(product(*list_of_lists, tqdm_class=None))
    assert len(out) == len(list_of_lists[0]) * len(list_of_lists[1]) * len(list_of_lists[2])

# Generated at 2022-06-14 13:15:32.256470
# Unit test for function product
def test_product():
    from .._tqdm import _prog_bar as PBar
    from .._tqdm import _term_move_up as TMU

    # Test the number of iterations is correct and returns right values

# Generated at 2022-06-14 13:15:37.971588
# Unit test for function product
def test_product():  # pragma: no cover
    a = range(100000)
    b = range(100000)
    c = range(100000)
    i = 0
    for x in product(a, b, c, tqdm_class=tqdm_auto):
        assert x == (i//1000000, (i//1000) % 1000, i % 1000)
        i += 1

# Generated at 2022-06-14 13:15:44.142917
# Unit test for function product
def test_product():
    import numpy  # NOQA

    def product_test_fix(n, r):
        """
        Compute the exact value of product from scratch.
        """
        return numpy.prod(range(n - (r - 1), n + 1))

    for n in range(4, 8):
        for r in range(1, 5):
            res = product_test_fix(n, r)
            assert res == sum(
                t for t in product(range(n), repeat=r))

# Generated at 2022-06-14 13:15:49.172614
# Unit test for function product
def test_product():
    """
    Test function `tqdm.itertools.product`.
    """
    from ..utils import _term_move_up
    try:
        from itertools import product as itertools_product
    except ImportError:
        # In Python 2.6, `itertools.product` is not present
        return
    from ..utils import _range, FormatCustomTextTestCase, format_interval, \
        format_meter, format_sizeof
    import sys
    try:
        import numpy
    except ImportError:
        numpy = None

    kwargs = dict(iterable=None, total=None, ascii=False, unit="it")
    if numpy is not None:
        numpy_kwargs = kwargs.copy()

# Generated at 2022-06-14 13:15:58.950230
# Unit test for function product
def test_product():
    from .testsig import test
    from .utils import BetterRepr, ClosingContext

    @test
    def test_basics():
        from random import randrange
        from itertools import product

        with ClosingContext(BetterRepr(total=None)) as cr:
            assert cr._total is None
            assert list(cr(product,
                        range(randrange(5, 10)),
                        range(randrange(1, 5)))) == list(product(
                            range(randrange(5, 10)),
                            range(randrange(1, 5))))
            assert cr._total is None
            assert list(cr(product,
                        range(randrange(1, 5)),
                        range(randrange(5, 10)))) == list(product(
                            range(randrange(1, 5)),
                            range(randrange(5, 10))))

# Generated at 2022-06-14 13:16:01.503075
# Unit test for function product
def test_product():
    for i in product(range(4), repeat=4):
        pass
    for i in product(range(4), range(3), range(2), range(1)):
        pass

# Generated at 2022-06-14 13:16:04.272332
# Unit test for function product
def test_product():
    for i in product(*[range(i) for i in [10, 20]], tqdm_class=lambda c: c):
        pass

# Generated at 2022-06-14 13:16:11.350500
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    from tqdm.contrib.test import _range
    res = list(product(range(100),
                       _range(100, 200),
                       range(100, 200, 2),
                       tqdm_class=lambda *x: None))
    assert res == list(itertools.product(range(100),
                                         _range(100, 200),
                                         range(100, 200, 2)))


if __name__ == '__main__':
    from .tests import _test_extras
    _test_extras()

# Generated at 2022-06-14 13:16:20.226435
# Unit test for function product
def test_product():
    for i in product(range(4), range(4), range(4),
                     tqdm_class=tqdm_auto,
                     bar_format="{n_fmt}/{total_fmt} [{bar}] {postfix}",
                     postfix="YAY!"):
        assert len(i) == 3
        yield None

# Generated at 2022-06-14 13:16:30.291056
# Unit test for function product
def test_product():
    """
    Unit test for `tqdm.itertools.product`.
    """
    from nose import with_setup
    from random import shuffle
    from ...utils import format_sizeof
    from six.moves import range
    import sys
    import os

    def get_sizes(lengths):
        total = 1
        mem_total = int(sys.getsizeof(42))
        mem_sizes = []
        for i in lengths:
            total *= i
            mem_sizes.append(int(sys.getsizeof(42) * i))
        mem_total *= total
        return total, mem_sizes, mem_total

    # check that module has not changed
    assert len(list(itertools.product([]))) == 1

    # check that function has not changed

# Generated at 2022-06-14 13:16:38.318413
# Unit test for function product
def test_product():
    """
    Unit test for function product().
    """
    from collections import Counter
    from ..utils import FormatSize

    def f(i):
        from time import sleep
        sleep(5 / 1e6)
        return i

    # Basic test
    res = list(product(range(1), range(2), range(3), range(4)))

# Generated at 2022-06-14 13:16:40.470096
# Unit test for function product
def test_product():
    assert sum(1 for _ in product([1, 2, 3], [4, 5, 6])) == 9

# Generated at 2022-06-14 13:16:48.612062
# Unit test for function product
def test_product():
    """Unit test for function product"""
    try:
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        l3 = [7, 8, 9]
        l4 = [10, 11]
        p1 = [i for i in product(l1, l2, l3, l4)]
        p2 = [i for i in product(l1, l2, l3, l4, tqdm_class=tqdm_auto)]
        p3 = [i for i in product(l1, l2, l3, l4, tqdm_class=tqdm_auto)]
        assert p1 == p2 == p3
    except:
        assert False

# Generated at 2022-06-14 13:16:55.755590
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from .utils import FormatWrapBase
    test_kwargs = {'leave': False, 'ascii': True, 'dynamic_ncols': True}

    assert list(product(list(range(10)), list(range(10)))) == \
        list(itertools.product(list(range(10)), list(range(10))))

    class FakeTqdm(FormatWrapBase):
        def __init__(self, *args, **kwargs):
            super(FakeTqdm, self).__init__(*args, **kwargs)
            self.sp = set()
            self.si = 0

        def __enter__(self):
            return self


# Generated at 2022-06-14 13:17:01.373230
# Unit test for function product
def test_product():
    from .main import main as tqdm_main
    from .tests import PretendGen
    from .test_pandas import _test_pandas_prog

    # Create a generator that yields a random number in [0, 0.1)
    # every time next is called
    import random
    gen = ((random.random()) for x in range(100))

    # Use tqdm to wrap the above generator
    wordr = PretendGen(gen)
    # Ensure that the start count is 0 and the total is 100
    r = tqdm_main(wordr, total=100)

    # Ensure that the start count and the total are correct
    assert r.n == 0
    assert r.total == 100

    # Ensure that tqdm gives the expected output

# Generated at 2022-06-14 13:17:11.064733
# Unit test for function product
def test_product():
    assert sum(1 for _ in product(range(10), tqdm_class=None)) == 100
    assert sum(1 for _ in product(range(2), repeat=3, tqdm_class=None)) == 8
    assert sum(1 for _ in product(range(2), range(2), range(2), tqdm_class=None)) == 8
    assert sum(1 for _ in product(range(2), repeat=5, tqdm_class=None)) == 32

if __name__ == "__main__":
    test_product()

    def product_is_map_reduce_chain():
        import pandas
        import numpy as np

        def func(a, b):
            return a + b


# Generated at 2022-06-14 13:17:14.791065
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    import numpy as np
    list1 = np.arange(3)
    list2 = ['a', 'b', 'c']
    output = list(product(list1, list2))
    assert output == [(i, j) for i in list1 for j in list2]

# Generated at 2022-06-14 13:17:20.309999
# Unit test for function product
def test_product():
    """Tests that tqdm(range(3), total=3) == (0, 1, 2)"""
    from tqdm import tqdm
    assert tuple(tqdm(range(3), total=3)) == (0, 1, 2)
    assert tuple(tqdm(range(4), total=4)) == (0, 1, 2, 3)

if __name__ == '__main__':
    from .collections import del_tqdm_tqdm
    # https://tqdm.github.io/docs/tqdm/
    for i in product(range(5), range(5), range(5), ['a', 'b'],
                     tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:17:34.618690
# Unit test for function product
def test_product():
    """Unit test for product"""
    assert list(product(['a', 'b', 'c'], range(0, 2), tqdm_class=tqdm_auto)) \
        == [('a', 0), ('a', 1),
            ('b', 0), ('b', 1),
            ('c', 0), ('c', 1)]

    assert list(product(['a', 'b', 'c'], repeat=2, tqdm_class=tqdm_auto)) \
        == [('a', 'a'), ('a', 'b'), ('a', 'c'),
            ('b', 'a'), ('b', 'b'), ('b', 'c'),
            ('c', 'a'), ('c', 'b'), ('c', 'c')]


# Generated at 2022-06-14 13:17:37.331797
# Unit test for function product
def test_product():
    """
    Simple unit test for function product.
    """
    with tqdm_auto(total=10) as t:
        for _ in product(range(10), tqdm_class=tqdm_auto):
            t.update()

# Generated at 2022-06-14 13:17:38.594783
# Unit test for function product
def test_product():
    '''No unit test because it is exactly equivalent to `itertools.product`'''
    return None

# Generated at 2022-06-14 13:17:43.499822
# Unit test for function product
def test_product():
    """Test for product"""
    from ..utils import format_sizeof
    from .monitor import total_seconds

    import copy
    import sys
    import types
    from itertools import product
    from time import sleep

    def test_product_gen(it_kwargs_test, it_kwargs_ref, tqdm_kwargs):
        """Run with tqdm and without, compare outputs and errors/warnings."""
        tqdm_kwargs = copy.deepcopy(tqdm_kwargs)
        it_kwargs_test = copy.deepcopy(it_kwargs_test)
        it_kwargs_ref = copy.deepcopy(it_kwargs_ref)


# Generated at 2022-06-14 13:17:47.190104
# Unit test for function product
def test_product():
    import numpy as np
    np.testing.assert_array_equal(
        list(product(range(3), range(4))),
        list(itertools.product(range(3), range(4))))
test_product()

# Generated at 2022-06-14 13:17:56.605084
# Unit test for function product
def test_product():
    """
    Test for `tqdm.itertools.product`
    """
    import numpy as np
    from .utils import FormatStremTqdmTest

    for tqdm_cls in [tqdm_auto, FormatStremTqdmTest]:
        assert(
            list(product('ABCD', repeat=2, tqdm_class=tqdm_cls)) ==
            list(map(''.join, itertools.product('ABCD', repeat=2))),
            "Wrong product output"
        )

# Generated at 2022-06-14 13:17:57.928469
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    assert list(product(range(10), range(10))) == list(itertools.product(range(10), range(10)))

# Generated at 2022-06-14 13:18:01.454970
# Unit test for function product
def test_product():
    from os import remove
    from tempfile import NamedTemporaryFile
    try:
        f = NamedTemporaryFile(delete=False)
        for x in product(range(5), repeat=5, tqdm_class=tqdm_auto, file=f):
            pass
        total = sum((i + 1)**5 for i in range(5))
        assert total == f.read()[1:].count(b'8')
    finally:
        f.close()
        remove(f.name)

# Generated at 2022-06-14 13:18:05.320715
# Unit test for function product
def test_product():
    from .tests import closing, pretest_posttest

    @closing
    def _test():
        # Test 1
        a = product(range(4), range(4))
        for i, ai in enumerate(a):
            # Test 2
            assert i == ai[0] + 4 * ai[1]
        assert i == 15

    pretest_posttest(_test)

# Generated at 2022-06-14 13:18:13.268952
# Unit test for function product
def test_product():
    """pytest unit test"""
    # pylint: disable=missing-docstring
    # pylint: disable=unused-variable
    from . import _test_itertools
    for ret in product("abcd", "1234", tqdm_class=tqdm_auto):
        assert ret is next(_test_itertools.product("abcd", "1234"))
    for ret in product("abcd", "1234", tqdm_class=tqdm_auto):
        assert ret is next(_test_itertools.product("abcd", "1234"))

# Generated at 2022-06-14 13:18:27.048967
# Unit test for function product
def test_product():
    iterables = [range(10), range(10)]
    x = product(*iterables)
    assert list(x) == list(itertools.product(*iterables))

# Generated at 2022-06-14 13:18:34.454013
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from ..utils import _range
    from ..std import List

    def test(iterables, total, **tqdm_kwargs):
        """
        Unit test for function product

        Parameters
        ----------
        iterables  : iterable of iterables.
        total  : int.
            Total number of expected iterations.
        tqdm_kwargs  : dict.
        """
        # loop
        result = list(product(*iterables, **tqdm_kwargs))
        # check wrapping
        assert isinstance(result, List)
        # check correctnes
        assert list(result) == list(itertools.product(*iterables))
        # check correctnes
        assert len(result) == total


# Generated at 2022-06-14 13:18:45.166134
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import nose.tools as nt
    from numpy.testing import assert_equal
    from ..std import numpy as np
    from ..std import six

    def test_product_examples():
        """
        Test some custom product examples.
        """
        with tqdm_auto(total=2) as t:
            assert_equal([i for i in product(range(2), tqdm=t)],
                         [i for i in itertools.product(range(2))])
            assert_equal([i for i in product(
                [1, 2, 3, 4], [0, 1], tqdm=t)],
                [i for i in itertools.product([1, 2, 3, 4], [0, 1])])

# Generated at 2022-06-14 13:18:47.423130
# Unit test for function product
def test_product():
    """ > python -m tqdm.utils.itertools itertools.py """
    for n in product(range(10), repeat=3):
        pass

# Generated at 2022-06-14 13:18:55.362985
# Unit test for function product
def test_product():
    """
    Unit test of function product.
    """
    def check_product(x, y, z):
        actual = set()
        for t in product(x, y, z):
            actual.add(t)
        expected = set(itertools.product(x, y, z))
        assert expected == actual

    check_product(range(10), range(10), range(10))
    check_product([], range(10), range(10))
    check_product(range(10), [], range(10))
    check_product(range(10), range(10), [])
    check_product([], [], range(10))
    check_product([], range(10), [])
    check_product(range(10), [], [])
    check_product([], [], [])

# Generated at 2022-06-14 13:19:04.802225
# Unit test for function product
def test_product():
    """Unit test for function product"""
    # All
    with tqdm_auto(total=5) as t:
        list(product([0, 1], [2, 3], [4, 5], tqdm_class=tqdm_auto))
        assert t.n == 5
    # Short-circuit
    with tqdm_auto(total=5) as t:
        list(product([0, 1], [2, 3], [4, 5], tqdm_class=tqdm_auto, miniters=6))
        assert t.n == 5
    # Short-circuit
    with tqdm_auto(total=5) as t:
        list(product([0, 1], [2, 3], [4, 5], tqdm_class=tqdm_auto, miniters=4))


# Generated at 2022-06-14 13:19:10.364928
# Unit test for function product
def test_product():
    for i in product((1, 2, 3), (4, 5)):
        assert len(i) == 2

    for i in product({'a': 1, 'b': 1}):
        assert len(i) == 2

    for i in product((1, 2, 3), total=2):
        assert len(i) == 2

    # Test iterator argument
    assert list(range(10)) == list(product(range(10)))

# Generated at 2022-06-14 13:19:13.126018
# Unit test for function product
def test_product():
    """
    Manually tested, as it is trivial to test.
    
    Just use the standard itertools.product function,
    with or without the tqdm wrapper.
    """
    pass

# Generated at 2022-06-14 13:19:18.527514
# Unit test for function product
def test_product():
    from .tqdm_gui import tqdm
    from .utils import _range
    from .std import compat_get_terminal_size

    for i in product(_range(4), _range(2), _range(3), tqdm_class=tqdm,
                     mininterval=0.01, miniters=2, ascii=True):
        pass
    for i in product(_range(4), _range(2), _range(3), tqdm_class=tqdm,
                     mininterval=0.01, miniters=2, ascii=True,
                     desc="my_desc"):
        pass

# Generated at 2022-06-14 13:19:22.912065
# Unit test for function product
def test_product():
    """Test the function `product`."""
    assert list(product(list("abc"), repeat=2)) == \
        [('a', 'a'), ('a', 'b'), ('a', 'c'),
         ('b', 'a'), ('b', 'b'), ('b', 'c'),
         ('c', 'a'), ('c', 'b'), ('c', 'c')]

# Generated at 2022-06-14 13:19:50.810999
# Unit test for function product
def test_product():
    """Test product"""
    import numpy as np
    a1 = list('abc')
    a2 = [list(range(10)), tuple(range(10))]

    for arr1, arr2 in itertools.product(a1, a2):
        for i, j in product(arr1, arr2):
            assert(np.all(np.asarray(i) == np.asarray(j)))

# Generated at 2022-06-14 13:19:53.600514
# Unit test for function product
def test_product():
    """ test function product """
    p = list(product(range(5), repeat=2))
    assert (5**2), p
    p = list(product(range(5), range(1, 4)))
    assert (5*3), p

# Generated at 2022-06-14 13:19:59.923870
# Unit test for function product
def test_product():
    from .utils import TestBarBase
    from collections import Iterable
    from sys import version_info

    class Test(TestBarBase):
        def __init__(self):
            super(Test, self).__init__()

        def test_product_map(self):
            x = product(range(100))
            assert isinstance(x, Iterable)
            y = list(x)
            assert len(y) == 100
            assert y[0][0] == 0
            assert y[-1][0] == 99

        def test_product_map_desc(self):
            x = product(range(100), desc='Test', leave=False)
            y = list(x)
            assert len(y) == 100
            assert y[0][0] == 0
            assert y[-1][0] == 99


# Generated at 2022-06-14 13:20:06.637286
# Unit test for function product
def test_product():
    from . import TMonitor
    from .tests import tqdm

    with TMonitor(leave=True) as m:
        for _ in tqdm(product([1, 2], repeat=2), desc="product", total=4):
            pass
    assert m.results == ([], [1.0] * 4, [1.0] * 4)

    with TMonitor(leave=True) as m:
        for _ in tqdm(product([1, 2], repeat=2), desc="product"):
            pass
    assert m.results == ([], [1.0] * 4, [1.0] * 4)

# Generated at 2022-06-14 13:20:14.742849
# Unit test for function product
def test_product():
    import shutil as shu
    import sys
    try:
        true = True
        false = False
    except NameError:
        true = 1
        false = 0
    for verbose, _total, leave, ascii in product([true, false], [None, 1],
                                                 [True, False], [True, False]):
        secs = .5
        with tqdm(total=_total, miniters=1, mininterval=0, leave=leave,
                  ascii=ascii, file=sys.stdout) as my_bar:
            for i in range(10, 27, 2):
                my_bar.update(i)

# Generated at 2022-06-14 13:20:19.454561
# Unit test for function product
def test_product():
    from ...tests import test_iterable
    from ...tests.test_itertools import test_product as _test_product
    kwargs = dict(
        tqdm_class=tqdm_auto,
        iterable_length=1000,
        sample_size=100,
    )
    _test_product(product, **kwargs)
    test_iterable(product, **kwargs)

# Generated at 2022-06-14 13:20:22.459451
# Unit test for function product
def test_product():
    import nose.tools as nt

    def product_it():
        for i in itertools.product(range(5), range(5), range(5)):
            yield i

    nt.assert_equal(list(product(range(5), range(5), range(5))),
                    list(product_it()))

# Generated at 2022-06-14 13:20:30.424518
# Unit test for function product
def test_product():
    from random import randint
    from itertools import product as itertools_product
    for tot in range(1, 11):
        iterables = [range(randint(1, 10)) for _ in range(tot)]
        iterables_p = product(*iterables)
        iterables_p_itertools = itertools_product(*iterables)
        assert list(iterables_p) == list(iterables_p_itertools)


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:20:36.436923
# Unit test for function product
def test_product():
    from tqdm import tqdm
    t = tqdm(total=10)
    assert list(product(t, range(5), range(5))) == [(t, 0, 0), (t, 1, 0),
                                                    (t, 2, 0), (t, 3, 0),
                                                    (t, 4, 0), (t, 0, 1),
                                                    (t, 1, 1), (t, 2, 1),
                                                    (t, 3, 1), (t, 4, 1)]

# Generated at 2022-06-14 13:20:45.864746
# Unit test for function product
def test_product():
    from numpy.random import randint

    def gen():
        from .utils import numpy
        a = numpy.array([[1, 2, 3], [4, 5, 6], [8, 8, 7]])
        for i, j in product(a, repeat=2):
            yield (i, j)
    res = list(gen())
    assert len(res) == 27
    for i, j in res:
        assert i <= j

    res = list(product(range(10), repeat=randint(0, 5)))
    assert len(res) == 0
    res = list(product(range(10), repeat=randint(0, 5), tqdm_class='nongit'))
    assert len(res) == 0

# Generated at 2022-06-14 13:21:40.467272
# Unit test for function product
def test_product():
    from .._tqdm_test_cli import _test_iterable

    def product_closure(a, b):
        """Return product of two numbers"""
        return a * b

    _test_iterable(product, 1, 10, 3, 5, tqdm_class=tqdm_auto)
    _test_iterable(product_closure, 10, range(1, 10), tqdm_class=tqdm_auto)
    _test_iterable(lambda: list(product([1])))
    _test_iterable(lambda: list(product([1], [2])), tqdm_class=tqdm_auto)
    _test_iterable(lambda: list(product([1], [2], repeat=3)))

# Generated at 2022-06-14 13:21:48.613884
# Unit test for function product
def test_product():
    """Test for itertools.product() wrapper."""
    from .tests_tqdm_gui import _test_cls, _test_cls_leave
    from itertools import product

    for cls in _test_cls:
        for a in range(2, 4):
            for b in range(2, 4):
                x = list(product(range(a), range(b)))
                y = list(product(range(a), range(b), tqdm_class=cls))
                for i, j in zip(x, y):
                    assert i == j
        _test_cls_leave(cls)

# Generated at 2022-06-14 13:21:53.754620
# Unit test for function product
def test_product():
    for i in product("ABC", "DEF"):
        assert isinstance(i, tuple)
    for i in product("ABC", "DEF", tqdm_class=None):
        assert isinstance(i, tuple)
    for i in product([1, 2, 3], [4, 5, 6], tqdm_class=None):
        assert isinstance(i, tuple)

# Generated at 2022-06-14 13:22:02.624658
# Unit test for function product
def test_product():
    from .main import tqdm

    for a in range(10):
        for i in tqdm.tqdm(range(a)):
            assert i == i
    p = tqdm.tqdm.pandas(tqdm.tqdm(tqdm.tqdm.tqdm(tqdm.tqdm.tqdm(tqdm.tqdm.tqdm(tqdm.tqdm.tqdm(tqdm.tqdm.tqdm(tqdm.tqdm.tqdm(tqdm.tqdm.tqdm(tqdm.tqdm.tqdm(range(9)))))))))))
    for i in p:
        assert i == i

# Generated at 2022-06-14 13:22:04.736418
# Unit test for function product
def test_product():
    for _ in product(["foo", "bar"], ["baz", "qux"], ["quux", "quuz"]):
        pass

# Generated at 2022-06-14 13:22:11.182793
# Unit test for function product
def test_product():
    """
    Test ``tqdm.itertools.product``
    """
    from numpy.random import randint
    a = randint(0, 10, 6)
    b = randint(0, 10, 4)
    c = randint(0, 10, 2)
    assert list(product(a, b)) == list(itertools.product(a, b))  # NOQA
    assert list(product(a, b, c)) == list(itertools.product(a, b, c))  # NOQA

# Generated at 2022-06-14 13:22:14.803945
# Unit test for function product
def test_product():
    import numpy as np

    ans = np.array(list(itertools.product(range(2), range(2), range(2))))
    res = np.array(list(product(range(2), range(2), range(2))))
    assert (ans == res).all()

# Generated at 2022-06-14 13:22:23.897284
# Unit test for function product
def test_product():
    from .gui import tqdm
    from .utils import FormatCustomText

# Generated at 2022-06-14 13:22:34.118890
# Unit test for function product
def test_product():
    "Test function"
    import numpy as np
    from ..utils import TestingIO  # NOQA

    assert list(product("AB", "12")) == list(itertools.product("AB", "12"))

    assert list(product("AB", "12", tqdm_class=None)) == \
        list(itertools.product("AB", "12"))

    out = list(product("AB", "12", tqdm_class=TestingIO))
    assert out == list(itertools.product("AB", "12"))

    out = list(product(np.arange(3), repeat=3))
    assert out == list(itertools.product(np.arange(3), repeat=3))

    out = list(product(np.arange(3), repeat=3, tqdm_class=None))
