

# Generated at 2022-06-14 13:01:42.384087
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from numpy.random import randn
    from pandas import DataFrame
    from tqdm import tqdm, tqdm_notebook, trange
    from itertools import product

    def add1(x):
        from time import sleep
        sleep(0.01)
        return x + 1


# Generated at 2022-06-14 13:01:47.866140
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import sys
    import tqdm
    from tqdm import TqdmDeprecationWarning

    def check_output(out, expected):
        import re
        out = re.sub(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', 'YYYY-MM-DD', out)
        assert out == expected

    # Delayed tqdm case:
    with tqdm.tests.nested(
            stdout=tqdm.tests.StringIO(),
            stderr=tqdm.tests.StringIO()) as (out, err):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            tqdm_pandas(tqdm.tqdm)
        assert len(w) == 1

# Generated at 2022-06-14 13:01:54.657920
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])

    tqdm_pandas(tqdm)

    def f(df):
        return df

    df.groupby('a').progress_apply(f)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:00.674540
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    import tqdm
    with tqdm.tqdm_pandas(total=len(df)) as t:
        df.progress_apply(lambda dummy: t.update())
    return True

# Generated at 2022-06-14 13:02:10.226486
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    df = pd.DataFrame({'a': np.random.randn(100),
                       'b': np.random.randint(100, size=100)})

    def tqdm_ex_func(x):
        # Just to make it non-trivial
        import math
        import time
        time.sleep(0.5)
        x['b'] = math.sqrt(x['b'])
        return x

    df.groupby('b').apply(tqdm_pandas(tqdm.tqdm,
                                      desc='testing pandas apply'))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:15.974557
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    n = 100
    df = pd.DataFrame({'A': list(range(n)),
                       'B': list(range(n)),
                       'C': list(range(n))})

    df.groupby('A').B.progress_apply(lambda x: x + 3).compute()


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:23.177577
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for the function `tqdm_pandas`.
    """
    from tqdm import tqdm

    def assert_in(st, fname, hash_str=False):
        """
        Asserts that `st` is in the contents of file `fname`.
        """
        import os
        import hashlib
        with open(fname, "r") as f:
            contents = f.read()
            if hash_str:
                contents = hashlib.sha256(contents.encode()).hexdigest()
            assert st in contents, "'{}' not found in file {}" \
                .format(st, fname)
        os.unlink(fname)  # Cleanup

    # Test function itself
    tqdm_pandas(tqdm)

    # Test

# Generated at 2022-06-14 13:02:33.224045
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # To check whether the tqdm_pandas() function can be called
    # by both the old style and the new style.
    # The old style is deprecated, but we still have to make it work.
    from tqdm import tqdm

    try:
        # old style
        tqdm_pandas(tqdm, ascii=True)
    except TypeError:
        raise

    try:
        # new style
        with tqdm(ascii=True, leave=False) as t:
            tqdm_pandas(t)
    except TypeError:
        raise


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:43.574800
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import trange
    from tqdm.auto import tqdm

    # Test compatibility with pandas v0.19.x and v0.20.x
    if hasattr(pd, '__version__') and pd.__version__.startswith('0.19'):
        pd.core.groupby.DataFrameGroupBy.progress_apply = tqdm_pandas(tqdm)
    else:
        tqdm_pandas(tqdm)

    # tqdm.pandas(**tqdm_kwargs) does not support nested progressbars
    # and progressbars with leave=True so that the following code is for testing
    # the tqdm_pandas function only

# Generated at 2022-06-14 13:02:50.975765
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm, trange
    from tqdm.pandas import tqdm_pandas

    data = pd.DataFrame({"a": np.random.randint(0, 10, size=100)})

    # Line below is equivalent to:
    # @tqdm_pandas
    # def groupby(df):
    #     return df.groupby("a").count()
    groupby = tqdm_pandas(tqdm(total=None, leave=False))(
        data.groupby("a").count)

    data = pd.DataFrame({"a": np.random.randint(0, 10, size=100)})

    # Line below is equivalent to:
    # @tqdm

# Generated at 2022-06-14 13:03:03.156727
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas as pd

    # test old-style
    t = tqdm.tqdm
    tclass = t()
    tqdm_pandas(tclass)
    assert tclass.get_lock() is t.get_lock()

    # test new-style
    t = tqdm.tqdm
    tclass = t(disable=True)
    tqdm_pandas(tclass)
    assert tclass._instances == []
    assert tclass.get_lock() is t.get_lock()

    # test delayed
    tclass = tqdm.tqdm
    tqdm_pandas(tclass)
    assert tclass._instances == []
    assert tclass.get_lock() is t.get_lock()

    df = p

# Generated at 2022-06-14 13:03:10.897410
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    import pandas as pd
    df = pd.DataFrame({"a": ["a"] * 100000})
    tqdm.pandas(unit="rows")  # initializes default
    assert "pandas" in tqdm.tqdm.__module__
    assert "unit" in tqdm.tqdm.default_kwargs
    assert tqdm.tqdm.default_kwargs['unit'] == "rows"


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:24.149419
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    from tqdm import tqdm
    from tqdm.auto import trange

    # timeit.timeit('pd.read_csv(r"C:\Users\A\Desktop\dataset_train.csv")',number=100,globals=globals())
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm.tqdm)
    tqdm_pandas(trange)

    # with named kwargs
    tqdm()
    tqdm(file=sys.stdout)
    pd.read_csv(r"C:\Users\A\Desktop\dataset_train.csv").progress_apply(
        lambda x: sum(map(int, x[0].split('_'))))

   

# Generated at 2022-06-14 13:03:31.839758
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    from tqdm import tqdm, tqdm_pandas

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))

    tqdm_pandas(tqdm())   # can use tqdm_gui, optional kwargs, etc

    # Now you can use `progress_apply` instead of `apply`
    # and `progress_map` instead of `map`
    df.groupby(0).progress_apply(lambda x: x**2)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:40.747678
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Test all modes
    list(map(tqdm_pandas, [tqdm_gui, tqdm_notebook, tqdm_pandas, tqdm]))
    # Test functionality
    try:
        import pandas as pd
    except ImportError:
        print('test_tqdm_pandas skipped because pandas not found')
        # Test delayed adapter
    tqdm_pandas(tqdm)
    tqdm_kwargs = {'desc': 'test', 'bar_format': 'test %s'}
    from tqdm.contrib.tests.pandas_tests import df as pd_df

# Generated at 2022-06-14 13:03:50.848089
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas"""
    # Test "tqdm_pandas(tqdm(...))"
    from tqdm.auto import tqdm
    t = tqdm(total=1000)
    with closing(t):
        tqdm_pandas(t)
        for i in t:
            pass

    # Test "tqdm.pandas(tqdm_foo(...))"
    from tqdm.contrib.concurrent import process_map
    t = process_map(tqdm, range(1000), total=1000)
    with closing(t):
        tqdm_pandas(t)
        for i in t:
            pass



# Generated at 2022-06-14 13:04:01.129789
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
    except ImportError:
        raise SkipTest

    df = pd.DataFrame(
        {'a': [1, 2, 3], 'b': [4, 5, 6]},
        index=pd.MultiIndex.from_product(
            (np.arange(99999), np.arange(9999))))
    df.groupby('a').progress_apply(lambda x: x)
    df.groupby('a').progress_apply(lambda x: x, meta='m')
    df.groupby('a').progress_apply(lambda x: x, meta={'m': 'm'})
    df.groupby('a').progress_apply(lambda x: x, meta={'mi': 'm'})


#-----------------------------------------------------------------------------
# Copyright (C)

# Generated at 2022-06-14 13:04:08.621883
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from tqdm import tqdm
        from tqdm.contrib import pandas
    except ImportError:
        try:
            from tqdm.auto import tqdm
            from tqdm.auto.contrib import pandas
        except ImportError:
            return
    import pandas as pd
    df = pd.DataFrame({'a': [1] * 3 + [2] * 5 + [3] * 2})
    res = df.groupby('a').progress_apply(lambda x: x)
    assert set(df['a']) == set(res['a'])

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:13.655415
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return

    tqdm_pandas(tqdm(bar_format='{desc}'))
    df = pd.DataFrame({'a': range(100), 'b': range(100), 'x': range(100)})
    assert list(df.groupby('a').progress_apply(lambda x: x ** 2))[0].x.tolist() == \
           list(df.groupby('a').apply(lambda x: x ** 2))[0].x.tolist()

# Generated at 2022-06-14 13:04:23.888977
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm.pandas import tqdm_pandas
    from tqdm.auto import tqdm

    # Assert that the adapter for the tqdm class is working
    df = DataFrame(dict(a=[0, 0, 1, 1, 2, 2], b=[0, 1, 1, 0, 0, 1]))
    tqdm.pandas()
    df.groupby('a').progress_apply(lambda x: x)

    # Assert that the adapter for the TqdmDeprecationWarning is working
    tqdm_pandas(tqdm)

    # Assert that the adapter for the TqdmDeprecationWarning is working
    # with the alias (sincethe 1.0.0 release of tqdm_notebook)
    tq

# Generated at 2022-06-14 13:04:38.861939
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    import copy
    import warnings

    # Delayed adapter case
    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm)
    assert w[0].category == tqdm.TqdmDeprecationWarning
    assert 'Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.' in str(w[0].message)

    # Non-delayed adapter case

# Generated at 2022-06-14 13:04:41.931119
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    from numpy import random
    df = pd.DataFrame(random.randn(10000, 3))
    tqdm_pandas(tqdm(total=len(df)), show=False)(df.apply)(lambda x: x)

# Generated at 2022-06-14 13:04:53.089421
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    import tqdm
    import tqdm.pandas

    # Generate DataFrame
    np.random.seed(0)
    df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
                      index=['falcon', 'dog'])
    df2 = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
                      index=['falcon', 'dog'])

    # Tests
    total = float(len(df))

    # Test 1: progress_apply with `pandas`
    # tqdm.pandas.tqdm_pandas(df)
    tqdm.pandas.tqdm

# Generated at 2022-06-14 13:05:03.654238
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    from pandas.util.testing import assert_frame_equal

    df = pd.DataFrame({
        'a': list(range(90)),
        'b': list(range(90))
    })

    def square(x):
        return x*x

    def process(df):
        return pd.concat(
            [
                df, df.groupby(['b'])
                .progress_apply(square)
                .rename(columns={'a': 'a_squared'})
            ],
            axis=1
        )

    df_with_tqdm = process(df).pipe(tqdm_pandas, total=df.shape[0])
    df_without_tqdm = process(df)

    # dropped index column

# Generated at 2022-06-14 13:05:16.382881
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm
    from numpy.random import randint

    df = DataFrame([randint(0, 42, size=42) for _ in range(42)],
                   columns=list('abcdefghijklmnopqrstuvwxyzABCDEF')).set_index('a')

    df.groupby('f').progress_apply(lambda x: x.sum())

    with tqdm(total=42) as t:
        def progress_apply_handler(args, kwargs):
            t.update()

        df.groupby('f').progress_apply = progress_apply_handler
        df.groupby('f').progress_apply(lambda x: x.sum())

    with tqdm(total=42, miniters=1) as t:
        df

# Generated at 2022-06-14 13:05:26.693295
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_pandas
    import pandas as pd
    x = pd.DataFrame(dict(a=list('abcdefghijklmnopqrst')))
    tqdm_pandas(tqdm(leave=False))
    results = x.groupby('a').progress_apply(len)


try:
    from pandas import DataFrame, Series, Panel
except ImportError:
    pass
else:
    # Adapted from https://github.com/bstriner/keras-tqdm
    def tqdm_proxy(*args, **kwargs):
        """
        Creates a `pandas.core.groupby.DataFrameGroupBy.progress_apply`-compatible
        progress bar decorator for `apply` methods.
        """
        #

# Generated at 2022-06-14 13:05:33.012889
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import subprocess
    import os
    from tqdm import tqdm
    from .tqdm import tqdm_pandas

    # Test 1
    tqdm_pandas(tclass=tqdm)

    # Test 2
    tqdm_pandas(tclass=tqdm())

    # Test 3
    tqdm_pandas(tclass=tqdm, file=sys.stderr)

    # Test 4
    null = open(os.devnull, 'w')
    tqdm_pandas(tclass=tqdm, file=null)
    null.close()

    # Test 5
    t = tqdm()
    tqdm_pandas(tclass=t)

    # Test 6

# Generated at 2022-06-14 13:05:34.546963
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    t = tqdm_pandas(tqdm())

# Generated at 2022-06-14 13:05:46.825379
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Tests that tqdm_pandas() actually works"""
    import pandas as pd
    import numpy as np
    import gc
    from time import sleep

    # Create dummy data frame
    df = pd.DataFrame(np.random.rand(100000, 10))

    # Use TqdmUpTo to make sure that memory footprint stays the same:
    #  * `max_iter` - to specify total number of iterations
    #  * `lock_args` - to ensure parameters do not change during iteration
    t = tqdm(total=len(df), lock_args=False, disable=False)
    t.pandas(total=len(df), unit='row', leave=False)

    # Perform test
    len(df.apply(lambda x: sleep(0.000001), axis=1))


# Generated at 2022-06-14 13:05:50.762038
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    import tqdm

    def f(df):
        time.sleep(.01)
        return df

    df = pd.DataFrame(np.random.randn(100, 3), columns=list('ABC'))
    tqdm.pandas(tqdm.tqdm())
    f(df)
    assert isinstance(df.progress_apply(f), pd.DataFrame)

# Generated at 2022-06-14 13:06:10.011273
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Test of the tqdm_pandas() function.
    """

# Generated at 2022-06-14 13:06:18.800001
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas."""
    from functools import partialmethod

    with catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        tqdm_pandas(tqdm)
        assert len(w) == 1
        assert "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`." \
            in str(w[-1].message)

    assert isinstance(DataFrameGroupBy.progress_apply, partialmethod)

    with catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        tqdm_pandas(tqdm(total=1))
        assert len(w) == 1

# Generated at 2022-06-14 13:06:30.174786
# Unit test for function tqdm_pandas
def test_tqdm_pandas():  # pragma: no cover
    from .tests import pandas_fixture  # pragma: no cover
    from warnings import catch_warnings  # pragma: no cover

    assert not hasattr(pandas_fixture.df, 'progress_apply')

    with catch_warnings(record=True) as w:
        tqdm_pandas(tclass=pandas_fixture.tqdm_class)
        assert len(w) == 0

    def mysum(x):
        return (x + 1).sum(axis=1)


# Generated at 2022-06-14 13:06:38.190848
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm_notebook as tqdm
    from functools import reduce
    from random import randint as ri
    from operator import or_
    import numpy as np
    print('doctest in progress')
    # Unit test
    print('test 1: SeriesGroupBy.progress_apply')
    df = DataFrame({'col_1': [ri(0, 10) for _ in range(1000)]})
    df.groupby('col_1').progress_apply(lambda x: 1)
    print('test 2: DataFrameGroupBy.progress_apply')
    df.groupby('col_1').progress_apply(lambda x: x)
    print('test 3: DataFrame.progress_apply')

# Generated at 2022-06-14 13:06:42.793239
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        return True
    except ImportError:
        return None

    # Empty test (because it is a decorator)
    # TODO: integrate in global unit tests
    return True


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:47.409780
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    from random import randint
    from time import sleep

    rows = 32
    df = DataFrame([[randint(0, 100) for _ in range(4)] for _ in range(rows)])
    df.progress_apply(lambda x: sleep(.01))

# Generated at 2022-06-14 13:06:58.423586
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas import DataFrame
    from pandas import Series
    from tqdm import tqdm
    from tqdm import tqdm_notebook


# Generated at 2022-06-14 13:07:05.245032
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    [tqdm_pandas(t) for t in [
        tqdm_pandas, tqdm.tqdm_pandas, tqdm.pandas, tqdm]]

    # Regression test for #446: no error for empty DataFrame
    pd.DataFrame().groupby('a').progress_apply(lambda x: x)
    pd.DataFrame().progress_apply(lambda x: x)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:11.323462
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm._tqdm import tqdm

    for t in (tqdm, tqdm(0, leave=True, disable=True)):
        tqdm_pandas(t)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:19.316243
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm)

    try:
        import numpy as np
    except ImportError:
        return

    irange = range(100)
    df = DataFrame({'a': np.random.randint(-100, 100, len(irange)),
                    'b': np.random.random(len(irange))})

    # Test pandas integration with tqdm_notebook
    try:
        from tqdm import tqdm_notebook
    except ImportError:
        return

    tqdm_notebook().pandas(desc='test', leave=True)
    (df + 1).groupby(0).progress_apply(lambda x: x)

# Generated at 2022-06-14 13:07:34.680338
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, trange  # NOQA
    from pandas import DataFrame, Series  # NOQA

    try:
        import pandas as pd
        import numpy as np
    except ImportError:
        # No pandas installed, exit
        return

    with trange(1) as t:
        try:
            df = DataFrame([1, 2, 3])
            df.groupby(df[0]).progress_apply(lambda x: x)
        except (AttributeError, NameError):
            return

        # Testing delayed adapter
        tqdm_pandas(tclass=tqdm)
        df.groupby(df[0]).progress_apply(lambda x: x)

        # Testing old-style

# Generated at 2022-06-14 13:07:39.263553
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas import Series
    from tqdm import tqdm
    from tqdm.contrib import pandas as tqdm_pandas_
    from tqdm.contrib.tests import df, series

    tqdm_pandas_(tqdm)
    DataFrame(df).groupby('A').progress_apply(lambda x: x)
    Series(series).groupby(series).progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:48.878165
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test whether tqdm_pandas function is working properly
    """
    try:
        import pandas as pd
    except ImportError:
        return
    else:
        from tqdm.auto import tqdm

        tqdm.pandas(tqdm)

        df = pd.DataFrame({'values': range(10)})
        result = df.groupby(df['values'] % 2).progress_apply(lambda x: x)
        assert isinstance(result, pd.DataFrame)


test_tqdm_pandas()

# Generated at 2022-06-14 13:07:54.115763
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    try:
        tqdm_pandas(tqdm)
    except Exception as e:
        print(e)
        return False
    else:
        return True

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:58.905903
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    max_len = 100
    with tqdm.pandas(total=max_len, smoothing=0) as pbar:
        (pd.DataFrame(np.random.randint(0, 100, (1000, 6)))
         .progress_apply(lambda x: x ** 2))

# Generated at 2022-06-14 13:08:06.309281
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from numpy import arange
    from tqdm import tqdm


# Generated at 2022-06-14 13:08:16.523167
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from numpy import random
    from tqdm import tqdm
    from random import shuffle

    # Initialize a test DataFrame
    df_test = DataFrame(data={'A': [random.randint(-100, 100) for _ in range(100)],
                              'B': ['test' for _ in range(100)]})
    df_test = df_test.astype(dtype={'A': 'float32', 'B': 'str'})

    df_test = df_test.groupby('B')
    df_test.progress_apply = tqdm(desc='Test', leave=True, ascii=True,
                                  total=df_test.size())
    df_test.progress_apply(sum)  # Sum within group
    df_test.progress_

# Generated at 2022-06-14 13:08:23.859904
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    tqdm_pandas(pandas)
    tqdm_pandas(pandas.core.groupby.DataFrameGroupBy)

    with pandas.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        df = pandas.DataFrame({'a': list(range(100))})

        df.groupby('a').progress_apply(lambda x: x)

# Generated at 2022-06-14 13:08:30.212821
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Test that the tqdm_pandas function is working properly.

    Test by calling it with a few options beginning with the name 'file'
    and check that it is properly executed.

    """
    import io

    # Testing a function call
    tqdm_pandas(tqdm_pandas(
        tqdm(total=1, file=io.StringIO('test')), file=io.StringIO('test')))



# Generated at 2022-06-14 13:08:36.107685
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import trange

    df = pd.DataFrame({'a': range(int(1e4))})

    with trange(10) as t:
        df.groupby('a').progress_apply(lambda _: t.update())


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:59.709328
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from tqdm import tqdm, tqdm_notebook

    df = DataFrame({'a': Series(list('abcde')),
                    'b': Series(range(5, 0, -1))},
                   index=['a', 'b', 'c', 'd', 'e'])
    tqdm_pandas(tqdm)
    assert isinstance(df.groupby('b').progress_apply(lambda x: x),
                      DataFrame)
    assert isinstance(df.groupby('b').progress_apply(lambda x: x),
                      DataFrame)
    tqdm_pandas(tqdm_notebook)
    assert isinstance(df.groupby('b').progress_apply(lambda x: x),
                      DataFrame)

# Generated at 2022-06-14 13:09:11.342686
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from tqdm import trange
    except ImportError:
        return
    from tqdm import tqdm
    from time import sleep

    for n in trange(4, leave=False):
        for i in tqdm(range(10), desc='2nd loop', leave=False):
            for j in tqdm(range(100), desc='3rd loop', leave=False):
                sleep(0.01)

    df = pd.DataFrame(
        {'col1': np.random.randn(1000), 'col2': np.random.randn(1000)})
    a = df.progress_apply(tqdm, axis=1)

if __name__ == '__main__':
    try:
        from pandas import DataFrame, Series
    except ImportError:
        raise Runtime

# Generated at 2022-06-14 13:09:23.984154
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    from tqdm._utils import _deprecate_module, _supplementary_tqdm as tqdm
    from tqdm import TqdmDeprecationWarning
    from pandas import DataFrame
    from pandas.util.testing import assert_frame_equal

    with TqdmDeprecationWarning():
        # Regular tqdm function
        with tqdm(total=10, desc='TESTTQDM', leave=True) as t:
            df = DataFrame({
                'A': range(10),
                'B': [{i: i} for i in range(10)]
            })

# Generated at 2022-06-14 13:09:26.410652
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm, desc='Testing tqdm_pandas...')

# Generated at 2022-06-14 13:09:37.949078
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm, tnrange

    df = pd.DataFrame({'A': np.random.randint(0, 1000, size=1000),
                       'B': np.random.randint(0, 1000, size=1000)})
    # tqdm_pandas(tnrange(10), desc='test')  # tnrange does not work
    # tqdm_pandas(tqdm(total=10), desc='test')   # this works
    # tqdm_pandas(tqdm(total=10))   # this works
    tqdm_pandas(color='red')
    result = df.groupby('B').progress_apply(lambda x: x['A'].sum())
    result.head

# Generated at 2022-06-14 13:09:47.063743
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    import warnings
    from tqdm import tqdm
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    pandas_version = int(''.join(map(str, pd.__version__.split('.'))))
    df = pd.DataFrame({'test': list(map(str, range(100))),
                       'test2': list(map(str, range(100, 200))),
                       'test3': list(map(str, range(200, 300))),
                       'test4': list(map(str, range(300, 400)))})

    def test_time(x):
        time.sleep(0.01)


# Generated at 2022-06-14 13:09:50.322740
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    with tqdm_pandas(total=10) as pbar:
        pd.DataFrame({"a": range(10)}).groupby("a").progress_apply(lambda x: x)
    assert pbar.n == 10

# Generated at 2022-06-14 13:10:02.225456
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.pandas import tqdm_pandas
    from tqdm import tqdm

    @tqdm_pandas
    def f(df, a=1, b=4):
        for k, _ in df.iterrows():
            df.loc[k, 'col'] = k * b + a + np.random.randn() > 0
        return df

    df = pd.DataFrame({'col': [-3, -2, -1, 0, 1]}, index=range(5))
    f(df)


# Generated at 2022-06-14 13:10:09.644259
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas, tqdm
    pd = pytest.importorskip('pandas')
    import pandas.core.groupby

    def _tqdm_pandas():
        pd.DataFrame([[1, 2], [3, 4], [5, 6]]).groupby(0).progress_apply(sum)

    tqdm_pandas()
    _tqdm_pandas()
    tqdm_pandas(pandas=True)
    _tqdm_pandas()
    tqdm_pandas(tqdm_class=tqdm)
    _tqdm_pandas()
    tqdm_pandas(tqdm)
    _tqdm_pandas()
    tq

# Generated at 2022-06-14 13:10:20.487391
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame({'col_1': np.random.randint(0, 100, size=1000)})

    def f(df):
        import time
        time.sleep(0.1)
        return df['col_1'] * 2

    # old version
    tqdm_pandas(tqdm)
    pbar = tqdm(total=len(df), desc='Old version')
    df.progress_apply(f, axis=1, args=(pbar,))
    pbar.close()
    # new version
    pbar = tqdm_pandas(df, total=len(df), desc='New version')

# Generated at 2022-06-14 13:10:57.367874
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # The following just tests that the statement below doesn't raise
    # TypeError as it would if the deprecated version of tqdm_pandas
    # was used.
    try:
        tqdm_pandas(tqdm())
    except TypeError:
        raise TypeError(
            'Deprecated version of tqdm_pandas() must be used. '
            'Make sure the tqdm version is < 4.26.0.')


import pandas as pd
from pandas.core.generic import NDFrame
from pandas.core.groupby.groupby import DataFrameGroupBy, SeriesGroupBy
from pandas.core.window.rolling import _Rolling_and_Expanding

# Type checks for deprecated functions

# Generated at 2022-06-14 13:11:06.413889
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    import tqdm
    from tqdm import TqdmExperimentalWarning

    df = pd.DataFrame([np.random.randint(0, 2, size=10000)
                       for i in range(10)]).T

    # with warning
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', TqdmExperimentalWarning)
        res = df.groupby(0).progress_apply(lambda x: x.sum())
    assert (res == df.sum()).all().all()

    # without warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', TqdmExperimentalWarning)
        warnings.simplefilter('ignore', TqdmDeprecationWarning)
        res = df.groupby(0).progress_apply

# Generated at 2022-06-14 13:11:16.942806
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Create dummy data for unit testing
    import pandas as pd
    np.random.seed(1)
    n = 100000
    cols = ['col_{}'.format(i) for i in range(10)]
    df = pd.DataFrame({c: np.random.randint(0, 100, n) for c in cols})
    # Test it
    import tqdm

    # monkey-patching !!!
    tqdm.pandas(tqdm.tqdm())
    # redundant but we need to check that the newly added method exists
    assert hasattr(pd.DataFrame.progress_apply, '__wrapped__')
    assert 'default' in df.progress_apply(lambda x: x, axis=1)
    # Test if tqdm_pandas works
    t = tq

# Generated at 2022-06-14 13:11:24.015906
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy

    def progress_apply_wrapper(*args, **kwargs):
        return DataFrameGroupBy.progress_apply(type(t).__name__,
                                               self=kwargs['self'],
                                               func=kwargs['func'],
                                               *args,
                                               **kwargs)

    df = DataFrame({'col1': [1, 2, 3] * 100,
                    'col2': [4, 5, 6] * 100})
    for t in [tqdm, tqdm_notebook, tqdm_gui, trange]:
        tqdm_pandas(t)
        assert progress_apply_wrapper != DataFrameGroupBy.progress_apply

# Generated at 2022-06-14 13:11:34.584023
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series, date_range
    from pandas.core.common import _ENABLE_MULTI_PROCESSING
    _ENABLE_MULTI_PROCESSING = False

    from tqdm import tqdm
    from tqdm._utils import _range
    from tqdm.contrib import DummyTqdmFile, dummy_func
    from tqdm.utils import _term_move_up
    from tqdm.std import TqdmFile

    n_epochs = n_series = n_tuples = 2
    dtype_epoch = int
    dtype_series = str
    dtype_tuple = float
    t_epoch = tqdm(range(n_epochs), dtype=dtype_epoch, desc='Epoch')
   