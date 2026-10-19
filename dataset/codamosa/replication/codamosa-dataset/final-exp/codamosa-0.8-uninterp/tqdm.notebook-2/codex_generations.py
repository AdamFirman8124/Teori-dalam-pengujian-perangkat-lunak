

# Generated at 2022-06-14 13:58:39.478906
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from contextlib import contextmanager

    class out:
        """Store `stdout` and `display` calls in a class instance."""
        def __init__(self):
            self.clear()

        def write(self, x):
            self.stdout += x

        def display(self, x):
            self.displayed.append(x)

        def clear(self):
            self.stdout = ""
            self.displayed = []

    with contextmanager(out) as o:
        with tqdm_notebook(total=10, file=o) as bar:
            bar.display()
            assert o.displayed == [bar.container]
            assert '\r' not in o.stdout

            bar.display(msg='Something')
            assert o.displayed == [bar.container]

# Generated at 2022-06-14 13:58:49.338932
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test tqdm.tqdm_notebook.status_printer function by comparing with
    known good result.
    """
    # import json
    import sys
    # import io
    # import tempfile

    # Testing
    try:
        tqdm_notebook.status_printer(sys.stdout, 101)
    except:
        print("\nError: tqdm_notebook.status_printer function not found")
        raise

    # tqdm_notebook.status_printer(sys.stdout, 101)
    # with tempfile.TemporaryFile() as tmp:
    #    with io.open(tmp, mode='w', encoding='utf-8') as tmp2:
    #        tqdm_notebook.status_printer(tmp2, 101)
    #        tmp

# Generated at 2022-06-14 13:58:52.836616
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        for _ in tqdm_notebook(range(4)):  # tqdm_notebook(range(4), leave=True):
            pass
    except KeyboardInterrupt:
        pass



# Generated at 2022-06-14 13:59:00.053072
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Unit test for method status_printer of class tqdm_notebook"""
    from unittest import TestCase, main
    from tempfile import NamedTemporaryFile
    from copy import copy

    class Test(TestCase):
        def test_no_total(self):
            tqdm_notebook.status_printer(file=NamedTemporaryFile())

        def test_total(self):
            tqdm_notebook.status_printer(file=NamedTemporaryFile(), total=42)

        def test_total_desc(self):
            tqdm_notebook.status_printer(file=NamedTemporaryFile(),
                                         total=42, desc="test desc")


# Generated at 2022-06-14 13:59:11.360160
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .std import tqdm_notebook as tqdm; from platform import python_version
    from random import randint

    # IPython/Jupyter Notebook 4.x (dev)

# Generated at 2022-06-14 13:59:16.329565
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from types import GeneratorType
    # check a displayable widget is returned
    pbar = tqdm_notebook.status_printer(sys.stderr, 100, "Description")
    assert hasattr(pbar, '_repr_html_') or hasattr(pbar, '_repr_png_')
    # check a generator is returned
    pbar = tqdm_notebook.status_printer(sys.stderr)
    assert isinstance(pbar, GeneratorType)


if __name__ == '__main__':  # pragma: no cover
    question = "Do you want to run the test of the module `tqdm.notebook`?"
    if IPY >= 3 and input(question).strip().lower() in ['y', 'yes']:
        test_tqdm_notebook_status_

# Generated at 2022-06-14 13:59:21.970939
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """Test tqdm_notebook class display method"""

    def _test():
        yield 1
        yield 2
        raise ValueError()
        yield 3

    it = _test()

    t = tqdm_notebook(it)
    try:
        while True:
            next(t)
    except ValueError:
        import traceback
        traceback.print_exc()  # NOQA
    else:
        raise ValueError("should have raised!")


if __name__ == '__main__':
    test_tqdm_notebook_display()
    from .main import main
    main()

# Generated at 2022-06-14 13:59:26.352282
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    import time
    from random import random
    with tqdm_notebook(total=1000) as t:
        for _ in t:
            t.set_description('Testing desc')
            t.set_postfix(loss=random() ** 2)
            time.sleep(0.01)



# Generated at 2022-06-14 13:59:30.248651
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from inspect import isgeneratorfunction
    assert isgeneratorfunction(tqdm_notebook.__iter__)


if __name__ == "__main__":
    from ._utils import _test_argparse  # noqa: F401
    from ._tqdm import _test as _test_tqdm  # noqa: F401
    from ._tqdm_gui import _test as _test_tqdm_gui  # noqa: F401

# Generated at 2022-06-14 13:59:38.913619
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from random import random
    from time import sleep

    # Test with `disable` as False and True
    for disable in [False, True]:
        # Test widget with `total` known (`total` must not be None here)
        with tqdm_notebook(total=10000, disable=disable) as pbar:
            # Test widget with `total` unknown (`total` must be None here)
            for i in pbar:
                sleep(random() * 1e-2)
                pbar.display(str(i), i)
                if i == 100:
                    break

        # Test with `total` known (`total` must not be None here)

# Generated at 2022-06-14 14:00:08.250483
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from os import getpid
    from time import sleep
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    clear_str = "".join(["\r"] + [" "] * 100 + ["\r"])
    with std_tqdm(total=10, miniters=1, mininterval=0,
                  # file=StringIO(),  # Python2 is broken...
                  file=StringIO() if sys.version_info >= (3, 0) else sys.stderr,
                  dynamic_ncols=True) as t:
        for _ in t:
            # if getpid() != t_pid:
            #     t.close()
            t.clear()
            # t._instances.clear()  # for Python2.7

# Generated at 2022-06-14 14:00:12.132255
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    """
    Unit test for method clear of class tqdm_notebook
    """
    with tqdm_notebook(total=1, leave=True) as t:
        assert t.n == 0
        t.clear()
        assert t.n == 0



# Generated at 2022-06-14 14:00:20.779518
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for method reset of class tqdm_notebook.
    """
    if IProgress is None:
        raise SkipTest("IPython >= 3 or ipywidgets >= 7 required")

    from .utils import format_sizeof
    from .gui import tqdm_gui
    # Test for infos in bar
    for obj in [tqdm(total=1000,
                     bar_format='{desc}:{bar}'),
                tqdm(total=1000,
                     bar_format='{postfix[0]}:{bar}')]:
        with obj:
            obj.set_description("Description")
            obj.set_postfix_str("Postfix", refresh=False)
            obj.update(500)
        # Check bar is still visible
        assert obj.container.visible

# Generated at 2022-06-14 14:00:30.783620
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from tempfile import TemporaryFile
    from .utils import _term_move_up
    with TemporaryFile('w+') as fp:
        tqdm_notebook.status_printer(fp)
        fp.seek(0)
        assert fp.read() == '0.00%|          | 0/?' + _term_move_up()
        fp.seek(0)
        tqdm_notebook.status_printer(fp, total=1)
        fp.seek(0)
        assert fp.read() == '0.00%|          | 0/1' + _term_move_up()
        fp.seek(0)
        tqdm_notebook.status_printer(fp, total=2, ncols=32)
        fp.seek(0)

# Generated at 2022-06-14 14:00:38.863629
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Check if HTML text is correctly updated by status_printer"""
    c = tqdm_notebook.status_printer(total=10, desc='Description:')
    ltext, pbar, rtext = c.children
    assert ltext.value == 'Description:'
    assert pbar.bar_style == ''
    assert rtext.value == '  0%|                                       |'
    pbar.value = 1
    assert ltext.value == 'Description:'
    assert pbar.bar_style == ''
    assert rtext.value == ' 10%|########                              |'
    pbar.value = 2
    assert ltext.value == 'Description:'
    assert pbar.bar_style == ''
    assert rtext.value == ' 20%|############                          |'
    pbar.value = 3

# Generated at 2022-06-14 14:00:46.568155
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from .tests import tests

    with tests.capture_output() as (out, _):
        t = tqdm_notebook(total=10, file=out)
        # shouldn't print anything
        t.update(0)
        # should update every second iteration
        for i in range(10):
            t.update(1) if i % 2 else t.update(0)
        t.close()



# Generated at 2022-06-14 14:00:56.193169
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for method display of class tqdm_notebook.
    """
    from time import sleep
    from IPython.core.display import clear_output
    from IPython.display import HTML
    tqdm_notebook.clear()  # reset config
    bar = tqdm_notebook(total=3, bar_format='{l_bar}{bar:5.5}{r_bar}')
    for _ in range(3):
        for msg in ('', 'Msg', 'Msg1|<bar/>Msg2', 'Msg1|<bar/>Msg2|'):
            bar.display(msg=msg)
            sleep(0.2)
        bar.update()
    bar.close()
    bar.container.close()

# Generated at 2022-06-14 14:01:03.867776
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from nose.tools import assert_equal
    from time import sleep
    from tqdm import tqdm
    from tqdm.utils import _term_move_up

    for leave in [False, True]:
        for disable in [False, True]:
            for iterable in [tqdm(range(5), leave=leave),
                             tqdm(range(5), leave=leave,
                                  disable=disable)]:
                with iterable as it:
                    # Assert __iter__() returns self
                    assert_equal(it, iter(it))
                    # Assert print() prints to stdout
                    print("Dummy text")
                    # Assert progressbar is displayed and updated
                    assert not it.disable
                    assert not it.displayed
                    iterable.__iter__()
                    assert it.displayed
                    # Assert

# Generated at 2022-06-14 14:01:15.833257
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep
    with tqdm_notebook(total=5) as t:
        for i in range(5):
            sleep(.5)
            t.set_description("Processing %i" % i)
            t.update()
    # Test class construction
    for n in (1, 3):
        with tqdm_notebook(total=n, bar_format="{l_bar}{bar}{r_bar}",
                desc="testing widget display", leave=True) as t:
            assert (len(t) == n)
            for i in range(n):
                t.update()
    # Test bar style change
    t = tqdm_notebook(total=3, bar_format="{l_bar}{bar}{r_bar}")
    t.update()
    t.clear()
   

# Generated at 2022-06-14 14:01:23.429554
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    import sys
    import io
    import os
    import time

    # pylint: disable=E0602
    if os.name == 'nt':  # pragma: no cover
        import msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

    def get_fp(file):
        if IPY:
            return file
        # The following is necessary as we're in a IPython Notebook cell
        return io.StringIO()

    fp = get_fp(sys.stderr)

    # Prevent tqdm from using tqdm-specific newline= argument
    # to print_function

# Generated at 2022-06-14 14:01:50.382328
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    # Issue #959
    x = tqdm_notebook(range(10))
    x.reset(total=10)
    # Issue #977
    x.reset(total=20)
    x.reset(total=30)


# Generated at 2022-06-14 14:01:53.893747
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    t = tqdm_notebook(range(1), desc='test_tqdm_notebook_reset')
    t.display()
    t.reset(5)
    t.reset(5)
    assert t.total == 5
    t.reset()
    assert t.total == None


# Generated at 2022-06-14 14:02:06.730474
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep

    for total in [None, 50]:
        t = tqdm_notebook(total=total)
        for i in range(10):
            sleep(0.1)
            t.update()
        for i in range(10):
            sleep(0.1)
            t.update()
        # test reset with unknown total
        t.reset()
        t.reset(total=100)
        t.reset()
        # test reset with known total
        t.reset(total=50)
        t.reset()
        t.reset(total=100)
        # test reset in manual mode
        t.n = 0
        t.total = None
        t.reset()
        t.reset(total=100)
        t.reset()
        t.reset(total=50)
        t.close

# Generated at 2022-06-14 14:02:09.303872
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from random import random
    from tqdm import tnrange, trange

    tqdm_range = tnrange if IPY else trange
    tqdm_range = tqdm_range(10)
    for _ in tqdm_range:
        # Do nothing
        if random() < 0.1:
            tqdm_range.reset()



# Generated at 2022-06-14 14:02:14.736816
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from shutil import get_terminal_size
    for t in [get_terminal_size(0).columns-3, _range(100, 200)]:
        with tqdm_notebook(total=t) as tbar:
            for i in _range(10):
                tbar.update(10)
                tbar.reset(t+20)


if __name__ == "__main__":
    # Run main test function
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:02:23.815063
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from sys import version_info
    from io import StringIO
    from IPython.core.display import display
    from IPython.core.display import clear_output
    from time import sleep

    # We clear the notebook output
    clear_output()

    # We create a progress bar
    with StringIO() as f:
        pbar = tqdm_notebook(total=100, file=f)
        pbar.start()

        # We update the progress bar
        for i in range(7):
            pbar.update(10)
            sleep(0.1)

        # We check that the bar is properly closed
        pbar.close()
        assert '\r' not in f.getvalue()

    # We create a progress bar

# Generated at 2022-06-14 14:02:32.779438
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    print("testing tqdm_notebook()")
    try:
        from jupyter_client.manager import start_new_kernel
    except ImportError:
        return
    kernel_name = 'python3' if sys.version_info[0] >= 3 else 'python2'
    start_new_kernel(kernel_name=kernel_name)
    time.sleep(0.2)
    x = list(tqdm_notebook(range(10), desc='testing'))
    assert x == list(range(10))
    try:  # pragma: no cover
        from IPython.display import clear_output
        clear_output()
    except ImportError:  # pragma: no cover
        pass
    print("successful")

if __name__ == "__main__":  # pragma: no cover
    test

# Generated at 2022-06-14 14:02:42.914965
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    try:
        from IPython.display import clear_output
    except ImportError:
        return False
    else:
        with tqdm_notebook(total=10) as pbar:
            assert (repr(pbar) ==
                    "<widget>\n"
                    "<div>\n"
                    "  <style scoped>\n"
                    "    progress {\n"
                    "      width: 100%;\n"
                    "    }\n"
                    "  </style>\n"
                    "</div>\n"
                    "<progress class=\"widget-progress\" />")
            for i in _range(10):
                pbar.update()

# Generated at 2022-06-14 14:02:45.439739
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from tqdm.auto import trange
    for _ in trange(2):
        for i in trange(2):
            assert i in {0, 1}



# Generated at 2022-06-14 14:02:51.090255
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    tqdm_notebook.status_printer(None, total=1, desc="desc", ncols=10)
    tqdm_notebook.status_printer(None, total=1, desc="desc")
    tqdm_notebook.status_printer(None, total=1)
    tqdm_notebook.status_printer(None)
    try:  # coverage of if-else-branches above
        IProgress = None
        tqdm_notebook.status_printer(None)
    except ImportError:
        pass

# Generated at 2022-06-14 14:03:42.979718
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=1, leave=False) as bar:
        bar.update()
        bar.clear()
        bar.close()


if __name__ == '__main__':
    # Create example progressbar without a total
    pbars = [tqdm_notebook(['a', 'b', 'c']), tqdm_notebook(['d', 'e', 'f'])]

    # Display progressbars
    display(pbars[0])
    display(pbars[1])

    # Iterate over progress bars
    for pbar in pbars:
        for char in pbar:
            pbar.set_description("Processing %s" % char)
            pbar.update()
            time.sleep(0.1)

        # Manually close the progressbar
        pbar.close

# Generated at 2022-06-14 14:03:48.323542
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from sys import stdout
    from time import sleep
    from tqdm import tqdm

    if 'IPython' not in sys.modules:
        return None

    with closing(stdout):
        for _ in tqdm(range(10), file=stdout, leave=True, miniters=0, mininterval=0):
            sleep(0.1)



# Generated at 2022-06-14 14:03:56.101022
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Unit test for method status_printer of class tqdm_notebook
    """
    # 0 bars
    pbar = tqdm_notebook.status_printer(None)
    pbar_dict = pbar._repr_json_()
    assert pbar_dict['ascii'] is False

    # 1 bar
    pbar = tqdm_notebook.status_printer(None, total=1)
    pbar_dict = pbar._repr_json_()
    assert pbar_dict['ascii'] is False
    assert pbar_dict['bar_format'] == '{l_bar}{bar}{r_bar}'
    assert pbar_dict['desc'] == ''
    assert pbar_dict['ncols'] == None
    assert pbar_dict['n'] == 0

# Generated at 2022-06-14 14:04:04.265210
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Unit test for method __iter__ of class tqdm_notebook
    (Test for tqdm_notebook.__iter__())
    """
    from time import sleep
    from numpy.random import uniform
    from numpy import arange

    for _ in tqdm_notebook(arange(10), desc='1st loop'):
        for _ in tqdm_notebook(arange(100), desc='2nd loop'):
            for _ in tqdm_notebook(arange(100), desc='3nd loop'):
                sleep(uniform(0.01, 0.1))



# Generated at 2022-06-14 14:04:13.149331
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from .gui import tqdm_gui
    from .utils import _term_move_up
    tqdm_notebook.status_printer(
        tqdm_gui(), total=10, desc="Desc ", ncols=10)
    tqdm_notebook.status_printer(
        tqdm_gui(), total=10, desc="Desc ", ncols=None)
    tqdm_notebook.status_printer(
        tqdm_gui(), total=10, desc="Desc ", ncols="100px")


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 14:04:20.372028
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    from io import StringIO
    from .std import tqdm
    from .utils import _range

    with StringIO() as f:
        for _ in tqdm(_range(10), file=f):
            pass

    if sys.version_info >= (3, 3):
        from unittest.mock import patch, MagicMock

        with patch('tqdm.notebook.HTML', autospec=True) as m, \
                patch('tqdm.notebook.IProgress', autospec=True) as p, \
                patch('tqdm.notebook.HBox', autospec=True) as o:
            HTML, IProgress, HBox = m, p, o
            HTML.return_value = True
            IProgress.return_value = True
            HBox.return_value = True
            ltext, p

# Generated at 2022-06-14 14:04:33.373100
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    if IProgress is None:  # #187 #451 #558 #872
        raise ImportError(
            "IProgress not found. Please update jupyter and ipywidgets."
            " See https://ipywidgets.readthedocs.io/en/stable/user_install.html")
    from sys import version_info
    from .std import PY3
    if PY3:
        from io import StringIO
    else:
        from StringIO import StringIO
    fp = StringIO()

    # Test case params and expected outputs

# Generated at 2022-06-14 14:04:40.632319
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for method display of class tqdm_notebook
    """
    from .utils import _supports_unicode  # NOQA
    from .std import tqdm as _tqdm
    from ._monitor import _get_free_space as _gfs

    desc = ['\u30B3', '\u4E01'] if _supports_unicode() else '01'
    for fd in (sys.stdout, None):
        for ascii in (True, False):
            try:  # redirect stdout to stdout (to check we don't print)
                from StringIO import StringIO
                buf = StringIO()
            except ImportError:
                from io import StringIO
                buf = StringIO()

# Generated at 2022-06-14 14:04:50.652390
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from IPython.display import clear_output
    from io import StringIO
    import time
    import sys

    out = StringIO()

    # Empty bar
    tqdm_notebook(leave=True, file=out)

    pbar = trange(3, file=out, desc='foo', ncols=100, disable=False)
    for i in pbar:
        time.sleep(0.01)
        pbar.set_description('bar %i' % i)
        pbar.refresh()
    print('\n', file=sys.stderr)

    # pbar.set_description_str('blah')  # Deprecated
    pbar.set_description('blah')

    pbar.close()


# Generated at 2022-06-14 14:04:56.525857
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from IPython.display import clear_output
    class FakeDisplay():
        def __init__(self):
            self.display_calls = []
    fake_display = FakeDisplay()
    def fake_display_func(*args, **kwargs):
        fake_display.display_calls.append((args, kwargs))
    old_display = tqdm_notebook.display
    tqdm_notebook.display = fake_display_func
    bar = tqdm_notebook(total=5)
    assert(False == bar.displayed)
    bar.update()
    bar.update()
    bar.update()
    assert(5 == len(fake_display.display_calls))
    assert(False == bar.displayed)
    tqdm_notebook.display = old_display
    tqdm

# Generated at 2022-06-14 14:06:25.696675
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from shutil import rmtree
    from tempfile import mkdtemp
    try:
        tmpdir = mkdtemp()
        progress = tqdm_notebook(total=100)
        for __ in progress:
            rmtree(tmpdir)
    except Exception:
        pass


if __name__ == "__main__":
    test_tqdm_notebook___iter__()

# Generated at 2022-06-14 14:06:33.231624
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    import warnings
    from tqdm.auto import tqdm as _tqdm

    with warnings.catch_warnings(record=True) as w:
        pt = _tqdm(total=10)
        pt.display()
        # Warning format changed in v5.1.0
        assert str(w[-1].message).endswith(
            "`tqdm_notebook` display was not set! Please set it manually"
            " (see https://github.com/tqdm/tqdm#ipython-jupyter-integration)"
            "\n  warnings.warn(TqdmDeprecationWarning(...))")
        pt.display('')
        pt.display('Hello World!')
        pt.display('Hello <b>World</b>!', "Left", "Right", True)


# Generated at 2022-06-14 14:06:35.350533
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    for _ in tqdm_notebook(range(100), desc="test tqdm_notebook"):
        pass

# Generated at 2022-06-14 14:06:44.772336
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from tqdm import _tqdm, format_interval, format_meter
    from tqdm.contrib import DummyTqdmFile, DummyContainterWidgetClass

    t = tqdm(total=13, desc="testing tqdm_notebook.display")
    assert t.container.children == DummyContainterWidgetClass().children

    t.display(desc="bar_desc", pos=None,
              close=False, bar_style=None, check_delay=True)
    assert t.container.children[0].value == "bar_desc"

    t.display(desc="bar_desc", pos=None,
              close=False, bar_style=None, check_delay=True)

# Generated at 2022-06-14 14:06:54.537778
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import numbers
    from .std import tqdm as std_tqdm
    from .std import trange as std_trange

    for t in [tqdm_notebook, tnrange]:
        # Fallback to text bar if there's no total
        # DEPRECATED: replaced with an 'info' style bar
        # h = [t.status_printer(None) for _ in std_trange(3)]
        # assert h == [None, None, None]

        # Get a progress bar
        t.status_printer(None, 3)
        h = [t.status_printer(None, 3, "desc" + str(i))
             for i in std_trange(3)]

        # Check types
        assert len(h) == 3

# Generated at 2022-06-14 14:07:05.683939
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from tqdm.auto import trange
    import inspect

    t = trange(10, desc='test iter')
    yield lambda: t.__next__() is None
    yield lambda: inspect.isgenerator(t.__iter__()) is True
    t.close()


if __name__ == "__main__":
    # Unit test
    from tqdm.auto import tqdm as auto_tqdm

    def helper_test_tqdm_notebook_display():
        t = auto_tqdm([], file=sys.stdout)
        t.display()

    def helper_test_tqdm_notebook_width():
        ipywidgets.FloatProgress(layout=dict(width='10%'))
        ipywidgets.FloatProgress(layout=dict(width='10px'))

   

# Generated at 2022-06-14 14:07:15.013985
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import unittest
    import shutil
    from test.python import TestCase
    from tqdm.notebook import tqdm_notebook

    class Tests(TestCase):
        def test_status_printer(self):

            class Pbar:
                def __init__(self):
                    self.n = 0
                    self.total = 3

            pbar = Pbar()
            status_printer = tqdm_notebook.status_printer(
                file=None, total=pbar.total)

            status_printer(pbar)
            ltext, pbar2, rtext = status_printer.children
            self.assertEqual(str(pbar2), '0%|          | 0/3 [00:00<?, ?it/s]')

            pbar.n = 1
            status_

# Generated at 2022-06-14 14:07:19.842921
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Test the `reset` method of `tqdm_notebook.tqdm` to validate that it
    updates the progress bar when called recursively.
    """
    try:
        for _ in range(3):
            for i in tqdm_notebook(range(1000)):
                if i == 100:
                    break
            tqdm_notebook.reset(total=1000)
    except:  # NOQA
        pass

# Generated at 2022-06-14 14:07:22.124383
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .tests import test_notebook
    test_notebook.test_tqdm_notebook___iter__(tqdm_notebook, __name__)


# Generated at 2022-06-14 14:07:23.997205
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    t = tqdm_notebook(total=5)
    for i in range(10):
        t.update()
    t.close()