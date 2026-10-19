

# Generated at 2022-06-14 13:58:11.668080
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    assert HBox() == tqdm_notebook.status_printer(None)
    assert HBox() == tqdm_notebook.status_printer(None, 10)
    assert HBox() == tqdm_notebook.status_printer(None, 10, "Hello")

try:
    from unittest import mock
except ImportError:  # Python 3.2 and below
    import mock


# Generated at 2022-06-14 13:58:17.481585
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    """
    Test if the `__repr__` method of `TqdmHBox` class
    correctly format to ipython notebook format
    """
    from ast import literal_eval

    def dict_test(test_dict):
        return all(elem in test_dict.values() for elem in list(test_dict))

    def test_two_dicts(dict1, dict2):
        return all(dict_test(elem) for elem in [dict1, dict2])

    # start test by creating a tqdm object
    tqdm_obj = tqdm_notebook(range(100), desc="test")
    # get some values from the tqdm object
    tqdm_format_dict = tqdm_obj.format_dict
    tqdm_total = tqdm_obj.total


# Generated at 2022-06-14 13:58:26.379565
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Unit test for method `__iter__` of class `tqdm_notebook`
    """
    #
    # Test 1 - Simple iterator
    #
    with tqdm_notebook(total=10) as pbar:
        for _ in range(10):
            # pbar.clear()  # Clear display
            pbar.update()

    #
    # Test 2 - Exception in the loop (manual tqdm only)
    #
    with tqdm_notebook(total=10, disable=False) as pbar:
        for k in range(10):
            if k == 5:
                1 / 0  # Generate exception
            pbar.update()



# Generated at 2022-06-14 13:58:37.657130
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep
    from random import random
    from tqdm import trange
    from IPython.display import clear_output

    total = 10
    with tqdm_notebook(total=total) as pbar:
        for i in range(total):
            sleep(0.1)
            pbar.update(1)
    assert pbar.n == total

    with trange(10) as pbar:
        for i in pbar:
            sleep(0.1)
    assert pbar.n == total

    desc = 'Test tqdm_notebook with no total'
    pbar = tqdm_notebook(desc=desc)
    for i in range(10):
        sleep(0.1)
        pbar.update(1)
    pbar.close()


# Generated at 2022-06-14 13:58:39.786903
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():  # pragma: no cover
    from IPython.display import clear_output
    with tqdm_notebook(total=10) as pbar:
        for k in range(10):
            clear_output(wait=True)
            pbar.update(1)

# Generated at 2022-06-14 13:58:43.426632
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    # ref:
    # https://github.com/tqdm/tqdm/blob/master/tests/test_tqdm.py
    from time import sleep

    import nose
    with nose.plugins.attrib.attr('type', 'notebook'):
        for i in tqdm([0, 1, 2]):
            sleep(0.01)
            assert i == i

# Generated at 2022-06-14 13:58:51.270592
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    from sys import stdout
    t = tqdm_notebook(3)
    t.n = 1
    t.refresh()
    try:
        test_t = TqdmHBox(children=t.container.children)
        assert repr(test_t) == t.format_meter(**t.container._repr_json_(False))
        assert repr(test_t) != t.format_meter(**t.container._repr_json_(True))
        stdout.write(repr(test_t))
    finally:
        t.close()

# Generated at 2022-06-14 13:58:59.287240
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from io import StringIO  # for Python 3 compat
    from subprocess import Popen, PIPE
    # Note: cgi.escape does not handle `>` nor `<`
    print_string = "Hi \033[31m<world>\033[0m!"

    def _test_display_kwarg_true():
        # Test the display kwarg
        with StringIO() as our_file:
            with tqdm_notebook(total=2, file=our_file) as pbar:
                assert pbar.displayed is False
                assert pbar.disable is False
                pbar.display()
                assert pbar.displayed is True
                pbar.update()
                pbar.update()
                assert our_file.getvalue() == ''
                # assert our_file.getvalue() == "\r\

# Generated at 2022-06-14 13:59:03.772231
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from IPython.display import clear_output
    with tqdm_notebook(total=1, leave=True) as pbar:
        pbar.display()
        clear_output(wait=True)


if __name__ == '__main__':
    test_tqdm_notebook_display()

# Generated at 2022-06-14 13:59:11.874641
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """Test the method reset of class tqdm_notebook"""
    from time import sleep
    pbar = tqdm_notebook(total=4)
    for i in _range(4):
        pbar.update(1)
        sleep(0.01)
    pbar.reset(5)
    sleep(0.01)
    for i in _range(5):
        pbar.update(1)
        sleep(0.01)
    pbar.close()


if __name__ == '__main__':
    """
    A command-line interface to the tqdm notebook
    """

    try:
        import argparse
    except ImportError:
        sys.stderr.write('WARNING: the python module `argparse` is missing.\n')

# Generated at 2022-06-14 13:59:39.706746
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    try:
        with tqdm_notebook(total=1) as t:
            pass
        t.close()
    except AssertionError:
        return False
    return True

# Generated at 2022-06-14 13:59:50.573532
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Test bar message and update/close.
    """
    import io
    import contextlib
    import sys
    import logging
    logger = logging.getLogger(__name__)

    @contextlib.contextmanager
    def capture_output():
        oldout, olderr = sys.stdout, sys.stderr
        try:
            out = [io.StringIO(), io.StringIO()]
            sys.stdout, sys.stderr = out
            yield out
        finally:
            sys.stdout, sys.stderr = oldout, olderr
            out[0] = out[0].getvalue()
            out[1] = out[1].getvalue()


# Generated at 2022-06-14 13:59:58.356865
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    from time import sleep
    from tqdm import tqdm

    with tqdm(total=5, desc='Test', miniters=2, mininterval=0) as bar:
        bar.display(bar_style='danger', close=True)
        bar.display(bar_style='danger', close=True)
        sleep(1)
        bar.display(bar_style='success', close=True)
        bar.display(bar_style='success', close=True)
        sleep(1)
        bar.display(bar_style='success')
        bar.display(bar_style='success')
        bar.display(bar_style='info')
        bar.display(bar_style='info')
        bar.display(bar_style='warning')

# Generated at 2022-06-14 14:00:08.015762
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep
    for close in [False, True]:
        for bar_style in ['', 'info', 'success', 'warning', 'danger']:
            for msg in ["test msg", '']:
                for ncols in [-1, 100, "100", "100%", None]:
                    print("close = %s, bar_style = '%s', msg = '%s', ncols = %s"
                          % (close, bar_style, msg, ncols))
                    t = tqdm_notebook(total=2, ncols=ncols)
                    sleep(0.01)
                    t.display(msg=msg, bar_style=bar_style, close=close)
                    sleep(0.01)
                    t.display(bar_style='')
                    sleep(0.01)
                   

# Generated at 2022-06-14 14:00:14.238797
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from .tests_tqdm import pretest_posttest  # NOQA
    from .gui import tqdm, tqdm_notebook
    bar = tqdm_notebook.status_printer(None, 100, "Notebook Bar Title")
    for _ in tqdm_notebook(range(101), desc="Custom Bar", gui=True):
        pass


if __name__ == "__main__":
    test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 14:00:22.200849
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    from random import randrange

    for unit_scale in [False, True, 10]:
        t = tqdm_notebook(total=10, unit_scale=unit_scale, leave=True)
        for x in range(10):
            t.update()
            sleep(0.1)
        t.close()

        # Test reset
        t.reset()

        # Check manual increment
        t.update()

        # Test reset with total=3
        t.reset(3)
        t.update(2)
        try:
            t.update(2)
        except:
            pass
        else:
            assert False

        # Test total=None (unknown total)
        t.reset(None)
        t.update(2)

# Generated at 2022-06-14 14:00:31.492923
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    """
    Unit test for constructor of class tqdm_notebook
    """
    # Test constructor (normal)
    with tqdm(total=10) as t:
        assert len(t.container.children) == 3
        assert isinstance(t.container, HBox)
        assert isinstance(t.container, TqdmHBox)
        assert isinstance(t.container.children[0], HTML)
        assert isinstance(t.container.children[1], IProgress)
        assert isinstance(t.container.children[2], HTML)

        assert t.container.children[0].value == ''
        assert t.container.children[1].value == 0
        assert t.container.children[2].value == ''

        assert t.container.children[1].min == 0

# Generated at 2022-06-14 14:00:39.364201
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    try:
        from IPython import get_ipython
    except ImportError:
        print("IPython is needed to test tqdm_notebook_update.")
        return

    IP = get_ipython()
    if IP is None:
        print("IPython is needed to test tqdm_notebook_update.")
        return


# Generated at 2022-06-14 14:00:51.340918
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    hbox = TqdmHBox(
        children=[HTML(), IProgress(min=0, max=10), HTML()])
    hbox.pbar = proxy(tqdm_notebook(10))
    hbox.pbar.n = 5
    d = hbox.pbar.format_dict.copy()
    for pretty in (False, True):
        # Test header
        header_type = {'ascii': '▐', 'unicode': '█'}.get(
            d['ascii'] if pretty is None else pretty, 'type')
        pattern = r'^\s*{header_type}.*{header_type}\s*$'.format(
            header_type=re.escape(header_type))
        assert re.match(pattern, repr(hbox)) is not None
        # Test bar


# Generated at 2022-06-14 14:00:54.593443
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from .gui import tqdm
    # Too short for progress bar
    for _ in tqdm(range(5), total=10):
        pass
    # Reset and reuse as info bar
    for _ in tqdm.reset(total=None, leave=True):
        pass

# Generated at 2022-06-14 14:01:19.470582
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():

    # Test bar display
    bar_msg = 'bar display'
    bar_msg_encoded = re.escape(bar_msg)
    bar_html_encoded = re.escape(escape(bar_msg))
    bar_regex = r'^(?:' + bar_msg_encoded + r'|\A).*' + \
        r'(?:' + bar_msg_encoded + r'|\Z)'
    bar_html_regex = r'^(?:' + bar_html_encoded + r'|\A).*' + \
        r'(?:' + bar_html_encoded + r'|\Z)'
    bar_regex_nobar = r'.*\Z'
    bar_html_regex_nobar = r'(?:' + bar_html_encoded + r

# Generated at 2022-06-14 14:01:25.436782
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    # Testing the close method of a tqdm_notebook instance in an interactive
    # way.
    # This test is mainly aimed to check that the closing of the bar is
    # smooth and without raising any exception.

    # Initialize a tqdm_notebook instance
    t = tqdm_notebook(total=50)

    # Fill the bar up to 50 iterations (total of the tqdm_notebook instance)
    for i in range(1, 51):
        t.update()

    # Close the bar
    t.close()

# Generated at 2022-06-14 14:01:28.650436
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    with tqdm_notebook(total=100) as bar:
        for i in range(50):
            bar.update()
        bar.close()



# Generated at 2022-06-14 14:01:31.066734
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep

    for i in tqdm_notebook(__name__, total=5):
        sleep(0.3)

# Generated at 2022-06-14 14:01:41.552355
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Tests the method status_printer of class tqdm_notebook"""
    status_printer = tqdm_notebook.status_printer
    if IProgress is None:  # #187 #451 #558 #872
        return
    assert(isinstance(status_printer(_, total=10), TqdmHBox))
    assert(isinstance(status_printer(_, total=None), TqdmHBox))  # info bar
    assert(isinstance(status_printer(_, ncols=100), TqdmHBox))
    assert(isinstance(status_printer(_, ncols="100px"), TqdmHBox))
    assert(isinstance(status_printer(_, ncols=100, total=10), TqdmHBox))



# Generated at 2022-06-14 14:01:53.020268
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from random import shuffle
    from time import sleep
    for _ in tqdm_notebook(
            [3, 2.5, 1, 0.5, 0],
            desc='1st loop', leave=True):
        sleep(0.75)
    for _ in tqdm_notebook(
            [4, 3, 2, 1],
            desc='2nd loop', leave=True, unit_scale=True, unit='i'):
        sleep(0.75)
    for _ in tqdm_notebook(
            [6, 5, 4, 3, 2, 1],
            desc='3rd loop', leave=True, dynamic_ncols=True):
        shuffle(_)  # fake randomness of loop iterations
        sleep(0.75)

if __name__ == "__main__":
    test_t

# Generated at 2022-06-14 14:01:59.012563
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from .gui import tqdm_gui

    # tqdm_notebook is a subclass of tqdm_gui which has a method status_printer
    tqdm_notebook_status_printer = tqdm_notebook.status_printer

    # Get tqdm_gui status_printer, as tqdm_notebook.status_printer is a static
    # and not a class method, we need to get an instance of tqdm_notebook and
    # access its value of status_printer, which is the same as the tqdm_gui
    # status_printer
    tqdm_gui_status_printer = tqdm_notebook().status_printer

    # Test that the methods are the same
    assert tqdm_notebook_status_printer == tqdm_gui_status

# Generated at 2022-06-14 14:02:06.724383
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # setup
    pbar = tqdm_notebook(total=10, desc='test')
    # test
    for i in pbar:
        pass
    # verify
    assert pbar.n == 10
    assert pbar.container.children[-2].bar_style == 'success'


if __name__ == '__main__':
    test_tqdm_notebook___iter__()

# Generated at 2022-06-14 14:02:13.330562
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    import unittest
    import sys
    import re

    class TestTqdmNotebook_Display(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.bar = tqdm_notebook(range(3), leave=False, dynamic_ncols=True)
            cls.bar.start()
            sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8',
                              errors='replace')
            sys.stderr = open(sys.stderr.fileno(), mode='w', encoding='utf8',
                              errors='replace')

        @classmethod
        def tearDownClass(cls):
            cls.bar.close()
            cls.bar.container.close()
            cls.bar.clear()


# Generated at 2022-06-14 14:02:19.697721
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep

    for bar_style in ['', 'success', 'info', 'warning', 'danger']:
        t = tqdm_notebook(desc='Testing {}'.format(bar_style), leave=True,
                          total=100, bar_format='{desc}: {bar}')
        for i in range(100):
            if bar_style:
                t.disp(bar_style=bar_style)
            sleep(0.05)
            t.update(1)
        t.close()
        sleep(0.2)



# Generated at 2022-06-14 14:02:58.351670
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for method reset of class tqdm_notebook
    """
    import sys
    # Test case when total is not set
    with tqdm(total=None, desc='tqdm', ascii=True) as pbar:
        for i in _range(10):
            pbar.update()
    assert(sys.stdout.getvalue().strip().split('\r')[-1] == "tqdm:  10%|#         | 1/10 [00:00<?, ?it/s]")
    sys.stdout.close()

    # Test case when total is set
    with tqdm(total=10, desc='tqdm', ascii=True) as pbar:
        for i in _range(10):
            pbar.update()

    # sys.stdout.

# Generated at 2022-06-14 14:03:03.396965
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    """ Test tqdm.notebook.clear() method. """
    if not IPY:
        return  # It's only a test for notebook
    tn = tqdm_notebook(["a", "b"], file=None)
    tn.display(bar_style='danger')
    tn.clear()
    tn.close()
    assert True

# Generated at 2022-06-14 14:03:09.909872
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from .utils import format_dict
    _tqdm = tqdm_notebook(range(7), ascii=True)
    _tqdm.close()

# Generated at 2022-06-14 14:03:21.367390
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    ipywidgets = None
    try:
        import ipywidgets  # NOQA
    except ImportError:
        pass
    assert IPY and ipywidgets, "Test requires IPython and ipywidgets"
    from IPython.display import HTML, display
    display(HTML("<hr/>"))  # create new output cell
    from contextlib import contextmanager
    from io import StringIO
    @contextmanager
    def capture_output(file):
        stream, file.stream = file.stream, StringIO()
        yield
        file.stream = stream
    class tqdm_notebook_capture(tqdm_notebook):
        @property
        def container(self):
            return super(tqdm_notebook_capture, self).container


# Generated at 2022-06-14 14:03:29.782265
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from sys import getsizeof
    from time import sleep
    for i in tqdm_notebook(range(5), desc="1st loop"):
        sleep(.1)
    size_before = getsizeof(tqdm_notebook.pbar_dict)
    # This is the thing we are testing (reset function)
    tqdm_notebook.reset()
    for i in tqdm_notebook(range(5), desc="2nd loop"):
        sleep(.1)
    size_after = getsizeof(tqdm_notebook.pbar_dict)
    assert size_before == size_after

# Generated at 2022-06-14 14:03:40.972798
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from unittest import TestCase
    import time
    import numpy as np

    class MyTestCase(TestCase):
        def test_tqdm_notebook___iter__(self):
            with tqdm(total=10, miniters=0, bar_format='{l_bar}{bar}{r_bar}') as t:
                for i in t:
                    time.sleep(0.1)
                    t.set_description("Counting to %d" % i)
                    self.assertEqual(i, t.n)
                    self.assertEqual("Counting to %d" % i, str(t))
                    if i == 5:
                        t.total = 20
                    if i == 6:
                        t.miniters = 1
                        t.update(-1)

# Generated at 2022-06-14 14:03:49.808181
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Test reset of tqdm_notebook
    """
    import time
    t = tqdm_notebook(total=2)
    t.update(1)
    assert t.n == 1
    t.reset()
    assert t.n == 0
    # test reset total
    t = tqdm_notebook(total=10, mininterval=0.1)
    time.sleep(0.3)
    assert t.n == 10
    t.reset(total=2)
    time.sleep(0.3)
    assert t.n == 2


if __name__ == '__main__':
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:03:57.038235
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    # Method reset of class tqdm_notebook
    # Unit test for general cases
    from .utils import FormatCustom, format_dict
    from .std import tqdm_notebook as tqdm


# Generated at 2022-06-14 14:03:59.782515
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from random import random
    L = [random() for i in tqdm_notebook(range(1000))]
    assert len(L) == 1000



# Generated at 2022-06-14 14:04:09.901228
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    blank_line = " \x1b[A\n\r"
    blank_line += "\x1b[A"
    total_width = 20
    widgets = ["Test: ", IProgress(min=0, max=total_width), " ", HTML(), " ", HTML()]
    pbar = HBox(widgets)
    desc = 'test'
    bar_format = '{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}'
    format_dict = tqdm_notebook.format_dict  # type: ignore
    format_dict['ncols'] = total_width
    format_dict['bar_format'] = bar_format
    format_dict['desc'] = desc

# Generated at 2022-06-14 14:05:51.209815
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    ncols = 100
    tqdm_notebook.status_printer(None, None, 'Desc', ncols)
    # Test ncols
    expected_ncols = str(ncols) + 'px'
    actual_ncols = tqdm_notebook.status_printer(None, None, 'Desc', ncols).layout.width
    assert expected_ncols == actual_ncols
    # Test width
    expected_width = '20px'
    actual_width = tqdm_notebook.status_printer(None, None, None).layout.width
    assert expected_width == actual_width
    # Test default width
    expected_width = '20px'
    actual_width = tqdm_notebook.status_printer(None, None, None, None).layout

# Generated at 2022-06-14 14:05:59.826228
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    with tqdm_notebook(total=10, desc='default') as pb:
        pb.update()
        assert pb.n == 1

    with tqdm_notebook(total=10, desc='reset') as pb:
        pb.update()
        pb.reset(total=20)
        assert pb.n == 1
        assert pb.total == 20

    with tqdm_notebook(total=10, desc='auto') as pb:
        pb.update()
        pb.reset()
        assert pb.n == 1
        assert pb.total == 10

    with tqdm_notebook(total=10, desc='default') as pb:
        pb.update()
        assert pb.n == 1

# Generated at 2022-06-14 14:06:02.263369
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep

    for i in tqdm_notebook(range(3)):
        sleep(0.2)
        assert(True)



# Generated at 2022-06-14 14:06:12.163117
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from io import StringIO
    from random import random

    # Unit tests

# Generated at 2022-06-14 14:06:16.610233
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time
    bar = tqdm_notebook(total=10)
    for i in range(5):
        time.sleep(1)
        bar.update()
    bar.reset(total=5)
    for i in range(5):
        time.sleep(1)
        bar.update()
    assert bar.n == 5 and bar.total == 5
    return True


if __name__ == "__main__":
    from .__main__ import _test_tqdm

    _test_tqdm('notebook', function=test_tqdm_notebook_reset)

# Generated at 2022-06-14 14:06:27.553164
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    if IProgress is None:
        raise ImportError("IProgress not found.")

    # Try with desc
    container = tqdm_notebook.status_printer(file=None, desc='Testing')
    assert (container.children[0].value == 'Testing')

    # Try with total
    container = tqdm_notebook.status_printer(file=None, total=50)
    assert (container.children[1].value == 0)
    assert (container.children[1].max == 50)

    # Try with total and desc
    container = tqdm_notebook.status_printer(file=None, total=50, desc='Testing')
    assert (container.children[0].value == 'Testing')
    assert (container.children[1].value == 0)

# Generated at 2022-06-14 14:06:30.228463
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    t = tnrange(4, leave=True)
    for _ in t:
        pass


if __name__ == "__main__":
    from .main import _test_functionalities
    _test_functionalities()

# Generated at 2022-06-14 14:06:34.749082
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(total=10) as progress_bar:
        progress_bar.update(2)
        progress_bar.update(2)
        progress_bar.update(3)


if __name__ == '__main__':
    test_tqdm_notebook_update()

# Generated at 2022-06-14 14:06:37.589313
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import pytest
    t = tqdm_notebook(total=2)
    t.clear()
    t.close()

test_tqdm_notebook_clear()

# Generated at 2022-06-14 14:06:39.962276
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    for i in tqdm_notebook(range(5)):
        sleep(0.05)
        assert True
