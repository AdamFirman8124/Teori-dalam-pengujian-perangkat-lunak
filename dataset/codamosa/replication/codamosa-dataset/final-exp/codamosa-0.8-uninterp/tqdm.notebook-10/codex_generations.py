

# Generated at 2022-06-14 13:58:47.275093
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():  # pragma: no cover
    import time
    with tqdm_notebook(total=10, unit='frames', ncols=500) as pbar:
        for i in trange(10):
            time.sleep(0.1)
            pbar.set_description('Processing frame %i' % i)



# Generated at 2022-06-14 13:58:54.421665
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from random import randint

    class TestClass:
        pass

    n = randint(1, 10)
    tc = TestClass()
    with tqdm_notebook(total=n, unit='iter', dynamic_ncols=True, desc='Test') as t:
        for _ in t:
            tc.tqdm_notebook___iter__ = True
            tc.tqdm_notebook_update = None
            break

    assert tc.tqdm_notebook___iter__



# Generated at 2022-06-14 13:59:02.767536
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    """
    Unit test for `tqdm_notebook`.
    """
    tn = tqdm_notebook(range(4), postfix={"life": 42},
                       leave=False)
    for i in tn:
        tn.set_postfix_str("life=%d" % i)
    tn = tqdm_notebook(range(1, 4), postfix={"life": 42},
                       leave=False)
    for i in tn:
        tn.set_postfix_str("life=%d" % i)

# Generated at 2022-06-14 13:59:11.351505
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import os
    import psutil
    import time
    # First verify that the memory usage is the same with or without call to reset
    t = tqdm_notebook(total=500)
    mem_before = psutil.virtual_memory().used
    t.reset(total=500)
    t.reset(total=500)
    t.reset(total=500)
    t.reset(total=500)
    for i in t:
        time.sleep(0.01)
    assert os.path.isfile("tqdm_notebook_reset.py")
    t.close()
    mem_after = psutil.virtual_memory().used
    assert mem_after - mem_before < 1e5

    # Also verify that resetting the total to a different value works as expected

# Generated at 2022-06-14 13:59:17.388798
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from io import BytesIO
    from sys import stdout
    from contextlib import contextmanager
    from tempfile import NamedTemporaryFile

    @contextmanager
    def stdout_file():
        """Suppress stdout"""
        old_stdout = stdout
        tmp_stdout = BytesIO()
        try:
            stdout = tmp_stdout
            yield
        finally:
            stdout = old_stdout
            tmp_stdout.close()

    def stdout_as_str(stdout):
        """Returns stdout as a string"""
        return str(stdout.getvalue(), encoding='utf-8')


# Generated at 2022-06-14 13:59:19.698620
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    import pytest
    with pytest.raises(Exception):
        for _ in tqdm_notebook([1], ascii=True):
            break
        else:
            raise RuntimeError



# Generated at 2022-06-14 13:59:25.290430
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from .std import tqdm_gui
    # just a test for jupyter notebook reset issue #351
    with tqdm_gui(total=10) as gui_tqdm:
        for _ in gui_tqdm:
            gui_tqdm.reset(total=1)
            break
    # reset(total=None)
    with tqdm_gui(total=10) as gui_tqdm:
        for _ in gui_tqdm:
            gui_tqdm.reset()
            break
    # reset(total=None) followed by reset(total=None)
    with tqdm_gui(total=10) as gui_tqdm:
        gui_tqdm.reset()
        gui_tqdm.reset()


# Generated at 2022-06-14 13:59:28.546077
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    dummy_container = tqdm_notebook.status_printer(sys.stderr)
    dummy_container = tqdm_notebook.status_printer(sys.stderr, 10)



# Generated at 2022-06-14 13:59:37.394000
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import os
    import time
    # Note: this test should ALWAYS be run in a Jupyter Notebook
    # Create the tqdm instance
    with tqdm_notebook(total=10, desc="TEST") as t:
        assert t.total == 10
        # Sleep a little
        time.sleep(0.1)
        # Reset the instance
        t.reset(total=1)
        # Write to stdout to move the cursor
        sys.stdout.write('\r')
        # Sleep a little
        time.sleep(0.1)
        # Assert that the reset was correctly done
        assert t.total == 1
        # Cleanup
        sys.stdout.write(os.linesep)


if __name__ == "__main__":
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 13:59:44.526992
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # Test 'n < total' case
    pbar = tqdm_notebook(total=100)
    pbar.update(50)
    assert pbar.n == 50
    assert pbar.n < pbar.total

    # Test 'n >= total' case
    pbar.update(50)
    assert pbar.n == 100
    assert pbar.n >= pbar.total

# Generated at 2022-06-14 14:00:04.459193
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Check that `tqdm_notebook().status_printer` works"""
    # Test when total is None
    w = tqdm_notebook.status_printer(None)
    assert isinstance(w, TqdmHBox)

    # Test when total is not None
    w = tqdm_notebook.status_printer(None, total=10)
    assert isinstance(w, TqdmHBox)
    assert w.children[-2].max == 10

    # Test when desc is not None
    w = tqdm_notebook.status_printer(None, total=10, desc='desc')
    assert isinstance(w, TqdmHBox)
    assert w.children[0].value == 'desc'



# Generated at 2022-06-14 14:00:15.151918
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    try:
        tqdm_notebook
    except NameError:
        pass
    else:
        from io import StringIO
        stream = StringIO()
        # Test normal display
        from tqdm import tqdm_notebook
        with tqdm_notebook(total=4, file=stream) as pbar:
            pbar.display()
            pbar.display()
            pbar.display()
        # Test colouring
        from tqdm import tqdm_notebook
        with tqdm_notebook(total=4, file=stream) as pbar:
            pbar.display()
            pbar.colour = 'red'
            pbar.display()
            pbar.display()
        # Test clearing bar
        from tqdm import tqdm_notebook

# Generated at 2022-06-14 14:00:22.921014
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time

    # The delay is used to let the progress bar appear before
    # the first update can occur.
    with tqdm_notebook(total=100, position=0, leave=True,
                       miniters=1, mininterval=0.1,
                       desc="test 0", delay=0.5,
                       unit_scale=True) as pbar:
        for i in range(10):
            time.sleep(0.01)
            pbar.update(10)
            pbar.set_description("test %s" % i)
        pbar.reset(total=50)
        for i in range(5):
            time.sleep(0.01)
            pbar.update(10)
        pbar.reset(total=100)

# Generated at 2022-06-14 14:00:30.314145
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Test __iter__ of the tqdm_notebook.

    Note
    ----
    This function is copied from the function `test_tqdm___iter__` of the file
    `test_tqdm.py`.
    """
    for __init in [tqdm_notebook, trange, tqdm]:
        with __init(total=2) as t:
            for i in t:  # toolbox.Iterator() behaves like a generator
                assert i == next(t)
                t.update()

test_tqdm_notebook___iter__()  # run the test

# Generated at 2022-06-14 14:00:34.973700
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    from time import sleep
    pbar = tqdm_notebook(total=5)
    for _ in pbar:
        sleep(0.1)
        pbar.display()
        pbar.update()
    pbar.close()

if __name__ == "__main__":  # pragma: no cover
    test_tqdm_notebook_display()

# Generated at 2022-06-14 14:00:38.766732
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    # getclass function
    class_ = type('tqdm_notebook_class', (tqdm_notebook,), {})
    instance = class_(total=None, ncols=None)
    new_instance = instance.reset(total=2)
    assert isinstance(new_instance, class_)
    assert new_instance.container.children[1].max == 2

# Generated at 2022-06-14 14:00:51.252416
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """
    NOTES:
        Using `tqdm_notebook.status_printer(ncols=None, desc='foo')`
        to test `tqdm_notebook.status_printer` method is deprecated.
        Use `tqdm_notebook(desc='foo')` instead.

        Using `tqdm_notebook.status_printer(ncols=100)`
        to test `tqdm_notebook.status_printer` method will test it for
        only one value of `ncols`, which is error-prone.
        Use `tqdm_notebook(ncols=100)` instead.
    """
    tqdm_notebook(ncols=None, desc="foo")
    tqdm_notebook(ncols=100, desc="foo")
    t

# Generated at 2022-06-14 14:00:59.862616
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    pbar = tqdm_notebook(total=5, disable=True)
    pbar.close()
    pbar.disable = False
    pbar.reset()
    pbar.update()
    pbar.update(2)
    pbar.update(2)
    pbar.update(2)
    pbar.update(2)
    pbar.update(2)
    pbar.update(2)
    pbar.update(2)
    pbar.close()
    pbar.update()
    pbar.close()
    pbar.update()
    pbar.close()
    pbar.update(1)
    pbar.update(1)
    pbar.update(1)
    pbar.update()
    pbar.update()
    pbar.update()

# Generated at 2022-06-14 14:01:02.058468
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    try:
        for i in tnrange(5, desc='1st loop'):
            for j in tnrange(5, desc='2nd loop'):
                pass
    except KeyboardInterrupt:
        pass
    for i in tnrange(1, desc='3rd loop'):
        for i in tnrange(1, desc='4th loop'):
            pass

# Generated at 2022-06-14 14:01:03.852364
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm_notebook(total=1) as pbar:
        pbar.update(1)

# Generated at 2022-06-14 14:01:38.449116
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from io import StringIO

    # Setup default output
    file_kwarg = sys.stderr
    if file_kwarg is sys.stderr or file_kwarg is None:
        sys.stderr = StringIO()

    # Initialize tqdm_notebook
    bar_kwargs = {
        'disable': False,
        'ncols': 100,
        'gui': True,
        'file': sys.stderr
    }
    tqdm_nb_test = tqdm_notebook(**bar_kwargs)
    tqdm_nb_test.container.pbar = proxy(tqdm_nb_test)
    tqdm_nb_test.displayed = False
    tqdm_nb_test.disp = tqdm_nb_test.display

    # Test

# Generated at 2022-06-14 14:01:42.738646
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Test method __iter__ of class tqdm_notebook.
    """
    l = [1, 2, 3, 4, 5]
    for i in tqdm_notebook(l):
        assert i in l


if __name__ == '__main__':
    test_tqdm_notebook___iter__()
    sys.exit(0)

# Generated at 2022-06-14 14:01:53.683986
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep
    from tqdm.utils import _term_move_up

    # Basic test
    assert tqdm_notebook.display(bar_style='success') is None

    with tqdm_notebook(ascii=True) as pbar:
        for _ in pbar:
            pbar.set_description('Desc')
            pbar.update()
            sleep(.2)
            pbar.display(pos=pbar.pos + 1, bar_style='warning')
            sleep(.2)
            pbar.display(pos=pbar.pos + 1, bar_style='danger')
            sleep(.2)
    print('\n')

    # Test message
    with tqdm_notebook(ascii=True) as pbar:
        for _ in pbar:
            p

# Generated at 2022-06-14 14:02:06.723912
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Unit test function for the reset method of class tqdm_notebook
    """
    class RandomIterator:
        """
        Random iterator to use for testing
        """
        def __iter__(self):
            return self

        def __next__(self):
            return random.random()

    random.seed(0)  # Reset random generator
    iterable = RandomIterator()
    progress_bar_1 = tqdm_notebook(iterable, total=10)
    for _ in progress_bar_1:
        if random.randint(0, 4) == 0:
            progress_bar_1.reset()
    progress_bar_2 = tqdm_notebook(iterable, total=10)
    for element in progress_bar_2:
        if element > 0.5:
            progress_bar_2

# Generated at 2022-06-14 14:02:15.229506
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    assert repr(TqdmHBox()) == "<TqdmHBox>\n"
    # {"__fidl__": 1, "unit": "it", "unit_scale": True, "n": 0, "total": None,
    # "bar_format": "{l_bar}{bar}{r_bar}", "desc": null, "ncols": null,
    # "ascii": false, "leave": false}
    TqdmHBox().pbar = tqdm_notebook(unit='it', total=None)

# Generated at 2022-06-14 14:02:24.440460
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from tqdm import tqdm

    t = tqdm(total=2, leave=False)
    assert t.display(close=True) is None
    t.close()


# Python 2/3 cross-compatibility
try:
    from inspect import signature

    def inspect_signature(func):
        return signature(func)
except ImportError:
    # Stolen from the stdlib
    # Added '.' and 'self' to the exceptions, as they never match anyway
    def _sig_re(name):
        return re.compile(r'\b' + re.escape(name) + r'\b')

    def _exclude_names(func):
        names = set()
        for name in dir(func):
            if not name.startswith('_'):
                names.add(name)


# Generated at 2022-06-14 14:02:29.129266
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # Initialization
    from .tests_tqdm import tqdm as _tqdm  # NOQA
    d = tqdm(total=5)

    # Tests
    d.container = tqdm_notebook.status_printer(d.file)
    assert d.container.children[1].max == 5

    d.container = tqdm_notebook.status_printer(d.file, None)
    assert d.container.children[1].max == 1

    d.container = tqdm_notebook.status_printer(d.file, None,
                                               'Test desc')
    assert d.container.children[0].value == 'Test desc'


# Generated at 2022-06-14 14:02:35.939802
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from contextlib import suppress
    try:
        with suppress(AttributeError):
            del tqdm.tnrange
    except BaseException:
        pass
    tqdm.tnrange = tqdm.tnrange if tqdm.tnrange else tnrange
    tmp = tqdm.tnrange(2)
    tmp.__next__()
    tmp.reset()
    assert tmp.total is None
    assert tmp.n == 0
    del tmp

if __name__ == '__main__':
    test_tqdm_notebook_reset()

# Generated at 2022-06-14 14:02:45.766417
# Unit test for method display of class tqdm_notebook

# Generated at 2022-06-14 14:02:50.420639
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    import random
    for bar_style in ['', 'info', 'success', 'danger']:
        with tqdm_notebook(leave=True, bar_style=bar_style) as t:
            for _ in t:
                t.display(bar_style=bar_style)
                t.display("|<bar/>|" + random.choice('abcdefghijklmnopqrstuvwxyz'))
                t.update()
