

# Generated at 2022-06-22 13:27:49.685511
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from ._tqdm import TqdmTypeError, TqdmDeprecationWarning, TqdmKeyError, TqdmExperimentalWarning

    import pytest

    with pytest.raises(TqdmDeprecationWarning):
        std_tqdm.write("Testing")
    with pytest.raises(TqdmExperimentalWarning):
        tqdm.write("Testing")

    for cls in std_tqdm, tqdm_rich:
        with pytest.warns(None) as record:
            with pytest.raises(ValueError):
                cls(0, ascii=True)
        assert len(record) == 1

# Generated at 2022-06-22 13:27:52.959769
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    try:
        tqdm_rich(range(10), ascii=True).close()
    except Exception as e:
        raise Exception("tqdm_rich close failed") from e


# Generated at 2022-06-22 13:27:59.057816
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Task
    task = Task(description="Test", completed=1, total=2)
    assert task.description == "Test"
    assert task.completed == 1
    assert task.total == 2
    assert FractionColumn().render(task) == Text(
        "0.5/2 ", style="progress.download")
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(task) == Text(
        "0.5/2 ", style="progress.download")
    # decimal with unit_scale=True
    task_decimal = Task(description="Test_decimal", completed=1000, total=4000)
    assert task_decimal.description == "Test_decimal"
    assert task_decimal.completed == 1000
    assert task_decimal.total == 4000
   

# Generated at 2022-06-22 13:28:04.914488
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test tqdm._main_loop with tqdm_rich.display as _instantiate_default"""
    self = tqdm_rich(desc='display', total=10, leave=True)
    self.display()
    self.refresh()
    # TODO: check if the text was written to the terminal!

# Generated at 2022-06-22 13:28:07.708765
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    def test():
        pbar = tqdm(xrange(10))
        for j in range(10):
            pbar.update(1)
    test()

# Generated at 2022-06-22 13:28:11.587628
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    a = tqdm_rich(total=5)
    assert a.n == 0
    assert a.total == 5
    a.reset(total=10)
    assert a.n == 0
    assert a.total == 10

# Generated at 2022-06-22 13:28:15.679482
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=3, desc='Method reset of class tqdm_rich') as progress:
        progress.update()
        progress.update()
        progress.reset()
        progress.update()
        progress.update()
        progress.update()

# Generated at 2022-06-22 13:28:17.800123
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    for _ in tqdm(["a", "b", "c"], desc="test"):
        pass

# Generated at 2022-06-22 13:28:20.579435
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    tasks = [
        {'completed': 0, 'total': 0, 'expected': '0.0/0.0'},
        {'completed': 0, 'total': 10, 'expected': '0.0/10.0'},
        {'completed': 10, 'total': 0, 'expected': '0.0/0.0'},
        {'completed': 50, 'total': 100.3, 'expected': '50.0/100.3'},
    ]
    for task in tasks:
        assert FractionColumn().render(task) == task['expected']



# Generated at 2022-06-22 13:28:24.527952
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="/s", unit_scale=False, unit_divisor=1000)
    assert rate_column.render(10, None, None) == "10.0 /s"

# Generated at 2022-06-22 13:28:40.225154
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    class FakeTask:
        """A fake task to test `RateColumn.render`."""
        def __init__(self, completed, total, speed):
            self.completed = completed
            self.total = total
            self.speed = speed

    task = FakeTask(completed=1024, total=3 * 1000 * 1000 * 1000, speed=1024 * 1024 * 1024 * 8 * 3 * 1000 * 1000 * 1000)
    assert FractionColumn(unit_scale=True).render(task) == Text('0.00 GB/3.00 TB', style='progress.download')
    assert RateColumn(unit='b', unit_scale=True).render(task) == Text('2.56 Yb/s', style='progress.data.speed')

# Generated at 2022-06-22 13:28:50.671592
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.progress import Progress
    from rich.progress import task as task_
    import sys
    import unittest
    import unittest.mock

    class tqdm_rich_display(unittest.TestCase):
        @unittest.mock.patch.object(sys, 'stderr', new_callable=unittest.mock.StringIO)
        def test_tqdm_rich_display(mock_stderr):
            progress = Progress()
            progress.add_task(task_.Task("Task 2", total=10))
            progress.add_task(task_.Task("Task 1", total=10))
            progress.add_task(task_.Task("Task 3", total=10))

# Generated at 2022-06-22 13:28:52.577146
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    tqdm_rich().close()
    tqdm_rich(disable=True).close()

# Generated at 2022-06-22 13:28:55.035602
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    # Create an instance of class tqdm_rich
    t = tqdm_rich(total=2)
    # Reset before iterating
    t.reset()
    # Iterate over the instance
    t.update(1)
    time.sleep(0.1)
    t.update(1)

# Generated at 2022-06-22 13:29:06.631779
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = ProgressColumn()
    task.progress = Progress()
    task.time_last = 1
    task.time_elapsed = 1
    task.completed = 1
    task.total = 1
    task.speed = None

    assert RateColumn().render(task)._text == "? /s"
    assert RateColumn(unit="B").render(task)._text == "? B/s"
    assert RateColumn(unit_scale=True).render(task)._text == "? B/s"
    assert RateColumn(unit_scale=True, unit_divisor=1024).render(task)._text == "? B/s"
    task.speed = 1024 + 1
    assert RateColumn(unit_scale=True).render(task)._text == "1.0 K/s"

# Generated at 2022-06-22 13:29:14.580630
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import rich.progress

    text = ""

    def mock_print_text(text_to_print, **_):
        nonlocal text
        text += text_to_print

    rich.progress.print_text = mock_print_text

    tqdm_rich(total=100)

    assert text == "[progress] 0% | |\n"

    tqdm_rich.reset(total=1000)

    assert text == "[progress] 0% | | 0/1000\n"

# Generated at 2022-06-22 13:29:26.441359
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    ratecolumn = RateColumn(unit = "b", unit_scale = False, unit_divisor=1000)
    assert ratecolumn.render(None) == Text("? b/s", style="progress.data.speed")

    ratecolumn = RateColumn(unit = "b", unit_scale = False, unit_divisor=1000)
    assert ratecolumn.render(0) == Text("? b/s", style="progress.data.speed")

    ratecolumn = RateColumn(unit = "b", unit_scale = False, unit_divisor=1000)
    assert ratecolumn.render(999) == Text("999 b/s", style="progress.data.speed")

    ratecolumn = RateColumn(unit = "b", unit_scale = False, unit_divisor=1000)

# Generated at 2022-06-22 13:29:33.831371
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    progress = Progress()
    progress.add_task("task 1", total=10)
    progress.add_task("task 2", total=2)
    task = tqdm_rich(range(10), leave=True, progress=progress)
    task.reset(total=2)
    task.close()
    task.clear()


if __name__ == "__main__":
    from unittest import main
    main()

# Generated at 2022-06-22 13:29:36.625365
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    tqdm_instance = tqdm_rich(total=1)
    tqdm_instance.clear()
    tqdm_instance.close()

# Generated at 2022-06-22 13:29:41.141585
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from .tqdm import trange
    from .utils import format_sizeof
    import sys
    import time

    range_iterator = trange(100, desc='test_tqdm_rich_clear')

    for i in range_iterator:
        time.sleep(0.01)
        # Reset to 0
        range_iterator.reset()
        # Clear
        range_iterator.clear()

# Generated at 2022-06-22 13:29:51.293921
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm(total=1000) as t:
        for i in range(50):
            t.update(i)
            t.set_description("%s" % i)
            t.set_postfix({"postfix": i})

# Generated at 2022-06-22 13:29:53.447024
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    pbar = tqdm(total=10, disable=True)
    pbar.clear()
    pbar.close()


# Generated at 2022-06-22 13:29:57.711338
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time

    with tqdm_rich(total=100, leave=False) as progress_bar:
        for i in range(100):
            progress_bar.update(1)
            time.sleep(0.01)
            if i % 10 == 0:
                progress_bar.reset(total=100 * (i + 1))

# Generated at 2022-06-22 13:30:09.354459
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.console import Console
    from rich.progress import Progress, BarColumn
    from rich.progress import TimeElapsedColumn, TimeRemainingColumn, RateColumn
    from rich.progress import filesize
    progress = Progress(
        "[progress.description]{task.description}"
        "[progress.percentage]{task.percentage:>4.0f}%",
        BarColumn(bar_width=None),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(),
        ",", RateColumn(), "]"
    )
    console = Console()
    console.print(progress)
    task_id = progress.add_task("Test", total=1024)
    progress.update(task_id, completed=1024, description="Test")

# Generated at 2022-06-22 13:30:19.284956
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Test method tqdm_rich.reset
    """
    from rich.console import Console
    from rich.progress import Progress

    console = Console()
    progress = Progress()
    task = progress.add_task("[red]Test")

    i = 0
    running = True
    while running:
        progress.update(task, completed=i)
        i += 1
        progress.update(task, completed=i)
        if i == 10:
            progress.update(task, completed=i)
            progress.reset()
            progress.update(task, completed=i)

        if i > 10:
            running = False

    progress.__exit__(None, None, None)
    console.print(progress.render())

# Generated at 2022-06-22 13:30:25.911660
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    Method render
    """
    completed = 100
    total = 1000
    unit = 1
    unit_scale = False
    unit_divisor = 1000
    precision = 0
    file_size = f"{completed/unit:,.{precision}f}/{total/unit:,.{precision}f} "
    test = Text(
        file_size,
        style="progress.download")
    assert test == FractionColumn(unit_scale, unit_divisor).render(completed, total)


# Generated at 2022-06-22 13:30:31.806985
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    does the reset method of tqdm_rich work?
    """
    from tqdm.auto import tqdm
    from tqdm.utils import _term_move_up
    bars = []
    total = 10
    for i in tqdm(range(total)):  # create bars
        bars.append(tqdm(total=total))
    for i in range(total):
        bars[i].reset()  # resets to 0 iterations for repeated use
        bars[i].set_description("descr")
        bars[i].update()
        assert bars[i].desc == "descr"
        assert bars[i].n == 0
        assert bars[i].last_print_n == 0
        assert bars[i].dynamic_ncols == 0

# Generated at 2022-06-22 13:30:43.583861
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    r = RateColumn(unit_scale=True).render
    assert r(Progress(total=1000, completed=1000, speed=0.01)) == "0.001 Ks/s"
    assert r(Progress(total=1000, completed=1000, speed=1333.333)) == "1.333 Ms/s"
    assert r(Progress(total=1000, completed=1000, speed=1333333)) == "1.333 Gs/s"
    assert r(Progress(total=1000, completed=1000, speed=1333333000)) == "1.333 Ts/s"
    assert r(Progress(total=1000, completed=1000, speed=1333333000000)) == "1.333 Ps/s"

# Generated at 2022-06-22 13:30:53.253964
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Test method reset of class tqdm_rich.
    """
    # reset() is called on a tqdm_rich instance with default arg
    progress_bar = tqdm_rich(list(range(10)), total=10)
    progress_bar.reset()
    assert progress_bar._prog.total == None

    # reset() is called on a tqdm_rich instance with arg total=50
    progress_bar = tqdm_rich(list(range(50)), total=10)
    progress_bar.reset(50)
    assert progress_bar._prog.total == 50

# Generated at 2022-06-22 13:31:02.031635
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = {'completed': 2000, 'total': 2300}
    assert FractionColumn().render(task) == Text("2.0/2.3 G", style='progress.download')
    assert FractionColumn(unit_divisor=1024).render(task) == Text("1.9/2.2 G", style='progress.download')
    assert FractionColumn(unit_divisor=1).render(task) == Text("2,000/2,300 ", style='progress.download')
    assert FractionColumn(unit_scale=False).render(task) == Text("2,000/2,300", style='progress.download')
    assert FractionColumn(unit_scale=False, unit_divisor=1024).render(task) == Text("2,000/2,300", style='progress.download')
    assert Fraction

# Generated at 2022-06-22 13:31:14.617499
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    c = RateColumn()
    assert c.render(object()) == Text("? B/s", style="progress.data.speed")
    c.unit_scale = True
    assert c.render(object()) == Text("? B/s", style="progress.data.speed")
    c.unit_scale = False
    assert c.render(object()) == Text("? B/s", style="progress.data.speed")
    task = object()
    task.speed = 0
    assert c.render(task) == Text("0.0 B/s", style="progress.data.speed")
    task.speed = 0.30
    assert c.render(task) == Text("0.3 B/s", style="progress.data.speed")
    task.speed = 999

# Generated at 2022-06-22 13:31:26.819615
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="B", unit_scale=False, unit_divisor=1000)
    rate = rate_column.render(0)
    assert rate == Text("0.0 B/s", style="progress.data.speed")
    rate = rate_column.render(100)
    assert rate == Text("100.0 B/s", style="progress.data.speed")
    rate = rate_column.render(1000)
    assert rate == Text("1,000.0 B/s", style="progress.data.speed")
    rate = rate_column.render(1000000)
    assert rate == Text("1,000,000.0 B/s", style="progress.data.speed")
    rate = rate_column.render(speed=None)

# Generated at 2022-06-22 13:31:28.968267
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    with tqdm_rich(total=100, smoothing=1) as pbar:
        for i in range(100):
            pbar.display()
            pbar.update(1)
    assert pbar._prog.completed == pbar.n

# Generated at 2022-06-22 13:31:38.225227
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from time import sleep
    from rich.progress import Progress, Text
    from rich.panel import Panel
    from rich.repr import Repr
    from rich.table import Column, Table
    from rich.console import Console
    from rich.markup import Markup
    from rich.markdown import Markdown
    from rich.style import Style
    console = Console()
    t = tqdm_rich(range(10), total=10, desc="Sample tqdm", bar_format="{desc}: {percentage:3.0f}%|{bar}| "
                                                                        "{n_fmt}/{total_fmt}")
    sleep(2)
    total = 100
    t.reset(total=total)
    for i in t:
        sleep(0.1)
    drepr = Repr()
   

# Generated at 2022-06-22 13:31:43.905010
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from time import sleep
    with tqdm_rich(total=11) as bar:
        for i in range(10):
            bar.update(1)
            sleep(0.01)
    with tqdm_rich(total=21) as bar:
        for i in range(20):
            bar.update(1)
            sleep(0.01)

# Generated at 2022-06-22 13:31:48.961921
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    try:
        import rich.progress  # NOQA
    except ImportError:
        pass
    else:
        with tqdm_rich(10, bar_format="* * * * * *") as t:
            for _ in _range(3):
                t.reset(total=5)
                for i in _range(5):
                    t.update(2)
                    t.set_description("Reset: {}".format(i))
                t.reset()

# Generated at 2022-06-22 13:31:54.374471
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # Test with speed > 1
    task = std_tqdm(total=100, postfix={"n_fmt": "%.1f", "speed":20.5, "unit": "B"})
    task.n = 20
    task.refresh()
    assert RateColumn().render(task).text == "20.5 B/s"

    # Test with speed < 1
    task.postfix['speed'] = 0.5
    task.refresh()
    assert RateColumn().render(task).text == "0.5 B/s"

    # Test with speed = None
    task.postfix = {"speed": None}
    task.refresh()
    assert RateColumn().render(task).text == "? B/s"

    # Test with unit_scale = True
    task.postfix['speed'] = 120
   

# Generated at 2022-06-22 13:32:00.161120
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import unittest

    class RateColumnTest(unittest.TestCase):
        def setUp(self):
            self.rateColumn = RateColumn(
                unit="",
                unit_scale=False,
                unit_divisor=1000
            )
            self.MockTask = CreateMockTask()

        def test_unit_is_not_blank(self):
            self.rateColumn.unit = "B"
            self.assertEqual(self.rateColumn.unit, "B")

        def test_unit_scale_is_false(self):
            self.rateColumn.unit_scale = False
            self.assertEqual(self.rateColumn.unit_scale, False)

        def test_unit_divisor_is_1000(self):
            self.rateColumn.unit_divisor = 1000
           

# Generated at 2022-06-22 13:32:12.814397
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    # pylint: disable=protected-access
    # pylint: disable=missing-docstring

    for cls in (tqdm_rich, std_tqdm):
        # test bool(tqdm(..., disable=None))
        assert bool(cls(disable=None))
        # test bool(tqdm(..., disable=False))
        assert bool(cls(disable=False))
        # test bool(tqdm(..., disable=True))
        assert not bool(cls(disable=True))

        # test total=inf
        assert cls(total=float('inf')).total == float('inf')
        # test bar_format with %i and %s

# Generated at 2022-06-22 13:32:14.499815
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rc = RateColumn()
    assert rc.render(None) == '? /s'

# Generated at 2022-06-22 13:32:34.283535
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import pytest
    from collections import namedtuple
    from .tqdm import bar_format
    Task = namedtuple('Task', ['completed', 'total', 'bar_format'])

# Generated at 2022-06-22 13:32:44.797634
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from os import getpid
    from time import time
    from threading import Thread
    def some_work(x):
        prog.update(thread_id, completed=x)
    start_time = time()
    prog = Progress("[progress.description]{task.description}")
    thread_id = prog.add_task("Loading")
    work_thread = Thread(target=some_work, args=(5,))
    work_thread.daemon = True
    work_thread.start()
    while work_thread.is_alive():
        prog.update(thread_id, description="Loading %d" % getpid())
        if time() - start_time >= 1:
            prog.reset(10)
            start_time = time()

if __name__ == "__main__":
    test_tqdm_rich

# Generated at 2022-06-22 13:32:52.794514
# Unit test for method render of class RateColumn

# Generated at 2022-06-22 13:33:00.944516
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from unittest import TestCase, mock

    # noinspection PyProtectedMember
    class TqdmRichDisplayTest(TestCase):
        def setUp(self):
            self.pbar = tqdm_rich("Loading data", max_value=20)
            self.pbar.reset = mock.MagicMock()

        def test_display_updates_pbar(self):
            self.pbar.display()
            self.pbar.reset.assert_called()

    TqdmRichDisplayTest().test_display_updates_pbar()

# Generated at 2022-06-22 13:33:05.478178
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = None
    c = RateColumn(unit_scale=False, unit_divisor=1000)
    print(c.render(task))
    c = RateColumn(unit="b", unit_scale=True, unit_divisor=1000)
    print(c.render(task))



# Generated at 2022-06-22 13:33:09.978867
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Assert that RateColumn renders the correct string."""
    r = RateColumn(unit="B", unit_scale=True, unit_divisor=1000)
    task = {"speed":100.0, "total":100.0, "completed":100.0, "eta":0}
    assert r.render(task) == Text("100 B/s", style="progress.data.speed")


# Generated at 2022-06-22 13:33:13.447125
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = trange(10, ascii=True)
    progress_column = RateColumn('b')
    progress_column.render(task)

# Generated at 2022-06-22 13:33:23.979377
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    """1. test `reset` method: creating a progress bar with total=100, complete
       it to 80 and reset it.
    """
    from rich.progress import Progress
    from rich import print
    import time

    progress = Progress(f"{'[progress.description]{task.description}':<25}", "[progress.percentage]{task.percentage:>4.0f}%",
                        BarColumn(bar_width=None),
                        FractionColumn(),
                        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), "]")
    progress.__enter__()

    task_id = progress.add_task("Test reset method of class tqdm_rich",
                                total=100.0)
    old_task = progress.get_task(task_id)
    # updating...

# Generated at 2022-06-22 13:33:35.277059
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    import random

    def tqdm_test(t, desc=None):
        with tqdm_rich(total=t, desc=desc) as pbar:
            for i in range(t):
                time.sleep(1e-6 * random.randint(1, 1e5))
                pbar.update()

    for _ in range(5):
        tqdm_test(5)
        tqdm_test(10)
        tqdm_test(5, "Foo")
        tqdm_test(15, "Bar")
        tqdm_test(10, "Baz")
        tqdm_test(15, "Foo")
        tqdm_test(10, "Bar")
        tqdm_test(15, "Baz")
        tqdm_test

# Generated at 2022-06-22 13:33:40.307698
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Unit test for method display of class tqdm_rich."""
    with tqdm_rich(total=10) as t:
        for i in range(10):
            t.update()
            time.sleep(0.1)
        time.sleep(0.1)
    assert t.n == 10

# Generated at 2022-06-22 13:34:10.167366
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """ Test method tqdm_rich.reset() """
    # Test with simple reset
    with tqdm_rich(total=50) as pbar:
        for _ in range(20):
            pbar.update()
        pbar.reset()
    # Test with wrong reset in terms of total
    with tqdm_rich(total=50) as pbar:
        for _ in range(20):
            pbar.update()
        pbar.reset(total=80)
    # Test with wrong reset in terms of total
    with tqdm_rich(total=50) as pbar:
        for _ in range(20):
            pbar.update()
        pbar.reset(total=20)

# Generated at 2022-06-22 13:34:20.061678
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    def assert_equal(actual, expected):
        assert actual == expected, f"\n{actual}\n!=\n{expected}"

    speed = 12345
    unit = "Mi"
    suffix = "B"
    precision = 1
    expected = f"12.3 {suffix}{unit}/s"
    assert_equal(expected, RateColumn("Mi", unit_scale=True, unit_divisor=1024).render(speed))
    assert_equal(expected, RateColumn("Mi", unit_scale=True).render(speed))
    expected = f"12.3 {suffix}{unit}/s"
    assert_equal(expected, RateColumn("Mi", unit_scale=False).render(speed))
    expected = f"12.3 {suffix}{unit}/s"

# Generated at 2022-06-22 13:34:31.476788
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = {
        "description": "Downloading",
        "completed": 750,
        "total": 1024
    }
    test_cases = {
        (False, 1): Text("0.73/1.00", style="progress.download"),
        (True, 1): Text("0.7/1.0 B", style="progress.download"),
        (True, 103): Text("0.7/1.0 KiB", style="progress.download"),
        (True, 1000): Text("0.7/1.0 k", style="progress.download"),
        (True, 1000000): Text("0.7/1.0 M", style="progress.download"),
        (True, 1000000000): Text("0.7/1.0 G", style="progress.download")
    }

# Generated at 2022-06-22 13:34:37.227011
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich import progress
    from rich.table import Column
    progress.FractionColumn(unit_scale=False, unit_divisor=1)
    progress.Column.FractionColumn(unit_scale=False, unit_divisor=1)
    Column.FractionColumn(unit_scale=False, unit_divisor=1)
    # following line is only used to make pyflakes happy
    Column.__module__

# Generated at 2022-06-22 13:34:40.231250
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = Progress(total=100, completed=10)
    result = RateColumn(unit_scale=True, unit_divisor=1000).render(task)
    assert result.text == "0.0 B/s"

# Generated at 2022-06-22 13:34:47.921697
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from unittest.mock import Mock
    from datetime import datetime
    task = Mock()
    task.completed = 10
    task.total = 100
    task.start_t = datetime.utcnow()
    task.last_print_t = task.start_t
    task.speed = 10
    rate_column = RateColumn(unit="", unit_scale=False, unit_divisor=1000)
    assert rate_column.render(task) == Text("10.0 /s", style="progress.data.speed")

# Generated at 2022-06-22 13:34:57.484150
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    >>> from tqdm.rich import tqdm
    >>> pbar = tqdm(total=100, unit_scale=True)
    >>> def get_total_length(task):
    ...     return len(FractionColumn().render(task))
    >>> assert get_total_length(pbar) == len(pbar.__repr__())
    >>> pbar.update(50)
    >>> assert get_total_length(pbar) == len(pbar.__repr__())
    >>> for _ in range(51):
    ...     pbar.update()
    >>> assert get_total_length(pbar) == len(pbar.__repr__())
    """
    pass

# Generated at 2022-06-22 13:34:59.537717
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    x = tqdm_rich(range(10))
    x.reset(total=10)
    assert x.total is not None

# Generated at 2022-06-22 13:35:11.008005
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Test unit for 'render' method of RateColumn class
    """
    class task:
        """
        Mock object of a task class
        """
        def __init__(self, speed):
            self.speed = speed
    ratecolumn = RateColumn()
    # If speed is not None, check if the text returned is correct
    assert ratecolumn.render(task(10)) == Text("10 /s", style="progress.data.speed")
    assert ratecolumn.render(task(10.4)) == Text("10.4 /s", style="progress.data.speed")
    # If speed is None, check if the text returned is correct
    assert ratecolumn.render(task(None)) == Text("? /s", style="progress.data.speed")
    ratecolumn = RateColumn(unit="B")

# Generated at 2022-06-22 13:35:21.546777
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import unittest
    from unittest.mock import Mock

    class TestTask(Mock):
        def __init__(self):
            super().__init__()
            self.speed = None

    task = TestTask()
    task.speed = None
    test_1 = RateColumn()
    assert test_1.render(task) == Text(f"? /s", style="progress.data.speed")

    task.speed = 10
    test_2 = RateColumn("B")
    assert test_2.render(task) == Text(f"10.000 B/s", style="progress.data.speed")

    task.speed = 970
    test_3 = RateColumn("B", unit_scale=False)

# Generated at 2022-06-22 13:36:21.145799
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn("s")
    assert rate_column.render(rate_column).content == "? s/s"
    rate_column.unit_scale = True
    task = object()
    task.speed = 1000
    assert rate_column.render(task).content == "1.0 Ks/s"
    task.speed = 1000 * 1000
    assert rate_column.render(task).content == "1.0 Ms/s"
    task.speed = 1000 * 1000 * 1000
    assert rate_column.render(task).content == "1.0 Gs/s"
    task.speed = 1000 * 1000 * 1000 * 1000
    assert rate_column.render(task).content == "1.0 Ts/s"
    task.speed = 1000 * 1000 * 1000 * 1000 * 1000

# Generated at 2022-06-22 13:36:24.591241
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from time import sleep
    pbar = tqdm_rich(total=100)
    for _ in range(10):
        pbar.update(10)
        sleep(0.01)
    pbar.close()

# Generated at 2022-06-22 13:36:36.342566
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column_1 = RateColumn("/s")
    rate_column_2 = RateColumn("/s", unit_scale=True)
    for rate_column in [rate_column_1, rate_column_2]:
        rate_column.render(tqdm({'speed': 0, 'total': 0, 'completed': 0, 'description': "0/0"}))
        rate_column.render(tqdm({'speed': 1024, 'total': 0, 'completed': 0, 'description': "0/0"}))
        rate_column.render(tqdm({'speed': 2048, 'total': 0, 'completed': 0, 'description': "0/0"}))

# Generated at 2022-06-22 13:36:40.556083
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    with tqdm_rich(reset=True, total=10, desc="Test") as pbar:
        for _ in range(6):
            pbar.update(1)
            time.sleep(0.1)
        pbar.reset(total=5)
        for _ in range(5):
            pbar.update(1)
            time.sleep(0.1)

# Generated at 2022-06-22 13:36:50.638418
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    total = 1_800_000
    completed = 1_000_000
    speed = 100
    unit_scale = True
    unit_divisor = 1_024
    unit = 'B'

    progress_column = RateColumn(unit, unit_scale, unit_divisor)
    bytes_per_second = filesize.human_readable_bytes_per_second(speed, unit, unit_scale, unit_divisor)
    task = tqdm_rich.Task(total, completed, speed, "")

    assert(progress_column.render(task).text == f"{bytes_per_second}/s")

# Generated at 2022-06-22 13:36:57.277322
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test method render of class RateColumn."""
    class FakeProgressColumn:
        """Simulates the class ProgressColumn from rich.progress."""
        def __init__(self, speed):
            self.speed = speed

    for speed in [None, 1000, 1000 * 60]:
        fake_progress_column = FakeProgressColumn(speed)
        rate_column = RateColumn(unit_scale=True)
        rate_column.render(fake_progress_column)

# Generated at 2022-06-22 13:37:04.131851
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    import sys
    tt = tqdm(total=100)
    tt.display()
    time.sleep(0.1)
    tt.reset(total=50)
    tt.display()
    time.sleep(0.1)
    tt.reset()
    tt.display()
    time.sleep(0.1)
    # For tqdm progress bar is not clear
    # test_tqdm_rich_reset()
    if 'tqdm.tests' in sys.modules:
        print('delete progress bar')

# Generated at 2022-06-22 13:37:15.161289
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Test to check that method render of object RateColumn returns
    the appropriate string for a given speed.
    """
    assert RateColumn(unit="", unit_scale=False, unit_divisor=1000).render({"speed": 512}) == "512.0 /s"
    assert RateColumn(unit="", unit_scale=False, unit_divisor=1000).render({"speed": 1024}) == "1.0 K/s"
    assert RateColumn(unit="", unit_scale=False, unit_divisor=1000).render({"speed": 2048}) == "2.0 K/s"
    assert RateColumn(unit="", unit_scale=False, unit_divisor=1000).render({"speed": 2097152}) == "2.0 M/s"

# Generated at 2022-06-22 13:37:23.236061
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    msg = "0.5/2.3 G"
    completed = 2.3
    total = 0.5
    unit_scale = False
    unit_divisor = 1000
    fc = FractionColumn(unit_scale, unit_divisor)
    assert fc.render(completed, total) == msg
    unit_scale = True
    fc = FractionColumn(unit_scale, unit_divisor)
    assert fc.render(completed, total) == msg


# Generated at 2022-06-22 13:37:34.788387
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    assert rate_column.render({"speed": 1}) == "[bold blue]1[/bold blue] [blue]B/s[/blue]"
    assert rate_column.render({"speed": 1024}) == "[bold blue]1.0[/bold blue] [blue]K/s[/blue]"
    assert rate_column.render({"speed": 1048576}) == "[bold blue]1.0[/bold blue] [blue]M/s[/blue]"
    assert rate_column.render({"speed": 1073741824}) == "[bold blue]1.0[/bold blue] [blue]G/s[/blue]"
    assert rate_column.render({"speed": 1099511627776}) == "[bold blue]1.0[/bold blue] [blue]T/s[/blue]"