

# Generated at 2022-06-13 18:27:49.579842
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('timer1', 1)
    t.add('timer1', 2)
    t.add('timer1', 3)
    t.add('timer1', 4)
    t.add('timer1', 5)
    assert t.min('timer1') == 1
    assert t.min('timer2') == 0


# Generated at 2022-06-13 18:27:53.835944
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('test', 2)
    t.add('test', 1)
    t.add('test', 3)
    min = t.min('test')
    assert min == 1, min



# Generated at 2022-06-13 18:28:03.319931
# Unit test for method median of class Timers
def test_Timers_median():
    t1 = Timers()
    t1.add("t1", 1)
    t1.add("t1", 2)
    t1.add("t1", 3)
    assert t1.median("t1") == 2.0

    t2 = Timers()
    t2.add("t2", 1)
    t2.add("t2", 2)
    t2.add("t2", 3)
    t2.add("t2", 4)
    assert t2.median("t2") == 2.5


# Generated at 2022-06-13 18:28:06.888806
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add('a',3)
    t.add('a',1)
    t.add('a',4)
    assert(t.max('a')==4)


# Generated at 2022-06-13 18:28:13.442739
# Unit test for method median of class Timers
def test_Timers_median():
    """Test function for unit-test"""
    timers = Timers()
    timers.add("timer1", 1)
    timers.add("timer1", 2)
    timers.add("timer1", 3)
    timers.add("timer2", 3)
    timers.add("timer2", 3)
    # test median values for all timers
    assert timers.median("timer1") == 2
    assert timers.median("timer2") == 3


# Generated at 2022-06-13 18:28:17.267891
# Unit test for method max of class Timers
def test_Timers_max():
    """Check if the correct value is returned"""
    timers = Timers()
    timers.add('Test', 12)
    assert timers.max('Test') == 12


# Generated at 2022-06-13 18:28:24.916688
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of Timers."""
    # Create a Timers object
    timers = Timers()
    # Add a timing named 'foo', with one element
    timers.add('foo', 5)
    # Check that its median is correct
    assert timers.median('foo') == 5
    # Add a timing named 'foo', with two elements
    timers.add('foo', 1)
    # Check that its median is correct
    assert timers.median('foo') == 3

# Generated at 2022-06-13 18:28:30.606566
# Unit test for method median of class Timers
def test_Timers_median():
    # Define input
    Timers = Timers()
    Timers.add("call", 0.2)
    Timers.add("call", 0.2)
    Timers.add("call", 0.2)
    Timers.add("call", 0.4)
    Timers.add("call", 0.4)

    # Test if method returns expected value
    assert Timers.median("call") == 0.3


# Generated at 2022-06-13 18:28:35.080230
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("one", 6)
    t.add("two", 7)
    t.add("one", 5)
    t.add("two", 0)
    assert t.mean("one") == 5.5


# Generated at 2022-06-13 18:28:41.205495
# Unit test for method median of class Timers
def test_Timers_median():
    from random import randrange
    import numpy as np
    n = 10
    t = Timers()

    assert t.median("test_median") == 0.0, ("Median of non existent timer should be zero")
    for i in range(n):
        t.add("test_median", i)

    assert t.median("test_median") == np.median(list(range(n)))

# Generated at 2022-06-13 18:28:54.239715
# Unit test for method median of class Timers
def test_Timers_median():
    """
    It should return a median value

    This does not use pytest to avoid false-positives for `type` hints.
    """
    # Data for the test, the data of the median should be 9
    data = [2, 9, 4, 1, 5, 9, 10, 4, 5, 9, 9, 4, 5, 9, 4, 5, 5, 9, 1, 3]

    # Create a timers instance and add data to a timer called 'test'
    timers = Timers()
    for value in data:
        timers.add('test', value)

    # Check that mean(data) == timers.median('test')
    assert statistics.median(data) == timers.median('test')

# Generated at 2022-06-13 18:29:03.737710
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    from ..version import __version__
    from datetime import datetime

    print(f"Test method max of class Timers, version {__version__}")
    print(f"Python {sys.version}\n")
    print(f"{datetime.now().isoformat()}")
    print(f"{__file__}")
    print(f"{sys.platform} {sys.version}")
    print()

    # Test empty
    print("Test empty...")
    timer = Timers()
    print(timer)
    try:
        timer.max("a")
        assert False
    except KeyError:
        pass

    # Test single value
    print("Test single value...")
    timer = Timers()
    timer.add("a", 1.0)

# Generated at 2022-06-13 18:29:15.515747
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()
    timers.add("query", 10)
    timers.add("query", 20)
    assert timers.median("query") == 15
    timers.add("query", 40)
    assert timers.median("query") == 20
    timers.add("query", 60)
    assert timers.median("query") == 30
    timers.add("query", 80)
    assert timers.median("query") == 40
    timers.add("query", 100)
    assert timers.median("query") == 50
    timers.add("query", 120)
    assert timers.median("query") == 60
    timers.add("query", 140)
    assert timers.median("query") == 70


# Generated at 2022-06-13 18:29:18.503965
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers({"a": 5.0, "b": 10.0})
    assert t.mean("a") == 5.0
    assert t.mean("b") == 10.0

# Generated at 2022-06-13 18:29:20.577648
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("Test", 1234)
    assert timers.max("Test") == 1234

# Generated at 2022-06-13 18:29:25.095723
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test mean"""
    timer = Timers()
    timer.add('loop', 0)
    assert timer.mean('loop') == 0
    timer.add('loop', 10)
    assert timer.mean('loop') == 5
    timer.add('loop', 20)
    assert timer.mean('loop') == 10


# Generated at 2022-06-13 18:29:37.938176
# Unit test for method mean of class Timers
def test_Timers_mean():
    # Define object with two timers, each with 5 values
    my_timers = Timers(
        {'timer1': 50, 'timer2': 75}
    )
    my_timers.add('timer1', 10)
    my_timers.add('timer1', 20)
    my_timers.add('timer1', 30)
    my_timers.add('timer1', 40)
    my_timers.add('timer1', 50)
    my_timers.add('timer2', 100)
    my_timers.add('timer2', 200)
    my_timers.add('timer2', 300)
    my_timers.add('timer2', 400)
    my_timers.add('timer2', 500)
    # Test method mean for timer1
    assert my_timers.mean

# Generated at 2022-06-13 18:29:44.506655
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('test', float('nan'))
    assert math.isnan(timers.min('test'))
    timers.add('test', float('nan'))
    assert math.isnan(timers.min('test'))
    timers.add('test', 0)
    assert timers.min('test') == 0
    timers.add('test', 1)
    assert timers.min('test') == 0
    timers.add('test', -1)
    assert timers.min('test') == -1


# Generated at 2022-06-13 18:29:48.564053
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('t1', 10_000)
    timers.add('t1', 20_000)
    assert timers.max('t1') == 20_000


# Generated at 2022-06-13 18:29:56.812026
# Unit test for method min of class Timers
def test_Timers_min():
    import random
    import time
    timers1 = Timers()
    timers2 = Timers()
    x = random.random()
    y = random.random()
    z = random.random()
    timers1.add('timer', x)
    timers2.add('timer', y)
    timers1.add('timer', z)
    t1 = timers1.min('timer')
    t2 = min(x,y,z)
    assert (t1 == t2)

# Generated at 2022-06-13 18:30:06.706648
# Unit test for method max of class Timers
def test_Timers_max():
    """This method checks if Timers.max() is working properly"""
    timers = Timers()
    timers.add("a", 1)
    timers.add("a", 2)
    timers.add("a", 3)
    timers.add("b", 1)
    timers.add("b", 2)
    timers.add("b", 3)
    timers.add("b", 4)
    assert timers.max("a") == 3
    assert timers.max("b") == 4


# Generated at 2022-06-13 18:30:17.820977
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    assert isinstance(timers, Timers)
    timers.add("t", 100)
    assert timers.max(name="t") == 100
    timers.add("t", 30)
    assert timers.max(name="t") == 100
    timers.add("t", 130)
    assert timers.max(name="t") == 130
    timers.add("t", 120)
    assert timers.max(name="t") == 130
    timers.add("t", 80)
    assert timers.max(name="t") == 130
    timers.add("t", 5.4)
    assert timers.max(name="t") == 130
    timers.add("t", 4.2)
    assert timers.max(name="t") == 130
    timers

# Generated at 2022-06-13 18:30:21.663534
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the mean method of class Timers"""
    timers = Timers()
    timers.add("time", 1.0)
    timers.add("time", 2.0)
    assert timers.mean("time") == 1.5
    timers._timings.clear()
    timers._timings["time"] = []
    assert timers.mean("time") == 0

# Generated at 2022-06-13 18:30:29.901557
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("test1", 2.2)
    timers.add("test1", 4.4)
    timers.add("test1", 1.9)
    assert timers.max("test1") == 4.4
    assert timers.min("test1") == 1.9
    assert timers.total("test1") == 8.5
    assert timers.mean("test1") == 2.833333
    assert timers.median("test1") == 2.2
    assert timers.stdev("test1") == 1



# Generated at 2022-06-13 18:30:36.562732
# Unit test for method median of class Timers
def test_Timers_median():
    """Test if the median of the Timers class calculates correctly"""
    test_timers = Timers()
    test_timers.add('test_name', 1)
    test_timers.add('test_name', 2)
    test_timers.add('test_name', 3)
    assert test_timers.median('test_name') == 2

# Generated at 2022-06-13 18:30:40.790777
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("test", 1)
    assert timers.max("test") == 1
    timers.add("test", 2)
    assert timers.max("test") == 2
    assert timers.max("test2") == 0
    timers.add("test2", 3)
    assert timers.max("test2") == 3


# Generated at 2022-06-13 18:30:48.015001
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    data = {
        'update_timer': 0.7362499237060547,
        'create_map_timer': 0.4637500047683716,
        'create_objects_timer': 0.686874988079071,
        'build_object_grid_timer': 0.11249999701976776
    }
    for name, value in data.items():
        timers.add(name, value)
    assert timers.min('update_timer') == 0.7362499237060547
    assert timers.min('create_map_timer') == 0.4637500047683716
    assert timers.min('create_objects_timer') == 0.686874988079071
    assert timers.min('build_object_grid_timer') == 0.11249999701

# Generated at 2022-06-13 18:30:54.154987
# Unit test for method median of class Timers
def test_Timers_median():
  """Test for the Timers class"""
  times = Timers()
  times.add("test1", 1.2)
  times.add("test1", 2.1)
  times.add("test1", 3.2)
  assert times.median("test1") == 2.1
  

# Generated at 2022-06-13 18:30:58.337261
# Unit test for method mean of class Timers
def test_Timers_mean():
    A = Timers()
    A.add('A', 3)
    A.add('A', 5)
    A.add('A', 6)
    assert A.mean('A') == 4.666666666666667
    assert A.count('A') == 3
    print('Timers.mean() ok')


# Generated at 2022-06-13 18:31:01.800205
# Unit test for method min of class Timers
def test_Timers_min():
    """Test min method of class Timers"""
    timings = Timers()
    timings.add('foo', 1)
    timings.add('foo', 2)
    assert timings.min('foo') == 1


# Generated at 2022-06-13 18:31:07.329248
# Unit test for method mean of class Timers
def test_Timers_mean():
    timer = Timers()
    timer.add("test", 1)
    assert timer.mean("test") == 1
    timer.add("test", 2)
    assert timer.mean("test") == 1.5
    return
test_Timers_mean()

# Generated at 2022-06-13 18:31:09.146419
# Unit test for method max of class Timers
def test_Timers_max():
    x = Timers()
    x.add('c',2)
    assert x.max('c') == 2


# Generated at 2022-06-13 18:31:11.873690
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    assert timers.max('timing') == 0
    timers.add('timing', 1)
    assert timers.max('timing') == 1
    timers.add('timing', 2)
    assert timers.max('timing') == 2


# Generated at 2022-06-13 18:31:17.027487
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit tests for the method min of Timers"""
    timers = Timers()
    timers.add("a", 1)
    timers.add("a", 2)
    timers.add("b", 1)
    assert timers.min("a") == 1
    assert timers.min("b") == 1
    assert timers["a"] == 3
    assert timers["b"] == 1


# Generated at 2022-06-13 18:31:25.922027
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min"""
    from unittest import TestCase
    from unittest.mock import Mock

    method = Timers.min
    method_name = method.__name__
    target = "pylarization.timers.Timers.min"
    args = tuple()
    kwargs = {"name": "test"}
    test_case = TestCase()

    class TimersMock(Mock):
        """Mock Timers class"""
        apply = method
    mock_self = TimersMock()
    mock_self._timings = collections.defaultdict(list, {"test": [1, 5, 3]})
    expected = 1

    actual = method(mock_self, *args, **kwargs)
    test_case.assertEqual(expected, actual)

# Generated at 2022-06-13 18:31:33.097215
# Unit test for method mean of class Timers
def test_Timers_mean():
    """The mean of a list of numbers is the sum of the numbers divided by the count of numbers."""
    values = [1, 2, 3, 4, 5]
    timings = Timers()
    for i in values:
        timings.add('timers', i)
    assert timings.mean('timers') == statistics.mean(values)

# Generated at 2022-06-13 18:31:37.123840
# Unit test for method min of class Timers
def test_Timers_min():
    """Test Timers.min"""
    timers = Timers()
    timers.add('a', 1)
    timers.add('a', 2)
    timers.add('b', 3)
    assert timers.min('a') == 1
    assert timers.min('b') == 3


# Generated at 2022-06-13 18:31:39.877883
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("test", 5)
    assert t.mean("test") == 5
    assert t.mean("nothing") == 0

# Generated at 2022-06-13 18:31:45.721351
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('timer1', 1)
    timers.add('timer2', 2)
    timers.add('timer2', 3)
    assert timers.max('timer1') == 1
    assert timers.max('timer2') == 3


# Generated at 2022-06-13 18:31:51.747901
# Unit test for method max of class Timers
def test_Timers_max():
    import numpy as np
    timers = Timers()
    timers.add("first_timer",1)
    timers.add("first_timer",2)
    assert timers.max("first_timer") == 2
    timers.add("second_timer",np.nan)
    assert np.isnan(timers.max("second_timer"))

# Generated at 2022-06-13 18:32:05.877805
# Unit test for method median of class Timers
def test_Timers_median():
    """Check that the median method works correctly"""
    t = Timers()
    t.add("a", 1)
    assert t.median("a") == 1
    t.add("a", 2)
    assert t.median("a") == 1.5
    t.add("a", 3)
    assert t.median("a") == 2
    t.add("a", 4)
    assert t.median("a") == 2.5
    t.add("a", 4)
    assert t.median("a") == 3
    t = Timers()
    t.add("a", 1)
    assert t.median("a") == 1
    t.add("a", 2)
    assert t.median("a") == 1.5
    t.add("a", 3)

# Generated at 2022-06-13 18:32:11.281405
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add('a', 1)
    t.add('a', 2)
    t.add('a', 3)
    t.add('a', 4)
    t.add('a', 5)
    t.add('a', 6)
    assert t.mean('a') == 3.5
    assert t.mean('b') !=  3.5

# Generated at 2022-06-13 18:32:16.246518
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add("test", 2)
    t.add("test", 8)
    t.add("test", 3)
    t.add("test", 7)
    assert t.median("test") == 5
    t.clear()
    t.add("test", 1)
    assert t.median("test") == 1

# Generated at 2022-06-13 18:32:21.331066
# Unit test for method max of class Timers
def test_Timers_max():
    """Test for method max of class Timers"""
    from time import sleep
    timers = Timers()
    timers.add('no_sleep', 0.9)
    sleep(1)
    timers.add('sleep', 0.8)
    assert timers.max('no_sleep') == 0.9
    assert timers.max('sleep') == 1.8


# Generated at 2022-06-13 18:32:26.030275
# Unit test for method max of class Timers
def test_Timers_max():
    """Test Timers_max"""
    timers = Timers()
    timers.add("wait", 0.5)
    timers.add("wait", 1.5)
    assert timers.max("wait") == 1.5
    timers = Timers()
    assert timers.max("wait") == 0
    timers = Timers()
    timers.add("wait", 0.5)
    timers.add("wait", -1.5)
    assert timers.max("wait") == 0.5


# Generated at 2022-06-13 18:32:28.218906
# Unit test for method max of class Timers
def test_Timers_max():
    """
    Test Timers.max
    """
    t = Timers()
    t.add("a", 1)
    t.add("a", 2)
    assert t.max("a") == 2


# Generated at 2022-06-13 18:32:29.544549
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('time 1', 1)
    assert(timers.mean('time 1') == 1)

# Generated at 2022-06-13 18:32:34.420004
# Unit test for method median of class Timers
def test_Timers_median():
    """Test for Timers.median"""
    timers = Timers()
    assert not timers
    timers.add('a', 1)
    assert timers['a'] == 1
    assert timers.median('a') == 1
    timers.add('a', 2)
    assert timers['a'] == 3
    assert timers.median('a') == 1.5
    timers.add('b', 1)
    assert timers['b'] == 1
    assert timers.median('b') == 1
    timers.add('b', 100)
    assert timers['b'] == 101
    assert timers.median('b') == 50.5
    timers.add('b', math.inf)
    assert timers['b'] == math.inf
    assert timers.median('b') == 100
    timers.add('b', math.inf)
   

# Generated at 2022-06-13 18:32:42.992736
# Unit test for method max of class Timers
def test_Timers_max():
    # x=x+1
    x = Timers()
    x.add('a', 1)
    assert x.max('a') == 1
    x.add('a', 10)
    assert x.max('a') == 10
    x.add('a', 2)
    x.add('a', 3)
    assert x.max('a') == 10
    # x={}
    x = Timers()
    x.add('a', 1)
    x.add('a', 2)
    assert x.max('a') == 2
    # x=x
    x = Timers()
    x.add('a', 1)
    x.add('a', 2)
    x.add('a', 3)
    x.add('a', 4)
    assert x.max('a') == 4
    # x

# Generated at 2022-06-13 18:32:50.173451
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timers = Timers()
    assert timers.min("new timer") == 0  # New timer has a zero value

    timers.add("new timer", value=1)
    assert timers.min("new timer") == 1

    timers.add("new timer", value=2)
    assert timers.min("new timer") == 1


# Generated at 2022-06-13 18:32:57.811406
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("timer 1", 1)
    timers.add("timer 1", 2)
    timers.add("timer 1", 3)
    assert timers.median("timer 1") == 2

# Generated at 2022-06-13 18:33:05.560759
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    import pytest
    timers = Timers({'timer1': 1, 'timer2': 2, 'timer3': 3, 'timer4': 4})

    assert timers.min('timer1') == 1
    assert timers.min('timer2') == 2
    assert timers.min('timer3') == 3
    assert timers.min('timer4') == 4

    with pytest.raises(KeyError) as excinfo:
        timers.min('timer5')
    

# Generated at 2022-06-13 18:33:08.023771
# Unit test for method median of class Timers
def test_Timers_median():
    timer = Timers()
    timer.add("z", 3)
    timer.add("a", 4)
    timer.add("m", 2)
    timer.add("d", 1)
    assert timer.median("z") == 3
    assert timer.median("a") == 4
    assert timer.median("m") == 2
    assert timer.median("d") == 1



# Generated at 2022-06-13 18:33:09.928859
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('Example', 5)
    assert timers.mean('Example') == 5

# Generated at 2022-06-13 18:33:10.941168
# Unit test for method median of class Timers
def test_Timers_median():
    assert Timers().median("dummy") == 0

# Generated at 2022-06-13 18:33:16.396403
# Unit test for method median of class Timers
def test_Timers_median():
    """Test class Timers method median"""
    timers = Timers()
    timers.add('foo', 1)
    timers.add('foo', 2)
    timers.add('foo', 2)
    timers.add('foo', 3)
    timers.add('foo', 3)
    timers.add('foo', 4)
    assert timers.median('foo') == 2.5
    assert timers.median('bar') == 0


# Generated at 2022-06-13 18:33:18.982520
# Unit test for method max of class Timers
def test_Timers_max():
    """
    Test the method max of class Timers
    """
    timers = Timers()

    timers.add("key", 1)
    assert timers.max("key") == 1

    timers.add("key", 4)
    assert timers.max("key") == 4


# Generated at 2022-06-13 18:33:21.894162
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("t1", 2.)
    timers.add("t1", 1.)
    assert timers.min("t1") == 1.


# Generated at 2022-06-13 18:33:25.812684
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()

    timers.add("timer1", 1)
    timers.add("timer1", 2)

    timers.add("timer2", 5)
    timers.add("timer2", 7)

    assert round(timers.mean("timer1"), 2) == 1.5
    assert round(timers.mean("timer2"), 2) == 6

# Generated at 2022-06-13 18:33:27.224377
# Unit test for method max of class Timers
def test_Timers_max():

    timers = Timers()
    timers.add('foo', 1)
    timers.add('foo', 2)
    timers.add('foo', 3)

    assert timers.max('foo') == 3

# Generated at 2022-06-13 18:33:33.378638
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    timers.add('Max Timer', 1)
    assert timers.max('Max Timer') == 1



# Generated at 2022-06-13 18:33:36.962529
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('test', 10)
    assert timers.max('test') == 10
    timers.add('test', 20)
    assert timers.max('test') == 20
    assert timers.max('test2') == 0


# Generated at 2022-06-13 18:33:47.212831
# Unit test for method min of class Timers
def test_Timers_min():
    """Test that Timers.min returns the minimum value of the timing list.
    
    If the list is empty or all values are None, return 0.
    """
    # Test for returning 0 for all lists that are empty or only contain None
    for i in range(100):
        value = [None for i in range(i)]
        min = Timers().apply(lambda values: min(values or [0]), value)
        assert min == 0

    # Test for returning the minimum value of non-empty lists
    list1 = [1, 2, 3]
    list2 = [10, 20, 30, 40]
    list3 = [0.1, 0.01, 0.001]
    list4 = [-1, -2, -3]
    list5 = [1, 2, 2, 3]

# Generated at 2022-06-13 18:33:56.824493
# Unit test for method median of class Timers
def test_Timers_median():
    """Test medain of values"""
    # Default behavior
    assert Timers({'a': 1}).median('a') == 1, "Should return the value"
    # Empty list
    assert Timers({'a': 0}).median('a') == 0, "Should return 0"
    # With values
    assert Timers().add('a', 1)
    assert Timers().add('a', 2)
    assert Timers().median('a') == 1.5, "Should return the median"

# Generated at 2022-06-13 18:33:59.734353
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("test", 2)
    timers.add("test", 1)
    timers.add("test", 4)
    assert timers.max("test") == 4

# Generated at 2022-06-13 18:34:04.097369
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    timers.add("test", 1)
    assert timers.mean("test") == 1.0


# Generated at 2022-06-13 18:34:13.164658
# Unit test for method max of class Timers
def test_Timers_max():
    import random
    import string
    import unittest
    class TestCase(unittest.TestCase):
        def test_max(self):
            timings = Timers()
            names = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(10)]
            words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(10)]
            for name in names:
                values = [random.random() for _ in range(10)]
                for value in values:
                    timings.add(name, value)

# Generated at 2022-06-13 18:34:18.114829
# Unit test for method min of class Timers
def test_Timers_min():
    """Test min() method of class Timers."""
    timers = Timers()
    for i in range(10):
        timers.add("test", i)
    assert timers.min("test")  == 0


# Generated at 2022-06-13 18:34:24.518342
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method Timers.min()"""
    timers = Timers()
    timers.add('test', 0.1)
    timers.add('test', 0.3)
    timers.add('test', 0.2)
    assert timers.min('test') == 0.1
    assert timers['test'] == 0.6


# Generated at 2022-06-13 18:34:29.679776
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("time1", 0.5)
    timers.add("time1", 0.2)
    timers.add("time1", 0.3)
    timers.add("time2", 0.3)
    timers.add("time2", 0.5)
    timers.add("time2", 0.7)
    assert timers.mean("time1") == 0.3
    assert timers.mean("time2") == 0.5

test_Timers_mean()


# Generated at 2022-06-13 18:34:41.920290
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min("test") == 0

    timers = Timers()
    timers["test"] = 1
    assert timers.min("test") == 1

    timers = Timers()
    timers.add("test", 1)
    assert timers.min("test") == 1

    timers = Timers()
    timers.add("test", 1)
    timers.add("test", 2)
    assert timers.min("test") == 1

# Generated at 2022-06-13 18:34:48.004663
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers. Sets a timer, and then gets
    the value of the timer. Tests that when the timer value is None, it
    returns correctly."""
    timers = Timers()
    timers.add("test_timer", 0)
    assert(timers.min("test_timer") == 0)


# Generated at 2022-06-13 18:34:51.514300
# Unit test for method min of class Timers
def test_Timers_min():
    """Check the output of Timers().min"""
    data = [3.5, 2.5, 2.5]
    timers = Timers()
    timers._timings["data"] = data
    assert timers.min("data") == 2.5

# Generated at 2022-06-13 18:34:52.940975
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Check if mean calculation of an empty collection returns 0"""
    result = Timers().mean("duration")
    assert result == 0

# Generated at 2022-06-13 18:34:56.274231
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timers = Timers()
    timers.add("a", 4)
    timers.add("a", 6)
    timers.add("a", 2)
    assert timers.min("a") == 2


# Generated at 2022-06-13 18:35:09.995831
# Unit test for method max of class Timers
def test_Timers_max():
    from pytest import approx
    from .test_helpers import CALLBACK_EXECUTION_TIMES
    timers = Timers()
    for k, v in CALLBACK_EXECUTION_TIMES.items():
        timers.add(k, v)
    assert timers.max("log") == approx(0.0014)
    assert timers.max("signals") == approx(0.0001)
    assert timers.max("build") == approx(0.0003)
    assert timers.max("build_indices") == approx(0.0001)
    assert timers.max("move") == approx(0.0001)
    assert timers.max("init_solution") == approx(0.0027)
    assert timers.max("callbacks") == approx(0.0001)

# Generated at 2022-06-13 18:35:14.354507
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Check that Timers.mean returns the mean value of the timings
    """
    timers = Timers()
    timers.add('time', 10.0)
    timers.add('time', 20.0)
    timers.add('time', 30.0)
    mean = timers.mean('time')
    assert mean == 20.0

# Generated at 2022-06-13 18:35:23.805084
# Unit test for method median of class Timers
def test_Timers_median():
    data = Timers()
    assert data.median('a') == 0
    data.add('a', 2)
    assert data.median('a') == 2
    data.add('a', 1)
    assert data.median('a') == 1.5
    data.add('a', 3)
    assert data.median('a') == 2
    data.add('a', 4)
    data.add('a', 5)
    assert data.median('a') == 3.5

# Generated at 2022-06-13 18:35:30.545306
# Unit test for method min of class Timers
def test_Timers_min():
    """Test .min() method of Timers"""
    timers = Timers()
    timers.add('timer1', 1)
    timers.add('timer1', 2)
    timers.add('timer2', 3)
    assert timers.min('timer1') == 1
    assert timers.min('timer2') == 3
    assert timers.min('timer3') == 0



# Generated at 2022-06-13 18:35:34.221402
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    # Test min
    timers = Timers()
    assert timers.min("test") == 0
    timers.add("test", 1)
    assert timers.min("test") == 1
    timers.add("test", 0.1)
    assert timers.min("test") == 0.1


# Generated at 2022-06-13 18:35:49.398620
# Unit test for method min of class Timers
def test_Timers_min():
    timer = Timers()
    for i in range(10):
        timer.add(i)
    assert timer.min() == 0


# Generated at 2022-06-13 18:35:58.184040
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()

    # Empty timers
    assert timers.max("empty") == 0

    # Timers with only one element:
    timers.add("one", 1)
    assert timers.max("one") == 1

    # Timers with only two elements:
    timers.add("two", 2)
    assert timers.max("two") == 2

    # Timers with only two equal elements:
    timers.clear()
    timers.add("two equal", 1)
    timers.add("two equal", 1)
    assert timers.max("two equal") == 1

    # Timers with several elements:
    timers.clear()
    timers.add("several", 1)
    timers.add("several", -1)
    assert timers.max("several") == 1


# Generated at 2022-06-13 18:36:01.038506
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('foo', 10)
    t.add('foo', 15)
    assert t.min('foo') == 10


# Generated at 2022-06-13 18:36:05.854027
# Unit test for method min of class Timers
def test_Timers_min():
    timer = Timers()
    timer.add("my_timer", 10)
    print(f"min = {timer.min('my_timer')}")
# This unit test returns:
# min = 10.0


# Generated at 2022-06-13 18:36:10.312281
# Unit test for method max of class Timers
def test_Timers_max():
	t = Timers()
	t.add("first", 50)
	t.add("second", 50)
	assert t.max("first") == 50.0
	assert t.max("second") == 50.0


# Generated at 2022-06-13 18:36:17.941952
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timers = Timers()
    timers.add("a", 3)
    timers.add("a", 0)
    timers.add("b", 1)
    timers.add("b", 2)
    assert timers.count("a") == 2
    assert timers.count("b") == 2
    assert timers.min("a") == 0
    assert timers.min("b") == 1
    assert timers.min("c") == 0


# Generated at 2022-06-13 18:36:25.622314
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers({})
    timers._timings['foo'] = [10, 15, 20, 25]
    timers.data['foo'] = 80
    assert timers.median(name='foo') == 17.5
    # inspect.getfullargspec(timers.median)
    # Out[47]: FullArgSpec(args=['self', 'name'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={'name': <class 'str'>, 'return': <class 'float'>})


# Generated at 2022-06-13 18:36:29.740937
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    # Create test data
    timers: Timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    # Test
    assert timers.mean('test') == 2.0


# Generated at 2022-06-13 18:36:38.321760
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('a', 50)
    assert timers.median('a') == 50
    assert timers.median('b') == 0
    timers.add('a', 100)
    assert timers.median('a') == 75
    timers.add('a', 75)
    assert timers.median('a') == 75
    timers.add('a', 100)
    assert timers.median('a') == 75
    timers.add('a', 100)
    assert timers.median('a') == 100
    timers.add('a', 50)
    assert timers.median('a') == 75
    assert timers.data['a'] == 475

# Generated at 2022-06-13 18:36:43.424850
# Unit test for method mean of class Timers
def test_Timers_mean():
    assert Timers().mean('name') == 0
    t = Timers()
    t.add('name', 1)
    assert t.mean('name') == 1
    t.add('name', 2)
    assert t.mean('name') == 1.5

# Generated at 2022-06-13 18:37:17.263752
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    assert timers.max("x") == 0
    timers.add("x", 1)
    assert timers.max("x") == 1
    timers.add("x", 2)
    assert timers.max("x") == 2
    timers.add("x", 1)
    assert timers.max("x") == 2
    timers.add("x", 2)
    assert timers.max("x") == 2
    timers.add("x", 1)
    assert timers.max("x") == 2
    timers.add("x", 3)
    assert timers.max("x") == 3
    assert timers.max("y") == 0
    timers.add("y", 2)
    assert timers.max("y") == 2
    timers.add("y", 1)
    assert timers.max("y") == 2

# Generated at 2022-06-13 18:37:23.309854
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    assert t.mean('no_data') == 0
    t.add('t1', 10)
    t.add('t1', 20)
    t.add('t1', 30)
    t.add('t1', 40)
    assert t.mean('t1') == 25
    assert t.mean('t2') == 0
    del t['t1']
    assert t.mean('t1') == 0

# Generated at 2022-06-13 18:37:30.549746
# Unit test for method median of class Timers
def test_Timers_median():
    from numpy import median

    timers = Timers()
    timers.add("test", 1)
    timers.add("test", 2)
    timers.add("test", 3)

    # Median computed in Python
    assert timers.median("test") == median([1, 2, 3])

    # Median computed in numpy
    assert median([1, 2, 3]) == median([1, 2, 3])

    # Median computed in Timers.median
    timers = Timers()
    timers.add("test", 1)
    timers.add("test", 2)
    timers.add("test", 3)
    assert median([1, 2, 3]) == timers.median("test")

    # Median of empty timer
    timers = Timers()
    assert math.isnan(timers.median("test"))

# Unit test

# Generated at 2022-06-13 18:37:39.387197
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    timers.add("i", 2)
    timers.add("i", 1)
    timers.add("i", 3)
    
    assert timers.max("i") == 3
    assert timers.max("j") == 0
    assert timers.min("i") == 1
    assert timers.min("j") == 0
    assert timers.mean("i") == 2.0
    assert timers.mean("j") == 0
    assert timers.median("i") == 2.0
    assert timers.median("j") == 0
    assert timers.total("i") == 6
    assert timers.total("j") == 0
    assert timers.count("i") == 3
    assert timers.count("j") == 0
    assert timers.stdev("i")