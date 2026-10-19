

# Generated at 2022-06-13 18:27:45.119144
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the median funciton of Timers"""
    test_object = Timers()
    assert (test_object.median('timed') == 0)

# Generated at 2022-06-13 18:27:47.654025
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('a', 2.0)
    timers.add('a', 2.0)
    timers.add('a', 2.0)
    assert timers.min('a') == 2.0


# Generated at 2022-06-13 18:27:54.169720
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    assert math.isnan(t.mean("none"))
    t.add("test", 15)
    assert t.mean("test") == 15
    t.add("test", 15)
    assert t.mean("test") == 15
    t.add("test", 3)
    assert t.mean("test") == 11

# Generated at 2022-06-13 18:27:58.422896
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("old", 0)
    timers.add("new", 0)
    assert timers.max("old") == 0
    assert timers.max("new") == 0

# Generated at 2022-06-13 18:28:05.627025
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    # Initialize a new class Timers
    timer = Timers()
    # Add a timing value to the given timer
    timer.add("test", 2.0)
    # Test the method max of class Timers
    assert timer.max("test") == 2.0, "Error in method max of class Timers"



# Generated at 2022-06-13 18:28:13.083234
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers class"""
    timers = Timers()
    # Make sure value is correct
    timers.add("One", 1)
    assert timers.median("One") == 1
    timers.add("Two", 2)
    timers.add("Two", 3)
    assert timers.median("Two") == 2.5
    # Make sure if value does not exist, it throws error
    try:
        timers.median("Three")
    except KeyError:
        pass
    else:
        assert False


# Generated at 2022-06-13 18:28:18.142632
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('Timers', 1.0)
    timers.add('Timers', 1.0)
    timers.add('Timers', 1.0)

    assert timers.min('Timers') == 1.0

# Generated at 2022-06-13 18:28:21.850793
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add("test", 1)
    assert t.median("test") == 1

    t.add("test", 2)
    assert t.median("test") == 1.5

# Generated at 2022-06-13 18:28:29.159693
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add("x", 1)
    assert t.data["x"] == 1
    assert t.median("x") == 1
    t.add("x", 2)
    assert t.data["x"] == 3
    assert t.median("x") == 1.5
    t.add("x", 3)
    assert t.data["x"] == 6
    assert t.median("x") == 2

# Generated at 2022-06-13 18:28:32.176989
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("foo",4)
    t.add("foo", 5)
    t.add("foo", 6)
    t.add("foo", 8)
    assert t.mean("foo") == 5.5
    assert t.stdev("foo") == 1.707825127659933

if __name__ == " __main__ ":
    test_Timers_mean()

# Generated at 2022-06-13 18:28:38.951428
# Unit test for method mean of class Timers
def test_Timers_mean():
    """test_Timers_mean"""

    # New object
    timers = Timers()
    timers._timings['first'] = [1, 2, 3]

    # Check value returned by method mean
    assert timers.mean('first') == 2


# Generated at 2022-06-13 18:28:44.493252
# Unit test for method min of class Timers
def test_Timers_min():
    from hypothesis import given, settings
    from hypothesis.strategies import sampled_from
    from django_analyses.models.input.definitions import IntegerInputDefinition
    from django_analyses.models.input.types import IntegerInput
    from django_analyses.models.output.definitions import IntegerOutputDefinition
    from django_analyses.models.output.types import IntegerOutput
    from django_analyses.models.run.mixins import RunStatus
    from tests.strategies import integers
    from tests.utils import run_analysis

    analysis_cls = IntegerInputDefinition.get_analysis_class()
    input_def = IntegerInputDefinition.objects.create(required=False)
    output_def = IntegerOutputDefinition.objects.create(required=False)
    input_def.set_analysis_class(analysis_cls)

# Generated at 2022-06-13 18:28:47.385374
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('task1', 10)
    assert timers.min('task1') == 10


# Generated at 2022-06-13 18:28:50.115741
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers.median method"""
    t = Timers()
    t.add("a", 1)
    t.add("a", 3)
    t.add("b", 3)
    t.add("b", 3)
    assert t.median("a") == 2
    assert t.median("b") == 3

# Generated at 2022-06-13 18:28:52.822455
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('test', 2.0)
    timers.add('test', 3.0)
    assert timers.mean('test') == 2.5

# Generated at 2022-06-13 18:29:00.333319
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    assert t == {}, "Initial value is not empty (Dict)"
    t.add("latency", 1.0)
    t.add("latency", 1.0)
    t.add("latency", 1.0)
    t.add("throughput", 1.0)
    t.add("throughput", 1.0)
    t.add("throughput", 1.0)
    assert t == {'latency':3.0, 'throughput':3.0}, "Incorrect values (Dict)"
    assert t.max("latency") == 1.0, "Incorrect max value (Dict)"
    assert t.max("throughput") == 1.0, "Incorrect max value (Dict)"
    t.clear()

# Generated at 2022-06-13 18:29:05.814918
# Unit test for method median of class Timers
def test_Timers_median():
    import pytest
    timers = Timers()
    timers.add("cpu", 1.0)
    timers.add("cpu", 2.0)
    timers.add("cpu", 3.0)
    assert timers.median("cpu") == 2.0

# Generated at 2022-06-13 18:29:09.544155
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("TEST", 0.0)
    timers.add("TEST", 1.0)
    assert timers.min("TEST") == 0.0


# Generated at 2022-06-13 18:29:21.648331
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method 'median' of class Timers"""
    import pytest
    timers = Timers()
    timers.add('foo', 1)
    timers.add('foo', 2)
    timers.add('foo', 3)
    timers.add('foo', 4)
    assert timers.median('foo') == 2.5
    assert pytest.approx(timers.median('foo'), abs=1e-16) == 2.5
    timers.add('foo', 5)
    timers.add('foo', 6)
    timers.add('foo', 7)
    assert timers.median('foo') == 4.0
    assert pytest.approx(timers.median('foo'), abs=1e-16) == 4.0
    timers.add('foo', 8)

# Generated at 2022-06-13 18:29:24.234942
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("test_median", 0.1)
    timers.add("test_median", 0.2)
    timers.add("test_median", 0.2)
    assert timers.median("test_median") == 0.2

# Generated at 2022-06-13 18:29:26.772707
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers._timings['min'] = [10, 10, 100]
    assert timers.min('min') == 10

# Generated at 2022-06-13 18:29:41.601885
# Unit test for method mean of class Timers
def test_Timers_mean():
    """
    Test if method Timer.mean() calculates the mean correctly.
    """
    import numpy as np

    timer = Timers()

    # Test mean of empty sequence
    timer.add("test_1", 0)
    assert timer.mean("test_1") == 0.0

    # Test mean of sequence with a single value
    timer.clear()
    timer.add("test_1", 2)
    assert timer.mean("test_1") == 2.0

    # Test mean of sequence with two values
    timer.add("test_1", 3)
    assert timer.mean("test_1") == 2.5

    # Test mean of sequence with three values
    timer.add("test_1", 5)
    assert timer.mean("test_1") == 3.3333333333333335

    # Test mean with more values

# Generated at 2022-06-13 18:29:47.733601
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the median method from the Timers class"""
    timers = Timers()
    timers.add("a", 1)
    timers.add("a", 5)
    timers.add("a", 2)
    timers.add("b", 3)
    assert timers.median("a") == 2
    assert timers.median("b") == 3

# Generated at 2022-06-13 18:29:58.782301
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""

    # Initialization
    timers = Timers()

    # Default value before setting any timers
    assert timers.min('first') == 0

    # Error raised when accessing non-existing key
    try:
        timers.min('second')
    except KeyError as exc:
        assert str(exc) == "'second'"
    else:
        raise AssertionError('KeyError not raised')

    # Do a bunch of measurements
    for _ in range(10):
        timers.add('first', 1)
        timers.add('first', 2)
    timers.add('first', 3)

    # Check that the minimal value is returned
    assert timers.min('first') == 1

# Generated at 2022-06-13 18:30:01.002437
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    idx = -1
    t.add('test', idx)
    assert t.min('test') == idx


# Generated at 2022-06-13 18:30:05.828020
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()
    timers.add('Test', 5)
    timers.add('Test', 9)
    timers.add('Test', 11)
    timer = timers.median('Test')
    assert timer == 9



# Generated at 2022-06-13 18:30:13.050909
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers."""
    timers = Timers()
    timers._timings = {'a': [], 'b': [1, 2, 3], 'c': [1, 2, 3]}
    assert timers.min('a') == 0
    assert timers.min('b') == 1
    assert timers.min('c') == 1


# Generated at 2022-06-13 18:30:21.834088
# Unit test for method max of class Timers
def test_Timers_max():
    # Create an instance and add some timings
    t = Timers()
    t.add("x", 1)
    t.add("x", 2)
    t.add("y", -1)

    # Return the maximal value for each timer
    assert t.max("x") == 2
    assert t.max("y") == -1
    try:
        t.max("z")
        assert False, "KeyError should have been raised"
    except KeyError:
        pass

    # Correctly handle missing values
    t.clear()
    assert t.max("x") == 0
    assert t.max("y") == 0

# Generated at 2022-06-13 18:30:26.349213
# Unit test for method min of class Timers
def test_Timers_min():
    # Simple timer
    timers = Timers()
    timers.add("time", 123.0)
    assert timers.min("time") == 123.0

    # multiple timers
    timers.add("time", 456.0)
    assert timers.min("time") == 123.0

    # Empty timer name
    timers.add("", 300.0)
    assert timers.min("") == 300.0

    # multiple timers and empty string
    timers.add("", 400.0)
    assert timers.min("") == 300.0


# Generated at 2022-06-13 18:30:26.906303
# Unit test for method mean of class Timers
def test_Timers_mean():
    pass


# Generated at 2022-06-13 18:30:35.897351
# Unit test for method median of class Timers
def test_Timers_median():

    from math import isclose

    # check median of even size list
    assert isclose(Timers().add("test", 2).add("test", 4).median("test"), 3)
    # check median of odd size list
    assert isclose(Timers().add("test", 2).add("test", 4).add("test", 6).median("test"), 4)
    # check median of empty
    assert isclose(Timers().median("test"), 0)

# Generated at 2022-06-13 18:30:40.090912
# Unit test for method min of class Timers
def test_Timers_min():
    """Test min function of Timers"""

    timers = Timers()
    timers.add('foo', 1.0)
    timers.add('foo', 2.0)
    assert timers.min('foo') == 1.0



# Generated at 2022-06-13 18:30:47.885728
# Unit test for method mean of class Timers
def test_Timers_mean():
    # Test situation where list statistics is empty
    d = Timers()
    d.add("test", 0)
    assert d.mean("test") == 0

    # Test situation where list statistics is filled with valid numbers
    d.add("test", 5)
    d.add("test", 2)
    assert d.mean("test") == 3

    # Test situation where list statistics is filled with invalid numbers
    d.add("test", float('nan'))
    assert math.isnan(d.mean("test"))



# Generated at 2022-06-13 18:30:52.392361
# Unit test for method min of class Timers
def test_Timers_min():
    """Test special handling in Timers.min"""
    timers = Timers()
    assert timers.min("foo") == 0
    timers.add("foo", 1)
    assert timers.min("foo") == 1

# Generated at 2022-06-13 18:30:55.689616
# Unit test for method min of class Timers
def test_Timers_min():
    """Test timers"""
    timers = Timers()
    timers.add("name 1", 1.0)
    assert timers.min("name 1") == 1.0

# Generated at 2022-06-13 18:30:59.570321
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("req", 1)
    assert timers.median("req") == 1
    timers.add("req", 1)
    assert timers.median("req") == 1
    timers.add("req", 2)
    assert timers.median("req") == 1

# Generated at 2022-06-13 18:31:02.195498
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('foo', 10.0)
    assert timers.max('foo') == 10.0
    assert timers.max('bar') == 0.

# Generated at 2022-06-13 18:31:09.219594
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add('test', 10)
    assert t.max('test') == 10

    t2 = Timers({'test': 10})
    assert t2.max('test') == 10

    t2.add('test', 20)
    assert t2.max('test') == 20

    t2.add('test2', 10)
    assert t2.max('test2') == 10

    assert 'test3' not in t2.data

    assert 'test3' not in t2._timings
    t2.add('test3', 10)
    assert 'test3' in t2._timings

    assert t2.max('test3') == 10


# Generated at 2022-06-13 18:31:11.678903
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("Minimal", 1)
    timers.add("Minimal", 2)
    timers.add("Minimal", 3)
    assert timers.min("Minimal") == 1


# Generated at 2022-06-13 18:31:15.997718
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('test', 5)
    assert timers.min('test') == 5
    timers.add('test', 10)
    assert timers.min('test') == 5
    

# Generated at 2022-06-13 18:31:26.334428
# Unit test for method max of class Timers
def test_Timers_max():
    """Test method 'max' of class Timers"""

    def test_max(a_list, max_value):
        """Test that the maximum value of 'a_list' is 'max_value'"""
        timers = Timers()
        timers.data.clear()
        for a_item in a_list:
            timers.add('foo', a_item)
        assert timers.max('foo') == max_value

    # Perform tests
    test_max([], 0.0)
    test_max([1.0], 1.0)
    test_max([1.0, 2.0], 2.0)
    test_max([2.0, 1.0], 2.0)
    test_max([1.0, 1.0], 1.0)

# Generated at 2022-06-13 18:31:37.826537
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    from .utils import median

    test_cases = [([], None), ([1], 1), ([1, 2], 1.5), ([1, 3, 2], 2)]
    for values, expected in test_cases:
        timers = Timers()
        timers.apply = lambda func, name: func(values)
        result = timers.median("test")
        assert result == expected, (result, expected)

    assert median([]) == None
    assert median([1]) == 1
    assert median([1, 2]) == 1.5
    assert median([1, 3, 2]) == 2

# Generated at 2022-06-13 18:31:40.790693
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add('a', 1)
    assert t.mean('a') == 1


# Generated at 2022-06-13 18:31:47.792998
# Unit test for method median of class Timers
def test_Timers_median():
    x = Timers()
    x.add('a', 1.0)
    x.add('a', 3.0)
    x.add('a', 4.0)
    assert x.median('a') == 3.0
    assert x.median('b') == 0.0

test_Timers_median()

# Generated at 2022-06-13 18:31:57.715239
# Unit test for method min of class Timers
def test_Timers_min():
    """Test min method of Timers class"""
    timers = Timers()

    # Timings are empty
    assert timers.min("name") == 0

    # Add an empty list of timings
    timers.apply(len, name="name")
    assert timers.min("name") == 0

    # Add an empty list of timings
    timers._timings["name"] = []
    assert timers.min("name") == 0

    # Add an value
    timers._timings["name"] = [1.5]
    assert timers.min("name") == 1.5

    # Add an value
    timers._timings["name"] = [2.5]
    assert timers.min("name") == 2.5

    # Add an value
    timers._timings["name"] = [1.5, 2.5]
    assert timers.min

# Generated at 2022-06-13 18:32:07.883405
# Unit test for method min of class Timers
def test_Timers_min():
    """Check that all public methods work as intended"""
    timers = Timers()
    timers.add("T1", 1)
    timers.add("T1", 2)
    timers.add("T2", 3)
    timers.add("T2", 4)
    assert timers.count("T1") == 2
    assert timers.total("T1") == 3
    assert timers.min("T1") == 1
    assert timers.max("T1") == 2
    assert timers.mean("T1") == 1.5
    assert timers.median("T1") == 1.5
    assert timers.stdev("T1") == 0.5
    try:
        _ = timers.mean("Foo")
    except KeyError:
        assert True
    else:
        assert False
    timers.add("T1", 5)


# Generated at 2022-06-13 18:32:12.944147
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    assert t.min("foo") == 0
    assert t.min("bar") == 0
    t.add("foo", 1.0)
    t.add("foo", 2.0)
    t.add("bar", 3.0)
    assert t.min("foo") == 1.0
    assert t.min("bar") == 3.0


# Generated at 2022-06-13 18:32:19.566700
# Unit test for method min of class Timers
def test_Timers_min():
    """Check that min works as intended"""
    timers = Timers()
    timers.add("foo", 1)
    assert timers.min("foo") == 1.0

    timers.add("foo", 2)
    assert timers.min("foo") == 1.0

    timers.add("foo", 3)
    assert timers.min("foo") == 1.0

    timers.add("foo", 1)
    assert timers.min("foo") == 1.0


# Generated at 2022-06-13 18:32:23.935760
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()

    for _ in range(100):
        timers.add("test", 1)

    assert timers.count("test") == 100
    assert timers.median("test") == 1
    assert timers.total("test") == 100
    assert timers.mean("test") == 1
    assert timers.min("test") == 1
    assert timers.max("test") == 1

# Generated at 2022-06-13 18:32:28.093212
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('method mean test', 4)
    expected = 4
    actual = timers.mean('method mean test')
    assert actual == expected

# Generated at 2022-06-13 18:32:34.787927
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    test_values = {'a':1, 'b':2, 'c':3, 'd':4}
    for name, value in test_values.items():
        timers.add(name=name, value=value)
    assert max(test_values.values()) == timers.max('d')


# Generated at 2022-06-13 18:32:46.600435
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers.median"""
    # Define input, expected output and actual output
    input_value: List[float] = [2.0, 3.0, 4.0]
    expected_output: float = 3.0
    timers: Timers = Timers() # Create instance of Timers class
    # Get actual output
    actual_output: float = timers.median(input_value)
    # Compare expected output with actual output
    assert(expected_output == actual_output)
    # Report test result
    print("Success!")

# Perform doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()




# Generated at 2022-06-13 18:32:51.697599
# Unit test for method max of class Timers
def test_Timers_max():
    """Ensures that the currently stored maximal value of one timer is returned"""
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    timers.add("test", 3.0)

    assert timers.max("test") == 3.0



# Generated at 2022-06-13 18:32:59.667894
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("test", 0)
    assert timers.min("test") == 0
    timers.add("test", 1)
    assert timers.min("test") == 0
    timers.add("test", -1)
    assert timers.min("test") == -1
    timers.clear()


# Generated at 2022-06-13 18:33:06.612803
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    # Define timers
    timers = Timers()

    # Add values
    timers.add("foo", 1)
    timers.add("foo", 2)
    timers.add("foo", 3)
    timers.add("foo", 4)
    timers.add("bar", 1)
    timers.add("bar", 2)

    # Test mean
    assert timers.mean("foo") == 2.5
    assert timers.mean("bar") == 1.5

# Generated at 2022-06-13 18:33:11.988631
# Unit test for method mean of class Timers
def test_Timers_mean():
    # Initialize name, value and expected_output
    name = 'timer_name'
    value = 2
    expected_output = 2
    timers = Timers()

    # Add value to timers
    timers.add(name, value)

    # Compare mean of name with expected_output
    assert timers.mean(name) == expected_output


# Generated at 2022-06-13 18:33:15.287369
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit tests for method min of class Timers"""
    tim = Timers()
    tim.add("test1", 1)
    tim.add("test2", 5)
    assert tim.min("test2") == 5
    assert tim.min("test1") == 1

# Generated at 2022-06-13 18:33:17.939893
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t._timings['foo'] = [1, 2, 3]
    t.data['foo'] = 6
    assert t.median('foo') == 2
    t._timings['bar'] = [1, 2, 3, 4]
    t.data['bar'] = 10
    assert t.median('bar') == 2.5

# Generated at 2022-06-13 18:33:27.514508
# Unit test for method median of class Timers
def test_Timers_median():
    """Something like unit testing: ensure that the median value of the
    values in _timings['name'] is returned.
    """
    timers = Timers()

    def f(name: str, values: List[float], expected: float) -> None:
        timers._timings[name] = values
        assert timers.median(name) == expected

    # Odd number of values
    f('nice', [11.0, 22.0, 33.0], 22.0)
    # Even number of values
    f('nice', [10.0, 20.0, 30.0, 40.0], 25.0)
    # One value
    f('nice', [10.0], 10.0)
    # Empty list
    f('nice', [], math.nan)


# Generated at 2022-06-13 18:33:30.916119
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min('test') == 0
    timers.add('test', 10)
    assert timers.min('test') == 10
    timers.add('test', 20)
    assert timers.min('test') == 10
    timers.add('test', 5)
    assert timers.min('test') == 5


# Generated at 2022-06-13 18:33:47.139423
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""

    # Create a timer
    timers = Timers()

    # Test exception if timer does not exist
    try:
        # Getting the median of a timer that does not exist should raise a
        # KeyError exception.
        _ = timers.median("not a timer")
    except KeyError:
        pass
    else:
        # Fail the test if no exception is raised.
        raise AssertionError

    # Test empty timer
    timers.add("empty timer", 0.0)
    assert timers.median("empty timer") == 0.0

    # Test a couple of timers
    for i in range(10):
        timers.add("timer #1", i)
        timers.add("timer #2", 2 * i)
        timers.add("timer #3", 3 * i)


# Generated at 2022-06-13 18:33:53.363261
# Unit test for method min of class Timers
def test_Timers_min():
    """Test for method Timers.min"""
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    timers.add('test2', -1)
    timers.add('test2', -2)
    timers.add('test2', -3)
    assert timers.min('test') == 1
    assert timers.min('test2') == -3
    assert timers.min('test3') == 0


# Generated at 2022-06-13 18:33:58.001608
# Unit test for method max of class Timers
def test_Timers_max():
    assert Timers().max("name1") == 0
    t = Timers({"name1": 1, "name2": 2})
    assert t.max("name2") == 2
    with pytest.raises(KeyError):
        t.max("name3")

# Generated at 2022-06-13 18:34:05.438094
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    from .test_util import assert_never_called
    timers = Timers()
    timers.add("test_timer", 10)
    assert timers.min("test_timer") == 10
    assert timers.min("test_timer_2") == 0
    assert_never_called(timers.min, "test_timer_3")

# Generated at 2022-06-13 18:34:06.990504
# Unit test for method min of class Timers
def test_Timers_min():
    timer = Timers()
    assert timer.min('my timer') == 0

# Generated at 2022-06-13 18:34:10.577561
# Unit test for method mean of class Timers
def test_Timers_mean():
    a = Timers()
    a.add("test", 100)
    a.add("test", 200)
    a.add("test", 50)
    assert a.mean("test") == 125.0

# Generated at 2022-06-13 18:34:14.950993
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("mytimer", 5.)
    timers.add("mytimer", 10.)
    assert timers.mean("mytimer") == 7.5

# Generated at 2022-06-13 18:34:27.345972
# Unit test for method median of class Timers
def test_Timers_median():
    from random import random
    from functools import partial

    functools_sort = partial(sorted, key=lambda x: x[1])
    input_items = [(f'{i}', random()) for i in range(100)]

    timers = Timers()
    for key, value in input_items:
        timers.add(key, value)

    assert sorted(timers.items()) == functools_sort(timers.items())
    assert sorted(timers.data.items()) == functools_sort(timers.data.items())
    assert sorted(timers._timings.items()) == functools_sort(timers._timings.items())

    output = [(k, timers.median(k)) for k in timers._timings]
    assert sorted(output) == functools_sort(output)

# Generated at 2022-06-13 18:34:30.146558
# Unit test for method min of class Timers
def test_Timers_min():
    """Test minimal value of timings"""
    timers = Timers()
    timers.add('a', 1)
    timers.add('a', 2)
    assert timers.min('a') == 1
    timers.add('b', 3)
    assert timers.min('b') == 3
    assert timers.min('c') == 0


# Generated at 2022-06-13 18:34:33.146283
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("timer", 0.1)
    timers.add("timer", 0.2)
    assert timers.median("timer") == 0.15

# Generated at 2022-06-13 18:34:55.798319
# Unit test for method mean of class Timers
def test_Timers_mean():
    timing = Timers()
    timing.add('test', 10)
    assert timing.mean('test') == 10
    timing.add('test', 20)
    assert timing.mean('test') == 15
    timing.add('test', 30)
    assert timing.mean('test') == 20
    timing.add('test', 40)
    assert timing.mean('test') == 25
    timing.add('test', 50)
    assert timing.mean('test') == 30
    timing.add('test', 60)
    assert timing.mean('test') == 35
    timing.add('test', 70)
    assert timing.mean('test') == 40
    timing.add('test', 80)
    assert timing.mean('test') == 45
    timing.add('test', 90)
    assert timing.mean('test') == 50

# Generated at 2022-06-13 18:35:02.075934
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    x= Timers()
    x.add("1",1)
    x.add("1",2)
    x.add("1",3)
    assert x.median("1") == 2.0

# Generated at 2022-06-13 18:35:06.269862
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timer = Timers()
    timer._timings = {'foo': []}
    timer.add('foo', 100.0)
    assert timer.min('foo') == 100.0


# Generated at 2022-06-13 18:35:09.688606
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()

    timers['a'] = 0.1
    timers.add('a', 0.1)
    timers.add('a', 0.2)
    timers.add('a', 0.3)
    timers.add('a', 0.4)
    timers.add('a', 0.5)

    assert timers.max('a') == 0.5



# Generated at 2022-06-13 18:35:17.880827
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers["Test"] = 0.0
    timers.add("Test", 1.4)
    assert timers.max("Test") == 1.4
    timers.add("Test", 2.6)
    assert timers.max("Test") == 2.6
    timers.add("Test", 2.6)
    assert timers.max("Test") == 2.6
    timers.add("Test", 3.9)
    assert timers.max("Test") == 3.9
    timers.add("Test", 5.1)
    assert timers.max("Test") == 5.1
    assert timers.max("Test") == 5.1


# Generated at 2022-06-13 18:35:28.146566
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("my_timer", 5.0)
    timers.add("my_timer", 12.0)
    timers.add("my_timer", 7.0)
    timers.add("my_timer", 3.0)
    timers.add("my_timer", 8.0)
    timers.add("my_timer", 12.0)
    timers.add("my_timer", 7.0)
    assert timers.mean("my_timer") == 7  # Expected result



# Generated at 2022-06-13 18:35:34.942274
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add('test', 3)
    assert t.mean('test') == 3
    assert t.count('test') == 1
    assert t.total('test') == 3
    t.add('test', 7)
    assert t.mean('test') == 5
    assert t.count('test') == 2
    assert t.total('test') == 10
    t.add('test', 5)
    assert t.mean('test') == 5
    assert t.count('test') == 3
    assert t.total('test') == 15
    assert t.mean('test2') == math.nan

# Generated at 2022-06-13 18:35:36.509692
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("test", 100)
    assert t.max('test') == 100


# Generated at 2022-06-13 18:35:40.950426
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('1', 1)
    timers.add('1', 2)
    timers.add('2', 3)

    assert timers.mean('1') == 1.5
    assert timers.mean('2') == 3.0



# Generated at 2022-06-13 18:35:48.707358
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers._timings = {
        "real": [1, 2, 3],
        "user": [0.5, 0.6, 1],
        "sys": [0.1, 0.2, 0.3]
    }
    assert timers.min("real") == 1
    assert timers.min("user") == 0.5
    assert timers.min("sys") == 0.1
    assert timers.min("__not_there__") == 0


# Generated at 2022-06-13 18:36:06.346807
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    for i in range(0, 10):
        timers.add("timer", i*0.1)
    assert timers.max("timer") == 0.9


# Generated at 2022-06-13 18:36:11.531340
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Return the mean of the results of a named timer"""
    test = Timers()
    test.add("test_timer", 1.0)
    test.add("test_timer", 2.0)
    assert test.mean("test_timer") == 1.5

# Generated at 2022-06-13 18:36:19.519716
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    # Test when the internal timings are empty
    timers = Timers()
    assert timers.mean("dummy") == 0.0

    # Test when the internal timings contain only one value
    timers = Timers()
    timers.add("dummy", 1.0)
    assert timers.mean("dummy") == 1.0

    # Test when the internal timings contain several values
    timers = Timers()
    timers.add("dummy", 1.0)
    timers.add("dummy", 2.0)
    timers.add("dummy", 3.0)
    timers.add("dummy", 4.0)
    assert timers.mean("dummy") == 2.5

# Generated at 2022-06-13 18:36:25.222876
# Unit test for method mean of class Timers
def test_Timers_mean():
    from unittest.mock import patch

    timers = Timers()

    # Perform patching
    with patch.object(statistics, "mean") as mock_mean:
        timers.apply(lambda x: x, "first one")
        mock_mean.assert_not_called()

        timers.apply(lambda x: x, "second one")
        mock_mean.assert_called_once()

# Generated at 2022-06-13 18:36:28.086079
# Unit test for method min of class Timers
def test_Timers_min():
    test = Timers()
    test.add('first', 5)
    test.add('third', 7)
    test.add('second', 1)
    test.add('third', 2)
    assert test.min('third') == 2


# Generated at 2022-06-13 18:36:38.417491
# Unit test for method median of class Timers
def test_Timers_median():
    # Test for empty series
    empty = Timers()
    assert empty.median("name") == 0

    # Test for single-entry series
    single = Timers({"name": 1.0})
    assert single.median("name") == 1.0

    # Test for even-numbered series
    even = Timers({"name": 5.0})
    for i in range(4):
        even.add("name", i)
    assert even.median("name") == 2.0

    # Test for odd-numbered series
    odd = Timers({"name": 5.0})
    for i in range(5):
        odd.add("name", i)
    assert odd.median("name") == 2.5

    # Test for out of range index

# Generated at 2022-06-13 18:36:40.116796
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median method of Timers class"""
    assert Timers.median(Timers, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5

# Generated at 2022-06-13 18:36:48.196628
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('test', 3.0)
    timers.add('test', 6.0)
    timers.add('test', 7.0)
    timers.add('test', 8.0)
    timers.add('test', 8.0)
    timers.add('test', 10.0)
    timers.add('test', 13.0)
    timers.add('test', 15.0)
    timers.add('test', 16.0)
    timers.add('test', 20.0)
    assert timers.median('test') == 9.0


# Generated at 2022-06-13 18:37:00.041420
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("a", 1.0)
    timers.add("a", 2.0)
    assert timers.mean("a") == 1.5
    timers.add("b", 4.0)
    assert timers.mean("b") == 4.0
    # This will raise a KeyError
    try:
        timers.mean("c")
        False
    except KeyError:
        True
    except:
        False
    # This will raise a TypeError
    try:
        timers.mean(1)
        False
    except TypeError:
        True
    except:
        False
    # This will raise a TypeError
    try:
        timers["a"] = 3.0
        False
    except TypeError:
        True
    except:
        False
    return


# Generated at 2022-06-13 18:37:08.181945
# Unit test for method min of class Timers
def test_Timers_min():
    # test_Timers_min1
    # Test for empty dictionary
    try:
        t = Timers()
        x = t.min('a')
    except Exception:
        pass

    # test_Timers_min2
    # Test for non-empty dictionary with non-empty key
    t = Timers()
    t._timings['a'] = [3, 5]
    assert t.min('a') == 3

    # test_Timers_min3
    # Test for non-empty dictionary with empty key
    t = Timers()
    t._timings['a'] = []
    try:
        x = t.min('b')
    except Exception:
        pass

