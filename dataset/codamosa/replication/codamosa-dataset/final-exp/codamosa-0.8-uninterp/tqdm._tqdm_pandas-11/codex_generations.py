

# Generated at 2022-06-14 13:01:54.862850
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import numpy
        import pandas
    except ImportError:
        raise SkipTest("numpy or pandas is not installed")

    class T(tqdm):
        @staticmethod
        def pandas(deprecated_t):
            assert deprecated_t.__class__ == tqdm

    tqdm_pandas(T)
    tqdm_pandas(tqdm)
    try:
        tqdm_pandas(tqdm, total=1)
    except TypeError as e:
        if "tqdm_pandas() got an unexpected keyword argument 'total'" not in str(e):
            raise e
    else:
        raise Exception

    # Check if it works after a restart:
    import pandas as pd
    import sys
    from tqdm import tq

# Generated at 2022-06-14 13:02:02.701576
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd

    df = pd.DataFrame(range(10), columns=['x'])

    with tqdm(total=len(df), desc='dft') as t:
        tqdm_pandas(t, desc='tft')
        df.groupby('x').progress_apply(lambda x: x, meta='test')
        t.close()

# Generated at 2022-06-14 13:02:10.043716
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import tqdm

    # Test pandas is available
    try:
        import pandas as pd
        from pandas import Series, DataFrame
    except ImportError:
        raise SkipTest

    # Test tqdm.pandas(..., leave=False) (i.e. test that tqdm_pandas(tqdm(...))
    # works too)
    with tqdm.tests.in_completion_context() as ctx:
        tqdm_pandas(tqdm.tqdm(total=1, leave=False))
        assert ctx.status == 'completed'

    # Test tqdm.pandas(...) (i.e. test that tqdm_pandas(tqdm.tqdm.pandas) works
    # too)

# Generated at 2022-06-14 13:02:18.929353
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm.auto import tqdm, trange
    import numpy as np
    tqdm_pandas(tqdm())
    tqdm_pandas(trange())
    tqdm_pandas(tqdm)
    tqdm_pandas((tqdm, trange))

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    # We must use a multi-column groubpy to trigger progress_apply
    # Single-column groupby uses fast C code that doesn't callback to Python
    df.groupby(list(df)).progress_apply(lambda g: g.sum())

    assert True

# Generated at 2022-06-14 13:02:30.802161
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd
    import tqdm
    N = 100
    B = 100
    df = pd.DataFrame({
        'a': np.random.randint(0, N, size=(N,))
    })

    def progress_group(df):
        return df.groupby('a').progress_apply(lambda x: x['a'].sum())

    t_pandas = tqdm.pandas(total=N)
    t_pandas(progress_group)(df)

    # Test function registered with @tqdm_pandas
    t_pandas = tqdm.pandas(total=N, desc=__file__.split('/')[-1])
    t_pandas(progress_group)(df)



# Generated at 2022-06-14 13:02:40.065313
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    df = pd.DataFrame([[0, 1], [1, 2], [2, 3]])
    try:
        df.groupby(0).progress_apply(lambda x: 1)
    except AttributeError:
        return
    try:
        df.groupby(0).progress_apply(lambda x: 1)
    except TypeError:
        return
    from tqdm import tqdm
    df.groupby(0).progress_apply(lambda x: 1)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:45.974805
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
        df = pd.DataFrame([list(range(10)), list(range(10, 20))]).T
        df.progress_apply(np.sum)
        df.progress_apply(np.sum, axis=1)
    except ImportError:
        return
    except Exception:
        print(sys.exc_info())

# Generated at 2022-06-14 13:02:52.889259
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    try:
        import tqdm
    except ImportError:
        return

    df = pd.DataFrame(np.random.randn(1000, 3))
    for prog_k in ["", "tqdm_notebook", "tqdm"]:
        tqdm_pandas(prog_k, leave=False, ascii=True, desc='test')
        tqdm_pandas(prog_k, file=sys.stdout, leave=False, ascii=True,
                    desc='test_out')
        tqdm_pandas(prog_k, leave=False, ascii=True, desc='test_multi')

# Generated at 2022-06-14 13:03:03.844162
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm

    if sys.version_info[0] >= 3:
        from io import StringIO
        # StringIO is not supported in Python2
    else:
        from StringIO import StringIO
        StringIO

    iterable = list(range(10))
    df_input = pd.DataFrame(iterable)

    tqdm_pandas(tqdm, total=10)
    output = pd.DataFrame(df_input.progress_apply(lambda x: x))
    assert iterable == output.values.tolist()

    # Test for `tqdm(total=...)` case
    tqdm_pandas(tqdm(total=10))
    output = pd.DataFrame(df_input.progress_apply(lambda x: x))


# Generated at 2022-06-14 13:03:12.745509
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    import numpy as np

    df = pd.DataFrame(np.random.randn(100, 100))
    t = tqdm.tqdm(total=df.progress_apply(len).sum(),
                  unit='cols')
    df.progress_apply(t.update)
    t.close()
    del t

    df = pd.DataFrame(np.random.randn(100, 100))
    t = tqdm.tqdm(total=100)

    def my_func(x):
        t.update()
        return len(x)

    df.progress_apply(my_func)
    t.close()
    del t
    print("Unit test passed.")



# Generated at 2022-06-14 13:03:27.096619
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function tqdm_pandas.
    """
    from tqdm import tqdm
    import pandas as pd
    import numpy as np
    tqdm_pandas(tqdm, quiet=True)
    rng = pd.date_range(start='2016-04-11', periods=100, freq='D')
    df = pd.DataFrame(data={'a': np.arange(100)}, index=rng)
    df.groupby(df.index.day).apply(lambda x: x)
    tqdm_pandas(tqdm, quiet=True)
    df.groupby(df.index.day).apply(lambda x: x)


if __name__ == '__main__':
    test_tqdm_pand

# Generated at 2022-06-14 13:03:33.483835
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        import random
        test_data = range(0, random.randint(1, 100))
        pandas.groupby(test_data, lambda x: x % 5).progress_apply(
            lambda x: "a" * sum(x))
    except (ImportError, AttributeError):
        pass

test_tqdm_pandas()
del test_tqdm_pandas

# Generated at 2022-06-14 13:03:42.155743
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    ''' Testing tqdm_pandas '''
    sys.stderr.write('Using pandas:\n')
    import pandas as pd
    import pandas.core.groupby
    from tqdm import tqdm
    try:
        from pandas import _config
        assert _config.get_option('mode.chained_assignment') == 'raise'
    except:
        pass
    d = {'a': [1, 2, 3], 'b': [4.0, 5.0, 6.0], 'c': ['7', '8', '9']}
    df = pd.DataFrame(d)
    df = df.astype({'a': int, 'b': float, 'c': str}, copy=False)

# Generated at 2022-06-14 13:03:53.233345
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    n = 100
    import pandas as pd
    assert((pd.DataFrame(np.arange(n))
            .groupby(0).progress_apply(lambda x: x) == 0).all().all())
    assert((pd.DataFrame(np.arange(n))
            .groupby(0).progress_apply(lambda x: x) == 0).all().all())
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", TqdmDeprecationWarning)
        assert((pd.DataFrame(np.arange(n))
                .groupby(0).progress_apply(lambda x: x) == 0).all().all())
        assert((pd.DataFrame(np.arange(n))
                .groupby(0).progress_apply(lambda x: x) == 0).all().all())

# Generated at 2022-06-14 13:03:56.854719
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Unittest for tqdm_pandas (test tqdm_pandas only uses tqdm.pandas())
    from tqdm.contrib import pandas

    tqdm_pandas(pandas)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:05.611471
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm())
    tqdm_pandas(tqdm, total=1000)
    tqdm_pandas(tqdm(), total=1000)
    tqdm_pandas(tqdm, total=1000, file=open(os.devnull, 'w'))
    tqdm_pandas(tqdm(), total=1000, file=sys.stdout)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:12.329318
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    tqdm.tqdm_pandas(tqdm.tqdm())
    df = pd.DataFrame({"a":range(100)})
    df.groupby("a").progress_apply(lambda x:x**2)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:04:22.539088
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    n_rows = 1000000
    n_dfs = 10
    n_cols = 20

    df = pd.DataFrame(
        np.random.randint(0, 100, (n_rows, n_cols)),
        columns=["col_%d" % col for col in range(n_cols)])

    def slow_square(x):
        import time
        time.sleep(.01)
        return x ** 2

    df = pd.concat([df] * n_dfs)

    with tqdm(total=n_dfs) as pbar:
        def wrapped_gen():
            for x in df.groupby(0):
                pbar.update()
                yield x


# Generated at 2022-06-14 13:04:29.192015
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    from tqdm import tqdm, trange

    def test_single():
        with trange(1) as t:
            pandas.Series(range(1)).progress_apply(lambda x: x)
        tqdm(t).monitor_interval = 0

    def test_multiple():
        with tqdm() as t:
            pandas.Series(range(10)).progress_apply(lambda x: x)
        tqdm(t).monitor_interval = 0

    test_single()
    test_multiple()



# Generated at 2022-06-14 13:04:32.332673
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm())

# Generated at 2022-06-14 13:04:44.016201
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    try:
        progress_apply = pandas.core.groupby.DataFrameGroupBy.progress_apply
        progress_apply
    except (AttributeError, NameError):
        return print("Skip function test_tqdm_pandas()")
    with closing(StringIO()) as our_file:
        tqdm_pandas(tqdm(leave=False, file=our_file))
        try:
            _ = progress_apply
        except (AttributeError, NameError):
            return
        test_df = pandas.DataFrame({'col': range(5)})
        with tqdm(total=test_df.shape[0],
                    leave=False,
                    file=our_file) as t:  # Register `t` with `progress_apply()`
            _

# Generated at 2022-06-14 13:04:53.193414
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Example of use

    def func(text):
        import time
        print("inside the function")
        print(type(text))
        print(text)
        time.sleep(2)

    import pandas as pd
    import numpy as np
    df = pd.DataFrame()
    df['Name'] = np.random.randint(10, size=(10000,))
    df['test'] = np.random.randint(10, size=(10000,))
    df.groupby("test").progress_apply(func)


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:03.727148
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    # test basic
    tqdm_pandas(tqdm)
    # test pandas
    tqdm_pandas(tqdm(ascii=True))
    # test delayed
    t = tqdm(ascii=True, mininterval=0)
    tqdm_pandas(t.__class__)
    # test delayed class
    tqdm_pandas(tqdm.__class__)

numpy_imported = False
try:
    import numpy as np
    numpy_imported = True
except ImportError:
    pass

# Tests
if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:16.421588
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Only tests that the function is called without error
    """
    from tqdm.auto import tqdm
    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm, desc="Dummy desc", leave=False, position=0)
    tqdm_pandas(tqdm(desc="Dummy desc", leave=False, position=0),
                desc="Dummy desc", leave=False, position=0)
    from tqdm import tqdm_notebook
    tqdm_pandas(tqdm_notebook)
    tqdm_pandas(tqdm_notebook, desc="Dummy desc", leave=False, position=0)

# Generated at 2022-06-14 13:05:22.876157
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    class Test:
        @staticmethod
        def progress_apply(self, func, axis=0, raw=False, result_type=None,
                           args=(), kwds={}):
            """
            Similar to pandas.DataFrame.apply.

            Parameters
            ----------
            func : function
                Can be a Series, DataFrame, or Panel object

            Additional keyword arguments to be passed to `func`

            Returns
            -------
            result : Series, DataFrame or Panel
            """

            from pandas.core.base import PandasObject

            if axis == 0:
                axis = 1
            else:
                axis = 0

            assert isinstance(self, PandasObject), 'must be a Pandas object'
            result = self.apply

# Generated at 2022-06-14 13:05:30.301472
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import numpy as np
    import pandas as pd

    N = int(1e6)
    df = pd.DataFrame({
        'A': [x for x in range(N)],
        'B': [np.NaN for _ in range(N)]})

    tqdm_pandas(tqdm(smoothing=0.))
    df.groupby('A').progress_apply(lambda x: x.B.fillna(method='ffill'))

    from tqdm.utils import _term_move_up as tmud

    # static
    class DummyTqdmStatic:
        """
        Fake static tqdm class for testing function ``tqdm_pandas``
        """


# Generated at 2022-06-14 13:05:38.180111
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    try:
        import numpy as np
    except ImportError:
        return
    try:
        df = pd.DataFrame(np.random.choice(50, size=(100, 4)))
        # DataFrameGroupBy.progress_apply
        df.groupby(0).progress_apply(lambda x: x ** 2)
        [df.groupby(c).progress_apply(lambda x: x ** 2) for c in df]
        df.groupby([0, 1]).progress_apply(lambda x: x ** 2)
        # TODO: DataFrame.progress_apply
    except Exception:
        return

# Generated at 2022-06-14 13:05:41.546651
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm
    tqdm_pandas(tqdm)
    # tqdm.pandas()


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:05:52.653925
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas"""

# Generated at 2022-06-14 13:06:01.459714
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import io
    import pandas as pd
    from tqdm import trange

    # test tqdm_pandas(tclass)
    buffer = io.StringIO()
    for i in trange(10, desc='foo', file=buffer):
        pass
    assert len(buffer.getvalue().strip().split('\n')) == 10

    df = pd.DataFrame({'a': list(range(10))})
    buffer = io.StringIO()
    tqdm_pandas(trange, desc='foo', file=buffer)
    df.groupby('a').progress_apply(lambda x: x)
    assert len(buffer.getvalue().strip().split('\n')) == 10

    # test tqdm_pandas(tqdm(...))
    buffer = io.StringIO

# Generated at 2022-06-14 13:06:12.825912
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm_pandas

    for tqdm in [tqdm, tqdm_pandas(tqdm)]:  # test with and without delayed adapter
        df = pd.DataFrame({'x': range(10000)})
        list(tqdm(df.groupby('x')))

    tqdm_pandas(tqdm, total=20)
    tqdm_pandas(tqdm(total=20))


# Generated at 2022-06-14 13:06:24.548638
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    df = pd.DataFrame({"x": np.random.random(100),
                       "y": np.random.random(100)})
    df1 = df.groupby("x", as_index=False).progress_apply(lambda x: x.sort_values("y"))
    df2 = df.groupby("x", as_index=False).progress_apply(lambda x: x.sort_values("y"))
    tqdm_pandas(tqdm.tqdm, desc="test")
    df3 = df.groupby("x", as_index=False).progress_apply(lambda x: x.sort_values("y"))

# Generated at 2022-06-14 13:06:34.760135
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, trange
    import pandas as pd

    class DummyPandasGroupby(object):  # Dummy to prevent pandas imports
        def progress_apply(self, *args, **kwargs):
            assert 'leave' not in kwargs
            assert 'desc' not in kwargs
            assert args == (lambda *args: None,)
            return

    df = pd.DataFrame()
    df.groupby(lambda *args: None).progress_apply(lambda *args: None)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        tqdm_pandas(trange, 'Desc', total=10)
        tqdm_pandas(tqdm, 'Desc', total=10)


# Generated at 2022-06-14 13:06:45.410367
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    df = pd.DataFrame({'A': range(1000)})
    # Skip test on Python 3.8+ as it changes the progress bar coloring
    min_py_version = (3, 8)
    if sys.version_info[0:2] >= min_py_version:
        tqdm_pandas(tclass=pd.DataFrame, file=sys.stderr)
        df.progress_apply(lambda x: x)
    else:
        with pytest.deprecated_call():
            tqdm_pandas(tqdm, file=sys.stderr)
            df.progress_apply(lambda x: x)

# Generated at 2022-06-14 13:06:50.615473
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.std import tqdm
    from tqdm import tqdm_pandas
    import sys

    sys.stderr = sys.stdout
    df = pd.DataFrame({
        'letter': 'abcdefghijklmnopqrstuvwxyz',
        'value': np.random.randint(0, 100, 26)
    })
    tqdm.pandas(tqdm_pandas)

    def add_one(x):
        import time
        time.sleep(0.01)
        return x + 1

    df.groupby('letter').progress_apply(add_one)

# Generated at 2022-06-14 13:07:00.826886
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    # Delayed case
    tqdm_pandas(tqdm, bar_format='{l_bar}{bar}|')
    # Non-delayed case
    tqdm_pandas(tqdm(total=42, dynamic_ncols=True))
    tqdm_pandas(tqdm(total=42, dynamic_ncols=True), smoothing=1.)
    tqdm_pandas(tqdm(total=42, dynamic_ncols=True), leave=False)
    tqdm_pandas(tqdm(total=42, dynamic_ncols=True), bar_format='{l_bar}{bar}|')
    tqdm_pandas(tqdm(total=42, dynamic_ncols=True), ascii=True)


# Generated at 2022-06-14 13:07:07.040354
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from pandas.core.groupby import DataFrameGroupBy
    from tqdm import tqdm, trange

    tqdm_pandas(tqdm)
    assert hasattr(tqdm, "pandas")
    assert hasattr(DataFrameGroupBy, "progress_apply")

    tqdm_pandas(trange)
    assert hasattr(trange, "pandas")
    assert hasattr(DataFrameGroupBy, "progress_apply")

    def _test_deprecated_usecase(tclass):
        try:
            tqdm_pandas(tclass)
            assert hasattr(tclass, "pandas")
        except DeprecationWarning:
            pass

    _test_deprecated_usecase(tqdm)
    _test

# Generated at 2022-06-14 13:07:17.089387
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return None
    import numpy as np
    from tqdm.autonotebook import tqdm
    df = pd.DataFrame(index=[0, 1, 2, 3, 4], data=dict(a=[0, 1, 2, 3, 4],
                                                       b=[0, 1, 2, 3, 4]))
    for cls in [tqdm, tqdm.__class__]:
        tqdm_pandas(cls)
        assert np.all(df.groupby('a').progress_apply(sum) == df.groupby('a').apply(sum)), \
            "tqdm_pandas failed"


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:07:27.969154
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from pandas import DataFrame, Series
    from tqdm import tqdm_notebook

    df = DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [6, 7, 8]},
                   index=['X', 'Y', 'Z'])

    # Test deprecated Pandas 1.x interface
    for _ in tqdm_pandas(df.groupby('a')):
        pass

    # Test deprecated Pandas 2.x interface
    for _ in tqdm_pandas(df.groupby('a').progress_apply(lambda _: None)):
        pass

    # Test tqdm as class decorator

# Generated at 2022-06-14 13:07:35.441983
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for tqdm_pandas()"""
    import pandas as pd
    from tqdm.auto import tqdm
    tqdm.pandas(desc='Loading data...')
    df = pd.read_csv('https://raw.githubusercontent.com/chendaniely/pandas_for_everyone/master/data/gapminder.tsv',
                     sep='\t')
    print(df.groupby('continent')['lifeExp'].progress_apply(
        lambda x: x.mean()).reset_index())

# Generated at 2022-06-14 13:07:53.503027
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """ 
    Unit test for function tqdm_pandas()
    """
    from tqdm.contrib.tests import pretest_posttest_testsuite
    from tqdm.contrib.tests import pandas_installed


    @pretest_posttest_testsuite
    def test_tqdm_pandas_():
        "test that tqdm_pandas() registers with DataFrameGroupBy.progress_apply"
        if not pandas_installed:
            return

        import pandas as pd
        import tqdm
        df = pd.DataFrame({'a': range(100000), 'b': range(100000, 200000)})
        tqdm.tqdm.pandas(tqdm.tqdm, leave=False)

# Generated at 2022-06-14 13:08:00.908622
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np

    def f(x):
        # slow function to test for progression bars
        for i in range(int(4e6)):
            x = i * np.exp(i)
        return x

    with tqdm(total=100) as pbar:
        pbar.set_description("tqdm_pandas")
        df = pd.DataFrame(np.random.randn(100, 3))
        df.progress_apply(f)



# Generated at 2022-06-14 13:08:04.606642
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame

    class A:
        def progress_apply(self):
            print('progress_apply()')

    tqdm_pandas(tqdm(desc='test'))
    tqdm_pandas(tqdm)
    tqdm_pandas(A)

# Generated at 2022-06-14 13:08:15.499156
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from tqdm import tqdm, tqdm_notebook
    from pandas import DataFrame

    df = DataFrame({'A': [1, 2], 'B': [3, 4]})
    df.groupby('A').progress_apply(lambda x: x)
    tqdm_pandas(tqdm)
    df.groupby('A').progress_apply(lambda x: x)

    # in Jupyter notebook, tqdm_notebook is a context manager
    try:
        with tqdm_notebook():
            df.groupby('A').progress_apply(lambda x: x)
    except TypeError:
        pass


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:26.568865
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import read_csv
    from tqdm import trange

    N = len(read_csv('test_pandas.csv')['values'])

    for _ in trange(2, ncols=80):
        for _ in tqdm(read_csv('test_pandas.csv')['values'],
                      total=N, ncols=80):
            pass

        tqdm.pandas(desc='Progress:')
        read_csv('test_pandas.csv').progress_apply(lambda x: x)

    trange.pandas(desc='Progress:')
    read_csv('test_pandas.csv').progress_apply(lambda x: x)


# to be deleted when version gets bumped

# Generated at 2022-06-14 13:08:32.001279
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    assert tqdm_pandas(TqdmTypeError('ERROR'))
    assert tqdm_pandas(TqdmTypeError)
    assert tqdm_pandas(tqdm_foo(TqdmTypeError))


if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:42.296369
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm.contrib.tests import _range
    df1 = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))

    # Register tqdm instance
    tqdm_pandas(tqdm)

    # Now you can use `progress_apply`
    df2 = df1.copy()
    df2.progress_apply(lambda x: x**2)
    df3 = df1.copy()
    df3.progress_apply(lambda x: x**2, axis=1)

    # Unit test
    assert_equal(df1.apply(lambda x: x**2), df2)

# Generated at 2022-06-14 13:08:46.232260
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(tqdm)
    # tqdm_pandas(tqdm.tqdm)
    tqdm_pandas(tqdm(range(10)))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:49.741580
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas

    tqdm_pandas(pandas.core.groupby.DataFrameGroupBy.progress_apply,
                pd=True,
                file=sys.stdout)

# Generated at 2022-06-14 13:08:52.585406
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.rand(1000,1000), columns=list('ABCDEFGH'))
    df.groupby('A').progress_apply(lambda x: x)
    df.groupby('A').progress_apply(tqdm_pandas, lambda x: x)

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:11.342044
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        print("\nSkip function `tqdm_pandas()`, because `pandas` is not installed.")
        return

    def _test(t):
        pd.DataFrame([[1, 2], [3, 4]]).groupby(1).progress_apply(lambda x: x)

    with closing(StringIO()) as our_file:
        tqdm_pandas(tqdm(desc='Yay', file=our_file), unit='bytes')
        _test(tqdm)
        assert "Yay: 100%|##########| 2/2 [00:00<00:00, ?it/s]\n" in our_file.getvalue()


# Generated at 2022-06-14 13:09:23.982159
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        try:
            import pandas  # NOQA
        except ImportError:
            raise unittest.SkipTest()
        else:
            raise
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame({'a': [0, 1],
                       'b': [1., 2.]})

    with tqdm(leave=False, ncols=0, smoothing=0, total=3, disable=False) as t:
        def tqdm_bar(__, progress_bar):
            progress_bar.update()

        tqdm.pandas(tqdm_bar)
        assert hasattr(df.groupby('a').progress_apply, '__wrapped__')

        pd

# Generated at 2022-06-14 13:09:29.958078
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import tqdm
    tqdm_pandas(tqdm)
    with tqdm.tqdm_notebook(total=len(pd.DataFrame(range(0)))) as t:
        pd.DataFrame(range(0)).progress_apply(lambda a: t.update())



# Generated at 2022-06-14 13:09:40.303019
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    df = pd.DataFrame({'a': np.random.randint(1, 10, size=100)})

    def slow_inc(x):
        _ = tqdm.sleep(0.01)
        return x + 1

    tqdm_pandas(tqdm())
    assert (df.groupby('a').progress_apply(slow_inc) == df.groupby('a').apply(slow_inc)).all()

    tqdm_pandas(tqdm(leave=False))
    assert (df.groupby('a').progress_apply(slow_inc) == df.groupby('a').apply(slow_inc)).all()

    tqdm_pandas(tqdm)


# Generated at 2022-06-14 13:09:43.770993
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""

    from tqdm.tests import _test_tqdm_pandas
    _test_tqdm_pandas(tqdm_pandas)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:51.701461
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import io
    import tqdm

    # delayed adapter case
    f = io.StringIO()
    try:
        tqdm.tqdm(ascii=True, file=f, ncols=100)('hello')
        tqdm.tqdm_pandas(tqdm.tqdm, ascii=True)
        assert f.getvalue() == '\r|hello| 100%||5.00/5.00 [00:00<00:00,  5.00it/s]\n'
    except AttributeError:
        tqdm._deprecated_range()
        tqdm.tqdm_pandas(tqdm._deprecated_range, ascii=True)
    finally:
        f.close()

    # deprecated tqdm case

# Generated at 2022-06-14 13:09:58.664739
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    JSON_PATH = "../data/train.json"

    tqdm_pandas(tqdm.tqdm,
                tqdm.tqdm.pandas(
                    tqdm.tqdm.pandas.read_json(JSON_PATH, lines=True, chunksize=2)
                    ))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:07.859728
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm.auto import trange

    try:
        from pandas.core.groupby import DataFrameGroupBy
        DataFrameGroupBy.progress_apply = tqdm_pandas(
            tqdm(desc='GroupBy_progress_apply', leave=False))
    except ImportError:
        pass

    try:
        from pandas.core.groupby import SeriesGroupBy
        SeriesGroupBy.progress_apply = tqdm_pandas(
            trange(desc='SeriesGroupBy_progress_apply', leave=False))
    except ImportError:
        pass


# Generated at 2022-06-14 13:10:19.838626
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        from pandas import DataFrame
        from numpy.random import randint
        import pandas as pd
    except:
        return

    data = DataFrame(randint(0, 100, (1000, 3)), columns=['a', 'b', 'c'])
    groups = data.groupby('a')

    progressbar = tqdm_pandas(range(len(groups)))
    result = groups.progress_apply(lambda x: x['b'] / x['c'].sum(),
                                   progressbar=progressbar)
    assert isinstance(result, pd.Series)
    progressbar.close()

    progressbar = tqdm_pandas(range(len(groups)))

# Generated at 2022-06-14 13:10:32.166363
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    df = pandas.DataFrame({"Group": ["A", "A", "B", "B", "B", "C", "C"],
                       "Integer": [1, 2, 3, 4, 5, 6, 7]})
    from tqdm import tqdm, tqdm_notebook, tqdm_pandas
    from time import sleep

    def f(x):
        sleep(0.01)
        return x

    # Use the function tqdm_pandas
    tqdm_pandas(tqdm())
    # Or use the following:
    # tqdm.pandas(tqdm())
    df.groupby("Group").progress_apply(f)

    # Or use the following:
    # tqdm.pandas(tqdm_notebook

# Generated at 2022-06-14 13:10:57.830564
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm, trange
    from tqdm.pandas import tqdm_pandas
    df = pd.DataFrame(np.random.randn(1000, 4))
    df.head()
    
    with trange(10) as t:
        for i in t:
            t.set_description('GEN %i' % i)
            df.progress_apply(lambda x: x ** 2)
    
    tqdm_pandas(tqdm(total=df.memory_usage().sum()))
    df.progress_apply(lambda x: x ** 2)

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:11:03.378985
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    >>> import tqdm
    >>> try:
    ...     import pandas
    ... except ImportError:
    ...     raise unittest.SkipTest("no pandas to test")
    >>> df = pandas.DataFrame({'a': range(100), 'b': range(100)})
    >>> df.groupby('a').progress_apply(lambda x: x.sum())
    10it [00:00,  9.95it/s]
    """

# Generated at 2022-06-14 13:11:13.774232
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest("skipping pandas tests (requires pandas)")
    tqdm_pandas(tqdm, smoothing=0)
    tqdm_pandas(tqdm(leave=False), smoothing=0)
    tqdm_pandas(tqdm, total=10, smoothing=0)
    tqdm_pandas(tqdm(leave=False), total=10, smoothing=0)
    tqdm_pandas(tqdm(leave=False), smoothing=1)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', TqdmDeprecationWarning)
        df = pd.DataFrame({'a': range(6)})


# Generated at 2022-06-14 13:11:22.193226
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    from tqdm import tnrange, tqdm_notebook

    # Function to test
    def func(x, y=4):
        return (x + y)
    # Function to test
    def func_2(x, y=2):
        return (x + y)

    tqdm_pandas(tqdm)
    tqdm_pandas(tnrange)
    tqdm_pandas(tqdm_notebook)

    # Test the function on a pandas dataframe
    # Function takes rows as pandas series and returns pandas series
    df = pd.DataFrame({'a': [2, 4, 6, 8], 'b': [4, 6, 8, 10]})

# Generated at 2022-06-14 13:11:32.746218
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas"""
    from tqdm import tqdm, tqdm_pandas
    import pandas as pd
    import numpy as np
    tqdm(pd.DataFrame([i for i in np.arange(100)]).groupby(0).progress_apply(lambda x: x))
    tqdm_pandas(pd.DataFrame([i for i in np.arange(100)]).groupby(0).progress_apply(lambda x: x))
    tqdm_pandas(tqdm(pd.DataFrame([i for i in np.arange(100)]).groupby(0).progress_apply(lambda x: x)))


if __name__ == '__main__':
    from tqdm import tqdm_pandas
    t

# Generated at 2022-06-14 13:11:35.816612
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import tqdm as tqdm
        import pandas as pd
    except ImportError:
        return
    try:
        pd.DataFrame([1, 2, 3]).progress_apply(lambda x: x * 2)
    except AttributeError:
        tqdm.pandas(smoothing=1)
    finally:
        pd.DataFrame([1, 2, 3]).progress_apply(lambda x: x * 2)

# Generated at 2022-06-14 13:11:44.383208
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    '''Test tqdm_pandas function, this function is purely for backward
    compatibility and will be deprecated in the future.'''
    try:
        import pandas as pd
        import numpy as np
        from tqdm import tqdm, tqdm_notebook
    except ImportError:
        return
    from pandas.core.groupby import DataFrameGroupBy
    from pandas.core.frame import DataFrame

    iframe = pd.DataFrame({'a': np.random.randint(0, 100, 100)})
    dfg = iframe.groupby(['a'])

    def apply_f(df):
        return df.a.sum()

    def apply_f_kw(df, k=0):
        return df.a.sum() + k
