

# Generated at 2022-06-13 18:27:45.472751
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timers = Timers()
    timers.add("foo", 10.0)
    assert timers.min("foo") == 10.0, "should get 10.0"
    timers.add("foo", 9.0)
    assert timers.min("foo") == 9.0, "should get 9.0"
    timers.add("foo", 11.0)
    assert timers.min("foo") == 9.0, "should get 9.0"
    timers.add("foo", 10.0)
    assert timers.min("foo") == 9.0, "should get 9.0"
    timers.add("foo", 10.0)
    assert timers.min("foo") == 9.0, "should get 9.0"
    timers.add("foo", 10.0)

# Generated at 2022-06-13 18:27:47.878966
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add("foo", 2)
    t.add("bar", 3)
    t.min("foo") == 2
    t.min("bar") == 3
    t.min("qux")



# Generated at 2022-06-13 18:27:53.396716
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('timers', 0.0)
    timers.add('timers', 1.0)
    timers.add('timers', 2.0)
    assert timers.min('timers') == 0.0


# Generated at 2022-06-13 18:28:01.575693
# Unit test for method mean of class Timers
def test_Timers_mean():
    tim = Timers()
    tim.add("test", 1)
    tim.add("test", 2)
    tim.add("test", 3)
    tim.add("test", 4)
    tim.add("test", 5)
    tim.add("test", 6)
    mean = tim.mean("test")

    if mean != 3.5:
        raise ValueError(f"Mean value is {mean} instead of 3.5")

# Generated at 2022-06-13 18:28:04.009285
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers._timings['foo'] = [1,2]
    assert timers.min('foo') == 1

# Generated at 2022-06-13 18:28:11.756860
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add("first", 1.0)
    timers.add("first", 2.0)
    timers.add("second", 3.0)
    timers.add("second", 4.0)
    timers.add("second", 5.0)
    assert timers.mean("first") == 1.5
    assert timers.mean("second") == 4.0
    assert timers.mean("missing") == 0.0

# Generated at 2022-06-13 18:28:15.296856
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the median method of class Timers"""
    # Create new instance of Timers
    timers = Timers()
    # Add timing values
    timers.add("timer1", 1.0)
    timers.add("timer1", 2.0)
    timers.add("timer1", 3.0)
    # Check value
    assert timers.median("timer1") == 2.0

# Generated at 2022-06-13 18:28:21.993209
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test of .mean()"""
    timers = Timers()
    timers.add("test", 1)
    assert timers.mean("test") == 1.0
    timers.add("test", 2)
    assert timers.mean("test") == 1.5
    with pytest.raises(KeyError):
        timers.mean("test2")

# Generated at 2022-06-13 18:28:28.998089
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    assert t.max("n1") == 0
    t.add("n1", 2.5)
    assert t.max("n1") == 2.5
    t.add("n2", 1.0)
    assert t.max("n2") == 1.0
    t.add("n2", 2.3)
    assert t.max("n2") == 2.3
    t.add("n2", 3.9)
    assert t.max("n2") == 3.9


# Generated at 2022-06-13 18:28:32.723941
# Unit test for method min of class Timers
def test_Timers_min():
    # Given
    timers = Timers()
    expected = []
    # When
    result = timers.min("")
    # Then
    assert result == expected
    assert not timers


# Generated at 2022-06-13 18:28:43.817973
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method Timers.min()"""
    timers = Timers()
    timers.add("time", 0)
    assert timers.min("time") == 0
    timers.add("time", 1)
    assert timers.min("time") == 0
    timers.add("time", 2)
    assert timers.min("time") == 0
    timers.add("time", 3)
    assert timers.min("time") == 0
    timers.add("time", 4)
    assert timers.min("time") == 0
    timers.add("time", 5)
    assert timers.min("time") == 0
    timers.add("time", 6)
    assert timers.min("time") == 0


# Generated at 2022-06-13 18:28:50.396521
# Unit test for method median of class Timers
def test_Timers_median():
    d = Timers()
    assert d.median("foo") == 0
    d.add("foo", 1)
    assert d.median("foo") == 1
    d.add("foo", 2)
    assert d.median("foo") == 1.5
    d.add("foo", 3)
    assert d.median("foo") == 2



# Generated at 2022-06-13 18:28:59.181804
# Unit test for method median of class Timers
def test_Timers_median():
    """test_Timers_median"""
    import random
    test_dict = Timers()
    for i in range(random.randrange(30)):
        test_dict.add("test_1", random.randrange(30))
        test_dict.add("test_2", random.randrange(30))
        test_dict.add("test_3", random.randrange(30))
    test_list = [test_dict.count("test_1"), test_dict.count("test_2"), test_dict.count("test_3")]
    test_list.sort()
    test_list = [test_dict.total("test_1"), test_dict.total("test_2"), test_dict.total("test_3")]
    test_list.sort()

# Generated at 2022-06-13 18:29:08.923190
# Unit test for method mean of class Timers
def test_Timers_mean():
    lst = [56, 23, 66, 78, 34, 97, 24, 67, 34, 89, 76, 78, 34, 90, 67, 23]
    timers = Timers()
    for ele in lst:
        timers.add(ele, ele)
    avg = 0
    for ele in lst:
        avg += ele
    avg = avg / len(lst)
    assert timers.mean(lst[0]) == avg

# Generated at 2022-06-13 18:29:17.956662
# Unit test for method min of class Timers
def test_Timers_min():
    # Test empty input
    timers = Timers()
    assert timers.min("test") == 0

    # Test not computed
    timers = Timers()
    timers.data["test"] = 10
    assert timers.min("test") == 0

    # Test computed
    timers = Timers()
    timers._timings["test"] = [1, 2, 3]
    assert timers.min("test") == 1

    # Test computed
    timers = Timers()
    timers._timings["test"] = []
    assert timers.min("test") == 0



# Generated at 2022-06-13 18:29:22.117979
# Unit test for method max of class Timers
def test_Timers_max():
    """Test method max of the class Timers"""
    timers = Timers()
    name = "timer_name"
    for i in range(100):
        timers.add(name=name, value=i)
    assert timers.max(name=name) == 99


# Generated at 2022-06-13 18:29:26.811135
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("foo", 0.1)
    timers.add("foo", 0.2)
    timers.add("bar", 0.3)
    assert timers.min("foo") == 0.1
    assert timers.min("bar") == 0.3
    assert timers.min("foobar") == 0.0


# Generated at 2022-06-13 18:29:36.202133
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    assert timers.mean("t") == 0.0
    timers.add("t", 0.5)
    assert timers.mean("t") == 0.5
    timers.add("t", 0.75)
    assert timers.mean("t") == 0.625
    timers.add("t", 0.0)
    assert timers.mean("t") == 0.5


# Generated at 2022-06-13 18:29:41.448101
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    timers = Timers()
    timers.add("a", 1)
    timers.add("b", 2)
    timers.add("b", 1)
    timers.add("c", 3)
    assert timers.min("a") == 1
    assert timers.min("b") == 1



# Generated at 2022-06-13 18:29:47.681859
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add(name='timer1', value=10)
    timers.add(name='timer1', value=20)
    timers.add(name='timer1', value=30)
    timers.add(name='timer1', value=40)
    assert timers.median(name='timer1') == 25
    return

# Generated at 2022-06-13 18:29:59.137121
# Unit test for method mean of class Timers
def test_Timers_mean():
    # verify the Timers class with a simple test case
    myTimers = Timers()
    assert myTimers.mean(name = "test") == 0.0
    myTimers.add(name = "test", value = 1.0)
    assert myTimers.mean(name = "test") == 1.0
    myTimers.add(name = "test", value = 0.1)
    assert myTimers.mean(name = "test") == 0.55
    return True


# Generated at 2022-06-13 18:30:07.394132
# Unit test for method median of class Timers
def test_Timers_median():
    t = Timers()
    t.add("a", 1.0)
    assert t.median("a") == 1.0

    t = Timers()
    t.add("a", 1.0)
    t.add("a", 2.0)
    assert 1.0 <= t.median("a") <= 2.0

    t = Timers()
    t.add("a", 1.0)
    t.add("a", 2.0)
    t.add("a", 3.0)
    assert 2.0 <= t.median("a") <= 3.0

    t = Timers()
    t.add("a", 1.0)
    t.add("a", 2.0)
    t.add("a", 3.0)
    t.add("a", 4.0)
   

# Generated at 2022-06-13 18:30:10.306651
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    timers = Timers()
    timers.add('a', 1)
    timers.add('a', 2)
    timers.add('a', 3)
    assert timers.median('a') == 2

# Generated at 2022-06-13 18:30:16.942627
# Unit test for method max of class Timers
def test_Timers_max():
    """Test method max of class Timers """
    timers = Timers()
    timers.add('first', 1)
    timers.add('second', 2)
    timers.add('third', 3)
    timers.add('fourth', 4)
    assert timers['first'] == 4
    assert timers.max('second') == 4
    assert isinstance(timers['first'], float)
    assert timers.max('second') == 4.0
    assert timers.max('fourth') == 4
    assert timers.max('fourth') == 4.0

# Generated at 2022-06-13 18:30:25.273174
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.data.clear()
    timers._timings.clear()
    timers._timings['foo'] = [1, 2, 3]
    assert timers.max('foo') == 3
    timers._timings['foo'] = [3, 2, 1]
    assert timers.max('foo') == 3
    timers._timings['foo'] = [1, 2, 1]
    assert timers.max('foo') == 2


# Generated at 2022-06-13 18:30:30.023692
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    timers = Timers()
    assert timers.min("i") == 0
    timers.add("i", 1)
    assert timers.min("i") == 1
    timers.add("i", 2)
    assert timers.min("i") == 1
    timers.add("i", 0.5)
    assert timers.min("i") == 0.5

# Generated at 2022-06-13 18:30:35.897607
# Unit test for method median of class Timers
def test_Timers_median():
    """Test for method median of class Timers"""
    timer = Timers()
    timer.add("Test", 0.0)
    timer.add("Test", 1.0)
    timer.add("Test", 2.0)
    timer.add("Test", 3.0)
    assert 1.5 == timer.median("Test")


# Generated at 2022-06-13 18:30:38.364489
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("runtime",1)
    assert timers.median("runtime") == 1
    timers.add("runtime",2)
    assert timers.median("runtime") == 1.5

# Generated at 2022-06-13 18:30:41.765870
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()

    timers.add("name", 5)
    timers.add("name", 4)
    timers.add("name", 3)
    timers.add("name", 2)
    timers.add("name", 1)

    assert timers.min("name") == 1


# Generated at 2022-06-13 18:30:46.526842
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("a", 5)
    t.add("a", 9)
    t.add("b", 3)
    assert t.max("a") == 9
    assert t.max("b") == 3


# Generated at 2022-06-13 18:30:58.274251
# Unit test for method max of class Timers
def test_Timers_max():
    """Test the max method of the Timers class"""
    d = Timers()
    d.add('a', 1)
    d.add('b', 2)
    assert d.max('a') == 1
    assert d.max('b') == 2
    try:
        d.max('c')
        assert False
    except KeyError:
        pass

# Generated at 2022-06-13 18:31:03.645903
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("foo", 1)
    assert timers.median("foo") == 1

    timers.add("foo", 3)
    assert timers.median("foo") == 2

    timers.add("foo", 4)
    assert timers.median("foo") == 2.5

    with pytest.raises(KeyError):
        timers.median("bar")

# Generated at 2022-06-13 18:31:07.096075
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the method mean() for Timers class"""
    t = Timers()
    t.add("timer1", 1)
    t.add("timer1", 2)
    t.add("timer2", 3)

    assert t.mean("timer1") == 1.5
    assert t.mean("timer2") == 3


# Generated at 2022-06-13 18:31:09.267082
# Unit test for method max of class Timers
def test_Timers_max():
    # Step 1 - create object
    timers = Timers()

    # Step 2 - add data
    timers.add("a", 4)
    timers.add("a", 7)
    timers.add("a", 4)

    # Step 3 - verify ouput
    assert timers.max("a") == 7

# Generated at 2022-06-13 18:31:12.224984
# Unit test for method median of class Timers
def test_Timers_median():
    """ Test method median of class Timers """
    timers = Timers()
    timers.add('test', 5.0)
    assert timers.median('test') == 5.0

    timers.add('test', 2.0)
    assert timers.median('test') == 3.5

    timers.add('test', 10.0)
    assert timers.median('test') == 5.0

# Generated at 2022-06-13 18:31:15.624104
# Unit test for method min of class Timers
def test_Timers_min():
    """Tests correct functionality for method min of class Timers"""
    a = Timers()
    a.add("timing1", 0.01)
    a.add("timing2", 0.02)
    a.add("timing2", 0.04)
    assert a.min("timing1") == 0.01
    assert a.min("timing2") == 0.02
    assert a.min("timing3") == 0

# Generated at 2022-06-13 18:31:24.245531
# Unit test for method median of class Timers
def test_Timers_median():
    """Test definition at the end of file"""
    timers = Timers()
    assert timers.median("timer_1") == 0
    timers.add("timer_1", 1)
    assert timers.median("timer_1") == 1
    timers.add("timer_1", 2)
    assert timers.median("timer_1") == 1.5
    timers.add("timer_1", 3)
    assert timers.median("timer_1") == 2
    timers.add("timer_1", 4)
    assert timers.median("timer_1") == 2.5


# Generated at 2022-06-13 18:31:29.928903
# Unit test for method max of class Timers
def test_Timers_max():
    """Test for Timers.max method"""
    timers = Timers()
    timers.add("test", 33.3)
    timers.add("test", 66.6)
    assert timers.max("test") == 66.6, "Timers.max did not return correct time"

# Generated at 2022-06-13 18:31:41.782353
# Unit test for method min of class Timers
def test_Timers_min():
    dummy = Timers([])
    assert dummy.total("dummy") == 0
    assert dummy.min("dummy") == 0
    dummy.add("dummy", 1)
    assert dummy.total("dummy") == 1
    assert dummy.min("dummy") == 1
    dummy.add("dummy", 2)
    assert dummy.total("dummy") == 3
    assert dummy.min("dummy") == 1
    dummy.add("dummy", 0.5)
    assert dummy.total("dummy") == 3.5
    assert dummy.min("dummy") == 0.5
    dummy.add("dummy", -1)
    assert dummy.total("dummy") == 2.5
    assert dummy.min("dummy") == -1
    dummy.add("dummy", -1)
    assert dummy.total

# Generated at 2022-06-13 18:31:46.609507
# Unit test for method max of class Timers
def test_Timers_max():
    """Test for Timers"""
    timers = Timers()

    timers.add("name", 1.0)

    assert isinstance(timers, Timers)
    assert timers.max("name") == 1.0


# Generated at 2022-06-13 18:32:06.926167
# Unit test for method median of class Timers
def test_Timers_median():
    import numpy as np
    from random import Random
    random = Random(1)  # pylint: disable=invalid-name

    for _ in range(1000):
        timer = Timers()
        values = [random.random() for _ in range(random.randrange(1, 1000))]
        [timer.add('test', value) for value in values]

        assert np.isclose(timer.median('test'), np.median(values))

# Generated at 2022-06-13 18:32:12.377736
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('t1', 2.0)
    assert timers.min('t1') == 2.0
    timers.clear()
    assert timers.min('t1') == 0.0
"""Classes for customizing performance counters"""

# Standard library imports
from abc import ABC, abstractmethod
from typing import Any, Dict

# Local imports
from .timers import Timers



# Generated at 2022-06-13 18:32:19.372303
# Unit test for method mean of class Timers
def test_Timers_mean():
    # Create Timers object
    timers = Timers()

    # Add two values for timer "test"
    timers.add("test", 1)
    timers.add("test", 2)

    # Compute mean
    mean = timers.mean("test")

    # Check correct mean value
    print(f"\nMean value of timer 'test': {mean}")
    assert mean == 1.5

if __name__ == "__main__":
    test_Timers_mean()

# Generated at 2022-06-13 18:32:24.650565
# Unit test for method median of class Timers
def test_Timers_median():
    assert Timers().median("foo") == 0.0

    timers = Timers()
    timers.add("foo", 1.0)
    assert timers.median("foo") == 1.0

    timers.add("foo", 2.0)
    assert timers.median("foo") == 1.5

    timers.clear()
    timers.add("foo", 2.0)
    timers.add("foo", 1.0)
    assert timers.median("foo") == 1.5

# Generated at 2022-06-13 18:32:27.424846
# Unit test for method min of class Timers
def test_Timers_min():
    """Test the Timers.min method"""
    timer = Timers({"test": 3})
    assert timer.min("test") == 3


# Generated at 2022-06-13 18:32:30.161667
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    for i in range(100):
        timers.add(name = 'timings', value = i)
    assert timers.max('timings') == 99

# Generated at 2022-06-13 18:32:35.492018
# Unit test for method median of class Timers
def test_Timers_median():
    """Test median()"""

    # Create an empty Timers instance and check whether the median of an unknown element is zero
    timers = Timers()
    assert timers.median("unknown") == 0.0

    # Create a Timers instance, add three values and check whether the median is as expected
    timers = Timers()
    timers.add("name", 1.0)
    timers.add("name", 2.0)
    timers.add("name", 3.0)
    assert timers.median("name") == 2.0

# Generated at 2022-06-13 18:32:38.135325
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("a", 1)
    timers.add("a", 2)
    assert timers.median("a") == 1.5

# Generated at 2022-06-13 18:32:43.419042
# Unit test for method max of class Timers
def test_Timers_max():
    """Test method max of class Timers"""
    t = Timers()
    t.add("a", 2)
    t.add("b", 1)
    t.add("a", 3)
    assert t.max("a") == 3
    assert t.max("b") == 1

# Generated at 2022-06-13 18:32:53.973891
# Unit test for method min of class Timers
def test_Timers_min():
    """Tests for the 'min' method of class Timers"""
    # Inputs
    name = "name"
    t = Timers()
    # Show that the minimum value of empty timers is 0
    assert t.min(name) == 0
    # Add two timers. Also check that '_timings' and 'data' are updated
    assert t._timings == {}
    assert t.data == {}
    t.add(name, 1)
    t.add(name, 2)
    assert t._timings == {"name": [1, 2]}
    assert t.data == {"name": 3}
    # Show that the minimum value is updated
    assert t.min(name) == 1


# Generated at 2022-06-13 18:33:27.022747
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("duration", 2)
    timers.add("duration", 1)
    assert timers.max("duration") == 2


# Generated at 2022-06-13 18:33:32.812373
# Unit test for method mean of class Timers
def test_Timers_mean():
    from pytest import approx

    timers = Timers()
    timers.add("timer_1", 0.5)
    timers.add("timer_2", 1)
    timers.add("timer_1", 1.5)
    assert timers.mean("timer_1") == approx(1.0)
    assert timers.mean("timer_2") == approx(1.0)


# Generated at 2022-06-13 18:33:35.582553
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    t = Timers()
    t.add("test", 1)
    t.add("test", 1)
    t.add("test", 1)
    assert t.mean("test") == 1.


# Generated at 2022-06-13 18:33:43.744258
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min("test") == 0
    timers.add("test", 1)
    assert timers.min("test") == 1
    timers.add("test", 2)
    assert timers.min("test") == 1
    timers.add("test", 3)
    assert timers.min("test") == 1
    timers.add("test", 4)
    assert timers.min("test") == 1
    timers.add("test", 5)
    assert timers.min("test") == 1
    timers.add("test", 0)
    assert timers.min("test") == 0


# Generated at 2022-06-13 18:33:51.908813
# Unit test for method max of class Timers
def test_Timers_max():
    t1 = Timers()
    assert t1.max("t1") == 0
    t1.add("t1", 3.2)
    assert t1.max("t1") == 3.2
    t1.add("t1", 1.2)
    assert t1.max("t1") == 3.2
    assert t1.apply(lambda x: max(x), "t1") == 3.2
    t2 = Timers()
    assert t2.max("t2") == 0
    t2["t2"] = 5.6      # Test TypeError


# Generated at 2022-06-13 18:33:56.410492
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('test', 2.5)
    timers.add('test', 4.5)
    timers.add('test', 3.5)
    assert timers.max('test') == 4.5


# Generated at 2022-06-13 18:34:00.622989
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add('a',1)
    t.add('a',2)
    t.add('a',3)
    t.add('a',4)
    t.add('a',5)
    t.add('a',6)
    assert t.mean('a') == 3.5


# Generated at 2022-06-13 18:34:10.974870
# Unit test for method min of class Timers
def test_Timers_min():
    # Empty dictionary
    timers = Timers()
    assert timers.min("foo") == 0.0

    # Non empty dictionary
    timers = Timers()
    timers.add("foo", 0.0)
    assert timers.min("foo") == 0.0

    timers = Timers()
    timers.add("foo", 1.0)
    assert timers.min("foo") == 1.0

    timers = Timers()
    timers.add("foo", 1.0)
    timers.add("foo", 2.0)
    assert timers.min("foo") == 1.0

    timers = Timers()
    timers.add("foo", 2.0)
    timers.add("foo", 1.0)
    assert timers.min("foo") == 1.0

# Generated at 2022-06-13 18:34:20.203002
# Unit test for method max of class Timers
def test_Timers_max():
    """max function works correctly"""
    timers = Timers()
    assert timers.max('test') == 0
    timers.add('test', 1)
    assert timers.max('test') == 1
    timers.add('test', 2)
    assert timers.max('test') == 2
    try:
        timers.max('fail')
        assert False, 'Not raising exception'
    except KeyError:
        assert True

# Generated at 2022-06-13 18:34:29.841084
# Unit test for method median of class Timers
def test_Timers_median():
    """Test statistics.median"""
    assert Timers().median("foo") == 0.0
    assert Timers().median(123) == 0.0
    assert Timers({}).median(123) == 0.0
    assert Timers({123: 0.0}).median(123) == 0.0
    assert Timers({123: 1.0}).median(123) == 1.0
    assert Timers({123: 1.0}).median(234) == 0.0
    assert Timers({"foo": 1.0}).median("foo") == 1.0
    assert Timers({"foo": 1.0}).median("bar") == 0.0
    assert Timers({"foo": [1.0]}).median("foo") == 1.0

# Generated at 2022-06-13 18:35:36.223876
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    assert timers.min('foo') == 0
    timers._timings['foo'] = [1, 2]
    assert timers.min('foo') == 1
    assert timers.min('bar') == 0
    assert timers.min('spam') != 0

# Generated at 2022-06-13 18:35:39.656942
# Unit test for method min of class Timers
def test_Timers_min():
    x = Timers()
    x.add("a", 1)
    x.add("a", 2)
    assert x.min("a") == 1

# Generated at 2022-06-13 18:35:44.443688
# Unit test for method max of class Timers
def test_Timers_max():
    """Test Timers.max() method"""
    timer = Timers()
    assert timer.max(name="test") == 0
    timer.add(name="test", value=1)
    timer.add(name="test", value=2)
    timer.add(name="test", value=2)
    timer.add(name="test", value=3)
    timer.add(name="test", value=5)
    assert timer.max(name="test") == 5
    assert timer.max(name="test") == 5

# Generated at 2022-06-13 18:35:55.300177
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the median method of class Timers."""

    from pycalcmodel.core import Timers

    timers = Timers()
    assert len(timers) == 0
    median = timers.median("key")
    assert median == 0
    with pytest.raises(KeyError):
        timers.median("key2")

    timers.add("key", 1.0)
    timers.add("key", 3.0)
    timers.add("key", 2.0)
    assert timers["key"] == 6.0
    assert len(timers) == 1
    median = timers.median("key")
    assert median == 2.0

    timers.add("key2", -1.0)
    timers.add("key2", 0.0)
    assert timers["key2"] == -1.0

# Generated at 2022-06-13 18:36:02.410194
# Unit test for method median of class Timers
def test_Timers_median():
    """
    Test for Timers.median
    See <https://en.wikipedia.org/wiki/Median#Example>
    """
    timers = Timers()
    timers.add("a", 11)
    timers.add("a", 6)
    timers.add("a", 7)
    timers.add("a", 8)
    timers.add("a", 9)
    timers.add("a", 10)
    assert timers.median("a") == 9.5

# Generated at 2022-06-13 18:36:10.546201
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('timer', 1)
    timers.add('timer', 2)
    assert timers.min('timer') == 1
    assert timers.min('timer2') == 0
    timers.add('timer2', 10)
    timers.add('timer2', np.nan)
    timers.add('timer2', np.inf)
    assert timers.min('timer2') == 10


# Generated at 2022-06-13 18:36:21.097331
# Unit test for method mean of class Timers
def test_Timers_mean():
    # init 3 test timers
    t = Timers()
    t.add("a", 1)
    t.add("a", 2)
    t.add("a", 3)
    t.add("b", 4)
    t.add("b", 5)
    t.add("c", 6)

    # calc mean
    mean1 = t.mean("a")
    mean2 = t.mean("b")
    mean3 = t.mean("c")

    # check for correct values
    assert mean1 == 2
    assert mean2 == 4.5
    assert mean3 == 6

    # test for wrong key
    try:
        t.mean("d")
    except KeyError:
        assert True

    # test for empty timer
    t.clear()
    t.add("d", 0)

    mean4 = t

# Generated at 2022-06-13 18:36:24.488287
# Unit test for method median of class Timers
def test_Timers_median():
    """Test definition of median value of timer"""
    timer = Timers()
    timer.add("foo", 2.0)
    timer.add("foo", 3.0)
    assert timer.median("foo") == 2.5



# Generated at 2022-06-13 18:36:32.628973
# Unit test for method min of class Timers
def test_Timers_min():
    """test min function of Timers"""
    timer = Timers()
    assert timer.min("test") == 0
    timer.add("test", 1)
    assert timer.min("test") == 1
    timer.add("test", 2)
    assert timer.min("test") == 1
    assert timer.min("test2") == 0
    try:
        timer.min("test2") != 0
    except KeyError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 18:36:40.826702
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    from pytest import raises
    from time import sleep
    timers = Timers()
    #
    timers.add("timer1", 1.0)
    timers.add("timer1", 2.0)
    timers.add("timer1", 3.0)
    timers.add("timer2", 0.0)
    #
    assert timers.min(name="timer1") == 1.0
    assert timers.min(name="timer2") == 0.0
    #
    with raises(KeyError):
        timers.min(name="missing")
    #
    with raises(TypeError):
        timers["timer1"] = 1.0
    #
    timers.clear()
    #
    timers.add("timer1", 0.0)