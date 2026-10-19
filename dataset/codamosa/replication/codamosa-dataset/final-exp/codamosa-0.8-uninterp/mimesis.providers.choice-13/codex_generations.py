

# Generated at 2022-06-13 23:50:41.768322
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from types import SimpleNamespace

    assert isinstance(Choice().__call__(items='ABCdef123', length=2), str)
    assert hasattr(Choice().__call__(items=['A', 'B', 'C'], length=1), '__iter__')
    assert isinstance(Choice().__call__(items=['A', 'B', 'C']), str)
    assert isinstance(Choice().__call__(items=('A', 'B', 'C')), str)
    assert isinstance(
        Choice().__call__(items=('A', 'B', 'C'), length=1), tuple)

    assert isinstance(Choice().__call__(items=SimpleNamespace(__iter__=lambda self: ['A', 'B', 'C'])),
                      str)


# Generated at 2022-06-13 23:50:51.354998
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print("Testing method Choice.__call__...")

    # Test example from docstring
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ab', 'ba', 'ac', 'ca', 'bc', 'cb']

# Generated at 2022-06-13 23:50:57.550222
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print('test_Choice___call__')
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1

    ret = choice(items, length)
    assert ret == ['a']
    ret = choice(items, length, False)
    assert ret == ['a']
    ret = choice(items, length, True)
    assert ret == ['a']



# Generated at 2022-06-13 23:51:04.214640
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    items = ['a', 'b', 'c']

    actual = choice(items=items)
    assert type(actual) is str

    actual = choice(items=items, length=1)
    assert type(actual) is list

    actual = choice(items='abc', length=2)
    assert type(actual) is str

    actual = choice(items=('a', 'b', 'c'), length=5)
    assert type(actual) is tuple

    actual = choice(items='aabbbccccddddd', length=4, unique=True)
    assert type(actual) is str

# Generated at 2022-06-13 23:51:15.501641
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice_provider = Choice()
    assert isinstance(choice_provider(['a', 'b', 'c', 'd']), str)
    assert isinstance(choice_provider(['a', 'b', 'c', 'd'], length=1), list)
    assert isinstance(choice_provider(['a', 'b', 'c', 'd'], length=5, unique=True), str)
    assert isinstance(choice_provider(('a', 'b', 'c', 'd'), length=5), tuple)
    assert isinstance(choice_provider('abcd', length=1), str)
    assert choice_provider(['a', 'b', 'c', 'd']) in ['a', 'b', 'c', 'd']

# Generated at 2022-06-13 23:51:26.281229
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    try:
        choice(items=5, length=5)
    except TypeError:
        assert True
    except:
        assert False

# Generated at 2022-06-13 23:51:28.004950
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert callable(choice)



# Generated at 2022-06-13 23:51:32.782539
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # TODO
    pass

# Generated at 2022-06-13 23:51:35.305357
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    choice = Choice()
    assert choice(items) in items
    assert choice(items, length=1) in (items, )

if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:51:43.587924
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:51:56.654257
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    class Choice_Counter:
        def __init__(self):
            self.count = 0

        def choice(self, items):
            self.count += 1
            return "a"

    global_counter1 = Choice_Counter()
    global_counter2 = Choice_Counter()

    def mock_random(items, length, unique):
        global_counter1.choice(items)
        return global_counter1.choice(items)

    class MockChoice(Choice):
        def __init__(self):
            super().__init__()

        # noinspection PyMethodMayBeStatic
        def random(self):
            return global_counter2

    from unittest.mock import patch

    mock_choice = MockChoice()
    # 1
    items = ('a', 'b', 'c')

# Generated at 2022-06-13 23:51:58.298619
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass
    #assert True

# Generated at 2022-06-13 23:52:07.686435
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Create a Choice object
    choice = Choice()

    # Call the instance
    # res = choice(['a','b','c'])
    res = choice(['a','b','c'], 1)
    print(res)

    # call the instance
    res2 = choice('abc', 2)
    print(res2)

    # call the instance
    res3 = choice(('a','b','c'), 5)
    print(res3)

    # call the instance
    res4 = choice('aabbbccccddddd', 4, True)
    print(res4)



if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:52:15.722863
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from . import MockRandom, Choice
    from .test_helpers import func_name, generate_data
    from hypothesis import assume, given, settings

    # Unit test for method __call__ of class Choice
    @given(data=generate_data(
        length=1,
        unique=True,
        elements=Choice(random=MockRandom(1)).random.choice,
    ))
    @settings(max_examples=100)
    def test_Choice_data(data):
        choice = Choice(random=MockRandom(1))
        assume(data) # assume data is non-empty, so we can index it
        assume(choice.random.choice(data) in data)

        unique = choice.random.boolean()
        length = choice.random.integer(max_value=len(data))

# Generated at 2022-06-13 23:52:27.740292
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    r = choice(items=['a', 'b', 'c'])
    assert r in ['a', 'b', 'c']
    r = choice(items=['a', 'b', 'c'], length=1)
    assert isinstance(r, list)
    assert len(r) == 1
    assert r[0] in ['a', 'b', 'c']
    r = choice(items='abc', length=2)
    assert isinstance(r, str)
    assert len(r) == 2
    assert r[0] in ['a', 'b', 'c']
    assert r[1] in ['a', 'b', 'c']
    r = choice(items=('a', 'b', 'c'), length=5)
    assert isinstance(r, tuple)

# Generated at 2022-06-13 23:52:33.910744
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    items = [1, 2, 3, 4, 5]
    length = 3
    data = c(items=items, length=length)
    assert len(data) == length
    assert type(data) == type(items)
    assert not set(items) - set(data)
    assert not set(data) - set(items)

# Generated at 2022-06-13 23:52:47.735028
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Note: `items` is of type Optional[Sequence[Any]]
    input = {'items': ['a', 'b', 'c'], 'length': 0, 'unique': False}
    expected = 'c'
    assert Choice.Meta().__call__(**input) == expected
    input = {'items': ['a', 'b', 'c'], 'length': 1, 'unique': False}
    expected = ['a']
    assert Choice.Meta().__call__(**input) == expected
    input = {'items': 'abc', 'length': 2, 'unique': False}
    expected = 'ba'
    assert Choice.Meta().__call__(**input) == expected
    input = {'items': ('a', 'b', 'c'), 'length': 5, 'unique': False}

# Generated at 2022-06-13 23:53:02.229344
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert isinstance(c(items=['a', 'b', 'c']), str)
    assert isinstance(c(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(c(items='abc', length=2), str)
    assert isinstance(c(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(c(items='aabbbccccddddd', length=4, unique=True), str)

    with pytest.raises(ValueError):
        c(items=['a', 'b', 'c'], length=0)
    with pytest.raises(ValueError):
        c(items='abc', length=-1)

# Generated at 2022-06-13 23:53:04.625912
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 23:53:05.970664
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass


# Generated at 2022-06-13 23:53:29.946062
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'a'
    assert choice(items=['a', 'b', 'c'], length=1) == ['c']
    assert choice(items='abc', length=2) == 'ab'
    assert choice(items=('a', 'b', 'c'), length=5) == ('b', 'a', 'c', 'a', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'bacd'



# Generated at 2022-06-13 23:53:30.456131
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert True == True

# Generated at 2022-06-13 23:53:39.404407
# Unit test for method __call__ of class Choice

# Generated at 2022-06-13 23:53:50.733732
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    provider = Choice()
    data = provider(items=['a', 'b', 'c'])
    assert data in ['a', 'b', 'c']
    data = provider(items=['a', 'b', 'c'], length=1)
    assert data == ['a'] or data == ['b'] or data == ['c']
    data = provider(items='abc', length=2)
    assert data == 'ba' or data == 'ab' or data == 'cb' \
           or data == 'bc' or data == 'ca' or data == 'ac'
    data = provider(items=('a', 'b', 'c'), length=5)
    assert data == ('c', 'a', 'a', 'b', 'c') \
           or data == ('a', 'b', 'c', 'a', 'a') \
          

# Generated at 2022-06-13 23:54:01.169547
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test the results of calling a method."""
    import unittest
    from unittest import TestCase
    from unittest.mock import Mock

    from mimesis.enums import Provider
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.utils import TypedList

    from . import Choice

    class StubChoice(Choice):
        """Stub version of the Choice class."""

        def __init__(self, *args, **kwargs):
            """Initialize attributes."""
            super().__init__(*args, **kwargs)

        def __call__(self, items, length=0, unique=False):
            """Generate a randomly-chosen sequence."""
            items = items * length
            return items


# Generated at 2022-06-13 23:54:13.872643
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    from mimesis import Choice
    choice = Choice()

    # Tests method __call__ of class Choice
    # Tests branch branch-B-B-B1-B1-B1
    assert(choice(items=['a', 'b', 'c']) == 'c')

    # Tests method __call__ of class Choice
    # Tests branch branch-B-B-B1-B1-B2
    assert(choice(items=['a', 'b', 'c'], length=1) == ['a'])

    # Tests method __call__ of class Choice
    # Tests branch branch-B-B-B1-B2-B1
    assert(choice(items='abc', length=2) == 'ba')

    # Tests method __call__ of class Choice
    # Tests branch branch-B-B-B2-B1
   

# Generated at 2022-06-13 23:54:23.999003
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from hypothesis import given
    from hypothesis.strategies import integers, tuples, lists
    from hypothesis.strategies import text

    @given(integers(), integers())
    def test_negative_length(items, length):
        if length < 0:
            from mimesis.exceptions import NonPositiveIntegerError
            Choice()(items=items, length=length)
            assert False

    @given(integers(), text())
    def test_string_items(items, length):
        items = Choice()(items=items, length=length)
        assert len(items) == length

    @given(text(), integers())
    def test_string_items(items, length):
        items = Choice()(items=items, length=length)
        assert len(items) == length


# Generated at 2022-06-13 23:54:35.790258
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import sys
    import io
    # Capturing the output
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    tester = Choice()

    tester(items=['a', 'b', 'c'])
    assert capturedOutput.getvalue() == "c\n"

    capturedOutput.truncate(0)
    capturedOutput.seek(0)

    tester(items=['a', 'b', 'c'], length=1)
    assert capturedOutput.getvalue() == "['a']\n"

    capturedOutput.truncate(0)
    capturedOutput.seek(0)

    tester(items='abc', length=2)
    assert capturedOutput.getvalue() == "ba\n"

    capturedOutput.truncate(0)
    capturedOutput.seek(0)



# Generated at 2022-06-13 23:54:44.166974
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import mimesis
    fake = mimesis.Choice()
    assert fake(items=['a', 'b', 'c']) == 'c'
    assert fake(items=['a', 'b', 'c'], length=1) == ['a']
    assert fake(items = 'abc', length=2) == 'ba'
    assert fake(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert fake(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:54:46.783577
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    items = ('a', 'b', 'c')
    length = 5
    c.__call__(items=items, length=length)



# Generated at 2022-06-13 23:55:40.121413
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import string

    item_list = string.ascii_uppercase
    choice_inst = Choice()
    choice_inst.seed(0)

    # Call __call__ of base class
    _, result = choice_inst.__call__(item_list)

    assert isinstance(result, str)
    assert len(result) == 1
    assert result == 'F'
    return True


# Generated at 2022-06-13 23:55:46.343536
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = Choice().__call__(items=['a', 'b', 'c'])
    assert isinstance(data, str)
    assert data in ['a', 'b', 'c']
    data = Choice().__call__(items=('a', 'b', 'c'))
    assert isinstance(data, str)
    assert data in ['a', 'b', 'c']
    data = Choice().__call__(items=('a', 'b', 'c'), length=1)
    assert isinstance(data, list)
    assert data in [['a'], ['b'], ['c']]
    data = Choice().__call__(items=('a', 'b', 'c'), length=1, unique=True)
    assert isinstance(data, list)

# Generated at 2022-06-13 23:55:49.522243
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""

    actual = Choice().__call__(items=('a', 'b', 'c'), length=5)
    expected = ('c', 'a', 'a', 'b', 'c')
    assert expected == actual

# Generated at 2022-06-13 23:55:58.448285
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method Choice.__call__().
    """
    choice = Choice()
    items=['a', 'b', 'c']
    length=1
    unique=False
    assert choice(items, length, unique) in items
    items=('a', 'b', 'c')
    length=5
    unique=False
    assert choice(items, length, unique) in items
    items='abc'
    length=2
    unique=True
    assert choice(items, length, unique) in items
    items='aabbbccccddddd'
    length=4
    unique=False
    assert choice(items, length, unique) in items



# Generated at 2022-06-13 23:56:04.149596
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == \
           ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:56:14.557153
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Example 1
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    # Example 2
    choice = Choice()
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    # Example 3
    choice = Choice()
    assert choice(items='abc', length=2) == 'ba'
    # Example 4
    choice = Choice()
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    # Example 5
    choice = Choice()
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:56:26.125989
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # test_Choice___call__ is called only directly, not by pytest so we need to import pytest
    import pytest

    # Check that method __call__ of class Choice raise exception when length is lower than 0
    choice = Choice()
    with pytest.raises(ValueError) as excinfo:
        choice(items=['a', 'b', 'c'], length=-2)
    assert '**length** should be a positive integer.' in str(excinfo.value)

    # Check that method __call__ of class Choice raise exception when length is higher than the length of the list
    with pytest.raises(ValueError) as excinfo:
        choice(items=['a'], length=2)
    assert 'There are not enough unique elements in **items** to provide the specified **number**.' in str(excinfo.value)


#

# Generated at 2022-06-13 23:56:35.933503
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    t = Choice()
    # items = ['a', 'b', 'c']
    # length = 1
    # unique = 1
    # assert (t(items, length, unique) == ['a'])
    # items = 'abc'
    # length = 2
    # unique = 1
    # assert (t(items, length, unique) == 'ba')
    # items = ['a', 'b', 'c']
    # length = 5
    # unique = 1
    # assert (t(items, length, unique) == ['c', 'a', 'a', 'b', 'c'])
    # items = 'aabbbccccddddd'
    # length = 4
    # unique = 1
    # assert (t(items, length, unique) == 'cdba')
    # items = ['a

# Generated at 2022-06-13 23:56:39.110902
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    print(choice(['a','b','c','d']))
    print(choice(['a','b','c','d'],length = 1))
    print(choice('abcdefg',length = 3, unique = True))
    print(choice( ('a', 'b', 'c', 'd'), 3))


# Generated at 2022-06-13 23:56:52.962238
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.builtins import MexicoSpecProvider

    choice = Choice(seed=12345)
    items = [None, Gender.FEMALE, Gender.MALE]
    assert isinstance(choice(items), int)

    choice = Choice(MexicoSpecProvider, seed=12345)
    items = [None, 'FEMALE', 'MALE']
    assert isinstance(choice(items), str)
    assert choice(items, length=0) in {None, 'FEMALE', 'MALE'}
    assert len(choice(items, length=3)) == 3

# Generated at 2022-06-13 23:57:29.738404
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:57:40.978360
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    assert Choice()('a', 'b', 'c') in ['a', 'b', 'c']
    assert Choice()('a', 'b', 'c', length=1) == ['a']
    assert Choice()('a', 'b', 'c', length=2) == ['a', 'b'] or \
           Choice()('a', 'b', 'c', length=2) == ['a', 'c'] or \
           Choice()('a', 'b', 'c', length=2) == ['c', 'b']

# Generated at 2022-06-13 23:57:47.733948
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import unittest
    from unittest import TestCase

    from mimesis.enums import Gender

    class ChoiceTests(TestCase):
        """Class with tests for method __call__ of class Choice."""

        def setUp(self) -> None:
            """Set up test data."""
            self.choice = Choice(seed=100)

        def test_choice_length_0(self) -> None:
            """Test for length=0."""
            result = self.choice(items=['a', 'b', 'c'])
            self.assertEqual(result, 'b')

        def test_choice_length_1(self) -> None:
            """Test for length=1."""
            result = self.choice(items=['a', 'b', 'c'], length=1)
            self.assertEqual

# Generated at 2022-06-13 23:57:51.355526
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests method Choice"""
    # TODO Fix this test
    pass

# Generated at 2022-06-13 23:57:55.376662
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    choice(items=['a', 'b', 'c'])
    choice(items=['a', 'b', 'c'], length=1)
    choice(items='abc', length=2)
    choice(items=('a', 'b', 'c'), length=5)
    choice(items='aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:57:58.766150
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    length = 1
    unique = True
    assert(Choice().__call__(items, length, unique) in ('a', 'b', 'c'))

# Generated at 2022-06-13 23:58:06.814797
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Testing method Choice.__call__

    It tests with data from docstrings above .
    """

    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False

    assert choice(items=items) == 'c'
    assert choice(items=items, length=length) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:58:15.037025
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """ Unit test for method __call__ of class Choice """
    t = Choice()
    assert len(t(items=['a', 'b', 'c'], length=1, unique=True)) == 1
    assert len(t(items=['a', 'b', 'c'], length=2, unique=True)) == 2
    assert len(t(items=['a', 'b', 'c'], length=3, unique=True)) == 3
    assert len(t(items=['a', 'b', 'c'], length=4, unique=True)) == 3
    assert len(t(items=['a', 'b', 'c'], length=5, unique=True)) == 3

# Generated at 2022-06-13 23:58:20.636358
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert isinstance(choice.__call__(['a', 'b', 'c']), str)
    assert isinstance(choice.__call__(['a', 'b', 'c'], 1), list)
    assert isinstance(choice.__call__('abc', 2), str)
    assert isinstance(choice.__call__(('a', 'b', 'c'), 5), tuple)
    assert isinstance(choice.__call__('aabbbccccddddd', 4, unique=True), str)


# Generated at 2022-06-13 23:58:31.636489
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # TypeError - for non-sequence items or non-integer length
    try:
        choice = Choice()
        choice(items='abc', length='1')
    except TypeError as e:
        print(e)
    else:
        print('Test 1 - FAIL.')

    # ValueError - if negative length or insufficient unique elements
    try:
        choice = Choice()
        choice(items='aabbbccccddddd', length=-4, unique=True)
    except ValueError as e:
        print(e)
    else:
        print('Test 2 - FAIL.')

    try:
        choice = Choice()
        choice(items='aabbbccccddddd', length=4, unique=True)
    except ValueError as e:
        print(e)

# Generated at 2022-06-13 23:59:04.489179
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = ['a', 'b', 'c']
    method_name = "_Choice__call__"
    patch_class = "mimesis.providers.sequence.Choice"
    with patch("{}.{}".format(patch_class, method_name)) as p:
        p.return_value = "a"
        assert Choice().__call__(data) == "a"

    with patch("{}.{}".format(patch_class, method_name)) as p:
        p.return_value = ["a"]
        assert Choice().__call__(data, 1) == ["a"]

    with patch("{}.{}".format(patch_class, method_name)) as p:
        p.return_value = "ba"
        assert Choice().__call__(data, 2) == "ba"

# Generated at 2022-06-13 23:59:07.315344
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = "ab"
    length = 2
    unique = True
    random = Choice(random = "random")
    data = random.__call__(items, length, unique)
    print(data)
    return True


# Generated at 2022-06-13 23:59:18.389615
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    assert choice(items=items) == 'b'
    assert choice(items=items, length=3) == ['a', 'b', 'c']
    items = 'abc'
    assert choice(items=items, length=2) == 'ca'
    items = ('a', 'b', 'c', 'd')
    assert choice(items=items, length=5) == ('c', 'a', 'd', 'b', 'b')
    items = 'aabbbccccddddd'
    assert choice(items=items, length=4, unique=True) == 'adbc'
    choice = Choice()
    assert choice.__call__([], length=10) == ""

# Generated at 2022-06-13 23:59:28.344680
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    items = ('a', 'b', 'c')
    length = 2
    unique = True
    result = choice(items=items, length=length, unique=unique)
    assert result == 'bc'
    items = 'aabbbccccddddd'
    length = 4
    unique = True
    result = choice(items=items, length=length, unique=unique)
    assert result == 'cbda'
    items = ('a', 'b', 'c')
    length = -1
    unique = False
    result = choice(items=items, length=length, unique=unique)
    assert result == 'a'
    items = ('a', 'b', 'c')
    length = 2
    unique = False

# Generated at 2022-06-13 23:59:34.938065
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:59:43.002718
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    # Define a mock for random() method
    def mock_choice(seq):
        return seq[len(seq) - 1]

    # Define a mock for function random.choice
    def mock_choice_func(seq):
        return lambda x: mock_choice(x)

    # Create an instance of Choice
    choice = Choice()

    # Run code to be tested
    choice._random = mock_choice_func(['a', 'b', 'c'])
    choice.__call__(items=['a', 'b', 'c'], length=1)

# Generated at 2022-06-13 23:59:56.734983
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    pr = Choice()
    assert isinstance(pr.choice(['a', 'b', 'c']), str)
    assert isinstance(pr.choice(['a', 'b', 'c'], 5), list)
    assert isinstance(pr.choice(['a', 7, {}]), str)
    assert isinstance(pr.choice(['a', 7, {}], 6), list)
    assert pr.choice(['a', 'a', 'a']) in ['a', 'a', 'a']
    assert pr.choice(('a', 'a', 'a'), 5) == ('a', 'a', 'a', 'a', 'a')

# Generated at 2022-06-14 00:00:09.699857
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()._Choice__call__(items=["a", "b", "c"]) == "c"

    assert Choice()._Choice__call__(items=["a", "b", "c"], length=1) == ["a"]

    assert Choice()._Choice__call__(items="abc", length=2) == "ba"

    assert Choice()._Choice__call__(items=("a", "b", "c"), length=5) == ("c", "a", "a", "b", "c")

    assert Choice()._Choice__call__(items='aabbbccccddddd', length=4, unique=True) == "cdba"

# Generated at 2022-06-14 00:00:16.053618
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from hypothesis import strategies as st
    from hypothesis import given
    from . import strategies as mime_st

    # TODO: Fix when __call__ returns proper type
    @given(st.data())
    def test(data):
        c = Choice(data.draw(st.from_regex('[a-z]{5}')))
        r = data.draw(mime_st.random_choice(c))
        assert isinstance(r, list) or isinstance(r, tuple)

    test()


# Generated at 2022-06-14 00:00:22.019547
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from hypothesis import given
    from hypothesis.strategies import lists, text
    from mimesis.providers.choice import Choice
    from typing import List
    choice = Choice()
    list_of_str = lists(elements=text(), min_size=1, max_size=10)
    @given(sequence=list_of_str, length=lists(elements=list_of_str, max_size=10))
    def test_sequence_length(sequence: List[str], length: List[List[str]]) -> None:
        # Test sequence and length
        choice(sequence, len(sequence), unique=False)
        choice(sequence, length, unique=False)
        choice(sequence, unique=False)
        choice(sequence, length, unique=True)
        choice(sequence, length, unique=True)