

# Generated at 2022-06-14 13:58:27.154128
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    from IPython.display import clear_output, display  # , HTML
    from time import sleep

    # Test display(close=True)
    for i in tqdm(range(4), desc='1st loop', leave=False):
        sleep(0.01)
    # Test display(bar_style='danger')
    for i in tqdm(range(4), desc='2nd loop', leave=False):
        sleep(0.01)
        raise Exception
    # Test display(bar_style='success')
    for i in tqdm(range(4), desc='3nd loop', leave=True):
        sleep(0.01)
    # Test display(bar_style='warning')

# Generated at 2022-06-14 13:58:30.915693
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    # Issue #391
    with tqdm(total=2) as pbar:
        assert pbar.clear() is None
        pbar.update()
        assert pbar.clear() is None
        pbar.update()

# Generated at 2022-06-14 13:58:41.321968
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    try:
        from IPython.display import clear_output
        from IPython import get_ipython
    except ImportError:
        return None

    pbar = tnrange(10, desc='tqdm notebook', leave=True, ncols=50, mininterval=0.1)
    for i in pbar:
        try:
            pbar.set_description('Testing %i' % i)
            pbar.update()
            raise ValueError()
        except ValueError:
            pbar.set_description('Testing ERROR %i' % i)
            pbar.update()
        finally:
            pbar.set_description('Testing FINALLY %i' % i)
            pbar.update()

    # test close()
    pbar.close()
    assert pbar.displayed == False

    # test reset()

# Generated at 2022-06-14 13:58:47.807530
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Tests method `__iter__` of class `tqdm_notebook`.
    """
    import time
    # iterate over range
    i = 0
    for _ in tqdm(range(3), total=3):
        time.sleep(0.01)
        i += 1
    assert i == 3
    # iterate over list
    i = 0
    for _ in tqdm([0, 1, 2]):
        time.sleep(0.01)
        i += 1
    assert i == 3



# Generated at 2022-06-14 13:58:55.210974
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    ipython = True
    try:
        display
    except NameError:
        ipython = False
    try:
        IProgress
    except NameError:
        ipython = False
    if not ipython:
        return
    pbar = tqdm_notebook.status_printer(sys.stderr, 10, "Test")
    display(pbar)
    pbar.close()

# Generated at 2022-06-14 13:58:59.868959
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import time
    from tqdm.notebook import tqdm_notebook
    for _ in tqdm_notebook(range(3)):
        time.sleep(0.1)
        tqdm_notebook.clear()
        time.sleep(0.1)

# Generated at 2022-06-14 13:59:04.726034
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # Test without total
    out1 = tqdm_notebook.status_printer(None, None, desc="Test Desc #1")
    assert isinstance(out1, TqdmHBox)
    out1.close()
    # Test with total
    out2 = tqdm_notebook.status_printer(None, 30, desc="Test Desc #2")
    assert isinstance(out2, TqdmHBox)
    out2.close()



# Generated at 2022-06-14 13:59:08.562577
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    # Test for empty display
    t = tqdm_notebook(total=5)
    # Test for normal display
    t.display()
    t.display(desc='test display:')
    t.display(pos=4)
    # Test for error display
    t.display(bar_style='danger')
    t.close()
    return t



# Generated at 2022-06-14 13:59:16.073719
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time
    t = tqdm_notebook(total=10)
    for i in range(5):
        time.sleep(0.01)
        t.update(1)
    t.reset()
    t.update(3)
    time.sleep(0.01)
    t.close()
    time.sleep(0.01)
    t.reset(total=20)
    t.update(3)
    time.sleep(0.01)
    t.close()


if __name__ == '__main__':
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 13:59:21.560758
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    """
    Unit test for `TqdmHBox.__repr__`.
    """
    for z in range(2):
        tqdm_notebook.leave = z
        for r in (None, {'n': 0}):
            for d in (None, 'description'):
                for ascii1 in (False, True):
                    tqdm_notebook.ascii = ascii1
                    for ascii2 in (False, True):
                        ipywidgets.Widget.displayed = ascii2
                        hb = TqdmHBox()
                        if r is not None:
                            hb.pbar = Proxy(r)
                        repr = hb.__repr__(ascii2)
                        if ascii1 ^ ascii2:
                            assert repr != ''


# Generated at 2022-06-14 13:59:48.835355
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import sys
    import time
    with tqdm_notebook(total=100, file=sys.stdout, leave=False) as pbar:
        for i in range(100):
            time.sleep(.1)
            pbar.update()


# From https://github.com/tqdm/tqdm/issues/320#issuecomment-432298399

# %load https://gist.githubusercontent.com/crwiley/a08f72b7c1cf47d40a7f9d9e2b56c08f/raw/f69e848c15db7b1f946040e56a947c809e3f4fb4/ipython_tqdm.py


# Generated at 2022-06-14 13:59:52.143627
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # TODO: to be implemented
    if IPY <= 0:
        raise SkipTest("IPython/Jupyter not found")
    # TODO: test loading by IPython
    # test_tqdm_notebook_status_printer_IPython()
    pass



# Generated at 2022-06-14 13:59:57.022818
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # save and clean environment
    old_IPY = IPY
    old_IProgress = IProgress
    IPY = 1  # fake IPython
    IProgress = None  # fake widget
    tqdm_notebook.status_printer({}, total=100, desc='Test: ', ncols=100)
    # restore environment
    IProgress = old_IProgress
    IPY = old_IPY
    print('\nTest status_printer passed')

# Generated at 2022-06-14 14:00:01.061584
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    # TODO: use pytest
    # create empty instance
    hb = TqdmHBox()
    # check repr
    repr(hb)  # noqa
    # check repr_pretty
    hb._repr_pretty_(None)  # noqa

# Generated at 2022-06-14 14:00:06.000453
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Test tqdm_notebook.__iter__()
    """
    for _ in tqdm_notebook(range(2), desc='test', leave=False):
        pass
    for _ in tqdm_notebook(range(2), desc='test'):
        pass

if __name__ == '__main__':
    test_tqdm_notebook___iter__()

# Generated at 2022-06-14 14:00:09.855345
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    try:
        from time import sleep
        for i in tqdm_notebook(range(3), desc='1st loop'):
            sleep(.3)
            for _ in tqdm_notebook(range(5), desc='2nd loop', leave=False):
                sleep(.1)
    except (KeyboardInterrupt, SystemExit):
        print('interrupted!')
        return

# Generated at 2022-06-14 14:00:19.086812
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from .utils import format_sizeof
    from random import uniform
    from time import sleep
    try:
        iterable = xrange(1000)
    except NameError:
        iterable = range(1000)
    total = len(iterable)

    p = tqdm_notebook(iterable, leave=True)

    for i in iterable:
        p.update()
        sleep(uniform(0, 0.01))

    assert p.total == total
    assert p.n == total
    assert p.last_print_n == total
    assert p.last_print_t == p.last_print_t
    assert p.dynamic_miniters == 0
    assert format_sizeof(p.n) in str(p)
    assert format_sizeof(p.n) in repr(p)




# Generated at 2022-06-14 14:00:24.050781
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    test_list = [1, 2, 3, 4]
    this_tqdm_notebook = tqdm_notebook(test_list)
    assert next(this_tqdm_notebook) == test_list[0]


# Generated at 2022-06-14 14:00:28.755676
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from IPython.lib.pretty import pretty
    from IPython.core.display import display
    from IPython.core.display import display_html
    bar = tqdm_notebook()
    bar.display()
    display(bar)
    display(pretty(bar))
    display_html('<code>' + pretty(bar, True) + '</code>')

# Generated at 2022-06-14 14:00:32.341513
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    if not IPY:
        return
    glob = {}
    exec("""from tqdm.notebook import tqdm as tqdm_notebook
for i in tqdm_notebook([0, 1]):
    glob['i'] = i""", glob)
    assert(glob['i'] == 1)



# Generated at 2022-06-14 14:00:54.814870
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for method `display` of class `tqdm_notebook`.
    Adds an additional `bar_style` argument.
    """

    try:
        from IPython.utils.tests import skip_file_write_tests as skip
    except ImportError:
        from nose.plugins.skip import SkipTest as skip
    if skip is None:  # pragma: no cover
        raise unittest.SkipTest("IPython is too old")

    from unittest import TestCase
    class test_tqdm_notebook_display(TestCase):

        class tqdm(tqdm_notebook):
            """Overrides `display` method to store the last display instead
            of printing it"""

# Generated at 2022-06-14 14:00:57.045399
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    for _ in tqdm_notebook([0, 1, 2, 3]):
        sleep(0.01)



# Generated at 2022-06-14 14:01:03.753245
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    try:
        assert IProgress is not None
    except AssertionError:
        return
    test_bar = tqdm_notebook(total=10)
    assert test_bar.container.pbar.bar_style == ''
    test_bar.update()
    test_bar.reset(total=None)
    assert test_bar.container.pbar.bar_style == 'info'
    test_bar.n = 1
    assert test_bar.container.pbar.bar_style == ''
    test_bar.close()
    assert test_bar.container.pbar.bar_style == 'success'

if __name__ == '__main__':
    test_tqdm_notebook()

# Generated at 2022-06-14 14:01:15.706937
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    import time
    import numpy as np

    def assert_tqdm_notebook_working():
        assert len(container.children) == 3
        assert len(container.children[-2].children) == 3
        assert len(container.children[-2].children[2].children) == 3
        assert container.children[-2].bar_style == ""

    for desc in ["desc", None]:
        for leave in [True, False]:
            for total in [None, 10, 10.0]:
                for disable in [True, False]:
                    for leave in [True, False]:
                        with tqdm_notebook(
                                total=total, desc=desc, disable=disable,
                                leave=leave, ncols=50, dynamic_ncols=True) as t:
                            container = t.container
                

# Generated at 2022-06-14 14:01:23.347302
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    import os
    import sys
    import time
    import warnings

    from unittest import mock

    from .std import tqdm as std_tqdm
    from .utils import _range, format_sizeof

    # Mock the IPython display function during tests
    # See: https://stackoverflow.com/a/35983938
    with mock.patch("IPython.display.display") as mock_display:
        mock_display.return_value = None

        # Test method signature of display
        fp = open(os.devnull, 'w')
        iterable = _range(400)
        t = tqdm_notebook(iterable, desc="Desc", total=len(iterable), file=fp)
        # We override the `bar_format` with something simple
        # to avoid long lines on console window
       

# Generated at 2022-06-14 14:01:33.931924
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for method tqdm_notebook.reset of class tqdm_notebook
    """
    from types import GeneratorType
    # Test __init__
    t = tqdm_notebook(total=10)
    assert t.total == 10
    assert t.displayed
    t.close()
    assert not t.displayed

    t = tqdm_notebook(total=10, unit_scale=True)
    assert t.unit_scale

    t = tqdm_notebook(total=10, unit="bla")
    assert t.unit == "bla"

    t = tqdm_notebook(total=10, unit_scale=True, unit="bla")
    assert t.total == 10
    assert t.unit == "bla"
    assert t.unit_scale



# Generated at 2022-06-14 14:01:43.647685
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:
        from IPython.display import clear_output
    except ImportError:
        return  # pragma: no cover

    with tqdm_notebook(total=0) as t:
        assert t.desc == None
        assert t.container.layout.width == "20px"
        t.reset(total=5, desc="test_tqdm_notebook_reset")
        assert t.desc == "test_tqdm_notebook_reset"
        assert t.container.layout.width != "20px"  # now it should have width

    with tqdm_notebook(total=2) as t:
        t.update(1)
        t.update(1)
        assert t.total == 2
        t.reset(total=5)
        assert t.total == 5



# Generated at 2022-06-14 14:01:54.197879
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    import sys
    hbox = TqdmHBox(children=[HTML(), IProgress(min=0, max=1), HTML()])
    pbar = std_tqdm(unit_scale=0.1)
    pbar.total = 3
    pbar.n = 2
    pbar.format_dict = {'bar_format': '{l_bar}{bar}|{n_fmt}/{total_fmt}{postfix}'}
    hbox.pbar = pbar

    if sys.version_info.major >= 3:
        assert hbox.__repr__() == u'\u2588\u2593|2.0/3.0'
        assert hbox.__repr__(pretty=True) == '█▓|2.0/3.0'



# Generated at 2022-06-14 14:01:57.309066
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    "Unit test for method display of class tqdm_notebook"
    with tqdm(total=1) as pbar:
        pbar.display()
    assert pbar.displayed



# Generated at 2022-06-14 14:02:09.595449
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():  # pragma: no cover
    from unittest import TestCase
    from unittest import main

    class TestTQDMNotebookStatusPrinter(TestCase):
        def test_tqdm_notebook_status_printer(self):
            import re
            from sys import getsizeof

            def case_200():  # test ncols
                # ncols could be 100 or "100%", "100px"
                for ncols in (100, "100%", "100px"):
                    title = "case_200_ncols_%s" % ncols
                    pbar = tqdm_notebook.status_printer(title=title, ncols=ncols)

# Generated at 2022-06-14 14:02:30.023797
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .gui import tqdm_gui
    from .std import tqdm

    import time
    # Test exception handling
    for cls in [tqdm, tqdm_notebook, tqdm_gui]:
        try:
            for obj in tqdm(range(1000),
                            desc='1st loop', leave=True,
                            disable=tqdm is cls,
                            ascii=tqdm is cls)():
                raise Exception("error")
        except Exception:
            pass
        time.sleep(.5)

    # Test immediate reset (and repeated use)
    # (also ensure gui=True)

# Generated at 2022-06-14 14:02:40.348415
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    """
    Unit test for tqdm_notebook
    """
    with tqdm_notebook(range(4), desc='1st loop') as pbar:
        for i in pbar:
            pass
        # allow manual closing of tqdm
        pbar.close()
    # in manual mode, IProgress bar should not be displayed
    try:
        with tqdm_notebook(range(4), desc='2nd loop', leave=True) as pbar:
            for i in pbar:
                pass
    except KeyboardInterrupt:
        pass  # for IPython async tests
    # no total parameter: info style bar
    with tqdm_notebook(desc='3rd loop', ncols=100, leave=True) as pbar:
        for i in _range(4):
            pbar.update()

# Generated at 2022-06-14 14:02:49.442107
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from .std import set_lock as set_tqdm_lock
    with set_tqdm_lock(False):
        import io
        import html
        import re
        import unittest

        from .gui import _timeit

        class TqdmTest(unittest.TestCase):
            """Test class for tqdm_notebook(...)"""
            def __init__(self, *args, **kwargs):
                super(TqdmTest, self).__init__(*args, **kwargs)
                self.default_format = "{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]"
                self.default_msg = self.default_format.format(
                    bar='', n_fmt=0, total_fmt=0, elapsed=0)
               

# Generated at 2022-06-14 14:03:00.172229
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # Prepare expected output
    msg = "any message"
    total = 5  # any integer
    ncols = 100  # any integer or string representing a length

    # Get actual output
    output = tqdm_notebook.status_printer(0, total, msg, ncols)
    # output is a HBox containing an HTML widget and a progress bar
    assert isinstance(output, TqdmHBox)
    assert isinstance(output.children[0], HTML)
    assert output.children[0].value == msg
    assert isinstance(output.children[1], IProgress)
    assert output.children[1].value == (0 if total is None else total)
    assert output.children[1].max == 0 if total is None else total
    # assert output.children[1].max == 1 if total is None else total


# Generated at 2022-06-14 14:03:02.773839
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(total=100) as bar:
        for i in range(5):
            bar.update()
            assert bar.n == i + 1



# Generated at 2022-06-14 14:03:04.871340
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from tqdm.notebook import tnrange
    with tnrange(1) as t:
        t.n += 1
        t.close()

# Generated at 2022-06-14 14:03:10.922301
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    """Tests for class tqdm_notebook"""
    t = tqdm_notebook(range(10), desc="test", display=False)
    t.update()
    t.update()
    t.update()
    t.close()
    t.reset()


if __name__ == "__main__":
    test_tqdm_notebook()

# Generated at 2022-06-14 14:03:20.861676
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from six.moves import xrange as range
    from time import sleep

    for leave in (True, False):
        for total in (None, 10):
            for display in (True, False):
                for width in (None, 1000):
                    for disable in (True, False):
                        print("leave = %s     total = %s     display = %s     width = %s     disable = %s" % (
                            leave, total, display, width, disable))
                        with tqdm_notebook(range(10), leave=leave,
                                           display=display, ncols=width,
                                           disable=disable) as t:
                            t.reset(total=total)
                            for i in t:
                                sleep(0.01)

# Generated at 2022-06-14 14:03:24.904415
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    x = tqdm_notebook(range(3))
    assert '<bar/>' in x.__repr__(pretty=False)
    x.clear()
    assert x.__repr__(pretty=False) == {}
    x.close()



# Generated at 2022-06-14 14:03:29.406539
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    try:
        t = tqdm_notebook(total=10)
        x = 0
        while x < 10:
            t.update()
            x += 1
    except TypeError:
        raise Exception("bug in method update")
    finally:
        t.close()


# Generated at 2022-06-14 14:04:04.339231
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """Test if validating progress bar is raised correctly."""
    # Test that bar raises correctly
    try:
        for _ in tqdm_notebook(_range(10)):
            1 / 0
    except ZeroDivisionError:
        pass
    except:  # NOQA
        raise
    try:  # Ensure that bar is valid after manual raise
        for _ in tqdm_notebook(_range(10), leave=True):
            1 / 0
    except ZeroDivisionError:  # pragma: no cover
        # validating bar
        # but this branch not reachable, because of `leave=True`
        pass
    except:
        raise

    # Test bar finish in case of manual raise

# Generated at 2022-06-14 14:04:07.754988
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import time
    t = tqdm_notebook(total=100)
    for i in range(100):
        t.update()
        time.sleep(0.01)

# Generated at 2022-06-14 14:04:14.566485
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from tqdm import tqdm
    with tqdm(total=2, gui=True) as pbar:
        try:
            pbar.update(1)
            if not pbar.displayed:
                raise AssertionError("display() should have been called")
            # This should not raise an exception
            pbar.close()
        except Exception as e:
            raise AssertionError("test failed with {} ({})".format(
                type(e).__name__, e))


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_notebook()

# Generated at 2022-06-14 14:04:21.752496
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from os import linesep
    from sys import version_info

    from .gui import tqdm as tqdm_gui
    from .std import tqdm as tqdm_std

    # 0) Tests for standard tqdm
    # 0a) test the py26/py32 compatibility
    for __ in tqdm_std([1, 2]):
        break
    # 0b) test that error is propagated
    try:
        for _ in tqdm_std([1, 2, None]):
            pass
    except TypeError:
        pass
    else:
        raise AssertionError("tqdm_std failed to propagate error")
    # 0c) check that we're iterating at least once
    i = 42
    for _ in tqdm_std([1]):
        i -= 1
    assert i

# Generated at 2022-06-14 14:04:26.740235
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from random import random
    for _ in tqdm_notebook(range(1000)):
        for _ in tqdm_notebook(range(100+int(100*random())), leave=True):
            pass

# Generated at 2022-06-14 14:04:32.940083
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from .utils import FormatInfo

    def test_container():
        # Test container to test close method
        class TestContainer(dict):
            def close(self):
                self['closed'] = True
        return TestContainer()

    # Test no errors
    t = tqdm_notebook(total=10)
    t.container = test_container()
    t.close()
    assert t.container['closed']

    # Test with errors
    t = tqdm_notebook(total=10)
    t.update(5)
    t.container = test_container()
    t.close()
    assert t.container['closed']

    # Test with error style
    t = tqdm_notebook(total=10, bar_format=FormatInfo('{bar}'))
    t.update(5)
    t.container

# Generated at 2022-06-14 14:04:41.929058
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .gui import tqdm
    from .tests import pretest_posttest

    with pretest_posttest() as (pt, _):
        t = tqdm(range(10), file=pt, leave=True)
        try:
            for i in t:
                assert i == t.n - 1
                if i == 4:
                    raise Exception("Dummy Error")
        except:  # NOQA
            pass
        pt.seek(0)
        output = pt.read()
        assert len(re.findall("\|#+[>-]*\|", output)) == 1
        assert len(re.findall("\| +\|", output)) == 1
        assert len(re.findall("\| +>+\|", output)) == 1

# Generated at 2022-06-14 14:04:50.426266
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:
        pbar = tqdm_notebook(total=5)
        assert str(pbar) == ('  0%|                                         | 0/5 '
                             '[00:00<?, ?it/s]')
        for i in range(4):
            pbar.update()
        pbar.reset()
        assert str(pbar) == ('  0%|                                         | 0/5 '
                             '[00:00<?, ?it/s]')
        pbar.close()
    except:
        pass  # pragma: no cover : py2 / py3


if __name__ == '__main__':
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:05:01.298022
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """Unit test `tqdm.notebook.tqdm.reset()`."""
    import sys

# Generated at 2022-06-14 14:05:08.745818
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    t = tqdm_notebook(range(5))
    for i in t:
        assert(i in t.n)


if __name__ == '__main__':
    from sys import version_info as py_version_info
    from .utils import _test_environment, format_sizeof

    print("Python {0}; tqdm_notebook {1}\n"
          .format(format_sizeof(py_version_info),
                  format_sizeof(tqdm_notebook.__version__)))
    _test_environment()
    if IPY:
        try:
            test_tqdm_notebook___iter__()
        except:
            print("\n\n*** Unit tests failed ***\n\n")
            raise

# Generated at 2022-06-14 14:06:37.936378
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep
    for _ in tqdm(range(4), desc='1st loop', leave=False, disable=False):
        for _ in tqdm(range(3), desc='2nd loop', leave=False, disable=False):
            for _ in tqdm(range(11), desc='3rd loop', leave=False, disable=False):
                sleep(0.01)

# Generated at 2022-06-14 14:06:46.946018
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    pbar = tqdm_notebook.status_printer(None, total=0)
    assert isinstance(pbar, TqdmHBox)
    assert pbar.children[0].value == ''
    pbar = tqdm_notebook.status_printer(None, total=0, desc="desc")
    assert pbar.children[0].value == "desc"
    pbar = tqdm_notebook.status_printer(None, total=0, ncols=100)
    assert pbar.layout.width == '100px'
    assert pbar.layout.display == 'inline-flex'
    assert pbar.layout.flex_flow == 'row wrap'
    pbar = tqdm_notebook.status_printer(None, total=0, ncols="100px")

# Generated at 2022-06-14 14:06:53.186270
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from .gui import tqdm as tqdm_gui

    for leave in (True, False):
        for n in range(4):
            for klass in (tqdm_notebook, tqdm_gui):
                try:
                    pbar = klass(range(4), leave=leave)
                    for i in pbar:
                        if not i:
                            raise ValueError
                except ValueError:
                    pass
                pbar.close()

# Generated at 2022-06-14 14:07:00.457866
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from contextlib import redirect_stderr, redirect_stdout
    def test_reset(msg, total, new_total):
        with redirect_stdout(None), redirect_stderr(None):
            t = tqdm_notebook(total=total, desc=msg, unit='B', miniters=1, unit_scale=True)
            t.reset(new_total)
            return t.total
    assert test_reset('', 1, 2) == 2
    assert test_reset('', 1, 0) == 0
    assert test_reset('', None, 2) == 2

# Generated at 2022-06-14 14:07:10.866799
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from contextlib import contextmanager
    from io import StringIO

    @contextmanager
    def capture_output():
        # redirect stdout
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()
        # yield new stdout
        yield new_stdout
        # close new stdout
        new_stdout.close()
        # restore stdout
        sys.stdout = old_stdout

    # set seed such that only test_tqdm_notebook_reset() will succeed
    tqdm.monitor_interval = 100
    tqdm.gui.tests.set_test_hash_seed(97)


# Generated at 2022-06-14 14:07:13.992840
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm_notebook(range(5)) as t:
        for i in t:
            assert i == t.n - 1
    # try to close the bar (will raise if already closed)
    t.close()



# Generated at 2022-06-14 14:07:22.084734
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    dummy = tqdm_notebook(total=1)
    dummy.n = 0
    description = 'this is a description'
    bar_width = '123%'
    result = dummy.status_printer(total=10, desc=description, ncols=bar_width)
    assert result.layout.width == bar_width
    assert result.children[0].value == description
    assert result.children[1].value == 0
    assert result.children[1].max == 10

    dummy.n = 1
    result.children[1].value = 2
    # assert result.children[1].value == 2

    # assert `result` is an instance of `ipywidgets.HBox`
    assert isinstance(result, HBox)


if __name__ == "__main__":
    test_tqdm_note

# Generated at 2022-06-14 14:07:27.548868
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from IPython.display import clear_output

    for i in trange(2):
        for j in trange(10):
            if j == 5:
                break
        clear_output()
        trange(10, leave=True).reset()

# Need to call it explicitly to see output,
# but the need for the explicit call is a feature,
# not a bug like in the text version.
test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:07:31.317136
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():  # pragma: no cover
    # no errors should be raised
    with tqdm_notebook(total=2) as t:
        t.update()
        raise ValueError()
        t.update()

# Generated at 2022-06-14 14:07:38.495187
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from .utils import format_sizeof, FormatSizeof

    # Create the progressbar
    progress = tqdm_notebook(total=10)

    # Make sure tqdm is using the correct total
    assert progress.total == 10
    assert progress.n == 0

    # Print the current status of the progressbar
    print(progress, end="")
    assert progress.n == 0

    # Should throw an error if the total is negative
    try:
        progress.reset(-1)
    except ValueError:
        pass
    else:
        raise Exception("Should have thrown an exception")

    # Update the progressbar without changing the total
    progress.reset()
    assert progress.total == 10
    assert progress.n == 0

    # Update the progressbar with a new total
    progress.reset(total=42)