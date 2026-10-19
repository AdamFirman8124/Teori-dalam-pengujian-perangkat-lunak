

# Generated at 2022-06-14 13:42:57.397435
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    """
    Unit test for class tqdm_gui
    """
    t = tqdm_gui(total=2, miniters=1)
    t.display()
    t.update()
    t.display()
    t.close()


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:03.330965
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    try:
        from time import sleep
        from matplotlib import pyplot as plt
        for i in trange(4, desc='1st loop', miniters=1, mininterval=0.2):
            for j in trange(5, desc='2nd loop', leave=False, mininterval=0.1):  # pragma: no cover
                sleep(0.1)
        plt.ioff()
        plt.show()
    except (ImportError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:13.873932
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from time import sleep
    from nose.tools import (assert_true, raises)
    from sys import modules
    from os import devnull
    from io import StringIO
    with open(devnull, 'w') as fout:
        from warnings import filterwarnings
        filterwarnings("ignore", category=tqdm.TqdmDeprecationWarning)
        # Jupyter
        if 'ipykernel' in modules:
            modules['tkinter'] = modules['IPython.kernel.zmq.inprocess.tk']
            modules['tkinter.ttk'] = modules['IPython.kernel.zmq.inprocess.ttk']

        # Make a simple progress bar
        pbar = tqdm_gui(total=100)

# Generated at 2022-06-14 13:43:23.104765
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from inspect import getsourcefile
    from os.path import abspath, dirname, join
    import sys

    sys.path.insert(0, dirname(dirname(abspath(getsourcefile(lambda: 0)))))

    import tests
    import tests.utils
    import time

    # If Matplotlib is not installed, the decorator would be disabled
    runtest = tests.utils.is_module_installed("matplotlib")
    if runtest:
        with tests.utils.DisableLogger():
            with tqdm(total=100) as t:
                for i in range(100):
                    time.sleep(0.01)
                    t.update()
# test_tqdm_gui_close()

# Generated at 2022-06-14 13:43:29.654258
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    for i in trange(4):
        for j in trange(5):
            pass


if __name__ == '__main__':  # pragma: no cover
    from time import sleep
    for i in tqdm(range(3), disable=True):
        print(i)
    for i in tqdm(range(10)):
        sleep(0.1)
    f = tqdm(range(10))
    for i in f:
        if i == 5:
            f.close()
        sleep(0.1)

# Generated at 2022-06-14 13:43:40.986170
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    import matplotlib.pyplot as plt
    import time
    with tqdm_gui(total=10, unit="sec", desc="wait") as pbar:
        for _ in pbar:
            time.sleep(1)
            pbar.update()

    # plt.show()
    time.sleep(1)
    plt.close()
    with tqdm_gui(desc="wait") as pbar:
        for _ in pbar:
            time.sleep(1)
            pbar.update()
    plt.close()
    time.sleep(1)
    with tqdm_gui(total=10, unit="sec", desc="wait") as pbar:
        for _ in pbar:
            time.sleep(1)
            pbar.update()
    plt.close()
    time

# Generated at 2022-06-14 13:43:50.689593
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    """Runs tqdm_gui with all arguments set."""
    try:
        from matplotlib import pyplot as plt
    except ImportError as e:
        return
    # Everything is tested in tqdm, this test is just to check the import,
    # and all possible arguments for tqdm_gui.
    with tqdm_gui(10,
                  disable=True,
                  ascii=True,
                  ncols=3,
                  miniters=2,
                  mininterval=0.5,
                  maxinterval=1.0,
                  bar_format="{l_bar}{bar}{r_bar}",
                  initial=4) as t:
        for i in t:
            t.set_description("TEST")

# Generated at 2022-06-14 13:43:54.526594
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui(): # pragma: no cover
    """
    Minimalist test for interactive mode
    """
    with tqdm_gui(total=1, leave=True) as pbar:
        pbar.update(1)

# Generated at 2022-06-14 13:44:01.848302
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    """Check if closing a GUI is possible"""
    import matplotlib.pyplot as plt  # isort:skipexport
    for i in tgrange(0.1, 0, 0.01):
        plt.pause(1e-6)
        plt.figtext(0, 0, i)

if __name__ == '__main__':  # pragma: no cover
    test_tqdm_gui_close()

# Generated at 2022-06-14 13:44:06.874578
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from matplotlib import pyplot as plt
    # Setup
    if tqdm_gui.gui:
        old_toolbar = plt.rcParams['toolbar']
        old_interactive = plt.isinteractive()
    # Test
    tqdm_gui.close()
    # Teardown
    if tqdm_gui.gui:
        plt.rcParams['toolbar'] = old_toolbar
        if not old_interactive:
            plt.ioff()

# Generated at 2022-06-14 13:44:23.087872
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from time import sleep
    try:
        t = tqdm_gui(10)
        for i in t:
            sleep(1)
            t.clear()
    except Exception:
        raise AssertionError("tqdm_gui method clear() is not working properly.")

# Generated at 2022-06-14 13:44:26.338175
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from numpy import arange
    from time import sleep
    with tqdm(total=100) as pbar:
        for i in arange(100):
            pbar.update(1)
            if i % 10 == 0:
                sleep(1)


if __name__ == "__main__":  # pragma: no cover
    test_tqdm_gui_display()

# Generated at 2022-06-14 13:44:30.066891
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    n = 100
    x = list(tqdm_gui(range(n), desc='test', unit='it',
                      unit_scale=True, miniters=1, mininterval=0.01,
                      maxinterval=0.01))
    assert x == list(range(n)), repr(x)


# Generated at 2022-06-14 13:44:40.585848
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    import matplotlib.pyplot as plt
    t = tqdm_gui(total=None)  # #81
    cmd = 'command'
    cmd += '&' * 30000
    cmds = cmd.split('&')
    num_cmds = len(cmds)
    for i, c in enumerate(tqdm(cmds)):
        for _ in range(100):
            pass
        frac = i / num_cmds
        t.n = frac * 100
        t.set_description(c[:30])
    t.close()
    assert 'xdata' in dir(t)
    assert 'ydata' in dir(t)
    assert 'line1' in dir(t)
    assert 'ax' in dir(t)
    assert 'fig'

# Generated at 2022-06-14 13:44:50.528277
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():  # pragma: no cover
    import warnings
    from sys import version_info
    from unittest import TestCase

    class TqdmGuiClearTest(TestCase):
        if version_info.major == 2:
            long_message = True  # allow long messages in assertWarns

        def test_tqdm_gui_clear(self):
            with warnings.catch_warnings(record=True) as w:
                with tqdm(range(3)) as pbar:
                    pbar.clear()
                self.assertEqual(len(w), 1)
                self.assertTrue(issubclass(w[0].category, RuntimeWarning))


# Generated at 2022-06-14 13:44:55.894653
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    import sys
    import time
    from tqdm.gui import tqdm
    # if len(sys.argv) > 1 and
    # sys.argv[1] == '--version':
    # from .version import __version__
    # print(__version__)
    # exit()

    for i in tqdm(xrange(1000)):
        for _ in range(1000):
            pass
        time.sleep(1)


# Generated at 2022-06-14 13:45:01.219994
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from matplotlib import pyplot as plt
    from time import sleep

    for i in tqdm_gui(range(10)):
        sleep(.1)
    plt.show()

if __name__ == "__main__":
    test_tqdm_gui()

# Generated at 2022-06-14 13:45:05.117622
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    """test_tqdm_gui_clear"""
    # TODO: Make test quiet
    from tqdm.gui import trange
    from time import sleep

    with trange(10) as t:
        for i in range(10):
            sleep(0.1)
            t.update()
            t.clear()

# Generated at 2022-06-14 13:45:10.894997
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    for _ in tqdm(range(2), leave=True, gui=True):
        for _ in tqdm(range(3), leave=True, gui=True):
            t = tqdm(range(2), leave=True, gui=True)
            for _ in t:
                pass
            t.close()
    tqdm(range(2), leave=True, gui=True).close()

# Generated at 2022-06-14 13:45:18.294550
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    for _ in tqdm_gui(range(100)):
        pass
    # test if method clear is implemented
    # (i.e is not empty and raises AttributeError)
    try:
        tqdm_gui(range(10)).clear()
    except AttributeError as e:
        msg = str(e)
        raise AttributeError("{0}. Are you sure to use the "
                             "right tqdm version{1}?".format(msg,
                             " (e.g. `pip install tqdm`)" if
                             msg == "'tqdm_gui' object has no attribute 'clear'"
                             else ""))