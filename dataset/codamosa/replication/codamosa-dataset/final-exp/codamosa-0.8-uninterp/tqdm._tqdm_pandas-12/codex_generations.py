

# Generated at 2022-06-14 13:01:43.641530
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    def test_f(row):
        for _ in range(10):
            row = row[::-1]
        return row
    df = pd.DataFrame([[i, i] for i in range(10)])
    df.columns = ['foo', 'bar']

    from tqdm import tqdm, pandas
    from tqdm._tqdm import TqdmTypeError
    with pytest.raises(TqdmTypeError):
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm())
        with pandas(tqdm) as pbar:
            pass

# Generated at 2022-06-14 13:01:54.085262
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from numpy import random

    df = pd.DataFrame(random.randn(1000))
    res = df.groupby(0).progress_apply(lambda x: x ** 2)

    # Test with an existing tqdm instance
    res = df.groupby(0).progress_apply(lambda x: x ** 2, tqdm_instance=tqdm())

    # Test with the progress_apply wrapper
    pd.options.display.max_rows = 10
    tqdm_pandas(tqdm)
    res = tqdm(df.groupby(0))
    # pd.options.display.max_rows = 10  # test get_ipython


# Generated at 2022-06-14 13:01:58.522962
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    from tqdm import tqdm

    df = pd.DataFrame(np.random.random(size=(2, 2)))
    tqdm_pandas(tqdm())
    tqdm_kwargs = {'desc': 'test_tqdm_pandas'}
    time.sleep(1)
    df.groupby(0).progress_apply(len, **tqdm_kwargs)

# Generated at 2022-06-14 13:02:06.080929
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    lines = [x for x in range(1000)]

    # noinspection PyDeprecation
    tqdm_pandas(tclass=tqdm)
    df = pd.DataFrame(lines)
    df = df[0]
    # noinspection PyDeprecation
    res = df.progress_apply(lambda x: x * 2)
    assert res[-1] == 1998

# Generated at 2022-06-14 13:02:14.279015
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    import tqdm.pandas
    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    df.groupby(0).progress_apply(lambda x: x**2)
    tqdm.pandas(tqdm())
    df.groupby(0).progress_apply(lambda x: x**2)
    tqdm.pandas(tqdm())
    df.progress_apply(lambda x: x**2)
    with tqdm(total=9) as t0:
        for i in tqdm_pandas(range(3), total=3, file=t0):
            pass
        t0.close()

# Generated at 2022-06-14 13:02:22.138176
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    def mock_tqdm(t, **kwargs):
        class mock_tqdm_class:
            @classmethod
            def pandas(cls, *args, **kwargs):
                return kwargs
        return mock_tqdm_class

    class mock_class:
        def __init__(self):
            self.fp = True
        def __name__(self):
            return 'tqdm_'

    m = mock_class()
    test_case_1 = tqdm_pandas(m, ncols=10)
    test_case_2 = tqdm_pandas(mock_tqdm(m), ncols=10)
    test_case_3 = tqdm_pandas(m)
    test_case_4 = tqdm_pandas

# Generated at 2022-06-14 13:02:29.633906
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    # Create pandas DataFrame
    df = pd.DataFrame({'Integers': list(range(10)),
                       'Floats': np.random.randn(10)**2})

    # Register tqdm instance to pandas
    tqdm_pandas(tqdm)

    # Compute mean over each column
    df.groupby('Integers').progress_apply(np.mean)

# Generated at 2022-06-14 13:02:35.297580
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    assert pd.DataFrame([1, 2, 3, 4]).progress_apply(lambda x: x).equals(
        pd.DataFrame([1, 2, 3, 4]))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:39.422931
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas"""
    try:
        tqdm_pandas(tqdm)
    except TqdmDeprecationWarning:
        pass
    else:
        raise Exception("Unit test failed")

# Generated at 2022-06-14 13:02:49.596269
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas

    df = pandas.DataFrame(dict(
        nums=[1, 2, 3, 4, 5],
        key=list('abcab')))

    import tqdm as deprecated
    deprecated.tqdm_pandas(tqdm=deprecated)
    assert isinstance(df.groupby('key').progress_apply(lambda x: x.sum()), pandas.Series)

    deprecated.tqdm_pandas(deprecated.tqdm())
    assert isinstance(df.groupby('key').progress_apply(lambda x: x.sum()), pandas.Series)

    deprecated.tqdm_pandas(deprecated.tqdm(total=4))

# Generated at 2022-06-14 13:03:02.598312
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, TqdmDeprecationWarning
    from pandas import DataFrame

    class MockTqdm(tqdm):
        class pandas:
            init = False
            @staticmethod
            def __init__(**kwargs):
                MockTqdm.pandas.init = True
                assert not kwargs
        # Recursive hashable class with same name
        class MockTqdm:
            pass
        # Recursive non-hashable class with same name
        tqdm_MockTqdm = MockTqdm


# Generated at 2022-06-14 13:03:12.666266
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from tqdm.auto import tqdm

    # Test tqdm creation
    tqdm.pandas(desc='test')
    tqdm.pandas(leave=False, total=0)  # total width > 0
    tqdm.pandas(leave=True, total=0)  # total width == 0

    # Regression tests

# Generated at 2022-06-14 13:03:25.938887
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from random import randint
    from pandas import DataFrame
    from tqdm.pandas import tqdm_pandas

    # Test DataFrame
    int_list = [randint(1, 9) for i in range(100)]
    str_list = [str(i) for i in int_list]
    df = DataFrame({"int": int_list, "str": str_list})

    # Test progress_apply
    df_to_int = df.progress_apply(lambda x: int(x["str"]) + 1, axis=1)

    # Test unique and value_counts
    df_str_counts = df["str"].progress_apply(lambda x: x + "a").value_counts()

# Generated at 2022-06-14 13:03:29.840845
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np

    df = pd.DataFrame(np.random.uniform(size=(10000, 1000)))
    df.groupby(df.columns.tolist(), sort=False).progress_apply(lambda x: x * 2)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:36.107549
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_pandas
    from pandas import DataFrame

    df = DataFrame({'a': [1, 2]})
    with tqdm(total=df.shape[0]) as pbar:
        df.groupby('a').progress_apply(lambda x: pbar.update())
    df.groupby('a').progress_apply(lambda x: pbar.update())
    for t in [tqdm, tqdm_pandas]:
        with t(total=df.shape[0]) as pbar:
            df.groupby('a').progress_apply(lambda x: pbar.update())

# Generated at 2022-06-14 13:03:49.178981
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from random import random

    with tqdm(total=5) as t:
        tqdm_pandas(t, desc='EPOCH')
        for i in range(5):
            df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4]})
            df.groupby('x').progress_apply(lambda x: x)
            df.groupby('x').progress_apply(lambda x: x ** random())
            t.update()

    with tqdm(total=5) as t:
        tqdm_pandas(tqdm(desc='EPOCH'), desc='EPOCH')

# Generated at 2022-06-14 13:03:59.061068
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Registers the given `tclass` instance with
    `pandas.core.groupby.DataFrameGroupBy.progress_apply`.
    """
    import pandas as pd
    import numpy as np

    # setup
    pd.DataFrame.progress_apply = tqdm_pandas
    try:
        pd.Series.progress_apply = tqdm_pandas
    except AttributeError:
        pass

    # tests
    MAX = 10 ** 6
    s = pd.Series(list(range(MAX)))
    df = pd.DataFrame({'a': s, 'b': s, 'c': s, 'd': s, 'e': s, 'f': s})
    assert df.progress_apply(lambda x: x) is not None
    assert df.progress_apply

# Generated at 2022-06-14 13:04:07.025827
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from numpy.random import randint

    try:
        from tqdm import tqdm
        from tqdm import TqdmDeprecationWarning
        from unittest.mock import patch

        tqdm_pandas(tqdm)

        df = pd.DataFrame({'x': randint(0, 10, (1000,)),
                           'y': randint(0, 10, (1000,))})

        with patch('sys.stderr', new=io.StringIO()) as my_stdout:
            tqdm_pandas(tqdm)
            assert ('Please use `tqdm.pandas(...)` instead' in my_stdout.getvalue())
    except ImportError:
        pass

# Generated at 2022-06-14 13:04:17.090431
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from collections import OrderedDict
    from tqdm._utils import _term_move_up as uu
    from tqdm._tqdm import _range
    pandas = pytest.importorskip('pandas')

    def mysleep(t=0.1):
        with tqdm(total=t) as pbar:
            for i in _range(t):
                pbar.update(i)
                time.sleep(0.1)

    @tqdm_pandas
    def myapply(x):
        time.sleep(0.05)
        return len(x)

    df = pandas.DataFrame({'a': [1],
                           'b': ['foo']})

    mysleep()

# Generated at 2022-06-14 13:04:25.923983
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd


# Generated at 2022-06-14 13:04:39.833673
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    import pandas
    import tqdm

    # Set data for Unit test
    data = [
        1, 2, 3
    ] * 10000000
    # Convert data to a DataFrame
    df = pandas.DataFrame(data)

    # Set groupby column
    groupby_column = 'one'

    # Create a groupby object manually
    groupby = df.groupby(df[df.columns[0] % 3], sort=False, as_index=False)

    # Test deprecated `tqdm.pandas(tclass)` syntax

# Generated at 2022-06-14 13:04:46.343969
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    np.random.seed(0)
    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    df.columns = ['a', 'b', 'c', 'd', 'e', 'f']

    # Register `tqdm` to `DataFrame.progress_apply`
    from tqdm import tqdm
    tqdm_pandas(tqdm)

    # Now you can use `progress_apply` instead of `apply`
    df.groupby(0).progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:04:58.763910
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy.random import randint, randn
    from tqdm import tqdm
    # Create a fake DataFrame for testing
    df = DataFrame({'a': [0, 0, 1, 1], 'b': [2, 2, 3, 3],
                    'c': [4, 4, 5, 5], 'd': [6, 6, 7, 7]})
    # Test whether the progress bar will be displayed
    with tqdm() as t:
        df.groupby('a').apply(
            lambda x: tqdm_pandas(t, leave=False, desc='groupby').progress_apply(
                lambda x: randn(100)))

# Generated at 2022-06-14 13:05:09.234833
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    import numpy as np
    from tqdm import trange

    # Define function to apply
    def my_func(x, y=0):
        c = x + y
        return c

    # Create pandas DataFrame with 1000 random values
    df = pd.DataFrame(np.random.rand(1000, 4), columns=['a', 'b', 'c', 'd'])

    # Apply & test my_func to df['a'] with tqdm
    with trange(10) as t:
        # Create iterator
        it = t.__iter__()

        def wrapper():
            next(it)
            t.update()

        # Test with file-like object

# Generated at 2022-06-14 13:05:21.119580
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    df = pd.DataFrame({"a": 1, "b": 2})
    tqdm_pandas(tqdm(total=len(df)))
    tqdm_pandas(tqdm, total=len(df))


if __name__ == '__main__':
    from tqdm import tqdm
    import pandas as pd
    df = pd.DataFrame({"a": 1, "b": 2})

    # Example 1:
    # tqdm_pandas(tqdm(total=len(df)))
    # df.groupby("a").progress_apply(lambda x: x)

    # Example 2:
    tqdm_pandas(tqdm, total=len(df))

# Generated at 2022-06-14 13:05:27.764011
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame

    N = 100
    a = DataFrame(dict(a=N*[0], b=N*[1], c=N*[2]))

    def f(df):
        return len(df)

    tqdm_pandas(tqdm)
    r = a.groupby('a').progress_apply(f)
    assert r.max() == r.mean() == r.min() == 1.0


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:33.851060
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas.util.testing import assert_frame_equal
    from tqdm import tqdm
    from tqdm.compat import OrderedDict

    def test_func(df):
        return pd.concat([df.groupby('a')['b'].sum(), df.groupby('a')['c'].mean()], axis=1)

    pd.DataFrame({'a': [1, 1, 2, 2, 1, 2],
                  'b': [2, 3, 2, 4, 2, 3],
                  'c': [0, 0, 0, 1, 1, 2]}).groupby('a').progress_apply(test_func)


# Generated at 2022-06-14 13:05:45.860599
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame, Series
    from pandas.util.testing import assert_series_equal

    def f(x):
        return +x

    def f_exc(x):
        raise ValueError()

    def f_exc_tqdm(x):
        try:
            raise ValueError()
        except ValueError:
            tqdm.pandas(tqdm)
            raise

    assert_series_equal(
        DataFrame({'a': [1, 2, 3, 4]}).groupby('a').progress_apply(f),
        DataFrame({'a': [1, 2, 3, 4]}).groupby('a').apply(f))

# Generated at 2022-06-14 13:05:48.244961
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # TODO check it works with a long import chain
    import pandas
    import tqdm
    tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:05:54.552112
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tempfile
    open = tempfile.SpooledTemporaryFile
    tqdm_kwargs = {'unit': 'B', 'unit_scale': True, 'leave': True,
                   'miniters': 1, 'desc': 'my bar', 'file': open(100)}
    with tqdm(**tqdm_kwargs) as t:
        tqdm_pandas(t, **tqdm_kwargs)
        # Test delayed adapter function
        tqdm_pandas(tqdm, **tqdm_kwargs)

# Generated at 2022-06-14 13:06:10.580201
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    test_panda_series = pd.Series([1,2,3,4,5])
    test_panda_series.progress_apply(lambda x: x * 2, tclass=tqdm_pandas)
    test_panda_df = pd.DataFrame({
        'col1': [1,2,3,4,5],
        'col2': [6,7,8,9,10],
        'col3': [11,12,13,14,15]
    })
    test_panda_df.groupby('col1').progress_apply(lambda x: x * 2, tclass=tqdm_pandas)

# Generated at 2022-06-14 13:06:15.553584
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    try:
        import pandas as pd
    except ImportError:
        return None
    import numpy as np
    a = pd.DataFrame(np.random.rand(10, 2))

    with tqdm(total=a.shape[0]) as pbar:
        def pb_wrapper(x):
            pbar.update()
            return x
        a.groupby(lambda x: x).progress_apply(pb_wrapper)


# Generated at 2022-06-14 13:06:27.153693
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Test for tqdm_pandas()

    :return: None
    """

    import pandas as pd
    from tqdm.auto import tqdm

    def test_generator():
        for i in range(10):
            yield i

    # Test on SeriesGroupBy
    pbar = tqdm_pandas(tqdm(position=0), leave=True)
    pd.Series(test_generator()).groupby(lambda x: x % 2).progress_apply(lambda x: x**2)

    # Test on DataFrameGroupBy
    pbar = tqdm_pandas(tqdm(position=0), leave=True)
    pd.DataFrame({'a': list(range(10)),
                  'b': list(range(10, 20))}).groupby

# Generated at 2022-06-14 13:06:33.240274
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    df = pd.DataFrame({'a': [2, 3, 1, 4], 'b': [1, 4, 2, 3]})
    with tqdm(total=len(df)) as pbar:
        def func(df):
            pbar.update()
            return df.sort_values(by=['a'])
        df = df.groupby('b').progress_apply(func)


# Simple decorator

# Generated at 2022-06-14 13:06:44.404424
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import math

    # Produce random dataframe
    N = 10000
    random_data = np.random.rand(100, 10)
    df = pd.DataFrame(random_data)

    # Define slow function
    def func(x):
        z = sum(x)
        return z

    # Test without pbar
    df.progress_apply(func)

    # Test with tqdm
    tqdm_pandas(tqdm())
    df.progress_apply(func)
    try:
        from tqdm import tqdm_notebook as tqdm
    except ImportError:
        # Some systems don't have tqdm_notebook
        pass
    else:
        tqdm_pandas(tqdm())


# Generated at 2022-06-14 13:06:55.757527
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Deprecation warning exceptions do not work in Python 2.7
    if sys.version_info[0] >= 3:
        from io import StringIO
        from contextlib import redirect_stderr
        import pandas as pd
        import tqdm

        with redirect_stderr(stderr=StringIO()) as err:
            tqdm_pandas(tqdm)
        assert (len(err.getvalue()) > 0)

        with redirect_stderr(stderr=StringIO()) as err:
            with tqdm.pandas(desc='pd') as pd_tqdm:
                pd.DataFrame({'a': range(100)}).progress_apply(lambda x: x + 1,
                                                               axis=1)

# Generated at 2022-06-14 13:07:06.141305
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_pandas

    for f in tqdm_pandas, tqdm.pandas:
        f(total=10000)
        f(total=1000, ascii=True)
        f(10000, total=10000)  # tqdm_pandas(tqdm(total=10000), total=10000)
        f(tqdm(total=10000), total=10000)  # tqdm_pandas(tqdm(total=10000), total=10000)
        f(tqdm(), total=10000)  # tqdm_pandas(tqdm(), total=10000)
        f(total=10000, file=sys.stdout)
        f(total=10000, file=sys.stdout.buffer)

# Generated at 2022-06-14 13:07:14.127946
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    df = DataFrame({'c1': [1, 2, 3, 4], 'c2': [2, 3, 4, 5]})
    tqdm_pandas(tqdm, df.groupby('c1', observed=True).progress_apply(
        lambda x: x + 1))


import pandas as pd

# Monkeys patch progress_apply into pd.DataFrameGroupBy



# Generated at 2022-06-14 13:07:20.835298
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import numpy as np
        import pandas as pd
        import pandas.core.groupby
        from tqdm import tqdm
        from types import MethodType
    except ImportError:
        raise SkipTest

    def apply_chunks(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    pandas.core.groupby.DataFrameGroupBy.progress_apply = apply_chunks

    class FakeTqdm:
        def __init__(self, *args, **kwargs):
            pass

        def pandas(self, *args, **kwargs):
            return None

    df = pd.DataFrame(np.random.random((1000, 100)))

# Generated at 2022-06-14 13:07:28.877140
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    import sys
    import os.path
    sys.stderr = open(os.devnull, "w")
    tqdm_pandas(tqdm)
    data = np.random.rand(100, 2)
    df = pd.DataFrame(data)
    tqdm_pandas(tqdm, **dict(smoothing=0.7))
    df.groupby(0).apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:48.613475
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas"""
    from tqdm._utils import _deprecate_async
    from tqdm.auto import tqdm
    try:
        import pandas as pd
    except ImportError:
        pd = None

    if pd is None:
        raise ImportError('Test requires pandas')
    df = pd.DataFrame({'col': range(100)})
    # Test Panda
    with tqdm(total=len(df.index)) as pbar:
        df.progress_apply(lambda x: pbar.update())
    # Test deprecated class
    with tqdm(total=len(df.index)) as pbar:
        tqdm_pandas(pbar)
        df.progress_apply(lambda x: x)
    # Test deprecated async

# Generated at 2022-06-14 13:07:51.003627
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from ._tqdm_pandas import test_tqdm_pandas
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:57.753881
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from operator import add

    def func(x):
        for i in range(int(1e4)):
            pass

    df = pd.DataFrame(np.random.randn(100, 100))
    pd.core.groupby.DataFrameGroupBy.progress_apply = tqdm_pandas(tqdm)
    df.groupby(df.columns.tolist()).progress_apply(func)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 13:08:00.909179
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)


if __name__ == '__main__':
    from tqdm import tqdm

    _ = tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:08:13.417290
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    test = pd.DataFrame({'a': [0, 0, 1, 1], 'b': [1, 1, 2, 2]})
    res = test.groupby('a').progress_apply(lambda x: x)

    for i in range(len(test)):
        assert_eq(test.iloc[i], res.iloc[i])

try:
    from pandas import DataFrameGroupBy, SeriesGroupBy
except ImportError:
    DataFrameGroupBy, SeriesGroupBy = None, None


if DataFrameGroupBy is not None:
    tqdm_pandas_inpatched = DataFrameGroupBy.progress_apply


# Generated at 2022-06-14 13:08:24.394879
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    tqdm = tqdm_pandas(tqdm)

    # Test groupby-apply with tqdm
    df = pd.DataFrame({'a': [1, 1, 2, 2], 'b': [1, 2, 3, 4]})
    gb = df.groupby('a')
    gb.progress_apply(lambda x: x)

    # Test progress apply with tqdm
    df.progress_apply(lambda x: x)

    # Test register with pandas
    _ = tqdm.pandas(pandas=True)
    gb.progress_apply(lambda x: x)

    # Test pandas module wrapper
    _ = tqdm_pandas(pandas=True)
   

# Generated at 2022-06-14 13:08:35.658957
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        tqdm_pandas_orig()
    except TypeError:
        pass



# Generated at 2022-06-14 13:08:39.851102
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    from tqdm.autonotebook import tqdm, tqdm_pandas

    df = pandas.DataFrame({'x': [1, 2, 3]})
    for i in tqdm(range(10)):
        df.progress_apply(lambda x: x * x * i)

# Generated at 2022-06-14 13:08:47.417870
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    import pandas as pd
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
    try:
        import tqdm as tqdm
        import tqdm.contrib.concurrent
    except ImportError:
        return
    tt = tqdm.tqdm
    tt_class = tqdm.tqdm
    tt_class.pandas = tqdm_pandas

    # class
    tt_class(total=0, leave=False)
    try:
        tt_class.pandas(df.groupby(0))
    except AttributeError:
        pass

# Generated at 2022-06-14 13:08:57.254943
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    df1 = pd.DataFrame()
    df1['col'] = np.random.sample(1000)
    tqdm_pandas(df1.groupby('col').progress_apply(lambda x: [len(x)]))
    tqdm_pandas(df1.groupby('col').progress_apply(lambda x: [len(x)]))
    # tqdm_pandas(tqdm(df1.groupby('col').progress_apply(lambda x: [len(x)])))
    # tqdm_pandas(tqdm(df1.groupby('col').progress_apply(lambda x: [len(x)])))

# Generated at 2022-06-14 13:09:08.799956
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    assert tqdm_pandas(tqdm())  # tqdm class


try:
    from tqdm._tqdm_pandas import tqdm_pandas  # type: ignore

    from tqdm.std import TqdmType  # type: ignore
    for t in [TqdmType, TqdmType.from_factory(None).__class__]:
        t.pandas = staticmethod(tqdm_pandas)  # type: ignore
except ImportError:
    pass

# Generated at 2022-06-14 13:09:16.261092
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.random((1000, 1000)))
    with tqdm(total=df.progress_apply(len).sum()) as pbar:
        def _progress_apply(self, *args, **kwargs):
            pbar.update(args[0].size)
            return pd.DataFrame.apply(*args, **kwargs)
        setattr(type(df), 'progress_apply', _progress_apply)

        df.progress_apply(len)
        if pbar.n != df.progress_apply(len).sum():
            raise AssertionError('sum(len) != pbar.n')


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:26.933578
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, trange

    N = int(1e3)
    df = pd.DataFrame({'a': [1] * N, 'b': [2] * N})
    rows = sum(1 for r in df.progress_apply(lambda x: x, axis=1))
    assert((rows, rows) == (N, N))

    # tqdm_pandas(tqdm)(df.a.apply(lambda x: x))
    # assert (N, N) == (last_bar.n, last_bar.total)
    # assert (N, N) == (last_bar.n, last_bar.total)
    # tqdm_pandas(tqdm)(df.a.apply(lambda x: x))
    # assert

# Generated at 2022-06-14 13:09:38.403018
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm._utils import _term_move_up
    from tqdm import tqdm

    # Define test for DataFrameGroupBy.progress_apply
    df = pd.DataFrame({'x': list(range(5))})
    tqdm_pandas(tqdm)
    try:
        df.groupby('x').progress_apply(lambda x: x)
    except NameError:
        _term_move_up()  # clearing up
        tqdm_pandas(tqdm, disable=True)
        raise

    from tqdm import trange
    from tqdm import tqdm

    # Define test for DataFrameGroupBy.progress_apply
    df = pd.DataFrame({'x': list(range(5))})
   

# Generated at 2022-06-14 13:09:44.036464
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    N = 100
    df = pd.DataFrame({"col1": np.random.choice(range(10), N),
                       "col2": np.random.choice(range(10), N)})
    tqdm_pandas(tqdm)
    df.groupby("col1").progress_apply(lambda x: x)

# Generated at 2022-06-14 13:09:51.449320
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from numpy.random import random

    tqdm = tqdm_pandas(tqdm)
    DataFrame(random((10000, 1000))).groupby(0).progress_apply(lambda x: x ** 2)
    tqdm = tqdm_pandas(tqdm)
    DataFrame({"A": [0, 1, 2] * 3,
               "B": [3] * 9}).groupby("A").progress_apply(lambda x: x * 2)
    if __name__ == "__main__":
        print("test_tqdm_pandas() #passed")


test_tqdm_pandas()

# Generated at 2022-06-14 13:10:02.833739
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    ##########################################################################
    # WARNING: This test is very likely to be broken by future changes to the
    # tqdm API.
    ##########################################################################
    import pandas as pd
    import random
    import tqdm
    import tqdm.auto

    df = pd.DataFrame(
        {'user': list(range(10)), 'value': [random.random() for _ in range(10)]})
    tclass = tqdm.tqdm(file=tqdm.tqdm.DEFAULT_STATUS_BAR_ASCII)
    tqdm_pandas(tclass, desc='test_tqdm_pandas')
    df.groupby('user').progress_apply(lambda x: x)



# Generated at 2022-06-14 13:10:09.917787
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import numpy as np
        import pandas as pd
    except ImportError:
        print('\nSkipping pandas tests (requires pandas).')
        return

    tqdm_pandas(tqdm(total=100), desc='My Pandas loop').apply(lambda x: x ** 2)
    try:
        df = pd.DataFrame(
            np.random.randint(0, 100, (100000, 6)), columns=list('ABCDEF'))
        tqdm_pandas(tqdm(total=3), desc='My Pandas loop').map_apply(
            lambda x: x ** 2, axis=1
        )
        print('\nPandas tqdm unit test successful.')
    except Exception as e:
        print(e)

# Generated at 2022-06-14 13:10:20.632122
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.auto import tqdm

    try:
        import pandas.core.groupby.DataFrameGroupBy
        pd.core.groupby.DataFrameGroupBy.progress_apply = tqdm_pandas(
            pd.core.groupby.DataFrameGroupBy.progress_apply,
            unit='rows', leave=False)
    except:
        pass

    try:
        import pandas.core.groupby.SeriesGroupBy
        pd.core.groupby.SeriesGroupBy.progress_apply = tqdm_pandas(
            pd.core.groupby.SeriesGroupBy.progress_apply,
            unit='rows', leave=False)
    except:
        pass


# Generated at 2022-06-14 13:10:32.437237
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from tqdm import tqdm

    def func1(s):
        for i in s:
            pass

    def func2(s):
        for i in s:
            pass

    def func3(s):
        for i in s:
            pass

    try:
        tqdm_pandas(tqdm(range(100)))
    except (ImportError, IndexError, TypeError):
        pass

    tqdm_pandas(tqdm(range(100)), leave=True)

    d = {
        "a": [1, 2, 3],
        "b": [5, 6, 7, ],
    }
    s = Series(d)

# Generated at 2022-06-14 13:10:55.283766
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from random import random
    from tqdm import tqdm
    import warnings
    # suppress warnings about pandas
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # test dataframe with \r
    tqdm_pandas(tqdm, ncols=100)
    df = DataFrame([(random(), i) for i in range(100)], columns=['a', 'b'])
    df_sum = df.groupby('b').progress_apply(lambda group: group.a.sum())
    assert df.shape == df_sum.shape

    # test dataframe with \r\n
    tqdm_pandas(tqdm, file=sys.stdout, ncols=100)

# Generated at 2022-06-14 13:11:04.577470
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from random import randint
    from pandas import DataFrame

    class TqdmTypeSubclass(tqdm):
        @property
        def pandas(self):
            return tqdm_pandas

    class TqdmSubclass(TqdmTypeSubclass):
        pass

    df = DataFrame(
        {'col0': [randint(0, 100) for _ in range(10)],
         'col1': [randint(0, 100) for _ in range(10)],
         'col2': [randint(0, 100) for _ in range(10)]
         })

    df.groupby('col1').progress_apply(lambda x: x)
    TqdmTypeSubclass().pandas()(df.groupby('col1'))
   

# Generated at 2022-06-14 13:11:08.713897
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    tqdm = tqdm_pandas(tqdm, unit='bar')
    df = pd.DataFrame({'x': [1, 2, 3]})
    df.groupby('x').progress_apply(sum)

# Generated at 2022-06-14 13:11:13.391626
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_notebook as tqdm

    df = pd.DataFrame(['a', 'b', 'c'])
    dg = df.groupby(0)
    tqdm_pandas(tqdm)
    dg.progress_apply(len)

# Generated at 2022-06-14 13:11:22.008144
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    from tqdm import trange

    df = DataFrame(data=[[i, i] for i in trange(100)])
    tqdm._pandas_apply_patched = False
    result = df.groupby('A').progress_apply(len).reset_index()
    assert (result == df.groupby('A').apply(len).reset_index()).all().all()
    tqdm_pandas(tqdm)
    result2 = df.groupby('A').progress_apply(len).reset_index()
    assert ((result != result2).values.any())
    assert (result2 == df.groupby('A').apply(len).reset_index()).all().all()

# Generated at 2022-06-14 13:11:32.588521
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    import random

    df = pd.DataFrame(
        data=[[random.randint(0, 1000), random.uniform(0, 0.0001)]
              for _ in range(1000)],
        columns=['rand_int', 'rand_float'])

    # Test method with `file` argument
    with open(os.devnull, "w") as devnull:
        with tqdm(df.groupby('rand_int'), desc="tqdm_pandas", file=devnull) as t:
            t.progress_apply(lambda x: x.apply(sum))

    # Test method without `file` argument

# Generated at 2022-06-14 13:11:42.672142
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    tqdm_pandas(tqdm)

    # pd.Series test
    assert np.all(
        pd.Series(tqdm(range(10))) == pd.Series(range(10)))
    assert np.all(
        pd.Series(tqdm(range(10))).progress_apply(lambda x: x) ==
        pd.Series(range(10)))

    # pd.DataFrame test
    assert np.all(
        pd.DataFrame(tqdm(range(10))).progress_apply(lambda x: x, axis=0) ==
        pd.DataFrame(range(10)))

    # pd.DataFrame groupby test