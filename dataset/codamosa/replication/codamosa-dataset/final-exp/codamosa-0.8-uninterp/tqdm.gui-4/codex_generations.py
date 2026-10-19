

# Generated at 2022-06-14 13:43:00.977508
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import sys
    import nose.tools as nt
    from nose.tools import assert_equal
    from nose.tools import assert_not_equal
    from nose.tools import assert_dict_equal
    from nose.tools import assert_dict_contains_subset
    from nose.tools import assert_in
    from nose.tools import assert_not_in
    from nose.tools import assert_true
    from nose.tools import assert_false
    from nose.tools import assert_raises
    from nose.tools import assert_raises_regexp
    from nose.tools import assert_almost_equal
    from nose.tools import assert_not_almost_equal
    from nose.tools import assert_items_equal
    from nose.tools import assert_greater
    from nose.tools import assert_greater_equal

# Generated at 2022-06-14 13:43:12.241875
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep
    from matplotlib import pyplot as plt

    with tqdm_gui(total=20) as t:
        for i in range(20):
            sleep(0.1)
            t.update(i)

    with tqdm_gui(unit='s', total=20) as t:
        for i in range(20):
            sleep(1)
            t.update(i)

    with tqdm_gui(unit='s', unit_scale=True, total=20) as t:
        for i in range(20):
            sleep(1)
            t.update(i)

    # Don't leave the figure open
    t = tqdm_gui(total=20, leave=False, unit='s')

# Generated at 2022-06-14 13:43:19.812608
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    import time
    from os import getpid
    with tqdm_gui(total=1.0, unit='GB', unit_scale=True) as pbar:
        time.sleep(1.0)
        pbar.write('the process id is {0}'.format(getpid()))
        for _ in _range(100):
            pbar.update(0.01)
            time.sleep(0.01)


if __name__ == "__main__":
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:22.539890
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    try:
        for i in trange(1):
            pass
    except Exception as e:
        assert e.args[0] == "clear() not implemented!"
        pass
    else:
        assert False

# Generated at 2022-06-14 13:43:25.987707
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Simple unit tests for tqdm_gui.close() method.
    """
    # TODO: write unit tests for tqdm_gui.close() method
    # + create a test for restored toolbars
    pass

# Generated at 2022-06-14 13:43:29.765080
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep
    import matplotlib.pyplot as plt

    with tqdm(total=100) as pbar:
        for i in range(10):
            sleep(0.1)
            pbar.update(10)

    # Allow the GUI to clean up before exiting
    plt.close()

# Generated at 2022-06-14 13:43:36.846997
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import sys
    import time
    t = tqdm_gui(1)
    t.start()
    t.display()
    t.update()
    t.display()
    if sys.flags.interactive:
        # The following lines should be the only ones of their kind in the
        # whole project (except for the one in test_tqdm)
        time.sleep(0.7)  # ensure progressbar is visible

# Generated at 2022-06-14 13:43:39.522137
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    """Test the Matplotlib GUI version of tqdm."""
    from time import sleep

    for i in tqdm(range(10)):
        sleep(.25)

# Generated at 2022-06-14 13:43:46.608552
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    """ Test GUI display function """
    from .utils import FormatMeter, FormatCustomText
    from .std import TqdmKeyError, TqdmTypeError, \
        tqdm_BASE, tqdm_NOTEBOOK, tqdm_PYGLET, tqdm_CURSES, tqdm_STDOUT

    class TqdmTypeErrorMock(TqdmTypeError):
        """ No-op `TqdmTypeError` with mock `__str__`"""
        def __str__(self):
            return str(self.__class__.__name__) + ": " + self.msg

    def exc(fun, *args, **kwargs):
        """ Return the exception str returned by `fun` """
        try:
            fun(*args, **kwargs)
        except Exception as e:
            return

# Generated at 2022-06-14 13:43:51.762791
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from sys import stderr
    from .std import tqdm
    from .utils import _term_move_up
    import matplotlib

    matplotlib.use('Agg')
    try:
        t = tqdm_gui(total=100, file=stderr)
        for i in range(10):
            t.update(10)
            _term_move_up()
    finally:
        t.close()

# Generated at 2022-06-14 13:44:13.186310
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    try:
        from unittest import TestCase
    except ImportError:
        from unittest2 import TestCase
    import sys
    import functools
    import mock

    class TqdmGuiTest(TestCase):
        @mock.patch('tqdm.gui.tqdm_gui.tqdm_gui._instances')
        @mock.patch('tqdm.gui.tqdm_gui.tqdm_gui._decr_instances')
        def test_clear(self, decr_instances, _instances):
            ig = tqdm_gui(None)
            ig.disable = False
            ig.clear()
            _instances.assert_called_once_with(ig)
            if sys.version_info >= (3,):
                decr_instances.assert_

# Generated at 2022-06-14 13:44:19.769776
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import sys
    if sys.version_info[0] == 3:
        from io import StringIO
    else:
        from StringIO import StringIO

    with StringIO() as our_file, tqdm(total=10, file=our_file, leave=True) as t:
        for i in _range(10):
            t.update()

    assert our_file.getvalue() == ""



# Generated at 2022-06-14 13:44:28.438768
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """Test method close of class tqdm_gui"""
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    # Remember if external environment uses toolbars
    toolbar = mpl.rcParams['toolbar']
    mpl.rcParams['toolbar'] = 'None'

    # Remember if external environment is interactive
    wasion = plt.isinteractive()
    plt.ion()

    for i in tqdm_gui(range(100)):
        pass

    # Restore toolbars
    mpl.rcParams['toolbar'] = toolbar

    # Return to non-interactive mode
    if not wasion:
        plt.ioff()

# Generated at 2022-06-14 13:44:38.766400
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    tqdm.write = lambda msg: None
    # Either matplotlib or PySide is required
    try:
        from PySide.QtCore import QCoreApplication
    except ImportError:
        tq = tqdm(["a", "b", "c"], disable=True)
    else:
        tq = tqdm(["a", "b", "c"])
    assert tq is not None

    # Everything is disabled
    tq.disable = True
    n = tq.n
    n_check = n
    tq.display()
    assert n == n_check

    # Now disable the GUI
    tq.gui = False
    n = tq.n
    n_check = n

# Generated at 2022-06-14 13:44:41.886227
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from .gui import tqdm as tqdm_gui
    from time import sleep
    for i in tqdm_gui(range(4)):
        sleep(0.5)
    assert not tqdm._instances

# Generated at 2022-06-14 13:44:47.794814
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import numpy as np, time

    x = np.linspace(0, 1, 200)
    t = tqdm_gui(x, gui=True)
    i = -1
    while True:
        time.sleep(0.02)
        i += 1
        if i >= len(x):
            break
        t.display()
        t.update(1)
    t.close()
    return t, i

# Generated at 2022-06-14 13:44:50.772460
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    for _ in tqdm([1, 2]):
        pass

# Generated at 2022-06-14 13:44:57.804054
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    t = tqdm_gui(100)
    t.close()


if __name__ == '__main__':
    import time
    import multiprocessing as mp

    def worker(q, n):
        with tqdm(total=n) as t:
            for i in range(n):
                t.update()
                time.sleep(0.01)
        q.put(n)

    for i in trange(20):
        q = mp.Queue()
        p = mp.Process(target=worker, args=(q, 100))
        p.start()
        p.join()
        print(i, q.get())
    input()

# Generated at 2022-06-14 13:45:02.119632
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from time import sleep
    with tqdm_gui(total=100) as t:
        for i in _range(100):
            sleep(0.1)
            t.update()

        t.clear()

# Generated at 2022-06-14 13:45:03.748914
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    t = tqdm_gui([10])
    t.display()
    t.close()