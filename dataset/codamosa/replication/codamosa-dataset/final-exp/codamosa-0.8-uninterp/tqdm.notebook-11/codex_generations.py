

# Generated at 2022-06-14 13:58:40.771384
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # initialize a tqdm_notebook
    from time import sleep
    from IPython.display import clear_output
    with tqdm_notebook(total=100, desc="test_update") as pbar:
        pbar.update(0)
        # make sure that it is working properly
        assert pbar.n == 0
        assert pbar.container.children[1].value == 0
        sleep(0.05)
        # make sure that it is working properly
        assert pbar.n == 0
        # increment the progress bar
        pbar.update(10)
        assert pbar.n == 10
        sleep(0.05)
        # make sure that it is working properly
        assert pbar.n == 10
        assert pbar.container.children[1].value == 10
        # increment the progress bar
        pbar

# Generated at 2022-06-14 13:58:47.339124
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    bar = tqdm_notebook(
        [1, 2, 3],
        desc='test',
        total=5,
        leave=True,
        dynamic_ncols=True,
        bar_format='{desc}: {percentage:3.0f}%|{bar}|')
    # first progress bar
    assert bar.n == 3
    assert bar.ncols is None
    assert bar.container.children[-2].max == 5
    assert bar.container.layout.width is None
    assert bar.container.children[0].value == 'test:  60%'
    bar.reset(total=2)
    # second progress bar
    assert bar.n == 0
    assert bar.ncols == '100%'
    assert bar.container.children[-2].max == 2
    assert bar

# Generated at 2022-06-14 13:58:57.332330
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    try:
        from IPython.display import clear_output
    except ImportError:
        return None
    from tqdm import tnrange
    from time import sleep

    t = tnrange(10, desc='1st loop')
    assert len(t) == 10
    for i in t:
        sleep(0.1)
    t.close()

    t = tnrange(4, desc='2nd loop')
    for i in t:
        sleep(0.1)
        t.set_description("2nd loop (after {}/{})".format(i, len(t)))
        t.refresh()
        if i == 2:  # manual close
            t.close()
            break
    clear_output()

    t = tnrange(5, desc='manual close', leave=True)

# Generated at 2022-06-14 13:59:02.819105
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep

    tqdm_notebook().update(1)

    for _ in tqdm_notebook(range(3)):
        sleep(1)
        tqdm_notebook().update()

    for i in tqdm_notebook(range(3)):
        sleep(1)
        tqdm_notebook().update(i)


# Generated at 2022-06-14 13:59:11.351505
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Tests `tqdm.notebook.tqdm_notebook.display` method.
    """
    from unittest import TestCase
    from IPython.html.widgets import FloatProgress
    from IPython.display import clean_output
    from time import sleep

    class TqdmTest(TestCase):
        """
        Internal test class.
        """
        def setUp(self):
            self.test_tqdm = tqdm_notebook(total=3)
            self.test_tqdm.start()

        def test_display(self):
            self.assertEqual(self.test_tqdm.displayed, False)
            self.test_tqdm.display(close=True)
            self.assertEqual(self.test_tqdm.displayed, False)
           

# Generated at 2022-06-14 13:59:20.055735
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from sys import getsizeof
    t = tqdm_notebook(total=200, desc="test")
    assert t.container.children[0].value == "test"
    t.display()
    t.display("test |{bar}|")
    assert t.container.children[2].value == "test |<bar/>|"
    assert t.container.children[1]._model_id == t.container.children[1].model_id
    assert t.container.children[1]._view_count == t.container.children[1].view_count  # noqa
    assert t.container.children[1]._model_id != t.container.children[2]._model_id
    assert t.container.children[1]._view_count != t.container.children[2]._view_count  # no

# Generated at 2022-06-14 13:59:21.331336
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    for i in tqdm_notebook(range(10), desc="test", leave=True):
        pass

# Generated at 2022-06-14 13:59:24.055090
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm(total=4) as t:
        for i in range(4):
            t.update(1)


# Generated at 2022-06-14 13:59:34.637073
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    from datetime import timedelta
    from time import sleep

    t = trange(2, desc="a", bar_format="{percentage:3.0f}%|{bar}|{r_bar}")
    for i in t:
        sleep(0.2)
    assert t.__repr__() == '  50%|{bar}|{r_bar} a:   1it [00:00,  6.38it/s]'
    t.display()
    t.reset()
    for i in t:
        sleep(0.2)
    assert t.__repr__() == '100%|{bar}|{r_bar} a:   1it [00:00,  6.38it/s]'
    t.display()


test_TqdmHBox___repr__()

# Generated at 2022-06-14 13:59:47.184200
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test `tqdm_notebook.status_printer` function.
    """
    # pylint: disable=unused-variable
    # pylint: disable=redefined-outer-name
    import io
    from contextlib import closing
    from .utils import _range

    if IPY == 0:
        return "IProgress not found -> skipping test"

    with closing(io.StringIO()) as f:
        for total in _range(0, 2):
            for desc in ['', 'desc']:
                for ncols in _range(0, 100, 10):
                    for leave in [True, False]:
                        if ncols == 0:
                            ncols = None

# Generated at 2022-06-14 14:00:04.836839
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from random import randrange
    for total in [None, randrange(10, 17)]:  # None or > 10
        pbar = tqdm_notebook(total=total)
        # should fail to reset (for while)
        try:
            pbar.reset(5)
        except ValueError:
            pass
        else:
            assert False
        pbar.reset(total)
        # should now work
        pbar.reset(5)

# Generated at 2022-06-14 14:00:13.341267
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from IPython.html.widgets import HBox, FloatProgress, HTML

    t = tqdm_notebook(total=10)
    assert isinstance(t.container, HBox)
    assert isinstance(t.container.children[1], FloatProgress)
    assert isinstance(t.container.children[0], HTML)

    # test if resetting works
    t.reset(10)
    assert t.total == 10
    assert t.container.children[1].max == 10
    assert t.container.children[0].value == ''
    assert t.container.children[2].value == ''



# Generated at 2022-06-14 14:00:19.675632
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        from ipywidgets import FloatProgress
    except ImportError:
        # if ipywidgets not installed, ignore the test
        pass
    else:
        with tqdm_notebook(total=10) as t:
            t.clear()  # In the test of tqdm_notebook, t.close() is called.
            # t.close()  # after the test of tqdm_notebook, uncomment this line
            assert t.container.children[1] is not None and \
                isinstance(t.container.children[1], FloatProgress)

# Generated at 2022-06-14 14:00:24.858091
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from tqdm import tqdm_notebook
    bar = tqdm_notebook(total=10)
    bar.reset(total=0)
    assert bar.total == 0
    bar.update(1)
    assert bar.n == 1
    bar.reset(total=2)
    assert bar.total == 2
    bar.close()

# Generated at 2022-06-14 14:00:33.185357
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from unittest import TestCase, main

    class DisplayMock(TestCase):
        """Mock display for method display of class tqdm_notebook."""
        def __init__(self):
            self.args = []
            self.kwargs = []

        def __call__(self, *args, **kwargs):
            self.args.append(args)
            try:
                self.kwargs.append(kwargs)
            except:  # NOQA: E722
                self.kwargs.append({})

    # Initialize & run tests
    if IProgress is not None:  # pragma: no cover
        with DisplayMock() as display:
            with tqdm_notebook(total=2, file=display) as bar:
                bar.update()
                bar.update()

# Generated at 2022-06-14 14:00:37.026442
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    for i in range(4):
        pbar = tqdm_notebook(["a", "b", "c", "d"])
        pbar.update()
    for i in range(4):
        pbar = tqdm_notebook(["a", "b", "c", "d"])
        for c in pbar:
            pbar.update()

test_tqdm_notebook_update()

# Generated at 2022-06-14 14:00:41.469257
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    total = 100

    with tqdm_notebook(total=total) as t:
        t.clear(nolock=True)
        for i in _range(total):
            t.update()

if __name__ == "__main__":
    test_tqdm_notebook_clear()

# Generated at 2022-06-14 14:00:45.734417
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for method reset
    """
    import time
    for _ in tqdm_notebook(range(4), unit='test', total=4):
        time.sleep(1)

# Generated at 2022-06-14 14:00:55.686846
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    # Simple example
    tqdm_format = "{n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"
    pbar = tqdm_notebook(total=10, bar_format=tqdm_format)
    pbar.update()
    assert repr(pbar) == pbar.format_meter(**pbar.format_dict)
    pbar.close()
    # Another example with no total
    pbar = tqdm_notebook(total=None, bar_format=tqdm_format)
    pbar.update()
    assert repr(pbar) == pbar.format_meter(**pbar.format_dict)
    pbar.close()
    # Another example with no total and disabled iterations
    pbar = tq

# Generated at 2022-06-14 14:00:58.727098
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    with patch('tqdm._tqdm.tqdm.clear'):
        a = tnrange(100)
        a.clear()

# Generated at 2022-06-14 14:01:42.444249
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    # import IPython.core.display
    t = tqdm_notebook(total=100, miniters=20)  # instantiate
    t.update(5)  # initial update to show bar
    t.container.children[-2].bar_style = 'success'
    t.display('test1')  # test content change
    t.display(bar_style='warning')  # test style change
    t.display(close=True)  # close bar
    # IPython.core.display.clear_output(wait=1)

try:
    # do not use to_dict() because it'll break in IPython 1.x
    display({'application/vnd.jupyter.widget-view+json': {}})
except TypeError:
    pass  # we're not in

# Generated at 2022-06-14 14:01:51.560874
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    tqdm_notebook(["a", "b", "c"], file=open(os.devnull, 'w'))  # + dates


if __name__ == "__main__":
    # python tqdm/tqdm_notebook.py [-v] | [-h]
    # python tqdm/tqdm_notebook.py [-v] [-u] | [-h] (for unit test)
    # python tqdm/tqdm_notebook.py [-v] [-n] | [-h] (for speed test)
    from .tests import main
    main(__file__)

# Generated at 2022-06-14 14:01:56.025549
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Test for tqdm_notebook.status_printer method
    """
    try:
        with warnings.catch_warnings(record=True) as w:
            fp = tqdm_notebook.status_printer(None)
        assert len(w) > 0
    except ImportError:
        assert IProgress is None

if __name__ == '__main__':
    test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 14:02:08.582702
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    for n in tqdm_notebook(
            _range(1),
            total=1,
            unit=' loop',
            unit_scale=1,
            unit_divisor=1,
            ascii=False,
            miniters=1):
        pass
    for n in tqdm_notebook(
            _range(10),
            total=10,
            unit=' loop',
            unit_scale=1,
            unit_divisor=1,
            ascii=False,
            miniters=1):
        pass
    # Raise testing

# Generated at 2022-06-14 14:02:17.210278
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from IPython.display import clear_output
    from time import sleep
    from random import random

    # class-based API
    with tqdm_notebook(total=100) as pbar:
        for i in range(10):
            sleep(0.1)
            pbar.update(10)
    assert pbar.n == 100
    assert pbar.last_print_n == 100
    clear_output()

    # function API
    pbar = tqdm_notebook(total=100)
    for i in range(10):
        sleep(0.1)
        pbar.update(10)
    assert pbar.n == 100
    assert pbar.last_print_n == 100
    pbar.close()
    clear_output()

    # dynamic_ncols
    # NB: sometimes, on

# Generated at 2022-06-14 14:02:25.030103
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from nose.tools import assert_equal
    from nose.tools import assert_raises
    from nose.tools import assert_true
    from nose.tools import assert_false
    from nose.tools import assert_in
    from nose.tools import assert_greater
    from nose.tools import assert_greater_equal
    from nose.tools import assert_less_equal

    # Test error message
    def gen():
        for _ in tqdm_notebook(range(10)):
            raise RuntimeError()

    assert_raises(RuntimeError, list, gen())
    assert_equal(list(tqdm_notebook(range(10))), list(range(10)))



# Generated at 2022-06-14 14:02:33.729642
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import sys
    import time
    try:
        from unittest import mock
    except ImportError:  # <3k
        import mock

    with mock.patch.object(sys, 'stderr', mock.Mock()):
        with mock.patch('tqdm.tqdm.write') as write:
            w = tqdm_notebook(
                _range(3), file=sys.stderr, leave=False,
                mininterval=0, miniters=None,
                bar_format="{l_bar}{r_bar}")
            for i in w:
                # assert that `write` is called to display
                assert write.call_count == i + 1

# Generated at 2022-06-14 14:02:44.057288
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from io import StringIO
    from copy import copy
    from time import sleep

    from tqdm.auto import tqdm, trange

    try:
        from ipywidgets import IntProgress
    except ImportError:
        return 1

    with StringIO() as f:
        tqdm.pandas(desc='Loading data', unit='table',
                    total=1, mininterval=0, file=f).pandas()

        # Test 1:
        pbar = tqdm.status_printer(file=f, total=100)
        assert isinstance(pbar, IntProgress)
        assert f.getvalue() == ''  # not printed yet
        assert pbar.max == 100
        pbar.value = 5

        # Test 2:

# Generated at 2022-06-14 14:02:51.677418
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from unittest import TestCase

    class _tqdm_notebook_status_printer(TestCase):
        def test_1(self):
            bar = tqdm_notebook.status_printer(total=3, desc='A', ncols=100)
            self.assertEqual(bar.layout.width, '100px')
            self.assertEqual(bar.layout.display, 'inline-flex')
            self.assertEqual(bar.layout.flex_flow, 'row wrap')
            self.assertEqual(len(bar.children), 3)
            self.assertEqual(bar.children[0].value, 'A')
            self.assertEqual(bar.children[0].layout.flex, '1')
            self.assertEqual(bar.children[1].max, 3)
           

# Generated at 2022-06-14 14:02:54.179403
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    pass

if __name__ == '__main__':
    test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 14:03:47.061535
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """Test that tqdm_notebook(x, leave=True) and tqdm_notebook(x, leave=False)
    gives the same outputs"""
    from .utils import FormatCustom

    def test_leave(leave):
        T = tqdm_notebook(range(10), leave=leave)
        for _ in T:
            pass
        T.close()
        return T

    # If we are using a custom format, make sure that we test the formatted
    # value instead of the raw value (which will differ)
    ls1 = test_leave(True)._format_meter(FormatCustom.format)
    ls2 = test_leave(False)._format_meter(FormatCustom.format)
    assert ls1 == ls2



# Generated at 2022-06-14 14:03:53.982257
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    import sys
    pbar = tqdm_notebook(total=10, file=sys.stderr)
    for i in range(10):
        pbar.update()

    pbar = tqdm_notebook(total=10)
    for i in range(10):
        pbar.update()

    assert repr(pbar) == "0/10\r[#              ] 0%|          | 0/10 [00:00<?, ?it/s]"


if __name__ == '__main__':
    test_tqdm_notebook()

# Generated at 2022-06-14 14:04:01.363115
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    Tests that repeatedly applying tqdm updates without finishing works.
    """
    from time import sleep
    from numpy.random import randint

    for _ in tqdm(range(4)):  # test 4 times
        for i in tqdm(range(5)):  # interruptible loop
            sleep(randint(2))  # random wait time


if __name__ == '__main__':
    test_tqdm_notebook_update()

# Generated at 2022-06-14 14:04:05.670739
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm_notebook(total=1, ascii=True, dynamic_ncols=True) as pbar:
        for i in pbar:
            assert pbar.last_print_t is None
            assert re.search(r"\r[^\r]*\r[# ]", pbar.format_meter())
            break



# Generated at 2022-06-14 14:04:08.188621
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import itertools
    pbar = tqdm_notebook(itertools.count())
    for _ in range(5):
        pbar.reset()
        for i in pbar:
            if i > 50:
                pbar.reset()
                break
            pbar.update()


if __name__ == "__main__":
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:04:10.968137
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm(total=5) as pbar:
        for i in pbar:
            pass
        assert pbar.n == 5
        assert pbar.last_print_n == 5



# Generated at 2022-06-14 14:04:18.531305
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    try:
        from unittest import mock
    except ImportError:  # < Python 3.3
        import mock

    with mock.patch('IPython.display.clear_output') as f:
        a = tqdm_notebook(range(10), disable=False)
        a.update()
        f.assert_called_with(wait=True)
        a = tqdm_notebook(range(10), disable=True)
        a.update()
        f.assert_not_called()



# Generated at 2022-06-14 14:04:22.712140
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from .std import tqdm as std_tqdm
    for n in tqdm_notebook(range(0, 10), total=10):
        tqdm_notebook.reset()
        for i in tqdm_notebook(range(0, 10), total=10):
            pass

# Generated at 2022-06-14 14:04:26.367746
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    for i in tqdm(range(8), total=10):
        assert i == i  # NOQA: F821

# Generated at 2022-06-14 14:04:29.660761
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    for _ in tqdm_notebook(range(100)): pass
    for _ in tqdm_notebook(range(100), leave=True, ncols=100, desc="test"): pass


# Generated at 2022-06-14 14:06:07.468904
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for method `display`.
    """
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    # Test `display` method of class `tqdm_notebook`
    # without IPython/Jupyter dependencies
    tqdm_notebook.disp = MagicMock()
    tqdm_notebook.IPY = 0
    tqdm_notebook.HTML = MagicMock()
    tqdm_notebook.FloatProgress = MagicMock()
    tqdm_notebook.ContainerWidget = MagicMock()
    tqdm_notebook.HBox = MagicMock()
    tqdm_notebook.IProgress = None
    tqdm_notebook.display = MagicMock()
    tn

# Generated at 2022-06-14 14:06:14.651841
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # Regular behaviour
    pbar = tqdm_notebook.status_printer(file=None, total=100)
    assert isinstance(pbar, TqdmHBox)
    assert isinstance(pbar.children[0], HTML)
    assert isinstance(pbar.children[1], IProgress)
    assert isinstance(pbar.children[2], HTML)
    assert pbar.children[-2].layout.width == "100%"
    assert pbar.children[1].layout.flex == "2"
    assert pbar.layout.display == "inline-flex"
    assert pbar.layout.flex_flow == "row wrap"
    ltext, _, rtext = pbar.children
    assert ltext.value == ""
    assert rtext.value == ""

    # ncols

# Generated at 2022-06-14 14:06:25.530247
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    ipy = 0
    if hasattr(tqdm_notebook, "container"):
        ipy = 4
    else:  # IPython 3.x / 2.x
        ipy = 32
        try:
            from IPython.html.widgets import HBox
            from IPython.html.widgets import FloatProgressWidget as IProgress
            ipy = 3
        except ImportError:
            try:
                from IPython.html.widgets import HBox
                from IPython.html.widgets import FloatProgressWidget as IProgress
                ipy = 2
            except ImportError:
                IProgress = None
                ipy = 0

    assert ipy > 0, "ipywidgets not found!"

    progress = tqdm_notebook(total=10)
    progress.update(1)

# Generated at 2022-06-14 14:06:33.155753
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    # Make sure we have a reference to a real TqdmHBox-class instance
    pbar = tqdm(total=100, desc="a TqdmHBox instance",
                bar_format="{l_bar}<bar/>{bar}|")
    hb = pbar.container

    def _wrap_in_br(s):
        return "<br/>".join(s.strip().split("\n"))

    # Test whether __repr__ prints the same as format_meter
    bar_format = hb._repr_json_(pretty=False).get("bar_format")
    assert _wrap_in_br(hb.__repr__(pretty=False)) == hb.format_meter(bar_format=bar_format)
    # Test whether _repr_pretty_ prints the same as format_meter

# Generated at 2022-06-14 14:06:34.884672
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    tqdm_notebook.status_printer(None)



# Generated at 2022-06-14 14:06:38.057549
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from tqdm import tnrange  # NOQA
    for b in [True, False]:
        for i in tnrange(2, disable=b):
            list(tnrange(3, disable=b))

# Generated at 2022-06-14 14:06:44.107149
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    for leave in [False, True]:
        tot = 100
        t = tqdm(total=tot, leave=leave)
        for i in range(tot):
            t.update()
        t.reset(total=10)
        for i in range(tot):
            t.update()
        t.close()
        assert t.total == 10
        assert t.n == 10
        assert t.ncols is None
        assert t.container.children[-2].layout.width is None

# Generated at 2022-06-14 14:06:50.221178
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """
    Unit test for tqdm_notebook method update.

    It generates a list of 10 random numbers and then calls
    function tqdm_notebook_update to update the data.
    """
    import random
    import time
    L = []
    for _ in trange(10):
        L.append(random.random())
        time.sleep(0.1)
    assert len(L) == 10
    for i in range(10):
        assert 0 <= L[i] <= 1

# Generated at 2022-06-14 14:06:53.268578
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():  # pragma: no cover
    from .tests import tqdm_notebook_status_printer
    tqdm_notebook_status_printer.main(tqdm_notebook)

# Generated at 2022-06-14 14:07:04.224844
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """Test for method `reset` of class `tqdm_notebook`."""

    from .utils import TestCase

    # Unit tests for `tqdm_notebook`
    class Test_tqdm_notebook_reset(TestCase):
        def setUp(self):
            self.tqdm = tqdm_notebook
            self.kwargs = {'total': 10}

        def tqdm_widget(self, **kwargs):
            """Helper function to test `tnrange`"""
            kwargs.update(self.kwargs)
            it = self.tqdm(**kwargs)
            it.update(1)
            self.assertEqual(it.n, 1)
            it.update(1)
            self.assertEqual(it.n, 2)
            it.reset()
