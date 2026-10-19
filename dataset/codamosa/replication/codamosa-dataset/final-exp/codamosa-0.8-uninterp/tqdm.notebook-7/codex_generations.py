

# Generated at 2022-06-14 13:58:03.346843
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    with tqdm_notebook(total=100) as t:
        for i in range(100):
            t.update(1)

if __name__ == '__main__':
    test_tqdm_notebook()

# Generated at 2022-06-14 13:58:05.137043
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .tests import Tests
    Tests._test_tqdm_notebook___iter__()



# Generated at 2022-06-14 13:58:11.838114
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from collections import namedtuple
    from nose.tools import timed
    from .utils import format_interval

    TestUnit = namedtuple('TestUnit', 'iterable errmsg xerr')

    class TstException(Exception):
        pass

    units = (TestUnit(iterable=tnrange(10),
                      errmsg="Should not raise an exception",
                      xerr=False),
             TestUnit(iterable=tnrange(1, 10),
                      errmsg="Should not raise an exception",
                      xerr=False),
             TestUnit(iterable=tnrange(1, 10, 2),
                      errmsg="Should not raise an exception",
                      xerr=False),
             TestUnit(iterable=tnrange(10),
                      errmsg="Should raise an exception",
                      xerr=True))
    for unit in units:
        err

# Generated at 2022-06-14 13:58:19.007132
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """Unit test for the update method of class tqdm_notebook."""
    from io import StringIO
    from time import time, sleep
    # Create a tqdm_notebook instance
    t = tqdm_notebook(total=100, file=StringIO())
    # Create a tqdm instance (for a comparison)
    s = std_tqdm(total=100, file=StringIO())
    # Go on until a keyboard interrupt is raised
    start = time()
    while True:
        try:
            # Wait 0.01 second
            sleep(0.01)
            # Update the tqdm_notebook instance
            t.update()
            # Update the tqdm instance
            s.update()
        except KeyboardInterrupt:
            # Stop the tqdm_notebook instance
            t.close()


# Generated at 2022-06-14 13:58:24.022043
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    for i in range(2):
        with tqdm_notebook(total=10) as t:
            for _ in t:
                sleep(.1)
                t.reset()
        with tqdm_notebook(total=10) as t:
            for _ in t:
                sleep(.1)
                t.reset(total=100)

# Generated at 2022-06-14 13:58:27.428068
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import time
    # DEPRECATED: tqdm.notebook is not interactive
    # with tqdm.notebook.tqdm(total=10) as pbar:
    with tqdm_notebook(total=10) as pbar:
        for i in range(11):
            pbar.update(1)
            time.sleep(.1)

# Generated at 2022-06-14 13:58:31.221573
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=10) as pbar:
        pbar.write("Hello world")
        pbar.clear()
        assert pbar.desc == ""



# Generated at 2022-06-14 13:58:37.204694
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    with tqdm_notebook(total=100) as t:
        for i in range(100):
            t.update()
    with tqdm_notebook(total=100) as t:
        for i in range(100):
            t.update()
    with tnrange(100) as t:
        for i in range(100):
            t.update()



# Generated at 2022-06-14 13:58:46.601799
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # todo: write unit test
    from tqdm.auto import tqdm_gui
    from .utils import _supports_unicode, _environ_cols_wrapper
    from ._utils import StringIO
    from ._tqdm import TMonitor, TMonitorThread
    _range = range if sys.version_info[0] >= 3 else _range
    with tqdm_gui(total=10, desc=__qualname__) as t:
        for i in _range(10):
            t.update(1)
        assert t.n == 10
        # Test update when total=None
        t.update(1)
        assert not hasattr(t, 'total') or t.total is None
        assert t.n == 11
        # Test reset and total=None
        t.reset()

# Generated at 2022-06-14 13:58:49.258799
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(total=10) as t:
        for i in _range(10):
            t.update()

# Generated at 2022-06-14 13:59:03.295421
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    with tqdm_notebook(total=1) as t:
        pass
    t.close()

# Generated at 2022-06-14 13:59:06.376363
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm(total=2) as pbar:
        assert pbar == pbar.__enter__()
        for _ in pbar:
            pass
        pbar.__exit__(None, None, None)



# Generated at 2022-06-14 13:59:08.597487
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    for _ in tqdm_notebook((x for x in range(5)), unit_scale=True):
        pass


if __name__ == "__main__":
    test_tqdm_notebook___iter__()

# Generated at 2022-06-14 13:59:10.391979
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    tqdm_notebook.status_printer(None, total=1, desc='Testing IPython widget')

# Generated at 2022-06-14 13:59:16.753748
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from contextlib import suppress
    from tqdm import notebook
    t = notebook.trange(10)
    t.reset()
    assert t.n == 0
    t.reset(5)
    assert t.total == 5
    with suppress(AttributeError):  # Jupyter < 4.3.1
        assert t.container.children[0].max == 5
        assert t.container.children[0].value == 0
    t.close()


if __name__ == "__main__":
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 13:59:22.089153
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    # test reset total
    with tqdm_notebook(total=10) as pbar:
        pbar.update(5)
        pbar.reset(total=5)
        assert pbar.total == 5
        pbar.update(5)
    # test reset total to unknown
    with tqdm_notebook() as pbar:
        assert pbar.total is None
        pbar.update(5)
        pbar.reset(total=5)
        assert pbar.total == 5
        pbar.update(5)
        pbar.reset(total=None)
        assert pbar.total is None
        pbar.update(5)
    # test reset total with wrong argument

# Generated at 2022-06-14 13:59:32.465381
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from tqdm import trange
    try:
        from IPython.display import display
    except ImportError:
        display = lambda *x: None
    for bar_style in ['success', 'info', 'warning', 'danger']:
        for msg in ['', 'msg']:
            with trange(2) as t:
                t.set_description('Test')
                if msg:
                    t.set_postfix_str(msg)
                display(t, close=True)
                t.set_postfix_str(msg, refresh=True)
                display(t, bar_style=bar_style)
                assert t.container.children[-2].bar_style == bar_style
                assert t.container.children[-2].value == 1
                display(t, bar_style='success')
                assert t.container

# Generated at 2022-06-14 13:59:37.393688
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep
    from tqdm.autonotebook import tqdm

    with tqdm(total=2, leave=True, file=sys.stdout) as pbar:
        for i in range(3):
            pbar.set_description("Fail")
            sleep(0.01)
            pbar.set_description("")


if __name__ == '__main__':
    test_tqdm_notebook_display()

# Generated at 2022-06-14 13:59:44.159604
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        import pandas as pd
    except ImportError:
        return None

    index = pd.timedelta_range('1 days', periods=100, freq='h')
    s = pd.Series(np.random.randn(len(index)), index=index)

    for i in tqdm(s):
        pass



# Generated at 2022-06-14 13:59:49.972010
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    for i in tqdm_notebook(range(10), leave=True):
        pass

    for i in tqdm_notebook(range(10), leave=False):
        pass

    for i in tqdm_notebook(range(10)):
        pass

    for i in tqdm_notebook(range(10), leave=False):
        break

    for i in tqdm_notebook(range(10)):
        break



# Generated at 2022-06-14 14:00:11.418629
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from random import random
    from time import sleep
    pbar = tqdm_notebook(total=100)
    for i in range(1, 100):
        pbar.update(1)
        sleep(random()*0.01)
    pbar.reset(total=1000)
    for i in range(1, 1000):
        pbar.update(1)
        sleep(random()*0.01)
    pbar.reset()
    pbar.reset(total=1000)
    for i in range(1, 1000):
        pbar.update(1)
        sleep(random()*0.01)
    pbar.close()

# Generated at 2022-06-14 14:00:15.903196
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(total=10) as bar:
        for i in range(10):
            bar.update()
    assert bar.n == 10, "bar.n is %r but should be 10" % bar.n
    assert bar.total == 10, "bar.total is %r but should be 10" % bar.total

# Generated at 2022-06-14 14:00:23.392207
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # default format
    tqdm_notebook.status_printer(None)

    # no total
    tqdm_notebook.status_printer(None, desc="")
    tqdm_notebook.status_printer(None, desc="test")

    # with total
    tqdm_notebook.status_printer(None, total=10)
    tqdm_notebook.status_printer(None, total=10, desc="")
    tqdm_notebook.status_printer(None, total=10, desc="test")

    # with ncols
    tqdm_notebook.status_printer(None, total=10, ncols=20)
    tqdm_notebook.status_printer(None, total=10, ncols=20, desc="")


# Generated at 2022-06-14 14:00:28.324027
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    list(tqdm_notebook(range(50)))
    try:
        for _ in tqdm_notebook(range(1000)):
            1 / 0
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError()
    # th = tqdm_notebook()
    # th.__iter__()



# Generated at 2022-06-14 14:00:36.896179
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    pbar = TqdmHBox()
    # test with a null value (total = 0)
    tqdm_notebook.status_printer(pbar, 0, 'Loading...')
    assert len(pbar.children) == 3
    assert isinstance(pbar.children[0], HTML)
    assert isinstance(pbar.children[1], IProgress)
    assert isinstance(pbar.children[2], HTML)
    assert pbar.children[0].value == 'Loading...'
    assert pbar.children[1].min == 0
    assert pbar.children[1].max == 0
    assert pbar.children[1].value == 0
    assert pbar.children[1].bar_style == 'info'
    assert pbar.children[2].value == ''

    # test with a real value (total

# Generated at 2022-06-14 14:00:40.397227
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test default status printer
    """
    import io
    fp = io.StringIO()
    assert tqdm_notebook.status_printer(fp, total=10)
    assert tqdm_notebook.status_printer(fp, total=100)
    assert tqdm_notebook.status_printer(fp, total=None)



# Generated at 2022-06-14 14:00:52.043215
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from IPython.core.display import display
    from IPython.core.display import clear_output
    from random import randint
    # Reset tqdm_notebook.status_printer
    tqdm_notebook.status_printer = tqdm_notebook.status_printer.__func__
    tqdm_notebook.status_printer()

    # Test with total
    total = randint(5, 10)
    pbar = tqdm_notebook.status_printer(
        None, total=total, ncols=randint(25, 100))
    try:
        clear_output()
        display(pbar)
    except RuntimeError:  # headless
        pbar.layout.display = "none"
        display(pbar)



# Generated at 2022-06-14 14:00:59.296381
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """Test display() method of tqdm_notebook() class"""
    # Check without error
    with tqdm_notebook(range(10), desc='Test desc') as bar:
        for _ in bar:
            bar.display('Test l_bar|<bar/>|Test r_bar')
    # Check with error
    with tqdm_notebook(range(10), desc='Test desc', leave=True) as bar:
        for i in bar:
            bar.display('Test l_bar|<bar/>|Test r_bar')
            if i == 6:
                bar.display('', bar_style='danger')
                raise RuntimeError("Error")
            bar.update()

# Generated at 2022-06-14 14:01:03.662158
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep

    for i_test in [0, 1]:
        with tqdm(total=3, desc='test') as t:
            # test iterable
            for i in t:
                sleep(0.1)
                if i >= 1:
                    raise Exception
            # test manual
            for i in range(2):
                sleep(0.1)
                t.update(1)
                if i >= 1:
                    raise Exception


# Generated at 2022-06-14 14:01:15.623161
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test for tqdm_notebook.status_printer().
    """
    bar = tqdm_notebook.status_printer(file=None, total=100, desc='test')
    display(bar)
    # Clear previous output (really necessary?)
    # clear_output(wait=1)
    ltext, pbar, rtext = bar.children
    assert pbar.max == 100
    assert ltext.value == 'test'
    assert rtext.value == ''
    bar.close()
    return bar


if __name__ == "__main__":  # pragma: no cover
    import doctest
    doctest.testmod(name="test_tqdm_notebook",
                    optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


# Generated at 2022-06-14 14:01:48.204078
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    try:
        # Unclosed non-auto GUI tqdm raises an error when closed
        tqdm_notebook(total=None).close()
    except:  # pylint: disable=bare-except
        pass
    else:
        raise AssertionError('tqdm.notebook.tqdm not raising error on close() '
                             'while having not finished!')

    # Autoclosed tqdm does not raise error on close
    tqdm_notebook(total=None, leave=True).close()

# Generated at 2022-06-14 14:01:51.954097
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    lst = [5] * 10
    with tqdm_notebook(lst) as t:
        for i in t:  # NOQA
            pass
        return t.displayed



# Generated at 2022-06-14 14:01:58.425641
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for tqdm_notebook().reset()
    """
    # Test a new bar with new total
    q = tqdm_notebook(total=7, desc='new bar')
    i = 1
    while i <= 7:
        i += 1
        q.update()
    q.close()
    q.reset(total=10)
    i = 1
    while i <= 10:
        i += 1
        q.update()
    q.close()

    # Test a new bar with same total
    q = tqdm_notebook(total=7, desc='same bar')
    i = 1
    while i <= 7:
        i += 1
        q.update()
    q.close()
    q.reset(total=7)
    i = 1

# Generated at 2022-06-14 14:02:09.091981
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    pbar = tqdm_notebook.status_printer(
        sys.stderr, 5, "Title", ncols=666)
    assert pbar.layout.width == '666px'
    assert pbar.children[2].layout.width == '666px'
    assert pbar.children[0].layout.width == '666px'
    assert pbar.children[-1].layout.width == '666px'
    assert pbar.layout.flex == '2'
    assert pbar.max == 5
    assert pbar.value == 0
    assert pbar.children[0].value == 'Title'
    pbar.bar_style = 'danger'



# Generated at 2022-06-14 14:02:13.219289
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        import mock
    except ImportError:
        import unittest.mock as mock

    with mock.patch('IPython.display.clear_output') as mock_clear_output:
        with tqdm(total=5) as pbar:
            pbar.clear()

        mock_clear_output.assert_called_once_with(wait=True)

# Generated at 2022-06-14 14:02:22.262838
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    import time
    import re
    import warnings
    with warnings.catch_warnings(record=True) as w:
        # make sure deprecation warnings are triggered
        with tqdm_notebook(total=10, disable=False) as t:
            for i in t:
                time.sleep(0.01)
        assert "deprecated" in str(w[0].message)
        assert "dev" in str(w[1].message)

    with tqdm_notebook(total=10, miniters=2, leave=False) as t:
        for i in t:
            assert t.n == i + 1
            time.sleep(0.01)


# Generated at 2022-06-14 14:02:29.407848
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep
    from .utils import FormatCustomText, FormatCustomTime, Iterable, format_sizeof

    for i in tqdm(Iterable(interval=0.001), desc="test_tqdm_notebook_display",
                  unit=FormatCustomText(' mem: ', format_sizeof),
                  unit_scale=1,
                  bar_format=FormatCustomTime('{l_bar} {postfix[0]} {postfix[1][value]:0.1f}s')):
        sleep(0.01)
        if i == 3:
            raise KeyboardInterrupt("ctrl+c!")
        elif i == 4:
            raise ValueError("test error!")

# Generated at 2022-06-14 14:02:39.624111
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test function for tqdm_notebook.status_printer method.
    """
    from .tests._utils import windll  # noqa: F401
    from .std import tqdm as std_tqdm

    ipywidgets_disabled = IProgress is None
    if IPY == 0 and not ipywidgets_disabled:
        raise ImportError("tqdm.notebook.tqdm_notebook.status_printer test"
                          " requires IPython >= 2.0")
    elif ipywidgets_disabled:
        return  # skip tests


# Generated at 2022-06-14 14:02:48.855026
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from ipywidgets.widgets import Button

    pbar = tqdm_notebook(total=10)
    # Test update() with iterable
    for _ in pbar.update([1, 2, 3]):
        pass
    assert pbar.n == 6
    # Test update() with single integer
    for _ in pbar.update(4):
        pass
    assert pbar.n == 10
    pbar.close()

    # Test update() error handling
    pbar = tqdm_notebook(total=10)
    try:
        raise ValueError()
    except ValueError:
        pbar.update()
    assert pbar.container.children[-2].bar_style == 'danger'

    # Test update() with manual KB interrupt handling

# Generated at 2022-06-14 14:02:55.898776
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:
        t0 = tqdm_notebook(total=10)
        for i in t0:
            if i > 3:
                t0.reset(5)
                for j in t0:
                    if j > 1:
                        t0.reset(3)
                        for k in t0:
                            if k > 2:
                                t0.clear()
                                t0.reset()
                                break
    except KeyboardInterrupt:
        t0.close()
        raise

# Generated at 2022-06-14 14:03:45.489119
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep
    for i in tqdm_notebook(range(10)):
        sleep(0.1)

# Generated at 2022-06-14 14:03:51.539082
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Test `tqdm.notebook.tqdm_notebook.status_printer`."""
    from IPython.display import clear_output
    tqdm_notebook.status_printer(
        None, total=1, desc='test', ncols='100px')
    clear_output()

# Alias
test_tqdm_notebook = test_tqdm_notebook_status_printer



# Generated at 2022-06-14 14:03:56.619343
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    class custom_tqdm(tqdm_notebook):
        def clear(self, *_, **__):
            pass

    _tqdm = custom_tqdm(1000)
    _tqdm.reset()
    _tqdm.reset(total=15)
    _tqdm.reset()
    _tqdm.reset(4)
    _tqdm.reset(total=4)
    _tqdm.reset(total=0)
    _tqdm.reset(total=0)
    _tqdm.reset()

# Generated at 2022-06-14 14:04:02.432015
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    import unittest
    tests = unittest.TestSuite()
    tests.addTest(unittest.FunctionTestCase(test_TqdmHBox___repr__))
    return tests

if __name__ == '__main__':
    from unittest import main
    main(defaultTest='test_TqdmHBox___repr__')


# vim: set fileencoding=utf-8 :

# Generated at 2022-06-14 14:04:07.953631
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    assert TqdmHBox.__repr__(None) == "TqdmHBox(children=(), layout=Layout(display='flex', display_in_flexbox=True, flex_box='row', flex_flow='row wrap', flex_grow=0.0, flex_shrink=1.0, height=''))"
    assert TqdmHBox.__repr__(None, True) == "TqdmHBox(children=(), layout=Layout(display='flex', display_in_flexbox=True, flex_box='row', flex_flow='row wrap', flex_grow=0.0, flex_shrink=1.0, height=''))"
    tqdm_hbox = TqdmHBox()
    tqdm_hbox.pbar = std_tqdm()
    tqdm_h

# Generated at 2022-06-14 14:04:16.393384
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    For tqdm_notebook only.
    """
    from contextlib import closing
    from IPython.core import display
    import tempfile

    # TODO: add tests

    # remove progress bar display
    with closing(tempfile.TemporaryFile()) as f:
        display.display_pretty({'application/json': {'test': 1}}, raw=False, fp=f)
        f.seek(0)
        assert all(
            b'progress' not in line for line in f.readlines()), "progress bar shouldn't be displayed!"


if __name__ == '__main__':  # pragma: no cover
    import time
    s = 0

# Generated at 2022-06-14 14:04:18.475710
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    pbar = tqdm_notebook(range(10))
    for i in pbar:
        pass



# Generated at 2022-06-14 14:04:30.315212
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    # test display()
    t = tqdm_notebook(total=0)
    # check bar style
    t.display(bar_style='danger')
    assert t.container.children[-2].bar_style == 'danger'
    # check closing the bar
    t.display(close=True)
    t.display(close=True)
    # check clearing the bar
    t.display(msg='')
    # check setting description
    t.display(desc='test')
    assert t.container.children[-3].value == 'test'
    # check msg='' does not clear description
    t.display(msg='')
    assert t.container.children[-3].value == 'test'
    # check msg='' does not clear bar
    t.display(msg='')
    assert t.container

# Generated at 2022-06-14 14:04:33.235843
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():

    t = tqdm_notebook(total=100, desc='test')
    for i in range(100):
        t.update(i)
    t.close()

# Generated at 2022-06-14 14:04:36.033507
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    """
    Verify that the displaying of bar states (error and success) on close function
    properly.
    """
    tqdm_notebook.close()
    tqdm_notebook.close()

# Generated at 2022-06-14 14:06:13.879129
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from io import StringIO
    from tqdm import __version__ as v
    from sys import getrefcount as gr
    from time import sleep

    # Simulate user code that prints something
    with StringIO() as f:
        for i in tqdm_notebook(iterable=[1, 2, 3],
                               desc='PRINTING', unit='foo', file=f):
            print(i, file=f)
            sleep(0.5)
        f.seek(0)
        s = f.read()
    assert s == '42foo\n1\n2\n3\n'

    # Test basic interface
    with StringIO() as f:
        for i in tqdm_notebook(iterable=[0, 1],
                               desc="TESTINTERFACE", file=f):
            pass
        f

# Generated at 2022-06-14 14:06:24.533055
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep

    with tqdm(total=2) as pbar:
        assert pbar.gui == True
        assert len(pbar.container.children) == 3
        assert pbar.total == 2
        pbar.update()
        sleep(0.01)  # need this otherwise bar is not shown
        pbar.update()
        assert pbar.closed

    assert pbar.container.visible == False

    for _ in tnrange(5, desc='1st loop'):
        for _ in tqdm_notebook(range(100), desc='2nd loop'):
            for _ in trange(20):
                sleep(0.01)
    try:
        for _ in tqdm(range(10), desc='err'):
            1 / 0
    except ZeroDivisionError:
        pass 

# Generated at 2022-06-14 14:06:30.833526
# Unit test for method update of class tqdm_notebook

# Generated at 2022-06-14 14:06:41.029574
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    """
    Unit tests for `tqdm.notebook.tqdm.close()`
    """

    # Import and create tqdm_notebook
    from tqdm.notebook import tqdm
    t = tqdm(total=2)

    # Should pass if bar is displayed
    assert t._repr_pretty_(None, None)
    assert t._repr_json_(None)
    repr(t) == str(t)

    # Update progress bar to be closed
    t.update()

    # Should pass if bar is closed
    assert t._repr_pretty_(None, None) == ""
    assert t._repr_json_(None) == {}
    repr(t) == str(t)

    # Update progress bar to be closed with leave=True
    t.reset(total=2)
    t

# Generated at 2022-06-14 14:06:44.260762
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    test for method update of class tqdm_notebook
    """
    from .tests import test_tqdm_update

    test_tqdm_update(tqdm, 'Notebook')



# Generated at 2022-06-14 14:06:54.077837
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from IPython.html.widgets import IntSlider
    from IPython.display import clear_output
    import time

    def _test():
        for i in tqdm(range(100), desc="dummy"):
            time.sleep(.01)
            if i == 50:
                pbar.bar_style = 'danger'
            elif i == 70:
                pbar.bar_style = 'info'
            if not i % 10:
                pbar.description = "dummy" + str(i / 10)
            pbar.value = i

    pbar = tqdm_notebook(total=100, desc="dummy")
    pbar.display()
    slider = IntSlider(description="delay", min=0, max=10, value=2)


# Generated at 2022-06-14 14:07:05.121716
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for method reset of class tqdm_notebook.

    Run:
    >>> import sys
    >>> from tqdm.notebook import tqdm_notebook
    >>> tqdm_notebook.test_tqdm_notebook_reset()

    Reference output:
    >>> Range(0, 100)
    <
    >>> Range(0, 100)
    |||
    >>> Range(0, 100)
    |
    >>> Range(0, 100)
    <
    >>> Range(0, 100)
    @@
    >>> Range(0, 100)
    <
    """

# Generated at 2022-06-14 14:07:12.513544
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    import time
    from random import random
    from pytest import raises

    with raises(ImportError):
        tqdm_notebook(range(3), file=None)

    with tqdm_notebook(total=5, file=None) as pbar:
        for i in range(5):
            time.sleep(random())
            pbar.update()
    # Test for error
    try:
        for _ in tqdm_notebook(range(3), file=None):
            time.sleep(random())
            raise Exception('error')
    except Exception:
        pass



# Generated at 2022-06-14 14:07:15.935352
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from random import random
    from operator import truediv

    with tqdm(total=100) as pbar:
        for i in pbar:
            pbar.set_postfix(frac=i / pbar.total, refresh=False)
            pbar.update(random() - .1)



# Generated at 2022-06-14 14:07:24.072735
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    assert TqdmHBox().__repr__() == "{desc}{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"
    assert TqdmHBox().__repr__() == "{desc}{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"
    assert TqdmHBox().__repr__() == "{desc}{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"