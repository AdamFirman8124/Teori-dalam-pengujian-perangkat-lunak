

# Generated at 2022-06-13 23:50:40.568289
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """
    test__Choice___call__(choice):

    Unit test for method __call__ of class Choice.

    :param choice: Unit test provider instance
    :return: None
    :rtype: None
    """
    choice = Choice()
    assert isinstance(choice(items=[1, 2, 3]), int)
    assert isinstance(choice(items=[1, 2, 3], length=1), list)
    assert isinstance(choice(items=[1, 2, 3], length=2), list)
    assert isinstance(choice(items=[1, 2, 3], length=3), list)
    assert isinstance(choice(items=[1, 2, 3], unique=True), int)
    assert isinstance(choice(items=[1, 2, 3], unique=True, length=1), list)

# Generated at 2022-06-13 23:50:49.585459
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:51:01.608647
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert Choice()(items=['a', 'b', 'c'], length=3) in [['a', 'b', 'c'],
                                                          ['a', 'c', 'b'],
                                                          ['b', 'a', 'c'],
                                                          ['b', 'c', 'a'],
                                                          ['c', 'b', 'a'],
                                                          ['c', 'a', 'b']]
    assert Choice()(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]

# Generated at 2022-06-13 23:51:13.339188
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    
    # Test case 1: 
    choices = Choice()
    list1 = [1, 2, 3, 4, 5, 6]
    assert choices(items=list1) in list1

    # Test case 2: 
    choices = Choice()
    list1 = [1, 2, 3, 4, 5, 6]
    assert len(choices(items=list1, length=1)) == 1

    # Test case 3: 
    choices = Choice()
    string1 = 'abcdefghijklmnopqrstuvwxyz'
    assert choices(items=string1, length=2) in [string1[i] + string1[j] for i in range(len(string1)) for j in range(len(string1))]

    # Test case 4: 
    choices = Choice()

# Generated at 2022-06-13 23:51:25.234592
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.providers import Address
    from mimesis.providers import Person
    from mimesis.providers import Science
    from mimesis.providers import Text
    from mimesis.providers import Web

    p = Person(locale='ru')
    science = Science(locale='ru')
    address = Address(locale='ru')
    web = Web(locale='ru')
    text = Text(locale='ru')


    assert p.gender() in [Gender.MALE, Gender.FEMALE]

# Generated at 2022-06-13 23:51:32.424622
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    import unittest
    from hypothesis import given, assume, example
    from hypothesis.strategies import integers, lists, tuples
    from mimesis import Choice
    from typing import Any, Callable, List

    class ChoiceTestCase(unittest.TestCase):
        """Unit test for method __call__ of class Choice."""

        def setUp(self) -> None:
            """Initialize random, choice and test lists."""
            self.random = random.Random()
            self.choice = Choice()

# Generated at 2022-06-13 23:51:39.814523
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=('a', 'b', 'c')) in ('a', 'b', 'c')
    assert choice(items='abc') in 'abc'



# Generated at 2022-06-13 23:51:48.890804
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.builtins import Choice
    # Setup
    choice = Choice()
    # Exercise
    
    # Verify
    assert type(choice(items=['a', 'b', 'c'])) is str
    assert type(choice(items=['a', 'b', 'c'], length=1)) is list
    assert type(choice(items='abc', length=2)) is str
    assert type(choice(items=('a', 'b', 'c'), length=5)) is tuple
    assert type(choice(items='aabbbccccddddd', length=4, unique=True)) is str
    try:
        choice(2, 3)
    except TypeError:
        pass
    else:
        raise AssertionError('TypeError not raised')

# Generated at 2022-06-13 23:51:56.335408
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Parameter **items** is empty list
    choice = Choice()
    try:
        choice(items=[])
    except ValueError as exc:
        assert str(exc) == '**items** must be a non-empty sequence.'
    else:
        assert False

    # Parameter **length** is float
    choice = Choice()
    try:
        choice(items=['a', 'b', 'c'], length=0.537)
    except TypeError as exc:
        assert str(exc) == '**length** must be integer.'
    else:
        assert False

    # Parameter **items** is not sequence
    choice = Choice()
    try:
        choice(items=0)
    except TypeError as exc:
        assert str(exc) == '**items** must be non-empty sequence.'

# Generated at 2022-06-13 23:52:02.800019
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()('abc') == 'c'
    assert Choice()('abc', 1) == ['c']
    assert Choice()('abc', 2) == 'cb'
    assert Choice()(('a', 'b', 'c'), 5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice()('aabbbccccddddd', 4, True) == 'cdba'


# Generated at 2022-06-13 23:52:15.847246
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    response = choice(items, length, unique)

# Generated at 2022-06-13 23:52:23.493501
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    choice = Choice()
    assert choice(['a', 'b', 'c']) in ['a','b','c']
    assert isinstance(choice(['a', 'b', 'c'], length=1), list)
    assert isinstance(choice([1, 'a', 2]), str)
    assert choice(['a', 'b', 'c'], unique=True) in ['a','b','c']
    assert choice(['a', 'b', 'c'], length=5, unique=True) in ['a','b','c']
    assert choice('abc', length=2) in ['ba', 'ab', 'ac', 'bb', 'bc', 'cb', 'cc']

# Generated at 2022-06-13 23:52:24.011444
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:52:34.535034
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:52:48.051953
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    # Testing with valid values
    # Testing with items=['a', 'b', 'c'], length=0, unique=False
    assert isinstance(choice(items=['a', 'b', 'c']), str) or \
        isinstance(choice(items=('a', 'b', 'c')), tuple)
    # Testing with items=['a', 'b', 'c'], length=1, unique=False
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    # Testing with items='abc', length=2, unique=False
    assert isinstance(choice(items='abc', length=2), str)
    # Testing with items=['a', 'b', 'c'], length=5, unique=False

# Generated at 2022-06-13 23:52:56.279264
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    num = 5

    for _ in range(num):
        res = choice('abc', length=2)
        assert len(res) == 2

    for _ in range(num):
        res = choice(('a', 'b', 'c'), length=2)
        assert len(res) == 2

    for _ in range(num):
        res = choice('aabbbccccddddd', length=4, unique=True)
        assert len(res) == 4


# Generated at 2022-06-13 23:53:03.637341
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test 1. TypeError: For non-sequence items or non-integer length.
    import pytest
    from mimesis.exceptions import NonUniqueError, NonUniqueSequenceError

    choice = Choice()
    with pytest.raises(TypeError):
        choice(items=['a', 'b', 'c'], length='a')
    with pytest.raises(TypeError):
        choice(items=object())
    with pytest.raises(TypeError):
        choice(items=['a', 'b', 'c'], length=1.0)
    with pytest.raises(NonUniqueError):
        choice(items=['a', 'b', 'c'], length=3, unique=True)

# Generated at 2022-06-13 23:53:04.628888
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    Choice()
    return

# Generated at 2022-06-13 23:53:17.339832
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Initialize class Choice
    choice = Choice()

    # Test __call__ method of class Choice
    items = ['a', 'b', 'c']
    assert len(choice(items)) == 1
    assert choice(items) in items
    assert len(choice(items, length=1)) == 1
    assert choice(items, length=1) in items
    assert len(choice(items, length=2)) == 2
    assert choice(items, length=2) in items
    length = 5
    assert len(choice(items, length=length)) == length
    assert choice(items, length=length) in items

    items = 'abc'
    assert len(choice(items, length=2)) == 2
    assert choice(items, length=2) in items

    items = ('a', 'b', 'c')

# Generated at 2022-06-13 23:53:23.950629
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    items_list = ['a', 'b', 'c']
    items_string = 'abc'
    items_tuple = ('a', 'b', 'c')
    items_empty = []
    negative_length = -1
    zero_length = 0
    non_int_length = '2'
    int_length = 2
    unique_constraint = True
    no_unique_constraint = False

    choice = Choice()
    with pytest.raises(TypeError):
        choice(items=items_list, length=non_int_length)
    with pytest.raises(ValueError):
        choice(items=items_list, length=negative_length)
    with pytest.raises(TypeError):
        choice(items=items_string, length=non_int_length)


# Generated at 2022-06-13 23:53:46.086778
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    d = Choice()
    print(d(items=['a', 'b', 'c']))
    print(d(items=['a', 'b', 'c'], length=1))
    print(d(items='abc', length=2))
    print(d(items=('a', 'b', 'c'), length=5))
    print(d(items='aabbbccccddddd', length=4, unique=True))

# Test for testing class method Choice().__call__
if __name__ == '__main__':
    print('Testing class method Choice().__call__')
    test_Choice___call__()

# Generated at 2022-06-13 23:53:57.603582
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    result = choice.__call__(items=['a', 'b', 'c'])
    assert (result in ['a', 'b', 'c'])
    result = choice.__call__(items=['a', 'b', 'c'], length=1)
    assert (result == ['a'] or result == ['b'] or result == ['c'])
    result = choice.__call__(items='abc', length=2)
    assert (result in ['ab', 'ba', 'cb', 'bc', 'ac', 'ca'])
    result = choice.__call__(items=('a', 'b', 'c'), length=5)

# Generated at 2022-06-13 23:54:11.317605
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    meta = Choice.Meta()
    choice = Choice()
    assert meta.name == 'choice'

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ba', 'ab', 'ac', 'bc', 'ca', 'cb']

# Generated at 2022-06-13 23:54:21.479945
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ba', 'ca', 'ac', 'cb', 'bc']

# Generated at 2022-06-13 23:54:23.552538
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    result = choice(items=['a', 'b', 'c'])
    assert result in ['a', 'b', 'c']


# Generated at 2022-06-13 23:54:29.773172
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""
    # Test for non-list items
    items = 'test'
    length = 10
    unique = True
    choice = Choice()
    assert choice(items, length, unique) == 'tttteestt'
    assert isinstance(choice(items, length, unique), str)

    # Test for non-integer length
    items = ['a', 'b', 'c']
    length = 'test'
    unique = True
    choice = Choice()
    try:
        choice(items, length, unique)
    except TypeError:
        pass
    else:
        raise AssertionError('Should raise TypeError')

    # Test for negative length
    items = ['a', 'b', 'c']
    length = -1
    unique = True
    choice = Choice()
   

# Generated at 2022-06-13 23:54:33.390216
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # should return Sequence or uncontained element randomly chosen from items
    items_ = ['a', 'b', 'c']
    length_ = 1
    unique_ = False
    return_value = ['a']
    choice = Choice()
    assert choice(items_, length_, unique_) == return_value

# Generated at 2022-06-13 23:54:43.074462
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:54:51.645133
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.choice import Choice
    assert issubclass(Choice, BaseProvider)
    assert issubclass(Choice, object)
    choice = Choice()
    assert isinstance(choice, Choice)
    assert isinstance(choice, BaseProvider)
    assert isinstance(choice, object)
    assert callable(choice)
    assert (choice(items=['a', 'b', 'c']) in ['a', 'b', 'c'])
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ba', 'ab', 'cb', 'ac']

# Generated at 2022-06-13 23:54:58.622412
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    instance = Choice()
    items_list = ['a', 'b', 'c']
    assert isinstance(instance.__call__(items=items_list), str)
    assert isinstance(instance.__call__(items=items_list), str)
    assert isinstance(instance.__call__(items=items_list), str)
    assert isinstance(instance.__call__(items=items_list, length=1), list)
    assert isinstance(instance.__call__(items='abc', length=2), str)
    assert isinstance(instance.__call__(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(instance.__call__(items='aabbbccccddddd', length=4, unique=True), str)

# Generated at 2022-06-13 23:55:18.390118
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    from mimesis.enums import Gender
    from mimesis.typing import GenderTyped
    from mimesis.exceptions import NonEnumerableError

    choice = Choice('en')
    choice.random.seed(0)
    assert choice(items=['a', 'b', 'c']) == 'a'

    choice = Choice('en', seed=0)
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('a', 'c', 'c', 'c', 'b')

# Generated at 2022-06-13 23:55:23.376714
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    _items = ['a', 'b', 'c']
    _length = 20
    _unique = True
    # Create instance of class Choice
    choice = Choice(locale='en')
    # Check call of method __call__ of class Choice
    assert isinstance(choice(items=_items, length=_length, unique=_unique), str)
    assert callable(choice)

test_Choice___call__()

# Generated at 2022-06-13 23:55:33.455349
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:55:43.547298
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert choice(items=['a', 'b', 'c'], length=1)[0] in ['a', 'b', 'c']
    assert isinstance(choice(items='abc', length=2), str)
    assert set(choice(items='abc', length=2)).issubset(set('abc'))
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)

# Generated at 2022-06-13 23:55:50.601367
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests method __call__ of class Choice."""
    # Setup
    choice = Choice()

    # Exercise
    actual_calls_1 = choice(items=['a', 'b', 'c'])
    actual_calls_2 = choice(items=['a', 'b', 'c'], length=1)
    actual_calls_3 = choice(items='abc', length=2)
    actual_calls_4 = choice(items=('a', 'b', 'c'), length=5)
    actual_calls_5 = choice(items='aabbbccccddddd', length=4, unique=True)

    # Verify
    assert actual_calls_1 in ['a', 'b', 'c']
    assert actual_calls_2 in [['a'], ['b'], ['c']]


# Generated at 2022-06-13 23:55:58.881195
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=['a', 'b', 'c']) == 'c'
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) == 'ba'
    assert c(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    print("test_Choice___call__() passed")


# Generated at 2022-06-13 23:56:07.055535
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis.builtins import Choice
    choice = Choice()

    items = ['a', 'b', 'c']
    res = choice(items=items)
    # assert isinstance(res, str)

    res = choice(items=items, length=1)
    # assert isinstance(res, list)

    items = 'abc'
    res = choice(items=items, length=2)
    # assert isinstance(res, str)

    items = ('a', 'b', 'c')
    res = choice(items=items, length=5)
    # assert isinstance(res, tuple)

    items = 'aabbbccccddddd'
    res = choice(items=items, length=4, unique=True)
    # assert isinstance(

# Generated at 2022-06-13 23:56:16.823876
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print("\n===test_Choice___call__===")
    print("\nTesting Choice.__call__ method")
    choice = Choice()
    print(choice(items=['a', 'b', 'c']))
    print(choice(items=['a', 'b', 'c'], length=1))
    print(choice(items='abc', length=2))
    print(choice(items=('a', 'b', 'c'), length=5))
    print(choice(items='aabbbccccddddd', length=4, unique=True))
    # length is not integer
    try:
        print(choice(items=['a', 'b', 'c'], length=1.5))
    except TypeError as e:
        print("TypeError: " + str(e))
    # items is not sequence


# Generated at 2022-06-13 23:56:27.805244
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Arrange
    choice = Choice()

    # Act 1
    result1 = choice(['a', 'b', 'c'])

    # Act 2
    result2 = choice(['a', 'b', 'c'], 1)

    # Act 3
    result3 = choice('abc', 2)

    # Act 4
    result4 = choice(('a', 'b', 'c'), 5)

    # Act 5
    result5 = choice('aabbbccccddddd', 4, True)

    # Act 6
    result6 = choice('aabbbccccddddd', 4, False)

    # Assert 1
    assert result1 == 'c'

    # Assert 2
    assert result2 == ['a']

    # Assert 3
    assert result3 == 'ba'

    # Assert 4

# Generated at 2022-06-13 23:56:28.415273
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:57:03.630234
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c'], length=4, unique=True) == ['a', 'c', 'b', 'd']


# Generated at 2022-06-13 23:57:10.333451
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=('a', 'b', 'c')) == 'c'
    assert choice(items='abc', length=1) == 'c'
    assert choice(items=('a', 'b', 'c'), length=5) == ('a', 'c', 'b', 'c', 'a')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cbad'

# Generated at 2022-06-13 23:57:21.365136
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()(items=['a', 'b', 'c']) == 'c'
    assert Choice()(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice()(items='abc', length=2) == 'ba'
    assert Choice()(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice()(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert Choice()(length=10, unique=True) == []


# Generated at 2022-06-13 23:57:37.004964
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice(items='abc', length=2), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)
    assert choice(items=[1, 2, 3], length=1) == [2]
    assert choice(items=('a', 'b', 'c'), length=1) == ('a',)
    assert choice(items='abc', length=2) == 'ab'

# Generated at 2022-06-13 23:57:45.776434
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from random import seed

    choice = Choice()
    seed(3)

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['c']
    assert choice(items='abc', length=2) == 'ca'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'b', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cadb'

    try:
        choice(items=[])
    except ValueError as err:
        assert err.args[0] == '**items** must be a non-empty sequence.'

# Generated at 2022-06-13 23:57:54.370590
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    ch = Choice()
    assert ch(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert ch(['a', 'b', 'c'], length=1) == ['a']
    assert ch('abc', length=2) in ['ba', 'bb', 'bc', 'cb', 'cc', 'ca']

# Generated at 2022-06-13 23:58:05.397050
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for the Choice.__call__ method."""
    sequence = Choice()
    assert isinstance(sequence(items=['a', 'b', 'c'], length=4), list)
    assert isinstance(sequence(items=('a', 'b', 'c'), length=4), tuple)
    assert isinstance(sequence(items='abcd', length=4), str)
    assert sequence(items=['a', 'b', 'c'], length=4) == ['c', 'a', 'c', 'c']
    assert sequence(items=('a', 'b', 'c'), length=4) == ('c', 'c', 'a', 'c')
    assert sequence(items='abcd', length=4) == 'ccac'

# Generated at 2022-06-13 23:58:13.777194
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    choice = Choice()
    list_ = ['a', 'b', 'c']
    length = 1
    response = choice(list_, length)
    assert response == ['a']
    assert isinstance(response, list)
    unique = True
    response = choice(list_, length, unique)
    assert response == ['c']
    assert isinstance(response, list)
    response = choice(list_)
    assert isinstance(response, str)
    assert response in list_
    response = choice(list_, 0, unique)
    assert response in list_
    assert isinstance(response, str)
    tuple_ = ('a', 'b', 'c')
    response = choice(tuple_, length)
    assert response == ('a',)
    assert isinstance(response, tuple)

# Generated at 2022-06-13 23:58:22.250595
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c']) == 'c'
    assert Choice().__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice().__call__(items='abc', length=2) == 'ba'
    assert Choice().__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert Choice().__call__(items=[], length=3) == []

# Generated at 2022-06-13 23:58:33.348693
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.providers.datetime import Datetime

    rus = RussiaSpecProvider()
    dt = Datetime()

    expected_values = ['female', 'male']

    choice_obj = Choice(datetime=dt, russia_spec=rus, seed=42)
    result = choice_obj(items=expected_values, length=5, unique=True)
    assert result == ['male', 'male', 'female', 'female', 'male']

    result = choice_obj(items=expected_values, length=5)
    assert result == ['female', 'male', 'male', 'female', 'male']

    result = choice_obj(items=expected_values, length=5, unique=True)