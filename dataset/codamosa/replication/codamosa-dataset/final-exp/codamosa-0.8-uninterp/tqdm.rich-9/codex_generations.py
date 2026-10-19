

# Generated at 2022-06-22 13:27:44.556994
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=10) as bar:
        bar.reset(total=20)
        assert bar.total == 20

    with tqdm(total=10) as bar:
        bar.reset()
        assert bar.total == 0

# Generated at 2022-06-22 13:27:56.343611
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Test for RateColumn render method.
    """
    from collections import defaultdict
    from rich.progress import Progress

    # Test without unit
    task = Progress.task()
    task.total = 1024
    task.completed = 512
    task.set_speed(1)
    column = RateColumn()
    result = column.render(task)
    expected = Text("0.5 /s", style="progress.data.speed")
    assert (result == expected)

    # Test with unit
    task = Progress.task()
    task.total = 1024
    task.completed = 512
    task.set_speed(1)
    column = RateColumn(unit='B')
    result = column.render(task)
    expected = Text("0.5 B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:28:08.543733
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    import sys
    from io import StringIO
    from argparse import ArgumentParser
    from .nested import nested_sum

    p = ArgumentParser()
    p.add_argument('-t', '--total', type=int, help='total', default=10)
    p.add_argument('-n', '--nested', type=int, help='nested', default=3)
    p.add_argument('-c', '--column', help='column', action='store_true')
    p.add_argument('-u', '--unit_scale', help='unit_scale', action='store_true')

    args = p.parse_args()

    total = args.total
    nested = args.nested
    column = args.column
    unit_scale = args.unit_scale

    f = StringIO()

# Generated at 2022-06-22 13:28:20.602120
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.console import Console
    from rich.text import Text

    console = Console()
    rate_column = RateColumn()
    text = rate_column.render(None)
    assert text == Text("? /s", style="progress.data.speed")

    text = rate_column.render(None, speed=10)
    assert text == Text("10 /s", style="progress.data.speed")

    text = rate_column.render(None, speed=10, unit="B")
    assert text == Text("10 B/s", style="progress.data.speed")

    text = rate_column.render(None, speed=100, unit="B", unit_scale=True)
    assert text == Text("100 /s", style="progress.data.speed")


# Generated at 2022-06-22 13:28:28.891962
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fraction = FractionColumn()
    task = Progress(
            Task(completed=10, total=3),
        )
    assert fraction.render(task) == Text(
            "3.3/10 ",
            style="progress.download")
    task = Progress(
            Task(completed=10, total=3),
            Task(completed=2, total=1000),
        )
    assert fraction.render(task) == Text(
            "3.3/10 ",
            style="progress.download")


# Generated at 2022-06-22 13:28:32.611586
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from .tqdm import tqdm
    from .std import time
    for n in tqdm(range(100)):
        time.sleep(0.001)

# Generated at 2022-06-22 13:28:41.801188
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from unittest.mock import MagicMock
    from unittest.mock import patch
    from unittest import TestCase
    from io import StringIO
    stream = StringIO()
    m = MagicMock()
    with patch.object(tqdm_rich, 'display', m):
        t = tqdm_rich(["1", "2", "3"], unit="", unit_scale=False, unit_divisor=1000, file=stream)
        t.update(1)
    m.assert_called()
    return True



# Generated at 2022-06-22 13:28:43.608490
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .gui import tnrange
    from .gui import test_gui

    test_gui(tnrange, tqdm_rich)

# Generated at 2022-06-22 13:28:44.822758
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    t = tqdm_rich(range(100))
    t.clear()

# Generated at 2022-06-22 13:28:51.801240
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress = RateColumn(unit="bytes")
    speed = progress.render(progress.render.__globals__['task'])
    assert(speed == "0 bytes/s")
    speed = progress.render(progress.render.__globals__['task'])
    assert(speed == "0 bytes/s")
    task = progress.render.__globals__['task']
    task.speed += 1
    speed = progress.render(task)
    assert(speed == "1 bytes/s")
    task.speed = 1024
    speed = progress.render(task)
    assert(speed == "1.0 Kbytes/s")


# Generated at 2022-06-22 13:29:03.231181
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    """
    Unit test for method clear of class tqdm_rich.
    """
    is_pass = True
    try:
        tqdm_rich(range(0)).clear()
    except NotImplementedError:
        is_pass = False
    assert is_pass

# Generated at 2022-06-22 13:29:05.454336
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    tqdm_test = tqdm_rich(range(10))
    tqdm_test.display()
    tqdm_test.close()

# Generated at 2022-06-22 13:29:17.502851
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    render0 = RateColumn(unit="b", unit_scale=True).render
    render1 = RateColumn(unit="B", unit_scale=True).render
    render2 = RateColumn(unit="b", unit_scale=False).render
    render3 = RateColumn(unit="B", unit_scale=False).render
    render4 = RateColumn(unit="b", unit_scale=True, unit_divisor=1024).render
    render5 = RateColumn(unit="B", unit_scale=True, unit_divisor=1024).render
    render6 = RateColumn(unit="b", unit_scale=False, unit_divisor=1024).render
    render7 = RateColumn(unit="B", unit_scale=False, unit_divisor=1024).render

    # test the method render

# Generated at 2022-06-22 13:29:19.500743
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    test = tqdm_rich(total=2)
    assert test.disable == False
    test.close()

# Generated at 2022-06-22 13:29:25.207856
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import Progress
    from rich.console import Console
    console = Console()
    progress = Progress(FractionColumn())
    task = progress.add_task("task", total=200)
    task.update(50)
    progress.render(console)
    assert console.get_text() == '[                        ] 0.3/2.0 K'

# Generated at 2022-06-22 13:29:30.685931
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = tqdm_rich(range(1000000), unit="B")
    rc = RateColumn(unit="")

    task.desc = "Testing"
    task.update(1000)
    assert rc.render(task) == Text('976.56 KB/s', style='progress.data.speed')

# Generated at 2022-06-22 13:29:34.397670
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    iterable = [1, 2]
    with tqdm_rich(iterable, desc="foo") as t:
        t.reset(total=10)
        iterable.append(3)
        iterable.append(4)
    return t

# Generated at 2022-06-22 13:29:43.066457
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = type('', (), {'speed': None, 'description': None})()
    task.description = "Loading... "
    task.speed = 100
    rate_column = RateColumn(unit="B")
    assert rate_column.render(task) == Text("100 B/s", style="progress.data.speed")

    task.speed = 1000
    assert rate_column.render(task) == Text("1 K/s", style="progress.data.speed")

    task.speed = 1000000
    assert rate_column.render(task) == Text("1 M/s", style="progress.data.speed")

    task.speed = 1000000000
    assert rate_column.render(task) == Text("1 G/s", style="progress.data.speed")

    task.speed = 1000000000000

# Generated at 2022-06-22 13:29:47.529574
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    Test class FractionColumn
    """
    task = std_tqdm(total=123456789, position=0, desc="Downloading file")
    assert FractionColumn().render(task) == Text('0/123,456,789 ', style='progress.download')



# Generated at 2022-06-22 13:29:51.600012
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    >>> t = tqdm_rich(total=5, leave=True)
    >>> for _ in t:
    ...     t.reset(total=2)
    2/2 [============================] 100%

    """
    pass

# Generated at 2022-06-22 13:29:56.698376
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    for _ in tqdm_rich(range(4), desc='test'):
        pass

# Generated at 2022-06-22 13:29:58.720614
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    pass

# Generated at 2022-06-22 13:30:09.794040
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test render method of class RateColumn."""
    import pytest
    from rich.progress import Progress
    from tqdm.rich.progress_test import Task
    total = 100
    completed = 3
    speed = 54
    task = Task(total, completed, speed)
    rate_column = RateColumn()
    progress = Progress(rate_column)
    progress.start()
    assert rate_column.render(task) == Text('54.00  /s', style='progress.data.speed'),\
        'rate column should be 54  /s'
    progress.stop()
    rate_column = RateColumn(unit_scale=True)
    progress = Progress(rate_column)
    progress.start()

# Generated at 2022-06-22 13:30:17.104336
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fraction_column = FractionColumn(unit_scale=False, unit_divisor=1000)
    assert fraction_column.render(Progress(description="description", completed=1, total=1000)).text == "1.0/1000 "
    assert fraction_column.render(Progress(description="description", completed=200, total=1000)).text == "200.0/1000 "
    assert fraction_column.render(Progress(description="description", completed=200, total=2000)).text == "0.1/2.0 "

# Generated at 2022-06-22 13:30:19.767565
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    import time
    for _ in tqdm_rich(range(4)):
        time.sleep(0.5)
        tqdm_rich.clear()
        time.sleep(0.5)

# Generated at 2022-06-22 13:30:28.400720
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from rich.progress import TaskID
    from unittest.mock import Mock
    from unittest import TestCase

    class TestFractionColumn(TestCase):
        def test_with_scale(self):
            column = FractionColumn(unit_scale=True)
            task = Mock(TaskID, completed=0.5, total=2.3)
            self.assertEqual(column.render(task), '0.5/2.3 B')
            
            task = Mock(TaskID, completed=0.5, total=230)
            self.assertEqual(column.render(task), '0.5/230 B')

            task = Mock(TaskID, completed=500, total=230)
            self.assertEqual(column.render(task), '500.0/230 KB')


# Generated at 2022-06-22 13:30:31.748938
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from math import inf
    from .gui import tnrange

    with tnrange(0, inf, desc="my bar!") as bar:
        bar.__class__.display(bar)

# Generated at 2022-06-22 13:30:38.276510
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from unittest.mock import patch
    with patch.object(tqdm_rich, 'display') as mock_display:
        for total_number in [100, 1000]:
            tqdm_rich.reset(total=total_number)
            assert tqdm_rich.total == total_number
            tqdm_rich.n = total_number
            mock_display.assert_called_with(tqdm_rich)

# Generated at 2022-06-22 13:30:48.233475
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import math
    # given
    task = object()
    task.speed = 500
    # when
    rate_column = RateColumn(unit_scale=True, unit_divisor=1000)
    # then
    assert rate_column.render(task) == Text("500.0 B/s", style="progress.data.speed")
    # given
    task.speed = 10000
    # when
    rate_column = RateColumn(unit_scale=True, unit_divisor=1000)
    # then
    assert rate_column.render(task) == Text("10.0 K/s", style="progress.data.speed")
    # given
    task.speed = 10000000
    # when
    rate_column = RateColumn(unit_scale=True, unit_divisor=1000)
    # then
    assert rate_

# Generated at 2022-06-22 13:30:59.572311
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.progress import Progress, TaskID
    from rich.console import Console
    from unittest.mock import patch
    with patch('rich.progress.Progress') as MockedProgress:
        tqdm_rich_obj = tqdm_rich(total=100)
        tqdm_rich_obj.disable = False
        tqdm_rich_obj.n = 20
        tqdm_rich_obj.desc = "Desc"
        tqdm_rich_obj.format_dict = {'int_completed_len': 5}
        mocked_progress = Progress()
        mocked_progress.update = lambda x, y, z: x
        mocked_progress.add_task = lambda x, **kwargs: TaskID(1)
        MockedProgress.return_value = mocked_progress
        tqdm_rich_obj

# Generated at 2022-06-22 13:31:12.355735
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import pytest
    from .rich import RateColumn
    rate = RateColumn()

    assert rate.render(object()) == Text('? /s', style='progress.data.speed')
    assert rate.render(object(), speed=0) == Text('0 /s', style='progress.data.speed')
    assert rate.render(object(), speed=1) == Text('1 /s', style='progress.data.speed')
    assert rate.render(object(), speed=10) == Text('10 /s', style='progress.data.speed')
    assert rate.render(object(), speed=100) == Text('100 /s', style='progress.data.speed')



# Generated at 2022-06-22 13:31:15.998310
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich.progress import TaskID
    t = tqdm_rich(total=10)
    t._task_id = TaskID.temp()
    t.display()
    t.close()

# Generated at 2022-06-22 13:31:21.632412
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """tqdm.tqdm.tqdm_rich test."""
    from time import sleep
    expected_str = " 100%|██████████| 100/100 [00:00<00:00, 534.05it/s]"
    t = tqdm_rich(total=100)
    for i in range(100):
        sleep(0.001)
        t.update()
    t.close()
    t.clear()
    assert str(t) == expected_str

# Generated at 2022-06-22 13:31:33.072829
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from .std import tqdm as std_tqdm
    from .utils import _range
    #  estimate of number of remaining iterations
    estimate = 9999
    #  estimate of number of total iterations
    maximum = 10000
    for i in std_tqdm(_range(estimate),
                      total=maximum,
                      mininterval=0,
                      miniters=None,
                      unit_scale=False,
                      unit_divisor=1000,
                      leave=False):
        print(FractionColumn(unit_scale=False, unit_divisor=1000).render(i))

# Generated at 2022-06-22 13:31:45.672434
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """FractionColumn class should output correct and
    expected string when calling the method render.
    """
    class MockTask:
        def __init__(self, completed, total):
            self.completed = completed
            self.total = total
    fc = FractionColumn(unit_scale=False, unit_divisor=1000)
    fc_scaled = FractionColumn(unit_scale=True, unit_divisor=1000)
    fc_mmdd = FractionColumn(unit_scale=False, unit_divisor=1024)
    assert fc.render(MockTask(0, 0)) == Text("0.0/0.0 ", style="progress.download")

# Generated at 2022-06-22 13:31:47.250338
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    t = tqdm_rich(total=10)
    t.reset()
    t.close()

# Generated at 2022-06-22 13:31:49.213265
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    fc = FractionColumn()
    task = object()
    task.completed = 5
    task.total = 6
    assert fc.render(task)

# Generated at 2022-06-22 13:32:00.239358
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(0, 0, 0, 0) == "? /s"
    assert RateColumn(unit_scale=True).render(0, 0, 0, 0) == "? /s"
    assert RateColumn(unit_scale=False).render(0, 0, 0, 0) == "? /s"
    assert RateColumn().render(100, 0, 100, 0) == "100.0 /s"
    assert RateColumn(unit_scale=True).render(100, 0, 100, 0) == "100.0 /s"
    assert RateColumn(unit_scale=False).render(100, 0, 100, 0) == "100.0 /s"
    assert RateColumn().render(1000, 0, 100, 0) == "10.0 K/s"
    assert RateColumn(unit_scale=True).render

# Generated at 2022-06-22 13:32:07.896999
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    Test the method FractionColumn.render.
    """
    # Arrange
    task = Progress(min=0, max=2.3)
    task.value = 0.5
    expected = Text("0.5/2.3 ", style="progress.download")

    # Act
    actual = FractionColumn().render(task)

    # Assert
    assert str(actual) == str(expected)


# Generated at 2022-06-22 13:32:12.771012
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = tqdm_rich(total=256)
    column = RateColumn(unit="B", unit_scale=False, unit_divisor=1000)
    actual = column.render(task)
    expected = Text("0.000000 B/s", style="progress.data.speed")
    assert actual == expected

# Generated at 2022-06-22 13:32:32.802559
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import os
    import time
    from rich.progress import Progress
    test_file_name = os.path.join(os.path.abspath(__package__), "tests", "test.txt")
    f = open(test_file_name, "r")

    p = Progress(
        f"Reading file '{test_file_name}'",
        BarColumn(),
        FractionColumn(),
        time_remaining=True,
        transient=True
    )
    p.__enter__()
    task_id = p.add_task(
        f"Reading file '{test_file_name}'",
        total=os.path.getsize(test_file_name),
        completed=0,
        started_at=time.time(),
        end_at=None)

# Generated at 2022-06-22 13:32:43.674448
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    """ Test method clear of class tqdm_rich """
    import sys
    import io
    # capture the standard output
    std_display_capture = io.StringIO()
    sys.stderr = std_display_capture
    # capture the standard error output
    std_error_capture = io.StringIO()
    sys.stderr = std_error_capture
    # test the method
    tqdm_rich(disable=False, total=100).clear()
    tqdm_rich(disable=True, total=100).clear()
    # check the standard output
    std_display_capture.seek(0)
    assert std_display_capture.read() == ''
    std_display_capture.close()
    # check the standard error output

# Generated at 2022-06-22 13:32:45.388575
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich(total=3)
    t.display()
    t.update()
    t.update()
    t.update()
    t.close()

# Generated at 2022-06-22 13:32:48.018451
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    if not hasattr(tqdm_rich, '_prog'):
        return
    with tqdm_rich(total=10, desc="progress:", unit="B") as t:
        t.reset(10)

# Generated at 2022-06-22 13:32:51.756826
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test method 'reset' of class tqdm_rich."""
    bar = tqdm_rich(total=10)
    bar.reset(total=20)
    assert(bar._prog.total == 20)
    assert(bar.total == 20)
    bar.reset()
    assert(bar._prog.total == 10)
    assert(bar.total == 10)

# Generated at 2022-06-22 13:32:53.336808
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    r = RateColumn(unit="B")
    assert r.render(None) == Text("? B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:33:05.237596
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    Test method render of class FractionColumn.
    """
    from rich.text import Text
    column = FractionColumn()
    assert column.render(None) == Text('0.0/0.0')
    assert column.render({'completed': 1024, 'total': 1024}) == Text('1.0/1.0')
    assert column.render({'completed': 2048, 'total': 1024}) == Text('2.0/1.0')
    # Test unit_scale
    column = FractionColumn(True)
    assert column.render({'completed': 1024, 'total': 1024}) == Text('1.0/1.0')
    assert column.render({'completed': 2048, 'total': 1024}) == Text('2.0/1.0')

# Generated at 2022-06-22 13:33:07.280765
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    t = tqdm_rich(desc="Test", total=0)
    assert t.desc == "Test"
    t.close()

# Generated at 2022-06-22 13:33:08.969742
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm_rich(total=10) as pbar: # pylint: disable=unused-variable
        pbar.display()

# Generated at 2022-06-22 13:33:21.214103
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    import time
    import math

    with tqdm(total=10) as progress:
        for x in range(10):
            progress.update(1)
            time.sleep(0.1)

    with tqdm(total=2) as progress:
        for x in (1, 2):
            progress.update(1)
            time.sleep(0.1)

    with tqdm(total=10) as progress:
        for x in range(10, 20):
            progress.update(1)
            time.sleep(0.1)

    with tqdm(total=10, desc="10items") as progress:
        for x in range(10):
            progress.update(1)
            time.sleep(0.1)


# Generated at 2022-06-22 13:33:39.108770
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm(disable=False) as pbar:
        pass


# Generated at 2022-06-22 13:33:45.014402
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from time import sleep

    for i in tqdm_rich(total=3):
        sleep(0.1)
        if i == 1:
            tqdm_rich.reset(total=3**3)
        if i == 2:
            tqdm_rich.reset(total=3**4)



# Generated at 2022-06-22 13:33:49.533455
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for total in [0, 10,30]:
        with tqdm_rich(total=total) as t:
            for i in _range(10):
                t.update()
                if i == 5:
                    t.reset(total=20)
                    assert t.total == 20, "Total number of iteration is wrong after reset"
                    assert t.n == 0, "Current number of iteration is wrong after reset"

# Generated at 2022-06-22 13:33:58.886906
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = ProgressColumn.Task()
    task.completed = 123
    task.total     = 456
    assert(FractionColumn(False, 1).render(task) == Text("123/456", style="progress.download"))
    assert(FractionColumn(False, 1000).render(task) == Text("123/456 K", style="progress.download"))
    assert(FractionColumn(False, 1000000).render(task) == Text("123/456 M", style="progress.download"))
    assert(FractionColumn(True, 1).render(task) == Text("0/1", style="progress.download"))
    assert(FractionColumn(True, 1000).render(task) == Text("0/1 K", style="progress.download"))

# Generated at 2022-06-22 13:34:01.101502
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm(total=10) as t:
        for i in range(5):
            t.update()
            if i == 2:
                t.reset()
        for i in range(10):
            t.update()

# Generated at 2022-06-22 13:34:12.483498
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Unit test for FractionColumn.render() method."""
    # 1. test unit is float
    # 10.0/50.0
    task = object()
    task.completed = 10.0
    task.total = 50.0
    column = FractionColumn()
    assert column.render(task) == Text(
        "10.0/50.0", style="progress.download")

    # 2. test unit is float with precision of 2
    # 10.23/50.234
    task = object()
    task.completed = 10.23
    task.total = 50.234
    column = FractionColumn()
    assert column.render(task) == Text(
        "10.23/50.23", style="progress.download")

    # 3. test unit is int
    # 10/50

# Generated at 2022-06-22 13:34:15.316998
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    progress = tqdm_rich(total=5, disable=True)
    progress.display()
    progress.disable = False
    progress.format_dict = {"n": 10}
    progress.display()

# Generated at 2022-06-22 13:34:17.475939
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(total=10) as pbar:
        pbar.update(5)
    assert pbar.n == 0

# Generated at 2022-06-22 13:34:25.181035
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import unittest
    from rich.console import Console

    class UnitTest(unittest.TestCase):
        def test_RateColumn_render(self):
            console = Console()
            column = RateColumn()

            # Test if column displays '?' when task.speed is None
            task = console.progress.add_task('Test', start=True)
            result = column.render(task)
            self.assertEqual(result, '? /s')

            # Test if column displays correct message with task.speed
            task.start(total=10)
            task.update(5)
            result = column.render(task)
            self.assertEqual(result, '0.5 /s')
            task.update(10)
            result = column.render(task)

# Generated at 2022-06-22 13:34:36.043838
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = tqdm_rich(
        total=123456789,
        unit_scale=True,
        unit_divisor=1000,
        disable=True)
    task.n = 678
    task.last_print_n = 0
    task.start_t = 0.0
    task.last_print_t = 0.0
    task.desc = "test"
    task.dynamic_ncols = True
    task.smoothing = 0.9
    task.bar_format = "[{desc}{bar}]{percentage:>4.0f}%|{fraction}|"
    task.total_time = 0.0
    task.iterable = None
    task.ncols = 0
    task.ascii = False
    task.unit = None
    task.unit

# Generated at 2022-06-22 13:35:19.224256
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress = Progress(
        "[percentage]{task.percentage:>4.0f}%",
        " | ",
        FractionColumn(unit_scale=True),
        " | ",
        RateColumn(unit_scale=True),
        " | ",
        "[progress.description]{task.description}")
    with progress:
        task_id = progress.add_task(
            "Downloading",
            total=1234567,
            start=True,
            description="test",
        )
    for i in _range(1234567):
        progress.update(task_id, completed=i)
    progress.update(task_id, completed=1234567)

# Generated at 2022-06-22 13:35:29.580646
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    import os
    from rich.progress import (
        Progress,
        Column,
        TimeRemainingColumn,
        BarColumn,
    )
    from .tqdm_std import tqdm

    def not_visible():
        tq = tqdm_rich(
            total=11,
            leave=True,
            smoothing=0.5,
            disable=False,
            unit="test",
            unit_scale=True,
            desc="not_visible",
            bar_format="{desc}{percentage:3.0f}%|{bar}|",
        )
        for _ in tq:
            pass
        tq.close()


# Generated at 2022-06-22 13:35:32.254393
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = Progress(total=100)
    task.completed = 20
    column = FractionColumn()
    assert column.render(task) == Text('20.0/100', style='progress.download')



# Generated at 2022-06-22 13:35:32.851707
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    pass

# Generated at 2022-06-22 13:35:37.030288
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task=Progress()
    task.completed=20
    task.total=30
    test=FractionColumn()
    assert ("20.0" in test.render(task))
    assert ("30.0" in test.render(task))


# Generated at 2022-06-22 13:35:48.413233
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # When there is no speed
    rate_cl = RateColumn()
    task = tqdm_rich(total=1)
    assert rate_cl.render(task) == Text(f"? /s", style="progress.data.speed")
    # When there is a speed and unit_scale is False
    task = tqdm_rich(total=1, unit="B")
    task.n = 0.39
    assert rate_cl.render(task) == Text(f"0.3 /s", style="progress.data.speed")
    # When there is a speed and unit_scale is True
    task = tqdm_rich(total=1, unit="B", unit_scale=True)
    task.n = 100000000

# Generated at 2022-06-22 13:36:00.296038
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    from .std import tqdm as std_tqdm
    from .std import trange as std_trange

    for i in tqdm_rich(range(10)):  # all defaults
        pass

    for i in tqdm_rich(range(10), desc="test", mininterval=0):
        pass

    for i in tqdm_rich(range(10), bar_format="test %s"):
        pass

    for i in tqdm_rich(range(10), mininterval=0, smoothing=0):
        pass

    for i in tqdm_rich(range(10), file=open(__file__, 'w')):
        pass

    for i in tqdm_rich(range(10), ncols=80):
        pass


# Generated at 2022-06-22 13:36:10.642589
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.progress import Progress
    from tqdm.rich import RateColumn

    unit = "B"
    unit_divisor = 1000
    unit_scale = False
    transfer_speed = 8123

    rate_column = RateColumn(
            unit=unit, unit_scale=unit_scale, unit_divisor=unit_divisor)
    progress = Progress(rate_column)
    task = progress.add_task(total=1, speed=transfer_speed)
    assert rate_column.render(task) == Text(f"8{unit}/s", style="progress.data.speed")

# Generated at 2022-06-22 13:36:16.465269
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = object()
    task.completed = 1
    task.total = 1024
    assert FractionColumn(False).render(task) == Text('1/1024', style='progress.download')
    assert FractionColumn(True, 1000).render(task) == \
           Text('0.001/1.000 kb', style='progress.download')
    assert FractionColumn(True, 1024).render(task) == \
           Text('0.000/1.000 kb', style='progress.download')


# Generated at 2022-06-22 13:36:20.274057
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test display method of class tqdm_rich."""
    t = tqdm_rich(total=10, unit='B', unit_scale=True, unit_divisor=1024)
    t.display()
    t.close()