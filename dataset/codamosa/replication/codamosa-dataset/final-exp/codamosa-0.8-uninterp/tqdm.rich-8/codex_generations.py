

# Generated at 2022-06-22 13:27:43.121730
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    _test_tqdm_rich_display()


# Generated at 2022-06-22 13:27:50.457297
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress = Progress()
    rate_column = RateColumn(unit="B")
    task = progress.add_task("test")
    task.update(speed=1.0)
    assert rate_column.render(task) == Text("1.0 B/s", style="progress.data.speed")
    task.update(speed=1000.0)
    assert rate_column.render(task) == Text("1.0 KB/s", style="progress.data.speed")


# Generated at 2022-06-22 13:27:53.378075
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="/s")
    assert rate_column.render(rate_column) == Text("? /s", style="progress.data.speed")

# Generated at 2022-06-22 13:27:57.065125
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    try:
        # pylint: disable=E1101
        tqdm_rich.close()
    except Exception:
        # pylint: enable=E1101
        raise SystemExit(1)

# Generated at 2022-06-22 13:28:00.972164
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=100) as pbar:
        for i in range(100):
            pbar.update()
    with tqdm_rich(total=100, desc="Desc") as pbar:
        for i in range(100):
            pbar.update()

# Generated at 2022-06-22 13:28:07.812192
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from .tqdm import tnrange
    from time import sleep
    it = tnrange(5)
    for i in it:
        it.set_description(str(i))
        sleep(0.1)
    it.close()

if __name__ == '__main__':  # pragma: no cover
    test_tqdm_rich_close()

# Generated at 2022-06-22 13:28:09.368426
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    for _ in tqdm(range(3)):
        pass

# Generated at 2022-06-22 13:28:22.260226
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    a = FractionColumn()

    # test division by 0
    assert a.render(object()) == Text("0.0/0.0 ", style="progress.download")

    # test division by integer
    b = FractionColumn(unit_scale=True, unit_divisor=1000)
    assert b.render(object()) == Text("0.0/0.0 ", style="progress.download")
    assert b.render(object(total=123)) == Text("0.0/0.1 K", style="progress.download")
    assert b.render(object(total=123, completed=67)) == Text("0.1/0.1 K", style="progress.download")
    c = FractionColumn(unit_scale=False, unit_divisor=1000)

# Generated at 2022-06-22 13:28:25.459315
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=5) as t:
        pass
    assert t._prog.total == 5
    t.reset(total=10)
    assert t._prog.total == 10

# Generated at 2022-06-22 13:28:28.891170
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import pytest
    from pytest import approx
    r = RateColumn(unit_scale=False)
    assert '1000.1 /s' == r.render({"speed":1000.1})


# Generated at 2022-06-22 13:28:43.174758
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from sys import stdout
    from time import sleep
    try:
        from tqdm.contrib.test import dummy
    except ImportError:
        from tqdm.test import dummy
    dummy = dummy()
    # No bar to close
    with tqdm(total=100, file=stdout, desc='test_tqdm_rich_close',
              disable=False) as _t:
        _t.close()
        sleep(.5)

    # With bar
    _t = tqdm(total=100, file=stdout, desc='test_tqdm_rich_close',
              disable=False)
    sleep(.5)
    _t.close()

# Generated at 2022-06-22 13:28:44.742875
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    try:
        p = tqdm_rich(total=10)
    except:
        return
    p.clear()

# Generated at 2022-06-22 13:28:53.115436
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fc = FractionColumn()
    fc.unit_scale, fc.unit_divisor = False, 1
    assert fc.render({'completed': 2, 'total': 5}) == Text('2/5 ')
    fc.unit_scale = True
    assert fc.render({'completed': 2, 'total': 5}) == Text('2.0/5.0')
    fc.unit_scale, fc.unit_divisor = False, 1000
    assert fc.render({'completed': 2, 'total': 5}) == Text('2/5.0 K')
    fc.unit_scale = True
    assert fc.render({'completed': 2, 'total': 5}) == Text('2.0/5.0 K')

# Generated at 2022-06-22 13:28:55.464705
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    t = tqdm_rich(list(range(5)), bar_format=".", unit="i")
    t.close()
    assert t.format_dict["total"] == 5



# Generated at 2022-06-22 13:28:59.812327
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = tqdm_rich(total=10)
    col = FractionColumn()
    assert col.render(task) == Text('0.0/10.0 ', style='progress.download')
    assert isinstance(col.render(task), Text)



# Generated at 2022-06-22 13:29:09.009945
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    import pytest  # noqa: F401
    from .tqdm import format_sizeof, format_interval, format_meter, unicode, \
        moveto_line_up, clear_line, term_move_up

    idx, _range = 0, range(100)

# Generated at 2022-06-22 13:29:15.850829
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():

    task = tqdm_rich(total=1000, desc='A progress bar')
    for i in range(500):
        task.update()
    task.reset(total=100, desc='A new bar')
    for i in range(50):
        task.update()
    task.close()


if __name__ == "__main__":
    from .tests import _test_tqdm_rich
    _test_tqdm_rich()

# Generated at 2022-06-22 13:29:28.604865
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fc_unit_scale=True
    fc_unit_divisor=1024
    completed = 1024
    total = 2097152
    unit, suffix = filesize.pick_unit_and_suffix(total, ["", "K", "M", "G", "T", "P", "E", "Z", "Y"], fc_unit_divisor)
    precision = 0 if unit == 1 else 1
    # Test result 
    result = FractionColumn(unit_scale=fc_unit_scale, unit_divisor=fc_unit_divisor).render(Progress(total=total, completed=completed)) 
    assert result == Text(f"{completed/unit:,.{precision}f}/{total/unit:,.{precision}f} {suffix}",style="progress.download") 


# Generated at 2022-06-22 13:29:34.611149
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=1,
                   desc='Progress',
                   position=0,
                   bar_format='{desc}{bar}{percentage:3.0f}%') as progress:
        progress.update(0)
        progress.reset(2)
        progress.update(1)
        progress.update(2)
        progress.refresh()

# Generated at 2022-06-22 13:29:43.227357
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    error = 0.0
    for _ in range(100):
        x = np.random.randint(0,1000)
        choice = np.random.choice(['unit_scale','unit_divisor'])
        unit, suffix = filesize.pick_unit_and_suffix(
            x,["", "K", "M", "G", "T", "P", "E", "Z", "Y"],1000)
        if choice == 'unit_scale':
            col = RateColumn(unit="",unit_scale=True,unit_divisor=unit)
            out = (x/unit)
        else:
            col = RateColumn(unit="",unit_scale=False,unit_divisor=unit)
            out = (x/unit)/1000

# Generated at 2022-06-22 13:29:57.126666
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = None
    unit = "MiB"
    speed = 1024
    column = RateColumn(unit, True, 1024)
    actual = column.render(task).text
    expected = "1.00 MiB/s"
    assert actual == expected

if __name__ == '__main__':
    test_RateColumn_render()

# Generated at 2022-06-22 13:30:09.313573
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import tqdm
    from .utils import fpformat
    if not tqdm:
        print('to run this test install tqdm >= 4.15.0')
        return
    assert (str(tqdm_rich(10)) == tqdm(10)._instances[0]._get_free_str() ==
            '[100%]|███████████| 10/10 [00:00<00:00, 1000.00it/s]')
    assert (str(tqdm_rich(10, 10)) == tqdm(10, 10)._instances[0]._get_free_str() ==
            '[100%]|███████████| 10/10 [00:00<00:00, 1000.00it/s]')

# Generated at 2022-06-22 13:30:11.666854
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm(total=2) as pbar:
        pbar.clear()



# Generated at 2022-06-22 13:30:20.962088
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test method render()"""
    rate_column = RateColumn()
    task = Progress(
        completed=0,
        total=20,
        start_time=1571748362.746571,
        time_delta=0.021132,
        time_start=1571748362.725439,
        handle="(total: 15.02 sec, remaining: 14.00 sec)",
        speed=2,
        description="",
        transient=False,
    )
    assert rate_column.render(task) == "2.00 /s"
    rate_column = RateColumn(unit_scale=True)
    assert rate_column.render(task) == "2.00 B/s"
    rate_column = RateColumn(unit_scale=True, unit_divisor=1024)
    assert rate_column

# Generated at 2022-06-22 13:30:24.964664
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    value = RateColumn(unit="")
    assert value.render(None) == Text(f"? /s", style="progress.data.speed")
    value = RateColumn(unit="", unit_scale=True)
    assert value.render(None) == Text(f"? /s", style="progress.data.speed")

# Generated at 2022-06-22 13:30:37.497375
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from contextlib import contextmanager
    from unittest import TestCase, main
    from rich.progress import Progress

    class dummy_Progress(Progress):
        _progress = []

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            dummy_Progress._progress = self

        def __getattr__(self, name):
            return getattr(dummy_Progress._progress, name)

        @contextmanager
        def __call__(self, *args, **kwargs):
            yield self

    class TestTqdmRichDisplay(TestCase):
        def test_display(self):
            with self.assertRaises(AttributeError):
                # Test case without _prog
                tqdm_rich().display()


# Generated at 2022-06-22 13:30:43.750964
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    the_tqdm = tqdm_rich(range(100), bar_format='{l_bar}{bar:10.2f}{r_bar}')
    try:
        for i in the_tqdm:
            pass
    finally:
        the_tqdm.close()

    try:
        for i in trange(100):
            pass
    finally:
        the_tqdm.close()

# Generated at 2022-06-22 13:30:46.651205
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    for x in [200, 2000, 200000, 2000000]:
        _tqdm = tqdm_rich(total=x)
        _tqdm.reset(total=0)

# Generated at 2022-06-22 13:30:56.998992
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Unit test for method render of class RateColumn."""
    import pandas as pd
    test_df = pd.read_csv('data/RateColumn_unit_test_data.csv', index_col=0)
    rate_column = RateColumn(unit_scale=False)
    for index, row in test_df.iterrows():
        row_label = rate_column.render(row)
        test_df.loc[index, 'label'] = row_label

    test_df['pass'] = test_df['label'] == test_df['expected_label']
    test_df['pass'].value_counts()
    assert test_df['pass'].all()

# Generated at 2022-06-22 13:30:59.712703
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no coverage
    with tqdm(total=10) as pbar:
        for i in range(10):  # pragma: no coverage
            pbar.update()


# Generated at 2022-06-22 13:31:18.457381
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=100) as pbar:
        for i in range(100):
            pbar.update()
            if i == 20:
                pbar.reset(100)
                pbar.set_description('New description')
    assert i == 99

# Generated at 2022-06-22 13:31:28.587874
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from .utils import _range
    from tqdm.rich import trange

    for i in trange(1000000000): # test case to fail without the fix described in issue #2
        pass

    for i in trange(1000, unit_scale=True):
        pass

    for i in trange(1000, unit_scale=True, unit_divisor=1024):
        pass

    for i in trange(1000, desc='1'):
        pass

    for i in trange(1000, unit_scale=True, desc='2'):
        pass

    for i in trange(1000, unit_scale=True, unit_divisor=1024, desc='3'):
        pass

# Generated at 2022-06-22 13:31:31.254769
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=10) as pbar:
        assert pbar.reset(total=20) is None

# Generated at 2022-06-22 13:31:37.143883
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from tqdm.auto import trange
    with trange(10, disable=True) as t:
        t.display()


if __name__ == "__main__":
    from tqdm.auto import trange
    for i in trange(100, desc="tqdm_rich", leave=False, disable=False):
        pass

# Generated at 2022-06-22 13:31:41.457732
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    input_rate = 1024
    input_unit = 'B'
    output = RateColumn(input_unit, unit_scale=True, unit_divisor=1024).render(input_rate)
    assert output == Text("1.00 K/s", style="progress.data.speed")

# Generated at 2022-06-22 13:31:42.847700
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    for _ in tqdm_rich(range(2)):
        pass

# Generated at 2022-06-22 13:31:51.047596
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate = RateColumn()
    speed = rate.render(1000)
    assert str(speed) == "1.0 KB/s"
    speed = rate.render(1)
    assert str(speed) == "1.0 KB/s"
    speed = rate.render(0)
    assert str(speed) == "0.0 KB/s"
    speed = rate.render(100000)
    assert str(speed) == "100.0 KB/s"
    speed = rate.render(10000)
    assert str(speed) == "10.0 KB/s"
    speed = rate.render(100)
    assert str(speed) == "0.1 KB/s"
    speed = rate.render(10)
    assert str(speed) == "0.01 KB/s"
    speed = rate.render(1)

# Generated at 2022-06-22 13:32:02.498694
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """Test tqdm_rich (rich constructor)."""
    # Check general functionality
    with tqdm(total=5, unit_scale=True, unit='iB') as pbar:
        for _ in range(3):
            pbar.update()

    # Check total=None
    with tqdm(unit_scale=True, unit='iB') as pbar:
        pbar.update(1)
        assert pbar.total is None
        pbar.update(2)
        assert pbar.total is None
        pbar.update(1)
        assert pbar.total is None
        pbar.n = 0

    # Check rate unit
    with tqdm(total=5, unit_scale=True, unit='iB') as pbar:
        for _ in range(3):
            pbar.update

# Generated at 2022-06-22 13:32:12.984412
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Check the method reset of class tqdm_rich with parameter total=None and total=1
    """
    tqdm_rich_1 = tqdm_rich(range(5000), total=5000)
    tqdm_rich_1.reset()
    assert tqdm_rich_1.n == 0
    assert tqdm_rich_1.total == 5000
    tqdm_rich_2 = tqdm_rich(range(5000), total=5000)
    tqdm_rich_2.reset(total=1)
    assert tqdm_rich_2.n == 0
    assert tqdm_rich_2.total == 1

# Generated at 2022-06-22 13:32:24.651043
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    tqdm_rich_obj = tqdm_rich(*range(1), unit="i/s", unit_scale=True)
    assert hasattr(tqdm_rich_obj, '_prog')
    assert tqdm_rich_obj.disable == False
    assert hasattr(tqdm_rich_obj, 'desc') == True
    assert tqdm_rich_obj.desc == ''

    tqdm_rich_obj.display()
    assert hasattr(tqdm_rich_obj, '_task_id')
    assert hasattr(tqdm_rich_obj, '_prog')
    tqdm_rich_obj.display()


# Generated at 2022-06-22 13:33:24.825067
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Unit test for method reset of class tqdm_rich."""
    import sys
    from .std import tqdm

    with tqdm(total=100) as pbar:
        for i in range(50):
            pbar.update()

        assert pbar.n == 50

        pbar.reset(total=10)
        assert pbar.total == 10
        assert pbar.n == 0

        for i in range(5):
            pbar.update()

        assert pbar.n == 5

        pbar.reset()
        assert pbar.total is None
        assert pbar.n == 0

        pbar.reset(total=None)
        assert pbar.total is None
        assert pbar.n == 0

        pbar.reset(total=0)
        assert pbar.total == 0
       

# Generated at 2022-06-22 13:33:29.762816
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from .utils import patch_configuration
    from .utils import TqdmDeprecationWarning
    kwargs = {'unit': 'Γ', 'unit_scale': True, 'unit_divisor': 1024}
    r = RateColumn(**kwargs)

    with patch_configuration('compliance', True):
        warn("collections.deque + maxlen is deprecated. Use maxlen=N Deque instead.", TqdmDeprecationWarning, stacklevel=2)
        assert r.render(ProgressColumn(speed=None)) == Text("? Γ/s", style="progress.data.speed")
        assert r.render(ProgressColumn(speed=1024*1024)) == Text("1.0 MΓ/s", style="progress.data.speed")

# Generated at 2022-06-22 13:33:32.921257
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fc = FractionColumn(unit_scale=True, unit_divisor=1000)
    task = {'completed': 1, 'total': 1024}
    assert fc.render(task) == Text('1.0/1.0 K', style='progress.download')


# Generated at 2022-06-22 13:33:37.627781
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    column = FractionColumn(unit_scale=False, unit_divisor=1000)
    task = Progress.__getitem__(column)
    task(description="", total=1_000, completed=500)
    assert column.render(task) == Text("500.0/1,000 ", style="progress.download")



# Generated at 2022-06-22 13:33:48.645780
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from types import SimpleNamespace
    class fake_task(SimpleNamespace):
        def __init__(self, completed, description):
            self.completed = completed
            self.description = description
    bar = tqdm_rich()
    bar._task_id = bar._prog.add_task("test_tqdm_rich_display", total=1)
    # prepare parameters to test different situations
    completed = [0, 0.5, 1]
    description = ["", " ", "t"]
    # begin the test
    for i, j in zip(completed, description):
        bar._prog._tasks[bar._task_id] = fake_task(i, j)
        bar.display()
        # check results
        assert bar._prog.completed == i
        assert bar._prog.description == j

# Generated at 2022-06-22 13:33:57.149927
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # rate = speed * unit
    rate = 1000
    assert RateColumn(unit='B').render(rate) == '1KB/s'
    assert RateColumn(unit='B', unit_scale=True).render(rate) == '1.0KB/s'
    assert RateColumn(unit='B', unit_divisor=1).render(rate) == '1.0KB/s'
    assert RateColumn(unit='B', unit_scale=True, unit_divisor=1).render(rate) == '1.0KB/s'
    assert RateColumn(unit='B', unit_divisor=1024).render(rate) == '1.0MB/s'
    assert RateColumn(unit='B', unit_scale=True, unit_divisor=1024).render(rate) == '1.0MB/s'


# Generated at 2022-06-22 13:34:05.109714
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    assert FractionColumn().render({'completed': 0, 'total': 1000}) == Text('0.0/1.0', style='progress.download')
    assert FractionColumn(unit_scale=True).render({'completed': 0, 'total': 1000}) == Text('0.0/1.0 K', style='progress.download')
    assert FractionColumn(unit_divisor=1024).render({'completed': 0, 'total': 1000}) == Text('0.0/1.0', style='progress.download')
    assert FractionColumn(unit_scale=True, unit_divisor=1024).render({'completed': 0, 'total': 1000}) == Text('0.0/1.0 Ki', style='progress.download')
    assert FractionColumn(unit_scale=True, unit_divisor=1024).render

# Generated at 2022-06-22 13:34:15.147538
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import math
    import pytest

    # tests with unit scale

# Generated at 2022-06-22 13:34:18.898830
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    >>> t = tqdm_rich(total=10, desc='Bla', gui=True)
    >>> for _ in t:
    ...     t.update()    # progress bar moves
    ...     t.reset(30)   # progress bar resets to 0
    ...     t.update()    # progress bar moves
    """

# Generated at 2022-06-22 13:34:25.971077
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .tests_tqdm import with_setup
    from random import randint
    try:
        from unittest.mock import patch
    except ImportError:  # pragma: no cover
        from mock import patch  # type: ignore


# Generated at 2022-06-22 13:36:02.263957
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test tqdm_rich.display method."""
    from rich.progress import TaskID, Progress, TimeElapsedColumn, BarColumn
    from rich.style import Style
    from rich.text import Text
    d = {'progress.download': Style(color='blue'), 'progress.data.speed': Style()}

# Generated at 2022-06-22 13:36:11.934495
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = Progress(total=100, start=0, completed=50)
    assert FractionColumn(unit_scale=False).render(task).text == "50/100"
    assert FractionColumn(unit_scale=True, unit_divisor=1000,).render(task).text == "0.1/0.1"
    assert FractionColumn(unit_scale=True, unit_divisor=1000,).render(task).style == "progress.download"
    assert FractionColumn(unit_scale=False).render(task).style == "progress.download"

# Generated at 2022-06-22 13:36:21.562776
# Unit test for method render of class FractionColumn

# Generated at 2022-06-22 13:36:26.931256
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    with tqdm_rich(total=10, desc="test") as pbar:
        for i in range(10):
            pbar.update(1)
            time.sleep(0.1)
    with tqdm_rich(total=None, desc="test") as pbar:
        time.sleep(1)
        pbar.reset(total=10)
        for i in range(10):
            pbar.update()
            time.sleep(0.1)



# Generated at 2022-06-22 13:36:31.801918
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm_rich(range(10)) as pbar:
        pbar.display()
        pbar.n = 4
        pbar.display()

# Generated at 2022-06-22 13:36:34.554869
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import warnings
    warnings.simplefilter("ignore", TqdmExperimentalWarning)  # we really want to run test
    task = None
    column = FractionColumn()
    assert column.render(task) is None

# Generated at 2022-06-22 13:36:39.572783
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    unit = "s"
    speed = 1000
    unit_scale = False
    unit_divisor = 1000
    rate_column = RateColumn(unit=unit, unit_scale=unit_scale,
                             unit_divisor=unit_divisor)
    expected_text = "1.0 s/s"
    actual_text = rate_column.render(None)
    assert actual_text.text == expected_text

# Generated at 2022-06-22 13:36:50.224890
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Unit test for method render of class RateColumn
    """
    from rich.progress import Task
    progress_task = Task("task_description", total=10)
    progress_task.completed = 10
    progress_task.speed = 10
    column = RateColumn(unit="B")
    assert column.render(progress_task) == Text("10.00 B/s", style="progress.data.speed")

    column = RateColumn(unit="B", unit_scale=True, unit_divisor=1024)
    assert column.render(progress_task) == Text("10.00 KB/s", style="progress.data.speed")


# Generated at 2022-06-22 13:37:00.980551
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Test method render of class RateColumn
    """
    # Case 1: rate > 0 and unit_scale = False
    task = object()
    task.speed = 100
    rc = RateColumn(unit="", unit_scale=False, unit_divisor=1000)
    assert rc.render(task) == Text("100.0 /s", style="progress.data.speed")

    # Case 2: rate > 0 and unit_scale = True
    task = object()
    task.speed = 100
    rc = RateColumn(unit="", unit_scale=True, unit_divisor=1000)
    assert rc.render(task) == Text("100.0 /s", style="progress.data.speed")

    # Case 3: rate == None
    task = object()
    task.speed = None

# Generated at 2022-06-22 13:37:05.697137
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test if progress bar reset works for repeated use."""
    for j in tqdm(range(20)):
        value = j
        if j == 5:
            tqdm.reset(total=10)
            value = 0
        elif j == 10:
            tqdm.reset()
            value = 0
        tqdm.update(1)
        assert value == j or value == 0