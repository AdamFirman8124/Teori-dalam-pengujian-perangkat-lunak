

# Generated at 2022-06-14 13:58:27.429145
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from random import random
    from time import sleep
    from unittest import TestCase
    from tempfile import TemporaryFile

    # We need to use a file object specified as 'file' for
    # the unit test, otherwise the test will pass as there is no
    # output to display (NOQA is for flake8 to avoid F821 error)
    class _TestUpdate(TestCase):
        def runTest(self):
            for i in tqdm_notebook(list(range(10)), file=self.f, ncols=False):
                sleep(random() / 100.)  # NOQA
            # self.assertEqual(self.f.getvalue().count('%'), 10)
    with TemporaryFile() as f:
        test = _TestUpdate()
        test.f = f
        test.runTest()



# Generated at 2022-06-14 13:58:36.048234
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    """Unit test for `TqdmHBox.__repr__` method"""
    from io import StringIO
    from contextlib import redirect_stdout

    stream1 = StringIO()
    stream2 = StringIO()
    with redirect_stdout(stream1):
        tqdm.write('Test')
    with redirect_stdout(stream2):
        print(TqdmHBox(pbar=tqdm))

    # Make sure `__repr__` runs with no errors
    assert stream1.getvalue().strip() == stream2.getvalue().strip()



# Generated at 2022-06-14 13:58:37.566034
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=2) as t:
        t.clear()

# Generated at 2022-06-14 13:58:46.991828
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test the method `status_printer` of class `tqdm_notebook`.
    """

    # Test with default argument
    msg = tqdm_notebook.status_printer(None)
    assert isinstance(msg, HBox)
    assert len(msg.children) == 3
    assert isinstance(msg.children[0], HTML)
    assert msg.children[0].value == ''
    assert isinstance(msg.children[1], IProgress)
    assert msg.children[1].value == 0
    assert msg.children[1].max == 1
    assert isinstance(msg.children[2], HTML)
    assert msg.children[2].value == ''

    # Test with total and desc arguments
    msg = tqdm_notebook.status_printer(None, 100, 'Hello')

# Generated at 2022-06-14 13:58:56.800765
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():  # pragma: no cover
    out = std_tqdm.status_printer(None, 10, 'Parsing in progress ...')
    assert out == "[  0%]: Parsing in progress ...\r"

    out = std_tqdm.status_printer(
        None, 10, 'Parsing in progress ...', 40)
    assert out == "[  0%]: Parsing in progress ...\r"

    out = tqdm_notebook.status_printer(
        None, 10, 'Parsing in progress ...')
    assert out.__repr__()
    assert out.__repr__(True)
    assert '<IPython.core.display.HTML object' in str(out)
    assert '>' in str(out)

# Generated at 2022-06-14 13:59:07.804162
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import unittest
    from .tests import tests

    class TqdmNotebookUpdateTests(tests.TqdmUpdateTestCase):
        tgr = tqdm_notebook
        module = tqdm_notebook

        def setUp(self):
            super(TqdmNotebookUpdateTests, self).setUp()
            self.pbar = tqdm_notebook(self.iterable, desc='', leave=True, ncols=50)

        def finish(self):
            self.pbar.close()
            text = self.pbar.format_dict['_postfix']
            elapsed_time = text[text.find("[") + len("["):text.find("s]")]
            elapsed_time = float(elapsed_time)

# Generated at 2022-06-14 13:59:17.902793
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    Test tqdm.notebook.tqdm.update()
    """
    from time import sleep
    from .gui import tqdm
    from .utils import format_sizeof

    try:
        from IPython.display import clear_output
    except ImportError:
        clear_output = None

    n = 10000
    for i in tqdm(range(1, n + 1), total=n, leave=False, ascii=True):
        sleep(0.001)
    # note: if `leave=False` is not present, the final clarity is left
    #       to __del__ of tqdm (see #83)

    # Test reset
    if clear_output:
        clear_output()


# Generated at 2022-06-14 13:59:22.032878
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import sys

    with tqdm(total=4) as t:
        for i in range(4):
            t.update()

    with tqdm(total=0) as t:
        t.update(1)
        assert t.total == 0
        t.update(2)
        assert t.total == 0
        t.update(5)
        assert t.total == 0

    with tqdm(total=0, dynamic_ncols=True) as t:
        t.update(1)
        assert t.total == 1
        t.update(2)
        assert t.total == 3
        t.update(5)
        assert t.total == 8

    with tqdm(total=0, dynamic_ncols=True) as t2:
        t2.update(1)
        t

# Generated at 2022-06-14 13:59:26.762314
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from IPython.display import clear_output
    import time
    test_list = [1, 2, 3]
    for item in tqdm(test_list, desc='Testing', ascii=True):
        if item == 2:
            time.sleep(1)
            clear_output()
        time.sleep(0.25)

# Generated at 2022-06-14 13:59:36.235803
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from random import random, randint
    from time import sleep
    out = tqdm_notebook(["a", "b", "c", "d"], desc="Loading", ncols=200)
    pb = out.container  # the real ipywidgets.Widget
    assert pb.max == 4
    assert pb.value == 0
    assert pb.bar_style == ''
    assert pb.children[0].value == 'Loading: '
    assert pb.children[2].value == ''
    out.display(bar_style='warning')
    assert pb.bar_style == 'warning'
    out.display(bar_style='danger')
    assert pb.bar_style == 'danger'
    out.display(bar_style='success')
    assert pb.bar_style == 'success'


# Generated at 2022-06-14 14:00:08.400426
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    tqdm_notebook.status_printer(_range(10), 10, "", 20)

# Generated at 2022-06-14 14:00:17.897351
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from .std import tqdm as std_tqdm
    from .std import tqdm_gui as std_tqdm_gui

    file = sys.stderr

    total = 10
    desc = "Test"
    ncols = 100

    # Case: IProgress not found
    try:
        std_tqdm_gui.status_printer(file, total, desc, ncols)
    except ImportError:
        pass

    # Case: create progress bar
    pbar = std_tqdm_gui.status_printer(file, total, desc, ncols)
    assert isinstance(pbar, std_tqdm.IProgress)
    assert pbar.min == 0
    assert pbar.max == total
    assert pbar.bar_style == ''

# Generated at 2022-06-14 14:00:24.692019
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    from IPython.html.widgets import HBox
    from functools import partial
    f = lambda: tqdm_notebook(total=1, leave=True).display()
    b = HBox([f(), f(), f()])
    display(b)
    sleep(.01)
    # since total is 'None|1|1', total is not computable and width is fixed
    assert b.children[0].layout.width == b.children[1].layout.width
    assert b.children[1].layout.width == b.children[2].layout.width
    # reset first one
    b.children[0].pbar.reset(total=2)
    # since total is '2|1|1', total is not computable and width is reset to %
    assert b.children[1].layout

# Generated at 2022-06-14 14:00:33.126321
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from contextlib import contextmanager

    @contextmanager
    def capture():
        from cStringIO import StringIO
        from sys import stdout
        old, sys.stdout = sys.stdout, StringIO()
        yield sys.stdout
        sys.stdout = old

    with capture() as captured:
        t = tqdm_notebook(total=10)
        for i in range(10):
            t.set_description("State %d" % (i,))
            t.update(1)
        t.close()

    with capture() as captured:
        t = tqdm_notebook(total=10)
        for i in range(10):
            t.set_description("State %d" % (i,))
            t.update(1)
        t.clear()

    assert captured.getvalue()

# Generated at 2022-06-14 14:00:40.590703
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from inspect import signature
    from .std import tqdm

    file = sys.stdout
    if IPY == 4:
        if 'total' not in signature(tqdm_notebook.status_printer).parameters:
            raise ValueError('IPython 4.x: total not in signature of status_printer')
    else:  # IPY == 3
        if 'total' in signature(tqdm_notebook.status_printer).parameters:
            raise ValueError('IPython 3.x: total in signature of status_printer')

    def _test_out(out, total, desc, ncols):
        assert out.min == 0
        assert out.max == total
        if total is None:
            assert not out.bar_style


# Generated at 2022-06-14 14:00:52.254844
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import io
    import io as io_orig
    import sys
    if sys.version_info.major < 3:
        io_orig.FileIO = io.FileIO
        io.FileIO = None

# Generated at 2022-06-14 14:01:00.674207
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from itertools import count
    from .utils import FormatCustomTextType, format_updatable

    # Checks a basic functionality
    pbar = tqdm.status_printer(None, 1000000, "test")
    for i in count():
        pbar.value = i
        if i >= pbar.max:
            pbar.close()
            break

    # Checks text customization
    lbar = '{l_bar}'
    rbar = '{desc}: {percentage:3.0f}%|{bar}| {r_bar:20}'
    pbar = tqdm.status_printer(None, 1000000, "", lbar, rbar, 100, None)
    for i in count():
        pbar.value = i
        if i >= pbar.max:
            pbar.close

# Generated at 2022-06-14 14:01:12.214969
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:  # ipywidgets not installed
        from ipywidgets import FloatProgress, IntProgress
    except ImportError:
        return

    def _test(TProgress):
        pbar = tqdm_notebook(total=None, unit='foo', ncols=100,
                             miniters=None, mininterval=0, mininterval2=0,
                             desc=None, position=None, dynamic_ncols=True,
                             file=None, ascii=None, disable=False,
                             leave=False, unit_scale=False,
                             gui=True, colour='white')
        pbar.container = TProgress()

        pbar.reset(total=None)
        assert pbar.container.pbar.max is None
        assert pbar.container.pbar.value == 0

# Generated at 2022-06-14 14:01:21.452997
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    """Unit test for method clear of class tqdm_notebook"""
    try:
        from unittest.mock import patch
        from unittest.mock import Mock
    except ImportError:
        from mock import patch
        from mock import Mock

    t = tqdm_notebook(total=2, leave=False)
    t.n = 0

    with patch('IPython.display.clear_output') as mock_clear:
        t.clear()
        assert mock_clear.call_count == 0

    with patch('IPython.display.clear_output') as mock_clear:
        t.display()
        t.clear()
        assert mock_clear.call_count == 0

    with patch('IPython.display.clear_output') as mock_clear:
        t.update()
        t.clear()
       

# Generated at 2022-06-14 14:01:32.791097
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from itertools import count
    from datetime import timedelta

    for leave in [True, False]:

        for unit_scale in [1, 1.0, True]:
            for total in [0, 1/unit_scale, 2/unit_scale, 10/unit_scale]:
                pbar = tqdm_notebook(count(), total=total, unit_scale=unit_scale, leave=leave)
                for _ in pbar:
                    pass
                pbar.reset(total=total)
                pbar.close()


# Generated at 2022-06-14 14:02:50.026811
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    b = std_tqdm(total=1)
    b.n = None
    b.pulse()
    hb = TqdmHBox(children=[])
    hb.pbar = b
    assert (b.format_dict == hb._repr_json_())

# Generated at 2022-06-14 14:02:53.660604
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from tqdm.auto import trange
    for i in trange(9):
        pass


if __name__ == "__main__":
    test_tqdm_notebook_update()

# Generated at 2022-06-14 14:03:03.555812
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .gui import tgrange
    from .misc import _term_move_up

    with tqdm_notebook(total=4, desc="test__iter__") as pbar:
        for _ in range(5):
            pbar.update(1)
            if pbar.n > pbar.total:
                break
        pbar.clear()
    with tqdm_notebook(total=4, desc="test__iter__") as pbar:
        for _ in range(5):
            pbar.update(1)
            if pbar.n > pbar.total:
                break
        pbar.clear()
    with tqdm_notebook(total=4, desc="test__iter__") as pbar:
        for _ in range(5):
            pbar.update(1)

# Generated at 2022-06-14 14:03:10.010208
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from .utils import _range
    from .std import format_interval
    from .std import time

    with tqdm_notebook(total=1e3, desc="world",
                       bar_format="{l_bar}{bar:10}{r_bar} [{remaining}{postfix}]") as t:
        for i in _range(100):
            t.set_postfix(foo='bar', bar=i)
            time.sleep(0.01)
            t.update(10 * i)
            time.sleep(0.01)


# Generated at 2022-06-14 14:03:15.948707
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    prog_bar = tqdm_notebook.status_printer(None, total=200, desc='TEST', ncols=100)
    html = prog_bar._repr_html_()
    # print(html)
    assert 'TEST' in html
    assert '<progress' in html
    assert 'width="100px"' in html


# Generated at 2022-06-14 14:03:26.688518
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():

    # import the tested class
    from ._tqdm_notebook import tqdm_notebook

    # create an instance of the tested class (without arguments)
    tb = tqdm_notebook()
    assert tb.disable is False
    assert tb.unit_scale == 1
    assert tb.lock_args == {}
    assert tb.last_print_n is None
    assert tb.unit == ''
    assert tb.leave == False
    assert tb.miniters == 0
    assert tb.ascii == False
    assert tb.maxinterval == 10.0
    assert tb.interval == 0.05
    assert tb.smoothing == 0.3
    assert tb.avg_time == None

    # call the method under test
    tb.clear()


# Generated at 2022-06-14 14:03:33.511010
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import os

    # Cleanup any previous output
    for f in os.listdir('.'):
        if f.startswith('_tqdm_notebook_status_printer_test_'):
            os.remove(f)

    import tempfile
    from types import GeneratorType

    # Create a dummy file with a fixed name to avoid multiple calls
    # to the same test
    fname = '_tqdm_notebook_status_printer_test_'
    fh, fname = tempfile.mkstemp(suffix=fname)
    # Note: cannot close the file it will be overwritten
    #       with the generating function

    # Define test function

# Generated at 2022-06-14 14:03:38.756571
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import tqdm.notebook as tn
    try:
        bar = tn.tqdm_notebook(total=2, desc='Testing clear')
        bar.update()
        bar.clear()
        assert bar.last_print_n == 0
    finally:
        bar.close()



# Generated at 2022-06-14 14:03:46.819243
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    pbar = IProgress(min=0, max=5)
    pbar.value = 2
    pbar.bar_style = ''
    ltext = HTML()
    ltext.value = "test"
    rtext = HTML()
    rtext.value = "desc"
    container = TqdmHBox(children=[ltext, pbar, rtext])
    container.pbar = proxy(pbar)
    result = container.__repr__(False)
    expected = '  0%|          | 0/5 [00:00<?, ?it/s]testdesc'
    assert result == expected



# Generated at 2022-06-14 14:03:55.699838
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():  # {{{
    """Unit test for method update of class tqdm_notebook"""
    try:
        from IPython.display import clear_output
    except ImportError:
        pass
    else:
        # Reset ipywidgets:
        try:
            clear_output()
        except Exception:  # pragma: no cover
            pass
        tqdm.pandas()
        tnrange(2)  # tqdm.notebook.tnrange
        trange(2)  # tqdm.notebook.trange
        pbar = tqdm_notebook(total=3)
        for i in range(4):
            pbar.set_description("test" + str(i))
        pbar.clear()
        pbar.write("")

# Generated at 2022-06-14 14:05:54.972171
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """Test case for tqdm_notebook class"""
    iterable_items = ['cat', 'dog', 'rabbit', 'chicken']
    tqdm_widget = tqdm_notebook(iterable_items)

    assert tqdm_widget.n == 0
    assert next(tqdm_widget) == 'cat'
    assert tqdm_widget.n == 1
    assert next(tqdm_widget) == 'dog'
    assert tqdm_widget.n == 2
    assert next(tqdm_widget) == 'rabbit'
    assert tqdm_widget.n == 3
    assert next(tqdm_widget) == 'chicken'
    assert tqdm_widget.n == 4
    assert tqdm_widget.leave == True

# Generated at 2022-06-14 14:05:59.391848
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    from tqdm import tqdm_notebook as tqdm
    t = tqdm([1, 2, 3])
    for i in t:
        sleep(0.1)
        if i == 2:
            t.close()
            raise ValueError
    assert not t.displayed
    t.container.close()



# Generated at 2022-06-14 14:06:08.963414
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    class TqdmNotebook(tqdm_notebook):
        def display(self, pos=None, close=False, bar_style='info'):  # NOQA
            TqdmNotebook.pos = pos
            TqdmNotebook.close = close
            TqdmNotebook.bar_style = bar_style

    TqdmNotebook().close()
    assert (TqdmNotebook.close, TqdmNotebook.bar_style) == (True, 'info')
    TqdmNotebook(miniters=0).update()
    assert (TqdmNotebook.pos, TqdmNotebook.close, TqdmNotebook.bar_style) == (0, False, 'info')

# Generated at 2022-06-14 14:06:15.693200
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    from time import sleep
    from datetime import timedelta
    from tqdm.auto import tqdm, trange
    from tests_tqdm import with_setup, _range

    @with_setup(pretest=lambda: tqdm.pandas())
    def test_display_1():
        with tqdm(total=100) as pbar:
            for i in _range(10):
                pbar.display(i)
                sleep(0.01)
            assert pbar._inst_force == pbar._inst_force_max
        # To test "not pbar.disable" in tqdm.display()


# Generated at 2022-06-14 14:06:20.389559
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """Test method `__iter__` of class `tqdm_notebook`."""
    try:
        import tqdm.notebook as tn
    except ImportError:
        return None
    for __ in tn.tqdm_notebook(range(2), leave=True):
        pass



# Generated at 2022-06-14 14:06:30.250292
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .std import tqdm
    with tqdm.external_write_mode():
        # test 1
        t = tqdm()
        for _ in t:
            t.set_description("Hello world!")
            # test 2
            break
        t.reset()
        with t.set_description("Hello world!"):
            # test 3
            t.reset()
        for _ in t:
            # test 4
            pass
        t.reset()
        for _ in t:
            pass
        # test 5
        t.set_description("Hello world!")
        # test 6
        t.set_description("Hello world!", refresh=False)
        # test 7
        t.set_description("Hello world!", refresh=True)



# Generated at 2022-06-14 14:06:37.005301
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # Dummy starts
    tqdm.status_printer(None, total=3)
    tqdm.status_printer(None, total=3, ncols=100)
    tqdm.status_printer(None, total=3, ncols=150)
    tqdm.status_printer(None, total=0)


if __name__ == '__main__':
    test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 14:06:41.135912
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():  # pragma: no cover
    """
    Unit test of tqdm_notebook constructor.
    """
    tqdm_notebook(total=100)
    trange(100)
    tnrange(100)
    tqdm_notebook(total=100, leave=True, desc='Test')


# Generated at 2022-06-14 14:06:43.437719
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from tqdm.auto import trange
    from time import sleep
    with trange(1) as t:
        t.update()
        sleep(0.2)



# Generated at 2022-06-14 14:06:45.681797
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=10) as pbar:
        for i in range(10):
            pbar.clear()
            pbar.update()