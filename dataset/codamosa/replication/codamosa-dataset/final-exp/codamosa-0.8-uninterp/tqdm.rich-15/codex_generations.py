

# Generated at 2022-06-22 13:27:51.268001
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # type: (None) -> None
    """
    """
    below_1K = RateColumn(unit_scale=True, unit_divisor=1000)
    below_1K.render_ = lambda *args, **kwargs: (args, kwargs)
    assert below_1K.render(object()) == (
        (None,),
        {'unit': '', 'unit_scale': True, 'unit_divisor': 1000}
    )

    below_1KiB = RateColumn(unit_scale=True, unit_divisor=1024)
    below_1KiB.render_ = lambda *args, **kwargs: (args, kwargs)

# Generated at 2022-06-22 13:28:03.730978
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    completed, total = 1, 2
    unit_scale, unit_divisor = False, 1000
    unit, suffix = filesize.pick_unit_and_suffix(total, [""], 1)
    precision = 0 if unit == 1 else 1
    fraction = f"{completed/unit:,.{precision}f}/{total/unit:,.{precision}f} {suffix}"
    assert fraction == "1/2 "
    unit_scale, unit_divisor = True, 1000
    unit, suffix = filesize.pick_unit_and_suffix(total, ["", "K", "M", "G", "T", "P", "E", "Z", "Y"], unit_divisor)
    precision = 0 if unit == 1 else 1

# Generated at 2022-06-22 13:28:07.657819
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    result = RateColumn().render({'speed': 123})
    assert result == Text(f"123.0 /s", style="progress.data.speed")
    result = RateColumn().render({'speed': 123, 'disable': True})
    assert result is None

# Generated at 2022-06-22 13:28:14.964610
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    progress = [
        "[progress.description]{task.description}",
        FractionColumn(),
        BarColumn(bar_width=None),
        " [", TimeElapsedColumn(), ",", TimeRemainingColumn(), "]",
    ]
    with tqdm_rich(total=0, progress=progress) as trange:
        trange.reset(total=10)


# vim: set fileencoding=utf-8 ts=4 sw=4 et tw=80 :

# Generated at 2022-06-22 13:28:17.491273
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    new_RateColumn = RateColumn()
    assert isinstance(new_RateColumn.render(1), Text)


# Generated at 2022-06-22 13:28:29.568898
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import time
    import math
    class DummyProgress:
        time = time.time
        completed = 0.0
        total = 100.0
        speed = 0.0
    dummy_progress = DummyProgress()

# Generated at 2022-06-22 13:28:42.351908
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    assert FractionColumn().render({"total": 123456789, "completed": 23456789}) == "[progress.download]23.5/123.5 M"
    assert FractionColumn().render({"total": 123456789, "completed": 1.23456789}) == "[progress.download]1.2/123.5 M"
    assert FractionColumn().render({"total": 123456789, "completed": 2345678.9}) == "[progress.download]2.3/123.5 M"
    assert FractionColumn().render({"total": 12345678.9, "completed": 2345678.9}) == "[progress.download]2.3/12.3 M"

# Generated at 2022-06-22 13:28:44.126193
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(total=100, disable=False) as t:
        t.clear()
    assert t.disable == True


# Generated at 2022-06-22 13:28:52.957089
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import sys, os
    try:
        import builtins
    except ImportError:
        import __builtin__ as builtins

    def print(*args, **kwargs):
        """The new-style print function taken from
        https://docs.python.org/3.0/whatsnew/3.0.html#print-is-a-function
        """
        fp = kwargs.pop("file", sys.stdout)
        if fp is None:
            return

        def write(data):
            if not isinstance(data, basestring):
                data = str(data)
            # If the file has an encoding, encode unicode with it.
            if (isinstance(fp, file) and
                isinstance(data, unicode) and
                fp.encoding is not None):
                errors = getattr

# Generated at 2022-06-22 13:28:59.521947
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .utils import _locale_reset, _unicode
    from .std import tqdm, tqdm_gui, tqdm_notebook, tqdm_pandas, tqdm_pandas_notebook
    from .auto import tqdm as atqdm

    _locale_reset()
    try:  # Python 2
        range_ = xrange
    except NameError:
        range_ = range
    with tqdm_rich(range_(10)) as t:
        assert hasattr(t, '_prog')
        t.reset(total=5)
        assert t._prog.total == 5
        assert t.total == 5
        t.reset(total=10)
        assert t._prog.total == 10
        assert t.total == 10

# Generated at 2022-06-22 13:29:04.153223
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    tqdm_rich(range(100))

# Generated at 2022-06-22 13:29:09.184623
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.panel import Panel
    from rich.console import Console

    with Console() as console:
        console.print(Panel("[bold underline] [yellow] tqdm_rich.display() test [/yellow] [/bold underline]", style="cyan"))
        for _ in tqdm(range(5), desc="Test", gui=True, progress=(
                "[progress.description]{task.description}",
                "[progress.percentage]{task.percentage:>4.0f}%"), transient=False):
            pass



# Generated at 2022-06-22 13:29:18.912858
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress
    from rich.text import Text
    from rich.columns import Columns
    import sys
    import time

    console = Console()
    progress = Progress(Text("[progress.description]{task.description}"),
                        "[progress.percentage]{task.percentage:>4.0f}%",
                        BarColumn(bar_width=None))
    with console.progress(progress, transient=False) as prog:
        task_id = prog.add_task("Task 1", total=100)
        for i in std_tqdm(range(100)):
            time.sleep(0.01)
            prog.update(task_id, i)
        sys.stdout.write('\n')


# Generated at 2022-06-22 13:29:31.675891
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from re import findall
    from os import name as os_name
    from subprocess import check_output

    for dialect in [tqdm_rich, std_tqdm]:
        # Test progress bar display
        progress_bar = dialect(
            "Testing progress bar...",
            total=3,
            dynamic_ncols=True,
            unit='B',
            unit_scale=True,
            bar_format='{desc}{representation}{percentage:>5.2f}%|{bar}| {n}/{total_fmt} [{elapsed_s}<{remaining_s},{rate_fmt}]',
        )
        progress_bar.display()

        # Static bar, no output

# Generated at 2022-06-22 13:29:33.833192
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import trange
    t = trange(10, desc="Test")
    for _ in t:
        assert t.total == 10
        if t.n > 5:
            assert t.n == 6
            t.reset(total=4)
            assert t.total == 4


# Generated at 2022-06-22 13:29:37.952115
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from tqdm.rich import FractionColumn
    from rich.progress import Task

    task = Task(total=1000, completed=500)
    assert FractionColumn().render(task) == \
        Text("0.5/1.0 ", style="progress.download")

# Generated at 2022-06-22 13:29:44.577593
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rc = RateColumn("/s")
    rc._task = {'speed': None, 'description': '1.0 M'}
    rc._d = {'unit': 'M', 'unit_scale': True, 'unit_divisor': 1000}
    assert rc.render() == Text("? M/s", style="progress.data.speed")

    rc._task = {'speed': 123456, 'description': '1.0 M'}
    assert rc.render() == Text("123.456 K/s", style="progress.data.speed")

    rc._task = {'speed': 12345678, 'description': '1.0 M'}
    assert rc.render() == Text("12.346 M/s", style="progress.data.speed")

    rc = RateColumn("/s", unit_scale=False)
    rc

# Generated at 2022-06-22 13:29:55.395228
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="B",unit_divisor=1000) 
    result = rate_column.render(0,0,0)
    assert result.value == "? B/s"
    assert result.style.name == "progress.data.speed"
    result = rate_column.render(0,0,3)
    assert result.value == "3 B/s"
    assert result.style.name == "progress.data.speed"
    result = rate_column.render(0,0,300)
    assert result.value == "300 B/s"
    assert result.style.name == "progress.data.speed"
    result = rate_column.render(0,0,300000)
    assert result.value == "300 KB/s"

# Generated at 2022-06-22 13:30:08.434919
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    column = RateColumn(unit="B", unit_scale=True, unit_divisor=1000)
    render = column.render(std_tqdm(total=123, unit="B", unit_scale=True, unit_divisor=1000))
    assert render.text == "0.0 KB/s"
    render = column.render(std_tqdm(total=12345, unit="B", unit_scale=True, unit_divisor=1000))
    assert render.text == "12.3 KB/s"
    render = column.render(std_tqdm(total=12345678, unit="B", unit_scale=True, unit_divisor=1000))
    assert render.text == "12.3 MB/s"

# Generated at 2022-06-22 13:30:18.463094
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import Progress
    with Progress() as prog:
        task_id = prog.add_task('task1', total=10)
        task_id2 = prog.add_task('task2', total=20)
        bar = tqdm(
            iterable=range(10),
            total=10,
            leave=False,
            disable=None,
            bar_format='{l_bar}',
            progress=(
                '[progress.description]{task.description}',
                BarColumn(bar_width=None)))
        # prog.reset(task_id, total=20)
        bar.reset(total=20)
        for i in bar:
            pass
        bar.close()

# Generated at 2022-06-22 13:30:25.641064
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    with tqdm_rich(total=10) as pbar:
        def display(self, *_, **__):
            pass
        display_mem = pbar.display
        pbar.display = display
        time.sleep(0.2)
        pbar.display = display_mem

# Generated at 2022-06-22 13:30:37.496491
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    import sys
    import random
    from .gui import tqdm
    from .utils import _range

    a = tqdm(_range(10), desc="Test")
    for _ in a:
        # Do not use time.sleep here, it makes the test *slow*
        # It is used in 'test_prog_gui' instead
        pass
    assert a.dynamic_miniters, \
        "miniters != 0 for dynamic_miniters=True (default)"

    b = tqdm(_range(10), dynamic_miniters=False)
    assert not b.dynamic_miniters
    b.close()

    c = tqdm(_range(10))
    c.total = 20
    assert c.total == 20
    c.close()

    d = t

# Generated at 2022-06-22 13:30:42.448252
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from tqdm import tqdm
    with tqdm(total=1000) as pbar:
        for i in range(100):
            pbar.n = 100*i
            pbar.reset(total=1000)
    assert pbar.n == 10000

# Generated at 2022-06-22 13:30:45.505959
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich(1, 1)
    t.n = 1
    t.total = 1
    t.last_print_n = 1
    t.display()
    assert t.last_print_n == 1
    t.close()

# Generated at 2022-06-22 13:30:54.349131
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    completed = 999999999999999
    total = 9999999999999999999999999999999
    scale_unit, suffix = filesize.pick_unit_and_suffix(total, ["", "K", "M", "G", "T", "P", "E", "Z", "Y"], 1000)
    precision = 0 if scale_unit == 1 else 1
    assert f"{completed/scale_unit:,.{precision}f}/{total/scale_unit:,.{precision}f} {suffix}" == '0.9/0.9 T'

# Generated at 2022-06-22 13:30:57.573993
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(42) == Text("42 /s", style="progress.data.speed")
    assert RateColumn('B').render(42) == Text("42 B/s", style="progress.data.speed")


# Generated at 2022-06-22 13:31:00.613247
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from tqdm.auto import tqdm
    with tqdm(total=100, leave=False) as t:
        for i in range(100):
            t.update(10)

# Generated at 2022-06-22 13:31:11.807960
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Unit testing the method reset() of class tqdm_rich."""
    with tqdm_rich(total=10) as bar:
        # test tqdm_rich with total defined
        bar.reset(total=12)
        assert bar._prog.tasks[bar._task_id].total == 12
        assert bar.total == 12
        # test tqdm_rich with no total defined
        bar.reset()
        assert bar._prog.tasks[bar._task_id].total is None
        assert bar.total is None
        # test tqdm_rich raising error if total is not an integer
        try:
            bar.reset(total=1.2)
        except TypeError:
            pass
        else:
            raise Exception("AssertionError: reset() method should raise TypeError!")



# Generated at 2022-06-22 13:31:14.567143
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render({"speed": 1000, "completed": 10, "total": 10}) == Text("1.0 K/s", style = "progress.data.speed")


# Generated at 2022-06-22 13:31:21.715370
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import sys
    from io import StringIO
    t_str = '12345\r1234 \r123  \r12   \r1    \r'
    t_out = StringIO()
    sys.stdout = t_out
    
    from tqdm import trange
    for i in trange(10, desc=t_str):
        pass
    sys.stdout = sys.__stdout__
    assert t_out.getvalue() == t_str

# Generated at 2022-06-22 13:31:32.653043
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Unit test for method render of class FractionColumn"""
    pc = FractionColumn()
    class TestTask:
        completed = 2000
        total = 5000
    tt = TestTask()
    pc.render(tt)


# Generated at 2022-06-22 13:31:40.689759
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    assert FractionColumn().render(Progress().add_task("", 100, completed=1)) == Text("0.0/1.0 ")
    assert FractionColumn().render(Progress().add_task("", 10**6, completed=10**5)) == Text("0.0/1000.0 K")
    assert FractionColumn().render(Progress().add_task("", 10**9, completed=10**6)) == Text("0.0/1.0 M")

# Generated at 2022-06-22 13:31:44.129633
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = Progress.Task(completed = 1, total = 2)
    fraction = FractionColumn()
    assert fraction.render(task) == Text("0.5/2.0 ", style="progress.download")

# Generated at 2022-06-22 13:31:48.286888
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Test `FractionColumn#render` method"""
    class MockTask(object):
        completed = 1500
        total = 5000
    column = FractionColumn()
    assert column.render(MockTask()) == Text('1.5/5.0 ', style='progress.download')
    column = FractionColumn(unit_scale=True)
    assert column.render(MockTask()) == Text('1.5K/5.0K ', style='progress.download')
    column = FractionColumn(unit_scale=True, unit_divisor=1024)
    assert column.render(MockTask()) == Text('1.5K/5.0K ', style='progress.download')

# Generated at 2022-06-22 13:31:51.698771
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    with tqdm(total=10) as bar:
        for i in range(10):
            bar.update(1)

# Generated at 2022-06-22 13:32:03.209583
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    # The assert of exception is wrong, but it is not necessary to test
    assert FractionColumn(unit_scale=False, unit_divisor=1000).render(0) == Text('0.0/0.0 ', style="progress.download")
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(1) == Text('0.0/0.0 K', style="progress.download")
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(1023) == Text('0.0/0.0 K', style="progress.download")
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(1024) == Text('1.0/1.0 K', style="progress.download")

# Generated at 2022-06-22 13:32:08.035474
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import gc
    try:
        import rich
    except ImportError:
        # local import because of the class TqdmExperimentalWarning
        from . import tqdm
        tqdm_rich = tqdm.tqdm_rich
    else:
        from . import tqdm_rich
    # test _prog is None
    t = tqdm_rich(10)
    t.display()
    t.close()
    # test _prog is not None
    gc.collect()
    t = tqdm_rich(10)
    t._prog = 1
    t.display()
    t.close()

# Generated at 2022-06-22 13:32:20.420575
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.progress import BarColumn, Progress
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.table import Table
    from rich.text import Text
    from rich.columns import Columns
    from tqdm.auto import trange

    console = Console(markup=True)

    progress = Progress("[progress.description]{task.description}",
                        BarColumn(bar_width=None),
                        "[progress.percentage]{task.percentage:>6.2f}%",
                        transient=False)
    progress.__enter__()
    console.print("[green]This is a progress bar:")
    task_id = progress.add_task("Downloading 1.txt", total=5)

# Generated at 2022-06-22 13:32:28.940599
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch  # python2
    from rich.progress import Progress
    t = tqdm_rich([], progress=(), leave=True)
    with patch.object(Progress, '__enter__') as mock_enter, \
            patch.object(Progress, '__exit__') as mock_exit, \
            patch.object(Progress, 'add_task') as mock_add, \
            patch.object(Progress, 'update') as mock_updt:
        t.display()
        mock_enter.assert_called_once()
        mock_exit.assert_not_called()
        mock_add.assert_not_called()
        mock_updt.assert_not_called()


# Generated at 2022-06-22 13:32:35.020760
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rateColumn = RateColumn()
    assert rateColumn.render("None") == Text("? /s", style="progress.data.speed")
    rateColumn = RateColumn(unit = "sec")
    assert rateColumn.render("None") == Text("? sec/s", style="progress.data.speed")

# Generated at 2022-06-22 13:32:49.968411
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich()
    assert hasattr(t, 'display')
    t.close()

# Generated at 2022-06-22 13:32:55.179035
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .tqdm import trange
    from .utils import format_dict
    max_value = 13


# Generated at 2022-06-22 13:33:00.410893
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm_rich(unit='B', unit_scale=True, total=2**64 - 1,
                   ascii=False) as pbar:
        for i in _range(2**64):
            pbar.display()

# Generated at 2022-06-22 13:33:09.414231
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():

    def rounding(number):
        """Round to 1 digit if number > 1, else round to 2 digits."""
        return f"{number:.1f}" if number >= 1. else f"{number:.2f}"

    fc = FractionColumn()
    assert rounding(fc.render(bar(1, 1)).content) == "1.0/1.0"
    assert rounding(fc.render(bar(1, 2)).content) == "1.0/2.0"
    assert rounding(fc.render(bar(1, 10)).content) == "1.0/10.0"
    assert rounding(fc.render(bar(1, 100)).content) == "1.0/100.0"
    assert rounding(fc.render(bar(1, 100)).content) == "1.0/100.0"

# Generated at 2022-06-22 13:33:21.951682
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import sys
    import warnings
    # Context manager
    with warnings.catch_warnings(record=True) as w:
        with tqdm_rich(total=10, unit='B') as bar:
            bar.reset(total=20)
            assert bar.total == 20
            assert bar.n == 0
            bar.update()
            bar.update(2)
            assert bar.n == 2
            assert (w[-1].category == TqdmExperimentalWarning and
                    str(w[-1].message) == 'rich is experimental/alpha')
    # Manually
    bar = tqdm_rich(total=10, unit='B')
    bar.reset(total=20)
    assert bar.total == 20
    assert bar.n == 0
    bar.update()
    bar.update(2)
   

# Generated at 2022-06-22 13:33:34.001204
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():

    # Test using default bars provided by rich (no-op)
    # Test with default number of itereations (total=1)
    with tqdm_rich(total=1) as progress_bar:
        assert progress_bar.total == 1
    # Test with explicit number of iterations (total=10)
    with tqdm_rich(total=10) as progress_bar:
        assert progress_bar.total == 10

    # Test with custom bars provided by user
    # Test with default number of itereations (total=1)

# Generated at 2022-06-22 13:33:45.756878
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = ProgressColumn()
    task.speed = 1.2
    task.total = 20.0
    task.completed = 10.0

    column = RateColumn(unit="B", unit_scale=False, unit_divisor=1000)
    assert column.render(task).text == "1.2 B/s"

    column = RateColumn(unit="B", unit_scale=True, unit_divisor=1000)
    assert column.render(task).text == "0.0 B/s"

    column = RateColumn(unit="B", unit_scale=True, unit_divisor=1024)
    assert column.render(task).text == "0.0 B/s"

    column = RateColumn(unit="B", unit_scale=True, unit_divisor=1.0)
    assert column.render

# Generated at 2022-06-22 13:33:56.488780
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    with Progress(
        "[bold magenta]{task.description}",
        BarColumn(),
        "[green]•{task.percentage:>4.1f}%",
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), ",",
        RateColumn(unit="B"), "]",
    ) as progress:
        for i in tqdm(range(1000000000), desc="Uploading"):
            progress.update(task_id, completed=i)

# Testing if __all__ works
__all__ = [tqdm_rich, trrange, tqdm, trange]
__all__.append(test_RateColumn_render)

if __name__ == "__main__":
    test_RateColumn_render()

# Generated at 2022-06-22 13:34:04.841152
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    BarColumn_render_test1 = \
    FractionColumn(unit_scale=True, unit_divisor=1000).render(
        [1, 0, 1, 0, 1, 1, 0.5, 1, 1]
    )
    assert BarColumn_render_test1 == Text('1.0/1.0 B', style='progress.download'), \
    'The value is not correct'
    BarColumn_render_test2 = \
    FractionColumn(unit_scale=True, unit_divisor=1000).render(
        [1030, 0, 1030, 1, 1030, 1030, 1030.5, 1, 1030]
    )
    assert BarColumn_render_test2 == Text('1.0/1.0 KB', style='progress.download'), \
    'The value is not correct'

# Generated at 2022-06-22 13:34:07.873592
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import pytest
    with pytest.raises(RuntimeError):
        tqdm_rich(10).display()

# Generated at 2022-06-22 13:34:37.436799
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    monitor = tqdm_rich(1)
    monitor.reset()
    monitor.reset(None)
    monitor.reset(1)
    monitor.reset(None, 10)
    monitor.reset(10, None)
    monitor.reset(10, 10)

# Generated at 2022-06-22 13:34:47.923738
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        from rich.progress import Progress
    except ImportError:
        return
    t = tqdm_rich(range(10), disable=True)
    assert isinstance(t._prog, Progress)
    assert t._prog.description == ": "
    assert t._prog.completed == 0
    assert t._prog.total is None
    t.set_description("Test task")
    t.update(5)
    t.set_description("Test task", True)
    assert t._prog.description == "Test task: "
    assert t._prog.completed == 5
    t.set_description("Test task", False)
    assert t._prog.description == "Test task: "
    assert t._prog.completed == 5

# Generated at 2022-06-22 13:34:58.806985
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .tqdm import tnrange
    from .utils import _supports_unicode
    from .utils import FormatStr
    import time

    try:
        tnrange(10, desc="original task", unit_scale=True, unit_divisor=1e6)
        time.sleep(0.2)
    except KeyboardInterrupt:
        pass

# Generated at 2022-06-22 13:35:10.307397
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import rich
    import rich.progress
    import sys

    class MockDisplay(object):
        def __init__(self):
            rich.progress.Progress.__init__(self)
            self.called = 0

        def update(self, *pargs, **kwargs):
            called = rich.progress.Progress.update
            called(self, *pargs, **kwargs)
            self.called += 1

    with MockDisplay() as prog, tqdm_rich(total=1, desc="Progress", leave=True) as tra,\
            tqdm_rich(total=1, desc="Progress", leave=True) as tra_dis:
        assert prog.called == 0
        tra.display()
        tra_dis.display()
        del tra
        del tra_dis
        assert prog.called == 2
        # check if

# Generated at 2022-06-22 13:35:20.747941
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time

    # Test with a progress bar of 10
    progress_bar = tqdm_rich(total=10)
    progress_bar.total = 5
    progress_bar.display()

    # Test with a progress bar of 10
    progress_bar = tqdm_rich(total=100)
    for i in range(10):
        progress_bar.display()

    # Test with a progress bar of 10
    progress_bar = tqdm_rich(total=10)
    progress_bar.display()
    progress_bar.total = 5
    progress_bar.display()

    # Test with a progress bar of 10
    progress_bar = tqdm_rich(total=100)
    progress_bar.display()
    for i in range(10):
        progress_bar.display()

    # Test with a progress bar

# Generated at 2022-06-22 13:35:24.296125
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = Progress().add_task("", total=100)
    task.update(50)
    rate = RateColumn()
    assert rate.render(task) == Text("36.0/s", style="progress.data.speed")


# Generated at 2022-06-22 13:35:33.029505
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for total in [None, 10, 15]:
        try:
            with tqdm(total=total) as t:
                t.update()

            with tqdm(total=total) as t:
                t.update()
                t.reset()

            with tqdm(total=total) as t:
                t.update()
                t.reset(total=total)

            with tqdm() as t:
                t.update()
                t.reset(total=total)

        except Exception as e:
            warn("Error creating/resetting tqdm_rich with total=" +
                 str(total) + ":\n" + str(e), TqdmExperimentalWarning, stacklevel=2)

# Generated at 2022-06-22 13:35:34.297583
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(dict(speed=10)) == '10.0  /s'

# Generated at 2022-06-22 13:35:46.660354
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from tqdm.utils import _term_move_up
    from tqdm.utils import detect_environment
    from .std import tqdm
    import sys

    # Disable tests if rich is not installed
    try:
        from rich.progress import Progress
    except (ImportError, AttributeError):
        return

    bar_format = "{bar}"
    postfix = {'bar': '{bar}'}

    with tqdm(total=100, desc="", leave=False,
              dynamic_ncols=True,
              bar_format=bar_format,
              postfix=postfix) as t:
        t.display()
        lines = []
        lines.append(sys.stderr.write('\r' + _term_move_up() + '\r'))

# Generated at 2022-06-22 13:35:50.853081
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import sys
    progress = tqdm_rich(range(2), file=sys.stdout, desc="Test_description")
    progress.reset(total=100)
    output = sys.stdout.getvalue()
    assert "[" not in output
    assert "]" not in output
    assert "Test_description" in output

# Generated at 2022-06-22 13:36:51.084895
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    # Test exception throwing
    mock_exception = Exception('Mock exception')

    def raise_exception(*args):  # pragma: no cover
        raise mock_exception

    with tqdm_rich(1) as t:
        t.update = raise_exception
        t.display()


if __name__ == "__main__":  # pragma: no cover
    test_tqdm_rich_display()

# Generated at 2022-06-22 13:36:58.053373
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test that resetting tqdm_rich is seamless."""
    t = tqdm_rich(["a", "b"], total=2)
    assert t.last_print_t == 0.1
    t.reset()
    assert t.last_print_t == 0.1
    t.reset(total=5)
    assert t.last_print_t == 0.1
    t.reset(total=5)
    assert t.last_print_t == 0.1

# Generated at 2022-06-22 13:37:01.802801
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from time import sleep
    tq = tqdm_rich(total=100)
    for i in range(10):
        tq.update()
        sleep(0.25)
        tq.reset(total=10)
        tq.reset(total=10)
        sleep(0.25)
        tq.reset(total=10)
        sleep(0.25)
    tq.close()


if __name__ == '__main__':  # pragma: no cover
    main_tqdm_rich_reset()

# Generated at 2022-06-22 13:37:04.796225
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=4) as pbar:
        assert pbar._prog.total == 4
        pbar.reset(total=5)  # New tqdm_rich object must be created
        assert pbar._prog.total == 5

# Generated at 2022-06-22 13:37:12.977309
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fc = FractionColumn(unit_scale=False, unit_divisor=1000)
    class ProgressTest:
        completed = 1
        total = 100
    result = fc.render(ProgressTest)
    assert '1/100' in str(result)
    fc = FractionColumn(unit_scale=True, unit_divisor=1000)
    result = fc.render(ProgressTest)
    assert '1.0/100.0' in str(result)

# Generated at 2022-06-22 13:37:16.262306
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time

    def test_range(n):
        for i in trange(n):
            time.sleep(0.01)

    test_range(10)

# Generated at 2022-06-22 13:37:20.138302
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    p = tqdm_rich()
    try:
        p.display()
        getattr(p, '_task_id')
    except:
        raise Exception('tqdm_rich_display() test failed')

# Generated at 2022-06-22 13:37:31.349516
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    try:
        with tqdm_rich(total=9) as pbar:
            i = 0
            while i < 10:
                time.sleep(0.02)
                if i == 8:
                    pbar.display()
                i += 1
    except Exception:
        pass


if __name__ == "__main__":
    from shutil import get_terminal_size
    from time import sleep

    with Progress() as progress:
        task = progress.add_task("Download", total=10, start=True)
        task.update(completed=0)
        for i in range(1, 10):
            task.update(completed=i)
            sleep(0.05)
        task.update(completed=10)
        input()

# Generated at 2022-06-22 13:37:38.719327
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import rich
    import rich.progress
    import sys
    from tqdm.auto import tqdm, trange

    for _ in trange(4):
        assert rich.progress.Progress.default_console == sys.__stdout__
        import time
        time.sleep(0.5)

    for _ in tqdm(range(4)):
        assert rich.progress.Progress.default_console == sys.__stdout__
        import time
        time.sleep(0.5)