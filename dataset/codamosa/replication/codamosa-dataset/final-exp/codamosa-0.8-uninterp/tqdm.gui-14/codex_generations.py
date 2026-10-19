

# Generated at 2022-06-14 13:43:00.626953
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from time import sleep
    from shutil import rmtree
    try:
        from tempfile import mkdtemp
    except ImportError:
        from backports.tempfile import mkdtemp
    try:
        import matplotlib
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError("tqdm_gui requires matplotlib")

    matplotlib.interactive(True)
    tmpdir = mkdtemp()
    for f in ("tqdm_gui.png", "tqdm_gui.pdf"):
        f = tmpdir + "/" + f

# Generated at 2022-06-14 13:43:11.939855
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    # Remember if external environment uses toolbars
    toolbar = mpl.rcParams['toolbar']
    mpl.rcParams['toolbar'] = 'None'

    # Remember if external environment is interactive
    wasion = plt.isinteractive()
    plt.ion()

    # Instantiate class
    instance = tqdm_gui(total=100)

    # Test display()
    for i in _range(100):
        instance.n = i + 1
        instance.last_print_n = i
        instance.last_print_t = 0
        instance.start_t = 0
        instance.display()

    # Restore toolbars
    mpl.rcParams['toolbar'] = toolbar
    # Return to non-interactive

# Generated at 2022-06-14 13:43:22.622416
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from .std import _term_move_up  # NOQA

    t = tqdm_gui(total=None, leave=True)
    for _ in range(4):
        t.display()  # NOQA

    t = tqdm_gui(total=5)
    t.update(1)
    assert len(t.xdata) == len(t.ydata) == len(t.zdata) == 1
    assert t.xdata[0] == 20
    assert t.ydata[0] > 0
    assert t.zdata[0] > 0
    t.update(1)
    assert len(t.xdata) == len(t.ydata) == len(t.zdata) == 2
    assert t.xdata[1] == 40

# Generated at 2022-06-14 13:43:26.038556
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    frmt = '{n} {bar} {n_fmt} {rate_fmt}'
    with tqdm(total=10, desc='Progress', postfix=frmt, unit_scale=True,
              miniters=1, mininterval=0.2) as pbar:
        for i in _range(10):
            pbar.update()
            pbar.set_postfix_str(
                '{0:.2f}{1}'.format(i, pbar.unit), refresh=False)

# Generated at 2022-06-14 13:43:32.799892
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    with tqdm_gui(total=1) as pbar:
        pbar.display()
        pbar.clear()


if __name__ == "__main__":
    try:
        from time import sleep
        with tqdm(total=100, mininterval=1) as pbar:
            for i in range(50):
                sleep(0.01)
                pbar.update(2)
    except (KeyboardInterrupt, SystemExit):
        pass

# Generated at 2022-06-14 13:43:41.226047
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from time import sleep
    from matplotlib import pyplot as plt

    with plt.xkcd():  # Must be before import tqdm_gui
        from .gui import tqdm_gui

        # The with statement is necessary to close the server
        with tqdm_gui(total=100) as t:
            for i in range(100):
                sleep(0.1)
                t.update()

        # The with statement is necessary to close the server
        with tqdm_gui(total=100) as t:
            for i in range(100):
                sleep(1)
                t.update()

# Generated at 2022-06-14 13:43:44.588269
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    # remove progress bars from test output
    with tqdm(total=10, leave=True) as pbar:
        for i in trange(10):
            pbar.update()
    print("test_tqdm_gui done!")

# Generated at 2022-06-14 13:43:51.255194
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    from time import sleep
    from .std import tqdm_gui
    try:
        from io import StringIO
    except ImportError:
        from StringIO import StringIO

    previous_stdout = sys.stdout
    sys.stdout = StringIO()

    for i in tqdm_gui(range(1, 10)):
        sleep(0.3)

    output = sys.stdout.getvalue()
    sys.stdout = previous_stdout

    assert output
    assert isinstance(output, str)
    assert len(output) > 300

# Generated at 2022-06-14 13:43:55.110028
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    l = range(100)
    l = tqdm_gui(l)
    for _ in l:
        ...
    l.close()


# Generated at 2022-06-14 13:43:57.772284
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from .gui import tqdm
    with tqdm(leave=False, total=10) as t:
        for i in range(10):
            t.clear(i)

# Generated at 2022-06-14 13:44:15.706474
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    """Unit test for constructor of class tqdm_gui"""
    try:
        # Forcefully import all modules
        from .gui import tqdm_gui as tg
        from matplotlib import pyplot as plt
        import numpy as np
    except ImportError:
        return

    # Constructor tests
    with tg(total=10) as t:
        assert len(t.xdata) == 10
        assert len(t.ydata) == 10
        assert len(t.zdata) == 10
    # -
    with tg(10) as t:
        assert len(t.xdata) == 10
        assert len(t.ydata) == 10
        assert len(t.zdata) == 10
    # -

# Generated at 2022-06-14 13:44:19.120814
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    """
    Unit test for method clear of class tqdm_gui
    """
    t = tqdm_gui(total=10)
    t.clear()
    t.display()
    t.update()
    t.clear()

# Generated at 2022-06-14 13:44:22.957683
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from time import sleep

    t = trange(100)
    for i in t:
        sleep(0.01)
        t.display()


# Unit testing (when run directly)
if __name__ == "__main__":  # pragma: no cover
    test_tqdm_gui_display()

# Generated at 2022-06-14 13:44:28.259811
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    for i in range(4):
        for _ in tqdm_gui(range(4), desc='testing clear'):
            pass
    for i in range(4):
        tqdm_gui(range(4), desc='testing clear').close()

# For dynamic loading (e.g. IPython extension)
TQDM_GUI_CLS = tqdm_gui

# Generated at 2022-06-14 13:44:38.522636
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma : no cover
    """
    Unit test for constructor of class tqdm_gui.
    """
    from random import random
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise unittest.SkipTest("matplotlib is not installed")
    t = tqdm(total=200)
    for i in range(200):
        t.set_postfix(time="test" * i, refresh=False)
        t.update(1)
        update_t = t.last_print_t
        time.sleep(random() * 0.2)
        t.update()
        assert t.last_print_t > update_t
    t.close()
    assert plt.fignum_exists(1)



# Generated at 2022-06-14 13:44:43.709208
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep

    with tqdm_gui(total=100) as t:
        for i in _range(100):
            sleep(0.1)
            t.update()


if __name__ == "__main__":
    try:
        test_tqdm_gui()
    except KeyboardInterrupt:
        pass

# Generated at 2022-06-14 13:44:52.964107
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from .utils import FormatStdout
    from tqdm import main_gui
    __init__ = main_gui.tqdm.__init__
    main_gui.tqdm.__init__ = lambda *a, **kw: None
    main_gui.tqdm.__init__.miniters = 1
    with FormatStdout():
        main_gui.tqdm._instances.clear()
        main_gui.tqdm(total=10, file=sys.stderr, mininterval=0)
        with main_gui.tqdm(total=10, file=sys.stderr, mininterval=0) as t:
            assert t.gui

    main_gui.tqdm.__init__ = __init__

# Generated at 2022-06-14 13:44:55.737032
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    with tqdm(_range(5), gui=True) as t:
        for i in t:
            pass


# Generated at 2022-06-14 13:45:01.667008
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    """
    Test that the clear method of tqdm_gui
    does not delete the class attributes
    """
    t = tqdm_gui([], disable=True)
    t_attributes = dir(t)
    t.update(2)
    t.clear()
    t.display()
    t_attributes_after = dir(t)
    assert t_attributes == t_attributes_after

# Generated at 2022-06-14 13:45:06.237362
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot([1], [2])
    assert plt.get_fignums() == [1]  # One figure open
    t = tqdm(total=1)
    t.close()
    assert plt.get_fignums() == []  # No figure left open