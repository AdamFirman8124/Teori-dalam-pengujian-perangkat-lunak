

# Generated at 2022-06-14 13:43:01.512841
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():  # pragma: no cover
    for i in tqdm(
            _range(16),
            desc='test_tqdm_gui_clear',
            leave=True,
            position=22):
        if i == 8:
            tqdm.write("what the hack?")
        elif i == 9:
            tqdm.clear()
        elif i == 10:
            tqdm.write("well, this is a second try")
        elif i == 11:
            tqdm.clear(False)
        elif i == 12:
            tqdm.write("what if I want to overlay?")
        elif i == 13:
            tqdm.clear()
        elif i == 14:
            tqdm.clear()
            tqdm.write("coucou")

# Generated at 2022-06-14 13:43:08.902405
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    # Test 1
    import matplotlib.pyplot as plt
    import pylab as pl

    plt.ion()
    with std_tqdm(total=100) as pbar:
        for i in range(100):
            pl.plot(i)
            pbar.update()
        pbar.clear()
        plt.show()
    plt.close()
    # Test 2
    # tqdm_gui(total=10).clear()
    # plt.close()



# Generated at 2022-06-14 13:43:11.752493
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    with tqdm(total=10) as t:
        for i in range(10):
            t.update()
    assert t.n == 10



# Generated at 2022-06-14 13:43:15.787972
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    with tqdm_gui(total=3) as pbar:
        try:
            pbar.clear()
        except:
            pass
        else:
            assert False, "clear not implemented"
        try:
            with tqdm_gui() as pbar2:
                pbar2.clear()
        except:
            pass
        else:
            assert False, "clear not implemented"

# Generated at 2022-06-14 13:43:25.056172
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    """ Test tqdm_gui constructor """
    try:
        import matplotlib
        import matplotlib.pyplot as plt
    except ImportError:
        return  # Tested under Python 3.4.0 (with matplotlib and tkinter)

    with tqdm_gui(total=100) as t:
        for _ in t:
            pass
        assert ('[100/100]' in t.ax.get_title())

    # Test with `total` = None
    with tqdm_gui(total=None) as t:
        for _ in t:
            pass
        assert ('[100/100]' in t.ax.get_title())

    # Test with `leave` = True

# Generated at 2022-06-14 13:43:32.769780
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from io import StringIO
    from sys import stderr, stdout
    import os

    f = StringIO()  # create a fake file
    # Save the state of stdout
    saved_stdout = stdout
    saved_stderr = stderr
    # Redirect stdout and stderr to files
    stdout = f
    stderr = f
    # Test close() method of class tqdm_gui
    try:
        with tqdm_gui(range(10), file=f, ncols=100) as xt:
            for i in xt:
                pass
        # tqdm_gui.close()
    except Exception as exc:
        warnings.warn(str(exc))
    finally:
        # Restore stderr and stdout
        stdout = saved_stdout
        st

# Generated at 2022-06-14 13:43:37.854443
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    with tqdm_gui(total=10) as pbar:
        for i in pbar:
            time.sleep(0.2)
    return

if __name__ == '__main__':
    import time
    tqdm.write("Testing tqdm_gui")
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:45.810217
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """ Unit tests for tqdm_gui.display """
    # Prevent display to be called
    tqdm_gui.display = lambda *x, **y: None

    from time import sleep
    from pylab import atleast_2d

    total = 100
    t = tqdm_gui(total=total)
    for i in range(total):
        t.update(1)
        if i % 5 == 0:
            sleep(0.2)
    t.close()

    total = 100
    t = tqdm_gui(total=total)
    for i in range(total):
        t.update(1)
        if i % 5 == 0:
            sleep(0.2)
    t.close()

    t = tqdm_gui(0, 0.5, unit_scale=True)


# Generated at 2022-06-14 13:43:54.007172
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import sys
    from .utils import FormatStrenthFilter
    from .std import TqdmTypeError, TqdmKeyError

    with FormatStrenthFilter(TqdmKeyError):
        with sys.stdout as f:
            try:
                tqdmg = tqdm_gui(unit="foobar", total=3, file=f)
            except TqdmTypeError:
                raise AssertionError("tqdm_gui(unit='foobar') raised unexpected exception")
        with sys.stdout as f:
            try:
                tqdmg = tqdm_gui(desc="foobar", total=3, file=f)
            except TqdmTypeError:
                raise AssertionError("tqdm_gui(desc='foobar') raised unexpected exception")

# Generated at 2022-06-14 13:44:02.608266
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep
    from os import getpid
    import matplotlib.pyplot as plt


# Generated at 2022-06-14 13:44:17.737888
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    t = tqdm_gui(0, 1)
    t.display()
    t.close()

# Generated at 2022-06-14 13:44:21.331930
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    # Test for undefined total
    t = tqdm_gui("test")
    t.update(50)
    t.close()

    # Test for defined total
    t = tqdm_gui("test", total=10)
    t.update(5)
    t.close()

# Generated at 2022-06-14 13:44:27.660910
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    import matplotlib.pyplot as plt
    import random

    with tqdm_gui(total=100, leave=False, disable=False) as t:
        for i in _range(100):
            t.update()
            plt.pause(random.random() / 30)
    plt.close()


if __name__ == "__main__":
    test_tqdm_gui_display()

# Generated at 2022-06-14 13:44:30.461494
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    for _ in tqdm_gui(range(10)):
        pass
    assert not plt.fignum_exists(tqdm_gui._instances[0].fig.number)

# Generated at 2022-06-14 13:44:33.809389
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from time import sleep
    from matplotlib import pyplot
    t = tqdm_gui(5)
    sleep(2)
    t.close()
    assert pyplot.isinteractive() == t.wasion

# Generated at 2022-06-14 13:44:44.331195
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    # TODO: create a test where the loop generates an exception
    import time
    import unittest

    class TestTqdmGuiDisplay(unittest.TestCase):
        def setUp(self, **kwargs):
            self.t = tqdm(total=500)

        def test_display_total(self):
            n = self.t.n
            cur_t = self.t._time()
            elapsed = cur_t - self.t.start_t
            delta_it = n - self.t.last_print_n
            delta_t = cur_t - self.t.last_print_t

            # Inline due to multiple calls
            total = self.t.total
            xdata = self.t.xdata
            ydata = self.t.ydata
            zdata = self.t

# Generated at 2022-06-14 13:44:49.598216
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from io import StringIO
    import sys
    import time

    pbar = tqdm_gui(total=100, ascii=True)
    stream = StringIO()
    pbar.out = stream
    for i in range(100):
        time.sleep(0.01)
        pbar.refresh()
        sys.stdout.flush()
        if i == 5:
            pbar.close()

# Generated at 2022-06-14 13:44:58.028562
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    # Test with tqdm_gui
    t = tqdm_gui(total=99, gui=True, disable=False)
    assert t.disable is False
    assert t.gui is True
    t.close()
    assert t.disable is True


if __name__ == '__main__':  # pragma: no cover
    from time import sleep
    from .std import TqdmKeyError, TqdmTypeError

    # Test basic GUI plotting
    with trange(9) as t:
        for i in t:
            sleep(0.1)

    # Test leave
    with trange(9) as t:
        for i in t:
            sleep(0.1)
    # t.close()

    # Test nested trange

# Generated at 2022-06-14 13:45:00.563878
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    pbar = tqdm_gui(total=10)
    pbar.close()

# Generated at 2022-06-14 13:45:02.656873
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    t = tqdm_gui(range(10))
    t.clear


# Generated at 2022-06-14 13:45:37.519779
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """Tests to make sure that the method tqdm_gui.close() properly restores
    the matplotlib environment.
    """
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    was_ion = plt.isinteractive()

# Generated at 2022-06-14 13:45:41.746283
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import random
    random.seed(6)
    with tqdm_gui(total=10) as pbar:
        for i in _range(10):
            time.sleep(0.1)
            pbar.update(1)

if __name__ == "__main__":
    test_tqdm_gui_display()

# Generated at 2022-06-14 13:45:53.177677
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    # Test for test coverage
    from tqdm import gui

    gui.tqdm_gui()
    gui.tqdm_gui(unit="bytes")
    gui.tqdm_gui(total=123)
    gui.tqdm_gui(total=123, disable=True)
    gui.tqdm_gui(total=123, disable=False)
    gui.tqdm_gui(total=123, disable=True, leave=False)
    gui.tqdm_gui(total=123, disable=True, leave=True)
    gui.tqdm_gui(total=123, disable=False, leave=True)
    gui.tqdm_gui(total=123, disable=False, leave=False)
    gui.tqdm_gui(total=123, unit="bytes")
    gui.t

# Generated at 2022-06-14 13:46:02.404343
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from nose.tools import assert_equal, assert_almost_equal

    with tqdm_gui() as t:
        for i in range(20):
            t.update()
        # https://github.com/tqdm/tqdm/issues/480#issuecomment-258933219
        t.xdata = [1, 2, 3, 4, 5]
        t.ydata = [0.1, 0.2, 0.3, 0.4, 0.5]
        t.zdata = [0.01, 0.02, 0.03, 0.04, 0.05]
        t.start_t = 1
        t.last_print_n = 2
        t.last_print_t = 3
        t.total = 4
        t.line1.set_data = lambda x, y: y

# Generated at 2022-06-14 13:46:07.154779
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    with tqdm_gui(unit=" it", unit_scale=True) as t:
        for i in t:
            t.set_postfix(it=i, refresh=False)
            if i >= 500:
                break

if __name__ == "__main__":
    test_tqdm_gui()

# Generated at 2022-06-14 13:46:11.245157
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from time import sleep
    from numpy import random

    @tqdm_gui
    def _test(t=10):
        for i in trange(t):
            sleep(random.randint(1, 5) * 1e-3)
    _test()

# Generated at 2022-06-14 13:46:20.736650
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    """Test that tqdm_gui close restores external environment"""
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    # Remember if external environment uses toolbars
    toolbar = mpl.rcParams['toolbar']
    # Remember if external environment is interactive
    wasion = plt.isinteractive()
    mpl.rcParams['toolbar'] = 'None'
    plt.ion()
    # The test
    # Create tqdm_gui
    tqdm_gui(total=10)
    # Check that toolbars are removed and interactive mode is activated
    assert(mpl.rcParams['toolbar'] == 'None')
    assert(plt.isinteractive() == True)
    # The close method

# Generated at 2022-06-14 13:46:30.346320
# Unit test for method display of class tqdm_gui

# Generated at 2022-06-14 13:46:40.398197
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """
    Test method display of class tqdm_gui.
    """
    from copy import copy

    def my_range(*args, **kwargs):
        """
        Wrapper for xrange/range function that just counts calls.
        """
        try:
            my_range.__calls__ += 1
        except AttributeError:
            my_range.__calls__ = 1
            return _range(*args, **kwargs)

    def my_time(*args, **kwargs):
        """
        Wrapper for time.time() that just counts calls.
        """
        try:
            my_time.__calls__ += 1
            return my_time.__calls__
        except AttributeError:
            my_time.__calls__ = 1
            return time.time(*args, **kwargs)

   

# Generated at 2022-06-14 13:46:46.306972
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    try:
        from matplotlib import pyplot as plt
    except ImportError:
        raise unittest.SkipTest("matplotlib not found")
    # Test tgrange
    with tgrange(10) as t:
        for i in t:
            pass


if __name__ == "__main__":
#     with tgrange(10) as t:
#         for i in t:
#             pass
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 13:47:41.853568
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    with mpl.rc_context(rc={'backend': 'agg'}):
        mpl.use('Agg')

        t = tqdm_gui(1, unit='s')
        t.display()

        t = tqdm_gui(1, unit='s', smoothing=1)
        t.display()

        t = tqdm_gui(total=1000, unit='s', smoothing=1)
        t.update(500)
        t.display()

        plt.close("all")

# Generated at 2022-06-14 13:47:43.652555
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    x = tqdm_gui(range(5))
    x.close()

# Generated at 2022-06-14 13:47:47.126581
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    t = tqdm_gui(disable=True)
    # Test display
    for i in tqdm_gui(range(10)):  # pragma: no cover
        t.display()

# Generated at 2022-06-14 13:47:50.384810
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    with tqdm_gui(total=10) as t:
        for i in _range(10):
            t.update(1)


if __name__ == '__main__':
    test_tqdm_gui()

# Generated at 2022-06-14 13:47:53.403056
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    with tqdm_gui(total=100) as t:
        for i in range(100):
            t.update(1)
    assert t.disable



# Generated at 2022-06-14 13:47:57.440055
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    with tqdm_gui(total=9, bar_format="{l_bar}{bar}{r_bar}") as pbar:
        pbar.update(2)
        # this should not raise an exception
        pbar.clear()

# Generated at 2022-06-14 13:48:05.450426
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib.pyplot as plt
    import sys

    # Create a toolbar
    toolbar = plt.rcParams['toolbar']

    # Remember interactive mode
    wasion = plt.isinteractive()

    # Run tqdm_gui
    t = tqdm_gui(10)
    t.close()

    # Test if toolbars have been restored
    assert plt.rcParams['toolbar'] == toolbar
    # Test if interactive mode has been restored
    assert plt.isinteractive() == wasion

    # Check if the gui was properly closed
    assert sys.flags.interactive == wasion

# Generated at 2022-06-14 13:48:09.924006
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    import time
    try:
        import numpy as np
        a = np.random.rand(50, 2)
        for i in tqdm(a):
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    test_tqdm_gui_clear()

# Generated at 2022-06-14 13:48:18.641451
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    # Test 1: check if close() removes self from _instances
    with std_tqdm(total=10) as t:
        instance_added = t in t._instances
    assert instance_added, "close() should add self to _instances"

    # Test 2: check if close() restores the _instances list after a
    #         left bar and re-enable toolbars
    with std_tqdm(total=10, leave=True) as t:
        instance_added = t in t._instances
        mpl_toolbar = t.mpl.rcParams['toolbar']
    assert instance_added, "close() should add self to _instances"
    assert mpl_toolbar == "None", "close() should re-enable toolbars"

    # Test 3: check if close() restores the non-interactive

# Generated at 2022-06-14 13:48:22.260702
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    t = tqdm_gui(total=100)
    try:
        t.clear()
        t.close()
    except TypeError:
        raise TypeError(
            "The method clear of the class tqdm_gui should be overwritten.")

# Generated at 2022-06-14 13:50:04.242156
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    import os
    import sys
    import time
    # Disable tqdm (pil) window
    os.environ["TK_SILENCE_DEPRECATION"] = "1"
    # Initialise
    t = tqdm_gui(total=os.get_terminal_size().columns,
                 gui=True, desc="test_tqdm_gui()")

    # Test update()
    for _ in t:
        t.update()
    # Non-blocking!
    with t:
        print("tqdm_gui hidden by default")
        time.sleep(2)
        print("but you can change its status")
    print("tqdm_gui is now closed!")

    # Test iterable display

# Generated at 2022-06-14 13:50:13.225540
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    # list of all tested cases
    tested_cases = []

    # helper function
    def _test_case(case):
        assert (case['called_args'] == case['expected_args']), \
            'called_args: {}\nexpected_args: {}'.format(
                case['called_args'], case['expected_args'])
        assert (case['poly_lims'] == case['expected_poly_lims']), \
            'poly_lims ({}):\n{}\nexpected_poly_lims ({}):\n{}'.format(
                case['n'], case['poly_lims'], case['n'], case['expected_poly_lims'])


# Generated at 2022-06-14 13:50:21.715034
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from tqdm.gui import tqdm_gui
    import sys
    _range = range if sys.version_info[0] >= 3 else xrange
    pbar = tqdm_gui(_range(1), disable=False)

    # before close
    assert pbar.disable is False
    assert len(pbar._instances) == 1
    assert pbar.mpl.rcParams['toolbar'] == 'None'
    assert pbar.plt.isinteractive() is True
    # check plot is drawn
    try:
        assert pbar.figure.canvas.manager.window.winfo_exists() is not None
    except (RuntimeError, AttributeError):
        assert pbar.ax._get_lines.get_window_extent().width is not None
    # check plot is not closed and window exists


# Generated at 2022-06-14 13:50:28.125801
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """Test the display method of tqdm_gui"""
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    t = tqdm_gui(total=10, dynamic_ncols=True)
    for i in range(10):
        t.update(1)
    t.close()
    # restore settings
    mpl.rcParams['toolbar'] = 'None'  # restore settings
    if not plt.isinteractive():
        plt.ion()
    plt.close('all')
    # Ignore exception
    pass

# Generated at 2022-06-14 13:50:33.479785
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Checks if close will not raise any Exception for the most basic use case
    and if the figure is closed or not

    :return: Nothing
    """
    from tqdm import gui
    from matplotlib import pyplot as plt

    progress_bar = gui.tqdm(total=10)
    progress_bar.close()
    assert progress_bar.fig.canvas.manager.window is None or \
        not plt.fignum_exists(progress_bar.fig.number), "Figure should be closed"

if __name__ == "__main__":
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=ArgumentDefaultsHelpFormatter)

# Generated at 2022-06-14 13:50:42.323756
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from numpy.random import RandomState
    from time import sleep

    rng = RandomState(0)
    max_t = rng.exponential(60, size=100)
    tot_t = 0

    with tqdm(max_t) as t:
        for i, sec in enumerate(max_t):
            t.display()
            sleep(sec)
            tot_t += sec / max_t[i]
            t.n = tot_t

    with tqdm(max_t, total=len(max_t)) as t:
        for i, sec in enumerate(max_t):
            t.display()
            sleep(sec)
            t.update()

if __name__ == '__main__':  # pragma: no cover
    test_tq

# Generated at 2022-06-14 13:50:44.919949
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    """Test method clear of class tqdm_gui"""
    pbar = tqdm_gui(total=100)
    for _ in range(100):
        pbar.update()
    pbar.clear()
    assert pbar.disable is True

# Generated at 2022-06-14 13:50:52.533687
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    try:
        _ = tqdm_gui(total=3)
    except TypeError:
        tqdm_gui.close()
    else:
        raise RuntimeError
    return


if __name__ == '__main__':
    from time import sleep
    try:
        from itertools import product
        for x, y in tqdm(list(product(range(4), repeat=3)), desc='123'):
            sleep(1)
    except KeyboardInterrupt:
        print("Interrupted")

# Generated at 2022-06-14 13:51:02.499556
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .std import TqdmTypeError, TqdmDeprecationWarning
    from .std import tqdm
    from .utils import _decr_tracking, _supports_unicode, _term_move_up
    import re
    import sys
    import time

    def format_dict():
        warn('format_dict is deprecated in favour of bar_format',
             TqdmDeprecationWarning, stacklevel=2)
        return {'l_bar': '<', 'r_bar': '>', 'bar_format': ''}

    # list of tested attributes
    attr_list = ['bar_format', 'postfix', 'smoothing']
    # list of tested widgets

# Generated at 2022-06-14 13:51:03.885867
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    pass

