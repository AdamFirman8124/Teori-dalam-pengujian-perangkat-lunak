

# Generated at 2022-06-14 13:58:10.294521
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import sys
    from io import StringIO
    from time import sleep

    class Capturing(list):
        """
        Context manager for capturing standard output or another stream.

        Code forked from https://stackoverflow.com/a/16571630/353337
        """
        def __init__(self, stream=None):
            self._stream = stream or sys.stdout
            self._stdout = sys.stdout
            self._stderr = sys.stderr
            sys.stdout = self._stringio = StringIO()
            sys.stderr = self._stringio

        def __enter__(self):
            return self

        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            sys.stdout = self._stdout
            sys

# Generated at 2022-06-14 13:58:16.415726
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    assert str(TqdmHBox([])) == 'HBox()'

    pbar = IProgress()
    container = TqdmHBox(children=[HTML(), pbar, HTML()], pbar=proxy(pbar))
    pbar.value = 123
    pbar.bar_style = 'info'
    container.layout.width = '100px'
    assert str(container) == 'HBox(layout=Layout(width=\'100px\', height=\'30px\'),\n' \
                             '    children=(HTML(), FloatProgress(value=0.0, description=\'\', ' \
                             'max=100.0, style=ProgressStyle(description_width=\'initial\')), HTML()))'

# Generated at 2022-06-14 13:58:27.097055
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    base_cls = tqdm_notebook if IPY else object

    class BaseTester(base_cls):
        @staticmethod
        def status_printer(*args, **kwargs):  # pragma: no cover
            return super(BaseTester, BaseTester).status_printer(*args, **kwargs)

    desc = 'testing'
    t = BaseTester(total=2, desc=desc)
    container = t.status_printer(t.fp, t.total, t.desc)

    assert container is not None
    assert all(hasattr(x, "value") for x in container.children)

    # REPLICATE
    # ltext = HTML(desc)
    # rtext = HTML()
    # pbar = IProgress(min=0, max=t.total)
    # if

# Generated at 2022-06-14 13:58:33.945169
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import sys
    for file in (sys.stderr, sys.stdout):
        for ncols in (None, '100%', '20px'):
            with tqdm(total=100, file=file, ncols=ncols) as pbar:
                assert pbar._instances
                pbar.clear()

if __name__ == '__main__':
    test_tqdm_notebook_clear()

# Generated at 2022-06-14 13:58:43.583697
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        # pylint: disable=unused-variable
        from ipykernel.tests.test_ipkernel import IPyKernelTestCase

        class mock_IPyKernelTestCase(IPyKernelTestCase):
            @staticmethod
            def clear_output():
                pass

        # pylint: disable=unused-variable
        class TqdmNotebookClearTest(mock_IPyKernelTestCase):
            def test_clearing_tqdm_notebook(self):
                from tqdm.notebook import tqdm

                for _ in tqdm(range(8), disable=True):
                    # pylint: disable=protected-access
                    tqdm._instances.clear()
    except ImportError:
        pass
    except NameError:
        pass

# Generated at 2022-06-14 13:58:54.164766
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    with tqdm_notebook(total=100,
                       desc='desc',
                       bar_format='{postfix}|{bar}|{n_fmt}/{total_fmt}',
                       postfix=dict(loss=5.6, acc=6.7, epoch=1)) as t:
        for i in range(10):
            assert not t.displayed
            t.update(9)
            assert t.displayed
            tmp = t.format_dict.copy()
            tmp['bar'] = None
            tmp['postfix'] = {'epoch': 1,
                              'loss': '{0:.2f}'.format(5.6),
                              'acc': '{0:.2f}'.format(6.7)}
            tmp['n'] = t.n
            tmp['total']

# Generated at 2022-06-14 13:59:05.440072
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # Setup fake stdin/stdout tqdm and check it's working
    class fake_stream(object):
        def __init__(self):
            self.buf = ''

        def write(self, s):
            self.buf += s.strip()

    f = fake_stream()
    tqdm_test = tqdm_notebook(total=None, file=f)

    # Setup fake IPython/Jupyter Notebook stdin/stdout
    class fake_ipython_stream(object):
        def __init__(self):
            self.buf = ''

        def write(self, s):
            self.buf += s.strip()

        def flush(self):
            pass

    i = fake_ipython_stream()
    sys.stdout = i
    tqdm_test.status_printer

# Generated at 2022-06-14 13:59:13.049151
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Tests update, close, display methods of class tqdm_notebook.
    Tests that manually-closed bars can be re-opened.
    """
    import platform
    import os
    import time
    import signal

    def signal_handler(signum, frame):
        """
        Force termination of program.
        """
        if platform.system() == "Windows":
            os.kill(os.getpid(), signal.SIGINT)
        else:
            os.kill(os.getpid(), signal.SIGTERM)

    from .tests import pretest_posttest

    with pretest_posttest(False):
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)


# Generated at 2022-06-14 13:59:21.051305
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Unit test for method status_printer of class tqdm_notebook.
    Also test for method _repr_json_ of class TqdmHBox,
    method _repr_pretty_ of class TqdmHBox.
    """
    from collections import defaultdict
    from io import StringIO
    from json import dumps, loads
    from sys import version_info
    from IPython.display import HTML, JSON, Javascript, display

    ltext = HTML()
    rtext = HTML()
    pbar = IProgress(min=0, max=1)
    pbar.bar_style = 'info'
    container = TqdmHBox(children=[ltext, pbar, rtext])

    # test json
    # normal case
    pbar.value = 0.5
    ltext.value = "a"

# Generated at 2022-06-14 13:59:31.250505
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """Smoke test to check that tqdm_notebook.display can be called"""
    try:
        import ipywidgets
    except ImportError:
        pass  # ok

    try:
        from IPython.html.widgets import HTML
    except ImportError:
        HTML = object  # ok

    # test on trivial case that cannot fail
    try:
        bar = tqdm_notebook(total=1, desc="testing")
        bar.display()
        assert isinstance(bar.container.children[0], HTML)
        # assert isinstance(bar.container, HBox)
    except ImportError:
        pass  # ok


# Tests
if __name__ == '__main__':
    test_tqdm_notebook_display()

# Generated at 2022-06-14 13:59:54.959112
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test tqdm_notebook.status_printer
    """
    # Initial setup
    if IPY == 0:  # pragma: no cover
        return  # Test requires IPython/Jupyter
    try:
        from IPython.display import clear_output
    except ImportError:
        return
    from contextlib import contextmanager
    from io import StringIO
    from time import sleep

    # Define helper functions
    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.std

# Generated at 2022-06-14 13:59:56.308297
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    """ Clear progressbar in notebook"""
    assert True


# Generated at 2022-06-14 14:00:02.536510
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        display
    except NameError:
        raise ImportError("IPython/Jupyter notebook not found, skipping...")

    x = tqdm_notebook(iter([1]))
    assert next(x) == 1
    assert x.n == 1
    try:
        next(x)
        assert False  # NOTREACHED
    except StopIteration:
        assert x.n == 1



# Generated at 2022-06-14 14:00:04.177112
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    tqdm_notebook(["a", "b", "c"]).__iter__()



# Generated at 2022-06-14 14:00:11.601546
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for method `display` of class `tqdm_notebook`.
    """
    from itertools import chain
    try:
        # Jupyter/IPython 4.x/5.x (notebook) tested on Linux and MacOS
        from IPython.display import clear_output, HTML
        ipy_major_minor = "{}.{}".format(*map(int, IPython.__version__.split('.')[:2]))
    except ImportError:
        # IPython 3.x tested on Linux
        from IPython.html.widgets import HTML, ContainerWidget
        ipy_major_minor = "{}".format(*map(int, IPython.__version__.split('.')[:1]))

# Generated at 2022-06-14 14:00:20.119230
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep
    with tqdm_notebook(total=5) as pbar:
        for i in range(5):
            pbar.set_description('description %d' % (i + 1))
            pbar.update()
            sleep(0.1)
        pbar.display(close=True)


if __name__ == "__main__":
    try:
        import unittest
        from .tests import TqdmNotebookTest
        suite = unittest.TestLoader().loadTestsFromTestCase(TqdmNotebookTest)
        # run the tests that are not in TqdmTest
        for test in suite:
            test.runTest(test)
    except:  # pragma: no cover
        test_tqdm_notebook_display()

# Generated at 2022-06-14 14:00:27.572759
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Tests whether method iter of class tqdm_notebook works
    """
    from .utils import _test_iter_with_breakpoint
    return _test_iter_with_breakpoint(
        tqdm_notebook(total=2, leave=True, desc='Testing tqdm_notebook...',
                      position=0, postfix={"ascii": True, "eta": True},
                      disable=False, mininterval=0.1, miniters=None,
                      file=sys.stdout, gui=True))



# Generated at 2022-06-14 14:00:34.845572
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    """test_tqdm_notebook_clear"""
    import time
    import logging
    from .utils import format_sizeof
    from .utils import format_interval
    try:
        from pandas import DataFrame
    except ImportError:
        DataFrame = None

    # Ignore warnings from notebook
    logging.getLogger("notebook").setLevel(logging.ERROR)

    # Wait for Notebook to load
    time.sleep(1)

    # Initial test
    with tqdm(total=2, leave=True) as pbar1:
        pbar1.set_description("Test 1")
        pbar1.update(1)
        pbar1.update(1)

    # Prepare test2
    islice = iter(tqdm(_range(10000), ascii=True, leave=True))


# Generated at 2022-06-14 14:00:38.663312
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # Initialize variables
    iterator = range(10)

    # Initialize tqdm_notebook
    actual = tqdm_notebook(iterator)

    # Assert type
    assert isinstance(actual, tqdm_notebook)

    # Assert iterator
    assert list(actual) == iterator

    # Close tqdm_notebook
    actual.close()



# Generated at 2022-06-14 14:00:51.163682
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Test the function `tqdm_notebook.status_printer`"""
    hbox = TqdmHBox([])
    ipbar = IProgress()
    hbox.children = [HTML(), ipbar, HTML()]
    hbox.pbar = ipbar

    pbar = tqdm_notebook(total=0)
    pbar.container = hbox

    print("-- Text only, no total --")
    msg = pbar.format_meter()
    pbar.container.pbar = None  # avoid printing the bar
    print(msg, pbar.container)
    # avoid printing the bar
    hbox.pbar = None

    print("-- Progress bar, unknown total --")
    pbar = tqdm_notebook("Custom message")
    pbar.container.pbar = None  # avoid printing

# Generated at 2022-06-14 14:01:16.613709
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import sys
    import re
    if sys.version_info[0] >= 3:
        _range = range
    else:
        _range = xrange

    # Test 1
    progress = tqdm_notebook.status_printer(
        file=sys.stdout, total=10, desc="Test 1", ncols=150)
    for i in _range(10):
        progress.value = i

    # Test 2
    progress = tqdm_notebook.status_printer(
        file=sys.stdout, total=10, desc="Test 2", ncols="50%")
    for i in _range(10):
        progress.value = i

    # Test 3

# Generated at 2022-06-14 14:01:23.810151
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for method reset of tqdm_notebook
    """
    try:
        from IPython.testing.globalipapp import get_ipython
        ipy = get_ipython()
        if ipy is None:  # pragma: no cover
            raise ImportError("IPython could not be found")
    except ImportError:  # pragma: no cover
        return

    from IPython.utils.capture import capture_output
    # Should not raise an exception
    with capture_output(stdout=False, stderr=False) as cap:
        pbar = tqdm_notebook(total=100)
        for i in range(10):
            pbar.update()
        pbar.reset()
        pbar.update()
        pbar.reset(total=3)
        pbar.close

# Generated at 2022-06-14 14:01:34.632752
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    Unit test for method `update` of class `tqdm_notebook`

    Test for the following scenarios:
      - [x] new: normal case
      - [x] new: tqdm_notebook instance with `disable`
      - [x] new: tqdm_notebook instance without `disable` but without gui
      - [x] old: normal case
      - [x] old: tqdm_notebook instance with `disable`
      - [x] old: tqdm_notebook instance without `disable` but without gui
      - [x] normal case with exception
      - [x] normal case with exception, tqdm_notebook instance with `disable`
      - [x] normal case with exception, tqdm_notebook instance without `disable`
      but without gui
    """
    # normal case


# Generated at 2022-06-14 14:01:43.946520
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .utils import FormatCustomTextTest, format_dicts

    for format_dict in format_dicts:
        with FormatCustomTextTest(format_dict["format"]):
            for iterable in [_range(4), "abcd"]:
                for i in tqdm(iterable, **format_dict):
                    pass


if __name__ == '__main__':
    # Just testing
    tqdm_notebook().display()

    # Unit tests
    test_tqdm_notebook___iter__()

    # Benchmark
    from timeit import timeit

# Generated at 2022-06-14 14:01:46.836227
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .tests import comparison_test_tqdm_cls_display
    comparison_test_tqdm_cls_display(tqdm_notebook)


# Generated at 2022-06-14 14:01:50.474296
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(total=10) as t:
        for _ in range(5):
            t.update()
    assert not t.container.visible

# Generated at 2022-06-14 14:01:55.808761
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    """Unit test for method __repr__ of class TqdmHBox"""
    import pytest
    # default arguments
    TqdmHBox.pbar = tqdm_notebook(total=1)
    assert repr(TqdmHBox()) == '|                                                                            | 0.00% '
    # with argument pretty = True
    assert repr(TqdmHBox()) == '{desc}{bar}|{percentage:6.2f}%{postfix}'.format(
        desc='',
        bar='|',
        percentage=0,
        postfix=' ')
    # with argument pretty = False
    assert repr(TqdmHBox()) == '|                                                                            | 0.00% '
    # overwrite argument pretty

# Generated at 2022-06-14 14:02:08.503211
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    try:
        import IPython.html as ipywidgets  # NOQA
        # TODO: ipywidgets import patch (see std.tqdm examples)
        ipywidgets = ipywidgets.widgets
    except ImportError:
        pass

    t = tqdm_notebook(total=10)
    try:
        for _ in t:
            pass
    except KeyboardInterrupt:
        pass
    assert getattr(t, "displayed", None) is True
    assert t.format_dict['bar_format'] == "{l_bar}<bar/>{r_bar}"

    for l in [False, True]:
        t = tqdm_notebook(total=10, leave=l)

# Generated at 2022-06-14 14:02:11.758652
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(desc="init") as _t:
        pass
    _t.close()
    with tqdm_notebook(desc="hello") as _t2:
        _t2.update()
        _t2.update(1)

# Generated at 2022-06-14 14:02:14.230142
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    for i in tqdm_notebook(range(10)):
        if i < 3:
            tqdm_notebook.clear(tqdm_notebook)
            time.sleep(1)
        time.sleep(1)

# Generated at 2022-06-14 14:02:37.792704
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    t = tqdm_notebook(total=None)
    assert t.displayed == False
    t.reset(total=100)
    assert t.displayed == True
    t.reset(total=0)
    assert t.displayed == True
    t.reset(total=None)
    assert t.displayed == True

    t.delay = 0
    t.reset(total=None)
    t.displayed = False
    t.update(1)
    assert t.displayed == True

    t.display = Mock()
    t.reset()
    t.display.assert_called_with(check_delay=False)
    t.update()

# Generated at 2022-06-14 14:02:47.581684
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    from random import randint
    with tqdm_notebook(range(10), desc='1st loop', leave=True) as it:
        for i in it:
            sleep(0.01)
        for i in it:
            # Test for reset in manual mode
            it.set_description("1st loop (reset %i)" % i)
            sleep(0.01)
        for i in it:
            # Test for reset in automaticmode
            it.reset(total=10)
            it.set_description("1st loop (reset %i)" % i)
            sleep(0.01)
            if i == 1:
                # Test for close
                it.close()
                break

# Generated at 2022-06-14 14:02:58.523127
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Unit tests for method status_printer of class tqdm_notebook
    """
    assert tqdm_notebook.status_printer(None, total=None, desc=None, ncols=None)
    assert tqdm_notebook.status_printer(None, total=None, desc=None, ncols="100%")
    assert tqdm_notebook.status_printer(None, total=None, desc=None, ncols="100px")
    assert tqdm_notebook.status_printer(None, total=None, desc=None, ncols="100")
    assert tqdm_notebook.status_printer(None, total=None, desc=None, ncols=100)


# Allow running tests with "python tqdm/notebook.py"


# Generated at 2022-06-14 14:03:04.980693
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Unit test for method __iter__ of class tqdm_notebook.
    It is also a very basic usage example.
    """
    # Suppress TqdmExperimentalWarning
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=TqdmExperimentalWarning)

        total = 100
        t = tqdm_notebook(total=total)
        for i in t:
            pass
        assert t.n == total



# Generated at 2022-06-14 14:03:09.741053
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    from .tests import SetupTests, test_TqdmHBox___repr___content, tu
    # Run standard tests
    SetupTests.set_up()
    SetupTests.test_tqdm(tu)
    # Run method tests
    test_TqdmHBox___repr___content()

# Generated at 2022-06-14 14:03:20.966050
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    from tqdm.notebook import tqdm_notebook, display
    with patch.object(tqdm_notebook, 'status_printer') as mock_status_printer, \
            patch.object(tqdm_notebook, 'display', autospec=True) as mock_display:
        mock_status_printer.return_value = i_progress = object()
        mock_display.return_value = display_return_val = object()

        t = tqdm_notebook(total=5, desc='x')
        t.display(msg='test')

# Generated at 2022-06-14 14:03:30.818473
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    def test_printer(arg, total, ncols=None):
        if ncols is not None:
            return tqdm_notebook.status_printer(arg, total, ncols=ncols)
        else:
            return tqdm_notebook.status_printer(arg, total)

    from nose.tools import assert_equal
    assert_equal(test_printer(1, 1).layout.flex, '2')
    assert_equal(test_printer(1, 1, ncols='10%').layout.flex, '2')
    assert_equal(test_printer(1, 1, ncols='50%').layout.flex, '2')
    assert_equal(test_printer(1, 1, ncols='100%').layout.flex, '2')

# Generated at 2022-06-14 14:03:42.197966
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from copy import copy
    from IPython.utils.capture import capture_output
    from contextlib import contextmanager
    from io import StringIO

    @contextmanager
    def capture_stdout():
        sys.stdout = StringIO()
        yield
        sys.stdout = sys.__stdout__

    for __ in tqdm_notebook(list(range(1)), desc="Error?"):
        raise ValueError

    with capture_stdout():
        for __ in tqdm_notebook(list(range(1)), desc="Error?"):
            raise ValueError

    for __ in tqdm_notebook(list(range(1)), desc="Success?"):
        pass

    with capture_stdout():
        for __ in tqdm_notebook(list(range(1)), desc="Success?"):
            pass

   

# Generated at 2022-06-14 14:03:52.125920
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    import sys
    from tqdm.utils import _term_move_up
    from .utils import _range

    # Inits
    kwargs = dict(desc="Class test", leave=True, ascii=True,
                  file=sys.stderr)
    for total, dynamic_ncols, unit_scale in [
            (5, False, 1),
            (5, False, True),
            (5, True, 1),
            (5, True, True),
            (None, False, 1),
            (None, False, True),
            (None, True, 1),
            (None, True, True),
    ]:
        kwargs['total'] = total
        kwargs['dynamic_ncols'] = dynamic_ncols
        kwargs['unit_scale'] = unit_scale

# Generated at 2022-06-14 14:04:03.779526
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import sys
    if IPY < 4:
        if IProgress is None:
            raise ImportError(
                "IProgress not found. Please update jupyter and ipywidgets."
                " See https://ipywidgets.readthedocs.io/en/stable"
                "/user_install.html")

    if IPY == 0:
        raise ImportError("Could not import ipywidgets. Please install it.")

    total = 10
    #file = sys.stdout

    pbar = tqdm_notebook.status_printer(sys.stdout, total, "test")
    assert len(pbar.children) == 3
    pbar, left, right = pbar.children

    assert isinstance(pbar, IProgress)
    assert pbar.min == 0
    assert pbar.max == total

# Generated at 2022-06-14 14:05:07.726098
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """Tests both the update() and close() methods"""
    # On python 2, catching all exceptions including KeyboardInterrupt
    # needs to be done in a `except Exception, e` syntax as
    # `except KeyboardInterrupt as e` only catches SyntaxError.
    # See https://stackoverflow.com/questions/12894457/why-doesnt-python-catch-keyboardinterrupt-as-e
    # Note:
    # - We need to make the exception a global variable,
    #   so it doesn't get garbage collected when leaving the `with` block.
    #   See https://stackoverflow.com/questions/25818715/how-to-correctly-use-sys-exc-info-in-python
    # - The `as e` syntax is being used as much as possible
    #   to avoid breaking `

# Generated at 2022-06-14 14:05:17.763447
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # Default values
    container = tqdm_notebook.status_printer(_total=None)
    assert container.children[0].value == ''
    assert container.children[1].value == 0
    assert container.children[2].value == ''

    # 100% bar
    container = tqdm_notebook.status_printer(_total=None, _desc='test')
    assert container.children[0].value == 'test'
    assert container.children[1].value == 0
    assert container.children[2].value == '100%'

    # 100% bar with ncols
    container = tqdm_notebook.status_printer(
        _total=None, _desc='test', _ncols='100%')
    assert container.children[0].value == 'test'

# Generated at 2022-06-14 14:05:26.186377
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from .utils import format_dict, _decr_instances

    text_to_test = 'Hello World!'
    width_to_test = "40%"
    tqdm_notebook.status_printer(None, total=None, desc=text_to_test,
                                 ncols=width_to_test)

    # Test description display
    d = format_dict({}, text_to_test, 0, 0, 'desc')
    tqdm_notebook.status_printer(None, total=None, desc=d['desc'],
                                 ncols=width_to_test)
    # Test info style
    tqdm_notebook.status_printer(None, total=None, desc=d['desc'],
                                 ncols=width_to_test)



# Generated at 2022-06-14 14:05:28.591679
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    container = TqdmHBox(children=[None, None, None])
    container.pbar = tqdm_notebook(desc='tqdm_notebook')
    print(repr(container))


if __name__ == '__main__':
    test_TqdmHBox___repr__()

# Generated at 2022-06-14 14:05:34.532390
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from IPython.display import clear_output

    with tqdm_notebook(total=100) as bar:
        for i in range(10):
            bar.update()
            if i == 5:
                bar.reset(total=50)
            clear_output(wait=True)

if __name__ == '__main__':  # pragma: no cover
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:05:44.114744
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from sys import stdout as fp
    from tqdm.notebook import tqdm_notebook
    # sys.stderr = fp = io.StringIO()
    t = tqdm_notebook(total=2)
    # Note: manual tqdm() will not catch exception
    # def f():
    #    [][0]
    # t.write(f)
    t.write('\n')  # this is a no-op
    t.display()
    t.write('\n')  # update description
    t.display()
    t.n = 1
    t.refresh()  # this is a no-op
    t.display()
    t.refresh()
    try:
        [][0]
    except Exception:
        t.write('\n')

# Generated at 2022-06-14 14:05:54.392447
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    assert TqdmHBox().__repr__() == ''
    assert TqdmHBox().__repr__(True) == ''
    assert TqdmHBox(pbar=1).__repr__() == '100.00%|██████████| 1/1 [00:00<?, ?it/s]'

# Generated at 2022-06-14 14:05:59.461937
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        # set up a fake iterable to test clear()
        class iter_test:
            def __iter__(self):
                for i in range(10):
                    yield i
        # create tqdm widget
        pbar = tqdm_notebook(iter_test())
        # close widget
        pbar.close()
    except:
        raise AssertionError("Clear method of tqdm_notebook class throws an exception!")

# Generated at 2022-06-14 14:06:01.357688
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    import time

    with tqdm_notebook(total=10) as t:
        for i in t:
            time.sleep(1)


# Generated at 2022-06-14 14:06:05.034513
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    with tqdm_notebook(total=1, leave=False) as t:
        t.clear()
        assert t.n == 0

