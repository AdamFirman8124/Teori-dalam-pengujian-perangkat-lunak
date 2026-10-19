

# Generated at 2022-06-14 13:12:29.373082
# Unit test for function product
def test_product():
    """ Unit test for `product` """
    assert list(product(range(3), range(3))) == list(itertools.product(range(3), range(3)))
    assert list(product(range(3), range(3), tqdm_class=None)) == list(product(range(3), range(3)))

# Generated at 2022-06-14 13:12:31.826472
# Unit test for function product
def test_product():
    assert list(product(range(10), repeat=3)) == list(product(range(10), range(10), range(10)))

# Generated at 2022-06-14 13:12:38.318703
# Unit test for function product
def test_product():
    # set up inputs
    iterables = ("ABCD", "xy")
    # compute result
    outputs = list(product(*iterables))
    assert outputs == list(itertools.product(*iterables))
    # compute and reassign result (this is to make sure that the
    # iterator isn't exhausted after being cast into a list)
    outputs = list(product(*iterables))
    assert outputs == list(itertools.product(*iterables))

# Generated at 2022-06-14 13:12:44.123234
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from ..utils import FormatCustomText
    import random
    lst = []
    for x in product(range(10000), range(20000),
                     tqdm_class=FormatCustomText):
        lst.append(x)
        if random.random() < 0.001:
            break
    else:
        raise AssertionError

# Generated at 2022-06-14 13:12:52.678210
# Unit test for function product
def test_product():
    """Test for function product"""
    from .tests_tqdm import discretize, StringIO
    from .tests_tqdm import _range as range

    product_iter = list(product(range(4), ['a', 'b', 'c', 'd']))
    product_list = [tuple(map(str, product))
                    for product in itertools.product(range(4),
                                                     ['a', 'b', 'c', 'd'])]
    assert product_list == product_iter

    product_iter = list(product(range(4), ['a', 'b', 'c', 'd'],
                                tqdm_class=tqdm_auto,
                                leave=False))

# Generated at 2022-06-14 13:13:03.390724
# Unit test for function product
def test_product():
    from ..utils import FormatStopNow

    try:
        total_len, max_len, cnt = 0, 0, 0
        for i in product(range(10), range(20), range(30), tqdm_class=tqdm_auto, desc="bar"):
            i_len = len(str(i))
            if i_len > max_len:
                max_len = i_len
            total_len += i_len
            cnt += 1
        assert total_len == 24450  # 10 * 20 * 30 * 3
        assert max_len == 4  # 0, 0, 0,
    except FormatStopNow:
        pass
    else:
        raise RuntimeError("Test failed!")

# Generated at 2022-06-14 13:13:10.738794
# Unit test for function product
def test_product():
    assert list(product(range(2), repeat=3)) == list(itertools.product(range(2), repeat=3))
    assert list(product(range(2), tqdm=None, repeat=3)) == list(itertools.product(range(2), repeat=3))
    assert list(product(range(2), tqdm=tqdm_auto, repeat=3)) != list(itertools.product(range(2), repeat=3))

# Generated at 2022-06-14 13:13:15.527973
# Unit test for function product
def test_product():
    """Unit test for function `product`."""
    p = product(range(10), range(10), tqdm_class=tqdm_auto)
    assert sum(1 for _ in p) == 100
    p = product(range(100), range(100), tqdm_class=tqdm_auto)
    assert sum(1 for _ in p) == 10000

# Generated at 2022-06-14 13:13:23.170097
# Unit test for function product
def test_product():
    from .trange import trange
    from .tqdm import tqdm
    from .._tqdm import TqdmTypeError

    def pbar(iterable, tqdm_class=TrangeType, **kwargs):
        return tqdm(iterable, tqdm_class=tqdm_class, **kwargs)

    # Empty iterables
    assert list(range(0)) == list(pbar(range(0)))
    assert list(range(0)) == list(pbar(range(0), total=0))
    assert list(range(0)) == list(pbar(range(0), total=1))
    assert list(range(0)) == list(pbar(range(0), total=2))

    # One iterable

# Generated at 2022-06-14 13:13:32.250876
# Unit test for function product
def test_product():
    from .utils import SimpleTextIOWrapper, closing, StringIO
    from ._tqdm import trange, tqdm
    from ._utils import format_sizeof

    with closing(StringIO()) as our_file:
        with SimpleTextIOWrapper(our_file) as s:
            for _ in tqdm(product(range(3), range(2), tqdm_class=trange), file=s):
                pass

    with closing(StringIO()) as our_file:
        with SimpleTextIOWrapper(our_file) as s:
            for _ in tqdm(xrange(6), file=s):
                pass


# Generated at 2022-06-14 13:13:39.315220
# Unit test for function product
def test_product():
    """Test the tqdm product function"""
    from ..utils import _range
    with tqdm_auto(total=2 * 3 * 4) as t:
        for i in product(_range(2), _range(3), _range(4)):
            assert i[0] < 2 and i[1] < 3 and i[2] < 4
            t.update()


# Aliases
imap = itertools.imap

# Generated at 2022-06-14 13:13:47.344316
# Unit test for function product
def test_product():
    from numpy.random import randint
    from numpy import product
    tot = 0
    for i in product(range(100), repeat=3):
        tot += 1
    assert tot == 100 ** 3
    tot = 0
    T = randint(100, size=(100, 3))
    for i in product(*T):
        tot += 1
    assert tot == product(T.shape)
    try:
        # Should not iterate
        for _ in product(*T): raise RuntimeError()
    except RuntimeError:
        pass
    try:
        # Should not iterate
        for _ in product(): raise RuntimeError()
    except RuntimeError:
        pass
    try:
        # Should not iterate
        for _ in product(*T, total=10): raise RuntimeError()
    except RuntimeError:
        pass

# Generated at 2022-06-14 13:13:51.623081
# Unit test for function product
def test_product():
    assert str(list(product(range(3),
                            range(4),
                            range(2),
                            tqdm_class=lambda x: tqdm_auto(x,
                                                          disable=True)))
               ) == str(list(itertools.product(range(3),
                                               range(4),
                                               range(2))))


# For backwards compatibility

# Generated at 2022-06-14 13:14:00.757565
# Unit test for function product
def test_product():
    # Need to define the global function here instead of
    # importing from libs/itertools.py to avoid cyclic import
    from .libs.itertools import product
    """Simple test for product"""
    from .pandas import DataFrame
    ids = list("abc")
    events = zip(*(ids, range(1, 7)))
    data = {ids[0]: [1, 2, 3, 1, 2, 3],
            ids[1]: [1, 1, 1, 2, 2, 2],
            ids[2]: [1, 2, 3, 4, 5, 6]}
    df = DataFrame(data)

    assert list(product(*(ids, range(1, 7)))) == events
    assert list(product(*(ids, range(1, 7)), tqdm_class=None)) == events


# Generated at 2022-06-14 13:14:11.644145
# Unit test for function product
def test_product():
    """Tests that the `tqdm.tqdm.product` function behaves the same as
    `itertools.product`
    """
    from random import randint

    for lo, hi in [(0, 1000), (10 ** 2, 10 ** 2 + 10 ** 2 / 2)]:
        for n in (0, 1, 2, 3):
            for r in (0, 2, 5):
                for ragged in (False, True):
                    if ragged:
                        lens = [randint(lo, hi) for _ in range(n)]
                    else:
                        lens = [lo + randint(0, hi - lo) for _ in range(n)]
                    iterables = [[randint(0, r) for _ in range(size)]
                                 for size in lens]

# Generated at 2022-06-14 13:14:20.628581
# Unit test for function product
def test_product():
    """
    Unit testing for `tqdm.itertools.product`.
    """
    from .tests_tqdm import with_setup, _range, closing

    def foo():
        for _ in product(['a', 'b'], repeat=3, tqdm_class=None):
            yield
    with closing(tqdm_auto()) as t:
        with t.debug(leave=True):
            _ = list(foo())
    assert t.total == 2**3
    assert t.n == 8

    @with_setup(foo)
    def test_product_iter():
        """
        Unit testing for `tqdm.itertools.product` with **iterables.
        """

# Generated at 2022-06-14 13:14:27.590423
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from ..utils import FormatCustomText

    class Foo(FormatCustomText):
        pass

    with Foo(unit="B", unit_scale=True) as pbar:
        for i in product(range(10), range(7), range(5)):
            pass
        assert pbar.n == 10 * 7 * 5, "tqdm(itertools.product) counts items"
        assert pbar.total == 10 * 7 * 5, "tqdm(itertools.product) counts items"

if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:14:36.319060
# Unit test for function product
def test_product():
    """Unit test for function product."""
    from . import trange

    # small tests
    a = '1234'
    b = 'abcd'
    c = 'efgh'
    assert list(product(a, b, c)) == [
        (x, y, z) for x in a for y in b for z in c]
    assert list(product(a, b, c)) == list(product(b, a, c))
    assert list(product(a, b, c)) == list(product(b, c, a))
    assert list(product(a, b, c)) == list(product(c, b, a))
    assert list(product(a, b, c)) == list(product(c, a, b))

# Generated at 2022-06-14 13:14:46.650271
# Unit test for function product
def test_product():
    import os
    import gc
    import sys
    # Make sure pytest's print capture works
    print("Hello", file=sys.stderr)

# Generated at 2022-06-14 13:14:49.896040
# Unit test for function product
def test_product():
    """
    UnitTest for the function product.

    Raises
    ------
    AssertionError
        If results are not successful.
    """
    # Test 1
    raise Exception('TODO')


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:14:53.633491
# Unit test for function product
def test_product():
    from .tests import run_product
    run_product(product)

# Generated at 2022-06-14 13:15:00.407670
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    # pylint: disable=line-too-long
    import numpy as np

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        import warnings
        warnings.warn("Matplotlib not found: no plots will be shown.")
        plt = None

    # pylint: disable=expression-not-assigned
    [int(i) for i in tqdm_auto.product(range(10))]
    [int(i) for i in tqdm_auto.product(range(10))]
    [int(i) for i in tqdm_auto.product(range(10))]
    [int(i) for i in tqdm_auto.product(range(10))]

# Generated at 2022-06-14 13:15:07.096707
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    from ..utils import FormatCustomText
    from ..std import sys

    for p in product('ABCD', 'xy', total=None):
        sys.stdout.write(''.join(p))
        sys.stdout.flush()

    for p in product(range(2), repeat=3, tqdm_class=FormatCustomText):
        pass

    try:
        from itertools import product as i_product
    except ImportError:
        pass
    else:
        for p in product(range(100)):
            assert next(i_product(range(100))) == p


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:15:17.075509
# Unit test for function product
def test_product():
    """Unit test for product"""
    from ..utils import FormatCustomText as __
    from ._utils import _screen_shape

    # Sanity check
    assert tqdm_auto(1) == tqdm_auto(itertools.product([1]), total=1)
    assert tqdm_auto(0, 1, desc=1) == tqdm_auto(itertools.product([0], [1]),
                                                total=1, desc=1)
    assert tqdm_auto(range(3)) == tqdm_auto(itertools.product(range(3)),
                                            total=3)
    assert tqdm_auto(desc=0) == tqdm_auto(itertools.product([]), desc=0)

    # Return type test

# Generated at 2022-06-14 13:15:18.272159
# Unit test for function product
def test_product():
    fr

# Generated at 2022-06-14 13:15:22.644849
# Unit test for function product
def test_product():
    """Unit test for tqdm.itertools.product"""
    it = product(range(10), repeat=2, tqdm_class=tqdm_auto.tqdm,
                 unit='test units')
    assert len(list(it)) == 100
    # Check that kwargs are passed
    it = product(range(10), repeat=2, tqdm_class=tqdm_auto.tqdm,
                 unit='test units', miniters=1, ascii=True)
    assert len(list(it)) == 100

# Generated at 2022-06-14 13:15:29.316523
# Unit test for function product
def test_product():
    from nose.tools import assert_equal
    import numpy as np
    from pdb import set_trace

    input_size = 3

    # Initialize data
    data = np.random.randint(0, 2**32 - 1, size=input_size)

    # Run product
    p = list(product(data))

    # Run itertools
    ip = list(itertools.product(data))

    # Check
    assert_equal(p, ip)

# Generated at 2022-06-14 13:15:37.163966
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    ip = iter(product(range(3), repeat=2))
    assert next(ip) == (0, 0)
    assert next(ip) == (0, 1)
    assert next(ip) == (0, 2)
    assert next(ip) == (1, 0)

if __name__ == '__main__':
    from . import _test_func
    _test_func(test_product)
    print("All tests passed.")

# Generated at 2022-06-14 13:15:46.343539
# Unit test for function product
def test_product():
    """test_product
    Examples
    --------
    >>> list(product(["a", "b"], ["c", "d"], ["e", "f"]))
    [('a', 'c', 'e'), ('a', 'c', 'f'), ('a', 'd', 'e'), ('a', 'd', 'f'), ('b', 'c', 'e'), ('b', 'c', 'f'), ('b', 'd', 'e'), ('b', 'd', 'f')]
    """
    from .tqdm import trange

# Generated at 2022-06-14 13:15:55.495420
# Unit test for function product
def test_product():
    from .tests import TestCase
    from numpy.testing import assert_equal

    def prod_no_tqdm(iterables):
        return list(itertools.product(*iterables))

    class TestProduct(TestCase):
        """Test case for function product"""
        _multiprocess_can_split_ = True

        def test_product(self):
            for iterables in (
                    (), ([],),
                    ([1], [2]),
                    ([1, 2], [3, 4], [5, 6])):
                assert_equal(
                    product(*iterables),
                    prod_no_tqdm(iterables),
                    err_msg=iterables)

# Generated at 2022-06-14 13:16:11.739479
# Unit test for function product
def test_product():
    """
    Simple unit test for function `product`.
    """
    import random
    import string
    random.seed(42)

    for _ in tqdm_auto.tqdm(range(200)):
        size = random.randint(1, 5)
        _str = ''.join(random.choice(string.ascii_uppercase)
                       for _ in range(size))
        _str_list = [_str for _ in range(size)]
        n = random.randint(1, 5)
        m = random.randint(1, 5)
        for x in product(_str_list, repeat=n):
            assert isinstance(x, tuple)
            assert len(x) == n
            for y in x:
                assert y in _str_list

# Generated at 2022-06-14 13:16:18.363994
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    a = range(20)
    L = [0, 0, 0]
    for i, j, k in tqdm.itertools.product(a, a, a):
        L[0] += 1
        L[1] += i * j * k
        L[2] += i * i * j * j * k * k

    assert L == [8000, 102739200, 68428805568000]

# Generated at 2022-06-14 13:16:29.278229
# Unit test for function product
def test_product():
    from ..utils import UnknownLength
    # Test 1: No iteration
    assert list(product([], repeat=2, tqdm_class=None)) == []
    # Test 2: Unknown lengths
    assert list(product([1, 2, 3], [1], tqdm_class=None)) == [(1, 1), (2, 1), (3, 1)]
    assert list(product([1, 2, 3], UnknownLength, tqdm_class=None)) == [(1, None), (2, None), (3, None)]
    assert list(product([1, 2, 3], UnknownLength, UnknownLength, tqdm_class=None)) == [(1, None, None), (2, None, None), (3, None, None)]
    # Test 3: Visualisation
    # Known lengths

# Generated at 2022-06-14 13:16:33.194055
# Unit test for function product
def test_product():
    from ._utils import TrainMonitor
    from ._utils import monitor_sleep as sleep

    monitor = TrainMonitor()
    monitor.start()

    for _ in product(*[range(10) for _ in range(10)], total=100,
                     tqdm_class=monitor.__class__):
        sleep()

    monitor.pause()
    assert len(monitor.sp) == 100
    assert all([sp["n"] == 1 for sp in monitor.sp])
    monitor.close()

# Generated at 2022-06-14 13:16:38.712192
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from .tests_tqdm import with_unit_option, closing_iter

    for _ in range(2):
        for i in with_unit_option(product(closing_iter(), repeat=2)):
            pass
    for i in with_unit_option(product(closing_iter(), repeat=2),
                              ascii=True):
        pass

# Generated at 2022-06-14 13:16:48.423899
# Unit test for function product
def test_product():
    import sys

    def test_total():
        for t in range(1, 10):
            assert sum(1 for _ in product(range(t), total=t)) == t
            assert sum(1 for _ in product(range(t+1), total=t)) == t

    def test_len():
        for t in range(1, 10):
            assert sum(1 for _ in product(range(t))) == t
            assert sum(1 for _ in product(range(t+1))) == t+1

    test_len()
    test_total()


# Generated at 2022-06-14 13:16:57.432278
# Unit test for function product
def test_product():
    from collections import Counter
    from .utils import capture_stdout

    result_tuple = Counter(product(range(0, 10), repeat=2))
    assert len(result_tuple) == 100
    assert sum(result_tuple.values()) == 100

    result_dict = Counter(product(
        {'a': 1, 'b': 2}, repeat=2))
    assert len(result_dict) == 4
    assert sum(result_dict.values()) == 4

    with capture_stdout() as io:
        for _ in tqdm_auto.tqdm(product(range(10), repeat=2)):
            pass
        assert len(io.getvalue())
        assert "100%|" in io.getvalue()

# Generated at 2022-06-14 13:17:08.760510
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    import io
    import sys
    with io.StringIO() as our_file:
        # Capture output to our_file
        with redirect_stdout(our_file):
            with tqdm_auto(total=10) as t:
                for i in product(range(3), range(3), range(3), tqdm_class=tqdm_auto):
                    t.update()

        # Assert that the captured output matches "expected"
        with open(__file__.replace('.pyc', '.py'), 'r', encoding='utf-8') as expected_file:
            expected = expected_file.read()
        our_out = our_file.getvalue()
        from ast import literal_eval

# Generated at 2022-06-14 13:17:16.883598
# Unit test for function product
def test_product():
    """
    Test if tqdm(range(3)) range works.
    """
    from ..tqdm import trange

    assert list(product('ABCD', repeat=2)) == \
        [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'),
         ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'),
         ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'),
         ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D')]


# Generated at 2022-06-14 13:17:26.948270
# Unit test for function product
def test_product():
    assert tuple(product(range(3), tqdm_class=None)) == ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))

# Generated at 2022-06-14 13:17:48.200781
# Unit test for function product
def test_product():
    from .tests import TestCase, closing
    from .utils import _range

    with closing(TestCase()) as tc:
        for i in product(_range(10)):
            tc.assertEqual(i, 9)

        for i in product(_range(10), _range(10)):
            tc.assertEqual(i, (9, 9))

        for i in product(_range(10), _range(10), _range(10)):
            tc.assertEqual(i, (9, 9, 9))

        tc.assertEqual(list(product(_range(3), repeat=3)),
                       [(i, i, i) for i in _range(3)])


# Generated at 2022-06-14 13:17:57.600979
# Unit test for function product
def test_product():
    """
    Basic test for function `product`.
    """
    import numpy as np
    from .utils import FormatTemplate, SimpleNamespace
    from .tests_tqdm import tests_data

    class MockTqdm():
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def update(self, n=1):
            pass

    # Check product
    test_iter = (np.random.randint(0, 10, 100),
                 range(0, 10),
                 np.random.randint(0, 10, 100))
    my_iter = product(*test_iter, tqdm_class=MockTqdm)

# Generated at 2022-06-14 13:18:02.904916
# Unit test for function product
def test_product():
    from .tests import TestCase
    from .utils import closing, StringIO


# Generated at 2022-06-14 13:18:13.355151
# Unit test for function product
def test_product():
    from random import shuffle, randint
    g = product(range(10), range(20), [1,2,3], tqdm_class=tqdm_auto)
    assert list(g) == list(itertools.product(range(10), range(20), [1,2]))
    g = product(range(100), range(100), range(100), tqdm_class=tqdm_auto)
    t = []
    for i in g:
        # if randint(1, 100) == 1:  # 1% chance of error
        #     raise IOError()
        t.append(i)
    shuffle(t)
    for (i, j) in zip(t, itertools.product(range(100), range(100), range(100))):
        assert i == j
    # Ensure total

# Generated at 2022-06-14 13:18:22.283695
# Unit test for function product
def test_product():
    from .tqdm import trange
    from .utils import format_time

    # Test the time estimation
    with trange(10, mininterval=0.1) as t:
        for i in product(xrange(50000), "abcdefghijklmnopqrstuvwxyz"):
            t.update()

    # Test auto status_printer
    with trange(10, desc="foo", mininterval=0, miniters=1) as t:
        for i in product(xrange(50000), "abcdefghijklmnopqrstuvwxyz"):
            t.update()

    # Test the output

# Generated at 2022-06-14 13:18:25.896829
# Unit test for function product
def test_product():
    assert list(product(range(6), repeat=2)) == [
        (i, j) for i in range(6)
        for j in range(6)]
    assert list(product(range(6))) == list(range(6))



# Generated at 2022-06-14 13:18:29.046952
# Unit test for function product
def test_product():
    assert list(product(range(5), range(5))) == itertools.product(range(5), range(5))
    assert list(product(range(5), range(5), tqdm_class=None)) == itertools.product(range(5), range(5))

# Generated at 2022-06-14 13:18:32.210848
# Unit test for function product
def test_product():
    from itertools import product
    from .utils import StringIO

    with StringIO() as f:
        for i in product('ABCD', 'xy', tqdm_class=tqdm_auto, file=f):
            pass
        f.seek(0)
        assert '33it/s' in f.read()

# Generated at 2022-06-14 13:18:35.702304
# Unit test for function product
def test_product():
    lst = [list(map(str, range(3))),
           list(map(str, range(2)))]
    result = [' '.join(i) for i in product(*lst,
                                           tqdm_class=tqdm_auto)]
    assert result == ['0 0', '0 1', '1 0', '1 1', '2 0', '2 1']

# Generated at 2022-06-14 13:18:44.795272
# Unit test for function product
def test_product():
    """
    Tester function for `product`.
    """
    # pylint: disable=protected-access
    it = product(range(3), range(3), range(3))
    assert list(it) == list(range(3)) * 3
    assert it._instances['total'] == 27  # pylint: disable=no-member

    it = product(range(3), range(3), range(3), tqdm_class=tqdm_auto)
    assert list(it) == list(range(3)) * 3
    assert it._instances['total'] == 27  # pylint: disable=no-member

# Generated at 2022-06-14 13:19:17.184728
# Unit test for function product
def test_product():
    """Unit test for function product"""
    for e in product(['a', 'b', 'c'],
                     ['a', 'b', 'c'],
                     ['a', 'b', 'c'],
                     tqdm_class=tqdm_auto):
        pass
    for e in product('abc',
                     ['a', 'b', 'c'],
                     ['a', 'b', 'c'],
                     tqdm_class=tqdm_auto):
        pass
    assert e == ('c', 'c', 'c')


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:19:24.041622
# Unit test for function product
def test_product():
    """Unit test for function `product`."""
    import numpy as np
    a = np.arange(5)
    b = np.arange(5).reshape(5, 1)
    t = []
    for _a, _b in product(a, b, tqdm_class=tqdm_auto, miniters=20):
        t.append((_a, _b))
    assert np.all(a == [x[0] for x in t])  # check 1st item
    assert np.all(b == [x[1] for x in t])  # check 2nd item

# Generated at 2022-06-14 13:19:31.539208
# Unit test for function product
def test_product():
    "Tests for `product`."
    # Test first with a *multiprocessing* class
    try:
        multiprocessing = __import__('multiprocessing')  # NOQA
    except ImportError:
        pass
    else:
        from ..multiprocessing import tqdm as mp_tqdm
        from ..utils import _environ_cols_wrapper
        iterables = [range(2), range(2), range(2)]
        with _environ_cols_wrapper(40):
            assert "".join(str(x) for x in
                           product(*iterables, tqdm_class=mp_tqdm)) == \
                "".join(str(x) for x in itertools.product(*iterables))

# Generated at 2022-06-14 13:19:39.831148
# Unit test for function product
def test_product():
    import sys
    if sys.version_info < (3, 0):
        from contextlib import nested

# Generated at 2022-06-14 13:19:42.941014
# Unit test for function product
def test_product():
    """Test whether product works the same as itertools.product"""
    for _ in range(10):
        args = [list(range(i)) for i in range(1, 10)]
        assert all(
            it == tq for it, tq in zip(
                itertools.product(*args), product(*args, tqdm_class=None)))

# Generated at 2022-06-14 13:19:53.450612
# Unit test for function product
def test_product():
    import itertools as it
    import math
    import random
    import string

    def product(*iterables):
        """Equivalent of itertools.product."""
        if len(iterables) == 0:
            yield ()
        else:
            for item in iterables[0]:
                for items in product(*iterables[1:]):
                    yield (item,) + items

    total_runs = 1000
    test_range = 100
    max_size = 5

    for _ in tqdm_auto(range(total_runs)):
        # Generate test case
        size = random.randint(0, max_size)

# Generated at 2022-06-14 13:19:58.326518
# Unit test for function product
def test_product():
    for i, x in enumerate(
            tqdm_auto.product(range(10),
                              range(10),
                              "abcd",
                              iterable=range(10),
                              desc="Test", ascii=True)):
        if i == 99:
            break
    assert i == 99

# Generated at 2022-06-14 13:19:59.680096
# Unit test for function product
def test_product():
    from .tests import test_product
    test_product(product)


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:20:03.907169
# Unit test for function product
def test_product():
    with tqdm_auto(unit="B", unit_scale=True, unit_divisor=1024) as t:
        for i in product("ABCD", "xy", tqdm=t):
            pass
        assert t.n == 4 * 2

# Generated at 2022-06-14 13:20:12.645523
# Unit test for function product
def test_product():
    """Unit test for function product"""
    import numpy as np
    import pandas as pd
    from pandas.util.testing import assert_frame_equal
    from numpy.testing import assert_array_equal

    # Test case 1
    expected = [['a', 0],
                ['a', 1],
                ['a', 2],
                ['b', 0],
                ['b', 1],
                ['b', 2],
                ['c', 0],
                ['c', 1],
                ['c', 2]]
    result = list(product(['a', 'b', 'c'], [0, 1, 2]))
    assert_array_equal(result, expected)

    # Test case 2

# Generated at 2022-06-14 13:21:12.840100
# Unit test for function product
def test_product():
    from random import randint
    from operator import mul
    from .utils import FormatCustomText


# Generated at 2022-06-14 13:21:18.703197
# Unit test for function product
def test_product():
    """
    Unit test for `itertools.product`
    """
    # Setting up variables
    l = [3, 2, 5]
    it = list(itertools.product(*(range(i) for i in l)))
    # Testing no total
    assert list(product(range(i) for i in l)) == it
    # Testing with total

# Generated at 2022-06-14 13:21:24.003385
# Unit test for function product
def test_product():
    """
    Test for `tqdm.itertools.product`.
    """
    from .tests.common import IN, _range

    assert list(product(_range(2), _range(2))) == list(itertools.product(_range(2), _range(2)))
    assert list(product(_range(2), _range(2))) == [(0, 0), (0, 1), (1, 0), (1, 1)]

    assert IN in ''.join(map(str, product(_range(2), _range(2), _range(2), _range(2))))

# Generated at 2022-06-14 13:21:27.743493
# Unit test for function product
def test_product():
    for i in product([1, 2, 3], ['a', 'b']):
        pass
    for i in product([1, 2, 3], ['a', 'b'], tqdm_class=tqdm_auto.tqdm):
        pass

# Generated at 2022-06-14 13:21:37.854647
# Unit test for function product
def test_product():
    """
    Unit test for function :func:`tqdm.itertools.product`
    """
    from numpy.random import randint
    from numpy import product as np_product

    def tqdm_product(r, *iterables):
        """
        Equivalent of `itertools.product` with `range(r)`
        """
        return product(*([range(r)] + list(iterables)))

    def prod(r, *iterables):
        """Equivalent of numpy.product with `range(r)`"""
        return np_product(([r] + list(iterables)))


# Generated at 2022-06-14 13:21:40.922394
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    for i in product("XYZ", "ABCdefg", [1, 2, 3]):
        assert isinstance(i, tuple)
        for e in i:
            assert isinstance(e, str) or isinstance(e, int)
        assert len(i) == 3

# Generated at 2022-06-14 13:21:45.119727
# Unit test for function product
def test_product():
    with tqdm_auto(total=0) as t:
        assert list(product(range(3), tqdm_class=tqdm_auto,
                            tqdm_kwargs={"total": None})) \
            == list(itertools.product(range(3)))

# Generated at 2022-06-14 13:21:55.420011
# Unit test for function product
def test_product():
    import numpy as np

# Generated at 2022-06-14 13:22:03.477185
# Unit test for function product
def test_product():
    from ..auto import tqdm
    assert list(product(range(4), repeat=2)) == list(itertools.product(range(4), repeat=2))
    assert list(product(range(3), range(3))) == list(itertools.product(range(3), range(3)))
    list(product(range(2), repeat=2))
    with tqdm(total=None, unit="a", unit_scale=True, unit_divisor=1024) as t:
        for _ in product(range(2), repeat=2):
            t.update()
    with tqdm(total=None, unit="a", unit_scale=True, unit_divisor=1024) as t:
        t.update(2)
        for _ in product(range(2), repeat=2):
            t.update

# Generated at 2022-06-14 13:22:12.888611
# Unit test for function product
def test_product():
    """Test the product function"""
    from numpy.random import randint
    from time import sleep
    from .utils import format_sizeof

    a = randint(0, 5, size=10)
    b = randint(0, 5, size=10)
    for ab in tqdm(product(a, b)):
        pass

    for ab in tqdm(product(a, b)):
        sleep(0.05)

    for ab in tqdm(product(a, b), total=len(a) * len(b)):
        sleep(0.05)

    try:
        for ab in tqdm(product(a, b), total=len(a) * len(b) + 1):
            sleep(0.05)
    except AssertionError:
        pass
