

# Generated at 2022-06-14 13:01:30.403021
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        df = pandas.DataFrame({"test": [1, 2, 3]})
        t = tqdm(total=len(df))
        t.pandas(df=df, total=len(df), desc='testing pandas')
        t.pandas(df=df, unit='test', desc='testing pandas')
        assert(len(t) == len(df))
        assert(t.total == len(df))
        assert(t.desc == 'testing pandas')
        assert(t.unit == 'test')
        t.n = len(t)
        t.update(0)
        t.update()
        t.close()
    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    test

# Generated at 2022-06-14 13:01:39.467778
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas import read_csv

    df_iris = read_csv(
        'https://raw.githubusercontent.com/pandas-dev'
        '/pandas/master/pandas/tests/data/iris.csv')
    df_iris.groupby('Name').progress_apply(lambda x: x.describe())

    df = DataFrame({
        'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Fruit': ['Banana', 'Strawberry', 'Apple', 'Banana'],
        'Quantity': [1, 2, 3, 4],
        'Price': [0.56, 1.7, 2.22, 2.7]
    })
    f = lambda x: x.progress_apply(lambda y: x.Fruit.unique())


# Generated at 2022-06-14 13:01:49.586701
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    from datetime import datetime

    # A list of dates
    date_list = [datetime(2019, 1, 1),
                 datetime(2019, 1, 2),
                 datetime(2019, 1, 3),
                 datetime(2019, 2, 5)] * 10
    # Convert [datetime] into [date]
    df = pandas.DataFrame(date_list)
    df.columns = ['date']

    # Call tqdm_pandas, which calls tqdm.pandas(...)
    tqdm_pandas(tqdm)

    # Group dates by month, and apply tqdm_pandas progress bars to each group
    df.groupby(df['date'].dt.month).progress_apply(len)

# Generated at 2022-06-14 13:01:59.351003
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    try:
        import pandas as pd
    except ImportError:
        warnings.warn("pandas not found, skipping pandas tests")
    else:
        # Test definitions
        pandas_test_df = DataFrame(
            {'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

        pandas_test_df2 = pandas_test_df.groupby('Value').sum()

        # Unit tests

# Generated at 2022-06-14 13:02:09.795223
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Tests
    :func:`tqdm.utils.tqdm_pandas`
    """
    from tqdm import tqdm
    tqdm.pandas(desc='a')
    tqdm.pandas(desc='b')
    tqdm.pandas(desc='c')
    tqdm.pandas(desc='d')
    tqdm.pandas(desc='e')
    tqdm.pandas(desc='f')
    tqdm.pandas(desc='g')
    tqdm.pandas(desc='h')
    tqdm.pandas(desc='i')
    tqdm.pandas(desc='j')
    tqdm.pandas(desc='k')
    tqdm.p

# Generated at 2022-06-14 13:02:19.359085
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Tests `tqdm_pandas` function.
    """
    from tqdm import trange
    from tqdm import TqdmDeprecationWarning

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        tqdm_pandas(trange(3, 0, -1))
        assert len(w) == 1
        assert issubclass(w[-1].category, TqdmDeprecationWarning)
        assert "Please use `tqdm.pandas(" in str(w[-1].message)
        tqdm_pandas(tqdm_notebook(range(3), desc='', leave=True))
        assert len(w) == 2

# Generated at 2022-06-14 13:02:24.222938
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    df = pd.DataFrame({'a': [1, 2, 3]})
    tqdm_pandas(df.groupby('a').progress_apply(lambda x: x))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:31.013500
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.contrib.tests import dummy_pandas, tqdm
    tqdm_pandas(tqdm)  # apply the adapter
    assert isinstance(pd.DataFrame([])['a'].progress_apply(lambda x: x),
                      dummy_pandas.DummyProgressBar)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:37.898617
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm
    df = pd.DataFrame({'a': np.random.randint(100, size=100),
                       'b': np.random.randint(100, size=100)})
    list(df.groupby(['a']).progress_apply(lambda x: x.sum()))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:47.066665
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    @tqdm_pandas
    def main():
        pass
    @tqdm_pandas
    def main1(t):
        pass
    main()
    main1(None)

# Generated at 2022-06-14 13:03:00.699037
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import warnings
    import tqdm
    tqdm.tqdm.pandas(tqdm.tqdm)

    with warnings.catch_warnings(record=True) as warn_list:
        tqdm_pandas(tqdm.tqdm)

    tqdm_pandas(tqdm.tqdm_notebook)

    df = pd.DataFrame({'A': np.arange(1000)})
    with tqdm.tqdm_notebook(total=df.shape[0]) as pbar:
        def foo(x):
            pbar.update()
            return x
        df = df.progress_apply(foo, axis=1)


# Generated at 2022-06-14 13:03:07.950441
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    from numpy import random
    data = random.randint(10, size=(10000, 1000))
    expected = DataFrame(data).progress_apply(sum)

    with tqdm(total=len(data)) as t:
        def prog_apply(chunk):
            tqdm_pandas(t, total=len(data))
            return sum(chunk)

        actual = DataFrame(data).progress_apply(prog_apply)

    assert (actual == expected).all().all()


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:11.376187
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    tqdm_pandas(tqdm(unit='B', unit_scale=True, unit_divisor=1024))

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:19.703418
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(None)
    tqdm_pandas(1)
    tqdm_pandas(type(None))
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm_notebook)
    tqdm_pandas(tqdm_notebook())


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:30.368548
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    def _test_pandas_apply(tqdm_cls):
        import numpy as np
        import pandas as pd
        import random
        indices = np.arange(1, 10**7)
        data = {'c%i' % i: np.random.randn(len(indices)) for i in range(100)}
        df = pd.DataFrame(data, index=indices)

        def add_val_to_column(df, column_name, value):
            df[column_name] += value
            return df

        old_cols = list(df.columns)
        new_cols = list(df.columns) + ['new_col']

# Generated at 2022-06-14 13:03:39.424585
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, ProgressBar, Series
    from numpy.random import choice

    class TestProgressBar(ProgressBar):
        def __init__(self, *args, **kwargs):
            super(TestProgressBar, self).__init__(*args, **kwargs)
            self.iter = 0

        def update(self, *args):
            self.iter += 1

    def apply_func(df):
        return df.apply(lambda x: x)
    for n in [0, 1, 2, 5, 10]:
        df = DataFrame(choice(range(1000), size=(n, n)))
        df_test = df.copy()
        df_test.progress_apply = apply_func
        tp = TestProgressBar()
        pbar = tqdm_pandas(tp)

# Generated at 2022-06-14 13:03:49.831724
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_pandas, tqdm
    try:
        from pandas import Series
    except ImportError:
        return
    try:
        # pandas deprecation warning not raised on older versions
        tqdm_pandas(tqdm(desc='test', total=100))
    except:
        pass
    try:
        # pandas deprecation warning not raised on older versions
        tqdm_pandas(tqdm_pandas)
    except:
        pass
    with tqdm_pandas(tqdm(desc='test', total=10000)) as t:
        Series(range(10000)).progress_apply(lambda x: x ** 2)
    t.close()



# Generated at 2022-06-14 13:03:53.142077
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        tqdm_pandas(tqdm, iterable=range(100))
    except (TypeError, Exception):
        raise TypeError("tqdm_pandas is not a function!")
    return True  # no errors

# Generated at 2022-06-14 13:04:03.834681
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for the function tqdm_pandas
    """
    from tqdm.contrib.test_tqdm import with_setup
    from tests_tqdm import SilentNoBarTestCase, closing, skipIf

    try:
        import pandas
    except ImportError:
        pandas = None

    class TestPandas(SilentNoBarTestCase):

        def setUp(self):
            super(TestPandas, self).setUp()
            self.range_it = range(1000)

        @skipIf(pandas is None, "pandas not installed")
        def testPandas(self):
            """
            Test the pandas pandas_prog functions
            """
            import pandas

# Generated at 2022-06-14 13:04:10.713630
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm, pandas

    # with class
    tqdm_pandas(tqdm.tqdm)
    # set display option
    tqdm_pandas(tqdm.tqdm, mininterval=0)
    # set progress bar position
    tqdm_pandas(tqdm.tqdm, position=1)
    # with instance
    tqdm_pandas(tqdm.tqdm())

    # deprecated case
    tqdm_pandas(tqdm_pandas)
    # deprecated case
    tqdm_pandas(tqdm_pandas(tqdm.tqdm, mininterval=0))

# Generated at 2022-06-14 13:04:22.730514
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with tqdm_pandas(total=0) as pbar:
        assert pbar.smoothing == 1e-3
        assert pbar.dynamic_ncols
    with tqdm_pandas(total=0, smoothing=0) as pbar:
        assert not pbar.dynamic_ncols
    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    df.groupby(0).progress_apply(lambda x: x)
    df2 = pd.DataFrame(np.random.randint(0, 100, (1000000, 6)))
    df2.groupby(0).progress_apply(lambda x: x)


if __name__ == "__main__":
    r = test_tqdm_pandas()

# Generated at 2022-06-14 13:04:31.072087
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame(np.random.rand(10000, 2),
                      columns=['x', 'y'])

    # deprecated
    t = tqdm(total=len(df), desc='foo')
    tqdm_pandas(t, df.groupby('x').progress_apply(lambda x: x + 1))
    t.close()

    # recommended
    tqdm.pandas(desc='foo').progress_apply(df.groupby('x'),
                                           lambda x: x + 1)

    # recommended with tqdm_obj
    t = tqdm(total=len(df), desc='foo')

# Generated at 2022-06-14 13:04:41.712333
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import tqdm

    df = pandas.DataFrame({'a': range(10)})
    try:
        tqdm_pandas(tqdm)
        df.groupby(lambda x: x).progress_apply(lambda x: x)

        tqdm_pandas(tqdm.tqdm)
        df.groupby(lambda x: x).progress_apply(lambda x: x)

        tqdm_pandas(tqdm.tqdm(
            'foo', file=sys.stdout))  # delayed adapter case must not output anything
    except TqdmDeprecationWarning:
        pass
    else:
        raise RuntimeError("tqdm_pandas unit test failed")



# Generated at 2022-06-14 13:04:47.740013
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    import pandas as pd
    from tqdm.auto import tqdm

    df = pd.DataFrame(
        data=range(100), columns=['tqdm_pandas'])
    assert list(df.tqdm_pandas) == list(df.tqdm_pandas.apply(
        lambda x: x,
        meta=str,
    ))
    assert isinstance(df['tqdm_pandas'].progress_apply(
        lambda x: x,
        meta=str,
    ), tqdm)
    tqdm_pandas(tqdm, leave=False)

# Generated at 2022-06-14 13:05:00.193628
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy

    class DummyDFGroupBy(DataFrameGroupBy):
        pass

    for _ in tqdm_pandas(DummyDFGroupBy()):
        pass
    for _ in tqdm_pandas(tqdm()):
        pass


if __name__ == '__main__':
    from tqdm import tqdm
    from pandas import DataFrame, Series
    from pandas.core.groupby import DataFrameGroupBy

    # Unit test for function DataFrameGroupBy.progress_apply
    def test_DataFrameProgressApply():
        class DummyDFGroupBy(DataFrameGroupBy):
            pass


# Generated at 2022-06-14 13:05:12.278575
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.tests import FakePandas

    # Setting up fake pandas module
    orig_pd, sys.modules['pandas'] = sys.modules['pandas'], FakePandas()

# Generated at 2022-06-14 13:05:20.287914
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return
    with tqdm_pandas(tqdm(total=1)) as pbar:
        df = pandas.DataFrame([1, 2, 3])
        # The following will be shown on `pbar`:
        df.groupby(df[0]).progress_apply(lambda x: x**2)

# Test for tqdm_pandas function
if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:28.940891
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return

    def afunc(arg):
        return arg / 2

    pd.options.display.max_rows = 7

    with closing(StringIO()) as our_file:
        t = tqdm(total=4, file=our_file)
        t.pandas(desc='pandas loop')
        df = pd.DataFrame({'A': [1, 2, 3, 4]})
        df2 = pd.DataFrame({'A': [5, 6, 7, 8]})
        df3 = pd.DataFrame({'A': [1.5, 2.5, 3.5, 4.5]})

# Generated at 2022-06-14 13:05:39.822176
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    '''
    Unit test for function tqdm_pandas.
    Note:
        1. Run this test with `python -m tqdm.tests.test_pandas`.
        2. It also tests that `tqdm.pandas(bar_format)` returns a
           `tqdm` instance with the `bar_format` set.
    '''
    from tqdm import trange

    # NOTE: we test the `tqdm.pandas(...)` interface
    # and not `tqdm.tqdm_pandas(tqdm, ...)`

    # Function to test pandas
    func = lambda x: x ** 2

    # Check that `tqdm` returns a `tqdm` instance with `bar_format` set

# Generated at 2022-06-14 13:05:47.558065
# Unit test for function tqdm_pandas
def test_tqdm_pandas():  # pragma: no cover
    import pandas as pd
    from tqdm.contrib import DummyTqdmFile

    with tqdm_pandas(DummyTqdmFile()) as t:
        for i in t(pd.DataFrame(pd.util.testing.getSeriesData()).groupby('A', as_index=False)):
            pass

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:59.230685
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, TqdmTypeError

    # Test without arguments
    assert tqdm_pandas == tqdm.pandas

    # Test with tqdm class
    assert tqdm.pandas == tqdm(ascii=True, ncols=80, mininterval=0.1,
                               smoothing=0.3).pandas

    # Test with tqdm instance
    assert tqdm(ascii=True, ncols=80, mininterval=0.1, smoothing=0.3
                ).pandas == tqdm_pandas(tqdm(ascii=True, ncols=80,
                                              mininterval=0.1, smoothing=0.3))

    # Test with wrong arguments
    assert t

# Generated at 2022-06-14 13:06:11.997831
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from pandas import DataFrame

    try:
        from unittest import mock
    except ImportError:
        import mock

    with mock.patch("tqdm.tqdm.pandas") as mocked_pandas_fn:
        for tclass in [tqdm, lambda: tqdm]:
            tqdm_pandas(tclass(), desc="test_tqdm_pandas")
            mocked_pandas_fn.assert_called_with(desc="test_tqdm_pandas")

        df = DataFrame(np.array(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

# Generated at 2022-06-14 13:06:20.219928
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, trange
    from pandas import DataFrame, Series
    import pandas as pd
    import pandas.core.groupby as pandas_gb
    from typing import Dict
    from functools import partial
    from tqdm.auto import tqdm

    def old_map(self, func, *args, **kwargs):
        """
        Map function on group data.
        This is just a call to `.apply` with the arguments reversed.
        Parameters
        ----------
        func : function
        args : positional arguments passed into func
        kwargs : a dictionary of keyword arguments passed into func
        Returns
        -------
        applied : Series or DataFrame
        """
        return self.apply(func, *args, **kwargs)

    pandas_gb.DataFrameGroupBy.map

# Generated at 2022-06-14 13:06:28.340225
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    df = pd.DataFrame({"id": np.arange(10, 20), "val": np.arange(20, 30)})
    assert df[["id", "val"]].groupby(df.id).progress_apply(lambda x: x.id.mean() + x.val.mean()).tolist() == [
        27.5, 28.5, 29.5, 30.5, 31.5, 32.5,
        33.5, 34.5, 35.5, 36.5]

# Generated at 2022-06-14 13:06:32.218219
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    filename = "tqdm_pandas_test.txt"
    tqdm_kwargs = {
        'desc': 'test',
        'total': 4,
        'miniters': 1,
        'ascii': True,
        'bar_format': '{l_bar}{r_bar}',
        'file': open(filename, "w")
    }

# Generated at 2022-06-14 13:06:43.209017
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm.utils import version_check
    from math import floor

    num_rows = 100
    num_cols = 4

    df = pd.DataFrame(
        [[None] * num_cols] * num_rows,
        columns=list('ABCD'),
    )

    # Create a mapping dictionary
    mapping_dict = {
        'A': 'red',
        'B': 'blue',
        'C': 'green',
    }
    mapping_dict.update(dict(zip(mapping_dict.values(), mapping_dict.keys())))

    def f(x):
        return mapping_dict.get(x, x)

    df2 = df.copy()
    df2 = df2.applymap(f)
   

# Generated at 2022-06-14 13:06:54.872561
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.contrib.tests.pandas_v0 import tqdm_pandas_v0
    from tqdm.contrib.tests.pandas_v1 import tqdm_pandas_v1
    import warnings

    try:
        import pandas as pd
        pd_exists = True
    except ImportError:
        pd_exists = False

    # test for pandas >= 0.17
    if pd_exists:
        pd.DataFrame([1]).groupby(0).apply(lambda x: x)
        df = pd.DataFrame([1])
        list(df.groupby(0, observed=True).progress_apply(lambda x: x))  # noqa

# Generated at 2022-06-14 13:07:03.260456
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # define a class, similar to the default tqdm class
    class mytqdm:
        def __init__(self, *args, **kwargs):
            self.n = 0

        def update(self, n=1):
            self.n += n

        @classmethod
        def pandas(cls, **kwargs):
            return pd.DataFrame({'a': [1, 2, 3]}).progress_apply(
                lambda _: None, tqdm_kwargs={'cls': TqdmUpTo,
                                             'params': {'total': 3,
                                                        'mininterval': 0.1,
                                                        'miniters': 1,
                                                        'file': sys.stderr}})

# Generated at 2022-06-14 13:07:08.483048
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import __version__ as version

    assert tqdm_pandas.__doc__ is not None
    with capture_output() as (_, stderr):
        tqdm_pandas(tqdm)

    assert "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`." \
        in stderr.getvalue()
    assert "You have `tqdm==" + version + "`" in stderr.getvalue()

    with capture_output() as (_, stderr):
        tqdm_pandas(tqdm(total=1))


# Generated at 2022-06-14 13:07:17.800520
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm, tqdm_notebook
    from random import choice
    class tqdm(tqdm):
        def __init__(self, *args, **kwargs):
            super(tqdm, self).__init__(*args, **kwargs)
            self.total = 0
            self.prev = 0

        def update_to(*args, **kwargs):
            cur = kwargs.get('n')
            total = kwargs.get('total')
            if self.total != total:
                self.total = total
                self.refresh()
            else:
                self.n = cur
                self.refresh()

        def display(self, *args, **kwargs):
            self.total = kwargs

# Generated at 2022-06-14 13:07:24.602909
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    t = tqdm()
    tqdm_pandas(t)

    try:
        tqdm_pandas(tqdm)
    except Exception:
        pass


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:27.279220
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    t = tqdm(total=10)
    tqdm_pandas(t)
    for i in pd.concat([pd.DataFrame([1])] * 10).progress_apply(lambda x: x):
        pass
    t.close()



# Generated at 2022-06-14 13:07:35.144244
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.randn(100, 100))
    tqdm_pandas(df.apply(lambda x: x.sum()))
    tqdm_pandas(df.apply(lambda x: x.sum(), axis=1))
    tqdm_pandas(df.groupby(range(100)).progress_apply(lambda x: x.sum()))
    tqdm_pandas(df.groupby(range(10)).progress_apply(lambda x: x.sum()))
    tqdm_pandas(df.groupby(range(10)).progress_apply(lambda x: x.sum(), axis=1))

if __name__ == '__main__':
    test_tqdm_p

# Generated at 2022-06-14 13:07:46.518500
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame

    class TqdmTest(tqdm):
        def __init__(self, iterable=None, desc=None, ncols=None, total=None,
                     leave=None, file=None):
            super(TqdmTest, self).__init__(iterable=iterable, desc=desc,
                                           ncols=ncols, total=total,
                                           leave=leave, file=file)
            self.prev = 0

        def update_(self, value):
            self.prev = self.n

    TqdmTest.pandas = tqdm_pandas
    tqdm_test = TqdmTest(total=1000)


# Generated at 2022-06-14 13:07:56.180274
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.contrib import pandas as tp

    # Generate pandas DataFrame
    df = pd.DataFrame({
        'A': np.random.normal(0, 1, size=10000),
        'B': np.random.randint(0, 10, size=10000),
    })
    df_out = df.progress_apply(lambda x: x, axis=1)
    assert df_out.equals(df)
    df = df.sample(frac=1).reset_index(drop=True)
    df_out = df.progress_apply(lambda x: x, axis=1)
    assert df_out.equals(df)

    # Transform tqdm instance to tqdm_pandas instance
    tp.p

# Generated at 2022-06-14 13:08:04.765938
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function `tqdm_pandas`
    """
    from ..std import PandasProgressBar

    df = pd.DataFrame({'X': [1, 2, 3, 4]})
    # Deprecated warning
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm_notebook)
        assert len(w) == 2
    # Compatible warning
    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm, file=sys.stderr)
        assert len(w) == 1
    tqdm_pandas(tqdm)
    df.groupby

# Generated at 2022-06-14 13:08:15.321906
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    _ = DataFrame([[1, 2], [3, 4]]).groupby(0).progress_apply(lambda x: x[1] * 2)

    with tqdm(total=10, leave=False) as t:
        _ = DataFrame([[1, 2], [3, 4]]).groupby(0).progress_apply(
            lambda x: t.update() or x[1] * 2)
    try:
        _ = DataFrame([[1, 2], [3, 4]]).groupby(0).progress_apply(
            lambda x: x[1] * 2)
    except TypeError:
        pass
    else:
        raise ValueError('should throw exception  above')

# Generated at 2022-06-14 13:08:24.984059
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for :func:`tqdm.addons.tqdm_pandas()`."""
    from tqdm.auto import tqdm
    from tqdm import TqdmExperimentalWarning

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", TqdmExperimentalWarning)
        tqdm_pandas(tqdm)

    # deprecated function tqdm_pandas
    with warnings.catch_warnings():
        # ignore all warnings
        warnings.simplefilter("ignore")

        tqdm_pandas(tqdm)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:30.971928
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.auto import tqdm


# Generated at 2022-06-14 13:08:41.483684
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    try:
        import pandas_datareader
    except ImportError:
        print('\nPandas datareader is not installed, skipping tqdm_pandas tests',
              file=sys.stderr)
    else:
        df = pd.DataFrame(pandas_datareader.data.DataReader(
            'SPY', 'yahoo')['Adj Close'])
        try:
            tqdm_pandas(tqdm, desc='test_tqdm_pandas')
        except TypeError:
            print('\nMissing tqdm.pandas, skipping tqdm_pandas tests',
                  file=sys.stderr)

# Generated at 2022-06-14 13:08:53.943174
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm_pandas

    df = pd.DataFrame(np.random.randint(0, 10, (100000, 6)))

    def progress_apply(df, func, **kwargs):
        with tqdm(total=df.shape[0], **kwargs) as t:
            df.progress_apply(lambda x: t.update() or func(x), axis=1)

    # Test on Series
    s = df[0]
    with tqdm(total=s.shape[0]) as t:
        s.progress_apply(lambda x: t.update() or x * x)

    # Test on DataFrame
    with tqdm(total=df.shape[0]) as t:
        df.progress_

# Generated at 2022-06-14 13:09:01.250394
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm_pandas as tp
    from tqdm import tqdm

    df_tqdm = DataFrame(dict(
        id=[1, 2, 3],
        name=['Jacky Jackson', 'Steven Stevenson', 'Lisa Simpson'],
        age=[21, 18, 20],
    ))

    tp(df_tqdm.groupby(['age']).progress_apply(lambda x: x.name.str.split(' ')))

    tp(tqdm(df_tqdm.groupby(['age']).progress_apply(lambda x: x.name.str.split(' '))))

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:12.314863
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    df = pd.DataFrame({'a': [1, 2, 3, 4]})
    df = df.groupby('a').progress_apply(lambda x: x)
    assert df is not None
    df = df.groupby('a')
    with tqdm(total=1, mininterval=0, miniters=1, unit='it') as t:
        df.progress_apply(lambda x: x, t=t)


try:
    from pandas.core.groupby import DataFrameGroupBy
except ImportError:
    pass
else:
    try:
        from pandas.core.groupby import GenericGroupBy
        from pandas.core.groupby import BlockGroupBy
    except ImportError:
        pass

# Generated at 2022-06-14 13:09:23.528837
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas."""
    import tqdm, pandas

    tqdm_pandas(tqdm.tqdm)
    try:
        df = pandas.DataFrame(
            {'A': [1, 2, 3], 'B': [10, 20, 30]},
            index=['a', 'b', 'c'])
        assert df.groupby('A').progress_apply(len) is not None
    except:
        AssertionError("Cannot use tqdm_pandas")

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:27.822598
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    pd.DataFrame.sum = progress_apply(pd.DataFrame.sum, desc="TESTING")
    try:
        tqdm_pandas(pd.DataFrame.sum)
        assert True
    except:
        assert False

# Generated at 2022-06-14 13:09:38.963734
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, TqdmTypeError
    import pandas as pd

    # Register `tqdm` with `pandas.DataFrameGroupBy.progress_apply`
    tqdm_pandas(tqdm)
    # Create a `pandas.DataFrame` instance
    df = pd.DataFrame({'col': [1, 2, 3, 4]})
    # Group by the `'col'` column and call `progress_apply` on the result
    list(df.groupby('col')['col'].progress_apply(lambda x: x))

    try:
        tqdm_pandas(tqdm, file=6)
    except TqdmTypeError:
        # TqdmTypeError is raised as expected
        pass
    else:
        raise Assert

# Generated at 2022-06-14 13:09:45.039308
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, read_csv
    tqdm_pandas(tqdm, unit_scale=True)
    df = DataFrame()
    df['data'] = read_csv('/etc/passwd', delimiter=':')['root']
    df['val'] = df['data'].progress_apply(len)
    assert df['val'][0] == 4
    df['val'] = df['data'].progress_apply(len)
    assert df['val'][0] == 4

# Generated at 2022-06-14 13:09:46.591554
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)



# Generated at 2022-06-14 13:09:53.130659
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import random
    import tqdm
    n = random.randint(100, 200)
    df = pd.DataFrame(np.random.randn(n, n))
    # 1. tqdm
    tqdm.pandas(desc="tqdm_pandas")
    df.progress_apply(lambda x: sum(x))
    df.progress_apply(lambda x: sum(x), axis=1)
    # 2. tqdm
    tqdm.pandas(desc="tqdm_pandas")
    for _, df_group in df.groupby(df.index // 10):
        df_group.progress_apply(lambda x: sum(x))

# Generated at 2022-06-14 13:10:04.691031
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    try:
        from pandas.core.groupby import DataFrameGroupBy
    except ImportError:
        from pandas.core.groupby import GroupBy as DataFrameGroupBy

    df = pd.DataFrame(np.random.randint(0, 1e6, 100))
    df['int'] = np.random.randint(-100, 100, 100)
    #print(df)

    @tqdm.tqdm(total=len(df))
    def my_func(x):
        return x * 2


# Generated at 2022-06-14 13:10:19.334687
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function ``tqdm_pandas``
    """
    from tqdm import tqdm
    from tqdm.contrib.concurrent import DummyTqdmFile
    from tqdm.contrib.concurrent import thread_map, process_map

    with DummyTqdmFile() as f:
        tqdm_pandas(tqdm(file=f))
        thread_map(tqdm_pandas, [tqdm(file=f)] * 5)
        process_map(tqdm_pandas, [tqdm(file=f)] * 5)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:31.754101
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:10:39.917799
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    df = pd.DataFrame({'C': [1, 2, 3, 4, 5, 6], 'D': [11, 12, 13, 14, 15, 16]})
    tqdm_pandas(tqdm)
    df.groupby('C').progress_apply(lambda x: x**2)
    tqdm_pandas(tqdm(desc="test"), desc="test")
    df.groupby('C').progress_apply(lambda x: x**2)
    tqdm_pandas(tqdm(desc="test"), desc="test")
    df.groupby('C').progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:10:48.012569
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
        from tqdm import tqdm_notebook as tn

        df = pd.DataFrame({'a': range(100)})

        # old style
        tqdm_pandas(tn)
        assert(df.groupby('a').progress_apply(lambda x: x).equals(df))

        # new style
        tqdm_pandas(tn())
        assert(df.groupby('a').progress_apply(lambda x: x).equals(df))
    except ImportError:
        pass

# Generated at 2022-06-14 13:10:58.895573
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError as e:
        print('Please install pandas to test tqdm_pandas: {}'.format(e))
        return None
    try:
        from tqdm import tqdm_pandas
    except ImportError as e:
        print('Please install tqdm to test tqdm_pandas: {}'.format(e))
        return None
    from tqdm import trange

    def my_power(x, n=2):
        time.sleep(0.1)
        return x ** n


# Generated at 2022-06-14 13:11:07.978049
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Import and check for errors
    import pandas as pd
    from tqdm.auto import tqdm
    from tqdm.contrib import pandas as tqdm_pd

    # Setup test objects
    df = pd.DataFrame({'col': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    df_r = pd.DataFrame({'col': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

    # Simple groupby
    df.groupby('col').progress_apply(lambda x: x, t=tqdm_pd)

    # Groupby with multiple columns
    df.groupby(['col', 'col']).progress_apply(lambda x: x, t=tqdm_pd)

    # Groupby

# Generated at 2022-06-14 13:11:18.178879
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from .tests import size, decorator

    # Testing without decorator case
    for i in range(2):
        with tqdm(total=size, **decorator.kwargs) as pbar:
            @tqdm_pandas(pbar)
            def f(x):
                return x
            df = pd.DataFrame(dict(x=range(size)))
            df.groupby(0).progress_apply(f)
        pbar.close()

    # Testing with decorator case
    with tqdm(total=size, **decorator.kwargs) as pbar:
        @tqdm_pandas(pbar)
        def f(_):
            return _

# Generated at 2022-06-14 13:11:28.646591
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    np.random.seed(seed=8)
    df = pd.DataFrame(np.random.random((50, 20)), columns=['a', 'b', 'c',
                                                           'd', 'e', 'f',
                                                           'g', 'h', 'i',
                                                           'j', 'k', 'l',
                                                           'm', 'n', 'o',
                                                           'p', 'q', 'r',
                                                           's', 't'])

    # test whether progress_apply yields the same result as apply
    assert_frame_equal(
        df.groupby('a')[['b', 'c']].progress_apply(sum),
        df.groupby('a')[['b', 'c']].apply(sum))

