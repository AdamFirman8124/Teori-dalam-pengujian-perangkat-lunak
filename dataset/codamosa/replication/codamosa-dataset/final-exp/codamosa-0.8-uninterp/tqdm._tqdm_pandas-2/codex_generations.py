

# Generated at 2022-06-14 13:01:54.732664
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd


# Generated at 2022-06-14 13:02:01.944082
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    import tqdm.pandas

    # Pandas DataFrames / Series
    tqdm_pandas(tqdm())
    pd.DataFrame(np.random.randint(0, 100, (10000, 26))) \
        .progress_apply(lambda x: x**2)
    pd.Series(np.random.randint(0, 100, 10000)) \
        .progress_apply(lambda x: x**2)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:09.704760
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    def _test(test_class):
        try:
            from pandas import DataFrame
            from tqdm import tqdm
        except ImportError:
            return
        from pandas.core.groupby import DataFrameGroupBy

        def progress_apply(obj, func, *args, **kwds):  # <- function to be wrapped
            func.pandas_groupby = obj
            if getattr(obj, '_desc_set', False):
                if 'desc' not in kwds:
                    kwds['desc'] = obj.desc
            if getattr(obj, '_leave_char_set', False):
                if 'leave' not in kwds:
                    kwds['leave'] = obj.leave

# Generated at 2022-06-14 13:02:11.660432
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)


# Generated at 2022-06-14 13:02:20.560963
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm.auto import tqdm

    # Create a DataFrame
    df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 10]}, index=['I1', 'I2', 'I3', 'I4', 'I5'])

    # Create a function to multiply the value by 10
    def mult(x):
        return 10 * x;

    # We are going to apply the function to the column 'a'
    df.groupby('a').progress_apply(mult)

    # We can also apply it to the column 'b'
    df.groupby('b').progress_apply(mult)

    # Or even to both of them

# Generated at 2022-06-14 13:02:25.950262
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm

    tqdm_pandas(tqdm, total=10)
    tqdm_pandas(tqdm, total=10)
    tqdm_pandas(tqdm.tqdm, total=10)
    tqdm_pandas(tqdm.tqdm, total=10)

# Generated at 2022-06-14 13:02:32.079247
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy.random import randint

    def fn(df, val):
        for _ in range(100):
            df += val
        return df

    df = DataFrame(randint(0, 100, (100000, 6)))
    tqdm_pandas(df.groupby(0).progress_apply(fn, 1), total=len(df.groupby(0)))

# Generated at 2022-06-14 13:02:42.476543
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from pandas import Series, DataFrame
    from math import sqrt
    from tqdm import tqdm

    df = pd.DataFrame({'data': [3, 2, 1, 0, -1, -2, -3]})

    def f(x):
        return x.sum() + sqrt(x.sum())

    df.groupby(pd.qcut(df.data, 3)).progress_apply(f)

    df = pd.DataFrame({'data': [3, 2, 1, 0, -1, -2, -3]})
    df['group'] = pd.qcut(df.data, 3)

    def f(x):
        return x.sum() + sqrt(x.sum())


# Generated at 2022-06-14 13:02:47.544399
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        pass  # Skip unit test if pandas not installed
    else:
        df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        # with tqdm(total=len(df), unit='row') as t:
        for row in df.progress_apply(lambda x: x, axis=1):
            pass

# Generated at 2022-06-14 13:02:59.559961
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    assert df.groupby('a').progress_apply(lambda x: x) == df
    try:
        df.groupby('a').progress_apply(lambda x: x, tqdm=tqdm)
    except AttributeError:
        pass
    df.groupby('a').progress_apply(lambda x: x) == df
    tqdm_pandas(tqdm())
    df.groupby('a').progress_apply(lambda x: x) == df
    tqdm_pandas(tqdm, desc='foo')
    df.groupby('a').progress_apply(lambda x: x)

# Generated at 2022-06-14 13:03:10.970705
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm.contrib.tests import _range
    from pandas.util.testing import assert_frame_equal

    df = pd.DataFrame([_range(20)])
    df_expected = pd.DataFrame([_range(20, 40)])
    tqdm_pandas(tqdm, desc="Loading")
    df = df.progress_apply(lambda x: x + 20, axis=1)
    assert_frame_equal(df, df_expected)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:24.198358
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.contrib import pandas
    n = 1000000
    df = pd.DataFrame({
        'x': np.random.exponential(size=n),
        'y': np.random.normal(size=n),
        'z': np.random.choice(range(1000), size=n),
    })

    def progress_apply_test(df):
        df.progress_apply(tqdm_pandas, lambda x: x)

    def groupby_progress_apply_test(df):
        df.groupby('z').progress_apply(tqdm_pandas, lambda x: x)

    def progress_map_test(df):
        df.progress_map(tqdm_pandas, lambda x: x)

# Generated at 2022-06-14 13:03:32.671117
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas as old_tqdm_pandas
    from pandas import DataFrame, Series


# Generated at 2022-06-14 13:03:41.645952
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import numpy
    import sys
    from tqdm._utils import _aux_test_decorator

    def df_test_1(df, *_, **__):
        return df * 2

    def df_test_2(df, *_, **__):
        return df[df > 0]

    def df_test_3(df, *_, **__):
        return df.sum()

    # random data
    df = pandas.DataFrame(numpy.random.rand(100000, 8))

    # Apply with tqdm
    tqdm_pandas(tdf_1, df=df)
    tqdm_pandas(tdf_2, df=df)
    tqdm_pandas(tdf_3, df=df)

    # Apply

# Generated at 2022-06-14 13:03:48.114312
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    tqdm_pandas(tqdm)

    # Create sample dataframe
    df = pd.DataFrame({'col1':[1,2,3], 'col2':[3,6,9]})

    # Run with tqdm
    df.groupby('col1').progress_apply(lambda x: sum(x))

# Generated at 2022-06-14 13:03:57.171166
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import itertools as it

    def test_tqdm_factory(tp_args, tp_kwargs, tp_func, tp_desc):
        """
        Unit tests for the tqdm_pandas factory function.
        """
        try:
            import pandas as pd
            import numpy as np
            import itertools as it
        except ImportError as e:
            sys.stderr.write("Error: Required module not found: {}\n".format(e))
            sys.exit(1)

        def tqdm_factory(*args, **kwargs):
            kwargs.setdefault('desc', tp_desc)
            t = tqdm(*args, **kwargs)
            t.n = 0
           

# Generated at 2022-06-14 13:04:05.542180
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from tqdm.auto import tqdm

    df = DataFrame(Series(range(10)))

    # tests if it actually works
    assert df.groupby(0).progress_apply(lambda _: _).equals(df)

    # If a warning is emitted, the next line raises an Exception
    with warnings.catch_warnings():
        warnings.simplefilter("error", TqdmDeprecationWarning)
        tqdm_pandas(tqdm)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:14.055091
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Checks if the deprecated tqdm_pandas does what it should"""
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    n_rows = 100
    df = pd.DataFrame({'A': np.arange(n_rows)})
    tqdm_pandas(tqdm, leave=False)(lambda x: x, df.groupby('A'))
    tqdm_pandas(tqdm(leave=False))(lambda x: x, df.groupby('A'))



# Generated at 2022-06-14 13:04:19.144583
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    pbar = tqdm.tqdm(total=100)
    tqdm_pandas(pbar, unit='better')
    pd.DataFrame([1, 1, 1]).groupby(0).progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:24.170203
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time

    df = pd.DataFrame(np.random.randint(0, 10, (100000, 6)))
    tqdm_pandas(tclass=tqdm, total=len(df))
    df.progress_apply(time.sleep)

# Generated at 2022-06-14 13:04:38.184539
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    import tqdm

    df = pd.DataFrame(np.random.rand(10**5, 10))

    def func(x):
        time.sleep(0.01)
        return x

    _ = df.groupby(df.columns.tolist(), axis=1).progress_apply(func)
    _ = df.groupby(df.columns.tolist(), axis=1).progress_apply(func, t=tqdm.tqdm)
    _ = df.groupby(df.columns.tolist(), axis=1).progress_apply(func, t=tqdm.tqdm_notebook)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:45.288851
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    try:
        from tqdm.autonotebook import tqdm
        tqdm_pandas(tqdm, leave=True)
        pd.Series(range(1000000)).progress_apply(lambda x: x)
    except Exception as e:
        raise e

    try:
        from tqdm.auto import tqdm
        tqdm_pandas(tqdm, leave=True)
        pd.Series(range(1000000)).progress_apply(lambda x: x)
    except Exception as e:
        raise e

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:55.508614
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    # tqdm_pandas(tqdm)
    tqdm_pandas(tqdm, total=10)
    # tqdm_pandas(tqdm.tqdm)
    tqdm_pandas(tqdm.tqdm, total=10)
    # tqdm_pandas(tqdm(total=10))
    tqdm_pandas(tqdm(total=10))
    # tqdm_pandas(tqdm.tqdm(total=10))
    tqdm_pandas(tqdm.tqdm(total=10))



# Generated at 2022-06-14 13:05:05.068271
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy import random
    from tqdm import tqdm

    random.seed(0)

    df = DataFrame({'int': random.randint(0, 100, 20),
                    'float': random.randn(20),
                    'str': ["Test"]*20})

    print("df.groupby('int').progress_apply(len)\n",
          df.groupby('int').progress_apply(len))
    print("\ndf.groupby('str').progress_apply(len)\n",
          df.groupby('str').progress_apply(len))

    tqdm_pandas(tqdm(ncols=90))


# Generated at 2022-06-14 13:05:17.907145
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:05:27.570439
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    df = pd.DataFrame({
        'A': [0, 1, 2],
        'B': [3, 4, 5],
    })

    def my_func(x):
        return x['A'] + x['B']

    def my_func_delay(x):
        import time
        time.sleep(1)
        return x['A'] + x['B']

    with tqdm_pandas(df.groupby('A').progress_apply) as g:
        assert g(my_func).equals(df.groupby('A').apply(my_func))

# Generated at 2022-06-14 13:05:33.676587
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    try:
        import pandas.testing
    except ImportError:
        return
    from tqdm.pandas import tqdm_pandas
    tqdm_pandas(tclass="tqdm_notebook")
    pd.DataFrame([1, 2, 3]).groupby(0).progress_apply(lambda x: x)
    # Test tqdm_pandas(tqdm)
    tqdm_pandas(tclass=tqdm(total=100), leave=False)
    pd.DataFrame([1, 2, 3]).groupby(0).progress_apply(lambda x: x)


# Register pandas progress bar to tqdm
tqdm_pandas(tclass="tqdm_notebook")


# Generated at 2022-06-14 13:05:39.554891
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    tqdm.pandas()
    tqdm_pandas(tqdm)

    df = DataFrame({"a": [1, 2, 3]})
    df.groupby("a").progress_apply(lambda x: x)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:50.906432
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_notebook
    from pandas import DataFrame
    from random import random
    from .utils import format_sizeof, silence_tqdm_deprecation_warning

    # Shut up TqdmDeprecationWarning (verbose only)
    with silence_tqdm_deprecation_warning():
        # Test for tqdm (manual adapter)
        if hasattr(tqdm, '_instances_pandas'):
            tqdm._instances_pandas = set()  # cleanup
        df = DataFrame({"x": [random() for _ in range(10*1000)]})

# Generated at 2022-06-14 13:05:55.046529
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # This unit test is only for coverage.
    from tqdm.auto import tqdm
    tqdm_pandas(tqdm, desc='', total=2)
    tqdm_pandas(tqdm(desc='', total=2))

# Generated at 2022-06-14 13:06:11.397410
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    from .utils import FormatCustom


# Generated at 2022-06-14 13:06:19.770852
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        pytest.skip("pandas not installed")
    try:
        from tqdm import tqdm
    except ImportError:
        pytest.skip("tqdm not installed")
    try:
        from scipy import sparse
    except ImportError:
        pytest.skip("scipy.sparse not installed")

    df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [5, 6, 7, 8]})

    def convert(x):
        from scipy import sparse
        return sparse.csc_matrix(x)

    # function
    with tqdm(total=len(df)) as t:
        tqdm_pandas(t, leave=False)
        df

# Generated at 2022-06-14 13:06:31.449274
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import random
    import string

    random_state = random.getstate()

    df = pd.DataFrame(
        {'a': 2, 'b': list(map(string.ascii_letters.index,
                               string.ascii_letters)), 'c': list(range(52))})
    tqdm_pandas(tqdm)
    assert df.progress_apply(lambda x: x) is not None

    df.progress_apply(lambda x: x)
    random.setstate(random_state)
    df.progress_apply(lambda x: x)
    for i in range(len(df)):
        assert df.iloc[i].all() == df.progress_apply(lambda x: x).iloc[i].all()
    assert df.progress

# Generated at 2022-06-14 13:06:37.000703
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
        df.groupby(0).progress_apply(lambda x: x**2)
    except ImportError:
        pass
    else:
        raise Exception('Pandas is installed. To avoid this error, run `test_tqdm(optional_args=["--disable-pandas"])`')


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:47.869736
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    try:
        from tqdm.auto import tqdm
    except ImportError:
        from tqdm import tqdm

    if sys.version_info > (3,):
        from io import StringIO as stringio
    else:
        from io import BytesIO as stringio

    from pandas.core.groupby import DataFrameGroupBy

    df = pd.DataFrame([(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (2, 3)], columns=['a', 'b'])
    df = df.groupby('a')
    DataFrameGroupBy.progress_apply = tqdm_pandas(df.progress_apply)
    DataFrameGroupBy.progress_apply(df, lambda x: None)
    s

# Generated at 2022-06-14 13:06:55.008098
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_gui().pandas()
    tqdm_gui().pandas(leave=False)
    tqdm_pandas(tqdm_gui())
    tqdm_pandas(tqdm_gui(), leave=False)
    tqdm_pandas(tqdm_gui, leave=False)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:03.351919
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm import trange
    from time import sleep

    pd.set_option('chained_assignment', None)

    def make_df():
        df = pd.DataFrame()
        for _ in trange(5):
            a = list(np.random.randint(0, 5, 10))
            b = list(np.random.randint(0, 5, 10))
            c = list(np.random.randint(0, 5, 10))
            d = list(np.random.randint(0, 5, 10))

# Generated at 2022-06-14 13:07:15.647886
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    if sys.version_info >= (3, 0):
        from tqdm import tqdm
    else:
        from tqdm import tqdm3 as tqdm
    from pandas import DataFrame
    from pandas import Series
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm(total=6))
    s = Series(range(2)).progress_apply(lambda x: x + 1)
    assert (s == Series(range(1, 3))).all()
    df = DataFrame({'a': [1, 2, 3], 'b': [1, 1, 1]})
    df2 = df.progress_apply(sum, axis=1)
    assert (df2 == Series([2, 3, 4])).all()

# Generated at 2022-06-14 13:07:26.737810
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.auto import tqdm
    from tqdm.auto import trange
    from itertools import product

    with tqdm(total=100) as t:
        t.update(5)
        assert t.n == 5
        t.update(10)
        assert t.n == 15

    with trange(10) as t:
        assert len(t) == 10
        t.set_description("description")
        assert t.desc == "description"
        t.set_description_str("description2")
        assert t.desc == "description2"
        t.set_postfix(OrderedDict(x=1))
        assert t.postfix == OrderedDict([('x', 1)])
        assert t.format_

# Generated at 2022-06-14 13:07:34.798949
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    with tqdm_pandas(tqdm(total=100)) as pbar:
        pd.DataFrame([5]).progress_apply(lambda x: pbar.update())

    with tqdm_pandas(tqdm(total=100), leave=False) as pbar:
        pd.DataFrame([5]).progress_apply(lambda x: pbar.update())

    with tqdm_pandas(tqdm(total=100, position=0)) as pbar:
        pd.DataFrame([5]).progress_apply(lambda x: pbar.update())

    with tqdm_pandas(tqdm_notebook(total=100, unit='B')) as pbar:
        pd.DataFrame([5]).progress

# Generated at 2022-06-14 13:07:46.194449
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import Series
    from tqdm import tqdm
    from tqdm.tests.test_tqdm import Fake_tqdm

    assert tqdm_pandas(tqdm)

    T = Fake_tqdm.pandas(total=10)
    for i in T(Series(range(10))):
        pass
    assert T._num_iter == 10, T._num_iter
    assert T._total_size == 10, T._total_size

# Generated at 2022-06-14 13:07:55.948714
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import numpy
    numpy.random.seed(0)
    import pandas.util.testing as ptest

    try:
        import tqdm
    except ImportError:
        try:
            import cvxpy
        except ImportError:
            return True

        from cvxpy.reductions.dpp.utilities.progress_bar import tqdm
    try:
        from pandas import DataFrame
    except ImportError:
        try:
            import cvxpy
        except ImportError:
            return True

        from cvxpy.reductions.dpp.utilities.progress_bar import DataFrame

    df = tqdm.pandas(DataFrame(numpy.random.randint(0, 100, (100000, 6))))

    # We run progress_apply with a lambda

# Generated at 2022-06-14 13:08:04.639999
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm
    from tqdm import trange

    tqdm_pandas(tqdm, desc='my-pandas')
    assert hasattr(pd.core.groupby.DataFrameGroupBy, 'progress_apply')

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)),
                      columns=list('ABCDEF'))
    tqdm_pandas(tqdm, desc='my-pandas')
    try:
        df.groupby('A').progress_apply(lambda x: x['B'].sum())
    except Exception as e:
        raise e

    tqdm_pandas(trange, desc='my-pandas')

# Generated at 2022-06-14 13:08:09.401197
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    tqdm.pandas(desc="test")

if __name__ == '__main__':
    from multiprocessing import Pool
    p = Pool(5)
    p.map(test_tqdm_pandas, range(5))

# Generated at 2022-06-14 13:08:13.017063
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    T = tqdm_pandas(tclass=tqdm, total=100)
    for i in range(100):
        T.update()


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:15.820462
# Unit test for function tqdm_pandas
def test_tqdm_pandas():

    from tqdm import tqdm

    tqdm_pandas(tqdm)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:26.871957
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas
    import numpy

    def func_dummy(df):
        return numpy.sum(df)

    # tqdm is using by default `sys.stdout`
    nrows, ncolumns = 3, 3
    df = pandas.DataFrame(numpy.random.rand(nrows, ncolumns))
    fp_stdout = sys.stdout
    # redirect stdout in a dummy file
    sys.stdout = open(os.devnull, 'w')
    df.groupby(lambda i: i % 3).progress_apply(func_dummy)  # with tqdm
    sys.stdout = fp_stdout
    df.groupby(lambda i: i % 3).progress_apply(func_dummy)  # without tqdm

# Generated at 2022-06-14 13:08:38.189952
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm.auto import tqdm
    from numpy.random import randint

    try:
        from pandas.core.groupby import DataFrameGroupBy
        from pandas.core.groupby import SeriesGroupBy
    except ImportError:
        from pandas.core.groupby import DataFrameGroupBy
        from pandas.core.groupby import SeriesGroupBy

    def func(df, i):
        time.sleep(0.01)
        return i

    df = DataFrame({'a': randint(0, 100, (1000,)),
                    'b': randint(0, 100, (1000,))})

    tqdm_pandas(tqdm)
    r0 = df.groupby('a').progress_apply(func, i=1)
    tqdm

# Generated at 2022-06-14 13:08:46.357515
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas."""
    import pandas as pd

    def func(df):
        return len(df)

    df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['a', 'b'])
    grouped = df.groupby(df['a'] % 2)
    try:
        grouped.progress_apply(func)
    except NotImplementedError:
        print('No tqdm_pandas detected, skipping unit test #1.')
    else:
        assert 0, "Should fail without tqdm_pandas()."
    finally:
        # Test delayed adapter
        tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:08:50.761185
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    sys.modules['pandas'] = type('mock_pandas', (object,), {})()
    sys.modules['pandas.core'] = type('mock_pandas_core', (object,), {})()
    sys.modules['pandas.core.groupby'] = type('mock_pandas_core_groupby', (
        object,), {})()
    sys.modules['pandas.core.groupby.DataFrameGroupBy'] = type(
        'mock_pandas_core_groupby_DataFrameGroupBy',
        (object,), {})()


# Generated at 2022-06-14 13:09:08.642079
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        tqdm_pandas(tqdm)
        assert 'Please use `tqdm.pandas(...)` instead of ' \
               '`tqdm_pandas(tqdm, ...)`.' in str(w[0].message)
        tqdm_pandas(tqdm(total=123))
        assert 'Please use `tqdm.pandas(...)` instead of ' \
               '`tqdm_pandas(tqdm(...))`.' in str(w[1].message)

# Generated at 2022-06-14 13:09:14.837870
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.auto import tqdm
    from pandas import DataFrame
    try:
        import pandas as pd
        df = DataFrame(pd.np.random.randint(0, 100, size=(100000, 6)))
        total = len(df)
        with tqdm(total=total) as pbar:
            df.progress_apply(lambda x: pbar.update())
    except (ImportError, AttributeError):
        pass
    assert True


if __name__ == "__main__":
    test_tqdm_pandas()
    print("All tests passed")

# Generated at 2022-06-14 13:09:17.362110
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    exit(0)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:27.543045
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Test nested unit
    """
    import pandas as pd
    df = pd.DataFrame({'animal': list('abababab'),
                       'num_legs': [2, 4, 4, 2, 2, 4, 4, 2]})
    from tqdm import tqdm
    from collections import defaultdict
    from time import sleep

    # Inject pandas `progress_apply`
    def inject_tqdm_progress_apply(df, bar_format=None):
        if bar_format is None:
            bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
        tqdm.pandas(desc='apply-progress', bar_format=bar_format)
        return df

    #

# Generated at 2022-06-14 13:09:37.664695
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas  # noqa
    import numpy

    def test_func(df):
        assert isinstance(df, pandas.DataFrame)
        return df

    n = 1e6
    df = pandas.DataFrame(numpy.random.randn(int(2 * n), n),
                          columns=[str(i) for i in range(int(n))])
    tqdm_pandas(tqdm(total=int(1e5)), disable=True).progress_apply(test_func,
                                                                  axis=1,
                                                                  args=(df,))


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:46.749583
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from pandas import DataFrame
    except ImportError:
        return

    from tqdm import tqdm
    from .main import TqdmTypeError

    df = DataFrame({'a': list(range(10))})
    with pytest.raises(TqdmTypeError):
        df.groupby('a').progress_apply(tqdm, lambda x: x)

    tqdm_pandas(tqdm)
    df.groupby('a').progress_apply(tqdm, lambda x: x)

    tqdm_pandas(tqdm, unit_scale=True)
    df.groupby('a').progress_apply(tqdm, lambda x: x)

    tqdm_pandas(tqdm())
    df.groupby('a').progress_apply

# Generated at 2022-06-14 13:09:50.072270
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test for tqdm_pandas function"""
    tqdm_pandas(tqdm)


if __name__ == '__main__':
    test_tqdm_pandas()

###############################################################################
## END
###############################################################################

# Generated at 2022-06-14 13:10:02.178131
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    from tqdm import tqdm, tqdm_notebook
    from pandas import DataFrame
    from numpy import random
    import pandas.core.groupby as pg
    import unittest

    # Dummy function for testing
    def _simple_sum(x):
        return sum(x)

    # Create a dummy dataframe
    df = DataFrame(random.randn(100, 4), columns=list('ABCD'))

    # Create a dummy function for testing
    def func(df, ch=False):
        if ch:
            return df.groupby('A').progress_apply(_simple_sum)
        return df.groupby('A').apply(_simple_sum)

    # Create a test case

# Generated at 2022-06-14 13:10:09.629410
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    import tqdm
    try:
        import pandas_flavor as pf
    except ImportError:
        print('pandas_flavor not available.')
        return

    # Much larger times are needed on Windows...
    N = 1000
    TIME = 0.05
    
    df = pd.DataFrame({'A': [1, np.nan, 3, 2, 4, 2, 3, 1],
                       'B': [1, 1, 2, np.nan, 2, 2, 1, 2],
                       'C': [2, 1, np.nan, 1, 1, 2, 1, 2]})
    
    # Test for tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:10:19.549137
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from pandas.util.testing import assert_frame_equal
    from tqdm import tqdm, tqdm_pandas
    tqdm.pandas = tqdm_pandas
    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)), columns=list('ABCDEF'))
    # Test on Series
    res = df['A'].progress_apply(lambda x: x**2)
    exp = df['A'] ** 2
    assert_frame_equal(res, exp)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:41.327279
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    df = pd.DataFrame({"col1": [1, 2, 3, 4],
                       "col2": [2, 3, 4, 5],
                       "col3": [3, 4, 5, 6]})
    tqdm_pandas(df.groupby("col1").progress_apply(lambda x: x["col2"].sum()))


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:45.453535
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm._utils_tests import f1, f2

    f1(tqdm_pandas)
    f2(tqdm_pandas)


test_tqdm_pandas()
del test_tqdm_pandas

# Generated at 2022-06-14 13:10:56.257468
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    def f(x):
        import time
        time.sleep(0.01)
        return x

    df = pd.DataFrame({'x': list(range(10))})
    df.groupby('x').progress_apply(f)  # test unregistered progress_apply
    print('#' * 16 + ' test unregistered progress_apply ' + '#' * 16 + '\n')

    t = tqdm.tqdm_pandas(tqdm.tqdm)
    df.groupby('x').progress_apply(f)  # test registered progress_apply
    print('#' * 16 + ' test registered progress_apply ' + '#' * 16 + '\n')


# Generated at 2022-06-14 13:11:04.077023
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Checks if tqdm_pandas returns pandas DataFrame"""
    try:
        import pandas as pd
    except ImportError:
        return

    df = pd.DataFrame(data={'b': [0, 1, 2, 5]})
    with tqdm_pandas(total=len(df)) as pbar:
        assert (pd.DataFrame(data={'a': [0, 1, 2, 3]}) ==
                df.progress_apply(lambda x: x + 1, axis=1))
    assert len(pbar) == len(df)
    pbar.reset()
    assert len(pbar) == 0


# Generated at 2022-06-14 13:11:10.628244
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tnrange, tqdm_pandas
    from numpy import random as rd

    df = DataFrame({'a': rd.randint(0, 100, size=100)})
    tqdm_pandas(tnrange)  # same as `tqdm_pandas(tqdm.tnrange)`
    df.groupby('a').progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:11:20.156430
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5, 6],
        'B': [2, 3, 4, 5, 6, 7],
        'C': [3, 4, 5, 6, 7, 8],
        'D': [4, 5, 6, 7, 8, 9],
        'E': [5, 6, 7, 8, 9, 10],
        'F': [6, 7, 8, 9, 10, 11],
    })
    from tqdm.auto import tqdm
    from tqdm.contrib import pandas

    total = len(df)
    pbar = tqdm(total=total)


# Generated at 2022-06-14 13:11:30.744730
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        print("Pandas not found, skipping tqdm_pandas test.")
        return

    with closing(StringIO()) as our_file:
        tqdm_pandas(tqdm, file=our_file)
        assert tqdm.pandas.__original_module__ == 'pandas.core.groupby'

        try:
            result = pandas.DataFrame(dict(a=[1, 2])).groupby("a").progress_apply(
                lambda _: _)
        except AttributeError:
            print("Pandas version < 0.18, skipping tqdm_pandas test.")
            return
        assert result == pandas.DataFrame(dict(a=[1, 2]))



# Generated at 2022-06-14 13:11:41.226655
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pytest
        # the following is needed on Python 2.6
        __tracebackhide__ = True
    except ImportError:
        pass
    tqdm_pandas(tqdm(range(2)))
    with pytest.raises(TqdmDeprecationWarning):
        tqdm_pandas(range(2))


# Pandas 0.x support

# Generated at 2022-06-14 13:11:51.539022
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest("pandas not found")

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    result = df.groupby(0).progress_apply(lambda x: x ** 2)
    assert (((result - df ** 2) ** 2).sum().sum() < 0.1)
    result = df.progress_apply(lambda x: x ** 2)
    assert (((result - df ** 2) ** 2).sum().sum() < 0.1)


if __name__ == "__main__":
    from tqdm.autonotebook import tqdm
    tqdm_pandas(tqdm)  # from tqdm import tqdm