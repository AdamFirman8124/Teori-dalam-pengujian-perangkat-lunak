

# Generated at 2022-06-22 13:27:42.391406
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    t = tqdm_rich(total=None, dynamic_ncols=True)
    t.reset(total=5)
    assert t.total == 5


# Generated at 2022-06-22 13:27:52.372427
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn(unit='B').render(tqdm_rich(total=1024, miniters=10,
                                                 bar_format='{n_fmt}/{total_fmt}',
                                                 desc="Test")).text == "0.0 B/s"
    # Test with unit_scale parameter set to True
    assert RateColumn(unit="B", unit_scale=True).render(tqdm_rich(total=1024, miniters=10,
                                                                  bar_format='{n_fmt}/{total_fmt}',
                                                                  desc="Test")).text == "0.0 B/s"


# Generated at 2022-06-22 13:28:05.018970
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # Test precision according to unit
    unit_and_suffix = RateColumn().pick_unit_and_suffix(10, "", 1)
    precision = 0 if unit_and_suffix[0] == 1 else 1
    assert f"{10/unit_and_suffix[0]:,.{precision}f} {unit_and_suffix[1]}/s" == "10.0 /s"
    assert f"{10.44/unit_and_suffix[0]:,.{precision}f} {unit_and_suffix[1]}/s" == "10.4 /s"
    # Test suffixes

# Generated at 2022-06-22 13:28:11.045079
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    pbar = tqdm(range(10))
    pbar.close()
    task = pbar._prog.get_task(pbar._task_id)
    assert task.completed == 10.0, 'The completed must be 10.'
    assert task.total == 10.0, 'The total must be 10.'
    assert task.percentage == 100.0, 'The percentage must be 100.'

# Generated at 2022-06-22 13:28:13.433117
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    for i in tqdm_rich(range(10), desc="Testing tqdm_rich"):
        pass


# Generated at 2022-06-22 13:28:17.646712
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    r = RateColumn()
    assert(r.render(Progress(0, 1)) == Text("? /s", style="progress.data.speed"))
    assert(r.render(Progress(10, 20)) == Text("0.5 /s", style="progress.data.speed"))

# Generated at 2022-06-22 13:28:29.772279
# Unit test for method render of class RateColumn
def test_RateColumn_render():  # pragma: no cover
    from rich.progress import Progress
    from rich.console import Console
    from rich.table import Table

    # Test for speed calculation under different units
    console = Console()
    progress = Progress(
        BarColumn(bar_width=None),
        FractionColumn(),
        RateColumn(unit_scale=True)
    )
    table = Table(show_header=True, header_style="class:header", box="simple")
    table.add_column("Input(B)")
    table.add_column("Output(human readable)")
    table.add_row(1, progress.format_task(1, 1))
    table.add_row(10, progress.format_task(10, 10))
    table.add_row(1000, progress.format_task(1000, 1000))
    table.add

# Generated at 2022-06-22 13:28:42.722551
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    a = FractionColumn()
    assert a.render(3/5, 1) == Text('0.6/1', style='progress.download')
    assert a.render(8/10, 1) == Text('0.8/1', style='progress.download')
    assert a.render(8/10, 100) == Text('0.08/1', style='progress.download')
    assert a.render(80/10, 100) == Text('0.08/1', style='progress.download')
    a = FractionColumn(True)
    assert a.render(3/5, 10) == Text('0.6/1 K', style='progress.download')
    assert a.render(3/5, 1000) == Text('0.6/1 K', style='progress.download')

# Generated at 2022-06-22 13:28:45.940369
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    """
    Tests for method close of class tqdm_rich.
    """
    obj = tqdm_rich(total=10, disable=False)
    obj.close()
    assert obj.disable is True


# Generated at 2022-06-22 13:28:53.731301
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test RateColumn."""
    rate_column = RateColumn()
    t = rate_column.render(None)
    assert t.text == "? /s"
    assert t.style == "progress.data.speed"

    rate_scaled_column = RateColumn(unit_scale=True)
    t = rate_scaled_column.render(None)
    assert t.text == "? /s"
    assert t.style == "progress.data.speed"

    rate_divisor_column = RateColumn(unit_divisor=1024)
    t = rate_divisor_column.render(None)
    assert t.text == "? /s"
    assert t.style == "progress.data.speed"

    rate_unit_column = RateColumn(unit="b")
    t = rate_unit_

# Generated at 2022-06-22 13:29:03.194175
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Task
    task = Task()
    task.completed = 12345
    task.total = 23456
    fc = FractionColumn()

    assert fc.render(task) == Text("12,345/23,456", style="progress.download")

# Generated at 2022-06-22 13:29:05.761997
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    assert rate_column.render(Progress.Task(speed=99)) == Text("99 /s", style="progress.data.speed")

# Generated at 2022-06-22 13:29:08.726965
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # NOTE: this test is disabled because it requires a GUI session
    # to render the progress bar.
    raise NotImplementedError

# Generated at 2022-06-22 13:29:18.852831
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from tqdm.utils import _term_move_up
    from tqdm.auto import tqdm as auto_tqdm

    # Test without leaving
    for total in [5, 11, 2, 20, 99, 1000]:
        with auto_tqdm(total=total, leave=False) as bar:
            bar.update(1)
        assert bar.state.total == total
        assert bar.state.n == total
        assert bar.state.dynamic_ncols is None
        assert bar.state.last_print_length is None

    # Test with leaving
    for total in [5, 11, 2, 20, 99, 1000]:
        with auto_tqdm(total=total, leave=True) as bar:
            bar.update(1)
        assert bar.state.total == total
        assert bar

# Generated at 2022-06-22 13:29:21.713963
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    p = tqdm_rich(total=10)
    for i in _range(10):
        p.update(i)

# Generated at 2022-06-22 13:29:25.652650
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    tqdm_rich(disable=False).close()
    tqdm_rich(disable=True).close()
    tqdm_rich(disable=False).close()
    tqdm_rich(disable=True).close()


# Generated at 2022-06-22 13:29:29.158158
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    with tqdm_rich(total=None) as tqdm_obj:
        tqdm_obj.update(3)
    assert tqdm_obj.n == 3

# Generated at 2022-06-22 13:29:39.986458
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import unittest


# Generated at 2022-06-22 13:29:45.701087
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Unit test for method reset of class tqdm_rich."""
    # With total
    t = tqdm_rich(range(10), total=10)
    t.reset(100)
    assert t.total == 100

    # Without total
    t = tqdm_rich(range(10))
    t.reset()
    assert t.total == 10

# Generated at 2022-06-22 13:29:48.411089
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    tr = trange(5,disable=False)
    tr.close()
    assert tr._prog.is_complete


# Generated at 2022-06-22 13:30:04.464979
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.progress import Task
    assert RateColumn(unit='B').render(Task(speed=1000.0)) == Text(
        f"1.0 KB/s", style="progress.data.speed")
    assert RateColumn(unit='', unit_scale=True).render(Task(speed=100.0)) == Text(
        f"0.1 K/s", style="progress.data.speed")



# Generated at 2022-06-22 13:30:10.521959
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    # Test case: Test unit=G, fraction=1000
    from rich.progress import Progress
    from .std import tqdm as std_tqdm
    for i in std_tqdm(range(100), desc='test progress'):
        progress = Progress()
        column = FractionColumn(unit_scale=True, unit_divisor=1000)
        assert column.render(progress.task).text == "0.0/0.1 G", "Fail"


# Generated at 2022-06-22 13:30:16.599052
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    class Task():
        completed = 10
        total = 20
    task = Task()
    assert FractionColumn().render(task) == Text("1.0/2.0 ", style="progress.download")
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(task) == Text("10.0/20.0 ", style="progress.download")


# Generated at 2022-06-22 13:30:20.676210
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = globals()['tqdm'].tqdm_gui(["a"], total=3)
    assert FractionColumn().render(task) == Text("1/3", style="progress.download")
    task.update(2)
    assert FractionColumn().render(task) == Text("3/3", style="progress.download")
    task.close()


# Generated at 2022-06-22 13:30:22.976179
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Generate the rate string when the unit is bytes and no scaling.
    """
    task = type('task', (), {'speed': None})()
    rate = RateColumn()
    assert rate.render(task) == '0 B/s'



# Generated at 2022-06-22 13:30:28.400766
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from .std import tqdm
    from rich.progress import Progress
    t = tqdm(total=500, desc="test_FractionColumn")
    p = Progress(FractionColumn())
    p.add_task("test_FractionColumn", 0, 500)
    p.update(0, completed=500)
    assert p.render() == '\x1b[2K[0.0/4.8 K][\x1b[92m########          \x1b[0m]\x1b[2K\r'


# Generated at 2022-06-22 13:30:40.936852
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test tqdm_rich.reset()"""
    import time
    import sys
    import io

    @tqdm_rich
    def test():
        for i in range(10):
            yield i
            time.sleep(0.01)
    try:
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        test = test()
        for _ in test:
            pass
    finally:
        sys.stdout = stdout

    assert next(test).n == 0
    assert next(test).n == 1
    assert next(test).n == 2
    assert next(test).n == 3
    test.reset(total=20)
    test.reset(total=-2)
    assert test.total == -2
    assert next(test).n == 0

# Generated at 2022-06-22 13:30:49.293901
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    class Task:
        def __init__(self):
            self.speed = None
    task = Task()
    rate_column = RateColumn()
    assert rate_column.render(task) == Text(f"? B/s", style="progress.data.speed")

    task.speed = 1024 * 1024
    assert rate_column.render(task) == Text(f"1.0 MB/s", style="progress.data.speed")

    rate_column.unit = "i"
    assert rate_column.render(task) == Text(f"1.0 Mi/s", style="progress.data.speed")

    # test scale
    rate_column.unit = "B"
    rate_column.unit_scale = True

# Generated at 2022-06-22 13:30:56.354185
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    """
    Unit test for `tqdm.rich.tqdm()`.
    """
    import time
    total = 100
    with tqdm(total=total, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
        for _ in range(total):
            pbar.update(1)
            time.sleep(0.01)



# Generated at 2022-06-22 13:31:08.365526
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    column = RateColumn()
    task = Progress()
    task.speed = 1024
    assert '1.0 KB/s' == column.render(task)
    task.speed = 8192
    assert '8.1 KB/s' == column.render(task)
    task.speed = 1048576
    assert '1.0 MB/s' == column.render(task)
    task.speed = 1073741824
    assert '1.0 GB/s' == column.render(task)
    column = RateColumn(unit='B')
    task = Progress()
    task.speed = 1024
    assert '1,024.0 B/s' == column.render(task)
    column = RateColumn(unit='iB')
    task = Progress()
    task.speed = 1024
    assert '1.0 KiB/s'

# Generated at 2022-06-22 13:31:34.073819
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.progress import Progress

    def _display(n, desc=None, total=None, leave=None, unit='it',
                 miniters=None, mininterval=None, maxinterval=None,
                 smoothing=None, ascii=None, disable=None):
        p = Progress()
        p.__enter__()
        id = p.add_task(desc or "", total=total, percent=False)
        p.update(id, completed=n, description=desc)
        p.__exit__(None, None, None)

    display = tqdm_rich(gui=True).display
    display(1, desc="desc", total=100, disable=False)  # Test without self.disable
    display(1, desc="desc", total=100, disable=True)  # Test with self.disable

# Generated at 2022-06-22 13:31:38.865004
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress_col = RateColumn(unit_scale=True)
    task = RichTqdmExample(speed=1)
    assert progress_col.render(task).text == "1.0 B/s"
    task = RichTqdmExample(speed=10000)
    assert progress_col.render(task).text == "10.0 K/s"
    task = RichTqdmExample(speed=1000000000)
    assert progress_col.render(task).text == "1.0 G/s"


# Generated at 2022-06-22 13:31:44.083562
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Unit test for method render of class FractionColumn."""
    from rich.progress import Task
    from rich.progress import Progress

    progress = Progress("[progress.description]{task.description}")
    task = Task("1.txt")
    task.start()

    column = FractionColumn()
    column.update(progress, task)



# Generated at 2022-06-22 13:31:50.228307
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # test with unit and unit_scale
    column = RateColumn("B", True)
    assert 'GBytes/s' == column.render(None).text
    # test without unit and unit_scale
    column = RateColumn()
    assert 'Bytes/s' == column.render(None).text
    # test with unit and without unit_scale
    column = RateColumn("B")
    assert 'Bytes/s' == column.render(None).text
    # test without unit and with unit_scale
    column = RateColumn(unit_scale=True)
    assert 'Bytes/s' == column.render(None).text

# Generated at 2022-06-22 13:31:55.499391
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = _range(1, 100, 1)
    task.description = ''
    task.completed = 55
    task.total = 100
    column = FractionColumn()
    column_out = column.render(task)
    assert type(column_out) == Text
    assert column_out.text == '55.0/100.0 '


# Generated at 2022-06-22 13:32:08.052414
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    # Initialization
    unit_scale = False; unit_divisor = 1000
    test_column = FractionColumn(unit_scale, unit_divisor)
    # Create a mock task
    task_mock_describe = "task_mock_describe"
    task_mock_completed = 3000
    task_mock_total = 10000
    class Task:
        def __init__(self, description, completed, total):
            self.description = description
            self.completed = completed
            self.total = total
            self.speed = None
    task_mock = Task(task_mock_describe, task_mock_completed, task_mock_total)
    # Calculate the result of render() method
    result = test_column.render(task_mock)
    # Assert the

# Generated at 2022-06-22 13:32:20.377102
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    column = RateColumn()
    task = tqdm_rich()
    task._total_width = None
    task._units_scale = False
    task._unit_divisor = 1000
    task.miniters = 1
    task.disable = False
    task.dynamic_miniters = False
    task.unit = ""
    task.unit_scale = False
    task.n = 0
    task.miniters = 1
    task.last_print_t = 0
    task.total = 100
    task.dynamic_ncols = True
    task.avg_time = 1
    task.last_print_n = None
    task.total_time = None
    task._time = 0
    task._avg_time = None
    task.iterable = _range(100)
    task.desc

# Generated at 2022-06-22 13:32:28.788047
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    >>> from tqdm.rich import tqdm
    >>> from tqdm import tnrange
    >>> from tqdm._utils import _term_move_up
    >>> for _ in tnrange(4, desc='test_FractionColumn_render', unit='B'):
    ...     print('test_FractionColumn_render')
    ...     with tqdm(total=4, desc='test_FractionColumn_render',
    ...               unit_scale=False, unit_divisor=1000, position=0) as pbar:
    ...         pbar.update(1)
    ...     print(_term_move_up(), end='')
    """
    pass
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-22 13:32:40.454776
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = tqdm_rich(['a', 'b', 'c'], total=3, mininterval=0, miniters=1,
                     unit='it', unit_scale=True, unit_divisor=1024,
                     desc='Test', leave=True)
    task.update(1)
    task._task_id = 1
    task._prog.tasks = {task._task_id: task}
    column = RateColumn('it', True, 1024)
    assert column.render(task) == Text(f"1.0 Kiit/s", style="progress.data.speed")
    task.update(2)
    assert column.render(task) == Text(f"2.0 Miit/s", style="progress.data.speed")
    task.close()

# Generated at 2022-06-22 13:32:49.821866
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = std_tqdm()
    task.speed = 10.3
    task.total = 0
    task.format_dict['unit'] = 'B'
    task.format_dict['unit_scale'] = False
    task.format_dict['unit_divisor'] = 1000
    task.format_dict['unit_divisor'] = 1000
    # try with speed = 0
    assert RateColumn(unit=None).render(task) == Text('0.0 B/s', style='progress.data.speed')
    # try with speed = 10.3
    assert RateColumn(unit=None).render(task) == Text('10.3 B/s', style='progress.data.speed')
    # try with unit = 'B'

# Generated at 2022-06-22 13:33:49.856417
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task =  type('', (), {})()
    task.completed = 1234
    task.total = 4567
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(task) == '1.2/4.6 K'
    assert FractionColumn(unit_scale=False, unit_divisor=1000).render(task) == '1234/4567 '



# Generated at 2022-06-22 13:33:53.846462
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    t = tqdm_rich(total=100, unit="B")
    for i in range(100):
        if i == 50:
            t.reset(total=None)
        t.update(1)
        time.sleep(0.01)
    t.close()

# Generated at 2022-06-22 13:34:00.702435
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from unittest.mock import MagicMock

    # Initialize tqdm_rich
    t = tqdm_rich(total=100)

    for _ in range(100):
        t.update()
        # Test if method display is called
        t._prog.update = MagicMock()
        t.display()
        assert t._prog.update.call_count == 1

    # clear the tqdm_rich
    t.close()


if __name__ == '__main__':
    test_tqdm_rich_display()

# Generated at 2022-06-22 13:34:11.069231
# Unit test for method render of class RateColumn
def test_RateColumn_render():

    class MockTask:
        def __init__(self, speed):
            self.speed = speed

    progress_column = RateColumn()
    task = MockTask(None)
    text = progress_column.render(task)
    assert text.text == '? /s'

    task = MockTask(0)
    text = progress_column.render(task)
    assert text.text == '0.00 /s'

    task = MockTask(1000)
    text = progress_column.render(task)
    assert text.text == '1.00 K/s'

    task = MockTask(1000000)
    text = progress_column.render(task)
    assert text.text == '1.00 M/s'

# Generated at 2022-06-22 13:34:13.208727
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    t = tqdm_rich(total=100)
    t.reset(total=200)
    assert t.total == 200

# Generated at 2022-06-22 13:34:19.682970
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    iterable = tqdm_rich(['foo', 'bar', 'baz'], total=3)
    assert iterable.total == 3
    assert iterable.n == 0

    for i in iterable:
        pass
    assert iterable.total == 3
    assert iterable.n == 3

    iterable.reset(total=4)
    assert iterable.total == 4
    assert iterable.n == 0

    for i in iterable:
        pass
    assert iterable.total == 4
    assert iterable.n == 4

# Generated at 2022-06-22 13:34:25.709976
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Progress, BarColumn, FractionColumn

    prog = Progress(BarColumn(bar_width=None), FractionColumn())

    with prog.task("task1", total=100) as task:
        for j in _range(100):
            task.update(complete=j)
            assert task.completed == j
            task.render()


# Generated at 2022-06-22 13:34:26.843112
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # TODO
    pass

# Generated at 2022-06-22 13:34:34.220029
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    import pytest
    from time import time

    tqdm_rich_obj = tqdm_rich(total=10, desc='test', unit='B', unit_scale=True,
                         mininterval=0, miniters=1)
    tqdm_rich_obj.update(1)
    tqdm_rich_obj.last_print_t = time()
    tqdm_rich_obj.display()
    tqdm_rich_obj.close()
    assert True

# Generated at 2022-06-22 13:34:39.266390
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = Progress(0.0, 1.0)
    task._speed = None
    assert RateColumn().render(task).text == "? /s"
    task._speed = 1024
    assert RateColumn().render(task).text == "1.0 K/s"
    assert RateColumn(unit="B").render(task).text == "1.0 KB/s"

# Generated at 2022-06-22 13:36:12.518321
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    # This test relies on the human vision system.
    # It is tested by viewing the output.

    with tqdm_rich([1, 2, 3], "My label", "My desc",
                   total=1000, unit="steps", unit_scale=True, unit_divisor=1024,
                   ascii=True, miniters=1, mininterval=0, smoothing=0) as bar:
        assert bar.remaining == "?"
        assert bar.n == 0
        time.sleep(0.5)
        bar.update(1)  # unit="steps"
        assert bar.n == 1
        assert bar.unit == "step"  # suffix is stripped
        time.sleep(0.5)
        bar.update(1)  # unit="steps"
        assert bar.n == 2
        time.sleep

# Generated at 2022-06-22 13:36:17.342497
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    column = RateColumn(unit_scale=False, unit_divisor=1000)
    assert column.render(object) == Text('? B/s', style='progress.data.speed')
    column = RateColumn(unit_scale=True, unit_divisor=1000)
    assert column.render(object) == Text('? B/s', style='progress.data.speed')


# Generated at 2022-06-22 13:36:20.952659
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test that reset() works."""
    with tqdm(total=10, bar_format='{n_fmt}/{total_fmt}') as t:
        t.reset(total=100)
        assert t.total == 100

# Generated at 2022-06-22 13:36:26.993068
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time

    for i in tqdm([1, 2, 3, 4, 5]):
        time.sleep(0.1)

    # To check 'tqdm_rich.reset'
    tqdm.reset()

    for i in tqdm([1, 2, 3, 4, 5]):
        time.sleep(0.1)

    # To check 'tqdm_rich.reset'
    tqdm.reset()

    for i in tqdm([1, 2, 3, 4, 5]):
        time.sleep(0.1)

# Generated at 2022-06-22 13:36:31.772545
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    a = tqdm_rich(total=100, desc='test')
    a._prog.add_task('task2')
    assert getattr(a, '_prog') is not None
    assert a._task_id == 1
    a.display()
    assert a.desc == "test"
    assert getattr(a, '_prog').tasks[1].completed == 0
    a.n = 1
    a.display()
    assert getattr(a, '_prog').tasks[1].completed == 1
    # Test after close()
    a.close()
    assert getattr(a, '_prog') is None
    a.display()



# Generated at 2022-06-22 13:36:40.470807
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import tqdm as std_tqdm
    from .std import tnrange as std_tnrange
    from .std import trange as std_trange
    from .std import tqdm_notebook as std_tqdm_notebook
    from .std import tgrange as std_tgrange
    with open(r'tqdm_rich.py', 'r') as handle:
        text = handle.read()
    text = text.replace('std_tqdm', 'tqdm')
    exec(text)
    text = text.replace('tqdm', 'std_tqdm')
    exec(text)
    text = text.replace('std_tnrange', 'tnrange')
    exec(text)
    text = text.replace('tnrange', 'std_tnrange')

# Generated at 2022-06-22 13:36:52.856582
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .gui import tqdm  # import local tqdm
    from .utils import format_sizeof
    from .utils import time_interval_to_human
    from .utils import time_to_str


# Generated at 2022-06-22 13:37:03.386030
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    total_test_cases = 10
    with tqdm_rich(total=total_test_cases) as t:
        for i in range(total_test_cases):
            assert t.total == total_test_cases
            assert t.n == i + 1
            if i == 5:
                t.reset(total=total_test_cases * 2)
            assert t.total == total_test_cases * 2
            assert t.n == i + 1

    with tqdm_rich(total=total_test_cases) as t:
        for i in range(total_test_cases):
            assert t.total == total_test_cases
            assert t.n == i + 1
            if i == 5:
                t.reset()
            assert t.total == total_test_cases

# Generated at 2022-06-22 13:37:04.719003
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm_rich(total=10) as t:
        for i in range(10):
            t.display()
            t.n = i + 1

# Generated at 2022-06-22 13:37:15.456185
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import math
    rateCol = RateColumn(unit="")
    # Test for a zero value
    rateCol.render(Progress(total=1, completed=0))
    try:
        rateCol.render(Progress(total=1, completed=0))
    except ZeroDivisionError:
        print('Test successful')
    # Test for a non-zero value
    rateCol.render(Progress(total=1, completed=1))
    try:
        rateCol.render(Progress(total=1, completed=1))
    except ZeroDivisionError:
        print('Test failed')
    # Test for large values passed
    rateCol.render(Progress(total=math.pow(2, 40), completed=math.pow(2, 40)))