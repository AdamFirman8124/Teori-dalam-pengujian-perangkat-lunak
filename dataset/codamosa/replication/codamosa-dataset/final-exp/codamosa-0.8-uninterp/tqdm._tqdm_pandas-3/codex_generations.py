

# Generated at 2022-06-14 13:01:49.586832
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm._utils import _term_move_up

    def test_equals(lhs, rhs, msg=''):
        try:
            print(lhs, '\n  =?\n', rhs)
            assert lhs == rhs, msg
        except AssertionError:
            print('Error: %s\nPassed: %s\nExpected: %s' %
                  (msg, lhs, rhs))
            raise

    # Test pandas.core.groupby.DataFrameGroupBy.progress_apply
    test_df = pd.DataFrame({'a': [1, 2, 3], 'b': [1, 2, 3]})
    test_g = test_df.groupby('b')
   

# Generated at 2022-06-14 13:01:55.555765
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm import tqdm_pandas

    for x in tqdm(range(3), 'test tqdm'):
        print(x)

    try:
        tqdm_pandas(tqdm(range(3)))
    except DeprecationWarning:
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:07.452611
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm import TqdmTypeError

    try:
        from .tests_tqdm import closing, pretest_posttest  # NOQA
    except (ImportError, SystemError):
        from tests_tqdm import closing, pretest_posttest  # NOQA

    def slowgen():
        # generator that sleeps for 0.5 seconds between each iteration
        import time
        for i in range(5):
            yield i
            time.sleep(0.5)

    if not hasattr(pd, 'core'):
        return

    if hasattr(pd.core.groupby, 'progress_apply'):
        with closing(StringIO()) as our_file:
            pd.core.groupby.progress

# Generated at 2022-06-14 13:02:17.454411
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, TqdmWarning

    try:
        import pandas
        from pandas import DataFrame
    except ImportError:
        tqdm.write('Unit test not passed: pandas not installed')
        return

    # Create a random DataFrame
    df = DataFrame({
        'a': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'b': [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]})
    df = df.groupby('a').apply(lambda x: x)
    tqdm_pandas(tqdm)
    df.progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:29.316074
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    "Test function tqdm_pandas()."
    old_stderr = sys.stderr


# Generated at 2022-06-14 13:02:38.192725
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # test that the alias works
    x = tqdm.pandas()
    assert x.deprecated_t.__class__.__name__ == 'tqdm'  # The class of the returned tqdm instance
    return x

x = test_tqdm_pandas()

# E.g., import into existing script with:
# import tqdm; tqdm_pandas(tqdm)
#
# or:
# import tqdm as t; tqdm_pandas(t)

# It is important that this is after the `test_tqdm_pandas`, since the deprecation
# warning depends upon a class attribute that is only set after an instance is
# created.
from tqdm.pandas import tqdm_pandas

# Hook pandas `

# Generated at 2022-06-14 13:02:47.215010
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    try:
        import pandas
    except ImportError:
        return
    df = pandas.DataFrame(
        {'a': [None] * 10, 'b': np.random.randint(0, 10, 10)})
    gdf = df.groupby('b')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', TqdmDeprecationWarning)
        assert gdf.progress_apply(len).sum() == len(df)
    assert (gdf.progress_apply(len, tclass=tqdm)
            .sum() == len(df))
    assert (gdf.progress_apply(len, tclass=tqdm(total=len(df)))
            .sum() == len(df))

# Generated at 2022-06-14 13:02:58.843220
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.autonotebook import tqdm as tqdm_n

    test_df = pd.DataFrame(list(zip(range(10), range(10), range(10), range(10), range(10),
                                    range(10))),
                           columns=['a', 'b', 'c', 'd', 'e', 'f'])

    for tcls in [tqdm_n, tqdm_n(position=0)]:
        tqdm_pandas(tcls)
        assert tcls.n is None
        tqdm_pandas(tcls, total=len(test_df.groupby('a')))
        assert tcls.n == len(test_df.groupby('a'))
        tqdm

# Generated at 2022-06-14 13:03:09.036982
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm import trange
    from tqdm import TqdmExperimentalWarning

    df = pd.DataFrame({'x': range(10)})
    tqdm_pandas(tqdm, desc='testing', bar_format='{l_bar}')
    tqdm_pandas(tqdm, desc='testing2', bar_format='{l_bar}')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', TqdmExperimentalWarning)
        tqdm_pandas(tqdm, desc='testing3', bar_format='{l_bar}')
        tqdm_pandas(trange, desc='testing4', bar_format='{l_bar}')
       

# Generated at 2022-06-14 13:03:14.586534
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame(np.random.rand(1000, 1000))
    N = 10000
    with tqdm(total=N) as pbar:
        for _ in range(N):
            _ = df.progress_apply(lambda x: sum(x))
            pbar.update()

# Generated at 2022-06-14 13:03:27.785335
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import tqdm
        import pandas as pd
        import numpy as np
        # Create a dataframe
        df = pd.DataFrame({'A': np.random.rand(100)})
        tqdm_pandas(tqdm.tqdm)

        def sum(x):
            return x.sum()

        def sum_df(x):
            return x.groupby('A').progress_apply(sum)

        if sys.version_info[0] * 10 + sys.version_info[1] <= 26:
            assert sum_df(df) == 0
        else:
            assert sum_df(df) == 1

    except ImportError:
        pass
    except SyntaxError:
        pass

# Generated at 2022-06-14 13:03:35.491851
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    N = 10000
    M = 1000
    tdf = pd.DataFrame(index=range(M))
    tdf['test'] = 42
    result = tdf.progress_apply(lambda x: x + 42, axis=1)
    assert result.equals(tdf + 42)
    # ensure it re-registers correctly (gh-10)
    tdf.progress_apply(lambda x: x + 42, axis=1)


# Compatibility for `Series.progress_apply`

# Generated at 2022-06-14 13:03:41.739154
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    tp = tqdm.tqdm_pandas(tqdm.tqdm())
    assert isinstance(tp, tqdm.tqdm)
    tqdm.tqdm_pandas(tp)
    assert isinstance(tp, tqdm.tqdm)

# Decorator

# Generated at 2022-06-14 13:03:53.052627
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas
    from tqdm import trange
    from tqdm import tqdm
    import pandas as pd
    import numpy as np

    def func(df):
        return np.sum(df)

    df = pd.DataFrame(np.random.RandomState(0).rand(10000, 10))
    with tqdm(total=df.size) as pbar:
        res = df.groupby(len(df)).progress_apply(func, pbar=pbar)
    assert res.size == pbar.n, "{}: {} != {})".format(type(pbar), res.size, pbar.n)

    def func(df):
        return np.sum(df)


# Generated at 2022-06-14 13:03:56.242921
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.contrib import pandas
    assert pandas._tqdm_pandas is tqdm_pandas

# Generated at 2022-06-14 13:04:06.466931
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    import tqdm
    import tqdm.pandas
    import tqdm.auto

    tqdm.pandas(tqdm.auto.tqdm(ncols=60, ascii=False))
    tqdm_pandas(tqdm.auto.tqdm(ncols=60, ascii=False))

    def f(x):
        import time
        time.sleep(0.1)
        return x * 2

    df = pd.DataFrame({'a': [1, 2, 3, 4]})
    assert list(df.groupby('a').progress_apply(f)) == [2, 4, 6, 8]


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:16.894117
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from random import random

    def test_series(tqdm_class):
        # test series
        index = ['a', 'b', 'c', 'd', 'e']
        df = DataFrame(index=index)
        df['value'] = [random() for _ in index]

        tqdm_pandas(tqdm_class, leave=False, unit='unit')
        tqdm_class.close()
        result = df.value.progress_apply(lambda x: x + 1)
        assert result.equals(df.value + 1)

    def test_dataframe(tqdm_class):
        # test dataframe
        index = ['a', 'b', 'c', 'd', 'e']
        df = DataFrame(index=index)

# Generated at 2022-06-14 13:04:25.768887
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    `tqdm.pandas()` should work just like `tqdm_pandas()`
    """
    import numpy as np
    import pandas as pd

    tqdm = pandas_import_tqdm()
    pd.DataFrame({'a': [100 * np.random.random() for _ in range(100)]})\
        .groupby('a')[['a']].progress_apply(lambda x: x * 2,
                                            desc="group")

# Generated at 2022-06-14 13:04:38.086256
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm
    from tqdm import trange

    # Unit test 1
    arr = np.arange(100).reshape(10, 10)
    df = pd.DataFrame(arr)
    res = df.groupby(arr.mean(1)).progress_apply(lambda x: x.mean() * 10)
    assert np.allclose(res.values, arr.mean(1) * 10)

    arr = np.arange(10000).reshape(1000, 10)
    df = pd.DataFrame(arr)
    res = df.groupby(arr.mean(1)).progress_apply(
        lambda x: x.mean() * 10, miniters=10)

# Generated at 2022-06-14 13:04:43.709857
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame

    tqdm = tqdm_pandas(tqdm)
    DataFrame({'a': range(100)}).groupby('a').progress_apply(lambda x: x)

if __name__ == '__main__':
    test_tqdm_pandas()

# import tqdm
# tqdm_pandas(tqdm)
# df.groupby(['a', 'b']).progress_apply(func_a)

# Generated at 2022-06-14 13:04:56.807742
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Tests `tqdm_pandas` function (100% coverage).
    """
    import random
    import tqdm

    try:
        import pandas as pd
    except ImportError:
        return

    class Tqdm(tqdm.tqdm):
        def __init__(self, *args, **kwargs):
            tqdm.tqdm.__init__(self, *args, **kwargs)
            self._instances = []

        def pandas(self, *args, **kwargs):
            self._instances.append((args, kwargs))

    with Tqdm() as t:
        t.pandas(init='init')
        t.pandas(total=100)
        t.pandas(postfix='postfix')
    assert t._

# Generated at 2022-06-14 13:05:05.814188
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, tqdm_pandas

    df = pd.DataFrame({'x': [1, 2, 3, 4]})
    result = df.groupby(
        'x').progress_apply(
            lambda x: tqdm.pandas(x.x + 1)
        )
    assert result.equals(pd.DataFrame({'x': [2, 3, 4, 5]}))

    try:
        tqdm_pandas(
            tqdm, total=10, smoothing=0.05, dynamic_ncols=True, mininterval=0.1)
    except Exception as e:
        raise e
    else:
        print("Success tqdm_pandas!")


# Generated at 2022-06-14 13:05:17.276949
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest
    df = pd.DataFrame({'x': [1, 0] * 10})
    import tqdm
    tqdm.pandas(tqdm.tqdm())
    assert '\n' not in str(df.groupby('x').progress_apply(lambda x: x.sum()))
    tqdm.pandas(tqdm.tqdm(), leave=False)
    assert '\n' in str(df.groupby('x').progress_apply(lambda x: x.sum()))


if __name__ == "__main__":
    unittest.main()

# Generated at 2022-06-14 13:05:27.180707
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from numpy.random import randint

    x = randint(0, 100, 100)
    y = randint(0, 100, 100)
    df = DataFrame({'x': x, 'y': y})

    def func(a, b):
        return a.sum() + b.sum()

    with tqdm(total=df.groupby('x').progress_apply(func, 'y').shape[0]) as t:
        result = df.groupby('x').progress_apply(func, 'y',
                                                progress_kwargs={'t': t})
        t.update()
    return result, t

if __name__ == '__main__':
    _ = test_tqdm_pandas()

# Generated at 2022-06-14 13:05:35.896731
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # pip install pandas
    from pandas import DataFrame
    from random import randint
    from tqdm import tqdm, tqdm_gui
    from time import sleep

    try:
        from pandas.errors import DtypeWarning
    except ImportError:
        DtypeWarning = None

    try:  # pragma: no cover
        from pandas.errors import PerformanceWarning
    except ImportError:
        PerformanceWarning = None

    def demo_func(x):
        sleep(0.01)
        return x  # pragma: no cover

    # Demo 1: pandas.DataFrame.progress_apply and tqdm integration

# Generated at 2022-06-14 13:05:47.922766
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm_pandas, tqdm

    def f(df):
        return pd.DataFrame({'A': np.random.rand(df.shape[0])})


    df = pd.DataFrame({'A': np.random.rand(100)})
    tqdm.pandas(**tqdm_kwargs)
    tqdm_pandas(tqdm, **tqdm_kwargs)
    tqdm_pandas(tqdm())

    # tqdm_pandas(tqdm, **tqdm_kwargs)(td)
    # tqdm_pandas(tqdm(**tqdm_kwargs))(td)
    # tqdm_

# Generated at 2022-06-14 13:05:56.619120
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from numpy.random import randint, uniform
    from numpy import arange

    # useful for random reproducible DataFrames
    random_state = randint(0, 4294967296 - 1)
    try:
        # only works on Python 3.6+
        random_state = randint(0, 4294967296 - 1).to_bytes(length=8,
                                                           byteorder='little')
    except AttributeError:
        pass

    n = 100
    df = DataFrame(data=uniform(size=(n, n)), index=arange(n), columns=arange(n))
    s = Series(uniform(size=n), index=arange(n))


# Generated at 2022-06-14 13:06:01.521016
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # deprecated way
    try:
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm(range(10)))
    except TypeError:
        pass
    else:
        assert False, "Should be deprecated"

    # proper way
    tqdm.pandas(tqdm(range(10)))
    tqdm.pandas()


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:06.550705
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, TqdmDeprecationWarning

    with pytest.raises(TqdmDeprecationWarning):
        tqdm_pandas(tqdm)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:16.392309
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_pandas, pandas

    # Test deprecated arguments
    tqdm_pandas(tqdm_pandas)
    tqdm_pandas(tqdm_pandas)

    # Test pandas
    tqdm_pandas(tqdm_pandas)

    # Test correct output
    df = pd.DataFrame(index=range(10))
    df.groupby(df.index // 2).progress_apply(lambda x: x)
    df.groupby(df.index // 2).progress_apply(lambda x: x)
    with tqdm_pandas():
        df.groupby(df.index // 2).progress_apply(lambda x: x)

# Generated at 2022-06-14 13:06:27.154108
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    df = pd.DataFrame({'x': [1,2,3,4,5]})
    tqdm_pandas(tqdm, desc='test', ascii=True)
    print(df.groupby(['x']).progress_apply(lambda x: x))

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:33.243998
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import sys
    with tqdm_pandas(total=10) as t:
        assert t.total == 10
        assert sys.stderr.write in t.fp_write
    with tqdm_pandas(file=open('test', 'w')) as t:
        assert t.total is None
        assert t.fp_write == open('test', 'w').write


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:36.561445
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    from tqdm import tqdm

    tqdm_pandas(tqdm(0, 10))



# Generated at 2022-06-14 13:06:47.406600
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        import numpy as np
        import time
    except ImportError:
        warnings.warn("Unable to test function `tqdm_pandas`.")
    else:
        df = pandas.DataFrame(np.random.randint(0, 10, (100000, 6)))
        totals = []

        def nop(x):
            time.sleep(0.01)
            return x

        for i in range(8):
            t = tqdm_pandas(position=i, leave=False, file=sys.stdout)
            totals = df.groupby(i % 3).progress_apply(nop)
        assert_array_equal(df[0], totals[[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]])

# Generated at 2022-06-14 13:06:58.428010
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    t = tqdm(["a", "b", "c", "d"])
    tqdm_pandas(t)
    assert hasattr(t, 'pandas')
    assert not hasattr(tqdm_pandas, 'pandas')
    t = tqdm_pandas(t)  # no-op

    assert hasattr(DataFrame(), 'progress_apply')
    assert hasattr(DataFrame().groupby('a'), 'progress_apply')

    def f(x):
        return x

    tqdm.pandas(t)
    DataFrame({"a": [1, 2, 3, 4, 5]}).progress_apply(f)

# Generated at 2022-06-14 13:07:01.985571
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm_pandas as tp
    from tqdm.tests.test_pandas import unit_test as test
    import tqdm
    tqdm.pandas.tqdm_pandas = tp
    test()

# Generated at 2022-06-14 13:07:10.427821
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Test adapter
    import pandas as pd
    import numpy as np
    tqdm_pandas(pd.DataFrame())
    tqdm_pandas(pd.DataFrame().groupby(lambda x: x))
    tqdm_pandas(pd.Series(range(100)).groupby(lambda x: x))
    tqdm_pandas(pd.Series(range(100)).progress_apply)

    # Test auxiliary decorator
    df = pd.DataFrame({'vectors': [np.random.rand(100) for i in range(1000)]})

    def make_norm(x):
        from tqdm.autonotebook import tqdm
        return np.linalg.norm(x)


# Generated at 2022-06-14 13:07:15.223828
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas as pd
    from tqdm.pandas import TqdmPandasWarning
    from pandas.core.groupby import DataFrameGroupBy

    for t in [tqdm, tqdm.tqdm]:
        tqdm_pandas(t)
        assert 'progress_apply' in DataFrameGroupBy.__dict__
        t.pandas.deprecate()

# Generated at 2022-06-14 13:07:18.513095
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm(total=100))

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:28.834471
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    import pandas as pd
    try:
        import tqdm
    except ImportError:
        try:
            import tqdm_pandas
        except ImportError:
            pytest.skip("Pandas unit tests require tqdm")

    df = pd.DataFrame(index=range(100))
    with pytest.deprecated_call():
        tqdm_pandas.tqdm_pandas(tclass=tqdm, total=None)
    with pytest.deprecated_call():
        tqdm_pandas.tqdm_pandas(tclass=tqdm_pandas.tqdm, total=None)
    with pytest.deprecated_call():
        tqdm_

# Generated at 2022-06-14 13:07:48.577969
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.contrib import tqdm_pandas

    with tqdm_pandas(total=6) as pbar:  # can use `tqdm_gui`, `tqdm_notebook`,
        df = pd.DataFrame(
            {'x': [1, 2, 3, 4, 5, 6]})
        df.groupby(['x']).progress_apply(
            lambda x: df.set_value(x.name, 'y', sum(x)))


# Avoid tqdm_pandas import when tqdm.pandas is already available
if 'tqdm.pandas' not in sys.modules:
    tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:07:59.925674
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy import random
    from tqdm import tqdm_pandas

    # Generate some random test data
    df = DataFrame(random.randint(0, 100, (100000, 6)))

    # Register `pandas.progress_apply()` with `tqdm`
    # (can use `tqdm_gui`, `tqdm_notebook`, optional kwargs, etc.)
    tqdm_pandas(tqdm(desc="my bar!"))

    # Now you can use `progress_apply` instead of `apply`
    # and `progress_map` instead of `map`
    df.groupby(0).progress_apply(lambda x: x**2)

    # can also groupby list, the func would apply to each group
    df.group

# Generated at 2022-06-14 13:08:06.453924
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas.util.testing import makeDataFrame
    data = makeDataFrame()
    col_name = data.columns.tolist()[0]

    from tqdm.test import TqdmDeprecationWarning
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        tqdm_pandas(tqdm.tqdm)
        assert len(w) == 1
        assert issubclass(w[-1].category, TqdmDeprecationWarning)
        assert '`tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`' in str(w[-1].message)

# Generated at 2022-06-14 13:08:16.606458
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    import pandas
    import numpy as np
    import warnings
    import tqdm
    from tqdm.contrib import pandas as tqdm_pandas

    df = pandas.DataFrame({'x': np.random.randint(10, size=1000000)})

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        tqdm_pandas(tqdm)

    # should not raise
    for _ in df.groupby('x').progress_apply(lambda x: np.mean(x)):
        pass


# Generated at 2022-06-14 13:08:27.646851
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    try:
        from pandas import DataFrame
    except ImportError:
        from pandas.core.frame import DataFrame

    try:
        from tqdm.autonotebook import tqdm
    except ImportError:
        from tqdm import tqdm

    df = DataFrame(np.random.randint(0, 100, (100000, 6)))
    tq = tqdm_pandas(tqdm)
    df.groupby(0).progress_apply(
        lambda x: x**2)  # will automatically display a progress bar



# Generated at 2022-06-14 13:08:38.966450
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    # Testing adapter for tqdm_pandas
    with tqdm(total=100, file=sys.stdout) as pbar:
        tqdm_pandas(pbar)
        for i in range(100):
            pbar.update(1)
    print()

    # Testing adapter for tqdm
    with tqdm(total=100, file=sys.stdout) as pbar:
        tqdm_pandas(pbar)
        for i in range(100):
            pbar.update(1)
    print()

    # Testing delayed adapter for tqdm_pandas
    tqdm_pandas(tqdm, total=100, file=sys.stdout)
    for i in range(100):
        tqdm_

# Generated at 2022-06-14 13:08:45.643669
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        from nose import SkipTest
        raise SkipTest("pandas not found")
    from tqdm.auto import trange
    df = pandas.DataFrame({'a': [1, 2, 3, 4, 5]})
    # testing `tqdm` constructor
    df.groupby('a').progress_apply(lambda x: x).apply(lambda x: x)
    # testing `tqdm.pandas`
    with trange(10) as t:
        df.groupby('a').progress_apply(lambda x: x).apply(lambda x: x)

# Generated at 2022-06-14 13:08:52.506959
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    np.random.seed(0)
    df = pd.DataFrame({'a': np.random.rand(10), 'b': np.random.rand(10)})
    df.groupby('a').progress_apply(lambda x: x ** 2)
    tqdm_pandas(tqdm)

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:58.519971
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd

        df = pd.DataFrame([])
        df['a'] = list(range(0, 100))
        df['b'] = df.a.progress_apply(lambda x: x+1, tqdm_kwargs={'gui': True})
        if isinstance(df['b'][0], (float, int)):
            return True
        else:
            return False
    except:
        return False

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:06.410780
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from tqdm import tqdm
    with tqdm.pandas(total=100) as t:
        import pandas as pd
        df = pd.DataFrame({"row": [1] * 100})
        df["bar"] = df.row.progress_apply(  # automatically wraps within t
            lambda x: x + 2)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:28.766843
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm.auto import tqdm
    from tqdm._tqdm_pandas import tqdm_pandas  # NOQA
    from pandas import DataFrame, Series

    # Test 1: pd.DataFrame.apply()
    df = DataFrame({'x': [1, 2], 'y': [3, 4]})
    with tqdm(total=len(df), unit='rows') as pbar:
        df.apply(lambda x: pbar.update(), axis=1)

    # Test 2: pd.DataFrame.progress_apply()
    df = DataFrame({'x': [1, 2], 'y': [3, 4]})
    with tqdm(total=len(df), unit='rows') as pbar:
        df

# Generated at 2022-06-14 13:09:31.015849
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

# Generated at 2022-06-14 13:09:41.067017
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return  # only run test if pandas is installed

    try:
        from unittest import mock
    except ImportError:  # python <3.3
        import mock

    d = {'a': [10, 20, 30, 40, 50], 'b': [3.3, 4.4, 5.5, 6.6, 7.7]}
    df = pd.DataFrame(data=d)
    tclass = mock.Mock()


# Generated at 2022-06-14 13:09:45.077087
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    df.progress_apply(lambda x: x ** 2)
    with tqdm.tqdm() as _t:
        tqdm_pandas(_t, leave=False)
        df.progress_apply(lambda x: x ** 2)

# Generated at 2022-06-14 13:09:49.114957
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from .tests import pretest_bar

    # Create DataFrame
    df = pd.DataFrame(data=['train', 'test'])

    # Attempt to register tqdm to pandas
    tqdm_pandas(tqdm)

    # Verify tqdm is registered to pandas
    pretest_bar(df.groupby(df[0]).progress_apply(lambda x: x))


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:57.797320
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    tqdm_pandas(tqdm(total=len(df), desc='test'), file=sys.stdout)
    res = df.groupby(['a']).progress_apply(lambda x: x)
    assert res.equals(df)


# Script run when invoked directly
if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:04.204082
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest("pandas is not installed")

    def test_with_tqdm(tclass, **tqdm_kwargs):
        if isinstance(tclass, type) or (getattr(tclass, '__name__', '').startswith(
                'tqdm_')):  # delayed adapter case
            tclass.pandas(**tqdm_kwargs)
        else:
            type(tclass).pandas(deprecated_t=tclass)

    class DummyTqdm(tqdm):
        def __init__(self, *args, **kwargs):
            super(DummyTqdm, self).__init__(*args, **kwargs)


# Generated at 2022-06-14 13:10:09.005582
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame(np.random.randn(10000000, 1))
    with tqdm(total=len(df)) as progress_bar:
        # progress_apply() just returns the dataframe unchanged.
        df.progress_apply(lambda x: x)
        # In reality you would apply some function here.
        # The second argument is the number of columns.
        progress_bar.update(1)
    assert progress_bar.n == len(df)
    assert progress_bar.total == len(df)


# Generated at 2022-06-14 13:10:14.791578
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    df = pd.DataFrame({'A': np.random.randn(100)})
    df.groupby('A').progress_apply(lambda x: x)
    df.groupby('A').progress_apply(lambda x: x,
                                   show_count=True)

# Generated at 2022-06-14 13:10:23.337803
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    tqdm_pandas(tqdm.tqdm(pandas=True))
    tqdm_pandas(tqdm.tqdm())
    tqdm_pandas(tqdm.tqdm(pandas=True, total=1000))
    tqdm_pandas(tqdm.tqdm(), total=1000)
    tqdm_pandas(tqdm.tqdm(total=1000))
    tqdm_pandas(tqdm.tqdm(pandas=True), total=1000)
    tqdm_pandas(tqdm.tqdm(total=1000), pandas=True)

# Generated at 2022-06-14 13:10:49.408954
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from pandas import DataFrame, Series
    except ImportError:
        return
    from tqdm import trange

    # Test DataFrameGroupBy.progress_apply
    N = 100
    df = DataFrame({'col_' + str(i): Series(range(N)) for i in range(4)})
    for progress_apply in [True, False]:
        func = tqdm_pandas if progress_apply else tqdm
        with func(total=N) as pbar:
            _ = df.groupby(
                'col_0',
                sort=False).progress_apply(lambda x: len(x))  # noqa
            assert pbar.n == N

    # Test DataFrame.progress_apply
    df = DataFrame({'col': list(range(N))})

# Generated at 2022-06-14 13:10:59.739280
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    try:
        import pandas as pd
    except ImportError:
        return  # pandas req'd for testing

    df = pd.DataFrame({"a": np.random.randint(0, 100, size=1000)})

    from tqdm import tqdm
    # deprecated
    with tqdm(total=len(df)) as pbar:
        for _ in df.a.progress_apply(lambda x: x * 2):
            pbar.update()

    # new
    for _ in tqdm(df.a.progress_apply(lambda x: x * 2)):
        pass

# test_tqdm_pandas()

# Generated at 2022-06-14 13:11:07.744201
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas import Series
    from tqdm import tqdm
    from tqdm import tqdm_pandas

    df = DataFrame({'K': Series(range(100)),
                    'V': Series(range(100)),
                    'W': Series(range(100))})
    tqdm_pandas(tqdm())

    def test_func(df):
        return df

    # test_func(df.groupby('K', sort=False).progress_apply(test_func))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:11:17.286265
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_notebook as tqdm
    from tqdm import tqdm_pandas
    tqdm_pandas(tqdm)
    from pandas.core.groupby.generic import DataFrameGroupBy
    data = pd.DataFrame(
        {'A': [1, 1, 2, 2, 2, 3, 3],
         'B': [0, 1, 2, 0, 1, 0, 1]})
    def some_fn(x):
        return x*2
    print(data.groupby('A').progress_apply(some_fn))
    assert True, "If you're reading this, test_tqdm_pandas() failed"

# Generated at 2022-06-14 13:11:24.237352
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from numpy.random import randint
    from numpy import concatenate
    n = 2**20

    tqdm_pandas(tqdm)
    df = DataFrame({'col': concatenate((randint(0, 2, n), randint(0, 2, n)))})
    _ = df.groupby('col').progress_apply(lambda x: x)

    tqdm_pandas(tqdm(total=n, unit='rows'))
    df = DataFrame({'col': concatenate((randint(0, 2, n), randint(0, 2, n)))})
    _ = df.groupby('col').progress_apply(lambda x: x)



# Generated at 2022-06-14 13:11:34.741001
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    # Test if it works with tqdm and pd.DataFrame.progress_apply
    df = pd.DataFrame(np.arange(10, dtype=int))
    with tqdm_pandas(total=len(df)) as pbar:
        pbar.update(df.progress_apply(lambda x: x**2).sum())

    # Test if it works with tqdm.pandas
    df = pd.DataFrame(np.arange(10, dtype=int))
    with tqdm_pandas(total=len(df)) as pbar:
        pbar.update(df.progress_apply(lambda x: x**2).sum())

    # Test if it works with delayed tqdm adapter
    tqdm_

# Generated at 2022-06-14 13:11:43.839590
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    try:  # pandas >= 0.18
        from pandas import Series
    except ImportError:
        from pandas import Series
        Series.progress_apply = Series.apply
        DataFrameGroupBy.progress_apply = DataFrameGroupBy.apply

    df = pd.DataFrame({'a': range(50), 'b': range(50, 100)})
    tqdm_pandas(tqdm(total=len(df)))
    df.groupby('a').progress_apply(lambda x: (x, 'hoge'))
    tqdm_pandas(tqdm(total=len(df)), leave=False)


if __name__ == '__main__':
    test_tqdm_pandas()