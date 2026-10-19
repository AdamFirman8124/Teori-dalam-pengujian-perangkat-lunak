

# Generated at 2022-06-13 23:50:36.063883
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    # Get instance of class Choice.
    obj = Choice()

    # Get a sequence or bare element randomly chosen from 
    # a sequence of items, with or without length and unique constraints.
    obj(items=['a', 'b', 'c'])
    obj(items=['a', 'b', 'c'], length=1)
    obj(items='abc', length=2)
    obj(items=('a', 'b', 'c'), length=5)
    obj(items='aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:50:48.764642
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # print(Choice().__call__(items=['a', 'b', 'c', 'd', 'e'], length=6))
    print(Choice().__call__(items=('a', 'b', 'c', 'd', 'e'), length=6))
    # print(Choice().__call__(items=('a', 'b', 'c', 'd', 'e'), length=6, unique=True))
    print(Choice().__call__(items='abc', length=10, unique=True))
    print(Choice().__call__(items='abc', length=10, unique=False))
    print(Choice().__call__(items='abc', length=0))
    print(Choice().__call__(items='abc'))
    # print(Choice().__call__(items='abc', length=0, unique=True))

# Generated at 2022-06-13 23:50:59.268350
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice.__call__(Choice(), ['a', 'b', 'c']) in ['a', 'b', 'c']
    assert Choice.__call__(Choice(), ['a', 'b', 'c'], 2) in [['a', 'b'], ['a', 'c'], ['b', 'c']]
    assert Choice.__call__(Choice(), 'aabbbccccddddd', 4, True) in ['cdba', 'bdac', 'dcab']
    assert Choice.__call__(Choice(), ['a', 'b', 'c'], -1) == ValueError
    assert Choice.__call__(Choice(), 3, 1) == TypeError

# Generated at 2022-06-13 23:51:11.539755
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    items = ['a', 'b', 'c']
    items_str = 'abc'
    items_tuple = ('a', 'b', 'c')

    result_element = c(items)
    assert result_element in items

    result_sequence = c(items_str, length=2)
    assert len(result_sequence) == 2
    assert result_sequence in ('ab', 'bc', 'ac')
    #result_sequence == result_sequence[::-1]

    result_sequence = c(items_tuple, length=5)
    assert len(result_sequence) == 5
    #result_sequence == result_sequence[::-1]

    result_sequence = c(items_str, length=4, unique=True)
    assert len(result_sequence) == 4
    assert result_sequence

# Generated at 2022-06-13 23:51:16.733273
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    from random import seed

    # Arrange
    seed(42)
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False

    # Act
    actual = choice(items=items, length=length, unique=unique)

    # Assert
    assert actual == ['b']


# Generated at 2022-06-13 23:51:23.086261
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    items = [1, 2, 3, 4]
    length = 3
    unique = False
    
    data = choice(items, length, unique)
    
    assert len(data) == length
    assert isinstance(data, list)
    assert min(data) >= min(items)
    assert max(data) <= max(items)
    
    print("\nSuccess!\n")

# Generated at 2022-06-13 23:51:25.848094
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    # items=['a', 'b', 'c'], length=0, unique=False
    assert choice(items=['a', 'b', 'c']) == 'c'


# Generated at 2022-06-13 23:51:27.329976
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'



# Generated at 2022-06-13 23:51:33.824703
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

# Generated at 2022-06-13 23:51:40.470217
# Unit test for method __call__ of class Choice
def test_Choice___call__():
  choice = Choice(seed=64)

  assert choice(items=['a', 'b', 'c']) == 'a'
  assert choice(items=['a', 'b', 'c'], length=1) == ['b']
  assert choice(items='abc', length=2) == 'cb'
  assert choice(items=('a', 'b', 'c'), length=5) == ('a', 'c', 'b', 'b', 'a')
  assert choice(items='aabbbccccddddd', length=4, unique=True) == 'ddca'


# Generated at 2022-06-13 23:51:52.983425
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from unittest.mock import Mock, patch, call
    from random import choice
    from mimesis import Choice

    c = Choice()
    items = ['a', 'b', 'c']
    length = len(items)
    assert c(items) in items

    c.random = Mock()
    c(items)
    c.random.choice.assert_called_once_with(items)
    c.random.choice.reset_mock()

    c(items, length)
    c.random.choice.assert_has_calls([call(items)] * length)
    c.random.choice.reset_mock()

    c('abc', length)
    c.random.choice.assert_has_calls([call('abc')] * length)
    c.random.choice.reset_mock()

    c

# Generated at 2022-06-13 23:52:01.330575
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    assert choice(items, length) == ['a']
    
    # input validation
    items = ['a', 'b', 'c']
    length = -1
    assert choice(items, length) == None
    
    items = ['a', 'b', 'c']
    length = 1
    assert choice(items, length) == ['a']
    assert choice(items, length) == ['b']
    


# Generated at 2022-06-13 23:52:08.527259
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['aa', 'ab', 'ac',
                                             'ba', 'bb', 'bc',
                                             'ca', 'cb', 'cc',
                                             ]
    assert choice(items='abc', length=2) in ['aa', 'ab', 'ac',
                                             'ba', 'bb', 'bc',
                                             'ca', 'cb', 'cc',
                                             ]

# Generated at 2022-06-13 23:52:16.156195
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert isinstance(choice(items=('a', 'b', 'c', 'd', 'e'), length=0), str)
    assert isinstance(choice(items=('a', 'b', 'c', 'd', 'e'), length=4), str)
    assert isinstance(choice(items=('a', 'b', 'c', 'd', 'e'), length=4), str)
    assert isinstance(choice(items='abcdefghijklmnopqrstuvwxyz', length=0, unique=True), str)
    assert isinstance(choice(items='abcdefghijklmnopqrstuvwxyz', length=9, unique=True), str)

# Generated at 2022-06-13 23:52:27.914159
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    import pytest

    provider = Choice()

    pytest.raises(ValueError, lambda: provider(items=[], length=5, unique=True))
    pytest.raises(TypeError, lambda: provider(items=[], length='5', unique=True))
    pytest.raises(TypeError, lambda: provider(items=[], length=5, unique='true'))
    pytest.raises(TypeError, lambda: provider(items=Gender.MALE, length=5, unique=True))

    data = provider(items=[1,2,3,4,5], length=5, unique=False)
    assert len(data) == 5 and list in data.__class__.__bases__


# Generated at 2022-06-13 23:52:42.053937
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    class Choice1(Choice):
        pass

    choice = Choice1()

    choice(items=['a', 'b', 'c'])
    choice(items=['a', 'b', 'c'], length=1)
    choice(items='abc', length=2)
    choice(items=('a', 'b', 'c'), length=5)
    choice(items='aabbbccccddddd', length=4, unique=True)

    try:
        choice(items=['a', 'b', 'c'], length='2')
    except TypeError:
        # TypeError: **length** must be integer.
        pass

    try:
        choice(items={'a', 'b', 'c'})
    except TypeError:
        # TypeError: **items** must be non-empty sequence.
        pass



# Generated at 2022-06-13 23:52:46.864026
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    choice(items=['a', 'b', 'c'])
    choice(items=['a', 'b', 'c'], length=1)
    choice(items='abc', length=2)
    choice(items=('a', 'b', 'c'), length=5)
    choice(items='aabbbccccddddd', length=4, unique=True)

test_Choice___call__()

# Generated at 2022-06-13 23:52:56.970297
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    func = Choice()
    assert func(items=['a', 'b', 'c']) == 'c'
    assert func(items=['a', 'b', 'c'], length=1) == ['a']
    assert func(items='abc', length=2) == 'ba'
    assert func(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert func(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:52:59.552289
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    generator = Choice()
    generator(items=['a', 'b', 'c'])



# Generated at 2022-06-13 23:53:08.180700
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    choice = Choice()
    #assert choice(items=['a', 'b', 'c']) == 'c'
    #assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    #assert choice(items='abc', length=2) == 'ba'
    #assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    #assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    #with pytest.raises(TypeError) as err:
    #    choice(items=[1,2,3], length=1.1)
    #assert str(err.value) == '**length** must be integer.'

    #with pytest

# Generated at 2022-06-13 23:53:16.935761
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert isinstance(Choice.__call__(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(Choice.__call__(items='abc', length=2), str)
    assert isinstance(Choice.__call__(items=('a', 'b', 'c'), length=5), tuple)


# Generated at 2022-06-13 23:53:28.133295
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for the method __call__ of class Choice.
    :return: True if test passed, False if test failed.
    """
    choice = Choice()
    if not isinstance(choice(items=['a', 'b', 'c']), str):
        return False
    if not isinstance(choice(items=['a', 'b', 'c'], length=1), list):
        return False
    if not isinstance(choice(items='abc', length=2), str):
        return False
    if not isinstance(choice(items=('a', 'b', 'c'), length=5), tuple):
        return False
    if not isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str):
        return False

# Generated at 2022-06-13 23:53:38.027917
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import os
    from mimesis import Choice, Random, Seed
    from mimesis.enums import Gender

    seed = Seed()
    choice = Choice(random=Random(seed), seed=seed)
    # it should generate random value
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    # it should return a random element from a sequence
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    # it should return list of strings
    assert choice(items='abc', length=2) == 'ba'
    # it should return a random element from a sequence

# Generated at 2022-06-13 23:53:48.613342
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    # добавить assert-ы для остальных значений
    # написать тест для выборки только уникальных элементов
    # и неуникальных элементов
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']

# Generated at 2022-06-13 23:53:52.010593
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Check for TypeError
    for length in [None, 1.0, True]:
        try:
            assert Choice().__call__(items=['a', 'b', 'c'], length=length)
        except TypeError:
            pass

    # Check for ValueError
    for length in [-1, -10]:
        try:
            assert Choice().__call__(items=['a', 'b', 'c'], length=length)
        except ValueError:
            pass

# Generated at 2022-06-13 23:53:59.051761
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print('Unit test method __call__ of class Choice')
    choice = Choice()
    assert isinstance(choice(items=('a', 'b', 'c')), tuple)
    assert isinstance(choice(items=('a', 'b', 'c'), length=1), tuple)
    assert isinstance(choice(items=('a', 'b', 'c'), length=2), tuple)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items=('a', 'b', 'c'), length=0), str)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)
test_Choice___call__()

# Generated at 2022-06-13 23:54:07.887966
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice"""
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ba', 'ac', 'ca', 'bc', 'cb']

# Generated at 2022-06-13 23:54:17.314368
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice(seed=0).__call__(['a', 'b', 'c']) == 'c'
    assert Choice(seed=0).__call__(['a', 'b', 'c'], 1) == ['a']
    assert Choice(seed=0).__call__('abc', 2) == 'ba'
    assert Choice(seed=0).__call__(('a', 'b', 'c'), 5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice(seed=0).__call__('aabbbccccddddd', 4, True) == 'cdba'
    assert Choice(seed=0).__call__('aabbbccccddddd', 0, True) == 'a'

# Generated at 2022-06-13 23:54:32.010680
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    import pytest
    choice = Choice()

    # Test with default value None
    result = choice(items=None, length=None, unique=None)
    assert result

    # Test with default value 0
    result = choice(items=[], length=0, unique=0)
    assert result

    # Test with default value False
    result = choice(items=[], length=0, unique=False)
    assert result

    # Test with list of 2 element
    result = choice(items=['a', 'b'], length=2, unique=False)
    assert result

    # Test with list of 2 element
    result = choice(items=['a', 'b'], length=3, unique=False)
    assert result

    # Test with list of 3 element

# Generated at 2022-06-13 23:54:37.443426
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from random import seed
    from typing import Sequence
    from mimesis.providers.choice import Choice
    seed(0)

    choice = Choice(seed=0)
    statement = choice(items=['a', 'b', 'c'],length=0, unique=False)
    assert statement == 'a'
    statement = choice(items=['a', 'b', 'c'],length=1, unique=False)
    assert statement == ['c']
    statement = choice(items='abc',length=2, unique=False)
    assert statement == 'ac'
    statement = choice(items=('a', 'b', 'c'),length=5, unique=False)
    assert statement == ('c', 'a', 'c', 'c', 'a')

# Generated at 2022-06-13 23:54:52.893264
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis import Choice

    choice = Choice()

    # Test for TypeError
    try:
        choice(items=1, length=1)
    except TypeError:
        pass
    else:
        raise AssertionError('TypeError not raised.')

    try:
        choice(items='abc', length='abc')
    except TypeError:
        pass
    else:
        raise AssertionError('TypeError not raised.')

    # Test for ValueError
    try:
        choice(items=[], length=1)
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError not raised.')

    try:
        choice(items=[1, 2, 3], length=-1)
    except ValueError:
        pass

# Generated at 2022-06-13 23:54:59.080844
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']  # type: ignore
    length = 1
    choice = Choice()
    assert isinstance(choice(items=items), str)
    assert isinstance(choice(items=items, length=length), list)
    assert isinstance(choice(items='abc'), str)
    assert isinstance(choice(items='abc', length=length), str)
    assert isinstance(choice(items=('a', 'b', 'c')), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=length), list)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)



# Generated at 2022-06-13 23:55:01.982621
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""

    assert isinstance(choice(['a', 'b', 'c']), str)
    assert isinstance(choice(['a', 'b', 'c'], length=1), list)
    assert isinstance(choice('abc', length=2), str)
    assert isinstance(choice(('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice('aabbbccccddddd', length=4, unique=True), str)



# Generated at 2022-06-13 23:55:06.866057
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = [('c',), ('a',), ('a',), ('b',), ('c',)]
    assert Choice().__call__(items=('a', 'b', 'c'), length=5) == data

# Generated at 2022-06-13 23:55:16.301532
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    import sys
    import unittest

    class ChoiceTests(unittest.TestCase):

        def setUp(self):
            self.items = ['a', 'b', 'c']
            self.choice = Choice()

        def tearDown(self):
            del self.choice
            del self.items

        def test_not_integer_length(self):
            self.assertRaises(
                TypeError,
                self.choice,
                items=['a', 'b', 'c'],
                length=3.14
            )

        def test_non_sequence_items(self):
            self.assertRaises(
                TypeError,
                self.choice,
                items={1, 2, 3}
            )


# Generated at 2022-06-13 23:55:27.268696
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    actual = Choice().__call__(['a', 'b', 'c'], 1, False)
    expect = 'b'
    assert actual == expect

    actual = Choice().__call__(['a', 'b', 'c'], 2, True)
    expect = ['c', 'a']
    assert actual == expect

    actual = Choice().__call__(['a', 'b', 'c'], 2, False)
    expect = ['c', 'a']
    assert actual == expect

    actual = Choice().__call__(['a', 'b', 'c'], 2, False)
    expect = ['a', 'b']
    assert actual == expect

    actual = Choice().__call__(['a', 'b', 'c'], 1, True)
    expect = ['c']
    assert actual == expect


# Generated at 2022-06-13 23:55:36.095215
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # When the items is empty.
    choice = Choice()
    assert choice(items=[]) == []

    # When the length is a float.
    choice = Choice()
    assert choice(items=['a', 'b', 'c'], length=5.5)
    assert choice('abc', length=2.2)
    assert choice(('a', 'b', 'c'), length=5.5)
    assert choice('aabbbccccddddd', length=4.4, unique=True)

# Generated at 2022-06-13 23:55:44.143901
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    from hypothesis import given
    from . import strategies

    _choice = Choice()

    @given(strategies.anything, strategies.integers, strategies.booleans)
    def test_Choice___call__(items, length, unique):
        # TODO: need fix for a parametric problem
        result = _choice(items, length, unique)
        if length == 0 and isinstance(items, collections.abc.Sequence):
            assert result in items
        if length > 0 and isinstance(items, collections.abc.Sequence):
            assert len(result) == length
            if unique:
                assert len(set(result)) == length
            else:
                assert len(set(result)) == len(result)

    test_Choice___call__()

# Generated at 2022-06-13 23:55:53.006475
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.providers.datetime import Datetime

    person = Person('en', category=Gender.FEMALE)
    choice = Choice(datetime=Datetime())
    choice(items=('a', 'bb', 'ccc', 'dddd'))
    choice(items=('a', 'bb', 'ccc', 'dddd'), length=2)
    choice(items=('a', 'bb', 'ccc', 'dddd'), length=1)
    choice(items='abc', length=7)
    choice(items='abc', length=3)
    choice(items='abc', unique=True, length=3)
    choice(items=person.full_name())
    choice(items=person.full_name(), length=7)

# Generated at 2022-06-13 23:56:02.124992
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice(items='abc', length=2), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)


# Generated at 2022-06-13 23:56:22.981290
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    from mimesis import Choice
    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice(items='abc', length=2), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)

# Generated at 2022-06-13 23:56:26.014441
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert type(c(items=['a', 'b', 'c'], length=1)) == list
    assert type(c(items=['a', 'b', 'c'], unique=True)) == str

# Generated at 2022-06-13 23:56:27.477131
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:56:36.213281
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items='abc', length=2, unique=True) == 'ba'
    assert Choice().__call__(items=('a', 'b', 'c'), length=5, unique=True) == ('c', 'a', 'b', 'b', 'c')
    assert Choice().__call__(items=['a', 'b', 'c'], length=1, unique=True) == ['a']
    assert Choice().__call__(items=('a', 'b', 'c'), length=1, unique=True) == ('a',)
    assert Choice().__call__(items=('a', 'b', 'c'), length=1, unique=False) == ('a',)
    assert Choice().__call__(items='abc', length=1, unique=False) == 'a'
    assert Choice().__call

# Generated at 2022-06-13 23:56:45.805833
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    try:
        choice(items=['a', 'b', 'c'], length=1.1)
        assert False
    except TypeError:
        assert True


# Generated at 2022-06-13 23:56:46.556417
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:56:56.476866
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    # Test 1
    print(choice(items=['a', 'b', 'c'], length=3))
    # Test 2
    print(choice(items=[1, 2, 3], length=4))
    # Test 3
    print(choice(items=[1, 2, 3], length=0))
    # Test 4
    print(choice(items=[1, 2, 3], length=2, unique=True))
    # Test 5
    print(choice(items=['a', 'b', 'c'], length=0))
    # Test 6
    print(choice(items=['a', 'b', 'c'], length=1))

    # Return
    # ['b', 'b', 'c']
    # [1, 3, 1, 3]
    # 1
    # [3, 3]

# Generated at 2022-06-13 23:57:03.992481
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()._Choice__call__(items=['a', 'b', 'c']) == 'a'
    assert Choice()._Choice__call__(items=['a', 'b', 'c'], length=2) == ['b', 'b']
    assert Choice()._Choice__call__(items='abc', length=4) == 'caba'
    assert Choice()._Choice__call__(items=('a', 'b', 'c'), length=5) == ('c', 'c', 'b', 'c', 'c')
    assert Choice()._Choice__call__(items='aabbbccccddddd', length=4, unique=True) == 'acbd'
    assert Choice()._Choice__call__(items=['a', 'b', 'c'], length=1) == ['c']
    assert Choice()._Choice

# Generated at 2022-06-13 23:57:14.305015
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(['a', 'b', 'c'], length=1) == ['a']
    assert choice('abc', length=2) in ['ab', 'bc', 'ac']

# Generated at 2022-06-13 23:57:22.886867
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:58:49.524874
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    data = choice(items=['a', 'b', 'c'])
    assert data in ['a', 'b', 'c']
    assert isinstance(data, str)

    data = choice(items=['a', 'b', 'c'], length=1)
    assert isinstance(data, list)
    assert len(data) == 1

    data = choice(items='abc', length=2)
    assert isinstance(data, str)
    assert len(data) == 2

    data = choice(items=('a', 'b', 'c'), length=5)
    assert isinstance(data, tuple)
    assert len(data) == 5

    data = choice(items='aabbbccccddddd', length=4, unique=True)
    assert isinstance(data, str)

# Generated at 2022-06-13 23:59:03.345631
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert Choice().__call__(['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert Choice().__call__('abc', length=2) in ['ab', 'ac', 'bc']

# Generated at 2022-06-13 23:59:11.029651
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ba', 'ab', 'cb', 'bc']
    assert choice(items=('a', 'b', 'c'), length=5) in [('c', 'a', 'a', 'b', 'c'), ('c', 'b', 'a', 'c', 'a'), ('c', 'b', 'c', 'a', 'a'), ('c', 'b', 'a', 'a', 'c')]

# Generated at 2022-06-13 23:59:16.497876
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = [1, 2, 3, 4, 5]
    length = 10
    unique = False
    choice = Choice(seed=12345678)
    return choice(items, length, unique)

#data = choice(items, length, unique)

if __name__ == '__main__':
    result = test_Choice___call__()
    print(result)

# Generated at 2022-06-13 23:59:21.053119
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # TODO: create a test
    print('TODO: Create a test')



# Generated at 2022-06-13 23:59:30.975761
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c1 = Choice()
    assert c1.__call__(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert c1.__call__(['a', 'b', 'c'], 1) == ['a']
    assert c1.__call__('abc', 2) in ['ba', 'ab', 'cb']

# Generated at 2022-06-13 23:59:34.800406
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    result = choice(items=['a', 'b', 'c'])
    assert isinstance(result, str)


# Generated at 2022-06-13 23:59:45.744523
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import sys, os
    sys.path.append( os.path.abspath('..') )
    from dummy import *

    choice = Choice(random)

    items = ['a', 'b', 'c']
    length = 1
    unique = False

    expect = 'b'
    actual = choice(items=items)
    assert expect == actual

    expect = ['a']
    actual = choice(items=items, length=length)
    assert expect == actual

    expect = 'ba'
    actual = choice(items='abc', length=2)
    assert expect == actual

    expect = ('c', 'a', 'a', 'b', 'c')
    actual = choice(items=('a', 'b', 'c'), length=5)
    assert expect == actual

    expect = 'cdba'

# Generated at 2022-06-13 23:59:55.024614
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data_list = ['a', 'b', 'c']
    data_tuple = ('a', 'b', 'c')
    data_str = 'abc'
    length = 5
    choice = Choice()
    data = choice(data_list)
    assert isinstance(data, str)
    assert len(data) == 1
    data = choice(data_list, length=1)
    assert isinstance(data, list)
    assert len(data) == 1
    data = choice(data_str, length=1)
    assert isinstance(data, str)
    assert len(data) == 1
    data = choice(data_tuple, length=length)
    assert isinstance(data, tuple)
    assert len(data) == length
    data = choice(data_str, length=length, unique=True)
   

# Generated at 2022-06-14 00:00:01.632423
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    obj = Choice('en')
    assert obj.__call__(items=['a', 'b', 'c']) == "c"
    assert obj.__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert obj.__call__(items='abc', length=2) == "ba"
    assert obj.__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert obj.__call__(items='aabbbccccddddd', length=4, unique=True) == "cdba"