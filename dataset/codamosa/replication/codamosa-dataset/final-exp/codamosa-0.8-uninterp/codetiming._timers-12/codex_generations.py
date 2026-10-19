

# Generated at 2022-06-13 18:27:46.385217
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()

    assert timers.max("test") == 0

    timers.add("test", 1)
    assert timers.max("test") == 1

    timers.add("test", 0)
    assert timers.max("test") == 1

    timers.add("test", 2)
    assert timers.max("test") == 2


# Generated at 2022-06-13 18:27:47.908719
# Unit test for method mean of class Timers
def test_Timers_mean():
    """
    Unit test for method mean of class Timers
    """
    assert isinstance(Timers(), Timers)


# Generated at 2022-06-13 18:27:52.686862
# Unit test for method mean of class Timers
def test_Timers_mean():
    assert Timers().mean("missing") == math.nan
    assert Timers({"x":0}).mean("x") == 0
    assert Timers({"x":1}).mean("x") == 1
    assert Timers().add("x", 2).mean("x") == 2
    assert Timers().add("x", 2).add("x", 2).mean("x") == 2
    assert Timers().add("x", 1).add("x", 2).mean("x") == 1.5
    assert Timers().add("x", 2).add("x", 1).mean("x") == 1.5
    return True


# Generated at 2022-06-13 18:27:56.989108
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timings = Timers()

    # Test empty timers
    assert timings.median("test1") == 0

    # Test for one time
    timings.add("test1", 5)
    assert timings.median("test1") == 5

    # Test for even number of times, even number of times, odd number of times
    timings.add("test1", 2)
    timings.add("test1", 4)
    timings.add("test1", 3)
    assert timings.median("test1") == 3
    timings.add("test1", 1)
    assert timings.median("test1") == 2.5
    timings.add("test1", 0)
    assert timings.median("test1") == 2

# Generated at 2022-06-13 18:28:02.499051
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("time", 1.0)
    timers.add("time", 2.0)
    assert timers.mean("time") == 3/2
    assert timers.mean("not_here") == 0



# Generated at 2022-06-13 18:28:07.830910
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Check that Timers.mean() returns the mean of a list of values"""
    # Test simple values
    t = Timers()
    for i in range(4):
        t.add('timer', i)
    assert t.mean('timer') == 1.5
    # Test empty list
    t.add('timer', 0)
    assert t.mean('timer') == 2.0


# Generated at 2022-06-13 18:28:14.824816
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()

    timers.add("test1", 0.5)
    timers.add("test1", 0.75)
    timers.add("test1", 1)
    timers.add("test1", 1.5)

    timers.add("test2", 0.5)
    timers.add("test2", 1)
    timers.add("test2", 2)
    timers.add("test2", 3)

    assert timers.min("test1") == 0.5
    assert timers.max("test2") == 3


# Generated at 2022-06-13 18:28:21.627122
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("Timer1", 1)
    timers.add("Timer1", 2)
    timers.add("Timer1", 3)
    timers.add("Timer2", 4)
    timers.add("Timer2", 5)
    assert timers.max("Timer1") == 3
    assert timers.max("Timer2") == 5

# Generated at 2022-06-13 18:28:31.546904
# Unit test for method median of class Timers
def test_Timers_median(): 
    """Unit test for method median of class Timers"""

    # Timers-object
    timers = Timers()

    # fill timers-object with data
    for x in ["name1", "name2", "name3"]:
        for y in range(10):
            timers.add(x, y)

    # median of existing name
    if timers.median("name1") == 4.5:
        print("Unit test for method median of class Timers: PASSED")
    else:
        print("Unit test for method median of class Timers: FAILED")

    # median of not existing name
    try:
        timers.median("nameX")
    except KeyError:
        print("Unit test for method median of class Timers: PASSED")

# Generated at 2022-06-13 18:28:36.482181
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.data = {'MyTimer': 100}
    timers._timings = {'MyTimer': [10, 15, 20, 25, 30]}
    assert 15 == timers.median('MyTimer')
    timers.clear()
    assert 0 == timers.median('MyTimer')



# Generated at 2022-06-13 18:28:44.063134
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()
    assert timers.median("test") == 0
    timers._timings["test"] = [1, 2, 3]
    assert timers.median("test") == 2
    timers._timings["test"] = [1, 2, 3, 4, 5]
    assert timers.median("test") == 3

# Generated at 2022-06-13 18:28:49.732330
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add('test', 1.0)
    t.add('test', 2.0)
    t.add('test', 3.0)

    # Call max on the timers
    value = t.max('test')

    print(value)


# Generated at 2022-06-13 18:28:53.109998
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test if average time is correctly calculated"""
    timers = Timers()
    timers.add('name', 5.0)
    timers.add('name', 10.0)
    assert timers.mean('name') == 7.5

# Generated at 2022-06-13 18:28:57.055537
# Unit test for method min of class Timers
def test_Timers_min():
    timer = Timers()
    timer.add("a", 1)
    timer.add("a", 2)
    timer.add("a", -3)
    timer.add("a", 4)
    assert timer.min("a") == -3
    assert timer.min("b") == 0



# Generated at 2022-06-13 18:29:01.859210
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median value of timings"""
    timers = Timers()
    # Assert that non-existent key raises a KeyError
    assert timers.median('key')
    timers._timings['key'] = [5, 3, 1, 4]
    assert timers.median('key') == 4
    timers._timings['key'].append(2)
    assert timers.median('key') == 3.5

# Generated at 2022-06-13 18:29:06.490708
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    data = Timers()
    data.add('a', 1)

    assert data.min('a') == 1
    assert data.min('b') == 0



# Generated at 2022-06-13 18:29:09.722091
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    for i in range(4):
        timers.add('test', i)
    assert timers.max('test') == 3


# Generated at 2022-06-13 18:29:14.199349
# Unit test for method median of class Timers
def test_Timers_median():
    _timers = Timers()
    _timers.add("A", 1)
    _timers.add("A", 2)
    _timers.add("A", 3)
    assert _timers.median("A") == 2

# Generated at 2022-06-13 18:29:19.418082
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    assert timers.median("foo") == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(f"{__file__} passed all {doctest.master.summarize()} tests")
    test_Timers_median()

# Generated at 2022-06-13 18:29:21.852693
# Unit test for method min of class Timers
def test_Timers_min():
    try:
        Timers().min("bla")
    except:
        pass
    else:
        assert False


# Generated at 2022-06-13 18:29:31.295957
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('1', 1)
    timers.add('1', 2)
    timers.add('2', 3)
    assert timers.max('1') == 2
    assert timers.max('2') == 3

# Generated at 2022-06-13 18:29:34.615191
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("foo", 1)
    timers.add("foo", 2)
    timers.add("foo", 3)
    assert  timers.median("foo") == 2

# Generated at 2022-06-13 18:29:39.579524
# Unit test for method max of class Timers
def test_Timers_max():
    dict1 = Timers()
    dict1.add('test', 10)
    dict1.add('test', 15)
    dict1.add('test1', 12)
    dict1.add('test1', 13)
    assert dict1.max('test') == 15
    assert dict1.max('test1') == 13

# Generated at 2022-06-13 18:29:44.630103
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min("test") == 0.0
    timers.add("test", 2.0)
    assert timers.min("test") == 2.0
    timers.add("test", 2.0)
    assert timers.min("test") == 2.0
    timers.add("test", 1.0)
    assert timers.min("test") == 1.0


# Generated at 2022-06-13 18:29:52.425357
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("A", 1)
    timers.add("A", 2)
    timers.add("A", 3)
    timers.add("B", 1)
    timers.add("B", 2)
    timers.add("C", 1)
    assert timers.mean("A") == 2.0
    assert timers.mean("B") == 1.5
    assert timers.mean("C") == 1.0


# Generated at 2022-06-13 18:29:57.512166
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    timers.add('test1', 1)
    timers.add('test1', 2)
    timers.add('test2', 10)
    assert timers.mean('test1') == 1.5
    assert timers.mean('test2') == 10

# Generated at 2022-06-13 18:30:00.914072
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timers = Timers()
    timers.add('name', 1)
    timers.add('name', 2)
    timers.add('name', 3)
    assert timers.min('name') == 1



# Generated at 2022-06-13 18:30:08.613920
# Unit test for method min of class Timers
def test_Timers_min():
    """
    Check correctness of method min of class Timers
    """
    timers = Timers()
    assert timers.min("test") == 0

    timers = Timers()
    timers.add("test", 10)
    assert timers.min("test") == 10

    timers = Timers()
    timers.add("test", 10)
    timers.add("test", 20)
    assert timers.min("test") == 10

    timers = Timers()
    timers.add("test", 20)
    timers.add("test", 10)
    assert timers.min("test") == 10

# Generated at 2022-06-13 18:30:13.440983
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    timers = Timers()
    timers.add("A", 2)
    timers.add("A", 3)
    timers.add("A", 5)
    timers.add("A", 5)
    assert timers.min("A") == 2

# Generated at 2022-06-13 18:30:18.811902
# Unit test for method median of class Timers
def test_Timers_median():
    """test_Timers_median"""
    timers = Timers()
    for i in range(1, 10):
        timers.add("test", i)
    assert isinstance(timers.median("test"), float) == True
    assert timers.median("test") == 5.0


# Generated at 2022-06-13 18:30:23.957079
# Unit test for method max of class Timers
def test_Timers_max():
    timers=Timers()
    timers.add("A", 1)
    timers.add("A", 2)
    timers.add("A", 3)
    assert timers.max("A") == 3

# Generated at 2022-06-13 18:30:30.470297
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t["total"] = 10
    t["min"] = 1
    t["max"] = 100
    t["mean"] = 10
    t["stdev"] = 10
    t.add("median", 10)

    assert t.min("total") == 1
    assert t.min("min") == 1
    assert t.min("max") == 100
    assert t.min("mean") == 10
    assert t.min("stdev") == 10
    assert t.min("median") == 10



# Generated at 2022-06-13 18:30:34.776097
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("max", 5.5)
    timers.add("max", 10.5)
    timers.add("other", 5.5)
    assert timers.max("max") == 10.5


# Generated at 2022-06-13 18:30:43.007628
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the mean() method of class Timers"""
    timer = Timers()
    timer.add("setup", 0.01)
    timer.add("setup", 0.01)
    timer.add("setup", 0.01)
    timer.add("trajectory", 0.02)
    timer.add("trajectory", 0.02)
    timer.add("trajectory", 0.02)
    timer.add("trajectory", 0.02)
    timer.add("trajectory", 0.02)
    timer.add("trajectory", 0.02)

    assert abs(timer.mean("setup") - 0.01) < 1e-8
    assert abs(timer.mean("trajectory") - 0.02) < 1e-8



# Generated at 2022-06-13 18:30:46.168389
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit tests for method max of class Timers"""
    timers = Timers()
    timers.add("name", 1)
    timers.add("name", 5)
    timers.add("name", 2)
    assert timers.max("name") == 5


# Generated at 2022-06-13 18:30:49.993269
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("max", 10)
    timers.add("max", 20)
    timers.add("max", 30)
    assert timers.max("max") == 30



# Generated at 2022-06-13 18:30:52.755794
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.data["timer 1"] = 2
    assert timers.min("timer 1") == 2

# Generated at 2022-06-13 18:31:01.117963
# Unit test for method min of class Timers
def test_Timers_min():
    import pandas as pd
    """
        Test that .min() method of Timers class
        return the minimum value of the timer
    """
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    g = {}
    for value in a:
        g[value] = value
    df = pd.DataFrame.from_dict(g)

    # Call method
    result = df.min()[0]

    # Expected output
    expected = 0

    assert result == expected



# Generated at 2022-06-13 18:31:06.708023
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('A', 1.0)
    timers.add('A', 2.0)
    timers.add('A', 3.0)
    assert timers.median('A') == 2.0
    timers.add('A', 4.0)
    timers.add('A', 5.0)
    assert timers.median('A') == 3.0
    try:
        timers.median('B') == 3.0
    except Exception as error:
        raise error


# Generated at 2022-06-13 18:31:08.867212
# Unit test for method median of class Timers
def test_Timers_median():
    """Used to test if the median value is calculated correctly.
    """
    timers = Timers()
    timers.add("test", 1)
    timers.add("test", 2)
    timers.add("test", 3)
    assert timers.median("test") == 2
    assert timers.total("test") == 6

# Generated at 2022-06-13 18:31:16.381487
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('test', 1)
    assert timers.median('test') == 1, "Function median has failed to return the median of a single element list"
    timers.add('test', 2)
    assert timers.median('test') == 1.5, "Function median has failed to return the median of a two element list"
    timers.add('test', 3)
    assert timers.median('test') == 2, "Function median has failed to return the median of a three element list"
    timers.clear()
    assert timers.median('test') == 0, "Function median has failed to handle an empty list"


# Generated at 2022-06-13 18:31:25.378504
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    #
    # Test with an empty dictionary
    assert timers.min('foo') == 0
    #
    # Test with a dictionary with one entry
    timers['foo'] = 1
    timers._timings['foo'] = [2.3, 4.5]
    assert timers.min('foo') == 2.3
    #
    # Test with a dictionary with several entries
    timers['bar'] = 21
    timers['baz'] = 34
    timers._timings['bar'] = [4.4, 3.1]
    assert timers.min('bar') == 3.1
    #
    # Test with a non-existing key
    assert timers.min('zab') == 0
    #
    return


# Generated at 2022-06-13 18:31:32.241430
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()

    timers.add("time", 1.0)
    timers.add("time", 2.0)
    timers.add("time", 3.0)

    median = timers.median("time")

    assert median == 2.0



# Generated at 2022-06-13 18:31:34.699967
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    try:
        timers.mean('no_data')
    except KeyError as e:
        assert 'no_data' in str(e)

# Generated at 2022-06-13 18:31:40.577599
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min("test") == 0
    assert timers.min("test") == 0
    timers.add("test", 2)
    assert timers.min("test") == 2
    timers.add("test", 1)
    assert timers.min("test") == 1
    timers.add("test", 4)
    assert timers.min("test") == 1

# Generated at 2022-06-13 18:31:46.356662
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    timers = Timers()
    timers.add("one", 1.0)
    assert isinstance(timers, Timers)
    assert timers.min("two") == 0
    assert timers.min("one") == 1.0


# Generated at 2022-06-13 18:31:50.383584
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    assert timers.min('test') == 1.0



# Generated at 2022-06-13 18:31:55.446909
# Unit test for method mean of class Timers
def test_Timers_mean():
    import pytest
    from comb_spec_searcher.strategies.caching import Timers
    values = Timers()
    values.add("aaa", 2)
    values.add("aaa", 3)
    assert values.mean("aaa") == 2.5
    with pytest.raises(KeyError):
        values.mean("abc")

# Generated at 2022-06-13 18:32:01.035157
# Unit test for method mean of class Timers
def test_Timers_mean():
    timings = Timers()
    timings.add("First", 0.1)
    timings.add("First", 0.2)
    timings.add("First", 0.3)
    assert timings.mean("First") == 0.2

# Generated at 2022-06-13 18:32:05.294762
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    assert timers.max('name') == 0
    timers.add('name', 3.0)
    assert timers.max('name') == 3.0
    timers.add('name', 2.0)
    assert timers.max('name') == 3.0
    timers.add('name', 4.0)
    assert timers.max('name') == 4.0

# Generated at 2022-06-13 18:32:16.530559
# Unit test for method max of class Timers
def test_Timers_max():
    """Case where there are no timings, then one, then two"""
    timers = Timers()
    assert timers.max("test timer name") == 0
    timers.add("test timer name", 1)
    assert timers.max("test timer name") == 1
    timers.add("test timer name", 2)
    assert timers.max("test timer name") == 2


# Generated at 2022-06-13 18:32:25.578945
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Doctest for method mean of class Timers"""
    from unittest import TestCase
    from doctest import testmod as doctest_testmod
    from doctest import ELLIPSIS
    import unittest

    class Test(TestCase):
        """Test case for method mean of class Timers"""
        def test_mean(self):
            """Test method mean of class Timers"""
            timers = Timers()
            timers.add('name', 2)
            timers.add('name', 3)
            timers.add('name', 4)
            self.assertEqual(timers.mean('name'), 3.0)
            self.assertEqual(timers.mean('name2'), 0.0)
            with self.assertRaises(KeyError):
                timers.mean('name3')

    failure_count, test_count

# Generated at 2022-06-13 18:32:31.581392
# Unit test for method max of class Timers
def test_Timers_max():
    """Test the method max of class Timers"""
    t = Timers()
    t._timings = {'test1': [1, 7, 3], 'test2': [2, 3]}
    assert t.max('test1') == 7
    assert t.max('test2') == 3
    assert t.max('test3') == 0
    t._timings = {}
    assert t.max('test1') == 0


# Generated at 2022-06-13 18:32:35.016175
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('test', 0)
    t.add('test', 1)
    t.add('test', 2)
    assert t.min('test') == 0


# Generated at 2022-06-13 18:32:40.492416
# Unit test for method max of class Timers
def test_Timers_max():
    # Setup
    timers = Timers()
    # Exercise
    timers.add('name1', 1)
    timers.add('name2', 2)
    timers.add('name3', 3)
    # Verify
    assert timers.max('name1') == 1
    assert timers.max('name2') == 2
    assert timers.max('name3') == 3
    assert timers.max('name4') == 0


# Generated at 2022-06-13 18:32:43.035669
# Unit test for method min of class Timers
def test_Timers_min():
    """Test for method min of class Timers"""
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 18:32:49.308717
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('foo', 3)
    assert timers.mean('foo') == 3
    timers.add('foo', 4)
    assert timers.mean('foo') == 3.5
    timers.clear()
    assert timers.mean('foo') == 0

# Generated at 2022-06-13 18:32:53.891139
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers._timings["a"] = [10, 20, 30]
    timers._timings["b"] = [50, 60]
    timers._timings["c"] = [70]
    assert timers.median("a") == 20
    assert timers.median("b") == 55
    assert timers.median("c") == 70.0

# Generated at 2022-06-13 18:33:06.412985
# Unit test for method min of class Timers
def test_Timers_min():
    """
    Test method min of class Timers
    """
    timer = Timers()
    timer.add("timer1", 6)
    timer.add("timer1", 2)
    timer.add("timer1", 5)
    timer.add("timer2", 3)
    assert timer.min("timer1") == 2
    assert timer.min("timer2") == 3
    assert timer.total("timer1") == 13
    assert timer.total("timer2") == 3
    timer = Timers()
    timer.add("timer1", 6)
    timer.add("timer1", 2)
    timer.add("timer1", 5)
    timer.add("timer2", 3)
    assert timer.min("timer1") == 2
    assert timer.min("timer2") == 3

# Generated at 2022-06-13 18:33:10.554773
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add("1", 1)
    t.add("1", 2)
    t.add("1", 3)

    assert t.median("1")==2.0


# Generated at 2022-06-13 18:33:20.238093
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('timers_mean_test', 2)
    assert isinstance(timers.mean('timers_mean_test'), float)

# Generated at 2022-06-13 18:33:31.236479
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()
    timers.add("foo", 0.1)
    timers.add("foo", 0.2)
    timers.add("foo", 0.3)
    assert timers.median("foo") == 0.2
    timers.add("foo", 0.4)
    assert timers.median("foo") == 0.25
    timers.add("bar", 0.5)
    timers.add("bar", 0.6)
    assert timers.median("bar") == 0.55
    timers.add("bar", 0.7)
    assert timers.median("bar") == 0.6


# Generated at 2022-06-13 18:33:36.113641
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add('abc', 1)
    timers.add('abc', 2)
    timers.add('abc', 4)
    timers.add('abd', 5)
    timers.add('abd', 5)
    assert timers.median('abc') == 2
    assert timers.median('abd') == 5

# Generated at 2022-06-13 18:33:39.715794
# Unit test for method min of class Timers
def test_Timers_min():
    """Test min of Timers"""
    timers = Timers()
    for i in range(1000):
        timers.add("test", i)
    assert timers.min("test") == 0


# Generated at 2022-06-13 18:33:44.433859
# Unit test for method min of class Timers
def test_Timers_min():
    """Test Timers.min()"""
    timers = Timers()
    timers.add('a', 1)
    assert timers.min('a') == 1
    timers.add('a', 2)
    assert timers.min('a') == 1
    timers.add('a', -1)
    assert timers.min('a') == -1

# Generated at 2022-06-13 18:33:48.381068
# Unit test for method max of class Timers
def test_Timers_max():
    # Create a Timers object
    timers = Timers()

    # Add a few timings
    timers.add("a", 1)
    timers.add("a", 5)
    timers.add("a", 2)

    # Calculate the maximum values
    max_a = timers.max("a")

    # Check the result
    assert max_a == 5, max_a

# Generated at 2022-06-13 18:33:52.960703
# Unit test for method max of class Timers
def test_Timers_max():
    """
    Unit test for method max of class Timers
    """
    timers = Timers()
    # no data available
    with pytest.raises(KeyError):
        timers.max("random_key")
    # data available
    timers.add("key", 1)
    timers.add("key", 2)
    assert timers.max("key") == 2

# Generated at 2022-06-13 18:34:05.478170
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the median of class Timers"""
    timers = Timers()
    assert timers.median("test") == 0
    timers.add("test", 5)
    assert timers.median("test") == 5

    timers.add("test", 10)
    assert timers.median("test") == 7.5
    timers.add("test", 15)
    assert timers.median("test") == 10

    timers.add("test2", 5)
    assert timers.median("test2") == 5
    timers.add("test2", 10)
    assert timers.median("test2") == 7.5


# Generated at 2022-06-13 18:34:11.837266
# Unit test for method min of class Timers
def test_Timers_min():
    """Test the min method of class Timers"""
    timers = Timers()
    assert timers.min("name") == 0
    with pytest.raises(KeyError):
        timers.min("not_found")
    timers.add("name", 0)
    assert timers.min("name") == 0
    timers.add("name", 1)
    assert timers.min("name") == 0
    timers.add("name", -1)
    assert timers.min("name") == -1

# Test method max of class Timers

# Generated at 2022-06-13 18:34:18.239359
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min('name') == 0
    timers.add('name', 1)
    assert timers.min('name') == 1
    timers.add('name', 2)
    assert timers.min('name') == 1
    assert timers.min('no_name') == 0


# Generated at 2022-06-13 18:34:27.846203
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers._timings = dict(test=[10, 20, 30])
    result = timers.mean("test")
    assert result == 20

# Generated at 2022-06-13 18:34:30.956105
# Unit test for method mean of class Timers
def test_Timers_mean():
    # create an instance of Timers
    test_timers = Timers()
    # add a timer named a with 1 value
    test_timers.add("a", 1)
    assert test_timers.mean("a") == 1

# Generated at 2022-06-13 18:34:36.091516
# Unit test for method median of class Timers
def test_Timers_median():
    # Init timers
    t = Timers()
    t.add("test", 0)
    t.add("test", 4)
    t.add("test", 4)
    t.add("test", 13)
    t.add("test", 13)
    t.add("test", 13)
    t.add("test", 13)
    t.add("test", 13)
    t.add("test", 13)
    t.add("test", 13)

    # Test
    assert t.median("test") == 10

# Generated at 2022-06-13 18:34:38.904078
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers({"s1": 1})
    t.add("s1", 2)
    t.add("s1", 3)
    t.add("s1", 4)
    assert t.max("s1") == 4



# Generated at 2022-06-13 18:34:43.283885
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    import math
    from hypothesis import assume, given, strategies as st
    from .timer import Timer

    @given(st.floats(min_value=0))
    def _test_mean(value: float) -> None:
        """Test mean function of timers"""
        timer = Timer("Timer")
        assume(math.isfinite(value))
        timer.start()
        timer.stop(value)
        assert timer.timers.mean("Timer") == value

    _test_mean()

# Generated at 2022-06-13 18:34:48.783518
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers._timings = {'test': [1, 2, 3, 4]}
    result = timers.median('test')
    assert result == 2.5
    result = timers.median('nonexistent')
    assert result is None

# Generated at 2022-06-13 18:34:55.015611
# Unit test for method mean of class Timers
def test_Timers_mean():
    """
    Unit test of method mean of class Timers
    """
    # Initiate the object to be tested
    timers = Timers()
    # Add some values
    timers.add('test', 5.0)
    timers.add('test', 2.0)
    timers.add('test', 3.0)
    # Check that the mean is correct
    assert(timers.mean('test') == 3.0)


# Generated at 2022-06-13 18:35:00.960933
# Unit test for method min of class Timers
def test_Timers_min():
    actual_output = Timers()
    actual_output.add("name", 0.001)
    actual_output.add("name", 0.0005)
    actual_output.add("name", 0.002)
    expected_output = 0.0005
    assert actual_output.min("name") == expected_output


# Generated at 2022-06-13 18:35:05.401973
# Unit test for method max of class Timers
def test_Timers_max():
    # Create a Timers object
    t = Timers()
    # Test if method max works properly
    try:
        t.max("yo")
    except KeyError:
        pass
    t.add("yo", 1)
    assert t.max("yo") == 1


# Generated at 2022-06-13 18:35:10.041394
# Unit test for method max of class Timers
def test_Timers_max():
    """
    Test for max method of Timers class

    Doctest:
    >>> from casymda.visualization.timers import Timers
    >>> t = Timers()
    >>> t.add("a", 1)
    >>> t.add("a", 4)
    >>> t.add("b", 5)
    >>> t.data
    {'a': 5, 'b': 5}
    >>> t.max("a")
    4.0
    >>> t.max("b")
    5.0
    """
    pass

# Generated at 2022-06-13 18:35:21.240863
# Unit test for method max of class Timers
def test_Timers_max():
    """Test the max method of the Timers class"""
    expected = 42.0
    timers = Timers()
    timers.add("mytimer", 1)
    timers.add("mytimer", 42)
    actual = timers.max("mytimer")
    assert actual == expected

# Generated at 2022-06-13 18:35:23.828145
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("test", 5)
    assert timers.max("test") == 5


# Generated at 2022-06-13 18:35:28.690801
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    assert timers.max('test') == 3
    assert timers.apply(lambda values: max(values or [0]), name='test') == 3

# Generated at 2022-06-13 18:35:31.593466
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("time", 1)
    t.add("time", 3)
    x = t.max('time')
    print(x)
    assert x == 3, x


# Generated at 2022-06-13 18:35:37.455677
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    assert timers.mean("none") == 0.0
    timers.add("single", 1.0)
    assert timers.mean("single") == 1.0
    timers.add("two", 1.0)
    timers.add("two", 2.0)
    assert timers.mean("two") == 1.5

# Generated at 2022-06-13 18:35:38.625298
# Unit test for method mean of class Timers
def test_Timers_mean():
    pass  # pragma: no cover

# Generated at 2022-06-13 18:35:41.249481
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('a',2)
    t.add('a',1)
    

    assert(t.min('a') == 1)


# Generated at 2022-06-13 18:35:45.433830
# Unit test for method max of class Timers
def test_Timers_max():
    # Given
    timers = Timers()
    name = 'toto'

    # When
    timers.add(name, 2)
    timers.add(name, 4)
    timers.add(name, 6)

    # Then
    assert(timers.max(name) == 6)


# Generated at 2022-06-13 18:35:51.256871
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median"""
    timer = Timers()
    timer.add("name", 10)
    timer.add("name", 100)
    timer.add("name", 1000)
    assert timer.median("name") == 10, "Median of 3 values fail"
    timer.add("name", 10000)
    assert timer.median("name") == 1000, "Median of 4 values fail"

# Generated at 2022-06-13 18:35:56.234704
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test method mean"""
    timers = Timers()
    timers.add('foo', 0)
    timers.add('foo', 3)
    timers.add('foo', 4)
    assert timers.mean('foo') == 3

    timers.add('bar', 1)
    assert timers.mean('bar') == 1

    with pytest.raises(KeyError):
        timers.mean('baz')


# Generated at 2022-06-13 18:36:09.483901
# Unit test for method mean of class Timers
def test_Timers_mean():
    _ = Timers()
    assert _.mean('test') == 0.0
    _.add('test', 1.0)
    _.add('test', 2.0)
    assert _.mean('test') == 1.5
    _.add('test', 3.0)
    assert _.mean('test') == 2.0


# Generated at 2022-06-13 18:36:15.912717
# Unit test for method median of class Timers
def test_Timers_median():
    """Test method median in class Timers"""
    # Initialize instance of Timers
    timers = Timers()
    # Add values to timers
    timers.add("test", 1)
    timers.add("test", 3)
    timers.add("test", 5)
    # Test method median
    assert timers.median("test") == 3


# Generated at 2022-06-13 18:36:19.094667
# Unit test for method mean of class Timers
def test_Timers_mean():
    timer = Timers()
    timer.add('foo', 42)
    assert timer.mean('foo') == 42

# Generated at 2022-06-13 18:36:22.794783
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    tc = Timers()
    tc.add('y', 1)
    tc.add('y', 2)
    tc.add('y', 3)
    assert tc.median('y') == 2

# Generated at 2022-06-13 18:36:27.116061
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()

    # Check that timer with no values returns 0
    assert timers.min("timer1") == 0

    # Check that timer with a few values returns the minimum
    timers._timings["timer2"] = [1.0, 2.5, 0.5]
    assert timers.min("timer2") == 0.5



# Generated at 2022-06-13 18:36:34.974145
# Unit test for method median of class Timers
def test_Timers_median():  # pragma: no cover
    t = Timers()
    t._timings['test'] = [1,2,3]
    assert t.median('test') == 2
    t._timings['test'] = [1,1,1,1]
    assert t.median('test') == 1
    t._timings['test'] = [1]
    assert t.median('test') == 1
    t._timings.clear()
    assert t.median('test') == 0
    assert t.median('test2') == 0

# Generated at 2022-06-13 18:36:35.605522
# Unit test for method median of class Timers
def test_Timers_median():
    pass

# Generated at 2022-06-13 18:36:37.387377
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("test", 1)
    t.add("test", 2)
    assert t.mean("test") == 1.5

# Generated at 2022-06-13 18:36:44.495798
# Unit test for method max of class Timers
def test_Timers_max():
    """Test the method max of class Timers"""
    t = Timers()
    name = "test"
    t.add(name=name, value=1)
    t.add(name=name, value=2)
    t.add(name=name, value=3)
    assert t.max(name=name) == 3


# Generated at 2022-06-13 18:36:47.913966
# Unit test for method max of class Timers
def test_Timers_max():
    # Create object
    timers = Timers()

    # Define values
    values = [ 1, 5, -3, 4 ]

    # Add values
    for value in values:
        timers.add(name = 'test', value = value)

    # Check result
    assert timers.max(name = 'test') == max(values)

# Generated at 2022-06-13 18:36:56.182514
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("foo", 12)
    assert timers.max("foo") == 12
    assert timers.min("foo") == 12


# Generated at 2022-06-13 18:37:01.915317
# Unit test for method max of class Timers
def test_Timers_max():
    """Test Timers class max method"""
    timers = Timers()
    timers.add('mytimer', 42)
    timers.add('othertimer', 24)
    assert timers.max('mytimer') == 42
    assert timers.max('othertimer') == 24
    assert timers.data['mytimer'] == 42
    assert timers.data['othertimer'] == 24

# Generated at 2022-06-13 18:37:05.209261
# Unit test for method max of class Timers
def test_Timers_max():
    timer = Timers()
    timer.add("test", 42)
    assert timer.max("test") == 42
    timer.add("test", 69)
    assert timer.max("test") == 69

# Generated at 2022-06-13 18:37:07.371821
# Unit test for method max of class Timers
def test_Timers_max():
    import statistics
    timers = Timers()
    timers.add('test', 10)
    timers.add('test', 20)
    timers.add('test', 30)
    assert timers.max('test') == max(10,20,30)


# Generated at 2022-06-13 18:37:14.541843
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test method mean of class Timers"""
    test_timers = Timers()
    test_timers["x"] = 1
    test_timers["y"] = 2
    test_timers["z"] = 3
    assert test_timers.mean("x") == 1
    assert test_timers.mean("y") == 2
    assert test_timers.mean("z") == 3


# Generated at 2022-06-13 18:37:18.705531
# Unit test for method min of class Timers
def test_Timers_min():
    """Test if the minimum is being calculated correctly

    ========= ==== ========= ========= ========= ========= ========= =========
    Values     min Median     Mean      Max       Standard
    ========= ==== ========= ========= ========= ========= ========= =========
    [1, 2, 3]  1    2.0       2.0       3         0.816497
    [1, 2]     1    1.5       1.5       2         0.707107
    [1]        1    1.0       1.0       1         NaN
    []         0    NaN       NaN       NaN       NaN
    ========= ==== ========= ========= ========= ========= ========= =========

    """
    # Prepare test data
    data: Dict[str, List[float]] = collections.defaultdict(list)

# Generated at 2022-06-13 18:37:22.609284
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('min', 3)
    assert timers.min('min') == 3
    timers.add('min', 1)
    assert timers.min('min') == 1
    assert timers.apply(min, 'min') == 1


# Generated at 2022-06-13 18:37:28.311272
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("t1", 1)
    timers.add("t1", 2)
    timers.add("t1", 3)
    assert timers.median("t1") == 2
    assert timers.median("t2") == 0

# Generated at 2022-06-13 18:37:30.259411
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('min', 1)
    timers.add('min', 2)
    timers.add('min', 3)
    assert timers.min('min') == 1

# Generated at 2022-06-13 18:37:37.164934
# Unit test for method max of class Timers
def test_Timers_max():
    assert (
        Timers()
        .add("timer", value=1.0)
        .add("timer2", value=2.0)
        .add("timer", value=3.0)
        .max("timer")
        == 3.0
    )

