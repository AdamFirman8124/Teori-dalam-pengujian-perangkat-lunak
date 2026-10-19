

# Generated at 2022-06-22 13:27:52.994892
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn(unit="B").render(std_tqdm(total=1)) == Text("1.00 B/s", style="progress.data.speed")
    assert RateColumn(unit="B", unit_scale=True).render(std_tqdm(total=1)) == Text("1 B/s", style="progress.data.speed")
    assert RateColumn(unit="B", unit_scale=True, unit_divisor=1024).render(std_tqdm(total=1)) == Text("1 B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:27:58.817303
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from trange import trange
    from time import sleep
    for i in trange(4, position=0):
        assert i in range(4), "iterator should range from 0 to 3"
        sleep(0.5)
    for i in trange(4, position=0):
        assert i in range(4), "iterator should range from 0 to 3"
        sleep(0.5)

# Generated at 2022-06-22 13:28:11.327402
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import Progress as RichProgress
    from unittest.mock import Call, Mock, patch

    # Mock rich.progress.Progress to check that the total iterations
    # given to the reset method is correctly passed to the wrapped
    # rich.progress.Progress instance.
    with patch.object(RichProgress, 'reset') as patch_reset:
        mock_reset = Mock(wraps=patch_reset)
        patch_reset.return_value = mock_reset
        with patch.object(RichProgress, '__enter__'):
            with patch.object(RichProgress, '__exit__'):
                t = tqdm.tqdm(total=1000)
                t.reset(total=500)
                assert mock_reset.call_args_list == [
                                                     Call(total=500)
                                                    ]

# Generated at 2022-06-22 13:28:23.879906
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Unit test for `rich.progress.FractionColumn.render()`."""
    class Task:
        total = 1048576
        completed = 524288

    test_cases = [
        (FractionColumn(), True, False, "5.0/10.0 M"),
        (FractionColumn(), False, False, "524.3/1024.0 k"),
        (FractionColumn(), True, True, "5.0/10.0 MB"),
        (FractionColumn(), False, True, "524.3/1024.0 KB"),
    ]

    for test_case in test_cases:
        column = test_case[0]
        column.unit_scale = test_case[1]
        column.unit_divisor = test_case[2] + 1 if test_case[2] else 1

# Generated at 2022-06-22 13:28:26.673852
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    task = trange(0, 100, 0.001)
    task.display()
    task.update(45)
    rate_column.render(task)
    task.close()



# Generated at 2022-06-22 13:28:34.543734
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    r = RateColumn()
    assert r.render({'speed': None}) == Text('? /s', style='progress.data.speed')

    for speed in range(100, 1010, 100):
        assert r.render({'speed': speed}) == Text('100.0 /s', style='progress.data.speed')

    for speed in range(1000, 10000, 1000):
        assert r.render({'speed': speed}) == Text('1.0 K/s', style='progress.data.speed')

    r.unit_scale = True
    r.unit_divisor = 1024
    assert r.render({'speed': 1000}) == Text('0.98 K/s', style='progress.data.speed')

# Generated at 2022-06-22 13:28:44.150456
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import sys
    import os
    sys.modules['rich'] = os.environ.get("TEST_RICH_BACKEND", "curtsies")
    global tqdm_rich
    from .rich import tqdm_rich
    d = tqdm_rich(total=3, desc='test_tqdm_rich_display')
    assert d.total == 3, 'total default not 3'
    d.refresh()
    d.display()
    d.refresh()
    d.update()
    d.display()
    d.update()
    d.display()
    d.update()
    d.display()
    d.close()

# Generated at 2022-06-22 13:28:47.978042
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .tests import pretest_posttest
    from .utils import TStr

    pretest_posttest(
        lambda: hasattr(tqdm_rich, 'display'),
        lambda: tqdm_rich.display(),
        test=lambda: isinstance(tqdm_rich.display(), TStr))

# Generated at 2022-06-22 13:28:49.860646
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(total=1) as pbar:
        pbar.update(1)
        pbar.clear()

# Generated at 2022-06-22 13:28:57.872047
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rc = RateColumn(unit='B', unit_scale=False)
    assert rc.render({'speed': 100}) == '100 B/s'

    rc = RateColumn(unit='B', unit_scale=True)
    assert rc.render({'speed': 100}) == '100 B/s'
    assert rc.render({'speed': 2000}) == '2.0 KB/s'
    assert rc.render({'speed': 1000000}) == '1.0 MB/s'

    rc = RateColumn(unit='B', unit_scale=True, unit_divisor=1024)
    assert rc.render({'speed': 100}) == '100 B/s'
    assert rc.render({'speed': 2000}) == '1.95 KB/s'

# Generated at 2022-06-22 13:29:03.601319
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(Progress.Task()) == Text("? /s", style="progress.data.speed")


# Generated at 2022-06-22 13:29:07.373008
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = Progress.Task(completed=0, total=1e3)
    column = FractionColumn()
    # without unit convertion
    assert column.render(task) == Text("0.0/1.0 ", style="progress.download")
    task.completed = 1e3
    assert column.render(task) == Text("1.0/1.0 ", style="progress.download")
    # with unit convertion
    column = FractionColumn(unit_scale=True)
    assert column.render(task) == Text("1.0/1.0 K", style="progress.download")
    task.completed = 1e6
    assert column.render(task) == Text("1.0/1.0 M", style="progress.download")


# Generated at 2022-06-22 13:29:14.796847
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import unittest

    class TestRateColumnRender(unittest.TestCase):
        def setUp(self):
            self.dummy = RateColumn()

        def test_render(self):
            answer = self.dummy.render({'speed': 10})
            self.assertEqual(answer.style, 'progress.data.speed')
            self.assertEqual(answer.text, '10.0 /s')

    unittest.main()

# Generated at 2022-06-22 13:29:26.735988
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():

    from unittest.mock import patch

    from rich.progress import Progress

    def check_fraction(task, completed, total, unit, suffix, precision):
        task.completed = completed
        task.total = total
        FractionColumn(unit_scale=True, unit_divisor=10).render(task)
        assert(task._progress.markup == f'{completed/unit:,.{precision}f}/{total/unit:,.{precision}f} {suffix}')

    def check_fraction_with_zero_completed(task, completed, total, unit, suffix, precision):
        task.completed = completed
        task.total = total
        FractionColumn(unit_scale=True, unit_divisor=10).render(task)

# Generated at 2022-06-22 13:29:29.279865
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    column = FractionColumn()
    task = object()
    task.completed = 1
    task.total = 2
    task.description = "description"
    description = Text("description")
    assert column.render(task) == Text("0.5/2 [description]", style="progress.download")
    assert column.render(task) == Text("0.5/2 description", style="progress.download")


# Generated at 2022-06-22 13:29:40.097583
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = MockTask()
    # init
    RateColumn()
    # case 1
    task.speed = None
    task.total = 1000
    assert RateColumn().render(task).text == "? /s"
    # case 2
    task.speed = 2000
    task.total = 3000
    assert RateColumn().render(task).text == "2.00 /s"
    # case 3
    task.speed = 2000
    task.total = 30000
    assert RateColumn().render(task).text == "2.00 K/s"
    # case 4
    task.speed = 2000
    task.total = 3000000
    assert RateColumn().render(task).text == "2.00 M/s"
    # case 5
    task.speed = 2000
    task.total = 3000000000

# Generated at 2022-06-22 13:29:44.603060
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.progress import Progress
    from rich.console import Console
    console = Console()
    prog = Progress()
    t = tqdm_rich(range(2), console=console)
    prog.add_task(t.desc, total=t.total)
    t.display()

# Generated at 2022-06-22 13:29:52.604089
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    lst = list(range(20))
    with tqdm(initial=len(lst), bar_format="{desc}{bar}") as pbar:
        for x in lst[:10]:
            pbar.desc = f"{x}/{len(lst)}"
            pbar.reset(total=2*len(lst))
            time.sleep(0.1)
        for x in lst[10:]:
            pbar.desc = f"{x}/{2*len(lst)}"
            time.sleep(0.1)

# Generated at 2022-06-22 13:30:00.961292
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    tc = FractionColumn()
    out = tc.render(Progress.Task(100, 100, "", "", "", "", "", "", "", "", ""))
    assert(out.text == '1/1')
    tc = FractionColumn(unit_scale=True, unit_divisor=1000)
    out = tc.render(Progress.Task(100, 100, "", "", "", "", "", "", "", "", ""))
    assert(out.text == '1.0/1.0')
    tc = FractionColumn(unit_scale=True, unit_divisor=1000)
    out = tc.render(Progress.Task(1234, 1234, "", "", "", "", "", "", "", "", ""))

# Generated at 2022-06-22 13:30:04.010694
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """
    Test if method display of class tqdm_rich works.
    """

    t = tqdm(["a", "b"], total=2)
    t.display()

# Generated at 2022-06-22 13:30:19.364955
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import pytest
    assert FractionColumn(unit_scale=False).render(Progress('test',total=0,completed=0)) == Text('0.0/0.0 ',style='progress.download')
    assert FractionColumn(unit_scale=False).render(Progress('test',total=1,completed=1)) == Text('1.0/1.0 ',style='progress.download')
    assert FractionColumn(unit_scale=False).render(Progress('test',total=1000,completed=1000)) == Text('1,000/1,000 ',style='progress.download')
    assert FractionColumn(unit_scale=True).render(Progress('test',total=0,completed=0)) == Text('0.0/0.0 ',style='progress.download')

# Generated at 2022-06-22 13:30:28.252570
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Test the method reset of class tqdm_rich
    """
    from .std import tqdm
    from .std import trange
    from .std import tnrange
    from .std import tqdm_notebook
    from .std import tqdm_pandas
    from .std import tqdm_gui


# Generated at 2022-06-22 13:30:40.569170
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Unit test for method reset of class tqdm_rich

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # unit test for method reset of class tqdm_rich
    # create a fake task to test method reset of class tqdm_rich
    task_id = 123  # a fake task id
    percent = 0  # a fake percent
    desc = ""  # empty string
    total = 10  # a fake total
    unit_scale = False  # a fake unit_scale
    unit_divisor = 1  # a fake unit_divisor
    unit = ""  # a fake unit

# Generated at 2022-06-22 13:30:47.863205
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """ test render method of class FractionColumn """
    assert FractionColumn().render(dict(completed=10, total=20)) == Text('0.5/2 [bytes]', style="progress.download")
    assert FractionColumn(unit_scale=True).render(dict(completed=10, total=20)) == Text('0.5/2 [bytes]', style="progress.download")
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(dict(completed=10, total=20)) == Text('0.0/0.0 [bytes]', style="progress.download")



# Generated at 2022-06-22 13:30:54.166943
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=10) as progress:
        for _ in progress:
            progress.reset(total=20)
            with tqdm_rich(total=10) as progress1:
                for _ in progress1:
                    progress1.reset(total=20)


test_tqdm_rich_reset()

# Generated at 2022-06-22 13:31:02.516763
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Test method render of class FractionColumn."""
    task = [10, 10, 1, 1, 0, 0, 10]
    column = FractionColumn()
    assert str(column.render(task)) == '10.0/10.0 '
    column = FractionColumn(unit_scale=True, unit_divisor=1000)
    assert str(column.render(task)) == '10.0/10.0 '
    task = [10, 10, 1, 1, 0, 0, 1000]
    assert str(column.render(task)) == '10.0/10.0 K'
    task = [10, 10, 1, 1, 0, 0, 1000000]
    assert str(column.render(task)) == '10.0/10.0 M'

# Generated at 2022-06-22 13:31:13.007933
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = Progress()
    task.total = 100
    task.completed = 5
    assert FractionColumn().render(task) == Text(
        "0.0/1.0 ", style="progress.download")
    task.completed = 50
    assert FractionColumn().render(task) == Text(
        "0.5/1.0 ", style="progress.download")
    task.completed = 51
    assert FractionColumn().render(task) == Text(
        "0.5/1.0 ", style="progress.download")
    task.completed = 70
    assert FractionColumn().render(task) == Text(
        "0.7/1.0 ", style="progress.download")
    task.completed = 100

# Generated at 2022-06-22 13:31:25.688217
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Progress
    from rich.style import Style
    from rich.panel import Panel
    from rich.progress import BarColumn
    from tqdm.rich import ProgressColumn, FractionColumn, Text, TimeElapsedColumn, TimeRemainingColumn, filesize

    progress = Progress(
        "[progress.description]{task.description}",
        BarColumn(bar_width=None),
        FractionColumn(
            unit_scale=True, unit_divisor=1000),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), "]")
    progress.__enter__()
    task_id = progress.add_task("", total=100)
    progress.update(task_id, completed=100)
    progress.__exit__(None, None, None)



# Generated at 2022-06-22 13:31:27.473217
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=10) as t:
        t.n = 2
        t.reset(total=20)
        assert t._prog.total == 20

# Generated at 2022-06-22 13:31:31.473047
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test tqdm.rich.tqdm().reset()"""
    with tqdm(total=10) as t:
        t.reset(total=20)
        assert t.total == 20


# Generated at 2022-06-22 13:31:48.735514
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    # Test with `total`
    t = tqdm_rich(10)  # will have `10` total
    t.reset(total=20)  # will have `20` total
    assert t.total == 20
    t.reset(9)  # will have `9` (should be int, not float)
    assert t.total == 9
    # Test without `total`
    t = tqdm_rich(10)  # will have `10` total
    t.reset()  # should have `10` total
    assert t.total == 10
    # Test with `total`=None
    t = tqdm_rich(10)
    t.reset(total=None)  # should have `10` total
    assert t.total == 10
    t = tqdm_rich(10)
    t.reset

# Generated at 2022-06-22 13:31:53.587694
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Test tqdm_rich reset method.
    """
    t = tqdm_rich(total=10)
    for i in range(10):
        t.update()
        if i == 5:
            t.reset(total=3)
    t.close()

# Generated at 2022-06-22 13:32:00.815622
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.traceback import Traceback
    from rich.console import Console
    from rich import print
    from tqdm.auto import tqdm
    from .std import TqdmDeprecationWarning
    import warnings

    warnings.simplefilter('default', TqdmDeprecationWarning)

    with Traceback(), Console(file=None) as console:
        try:
            with tqdm(total=10) as t:
                t.display()
        except AttributeError as e:
            print(e)

# Generated at 2022-06-22 13:32:13.518856
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = rich.Progress.DEFAULT_TASK
    fraction_column = FractionColumn()
    assert fraction_column.render(task) == Text(
        "0.0/1.0", style="progress.download")

    task.completed = 1
    assert fraction_column.render(task) == Text(
        "1.0/1.0", style="progress.download")

    task.completed = 1500
    assert fraction_column.render(task) == Text(
        "1.5/1.0", style="progress.download")

    task.completed = 1.5
    assert fraction_column.render(task) == Text(
        "1.5/1.0", style="progress.download")

    task.completed = 1.578

# Generated at 2022-06-22 13:32:20.685024
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for total in [None, 0, 10]:
        with tqdm(total=total) as t:
            assert t.total == total
            t.n = 7
        with tqdm(total=total) as t:
            assert t.total == total
            assert t.n == 0
            t.update(3)
        with tqdm(total=total) as t:
            assert t.total == total
            assert t.n == 0

# Generated at 2022-06-22 13:32:25.776411
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with trange(100, leave=True) as t:
        assert t.total == 100.0
    with tqdm(100, leave=True) as t:
        assert t.total == 100.0
        t.reset(total=200)
        assert t.total == 200.0
        t.reset()
        assert t.total == 200.0
        t.reset(total=300)
        assert t.total == 300.0

# Generated at 2022-06-22 13:32:34.562937
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import Progress
    from rich.panel import Panel
    from rich.console import Console
    from rich.colors import Color
    from rich.text import Text
    from rich.panel import Panel
    from rich.progress import (
    BarColumn, Progress, ProgressColumn, Text, TimeElapsedColumn,
    TimeRemainingColumn, filesize)
    with Console() as console:
        progress = Progress()
        progress.__enter__()
        params = dict(total=500, desc='Task description')
        task_id = progress.add_task('Second task',
                            BarColumn(bar_width=None),
                            FractionColumn(),
                            "[", TimeElapsedColumn(), "<", TimeRemainingColumn(),
                            "]")
        progress.update(task_id, **params)

# Generated at 2022-06-22 13:32:43.326620
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    >>> class Task:
    ...     total = 1000
    ...     completed = 100
    ...
    >>> uc = FractionColumn()
    >>> uc.render(Task()).text
    '100.0/1,000'
    >>> uc = FractionColumn(unit_scale=True)
    >>> uc.render(Task()).text
    '0.1/1.0 K'
    >>> uc = FractionColumn(unit_scale=True, unit_divisor=1024)
    >>> uc.render(Task()).text
    '98.04/977.54 K'
    """
    pass

# Generated at 2022-06-22 13:32:51.380356
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .gui import tqdm as gui_tqdm

    for tqdm_instance in [tqdm_rich, gui_tqdm]:
        t = tqdm_instance(total=100, leave=True)
        t.update(10)
        t.n = 15
        assert t.n == 15
        t.reset()
        assert t.n == 0
        t.reset(500)
        assert t.n == 0
        assert t.total == 500
        t.update(10)
        t.n = 15
        assert t.n == 15
        t.reset(total=750)
        assert t.n == 0
        assert t.total == 750
        t.update(10)
        t.n = 15
        assert t.n == 15

# Generated at 2022-06-22 13:32:59.709442
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import tqdm
    with tqdm_rich(total=10) as t:
        t.reset(total=1)
        t.reset(total=100)
        t.reset(total=1)
        t.reset(total=10)
        t.reset(total=200)
    with tqdm(total=10) as t:
        t.reset(total=1)
        t.reset(total=100)
        t.reset(total=1)
        t.reset(total=10)
        t.reset(total=200)

# Generated at 2022-06-22 13:33:36.421971
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.console import Console
    from rich.progress import Progress, TaskID
    from rich.text import Text
    from rich.markup import markup
    from rich import box

    progress = Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        FractionColumn(
            unit_scale=False, unit_divisor=1000),
    )
    console = Console()
    taskid = TaskID(box('hello'))
    text = Text(f"0.0/0.0", style="progress.download")
    percentage = "0.0"
    completed = 0
    total = 0
    description = taskid.item
    task=progress.Task(
        completed=completed,
        total=total,
        description=taskid.item,
        percentage=percentage,
    )


# Generated at 2022-06-22 13:33:39.856433
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn(unit="B").render(ProgressColumn.Task(None, None, None, None, None, None, 100, None)) == Text('100.0 B/s', style='progress.data.speed')

# Generated at 2022-06-22 13:33:50.015216
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.console import Console
    from rich.progress import (BarColumn, Progress, ProgressBar)

    console = Console()
    with Progress(transient=True) as progress:
        task_id = progress.add_task("TEST", start=0, end=100)
        with console.progressbar(width=80, show_count=True, show_time=True, show_pos=False, transient=True) as progress_bar:
            progress_bar.reset(total=100)
            assert isinstance(progress_bar, ProgressBar)
            assert isinstance(progress_bar.columns[0], BarColumn)
            progress_bar.update(0, "TEST")
            progress.update(task_id, completed=0)
            assert progress_bar.progress.description == "TEST"

# Generated at 2022-06-22 13:33:58.403657
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import TaskID
    from rich.console import Console
    from time import time as time_now
    from time import sleep

    console = Console()

    with tqdm(total=100, desc="[progress.describe]Test") as pbar:
        task_id = TaskID(pbar._prog, pbar._task_id)
        time0 = time_now()

        # Test if reset() without parameter works
        sleep(0.1)  # sleep 0.1 sec
        pbar.reset()
        sleep(0.1)  # sleep 0.1 sec
        time1 = time_now()
        assert task_id.elapsed == time1 - time0

        # Test if reset() with a parameter works
        pbar.reset(total=200)
        sleep(0.1)  # sleep 0

# Generated at 2022-06-22 13:34:02.477344
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit_scale=True, unit_divisor=1000)
    assert rate_column.render(None) == Text('? /s', style='progress.data.speed')
    assert rate_column.render(0) == Text('? /s', style='progress.data.speed')


# Generated at 2022-06-22 13:34:05.408325
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for unit in range(1):
        t = tqdm_rich(total=100)
        assert t.total == 100
        for i in t:
            pass
        assert t.total == 100
        t.reset(10)
        assert t.total == 10
        for i in t:
            pass
        assert t.total == 10

# Generated at 2022-06-22 13:34:15.142112
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import pytest
    unit = "M"
    rate = RateColumn(unit=unit)
    """
    >>> rate.render(speed=1024, unit_scale=True)
    '1.0 KM/s'
    >>> rate.render(speed=1024, unit_scale=False)
    '1024 M/s'
    >>> rate.render(speed=None, unit_scale=False)
    '? M/s'
    """
    assert rate.render(speed=1024, unit_scale=True) == Text(f"1.0 KM/s", style="progress.data.speed")
    assert rate.render(speed=1024, unit_scale=False) == Text(f"1024 M/s", style="progress.data.speed")

# Generated at 2022-06-22 13:34:18.359560
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    iterable = tqdm_rich(_range(10))
    for _ in iterable:
        pass
    iterable.reset(total=20)  # reset iterable to 20 instead of 10
    for _ in iterable:
        pass
    assert iterable.n == 20

# Generated at 2022-06-22 13:34:23.012292
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import Progress
    progress = Progress(FractionColumn())
    progress.__enter__()
    mytask = progress.add_task("test reset", start=0, total=100)
    progress.update(mytask, completed=100)
    progress.reset(total=None)
    progress.update(mytask, completed=200)
    progress.__exit__(None, None, None)

# Generated at 2022-06-22 13:34:25.420422
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich(total=100)
    t.display()
    t.close()

# Generated at 2022-06-22 13:34:48.792364
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    column = RateColumn(unit='B')
    task = Progress()
    task._total = 1000
    task._completed = 100
    task._start_t = 1519550800.0
    task._last_step_t = 1519550950.0
    task._pos = 700
    assert(column.render(task) == Text("6.0 B/s", style="progress.data.speed"))
    column = RateColumn(unit='B', unit_scale=True)
    assert(column.render(task) == Text("0.006 KB/s", style="progress.data.speed"))
    column = RateColumn(unit='B', unit_scale=True, unit_divisor=1024)
    assert(column.render(task) == Text("0.006 KiB/s", style="progress.data.speed"))

# Generated at 2022-06-22 13:34:56.876939
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Unit test for method display of class tqdm_rich."""
    from rich.progress import Progress

    with Progress() as progress:
        task_id = progress.add_task("", total=10)
        with tqdm_rich(total=10, desc="test", leave=True) as t:
            for i in range(10):
                progress.update(task_id, description="test")
                progress.update(task_id, completed=i)
                t.display()
    assert progress.completed == 10
    assert progress.description == "test"

# Generated at 2022-06-22 13:35:08.411418
# Unit test for method display of class tqdm_rich

# Generated at 2022-06-22 13:35:09.697590
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    trange(1).display()

# Generated at 2022-06-22 13:35:17.250196
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import tqdm_proxy
    t = tqdm_rich(total=2).reset(total=4)
    assert t.total == 4 and t.n == 0

    t = tqdm_proxy(t).reset(total=2)
    assert t.total == 2 and t.n == 0

    t2 = tqdm_rich(total=2).reset(total=4)
    assert t2.total == 4 and t2.n == 0

    t2 = tqdm_proxy(t2).reset(total=2)
    assert t2.total == 2 and t2.n == 0

# Generated at 2022-06-22 13:35:20.831661
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    pbar = tqdm(total=1000)
    assert pbar.total == 1000
    pbar.reset(total=200)
    assert pbar.total == 200

# Generated at 2022-06-22 13:35:29.905740
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = std_tqdm(total=99)

    def test_RateColumn_gen(task, unit, unit_scale, unit_divisor):
        task.speed = None
        RateColumn(unit=unit, unit_scale=unit_scale,
                   unit_divisor=unit_divisor).render(task)

    test_RateColumn_gen(task, "MB", False, 1000)
    test_RateColumn_gen(task, "KB", True, 1000)
    test_RateColumn_gen(task, "MB", True, 1024)
    test_RateColumn_gen(task, "B", True, 1000)
    test_RateColumn_gen(task, "B", True, 1024)


# Generated at 2022-06-22 13:35:35.034332
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        from rich.console import Console
        Console(width=25).print("1234")
    except ImportError:
        return
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for _ in trange(100, desc='Total tqdm_rich'):
        for _ in trange(100, desc='Inner tqdm_rich'):
            pass

# Generated at 2022-06-22 13:35:47.444446
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    class Task:
        def __init__(self, completed, total):
            self.completed = completed
            self.total = total

    actual = FractionColumn(False).render(Task(10, 20))
    expected = "10/20 "
    assert str(actual) == expected
    actual = FractionColumn(False).render(Task(1000, 2000))
    expected = "1,000/2,000 "
    assert str(actual) == expected
    actual = FractionColumn(False).render(Task(10000, 20000))
    expected = "10,000/20,000 "
    assert str(actual) == expected
    actual = FractionColumn(False).render(Task(100000, 200000))
    expected = "100,000/200,000 "
    assert str(actual) == expected

# Generated at 2022-06-22 13:35:51.269485
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=100) as t:
        for i in range(t.total):
            t.update(1)
        t.reset(total=200)
        for i in range(t.total):
            t.update(1)

# Generated at 2022-06-22 13:36:24.749440
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test tqdm_rich display method."""
    from .utils import FormatCustomText, _unicode

    with FormatCustomText(dict(default="{task.completed} ")) as format_dict:
        t = tqdm_rich(format_custom_text=format_dict)
        assert _unicode(t) == "0 "
        t.n = 100
        t.display()
        assert _unicode(t) == "100 "

# Generated at 2022-06-22 13:36:35.402240
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import rich.console

    console = rich.console.Console()

    progress = Progress(
        "Downloading...",
        TimeElapsedColumn(style="bright_magenta"),
        BarColumn(bar_width=None),
        FileSizeColumn(unit_divisor=1000, unit_scale=True),
        "[", TimeRemainingColumn(), "]"
    )

    progress.__enter__()
    task = progress.add_task(
        "example.com",
        total=10,
        completed=0,
        start_time=1460000000.0
    )

    for i in range(10):
        progress.update(task, completed=i)
        console.print(progress)



# Generated at 2022-06-22 13:36:42.987080
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    class TestTask:
        completed = 1
        total = 2
        speed = None
    task = TestTask()
    rate_column = RateColumn()
    assert rate_column.render(task) == Text(f"? /s", style="progress.data.speed")
    rate_column = RateColumn(unit="B")
    assert rate_column.render(task) == Text(f"? B/s", style="progress.data.speed")
    rate_column = RateColumn(unit="B", unit_scale=False)
    assert rate_column.render(task) == Text(f"? B/s", style="progress.data.speed")
    rate_column = RateColumn(unit="B", unit_scale=True)
    assert rate_column.render(task) == Text(f"? B/s", style="progress.data.speed")


# Generated at 2022-06-22 13:36:47.016459
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test `tqdm_rich.display()` method."""
    from .utils import format_sizeof
    pbar = tqdm_rich(total=format_sizeof(5))
    pbar.n = format_sizeof(3)
    pbar.update()

# Generated at 2022-06-22 13:36:58.892160
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    column = RateColumn(unit='B', unit_scale=True, unit_divisor=1024)
    task = {'completed': 10, 'total': 100, 'speed': 10}
    style = column.render(task)
    assert style == "10.00 B/s"
    task = {'completed': 10, 'total': 100, 'speed': 980}
    style = column.render(task)
    assert style == "0.96 KiB/s"
    task = {'completed': 10, 'total': 100, 'speed': 980 ** 2}
    style = column.render(task)
    assert style == "0.94 MiB/s"
    task = {'completed': 10, 'total': 100, 'speed': 980 ** 3}
    style = column.render(task)

# Generated at 2022-06-22 13:37:02.818354
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import pandas as pd
    import pandas.util.testing as pdt
    task = pd.Series({'completed': 1.2, 'total': 2.3})
    tester = FractionColumn()
    result = tester.render(task)
    pdt.assert_series_equal(task, result)

# Generated at 2022-06-22 13:37:09.590026
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from unittest import TestCase, main
    from collections import namedtuple
    from tqdm.utils import _min_interval
    from tqdm.std import FakeTqdmFile
    import sys
    import threading
    import time
    import weakref

    class MockProgress(object):
        class Task(object):
            def __init__(self, **kwargs):
                self.__dict__.update(kwargs)

        def __init__(self):
            self.tasks = {}
            self.ref = weakref

        def add_task(self, description, total, **kwargs):
            task_id = len(self.tasks)
            self.tasks[task_id] = self.Task(description=description,
                                            total=total, **kwargs)
            return task_id



# Generated at 2022-06-22 13:37:11.519856
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    assert hasattr(tqdm_rich(disable=True).display, '__call__')


# Generated at 2022-06-22 13:37:14.278948
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=10) as t:
        t.reset(total=20)
        assert t.total == 20
        t.reset(total=10)

# Generated at 2022-06-22 13:37:17.929333
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    if not hasattr(tqdm_rich(), '_prog'):
        raise AssertionError("'_prog' variable is not defined.")
