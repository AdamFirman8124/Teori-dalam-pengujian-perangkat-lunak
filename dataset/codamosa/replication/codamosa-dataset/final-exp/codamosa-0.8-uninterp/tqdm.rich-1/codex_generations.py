

# Generated at 2022-06-22 13:27:39.038661
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(total=10) as pbar:
        pbar.clear()
        pbar.update(1)

# Generated at 2022-06-22 13:27:41.928186
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from time import sleep
    for i in tqdm(range(10)):
        assert i == 0
        sleep(0.01)
    for i in tqdm(range(10)):
        assert i == 1
        sleep(0.01)

# Generated at 2022-06-22 13:27:46.687726
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    t = tqdm_rich(range(10), leave=True)
    t.reset()
    assert t.n == 0
    assert t.total == 10
    t.reset(total=100)
    assert t.n == 0
    assert t.total == 100

# Generated at 2022-06-22 13:27:58.062746
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    result = RateColumn(unit="B").render(thread=None, task=None)
    assert result.style == "progress.data.speed"
    assert result.text == "? B/s"

    result = RateColumn(unit="B", unit_scale=True, unit_divisor=1024).render(thread=None, task=None)
    assert result.style == "progress.data.speed"
    assert result.text == "? B/s"

    result = RateColumn(unit="B", unit_scale=True, unit_divisor=1024).render(thread=None, task=None)
    assert result.style == "progress.data.speed"
    assert result.text == "? B/s"


# Generated at 2022-06-22 13:28:02.513682
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    from rich.progress import Progress
    from time import sleep
    with Progress() as progress:
        task = progress.add_task("test", total=3)
        for _ in range(3):
            sleep(1)
            progress.update(task, advance=1)


# Generated at 2022-06-22 13:28:14.811065
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rc = RateColumn()
    assert rc.render(0) == '0.00 /s'
    assert rc.render(1) == '1.00 /s'
    assert rc.render(10) == '10.00 /s'
    assert rc.render(100) == '100.00 /s'
    assert rc.render(-1) == '-1.00 /s'
    assert rc.render(-10) == '-10.00 /s'
    assert rc.render(-100) == '-100.00 /s'
    assert rc.render(0.123456789) == '0.12 /s'
    assert rc.render(1.123456789) == '1.12 /s'
    assert rc.render(10.123456789) == '10.12 /s'

# Generated at 2022-06-22 13:28:23.980024
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Unit test for method display of class tqdm_rich."""
    from .std import tqdm
    with tqdm(total=2) as pbar:
        pbar.display(pbar, 1, 4)
        pbar.display(2, 3, 4)
        pbar.display(3, 4)
    assert pbar.n == 3


if __name__ == "__main__":  # pragma: no cover
    from time import sleep
    with trange(10) as t:
        for i in t:
            sleep(0.1)

# Generated at 2022-06-22 13:28:33.295299
# Unit test for method render of class RateColumn

# Generated at 2022-06-22 13:28:44.937309
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.progress import Progress
    from rich.columns import SpacesColumn
    from rich.text import Text
    from rich.progress import UnknownTimeRemaining

    prog = Progress(SpacesColumn(24), "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), ",", RateColumn(unit="B"), "]")
    prog.__enter__()
    task = prog.add_task("a", total=100)

    task.update(n=0, speed=None)

# Generated at 2022-06-22 13:28:49.820583
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Unit test of method _reset
    """
    old_ = tqdm_rich(total=10)
    old_.update()
    old_.update()
    old_.reset(total=10)
    assert old_.n == 0
    new_ = tqdm_rich(total=10)
    new_.update(8)
    new_.reset()
    assert new_.n == 0

# Generated at 2022-06-22 13:29:07.158832
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from io import StringIO
    import sys
    import unittest

    class TqdmRichDisplayTest(unittest.TestCase):
        """Test display() function of tqdm_rich class."""

        def test_display(self):
            """Test display() function of tqdm_rich class"""
            with StringIO() as sio:
                sys.stdout = sio
                with tqdm(total=2) as pbar:
                    pbar.display()
                    pbar.n = 1
                    pbar.display()
                sys.stdout = sys.__stdout__
                self.assertEqual(sio.getvalue(), "\r                                     \r")

    unittest.main(buffer=True, exit=False)

# Generated at 2022-06-22 13:29:15.651116
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    prg = Progress(
        "[progress.description]{task.description}",
        BarColumn(bar_width=None),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), "]",
    )
    prg.__enter__()

    d = ['a','b','c','d']
    t = tqdm_rich(d, progress=prg)

    t.update()
    t.update()
    t.display()

    t.close()
    prg.__exit__(None, None, None)

# Generated at 2022-06-22 13:29:28.185782
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Progress
    progress = Progress()
    f = FractionColumn(unit_scale=False, unit_divisor=1000)
    f._task = progress._tasks[0]
    f._task.completed = 0
    f._task.total = 0
    f._task.update(completed=1, total=1)
    assert f.render(f._task) == Text('1/1 ', style='progress.download')
    f._task.update(completed=2, total=2)
    assert f.render(f._task) == Text('2/2 ', style='progress.download')
    f._task.update(completed=10, total=20)
    assert f.render(f._task) == Text('0.5/2.0 ', style='progress.download')
    f._task

# Generated at 2022-06-22 13:29:37.023845
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from tqdm.contrib.test import skip_if_disabled
    from tqdm._tqdm_gui import tqdm_gui
    skip_if_disabled()
    for disable in [False, True]:
        for cls in [tqdm_rich, tqdm_gui]:
            for leave in [False, True]:
                with cls(disable=disable, leave=leave) as bar:
                    bar.total = 3
                    bar.update()
                    bar.update()
                    bar.clear()
                    bar.update()

# Generated at 2022-06-22 13:29:42.071699
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """run doctests."""
    import doctest
    doctest.testmod()

    # tqdm_rich is not tested in tests/__main__.py, as it is coupled with
    # rich.progress, and requires a GUI running in order to.
    #
    # For anyone interested in testing manually, set `gui=True` in
    # `python3 -m tqdm.tests.__main__` to show a manual test for tqdm_rich.

# Generated at 2022-06-22 13:29:46.296520
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from io import StringIO
    import sys
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    t = tqdm_rich(1, 1)
    t.close()
    assert capturedOutput.getvalue() == '\x1b[?25h'

# Generated at 2022-06-22 13:29:51.336374
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        progress = Progress()
        progress.__enter__()
        task_id = progress.add_task("test_task")
        progress.update(task_id, completed=1, description="test_task")
    finally:
        progress.__exit__(None, None, None)

# Generated at 2022-06-22 13:29:56.569619
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    class Task():
        completed = 123.45
        total = 678.90
    task=Task()
    r1=Text(
            f"{task.completed:,.0f}/{task.total:,.0f} ",
            style="progress.download")
    r2=FractionColumn().render(task)
    assert (r1.plain_text == r2.plain_text)


# Generated at 2022-06-22 13:30:09.193005
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.text import Text
    from rich.progress import ProgressColumn
    from rich.progress import Progress
    from rich.progress import TaskID
    from rich.markup import Markup
    from rich.console import Console

    # Create a task id
    progress = Progress('', transient=True)
    task_id = progress.add_task('', total=1)

    # Create a FractionColumn
    fraction_column = FractionColumn()

    # Get the output of FractionColumn
    # Note, the task id is a data-structure which is hard to construct
    # We will try to construct one resembling the real one
    task_id.total = 1.0
    task_id.completed = 0.5
    output = fraction_column.render(task_id)

    # The output is a Text

# Generated at 2022-06-22 13:30:19.667755
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    bar1 = tqdm(total=10)
    bar2 = tqdm_rich(total=10)
    bar1.reset(total=20)
    bar2.reset(total=20)
    bar1.reset()
    bar2.reset()
    if not hasattr(bar1, '_instances'):
        bar1._instances = []
    if not hasattr(bar1, '_leave_last'):
        bar1._leave_last = False
    if not hasattr(bar2, '_instances'):
        bar2._instances = []
    if not hasattr(bar2, '_leave_last'):
        bar2._leave_last = False
    assert bar1._instances == bar2._instances
    assert bar1._leave_last == bar2._leave_last
   

# Generated at 2022-06-22 13:30:37.496133
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm([1, 2, 3])
    t.set_description('foo')
    t.display()
    t.close()
    t = tqdm(disable=True, ncols=80)
    t.disable = False
    t.display()
    t.close()
    t.disable = True
    t.display()
    t.close()
    t = tqdm(total=5, disable=True)
    t.disable = False
    t.n = 5
    t.display()
    t.close()
    t.disable = True
    t.n = 1
    t.display()
    t.close()
    t = tqdm(total=5, disable=True)
    t.disable = False
    t.n = 1
    t.display()

# Generated at 2022-06-22 13:30:41.766694
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    column_result = rate_column.render(4000)
    assert column_result.text == "4.0 /s"
    assert column_result.markup == "/s"

# Generated at 2022-06-22 13:30:49.589463
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.console import Console
    from rich import box
    from rich.progress import increment, TaskID
    from rich.panel import Panel
    from rich.table import Table
    import time
    import json
    import sys

    def _callback(task_id, total, completed, desc, **_):
        progress = progress_dict[task_id]

        progress.console.print(
            progress.console.get_console_width() * " " + "\r",
            end="")
        progress.console.print(
            "TaskID: ",
            task_id,
            " - Total: ",
            total,
            " - Completed: ",
            completed,
            " - Total Completed: ",
            progress.total_completed,
            " - Desc: ",
            desc,
            "\r",
            end=""
        )



# Generated at 2022-06-22 13:30:54.874021
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Unit testing the method reset of class tqdm_rich
    """
    a = tqdm_rich(total=10)
    assert(a._prog.total == 10)
    a.reset(total=3)
    assert(a._prog.total == 3)
    a.close()

# Generated at 2022-06-22 13:30:59.154233
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    assert FractionColumn().render(10.0) == Text(
        "10.0/10.0 ", style="progress.download")
    assert FractionColumn(unit_scale=True, unit_divisor=1024).render(1000.0) == Text(
        "0.977/0.977 K", style="progress.download")

# Generated at 2022-06-22 13:31:10.123316
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="B")
    assert rate_column.render(task=None) == Text("0.0 B/s", style="progress.data.speed")
    rate_column = RateColumn(unit="B", unit_scale=True, unit_divisor=1024)
    assert rate_column.render(task=None) == Text("0.0 B/s", style="progress.data.speed")
    rate_column = RateColumn(unit="B", unit_scale=True, unit_divisor=1000)
    assert rate_column.render(task=None) == Text("0.0 B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:31:13.708022
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=10, desc='Test reset') as pbar:
        for i in range(5):
            pbar.reset(total=i)

# Generated at 2022-06-22 13:31:22.638498
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    class _tqdm_rich(tqdm_rich):
        def __init__(self, *args, **kwargs):
            super(_tqdm_rich, self).__init__(*args, **kwargs)
            self._prog = None

    with patch('tqdm._tqdm.tqdm_rich._prog', '_prog'):
        _tqdm_rich(disable=True).display()
        _tqdm_rich(disable=False).display()

# Generated at 2022-06-22 13:31:33.807742
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import sys
    import random
    # testing progress bar
    with tqdm(total=10, desc="Hello World!", unit_scale=True) as pbar:
        for i in range(10):
            pbar.update(1)
    assert sys.stdout.isatty()

    with tqdm(total=10, desc="Hello World!", unit_scale=False) as pbar:
        for i in range(10):
            pbar.update(1)
    assert sys.stdout.isatty()

    # test with looping
    with tqdm(total=100, desc="Hello World!", unit_scale=False) as pbar:
        for i in range(100):
            pbar.update(1)
    assert sys.stdout.isatty()

    # test with random sampling

# Generated at 2022-06-22 13:31:39.081279
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = trange(10)
    task.total = 100
    task.completed = 50
    assert FractionColumn().render(task) == Text("0.5/1.0 ", style="progress.download")

test_FractionColumn_render()

# Generated at 2022-06-22 13:31:44.824417
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        import rich.progress
        rich.progress.Progress()
    except ImportError:
        return
    else:
        t = tqdm_rich(total=100)
        t.display()
        t.close()

# Generated at 2022-06-22 13:31:45.787501
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # TODO: Write test
    pass

# Generated at 2022-06-22 13:31:51.035589
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    t = tqdm(total=10)
    t.reset(total=20)
    assert t.total == 20, t.total
    assert t._prog.total == 20, t._prog.total

    t = tqdm(total=10)
    t.reset()
    assert t.total == 10, t.total
    assert t._prog.total == 10, t._prog.total

    t = tqdm(range(10))
    t.reset(total=20)
    assert t.total == 20, t.total
    assert t._prog.total == 20, t._prog.total

    t = tqdm(range(10))
    t.reset()
    assert t.total == 10, t.total
    assert t._prog.total == 10, t._prog.total

# Generated at 2022-06-22 13:31:52.173464
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    for _ in trange(1):
        pass

# Generated at 2022-06-22 13:32:04.393727
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    # Test 1: new total greater than old total
    with tqdm_rich(total=10, unit_scale=True, leave=False) as t:
        t.reset(total=100)
        assert t.total == 100

    # Test 2: new total less than old total
    with tqdm_rich(total=50, unit_scale=True, leave=False) as t:
        t.reset(total=5)
        assert t.total == 5

    # Test 3: new total equal to old total
    with tqdm_rich(total=10, unit_scale=True, leave=False) as t:
        t.reset(total=10)
        assert t.total == 10

    # Test 4: new total not specified (same as old total)

# Generated at 2022-06-22 13:32:16.409028
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from time import time
    from .std import open as gopen
    import os

    with gopen('test_file', 'w') as fp:
        fp.write('1' * 100)
    stat = os.stat('test_file')
    size = stat.st_size


# Generated at 2022-06-22 13:32:19.299125
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm_rich(total=10) as t:
        for i in range(10):
            t.update(1)

# Generated at 2022-06-22 13:32:20.027073
# Unit test for method render of class RateColumn

# Generated at 2022-06-22 13:32:22.249114
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=10) as pbar:
        pbar.update(5)
        pbar.reset()
        pbar.update(3)

# Generated at 2022-06-22 13:32:32.683782
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    class Task(object):
        def __init__(self, speed):
            self.speed = speed

    task = Task(1024**3)
    assert RateColumn(unit="bytes", unit_scale=True).render(task) == Text("1.0 GiB/s", style="progress.data.speed")
    task = Task(1024**2)
    assert RateColumn(unit="B", unit_scale=False).render(task) == Text("1.0 KB/s", style="progress.data.speed")
    task = Task(None)
    assert RateColumn(unit="B", unit_scale=False).render(task) == Text("? B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:32:54.186612
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from contextlib import contextmanager
    import sys
    import os

    @contextmanager
    def captured_output():
        new_out, new_err = os.pipe()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = os.fdopen(new_out, 'w'), os.fdopen(new_err, 'w')
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err


# Generated at 2022-06-22 13:33:05.994420
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Test if values are correctly formatted.
    """
    r = RateColumn()
    assert r.render(None) == Text(f"? ", style="progress.data.speed")
    assert r.render(0) == Text(f"0 ", style="progress.data.speed")
    assert r.render(1.0) == Text(f"1 ", style="progress.data.speed")
    assert r.render(1.1) == Text(f"1.1 ", style="progress.data.speed")
    assert r.render(1000) == Text(f"1K ", style="progress.data.speed")
    assert r.render(1100) == Text(f"1.1K ", style="progress.data.speed")

# Generated at 2022-06-22 13:33:09.202207
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.panel import Panel
    from rich.progress import Task
    task = Task(description="test", completed=7, total=10, start=True)
    assert str(FractionColumn().render(task)) == str(Panel("0.7/1.0"))

# Generated at 2022-06-22 13:33:15.382036
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """ En especial para pruebas con python3.6+ """
    p = tqdm_rich(total=100)
    p.set_description("Prueba")
    for i in p:
        p.n = i
        continue

if __name__ == "__main__":
    test_FractionColumn_render()

# Generated at 2022-06-22 13:33:24.741734
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    task = {'speed': 1000}
    assert rate_column.render(task) == Text(
        f"{1000:,.0f} /s", style="progress.data.speed")
    rate_column = RateColumn(unit="B")
    task = {'speed': 1000}
    assert rate_column.render(task) == Text(
        f"{1000:,.0f} B/s", style="progress.data.speed")
    rate_column = RateColumn(unit="B", unit_scale=True)
    task = {'speed': 1000}
    assert rate_column.render(task) == Text(
        f"{1000:,.0f} /s", style="progress.data.speed")
    rate_column = RateColumn(unit="B", unit_scale=True)


# Generated at 2022-06-22 13:33:29.696710
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=10) as t:
        for i in range(5):
            assert t.n == i
            t.update()
        t.reset(total=5)
        for i in range(5):
            assert t.n == i
            t.update()
    assert t.n == 10


if __name__ == "__main__":  # pragma: no cover
    total = 100
    with tqdm(total=total, desc="Hello") as pbar:
        for i in pbar:
            pbar.set_description("World")
            pbar.set_postfix({"abc": 123, "def": 456})
            pbar.update()
    total = 500000

# Generated at 2022-06-22 13:33:37.065331
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    # to disable issue https://github.com/casperdcl/tqdm/issues/539
    total_default = 10000
    total = 100
    # we expect that total must be given by 100
    # we expect that the count of iteration is 100
    # we expect that the last message is "99it"
    # we expect that reset use total given by the user
    # we expect that total_default is not used
    # we expect that reset always set total to 100

# Generated at 2022-06-22 13:33:48.179041
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """
    This test should be called from the parent directory.
    The following command from the parent directory should call this test:
    python3 -m tqdm.rich.tests.test_rich
    """
    try:
        from rich.progress import Progress
    except ImportError:
        return

    kwargs = {
        'total': 10,
        'gui': True,
        'disable': False
    }

    bar = tqdm_rich(**kwargs)
    # Normal update
    bar.update(5)
    assert bar.n == 5
    assert bar._task_id == bar._prog.get_task()['id']
    assert bar.desc == ''

    # Update with nested total
    nested_total = 20

# Generated at 2022-06-22 13:33:52.332739
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import locale
    locale.setlocale(locale.LC_ALL, '')
    with tqdm_rich(total=100) as t:
        for i in t:
            t.set_description("The current number is: %s" % i)
            t.update()

# Generated at 2022-06-22 13:33:54.924242
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test method display of class tqdm_rich."""
    iteration = [0, 1, 2, 3]
    with tqdm(iteration) as bar:
        for _ in bar:
            pass

# Generated at 2022-06-22 13:34:19.511165
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import decorate_clone
    for i in tqdm_rich(range(2)):
        if i == 0:
            pass
        elif i == 1:
            # Reset the parent instance of the loop
            tqdm_rich.reset(tqdm_rich())
        pass
    # Should not raise
    tqdm_rich(range(2)).__exit__()
    # Should not raise
    decorate_clone(range(2), tqdm_rich).__exit__()


if __name__ == '__main__':
    print("This script should be run with `python -m tqdm.rich`")

# Generated at 2022-06-22 13:34:21.828854
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from .std import tqdm
    import time
    for _ in tqdm(range(100)):
        time.sleep(0.01)

# Generated at 2022-06-22 13:34:25.553741
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    iterator_1 = (i for i in range(10))
    iterator_2 = (i for i in range(10))

    pbar_1 = tqdm(iterator_1, total=10, desc='first loop')
    for _ in pbar_1:
        pass

    pbar_2 = tqdm(iterator_2, total=10, desc='second loop')
    for _ in pbar_2:
        pass

# Generated at 2022-06-22 13:34:36.174449
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import time
    import rich
    import rich.progress
    import tqdm.rich
    import warnings

    warnings.simplefilter("ignore")

    task = rich.progress.ProgressTask(completed=1, speed=1, start_time=time.time())

    percent = tqdm.rich.RateColumn()
    assert percent.render(task) == rich.Text("1.0 B/s", style="progress.data.speed")

    percent = tqdm.rich.RateColumn(unit_scale=True)
    assert percent.render(task) == rich.Text("1.0 B/s", style="progress.data.speed")

    percent = tqdm.rich.RateColumn(unit_divisor=1024)

# Generated at 2022-06-22 13:34:47.130996
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        from time import sleep
    except ImportError:
        return

    with tqdm_rich(total=10, desc="foo") as pbar:
        for i in _range(10):
            sleep(0.01)
            pbar.display(desc="bar")
            assert pbar.desc == "bar"
            pbar.update()
        assert pbar.n == 10
        assert pbar.total == 10
        assert pbar.last_print_n != pbar.n
        assert pbar.last_print_n != pbar.total
        pbar.display()
        assert pbar.last_print_n == pbar.n
        assert pbar.last_print_n == pbar.total
        pbar.display(n=pbar.last_print_n)

# Generated at 2022-06-22 13:34:57.744714
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import random  # random.randrange
    random.seed(0)
    # test RateColumn when bytesize is True
    #test_cases = [(1024, False, 1, 'B'),
                  #(1024, False, 1000, 'B'),
                  #(10**3, False, 1, 'B'),
                  #(10**3, False, 1000, 'B'),
                  #(10**6, False, 1, 'B'),
                  #(10**6, False, 1000, 'B'),
                  #(10**9, False, 1, 'B'),
                  #(10**9, False, 1000, 'B'),
                  #(2**10, False, 1, 'B'),
                  #(2**10, False, 1000, 'B'),
                  #(2**20, False, 1, 'B'),
                  #(2**

# Generated at 2022-06-22 13:35:00.406841
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    try:
        tqdm_rich(total=1).display()
    except Exception as e:
        assert "hasattr(self, '_prog')" in str(e)

# Generated at 2022-06-22 13:35:11.710808
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import BarColumn, TimeElapsedColumn, TimeRemainingColumn
    from rich.progress import PercentageColumn
    p = Progress(
        Text("[progress.description]{task.description}"),
        PercentageColumn(),
        "|",
        BarColumn(bar_width=None),
        "|",
        Text("[", TimeElapsedColumn(), "<", TimeRemainingColumn(), "]"),
    )
    p.__enter__()
    t = p.add_task("test", total=10)

    # test reseting with total (i.e. progress.main(total=...))
    p.update(t, completed=0)
    p.update(t, completed=1)
    p.update(t, completed=2)
    p.update(t, total=10)

# Generated at 2022-06-22 13:35:15.582420
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover # testing-only
    with tqdm_rich(total=100, disable=True) as t:
        for i in _range(100):
            t.n = i
            t.display()

if __name__ == "__main__":
    test_tqdm_rich_display()

# Generated at 2022-06-22 13:35:25.303591
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress = Progress(
        "[progress.description]{task.description}",
        "[progress.percentage]{task.percentage:>3.0f}%",
        BarColumn(bar_width=None),
        "[", TimeElapsedColumn(), ",", RateColumn(unit="B", unit_scale=True), "]",
    )
    progress.__enter__()
    task_id = progress.add_task(
        "Downloading content.bin…",
        total=filesize.parse("100M"),
        completed=filesize.parse("50M"),
    )
    progress.update(task_id, completed=filesize.parse("51M"))
    progress.__exit__(None, None, None)

# Generated at 2022-06-22 13:36:15.229636
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import os

    with open('test_tqdm_rich_display.txt', 'w') as f:
        f.write("test")

    with tqdm_rich(total=os.stat("test_tqdm_rich_display.txt").st_size) as t:
        with open("test_tqdm_rich_display.txt") as fi:
            t.update(t.total - t.n)
            for i in fi:
                pass

    os.remove("test_tqdm_rich_display.txt")


# Generated at 2022-06-22 13:36:24.859253
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = std_tqdm(range(10))
    task.n = 5
    task.last_print_n = 0
    task.start_t = 1596610057.81414
    task.last_print_t = 1596610057.81414
    task.smoothing = 0
    task.remote_size = None
    task.disable = False
    task.unit = 'bytes'
    task.unit_scale = False
    task.unit_divisor = 1000
    task.format_dict = {'n': 5, 'total': 9, 'elapsed': 0.5895171165466309, 'percentage': 55.55555555555556, 'desc': '', 'rate': 8.478035475600917}
    task.write = std_tqdm.write
   

# Generated at 2022-06-22 13:36:33.597875
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import _range
    from .gui import tqdm_gui
    import time
    # use tqdm_gui to cleanup the progress bar
    with tqdm_gui(total=100) as pbar:
        # DEBUG
        # pbar.display()
        for _ in _range(100):
            pbar.update(1)
            # delay 0.5 seconds to show the progress bar
            time.sleep(0.5)


if __name__ == '__main__':
    test_tqdm_rich_display()

# Generated at 2022-06-22 13:36:41.409568
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import tqdm

    with tqdm(0, file=None) as bar:
        bar.write("Hello")
        bar.write("\rWorld\n")
        bar.write("!")

    with tqdm(0, file=None, ascii=False) as bar:
        bar.write("Hello")
        bar.write("\rWorld\n")
        bar.write("!")

    with tqdm(0, file=None, disable=True) as bar:
        bar.write("Hello")
        bar.write("\rWorld\n")
        bar.write("!")

# Generated at 2022-06-22 13:36:46.712432
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.console import Console
    from rich.progress import TaskID
    task = TaskID()
    console = Console()
    v = tqdm_rich(disable=True)
    v._prog = Progress(console, task)
    v.close()
    v.display()
    v.reset()


# Generated at 2022-06-22 13:36:50.815199
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    with tqdm_rich(total=100) as t:
        for i in range(10):
            time.sleep(0.1)
            t.update(10)
        assert t.n == 100

# Generated at 2022-06-22 13:36:53.969997
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    c = RateColumn(unit="B", unit_scale=False, unit_divisor=1000)
    assert '1.0 B/s' == c.render(Progress.task)



# Generated at 2022-06-22 13:37:04.214704
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Unit test for method 'display' of class 'tqdm_rich'."""
    from textwrap import dedent
    import sys
    import subprocess
    from os import devnull

    with open(devnull, 'w') as fnull:
        outs = subprocess.check_output(
            'python -m tqdm',
            stderr=subprocess.STDOUT,
            shell=True,
            universal_newlines=True,
        )
    try:
        from rich.progress import Progress, Text
    except ImportError:
        raise ImportError("rich not found (try `pip install rich`)")


# Generated at 2022-06-22 13:37:07.928377
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    speed = 1.
    assert RateColumn(unit='KiB', unit_scale=False, unit_divisor=1024).render(speed)


# Generated at 2022-06-22 13:37:14.264578
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import subprocess
    import time
    with subprocess.Popen(
            ['python', '-c',
             'import time;'
             'from tqdm import trange;'
             'for _ in trange(5):;'
             '    time.sleep(1);'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL) as proc:
        for _ in trange(5):
            time.sleep(1)
    assert proc.poll() == 0