

# Generated at 2022-06-14 13:42:52.450737
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Check `tqdm_gui.close` method.
    """
    from time import sleep
    for i in tqdm([1, 2, 3]):
        sleep(0.1)
    tqdm.close()



# Generated at 2022-06-14 13:43:01.620242
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from time import sleep
    from numpy import linspace

    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    # Monkeypatch to test class tqdm_gui in isolation
    tqdm_gui._instances = []
    tqdm_gui.tqdm_gui = tqdm_gui

    # Use of the class
    t = tqdm_gui(range(100))
    t.start()
    sleep(0.1)
    t.display()
    for i in range(1, 100):
        sleep(0.01)
        t.update(i)
    t.close()
    # Check that a Polygon is created
    assert isinstance(t.hspan, Polygon)
    # Check that the plot is cleared


# Generated at 2022-06-14 13:43:05.153194
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    i = 0
    progress = tqdm_gui(total=10)
    for i in range(0, 10):
        progress.update(1)
    progress.close()
    assert i == 10

# Generated at 2022-06-14 13:43:10.635112
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from ._tqdm import __version__
    from ._tqdm import _version

    # Following two lines should be equivalent:
    for i in tqdm_gui(["a", "b", "c"], ascii=True, desc="test_close"):
        for _ in tqdm_gui(xrange(100), ascii=True):
            pass



# Generated at 2022-06-14 13:43:17.488487
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    """Test tqdm.gui.tqdm._display"""
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    import time

    matplotlib.use('Qt5Agg')
    pbar = tqdm_gui(total=None, unit='B', unit_scale=True, smoothing=0)
    for i in pbar:
        pbar.display(1)
        time.sleep(0.01)
    assert abs(np.mean(pbar.ydata) - 100) < 1
    assert abs(np.mean(pbar.zdata) - 100) < 1
    plt.close(pbar.fig)



# Generated at 2022-06-14 13:43:21.263107
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    import time

    with tqdm(total=9) as pbar:
        for i in range(3):
            pbar.update()
            time.sleep(0.1)

if __name__ == '__main__':
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:28.322126
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib as mpl

    t = tqdm_gui(["a", "b"])

    assert t
    assert t._instances
    assert t.disable is False
    assert t.gui is True
    assert isinstance(t.mpl, type(mpl))
    assert t.plt
    assert t.toolbar == mpl.rcParams['toolbar']
    assert t.mpl.rcParams['toolbar'] == 'None'
    assert t.wasion == t.plt.isinteractive()
    assert t.plt.isinteractive() is True
    assert t.ax
    assert t.ax.get_xlabel() == 'percent' if t.total else 'seconds'
    assert t.ax.get_ylabel() == t.unit if t.unit else "it"
   

# Generated at 2022-06-14 13:43:34.717328
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from unittest import TestCase

    from .std import _instances

    class TestTqdmGui(TestCase):
        def test_close(self):
            t = tqdm_gui(range(3))
            t.close()
            self.assertNotIn(t, _instances)

    from .utils import run_tests
    run_tests(TestTqdmGui)

# Generated at 2022-06-14 13:43:42.512688
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .std import tqdm as std_tqdm
    from .utils import _range
    from time import sleep

    t = tqdm_gui(_range(4), leave=False)
    for n in t:
        sleep(0.01)

    t = tqdm_gui(_range(4), leave=False)
    for n in t:
        sleep(0.01)

    t = std_tqdm(_range(4), leave=False)
    for n in t:
        sleep(1)


if __name__ == "__main__":
    pass
    # test_tqdm_gui_display()

# Generated at 2022-06-14 13:43:51.761960
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .utils import FormatCustomText
    from .std import TqdmTypeError

    with tqdm_gui(total=100, unit_scale=True, unit="iB",
                  unit_divisor=1024, ncols=80, dynamic_ncols=False,
                  bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]", position=0) as t:
        for i in range(10):
            t.display()
            t.update()

    with FormatCustomText(bar_format='{bar} {n} {total}'):
        with tqdm_gui(total=100) as t2:
            t2.display()
            t2.update()


# Generated at 2022-06-14 13:44:07.388100
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    import time
    # do the test
    with tqdm_gui(total=100) as pbar:
        for i in range(100):
            time.sleep(0.1)
            if i == 25:
                pbar.clear()
            pbar.update(1)


# Generated at 2022-06-14 13:44:15.603367
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    import sys
    from cStringIO import StringIO
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from .tqdm import trange
    import time

    # mocking figure objects
    class MockedObject:
        class MockLine:
            def __init__(self, x, y):
                pass

            def set_data(self, x, y):
                pass

        class MockAxis:
            def __init__(self):
                pass

            def plot(self, x, y):
                return MockedObject.MockLine(x, y)

            def set_ylim(self, ymin, ymax):
                pass

            def set_xlabel(self, label):
                pass

            def set_ylabel(self, label):
                pass

# Generated at 2022-06-14 13:44:25.289095
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from .std import TqdmDefaultWriteLock
    t = tqdm(total=100)
    assert len(t.xdata) == len(t.ydata) == len(t.zdata) == 0
    for i in tqdm(range(4), total=4):
        t.display(n=i, total=4)
        assert len(t.xdata) == len(t.ydata) == len(t.zdata) == (i + 1)
        assert t.xdata[i] == i * 25
        assert t.ydata[i] < 1000
        assert t.zdata[i] < 1000
    t.close()
    assert t.get_lock() is TqdmDefaultWriteLock

# Generated at 2022-06-14 13:44:30.111982
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """
    Unit test for method display of class tqdm_gui
    """
    from time import sleep
    import matplotlib.pyplot as plt
    for _ in tqdm_gui(range(3), desc='1st loop', leave=False):
        for _ in tqdm_gui(range(50), desc='2nd loop', leave=False, gui=True):
            sleep(0.01)

    plt.close('all')

# Generated at 2022-06-14 13:44:38.183978
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    try:
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        mpl.use("Agg")
        t = tqdm_gui(0, unit="i", unit_scale=True, unit_divisor=2 ** 10)
        t.close()
        t = tqdm_gui(0, unit="i", unit_scale=True, unit_divisor=2 ** 10)
        t.close()
    except Exception as e:
        raise e
    # finally:
    #     plt.close("all")

# Generated at 2022-06-14 13:44:45.216483
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    with tqdm(total=10) as pbar:
        pbar.clear()
    assert not pbar.disable


if __name__ == "__main__":  # pragma: no cover
    from time import sleep
    # avoid deadlock on ctrl+c/break/abort on Windows, as in #242
    try:
        with tqdm(total=200) as pbar:
            for i in pbar:
                sleep(0.02)
    except:
        pass

# Generated at 2022-06-14 13:44:54.143618
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    import time, locale
    locale.setlocale(locale.LC_ALL, '')
    try:
        from matplotlib import pyplot as plt
    except ImportError:
        return

    for n in [
            0, 1, 2, 33, 34, 35, 36, 37, 61, 62, 63, 64,
            65, 66, 1000, 2 ** 32, 2 ** 33, 2 ** 36, 2 ** 40]:
        t = tqdm_gui(n,
                     unit="B",
                     unit_scale=True,
                     mininterval=0.01,
                     miniters=1,
                     leave=False)
        for i in t:
            time.sleep(0.01)
        t.close()


# Generated at 2022-06-14 13:44:58.262590
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from .gui import tqdm
    from time import sleep
    for i in tqdm(range(10)):
        sleep(0.05)
        tqdm.clear()

if __name__ == "__main__":
    test_tqdm_gui_clear()

# Generated at 2022-06-14 13:45:09.526969
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from time import sleep
    from numpy import isclose
    from numpy.testing import assert_almost_equal

    # import matplotlib as mpl
    # import matplotlib.pyplot as plt
    # mpl.rcParams['toolbar'] = 'None'
    # print("isinteractive:", plt.isinteractive())
    # print("rcParams['toolbar']:", mpl.rcParams['toolbar'])

    t = tqdm_gui(range(1000))
    sleep(0.1)
    t.last_print_n = 200
    t.last_print_t = t._time() - 0.5
    t.display()
    sleep(0.1)
    t.display()
    t.close()

# Generated at 2022-06-14 13:45:11.853581
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    import time
    pbar = tqdm_gui(total=10)
    for i in range(10):
        pbar.update()
        time.sleep(0.1)
    pbar.close()