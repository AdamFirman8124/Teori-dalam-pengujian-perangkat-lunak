

# Generated at 2022-06-14 13:42:48.444160
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    import time
    with tqdm_gui(total=100) as t:
        for i in _range(100):
            time.sleep(0.1)
            t.update()
        t.clear()

# Generated at 2022-06-14 13:42:55.916342
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """Tests tqdm_gui close() method"""
    from collections import deque
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # Initialize tqdm_gui object
    tq = tqdm_gui(disable=False)

    # Initialize the parameters of tqdm_gui and test the close() method
    tq.disable = True
    tq.mpl = mpl
    tq.plt = plt
    tq.toolbar = 'None'
    tq.fig, tq.ax = plt.subplots(figsize=(9, 2.2))
    tq.mininterval = 0.5

    tq.close()

    # Initialize the parameters of tqdm_gui and test the close() method
    tq.disable = False

# Generated at 2022-06-14 13:43:06.220516
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import sys
    import time
    import matplotlib.pylab as plt

    # Instantiate tqdm
    tq = tqdm_gui(total=100)
    # Display figure
    plt.show()
    # Update progressbar several times
    for i in range(1, 100):
        tq.update(1)
        time.sleep(0.01)     # Sleep for a while
        tq.display()         # Display figure
        # Ensure that figure is displayed
        assert sys.flags.interactive and plt.fignum_exists(tq.fig.number)
    # Close tqdm bar
    tq.close()
    # Ensure that figure is closed
    assert not plt.fignum_exists(tq.fig.number)

# Generated at 2022-06-14 13:43:15.641441
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep
    from numpy import mean, min, max
    from matplotlib import pyplot as plt

    with tqdm(1e6, desc="test 1", ncols=10, color="#F4A460") as t:
        for _ in t:
            sleep(0.00111111)

    # with tgrange(1e6, desc="test 2", ncols=10, color="#F4A460") as t:
    #     for _ in t:
    #         sleep(0.00111111)

    with tqdm(1e6, desc="test 3", ncols=10, color="#8B4513") as t:
        for _ in t:
            sleep(0.00111111)

# Generated at 2022-06-14 13:43:17.791973
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    t = tqdm_gui(["A", "B", "C"])
    t.clear()

# Generated at 2022-06-14 13:43:23.484720
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from .std import TqdmWarning
    try:
        for i in tqdm(range(150), desc='test_tqdm_gui_close'):
            pass
    except (TqdmWarning, ImportError, NameError):
        return
    # Check toolbars restored to previous state
    assert mpl.rcParams['toolbar'] == toolbar_state
    # Check if interactive state restored to previous state
    assert plt.isinteractive() == wasion_state

# Generated at 2022-06-14 13:43:32.055148
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .std import tqdm as std_tqdm
    from .std import trange as std_trange
    from .std import tqdm_gui as std_tqdm_gui
    from .std import trange as std_trange

    for t in (tqdm, std_tqdm, tqdm_gui, std_tqdm_gui):  # pragma: no cover
        with t(total=10, desc='test') as tg:
            for _ in _range(1, 10):
                tg.display()
                tg.update()
        with t(desc='test', leave=True) as tg:
            for _ in _range(5):
                tg.display()
                tg.update()


# Generated at 2022-06-14 13:43:34.556983
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from .gui import trange
    for _ in trange(9, desc='GUI Progressbar', leave=True):
        pass

# Generated at 2022-06-14 13:43:43.654770
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from nose.tools import assert_equal
    from matplotlib.testing.decorators import cleanup
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    #from matplotlib.testing.compare import compare_images
    import os
    import shutil

    toolbar = mpl.rcParams['toolbar']
    mpl.rcParams['toolbar'] = 'None'

    @cleanup
    def test_tqdm_gui_display_():
        import tempfile
        from .std import tqdm

        tmp = tempfile.mkdtemp()

# Generated at 2022-06-14 13:43:52.546028
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Unit test for method `close` of class `tqdm_gui`
    It checks if the progress bar is successfully closed.
    """
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    from .std import TqdmExperimentalWarning


# Generated at 2022-06-14 13:44:14.345979
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    # Following commands are used to clear any previous errors that may occur after the unit test is run
    import matplotlib.backends.backend_tkagg as tkagg
    import matplotlib.pyplot as plt
    tkagg.FigureCanvasTkAgg.blit = tkagg.FigureCanvasTkAgg.draw
    tkagg.FigureCanvasTkAgg.resize_event = lambda self: None
    plt.close('all')

    # Following commands will be used to run the unit test
    from tqdm import tqdm_gui, trange, tqdm
    from time import sleep

    for i in tqdm_gui(range(10), desc="Progress", leave=False):
        sleep(0.5)


# Generated at 2022-06-14 13:44:16.771939
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    import time
    for _ in tqdm(range(100)):
        time.sleep(0.01)


# Generated at 2022-06-14 13:44:24.330380
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    import shutil
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    from itertools import islice
    orig_stdout = sys.stdout
    sys.stdout = StringIO()

# Generated at 2022-06-14 13:44:28.785377
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    try:
        t = trange(100)
        t.close()
    except Exception as e:
        raise Exception('[Exception in tqdm_gui.close]: '
                        '{}'.format(e))
    # ... (to be continued)

if __name__ == '__main__':
    test_tqdm_gui_close()

# Generated at 2022-06-14 13:44:30.539330
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    t = tqdm_gui(range(2), leave=True)
    t.start()
    t.close()

# Generated at 2022-06-14 13:44:34.713184
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib.pyplot as plt
    g = tqdm_gui(total=100, dynamic_ncols=True)
    for i in g:
        g.display()
        g.update()
    g.close()
    plt.show()

# Generated at 2022-06-14 13:44:44.819477
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep

    try:
        for i in tqdm_gui(range(5)):
            sleep(2)
        for i in tqdm_gui(range(5), unit="it"):
            sleep(2)
        for i in tqdm_gui(range(5), unit="foos"):
            sleep(2)
        for i in tqdm_gui(range(5), unit="foos", unit_scale=True):
            sleep(2)

    except Exception as e:  # pragma: no cover
        raise e
    finally:
        tqdm_gui(leave=True)


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_gui()

# Generated at 2022-06-14 13:44:49.372047
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from matplotlib import pyplot as plt
    from numpy import random as rd
    from time import sleep
    pbar = tqdm_gui(total=200)

    for i in _range(200):
        sleep(rd.rand())
        pbar.update()

    pbar.close()
    plt.close('all')

# Generated at 2022-06-14 13:44:57.998118
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from collections import deque
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from .std import TqdmExperimentalWarning

    warn("GUI is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
    mpl.rcParams['toolbar'] = 'None'
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    xdata = deque([])
    ydata = deque([])
    zdata = deque([])
    line1, = ax.plot(xdata, ydata, color='b')
    line2, = ax.plot(xdata, zdata, color='k')
    ax.set_ylim(0, 0.001)

# Generated at 2022-06-14 13:45:07.532471
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    This unit test is not able to verify the actual behaviour
    of method `close`, it just runs it.
    """
    pbar = tqdm_gui(total=5)
    for i in _range(3):
        pbar.update(1)
    pbar.close()
    try:
        pbar.update(1)
    except ValueError:
        pass
    else:
        assert False, "ValueError should be raised when updating a closed tqdm"
    try:
        pbar.close()
    except ValueError:
        pass
    else:
        assert False, "ValueError should be raised when closing a closed tqdm"

# Generated at 2022-06-14 13:45:32.781824
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    with tqdm(total=1) as t:
        t.clear()

# Generated at 2022-06-14 13:45:36.761948
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    """
    Simply verify that the tqdm_gui class constructor can run.
    """
    with tqdm_gui(total=10) as t:
        t.update()
    # Do not close the plot, too annoying
    t.close()



# Generated at 2022-06-14 13:45:38.126645
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    t = tqdm_gui(0, file=None)
    t.close()

# Generated at 2022-06-14 13:45:45.285576
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from matplotlib import pyplot as plt
    from unittest import TestCase, main

    class Test(TestCase):
        def setUp(self):
            if not plt.get_backend():
                plt.switch_backend('agg')

        def tearDown(self):
            if self.plt is not None:
                self.plt.close()
                self.plt = None

        def test_tqdm_gui_close(self):
            from tqdm.gui import tqdm
            from time import sleep
            self.plt = plt
            for i in tqdm(range(1)):
                sleep(0.05)
            self.plt = None

    main()

# Generated at 2022-06-14 13:45:56.377370
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Testing tqdm_gui close method.
    """
    import matplotlib.pyplot as plt
    import matplotlib

    fig = plt.figure()
    fig.canvas.set_window_title("tqdm_gui_close test")

    # Should be closed when kwarg "leave" is not set to True
    tqdm_gui(total=10, leave=False).close()
    plt.show(block=False)
    assert not fig.canvas.get_window_title(), "Window title was not changed."

    # Should NOT be closed when kwarg "leave" is set to True
    tqdm_gui(total=1, leave=True).close()
    plt.show(block=False)

# Generated at 2022-06-14 13:46:01.789166
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    with tqdm_gui(total=10) as t:
        for i in range(5):
            t.update()
            t.display()
        t.n = 7
        t.display()

if __name__ == '__main__':
    test_tqdm_gui()

# Generated at 2022-06-14 13:46:05.225823
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    """Test that tqdm_gui constructor can be used"""
    with tqdm_gui(total=100) as pbar:
        pbar.display()
        for i in range(0, 100):
            pass

# Generated at 2022-06-14 13:46:13.023950
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    n = 1000000
    #with tqdm_gui(total=n) as pbar:
    #    for i in range(n):
    #        pbar.update()
    #    pbar.close()
    #    pbar.clear()
    with tqdm_gui(total=n) as pbar:
        for i in _range(n):
            pbar.update()
        pbar.close()
        pbar.clear()


if __name__ == "__main__":
    test_tqdm_gui()

# Generated at 2022-06-14 13:46:13.978332
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    assert tqdm_gui.clear(1) == None

# Generated at 2022-06-14 13:46:15.352475
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from .tests import test_cls
    test_cls(tqdm_gui)

# Generated at 2022-06-14 13:47:04.646732
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    with tqdm_gui(5) as t:
        for i in t:
            t.set_postfix(sum=i, curr=i + 1)

# Generated at 2022-06-14 13:47:08.399383
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    # Input values
    args, kwargs = (), {}

    # Creating a new object of class tqdm_gui
    tqdm_ob = tqdm_gui()
    # Calling tqdm_ob.clear
    tqdm_ob.clear(*args, **kwargs)

# Generated at 2022-06-14 13:47:10.013658
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    t = tqdm_gui()
    t.close()


# Generated at 2022-06-14 13:47:21.329262
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib.pyplot as plt
    import numpy as np
    c_func = tqdm_gui.display
    # test values
    n = 10
    cur_t = 10.0
    elapsed = 10.0
    delta_it = 10
    delta_t = 10.0
    # test variables
    t = tqdm_gui()
    t.total = n
    t.start_t = cur_t - 10
    t.n = n - 10
    t.last_print_n = n - 10
    t.last_print_t = cur_t - 10
    t.ax = plt.axes()
    t.line1 = plt.plot(np.arange(10), np.arange(10))[0]

# Generated at 2022-06-14 13:47:30.221377
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep
    from random import uniform
    from numpy import random
    from pylab import close


# Generated at 2022-06-14 13:47:39.298228
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from tqdm.auto import trange
    import re
    # the following is guaranteed to be silent;
    #   it only fails with an AttributeError
    with trange(1) as t:
        t.close()
        t.close()
        t.close()
    tqdm_gui_close_patched = re.findall(r"<class 'tqdm.gui._tqdm_gui.tqdm_gui'>",
                                        str(tqdm_gui.__bases__))
    assert tqdm_gui_close_patched

# Generated at 2022-06-14 13:47:50.198451
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .tqdm import __version__ as V
    from matplotlib.testing.decorators import cleanup

    if not V[:1] == '2':
        return  # expected version format: "2.x.y"
    # noinspection PyUnusedLocal
    @cleanup
    def unit_test_display():
        import matplotlib.pyplot as plt
        import numpy as np

        with tqdm_gui(total=100) as pbar:
            for i in _range(100):
                pbar.display()
                plt.pause(1e-5)
                plt.draw()

        # FLAKY: the following 2 tests fail on Travis (but not locally)
        # with tqdm(total=100) as pbar:
        #     for i in range(1, 101):

# Generated at 2022-06-14 13:47:56.296245
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from .utils import _range

    with tqdm_gui(total=10) as t:
        for i in _range(10):
            t.update()


if __name__ == "__main__":
    from .utils import _range
    with tqdm_gui(total=10) as t:
        for i in _range(10):
            t.update()

# Generated at 2022-06-14 13:48:07.284222
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from matplotlib.testing.compare import compare_images

    import io
    import os
    import sys
    import tempfile
    import matplotlib.pyplot as plt
    import matplotlib.testing.decorators as mpl_decorators
    # import matplotlib.test.compare as mpl_compare

    # Importing a non-existent optional dependency doesn't raise error
    if 'PYTEST_CMD' in os.environ:  # pragma: pytest no cover
        return

    # Ignore warnings in Pytest since we are testing a failed import here
    pytest_path = os.path.dirname(os.path.abspath(__file__))

# Generated at 2022-06-14 13:48:10.855162
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    import time
    args = list(range(10))
    for i in tqdm(args):
        time.sleep(0.1)


if __name__ == '__main__':
    test_tqdm_gui()

# Generated at 2022-06-14 13:49:52.361062
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    try:
        from matplotlib import pyplot as plt
    except ImportError:
        return
    with tqdm_gui(total=1000) as t:
        for _ in _range(1000):
            t.clear()
            if not plt.fignum_exists(t.fig.number):
                raise AssertionError("fig not closed")
            if not plt.get_fignums():
                raise AssertionError("window not shown")
            t.update()
            if not plt.fignum_exists(t.fig.number):
                raise AssertionError("fig not closed")
            if not plt.get_fignums():
                raise AssertionError("window not shown")


if __name__ == '__main__':
    test_tqdm_gui_clear

# Generated at 2022-06-14 13:50:01.210105
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    """Test the constructor of the tqdm class"""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        # skip the test if matplotlib is not available
        return
    from .utils import _supports_unicode, format_sizeof, format_interval
    from .std import tqdm as std_tqdm
    from .std import TqdmTypeError, TqdmKeyError, TqdmDeprecationWarning

    ncols = 60  # depends on the terminal size and the font used
    nrows = 1

    class TqdmHandler(object):
        """Dummy handler for all tqdm functions."""

        @staticmethod
        def write(s):
            """Dummy write method."""
            pass


# Generated at 2022-06-14 13:50:08.078299
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from .std import TestCase
    from .std import TestLogger
    from .std import StringIO
    import matplotlib.pyplot as plt
    import sys
    import time

    class _T(TestCase):
        def setUp(self):
            self.old_stdout = sys.stdout
            self.old_plt = plt
            plt.ioff()
            plt.close('all')
            self.mock_stdout = StringIO()
            sys.stdout = self.mock_stdout

        def tearDown(self):
            sys.stdout = self.old_stdout
            plt.close('all')
            plt.ion()

        def test_tqdm_gui_display(self):
            plt.close('all')
           

# Generated at 2022-06-14 13:50:12.180347
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    t = tqdm_gui(total=10)
    t.update_to(10)

    toolbar = t.mpl.rcParams['toolbar']
    t.close()

    assert t.mpl.rcParams['toolbar'] == toolbar
    assert t.disable

# Generated at 2022-06-14 13:50:20.961297
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    with tqdm(total=10) as t:
        t.clear()
    with tqdm(total=10) as t:
        for i in range(10):
            t.update()


if __name__ == '__main__':
    # handle_interrupt() # Deprecated

    from time import time, sleep

    def my_func():
        t = time()
        total = 30
        for i in tqdm_gui(total=total, smoothing=0.5, leave=True):
            sleep(0.05)
        print((time() - t) / total)

    def my_train():
        from numpy import random
        t = time()
        total = 1e3
        x = []
        y = []

# Generated at 2022-06-14 13:50:24.746362
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    from time import sleep
    from sys import version_info

    with tqdm(total=10) as t:
        for i in range(10):
            if version_info.major == 2:
                sleep(.2)
            else:
                sleep(.25)
            t.update(1)

# Generated at 2022-06-14 13:50:34.531979
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    import time
    with tqdm_gui(total=10) as pbar:
        for i in range(5):
            pbar.clear()
            time.sleep(1)
            pbar.update(2)


if __name__ == "__main__":
    from time import sleep as time_sleep
    for i in tgrange(15):
        time_sleep(0.01)
        if i == 5:
            continue
    for i in tgrange(15):
        time_sleep(0.01)
        if i == 10:
            continue
    for i in tqdm(["a", "b", "c", "d"]):
        time_sleep(0.01)
    try:
        from time import monotonic
    except ImportError:
        from time import time as monotonic
   

# Generated at 2022-06-14 13:50:41.597465
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    # simple case
    t = tqdm_gui(iterable=range(10), smoothing=0)
    for i in t:
        t.display()
    t.close()

    # with smoothing
    t = tqdm_gui(iterable=range(10), smoothing=0.90)
    for i in t:
        t.display()
    t.close()

    # no widget (for easier testing)
    t = tqdm_gui(iterable=range(10), smoothing=0.90, leave=True)
    for i in t:
        t.display()
    t.close()

# Generated at 2022-06-14 13:50:45.588628
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from time import sleep
    from numpy import random

    t = tqdm_gui(total=100)
    for i in _range(10):
        # do some work
        sleep(random.randint(1, 10) * .1)
        n = random.randint(10)
        t.update(n)
    t.close()

# Generated at 2022-06-14 13:50:48.387215
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    with tqdm_gui(total=10) as t:
        for i in range(10):
            t.update()
            t.clear()