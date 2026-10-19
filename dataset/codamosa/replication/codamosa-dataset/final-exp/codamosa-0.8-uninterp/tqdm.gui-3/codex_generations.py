

# Generated at 2022-06-14 13:43:06.270718
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from time import sleep
    from numpy import random

    for i in trange(15):
        sleep(random.random() * 0.2)
    for i in trange(15, desc='description'):
        sleep(random.random() * 0.2)

    for i in trange(15, desc='description', unit='it', position=3):
        sleep(random.random() * 0.2)
    for i in trange(15, desc='description', unit='it', position=3, leave=False):
        sleep(random.random() * 0.2)

    for i in trange(15, desc='description', unit='it',
                    position=3, leave=False, mininterval=0.05):
        sleep(random.random() * 0.2)



# Generated at 2022-06-14 13:43:15.418939
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Test tqdm_gui close method
    """
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # Set interactive mode
    assert not plt.isinteractive(), "It should be no interactive mode"
    tgrange(10, leave=True)
    assert plt.isinteractive(), "It should be interactive mode"
    plt.ioff()

    # Check if toolbars are activated
    assert mpl.rcParams['toolbar'] == 'None', "Toolbar should be None"
    tgrange(10, leave=True)
    assert mpl.rcParams['toolbar'] == 'Toolbar2', "Toolbar should be Toolbar2"
    mpl.rcParams['toolbar'] = 'None'

# Generated at 2022-06-14 13:43:18.093467
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    t = tqdm_gui(total=2, disable=False)
    t.update(1)
    t.close()

# Generated at 2022-06-14 13:43:26.446794
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from pylab import show, close, gca
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    import itertools as it
    try:
        from itertools import izip
    except ImportError:
        from itertools import zip as izip
    try:
        from itertools import imap
    except ImportError:
        imap = map

    def assert_array_equal(var1, var2):
        return imap(lambda x, y: x == y, var1, var2)

    class TestTqdmGui(tqdm_gui):
        def __init__(self, *args, **kwargs):
            super(TestTqdmGui, self).__init__(*args, **kwargs)
            self.fig.tight

# Generated at 2022-06-14 13:43:32.295288
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    t = tqdm_gui(total=1, leave=False)
    t.close()
    assert mpl.rcParams['toolbar'] != 'None'
    assert not plt.isinteractive()

    tqdm_gui(total=1, leave=False, disable=True).close()



# Generated at 2022-06-14 13:43:41.481443
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    """
    >>> from time import sleep
    >>> pbar = tqdm_gui(total=5)
    >>> for i in range(5):
    ...     pbar.update()
    ...     sleep(0.01)
    >>> pbar.close()
    >>> pbar = tqdm_gui(total=50)
    >>> for i in range(50):
    ...     pbar.update()
    ...     sleep(0.01)
    >>> pbar.close()
    """
    pass

if __name__ == '__main__':  # pragma: no cover
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 13:43:51.021914
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():  # pragma: no cover
    import sys

    if sys.version_info < (3, 4):
        return

    from tempfile import NamedTemporaryFile
    import matplotlib.pyplot as plt
    # test bar closure
    __test_close_f = NamedTemporaryFile(delete=False)
    with open(__test_close_f.name, 'w') as f:
        for _ in tqdm_gui(range(3), file=f, leave=True):
            pass
    with open(__test_close_f.name, 'r') as f:
        assert f.readlines() == ['|33%||']
    # test figure closure
    # Save current interactive state:
    ion_default = plt.isinteractive()
    plt.ion()
    # Test with leave=True

# Generated at 2022-06-14 13:43:51.649209
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    pass

# Generated at 2022-06-14 13:44:01.314637
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """
    Tester unitaire de la méthode display de la class tqdm_gui.
    """
    # On importe les modules nécessaires à la fonction
    from tqdm.gui import tqdm
    from time import sleep

    # On effectue un exemple simple avec un tqdm
    # On utilise la méthode display pour mettre à jour l'affichage
    print("Exemple 1 :")
    for i in tqdm(range(10), unit=" itérations"):
        sleep(0.25)
        tqdm.display()
    print("\nFin exemple 1")
    print("\n")

    # On affiche "récapitulatif"
    # On utilise la méthode display pour mettre à jour l'

# Generated at 2022-06-14 13:44:09.096091
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """
    $ python -m tqdm.gui
    """
    from collections import deque

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    t = tqdm_gui(total=100, disable=True)

    # remember if external environment uses toolbars
    toolbar = mpl.rcParams['toolbar']
    mpl.rcParams['toolbar'] = 'None'

    t.mininterval = max(t.mininterval, 0.5)
    fig, ax = plt.subplots(figsize=(9, 2.2))
    total = t.__len__()  # avoids TypeError on None #971
    if total is not None:
        t.xdata = []
        t.ydata = []
        t.zdata = []

# Generated at 2022-06-14 13:44:26.531160
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    import time
    with tqdm_gui(total=100) as t:
        for i in _range(100):
            t.update()
            time.sleep(0.01)


if __name__ == "__main__":
    test_tqdm_gui()

# Generated at 2022-06-14 13:44:33.040347
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import os
    import sys
    import time
    #from time import sleep

    #from matplotlib import pyplot as plt
    from ...tests import TestTqdmGUI

    def get_sizes(filename):
        """Find size of file during writing"""
        sizes = []
        old = 0
        while True:
            try:
                sizes.append(os.path.getsize(filename))
                old = os.path.getsize(filename)
            except Exception:
                pass
            finally:
                if sizes:
                    old = sizes[-1]
                yield old
                time.sleep(0.01)


# Generated at 2022-06-14 13:44:37.020949
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from tqdm.gui import tqdm
    for i in tqdm(range(2)):
        pass


if __name__ == "__main__":
    test_tqdm_gui_close()
    # import doctest
    # doctest.testmod()

# Generated at 2022-06-14 13:44:39.061983
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from .gui import tqdm
    f = tqdm(total=100)
    f.close()

# Generated at 2022-06-14 13:44:40.908691
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from time import sleep
    for _ in tqdm_gui(range(1000)):
        sleep(0.0001)

# Generated at 2022-06-14 13:44:46.645651
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    """
    >>> import time
    >>> from tqdm.gui import tqdm
    >>> t = tqdm(total=60)
    >>> last = [0]
    >>> for i in range(1, 60):
    ...     t.update()
    ...     time.sleep(1)
    ...     last.append(t.last_print_n)

    >>> last == list(range(1, 60))
    True
    """
    pass

# Generated at 2022-06-14 13:44:54.270627
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """Test tqdm_gui close function"""
    # _instances is private
    # pylint: disable=W0212
    from tqdm import _instances
    import matplotlib.pyplot as plt

    # Remember if external environment uses toolbars
    toolbar = plt.rcParams['toolbar']
    # Remember if external environment is interactive
    wasion = plt.isinteractive()

    # init tqdm_gui
    tqdm_gui_test = tqdm_gui(desc='test_tqdm_gui_close', leave=True)
    tqdm_gui_test.close()

    try:
        assert _instances == []
    except AssertionError:
        raise ValueError('tqdm_gui.close() failed to remove tqdm_gui from _instances')


# Generated at 2022-06-14 13:45:01.949459
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    import matplotlib.pyplot as plt
    t = tqdm_gui(total=1e3, leave=False)
    b = 1e-6
    for j in range(0, int(1e3), 10):
        # Add some data
        t.xdata.append(j)
        t.ydata.append(b)
        t.zdata.append(b)
        t.display()
        b += 1e-6
    t.close()
    plt.show()

# Generated at 2022-06-14 13:45:07.639818
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    import sys
    import time

    # Hack to not display in CI for now
    if 'TRAVIS' in sys.environ or 'APPVEYOR' in sys.environ:
        return
    with tqdm_gui(total=10, unit='spam') as pbar:  # total unnecessary
        for i in range(10):
            pbar.update()
            time.sleep(0.1)


if __name__ == "__main__":
    test_tqdm_gui()

# Generated at 2022-06-14 13:45:10.789833
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    import matplotlib.pyplot as plt

    with tqdm(total=None) as t:
        for i in _range(100):
            plt.draw()
            t.update()

