

# Generated at 2022-06-13 23:50:38.679928
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.providers.choice import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c'], length=0, unique=False) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1, unique=False) == ['a']
    assert choice(items='abc', length=2, unique=False) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5, unique=False) == ('c', 'a', 'a', 'b', 'c')
    assert choice('aabbbccccddddd', 4, True) == 'cdba'

# Generated at 2022-06-13 23:50:50.139037
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    from pytest import raises

    with raises(TypeError):
        choice(items=[1, 2, 3], length=1.5)

    with raises(ValueError):
        choice(items=[1, 2, 3], length=-1)


# Generated at 2022-06-13 23:50:58.820405
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:51:11.497111
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice.

    """
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    try:
        choice(items='abc', length=2.0)
        print('Failed - TypeError: **length** must be integer not float.')
    except TypeError:
        pass
   

# Generated at 2022-06-13 23:51:21.465294
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    abc = ['a', 'b', 'c']
    choice = Choice()

    assert choice(abc, length=0) in abc

    # Should be list type
    assert isinstance(choice(abc, length=1), list)
    assert len(choice(abc, length=1)) == 1
    assert all(x in abc for x in choice(abc, length=1))
    assert all(x in abc for x in choice(abc, length=2))
    assert all(x in abc for x in choice(abc, length=3))
    assert all(x in abc for x in choice(abc, length=4))
    assert all(x in abc for x in choice(abc, length=5))

    # Should be string type
    assert isinstance(choice(abc, length=1, unique=True), str)


# Generated at 2022-06-13 23:51:29.178783
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = [
        ('abc', 1),
        ('abc', 10),
        ('abc', 20),
        ('abc', 50),
        ('abc', 100),
        ('abc', 1000),
        ('abc', 10000),
        ('abc', 100000),
        ('abc', 1000000),
        ('abc', 10000000),
    ]
    for elem, num in data:
        print(f'\n{num} iterations')
        result = [Choice.__call__(elem, length=1, unique=True) for i in range(0, num)]
        assert len(list(set(result))) == len(elem)


if __name__ == "__main__":
    test_Choice___call__()

# Generated at 2022-06-13 23:51:38.027849
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.providers import Choice
    x = Choice()
    y = x.__call__(['a', 'b', 'c'])
    assert  y == 'c'
    y = x.__call__(['a', 'b', 'c'],1)
    assert  y == ['a']
    y = x.__call__('abc',2)
    assert  y == 'ba'
    y = x.__call__(('a', 'b', 'c'),5)
    assert  y == ('c', 'a', 'a', 'b', 'c')
    y = x.__call__('aabbbccccddddd',4,True)
    assert  y == 'cdba'


# Generated at 2022-06-13 23:51:44.672414
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    data = choice('abcd', 2)
    assert isinstance(data, str)
    assert data == 'bc'
    data = choice('abcd', 2, True)
    assert isinstance(data, str)
    assert data == 'cb'
    data = choice('abcd', 4, True)
    assert isinstance(data, str)
    assert data == 'cdba'
    data = choice(['a', 'b', 'c'], 2, True)
    assert isinstance(data, list)
    assert data == ['a', 'c']

# Generated at 2022-06-13 23:51:49.625050
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """ Unit test for method __call__ of class Choice. """
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 3
    unique = True
    counter = 0
    while counter < 10:
        result = choice(items=items, length=length, unique=unique)
        if len(result) == length:
            if unique:
                assert len(set(result)) == len(result)
            counter += 1
        else:
            continue

# Generated at 2022-06-13 23:51:57.754107
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests method __call__ of class Choice."""
    choice = Choice('en')
    # Testing __call__ with a list of length 3.
    choice = Choice('en')
    sample = choice(items=['a', 'b', 'c'], length=0)
    assert sample in ['a', 'b', 'c']
    sample = choice(items=['a', 'b', 'c'], length=3)

# Generated at 2022-06-13 23:52:06.607996
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from . import Choice
    from .person import Person

    person = Person('en')
    choice = Choice('en')
    first_names = [person.name(gender=Gender.MALE), person.name(gender=Gender.FEMALE), person.nickname()]
    print(choice(items=first_names))
    print(choice(items=first_names, length=1))
    print(choice(items='abc', length=2))
    print(choice(items=('a', 'b', 'c'), length=5))
    print(choice(items='aabbbccccddddd', length=4, unique=True))
if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:52:15.122723
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__."""

# Generated at 2022-06-13 23:52:27.060543
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from nose.tools import assert_raises
    from mimesis import Choice
    choice = Choice()

    assert_raises(TypeError, choice, items=123)
    assert_raises(TypeError, choice, items='abc', length='abc')
    assert_raises(ValueError, choice, items=[], length=3)
    assert_raises(ValueError, choice, items='aabbbccccddddd', length=4, unique=True)
    assert_raises(ValueError, choice, items='abc', length=-1)
    assert_raises(ValueError, choice, items='abc', length=0, unique=True)
    assert choice(items='abc', length=0) in 'abc'

# Generated at 2022-06-13 23:52:34.579608
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    ch = Choice()
    for i in range(100):
        if i == 0:
            test = ('2.3.4', '3.3.4', '3.4.4', '4.0.0')
        else:
            test = ['2.3.4', '3.3.4', '3.4.4', '4.0.0']
        assert ch(items=test) in test


# Generated at 2022-06-13 23:52:43.473960
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().choice(['a', 'b', 'c']) == 'c'
    assert Choice().choice(['a', 'b', 'c'], length=1) == ['a']
    assert Choice().choice('abc', length=2) == 'ba'
    assert Choice().choice(('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().choice('aabbbccccddddd', length=4, unique=True) == 'cdba'


# Unit tests for method __call__ of class Choice

# Generated at 2022-06-13 23:52:45.249853
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # TODO: add tests
    pass

# Generated at 2022-06-13 23:52:53.263570
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    choice(list(range(1,10)))
    choice(list(range(1,10)), 5)
    choice(list(range(1,10)), 5, True)
    choice(list(range(1,10)), length = 5, unique = True)
    choice(list(range(1,10)), length = 5)
    choice(list(range(1,10)), unique = True)

# Generated at 2022-06-13 23:52:59.546682
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()('abc', 1) == 'c'
    assert Choice()('abc', 1) == 'c'
    assert Choice()('abc', 2) == 'bc'
    assert Choice()('abc', 3) == 'cab'
    assert Choice()('abc', 4) == 'cbc'
    assert Choice()('abc', 5) == 'bcab'
    assert Choice()('abc', 6) == 'cbca'
    assert Choice()('abc', 7) == 'bcab'
    assert Choice()('abc', 8) == 'cbca'
    assert Choice()('abc', 9) == 'bcac'
    assert Choice()('abc', 10) == 'cbca'
    assert Choice()('abc', 11) == 'bcab'
    assert Choice()('abc', 12) == 'bcba'

# Generated at 2022-06-13 23:53:05.799576
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    provider = Choice()
    # Test method first time
    result_call_method = provider()
    assert isinstance(result_call_method, str)
    assert len(result_call_method) > 0

    # Test method second time
    result_call_method_second_time = provider()
    assert isinstance(result_call_method_second_time, str)
    assert len(result_call_method_second_time) > 0

# Generated at 2022-06-13 23:53:06.943857
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__()

# Generated at 2022-06-13 23:53:22.125116
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method ``__call__`` of class ``Choice``."""
    # Generate a randomly-chosen sequence or bare element from a sequence
    choice = Choice()

    item = choice(items=['a', 'b', 'c'])
    assert isinstance(item, str)
    assert item in ['a', 'b', 'c']

    item = choice(items=['a', 'b', 'c'], length=1)
    assert isinstance(item, list)
    assert item in [['a'], ['b'], ['c']]

    item = choice(items='abc', length=2)
    assert isinstance(item, str)
    assert item in ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']


# Generated at 2022-06-13 23:53:28.203523
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print('Testing Choice.__call__')
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:53:37.742751
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = True

    if not isinstance(length, int):
        raise TypeError('**length** must be integer.')

    if not isinstance(items, collections.abc.Sequence):
        raise TypeError('**items** must be non-empty sequence.')

    if not items:
        raise ValueError('**items** must be a non-empty sequence.')

    if length < 0:
        raise ValueError('**length** should be a positive integer.')

    if length == 0:
        return choice.random.choice(items)

    data = []  # type: ignore

# Generated at 2022-06-13 23:53:48.599139
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert choice.Choice().__call__(items=['a', 'b', 'c']) != 'c'
    assert choice.Choice().__call__(items=['a', 'b', 'c'], length=1) != ['a']
    assert choice.Choice().__call__(items='abc', length=2) != 'ba'
    assert choice.Choice().__call__(items=('a', 'b', 'c'), length=5) != ('c', 'a', 'a', 'b', 'c')
    assert choice.Choice().__call__(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:53:58.284548
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    from random import Random
    from typing import List

    class FakeRandom(object):
        def choice(self, seq: List[Any]) -> Any:
            return seq[0]
    
    # Generate a single element randomly chosen from a list
    choice = Choice(random=FakeRandom())
    print(choice(items=['a', 'b', 'c']))
    
    # Generate a single element randomly chosen from a string
    choice = Choice(random=FakeRandom())
    print(choice(items='abc'))

    # Generate a 2-element string chosen from a string of 4
    choice = Choice(random=FakeRandom())
    print(choice(items='abcd', length=2))
    
    # Generate a single element randomly chosen from a tuple
    choice = Choice(random=FakeRandom())

# Generated at 2022-06-13 23:54:03.276937
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    choice = Choice()

    # Check default values
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert (
        choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba')

    # Check TypeError exceptions
    try:
        choice(items='abc', length=2.2)
    except TypeError:
        pass
    else:
        raise Assertion

# Generated at 2022-06-13 23:54:15.836572
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    from mimesis.exceptions import NonEnumerableError
    from hypothesis import given, strategies as st

    from . import constants

    @given(st.text(alphabet=constants.NONSPACE_ASCII_CHARS,min_size=1),
           st.integers(min_value=0),
           st.booleans())
    def test_Choice___call__(text,length,unique):
        choice=Choice()
        choice(text,length,unique)

    def test_Choice___call__with_empty_list():
        choice=Choice()
        with pytest.raises(NonEnumerableError):
            choice([])

    def test_Choice___call__with_empty_tuple():
        choice=Choice()

# Generated at 2022-06-13 23:54:30.796310
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    obj = Choice()
    # Define test scenarios.

# Generated at 2022-06-13 23:54:38.497936
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    foo = Choice()
    assert foo(items=['a', 'b', 'c']) in {'c', 'a', 'b'}
    assert foo(items=['a', 'b', 'c'], length=1) in {['a'], ['b'], ['c']}
    assert foo(items='abc', length=2) in {'ba', 'cb', 'bc'}
    assert foo(items=('a', 'b', 'c'), length=5) in {('a', 'c', 'b', 'b', 'c'),
                                                    ('c', 'c', 'a', 'a', 'a'),
                                                    ('a', 'c', 'a', 'a', 'c')}

# Generated at 2022-06-13 23:54:48.226221
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    person = Person('en')

    first_names = [person.name(gender=Gender.FEMALE),
                   person.name(gender=Gender.MALE)]
    last_names = [person.surname(gender=Gender.FEMALE),
                  person.surname(gender=Gender.MALE)]

    choice = Choice()

    assert isinstance(choice(first_names), str)
    assert isinstance(choice(items=first_names, length=2), list)
    assert isinstance(choice(items=last_names, length=2), list)
    assert isinstance(choice(items=first_names, length=2, unique=True), list)

# Generated at 2022-06-13 23:54:58.924927
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """
    Test method __call__ of class Choice.
    """
    def __test(items, length=0, unique=False):
        """
        Internal method for testing.
        """
        from mimesis import Choice
        result = Choice().__call__(items, length, unique)
        if unique:
            assert len(result) == length
            for item in result:
                assert result.count(item) == 1
        if length == 0:
            assert result in items
        elif isinstance(items, list):
            assert result == items[:length]
        elif isinstance(items, tuple):
            assert result == items[:length] + tuple()
        else:
            assert result == items[:length]

    __test(items="")
    __test(items=())
    __test(items=[])

   

# Generated at 2022-06-13 23:55:03.536063
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    sequence = ['a', 'b', 'c']
    length = 1
    unique = True
    choice_instance = Choice()
    result = choice_instance(sequence, length, unique)
    assert isinstance(result, str)
    assert len(result) == length
    assert len(set(result)) == length



# Generated at 2022-06-13 23:55:18.143785
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """
    Unit tests for Choice.__call__(...)
    """
    items = ['a', 'b', 'c']
    choice = Choice(seed=42)

    element = choice(items = items)
    assert element == 'b'

    items = ['a', 'b', 'c']
    length = 1
    choice = Choice(seed=42)
    sequence = choice(items = items, length = length)
    assert sequence == ['c']

    items = 'abc'
    length = 2
    choice = Choice(seed=42)
    element = choice(items = items, length = length)
    assert element == 'ab'

    items = ('a', 'b', 'c')
    length = 5
    choice = Choice(seed=42)
    sequence = choice(items = items, length = length)

# Generated at 2022-06-13 23:55:24.223325
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    assert choice(items=items) == 'c'
    assert choice(items=items, length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:55:37.813959
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Verify function Choice.__call__."""
    provider = Choice()
    result = provider(['a', 'b', 'c'])
    assert isinstance(result, str) and result in ['a', 'b', 'c']
    result = provider(['a', 'b', 'c'], length=1)
    assert isinstance(result, list) and len(result) == 1 and result[0] in ['a', 'b', 'c']
    result = provider('abc', length=2)
    assert isinstance(result, str) and len(result) == 2
    result = provider(('a', 'b', 'c'), length=5)
    assert isinstance(result, tuple) and len(result) == 5

# Configuration
if __name__ == '__main__':
    import doctest
    doctest.test

# Generated at 2022-06-13 23:55:44.251120
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice.
    """
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    return

# Generated at 2022-06-13 23:55:53.150348
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random

    from mimesis.typing import Sequence
    from mimesis.enums import Gender

    class Seed:
        """Seed for set random state."""

        def __init__(self, seed: int = 42) -> None:
            """Initializer for set seed for random.

            :param seed: Seed for random.
            """
            self._random = random.Random()
            self._random.seed(seed)


# Generated at 2022-06-13 23:56:04.953074
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.providers import Internet, Person
    from mimesis.providers.misc import Choice
    from mimesis.providers.person.en_US import Providers as Person_en_US
    from mimesis.typing import Seed

    # Given a seed
    seed = Seed(1234567)
    # and a non-empty sequence of elements
    names = Person_en_US.names_male
    # when the Choice class is initialized
    choice = Choice(seed=seed)
    # then the __call__ method of Choice
    assert choice(items=names, length=1) == 'David'

# Generated at 2022-06-13 23:56:13.421927
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    assert choice(items=items) in items
    assert choice(items=items, length=1) in [['a']]
    assert choice(items='abc', length=2) in ['ba']
    assert choice(items=('a', 'b', 'c'), length=5) in [('c', 'a', 'a', 'b', 'c')]
    assert choice(items='aabbbccccddddd', length=4, unique=True) in ['cdba']


# item is not a sequence

# Generated at 2022-06-13 23:56:21.791082
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    result = choice(items=['a', 'b', 'c'])
    assert isinstance(result, str)
    assert len(result) == 1
    assert result in 'abc'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:56:38.058862
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test 1
    choice = Choice()

    assert choice(items = ['a','b','c']) == 'c'

    # Test 2
    assert choice(items = ['a','b','c'], length=1) == ['a']

    # Test 3
    assert choice(items = 'abc', length=2) == 'ba'

    # Test 4
    assert choice(items = ('a','b','c'), length=5) == ('c', 'a', 'a', 'b', 'c')

    # Test 5
    assert choice(items = 'aabbbccccddddd', length=4, unique=True) == 'cdba'



# Generated at 2022-06-13 23:56:47.388642
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ba', 'ac', 'ab']
    assert choice(items=('a', 'b', 'c'), length=5) in [('c', 'a', 'a', 'b', 'c')]
    assert choice(items='aabbbccccddddd', length=4, unique=True) in ['cdba']
    try:
        choice(items={'a', 'b', 'c'})
    except:
        assert True
        print("OK, with error - passed")

# Generated at 2022-06-13 23:56:48.069442
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:56:59.978842
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    output = choice(items=['a', 'b', 'c'])
    assert output == 'c'

    output = choice(items=['a', 'b', 'c'], length=1)
    assert output == ['a']

    output = choice(items='abc', length=2)
    assert output == 'ba'

    output = choice(items=('a', 'b', 'c'), length=5)
    assert output == ('c', 'a', 'a', 'b', 'c')

    output = choice(items='aabbbccccddddd', length=4, unique=True)
    assert output == 'cdba'

    # Test exceptions
    try:
        choice(items=['a', 'b', 'c'], length=1.1)
    except TypeError:
        assert True

# Generated at 2022-06-13 23:57:09.819788
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method Choice.__call__."""
    choice = Choice()
    assert choice(['a', 'b', 'c']) == 'c'
    assert choice(['a', 'b', 'c'], 1) == ['a']
    assert choice('abc', 2) == 'ba'
    assert choice(('a', 'b', 'c'), 5) == ('c', 'a', 'a', 'b', 'c')
    assert choice('aabbbccccddddd', 4, True) == 'cdba'
    assert callable(choice)


# Generated at 2022-06-13 23:57:11.379658
# Unit test for method __call__ of class Choice

# Generated at 2022-06-13 23:57:23.251152
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.providers import Choice
    choice = Choice()

    for _ in range(50):
        assert choice(items=['a', 'b', 'c']) in {'a', 'b', 'c'}

        assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
        assert len(choice(items=['a', 'b', 'c'], length=2)) == 2

        assert choice(items='abc', length=2) in ['ab', 'ba', 'bc', 'cb', 'ca', 'ac']
        assert len(choice(items='abc', length=2)) == 2


# Generated at 2022-06-13 23:57:26.137766
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    choice = Choice()
    assert choice(items=items, length=1) == ['a']

# Generated at 2022-06-13 23:57:27.889654
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__."""
    pass

# Generated at 2022-06-13 23:57:36.857558
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """TODO: Documentation."""
    provider = Choice()
    items = [1, 2, 3, 4, 5]
    length = 3
    unique = False
    x = provider.__call__(items, length, unique)
    isinstance(x, collections.abc.Sequence)
    y = provider.__call__(items, length, unique)
    isinstance(y, collections.abc.Sequence)


# Generated at 2022-06-13 23:58:08.225749
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis import Choice
    from mimesis.exceptions import NonUniqueError
    from mimesis.types import Type

    choice = Choice()
    for i in range(10):
        assert isinstance(choice(items=Type.CARDINALS, length=4,
                                 unique=False), str)
        assert isinstance(choice(items=Type.CARDINALS, length=4,
                                 unique=True), str)
        assert isinstance(choice(items=Type.CARDINAL_WORDS, length=4,
                                 unique=True), str)
        assert isinstance(choice(items=Type.ORDINALS, length=4, unique=True),
                          str)

# Generated at 2022-06-13 23:58:15.894563
# Unit test for method __call__ of class Choice
def test_Choice___call__():

	choice = Choice()

	assert choice(items=['a', 'b', 'c']) == 'c'
	assert choice(items=['a', 'b', 'c'], length=1) == ['a']
	assert choice(items='abc', length=2) == 'ba'
	assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
	assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:58:25.941526
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    c = choice(items = ['a', 'b', 'c'], length = 1)
    if c in ['a', 'b', 'c']:
        print(c)
    c = choice(items = 'abc', length = 3)
    if c in ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc',
             'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc',
             'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']:
        print(c)

# Generated at 2022-06-13 23:58:27.681548
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c']) == 'c'


# Generated at 2022-06-13 23:58:35.184239
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    class Foo:
        def __init__(self, num=0):
            self.num = num


    foo = Foo()
    foo2 = Foo()
    foo3 = Foo()
    # 1. unique=True
    # 1.1. Some containers as inputs
    #     1.1.1. list as inputs
    x = Choice()
    assert x(items=[1, 2, 3], unique=True) in [1, 2, 3]
    assert len(x(items=[1, 2, 3], length=2, unique=True)) == 2
    assert len(x(items=[1, 2, 3], length=5, unique=True)) == 5
    #     1.1.2. tuple as inputs
    assert x(items=(1, 2, 3), unique=True) in [1, 2, 3]

# Generated at 2022-06-13 23:58:49.429158
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Asserts the functionality of Choice.__call__(), the random choice
    from sequence method."""

    from mimesis import Choice
    choice = Choice()
    assert isinstance(choice.__call__(items=['a', 'b', 'c']), str)

    assert choice.choice(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice.choice(['a', 'b', 'c'], unique=True) in ['a', 'b', 'c']
    assert choice.choice(['a', 'b', 'c'], length=1) == ['a']
    assert choice.choice(['a', 'b', 'c'], length=5) == ['c', 'a', 'a', 'b', 'c']

# Generated at 2022-06-13 23:59:03.230171
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice.__call__(items=['a', 'b', 'c']) == 'c'
    assert choice.__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice.__call__(items='abc', length=2) == 'ba'
    assert choice.__call__(items=('a', 'b', 'c'), length=5) == ('c',
            'a', 'a', 'b', 'c')
    assert choice.__call__(items='aabbbccccddddd', length=4,
                           unique=True) == 'cdba'

# Generated at 2022-06-13 23:59:12.454574
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    random_ = Choice()

# Generated at 2022-06-13 23:59:20.210000
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    _choice_ = Choice()
    _choice_(list(range(5)))
    _choice_([-1, 0, 1])
    _choice_('abcd', length=0)
    _choice_((-1, 0, 1), length=1)
    _choice_({'one': 1, 'two': 2, 'three': 3}, length=2)
    _choice_(list(range(5)), length=5)
    _choice_(('a', 'b', 'c'), length=5)
    _choice_({'a', 'b', 'c'}, length=5)
    _choice_('aabbbccccddddd', length=4, unique=True)
    _choice_('', length=4)
    _choice_('aabbbccccddddd', length=15, unique=True)
    _

# Generated at 2022-06-13 23:59:30.504037
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from hypothesis import given
    from hypothesis.strategies import integers, lists, one_of, text
    from mimesis.providers.datetime import datetime
    from .check import check_provider

    @given(
        lists(elements=text(), min_size=1),
        one_of(integers(min_value=0, max_value=100), integers()),
        text(max_size=1),
    )
    def test(items, length, unique):
        try:
            datetime = Choice(datetime.seed)
            assert datetime(items, length, unique)
        except ValueError:
            pass

    class CustomProvider(BaseProvider):
        foo = Choice()

    check_provider(CustomProvider)
    test()
