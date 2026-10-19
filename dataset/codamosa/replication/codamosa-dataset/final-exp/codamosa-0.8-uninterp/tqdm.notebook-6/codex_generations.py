

# Generated at 2022-06-14 13:58:16.281993
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    This test must be run as a Notebook.
    """
    import io
    import sys
    import unittest
    from IPython.utils import io

    class TestUpdate(unittest.TestCase):
        def setUp(self):
            # ensure that we can create the widget without raising
            self.pbar = tqdm_notebook(total=100)

        @io.capture_output(stdout=True, display=False)
        def test_update(self):
            # Test text progress bar.
            self.pbar.update()

    TestUpdate().test_update()

# Generated at 2022-06-14 13:58:18.353187
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=0, desc="Testing tqdm_notebook.clear") as t:
        t.update(1)
        assert t.n == 1
        t.clear()
        assert t.n == 0
    assert t.n == 0

# Generated at 2022-06-14 13:58:21.627557
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    # TODO: it is a useless test, see #748
    t = tqdm_notebook(total=None)
    t.clear()
    if 'cleanup' in dir(t):
        t.cleanup()

# Generated at 2022-06-14 13:58:28.844743
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    from time import time
    import numpy as np

    t = time()
    pbar = tqdm_notebook(total=100)
    for i in range(10):
        pbar.display(i)
        time()
        time()
        time()
    pbar.close()
    assert time() - t < 1

    t = time()
    pbar = tqdm_notebook(total=100)
    for i in range(10):
        pbar.display(i)
        time()
        time()
        time()
    pbar.close()
    assert time() - t < 1

    t = time()
    pbar = tqdm_notebook(total=100)

# Generated at 2022-06-14 13:58:39.693760
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    t = tqdm_notebook(total=10)

    t.reset()
    assert t.n == 0 and t.total == 10

    t.reset(total=100)
    assert t.n == 0 and t.total == 100

    t.reset(100)
    assert t.n == 0 and t.total == 100

    t = tqdm_notebook(total=10, leave=True)

    t.reset()
    assert t.n == 1 and t.total == 10  # 1 because we don't call update again

    t.reset(total=100)
    assert t.n == 1 and t.total == 100

    t.reset(total=100)
    assert t.n == 1 and t.total == 100

# Generated at 2022-06-14 13:58:49.799448
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """ Unit test for method :status_printer: of class :tqdm_notebook:
        This unit test is a first test and is VERY important, because it test the status printer,
        the main method of this class.
    """
    test_tqdm_notebook_status_printer.tested = True
    pbar = tqdm_notebook.status_printer(None, total=10, desc="Test")
    assert pbar.children[0].value == "Test", "Value of HBox left (HBox[0]) is not correct"
    assert pbar.children[1].max == 10, "Value of bar HBox[1] max must be 10"
    assert pbar.children[2].value == "", "Value of HBox right (HBox[2]) is not correct"
    # Test the layout

# Generated at 2022-06-14 13:58:55.929624
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        import ipywidgets
    except ImportError:
        return
    with tqdm_notebook(range(3), desc='foobar') as t:
        for i in t:
            assert isinstance(t, tqdm_notebook)
            pass
        assert not hasattr(t, 'container')
        try:
            t.container.close()
        except AttributeError:
            pass  # already deleted
    import gc
    gc.collect()



# Generated at 2022-06-14 13:58:57.587855
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    for i in tqdm_notebook([0, 1, 2]):
        assert i in [0, 1, 2]


# Generated at 2022-06-14 13:59:03.076266
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from io import StringIO
    sys.stdout = StringIO()
    with tqdm(total=3) as progress_bar:
        progress_bar.displayed = True
        progress_bar.update()
        progress_bar.update()
        progress_bar.update()
        sys.stdout = sys.__stdout__
    assert not progress_bar.disable



# Generated at 2022-06-14 13:59:14.169451
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    import sys
    import unittest
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    from io import StringIO
    from tqdm.notebook import tqdm_notebook

    capture_out = StringIO()

    class OverrideStdERR(StringIO):
        def isatty(self):
            return True


# Generated at 2022-06-14 13:59:32.024470
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    ltext = HTML()
    pbar = IProgress(min=0, max=10)
    rtext = HTML()
    container = TqdmHBox(children=[ltext, pbar, rtext])

    tqdm_notebook.status_printer(fp=sys.stdout, total=10, desc='desc', ncols='100%')
    pbar.bar_style = 'info'
    tqdm_notebook.status_printer(fp=sys.stdout, total=0, desc='desc', ncols='100%')
    pbar.bar_style = ''

    tqdm_notebook.status_printer(fp=sys.stdout, desc='desc', ncols='100%')
    pbar.bar_style = 'info'
    tqdm_notebook.status_

# Generated at 2022-06-14 13:59:34.931260
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import pytest
    with pytest.raises(RuntimeError):
        with tqdm_notebook(total=2) as t:
            t.clear()
            t.__enter__()

# Generated at 2022-06-14 13:59:47.267165
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import sys  # noqa
    try:
        from IPython.utils import io  # noqa
        io.capture_output()
        print_captured = True
    except ImportError:
        # Capture not supported, just let it print
        print_captured = False
    try:
        from StringIO import StringIO  # noqa
    except ImportError:
        from io import StringIO  # NOQA

    output = StringIO()
    tqdm_notebook(range(3), file=output)
    tqdm_notebook(range(3), file=output).clear()
    tqdm_notebook(range(3), file=output).clear(nolock=True)

    # Restore stdout
    if print_captured:
        io.capture_output(stdout=True)


# Generated at 2022-06-14 13:59:56.071597
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from IPython.core.display import HTML
    from IPython.core.display import display

    tqdm_notebook.status_printer(None,total=100,desc="desc")
    tqdm_notebook.status_printer(None,total=100,desc="desc",ncols=100)
    tqdm_notebook.status_printer(None,total=100,desc="desc",ncols="100%")
    tqdm_notebook.status_printer(None,total=100,desc="desc",ncols="200px")
    tqdm_notebook.status_printer(None,total=None,desc="desc",ncols=10)
    pbar = tqdm_notebook.status_printer(None,total=100,desc="desc")

# Generated at 2022-06-14 14:00:06.090307
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from re import sub
    from IPython.display import clear_output
    from unittest import TestCase

    class Test_status_printer(TestCase):
        def setUp(self):
            self.out = tqdm_notebook.status_printer(
                'stdout', 42, '42nd iteration', ncols='100%')

        def tearDown(self):
            # clear_output(wait=1)
            del self.out

        def test_class(self):
            self.assertEqual(self.out.__class__.__name__, 'HBox')
            self.assertEqual(self.out.children[1].min, 0)
            self.assertEqual(self.out.children[1].value, 0)

# Generated at 2022-06-14 14:00:12.903255
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:
        from IPython import get_ipython
        ipy = get_ipython()
        if ipy is None:
            raise ImportError()
    except ImportError:
        return  # not an ipython env -> no test to run
    else:
        ipy.magic('gui qt5')

    with tqdm_notebook(total=1) as pbar:
        pbar.reset(total=2)
        assert pbar.total == 2

    with tqdm_notebook(total=None, leave=True) as pbar:
        pbar.reset(total=2)
        assert pbar.total == 2

    with tqdm_notebook(total=1, leave=True) as pbar:
        pbar.reset(total=None)
        assert pbar.total == None

# Generated at 2022-06-14 14:00:16.110953
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Unit test for IPython/Jupyter Notebook widget using tqdm!
    """
    try:
        _test_tqdm_notebook_status_printer()
    except ImportError:
        pass



# Generated at 2022-06-14 14:00:19.864268
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep
    t = tqdm_notebook(total=2)
    assert isinstance(t, tqdm_notebook)
    try:
        t.update()
    except:
        pass
    sleep(2)
    t.display()
    sleep(2)
    t.display()
    t.close()

# Generated at 2022-06-14 14:00:24.153326
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    with tqdm_notebook(total=2) as bar:
        bar.update()
        assert bar.displayed
        bar.close()
        assert not bar.displayed
        bar.close()
        assert not bar.displayed
        bar.total = 4
        bar.close()
        assert not bar.displayed

        bar.reset()
        bar.close()
        assert not bar.displayed
        bar.reset(total=4)
        bar.close()
        assert not bar.displayed

# Generated at 2022-06-14 14:00:28.842786
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    with tqdm_notebook(total=4, leave=True) as pbar:
        for i in range(3):
            pbar.n += 1
        pbar.reset()
        for i in range(3):
            pbar.n += 1

if __name__ == '__main__':
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:00:55.441047
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=5) as pbar:
        pbar.postfix = 'remaining'
        assert re.search(r'\[\ ?\]', pbar.container.__repr__(True))
        pbar.clear()
        assert re.search(r'\[\ ?\]', pbar.container.__repr__(True))
        pbar.clear('remaining')
        assert re.search(r'\[\ ?\]', pbar.container.__repr__(True))



# Generated at 2022-06-14 14:01:03.318827
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Test status printer"""
    pbar = tqdm_notebook.status_printer(None, 5, "test")
    ncols = '100%'
    pbar2 = tqdm_notebook.status_printer(None, 5, "test", ncols)
    assert pbar2.layout.width == ncols
    assert pbar2.layout.display == 'inline-flex'
    assert pbar2.layout.flex_flow == 'row wrap'
    assert hasattr(pbar2, 'children')
    assert len(pbar2.children) == 3
    assert type(pbar2.children[1]) == IProgress
    assert hasattr(pbar2.children[1], 'min')
    assert hasattr(pbar2.children[1], 'max')

# Generated at 2022-06-14 14:01:15.411897
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    Unit test for method update of class tqdm_notebook.
    """
    import time
    from multiprocessing import Pool

    class T(tqdm_notebook):
        """
        Testing subclass of tqdm_notebook.
        """
        @staticmethod
        def disp(*args, **kwargs):
            """
            Wrapper around tqdm_notebook.display that allows passing of self.
            """
            # close before displaying a bar
            if args and 'close' in args[0]:
                if kwargs.pop('close', None):
                    try:
                        T.w.close()
                    except BaseException:
                        pass
            return T.w.display(*args, **kwargs)


# Generated at 2022-06-14 14:01:23.172301
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    with tqdm_notebook(total=None, leave=True) as t:
        t.display()
        t.display("Test 1.", pos=0)
        t.display("Test 2.", pos=1)
        t.display("Test 3.", pos=2)
        t.display("Test 4.", pos=3)
        t.display("Test 5.", pos=4)
        t.display("Test 6.", pos=5)
        t.display("Test 7.", pos=6)
        t.display("Test 8.", pos=7)
        t.display("Test 9.", pos=8)
        t.display("Test 10.", pos=9)
        t.display("Test 11.", pos=10)
        t.display("Test 12.", pos=11)
        t.display("Test 13.", pos=12)

# Generated at 2022-06-14 14:01:33.724018
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # iterating over an empty loop should not raise an exception
    for i in trange(0):
        pass
    # test iterating over a range
    for i in trange(4):
        assert i < 4
    # test iterating over a list
    for i in trange([0, 1, 2, 3]):
        assert i < 4
    # test iterating over a generator
    for i in trange((x for x in [0, 1, 2, 3])):
        assert i < 4
    # test iterating over a dictionary
    for i in trange({'a': 1, 'b': 2}):
        assert i in ('a', 'b')
    # test iterating over a string
    for i in trange('1234'):
        assert i in ('1', '2', '3', '4')
   

# Generated at 2022-06-14 14:01:40.705777
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        # create a new iterable object
        iter_object = iter(tqdm_notebook(range(100)))

        # iterate over the list created above
        sum = 0
        while True:
            try:
                sum += iter_object.next()
            except StopIteration:
                break

        # check the sum
        if sum != 4950:
            raise AssertionError()

    except Exception as e:
        raise AssertionError(e)


# Generated at 2022-06-14 14:01:44.869885
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Tests the behaviour of the method status_printer of class tqdm_notebook.
    """
    from .tests import TestTqdmNotebook

    TestTqdmNotebook.test_status_printer(tqdm_notebook)

# Generated at 2022-06-14 14:01:51.439036
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import random
    import string

    random.seed(0)
    list_of_words = [random.choice(
        string.printable) for _ in range(10)]
    t = tqdm_notebook(list_of_words)
    t.reset(total=100)

    t.close()

# if __name__ == '__main__':
#     test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:01:55.464850
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    assert repr(tqdm_notebook.status_printer(
        None, 99999, ncols=100, desc="This is a test")) == (
        "{'bar_format': '{l_bar}<bar/>{r_bar}', "
        "'desc': 'This is a test', "
        "'dynamic_ncols': False, 'ncols': 100, 'total': 99999}")

# Generated at 2022-06-14 14:02:03.867795
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from IPython.html.widgets import ContainerWidget
    from IPython.utils.capture import capture_output
    t = tqdm_notebook()
    assert isinstance(t.container, ContainerWidget)
    t.close()
    with capture_output() as io:
        t.display()
    assert io.stdout == ""
    t.reset(total=10)
    assert t.miniters == 1
    t.update(100)
    assert t.miniters == 10
    t.close()

# Generated at 2022-06-14 14:03:16.187237
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    t = tqdm_notebook(total=12)
    t.update()
    t.update()
    t.update()
    t.update(8)
    t.close()
    return t

# Generated at 2022-06-14 14:03:18.910740
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    with tqdm_notebook(total=5) as bar:
        for i in bar:
            sleep(0.01)



# Generated at 2022-06-14 14:03:20.825162
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    pbar = tnrange(10)
    pbar.clear()
    pbar.close()

# Generated at 2022-06-14 14:03:30.789582
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from tqdm.auto import tqdm
    tqdm.monitor_interval = 0  # try to prevent unit tests hanging

    # Check the progress bars display nicely by default
    with tqdm(total=20) as pbar:
        for _ in range(20):
            pbar.update()

    # Check the progress bars display nicely with "pretty" = False
    with tqdm(total=20, bar_format="{l_bar}||{r_bar}", pretty=False) as pbar:
        for _ in range(20):
            pbar.update()

    # Check the progress bars display nicely with "pretty" = True

# Generated at 2022-06-14 14:03:35.680784
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import ipywidgets
    with ipywidgets.Output() as o:
        with tqdm_notebook(total=10) as pbar:
            for i in range(10):
                pbar.update(1)
            display(o)
        assert pbar.n == 10 and pbar.container.visible == False



# Generated at 2022-06-14 14:03:46.312700
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    import warnings
    try:
        import IPython
        have_ipython = True
    except ImportError:
        have_ipython = False


# Generated at 2022-06-14 14:03:55.328592
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Test method __iter__ of class tqdm_notebook
    """
    try:
        from unittest import mock
    except ImportError:
        from mock import mock
    n = 21
    dummy_iterable = (i for i in range(n))
    pbar = tqdm_notebook(dummy_iterable, leave=True)
    assertequal(pbar.container.__repr__(), '    0%|                                                   | 0/21 [00:00<?, ?it/s]')
    for i in range(n):
        assertequal(pbar.__iter__().__next__(), i)

# Generated at 2022-06-14 14:04:06.292172
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """Tests for tqdm_notebook.reset()"""
    from unittest import TestCase
    import time

    class T(TestCase):
        """Test class for tqdm_notebook.reset()"""
        @staticmethod
        def test_reset():
            """Test tqdm_notebook.reset()"""
            bar = tqdm_notebook()
            time.sleep(0.08)
            bar.update(1)
            time.sleep(0.08)
            bar.reset()
            time.sleep(0.08)
            bar.update(1)
            bar.close()
    T.test_reset()


if __name__ == '__main__':
    from tqdm._tqdm_test import TestTqdm
    TestTqdm.test_tqdm_notebook

# Generated at 2022-06-14 14:04:15.339780
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from .utils import _term_move_up
    pbar = tqdm_notebook(total=4)
    for _ in pbar:
        pbar.update(1)
    assert pbar.n == 4
    assert pbar.total == 4
    pbar.reset()
    assert pbar.n == 0
    assert pbar.total == 4
    pbar.reset(total=8)
    assert pbar.n == 0
    assert pbar.total == 8
    pbar.reset(total=None)
    pbar.reset()
    assert pbar.total == None
    assert pbar.n == 0
    pbar.reset(total=8)
    assert pbar.total == 8
    for _ in pbar:
        pbar.update(1)
    assert pbar.total == 8


# Generated at 2022-06-14 14:04:19.286154
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Simulate a simple iteration with tqdm notebook"""
    t = tqdm_notebook(total=10)
    for n in t:
        t.set_description(desc="DESCRIPTION")
        if n == 3:
            t.set_postfix(postfix="POSTFIX")
    t.close()


if __name__ == '__main__':
    test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 14:05:59.498638
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    from inspect import isclass
    # Test if TqdmHBox inherits from HBox
    assert(issubclass(TqdmHBox, HBox))

    # Test if TqdmHBox is really a subclass of HBox
    assert(issubclass(TqdmHBox, HBox))

    # Test if TqdmHBox is an instance of HBox
    assert(isinstance(TqdmHBox, HBox))

    # Test if TqdmHBox is really an instance of HBox
    assert(isinstance(TqdmHBox, HBox))

    # Test if TqdmHBox is an instance of HBox
    assert(isinstance(TqdmHBox, HBox))

    # Test if TqdmHBox is really an instance of HBox

# Generated at 2022-06-14 14:06:04.752037
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    tqdm_notebook.status_printer(None, ncols=100).children[-2].layout.width
    tqdm_notebook.status_printer(None, ncols=100).children[-2].value
    tqdm_notebook.status_printer(None, ncols=100).children[-1].value

# Generated at 2022-06-14 14:06:08.636013
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import sys
    from tqdm import tqdm
    for __ in tqdm(range(1000), file=sys.stdout):
        pass
    from IPython.display import clear_output
    clear_output(wait=True)

# Generated at 2022-06-14 14:06:12.821455
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    # Note: if this fails, test_tqdm_reset should also be updated
    # as they both test the same thing on different backends
    d = tqdm_notebook(total=9, desc='test')
    d.display(close=True)
    d.reset(total=10)
    d.display(close=True)
    d.reset()
    d.display(close=True)



# Generated at 2022-06-14 14:06:21.668717
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import sys
    # constant
    total = 1000000
    # pbar, ltext, rtext = tqdm_notebook.status_printer(sys.stdout, total)
    pbar, ltext, rtext = tqdm_notebook.status_printer(sys.stdout)

    # change bar style
    pbar.bar_style = 'info'
    assert(pbar.bar_style == 'info')
    pbar.bar_style = 'success'
    assert(pbar.bar_style == 'success')
    # change value
    pbar.value = 500000
    assert(pbar.value == 500000)
    # change description
    ltext.value = 'foobar'
    assert(ltext.value == 'foobar')
    # progress bar goes to 100%

# Generated at 2022-06-14 14:06:31.202036
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from base64 import b64encode
    from shutil import copyfileobj
    from io import BytesIO
    from urllib.parse import quote

    def save_png(fig, filename):
        buf = BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        base64img = b64encode(buf.read()).decode('ascii')
        data = 'data:image/png;base64,%s' % quote(base64img)
        display(HTML('<img src="%s">' % data))

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns


# Generated at 2022-06-14 14:06:36.083763
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test of the notebook status printer method.
    """
    # Test with total
    tqdm_notebook.status_printer(file=None, total=100)

    # Test with unknown total
    tqdm_notebook.status_printer(file=None, total=None)

# Generated at 2022-06-14 14:06:45.142446
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Test `status_printer` method of `tqdm_notebook` class"""
    t = tqdm_notebook
    p = t.status_printer
    l = HTML()
    pbar = IProgress(min=0, max=9)
    r = HTML()
    hbox = TqdmHBox(children=[l, pbar, r])
    pbar.layout.width = "20px"  # Default width is 100px
    assert p(hbox, 20) == hbox
    assert p(hbox, 20, desc="desc") == hbox
    assert p(hbox, 20, desc="multi\nline") == hbox

# Generated at 2022-06-14 14:06:52.091066
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    Display
    """
    with tqdm_notebook(total=9) as pbar:
        assert pbar.n == 0
        pbar.update()
        assert pbar.n == 1
        pbar.update(3)
        assert pbar.n == 4
        pbar.update(5)
        assert pbar.n == 9
    assert pbar.n == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 14:06:55.463473
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    loop = tqdm_notebook(total=10)
    loop.update(1)
    assert loop.n == 1
    assert not loop.disable
    loop.disp = lambda *_, **__: None
    loop.disable = True
    loop.update(1)
    assert loop.n == 2
    assert loop.disable

