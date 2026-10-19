

# Generated at 2022-06-14 13:42:52.554800
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .std import TqdmDeprecationWarning
    from .std import TqdmExperimentalWarning

    import matplotlib.pyplot as plt

    warn("GUI is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
    warn("Display refreshes are white-listed; enable tqdm_gui.monitor_interval to improve performance",
         TqdmDeprecationWarning, stacklevel=2)

    # Prepare grid and lines
    plt.figure(figsize=(9, 2.2))
    ax = plt.subplot(111)
    ydata = plt.get_cmap('jet')([0.5])
    ydata[0][3] = 0.5
    plt.plot([], [], color=ydata[0])

# Generated at 2022-06-14 13:43:01.723238
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():  # pragma: no cover
    t = tqdm_gui(range(1))
    try:
        t.clear()
    except Exception as e:
        raise e


if __name__ == '__main__':  # pragma: no cover
    import time
    from random import random

    # Initialise
    t = tqdm_gui(total=1)
    # Update without any error
    for i in tqdm_gui(range(30)):
        t.update()
        time.sleep(0.03)
    # Update with error
    for i in tqdm_gui(range(30)):
        t.update(False)
        time.sleep(0.03)
    # Update with error break
    for i in tqdm_gui(range(30)):
        t.update(False)

# Generated at 2022-06-14 13:43:05.203745
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    """
    Tests `close` method of class `tqdm_gui`
    """
    t = tqdm_gui(0, 0)
    t.close()

# Generated at 2022-06-14 13:43:14.991201
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    # Construct a mock object
    class MagicMock:
        def __init__(self):
            self.mock = True
            self.func_calls = []

        def __getattr__(self, key):  # pragma: no cover
            def func_call(*args, **kwargs):
                self.func_calls.append([key, args, kwargs])
                return self
            return func_call
    mock = MagicMock()

    # Overwrite the display method with the mock object
    tq = tqdm_gui(total=None, disable=True)
    tq.display = mock.display

    # Call display
    tq.display()

    # Test the function calls of the mock object
    # The order of the function calls of the mock object is tested

# Generated at 2022-06-14 13:43:17.250160
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    progressbar = tqdm_gui(total=100)
    progressbar.clear()


# Generated at 2022-06-14 13:43:20.708406
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():  # pragma: no cover
    # testing clear method
    from .gui import tqdm_gui
    import time

    for _ in tqdm_gui(list(range(100))):
        time.sleep(0.1)



# Generated at 2022-06-14 13:43:24.527501
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from .auto import trange
    l = list(range(100))
    for _ in tqdm(l):
        a = 1
    for _ in tgrange(len(l)):
        a = 1

    with trange(10) as t:
        for i in t:
            a = 1
            if i > 2:
                break
            t.set_description("test%i" % i)


if __name__ == '__main__':  # pragma: no cover
    # python -m tqdm.gui
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:32.165602
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from io import StringIO
    io = StringIO()
    i, n = 0, 2

    with tqdm_gui(total=n, file=io) as t:
        t.display()
        assert (t.xdata == [0] and t.ydata == [0] and t.zdata == [0])

        t.update()
        t.display()
        i += 1
        assert (t.xdata == [0] and t.ydata == [1] and t.zdata == [1])

        t.update()
        t.display()
        i += 1
        assert (t.xdata == [0, 100] and t.ydata == [1, 1] and t.zdata == [1, 1])

# Generated at 2022-06-14 13:43:42.652625
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    try:
        from matplotlib.testing.decorators import image_comparison
    except ImportError:
        return
    # Note that matplotlib version has to be >= 2.0
    # to have the possibility to compare images
    # So this test is disabled by default,
    # and only works in CI builds
    import numpy as np
    import matplotlib.pyplot as plt

    @image_comparison(baseline_images=['tqdm_gui_display'],
                      extensions=['png'], style='default')
    def do_test():
        t = tqdm(total=100)
        for _ in range(10):
            t.update()
            plt.pause(0.1)
        for _ in range(50):
            t.update()

# Generated at 2022-06-14 13:43:51.899709
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from time import sleep
    try:
        from numpy import arange
        from numpy.random import rand
        nparange = arange
    except ImportError:
        from six.moves import range as nparange
    for i in tqdm(nparange(30), leave=True):
        sleep(0.1)
    for i in tqdm(nparange(30), leave=False):
        sleep(0.1)
        tqdm.write('i = ' + str(i))
    for i in tqdm(nparange(30), leave=False):
        sleep(0.1)
        tqdm.write('i = ' + str(i) + '\nj = ' + str(rand()) + '\nk = ' + str(rand()))

# Generated at 2022-06-14 13:44:07.202426
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    import time
    with tqdm_gui(total=10) as pbar:
        for i in range(10):
            pbar.clear()
            time.sleep(0.1)
            pbar.update()

# Generated at 2022-06-14 13:44:15.459425
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import sys
    import matplotlib.pyplot as plt
    import numpy as np
    sys.excepthook = lambda exctype, exc, tb: sys.__excepthook__(exctype, exc,
                                                                tb)
    try:
        tqdmg = tqdm_gui(total=100)
        # tqdmg = tqdm_gui(100)
        for x in tqdmg:
            if tqdmg.n > 50:
                tqdmg.total = None
            tqdmg.update(random.randint(-10, 40))
            if tqdmg.n >= 100:
                break
            sleep(random.random() * 0.01)
    finally:
        plt.close('all')

# Generated at 2022-06-14 13:44:22.040136
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from time import sleep
    from sys import stderr
    with tqdm_gui(total=10) as pbar:
        for _ in pbar:
            sleep(0.1)
    assert not pbar.disable
    pbar.close()
    assert pbar.disable
    pbar.display()  # should not fail
    pbar.update()  # should not fail
    pbar.close()  # should not fail
    assert pbar._instances == []
    assert stderr.isatty()



# Generated at 2022-06-14 13:44:27.373772
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    # pretend to be a Jupyter notebook
    get_ipython = lambda: None
    get_ipython.__class__ = type(
        '_DummyGetIPython', (object,),
        {'__getattr__': lambda self, key: key == 'kernel'})()

    get_ipython()  # trigger __getattr__
    # check that no error is raised outside of notebook
    tqdm_gui(total=10)


if __name__ == '__main__':
    test_tqdm_gui()
    tqdm_gui(total=10)
    tqdm_gui(total=10, dynamic_ncols=True)

# Generated at 2022-06-14 13:44:34.562695
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """Test display method of tqdm_gui class"""
    import matplotlib.pyplot as plt

    # Set interactive mode to False
    plt.ioff()

    # Instantiate tqdm_gui
    tgui = tqdm_gui(total=100, bar_format="{bar}")

    # Check draw
    tgui.display()
    plt.pause(0.01)
    for _ in range(4):
        tgui.update()
        plt.pause(0.01)
    plt.close(tgui.fig)

# Generated at 2022-06-14 13:44:40.440963
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    """Unit test for constructor of class tqdm_gui"""
    try:
        import matplotlib
        matplotlib.use('Agg')
    except ImportError:
        return
    t = tqdm_gui(total=1024, leave=True)
    assert isinstance(t, tqdm_gui)
    t.close()
    assert not isinstance(t, tqdm_gui)

# Generated at 2022-06-14 13:44:50.399131
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Unit test for method close of class tqdm_gui
    """
    TEST_TOOLBAR = 'tool'
    tqdm.mpl.rcParams['toolbar'] = TEST_TOOLBAR
    for wasion in (True, False):
        tqdm.wasion = wasion
        try:
            tqdm.plt  # pylint: disable=pointless-statement
        except AttributeError:
            tqdm.plt = tqdm.mpl.pyplot  # pylint: disable=attribute-defined-outside-init
        with tqdm(total=100, leave=True) as t:
            for _ in t:
                pass
        assert tqdm.mpl.rcParams['toolbar'] == TEST_TOOLBAR

# Generated at 2022-06-14 13:44:58.490003
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    # creating a test progressbar
    from tqdm.gui import trange
    from tqdm import tqdm
    from time import sleep
    from sys import argv

    # set total to None for iterable progressbar
    if len(argv) <= 1:
        total = 10
    else:
        total = None
    pbar = tqdm(list(range(total)), ncols=None, mininterval=1, miniters=1,
                total=total, unit=' it', unit_scale=True, ascii=True,
                disable=False)
    # save initial state to check against later
    xdata0 = pbar.xdata[:]
    ydata0 = pbar.ydata[:]
    zdata0 = pbar.zdata[:]
    hspan0 = pbar.hspan

# Generated at 2022-06-14 13:45:09.731578
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from time import sleep

    tk = tqdm_gui(total=100, leave=False)
    for _ in tk:
        sleep(0.01)
        tk.update()
        if tk.n >= 100:
            break
    tk.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    def run():
        import time
        try:
            from tqdm.std import tqdm
            tqdm = tqdm(total=100, desc='Testing tqdm_gui')
            for t in tqdm_gui(range(100)):
                tqdm.update()
                time.sleep(0.01)
        except KeyboardInterrupt:
            pass
        except AssertionError:
            run()
            time

# Generated at 2022-06-14 13:45:17.898825
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from tqdm.utils import _term_move_up
    from copy import deepcopy
    from os import linesep
    from sys import stdout

    def get_updated_stdout(tqdm_obj):
        """Return the updated stdout of tqdm instance by calling display()"""
        stdout._tqdm_old_write = stdout.write
        stdout.write = lambda x: True
        msg = tqdm_obj.format_dict['desc']
        tqdm_obj.display()
        stdout.write = stdout._tqdm_old_write
        del stdout._tqdm_old_write
        return linesep + msg + linesep

    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
   