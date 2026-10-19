

# Generated at 2022-06-14 13:01:36.849117
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        from tqdm import tqdm, tqdm_notebook, tqdm_gui, trange

        for _t in (tqdm, tqdm_notebook, tqdm_gui, trange):
            pd.DataFrame(range(10)).progress_apply(_t)
        assert True  # success
    except Exception as e:
        print(e)
        assert False  # failure



# Generated at 2022-06-14 13:01:42.814533
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm
    tqdm_pandas(tclass=tqdm.tqdm(ncols=80, desc="test pandas"))


if __name__ == '__main__':
    """
    test the function tqdm_pandas
    """
    test_tqdm_pandas()

# Generated at 2022-06-14 13:01:48.690001
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame({'a': range(10)})
    tqdm_pandas(tqdm())
    df.groupby('a').progress_apply(lambda x: x.sum)
    tqdm_pandas(tqdm(desc='testing'))
    df.groupby('a').progress_apply(lambda x: x.sum)



# Generated at 2022-06-14 13:01:53.582145
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.contrib import pandas
    from pandas import DataFrame
    import pandas as pd
    import numpy as np

    a = np.random.rand(100, 100)
    b = np.random.rand(100, 100)
    df = DataFrame({
        'a': np.average(a, 1),
        'b': np.average(b, 1),
        'c': np.average(a + b, 1)
    })
    tqdm_pandas(pandas)
    assert isinstance(df.groupby('c').progress_apply(lambda x: x), pd.core.groupby.DataFrameGroupBy)

# Test for the deprecated format of tqdm_pandas

# Generated at 2022-06-14 13:02:00.772288
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas

        def gen():
            for i in range(200):
                yield i, i * i, i * i * i

        tqdm_pandas(tqdm())
        pandas.DataFrame(gen()).groupby(0).progress_apply(
            lambda x: x[1] + x[2] + x[0])
    except Exception:
        print("Cannot test tqdm_pandas", file=sys.stderr)
        return
    print("Test passed !")

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:09.993739
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import unittest
    import tqdm
    import pandas
    rows = 10
    cols = 100
    x = np.random.randn(rows, cols)
    dx = pd.DataFrame(x)
    y = dx.apply(tqdm.tqdm, axis=0, desc='cols', **tqdm.__dict__)
    assert np.allclose(y.values, x)
    y = dx.progress_apply(tqdm.tqdm, axis=0, desc='cols', **tqdm.__dict__)
    assert np.allclose(y.values, x)

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:19.506494
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm

    tqdm_pandas(tqdm._tqdm_gui)
    tqdm_pandas(tqdm.tqdm)

    with pytest.raises(tqdm.TqdmDeprecationWarning, match=r"Please use `tqdm.pandas\(\.\.\.\)` instead of `tqdm_pandas\(tqdm, \.\.\.\)`."):
        tqdm_pandas(tqdm.tqdm, file=sys.stderr)

# Generated at 2022-06-14 13:02:31.329152
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    # pylint: disable=undefined-variable
    import pandas, pandas._libs.groupby  # noqa
    # pylint: enable=undefined-variable
    import tqdm
    var = pandas.Series(range(10000))

    # Test calc()
    tqdm_pandas(tqdm.tqdm, desc='test')
    var.groupby(var).progress_apply(lambda x: x)

    # Test eval()
    tqdm_pandas(tqdm.tqdm, desc='test')
    var.groupby(var).progress_apply(lambda x: x)

    # Test apply()

# Generated at 2022-06-14 13:02:41.874248
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with warnings.catch_warnings(record=True) as ws:
        warnings.resetwarnings()  # should not be necessary, but just in case
        tqdm_pandas(tqdm)
    assert len(ws) == 1
    assert 'Please use `tqdm.pandas(...)`' in str(ws[0].message)

    with warnings.catch_warnings(record=True) as ws:
        warnings.resetwarnings()  # should not be necessary, but just in case
        tqdm_pandas(tqdm(ascii=True))
    assert len(ws) == 1
    assert 'Please use `tqdm.pandas(...)`' in str(ws[0].message)


# Generated at 2022-06-14 13:02:49.927967
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm_pandas
    import pandas as pd
    from tqdm import tqdm
    from tqdm._utils import _term_move_up

    # Test df.apply
    df = pd.DataFrame({'a': [4, 5, 6], 'b': [1, 2, 3]})

    # deprecated
    tqdm_pandas(tqdm(total=df.shape[0]))
    df.progress_apply(lambda x: x)
    sys.stderr.write(_term_move_up())
    assert True

    # non-deprecated
    tqdm_pandas(tqdm(total=df.shape[0]))
    df.progress_apply(lambda x: x)

# Generated at 2022-06-14 13:03:01.475395
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.pandas import tqdm_pandas
    # Create a sample df
    df = pd.DataFrame({
        'a': [1,2,3,4,5,6,7,8,9,10],
        'b': [2,4,6,8,10,12,14,16,18,20],
        'c': [4,8,12,16,20,24,28,32,36,40],
        'd': [8,16,24,32,40,48,56,64,72,80]})
    # Apply tqdm_pandas function
    df.progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:03:12.486560
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from tqdm import tqdm

    def test_progress_apply(deprecated_t):
        from pandas import DataFrame, Series
        from tqdm import tqdm

        # Test tqdm_pandas()
        tqdm_pandas(deprecated_t)

        def identity(x):
            """Identity function"""
            return x

        def copy(x):
            """Copy function"""
            return x.copy()

        def square(x):
            """Square function"""
            return x * x

        def progress_apply(df_group, func, *args, **kwargs):
            """Test progress_apply()"""
            try:
                progress = tqdm(total=len(df_group), unit='group')
            except TypeError:
                progress

# Generated at 2022-06-14 13:03:25.712375
# Unit test for function tqdm_pandas
def test_tqdm_pandas():  # pragma: no cover
    import pandas as pd
    from tqdm.contrib import pandas

    df = pd.DataFrame({'a': [1, 2, 3], 'b': [1, 2, 3]})[::-1]

    df.progress_apply(lambda row: row.a + row.b)

    with tqdm.pandas(desc='testing pandas') as t:
        df.progress_apply(lambda row: row.a + row.b)
        assert t.gui.pos() == 2

    # Test args

# Generated at 2022-06-14 13:03:36.970109
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with suppress(DeprecationWarning):
        from tqdm import tqdm_pandas  # noqa
        assert tqdm_pandas  # Fix for `pyflakes`
        from tqdm.autonotebook import tnrange  # noqa
        from pandas import DataFrame  # noqa
        from numpy import arange, array_equal  # noqa
        tqdm_pandas(tnrange)
        df = DataFrame(arange(10000).reshape(100, 100))
        r = df.groupby(df.sum()).progress_apply(lambda x: x ** 2)


# Monkey patching pandas
from pandas import core, compat
from pandas.core.groupby import DataFrameGroupBy
from tqdm import tqdm



# Generated at 2022-06-14 13:03:49.753954
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Import pandas and tqdm
    try:
        import pandas as pd
        try:
            import tqdm
        except ImportError:
            raise ImportError("tqdm not found, please install tqdm first.")
    except ModuleNotFoundError:
        raise ModuleNotFoundError("pandas not found, please install pandas first.")

    # Test pandas.core.groupby.DataFrameGroupBy.progress_apply

# Generated at 2022-06-14 13:03:58.111282
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import warnings
    import pandas as pd
    import numpy as np
    from tqdm import pandas as tqdm

    # tqdm.pandas()
    df = pd.DataFrame()
    with warnings.catch_warnings(record=True) as w:
        tqdm.pandas(nrows=10, ncols=10, nchunks=1, unit='B')
    assert len(w) == 2
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        tqdm.pandas(nrows=10, ncols=10, nchunks=1, unit='B')
    assert len(w) == 1

# Generated at 2022-06-14 13:04:03.991816
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.autonotebook import tqdm

    tqdm_pandas(tqdm)
    df = pd.DataFrame({'a': [0, 1, 2, 3, 4, 5, 6]})
    df.groupby("a").progress_apply(lambda x: None)
    assert True

# Generated at 2022-06-14 13:04:07.349025
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test that tqdm_pandas can be called without error."""
    try:
        # Instantiating the parent class TqdmBaseBar
        from tqdm import TqdmBaseBar
        tcls = TqdmBaseBar()
        # If no error was raised, we're good
        tqdm_pandas(tcls)
    except Exception:
        # If any error was raised, we're not good
        raise

# Generated at 2022-06-14 13:04:13.280559
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    def group_count(arr):
        return len(arr)

    data = pd.DataFrame(np.random.randint(0, 10, (20000000, 2)))
    with tqdm_pandas(total=data.shape[0]) as t:
        data.groupby(2, group_keys=False).progress_apply(group_count)

# Generated at 2022-06-14 13:04:23.062585
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas

        def f(x):
            import time
            time.sleep(0.1)

        try:
            from multiprocessing import cpu_count
        except ImportError:
            cpu_count = lambda: 1  # noqa

        tqdm_pandas(pandas.DataFrame(range(10000)).groupby(0).progress_apply(f))
        tqdm_pandas(
            pandas.DataFrame(range(10000)).groupby(0).progress_apply(
                f,
                num_workers=cpu_count()),
            desc='Computing',
            leave=False)
    except:
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:28.658826
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm(total=1))


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:40.524549
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    func = 'tqdm_pandas'

    try:
        tqdm_pandas(42)
    except TypeError:
        pass
    else:
        raise Exception('function "{}" fails: "{}"'.format(func, 'test0'))

    try:
        tqdm_pandas(('abc',))
    except TypeError:
        pass
    else:
        raise Exception('function "{}" fails: "{}"'.format(func, 'test1'))

    try:
        tqdm_pandas(['abc'])
    except TypeError:
        pass
    else:
        raise Exception('function "{}" fails: "{}"'.format(func, 'test2'))

    try:
        tqdm_pandas(set('abc'))
    except TypeError:
        pass
   

# Generated at 2022-06-14 13:04:45.443171
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.rand(200000, 5))
    tqdm_pandas(df.groupby(0).sum().progress_apply(lambda x: x))
    tqdm_pandas(df.groupby(0).sum().progress_apply(lambda x: x), desc='testing')


if __name__ == '__main__':
    from tqdm import tqdm
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:57.647543
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Test tqdm_pandas.
    """
    import numpy as np
    import pandas as pd
    from tqdm._tqdm_pandas import tqdm_pandas

    if not pd:
        raise unittest.SkipTest('no pandas')

    # just in case, so that the pandas tqdm is really used
    try:
        import pandas.core.groupby
        pandas.core.groupby.DataFrameGroupBy.progress_apply = None
    except AttributeError:
        pass

    with closing(StringIO()) as our_file:
        with tqdm(total=50, file=our_file) as t:
            tqdm_pandas(t)

# Generated at 2022-06-14 13:05:06.150230
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.test import test_pandas_deprecation

    test_pandas_deprecation()

    df = pd.DataFrame(np.random.randint(0,100,size=(100000, 1)))
    pb = tqdm_pandas(total=len(df))
    result = df[0].progress_apply(lambda x: x**2)
    pb.close()
    assert result.sum() == 33833842500

    # fix pandas < 0.19.0 column indices
    pb = tqdm_pandas(total=len(df))  # noqa
    result = df[0].progress_apply(lambda x: x**2)
    pb.close()
    assert result.sum()

# Generated at 2022-06-14 13:05:18.164530
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.auto import trange
    from tqdm.pandas import tqdm
    df = pd.DataFrame({'a': np.arange(10), 'b': np.arange(10)})
    tqdm_pandas(tqdm(total=len(df)))
    df.groupby('a').progress_apply(lambda x: x)  # no-op
    tqdm_pandas(tqdm)
    df.groupby('a').progress_apply(lambda x: x)  # no-op
    tqdm_pandas(trange)
    df.groupby('a').progress_apply(lambda x: x)  # no-op

# Generated at 2022-06-14 13:05:21.752992
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with CreateProgressBar() as bar:
        tqdm_pandas(bar)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 13:05:28.116921
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas, tqdm
    import numpy as np
    df = pandas.DataFrame({
        'a': np.random.normal(size=10000),
        'b': np.random.normal(size=10000),
    })
    with tqdm.tqdm() as t:
        output = df.groupby('a').progress_apply(np.mean, meta=('b', float))
    assert t.n == len(df.a.unique())
    assert isinstance(output, pandas.Series)
    assert len(output) == len(df.a.unique())



# Generated at 2022-06-14 13:05:35.696896
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    [tqdm.pandas()]
    [tqdm_pandas(tqdm.tqdm())]
    [tqdm_pandas(tqdm.tqdm, total=1000)]
    [tqdm_pandas(tqdm, total=1000)]
    pd.Series(list(range(1000))).progress_apply(lambda x: x)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:47.785858
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas"""
    import numpy as np
    import pandas as pd
    from random import random
    from tqdm import tqdm
    seed = 42
    np.random.seed(seed)

    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm(total=1), total=1)

    def slow(x):
        time.sleep(0.01)
        return x

    n = 1000
    df = pd.DataFrame(
        {'a': np.random.randint(0, 100, n),
         'b': [random() for _ in range(n)]})

    # Groupby unordered
    for i in tqdm(range(100), desc='unordered groupby'):
        df.group

# Generated at 2022-06-14 13:06:00.470296
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    test1 = tqdm(total=1).pandas(desc='test')
    assert test1._reference_t.__class__.__name__ == 'tqdm_gui'
    test1.__exit__(None, None, None)
    test2 = tqdm(total=1, file=None).pandas(desc='test')
    assert test2._reference_t.__class__.__name__ == 'tqdm_notebook'
    test2.__exit__(None, None, None)

    test3 = tqdm_pandas(tqdm(total=1), desc='test')
    assert test3._reference_t.__class__.__name__ == 'tqdm_gui'

# Generated at 2022-06-14 13:06:12.782617
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time
    import tqdm
    import tqdm.pandas

    pd.set_option('mode.chained_assignment', None)

    with warnings.catch_warnings():
        warnings.simplefilter('ignore', tqdm.TqdmExperimentalWarning)
        # Setup
        try:
            tqdm.pandas.tqdm_pandas(tqdm.tqdm, desc='test')
        except tqdm.TqdmDeprecationWarning:
            return
        df = pd.DataFrame({
            'x': np.random.randint(0, 100000, 10000),
            'y': np.random.randint(0, 100000, 10000),
        })
        # Tests
        # tq

# Generated at 2022-06-14 13:06:17.567058
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        tqdm_pandas(tqdm, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} "
                    "[{elapsed}<{remaining}, {rate_fmt}{postfix}]",
                    **{'disable': True})
    except TypeError:
        # TODO: remove in v5.0.0
        tqdm_pandas(tqdm, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} "
                    "[{elapsed}<{remaining}, {rate_fmt}{postfix}]")


# Try to register tqdm

# Generated at 2022-06-14 13:06:23.655197
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame({'A': range(10)})

    def f(x):
        from tqdm import tqdm_pandas
        tqdm_pandas(tqdm(desc='test_tqdm_pandas'))

        # tqdm_pandas(tqdm(df))  # deprecated use
        def g(y):
            from time import sleep
            sleep(0.0001)
            return 1
        df.progress_apply(g, axis=1)
    f(df)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:29.297736
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.auto import tqdm
    df = pd.DataFrame([1, 2, 3, 4], columns=['a'])
    with tqdm(total=4) as t:
        df.groupby('a').progress_apply(lambda x: x)
        assert t.n == 4, 'tqdm_pandas failed'

# Generated at 2022-06-14 13:06:36.969884
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from numpy import random
    from pandas import DataFrame, concat

    for _ in tqdm_pandas(range(4)):
        # Create some random data
        df = DataFrame(random.rand(100, 3), columns=["A", "B", "C"])
        dfs = [df.iloc[10 * i:10 * i + 10] for i in range(10)]
        # pd.concat(dfs).groupby(0).progress_apply(lambda x: x**2)
        concat(dfs).groupby(0).progress_apply(lambda x: x**2)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:40.514406
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm, total=100)

# Generated at 2022-06-14 13:06:43.496671
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    tq = tqdm_pandas(tqdm())
    pd.DataFrame({'a': [1, 2]}).progress_apply(lambda x: x, axis=1)
    tq.close()
    del tq

    import pandas as pd
    tq = tqdm_pandas(tqdm)
    pd.DataFrame({'a': [1, 2]}).progress_apply(lambda x: x, axis=1)
    tq.close()
    del tq


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:55.190500
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        # Python 2
        from StringIO import StringIO
    except ImportError:
        # Python 3
        from io import StringIO

    def is_close(a, b):
        return abs(a - b) < 1e-5

    # Create test pandas dataframe
    df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4],
                       'A': [5, 4, 3, 2, 1],
                       'C': ['a'] * 5})

    # Test with tqdm class
    t = tqdm(total=df.groupby('A').count().sum().sum(),
             bar_format='{desc}: {n_fmt}/{total_fmt} ({percentage:3.0f}%)|{bar}|')
    tqdm_pand

# Generated at 2022-06-14 13:07:05.876962
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, trange
    from random import random

    def test_func(x):
        return x + random()
    # Build a dummy DataFrame
    df = pd.DataFrame({'AAA': [1, 2, 3], 'BBB': [4, 5, 6], 'CCC': [7, 8, 9]})
    df2 = pd.DataFrame(dict((i, [1, 2, 3]) for i in trange(10)))
    # Progress apply with `tqdm` class
    tqdm_pandas(tqdm, desc='my_df1')
    df.groupby('AAA').progress_apply(test_func)
    tqdm_pandas(tqdm, desc='my_df2')
    df2.group

# Generated at 2022-06-14 13:07:22.327302
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)),
                      columns=list('ABCDEF'))
    tqdm_pandas(tqdm, file=sys.stdout)

    # Test on SeriesGroupBy
    for i in df.groupby('A')['B'].progress_apply(lambda x: x + 1):
        pass
    # Test on DataFrameGroupBy
    for i in df.groupby('A').progress_apply(lambda x: x + 1):
        pass

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:31.871674
# Unit test for function tqdm_pandas
def test_tqdm_pandas():

    # Initialize a tqdm instance
    from tqdm import tqdm
    from tqdm._tqdm import TqdmDeprecationWarning
    import pandas as pd
    import numpy as np
    from math import isclose

    # Check deprecated function
    with TqdmDeprecationWarning(fp_write=sys.stderr.write):
        tqdm_pandas(tqdm)

    # Check deprecated function
    with TqdmDeprecationWarning(fp_write=sys.stderr.write):
        tqdm_pandas(tqdm())

    # Check deprecated function

# Generated at 2022-06-14 13:07:34.515467
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    #TODO(casperdcl): add function unit test
    assert tqdm_pandas(tqdm, file=sys.stdout) is None
    assert tqdm_pandas(tqdm(file=sys.stdout)) is None



# Generated at 2022-06-14 13:07:46.019152
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    # pandas >= 0.24
    df = pd.DataFrame({'a': [1, 2]})
    tqdm_pandas(tqdm, unit='row')
    df = df.progress_apply(lambda x: x, axis=1)
    tqdm_pandas(tclass=type(df.progress_apply(lambda x: x, axis=1)),
                file=sys.stderr, unit='row')

    # pandas < 0.24
    df = pd.DataFrame({'a': [1, 2]})
    tqdm_pandas(tqdm, unit='row')
    df = df.apply(lambda x: x, axis=1)

# Generated at 2022-06-14 13:07:50.272059
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    tqdm_pandas(tqdm_pandas)
    tqdm_pandas(tqdm_pandas)

# Generated at 2022-06-14 13:07:57.443320
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm import pandas

    # Test simple case
    tqdm_pandas(tqdm)
    pandas(tqdm)

    # Test delayed adapter
    tclass = type
    tqdm_pandas(tclass)
    tclass.pandas()

# Test function
if __name__ == "__main__":
    # Test function
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:05.483913
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    # Simple
    df = pd.DataFrame(np.random.randn(15, 2), columns=['foo', 'bar'])
    with tqdm(total=df.shape[0], desc='Unit Test', leave=False) as pbar:
        print(df.groupby('foo').progress_apply(lambda x: x**2, pbar=pbar).head())

    # Test whether it accepts tqdm_kwargs
    # Can't test stdout redirection because it's a global operation
    df = pd.DataFrame(np.random.randn(15, 2), columns=['foo', 'bar'])
    file = open('temp_tqdm_pandas', mode='w')

# Generated at 2022-06-14 13:08:14.944550
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    df = DataFrame({'a': list(range(100)), 'b': list(range(100))})
    import tqdm
    _ = df.groupby('a').progress_apply(lambda x: x)
    tqdm_pandas(tqdm.tqdm())
    _ = df.groupby('a').progress_apply(lambda x: x)
    tqdm_pandas(tqdm.tqdm)
    _ = df.groupby('a').progress_apply(lambda x: x)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:25.994403
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm

    tqdm.tqdm_pandas(tqdm.tqdm(total=5))
    tqdm.tqdm_pandas(tqdm.tqdm(total=5), desc="desc")
    tqdm.tqdm_pandas(tqdm.tqdm(total=5), leave=True)
    tqdm.tqdm_pandas(tqdm.tqdm(total=5), disable=True)
    tqdm.tqdm_pandas(tqdm.tqdm(total=5), mininterval=0.01)
    tqdm.tqdm_pandas(tqdm.tqdm(total=5), mininterval=0.01, maxinterval=1)
    tq

# Generated at 2022-06-14 13:08:37.314123
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    from tqdm import tqdm
    tqdm = tqdm(pandas_dataframe_provider())
    tqdm_pandas(tqdm)
    tqdm.close()

    # Check that we can call `tqdm` and `pandas` manually
    tqdm = tqdm(pandas_dataframe_provider())
    tqdm_pandas(tqdm)
    tqdm.pandas()
    tqdm.close()

    # Check that we can pass `tqdm_kwargs` to `tqdm`
    tqdm = tqdm_pandas(tqdm(pandas_dataframe_provider()), total=5)
    tqdm.close()



# Generated at 2022-06-14 13:09:00.498138
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Test function `tqdm_pandas`.
    """
    try:
        import pandas as pd
        import tqdm

        def func(a, b, c, tqdm_kwargs):
            d = a + b + c
            for _ in pd.DataFrame(
                    {'a': [0], 'b': [0], 'c': [0]}).groupby(
                        'a').progress_apply(d, **tqdm_kwargs):
                pass

        for f in [tqdm_pandas, tqdm.tqdm.pandas, tqdm.tqdm.tqdm.pandas]:
            func(1, [0], 'a', {'f': f})
    except ImportError:
        pass



# Generated at 2022-06-14 13:09:11.698973
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from pandas.core.groupby import DataFrameGroupBy
    from inspect import getsource
    from os import path
    from sys import modules
    from .deprecation import TqdmDeprecationWarning
    with TqdmDeprecationWarning(fp_write=sys.stderr.write):
        assert (tqdm_pandas(tqdm) ==
                tqdm_pandas(type(tqdm)) ==
                tqdm_pandas(tqdm()) ==
                tqdm_pandas(type(tqdm())))

    with TqdmDeprecationWarning(fp_write=sys.stderr.write):
        tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:09:17.547584
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from numpy.testing import assert_equal
    from numpy import arange

    vals = arange(10)
    df = DataFrame({'vals': vals})
    expected = Series(vals ** 2).values
    assert_equal(df.progress_apply(lambda x: x ** 2, axis=1), expected)

# Generated at 2022-06-14 13:09:24.621801
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np 
    from tqdm import tqdm

    df = pd.DataFrame(np.random.randn(10000, 10000))

    tqdm_pandas(tqdm)
    df.groupby(0).progress_apply(lambda x: x**2)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:34.116059
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame

    tclass = None
    tqdm_kwargs = {}
    try:
        tqdm_pandas(tclass, **tqdm_kwargs)
    except SystemExit:
        pass

    tclass = DataFrame
    tqdm_kwargs = {}
    tqdm_pandas(tclass, **tqdm_kwargs)

    tclass = tqdm.tqdm
    tqdm_kwargs = {}
    tqdm_pandas(tclass, **tqdm_kwargs)

# Generated at 2022-06-14 13:09:39.299585
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm

    _tqdm_pandas = tqdm_pandas(tqdm())
    isinstance(_tqdm_pandas, type(tqdm()))

    _tqdm_pandas = tqdm_pandas(tqdm)
    isinstance(_tqdm_pandas, type(tqdm()))

# Generated at 2022-06-14 13:09:48.503113
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas"""
    try:
        import pandas
        from pandas import DataFrame, Series

        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        df = DataFrame({'listlen': items})
        with tqdm.tqdm_pandas(leave=False) as t:
            df['listlen_squared'] = df['listlen'].progress_apply(lambda x: x**2)
        assert 'listlen_squared' in df.columns
        assert (df['listlen_squared'] == Series(i**2 for i in items)).all()
    except ImportError:
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:52.135607
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        import tqdm

        tqdm.pandas(tqdm.tqdm(total=None), desc='pandas')
    except ImportError:
        pass

# Generated at 2022-06-14 13:10:03.864814
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    # Create test dataframe
    df = pd.DataFrame({'a': range(1, 100000), 'b': range(1, 100000)})
    # Capture the printed output of `pandas.core.groupby.DataFrameGroupBy.progress_apply`
    f = StringIO()
    with redirect_stdout(f):
        df.groupby('a').progress_apply(lambda x: round(x.mean()))

    # Check printed output
    out = f.getvalue()
    assert out.find('100%|##########|') >= 0

# Generated at 2022-06-14 13:10:08.208043
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return  # pandas not installed
    df = pandas.DataFrame({'idx': [1, 2, 3]})
    df.groupby('idx').progress_apply(
        lambda x: None,
        tqdm_kwargs=dict(total=len(df),
                         desc='test_tqdm_pandas',
                         disable=False))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:42.056769
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    with tqdm_pandas(total=10) as pbar:
        df = pd.DataFrame({'a': [1] * 10})
        df.groupby('a').progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:10:51.847419
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test function interface"""
    import pandas as pd
    import tqdm

    # Must raise warning
    with pytest.warns(TqdmDeprecationWarning):
        tqdm_pandas(tqdm, desc='test')

    # Must not raise warning
    tqdm.pandas(desc='test')  # no warning


if __name__ == "__main__":
    # Tests
    test_tqdm_pandas()
    # Example
    import pandas as pd
    import tqdm
    from tqdm import tqdm_pandas

    @tqdm_pandas  # Or add directly to pandas
    def parallel_sum(df):
        return df.apply(lambda x: x.sum())


# Generated at 2022-06-14 13:11:02.252522
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    df = pd.DataFrame({u'a': [1, 2, 3], u'b': [u'a', u'b', u'c']})
    # Delayed adapter case test
    t = tqdm
    t.pandas = lambda **kwargs: (
    lambda: None)

    tqdm_pandas(t)
    # Adapted case test
    t = tqdm(range(12))
    t.pandas = lambda **kwargs: (
    lambda: None)

    tqdm_pandas(t)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:11:12.995375
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.pandas import tqdm_pandas

    df = pd.DataFrame(np.random.random((1000000, 3)))
    tqdm_pandas(tqdm(leave=False))

    # Test ignoring a deprecated warning
    import warnings
    with warnings.catch_warnings(record=True) as w:
        tqdm_pandas(tqdm(leave=False))
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert ('Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`'
                in str(w[-1].message))

    # Test function

# Generated at 2022-06-14 13:11:19.222926
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm.auto as tqdm
    tqdm.pandas()
    data = {'a': [1, 2, 3], 'b': [3, 4, 5]}
    df = pd.DataFrame(data)
    df.groupby('a').progress_apply(lambda x: x)
    df.progress_apply(lambda x: x)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:11:25.513868
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    class tqdm:
        """Dummy `tqdm` class."""
        @staticmethod
        def pandas(*a, **k):
            return a, k

        @staticmethod
        def tqdm(x, **kwargs):
            return x

    tqdm_pandas(tqdm(), ascii=True)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:11:35.231123
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        del os.environ['TQDM_DISABLE']
    except KeyError:
        pass
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    import sys

    df = pd.DataFrame(
        {'id': np.arange(100), 'dummy_col': np.random.randn(100)})
    df.groupby(['id']).progress_apply(lambda x: x)

    df = pd.DataFrame(
        {'id': np.arange(1000)})
    # has progress_apply but no groupby
    df.progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()