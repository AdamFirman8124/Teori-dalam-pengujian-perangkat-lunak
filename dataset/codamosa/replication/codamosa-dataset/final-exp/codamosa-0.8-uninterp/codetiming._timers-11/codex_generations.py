

# Generated at 2022-06-13 18:27:39.515078
# Unit test for method median of class Timers
def test_Timers_median():
    import random
    import statistics
    x = random.sample(range(1, 1000), 999)
    timers = Timers({'test': 0})
    for i in x:
        timers.add('test', i)
    assert timers.data['test'] == 499500
    assert timers.median('test') == statistics.median(x)

# Generated at 2022-06-13 18:27:49.461449
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    assert timers.median('test') == 0
    timers.add('test', 0)
    assert timers.median('test') == 0
    timers.add('test', 1)
    assert timers.median('test') == 0.5
    timers.add('test', 2)
    assert timers.median('test') == 1.0
    timers.add('test', 3)
    assert timers.median('test') == 1.5
    timers.add('test', 4)
    assert timers.median('test') == 2.0
    timers.add('test', 5)
    assert timers.median('test') == 2.5
    timers.add('test', 6)
    assert timers.median('test') == 3.5
    timers.add('test', 7)

# Generated at 2022-06-13 18:27:58.654044
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Check that the method mean() of the class Timers has been correctly implemented"""
    # Construct a Timers object with 2 timers and a different number of timings
    timers = Timers()
    timers["mean_test"] = [1, 2, 3, 4, 5, 6]
    timers["mean_test2"] = [1]
    # Check that mean() returns the expected values
    assert timers.mean("mean_test") == (1 + 2 + 3 + 4 + 5 + 6) / 6
    assert timers.mean("mean_test2") == 1
    # Check that mean() raises a KeyError if the name of the timer is non-existent
    assert timers.mean("mean_test3")



# Generated at 2022-06-13 18:28:05.682769
# Unit test for method mean of class Timers
def test_Timers_mean():
    # initialize empty Timers
    t = Timers()
    # check that mean of empty Timers is None
    assert(t.mean("mean") == 0.0)
    # add a few values to Timers
    t.add("mean", 0.0)
    t.add("mean", 1.0)
    assert(t.mean("mean") == 0.5)

# Generated at 2022-06-13 18:28:14.185151
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    # Empty Timer
    with pytest.raises(KeyError, match=r"s0"):
        timers.max("s0")
    # Success
    timers.add("s0", 3)
    timers.add("s0", 4)
    timers.add("s0", 5)
    timers.add("s0", 2)
    assert timers.max("s0") == 5, "Bad max()"
    # Add duplicate
    timers.add("s0", 5)
    assert timers.max("s0") == 5, "Bad max()"


# Generated at 2022-06-13 18:28:20.005103
# Unit test for method min of class Timers
def test_Timers_min():
    """Test correctness of Timers.min method"""
    timers = Timers()
    timers.add("my timer", 3)
    assert timers.min("my timer") == 3
    timers.add("my timer", 5)
    assert timers.min("my timer") == 3


# Generated at 2022-06-13 18:28:25.967433
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('foo', 1)
    t.add('bar', 4)
    t.add('baz', 3)
    t.add('foo', 0.5)
    assert t.min('foo') == 0.5
    assert t.min('bar') == 4
    assert t.min('baz') == 3


# Generated at 2022-06-13 18:28:31.591632
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the median method of the Timers class"""
    timers = Timers()
    timers.add("one", 1)
    timers.add("one", 2)
    timers.add("one", 3)
    assert timers.median("one") == 2
    assert timers.median("two") == 0


# Generated at 2022-06-13 18:28:35.854489
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('time', 0.4)
    timers.add('time', 1.2)
    assert timers.min('time') == 0.4
    assert timers.min('no_key') == 0.0


# Generated at 2022-06-13 18:28:37.236654
# Unit test for method max of class Timers
def test_Timers_max():
    Timer.timers.clear()
    Timer.timers.max("max_error")

# Generated at 2022-06-13 18:28:44.289142
# Unit test for method median of class Timers
def test_Timers_median():
    """Test method Timers.median"""

    t = Timers()
    t.add('foo', 0)
    assert t.median('foo') == 0

    t.add('bar', 1)
    assert t.median('bar') == 1

    t.add('baz', 2)
    assert t.median('baz') == 1

    t.add('baz', 3)
    assert t.median('baz') == 2

    t.add('baz', 4)
    assert t.median('baz') == 2

    t.add('baz', 5)
    assert t.median('baz') == 3

    t.add('baz', 6)
    assert t.median('baz') == 3

    t.add('baz', 7)
    assert t.median

# Generated at 2022-06-13 18:28:50.624723
# Unit test for method mean of class Timers
def test_Timers_mean():
    import pytest
    with pytest.raises(KeyError):
        Timers().mean("unknown")

    assert Timers().mean("name") == 0.0

    timer = Timers()
    timer.add("name", 1.0)
    timer.add("name", 2.0)
    timer.add("name", 3.0)
    assert timer.mean("name") == 2.0

# Generated at 2022-06-13 18:28:55.056720
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("total_time", 1)
    timers.add("total_time", 2)
    timers.add("total_time", 3)
    timers.add("total_time", 0)
    assert timers.min("total_time") == 0
    assert timers.min("total_time2") == 0

# Generated at 2022-06-13 18:29:03.639030
# Unit test for method median of class Timers
def test_Timers_median():
    input = [3, 4, 6, 7, 8, 10, 11, 12, 13, 14]
    result = statistics.median(input)
    true = 9.5
    assert result == true, f"Wrong result: {result}, Should be {true}"

    input = [3, 4, 6, 7, 8, 10, 11, 12, 13]
    result = statistics.median(input)
    true = 8.5
    assert result == true, f"Wrong result: {result}, Should be {true}"

    input = [3, 4, 6, 7, 8, 10, 11, 12]
    result = statistics.median(input)
    true = 8
    assert result == true, f"Wrong result: {result}, Should be {true}"

# Generated at 2022-06-13 18:29:14.223293
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Tests method mean of class Timers"""
    collection = Timers()
    collection.add('timers', 0.01)
    collection.add('timers', 0.02)
    collection.add('timers', 0.03)
    collection.add('timers', 0.04)
    collection.add('timers', 0.05)
    collection.add('timers', 0.06)
    collection.add('timers', 0.07)
    collection.add('timers', 0.08)
    collection.add('timers', 0.09)
    collection.add('timers', 0.10)
    assert collection.mean('timers') == 0.055

# Generated at 2022-06-13 18:29:25.143852
# Unit test for method min of class Timers
def test_Timers_min():
    # Test minimal timing is correctly computed
    timers = Timers()
    timers.add('test1', 1.0)
    timers.add('test1', 0.0)
    timers.add('test1', 2.0)
    assert timers.min('test1') == 0

    # Test minimal timing is correctly computed even if the time measurement was 0
    timers = Timers()
    timers.add('test1', 1.0)
    timers.add('test1', 0.0)
    timers.add('test1', 0.0)
    assert timers.min('test1') == 0

    # Test a KeyError is raised if the timer is not present in the dictionary
    timers = Timers()
    timers.add('test1', 1.0)
    with pytest.raises(KeyError):
        timers.min('test2')

# Generated at 2022-06-13 18:29:33.022353
# Unit test for method median of class Timers
def test_Timers_median():
    timer = Timers()
    timer.add('test', 1)
    timer.add('test', 2)
    timer.add('test', 3)
    assert timer.median('test') == 2
    timer.add('test', 4)
    assert timer.median('test') == 2.5
    timer.add('test', 5)
    assert timer.median('test') == 3

# Generated at 2022-06-13 18:29:36.740958
# Unit test for method max of class Timers
def test_Timers_max():
    ts = Timers()
    ts.add('foo', 3)
    ts.add('foo', 2)
    ts.add('foo', 7)
    ts.add('bar', 12)
    assert ts.max('foo') == 7
    assert ts.max('bar') == 12

# Generated at 2022-06-13 18:29:42.623423
# Unit test for method median of class Timers
def test_Timers_median():
    # Set up data
    values = [5, 600, 800, 1500, 1300, 1400, 2000, 2100, 2200, 2300, 2400]
    # Create instance of class
    f = Timers()
    # Set up name with arbitrary value
    f["name1"] = 1
    # Set up values for timings with name
    f._timings["name1"] = values
    # Call and test method
    assert f.median("name1") == 1900

# Generated at 2022-06-13 18:29:52.943043
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""

    # Define tests to run
    tests = [
        ([-4.0, 6.0, -2.0, 10.0], -1.5),
        ([-4.0, 6.0, -2.0], -2.0),
        ([100.0, 300.0, 0.0], 100.0),
    ]

    # Run tests
    for values, expected in tests:
        timers = Timers({"one": 100.0, "two": 200.0})
        timers._timings = {"test": values}
        assert round(timers.median("test"), 6) == expected

# Generated at 2022-06-13 18:30:01.690640
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    assert t.max("A") == 0
    t.add("A", 2.0)
    assert t.max("A") == 2.0
    t.add("A", 1.0)
    assert t.max("A") == 2.0
    t.add("A", 3.0)
    assert t.max("A") == 3.0
    t.clear()
    assert t.max("A") == 0


# Generated at 2022-06-13 18:30:07.085211
# Unit test for method max of class Timers
def test_Timers_max():
    dict = Timers()
    dict.add('foo', 3.14)
    assert dict.max('foo') == 3.14
    dict.add('foo', 5)
    assert dict.max('foo') == 5
    dict.add('foo', 1)
    assert dict.max('foo') == 5
    dict.add('foo', 0)
    assert dict.max('foo') == 5

# Generated at 2022-06-13 18:30:12.948790
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()

    timers.add('x', 2.0)
    assert timers.min('x') == 2.0

    timers.add('y', 3.0)
    assert timers.min('y') == 3.0

    timers.add('y', 1.0)
    assert timers.min('y') == 1.0


# Generated at 2022-06-13 18:30:17.829438
# Unit test for method max of class Timers
def test_Timers_max():
    # Setup
    counter = Timers()

    # Exercise
    counter.add("loop", 63)
    counter.add("loop", 65)
    counter.add("loop", 66)

    # Verify
    assert counter.max("loop") == 66

# Generated at 2022-06-13 18:30:21.095510
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("name", 1)
    timers.add("name", 2)
    timers.add("name", None)
    assert timers.max("name") == 2
    assert timers.max("nonexistent") == 0


# Generated at 2022-06-13 18:30:25.411515
# Unit test for method min of class Timers
def test_Timers_min():
    from copy import copy
    timers = Timers()
    timers.add('timer', 100)
    timers.add('timer', 200)
    timers.add('timer', 300)
    timers.add('timer', 400)
    assert timers.min('timer') == 100
    timers_copy = copy(timers)
    timers_copy.add('timer', 500)
    assert timers.min('timer') == 100
    assert timers_copy.min('timer') == 100
    assert timers == timers_copy


# Generated at 2022-06-13 18:30:28.052725
# Unit test for method mean of class Timers
def test_Timers_mean():
    self = Timers()
    self.data = {'test': 1.0}
    assert(self.mean('test') == 1.0)


# Generated at 2022-06-13 18:30:40.954585
# Unit test for method median of class Timers
def test_Timers_median():
    """Check that the median function is working for special cases"""
    timers = Timers()
    assert timers.median("foo") == 0
    timers.data["foo"] = 1.0
    timers._timings["foo"] = [0.0]
    assert timers.median("foo") == 0.0
    timers._timings["foo"] = [5.0]
    assert timers.median("foo") == 5.0
    timers._timings["foo"] = [1.0, 2.0]
    assert timers.median("foo") == 1.5
    timers._timings["foo"] = [1.0, 3.0, 5.0]
    assert timers.median("foo") == 3.0
    timers._timings["foo"] = [1.0, 5.0, 3.0]
    assert timers

# Generated at 2022-06-13 18:30:47.675937
# Unit test for method max of class Timers
def test_Timers_max():
    Timer = Timers()
    Timer.add('print', 0.17777777777777776)
    Timer.add('print', 0.30861111111111113)
    Timer.add('print', 0.19083333333333335)
    Timer.add('print', 0.17999999999999994)
    Timer.add('print', 0.17694444444444457)
    Timer.add('print', 0.18944444444444437)
    Timer.add('print', 0.1738888888888889)

    # Test whether Timer.max = 0.30861111111111113
    assert Timer.max('print') == 0.30861111111111113

# Generated at 2022-06-13 18:30:50.146659
# Unit test for method min of class Timers
def test_Timers_min():
    x = Timers()
    assert x.min('test') == 0
 

# Generated at 2022-06-13 18:31:03.340036
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add('test1', 1)
    t.add('test1', 2)
    t.add('test1', 3)
    t.add('test1', 4)
    t.add('test1', 5)
    t.add('test1', 6)
    t.add('test2', 2)
    t.add('test2', 3)

    assert t.total('test1') == 21
    assert t.total('test2') == 5
    assert t.min('test1') == 1
    assert t.min('test2') == 2
    assert t.max('test1') == 6
    assert t.max('test2') == 3
    assert t.mean('test1') == 3.5
    assert t.mean('test2') == 2.5

# Generated at 2022-06-13 18:31:18.175733
# Unit test for method median of class Timers
def test_Timers_median():
    # source: https://docs.python.org/3/library/statistics.html
    # test_data: [2.0, 3.0, 4.0]
    data = Timers()
    data._timings = {'test_data': [2.0, 3.0, 4.0]}
    res = data.median('test_data')
    assert res == 3.0
    # test_data: [1, 2, 4]
    data._timings = {'test_data': [1, 2, 4]}
    res = data.median('test_data')
    assert res == 2
    # test_data: [10, 3, 2, 4]
    data._timings = {'test_data': [10, 3, 2, 4]}
    res = data.median('test_data')


# Generated at 2022-06-13 18:31:21.969353
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)

    assert timers.mean('timer1') == 1.5


# Generated at 2022-06-13 18:31:25.573679
# Unit test for method mean of class Timers
def test_Timers_mean():

    # prepare parameters
    values = [1, 2, 3]
    res = Timers()

    # assertion
    assert res.mean(values) == 2.0

# Generated at 2022-06-13 18:31:31.251593
# Unit test for method min of class Timers
def test_Timers_min():
    """Test that Timers.min() returns the minimal value of all timings"""
    timers = Timers()
    timers.add('timer1', 1)
    timers.add('timer1', 2)
    assert timers.min('timer1') == 1


# Generated at 2022-06-13 18:31:36.332451
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min('something') == 0.0
    timers.add('something', 1)
    assert timers.min('something') == 1.0
    timers.add('something', 2)
    assert timers.min('something') == 1.0


# Generated at 2022-06-13 18:31:42.497348
# Unit test for method max of class Timers
def test_Timers_max():
    from pytest import raises
    timers = Timers()
    assert timers.max(name="test") == 0
    timers.add(name="test", value=0)
    assert timers.max(name="test") == 0
    timers.add(name="test", value=1)
    assert timers.max(name="test") == 1
    with raises(KeyError):
        timers.max(name="test_other")


# Generated at 2022-06-13 18:31:56.916395
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    assert timers.mean('t1') == 0.0
    timers.add('t1', 1.0)
    assert timers.mean('t1') == 1.0
    timers.add('t1', 2.0)
    assert timers.mean('t1') == 1.5
    assert timers.data['t1'] == 3.0
    # Timers do not support assignment
    with pytest.raises(TypeError):
        timers['t1'] = 1.0
    # KeyError for non-existent timer
    with pytest.raises(KeyError):
        timers.mean('xxx')

if __name__ == '__main__':
    import pytest    # pylint: disable=import-outside-toplevel

# Generated at 2022-06-13 18:32:00.366325
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    obj = Timers()
    obj._timings["test"] = [0, 1, 2, 3]
    assert obj.median("test") == 1.5

# Generated at 2022-06-13 18:32:02.617296
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    for i in range(3):
        timers.add('test', i)
    assert timers.max('test')==2

# Generated at 2022-06-13 18:32:11.777789
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test method mean for class Timers"""
    timers = Timers()
    timers.add("test", 2)
    timers.add("test", 1)
    timers.add("test", 3)
    assert timers.mean("test") == 2


# Generated at 2022-06-13 18:32:13.276634
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    pass

# Generated at 2022-06-13 18:32:20.322009
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('test', 1)
    assert timers.median('test') == 1
    timers.add('test', 2)
    assert timers.median('test') == 1.5
    timers.add('test', 3)
    assert timers.median('test') == 2
    timers.add('test', 4)
    assert timers.median('test') == 2.5
    timers.add('test', 5)
    assert timers.median('test') == 3

# Generated at 2022-06-13 18:32:25.052392
# Unit test for method min of class Timers
def test_Timers_min():

    # Create Timers object
    timers = Timers()

    # Add a timing
    timers.add('foo', 2.0)
    assert timers.min('foo') == 2.0

    # Add another timing
    timers.add('foo', 4.0)
    assert timers.min('foo') == 2.0

    # Add a timing that is smaller
    timers.add('foo', 1.0)
    assert timers.min('foo') == 1.0

# Generated at 2022-06-13 18:32:27.485607
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("name", 1)
    assert timers.mean("name") == 1


# Generated at 2022-06-13 18:32:36.123633
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for the method mean of class Timers.
    It should return the arithmetic mean over a list of numbers.
    """
    timer_list = Timers()
    timer_list.add("A", 3)
    timer_list.add("A", 7)
    timer_list.add("B", 7)
    assert timer_list.mean("A") == 5
    assert timer_list.mean("B") == 7

    timer_list.clear()
    timer_list.add("A", 1)
    timer_list.add("A", 2)
    timer_list.add("A", 8)
    timer_list.add("B", 1)
    timer_list.add("B", 1)
    assert timer_list.mean("A") == 3.67
    assert timer_list.mean("B") == 1

   

# Generated at 2022-06-13 18:32:38.543576
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("timer1", 0.1)
    t.add("timer1", 2.3)
    return t.max("timer1") == 2.3

# Generated at 2022-06-13 18:32:46.229324
# Unit test for method max of class Timers
def test_Timers_max():
    from math import nan
    timers = Timers()

    assert timers.max('dummy') == 0

    timers.add('dummy', 1.0)
    assert timers.max('dummy') == 1

    timers.add('dummy', 2.0)
    assert timers.max('dummy') == 2

    timers.add('dummy', 0.0)
    assert timers.max('dummy') == 2

    timers.add('dummy', nan)
    assert timers.max('dummy') == 2

# Generated at 2022-06-13 18:32:52.786592
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    # Create timers
    timers = Timers()
    # Add some timing data
    timers.add('test', 17.7)
    timers.add('test', 17.9)
    timers.add('test', 18.0)
    timers.add('test', 18.4)
    # Make sure median is correct
    assert timers.median('test') == 18.0


# Generated at 2022-06-13 18:33:01.449000
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("a", 1)
    assert timers.min("a") == 1
    timers.add("a", 3)
    assert timers.min("a") == 1
    timers.add("b", -1)
    assert timers.min("b") == -1
    timers.add("c", -1)
    assert timers.min("c") == -1
    assert timers.min("d") == 0


# Generated at 2022-06-13 18:33:11.779400
# Unit test for method max of class Timers
def test_Timers_max():
    """Test for method max of class Timers"""
    timers = Timers()
    timers.add('test_timer', 1.0)
    assert timers.apply(lambda l: max(l), name='test_timer') == 1.0
    assert timers.max('test_timer') == 1.0


# Generated at 2022-06-13 18:33:15.726459
# Unit test for method max of class Timers
def test_Timers_max():
    """Test how Timers method max is working"""
    from .utils import get_timers, get_timers_map

    timers = get_timers()
    timers.max("not")
    timers_map = get_timers_map()
    timers_map.max("not")

# Generated at 2022-06-13 18:33:22.949821
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("a", 0)
    assert t.mean("a") == 0
    t.add("a", 1)
    assert t.mean("a") == 0.5
    t.add("a", 2)
    assert t.mean("a") == 1.0
    t.add("a", 3)
    assert t.mean("a") == 1.5

# Generated at 2022-06-13 18:33:27.191477
# Unit test for method mean of class Timers
def test_Timers_mean():
    """
    Test if mean value of timings works
    """
    timers = Timers()
    timers.add("test", 10)
    timers.add("test", 20)
    assert timers.mean("test") == 15    
    

# Generated at 2022-06-13 18:33:32.223626
# Unit test for method max of class Timers
def test_Timers_max():
    """Test for method max of class Timers"""

    # Default initialization
    timers = Timers()

    timers.add("timer1", 1.5)
    timers.add("timer2", 3.0)
    timers.add("timer1", 2.5)
    timers.add("timer2", 2.0)

    assert timers.max("timer1") == 2.5
    assert timers.max("timer2") == 3.0

# Generated at 2022-06-13 18:33:37.661651
# Unit test for method max of class Timers
def test_Timers_max():
    """Test the max method of the Timers class"""
    from pytest import approx

    timers = Timers()
    timers.add("test", -1)
    assert timers.max("test") == approx(-1)
    timers.add("test", 3)
    assert timers.max("test") == approx(3)
    timers.add("test", -2)
    assert timers.max("test") == approx(3)

# Generated at 2022-06-13 18:33:41.641428
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("test",1.5)
    t.add("test",2.0)
    t.add("test",0.5)
    print(t.mean("test"))

test_Timers_mean()

# Generated at 2022-06-13 18:33:44.073153
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("timer_max", 1.0)
    assert timers.max("timer_max") == 1.0


# Generated at 2022-06-13 18:33:46.730584
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('timer1', 1.0)
    t.min('timer1')
    t.add('timer1', 0.0)
    t.min('timer1')


# Generated at 2022-06-13 18:33:53.428854
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test mean method of Timers class"""
    timers = Timers()
    assert timers.mean('test') == 0.0
    timers.data['test'] = 1.0
    timers._timings['test'] = [1.0]
    assert timers.mean('test') == 1.0
    timers.data['test'] = 5.0
    timers._timings['test'].append(2.0)
    timers._timings['test'].append(3.0)
    assert timers.mean('test') == 2.5

# Generated at 2022-06-13 18:34:03.541173
# Unit test for method mean of class Timers
def test_Timers_mean():
    timer = Timers()
    timer.add("", 100)
    timer.add("", 200)
    return timer.mean("") == (100 + 200) / 2

# Generated at 2022-06-13 18:34:12.653429
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the method mean of class Timers"""
    from hypothesis import given
    from hypothesis.strategies import floats

    timers = Timers()
    name = "some_name"
    for value in [5.5, 5.5, 4.5, 5.5, 6.5]:
        timers.add(name=name, value=value)
    assert isinstance(timers, collections.UserDict)
    assert isinstance(timers._timings, collections.defaultdict)
    assert isinstance(timers._timings[name], list)
    assert isinstance(timers.data, collections.UserDict)
    assert isinstance(timers.data[name], float)
    assert timers.mean(name=name) == pytest.approx(5.5)



# Generated at 2022-06-13 18:34:16.980082
# Unit test for method max of class Timers
def test_Timers_max():
    """Test function for method max of class Timers"""
    data = {'1': 10**-2, '2': 10**1, '3': 10**-1}
    timings = {'1': [10**-3, 10**-3, 10**-2], '2': [10**2, 10**3, 10**4], '3': [10**-5, 10**-4, 10**-3]}
    timers = Timers(data)
    timers._timings = timings
    assert timers.max('1') == 10**-2
    assert timers.max('2') == 10**4
    assert timers.max('3') == 10**-1

# ---------   Remove whitespaces from string   ---------


# Generated at 2022-06-13 18:34:22.646613
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("test", 1)
    assert t.max("test") == 1
    t.add("test", 2)
    assert t.max("test") == 2
    t.add("test", 3)
    assert t.max("test") == 3


# Generated at 2022-06-13 18:34:25.114746
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("distances", 12.34)
    timers.add("distances", 23.45)
    assert 17.895 == timers.mean("distances")
    assert 0 == timers.mean("other")

# Unit test method min of class Timers

# Generated at 2022-06-13 18:34:36.220592
# Unit test for method min of class Timers
def test_Timers_min():
    """Test min(name) of class Timers"""
    timers = Timers()
    timers.add("t1", 1)
    timers.add("t1", 2)
    timers.add("t1", 3)
    timers.add("t2", -3)
    assert timers.min("t1") == 1, "min(t1) should be 1"
    assert timers.min("t2") == -3, "min(t2) should be -3"
    try:
        timers.min("t3")
    except KeyError as err:
        assert err.args[0] == "t3", "KeyError for unknown name"
    else:
        assert False, "KeyError should be raised for unknown name"

# Generated at 2022-06-13 18:34:42.930755
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('a', 1.0)
    timers.add('b', 3.0)
    timers.add('b', 2.0)

    assert timers.count('a') == 1
    assert timers.count('b') == 2
    assert timers['a'] == 1.0
    assert timers['b'] == 5.0
    assert timers.max('a') == 1.0
    assert timers.max('b') == 3.0
    assert timers.min('a') == 1.0
    assert timers.min('b') == 2.0

# Generated at 2022-06-13 18:34:47.952251
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()

    timers.add("ntrees", 90)
    timers.add("ntrees", 120)
    timers.add("ntrees", 150)

    assert(timers.median("ntrees") == 120)

# Generated at 2022-06-13 18:34:51.476190
# Unit test for method median of class Timers
def test_Timers_median():
    timer = Timers()
    timer.add('name', 1)
    timer.add('name', 2)
    timer.add('name', 4)
    assert timer.count('name') == 3
    assert timer.median('name') == 2

# Generated at 2022-06-13 18:34:55.168066
# Unit test for method max of class Timers
def test_Timers_max():
    """Test max method"""
    timers = Timers()
    timers.add('test', 5)
    assert timers.max('test') == 5
    with pytest.raises(KeyError):
        timers.max('wrong_key')

# Generated at 2022-06-13 18:35:11.029111
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    timers.add('timer1', 1.0)
    assert(timers.mean('timer1') == 1.0)

    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
    assert(timers.mean('timer1') == (1.0 + 2.0 + 3.0) / 3.0)

    try:
        timers.mean('timer2')
        assert(False)  # This should not be reached
    except KeyError:
        assert(True)  # This should be reached


test_Timers_mean()
# EOF

# Generated at 2022-06-13 18:35:18.833044
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()

    timers.add("a", 1.0)
    timers.add("a", 2.0)
    timers.add("b", 3.0)
    timers.add("b", 4.0)

    assert timers.max("a") == 2.0
    assert timers.max("b") == 4.0

    try:
        timers.max("c")
    except KeyError:
        assert True

# Generated at 2022-06-13 18:35:31.235060
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers
    """
    timers = Timers()
    timers.add("Timer 1", 2.0)
    timers.add("Timer 1", 0.5)
    timers.add("Timer 2", 3.0)
    timers.add("Timer 2", 0.75)
    timers.add("Timer 2", 4.0)
    timers.add("Timer 3", 0.0)
    assert timers.mean("Timer 1") == 1.25
    assert timers.mean("Timer 2") == 2.25
    assert timers.mean("Timer 3") == 0.0
    assert timers.mean("Missing") == 0.0

if __name__ == "__main__":  # pragma: no cover
    test_Timers_mean()

# Generated at 2022-06-13 18:35:38.559854
# Unit test for method max of class Timers
def test_Timers_max():
    """Test method max of class Timers"""
    import warnings

    # Create objects
    timers = Timers()
    
    # Add a value to a timer
    timers.add("First test", 1.0)
    timers.add("First test", 2.0)
    
    # Test the max function
    assert 2.0 == timers.max("First test")
    
    # Test the max function with another timer
    assert 0.0 == timers.max("Second test")


# Generated at 2022-06-13 18:35:42.922362
# Unit test for method median of class Timers
def test_Timers_median():
    """
    Test the method Timers.median
    """
    timers = Timers()
    timers.add('test', 2)
    timers.add('test', 6)
    timers.add('test', 6)
    timers.add('test', 0)
    timers.add('test', 4)
    assert timers.median('test') == 4


# Generated at 2022-06-13 18:35:48.010153
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers.median()"""
    timers = Timers()
    timers._timings['test'] = [1, 2, 3, 4, 5]
    assert timers.median('test') == 3
    timers._timings['test'] = [1, 5]
    assert timers.median('test') == 3
    timers._timings['test'] = [1, 2]
    assert timers.median('test') == 1.5
    timers._timings['test'] = [1]
    assert timers.median('test') == 1
    timers._timings['test'] = []
    assert timers.median('test') == 0

# Generated at 2022-06-13 18:35:56.468977
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the median function of the Timers class"""
    # Test case: empty list of timings
    data = collections.defaultdict(list)
    timers = Timers()
    timers._timings = data
    assert timers.median("test") == 0

    # Test case: single timing
    data["test"].append(1)
    assert timers.median("test") == 1

    # Test case: list with even number of timings
    data["test"].extend([2, 4, 5, 7])
    assert timers.median("test") == 4

    # Test case: list with odd number of timings
    data["test"].extend([11, 13, 17, 19, 23])
    assert timers.median("test") == 13

    # Test case: timings with 0

# Generated at 2022-06-13 18:36:00.957551
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Median-Function of Timers"""
    timers = Timers()
    for i in range(1, 6):
        timers.add('test', i)
    assert timers.median('test') == 3


# Generated at 2022-06-13 18:36:13.013394
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.data = {0: 0, 1: 1}
    assert timers.mean(1) == 0.5
    assert timers.median(1) == 0.5
    assert timers.stdev(1) == 0.5
    assert timers.min(1) == 0
    assert timers.max(1) == 1
    assert timers.total(1) == 1
    assert timers.mean(0) == 0
    assert timers.median(0) == 0
    assert timers.stdev(0) == 0
    assert timers.min(0) == 0
    assert timers.max(0) == 0
    assert timers.total(0) == 0

# Generated at 2022-06-13 18:36:20.147150
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Class Timers has a mean function"""
    from copy import copy
    timers = Timers()
    timers.add('key1', 1)
    timers.add('key1', 2)
    timers.add('key2', 3)
    timers.add('key2', 4)

    for key in timers.keys():
        # tests if mean is correct
        assert timers.mean(key) == (sum(timers._timings[key])/len(timers._timings[key]))
    timer2data = copy(timers.data)
    timers.clear()
    # tests if data is cleared
    assert timers.data == {}
    # tests that _timings is also cleared
    assert timers._timings == {}
    # tests if data can be set
    timers.data.update(timer2data)
    assert timers.data

# Generated at 2022-06-13 18:36:47.029660
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for min method"""
    t = Timers(**{'name': 0})
    t.add('name', 1)
    assert t.min('name') == 1
    t.add('name', 2)
    assert t.min('name') == 1
    t.add('name', 0)
    assert t.min('name') == 0
    t.add('name2', 0)
    assert t.min('name2') == 0
    assert t.min('name_no_such') == 0


# Generated at 2022-06-13 18:36:49.157252
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("GenericMeasurements", 5.0)
    timers.add("GenericMeasurements", 10.0)
    assert timers.mean("GenericMeasurements") == 7.5

# Generated at 2022-06-13 18:36:52.695193
# Unit test for method mean of class Timers
def test_Timers_mean():
    timings = Timers()
    timings.add("all", 10)
    timings.add("all", 20)
    assert timings.mean("all") == 15


# Generated at 2022-06-13 18:36:57.274795
# Unit test for method mean of class Timers
def test_Timers_mean():
    """test_Timers_mean: Mean value of a given number of timers"""
    timers = Timers()
    timers.add("timer1", 0.3)
    timers.add("timer1", 0.5)
    timers.add("timer1", 0.7)
    timers.add("timer2", 0.2)
    timers.add("timer2", 0.8)
    assert timers.mean("timer1") == 0.5
    assert timers.mean("timer2") == 0.5

# Generated at 2022-06-13 18:37:02.050855
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median value of timings"""

    result = Timers()
    result.add('key', 10)
    result.add('key', 20)
    result.add('key', 30)
    assert result.median('key') == 20
    assert result.median('key2') == 0

# Generated at 2022-06-13 18:37:06.292654
# Unit test for method max of class Timers
def test_Timers_max():
    """Test max"""
    timers = Timers()
    assert timers.max("test") == 0
    timers.add("test", 123)
    assert timers.max("test") == 123
    timers.add("test", 456)
    assert timers.max("test") == 456


# Generated at 2022-06-13 18:37:11.743567
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('test', 1.2)
    result = timers.mean('test')
    assert result == 1.2
    assert isinstance(result, float)



# Generated at 2022-06-13 18:37:14.629091
# Unit test for method median of class Timers
def test_Timers_median():
    test = Timers()
    test.add('test', 1)
    test.add('test', 2)
    test.add('test', 3)
    assert test.median('test') == 2.0

# Generated at 2022-06-13 18:37:16.280079
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min("my_timer") == 0
    timers.add("my_timer", value=1)
    assert timers.min("my_timer") == 1

# Generated at 2022-06-13 18:37:20.865583
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("test", 1)
    timers.add("test", 2)
    timers.add("test", 3)
    assert timers.max("test") == 3
    # Cleanup
    timers.clear()