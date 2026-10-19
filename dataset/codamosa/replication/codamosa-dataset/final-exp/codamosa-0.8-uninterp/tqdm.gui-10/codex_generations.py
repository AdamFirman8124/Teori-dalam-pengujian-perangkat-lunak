

# Generated at 2022-06-14 13:42:55.593716
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    print("test_tqdm_gui")
    try:
        with tqdm(total=10, desc='Test', leave=True) as t:
            import time
            for i in range(10):
                time.sleep(1)
                t.update()
    except BaseException as e:
        print(" > TEST FAILED: {}".format(e))


if __name__ == '__main__':
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:03.665407
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():  # pragma: no cover
    from tqdm import tqdm_gui
    from time import sleep
    # import matplotlib.pyplot as plt
    # plt.ion()

    with tqdm_gui(unit='us') as t:
        for i in range(0, 100):
            sleep(0.01)
            t.clear()
            t.postfix = [i]
            t.update(1)

    # plt.ioff()
    # plt.show(block=True)

if __name__ == '__main__':
    test_tqdm_gui_clear()

# Generated at 2022-06-14 13:43:14.047772
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib.pyplot as plt
    mpl = plt
    t = tqdm_gui(total=60, gui=True)
    t.start_t = 0.0
    t.n = 0.0
    t.mpl = mpl
    t.plt = plt
    t.fig = plt.figure()
    t.ax = t.fig.add_subplot(111)
    t.line1, = t.ax.plot(t.xdata, t.ydata, color='b')
    t.line2, = t.ax.plot(t.xdata, t.ydata, color='k')
    t.ax.legend(("cur", "est"), loc='lower left')
    t._time = lambda: 0.0

# Generated at 2022-06-14 13:43:17.247245
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from time import sleep

    t = tqdm_gui(total=100, leave=False)
    for i in t:
        sleep(0.01)

    t.close()

# Generated at 2022-06-14 13:43:21.922432
# Unit test for constructor of class tqdm_gui

# Generated at 2022-06-14 13:43:31.361752
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    # Test tqdm_gui()
    from multiprocessing import freeze_support
    from collections import deque
    from math import sqrt
    from time import sleep
    try:
        from tkinter import Tcl
    except ImportError:
        from tkinter import Tk

    freeze_support()
    try:
        Tcl().eval('exit')
    except TclError:
        Tk().destroy()

    # Test
    with tqdm(total=100) as t:
        for i in range(10):
            sleep(0.1)
            t.update(10)

    # Test with manual GUI refresh
    with tqdm(total=100, leave=True) as t:
        for i in range(10):
            sleep(0.1)
            t.update(10)

# Generated at 2022-06-14 13:43:42.073807
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .std import TqdmTypeError, TqdmKeyError, TqdmDeprecationWarning
    import sys
    from matplotlib import pyplot as plt
    from matplotlib import rcParams
    from unittest import TestCase, skipIf
    from .utils import _range

    class MatplotlibWarning(Exception):
        pass

    def import_warn(name, globals=None, locals=None, fromlist=(), level=-1):
        """Warn on import of `name`

        Warn if `warn` is True, and raise an exception if it is a callable.
        """
        if isinstance(warn, bool):
            if warn:
                warn("{0} module is required for tests. Skipping.."
                     .format(name), TqdmExperimentalWarning)
                return False

# Generated at 2022-06-14 13:43:51.427553
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from .std import tqdm as tqdm_std
    from .std import trange as trange_std
    t = tqdm_gui(range(10))
    with t:
        for i in range(10):
            t.clear()
            assert t.last_print_n == 10
    assert t.last_print_n == 10
    t = trange_std(range(10))
    with t:
        for i in range(10):
            t.clear()
            assert t.last_print_n == 10
    assert t.last_print_n == 10
    t = tqdm_std(range(10))
    with t:
        for i in range(10):
            t.clear()
            assert t.last_print_n == 10

# Generated at 2022-06-14 13:44:01.135500
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep, time
    import matplotlib.pyplot as plt
    plt.ion()

# Generated at 2022-06-14 13:44:03.076001
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    with tqdm_gui(total=1) as t:
        t.close()
    assert t.disable



# Generated at 2022-06-14 13:44:33.004292
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    # see issue #775
    from math import sqrt

    with tqdm_gui(
        total=10, ncols=10, ascii=True, disable=False, leave=False,
            dynamic_ncols=False) as pbar:
        for _ in range(10):
            pbar.update()
            pbar.set_postfix(val=sqrt(_))
    pbar.close()
    with tqdm_gui(
        total=None, ncols=10, ascii=True, disable=False, leave=False,
            dynamic_ncols=True) as pbar:
        for _ in range(10):
            pbar.update()
            pbar.set_postfix(val=sqrt(_))
    pbar.close()

    # Test toolbars

# Generated at 2022-06-14 13:44:43.591108
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib.pyplot as plt
    from tqdm.gui import tqdm, tgrange
    from tqdm import TqdmExperimentalWarning

    """
    Test suite to ensure the tqdm.gui module is working properly

    :raises: AssertionError
    """
    # test tqdm_gui close
    with tqdm(total=100) as t:
        t.close()
    assert (t.disable == True)

    # test tqdm_gui using iterator
    with tqdm(iterable=range(10)) as t:
        # this is the most important part of the test
        t.close()
        assert (t.disable == True)

    # test tgrange close
    with tgrange(10) as t:
        t.close()

# Generated at 2022-06-14 13:44:47.843244
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .utils import _time

    t = tqdm_gui(total=None, disable=True, gui=True, miniters=1)
    t.last_print_n = 0
    t.last_print_t = t.start_t = _time()
    t.n = 1
    t.display()

# Generated at 2022-06-14 13:44:57.943816
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    with tqdm_gui(total=10) as t:
        assert not t.disable
        t.clear()
        assert t.disable

if __name__ == "__main__":
    from tqdm._tqdm_test_mixins import DifferentToNextMixin
    import pytest

    class TqdmGuiTest(DifferentToNextMixin, object):
        tclass = tqdm_gui

    @pytest.mark.gui
    @pytest.mark.tqdm_gui
    def test_tqdm_gui(*args, **kwargs):
        kwargs['leave'] = True
        TqdmGuiTest.test_callback(*args, **kwargs)
        TqdmGuiTest.test_position(*args, **kwargs)
        TqdmGuiTest.test_gui

# Generated at 2022-06-14 13:45:06.198740
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from nose.tools import assert_equal
    from .tests import TEST_DISPLAY, closing, Pretend
    # make sure tqdm_gui is not affected by tests
    if not TEST_DISPLAY or __name__ != "__main__":
        return
    with closing(Pretend([""], ['\r\x1b'], [])) as stream:
        with tqdm(total=2, file=stream, mininterval=1e6) as t:
            t.update(1)
            t.clear()


# Test tqdm_gui (method display)

# Generated at 2022-06-14 13:45:12.663229
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    import matplotlib
    import matplotlib.pyplot as plt
    from time import sleep
    pbar = tqdm_gui(total=100, desc="preparing...", leave=True)
    for i in _range(100):
        pbar.update(1)
        sleep(0.1)
        pbar.clear()
        pbar.display()
    pbar.close()  # stop and close current bar
    pbar.clear()  # do nothing

# Generated at 2022-06-14 13:45:21.174664
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    """Unit test for method clear of class tqdm_gui"""
    with std_tqdm(total=1000000) as t:
        try:
            t.clear()
        except NotImplementedError:
            pass
        else:
            raise AssertionError('tqdm_gui().clear() should raises NotImplementedError')
    try:
        std_tqdm.clear()
    except NotImplementedError:
        pass
    else:
        raise AssertionError('tqdm_gui.clear() should raises NotImplementedError')
    # Inline due to multiple calls
    from .std import format_interval, format_meter
    # unit='it'
    assert format_meter(1, 1, 20, ncols=20, unit='it') == '1              <it>/s'

# Generated at 2022-06-14 13:45:29.075145
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from matplotlib import pyplot as plt

    from .gui import tqdm_gui
    # Uncomment the following line to see what happens if you
    #  use the same progressbar twice!
    # from tqdm import tqdm

    b = tqdm_gui(range(50))
    for i in b:
        if i > 5:
            b.set_description("Wow")
        plt.pause(0.001)
        b.update()

# Generated at 2022-06-14 13:45:31.899079
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    t = tqdm(total=10)
    assert not t.disable
    t.clear(nolock=True)
    assert str(t) == ''
    t.close()

# Generated at 2022-06-14 13:45:39.386129
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    """Unit test for method display of class tqdm_gui"""
    import time
    import matplotlib

    # if matplotlib.rcsetup is None:
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    plt.ion()
    plt.figure()
    tq = tqdm(total=100)
    for i in range(100):
        time.sleep(0.1)
        tq.update(1)
    tq.close()
    plt.close()