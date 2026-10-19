

# Generated at 2022-06-14 13:58:17.376171
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # Avoid print
    global tqdm_notebook
    old_disp = tqdm_notebook._instances[0].disp
    tqdm_notebook._instances[0].disp = lambda *_, **__: None

    t = tqdm_notebook(range(5))
    for i in t:
        if i == 2:
            raise RuntimeError()
        assert i == t.n  # check autoincrement
    assert t.n == 5

    # Restore display
    tqdm_notebook._instances[0].disp = old_disp



# Generated at 2022-06-14 13:58:27.126508
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from bs4 import BeautifulSoup as bs
    import os
    import socket
    import subprocess

    # First check: run a jupyter server and check if it's ok
    # This test is for jupyter server. So we will start a server and test it.
    if not os.path.isfile('jupyter_notebook_config.py'):
        print('Generating jupyter_notebook_config.py ...')
        from notebook.auth import passwd
        subprocess.call('jupyter notebook --generate-config', shell=True)
        # Because linux 'nc' doesn't support -z option, we use python socket
        # to find unused port

# Generated at 2022-06-14 13:58:38.513838
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    """Testing tqdm_notebook constructor"""
    # Test 1: disable=None
    with tqdm_notebook(disable=None) as bar:
        bar.update()

    # Test 2: disable=False/'auto'
    with tqdm_notebook(disable=False) as bar:
        bar.update()
    with tqdm_notebook(disable='auto') as bar:
        bar.update()

    # Test 3: disable=True
    with tqdm_notebook(disable=True) as bar:
        bar.update()
        assert bar.disable is True

    # Test 4: disable=True
    with tqdm_notebook(disable=False, leave=True) as bar:
        bar.update(100)
        assert bar.bar_format == '%s %t'

# Generated at 2022-06-14 13:58:43.093764
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    # Avoid display output during testing
    tqdm_notebook.display = lambda *_, **__: None

    t = tqdm_notebook(total=4)
    t.display()  # default
    t.display(msg="test")  # custom msg
    t.display(bar_style='danger')
    t.display(bar_style='success')
    t.display(close=True)


if __name__ == '__main__':
    test_tqdm_notebook_display()

# Generated at 2022-06-14 13:58:45.430968
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    opts = {'miniters': 2, 'desc': 'Foo', 'total': 4}
    t = tqdm_notebook(**opts)
    t.update_to(3)
    t.close()

# Generated at 2022-06-14 13:58:55.705881
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    for leave in [True, False]:
        for total in [None, 0, 1, 2]:
            for n in [None, 0, 1, 2]:
                if total is not None:
                    if n is None:
                        n = total
                else:
                    if n is None:
                        n = 0
                desc = 'LOOP'
                pbar = tqdm_notebook(total=total, leave=leave, desc=desc)
                pbar.reset(total=total)
                pbar.update(n=n)
                for i in range(n + 1, total + 1):
                    pbar.desc = 'LOOP %d' % i
                    pbar.update(n)
                    pbar.reset(total=total)
                if pbar.leave:  # leave is set
                    assert pbar.container.children

# Generated at 2022-06-14 13:59:02.013031
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from types import SimpleNamespace
    from IPython.html.widgets import FloatProgress, HBox, HTML
    out = tqdm_notebook.status_printer(SimpleNamespace(name='stdout'), 5,
                                       'Testing bar', 7)
    assert isinstance(out, HBox)
    assert len(out.children) == 3
    assert isinstance(out.children[0], HTML)
    assert out.children[0].value == 'Testing bar'
    assert isinstance(out.children[1], FloatProgress)
    assert out.children[1].max == 5
    assert out.children[1].min == 0
    assert isinstance(out.children[2], HTML)
    assert out.children[2].value == ''
    assert out.layout.width == '7px'

# Generated at 2022-06-14 13:59:13.275117
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from tqdm import tqdm, trange
    from time import sleep

    try:
        from ipykernel import iostream
    except ImportError:
        iostream = None

    # Removes None from sys.stdout for pytest
    for t in [tqdm, trange]:
        t.write = lambda s, file=None, flush=None: None
    tqdm_notebook.write = lambda s, file=None, flush=None: None

    io = iostream.OutStream(sys_module=iostream._sys)

    test_str = 'Testing display(self.container) of class tqdm_notebook()\n'

    # Capture sys.stdout

# Generated at 2022-06-14 13:59:21.269830
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from unittest import TestCase, main
    from io import StringIO
    import sys
    import traceback
    from time import sleep


# Generated at 2022-06-14 13:59:32.342318
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """Unit test for reset"""
    from .gui import tgrange

    bar1 = tgrange(0, 10, desc="Bar1")
    bar2 = tgrange(0, 10, desc="Bar2")
    bar1.n = 5
    bar1.reset()
    assert bar1.n == 0
    assert bar1.total == 10
    assert bar1.dynamic_ncols == False
    assert bar1.disable == False
    assert bar1.unit_scale == False
    assert bar1.position == 0
    assert bar1.desc == "Bar1"
    assert bar1.file == sys.stdout
    assert bar2.desc == "Bar2"
    assert bar2.file == sys.stdout
    bar1.reset(total=1)
    assert bar1.total == 1

# Generated at 2022-06-14 13:59:58.409513
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    default = tqdm_notebook.status_printer(None, total=10, desc='Test')
    output = default.children[0].value
    expected = r'Test:   0%|          | 0/10 \[elapsed: 00:00 left: ?, ? iters/sec]'
    if output != expected:
        raise ValueError('\nExpected:\n{}\nGot:\n{}\n'.format(expected, output))

    # Test bar style
    bar = tqdm_notebook.status_printer(None, total=0, desc='Test')
    # Test that style is not None (empty string)
    if bar.children[-2].bar_style is None:
        raise ValueError('\nExpected: {bar_style: ""}\nGot: {bar_style: None}\n')
   

# Generated at 2022-06-14 14:00:06.757789
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .gui import tgrange
    tgrange(1)
    tgrange(1, desc="Description")
    tgrange(1, desc="Description 1", leave=True)
    tgrange(1, desc="Description 2", leave=False)
    tgrange(1, desc="Description 2", leave=False, disable=True)
    tgrange(1, desc="", leave=False)
    tgrange(1, desc="", leave=False, disable=True)
    with tqdm_notebook(total=1) as pbar:
        pbar.display(close=True)

# Test that unit_scale is properly passed along (issue #540)

# Generated at 2022-06-14 14:00:14.095274
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:
        IPY
    except NameError:
        return
    pbar = tqdm_notebook(total=100)
    for i in range(20):
        pbar.update()
    pbar.reset(total=10)
    for i in range(5):
        pbar.update()
    pbar.reset(total=20)
    for i in range(10):
        pbar.update()
    pbar.close()

if __name__ == "__main__":  # pragma: no cover
    r"""
    CommandLine:
        python -m tqdm.notebook
        python -m tqdm.notebook --all-tests
    """
    import pytest

# Generated at 2022-06-14 14:00:22.138515
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    # setup
    t = tqdm_notebook(total=10, leave=True, position=0)
    # test-1: close progressbar without error
    t.close()
    # test-2: close progressbar with error
    t.n = 5
    t.close()



# Generated at 2022-06-14 14:00:23.166194
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    pass



# Generated at 2022-06-14 14:00:25.083489
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    for _ in tnrange(5):
        tnrange(5, desc='Will be reset').reset()()

# Generated at 2022-06-14 14:00:33.328141
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from .utils import BetterStringIO
    with BetterStringIO() as f:
        # test with reset
        bar = tqdm_notebook(total=10, file=f)
        for _ in bar:
            pass
        assert f.getvalue() == ''
        bar.close()
        assert f.getvalue() == ''
        # test without reset (with leave)
        f.seek(0)
        bar = tqdm_notebook(total=10, leave=True, file=f)
        for _ in bar:
            pass
        assert f.getvalue() == ''
        bar.close()
        assert f.getvalue() == ''
        # test without reset (without leave)
        f.seek(0)
        bar = tqdm_notebook(total=10, file=f)

# Generated at 2022-06-14 14:00:40.671808
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for method `display` of class `tqdm_notebook`
    """
    from .auto import tqdm
    from .std import time

    # Initialize tqdm
    # IPython in terminal does not run displays
    is_ipynb = IProgress is not None
    if is_ipynb:
        try:
            from IPython import get_ipython
            if not get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
                is_ipynb = False
        except (ImportError, NameError):
            is_ipynb = False

    # verbose print to stderr
    def vprint(*args):
        print(*args, file=sys.stderr)

    # First test without output
    vprint("Test without output:")
    p

# Generated at 2022-06-14 14:00:47.574503
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    with tqdm_notebook(total=2) as t:
        t.reset(total=3)
        assert t.total == 3

        t.reset(total=2)
        assert t.total == 2

        t.reset()
        assert t.total is None

        t.reset(total=0)
        assert t.total == 0

        t.reset(total=1)
        assert t.total == 1

# Generated at 2022-06-14 14:00:52.129760
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():  # pragma: no cover
    """Unit test for method close of class tqdm_notebook."""
    # Initialization and stop of a tqdm_notebook
    with tqdm_notebook(total=1, leave=True) as t:
        t.update()
        # t.close()  # not necessary, but explicit call anyway



# Generated at 2022-06-14 14:01:22.193890
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():  # pragma: no cover
    from time import sleep

    with tqdm(total=10) as pbar:
        for i in range(10):
            sleep(0.1)
            pbar.update()
        assert pbar.n == 10
        assert pbar.total == 10
        assert pbar.container.children[-2].value == 10
        assert pbar.container.children[-2].max == 10



# Generated at 2022-06-14 14:01:25.556336
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm_notebook(['1', '2', '3']) as t:
        for i in t:
            assert i in ('1', '2', '3')
            t.update()

# Generated at 2022-06-14 14:01:36.848472
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    """Unit test for method close of class tqdm_notebook"""
    for leave in [False, True]:
        bar = tqdm_notebook(range(10), leave=leave)
        assert isinstance(bar.container, TqdmHBox)

        for i in bar:
            assert isinstance(bar.container, TqdmHBox)
            if i == 3:
                break
        else:
            assert isinstance(bar.container, TqdmHBox)
        bar.close()

        if not leave:
            try:
                assert bar.container.style.display == 'none'
            except AttributeError:
                assert bar.container.visible is False
        else:
            assert isinstance(bar.container, TqdmHBox)



# Generated at 2022-06-14 14:01:42.555248
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from os import devnull
    with open(devnull, 'wb') as DEVNULL:
        t = tqdm_notebook(total=10, file=DEVNULL)
        # print(t)
        t.display()
        t.display(pos=4)
        t.display(pos=6, close=True)
        t.display(pos=9, close=True)


if __name__ == '__main__':
    test_tqdm_notebook_display()

# Generated at 2022-06-14 14:01:53.574923
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():  # pragma: no cover
    from time import sleep
    from tqdm.auto import trange
    from tqdm.contrib import tenumerate
    from tqdm import TqdmTypeError
    with trange(10) as t:
        t.set_description("Testing reset")
        # try resetting after few iterations
        for (i, _) in tenumerate(range(10)):
            assert t.n == i
            sleep(0.05)
            if i == 3:
                t.reset()
        # try resetting with total=None
        for i in range(5):
            assert t.n == i
            sleep(0.05)
        t.reset(total=None)
        for i in range(5):
            assert t.n == i
            sleep(0.05)
        #

# Generated at 2022-06-14 14:02:06.630339
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from nose.tools import assert_equal
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch  # PY2

    # Test basic construction
    with patch('jupyter_client.manager.BlockingKernelManager',
               side_effect=ImportError):
        # IPython.html.widgets not available
        assert_equal(tqdm_notebook(disable=True).disable, True)
        assert_equal(tqdm_notebook().disable, True)

    with patch('ipykernel.connect.get_connection_file',
               side_effect=ImportError):
        # ipykernel not available
        assert_equal(tqdm_notebook(gui=True).gui, True)

# Generated at 2022-06-14 14:02:08.867694
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from time import sleep
    for _ in tqdm_notebook(range(1)):
        for _ in trange(10):
            sleep(0.1)

# Generated at 2022-06-14 14:02:15.795083
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import tempfile
    from io import StringIO
    bar = tqdm_notebook(total=100)
    bar.update(1)
    bar.reset()
    assert bar.n == 0
    assert bar.last_print_n == 0
    assert bar.total == 100
    bar.reset(total=None)
    assert bar.n == 0
    assert bar.last_print_n == 0
    assert bar.total is None

    bar = tqdm_notebook(total=100)
    bar.update(1)
    bar.reset(total=50)
    assert bar.n == 0
    assert bar.last_print_n == 0
    assert bar.total == 50

    bar = tqdm_notebook(total=100, leave=True)
    bar.update(1)
    bar.reset

# Generated at 2022-06-14 14:02:17.510461
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .tests import tqdm_notebook_display_test
    tqdm_notebook_display_test()

# Generated at 2022-06-14 14:02:26.573165
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from IPython import get_ipython
    ip = get_ipython()

    tqdm.displayed = False
    # test with total
    total = 9
    pbar = tqdm(total=total)
    tqdm.displayed = True
    assert pbar.n == 0
    assert pbar.container.children[1].value == 0
    # test update + 1
    pbar.update()
    assert pbar.n == 1
    assert pbar.container.children[1].value == 1
    # test update + 2
    pbar.update(2)
    assert pbar.n == 3
    assert pbar.container.children[1].value == 3
    # test update + 3
    pbar.update(3)
    assert pbar.n == 6

# Generated at 2022-06-14 14:03:05.953570
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from .gui import tgrange
    from .utils import mute_stderr, format_sizeof
    mock_kwargs = {
        'desc': 'desc',
        'total': 10,
        'unit_scale': 1,
        'unit': 'foos',
        'leave': True,  # otherwise KeyboardInterrupt won't be properly raised
        'dynamic_ncols': True,
        'ascii': True,
        'position': 0
    }
    with mute_stderr():
        tn = tgrange(10, **mock_kwargs)
    container = tn.status_printer(None, **mock_kwargs)

# Generated at 2022-06-14 14:03:10.921484
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():  # pragma: no cover
    a = 0
    with tqdm_notebook(range(100)) as pbar:
        for i, _ in enumerate(pbar):
            a += i
    assert a == sum(range(100))


# Unit tests for method update of class tqdm_notebook

# Generated at 2022-06-14 14:03:20.216043
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """Unit test for method display of class tqdm_notebook"""
    # Smoke test
    progress_bar = tqdm_notebook()
    progress_bar.display()
    progress_bar.display(close=True)

    # Do not clear the bar in manual mode
    progress_bar = tqdm_notebook(total=0)
    progress_bar.display()
    progress_bar.display(msg='')  # should not clear it
    progress_bar.display(close=True)

    # Test HTML escape
    progress_bar = tqdm_notebook()
    progress_bar.display()
    progress_bar.display(msg='&')
    progress_bar.display(close=True)

# Generated at 2022-06-14 14:03:30.559513
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        import ipywidgets
    except ImportError:
        raise ImportError("ipywidgets not installed!")
    try:
        import IPython
    except ImportError:
        raise ImportError("IPython not installed!")
    from IPython.display import display
    from .utils import format_interval
    from .utils import format_meter

    from time import sleep
    from .std import TestTZ as tz

    with tz("UTC"):
        for i in tqdm_notebook(range(10), miniters=1, mininterval=.01,
                               smoothing=1, ascii=True, desc='test', unit='i',
                               dynamic_ncols=True):
            sleep(.01)

    class ContainerEmpty(Exception):
        pass


# Generated at 2022-06-14 14:03:42.025779
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Unit test for method `__iter__` of class `tqdm_notebook`.
    """
    # no check for disable leaks (tested in tqdm.tests.__init__)

    # Check for iteration
    L = list(tqdm_notebook(range(10)))
    assert L == list(range(10))

    # Check for `close`
    L = tqdm_notebook(range(10))
    next(L)
    L.close()
    assert L.container.visible == False

    # Check for exception in the for loop
    L = tqdm_notebook(range(10))
    next(L)
    try:
        for _ in L:
            raise Exception("test")
    except:  # NOQA
        pass

# Generated at 2022-06-14 14:03:51.978676
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from datetime import datetime
    from time import sleep
    from tqdm import notebook

    sleep_duration = .1

    first_iteration = datetime.now()
    for i in notebook.tqdm(range(4)):
        sleep(sleep_duration)
        # This test is to check that `update()` has automatic
        # calls to `display()`
        if i == 1:
            assert datetime.now() - first_iteration > sleep_duration * 3
            break

    sleep(sleep_duration)
    second_iteration = datetime.now()
    for i in notebook.tqdm(range(4)):
        sleep(sleep_duration)
        if i == 1:
            assert datetime.now() - second_iteration < sleep_duration * 3
            break

# Generated at 2022-06-14 14:04:01.359497
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    from IPython.display import clear_output
    for _ in tqdm_notebook(range(3), desc='1st loop'):
        for _ in tqdm_notebook(range(5), desc='2nd loop'):
            for _ in tqdm_notebook(range(2), desc='3rd loop'):
                sleep(0.01)
        clear_output()
        sleep(0.05)
    clear_output()


if __name__ == '__main__':
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:04:07.443095
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from IPython import get_ipython
    ip = get_ipython()

    # check without error
    with tqdm(total=1, leave=True) as t:
        assert not t.container.visible, "Bar should be closed by default"

    with tqdm(total=1, leave=False) as t:
        pass
    assert not t.container.visible, "Bar should be closed by default"

    # check error with leave=True
    with tqdm(total=1, leave=True) as t:
        raise RuntimeError("Pretend this is an exception")
    assert t.container.visible, "Bar should be visible because of the error"
    assert t.container.children[-2].bar_style == 'danger', (
        "Error bar should be visible because of the error")

    # check error with leave

# Generated at 2022-06-14 14:04:15.372490
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    # enable tests to catch exceptions
    old_catch = tqdm_notebook.catch_warnings
    tqdm_notebook.catch_warnings = True

    with tqdm_notebook(total=1) as t:
        assert t.total == 1
        t.update()
        assert t.total == 1
        assert t.n == 1
        t.reset()
        assert t.total == 1
        assert t.n == 0
        t.reset(total=50)
        assert t.total == 50
        assert t.n == 0
        t.reset(total=100)
        assert t.total == 100
        assert t.n == 0

    tqdm_notebook.catch_warnings = old_catch

# Generated at 2022-06-14 14:04:22.457516
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from subprocess import check_output

    def tqdm_notebook___iter__():
        """
        Lazily test that tqdm_notebook___iter__() raises an RuntimeError
        """
        for i in tqdm_notebook(range(10)):
            if i == 5:
                raise RuntimeError
            yield i

    try:
        res = list(tqdm_notebook___iter__())
    except RuntimeError:
        pass
    # Catch RuntimeError raised in the method __iter__ of class tqdm_notebook
    else:
        raise RuntimeError
    assert res == range(6)
    # Check that the file descriptor is free (no error during print)

# Generated at 2022-06-14 14:05:22.580201
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    try:  # IPython/Jupyter
        import IPython
    except ImportError:
        return
    # hack to test display method of tqdm_notebook
    # even if it is not in the main __init__
    import tqdm.gui._tqdm_notebook
    tqdm.gui._tqdm_notebook._tqdm_notebook._repr_pretty_ =\
        tqdm.gui._tqdm_notebook._tqdm_notebook.__repr__
    tqdm.gui._tqdm_notebook._tqdm_notebook.__repr__ =\
        tqdm.gui._tqdm_notebook._tqdm_notebook._repr_pretty_
    # hack to not print display in stdout
    orig_display = IPython

# Generated at 2022-06-14 14:05:26.098941
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    pbar = tqdm_notebook.status_printer(file=None)
    assert '<bar/>' in repr(pbar)


if __name__ == "__main__":  # pragma: no cover
    from doctest import testmod
    testmod(verbose=True)

# Generated at 2022-06-14 14:05:27.227894
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with trange(1) as t:
        for i in t:
            assert (i == 0)



# Generated at 2022-06-14 14:05:31.131762
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    from nose import SkipTest
    raise SkipTest  # TODO: test plot color
    pbar = IProgress(min=0, max=1)
    container = TqdmHBox(children=[HTML(), pbar, HTML()])
    container.pbar = proxy(pbar)
    pbar.gui.total = 1
    pbar.gui.n = 1
    pbar.gui.dynamic_min = False
    pbar.gui.bar_format = '{bar}'
    return pbar, container


if __name__ == '__main__':
    test_TqdmHBox___repr__()

# Generated at 2022-06-14 14:05:38.686092
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    t = tqdm_notebook([1, 2])
    t.update(1)


# Use tqdm_notebook if in a notebook, otherwise use tqdm
if IPY > 0:
    try:
        from IPython import get_ipython
        if get_ipython() is not None:
            tqdm = tqdm_notebook
            trange = tnrange
            tqdm_notebook.__module__ = "tqdm"
    except ImportError:
        pass

# Generated at 2022-06-14 14:05:45.940453
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from IPython import get_ipython
    from IPython.display import HTML, clear_output
    from math import isnan, isinf
    ip = get_ipython()
    for leave in [True, False]:
        for total in [None, 1, 10]:
            f = tqdm_notebook(total=total, leave=leave)
            try:
                if total is None:  # undefined total
                    assert isinf(f.container.children[-2].max)
                else:
                    assert f.container.children[-2].max == total
            except:
                pass
            if leave:
                f.update(1)
            f.reset(total=1)
            if leave:
                assert not f.container.children[-2].visible
            else:
                assert clear_output.called
            clear_output

# Generated at 2022-06-14 14:05:55.010034
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    """
    Test method close of class tqdm_notebook
    """
    with tqdm_notebook(total=10) as nb:
        assert nb.container.children[-2].bar_style == ''  # no error
        nb.n = 9
        nb.close()
        assert nb.container.children[-2].bar_style == 'success'  # no error
        nb.reset()
        nb.n = 3
        nb.close()
        assert nb.container.children[-2].bar_style == 'danger'  # error


# Simple test
if __name__ == '__main__':
    test_tqdm_notebook_close()

# Generated at 2022-06-14 14:06:04.681324
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    from os import environ, pathsep
    from sys import executable
    from tempfile import NamedTemporaryFile
    if not environ.get("TEST_TQDM_NB"):
        raise unittest.SkipTest("$TEST_TQDM_NB is not set.")

    def get_output(sl):
        """Run `sl` in a subprocess and capture the output"""
        with NamedTemporaryFile(mode='w+t') as f:
            p = subprocess.Popen(
                [executable, '-u'] + ['-c', sl],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                cwd=sys.argv[-1])
            for line in iter(p.stdout.readline, b''):
                f

# Generated at 2022-06-14 14:06:07.177491
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep
    for i in tqdm_notebook(range(15)):
        sleep(0.1)

# Generated at 2022-06-14 14:06:10.230851
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from random import randint
    from time import sleep

    number_of_tries = randint(5, 10)
    sleep_time = randint(2, 5)
    for i in trange(number_of_tries):
        sleep(sleep_time)

# Generated at 2022-06-14 14:07:54.465720
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    for total, n in ((100, 50), (100, 0), (100, 100)):
        tqdm_notebook(total=total, mininterval=0).update(n).reset()


# Generated at 2022-06-14 14:08:01.842711
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import time
    pbar = tqdm_notebook.status_printer(None, 10, 'desc')
    pbar.children[1].value = 1
    pbar.children[1].bar_style = 'info'
    pbar.children[1].description = 'description'
    pbar.children[0].value = 'description'
    pbar.children[2].value = 'desc'
    assert pbar.layout.width == '20px'
    assert str(pbar).find('desc') == 0
    assert str(pbar).find('desc') == len(str(pbar)) - len('desc')
    assert pbar._repr_json_()['bar_format'] == '{l_bar}<bar />{r_bar}'
    assert pbar._repr_pretty_() is None

   