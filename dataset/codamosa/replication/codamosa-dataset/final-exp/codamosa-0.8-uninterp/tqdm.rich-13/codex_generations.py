

# Generated at 2022-06-22 13:27:52.023734
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from unittest import TestCase, SkipTest
    from .utils import format_dict

    try:
        from rich.progress import Progress
    except (ImportError, AttributeError):
        raise SkipTest

    class Dummy(TestCase):
        def test_tqdm_rich_close(self):
            from .std import tqdm as std_tqdm
            from .utils import _range
            d = format_dict(unit='iB', unit_scale=True, unit_divisor=1024,
                            miniters=10, mininterval=0.1)
            with tqdm_rich(_range(100), **d) as t:
                for _ in std_tqdm([1], **d):
                    break
                t.close()
            self.assertTrue(t.closed)

    return Dummy

# Generated at 2022-06-22 13:27:53.913205
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(total=10) as t:
        t.clear()


# Generated at 2022-06-22 13:27:56.394525
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    with tqdm_rich(10) as pbar:
        pbar.close()



# Generated at 2022-06-22 13:28:04.697153
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    class test_tqdm_rich():
        def __init__(self):
            self.disable = True

        def close(self):
            print("tqdm_rich.close()")
            return super().close()

    with test_tqdm_rich() as t:
        t.close()
        class test_super():
            def close(self):
                print("super.close()")
                return super().close()

        with test_super() as t:
            t.close()



# Generated at 2022-06-22 13:28:07.081089
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    a = tqdm_rich('test')
    assert a.disable == False
    a.close()
    assert a.disable == True



# Generated at 2022-06-22 13:28:16.099952
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Unit test for method reset of class tqdm_rich
    """
    try:
        # Check if we can import the sys module before calling tqdm_rich.reset
        import sys
        reset_tqdm = tqdm_rich(total=10)
        # Check if total has been updated
        assert reset_tqdm.total == 10
        reset_tqdm.reset(total=15)
        # Check if total has been updated
        assert reset_tqdm.total == 15
    finally:
        # Prevent other tests to be impacted
        reset_tqdm.close()

# Generated at 2022-06-22 13:28:20.000819
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # method display should not violate progress bar display
    with tqdm_rich(total=1, desc="a test progress bar", leave=False) as t:
        for i in range(2):
            t.display(i)



# Generated at 2022-06-22 13:28:24.074079
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = tqdm_rich()
    task.speed = 1234567890
    assert RateColumn().render(task) == Text("~1.15 GB/s", style="progress.data.speed")



# Generated at 2022-06-22 13:28:32.097262
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import rich.console
    console = rich.console.Console()
    rate_column = RateColumn(unit="B")
    speed = rate_column.render({"speed": 1024})
    console.print(speed, end="\n")
    speed = rate_column.render({"speed": 50})
    console.print(speed, end="\n")
    speed = rate_column.render({"speed": 1})
    console.print(speed, end="\n")
    speed = rate_column.render({"speed": None})
    console.print(speed, end="\n")


# Generated at 2022-06-22 13:28:36.789751
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():  # pragma: no cover
    """This function tests the code in method 'clear' of class 'tqdm_rich'"""
    t = tqdm_rich(['a','b','c'],gui=True)
    t.close()

# Generated at 2022-06-22 13:28:44.305510
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    with patch('tqdm.rich.tqdm_rich._prog.clear') as mock_method:
        tq = tqdm_rich(total=10)
        tq.clear()
        mock_method.assert_called_once_with()

# Generated at 2022-06-22 13:28:48.189644
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    """Generate a tqdm_rich instance, close it and assert that the total of the task is 0.0"""
    tqdm_rich(1000000, desc='Test', leave=True).close()
    assert tqdm_rich(1000000, desc='Test', leave=True).total == 0.0

# Generated at 2022-06-22 13:28:52.796890
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(10, miniters=1) as t:
        for i in range(10):
            t.update(1)
            if t.n >= 5:
                t.reset(total=11)
            elif t.n > 0:
                t.reset(total=9)



# Generated at 2022-06-22 13:28:57.990500
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from sys import stdout
    from rich.console import Console
    from rich.progress import Progress
    x = tqdm_rich(range(10), file=stdout,
                  desc='Version 0 (Rich Progress)',
                  ascii=True, ncols=80, mininterval=0.1,
                  disable=False, bar_format='{l_bar}{bar}| ',
                  dynamic_ncols=True, postfix=None,
                  smoothing=0.3, bar_template='{desc}{bar}{n_fmt}/{total_fmt}')
    assert hasattr(x, '_prog')
    assert isinstance(x._prog, Progress)
    assert isinstance(x._prog._console, Console)
    assert x._prog._console._session.detach() is None
   

# Generated at 2022-06-22 13:29:08.339202
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from rich.console import Console
    from rich.progress import Progress
    from rich.table import Table
    from rich.text import Text
    from rich.markdown import Markdown
    from rich.panel import Panel
    _console = Console()
    _progress_bar = Progress(
        _console,
        Text("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        TimeElapsedColumn()
    )

    _table = Table(title='Progress Bar')
    _table.add_column("Description")
    _table.add_column("Column", justify="right")

    _table_row_1 = _table.add_row("Timed Progress Bar", _progress_bar)


# Generated at 2022-06-22 13:29:18.802534
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from time import sleep
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()
    tqdm_rich(range(10), total=10).close()

# Generated at 2022-06-22 13:29:22.192923
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    with trange(10) as t:
        for i in t:
            pass
        assert (t.close() == None)


# Generated at 2022-06-22 13:29:26.107320
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    __name__ = "tqdm_rich_clear"
    t = tqdm_rich(range(10), ascii=True, unit="it", unit_scale=True, leave=True)
    for x in t:
        pass

# Generated at 2022-06-22 13:29:36.978348
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate = RateColumn(unit="B")
    rate.render('0.5')
    rate.unit_scale = True
    rate.unit = "B"
    rate.render(500)
    rate.unit_scale = False
    rate.unit = "B"
    rate.render(500)
    rate.render(500000)
    rate.render(500000000)
    rate.render(500000000000)
    rate.render(500000000000000)
    rate.render(5000000000000000000)
    rate.render(5000000000000000000000)
    rate.render(5000000000000000000000000)
    rate.render(5000000000000000000000000000)
    rate.render(5000000000000000000000000000000)
    rate.render(5000000000000000000000000000000000)

# Generated at 2022-06-22 13:29:44.213579
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import BarColumn

    bar = BarColumn(bar_width=None)
    expected_text = "  0%|                                                                                                     |"
    assert bar.render(dict(completed=0, total=100)).text == expected_text

    t = trange(total=100)
    t.update()
    expected_text = "  2%|▊                                                                                                   |"
    assert bar.render(dict(completed=2, total=100)).text == expected_text

    t.reset(total=10)
    expected_text = "  0%|                                                                                                   |"
    assert bar.render(dict(completed=0, total=10)).text == expected_text

    t.update()

# Generated at 2022-06-22 13:30:02.045935
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from unittest import TestCase, main
    from unittest.mock import Mock
    from rich.progress import Task

    class TestRateColumn(TestCase):
        @staticmethod
        def test_none():
            progress = RateColumn()
            task = Task()
            task.speed = None
            assert progress.render(task) == Text(u'? /s', style='progress.data.speed')

        @staticmethod
        def test_not_none():
            progress = RateColumn()
            task = Task()
            task.speed = 12
            assert progress.render(task) == Text(u'12.0 /s', style='progress.data.speed')
        
        @staticmethod
        def test_specified_unit():
            progress = RateColumn(unit='B')
            task = Task()
            task.speed = 12


# Generated at 2022-06-22 13:30:11.663517
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    This function tests if the RateColumn class is working properly
    """
    from .std import tqdm as std_tqdm

    with std_tqdm(total=100) as pbar:
        pbar.update(30)
        assert(isinstance(pbar._rate_column.render(pbar), Text) is True)
        assert(pbar._rate_column.render(pbar).plain == '30.0  B/s')
        pbar.update(70)
        assert(pbar._rate_column.render(pbar).plain == '100.0  B/s')
        assert(str(pbar) == "30/100 [=============>                          ] 30.0% 100.0  B/s")


# Generated at 2022-06-22 13:30:14.889295
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    completed = f = FractionColumn()
    assert completed.render(progress_id=1, completed=1, total=10) == Text(
        '0.1/10 ', style='progress.download')

# Generated at 2022-06-22 13:30:20.106359
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    import rich
    with rich.console.render_cell(1, 1) as cell:
        with rich.live_trace(cell) as trace:
            cell.text = "Starting tqdm_rich"
            with tqdm_rich(range(10), desc="foo") as bar:
                for _ in bar:
                    bar.clear()
                    trace.writeln("clear")
                bar.display()
            cell.text = "Ending tqdm_rich"

# Generated at 2022-06-22 13:30:28.282049
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    # create new bar
    bar = tqdm_rich(total=10)
    # update the bar
    for i in range(5):
        bar.update()
    # reset the bar
    bar.reset(total=5)
    # test if bar is reset
    assert bar.n == 0
    assert bar.last_print_n == 0
    assert bar.total == 5
    # create new bar
    bar = tqdm_rich(total=10)
    # update the bar
    for i in range(5):
        bar.update()
    # reset the bar
    bar.reset()
    # test if bar is reset
    assert bar.n == 0
    assert bar.last_print_n == 0
    # test same total as before reset
    assert bar.total == 10

# Generated at 2022-06-22 13:30:40.736242
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Progress
    from tqdm.rich import FractionColumn, tqdm_rich
    with tqdm_rich(total=10, desc="Download", unit='B', unit_scale=True,
                   unit_divisor=1024, ascii=False) as bar:
        for i in range(10):
            bar.update()
    assert '0.0B/10.0KB' == FractionColumn(unit_scale=True,
                                           unit_divisor=1024).render(Progress())
    assert '0.0/10.0 KB' == FractionColumn(unit_scale=True,
                                           unit_divisor=1024).render(Progress(fill_char="#"))

# Generated at 2022-06-22 13:30:49.170470
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Test method FractionColumn.render"""
    frac_col = FractionColumn(unit_scale=True)
    assert frac_col.render(Progress().add_task('example', total=3000)) == Text('3.0/3.0 K', style='progress.download')
    assert frac_col.render(Progress().add_task('example', total=300)) == Text('0.3/0.3 K', style='progress.download')
    assert frac_col.render(Progress().add_task('example', total=30)) == Text('30/30 ', style='progress.download')

    frac_col = FractionColumn(unit_scale=False)
    assert frac_col.render(Progress().add_task('example', total=3000)) == Text('3000/3000', style='progress.download')
    assert frac

# Generated at 2022-06-22 13:30:58.215418
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    from .utils import format_sizeof, format_interval
    for x in ('foo', 'bar', 'baz', 'qux'):
        with tqdm(total=10, desc=x) as t:
            for i in range(10):
                t.update()
                time.sleep(.1)
        t.reset(total=None)
        t.reset(total=3)
        with tqdm(total=3, desc=x) as t:
            for i in range(3):
                t.update()
                time.sleep(1)

# Generated at 2022-06-22 13:31:10.556746
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from math import nan, inf

    rc = RateColumn()

    unit, suffix = filesize.pick_unit_and_suffix(2 ** 20, [""], 1)  # MB
    assert rc.render(Task(speed=2 ** 20)) == "1.0 MB/s"

    unit, suffix = filesize.pick_unit_and_suffix(2 ** 20, ["", "K", "M", "G"],
                                                 1000)  # MB
    assert rc.render(Task(speed=2 ** 20)) == "1.0 MB/s"

    unit, suffix = filesize.pick_unit_and_suffix(2 ** 20, [""], 1)
    assert rc.render(Task(speed=2 ** 20 * 1024)) == "1.0 GB/s"

    unit, suffix = filesize.pick_unit_and

# Generated at 2022-06-22 13:31:12.475952
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    tqdm_rich('').clear()

# Generated at 2022-06-22 13:31:32.094452
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    completed = '1337'
    total = '1337'
    unit = 'B'
    suffix = ''
    precision = 0
    assert FractionColumn().render(Progress(0, 1, '')).content == '0.0/1.0 '
    assert FractionColumn().render(Progress(0.999999999, 1, '')).content == '1.0/1.0 '
    assert FractionColumn().render(Progress(1337, 1337, '')).content == '1.0/1.0 '
    assert FractionColumn(unit_scale=True).render(Progress(0, 1, '')).content == '0.0/1.0 '
    assert FractionColumn(unit_scale=True).render(Progress(1337, 1337, '')).content == '1.0/1.0 K'
    assert FractionColumn

# Generated at 2022-06-22 13:31:44.996413
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import unittest
    class rateColumnUnitTest(unittest.TestCase):
        def test_RateColumn_render1(self):
            rc = RateColumn(unit="B", unit_scale=True, unit_divisor=1000)
            self.assertEqual(rc.render(0), Text("0 B/s", style="progress.data.speed"))
        def test_RateColumn_render2(self):
            rc = RateColumn(unit="B", unit_scale=False, unit_divisor=1000)
            self.assertEqual(rc.render(1000), Text("1 B/s", style="progress.data.speed"))
        def test_RateColumn_render3(self):
            rc = RateColumn(unit="B", unit_scale=True, unit_divisor=1000)
            self.assertEqual

# Generated at 2022-06-22 13:31:52.139404
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich(total=1)
    t.n = 10
    t.desc = "Progress display"
    t.total = 20
    t.display()


if __name__ == '__main__':  # pragma: no cover
    from time import sleep
    with tqdm(unit="block", unit_scale=True, total=10) as t:
        for i in range(10):
            sleep(1)
            t.update(1)

    values = ["smth", "smth2", "smth3"]
    with tqdm(values, unit="block", unit_scale=True) as t:
        t.set_description("Cool progress")
        for val in t:
            sleep(1)

    test_tqdm_rich_display()

# Generated at 2022-06-22 13:32:02.733037
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from time import sleep

    def stop_reset():
        for i in trange(100):
            sleep(0.1)
            if i == 0:
                tqdm.reset()
            if i > 5 and i < 10:
                tqdm.reset(total=0)
            if i > 20:
                tqdm.reset(total=20)

    stop_reset()

    def disable_reset():
        pbar = trange(100, disable=True)
        pbar.reset()
        pbar = trange(100, disable=True)
        pbar.reset(total=0)
        pbar = trange(100, disable=True)
        pbar.reset(total=20)

    disable_reset()



# Generated at 2022-06-22 13:32:05.128258
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .tests import tests

    tests.test_tqdm_rich_reset()

# Generated at 2022-06-22 13:32:10.507960
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import tqdm
    import time

    progress = tqdm(total=100)
    progress.set_description("test")

    try:
        while True:
            progress.update(10)
            time.sleep(1)
    except KeyboardInterrupt:
        progress.close()

# Generated at 2022-06-22 13:32:12.056429
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm(total=42) as bar:
        bar.clear()
        assert bar.n == 0

# Generated at 2022-06-22 13:32:18.786955
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    # Test for tqdm_rich.clear() raise NotImplementedError
    # add a traceback of tqdm_rich.clear()
    try:
        with tqdm_rich(total=10) as t:
            t.clear()
    except NotImplementedError as e:
        assert "'tqdm_rich' object has no attribute '_prog'" in str(e)

# Generated at 2022-06-22 13:32:20.359478
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert str(RateColumn(unit='/s').render(Progress.from_task({'speed': 5}))) == '5.0 /s'


# Generated at 2022-06-22 13:32:24.650784
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rc = RateColumn(unit_scale=True, unit_divisor=1000)
    assert rc.render(None) == '0.0 /s'
    assert rc.render(object()) == '0.0 /s'
    assert rc.render(object()) == '0.0 /s'



# Generated at 2022-06-22 13:32:36.541460
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    from tqdm.auto import tqdm as tqdm_simple
    with tqdm_simple(total=100) as pbar:
        for i in pbar:
            if i==10:
                pbar.reset(total=200)
            time.sleep(0.05)

# Generated at 2022-06-22 13:32:39.154733
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn(unit='b').render(Progress(None)) == Text("? b/s", style="progress.data.speed")

# Generated at 2022-06-22 13:32:44.341267
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # Test for the display method of the rich.progress tqdm version
    from random import random
    from time import sleep

    pbar = tqdm_rich(iterable=range(100), desc='mytest', gui=True)
    for i in pbar:
        sleep(0.1 * random())
        if i % 10 == 0:
            pbar.display()

# Generated at 2022-06-22 13:32:46.010472
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from .tests.test_gui import test_FractionColumn_render
    test_FractionColumn_render(FractionColumn)

# Generated at 2022-06-22 13:32:49.199088
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from time import sleep
    from rich.console import Console

    console = Console(file=None, color_system="ansi")
    for _ in tqdm([], total=3, file=console):
        sleep(0.000001)
        assert console.lines is not None

# Generated at 2022-06-22 13:32:52.550558
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test method reset of class tqdm_rich"""
    with tqdm_rich(total=None) as progressbar:
        progressbar.reset(total=64)
        progressbar.n = 16
        progressbar.reset(total=42)
        progressbar.n = 42
        progressbar.reset(total=0)

# Generated at 2022-06-22 13:33:04.314894
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    class task:
        def __init__(self, completed, total):
            self.completed = completed
            self.total = total

    task1 = task(20, 50)
    task2 = task(20000, 500)
    fc = FractionColumn(unit_scale=False)
    assert fc.render(task1) == Text(
        "20.0/50 0", style="progress.download")
    fc = FractionColumn(unit_scale=False, unit_divisor=1)
    assert fc.render(task1) == Text(
        "20.0/50 0", style="progress.download")
    fc = FractionColumn(unit_scale=True)
    assert fc.render(task1) == Text(
        "20.0/50 K", style="progress.download")


# Generated at 2022-06-22 13:33:14.225298
# Unit test for constructor of class tqdm_rich

# Generated at 2022-06-22 13:33:24.183974
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import ast
    from .utils import _write_file, _read_file, _pick_unused_port
    from rich.progress import Progress
    from rich.progress import FractionColumn as frac
    
    port = _pick_unused_port()
    with _write_file("test", port=port) as tmp_file:
        progress = Progress("desc", "",
                        BarColumn(),
                        FractionColumn(
                            unit_scale=False, unit_divisor=1),
                        port=port
                        )
        progress.__enter__()
        progress.update("taskid", completed=23, total=100)
        progress.__exit__()

        text = _read_file(tmp_file)

# Generated at 2022-06-22 13:33:27.572597
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rc = RateColumn("", "", "")
    assert rc.render() == Text("? /s", style="progress.data.speed")

# Generated at 2022-06-22 13:33:50.263438
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test RateColumn.render with different size units."""
    # Handle speed no set
    assert RateColumn().render(Progress.Task(speed=None)).text == "? /s"
    # Handle small speed
    assert RateColumn().render(Progress.Task(speed=12.34)).text == "12.34 /s"
    # Handle no unit with small speed
    assert RateColumn(unit="").render(Progress.Task(speed=12.34)).text == "12.34 /s"
    # Handle no unit with large speed
    assert RateColumn(unit="").render(Progress.Task(speed=1234567.89)).text == "1.23 M/s"
    # Handle unit with large speed
    assert RateColumn(unit="bps").render(Progress.Task(speed=1234567.89)).text == "1.23 Mbps"
   

# Generated at 2022-06-22 13:33:55.887879
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rc = RateColumn()
    assert rc.render(None) == '125.0 K/s'
    rc = RateColumn(unit='B')
    assert rc.render(None) == '125.0 KB/s'
    rc = RateColumn(unit_scale=False)
    assert rc.render(None) == '125.0 /s'
    rc = RateColumn(unit_scale=False, unit='B')
    assert rc.render(None) == '125.0 B/s'

# Generated at 2022-06-22 13:34:03.029839
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from datetime import datetime
    from time import sleep
    from tqdm import tqdm
    from tqdm.rich import trange
    total = 100
    for i in trange(total):
        sleep(0.1)

    for i in trange(total, mininterval=0.1):
        sleep(0.1)

    t = tqdm(total=total, mininterval=0.1)
    for i in range(total):
        sleep(0.01)
        t.update()
    t.close()
    sleep(1)



# Generated at 2022-06-22 13:34:08.564127
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    bar = tqdm_rich(range(10), desc="Test1")
    bar.n = 5
    bar.reset(total=5)
    assert bar.n == 0
    assert bar.total == 5
    assert bar._prog is not None
    assert bar._task_id is not None

# Generated at 2022-06-22 13:34:10.451908
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    tqdm_rich(0, 100, desc='test', bar_format='{desc}')



# Generated at 2022-06-22 13:34:18.359484
# Unit test for method render of class RateColumn
def test_RateColumn_render():  # pragma: no cover
    assert RateColumn().render(object) == '? /s'
    assert RateColumn(unit='B').render(object) == '? B/s'
    assert RateColumn(unit='bit').render(object) == '? bit/s'
    assert RateColumn(unit='bit', unit_scale=True).render(object) == '? bit/s'
    assert RateColumn(unit='b', unit_scale=True, unit_divisor=1024).render(object) == '? B/s'
    assert RateColumn().render(object) == '? /s'
    assert RateColumn().render(object) == '? /s'

# Generated at 2022-06-22 13:34:25.008547
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import mock
    with mock.patch("tqdm.rich._range") as mock_range:
        mock_range.return_value = [1,2,3]
        t = tqdm_rich(range(1,4))
        t.reset()
        assert t.n == 0
        assert t.total == 3
    # If a different total is passed to reset, it is used instead
    with mock.patch("tqdm.rich._range") as mock_range:
        mock_range.return_value = [1,2,3]
        t = tqdm_rich(range(1,4))
        t.reset(5)
        assert t.total == 5

# Generated at 2022-06-22 13:34:27.082155
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Test method reset of class tqdm_rich.
    """
    # Init
    with tqdm_rich(total=10) as t:
        # Reset total to 5
        t.reset(total=5)
        for i in _range(5):
            t.update(1)


# Generated at 2022-06-22 13:34:37.729491
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        import rich
    except ImportError:
        pass
    else:
        import sys
        # Initialize tqdm_rich object
        # It is done with a string so that there is no formatting in sys.stderr
        # The default values should be used

# Generated at 2022-06-22 13:34:48.326116
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(Progress(completed=20, total=100, speed=20,
                                       start_time=0)).plain == "? /s"

    assert (RateColumn(unit="B").render(Progress(completed=20, total=100, speed=20,
                                                 start_time=0)).plain
            == "20.00 B/s")

    assert (RateColumn(unit="B", unit_scale=True, unit_divisor=1000).
            render(Progress(completed=20, total=100, speed=2000,
                            start_time=0)).plain
            == "2.00 KB/s")


# Generated at 2022-06-22 13:35:06.162996
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    import pytest
    with pytest.raises(AttributeError):
        tqdm_rich().display()

# Generated at 2022-06-22 13:35:14.330444
# Unit test for method render of class RateColumn
def test_RateColumn_render():

    # For speed 1
    column = RateColumn(unit_scale=False, unit_divisor=1000)
    assert column.render({'speed': 1}) == Text("1 /s", style="progress.data.speed")

    # For speed 99999
    column = RateColumn(unit_scale=False, unit_divisor=1000)
    assert column.render({'speed': 99999}) == Text("99,999 /s", style="progress.data.speed")

    # For speed 999999
    column = RateColumn(unit_scale=False, unit_divisor=1000)
    assert column.render({'speed': 999999}) == Text("999,999 /s", style="progress.data.speed")

    # For speed 1000000
    column = RateColumn(unit_scale=False, unit_divisor=1000)
   

# Generated at 2022-06-22 13:35:18.980243
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    try:
        from rich.progress import Progress
    except ImportError:
        return
    p = Progress()
    with tqdm_rich(desc='test', progress=p) as t:
        while t.n < 5:
            t.update(1)

# Generated at 2022-06-22 13:35:29.265559
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    from rich.progress import Task
    import unittest.mock as mock

    with mock.patch.object(tqdm_rich, '_prog', new_callable=mock.PropertyMock) as mock_prog:
        with mock.patch.object(tqdm_rich, '_task_id', new_callable=mock.PropertyMock) as mock_task_id:
            mock_prog.return_value = progress = Progress()
            mock_task_id.return_value = id = progress.add_task('top-level', total=100)
            progbar = tqdm_rich(total=100)
            mock_prog.assert_called_once()
            mock_task_id.assert_called_once()
            assert isinstance(progress, Progress)


# Generated at 2022-06-22 13:35:33.883452
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    t = tqdm_rich(2, 2)

    t.reset(total=None)
    assert t.total == 2
    assert t._prog.totals[t._task_id] == 2

    t.reset(total=4)
    assert t.total == 4
    assert t._prog.totals[t._task_id] == 4

    t.close()

# Generated at 2022-06-22 13:35:34.538304
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    pass

# Generated at 2022-06-22 13:35:46.797002
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Unit test for method display of class tqdm_rich."""
    from unittest.mock import patch
    from rich.progress import Progress
    with patch.object(tqdm_rich, '_prog') as progress_mock, patch.object(Progress, 'update') as update_mock:
        progress_mock.return_value = Progress()
        tqdm_ = tqdm_rich(total=1)
        tqdm_.disable = False
        tqdm_.n = 1
        tqdm_.desc = 'test_desc'
        tqdm_.display()
        assert update_mock.called
        assert update_mock.call_count == 1
        update_mock.assert_called_once_with(0, completed=1, description='test_desc')

# Generated at 2022-06-22 13:35:58.432097
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from tqdm.auto import tqdm
    """
    Test tqdm_rich.reset()
    """
    progress = (
        "[progress.description]{task.description}"
        "[progress.percentage]{task.percentage:>4.0f}%",
        BarColumn(bar_width=None),
        FractionColumn(),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), "]")
    task = tqdm.get_instance()
    task.disable = False
    task.format_dict['unit'] = "I"
    task.format_dict['unit_scale'] = False
    task.format_dict['unit_divisor'] = 1000
    task._prog = Progress(*progress)
    task._prog.__enter__()
    task._task_id = task._pro

# Generated at 2022-06-22 13:36:01.944481
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    with tqdm(range(10)) as t:
        for i in t:
            if i == 5:
                t.reset(total=5)  # reset total iterations to 5
            elif i == 8:
                t.reset()  # reset total iterations to 10


# Generated at 2022-06-22 13:36:04.176983
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    assert rate_column.render(None) == "? /s"

# Generated at 2022-06-22 13:36:33.234226
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    r = RateColumn()
    assert r.render(task=None) == Text("? /s", style="progress.data.speed")


# Unit tests for method render of class FractionColumn

# Generated at 2022-06-22 13:36:39.934236
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # variable to store the results of unit test
    result = {}
    tc = RateColumn(unit="", unit_scale=False, unit_divisor=1000)
    result["Case1"] = tc.render(StandardError("task"))
    result["Case2"] = tc.render(
        StandardError("task"),
        speed=None)
    result["Case3"] = tc.render(
        StandardError("task"),
        speed=100)
    result["Case4"] = tc.render(
        StandardError("task"),
        speed=100000)

# Generated at 2022-06-22 13:36:50.598360
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import Progress
    import time

    with Progress() as progress:
        task = progress.add_task("task1", start=0, total=20)
        for i in tqdm(range(1, 21), progress=None):
            time.sleep(0.1)
            progress.update(task, completed=i)
        progress.reset(total=10)
        task = progress.add_task("task2", start=0, total=10)
        for i in tqdm(range(1, 11), progress=None):
            time.sleep(0.1)
            progress.update(task, completed=i)

# Generated at 2022-06-22 13:36:58.005649
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Unit test tqdm_rich.reset()
    """
    with tqdm_rich(total=10, desc="Testing reset()") as t:
        t.reset(total=100)
        for i in range(10):
            time.sleep(0.01)
            t.update()
        assert t.n == 10
        t.reset()
        for i in range(5):
            time.sleep(0.01)
            t.update()
        assert t.n == 5



# Generated at 2022-06-22 13:36:59.938831
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch  # type: ignore
    with patch.object(Progress, 'update'):
        tqdm_rich().display()

# Generated at 2022-06-22 13:37:02.725667
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=10) as pbar:
        pbar.reset(total=20)
        assert pbar.total == 20
        pbar.reset(total=30)
        assert pbar.total == 30

# Generated at 2022-06-22 13:37:08.510670
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Unit test for method render of class RateColumn.
    """
    task = tqdm(total=100, disable=True)
    task.n = 0
    task.last_print_n = 0
    task.start_t = 0
    task.last_print_t = 0
    task.total = 100
    task.smoothing = 0.5
    task.disable = True
    task.n = 10
    task.total = 100
    task.n = 0.005
    task.total = 1000
    task.n = 10
    task.total = 100
    task.n = 0.005
    task.total = 1000

# Generated at 2022-06-22 13:37:13.336452
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    import time
    with tqdm_rich(total=10, desc="test_tqdm_rich") as pbar:
        for i in range(10):
            pbar.update(1)
            time.sleep(1)


if __name__ == '__main__':
    test_tqdm_rich()

# Generated at 2022-06-22 13:37:21.058461
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    def test_reset(t, total):
        t.reset(total=total)
        return t.total

    t = trange(100)
    assert test_reset(t, total=100) == 100
    assert test_reset(t, total=50) == 50
    assert test_reset(t, total=None) is None
    assert test_reset(t, total=0) == 0

    t.close()

# Generated at 2022-06-22 13:37:26.161357
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    _task = type('task',(object,), {'completed': 12.545,
                                    'total': 1.5,
                                    'speed': 2.5})()
    _RateColumn = RateColumn()
    assert _RateColumn.render(_task) == Text('2.5 /s', style="progress.data.speed")
