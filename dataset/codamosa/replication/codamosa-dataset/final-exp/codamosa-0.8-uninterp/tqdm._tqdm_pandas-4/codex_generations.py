

# Generated at 2022-06-14 13:01:24.774626
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm_pandas
    val = tqdm_pandas("test")
    assert isinstance(val, TqdmType)

# Generated at 2022-06-14 13:01:31.272143
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas import read_csv

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmDeprecationWarning)
        import tqdm

    def test_iter():
        for _ in tqdm.pandas(range(100)):
            time.sleep(0.01)

    def test_df(df):
        df.groupby('A').progress_apply(lambda x: x + 1)

    def test_deprecated_df(df):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=TqdmDeprecationWarning)
            tqdm_pandas(tqdm, df=df)
        warnings.warn("function tqdm_pandas is deprecated", TqdmDeprecationWarning)

# Generated at 2022-06-14 13:01:39.645485
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import trange

    # Create a pandas dataframe
    df = DataFrame({'a': [1.0, 2.0, 3.0], 'b': [1, 2, 3]})

    def add_one(x):
        return x + 1

    # Calculate progress of apply()
    for _ in trange(5, desc='tqdm_pandas'):
        df.progress_apply(add_one)

if __name__ == '__main__':
    try:
        from tqdm.contrib.tests.pandas_tests import test_tqdm_pandas

        test_tqdm_pandas()
    except ImportError:
        pass

# Generated at 2022-06-14 13:01:49.902715
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm as tq
    from tqdm import pandas
    from pandas import DataFrame
    import numpy as np
    # Ensure that tqdm_pandas returns a namedtuple
    assert "tqdm_pandas" in str(type(tqdm_pandas(tq())))
    # Ensure that tqdm_pandas accepts class input
    assert "tqdm_pandas" in str(type(tqdm_pandas(tq)))
    # Ensure that tqdm_pandas wrapper works for pandas.DataFrame
    df = DataFrame({'x': np.random.randn(1000000)})

# Generated at 2022-06-14 13:01:59.639459
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for `tqdm_pandas`"""
    from tqdm import trange
    from pandas import DataFrame

    # first, test that it works with a valid `tqdm` instance
    for i in trange(10, desc='foo', ascii=True, dynamic_ncols=True):
        pass
    assert i == 9

    # next, test that it works with a valid `tqdm` class
    for i in trange(10, desc='foo', ascii=True, dynamic_ncols=True):
        pass
    assert i == 9

    # finally, test that it raises a proper warning when used with a stale `tqdm` class

# Generated at 2022-06-14 13:02:08.543102
# Unit test for function tqdm_pandas
def test_tqdm_pandas():

    from pandas import DataFrame
    from pandas import Series

    import tqdm.pandas

    N = 100

    s_ = Series(range(N))
    s_.progress_apply(lambda _: _)

    df_ = DataFrame(range(N))
    df_.progress_apply(lambda _: _, axis=1)
    df_.progress_apply(lambda _: _)

    df_ = DataFrame(range(N), columns=['a'])
    df_.progress_apply(lambda _: _['a'], axis=1)
    df_.progress_apply(lambda _: _['a'])


# Generated at 2022-06-14 13:02:18.380292
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from unittest import TestCase, main
    from pandas import DataFrame, Series
    from numpy.random import randint
    from numpy import zeros, ravel
    from tqdm import tqdm
    from tqdm.std import TqdmTypeError
    from tqdm.utils import _supports_unicode

    class _1D_DF(DataFrame):

        def __init__(self):
            super().__init__({'a': Series(zeros(1))})

        def apply(self, func, axis=0):
            return Series(func(ravel(self.values)))

        def progress_apply(self, func, axis=0):
            iterable = map(func, iter(self.values))
            return Series(iterable)


# Generated at 2022-06-14 13:02:30.471377
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    df = pd.DataFrame({'x': np.random.randint(0, 100, (1000,))})
    t = tqdm(total=len(df))
    t.close()

    t = tqdm(total=len(df))
    df.x.progress_apply(t.update, axis=1)  # fails without tqdm_pandas
    t.close()

    tqdm_pandas(tqdm)  # delayed adapter
    tqdm_pandas(tqdm())  # delayed adapter
    tqdm_pandas(tqdm, total=len(df))  # delayed adapter
    t.close()


# Generated at 2022-06-14 13:02:41.102556
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    try:
        # Test pd.DataFrame
        df = pd.DataFrame({'ints': [1, 2, 3, 4], 'floats': [0.5, 0.75, 0.875, 0.125]})
        n = len(df)

        # Test 1: not iterable
        tqdm_pandas(df.groupby('ints').mean())
        # Test 2: iterable with auto-set total
        list(tqdm_pandas(df.groupby('ints').mean(), leave=True))
        # Test 3: iterable with manual-set total
        list(tqdm_pandas(df.groupby('ints').mean(), total=n, leave=True))
    except:
        raise

# Generated at 2022-06-14 13:02:49.477611
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    import numpy as np
    from tqdm import tqdm
    from tqdm.contrib._test_tqdm_pandas import (
        _test_tqdm_pandas_dfg_progress_apply)

    # test with the old display
    tqdm_pandas(tqdm)
    x = pd.DataFrame(
        {'a': np.random.randn(100),
         'b': np.random.randn(100),
         'c': np.arange(100),
         'd': np.random.randn(100)})

    def foo(df):
        return pd.Series(df.sum() + np.random.random())

    old_display = p

# Generated at 2022-06-14 13:03:01.004413
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    t = tqdm_pandas
    t(tqdm)
    t(tqdm.tqdm)
    t(tqdm.tqdm_gui)
    t(tqdm.tqdm_notebook)
    t(tqdm.tqdm_pandas)
    t(tqdm.tqdm_pandas(tqdm.tqdm))
    t(tqdm.tqdm_pandas(tqdm.tqdm(tqdm.tqdm_notebook)))
    t(tqdm.tqdm_pandas(tqdm.tqdm_gui))

# Generated at 2022-06-14 13:03:12.093492
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    import tqdm

    df = pd.DataFrame(np.random.randn(100, 3))
    tq = tqdm.tqdm(total=len(df))

    tqdm_pandas(tq, desc='desc')
    df.groupby([0, 1, 2]).progress_apply(lambda x: x)
    # test for re-initialisation
    tqdm_pandas(tq, desc='desc')
    df.groupby([0, 1, 2]).progress_apply(lambda x: x)

    # test for delayed adapter
    tqdm_pandas(tqdm.tqdm, desc='desc')
    df.groupby([0, 1, 2]).progress_apply(lambda x: x)



# Generated at 2022-06-14 13:03:25.286425
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    import pandas.testing as pt
    from tqdm.notebook import tqdm_notebook

    # Test DataFrameGroupBy.progress_apply
    df = pd.DataFrame(np.random.rand(10000, 1000))
    ax = np.random.randint(0, 1000, size=len(df))
    dg = df.groupby(ax)
    result = dg.progress_apply(lambda x: x ** 2)
    pt.assert_frame_equal(result, dg.apply(lambda x: x ** 2), check_dtype=False)

    # Test Series.progress_apply
    s = df.sample(1000).squeeze()
    # Test `datasize`

# Generated at 2022-06-14 13:03:36.632346
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    from tqdm import tqdm_pandas

    tqdm_pandas(tqdm(), leave=False)

    pd.DataFrame([[0]]).groupby(0).progress_apply(lambda x: x)

    pd.DataFrame(np.random.randint(0, 10, size=(1000, 1000))).groupby(0).progress_apply(lambda x: x)

    # should not raise
    pd.DataFrame(np.random.randint(0, 10, size=(10000, 1000))).groupby(0).progress_apply(lambda x: x)
    pd.DataFrame(np.random.randint(0, 10, size=(100000, 1000))).groupby(0).progress_apply(lambda x: x)

# Generated at 2022-06-14 13:03:48.218589
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.autonotebook import tqdm
    tqdm_pandas(tqdm)
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5], "b": [1, 4, 9, 16, 25]})
    df_sum = df.groupby('a').progress_apply(lambda x: x.sum())
    assert df_sum.equals(df)
    del df_sum, df


if __name__ == '__main__':  # pragma: no cover
    try:
        test_tqdm_pandas()
    finally:
        del tqdm_pandas

# Generated at 2022-06-14 13:03:57.235677
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm
    import tqdm._utils as _utils

    df = pd.DataFrame(np.random.random((10, 5)))

    class DummyTqdmFile(object):
        """Dummy file-like that will write to tqdm"""
        file = None

        def __init__(self, file):
            self.file = file

        def write(self, x):
            # Avoid print() second call (useless \n)
            if len(x.rstrip()) > 0:
                tqdm.tqdm.write(x, file=self.file)

    # Monkey-patch pandas progress_apply to work with our tqdm instance
    _tqdm = tqdm.tqdm(total=len(df))



# Generated at 2022-06-14 13:04:04.793430
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # We use the `smoke` package to test `tqdm_pandas` in the simplest way
    # possible. The `smoke` package is available at PyPI via `pip install smoke`.
    # See https://pypi.python.org/pypi/smoke/1.0.0 and
    # https://github.com/bitranox/smoke.
    from smoke.utils import smoke

    smoke.test_test(test=tqdm_pandas, negative=False, verbose=False)

# Generated at 2022-06-14 13:04:12.317581
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas.util.testing import assert_frame_equal
    import numpy as np
    from tqdm import tqdm
    from tqdm._tqdm import TqdmTypeError

    try:
        from tqdm import trange  # ImportError: No module named 'tqdm'
    except ImportError:
        from tqdm import xrange as trange

    from tqdm.pandas import tqdm_pandas


# Generated at 2022-06-14 13:04:22.483440
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import Series, DataFrame

    # Series test
    s = Series(range(10))
    assert (sum(s.progress_apply(lambda x: x * x)) == 285) == True
    assert (sum(s.progress_apply(lambda x: x * x,
                                 tqdm=tqdm_pandas(tqdm))) == 285) == True

    # DataFrameGroupBy test
    s = Series([[1, 2], [2, 3]])
    assert (s.groupby(
        lambda x: x).progress_apply(lambda x: x[0] * x[0]) == 285) == True

# Generated at 2022-06-14 13:04:28.321705
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame({'x': [1, 2, 3, 4, 5]}, columns=['x'])

    tqdm_pandas(tqdm, file=sys.stdout)
    assert (df.groupby('x').progress_apply(lambda x: x) is None)
    tqdm_pandas(tqdm)
    assert (df.groupby('x').progress_apply(lambda x: x) is None)



# Generated at 2022-06-14 13:04:35.956181
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    df = pd.DataFrame({"a": np.random.randn(10000)})
    df.groupby("a").progress_apply(len)


# Monkeypatch pandas.core.groupby.DataFrameGroupBy.progress_apply

# Generated at 2022-06-14 13:04:44.468922
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import trange
    from tqdm import tqdm_pandas


# Generated at 2022-06-14 13:04:56.131807
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    # Assert tqdm_pandas accepts a tqdm instance
    tqdm_pandas(tqdm(total=2))

    # Assert tqdm_pandas accepts a tqdm class
    tqdm_pandas(tqdm)

    # Assert tqdm_pandas accepts a tqdm class with custom kwargs
    tqdm_pandas(tqdm, miniters=2)

    # Create some test data
    df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])

    # Assert progress_apply works
    def my_func(row):
        return row['a'] + row['b']


# Generated at 2022-06-14 13:05:04.931087
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    @tqdm_pandas(tclass=tqdm)
    def f(x):
        return x ** 2

    def g(x):
        return x ** 2

    try:
        tqdm.pandas()
    except BaseException:
        pass

    tqdm_pandas(tclass=tqdm)

    assert (f(range(10)).sum() == sum(g(range(10))))

# Remove tqdm_pandas from global namespace to avoid this function
# being used as a decorator.
del tqdm_pandas

if __name__ == '__main__':
    test_tqdm_pandas()
    print('Success')

# Generated at 2022-06-14 13:05:12.052683
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Just tests whether the decorator works.
    # Its effect is not critical to tqdm's functionality
    import pandas as pd

    N = 5
    df = pd.DataFrame({'x': list(range(N))})
    with tqdm(total=N) as pbar:
        df.progress_apply(lambda x: x**2, axis=1)
        pbar.update()

# Generated at 2022-06-14 13:05:23.689462
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from pandas import DataFrame
    except ImportError as e:
        raise unittest.SkipTest(e)

    df = DataFrame({'x': range(50), 'y': range(50, 100)})
    try:
        with tqdm.external_write_mode():
            df.progress_apply(lambda x: x**2)
    except AttributeError as e:
        raise unittest.SkipTest(e)
    with tqdm.external_write_mode():
        df.progress_apply(lambda x: x**2)
    with tqdm(total=2) as t:
        tqdm_pandas(t, total=1, leave=False)
        df.progress_apply(lambda x: x**2)
        t.update(1)

# Generated at 2022-06-14 13:05:29.881027
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    try:
        import sklearn
    except ImportError:
        print('sklearn not found (needed for test_tqdm_pandas)')
    else:
        from sklearn.datasets import load_digits

        digits = load_digits()
        df = pd.DataFrame(digits.data)
        df = df.groupby(0).progress_apply(lambda x: x ** 2)

# Generated at 2022-06-14 13:05:34.358017
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        tqdm_pandas(tqdm(range(3)))
        pd.DataFrame(range(3)).progress_apply(lambda x: x)
    except ImportError:
        pass

if __name__ == '__main__':
    test_tqdm_pandas()
    print('\n' + 'PASS')

# Generated at 2022-06-14 13:05:40.253199
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    tqdm.pandas(tclass=tqdm)
    df = DataFrame({'a': range(10)})
    assert (hasattr(df.groupby([df.a // 3]), 'progress_apply'))
    df.groupby([df.a // 3]).progress_apply(lambda x: x + 1)

# Generated at 2022-06-14 13:05:51.293387
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    class TqdmClass:
        """
        Dummy class for testing.
        """
        progress_apply_registered = False

        def __init__(self, tqdm_kwargs):
            self.fp = tqdm_kwargs['file']

        @classmethod
        def pandas(cls, **tqdm_kwargs):
            TqdmClass.progress_apply_registered = True

    assert not TqdmClass.progress_apply_registered
    tqdm_pandas(TqdmClass)
    assert TqdmClass.progress_apply_registered
    tqdm_pandas(TqdmClass(fp=sys.stderr, file=sys.stderr))
    assert TqdmClass.progress_apply_registered

# Generated at 2022-06-14 13:05:57.577316
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    def fun(a):
        return a
    df = pd.DataFrame({'a': [1]*100, 'b': [2]*100})
    tqdm_pandas(df.groupby('a').progress_apply(fun))

# Generated at 2022-06-14 13:06:02.468511
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    import tqdm

    df = pd.DataFrame({'a': list(np.arange(0, 100))})
    tqdm_pandas(tqdm.tqdm, leave=True)
    df.groupby('a').progress_apply(lambda x: x)
    tqdm_pandas(tqdm.tqdm, leave=True)
    tqdm_pandas(tqdm.tqdm(leave=True))

# Generated at 2022-06-14 13:06:09.424055
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    data = pd.DataFrame({'a': np.arange(0, 10)})

    def test_func(x):
        return x

    with tqdm_pandas(data.groupby(by='a'), leave=False) as t:
        t.get_lock().locks = []  # No lock required
        data.groupby(by='a').progress_apply(test_func)

# Generated at 2022-06-14 13:06:10.580336
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm())

# Generated at 2022-06-14 13:06:19.213888
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, trange
    from pandas import DataFrame, Series
    from numpy import arange

    # Test on Series
    for df in [Series(arange(10000)), DataFrame({'A': arange(10000)})]:
        # Test that tqdm_pandas(tqdm(...)) works
        tqdm_pandas(tqdm(df.progress_apply, total=len(df)))
        assert df.apply(lambda x: x).equals(df.progress_apply(lambda x: x))

        # Test that tqdm_pandas(tqdm) works
        tqdm_pandas(tqdm)
        assert df.apply(lambda x: x).equals(df.progress_apply(lambda x: x))

        # Test that tq

# Generated at 2022-06-14 13:06:30.635458
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, pandas  # noqa: F401
    assert hasattr(pandas, 'progress_map')
    assert hasattr(tqdm, 'pandas')
    tqdm_pandas(tqdm, ncols=0)
    try:  # tqdm < 4.23
        from tqdm._tqdm import _tqdm_pandas, _time, _tqdm  # noqa: F401
    except ImportError:
        from tqdm._tqdm import _tqdm_gui as _tqdm_pandas  # noqa: F401
    assert hasattr(_tqdm_pandas, 'progress_map')
    assert hasattr(_tqdm, 'pandas')

# Generated at 2022-06-14 13:06:34.909277
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Tests that `tqdm_pandas` doesn't crash (takes no arguments).
    """
    try:
        tqdm_pandas()
    except TypeError as e:
        assert 'tqdm_pandas() takes 1 positional argument but 2 were given' in str(e)
    else:
        assert False

# Generated at 2022-06-14 13:06:45.587018
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import random

    class CustomTqdm(tqdm):

        def __call__(self, *args, **kwargs):
            return CustomTqdm(total=random.randint(100, 1000), **kwargs)

    try:
        import pandas as pd
        df = pd.DataFrame([random.random() for _ in range(1000)])
        tqdm_pandas(CustomTqdm, desc='TEST', leave=False, file=open(os.devnull, 'wb'))
        # should not raise
        df.groupby(df.columns[0] // 0.1).progress_apply(lambda x: x**2)
    except ImportError:
        tqdm.write('Pandas not found, skipping test_tqdm_pandas()')

# Generated at 2022-06-14 13:06:56.888821
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    df = DataFrame({"A": range(100000)})
    ret = df.groupby("A").progress_apply(len)
    assert ret.sum() == df.shape[0]
    ret = df.groupby("A").progress_apply(len)
    assert ret.sum() == df.shape[0]
    with tqdm(ascii=True) as t:
        ret = df.groupby("A").progress_apply(len, t=t)
        assert ret.sum() == df.shape[0]
        ret = df.groupby("A").progress_apply(len, t=t)
        assert ret.sum() == df.shape[0]



# Generated at 2022-06-14 13:07:06.768383
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from tqdm import tqdm
    from pandas import DataFrame

    df = DataFrame({'A': ['a', 'b', 'c'],
                    'B': ['d', 'e', 'f']})
    df = df.groupby('A')
    tqdm_pandas(tqdm())

    tqdm_pandas(tqdm(**{'mininterval': 0.001}))
    tqdm_pandas(tqdm(**{'mininterval': 1}))
    tqdm_pandas(tqdm(**{'mininterval': 0}))

    # Dummy groupby, to check for errors
    df.progress_apply(lambda x: x)

# Generated at 2022-06-14 13:07:18.875118
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    # test pandas >= 0.23
    if pd.__version__ >= '0.23':
        pdgb = pd.DataFrame([[1,2]]).groupby(1)
        tqdm_pandas(tqdm.tqdm)
        def func(x):
            return 1
        pdgb.progress_apply(func)
        tqdm_pandas(tqdm.tqdm, total=1)
        pdgb.progress_apply(func)

        # test pandas < 0.23
    else:
        try:
            from pandas.core.groupby import SeriesGroupBy, DataFrameGroupBy
        except ImportError:
            from pandas.core.groupby import SeriesGroupBy, GroupBy

# Generated at 2022-06-14 13:07:29.168024
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return
    try:
        import tqdm
    except ImportError:
        return
    from tqdm import TqdmExperimentalWarning

    if os.name == 'nt':
        # In Windows, there is a bug with the progress bar that makes it fail
        # the test https://github.com/pandas-dev/pandas/issues/26284
        return

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)
        df = pandas.DataFrame([{'a': 'aa', 'b': 'bb'},
                               {'a': 'aaa', 'b': 'bbb'},
                               {'a': 'aaaa', 'b': 'bbbb'}])
        tq

# Generated at 2022-06-14 13:07:40.149673
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import trange
    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy
    from numpy import random

    def f(x):
        return 1 + random.random()

    # Test
    tqdm_pandas(trange)
    df = DataFrame(dict(a=[1, 2, 3], b=[1, 2, 3]))
    DataFrameGroupBy.progress_apply = tqdm_pandas.progress_apply
    df.groupby('a').progress_apply(f)


# Adaptation of class PandasMixin

# Generated at 2022-06-14 13:07:52.008386
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    from tqdm import tqdm, tqdm_notebook
    from tqdm.autonotebook import tqdm as tqdm_tqdm

    try:
        from pandas import Series
    except ImportError:
        Series = None

    tqdm_pandas(tqdm)

    # test with series
    if Series is not None:
        ser = Series(np.random.randn(100))
        assert len(list(ser.groupby(0).progress_apply(lambda x: x))) == 100
        assert len(list(ser.groupby(lambda x: x % 5).progress_apply(lambda x: x))) == 5
        ser.groupby(0).progress_apply(lambda x: x)

    # test with dataframe

# Generated at 2022-06-14 13:07:59.430277
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    tqdm_pandas(tqdm, unit="row")
    sum_row = df.progress_apply(lambda x: x.sum(), axis=1)
    sum_row.head()


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:06.092549
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import numpy
    from pandas import Series, DataFrame

    t0 = Series(numpy.random.randn(100), index=numpy.arange(100))
    with tqdm(**tqdm_kwargs('tqdm_pandas.test_tqdm_pandas')) as t:
        df1 = t0.progress_apply(lambda x: x)
        assert df1.equals(t0)
        t.update()

        df1 = t0.progress_apply(lambda x: x**2)
        df2 = t0.apply(lambda x: x**2)
        assert df1.equals(df2)
        t.update()

        df1 = t0.progress_apply(lambda x: 2*x)

# Generated at 2022-06-14 13:08:16.402728
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import os
    try:
        # python2.6 does not have unittest.skip
        import unittest2 as unittest
    except ImportError:
        import unittest
    tqdm_pandas = globals()['tqdm_pandas']

    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest("pandas is required for tqdm's pandas integration test")

    df = pd.DataFrame({'a': range(10000)})

    class tqdm(object):
        def __init__(self, total):
            self.total = total
            self.n = 0
            self.pandas_bar = None


# Generated at 2022-06-14 13:08:27.506783
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from numpy.random import randint, rand

    df = pd.DataFrame(np.random.randn(1000, 50))

    with tqdm_pandas(ascii=True) as t:
        df.progress_apply(lambda x: x**2)
        assert 'Pandas' in t.desc
        assert 'numpy' in repr(t)

    with tqdm(
            ascii=True,
            total=1000,
            desc='Mixed',
            leave=True,
            smoothing=1,
            bar_format='{l_bar}{bar}|',
    ) as t:
        for i in range(100):
            t.update(10)

# Generated at 2022-06-14 13:08:34.306270
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    df = DataFrame({'a': range(1000), 'b': range(1000)})
    tqdm_pandas(tqdm)
    df.groupby('a').progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:38.940000
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import argparse
    import pandas as pd
    from tqdm import tqdm
    from pandas.core.groupby import DataFrameGroupBy
    from .tqdm_pandas import tqdm_pandas

    parser = argparse.ArgumentParser(
        description='Benchmark pandas groupby with tqdm')
    parser.add_argument('--n', default=1000, type=int,
                        help='Number of rows of the dataset.')
    parser.add_argument('--c', default=2, type=int,
                        help='Number of columns of the dataset.')
    parser.add_argument('--grps', default=10, type=int,
                        help='Number of groups')

# Generated at 2022-06-14 13:08:51.392961
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
    gb = df.groupby('A')
    tqdm_pandas(gb.B.progress_apply, lambda x: x * 2)

# Generated at 2022-06-14 13:09:00.065852
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas

    See <https://github.com/tqdm/tqdm/tree/master/tests>
    """
    from pandas import DataFrame, Series
    from .tqdm import tqdm
    from .tests import pretest_posttest  # NOQA

    def _test_tqdm_pandas():
        # Test data (see: https://github.com/tqdm/tqdm/issues/385)
        df = DataFrame({'col1': Series([1, 2, 3]),
                        'col2': Series([4, 5, 6])})

        # Basic unit test
        t = tqdm(df.groupby('col1'))
        assert len(t.children) == 1

# Generated at 2022-06-14 13:09:01.638280
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(dict(), total=100)
    assert True

# Generated at 2022-06-14 13:09:12.616222
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    with tqdm_pandas(tqdm(total=len(range(10)), unit_scale=True)) as pbar:
        DataFrame({'a': range(10)}).progress_apply(lambda x: pbar.update(), axis=1)
    with tqdm_pandas(tqdm(total=len(range(10)), unit_scale=True)) as pbar:
        Series(range(10)).progress_apply(lambda x: pbar.update())
    # delayed adapter case
    with tqdm(total=len(range(10)), unit_scale=True) as dep_t:
        tqdm_pandas(dep_t)

# Generated at 2022-06-14 13:09:17.783104
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    global N
    N = 100
    test_df = pd.DataFrame(np.random.rand(N, 5))

    assert hasattr(test_df.groupby(test_df[0] > 0.5).sum(), '_tqdm')

# Generated at 2022-06-14 13:09:23.441707
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with tqdm_pandas(total=100) as df_progress:
        df_progress.update()
        df_progress.update()
        df_progress.update(0)  # shouldn't have any effect

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 13:09:35.621269
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("This test needs the module `pandas`.")
    try:
        import numpy as np
    except ImportError:
        raise ImportError("This test needs the module `numpy`.")
    try:
        import tqdm
    except ImportError:
        raise ImportError("This test needs the module `tqdm`.")

    df = pd.DataFrame({0: np.random.rand(1000),
                       1: np.random.rand(1000)})
    df = pd.concat((df, df), axis=1)
    assert df.groupby(lambda x: x % 2, axis=1).progress_apply(
        lambda x: x * 2).equals(df * 2)

# Generated at 2022-06-14 13:09:44.154665
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from ._tqdm import TqdmTypeError
    from tqdm._utils import _supports_unicode
    if _supports_unicode:
        from tqdm._tqdm_gui import tqdm_gui
        tqdm_gui.pandas(mininterval=1e-10)

    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm)
        assert len(w) == 0

    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm(unit_scale=0.1))
        assert len(w) == 0


# Generated at 2022-06-14 13:09:53.785527
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test for function tqdm_pandas"""
    def test_tqdm(tqdm):
        tqdm_pandas(tqdm)
    try:
        from unittest.mock import patch
        from unittest.mock import Mock
        from unittest.mock import MagicMock
    except ImportError:
        from mock import patch
        from mock import Mock
        from mock import MagicMock

# Generated at 2022-06-14 13:10:05.128004
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm import trange
    from tqdm import tnrange

    tqdm_pandas(tqdm)
    tqdm_pandas(trange)
    tqdm_pandas(tnrange)


# Generated at 2022-06-14 13:10:31.605388
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    aliased_func = None
    def progress_apply():
        return None

# Generated at 2022-06-14 13:10:39.734947
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    @tqdm_pandas
    def test():
        """
        A test function that implements the `pandas.core.groupby.DataFrameGroupBy.progress_apply` interface.
        """
        return

    import pandas as pd
    df = pd.DataFrame({'x': [1, 2, 3],
                       'y': [10, 20, 30]},
                      index=[1, 2, 3])
    groups = df.groupby('x')
    groups.progress_apply(test)

    @tqdm_pandas(tqdm=lambda: tqdm())
    def test2():
        """
        A test function that implements the `pandas.core.groupby.DataFrameGroupBy.progress_apply` interface.
        """

# Generated at 2022-06-14 13:10:47.471811
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
    except ImportError:
        print("Could not import pandas and/or numpy --> skipping test")
        return

    pandas_df = pd.DataFrame({'A': np.random.randn(1000)})
    pandas_df.groupby('A').pandas(
        tqdm_kwargs=dict(total=len(pandas_df['A'])))

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:58.338694
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    # Dummy DataFrame
    N = 100000
    df = pd.DataFrame(np.random.randint(0, N, (N, 6)))

    # Workaround to capture stderr and restore afterwards
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()

    # Testing tqdm tclass and deprecated class
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm(total=N))
    tqdm_pandas(tqdm(total=N), leave=False)
    tqdm_pandas(tqdm(total=N), leave=True)



# Generated at 2022-06-14 13:11:07.666967
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        # DataFrame
        x = pd.DataFrame({'x': [1, 2, 3], 'y': [1., 2., 3.]})
        res = x.groupby('x').progress_apply(lambda g: g['y'].sum())
        assert (res == 4.).all()
        # Series
        x = pd.Series([1, 2, 3], name='x')
        res = x.groupby(x).progress_apply(lambda g: g.sum())
        assert (res == 4.).all()

        del pd  # ensure import pandas doesn't occur in coverage report
    except ImportError:
        pass

if __name__ == '__main__':
    from tqdm import trange
    from time import sleep


# Generated at 2022-06-14 13:11:17.885129
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit testing for the function `tqdm_pandas`.

    Raises
    ------
    AssertionError
        If any of the tests fails.
    """
    class MockTqdm():
        __name__ = 'mock_tqdm'
        def write(self, x):
            pass

    def _test_tqdm_pandas(tclass):
        # function syntax
        tqdm_pandas(tclass)

        # class syntax
        tqdm_pandas(tclass, **{'mininterval': 0.1})
        return True

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        assert _test_tqdm_pandas(MockTqdm())

# Generated at 2022-06-14 13:11:24.571191
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest("Skipping test_tqdm_pandas because pandas is not installed")
    from tqdm import tqdm
    from tqdm import tqdm_gui
    # Test pandas support for apply
    pd_test = pd.DataFrame({'x': [1, 2, 3, 4, 5]})
    tqdm.pandas(desc="a description")
    pd_test.progress_apply(lambda x: x + 1)
    tqdm_gui.pandas(desc="a description")
    pd_test.progress_apply(lambda x: x + 1)
    # Remove deprecated function support
    import warnings
    with warnings.catch_warnings():
        warnings.filter