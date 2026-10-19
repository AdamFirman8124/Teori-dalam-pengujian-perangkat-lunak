

# Generated at 2022-06-14 13:58:19.754852
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    container = tqdm_notebook.status_printer(sys.stdout, 100, "test_desc", 20)
    assert container.children[-2].max == 100
    assert container.children[-2].layout.width == "20px"
    assert container.children[0].value == "test_desc"
    assert container.children[-1].value == ""
    assert container.children[-2].value == 0
    assert container.children[-2].bar_style == ""
    assert container.children[-2].style.bar_color == ""

    container = tqdm_notebook.status_printer(sys.stdout, 100, "", 20)
    assert container.children[0].value == ""
    assert container.children[-1].value == ""
    assert container.children[-2].value == 0

# Generated at 2022-06-14 13:58:23.010181
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import nose

    t = tnrange(4)
    for i in t:
        t.clear()
        if i == 3:
            return None
    nose.tools.assert_equal(i, 3)

# Generated at 2022-06-14 13:58:25.187664
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    a = tqdm_notebook(total=5)
    a.reset(6)
    for _ in a:
        pass
    assert a.n == 6

# Generated at 2022-06-14 13:58:31.394190
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from .gui import tnrange
    from time import sleep
    from random import random

    for i in tnrange(4, desc='1st loop'):
        for j in tnrange(100, desc='2nd loop'):
            sleep(random() / 200.0)
        if random() < 0.1:
            raise Exception("Boom!")
        if random() < 0.5:
            break
    print('Well done!')

# Generated at 2022-06-14 13:58:35.713218
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        tqdm_notebook(total=2, leave=False).clear()
    except:
        raise AssertionError("Failed to clear tqdm_notebook")


if __name__ == '__main__':
    test_tqdm_notebook_clear()

# Generated at 2022-06-14 13:58:42.378687
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    import sys
    try:
        from unittest.mock import patch
    except ImportError:  # Python < 3.3
        from mock import patch

    with patch('sys.stderr', sys.stdout) as sys_stderr:
        for _ in tqdm_notebook(range(3)):
            pass
        assert sys_stderr.getvalue() == '100%|##########| 3/3 [00:00<?, ?it/s]\n'
        sys_stderr.close()

# Generated at 2022-06-14 13:58:52.966003
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    # case 1: when there is no pbar
    h = TqdmHBox()
    assert h.__repr__(pretty=False) == 'HBox(children=(HTML(value=\'\'), HTML(value=\'\'), HTML(value=\'\')))'
    assert h.__repr__(pretty=True) == 'HBox(children=(HTML(value=\'\'), HTML(value=\'\'), HTML(value=\'\')))'
    assert h._repr_pretty_(None, pretty=True) is None
    assert h._repr_pretty_(None, pretty=False) is None
    assert h._repr_json_(pretty=True) == {}
    assert h._repr_json_(pretty=False) == {}

    # case 2: when there is pbar
    h = TqdmHBox()
    h

# Generated at 2022-06-14 13:58:59.070949
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Issue #858: Trailing spaces in tqdm bar
    """
    with tqdm_notebook(total=10) as pbar:
        for i in range(10):
            pbar.update()
            try:
                assert(" " not in pbar.container.__repr__(pretty=True))
            except:
                import sys
                import traceback
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                raise ValueError("Trailing spaces found in progress bar!")

# Generated at 2022-06-14 13:59:02.450410
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    # with total
    t = tqdm_notebook(total=10)
    t.close()
    # no total
    t = tqdm_notebook()
    t.close()

# Generated at 2022-06-14 13:59:07.059213
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test for method reset of tqdm_notebook class.
    """
    tq = tqdm_notebook(total=100)
    tq.reset(total=10)

    # note: tqdm is an iterable so we need to iterate over it
    for _ in tq:
        pass


test_tqdm_notebook_reset()

# Generated at 2022-06-14 13:59:24.473661
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        import ipywidgets
    except ImportError:  # IPython 3.x / 2.x
        return

    # Code of method '__iter__' of class tqdm_notebook
    def __iter__(self):
        try:
            for obj in super(tqdm_notebook, self).__iter__():
                # return super(tqdm...) will not catch exception
                yield obj
        # NB: except ... [ as ...] breaks IPython async KeyboardInterrupt
        except:  # NOQA
            self.disp(bar_style='danger')
            raise
        # NB: don't `finally: close()`
        # since this could be a shared bar which the user will `reset()`

    # Class `tqdm_notebook` definition

# Generated at 2022-06-14 13:59:34.932187
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    n = 11

    try:
        from IPython.html.widgets import Label
        from IPython.html.widgets import VBox
    except ImportError:
        from IPython.html.widgets import ContainerWidget as Label
        from IPython.html.widgets import ContainerWidget as VBox

    fp = tqdm_notebook.status_printer(None, n)
    assert isinstance(fp, VBox)

    ltext = fp.children[0]
    assert isinstance(ltext, Label)
    assert ltext.value == ''

    pbar = fp.children[1]
    assert isinstance(pbar, IProgress)
    assert pbar.max == n
    assert pbar.layout.width is None

    rtext = fp.children[2]

# Generated at 2022-06-14 13:59:38.697399
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(total=1) as pbar:
        try:
            pbar.update()
            return False
        except:  # NOQA
            pass
    return True

# Generated at 2022-06-14 13:59:43.999761
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep
    tqdm_notebook.clear()
    t = tqdm_notebook()
    t.write('First')
    sleep(0.5)
    t.write('Second')
    sleep(0.5)
    t.write('Third')

# Generated at 2022-06-14 13:59:49.816606
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    for i in trange(2, leave=True, desc="1st loop"):
        for j in trange(3, desc="2nd loop", leave=True):
            sleep(0.01)
        trange(3).reset(3)
        sleep(0.01)

    tqdm_notebook(range(10000)).reset(10000)


if __name__ == '__main__':
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 13:59:57.824133
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    with tqdm_notebook(total=None, desc="test_tqdm_notebook_display") as t:
        t.display(pos=0, total=10, bar_style="info")
        t.display(pos=0, total=10000, bar_style="info")
        t.display(pos=10, total=10)
        t.display(pos=10, total=10000)
        t.display(pos=10)

# Generated at 2022-06-14 14:00:00.531765
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # Test with parameter: n=None
    t = tqdm_notebook(total=10)
    for i in range(100):
        t.update(n=None)
    # Test with parameter: n=2
    t = tqdm_notebook(total=10)
    for i in range(100):
        t.update(n=2)

# Generated at 2022-06-14 14:00:09.370175
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # Get bar instance
    bar = tqdm_notebook(total=2)
    assert bar == bar.__iter__()
    # Test first iteration
    next(bar)
    if bar.total:
        assert bar.n == 1
    assert bar.last_print_n == 1
    # Test second iteration
    next(bar)
    if bar.total:
        assert bar.n == 2
    assert bar.last_print_n == 2
    # Check closing on 'close'
    bar.close()
    if bar.total:
        assert bar.n == bar.total
    assert bar.last_print_n == bar.total
    # Check closing on 'success'
    bar = tqdm_notebook(total=2)
    next(bar)
    next(bar)
    assert bar.container.children

# Generated at 2022-06-14 14:00:18.492475
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .main import _tqdm
    from .gui import _version

    if not _version:
        return
    try:
        fp = io.StringIO()
        with _tqdm(total=1, unit="it", file=fp) as t:
            test_arr = [i for i in tqdm_notebook(t)]
        # fp.seek(0)
        print(fp.getvalue())
        assert fp.getvalue() != ''
        assert test_arr == list(t)
        assert test_arr == [0]
    except Exception as e:  # pragma: no cover
        # IPython 7.x doesn't work very well on TravisCI, so just skip the test.
        print(str(e))
        pass



# Generated at 2022-06-14 14:00:21.400605
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    b = tqdm_notebook(total=1)
    b.start()

    try:
        for i in b:
            pass
    except Exception:  # FIXME: no exception type(s) specified
        assert False
    finally:
        b.close()

# Generated at 2022-06-14 14:00:38.305203
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    try:
        import ipykernel
        ipykernel.get_ipython
    except:
        return

    print("test `clear`() method")
    from tqdm import tnrange
    from time import sleep
    import sys
    for i in tnrange(5, desc='test clear()'):
        sleep(.5)
        sys.stdout.write("\rSleeping: {}".format(i))
        sys.stdout.flush()

if __name__ == "__main__":  # pragma: no cover
    test_tqdm_notebook_clear()

# Generated at 2022-06-14 14:00:50.730848
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from .gui import tqdm_gui
    from .std import TqdmExperimentalWarning

    with warnings.catch_warnings(record=True):
        pbar = tqdm_notebook(["a", "b", "c"], desc="test")
        assert not pbar.disable
        assert not pbar.position
        pbar.clear()
        pbar.update(1)
        pbar.close()

        pbar = tqdm_notebook(["a", "b", "c"], desc="test", disable=True)
        assert pbar.disable
        pbar.clear()
        pbar.update(1)
        pbar.close()

        pbar = tqdm_notebook(["a", "b", "c"], desc="test", unit='B', unit_scale=True)

# Generated at 2022-06-14 14:00:55.747607
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep

    def check_interruption(tq):
        """Asserts that Ctrl+C/`InterruptKernel` interrupts the tqdm loop."""
        try:
            for _ in tq:
                sleep(.01)
        except KeyboardInterrupt:
            pass
        # not sure whether this is the guaranteed behaviour
        # actually, if KeyboardInterrupt is interrupted by signal
        # then tqdm may have closed and displayed its bar
        # but at least the loop was interrupted:
        assert tq.n < tq.total

    # check interruption
    for leave in [True, False]:
        tq = tqdm_notebook(total=1, leave=leave)
        check_interruption(tq)

    # check new total

# Generated at 2022-06-14 14:00:58.808825
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import time
    for i in trange(15, desc='test', leave=True, unit='it'):
        if i == 5:
            tqdm.clear()
        time.sleep(.01)
    print('Done!')

# Generated at 2022-06-14 14:01:03.252610
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from os import getpid
    from time import sleep
    from .auto import tqdm as auto_tqdm

    # Open a new IPython Notebook
    with tqdm_notebook(total=100) as t:
        for i in auto_tqdm(range(100), leave=False):
            t.set_description("PID: %i" % getpid())
            # Sleep for 0.01 s to make sure the update is visible
            sleep(0.01)

# Generated at 2022-06-14 14:01:15.212677
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    t = tqdm_notebook(total=10, ncols=100,
                      bar_format="{desc}: {total}", desc="name")
    assert t._repr_pretty_(None) == \
        "name: 10 |███████████████████████████████████████████████████| 10/10   "
    t.display(msg="step 1")
    assert t._repr_pretty_(None) == \
        "name: 10 |███████████████████████████████████████████████████| 10/10   step 1"
    t.display(msg="step 2")
    assert t._repr_pretty_(None) == \
        "name: 10 |███████████████████████████████████████████████████| 10/10   step 2"
    t.display(msg="", close=True)
    assert t.container.visible is False

# Generated at 2022-06-14 14:01:20.097992
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .gui import tqdm
    from .tqdm import TqdmTypeError
    # Test for https://github.com/tqdm/tqdm/issues/514
    assert not isinstance(tqdm, TqdmTypeError)
    with tqdm(total=10) as t:
        assert isinstance(t, tqdm_notebook)
        for _ in t:
            break
    t.close()



# Generated at 2022-06-14 14:01:25.222442
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import os
    try:
        os.remove('test_tqdm_notebook_status_printer.out')
    except OSError:
        pass
    fp = open('test_tqdm_notebook_status_printer.out', 'w')
    fp.write('aaa\n')
    fp.flush()
    tqdm_notebook.status_printer(fp, desc='bbb')
    assert open('test_tqdm_notebook_status_printer.out', 'r').read() == "aaa\nbbb\n"
    os.remove('test_tqdm_notebook_status_printer.out')

# Generated at 2022-06-14 14:01:32.699754
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    import time
    for total in [1, 2]:
        for leave in [True, False]:
            for bar_style in ['info', 'success', 'warning', 'danger']:
                out = tqdm_notebook(total=total, leave=leave)
                if total == 2:
                    out.update(1)
                time.sleep(.1)
                out.close(bar_style=bar_style)
                assert out.container.children[-2].bar_style == bar_style

# Generated at 2022-06-14 14:01:42.912561
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    """
    Test for method clear() of class tqdm_notebook
    """
    from .utils import FreezableIterable
    from .std import tqdm
    from .std import sys

    tmp = tqdm(["a", "b", "c", "d", "e", "f"], disable=True)
    for i in tmp:
        pass

    with tmp.external_write_mode(disable=False):
        tmp.clear()
        tmp.set_description("clear works")
        tmp.refresh()
        tmp.reset(total=10)
        for i in FreezableIterable(range(5)):
            tmp.update()
        tmp.reset()
        tmp.clear()
        tmp.set_description("clear works")
        tmp.refresh()
        tmp.reset(total=10)


# Generated at 2022-06-14 14:02:12.871366
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm_notebook(total=10) as t:
        for i in range(10):
            t.update(1)



# Generated at 2022-06-14 14:02:21.863289
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from random import randint
    from time import sleep
    from pytest import raises

    with raises(TypeError):
        tqdm_notebook(update=3)

    with tqdm_notebook(total=100, leave=False) as t:
        assert t.n == 0
        t.update(55)
        assert t.n == 55
        t.update(23)
        assert t.n == 78
        t.update()
        assert t.n == 79
        t.update()
        assert t.n == 80
        t.update(-10)
        assert t.n == 70
        t.update(-10)
        assert t.n == 60
        t.update(-100)
        assert t.n == 0
        t.update(100)
        assert t.n == 100

# Generated at 2022-06-14 14:02:30.292946
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from .gui import tqdm as tqdm_gui
    
    for leave in [True, False]:
        with tqdm_notebook(leave=leave) as t:
            repr(t)  # smoke test
            t.set_postfix(refresh=False, foo=1)
            t.set_postfix(refresh=False, foo=2)
            t.set_postfix(test="test", refresh=False)
        assert not t.disable
        t.disable = True
        with tqdm(leave=leave) as t:
            t.set_postfix(refresh=False, foo=2)
        assert not t.disable
        with tqdm_notebook(leave=leave) as t:
            t.set_postfix(refresh=False, foo=2)
        assert not t

# Generated at 2022-06-14 14:02:40.559018
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import gc
    for _ in [0, 1]:
        # Create a progress bar without iteration
        pbar = tqdm_notebook(total=None, desc='Iterating...', leave=False)
        # Update a few times
        for i in range(5):
            pbar.update(i)
        # Close the progress bar (no effect)
        pbar.close()
        # Manually delete the progress bar (just in case)
        del pbar
        # Iterate via a context manager
        with tqdm_notebook(total=10, desc='Iterating...', leave=False) as pbar:
            for i in range(5):
                pbar.update(i)
        # Collect garbage and re-iterate
        gc.collect()
    return



# Generated at 2022-06-14 14:02:48.453724
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():  # pragma: no cover
    # test when delta s is lower than delay
    # (https://github.com/tqdm/tqdm/issues/508)
    stderr = sys.stderr
    sys.stderr = None
    with tqdm_notebook(total=10, desc="test") as pbar:
        pbar.update_shown = False  # simulate a manual `disable=True`
        for i in range(10):
            pbar.update()
    # Restore
    sys.stderr = stderr


if __name__ == '__main__':  # pragma: no cover
    test_tqdm_notebook_update()

# Generated at 2022-06-14 14:02:59.013667
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    # Tests the method __iter__ of class tqdm_notebook.
    # The method __iter__ returns the object itself and calls
    # the method __iter__ of the superclass `tqdm.tqdm`.
    # The purpose of this unit test is to check that the
    # method __iter__ of the superclass `tqdm.tqdm` is automatically
    # called and that the method __iter__ of class tqdm_notebook
    # does not return a new object.

    def method_is_called(name_method, object_type):
        """
        Raises an AssertionError if the it is not the method `name_method`
        of the class `object_type` that is being called.
        """


# Generated at 2022-06-14 14:03:07.574614
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from IPython.display import HTML, display
    # Test without total
    with std_tqdm._suppress_stderr_debugging():  # _suppress_stderr_debugging() is used for testing only
        d = tqdm_notebook.status_printer(None, None, "desc")
        assert isinstance(d, HBox)
        assert isinstance(d.children[1], IProgress)
        display(d)
        # Test with total > 1

# Generated at 2022-06-14 14:03:18.400547
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    import time
    try:
        from IPython.display import clear_output
    except ImportError:
        return

    # Unit test of tqdm_notebook constructor
    with tqdm_notebook(total=1, desc="Loading ...", unit="B",
                       unit_scale=True, dynamic_ncols=True) as t:
        time.sleep(0.1)
        assert t.total == 1
        assert t.ncols == "100%"
        assert t.desc == "Loading ..."
        assert t.unit == "B"
        assert t.unit_scale == True
        assert t.unit_divisor == 1
        assert t.n == 1
        assert t.dynamic_ncols == True
        assert t.ascii == True
        assert t.disable == 0
        assert t.min

# Generated at 2022-06-14 14:03:29.289481
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    try:
        # Hack to avoid creating a tqdm_notebook with gui=True in __init__
        # since this raises an ImportError if IPython widgets are not available
        tqdm_notebook.status_printer = lambda *_, **__: None
        tn = tqdm_notebook(1, gui=True, file=None)
        tn._instances = []
    except:
        print("Tests skipped: no IPython widgets found.")
        return

    def test_set(bar_style, colour):
        tn = tqdm_notebook(1, gui=True, file=None)
        tn.colour = colour
        tn.display(bar_style=bar_style)
        tn.close()

# Generated at 2022-06-14 14:03:40.285296
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from tqdm._utils import _term_move_up
    from tqdm.auto import trange
    for ncols in ['100%', 100]:
        t = tqdm_notebook(total=100, ncols=ncols)
        for _ in trange(10):
            t.update()
            _term_move_up()  # simulate jupyter notebook output
        t.update(90)
        t.close()


if __name__ == "__main__":
    r = tqdm_notebook(total=10)
    for i in range(9):
        r.update()
        r.reset()
    r.close()

    space = " "
    r = tqdm_notebook(total=10)
    for i in range(9):
        r.update()

# Generated at 2022-06-14 14:04:43.773740
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    for _ in trange(1):
        pass


# Generated at 2022-06-14 14:04:47.702743
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    '''Test case of tqdm_notebook.__iter__()

    This is a test method for tqdm_notebook.__iter__()
    '''
    for _ in tqdm_notebook(range(10)):
        pass



# Generated at 2022-06-14 14:04:57.195816
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from sys import stderr
    tot = 53
    pbar = tqdm_notebook.status_printer(stderr, total=tot)
    assert pbar.value == 0
    assert pbar.max == tot
    pbar.value = tot
    assert pbar.value == tot
    assert pbar.layout.visibility == 'visible'
    pbar.visible = False
    assert pbar.layout.visibility == 'hidden'

    # Test default 'ndivisible' progress bar
    pbar = tqdm_notebook.status_printer(stderr)
    assert pbar.layout.width == '20px'
    assert pbar.description == ''
    assert pbar.max == 1
    assert pbar.bar_style == 'info'
    assert pbar.value == 1

    #

# Generated at 2022-06-14 14:05:06.528518
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from .gui import tnrange
    from random import sample
    from copy import copy

    bar = tnrange(10)
    bar2 = copy(bar)
    bar3 = copy(bar)
    bar4 = copy(bar)
    bar5 = copy(bar)
    l = sample(range(10), 10)

    for i in bar:
        # no button
        bar2.n = l[i]
        bar2.refresh()  # refresh manually

        # no button
        bar3.n = l[i]
        bar3.refresh(nolock=True)  # refresh manually (nolock)

        # with button
        bar4.update(l[i] - bar4.n)  # n: new value

        # with button
        bar5.update(0)  # n=0

# Generated at 2022-06-14 14:05:13.421584
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    from IPython.core.getipython import get_ipython
    ip = get_ipython()
    if not ip:
        raise Exception("test_tqdm_notebook_close can only be called from inside an IPython notebook")
    if IPY < 2:
        raise Exception("test_tqdm_notebook_close: IProgress doesn't exist")
    # Test case 1, closing with total != n
    tqdm_notebook(total=3)
    # Test case 2, closing with total == n
    tqdm_notebook(total=1)

# Generated at 2022-06-14 14:05:22.317846
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    with tqdm_notebook(total=2) as pbar:
        assert pbar.total == 2, "total = 2 was expected, but got %s" % pbar.total
        pbar.reset()
        assert pbar.total == None, "total = 2 was expected, but got %s" % pbar.total
        assert pbar.n == 0, "n = 0 was expected, but got %s" % pbar.n
        pbar.reset(total=3)
        pbar.update(1)
        pbar.reset()
        assert pbar.total == None, "total = 2 was expected, but got %s" % pbar.total
        assert pbar.n == 0, "n = 0 was expected, but got %s" % pbar.n

# Generated at 2022-06-14 14:05:29.403042
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    # case total = None
    with tqdm_notebook(total=5, leave=True) as pbar:
        assert pbar.total == 5
        for _ in range(3):
            pbar.update()
        pbar.reset(size=2)
        assert pbar.total == 2
        pbar.update()
        assert pbar.total == 2
        assert pbar.n == 1
        pbar.update()
        assert pbar.total == 2
        assert pbar.n == 2
        pbar.reset()
        assert pbar.total == 2
        pbar.update()
        assert pbar.total == 2
        assert pbar.n == 1
        pbar.reset(size=None)
        assert pbar.total is None
        pbar.update()

# Generated at 2022-06-14 14:05:40.515729
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time
    import numpy as np

    min_interval = 1  # the minimum time it takes to print a new bar
    n = [1, 100, 300]
    bar_style = ["success", "success", "success"]
    leave = [False, True, False]

# Generated at 2022-06-14 14:05:46.253531
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from time import sleep
    with tqdm_notebook(total=10) as pbar:  # noqa
        for i in range(5):
            sleep(0.2)
            pbar.update(1)
        pbar.reset(total=5)
        for i in range(5):
            sleep(0.2)
            pbar.update(1)
        pbar.reset()
        for i in tqdm_notebook(range(5)):  # noqa
            sleep(0.2)
            pbar.update(1)


if __name__ == '__main__':  # pragma: no cover
    # Unit test
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:05:50.743758
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from tqdm._tqdm_notebook import _tqdm_notebook
    b = _tqdm_notebook(total=3)
    for i in range(4):
        b.update()
    assert not b.disable
    b.close()

# Generated at 2022-06-14 14:07:12.872400
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    t0 = trange(10)
    for i in tqdm_notebook(_range(10)):
        # assert tqdm_notebook.update() is None
        assert t0.update() is None

# Generated at 2022-06-14 14:07:15.344832
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        from tqdm.auto import trange
        assert iter(tqdm_notebook(range(3))) == iter(trange(3))
    except ImportError:
        pass



# Generated at 2022-06-14 14:07:23.509710
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from IPython.display import clear_output
    try:
        from tqdm.gui import tnrange, tqdm_notebook
        from tqdm import trange, tqdm
        from tqdm._tqdm_gui import tgrange, tqdm_gui, tqdm_notebook
        assert tqdm == tqdm_notebook
        assert trange == tnrange
    except ImportError:
        pass

# Generated at 2022-06-14 14:07:26.902978
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time

    with tqdm_notebook(total=100, leave=True) as pbar:
        for i in range(100):
            time.sleep(0.01)
            pbar.update()

    pbar.reset(total=100)

    with tqdm_notebook(total=100) as pbar:
        for i in range(100):
            time.sleep(0.01)
            pbar.update()


test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:07:36.236754
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep
    t = tqdm_notebook(total=2)
    assert t.total == 2
    for i in t:
        sleep(.1)
        t.display()
        assert t.n == i + 1
    assert t.total == 2
    t.close()

    t = tqdm_notebook(total=2)
    assert t.total == 2
    for i in t:
        sleep(.1)
        t.display()
        assert t.n == i + 1
    assert t.total == 2
    t.display(close=True)
    assert t.container.visible is False

    t = tqdm_notebook(total=2)
    assert t.total == 2
    for i in t:
        sleep(.1)
        t.display()

# Generated at 2022-06-14 14:07:44.636992
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    # Initialize bar
    with tqdm(total=10) as bar:
        for _ in bar:
            pass
        assert bar.total == 10
        assert bar.n == 10
        bar.reset(total=20)
        assert bar.total == 20
        assert bar.n == 0

# Pytest is not able to detect the test if it is inside the class
# since pytest uses the inspect module and gets None as the function name
# These tests are written in order to avoid importing the class and pytest_plugins
# just to test the methods of the class `tqdm`, which is imported by `tqdm.notebook`.


# Generated at 2022-06-14 14:07:52.754297
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    if IPY == 0:
        raise ImportError("Ipython not found")
    from time import sleep
    from tqdm import trange
    from tqdm.auto import tqdm
    for t in trange(4), tqdm(range(4), disable=True), tqdm(range(4), unit='s'):
        sleep(0.01)
        t.update()
        sleep(0.01)
        t.update(0)
        sleep(0.01)
        t.update(1)
        sleep(0.01)
        t.update(2)
        sleep(0.01)


if __name__ == "__main__":
    test_tqdm_notebook_update()

# Generated at 2022-06-14 14:07:58.964767
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time
    from tqdm.auto import tqdm, trange

    with tqdm(total=10, ncols=90) as t:
        for i in trange(0, 10):
            time.sleep(0.1)
            t.reset(total=200)
            for j in trange(0, 200):
                time.sleep(0.01)
            t.reset(total=10)
            for j in trange(0, 10):
                time.sleep(0.1)
                t.reset()

# Generated at 2022-06-14 14:08:04.384150
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from .utils import _test_iter
    from .tests import TqdmTestCase, pretest
    pretest()
    _test_iter(tqdm_notebook)
    _test_iter(tnrange)
    return TqdmTestCase.check_results()

