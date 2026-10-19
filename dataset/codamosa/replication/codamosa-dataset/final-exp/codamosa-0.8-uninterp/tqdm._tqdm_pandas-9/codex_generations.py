

# Generated at 2022-06-14 13:01:42.020100
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas.core.groupby import GroupBy
    from tqdm import tqdm

    with tqdm(total=10) as pbar:
        DataFrame(dict(col=[1, 2])).groupby("col").progress_apply(
            lambda x: pbar.update())
    with tqdm(total=10) as pbar:
        DataFrame(dict(col=[1, 2])).groupby("col").progress_apply(
            lambda x: pbar.update())

    def assert_raises(exc, fun, *args, **kwargs):
        try:
            fun(*args, **kwargs)
        except exc as e:
            pass
        else:
            raise Exception('Exception was not raised')


# Generated at 2022-06-14 13:01:47.978970
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    df = pd.DataFrame(np.arange(30).reshape(5, 6))
    res = df.groupby(0).progress_apply(lambda x: x)
    assert isinstance(type(res), df._constructor)
    assert res.equals(df)



# Generated at 2022-06-14 13:01:56.510250
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_notebook
    import numpy as np
    N = 100
    df = pd.DataFrame({
        'a': np.random.randint(0, 50, size=N),
        'b': np.random.randint(0, 50, size=N),
        'n': np.random.randint(5, size=N)
    })

    def progress_apply_test(df, f, **kwargs):
        kwargs.setdefault('leave', False)
        f_name = f.__name__
        f_original = df[f_name]
        # TODO: use decorator
        f = tqdm_pandas(tqdm_notebook, **kwargs)(f)

# Generated at 2022-06-14 13:02:06.123812
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function `tqdm_pandas`."""
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame(np.random.random(100000))
    t = tqdm(total=len(df))
    t.__enter__()
    tqdm_pandas(t, file=t.fp._fp)
    sum_ = df.sum()
    t.__exit__()


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:14.302587
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    import sys
    import os
    from tqdm import tqdm

    def f(df):
        return pd.DataFrame({'a': np.arange(len(df))})

    try:
        f(pd.DataFrame({'b': np.arange(10)}))
    except TypeError:
        pass
    else:
        raise RuntimeError("Expected function f() to fail.")

    # Test without tqdm
    df = pd.DataFrame({'b': np.arange(10)})
    try:
        f(df).progress_apply(f, axis=1)
    except AttributeError:
        pass
    else:
        raise RuntimeError("Expected progress_apply() to fail.")

    # Test with

# Generated at 2022-06-14 13:02:20.496584
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm.autonotebook import tqdm
    from time import sleep

    df = pd.DataFrame({"abc": np.random.randint(0, 100, 10000),
                       "def": np.random.random(size=(10000,))})
    df = df.groupby("abc").progress_apply(lambda x: sleep(0.01))
    assert df is not None, "df is None"

    df = pd.DataFrame({"abc": np.random.randint(0, 100, 10000),
                       "def": np.random.random(size=(10000,))})
    df = df.groupby("abc").progress_apply(lambda x: sleep(0.01))
    assert df is not None, "df is None"

# Generated at 2022-06-14 13:02:32.315441
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for `tqdm_pandas`.
    """
    import numpy as np
    import pandas as pd
    from tqdm import tqdm
    from tqdm import tqdm_pandas as tqdm_pd

    df = pd.DataFrame({'x': np.random.randint(0, 100, 1000),
                       'y': np.random.randint(0, 100, 1000)})

    # test for pandas object
    df_prg = tqdm_pd.progress_apply(df, lambda x: x)
    assert (df == df_prg).all().all()

    # test for pandas groupby object
    df_grp = df.groupby('x')

# Generated at 2022-06-14 13:02:39.294470
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas

    df = pandas.DataFrame(
        np.arange(1000).reshape(100, 10), columns=range(10))
    g = df.groupby(0)
    with tqdm(total=len(g)) as t:
        for _, _ in g.progress_apply(lambda x: t.update(1)):
            pass

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:48.044046
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test for tqdm_pandas."""
    try:
        from pandas import DataFrame
    except ImportError:
        return
    from numpy import random
    from pandas import DataFrame
    from pandas import Series
    from tqdm import tqdm
    from tqdm import tqdm_notebook
    from tqdm import tqdm_gui
    import sys
    import warnings

    if sys.version_info.major < 3:
        tqdms = [tqdm]
    else:
        tqdms = [tqdm, tqdm_notebook, tqdm_gui]

    df = DataFrame({
        'a': [1, 2, 3, 4, 5],
        'b': [6, 7, 8, 9, 10],
    })


# Generated at 2022-06-14 13:03:00.333962
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, tqdm_pandas
    import random

    df = pd.DataFrame(data=[[random.random() for i in range(100)] for j in
                            range(100)], columns=['col' + str(i) for i in range(100)])
    df.groupby('col0').progress_apply(lambda x: x)
    tqdm_pandas(tqdm())
    df.groupby('col0').progress_apply(lambda x: x)
    tqdm_pandas(tqdm(leave=False))
    df.groupby('col0').progress_apply(lambda x: x)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:12.637743
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm import trange
    from tqdm.pandas import tqdm_pandas as tqdm_pd
    from pandas import DataFrame

    N = 100
    M = 10
    df = DataFrame(index=range(N), data=[[0] * n for n in range(N)])
    for nactive in range(1, M):
        tqdm_pd(tqdm(total=N))(df.groupby(df.index // nactive).progress_apply)(len)
        tqdm_pd(trange(N))(df.groupby(df.index // nactive).progress_apply)(len)

# Generated at 2022-06-14 13:03:25.940269
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas"""
    try:
        import numpy as np
        import pandas as pd
        from pandas import DataFrame, Series
        from pandas.core.groupby import DataFrameGroupBy
        from tqdm import TqdmDeprecationWarning
    except ImportError:
        pass
    else:
        # fake DataFrame for testing
        df = DataFrame({'value': [1, 2, 3] * 10000,
                        'key': ['odd'] * 3 + ['even'] * 3})
        gb = df.groupby('key', sort=False)

        prev_agp = DataFrameGroupBy.apply
        tqdm_kwargs = dict(total=len(df))

        def test(dfg):
            if isinstance(dfg, Series):
                return dfg

# Generated at 2022-06-14 13:03:33.585870
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from time import sleep

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=TqdmDeprecationWarning)

        # pandas.DataFrame.progress_apply
        for cls in [tqdm_pandas, tqdm]:
            df = pd.DataFrame(np.ones((10_000, 10)))
            cls(total=df.shape[0]).progress_apply(
                lambda x: sleep(0.01), axis=1)
        assert True

        # pandas.DataFrame.groupby.progress_apply
        for cls in [tqdm_pandas, tqdm]:
            df = pd.DataFrame({'A': np.random.choice(range(100), size=10000)})

# Generated at 2022-06-14 13:03:38.166916
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.autonotebook import tqdm
    from .tests_tqdm import pretest_posttest_nopandas  # NOQA
    import numpy
    from pandas import DataFrame

    def tp_test(t):
        with t.disable_global_instance():
            n = 1000
            tqdm_pandas(t, data=DataFrame(
                numpy.random.randn(n, n)))
            tqdm_pandas(t, data=DataFrame(
                numpy.random.randn(n, n)), miniters=1, mininterval=0.01)
            tqdm_pandas(t, data=DataFrame(
                numpy.random.randn(n, n)), smoothing=1, leave=True)
        tqdm

# Generated at 2022-06-14 13:03:50.771657
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, read_csv
    from tqdm import tqdm
    from os import getcwd, chdir, remove
    from io import StringIO
    from datetime import datetime

    # Get current directory
    cwd = getcwd()

    # Prepare directory for test
    test_directory = cwd + '/testing/'
    try:
        chdir(test_directory)
    except FileNotFoundError:
        exit('This test requires the directory ' + test_directory)

    # Prepare a csv file
    csv_file = test_directory + 'test_tqdm_pandas.csv'
    with open(csv_file, 'w') as file:
        file.write('a;b;c;d\n')

# Generated at 2022-06-14 13:04:01.089901
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]})
    df.groupby("a").progress_apply(lambda x: x['b'].sum())
    df.progress_apply(lambda x: x['b'].sum())
    df.apply(lambda x: x['b'].sum())
    tqdm_pandas(tqdm(desc='foo'))
    tqdm_pandas(tqdm(desc='bar'))
    tqdm_pandas(tqdm(desc='baz'))


if __name__ == "__main__":
    test_tq

# Generated at 2022-06-14 13:04:09.438418
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series, concat
    from tqdm import tqdm

    print('Function: tqdm_pandas')

    # Test AttributeError
    try:
        df = DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
        df.groupby(["col1"]).apply(lambda x: print(x))
    except AttributeError as e:
        if "apply" in str(e):
            pass
        else:
            raise e

    # Test normal case
    tqdm_pandas(tqdm(unit=" rows", desc="  Test: tqdm_pandas"))
    df = DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})


# Generated at 2022-06-14 13:04:19.146976
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm_pandas
    from tqdm import tqdm, TqdmDeprecationWarning

    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm)

        assert len(w) == 1
        assert issubclass(w[-1].category, TqdmDeprecationWarning)

    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm(total=100))

        assert len(w) == 1
        assert issubclass(w[-1].category, TqdmDeprecationWarning)

    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas('tqdm')


# Generated at 2022-06-14 13:04:30.489719
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test of tqdm_pandas"""
    import pandas as pd
    import numpy as np
    import time
    import os

    def testfun(df):
        """Testing function"""
        return np.array(df) * 2

    np.random.seed(1)
    N = 100
    df = pd.DataFrame(np.random.rand(N, 3), columns=['a', 'b', 'c'])

    # Setup tqdm_pandas
    tqdm_pandas(tqdm)  # This can also be: tqdm_pandas(tqdm_notebook)
    try:
        pd.options.mode.chained_assignment = None
    except:
        pass

    # Set verbosity

# Generated at 2022-06-14 13:04:37.984956
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    from .utils import tnrange

    df = DataFrame(dict(
        (c, tnrange(30)) for c in 'ABCDEFGHIJKLMNOPQRSTUVWX'))
    for n in tqdm(range(10), ncols=80):
        df.progress_apply(lambda x: [c for c in str(x['A'])])

# Generated at 2022-06-14 13:04:42.310737
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        assert tqdm_pandas
    except ModuleNotFoundError:
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:48.081734
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas.util.testing import assert_frame_equal

    def test_func(df):
        return df + 1

    df = pd.DataFrame({'A': [1] * 10, 'B': [2] * 10, 'C': [2] * 10})
    df_expected = pd.DataFrame({'A': [2] * 10, 'B': [3] * 10, 'C': [3] * 10})
    assert_frame_equal(df_expected, df.progress_apply(test_func))

    result = (df.groupby('A')
              .progress_apply(test_func))
    assert_frame_equal(df_expected, result)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:00.524705
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_notebook as tqdm
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(dict(
        n=np.arange(100),
        c=(np.arange(100) % 10).astype(str),
        x=1,
        y=100,
    ))
    df.groupby('c').progress_apply(lambda x: x.x.sum())
    assert list(df.groupby('c').progress_apply(lambda x: x.x.sum())) == [
        100] * 10

    tqdm_pandas(tqdm)

    # Registering should fail without pandas

# Generated at 2022-06-14 13:05:11.572603
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test TQDM's `pandas()` progress bar."""
    try:
        import pandas as pd
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

        # register the `tqdm_pandas` module to monitor execution of the `sum()` method.
        tqdm_pandas(tqdm(desc='groupby', leave=True))
        df.groupby('a').progress_apply(lambda x: x**2).sum()
        assert True
    except ImportError:
        pass


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:23.280535
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # If pandas is not installed, skip
    try:
        import pandas as pd
    except ImportError:
        return
    
    from tqdm import tqdm, TqdmDeprecationWarning

    # Test correct decorator
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        tqdm_pandas(tqdm)
        assert issubclass(w[-1].category, TqdmDeprecationWarning)
        assert "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`" in str(w[-1].message)
    assert tqdm.pandas

    # Test old decorator

# Generated at 2022-06-14 13:05:29.744820
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        sys.stderr.write("Skipping test_tqdm_pandas: pandas not found.\n")
        return

    g = tqdm_pandas(tqdm())
    s = pd.Series([3] * 10**6)
    g.progress_apply(lambda x: x, axis=1)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:36.003318
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd, numpy as np
    from tqdm import tqdm_pandas

    tqdm_pandas(tqdm)

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    # Test on Series
    df[0].progress_apply(lambda x: x**2)
    # Test on DataFrame
    df.progress_apply(lambda x: x**2)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:48.055532
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas
    from tqdm._tqdm_pandas import tqdm_pandas as _tqdm_pandas
    from pandas import DataFrame, Series
    from numpy import random
    from time import sleep

    tqdm_pandas.__name__ = "tqdm_pandas"
    _tqdm_pandas.__name__ = "_tqdm_pandas"

    print("\nTesting tqdm_pandas.__closure__[0](tclass, **tqdm_kwargs)")
    print("- Testing tqdm_pandas.__closure__[0](tqdm, ...)")

# Generated at 2022-06-14 13:05:56.686305
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm
    try:
        import pandas.core.groupby.groupby  # pylint: disable=unused-import
    except ImportError:
        raise RuntimeError("pandas is required for `tqdm.pandas`")

    test_df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    tqdm_pandas(tqdm.tqdm(leave=False, ascii=True), file=sys.stdout)
    calc = test_df.groupby(0).progress_apply(
        lambda x: pd.Series([x.sum(), x.mean()]))
    assert calc[1].sum() > 0

# Generated at 2022-06-14 13:06:02.298321
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    import tqdm

    try:
        # This line allows two tqdm instances to coexist in the same process
        tqdm._instances.clear()

        t = tqdm.tqdm(total=100)
        t.close()

        t = tqdm.tqdm(total=100)
        t.close()
    except:
        assert False, "Function tqdm_pandas test #1 has failed"

# tqdm_pandas unit test execution
test_tqdm_pandas()

# Generated at 2022-06-14 13:06:14.817777
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    tqdm = tqdm_pandas(tqdm)  # import tqdm as tqdm
    tqdm.pandas()  # register tqdm instance with pandas

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    # Now you can use `progress_apply` instead of `apply`
    df.groupby(0).progress_apply(lambda x: x**2)
    tqdm.pandas(miniters=None)  # disable progress_apply
    # Now you can use `progress_apply` instead of `apply`
    df.groupby(0).progress_apply(lambda x: x**2)



# Generated at 2022-06-14 13:06:21.115691
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        print('No pandas module, cannot test tqdm_pandas')
        return
    t = tqdm(range(10))
    tqdm_pandas(t)
    df = pd.DataFrame({'x': range(10)})
    df.groupby('x').progress_apply(lambda x: x)
    return True

# Generated at 2022-06-14 13:06:32.243597
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, trange
    from tqdm.auto import tqdm as a_tqdm
    import pandas as pd

    # check that progress_apply works for list of lists
    tqdm(pd.DataFrame({'A': [[1, 2, 3], [4, 5, 6]]}).progress_apply(sum))

    # check that progress_apply works with lambda
    tqdm(pd.DataFrame({'A': [[1, 2, 3], [4, 5, 6]]}).progress_apply(lambda x: sum(x)))

    # check that progress_apply works with delayed adapter
    tqdm_pandas(tqdm, total=5)
    tqdm_pandas(trange, total=5)

# Generated at 2022-06-14 13:06:41.479222
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.contrib.tests import unittest
    try:
        import pandas
    except ImportError:
        raise unittest.SkipTest("pandas not found")
    try:
        import numpy
    except ImportError:
        raise unittest.SkipTest("numpy not found")
    df = pandas.DataFrame([range(10000000)], dtype='int64').apply(numpy.sum)
    with tqdm(total=len(df)) as pbar:
        def mysum(x):
            pbar.update()
            return x.sum()
        df.progress_apply(mysum)

# Generated at 2022-06-14 13:06:48.452132
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Test 1
    def test_tqdm_simple():
        with captured_output() as (out, err):
            with tqdm(["a", "b", "c"], file=sys.stdout) as t:
                t.pandas([1, 2, 3])

        output = out.getvalue().strip()
        assert output == """\
  0%|          | 0/3 [00:00<?, ?it/s]
Processing pandas apply...
100%|##########| 3/3 [00:00<00:00,  ?it/s]"""

    test_tqdm_simple()

    # Test 2
    def test_tqdm_cls():
        tclass = tqdm(["a", "b", "c"], file=sys.stdout)


# Generated at 2022-06-14 13:06:55.190537
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.randn(10000,1000))
    tqdm_pandas(tqdm(total=df.shape[0]))
    # Apply progress_apply using tqdm/tqdm_pandas
    df.groupby(0).progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:06:58.462722
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import numpy

    df = pandas.DataFrame(numpy.random.rand(10000, 10000))
    df.progress_apply(lambda x: x)

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:06.220479
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from time import sleep
    from tqdm import tqdm

    # Dummy progress function
    def dummy_progress(x):
        sleep(0.001)
        return x ** 2

    # Test tqdm Pandas
    df = pd.DataFrame(np.random.uniform(size=(100, 100)))
    tqdm_pandas(tqdm, desc='Dummy GroupBy', leave=False, total=len(df) + 1)
    df = df.groupby(0, sort=False).progress_apply(dummy_progress)
    assert len(df) == 100



# Generated at 2022-06-14 13:07:16.692221
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test function for tqdm_pandas
    """
    from pandas import DataFrame
    from tqdm import tqdm

    try:
        import pandas as pd
        import numpy as np

        def squared(x):
            return x ** 2

        np.random.seed(0)
        df = pd.DataFrame(dict(A=np.random.rand(20)))
        df.get_group = lambda x: df
        with tqdm(total=len(df.A)) as t:
            tqdm_pandas(t)
            results = df.groupby('A').progress_apply(squared)
            assert (results.values == df.A.values ** 2).all()
    except ImportError:
        pass

# Generated at 2022-06-14 13:07:26.648133
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    import pandas
    from time import sleep
    from tqdm.contrib import pandas as tqdm_pandas
    tqdm_pandas.pandas()
    df = pandas.DataFrame(
        {'a': [1, 2, 3], 'b': [1., 2., 3.]},
        index=pandas.date_range('2012-01-01', '2012-01-03', freq='D'))
    for _ in df.groupby('a').progress_apply(lambda x: sleep(1)):
        pass

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:34.547135
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    t = tqdm.pandas(**tqdm.__dict__)
    t.tqdm_pandas = staticmethod(tqdm_pandas)  # tqdm.tqdm_pandas
    t.tqdm_pandas(tqdm.tqdm)  # tqdm.tqdm_pandas(tqdm.tqdm)


# Generated at 2022-06-14 13:07:39.626564
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    def progress_apply(df, func, **kwargs):
        self = df.groupby(level=0)
        return self.progress_apply(func, **kwargs)

    from tqdm.auto import tqdm
    from tqdm._tqdm import TqdmExperimentalWarning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
        print(progress_apply(pd.DataFrame([np.random.randn(1000)]), tqdm_pandas, sum, axis=0))

# Generated at 2022-06-14 13:07:51.649773
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    def test(df, tqdm_class=tqdm.tqdm):
        # Test 1
        df.progress_apply(lambda x: x['b'].sum())
        # Test 2
        list(df.progress_apply(lambda x: x['b'].sum()))
        # Test 3
        df.progress_apply(lambda x: x['b'].sum(), axis=1)
        # Test 4
        df['c'] = df.progress_apply(lambda x: x['b'].sum(), axis=1)
        # Test 5
        df['c'] = df.progress_apply(lambda x: x['b'].sum(), axis=1)
        list(df['c'])
        # Test 6

# Generated at 2022-06-14 13:08:00.230102
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    tqdm_pandas(pandas.core.groupby.DataFrameGroupBy.progress_apply)
    tqdm_pandas(pandas.core.groupby.SeriesGroupBy.progress_apply)
    try:
        import dask
        tqdm_pandas(dask.base.ProgressBar, smoothing=0)
        tqdm_pandas(dask.array.progress_map, smoothing=0)
    except ImportError:
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:06.653447
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import pandas

    # Delayed multi-functionality (to avoid set-up again)
    tqdm_pandas(tqdm)

    # Unit tests
    pd = pandas.DataFrame()
    pd['a'] = [2, 4, 6, 8]
    pd['b'] = [5, 10, 15, 20]
    assert pd.groupby('a').progress_apply(lambda x: x).equals(pd)
    assert pd.groupby('a').progress_apply(lambda x: x).equals(pd)
    assert pd.groupby('a').progress_aggregate(lambda x: x).equals(pd)
    assert pd.groupby('a').progress_transform(lambda x: x).equals(pd)

# Generated at 2022-06-14 13:08:16.714410
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:08:24.490109
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm_pandas
    import numpy as np
    # Test for name error
    try:
        tqdm_pandas(tqdm)
    except Exception as e:
        if not isinstance(e, NameError):
            raise ValueError("tqdm_pandas() raised an unexpected exception")


if __name__ == '__main__':
    test_tqdm_pandas()
    print("All tests passed")

# Generated at 2022-06-14 13:08:35.709222
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    class tqdm:
        def __init__(self, iterable, **kwargs):
            pass
        def close(self):
            pass

    class tqdm_:
        pandas = lambda self, t=None, **kwargs: None

    # test tclass as TqdmType
    tqdm_pandas(tqdm, total=50)

    # test tclass as TqdmType instance
    t = tqdm(total=50)
    tqdm_pandas(t)

    # test tclass as deprecated TqdmType
    tqdm_pandas(tqdm_, total=50)

    # test tclass as deprecated TqdmType instance
    t = tqdm_(total=50)
    tqdm_pandas(t)


# Generated at 2022-06-14 13:08:44.591752
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    from tqdm import tqdm_pandas
    from tqdm import tqdm

    df = pd.DataFrame(np.random.randint(0, 10, (100000, 6)))
    if TRAVIS:
        tqdm_pandas(tqdm_pandas)  # to prevent "delayed adapter case" warning
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm(ncols=80))
        with pytest.warns(TqdmDeprecationWarning, match="deprecated_t"):
            tqdm_pandas(tqdm(ncols=80).__enter__())

# Generated at 2022-06-14 13:08:55.255747
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.autonotebook import tqdm

    n = 1000
    df = pd.DataFrame({'x': np.linspace(0, 1, n)})
    tmp = np.zeros(n)

    tcls = tqdm(total=n, file=sys.stdout)
    tqdm_pandas(tcls, leave=False)
    def f(x):
        for i in range(n):
            df[i] = x + i
    df.progress_apply(f)
    tcls.close()

    # with tqdm_pandas(tqdm(total=n, file=sys.stdout), leave=False) as tcls:
    #     def f(x):


# Generated at 2022-06-14 13:09:10.835153
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    try:
        tqdm_pandas(tqdm)
        # tqdm_pandas(tqdm())
    except Exception as e:  # pragma: no cover
        try:  # Check for deprecation warnings
            import warnings
            assert issubclass(e.__class__, warnings.warnings.WarningMessage)
        except Exception:
            raise e
    else:  # pragma: no cover
        print("Error, should have raised deprecation warning")
        assert False


if __name__ == '__main__':
    # Unit test
    test_tqdm_pandas()

    # Example
    if False:
        import pandas as pd
        import numpy as np
        import math
        import pandas as pd

# Generated at 2022-06-14 13:09:23.486089
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # tqdm_pandas(tqdm)
    tqdm_pandas(tqdm)
    with tqdm(total=100) as t:
        assert t.__name__.startswith('tqdm_')
    # tqdm_pandas(tqdm(total=1))
    with tqdm(total=1) as t:
        assert t.__name__.startswith('tqdm_')
        tqdm_pandas(t)
        assert t.__name__.startswith('tqdm_')  # Improves coverage of tqdm.pandas
        t.total = 100  # Improves coverage of tqdm._new_total
    # tqdm_pandas(tqdm, ...)
    tqdm_pand

# Generated at 2022-06-14 13:09:27.722784
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with tqdm_pandas(total=100) as pbar:
        for i in range(10):
            pbar.update()
            time.sleep(0.1)
    time.sleep(3)



# Generated at 2022-06-14 13:09:37.409666
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    # Randomly generate data
    data = np.random.randint(0, 10, size=(10, 5))
    df = DataFrame(data, columns=list('abcde'))

    # Register tqdm
    tqdm_pandas(tqdm())
    df.groupby('a').progress_apply(lambda x: x.b + x.c)
    print('successfully pass tqdm_pandas test!')


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:45.309868
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import warnings
    import tqdm

    try:
        import pandas as pd
    except ImportError:
        return

    with warnings.catch_warnings():
        warnings.simplefilter('error', TqdmDeprecationWarning)

        try:
            tqdm_pandas(tqdm)
        except TqdmDeprecationWarning:
            pass
        else:
            raise AssertionError

        try:
            tqdm_pandas(tqdm.tqdm)
        except TqdmDeprecationWarning:
            pass
        else:
            raise AssertionError

        try:
            tqdm_pandas(tqdm.tqdm())
        except TqdmDeprecationWarning:
            pass
        else:
            raise AssertionError

        tqdm

# Generated at 2022-06-14 13:09:51.644765
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_gui

    test_df = pd.DataFrame({'a': range(10), 'b': range(0, 20, 2)})

    def short_sleep(x):
        from time import sleep
        sleep(0.1)
        return x

    result = test_df.progress_apply(short_sleep)
    print(result)

    # Gui
    result = test_df.progress_apply(short_sleep, t=tqdm_gui)
    print(result)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:03.020442
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        tqdm_pandas(1, total=2, file=sys.stderr)
        assert issubclass(w[-1].category, TqdmDeprecationWarning)

        class TestTqdm:
            name = 'test_tqdm'
            file = sys.stderr
            __name__ = name

        tqdm_pandas(TestTqdm, total=2, file=sys.stderr)
        assert issubclass(w[-1].category, TqdmDeprecationWarning)


if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)

# Generated at 2022-06-14 13:10:06.249653
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        pd.DataFrame.apply
        # tqdm_pandas(tqdm)
    except ImportError:
        pass

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:19.028347
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas  # NOQA
    except ImportError:
        return

    from tqdm.contrib import pandas as tup

    from pandas import Series, DataFrame
    from tqdm import tqdm

    df = DataFrame({'A': Series([1, 2, 3]), 'B': Series([4, 5, 6])})
    for tclass in [tqdm, tqdm_pandas]:
        tclass = tup
        try:
            assert len(df.progress_apply(lambda x: x + 1)) == len(df)
        except TypeError:
            raise TypeError(tclass, 'tup')
        try:
            assert len(df.progress_apply(lambda x: x + 1, axis=1)) == len(df)
        except TypeError:
            raise

# Generated at 2022-06-14 13:10:27.323806
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame

    df = DataFrame(data={'a': range(1000), 'b': range(1000)})

    # Inline usage
    tqdm_pandas(tqdm())
    df.groupby('a').progress_apply(lambda x: x)

    # Delayed usage
    tqdm_pandas(tqdm)
    df.groupby('a').progress_apply(lambda x: x)

# Generated at 2022-06-14 13:10:41.999989
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    for tclass in [tqdm,
                   tqdm(total=1, ascii=True, disable=None),
                   tqdm(total=1, ascii=False, disable=True)]:
        tqdm_pandas(tclass)
        assert hasattr(DataFrame.groupby, 'progress_apply')
        del DataFrame.groupby.progress_apply


if __name__ == '__main__':
    try:
        test_tqdm_pandas()
    except ImportError:
        print("SKIP: pandas is not installed")

# Generated at 2022-06-14 13:10:50.308742
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm_pandas

    df = pd.DataFrame({
        'x': np.random.random(size=(1000, 2)).tolist(),
        'y': np.random.random(size=(1000, 2)).tolist(),
    })

    def f(df):
        return pd.DataFrame({'x': [df.x.sum()], 'y': [df.y.sum()]})

    df.groupby('x').progress_apply(f, tqdm_kwargs={'tclass': tqdm_pandas})


# Generated at 2022-06-14 13:10:57.319240
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    from tqdm import tqdm, trange

    # delayed tqdm
    ##############################
    tqdm_pandas(tqdm)  # noqa
    progbars = []
    for i in trange(10, leave=False):
        progbars.append(pd.DataFrame(np.random.randint(0, 100, (100000, 6)),
                                     columns=list('ABCDEF')).groupby('A')
                                     .progress_apply(len))
    ##############################

    # immediate tqdm
    ##############################
    tqdm_pandas(tqdm(leave=False))  # noqa
    progbars = []

# Generated at 2022-06-14 13:11:06.382130
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.pandas import tqdm_pandas

    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})

    # noinspection PyPep8Naming
    def func(arg):
        return arg + 1
    _ = df.groupby(['a', 'b']).progress_apply(func)

    tqdm_kwargs = {'total': 1,
                   'desc': '|',
                   'bar_format': '{l_bar}{bar}|',
                   'unit': ''}
    tqdm_pandas(tqdm_kwargs)
    _ = df.groupby(['a', 'b']).progress_apply(func)

# Generated at 2022-06-14 13:11:16.891157
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from pandas.util._decorators import Appender
    assert hasattr(DataFrame, '_apply_progress_enabled')
    tqdm_pandas(tqdm)
    assert hasattr(DataFrame, '_apply_progress_enabled')
    assert hasattr(DataFrame, 'progress_apply')
    assert isinstance(DataFrame.progress_apply, Appender)
    tqdm_pandas(tqdm())
    assert hasattr(DataFrame, '_apply_progress_enabled')
    assert hasattr(DataFrame, 'progress_apply')
    assert isinstance(DataFrame.progress_apply, Appender)
    tqdm_pandas(tqdm, leave=False)

# Generated at 2022-06-14 13:11:23.990475
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        raise SkipTest

    t = tqdm(total=100, file=sys.stderr)
    t.pandas()
    tqdm_pandas(t)
    assert getattr(pandas.core.groupby.DataFrameGroupBy, 'progress_apply', None)
    t.close()

    t = tqdm(total=100, file=sys.stderr)
    try:
        tqdm_pandas(tqdm)
    except:
        pass
    else:
        raise Exception("should raise")
    t.close()

    t = tqdm(total=100, file=sys.stderr)

# Generated at 2022-06-14 13:11:31.382356
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame

    data = DataFrame(dict(col1=[1, 2], col2=[3, 4]))
    with tqdm(total=2, dynamic_ncols=True, file=sys.stdout) as pbar:
        def func(df):
            pbar.update()
            return df.col1 + df.col2

        result = data.groupby(["col2"]).progress_apply(func)
    assert result.values.tolist() == [[4], [6]]

# Generated at 2022-06-14 13:11:40.233601
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    # ToDo: find fast way to test this
    from tqdm import tqdm

    X = {'a': range(50), 'b': range(50, 100)}
    X = pd.DataFrame(X)

    result = tqdm_pandas(tqdm)(X)
    assert 0 == result.sum(axis=1)['a']

    # Show that wrap the tqdm function works
    tqdm_pandas(tqdm(total=10))()

if __name__ == '__main__':
    test_tqdm_pandas()