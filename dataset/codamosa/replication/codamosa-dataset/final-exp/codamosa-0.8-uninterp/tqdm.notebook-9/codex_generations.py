

# Generated at 2022-06-14 13:58:26.352768
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import doctest
    doctest.run_docstring_examples(tqdm_notebook.status_printer, globals())

# Generated at 2022-06-14 13:58:37.611464
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """Test method __iter__ of class tqdm_notebook."""
    import pytest
    from random import randrange, seed  # NOQA
    from time import sleep  # NOQA

    seed(1)
    for i in tnrange(10, desc="outer loop"):
        for j in tnrange(10, desc="inner loop"):
            sleep(randrange(1000) / 1e6)
            if i == j == 5:
                raise IndexError("i == j == 5")  # to test exception handling
        if i == 7:
            break  # to test early break handling

    with pytest.raises(ImportError):
        # test error handling
        # GH-562
        tqdm._instances.clear()

# Generated at 2022-06-14 13:58:44.235819
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from unittest import main

    import IPython

    if IPY == 0 or not hasattr(IPython, 'display'):
        return

    # Tests printing of blank progress bar
    try:
        tqdm_notebook.status_printer(None)
    except ImportError:
        pass
    else:
        raise Exception("Expected ImportError")

    # Tests printing of progress bar with unknown total
    # HACK: 'None' used to indicate a progress bar with unknown total
    progress_bar = tqdm_notebook.status_printer(None, 'None')
    try:
        display(progress_bar)
    except Exception:
        raise Exception
    finally:
        try:
            progress_bar.close()
            progress_bar.layout.display = 'none'
        except Exception:
            pass



# Generated at 2022-06-14 13:58:47.983135
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    try:
        for i in tqdm_notebook([1, 2, 3]):
            pass
    except ImportError:
        return
    except:  # NOQA
        assert False, "update method of class tqdm_notebook" \
                      "should not raise an exception"

# Generated at 2022-06-14 13:58:57.712577
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from json import loads
    fp = sys.stderr

    for desc, leave, ncols in (
            ('desc', False, None),
            ('', False, None),
            ('desc', True, None),
            ('', True, None),
            ('desc', False, 100),
            ('', False, 100),
            ('desc', True, 100),
            ('', True, 100),
            ('', False, "100px"),
            ('', False, "100%"),
            # IPython 7+
            # ('', False, '100%'),
            # ('', False, '100px'),
            # ('', False, 100),
    ):

        class MyTqdm(tqdm_notebook):
            def __init__(self, *args, **kwargs):
                super(MyTqdm, self).__

# Generated at 2022-06-14 13:59:09.610612
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from IPython.display import display, clear_output  # NOQA
    from ipywidgets import Output  # NOQA
    from re import search  # NOQA
    from sys import stdout  # NOQA

    with Output():
        for i in tqdm_notebook(
                range(4), total=4, desc="Lorem", bar_format="{desc}: {n_fmt}/{total_fmt} [{bar}] {postfix}",
                unit='foo', dynamic_ncols=True):
            # print("lorem ipsum\nlorem ipsum\nlorem ipsum\nlorem ipsum\nlorem ipsum\nlorem ipsum")
            # stdout.flush()
            stdout.write("\r\x1b[2K\r")


# Generated at 2022-06-14 13:59:14.447051
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    # a simple test to avoid adding a new test
    try:
        import nose  # NOQA
    except ImportError:
        raise nose.SkipTest
    p = tqdm(total=10, desc="desc", leave=True)
    for i in p:
        if i == 5:
            p.clear()
        p.update()
    p.close()



# Generated at 2022-06-14 13:59:20.183206
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from distutils.version import LooseVersion
    import ipywidgets

    if LooseVersion(ipywidgets.__version__) < LooseVersion('7.0.0'):
        raise AssertionError(
            "IPython/Jupyter tqdm update test requires ipywidgets >= 7.0.0")

    from IPython.utils.capture import capture_output
    with capture_output() as io:
        try:
            pbar = tqdm(total=100)
            for i in range(5):
                pbar.update(5)
                raise Exception()
        except Exception:
            pbar.clear()
            pbar.close()

    err = io.stderr.getvalue()
    assert '100%|#####6|' in err, err

# Generated at 2022-06-14 13:59:25.604336
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for the method `tqdm_notebook.display`.
    """
    import unittest

    class Test_tqdm_notebook_display(unittest.TestCase):
        """Unit tests for `tqdm_notebook.display`"""

        def test_display(self):
            """
            Unit tests for `tqdm_notebook.display`.
            """
            from tqdm.notebook import tqdm_notebook
            from tqdm.auto import tqdm
            t = tqdm(range(4), desc="test", ncols=1000)
            t.display()
            t.close()
            for _ in tqdm_notebook(range(4), desc="test", ncols=1000):
                pass

# Generated at 2022-06-14 13:59:29.695776
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from random import randrange
    from time import sleep
    iterable = [randrange(1000) for _ in range(1000)]

    progress_bar = tqdm_notebook(
        iterable,
        miniters=len(iterable),
        mininterval=0.1,
        total=1000,
        unit_scale=True,
        unit='iB',
        leave=True)

    for i in progress_bar:
        sleep(0.01)
