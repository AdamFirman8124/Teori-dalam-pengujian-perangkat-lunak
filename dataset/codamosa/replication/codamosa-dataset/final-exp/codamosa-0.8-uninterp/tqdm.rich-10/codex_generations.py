

# Generated at 2022-06-22 13:27:52.959774
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from tqdm.rich.progress import Progress
    from random import random
    t = tqdm_rich(0, 1)
    t.close()
    assert not hasattr(t, '_prog')
    t = tqdm_rich(0, 1)
    t._prog = Progress("Test progress")
    t.close()
    assert hasattr(t, '_prog')
    t._prog.__exit__(None, None, None)
    assert not hasattr(t, '_prog')
    t = tqdm_rich(0, 1)
    t.update(1)
    t._prog.add_task("Test task", total=1)
    assert hasattr(t, '_prog')
    t.close()
    assert hasattr(t, '_prog')

# Generated at 2022-06-22 13:27:54.899925
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    with tqdm_rich(range(10)) as t:
        t.close()


# Generated at 2022-06-22 13:27:59.765658
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    """
    This test tries to test the method close of class tqdm_rich.
    The task of close() is to set attribute _prog to None.
    """
    t = tqdm_rich(100)
    assert t._prog != None
    t.close()
    assert t._prog == None



# Generated at 2022-06-22 13:28:05.591700
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    progress_bar = tqdm_rich(total=10, desc="Desc")
    progress_bar(0)

    assert progress_bar.reset(total=20) is None

    assert progress_bar.desc == "Desc"
    assert progress_bar.total == 20
    assert progress_bar.n == 0

# Generated at 2022-06-22 13:28:17.389752
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    task = {"task": None, "total": None, "completed": 5, "speed": 16}
    assert rate_column.render(task) == "[16    bps][style=progress.data.speed]"
    rate_column = RateColumn(unit_scale=True, unit_divisor=1000)
    assert rate_column.render(task) == "[16    B/s][style=progress.data.speed]"
    rate_column = RateColumn(unit="ib")
    assert rate_column.render(task) == "[16    bib/s][style=progress.data.speed]"
    rate_column = RateColumn(unit_scale=True, unit_divisor=1000, unit="ib")

# Generated at 2022-06-22 13:28:27.690584
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Unit test for method render of class FractionColumn."""
    import rich
    task = rich.progress.Task(description="test")
    task.completed = 2.5
    task.total = 2.3
    task.update_progress(5, 10)
    assert FractionColumn().render(task) == "1.0/1.0 "
    assert FractionColumn(unit_scale=True).render(task) == "1.0/1.0 K"
    assert FractionColumn(unit_scale=True, unit_divisor=1024).render(task) == "1.0/1.0 K"


# Generated at 2022-06-22 13:28:35.121941
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import rich
    import rich.console
    console = rich.console.Console()

    prog = Progress(
        BarColumn(bar_width=None),
        '{task.description}',
        BarColumn()
    )
    prog.__enter__()
    task = prog.add_task('task', total=10, start=0)
    prog.update(task, completed=3)
    prog.__exit__(None, None, None)
    print()

    prog = Progress(
        BarColumn(bar_width=None),
        '{task.description}',
        BarColumn()
    )
    prog.__enter__()
    task = prog.add_task('task', total=10, start=0)
    prog.update(task, completed=3)
    prog.reset(5)  # set total to 5

# Generated at 2022-06-22 13:28:46.780448
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(range(5), desc="test_tqdm_rich_clear") as pbar:
        for x in pbar:
            pbar.clear()


if __name__ == "__main__":  # pragma: no cover
    import sys
    import time


# Generated at 2022-06-22 13:28:49.007612
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    self = FractionColumn()
    task = {'completed': '1', 'total': '2'}
    assert self.render(task) == '0.5/2.0'

# Generated at 2022-06-22 13:28:51.520462
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    with tqdm_rich(total=1000) as progress:
        for i in progress:
            pass
        progress.reset(total=2000)

# Generated at 2022-06-22 13:28:59.635911
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for total in (0, 1, 2):
        with tqdm(total=total) as bar:
            assert bar.total == total
            bar.reset(total=total-1)
            assert bar.total == total-1


# Generated at 2022-06-22 13:29:03.131016
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    tqdm_rich_obj = tqdm_rich(["this", "is", "tqdm", "Rich", "test"])
    tqdm_rich_obj.close()

# Generated at 2022-06-22 13:29:09.980111
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = Progress.Task()
    task.completed = 9
    task.total = 14
    fc = FractionColumn()
    result = fc.render(task)
    print(result)
    assert str(result) == "[progress.download]0.6/1.0"
    task.completed = 3.12
    task.total = 5.1
    fc = FractionColumn()
    result = fc.render(task)
    print(result)
    assert str(result) == "[progress.download]0.6/1.0"
    fc = FractionColumn(unit_scale=True, unit_divisor=2)
    result = fc.render(task)
    print(result)
    assert str(result) == "[progress.download]0.6/1.0 Ki"
   

# Generated at 2022-06-22 13:29:19.165558
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import tqdm as std_tqdm
    from .std import tgrange as std_trange

    for cls in (std_tqdm, tqdm_rich):
        with cls(total=100) as pbar:
            assert pbar.total == 100
            assert pbar.n == 0
            pbar.reset(total=200)
            assert pbar.total == 200
            assert pbar.n == 0
        with cls(total=100, mininterval=0, miniters=0) as pbar:
            assert pbar.total == 100
            assert pbar.n == 0
            pbar.reset(total=200)
            assert pbar.total == 200
            assert pbar.n == 0

# Generated at 2022-06-22 13:29:31.907638
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    import pytest
    class MockProgress:
        def __init__(self):
            self.start_time = time.time()
            self.last_update_time = self.start_time
            self.update_interval = .1
        def update(self, progress, completed, description):
            time_now = time.time()
            time_since_update = time_now - self.last_update_time
            self.last_update_time = time_now
            assert time_since_update >= self.update_interval

    mock_progress = MockProgress()
    # test that tqdm_rich.display updates progress at correct interval
    t = tqdm_rich(range(1000), progress=mock_progress, gui=True)
    with pytest.raises(AssertionError):
        mock

# Generated at 2022-06-22 13:29:41.562795
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Unit test for RateColumn.render()."""
    # RateColumn.render()
    rc = RateColumn()
    assert rc.render(Progress.Task(completed=100, total=100, speed=100)) == '100.00 B/s'
    assert rc.render(Progress.Task(completed=1000, total=2000, speed=800)) == '800.00 B/s'
    assert rc.render(Progress.Task(completed=1024, total=4096, speed=4096)) == '4.00 K/s'
    assert rc.render(Progress.Task(completed=1024 ** 2, total=1024 ** 3, speed=1024 ** 3)) == '1.00 M/s'

# Generated at 2022-06-22 13:29:44.827811
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    with tqdm_rich(total=10) as _t:
        for i in _range(10):
            pass
        _t.close()


# Generated at 2022-06-22 13:29:55.498336
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    import sys

    # Test default arguments of method clear
    with tqdm_rich(total=2, disable=False) as pbar1:
        pbar1.update()
        pbar1.update()
    assert pbar1.n == 2

    # Test with custom arguments for method clear
    with tqdm_rich(total=2, disable=False) as pbar2:
        pbar2.update()
        pbar2.update(1)

    # Test with disable=True
    with tqdm_rich(total=2, disable=True) as pbar3:
        pbar3.update()
    assert pbar3.n == 1
    assert pbar3.total == 2

    # Test with file=sys.stderr

# Generated at 2022-06-22 13:30:03.443381
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    tqdm.write("standard test")
    assert tqdm.disable

    import sys
    import io
    sys.stdout = io.StringIO()

    t = tqdm(total=1, leave=False)
    assert not t.disable
    t.write("rich test")
    t.close()
    sys.stdout = sys.__stdout__

# Generated at 2022-06-22 13:30:06.772475
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    try:
        from unittest import mock
    except ImportError:
        import mock
    test_bar = tqdm_rich()
    test_bar.close()
    assert not test_bar.disable

# Generated at 2022-06-22 13:30:23.419151
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Test render method of class FractionColumn."""
    import pytest
    from rich.progress import Task

    progress_column = FractionColumn()

    task = Task(completed=0, total=100)
    assert progress_column.render(task) == Text(
        "0/100", style="progress.download")

    task = Task(completed=1, total=100)
    assert progress_column.render(task) == Text(
        "0.0/1.0", style="progress.download")

    task = Task(completed=1, total=10)
    assert progress_column.render(task) == Text(
        "0.1/1.0", style="progress.download")

    task = Task(completed=1, total=1)

# Generated at 2022-06-22 13:30:37.496321
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Unit test for method render of class FractionColumn."""
    from rich.progress import Task
    task = Task("test", completed=0, total=10)
    column = FractionColumn()
    assert str(column.render(task)) == "0.0/10.0"

    column = FractionColumn(unit_scale=True)
    assert str(column.render(task)) == "0.0/10.0"

    task = Task("test", completed=1500, total=10)
    column = FractionColumn(unit_scale=True)
    assert str(column.render(task)) == "1.5/10.0 K"

    column = FractionColumn(unit_scale=True, unit_divisor=1024)
    assert str(column.render(task)) == "1.4/10.0 K"



# Generated at 2022-06-22 13:30:47.666421
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    try:
        from IPython import get_ipython  # type: ignore[attr-defined]
    except ImportError:
        return
    ip = get_ipython()  # type: ignore[attr-defined]
    ip.magic('gui qt5')  # type: ignore[attr-defined]
    ip.magic('autoindent')  # type: ignore[attr-defined]  # noqa: F821
    bar = ip.get_ipython().user_ns['bar']
    bar.reset(total=100)
    assert bar.total == 100
    bar.reset()
    assert bar.total == len(bar.iterable)
    bar.reset(total=None)
    assert bar.total == len(bar.iterable)
    for _ in bar:
        pass

# Generated at 2022-06-22 13:30:59.197563
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    def FractionColumn_render(completed, total, unit_scale, unit_divisor):
        f = FractionColumn(unit_scale=unit_scale, unit_divisor=unit_divisor)
        return f.render(completed, total)
    # init value
    assert FractionColumn_render(1, 1000, False, 1000) == "0.0/1,000 "
    # rounding rule
    assert FractionColumn_render(1, 1000, True, 1000) == "0.0/1 K"
    assert FractionColumn_render(10, 1000, True, 1000) == "0.0/1 K"
    assert FractionColumn_render(100, 1000, True, 1000) == "0.1/1 K"

# Generated at 2022-06-22 13:31:01.898431
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm(total=1) as t:
        assert hasattr(t, 'display')


# Generated at 2022-06-22 13:31:12.597712
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    for rate in [0, 1000, 1024, 1024*1024, 1024*1024*1024, 1024*1024*1024*1024*1024]:
        rate_column = RateColumn()
        data_str = rate_column.render(None).data
        if rate == 0:
            assert data_str == "0 B/s", f"Rate: {rate} != 0 B/s, {data_str}"
            continue
        if rate < 1000:
            assert data_str == f"{rate} B/s", f"Rate: {rate} != {rate} B/s"
        elif rate < 1024*1024:
            assert data_str == f"{rate/1024:.1f} K/s", f"Rate: {rate} != {rate/1024:.1f} K/s"

# Generated at 2022-06-22 13:31:25.087797
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    r_c = RateColumn()
    assert r_c.render(0) == Text('0 B/s', style='progress.data.speed')
    assert r_c.render(1000) == Text('1 KB/s', style='progress.data.speed')
    assert r_c.render(1000 * 1000) == Text('1 MB/s', style='progress.data.speed')
    assert r_c.render(1000 * 1000 * 1000) == Text('1 GB/s', style='progress.data.speed')
    assert r_c.render(1000 * 1000 * 1000 * 1000) == Text('1 TB/s', style='progress.data.speed')
    assert r_c.render(1000 * 1000 * 1000 * 1000 * 1000) == Text('1 PB/s', style='progress.data.speed')
    assert r_c.render

# Generated at 2022-06-22 13:31:29.409260
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    for i in tqdm([1, 2, 3], total=7):
        time.sleep(0.1)
    for i in tqdm([1, 2], total=6):
        time.sleep(0.1)
if __name__ == "__main__":
    test_tqdm_rich_reset()

# Generated at 2022-06-22 13:31:34.007833
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = {"task.completed": 145, "task.total": 1095, "task.percentage": 13.2}
    obj = FractionColumn({}, 1000)
    obj.format_dict = task
    expected_value = "0.1/1.1 K"
    assert obj.render(None) == expected_value


# Generated at 2022-06-22 13:31:40.201396
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    f = FractionColumn(unit_scale = True)
    task = Progress.Task(description = 'Test task', completed = 10, total = 17)
    assert f.render(task).content == '0.6/1.7 K'
    assert f.render(task).style.name == 'progress.download'

# Generated at 2022-06-22 13:31:45.756081
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    a=tqdm_rich(total=10)
    assert a.total == 10
    a.reset(total=5)
    assert a.total == 5, "tqdm_rich reset failed"

# Generated at 2022-06-22 13:31:48.488807
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import pytest
    tq = tqdm_rich(range(15), total=25)
    for i in tq:
        tq.reset(total=50)
        assert tq.total == 50
    tq.close()

# Generated at 2022-06-22 13:31:53.534534
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    with tqdm_rich(total=100) as t:
        for i in _range(10):
            time.sleep(0.01)
            if i == 5:
                t.reset(total=50)
            t.update()
    assert t.n == 10

# Generated at 2022-06-22 13:31:58.936487
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    progress = Progress()
    progress.__enter__()
    task = progress.add_task("prog", total=100)
    progress.completed = {task: 20}
    progress.total = {task: 100}
    fc = FractionColumn()
    assert fc.render(progress.tasks[task]).text == "0.2/1.0"
    progress.__exit__(None, None, None)

# Generated at 2022-06-22 13:32:12.073228
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        import unittest
    except ImportError:
        raise
    from tqdm.std import tqdm_proxy

    from .gui import tgrange

    class TqdmRichTest(unittest.TestCase):
        def setUp(self):
            self.pbars = [tqdm_rich(total=5, bar_format="{l_bar}{bar}{r_bar}")]

        def tearDown(self):
            self.assertFalse(tqdm_proxy._instances)

        def test_update(self):
            """Test update"""
            # sanity check
            self.assertEqual(len(self.pbars), 1)
            self.assertEqual(self.pbars[0].n, 0)
            self.pbars[0].update(3)
            # move to next

# Generated at 2022-06-22 13:32:22.966516
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    progress = (
        "[progress.description]{task.description}",
        " [progress.percentage]{task.percentage:>2.0f}%",
        BarColumn(bar_width=None),
        FractionColumn(
            unit_scale=False, unit_divisor=1000),
        "[", TimeElapsedColumn(), TimeRemainingColumn(), "]")
    try:
        clear = 'cls' if os.name == 'nt' else 'clear'
        subprocess.call(clear, shell=True)
    except:
        pass
    with tqdm(range(100)) as t:
        for i in t:
            t.set_description("Processing")
            time.sleep(0.05)

# Generated at 2022-06-22 13:32:34.196173
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = tqdm_rich(total=10)
    column = FractionColumn()
    task.n = 1
    assert column.render(task) == Text('0.0/1.0')
    task.n = 3
    assert column.render(task) == Text('0.3/1.0')
    task.n = 10
    assert column.render(task) == Text('1.0/1.0')
    column = FractionColumn(unit_scale=True)
    task.n = 1000
    assert column.render(task) == Text('0.0/1.0 K')
    task.n = 1024
    assert column.render(task) == Text('1.0/1.0 K')
    task.n = 1000

# Generated at 2022-06-22 13:32:41.564724
# Unit test for method render of class RateColumn
def test_RateColumn_render():

    col = RateColumn(unit="B")

    task = object()
    task.speed = 100
    assert col.render(task) == Text("100 B/s", style="progress.data.speed")

    col.unit_scale = True
    col.unit_divisor = 1000
    assert col.render(task) == Text("100 B/s", style="progress.data.speed")

    task.speed = 1000
    assert col.render(task) == Text("1.0 K/s", style="progress.data.speed")

# Generated at 2022-06-22 13:32:47.284695
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    t = tqdm_rich(total=10)
    t.update(5)
    display_kwargs = {'n': 5, 'desc': ''}
    t._prog.update = lambda _id, **kwargs: display_kwargs.update(**kwargs)
    t.display()
    assert display_kwargs == {'n': 5, 'desc': '', 'completed': 5}

# Generated at 2022-06-22 13:32:49.782895
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=100, gui=True) as x:
        x.n = 50
        x.reset()  # this fails with a fixed/global Progress object
        assert x.n == 0

# Generated at 2022-06-22 13:33:08.153653
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render({"speed": 0}) == Text("0 B/s", style="progress.data.speed")
    assert RateColumn().render({"speed": 1}) == Text("1 B/s", style="progress.data.speed")
    assert RateColumn().render({"speed": 1.5}) == Text("1.5 B/s", style="progress.data.speed")
    assert RateColumn().render({"speed": 10}) == Text("10 B/s", style="progress.data.speed")
    assert RateColumn().render({"speed": 10.1}) == Text("10.1 B/s", style="progress.data.speed")
    assert RateColumn().render({"speed": 100}) == Text("100 B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:33:16.704958
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import tqdm
    from .utils import format_sizeof
    import time

    with tqdm(range(10), disable=True, unit_scale=True, unit="B") as t:
        for _ in t:
            t.display()
            time.sleep(0.1)
            t.n = format_sizeof(t.n)
            t.total = format_sizeof(t.total)

# Aliases
td = tqdm_rich
trd = trange

# Generated at 2022-06-22 13:33:22.432676
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = tqdm_rich(_range(200), total=100)
    task.n = 50
    method = FractionColumn.render
    assert method(task, task) == Text("0.5/1.0 ", style="progress.download")
    task.n = 100
    assert method(task, task) == Text("1.0/1.0 ", style="progress.download")


# Generated at 2022-06-22 13:33:28.461760
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=1000) as t:
        t.update(500)
    t.reset()
    assert t.n == 0
    assert t.total == 500
    t.reset(total=1000)
    assert t.n == 0
    assert t.total == 1000

# Generated at 2022-06-22 13:33:38.336193
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from unittest.mock import patch
    import tqdm.rich

    with patch.object(tqdm.rich.tqdm_rich, 'display') as mock_disp:
        with tqdm.rich.tqdm_rich(total=5) as t:
            t.update(1)
            assert mock_disp.call_count == 1
            assert mock_disp.call_args == (
                (), {'n': 1, 'total': 5, 'final': False, 'bar_format': None})
        assert mock_disp.call_count == 2
        assert mock_disp.call_args == (
            (), {'n': 1, 'total': 5, 'final': True, 'bar_format': None})



# Generated at 2022-06-22 13:33:49.113378
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import sys
    from io import StringIO
    from .utils import _term_move_up
    from .std import format_interval, format_meter

    # Disable tqdm_rich during test
    tqdm_orig = tqdm_rich
    tqdm_rich = std_tqdm
    capture = StringIO()
    out = sys.stdout
    sys.stdout = capture

    for i in tqdm(total=100):
        sys.stdout.write("\r")
        # capture.write("\r")

# Generated at 2022-06-22 13:33:57.404533
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    progress = (
        "[progress.description]{task.description}"
        "[progress.percentage]{task.percentage:>4.0f}%",
        BarColumn(bar_width=None),
        FractionColumn(
            unit_scale=False, unit_divisor=1000),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(),
        ",", RateColumn(unit="B", unit_scale=False,
                        unit_divisor=1000), "]"
    )

# Generated at 2022-06-22 13:34:05.212856
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import tqdm as std_tqdm
    from .std import trange as std_trange
    from .std import tqdm_gui as std_tqdm_gui
    from .std import trange_gui as std_trange_gui
    for t, T in ((tqdm, std_tqdm),
                 (trange, std_trange),
                 (tqdm_rich, std_tqdm_gui),
                 (trange, std_trange_gui)):
        with t(10, desc="bar") as t_bar:
            assert getattr(t_bar, '_prog', False)
            t_bar.display()
            t_bar.write("text")
        with t(10, desc="bar", file=None) as t_bar:
            assert getattr

# Generated at 2022-06-22 13:34:12.520454
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Testing that the reset method only checks the type of the argument.
    """
    with tqdm_rich(total=3) as pbar:
        pbar.reset(total=1)
        pbar.update()
        pbar.reset(total=None)
        pbar.update()
        pbar.reset(total="null")
        pbar.update()
# https://github.com/tqdm/tqdm/issues/581
test_tqdm_rich_reset()



# Generated at 2022-06-22 13:34:16.156731
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit='B', unit_scale=True, unit_divisor=1024)
    speed = 128.6
    rate = rate_column.render(speed)
    expected = '128.6 B/s'
    assert(rate == expected)

# Generated at 2022-06-22 13:34:32.104873
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import Progress
    with Progress(transient=False) as p:
        task_id = p.add_task("a")
        p.update(task_id, total=10, completed=0)
        task_id = p.add_task("b")
        p.update(task_id, total=5, completed=5)
        task_id = p.add_task("c")
        p.update(task_id, total=1, completed=1)
        p.__exit__(None, None, None)

# Generated at 2022-06-22 13:34:43.090922
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import functools
    from .std import tqdm as std_tqdm

    def assertEqual(a, b):
        if a != b:
            raise ValueError(f'{a} != {b}')

    tqdm_instances = [std_tqdm, tqdm_rich]

    for iterable in [_range(500), 'abcdefghij', object()]:
        for tqdm_cls in tqdm_instances:
            assertEqual(
                list(map(str, tqdm_cls(iterable))),
                list(map(str, tqdm_cls(iterable, disable=True))),
            )

# Generated at 2022-06-22 13:34:47.843529
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # raises AttributeError:
    #   tqdm_rich(0)._prog.update(0, description='foo')
    # raises ValueError:
    #   tqdm_rich(0)._prog.update(10, description='foo')
    tqdm_rich(0)._prog.update(1, description='foo')

# Generated at 2022-06-22 13:34:58.489120
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = lambda **x: type('', (), x)()
    # t/T
    column = FractionColumn(unit_scale=False)
    assert column.render(task(completed=1, total=8)) == Text('0/8 ', style="progress.download")
    # t/T
    column = FractionColumn(unit_scale=False, unit_divisor=1000)
    assert column.render(task(completed=1, total=8)) == Text('0/8 ', style="progress.download")
    # t/T
    column = FractionColumn(unit_scale=True, unit_divisor=1000)
    assert column.render(task(completed=0, total=1000)) == Text('0/1.0 K', style="progress.download")

# Generated at 2022-06-22 13:35:04.509278
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    unit_scale = False
    unit_divisor=1024
    completed = 2
    total = 8.64
    fraction = FractionColumn(unit_scale, unit_divisor)
    result = fraction.render(completed, total)
    assert result == '2.00/8.64 ', 'Not correct result'    


# Generated at 2022-06-22 13:35:10.064070
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    with tqdm_rich(total=3) as pbar:
        assert pbar.gui
        pbar.update()
        time.sleep(0.1)
        pbar.display()
        time.sleep(0.1)
        pbar.update()
        time.sleep(0.1)
        pbar.display()
        time.sleep(0.1)
        pbar.update()

# Generated at 2022-06-22 13:35:20.748834
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import Progress
    from rich.progress import BarColumn
    from rich.progress import TextColumn
    from rich.progress import TimeRemainingColumn
    from rich.progress import TimeElapsedColumn
    from rich.progress import PercentageColumn
    import time
    import random

    prog = Progress(
        TextColumn("[bold magenta]{task.fields[name]}", justify="right"),
        "[progress.percentage]{task.percentage:>4.0f}%",
        BarColumn(bar_width=None),
        " ",
        TextColumn("[red]{task.fields[progress]}"),
        " ",
        TimeRemainingColumn(),
        " ",
        TimeElapsedColumn(),
    )
    prog.__enter__()

    def add_random_number():
        """Add a random number to a list."""

# Generated at 2022-06-22 13:35:22.684000
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # Create the object
    t = tqdm_rich(0)
    t.display()
    t.close()

# Generated at 2022-06-22 13:35:32.616941
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """
    This function tests display() method of class tqdm_rich.
    """
    # instantiate tqdm to test
    if hasattr(tqdm_rich, '_instances'):
        del tqdm_rich._instances[:]
    t = tqdm_rich(disable=False)
    # prepare the test
    t._prog = Progress(
        "[progress.description]{task.description}"
        "[progress.percentage]{task.percentage:>4.0f}%",
        BarColumn(bar_width=None),
        FractionColumn(),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), "]")
    t._prog.__enter__()
    t._task_id = t._prog.add_task("", **{"n": 100.0})


# Generated at 2022-06-22 13:35:37.115146
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.console import Console

    rc = RateColumn()
    task = Progress()
    task._speed = None
    result = rc.render(task)
    assert result == Text("? /s", style="progress.data.speed")

    task._speed = 10
    result = rc.render(task)
    assert result == Text("10.0 /s", style="progress.data.speed")

    task._speed = 9600
    result = rc.render(task)
    assert result == Text("9.6 K/s", style="progress.data.speed")

    task._speed = 9600000
    result = rc.render(task)
    assert result == Text("9.6 M/s", style="progress.data.speed")

    task._speed = 9600000
    result = rc.render(task)

# Generated at 2022-06-22 13:35:52.467355
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Unit test for method render of class RateColumn."""
    import tqdm.rich.progress
    import tqdm.logging
    tqdm.logging.disable_default_handler()
    progress = tqdm.rich.progress.Progress()
    assert progress.render() == ""

    rate_column = RateColumn()
    progress.add_task("task1", 1, 2)
    progress.update(0, speed=None)
    assert rate_column.render(progress.tasks[0]) == Text(
        f" ? /s", style='progress.data.speed')
    progress.update(0, speed=100)
    assert rate_column.render(progress.tasks[0]) == Text(
        f" 100 /s", style='progress.data.speed')

# Generated at 2022-06-22 13:36:02.649925
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test RateColumn class render method"""
    rate_columns = RateColumn(unit="B")
    rate_columns2 = RateColumn(unit="B", unit_scale=True)
    rate_columns3 = RateColumn(unit="B", unit_scale=True, unit_divisor=1024)
    # unit = "B" ; unit_scale = False ; unit_divisor = 1000
    assert (rate_columns.render(10) == "10 B/s")
    assert (rate_columns.render(1025) == "1025 B/s")
    # unit = "B" ; unit_scale = True ; unit_divisor = 1000
    assert (rate_columns2.render(1025) == "1 KB/s")

# Generated at 2022-06-22 13:36:06.721292
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Set the total units of work and reset."""
    with tqdm(total=5) as pbar:
        pbar.reset(total=3)
        for _ in range(3):
            pbar.update()

# Generated at 2022-06-22 13:36:13.582893
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    for i in tqdm(range(8), total=5):
        tqdm.reset()


if __name__ == "__main__":  # pragma: no cover
    from time import sleep

    with tqdm(total=100, desc="Testing...") as pbar:
        for _ in range(10):
            sleep(.1)
            pbar.update(10)

# Generated at 2022-06-22 13:36:18.269176
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    """
    Test method reset of class tqdm_rich.
    """
    with trange(10) as obj:
        assert (obj._prog.total == 10)
        assert (obj._prog._tasks[obj._task_id]['total'] == 10)
        obj.reset(total=20)
        assert (obj._prog.total == 20)
        assert (obj._prog._tasks[obj._task_id]['total'] == 20)

# Generated at 2022-06-22 13:36:27.181646
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # Case when speed is not None
    task = FakeTask()
    task.speed = 10
    task.unit = 'B/s'
    task.unit_scale = False
    task.unit_divisor = 1000
    expected_result = Text(f"10.0 B/s", style="progress.data.speed")
    actual_result = RateColumn(unit='B/s', unit_scale=False, unit_divisor=1000).render(task)
    assert expected_result.text == actual_result.text
    assert expected_result.style == actual_result.style

    # Case when speed is None
    task.speed = None
    expected_result = Text(f"? B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:36:35.838742
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    with tqdm_rich(total=2) as t:
        t.reset(total=5)
        for i in range(5):
            time.sleep(0.1)
            t.set_description(str(i))
            t.update(1)


if __name__ == '__main__':  # pragma: no cover
    from .cli import main
    import sys
    sys.exit(main(prog_name='python -m tqdm.rich'))

# Generated at 2022-06-22 13:36:38.906066
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from time import sleep

    for _ in tqdm(range(10)):
        sleep(0.1)
    tqdm.reset()
    for _ in tqdm(range(10)):
        sleep(0.1)

# Generated at 2022-06-22 13:36:44.885662
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    Test code of FractionColumn.render
    """
    # FIXME: construct object with mandatory attributes with example
    # values
    # instance = rich_progress.FractionColumn(unit_scale=True, unit_divisor=1000)
    # assert expected == instance.render()



# Generated at 2022-06-22 13:36:56.726658
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """Check tqdm_rich() api."""
    tqdm_rich(1)
    tqdm_rich(1, disable=False)
    tqdm_rich(1, disable=True)
    try:
        tqdm_rich(1, bar_format=None, disable=True)  # pylint: disable=unused-variable
    except TypeError:
        pass

    with tqdm_rich(1) as t:
        assert t is not None
        assert t.format_dict['ncols'] >= 0

    try:
        tqdm_rich(1, bar_format=None)  # pylint: disable=unused-variable
    except TypeError:
        pass
    else:
        raise ValueError("should fail")


# Generated at 2022-06-22 13:37:08.786934
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    assert FractionColumn().render(
        Progress(total=10)) == Text('0.0/10.0 ', style='progress.download')



# Generated at 2022-06-22 13:37:13.212162
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Test that the reset method of class tqdm_rich is called and
    that the total argument is passed to the method.
    """
    my_tqdm = tqdm_rich()
    my_tqdm.reset(1)
    assert my_tqdm.total == 1

# Generated at 2022-06-22 13:37:21.627431
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich import box
    from rich.progress import Task
    # Given
    progress = FractionColumn()
    task = Task(completed=0, total=20, description="", start=0, **{"unit_scale": True})
    # When
    result = box.Box(progress.render(task), padding=1)
    # Then
    assert result.text == """
╭──────────────────╮
│0.0/20.0          │
╰──────────────────╯
    """.strip()

# Generated at 2022-06-22 13:37:24.913024
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    with tqdm(range(5)) as t:
        assert t.total == 5

    with tqdm(range(5)) as t:
        t.reset(total = 10)
        assert t.total == 10

# Generated at 2022-06-22 13:37:29.510402
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    pbar = tqdm_rich(total=100, desc="Test")
    for i in pbar:
        pass
        time.sleep(0.1)
        pbar.display()
        print(i)
    pbar.close()

# Generated at 2022-06-22 13:37:35.562243
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    f = tqdm_rich(total=10, unit="B", unit_scale=True, unit_divisor=1000, mininterval=0)
    f.update()
    f.update(1)
    f.update(8)
    f.update(2)
    f.update(9)
    f.update(1)
    f.update()
    f.close()