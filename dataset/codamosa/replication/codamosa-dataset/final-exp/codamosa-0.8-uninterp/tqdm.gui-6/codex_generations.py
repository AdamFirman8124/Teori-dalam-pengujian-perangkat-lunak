

# Generated at 2022-06-14 13:43:00.626242
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from time import sleep
    from random import randint
    try:
        t = tqdm_gui(0, 1.0)
        t.display()
        sleep(0.2)
        t.display()
        sleep(0.2)
        t.display()
        sleep(0.2)

        t = tqdm_gui(100)
        for _ in t:
            sleep(0.01 + (randint(0, 99) / 99.) / 5)

        t = tgrange(100)
        for _ in t:
            sleep(0.01 + (randint(0, 99) / 99.) / 5)
    finally:
        t.close()


if __name__ == "__main__":
    test_tqdm_gui_display()

# Generated at 2022-06-14 13:43:03.261202
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    with std_tqdm(range(10)) as t:
        for x in t:
            break

test_tqdm_gui_close()

# Generated at 2022-06-14 13:43:05.175907
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    a = 1
    for i in tqdm_gui(range(10)):
        tqdm_gui.write('step %s done' % i)
        a = a + 1

# Generated at 2022-06-14 13:43:07.420489
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from .gui import trange
    for __ in trange(3, desc='Foo'):
        pass
    print("Tests successful!")

# Generated at 2022-06-14 13:43:10.173172
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep

    with tqdm_gui(total=100) as t:
        for i in _range(10):
            sleep(.1)
            t.update(10)
    # t.set_postfix(ordered_dict=OrderedDict([('a', 1), ('b', 2), ('c', 3)]))


if __name__ == '__main__':
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:14.378503
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """Test function for tqdm_gui.close"""
    import gc
    from sys import version
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    if version[0] == "3":
        from functools import reduce  # Python 3
    else:
        reduce = reduce  # Python 2

    def get_refcounts():
        gc.collect()
        return reduce(
            lambda x, y: x + y,
            [len(gc.get_referrers(o)) for o in gc.get_objects()])

    t = tqdm(["a", "b"])
    ref0 = get_refcounts()
    t.close()
    assert get_refcounts() == ref0

    # Restore toolbars

# Generated at 2022-06-14 13:43:24.110631
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    tqdm_gui().clear()
    try:
        tqdm_gui(gui=False).clear()
    except RuntimeError:
        pass
    else:
        assert False, "tqdm.gui.tqdm clear should fail with gui=False."

if __name__ == "__main__":  # pragma: no cover
    from time import sleep
    from numpy.random import random
    from numpy import arange
    from multiprocessing import Pool

    def f(n):
        return arange(100).mean() + random()

    t = tqdm(total=100)
    for i in range(10):
        t.update()
        sleep(0.1)
    t.close()

    t = tqdm(total=100, leave=False)

# Generated at 2022-06-14 13:43:29.157487
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib.pyplot as plt
    import numpy as np
    plt.ion()
    pbar = tqdm_gui(total=100, ncols=70, leave=False)
    plt.show(block=False)
    for _ in pbar:
        x = np.arange(1e5, dtype='float')
        np.sin(x, x)

# Generated at 2022-06-14 13:43:35.291577
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib.pyplot as plt
    with tqdm_gui(total=8, disable=False) as t:
        t.n = 4
        assert plt.fignum_exists(t.fig.number)
        assert t.disable is False
    assert plt.fignum_exists(t.fig.number) is False
    assert t.disable is True

# Generated at 2022-06-14 13:43:44.105866
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from sys import version_info
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # we have to close the plot to avoid disturbing the tests
    # so we patch plt.close to pass silently
    # see https://stackoverflow.com/a/48355868/353337
    plt._close = plt.close
    def noop(*args, **kwargs):
        pass
    plt.close = noop

    # expected text
    text = '\r  0%|          | 0/9 [00:00<?, ?it/s]'
    # expected data
    xdata = []
    ydata = []
    zdata = []
    poly_lims = [[], []]
    # expected min and max values of y axis
    ymin, ymax = 0.