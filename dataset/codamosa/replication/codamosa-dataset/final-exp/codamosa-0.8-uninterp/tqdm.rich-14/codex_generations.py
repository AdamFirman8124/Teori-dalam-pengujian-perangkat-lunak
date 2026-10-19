

# Generated at 2022-06-22 13:27:58.351845
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = Progress('bar')
    this = FractionColumn()
    task.start()
    task.update(total=1.45)
    a = this.render(task)
    task.update(completed=0.3)
    b = this.render(task)
    task.update(total=2.00)
    c = this.render(task)
    task.update(completed=1.00)
    d = this.render(task)
    task.update(total=1.00)
    e = this.render(task)
    task.update(completed=1.00)
    f = this.render(task)
    task.completed = 1.00
    task.total = 1.00
    g = this.render(task)
    task.update(completed=1.00)


# Generated at 2022-06-22 13:28:07.470786
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.console import Console
    from rich.progress import TaskID
    from unittest import mock

    with mock.patch('tqdm.rich._tqdm_rich.Console'):
        # TODO: Should we use real Console instead of a mock?
        t = tqdm_rich('abc', gui=True)
        t.display()
        assert isinstance(t._task_id, TaskID)
        assert t._task_id == 1
        Console.print.assert_called_once_with('abc', 1)

# Generated at 2022-06-22 13:28:19.370404
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(Task(speed=None)) == Text("? /s", style="progress.data.speed")
    assert RateColumn().render(Task(speed=0)) == Text("0.0 /s", style="progress.data.speed")
    assert RateColumn(unit='B').render(Task(speed=1)) == Text("1.0 B/s", style="progress.data.speed")
    assert RateColumn(unit='B', unit_divisor=1000, unit_scale=True).render(Task(speed=1000)) == Text("1.0 K/s", style="progress.data.speed")
    assert RateColumn(unit='B', unit_divisor=1024, unit_scale=True).render(Task(speed=1024)) == Text("1.0 K/s", style="progress.data.speed")
    assert Rate

# Generated at 2022-06-22 13:28:22.588507
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm_rich(1) as t:
        t.display()
        t.display(True)

# Generated at 2022-06-22 13:28:27.206634
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    import rich.progress
    tp = tqdm_rich(total=5)
    try:
        tp.clear()
    except TypeError:
        pass
    except rich.progress.InvalidProgressOperation:
        pass
    else:
        raise AssertionError('Exception not raised')

# Generated at 2022-06-22 13:28:29.608660
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    >>> task = object()
    >>> col = FractionColumn()
    >>> print(col.render(task))
    None/None
    """
    pass


# Generated at 2022-06-22 13:28:33.453071
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich(total=1)
    try:
        t.display()
        t.close()
    except Exception as e:
        raise(e)
    else:
        pass


# Generated at 2022-06-22 13:28:43.619924
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fc = FractionColumn()
    assert fc.render(Progress(0, 10)) == Text('0.0/10.0')
    assert fc.render(Progress(1, 100)) == Text('0.0/100.0')
    assert fc.render(Progress(10, 100)) == Text('0.1/100.0')
    assert fc.render(Progress(100, 1000)) == Text('0.1/1.0 K')
    assert fc.render(Progress(1000, 10000)) == Text('1.0/10.0 K')
    assert fc.render(Progress(1024, 10000)) == Text('1.0/9.8 K')


# Generated at 2022-06-22 13:28:52.368414
# Unit test for method render of class RateColumn
def test_RateColumn_render():  # pragma: no cover
    from .tqdm import TqdmTypeError
    from .std import BarFormatError
    from .std import UnicodeMixin
    from .utils import _supports_unicode
    from .utils import _environ_cols_wrapper
    from .std import tqdm

    # NOTE: `tqdm` is a class for unit testing purpose
    class tqdm(UnicodeMixin, tqdm):
        @property
        def rate(self):
            return 100

        @property
        def speed(self):
            return 100

    with _environ_cols_wrapper(30):
        with _supports_unicode.set(True):
            t = tqdm(desc=""""\x00""", file=None)

# Generated at 2022-06-22 13:28:58.834596
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    test_RateColumn_render
    """
    rate_column = RateColumn(unit_scale=True, unit_divisor=1000)
    task = {"completed": 1000, "total": 10000}
    unit, suffix = filesize.pick_unit_and_suffix(
        task["total"] - task["completed"],
        ["", "K", "M", "G", "T", "P", "E", "Z", "Y"],
        1000,
    )
    speed = (task["total"] - task["completed"]) / unit
    precision = 0 if unit == 1 else 1
    result = f"{speed:,.{precision}f} {suffix}"
    assert rate_column.render(task) == result

# Generated at 2022-06-22 13:29:05.253954
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm(total=10) as t:
        t.update(1)
        t.display()
        t.update(3)
        t.display()

# Generated at 2022-06-22 13:29:12.217040
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    if not hasattr(tqdm_rich, '_prog'):
        return
    the_range = tqdm_rich(_range(10), desc='test')
    the_range.reset(total=100)
    assert the_range.total == 100
    the_range.close()

# Generated at 2022-06-22 13:29:14.144330
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    x = RateColumn()
    assert (x.render(object()).text == '? /s')

# Generated at 2022-06-22 13:29:20.965126
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress = RateColumn()
    task = std_tqdm(total=1000)
    task.start()
    task.set_description("Downloading")
    task.update(1)
    assert progress.render(task) == Text("? B/s", style="progress.data.speed")
    task.update(10)
    assert progress.render(task) == Text("2.0 K/s", style="progress.data.speed")
    task.update(100)
    assert progress.render(task) == Text("24.0 K/s", style="progress.data.speed")
    task.set_unit("MiB")
    task.update(200)
    assert progress.render(task) == Text("49.0 MiB/s", style="progress.data.speed")
    task.set_unit_scale(False)

# Generated at 2022-06-22 13:29:33.454240
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = std_tqdm(total=1)
    rc = RateColumn()

    # NULL speed
    speed = None
    task.speed = speed
    print(rc.render(task))  # -> Text("? /s", style="progress.data.speed")

    # speed = 1
    speed = 1
    task.speed = speed
    print(rc.render(task))  # -> Text("1 /s", style="progress.data.speed")

    # speed = 1024
    speed = 1024
    task.speed = speed
    print(rc.render(task))  # -> Text("1.00 K/s", style="progress.data.speed")

    # speed = 1024 * 1024 * 1024
    speed = 1024 * 1024 * 1024
    task.speed = speed
    print(rc.render(task))  # -> Text("1

# Generated at 2022-06-22 13:29:44.092361
# Unit test for method render of class RateColumn

# Generated at 2022-06-22 13:29:47.018959
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm(total=70)
    for _ in _range(70):
        t.display()

if __name__ == '__main__':
    test_tqdm_rich_display()

# Generated at 2022-06-22 13:29:50.760965
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    col = FractionColumn()
    completed = 2
    total = 5
    res = col.render(completed, total)
    assert res == Text('0.4/1.0 ', style='progress.download')

# Generated at 2022-06-22 13:29:58.619870
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit='')
    output_text = rate_column.render(Progress(total=1, completed=1))
    assert isinstance(output_text, Text)
    assert str(output_text).endswith(f"{1.0:,.0f} {''}/s")

    rate_column = RateColumn(unit='iterations')
    output_text = rate_column.render(Progress(total=1, completed=1))
    assert isinstance(output_text, Text)
    assert str(output_text).endswith(f"{1.0:,.0f} {''}iterations/s")



# Generated at 2022-06-22 13:30:07.046794
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate = RateColumn(unit="bytes", unit_scale=True, unit_divisor=1024)
    assert rate.render(1) == "1.0  bytes/s"
    assert rate.render(5000.0) == "4.9 Kbytes/s"
    assert rate.render(5000000.0) == "4.8 Mbytes/s"
    assert rate.render(5000000000.0) == "4.7 Gbytes/s"
    assert rate.render(5000000000000.0) == "4.7 Tbytes/s"


# Generated at 2022-06-22 13:30:16.835102
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import get_progress
    bar = tqdm(total=100, desc='Loading')
    bar.reset(total=42)
    bar.close()
    assert get_progress().max(bar._task_id) == 42

# Generated at 2022-06-22 13:30:23.467297
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    d = {}
    d["task"] = tqdm(range(100), unit='unit', unit_scale=True, unit_divisor=1000)
    d["task"].__enter__()
    rc = RateColumn(unit='unit', unit_scale=True, unit_divisor=1000)
    assert rc.render(d["task"]) == Text(f"? unit/s", style="progress.data.speed")

    d["task"].update(1)
    #assert rc.render(d["task"]) == Text(f"1 unit/s", style="progress.data.speed")
    assert rc.render(d["task"]) == Text(f"1 unit/s", style="progress.data.speed")

    d["task"].update(1)
    #assert rc.render(d["task"]) ==

# Generated at 2022-06-22 13:30:30.403634
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn(unit='B', unit_scale=True).render(
        std_tqdm(total=10, position=3)) in ['3.00 KB/s', '3.0 KB/s']
    assert RateColumn(unit='B', unit_scale=False).render(
        std_tqdm(total=10, position=3)) in ['3.00 B/s', '3.0 B/s']
    assert RateColumn(unit='B', unit_scale=True, unit_divisor=1024).render(
        std_tqdm(total=1000, position=3)) in ['3.00 MB/s', '3.0 MB/s']

# Generated at 2022-06-22 13:30:40.678849
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit='B', unit_scale=False)
    assert rate_column.render(Progress(total=1000)) == Text("1.0 B/s", style="progress.data.speed")
    rate_column = RateColumn(unit='', unit_scale=False)
    assert rate_column.render(Progress(total=1000)) == Text("1.0 /s", style="progress.data.speed")
    rate_column = RateColumn(unit='B', unit_scale=True, unit_divisor=2)
    assert rate_column.render(Progress(total=1024)) == Text("1.0 KB/s", style="progress.data.speed")


# Generated at 2022-06-22 13:30:49.194594
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # RateColumn.render(self, task)
    # self.unit = unit
    # self.unit_scale = unit_scale
    # self.unit_divisor = unit_divisor
    # task.speed = speed

    # test for self.unit_scale = True, self.unit = "", self.unit_divisor = 1000
    # speed = 0, 1, 2, 1K, 2K, 1M, 2M, 1G, 2G, 1T, 2T, 1P, 2P
    ratecol = RateColumn(unit="", unit_scale=True, unit_divisor=1000)


# Generated at 2022-06-22 13:31:00.165808
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # Test with real objects
    t = tqdm_rich(total=100)
    t.update(0)
    t.update(10)
    t.update(50)
    t.update(90)
    t.update(100)
    # Test with mock objects
    t = tqdm_rich(total=100)
    t.update(10)
    t.update(90)
    # Test with no total
    t = tqdm_rich()
    t.update(10)
    t.update(90)
    # Test with no bar
    import warnings
    warnings.filterwarnings("ignore", message=".*Using or importing the ABCs.*")
    t = tqdm_rich(total=100, leave=True, desc="Hello")
    t.update(10)

# Generated at 2022-06-22 13:31:06.687797
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Task
    task = Task(description="test", total=3)
    task._completed = 2
    assert FractionColumn().render(task).text == "0.7/3.0"
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(task).text == "0.7/3.0 K"


# Generated at 2022-06-22 13:31:14.051085
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    with tqdm(total=10, desc="testing") as pbar:
        for i in range(4):
            pbar.update()
        for i in range(4):
            pbar.update(2)
    with tqdm(total=10, desc="testing", mininterval=1000) as pbar:
        for i in range(4):
            pbar.update()
        for i in range(4):
            pbar.update(2)
    with tqdm(total=10, desc="testing", mininterval=0) as pbar:
        for i in range(4):
            pbar.update()
        for i in range(4):
            pbar.update(2)



# Generated at 2022-06-22 13:31:17.147408
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    with tqdm_rich(desc="test", total=10) as t:  # noqa
        for i in range(10):
            t.n = i
            t.update()

# Generated at 2022-06-22 13:31:20.379057
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """
    Test method display of class `tqdm_rich`
    """
    # display before adding a task
    obj = tqdm_rich(1, desc="Example")
    obj.display()
    obj.close()

# Generated at 2022-06-22 13:31:39.792099
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = tqdm_rich()
    task.total = 2.3
    task.completed = 0.5
    column = FractionColumn()
    assert column.render(task) == "0.5/2.3 "

# Generated at 2022-06-22 13:31:48.962209
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        import rich
    except ImportError:
        return
    from .std import tqdm
    from .utils import EmptyContext
    from .std import format_interval
    from time import time, sleep
    from numpy import random

    # Sleeps a random amount of time between 0.0 and 0.2s
    # and then prints a message
    def sleep_and_print(t):
        sleep(random.rand() * 0.2)
        t.set_description('Finished after %.2fs' %
                          format_interval(t.elapsed))

    # Creates a progressbar which sleeps a random amount of time
    # every time it's updated

# Generated at 2022-06-22 13:31:50.500173
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=0) as bar:
        bar.reset(total=100)
        assert bar.total == 100

# Generated at 2022-06-22 13:32:01.395756
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test display method of tqdm_rich"""
    import sys
    import os

    # Make sure tqdm is not available as an installed module:
    tqdm_rich.__module__ = 'NOT_INSTALLED'
    tqdm_rich._prog = None
    tqdm_rich.disable = True

    # In case tqdm was installed beforehand
    tqdm_rich.close()

    progress_test = tqdm_rich(total=10)
    progress_test.__enter__()

    try:
        progress_test.display()
    except AttributeError:
        pass  # Test passed

    tqdm_rich.close()

    progress_test = tqdm_rich(total=10)
    progress_test.__enter__()
    progress_test.disable = False

    progress

# Generated at 2022-06-22 13:32:06.668521
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = None
    column = FractionColumn(unit_scale = False, unit_divisor = 1000)
    column.render(task)
    column = FractionColumn(unit_scale = True, unit_divisor = 1000)
    column.render(task)


# Generated at 2022-06-22 13:32:16.158544
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import rich.progress
    import io
    import sys

    old_sys = sys.stdout
    try:
        sys.stdout = io.StringIO()
        progress = Progress()
        with progress:
            # Make sure the task is added so that we can test the reset
            progress.add_task("test")
            def test_reset(total):
                progress.reset(total=total)
                progress.update(0, advance=total)
            does_not_raise = test_reset(1)
            assert does_not_raise is None

    finally:
        sys.stdout = old_sys

# Generated at 2022-06-22 13:32:22.650933
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = object()
    task.completed = 1234567890
    task.total = 123456789
    column = FractionColumn()
    assert column.render(task) == Text("12,345,678.9/1,234,567.9", style="progress.download")
    column = FractionColumn(unit_scale=True)
    assert column.render(task) == Text("12.3/1.2 G", style="progress.download")


# Generated at 2022-06-22 13:32:34.134764
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress_trange = trange(10, desc="testing", leave=True)
    progress_trange.update(2)
    r = FractionColumn(unit_scale=False, unit_divisor=1)
    assert r.render(progress_trange) == Text("2/10", style="progress.download")
    r = FractionColumn(unit_scale=True, unit_divisor=1000)
    assert r.render(progress_trange) == Text("2.0/10 K", style="progress.download")
    r = FractionColumn(unit_scale=True, unit_divisor=1024)
    assert r.render(progress_trange) == Text("2.0/10 K", style="progress.download")
    r = FractionColumn(unit_scale=True, unit_divisor=1)

# Generated at 2022-06-22 13:32:42.908805
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = std_tqdm(total=10, smoothing=0)
    fc = FractionColumn()
    assert fc.render(task) == Text('0.0/10.0 ')
    task.update(5)
    assert fc.render(task) == Text('5.0/10.0 ')
    task.update(5)
    assert fc.render(task) == Text('10.0/10.0 ')
    task.update(5)
    assert fc.render(task) == Text('15.0/10.0 ')
    task.close()
    del fc, task


# Generated at 2022-06-22 13:32:45.861598
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    tr = tqdm_rich(total=100)
    assert tr.n == 0 and tr.total == 100
    tr.display()
    assert tr.n == 0 and tr.total == 100
    tr.close()

# Generated at 2022-06-22 13:33:10.194092
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test RateColumn.render() method."""
    from rich.progress import Task
    task = Task()
    task._speed = None
    assert RateColumn().render(task) == Text("? /s", style="progress.data.speed")
    task._speed = 1
    assert RateColumn().render(task) == Text("1.0 /s", style="progress.data.speed")
    task._speed = 2
    assert RateColumn().render(task) == Text("2.0 /s", style="progress.data.speed")
    task._speed = 3
    assert RateColumn().render(task) == Text("3.0 /s", style="progress.data.speed")
    task._speed = 4
    assert RateColumn().render(task) == Text("4.0 /s", style="progress.data.speed")

# Generated at 2022-06-22 13:33:15.381028
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=1, leave=True) as pbar:
        assert pbar.total == 1
        pbar.reset(total=2)
        assert pbar.total == 2

# Generated at 2022-06-22 13:33:24.767254
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    test_task = std_tqdm.tqdm(total=2.3)
    test_task.n = 1.2
    test_task.last_print_n = 1.2
    test_task.last_print_t = 1
    test_task.smoothing = 1.0
    test_task.total = 2.3
    test_task.start_t = 1
    test_task.n_fmt = '{n:.3f}{postfix[0]}'
    test_task.desc = None
    test_task.unit = 'B'
    test_task.unit_scale = False
    test_task.unit_divisor = 1
    test_task.monitor = None
    test_task.refresh_rate = 0.001
    test_task.disable = False
    test

# Generated at 2022-06-22 13:33:29.255375
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    The render method should return '0  B/s' for first call
    and then return '0.0 B/s' for second call.
    """
    column = RateColumn()
    task = Progress(1)
    task.completed = 0
    task.total = 1
    task.speed = 0
    # First call of render method
    test_speed = column.render(task)
    assert test_speed.string.strip() == '0  B/s'
    # Second call of render method
    task.speed = 3.2
    test_speed = column.render(task)
    assert test_speed.string.strip() == '3.2 B/s'



# Generated at 2022-06-22 13:33:31.341816
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    f = tqdm_rich(range(10))
    for i in f:
        pass

# Generated at 2022-06-22 13:33:42.426314
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    tqdm_column = RateColumn(unit="B")
    task = ProgressColumn()
    task.speed = None
    task.completed = None
    task.total = None
    assert tqdm_column.render(task) == Text(f"? B/s", style="progress.data.speed")

    task.speed = 11
    task.completed = None
    task.total = None
    assert tqdm_column.render(task) == Text(f"11 B/s", style="progress.data.speed")

    task.speed = 11
    task.completed = 32
    task.total = 134
    task.speed = 1024
    assert tqdm_column.render(task) == Text(f"1.00 KiB/s", style="progress.data.speed")

# Generated at 2022-06-22 13:33:48.456527
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import rich.progress as r

    class Mock_r():
        def __init__(self, *args):
            pass

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, exc_traceback):
            pass

        def add_task(self, *args, **kwargs):
            pass

        def update(self, *args, **kwargs):
            pass

    r.Progress = Mock_r
    tqdm(range(4)).display()

# Generated at 2022-06-22 13:33:57.504435
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    try:
        import rich
    except ImportError:
        raise ImportError("rich is not installed. "
                          "To use this feature, install it:   pip install rich")

    # Error: Missing attribute _prog
    tqdm_rich_no_prog = tqdm_rich()
    tqdm_rich_no_prog.display()

    # Error: Missing attribute _task_id
    tqdm_rich_no_task_id = tqdm_rich()
    tqdm_rich_no_task_id._prog = Progress()
    tqdm_rich_no_task_id.display()

    # Normal behaviour. Adding a task and updating it.
    tqdm_rich_normal = tqdm_rich()
    tqdm_rich_normal._pro

# Generated at 2022-06-22 13:34:05.238959
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    f = FractionColumn()
    task = Progress(total=10)
    assert f.render(task) == Text("0.0/10 ", style="progress.download")
    task.completed = 1
    assert f.render(task) == Text("0.1/10 ", style="progress.download")
    task.total = 1
    assert f.render(task) == Text("1.0/1 ", style="progress.download")
    task.total = 1000
    assert f.render(task) == Text("1.0/1 K", style="progress.download")
    task.total = 1000000
    assert f.render(task) == Text("1.0/1.0 M", style="progress.download")
    task.total = 1000000000

# Generated at 2022-06-22 13:34:08.221346
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    pbar = tqdm(total=100)
    pbar.reset()

    assert pbar.total == 1

# Generated at 2022-06-22 13:35:34.743128
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from datetime import timedelta
    from re import compile as compile_re
    from rich import progress
    from .std import tqdm

    progress.interval = timedelta(microseconds=1)

    def observed(rate):
        t = tqdm(total=100, desc='test', unit='B', unit_scale=True, unit_divisor=1000)
        t.update(rate)
        inner_regex = compile_re('\\[\\d+%\\]\\s+')
        outer_regex = compile_re('\\[test\\]\\[\\d+%\\]\\s+\\d+.\\d+[kKM]B/s')
        return outer_regex.search(inner_regex.sub('', str(t))).group()


# Generated at 2022-06-22 13:35:37.272674
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from tqdm.auto import trange
    for _ in trange(2, disable=True):
        pass

# Generated at 2022-06-22 13:35:44.201111
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import time
    wait_rate = RateColumn(unit_scale=True)
    task = Progress()
    task.start()
    time.sleep(1)
    task.update()
    print(wait_rate.render(task))
    task.update(task.total)
    print(wait_rate.render(task))
    task.update()
    print(wait_rate.render(task))
    

# Generated at 2022-06-22 13:35:51.776228
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    from .std import tqdm as std_tqdm
    import time

    # Testing case total is None
    for i in tqdm_rich(range(10), desc="Reset case1", leave=True):
        time.sleep(0.1)
        if i == 5:
            i.reset()
        time.sleep(0.1)

    # Testing with total is 2
    for i in tqdm_rich(range(10), desc="Reset case2", leave=True,
                       total=2):
        time.sleep(0.1)
        if i == 5:
            i.reset(2)
        time.sleep(0.1)

    # Testing with total is 20

# Generated at 2022-06-22 13:36:01.173408
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from .utils import bytesize
    rc = RateColumn(unit='B')
    data_rate = bytesize(1000, 'B')
    assert rc.render(data_rate) == Text("1 B/s", style="progress.data.speed")
    data_rate = bytesize(1200, 'B', 1)
    assert rc.render(data_rate) == Text("1.2 B/s", style="progress.data.speed")
    data_rate = bytesize(1050, 'B', 1)
    assert rc.render(data_rate) == Text("1.1 B/s", style="progress.data.speed")


# Generated at 2022-06-22 13:36:13.752634
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    """Simple unit test for tqdm_rich."""
    from time import sleep
    from rich import print
    print("Progress Bars")
    print("--------------")

    # The simplest tqdm_rich usage.
    print("Progress")
    with Progress() as progress:
        task_id1 = progress.add_task("Progress", total=3)
        for i in range(3):
            sleep(0.5)
            progress.update(task_id1, advance=1)

    # options can be passed to Progress
    print("Progress (no transient)")
    with Progress(transient=False) as progress:
        task_id1 = progress.add_task("Progress", total=3)
        task_id2 = progress.add_task("Progress", total=3)

# Generated at 2022-06-22 13:36:17.210842
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import io
    import sys
    rate_column = RateColumn()
    sys.stdout = io.StringIO()
    task = {"speed":1000, "description": "a"}
    rate_column.render(task)
    sys.stdout = sys.__stdout__

# Generated at 2022-06-22 13:36:20.155927
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Tests tqdm_rich method 'reset'"""
    for i in tqdm([1, 2, 3]):
        if i == 2:
            tqdm.reset()

# Generated at 2022-06-22 13:36:24.112109
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="Byte", unit_scale=True, unit_divisor=1000)
    task = type('Task', (), {'speed': 100})()
    assert rate_column.render(task) == Text("0.10 KByte/s", style="progress.data.speed")

# Generated at 2022-06-22 13:36:35.796119
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn(unit_scale=False, unit_divisor=1).render({'speed': None}) == Text('? /s', style='progress.data.speed')
    assert RateColumn(unit_scale=False, unit_divisor=1).render({'speed': 5}) == Text('5 /s', style='progress.data.speed')
    assert RateColumn(unit_scale=True, unit_divisor=1).render({'speed': 50}) == Text('50 /s', style='progress.data.speed')
    assert RateColumn(unit_scale=True, unit_divisor=10).render({'speed': 50}) == Text('5 K/s', style='progress.data.speed')

# Generated at 2022-06-22 13:37:22.833517
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    with tqdm(10) as _t:
        assert isinstance(_t, tqdm_rich)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-22 13:37:34.084993
# Unit test for method render of class RateColumn
def test_RateColumn_render():  
    """
    Test the render function with following values:
        speed = 1000 (unit_scale = False)
        speed = 1000 (unit_scale = True)
        speed = None
    """
    task = Progress
    task.speed = 1000
    ratecolumn = RateColumn()
    assert ratecolumn.render(task) == Text("1,000  /s", style="progress.data.speed")
    ratecolumn = RateColumn(unit_scale = True)
    assert ratecolumn.render(task) == Text("1,000   /s", style="progress.data.speed")
    task.speed = None
    assert ratecolumn.render(task) == Text("?  /s", style="progress.data.speed")
    # TODO: more testcases