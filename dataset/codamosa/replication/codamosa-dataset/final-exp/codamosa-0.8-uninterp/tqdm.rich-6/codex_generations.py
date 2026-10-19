

# Generated at 2022-06-22 13:27:39.979321
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import random
    with tqdm(total=random.randint(100, 200)) as t:
        assert t.total == t.n
        t.reset(100)
        assert t.total == t.n

# Generated at 2022-06-22 13:27:50.925894
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    class FakeTask:
        completed = None
        total = None
        speed = None


# Generated at 2022-06-22 13:27:55.055714
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # Simple test for `tqdm` class' `display` method.
    from time import sleep
    for i in tqdm_rich(range(10), desc="test_tqdm_rich_display"):
        sleep(0.01)

# Generated at 2022-06-22 13:27:58.730008
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    with tqdm_rich(total=10) as pbar:
        for i in pbar:
            assert pbar.n == i
            pbar.display()
    assert pbar.n == 10

# Generated at 2022-06-22 13:28:11.222239
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    warn("rich is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
    import time
    from rich.console import Console
    from rich.progress import Progress
    console = Console()
    progress = Progress(
        "(progress.description){task.description}",
        progress=BarColumn(bar_color="progress.task")
    )
    with progress:
        task = progress.add_task("Uploading", start=0, total=100)
        while task.completed < 100:
            time.sleep(0.1)
            task.update(increment=10)
    time.sleep(1)
    console.print(progress)
    time.sleep(1)
    progress.close()
    time.sleep(1)
    progress.__exit__()


# Generated at 2022-06-22 13:28:14.964541
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with trange(10) as t:
        t.set_description('Foo')
        for i in t:
            t.reset(total=4)
            for _ in t:
                pass

# Generated at 2022-06-22 13:28:18.795151
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    # Must not crash
    t = tqdm_rich(total=10, desc="test")
    t.display()
    t.display(10)
    t.display(10, 1.0)

# Generated at 2022-06-22 13:28:30.550757
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Test for RateColumn.
    """
    assert RateColumn().render(0) == "? B/s"
    assert RateColumn("", unit_scale=False, unit_divisor=1000).render(0) == "? B/s"
    assert RateColumn("", unit_scale=False, unit_divisor=1024).render(0) == "? B/s"
    assert RateColumn("", unit_scale=True, unit_divisor=1000).render(0) == "? B/s"
    assert RateColumn("", unit_scale=True, unit_divisor=1024).render(0) == "? B/s"

    assert RateColumn().render(1000) == "? K/s"
    assert RateColumn("", unit_scale=False, unit_divisor=1000).render(1000)

# Generated at 2022-06-22 13:28:36.316839
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    """
    Test method close of class tqdm_rich
    """
    with tqdm_rich(total=10) as progress:
        for _idx in progress:
            pass

    assert progress.n == 10
    assert progress.last_print_n == 10

# Generated at 2022-06-22 13:28:43.961913
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import TaskID

    progress_column = FractionColumn()
    task = TaskID(description="Dummy task", completed=0, total=10)

    # Test for rendering the first unit.
    assert "0.0/10 " == progress_column.render(task).text
    task.completed = 35
    assert "3.5/10 " == progress_column.render(task).text

    # Test for rendering the second unit.
    task.completed = 1012
    assert "1.0/10.1 K" == progress_column.render(task).text

    # Test for rendering the third unit.
    task.completed = 10120000
    assert "0.1/10.1 M" == progress_column.render(task).text


# Generated at 2022-06-22 13:28:54.845308
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        tqdm(0)
    except AttributeError:
        print("No gui available, skipping test")
        return
    with tqdm(10) as pbar:
        for _ in range(5):
            pbar.set_description("foo bar")
        for _ in range(5):
            pbar.set_description("foo bar baz")

# Generated at 2022-06-22 13:29:03.277254
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.progress import Progress
    from rich.syntax import Syntax
    progress = Progress(
        rate=RateColumn(unit="B/s", unit_scale=True, unit_divisor=1000))
    with progress:
        for task in progress.add_task("...", total=20):
            task.update()
            task(speed=1000)
            break
    progress.console.print(Syntax("<bold><green>Done!</green></bold>"))
    progress.console.rule()

# Generated at 2022-06-22 13:29:07.698004
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    import tempfile
    try:
        f = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
        f.close()
        t = tqdm(total=None, file=f)
        t.clear()
        #f.close() # Comment out file close to prevent PermissionError
    except PermissionError:
        pass
    else:
        assert False

# Generated at 2022-06-22 13:29:15.498221
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import sys
    # TODO: rewrite test for tqdm_rich
    pbar = tqdm_rich(total=10)
    for _ in tqdm_rich(total=10):
        pass
    pbar.reset(total=None)
    pbar.display()
    for _ in tqdm_rich(total=10):
        pass
    pbar.display()
    pbar.close()
    sys.stdout.write('\n')

# Generated at 2022-06-22 13:29:25.807974
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.progress import Track
    progress = Progress(
        BarColumn(bar_width=None),
        "[progress.description]{task.description}",
        "[progress.percentage]{task.percentage}",
        "[progress.remaining]",
        transient=True,
        console=None,
    )
    track = Track(progress)
    task_id = track.add_task("Reset Test", start=0, total=10)
    track.update(task_id, total=50)
    track.update(task_id, completed=50)
    assert track.tasks[task_id].completed == 50

# Generated at 2022-06-22 13:29:28.139637
# Unit test for method close of class tqdm_rich
def test_tqdm_rich_close():
    a = tqdm(total=100)
    for i in range(100):
        a.update(1)
    a.close()

# Generated at 2022-06-22 13:29:39.699823
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from tqdm.rich import FractionColumn
    from tqdm.tests import FakeTask

    total = 10000
    frac_col_unit_scale_false = FractionColumn(unit_scale=False)
    frac_col_unit_scale_true = FractionColumn(unit_scale=True)

    frac_col_unit_scale_false_task = FakeTask(total=total)
    frac_col_unit_scale_true_task = FakeTask(total=total)

    assert frac_col_unit_scale_false.render(frac_col_unit_scale_false_task) == Text(
        "0/10000 ", style="progress.download")

# Generated at 2022-06-22 13:29:42.509009
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich(total=10)
    for i in range(10):
        t.update()
    t.close()

# Generated at 2022-06-22 13:29:53.621344
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Column
    from rich.text import Text

    column = FractionColumn(unit_scale=True)
    task_1 = Column.Task(description="", completed=1230, total=2300)
    task_2 = Column.Task(description="", completed=12300, total=23000)
    task_3 = Column.Task(description="", completed=1.23, total=2.3)
    task_4 = Column.Task(description="", completed=1.23, total=2.30)

    assert isinstance(column.render(task_1), Text)
    assert isinstance(column.render(task_2), Text)
    assert isinstance(column.render(task_3), Text)
    assert isinstance(column.render(task_4), Text)


# Generated at 2022-06-22 13:29:59.449459
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    """Test constructor of class tqdm_rich."""
    for progress in [None, [], ["", ""], ("",), [BarColumn()],
                     [BarColumn(), FractionColumn()],
                     [BarColumn(bar_width=None), Text("{task.description}"),
                      FractionColumn(), "[", TimeElapsedColumn(),
                      TimeRemainingColumn(), "]"]]:
        with tqdm(total=100, progress=progress) as t:
            for _ in t:
                pass

# Generated at 2022-06-22 13:30:14.074415
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress  = (
            "[progress.description]{task.description}"
            "[progress.percentage]{task.percentage:>4.0f}%",
            BarColumn(bar_width=None),
            FractionColumn(
                unit_scale=True, unit_divisor=1000),
            "[", TimeElapsedColumn(), "<", TimeRemainingColumn(),
            ",", RateColumn(unit="B", unit_scale=False,
                                unit_divisor=1000), "]"
        )
    prog = Progress(*progress, transient=True)
    prog.__enter__()
    task_id = prog.add_task("test", total=100, n=50)
    prog.update(task_id, completed=50, description="test", speed=1880)
    assert prog._tasks[0].completed

# Generated at 2022-06-22 13:30:20.639772
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="b")
    result = rate_column.render(task=None)
    assert str(result) == "0.0 b/s"

    rate_column = RateColumn(unit="b", unit_scale=True, unit_divisor=1024)
    result = rate_column.render(task=None)
    assert str(result) == "0.0 b/s"

    rate_column = RateColumn(unit="b", unit_scale=True)
    result = rate_column.render(task=None)
    assert str(result) == "0.0 b/s"

# Generated at 2022-06-22 13:30:31.350787
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """test reset in trange"""
    for i in trange(5):
        pass

    _task_id = None
    _prog = Progress(
        "[progress.description]{task.description}"
        "[progress.percentage]{task.percentage:>4.0f}%",
        BarColumn(bar_width=None),
        FractionColumn(
            unit_scale=False, unit_divisor=1000),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(),
        ",", RateColumn(unit='it', unit_scale=False, unit_divisor=1000), "]",
        transient=True
    )
    _prog.__enter__()
    with trange(5) as t:
        _task_id = t._task_id
        _prog = t._pro

# Generated at 2022-06-22 13:30:43.201906
# Unit test for method render of class RateColumn

# Generated at 2022-06-22 13:30:46.317031
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rateColumn = RateColumn("B", unit_scale=True, unit_divisor=1000)
    result = rateColumn.render(rateColumn)
    assert result.text == "? B/s", "The returned string is not correct"



# Generated at 2022-06-22 13:30:54.021163
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    try:
        with tqdm(total=0, unit='B',
                  unit_scale=True, unit_divisor=1024) as t:
            # Trick to add progressbar in progressbar :)
            # We can not use trange or tqdm_rich directly
            # because they use the same class
            t.reset(total=1)
    except RecursionError:
        # RuntimeError: maximum recursion depth exceeded in cmp
        raise

# Generated at 2022-06-22 13:31:01.402588
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    progress = (
        "[progress.description]{task.description}"
        "[progress.percentage]{task.percentage:>4.0f}%",
        BarColumn(bar_width=None),
        FractionColumn(),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), ",", RateColumn(),
        "]"
    )
    with tqdm_rich(total=10, progress=progress) as t:
        for i in t:
            t.reset(total=5)
            for j in tqdm_rich(total=5):
                pass
        t.reset(total=5)
        for i in t:
            pass

# Generated at 2022-06-22 13:31:06.787087
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm_rich(total=5) as t:
        assert hasattr(t, '_prog')
        for i in _range(5):
            t.display()
            t.update()
    assert not hasattr(t, '_prog')



# Generated at 2022-06-22 13:31:12.432127
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    warn("rich is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
    speed = 0
    unit = ""
    rate_column = RateColumn(unit=unit, unit_scale=False, unit_divisor=1000)
    task = tqdm(0,9,0,speed)
    rate_column.render(task)

# Generated at 2022-06-22 13:31:13.078712
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn

# Generated at 2022-06-22 13:31:22.141431
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """Test for tqdm_rich() class constructor."""
    try:
        import rich
    except ImportError:
        return

    assert hasattr(tqdm_rich(disable=True), "__exit__")
    assert hasattr(tqdm_rich(disable=True, gui=False), "__exit__")
    assert hasattr(tqdm_rich(disable=False, gui=True), "__exit__")
    assert not hasattr(tqdm_rich(disable=False, gui=False), "__exit__")



# Generated at 2022-06-22 13:31:27.810821
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    t = tqdm_rich(total=10)
    for i in range(10):
        time.sleep(0.1)
        t.update()
    t.reset(total=5)
    for i in range(5):
        time.sleep(0.1)
        t.update()
    t.close()

# Generated at 2022-06-22 13:31:30.205018
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm_rich(total=10) as pbar:
        for i in range(10):
            pbar.update(1)

# Generated at 2022-06-22 13:31:31.123742
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(None) == Text("? b/s", style="progress.data.speed")



# Generated at 2022-06-22 13:31:33.478800
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    tqdm_rich_test = tqdm_rich("test")
    tqdm_rich_test.reset()
    assert tqdm_rich_test._prog.tasks[0].completed == 0

# Generated at 2022-06-22 13:31:37.661872
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    f = lambda i: None
    for _ in trange(5):
        f(2)
    trange(100).reset(total=200)

# Generated at 2022-06-22 13:31:41.859318
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    column = RateColumn(unit="B", unit_scale=True, unit_divisor=1000)
    task = Progress(total=2**30, start=0)
    task.completed = 2**32
    task.speed = 2**26
    print(column.render(task))

# Generated at 2022-06-22 13:31:45.156960
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    test function for method render of class RateColumn
    """
    task = None
    assert RateColumn(unit="").render(task) == Text(f"? /s", style="progress.data.speed")

# Generated at 2022-06-22 13:31:50.349701
# Unit test for method render of class RateColumn

# Generated at 2022-06-22 13:32:01.240430
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """Test constructor of tqdm_rich"""
    with tqdm_rich(total=10) as pbar:
        for i in _range(10):
            pbar.update()
        assert pbar.disable is False
    with tqdm_rich(total=10, gui=False) as pbar:
        for i in _range(10):
            pbar.update()
        assert pbar.disable is True


if __name__ == '__main__':  # pragma: no cover
    from time import sleep
    from tqdm.auto import trange, tqdm


# Generated at 2022-06-22 13:32:19.972866
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from unittest import TestCase
    from mock import patch, MagicMock

    class Test_tqdm_rich_display(TestCase):
        def setUp(self):
            self.mock_progress_add_task = patch.object(
                tqdm_rich, '_prog').start()

        def test_tqdm_rich_display(self):
            mock_progress_add_task = self.mock_progress_add_task.return_value
            mock_progress_add_task.update = MagicMock()
            test_tqdm = tqdm_rich(range(1000))
            test_tqdm._prog = MagicMock()
            test_tqdm.display()
            mock_progress_add_task.update.assert_called_once()


# Generated at 2022-06-22 13:32:26.822266
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """Tests tqdm_rich instantiation."""
    from rich.progress import TaskID
    from .utils import _environ

    with _environ(TQDM_DISABLE="0", REFRESH="0"):
        with std_tqdm(total=1) as t:
            pass
        with tqdm_rich(total=1) as t:
            assert isinstance(t._task_id, TaskID)
            assert len(t._prog.task_ids) == 1
            assert t._prog.completed == 1
            with t.external_write_mode():
                t.display()
                t.display()

# Generated at 2022-06-22 13:32:34.003551
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test the method reset of class tqdm_rich"""
    from collections import deque
    import time

    queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

    #Test with reset of total value
    with tqdm_rich(total=len(queue)) as pbar:
        while queue:
            time.sleep(1)
            pbar.reset(total=len(queue))

    #Test with reset of total value
    with tqdm_rich(total=len(queue)) as pbar:
        while queue:
            time.sleep(1)
            pbar.reset()

# Generated at 2022-06-22 13:32:41.965412
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit_scale=True, unit_divisor=400)
    task = Progress()
    task.speed = 50000
    assert rate_column.render(task) == Text("0.1 K.B/s", style="progress.data.speed")
    task.speed = 180000000000
    assert rate_column.render(task) == Text("45 G.B/s", style="progress.data.speed")
    task.speed = 599702
    assert rate_column.render(task) == Text("599 K.B/s", style="progress.data.speed")



# Generated at 2022-06-22 13:32:46.152637
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import tqdm as std_tqdm
    t = tqdm_rich(total=10, leave=True)

    for i in range(10):
        t.display()
        t.update()

    t.display()
    t.close()

    # Passes if no exception is raised

# Generated at 2022-06-22 13:32:47.777094
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    t = tqdm_rich(10)
    t.reset(5)
    assert t.total == 5

# Generated at 2022-06-22 13:32:52.422904
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    total = 10
    with tqdm_rich(total=total, leave=True) as pbar:
        for i in range(total):
            pbar.update()
            time.sleep(0.1)

    with tqdm_rich(total=total, leave=True) as pbar:
        for i in range(total):
            pbar.update()
            pbar.reset(total=i+2)
            time.sleep(0.1)

# Generated at 2022-06-22 13:33:03.858503
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from unittest.mock import Mock
    from unittest import TestCase

    TestCase.assertEqual = TestCase.assertEqual
    TestCase.assertRaises = TestCase.assertRaises

    t = tqdm_rich(total=10, disable=True)
    t._prog.reset = Mock()

    # t doesn't have _prog
    t.reset()
    t._prog.reset.assert_not_called()

    # t has _prog
    delattr(t, '_prog')
    t._prog.reset.reset_mock()
    t._prog.total = 10
    t.reset()
    t._prog.reset.assert_called_once_with(total=10)
    t._prog.reset.reset_mock()
    t.reset

# Generated at 2022-06-22 13:33:13.403662
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """Test tqdm_rich()"""
    assert tqdm_rich(total=1).disable == False
    assert tqdm_rich(total=1, disable=None).disable == False
    assert tqdm_rich(total=1, disable=True).disable == True
    # Ensure arguments passed to trange() a tqdm() are passed through to the
    # underlying iterable:
    for obj in [tqdm_rich(total=0)]:
        assert obj.total == 0
    for obj in [tqdm_rich(total=0, ascii=True)]:
        assert obj.ascii == True
    for obj in [tqdm_rich(total=0, leave=True)]:
        assert obj.leave == True

# Generated at 2022-06-22 13:33:15.108874
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    _ = RateColumn()



# Generated at 2022-06-22 13:33:38.289324
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """
    Test whether the tqdm_rich() displays the message completely.
    """
    # the tqdm_rich should display the message completely
    # without any trailing message.
    # To test that, we compare the tqdm_rich messages with
    # the std_tqdm messages, i.e. the std_tqdm messages should
    # be completely subset of the tqdm_rich messages.
    rich_messages = []
    std_messages = []
    for i in tqdm_rich(range(5)):
        rich_messages.append(i)
    for i in std_tqdm(range(5)):
        std_messages.append(i)

# Generated at 2022-06-22 13:33:39.948767
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich()
    t.display()

# Generated at 2022-06-22 13:33:44.177799
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=10) as pbar:
        pbar.reset(total=5)
        assert pbar.total == 5, "Failed to reset total of Progress class"



# Generated at 2022-06-22 13:33:52.089696
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # init
    rate_column = RateColumn()

    # test
    assert rate_column.render(None) == Text("? /s", style="progress.data.speed")
    assert rate_column.render({"speed": None}) == Text("? /s", style="progress.data.speed")
    assert rate_column.render({"speed": 10}) == Text("10.00 /s", style="progress.data.speed")
    assert rate_column.render({"speed": 10.0}) == Text("10.00 /s", style="progress.data.speed")
    assert rate_column.render({"speed": 10000.0}) == Text("10.00 K/s", style="progress.data.speed")

# Generated at 2022-06-22 13:33:56.778995
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    def display(self, *_, **__):
        self.n = 1
    import unittest
    import unittest.mock
    with unittest.mock.patch.object(tqdm_rich, 'display', display):
        t = tqdm_rich(total=10)
        assert t.n == 1
        t.__exit__ = None
        t.close()
        assert t._prog is None

# Generated at 2022-06-22 13:34:02.438725
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .utils import format_sizeof
    from .std import tqdm_pandas as tpd

    df = tpd.read_csv('https://www.w3schools.com/python/demopage.htm')
    total = len(df)
    for n in trange(10):
        for i in trange(total):
            trange(1, total=1).reset(i).close()
        trange(total).reset(n).close()


# Generated at 2022-06-22 13:34:13.137598
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for _ in tqdm_rich([_ for _ in range(100)]):
        pass
    for _ in tqdm_rich(range(100)):
        pass
    for _ in tqdm_rich(range(100)):
        try:
            for _ in tqdm_rich([_ for _ in range(100)], desc="test", leave=True):
                pass
        except Exception as e:
            print(e)
            pass
        try:
            for _ in tqdm_rich(range(100), desc="test", leave=True):
                pass
        except Exception as e:
            print(e)
            pass
        try:
            for _ in tqdm_rich(range(100), desc="test", leave=True):
                pass
        except Exception as e:
            print(e)
           

# Generated at 2022-06-22 13:34:18.524100
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Unit test for method reset of class tqdm_rich"""
    total = 5
    for i in tqdm_rich(range(total), total=total):
        assert i == tqdm_rich.n
        tqdm_rich.reset()
        assert tqdm_rich.n == 0
        tqdm_rich.reset(total=total)
        assert tqdm_rich.total == total
        i += 1

# Generated at 2022-06-22 13:34:25.792285
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    verify the output of method render from class RateColumn
    """
    try:
        from rich.progress import tasks
    except ImportError:
        # rich not installed
        return
    task = tasks.Task("Test RateColumn")
    task.speed = None
    assert RateColumn().render(task) == Text("? /s", style="progress.data.speed")
    task.speed = 0
    assert RateColumn().render(task) == Text("0 /s", style="progress.data.speed")
    task.speed = 1000
    assert RateColumn().render(task) == Text("1.0 K/s", style="progress.data.speed")
    task.speed = 1000000
    assert RateColumn().render(task) == Text("1.0 M/s", style="progress.data.speed")
    task.speed = 1000000000

# Generated at 2022-06-22 13:34:34.577923
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(0) == Text('0  /s', style='progress.data.speed')
    # TODO: test RateColumn(unit)
    # TODO: test RateColumn(unit_scale)
    # TODO: test RateColumn(unit_scale and unit)
    # TODO: test RateColumn(unit_divisor)
    # TODO: test RateColumn(unit_divisor and unit)
    # TODO: test RateColumn(unit_scale and unit_divisor)
    # TODO: test RateColumn(unit_scale and unit_divisor and unit)
    # TODO: test RateColumn(disable)
    pass

# Generated at 2022-06-22 13:35:16.744599
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # Test disabling
    with tqdm_rich(disable=True):
        for _ in trange(2):
            pass
    # tqdm_rich.display() depends on tqdm._instances, so test here
    assert not len(tqdm._instances)



# Generated at 2022-06-22 13:35:25.056183
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(100, reset=True) as pbar:
        for i in pbar:
            pbar.reset()
            break


if __name__ == "__main__":  # pragma: no cover
    from tqdm.autonotebook import tqdm as au  # noqa
    for i in tqdm(au(range(10)), leave=True):
        for j in tqdm(au(range(10)), leave=True):
            for k in tqdm(au(range(10)), leave=True):
                pass
            pass
            pass

# Generated at 2022-06-22 13:35:29.064277
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from time import sleep

    for i in tqdm(range(4), desc='Foo'):
        sleep(0.01)
        if i == 1:
            tqdm.reset(total=4, desc='Bar')
        sleep(0.01)

# Generated at 2022-06-22 13:35:33.072112
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    # some random tests for total=None and total=12
    for i in [None, 0.5, 1, 10, 10.5, 11, 11.5, 12]:
        t = tqdm(total=None, disable=True)
        t.reset(total=i)
        assert t.total == i
        assert t.n == 0



# Generated at 2022-06-22 13:35:38.853419
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import tqdm
    with tqdm(total=4) as t:
        for i in range(4):
            t.update()
        t.reset(total=2)
        for i in range(2):
            t.update()


try:
    from IPython.display import display, clear_output
except ImportError:
    pass



# Generated at 2022-06-22 13:35:49.488059
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import tqdm
    from time import sleep
    for i in tqdm_rich(range(10), total=None):
        sleep(0.1)
    for i in tqdm_rich(range(10), total=None, ascii=True):
        sleep(0.1)
    try:
        range(10).__next__
    except AttributeError:
        pass
    else:
        for i in tqdm_rich(range(10), total=None, ascii=True, mininterval=0):
            sleep(0.1)
        try:
            range(10).__len__
        except AttributeError:
            pass

# Generated at 2022-06-22 13:35:52.438796
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    for _ in tqdm(range(2), desc='my bar', ncols=10, smoothing=0.0, total=2):
        pass

# Generated at 2022-06-22 13:35:55.058827
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from math import ceil
    for _ in tqdm(range(4), desc='I am task'):
        pass

# Generated at 2022-06-22 13:36:03.412387
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():

    import pytest

    @pytest.fixture
    def tqdm_cls(monkeypatch):
        monkeypatch.setattr('tqdm._tqdm.tqdm.display', lambda self: self.__dict__.update({'display_called': True}))
        return tqdm_rich

    @pytest.fixture
    def prog(monkeypatch):
        prog = Progress()
        monkeypatch.setattr('rich.progress.Progress', lambda *args, **kwargs: prog)
        return prog

    def test_no_prog(tqdm_cls):
        tqdm_cls('foobar').display()

    def test_with_prog(tqdm_cls, prog):
        tqdm_cls('foobar').display()
        assert prog.__dict__ == {}

# Generated at 2022-06-22 13:36:08.855576
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    # test tqdm_rich reset method works
    with tqdm_rich(10) as progress1:
        time.sleep(0.5)
        progress1.reset(total=100)
        time.sleep(0.5)
        progress1.reset()
