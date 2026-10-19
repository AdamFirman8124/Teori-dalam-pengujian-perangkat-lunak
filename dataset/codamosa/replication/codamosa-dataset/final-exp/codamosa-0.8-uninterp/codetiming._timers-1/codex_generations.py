

# Generated at 2022-06-13 18:27:45.780824
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    assert timers.min('test') == 1
    assert timers.min('test2') == 0


# Generated at 2022-06-13 18:27:53.544362
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add(name = "test", value = 1)
    t.add(name = "test", value = 2)
    t.add(name = "test", value = 3)
    t.add(name = "test", value = 4)
    assert t.median(name = "test") == 2.5


# Generated at 2022-06-13 18:27:57.414767
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("a", 1)
    t.add("a", 2)
    assert t.mean("a") == 1.5


# Generated at 2022-06-13 18:28:05.339729
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test that 'Timers.mean' returns the correct result"""
    timers = Timers()
    timers.add('foo', 1.0)
    timers.add('foo', 2.0)
    timers.add('bar', 3.0)
    timers.add('bar', 4.0)
    assert timers.mean('foo') == 1.5
    assert timers.mean('bar') == 3.5

# Generated at 2022-06-13 18:28:09.114429
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the mean method."""
    # Pass
    data = Timers()
    data.add('foo', 1)
    data.add('foo', 2)
    data.add('foo', 3)
    assert data.mean('foo') == 2
    # Fail
    try:
        data.mean('bar')
        assert False
    except KeyError:
        assert True

# Generated at 2022-06-13 18:28:13.053405
# Unit test for method median of class Timers
def test_Timers_median():
    """Test method median of user class Timers"""
    # Timers is used in class Context but this code is superfluous in this case
    from context import Context  # pragma: no cover
    context = Context(__name__)

    context.timers.median("test_timer_1")

# Generated at 2022-06-13 18:28:17.391394
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the method median of class Timers"""
    timer = Timers()
    timer.add('fps', 50)
    timer.add('fps', 10)
    assert timer.median('fps') == 30

# Generated at 2022-06-13 18:28:21.209004
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers._timings['name'] = [1, 2, 3]
    assert timers.mean('name') == 2.



# Generated at 2022-06-13 18:28:29.066492
# Unit test for method max of class Timers
def test_Timers_max():  # pragma: nocover
    """Verify that method Timers.max() works properly"""
    timers = Timers()
    timers.add("A", 1.0)
    timers.add("A", 2.0)
    timers.add("A", 3.0)
    assert timers.max("A") == 3.0

    timers.add("B", 1.0)
    timers.add("B", 2.0)
    timers.add("B", 3.0)
    assert timers.max("B") == 3.0

    assert timers.max("C") == 0.0



# Generated at 2022-06-13 18:28:36.473518
# Unit test for method median of class Timers
def test_Timers_median():
    """Check that method Timers.median() gives the correct result"""
    timer = Timers()
    timer.add('foo', 2)
    timer.add('foo', 3.5)
    timer.add('foo', 4)
    timer.add('foo', 3)
    timer.add('foo', 4)
    timer.add('foo', 3.5)
    assert timer.median('foo') == 3.5
    assert timer.median('foo') == timer.median('bar')

# Generated at 2022-06-13 18:28:42.106026
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("test", 1.0)
    assert timers.max("test") == 1.0
    timers.add("test", 2.0)
    assert timers.max("test") == 2.0


# Generated at 2022-06-13 18:28:48.272696
# Unit test for method median of class Timers
def test_Timers_median():
    timer = Timers()
    timer.add('test', 1.0)
    timer.add('test', 2.0)
    timer.add('test', 3.0)
    assert timer.median('test') == 2.0

# Generated at 2022-06-13 18:28:56.299974
# Unit test for method median of class Timers
def test_Timers_median():

    # Setup
    t1 = Timers()
    t2 = Timers()

    t1.add("a", 0.1)
    t1.add("a", 0.2)
    t1.add("a", 0.3)

    t2.add("b", 0.2)
    t2.add("b", 0.3)
    t2.add("b", 0.4)

    # Run
    m1 = t1.median("a")
    m2 = t2.median("b")

    # Test
    assert m1 == 0.2
    assert m2 == 0.3

# Generated at 2022-06-13 18:29:00.665386
# Unit test for method min of class Timers
def test_Timers_min():
    """Test the minimum timing value"""
    # Create a Timers instance
    timers = Timers()
    # Add a timing value
    name = 'min_test'
    value = 0.1234
    timers.add(name, value)
    # Check minimum timing value
    assert timers.min(name) == value


# Generated at 2022-06-13 18:29:05.883400
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()
    timers.add('timer_1', 42)
    timers.add('timer_1', 8)
    assert timers.median('timer_1') == 25


# Generated at 2022-06-13 18:29:10.529927
# Unit test for method min of class Timers
def test_Timers_min():
    """
    Test method min of class Timers
    """
    # Test case 1
    timers = Timers()
    timers.add('example', 1.5)
    timers.add('example', 1.5)

    assert timers.min('example') == 1.5



# Generated at 2022-06-13 18:29:20.631178
# Unit test for method mean of class Timers
def test_Timers_mean():

    # First, test Timers on an empty list, which should return 0
    timers = Timers('timers')
    
    assert timers.mean('mean') == 0

    # Second, test Timers on a list of three random numbers, which should return the mean
    timers = Timers('timers')
    timers.add('mean', 5)
    timers.add('mean', 7)
    timers.add('mean', 9)

    assert timers.mean('mean') == 7

    # Third, test Timers on a list with one random number, which should return the number
    timers = Timers('timers')
    timers.add('mean', 5)

    assert timers.mean('mean') == 5

# Generated at 2022-06-13 18:29:23.872078
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("timer1", 1.0)
    timers.add("timer2", 2.0)
    timers.add("timer2", 3.0)
    assert timers.median("timer1") == 1.0
    assert timers.median("timer2") == 2.5
    assert timers.median("timer3") == 0.0

# Generated at 2022-06-13 18:29:25.903133
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers._timings['test'] = [1, 2, 3]
    assert timers.median('test') == 2.0

# Generated at 2022-06-13 18:29:37.980701
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    func = lambda value: value

    # Empty list
    assert Timers().min(name="empty") == 0

    # One item
    assert Timers().min(name="one") == 0
    assert Timers().add(name="one", value=1.0) == None
    assert Timers().min(name="one") == 1.0

    # Two items
    assert Timers().min(name="one") == 0
    assert Timers().add(name="one", value=1.0) == None
    assert Timers().add(name="one", value=1.0) == None
    assert Timers().min(name="one") == 1.0

    # Three items
    assert Timers().min(name="three") == 0

# Generated at 2022-06-13 18:29:46.721686
# Unit test for method max of class Timers
def test_Timers_max():
    def test_method_Timers_max():
        T = Timers()
        T.add('a', 4)
        T.add('b', 1)
        T.add('b', 3)
        T.add('c', 'value')
        assert T.max('a') == 4
        assert T.max('b') == 3
        assert T.max('c') == 0
        try:
            T.max('d')
        except KeyError as e:
            print(e)
        assert T.max('d') == 0
    test_method_Timers_max()



# Generated at 2022-06-13 18:29:51.166343
# Unit test for method min of class Timers
def test_Timers_min():
    import pytest
    t = Timers()
    t.add("timer_name", 1)
    assert t.min("timer_name") == 1
    with pytest.raises(KeyError):
        t.min("another_timer_name")

# Generated at 2022-06-13 18:30:02.364298
# Unit test for method max of class Timers
def test_Timers_max():
    from pickle import dump, load

    # Create test instance of this class
    test = Timers()
    test.add('test.A', 0)
    test.add('test.A', 1)
    test.add('test.A', 2)
    test.add('test.B', 3)
    test.add('test.B', 4)
    test.add('test.B', 5)

    # Ensure max value is correctly computed
    assert test.max('test.A') == 2
    assert test.max('test.B') == 5
    assert test.max('test.C') == 0

    # Ensure valid serialized format
    assert repr(test) == repr(eval(repr(test)))

    # Ensure valid pickled format
    assert test == load(dump(test))

    # Attempt to set value

# Generated at 2022-06-13 18:30:06.148482
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the mean method"""
    timers = Timers()
    timers.add("A", 2)
    timers.add("A", 3)
    assert timers.mean("A") == 2.5
    assert timers.mean("B") == 0

# Generated at 2022-06-13 18:30:13.440484
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test for method mean in class Timers"""
    # Set up a timers object
    timers = Timers()
    # Add two timings
    timers.add('foo', 20.0)
    timers.add('foo', 22.0)
    # Call method mean
    mean_ = timers.mean('foo')
    # Assert that method mean returns correct value
    assert mean_ == 21.0


# Generated at 2022-06-13 18:30:19.162215
# Unit test for method max of class Timers
def test_Timers_max():
    """Test that a timer can be added"""
    timers = Timers()
    timers.add("BASE", 2.0)
    timers.add("BASE", 3.0)
    timers.add("DERIVED", 6.0)
    assert timers.max("BASE") == 3.0
    assert timers.max("DERIVED") == 6.0

# Generated at 2022-06-13 18:30:22.824666
# Unit test for method median of class Timers
def test_Timers_median():
    """
    This unit test is to check whether the median of all timings is correct.
    If a proper median is returned, the test will pass.
    """
    t = Timers()
    t.add("test", 1)
    t.add("test", 2)
    t.add("test", 3)
    assert t.median("test") == 2

# Generated at 2022-06-13 18:30:28.402955
# Unit test for method max of class Timers
def test_Timers_max():
    """Test function for method max of class Timers"""
    timers = Timers()
    timers["timer1"] = 1
    timers.add("timer2", 2)
    timers.add("timer3", 2)
    timers.add("timer3", 3)
    assert timers.min("timer1") == 1
    assert timers.max("timer2") == 2
    assert timers.max("timer3") == 3
    assert timers.max("timerx") == 0
    assert timers.max(100) == 0
    assert timers.mean("timer1") == 1
    assert timers.mean("timer2") == 2
    assert timers.mean("timer3") == 2.5
    assert math.isnan(timers.mean("timerx"))
    assert math.isnan(timers.mean(100))

# Generated at 2022-06-13 18:30:34.967499
# Unit test for method max of class Timers
def test_Timers_max():
    msg = "Method .max() works fine."
    times = Timers()
    times.add("A", 10)
    times.add("A", 20)
    times.add("A", 30)
    times.add("A", 40)
    assert times.max("A") == 40, msg
    assert times.max("B") == 0, msg


# Generated at 2022-06-13 18:30:43.288456
# Unit test for method median of class Timers
def test_Timers_median():
    """
    Test for the median method of the Timers class.

    The test data consists of a list of lists of test data and the expected
    result for each of those lists.
    """

# Generated at 2022-06-13 18:30:50.050920
# Unit test for method min of class Timers
def test_Timers_min():
    """
    Test that Timers.min recovers the minimum value of a timer
    """
    timers = Timers()
    timers.add("a", 1)
    timers.add("a", 4)
    assert timers.min("a") == 1



# Generated at 2022-06-13 18:30:56.382002
# Unit test for method median of class Timers
def test_Timers_median():
    timers: Timers = Timers()
    for i in range(2):
        for j in range(5):
            timers.add(str(i), j)

    assert timers.median('0') == 2
    assert timers.median('1') == 2
    assert timers.median('2') == 0

test_Timers_median()

# Generated at 2022-06-13 18:30:58.466514
# Unit test for method max of class Timers
def test_Timers_max():
    """Timers.max() should return zero when timer is empty"""
    timers = Timers()
    assert timers.max('name') == 0.0

# Generated at 2022-06-13 18:31:00.504842
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()

    for number in range(10):
        timers.add('foo', number)

    assert timers.mean('foo') == 4.5

# Generated at 2022-06-13 18:31:03.819627
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("name", 10)
    timers.add("name", 15)
    timers.add("name", 15)
    timers.add("name", 20)
    assert 15 == timers.median("name")

# Generated at 2022-06-13 18:31:06.388006
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()

    t.add('a', 1)
    assert 1 == t.max('a'), '1 == t.max("a")'
    assert 0 == t.max('b'), '0 == t.max("b")'

# Generated at 2022-06-13 18:31:11.362466
# Unit test for method median of class Timers
def test_Timers_median():

    from pyprobml_utils import assert_allclose

    x = Timers()
    x.add("a", 1)
    x.add("a", 2)
    x.add("a", 3)
    assert_allclose(x.median("a"), 2)
    x.add("a", 4)
    assert_allclose(x.median("a"), 2.5)
    x.add("a", 5)
    assert_allclose(x.median("a"), 3)



# Generated at 2022-06-13 18:31:13.095847
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("test_min_func", 1)
    assert timers.min("test_min_func") == 1


# Generated at 2022-06-13 18:31:16.616723
# Unit test for method max of class Timers
def test_Timers_max():
    # Set up context
    timers = Timers()

    # Set up parameters
    name = 'alpha'

    # Execute the code to be tested
    result = timers.max(name)

    # Verify the result
    assert result == 0


# Generated at 2022-06-13 18:31:25.845943
# Unit test for method max of class Timers
def test_Timers_max():
    # Create an instance of the Timers class
    t = Timers()
    # Add a value to 
    t.add('timing1',5)
    # Add a value to the timing 'timing1'
    t.add('timing1',10)
    # Add a value to the timing 'timing1'
    t.add('timing1',15)
    # Add a value to the timing 'timing2'
    t.add('timing2',20)
    # Add a value to the timing 'timing2'
    t.add('timing2',25)
    # Add a value to the timing 'timing2'
    t.add('timing2',30)
    
    # Creating a variable that stores the max of the timing 'timing1'

# Generated at 2022-06-13 18:31:33.743125
# Unit test for method mean of class Timers
def test_Timers_mean():
    class TimersStub:
        def __init__(self):
            pass
        def apply(self, func, name):
            return func([10.0, 20.0])
    timers_stub = TimersStub()
    # mean
    assert(timers_stub.mean == 15.0)

# Generated at 2022-06-13 18:31:42.488753
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    # empty timers
    assert timers.max("timer_name") == 0
    # default timers
    timers.data["timer_name"] = 0.0
    assert timers.max("timer_name") == 0
    timers.data["timer_name"] = 1.0
    assert timers.max("timer_name") == 1
    timers.data["timer_name"] = -1.0
    assert timers.max("timer_name") == -1
    # add timers
    timers._timings["timer_name"] = [1.0, 2.0, 3.0]
    assert timers.max("timer_name") == 3
    # add empty list of timers
    timers._timings["timer_name"] = []
    assert timers.max("timer_name") == 0

# Generated at 2022-06-13 18:31:48.356603
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('test', 1.1)
    timers.add('test', 5.2)
    timers.add('test', 3.4)
    assert(timers.min('test') == 1.1)


# Generated at 2022-06-13 18:31:56.211860
# Unit test for method median of class Timers
def test_Timers_median():
    # Create a Timers object
    t = Timers()
    # Add a number of values to timer 'testTimer'
    t.add('testTimer', 1.7)
    t.add('testTimer', 0)
    t.add('testTimer', 2)
    t.add('testTimer', 2.5)
    # Check the median value of 'testTimer'
    assert t.median('testTimer') == 1.75

# Generated at 2022-06-13 18:31:59.521779
# Unit test for method max of class Timers
def test_Timers_max():
    assert Timers({"a": 1.1}).max("a") == 1.1
    assert Timers().max("a") == 0


# Generated at 2022-06-13 18:32:04.578139
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min("name") == 0
    timers.add("name", 2)
    assert timers.min("name") == 2
    timers.add("name", 3)
    assert timers.min("name") == 2
    timers.add("name", 1)
    assert timers.min("name") == 1
    assert timers.min("nonexistent") == 0


# Generated at 2022-06-13 18:32:12.102686
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("timings", 0.5)
    assert timers.min("timings") == 0.5
    timers.add("timings", 0.2)
    assert timers.min("timings") == 0.2
    timers.add("timings", 1)
    assert timers.min("timings") == 0.2
    timers.add("timings2", 0)
    timers.add("timings2", 0.5)
    assert timers.min("timings2") == 0

# Generated at 2022-06-13 18:32:14.523891
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add("test", 1)
    assert t.min("test") == 1


# Generated at 2022-06-13 18:32:18.611178
# Unit test for method max of class Timers
def test_Timers_max():
    """Test method max of class Timers"""
    timers = Timers()
    timers.add('T0', 1)
    timers.add('T0', 2)
    timers.add('T0', 3)
    assert timers.max('T0') == 3


# Generated at 2022-06-13 18:32:25.266431
# Unit test for method max of class Timers
def test_Timers_max():

    timers = Timers()
    timers.data = {'a': 1, 'b': 3, 'c': 2}
    assert timers.max('a') == 1
    assert timers.max('b') == 3
    assert timers.max('c') == 2

    timers.add('c', 5)
    assert timers.max('c') == 5
    assert timers.max('a') == 1

    timers.clear()
    assert timers.max('a') == 0
    assert timers.max('b') == 0
    assert timers.max('c') == 0
    
    return True



# Generated at 2022-06-13 18:32:31.705724
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('timer1', 1)
    timers.add('timer1', 2)
    timers.add('timer2', 3)
    assert timers.min('timer1') == 1
    # if key not present, method returns 0
    assert timers.min('timer3') == 0


# Generated at 2022-06-13 18:32:35.053480
# Unit test for method max of class Timers
def test_Timers_max():
    timings = Timers()
    timings.add("test", 1.0)
    timings.add("test", 2.0)
    assert timings.max("test") == 2.0



# Generated at 2022-06-13 18:32:42.041176
# Unit test for method median of class Timers
def test_Timers_median():  # pragma: no cover
    """Test the median function"""
    timers = Timers({'t1': 2, 't2': 5, 't3': 7})
    assert timers.median('t1') == 2
    assert timers.median('t2') == 5
    assert timers.median('t3') == 7
    timers.add('t1', 3)
    assert timers.median('t1') == 2.5
    timers.add('t1', -1)
    assert timers.median('t1') == 2
    timers.add('t1', 4)
    assert timers.median('t1') == 3

# Generated at 2022-06-13 18:32:54.256404
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test method mean of Timers"""

# Generated at 2022-06-13 18:33:00.342138
# Unit test for method min of class Timers
def test_Timers_min():
    # Arrange
    timer = Timers()
    name = "min"

    # Act
    timer.add(name, 1)
    timer.add(name, 2)
    timer.add(name, 3)

    # Assert
    assert timer.min(name) == 1


# Generated at 2022-06-13 18:33:03.540938
# Unit test for method max of class Timers
def test_Timers_max():
    """
    Test the max function with no values
    >>> timers = Timers()
    >>> timers.max('test')
    0.0
    """
    pass



# Generated at 2022-06-13 18:33:07.404087
# Unit test for method min of class Timers
def test_Timers_min():
    assert Timers({"x": 1, "y": 2}).min(name="x") == 0, ""


# Generated at 2022-06-13 18:33:12.391902
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("test", 1.0)
    assert timers.mean("test") == 1.0
    timers.add("test", 1.0)
    assert timers.mean("test") == 1.0
    timers.add("test", 2.0)
    assert timers.mean("test") == 1.33

# Generated at 2022-06-13 18:33:15.026394
# Unit test for method mean of class Timers
def test_Timers_mean():
    assert Timers({'A': 10, 'B': 20}).mean(name='B') == 20
    assert Timers({'A': 10, 'B': 20}).mean(name='A') == 10

# Generated at 2022-06-13 18:33:22.294743
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median of Timers object"""
    test_timers = Timers()
    test_timers.add('test_time', 1.0)
    test_timers.add('test_time', 2.0)
    test_timers.add('test_time', 3.0)
    assert test_timers.median('test_time') == 2.0

# Generated at 2022-06-13 18:33:28.796031
# Unit test for method max of class Timers
def test_Timers_max():
    timer = Timers()
    timer.add("timer1", 0.5)
    timer.add("timer1", 0.3)
    timer.add("timer2", 1)
    assert timer.max("timer1") == 0.5
    assert timer.max("timer2") == 1

# Generated at 2022-06-13 18:33:31.238230
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("mean", 10.0)
    assert t.mean("mean") == 10.0


# Generated at 2022-06-13 18:33:36.115450
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("test", 1.1)
    timers.add("test", 2.1)
    timers.add("test", 3.1)
    timers.add("test", 4.1)
    timers.add("test", 5.1)
    assert timers.median("test") == 3.1



# Generated at 2022-06-13 18:33:38.631497
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 3)
    assert timers.max('test') == 3

# Generated at 2022-06-13 18:33:41.900840
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    assert t.max('test') == 0
    t.add('test', 1)
    assert t.max('test') == 1



# Generated at 2022-06-13 18:33:49.845555
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the median method of class Timers"""
    # Define data

# Generated at 2022-06-13 18:33:58.700988
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the Timers's method median."""
    assert Timers().median("abc") == 0.0
    assert Timers(abc=3.0).median("abc") == 3.0
    assert Timers(abc=[3.0]).median("abc") == 3.0
    assert Timers(abc=[2.0, 6.0]).median("abc") == 4.0
    assert Timers(abc=[2.0, 6.0, 4.0]).median("abc") == 4.0

# Generated at 2022-06-13 18:34:07.971446
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers._timings = {
        'timer1': [2, 3, 4],
        'timer2': [],
        'timer3': [0, 5]
    }
    timers.data = {
        'timer1': 9,
        'timer2': 0,
        'timer3': 5
    }
    assert timers.mean('timer1') == 3
    assert timers.mean('timer2') == 0
    assert timers.mean('timer3') == 2.5


# Generated at 2022-06-13 18:34:12.146346
# Unit test for method max of class Timers
def test_Timers_max():
    import random
    import pytest
    
    t = Timers()
    t.add("max", random.random())
    t.add("max", random.random())
    t.add("max", random.random())

    assert t.max("max") == 0.0

    with pytest.raises(KeyError):
        t.max("other")



# Generated at 2022-06-13 18:34:21.506020
# Unit test for method mean of class Timers
def test_Timers_mean():
    import sys
    import random
    sys.tracebacklimit = 0

    # Create a timings object
    timings = Timers()

    # Add times for a bunch of iterations
    for i in range(1, 100):
        timings.add(
            name='mytest',
            value=random.randint(1, 10),
        )

    # Calculate mean
    mean = timings.mean('mytest')

    # Assert
    assert isinstance(mean, float)


# Generated at 2022-06-13 18:34:27.111329
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Return mean value of timings"""
    timers = Timers()
    timers.add("example", 0.1)
    timers.add("example", 0.2)
    timers.add("example", 0.3)
    mean = timers.mean("example")
    assert mean == 0.2

# Generated at 2022-06-13 18:34:30.263241
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('test', 10)
    timers.add('test', 20)
    timers.add('test', 30)
    assert timers.mean('test') == 20

# Generated at 2022-06-13 18:34:36.137734
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    assert timers.max("some_timer") == 0.0
    timers.add("some_timer", 0.5)
    assert timers.max("some_timer") == 0.5
    timers.add("some_timer", 1.0)
    assert timers.max("some_timer") == 1.0
    timers.add("other_timer", 0.5)
    assert timers.max("other_timer") == 0.5

# Generated at 2022-06-13 18:34:41.779671
# Unit test for method median of class Timers
def test_Timers_median():
    # prepare
    timers = Timers()
    timers._timings = {
        "key1": [1, 2, 3],
        "key2": [1, 2, 3, 4],
        "key3": [1, 2],
        "key4": [1],
    }

    # test
    assert timers.median("key1") == 2
    assert timers.median("key2") == 2.5
    assert timers.median("key3") == 1.5
    assert timers.median("key4") == 1
    assert timers.median("key5") == 0

    # cleanup - none

# Generated at 2022-06-13 18:34:46.432058
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    min_values = timers.min('test')
    assert min_values == 1

# Generated at 2022-06-13 18:34:52.333774
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    timers = Timers()
    assert timers.min("") == 0
    timers.add("", 1)
    assert timers.min("") == 1
    timers.add("", 2)
    assert timers.min("") == 1
    timers.add("", 2)
    assert timers.min("") == 1
    timers.add("", 3)
    assert timers.min("") == 1


# Generated at 2022-06-13 18:34:57.021902
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Function for unit testing the mean method of class Timers"""
    timer = Timers()
    timer.add("timer1", 2)
    timer.add("timer1", 3)
    timer.add("timer1", 4)
    timer.add("timer2", 2)
    timer.add("timer2", 4)
    timer.add("timer2", 6)
    assert timer.mean("timer1") == 3 and timer.mean("timer2") == 4

# Generated at 2022-06-13 18:35:02.895441
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    timers.add('timer1', 0.1)
    timers.add('timer1', 0.2)
    assert timers.max('timer1') == 0.2


# Generated at 2022-06-13 18:35:06.373813
# Unit test for method min of class Timers
def test_Timers_min():
    from unittest import TestCase
    t = Timers()
    assert t.min("time") == 0
    t.add("time", 3.0)
    assert t.min("time") == 3.0
    t.clear()
    assert t.min("time") == 0


# Generated at 2022-06-13 18:35:10.537676
# Unit test for method mean of class Timers
def test_Timers_mean():
    # Arrange
    timer = Timers()
    timer.add("test", 12.3465)
    timer.add("test", 43.678567)
    timer.add("test", 78.0987657)
    timer.add("test", 43.4356)
    timer.add("test", 65.767)
    # Act
    result = timer.mean("test")
    # Assert
    assert result == 47.91161513333334

# Generated at 2022-06-13 18:35:19.922617
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    assert t.mean('toto') == 0
    t.add('toto', 2)
    assert t.mean('toto') == 2
    t.add('toto', 3)
    assert t.mean('toto') == 2.5

# Generated at 2022-06-13 18:35:28.957953
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t._timings = collections.defaultdict(list, {"a": [1, 2, 3, 4, 5]})
    assert t.median("a") == 3
    assert t.median("b") is None
    t._timings = collections.defaultdict(list, {"a": [1, 2, 5, 4, 5]})
    assert t.median("a") == 4
    t._timings = collections.defaultdict(list, {"a": [1]})
    assert math.isnan(t.median("a"))


# Generated at 2022-06-13 18:35:33.436242
# Unit test for method median of class Timers
def test_Timers_median():
    """Test whether Timers.median() returns correct value"""
    # Create timers object
    timers = Timers()

    # Define test data and assert minimal value is expected value
    timers.add("first", 1.1)
    timers.add("first", 2.2)
    timers.add("first", 3.3)
    assert math.isclose(timers.median("first"), 2.2)

# Generated at 2022-06-13 18:35:41.370055
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('test_median_1',1)
    timers.add('test_median_2',2)
    timers.add('test_median_3',3)
    timers.add('test_median_4',4)
    assert timers.median('test_median_1') == 1
    assert timers.median('test_median_2') == 2
    assert timers.median('test_median_3') == 3
    assert timers.median('test_median_4') == 4


# Generated at 2022-06-13 18:35:46.092066
# Unit test for method median of class Timers
def test_Timers_median():
    """Test method 'median' of class 'Timer'
    """
    values = [0.1, 0.2, 0.4]
    timers = Timers()
    timers.add('rms', values[0])
    timers.add('rms', values[1])
    timers.add('rms', values[2])
    assert timers.median('rms') == 0.2



# Generated at 2022-06-13 18:35:54.210850
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""

    data = {
        "a": [1,2,3],
        "b": [3,3],
        "c": []
    }

    t = Timers()
    # Add element to Timers
    for key in data:
        t._timings[key] = data[key]

    assert t.mean("a") == 2
    assert t.mean("b") == 3
    assert t.mean("c") == 0
    assert t.mean("d") == 0

# Generated at 2022-06-13 18:36:01.990246
# Unit test for method max of class Timers
def test_Timers_max():
    import pytest

    timers = Timers()
    assert timers.max("test") == 0
    timers.add("test", 1.)
    assert timers.max("test") == 1.
    timers.add("test", 2.)
    assert timers.max("test") == 2.
    timers.add("test", 3.)
    assert timers.max("test") == 3.
    with pytest.raises(KeyError):
        timers.max("missing")



# Generated at 2022-06-13 18:36:07.985461
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    assert timers.total('test') == 6
    assert timers.min('test') == 1
    assert timers.max('test') == 3


# Generated at 2022-06-13 18:36:18.683460
# Unit test for method min of class Timers
def test_Timers_min():
    timings = Timers()
    assert timings.min("test") == 0
    timings.add("test", 10)
    assert timings.min("test") == 10
    timings.add("test", 20)
    assert timings.min("test") == 10
    timings.add("test", 10)
    assert timings.min("test") == 10
    timings.add("test", 0)
    assert timings.min("test") == 0
    timings.add("test", -10)
    assert timings.min("test") == -10
    timings.add("test", -20)
    assert timings.min("test") == -20

# Generated at 2022-06-13 18:36:22.844995
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('test_timer', 0.25)
    timers.add('test_timer', 0.35)
    timers.add('test_timer', 0.22)
    assert timers.max('test_timer') == 0.35

# Generated at 2022-06-13 18:36:39.822940
# Unit test for method max of class Timers
def test_Timers_max():
    from hypothesis import given
    from .strategies import timedict
    from .strategies import nonempty_dict
    from .strategies import nonempty_dict_of_timer_dict

    @given(timedict())
    def test_max(timedict):
        result = max(timedict.items())[1]
        assert Timers(timedict).max(max(timedict.items())[0]) == result
    test_max()

    @given(nonempty_dict())
    def test_nonempty(nonempty_dict):
        result = max(nonempty_dict.items())[1]
        assert Timers(nonempty_dict).max(max(nonempty_dict.items())[0]) == result
    test_nonempty()


# Generated at 2022-06-13 18:36:40.400577
# Unit test for method median of class Timers
def test_Timers_median():
    pass

# Generated at 2022-06-13 18:36:48.676185
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add(name='test', value=5)
    t.add(name='test', value=3)
    t.add(name='test', value=2)
    t.add(name='test', value=1)
    t.add(name='test', value=4)
    t.add(name='test', value=5)
    t.add(name='test2', value=4)
    assert t.max(name='test') == 5
    assert t.max(name='test2') == 4
    assert t.max(name='test3') == 0 # Key does not exist


# Generated at 2022-06-13 18:36:52.653803
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("foo", 3)
    timers.add("XXX", 4)
    assert timers.min("foo") == 3


# Generated at 2022-06-13 18:36:54.356962
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("foo", 1)
    assert timers.mean("foo") == 1


# Generated at 2022-06-13 18:36:58.961553
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add('test', 1)
    t.add('test', 2)
    t.add('white', 1)
    t.add('white', 2)
    t.add('white', 3)
    t.add('black', 1)
    t.add('black', 2)
    assert t.mean('test') == 1.5
    assert t.mean('white') == 2
    assert t.mean('black') == 1.5

# Generated at 2022-06-13 18:37:08.276735
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    # First timer
    timers.add("timer1", 1)
    timers.add("timer1", 4)
    assert timers.min("timer1") == 1
    assert timers.mean("timer1") == 2
    assert timers.median("timer1") == 2
    assert timers.stdev("timer1") == math.sqrt(3) == 1.7320508075688772
    # Second timer
    timers.add("timer2", 2)
    timers.add("timer2", 3)
    assert timers.min("timer2") == 2
    assert timers.mean("timer2") == 2.5
    assert timers.median("timer2") == 2.5
    assert timers.stdev("timer2") == 0.5
    # Check total
    assert timers.total("timer1") == 5

# Generated at 2022-06-13 18:37:15.634828
# Unit test for method min of class Timers
def test_Timers_min():
    import math
    import random

    timers = Timers()
    timers.add("test", 1)

    assert timers.min("test") == 1
    assert math.isnan(timers.min("foo"))
    timers.add("test", 2)
    timers.add("test", 3)
    assert timers.min("test") == 1
    random.seed(0)
    timers.add("foo", random.random())
    timers.add("foo", random.random())
    assert timers.min("foo") < 0.1



# Generated at 2022-06-13 18:37:20.726292
# Unit test for method median of class Timers
def test_Timers_median():
    tests = [
        ([], 0),
        ([1, 2], 1.5),
        ([1, 3], 2),
        ([1, 2, 3], 2),
    ]
    for values, expected in tests:
        assert Timers().median("median") == expected

# Generated at 2022-06-13 18:37:32.389738
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers(
        {
            'first': 1,
            'second': 2,
        }
    )
    # Test if the function returns the minimum value of the given timer
    assert t.min('first') == 1
    # Test if the function returns the minimum value of the given timer
    assert t.min('second') == 2
    # Test if the function returns the minimum value of the given timer
    assert t.min('non-existent') == 0
    # Test if the function returns the minimum value of the given timer
    assert t.min('uninitialized') == 0
