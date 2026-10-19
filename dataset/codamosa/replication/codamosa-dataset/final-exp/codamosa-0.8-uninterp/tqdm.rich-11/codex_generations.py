

# Generated at 2022-06-22 13:27:39.946537
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # Tests: no '\r' used
    for _ in tqdm_rich(range(4)):
        pass
    # Tests: no excessive prints
    for _ in tqdm_rich(range(4), file=open(os.devnull, 'w')):
        pass

# Generated at 2022-06-22 13:27:50.877319
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    from datetime import timezone
    # test for '0/0'
    task = Progress.Task(total=0, completed=0, start_time=1575494683.341116, description=None,
                         start_time_global=1575494683.341116, timezone=timezone.utc)
    column = FractionColumn(unit_scale=True, unit_divisor=1000)
    assert column.render(task) == Text(
        "0.0/0.0 ", style="progress.download")
    # test for '0/1'

# Generated at 2022-06-22 13:27:52.959585
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    pbar = tqdm_rich(total=1, disable=False)
    pbar.display()

# Generated at 2022-06-22 13:27:57.963198
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = tqdm_rich(total=10, unit_scale=True, unit="B")
    for i in range(0, 10):
        task.update(1)
    task.close()
    assert task._prog.render() == '20.0 KB/s'


# Generated at 2022-06-22 13:27:59.827807
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(1) as t:
        t.clear()



# Generated at 2022-06-22 13:28:02.153770
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    for _ in tqdm(range(100), desc='test_tqdm_rich_clear'):
        pass

# Generated at 2022-06-22 13:28:13.900180
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich.console import Console
    from rich.panel import Panel
    console = Console()
    progress = Progress(
        Panel('[rate]{task.speed}'),
        RateColumn()
    )
    progress.__enter__()
    task_id = progress.add_task('test', speed=None)
    progress.update(task_id)
    print(console.render())
    progress.update(task_id, speed=1000)
    print(console.render())
    progress.update(task_id, speed=1024)
    print(console.render())
    progress.update(task_id, speed=1536)
    print(console.render())


if __name__ == "__main__":
    test_RateColumn_render()

# Generated at 2022-06-22 13:28:26.818042
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Unit test for RateColumn.render."""
    rate_column = RateColumn()
    task = type("Task", (), {"speed": None})()
    assert rate_column.render(task) == Text("? /s", style="progress.data.speed")
    task = type("Task", (), {"speed": 0})()
    assert rate_column.render(task) == Text("0 /s", style="progress.data.speed")
    task = type("Task", (), {"speed": 1000})()
    assert rate_column.render(task) == Text("1.0 K/s", style="progress.data.speed")
    rate_column = RateColumn(unit_scale=True)
    assert rate_column.render(task) == Text("1000 /s", style="progress.data.speed")

# Generated at 2022-06-22 13:28:30.407542
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = trange(10)
    task.update(5)
    task.total = 13.5
    test_FractionColumn = FractionColumn()
    assert test_FractionColumn.render(task) == \
        Text('5.0/13.5 ', style='progress.download')

# Generated at 2022-06-22 13:28:38.161582
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # int, str
    rc = RateColumn(unit="B")
    assert rc.render(1, 12) == '? B/s'
    assert rc.render(1, "12") == '? B/s'
    assert rc.render(1, "12.0") == '? B/s'
    assert rc.render(1, "12.1") == '? B/s'
    assert rc.render(1, "12.01") == '? B/s'
    # int, str, unit_scale=True
    rc = RateColumn(unit="B", unit_scale=True)
    assert rc.render(1, "12") == '? B/s'
    assert rc.render(1, "12.0") == '? B/s'
    assert rc.render(1, "12.1")

# Generated at 2022-06-22 13:28:45.231093
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    for _ in tqdm(range(1000)):
        pass
    for i in tqdm(range(1000)):
        if i == 500:
            tqdm.clear()
        pass


# This function is a dummy function to show the extra arguments of tqdm
# and their default values.

# Generated at 2022-06-22 13:28:53.395041
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    tqdm_test = tqdm_rich(total=100, ncols=80)
    cls_rate_column = RateColumn()
    cls_rate_column.render(tqdm_test)
    assert cls_rate_column.render(tqdm_test).__str__() == '0.00 B/s'
    tqdm_test.total=1024
    cls_rate_column.render(tqdm_test)
    assert cls_rate_column.render(tqdm_test).__str__() == '0.00 K/s'
    tqdm_test.total=1025
    cls_rate_column.render(tqdm_test)

# Generated at 2022-06-22 13:28:57.903736
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    import shutil
    from time import sleep
    from rich.progress import Progress as progress_bar
    from rich.progress import BarColumn as progress_bar_column
    from rich.progress import FractionColumn as progress_bar_fraction_column
    from rich.progress import TimeRemainingColumn as progress_bar_time_remaining_column
    from rich.progress import TimeElapsedColumn as progress_bar_time_elapsed_column
    from rich.progress import RateColumn as progress_bar_rate_column
    bar = tqdm_rich(
        desc="Test tqdm_rich.reset() method",
        total = 100,
        leave = True,
        unit = 'B',
        unit_scale = True,
        unit_divisor = 1024,
    )
    bar._prog = progress_bar

# Generated at 2022-06-22 13:29:01.300815
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from .gui import tgrange
    from time import sleep
    for _ in tgrange(1):
        sleep(0.25)

# Generated at 2022-06-22 13:29:06.747301
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    """
    Test the method clear of class tqdm_rich.
    """
    with tqdm_rich(total=10) as pbar:
        assert pbar.disable == False
        assert hasattr(pbar, '_prog')
        pbar._prog.__exit__(None, None, None)
        delattr(pbar, '_prog')
        pbar.clear()
    return


# Generated at 2022-06-22 13:29:17.133712
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn()
    assert rate_column.render(task=None) == Text('? /s', style='progress.data.speed')
    assert rate_column.render(task=0) == Text('0.0 /s', style='progress.data.speed')
    assert rate_column.render(task=1000) == Text('1.0 /s', style='progress.data.speed')
    rate_column = RateColumn(unit_scale=True)
    assert rate_column.render(task=1000) == Text('1.0 K/s', style='progress.data.speed')
    assert rate_column.render(task=1000000) == Text('1.0 M/s', style='progress.data.speed')


# Generated at 2022-06-22 13:29:17.978863
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    pass

# Generated at 2022-06-22 13:29:30.510164
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    def _(task):
        task.speed = 1
        return RateColumn(unit="B").render(task)

    assert(str(_) == "1.0 B/s")
    assert(_.style == "progress.data.speed")

    _.unit_scale = True
    assert(str(_) == "1.0 B/s")
    assert(_.style == "progress.data.speed")
    _.unit_scale = False

    _.unit_divisor = 1024
    assert(str(_) == "0.9 K/s")
    assert(_.style == "progress.data.speed")
    _.unit_divisor = 1000

    task.speed = 100
    assert(str(_) == "100.0 B/s")
    assert(_.style == "progress.data.speed")

    task.speed

# Generated at 2022-06-22 13:29:33.917988
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .tqdm import TqdmTypeError
    try:
        t = tqdm_rich(disable=False)
        t.display()
    except TqdmTypeError:
        pass

# Generated at 2022-06-22 13:29:42.744936
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    progress = Progress()
    fraction_column = FractionColumn(unit_divisor=1000)
    task = progress.add_task(total=100000)
    task.completed = 500.0
    assert fraction_column.render(task) == Text("0.5/100.0", style="progress.download")
    task.completed = 500000.0
    assert fraction_column.render(task) == Text("0.5/1.0 K", style="progress.download")
    task.completed = 5000000.0
    assert fraction_column.render(task) == Text("0.5/10.0 K", style="progress.download")
    task.completed = 50000000.0
    assert fraction_column.render(task) == Text("0.5/100.0 K", style="progress.download")
    task

# Generated at 2022-06-22 13:29:53.723802
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test for the progress of method display in class tqdm_rich."""
    for i in tqdm_rich(total=100, disable=False):
        i = i + 1
        tqdm_rich.display(total=100, i=i)


# Generated at 2022-06-22 13:30:01.604640
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from io import BytesIO
    from rich.console import Console
    from rich.progress import TaskID

    def fake_update(self, task_id, *args, **kwargs):
        self.task_id = task_id
        self.args = args
        self.kwargs = kwargs

    o = BytesIO()
    console = Console(file=o)
    console.print = fake_update
    prog = Progress(console=console)
    task_id = TaskID()
    task = tqdm_rich(total=10, console=console, desc="Hello World!", task_id=task_id)
    task.display()
    prog.__exit__(None, None, None)
    assert prog.task_id == task_id
    assert prog.args == (10, "Hello World!")

# Generated at 2022-06-22 13:30:11.601281
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate = RateColumn()
    assert rate.render(100) == Text("100.0 /s", style="progress.data.speed")
    assert rate.render(1000) == Text("1.0 K/s", style="progress.data.speed")
    assert rate.render(1024) == Text("1.0 K/s", style="progress.data.speed")
    assert rate.render(1025) == Text("1.0 K/s", style="progress.data.speed")
    assert rate.render(1048576) == Text("1.0 M/s", style="progress.data.speed")
    assert rate.render(1073741824) == Text("1.0 G/s", style="progress.data.speed")

# Generated at 2022-06-22 13:30:20.990159
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    # Test for unit scale = False
    task = object()
    task.completed = 1
    task.total = 2
    fraction_column = FractionColumn(unit_scale=False)
    text = fraction_column.render(task)
    assert text.plain == "1.0/2.0 "
    assert text.style_name == "progress.download"
    # Test for unit scale = True
    task.total = 1000000
    fraction_column = FractionColumn(unit_scale=True)
    text = fraction_column.render(task)
    assert text.plain == "1.0/1.0 K"
    assert text.style_name == "progress.download"
    # Test for unit divisor = 1024

# Generated at 2022-06-22 13:30:24.681438
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    def generate_tqdm_rich_display():
        for i in tqdm_rich(range(10), disable=False, miniters=1, smoothing=1):
            yield i

    for _ in generate_tqdm_rich_display():
        pass

# Generated at 2022-06-22 13:30:27.586838
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    assert FractionColumn().render(ProgressColumn.dummy_task(100, 500)) == Text('100/500')

# Generated at 2022-06-22 13:30:39.250556
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import os
    import io
    def remove_file(filename):
        '''
        Deletes file if the file exists
        '''
        if os.path.exists(filename):
            os.remove(filename)
        return None
    f_name = 'tqdm_log.txt'
    remove_file(f_name)
    # Empty DataFrame
    df = pd.DataFrame()
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(f_name, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    df = p

# Generated at 2022-06-22 13:30:48.714475
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="B", unit_scale=False, unit_divisor=1000)

    # 2 bytes per second
    task = std_tqdm(total=None)
    task.speed = 2
    rate = rate_column.render(task)
    assert str(rate) == '2.00 B/s', "rate=" + str(rate)

    # 200 bytes per second
    task.speed = 200
    rate = rate_column.render(task)
    assert str(rate) == '200.00 B/s', "rate=" + str(rate)

    # 1234567 bytes per second
    task.speed = 1234567
    rate = rate_column.render(task)
    assert str(rate) == '1.23 MB/s', "rate=" + str(rate)


# Generated at 2022-06-22 13:31:00.019626
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import os
    import pytest
    from .utils import FormatStub
    from .std import tqdm_gui

    os.environ["COLUMNS"] = "80"

    with FormatStub(False) as fmt:
        with tqdm_rich(total=10, unit='B', unit_scale=True, unit_divisor=1024) as t:
            for i in range(5):
                t.reset()
                t.update()


# Generated at 2022-06-22 13:31:11.548616
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    # Test case 1
    print(FractionColumn(unit_scale=True, unit_divisor=1000).render(task=tqdm_rich(3,unit_scale=True,unit_divisor=1000)))
    # Test case 2
    print(FractionColumn(unit_scale=False,unit_divisor=1000).render(task=tqdm_rich(4,unit_scale=False,unit_divisor=1000)))
    # Test case 3
    print(FractionColumn(unit_scale=True, unit_divisor=10000000).render(task=tqdm_rich(3,unit_scale=True,unit_divisor=10000000)))
    # Test case 4
    print(FractionColumn().render(task=tqdm_rich(3)))


# Generated at 2022-06-22 13:31:45.411194
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from tqdm.auto import tqdm as tqdm_std

    with tqdm_std(total=10, desc="Test for progress", unit_scale=True) as pbar:
        for i in _range(10):
            pbar.update()
            assert pbar.n == i + 1

        pbar.clear()
        assert pbar.n == 10

# Generated at 2022-06-22 13:31:52.337747
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        import unittest.mock as mock
    except ImportError:
        import mock  # noqa
    mock_prog = mock.create_autospec(Progress)
    mock_prog.update.return_value = None
    mock_prog.__enter__.return_value = None
    mock_prog.__exit__.return_value = None
    mock_prog.add_task.return_value = 4

# Generated at 2022-06-22 13:32:00.765845
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn().render(None).text == "? /s"
    assert RateColumn().render(None, speed=None).text == "? /s"
    assert RateColumn().render(None, speed=123).text == "123 /s"
    assert RateColumn(unit_scale=True).render(None, speed=123000).text == "123K /s"
    assert RateColumn(unit="b").render(None, speed=123).text == "123 b/s"
    assert RateColumn(unit_scale=True, unit="b").render(None, speed=123000).text == "123Kb/s"

# Generated at 2022-06-22 13:32:13.605010
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Unit test for method render of class RateColumn."""
    rcol = RateColumn()
    assert rcol.render(ProgressColumn().task) == Text(
        "0.0 /s",
        style="progress.data.speed")
    assert rcol.render(ProgressColumn(
        task=ProgressColumn().task, speed=500
    )).text == "500.0 /s"
    assert rcol.render(ProgressColumn(
        task=ProgressColumn().task, speed=5000
    )).text == "5.0 K/s"
    rcol = RateColumn(unit_scale=True, unit_divisor=1024)
    assert rcol.render(ProgressColumn(
        task=ProgressColumn().task, speed=5000
    )).text == "4.88 K/s"

# Generated at 2022-06-22 13:32:25.029830
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    progress = Progress(
        "[progress.description]{task.description}"
        "[progress.percentage]{task.percentage:>4.0f}%",
        BarColumn(bar_width=None),
        FractionColumn(unit_scale=True, unit_divisor=1024),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(),
        ",", RateColumn(unit='B', unit_scale=True, unit_divisor=1024), "]"
    )
    task = progress.add_task("", total=1024, position=0, initial=True)
    # When speed is None
    progress.update(task, speed=None)

# Generated at 2022-06-22 13:32:28.589521
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = lambda: None  # a simple function that does nothing
    task.completed = 0
    task.total = 5000
    task.speed = 500
    assert RateColumn().render(task) == "[2B/s]"

# Generated at 2022-06-22 13:32:40.774394
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    # Almost same test as in test_std.py
    import time
    import sys
    import os

    with tqdm(total=50) as pbar:
        for i in range(8):
            pbar.update(5)
            time.sleep(0.2)
            assert str(pbar)
            assert str(pbar) != ""

        # test with dynamic monitor
        if sys.version_info[0] == 2:
            from StringIO import StringIO
        else:
            from io import StringIO


# Generated at 2022-06-22 13:32:50.111216
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # Test 1: 
    task = std_tqdm.tqdm(total=1001, desc="test", gui=True)
    task.n = 1000
    task.start_t = 1000
    task.total = 1001
    task.speed = 2
    task.update_to(1000)
    task.close()
    assert RateColumn().render(task) == Text('0.5 K/s', style='progress.data.speed')

    # Test 2: 
    task = std_tqdm.tqdm(total=1001, desc="test", gui=True)
    task.n = 1000
    task.start_t = 1000
    task.total = 1001
    task.speed = 2
    task.update_to(1000)
    task.close()

# Generated at 2022-06-22 13:32:58.973761
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import time

    # simple test with total parameters
    with tqdm(total=100) as t:
        for i in range(10):
            time.sleep(.1)
            t.reset(total=i)
    assert t.n == 10
    assert t.total == 10

    # here, total is left unchanged
    with tqdm(total=100) as t:
        for i in range(10):
            time.sleep(.1)
            t.reset()
    assert t.n == 10
    assert t.total == 100
    print("Test of function test_tqdm_rich_reset passed!")

# Generated at 2022-06-22 13:33:00.433935
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():  # pragma: no cover
    """Test tqdm_rich method clear"""
    with tqdm_rich(total=10) as bar:
        for i in _range(10):
            bar.update()
        assert True

# Generated at 2022-06-22 13:33:27.159281
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """
    Unit test for method `display` of class `tqdm_rich`.

    Returns
    -------
    None.

    """
    bar = tqdm_rich(range(4))
    for i in bar:
        bar.display()
    bar.close()

# Generated at 2022-06-22 13:33:37.731279
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from rich import print
    r_c = RateColumn()
    unit, suffix = filesize.pick_unit_and_suffix(123-1, [""], 1)
    assert str(r_c.render(unit)) == f"122  /s"
    unit, suffix = filesize.pick_unit_and_suffix(123, ["K"], 1000)
    assert str(r_c.render(unit)) == f"0.1 K/s"
    unit, suffix = filesize.pick_unit_and_suffix(123, ["K"], 1024)
    assert str(r_c.render(unit)) == f"0.1  /s"
    unit, suffix = filesize.pick_unit_and_suffix(12345, ["K", "M"], 1024)
    assert str(r_c.render(unit))

# Generated at 2022-06-22 13:33:44.732913
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import time
    # backspace test
    with tqdm(total=100) as pbar:
        for i in range(100):
            time.sleep(0.01)
            pbar.update()
        pbar.display()
        # Tests that a new line is added.
        print("Hello World!")


if __name__ == '__main__':
    test_tqdm_rich_display()

# Generated at 2022-06-22 13:33:51.759638
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch  # type: ignore[no-redef]  # pragma: no cover
    with patch("tqdm.rich.tqdm_rich.Progress") as progress:
        progress.return_value.add_task.return_value = 1
        with tqdm_rich(total=5) as t:
            t.display()
            assert t._prog.update.call_count == 1
            t.desc = "description"
            t.display()
            assert t._prog.update.call_count == 2
        assert t._prog.__exit__.call_count == 1

# Generated at 2022-06-22 13:34:01.687687
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import pytest
    r = RateColumn()
    class test_task:
        def __init__(self):
            self.completed = 0
            self.total = 1
            self.last_print_n = 0
            self.last_print_t = 0
    t = test_task()
    t.speed = None
    assert r.render(t) == Text(f"? /s", style="progress.data.speed")
    t.speed = 100
    assert r.render(t) == Text(f"100.00 /s", style="progress.data.speed")
    t.speed = 200
    assert r.render(t) == Text(f"200.00 /s", style="progress.data.speed")
    t.speed = 1000

# Generated at 2022-06-22 13:34:08.418255
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    try:
        t = tqdm_rich(desc='test')
        t.close()
    except TypeError as e:
        assert 'can\'t be used in a string context' in str(e)

    try:
        t = tqdm_rich(format='test')
    except TypeError as e:
        assert 'format is forbidden with gui' in str(e)

# Generated at 2022-06-22 13:34:09.360630
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    _tqdm_rich_reset()



# Generated at 2022-06-22 13:34:13.214473
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    pbar = tqdm_rich(range(100), desc='foo', unit='B', unit_scale=True, unit_divisor=1000)
    for i in pbar:
        pbar.reset()
    assert pbar.total == pbar.n == 0
    pbar.close()
    assert pbar._prog.is_done

# Generated at 2022-06-22 13:34:22.355183
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Test if method reset of class tqdm_rich works as expected
    """
    def test_reset(total, newtotal):
        t = tqdm_rich(total=total)
        assert t.total == total, "total value not set on init"
        t.reset(total=newtotal)
        assert t.total == newtotal, "total value not set on reset"

    # test for negative total:
    test_reset(total=-123, newtotal=-456)

    # test for None (unspecified) total:
    test_resets = [(None, -456), (-123, None)]
    for initial, final in test_resets:
        t = tqdm_rich(total=initial)
        t.reset(total=final)

# Generated at 2022-06-22 13:34:34.003202
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    test case of expected output based on different inputs.
    """
    col = FractionColumn()
    assert col.render({
        'completed': 0,
        'total': 0
    }) == Text(
        f"0.0/0.0 ", style="progress.download")
    assert col.render({
        'completed': 0,
        'total': 1
    }) == Text(
        f"0.0/1.0 ", style="progress.download")
    assert col.render({
        'completed': 0,
        'total': 10
    }) == Text(
        f"0.0/10.0 ", style="progress.download")

# Generated at 2022-06-22 13:35:09.162036
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from tqdm import trange
    for i in trange(4, desc='1st loop'):
        for j in trange(4, desc='2nd loop'):
            for k in trange(4, desc='3rd loop'):
                pass
    trange(4, desc='1st loop').close()
    trange(4, desc='2nd loop').close()
    trange(4, desc='3rd loop').close()

# Generated at 2022-06-22 13:35:20.141701
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn("/s", unit_scale=True, unit_divisor=1000).render("") == Text("? /s", style="progress.data.speed")
    assert RateColumn("/s", unit_scale=True, unit_divisor=1000).render("0") == Text("0.0 /s", style="progress.data.speed")
    assert RateColumn("/s", unit_scale=True, unit_divisor=1000).render("1000") == Text("1.0 K/s", style="progress.data.speed")
    assert RateColumn("/s", unit_scale=True, unit_divisor=1000).render("1000000") == Text("1.0 M/s", style="progress.data.speed")

# Generated at 2022-06-22 13:35:23.706570
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn(unit='b', unit_divisor=1024).render(None).text == '? b/s'
    assert RateColumn(unit='b', unit_divisor=1024).render(None).style == 'progress.data.speed'

# Generated at 2022-06-22 13:35:28.728883
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    bar = tqdm_rich(total=5, leave=False)
    for i in range(4):
        bar.update()
    bar.reset(total=10)
    for i in range(8):
        bar.update()
    for i in range(8):
        bar.update()

# Generated at 2022-06-22 13:35:29.983107
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    TODO: unit test for method render of class RateColumn
    """
    pass

# Generated at 2022-06-22 13:35:32.630016
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """ Unit test for `display` method of class `tqdm_rich` """
    from .tests.common import TestTqdm
    t = TestTqdm(tqdm_rich)
    t.test_display()

# Generated at 2022-06-22 13:35:35.840508
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    RateColumn(unit="a").render(tqdm_rich(total=None))
    RateColumn(unit_scale=False).render(tqdm_rich(total=10))
    RateColumn(unit_scale=True).render(tqdm_rich(total=1e30))
    RateColumn(unit="a", unit_scale=True).render(tqdm_rich(total=1e30))
    RateColumn(unit="a", unit_scale=True, unit_divisor=2).render(tqdm_rich(total=1e30))

# Generated at 2022-06-22 13:35:47.941691
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():
    from tqdm._tqdm import _time as time
    from tqdm.autonotebook import tqdm as tc

    if tc is tqdm_rich:
        import pytest
        pytest.skip()
        return
    time.sleep(0.01)

    with tqdm(total=10, leave=False) as t:
        for i in _range(10):
            time.sleep(0.01)
            t.update(1)
        time.sleep(0.1)
    with tqdm(total=100, leave=True, disable=True) as t:
        for i in _range(100):
            t.update(1)

# Generated at 2022-06-22 13:35:59.864162
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    class Task(object):
        """Mock rich.progress.Task for testing."""
        def __init__(self, completed, total):
            self.completed = completed
            self.total = total

    # set unit_scale=False, unit_divisor=1000
    progress_column = FractionColumn(unit_scale=False, unit_divisor=1000)
    task = Task(completed=128, total=512)
    assert progress_column.render(task).plain == '0.128/0.512 '

    # set unit_scale=True, unit_divisor=1000, since 1000 < 512, unit=1 and suffix=""
    progress_column = FractionColumn(unit_scale=True, unit_divisor=1000)
    task = Task(completed=128, total=512)
    assert progress_

# Generated at 2022-06-22 13:36:02.206291
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    import rich
    assert tqdm_rich.display in rich.progress.Progress.update_all.__code__.co_varnames


# Generated at 2022-06-22 13:37:01.186184
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    bar = tqdm_rich(total=100)
    for i in range(100):
        bar.update(1)
    bar.reset()
    for i in range(100):
        bar.update(1)
    bar.close()

# Generated at 2022-06-22 13:37:03.769719
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for t in [tqdm_rich(), trange(10)]:
        t.reset(10)
        t.reset(20)
        assert t.total == 20

# Generated at 2022-06-22 13:37:05.518472
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    task = std_tqdm(range(100), disable=True)
    self = FractionColumn()
    self.render(task)

# Generated at 2022-06-22 13:37:11.810605
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """
    Create a RateColumn object, temporarily set speed to a
    value, call the object's method render and check if the
    method gives the right output.
    """
    col = RateColumn()
    col.temp_speed = 1.234
    assert col.render(col).text == "1.23 1/s"



# Generated at 2022-06-22 13:37:16.023626
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from time import sleep
    from rich.console import Console
    console = Console()

    with tqdm_rich(total=100, bar_width=25) as progress:
        for i in progress:
            progress.display()
            sleep(0.1)

# Generated at 2022-06-22 13:37:23.832005
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    import json
    from rich.console import Console

    task = {}
    task["speed"] = 1
    with open("tests/test_RateColumn_render.json", "r") as f:
        progress = json.load(f)
    for rate_column in progress:
        new_rate_column = RateColumn(**rate_column)
        result = new_rate_column.render(task)
        console = Console()
        console.print(result)
        console.flush()



# Generated at 2022-06-22 13:37:26.241855
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    from .std import tqdm
    for i in tqdm_rich(range(100)):
        pass

# Generated at 2022-06-22 13:37:31.523674
# Unit test for constructor of class tqdm_rich
def test_tqdm_rich():  # pragma: no cover
    from .gui import tqdm as gui
    from .gui import tgrange
    from .gui import tqrange
    from .gui import tnrange
    for t in (tqdm, tgrange, tqrange, tnrange):
        assert isinstance(t(1, 2), tqdm_rich)