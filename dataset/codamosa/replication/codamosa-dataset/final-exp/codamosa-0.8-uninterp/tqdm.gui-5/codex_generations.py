

# Generated at 2022-06-14 13:42:51.707623
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """
    Reference test for the method display of class tqdm_gui.
    """
    try:
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        mpl.use('TkAgg')
        tot = 100
        t = tqdm(total=tot)
        for i in range(tot + 5):
            t.update()
        t.close()
    except Exception:  # pragma: no cover
        assert False, "Reference test for the method display of class tqdm_gui" \
            " failed with error: {}".format(Exception)

# Generated at 2022-06-14 13:43:00.124496
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from sys import argv
    from time import sleep

    try:
        from numpy import arange
    except ImportError:
        from range import arange

    wait = float(argv[1]) if len(argv) > 1 else 0.1
    try:
        from tqdm.gui import tqdm_gui
        tqdm_gui(arange(10), leave=False).close()
        tqdm_gui(arange(10), leave=True).close()
        tqdm_gui(arange(10)).close()
        with tqdm_gui(arange(10)) as t:
            for _ in t:
                sleep(wait)
    except Exception as e:
        print(e)

# Generated at 2022-06-14 13:43:02.931140
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from time import sleep
    for i in tqdm(range(10), unit="s"):
        sleep(0.1)
    tqdm.close()

# Generated at 2022-06-14 13:43:13.634675
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np

    # Reset matplotlib default params
    plt.rcParams.update(mpl.rcParamsDefault)

    # Create random data
    ydata = np.random.random(100)
    # Create xdata with a specific seed to always have the same values
    np.random.seed(12345)
    xdata = np.linspace(0, 100, len(ydata))

    # Add cyclic noises
    for i in [-3, -2, -1, 1, 2, 3]:
        ydata += (1.5 + np.sin(xdata * 0.1 * i)) / (1.0 + i ** 2.0)


# Generated at 2022-06-14 13:43:21.155465
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    with tqdm_gui(total=10) as t:
        for i in range(10):
            t.update()
    with tqdm_gui(total=10, desc='desc', leave=True) as t:
        for i in range(5):
            t.update()
            t.set_description('desc%d' % i)
    with tqdm_gui(total=10) as t:
        for i in range(5):
            t.update(0)
            t.set_description('desc%d' % i)

# Generated at 2022-06-14 13:43:28.242202
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib

    import matplotlib.pyplot as plt
    from tqdm.gui import tqdm_gui as tqdm
    try:
        matplotlib.use('Agg')
    except ImportError:
        pass

    for t in [tqdm(range(10)), tqdm(range(10), leave=True)]:
        # test without error
        t.close()
        # test with exception after close
        try:
            t.update()
            raise AssertionError("t.update() after close() should raise")
        except ValueError:
            pass
        # test mpl params reset
        assert plt.isinteractive() == t.wasion, "isinteractive() incorrect"
        assert plt.rcParams['toolbar'] == t.toolbar, "mpl params incorrect"



# Generated at 2022-06-14 13:43:39.567992
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from .utils import formatted_size, naturalsize
    from .std import tqdm

    t = tqdm(total=100, leave=False)
    new_format = "{ru_wallclock}: {bar} {n_fmt}/{total_fmt} [{elapsed}<{remaining},{rate_fmt}]"
    t.set_postfix(total_fmt=formatted_size, n_fmt=naturalsize, ru_wallclock=lambda x: '1s')
    t.close()
    del t


if __name__ == '__main__':
    import sys
    import time
    from .utils import format_interval

    n = 100
    t = tqdm(total=n, leave=False)
    for i in range(n):
        time.sleep

# Generated at 2022-06-14 13:43:44.482254
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    class A(object):
        def __init__(self):
            self.append = False
        def append(self):
            self.append = True

    a = A()
    a._instances = [a]
    a.disable = False
    a.close()
    assert a.disable
    assert a.append


# Generated at 2022-06-14 13:43:49.035958
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from .std import tqdm

    t = tqdm(total=100, gui=True, colour="b")
    for i in t:
        continue


if __name__ == "__main__":  # pragma: no cover
    from .main import _test_gui
    _test_gui(__file__, test_tqdm_gui)

# Generated at 2022-06-14 13:43:50.653860
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    assert tgrange(1).clear() is None