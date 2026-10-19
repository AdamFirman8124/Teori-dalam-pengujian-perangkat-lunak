

# Generated at 2022-06-14 13:01:39.945505
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas."""
    # should be compatible in Python 2 and 3
    # ==> also, no need to do explicit test on version
    import pandas as pd
    tqdm_pandas(pd.DataFrame({'1': [1], '2': [2]}).groupby('1'))
    tqdm_pandas(pd.DataFrame(
        {'1': [1], '2': [2]}).groupby('1'), desc='test_pandas')
    tqdm_pandas(pd.DataFrame(
        {'1': [1, 1, 1], '2': [2, 2, 2]}).groupby('1').progress_apply(lambda x: x),
        desc='test_pandas')
    tqdm_pandas

# Generated at 2022-06-14 13:01:49.904378
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm.pandas import tqdm_pandas
    from tqdm._utils import _range

    df = pd.DataFrame(dict(a=_range(10), b=_range(10, 20), c=_range(20, 30)))

    for t in [tqdm, tqdm_notebook, tqdm_gui]:
        t.pandas(desc="test1")
        df.groupby("a").progress_apply(max)
        t.pandas(leave=False, desc="test2_a")
        df.groupby("a").progress_apply(min)
        t.pandas(leave=True, desc="test2_b")
        df.groupby("a").progress_apply

# Generated at 2022-06-14 13:01:59.637430
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with pytest.raises(TqdmDeprecationWarning):
        with tqdm.pandas(tqdm_cls=tqdm) as t:
            tqdm_pandas(tqdm, total=10)

        with tqdm.pandas(tqdm_cls=tqdm) as t:
            tqdm_pandas(t, total=10)

        with tqdm.pandas(tqdm_cls=tqdm) as t:
            tqdm_pandas(tqdm_pandas, tqdm_cls=tqdm)


# Generated at 2022-06-14 13:02:05.668236
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tclass = type
    assert tclass.pandas(deprecated_t=tclass) and tqdm_pandas(tclass)
    if IS_PYPY:
        return

    tclass = tqdm()
    tclass.pandas(deprecated_t=tclass)
    tqdm_pandas(tclass)


# Adapter for pandas

# Generated at 2022-06-14 13:02:10.032293
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    try:
        import pandas
    except ImportError:
        return
    from pandas.core.groupby import DataFrameGroupBy
    if DataFrameGroupBy is not None:
        tqdm_pandas(tqdm)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:16.544731
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_gui

    # Test tqdm_pandas(tqdm_gui, ...)
    try:
        import pandas
        df = pandas.DataFrame({'a': [1] * 5, 'b': [2] * 5})
        tqdm_pandas(tqdm_gui, desc='test')
        df.groupby('a').progress_apply(lambda x: x)
    except ImportError:
        print('Skipping pandas test')

# Generated at 2022-06-14 13:02:21.306703
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    ret = tqdm_pandas(tqdm)
    assert ret is None
    ret = tqdm_pandas(tqdm(unit='foo'))
    assert ret is None
    with pytest.raises(TypeError):
        tqdm_pandas(tqdm, unit='foo')


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:02:29.794409
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm_pandas
    from tqdm import tqdm
    import pandas as pd

    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm())

    # Bumblebee's test
    df = pd.DataFrame(data=[1, 2, 3, 4, 5, 6, 7, 8, 9], columns=['number'])
    df.groupby(by=df.number % 2).progress_apply(lambda x: x**2)

# Generated at 2022-06-14 13:02:39.424871
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    df = pd.DataFrame({'x': [1, 2, 3, 4, 5]})
    try:
        tqdm_pandas(df.groupby('x').progress_apply(lambda x: x))
    except AttributeError:
        return
    tqdm_pandas(tqdm.tqdm, df.groupby('x').progress_apply(lambda x: x))

# Generated at 2022-06-14 13:02:49.590107
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame, Series

    with tqdm(total=1) as _:
        # Will auto-register `tqdm` instance
        tqdm_pandas(tqdm)

        df = DataFrame(
            {'col1': list(Series(range(1000))), 'col2': list(range(1000))})

        # Should now be a `DataFrameGroupBy` attribute
        # Will use `tqdm` instance to update progress
        if hasattr(df, 'progress_apply'):
            df.groupby('col1').progress_apply(lambda x: x)
        else:
            df.groupby('col1').apply(lambda x: x)

    assert True


if __name__ == '__main__':
    test_tqdm

# Generated at 2022-06-14 13:03:02.243510
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        import numpy as np
        from tqdm import tqdm
        x = np.arange(100)
        x = pd.DataFrame(x)
        t = tqdm(total=len(x))
        tqdm_pandas(t)
        t.close()
    except Exception:
        return False
    else:
        return True


if __name__ == '__main__':
    from time import sleep
    from pandas import DataFrame
    from numpy import arange

    x = DataFrame(arange(10000).reshape(1000, 10))

    for _ in tqdm(x.groupby(0)):
        # Do some computation
        sleep(0.001)

# Generated at 2022-06-14 13:03:12.665253
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from numpy import random
    from tqdm import tqdm, tqdm_pandas
    tqdm_pandas(tqdm)

    df = DataFrame(random.randint(0, 100, (100000, 6)))
    df.groupby(0).progress_apply(lambda x: x ** 2)


if __name__ == '__main__':
    from time import sleep

    from pandas import DataFrame
    from numpy import random
    from tqdm import tqdm, tqdm_pandas

    tqdm_pandas(tqdm)

    df = DataFrame(random.randint(0, 100, (100000, 6)))
    result = df.groupby(0).progress_apply(
        lambda x: x ** 2)

# Generated at 2022-06-14 13:03:24.722473
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import numpy as np
        import pandas as pd
    except ImportError:
        raise SkipTest

    from tqdm import tqdm

    # for delayed adapter case
    tqdm_pandas(tqdm)

    # for delayed adapter case
    from tqdm.autonotebook import tqdm as tqdm_notebook
    tqdm_pandas(tqdm_notebook)

    # for functional case
    tqdm_pandas(tqdm())


test_tqdm_pandas()
del test_tqdm_pandas

# #############################################################################
# Main
# #############################################################################



# Generated at 2022-06-14 13:03:33.535037
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    t = tqdm(total=4)
    import pandas as pd
    pd.util.testing.N = 10
    df = pd.util.testing.makeDataFrame()
    gg = df.groupby(['A', 'B'])
    tqdm_pandas(t)(gg.progress_apply)
    assert t.n == 4, "tqdm_pandas: test failed"

if __name__ == "__main__":
    test_tqdm_pandas()

# Generated at 2022-06-14 13:03:42.195533
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    df = pd.DataFrame(
        {
            'a': [1, 2, 3],
            'b': [4, 5, 6],
            'c': [7, 8, 9],
            'd': [9, 8, 7],
        },
        index=['First', 'Second', 'Third']
    )

    t = tqdm(ascii=True)
    t.pandas(df.groupby('a').progress_apply(lambda x: x.d.sum()))
    t = tqdm(ascii=True)
    t.pandas(df.groupby('a').progress_apply(lambda x: x.d.sum()))
    t = tqdm(ascii=True)

# Generated at 2022-06-14 13:03:53.275586
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas
    from tqdm import tqdm
    from tqdm import tqdm_pandas
    from tqdm.contrib.tests import discretize, discretize_numpy

    # Series
    df = pandas.DataFrame(discretize())
    tqdm_pandas(tqdm(total=df.index.size))
    df.groupby(0).progress_apply(lambda x: x)

    # DataFrame
    df = pandas.DataFrame(discretize())
    tqdm_pandas(tqdm(total=df.index.size))
    df.progress_apply(lambda x: x, axis=1)

    # Numpy
    df = pandas.DataFrame(discretize_numpy())

# Generated at 2022-06-14 13:04:00.136665
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    from tqdm._utils import _term_move_up

    try:
        from pandas.core.groupby import DataFrameGroupBy
        if sys.version_info[:2] < (3, 3):
            raise ImportError
    except ImportError:
        return

    with tqdm(total=1) as bar:
        bar.set_description('testing tqdm_pandas')
        # register a non-delayed tqdm instance
        tqdm_pandas(bar)
        df = pd.DataFrame(dict(a=range(1, 6), b=range(6, 0, -1)))
        # test no-progress-bar-yet case

# Generated at 2022-06-14 13:04:08.866435
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
    except ImportError:
        return
    from tqdm.auto import tqdm
    from tqdm.pandas import tqdm_pandas

    iterations = 10000
    df = pandas.DataFrame({"x" + str(i): range(iterations) for i in range(10)})

    for tclass in [tqdm, lambda: tqdm(**defaults)]:
        df.groupby("x4").progress_apply(
            lambda x: tclass().update(sum(x)))  # noqa
        if hasattr(df, "progress_apply"):
            df.progress_apply(lambda x: tclass().update(sum(x)))  # noqa

# Generated at 2022-06-14 13:04:16.970912
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return
    tqdm_pandas(tqdm)
    assert hasattr(pd.DataFrame.progress_apply, 'tqdm_gui')
    assert hasattr(pd.DataFrame.progress_map, 'tqdm_gui')
    # only meaningful if tqdm is imported after tqdm_pandas
    tqdm_pandas(tqdm(total=0))
    assert hasattr(pd.DataFrame.progress_apply, 'tqdm_gui')
    assert hasattr(pd.DataFrame.progress_map, 'tqdm_gui')

# Generated at 2022-06-14 13:04:25.839917
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    from tqdm.autonotebook import tqdm

    df = pd.DataFrame({'name': ['John', 'Jane'], 'age': [23, 29]})

    tqdm_pandas(tqdm)
    assert hasattr(tqdm, 'pandas_deprecated')
    assert not hasattr(tqdm, 'pandas')

    res = df.groupby('name').progress_apply(len)
    assert res.name == 'progress_apply'

    tqdm_pandas(tqdm(desc='ProgressBar'))
    res = df.groupby('name').progress_apply(len)
    assert res.name == 'ProgressBar'

if __name__ == '__main__':
    test_tqdm_pandas

# Generated at 2022-06-14 13:04:39.790226
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm._utils import _supports_unicode
    from tqdm.contrib.concurrent import DummyExecutor, ProcessPoolExecutor, ThreadPoolExecutor

    # Sanity check
    with tqdm(total=100, leave=False) as t:
        for i in t:
            t.update()
            if i >= 10:
                break
    # Test pandas support
    import pandas as pd
    try:
        pd.set_option('compute.use_bottleneck', False)
        pd.set_option('compute.use_numexpr', False)
        pd.set_option('compute.use_numba', False)
        pd.set_option('compute.use_inference_cache', False)
    except Exception:
        pass
    df = p

# Generated at 2022-06-14 13:04:46.342325
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from pandas import DataFrame
    import pandas.core.groupby.groupby
    import numpy as np
    # Test with direct function call
    tqdm_pandas(tqdm)
    DataFrame(np.random.rand(1000, 2)).groupby(0).progress_apply(lambda x: x)
    # Test with delayed adapter
    tqdm_pandas(tqdm_pandas)
    DataFrame(np.random.rand(1000, 2)).groupby(0).progress_apply(lambda x: x)

# Generated at 2022-06-14 13:04:58.763763
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    import numpy as np

    pd.DataFrame(np.ones((100, 100))).progress_apply(lambda x: x)

    import pandas

    df = pandas.DataFrame({'a': range(100), 'b': range(100)})

    with tqdm_pandas(
            pandas.core.groupby.DataFrameGroupBy.progress_apply,
            file=sys.stdout) as t:
        trange = t(df.groupby('a'),
                   lambda _: pandas.DataFrame(np.random.randint(10, size=(100,
                                                                           100))))
        assert isinstance(trange, type(t))
        assert hasattr(trange, 'n') and trange.n == 100


# Generated at 2022-06-14 13:05:09.235043
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm.utils import _term_move_up
    from pandas import DataFrame, Series
    from numpy import arange, random

    df = DataFrame({'a': [1, 2, 3, 4], 'b': [1, 2, 3, 4]})

    series = Series(arange(42))
    expected = 2 * sum(series)

    with tqdm(total=expected, desc='testing', unit='it') as t:
        actual = df.groupby('a')['b'].progress_apply(lambda x: sum(series))
        t.update(2 * actual.sum())

    print(actual.sum())
    print(actual)


# Generated at 2022-06-14 13:05:21.121293
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm.pandas import tqdm_pandas
    import numpy as np
    tqdm_pandas(range(3), total=3)
    tqdm_pandas(type(tqdm_pandas), total=3)
    tqdm_pandas(tqdm_pandas(total=3))

# Generated at 2022-06-14 13:05:28.497066
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    try:
        from tqdm.contrib.test import closing
        tqdm_kwargs = dict(total=10, desc='test', mininterval=0.01)
    except ImportError:
        from contextlib import closing
        tqdm_kwargs = dict(total=10, desc='test', mininterval=0.01, ncols=80)
    with closing(tqdm_pandas(**tqdm_kwargs)) as t:
        pd.DataFrame(np.random.rand(100000, 3)).groupby('a').progress_apply(
            lambda x: len(x))

# Generated at 2022-06-14 13:05:34.280405
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas
        pandas  # to avoid "imported but unused" warning in PyCharm
    except ImportError:
        import pytest
        pytest.skip('pandas not installed')
        return
    import pandas as pd
    import numpy as np
    from tqdm.auto import tqdm
    # TODO: random segfaults (pandas.errors.ComplexWarning)
    # pandas.options.mode.chained_assignment = None  # default='warn'
    a = pd.DataFrame({'a': list(range(10000))})
    b = pd.DataFrame({'b': np.random.randn(10000)})

# Generated at 2022-06-14 13:05:40.467896
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas
    import pandas as pd
    import numpy as np
    from time import sleep

    x = np.random.normal(size=10)
    df = pd.DataFrame({'x': x})
    y = df.x.progress_apply(lambda x: sleep(0.1 * x))

    tqdm_pandas(tclass=tqdm, leave=True)
    z = df.x.progress_apply(lambda x: sleep(0.1 * x))

    assert y.equals(z)

    tqdm_pandas(tclass=True)
    z = df.x.progress_apply(lambda x: sleep(0.1 * x))
    tqdm_pandas(tclass=False)

    assert y.equ

# Generated at 2022-06-14 13:05:51.802124
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import io
    import sys

    class DummyTqdmFile(io.StringIO):
        """Dummy file-like that will write to tqdm"""
        file = None  # type: tqdm.tqdm

        def __init__(self, file):
            self.file = file
            super(DummyTqdmFile, self).__init__()

        def write(self, x):
            # Avoid print() second call (useless \n)
            if len(x.rstrip()) > 0:
                self.file.write(x)

    class dummy_tqdm(object):
        @staticmethod
        def set_description(*_, **__):
            pass

    def has_desc(f):
        return hasattr(f, 'desc')


# Generated at 2022-06-14 13:05:59.381534
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test for function tqdm_pandas()"""
    from tqdm import tqdm, tqdm_pandas, trange
    try:
        import numpy as np
        import pandas as pd
    except ImportError:
        return 0
    for _ in tqdm_pandas(trange(4), file=sys.stdout):
        _ = pd.DataFrame([np.random.random(1000000)])
        _.groupby(0).progress_apply(lambda x: x)
    return 1

if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:06:08.619814
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        # with pandas
        df = pd.DataFrame(np.arange(100), columns=['test'])
        t = tqdm_pandas(tqdm())
        df.groupby(['test']).progress_apply(lambda x: x**2)
        t.close()
        # without pandas
        tqdm_pandas(tqdm())
    except ImportError:
        pass

# Generated at 2022-06-14 13:06:17.895701
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        return  # skipped
    # Enable tqdm_gui for testing
    import os
    os.environ["TQDM_DISABLE_MINITER"] = "1"

    from tqdm import tqdm
    from tqdm._tqdm_gui import tqdm_gui

    for ttype in [tqdm, tqdm_gui]:
        from tqdm.contrib import DummyTqdmFile
        with DummyTqdmFile() as f:
            tclass = ttype(file=f)
            tqdm_pandas(tclass)
            df = pd.DataFrame({'a': range(tclass.total)})
            df.groupby('a').progress_apply(lambda x: x)


# Generated at 2022-06-14 13:06:24.510747
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm_pandas as tp, tqdm, pandas

    import pandas as pd
    import numpy as np

    def delay_calc(p):
        # delay some calculation computation
        delay = p['n'] * 0.01
        progress.update(delay * 1000)
        return delay

    df = pd.DataFrame({
        'n': list(np.random.randint(0, 1000, 100000))
    })
    # Track progress in `progress`
    progress = tqdm(total=100000)

    # Create a tqdm instance with `progress` as its file
    # and use it as an iterator by `pandas.core.groupby.DataFrameGroupBy.progress_apply`

# Generated at 2022-06-14 13:06:34.758802
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series, date_range
    from random import random
    import numpy as np
    from tqdm.autonotebook import tqdm
    from time import sleep
    # Dummy data
    index = date_range('1/1/2000', periods=1000)
    df = DataFrame(
        np.random.randn(1000, 4), index=index, columns=list('ABCD'))
    df = df.rolling(window=20).mean()
    df.A[:50] = np.nan
    df.B[-50:] = np.nan
    # Tests
    # (1) SeriesGroupBy.apply()

# Generated at 2022-06-14 13:06:41.477813
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
        from tqdm import tqdm
        import numpy as np

        def square(x):
            return x ** 2

        # basic test
        df = pd.DataFrame(np.random.rand(10000, 3))
        tqdm_pandas(tqdm(total=len(df.index)), file=sys.stderr)
        df.progress_apply(square)
    except ImportError:
        pass

# Generated at 2022-06-14 13:06:48.447694
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Test for tqdm_pandas, including with deprecated signature."""
    # pylint: disable=import-outside-toplevel
    from tqdm import tqdm
    from pandas import DataFrame, Series
    from pandas.core.groupby import DataFrameGroupBy

    tqdm_pandas(tqdm)
    tqdm_pandas(tqdm(total=5))
    class DummyCls(tqdm):
        pass
    tqdm_pandas(DummyCls)
    tqdm_pandas(DummyCls(total=5))

    df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    count = [0]
    df_

# Generated at 2022-06-14 13:06:59.387844
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm
    import numpy as np
    # with tqdm.pandas()
    tqdm.pandas()
    df = pd.DataFrame({
        'id': np.arange(10),
        'val': np.random.randint(0, 10, (10)),
    })
    df = df.groupby(df.id // 2).progress_apply(lambda x: x * 2)
    # with tqdm.tqdm_pandas(tqdm())
    tqdm_pandas(tqdm())
    df = pd.DataFrame({
        'id': np.arange(10),
        'val': np.random.randint(0, 10, (10)),
    })
    df = df

# Generated at 2022-06-14 13:07:08.417491
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm import tqdm, trange
    from tqdm._tqdm_pandas import _tqdm_pandas_deprecated

    def _test_tqdm_pandas_deprecated():
        for _ in _tqdm_pandas_deprecated(range(3)):
            for i in trange(4):
                pass

    def _test_tqdm_pandas_tclass():
        for _ in tqdm.pandas(range(3)):
            for i in trange(4):
                pass

    # Test deprecated API
    with tqdm(disable=True) as f:
        assert _test_tqdm_pandas_deprecated() == None

# Generated at 2022-06-14 13:07:17.765555
# Unit test for function tqdm_pandas
def test_tqdm_pandas():  # pragma: no cover
    from pandas import DataFrame, Series
    from datetime import timedelta
    from tqdm import tqdm

    # Pandas series
    s = Series(range(3))
    tqdm_pandas(tqdm(), total=s.shape[0])  # init
    s.progress_apply(lambda x: x * 2)
    # Pandas dataframe
    N = 100000
    df = DataFrame({'A': 3, 'B': 'foo', 'C': 1.0 / N, 'D': range(N)})
    df = df.set_index('D')
    tqdm_pandas(tqdm(), total=len(df))  # init
    df.progress_apply(lambda x: x.sum())
    # Pandas dateframe groupby
   

# Generated at 2022-06-14 13:07:28.580166
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit tests for function `tqdm_pandas`.
    """
    import sys
    import types
    import pandas as pd
    from tqdm import tqdm

    assert hasattr(pd.core.groupby.DataFrameGroupBy, 'progress_apply')

    # Test warning
    try:
        sys.stderr.write('<')
        tqdm_pandas(tqdm.tqdm)
    except TqdmDeprecationWarning as e:
        assert str(e) == 'Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.'
    else:
        assert False


# Generated at 2022-06-14 13:07:36.802491
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        tqdm_pandas(tqdm, foo='bar')
        tqdm_pandas(tqdm(foo='bar'))
        assert len(w) == 2

        tqdm_pandas(tqdm_gui)
        assert len(w) == 3

        # The following are deprecated.
        tqdm_pandas(tqdm_notebook)
        assert len(w) == 4

        tqdm_pandas(tqdm_nb)
        assert len(w) == 5


# For compatibility with Python 2.6+:
try:
    from collections import Mapping
except ImportError:
    Mapping = collections.Mapping



# Generated at 2022-06-14 13:07:42.175569
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always', TqdmDeprecationWarning)
        tqdm_pandas(tqdm_gui, foo='bar')
        assert any(
            issubclass(w_.category, TqdmDeprecationWarning)
            for w_ in w)
        assert any('Please use `tqdm.pandas(...)`' in str(w_) for w_ in w)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always', TqdmDeprecationWarning)
        tqdm_pandas(tqdm)
        assert any(
            issubclass(w_.category, TqdmDeprecationWarning)
            for w_ in w)

# Generated at 2022-06-14 13:07:47.102968
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for `tqdm_pandas`.
    """
    # Test cases:
    #  1. Import `tqdm`
    #  2. Import `tqdm.pandas`
    #  3. Import `tqdm_pandas`, initialise a `tqdm` instance, call `tqdm_pandas(t)`
    #  4. Same as (3), but use a newly initialised `tqdm` instance mangled to
    #  look like `tqdm_pandas`
    #  5. Same as (3), but use a `tqdm.pandas` instance
    #  6. Import `tqdm_pandas`, call `tqdm_pandas(tqdm)`
    #  7. Same as (6),

# Generated at 2022-06-14 13:07:56.219960
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    t = tqdm_pandas(tqdm())
    C = t.__class__
    assert C.pandas.__globals__ == {'tqdm': tqdm}
    t = tqdm_pandas(t)  # should be a no-op
    assert t.__class__ == C
    t = tqdm_pandas(tclass=t)  # should be a no-op too
    assert t.__class__ == C
    t = tqdm_pandas(tclass=tqdm)
    assert t.__class__ == tqdm
    t = tqdm_pandas(tqdm)(
        desc="dummy",
        total=123456,
        file=open(os.devnull, 'w'))  # should not raise a

# Generated at 2022-06-14 13:08:04.797899
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import time

    # This is the test:
    def test_pandas_apply(n):
        df = pd.DataFrame({'x': np.random.randn(n)})
        df.groupby(0, sort=False).progress_apply(lambda _: time.sleep(0.01))
        return df

    n = 5

    try:
        with tqdm(total=n, ncols=120) as t:
            for i in range(n):
                t.update()
                test_pandas_apply(10)
        # t.close()
    except AttributeError:
        pass


# Generated at 2022-06-14 13:08:15.604427
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    from tqdm.std import tqdm, tqdm_pandas

    def test_apply(df):
        df = df.apply(lambda x: x ** 2)
        return df

    ###########
    # No tqdm #
    ###########

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))

# Generated at 2022-06-14 13:08:22.963373
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:  # pragma: no cover
        return  # skip tests if not installed

    test_values = list(range(30))

    def test_func(df):
        return len(df)

    df = pd.DataFrame(test_values)
    tqdm_pandas(tqdm_pandas, desc="test")
    df.groupby(df[0] // 2).progress_apply(test_func)

# Generated at 2022-06-14 13:08:30.086910
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from tqdm import tqdm

    df = DataFrame(
        [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']],
        columns=['col1', 'col2', 'col3'],
        index=['indice1', 'indice2', 'indice3', 'indice4'])
    df.groupby(['col1'])['col2'].progress_apply(
        lambda x: 1)  # test if progress_apply exists
    tqdm.pandas(desc='test')
    tqdm.pandas(dynamic_ncols=True)

# Generated at 2022-06-14 13:08:40.724208
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Test the tqdm_pandas decorator.
    """
    import pandas
    df = pandas.DataFrame([[1, 1], [2, 2], [3, 3], [4, 4]], columns=list("ab"))
    df.groupby("a").progress_apply(lambda x: x)
    # Check the registered_tqdms
    try:
        from pandas.core.groupby import DataFrameGroupBy
        assert DataFrameGroupBy.registered_tqdms
    except ImportError:
        pass
    # Check that tqdm_pandas(tqdm()) works
    try:
        tqdm_pandas('tqdm')
    except TypeError:
        pass
    # Check that tqdm_pandas(tqdm) works
    tq

# Generated at 2022-06-14 13:08:47.117885
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import tqdm

    n = 1000000
    tqdm_pandas(tqdm(total=n))
    df = pd.DataFrame({'i': [0.0] * n})
    df['x'] = df['i'].progress_apply(lambda i: i)
    assert df['i'].sum() == df['x'].sum()
    df = pd.DataFrame({'i': [0.0] * n})
    df.progress_apply(lambda i: i + 1)


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:08:59.744059
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    # Test normal case
    try:
        tqdm_pandas(tqdm)
        df = pd.DataFrame(np.arange(24))
        df.groupby(df.index // 6).progress_apply(
            lambda x: np.sum(x ** 2))  # works!
        tqdm.pandas(tqdm)  # to avoid warning
    except Exception:
        raise AssertionError("Test failed")

    # Test delayed adapter case
    try:
        tqdm_pandas(tqdm_gui)
        tqdm.gui.pandas(tqdm_gui)  # to avoid warning
    except Exception:
        raise AssertionError("Test failed")


#

# Generated at 2022-06-14 13:09:11.342449
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        print('Skipping pandas test (pandas not installed)')
        return
    from tqdm import tqdm

    N = 100
    df = pd.DataFrame({'x': [1, 2, 3] * N, 'y': [0] * N + [1] * N + [2] * N})
    assert (
        [i for i in tqdm(df.groupby('y')['x'].progress_apply(sum))] == [N, N, N]
    )
    assert (
        [i for i in tqdm(df.groupby('y')['x'].progress_apply(sum))] == [N, N, N]
    )

# Generated at 2022-06-14 13:09:23.982733
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Tests the function `tqdm_pandas`.
    """
    import os

    sys.path.insert(0, '..')
    from tqdm import tqdm, tqdm_notebook
    from pandas import DataFrame

    try:
        from pandas.core.groupby import DataFrameGroupBy
    except ImportError:
        print("pandas not installed, skipping pandas test")
        return

    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

    # tqdm = tqdm_notebook
    clear()
    print("Progress bar using pandas")
    tqdm_pandas(tqdm)

# Generated at 2022-06-14 13:09:32.905651
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    from tqdm import trange
    dummy_df = pd.DataFrame(range(100), columns=['val'])

    def test_func(df):
        return df

    with trange(10) as t:
        tqdm_pandas(t, dummy_df)
        res = (dummy_df
               .groupby('val')
               .progress_apply(test_func))


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:09:42.237381
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    # define simple function elements
    def test_fn_1(self, x):
        return x

    def test_fn_2(x):
        return x

    # define test data frame
    df = pd.DataFrame({'var1': list(range(10))})
    df = df.groupby(['var1'], as_index=False, group_keys=False)
    df = df.progress_apply(test_fn_1, 1)
    assert list(df['var1']) == list(range(10))
    df = df.progress_apply(test_fn_2, 1)
    assert list(df['var1']) == list(range(10))

    # define test series
    s = pd.Series(list(range(10)))

# Generated at 2022-06-14 13:09:48.453754
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame, Series
    from tqdm import tqdm as _tqdm

    tqdm = _tqdm(range(100))
    test_tqdm_pandas.test_df = DataFrame(Series(range(100)))

    def foo(x):
        return x

    assert hasattr(_tqdm, 'pandas')

    tqdm_pandas(tqdm)
    tqdm_pandas(_tqdm)
    tqdm_pandas.test_df.progress_apply(foo)
    tqdm_pandas(tqdm)
    tqdm_pandas(_tqdm)
    tqdm_pandas.test_df.progress_apply(foo)


# Generated at 2022-06-14 13:10:00.731246
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    tqdm.pandas(desc='test_pandas')
    data = pd.DataFrame({'a': [1, 2, 3, 4, 5],
                         'b': [2, 4, 6, 8, 10],
                         'c': [3, 6, 9, 12, 15]})

    data['d'] = data['b'].progress_apply(lambda x: x ** 2)
    assert data['d'].sum() == 440

    data['d'] = data['b'].progress_apply(lambda x: x + 1)
    assert data['d'].sum() == 45


# Generated at 2022-06-14 13:10:07.878452
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from .tqdm import tqdm, tqdm_pandas
    from pandas import DataFrame
    from numpy.random import random
    import time

    test_df = DataFrame(random((10, 10)))
    for i in range(2):
        tqdm_pandas(lambda x: x, tqdm_kwargs={'desc': 'description {}'.format(i)})
        test_df.progress_apply(lambda x: x)  # noqa: E741
        test_df.progress_apply(lambda x: x, axis=0)  # noqa: E741
        test_df.progress_apply(lambda x: x, axis=1)  # noqa: E741


# Generated at 2022-06-14 13:10:19.843477
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    try:
        import pandas as pd
    except ImportError:
        raise unittest.SkipTest("requires Pandas")

    from tqdm import tqdm

    def f(x):
        """Silly function for testing"""
        for _ in range(int(x) * 10):
            i = 2 ** 31
            while i >= 2:
                i //= 2
        return x

    # Instantiate tqdm
    progressbar = tqdm(total=99)
    progressbar.update(1)

    # Register progressbar with pandas
    tqdm_pandas(progressbar, unit_scale=True)

    # Should have updated progressbar
    df = pd.DataFrame({"x": [29, 51, 23]})
    df["x**2"] = df["x"].progress_apply

# Generated at 2022-06-14 13:10:29.481447
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """Unit test function `tqdm_pandas`"""
    import pandas as pd
    from tqdm.auto import tqdm

    df = pd.DataFrame({'A': range(5)})
    tqdm_pandas(tqdm, total=len(df))

    # Should not raise any exception
    df.groupby('A').progress_apply(lambda x: x)

    # Should not raise any exception
    tqdm.pandas(total=len(df))
    df.groupby('A').progress_apply(lambda x: x)

# Generated at 2022-06-14 13:10:35.019313
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    tqdm_pandas(object())
    
    
    
    
 

# ======================================================================
# %% Descripti

# Generated at 2022-06-14 13:10:42.899193
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    import numpy as np
    import tqdm

    df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)), columns=list('ABCDEF'))
    # Apply "sum" after grouping by "A" with `progress_apply`
    tqdm_pandas(tqdm.tqdm)(df.groupby('A').progress_apply(lambda x: x['B'].sum()))


# Compatibility with old imports
tqdm_pandas.tqdm = tqdm_pandas
tqdm_pandas.tqdm_pandas = tqdm_pandas


if __name__ == '__main__':
    test_tqdm_pandas()

# Generated at 2022-06-14 13:10:52.462624
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from pandas import DataFrame
    from pandas import Series
    from tqdm.auto import trange, tqdm
    import numpy as np
    import pandas as pd

    # Test 1: pandas.DataFrameGroupBy.progress_apply()
    frame = DataFrame({'a': np.arange(100), 'b': np.arange(100)})
    tqdm_pandas(tqdm())
    result = frame.groupby('a').progress_apply(lambda x: Series(x['b']).sum())
    assert isinstance(result, Series)
    assert (result == frame['b'].cumsum()).all()

    # Test 2: pandas.core.groupby.GroupBy.progress_apply()
    frame = DataFrame({'a': np.arange(100)})


# Generated at 2022-06-14 13:10:58.089380
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm
    from tqdm.contrib import DummyTqdmFile
    tqdm_pandas(tqdm, file=DummyTqdmFile())
    tqdm_pandas(tqdm(file=DummyTqdmFile()))

# Generated at 2022-06-14 13:11:07.487929
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    from tqdm import tqdm, tqdm_pandas
    from pandas import DataFrame

    # Test tqdm_pandas on its own
    tqdm_pandas(tqdm_class=tqdm)
    df = DataFrame({'a': list(range(100)), 'b': list(range(100, 200))})
    for _ in df.progress_apply(lambda x: x, axis=0):
        pass
    for col in df.progress_apply(lambda x: x, axis=1):
        pass
    for x in df.progress_apply(lambda x: x['a']):
        pass
    for _, x in df.progress_apply(lambda x: (x['a'], x['b'])):
        pass

# Generated at 2022-06-14 13:11:17.758168
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    """
    Unit test for function `tqdm_pandas`
    """
    import tqdm
    import pandas as pd
    from tqdm import TqdmDeprecationWarning

    with tqdm.tests.clean_writable_directory() as tmp:
        input_file = tmp / 'input.csv'
        output_file = tmp / 'output.csv'

        with open(input_file, 'w') as f:
            for i in range(10):
                f.write(str(i) + "\n")

        df = pd.read_csv(input_file)

        # test for `tqdm.pandas(...)`
        with open(output_file, 'w') as f:
            with pytest.warns(TqdmDeprecationWarning):
                tqdm

# Generated at 2022-06-14 13:11:27.835510
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd

    tqdm_pandas(tqdm_gui())
    tqdm_pandas(tqdm_gui, leave=False)

    tqdm_pandas(tqdm(total=100))
    tqdm_pandas(tqdm(total=100, leave=False))

    tqdm_pandas(tqdm(total=100), Bar=None)

    # Itertools case
    for _ in tqdm_pandas(iterable=pd.DataFrame([[1, 2], [3, 4]]), desc='outer'):
        for _ in tqdm_pandas(iterable=pd.Series([1, 2]), desc='inner'):
            pass


if __name__ == '__main__':
    test_tqdm

# Generated at 2022-06-14 13:11:35.191763
# Unit test for function tqdm_pandas
def test_tqdm_pandas():
    import pandas as pd
    tqdm.pandas()   # tqdm_pandas is deprecated
    df = pd.DataFrame(columns=['a', 'b'])
    df.groupby('a').progress_apply(lambda df: df)
    tqdm.pandas(leave=True)
    df = pd.DataFrame(columns=['a', 'b'])
    df.groupby('a').progress_apply(lambda df: df)


if __name__ == '__main__':
    test_tqdm_pandas()