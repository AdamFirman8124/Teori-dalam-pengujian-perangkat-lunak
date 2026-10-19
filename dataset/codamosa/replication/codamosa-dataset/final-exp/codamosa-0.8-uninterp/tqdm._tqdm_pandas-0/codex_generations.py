

# Generated at 2022-06-14 13:01:40.075622
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    import tqdm
    df = pd.DataFrame(np.random.random((10, 3)))
    print(df.apply(np.sum))
    with tqdm.pandas(total=len(df)) as pbar:
        print(df.progress_apply(lambda x: np.sum(x)))

# Generated at 2022-06-14 13:01:49.942096
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm.pandas import tqdm_pandas

    print("Testing with tqdm instance (tqdm())...")
    tqdm_pandas(tqdm(total=42, desc="test"))

    print("Testing with class (tqdm)...")
    tqdm_pandas(tqdm, total=42, desc="test")

    print("Testing with optional tqdm_kwargs...")
    tqdm_pandas(tqdm, total=42, desc="test", leave=True)

    print("Testing with tqdm_pandas defaults...")
    tqdm_pandas(tqdm)

    print("Testing with deprecated tqdm instance (tqdm_notebook())...")

# Generated at 2022-06-14 13:01:58.296223
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        warnings.warn("Pandas not installed, skipping tqdm_pandas tests")
        return
    from tqdm import tqdm

    def slow_apply(x):
        from time import sleep
        sleep(0.001)
        return x

    df = pd.DataFrame(range(0, 10000))
    with tqdm(total=df.shape[0], desc="Dummy training") as pbar:
        df.progress_apply(slow_apply)
        pbar.update()


test_tqdm_pandas.test_tqdm_pandas = True

# Generated at 2022-06-14 13:02:07.100305
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    class dummy_tqdm(object):
        def pandas(self, **kwargs):
            return kwargs
    assert tqdm_pandas(dummy_tqdm, a=1) == {'a': 1}
    assert tqdm_pandas(dummy_tqdm(), a=1) == {'a': 1}
    assert tqdm_pandas(tqdm, a=1) == {'a': 1}
    assert tqdm_pandas(tqdm(), a=1) == {'a': 1}

# Generated at 2022-06-14 13:02:12.322361
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    try:
        from tqdm.contrib import DummyTqdmFile
        with tqdm(leave=True, file=DummyTqdmFile()) as t:
            tqdm_pandas(t)
    except ImportError:
        pass



# Generated at 2022-06-14 13:02:20.965892
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    with tqdm(total=10) as t:
        df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [4, 3, 2, 1]})
        # test set_postfix
        df.a.progress_apply(lambda _: t.update(1), axis='index')
        t.set_postfix(sum_a=df.a.sum())
        # test add
        df.a.progress_apply(lambda _: t.update(.5), axis='index')
        # test disable
        df.a.progress_apply(lambda _: t.update(2), axis='index', disable=True)
        # test dynamic nesting
        df.a.progress_apply

# Generated at 2022-06-14 13:02:32.724794
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""

    import pandas as pd
    import numpy as np
    import tqdm

    df = pd.DataFrame({'x': np.linspace(0, 1, 100000)})

    # The wrapper method tqdm_pandas() is deprecated, so should the
    # functions that it wraps
    with pytest.warns(TqdmDeprecationWarning):
        tqdm_pandas(df.progress_apply)
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm.tqdm)
        tqdm_pandas(tqdm.tqdm_notebook)

    # Check that using the pandas method works correctly

# Generated at 2022-06-14 13:02:43.040885
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import functools
    import create_pandas_obj
    import numpy as np
    import pandas as pd
    import pandas.core.groupby
    import tqdm

    tqdm_pandas(tqdm)  # initialize tqdm_pandas

    data = create_pandas_obj.create_pandas_dataframe(0, 99, 5)
    test_data = pd.DataFrame({
        'data ' + str(i): np.random.randint(-100, 100, size=100)
        for i, _ in enumerate(data.columns)
    })

# Generated at 2022-06-14 13:02:51.401203
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    try:
        import numpy
    except ImportError:
        numpy = None
    try:
        import sklearn
    except ImportError:
        sklearn = None

    a = pandas.Series(numpy.random.randint(0, 100, size=1000000))
    with tqdm_pandas(total=len(a)) as pbar:
        a.progress_apply(lambda x: x**2)
    assert pbar.smoothing > 0
    assert pbar.n == len(a)
    assert pbar.last_print_n == len(a)
    assert pbar.last_print_t is not None
    assert pbar.smoothed_measure >= 0


# Generated at 2022-06-14 13:03:02.683984
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    def f(x):
        return x.max()

    try:  # Pandas 0.18+
        df = pd.DataFrame(np.random.randint(0, int(1e8), size=(100, 10)))
        tqdm.pandas(desc="Iterating over pandas dataframe")
        assert list(df.progress_apply(f)) == list(df.apply(f)), "Pandas dataframe test failed"
        del df
    except AttributeError:  # Older pandas
        def agg(x):
            return pd.Series(dict(max_=x.max()))

# Generated at 2022-06-14 13:03:12.771895
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm.contrib.tests import TestCase
    from tqdm.contrib.tests.pymisc import opt_bar, zeros

    class Test_tqdm_pandas(TestCase):

        def test_basic(self):
            """Test tqdm_pandas()"""
            tqdm_pandas(tqdm())

        def test_basic_tqdm(self):
            """Test tqdm_pandas(tqdm(...))"""
            t = tqdm_pandas(tqdm(
                total=10, ascii=True, smoothing=0, dynamic_ncols=True,
                leave=False, miniters=1))

# Generated at 2022-06-14 13:03:26.073166
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy
    from tqdm import tqdm

    for i in range(2):
        tqdm_pandas(tqdm_pandas)

    df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = DataFrame({'a': [3, 2, 1], 'b': [6, 5, 4], 'c': [9, 8, 7]})
    dfgb = df.groupby(['a', 'b'])
    tqdm_pandas(tqdm)
    assert DataFrameGroupBy.progress_apply == tqdm_pandas_progress_apply


# Generated at 2022-06-14 13:03:31.372289
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import random

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    pbar = tqdm_pandas(tqdm())
    df.groupby(0).progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:03:40.266816
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    try:
        import pandas as pd
    except ImportError:  # pragma: no cover
        return
    tqdm = tqdm_pandas(tqdm)
    s = pd.Series(np.random.randint(0, 1000, 10000))
    assert len(list(tqdm(s))) == len(s)
    grouped = s.groupby(s)
    assert len(list(tqdm(grouped))) == len(grouped)
    grouped = s.groupby(s, group_keys=False)
    assert len(list(tqdm(grouped))) == len(grouped)

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:51.573909
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy
    from tqdm import tqdm

    class ProgressBar():
        def __init__(self):
            self.t = None

        def __call__(self, x):
            if self.t is None:
                tqdm_pandas(tclass=tqdm)
                self.t = tqdm(x.items(), leave=False)
            return list(self.t)

    def test_dfgb_progress_apply():
        df = DataFrame({'x': list('abcdefghijkl')})
        assert df.groupby('x').progress_apply(ProgressBar()) == df.groupby('x').apply(ProgressBar())

    test_dfgb_progress_apply()

# Generated at 2022-06-14 13:03:55.504025
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.ranf(size=(100000, 2)), columns=['a', 'b'])


# Generated at 2022-06-14 13:04:06.140938
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    df = pd.DataFrame([range(10), range(10), range(10), range(10), range(10), range(10), range(10),
                       range(10), range(10), range(10)]).transpose()

# Generated at 2022-06-14 13:04:16.617413
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with tqdm(total=100) as t:
        tqdm_pandas(t)
        assert hasattr(t, '_pandas_deprecated')

    with tqdm(total=100) as t:
        tqdm_pandas(t, file=sys.stderr)
        assert hasattr(t, '_pandas_deprecated')

    with tqdm(total=100) as t:
        tqdm_pandas(t, bar_format='{bar}')
        assert hasattr(t, '_pandas_deprecated')

    with tqdm(total=100) as t:
        tqdm_pandas(t, file=sys.stderr, bar_format='{bar}')

# Generated at 2022-06-14 13:04:22.557633
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    with tqdm.tests.mock.patch('tqdm.tqdm_pandas') as pp:
        tqdm.pandas()
    assert pp.called
    with tqdm.tests.mock.patch('tqdm.tqdm_pandas') as pp:
        tqdm.tqdm_pandas(tqdm.tqdm())
    assert pp.called

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:26.420443
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas as pd

    df = pd.DataFrame(
        {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
    )

    df.groupby(['col1']).progress_apply(lambda x: x)

# Generated at 2022-06-14 13:04:34.905331
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    tqdm_w = tqdm_pandas(ncols=60)
    df = pd.DataFrame({'a': [1, 2, 4, 8, 16, 32, 64], 'b': [2, 3, 5, 7, 11, 13, 17]})
    df.groupby('a').progress_apply(lambda x: len(x))

# Generated at 2022-06-14 13:04:40.866997
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from numpy import random

    df = DataFrame(random.randn(1000, 4), columns=list('ABCD'))
    tqdm_pandas(tqdm)
    assert list(df.groupby('A').progress_apply(len)) == [35, 95, 63, 67, 140]


if __name__ is "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:47.234241
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    def unit_tqdm(t, **tqdm_kwargs):
        # type: (Optional[Type[tqdm]], Any) -> tqdm
        import warnings
        from tqdm import tqdm

        if t is None:  # auto-detect tqdm class
            for tcls in [tqdm, tqdm.tqdm_notebook]:
                try:
                    return tcls(**tqdm_kwargs)
                except Exception as e:
                    warnings.warn(str(e), RuntimeWarning)

        elif isinstance(t, type) and issubclass(t, tqdm):  # create instance
            return t(**tqdm_kwargs)

        elif isinstance(t, tqdm):  # reuse existing instance t
            return t


# Generated at 2022-06-14 13:04:59.742815
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd, numpy as np
    from tqdm import tqdm

    if hasattr(pd.core.groupby.DataFrameGroupBy, 'progress_apply'):
        # No need to actually import pandas for testing
        tqdm_pandas(tqdm)

        # Test 1
        test1 = pd.DataFrame({'group': ['a', 'b', 'c', 'a', 'b', 'c'],
                              'values': [1, 2, 3, 4, 5, 6]})
        test1_expected = pd.DataFrame({'group': ['a', 'a', 'b', 'b', 'c', 'c'],
                                       'values': [1, 4, 2, 5, 3, 6]})

# Generated at 2022-06-14 13:05:10.117137
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_gui, trange
    for tclass in (tqdm, tqdm_gui, trange):
        tqdm_pandas(tclass)
        tqdm_pandas(tclass(
            file=sys.stdout, leave=False, ascii=True))
        tqdm_pandas(tclass(file=sys.stderr))  # leave default
        tqdm_pandas(tclass(file=sys.stderr, ascii=False), leave=True)
        tqdm_pandas(tclass, file=sys.stderr, ascii=False)  # leave default

# Generated at 2022-06-14 13:05:19.045487
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame

    tqdm_pandas(tqdm)

    df = DataFrame({'str': [str(x) for x in range(1000)],
                    'int': [int(x) for x in range(1000)],
                    'float': [float(x/100) for x in range(1000)]})

    def f(df):  # f(df) == df
        return df

    it = df.groupby('int').progress_apply(f)
    for _ in it:
        pass
    assert isinstance(it, tqdm)

# Generated at 2022-06-14 13:05:25.412211
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas
    import pandas as pd
    tqdm_pandas(tqdm())
    df = pd.DataFrame(list(range(10)))
    df.groupby(df[0]).progress_apply(lambda x: x) == \
        df.groupby(df[0]).apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:34.514577
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_notebook

    # I believe this is the simplest way to create a dataframe with a few ints
    # in it.
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], columns=["a", "b", "c"])
    
    # Apply the sum function across all columns in the dataframe
    df1 = df.groupby(level=0).progress_apply(sum)
    assert df1.iloc[0][0] == 6
    assert df1.iloc[1][0] == 15
    assert df1.iloc[2][0] == 24
    assert df1.iloc[3][0] == 33

    # Apply the sum

# Generated at 2022-06-14 13:05:44.845382
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5]})
    df.groupby('a').progress_apply(lambda x: x)

    dfg = df.groupby('a')
    tqdm.tqdm_pandas(tqdm.tqdm(total=len(dfg), postfix={'group': 'bar'}),
                     desc='Group')
    dfg.progress_apply(lambda x: x)
    assert True


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:54.246038
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:06:02.952909
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:06:07.171803
# Unit test for function tqdm_pandas
def test_tqdm_pandas():  # pragma: no cover
    from tqdm.auto import tqdm

    # NOTE: don't use pandas here as it may deactivate the progressbar in some cases
    tqdm_pandas(tqdm)
    print("tqdm_pandas passed")

# Generated at 2022-06-14 13:06:16.848781
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    from pandas import DataFrame
    from tqdm import tqdm

    df = DataFrame({'a': [1, 2, 3, 4],
                    'b': [5, 6, 7, 8],
                    'c': [9, 10, 11, 12]})

    # Check DataFrame
    with tqdm(total=len(df.index)) as pbar:
        pbar.set_description('Testing tqdm_pandas()')
        df.progress_apply(lambda row: pbar.update())

    # Check Series
    with tqdm(total=len(df['a'])) as pbar:
        pbar.set_description('Testing tqdm_pandas()')
        df['a'].progress_apply(lambda x: pbar.update())

    # Check GroupBy

# Generated at 2022-06-14 13:06:25.553211
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd

    df = pd.DataFrame({'BoolCol': [True, False, True]})
    df['BoolCol'] = df['BoolCol'].progress_apply(lambda x: x)

    df = pd.DataFrame({'BoolCol': [True, False, True]})
    df['BoolCol'] = tqdm_pandas(df['BoolCol'].progress_apply(lambda x: x))


if __name__ == '__main__':
    from tqdm import main
    main()

# Generated at 2022-06-14 13:06:33.908968
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    df = pd.DataFrame(dict(a=range(100), b=range(100)))
    tqdm_pandas(tqdm.tqdm)
    df.groupby('a').progress_apply(lambda x: None)

    tqdm_pandas(tqdm.tqdm(total=10))
    df.groupby('a').progress_apply(lambda x: None)

    tqdm_pandas(tqdm.tqdm.pandas(total=10))
    df.groupby('a').progress_apply(lambda x: None)

# Generated at 2022-06-14 13:06:44.831098
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas import Series
    from tqdm import tqdm, tqdm_pandas

    # Test `tqdm_pandas(tqdm)`
    tqdm_pandas(tqdm)
    assert Series(range(3)).progress_apply(lambda _: ()) is None

    # Test `tqdm_pandas(tqdm(...))`
    tqdm_pandas(tqdm(total=3))
    assert Series(range(3)).progress_apply(lambda _: ()) is None

    # Test `tqdm.pandas()`

# Generated at 2022-06-14 13:06:46.840744
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    test_pbar = tqdm(range(5))
    type(test_pbar).pandas(test_pbar)



# Generated at 2022-06-14 13:06:58.018375
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas."""
    import unittest
    from .main import tqdm
    from .tests import dummy_tqdm

    class TqdmPdTests(unittest.TestCase):
        """Test class for tqdm_pandas's deprecation warnings."""
        def test_tqdm_pandas(self):
            """Unit test for function tqdm_pandas."""
            try:
                tqdm_pandas(tqdm)
                tqdm_pandas(dummy_tqdm)
            except TqdmDeprecationWarning:
                pass

# Generated at 2022-06-14 13:07:01.606205
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from .tqdm import tqdm

    with tqdm(total=100) as pbar:
        pd.DataFrame({'a': range(100)}).progress_apply(lambda x: x)
        pbar.update()



# Generated at 2022-06-14 13:07:10.183453
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    def f(df):
        for _ in range(1000000):
            pass
        return df

    df = pd.DataFrame({'a': [1., 2., 3.],
                       'b': ['string', 'tuple', 'value'],
                       'c': [True, False, True]})
    df.progress_apply(f, axis=1)
    with tqdm(total=len(df)) as pbar:
        def add(df):
            pbar.update()
            return df
        df.progress_apply(add, axis=1)
        df.progress_apply(add, axis=0)

    tqdm_pandas(tqdm, desc='Using pandas')
    df.progress_apply(f, axis=1)
    del tclass

# Generated at 2022-06-14 13:07:23.239424
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from random import random
    from sys import version_info

    try:
        from tqdm.auto import trange, tqdm
    except ImportError:
        from tqdm import trange, tqdm

    # unit tests for delayed adapter
    if version_info.major == 2:  # python 2
        assert tqdm_pandas(
            tqdm, pandas=True, desc='test pandas').__class__.__name__ == 'tqdm'
    else:
        assert tqdm_pandas(
            tqdm, pandas=True, desc='test pandas').__class__.__name__ == 'tqdm_notebook'

# Generated at 2022-06-14 13:07:32.431919
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    def tqdm_pandas_decorator(df, func):
        from tqdm import tqdm
        from tqdm import tqdm_pandas
        tqdm_pandas(tqdm)
        return df.progress_apply(func)

    def pandas_apply_decorator(df):
        return df.apply(lambda x: x ** 2)

    df = pd.DataFrame([[1, 2], [3, 4]])
    assert (tqdm_pandas_decorator(df, pandas_apply_decorator) ==
            pandas_apply_decorator(df)).all().all()

    def pandas_progress_apply_decorator(df, func):
        return df.progress_apply(func)



# Generated at 2022-06-14 13:07:44.191825
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.random(size=(100, 3)))
    tqdm.pandas(tqdm.tqdm())
    df.groupby(0).progress_apply(lambda x: x)

    try:
        tqdm_pandas(tqdm.tqdm())
        raise Exception("")
    except:  # noqa
        pass
    else:
        raise Exception("")

    # miscellaneous tests
    df = pd.DataFrame({'A': [0, 1, 2], 'B': ['a', 'b', 'c']})
    df.groupby('A').progress_apply(lambda x: x['B'].sum())


# Generated at 2022-06-14 13:07:50.138657
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        import numpy
        tqdm_pandas(numpy.random.rand(100, 100), total=100)
        tqdm_pandas(pandas.DataFrame(numpy.random.rand(100, 100)), total=100)
    except Exception:
        pass



# Generated at 2022-06-14 13:08:01.030307
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    N = 10000
    df = pd.DataFrame(dict(a=np.random.random(N),
                           b=np.random.random(N),
                           c=np.random.random(N),
                           d=np.random.random(N),
                           e=np.random.random(N)))

    def f(g):
        return (g - g.min()) * 1.5

    with tqdm(total=N, ascii=True) as pbar:
        res = df.groupby('a').progress_apply(f, pbar=pbar)

    assert(np.array_equal(res.groupby('a').apply(f).values, res.values))


# Unit

# Generated at 2022-06-14 13:08:13.592369
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame as DF
    from tqdm import tqdm

    df = DF({'x': ('a', 'b', 'c', 'd')})
    res = df['x'].progress_apply(lambda x: x)
    assert set(res) == {'a', 'b', 'c', 'd'}

    tqdm_pandas(tqdm, leave=False)  # leave=False: can run multiple times
    df = DF({'x': ('a', 'b', 'c', 'd')})
    res = df['x'].progress_apply(lambda x: x)
    assert set(res) == {'a', 'b', 'c', 'd'}

    tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:08:24.624960
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Simple tests for `tqdm_pandas`.
    """
    import pandas as pd
    import random
    import tqdm
    import types

    tqdm.tqdm_pandas(tqdm.tqdm())
    assert hasattr(pd.core.groupby.DataFrameGroupBy, 'progress_apply')

    def foo(x):
        return x + 1

    df = pd.DataFrame({'a': list(range(10000))})
    for inplace in [False, True]:
        for progress in [True, False]:
            if progress:
                tqdm.tqdm_pandas(tqdm.tqdm())  # enable pandas progress bar
            else:
                tqdm.tqdm_pandas(None)  # disable pandas

# Generated at 2022-06-14 13:08:33.659285
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        from tqdm import tqdm
        from tqdm import TqdmDeprecationWarning
        tqdm(pandas=True).pandas()
        # tqdm_pandas(tqdm, pandas=True)
        tqdm(pandas=False).pandas()
        tqdm_pandas(tqdm, pandas=False)
    except Exception as e:
        if 'pandas' in str(e):
            pass
        else:
            raise
    except TqdmDeprecationWarning as e:
        pass

# Generated at 2022-06-14 13:08:34.735510
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    assert (pd.DataFrame([0])
            .groupby(0).progress_apply(lambda x: x))  # this should be lazy

# Generated at 2022-06-14 13:08:43.790849
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import tqdm
    except:
        return

    tqdm_pandas(tclass=tqdm.tqdm_notebook)
    tqdm_pandas(tclass=tqdm.tqdm_notebook())

    # Test data
    df1 = pd.DataFrame({'a': list('aeiou'), 'b': list('AEIOU')})
    df2 = pd.DataFrame({'a': list('aeiou'), 'b': [1, 2, 3, 4, 5]})

    # Test for progress_apply
    res1 = df1.groupby('a').progress_apply(lambda x: x.str.lower())
    assert isinstance(res1, pd.DataFrame)

# Generated at 2022-06-14 13:08:55.710046
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas  # noqa: F401
    except ImportError:
        # Cannot unit-test pandas
        return True
    tqdm_pandas(tqdm, smoothing=0, postfix='tqdm-pandas test')
    assert tqdm == tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:08:59.368284
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    assert tqdm_pandas('tqdm') is None
    assert tqdm_pandas('tqdm_notebook') is None
    assert tqdm_pandas('tqdm_gui') is None

# Generated at 2022-06-14 13:09:11.090158
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    try:
        import pandas as pd
    except ImportError:
        return
    from tqdm import tqdm, trange
    from multiprocessing import Pool
    from tqdm.contrib.concurrent import process_map

    df = pd.DataFrame()
    df['x'] = range(20)
    df['y'] = range(20)

    def f_row(row):
        return row['x'] + row['y']

    def f_row_t(row):
        trange(5, desc='row')

    def f_group(group):
        return group.x + group.y

    ret = df.groupby('x').progress_apply(f_group, tqdm_kwargs={})

# Generated at 2022-06-14 13:09:23.705504
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    def f(df):
        return len(df.index) * 2
    # dataframe
    df = pd.util.testing.makeDataFrame()
    # df.groupby
    gb = df.groupby('A')
    # progress_apply
    progress_apply = gb.progress_apply
    # check pandas
    assert hasattr(progress_apply, 'tqdm_gui')
    assert hasattr(progress_apply, 'tqdm_notebook')

    # check tqdm_pandas
    tqdm_pandas(tqdm.tqdm)
    assert hasattr(progress_apply, 'tqdm')
    assert hasattr(progress_apply, 'tqdm_gui')

# Generated at 2022-06-14 13:09:35.938765
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, tqdm_pandas

    def my_func(i):
        return i ** 2

    df = pd.DataFrame([1, 2, 3, 4, 5, 6])
    with tqdm(total=len(df)) as pbar:
        df.progress_apply(my_func, meta={'pandas': pbar})

    with tqdm_pandas(tqdm(total=len(df))) as pbar:
        df.progress_apply(my_func, meta={'pandas': pbar})

    with tqdm_pandas(total=len(df)) as pbar:
        df.progress_apply(my_func, meta={'pandas': pbar})

    tqdm_pand

# Generated at 2022-06-14 13:09:44.390919
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.auto import tqdm
    df = pd.DataFrame(np.random.randn(10, 3), columns=list('abc'))

    # delay adapter case
    tqdm_pandas(tqdm)
    for _ in df.progress_apply(lambda x: x, axis=0):
        pass

    # progressbar case
    with tqdm(total=len(df)) as pbar:
        for _ in df.progress_apply(lambda x: x, axis=0):
            pbar.update(1)

    # progressbar case without total
    tqdm_pandas(tqdm)
    for _ in df.progress_apply(lambda x: x, axis=0):
        pass

    # multi index

# Generated at 2022-06-14 13:09:53.921995
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import datetime as dt
    from pandas.core.groupby import DataFrameGroupBy
    from pandas import DataFrame, Series

    _test_data = [('a', dt.datetime(2020, 1, 2)),
                  ('a', dt.datetime(2017, 1, 2)),
                  ('b', dt.datetime(2014, 2, 3)),
                  ('b', dt.datetime(2012, 3, 2)),
                  ('c', dt.datetime(2012, 3, 2)),
                  ('c', dt.datetime(2014, 2, 4)),
                  ('c', dt.datetime(2020, 1, 1))]
    _test_df = DataFrame(_test_data, columns=['X', 'Y'])
    _test_gb = _test_df.groupby('X')


# Generated at 2022-06-14 13:10:04.172896
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        import numpy
        assert True
    except ImportError:
        return

    from tqdm import tqdm_notebook
    tqdm_notebook.pandas(unit="rows", smoothing=0)

    df = pandas.DataFrame(numpy.random.randint(0, 100, (100000, 6)))
    # Test on Series
    df['sum'] = df.progress_apply(lambda x: x.sum(), axis=1)
    # Test on Dataframe
    df.progress_apply(lambda x: x.sum(), axis=0)


try:
    _ = tqdm_pandas(__name__)
except:
    pass

# Generated at 2022-06-14 13:10:08.044827
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    try:
        import tqdm.auto as tqdm
    except ImportError:  # pragma: no cover
        raise pytest.skip("tqdm not found")

    df = pd.DataFrame({'a': range(100), 'b': range(100, 200)})
    tqdm_pandas(tqdm, desc="Testing...")
    df.groupby('a').progress_apply(lambda x: x)

# Generated at 2022-06-14 13:10:19.878721
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    try:
        from pandas.core.groupby import DataFrameGroupBy  # pandas>=0.23
    except ImportError:
        from pandas.core.groupby.generic import DataFrameGroupBy
    for cls in [tqdm, tqdm.tqdm]:
        DataFrameGroupBy._original_progress_apply = DataFrameGroupBy.progress_apply
        tqdm_pandas(cls)
        assert DataFrameGroupBy.progress_apply is not DataFrameGroupBy._original_progress_apply
        del DataFrameGroupBy.progress_apply
        assert DataFrameGroupBy.progress_apply is DataFrameGroupBy._original_progress_apply
        del DataFrameGroupBy._original_progress_apply


# ******************************************************************************
# TODOs:


# Generated at 2022-06-14 13:10:41.769727
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas
    from tqdm.auto import tqdm as tqdmx

    # tqdm = tqdm_pandas(tqdm)
    # tqdm.pandas(tqdm)
    # tqdm.pandas()
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdmx)
    tqdm_pandas(tqdmx(), mininterval=1, maxinterval=1)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:51.344589
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas.core.groupby import DataFrameGroupBy
    from tqdm import tqdm_pandas, tqdm

    df = pd.DataFrame({
        'A': [1, 1, 2, 2],
        'B': ['a', 'b', 'c', 'd']
    })

    # Test that tqdm_pandas is registered properly (from the above docstring unit test)
    assert df.groupby('A').progress_apply.__doc__.rstrip() == """Progressively apply `func` to `group`,\n        return DataFrame whose column names are the `names` of `func`
        """

    # Test that tqdm_pandas allows other kwargs to be passed to tqdm
    tqdm_pandas(total=10)

# Generated at 2022-06-14 13:11:02.593174
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import pandas.util.testing as pdt
    import numpy as np
    from tqdm.tests import dummy_pandas_apply

    df = pd.DataFrame(np.random.random((10, 3)))
    type(dummy_pandas_apply(df)).pandas(deprecated_t=dummy_pandas_apply(df))
    type(dummy_pandas_apply(df)).pandas(df.groupby('A').B, deprecated_t=dummy_pandas_apply(df))

# Generated at 2022-06-14 13:11:08.086304
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas  # NOQA
    except ImportError:
        return
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.array([1, 2, 3]), index=list('abc'))
    assert df.groupby(df[0]).progress_apply(lambda x: x + 1)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:11:18.261632
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return

    # Test 1
    result = []
    for i in pd.Series(range(100)).progress_apply(lambda x: x + 1):
        result.append(i)
    assert result == list(range(1, 101))

    # Test 2
    result = []
    for i in pd.Series(range(100)).progress_apply(lambda x: x + 1,
                                                  show_default=False):
        result.append(i)
    assert result == list(range(1, 101))

    # Test 3
    result = []
    for i in pd.Series(range(100)).progress_apply(lambda x: x + 1,
                                                  show_default=True):
        result.append(i)
    assert result

# Generated at 2022-06-14 13:11:27.539901
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm, tqdm_notebook

    df1 = pd.DataFrame(np.random.randint(0, 10, (1000000, 6)),
                       columns=list('ABCDEF'))

    tqdm_pandas(tqdm)
    dfg = df1.groupby('A').progress_apply(lambda x: x**2)

    tqdm_pandas(tqdm_notebook)
    dfg = df1.groupby('A').progress_apply(lambda x: x**2)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:11:38.143943
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm_pandas

    def func(x):
        # pause for a random time
        from time import sleep
        import numpy as np
        sleep(np.random.randint(1, 10) / 100)
        return x

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    tqdm_pandas(tqdm())  # can use tqdm instance
    res = df.progress_apply(func)  # now you can use `progress_apply`
    assert len(df) == len(res)
    tqdm_pandas(tqdm)  # can use tqdm class directly
    res = df.progress_apply(func)
   