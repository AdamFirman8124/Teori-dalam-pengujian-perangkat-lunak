

# Generated at 2022-06-14 13:58:51.088918
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from IPython.display import clear_output
    from time import sleep

    with tqdm_notebook(
            total=10, desc="Testing", leave=True,
            ncols=100) as pbar:
        for i in range(10):
            pbar.update(1)
            sleep(0.1)
        pbar.set_description("New desc")
        pbar.close()
        try:
            pbar.reset()
        except AttributeError:
            clear_output()



# Generated at 2022-06-14 13:58:58.726820
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:
        from ipykernel.kernelapp import IPKernelApp
        IPKernelApp.launch_instance(argv=[''])
    except ImportError:  # pragma: no cover
        pass
    except Exception:  # pragma: no cover
        print("Fail to test tqdm_notebook reset method in IPython Notebook")
    else:  # pragma: no cover
        from IPython.core.display import display

        from tqdm import tqdm_notebook as tqdm

        display('before loop')
        for i in tqdm(range(4)):
            pass
        display('after loop')
        for i in tqdm(range(4)):
            pass
        display('after reset')

# Generated at 2022-06-14 13:59:02.151991
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from tqdm.auto import trange
    for leave in (True, False):
        for total in (2, 3):
            for i in trange(total, leave=leave):
                pass

# Generated at 2022-06-14 13:59:13.396927
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from random import randrange
    # noinspection PyUnresolvedReferences
    list(tqdm_notebook(range(3)))
    list(tqdm_notebook(range(3), desc='desc'))
    list(tqdm_notebook(range(3), desc='desc', leave=False))
    list(tqdm_notebook(range(3), desc='desc', leave=True))
    list(tqdm_notebook(range(3), desc='desc', leave=True, disable=True))
    list(tqdm_notebook(range(3), desc='desc', unit_scale=True))
    list(tqdm_notebook(range(3), desc='desc', unit_scale=False))

# Generated at 2022-06-14 13:59:20.579129
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    The following will show a progress bar in IPython/Jupyter Notebook.
    """
    import time
    from tqdm.notebook import tqdm_notebook
    pbar = tqdm_notebook.status_printer(
        file=sys.stdout,
        total=100,
        bar_format='{l_bar}{bar}| [{elapsed}<{remaining}{postfix}]')

    for i in range(100):
        pbar.value = i
        time.sleep(0.02)

# Test
if __name__ == '__main__':  # pragma: no cover
    test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 13:59:32.297309
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    import time
    from tqdm import trange
    # First test without `display` in the loop
    with trange(10) as pbar:
        for c in pbar:
            time.sleep(0.1)
    assert pbar.n == pbar.total == 10
    # Test again with `display` in the loop
    with trange(10) as pbar:
        for c in pbar:
            time.sleep(0.1)
            pbar.display()
    assert pbar.n == pbar.total == 10
    # Test without `display` in the loop, but with `leave=True`
    with trange(10, leave=True) as pbar:
        for c in pbar:
            time.sleep(0.1)
    assert pbar.n == pbar.total == 10


# Generated at 2022-06-14 13:59:39.407532
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .utils import _term_move_up
    from IPython.display import display, HTML, clear_output

    fp = StringIO()

    try:  # IPython 6+
        get_ipython_info = get_ipython().version_info
    except NameError:
        get_ipython_info = (0, 0, 0)

    # Test with string
    t = tqdm_notebook(total=4, file=fp, leave=False)
    t.display(msg='hi')
    t.display(msg='')
    t.display(msg='hi', pos=0)
    t.display(msg='hi2', pos=1)
    t.display(msg='hi3', pos=0)
    t.display(msg='hi4', pos=1)

# Generated at 2022-06-14 13:59:42.552139
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=1) as pbar:
        pbar.clear()
        if pbar.disable:
            return
        assert not pbar.container.visible

# Generated at 2022-06-14 13:59:47.757863
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """ See https://github.com/tqdm/tqdm/issues/872 """
    for cls in [tqdm_notebook, tqdm, trange]:
        assert type(cls(disable=True).update(0)) is None
        assert type(cls().update(0)) is None

# Generated at 2022-06-14 13:59:56.301165
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from unittest import TestCase, main

    class TqdmTest(TestCase):
        def test_tqdm_notebook_status_printer(self):
            from .std import tqdm_notebook
            pbar = tqdm_notebook.status_printer(
                None, total=42, desc="baz", ncols=100)
            self.assertIsInstance(pbar, TqdmHBox)
            self.assertIsInstance(pbar.children[0], HTML)
            self.assertIsInstance(pbar.children[1], IProgress)
            self.assertIsInstance(pbar.children[2], HTML)
            self.assertEqual(pbar.children[0].value, "baz")
            self.assertEqual(pbar.children[2].value, "")

           

# Generated at 2022-06-14 14:00:14.733528
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():  # pragma: no cover
    from time import sleep
    for i in tqdm_notebook(iterable=range(4), desc='1st loop'):
        for j in tqdm_notebook(iterable=range(5), desc='2nd loop', leave=False):
            for k in tqdm_notebook(iterable=range(50), desc='3nd loop'):
                sleep(0.01)

# Generated at 2022-06-14 14:00:17.616737
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from random import uniform
    from time import sleep

    with tqdm_notebook(total=100) as pbar:
        for i in range(100):
            sleep(uniform(0.001, 0.2))
            pbar.update()

# Generated at 2022-06-14 14:00:23.915670
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from collections import Iterable
    for n in tqdm_notebook(range(2), leave=False):
        assert isinstance(n, int)
        for n in tqdm_notebook(range(5)):
            assert isinstance(n, int)
        with tqdm_notebook(range(2), leave=False) as t:
            for n in t:
                assert isinstance(n, int)
                assert isinstance(t, Iterable)
    total = 10
    with tqdm_notebook(total=total) as t:
        for n in range(total):
            t.set_description(" Testing")
            t.update()
    return


# Generated at 2022-06-14 14:00:27.442361
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm_notebook(total=5) as pbar:
        for i in pbar:
            assert pbar.n == i + 1
        # check if bar is closed properly
        assert pbar.n == pbar.total == 5



# Generated at 2022-06-14 14:00:34.768355
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Basic tests of tqdm_notebook initialization, update and output """
    from io import StringIO
    from sys import stdout
    from time import sleep
    from time import time as time_time

    out = StringIO()
    with tqdm(total=20, file=out) as pbar:
        for _ in range(20):
            # call display() manually
            pbar.display()
            sleep(.1)

    # Test auto-display
    out = StringIO()
    with tqdm(total=20, file=out) as pbar:
        for _ in range(20):
            sleep(.1)

    # Test initial bar_format
    out = StringIO()

# Generated at 2022-06-14 14:00:41.585410
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():  # pragma: no cover
    with tqdm_notebook(total=5, unit='B', unit_scale=True) as t:
        t.update(2)
        assert t.n == 2
        t.update(1)
        assert t.n == 3
        try:
            t.update(10)
        except ValueError as e:
            assert str(e.args[0]) == 'n ({}) cannot exceed total ({})'.format(
                10, t.total)
        # testing reset
        t.reset(total=10)
        assert t.total == 10
        try:
            t.update(10, 1)
        except TypeError as e:
            assert str(e.args[0]) == 'update() takes from 1 to 2 positional arguments but 3 were given'
        assert t.n == 10

# Generated at 2022-06-14 14:00:50.334417
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    tqdm.notebook.status_printer(None, total=10, desc='Testing tqdm',
                                 ncols=100)
    tqdm.notebook.status_printer(None, total=10, desc='Testing tqdm',
                                 ncols=100)


if __name__ == "__main__":
    from .main import _test_tqdm_notebook  # noqa: F401

    test_tqdm_notebook_status_printer()
    _test_tqdm_notebook()

# Generated at 2022-06-14 14:00:59.148869
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    try:
        from IPython.display import clear_output
    except ImportError:
        clear_output = lambda *a, **kw: None
    from IPython import get_ipython

    ipython = get_ipython()
    if ipython is None:
        return  # this test is not ran in test_notebook

    hbox1 = TqdmHBox()
    hbox2 = TqdmHBox()
    hbox_no_pbar = TqdmHBox()

    ipython.display_formatter.formatters['text/plain'].for_type_by_name(
        'tqdm', 'TqdmHBox', hbox1.__repr__)

# Generated at 2022-06-14 14:01:05.638405
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    """
    Tests the constructor of class tqdm_notebook.
    """
    if IPY:
        # test the contructor of class tqdm_notebook
        n = 9
        it = tqdm_notebook(iterable=range(n), total=n, disable=False)
        assert it.disable is False
        it = tqdm_notebook(iterable=range(n), total=n, disable=True)
        assert it.disable

        # test the contructor of class tnrange
        n = 9
        it = tnrange(n, disable=False)
        assert it.disable is False
        it = tnrange(n, disable=True)
        assert it.disable

        # test the contructor of class tqdm
        n = 9

# Generated at 2022-06-14 14:01:17.362009
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import sys
    from io import StringIO

    # Redirect stdout to StringIO
    _stdout = sys.stdout
    sys.stdout = StringIO()

    # Run test case
    t = tqdm_notebook(total=9, desc='1st loop')
    for i in range(10):
        t.update()
    t.reset()
    for i in range(9):
        t.update()
    t.close()

    # Read stdout
    value = sys.stdout.getvalue()
    sys.stdout.close()

    # Restore stdout
    sys.stdout = _stdout

    # Check that the output is as expected
    ncols = 100  # hard-coded

# Generated at 2022-06-14 14:01:51.679156
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    """Unit test for method __repr__ of class TqdmHBox"""
    from test._test_tqdm import _test_tqdm
    from sys import stdout
    with _test_tqdm(stdout) as t:
        for _ in t:
            assert repr(t.container)
            # maybe not called by IPython
            if hasattr(t.container, '_repr_pretty_'):
                t.container._repr_pretty_(None)
        t.close()
    # warning: not testing representation in case of manual bar (ncols=float('inf'))



# Generated at 2022-06-14 14:01:55.910009
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from tqdm.tests import TestCase
    # instantiate class for testing
    t = TestCase().assertRaises(AssertionError, tqdm_notebook, total=10)
    # test method close
    t.close()


if __name__ == "__main__":
    from tqdm.tests import _test_tqdm_notebook_main_loop
    _test_tqdm_notebook_main_loop()

# Generated at 2022-06-14 14:01:57.573393
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    tqdm_notebook.status_printer(None)

# Generated at 2022-06-14 14:02:09.837075
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from contextlib import closing
    from time import sleep

    with closing(tqdm_notebook(
            total=2, unit='it',
            unit_scale=False, mininterval=0, miniters=1,
            leave=True, desc='test')) as pbar:
        # test simple usage of tqdm_notebook
        for i in _range(2):
            sleep(.2)
            pbar.update()

    with closing(tqdm_notebook(
            total=2, unit='it',
            unit_scale=False, mininterval=0, miniters=1,
            leave=True, desc='test')) as pbar:
        # test context management
        for i in _range(2):
            sleep(.2)
            pbar.update()


# Generated at 2022-06-14 14:02:18.525416
# Unit test for method update of class tqdm_notebook

# Generated at 2022-06-14 14:02:27.449781
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    from os import remove
    from io import StringIO
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile(mode='w', delete=False) as f:
        # Don't print to stdout
        old_fds = sys.stdout, sys.stderr
        new_fds = StringIO(), StringIO()
        sys.stdout, sys.stderr = new_fds

# Generated at 2022-06-14 14:02:31.878118
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import time
    pbar = tqdm_notebook(total=5, leave=False)
    for i in range(5):
        time.sleep(0.1)
        pbar.update(1)
        pbar.clear()  # don't clear bar, keep all info
        time.sleep(0.1)
        pbar.update(1)

# Generated at 2022-06-14 14:02:38.963202
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Test for tqdm_notebook status_printer"""
    w = TqdmHBox(children=[HTML(), IProgress(min=0, max=10), HTML()])
    w.children[1].bar_style = 'success'
    pbar = w.children[1]
    try:
        assert str(w) == '100%|██████████| 10/10 [00:00<00:00, ?it/s]'
    except:
        print('WARNING: test_tqdm_notebook_status_printer test has failed')
        raise

# Generated at 2022-06-14 14:02:48.567247
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():  # pragma: no cover
    class fp:
        def write(self, x):
            pass
    container = tqdm_notebook.status_printer(fp())
    assert container.children[0].value == ''
    assert container.children[1].value == 0
    assert container.children[2].value == ''
    del container.children[-2].style
    assert container.children[2].value == ''
    container.children[0].value = '>'
    assert container.children[0].value == '&gt;'
    container.children[2].value = '<'
    assert container.children[2].value == '&lt;'

if __name__ == '__main__':  # pragma: no cover
    test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 14:02:59.125253
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from unittest import TestCase
    class Testtqdm_notebook_close(TestCase):
        def test_tqdm_notebook_close_success(self):
            """Test if tqdm_notebook.close() hides the progressbar"""
            t = tqdm_notebook(total=2)
            t.update()
            t.close()
            self.assertTrue(getattr(t.container, "visible", True) == False)
            self.assertTrue(getattr(t.container, "layout", True) == False)

        def test_tqdm_notebook_close_error(self):
            """Test if tqdm_notebook.close() hides the progressbar"""
            t = tqdm_notebook(total=2)
            t.update()
            t.total = None
           

# Generated at 2022-06-14 14:03:55.847323
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from io import StringIO
    from contextlib import closing
    with closing(StringIO()) as our_file:
        for _ in tqdm_notebook(range(5), file=our_file):
            pass
        our_file.seek(0)
        assert our_file.read() == '\r | 0/5 [00:00<?, ?it/s]\r\x1b[A | 2/5 [00:00<?, ?it/s]\r\x1b[A\r | 3/5 [00:00<?, ?it/s]\r\x1b[A | 5/5 [00:00<?, ?it/s]\r\x1b[A\r\x1b[A'

# Generated at 2022-06-14 14:04:06.986909
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    for i in tqdm_notebook(range(3)):
        assert i == 0
        break
    t = tqdm_notebook(range(3))
    for i in t:
        if i == 0:
            break
    else:
        t.close()
    t = tqdm_notebook(range(3))
    for i in t:
        if i == 0:
            t.close()
            break
    else:
        t.close()
    t = tqdm_notebook(range(3))
    for i in t:
        if i == 0:
            t.close()
            break
        else:
            t.close()
    t = tqdm_notebook(range(3))

# Generated at 2022-06-14 14:04:12.376600
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    """ Unit test for method close of class tqdm_notebook
    """
    with tqdm_notebook(total=100) as pbar:
        assert pbar.container.visible
        assert pbar.container.layout.visibility == 'visible'
        pbar.close()
        assert not getattr(pbar.container, 'visible', True)
        assert pbar.container.layout.visibility == 'hidden'



# Generated at 2022-06-14 14:04:19.505156
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    import textwrap
    from os import linesep

    def check(d, expected, pretty=None):
        repr(TqdmHBox(pbar=d))
        repr(TqdmHBox(pbar=d))
        repr(TqdmHBox(pbar=d))
        r = TqdmHBox(pbar=d).__repr__(pretty)
        assert r == textwrap.dedent(expected.rstrip('\r\n')).format(
            linesep=linesep)

    # Different formats
    d = std_tqdm({'n': 1, 'total': 10, 'bar_format': "{l_bar}"})
    check(d, '''\
    1/10: |█████████                           | 10.00% used
    ''')
    d = std_tq

# Generated at 2022-06-14 14:04:22.780998
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from random import random
    from time import sleep

    pbar = tqdm_notebook(total=4)
    for i in range(4):
        sleep(random())
        pbar.update()
    pbar.close()


if __name__ == "__main__":
    test_tqdm_notebook()

# Generated at 2022-06-14 14:04:23.931124
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    trange(2).clear()

# Generated at 2022-06-14 14:04:35.491918
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from tqdm.auto import tqdm as tqdm_auto
    with tqdm_auto() as _tqdm_auto:
        for _ in range(10):
            pass
        _tqdm_auto.clear()
    with tqdm_notebook() as _tqdm_notebook:
        for _ in range(10):
            pass
        _tqdm_notebook.clear()
        # assert _tqdm_notebook.n == 2  # impossible to check...
    # Test with dynamic ncols
    with tqdm_notebook(ascii=True, dynamic_ncols=True, leave=True) as _tqdm_notebook:
        for _ in range(10):
            pass
        _tqdm_notebook.clear()
        # assert _tqdm

# Generated at 2022-06-14 14:04:41.840719
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    for attr in ['total', 'leave', 'ncols', 'desc']:
        desc = '#' if attr == 'desc' else attr
        for v in [getattr(tnrange(int(10)), attr), getattr(tnrange(10, desc=desc), attr)]:
            try:
                desc = str(v)
            except Exception:
                desc = 'unknown'
            with tnrange(5) as t:
                assert getattr(t, attr) == v, ('getattr(t, attr) == v failed with %s'
                                               % desc)
                t.reset()
                assert getattr(t, attr) == v, ('t.reset() failed with %s'
                                               % desc)
                t.reset(total=100)

# Generated at 2022-06-14 14:04:46.734722
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=3) as pbar:
        pbar.update(1)
        pbar.update(2)
        pbar.clear(total=5)
        pbar.update(1)
        pbar.update(2)
        assert pbar.n == 5

# Generated at 2022-06-14 14:04:52.774138
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import unittest
    class TestPbar(unittest.TestCase):
        def test_clear(self):
            from tqdm.auto import tnrange, close
            pbar = tnrange(0, 5)
            self.assertEqual(str(pbar), '')
            for i in pbar:
                self.assertEqual(str(pbar), '')
            close(pbar)
    unittest.main(argv=[''], verbosity=2, exit=False)