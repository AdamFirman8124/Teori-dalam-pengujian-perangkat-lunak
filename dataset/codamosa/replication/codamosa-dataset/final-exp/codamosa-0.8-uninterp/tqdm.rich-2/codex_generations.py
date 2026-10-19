

# Generated at 2022-06-22 13:27:48.008636
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Test for method display of class tqdm_rich"""
    from .gui import tqdm as module_tqdm
    # check display() works even if file blackhole is in effect
    module_tqdm(range(3)).close()
    # test for closing with no total
    module_tqdm(range(3), total=None).close()

# Generated at 2022-06-22 13:27:54.809071
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from rich import print
    from time import sleep
    from tqdm.auto import tqdm, trange
    from tqdm.contrib.concurrent import thread_map

    with tqdm(total=2) as pbar:
        for _ in range(2):
            for _ in trange(100):
                sleep(0.01)
            pbar.clear()
        print('HELLO')



# Generated at 2022-06-22 13:28:07.081678
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """Test method render with iterable and unknown bar length"""
    test_frac_col = FractionColumn()

# Generated at 2022-06-22 13:28:18.846717
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = tqdm_rich(total=100, unit='B')
    task.update(1)
    # This is a mock 'task' object
    task.speed = 160
    task.total = 400
    task.completed = 100
    # Result has to be '160.0 B/s'
    assert RateColumn().render(task) == '160.0 B/s'
    # Human readable format with unit scale
    assert RateColumn(unit_scale=True).render(task) == '0.2 K/s'
    # Human readable format with unit prefix K
    assert RateColumn(unit='K').render(task) == '0.00016 K/s'
    # Human readable format with unit prefix K and unit scale

# Generated at 2022-06-22 13:28:22.692767
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    val = 1
    try:
        for i in tqdm_rich(range(10), desc="Test"):
            val += i
    except ValueError:
        assert val == 55

# Generated at 2022-06-22 13:28:28.056458
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    with tqdm_rich(10) as t:
        t.display()
        t.reset(total=100)
        t.display()
        t.reset(total=10)
        t.display()
        t.reset(total=20)
        t.display()
        t.reset()
        t.display()

# Generated at 2022-06-22 13:28:30.585867
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(total=2) as pbar:
        pbar.clear()
        pbar.display()
        pbar.update(pbar.n + 1)
        pbar.clear()

# Generated at 2022-06-22 13:28:37.980378
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    t = 1
    s = 1000
    unit = 'K'
    u, suf = filesize.pick_unit_and_suffix(s, ["", "K", "M", "G", "T", "P", "E", "Z", "Y"], 1000)
    c = RateColumn(unit=unit, unit_scale=False)
    print(c.render(t, s, 100))

# Generated at 2022-06-22 13:28:39.465032
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    for _ in tqdm_rich(range(5)):
        pass

# Generated at 2022-06-22 13:28:50.175150
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    progress = Progress(FractionColumn())
    task = progress.add_task("test")
    task.update(1, 10)
    c = FractionColumn()
    c.render(task) == "0.1/10 "
    c = FractionColumn(True)
    c.render(task) == "0.1/10 k"
    c = FractionColumn(True, 1024)
    c.render(task) == "0.1k/10 "
    task.update(10, 10)
    c = FractionColumn()
    c.render(task) == "1/1 "
    c = FractionColumn(True)
    c.render(task) == "1/1 k"
    c = FractionColumn(True, 1024)
    c.render(task) == "1k/1 "

# Generated at 2022-06-22 13:29:00.241901
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    assert FractionColumn(True, 1000).render(
        {"task": {"completed": 1000, "total": 1200}}) == \
        "1.0/1.2 K"
    assert FractionColumn(False, 1000).render(
        {"task": {"completed": 1000, "total": 1200}}) == \
        "1,000/1,200 "
    assert FractionColumn(True, 100).render(
        {"task": {"completed": 1234567, "total": 1234567.7}}) == \
        "12.3/12.4 M"
    assert FractionColumn(True, 1000000).render(
        {"task": {"completed": 1234567, "total": 1234567.7}}) == \
        "1.2/1.2 M"

# Generated at 2022-06-22 13:29:06.237275
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # Define method
    rate_column = RateColumn()
    # Define mock for object task
    class MockTask():
        completed = 10
        description = "Test description"
        total = 100
        speed = 10
    # Mock object
    task = MockTask()
    # Call method
    result = rate_column.render(task)
    # Check result
    assert result.text == '10.0 /s'

# Generated at 2022-06-22 13:29:13.959707
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    def display():
        _ = '1:20:30'
        return _
    test_tqdm_rich = tqdm_rich(['a', 'b', 'c'], desc='Title',
                               total=10, unit='items', unit_scale=True, miniters=1)
    test_tqdm_rich.display = display
    test_tqdm_rich.display()
    assert True

# Generated at 2022-06-22 13:29:15.246736
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    for _ in tqdm_rich(range(10)):
        pass


# Generated at 2022-06-22 13:29:27.351099
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from rich.progress import Progress
    from rich.console import Console
    from rich import box
    import shutil
    from time import sleep
    for length in range(shutil.get_terminal_size()[0] - 10):
        if len(box("a", width=length)) != length:
            break
    else:
        length = shutil.get_terminal_size()[0] - 10
    progress = Progress(f"[progress.description]{' ' * length}", transient=True)
    progress.__enter__()
    task_id = progress.add_task("")
    progress.update(task_id, description="")
    # Clear
    progress.console.clear()
    for _ in range(3):
        progress.console.print(f"[progress.description]{' ' * length}")
        sleep

# Generated at 2022-06-22 13:29:30.216735
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm(total=10) as pbar:
        pbar.clear(nolock=True)

# Generated at 2022-06-22 13:29:37.455278
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from unittest import TestCase
    from io import StringIO
    from contextlib import redirect_stdout

    class TestTqdmRichDisplay(TestCase):
        def test_output(self):
            with redirect_stdout(StringIO()) as buf:
                with tqdm_rich(desc='Atomic bomb') as pbar:
                    pbar.display()
            self.assertEqual(buf.getvalue(), "Atomic bomb...\n")

    TestTqdmRichDisplay().test_output()

# Generated at 2022-06-22 13:29:44.401655
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    assert str(FractionColumn().render(
        std_tqdm._get_empty_task())) == "0.0/0.0 "
    assert str(FractionColumn(1, 1).render(
        std_tqdm._get_empty_task())) == "0.0/0.0 "
    assert str(FractionColumn(1, 1).render(
        std_tqdm._get_empty_task(total=2300))) == "0.0/2.3 K"
    assert str(FractionColumn(1, 1024).render(
        std_tqdm._get_empty_task(total=2300))) == "0.0/2.3 K"
    assert str(FractionColumn(1, 1000).render(
        std_tqdm._get_empty_task(total=2300)))

# Generated at 2022-06-22 13:29:47.636090
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    progress = Progress()
    progress.total = 100
    progress.completed = 5

    fraction_column = FractionColumn(unit_scale=True)
    fraction_column.render(progress)



# Generated at 2022-06-22 13:29:50.861498
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    import rich
    task = rich.progress.Task(None, 0, 1)
    FractionColumn().render(task) == "0.0/1.0 "

# Generated at 2022-06-22 13:30:01.921912
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    test_tqdm = tqdm_rich()
    test_tqdm.reset(total=100)
    assert test_tqdm.total == 100

# Generated at 2022-06-22 13:30:04.021245
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(total=10) as t:
        t.clear()
        pass

# Generated at 2022-06-22 13:30:10.807308
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    x = tqdm_rich(total=2, unit='B', unit_scale=True, desc='Testing tqdm_rich.display()...')
    alpha = [0, '', '', '']
    beta = [1, 'Testing tqdm_rich.display()...', 0, 3]
    x.display(alpha)
    assert x._prog.format_task(x._task_id) == beta
    x.display(beta)
    assert x._prog.format_task(x._task_id) == beta
    x.close()

# Generated at 2022-06-22 13:30:19.592579
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from tempfile import mktemp
    tqdm_args = dict(total=10, desc='testing', unit='b', unit_scale=True, unit_divisor=1024)
    with tqdm_rich(**tqdm_args) as t:
        # Initialize
        for i in range(10):
            t.update()
        t.reset(20)
        for i in range(10, 20):
            t.update()
        t.reset(20)
        for i in range(0, 10):
            t.update()
        t.close()
        # Reset total of t
        t.reset(10)
        t.n = 10

# Generated at 2022-06-22 13:30:27.539854
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    from sys import version_info
    from time import sleep
    from re import findall
    from .utils import _term_move_up as up

    if version_info[0] >= 3:
        from io import StringIO
    else:
        from StringIO import StringIO

    with StringIO() as our_file:
        with tqdm(total=100, file=our_file, desc='foo', leave=True) as t:
            for i in _range(10):
                t.clear()
                t.write("\r{0}".format(i))
                sleep(0.05)

        assert findall(up(our_file), our_file.getvalue()) == ['\x1b[A']*10

# Generated at 2022-06-22 13:30:39.250727
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rc = RateColumn(unit='B', unit_scale=True, unit_divisor=1024)
    assert rc.render(None) == Text("? B/s", style="progress.data.speed")
    rc = RateColumn(unit='B', unit_scale=True, unit_divisor=1000)
    assert rc.render(None) == Text("? B/s", style="progress.data.speed")
    rc = RateColumn(unit='B', unit_scale=True, unit_divisor=512)
    assert rc.render(None) == Text("? B/s", style="progress.data.speed")
    rc = RateColumn(unit='B', unit_scale=True, unit_divisor=1)
    assert rc.render(None) == Text("? B/s", style="progress.data.speed")

# Generated at 2022-06-22 13:30:48.713968
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = tqdm_rich(total=100, desc='', ncols=0, mininterval=0,
        disable=False, bar_format='{desc} [{bar}]', leave=True,
        miniters=1, smoothing=0.3, dynamic_ncols=False, unit='iB',
        unit_scale=False, unit_divisor=1000, unit_pos=None)
    task.speed = None
    RateColumn = RateColumn(unit_scale=False, unit_divisor=1000)
    assert RateColumn.render(task) == Text('? iB/s', style='progress.data.speed')
    task.speed = 100
    assert RateColumn.render(task) == Text('100.0 iB/s', style='progress.data.speed')
    RateColumn.unit

# Generated at 2022-06-22 13:30:59.982968
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    """Test method render of class RateColumn with different unit scales."""
    # Pick
    unit, suffix = filesize.pick_unit_and_suffix(
        100,
        ["", "K", "M", "G", "T", "P", "E", "Z", "Y"],
        1000,
    )
    assert unit == 1
    assert suffix == ""
    unit, suffix = filesize.pick_unit_and_suffix(
        1000,
        ["", "K", "M", "G", "T", "P", "E", "Z", "Y"],
        1000,
    )
    assert unit == 1
    assert suffix == "K"

# Generated at 2022-06-22 13:31:09.475352
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
  from decimal import Decimal
  t = tqdm_rich(total=10, smoothing=1.0)
  for i in range(5):
      t.update()  # old n = 5 + 1 smoothing
  t.reset(total=1)  # new n = 1
  assert t.last_print_n == Decimal('0')
  t.reset()  # new n = 0
  assert t.last_print_n == Decimal('0')
  for i in range(10):
    t.update()
  assert t.last_print_n == t.n
  t.close()

# Generated at 2022-06-22 13:31:21.341969
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from tqdm._tqdm import _range
    from tqdm.auto import trange
    # _range is a test for tqdm method reset compatibility
    for _t in trange(_range(3), **dict(desc='t1')):
        for _ in trange(_range(3), **dict(desc='t2')):
            for _ in trange(_range(3), **dict(desc='t3')):
                for _ in trange(_range(3), **dict(desc='t4')):
                    pass
    with trange(10) as t:
        for i in t:
            if i > 5:
                t.reset(5)
                t.set_description('RESET!')
            assert t.n <= 5

# Generated at 2022-06-22 13:31:38.978358
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    progress = tqdm_rich(total=1)
    progress.__enter__()
    progress.display()

# Generated at 2022-06-22 13:31:48.636085
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    rate_column = RateColumn(unit="B", unit_scale=True, unit_divisor=1024)
    task = MockTask()
    result_no_speed = Text("? B/s", style="progress.data.speed")
    assert result_no_speed == rate_column.render(task)
    task.speed = 1024
    result_with_speed = Text("1.00 B/s", style="progress.data.speed")
    assert result_with_speed == rate_column.render(task)
    rate_column.unit_divisor = 1000
    result_with_speed_unit_divisor_changed = Text("1.23 kB/s",
                                                  style="progress.data.speed")
    assert result_with_speed_unit_divisor_changed == rate_column.render(task)

# Generated at 2022-06-22 13:31:56.266339
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    """Unit test for method display of class tqdm_rich"""
    from .tests import pretest_posttest  # noqa: F401
    from os import getpid

    with tqdm_rich(total=5, desc=str(getpid()), leave=True,
                   bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}",
                   ) as pbar:
        for _ in pbar:
            pbar.display()

# Generated at 2022-06-22 13:32:01.983722
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich import print
    from tqdm.auto import tqdm
    from tqdm.rich import trange

    for _ in trange(10):
        for i in tqdm([1, 2, 3, 4]):
            print(i)


if __name__ == "__main__":  # pragma: no cover
    test_tqdm_rich_display()

# Generated at 2022-06-22 13:32:04.840595
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    if 100 < RateColumn(1000).render(ProgressColumn()):
        print("RateColumn is a child of ProgressColumn")

# Generated at 2022-06-22 13:32:07.143142
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    with tqdm_rich(total=1) as pbar:
        pbar.clear()
        pbar.update()
        pbar.close()

# Generated at 2022-06-22 13:32:19.751485
# Unit test for method clear of class tqdm_rich
def test_tqdm_rich_clear():
    # test clear function
    with tqdm_rich(total=0) as pbar:
        assert pbar.n == 0
        assert pbar.leave is False
        assert pbar.desc is None
        assert pbar.total == 0
        assert pbar.n is pbar.pos
        pbar.update(10)
        pbar.clear(total=1)  # this causes an AttributeError
    with tqdm_rich(total=1, leave=True) as pbar:
        assert pbar.n == 0
        assert pbar.leave is True
        assert pbar.desc is None
        assert pbar.total == 1
        assert pbar.n is pbar.pos
        pbar.update(10)
        pbar.clear(total=1)  # this causes an AttributeError

# Generated at 2022-06-22 13:32:21.721607
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    orig_total = 100
    reset_total = 500
    test_tqdm = tqdm(total=orig_total)
 

# Generated at 2022-06-22 13:32:33.598900
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    ratecolumn = RateColumn()
    assert ratecolumn.render(10) == Text('10.00 /s', style='progress.data.speed')
    ratecolumn_unit_M = RateColumn(unit="M", unit_scale=True, unit_divisor=1000)
    assert ratecolumn_unit_M.render(10000) == Text('10.00 M/s', style='progress.data.speed')
    ratecolumn_unit = RateColumn(unit="", unit_scale=True, unit_divisor=1000)
    assert ratecolumn_unit.render(10000) == Text('10.00 /s', style='progress.data.speed')
    ratecolumn_unit_K = RateColumn(unit="K", unit_scale=True, unit_divisor=1000)

# Generated at 2022-06-22 13:32:44.249809
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Unit test for method reset of class tqdm_rich"""
    import sys
    import time

    # For test with Python 2
    if sys.version_info[0] < 3:
        xrange = _range

    # Test reset with default value
    reset_timer = tqdm_rich(total=15)
    for _ in xrange(15):
        time.sleep(0.1)
        reset_timer.update()
    reset_timer.reset()
    for _ in xrange(15):
        time.sleep(0.1)
        reset_timer.update()

    # Test reset with value different from default
    reset_timer = tqdm_rich(total=15)
    for _ in xrange(15):
        time.sleep(0.1)
        reset_timer.update()
    reset_timer

# Generated at 2022-06-22 13:33:21.088444
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # When speed is None
    task = tqdm.tqdm(total=5, unit='B', unit_scale=False, unit_divisor=1000)
    task.update(5)
    task.close()
    task.speed = None
    assert (FractionColumn().render(task).text == '5.0/5.0 B') and \
    (RateColumn('B', unit_scale=False, unit_divisor=1000) \
    .render(task).text == '? B/s') and \
    (RateColumn('B', unit_scale=False, unit_divisor=1000) \
    .render(task).style == 'progress.data.speed')

    # When speed is an integer and unit_scale = False
    task.speed = 1024

# Generated at 2022-06-22 13:33:33.656567
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    a = RateColumn()
    assert a.render(0) == "? /s"
    assert a.render(1) == "1 /s"
    assert a.render(1000) == "1,000 /s"
    assert a.render(1000000) == "1,000,000 /s"
    assert a.render(1000000000) == "1,000,000,000 /s"
    assert a.render(1000000000000) == "1,000,000,000,000 /s"
    assert a.render(1000000000000000) == "1,000,000,000,000,000 /s"
    assert a.render(1000000000000000000) == "1,000,000,000,000,000,000 /s"

    b = RateColumn(unit="b")

# Generated at 2022-06-22 13:33:43.155896
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # Percentage sign rendering
    task = Progress.Task(12, 1234, 0.1234)
    unit_divisor = 1000
    unit_scale = True
    unit = "B"
    suffix = "K"
    speed = 123
    rate_column = RateColumn(unit, unit_scale, unit_divisor)
    rate_column.render(task)
    # test the render method
    rendered_text = rate_column.render(task)
    assert rendered_text.text == f"{speed/unit_divisor:,.0f} {suffix}{unit}/s"
    return True

# Generated at 2022-06-22 13:33:46.446315
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    total = 10
    t = tqdm_rich(total)
    assert t._prog.total == 10
    t.reset(total=6)
    assert t._prog.total == 6

# Generated at 2022-06-22 13:33:53.300580
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    def call_reset(reset_arg):
        with tqdm_rich(total=10, miniters=1, mininterval=0) as t:
            assert t._prog.total == 10
            t.reset(reset_arg)
            assert t._prog.total == reset_arg

    for reset_arg in [0, None, 1, 10]:
        yield call_reset, reset_arg

# Generated at 2022-06-22 13:33:56.341038
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from rich import print
    with tqdm_rich(total=5) as t:
        for i in range(5):
            print("test")
            t.update()
            t.display()

# Generated at 2022-06-22 13:34:03.837266
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    class tqdm_rich_mock(tqdm_rich):
        def display(self, *args, **kwargs):
            return super(tqdm_rich_mock, self).display(*args, **kwargs)
    mock = tqdm_rich_mock(disable=True)
    mock.n = 2
    mock.total = None
    mock.desc = "mock_desc"
    mock.disable = False
    mock.display()

    mock = tqdm_rich_mock()
    mock.n = 2
    mock.total = None
    mock.desc = "mock_desc"
    mock.disable = False
    mock.display()

# Generated at 2022-06-22 13:34:11.341024
# Unit test for method render of class FractionColumn
def test_FractionColumn_render():
    """
    render should return Text with concatenate of
    completed, total and suffix.
    """
    fc = FractionColumn()
    # task is mocked
    class Task:
        completed = 0
        total = 0
    task = Task()
    assert type(fc.render(task)) == Text
    assert fc.render(task).text == "0.0/0.0"
    # length of text should 8
    assert len(fc.render(task).text) == 8



# Generated at 2022-06-22 13:34:17.376461
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from collections import namedtuple
    from time import sleep
    import types

    tqdm_rich.set_lock(types.SimpleNamespace(acquire=lambda: sleep(0.1), release=lambda: sleep(0.1)))
    t = tqdm_rich(range(10))
    t.n = 3
    t.desc = "Test Description"
    t.display(namedtuple('Foo', ['n', 'desc'])(t.n, t.desc))
    t.close()

# Generated at 2022-06-22 13:34:22.195124
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    task = tqdm_rich(range(1000))
    columns = (
        BarColumn(bar_width=None),
        RateColumn(unit_scale=True)
    )
    for i in range(1000):
        task.update(n=1)
        rate = ''
        for c in columns:
            rate += c.render(task)
        print(rate)


# Generated at 2022-06-22 13:35:22.295955
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    r = RateColumn()
    assert r.render(None) == Text("? /s", style="progress.data.speed")

    class Task:
        def __init__(self, speed):
            self.speed = speed

    assert RateColumn().render(Task(1)) == Text("1 /s", style="progress.data.speed")
    assert RateColumn().render(Task(1000)) == Text("1 K/s", style="progress.data.speed")
    assert RateColumn().render(Task(1000000)) == Text("1 M/s", style="progress.data.speed")

    assert RateColumn(unit_scale=False).render(Task(1)) == Text("1 /s", style="progress.data.speed")

# Generated at 2022-06-22 13:35:26.172113
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    for i in tqdm(range(10), desc='test tqdm_rich reset'):
        if i == 0:
            tqdm.reset(total=5)
        if i == 1:
            tqdm.reset()

# Generated at 2022-06-22 13:35:31.848671
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    # Initialize a fake task
    class Task:
        def __init__(self, speed):
            self.speed = speed
    task = Task(100000)
    # Create RateColumn object
    rate_column = RateColumn(unit="B", unit_scale=True)
    # Check that render function returns the expected output
    assert rate_column.render(task) == Text("100.0 KB/s", style="progress.data.speed")

# Generated at 2022-06-22 13:35:43.899067
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """Test tqdm reset method"""
    progress = tqdm_rich(total=100)
    progress.update(99)
    progress.reset(total=200)
    progress.update(200)


if __name__ == '__main__':
    from time import sleep as ts
    from tqdm.auto import tqdm as tqdm_auto

    def sleep(t=0.3):
        ts(t)

    # iterable-based
    with tqdm_rich(total=10, leave=True, desc="progress") as progress:
        for i in progress:
            sleep(0.1)

    # manual
    with tqdm_rich(total=10, leave=True, desc="progress") as progress:
        for i in range(10):
            progress.update()

# Generated at 2022-06-22 13:35:50.729712
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    try:
        from io import StringIO as _StringIO  # Python 2: noqa
    except ImportError:
        from io import StringIO              # Python 3: noqa
    with _StringIO() as s:
        with tqdm_rich(total=10, file=s, ascii=True) as t:
            assert t.n == 0
            t.update(2)
            assert t.n == 2
            t.display()
            t.update(4)
            assert t.n == 6
            t.display()
            t.update(1)
            assert t.n == 7
            t.display()
            t.destroy()



# Generated at 2022-06-22 13:35:55.287882
# Unit test for method render of class RateColumn
def test_RateColumn_render():
    assert RateColumn(unit_scale=True, unit_divisor=1024).render(
        tqdm_rich(total=1e9, unit="B")) == '[progress.data.speed]9.30 GiB/s'



# Generated at 2022-06-22 13:36:00.518038
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    """
    Unit test for method reset of class tqdm_rich.
    """
    kwargs = {'total': 10, 'unit': 'K', 'unit_scale': True, 'unit_divisor': 1024}
    progress_bar = tqdm_rich(**kwargs)
    assert progress_bar.format_dict == kwargs

# Generated at 2022-06-22 13:36:13.126005
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    from .std import tqdm as std_tqdm
    from .std import trange as std_trange
    from .std import TqdmDeprecationWarning
    std_tqdm(std_trange(5), disable=False, ascii=True).display()
    std_tqdm(std_trange(5), disable=False, ascii=True, mininterval=1).display()
    std_tqdm(std_trange(5), disable=True, ascii=True).display()
    std_tqdm(std_trange(5), disable=True).display()
    std_tqdm(std_trange(5), disable=False).display()
    std_tqdm(std_trange(5), disable=False, dynamic_ncols=True).display()


# Generated at 2022-06-22 13:36:19.211046
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():  # pragma: no cover
    """Unit test for tqdm_rich.reset()"""
    with tqdm(3, 6) as t:
        for i in t:
            pass
    assert t._prog.total == 3
    t.reset(6)
    assert t._prog.total == 6
    with tqdm(3, 6) as t:
        for i in t:
            if i > 2:
                t.reset(9)
            assert t._prog.total == 9

# Generated at 2022-06-22 13:36:23.735696
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    from io import StringIO
    from .std import tqdm
    with StringIO() as string_io:
        with tqdm(desc='test', file=string_io) as iterator:
            for _ in iterator:
                iterator.reset(total=10)
                break



# Generated at 2022-06-22 13:37:24.507994
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():  # pragma: no cover
    # Regression test for Issue #623
    pbar = tqdm_rich(total=1)
    pbar.display()
    pbar.close()



# Generated at 2022-06-22 13:37:28.521911
# Unit test for method display of class tqdm_rich
def test_tqdm_rich_display():
    with tqdm((1,2), desc="Testing", disable=False) as t:
        t.display()
        t.reset(total=3)
        t.display()
    assert t.disable is False

# Generated at 2022-06-22 13:37:35.441028
# Unit test for method reset of class tqdm_rich
def test_tqdm_rich_reset():
    import random

    total = random.randint(1, 10000)
    with tqdm(total=total) as t:
        assert t.total == total

        for _ in t:
            pass

        t.reset()
        assert t.total == total

        t.reset(total)
        assert t.total == total

        new_total = total + random.randint(1, 100000)
        t.reset(total=new_total)
        assert t.total == new_total