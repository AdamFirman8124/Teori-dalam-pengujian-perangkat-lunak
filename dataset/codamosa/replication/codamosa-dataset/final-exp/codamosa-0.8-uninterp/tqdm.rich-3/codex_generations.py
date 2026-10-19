

# Generated at 2022-06-22 13:27:52.948128
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import io
    import sys
    import unittest

    class TestRateColumnRender(unittest.TestCase):
        def test_rate(self):
            ratecol = RateColumn(unit="MiB", unit_scale=False, unit_divisor=1024)
            # test for None speed
            output = io.StringIO()
            sys.stdout = output
            ratecol.render(None)
            sys.stdout = sys.__stdout__
            self.assertIn('? MiB/s', output.getvalue().strip())
            # test for non-None speed
            output = io.StringIO()
            sys.stdout = output
            d = dict()
            d['speed'] = 1
            ratecol.render(d)
            sys.stdout = sys.__stdout__

# Generated at 2022-06-22 13:28:05.591449
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    import os
    import tempfile
    import unittest
    from distutils.version import LooseVersion
    from rich.progress import Progress, Console
    from rich.console import Console
    tqdm = tqdm_rich(range(3), desc='Task 1')
    # file test
    os.chdir(tempfile.mkdtemp())
    f = tempfile.NamedTemporaryFile(mode='w', delete=False)
    file = f.name
    f.close()
    tqdm = tqdm_rich(range(3), desc='Task 2', file=file)
    tqdm.close()
    f = open(file)
    self.assertEqual(f.read(), 'Task 2: 100%|##########| 3/3 [00:00<00:00, ?it/s]')


# Generated at 2022-06-22 13:28:17.440658
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress = tqdm.tqdm_rich(total=3, leave=True, unit_scale=True, unit_divisor=1000, desc="1:")
    progress.update(1)
    assert RateColumn(unit_scale=True, unit_divisor=1000).render(progress) == Text('∞ K/s', style='progress.data.speed')
    progress.update(1)
    assert RateColumn(unit_scale=True, unit_divisor=1000).render(progress) == Text('2.000 K/s', style='progress.data.speed')
    progress.update(1)
    assert RateColumn(unit_scale=True, unit_divisor=1000).render(progress) == Text('1.000 K/s', style='progress.data.speed')

    progress = tqdm.tq

# Generated at 2022-06-22 13:28:20.906150
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from rich.progress import Manager
    from .std import tqdm
    t = tqdm(range(100), close=True)
    for _ in t:
        pass
    assert Manager.current is None

# Generated at 2022-06-22 13:28:30.369399
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = ProgressColumn.Task(3, 10)
    fraction_col = FractionColumn()
    assert fraction_col.render(task).text == "0.3/1.0"
    fraction_col = FractionColumn(unit_scale=True)
    assert fraction_col.render(task) == Text("0.3/1.0 ", style="progress.download")
    task = ProgressColumn.Task(20, 10)
    fraction_col = FractionColumn(unit_scale=True)
    assert fraction_col.render(task) == Text("2.0/1.0 K", style="progress.download")


# Generated at 2022-06-22 13:28:34.087746
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    """Test tqdm_rich.clear method"""
    with trange(1) as t:
        assert not t.disable
        t.clear()



# Generated at 2022-06-22 13:28:36.707135
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():  # pragma: no cover
    """Unit test for method close of class tqdm_rich."""
    with tqdm_rich(100) as t:
        for i in range(100):
            t.update()
            t.close()

# Generated at 2022-06-22 13:28:47.532431
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    # test disabled
    with tqdm_rich(disable=True) as _t:
        _t.reset(total=1e6)
        for i in _range(1000):
            _t.update(10)
        _t.reset(total=1e6)
        for i in _range(1000):
            _t.update(10)
        _t.reset(total=1e6)

    # test enabled
    with tqdm_rich() as _t:
        _t.reset(total=1e6)
        for i in _range(1000):
            _t.update(10)
        _t.reset(total=1e6)
        for i in _range(1000):
            _t.update(10)
        _t.reset(total=1e6)

# Generated at 2022-06-22 13:28:56.512453
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # test with speed of 0
    task = type('',(object,),{'speed':0})()
    assert RateColumn().render(task) == Text(f"? /s", style="progress.data.speed")
    # test with speed of 1
    task = type('',(object,),{'speed':1})()
    assert RateColumn().render(task) == Text(f"1 /s", style="progress.data.speed")
    # test with speed of 1000
    task = type('',(object,),{'speed':1000})()
    assert RateColumn().render(task) == Text(f"1.0 K/s", style="progress.data.speed")
    # test with speed of 10000
    task = type('',(object,),{'speed':10000})()

# Generated at 2022-06-22 13:29:04.936996
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    import os

    def clear_func_pass(*_, **__):
        pass

    tqdm_rich.clear = clear_func_pass
    iterable = range(5)
    tqdm_rich(iterable,
              disable=False,
              leave=False,
              smoothing=0.5,
              miniters=1,
              mininterval=0,
              ascii=False,
              desc='Testing tqdm_rich').__exit__()
    if os.name == 'nt':
        tqdm_rich.clear = std_tqdm.clear

# Generated at 2022-06-22 13:29:11.439466
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fc = FractionColumn()
    for i in range(100):
        completed = random.randint(1, 10000000)
        total = random.randint(completed, 100000000)
        task = type('Task', (object,), {'completed': completed, 'total': total})
        text = fc.render(task)
        assert isinstance(text, Text)
        assert text.plain == f'{int(completed)/int(total):.0%}'


# Generated at 2022-06-22 13:29:16.386158
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with trange(50) as t:
        for _ in tqdm(range(50)):
            t.set_description('Processing')
            t.set_postfix(file=['foo', 'bar', 'baz'], refresh=True)
            t.display()


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)

# Generated at 2022-06-22 13:29:29.162500
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test function of rendering rate column."""
    task = std_tqdm()
    print(task)
    task.n, task.nmin, task.last_print_n, task.last_print_t = 0, 0, 0, 0
    task.total = 2000
    task.smoothing = 0
    task.last_print_t -= 60
    task.update(1)
    task.update(1)
    rc = RateColumn()
    assert rc.render(task).plain == "2.0  B/s"
    task.total = 1024**4
    assert rc.render(task).plain == "1.0  B/s"
    assert rc.render(task).plain == "1.0  B/s"
    task.total = 10*1024**4

# Generated at 2022-06-22 13:29:39.982957
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """
    Tests the constructor of class tqdm_rich.
    """
    from .std import tqdm
    _test_tqdm = tqdm_rich(range(10), desc="test",
                           unit_scale=True, mininterval=.1)
    for _ in _test_tqdm:
        pass
    _test_tqdm.close()

    _test_tqdm2 = tqdm(range(10), desc="test", unit="B",
                       unit_scale=True, mininterval=.1)
    for _ in _test_tqdm2:
        pass
    _test_tqdm2.close()


# Generated at 2022-06-22 13:29:44.226680
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    expected = '0/2.3 G'
    actual = FractionColumn(unit_scale=True, unit_divisor=1000)
    actual = actual.render(0, 2300)
    assert actual == expected



# Generated at 2022-06-22 13:29:47.174221
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    pbar = tqdm_rich(total=10)
    for i in range(10):
        time.sleep(0.1)
        pbar.update()
    pbar.close()

# Generated at 2022-06-22 13:29:54.308045
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from .utils import _range
    from .std import tqdm
    from .utils import format_meter
    import io
    import sys

    f = io.StringIO()
    for i in tqdm(_range(100), total=100, file=f):
        assert '\r' in format_meter(i, 100, 1)
    f.seek(0)
    assert f.read() == '100it [00:00, 1787.24it/s]\n'



# Generated at 2022-06-22 13:30:01.880719
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    """
    Sanity checks for "close" method of tqdm_rich class.
    """
    from .std import __version__

    class MockTqdmReport(object):
        """
        Mock object for tqdm.std.TqdmReport.
        """
        def __init__(self):
            """
            """
            self.total = 0
            self.miniters = 0
            self.dynamic_miniters = False
            self.n = 0
            self.d = 0
            self.last_print_n = 0
            self.last_print_t = 0.0
            self.reset()

        def reset(self, *args, **kwargs):
            """
            """
            self.desc = ""
            self.unit = ""
            self.unit_scale = False

# Generated at 2022-06-22 13:30:11.726924
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test the behavior of tqdm_rich.reset()
    quick use case: tqdm_rich(total=3).reset(total=5)
    """
    from rich.progress import Progress, TimeRemainingColumn
    from rich.text import Text
    from time import time

    class FakeTask:
        """Fake Task class for testing tqdm_rich.reset()"""
        def __init__(self, total, idx):
            self.total = total
            self.idx = idx

    seconds_per_iteration = 0.1
    start_time = time()
    fake_progress = Progress(
        Text(""),
        TimeRemainingColumn()
    )

    # test 1, reset(total=3) -> total = 3, reset(total=5) -> total = 5

# Generated at 2022-06-22 13:30:22.140936
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Demonstrate that the `reset()` method actually works as intended.
    """
    from time import time as time_
    import random

    print("testing tqdm.reset()")

    bar = tqdm_rich(total=1000, leave=False)
    try:
        for _ in bar:
            bar.n += int(random.random() * 50)
            if bar.n >= bar.total:
                bar.n = bar.total
            bar.display()
            time_.sleep(0.05)
    finally:
        bar.close()

    bar = tqdm_rich(total=1000, leave=False)