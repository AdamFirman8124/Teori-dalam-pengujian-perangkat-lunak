

# Generated at 2022-06-14 13:58:35.668516
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time
    import warnings

    # Unit test for method reset of class tqdm_notebook
    with warnings.catch_warnings(record=True) as ws:
        with tqdm_notebook(total=3) as bar:
            bar.update()
            bar.update()
            bar.reset()
            bar.update()
    assert len(ws) == 0

# Generated at 2022-06-14 13:58:41.362771
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # Note: "from __future__ import division" is important
    with tqdm_notebook(range(10), total=10.0) as t:
        for i in t:
            pass
    assert t.n == 10
    assert t.total == 10.0


if __name__ == "__main__":  # pragma: no cover
    from pytest import main
    main([__file__.replace('.pyc', '.py')])

# Generated at 2022-06-14 13:58:47.824681
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # Create tqdm_notebook
    total = 2
    iterable = _range(total)
    with tqdm_notebook(iterable) as t:
        assert t.total == total
        # Check iterability
        for obj in t:
            pass
        assert t.n == total  # iteration finished
        assert t.n == t.total

    # Create tqdm_notebook with total=None
    iterable = _range(total)
    with tqdm_notebook(iterable, total=None) as t:
        assert t.total == max(total, 100)
        # Check iterability
        for obj in t:
            # check `t.n` incrementing as we iterate
            assert t.n == obj  # for-loop variable equals t.n
            assert t.n <= t.total

# Generated at 2022-06-14 13:58:54.551455
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from os import devnull

    for desc in (None, "Hello"):
        for total in (None, 0, 100):
            pbar = tqdm_notebook._status_printer(devnull, total, desc)
            _, i_pbar, _ = pbar.children
            assert i_pbar.min == 0
            assert i_pbar.max == total
            assert i_pbar.bar_style == 'info' if total is None else ''

# Generated at 2022-06-14 13:58:59.852472
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    t = tqdm(total=100)
    for i in range(50):
        t.update()
    # Ideally, update() should now be able to display n=50
    # in a single shot. However, in practice this doesn't seem to work.
    # So instead we call update() as many times as necessary to reach n=50.
    # Note that close() will be called by unit tests, so was leaving
    # the bar in a bad state.
    # The new reset() method addresses this issue and fix the test.
    while t.n < 50:
        t.update(n=t.n+1)

# Generated at 2022-06-14 13:59:05.702971
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():  # pragma: no cover
    for i in tqdm_notebook(range(4)):
        pass

    for i in tqdm_notebook(range(4)):
        raise KeyboardInterrupt()

    for i in tqdm_notebook(range(4)):
        break


if __name__ == "__main__":  # pragma: no cover
    test_tqdm_notebook_close()

# Generated at 2022-06-14 13:59:13.232847
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from IPython.display import HTML

    tqdm_notebook(total=10)
    tqdm_notebook(total=10, disable=True)
    tqdm_notebook(total=10, desc="desc", position=1)
    with tqdm_notebook(total=10, desc="desc", leave=True) as t:
        assert t.displayed
    with tqdm_notebook(total=0, desc="desc", leave=True) as t:
        assert not t.displayed
    with tqdm_notebook(total=10, desc="desc", leave=True, ncols=100) as t:
        assert isinstance(t.container, HTML)
    with tqdm_notebook(total=10, colour="red") as t:
        assert t.colour == "red"



# Generated at 2022-06-14 13:59:17.862060
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .tests import pretest_posttest  # NOQA

    with pretest_posttest():
        pbar = tqdm_notebook()
        pbar.display(bar_style='info', close=True)
        assert not pbar.n
        try:
            assert pbar.container.children[-2].bar_style != 'info'
        except Exception:
            pass



# Generated at 2022-06-14 13:59:24.173693
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for the method `reset` of the class `tqdm_notebook`
    It is also tested implicitly in :meth:`test_tqdm.main.test_gui_update_gui_save`
    """
    import time
    import copy
    from .tqdm import trange
    from .utils import format_interval

    # save old values
    old_format_meter = tqdm_notebook._format_meter

    def new_format_meter(self, *args, **kwargs):
        """
        Returns a formatted string just like the original one
        except that it also saves its parameters in the dict
        `self.last_format_args`.
        """
        # format str
        str_ = old_format_meter(self, *args, **kwargs)
        # save arguments before closing

# Generated at 2022-06-14 13:59:29.766035
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    with tqdm_notebook(total=9) as pbar:
        for i in range(3):
            for j in tqdm_notebook(range(3)):
                sleep(0.01)
                pbar.update()


# Run unit test if called
if __name__ == '__main__':
    test_tqdm_notebook___iter__()

# Generated at 2022-06-14 13:59:46.766472
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time
    with tqdm_notebook(total=10) as bar:
        for i in range(10):
            time.sleep(0.1)
            bar.update()
            if i >= 5:
                bar.reset(total=20)
        bar.reset()

# Generated at 2022-06-14 13:59:55.691435
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from nose.tools import assert_raises
    from time import sleep

    with tnrange(1) as t:
        for i in t:
            # Using .update() here is only for testing purpose
            t.update()
            raise SystemExit

    with tnrange(1, leave=True) as t:
        for i in t:
            t.update()
            raise SystemExit

    # ensure error does not linger between tests
    sleep(.01)

    with tnrange(1) as t:
        for i in t:
            t.update()
            assert_raises(SystemExit, raise_exc, SystemExit)

    with tnrange(1, leave=True) as t:
        for i in t:
            t.update()
            assert_raises(SystemExit, raise_exc, SystemExit)



# Generated at 2022-06-14 14:00:02.586331
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from pytest import raises
    from .gui import tqdm_gui
    from .auto import tqdm as tqdm_auto
    tot = 10

    for cls_ in (tqdm_notebook, tqdm_auto, tqdm_gui):
        with raises(KeyboardInterrupt):
            for _ in cls_(total=tot):
                raise KeyboardInterrupt

        with raises(ZeroDivisionError):
            for _ in cls_(total=tot):
                raise ZeroDivisionError

# Generated at 2022-06-14 14:00:05.916977
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep
    for i in tqdm_notebook(range(10), desc="test", leave=False):
        sleep(0.1)


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_notebook()

# Generated at 2022-06-14 14:00:11.219484
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit tests for the `IPython.display` functionality of `tqdm.notebook`
    """
    tn = tqdm_notebook(total=1, leave=True, desc='test')
    tn.display()
    tn.display(bar_style='warning', check_delay=False)
    tn.display('test message', check_delay=False)
    tn.display(bar_style='success', check_delay=False)
    tn.update()
    tn.display(close=True, check_delay=False)

# Generated at 2022-06-14 14:00:14.229276
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    """Test update method. """
    total = 10
    tn = tqdm_notebook(total=total)
    for i in range(total):
        tn.update()
    tn.close()



# Generated at 2022-06-14 14:00:16.281409
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        for i in trange(4):
            raise KeyboardInterrupt
            yield i
    except KeyboardInterrupt:
        pass


# Generated at 2022-06-14 14:00:23.648309
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    kwargs_ = {
        'total': 100,
        'desc': 'test description',
        'ncols': 80,
    }

    for ipy in range(4, 2, -1):
        with std_tqdm.set_lock(False):
            with tqdm_notebook.set_lock():
                container = tqdm_notebook.status_printer(
                    file=None, **kwargs_)

                # number of children need to be 3: left info, progress bar, right info
                assert (hasattr(container, 'children') and
                        len(container.children) == 3)

                ltext, pbar, rtext = container.children
                assert (isinstance(ltext, HTML) and
                        isinstance(rtext, HTML) and
                        isinstance(pbar, IProgress))



# Generated at 2022-06-14 14:00:26.117662
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    feedback = []
    x = tqdm_notebook(range(5), leave=True, desc="the loop")
    try:
        for _ in x:
            feedback.append(x.n)
            if x.n >= 1:
                raise ValueError()
    except ValueError:
        pass
    assert feedback == [0, 1]
    assert x.n == 1



# Generated at 2022-06-14 14:00:33.960493
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep
    from random import random
    from IPython.display import clear_output
    from tqdm import tnrange, tqdm_notebook

    def _test(cls, *args, **kwargs):
        for _ in cls(*args, **kwargs):
            sleep(random() / 100)

    class NB(tqdm_notebook):
        def display(self, msg=''):
            clear_output(wait=True)
            super(NB, self).display(msg)

    # Simple notebook test
    _test(NB, 100)
    _test(NB, 'Hello !', 100)
    _test(NB, 'Hello !', 'Goodbye !', 100)
    _test(NB, 'Hello !', 'Goodbye !', total=None)

# Generated at 2022-06-14 14:01:04.902188
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    try:
        from IPython.display import clear_output
    except ImportError:
        from IPython.html.widgets import widget_output

    # keep state across all bars (avoid separate counter/total/display)
    t = tqdm_notebook(total=100)
    t.displayed = False  # avoid print
    for i in t:
        t.update()
        if i >= 10 and i <= 0:
            t.displayed = True  # force print
        if i >= 20:
            t.colour = '#39FF14'
        t.set_postfix(i=str(i))

# Generated at 2022-06-14 14:01:15.955075
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    # IPython is not available by default
    # so we import it here only for testing purposes
    # (Not used yet in the whole script)
    try:
        from IPython.display import display  # NOQA: F401
    except ImportError:
        pass
    # TODO: test bar_style, pbar.value, ...
    # for msg, pos, clear, bar_style, check_delay in product:
    t = tqdm_notebook(total=100)
    t.displayed = True
    t.display(pos=1)
    t.display(pos=10)


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_notebook_display()

# Generated at 2022-06-14 14:01:17.671389
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    for _ in tqdm_notebook(range(1)):
        pass



# Generated at 2022-06-14 14:01:24.482605
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():  # noqa: D102
    from io import StringIO
    tqdm_notebook.status_printer(StringIO(), 20, "Lorem ipsum")


# Unit test this module
if __name__ == '__main__':
    import unittest

    class TestTqdmNotebook(unittest.TestCase):  # noqa: D101
        def setUp(self):  # noqa: D102
            try:
                self.range = xrange
            except NameError:
                self.range = range


# Generated at 2022-06-14 14:01:27.827550
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # Test attributes
    tqdm_notebook.status_printer(file=sys.stderr,
                                 total=10,
                                 desc='Desc',
                                 ncols=100)

# Generated at 2022-06-14 14:01:39.131092
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from tqdm import tqdm
    from tqdm._tqdm import TMonitor
    from tqdm._tqdm_gui import _range

    # Test TMonitor
    t = TMonitor(0)
    t.tot = 100
    # test display of a 0/100 bar
    t.display(check_delay=False)
    # assert t.bar._repr_html_() == '<i ...'  # assert repr() is ugly
    assert tqdm(t.bar) == "[{bar}]"
    # assert t.bar
    assert tqdm(t.bar, ncols=500) == "[{bar}]"

    # test display of a 100/100 bar
    t.update(100)
    t.display_factor = 1
    t.display(check_delay=False)
   

# Generated at 2022-06-14 14:01:51.993945
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    ncols = 100  # test ncols=100%
    tqdm_notebook([], total=10, ncols=ncols)  # test unknown total
    tqdm_notebook([], total=0, ncols=ncols)  # test zero total
    tqdm_notebook([]).display()  # test zero total and default ncols=-1
    # test ncols=100px
    tqdm_notebook([], ncols=str(ncols) + 'px')
    # test ncols=100%
    tqdm_notebook([], ncols=str(ncols) + '%')
    tqdm_notebook([]).display(ncols=None)  # test None ncols

# Generated at 2022-06-14 14:01:54.489242
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    from random import random
    with tqdm_notebook(total=2) as pbar:
        for _ in range(2):
            pbar.update()
            sleep(0.1 + random())
            pbar.set_description("Desc {:0.0f}".format(random() * 100))



# Generated at 2022-06-14 14:02:07.269378
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep
    from tqdm import tnrange
    from numpy.random import randint
    from numpy.linalg import norm

    for i in tnrange(1, 7):
        # test simple update
        with tnrange(100, desc='outer loop: ') as t1:
            for j in t1:
                sleep(randint(0, 3) * .001)
        sleep(1)  # sleep between loops

        # test manual update
        with tnrange(100, desc='outer loop: ') as t1:
            for j in range(100):
                sleep(randint(0, 3) * .001)
                t1.update(1)

        # test even more manual update

# Generated at 2022-06-14 14:02:15.761375
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from .std import tqdm
    from time import sleep

    # avoid printing "total=?" in Python2.7

# Generated at 2022-06-14 14:03:09.147042
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Test the status_printer method of tqdm_notebook, especially the layout"""
    tq = tqdm_notebook.status_printer(None, total=100)
    # default
    if IPY == 32:
        assert tq.layout.width == '100%'
        assert tq.layout.display == 'inline-flex'
        assert tq.layout.flex_flow == 'row wrap'
    # ncols=None
    tq = tqdm_notebook.status_printer(None, total=100, ncols=None)
    if IPY == 32:
        assert tq.layout.width == '100%'
        assert tq.layout.display == 'inline-flex'
        assert tq.layout.flex_flow == 'row wrap'
    # ncols=int

# Generated at 2022-06-14 14:03:20.062122
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .tests import TestCase, _range
    from .tests.gui import closing, on_linux

    class Test_tqdm_notebook(TestCase):
        def test_close(self):
            with closing(tqdm_notebook(total=10, leave=False)) as t:
                for _ in _range(10):
                    t.update()
            self.assertFalse(t.displayed)

        @on_linux
        def test_close_with_error(self):
            with closing(tqdm_notebook(total=10, leave=False)) as t:
                for _ in _range(5):
                    t.update()
                raise Exception()


# Generated at 2022-06-14 14:03:22.413920
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from .tests import tests
    tests.test_tqdm_notebook_display(__name__)

# Generated at 2022-06-14 14:03:31.557298
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .std import tqdm as tqdm_py
    from .std import tqdm as tqdm_py3
    from .std import trange as trange_py3
    from .std import trange as trange_py
    with tqdm_notebook(unit='iter', leave=True) as bar:
        pass
    with tqdm_notebook(unit='iter', leave=True) as bar:
        raise StopIteration
    with tqdm_notebook(unit='iter', leave=True) as bar:
        raise RuntimeError
    with tqdm_notebook(unit='iter', leave=True) as bar:
        raise KeyboardInterrupt
    with tqdm_py(unit='iter', leave=True) as bar:
        raise KeyboardInterrupt  # not caught if not in iterating context
   

# Generated at 2022-06-14 14:03:41.932573
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    msg = "<test: `tqdm_notebook.display` method>"
    if IProgress is None:
        return  # pragma: no cover
    t = tqdm_notebook(total=100)
    t.display(msg=msg)
    assert t.container.children[0].value == msg
    assert t.container.children[1].bar_style == ''
    t.display(bar_style='info')
    assert t.container.children[1].bar_style == 'info'
    t.display(bar_style='danger')
    t.display()  # check for no crashes


if __name__ == '__main__':
    from unittest import main
    main()

# Generated at 2022-06-14 14:03:49.100116
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Tests tqdm_notebook.status_printer() against three cases:
    No total specified, total = 1, total = 10 (bar > 0)
    """
    for total in [None, 1, 10]:
        with tqdm_notebook(total=total) as progress:
            progress.n = 0
            if total:
                progress.refresh()
            assert progress.displayed
            progress.displayed = False
            progress.n = progress.total - 1
            progress.refresh()
            assert progress.displayed

# Generated at 2022-06-14 14:03:51.779621
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(unit_scale=1, unit="B") as t:
        t.update(2)
        assert t.n == 2
        t.update(2)
        assert t.n == 4

# Generated at 2022-06-14 14:03:58.078652
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    Unit test for method status_printer of class tqdm_notebook
    """
    # import warnings
    # with warnings.catch_warnings():
    #     warnings.filterwarnings('ignore')
    import unittest2 as unittest
    # import unittest
    if IProgress:
        # Unit test for method status_printer of class tqdm_notebook
        # without total
        class test_tqdm_notebook_status_printer_without_total(unittest.TestCase):
            """
            Unit test for method status_printer of class tqdm_notebook
            without total
            """
            def setUp(self):
                self.bar = tqdm_notebook.status_printer(None, None)

# Generated at 2022-06-14 14:04:02.967488
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():  # pragma: no cover
    ipw = tqdm_notebook.status_printer(None, 10)
    assert isinstance(ipw, TqdmHBox)
    children = ipw.children
    assert isinstance(children[0], HTML)
    assert isinstance(children[1], IProgress)
    assert isinstance(children[2], HTML)

# Generated at 2022-06-14 14:04:06.985528
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    with open('/dev/null', 'w') as fp:
        c = tqdm_notebook.status_printer(fp, total=100)
        # assert c.pbar.max == 100
        # c.close()



# Generated at 2022-06-14 14:06:10.159799
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    for i in trange(4, desc='1st loop'):
        for j in trange(5, desc='2nd loop', leave=False):
            sleep(0.01)
        trange.reset(total=9)
        for j in trange(9, desc='2nd loop', leave=False):
            sleep(0.01)



# Generated at 2022-06-14 14:06:14.127951
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    for i in range(3):
        with tqdm_notebook(total=1) as pbar:
            pbar.reset(total=int(pbar.total / 2))
            sleep(.1)
            pbar.reset(total=int(pbar.total * 2))
            sleep(.1)


if __name__ == "__main__":
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:06:15.280783
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm(total=1) as t:
        t.update(1)



# Generated at 2022-06-14 14:06:20.909511
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # Check that tnrange works with manual updates
    prog = tnrange(8, desc='TEST')
    for _ in prog:
        prog.set_description_str('TEST IT')
        if prog.n == 2:
            break
    prog.n = 6
    prog.close()


if __name__ == "__main__":
    test_tqdm_notebook_update()

# Generated at 2022-06-14 14:06:30.595671
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from sys import stderr
    from time import sleep
    from copy import deepcopy

    # Test 1: display=False
    tq = tqdm_notebook(total=5, file=stderr, display=False)
    sleep(0.01)
    tq.reset()
    sleep(0.01)
    tq.close()

    # Test 2: display=True
    tq = tqdm_notebook(total=5, file=stderr, display=True)
    sleep(0.01)
    try:
        tq.reset()
        sleep(0.01)
    except Exception:
        pass
    tq.close()

    # Test 3: No total
    tq = tqdm_notebook(leave=False)
    sleep(0.01)

# Generated at 2022-06-14 14:06:40.642820
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():  # pragma: no cover
    import time
    from tqdm import _supports_unicode  # for py2 py3 compat
    for t in (tqdm, tnrange):
        with t(total=10) as pbar:
            for i in range(10):
                time.sleep(0.5)
            pbar.reset(leave=True)
        assert pbar.n == 0, "expected n=0, got {}".format(pbar.n)
        assert pbar.total == 10, "expected total=10, got {}".format(
            pbar.total)
        assert pbar.format_dict['bar_format'].split()[-3:] == [
            _supports_unicode and '10' or u'10', '0', '10']

# Generated at 2022-06-14 14:06:45.253230
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    n = 3
    try:
        for _ in tqdm_notebook(range(n)):
            raise Exception("123")
    except Exception:
        pass
    assert _.n == 0, "tqdm_notebook.update is not working properly"

if __name__ == "__main__":
    test_tqdm_notebook_update()

# Generated at 2022-06-14 14:06:48.398879
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    with tqdm_notebook(total=2) as pbar:
        for i in range(3):
            pbar.display(pos=i)
    pbar.container.close()  # for Coverage

# Generated at 2022-06-14 14:06:56.721954
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():  # pragma: no cover
    import random
    import time
    random.seed(0)

    # Test nested bars
    a = tqdm_notebook(tqdm_notebook(range(10), leave=False), leave=False)
    assert a.dynamic_ncols  # check dynamic_ncols is enabled

    # Test basic bar
    b = tqdm_notebook(range(10))
    for _ in b:
        time.sleep(0.01)

    # Test nested bars with manual update, and reset
    with tqdm_notebook(total=10) as a:
        for i in range(10):
            time.sleep(random.random())

# Generated at 2022-06-14 14:06:59.869579
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from nose.tools import assert_equal
    from .tests.test_tqdm_notebook import test_tqdm_notebook___iter__
    test_tqdm_notebook___iter__()

