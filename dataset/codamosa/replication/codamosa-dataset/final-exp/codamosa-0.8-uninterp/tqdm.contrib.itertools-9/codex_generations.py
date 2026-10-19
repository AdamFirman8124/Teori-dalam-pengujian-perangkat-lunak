

# Generated at 2022-06-14 13:12:25.378459
# Unit test for function product
def test_product():
    import numpy as np
    res = np.array(list(product(range(3), repeat=2)))
    assert (res == np.array([
        [0, 0], [0, 1], [0, 2],
        [1, 0], [1, 1], [1, 2],
        [2, 0], [2, 1], [2, 2],
    ])).all()

    res = np.array(list(product(*[range(2)]*4)))
    assert (res == 2**4) == (res.size == 2**4)

# Generated at 2022-06-14 13:12:28.557953
# Unit test for function product
def test_product():
    for a, b in product([1, 2], [1, 2, 3], tqdm_class=tqdm_auto.tqdm_gui):
        assert a <= 2
        assert b <= 3

# Generated at 2022-06-14 13:12:40.400783
# Unit test for function product
def test_product():
    from numpy.testing import assert_equal, assert_almost_equal
    try:
        from inspect import signature
        assert signature
    except ImportError:
        pass  # Python 2.7 fallback
    else:
        assert len(signature(product).parameters) == 2
    assert_equal(len(list(product(range(0)))), 0)
    assert_equal(len(list(product(range(1)))), 1)
    assert_equal(len(list(product(range(5)))), 5)
    assert_equal(len(list(product(range(3), range(3)))), 9)
    assert_equal(len(list(product(range(3), range(3), range(3)))), 27)
    assert_equal(len(list(product(range(3), repeat=3))), 27)

# Generated at 2022-06-14 13:12:42.706058
# Unit test for function product
def test_product():
    for n in product((0, -1, 1), (1, 2, 3), tqdm_class=tqdm_auto):
        assert -3 <= sum(n) <= 3

# Generated at 2022-06-14 13:12:51.969802
# Unit test for function product
def test_product():
    import numpy as np
    it = product(range(10), range(10), range(10), range(10),
                 range(10), range(10), range(10), range(10), tqdm_class=None)
    assert next(it) == (0, 0, 0, 0, 0, 0, 0, 0)
    assert next(it) == (0, 0, 0, 0, 0, 0, 0, 1)
    assert (np.all(np.array(list(it)) ==
                   np.array([(0, 0, 0, 0, 0, 0, 0, i) for i in range(2, 10)])))
    it = product(range(10), tqdm_class=None)
    assert next(it) == (0,)
    assert next(it) == (1,)

# Generated at 2022-06-14 13:13:04.709272
# Unit test for function product
def test_product():
    from operator import mul

    from . import trange

    from ..utils import chunkate

    for t in trange(chunkate(range(4), 3), total=4, miniters=1):
        assert sum(t) == sum(range(4))

    for t in trange(chunkate(range(4), 3), total=4, miniters=1, leave=False):
        assert sum(t) == sum(range(4))

    for t in trange(product(range(3), range(3), range(3)), total=27,
                    miniters=1):
        assert sum(t) == sum(map(mul, [0, 1, 2] * 3))


# Generated at 2022-06-14 13:13:10.985389
# Unit test for function product
def test_product():
    import numpy as np
    import tqdm
    num_reps = np.int(1e6)
    with tqdm.trange(num_reps) as t:
        for i in product(range(10), range(10), tqdm_class=tqdm.tqdm):
            pass


# Alias for backwards-compatibility
itertools.product = product

# Generated at 2022-06-14 13:13:19.613409
# Unit test for function product
def test_product():
    # pylint: disable=protected-access
    from numpy.testing import assert_equal
    from .tqdm import trange
    from .utils import FormatCustomTextExtension
    from .std import tqdm

    def prod(*iterables):
        res = []
        for i in product(*iterables):
            res.append(i)
        return res

    assert_equal(list(prod(range(5), range(2))),
                 list(itertools.product(range(5), range(2))))
    assert_equal(list(prod(range(5), range(2))),
                 list(product(range(5), range(2))))

    # test custom text
    def format_custom(self):  # pylint: disable=no-self-argument
        return "foo"

# Generated at 2022-06-14 13:13:30.589625
# Unit test for function product
def test_product():
    from .main import tqdm_object

    for i in product([1, 2, 3], repeat=3, tqdm_kwargs={"total": 10}):
        assert i in itertools.product([1, 2, 3], repeat=3)
        assert tqdm_object.total == 10
    for i in product([1, 2, 3], repeat=3, tqdm_kwargs={"total": 10}, tqdm_class=tqdm_auto):
        assert i in itertools.product([1, 2, 3], repeat=3)
        assert tqdm_object.total == 10
    for i in product([1, 2, 3], repeat=3, tqdm_class=tqdm_auto):
        assert i in itertools.product([1, 2, 3], repeat=3)

# Generated at 2022-06-14 13:13:40.629402
# Unit test for function product
def test_product():
    """
    Unit tests for function product.
    """
    from .tests_python import _test_tqdm_stdout
    from .tests_tqdm_gui import _test_tqdm_gui
    from .tests_python import _test_tqdm_pandas
    from .tests_tqdm import _test_tqdm_notebook
    from .tests_tqdm import _test_tqdm_wget
    from .tests_tqdm import _test_tqdm_main_progress_bar

    with _test_tqdm_stdout():
        list(product(range(5)))
    with _test_tqdm_stdout():
        list(product(range(5), range(5)))

# Generated at 2022-06-14 13:14:15.843843
# Unit test for function product
def test_product():
    import numpy as np
    from ..tests.test_misc import closing
    from ..utils import format_sizeof, format_interval
    from ..utils import format_meter
    from ..utils import chunk, format_num
    from ..utils import format_interval
    from ..utils import Percentage, ETA, FormatCustomTextExtension, \
        CounterExtension, SimpleProgress, FileTransferSpeed, ResizableFill

    def test_product_bar(bar_format):
        from collections import namedtuple
        from ..utils import _locale_en_US
        Observation = namedtuple('Observation', ['b', 'c', 'd'])

# Generated at 2022-06-14 13:14:22.030197
# Unit test for function product
def test_product():
    from .tqdm import _term_move_up
    from .utils import _range

    for i in product(_range(4), _range(4), _range(4), tqdm_class=tqdm_auto):
        pass

    for i in product(_range(4), _range(4), _range(4), tqdm_class=tqdm_auto):
        pass

    for i in product(_range(8), _range(8), _range(8), tqdm_class=tqdm_auto):
        pass

    # Multiline
    for i in product(_range(2), _range(2), _range(2), tqdm_class=tqdm_auto):
        _term_move_up()

# Generated at 2022-06-14 13:14:31.472438
# Unit test for function product
def test_product():
    import pytest

    def test(name, tqdm_class):
        kwds = {}
        if name != "no_tqdm":
            kwds["tqdm_class"] = tqdm_class
        assert list(product(range(2), repeat=3, **kwds)) == \
            list(itertools.product(range(2), repeat=3))

    for tqdm_class in [tqdm_auto, None]:
        test("tqdm", tqdm_class)
        test("no_tqdm", tqdm_class)

    # Test that "total" argument is respected
    with tqdm_auto(total=3) as t:
        kwds = {"tqdm_class": tqdm_auto}

# Generated at 2022-06-14 13:14:35.132621
# Unit test for function product
def test_product():
    import sys
    try:
        iter1 = range(1000)
        it = product(iter1)
        next(it)
    except:
        return False
    else:
        total1 = 1
        for i in iter1:
            total1 *= i
        for i in it:
            pass
        return True

# Generated at 2022-06-14 13:14:42.800910
# Unit test for function product
def test_product():
    """Simple unit test for function product"""
    from ..utils import format_sizeof
    for n in range(2, 11):
        for tqdm_class in (tqdm_auto, tqdm_auto.tqdm):
            assert format_sizeof(tqdm_class(n, unit="s").total) == "n**%d" % (
                n)
            assert format_sizeof(tqdm_class(n, unit="s").total) == format_sizeof(
                len(list(product(range(n), repeat=n, tqdm_class=tqdm_class))))


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:14:52.222857
# Unit test for function product
def test_product():
    """Test function `product`."""
    import numpy as np
    from numpy.testing import assert_array_equal
    from numpy.testing import assert_raises

    r1, r2, r3 = range(3), range(3), range(3)
    assert_array_equal(list(product(r1, r2, r3)),
                       list(itertools.product(r1, r2, r3)))
    assert_raises(
        TypeError, list, product(r1, r2, "bar"))

    for cls in [tqdm_auto, tqdm_auto.tqdm, tqdm_auto.tqdm_notebook]:
        r1, r2, r3 = range(3), np.arange(3), set(range(3))
        assert_array_

# Generated at 2022-06-14 13:14:59.490919
# Unit test for function product
def test_product():
    """
    Test for function product.
    """
    from numpy.random import randint
    from ..utils import format_interval
    from .trange import trange

    # Test 1: String iterables
    assert list(product("ABC", "D")) == [('A', 'D'), ('B', 'D'), ('C', 'D')]

    # Test 2: Integer iterables
    for total in (1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377):
        with trange(total=total) as t:
            for _ in product(range(total)):
                t.update()
        assert t.n == total

    # Test 3: Integer iterables (non-uniform)

# Generated at 2022-06-14 13:15:05.464755
# Unit test for function product
def test_product():
    with tqdm_auto(disable=True) as tqdm_obj:
        assert 0 == sum(1 for _ in product(iter(list(range(10))))) * 2
        assert 0 == sum(1 for _ in product(iter(list(range(10))), tqdm_class=tqdm_obj)) * 2
        pi = product(iter(list(range(10))), iter(list(range(10))),
                     tqdm_class=tqdm_obj)
        assert sum(1 for _ in pi) == 100

# Generated at 2022-06-14 13:15:13.876375
# Unit test for function product
def test_product():
    with product("ABC", "XYZ") as p:
        assert(list(itertools.product("ABC", "XYZ")) == list(p))
    with product("ABC", "XYZ", tqdm_class=tqdm_auto) as p:
        assert(list(itertools.product("ABC", "XYZ")) == list(p))
    with product("ABC", "XYZ", total=9) as p:
        assert(list(itertools.product("ABC", "XYZ")) == list(p))


if __name__ == "__main__":
    test_product()

# Generated at 2022-06-14 13:15:17.171495
# Unit test for function product
def test_product():
    """Unit test for function product"""
    list(product(range(3), range(3), (1, 2), tqdm_class=None))
    list(product(['a', 'b', 'cd'], range(2), tqdm_class=tqdm_auto))

# Generated at 2022-06-14 13:16:30.442528
# Unit test for function product
def test_product():
    import pandas as pd
    import itertools as it
    from pandas.util.testing import assert_frame_equal, assert_series_equal

    all_iterables = [
        ['abc', 'def', 'gh', ''],
        [1, 2, 3, 4]]

    def product_tests(a, b):
        try:
            assert_frame_equal(
                pd.DataFrame(a),
                pd.DataFrame(b),
                check_names=False)
        except:
            assert_series_equal(
                pd.Series(a),
                pd.Series(b),
                check_names=False)

    for iterables in all_iterables:
        product = tqdm_auto(it.product(*iterables))

# Generated at 2022-06-14 13:16:33.128530
# Unit test for function product
def test_product():
    assert list(product(range(5), repeat=2)) == \
        list(itertools.product(range(5), repeat=2))
    assert list(product(range(5), repeat=2, tqdm_class=None)) == \
        list(itertools.product(range(5), repeat=2))

# Generated at 2022-06-14 13:16:43.711136
# Unit test for function product
def test_product():
    """Test that product is equivalent to itertools.product"""
    assert list(product([])) == list(itertools.product([]))
    assert list(product([1])) == list(itertools.product([1]))
    assert list(product([1, 2])) == list(itertools.product([1, 2]))
    assert list(product([1, 2], repeat=0)) == list(
        itertools.product([1, 2], repeat=0))
    assert list(product([1, 2], repeat=1)) == list(
        itertools.product([1, 2], repeat=1))
    assert list(product([1, 2], repeat=2)) == list(
        itertools.product([1, 2], repeat=2))

# Generated at 2022-06-14 13:16:45.069788
# Unit test for function product
def test_product():
    list(product(range(0, 1000), range(0, 1000)))