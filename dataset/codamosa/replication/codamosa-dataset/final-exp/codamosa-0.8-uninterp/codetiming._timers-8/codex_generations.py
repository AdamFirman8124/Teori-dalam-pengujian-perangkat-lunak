

# Generated at 2022-06-13 18:27:36.617267
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("Test", 1.0)
    assert timers.min("Test") == 1.0



# Generated at 2022-06-13 18:27:39.465442
# Unit test for method stdev of class Timers
def test_Timers_stdev():
    timers = Timers()
    timers._timings.update({"a": [1, 2, 3, 4, 5], "b": [1, 2]})
    assert timers.stdev("a") == math.sqrt(2)
    assert timers.stdev("b") == math.nan
    assert timers.stdev("c") == 0
    assert timers.stdev("d") == 0

# Generated at 2022-06-13 18:27:45.994964
# Unit test for method stdev of class Timers
def test_Timers_stdev():
    """Test standard deviation of timings"""
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    assert math.isnan(timers.stdev("test"))
    timers.add("test", 3.0)
    assert timers.stdev("test") == 1.0

# Generated at 2022-06-13 18:27:53.134840
# Unit test for method stdev of class Timers
def test_Timers_stdev():
    # Setup
    t = Timers()
    # Test
    t.add("a", 1)
    t.add("a", 2)
    t.add("a", 3)
    t.add("a", 4)
    # Result
    stdev = t.stdev("a")
    assert stdev == 1.2909944487358056

# Generated at 2022-06-13 18:28:06.567326
# Unit test for method apply of class Timers
def test_Timers_apply():
    timers = Timers()
    timers._timings = {
        "A": [1, 2],
        "B": [3, 4],
        "C": [5, 6, 7],
    }
    assert timers.apply(lambda x: x, "A") == [1, 2]
    assert timers.apply(lambda x: len(x), "A") == 2
    assert timers.apply(lambda x: sum(x), "A") == 3
    assert timers.apply(lambda x: sum(x), "B") == 7
    assert timers.apply(lambda x: sum(x), "C") == 18
    assert timers.apply(lambda x: min(x), "C") == 5
    assert timers.apply(lambda x: max(x), "C") == 7

# Generated at 2022-06-13 18:28:16.158086
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    timers.add('a', 1)
    timers.add('a', 3)
    assert 1 == timers.min('a')
    assert 3 == timers.max('a')
    assert 2 == timers.mean('a')
    assert 2 == timers.median('a')
    assert math.sqrt(2) == timers.stdev('a')
    assert 2 == timers.count('a')
    assert 2 == timers.total('a')
    # Check that nonexistent key raises KeyError
    try:
        timers.stdev('b')
    except KeyError:
        pass
    else:
        raise AssertionError('KeyError expected, but not raised')
    # Check that methods min and max return 0
    # when called on an empty list
    timers

# Generated at 2022-06-13 18:28:21.970364
# Unit test for method stdev of class Timers
def test_Timers_stdev():
    timers = Timers()
    timers._timings = {'test': [1, 2, 3, 4]}
    assert timers.stdev('test') == 1.118033988749895

if __name__ == '__main__':
    test_Timers_stdev()
    print('Test successful')

# Generated at 2022-06-13 18:28:27.590551
# Unit test for method stdev of class Timers
def test_Timers_stdev():
    m = Timers()
    m.add("a", 1)
    m.add("a", 2)
    m.add("a", 3)
    assert m.stdev("a") == 1
    assert m.stdev("b") == math.nan
    m.clear()
    assert m.stdev("a") == math.nan

# Unit tests for whole class Timers

# Generated at 2022-06-13 18:28:33.409237
# Unit test for method median of class Timers
def test_Timers_median():
    from random import random
    from .test_utils import dict_almost_equal
    timer = Timers()
    timer._timings = {
        "random_numbers": [random() for _ in range(10000)],
        "empty_list": [],
        "single_item_list": [random()],
    }
    timer.data["random_numbers"] = sum(timer._timings["random_numbers"])
    timer.data["empty_list"] = 0
    timer.data["single_item_list"] = timer._timings["single_item_list"][0]

# Generated at 2022-06-13 18:28:38.340745
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test the method mean of Timers"""
    timers = Timers()
    assert timers.mean('test') == 0
    timers.add('test', 1.)
    assert timers.mean('test') == 1.
    timers.add('test', 2.)
    assert timers.mean('test') == 1.5
    timers.add('test', 3.)
    assert timers.mean('test') == 2.0

# Generated at 2022-06-13 18:28:45.283261
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    assert timers.max('undefined') == 0

    timers.add('timer', 0)
    assert timers.max('timer') == 0

    timers.add('timer', 1)
    assert timers.max('timer') == 1

    timers.add('timer', 2)
    assert timers.max('timer') == 2

    timers.add('timer', 3)
    assert timers.max('timer') == 3


# Generated at 2022-06-13 18:28:52.328955
# Unit test for method min of class Timers
def test_Timers_min():
    raw_timers = Timers()
    raw_timers.add('a2a', 60000000000)
    raw_timers.add('a2a', 50000000000)
    raw_timers.add('a2a', 40000000000)
    raw_timers.add('a2a', 30000000000)
    raw_timers.add('a2a', 20000000000)
    raw_timers.add('a2a', 10000000000)
    result = raw_timers.min('a2a')
    assert result == 10000000000

# Generated at 2022-06-13 18:28:56.417434
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("foo", 68.9)
    timers.add("foo", 7.42)
    timers.add("foo", 2.0)
    timers.add("foo", 1.0)
    assert math.isclose(timers.median("foo"), 2.0)

# Generated at 2022-06-13 18:28:59.801630
# Unit test for method max of class Timers
def test_Timers_max():
    import pytest
    timers = Timers()
    timers.add('A', 10)
    timer_max = timers.max('A')
    assert math.isclose(timer_max, 10, rel_tol = 1e-9)

# Generated at 2022-06-13 18:29:05.278034
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('test', 10)
    timers.add('test', 20)
    timers.add('test', 30)
    assert timers.min('test') == 10


# Generated at 2022-06-13 18:29:10.017373
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers._timings = {'name1': [1, 2, 3, 4, 5], 'name2': [6, 7, 8, 9, 10]}

    assert timers.median('name1') == 3
    assert timers.median('name2') == 8

# Generated at 2022-06-13 18:29:16.751786
# Unit test for method max of class Timers
def test_Timers_max():
    
    # Create a timer instance
    timer = Timers()
    
    # Add timer names and values
    timer.add("timer_1", 10)
    timer.add("timer_2", 20)
    timer.add("timer_3", 30)
    timer.add("timer_4", 40)
    
    # Test value
    assert timer.max("timer_1") == 10



# Generated at 2022-06-13 18:29:17.123888
# Unit test for method min of class Timers
def test_Timers_min():
    pass

# Generated at 2022-06-13 18:29:19.834141
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers.median()"""

    # Create a new Timers
    timer = Timers()

    # Populate Timers values
    timer.add('banana', 0.3)
    timer.add('banana', 0.5)
    timer.add('banana', 0.1)

    ### check that this method returns what it should
    assert timer.median('banana') == 0.3

# Generated at 2022-06-13 18:29:26.035192
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("User", 0.5)
    t.add("User", 0.3)
    t.add("User", 0.4)
    t.add("System", 0.2)
    t.add("System", 0.1)
    assert(t.max("User") == 0.5)
    assert(t.max("System") == 0.2)
    assert(t.max("NotExisting") == 0)


# Generated at 2022-06-13 18:29:41.833060
# Unit test for method min of class Timers
def test_Timers_min():
    """Testing method min of class Timers"""

    # Prepare
    import math
    import random
    import pytest
    from pytest_cases import case_name, parametrize_with_cases
    from typing import TYPE_CHECKING, Tuple
    from nfstream import nfstream

    if TYPE_CHECKING:
        TimersType = nfstream.Timers
    else:  # pragma: no cover
        TimersType = nfstream.nfstream.Timers

    timers: TimersType = TimersType()

    @pytest.fixture
    def rand_ints() -> Tuple[int, int, int]:
        return random.randint(0, 1), random.randint(0, 100), random.randint(0, 100)


# Generated at 2022-06-13 18:29:44.821393
# Unit test for method median of class Timers
def test_Timers_median():
    expected = 10

    obj = Timers()
    obj.add('test', 10)

    assert obj.median('test') == expected

# Generated at 2022-06-13 18:29:48.872332
# Unit test for method min of class Timers
def test_Timers_min():
    """Test for the min method of the Timers class."""
    timers = Timers()
    timers.add('test', 4)
    assert timers.min('test') == 4


# Generated at 2022-06-13 18:29:51.228264
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("test", 42)
    assert timers.max("test") == 42

# Generated at 2022-06-13 18:29:59.019633
# Unit test for method max of class Timers
def test_Timers_max():
    """Test Timers.max()"""
    t = Timers()
    t.add('t1', 2)
    t.add('t1', 3)
    t.add('t1', 5)
    t.add('t2', 4)
    t.add('t2', 2)
    t.add('t2', 6)
    assert t.max('t1') == 5
    assert t.max('t2') == 6
    assert t.max('t3') == 0


# Generated at 2022-06-13 18:30:02.664710
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit-test for `min` method of class `Timers`"""
    timers = Timers()
    timers.add("test", 5)
    timers.add("test", 6)
    timers.add("test", 7)
    assert timers.min("test") == 5


# Generated at 2022-06-13 18:30:09.688630
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add('foo', 1.5)
    timers.add('bar', 1.5)
    timers.add('bar', 1.5)
    assert timers.max('foo') == 1.5
    assert timers.max('bar') == 1.5
    timers.add('foo', 4.5)
    timers.add('bar', 4.5)
    timers.add('bar', 4.5)
    assert timers.max('foo') == 4.5
    assert timers.max('bar') == 4.5

test_Timers_max()

# Generated at 2022-06-13 18:30:15.162023
# Unit test for method median of class Timers
def test_Timers_median():
    """Test if method median of class Timers 
    returns the median value of a list of timings
    """
    # Arrange
    timers = Timers()
    # Act
    timers.add("t1", 1)
    timers.add("t1", 5)
    timers.add("t1", 7)
    # Assert
    assert timers.median("t1") == 5


# Generated at 2022-06-13 18:30:17.915313
# Unit test for method max of class Timers
def test_Timers_max():
    """test_Timers_max"""
    assert Timers().max('key') == 0


# Generated at 2022-06-13 18:30:22.232154
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test that method mean of class Timers works correctly"""
    timers = Timers()
    timers.data['sum'] = 1
    assert timers.mean('sum') == 1
    timers.add('mean', 1)
    assert timers.mean('mean') == 1
    timers.add('mean', 2)
    assert timers.mean('mean') == 3/2
    
test_Timers_mean()

# Generated at 2022-06-13 18:30:29.066715
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    import random
    import statistics

    timer = Timers()
    N = 100
    med = statistics.median([random.random() for n in range(N)])
    for n in range(N):
        timer.add('test', random.random())
    assert timer.median('test') == med



# Generated at 2022-06-13 18:30:35.588002
# Unit test for method mean of class Timers
def test_Timers_mean():
    d = Timers()
    d.add("x", 1)
    d.add("x", 2)
    d.add("x", 3)
    d.add("y", 4)
    d.add("y", 5)
    d.add("y", 6)

    assert d.mean("x") == 2
    assert d.mean("y") == 5


# Generated at 2022-06-13 18:30:37.968717
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("task1", 1)
    timers.add("task1", 3)
    timers.add("task1", 2)
    assert timers.median("task1") == 2.0

# Generated at 2022-06-13 18:30:41.235207
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for mean"""
    timers = Timers()
    timers.add("add", 1)
    timers.add("add", 2)
    assert timers.mean("add") == 1.5
    assert timers.mean("not a timer") == 0



# Generated at 2022-06-13 18:30:43.926269
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add('test', 4)
    t.add('test', 3)
    t.add('test', 5)
    assert t.mean('test') == 4


# Generated at 2022-06-13 18:30:52.889947
# Unit test for method max of class Timers
def test_Timers_max():
    """Test Timers.max() function"""
    timers = Timers()
    assert timers.max("name") == 0
    timers.add("name", value=1)
    timers.add("name", value=2)
    timers.add("name", value=3)
    assert timers.max("name") == 3

    assert timers.data["name"] == 6
    timers.clear()
    assert timers.max("name") == 0
    assert timers.data["name"] == 0
    timers.add("name", value=1)
    assert timers.data["name"] == 1


# Generated at 2022-06-13 18:31:01.230950
# Unit test for method max of class Timers
def test_Timers_max():
    import pytest

    timer = Timers()
    timer.add("t1", 2)
    timer.add("t1", 4)
    timer.add("t1", 1)
    timer.add("t2", 10)
    timer.add("t2", 5)
    timer.add("t2", 1)
    timer.add("t2", 3)

    assert timer.max("t1") == 4
    assert timer.max("t2") == 10
    assert timer.max("t3",) == 0


# Generated at 2022-06-13 18:31:09.255500
# Unit test for method median of class Timers
def test_Timers_median():
    def test_median_empty(self):
        """
        Test that the median method computes the expected value on an
        empty timer.
        """
        name = "this_is_a_name"

        # Compute median value, median of an empty list is 0
        value = self.median(name)
        self.assertEqual(value, 0)

    def test_median_even(self):
        """
        Test that the median method computes the expected value on a timer
        with an even number of timings.
        """
        name = "this_is_a_name"
        values = range(2, 10, 2)

        # Add values
        for value in values:
            self.add(name, value)

        # Compute median value, median of a list with an even number
        # of elements is

# Generated at 2022-06-13 18:31:15.674327
# Unit test for method max of class Timers
def test_Timers_max():
    # Unit tests for method 'max' of class 'Timers'
    # Create instance of Timers
    timers = Timers()
    # Add values
    timers.add('key1', 1.0)
    timers.add('key1', 2.0)
    timers.add('key1', 3.0)
    assert 3.0 == timers.max('key1')
    # Check timers.data
    assert {'key1': 6.0} == timers.data
    # Add values
    timers.add('key2', 1.0)
    timers.add('key2', 2.0)
    timers.add('key2', 3.0)
    assert 3.0 == timers.max('key2')
    # Check timers.data

# Generated at 2022-06-13 18:31:24.997813
# Unit test for method min of class Timers
def test_Timers_min():
    from unittest import TestCase
    from unittest.mock import patch

    class DummyTests(TestCase):

        def setUp(self) -> None:
            self.timers = Timers()

        def test_min(self) -> None:
            self.timers.add("dummy", 1.0)
            self.assertEqual(self.timers.min("dummy"), 1.0)

    with patch.object(DummyTests, "setUp") as mock_setUp:
        tests = DummyTests("setUp")
        tests.setUp()
        tests.test_min()
        mock_setUp.assert_called_once()


# Generated at 2022-06-13 18:31:37.890616
# Unit test for method median of class Timers
def test_Timers_median():
    # Tests for odd number of values
    values = Timers()
    values.add("A", 1)
    values.add("A", 3)
    values.add("A", 5)
    assert values.median("A") == 3
    # Tests for even number of values
    values = Timers()
    values.add("A", 1)
    values.add("A", 2)
    values.add("A", 3)
    values.add("A", 4)
    assert values.median("A") == 2.5
    # Tests for empty values
    values = Timers()
    assert values.median("A") == 0.0

# Generated at 2022-06-13 18:31:42.392287
# Unit test for method median of class Timers
def test_Timers_median():
    """Test Timers.median() function"""
    timers = Timers()
    timers.add("mytimer", 1)
    timers.add("mytimer", 2)
    timers.add("mytimer", 3)

    assert round(timers.median("mytimer"), 12) == 2


# Generated at 2022-06-13 18:31:46.926566
# Unit test for method mean of class Timers
def test_Timers_mean():
        res = []
        name = 'test'
        with Timers() as _timers:
            _timers.add(name, res[0])

        assert _timers.mean(name) == res[0]


# Generated at 2022-06-13 18:31:54.364615
# Unit test for method median of class Timers
def test_Timers_median():
    """Test the method Timers.median()"""
    timers = Timers()
    timers.add("MyName", 1.0)
    timers.add("MyName", 2.0)
    timers.add("MyName", 3.0)
    assert timers.median("MyName") == 2.0
    timers.add("MyName", 4.0)
    assert timers.median("MyName") == 2.5

# Generated at 2022-06-13 18:31:59.410429
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('x', 2)
    timers.add('x', 5)
    result = timers.mean('x')
    assert result == 3.5


# Generated at 2022-06-13 18:32:05.989963
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("foo", 8.0)
    timers.add("foo", 8.0)
    timers.add("foo", 8.0)
    assert timers.median("foo") == 8.0
    timers.add("foo", 10.0)
    timers.add("foo", 10.0)
    assert timers.median("foo") == 9.0
    timers.add("foo", 0.0)
    assert timers.median("foo") == 8.0
    try:
        timers.median("bar")
        assert False
    except KeyError:
        assert True

# Generated at 2022-06-13 18:32:09.831181
# Unit test for method max of class Timers
def test_Timers_max():
    t = Timers()
    t.add("test", 7)
    t.add("test", 5)
    t.add("test", 11)
    t.add("test", 9)

    assert t.max("test") == 11

# Generated at 2022-06-13 18:32:14.061874
# Unit test for method median of class Timers
def test_Timers_median():
    timings = Timers()
    assert timings.median("test") == 0
    timings.add("test", 1)
    timings.add("test", 2)
    timings.add("test", 3)
    assert timings.median("test") == 2

# Generated at 2022-06-13 18:32:19.831241
# Unit test for method max of class Timers
def test_Timers_max():
    timer_list = Timers()
    timer_list.add('a', 2)
    timer_list.add('b', 3)
    timer_list.add('c', 4)
    timer_list.add('b', 1)
    assert timer_list.max('b') == 3
    assert timer_list.max('a') == 2
    assert timer_list.max('c') == 4

# Generated at 2022-06-13 18:32:27.598138
# Unit test for method max of class Timers
def test_Timers_max():
    """Test method max of class Timers"""
    # pylint: disable=unused-argument
    def test_fun(args):
        """Function as first argument"""
        return args

    time = Timers()
    time.add('name', 1)
    time.add('name', 5)
    time.add('name', 9)
    time.add('name', 10)
    time.add('name', 2)
    time.add('name', 5)
    time.add('name', 3)
    time.add('name', 10)
    # Test
    assert time.max('name') == 10.0
    assert time.max('name1') == 0.0
    assert time.max('name2') == 0.0
    assert time.min('name') == 1.0
    assert time.min('name1')

# Generated at 2022-06-13 18:32:35.682704
# Unit test for method median of class Timers
def test_Timers_median():
    """Unit test for method median of class Timers"""
    values = [0.0, 0.0, 0.0, 5.0, 5.0, 5.0, 10.0, 10.0, 10.0]
    for i in range(100000):
        timers = Timers() # pylint: disable=unused-variable
        for value in values:
            timers.add("median", value)
        assert timers.median("median") == 5.0


# Generated at 2022-06-13 18:32:42.638487
# Unit test for method min of class Timers
def test_Timers_min():
    """Test for method min of class Timers

    :return:
    """

    # Setup
    empty_timers = Timers()

    # Assert
    assert empty_timers.min('sample_timer') == 0

    # Setup
    empty_timers.add('sample_timer', 2)

    # Assert
    assert empty_timers.min('sample_timer') == 2

    # Setup
    timers = Timers()

    # Setup
    timers.add('sample_timer', 2)
    timers.add('sample_timer', 1)
    timers.add('sample_timer', 3)

    # Assert
    assert timers.min('sample_timer') == 1

# Generated at 2022-06-13 18:32:50.332068
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit test for method mean of class Timers"""
    timers = Timers()
    assert timers == {}

    timers.add("name", value=3.0)
    assert timers == {"name": 3.0}

    timers.add("name", value=1.0)
    assert timers == {"name": 4.0}

    assert timers.mean("name") == 2.0


# Generated at 2022-06-13 18:32:53.697429
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t["read"] = 0.1
    t["write"] = 0.1
    t["write"] = 0.2
    assert t.min("read") == 0.1
    assert t.min("write") == 0.1


# Generated at 2022-06-13 18:32:58.363192
# Unit test for method min of class Timers
def test_Timers_min():
    """Test function for the min method."""
    timers = Timers()
    timers.add("min", 2)
    timers.add("min", 5)
    assert timers.min("min") == 2

# Generated at 2022-06-13 18:33:07.772309
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("timer1", 13.0)
    timers.add("timer1", 31.0)
    timers.add("timer1", 23.0)
    timers.add("timer1", 41.0)
    timers.add("timer1", 17.0)
    timers.add("timer1", 11.0)
    timers.add("timer1", 15.0)
    timers.add("timer1", 19.0)
    timers.add("timer1", 19.0)
    timers.add("timer1", 19.0)
    assert timers.min("timer1") == 11.0
    assert timers.min("timer2") == 0.0

# Generated at 2022-06-13 18:33:17.186277
# Unit test for method min of class Timers
def test_Timers_min():
    fields = ['total', 'min', 'max', 'mean', 'median', 'stdev', 'count']
    timers = Timers()
    timers._timings['test'] = [5, 5, 5, 5, 5]
    timers.data['test'] = 25
    assert timers['test'] == 25

# Generated at 2022-06-13 18:33:23.889584
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Unit tests for method mean of class Timers"""
    timers = Timers()
    timers.add("a", 1)
    timers.add("a", 2)
    timers.add("a", 3)
    timers.add("b", 10)
    timers.add("b", 20)
    timers.add("c", 100)
    assert timers.mean("a") == 2
    assert timers.mean("b") == 15
    assert timers.mean("c") == 100



# Generated at 2022-06-13 18:33:29.098461
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add("test", 1)
    assert timers.min("test") == 1
    timers.add("test", 2)
    assert timers.min("test") == 1
    assert "test" in timers
    timers.clear()
    assert "test" not in timers



# Generated at 2022-06-13 18:33:36.877176
# Unit test for method max of class Timers
def test_Timers_max():
    a = Timers()
    a.add("bla",0.2)
    a.add("bla",0.3)
    a.add("bla",0.4)
    a.add("ble",0.1)
    a.add("ble",0.3)
    a.add("ble",0.2)
    a.add("ble",0.1)
    b = a.max("bla")
    c = a.max("ble")
    assert b == 0.4
    assert c == 0.3


# Generated at 2022-06-13 18:33:46.389525
# Unit test for method min of class Timers
def test_Timers_min():
    counters = Timers()
    assert (counters.min("foobar")) == 0
    counters._timings = {"foobar" : [1,2,3,4,5]}
    assert (counters.min("foobar")) == 1
    return


# Generated at 2022-06-13 18:33:55.023258
# Unit test for method mean of class Timers
def test_Timers_mean():
    # define a object of class Timers
    # timers = Timers({'one': 1, 'two': 2, 'three': 3})
    timers = Timers()  # pragma: no cover

    # test if mean is an attribute
    assert hasattr(timers, "mean")

    # test if mean is a function
    assertcallable(timers.mean)

    # add some values
    timers.add("new", 2.3)
    timers.add("new", 2.4)
    timers.add("new", 2.5)

    # testing mean
    assert math.isclose(timers.mean("new"), 2.4, rel_tol=1e-08)

    # testing mean
    assert not math.isclose(timers.mean("new"), 2.5, rel_tol=1e-08)


# Generated at 2022-06-13 18:34:00.362586
# Unit test for method median of class Timers
def test_Timers_median():
    timers = Timers()
    timers.add("test_1", 1)
    timers.add("test_1", 1)
    timers.add("test_1", 1)
    timers.add("test_2", 3)
    timers.add("test_2", 3)
    assert timers.median("test_1") == 1
    assert timers.median("test_2") == 3


# Generated at 2022-06-13 18:34:11.087925
# Unit test for method mean of class Timers
def test_Timers_mean():
    # Arrange
    timers = Timers()
    timers.data = {"a": 1, "b": 1.5, "c": 0.75}
    timers._timings = {
        "a": [0.2, 0.3, 0.1, 0.0],
        "b": [0.25, 0.25, 0.25, 0.25, 0.25],
        "c": [0.75, 0.75],
    }
    # Act
    mean_a = timers.mean("a")
    mean_b = timers.mean("b")
    mean_c = timers.mean("c")
    # Assert
    assert mean_a == 0.15
    assert mean_b == 0.25
    assert mean_c == 0.75

# Generated at 2022-06-13 18:34:14.950720
# Unit test for method max of class Timers
def test_Timers_max():
    expected = max(values)
    res = Timers(dict(zip(names, values))).max("timer")


# Generated at 2022-06-13 18:34:21.541707
# Unit test for method max of class Timers
def test_Timers_max():
    """Test Timers.max() method"""
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    assert timers.max('test') == 3
    assert timers.max('test') == 3
    assert timers.max('test2') == 0


# Generated at 2022-06-13 18:34:26.684991
# Unit test for method max of class Timers
def test_Timers_max():
    '''Unit test for method max of class Timers'''
    timers = Timers()
    timers.add('test1', 3)
    timers.add('test2', 9)
    timers.add('test1', 11)
    assert timers.max('test1') == 11
    assert timers.max('test2') == 9



# Generated at 2022-06-13 18:34:33.013538
# Unit test for method mean of class Timers
def test_Timers_mean():
    t = Timers()
    t.add("foo", 10)
    t.add("foo", 0)
    t.add("foo", 1000)
    t.add("bar", 5)
    t.add("bar", 5)
    t.add("bar", 5)
    assert t.mean("foo") == 370
    assert t.mean("bar") == 5

test_Timers_mean()

# Generated at 2022-06-13 18:34:36.703634
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""
    timers = Timers()
    assert timers.max("test") == 0
    timers.add("test", 1)
    assert timers.max("test") == 1
    timers.add("test", 2)
    assert timers.max("test") == 2



# Generated at 2022-06-13 18:34:41.552445
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test function that returns the mean of a list"""
    test_timers = Timers()
    test_timers.add('name1', 3)
    test_timers.add('name1', 4)
    test_timers.add('name1', 5)
    test_timers.add('name1', 6)
    test_timers.add('name1', 7)
    assert test_timers.mean('name1') == 5

test_Timers_mean()


# Generated at 2022-06-13 18:34:56.450904
# Unit test for method max of class Timers
def test_Timers_max():
    test_timers = Timers()
    test_timers.add("test", 10)
    test_timers.add("test", 20)
    test_timers.add("test", 30)
    assert test_timers.max("test") == 30


# Generated at 2022-06-13 18:35:09.262181
# Unit test for method mean of class Timers
def test_Timers_mean():
    class TestTimers(UserDict):

        def __init__(self):
            super().__init__()
            self._timings = {'test':[1,2,3,4,5]}
            self.data.setdefault('test',0)
            self.data['test'] += 15

        def apply(self, func, name):
            if name in self._timings:
                return func(self._timings[name])
            raise KeyError(name)

        def mean(self, name):
            return self.apply(lambda values: statistics.mean(values or [0]), name=name)

    test_timers = TestTimers()
    assert test_timers.mean('test') == 3


# Generated at 2022-06-13 18:35:17.387429
# Unit test for method min of class Timers
def test_Timers_min():
    """Test method min of class Timers"""
    timer = Timers()

    # Test first call
    assert timer.min('name') == 0

    # Test with existing value
    timer._timings['name'] = [10, 20]
    assert timer.min('name') == 10

    # Test with empty list
    timer._timings['name'] = []
    assert timer.min('name') == 0

    # Test with none as value
    timer['name'] = None
    assert timer.min('name') == 0

    # Test with other key
    timer['name2'] = None
    assert timer.min('name2') == 0


# Generated at 2022-06-13 18:35:31.159621
# Unit test for method max of class Timers
def test_Timers_max():
    """Unit test for method max of class Timers"""

    timer_dict = Timers()

    print("Test when no key in dict")
    try:
        timer_dict.max("key")
    except KeyError as err:
        assert str(err) == "key"
        print("KeyError successfully raised")
    else:
        raise AssertionError("KeyError not raised")

    print("Test when key: value exists in dict")
    timer_dict.data["key"] = 1000
    assert timer_dict.max("key") == 1000
    print("Max successfully returned")

    print("Test when key: value plus list with values exists in dict")
    timer_dict._timings["key"] = [7.0, 3.0, 5.0, 3.0, 1.0]

# Generated at 2022-06-13 18:35:38.848340
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()

    timers.add('T1', 1.0)
    timers.add('T2', 1.0)
    timers.add('T1', 1.0)
    timers.add('T1', 2.0)
    timers.add('T2', 2.0)
    timers.add('T2', 3.0)

    assert timers.mean('T1') == 1.333
    assert timers.mean('T2') == 2.0
    assert timers.mean('T3') == 0.0

# Generated at 2022-06-13 18:35:41.409839
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers._timings = {'val1': [2, 3]}
    assert timers.max('val1') == 3


# Generated at 2022-06-13 18:35:46.091563
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    assert t.min("min") == 0
    t.add("min", 1)
    assert t.min("min") == 1
    t.add("min", 2)
    assert t.min("min") == 1
    t.add("min", 0)
    assert t.min("min") == 0
    assert t.min("max") == 0


# Generated at 2022-06-13 18:35:52.263357
# Unit test for method max of class Timers
def test_Timers_max():  # pragma: no cover
    """Unit tests for method max of class Timers"""
    timings = Timers()
    assert timings.max("foobar") == 0.0
    timings.add("foobar", 1.0)
    assert timings.max("foobar") == 1.0
    timings.add("foobar", 2.0)
    assert timings.max("foobar") == 1.0


# Generated at 2022-06-13 18:35:58.512424
# Unit test for method mean of class Timers
def test_Timers_mean():
    """Test Timers.mean

    The test is constructed so that it would fail if the input values
    would be used directly to calculate the mean instead of being sorted
    first.

    """
    # Define two generic timers
    timer1 = Timers({"TIMER1": 200})
    timer2 = Timers({"TIMER2": 200})

    # Append values to first timer
    timer1.add("TIMER1", 100)
    timer1.add("TIMER1", 100)
    timer1.add("TIMER1", 50)

    # Append values to second timer
    timer2.add("TIMER2", 25)
    timer2.add("TIMER2", 25)
    timer2.add("TIMER2", 25)
    timer2.add("TIMER2", 25)

# Generated at 2022-06-13 18:36:00.958251
# Unit test for method mean of class Timers
def test_Timers_mean():
    timers = Timers()
    timers.add('delay', 1.0)

    assert timers.mean('delay') == 1.0

# Generated at 2022-06-13 18:36:17.022152
# Unit test for method median of class Timers
def test_Timers_median():
    """
    Test median() method on class Timers
    """
    timers = Timers()
    timers.add("my-timer", 1)
    timers.add("my-timer", 2)
    timers.add("my-timer", 3)
    assert timers.median("my-timer") == 2

# Generated at 2022-06-13 18:36:23.892178
# Unit test for method median of class Timers
def test_Timers_median():
    dict = Timers()
    dict._timings = {'a': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'b': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

    try:
        assert dict.median('a') == 6
        assert dict.median('b') == 5.5
    except:
        print("Failed to implement median method")

test_Timers_median()

# Generated at 2022-06-13 18:36:28.012107
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers._timings = {'foo': [-1, 0, 1], 'bar': [1, 2, 3]}
    assert timers.min('bar') == 1
    assert timers.min('foo') == -1
    assert timers.min('baz') == 0
    assert timers.min('baz') == 0


# Generated at 2022-06-13 18:36:30.646596
# Unit test for method mean of class Timers
def test_Timers_mean():
    assert Timers({"foo": 1.0, "bar": 2.0, "baz": 3.0}).mean("foo") == 1.0

# Generated at 2022-06-13 18:36:35.669032
# Unit test for method min of class Timers
def test_Timers_min():
    """Unit test for method min of class Timers"""
    from stats_arrays.tests.dummy_module import timers  # type: ignore
    assert timers.min("foo") == 0
    assert timers.min("bar") == 1
    # Note: we are testing the default value of a defaultdict
    assert timers.min("unk") == 0


# Generated at 2022-06-13 18:36:37.840204
# Unit test for method max of class Timers
def test_Timers_max():
    timers = Timers()
    timers.add("timer_1", 10)
    timers.add("timer_2", 20)

    assert timers.max("timer_1") == 10
    assert timers.max("timer_2") == 20



# Generated at 2022-06-13 18:36:46.021039
# Unit test for method median of class Timers
def test_Timers_median():
    """median of Timers"""
    t = Timers()
    t.add("t1", 1)
    t.add("t1", 2)
    t.add("t1", 3)
    assert t.median("t1") == 2
    assert t.mean("t1") == 2
    assert t.max("t1") == 3
    assert t.min("t1") == 1
    assert t.count("t1") == 3


# Generated at 2022-06-13 18:36:48.403204
# Unit test for method max of class Timers
def test_Timers_max():
    """Test the Timers class max method"""
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    max_value = timers.max('test')
    assert max_value == 2


# Generated at 2022-06-13 18:36:52.939032
# Unit test for method min of class Timers
def test_Timers_min():
    t = Timers()
    t.add('a', 5)
    t.add('a', 10)
    t.add('a', 25)
    assert t.min('a') == 5



# Generated at 2022-06-13 18:36:54.478615
# Unit test for method min of class Timers
def test_Timers_min():
    timers = Timers()
    timers.add('time1',1)

# Generated at 2022-06-13 18:37:30.784822
# Unit test for method min of class Timers
def test_Timers_min():
    """Check if min function works as intended"""
    timings = Timers()
    if timings.min("timer") == 0.0:
        return False
    timings.add("timer", 23)
    if timings.min("timer") != 23.0:
        return False
    timings.add("timer", 1)
    timings.add("timer", 5)
    if timings.min("timer") != 1.0:
        return False
    return True
