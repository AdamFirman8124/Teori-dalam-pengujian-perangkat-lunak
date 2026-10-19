

# Generated at 2022-06-14 13:01:29.632477
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    df = DataFrame({'a': range(10), 'b': range(10)})
    df_grp = df.groupby('a')
    result = df_grp.progress_apply(lambda x: x * 2)
    # test adapter
    tqdm_pandas(tqdm)
    assert result.equals(df_grp.progress_apply(lambda x: x * 2))
    # test instance
    tqdm_pandas(tqdm())
    assert result.equals(df_grp.progress_apply(lambda x: x * 2))



# Generated at 2022-06-14 13:01:38.323893
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.contrib.pandas import tqdm_pandas
    from tqdm import tqdm

    df = pd.DataFrame(np.arange(10), columns=['a'])
    tqdm_pandas(tqdm(total=len(df)))
    grp = df.groupby('a')
    grp.progress_apply(lambda x: x)

    # Second test, without the decorator
    from tqdm.contrib import pandas

    pandas.tqdm_pandas(tqdm(total=len(df)))
    grp.progress_apply(lambda x: x)

# Generated at 2022-06-14 13:01:46.431936
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    data = {
        'i': [1, 2, 3, 4]
    }
    df = DataFrame(data)

    # Test that tqdm class can be passed to decorator
    df.groupby(['i']).progress_apply(lambda x: x)
    with tqdm(leave=True) as t:
        tqdm_pandas(t)
        df.groupby(['i']).progress_apply(lambda x: x)

    # Test that tqdm instance can be passed to decorator
    df.groupby(['i']).progress_apply(lambda x: x)
    with tqdm(leave=True) as t:
        tqdm_pandas(t)

# Generated at 2022-06-14 13:01:55.583893
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    def sleep_msec(ms):
        import time
        time.sleep(ms * 0.001)

    pd.Series.progress_apply = None
    pd.DataFrame.progress_apply = None

    df = pd.DataFrame(np.random.randn(100000, 4))
    t = tqdm(total=len(df), leave=False)
    for l in df.progress_apply(sleep_msec):
        t.update(len(l))
    t.close()
    df = pd.DataFrame(np.random.randn(100000, 4))

# Generated at 2022-06-14 13:02:07.453699
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from .gui import tqdm
    tqdm_pandas(tqdm)
    try:
        from numpy import random
        from pandas import DataFrame
        df = DataFrame(random.randint(0, int(1e9), (1000000, 100)),
                       columns=['col%d' % i for i in range(0, 100)])
        df.apply(lambda x: x, axis=0)  # warmup
    except ImportError:
        return
    import time
    with tqdm(total=df.size, unit=' cell', miniters=0,
              smoothing=0, disable=False) as t:
        def progress(x):
            t.update()
            return x
        tqdm_pandas(t)
        t.reset()
        ts = time.time

# Generated at 2022-06-14 13:02:17.455414
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm.pandas import tqdm_pandas
    import time

    ### Test 1:
    # Test registeration of tqdm instance with `pandas.core.groupby.DataFrameGroupBy.progress_apply`
    def test_func_1(x):
        time.sleep(0.001)
        return x

    df = pd.DataFrame(
        {'a': [1, 2, 3] * 1000,
         'b': np.random.randn(3000)})
    print(df.groupby('a').progress_apply(test_func_1).head())

    tqdm_pandas(tqdm())

# Generated at 2022-06-14 13:02:29.315424
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    from tqdm import tqdm

    print("Testing tqdm_pandas wrapper ...")

    df = pd.DataFrame({'a': [1, 2, 3], 'b': [[1.1, 2.1], [], [3.1, 4.2, 5.3]]})
    tqdm.pandas(desc="desc")

    t = tqdm(total=df.shape[0] * 2, leave=False)

    out = df.groupby('a').progress_apply(lambda x: len(x['b'])).tolist()
    assert out == [2, 0, 3]
    assert t.n == 6


# Generated at 2022-06-14 13:02:40.223391
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:02:50.173168
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame({'a': np.random.randint(0, 100, (1000, )),
                       'b': np.random.randint(0, 100, (1000, ))})
    df.groupby("a").progress_apply(tqdm_pandas,
                                   total=100,
                                   desc='bar',
                                   leave=False,
                                   postfix={'a': 1})  # should not fail


# Generated at 2022-06-14 13:03:02.417262
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for `tqdm.contrib.tqdm_pandas`.
    """
    from tqdm import tqdm, tqdm_pandas
    from pandas import DataFrame, Series
    tqdm_pandas(tqdm)
    df = DataFrame({'a': Series([1, 2, 3, 4]), 'b': Series([9, 8, 7, 6])})

    # Can be called with or without tqdm instance
    for func in (tqdm_pandas, tqdm.pandas):
        # Test normal usage
        assert list(
            func().progress_apply(lambda x: x)) == [0, 1, 2, 3]  # as index

        # Test non-Series

# Generated at 2022-06-14 13:03:13.404410
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_pandas
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.rand(10000, 2))
    tqdm_pandas(tqdm)
    df.groupby(0).progress_apply(lambda x: x**2)
    tqdm_pandas(tqdm(total=10))
    df.groupby(0).progress_apply(lambda x: x**2)
    tqdm_pandas(tqdm(total=10), ascii=True)
    df.groupby(0).progress_apply(lambda x: x**2)
    tqdm_pandas(tqdm(total=10), ascii=False)

# Generated at 2022-06-14 13:03:26.519266
# Unit test for function tqdm_pandas

# Generated at 2022-06-14 13:03:37.043227
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
        from tqdm.auto import tqdm_notebook as tqdm
        from tqdm.contrib.tests import pretest_posttest_decorator
    except ImportError:
        return

    @pretest_posttest_decorator
    def test_tqdm_pandas_hook(*args, **kwargs):
        tqdm_pandas(tqdm(*args, **kwargs))
        for i in range(4):
            df = pd.DataFrame(np.random.rand(10000, 4))
            kwargs['leave'] = kwargs.get('leave', True)  # otherwise fails in notebook
            df.groupby(df.sum()).progress_apply(lambda x: x ** 2)

   

# Generated at 2022-06-14 13:03:49.857649
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    import tqdm._tqdm as _tqdm

    # Test progress_apply
    _tqdm.tqdm_pandas(tqdm)
    n = 100
    with tqdm(total=n) as t:
        df = pd.DataFrame(np.random.randint(0, n, (n, 2)),
                          columns=['a', 'b'])
        df.groupby('a').progress_apply(
            lambda x: sum(x['b']),
            meta=[('a', int), ('b', 'int')],
        )
        t.update()

    # Test progress_map
   

# Generated at 2022-06-14 13:03:58.153507
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas.util.testing import assert_frame_equal
    from tqdm import tqdm_notebook as tn
    from tqdm import tqdm
    from tqdm import trange
    from tqdm import tqdm_pandas
    from pandas import DataFrame
    import random
    import numpy as np
    try:
        from tqdm import tqdm_gui as tg
    except:
        tg = None
    try:
        from tqdm import tnrange as tnr
    except:
        tnr = None

    def f(x, y):
        res = []
        for i in range(0, x):
            res.append(i ** y)
        return res


# Generated at 2022-06-14 13:04:07.149894
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    try:
        df = pd.DataFrame({'word': ['return', 'with']})
        _ = df.progress_apply(lambda x: x)
    except AttributeError:
        pass
    else:
        assert False, "DF already has .progress_apply"
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm())
    try:
        df = pd.DataFrame({'word': ['return', 'with']})
        _ = df.progress_apply(lambda x: x)
    except AttributeError:
        assert False, "DF does not have .progress_apply"

# Generated at 2022-06-14 13:04:12.066389
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm(total=10))


# Registering `pandas` as an available keyword argument
# (See also https://github.com/tqdm/tqdm/issues/543)



# Generated at 2022-06-14 13:04:21.352415
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas
    """
    import numpy as np
    import pandas as pd
    import tqdm.pandas

    A = pd.DataFrame(np.random.rand(100000))
    A['B'] = np.random.rand(100000)

    tqdm.pandas.tqdm_pandas(tqdm.tqdm, ascii=True)
    A.groupby('B').progress_apply(lambda x: x ** 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:24.098634
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    t = tqdm_pandas(tqdm(total=2))
    for _ in range(2):
        t.update(1)
    assert t.total == 2

# Generated at 2022-06-14 13:04:32.500658
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    try:
        import pandas as pd

        def f(x):
            from time import sleep
            sleep(0.01)
            return x

        df = pd.util.testing.makeDataFrame()
        for t in [tqdm, tqdm_pandas]:
            assert all(df.groupby('A').progress_apply(f) == df)
    except ImportError:
        pass

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:44.593703
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm.pandas"""
    import numpy as np
    import pandas as pd
    from tqdm import tqdm

    N, D = int(1e6), 10

    np.random.seed(0)
    df = pd.DataFrame(np.random.random(size=(N, D)))
    df.columns = ['col%d' % i for i in range(D)]

    # Manual
    assert list(df.progress_apply(lambda x: np.sum(x))) == \
        [np.sum(x) for x in tqdm(df.values, desc='apply', leave=False)]

    # Decorator

# Generated at 2022-06-14 13:04:49.815981
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    df = pd.DataFrame({'a': np.arange(1000)})
    g = df.groupby([df['a'] // 10 * 10, df['a'] % 10])
    out = g.progress_apply(lambda x: x['a'] // 10 * 10)
    assert out.equals(df['a'] // 10 * 10)

# Generated at 2022-06-14 13:05:01.976476
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import trange
    import pandas as pd
    import pandas.core.groupby

    df = pd.DataFrame({"a": [1, 1, 1, 2, 2], "b": [1, 2, 1, 1, 2]})
    df1 = pd.DataFrame({"a": [1, 1, 1, 2, 2], "b": [1, 2, 1, 1, 2]})

    def f(x):
        return x

    # Create a tqdm instance
    t = trange(2, desc='testing')
    # Register the tqdm instance with pandas
    tqdm_pandas(t)
    # Apply pandas function with `progress_apply`
    df.groupby("a").progress_apply(f)

    # Make sure that `progress_

# Generated at 2022-06-14 13:05:08.177944
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.autonotebook import tnrange
    import pandas as pd
    import numpy as np

    tqdm_pandas(tnrange)

    df = pd.DataFrame(np.random.rand(100, 100))
    # df.progress_apply(lambda x: [e ** 2 for e in x])

# Generated at 2022-06-14 13:05:14.587159
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    if HAS_PANDAS:
        import pandas as pd
        import numpy as np

        def retdf(n):
            for _ in tqdm_pandas(range(n)):
                yield pd.DataFrame(np.random.rand(5, 2))

        pd.concat(retdf(10)).head()

    else:
        print("Skipping test for 'tqdm_pandas' function, as pandas is missing")


# =============================================================================
# tqdm_notebook
# =============================================================================
if to_avoid_tqdm_pandas_dependency:
    try:
        from IPython.display import HTML, Javascript, display
        from ipywidgets import IntProgress, HTML as ProgressHTML
    except ImportError:
        pass

# Generated at 2022-06-14 13:05:19.462726
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas

    class t:

        @classmethod
        def pandas(cls, **kwargs):
            return 'pandas', kwargs

        name = 'name'

    assert tqdm_pandas(t) == ('pandas', {})
    assert tqdm_pandas(t, param=1) == ('pandas', {'param': 1})

# Generated at 2022-06-14 13:05:25.334910
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Registers tqdm instance with pandas.
    """
    import pandas as pd
    from pandas import DataFrame
    from tqdm import tqdm as tqdm_old

    tqdm_pandas(tqdm_old(total=100))
    df = DataFrame({'a': range(100)})
    df['a'].progress_apply(lambda x: x)  # Should be invisible

# Generated at 2022-06-14 13:05:27.801189
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from .gui import tqdm
    t = tqdm(total=1, leave=False)
    tqdm_pandas(t)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:34.420524
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:  # pragma: no cover
        raise ImportError('to use `tqdm_pandas`, please install pandas first')

    # Call without parameters
    tqdm_pandas(tclass=tqdm)

    # Call with pandas instance
    tqdm_pandas(tqdm(total=None))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:46.669584
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from random import randint
    from time import sleep

    def test_f(df):
        sleep(randint(1, 10) / 10)
        return len(df)


# Generated at 2022-06-14 13:05:58.356545
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import tqdm
        import pkg_resources
    except ImportError:
        return

    # DataFrame
    df = pd.DataFrame({'a': [123, 456, 789]})
    assert (tqdm_pandas(tqdm.tqdm_notebook).progress_apply(lambda x: len(str(x['a'])), axis=1) ==
            df.progress_apply(lambda x: len(str(x['a'])), axis=1)).all()

    # Series
    s = pd.Series((pd.Series({'a': 123, 'b': 456, 'c': 789})))

# Generated at 2022-06-14 13:06:10.705347
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    import numpy as np

    # Create a pandas dataframe with 1000 rows and a range of values from 0 to 999
    df = pd.DataFrame(np.random.randint(0, 1000, size=(1000, 4)), columns=list('ABCD'))

    # Sum all values in the dataframe using the tqdm class
    tqdm_pandas(tqdm)
    # https://stackoverflow.com/questions/52154876/how-to-use-tqdm-pandas-in-pandas-0-23
    sums = df.progress_apply(lambda x: x.sum())

    # Finally, print the sums of all columns
    print(sums)


# Generated at 2022-06-14 13:06:19.289350
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy

    _tqdm_pandas = tqdm_pandas

    def tqdm_pandas_mock(tclass, **tqdm_kwargs):
        assert isinstance(tclass, type)
        assert hasattr(tclass.pandas, 'tqdm')
        assert tclass == tclass.pandas.tqdm


# Generated at 2022-06-14 13:06:30.721817
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for tqdm_pandas()
    """
    # Test the deprecated-function implementation
    pd.DataFrame([range(20)])
    with tests.capture_output() as (out, err):
        tqdm_pandas(tqdm)
        tqdm_pandas(tqdm(total=100))

    with tests.capture_output() as (out, err):
        tqdm_pandas(tqdm(total=100, file=open(os.devnull, 'w')))

    with tests.capture_output() as (_, err):
        tqdm_pandas(tqdm(total=100, file=sys.stderr))
    assert "Please use `tqdm.pandas(...)`" in err.getvalue

# Generated at 2022-06-14 13:06:38.477108
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd

    # Basic test
    df = pd.DataFrame({'A': [1, 2, 3, 4]})
    tqdm_pandas(tqdm(total=df.shape[0]))
    df.groupby('A').progress_apply(lambda x: list(x))

    # Test deprecated_t argument (check "skip over")
    tqdm_pandas(tqdm(total=df.shape[0]-1))
    df.groupby('A').progress_apply(lambda x: list(x))

    # Test deprecated_t argument (check "skip over" warning)
    tqdm_pandas(tqdm(total=df.shape[0]-1, leave=False))

# Generated at 2022-06-14 13:06:43.003947
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from functools import partial
    from tqdm import tqdm

    test_pandas(partial(tqdm, leave=False, file=None))
    test_pandas(partial(tqdm, leave=False, file=None, dynamic_ncols=True))



# Generated at 2022-06-14 13:06:54.626651
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series, concat
    from numpy import nan, arange
    from tqdm import tqdm

    df = DataFrame({'A': [0, 0, 1, nan, nan, 1],
                    'B': [1, 2, 3, 4, 5, 6],
                    'C': [2, nan, nan, 5, 6, 7]})

    # groupby-apply test
    tqdm_pandas(tqdm(total=df.groupby('A').ngroups))
    assert df.groupby('A').progress_apply(Series.count).equals(
        df.groupby('A').count())

    # non-default axis
    g = df.groupby('A')
    tqdm_pandas(tqdm(total=g.ngroups))
   

# Generated at 2022-06-14 13:07:02.204911
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from random import random

    df = pd.DataFrame({'x': [random() for _ in range(1000_000)]})

    def foo(row):
        return row['x'] + row['x']

    res = df.progress_apply(foo, axis=1)
    res = tqdm(df, total=len(df), desc='foo').progress_apply(foo, axis=1)

    tqdm_pandas(tqdm(desc='foo'))
    df.progress_apply(foo, axis=1)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:09.194249
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return
    import numpy as np
    from tqdm import tqdm_notebook as tqdm
    from tqdm.autonotebook import trange
    df = pandas.DataFrame(np.random.randn(100, 2))
    t = trange(0)
    tqdm_pandas(t, desc='Test')
    t.close()
    df.groupby(0).progress_apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:17.199826
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        from tqdm import tqdm_pandas
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]})

        def g(a, b):
            return a + b

        tqdm_pandas(tqdm)
        df.groupby('a').progress_apply(g, 1)
    except Exception as e:
        sys.stderr.write("\nError: {}".format(e))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:33.322688
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for the tqdm_pandas function.

    Returns
    -------
    ret : bool
        Returns True if passes, otherwise False.
    """
    try:
        import pandas as pd
        import numpy as np
    except ImportError:
        return True

    ## case 1: verbose=False
    tqdm_pandas(tqdm())
    # 0 - no verbose
    pd.DataFrame(np.random.randn(10, 10)).groupby(0).progress_apply(lambda x: x)

    # 1 - verbose
    with Capturing() as output:
        pd.DataFrame(np.random.randn(10, 10)).groupby(0).progress_apply(lambda x: x)
    assert len(output) == 2

    ## case 2:

# Generated at 2022-06-14 13:07:41.263553
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for tqdm_pandas
    """
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame(np.random.random((int(1e5), 1)), columns=["x"])
    df.progress_apply(lambda x: x.x ** 2)

    tqdm_pandas(tqdm)  # <-- monkey-patch pandas with tqdm
    df.progress_apply(lambda x: x.x ** 2)

# Generated at 2022-06-14 13:07:51.729481
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame

    df = DataFrame(columns=['a', 'b', 'c'], data=[[1, 2, 3], [4, 5, 6]])
    tqdm_pandas(lambda x: None, leave=False)
    tqdm_pandas(tqdm, leave=False)
    df.groupby('a').progress_apply(lambda x: None)
    df.groupby('a').progress_apply(lambda x: None, leave=False)


# Import into tqdm namespace
tqdm.pandas = tqdm_pandas

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:02.222942
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        pd
    except NameError:
        raise unittest.SkipTest('Skipping because pandas is not installed.')
    from tqdm import tqdm
    from tqdm.pandas import tqdm_pandas
    from pandas import DataFrame
    import pandas.core.groupby
    import pandas
    import numpy as np
    from numpy.random import randint as rint
    from sys import version as sys_version

    # delay to avoid: AttributeError: 'module' object has no attribute '__getattr__'
    @tqdm_pandas
    def idfn(x):
        return x

    @tqdm_pandas
    def delayed_test(x):
        return x


# Generated at 2022-06-14 13:08:14.508521
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    try:
        tqdm.tqdm.pandas()
    except:
        tqdm_pandas(tqdm.tqdm)

    data = dict(
        N=np.arange(10000),
        A=np.random.standard_normal(10000),
        B=np.random.standard_normal(10000),
        C=np.random.standard_normal(10000),
        D=np.random.standard_normal(10000),
    )
    for i in range(4):
        data['N' + str(i)] = data['N']

    df = pd.DataFrame(data)
    print("\nTesting tqdm_pandas()...")

# Generated at 2022-06-14 13:08:25.587537
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    import numpy as np
    import tqdm.pandas

    df = pandas.DataFrame({'a': np.random.randint(0, 100, (1000,)),
                           'b': np.random.randint(0, 100, (1000,)),
                           'c': np.random.randint(0, 100, (1000,)),
                           'd': np.random.randint(0, 100, (1000,)),
                           })
    tqdm.pandas.tqdm(df.groupby(['a', 'b']).progress_apply(len))

    # Note:
    # tqdm_pandas() is an alias of tqdm.pandas.tqdm(...)
    # It is provided to maintain compatibility with the old way.
    # Dep

# Generated at 2022-06-14 13:08:28.541676
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        pd.Series(range(20)).progress_apply(lambda x: x)
    except:
        return False
    return True


if __name__ == '__main__':
    from tqdm import tqdm
    tqdm_pandas(tqdm(), total=100)

# Generated at 2022-06-14 13:08:39.411556
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.auto import tqdm_pandas
    import numpy as np
    import pandas as pd
    df = pd.DataFrame(np.random.rand(10000, 10))
    tqdm_pandas(tqdm_pandas(tqdm(leave=False)))
    tqdm_pandas(
        tqdm_pandas(tqdm(
            leave=False,
            total=df.progress_apply(len).sum(),
            desc='test_tqdm_pandas')))
    df.progress_apply(lambda _: None)

test_tqdm_pandas.test_name = "tqdm_pandas"  # for nose
test_tqdm_pandas.unit_test = True



# Generated at 2022-06-14 13:08:46.952285
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Creates a random pandas dataframe and a progress_bar,
    applies the progress_bar to the dataframe, and check
    if the progress_bar ends correctly
    """
    from tqdm import tqdm_pandas, trange
    from numpy import random
    from pandas import DataFrame

    n = 16
    bar = trange(n, desc='bar', leave=True)

    L = random.random((n, n))
    df = DataFrame(L, columns=['col_%d' % i for i in range(L.shape[1])])

    tqdm_pandas(bar)
    df.progress_apply(lambda x: x ** 2)

    assert bar.n == n, "progress_bar did not end correctly"

# Generated at 2022-06-14 13:08:56.952964
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas
    from pandas import DataFrame
    from random import shuffle

    df = DataFrame(list(range(20)))

    try:
        tqdm_pandas(tqdm(desc="Test_case1"))
    except TypeError:
        pass
    else:
        assert False, "No except for tqdm_pandas(tqdm(...)) case"

    try:
        tqdm_pandas(tqdm)
    except TypeError:
        pass
    else:
        assert False, "No except for tqdm_pandas(tqdm) case"

    # Single threaded
    df.progress_apply(shuffle)
    tqdm_pandas(tqdm(desc="Test_case2"))
    df.progress

# Generated at 2022-06-14 13:09:24.440444
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    from tqdm import tqdm

    df = pd.DataFrame(np.random.randint(0, 100, size=(100000, 4)), columns=list('ABCD'))
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm, leave=False)
    tqdm_pandas(tqdm(total=len(df)))

    df.groupby('A').progress_apply(lambda x: x)
    df.groupby('A').progress_apply(lambda x: x, group_keys=False)
    df.groupby('A').progress_apply(lambda x: x, group_keys=False, leave=False)

# Generated at 2022-06-14 13:09:36.793542
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pytest
    from pandas import DataFrame
    from tqdm import tqdm

    # Check that it works at least
    with tqdm(total=1) as t:
        tqdm_pandas(t)
        assert t.__enter__() is t

    # Check that it throws a deprecation warning
    with pytest.warns(TqdmDeprecationWarning):
        with tqdm(total=1) as t:
            tqdm_pandas(t)
            assert t.__enter__() is t

    # Check that it works for progress_apply
    df = DataFrame({'a': [1, 2, 3]})
    assert df.groupby('a').progress_apply(len) == df.groupby('a').apply(len)


# Set up DataFrameGroup

# Generated at 2022-06-14 13:09:44.925790
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import inspect
    from tqdm import tqdm, TqdmDeprecationWarning
    from pandas import DataFrame, Series

    with warnings.catch_warnings():
        warnings.filterwarnings("error")
        try:
            tqdm_pandas(tqdm)
            assert False, "should raise TqdmDeprecationWarning"
        except TqdmDeprecationWarning:
            pass

        tqdm_pandas(tqdm())
        assert inspect.isfunction(tqdm.pandas)
        try:
            tqdm_pandas(tqdm("a"))
            assert False, "should raise TqdmDeprecationWarning"
        except TqdmDeprecationWarning:
            pass


# Generated at 2022-06-14 13:09:52.410014
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    from pandas import DataFrame
    from pandas.core.groupby import DataFrameGroupBy
    from .tqdm import tqdm

    try:
        from numpy.random import randint
    except:
        from random import randint

    def pandas_apply(self, func, *args, **kwargs):
        """
        Enables `progress_apply` for pandas >= 0.18.
        See https://github.com/pandas-dev/pandas/issues/10040.
        """
        # TODO: remove check if issue is resolved
        if hasattr(DataFrameGroupBy, 'progress_apply'):
            return self.progress_apply(func, *args, **kwargs)
        else:
            return self.apply(func, *args, **kwargs)


# Generated at 2022-06-14 13:09:57.528776
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """ Unit test for function tqdm_pandas """
    import pandas as pd
    import numpy as np
    import tqdm
    x = pd.DataFrame(np.random.random(size=(1000, 1000)))
    tqdm.pandas(x.groupby(0).progress_apply)

# Generated at 2022-06-14 13:10:07.193069
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd

    df = pd.DataFrame(data=[1, 2, 3],
                      columns=['A'])

    list_ = []
    for _ in df.progress_apply(lambda x: [tqdm(['a', 'b', 'c'])]):
        list_.extend(_)
    assert len(list_) == 3

    list_ = []
    for _ in df.progress_apply(
            lambda x: [tqdm_pandas(tqdm(['a', 'b', 'c']))]):
        list_.extend(_)
    assert len(list_) == 3



# Generated at 2022-06-14 13:10:19.549835
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm, tqdm_gui

    # Test for range
    for obj in [tqdm, tqdm_gui]:

        # Instantiate tqdm
        t = obj(range(10))

        # Test for tqdm instance
        tqdm_pandas(t)
        assert t.use_dummy is True

        # Test for delayed tqdm
        tqdm_pandas(t.__class__)

        # Test for pandas
        df = pd.DataFrame({'a': range(10), 'b': range(10)})
        df.progress_apply(t.__class__)
        df.progress_apply(t.__class__, axis=0)

    # Test for pandas warning

# Generated at 2022-06-14 13:10:31.882446
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import trange

    df = pd.DataFrame({
        'A': [1, 1, 1, 2, 2, 2, 3, 3, 3, np.nan],
        'B': 2 * np.ones(10, dtype=int),
    })

    r = []
    for _ in trange(5, mininterval=0.1, file=sys.stdout, desc='foo'):
        r.append(df.groupby('A').progress_apply(lambda x: x))
    assert all(r[0].index == r[1].index)

    r = []

# Generated at 2022-06-14 13:10:35.712356
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    # Prepare example data
    df = pd.DataFrame()
    df['col'] = range(100000)
    df['col'] = df['col'] + 1
    assert len(df['col']) == 100000

    assert tqdm.tqdm_pandas(tqdm.tqdm()) == None

# Generated at 2022-06-14 13:10:42.621724
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    a = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]})
    a.groupby('a').progress_apply(lambda x: x['b'].sum())
    a.groupby('a').progress_apply(lambda x: x['b'].sum())
    a.groupby('a').progress_apply(lambda x: x['b'].sum())
    type(tqdm_pandas).pandas(tqdm_pandas)
    a.groupby('a').progress_apply(lambda x: x['b'].sum())

# Generated at 2022-06-14 13:11:04.708351
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    import tqdm

    df = pd.DataFrame(
        {"hello": range(100, 200), "world": range(200, 300)})

    with tqdm.tqdm(total=df.shape[0]) as t:
        def inc(*a, **k):
            t.update()
        tqdm_pandas(t, leave=False)
        df.groupby("hello").progress_apply(inc)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:11:08.867990
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from pandas import DataFrame
        tqdm_pandas(DataFrame())
    except Exception as e:  # pragma: no cover
        import traceback
        print(traceback.format_exc())
        raise e


# Compatibility with older versions of pandas

# Generated at 2022-06-14 13:11:12.733845
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm(1))
    tqdm_pandas(tqdm.tqdm)
    tqdm_pandas(tqdm.tqdm(1))

# Generated at 2022-06-14 13:11:21.597225
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from tqdm import tqdm_pandas as deprecated_tqdm_pandas

    class TqdmTestClass:
        """Does nothing"""
        @staticmethod
        def pandas(**kwargs):
            """Testing"""
            print("TESTING: tqdm.pandas", kwargs)

    # Test deprecated call
    deprecated_tqdm_pandas(tclass=TqdmTestClass)
    deprecated_tqdm_pandas(tclass=TqdmTestClass, bar_format='test')

    # Test deprecated call with tqdm instance
    deprecated_tqdm_pandas(tclass=TqdmTestClass(bar_format='test2'))

# Generated at 2022-06-14 13:11:29.653091
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
        df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))
        try:
            tqdm_pandas(tqdm, total=df.index.size)
        except AttributeError:
            # On IPython pandas <0.15.2, `DataFrame.progress_apply` does not exist
            pass
    except ImportError:
        pass

if __name__ == '__main__':
    test_tqdm_pandas()