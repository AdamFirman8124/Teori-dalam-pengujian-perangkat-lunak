

# Generated at 2022-06-13 18:27:38.794512
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("iter", 0.1)
    timers.add("iter", 0.2)
    timers.add("iter", 0.2)
    assert(timers.mean("iter") == 0.15)

# Generated at 2022-06-13 18:27:45.191742
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    values = [5.5, 7.5, 6, 1, 3.5, 6]

    for value in values:
        t.add('test', value)

    assert t.median('test') == 5.5


# Generated at 2022-06-13 18:27:48.386411
# Unit test for method max of class Timers
def test_Timers_max():
    """Tests Timers.max"""
    timers = Timers()
    timers.add("test", 0.1)
    assert timers.max("test") == 0.1
    timers.add("test", 0.2)
    assert timers.max("test") == 0.2
    assert timers.max("nope") == 0


# Generated at 2022-06-13 18:27:54.971606
# Unit test for method min of class Timers
def test_Timers_min():
    import statistics
    # Create a Timers object
    timers = Timers()
    # Add items to it
    timers.add('a', 1.0)
    timers.add('a', 2.0)
    timers.add('a', 0.0)
    # Check if it works
    assert timers.min('a') == min([1.0, 2.0, 0.0])


# Generated at 2022-06-13 18:28:02.988817
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('timer1', 2.1)
    timers.add('timer1', 1.3)
    timers.add('timer2', 2.1)
    assert timers.min('timer1') == 1.3
    assert timers.min('timer2') == 2.1
    try:
        timers.min('timer3')
    except KeyError:
        pass
    else:
        raise Exception('Should raise KeyError')


# Generated at 2022-06-13 18:28:14.384536
# Unit test for method median of class Timers
def test_Timers_median():
    from fractions import Fraction
    from pstats import Stats
    from io import StringIO
    from torchbearer.metrics import Timers

# Generated at 2022-06-13 18:28:25.015040
# Unit test for method min of class Timers
def test_Timers_min():
    # Create an instance of class Timers
    timers = Timers({'A': [1, 2, 3, 4, 5], 'Z': [1, 2]})
    # Adding the value 3 to timer Z
    timers.add('Z', 3)
    # Adding the value 10 to timer A
    timers.add('A', 10)
    # Perform unit test for attribute min
    assert timers.min('A') == min([1, 2, 3, 4, 5, 10])
    assert timers.min('Z') == min([1, 2, 3])
    assert timers.min('R') == min([0])
    

# Generated at 2022-06-13 18:28:32.890483
# Unit test for method max of class Timers
def test_Timers_max():
    """Test the method max of class Timers"""
    timers = Timers()

    timers.add("test", 1)
    timers.add("test", 2)
    assert timers.max("test") == 2

    timers.add("test", 3)
    assert timers.max("test") == 3

    timers.add("test", 2)
    assert timers.max("test") == 3

    timers.add("test", 1)
    assert timers.max("test") == 3


# Generated at 2022-06-13 18:28:35.366001
# Unit test for method min of class Timers
def test_Timers_min():
    timer = Timers()
    timer.add("Test", 1.5)
    assert timer.min("Test") == 1.5

# Generated at 2022-06-13 18:28:42.321381
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median value of class Timers"""
    timers = Timers()
    for timer_name in ["kinawa", "parabola", "mokka"]:
        for timing in range(11):
            timers.add(timer_name, timing)
    assert timers.median("kinawa") == 5
    assert timers.median("parabola") == 5
    assert timers.median("mokka") == 5
    assert timers.median("not in dict") == 0

# Generated at 2022-06-13 18:28:48.378328
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("foo", 1)
    timers.add("foo", 2)
    assert timers.mean("foo") == 1.5
    assert timers.mean("bar") == 0


# Generated at 2022-06-13 18:28:52.867570
# Unit test for method min of class Timers
def test_Timers_min():
    from ..utils import Timers

    timers = Timers()
    timers.add("my timer", 5.0)
    assert timers.min("my timer") == 5.0
    timers.add("my timer", 10.0)
    assert timers.min("my timer") == 5.0



# Generated at 2022-06-13 18:29:00.357667
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test for method mean"""
    timers = Timers()
    timers.data['foo'] = 0
    assert timers.mean('foo') == 0

    # Clear data
    timers.clear()

    # Add timer
    timers.add('foo', 1)
    timers.add('foo', 2)
    timers.add('foo', 3)
    assert timers.mean('foo') == 2
    assert timers.mean('foo') == timers.total('foo') / timers.count('foo')

    # Apply timers
    timers.apply(lambda values: values, name='foo')
    timers.apply(lambda values: sum(values) / len(values), name='foo')

    # Raise error
    try:
        timers.apply(lambda values: values, name='bar')
    except KeyError:
        pass


# Generated at 2022-06-13 18:29:14.454578
# Unit test for method median of class Timers
def test_Timers_median():  # pragma: no cover
    """Unit test for method median of class Timers"""
    timers = Timers()
    timers.add('test', 1)
    assert timers.count('test') == 1
    assert timers.median('test') == 1
    assert timers.mean('test') == 1
    timers.add('test', 2)
    assert timers.count('test') == 2
    assert timers.median('test') == 1.5
    assert timers.mean('test') == 1.5
    timers.add('test', 3)
    assert timers.count('test') == 3
    assert timers.median('test') == 2
    assert timers.mean('test') == 2
    timers.add('test', 4)
    assert timers.count('test') == 4
    assert timers.median('test') == 2.5
   

# Generated at 2022-06-13 18:29:19.616482
# Unit test for method median of class Timers
def test_Timers_median():
    """median of timings with zero or one value is 0.0 or the value, respectively"""
    t = Timers()
    assert t.median("any_value") == 0.0
    t.add("any_value", 1.0)
    assert t.median("any_value") == 1.0
    t.add("any_value", 2.0)
    assert t.median("any_value") == 1.5
    t.add("any_value", 3.0)
    assert t.median("any_value") == 2.0
    t.add("any_value", 4.0)
    assert t.median("any_value") == 2.5
    t.add("any_value", 5.0)
    assert t.median("any_value") == 3.0

# Generated at 2022-06-13 18:29:25.500295
# Unit test for method max of class Timers
def test_Timers_max():
    """Test Timers() class method max()"""
    # initialize the class
    test = Timers()
    # set a time to the Timers class
    test["Timer1"] = 1
    test["Timer2"] = 2
    test["Timer3"] = 3
    # check the max() function
    assert test.max("Timer1")==1
    assert test.max("Timer2")==2
    assert test.max("Timer3")==3

# Generated at 2022-06-13 18:29:28.441985
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    assert timers.max("test") == 0
    timers.add("test", 1)
    assert timers.max("test") == 1
    timers.add("test", 2)
    assert timers.max("test") == 2

# Generated at 2022-06-13 18:29:30.769490
# Unit test for method min of class Timers
def test_Timers_min():
   timings = {"red": 1, "green": 5, "blue": 3}
   timers = Timers(timings)
   assert timers.min("green") == 5

test_Timers_min()


# Generated at 2022-06-13 18:29:39.147300
# Unit test for method max of class Timers
def test_Timers_max():
    """Test the Timers max method."""
    from pytest import raises

    timers = Timers()
    with raises(KeyError):
        timers.max("unknown")

    timers._timings["known"].append(5.5)
    assert timers.max("known") == 5.5

    timers._timings["known"].append(-1.2)
    assert timers.max("known") == 5.5

    timers._timings["known"].append(-1.2)
    assert timers.max("known") == 5.5

    timers._timings["known"].append(6.2)
    assert timers.max("known") == 6.2



# Generated at 2022-06-13 18:29:45.242161
# Unit test for method max of class Timers
def test_Timers_max():
    """
    Class Timers method max
    """
    list_of_timers = Timers()
    list_of_timers.add("test", 1)
    list_of_timers.add("test", 2)
    list_of_timers.add("test", 3)
    list_of_timers.add("test", 4)
    list_of_timers.add("test", 5)
    assert list_of_timers.max("test") == 5
    return True


# Generated at 2022-06-13 18:29:56.915764
# Unit test for method max of class Timers
def test_Timers_max():
    """Test function for method max of class Timers."""
    # Case with an empty list.
    Timers._timings['notEmpty'] = []
    assert Timers.max('notEmpty') == 0
    # Case with an existing list.
    Timers._timings['notEmpty'] = [1,2,3]
    assert Timers.max('notEmpty') == 3
    # Case with an empty list.
    Timers._timings['empty'] = []
    assert Timers.max('empty') == 0

# Generated at 2022-06-13 18:30:01.381847
# Unit test for method min of class Timers
def test_Timers_min():
    # Create timers
    timers = Timers()
    # Add first timing
    timers.add(name="test_timer", value=0.123)
    # Add second timing
    timers.add(name="test_timer", value=0.456)
    # Run test
    assert timers.min(name="test_timer") == 0.123

# Generated at 2022-06-13 18:30:05.779167
# Unit test for method mean of class Timers
def test_Timers_mean():
    """
    Test method mean of class Timers.
    """
    timers = Timers()
    timers.add("timer_1", 1)
    timers.add("timer_1", 2)
    assert timers.mean("timer_1") == 1.5


# Generated at 2022-06-13 18:30:11.327133
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers({"a": 1, "b": 2, "c": 3})
    assert timers.max("a") == 1
    assert timers.max("b") == 2
    assert timers.max("c") == 3



# Generated at 2022-06-13 18:30:13.193138
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('foo', 123)
    assert timers.max('foo') == 123

# Generated at 2022-06-13 18:30:19.791663
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("foo", 3)
    t.add("foo", 7)
    t.add("bar", 4)
    t.add("bar", 5)
    t.add("bar", 10)
    t.add("bar", 12)
    assert t.mean("foo") == 5.0
    assert t.mean("bar") == 7.0


# Generated at 2022-06-13 18:30:22.251287
# Unit test for method min of class Timers
def test_Timers_min():
    """Check that Timer objects have the method min"""
    assert "min" in dir(Timers())

# Generated at 2022-06-13 18:30:23.649236
# Unit test for method median of class Timers
def test_Timers_median():
    assert Timers().median("test") == 0.0

test_Timers_median()

# Generated at 2022-06-13 18:30:27.713047
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("mean_test", 1)
    timers.add("mean_test", 2)
    timers.add("mean_test", 3)
    assert timers.mean("mean_test") == 2


# Generated at 2022-06-13 18:30:37.040360
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers1 = Timers()
    timers1.add("timer1", 1.0)
    timers1.add("timer1", 2.0)
    timers1.add("timer1", 3.0)
    assert(timers1.mean("timer1") == 2.0)
    timers2 = Timers()
    assert(timers2.mean("timer2") == 0.0)
    assert(timers2.mean("timer3") == 0.0)
    assert(timers2.mean("timer4") == 0.0)

# Generated at 2022-06-13 18:30:50.998302
# Unit test for method median of class Timers
def test_Timers_median():
    times = Timers()
    times.add('times1', 1.)
    times.add('times1', 2.)
    times.add('times1', 3.)
    times.add('times1', 4.)
    times.add('times2', 1.)
    times.add('times2', 2.)
    times.add('times2', 3.)
    times.add('times2', 4.)
    times.add('times2', 5.)
    times.add('times2', 6.)
    times.add('times2', 7.)
    times.add('times2', 8.)
    times.add('times2', 9.)
    assert times.median("times1") == 2.5
    assert times.median("times2") == 5.

# Generated at 2022-06-13 18:30:56.098518
# Unit test for method max of class Timers
def test_Timers_max():
    # GIVEN
    times = Timers()
    times.data = {'a': 3}
    times._timings = {'a': []}
    # WHEN
    max_time = times.max('a')
    # THEN
    assert max_time == 0


# Generated at 2022-06-13 18:30:59.830619
# Unit test for method max of class Timers
def test_Timers_max():
    """Test of custom dictionary structure Timers"""
    timers = Timers()
    timers.add("a", 1)
    assert timers.max("a") == 1
    timers.add("a", 2)
    assert timers.max("a") == 2
    timers.add("a", 3)
    assert timers.max("a") == 3


# Generated at 2022-06-13 18:31:03.540514
# Unit test for method min of class Timers
def test_Timers_min():
    timer = Timers()
    timer.add("a0", 0)
    timer.add("a1", 1)
    timer.add("a2", 2)
    timer.add("a3", 3)
    assert timer.min("a3") == 3



# Generated at 2022-06-13 18:31:17.244812
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers class: method median"""

    # Initialize empty Timers object
    timers = Timers()

    # Add some values for timer 'dummy'
    dummy_values = [3, 1, 2]
    for value in dummy_values:
        timers.add('dummy', value)
    dummy_median = statistics.median(dummy_values)

    # Test that method median returns correct value
    assert timers.median('dummy') == dummy_median

    # Test that method median raises error if key is not present
    assert 'not_present' not in timers
    try:
        timers.median('not_present')
    except KeyError:
        pass
    else:
        assert False, "KeyError not raised"

# Generated at 2022-06-13 18:31:19.098921
# Unit test for method mean of class Timers
def test_Timers_mean():
    import math
    timer = Timers()
    timer.add("test", math.nan)
    assert timer.mean("test") == math.nan

# Generated at 2022-06-13 18:31:23.669066
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    timers.add("count", 1)
    timers.add("count", 3)
    assert timers.mean("count") == 2.0
    assert timers.mean("count") == 2.0
    timers.add("count", 4)
    assert timers.mean("count") == 2.6666666666666665


# Generated at 2022-06-13 18:31:32.865378
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    assert len(t) == 0
    t.add("elapsed", 0.1)
    t.add("elapsed", 0.5)
    t.add("elapsed", 0.2)
    assert len(t) == 1
    assert t.max("elapsed") == 0.5
    try:
        t.max("notadded") == 0.5
        assert False
    except KeyError:
        assert True


# Generated at 2022-06-13 18:31:37.269225
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('A', 1.234)
    timers.add('A', 0.567)
    timers.add('A', 3.456)
    timers.add('B', 9.234)
    assert timers.max('A') == 3.456
    assert timers.max('B') == 9.234

# Generated at 2022-06-13 18:31:43.478860
# Unit test for method max of class Timers
def test_Timers_max():
    """Test max() for Timers"""
    t = Timers()
    t.add('foo', 10)
    assert t.max('foo') == 10
    t.add('foo', 20)
    assert t.max('foo') == 20
    t.add('foo', 5)
    assert t.max('foo') == 20
    t.add('foo', 0)
    assert t.max('foo') == 20
    t.add('foo', -10)
    assert t.max('foo') == 20
    t.add('foo', -10)
    assert t.max('foo') == 20
    t.add('foo', 30)
    assert t.max('foo') == 30
    t.add('foo', 'a')
    assert t.max('foo') == 30



# Generated at 2022-06-13 18:32:02.482595
# Unit test for method min of class Timers
def test_Timers_min():
    """Test min() of Timers"""
    timers = Timers()
    timers.add('foo', 1.0)
    timers.add('bar', 2.0)
    timers.add('baz', 3.0)
    timers.add('foo', 4.0)
    assert timers.min('foo') == 1.0
    assert timers.min('bar') == 2.0
    assert timers.min('baz') == 3.0
    assert timers.min('qux') == 0.0


# Generated at 2022-06-13 18:32:07.824628
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("some_timer", 2.0)
    timers.add("some_timer", 3.0)
    print("Accessing mean...")
    print(timers.mean("some_timer"))


# Generated at 2022-06-13 18:32:14.091911
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the function mean of class Timers"""

    # Create test list
    test_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # Create test object
    timers = Timers()

    # Add test list
    for i, value in enumerate(test_list):
        timers.add(str(i), value)

    # Check mean of test list
    if timers.mean('0') != 0:
        raise AssertionError('Test failed')


# Generated at 2022-06-13 18:32:18.197571
# Unit test for method median of class Timers
def test_Timers_median():
    # Arrange
    timer = Timers()
    name = "test_name"
    value = [0.5, 1, 0.1, 1]

    # Act
    timer.add(name, value)

    # Assert
    assert timer.median(name) == 0.5

# Generated at 2022-06-13 18:32:26.118877
# Unit test for method median of class Timers
def test_Timers_median():
    import pytest
    from .context import context
    T = Timers()
    with context("test_Timers_median_Success", T=T):
        T.add("test", 20)
        T.add("test", 12)
        T.add("test", 14)
        T.add("test", 11)
        assert T.count("test") == 4
        assert T.median("test") == 13.5
        assert T.median("test") == T.apply(lambda values: statistics.median(values or [0]), name="test")
    with context("test_Timers_median_Failure", T=T):
        with pytest.raises(KeyError):
            T.median("test_failure")

# Generated at 2022-06-13 18:32:28.775124
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test: Timers.min"""
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    timers.add('test', 4)
    assert timers.min('test') == 1


# Generated at 2022-06-13 18:32:31.427456
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    assert timers.median('A') == 0
    timers.add('A', 0.01)
    timers.add('A', 0.02)
    timers.add('A', 0.03)
    timers.add('A', 0.04)
    assert timers.median('A') == 0.02


# Generated at 2022-06-13 18:32:34.769645
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add("foo", 1)
    t.add("foo", 5)
    assert t.median("foo") == 3.0

# Generated at 2022-06-13 18:32:40.042833
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median method for Timers class"""
    timers = Timers()
    timers.add("foo", 1.0)
    timers.add("foo", 2.0)
    timers.add("foo", 3.0)
    assert timers.median("foo") == 2

    timers.add("foo", 4.0)
    assert timers.median("foo") == 2.5


# Generated at 2022-06-13 18:32:48.632662
# Unit test for method mean of class Timers
def test_Timers_mean():
    test_instance = Timers()
    test_instance._timings = {"a": [2.2, 3.3, 4.4], "b": [2.2, 3.3, 4.4, 5.5]}
    assert test_instance.mean("a") == 3.3
    assert test_instance.mean("b") == 3.85
    assert test_instance.count("b") == 4
    assert test_instance.min("b") == 2.2
    assert test_instance.max("b") == 5.5
    assert test_instance.total("b") == 16.4
    assert test_instance.stdev("b") == 1.052363469758661
    assert test_instance.median("b") == 3.3

# Generated at 2022-06-13 18:33:14.462845
# Unit test for method max of class Timers
def test_Timers_max():
    """Test max method"""
    timers = Timers()
    timers.add('test_timer1', 1)
    timers.add('test_timer2', 3)
    timers.add('test_timer1', 2)
    timers.add('test_timer1', 1)
    timers.add('test_timer2', 1)
    timers.add('test_timer2', 9)
    assert timers.max('test_timer1') == 2
    assert timers.max('test_timer2') == 9

# Generated at 2022-06-13 18:33:22.195141
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('a', 1)
    timers.add('a', 2)
    timers.add('a', 3)
    timers.add('b', 1)
    timers.add('b', 3)
    timers.add('b', 5)

    assert timers.min('a') == 1
    assert timers.min('b') == 1


# Generated at 2022-06-13 18:33:25.517642
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    assert timers.max("foo") == 0
    timers.data["foo"] = 1.23
    assert timers.max("foo") == 1.23

# Generated at 2022-06-13 18:33:31.821613
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("some_timer", 1.0)
    t.add("some_timer", 2.0)
    t.add("some_timer", 3.0)
    assert t.mean("some_timer") == 2.0
    assert t.mean("some_timer") == t.data["some_timer"] / t.count("some_timer")

# Generated at 2022-06-13 18:33:35.526745
# Unit test for method min of class Timers
def test_Timers_min():
    """Tests the Timers class method min"""
    timers = Timers()
    timers.add('timer', 0.1)
    timers.add('timer', 0.2)
    assert timers.min('timer') == 0.1



# Generated at 2022-06-13 18:33:39.143333
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('test', 5)
    timers.add('test', 10)
    timers.add('test', 15)
    timers.add('test', 20)
    assert timers.median('test') == 12.5
    assert timers.median('test_nonexistent') == 0

# Generated at 2022-06-13 18:33:41.995277
# Unit test for method mean of class Timers
def test_Timers_mean():
    tm = Timers()
    tm._timings = {"a": [0, 2]}
    assert tm.mean("a") == 1

# Generated at 2022-06-13 18:33:44.376265
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    for i in range(1, 5):
        timers.add('test', i)
    assert timers.min('test') == 1


# Generated at 2022-06-13 18:33:48.651281
# Unit test for method max of class Timers
def test_Timers_max():
    # Setup
    timers = Timers()
    timers.add(name='a', value=1.0)
    timers.add(name='a', value=2.0)
    timers.add(name='a', value=3.0)
    # Test
    assert timers.max(name='a') == 3.0
    assert timers.max(name='b') == 0.0


# Generated at 2022-06-13 18:33:52.994581
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("mio", 5)
    timers.add("mio", 2.5)
    timers.add("mio", 4)
    timers.add("mio", 2.5)
    timers.add("mio", 3)
    
    return timers.median("mio") - 2.5 < 1e-8


# Generated at 2022-06-13 18:34:33.504410
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('some timer', 5.0)
    assert timers.min('some timer') == 5.0
    timers.add('some timer', 7.0)
    assert timers.min('some timer') == 5.0



# Generated at 2022-06-13 18:34:37.092550
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()
    timers.add('timer1', 0.001)
    timers.add('timer1', 0.002)
    assert timers['timer1'] == 0.003
    assert timers.median('timer1') == 0.001

# Generated at 2022-06-13 18:34:43.814386
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t._timings = {'name': [1,2,3,4]}
    t.data = {}
    for i in range(5):
        t._timings['new'].append(i)
    assert t.count('name') == 4
    assert t.count('none') == 0
    assert t.total('name') == 10
    assert t.total('none') == 0
    assert t.min('name') == 1
    assert t.min('none') == 0
    assert t.max('name') == 4
    assert t.max('none') == 0
    assert t.mean('name') == 2.5
    assert t.mean('none') == 0
    assert t.median('name') == 2.5
    assert t.median('none') == 0

# Generated at 2022-06-13 18:34:46.973490
# Unit test for method min of class Timers
def test_Timers_min():
    assert Timers({'min' : [1,2,3]}).min('min') == 1


# Generated at 2022-06-13 18:34:52.937349
# Unit test for method max of class Timers
def test_Timers_max():
    """Test Timers.max"""
    timers = Timers()
    assert timers.max("abc") == 0
    timers.add("abc", 1)
    timers.add("def", 2)
    timers.add("abc", 3)
    assert timers.max("abc") == 3
    assert timers.max("def") == 2
    assert timers.max("ghi") == 0
    timers.add("ghi", 4)
    assert timers.max("ghi") == 4

# Generated at 2022-06-13 18:34:55.975839
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add('foo', 1)
    t.add('foo', 2)
    t.add('bar', 3)
    assert t.max('foo') == 2
    assert t.max('bar') == 3

# Generated at 2022-06-13 18:35:01.223874
# Unit test for method mean of class Timers
def test_Timers_mean():
    # Create Timers object
    timers = Timers()
    # Add test data
    timers.add('test_timer_1', 3)
    # Test mean function
    assert timers.mean('test_timer_1') == 3


# Generated at 2022-06-13 18:35:11.455541
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add('test_1', 10)
    t.add('test_1', 20)
    t.add('test_1', 30)
    t.add('test_2', 40)
    t.add('test_2', 50)
    t.add('test_2', 60)
    assert t.median('test_1') == 20
    assert t.median('test_2') == 50
    t.add('test_2', 40)
    assert t.median('test_2') == 45
    assert t.median('test_3') is None
    assert t.median('test_1') == 20
    assert t.median('test_2') == 45


# Generated at 2022-06-13 18:35:15.084740
# Unit test for method median of class Timers
def test_Timers_median():
    """Test that median of empty list evaluates to 0"""
    t = Timers()
    t._timings = {'test': []}
    assert t.median(name="test") == 0

# Generated at 2022-06-13 18:35:22.890664
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    assert Timers().median("") == 0.0
    assert Timers({"", 0}).median("") == 0.0
    assert Timers({"", 1}).median("") == 1.0
    assert Timers({"", 1, 2}).median("") == 1.5
    assert Timers({"", 1, 2, 3}).median("") == 2.0

# Generated at 2022-06-13 18:36:45.375103
# Unit test for method min of class Timers
def test_Timers_min():
    timer_object = Timers()
    timer_object.add("test", 1)
    timer_object.add("test", 3)
    timer_object.add("test", 5)
    assert timer_object.min("test") == 1

# Generated at 2022-06-13 18:36:53.469933
# Unit test for method min of class Timers
def test_Timers_min():
    data = Timers()
    data["first_timer"] = Timers()
    data["first_timer"].add("test", 100)
    data["first_timer"].add("test", 20)
    data["first_timer"].add("test", 300)
    data["first_timer"].add("test", 40)
    data["first_timer"].add("test", 500)
    data["second_timer"] = Timers()
    data["second_timer"].add("test", 44)
    data["second_timer"].add("test", 13)
    data["second_timer"].add("test", 66)
    data["second_timer"].add("test", 77)
    data["second_timer"].add("test", 55)
    assert data["first_timer"].min("test") == 20

# Generated at 2022-06-13 18:36:57.137673
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 1)
    assert timers.max('test') == 1
    timers.add('test', 2)
    assert timers.max('test') == 2
    assert timers.min('test') == 1
    timers.add('test', 2)
    assert timers.count('test') == 4
    assert timers.mean('test') == 1.5
    assert timers.median('test') == 1.5
    assert timers.total('test') == 6
    assert timers.stdev('test') == 0.5

# Generated at 2022-06-13 18:37:01.112016
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()
    timers.add("test", 4.8)
    timers.add("test", 2.0)
    assert timers.median("test") == 3.4

# Generated at 2022-06-13 18:37:04.610571
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('CPU_time', 22.3)
    timers.add('CPU_time', 24.3)
    assert timers.mean('CPU_time') == 23.3

# Generated at 2022-06-13 18:37:06.904141
# Unit test for method mean of class Timers
def test_Timers_mean():
    stats = Timers()
    stats.add("test", 1)
    stats.add("test", 2)
    stats.add("test", 3)
    assert stats.mean("test") == 2



# Generated at 2022-06-13 18:37:13.431122
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    # Add values
    timers.add("timer1", 0.1)
    timers.add("timer1", 0.2)
    timers.add("timer1", 0.3)
    # Check minimum value
    assert timers.min("timer1") == 0.1


# Generated at 2022-06-13 18:37:21.692935
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add("test", 3)
    t.add("test", 5)
    t.add("test", 6)
    assert t.median("test") == 5

    t = Timers()
    t.add("test", 3)
    t.add("test", 5)
    t.add("test", 7)
    assert t.median("test") == 5


# Generated at 2022-06-13 18:37:27.777253
# Unit test for method max of class Timers
def test_Timers_max():
    from pytest import approx

    t = Timers()
    t.add("test", 1)
    t.add("test", 2)
    t.add("test", 3)
    t.add("test", 4)
    assert t.max("test") == approx(4)

# Generated at 2022-06-13 18:37:35.796219
# Unit test for method mean of class Timers
def test_Timers_mean():
    myTimers = Timers()
    assert myTimers.mean("test") == 0.0

    myTimers.add("test", 0)
    assert myTimers.mean("test") == 0.0

    myTimers.add("test", 1)
    assert myTimers.mean("test") == 0.5
