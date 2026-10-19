

# Generated at 2022-06-14 13:43:10.276596
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from tempfile import mkstemp
    from os import close, remove
    fd, fname = mkstemp()
    close(fd)

    with tqdm_gui(total=1000) as t:
        for i in _range(10):
            t.update(i)
            t.display()
            plt.savefig(fname)

    remove(fname)
    plt.close()
    del t
    mpl.use('Agg')


if __name__ == "__main__":
    test_tqdm_gui_display()

# Generated at 2022-06-14 13:43:17.702305
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from .std import _term_move_up
    from .utils import _environ_cols_wrapper

    def do_test():
        """
        Does the job.
        """
        # Code run on initialization
        with tqdm_gui(total=2) as t:
            t.display = lambda **kwargs: False
            assert len(t.format_dict) > 0  # check presence of attribute

            # Code run on class instantiation
            with tqdm(total=2) as t2:
                t2.display = lambda **kwargs: False

                # Code run on exit
                std_tqdm.write = lambda s, **kw: True
                t.close()
                t2.close()
                warn("GUI is experimental/alpha", TqdmExperimentalWarning,
                     stacklevel=3)

# Generated at 2022-06-14 13:43:19.338244
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from .gui import tqdm_gui
    t = tqdm_gui(total=100, leave=True, disable=True)
    for _ in t:
        t.display()
        t.close()

# Generated at 2022-06-14 13:43:22.456726
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    for i in tqdm_gui(iterable=_range(1000)):
        pass


if __name__ == "__main__":  # pragma: no cover
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:29.038678
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    from time import sleep
    from numpy.random import random
    import gc
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", Warning)
        try:
            from ipykernel.iostream import IOPub
            IOPub.clear_instance()
        except:
            pass

    def test_close_refcounts(interval=0, gui=True):
        # Fetch current number of tqdm instances
        import sys

        gc.collect()
        # tqdm._instances = []
        instances = len(tqdm_gui._instances)

        # Create and destroy tqdm instances and make sure all are properly
        #   destroyed once the loop finishes

# Generated at 2022-06-14 13:43:32.443497
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from time import sleep

    t = tqdm_gui(total=10)
    for i in range(10):
        sleep(0.02)
        t.update()
    t.close()

# Generated at 2022-06-14 13:43:42.786560
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    try:
        from collections import deque
    except ImportError:
        return
    try:
        import matplotlib as mpl
        import matplotlib.pyplot as plt
    except ImportError:
        return

    with tqdm_gui(total=100, postfix={"var": "test"}, ncols=100) as t:
        for _ in t:
            assert isinstance(t.xdata, deque)
            assert isinstance(t.ydata, deque)
            assert isinstance(t.zdata, deque)
            assert isinstance(t.mpl, mpl.__class__)
            assert isinstance(t.plt, plt.__class__)
            assert t.postfix == {"var": "test"}

# Generated at 2022-06-14 13:43:47.998672
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from .std import tqdm
    from .std import tnrange
    from .utils import open
    from .gui import tqdm, tgrange, trange

    for t in (tqdm, tgrange, trange):
        with open(__file__, 'rb') as f:
            for _ in t(f, total=1000):
                pass

# Generated at 2022-06-14 13:43:59.111922
# Unit test for method close of class tqdm_gui

# Generated at 2022-06-14 13:44:07.682607
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from tqdm.gui import tqdm
    from matplotlib import pyplot as plt
    import pylab

    # create a figure
    fig = plt.figure()
    # add an axes to it
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 0.001)
    # add a line to the axes
    line, = ax.plot([], [], color='k')
    # set the figure to "interactive" mode
    plt.ion()
    # show the figure
    plt.show(block=False)

    for k in tqdm(range(100)):
        line.set_data(k, k * 0.0001)
        # update the "data lim" of the figure
        ax

# Generated at 2022-06-14 13:44:24.741139
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Unit test of the method close of class tqdm_gui.
    """
    __test__ = {
        'tqdm_gui close': test_tqdm_gui_close
    }

# Generated at 2022-06-14 13:44:32.212670
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import pandas as pd
    from pandas.util import testing as tm
    from .std import tqdm
    import numpy as np
    from random import randint

    # To improve test coverage, `tqdm.tqdm` is tested with the `tqdm_gui`.
    # The `tqdm_gui` will probably evolve with the `tqdm.tqdm`
    # because it shares a lot of the same code.

    a = tqdm(np.random.lognormal(size=10000, mean=3.0, sigma=0.7),
             leave=True, gui=True, miniters=1000)
    assert isinstance(a, tqdm_gui)

    # test_tqdm_gui_display -> test_tqdm_gui_display -> tqdm -> tr

# Generated at 2022-06-14 13:44:35.619325
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    t = tqdm_gui(total=1000)
    for i in t:
        pass
    t.close()


if __name__ == '__main__':
    test_tqdm_gui()

# Generated at 2022-06-14 13:44:44.132778
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    with tqdm_gui(total=10) as pbar:
        assert not pbar.disable
        pbar.close()
        assert pbar.disable


if __name__ == "__main__":
    from inspect import isfunction

    test_funcs = [obj for name, obj in list(globals().items())
                  if name.startswith('test_') and isfunction(obj)]
    for testfunc in test_funcs:
        try:
            print("{0}:".format(testfunc.__name__))
            testfunc()
            print("[pass]")
        except:
            print("[fail]")

# Generated at 2022-06-14 13:44:53.508429
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    import os
    import sys
    import warnings
    import subprocess as sp

    if os.environ.get('TRAVIS', None):
        # Travis-CI is not able to handle plots
        return

    from .utils import _term_move_up

    # Disable tqdm on other unit-tests & coverage
    os.environ['TQDM_DISABLE'] = '1'

    # Python GUI test
    if len(sys.argv) > 1:  # pragma: no cover
        # Unit tests for tqdm_gui
        # This is not supposed to be run from the unit-test suite
        from .gui import tqdm_gui

        def demo(**kwargs):
            import random
            import time

            random.seed(0)

# Generated at 2022-06-14 13:45:02.967431
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    try:
        plt = __import__('matplotlib').pyplot
    except ImportError:
        return
    with tqdm_gui(total=7) as pbar:
        for _ in range(5):
            pbar.clear()  # doesn't raise error
            pbar.update()
        pbar.close()


# Check that the imports work
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    with tqdm_gui(total=7) as pbar:
        for _ in range(5):
            pbar.clear()  # doesn't raise error
            pbar.update()
        pbar.close()

# Generated at 2022-06-14 13:45:13.391466
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    """
    Unit tests for class tqdm_gui.

    """
    try:
        from matplotlib.pyplot import close
    except ImportError:
        return

    import random
    random.seed(2)

    with tqdm_gui(total=20, desc="test-") as t:
        for i in tqdm_gui(range(20), ascii=True, desc="test-", leave=False):
            t.update(n=i+1)
            t.set_description("%d" % (i + 1))
            close(t.fig)
            t.display()

if __name__ == "__main__":  # pragma: no cover
    test_tqdm_gui()

# Generated at 2022-06-14 13:45:21.722704
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from .std import TqdmDefaultWriteLock
    from .utils import _range

    t = tqdm_gui(_range(100), leave=True, ncols=23, ascii=True)
    # mock the tqdm class
    t._time = lambda: 0.0
    t.last_print_n = 0
    t.last_print_t = 0
    t.start_t = 0
    t.total = 100
    t.update(10)

# Generated at 2022-06-14 13:45:23.518454
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from time import sleep
    for i in tqdm(range(10)):
        sleep(0.1)

# Generated at 2022-06-14 13:45:35.619085
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    try:
        from collections import deque
        from matplotlib import pyplot as plt
        from matplotlib import rcParams
        from matplotlib import grid
        from threading import Thread
        from time import sleep
    except ImportError:
        return

    def w(*args, **kwargs):
        with tqdm_gui(*args, **kwargs) as pbar:
            for _ in pbar:
                sleep(0.05)

    old_toolbar = rcParams['toolbar']
    rcParams['toolbar'] = 'None'
    rcParams['savefig.directory'] = '/tmp'
    rcParams['savefig.format'] = 'png'
    old_interactive = plt.isinteractive()
    plt.ion()
    # keep references to instances
    tqdm_