

# Generated at 2022-06-14 13:42:54.397839
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover

    t = tqdm_gui(total=100)
    for _ in range(100):
        t.update()
    t.close()

    t = tqdm_gui(total=100)
    for x in t:
        pass

    t = tqdm_gui()
    for x in t:
        pass

# Generated at 2022-06-14 13:42:56.606023
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from .utils import _range
    t = tqdm_gui(iterable=_range(1))
    t.update(1)
    t.close()

# Generated at 2022-06-14 13:43:03.255190
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    import sys
    import time

    t = tqdm_gui(total=70, smoothing=0)
    time.sleep(0.1)
    t.update(1)
    time.sleep(0.3)
    t.update(10)
    time.sleep(0.2)
    t.update(30)
    time.sleep(0.1)
    t.update(15)
    time.sleep(0.2)
    t.update(10)
    time.sleep(0.1)
    t.update(4)
    t.close()
    sys.exit(0)



# Generated at 2022-06-14 13:43:13.799083
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from random import random
    from time import sleep
    from itertools import repeat, chain

    def main(total=10, length=20):
        q = tqdm_gui(total=total)
        for i, _ in enumerate(repeat(None, total)):
            q.display(length=length)
            sleep(1. * random())
            q.update()

        # Test `leave` option
        q = tqdm_gui(total=total, leave=True)
        for i, _ in enumerate(repeat(None, total)):
            q.display(length=length)
            sleep(1. * random())
            q.update()

        # Test unknown length
        q = tqdm_gui()

# Generated at 2022-06-14 13:43:18.620226
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    try:
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        mpl.use('Agg')
        a = tqdm_gui(iterable=range(100), leave=False)
        plt.pause(1e-9)
    finally:
        a.close()

# Generated at 2022-06-14 13:43:23.261619
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib
    from matplotlib import pyplot
    from matplotlib import rcParams
    toolbar = rcParams['toolbar']
    # Test that tgrange restores toolbar state when closed
    with tgrange(1):
        rcParams['toolbar'] = 'toolbar'
    assert rcParams['toolbar'] == toolbar, 'BUG: tqdm_gui._close() should restore matplotlib.rcParams[\'toolbar\']'
    # Test that tgrange restores toolbars state when closed, even if raised a KeyboardInterrupt
    try:
        with tgrange(1):
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        assert matplotlib.is_interactive() is False, 'BUG: tqdm_gui._close() should restore matplotlib.is_interactive()'
       

# Generated at 2022-06-14 13:43:31.939676
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from .std import TqdmExperimentalWarning

    warn("GUI is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
    # pylint: disable=protected-access
    t = tqdm_gui(total=10)
    assert t.start_t  # already set
    assert t.last_print_n == 0
    assert t.last_print_t == t.start_t
    assert (t.xdata, t.ydata, t.zdata, t.line1, t.line2, t.ax,
            t.hspan)
    assert not t.disable
    assert t._instances == [t]
    assert t.leave
    assert t.iterable is None
    assert t.miniters == 0
    assert t._lock is None
   

# Generated at 2022-06-14 13:43:38.598873
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Test the method close of class tqdm_gui.
    """
    # Initialize a tqdm_gui instance with a disable = True value
    tqdm_gui_test = tqdm_gui(disable = True)
    # Test if the method close change the disable attribute of tqdm_gui_test
    tqdm_gui_test.close()
    assert tqdm_gui_test.disable == True

# Generated at 2022-06-14 13:43:46.168419
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """
    Unit tests for `display` method of `tqdm_gui` (Matplotlib GUI)
    """
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    import numpy as np
    from PIL import Image
    from time import sleep

    def nptolist(arr):
        return arr.tolist()

    def listtonp(arr):
        return np.array(arr)

    def listtoarr(arr):
        return np.asarray(arr)

    def get_data(xdata, ydata):
        return xdata, ydata

    def compare(a, b):
        return np.all(a == b)

    # Create a figure and get matplotlib canvas
    fig = plt.figure()
    canvas = FigureCanvasAgg(fig)
    #

# Generated at 2022-06-14 13:43:47.645162
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    t = tqdm(tgrange(1))
    t.close()