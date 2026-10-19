

# Generated at 2022-06-22 13:27:45.489424
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm(total=5) as t:
        for i in range(5):
            t.update(1)

# Generated at 2022-06-22 13:27:57.316481
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import unittest


# Generated at 2022-06-22 13:28:09.415260
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from io import StringIO
    # IOError: [Errno 9] Bad file descriptor
    import sys
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    def call_tqdm_rich_display(unused_arg, **kwargs):
        with patch('sys.stderr', new=StringIO()) as fake_stderr:
            with tqdm_rich(**kwargs) as prog:
                prog.display()

    # error message: [Errno 9] Bad file descriptor
    _, _, test_exception = sys.exc_info()

# Generated at 2022-06-22 13:28:15.105435
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit_scale=True, unit_divisor=1024)
    task = type('', (object,), {'speed': 123456789, 'desc': 'test'})()
    assert rate_column.render(task) == Text('117.7 Mbit/s', style='progress.data.speed')

# Generated at 2022-06-22 13:28:27.751895
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.progress import interact
    from rich.table import Column, Table
    from time import sleep

    class tqdm_rich_test(tqdm_rich):
        def display(self, *_, **__):
            if getattr(self, "_prog", None) is not None:
                self._prog.update(self._task_id,
                                  description=self.desc or "",
                                  **self.format_dict)

    if __name__ == "__main__":
        with tqdm_rich_test(range(10), desc="Rich:") as t:
            for i in t:
                sleep(0.01)

        def render_table(task):
            table = Table(
                show_header=False,
                show_edge=False,
            )

# Generated at 2022-06-22 13:28:36.370920
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    pbar = tqdm_rich(total=10)
    assert pbar.total == 10
    pbar.reset(total=20)
    assert pbar.total == 20
    pbar.reset(total=20)  # invalidate the cache
    assert pbar.total == 20
    pbar.reset(total=None)
    assert pbar.total is None
    pbar.reset(total=0)
    assert pbar.total == 0


# Generated at 2022-06-22 13:28:43.332832
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .tests_tqdm import pretest_tqdm, posttest_tqdm, with_bar_width

    @with_bar_width(50)
    def test_reset(bar_width):
        total = 999
        desc = "Rich reset"
        pretest_tqdm(total, desc)
        for i in tqdm_rich(_range(total), desc=desc, leave=False):
            # test `reset()`
            i += 1  # clever way to get the loop executed twice
            tqdm.reset(total=total)
            pretest_tqdm(total, desc)
        posttest_tqdm(total, bar_width, desc)

    test_reset()

# Generated at 2022-06-22 13:28:48.468423
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with trange(10) as t:
        for i in t:
            if i == 5:
                # reset the tqdm object
                t.reset(total=5)
                # add some description
                t.set_description("test_tqdm_rich_reset")
                for j in range(5):
                    t.update()

if __name__ == '__main__':
    test_tqdm_rich_reset()

# Generated at 2022-06-22 13:28:51.506709
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    progressColumn = FractionColumn()
    task = object()
    task.completed = 0.5
    task.total = 2.3
    assert progressColumn.render(task) == Text("0.5/2.3 ", style="progress.download")


# Generated at 2022-06-22 13:28:54.686812
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from .std import tqdm
    p = tqdm(total=2, desc='downloading', leave=False, disable=False, unit_scale=True)
    p.update(1)
    p.close()


# Generated at 2022-06-22 13:29:08.565152
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    # resets to 0 iterations for repeated use
    #   Parameters
    #   ----------
    #   total  : int or float, optional. Total to use for the new bar.
    from random import sample
    from string import ascii_lowercase

    for i in trange(2):
        for j in trange(10, desc='[%d]' % i):
            for k in trange(3):
                sample(ascii_lowercase, 2)
        trange(10).reset()

    if __name__ == "__main__":
        trange = trange(9)
        for i in trange:
            pass
        # tqdm.write("tqdm.write() is available in this mode.")
        trange.reset()
        for i in trange:
            pass

# Generated at 2022-06-22 13:29:18.822395
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import io
    import sys
    import unittest
    with unittest.mock.patch.object(sys, 'stdout', new_callable=io.StringIO) as fake_out:
        tqdm_obj = tqdm.tqdm(total=10)
        for i in range(5):
            tqdm_obj.update()
        tqdm_obj.reset(total=5)
        for i in range(5):
            tqdm_obj.update()
            progress_got = fake_out.getvalue()
        tqdm_obj.close()

# Generated at 2022-06-22 13:29:22.949831
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for _ in tqdm_rich(total=10):
        if _ == 5:
            break
    tqdm_rich.reset(total=20)
    for _ in tqdm_rich:
        if _ == 10:
            break

# Generated at 2022-06-22 13:29:35.283967
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.text import Text
    from rich.progress import Progress
    from rich.progress import ProgressColumn
    from rich.progress import BarColumn
    from rich.progress import TimeElapsedColumn
    from rich.progress import TimeRemainingColumn
    def test1():
        rc = RateColumn()
        assert rc.render(Progress().add_task("Task1")) == Text("? /s", style="progress.data.speed")
    def test2():
        rc = RateColumn()
        p = Progress()
        assert rc.render(p.add_task("Task2")) == Text("? /s", style="progress.data.speed")
    def test3():
        rc = RateColumn()
        p = Progress()
        p.update(1, speed=10)

# Generated at 2022-06-22 13:29:43.276643
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.progress import Task
    task = Task(None, total=1.0, progress=0.5, speed=1000)
    assert RateColumn().render(task) == Text("1.0 K/s", style="progress.data.speed")
    assert RateColumn(unit_scale=True).render(task) == Text("1.0 K/s", style="progress.data.speed")
    assert RateColumn(unit='B').render(task) == Text("1.0 KB/s", style="progress.data.speed")
    assert RateColumn(unit_scale=True, unit='B').render(task) == Text("1.0 KB/s", style="progress.data.speed")

# Generated at 2022-06-22 13:29:54.127429
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # define a task
    class Task:
        def __init__(self, speed):
            self.speed = speed
    # test the cases
    a_task = Task(speed=100)
    assert RateColumn().render(a_task) == Text(f"100 B/s", style="progress.data.speed")
    assert RateColumn(unit_scale=True).render(a_task) == Text(f"0.1 K/s", style="progress.data.speed")
    assert RateColumn(unit_scale=True, unit='b').render(a_task) == Text(f"0.1 Kb/s", style="progress.data.speed")
    assert RateColumn(unit_divisor=1024).render(a_task) == Text(f"0.1 K/s", style="progress.data.speed")
   

# Generated at 2022-06-22 13:29:56.612447
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich(0)
    t._prog.__exit__(None, None, None)
    t._prog = None
    t.display()



# Generated at 2022-06-22 13:30:01.196948
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    column = RateColumn(unit="B")
    task = tqdm()
    assert column.render(task) == Text("? B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:30:03.334783
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    a = tqdm(range(100))
    for _ in a:
        pass
    a.close()

# Generated at 2022-06-22 13:30:12.474690
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich import box
    from rich.columns import Columns
    from rich.table import Table

    def print_table(title, header, data, footer=None):
        """Print table."""
        columns = Columns(data, titles=header, box=box.SQUARE)
        print(Table.grid(columns, box=box.SQUARE, title=title))

    class Task():
        """Mock up a task class."""
        def __init__(self, completed, total):
            """Initialize task class."""
            self.completed = completed
            self.total = total

    task = Task(completed=124, total=4000)
    header = ["Column"]
    data = [["FractionColumn"]]
    c = FractionColumn()

# Generated at 2022-06-22 13:30:23.454295
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert str(RateColumn.render(RateColumn(), 1.1)) == "<Text:1.1 /s>"
    assert str(RateColumn.render(RateColumn(), 1.1 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000)) == "<Text:1.1 y /s>"

# Generated at 2022-06-22 13:30:28.169038
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=10) as pbar:
        assert pbar.total == 10
        pbar.reset(total=20)
        assert pbar.total == 20

# Generated at 2022-06-22 13:30:37.586305
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Unit test for method render of class RateColumn."""
    task = tqdm_rich()
    task.speed = 2**20
    task.total = 2**20
    rc = RateColumn()
    assert rc.render(task) == Text("2.0 MB/s", style="progress.data.speed")
    rc = RateColumn(unit_scale=True)
    assert rc.render(task) == Text("1.9 MB/s", style="progress.data.speed")
    rc = RateColumn(unit="/s")
    assert rc.render(task) == Text("2.0 MB/s/s", style="progress.data.speed")

# Generated at 2022-06-22 13:30:40.786575
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    std_tqdm.display = tqdm_rich.display
    std_tqdm(total=10).display()

# Generated at 2022-06-22 13:30:44.849412
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    from .tests._utils import _mock_tqdm

    with _mock_tqdm(tqdm_rich) as mock:
        for _ in tqdm_rich("hi"):
            pass
        assert mock.display.called



# Generated at 2022-06-22 13:30:56.731893
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import sys
    from tqdm.auto import tqdm_cls

    class MockTqdmRich(tqdm_rich):
        def display(self, *_, **__):
            pass

    with MockTqdmRich(total=10):
        pass

    with tqdm_cls(total=10, disable=False) as t:
        pass

    with tqdm_cls(total=10, disable=True) as t:
        pass

    class MockTqdm(tqdm_cls):
        def display(self, *_, **__):
            pass

    with MockTqdm(total=10):
        pass

    with MockTqdm(total=10, disable=False) as t:
        pass


# Generated at 2022-06-22 13:31:02.219633
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # '\u001b[?25l' is the ESC sequence to hide the cursor
    # '\x1b[?25h' is the ESC sequence to show the cursor
    from rich.progress import Progress
    with Progress(
        "Query progress",
        transient=True
    ) as progress_bar:
        for _ in tqdm_rich(
            ["Sending query...", "Reading results..."],
            progress=progress_bar
        ):
            pass

if __name__ == '__main__':
    test_tqdm_rich_display()

# Generated at 2022-06-22 13:31:06.882468
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = lambda: None
    task.completed = 1
    task.total = 2
    expected = '0.5/2.0 '
    actual = FractionColumn().render(task)

    assert actual == expected


# Generated at 2022-06-22 13:31:18.340104
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=10, unit_scale=True) as t:
        # Before reset
        assert t.total == 10
        assert t._dynamic_total == False
        assert t._dynamic_miniters == False
        # Check if reset resets everything as expected
        t.reset(total=10)
        assert t.total == 10
        assert t._dynamic_total == False
        assert t._dynamic_miniters == False
        # Check if reset resets the total with dynamic_total
        t.reset()
        assert t.total == 10
        assert t._dynamic_total == True
        assert t._dynamic_miniters == True
        t.reset(total=20)
        assert t.total == 20
        assert t._dynamic_total == True
        assert t._dynamic

# Generated at 2022-06-22 13:31:27.768570
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    >>> from tqdm.rich import tqdm_rich
    >>> from tqdm import trange
    >>> for i in trange(10, desc='foo', unit='i'):
    ...     _ = i
    ...
    >>> for i in trange(5, desc='bar', unit='i'):
    ...     _ = i
    ...
    >>> for i in trange(7, desc='baz', unit='i'):
    ...     _ = i
    ...
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()