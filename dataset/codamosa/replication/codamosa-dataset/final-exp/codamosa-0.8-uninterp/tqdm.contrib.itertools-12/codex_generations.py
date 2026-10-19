

# Generated at 2022-06-14 13:12:34.877142
# Unit test for function product
def test_product():
    """
    Make sure product works as expected.
    """
    assert list(product([1, 2], [3, 4])) == [(1, 3), (1, 4), (2, 3), (2, 4)]

# Generated at 2022-06-14 13:12:46.146611
# Unit test for function product
def test_product():
    iterable = product('ABCD', 'xy')
    assert iterable.next() == ('A', 'x')
    assert ''.join(iterable) == 'AyAzBxByBzCxCyCzDxDyDz'
    assert ''.join(product('ABC', repeat=2)) == 'AAABBBCCC'
    assert ''.join(product(range(2), repeat=3)) == '000 010 001 011 100 110 101 111'
    assert ''.join(product('ABC', repeat=2)) == 'AAABBBCCC'
    assert ''.join(product(range(2), repeat=3)) == '000 010 001 011 100 110 101 111'
    assert ''.join(product('ABC', 'xy')) == 'AxAyBxByCxCy'

# Generated at 2022-06-14 13:12:49.636959
# Unit test for function product
def test_product():

    iterables = [
        [1, 2, 3],
        [10, 11, 12],
        [100, 101, 102]
    ]
    assert type(product(*iterables)) == type(itertools.product(*iterables))

# Generated at 2022-06-14 13:13:01.551849
# Unit test for function product
def test_product():
    import numpy as np
    from ..tqdm import trange
    A = list(range(10))
    B = np.arange(5)
    C = list('abcd')

    # NB: this is not exactly the same as:
    # for i in trange(10):
    #     for j in range(5):
    #         for k in 'abcd':
    #             X += (i, j, k)
    #             # ...do something with X...
    #             X -= (i, j, k)
    # since the trange verbosity is not updated
    # at each iteration
    X = []
    for (i, j, k) in product(trange(10), range(5), 'abcd'):
        X += (i, j, k)
        # ...do something with X...

# Generated at 2022-06-14 13:13:03.725472
# Unit test for function product
def test_product():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:13:14.964707
# Unit test for function product

# Generated at 2022-06-14 13:13:19.398630
# Unit test for function product
def test_product():
    from .tests_tqdm import with_statement
    with with_statement(range(1000)) as t:
        for i in product(range(100), range(100),
                         tqdm_class=t.__class__, postfix={"s1": "s2"}):
            pass
        assert t.n == 10000
        assert t.postfix == {"s1": "s2"}

# Generated at 2022-06-14 13:13:21.539180
# Unit test for function product
def test_product():
    product(range(3), range(3))


# Generated at 2022-06-14 13:13:29.303427
# Unit test for function product
def test_product():
    from ..tests.states import states_obj
    for i, j in product(*states_obj):
        assert len(i) == 2 and len(j) == 2
    # no states_obj
    for _ in product(states=None):
        pass
    # no streams
    for _ in product(states=states_obj, close=True, disable=True):
        pass
    # no states_obj, streams
    for _ in product(states=None, close=True, disable=True):
        pass


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:13:39.860949
# Unit test for function product
def test_product():
    import sys
    import os
    import time
    # Test parallel

# Generated at 2022-06-14 13:13:50.569202
# Unit test for function product
def test_product():
    import pytest
    list(product('XY', repeat=4, tqdm_class=tqdm_auto))
    with pytest.raises(KeyError):
        list(product('XY', repeat=4, tqdm_class=tqdm_auto, foo=1))
    with pytest.raises(TypeError):
        list(product('XY', repeat=4, tqdm_class=1))

# Generated at 2022-06-14 13:13:58.142201
# Unit test for function product
def test_product():
    with tqdm_auto() as t:
        assert repr(t) == \
            "<tqdm_autonotebook.tqdm_autonotebook.tqdm_autonotebook " \
            "object at 0x" in repr(t)
        assert t.total is None

        for i in product(range(10), tqdm_auto=tqdm_auto):
            assert i == (0, 0)
            break

        assert t.total == 10**2

        for i in product(range(10), tqdm_auto=tqdm_auto):
            assert i[0] == i[1]

# Generated at 2022-06-14 13:14:08.366645
# Unit test for function product
def test_product():
    from .tqdm import _range
    from .utils import _term_move_up

    with tqdm_auto(total=4, leave=None) as t:
        for _ in product("abcd", "xy", tqdm_class=tqdm_auto,
                         tqdm_kwargs={"leave": None}):
            t.write("test_product")

    # dynamic total count
    with tqdm_auto() as t:
        for _ in product("abcd", "xy", tqdm_class=tqdm_auto,
                         tqdm_kwargs={"leave": None}):
            t.update(1)

    # no total count when non-numeric items

# Generated at 2022-06-14 13:14:12.002496
# Unit test for function product
def test_product():
    import doctest
    doctest.testmod(name='tqdm.itertools', extraglobs={})
    if test_product.__doc__ is not None:
        doctest.run_docstring_examples(product, globals())

# Generated at 2022-06-14 13:14:13.327131
# Unit test for function product
def test_product():
    """Test function `product`"""
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 13:14:22.273137
# Unit test for function product
def test_product():
    from .tests_tqdm import FakeTqdmFile, closing

    # Nested list comprehension with product
    with closing(FakeTqdmFile(open(__file__))) as f:
        for _ in tqdm_auto(product(range(10), range(20), range(30)),
                           file=f):
            pass
    assert f.cleared_lines  # Check that tqdm(..., file=f) works
    assert f.get_fp().getvalue().count(
        ' 100%') == 1, "There should be one progress line"

    # Nested list comprehension with product

# Generated at 2022-06-14 13:14:28.074005
# Unit test for function product
def test_product():
    import numpy as np
    from .utils import format_sizeof
    from .utils import format_interval
    from .utils import format_meter
    from .utils import format_number
    from .utils import format_timespan

    for i, k in enumerate(product(range(1000), range(10 ** 6), repeat=2)):
        pass

    i = np.arange(10000)
    k = np.arange(10000)
    arr = np.array(list(product(i, k)))

    t = tqdm_auto(total=10000, desc="product", unit="it",
                  ascii=True, miniters=1, file=sys.stdout)
    for i, k in product(range(10000), range(10000)):
        t.update()
    t.close()

    # Test

# Generated at 2022-06-14 13:14:30.430947
# Unit test for function product
def test_product():
    from ..utils import _range
    for i in _range(10):
        assert(list(product(_range(i), _range(i))) ==
               list(itertools.product(_range(i), _range(i))))

# Generated at 2022-06-14 13:14:37.287465
# Unit test for function product
def test_product():
    """Unit test for function product"""
    import cStringIO as StringIO
    import sys

    def lines(out):
        return out.getvalue().split('\n')


# Generated at 2022-06-14 13:14:43.437247
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from .utils import FormatWidget

    widgets = [FormatWidget("a{}", "b"), " ",
               FormatWidget("c{}", "d"), " ",
               FormatWidget("e{}", "f"), " ",
               FormatWidget("g{}", "h")]

    for i in product("abc", "def", "ghi", tqdm_class=tqdm_auto,
                     leave=True, widget=widgets):
        pass

# Generated at 2022-06-14 13:14:55.767819
# Unit test for function product
def test_product():
    from .utils import format_sizeof
    from ..auto import tqdm

    # Itertools product
    p = itertools.product(range(10))
    assert sum(1 for _ in p) == 10

    p = itertools.product(range(10))
    assert sum(1 for _ in p) == 10

    p10 = list(itertools.product(range(10)))
    assert len(p10) == 10**len(p10[0])
    assert sum(1 for _ in p10) == 10**len(p10[0])

    p101 = list(itertools.product(range(10), range(10)))
    assert len(p101) == 10**len(p101[0])
    assert sum(1 for _ in p101) == 10**len(p101[0])

    p

# Generated at 2022-06-14 13:15:01.545476
# Unit test for function product
def test_product():
    '''
    Unit test
    '''
    expected = [
        (1, 1,1), (1, 1,2), (1, 2,1), (1, 2,2),
        (2, 1,1), (2, 1,2), (2, 2,1), (2, 2,2)
    ]
    output = [i for i in product([1, 2],[1, 2],[1, 2], total=8)]
    assert output == expected

# Generated at 2022-06-14 13:15:06.290824
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    kwargs = {}
    total = 1
    for i in [10, 10, 10]:
        total *= i
    kwargs.setdefault("total", total)
    with tqdm_auto(**kwargs) as t:
        iterables = [range(10)] * 3
        for i in itertools.product(*iterables):
            assert len(i) == 3
            t.update()

# Generated at 2022-06-14 13:15:13.251042
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    from .tests import TestTqdmIterable, closing
    from .std import StringIO

    lst1 = [1, 2, 3]
    lst2 = ["a", "b"]

    @closing(StringIO())
    def wrapper(file):
        for x in tqdm_auto(product(lst1, lst2),
                           desc="product", file=file):
            pass

    TestTqdmIterable().check(wrapper)

# Generated at 2022-06-14 13:15:20.597005
# Unit test for function product
def test_product():
    from ..compatibility import StringIO
    with StringIO() as StringLikeIO:
        for c in product(range(10), range(10), range(10),
                         tqdm_class=tqdm_auto, file=StringLikeIO):
            pass
        try:
            assert len(StringLikeIO.getvalue().split('\r')) == 101
        except AssertionError:
            try:
                assert len(StringLikeIO.getvalue().split('\n')) == 101
            except AssertionError:
                raise AssertionError("len(StringIO().split(\\r)) != 101")
        else:
            assert len(StringLikeIO.getvalue().split('\r')) == 101
        finally:
            StringLikeIO.close()

# Generated at 2022-06-14 13:15:30.453612
# Unit test for function product
def test_product():
    """Test function product"""
    from . import pretest_posttest
    from tqdm.tests import unittest
    from tqdm.tests.class_ultratb import CaptureStdout

    # Setup
    def func(*args, **kwargs):
        return list(product(*args, **kwargs))

    funcs = [func, itertools.product]

    with pretest_posttest(capture_stdout=CaptureStdout) as _stdout:
        for func in funcs:
            func([1, 2, 3], [4, 5], [6])
            func(['a', 'b', 'c'], [4, 5], [6])
            func([1, 2, 3], ['a', 'b', 'c'], [6])

# Generated at 2022-06-14 13:15:33.855400
# Unit test for function product
def test_product():
    """Test for function `tqdm.itertools.product`"""
    from ._utils import _test_gen

    for n in range(1, 4):
        _test_gen(product, range(n))

# Generated at 2022-06-14 13:15:43.934079
# Unit test for function product
def test_product():
    """
    Test function product
    """
    from .utils import FormatTestCounter
    from .tqdm import trange
    from .utils import _range
    from .std import _range as range

    for a, b in product(['a', 'b', 'c', 'd'], range(2)):
        continue
    for a, b in product(['a', 1], range(2)):
        continue
    for a, b in product(range(1000), range(60)):
        continue
    for _, __ in product(_range(1000), range(0, 60)):
        continue
    for _, __ in product(_range(1000), range(60)):
        continue
    for _, __ in product(_range(6), _range(1)):
        continue

# Generated at 2022-06-14 13:15:49.534616
# Unit test for function product
def test_product():
    from ..utils import FastText, FastTextTelegram
    def _testit(tqdm_class=None):
        import numpy as np
        tqdm_kwargs = {'tqdm_class': tqdm_class}
        iterables = [range(5), range(5)]
        r = product(*iterables, **tqdm_kwargs)
        assert r is not None
        assert tqdm_class

    def test_none():
        _testit()

    def test_fasttext():
        _testit(FastText)
        _testit(FastTextTelegram)

    test_none()
    test_fasttext()

# Generated at 2022-06-14 13:15:59.168457
# Unit test for function product
def test_product():
    """
    Unit test examples for `tqdm.itertools.product`.

    Usage: `python -c "from tqdm.tests import test_product; test_product()"`
    """
    from ..defaults import DefaultMonitor


# Generated at 2022-06-14 13:16:14.021671
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from ..utils import format_sizeof
    iterables = [range(3), range(3)]
    total = 1
    lens = list(map(len, iterables))
    for i in lens:
        total *= i
    result = list(product(*iterables, tqdm_class=tqdm_auto))
    assert result == [(i, j) for i in range(3) for j in range(3)]
    assert format_sizeof.format_size(total, "o") == "9 bytes"

# Generated at 2022-06-14 13:16:24.406807
# Unit test for function product
def test_product():
    """
    Coverage: 80%
    Missing: tqdm_kwargs
    """
    from ..tests import closing, nullcontext
    from ..tests._utils import _range

    for l in (0, 1, 2):
        for j in _range(0, 1):
            with closing(tqdm_auto(0)) as t:
                # test regular usage
                assert list(product(_range(l), _range(l))) == list(itertools.product(range(l), range(l)))
                assert t.n == t.total
            with closing(tqdm_auto(0)) as t:
                assert list(product(_range(l), _range(j))) == list(itertools.product(range(l), range(j)))
                assert t.n == t.total

# Generated at 2022-06-14 13:16:32.568349
# Unit test for function product
def test_product():
    from contextlib import redirect_stdout
    from io import StringIO
    with tqdm_auto.app.wrapped_stdout() as file:
        with redirect_stdout(file):
            res = list(product(range(100), range(20),
                               range(10), range(100),
                               tqdm_class=tqdm_auto))
            assert res == list(itertools.product(range(100), range(20),
                                                 range(10), range(100)))
    assert "100it [00:00, 744.01it/s]" in file.getvalue()


if __name__ == "__main__":
    print(test_product())

# Generated at 2022-06-14 13:16:42.931196
# Unit test for function product
def test_product():
    """Test func: tqdm.itertools.product"""
    # pylint: disable=protected-access
    from .itertools import _prod
    from .utils import FormatStub, StringIO, RawIOBase, _range

    for cls in _range(tqdm_auto, FormatMixin=FormatStub):
        for nl in [True, False]:
            with StringIO() as file:
                with tqdm_auto(file=file, miniters=0, desc="",
                               leave=nl, disable=None, ascii=True) as pbar:
                    list(product(_range(10, 100), _range(2, 20),
                                 tqdm_class=cls,
                                 ))
                assert pbar.n == 90

# Generated at 2022-06-14 13:16:50.016099
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    from .utils import FormatStopIteration
    from .tqdm_gui import tqdm

    with FormatStopIteration():
        assert list(product([1, 2, 3], repeat=2)) == [
            (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        assert list(product([1, 2, 3], [4, 5])) == [
            (1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

# Generated at 2022-06-14 13:16:53.101584
# Unit test for function product
def test_product():
    """
    Unit test for function ``product``.
    """
    total_items = 10

# Generated at 2022-06-14 13:16:58.965239
# Unit test for function product
def test_product():
    """Unit test for function `product`"""
    from numpy.testing import assert_equal
    x = [1, 2]
    y = [3, 4]
    # Without total=
    assert_equal(list(product(x)), list(itertools.product(x)))
    assert_equal(list(product(x, y)), list(itertools.product(x, y)))
    # With total=
    assert_equal(list(product(x, total=2)), list(itertools.product(x)))
    assert_equal(list(product(x, y, total=4)), list(itertools.product(x, y)))

# Generated at 2022-06-14 13:17:03.664604
# Unit test for function product
def test_product():
    from .tests import pretest_product
    for iterables, total in pretest_product.items():
        t = tqdm_auto(total=total)
        for product_ in itertools.product(*iterables):
            t.update()
        t.close()

# Generated at 2022-06-14 13:17:13.181321
# Unit test for function product
def test_product():
    from .contrib.concurrent import thread_map
    import numpy as np

    with tqdm_auto(unit="B", miniters=1, leave=True) as t:
        for i, _ in enumerate(t):
            t.set_description("Generating %i" % i)
            yield i

    with tqdm_auto(unit="B", miniters=1, leave=True) as t:
        for i, _ in enumerate(t):
            t.set_description("Generating %i" % i)
            yield i

    sum(tqdm_auto(range(10), desc="1st loop"))
    sum(tqdm_auto(range(10), desc="2nd loop"))


# Generated at 2022-06-14 13:17:21.080749
# Unit test for function product
def test_product():
    import pytest
    import numpy as np
    from ..utils import numpy_interop

    @numpy_interop(np)
    def test(a, b):
        n = 0
        for i in product(a, b, tqdm_class=tqdm_auto):
            assert(len(i) == 2)
            n += 1
        return n

    assert(test([1, 2, 3], ["a", "b", "c"]) == 9)
    assert(test([1, 2, 3], "abc") == 9)
    assert(test((1, 2, 3), "abc") == 9)
    assert(test([1, 2, 3], np.array([1, 2, 3])) == 9)

# Generated at 2022-06-14 13:17:49.625457
# Unit test for function product
def test_product():
    from ...tests.py26 import skipped, TestCase

    # create a testcase that doesn't complain about `assertRaises`
    class TqdmTestCase(TestCase):
        def assertRaisesWithMessage(self, exc, msg=None):
            """
            See: http://stackoverflow.com/a/13674918/35070
            """
            context_copy = self.longMessage
            self.longMessage = False
            try:
                self.assertRaises(exc)
            except AssertionError as e:
                if not msg:
                    self.fail(e)
                else:
                    self.assertIn(msg, str(e))
            finally:
                self.longMessage = context_copy

    test_cases = TqdmTestCase()


# Generated at 2022-06-14 13:17:56.837656
# Unit test for function product
def test_product():
    from random import randint
    from random import random
    from .utils import FormatWrapBase

    class FormatWrap(FormatWrapBase):
        def format_meter(self, n):
            return "Test: [%s]" % (n,)

    for _ in range(50):
        for _ in range(1000):
            iterables = [randint(0, 1000) for i in range(randint(1, 10))]
            n = product(*iterables, tqdm_class=FormatWrap)
            list(n)


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:18:03.672543
# Unit test for function product
def test_product():
    from numpy import product as nprod
    from ..utils import FormatWrapBase, format_interval, tqdm
    from ..__main__ import _range

    N = 16
    M = 7
    K = 1000

    # Check basic usage
    assert sum(product(_range(N), _range(M))) == nprod(N, M) - 1

    # Check custom tqdm class usage
    class MyBar(FormatWrapBase):
        @property
        def format_dict(self):
            d = FormatWrapBase.format_dict.fget(self)
            d["rate"] = "custom rate"
            return d

    assert sum(product(_range(N), _range(M), tqdm_class=MyBar)) == nprod(N, M) - 1

    # Check with custom mininterval

# Generated at 2022-06-14 13:18:07.627419
# Unit test for function product
def test_product():
    from .utils import FormatWidget, ClosingString

    with FormatWidget("function ({})".format("product"), closing=ClosingString(" ")) as fw:
        for i in product([1, 2], [3, 4], ["a", "b"]):
            fw.update(i)
        fw.close()

# Generated at 2022-06-14 13:18:12.517963
# Unit test for function product
def test_product():
    assert (tuple(product(["a", "b", "c"], repeat=2)) ==
            tuple(itertools.product(["a", "b", "c"], repeat=2)))

if __name__ == "__main__":
    from .main import main
    main(__file__)

# Generated at 2022-06-14 13:18:21.663477
# Unit test for function product
def test_product():
    from .tests import TestCase
    from .utils import closing, SimpleTextIOWrapper
    from .std import StringIO

    # Test check `total` argument
    with closing(StringIO()) as our_file:
        with TestCase(tqdm_class=tqdm_auto) as tc:
            tc.assertRaises(AssertionError,
                            lambda: list(product('abc', tqdm=our_file)))
            tc.assertRaises(AssertionError,
                            lambda: list(product('abc', total=-1, tqdm=our_file)))
            tc.assertRaises(AssertionError,
                            lambda: list(product('abc', total=0, tqdm=our_file)))

    # Test `total` argument

# Generated at 2022-06-14 13:18:31.111454
# Unit test for function product
def test_product():
    assert list(product(range(2), range(2))) == [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert list(product(range(3), range(0))) == []
    assert list(product([], range(3))) == []
    assert list(product([], [])) == [()]
    assert list(product(range(2), repeat=2)) == [(0, 0), (1, 0), (0, 1), (1, 1)]
    assert list(product(range(2), repeat=3)) == [
        (0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1), (1, 0, 1),
        (0, 1, 1), (1, 1, 1)]

# Generated at 2022-06-14 13:18:34.876643
# Unit test for function product
def test_product():
    from ..utils import _term_move_up

    seq = []
    for i in product(range(2), range(3), range(4), range(5)):
        seq.append(i)

    assert seq == list(itertools.product(range(2), range(3), range(4), range(5)))

    print('Test `product`: ', end='')
    _term_move_up()

# Generated at 2022-06-14 13:18:44.601073
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from .. import trange
    from ..utils import _range
    from .tests_tqdm import pretest_posttest

    with pretest_posttest() as pt:
        for _ in trange(10, desc='outer'):
            for _ in trange(10, desc='inner'):
                list(_range(3))  # NOQA

    with pretest_posttest() as pt:
        for _ in product(range(10), desc='outer'):
            for _ in product(range(10), desc='inner'):
                list(_range(3))  # NOQA


if __name__ == "__main__":
    run_tests()

# Generated at 2022-06-14 13:18:47.928007
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    sum = 0
    for _ in product(range(100), tqdm_class=tqdm_auto):
        sum += 1
    # Done
    print("done!")
    assert sum == 100 ** 2

# Generated at 2022-06-14 13:19:33.261431
# Unit test for function product
def test_product():
    from . import trange
    from .utils import format_sizeof
    a = (2, 3, 4)
    b = (5, 6)
    total = len(a)*len(b)
    l = list(product(trange(len(a)), trange(len(b))))
    assert len(l) == total
    assert l == list(itertools.product(a, b))
    assert l == list(product(trange(len(a)), trange(len(b)),
                             tqdm_class=trange.trange))
    assert l == list(product(trange(len(a)), trange(len(b)),
                             tqdm_class=trange.trange,
                             bar_format='{bar}'))

# Generated at 2022-06-14 13:19:41.228233
# Unit test for function product
def test_product():
    from six.moves import range as xrange
    from .utils import closing, Disabled
    actual_results = list(product(xrange(4), xrange(4)))
    expected_results = [
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2), (2, 3),
        (3, 0), (3, 1), (3, 2), (3, 3)
    ]
    assert actual_results == expected_results, \
        "product() failed: expected {} but got {}".format(
            expected_results, actual_results)


# Generated at 2022-06-14 13:19:44.829631
# Unit test for function product
def test_product():
    """
    >>> import sys
    >>> from tqdm import tqdm, trange
    >>> from tqdm.utils import product

    >>> for i in trange(1000, file=sys.stdout):
    ...     for j in tqdm(list(range(100)), leave=True, file=sys.stdout):
    ...         for k in product(list(range(10)), list(range(10))):
    ...             pass
    """

# Generated at 2022-06-14 13:19:54.539758
# Unit test for function product
def test_product():
    from ..__init__ import tqdm
    from numpy import allclose, array

    def apply_func(func):
        return array([func(i) for i in range(3)]).reshape(3, 1)

    # 1D array
    assert allclose(apply_func(lambda i: i * 3),
                    array([0, 3, 6]))

    # 2D array

# Generated at 2022-06-14 13:20:05.430828
# Unit test for function product
def test_product():
    """Test function product"""
    import numpy as np
    import numpy.testing as npt

    # 1) test standard usage: psd combinations and no flattening
    # Create data
    params = {'a': [1,2], 'b': [3,4], 'c': [5,6]}

    # Get all possible parameter combinations
    all_param_combinations = list(product(params['a'],
                                          params['b'],
                                          params['c']))

    # Check with expected combinations
    expected = [[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]

# Generated at 2022-06-14 13:20:13.835412
# Unit test for function product
def test_product():
    from functools import partial

    def idx2xy(idx, nx, ny):
        """TODO: Docstring for idx2xy.

        :idx: TODO
        :returns: TODO

        """
        i = idx % nx
        j = idx // nx
        return i, j

    def seq(b):
        """TODO: Docstring for seq.

        :b: TODO
        :returns: TODO

        """
        return range(b)

    def not_in_seq(b, v):
        return filter(partial(ne, v), range(b))


# Generated at 2022-06-14 13:20:17.170158
# Unit test for function product
def test_product():
    try:
        with tqdm_auto() as t:
            for _ in product(range(10), range(10)):
                t.update(20)
    except Exception as e:
        raise e

# Generated at 2022-06-14 13:20:22.186540
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from .tests_basic import closing, formatted_timer  # NOQA
    from numpy import array, prod
    with closing(formatted_timer("tqdm.tqdm_product")) as timer:
        for _ in product(*map(range, range(0, 50))):
            pass
    assert int(prod(array(timer.elapsed) * [1000, 1])) < 4000


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:20:31.976085
# Unit test for function product
def test_product():
    # Check normal usage
    out = []
    for i in product(range(10), range(10), tqdm_class=tqdm_auto):
        out.append(i)
    assert len(out) == 100

    # Check normal usage with total
    out = []
    for i in product(range(10), range(10), tqdm_class=tqdm_auto):
        out.append(i)
    assert len(out) == 100

    # Check no total
    out = []
    for i in product(range(10)):
        out.append(i)
    assert len(out) == 10

# Generated at 2022-06-14 13:20:35.917594
# Unit test for function product
def test_product():
    """Test that tqdm_notebook works in non-notebook environments"""
    def generator():
        yield 1

    # Test that it works
    for _ in tqdm_auto.product(range(10), generator(), range(2), tqdm_class=tqdm_auto.tqdm_notebook):
        pass

# Generated at 2022-06-14 13:22:15.236154
# Unit test for function product
def test_product():
    """
    Unit test for `tqdm.itertools.product`.
    """
    for n in [1, 5, 10, 100, '20', '30', '10e1']:
        for m in [1, 5, 10, 100, '20', '30', '10e1']:
            # test via sum
            s = 0
            x = product(range(int(n)), range(int(m)))
            for _ in x:
                pass
            assert s == int(n) * int(m) - 1


if __name__ == '__main__':
    test_product()

# Generated at 2022-06-14 13:22:21.240807
# Unit test for function product
def test_product():
    assert product([1, 2, 3], [4, 5, 6], tqdm_class=tqdm_auto) !=\
        itertools.product([1, 2, 3], [4, 5, 6])
    assert list(product([1, 2, 3], [4, 5, 6], tqdm_class=tqdm_auto)) ==\
        list(itertools.product([1, 2, 3], [4, 5, 6]))

# Generated at 2022-06-14 13:22:23.663402
# Unit test for function product
def test_product():
    product(*[list(range(i, i+3)) for i in range(3)], ascii=True)
    product(*[list(range(i, i+3)) for i in range(3)], ascii=True, desc='test')

# Generated at 2022-06-14 13:22:32.040480
# Unit test for function product
def test_product():
    with tqdm_auto(total=24, desc="Casper") as t:
        for c in product("ABC", "xy", tqdm_class=tqdm_auto):
            pass
    assert t.n == len(list(itertools.product("ABC", "xy")))
    with tqdm_auto(total=12, desc="Casper") as t:
        for c in product((1, 2), repeat=3, tqdm_class=tqdm_auto):
            pass
    assert t.n == len(list(itertools.product((1, 2), repeat=3)))