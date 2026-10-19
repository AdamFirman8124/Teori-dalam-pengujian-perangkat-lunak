

# Generated at 2022-06-14 13:43:06.469082
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    from pylab import imread, imshow

    t = tqdm_gui(total=100, position=0)
    for x in range(100):
        t.update()

    t.close()
    t.close()

    t = tqdm_gui(total=100, position=0)
    for x in range(100):
        t.update()

    t.close()
    t.close()

    t = tqdm_gui(total=100, position=0)
    for x in range(100):
        t.update()

    t.close()
    t.close()

    t = tqdm_gui(total=100, position=0)
    for x in range(100):
        t.update()

    t.close()
    t.close()



# Generated at 2022-06-14 13:43:11.554181
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    """Unit test for constructor of class tqdm_gui."""
    from time import sleep
    import random

    with tqdm_gui(total=0, desc='Test', leave=False) as bar:
        for i in bar:
            sleep(random.random() * 0.01)
            bar.update()

# Generated at 2022-06-14 13:43:18.334155
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from .gui import trange
    from .gui import tqdm
    mpl.rcParams['toolbar'] = 'None'
    test_text = "display method unit test for class tqdm_gui"

# Generated at 2022-06-14 13:43:26.601109
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep
    from .utils import format_sizeof
    from .std import cpu_count
    from .std import tqdm as std_tqdm

    try:
        from collections import OrderedDict
    except ImportError:
        from ordereddict import OrderedDict

    # We need to create a new tqdm_gui object for initialisation
    pbar = tqdm_gui(ascii=True)
    try:  # pragma: no py3 cover
        # Python2
        assert isinstance(pbar, tqdm_gui)
    except NameError:  # pragma: no py2 cover
        # Python3
        assert isinstance(pbar, tqdm_gui)

    # Test on python 2 and 3

# Generated at 2022-06-14 13:43:37.967191
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from collections import deque
    from math import isnan
    from sys import getrefcount as grc
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np
    from tqdm._tqdm import TMonitor

    pbar = tqdm_gui(total=100)
    pbar.display()
    pbar.n = 50
    pbar.display()
    pbar.n = 100
    pbar.display()

    pbar = tqdm_gui(total=None, unit='B', unit_scale=True)
    pbar.display()
    pbar.update(1)
    pbar.display()
    pbar.update(1)
    pbar.display()


# Generated at 2022-06-14 13:43:43.099202
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():  # pragma: no cover
    from time import sleep
    from tqdm.gui import tqdm
    t = tqdm(total=10)
    for i in range(10):
        sleep(.1)
        t.update(1)
        t.clear()

# Generated at 2022-06-14 13:43:49.937785
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    import sys
    if sys.version_info[0] < 3:
        from io import StringIO
    else:
        from io import StringIO

    old_stdout = sys.stdout
    sys.stdout = StringIO()
    with tqdm(total=9) as t:
        for i in range(4):
            t.update()
    t.close()
    s = sys.stdout.getvalue()
    sys.stdout = old_stdout
    assert s == '\n', s

# Generated at 2022-06-14 13:43:54.908419
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from time import sleep
    I = tqdm_gui(100, leave=True)
    for i in I:
        sleep(0.1)
        I.display()
        assert I.n == i + 1
    assert I.n == 100

# Generated at 2022-06-14 13:44:03.210650
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import time
    from tqdm import tqdm

    from .std import tqdm_gui
    from .std import tqdm as std_tqdm

    # Prepare the cases
    cases = [
        {
            'tqdm_gui': tqdm_gui,
            'args': (range(4),),
            'args_for_close': (True,),
            'kwargs': None
        },
        {
            'tqdm_gui': tqdm,
            'args': (range(4),),
            'args_for_close': (True,),
            'kwargs': None
        }
    ]

    # the expected output when close method is called
    expected_output = "  0%|          | 0/4 [00:00<?, ?it/s]\r"

    #

# Generated at 2022-06-14 13:44:08.959322
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from numpy import inf
    from time import sleep as ts
    from tqdm.gui import trange
    import numpy as np
    tqdm.close()  # Close any remaining window
    tqdm.clear()
    for total in [None, 10, 11, 100, 101]:
        for leave in [True, False]:
            i = 0
            for x in trange(total, leave=leave):
                ts(i / 5)
                i += 1
            tqdm.close()


if __name__ == '__main__':
    test_tqdm_gui_display()