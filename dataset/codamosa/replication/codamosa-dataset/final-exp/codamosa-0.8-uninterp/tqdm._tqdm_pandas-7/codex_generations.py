

# Generated at 2022-06-14 13:01:54.181992
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy
    import pandas
    from tqdm.auto import tqdm, trange
    tqdm.pandas()

    list_ = numpy.arange(10 ** 2)
    numpy.random.shuffle(list_)
    list_ = list_.reshape(-1, 10)
    df = pandas.DataFrame(list_)
    # Aggregate rows
    df.groupby(0).progress_apply(
        lambda x: tqdm(x, total=x.shape[0], desc='aggregate rows'))
    # Aggregate columns
    df.progress_apply(
        lambda x: tqdm(x, total=x.shape[0], desc='aggregate columns'))
    del list_, df

    s = pandas.Series(range(10 ** 2))
    s

# Generated at 2022-06-14 13:01:58.385561
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    global tqdm_pandas
    from tqdm import tqdm_gui
    from pandas import DataFrame
    from numpy import arange
    tqdm_pandas(tqdm_gui)
    df = DataFrame(arange(100).reshape((10, 10)))
    df.groupby(df.sum()).progress_apply(lambda x: x.sum())
    tqdm_pandas(tqdm_gui)



# Generated at 2022-06-14 13:02:09.476909
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Simple test for `tqdm_pandas` function.
    """
    try:
        import pandas as pd
    except ImportError:
        return

    class tqdm:
        class tqdmFake:
            pass
        @staticmethod
        def set_lock(*args):
            pass
        @staticmethod
        def pandas(*args, **kwargs):
            pass
    assert tqdm_pandas(tqdm, bar_format='{postfix[0][index]} {rate_fmt}') is None

    class tqdm:
        class tqdmFake:
            pass
        @staticmethod
        def set_lock(*args):
            pass
        @staticmethod
        def pandas(*args, **kwargs):
            pass

# Generated at 2022-06-14 13:02:15.690091
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """ Unit test for function tqdm_pandas """
    import pandas as pd
    import numpy as np
    import tqdm

    tqdm.pandas()
    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    df.groupby(0).progress_apply(lambda x: x ** 2)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:21.305680
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import sys
    from tqdm.std import tqdm_pandas, tqdm
    from tqdm.auto import tqdm as ta
    tqdm_pandas(tqdm, file=sys.stdout)
    tqdm_pandas(ta, file=sys.stdout)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:32.979591
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm.contrib import pandas

    df = pd.DataFrame([[1, 2], [3, 4], [None, 5], [7, 8]], columns=['A', 'B'])
    test_col = 'A'
    out = df.groupby(test_col).progress_apply(lambda x: x.mean())
    assert out.isna().sum().sum() == 1
    assert out.isna().sum().sum() == 1
    assert out.shape == df.shape
    out = df.progress_apply(lambda x: x.mean())
    assert out.isna().sum().sum() == 1
    assert out.shape == (2, df.shape[1])

# Generated at 2022-06-14 13:02:42.354515
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import trange
    from tqdm.contrib.test_tqdm_pandas import TestTqdmPandas

    def tqdm_func(df):
        # print(df)
        return df.sum()

    for cls in [TestTqdmPandas, trange]:
        tqdm_pandas(cls, leave=False, desc='test')
        df = pd.DataFrame({'A': [0, 1, 2]})
        df.groupby(0).progress_apply(tqdm_func)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:49.120773
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Check that the function is working
    import pandas
    assert 'pandas' not in [x.__name__ for x in
                            pandas.core.groupby.DataFrameGroupBy.progress_apply.__code__.co_names]
    tqdm_pandas(type('', (object,), {'name': 'tqdm_test'}))
    assert 'pandas' in [x.__name__ for x in
                        pandas.core.groupby.DataFrameGroupBy.progress_apply.__code__.co_names]



# Generated at 2022-06-14 13:02:59.209334
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    try:
        import pandas as pd
    except:
        return

    with tqdm(total=1, leave=False, file=open(os.devnull, 'w')) as t:
        tqdm_pandas(t)

    with tqdm(total=1, leave=False, file=open(os.devnull, 'w')) as t:
        tqdm_pandas(TqdmDefault)

    df = pd.DataFrame({'a': range(10)})
    df.groupby('a').progress_apply(lambda x: None)

# Generated at 2022-06-14 13:03:09.893410
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    import random
    import string

    def rand_text(n=20):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(n))

    df = pd.DataFrame({
        'id': list(range(10)),
        'data': [rand_text() for _ in range(10)]
    })

    # Test in tqdm()
    with tqdm(total=df.shape[0], unit='rows') as pbar:  # same as tqdm_gui(total=df.shape[0])
        df2 = df.groupby(['id']).progress_apply(lambda x: x)
    assert len(df) == len(df2)
    assert df

# Generated at 2022-06-14 13:03:24.352068
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return  # skip test
    old_fname = '_tqdm.tqdm.pandas.fname'
    old_fname_val = getattr(pd.core.groupby.DataFrameGroupBy, old_fname, None)
    old_f = getattr(pd.core.groupby.DataFrameGroupBy, 'progress_apply', None)
    setattr(pd.core.groupby.DataFrameGroupBy, old_fname, 'success')

# Generated at 2022-06-14 13:03:32.763463
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm.contrib import pandas

    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm.tqdm_notebook)
    tqdm_pandas(tqdm.tqdm_gui)
    tqdm_pandas(tqdm.tqdm_pandas)

    tqdm_pandas(tqdm.tqdm)
    tqdm_pandas(tqdm.tqdm_notebook)
    tqdm_pandas(tqdm.tqdm_gui)
    tqdm_pandas(tqdm.tqdm_pandas)


if __name__ == '__main__':
    test_tqdm_

# Generated at 2022-06-14 13:03:44.464187
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:03:53.318532
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import trange
    with trange(100) as t:
        tqdm_pandas(t, desc='test_tqdm_pandas', dynamic_ncols=True, leave=False)
        arr = np.random.randint(0, 100, (1000, 1000))
        df = pd.DataFrame(arr)
        df.groupby(0).progress_apply(lambda x: x ** 2)
        df.groupby(0).progress_apply(lambda x: x ** 2)


# Class for tqdm_pandas

# Generated at 2022-06-14 13:04:00.161124
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.contrib.concurrent import thread_map
    from multiprocessing import Pool
    from pandas import DataFrame
    from itertools import product

    def progress_apply_test(f, **kwargs):
        from itertools import product
        from pandas import DataFrame

        df = DataFrame({'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]})

        # check the default tqdm is used
        with tqdm.utils.disable_std_write_close():
            df.progress_apply(f, **kwargs)

        # check the custom tqdm is used
        tqdm._instances.clear()
        tqdm.pandas()


# Generated at 2022-06-14 13:04:08.879912
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Stolen from pandas testsuite
    # Any update to pandas must be accompanied by an update to this.
    import numpy as np
    import pandas as pd
    import pandas.util.testing as tm
    import pandas._testing as lib


# Generated at 2022-06-14 13:04:18.840804
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Functional test: tqdm_pandas"""
    import pandas as pd
    df = pd.DataFrame(columns=['a', 'b', 'c'])
    df.loc[1] = [1, 2, 3]
    df.loc[2] = [4, 5, 6]
    df.loc[3] = [7, 8, 9]
    df.loc[4] = [10, 11, 12]
    import tqdm as tqdm
    with tqdm.tqdm_pandas(total=len(df.index)) as t:
        df['d'] = df.progress_apply(lambda x: sum(x), axis=1)
    assert df['d'].tolist() == [6, 15, 24, 33, 42]



# Generated at 2022-06-14 13:04:27.635731
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.autonotebook import tqdm
    import pandas as pd
    try:
        tqdm_pandas(tqdm, ascii=True)
    except:
        raise
    # Test DataFrameGroupBy
    N = 100000
    df = pd.DataFrame({'A': [0] * N, 'B': [1] * N})
    ret = df.groupby('A').progress_apply(lambda x: x['B'].sum())
    assert ret.equals(df['B'].sum())
    # Test DataFrame
    df = pd.DataFrame({'A': [0] * N, 'B': [1] * N})
    ret = df.progress_apply(lambda x: x['B'].sum(), axis=1)
    assert ret.equ

# Generated at 2022-06-14 13:04:39.705582
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas

    # check installation
    tqdm(pandas.Series([1, 2, 3]))

    # check deinstallation
    tqdm_pandas(tqdm(pandas.Series([1, 2])))
    tqdm_pandas(tqdm(pandas.Series([1, 2])), leave=True)
    tqdm_pandas(tqdm, pandas.Series([1, 2]))
    tqdm_pandas(tqdm, pandas.Series([1, 2]), leave=True)
    tqdm_pandas(tqdm, pandas.Series([1, 2]), leave=True, file=sys.stdout)


if __name__ == '__main__':
    test

# Generated at 2022-06-14 13:04:46.311798
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    df = pd.DataFrame()
    df['x'] = ['a', 'b', 'c'] * 100000
    df['y'] = [4, 5, 6] * 100000
    tqdm.pandas(desc='test')
    df.groupby('x').progress_apply(lambda x: x + x)
    df.groupby('y').progress_apply(lambda x: x + x)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:55.762343
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm
    def inc(x):
        """
        Dummy progress bar test function
        """
        return x + 1

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    with tqdm.tqdm_pandas(total=len(df)) as t:
        df.progress_apply(inc)


# Generated at 2022-06-14 13:05:05.229487
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    from tqdm import tqdm
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm, desc="tqdm_pandas(tqdm, desc)")
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm, desc="tqdm_pandas(tqdm, desc)")
    with tqdm(total=1) as t:
        tqdm_pandas(tqdm, desc="tqdm_pandas(tqdm, desc)")
    with tqdm(total=1) as t:
        tqdm_pandas(tqdm, desc="tqdm_pandas(tqdm, desc)")



# Generated at 2022-06-14 13:05:14.298236
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import tqdm

    # Test compatibility with variant 1
    pandas.Series(range(5)).progress_apply(lambda s: s)
    tqdm_pandas(tqdm.tqdm(
        pandas.Series(range(5)).progress_apply(lambda s: s), leave=False))

    # Test compatibility with variant 2
    pandas.Series(range(5)).progress_apply(lambda s: s)
    tqdm_pandas(tqdm.tqdm, pandas=True)

# Generated at 2022-06-14 13:05:21.648047
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.choice(a=[0,1],
                                       size=(10, 5)),
                      columns=['A','B','C','D','E'])
    for i in tqdm_pandas(range(5)):
        df.apply(len)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:29.558297
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    import logging
    import warnings
    import tqdm
    import sys

    sys.stderr = open('.test_tqdm_pandas.err', 'w')

    warnings.filterwarnings('once')
    logging.captureWarnings(True)
    # setup
    t = np.random.randint(1, 1000, size=100)
    df = pd.DataFrame({'d': t})
    expected_total = df.groupby(df.d).size().sum()

    # case 1: tqdm.pandas(...)
    tqdm.pandas(desc="my bar!")

# Generated at 2022-06-14 13:05:33.072612
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame, Series

    df = DataFrame({'a': Series(range(100)), 'b': Series(range(100))})
    tqdm_pandas(tqdm, df.groupby('a').sum())

# Generated at 2022-06-14 13:05:39.554806
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    df = pd.DataFrame(data={"a": [1] * 100, "b": [2] * 100})
    tqdm_pandas(tqdm())
    pd.DataFrame(data={"a": [1] * 100, "b": [2] * 100}).groupby("a").progress_apply(
        lambda x: x)

# Generated at 2022-06-14 13:05:46.459004
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.randn(10000, 3))
    tqdm_pandas(tqdm())
    df.groupby(0, as_index=False).progress_apply(lambda x:x)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:55.422470
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from time import sleep
    from .tqdm import tqdm

    # Load iris dataset
    iris_df = pd.read_csv("/home/casperdcl/Documents/Python_Codes/Kaggle/input/iris.csv")

    # Convert species column into boolean
    def convert_to_bool(x):
        if x == 'Iris-versicolor':
            return False
        if x == 'Iris-setosa':
            return True
        if x == 'Iris-virginica':
            return False

    iris_df['bool'] = iris_df['species'].apply(convert_to_bool)

    # Defining a groupby and progress apply lambda function
    groupby_species = iris_df.groupby('species')


# Generated at 2022-06-14 13:06:01.428344
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pytest

    with pytest.warns(None):
        try:
            from tqdm import tqdm, tqdm_notebook  # noqa
        except ImportError:
            pass
        else:
            tqdm_pandas(tqdm)
            tqdm_pandas(tqdm(total=1))
            tqdm_pandas(tqdm_notebook)
            tqdm_pandas(tqdm_notebook(total=1))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:14.817429
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    # dummy dataframe
    df = DataFrame({'a': [1, 2, 3],
                    'b': [4, 5, 6],
                    'c': [7, 8, 9]})
    # dummy func to apply on df
    def add_1(x):
        return x + 1
    df2 = df.groupby(by='a').progress_apply(add_1)
    # dummy func to apply on df
    def add_2(x):
        return x + 2
    df3 = df.groupby(by='a').progress_apply(add_2)
    # dummy func to apply on df
    def add_3(x):
        return x + 3

# Generated at 2022-06-14 13:06:26.487838
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    tqdm = tqdm_pandas(range(10))
    df = pd.DataFrame(np.random.random((10, 10)))
    df.groupby(by=[1]).progress_apply(lambda x: x.max())
    df.groupby(by=[1]).progress_apply(lambda x: x.max(), meta=tqdm)
    df.groupby(by=[1]).progress_apply(lambda x: x.max(), total=10)
    df.groupby(by=[1]).progress_apply(lambda x: x.max(), total=10,
                                      tqdm_deprecated=tqdm)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:35.871900
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    from tqdm.tests import common

    # Dummy function for testing
    def dummy(**kwargs):
        for i in range(4):
            yield i

    # Instantiate tqdm and test
    with common.AssertPrints("\r|0/4 [00:00<?, ?it/s]", disable=(not __debug__)):
        for _ in tqdm_pandas(tqdm(), desc='Test')(dummy()):
            pass

    # Decorate function and test
    @tqdm_pandas
    def dummy2(**kwargs):
        for i in range(4):
            yield i


# Generated at 2022-06-14 13:06:43.043586
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_pandas, tqdm

    df = pd.DataFrame(
        {'a': [100 * i for i in range(100000)], 'b': [100 * i for i in range(100000)]})
    tqdm_pandas(tqdm())
    df.groupby('a').progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:54.677133
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.autonotebook import tqdm
    import numpy as np
    # Create a dataframe
    df = pd.DataFrame(np.random.randn(100, 3), columns=list('ABC'))
    # Percentage split for training and testing
    split = int(len(df) * 0.80)
    # Split the dataframe into 'train' & 'test'
    df_train = df[:split]
    df_test = df[split:]

    # 'progress_apply' is used to apply a function along a particular axis
    # of the DataFrame.

    # In this case, it is the 'A' column of the train and test dataframes.
    # But it can be any column

    # This is the function that is called on each row of the column.


# Generated at 2022-06-14 13:07:03.074569
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm, tqdm_pandas
    from tqdm.auto import tqdm as auto_tqdm

    # Unit test for function tqdm_pandas
    try:
        from pandas.core.groupby import DataFrameGroupBy
    except ImportError:
        return

    def tqdm_test(tqdm_func, **kwargs):
        tqdm_func(**kwargs)
        DataFrameGroupBy.progress_apply = lambda x, y: x.apply(y)

    tqdm_test(tqdm)
    tqdm_test(auto_tqdm)
    tqdm_test(tqdm_pandas, tclass=tqdm)

# Generated at 2022-06-14 13:07:10.155705
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_pandas

    df = pd.DataFrame(data={
        'a': range(100),
        'b': range(100, 200),
        'c': range(200, 300),
        'd': range(300, 400),
    })
    tqdm_pandas(tqdm_kwargs={"mininterval": 1})
    df = df.groupby('a').progress_apply(lambda x: x['b'] + x['c'] + x['d'])
    assert all(df.values == pd.Series(range(500, 600)))


# Generated at 2022-06-14 13:07:16.627297
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import numpy as np
    import time
    N = 2 ** 18
    df = pandas.DataFrame({'a': np.arange(N, dtype=np.int64)})
    tqdm_pandas(lambda t: time.sleep(0.001), total=N)
    df.groupby('a').progress_apply(lambda x: time.sleep(0.001))


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:22.885108
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    d = {'col1': np.random.randint(0, 100, 10), 'col2': np.random.randint(0, 100, 10)}
    df = pd.DataFrame(data=d)
    tqdm_pandas(df.groupby("col1").progress_apply(lambda x: x))
    
test_tqdm_pandas()


# Generated at 2022-06-14 13:07:32.210237
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import random
    from tqdm import tqdm

    random.seed(42)
    df = pd.DataFrame()
    df['x'] = np.random.randn(1000)
    df['y'] = np.random.randn(1000)
    df['z'] = np.random.randn(1000)

    # Sanity check

# Generated at 2022-06-14 13:07:42.328582
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # FIXME: write unit-test
    pass


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:53.322991
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series

    try:
        import tqdm as tqdm
    except:
        import tqdm_py3 as tqdm

    vn = 100
    rng = range(vn)
    rng_100 = range(100)

# Generated at 2022-06-14 13:08:03.206448
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test `tqdm_pandas` function."""
    if sys.version_info >= (3, 4):
        from tqdm import tqdm
        import pandas as pd

        df = pd.DataFrame(index=range(
            100), columns=['x1', 'x2', 'x3'], dtype='float64')
        df['x1'] = df.index.values
        df = df.groupby('x1').apply(lambda x: x ** 2)


# Generated at 2022-06-14 13:08:14.946126
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
        pd.core.groupby.DataFrameGroupBy.progress_apply = \
            tqdm_pandas(tqdm, desc='DFGroupBy')
        df = pd.DataFrame({'a': np.random.randint(0,10, size=1000000),
                           'b': np.random.randint(0,10, size=1000000)})
        df.groupby('a').progress_apply(lambda x: x.sum())
        df.groupby('a').progress_apply(lambda x: x.sum(),
                                       desc='lambda_sum')
    except ImportError:
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:24.489504
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    print('testing tqdm_pandas')
    from tqdm import tqdm
    from tqdm._utils import _deprecate_module

    tqdm_pandas = _deprecate_module('tqdm_pandas', 'tqdm')
    t = tqdm_pandas(tqdm)
    # test the basic functionality
    t.pandas(total=10)
    # test the decorator with @tqdm_pandas
    # TODO: test with named argument 'total'


# Unit tests
if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:27.255549
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from spec.tqdm_pandas_tests import test  # NOQA
    test()


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:36.690968
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from numpy.random import randint

    df = DataFrame(randint(5, size=(5, 5)),
                   index=['a', 'b', 'c', 'd', 'e'],
                   columns=['1', '2', '3', '4', '5'])
    df.groupby('1').progress_apply(lambda x: x)

    def f(df):
        return df

    tqdm_pandas(df.groupby('1').progress_apply(lambda x: x))
    tqdm_pandas(df.groupby('1').progress_apply(f))

# Generated at 2022-06-14 13:08:45.343004
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy

    # Check delayed adapter
    class MockTclass:
        class PandasMock(object):
            pass

        pandas = PandasMock
        __name__ = 'mock'

    type(tqdm_pandas)(tclass=MockTclass,
                      tqdm_kwargs={})
    assert isinstance(tqdm_pandas.tclass.pandas, MockTclass.pandas)
    assert tqdm_pandas.tqdm_kwargs == {}

    # Check delayed adapter
    class MockProgressBar:
        class PandasMock(object):
            pass

        pandas = PandasMock

    tqdm_pandas

# Generated at 2022-06-14 13:08:55.958253
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm import tqdm_notebook
    from tqdm.contrib.tests import tclass

    # Test pandas.DataFrameGroupBy.progress_apply
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm_notebook)
    tqdm_pandas(tclass)
    tqdm_pandas(deprecated_t=tclass)
    for _ in tqdm([1, 2, 3], desc=None, leave=None):
        df = pd.DataFrame([[3, 2], [5, 1]], columns=['a', 'b'])
        grouped = df.groupby('a')
        grouped.progress_apply

# Generated at 2022-06-14 13:09:08.083144
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, tqdm_pandas

    tqdm_pandas(tqdm(total=100), leave=False)
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm(total=100), leave=True)
    tqdm_pandas(tqdm(pandas=False))
    tqdm_pandas(tqdm(pandas=True))
    tqdm_pandas(tqdm(pandas=None))

    pd.DataFrame([1]).groupby(0).progress_apply(lambda x: 1)


if __name__ == "__main__":
    test_tq

# Generated at 2022-06-14 13:09:27.292163
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        import numpy
    except ImportError:
        return None

    # This is currently just an identity function
    # that should work as a unit test.
    tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:09:38.625367
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.auto import trange
    import pandas as pd
    import numpy as np
    nrows = int(1e6)
    df = pd.DataFrame({'a': np.random.randint(0, 5000, size=nrows),
                       'b': np.random.randint(0, 5000, size=nrows),
                       'N': np.random.randint(5, size=nrows),
                       'x': 'x'})

    # test default pandas # i.e. no tqdm
    rs = df.groupby('x').progress_apply(lambda x: x**2)

    # test tqdm pandas
    with trange(10) as t:
        t.pandas(total=10)

# Generated at 2022-06-14 13:09:41.611682
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    __test_tqdm_pandas()
    __test_tqdm_pandas()
    __test_tqdm_pandas()



# Generated at 2022-06-14 13:09:49.789575
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from tqdm.autonotebook import tqdm
    except:
        from tqdm import tqdm
    try:
        import pandas as pd
    except ImportError:
        pass
    else:
        from pandas.core.groupby import DataFrameGroupBy

        tqdm_pandas(tqdm)
        assert DataFrameGroupBy.progress_apply.__module__ == __name__
        df = pd.DataFrame({'X': [1]})
        tqdm.pandas(desc='my desc')
        df.groupby('X').progress_apply(lambda x: x)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:10:01.942901
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    To run the tests: python3 setup.py test
    """
    import pandas as pd
    from tqdm import tqdm

    try:
        from unittest import mock
    except ImportError:
        from unittest.mock import mock

    df = pd.DataFrame(range(10))
    tclass1 = type(tqdm)
    tclass1.pandas = mock.MagicMock()
    tqdm_pandas(tclass1)
    assert tclass1.pandas.called

    tclass2 = mock.MagicMock()
    tclass2.__name__ = 'tqdm_notebook'
    tclass2.pandas = mock.MagicMock()
    tqdm_pandas(tclass2)
    assert tclass2

# Generated at 2022-06-14 13:10:09.482492
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas"""
    from pandas import DataFrame, Series
    from numpy import random

    # Generate random arrays
    a, b, c = [random.randint(-100, 100, 100) for _ in range(3)]
    df = DataFrame(dict(a=a, b=b, c=c))
    target = Series(a + b + c)

    # Without tqdm_pandas, progress_apply should trigger a warning
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = df.progress_apply(lambda x: x.sum(), axis=1)
        assert len(w) == 1
        assert issubclass(w[-1].category, tqdm.TqdmDeprecationWarning)



# Generated at 2022-06-14 13:10:20.416073
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import tqdm.pandas
    except ImportError:
        # skip test if tqdm.pandas is not available
        return
    # Check deprecated use case
    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm.tqdm)
        assert all(["Please use `tqdm.pandas(...)" in str(wi.message)
                    for wi in w])
    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm.tqdm, smoothing=0.1, mininterval=0.5)
        assert all(["Please use `tqdm.pandas(...)" in str(wi.message)
                    for wi in w])
    #

# Generated at 2022-06-14 13:10:32.323145
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    pd = __import__('pandas')
    tqdm = __import__('tqdm')
    assert tqdm.tqdm is tqdm.tqdm_gui is tqdm.tqdm_notebook is tqdm.trange
    assert tqdm.tqdm_pandas is tqdm_pandas
    assert pd.core.groupby.DataFrameGroupBy.progress_apply
    assert tqdm.pandas is not tqdm_pandas
    df = tqdm.tqdm_pandas(pd.DataFrame({'a': [1, 2, 3, 4]}))
    assert df.progress_apply is not None  # noqa: E711
    t

# Generated at 2022-06-14 13:10:40.089303
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from .auto import tqdm

    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy

    tqdm_pandas(tqdm)

    # Regression test for issue #267
    df = DataFrame({"a": [1]})
    assert DataFrameGroupBy(df).progress_apply.__name__ == 'progress_apply'

    # Test with all parameters
    tqdm_pandas(tqdm, ascii=True, mininterval=1., miniters=1, postfix=True,
                smoothing=1., unit_scale=True, unit='test')

# Generated at 2022-06-14 13:10:48.515928
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Tests function tqdm_pandas.
    """
    from tqdm.auto import tqdm, trange
    from pandas import DataFrame

    # Test if an error is raised with incorrect inputs
    with pytest.raises(Exception):
        tqdm_pandas(1)
        tqdm_pandas(1.2)
        tqdm_pandas([1, 2, 3])
        tqdm_pandas({1: 2})

    # Test if there is no error with correct inputs
    tqdm_pandas(tqdm)
    tqdm_pandas(trange)

# Generated at 2022-06-14 13:11:25.333555
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    try:
        tqdm_pandas(tqdm)
        pd.DataFrame({'a': [1, 2, 3]}).groupby(['a']).progress_apply(lambda g: g)
    except ImportError:
        return

    assert hasattr(tqdm.tqdm, 'pandas')


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:11:35.493576
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    # create dummy data
    data = pd.DataFrame(
        {'col': np.random.randint(5, size=(5, 1)).flatten()})

    # function to test progress_apply
    def fun(x: int) -> str:
        if x == 0:
            raise ValueError(
                "`ValueError` will be raised for testing `on_error` function"
            )
        else:
            return 'Pandas_progress_apply_test_OK'

    # The following doesn't work:
    # TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
    # data.groupby('col').progress_apply(fun, meta='str')



# Generated at 2022-06-14 13:11:43.394665
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm

    iterables = [range(1000), range(2000)]
    iterables_tqdm = tqdm.tqdm(iterables)
    res = tqdm_pandas(iterables_tqdm)
    assert isinstance(res, type(iterables_tqdm)), res

    iterables_tqdm = tqdm.tqdm(iterables, ascii=True)
    res = tqdm_pandas(iterables_tqdm)
    assert isinstance(res, type(iterables_tqdm)), res


if __name__ == '__main__':
    test_tqdm_pandas()