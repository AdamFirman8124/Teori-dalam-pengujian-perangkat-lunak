

# Generated at 2022-06-14 13:43:06.368466
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    from collections import deque
    from unittest import TestCase
    from numpy.random import randint
    randint(1, 10)
    import matplotlib.pyplot as plt
    plt.ion()
    import matplotlib as mpl
    mpl.rcParams['toolbar'] = 'None'

    class Test(TestCase):
        def test(self):
            # Initialize class
            t = tqdm_gui(total=100)
            # Make sure that the rest of the class was initialized properly
            self.assertEqual(t.desc, '')
            self.assertEqual(t.file, sys.stderr)
            self.assertEqual(t.miniters, 1)
            self.assertEqual(t.mininterval, 0.1)
            self.assertE

# Generated at 2022-06-14 13:43:13.222370
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():
    from inspect import isclass
    from tqdm import gui
    assert isclass(gui.tqdm_gui)


if __name__ == "__main__":  # pragma: no cover
    from time import sleep
    from tqdm import trange
    for i in trange(15, desc='1st loop'):
        for j in trange(100, desc='2nd loop'):
            for k in trange(100, desc='3nd loop'):
                sleep(0.01)

# Generated at 2022-06-14 13:43:17.643600
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    warn("gui tests are not implemented yet", TqdmExperimentalWarning, stacklevel=2)
    return
    import gc
    from time import sleep
    for i in range(5):
        for j in trange(5, leave=False):
            sleep(0.01)
        gc.collect()

# Generated at 2022-06-14 13:43:21.899246
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():  # pragma: no cover
    with tqdm(total=1) as t:
        t.update()
        assert t.last_print_n == 1
        assert t.last_print_t == t.last_print_n
        assert t.n == 1
        assert t.n == t.last_print_n
        assert t.last_print_n == t.last_print_t
        t.clear()
        assert t.last_print_n == 1
        assert t.last_print_t == t.last_print_n
        assert t.n == 1
        assert t.n == t.last_print_n
        assert t.last_print_n == t.last_print_t
    return True

# Generated at 2022-06-14 13:43:25.925715
# Unit test for constructor of class tqdm_gui
def test_tqdm_gui():  # pragma: no cover
    from time import sleep
    t = tqdm_gui([1, 1, 2, None, "foobar", 0, 0.5], mininterval=0.5)
    for x in t:
        sleep(0.5)
    t.close()


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_gui()

# Generated at 2022-06-14 13:43:33.128348
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():  # pragma: no cover
    # Create an instance of tqdm, with the default arguments
    t = tqdm_gui()
    # Test format_meter method (digits calculation and default argument)
    assert t.format_meter() == "  0%|          | 0/?"

    # Test update method
    t.total = 20
    for i in t._range(20):
        t.update()
    # Test format_meter method (percentage calculation)
    assert t.format_meter() == "100%|##########| 20/20"

    # Test format_dict method
    assert t.format_dict['rate'] == "1it/s"
    assert t.format_dict['elapsed'] == '0s'
    assert t.format_dict['remaining'] == '0s'
    assert t.format_dict

# Generated at 2022-06-14 13:43:43.126339
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    from matplotlib import rcParams
    from matplotlib import pyplot as plt

    default_toolbar = rcParams['toolbar']

    for leave in [True, False]:
        for wasion in [True, False]:
            for disable in [True, False]:
                for enable in [True, False]:
                    for leave in [True, False]:
                        for toolbar in ['toolbar', 'None']:
                            rcParams['toolbar'] = toolbar
                            pbar = tqdm_gui(total=10, disable=disable)
                            wfr = plt.get_current_fig_manager()
                            plt.ion()
                            pbar.wasion = wasion
                            pbar.leave = leave
                            pbar.close()
                            assert rcParams['toolbar'] == toolbar
                

# Generated at 2022-06-14 13:43:45.003595
# Unit test for method clear of class tqdm_gui
def test_tqdm_gui_clear():
    from .gui import tqdm_gui

    for _ in tqdm_gui(range(10)):
        pass

# Generated at 2022-06-14 13:43:50.094000
# Unit test for method display of class tqdm_gui
def test_tqdm_gui_display():
    import matplotlib.pyplot as plt
    import tempfile
    t = tqdm(total=100)
    for _ in range(20):  # force draw
        t.update()
    t.display()
    plt.draw()
    plt.pause(1e-9)
    with tempfile.TemporaryFile() as f:
        plt.savefig(f)

# Generated at 2022-06-14 13:43:56.760686
# Unit test for method close of class tqdm_gui
def test_tqdm_gui_close():
    """
    Test that tqdm_gui close work properly (no crash, only 1 instance)
    """
    import matplotlib as mpl
    mpl_toolbar = mpl.rcParams['toolbar']

    for i in tqdm_gui(range(10)):
        pass
    assert mpl.rcParams['toolbar'] == mpl_toolbar
    assert len(tqdm_gui._instances) == 0