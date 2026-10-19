

# Generated at 2022-06-14 13:01:51.461487
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    for tclass in [tqdm, tqdm.tqdm]:
        df = DataFrame(
            {'a': [1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6], 'b': [5, 5, 6, 5, 5, 5, 6, 5, 5, 5, 6, 5]})
        out = df.groupby('a').progress_apply(sum)
        assert (out == df.groupby('a').apply(sum)).all(), 'BUG FOUND!'

# Generated at 2022-06-14 13:01:58.572158
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    import types

    # Check tqdm case
    assert isinstance(tqdm_pandas(tqdm), types.FunctionType)

    # Check tqdm(...) case
    with tqdm(total=5) as pbar0:
        assert isinstance(tqdm_pandas(pbar0), tqdm)

    # Check tqdm.pandas(...) case
    with tqdm.pandas(total=5) as pbar1:
        assert isinstance(tqdm_pandas(pbar1), tqdm)

    # Check tqdm.pandas(tqdm, ...) case

# Generated at 2022-06-14 13:02:05.810241
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Example of how to use tqdm_pandas:."""
    import pandas as pd

    df = pd.DataFrame(dict(i=[1, 2, 3], b=[True, True, False]))
    t = tqdm.tqdm_pandas(df.groupby('b').progress_apply(lambda x: x))
    t.get_lock()
    t.close()



# Generated at 2022-06-14 13:02:14.041346
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.contrib import DummyTqdmFile

    # Simple test for tqdm
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [3, 2, 1]})
    with DummyTqdmFile() as f:
        tqdm_pandas(tclass=f)
        df.groupby('a').progress_apply(lambda x: x.sum())
    assert f.n == len(df)
    tqdm_kwargs = dict(smoothing=0, mininterval=0.1, miniters=1)
    with DummyTqdmFile(**tqdm_kwargs) as f:
        tqdm_pandas(tclass=f, **tqdm_kwargs)
       

# Generated at 2022-06-14 13:02:20.339818
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    try:
        import tqdm
    except:
        return
    tqdm_pandas(tqdm.tqdm)

    def func(df):
        return df['x'].sum()

    df = pd.DataFrame({'x': np.arange(100000)})

    res = df.groupby(len).progress_apply(func)
    assert res.sum() == 4999950000


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:28.401233
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    x = pd.DataFrame({'x': [1, 2, 3, 4] * 100,
                      'y': [3, 2, 5, 1] * 100})
    tqdm_pandas(tqdm())
    result = x.groupby('y').progress_apply(lambda x: x)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (400, 2)



# Generated at 2022-06-14 13:02:37.473601
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from pandas import Series
    from pandas import Timestamp
    from pandas import date_range
    from pandas import to_datetime
    import pandas
    import pyarrow
    import s3fs

    if tqdm.__name__.startswith('tqdm_'):
        # Test deprecated tqdm API
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm, mininterval=0.1, maxinterval=0.2)
        tqdm_pandas(tqdm, desc='desc', ascii=True)

# Generated at 2022-06-14 13:02:46.718077
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas

    # Create sample dataframe
    nb_rows, nb_cols = 3, 4
    df_sample = pandas.DataFrame({"col" + str(i): [i + j for j in range(nb_rows)]
                                  for i in range(nb_cols)})
    # Unit test #1
    try:
        tqdm_pandas(tqdm.tqdm())
        df_sample.groupby('col0').progress_apply(lambda x: x['col0'].sum())
    except AttributeError:
        pass
    # Unit test #2

# Generated at 2022-06-14 13:02:57.473582
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm._tqdm_pandas import _deprecated_TProgressBar_pandas, _deprecated_DataFrameGroupBy_progress_apply

    range_ = 5
    try:
        from pandas import DataFrame, Series
    except ImportError:
        return  # skip test

    # Check that tqdm_pandas() works as an adapter
    with tqdm(total=range_) as t:
        assert tqdm_pandas(t, total=range_) is None
        t.update(1)
        assert t.n == 1

    # Check that DataFrameGroupBy.progress_apply() is working
    df = DataFrame({'a': list(range(range_))})
    result = df.groupby('a').progress_apply(lambda x: x + 1)
    assert type

# Generated at 2022-06-14 13:03:04.525749
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.autonotebook import tqdm
    tqdm_pandas(tqdm)
    dataframe = pd.DataFrame(np.random.randint(0, 100, size=(100000, 4)), columns=list('ABCD'))
    dataframe.groupby(['A', 'B']).progress_apply(lambda x: x)
    dataframe.groupby(['A', 'B']).progress_apply(lambda x: x.sum())


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:13.810909
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import math
    import numpy as np

    # Dataframe
    N = 100
    df = pd.DataFrame({'x': np.random.randn(N), 'y': np.random.randn(N),
                       'z': np.random.randn(N)})

    def mymean(df):
        return df.x.mean(), df.y.mean(), df.z.mean()

    def myshuffle(df):
        df = df.copy()
        return df.iloc[np.random.permutation(len(df))].reset_index(drop=True)

    df2 = df.groupby('x').progress_apply(myshuffle).groupby('y').progress_apply(myshuffle).groupby('z').progress_apply(myshuffle)
   

# Generated at 2022-06-14 13:03:23.940002
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    N = 1000000
    df = pd.DataFrame({'A': np.random.randn(N)})
    df2 = pd.DataFrame({'A': np.random.randn(N)})

    tqdm_pandas(tqdm(total=N))

    def apply_fn(x):
        return x.abs()

    df.groupby('A').progress_apply(apply_fn)
    df2.groupby('A').progress_apply(apply_fn)

# Generated at 2022-06-14 13:03:32.511464
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    # Test case 1: tqdm_pandas(tqdm.pandas(**tqdm_kwargs))
    test_df = pd.DataFrame(
        {'a': np.arange(0, 100, 1), 'b': np.arange(100, 200, 1)},
        dtype=float)
    test_df.groupby('a').progress_apply(lambda x: x)

    # Test case 2: tqdm_pandas(tqdm(...), **tqdm_kwargs)

# Generated at 2022-06-14 13:03:40.371415
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return
    # tqdm usage with pandas
    p = pandas.DataFrame(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]).groupby(0).progress_apply(
        lambda x: x)
    assert len(p) == 3
    p = pandas.DataFrame(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]).groupby(0).progress_apply(
        lambda x: x, meta=('x', int))
    assert isinstance(p['x'][0], int)
    assert len(p['x']) == 3

# Generated at 2022-06-14 13:03:51.292277
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm)
    with tqdm_pandas(tqdm) as t:
        df = DataFrame({
            'A': range(1000),
            'B': [str(i) for i in range(1000)]
        })
        df.groupby('B').progress_apply(lambda x: x)
        t.write("Hello Pandas!")

    with tqdm_pandas(tqdm()) as t:
        df = DataFrame({
            'A': range(1000),
            'B': [str(i) for i in range(1000)]
        })
        df.groupby('B').progress_apply(lambda x: x)
        t.write("Hello Pandas!")

# Generated at 2022-06-14 13:03:59.061436
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({'a': np.random.randn(1000), 'b': np.random.randn(1000)})
    df.iloc[:, [1]] = df.progress_apply(pd.Series.cumsum, axis=1)
    # iterate over DataFrames using tqdm
    for _df in tqdm_pandas(pd.read_csv('data.csv', chunksize=100)):
        # do some work per DataFrame
        pass



# Generated at 2022-06-14 13:04:06.287737
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        from nose.plugins.skip import SkipTest
        raise SkipTest("pandas is not installed.")

    from .gui import tqdm
    from .utils import FormatCustomTextExt

    test_df = pd.DataFrame([[1, 1], [2, 2], [4, 2], [1, 2]],
                           columns=['a', 'b'])
    test_df.groupby('b').progress_apply(lambda x: x**2)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:11.578386
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy import random

    df = DataFrame({'x': random.sample(range(100), 10)})
    for i in tqdm_pandas(range(10)):
        df.groupby('x').progress_apply(lambda x: i)

# Generated at 2022-06-14 13:04:15.958832
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from tqdm.std import tqdm
    kwargs = {
        'total': 10,
        'desc': 'tqdm_pandas'
    }
    t = tqdm(**kwargs)
    tqdm_pandas(t)
    t.close()

# Generated at 2022-06-14 13:04:24.533960
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas."""
    from tqdm.deprecated import tqdm_pandas
    from tqdm.auto import tqdm

    tqdm_pandas(tqdm(), leave=True)
    tqdm_pandas(tqdm(leave=True), leave=True)


if __name__ == '__main__':
    from tqdm.auto import tqdm

    test_tqdm_pandas()

    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm(leave=True))

# Generated at 2022-06-14 13:04:38.725645
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd

    df = pd.DataFrame({'a': [1, 2, 3],
                       'b': [4, 5, 6],
                       'c': [7, 8, 9]})

    # Test an instance
    with tqdm(total=len(df), leave=False) as old_pbar:
        def tqdm_apply(x):
            old_pbar.update()
            return x

        df.progress_apply(tqdm_apply)

    # Test a delayed instance
    tqdm.pandas(leave=False)
    df.progress_apply(lambda x: x)

    print('\nTest passed successfully.')

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:45.840483
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        warnings.warn('Test tqdm_pandas requires pandas', TqdmExperimentalWarning)
        return
    tqdm_pandas(tqdm_notebook)
    from tqdm.pandas import tqdm_pandas
    tqdm_pandas(tqdm_notebook)
    tqdm_pandas(tqdm_notebook())
    T = tqdm_notebook.__class__
    tqdm_pandas(T)
    tqdm_pandas(T())
    tqdm_pandas(deprecated_t=tqdm_notebook)
    # tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:04:50.110192
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    tqdm_pandas(tqdm, leave=False)(df.groupby('a').progress_apply)(lambda x: x)

# Generated at 2022-06-14 13:05:01.163391
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time

    df = pd.DataFrame({'a': np.arange(100), 'b': np.arange(100)})

    def func(x):
        time.sleep(0.1)
        return pd.Series(dict(x_sum=x['a'].sum(), x_mean=x['a'].mean(), y_mean=x['b'].mean()))

    tqdm_pandas(tqdm(total=df.shape[0]))  # progress bar for pandas with tqdm

    df.groupby('a').progress_apply(func)
    df.groupby('a').progress_apply(func)

# Generated at 2022-06-14 13:05:12.053057
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """ Simple test for the default tqdm_pandas """
    import pandas as pd
    from tqdm import tqdm

    # Create a DataFrame
    df = pd.DataFrame({"A": ["spam", "eggs", "ham"], "B": [1, 2, 3]})
    df.set_index('A')

    # Create a progress bar
    with tqdm(total=len(df.groupby('A'))) as pbar:
        # Call the method
        df.groupby('A').progress_apply(lambda x: pbar.update())


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:21.758172
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import trange
    tqdm_pandas(trange(1, ncols=1), ncols=4)
    # test "delayed adapter case"
    tqdm_pandas(trange(1))

    df = DataFrame({'A': [1, 2, 3]})
    df.groupby('A').progress_apply(lambda x: x)
    tqdm.pandas()
    df.groupby('A').progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:30.943204
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm_pandas

    tqdm_pandas(tqdm, desc='my bar', unit='my unit')
    tqdm_pandas(tqdm(desc='my bar', unit='my unit'))

    from tqdm import tqdm
    df = pd.DataFrame({'a': np.random.randn(100000)})
    for _ in tqdm(df.groupby('a').progress_apply(lambda x: x * 2),
                  desc='my bar', unit='my unit'):
        pass

    try:
        tqdm_pandas(tqdm)
    except DeprecationWarning:
        pass

# Generated at 2022-06-14 13:05:36.577902
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Test tqdm_pandas
    from tqdm.contrib import pandas
    from pandas import DataFrame
    from tqdm import tqdm

    tqdm_pandas(pandas)

    d = DataFrame({'a': [1, 1, 2, 3, 4, 4]})
    d.groupby('a').progress_apply(lambda x: list(x))

    tqdm_pandas(tqdm())
    d.groupby('a').progress_apply(lambda x: list(x))

# Generated at 2022-06-14 13:05:48.309584
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas

    # Test with tqdm
    try:
        import tqdm
        tqdm_pandas(tqdm)
        df = pandas.DataFrame({'a': range(10)})
        df.groupby('a').progress_apply(lambda x: x)
    except ImportError:
        pass

    # Test with tqdm_notebook
    try:
        from tqdm import tqdm_notebook
        tqdm_pandas(tqdm_notebook)
        df = pandas.DataFrame({'a': range(10)})
        df.groupby('a').progress_apply(lambda x: x)
    except ImportError:
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:56.284030
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        pd.DataFrame([]).groupby(0).progress_apply(lambda x: None)
    except ImportError:
        raise SkipTest
    except RuntimeError as e:
        if "tqdm_pandas is not installed" in str(e):
            pass
        else:
            raise e


if __name__ == '__main__':
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    import pandas as pd
    df = pd.DataFrame({'a': range(5), 'b': range(5, 10)})
    for key, grp in tqdm(df.groupby('a')):
        pass

# Generated at 2022-06-14 13:06:12.647881
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm import tqdm_pandas as tqdm_pandas_

    def test_apply(df):
        tqdm_pandas_(tqdm)
        return df.progress_apply(lambda x: x, axis=1)

    def test_applymap(df):
        tqdm_pandas_(tqdm)
        return df.progress_applymap(lambda x: x)

    def test_map(df):
        tqdm_pandas_(tqdm)
        return df.progress_map(lambda x: x)

    def assert_identity(test, test_func, identity_func, df):
        identity_df = identity_func(df)

# Generated at 2022-06-14 13:06:20.697962
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        tqdm_pandas(get_tqdm())
    except Exception:
        raise
    try:
        tqdm_pandas(get_tqdm(__name__='tqdm_pandas'))
    except Exception:
        raise


# For backwards compatibility
tqdm_gui = deprecated(tqdm_gui,
                      '`tqdm.tqdm_gui` has been deprecated and will be'
                      'removed in version 4.0.0\nPlease use `tqdm_gui(...)`'
                      'instead of `tqdm.tqdm_gui(...)`')

# For backwards compatibility
if sys.version_info[0] == 3:
    import io

# Generated at 2022-06-14 13:06:32.200894
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Test 1
    if __name__ == "__main__":
        import pandas as pd

        df = pd.DataFrame([[0, 1], [1, 2], [2, 3], [3, 4]], columns=list('AB'))
        gr = df.groupby('A', sort=False)
        list(tqdm_pandas(gr, desc='foo'))

    # Test 2
    if __name__ == "__main__":
        import pandas as pd

        df = pd.DataFrame([[0, 1], [1, 2], [2, 3], [3, 4]], columns=list('AB'))
        gr = df.groupby('A', sort=False)

        assert list(tqdm_pandas(gr, desc='foo')) == list(gr)

# Generated at 2022-06-14 13:06:43.169058
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with tqdm.tests.noclean():
        try:
            import pandas as pd
        except ImportError:
            return  # pandas not found: nothing to test

        with tqdm.tests.mock_tqdm() as mock_class:
            tqdm_pandas(mock_class)
            assert mock_class.set_postfix.called
            assert mock_class.set_description.called
        with tqdm.tests.mock_tqdm() as mock_instance:
            tqdm_pandas(mock_instance)
            assert mock_instance.set_postfix.called
            assert mock_instance.set_description.called

        # Check delayed adapter case
        with tqdm.tests.mock_tqdm() as mock_adapter:
            tqdm

# Generated at 2022-06-14 13:06:54.840679
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for tqdm_pandas
    """
    from tqdm.autonotebook import tqdm
    from pandas import DataFrame
    from random import random

    df = DataFrame({"a": [random() for _ in range(100)]})
    t = tqdm(total=len(df), unit='row')
    try:
        # Register tqdm with pandas
        tqdm_pandas(t)
    except TypeError:
        pass
    else:
        raise ValueError("tqdm_pandas without parameters should fail")

    t = tqdm(total=len(df), unit='row', desc='t_1')

# Generated at 2022-06-14 13:07:03.228444
# Unit test for function tqdm_pandas
def test_tqdm_pandas():  # pragma: no cover
    from tqdm import tqdm
    from tqdm._tqdm import TqdmTypeError

    def test_ok(tqdm_class):
        try:
            tqdm_pandas(tqdm_class)
            return True
        except TqdmTypeError:
            return False

    assert test_ok(tqdm)
    assert test_ok(tqdm.tqdm)
    assert test_ok(tqdm.tqdm_notebook)
    assert test_ok(tqdm.tqdm_pandas)
    assert test_ok(tqdm.tqdm_gui)
    assert test_ok(tqdm.trange)
    assert test_ok(tqdm.tnrange)


# Generated at 2022-06-14 13:07:08.464151
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    
    df = pd.DataFrame({"A": [1, 2, 3, 4]})
    df.groupby('A').progress_apply(lambda x: x**2)
    
    df.groupby('A').progress_apply(lambda x: x**2, tclass=tqdm)
    df.groupby('A').progress_apply(lambda x: x**2, tclass=tqdm())
    df.groupby('A').progress_apply(lambda x: x**2, tqdm=tqdm)
    df.groupby('A').progress_apply(lambda x: x**2, tqdm=tqdm())
    
    tqdm.pandas(tqdm)

# Generated at 2022-06-14 13:07:15.407529
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.randn(1000000, 4),
                      columns=list('ABCD'))

    # Testing two instantiations of tqdm
    tqdm_pandas(tqdm_pandas(tqdm(total=len(df), desc='Testing')))
    df.groupby('A').progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:24.926133
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, pandas, tqdm_pandas
    import pandas as pd
    import numpy as np

    # Unit test
    test_df = pd.DataFrame({"col1": [1, 2, 3, 4, 5],
                            "col2": ['a', 'b', 'c', 'd', 'e']})
    tqdm_pandas(tqdm(tclass=pandas, **tqdm.__dict__))
    test_df.groupby('col1').progress_apply(np.sqrt)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:33.647473
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy.random import random
    from tqdm import tqdm
    from tqdm import tqdm_gui
    from tqdm import trange
    from tqdm import tnrange
    # Testing pandas integration
    df = DataFrame(random((100, 100)))
    # Test normal usage
    assert tqdm_pandas(df.groupby(0).progress_apply(lambda x: x * 2)) is not None
    # Test automatic iteration
    assert tqdm_pandas(tnrange(100, desc='pandas loops'),
                       miniters=1, smoothing=0) is not None
    assert tqdm_pandas(trange(100, desc='pandas loops'),
                       miniters=1, smoothing=0) is not None

# Generated at 2022-06-14 13:07:49.556470
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm._utils import _term_move_up
    from tqdm import tqdm, tnrange
    try:
        from pandas import DataFrame
    except ImportError:  # pragma: no cover
        return

    _range = range

    # Test normal usage (with progress bar)
    df = DataFrame([_range(0, 10), _range(100, 110)])
    out = df.groupby(0).progress_apply(len)
    assert out.equals(df.groupby(0).apply(len))

    # Test instantiation of new `tqdm` instance
    old_values = list(df.aggregate(len))
    tqdm_pandas(tqdm)
    out = df.progress_apply(len)
    assert list(out) == old_values

   

# Generated at 2022-06-14 13:08:00.827322
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    import sys

    # Test basic case
    with tqdm(total=10) as t:
        r = DataFrame({'a': [1, 2, 3, 4, 5], 'b': [2, 3, 4, 5, 6]}).apply(
            lambda r: r['a'] + r['b'], axis=1, result_type='expand')
        assert list(r) == [3, 5, 7, 9, 11]
        t.update()

    # Test proxy integration

# Generated at 2022-06-14 13:08:07.393477
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Tests function:
        - tqdm_pandas
    """
    from tqdm import tqdm, trange, TqdmTypeError
    try:
        import numpy as np
        import pandas as pd
    except ImportError:
        tqdm_pandas(tqdm)  # tqdm is a dummy arg
        return

    df = pd.DataFrame({'a': np.random.randint(0, 10000, (10000, 2))})

# Generated at 2022-06-14 13:08:16.247711
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                                  'Parrot', 'Parrot'],
                       'Max Speed': [380., 370., 24., 26.]},
                       columns=['Animal', 'Max Speed'])
    # updates=10 is required for unit test to pass
    for _ in tqdm.tqdm_pandas(tqdm.tqdm(range(10)), desc='Test'):
        df.groupby('Animal').apply(lambda df: df['Max Speed'] * 1.5)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:25.166553
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from .std import tqdm

    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B': [2, 3, 4, 5, 6, 7, 8, 9, 10]
    })

    def inc(x):
        return x + 1

    tqdm_pandas(tqdm)
    df['C'] = df.progress_apply(inc)
    assert (df['C'] - df['A'] == 1).all()
    del df
    tqdm.close()

# Generated at 2022-06-14 13:08:36.388445
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas import DataFrame
    total = 20
    data = {'col1': pd.Series(range(total)), 'col2': pd.Series(range(total))}
    df2 = DataFrame(data)

    # If tqdm is installed, check that the function works
    # without any error (we can't check more than that)
    with suppress(ImportError):
        from tqdm import tqdm
        from tqdm.utils import _range
        from tqdm import TqdmDeprecationWarning

        # Monkeypatch the tqdm "decorator"

# Generated at 2022-06-14 13:08:45.096090
# Unit test for function tqdm_pandas
def test_tqdm_pandas():

    import pandas as pd
    import numpy as np
    import time

    # Create a pandas dataframe
    df = pd.DataFrame({"A": ["A", "B", "C", "A", "C", "A"],
                       "B": ["A", "B", "A", "C", "A", "C"],
                       "C": [1, 2, 3, 1, 2, 1]})

    expected_result = {
        'A': np.array([1, 2, 3, 1, 2, 1], dtype='int64'),
        'B': np.array([2, 1, 2, 1, 2, 1], dtype='int64')}

    def func(df):
        time.sleep(0.01)
        return df.shape[0], df['C'].sum()


# Generated at 2022-06-14 13:08:51.270749
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    import pandas as pd

    def my_test():
        return pd.DataFrame({'a': [1, 2, 3]})
    tqdm_pandas(tqdm())
    df = my_test().progress_apply(lambda r: pd.Series([1, 2, 3]), axis=1)
    assert len(df) == 3

# Generated at 2022-06-14 13:09:00.003438
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """ Unit test for function tqdm_pandas()
        1. Checks for deprecation warnings
        2. Checks for correct function call
    """

    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame({'A': np.random.randint(0, 100, (100)),
                       'B': np.random.randint(0, 100, (100)),
                       'C': np.random.randint(0, 100, (100))})

    def testfunc(a, b, c):
        return a * b * c

    # checking for deprecation
    t = tqdm(total=4)
    tqdm_pandas(t)

    # checking for correct function call
    t = tqdm(total=4)

# Generated at 2022-06-14 13:09:11.132657
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm = tqdm_pandas(tqdm,
                       tqdm_kwargs={'total': 100, 'desc': 'Progress:'})
    df = pd.DataFrame({
        'a': [1, 2, 3, 4, 5],
        'b': [6, 7, 8, 9, 10]
    })

    print(df.groupby('a').progress_apply(
        lambda x: x['b'].values[0]))
    assert (df.groupby('a').progress_apply(lambda x:
                                           x['b'].values[0]).tolist() == [6, 7, 8, 9, 10])

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:22.472984
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm(total=0))

# Generated at 2022-06-14 13:09:27.092801
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    tqdm_pandas(tqdm())

    df = pd.DataFrame({"x": [1, 2, 3]})
    df = df.groupby("x").progress_apply(lambda x: x)
    df.index = df.index.droplevel(0)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:38.537270
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import pandas as pd
    import pandas.util.testing as pdt
    import numpy as np
    from tqdm import tqdm, trange
    from pandas import read_csv
    from tqdm import tqdm_notebook
    from tqdm import tnrange
    from pandas import DataFrame
    from pandas import Series
    from pandas import Panel
    from numpy import array
    from pandas_util import tqdm_pandas

    tclass = tqdm(total=100)

    tqdm_pandas(tclass)


# Generated at 2022-06-14 13:09:40.616199
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm)



# Generated at 2022-06-14 13:09:44.048703
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import numpy as np
    import tqdm

    N = 1000000
    tclass = tqdm.tqdm(total=N)
    df = pandas.DataFrame(np.random.random((N, 3)))
    df.groupby(0).progress_apply(lambda x: x)

# Generated at 2022-06-14 13:09:53.626662
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:10:02.042999
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    import tqdm

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    # Register instance
    tqdm_pandas(tqdm.tqdm(df))
    # Run tqdm with progress_apply
    df.groupby(0).progress_apply(time.sleep)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:08.870647
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm import TqdmDeprecationWarning

    # Function tests
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("error")

        try:
            tqdm_pandas(tqdm)
        except TqdmDeprecationWarning:
            pass
        except Exception as e:
            raise e

        try:
            tqdm_pandas(tclass=tqdm)
        except TqdmDeprecationWarning:
            pass
        except Exception as e:
            raise e

        try:
            tqdm_pandas(tqdm_notebook)
        except TqdmDeprecationWarning:
            pass
        except Exception as e:
            raise e


# Generated at 2022-06-14 13:10:18.116603
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    import numpy as np
    from io import StringIO
    rows = 100
    columns = 10
    df = pd.DataFrame(np.random.rand(rows, columns))
    tqdm.pandas(desc='Progress: ')
    expected_out = StringIO()
    tqdm.pandas(desc='Progress: ', file=expected_out)
    df.progress_apply(print)
    df.progress_apply(print)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:30.411269
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    # import tqdm.contrib.concurrent as tqdm_cc

    df = pd.DataFrame(['foo', 'moo', 'bar'], columns=['A'])
    pbar = tqdm.tqdm(desc='my bar', total=len(df))
    # pbar = tqdm_cc.tqdm(desc='my bar', total=len(df))
    result = df.progress_apply(lambda x: x, axis=1,
                               args=tuple([pbar]))
    pbar.close()
    assert isinstance(result, pd.DataFrame), \
        'progress_apply does not return a DataFrame'

# Generated at 2022-06-14 13:10:48.846471
# Unit test for function tqdm_pandas
def test_tqdm_pandas():  # pragma: no cover
    import pandas as pd
    import numpy as np
    from tqdm.contrib import pandas as tqdm_pd
    try:
        import pandas.core.groupby  # noqa
    except ImportError:
        raise unittest.SkipTest("pandas not installed")
    tqdm_pandas(tqdm_pd)
    N = 100
    df = pd.DataFrame({'A': np.random.randint(
        0, N, size=N), 'B': np.random.randint(0, N, size=N)})
    df = df.groupby('A')
    tqdm_pd.tqdm_pandas(df.apply(lambda x: x))
    tqdm_pd.tqdm_pand

# Generated at 2022-06-14 13:10:53.201416
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    pd.core.groupby.DataFrameGroupBy.progress_apply = tqdm.pandas

    df = pd.DataFrame({'A': 'a b c d e'.split(), 'B': list(range(5))})
    for _ in df.groupby('A').progress_apply(pd.DataFrame.describe):
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:59.082411
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm_notebook)
    except (Exception, SystemExit):
        raise
    else:
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm_notebook)

# Generated at 2022-06-14 13:11:08.087470
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas import Series
    from tqdm import tqdm
    from numpy import concatenate
    from numpy import nan
    from numpy import random
    from numpy import ones

    assert tqdm is not None

    def random_int_series():
        return Series(random.randint(0, 10, size=100))

    def random_float_series():
        return Series(random.uniform(0, 10, size=100))

    def random_nan_series():
        return Series(concatenate((random.uniform(0, 10, size=100), [nan])))

    def random_int_dataframe():
        return DataFrame(
            random.randint(0, 10, size=(100, random.randint(1, 10))))


# Generated at 2022-06-14 13:11:18.263140
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, trange, TqdmDeprecationWarning

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmDeprecationWarning)
        tclass = tqdm(total=10)
        tqdm_pandas(tclass)
        df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]})
        df.groupby("a").progress_apply(lambda x: x)
        with tqdm(total=10) as t:
            tqdm_pandas(t)
            df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]})
           

# Generated at 2022-06-14 13:11:27.542100
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd  # NOQA
    except ImportError:
        return  # no pandas installed, so nothing to test
    df = pd.DataFrame({
        'A': [1, 2, 1, 2, 1],
        'B': [1, 1, 2, 2, 1],
        'C': ['foo', 'bar', 'baz', 'qux', 'foo'],
    })
    from tqdm import tqdm
    df = df.groupby('A').progress_apply(
        lambda x: tqdm_pandas(tqdm(total=len(x))) or len(x.C.unique()))


# ----- Main pandas API -----



# Generated at 2022-06-14 13:11:34.614999
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Import pandas here so that we can use this module without pandas
    import pandas as pd
    from tqdm import tqdm

    # Test function's output data type
    df = pd.DataFrame({'a': [1, 2, 3]})
    result = tqdm_pandas(tqdm, df.groupby('a').progress_apply(lambda i: i))
    assert isinstance(result, pd.core.groupby.DataFrameGroupBy)
    assert result.equals(df.groupby('a'))

# Generated at 2022-06-14 13:11:43.753980
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy.random import choice
    from io import StringIO
    from tqdm import tqdm

    usernames = DataFrame([
        'usenet' + str(i) for i in range(42)
    ], columns=['username'])
    users = DataFrame({
        'posts': choice(range(1, 110), 42),
        'username': usernames['username'],
    })
    tqdm.pandas(desc="tqdm_pandas: " + 'map')
    usernames['username_len'] = usernames['username'].map(
        lambda username: len(username),
        meta=('username', 'int')
    )
    tqdm.pandas(desc="tqdm_pandas: " + 'apply')