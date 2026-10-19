

# Generated at 2022-06-14 13:58:27.773106
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """Test the __iter__ method of tqdm_notebook class."""
    with tqdm_notebook(total=1) as pbar:
        pass



# Generated at 2022-06-14 13:58:37.021686
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep
    # Tests
    with tqdm(total=3) as t:  # Initialise
        assert t.pos == 0  # Setup initial position
        # task 1
        assert t.pos == 0
        t.update()
        assert t.pos == 1
        # task 2
        for _ in t:
            sleep(0.2)
        # task 3
        t.update()
        assert t.pos == 3
        t.close()  # Close
        assert t.pos == 4

if __name__ == '__main__':
    test_tqdm_notebook()

# Generated at 2022-06-14 13:58:46.472786
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from IPython.core.display import clear_output

# Generated at 2022-06-14 13:58:55.707376
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """Unit test for method __iter__ of class tqdm_notebook"""
    if not IPY:
        raise unittest.SkipTest("IPython not installed.")
    # Initialise list
    a = list(range(100))
    # Build iterable
    b = tqdm_notebook(a)
    # Check that iterating through iterable is equivalent to iterating through list
    for i, _ in enumerate(b):
        # Check index
        assert(i == a[i])
    # Check that length of iterable is equivalent to length of list
    assert(len(b) == len(a))
    # Check that iterable is a list
    assert(isinstance(b, list))



# Generated at 2022-06-14 13:59:07.035301
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from random import randint
    with tqdm_notebook(total=10) as progressbar:
        for _ in progressbar:
            progressbar.n += randint(-1, 1)
    assert progressbar.n == 10
    progressbar.reset()
    with tqdm_notebook(total=10) as progressbar:
        for _ in progressbar:
            progressbar.n += randint(-1, 1)
            if progressbar.n >= 10:
                break
    assert progressbar.bar_style == 'danger'
    progressbar.reset()
    with tqdm_notebook(total=10) as progressbar:
        for _ in progressbar:
            progressbar.n += randint(-1, 1)
            if progressbar.n == 0:
                raise IndexError
    assert progressbar.bar_style

# Generated at 2022-06-14 13:59:14.261101
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    """Test tqdm_notebook and all its aliases"""

    # Python 2.6-2.7
    try:
        from nose.tools import assert_equal
    except ImportError:
        from nose.tools import assert_equals as assert_equal

    # Return False if not in notebook
    if IProgress is None:
        assert_equal(tqdm_notebook.gui, False)
        assert_equal(tqdm_notebook.gui, tqdm.gui)
        assert_equal(tqdm_notebook.gui, tnrange.gui)
        assert_equal(tqdm_notebook.gui, trange.gui)
        return False

    # Tests
    with tqdm(total=100) as pbar:
        assert_equal(pbar, tqdm.pbar)
        assert_

# Generated at 2022-06-14 13:59:20.000612
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    if IPY == 0:
        return

    f = tqdm_notebook.status_printer
    for total in [0, 42]:
        for desc in [
            None, 'desc',  # int/str should be supported
            'multi\nline\n\n',  # should handle newlines
            '<special>',  # should be escaped
            HTML('HTML'),  # should not be escaped
        ]:
            for ncols in [None, 42, '100%']:
                container = f(None, total, desc, ncols)
                if IPY == 2:
                    container.on_displayed(None)  # show widget
                display(container)
                # TODO: add tests to check total/desc/ncols


test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 13:59:24.074594
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    This test is a simple demo of the IPython/Jupyter Notebook tqdm widget.
    """
    # Init tqdm and display
    with tqdm_notebook(total=100) as pbar:
        pbar.update(10)  # no display
        pbar.display(80)  # display immediately
        pbar.n = 50
        pbar.display()  # display automatically
        pbar.close()  # display close
    print("exiting test_tqdm_notebook_display")

# Generated at 2022-06-14 13:59:34.637037
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from .tests import tests_aux
    # test_tqdm_notebook_reset
    from tqdm import tqdm_notebook
    for total in [None, 100]:
        for n in [None, 5]:
            for ncols in [None, 0, 100]:
                for leave in [False, True]:
                    # create progress bar
                    t = tqdm_notebook(total=total, unit='B',
                                      unit_scale=True, leave=leave,
                                      ncols=ncols)
                    # fill progress bar
                    if n:
                        for _ in range(n):
                            t.update()
                    # reset progress bar
                    t.reset(total=total)
                    # fill progress bar again
                    if n:
                        for _ in range(n):
                            t.update()


# Generated at 2022-06-14 13:59:47.184165
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from random import random
    from time import sleep

    with tqdm_notebook(range(10)) as t:
        for i in t:  # iterate through tqdm bar
            sleep(random()/10)

    # equivalent to:
    t = tqdm_notebook(range(10))
    for i in t:  # iterate through tqdm bar
        sleep(random()/10)
    t.close()

    # equivalent to:
    t = tqdm_notebook(range(10))
    for i in t:  # iterate through tqdm bar
        sleep(random()/10)
    t.reset(total=0)  # close bar

    # equivalent to:
    t = tqdm_notebook(range(10))

# Generated at 2022-06-14 14:00:11.829412
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from tqdm import tqdm_notebook
    fp = None

# Generated at 2022-06-14 14:00:14.366465
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Test method ``__iter__`` with empty iterable.
    """
    with tqdm(total=0) as t:
        assert not list(t)



# Generated at 2022-06-14 14:00:22.290285
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():  # pragma: no cover
    # Initialize tqdm_notebook
    t = tqdm_notebook(total=10)
    # Run tqdm_notebook
    for i in t:
        # Check status bar width
        assert t.ncols == '100%'
        assert str(t).count('%') == 1
        # Run tqdm_notebook
        # Check status bar width
        if i == 3:
            t.ncols = 200
            assert t.ncols == 200
        # Check bar style
        if i == 6:
            t.bar_style = 'success'
            assert t.bar_style == 'success'
    t.close()
    # Check bar style
    assert t.bar_style == 'success'
    # Clear output
    clear_output()


#

# Generated at 2022-06-14 14:00:23.609387
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    t = tqdm_notebook(range(10))
    for i in t:
        pass
    try:
        for i in t:
            raise Exception
    except Exception:
        pass


# Generated at 2022-06-14 14:00:32.406130
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    pbar = tqdm_notebook(total=100)
    assert pbar.__repr__() == '  0%|                                 | 0/100 [00:01<?, ?it/s]'

# Generated at 2022-06-14 14:00:40.106169
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():

    # Import all necessary packages
    import os
    import sys

    # Get path to main directory
    current_path = os.path.abspath('')
    father_directory = os.path.abspath(
        os.path.join(current_path, os.pardir))  # Get father directory
    father_father_directory = os.path.abspath(os.path.join(
        father_directory, os.pardir))  # Get father of father directory
    main_directory = os.path.abspath(os.path.join(
        father_father_directory, os.pardir))  # Get main directory

    # Add paths to python path
    sys.path.append(father_directory)
    sys.path.append(main_directory)

    # Import necessary modules

# Generated at 2022-06-14 14:00:51.782927
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Simple unit test for method reset of class tqdm_notebook.

    Tests the following features:
     - new bar is created with correct value and style
     - bar does not change if n < total
     - bar is green if n == total and leave=True
     - bar is hidden if n == total and leave=False
     - bar is red if n > total
     - bar is red if exception is raised
     - bar is red if KeyboardInterrupt is raised

    Returns
    -------
    bool
        Success or failure of the test
    """
    from .std import tqdm
    from .utils import IS_PYPY
    from time import sleep

    ERRORS = []
    TRUE_OR_NONE = lambda x: x is None or x is True
    # Verify method reset with NO total value set

# Generated at 2022-06-14 14:00:55.968372
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from .utils import TestCase
    from .std import TestWidget, TestTqdmDynamic

    class TestTqdmDynamicTn(TestTqdmDynamic, TestCase):
        tqdm = tqdm_notebook
        widget = TestWidget(unit='iB')
        is_notebook = True

    TestTqdmDynamicTn().test_reset()

# Generated at 2022-06-14 14:01:03.693388
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from sys import version_info
    from io import StringIO
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        import nbformat as nbf
        nb = nbf.v4.new_notebook()
        nb.worksheets.append(nbf.v4.new_worksheet())
        test_nb = str(tmpdir) + 'test_nbconvert.ipynb'
        nbf.write(nb, test_nb)
        try:
            from nbconvert import PythonExporter
            from nbconvert.preprocessors import ExecutePreprocessor
            pe = PythonExporter()
            body, _ = pe.from_filename(test_nb)
        except ImportError:
            return None


# Generated at 2022-06-14 14:01:15.666055
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    Unit test for method update of class tqdm_notebook.
    If main, uses `tqdm.tests` to test the method.
    """
    import signal

    bar_style = None

# Generated at 2022-06-14 14:01:29.632790
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    """Test if a cleared notebook is not showing anything"""
    with tqdm(total=1) as bar:
        bar.clear()
    bar.clear()

# Generated at 2022-06-14 14:01:33.931871
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    for i in tqdm_notebook([[1, None], [2, 3]]):
        sleep(0.1)

if __name__ == '__main__':  # pragma: no cover
    test_tqdm_notebook___iter__()

# Generated at 2022-06-14 14:01:38.314423
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    # basic tests
    with tnrange(2) as t:
        t.update()
    with tnrange(1) as t:
        pass
    with tnrange(1) as t:
        t.update(0)
    with tnrange(1, leave=True) as t:
        pass
    with tnrange(2, leave=True) as t:
        t.update()
    with tnrange(2, leave=True) as t:
        t.update(0)
    with tnrange(2) as t:
        raise Exception()
    # with tnrange(2) as t:
    #     raise RuntimeError()
    with tnrange(2, leave=True) as t:
        raise Exception()
    # with tnrange(2, leave=True) as t:


# Generated at 2022-06-14 14:01:45.843299
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    TqdmHBox._repr_json_ = lambda s, **k: {}
    pbar = tqdm_notebook.status_printer(sys.stderr, total=0)
    pbar_repr = repr(pbar)

    # Default output
    assert 'Progress:' in pbar_repr
    assert 'Unknown' in pbar_repr
    assert '0.00' in pbar_repr
    assert 'ETA:' in pbar_repr

    # Specify description
    pbar = tqdm_notebook.status_printer(sys.stderr, total=0, desc='test')
    assert 'test' in repr(pbar)

    # Specify integer amount of columns

# Generated at 2022-06-14 14:01:55.465523
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    tqdm_widget = tqdm_notebook.status_printer(sys.stderr, 10, desc='test_tqdm_notebook_status_printer')
    tqdm_widget.layout.width = '350px'
    assert repr(tqdm_widget).startswith('test_tqdm_notebook_status_printer:  ')
    # Check the bar is in the GUI
    assert '<tqdm_notebook_status_printer.bar>' in repr(tqdm_widget)
    assert '\r' not in repr(tqdm_widget)
    tqdm_widget.update(1)
    assert '\r' not in repr(tqdm_widget)
    assert '>' in repr(tqdm_widget)

# Generated at 2022-06-14 14:02:00.120197
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from time import sleep

    with tqdm(total=10) as pbar:
        for i in range(20):
            sleep(0.05)
            pbar.update(1)
            pbar.clear()
    print("Done", flush=True)

# Generated at 2022-06-14 14:02:11.394291
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep
    for i in tqdm_notebook(range(10), Leave=True):
        sleep(0.01)
    for i in tqdm_notebook(range(10), Leave=False):
        sleep(0.01)
    for i in tqdm_notebook(range(10), Leave=True, disable=False):
        sleep(0.01)
    for i in tqdm_notebook(range(10), Leave=False, disable=False):
        sleep(0.01)
    for i in tqdm_notebook(range(10), Leave=True, disable=True):
        sleep(0.01)
    for i in tqdm_notebook(range(10), Leave=False, disable=True):
        sleep(0.01)



# Generated at 2022-06-14 14:02:16.524233
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    """Test case"""
    # Test 1: no iteration
    with tqdm_notebook(total=0) as pbar:
        pass
    assert pbar.displayed is False
    # Test 2: standard iteration
    with tqdm_notebook(total=3) as pbar:
        pbar.update()
        assert pbar.displayed is False
        pbar.update()
        assert pbar.displayed is False
        pbar.update()
        assert pbar.displayed is True
        assert pbar.n == pbar.last_print_n == 3


# Generated at 2022-06-14 14:02:25.619933
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        # create a minimal tqdm_notebook
        t = tqdm_notebook(range(5), display_id=False)
        assert t.disable == False
        assert t.displayed == False
        # raise TypeError if display_id is False
        t.display()
        assert t.displayed == True
        # remove the progress bar from the display
        t.clear()
        assert t.disable == True
        assert t.displayed == False
    except:
        raise


if __name__ == "__main__":
    from ._tqdm_test_examples import \
        iteration_wrapper  # NOQA, pylint: disable=unused-variable

# Generated at 2022-06-14 14:02:27.150820
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    rng = tnrange(10)
    for i in rng:
        rng.update()



# Generated at 2022-06-14 14:03:00.529214
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    import time
    import numpy.testing as nt
    from IPython.display import clear_output
    with tqdm_notebook(total=3, leave=False) as t:
        for i in t:
            time.sleep(0.1)
            if i == 1:
                t.set_description(u'бабах')
            t.update()
    with tqdm_notebook(total=3, leave=False) as t:
        for i in t:
            time.sleep(0.1)
            try:
                raise Exception
            except:
                t.close()
    with tqdm_notebook(total=3, leave=False) as t:
        for i in t:
            time.sleep(0.1)

# Generated at 2022-06-14 14:03:08.496821
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # Unit test to check whether the update method of tqdm_notebook
    # behaves correctly.
    def f(tq):
        # This function has the same behaviour as the update method of
        # class tqdm_notebook, except that it does not display anything
        # and it returns a tuple (n, n_interval)
        n = tq.n
        delta_it = tq.n - tq.last_print_n
        if delta_it >= tq.miniters:
            tq.nintervals += delta_it // tq.miniters
            tq.miniters = 1
        return (n, tq.nintervals)

    with tqdm_notebook(total=3, leave=True) as t:
        # first iteration
        t.update()

# Generated at 2022-06-14 14:03:19.438289
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    try:
        from IPython.display import clear_output
    except ImportError:
        return  # skipping tests

    if IProgress is None:  # #187 #451 #558 #872
        return

    for ncols in [{}, {'ncols': None}, {'ncols': 100},
                  {'ncols': "100%"}, {'ncols': "100px"}]:
        with tqdm_notebook(total=2, **ncols) as t:
            t.update(1)
        clear_output()

    # Test bar style changing
    with tqdm_notebook(total=1) as t:
        assert t.bar_style == ''
        t.bar_style = 'info'
        assert t.bar_style == 'info'
    clear_output()

   

# Generated at 2022-06-14 14:03:29.997937
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # This test runs only if IProgress is not None
    if IProgress is not None:
        sp = tqdm_notebook.status_printer
        pbar = sp(None, 123, 'Hello')
        assert isinstance(pbar, TqdmHBox)
        ltext, pbar, rtext = pbar.children
        assert ltext is not None
        assert isinstance(ltext, HTML)
        assert ltext.value == 'Hello'
        assert rtext is not None
        assert isinstance(rtext, HTML)
        assert rtext.value == ''
        assert isinstance(pbar, IProgress)
        assert pbar.max == 123
        assert pbar.value == 0
        assert pbar.bar_style == 'info'
        assert pbar.layout.width == '100%'

# Generated at 2022-06-14 14:03:33.881489
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    for total in [None, 10]:
        t = tnrange(2, 3, total=total)
        for _ in t:
            pass
        assert t.last_print_n == 2

        t.reset(total=total)
        assert t.last_print_n == 0


# Generated at 2022-06-14 14:03:45.165350
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from six import StringIO
    from io import TextIOWrapper

    def unit_test():
        """Test case 1"""
        # Test case 1:
        # check that this case passes 100% with only python2
        with StringIO() as f:
            with tqdm_notebook(total=100, file=f) as bayes:
                # print(f) -> <__main__.StringIO object at 0x10fce7ed0>
                # print(f.getvalue()) -> ''
                assert isinstance(f, TextIOWrapper)  # check this works
                assert isinstance(f, StringIO)  # check this works
                for i in range(100):
                    bayes.update()

        # Test case 2:
        # check that this case passes 100% with only python2

# Generated at 2022-06-14 14:03:54.499047
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .tests import IPYTHON, NO_IPYTHON, PY3
    import matplotlib.pyplot as plt
    import io

    if NO_IPYTHON:
        return

    try:
        import ipywidgets
        assert IPYTHON
    except ImportError:
        return

    if PY3:
        def u(x):
            return x
    else:
        def u(x):
            return unicode(x)

    with io.StringIO() as f:
        with tqdm_notebook(total=10, file=f) as pbar:
            pbar.display(pos=1)
        assert u('\r  0%|') in f.getvalue()

# Generated at 2022-06-14 14:04:05.061977
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    # Make sure the bar doesn't close if there were no iterations
    with tqdm_notebook(total=None, desc="desc1") as bar:
        assert bar.container.children[-2].bar_style != 'success'
        assert bar.container.children[-2].bar_style != 'danger'
    with tqdm_notebook(total=0, desc="desc2") as bar:
        assert bar.container.children[-2].bar_style != 'success'
        assert bar.container.children[-2].bar_style != 'danger'


# # This test may fail in some configurations (#452 #872 #924)
# # See issue #78, #187, #307, #451, #558, #872
# # The reason is that IProgress should be updated when ipywidgets is updated.
#

# Generated at 2022-06-14 14:04:12.162884
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from six import StringIO

    f = StringIO()
    with tqdm_notebook(
            total=2,
            file=f,
            leave=False,
            disable=False) as pbar:
        pbar.display()
        pbar.clear()  # should do nothing
        pbar.update()

    f.seek(0)
    assert len(f.readlines()) == 2


if __name__ == '__main__':
    test_tqdm_notebook_clear()

# Generated at 2022-06-14 14:04:20.220250
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():  # pragma: no cover
    from time import sleep
    for i in tqdm_notebook(range(10), desc='1st loop'):
        for j in tqdm_notebook(range(5), desc='2nd loop', leave=False):
            for k in tqdm_notebook(range(100), desc='3nd loop'):
                sleep(0.01)
    for i in trange(10, desc='1st loop'):
        for j in trange(5, desc='2nd loop', leave=False):
            for k in trange(100, desc='3nd loop'):
                sleep(0.01)
    # not much to really test...
    # TODO: run it in the terminal

# Generated at 2022-06-14 14:05:11.252528
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from tqdm import _tqdm_notebook
    # Test msg
    pbar = _tqdm_notebook.tqdm_notebook(gui=True)
    pbar.container.children[1].bar_style = ''
    pbar.display(msg='Testing')
    assert pbar.container.children[1].bar_style == ''
    assert pbar.container.children[0].value == ''
    assert pbar.container.children[2].value == 'Testing'
    pbar.display(msg='Testing|<bar/>|Testing')
    assert pbar.container.children[1].bar_style == ''
    assert pbar.container.children[0].value == 'Testing'
    assert pbar.container.children[2].value == 'Testing'
    pbar.display(msg='')
   

# Generated at 2022-06-14 14:05:20.415551
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # Simple manual test
    iterable = tqdm_notebook([1, 2, 3, 4, 5], display=False)
    for i in iterable:
        assert i in [1, 2, 3, 4, 5]
    # Manual test, manual close
    iterable = tqdm_notebook([1, 2, 3, 4, 5], display=False)
    for i in iterable:
        raise KeyboardInterrupt
    iterable.close()
    # Manual test, auto close
    iterable = tqdm_notebook([1, 2, 3, 4, 5], leave=True, display=False)
    for i in iterable:
        raise KeyboardInterrupt
    # Manual test, auto close, manual reset

# Generated at 2022-06-14 14:05:26.657536
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep

    with tqdm_notebook(total=5) as t:
        for i in range(5):
            sleep(0.5)
            t.update()

    with tqdm_notebook(total=5) as t:
        for i in range(5):
            sleep(0.5)
            t.update(1)

    with tqdm_notebook(total=5) as t:
        for i in range(5):
            sleep(0.5)
            t.update(1, "Iterating")

    with tqdm_notebook(total=5) as t:
        for i in range(5):
            sleep(0.5)
            t.update(1, "Iterating", 'red')



# Generated at 2022-06-14 14:05:31.420043
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep
    from tqdm.auto import tqdm

    @tqdm_notebook
    def test_gen_n(n):
        for _ in test_gen(n):
            sleep(0.05)
            yield

    @tqdm
    def test_gen(n):
        for i in test_gen(n):
            sleep(0.05)
            yield i

    for _ in test_gen_notebook(3):
        pass
    for _ in test_gen(3):
        pass

if __name__ == "__main__":
    test_tqdm_notebook_update()

# Generated at 2022-06-14 14:05:34.018112
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # testing update
    with tqdm_notebook(total=12, leave=False) as t:
        for i in t:
            t.update(2)

# Generated at 2022-06-14 14:05:43.753460
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    import sys
    import time
    from tqdm import tqdm, trange
    try:
        from IPython.display import clear_output
    except ImportError:
        pass
    from .std import tqdm as std_tqdm

    def test_manual(inp, desc=''):
        """
        Expect .display() to do the following:
        - Update the value of the progress bar
        - Update the description text
        - Update the bar format
        - Update the bar color
        - Clear the progress bar

        Display the progress bar with and without `check_delay`
        (to test that the progress bar is only displayed once).
        """
        # Clear previous output (really necessary?)
        if 'clear_output' in globals():
            clear_output(wait=1)
        # Create progress bar
        pbar

# Generated at 2022-06-14 14:05:50.713677
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """Check that `tqdm_notebook.__iter__` examples works as expected."""
    # %%
    import time
    from tqdm.notebook import tqdm

    def foo():
        for i in tqdm(range(0, 5), desc='1st loop'):
            time.sleep(1)
        for i in tqdm(range(0, 5), desc='2nd loop'):
            time.sleep(1)
        return

    # %%
    # Check example
    foo()

# Generated at 2022-06-14 14:05:59.630157
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # test tqdm_notebook with n
    with tqdm_notebook(total=100) as t:
        for i in range(100):
            assert t.n <= 100
            t.update(n=1)
        assert t.n == 100
        # test tqdm_notebook with n=0
        t.update(n=0)
        assert t.n == 100
        # test tqdm_notebook with n as a string
        t.update(n='0')
        assert t.n == 100
        # test tqdm_notebook with negative n
        t.update(n=-1)
        assert t.n == 100
        # test tqdm_notebook with n=0.0
        t.update(n=0.0)
        assert t.n == 100
        # test

# Generated at 2022-06-14 14:06:10.123667
# Unit test for method status_printer of class tqdm_notebook

# Generated at 2022-06-14 14:06:16.375729
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import functools
    import time
    import ipywidgets
    import IPython.display as display

    np = tqdm_notebook(total=10)
    np.update(1)
    assert np.n == 1
    assert isinstance(np.container, ipywidgets.HBox)
    assert np.container.children[0].value == "<b>Description:</b>  "
    assert isinstance(np.container.children[1], ipywidgets.FloatProgress)
    assert isinstance(np.container.children[2], ipywidgets.HTML)
    assert np.container.children[2].value == ""

    np = tqdm_notebook(total=10, desc='text desc')
    np.update(1)
    assert np.n == 1