

# Generated at 2022-06-14 13:43:00.941224
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from time import sleep
    total = 5

    with tqdm_gui(total=total, leave=False) as t:
        xdata = t.xdata
        ydata = t.ydata
        zdata = t.zdata
        ax = t.ax
        line1 = t.line1
        line2 = t.line2
        # instantaneous rate
        y = 10
        # overall rate
        z = 20
        # update line data
        xdata.append(100.0)
        ydata.append(y)
        zdata.append(z)

        # Discard old values
        xmin, xmax = ax.get_xlim()
        if 100.0 > xmax:
            xdata.popleft()
            ydata.popleft()

# Generated at 2022-06-14 13:43:12.200416
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    """Unit test for `tqdm_gui.close()`"""
    import gc
    import matplotlib.pyplot as plt
    import sys


# Generated at 2022-06-14 13:43:22.665242
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from time import sleep
    N = 1000

    # test empty
    pbar = tqdm_gui(total=N)
    pbar.clear()
    assert pbar.n == 0
    assert len(pbar.xdata) == 0
    assert len(pbar.ydata) == 0
    assert len(pbar.zdata) == 0

    # test after iteration
    pbar = tqdm_gui(total=N)
    for _ in pbar:
        pass
    pbar.clear()
    assert pbar.n == 0
    assert len(pbar.xdata) == 0
    assert len(pbar.ydata) == 0
    assert len(pbar.zdata) == 0

    # test clear before iteration
    for _ in pbar:
        pbar.clear()
        assert pbar

# Generated at 2022-06-14 13:43:25.387104
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    import matplotlib.pyplot as plt
    with tqdm_gui(total=10) as pbar:
        pbar.update()
        assert(plt.fignum_exists(pbar.fig.number))
        assert(plt.get_fignums())
    assert(not plt.get_fignums())

# Generated at 2022-06-14 13:43:29.910529
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib.pyplot as plt
    from itertools import count

    for _ in tqdm(range(10)):
        for _ in tqdm(range(10)):
            for _ in tqdm(range(10)):
                for i in count(1):
                    plt.pause(0.01)
                    tqdm.write(i)
                    if i >= 10:
                        break

# Generated at 2022-06-14 13:43:41.226186
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    """Unit test for tqdm_gui."""
    from sys import executable, argv
    from time import sleep
    from subprocess import Popen

    if not executable:  # pragma: no cover
        return  # not an executable script
    try:  # pragma: no cover
        import matplotlib
    except ImportError:  # pragma: no cover
        return  # matplotlib not installed
    else:  # pragma: no cover
        if not hasattr(matplotlib, "figure"):  # pragma: no cover
            return  # no display

# Generated at 2022-06-14 13:43:47.949226
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from time import time

    with tqdm(total=1000, ncols=50, miniters=1000, ascii=True,
              unit_scale=True, unit='B') as t:
        for i in range(1000):  # pylint: disable=unused-variable
            t.display()
            time()
            time()
            time()


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_gui_display()

# Generated at 2022-06-14 13:43:59.110196
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():  # pragma: no cover
    import time
    import matplotlib as mpl
    fig, ax = plt.subplots(figsize=(9, 2.2))
    total = 100
    xdata = []
    ydata = []
    ax.set_xlim(0, 100)
    ax.set_xlabel("percent")
    line1, = ax.plot(xdata, ydata)
    # overall rate
    z = 0
    # update line data
    xdata.append(z * 100.0 / total)
    ydata.append(0)
    line1.set_data(xdata, ydata)
    ax.set_ylim(0, 0.001)
    ax.set_xlabel('percent')
    ax.set_ylabel((None if None else "it") + "/s")

# Generated at 2022-06-14 13:44:02.521246
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib as mpl
    t = tqdm_gui(total=1)
    assert mpl.rcParams['toolbar'] == 'None'
    t.close()
    assert mpl.rcParams['toolbar'] != 'None'

# Generated at 2022-06-14 13:44:05.160658
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    try:
        t = tqdm_gui(total=50)
        for i in range(50):
            t.update()
            t.clear()
    except:
        assert False, "tqdm_gui.clear() raised an exception"

# Generated at 2022-06-14 13:44:44.478492
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from matplotlib import pyplot as plt

    total = 1000

    # Try all variants of tqdm constructors
    for leave in (True, False):
        for ascii in (True, False):
            for unit_scale in (True, False):
                for unit in ("i", "it", "iter", "iters", "s", "sec", "secs",
                             "seconds", "m", "min", "mins", "minutes",
                             "h", "hour", "hours", "d", "day", "days"):  # pragma: no cover
                    # Create instance of class tqdm_gui
                    t = tqdm_gui(total=total, leave=leave,
                                 ascii=ascii, unit_scale=unit_scale, unit=unit,
                                 disable=False)


# Generated at 2022-06-14 13:44:50.826926
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from os import getpid
    from time import sleep
    for i in tqdm(range(2), total=2, leave=False):
        sleep(1)
        for j in tqdm(range(4), total=4, leave=False):
            sleep(0.1)
            tqdm.write("%s:%s" % (getpid(), j))
        tqdm.write("%s:%s" % (getpid(), i))
    tqdm.write("end of test")

# Generated at 2022-06-14 13:44:52.292149
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    t = tqdm(total=1000)
    t.close()

# Generated at 2022-06-14 13:44:59.482846
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from sys import argv
    from time import sleep
    from .utils import _range
    for n in trange(_range(1, 10)):
        sleep(0.1)
    for n in tqdm_gui(_range(1, 10)):
        sleep(0.1)
    for _ in tqdm_gui(total=10):
        sleep(0.1)
    # Test with no args
    for _ in tqdm_gui():
        sleep(0.1)
        break
    # Test with no args and disable
    with tqdm_gui(disable=True) as pbar:
        pbar.update(1)
    # Test with no args and maxinterval
    with tqdm_gui(maxinterval=1) as pbar:
        pbar.update(1)
        pbar

# Generated at 2022-06-14 13:45:05.797389
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from tqdm import gui
    gui.tqdm_gui().close()
    gui.tqdm_gui().close()
    gui.tqdm_gui().close()
    gui.tqdm_gui().close()
    gui.tqdm_gui().close()
    gui.tqdm_gui().close()

if __name__ == "__main__":
    test_tqdm_gui_close()

# Generated at 2022-06-14 13:45:09.938556
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """ Unit test for method close of class tqdm_gui """
    disable_check = tqdm_gui(total=1, disable=True)
    assert disable_check.disable == True
    disable_check.close()

    # TODO: check if anything is called or not

# Generated at 2022-06-14 13:45:19.342145
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """Unit test for method display of class tqdm_gui"""
    import matplotlib
    import matplotlib.pyplot as plt
    import time
    import unittest

# Generated at 2022-06-14 13:45:30.254879
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    try:  # catch Atom and IPython imports
        from matplotlib import pyplot as plt
        from matplotlib import animation
    except Exception as e:
        warn("test_tqdm_gui_display: " + str(e), TqdmExperimentalWarning)
        return
    plt.ioff()
    fig, ax = plt.subplots()

    t = tqdm_gui(dummy_tqdm(), unit="bps", dynamic_ncols=True, mininterval=0,
                 unit_scale=True, leave=True, position=1)

    xdata = []
    ydata = []
    line1, = ax.plot(xdata, ydata, lw=2)

    def run(data):
        # update the data
        t, y = data
        xdata.append

# Generated at 2022-06-14 13:45:33.259273
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from time import sleep
    for i in tqdm_gui(range(1, 500),
                    ascii=True, desc='tqdm_gui_display', miniters=1, mininterval=0.2):
        sleep(0.01)

# Generated at 2022-06-14 13:45:36.391843
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    with tqdm_gui(total=50) as t:
        [t.update(1) for _ in range(50)]


if __name__ == "__main__":
    test_tqdm_gui()