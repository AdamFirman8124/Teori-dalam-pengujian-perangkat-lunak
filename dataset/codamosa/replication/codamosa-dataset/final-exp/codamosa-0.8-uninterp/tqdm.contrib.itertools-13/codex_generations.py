

# Generated at 2022-06-14 13:12:38.318136
# Unit test for function product
def test_product():
    from . import trange
    from random import random

    for n in trange(1, 100):
        for i in product(range(4), range(4), range(4), tqdm_class=trange):
            pass
        for i in product(range(4), range(4), range(4)):
            pass
    for n in trange(1, 100):
        for i in product(range(4), range(4), range(4), tqdm_class=trange):
            pass
        for i in product(range(4), range(4), range(4)):
            pass
    for i in trange(random()):
        pass


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:12:44.206354
# Unit test for function product
def test_product():
    """Unit test for product"""
    import pytest
    from .tests_tqdm import with_setup, _range
    # `product` must be tested in its own process
    with pytest.raises(TypeError):

        for t in product(_range(10), ["a", "b", "c"], _range(5)):
            print(t)
            raise TypeError

# Generated at 2022-06-14 13:12:49.141119
# Unit test for function product
def test_product():
    import numpy
    numpy.random.seed(0)
    x = numpy.random.randint(0, 10, size=5)
    y = numpy.random.randint(0, 10, size=5)
    assert all(i == (j, k) for i, j, k in zip(itertools.product(x, y), x, y))


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:12:51.696355
# Unit test for function product
def test_product():
    from ..utils import __AUTHORS__
    assert product(__AUTHORS__, ['foo', 'bar'], tqdm_class=None) == \
        itertools.product(__AUTHORS__, ['foo', 'bar'])

# Generated at 2022-06-14 13:12:58.034066
# Unit test for function product
def test_product():
    import tqdm
    # Given:
    iterator = product(range(10), "abcd", tqdm_class=tqdm.tqdm)
    # When:
    assert (list(iterator) == [x for x in itertools.product(
        range(10), "abcd")])

# Generated at 2022-06-14 13:13:09.612989
# Unit test for function product
def test_product():
    """
    Tests function `tqdm.itertools.product`
    """
    from ..std.itertools import product as std_product
    from ..std.itertools import tee as std_tee
    from ..utils import strip_braces
    from .tests import BaseTestMixin, closing, pretest_posttest

    with closing(tqdm_auto(total=1)) as t:
        t.update()
        a = list(std_product([1, 2], t))

    with closing(tqdm_auto(total=4)) as t:
        t.update()
        b = list(product([1, 2], t))

    with closing(tqdm_auto(total=4)) as t:
        t.update()

# Generated at 2022-06-14 13:13:17.216184
# Unit test for function product
def test_product():
    """ Unit test for function product """
    p = list(product(range(10), range(20), range(30), tqdm_class=tqdm_auto.tqdm,
                     desc='perf', leave=True))
    assert p == [(i, j, k)
                 for i in range(10)
                 for j in range(20)
                 for k in range(30)]
    p = list(product(range(10), range(20), range(30)))
    assert p == [(i, j, k)
                 for i in range(10)
                 for j in range(20)
                 for k in range(30)]

# Generated at 2022-06-14 13:13:26.141127
# Unit test for function product
def test_product():
    from numpy.random import rand
    mat1 = rand(10, 3)
    mat2 = rand(10, 3)
    mat3 = rand(10, 3)
    res1 = list(product(mat1, mat2))
    res2 = list(product(mat1, mat2, mat3))
    assert len(res1) == len(mat1) * len(mat2)
    assert len(res2) == len(mat1) * len(mat2) * len(mat3)

# Generated at 2022-06-14 13:13:30.906807
# Unit test for function product
def test_product():
    "Check that product is correct"
    assert list(product(range(2), tqdm_class=None))
    assert list(product(range(3), tqdm_class=lambda *a, **k: None))
    assert list(product(range(4), tqdm_class=tqdm_auto))
    assert list(product(range(5), tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:13:35.958847
# Unit test for function product
def test_product():
    """Unit test for function product"""
    g = product(range(5), repeat=2)
    l = list(g)
    assert len(l) == 25, "Length of product(range(5), repeat=2) is not 25"


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:13:47.049712
# Unit test for function product
def test_product():
    from .tests import closing, closing_to_file
    from . import trange

    myzip = lambda *args: list(zip(*args))

    assert myzip() == [()]
    assert myzip('abc', [1, 2, 3]) == [('a', 1), ('b', 2), ('c', 3)]
    with closing(trange(10, desc='desc1')) as t1:
        with closing(t1(100)) as t2:
            with closing(t2(1000)) as t3:
                with closing(t3(10000)) as t4:
                    with closing(t4(100000)) as t5:
                        with closing(t5(1000000)) as t6:
                            res = list(myzip(t1, t2, t3, t4, t5, t6))

# Generated at 2022-06-14 13:13:48.999403
# Unit test for function product
def test_product():
    """Test for product"""
    import numpy as np
    assert list(product(range(3), range(4), range(5))) == \
        list(itertools.product(range(3), range(4), range(5)))

# Generated at 2022-06-14 13:13:51.930112
# Unit test for function product
def test_product():
    """
    Test `itertools.product` wrapper.
    """
    import sys
    for _ in product([1, 2], ["a", "b"], tqdm_class=tqdm_auto, file=sys.stdout):
        pass

# Generated at 2022-06-14 13:14:01.634820
# Unit test for function product
def test_product():
    import sys
    import os
    sys.argv[0] = os.path.basename(sys.argv[0])
    """Unit test for `itertools_ex.product`."""
    # Use dummy tqdm_class
    class Dummy:
        def __init__(self, **kwargs):
            self.total = kwargs.pop("total")
            self.count = 0

        def update(self):
            self.count += 1

    # Test that:
    #   * yields all the elements
    #   * updates progress bar properly
    total = 0
    for i in product(range(3), repeat=3, tqdm_class=Dummy):
        total += 1
        assert i == (total % 3, total % 3, total % 3)
    assert total == 27

    # Test that

# Generated at 2022-06-14 13:14:11.275234
# Unit test for function product
def test_product():
    """Test function `product`"""
    from .utils import FormatWrap
    import re
    import sys

    with FormatWrap(
            "[{bar}] {fmt_timer} {desc} {postfix}",
            bar_format='{l_bar}{bar}|',
            unit='it',
            unit_scale=True,
            disable=None,
            file=sys.stdout) as f:
        for x in product('ABCD', 'xy', tqdm_class=f):
            assert x == (x[0], x[1])
        f.reset(5)
        for x in product('ABCD', 'xy', tqdm_class=f):
            assert x == (x[0], x[1])



# Generated at 2022-06-14 13:14:14.031921
# Unit test for function product
def test_product():
    """Test product functions"""
    import sys
    import doctest
    sys.path.insert(0, '..')
    doctest.testmod()

if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:14:17.072531
# Unit test for function product
def test_product():
    """Unit test for function product"""
    assert sum(1 for _ in product(range(10), range(10))) == 100
    assert list(product(range(10), range(10))) == list(itertools.product(range(10), range(10)))

# Generated at 2022-06-14 13:14:20.028778
# Unit test for function product
def test_product():
    assert list(product([0, 1], [0, 2], [0, 3],
                        tqdm_class=tqdm_auto)) == \
           list(itertools.product([0, 1], [0, 2], [0, 3]))

# Generated at 2022-06-14 13:14:29.199176
# Unit test for function product
def test_product():
    """Test for function product"""
    try:
        from numpy import product as npprod
        npprod([])
    except:
        npprod = lambda x: 1
    from numpy import random
    x = random.randint(0, 9, size=10)
    y = random.randint(0, 5, size=7)

    try:
        assert not npprod(x)
        pytest.skip("numpy.product test disabled")
    except:
        pass

    for i in product(x, y, total=None):
        assert True
    for i in product(x, y, total=None):
        assert True
    for i in product(x, y, total=None):
        assert True
        break
    for i in product(x, y, total=None):
        pass

# Generated at 2022-06-14 13:14:31.270434
# Unit test for function product
def test_product():
    for a in product([1, 2, 3], ["a", "b", "c"], tqdm_class=tqdm_auto):
        pass

# Generated at 2022-06-14 13:14:46.170659
# Unit test for function product
def test_product():
    """Unit test for function product"""
    import numpy as np
    from ..utils import format_sizeof
    from .trange import trange
    from .tqdm import tqdm
    from .tqdm_pandas import tqdm_pandas

    def yield_from_product(product_iterable):
        for _ in product_iterable:
            pass

    def timing(total, desc, product_function, max_len=4, use_trange=False):
        lens = list(map(len, product_function))
        if use_trange:
            from .trange import trange
        else:
            from .tqdm import tqdm
        if isinstance(total, int):
            t = tqdm(total=total, desc=desc)

# Generated at 2022-06-14 13:14:53.648969
# Unit test for function product
def test_product():
    """
    Unit test for `itertools.product` wrapper.
    """
    try:
        from nose.tools import assert_equal
    except ImportError:
        raise unittest.SkipTest('nose not installed')
    for tqdm_cls in (tqdm_auto, tqdm_gui, tqdm_notebook, tqdm_ascii, tqdm):
        res = list(product([1, 2], [3.5], [60, 72], tqdm_class=tqdm_cls))
        assert_equal(res, [(1, 3.5, 60), (1, 3.5, 72),
                           (2, 3.5, 60), (2, 3.5, 72)])

# Generated at 2022-06-14 13:14:58.739689
# Unit test for function product
def test_product():
    from .utils import TestCase, pretest

    with TestCase(kargs={"disable": True}):
        pretest(product, 0, 1, 2, 3)
        pretest(lambda x: x, product(range(2), range(3)))
        pretest(lambda x: x, product(range(2), range(3), range(4)))
        pretest(lambda x: x, product(range(2)))
        pretest(lambda x: x, product(range(2), range(3), range(4),
                                     tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:15:00.177635
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """

# Generated at 2022-06-14 13:15:07.528733
# Unit test for function product
def test_product():
    """Test for function product"""
    from random import randint
    from .utils import FormatStdout

    with FormatStdout() as (out1, out2):
        for i in product(range(10), repeat=10):
            print(i, end=' ', file=out1)
        for i in product(range(10), repeat=10,
                         tqdm_class=tqdm_auto, desc="Test"):
            print(i, end=' ', file=out2)
    assert out1.getvalue().replace(' ', '') == out2.getvalue().replace(' ', '')


# Generated at 2022-06-14 13:15:13.539493
# Unit test for function product
def test_product():
    """Test function product"""
    from .tqdm_gui import tqdm

    for _ in product(range(10)):
        pass
    for _ in product(range(10), tqdm_class=tqdm):
        pass
    for _ in product(range(10), range(5), tqdm_class=tqdm):
        pass
    for _ in product(range(10), range(5), range(7), tqdm_class=tqdm):
        pass

# Generated at 2022-06-14 13:15:21.290951
# Unit test for function product
def test_product():
    """
    Returns
    -------
    True if successful.
    """
    d = dict(tqdm_class=tqdm_auto)
    assert list(product([1, 2], [3, 4], **d)) == \
        [i for i in itertools.product([1, 2], [3, 4])]
    assert list(product([1, 2], [], **d)) == []
    assert list(product([1, 2], repeat=0, **d)) == [()]
    assert list(product([1, 2], repeat=1, **d)) == [[1], [2]]
    assert list(product([1, 2], repeat=2, **d)) == \
        [i for i in itertools.product([1, 2], repeat=2)]

# Generated at 2022-06-14 13:15:27.614762
# Unit test for function product
def test_product():
    from ._utils import closing, _range

    @closing(range(10))
    def check(tqdm_cls):
        prod = list(tqdm_cls(product(_range(10), _range(10),
                                     _range(10), tqdm_class=tqdm_cls)))
        assert len(prod) == 1000

    yield (check,)

# Generated at 2022-06-14 13:15:37.734914
# Unit test for function product
def test_product():
    """
    Simple unit test for product().
    """
    from ..utils import FormatWrap
    from .std import tqdm
    from .gui import tqdm_gui

    def test_funcs(funcs):
        with FormatWrap(tqdm, fp=open(os.devnull, "w")) as format_wrap:
            for i in product(range(2), range(10), tqdm_class=funcs):
                pass
        assert format_wrap.smoothing == 0.0

    test_funcs(tqdm)
    test_funcs(tqdm_gui)

# Generated at 2022-06-14 13:15:46.761177
# Unit test for function product
def test_product():
    import numpy as np
    from ..utils import format_sizeof
    for iterables in [
            ((0, 1.), ('a', 'b'), ('A', 'B')),
            (tuple(range(x)) for x in range(4)),
            (np.arange(x) for x in range(4))]:
        prod = list(itertools.product(*iterables))
        assert list(product(*iterables)) == prod
        assert list(product(*iterables, tqdm_class=None)) == prod
        assert list(product(*iterables, miniters=1)) == prod
        assert list(product(*iterables, miniters=1, tqdm_class=None)) == prod
        assert list(product(*iterables, miniters=1, maxinterval=1)) == prod
    assert format_size

# Generated at 2022-06-14 13:15:59.276486
# Unit test for function product
def test_product():
    '''Unit test for function product.'''
    with tqdm_auto(total=16) as t:
        for _ in product(range(4), range(4),
                         tqdm_class=tqdm_auto, total=16):
            pass
        t.close()

# Generated at 2022-06-14 13:16:09.917140
# Unit test for function product
def test_product():
    from .tests import _test_iterable
    from .tests import _test_write_file

    # Sanity checks
    _test_iterable(itertools.product, lambda a: [''] if a == '' else a, 2)
    _test_iterable(itertools.product, lambda a: [''] if a == '' else a, 2, '')

    # Check that product(tqdm_class=X) works (it should use tqdm_auto)
    try:
        import __pypy__
    except ImportError:
        pass
    else:
        class foo(object):
            def __init__(self, *args, **kwargs): raise Exception()
            @property
            def total(self): raise Exception()

# Generated at 2022-06-14 13:16:14.601245
# Unit test for function product
def test_product():
    from ..utils import format_sizeof

    seq = range(6)
    n = 0
    for _ in product(seq, tqdm_class=tqdm_auto):
        n += 1
    assert n == 6 ** 2

    x = 6000000000
    n = 0
    for _ in product(xrange(x), xrange(x), tqdm_class=tqdm_auto):
        n += 1
    assert n == x ** 2

    print(format_sizeof(x ** 2))

# Generated at 2022-06-14 13:16:16.765222
# Unit test for function product
def test_product():
    from ..tqdm import main

    ranges = list(range(4))
    for i in main.product(*[ranges, ranges]):
        pass

# Generated at 2022-06-14 13:16:27.594897
# Unit test for function product
def test_product():
    from numpy.testing import assert_raises

    p = list(product([1, 2], [], [None, 'a'], tqdm=tqdm_auto))
    assert p == []

    p = list(product([1, 2], [], [None, 'a'], tqdm=tqdm_auto, total=4))
    assert p == []

    f = list(product([1, 2], [], [None, 'a'], tqdm_class=tqdm_auto))
    assert f == []

    f = list(product([1, 2], [], [None, 'a'], tqdm_class=tqdm_auto, total=4))
    assert f == []


# Generated at 2022-06-14 13:16:35.408693
# Unit test for function product
def test_product():
    import sys
    try:
        from shutil import get_terminal_size
    except ImportError:
        from backports.shutil_get_terminal_size import get_terminal_size
    from .utils import FontStatus
    from ..utils import format_sizeof
    import random
    try:
        from collections.abc import Iterable
    except ImportError:  # pragma: no cover
        from collections import Iterable

    # Internal function
    def verify_file_read(fd_in, md5sum_exp):
        """Verify that the sum of input file is equal to the expected"""
        import hashlib
        md5 = hashlib.md5()
        while True:
            data = fd_in.read(1024 * 8)
            if not data:
                break
            md5.update(data)
       

# Generated at 2022-06-14 13:16:45.520334
# Unit test for function product
def test_product():
    import sys

    assert list(product([1, 2, 3], repeat=2)) == [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3),
    ]

    assert list(product(range(4), repeat=2)) == [
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2), (2, 3),
        (3, 0), (3, 1), (3, 2), (3, 3),
    ]


# Generated at 2022-06-14 13:16:52.982047
# Unit test for function product
def test_product():
    """Unit test for function product"""
    from ._utils import TestCase, _range

    for iterable in (_range(2), range(2), (1, 0), ):
        for tqdm_class in (tqdm_auto, ):
            for repeat in (1, ):
                with TestCase(
                        msg="{}, {}, {}, {}".format(
                            iterable, tqdm_class,
                            repeat,
                            (iterable,) * repeat)):
                    with tqdm_class(total=2 * repeat) as t:
                        assert list(product(iterable, tqdm_class=tqdm_class,
                                            repeat=repeat)) == list(
                            itertools.product(iterable, repeat=repeat))
                        assert t.n == 2 * repeat
                        assert t.total == 2

# Generated at 2022-06-14 13:16:58.903218
# Unit test for function product
def test_product():
    import sys
    from ..utils import _range
    kwargs = {'miniters': 1, 'ascii': True,
              'disable': False, 'unit_scale': False,
              'unit': 'it', 'leave': False}
    # 1, 2, 3 = (1, 2, 3) = 1
    assert sum(x for x in product([1, 2, 3], tqdm_class=tqdm_auto, **kwargs)) == 1 * 2 * 3
    # 1, 2, 3, 4 = (1, 2, 3, 4) = 24
    assert sum(x for x in product([1, 2, 3, 4], tqdm_class=tqdm_auto, **kwargs)) == 1 * 2 * 3 * 4
    # 1, 2, 3 = (4, 5, 6) = 4

# Generated at 2022-06-14 13:17:03.010152
# Unit test for function product
def test_product():
    """Test for function product."""
    for i in product(*[['a', 'b', 'c'], [1, 2]], **{'tqdm_class': None}):
        pass

# Generated at 2022-06-14 13:17:31.657840
# Unit test for function product
def test_product():
    from .tests_tqdm import with_setup, pretest, posttest
    from .utils import FormatMixin, StringIO

    fn = lambda: product('ABCD', 'xy', tqdm_class=FormatMixin,
                         ascii=True, desc='test_product')

# Generated at 2022-06-14 13:17:38.376196
# Unit test for function product
def test_product():
    """Test function product"""
    from ..std import next

    # Normal case
    x = next(product([1, 2, 3], repeat=3))
    assert x == (1, 1, 1)
    x = next(product([1.5, 2], repeat=5))
    assert x == (1.5, 1.5, 1.5, 1.5, 1.5)
    x = next(product(["a", "b"], repeat=3))
    assert x == ("a", "a", "a")

    # Short circuit case
    x = next(product([1, 2, 3], repeat=3), None)
    assert x == (1, 1, 1)
    x = next(product([1.5, 2], repeat=5), None)

# Generated at 2022-06-14 13:17:41.902633
# Unit test for function product
def test_product():
    from .tqdm_test_cases import test_cases_itertools
    for n in [0, 1, 2, 10]:
        tqdm_kwargs = test_cases_itertools['float'](n)
        vals = (2, 4,)
        objs = product(*vals, tqdm_kwargs=tqdm_kwargs)
        list_obs = list(objs)
        exp = list(itertools.product(*vals))
        assert list_obs == exp



# Generated at 2022-06-14 13:17:52.186091
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from tqdm.utils import _supports_unicode

    # Unit tests
    assert list(product([], [], [], tqdm_class=tqdm_auto)) == []
    assert list(product(list(range(2)), repeat=2, tqdm_class=tqdm_auto)) == [
        (0, 0), (0, 1), (1, 0), (1, 1)]

    if _supports_unicode():
        # Test for Unicode support
        try:
            list(product(['\u0394'], ['\u03A6'], tqdm_class=tqdm_auto))
        except Exception as e:
            # Unicode not supported: let's move on
            pass

# Generated at 2022-06-14 13:17:58.225361
# Unit test for function product
def test_product():
    import numpy as np
    from .utils import SimpleHook

    thook = SimpleHook()
    for i in product(range(5), range(5), range(5),
            tqdm_class=tqdm_auto, leave=True,
            total=5**3,
            posthook=thook.post,
            mininterval=0.0001,
            maxinterval=0.001,
            smoothing=0.1):
        np.random.random(100)
    # Ensure that the total parameter is obeyed
    assert thook.n == 5**3

# Generated at 2022-06-14 13:18:05.244895
# Unit test for function product
def test_product():
    """
    Test that `tqdm.itertools.product` is equivalent to `itertools.product`

    Examples
    --------
    >>> from tqdm.itertools import product
    >>> list(product('ab', [1, 2])) == list(itertools.product('ab', [1, 2]))
    True
    >>> list(product([1, 2])) == list(itertools.product([1, 2]))
    True
    >>> list(product([1, 2], repeat=3)) == list(itertools.product([1, 2],
    ...     repeat=3))
    True
    """
    from .tests import tests
    import random

    tests(product)

    for i in range(5):
        a = random.randint(1, 20)
        b = random.randint

# Generated at 2022-06-14 13:18:13.546809
# Unit test for function product
def test_product():
    """ Test for function product"""
    for _ in product(range(5), repeat=5):
        break
    for _ in product(range(5), repeat=5, tqdm_class=tqdm_auto.tqdm_gui):
        break
    assert product(range(5), repeat=5) == itertools.product(range(5),
                                                           repeat=5)
    assert product(range(5), repeat=5, tqdm_class=tqdm_auto.tqdm_gui) == \
           itertools.product(range(5), repeat=5)

# Generated at 2022-06-14 13:18:22.437563
# Unit test for function product
def test_product():
    from ._utils import repr_long_iterable
    for V1, V2 in itertools.product(range(1, 4), range(4, 7)):
        # Product is not lazy:
        for kwargs in [{}, {"leave": True}]:
            r = list(product(range(V1), range(V2), tqdm_class=tqdm_auto,
                             **kwargs))
            assert r == list(itertools.product(range(V1), range(V2)))
            assert repr_long_iterable(r) == repr_long_iterable(
                itertools.product(range(V1), range(V2)))

    # test_exception_message_backward_compatibility:

# Generated at 2022-06-14 13:18:31.217581
# Unit test for function product
def test_product():
    import random
    import string
    random.seed(0)
    a = list(range(100))
    random.shuffle(a)
    b = list(range(1000))
    random.shuffle(b)
    c = list(range(10000))
    random.shuffle(c)
    d = list(range(100000))
    random.shuffle(d)
    e = list(string.ascii_lowercase)
    random.shuffle(e)
    f = list(string.ascii_uppercase)
    random.shuffle(f)
    g = list(range(1000))
    random.shuffle(g)
    h = list(range(100000))
    random.shuffle(h)


# Generated at 2022-06-14 13:18:34.991619
# Unit test for function product
def test_product():
    from tqdm.pyprind import trange
    for t in [trange, tqdm_auto, tqdm]:
        a = list(product('abcd', 'efgh', tqdm_class=t))
        assert ''.join(a[0]) == 'ae'
        assert ''.join(a[-1]) == 'dh'
        assert len(a) == (4 * 4)

# Generated at 2022-06-14 13:18:47.024971
# Unit test for function product
def test_product():
    """
    Unit test of product

    Returns
    -------
    True if unit test successful, else False
    """
    def _test_seq(g):
        """
        test sequence g
        """
        while True:
            try:
                v = g.next()
                assert v == (0, 0)
            except StopIteration:
                return True
    _test_seq(product(range(10), repeat=2, tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:18:53.499019
# Unit test for function product
def test_product():
    import numpy as np
    from tqdm.contrib.concurrent import thread_map
    from unittest import TestCase
    from multiprocessing import Pool

    # Plain
    with tqdm_auto(total=5+5*5) as t:
        assert all(len(i) == 3
                   for i in product(range(5), range(5), range(5)))
        assert sum(1 for _ in product(range(5), range(5), range(5))) == 5+5*5
        assert t.n == 5+5*5
        assert t.total == 5+5*5

    # Multiprocessing

# Generated at 2022-06-14 13:19:02.791337
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import numpy as np
    from ..std import numpy as tqdm_std

    def naive_product(*args, **kwargs):
        """
        Naive, CPU-intensive, unbuffered, and pure Python code of `product`.
        """
        for item in itertools.product(*args):
            tqdm_std.write(item)

    assert list(product(range(6), ["a", "b"])) == \
        list(itertools.product(range(6), ["a", "b"]))
    assert list(product(range(6), ["a", "b"], tqdm_class=None)) == \
        list(itertools.product(range(6), ["a", "b"]))

# Generated at 2022-06-14 13:19:13.204075
# Unit test for function product
def test_product():
    from numpy.testing import assert_equal
    from operator import mul
    from functools import reduce
    from itertools import product
    from ..utils import FormatCustomText

    format_custom_text = FormatCustomText()
    t = tqdm(product(range(10), repeat=2), ascii=True,
             miniters=0, mininterval=0,
             desc="test",
             file=format_custom_text)
    assert_equal(t.total, 100, msg="total mismatch ({} != {})".format(t.total,
                                                                      100))
    close_all()

# Generated at 2022-06-14 13:19:22.021005
# Unit test for function product
def test_product():  # pragma: no cover
    from numpy.testing import assert_allclose
    from random import randint, random
    import sys

    if sys.version_info < (3, 0):
        range = xrange

    def _product_2d(n, p, q):
        """
        Returns the first `n` elements of the list generated by
        `itertools.product(range(p), range(q))`.
        """
        return [next(itertools.islice(itertools.product(range(p), range(q)), n, None))
                for _ in range(6)]

    # Test 2D
    total = 0
    for i in (product(range(1000), tqdm_class=tqdm_auto) for _ in range(4)):
        for j in i:
            total += 1

# Generated at 2022-06-14 13:19:26.660815
# Unit test for function product
def test_product():
    """
    Test `itertools.product` on a simple loop
    """
    from .tests_tqdm import with_setup, pretest, posttest

    # Setup
    pretest()

    # Test

# Generated at 2022-06-14 13:19:33.705104
# Unit test for function product
def test_product():
    import sys
    import pytest

    def test_iter(iterables, total=None):
        """
        Generator-like test function.
        """
        for _ in tqdm_auto(product(*iterables), unit_scale=True):
            pass

    for iterables in ([[1, 2, 3], [4, 5, 6]],
                      [[1, 2, 3], [4.3, 5.6, 6.7]],
                      [range(10), range(100), range(1000)]):
        try:
            test_iter(iterables)
        except Exception as e:
            pytest.fail("product() raised an unexpected exception: %r" % e)

# Generated at 2022-06-14 13:19:41.655630
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    from ..utils import FormatCustomText, format_sizeof
    try:
        import numpy as np
    except ImportError:
        np = None

    nb_digits = 8
    gen1 = product(range(10), range(nb_digits), ["a", "b", "c"],
                   range(2 ** 3), range(2 ** 4))
    gen2 = itertools.product(range(10), range(nb_digits), ["a", "b", "c"],
                             range(2 ** 3), range(2 ** 4))
    for (a, b, c, d, e), (A, B, C, D, E) in zip(gen1, gen2):
        assert a == A
        assert b == B
        assert c == C

# Generated at 2022-06-14 13:19:47.123106
# Unit test for function product
def test_product():
    """
    Test that `tqdm.itertools.product` wrapper works correctly
    """
    import numpy as np
    from tqdm.auto import trange

    # NOTE: trange used rather than tqdm to avoid recursion
    it = product(trange(10), trange(7), tqdm_class=trange)
    assert (len(list(it)) == 10 * 7), "Wrong size"
    assert ([isinstance(x, tuple) for x in it] == [True] * 10 * 7), \
        "Not all tuples"
    assert (list(it) == list(product(range(10), range(7)))), \
        "Incorrect values"

    it = product(trange(10), trange(7), repeat=2, tqdm_class=trange)

# Generated at 2022-06-14 13:19:51.388769
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    from ..tqdm_gui import tqdm

    a = [1, 2, 3]
    b = [4, 5, 6]

    assert list(product(a, b, tqdm_class=tqdm)) == list(itertools.product(a, b))

# Generated at 2022-06-14 13:20:11.688939
# Unit test for function product
def test_product():
    def _test(a, b, total):
        for i, j in zip(a, b):
            assert i == j

    for N in [10, 100, 1000]:
        for n in [1, 5, 15]:
            a = list(range(n))
            b = list(product(*[a] * N))
            c = list(itertools.product(*[a] * N))
            assert list(b) == c
            _test(b, c, total=n ** N)
            _test(b, c, total=None)
            _test(b, c, total=n ** N + 1000)

# Test
if __name__ == "__main__":
    test_product()
    print("All tests passed")

# Generated at 2022-06-14 13:20:18.275780
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    I = list(range(5))
    K = list(product(I, I))
    assert len(K) == 25
    assert K[0] == (0, 0)
    assert K[-1] == (4, 4)

    J = list(product(I, I, key=sum))
    assert len(J) == 25
    assert J[0] == (0, 0)
    assert J[-1] == (4, 4)

    # test multi-pass iterator
    L = list(product(I, I))[10:15]
    assert L == [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:20:21.212789
# Unit test for function product
def test_product():
    r = list(range(5))
    assert list(product(r)) == list(product(r, tqdm_class=None)) == \
        list(itertools.product(r))


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:20:23.428834
# Unit test for function product
def test_product():
    assert list(product(range(4), repeat=4, tqdm_class=None)) == [(i, i, i, i)
                                                                  for i in range(4)]

# Generated at 2022-06-14 13:20:30.592207
# Unit test for function product
def test_product():
    import itertools as it
    from .utils import StabilityTest

    iterables = map(range, range(10))
    res = list(product(*iterables))
    assert res == list(it.product(*iterables))

    with StabilityTest(check="equal_to", verbose=True) as st:
        st.check_stability(lambda: list(product(*iterables)),
                           lambda: list(it.product(*iterables)))

# Generated at 2022-06-14 13:20:38.642731
# Unit test for function product
def test_product():
    from .utils import closing, FakeTqdmFile, StringIO

    iterables = [[], list(range(10)), list(map(str, range(3)))]
    string = "[]"
    for i in product(*iterables):
        assert i == ()

    for i in product(*iterables, tqdm_class=tqdm_auto):
        assert i == ()

    iterables = [[], list(range(10)), list(map(str, range(3)))]
    string = ("[{}]" * 3
              .format(*range(10), *range(3), *range(3)))
    with closing(StringIO()) as our_file:
        for i in product(*iterables, tqdm_class=tqdm_auto, file=our_file):
            pass
        assert our_file.getvalue() == string

# Generated at 2022-06-14 13:20:46.878322
# Unit test for function product
def test_product():
    import operator

    # Test for base cases
    assert list(product(list(range(1)))) == [0]
    assert list(product(list(range(1)), list(range(1)))) == [(0, 0)]
    assert list(product(list(range(1)), list(range(1)), repeat=0)) == [()]
    assert list(product(list(range(1)), repeat=1)) == [0]

    # Test for basic cases
    assert list(product(list(range(2)))) == list(range(2))
    assert list(product(list(range(2)), repeat=1)) == list(range(2))
    assert list(product(list(range(2)), repeat=2)) == [(0, 0), (0, 1), (1, 0), (1, 1)]

# Generated at 2022-06-14 13:20:57.565248
# Unit test for function product
def test_product():
    from .utils import SimpleNamespace
    from .tests import FakeTqdmFile, closing
    import os
    from collections import namedtuple
    from itertools import product

    t = FakeTqdmFile()
    ints = [1, 2, 4]
    it = product(ints, tqdm_class=tqdm_auto, tqdm_kwargs={"file":t})
    return_i = 0
    return_total = 0
    return_prod = [[1, 2, 4], [1, 2, 4], [1, 2, 4]]
    for i in it:
        assert i == return_prod[return_i]
        return_i += 1
        return_total += 1
    assert return_i == return_total

# Generated at 2022-06-14 13:21:05.225923
# Unit test for function product
def test_product():
    """
    Unit test for `itertools.product`
    """
    iterables = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

# Generated at 2022-06-14 13:21:15.083467
# Unit test for function product
def test_product():
    """ Test product """
    from .sigtools import _get_base
    with _get_base(unit_scale=True) as base:
        with tqdm_auto(ascii=True, total=100,
                       mininterval=0.1) as t:
            for _ in itertools.product(range(10), range(10),
                                       range(10), range(10), range(10),
                                       range(10), range(10), range(10)):
                t.update()
        assert t.total != base._total
    with _get_base(unit_scale=True) as base:
        for _ in product(range(10), range(10),
                         range(10), range(10), range(10),
                         range(10), range(10), range(10)):
            pass

# Generated at 2022-06-14 13:21:50.255256
# Unit test for function product
def test_product():
    def f(l):
        l = list(l)
        l.sort()
        return l


# Generated at 2022-06-14 13:21:56.862481
# Unit test for function product
def test_product():
    """
    Test function.
    """
    try:
        range = xrange
    except NameError:
        pass
    assert (list(product(range(3), range(3)))
            == list(itertools.product(range(3), range(3))))
    assert list(product([1, 2], repeat=2)) == [
        (1, 1), (1, 2), (2, 1), (2, 2)]
    assert (list(product([1, 2], repeat=3))
            == list(product([1, 2], [1, 2], [1, 2])))

# Generated at 2022-06-14 13:22:01.211438
# Unit test for function product
def test_product():
    seq = [range(5), range(5)]
    results = list(product(seq[0], seq[1]))
    assert len(results) == 25
    assert (4, 0) in results
    assert (4, 1) in results
    assert (4, 2) in results
    assert (4, 3) in results
    assert (4, 4) in results

# Generated at 2022-06-14 13:22:11.263714
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    from ..utils import format_sizeof
    import random

    with tqdm_auto(unit='B', unit_scale=True,
                   miniters=1, desc='Calculating') as t:
        iterables = [range(10), range(100), range(1000)]
        ret = sum(1 for _ in product(*iterables, tqdm_class=t))

    assert ret == 10 * 100 * 1000, "incorrect product result"
    assert len(t) == ret, "incorrect iteration count"
    assert len(str(t))
    assert 'desc' in str(t)
    assert 'Calculating' in str(t)
    assert 'elapsed' in str(t)
    assert 'it/s' in str(t)

# Generated at 2022-06-14 13:22:17.479914
# Unit test for function product
def test_product():
    """Test product"""
    assert list(product(range(2), range(2)))
    assert list(product(range(2), range(2), tqdm_class=None))
    assert list(product(range(2), range(2), tqdm_class=tqdm_auto))


if __name__ == "__main__":
    def _main():
        import doctest
        doctest.testmod()
    _main()

# Generated at 2022-06-14 13:22:24.993379
# Unit test for function product
def test_product():
    """
    Unit test for function product.
    """
    import numpy as np
    from .std import numpy

    total = 0
    for X, Y in numpy.product(
            np.array([[1, 2, 3], [4, 5, 6]]),
            np.array([[0, 1, 2]]),
            tqdm_class=numpy.tqdm,
            ):
        total += X + Y

    assert total == 30

    # OrderedDict {0: [1, 4], 1: [2, 5], 2: [3, 6]}
    total = 0

# Generated at 2022-06-14 13:22:34.669990
# Unit test for function product
def test_product():
    from .tests_tqdm import with_setup, PretendMutableSequence, closing

    with closing(PretendMutableSequence()) as s:
        def fxn():
            for _ in product(s, [1], tqdm_class=PretendMutableSequence):
                pass

        with_setup(setup=lambda: s.extend([1]), teardown=lambda: s.clear())(fxn)
        assert len(s) == 1
        assert s[0] == 2
        s.clear()

        with_setup(setup=lambda: s.extend([1, 2, 3]),
                   teardown=lambda: s.clear())(fxn)
        assert len(s) == 3
        assert s[0] == 2
        assert s[1] == 2
        assert s[2]