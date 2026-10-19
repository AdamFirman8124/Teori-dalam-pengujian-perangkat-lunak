

# Generated at 2022-06-14 13:01:43.342873
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    def f(x):
        """Dummy function to test passing a tqdm instance to it
        """
        return x

    df = DataFrame({'a': range(10000), 'b': range(10000)})
    df.progress_apply(f, axis=0)

    tqdm_pandas(tqdm)
    df.progress_apply(f, axis=0)
    tqdm_pandas(tqdm())
    df.progress_apply(f, axis=0)


tqdm_pandas.__doc__ = tqdm_pandas.__doc__.format(
    pandas=("pandas", pandas.__version__))

# Generated at 2022-06-14 13:01:53.642822
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)


if __name__ == '__main__':
    from tqdm import tqdm, trange
    from pandas import DataFrame

    with tqdm(total=500) as pbar:
        for i in trange(500):
            pbar.update()
            pbar.set_description("Processing %i" % i)

    tqdm_pandas(tqdm)
    df = DataFrame(dict(a=[1, 2, 3], b=[2, 3, 4]))
    tqdm.pandas(desc="example")
    df.groupby("a").progress_apply(lambda x: tqdm.pandas.get_lock().write("foo"))
    tqdm.pand

# Generated at 2022-06-14 13:02:02.660643
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, tqdm_gui
    df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]})

    t = tqdm_pandas(tqdm(total=len(df)))
    df.groupby('a').progress_apply(lambda x: x)
    df.progress_apply(lambda x: x)

    t = tqdm_pandas(tqdm_gui(total=len(df)))
    df.groupby('a').progress_apply(lambda x: x)
    df.progress_apply(lambda x: x)


if __name__ == '__main__':
    from tqdm import tqdm
    test_tqdm

# Generated at 2022-06-14 13:02:06.788031
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    pd = tqdm.pandas(file=sys.stderr)
    pd.progress_apply(lambda x: x, axis=1)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:14.196468
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import trange
    from tqdm.pandas import tqdm_pandas

    df = pd.DataFrame(np.random.random(size=(1000, 3)))

    # "classic" tqdm
    with trange(10) as t:
        for i in t:
            t.set_description("Desc %i" % i)
            df.progress_apply(len)

    # with tqdm_pandas(t):
    with trange(10) as t:
        for i in t:
            t.set_description("Desc %i" % i)
            df.progress_apply(len)



# Generated at 2022-06-14 13:02:17.281302
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test via the tqdm.tests.autogen.test_tqdm_pandas function."""
    from tqdm.tests.autogen import test_tqdm_pandas
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:23.902658
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import time
    import pandas as pd
    import numpy as np
    from tqdm import tqdm_pandas
    from tqdm import tqdm

    # Create input dataframe with same length as tqdm instance.
    df = pd.DataFrame({'foo': np.random.rand(10)})

    # Test usage of `tqdm_pandas` as a method
    t = tqdm(total=len(df))
    df.progress_apply(lambda row: time.sleep(0.1), axis=1, t=t)
    assert t.n == 10

    # Test usage of `tqdm_pandas` as a function
    t = tqdm(total=len(df))
    tqdm_pandas(t=t)
    df.progress_

# Generated at 2022-06-14 13:02:34.710987
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tempfile
    import pandas as pd
    import numpy as np

    with tempfile.TemporaryFile(mode='w+') as f:
        # Test deprecated interface
        a = tqdm(range(10), file=f)
        type(a).pandas(deprecated_t=a)
        df = pd.DataFrame({'a': np.arange(100)})
        df.groupby('a').progress_apply(lambda x: 1)
        f.seek(0)
        assert '|/--\\|' in f.read()

        # Test new interface
        a = tqdm(range(10), file=f)
        tqdm.pandas(a)
        df = pd.DataFrame({'a': np.arange(100)})
        df.groupby

# Generated at 2022-06-14 13:02:45.101760
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm import tqdm_pandas
    from pandas import DataFrame


# Generated at 2022-06-14 13:02:47.981313
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm_pandas
    from tqdm.tests import tests
    tests.test_tqdm_pandas(tqdm_pandas)



# Generated at 2022-06-14 13:03:01.576064
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas.util.testing import makeDataFrame
    import numpy as np
    N = 100
    test_df = makeDataFrame()

# Generated at 2022-06-14 13:03:08.951536
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from .gui import tqdm

    with tqdm(disable=True) as t:
        t.pandas()
        assert hasattr(DataFrame, 'progress_apply')
        DataFrame([[1], [2], [3]]).groupby(0).progress_apply(len, show_count=True)
        assert not hasattr(DataFrame, 'progress_apply')

# Generated at 2022-06-14 13:03:21.018188
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit testing for `tqdm_pandas`.
    """
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    # Testing delayed form
    type(tqdm).pandas(tqdm)

    # Testing tqdm(...) form
    # tqdm.pandas(tqdm())
    tqdm_pandas(tqdm())

    # Testing for actual performance
    df = pd.DataFrame({"a": np.random.randint(0, 5, size=10000000)})
    assert df.groupby(["a"]).progress_apply(sum).equals(df.groupby(["a"]).apply(sum))


if __name__ == "__main__":
    test_tqdm_pandas

# Generated at 2022-06-14 13:03:31.101684
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    a = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [3, 5, 7, 1, 2, 4]})
    a = a.groupby('A')
    a.progress_apply(lambda x: x)

    # Test delayed adapter
    tqdm_pandas(tqdm)
    # Test instantiated tqdm
    tqdm_pandas(tqdm())
    # Run test
    a.progress_apply(lambda x: x)

    # Test delayed adapter with kwargs
    tqdm_pandas(tqdm, mininterval=0.1)
    # Test instantiated tqdm with kwargs
    tqdm_pandas

# Generated at 2022-06-14 13:03:39.119304
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return  # skip
    tqdm_pandas(tqdm(total=4))
    tqdm_pandas(tqdm(total=4), total=4)
    pd.progress_apply(pd.Series(), lambda x: x)
    pd.progress_apply(pd.Series(range(4)), lambda x: x)
    if 'nested' in sys.argv:
        pd.progress_apply(pd.Series(range(4)),
                          lambda x: pd.Series([1, 2, 3]).progress_apply(
                              lambda x: x))


# Backward-compatibility

# Generated at 2022-06-14 13:03:46.903578
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        pass
    else:
        import numpy as np
        tqdm_pandas(pd, smoothing=0.1)
        tqdm_pandas(pd.DataFrame(range(10)).groupby(0).progress_apply(len))
        for series in range(10):
            tqdm_pandas(pd.DataFrame(np.random.random((series, series))))

# Generated at 2022-06-14 13:03:56.396296
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas import Series
    from tqdm import tqdm
    from tqdm import tqdm_pandas

    df = DataFrame(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],
         [17, 18, 19, 20]],
        columns=['a', 'b', 'c', 'd'])
    df['e'] = Series(['ab', 'cd', 'ef', 'gh', 'ij'])
    df['f'] = Series(['ab', 'cd', 'ef', 'gh', 'ij'])

    tqdm_pandas(tqdm, total=len(df))

# Generated at 2022-06-14 13:04:06.548163
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest("pandas is not installed")

    try:
        tqdm_pandas(tqdm, desc='Testing')
        df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5]})
        with closing(StringIO()) as our_file:
            with redirect_stdout(our_file):
                df.groupby('a').progress_apply(lambda x: x)
            assert 'Testing' in our_file.getvalue()
    finally:
        if 'progress_apply' in dir(pd.core.groupby.DataFrameGroupBy):
            del pd.core.groupby.DataFrameGroupBy.progress_apply

# Generated at 2022-06-14 13:04:13.192236
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [1, 2, 3, 4], 'c': [1, 2, 3, 4]})
    tqdm_pandas(tqdm)
    # df.groupby('a').progress_apply(lambda x: x.sum())  # doctest: +SKIP

# Generated at 2022-06-14 13:04:23.275404
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    import numpy as np

    # list comprehension
    tqdm_pandas(tqdm())
    df = DataFrame([[i, i * i] for i in range(10000)])
    dfc = df.groupby(df[0] % 100).progress_apply(
        lambda x: (x[0].max(), x[1].sum()))
    assert dfc.sum().sum() == df.sum().sum()

    # numpy array
    tqdm_pandas(tqdm())
    df = DataFrame(np.random.randn(10000, 20))
    df = df + df
    df = df.add(df, fill_value=0)

# Generated at 2022-06-14 13:04:39.270297
# Unit test for function tqdm_pandas
def test_tqdm_pandas():

    try:
        import pandas
    except ImportError:
        return
    else:
        import pandas as pd

    import io
    import tqdm
    from tqdm import tqdm

    with io.StringIO() as buf:
        try:
            tqdm_pandas(tqdm, file=buf)
        except TypeError:
            pass
        else:
            assert False, 'tqdm_pandas should fail if deprecated tqdm is not type.'

        tqdm_pandas(tqdm, file=buf)
        x = pd.DataFrame(data={'id': [1, 2, 3],
                               'length': [10, 20, 30]})

# Generated at 2022-06-14 13:04:48.297126
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.auto import tqdm

    def dummy_func(x):
        assert isinstance(x, pd.Series)
        return x.mean()

    df = pd.DataFrame(np.random.rand(1000, 10))
    var = df.groupby(0).progress_apply(dummy_func)
    assert isinstance(var, pd.Series)
    assert len(var) == len(df.groupby(0))

    # tqdm_pandas(tqdm)
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm.tqdm)

    for _ in range(10):
        i = np.random.randint(1, 10)
        df

# Generated at 2022-06-14 13:04:53.410946
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        tqdm_pandas(tqdm(range(10)))
        pd.DataFrame({'x': range(10)}).groupby('x').progress_apply(lambda x: None)
    except ImportError:
        pass

# Generated at 2022-06-14 13:04:58.447432
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm(total=100))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:08.177400
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # check that arguments are passed correctly
    with disable_dashboard():
        with closing(StringIO()) as our_file:
            tqdm_pandas(tqdm(file=our_file), total=100)
            assert "100it" in our_file.getvalue()

    # check that compatibility with legacy `tqdm_*` classes works
    tqdm_pandas(tqdm_notebook)
    tqdm_pandas(tqdm_gui)

    # check that delayed adapter works
    with closing(StringIO()) as our_file:
        with closing(tqdm(file=our_file)) as t:
            tqdm_pandas(t, total=100)
        assert "100it" in our_file.getvalue()

    # check that calling without arguments fails
   

# Generated at 2022-06-14 13:05:14.585737
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import warnings

    try:
        import unittest.mock as mock
    except ImportError:
        import mock
    warnings.simplefilter('always')
    with mock.patch('warnings.warn') as mocked_warn:
        tqdm_pandas(1)
        assert mocked_warn.call_count == 1
        tqdm_pandas(5, file=mock.MagicMock())
        assert mocked_warn.call_count == 2
    tqdm_pandas(tqdm(total=100))

    # Test that progress_apply works if tqdm is not active
    df0 = pd.DataFrame([])
    df0.groupby(df0.index // 2).progress_apply(lambda x: None)
    # test that progress_apply works with

# Generated at 2022-06-14 13:05:21.856985
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for `tqdm_pandas`"""
    class test_tqdm:
        class tclass:
            @staticmethod
            def pandas_test(*args, **kwargs):
                pass
    assert 'tqdm_pandas' in globals(), "Module `tqdm.pandas` must export function `tqdm_pandas`"
    orig_tqdm_pandas = tqdm_pandas
    def tqdm_pandas_mock(*args, **kwargs):
        tqdm_pandas_mock.called.append((args, kwargs))
        orig_tqdm_pandas(*args, **kwargs)
    tqdm_pandas_mock.called = []

# Generated at 2022-06-14 13:05:25.343084
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    df = pd.util.testing.makeDataFrame()
    with tqdm_pandas(total=len(df)) as pbar:
        _ = df.groupby('A').progress_apply(lambda x: x)
        pbar.close()



# Generated at 2022-06-14 13:05:33.148581
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import trange

    # Create DataFrame and register it with tqdm
    df = pd.DataFrame({'a': [1, 2, 3] * 10, 'b': [1, 2, 3] * 10})
    tqdm_pandas(trange(len(df)))

    # Compute and print sum of each column
    df.groupby('a').progress_apply(lambda x: sum(x))

    # Reset pandas console output
    tqdm_pandas.pandas(None)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:44.683416
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm_pandas as tqdm

    df = pd.DataFrame(np.random.randint(0, 100, (10000, 4)), columns=list('ABCD'))

    # Register `tqdm` with `pandas`
    tqdm.pandas(tqdm)

    # Now you can use `progress_apply` instead of `apply`
    # and `progress_map` instead of `map`
    df.groupby('A').progress_apply(
        lambda x: x ** 2)  # will show a tqdm-based progress bar
    df.progress_apply(lambda x: x ** 2)  # can also be used for dfs

# Generated at 2022-06-14 13:05:59.644067
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with captured_stdout() as stdout:
        tqdm_pandas(tqdm)
    assert any(line == 'Warning : `tqdm_pandas` was deprecated in version 0.23 and will be removed in version 0.24.'
               for line in stdout.getvalue().split())

    with captured_stdout() as stdout:
        tqdm_pandas(tqdm)
    assert any(line == 'Warning : Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.'
               for line in stdout.getvalue().split())

# Generated at 2022-06-14 13:06:12.413548
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.auto import trange
    from tqdm import tqdm

    def func(x):
        return x + 1

    # DataFrame
    for df in [pd.DataFrame([[1, 1], [2, 2], [3, 3]]),
               pd.DataFrame([[1, 1], [1, 1], [3, 3]])]:
        for iterable in [df, df.iloc]:
            for t in [trange, tqdm]:
                for series in [True, False]:
                    tqdm_pandas(t(leave=True))
                    res = iterable.progress_apply(func, axis=1, result_type=series)
                    assert isinstance(res, pd.Series) if series else pd.DataFrame

# Generated at 2022-06-14 13:06:20.521652
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function `tqdm_pandas`.
    """

    from collections import namedtuple
    from tqdm.std import TqdmType, TqdmTypeDeprecationWarning
    from tqdm.autonotebook import tqdm

    class MyTqdmType(TqdmType):
        """
        A mock `tqdm` class.
        """
        @staticmethod
        def pandas(t):
            """
            Registers the given `tqdm` instance with
            `pandas.core.groupby.DataFrameGroupBy.progress_apply`.
            """
            pass

    t = MyTqdmType(...)
    tqdm_pandas(t)

    t = tqdm(...)
    tqdm_pandas(t)

    #

# Generated at 2022-06-14 13:06:27.455131
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas."""
    tqdm = tqdm_pandas(tqdm)
    assert isinstance(
        tqdm.pandas,
        types.MethodType), "tqdm not registered with tqdm_pandas"


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:34.718497
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from .std import tqdm

    tqdm_pandas(tqdm)

    pdf1 = pd.DataFrame([[10, 20, 30, 40], [1, 2, 3, 4]]).T
    pdf2 = pdf1.copy()
    pdf1.groupby(0).progress_apply(lambda x: x)

    tqdm(pdf2.groupby(0).apply(lambda x: x), total=len(pdf2))._instances

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:39.915061
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas as pd
    df = pd.DataFrame({'x': ['a', 'b', 'c']})
    tqdm_pandas(tqdm.tqdm, tclass=tqdm.tqdm_gui)
    df.groupby('x').progress_apply(len)

# Generated at 2022-06-14 13:06:50.297880
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function `tqdm_pandas`."""
    import pandas as pd

    tqdm_pandas(tqdm)

    df = pd.DataFrame(
        columns=('first', 'second'),
        data=[
            {'first': 1, 'second': 2},
            {'first': 3, 'second': 4},
            {'first': 5, 'second': 6},
            {'first': 7, 'second': 8},
            {'first': 9, 'second': 10},
        ])

    with closing(StringIO()) as buf:
        with redirect_stdout(buf):
            df.groupby('first').progress_apply(lambda g: g.sum())
        assert 'Failed to enable progress' not in buf.getvalue()


# -----------------------------------------------------------------------------

# DEP

# Generated at 2022-06-14 13:06:57.520923
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        import numpy as np

        df = pandas.DataFrame({'a': np.random.random(100)})

        with tqdm(total=len(df.index)) as pbar:
            def wrapper(*args, **kwargs):
                pbar.update()
                return np.sum(*args, **kwargs)

            tqdm_pandas(pbar)
            df.groupby('a').progress_apply(wrapper)
    except Exception:
        pass



# Generated at 2022-06-14 13:07:06.839863
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm, tqdm_pandas

    tqdm_pandas(tqdm())

    with tqdm(total=10) as pbar:
        data = DataFrame({"A": [1, 2, 3, 4, 5], "B": [3, 5, 6, 7, 8]})
        data.groupby("A").progress_apply(lambda x: x ** 2).tqdm.tqdm_gui(pbar)

    tqdm_pandas(tqdm(total=10))
    DataFrame({"A": [1, 2, 3, 4, 5], "B": [3, 5, 6, 7, 8]}).groupby("A").\
        progress_apply(lambda x: x ** 2).tqdm.t

# Generated at 2022-06-14 13:07:15.244898
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return

    try:
        tqdm_pandas(tqdm(total=100))
    except TqdmDeprecationWarning:
        pass
    else:
        raise Exception("Should have raised TqdmDeprecationWarning")

    tqdm_pandas(tqdm.pandas(total=100))
    try:
        tqdm_pandas(tqdm.pandas(total=100))
    except AttributeError:
        pass
    else:
        raise Exception("Should have raised AttributeError")

# Generated at 2022-06-14 13:07:42.861289
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import numpy as np
    import tqdm

    df = pandas.DataFrame({'a': np.arange(1000), 'b': np.arange(1000),
                           'c': np.arange(1000)})

    # test with pandas Series
    assert len(list(df['a'].progress_apply(lambda x: x ** 2))) == 1000

    # test with pandas DataFrame
    assert len(list(df.progress_apply(
        lambda x: x['a'] ** 2 + x['b'] ** 2 + x['c'] ** 2, axis=1))) == 1000

    # test with pandas GroupBy

# Generated at 2022-06-14 13:07:53.631671
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    test = pd.DataFrame(columns=['a', 'b'])
    # test.progress_apply()
    test.progress_apply(lambda x: x+10)
    from tqdm import tqdm
    tqdm.pandas(tclass=None, leave=False)
    test.progress_apply(lambda x: x+10)
    try:
        tqdm_pandas(tqdm)
        assert False
    except Exception as e:
        print(e)
    try:
        tqdm_pandas(tqdm(total=10))
        assert False
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:01.960305
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
        import tqdm

        # Enable pandas progress_apply function
        tqdm_pandas(tqdm)

        # Test vectors
        df = pd.DataFrame({'col1': np.arange(10)})

        # Test dataframe apply
        df.apply(lambda x: 2 * x)

        # Test groupby apply
        df.groupby(lambda x: 0).progress_apply(lambda x: 2 * x)

        print('All Test Passed!')
        return True
    except Exception as e:
        print(e)
        return False

# Generated at 2022-06-14 13:08:07.957809
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # THIS TEST IS SUPPOSED TO FAIL UNLESS THE WARNING IS DISPLAYED
    import pandas

    with warnings.catch_warnings(record=True) as ws:
        warnings.simplefilter('always')
        tqdm_pandas(tqdm)  # should give Warning

        with tqdm(total=10) as t:
            pandas.DataFrame({'x': range(10)}).groupby('x').progress_apply(lambda _: t.update())

        assert len(ws) == 1
        assert issubclass(ws[0].category, TqdmDeprecationWarning)
        assert "instead of `tqdm_pandas(tqdm, ...)`" in str(ws[0].message)


# Setup pandas module-wide integration

# Generated at 2022-06-14 13:08:16.532671
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Test tqdm_pandas functionality with dummy DataFrame.
    """
    import pandas
    import numpy
    import time
    import gc
    numpy.random.seed(1)
    df = pandas.DataFrame(numpy.random.random((10, 10)))

    # Testing case 1: without tqdm
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=TqdmDeprecationWarning)
        start_time = time.time()
        assert 61 == df.progress_apply(lambda x: time.sleep(1) or 61).sum().sum()
        assert time.time() - start_time >= 10
    gc.collect()

    # Testing case 2: tqdm wrapper

# Generated at 2022-06-14 13:08:27.588903
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pkg_resources
    numpy_version = pkg_resources.get_distribution("numpy").version
    pandas_version = pkg_resources.get_distribution("pandas").version

    from tqdm.auto import tqdm
    import tqdm.pandas
    import pandas

    print("Numpy version:", numpy_version)
    print("Pandas version:", pandas_version)

    # Series
    print("Series:")
    s = pandas.Series(range(20))
    t1 = tqdm(s)
    t2 = tqdm(s, leave=False)
    s.progress_apply(lambda x: x * 2)
    assert t1.n == 20 and t1.last_print_n == 20

# Generated at 2022-06-14 13:08:38.880882
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm_notebook

    def test_fn(*args):
        """This function will be used as a parameter of `progress_apply`"""
        for _ in tqdm_notebook(range(10)):
            pass
        return args

    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    res = df.groupby('A').progress_apply(test_fn)
    assert (res == df).all().all()
    res = df.groupby('A').progress_apply(test_fn, args=(3, ('a', 'b')))
    assert (res == (df, 3, ('a', 'b'))).all().all()

# Generated at 2022-06-14 13:08:46.837929
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame(np.random.normal(size=(100, 100)))

    tqdm_pandas(tqdm, file=tqdm.tqdm_file_descriptor())
    df.apply(lambda x: np.mean(x))

    # Tqdm should work with magic methods.
    tqdm_pandas(tqdm, file=tqdm.tqdm_file_descriptor())
    df.apply(lambda x: np.mean(x))

    # Disable Tqdm pandas
    tqdm._dynamic_decorators.clear()
    for magic in ('apply', 'agg', 'transform', 'groupby'):
        assert tqdm._d

# Generated at 2022-06-14 13:08:56.876875
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    df = pd.DataFrame({'x': np.linspace(0, 1, 10)})

    def f(x):
        return pd.Series({'y': np.sum(x)})

    import tqdm
    t = tqdm.tqdm(total=1)
    try:
        tqdm.pandas(t, desc="Testing tqdm_pandas")
        df.groupby('x').progress_apply(f).mean()
    finally:
        t.close()
    _ = delattr(tqdm, 'pandas')  # for debugging
    tqdm_pandas(t, desc="Testing tqdm_pandas")

# Generated at 2022-06-14 13:09:08.891025
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    try:
        import pandas as pd
        df = pd.DataFrame({'x': [1, 2, 3]})
        # noinspection PyUnresolvedReferences
        df.groupby('x').progress_apply(lambda x: x**2)
    except ImportError:
        sys.stderr.write('Test TestPandas skipped due to missing pandas\n')
        import pandas as pd

# Generated at 2022-06-14 13:09:42.694959
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        df = pandas.DataFrame({'a': [0, 1, 2]})
        df.groupby('a').progress_apply(lambda x: x)
    except ImportError:
        # pandas not installed: can't test pandas stuff
        pass
    except NotImplementedError:
        # pandas<0.16.2: needs __iter__ patch
        pass

# Generated at 2022-06-14 13:09:51.434327
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Function requires pandas
    import pandas as pd
    from io import StringIO
    from tqdm import tqdm

    # Generate a pandas data frame
    data = {'a': [1, 2], 'b': [3, 4]}
    df = pd.DataFrame(data)

    # Generate some output from tqdm
    with StringIO() as buf, tqdm(**{'file': buf, 'disable': True}) as t:
        df.groupby('a').progress_apply(lambda x: x)
    assert buf.getvalue() != ''

    class TestTqdm():
        def __init__(self):
            pass
        def postfix(self, *a):
            return
        def __getattr__(self, x):
            return lambda *args: None


# Generated at 2022-06-14 13:09:57.911869
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import trange, TqdmDeprecationWarning
    tclass = trange(2, desc='my tqdm class')
    tqdm_pandas(tclass, ascii=False)
    tqdm_pandas(tclass, ascii=True)
    tqdm_pandas(tclass)

# Default pandas_apply method

# Generated at 2022-06-14 13:10:01.786310
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame

    DataFrame({'col': [1, 2, 3]}).groupby('col').progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:05.320315
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np

        a = pd.DataFrame(np.random.random((10, 1)))
        tqdm_pandas(tqdm(a))
    except Exception as e:
        return False
    return True

# Generated at 2022-06-14 13:10:18.376028
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    try:
        from tqdm import tqdm
    except ImportError:
        return  # Ignore on Pypy
    oldlen = len(set(dir(pd.DataFrameGroupBy)))
    try:
        from tqdm import tqdm_pandas
        tqdm_pandas(tqdm)
    except Exception as e:
        print(e)
        return
    assert len(set(dir(pd.DataFrameGroupBy))) > oldlen
    df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
    df.groupby('A').progress_apply(lambda x: x)

# Generated at 2022-06-14 13:10:30.648932
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from tqdm import tqdm
    except:
        # If you don't have tqdm installed, unit test for tqdm_pandas would fail.
        tqdm = None
        pass

    class MyTqdm(tqdm):
        @classmethod
        def pandas(cls, *args, **kwargs):
            assert kwargs.get('total', None) == 1234
            assert kwargs.get('leave', None) is False
            assert kwargs.get('miniters', None) == 1

            assert not hasattr(cls, 'instance')
            cls.instance = cls(*args, **kwargs)


# Generated at 2022-06-14 13:10:33.939722
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Normal case
    try:
        import pandas as pd
        tqdm_pandas(pd)
    except:
        pass
    # Delayed case
    try:
        tqdm_pandas(tqdm_pandas)
    except:
        pass

# Generated at 2022-06-14 13:10:42.533872
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    import pandas as pd
    import numpy as np
    from tqdm import tqdm, tqdm_pandas

    def test_func(df):
        return (df - df.mean()).sum()

    df = pd.DataFrame(np.random.random((1000, 2)))
    test = df.groupby(0).progress_apply(test_func)  # noqa
    assert isinstance(test, pd.DataFrame)
    assert test.shape == (1000, 2)
    assert test.iloc[0, 0] == test.iloc[0, 1]
    got_exception = False

# Generated at 2022-06-14 13:10:52.414460
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from .std import tqdm
    import numpy as np
    import pandas as pd
    from .utils import format_dict

    df = pd.DataFrame({"A": np.random.normal(1, 1, (100000)),
                       "B": np.random.randint(10, size=(100000))})

    assert not hasattr(df.groupby('B'), 'progress_apply')

    tqdm_pandas(tqdm)
    assert hasattr(df.groupby('B'), 'progress_apply')

    res = df.groupby('B').progress_apply(lambda x: x.sum())
    assert len(str(res)) > 0


# Generated at 2022-06-14 13:11:32.467704
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    df = pd.DataFrame({'a': range(50), 'b': range(50)})

    def test_method(x):
        return x * x

    df['a2'] = [test_method(i) for i in tqdm_pandas(df['a'])]
    df['a2'] = [test_method(i) for i in tqdm_pandas(df['a'], leave=False)]
    df['a2'] = [test_method(i) for i in tqdm_pandas(df['a'], leave=False, smoothing=1)]
    df['a2'] = df.progress_apply(test_method, axis=1)

# Generated at 2022-06-14 13:11:39.357370
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_pandas
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.arange(1000))
    tqdm_pandas(tqdm)
    df.groupby(0).progress_apply(lambda x: x)


# Alias
tqdm_pandas = tqdm_deprecated(tqdm_pandas)

