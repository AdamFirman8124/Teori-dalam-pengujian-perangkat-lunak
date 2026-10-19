

# Generated at 2022-06-14 13:58:31.308971
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    _, pbar, _ = tqdm_notebook(total=3).container.children
    assert pbar.bar_style == ''
    tqdm_notebook.write('')  # clear
    assert pbar.bar_style == ''

# Generated at 2022-06-14 13:58:35.623151
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    with tqdm_notebook(total=100, leave=False) as t:
        t.reset(total=10)
    assert t.n == 0
    assert t.total == 10
    assert t.container.children[1].max == 10


# Generated at 2022-06-14 13:58:45.264118
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    assert 'init' == next(tqdm_notebook(iter(['init', 'pass'])))

# Generated at 2022-06-14 13:58:55.628999
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from random import randint
    from shutil import rmtree
    from tempfile import mkdtemp
    from time import sleep
    from os import makedirs, listdir
    from os.path import join, isdir

    # suppress IProgress import error for testing
    global IProgress
    IProgress = type('Dummy', (object, ), dict())

    # Random tests
    for i in range(10):
        with std_tqdm(total=10, file=sys.stdout) as t:
            t.reset(total=1)
            t.reset(total=10)
            t.set_description('d')
            t.set_description('ddd')
            t.reset()
            t.set_postfix(dict(a=1, b=1))

# Generated at 2022-06-14 13:59:06.997369
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    pbar = tqdm_notebook(total=1000)
    container = pbar.container
    pbar.refresh()
    assert repr(container) == pbar.format_meter(**pbar.format_dict)
    assert container._repr_pretty_ == TqdmHBox._repr_pretty_  # #890
    assert container._repr_json_().get('l_bar')

# Test for issue #555
# @pbar.tqdm(ncols=100)
# def test_ncols():
#    for i in range(10):
#        pass
# test_ncols()

# Test for issue #872
# def test_error():
#    try:
#        with tqdm(total=1000) as pbar:
#            for _ in range(5

# Generated at 2022-06-14 13:59:13.080334
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():  # pragma: no cover
    import time
    from IPython.display import clear_output
    try:
        for i in tqdm(range(10)):
            time.sleep(0.1)
            clear_output(wait=1)
    except KeyboardInterrupt:
        pass
    try:
        bar = tqdm_notebook(range(10))
        for i in bar:
            time.sleep(0.1)
            clear_output(wait=1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":  # pragma: no cover
    test_tqdm_notebook_update()

# Generated at 2022-06-14 13:59:21.114625
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    import time
    try:
        from IPython.display import clear_output
    except ImportError:
        return

    with tqdm_notebook(total=10, gui=True) as t:
        for i in range(10):
            t.update()
            time.sleep(.05)

        t.display()  # display()
        clear_output(wait=True)
        time.sleep(.05)
        t.display()  # display(close=True)
        clear_output(wait=True)
        time.sleep(.05)
        t.display(close=True)
        assert t.n == 10

        t.reset()
        assert t.n == 0
        t.display()  # display()
        clear_output(wait=True)
        time.sleep(.05)

# Generated at 2022-06-14 13:59:28.657935
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    progress = IProgress(min=0, max=1)
    progress.value = 1
    progress.bar_style = 'info'
    ltext = HTML()
    rtext = HTML()
    container = TqdmHBox(children=[ltext, progress, rtext])

    if IProgress is not None:
        assert container.__repr__() == \
            '|██████████████████████████████████████████████████| 100% 16.4/s  \n'
    else:
        assert container.__repr__() == ''

# Generated at 2022-06-14 13:59:32.206138
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    # tqdm_notebook.status_printer(None)  # test fallback
    tqdm_notebook.status_printer(None, total=100)  # test IPython widget
    # TODO: test IPython widget with total=None

# Generated at 2022-06-14 13:59:39.330562
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """Unit test for method reset of class tqdm_notebook."""
    with tqdm_notebook(total=1) as tb:
        assert getattr(tb, 'container', None) is not None
    with tqdm_notebook(total=1) as tb:
        tb.reset(total=2)
        assert getattr(tb, 'container', None) is None
    with tqdm_notebook(total=None) as tb:
        tb.reset(total=None)
        assert getattr(tb, 'container', None) is None
    with tqdm_notebook(total=None) as tb:
        tb.reset(total=1)
        assert getattr(tb, 'container', None) is None

# Generated at 2022-06-14 13:59:53.660354
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    a = tqdm_notebook(range(10), desc="test", leave=False, ncols=100)
    for i in a:
        if i == 5:
            a.clear()
        time.sleep(1)
    a.close()
    return

# Generated at 2022-06-14 13:59:56.884025
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    from pytest import raises

    with raises(NotImplementedError):
        with tqdm_notebook(total=1) as pbar:
            pbar.clear()

# Generated at 2022-06-14 14:00:02.353281
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm_notebook(total=1) as t:
        for i in t:
            assert i == 0
            break
        assert t.disable == True  # was disabled by the for loop
    # make sure we weren't modifying tqdm's default _instances list
    assert len(std_tqdm._instances) == 0


# Generated at 2022-06-14 14:00:10.424053
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    try:
        from collections import Iterable
    except ImportError:  # Python < 2.7
        from collections import Sized  # NOQA
        from collections import Callable  # NOQA
        from collections import Container  # NOQA
        from collections import Hashable
        Iterable = Sized
    for n in trange(1, 3):
        assert isinstance(n, int)
        assert isinstance(n, Iterable)
    for n in trange(16):
        print(n)
        assert isinstance(n, int)
        assert isinstance(n, Iterable)
    try:
        for n in trange(16):
            print(n)
            raise ValueError()
    except ValueError:
        pass

# Generated at 2022-06-14 14:00:16.191340
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import sys
    assert tqdm_notebook().update() is None
    # test for close method before reset
    t = tqdm_notebook()
    if sys.version_info[0] == 2:
        t.update(1)
    else:
        t.update(2)
    t.close()
    # test for reset method
    t.reset()
    assert t.n == 0



# Generated at 2022-06-14 14:00:23.593427
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    res = {}
    def _aux(*args, **kwargs):
        res['out'] = tqdm_notebook(total=3, unit='step')
        try:
            yield
        except:
            res['out'].disp(bar_style='danger')
            raise
    with _aux():
        pass
    assert res['out'].n == 0
    res['out'].update()
    assert res['out'].n == 1
    res['out'].update()
    assert res['out'].n == 2
    res['out'].update()
    assert res['out'].n == 3
    res['out'].update()
    assert res['out'].n == 3

# Generated at 2022-06-14 14:00:27.940260
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    max_iter = 100
    iter_list = [i for i in range(0, max_iter)]

    # test method close
    tqdm.close()
    assert not tqdm.disable

    # test method disp
    tqdm.disp(bar_style='danger')
    assert not tqdm.disable

    # test method colour
    tqdm.colour = '#FF0000'
    assert not tqdm.disable

    # test with
    with tqdm(iter_list) as t:
        for i in iter_list:
            t.update(1)
    assert not tqdm.disable

    # test update
    tqdm.update(1)
    assert not tqdm.disable

    # test iter

# Generated at 2022-06-14 14:00:36.505152
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    class MyTqdm(tqdm_notebook):
        def display(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            return super(MyTqdm, self).display(*args, **kwargs)

    with MyTqdm(total=1) as pbar:
        pbar.display()
        assert pbar.args == (None, None, False)
        assert pbar.kwargs == {}

        pbar.display('', pos=1)
        assert pbar.args == ('', 1, False)
        assert pbar.kwargs == {}

        pbar.display(close=True)
        assert pbar.args == (None, None, True)
        assert pbar.kwargs == {}

        pbar.display(bar_style='info')


# Generated at 2022-06-14 14:00:40.750512
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from IPython.display import clear_output  # NOQA
    for i in trange(3, desc='1st loop', leave=False):
        for j in trange(3, desc='2nd loop', leave=False):
            pass
        clear_output(wait=True)
    assert '2nd loop' not in tqdm_notebook.format_dict['desc']
    assert tqdm_notebook.format_dict['desc'] == '1st loop'

# Generated at 2022-06-14 14:00:52.421003
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """
    Test method reset of class tqdm_notebook

    """
    from time import sleep
    from numpy.random import randint

    for foo in [
            {'total': None},
            {'total': 100, 'leave': True},
            {'total': 100, 'leave': False},
            {'total': 100, 'leave': True, 'dynamic_ncols': True},
            {'total': 100, 'leave': False, 'dynamic_ncols': True},
    ]:
        foo['total'] = randint(1, 6) * 10
        with tqdm_notebook(**foo) as t:
            for i in range(t.total):
                sleep(0.01)
                t.update(1)
            t.reset()



# Generated at 2022-06-14 14:01:11.192197
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():  # pragma: no cover
    for total in [None, 100]:
        for leave in [True, False]:
            t = tqdm_notebook(total=total, leave=leave)
            for _ in t:  # noqa
                pass
            t.reset(total=total)
            for _ in t:  # noqa
                pass
            t.reset()
            for _ in t:  # noqa
                pass
            t.close()
            display(t.container)  # display the bar in case of error

# Generated at 2022-06-14 14:01:14.898018
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Test for method display of the class tqdm_notebook
    """
    from .tests import tqdm_test_cases
    tqdm_test_cases(tqdm, tqdm_gui=False)

# Generated at 2022-06-14 14:01:22.877093
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep
    from numpy import arange

    def check_tqdm_notebook(t, max_t):
        for _ in t:
            sleep(0.01)

        assert t.n == max_t
        t.reset()
        assert t.n == 0

    for max_t in [int(1e5), arange(100).sum()]:
        t = tqdm_notebook(total=max_t, mininterval=0.01)
        check_tqdm_notebook(t, max_t)

        t = tqdm_notebook(total=max_t, mininterval=0.01, unit_scale=True)
        check_tqdm_notebook(t, max_t)


# Generated at 2022-06-14 14:01:33.724271
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    bar = tqdm_notebook(total=5)
    bar.update(1)
    assert bar.n == 1
    bar.reset(total=10)
    assert '10it [' in bar.container.__repr__()


if __name__ == "__main__":
    from unittest import TestCase, main
    from doctest import testmod

    class TestTqdmNotebook(TestCase):
        def setUp(self):
            self.results = []

        def test_reset(self):
            for _ in tnrange(4, desc='1st loop'):
                self.results.append(1)
            assert self.results == [1] * 4
            self.results = []
            for _ in trange(5, desc='2nd loop'):
                self.results.append(1)

# Generated at 2022-06-14 14:01:39.720744
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from .tests import test_tqdm_reset
    test_tqdm_reset(tqdm_notebook, trange,
                    _range=_range, _unich=str,
                    leave=False, dynamic_ncols=False)


# IPython/Jupyter Notebook specific test
# Tested with IPython 3.2.2, 4.1.2 and 5.0.0

# Generated at 2022-06-14 14:01:42.071863
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from time import sleep
    data = [1, 2, 3, 4]
    for i in tqdm_notebook(data):
        sleep(0.2)

# Generated at 2022-06-14 14:01:53.318523
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    if 'tqdm' not in globals():  # pragma: no cover
        raise ImportError('tqdm not found')

    import time

    # raise Exception("error")

    @tqdm_notebook(total=10)
    def test_1():
        for i in range(9):
            time.sleep(0.01)
            test_1.update()
        test_1.update(1)

    test_1()

    @tqdm_notebook(total=10)
    def test_2():
        for i in range(9):
            time.sleep(0.01)
            test_2.update()
        time.sleep(0.01)

    test_2()


# Generated at 2022-06-14 14:02:06.360016
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from IPython.html.widgets import FloatProgress as IProgress
    pbar = IProgress(min=0, max=100)
    left = HTML()
    right = HTML()
    container = TqdmHBox(children=[left, pbar, right])
    # init
    tqdm_notebook.display(tqdm_notebook(100), msg='<b>100</b>', close=True,
                          bar_style='danger')
    assert container.children[0].value == '<b>100</b>'
    assert container.children[2].value == ''
    assert container.children[1].bar_style == 'danger'
    assert container.children[1].value == 100
    # msg='' doesn't clear bar

# Generated at 2022-06-14 14:02:14.976417
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    """
    Unit test for the method __iter__ of the class tqdm_notebook.
    It is designed to catch a problem with the widget and the
    interrupt signal where the bar would crash at the end
    (ref: https://github.com/tqdm/tqdm/issues/445).
    """
    from tqdm.auto import tqdm

# Generated at 2022-06-14 14:02:17.012072
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    with tqdm_notebook(total=9) as pbar:
        for i in range(10):
            pbar.update(1)

# Generated at 2022-06-14 14:02:36.064255
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    '''Test method reset of class tqdm_notebook'''
    n = 10
    with tqdm_notebook(total=n) as t:
        assert len(t) == n

        t.reset(total=n+1)
        assert len(t) == n+1

        # Reset again
        t.reset(total=n*2)
        assert len(t) == n*2

        # Test with wrong arguments
        t.reset(total='5')
        assert len(t) == 10

        # Reset again
        t.reset()
        assert len(t) == 5

        # Test with wrong arguments
        t.reset(total=None)
        assert len(t) == 0

# Generated at 2022-06-14 14:02:45.926567
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    if IProgress is None:
        return
    pbar = tqdm_notebook.status_printer("file", desc="description")
    assert isinstance(pbar, TqdmHBox)
    assert len(pbar.children) == 3
    assert isinstance(pbar.children[0], HTML)
    assert isinstance(pbar.children[1], IProgress)
    assert isinstance(pbar.children[2], HTML)
    # DEPRECATED: replaced with an 'info' style bar
    # assert pbar.children[1].layout.width == '1000px'
    assert pbar.children[1].layout.width is None

    pbar = tqdm_notebook.status_printer("file", total=10, desc="description")
    assert pbar.children[1].max == 10

# Generated at 2022-06-14 14:02:50.092451
# Unit test for method clear of class tqdm_notebook
def test_tqdm_notebook_clear():
    import unittest
    class Test_tqdm_notebook_clear(unittest.TestCase):
        def test_1(self):
            with tqdm_notebook(total=7, desc='test') as t:
                t.update()
                t.clear()
    unittest.main(module=__name__, exit=False, verbosity=2)

# Generated at 2022-06-14 14:03:00.529975
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():  # pragma: no cover
    with tqdm_notebook(total=None, desc="test") as bar:
        bar.update()
        bar.disp(bar_style='danger', close=True)
        bar.update()
        assert True


# Execute this when run directly
if __name__ == '__main__':  # pragma: no cover
    # Unit test for method status_printer of class tqdm_notebook
    test_tqdm_notebook_status_printer()

    # Main test/demo of the tqdm_notebook progress bar and options
    from time import sleep
    from numpy.random import random
    from IPython.display import clear_output
    from warnings import warn

    # Dummy function for demonstration

# Generated at 2022-06-14 14:03:08.468052
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():

    if IPY <= 0:
        raise s.SkipTest("IPython not found")

    l = [1, 2, 3]

    # should raise StopIteration
    t = tqdm_notebook(l, leave=False)
    with pytest.raises(StopIteration):
        next(t)

    # should not raise StopIteration
    t = tqdm_notebook(l, leave=True)
    with pytest.raises(StopIteration, match="tqdm scaling"):
        next(t)

    # should raise TypeError
    t = tqdm_notebook(l)
    with pytest.raises(TypeError, match="unexpected keyword argument"):
        next(t, None)

    # should not raise TypeError

# Generated at 2022-06-14 14:03:19.393671
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    """Test the method status_printer of class tqdm_notebook"""
    # Setup object
    t = tqdm_notebook()
    t.total = 10

    # Test with total
    res = t.status_printer(None, total=10)
    assert isinstance(res, TqdmHBox)
    assert res.children[-2].max == 10
    assert res.children[-2].min == 0
    assert res.children[-2].bar_style == ''

    # Test without total
    res = t.status_printer(None)
    assert isinstance(res, TqdmHBox)
    assert res.children[-2].max == 1
    assert res.children[-2].min == 0
    assert res.children[-2].bar_style == 'info'



# Generated at 2022-06-14 14:03:21.522299
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    for _ in trange(4):
        sleep(1)


# Generated at 2022-06-14 14:03:25.561137
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from time import sleep
    from tqdm.auto import trange

    for _ in trange(3):
        for _ in trange(2):
            sleep(.01)
        for _ in trange(3):
            sleep(.01)



# Generated at 2022-06-14 14:03:31.690985
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    for leave in [True, False]:
        for total in [None, 0, 10, 100]:
            bar = tqdm_notebook(range(total), leave=leave)
            rng = range(total)
            if next(rng, None):  # mimic error and leave unfinished bar
                bar.reset(total=10)
                assert bar.total == 10
            else:
                bar.reset(total=100)
                assert bar.total == 100
            bar.close()
            if leave:
                assert bar.container.bar.bar_style == "success"
    return True

# Generated at 2022-06-14 14:03:43.020319
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    from unittest.mock import patch

    # Create a mock IProgress widget
    class MockIProgress(object):
        # Attributes of a mock IPython progress bar
        bar_style = ""
        max = 0
        value = 0
        layout = type('layout', (object,), {
            'width': '100px',
            'display': 'inline-flex',
            'flex_flow': 'row wrap'})()

    # instantiate a mock ipywidgets
    ipywidgets.widgets = type('widgets', (object,), {
        'HTML': HTML,
        'HBox': HBox,
        'FloatProgress': MockIProgress})()

    with patch('sys.stderr', new=sys.stdout):

        # Test 1: test if the progress bar has automatically created
        progress_bar = tq

# Generated at 2022-06-14 14:04:03.273579
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from IPython.html.widgets import FloatProgress
    t = tqdm_notebook(total=4)
    assert isinstance(t.pbar, FloatProgress)
    assert t.pbar.value == 0
    assert t.pbar.max == 4
    t.display()
    assert t.pbar.value == 0
    assert t.pbar.max == 4
    t.display()
    t.update()
    assert t.pbar.value == 1
    assert t.pbar.max == 4
    t.display(msg="testing display")
    assert t.pbar.value == 1
    assert t.pbar.max == 4


# Generated at 2022-06-14 14:04:13.298388
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():

    tqdm_notebook.status_printer(
        file=None, total=None, desc=None, ncols=None)

    tqdm_notebook.status_printer(
        file=None, total=10, desc='desc', ncols=None)

    tqdm_notebook.status_printer(
        file=None, total=10, desc='desc', ncols=100)

    tqdm_notebook.status_printer(
        file=None, total=10, desc='desc', ncols=50)

    tqdm_notebook.status_printer(
        file=None, total=10, desc='desc', ncols='100%')


# Generated at 2022-06-14 14:04:20.517854
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    """
    target function of unit test
    """
    # define test target
    target = TqdmHBox()
    target.pbar = tqdm_notebook(total=10)
    target.pbar.format_dict = {"n": 0, "total": 10}
    # define test data
    test_data = ({"pretty": False}, {"pretty": True})
    # define correct answer
    correct_answer = ("\r  0%|          | 0/10 [00:00<?, ?it/s]",
                      "\r{'n': 0, 'total': 10}")

    for i in range(len(test_data)):
        # execute
        current_answer = repr(target._repr_json_(test_data[i]["pretty"]))

        # confirm
        assert current_answer == correct_answer

# Generated at 2022-06-14 14:04:33.372974
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    from .gui import tqdm as _tqdm
    # without total
    progress = tqdm_notebook.status_printer(None)
    assert isinstance(progress, HBox)
    assert progress.children[0].value == ''  # left text
    assert progress.children[1].value == 1  # bar value
    assert progress.children[2].value == ''  # right text

    # with total
    progress = tqdm_notebook.status_printer(None, 100, 'foo', 10)
    assert isinstance(progress, HBox)
    assert progress.children[0].value == 'foo'
    assert progress.children[1].value == 0
    assert progress.children[2].value == ''
    assert progress.children[1].layout.width == '10px'


# with total = 0


# Generated at 2022-06-14 14:04:36.475634
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    with tqdm_notebook(total=3, leave=False) as bar:
        bar.update(1)
        bar.reset(total=1, leave=False)
        bar.update()
# tnrange test, see #604

# Generated at 2022-06-14 14:04:47.509318
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    import ipywidgets  # NOQA
    import IPython.display as display  # NOQA
    b = tqdm_notebook.status_printer(None, desc="Hello", total=5)
    assert isinstance(b, ipywidgets.HBox)
    assert len(b.children) == 3
    assert isinstance(b.children[0], ipywidgets.HTML)
    assert isinstance(b.children[1], ipywidgets.FloatProgress)
    assert isinstance(b.children[2], ipywidgets.HTML)
    display.clear_output()

    b = tqdm_notebook.status_printer(None, desc="Hello", total=5, ncols=200)
    assert len(b.layout.children) == 3

# Generated at 2022-06-14 14:04:57.009412
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep
    pbar = tqdm_notebook()

    # Initial bar
    pbar.display()
    pbar.p = pbar.total / 2.0
    pbar.display(pos=pbar.p, bar_style='success')
    sleep(0.2)

    # Reset bar
    pbar.reset()
    pbar.display(pos=pbar.p, bar_style='info')
    sleep(0.2)

    # First half
    for p in range(1, 51):
        pbar.p = p / 100.0
        pbar.display(pos=pbar.p)
        sleep(0.2)

    # Error bar
    try:
        1 / 0
    except:
        pbar.display(bar_style='danger')

# Generated at 2022-06-14 14:05:00.919963
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    from .tests import dummy_tqdm  # NOQA
    l = tqdm(list(range(3)), leave=False)
    for x in l:
        l.set_description("test")



# Generated at 2022-06-14 14:05:08.419810
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for method `display` of class `tqdm_notebook`.
    """
    import time
    import types

    # Testing no display
    t = tqdm_notebook(['a', 'b', 'c'], disable=True)
    assert not hasattr(t, 'container')

    # Testing display
    t = tqdm_notebook(['a', 'b', 'c'], disable=False)
    assert hasattr(t, 'container')  # minitest warns otherwise
    assert isinstance(t.container, HBox)
    assert t.container.children[0].value.startswith('{desc}:  0%')

    # Testing display #2
    t.update(1)
    assert t.container.children[0].value.startswith('{desc}: 33%|')

# Generated at 2022-06-14 14:05:13.505449
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    print()
    T = tqdm_notebook.TqdmType()
    # Test with a number
    T.status_printer(42, total=100)
    # Test with a tqdm instance
    T.status_printer(tqdm_notebook(total=100), total=100)


# Generated at 2022-06-14 14:05:26.558889
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    import time
    from random import random

    for i in tqdm_notebook(range(int(2e2)), desc="test"):
        time.sleep(random() / 1e3)


if __name__ == "__main__":  # pragma: no cover
    test_tqdm_notebook___iter__()

# Generated at 2022-06-14 14:05:32.271626
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """Test reset method of tqdm_notebook class"""
    for leave in [True, False]:
        for n in [1, 2, 3]:
            with tqdm_notebook(total=5, leave=leave) as progress:
                assert progress.total == 5
                assert progress.n == 0
                progress.update(n)
                progress.reset()
                assert progress.total == 5
                assert progress.n == 0
            assert progress.total is None
            assert progress.n == n
            progress.reset()
            assert progress.total is None
            assert progress.n == 0
            progress.reset(total=3)
            assert progress.total == 3
            assert progress.n == 0
            with tqdm_notebook(total=5, leave=leave) as progress:
                assert progress.total == 5

# Generated at 2022-06-14 14:05:38.855392
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    import time

    # Test with total
    x = tqdm_notebook(total=2)
    x.update()
    time.sleep(1)
    x.update()
    x.close()

    # Test without total
    y = tqdm_notebook()
    y.update()
    time.sleep(1)
    y.update()
    y.close()



# Generated at 2022-06-14 14:05:45.995463
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    with tqdm_notebook(range(100)) as t:
        assert t.miniters == 1
        assert t.unit == 'it'
        assert t.unit_scale == True
        assert t.desc == '100%|##################| 100/100 '
        assert t.ncols == 100
        assert t.disable == False
        assert t.mininterval == 0.1
        assert t.maxinterval == 10
        assert t.unit_divisor == 1000
        assert t.ascii == False
        assert t.unit_scale == True
        assert t.gui == True
        assert t.dynamic_ncols == True
        assert t.leave == False
        assert t.postfix == None
        for i in t:
            assert i >= 0 and i < 100
        assert t.total == 100

# Generated at 2022-06-14 14:05:50.131285
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():  # pragma: no cover
    from tqdm.auto import trange

    with trange(10) as t:
        for i in t:
            t.set_description("in loop %s" % i)
            t.update()



# Generated at 2022-06-14 14:05:59.259561
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from time import sleep, time
    from IPython.display import clear_output

    # Create test cases
    test_cases = {
        "bar": {"desc": "Loading", "ncols": 100, "colour": "blue"},
        "msg": {"msg": "Loading...", "ncols": "100%",
                "colour": "green"},
        "close": {"desc": "Loading", "colour": "red"},
        "bar_style": {"desc": "Loading", "ncols": 100,
                      "colour": "blue", "bar_style": "success"},
        "sec": {"desc": "Loading", "ncols": 100, "colour": "blue"},
    }

    # Initialize tnrange and progress bar

# Generated at 2022-06-14 14:06:03.417414
# Unit test for method __repr__ of class TqdmHBox
def test_TqdmHBox___repr__():
    import tempfile
    import os

    with open(os.devnull, 'w') as f, tempfile.TemporaryFile(mode='w+') as fp:
        tqdm_notebook(total=1, file=fp, dynamic_ncols=True, disable=False).display(
            file=f)


# Note: Deprecated range function defined at the top of this file

# Generated at 2022-06-14 14:06:07.971975
# Unit test for constructor of class tqdm_notebook
def test_tqdm_notebook():
    import time
    with tqdm_notebook(total=10) as t:
        for i in range(10):
            time.sleep(0.01)
            t.update()



# Generated at 2022-06-14 14:06:15.003671
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    from random import randrange
    from ipywidgets import FloatProgress
    import pytest
    t = tqdm_notebook(total=10)
    for _ in range(10):
        idx = randrange(5)
        t.display(str(idx), pos=idx)
    assert t.container.children[-2].value == '4'
    assert (t.container.children[-1].value == ''
            or t.container.children[-1].value == '0it [00:00, ?it/s]')

    t.display_total_mode()
    assert '10it' in t.container.children[-1].value

    desc = 'Testing display error'
    t = tqdm_notebook(total=10, desc=desc)

# Generated at 2022-06-14 14:06:21.324503
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    from numpy.random import rand

    # setup Tqdm with default values
    t = tqdm_notebook(total=5)
    for i in range(5):
        sleep(rand())
        t.update()

    # setup Tqdm with additional values
    t = tqdm_notebook(total=5, desc="Iteration")
    for i in range(5):
        sleep(rand())
        t.update()



# Generated at 2022-06-14 14:06:37.836840
# Unit test for method status_printer of class tqdm_notebook
def test_tqdm_notebook_status_printer():
    try:
        import ipywidgets
    except ImportError:
        try:
            import IPython.html.widgets
        except ImportError:
            return
    assert tqdm_notebook.status_printer(None, total=10, desc='Hello') is not None


if __name__ == '__main__':
    test_tqdm_notebook_status_printer()

# Generated at 2022-06-14 14:06:40.785757
# Unit test for method close of class tqdm_notebook
def test_tqdm_notebook_close():
    t = tqdm_notebook(10)
    t.update(5)
    t.close()
    t.close()
    t.update(5)
    t.close()
    t.close()
    t.close()

# Generated at 2022-06-14 14:06:50.349338
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    # Dummy IPython/Jupyter Notebook environment
    class Dummy_display(object):
        def __init__(self, **kwargs):
            pass

        def __call__(self, **kwargs):
            pass

    sys_modules_copy = sys.modules.copy()

# Generated at 2022-06-14 14:06:57.800979
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    """
    Unit test for method `display` of class `tqdm_notebook`.
    """
    pbar = tqdm_notebook(total=9, desc='', unit='test')
    # no msg, pos, close, bar_style
    pbar.display()
    assert pbar.container.visible
    assert pbar.container.children[0].value == ''
    assert pbar.container.children[1].bar_style == ''
    assert pbar.container.children[2].value == ''

    # no msg, pos, close, bar_style
    pbar.display(stop=1)
    assert pbar.container.visible
    assert pbar.container.children[0].value == ''
    assert pbar.container.children[1].bar_style == ''

# Generated at 2022-06-14 14:06:58.462310
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():
    pass

# Generated at 2022-06-14 14:07:00.817182
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    with tqdm_notebook(total=5) as pbar:
        for _ in range(5):
            pbar.update()

# Generated at 2022-06-14 14:07:09.341050
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    import time
    import random
    import numpy as np
    from tqdm import tqdm_notebook as tqdm
    s = sum([random.random() for _ in range(100)])
    n = 0
    for i in tqdm(range(100)):
        sleep_dur = random.random() * 0.01
        time.sleep(sleep_dur)
        n += random.random()
        tqdm.reset(total=s)
        tqdm.update(n)
    # Check we finished correctly
    assert np.isclose(s, n, atol=10e-4)

# Generated at 2022-06-14 14:07:16.365702
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    from contextlib import redirect_stdout

    from io import StringIO
    import re
    import time

    with StringIO() as buf, redirect_stdout(buf):
        with tqdm_notebook(total=42) as bar:
            bar.display()
            time.sleep(1)
            bar.reset(total=0)
            time.sleep(1)
            bar.reset(total=None)
            time.sleep(1)
            bar.reset(total=float('inf'))
            time.sleep(1)
            bar.reset(total=-1)
            time.sleep(1)
    buf = buf.getvalue()

    assert len(re.findall(r'\s*\d+%', buf)) > 3

# Generated at 2022-06-14 14:07:24.804074
# Unit test for method reset of class tqdm_notebook
def test_tqdm_notebook_reset():
    """ Unit test for method reset of class tqdm_notebook """
    from tqdm.auto import trange
    for unit_scale in (1, True, None):
        for total, leave in ((10, False), (10, True), (None, True)):
            t = trange(100, unit_scale=unit_scale,
                       leave=leave, total=total)
            t._instances.clear()
            t._decr_instances()
            t.reset()
            assert t.n == 0
            assert t.last_print_n == -1
            if total is None:
                # ncols hidden
                assert t.container.children[-2].layout.width == '20px'
            if leave and total is None:
                assert t.container.children[-2].bar_style == 'info'

# Generated at 2022-06-14 14:07:27.382040
# Unit test for method __iter__ of class tqdm_notebook
def test_tqdm_notebook___iter__():
    from time import sleep
    for i in tqdm_notebook(range(3), desc='tqdm_notebook'):
        sleep(.1)



# Generated at 2022-06-14 14:07:52.476843
# Unit test for method update of class tqdm_notebook
def test_tqdm_notebook_update():
    # Initialization of variables
    bar = tqdm_notebook(total=15000)
    # Test division by zero
    bar.update()
    bar.update(10)
    bar.update(15000)
    bar.update(15001)
    return



# Generated at 2022-06-14 14:08:00.739524
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():  # pragma: no cover
    """
    Test if `display()` works properly and the best that can be expected.
    """
    try:
        display()
    except Exception:
        pass

    try:  # if not IPython
        raise KeyboardInterrupt()
    except NameError:
        raise  # other NameErrors will be caught by tqdm itself (if used)
    except KeyboardInterrupt:
        pass

    with tqdm_notebook(total=1) as t:
        time.sleep(.5)
        t.display()

    with tqdm_notebook(total=1) as t:
        time.sleep(.5)
        t.display(msg='msg')

    with tqdm_notebook(total=1) as t:
        time.sleep(.5)
        t.display

# Generated at 2022-06-14 14:08:08.629030
# Unit test for method display of class tqdm_notebook
def test_tqdm_notebook_display():

    import sys
    import unittest
    from tqdm.notebook import tqdm
    from time import sleep

    class TqdmDisplayTest(unittest.TestCase):
        def test_display(self):
            """Tests that tqdm correctly displays
            pending bars when display() is called"""
            msg = 'message'

            with tqdm(total=2, leave=False) as t:
                self.assertEqual(t.n, 0, msg=msg)
                t.update()
                self.assertEqual(t.n, 1, msg=msg)
                t.display(pos=0, total=2, bar_style=None)
                self.assertEqual(t.n, 1, msg=msg)
                t.display(pos=1, total=2, bar_style='success')