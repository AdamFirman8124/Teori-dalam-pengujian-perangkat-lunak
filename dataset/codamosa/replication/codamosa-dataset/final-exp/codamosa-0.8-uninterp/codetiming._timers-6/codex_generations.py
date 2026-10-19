

# Generated at 2022-06-13 18:27:42.730873
# Unit test for method min of class Timers
def test_Timers_min():
    """Test that method min returns the minimal value of named timers."""

    # Retrieve the minimal value of a named timer
    timers = Timers()
    name = "timer"
    timers._timings[name] = [1, 2, 3]
    assert timers.min(name) == 1

    # Retrieve the minimal value of a named timer with no results
    timers = Timers()
    name = "timer"
    timers._timings[name] = []
    assert timers.min(name) == 0


# Generated at 2022-06-13 18:27:49.497411
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("foo", 10)
    assert 10 == timers.max("foo")
    timers.add("foo", 20)
    assert 20 == timers.max("foo")
    try:
        timers.max("bar")
        assert False
    except KeyError:
        assert True

# Generated at 2022-06-13 18:27:59.382885
# Unit test for method median of class Timers
def test_Timers_median():
    """Test method Timers.median()"""
    timers = Timers()
    timers.add('T1', 0.1)
    timers.add('T1', 0.2)
    timers.add('T1', 0.3)
    timers.add('T1', 0.4)
    timers.add('T1', 0.5)
    assert timers.count('T1') == 5
    assert timers.total('T1') == 1.5
    assert timers.mean('T1') == 0.3
    assert timers.median('T1') == 0.3
    assert timers.min('T1') == 0.1
    assert timers.max('T1') == 0.5
    assert timers.stdev('T1') == 0.135960651641

    timers = Timers()

# Generated at 2022-06-13 18:28:05.341119
# Unit test for method median of class Timers
def test_Timers_median():
    """
    Test that the class Timers() returns the correct median from a given array of values
    """
    test_timers = Timers()
    test_array = [4, 5, 6, 7, 8, 9]

    assert test_timers.median(test_array) == test_timers.data(6.5)

# Generated at 2022-06-13 18:28:12.399299
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("foo", 0.123)
    t.add("foo", 0.456)
    t.add("bar", 0.789)
    t.add("bar", 1.234)
    t.add("foo", 0.789)
    assert t.mean("foo") == 0.456
    assert t.mean("bar") == 1.011


# Generated at 2022-06-13 18:28:21.749647
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("test", 1)
    assert t.mean("test") == 1
    t.add("test", 2)
    assert t.mean("test") == 1.5
    t.add("test", 3)
    assert t.mean("test") == 2
    t.add("test", 5)
    assert t.mean("test") == 2.75
    t.add("test", 13)
    assert t.mean("test") == 4.0


# Generated at 2022-06-13 18:28:29.260053
# Unit test for method min of class Timers
def test_Timers_min():
    test_timers = Timers()
    assert test_timers.min(name='test_min') == 0
    test_timers.add(name='test_min', value=5)
    assert test_timers.min(name='test_min') == 5
    test_timers.add(name='test_min', value=2)
    assert test_timers.min(name='test_min') == 2
    test_timers.add(name='test_min', value=10)
    assert test_timers.min(name='test_min') == 2


# Generated at 2022-06-13 18:28:34.545008
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test mean of class Timers"""
    timers = Timers()
    assert timers.mean("test1") == 0
    timers.add("test1", 110)
    assert timers.mean("test1") == 110
    timers.add("test1", 42)
    assert timers.mean("test1") == 76


# Generated at 2022-06-13 18:28:41.836625
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median() method of Timers"""
    entry = Timers()
    # Test cases
    entry.add('test', 0)
    assert entry.data['test'] == 0
    assert entry.median('test') == 0
    entry.clear()
    assert entry.data['test'] == 0
    entry.add('test', 3.0)
    assert entry.data['test'] == 3.0
    assert entry.median('test') == 3.0
    entry.clear()
    assert entry.data['test'] == 0
    entry.add('test', 3.0)
    entry.add('test', 1.0)
    entry.add('test', 2.0)
    assert entry.data['test'] == 6.0
    assert entry.median('test') == 2.0
    entry.clear()
   

# Generated at 2022-06-13 18:28:44.062809
# Unit test for method max of class Timers
def test_Timers_max():
    """Check if max works correctly
    
    Test case:
    Check that the max of an empty Timers object is 0 (zero).
    """
    timers = Timers()
    assert timers.max("test") == 0

# Generated at 2022-06-13 18:28:50.198556
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test Timers.mean()"""
    timers = Timers()
    timers.add("timer", .5)
    timers.add("timer", .7)
    timers.add("timer", .4)
    assert timers.mean("timer") == .5

# Generated at 2022-06-13 18:28:58.335694
# Unit test for method max of class Timers
def test_Timers_max():
    timer = Timers()
    timer.add('timer1', 6.1)
    timer.add('timer2', 5.2)
    timer.add('timer1', 3.4)
    timer.add('timer2', 2.4)
    timer.add('timer1', 21.1)
    timer.add('timer2', 11.2)
    timer.add('timer1', 7.5)
    timer.add('timer2', 13.4)
    timer.add('timer1', 8.0)
    timer.add('timer2', 12.1)
    assert timer.max('timer1') == 21.1
    assert timer.max('timer2') == 13.4


# Generated at 2022-06-13 18:29:00.402014
# Unit test for method min of class Timers
def test_Timers_min():
    """Test min-method"""
    timers = Timers()
    timers.add("test", 0)
    timers.add("test", 0.5)
    timers.add("test", 1.0)
    assert timers.min("test") == 0.0


# Generated at 2022-06-13 18:29:06.948650
# Unit test for method max of class Timers
def test_Timers_max():
    """Test max of Timers"""
    timers = Timers()
    timers.add('foo', 2)
    timers.add('bar', 5)
    timers.add('foo', 1)
    timers.add('foo', 4)
    assert timers.max('foo') == 4
    assert timers.max('bar') == 5

# Generated at 2022-06-13 18:29:10.134838
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    for i in range(100):
        timers.add(name='foo', value=i)
    assert timers.max(name='foo') == 99

# Generated at 2022-06-13 18:29:16.810726
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('test', float('inf'))
    assert math.isnan(timers.median('test'))

    timers.add('test', float('inf'))
    assert math.isnan(timers.median('test'))

    timers.add('test', float('inf'))
    assert math.isnan(timers.median('test'))

# Generated at 2022-06-13 18:29:18.713178
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.data["key"] = 3
    timers._timings = {
            "key": [1, 2, 3, 4, 5]
        }
    mean = timers.mean("key")
    assert mean == 3

# Generated at 2022-06-13 18:29:24.002073
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test for the mean method of class Timers"""
    timers = Timers()
    timers._timings = {
        "foo": [1.0, 2.0, 3.5, 2.5],
        "bar": [],
    }
    assert timers.mean("foo") == 2.25
    assert math.isnan(timers.mean("bar"))


# Generated at 2022-06-13 18:29:28.517197
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timer = Timers({"timer_1": 5.5})
    timer._timings = {"timer_1": [1, 2, 3, 4, 5], "timer_2": [1, 2, 3]}
    assert timer.min("timer_1") == min([1, 2, 3, 4, 5])
    assert timer.min("timer_2") == min([1, 2, 3])
    # The following should raise a KeyError exception
    try:
        _ = timer.min("timer_3")
        raise AssertionError("timer_3 should not exist")
    except KeyError:
        pass


# Generated at 2022-06-13 18:29:32.223543
# Unit test for method median of class Timers
def test_Timers_median():
    timer = Timers()
    timer.add('name', 1)
    timer.add('name', 2)
    timer.add('name', 3)
    assert timer.median('name') == 2


# Generated at 2022-06-13 18:29:41.491985
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("T1", 3.0)
    timers.add("T1", 2.0)
    timers.add("T1", 5.0)
    timers.add("T1", 8.0)
    timers.add("T2", 4.0)
    timers.add("T2", 7.0)
    assert 3.0 == timers.min("T1")
    assert 4.0 == timers.min("T2")


# Generated at 2022-06-13 18:29:53.987342
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    from math import isclose
    t = Timers()
    t.add("a", 0.5)
    t.add("a", 0.5)
    t.add("a", 0.5)
    t.add("a", 0.5)
    assert isclose(t.median("a"), 0.5)

    t = Timers()
    t.add("a", 0.5)
    t.add("a", 1.0)
    t.add("a", 1.0)
    t.add("a", 1.0)
    assert isclose(t.median("a"), 1.0)

    t = Timers()
    t.add("a", 1.0)
    t.add("a", 1.0)
    t.add

# Generated at 2022-06-13 18:30:04.604306
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    # Create a new Timers object
    timers = Timers()
    # Assert empty
    assert not timers
    # Check that an empty list raises a KeyError
    try:
        timers.mean("test_1")
        assert False, "KeyError not raised"
    except KeyError:
        assert True
    # Add one timing
    timers.add("test_1", 10)
    # Check that the mean is 10
    assert timers.mean("test_1") == 10
    # Check that the mean is 7.5
    timers.add("test_1", 5)
    assert timers.mean("test_1") == 7.5
    # Add another timing
    timers.add("test_2", 15)
    # Check that the mean of the two timers is 10
    assert timers

# Generated at 2022-06-13 18:30:08.600467
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add("test", 10)
    assert t.min("test") == 10
    t.add("test", 20)
    assert t.min("test") == 10
    t.add("test", -10)
    assert t.min("test") == -10

# Generated at 2022-06-13 18:30:13.051238
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add(name="timer1", value=1)
    timers.add(name="timer1", value=2)
    assert timers.min(name="timer1") == 1
    assert timers.min(name="unknown_name") == 0


# Generated at 2022-06-13 18:30:22.622721
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    timers.add('my_timer', 0.1)
    assert timers.max('my_timer') == 0.1
    timers.add('my_timer', 0.2)
    timers.add('my_timer', 0.3)
    timers.add('other_timer', 0.4)
    timers.add('other_timer', 0.5)
    timers.add('other_timer', 0.6)
    timers.add('another_timer', 0.7)
    assert timers.max('my_timer') == 0.3
    assert timers.max('other_timer') == 0.6
    assert timers.max('another_timer') == 0.7

# Generated at 2022-06-13 18:30:31.097780
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers.median()"""
    # Setup: Create timers object
    timers = Timers()
    timers.add('Luby', 3.0)
    timers.add('Luby', 3.0)
    timers.add('Luby', 1.0)
    timers.add('Luby', 1.0)
    timers.add('Luby', 1.0)
    timers.add('Luby', 1.0)

    # Exercise: Get median timing
    median_timing = timers.median('Luby')

    # Verify: Check that median timing is correct
    assert median_timing == 1.0

# Generated at 2022-06-13 18:30:43.134555
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max"""
    timers = Timers()
    # Test empty list
    assert timers.max("dummy") == 0

    # Test list with a single value
    timers.add("dummy", 1.0)
    assert timers.max("dummy") == 1.0

    # Test list with multiple values
    timers.add("dummy", 2.0)
    timers.add("dummy", 3.0)
    assert timers.max("dummy") == 3.0

    # Test list with non-numerical values
    timers.add("dummy", None)
    assert timers.max("dummy") == float("nan")

    # Test non-existing key
    try:
        timers.max("foobar")
    except KeyError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-13 18:30:46.630009
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers({'a': 1, 'b': 2, 'c': 3})
    assert t.max('a') == t.min('a')
    assert t.max('b') == t.min('b')
    assert t.max('c') == t.min('c')

# Generated at 2022-06-13 18:30:53.375295
# Unit test for method max of class Timers
def test_Timers_max():
    timer = Timers()
    timer.add("start", 1)
    assert timer["start"] == 1
    timer.add("start", 2)
    assert timer["start"] == 3
    timer.add("end", 4)
    assert timer["end"] == 4
    assert timer.max("start") == 2


# Generated at 2022-06-13 18:30:58.923633
# Unit test for method min of class Timers
def test_Timers_min():  # pragma: no cover
    x = Timers()
    x.add('x',3)
    x.add('x',2)
    y = x.min('x')
    assert y == 2


# Generated at 2022-06-13 18:31:03.651249
# Unit test for method median of class Timers
def test_Timers_median():
    timers: Timers = Timers()
    timers.add("timer1", 3.0)
    timers.add("timer2", 2.0)
    timers.add("timer1", 2.0)
    timers.add("timer2", 8.0)
    median: float = timers.median("timer1")
    assert median == 2.5


# Generated at 2022-06-13 18:31:04.763421
# Unit test for method median of class Timers
def test_Timers_median():
    assert Timers().median("unknown") is math.nan

# Generated at 2022-06-13 18:31:07.855226
# Unit test for method min of class Timers
def test_Timers_min():
    T = Timers()
    T.add("test",10)
    T.add("test",1)
    T.add("test2",10)
    T.add("test2",1)
    assert T.min("test") == 1
    assert T.min("test2") == 1


# Generated at 2022-06-13 18:31:13.940048
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    assert 0 == timers.max('a')
    timers.add('a', 123)
    assert 123 == timers.max('a')
    timers.add('a', 1)
    assert 123 == timers.max('a')


# Generated at 2022-06-13 18:31:17.211631
# Unit test for method min of class Timers
def test_Timers_min():
    """Test that the method Timers.min returns the correct output"""
    t = Timers({"ex": 15.6})
    t.add('ex', 1)
    assert t.min('ex') == 1.0


# Generated at 2022-06-13 18:31:22.983466
# Unit test for method min of class Timers
def test_Timers_min():
    """
    Test that min of Timers works as expected.
    """
    t = Timers()
    assert t.min("foo") == 0

    t.add("foo", 4)
    assert t.min("foo") == 4

    t.add("foo", 5)
    assert t.min("foo") == 4

    t.add("foo", 3)
    assert t.min("foo") == 3

# Generated at 2022-06-13 18:31:25.628481
# Unit test for method max of class Timers
def test_Timers_max():
	d = Timers()
	d.add('foobar', 4)
	assert d.max('foobar') == 4


# Generated at 2022-06-13 18:31:30.073411
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("a", 1)
    assert t.mean("a") == 1
    t.add("a", 2)
    assert t.mean("a") == 1.5

# Generated at 2022-06-13 18:31:41.085456
# Unit test for method median of class Timers
def test_Timers_median():
    from . import Timers
    from .timers import median_timers
    from .timers import median_timings

    timers = Timers()
    timers.add("foo", 1)
    timers.add("foo", 2)
    assert timers.median("foo") == median_timers(timers, "foo") == median_timings(timers, "foo")

    timers.add("foo", 3)
    assert timers.median("foo") == median_timers(timers, "foo") == median_timings(timers, "foo")

    timers.add("foo", 4)
    assert timers.median("foo") == median_timers(timers, "foo") == median_timings(timers, "foo")

    timers.add("foo", 5)
    assert timers.median("foo") == median

# Generated at 2022-06-13 18:31:51.273209
# Unit test for method min of class Timers
def test_Timers_min():
    """Check method min of class Timers"""
    timers = Timers()
    for name, d_time in [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("b", 5)]:
        timers.add(name=name, value=d_time)
    assert timers.min("a") == 1
    assert timers.min("b") == 3


# Generated at 2022-06-13 18:31:55.270527
# Unit test for method median of class Timers
def test_Timers_median():  # pragma: no cover
    """Unit test for method median of class Timers"""
    import pandas as pd
    import numpy as np
    from pathlib import Path
    from pyinform import utils

    # Read the timing data
    data = pd.read_csv(Path(__file__).with_name("timings.csv"))

    # Compute the median of the timings
    timers = Timers()
    for title in data.title.unique():
        grouped = data.groupby("title")
        values = grouped.get_group(title)["timing"].to_numpy()
        timers.add(title, values.sum())
        timers._timings[title] = values.tolist()

    # Compute the median of the timings and check

# Generated at 2022-06-13 18:32:01.301047
# Unit test for method min of class Timers
def test_Timers_min():
    """Test if the minimum of timers is returned correctly"""
    t = Timers({"a": 5, "b": 3})
    assert t.min("a") == 5
    assert t.min("b") == 3
    assert t.min("c") == 0



# Generated at 2022-06-13 18:32:04.276171
# Unit test for method min of class Timers
def test_Timers_min():
    import pytest
    t = Timers()
    t._timings['test'] = [0, 1, 2]
    assert t.min('test') == 0


# Generated at 2022-06-13 18:32:09.880751
# Unit test for method max of class Timers
def test_Timers_max():
    _t = Timers()
    _t.add("timer1", 10)
    _t.add("timer1", 5)
    _t.add("timer2", 6)
    assert _t.max("timer1") == 10
    assert _t.max("timer2") == 6


# Generated at 2022-06-13 18:32:13.233397
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("a", 2)
    assert t.max("a") == 2
    t.add("a", 5)
    assert t.max("a") == 5


# Generated at 2022-06-13 18:32:20.659109
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    assert math.isnan(timers.median('test'))
    timers._timings['test'].append(10)
    assert 10 == timers.median('test')
    timers._timings['test'].append(20)
    assert 15 == timers.median('test')
    timers._timings['test'].append(30)
    assert 20 == timers.median('test')
    timers._timings['test'].append(40)
    assert 25 == timers.median('test')

# Generated at 2022-06-13 18:32:23.248956
# Unit test for method median of class Timers
def test_Timers_median():
    T= Timers()
    T.add('a',1)
    T.add('a',2)
    T.add('a',3)
    assert T.median('a') == 2

# Generated at 2022-06-13 18:32:34.177696
# Unit test for method median of class Timers
def test_Timers_median():
    """Test that the method median returns a correct result"""
    from hypothesis import given, settings
    from hypothesis.strategies import integers
    from .strategies import list_float

    # Define timers
    timers = Timers()
    timers["x"] = [1, 2, 3]

    # Create correct results for each list of numbers
    results = []
    for i in range(1, len(timers["x"])+1):
        sublist = timers["x"][0:i]
        results.append(statistics.median(sublist))

    # Check the result of the method median
    for i in range(1, len(results)+1):
        assert timers.median("x") == results[i-1]


# Generated at 2022-06-13 18:32:41.768344
# Unit test for method median of class Timers
def test_Timers_median():
    # Arrange
    timers = Timers()
    timers.add("foo", 1.0)
    timers.add("foo", 2.0)
    timers.add("foo", 3.0)
    timers.add("foo", 4.0)
    timers.add("foo", 5.0)
    timers.add("foo", 6.0)
    timers.add("foo", 7.0)
    timers.add("foo", 8.0)
    timers.add("foo", 9.0)
    timers.add("foo", 10.0)
    # Act
    expected = 5.5
    actual = timers.median("foo")
    # Assert
    assert expected == actual

# Generated at 2022-06-13 18:32:51.109619
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers' method median"""
    import random
    values = list([random.random()])
    timers = Timers()
    name = 'foo'
    timers.add(name, values[0])
    assert timers.median(name) == stats.median(values)

# Generated at 2022-06-13 18:32:53.069647
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('foo', 1)
    assert timers.min('foo') == 1
    timers.add('foo', 2)
    assert timers.min('foo') == 1
    assert timers.min('bar') != 1


# Generated at 2022-06-13 18:32:56.004877
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    timers.add("a", 1)
    assert timers.mean("a") == 1.0
    timers.add("a", 2)
    assert timers.mean("a") == 1.5
    timers.add("a", 3)
    assert timers.mean("a") == 2.0

# Generated at 2022-06-13 18:33:00.074129
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("test", 4)
    timers.add("test", 5)
    assert timers.min("test") == 4
    assert timers.min("test2") == 0

# Generated at 2022-06-13 18:33:03.698125
# Unit test for method min of class Timers
def test_Timers_min():
    assert True
    timer = Timers()
    timer.add('test', 1)
    timer.add('test', 2)
    timer.add('test', 3)
    assert timer.min('test') == 1

# Generated at 2022-06-13 18:33:10.110975
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers({"foo": 100})
    t.add("bar", 5)
    assert t.min("foo") == 100
    assert t.min("bar") == 5
    t.add("bar", 10)
    assert t.min("bar") == 5
    assert t.min("baz") == 0


# Generated at 2022-06-13 18:33:13.412606
# Unit test for method max of class Timers
def test_Timers_max():
    x = Timers()
    x.add("key", 1.5)
    assert x.max("key") == 1.5
    assert x.max("not_key") == 0



# Generated at 2022-06-13 18:33:16.299281
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max

    Test:

    >>> timers = Timers()
    >>> timers.add("mo", 10.2)
    >>> timers.add("mo", 3)
    >>> timers.max("mo")
    10.2
    """

# Generated at 2022-06-13 18:33:18.584473
# Unit test for method min of class Timers
def test_Timers_min():
    '''
    Use function min to generate a single number for timing results as a test
    for the min method of class Timers
    '''
    vals = [1, 2, 3]
    expected = 1
    actual = Timers().min(vals)
    assert expected == actual, f'Expected {expected}, but got {actual}!'


# Generated at 2022-06-13 18:33:23.777298
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""

    timers = Timers()
    timers.add('foo', 10)
    timers.add('foo', 20)
    timers.add('bar', 30)

    assert timers.max('foo') == 20
    assert timers.max('bar') == 30
    assert timers.max('baz') == 0


# Generated at 2022-06-13 18:33:37.091638
# Unit test for method median of class Timers
def test_Timers_median():
    """
    Test median method of Timers class

    Test data from:
    https://www.mathsisfun.com/data/medians.html
    """
    assert Timers().median("test") == 0
    assert Timers().add("test", 1).median("test") == 1
    assert Timers().add("test", 2).median("test") == 1.5
    assert Timers().add("test", 3).median("test") == 2
    assert Timers().add("test", 4).median("test") == 2.5
    assert Timers().add("test", 5).median("test") == 3

# Generated at 2022-06-13 18:33:38.543367
# Unit test for method mean of class Timers
def test_Timers_mean():
    assert Timers({"t1": 5}).mean("t1") == 5.0

# Generated at 2022-06-13 18:33:43.660026
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers({'a': 5, 'b': 10})
    max_a = timers.max('a')
    assert max_a == 5, max_a
    max_b = timers.max('b')
    assert max_b == 10, max_b
    max_c = timers.max('c')  # should not raise an error

# Generated at 2022-06-13 18:33:47.316173
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the mean method of the Timers class"""
    timers = Timers()

    timers.add("PCG", 0.1)
    timers.add("PCG", 0.2)

    assert timers.mean("PCG") == 0.15

# Generated at 2022-06-13 18:33:51.758135
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("my_timing1", 0.1)
    timers.add("my_timing1", 0.2)
    assert timers.median("my_timing1") == 0.15
    assert timers.median("my_timing2") == 0

# Generated at 2022-06-13 18:33:55.982408
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("foo", 1)
    t.add("foo", 2)
    t.add("foo", 3)
    assert t.max("foo") == 3


# Generated at 2022-06-13 18:34:01.320835
# Unit test for method max of class Timers
def test_Timers_max():
    """Method max of class Timers"""
    timers = Timers()
    timers._timings = {
        'timer1': [2.0, 3.5, 4.5],
        'timer2': [1.0, 2.5, 1.5],
    }
    assert timers.max('timer1') == max(timers._timings['timer1'])
    assert timers.max('timer2') == max(timers._timings['timer2'])



# Generated at 2022-06-13 18:34:08.473125
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers({'foo': 3, 'bar': 6, 'baz': 9})
    assert timers.min('foo') == 3, "A wrong value was returned for the minimal timing for timer 'foo'"
    assert timers.min('bar') == 6, "A wrong value was returned for the minimal timing for timer 'bar'"
    assert timers.min('baz') == 9, "A wrong value was returned for the minimal timing for timer 'baz'"


# Generated at 2022-06-13 18:34:16.518793
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median of Timers class"""
    timers = Timers()
    timers.add('foo', 4)
    timers.add('foo', 5)
    timers.add('foo', 3)
    assert timers.median('foo') == 4
    #
    timers = Timers()
    timers.add('foo', 2)
    timers.add('foo', 3)
    timers.add('foo', 0)
    timers.add('foo', 4)
    timers.add('foo', 1)
    assert timers.median('foo') == 2.5

# Generated at 2022-06-13 18:34:23.189103
# Unit test for method mean of class Timers
def test_Timers_mean():
    from . import Timers
    from .timer import Timer
    test_timer = Timers()
    timer1 = Timer()
    timer1.start()
    timer1.stop()
    test_timer.add("test", timer1.time)
    assert test_timer.mean("test") == timer1.time



# Generated at 2022-06-13 18:34:36.558764
# Unit test for method max of class Timers
def test_Timers_max():
    x = Timers()
    x.add("y1", 20)
    x.add("y2", 10)
    x.add("y1", 30)
    x.add("y2", 15)
    x.max("y1")
    x.max("y2")


# Generated at 2022-06-13 18:34:44.963225
# Unit test for method max of class Timers
def test_Timers_max():
    """Check that the JITMax wrapping works"""
    # pylint: disable=import-outside-toplevel
    from pyccel.decorators.jit import jit
    from pyccel.decorators.jitmax import jitmax

    timers = Timers()
    # Setup
    @jit
    def f(x):
        return x

    @jitmax(timers=timers)
    def f_jitmax(x):
        return f(x)

    # Check that timers work.
    for _ in range(10):
        f_jitmax(3)

    # Check that the timing results are correct
    assert f_jitmax(4) == 4
    assert timers.total("f_jitmax") == 30
    assert timers.mean("f_jitmax") == 3

    # Check that the max function works

# Generated at 2022-06-13 18:34:50.482894
# Unit test for method median of class Timers
def test_Timers_median():
    """

    """
    # Setup
    timers = Timers()
    timers.add("foo", 0.1)
    timers.add("foo", 0.1)
    timers.add("foo", 0.2)
    # Exercise
    result = timers.median("foo")
    # Verify
    expected = 0.1
    assert result == expected

# Generated at 2022-06-13 18:34:55.268745
# Unit test for method mean of class Timers
def test_Timers_mean():

    t = Timers()

    t.add('foo', 1)
    t.add('foo', 2)
    t.add('foo', 3)

    assert t.mean('foo') == 2

    t.add('bar', 3)
    t.add('bar', 2)
    t.add('bar', 1)

    assert t.mean('bar') == 2

# Generated at 2022-06-13 18:35:00.566147
# Unit test for method mean of class Timers
def test_Timers_mean():
    timer = Timers()
    timer.add("foo", 10)
    timer.add("foo", 20)
    timer.add("bar", 30)

    assert timer.mean("foo") == 15
    assert timer.mean("bar") == 30

# Generated at 2022-06-13 18:35:07.342490
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add ( 'min1', 5 )
    assert t.min('min1') == 5
    t.add ( 'min1', 5 )
    assert t.min('min1') == 5
    t.add ( 'min1', 10 )
    assert t.min('min1') == 5
    t.add ( 'min2', 0 )
    assert t.min('min2') == 0


# Generated at 2022-06-13 18:35:09.364350
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('test', 2)
    t.add('test', 1)
    assert t.min('test') == 1


# Generated at 2022-06-13 18:35:11.820003
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test mean of Timers class"""
    timers = Timers()
    timers.add("test", 10)
    assert timers.mean("test") == 10


# Generated at 2022-06-13 18:35:19.037100
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median method of class Timers"""
    timers = Timers()
    for _ in range(100):
        timers.add('single', 0.1)
    for _ in range(10):
        timers.add('multi', 0.2)
    assert timers.median('single') == 0.1
    assert timers.median('multi') == 0.2


# Generated at 2022-06-13 18:35:31.964727
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    timers1 = Timers()
    timers1.add('timer1', 4.0)
    timers1.add('timer1', 10.0)
    assert timers1.total('timer1') == 14  # Sum of two values
    assert timers1.min('timer1') == 4  # Minimal value
    assert timers1.count('timer1') == 2  # Number of values
    assert timers1._timings['timer1'] == [4, 10]  # Internal value
    timers1.clear()
    timers1.add('timer2', 6.0)
    timers1.add('timer2', 20.0)
    timers1.add('timer2', 9.0)
    assert timers1.total('timer2') == 35  # Sum of three values

# Generated at 2022-06-13 18:35:44.647905
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.data["test"] = 2.0
    assert timers.min("test") == 0.0

if __name__ == "__main__":
    test_Timers_min()

# Generated at 2022-06-13 18:35:52.062719
# Unit test for method max of class Timers
def test_Timers_max():
    """
    Let's create a Timers instance.
    Check that the maximum value is equal to max(values)
    """
    timers = Timers()  # We create a Timers object
    values = [1, 2, 3, 4]  # We create a list with values
    timers.add("timer", values[0])  # We add the first value of the list to the Timers instance
    assert timers.max("timer") == max(values)  # We check that their values are equal
    timers.clear()  # We clear the instance



# Generated at 2022-06-13 18:35:58.418478
# Unit test for method median of class Timers
def test_Timers_median():
    """Check for the actual value of median for the test data"""
    test_dictionary = {'test1': [1, 2, 3, 4], 'test2': [2, 4, 6, 8]}
    test_timers = Timers()
    for item in test_dictionary:
        if len(test_dictionary[item]) % 2 != 0:
            for i in range(len(test_dictionary[item])):
                test_timers.add(item, test_dictionary[item][i])
            assert test_timers.median(item) == (test_dictionary[item][1] + test_dictionary[item][2]) / 2
        else:
            for i in range(len(test_dictionary[item])):
                test_timers.add(item, test_dictionary[item][i])

# Generated at 2022-06-13 18:36:04.028122
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median() method of Timers class"""
    t = Timers()
    t.add('a', 3)
    assert t.median('a') == 3
    t.add('a', 4)
    assert t.median('a') == 3.5
    t.add('a', 5)
    assert t.median('a') == 4
    t.add('a', 6)
    assert t.median('a') == 4.5
    t.add('a', 7)
    assert t.median('a') == 5

# Generated at 2022-06-13 18:36:10.309372
# Unit test for method max of class Timers
def test_Timers_max():
    """Check if timer is cleared correctly"""
    t = Timers()
    t.add("one", 1.0)
    t.add("one", 2.0)
    t.add("one", 3.0)
    t.add("one", 4.0)
    return t.max("one") == 4.0


# Generated at 2022-06-13 18:36:19.891163
# Unit test for method min of class Timers
def test_Timers_min():
    """Test Timers class method min"""
    import hypothesis
    import hypothesis.strategies as st
    from pytest import raises

    timers = Timers()

    @hypothesis.given(st.lists(st.floats()))
    def test(values: List[float]) -> None:
        """Test Timers class method min"""
        timers.clear()
        name = "test_name"
        for value in values:
            timers.add(name, value)
        res = timers.min(name=name)
        assert res == min(values or [0])

    test()
    with raises(KeyError):
        timers.min("no_such_name")



# Generated at 2022-06-13 18:36:22.435357
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("timing", 1.0)
    assert timers.min("timing") == 1.0


# Generated at 2022-06-13 18:36:27.481253
# Unit test for method max of class Timers
def test_Timers_max():
  """
  Unit test for method max of class Timers.
  """
  # Initialize timer object and add two timer names
  timers = Timers()
  timers.add("a", 2)
  timers.add("b", 3)
  # Check max
  timers.max("a")
  assert(timers.max("a") == 2)
  assert(timers.max("b") == 3)

# Generated at 2022-06-13 18:36:34.971995
# Unit test for method median of class Timers
def test_Timers_median():
    """
    Check that the median of a set of values is computed correctly
    """
    timers = Timers()
    even = [1, 2, 3, 4]
    odd = [1, 2, 3, 4, 5]
    empty = []
    assert timers.apply(lambda values: statistics.median(values or [0]), even)
    assert timers.apply(lambda values: statistics.median(values), odd)
    assert timers.apply(lambda values: statistics.median(values), empty)

# Generated at 2022-06-13 18:36:36.902378
# Unit test for method min of class Timers
def test_Timers_min():
    # Create instance
    instance = Timers()
    # Call method
    print(instance.min(name = 'name'))
    # ValueError expected
    return True


# Generated at 2022-06-13 18:36:48.435886
# Unit test for method min of class Timers
def test_Timers_min():
    """Minimal value of timings"""
    timers = Timers()
    timers.add("test", 2)
    assert timers.min("test") == 2


# Generated at 2022-06-13 18:36:53.259042
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.data = {"a": 123}
    timers._timings = {"a": [1, 2, 3, 4, 5]}

    assert timers.median("a") == 3


# Generated at 2022-06-13 18:36:57.764852
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("Foo", 0.1)
    timers.add("Foo", 0.2)
    timers.add("Bar", 0.2)
    assert timers.mean("Foo") == 0.15
    assert timers.mean("Bar") == 0.2
    assert timers.mean("Baz") == 0  # noqa: WPS421

if __name__ == "__main__":
    test_Timers_mean()

# Generated at 2022-06-13 18:37:05.748785
# Unit test for method max of class Timers
def test_Timers_max():
    """Check that Timers.max works properly"""
    timers = Timers()
    timers._timings["test"] = [1.0]
    assert timers.max("test") == 1.0
    timers._timings["test"] = [0.0]
    assert timers.max("test") == 0.0
    timers._timings["test"] = [1.0, 2.0]
    assert timers.max("test") == 2.0
    try:
        timers.max("wrong")
    except KeyError:
        pass
    else:
        assert False

# Generated at 2022-06-13 18:37:11.679151
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    # insert some random values into the list
    timers._timings["My Timer"] = [50, 70]
    assert timers.mean("My Timer") == 60


# Generated at 2022-06-13 18:37:14.597079
# Unit test for method min of class Timers
def test_Timers_min():
    """Test Timers.min() on a single-timer timer structure"""
    timers = Timers()
    timers.add("MIN", 12.34)
    assert timers.min("MIN") == 12.34



# Generated at 2022-06-13 18:37:16.280422
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers._timings = {"test": [1, 2, 3, 4, 5]}
    assert timers.max("test") == 5


# Generated at 2022-06-13 18:37:19.038466
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('a', 1)
    assert timers.min('a') == 1



# Generated at 2022-06-13 18:37:23.317707
# Unit test for method max of class Timers
def test_Timers_max():
    # Create Timers instance
    tim = Timers()

    # Timer.__setitem__
    tim["foo"] = 0

    # Timer.add
    tim.add("foo", 0)

    # Timer.clear
    tim.clear()

    # Timer.apply
    def func(a: List[float]) -> float:
        return 1

    tim.apply(func, name="foo")

    # Timer.count
    tim.count("foo")

    # Timer.total
    tim.total("foo")

    # Timer.min
    tim.min("foo")

    # Timer.max
    tim.max("foo")

    # Timer.mean
    tim.mean("foo")

    # Timer.median
    tim.median("foo")

    # Timer.stdev


# Generated at 2022-06-13 18:37:26.459533
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    timers.add("foo", 42)
    timers.add("foo", 23)
    timers.add("bar", -1)
    assert timers.mean("foo") == 32.5  # manually calculated mean of [42, 23]
    assert timers.mean("bar") == -1.0  # manually calculated mean of [-1]
    assert timers.mean("nonexistent") == 0.0  # median of empty list is 0.0