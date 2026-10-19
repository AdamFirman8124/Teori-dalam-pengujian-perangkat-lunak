

# Generated at 2022-06-14 13:01:37.606711
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm_pandas, tqdm
    from .autonotebook import tqdm, trange
    from .utils import _range

    def assert_eq(x, y):
        assert x == y

    df = pd.DataFrame([1, 2])
    for t in [tqdm, trange, tqdm_pandas]:
        tqdm.pandas(t)
        assert_eq(df.progress_apply(lambda x: x), df.progress_apply(lambda x: x))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:01:45.514634
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.autonotebook import tqdm as tqdm_base

    # Register tqdm() instance with DataFrameGroupBy.progress_apply()
    df = pd.DataFrame({
        'key': ['a', 'a', 'b', 'b'],
        'x': [1, 2, 1, 2]
    })

    def test_apply(g):
        import time
        time.sleep(.1)
        return g.x.sum()

    tclass = tqdm_base(total=df.groupby(['key']).ngroups)
    res = df.groupby(['key']).progress_apply(test_apply, tqdm=tclass)
    assert np.all(res == [3, 3])
   

# Generated at 2022-06-14 13:01:54.641194
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        try:
            import pandas  # NOQA
        except ImportError:
            raise unittest.SkipTest("pandas not found")
    from pandas import DataFrame
    from tqdm import tqdm
    from tqdm import tqdm_pandas as td  # NOQA

    df = DataFrame(
        {'i': [1, 2, 3, 4, 5, 6, 7, 8, 9],
         'j': [4, 5, 6, 3, 2, 1, 0, 0, 0]})
    with closing(StringIO()) as our_file:
        with tqdm(total=len(df), file=our_file, leave=False) as t:
            td(t)

# Generated at 2022-06-14 13:02:06.635306
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame

    tqdm_pandas(tqdm(range(1000)))
    tqdm_pandas(tqdm(), total=1000)
    tqdm_pandas(tqdm, total=1000)
    tqdm_pandas(tqdm(total=1000))

    p = tqdm(total=1000)
    tqdm_pandas(p)
    assert p.total == tqdm.auto_total

    p = tqdm(total=1000)
    tqdm_pandas(p, total=100)
    assert p.total == 100

    p = tqdm()
    tqdm_pandas(p, total=1000)
    assert p.total == 1000

    p = tqdm()
    tqdm_

# Generated at 2022-06-14 13:02:11.743409
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    N = 1000
    df = pd.DataFrame(np.random.random((N, 3)))
    tqdm_pandas(tqdm())
    print(df.groupby(1).progress_apply(lambda x: x[0].sum()), flush=True)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:17.888715
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    def test_bar(df):
        return df

    tqdm.pandas(desc="Example")
    try:
        tqdm_pandas(tqdm()).pandas(desc="Example")
    except TypeError:
        pass
    else:
        raise AssertionError("Should raise TypeError")
    tqdm_pandas(tqdm, desc="Example")
    tqdm_pandas(tqdm(desc="Example"))

# Generated at 2022-06-14 13:02:25.865438
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas, tnrange
    import pandas as pd
    a = pd.DataFrame({'x': [1, 2, 3, 4, 5]})
    for _ in tnrange(10):
        tqdm_pandas(tqdm(total=10), a.x, lambda x: x)
    tqdm_pandas(a.x, lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:33.808307
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # test tqdm class
    tqdm_pandas(tqdm, desc='test')
    # tqdm class already registered
    tqdm_pandas(tqdm, desc='test')
    # tqdm_notebook class
    tqdm_pandas(tqdm_notebook, desc='test')
    # tqdm_notebook class already registered
    tqdm_pandas(tqdm_notebook, desc='test')


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:41.367381
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy.random import rand
    tqdm_pandas(tqdm(total=1000000))
    DataFrame(rand(1000000)).groupby(0).progress_apply(len)
    tqdm_pandas(tqdm(total=1000000), desc='my_tqdm').pandas(
        DataFrame(rand(1000000)).groupby(0).progress_apply(len))

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:49.691488
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Regression test for tqdm_pandas"""
    from .auto import tqdm
    from .std import Numeric

    tqdm_pandas(tqdm)
    try:
        from numpy import random
        from pandas import DataFrame
        df = DataFrame(random.rand(1000, 100))
        tqdm_pandas(tqdm, desc="Pandas test")
        for _ in df.groupby(0).progress_apply(Numeric.sum):
            pass
    except:
        pass
    else:
        raise Exception("tqdm_pandas unit test failed")
    finally:
        tqdm_pandas.disable = True



# Generated at 2022-06-14 13:02:56.133210
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    df = pd.DataFrame({'a':[1,2,3], 'b':[5,5,5]})
    tqdm_pandas(tqdm, leave=False)(lambda x: x, df)

# Generated at 2022-06-14 13:03:02.769906
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return  # Ignore
    pd.core.groupby.DataFrameGroupBy.progress_apply = \
        pd.core.groupby.DataFrameGroupBy.apply
    tqdm_pandas(pd.core.groupby.DataFrameGroupBy)
    tqdm_pandas()

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:10.412262
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    # DataframeGroupBy.progress_apply
    df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))
    try:
        df.groupby('A').progress_apply(lambda x: x ** 2)
        raise AssertionError
    except AttributeError:
        pass
    tqdm_pandas(tqdm())
    df.groupby('A').progress_apply(lambda x: x ** 2)
    tqdm_pandas(tqdm(total=3))
    df.groupby('A').progress_apply(lambda x: x ** 2)
    tqdm_pandas(tqdm(total=4, leave=False))

# Generated at 2022-06-14 13:03:23.368617
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd  # import here to avoid test failure when pandas is missing

    # Please implement a unit test

# Generated at 2022-06-14 13:03:29.121175
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame(np.random.random((100, 1000)))
    for i in tqdm(range(100)):
        df = df.apply(lambda x: np.abs(x), axis=1)
    tqdm_pandas(df.groupby(0).progress_apply(lambda x: x))

# Generated at 2022-06-14 13:03:35.643442
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    # This function is not intended to test the implementation of `tqdm`!
    tqdm = tqdm_pandas

    # Test basic functionality
    tqdm(total=100).start(0)
    tqdm(total=100).close()

    with tqdm(total=100) as pbar:
        pbar.update(10)

    with tqdm(total=100) as pbar:
        pbar.update(10)
        pbar.close()

    with tqdm(total=100) as pbar:
        try:
            pbar.update(10)
            raise Exception
        except Exception:
            pbar.close()

    with tqdm(total=100) as pbar:
        pbar.update(10)


# Generated at 2022-06-14 13:03:48.584690
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function `tqdm_pandas`"""
    import pandas as pd
    import numpy as np
    from tqdm.autonotebook import tqdm

    # Check that it doesn't break pandas
    def progress_apply_workaround(self, func, *args, **kwargs):
        """
        Replicate pandas 0.25 `DataFrame.progress_apply`
        with `tqdm` progress bar.
        """
        from pandas.core.groupby import DataFrameGroupBy
        from functools import partial

        if isinstance(self, DataFrameGroupBy):
            return self.apply(func, *args, **kwargs)

        new_kwargs = {}

# Generated at 2022-06-14 13:03:54.546024
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from sklearn.utils import shuffle

    df = pd.DataFrame(shuffle(pd.DataFrame([1, 2, 3, 4, 5, 6, 7, 8], columns=list('a'))))
    tqdm_pandas(tqdm(desc='Test tqdm_pandas'))
    df.groupby('a').progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:04:05.991039
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, trange

    df = pd.DataFrame({"a": range(100), "b": range(100)})

    pbar = tqdm_pandas(tqdm(total=df.size))
    pbar.register()
    df.groupby("a").progress_apply(lambda x: x)
    pbar.close()

    t = trange(100)
    t.pandas()
    df.groupby("a").progress_apply(lambda x: x)
    t.close()

    t = trange(100)
    t.pandas(desc="tqdm_pandas")
    df.groupby("a").progress_apply(lambda x: x)
    t.close()



# Generated at 2022-06-14 13:04:16.291152
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas.core.groupby import DataFrameGroupBy
    from tqdm import tqdm

    df = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2, 3, 3]})

    tqdm_pandas(tqdm, desc='Test')
    assert DataFrameGroupBy.progress_apply == tqdm

    tqdm_pandas(tqdm())
    assert DataFrameGroupBy.progress_apply == tqdm

    tqdm_pandas(tqdm(desc='Test'))
    assert DataFrameGroupBy.progress_apply == tqdm


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:26.420850
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from pandas import DataFrame

    # unit test
    test_data = {
        'col_%d' % i: range(100)
        for i in range(4)
    }
    df = DataFrame(test_data)
    test_result = df.groupby('col_0').progress_apply(
        lambda x: x['col_1'].sum())
    assert isinstance(test_result, pd.Series)
    assert test_result.name == 'col_1'
    assert test_result.index.name == 'col_0'
    assert test_result[0] == sum(0 + i for i in range(100))
    assert test_result[1] == sum(1 + i for i in range(100))
    assert test_

# Generated at 2022-06-14 13:04:36.738975
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except:
        return

    try:
        import numpy as np
    except:
        np = None  # noqa

    with tqdm.tqdm(total=None,
                   dynamic_ncols=True) as progressable:
        progressable.pandas(desc='test')
        pd.DataFrame({'x': np.random.randint(0, 100, (10))}).groupby('x').progress_apply(lambda x: x)


if __name__ == '__main__':
    # as a debugging tool
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:39.674065
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test for tqdm_pandas"""
    from .std.testing import _test_tqdm_pandas
    _test_tqdm_pandas(tqdm_pandas)

# Generated at 2022-06-14 13:04:40.524254
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:04:50.162524
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm_pandas, tqdm

    def progress_apply(dfg, func, **kwargs):
        """Custom progress_apply with nested tqdm progress bar"""
        index = kwargs.get('index')
        new_df = pd.concat([
            func(group, **kwargs)
            for i, (key, group) in enumerate(
                tqdm(
                    dfg.__iter__(),
                    total=len(dfg),
                    desc="Group",
                    leave=False,
                    dynamic_ncols=True,
                    unit="group"))
        ], axis=0, ignore_index=index is None).__finalize__(dfg)
        return new_df


# Generated at 2022-06-14 13:04:56.911878
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd

        df = pd.DataFrame(np.random.randn(100, 100))
        with tqdm_pandas(total=len(df)) as pbar:
            df.progress_apply(lambda x: x ** 2, axis=1)
            pbar.update()
    except ImportError:
        return

# Generated at 2022-06-14 13:04:59.014970
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return

    try:
        from tqdm import tqdm
    except ImportError:
        return

    for tclass in [tqdm, tqdm.pandas]:
        pandas.DataFrame([1, 2, 3]).progress_apply(lambda x: x + 1, tclass=tclass)

# Generated at 2022-06-14 13:05:02.934119
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        tqdm_pandas(pd.DataFrame([]).groupby([]).progress_apply)
    except ImportError:  # pragma: no cover
        from tqdm._vendor.tqdm_pandas import tqdm_pandas
        pass

# Generated at 2022-06-14 13:05:15.437028
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    # Test tqdm decorator
    @tqdm_pandas
    def my_apply(t, x):
        import time
        time.sleep(0.1)
        return x + 1

    pd_input = pd.DataFrame({'x': [1, 2, 3]})
    print(my_apply(pd_input))
    my_apply.close()

    # Test tqdm function
    def my_func(x):
        import time
        time.sleep(0.1)
        return x + 1

    my_apply = tqdm_pandas(tqdm)
    print(my_apply(pd_input, my_func))
    my_apply.close()


if __name__ == '__main__':
    import pandas

# Generated at 2022-06-14 13:05:26.085800
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.auto import tqdm
    from tqdm import TqdmDeprecationWarning
    t = tqdm(total=100)
    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(t)
    assert len(w) > 0

    t = tqdm(total=100)
    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(t, pandas=False)
    assert len(w) == 0

    df = pd.DataFrame()
    df['A'] = np.arange(100)
    df['B'] = np.arange(100)

    def f(x):
        return x[0] + x

# Generated at 2022-06-14 13:05:38.941431
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas import Series, concat
    from tqdm import tqdm, TqdmDeprecationWarning

    def _test_progress_apply(df, tclass):
        """Test if `progress_apply` is decorated and working"""
        # Set-up
        N = 100

        def test_func(df):
            return df.x + df.y

        # Test 1
        df['z'] = df.progress_apply(test_func, axis=1)
        assert isinstance(df.z.sum(), int)

        # Test 2
        df['a'] = df.progress_apply(test_func, axis=1)
        assert isinstance(df.a.sum(), int)

        # Test 3

# Generated at 2022-06-14 13:05:44.172223
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas.util.testing import assert_equal
    from tqdm import trange
    try:
        from pandas import DataFrame
    except ImportError:
        return
    DataFrame([trange(100) for i in range(100)]).progress_apply(lambda x: x)

    def f(s):
        return s.mean()

    class fake_tqdm_cls:
        @staticmethod
        def pandas(df):
            return df

    # Test delayed adapter case

# Generated at 2022-06-14 13:05:48.510911
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    import tqdm

    A = np.random.randint(0, 100, (100000, 100))
    df = pd.DataFrame(A)

    for tclass in [tqdm.tqdm, tqdm.trange]:
        # if tclass is tqdm.tqdm:
        #     from tqdm import TqdmExperimentalWarning
        #     with TqdmExperimentalWarning():
        assert hasattr(tclass, 'pandas')

        # test1: progress_apply
        def progress_test(x):
            time.sleep(0.001)
            return x

        begin = time.time()
        df.groupby(0).progress_apply(progress_test)
        t_pandas

# Generated at 2022-06-14 13:05:52.611966
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return
    df = pandas.DataFrame(
        {'test': [1, 2, 3] * 100},
        index=range(300)
    )
    assert tuple(df['test'].progress_apply(lambda x: x * 2)) == (2, 4, 6) * 100

# Generated at 2022-06-14 13:05:58.679052
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return  # not installed
    n = 1e6
    simple_series = pd.Series(range(n))
    tqdm_pandas(tqdm(total=n), file=sys.stdout)
    res = simple_series.progress_apply(lambda x: x * 2)
    assert isinstance(res, pd.Series)
    assert (res == simple_series * 2).all()

# Generated at 2022-06-14 13:06:11.295241
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.auto import trange, tqdm

    # Test registered method
    tqdm_pandas(tqdm)
    df = pd.DataFrame(range(1000))
    df.groupby(0).progress_apply(lambda x: x)

    # Test registered method with tqdm arguments
    tqdm_pandas(tqdm, dynamic_ncols=True, desc="Bar")
    df = pd.DataFrame(range(1000))
    df.groupby(0).progress_apply(lambda x: x)

    # Test delayed registration via default tqdm arguments
    tqdm_pandas(trange, dynamic_ncols=True, desc="Baz")
    df = pd.DataFrame(range(1000))

# Generated at 2022-06-14 13:06:19.697236
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas()"""
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm._utils import _term_move_up
    from tqdm._utils_tests import _discrete_randint

    def dummy_tqdm(iterable, total=None, file=None):
        res = []
        for obj in iterable:
            res.append(obj)
            print(',', end='', file=file)
            file.flush()
        return res

    df = pd.DataFrame({'col_{}'.format(i): _discrete_randint(0, 9, 50) for i in range(5)})

    def sum_group(group):
        return (group.sum())

    tqdm.p

# Generated at 2022-06-14 13:06:27.822106
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4]})

    def test1(d):
        return d

    def test2(d):
        return d

    assert df.groupby('a').progress_apply(test1, meta='test').equals(df)
    assert df.groupby('a').progress_apply(test2, meta='test').equals(df)

# Generated at 2022-06-14 13:06:33.026595
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm_gui

    df = pd.DataFrame(np.random.randn(3, 100000))
    df.progress_apply(lambda x: x.mean(), axis=0)
    tqdm_pandas(tqdm_gui)
    df.progress_apply(lambda x: x.mean(), axis=0)

# Generated at 2022-06-14 13:06:40.850205
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame()
    df['x'] = np.random.rand(10000)
    df['y'] = np.random.rand(10000)

    tqdm_pandas(tqdm(), leave=False)
    df.groupby('y').progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:54.453067
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function 'tqdm_pandas'."""
    import pandas as pd

    df = pd.DataFrame({"a": range(100), "b": range(100)})
    ix = pd.DataFrame({"a": range(100)})
    ix['b'] = ix['a'] + 1
    # test_tqdm_pandas_registration
    tqdm_pandas(tqdm(total=100))
    assert 'pbpandas_adapter' in df.progress_apply.__name__
    tqdm_pandas(tqdm(total=100))
    assert 'pbpandas_adapter' in df.progress_apply.__name__
    tqdm_pandas(tqdm(total=0))

# Generated at 2022-06-14 13:07:02.938900
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    N = 1000
    cnt = 0

    df = pd.DataFrame(np.random.randint(0, 10, size=(N, 4)),
                      columns=list('ABCD'))

    def groupby_test(df):
        global cnt
        for name, group in df.groupby('A'):
            for _, row in group.iterrows():
                cnt += 1
                print(row['B'])

    # Without tqdm:
    cnt = 0
    groupby_test(df)
    assert cnt == N

    # With tqdm:
    pdt = tqdm.pandas(**tqdm.__dict__)
    cnt = 0

# Generated at 2022-06-14 13:07:05.914578
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from .main import tqdm_pandas
    __test__ = {
        'tqdm_pandas': test_tqdm_pandas,
    }

# Generated at 2022-06-14 13:07:16.875722
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    arr = np.random.random((100, 100))
    df = pd.DataFrame({'a': arr, 'b': arr, 'c': arr})

    # Normal usage
    with tqdm_pandas(total=df.shape[0]) as pbar:
        def f_normal(x):
            pbar.update()
        df.progress_apply(f_normal)

    # Tqdm adaptor case
    with tqdm_pandas(tclass=tqdm, total=df.shape[0]) as pbar:
        def f_adaptor(x):
            pbar.update()
        df.progress_apply(f_adaptor)

    # Tqdm adaptor case 2

# Generated at 2022-06-14 13:07:27.652190
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, TqdmTypeError
    from pandas import DataFrame, Series
    df = DataFrame({'a': [1, 2, 3], 'b': ['x', 'y', 'z']})
    ser = Series(['a', 'b', 'c'])

    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm)

    with tqdm(total=100, disable=True) as t:
        tqdm_pandas(t)
        assert t.total == 100
        df.groupby('b').progress_apply(lambda x: x ** 2)

    with tqdm(disable=True) as t:
        t.total = 5
        tqdm_pandas(t)
        assert t.total == 5


# Generated at 2022-06-14 13:07:35.256189
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, trange
    import pandas as pd

    # Dummy Dataframe
    _ = pd.DataFrame({'a': [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.],
                      'b': [10., 9., 8., 7., 6., 5., 4., 3., 2., 1.]})
    # Dummy tqdm instance
    with trange(10) as t:
        # Unit test tqdm_pandas with explicit instance
        tqdm_pandas(t, file=sys.stdout)
        # Unit test tqdm_pandas with implicit instance

# Generated at 2022-06-14 13:07:41.305913
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm.auto import trange

    # DataFrame.
    df = pd.DataFrame({'x': range(1000)})
    df = tqdm(df, desc='1st loop')
    df = pd.DataFrame({'x': range(999)}, index=df.index)
    df = tqdm(df, desc='2nd loop')
    df = pd.DataFrame({'x': range(100)}, index=df.index)
    df = tqdm(df, desc='3rd loop')
    for i in trange(100, desc='4th loop'):
        df = pd.DataFrame({'x': range(i)})

    # GroupBy.

# Generated at 2022-06-14 13:07:52.712301
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))

    # Register `tqdm` with `pandas.core.groupby.DataFrameGroupBy.progress_apply`.
    # Allows use of `progress_apply` and `progress_map`
    tqdm.pandas(desc="my bar!")

    # Now you can use `progress_apply` instead of `apply`
    df.groupby(0).progress_apply(lambda x: x**2)
    # can also group by multiple columns
    df.groupby([0, 1]).progress_apply(lambda x: x**2)

    # Or to use `progress_map`, you need to wrap the `groupby` first:
    df

# Generated at 2022-06-14 13:08:00.660486
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_pandas
    from pandas import DataFrame
    import numpy as np
    df = DataFrame(np.random.randn(10, 3))
    df.progress_apply(lambda x: x**2)
    df.groupby('a').progress_apply(lambda x: x**2)
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:12.972119
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm
    import time

    tqdm_pandas(tqdm.tqdm)

    ## Generate a pandas DataFrame
    df = pd.DataFrame(np.random.randn(1000000, 4), columns=list('ABCD'))

    def multiply_by_2(x):
        time.sleep(0.0001)
        return x * 2

    # Apply multiply_by_2 on each column
    tqdm.pandas(desc='Progress')
    result = df.progress_apply(multiply_by_2)

    assert (result.A < 2 * df.A).all()
    assert (result.B < 2 * df.B).all()

# Generated at 2022-06-14 13:08:27.688889
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    n = 1000
    df = pd.DataFrame({'x': range(n), 'y': range(n)})

    for i, j in df.groupby('y').progress_apply(lambda x: (x, len(x))):
        assert len(j) == 1

    for i, j in df.groupby('y', group_keys=False).progress_apply(lambda x: len(x)):
        assert len(j) == 1

    for i, j in df.groupby('y').progress_apply(lambda x: (x, len(x)), min_itemsize=10):
        assert len(j) == 1


# Generated at 2022-06-14 13:08:39.010268
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import unittest
    import tempfile
    import os

    from pandas import DataFrame
    from tqdm import tqdm

    try:
        from unittest import mock  # PY3+
    except ImportError:
        import mock  # PY2

    tclass = tqdm(total=100, file=tempfile.NamedTemporaryFile())
    with mock.patch('sys.stderr', spec=sys.stderr) as mocked:
        tqdm_pandas(tclass)
        assert "Please use `tqdm.pandas(...)` instead" \
               " of `tqdm_pandas(tqdm, ...)`." in mocked.write.call_args_list[0][0][0]

# Generated at 2022-06-14 13:08:45.938332
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        with warnings.catch_warnings(record=True) as ws:
            warnings.simplefilter('always')
            tqdm_pandas(tqdm)
            tqdm_pandas(tqdm.tqdm)
            tqdm_pandas(tqdm.tqdm_notebook)
            tqdm_pandas(tqdm.tqdm_gui)
            assert any(str(w.message).startswith(
                'Please use `tqdm.pandas(...)`') for w in ws)
    except TqdmDeprecationWarning as e:
        print(e.message)



# Generated at 2022-06-14 13:08:56.481720
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Test _tqdm_pandas(...)
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    tqdm_pandas(df.groupby(0).progress_apply(lambda x: x ** 2))

    # Test _tqdm_pandas(tqdm_pandas(...))
    tqdm_pandas(tqdm_pandas(df.groupby(0).progress_apply(lambda x: x ** 2)))

    # Test _tqdm_pandas(tqdm(...))
    tqdm_pandas(tqdm(df.groupby(0).progress_apply(lambda x: x ** 2)))


# Main function


# Generated at 2022-06-14 13:08:57.795980
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:09:06.412585
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.autonotebook import tqdm
    a = np.random.rand(100,100)
    tqdm_pandas(tqdm.tqdm, file=sys.stdout)
    #tqdm_pandas(tqdm.tqdm)
    df = pd.DataFrame(a)
    df.progress_apply(lambda x: x)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:13.925674
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    t = tqdm(total=10)
    t.write = lambda *args, **kwargs: None
    t.update()
    tqdm_pandas(t)
    t.close()
    try:
        DataFrame([[1, 2], [3, 4]]).groupby(1).progress_apply(lambda x: x)
    except TypeError:
        pass
    else:
        raise Exception("`tqdm_pandas(t)` should not be used outside of a "
                        "`with tqdm(...) as t:` block")

# Generated at 2022-06-14 13:09:19.910073
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        tqdm_pandas(tqdm())
    except Exception as e:
        print('Test failed with error message: "{0}"'.format(e))
        sys.exit(1)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:28.443944
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm.pandas import tqdm_pandas
    from .tests_tqdm import pretest_posttest

    def test_func(x):
        return x**2

    N = 1000000
    df1 = pd.DataFrame(np.random.randint(0, 10, size=(N, 4)))
    # Test deprecated function tqdm_pandas
    pretest_posttest(tqdm_pandas(tqdm(leave=False, unit='MB'), unit_scale=True),
                     df1.progress_apply, test_func)
    # Test deprecated class tqdm_pandas

# Generated at 2022-06-14 13:09:34.324482
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    if (sys.version_info[0] * 10 + sys.version_info[1]) < 35:
        return False
    try:
        from tqdm import tqdm
        from tqdm.contrib import pandas
    except:
        return False
    tqdm_pandas(tqdm, smoothing=0.05)
    return True

# Generated at 2022-06-14 13:09:48.072097
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_gui
    v = lambda x: x * x

    x = tqdm_gui(range(1, 10), desc='trial')
    df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                       'y': [9, 8, 7, 6, 5, 4, 3, 2, 1]})
    # assert df.groupby('y').progress_apply(v) == "test"
    tqdm_pandas(tqdm_gui)
    assert df.groupby('y').progress_apply(v) == "test"
    tqdm_pandas(tqdm_gui())
    assert df.groupby('y').progress_apply(v) == "test"

# Generated at 2022-06-14 13:09:54.944433
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.contrib.test import test_tqdm
    with test_tqdm(leave=True) as t:
        t.update()
        df = pd.DataFrame([1, 2, 3, 4])
        df.groupby(1).progress_apply(lambda x: x)
        assert isinstance(t.last_iterable, pd.core.groupby.DataFrameGroupBy)

# Generated at 2022-06-14 13:09:59.221465
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    # Test pandas register
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    df_g = df.groupby('A').progress_apply(len)
    if 'with tqdm' in str(df_g):
        print('pandas.groupby.progress_apply test passed')
    else:
        print('pandas.groupby.progress_apply test failed')

    # Test pandas unregister
    df_g = df.groupby('A').progress_apply(len, register_tqdm=False)
    if 'with tqdm' not in str(df_g):
        print('pandas.groupby.progress_apply test passed')

# Generated at 2022-06-14 13:10:05.402700
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    tqdm_pandas(tqdm)

    class TestTqdm:
        def __init__(self):
            pass

        @staticmethod
        def pandas(*args, **kwargs):
            pass

    tqdm_pandas(TestTqdm)
    tqdm_pandas(TestTqdm())


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:15.478118
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest

    assert hasattr(tqdm(pandas=True), 'set_description')
    assert hasattr(tqdm(pandas=True), 'set_postfix')
    assert hasattr(tqdm(pandas=True), '__enter__')
    assert hasattr(tqdm(pandas=True), '__exit__')


if __name__ == '__main__':
    from _tqdm import main
    main()

# Generated at 2022-06-14 13:10:23.706371
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, trange
    import pandas as pd

    def func_1(x, **kws):
        return x * x

    def func_2(x, **kws):
        return pd.Series([x, x * x], index=['first', 'second'])

    df = pd.DataFrame({'a': [1, 2, 3] * 10, 'b': list(range(30))})

    # iteration based
    exp_1 = df.a.progress_apply(func_1)
    tqdm_pandas(tqdm(desc="", total=len(df.a)))
    obs_1 = df.a.progress_apply(func_1)
    assert exp_1.equals(obs_1)

    exp_2 = df.progress_apply

# Generated at 2022-06-14 13:10:27.017041
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
        pd.DataFrame({'a': np.random.randn(100), 'b': np.random.randn(100)}) \
            .groupby('a').progress_apply(lambda _: _)  # noqa
        print("Test passed")
    except:
        print("Test failed")
        raise

# Generated at 2022-06-14 13:10:37.635183
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time

    # Test deprecated method tqdm_pandas(tclass, ...)
    if hasattr(pd, 'DataFrame'):

        tqdm_pandas(tclass=pd.DataFrame, ascii=True)

        df = pd.DataFrame({'a': [1, 2, 3, 4, 5],
                           'b': [1, 2, 3, 4, 5],
                           'c': [1, 2, 3, 4, 5]})

        df.groupby('a').progress_apply(lambda x: time.sleep(0.5))

        df.progress_apply(lambda x: time.sleep(0.5))

    # Test deprecated method tqdm_pandas(tclass(...), ...)
   

# Generated at 2022-06-14 13:10:48.351723
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    from tqdm import tnrange
    from tqdm import tqdm

    if not (hasattr(pd, 'version') and pd.version.version.startswith('0.17')):
        raise SkipTest

    with closing(StringIO()) as our_file:
        tqdm_pandas(tqdm(desc='i=', file=our_file),
                    total=10, mininterval=0.01)

        # test over the series
        pd.Series(np.random.rand(10000,), name='A').progress_apply(
            lambda x: x ** 2)

# Generated at 2022-06-14 13:10:59.264694
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from .tqdm import tqdm
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm(), total=100)
    tqdm_pandas(tqdm.__name__)
    import io
    tqdm_pandas(tqdm(), file=io.StringIO())
    tqdm_pandas(tqdm.__name__, file=io.StringIO())

    # direct call
    tqdm.pandas()
    tqdm.pandas(total=100)
    tqdm.pandas(file=io.StringIO())

    # deprecated case

# Generated at 2022-06-14 13:11:19.104207
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    pd_test = tqdm_pandas(tqdm)
    df = pandas.DataFrame({'a': [1,2,3,4,5], 'b': [6,7,8,9,10]})
    def inc(x):
        return x+1
    df[['a', 'b']].progress_apply(inc)

# Generated at 2022-06-14 13:11:29.686199
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except:
        return
    from .tqdm import tqdm
    from .tqdm import trange
    from .tqdm import tnrange
    from .tqdm import tqdm_notebook
    from .tqdm import tgrange
    from .tqdm import tqdm_pandas
    from .tqdm import tqdm_gui
    from .tqdm import tqdm_gui
    import time

    # pylint:disable=unused-variable
    __tester = 1  # hi pylint, I need those classes to be instantiated
    tqdm_pandas(tqdm)
    tqdm_pandas(trange)
    tqdm_pandas(tnrange)
    tq