

# Generated at 2022-06-22 13:27:46.595377
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(_range(10)) as t:
        for i in t:
            t.clear()



# Generated at 2022-06-22 13:27:57.963521
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = Progress.Task(completed=52, total=103)
    assert FractionColumn(unit_scale=False, unit_divisor=1000).render(task) == '[progress.download]0.5/1.0'

    task = Progress.Task(completed=52, total=103)
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(task) == '[progress.download]0.1/0.1 K'

    task = Progress.Task(completed=523, total=10319)
    assert FractionColumn(unit_scale=True, unit_divisor=1000).render(task) == '[progress.download]0.5/1.0 K'

    task = Progress.Task(completed=523, total=10319)

# Generated at 2022-06-22 13:28:01.027854
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    try:
        with tqdm_rich(total=10) as t:
            for i in range(10):
                t.clear()
    except:  # pragma: no cover
        return False

    return True

# Generated at 2022-06-22 13:28:14.048354
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    try:
        from rich import box
    except ImportError:
        return  # skip test

    with tqdm_rich(total=3) as t:
        assert (t.format_dict["total"] == 3)
        assert (t.format_dict["n"] == 0)
        assert (t.format_dict["last_print_n"] == 0)
        assert (t.format_dict["dynamic_ncols"] == True)
        assert (t.format_dict["rate"] == None)
        assert (t.format_dict["desc"] == "")
        assert (t.format_dict["unit"] == "it")
        assert (t.format_dict["unit_scale"] == False)
        assert (t.format_dict["unit_divisor"] == 1000)


# Generated at 2022-06-22 13:28:20.246094
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from time import sleep
    try:
        for i in tqdm(range(10), desc='1st loop', miniters=1):
            sleep(0.01)
        for i in tqdm(range(10), desc='2nd loop', miniters=1):
            sleep(0.01)
    except Exception as e:
        raise e
    finally:
        pass

# Generated at 2022-06-22 13:28:31.327146
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import TaskID
    from rich.text import Text
    fc = FractionColumn(unit_scale=False, unit_divisor=1000)
    assert fc.render(TaskID("test", total=10, completed=1)) == Text("0.1/10.0", style="progress.download")
    fc = FractionColumn(unit_scale=True, unit_divisor=1000)
    assert fc.render(TaskID("test", total=10, completed=1)) == Text("0/0.0", style="progress.download")
    assert fc.render(TaskID("test", total=12345678, completed=1)) == Text("0.0/12.3 K", style="progress.download")

# Generated at 2022-06-22 13:28:43.313277
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import TaskID
    task = TaskID(0, 'tqdm_tqdm', None, 0, 0, 0, 0, 0, 0, None)
    task.total = 1000
    task.set_completed(500)
    assert FractionColumn().render(task) == "[progress.download]0.5/1.0 K"
    assert FractionColumn(unit_scale=False).render(task) == "[progress.download]0/1000"
    task.total = 1000000
    task.set_completed(500000)
    assert FractionColumn().render(task) == "[progress.download]0.5/1.0 M"
    assert FractionColumn(unit_scale=False).render(task) == "[progress.download]0/1000000"
    task.total = 500000000

# Generated at 2022-06-22 13:28:51.873190
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    class mock():
        def __init__(self, test):
            self.test = test
    class mock_progress():
        def __init__(self):
            self.tasks = []
        def add_task(self, *args, **kwargs):
            task = mock(self.tasks)
            task.id = len(self.tasks)
            self.tasks.append(task)
            return task.id
        def update(self, id, *args, **kwargs):
            self.tasks[id].kwargs = kwargs
        def reset(self, *args, **kwargs):
            pass
    class mock_desc():
        def __init__(self, val):
            self.val = val
        def __str__(self):
            return self.val
    # test

# Generated at 2022-06-22 13:28:53.758751
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    # Arrange

    # Act
    tqdm_rich.clear()

    # Assert
    assert True

# Generated at 2022-06-22 13:28:56.908151
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    import random
    with Progress() as pb:
        bar_id = pb.add_task("My bar")
        for i in range(10):
            time.sleep(random.random())
            pb.update(bar_id, progress=i, completed=i)


# Generated at 2022-06-22 13:29:06.724109
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    a = tqdm_rich(total=100)
    for i in range(100):
        a.update(1)
    assert a.n == 100
    a.reset(total=200)
    assert a.n == 0
    assert a.total == 200
    a.reset()
    assert a.n == 0
    assert a.total == 200

# Generated at 2022-06-22 13:29:08.529625
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    inst = tqdm_rich(range(10), disable=True)
    assert inst.clear(None, None) is None

# Generated at 2022-06-22 13:29:17.243353
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """
    Unit tests for `method display` of class `tqdm_rich`
    """
    test_tqdm = tqdm(total=3)
    test_tqdm.n = 0
    test_tqdm.display()
    assert hasattr(test_tqdm, '_prog')
    test_tqdm.n = 1
    test_tqdm.display()
    test_tqdm.n = 2
    test_tqdm.display()
    test_tqdm.close()
    assert not hasattr(test_tqdm, '_prog')


# Generated at 2022-06-22 13:29:20.591278
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm(total=2) as pbar:
        for _ in range(2):
            pbar.clear()
            pbar.update()
    assert pbar.format_dict == {}

# Generated at 2022-06-22 13:29:26.055523
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .tests_tqdm import pretest_posttest, posttest
    with pretest_posttest() as (f, disable):
        for _ in f(tqdm_rich, desc="tqdm_rich", unit="B", unit_scale=False,
                   total=4096, disable=disable):
            pass


# Generated at 2022-06-22 13:29:37.992956
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from tqdm.auto import trange
    from tqdm.auto import tqdm
    from tqdm._tqdm import format_interval

    for gui in (False, True):
        with trange(4, ascii=gui, gui=gui) as t:
            for i in t:
                # test clearing line
                t.set_description('testing tqdm_rich')
                # test clearing descriptor
                t.set_postfix(postfix='testing tqdm_rich')
                break

    desc = 'testing tqdm_rich'
    postfix = 'testing tqdm_rich'

    with tqdm(total=4, desc=desc) as t:
        for i in range(4):
            # Check that clearing bar works
            t.set_description('another description')

# Generated at 2022-06-22 13:29:43.093418
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import os
    import tempfile

    _, tqdm_rich_path = tempfile.mkstemp()

    tqdm_rich_reset_test = tqdm_rich(total=100)
    tqdm_rich_reset_test.reset(total=101)
    assert tqdm_rich_reset_test.total == 101

    tqdm_rich_reset_test.reset()
    assert tqdm_rich_reset_test.total == 0

    os.remove(tqdm_rich_path)

# Generated at 2022-06-22 13:29:53.172381
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    td = tqdm_rich(total=10)
    with td:
        assert td.total == 10
        assert td.n == 0
        assert td.dynamic_mess == ''
        td.clear(nolock=True)
        td.n = 10
        td.display(nolock=True)
        assert td.n == 10
        td.display(nolock=True)
        assert td.dynamic_mess == ''
        td.n = 0
        td.desc = 'test'
        td.display(nolock=True)
        assert td.dynamic_mess == '\r test: |█████████   | 4/10 [00:00<?, ?it/s]'
        td.close()

# Generated at 2022-06-22 13:30:01.274935
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.progress import TimeElapsedColumn, TimeRemainingColumn
    from rich.progress import Progress, BarColumn
    from rich.panel import Panel
    from rich.bar import Bar
    from rich.text import Text

    _list = ['a', 'b', 'c']
    panel = Panel("Demo")
    progress = Progress("[progress.descripton]{task.description}",
                        "[progress.percentage]{task.percentage:>3.0f}%",
                        BarColumn(),
                        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), ",",
                        RateColumn(), "]", transient=False)
    panel.add(progress)
    for i, item in enumerate(progress.bar(_list, start=1, label="Start")):
        progress.update(item, completed=i + 1)
       

# Generated at 2022-06-22 13:30:11.395895
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    obj = RateColumn()
    task = {'speed': None}
    result = obj.render(task)
    assert result.text == '? /s'
    task['speed'] = 1
    result = obj.render(task)
    assert result.text == '1 /s'
    task['speed'] = 1000
    result = obj.render(task)
    assert result.text == '1.0 K/s'
    task['speed'] = 999999999
    result = obj.render(task)
    assert result.text == '1.0 G/s'
    obj = RateColumn(unit="bit")
    task = {'speed': None}
    result = obj.render(task)
    assert result.text == '? bit/s'
    task['speed'] = 1
    result = obj.render(task)


# Generated at 2022-06-22 13:30:22.225922
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Test the reset() method of class tqdm_rich.
    """
    from .utils import TqdmKeyError, TqdmTypeError

    class dummy_tqdm_rich(tqdm_rich):
        def __init__(self, *args, **kwargs):
            kwargs['desc'] = kwargs.get('desc', 'A dummy progressbar')
            super(dummy_tqdm_rich, self).__init__(*args, **kwargs)

    with dummy_tqdm_rich(500) as bar:
        bar.reset()
        bar.reset(total=300)
        bar.reset()
        bar.reset(total=100)
        bar.reset(total=400)

# Generated at 2022-06-22 13:30:27.704454
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    unit = 'KiB'
    unit_scale = False
    unit_divisor = 1024
    rate_column = RateColumn(unit, unit_scale, unit_divisor)
    rate_column.render(Progress.TASK_TEMPLATE.copy(speed=1024))
    rate_column.render(Progress.TASK_TEMPLATE.copy(speed=2048))
    rate_column.render(Progress.TASK_TEMPLATE.copy(speed=3000))


# Generated at 2022-06-22 13:30:39.828334
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Test that the method is working properly by comparing the result
    of the output with an expected result.
    """
    test_expected_result = "2.3 K/s"
    test_unit = "/s"
    test_speed = 2300
    rate_column = RateColumn(test_unit, unit_scale=True, unit_divisor=1000)
    test_result = rate_column.render(test_speed)
    assert test_result == test_expected_result
    # test with unit_scale = False
    test_expected_result = "2300 /s"
    rate_column = RateColumn(test_unit, unit_scale=False, unit_divisor=1000)
    test_result = rate_column.render(test_speed)
    assert test_result == test_expected_result
    # test

# Generated at 2022-06-22 13:30:48.796965
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """Test tqdm_rich constructor."""
    # Test: create an instance of tqdm_rich
    with tqdm_rich(total=10, desc="foo", unit="b", unit_scale=True,
                   initial=5, miniters=1, mininterval=0.1,
                   ascii=True, disable=False, leave=False,
                   mininterval=0.1, maxinterval=10.0,
                   file=sys.stdout, dynamic_ncols=False,
                   smoothing=0.3, bar_format="{desc}{percentage:3.0f}%|{bar}|") as progress_bar:
        assert progress_bar.total == 10
        assert progress_bar.dynamic_ncols is False

# Generated at 2022-06-22 13:31:00.034780
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import pytest
    from .utils import printf


# Generated at 2022-06-22 13:31:07.483900
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test method tqdm_rich.display."""
    from time import sleep
    with tqdm_rich(total=20, desc="I'm a test", unit='B', unit_scale=True,
                   unit_divisor=1024) as t:
        for i in range(20):
            sleep(0.1)
            if i == 5 or i == 15:
                t.reset(20)
            t.update()
    return True

# Generated at 2022-06-22 13:31:14.638995
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test."""
    assert RateColumn(unit_scale=True, unit_divisor=1000).render(
        type('task', (object,), {'speed': None})()) == Text("? /s", style="progress.data.speed")
    assert RateColumn(unit_scale=True, unit_divisor=1000).render(
        type('task', (object,), {'speed': 0})()) == Text("0.0 /s", style="progress.data.speed")
    assert RateColumn(unit_scale=True, unit_divisor=1000).render(
        type('task', (object,), {'speed': 42})()) == Text("42.0  /s", style="progress.data.speed")

# Generated at 2022-06-22 13:31:17.312432
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    """test method "display" of class tqdm_rich"""
    t = tqdm(total=1000)
    try:
        t.display()
    except:
        raise AssertionError()

# Generated at 2022-06-22 13:31:19.461008
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    from time import sleep
    tqdm_rich(sleep(0.1) for _ in range(10))

# Generated at 2022-06-22 13:31:29.282050
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    import random

    interval = [0.1, 0.1, 0.1]

    t = tqdm_rich(interval)
    for i in t:
        time.sleep(i)

    t.reset()
    interval.append(0.1)
    for i in t:
        time.sleep(i)

    t.reset(len(interval))
    interval.append(0.1)
    for i in t:
        time.sleep(i)

    t.reset(len(interval))
    random.shuffle(interval)
    for i in t:
        time.sleep(interval.pop())

# Generated at 2022-06-22 13:31:42.250609
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Unit test to test the method reset of class tqdm_rich.

    Test to see that the method reset works as expected by checking that
    the bar is updated to the specified total (or to the default total if
    none is specified).

    """
    try:
        from time import sleep
    except ImportError:
        return
    t = tqdm_rich(range(100))
    t.reset(total=100)
    t.updat

# Generated at 2022-06-22 13:31:42.952220
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    trange(3)

# Generated at 2022-06-22 13:31:45.704673
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Unit test for method display of class tqdm_rich."""
    t = tqdm_rich(total=None)
    t.display()
    t.close()

# Generated at 2022-06-22 13:31:47.766984
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test method reset of class tqdm_rich."""
    total = 123
    with tqdm_rich(total=total) as t:
        t.reset()
        assert t.total == 0
        t.reset(total=total)
        assert t.total == total

# Generated at 2022-06-22 13:31:59.630950
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich import print
    from rich.progress import Progress
    from rich.panel import Panel
    from rich.columns import Columns
    from rich.text import Text
    from rich.markdown import Markdown
    from rich.table import Table
    from time import sleep
    from tqdm.rich import tqdm
    with Progress() as progress:
        # Set up initial task
        task_id = progress.add_task("Progress Bar Demo")
        # Here's the foreground task which we want to track:
        for i in tqdm(range(20)):
            sleep(0.1)

        # Update the task description
        progress.update(task_id, description="Updated description")
        # Call the reset method
        tqdm.reset(6)
        # Here's the foreground task which we want to track:

# Generated at 2022-06-22 13:32:04.841281
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    with tqdm(total=100) as t:
        t.update(1)
        t.update(2)
        time.sleep(0.1)
        t.update(3)
        t.update(50)

# Generated at 2022-06-22 13:32:16.781696
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .gui import tqdm
    import time
    from .utils import _range
    from .std import format_interval
    r = tqdm(total=10)
    for i in r:
        time.sleep(0.01)
        if i == 5:
            r.reset()
    r.close()

    # Same test as above, with `reset(total=None)`
    r = tqdm(total=10)
    for i in r:
        time.sleep(0.01)
        if i == 5:
            r.reset(total=None)
    r.close()

    # Total set to None when reset(total=None) is called
    r = tqdm(total=10)
    assert r.total
    r.reset(total=None)
    assert not r.total



# Generated at 2022-06-22 13:32:25.379812
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import tqdm
    from .utils import _range
    from .utils import format_sizeof
    from .utils import format_interval
    import time

    with tqdm_rich(total=100) as t:
        for i in _range(5):
            t.reset(total=i)
            t.set_description("Resetting")
            time.sleep(1)
            t.update()
        for i in _range(100):
            t.reset(total=i)
            t.update()
    print(format_interval(t.elapsed))
    print(format_sizeof(t.n))



# Generated at 2022-06-22 13:32:31.985829
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    # For integer
    task = (None, 12)
    good_result = Text("12  /s", style="progress.data.speed")
    assert (rate_column.render(task), "bad result") == (good_result, "good result")
    # For float
    task = (None, 12.12)
    good_result = Text("12.1 /s", style="progress.data.speed")
    assert (rate_column.render(task), "bad result") == (good_result, "good result")

# Generated at 2022-06-22 13:32:43.453756
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import math
    a = RateColumn()
    assert a.render(std_tqdm.tqdm(total=0, initial=0, leave=False, disable=True, unit='it', unit_scale=True, unit_divisor=1000).set_postfix(speed=10)) == Text(str(str(10) + '  it/s'), str('progress.data.speed'))
    a = RateColumn(unit='it', unit_scale=True, unit_divisor=1000)

# Generated at 2022-06-22 13:33:00.505960
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from io import StringIO
    import sys

    stream = StringIO()
    sys.stdout = stream
    t = tqdm_rich(range(10))
    t.update(8)
    sys.stdout = sys.__stdout__
    assert stream.getvalue() == ''

# Generated at 2022-06-22 13:33:05.438563
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=3) as pbar:
        pbar.update(1)
        pbar.reset(total=4)
        pbar.update(2)
    assert pbar.n == 2


if __name__ == "__main__":
    from .utils import _test_docstrings
    _test_docstrings()

# Generated at 2022-06-22 13:33:12.014066
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    layout = [
        "[progress.description]{task.description}",
        BarColumn(bar_width=None),
        "{task.percentage:>4.0f}%",
        "[",
        TimeElapsedColumn(),
        "<",
        TimeRemainingColumn(),
        "]",
    ]
    progress = Progress(*layout, transient=True)
    with progress:
        task = progress.add_task('Test')
        for _ in tqdm_rich(range(100), total=100, desc='tqdm', leave=False,
                           bar_format='{desc}: {percentage:3.0f}%'):
            pass
        progress.reset(100)

# Generated at 2022-06-22 13:33:17.145550
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    l = list(range(1000))
    with tqdm_rich(l, unit="B", unit_scale=True) as pbar:
        for i, b in enumerate(l):
            pbar.update(i)
            sleep(0.01)

# Generated at 2022-06-22 13:33:25.810607
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    def test_cases(speed, unit_scale, unit_divisor,
                   expected_result, expected_suffix):
        expected_result_split = expected_result.split()
        assert len(expected_result_split) == 3
        expected_result = expected_result_split[0]
        expected_unit = expected_result_split[1]
        expected_suffix = expected_result_split[2]
        rate_column = RateColumn(
            unit=expected_unit,
            unit_scale=unit_scale,
            unit_divisor=unit_divisor)
        real_result = rate_column.render(
            task=type('', (), dict(speed=speed))()).content
        assert real_result == expected_result

# Generated at 2022-06-22 13:33:30.990533
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich import print
    from tqdm.auto import tqdm as tn

    my_tqdm_range = tn(range(10), desc="my_tqdm_range")
    n = next(my_tqdm_range)
    print("testing:", n)
    my_tqdm_range.reset(1)

# Generated at 2022-06-22 13:33:42.585760
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # The input is the task.speed before _RateColumn.render
    # The first output is the return value of _RateColumn.render
    # The second output is the expected return value of _RateColumn.render
    unit_values = [
        (1, 'B'),
        (999, 'B'),
        (1000, 'KB'),
        (1000*1000, 'MB'),
        (1000*1000*1000, 'GB'),
        (1000*1000*1000*1000, 'TB'),
        (1000*1000*1000*1000*1000, 'PB'),
        (1000*1000*1000*1000*1000*1000, 'EB'),
    ]
    # Pick a suitable unit for completed and total
    for (speed, unit) in unit_values:
        # First, precision = 1
        rate_column = RateColumn()
        # Speed is not

# Generated at 2022-06-22 13:33:46.317552
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress_column = RateColumn()
    assert progress_column.render(Task(None, None, None, "200")) == "\x1b[36;1m200 \x1b[0m\x1b[36m/s\x1b[0m"

# Generated at 2022-06-22 13:33:52.182627
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from .std import trange
    for total in [None, 50]:
        with trange(100, desc="tqdm_rich_reset", leave=True) as t:
            t.reset(total=total)
            for i in t:
                t.reset()  # total should now be 50
                pass

# Generated at 2022-06-22 13:33:59.527119
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from time import sleep
    from .utils import _range
    from .std import tqdm
    from .std import tnrange as nrange

    # loop with no description
    with tqdm(_range(4), desc='Default', leave=True) as t:
        for i in t:
            t.display()
            sleep(0.01)

    # loop with description
    with tqdm(_range(4), desc='Test', leave=True) as t:
        for i in t:
            t.display(desc="Test")
            sleep(0.01)

    # loop with nested bars

# Generated at 2022-06-22 13:34:34.003273
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from time import sleep
    # Case 1: leave enabled and desc/n not empty/0
    t1 = tqdm_rich(0, desc="desc", leave=True)
    # Case 2: leave enabled and only desc not empty/0
    t2 = tqdm_rich(desc="desc", leave=True)
    # Case 3: leave enabled and only n not empty/0
    t3 = tqdm_rich(0, leave=True)
    # Case 4: leave disabled
    t4 = tqdm_rich(0, leave=False)

    _ = [sleep(0.01) for _ in range(3)]
    assert hasattr(t1, '_prog')
    t1.display()
    assert hasattr(t2, '_prog')
    t2.display()

# Generated at 2022-06-22 13:34:45.185373
# Unit test for method render of class RateColumn

# Generated at 2022-06-22 13:34:47.921430
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="")
    assert rate_column.render(task) == Text(f"{task.speed:,.1f} {self.unit}/s",
                    style="progress.data.speed")

# Generated at 2022-06-22 13:34:53.991307
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time
    with tqdm_rich(total=12) as pbar:
        for i in range(8):
            time.sleep(0.5)
            pbar.update()
        pbar.reset(total=5)  # resets total to 5
        for i in range(5):
            time.sleep(0.5)
            pbar.update()
    assert pbar.total == 5

# Generated at 2022-06-22 13:34:59.240251
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    """Test function constructor of class tqdm_rich."""
    with tqdm_rich(total=123) as t:
        assert t.desc == ":bar"
        t.set_description("Test")
        assert t.desc == "Test"
        assert t.total == 123
        t.update(10)
        assert t.n == 10
        t.close()



# Generated at 2022-06-22 13:35:07.578765
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.console import Console
    from rich.columns import Columns
    from rich.progress import TaskID, Progress

    columns = Columns()
    progress = Progress(transient=False)
    progress.__enter__()
    task_id = progress.add_task("")
    columns.add_progress(task_id, progress)
    progress.update(task_id, completed=10)
    progress.__exit__(None, None, None)
    console = Console()
    console.print(columns)

# Generated at 2022-06-22 13:35:14.854031
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel
    from rich.table import Table

    with Console(width=120) as console:
        console.print(Panel(Markdown('# I am a markdown panel')))
        console.print(Table(title='I am a table'))

        with Progress() as p:
            for i in trange(10, desc='So slow'):
                print(i)
                p.add_task('Simple task', complete=i)
                p.add_task('Fancy task', start=(i+1) * 24,
                           end=(i+1) * 48, complete=i * i)
                if i == 5:
                    p.reset()

# Generated at 2022-06-22 13:35:19.106559
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from tqdm.auto import tqdm

    with tqdm(10, desc='Progress:') as t:
        t.reset(50)
        t.reset(2500)

    # Make sure no errors are raised
    t.reset()

# Generated at 2022-06-22 13:35:29.424873
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    print(RateColumn().render(Progress(total=0)))
    print(RateColumn().render(Progress(completed=0, total=1)))
    print(RateColumn(unit="B").render(Progress(completed=0, total=1)))
    print(RateColumn(unit="B").render(
        Progress(completed=1, total=1, speed=0)))
    print(RateColumn(unit="B").render(
        Progress(completed=1, total=1, speed=1)))
    print(RateColumn(unit="B").render(
        Progress(completed=1, total=1, speed=10)))
    print(RateColumn(unit="B").render(
        Progress(completed=1, total=1, speed=100)))

# Generated at 2022-06-22 13:35:37.177812
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=20) as pbar:
        pbar.update(10)
        assert pbar._prog.completed == 10
        pbar.reset(total=30)
        assert pbar._prog.total == 30
        assert pbar._prog.completed == 0
    with tqdm(total=20) as pbar:
        pbar.update(10)
        assert pbar._prog.completed == 10
        pbar.reset()
        assert pbar._prog.total == 0
        assert pbar._prog.completed == 0

# Generated at 2022-06-22 13:36:39.054939
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = ProgressColumn()
    task.speed = 123456
    task.unit = "B"
    for unit_scale in (True, False):
        for unit_divisor in (1000, 1024):
            rate = RateColumn(unit=task.unit, unit_scale=unit_scale, unit_divisor=unit_divisor)

            task.speed = 123456000*10**0
            assert rate.render(task).as_text() == "123.46 MB/s"

            task.speed = 123456000*10**1
            assert rate.render(task).as_text() == "12.35 GB/s"

            task.speed = 123456000*10**2
            assert rate.render(task).as_text() == "1.23 TB/s"


# Generated at 2022-06-22 13:36:51.991270
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    import time
    for _ in tqdm_rich(range(4)):
        time.sleep(0.5)
    for _ in tqdm_rich(range(4), progress=(
            "Test progress bar",
            BarColumn(bar_width=None),
            FractionColumn(unit_scale=True, unit_divisor=1024),
            "[", TimeElapsedColumn(), "]",
            )):
        time.sleep(0.5)

# Generated at 2022-06-22 13:36:58.539222
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    # First, create an progress bar with a known `total` value
    with tqdm_rich(total=10) as current_bar:
        # Update the status
        for i in range(5):
            current_bar.update()
        # Reset the status with a new `total` value
        current_bar.reset(total=20)
        # Update the status again
        for i in range(10):
            current_bar.update()

# Generated at 2022-06-22 13:37:05.129833
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .gui import tqdm_gui
    with tqdm_rich(total=4, position=1, leave=False, ascii=True, disable=True) as t:
        for i in t:
            t.display()
            t.update()

if __name__ == '__main__':  # pragma: no cover
    from .gui import tqdm_gui
    with tqdm_rich(total=4, position=1, leave=False, ascii=True) as t:
        for i in t:
            t.update()

# Generated at 2022-06-22 13:37:15.481995
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from time import sleep

    tqdm_rich_test = tqdm_rich(
        range(5),
        desc='testing display',
        total=50,
        leave=True,
        unit='B',
        unit_scale=False,
        unit_divisor=1024,
        miniters=1,
        mininterval=0.1
    )

    assert not tqdm_rich_test.disable
    assert tqdm_rich_test.desc == 'testing display'
    assert tqdm_rich_test.total == 50
    assert tqdm_rich_test.leave
    assert tqdm_rich_test.unit == 'B'
    assert not tqdm_rich_test.unit_scale
    assert tqdm_rich_test.unit_divisor == 1024
    assert t

# Generated at 2022-06-22 13:37:21.430910
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import io
    import sys
    fake_stdout = io.StringIO()
    sys.stdout = fake_stdout
    tqdm_rich(range(10), disable=False)
    fake_stdout.seek(0)
    assert fake_stdout.read() == '\n'
    sys.stdout = sys.__stdout__

# Generated at 2022-06-22 13:37:23.631950
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    st = RateColumn()
    assert st.render(None) == Text("? B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:37:28.697719
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm(total=3) as pbar:
        pbar.display()
        pbar.update(1)
        pbar.display()
        pbar.update(1)
        pbar.display()
        pbar.update(1)
        pbar.display()
    assert pbar.n == 3

# Generated at 2022-06-22 13:37:40.899639
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.progress import BarColumn
    from rich.console import Console
    
    # Arrange
    # test is done with complete input
    test_desc = 'Description'
    test_total = 1.0
    test_postfix = 'Postfix'
    test_n = 1