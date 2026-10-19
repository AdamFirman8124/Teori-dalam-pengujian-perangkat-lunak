

# Generated at 2022-06-13 23:50:35.822723
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:50:48.537706
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    data = choice(items=['a', 'b', 'c'])
    assert data == 'c'
    data = choice(items=['a', 'b', 'c'], length=1)
    assert data == ['a']
    data = choice(items='abc', length=2)
    assert data == 'ba'
    data = choice(items=('a', 'b', 'c'), length=5)
    assert data == ('c', 'a', 'a', 'b', 'c')
    data = choice(items='aabbbccccddddd', length=4, unique=True)
    assert data == 'cdba'

    # TODO: Test following conditions
    # TypeError: For non-sequence items or non-integer length.
    # data = choice(items=5, length=5)

# Generated at 2022-06-13 23:50:53.955051
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random

    from mimesis import Choice
    from . import seed

    # Initialise a new class
    choice = Choice()
    # Persistent seed for random generator
    seed(1)
    # Get random elements from sequence
    results = choice(items=('a', 'b', 'c'), length=4, unique=True)
    assert results == ('b', 'c', 'a', 'a')
    # Get random elements from sequence
    results = choice(items=('a', 'b', 'c'), length=4, unique=True)
    assert results == ('b', 'c', 'a', 'a')


# Generated at 2022-06-13 23:51:01.718464
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()

    assert 'b' == choice(items=['a', 'b', 'c'])

    assert ['a'] == choice(items=['a', 'b', 'c'], length=1)

    assert 'cc' == choice(items='abc', length=2)

    assert ('c', 'a', 'b', 'c', 'b') == choice(items=['a', 'b', 'c'], length=5)

    assert 'dcba' == choice(items='aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:51:09.980812
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    print(choice(items=['a', 'b', 'c']))
    print(choice(items=['a', 'b', 'c'], length=1))
    print(choice(items='abc', length=2))
    print(choice(items=('a', 'b', 'c'), length=5))
    print(choice(items='aabbbccccddddd', length=4, unique=True))

if __name__ == "__main__":
    test_Choice__call__()

# Generated at 2022-06-13 23:51:17.443636
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice(seed=1)(items=['a', 'b', 'c']) == 'c'
    assert Choice(seed=1)(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice(seed=1)(items='abc', length=2) == 'ba'
    assert Choice(seed=1)(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice(seed=1)(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:51:24.227723
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    choice = Choice()
    assert choice(items=items) == 'c'
    assert choice(items=items, length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:51:31.776129
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert(True)

    c = Choice()
    # print(c(items=['a', 'b', 'c']))
    # print(c(items=['a', 'b', 'c'], length=1))
    # print(c(items='abc', length=2))
    # print(c(items=('a', 'b', 'c'), length=5))
    # print(c(items='aabbbccccddddd', length=4, unique=True))

    # c(items=['a', 'b', 'c'], length=1)
    # c(items='abc', length=2)
    # c(items='', length=2)
    # h = ['a', '']
    # c(items=h, length=2)
    # c(items=('a', 'b', '

# Generated at 2022-06-13 23:51:41.876772
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    
    from mimesis import Choice
    choice = Choice()
    class_name = 'Choice'
    method_name = '__call__'
    
    # Test Exception: TypeError
    try:
        choice(items=['a', 'b', 'c'], length=1.0)
    except TypeError as e:
        assert(e.args[0] == "**length** must be integer.")
    
    # Test Exception: ValueError
    try:
        choice(items=('a', 'b', 'c'), length=-5)
    except ValueError as e:
        assert(e.args[0] == "**length** should be a positive integer.")
    
    # Test Exception: TypeError

# Generated at 2022-06-13 23:51:52.574218
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    try:
        choice(items=['a', 'b', 'c'], length='foo')
    except TypeError:
        pass
    else:
        assert False


# Generated at 2022-06-13 23:52:02.996709
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Setup
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1

    # Exercise

    # Verify
    assert choice(items=items, length=length) == ['a']

# Generated at 2022-06-13 23:52:14.183858
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    print('choice(items=["a","b","c"]): ', choice(items=["a","b","c"]))
    print('choice(items=["a","b","c"], length=1): ', choice(items=["a","b","c"], length=1))
    print('choice(items="abc", length=2): ', choice(items="abc", length=2))
    print('choice(items=("a","b","c"), length=5): ', choice(items=("a","b","c"), length=5))
    print('choice(items="aabbbccccddddd", length=4, unique=True): ',
          choice(items="aabbbccccddddd", length=4, unique=True))


if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:52:27.177182
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    import itertools


# Generated at 2022-06-13 23:52:31.786675
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    all_items = ['a', 'b', 'c']
    Unique = False
    Length = 1
    c = Choice()
    print(c(all_items, Length, Unique))


test_Choice___call__()

# Generated at 2022-06-13 23:52:36.133304
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    data = [choice(items=['a', 'b', 'c']), choice(items=('a', 'b', 'c'),
                                                   length=1), choice(items='abc', length=2)]
    for d in data:
        assert d

test_Choice___call__()

# Generated at 2022-06-13 23:52:45.766519
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert(choice(items=['a', 'b', 'c']) == 'c')
    assert(choice(items=['a', 'b', 'c'], length=1) == ['a'])
    assert(choice(items='abc', length=2) == 'ab')
    assert(choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'b', 'a', 'b'))
    assert(choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba')
    try:
        choice(items=['a', 'b', 'c'], length='0')
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 23:52:53.051851
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    value1 = choice(items=['a', 'b', 'c'])
    value2 = choice(items=['a', 'b', 'c'], length=1)
    value3 = choice(items='abc', length=2)
    assert value1 == 'c'
    assert value2 == ['a']
    assert value3 == 'ba'


# Generated at 2022-06-13 23:52:58.453333
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice.__call__(items=['a', 'b', 'c']) == 'c'
    assert Choice.__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice.__call__(items='abc', length=2) == 'ba'
    assert Choice.__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice.__call__(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:53:11.071338
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert Choice()(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert Choice()(items='abc', length=2) in ['ab', 'ac', 'bc']

# Generated at 2022-06-13 23:53:24.562396
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    x = Choice()
    print(x.__call__(items=['a', 'b', 'c']))
    print(x.__call__(items=['a', 'b', 'c'], length=1))
    print(x.__call__(items='abc', length=2))
    print(x.__call__(items=('a', 'b', 'c'), length=5))
    print(x.__call__(items='aabbbccccddddd', length=4, unique=True))
    # print(x.__call__(items=['a', 'b', 'c'], length='1'))
    # print(x.__call__(items=['a', 'b', 'c'], length=-1))
    # print(x.__call__(items='abc', length=6,

# Generated at 2022-06-13 23:53:37.181861
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    from mimesis.enums import Gender
    from mimesis.exceptions import NonEnumerableError
    from mimesis.typing import AnyNumber
    from mimesis.providers.datetime import Datetime
    # TODO: Check with Datetime
    dt = Datetime(gender=Gender.FEMALE)
    choice = Choice(dt.datetime)
    choice.seed(456)
    dt1 = choice(dt.datetime(1900, 2010), 10, True)

# Generated at 2022-06-13 23:53:45.013081
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Given
    sequence = ['a', 'b', 'c']
    sequence2 = ['a', 'b', 'b', 'c']

    # When
    # TODO: change to Choice()
    c = Choice(seed=42)

    # Then
    assert c(sequence) == 'c'
    assert c(sequence, length=1) == ['a']
    assert c(('a', 'b', 'c'), length=2) == ('c', 'a')
    assert c(('a', 'b', 'c'), length=3) == ('b', 'b', 'c')
    assert c('aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert c('aabbbccccddddd', length=4, unique=False) == 'ddcc'

# Generated at 2022-06-13 23:53:54.205546
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Unit: Choice.__call__
    ch = Choice()
    assert ch(items=['a', 'b', 'c']) == 'c'
    assert ch(items=['a', 'b', 'c'], length=1) == ['a']
    assert ch(items='abc', length=2) == 'ba'
    assert ch(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert ch(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:54:00.653386
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(
        items=[
            'a',
            'b',
            'c',
        ],
    ) == 'a'
    assert Choice().__call__(
        items=[
            'a',
            'b',
            'c',
        ],
        length=1,
    ) == [
        'a',
    ]
    assert Choice().__call__(
        items='abc',
        length=2,
    ) == 'ba'
    assert Choice().__call__(
        items=(
            'a',
            'b',
            'c',
        ),
        length=5,
    ) == (
        'c',
        'a',
        'a',
        'b',
        'c',
    )

# Generated at 2022-06-13 23:54:10.706321
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a','b','c']) == 'c'
    assert choice(items=['a','b','c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a','b','c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:54:16.720973
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    choice = Choice()
    result = choice(items, length, unique)
    assert isinstance(result, collections.abc.Sequence)
    assert result == ['a']


# Generated at 2022-06-13 23:54:31.644279
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b',
                                                        'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    exception = False
    try:
        choice(items='abc', length='a')
    except TypeError:
        exception = True
    assert exception is True

    exception = False

# Generated at 2022-06-13 23:54:33.466607
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c']) in ['a', 'b', 'c']


# Generated at 2022-06-13 23:54:44.895418
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test for (items: Optional[Sequence[Any]], length: int = 0,
    #           unique: bool = False)
    from mimesis.providers.names import Choice

    choice = Choice()
    choice_str = str(choice)
    assert choice_str
    assert isinstance(choice_str, str)
    assert isinstance(choice, Choice)
    assert isinstance(choice._seed, int)
    assert isinstance(choice._random, str)
    assert isinstance(choice._datetime, str)
    assert isinstance(choice._datetime_format, str)
    assert isinstance(choice._locale, str)

    expectation = 'a'
    result = choice(items=['a', 'b', 'c'])
    assert result == expectation

    expectation = ['a']

# Generated at 2022-06-13 23:54:52.537381
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    from mimesis.providers.datetime import Datetime
    choice = Choice()
    datetime = Datetime()
    print(choice(items=['a', 'b', 'c']))
    print(choice(items=['a', 'b', 'c'], length=1))
    print(choice(items='abc', length=2))
    print(choice(items=('a', 'b', 'c'), length=5))
    print(choice(items='aabbbccccddddd', length=4, unique=True))
    print(choice(items=datetime.timezones(), length=5))

# test_Choice___call__()

# Generated at 2022-06-13 23:55:07.789006
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    seed(1)
    # Provision of proper sequence types for items
    choice = Choice()
    for _ in range(100):
        assert isinstance(choice(items=['a', 'b', 'c'], length=2, unique=True), str)
        assert isinstance(choice(items=('a', 'b', 'c'), length=3), tuple)
        assert isinstance(choice(items=[1, 2, 3], length=4), list)
        assert isinstance(choice(items='a', length=1), str)
    # Provision of single element when length is 0
    choice = Choice()
    for _ in range(100):
        assert isinstance(choice(items=['a', 'b', 'c']), str)


# Generated at 2022-06-13 23:55:18.179598
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Arrange
    choice = Choice()
    items = ['a', 'b', 'c']

    # Act
    actual_1 = choice(items=items)
    actual_2 = choice(items=items, length=1)
    actual_3 = choice(items='abc', length=2)
    actual_4 = choice(items=('a', 'b', 'c'), length=5)
    actual_5 = choice(items='aabbbccccddddd', length=4, unique=True)

    # Assert
    assert actual_1 in items
    assert actual_2 in [items]
    assert actual_3 in ['ba']
    assert actual_4 in [('c', 'a', 'a', 'b', 'c')]
    assert actual_5 in ['cdba']

# Generated at 2022-06-13 23:55:24.037951
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test Choice.__call__ method."""
    items1 = ['a', 'b', 'c']
    items2 = ['a', 'b', 'c', 'd', 'e']
    items3 = ['a', 'b', 'c', 'd', 'a']
    assert Choice()(items1) in items1
    assert Choice()(items1, length=1)[0] in items1
    assert Choice()(items2, length=3, unique=True) in ('abc', 'acb', 'bac', 'bca', 'cab', 'cba')
    assert Choice()(items3, length=3, unique=True)[0] in items3

test_Choice___call__()

# Generated at 2022-06-13 23:55:37.172785
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice()(items=['a', 'b', 'c'], length=0) == 'c'
    assert Choice()(items='abc', length=2) == 'ba'
    assert Choice()(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice()(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    try:
        Choice()(items=['a', 'b', 'c'], length='a')
    except TypeError:
        pass
    try:
        Choice()(items={1, 2, 3})
    except TypeError:
        pass

# Generated at 2022-06-13 23:55:43.945817
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for the method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert len(choice(items=['a', 'b', 'c'], length=1)) == 1
    assert choice(items='abc', length=2) in ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    assert len(choice(items=('a', 'b', 'c'), length=5)) == 5
    assert len(choice(items='aabbbccccddddd', length=4, unique=True)) == 4

# Generated at 2022-06-13 23:55:50.859587
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test Choice.__call__."""
    choice = Choice()

    # Define test data

# Generated at 2022-06-13 23:56:00.225186
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(['a', 'b', 'c'])=='c'
    assert choice(['a', 'b', 'c'], 1)==['a']
    assert choice('abc', 2)=='ba'
    assert choice(('a', 'b', 'c'), 5)==('c', 'a', 'a', 'b', 'c')
    assert choice('aabbbccccddddd' , 4, True)=='cdba'
    #assert choice(('a', 'b', 'c'), -1)==ValueError("**length** should be a positive integer.")
    #assert choice(('a', 'b', 'c'), 100, True)==ValueError("There are not enough unique elements in **items** to provide the specified **number**.")
    #assert choice(('a', 'b', '

# Generated at 2022-06-13 23:56:07.648007
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(('a', 'b', 'c'), length=1)== 'a'
    assert Choice().__call__(('a', 'b', 'c'), length=2)== 'bc'
    assert Choice().__call__(('a', 'b', 'c'), length=4)== 'abcb'
    assert Choice().__call__(('a', 'b', 'c'), length=5)== 'abccb'
    assert Choice().__call__(('a', 'b', 'c'), length=2, unique=True)== 'ac'
    assert Choice().__call__(('a', 'b', 'c'), length=4, unique=True)== 'abcd'
    assert Choice().__call__(('a', 'b', 'c'), length=5, unique=True)== 'abcdc'

# Generated at 2022-06-13 23:56:13.280607
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    from mimesis.compat import str_

    choice = Choice()
    assert str_('a') in choice('abc')
    assert str_('a') in choice('abc', 1)
    assert choice('abc', 2) == 'ba'
    assert choice(('a', 'b', 'c'), 5) == tuple('caabc')

# Generated at 2022-06-13 23:56:25.212970
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['aa', 'bb', 'cc']

# Generated at 2022-06-13 23:57:47.487486
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    result = choice(items=['a', 'b', 'c'])
    assert isinstance(result, str)
    assert len(result) == 1
    assert result in ['a', 'b', 'c']

    result = choice(items=['a', 'b', 'c'], length=1)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in ['a', 'b', 'c']

    result = choice(items='abc', length=2)
    assert isinstance(result, str)
    assert len(result) == 2
    assert result in ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']

    result = choice(items=('a', 'b', 'c'), length=5)

# Generated at 2022-06-13 23:57:58.039071
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    c1 = Choice().__call__(items=['a', 'b', 'c'])
    assert c1 == 'c'
    c2 = Choice().__call__(items=['a', 'b', 'c'], length=1)
    assert c2 == ['a']
    c3 = Choice().__call__(items='abc', length=2)
    assert c3 == 'ba'
    c4 = Choice().__call__(items=('a', 'b', 'c'), length=5)
    assert c4 == ('c', 'a', 'a', 'b', 'c')
    c5 = Choice().__call__(items='aabbbccccddddd', length=4, unique=True)
    assert c5 == 'cdba'

# Generated at 2022-06-13 23:58:01.011720
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print('Testing __call__ of class Choice ... ', end='')
    assert Choice('en').__call__(items='abc', length=2) == 'ba'
    print('Done')



# Generated at 2022-06-13 23:58:11.621269
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = {
        "args": {
            "items": ["a", "b", "c"],
            "length": 0,
            "unique": False,
        },
        "result": 'c'
    }
    assert Choice().__call__(**data['args']) == data['result']
    data = {
        "args": {
            "items": ["a", "b", "c"],
            "length": 1,
            "unique": False,
        },
        "result": ['a']
    }
    assert Choice().__call__(**data['args']) == data['result']
    data = {
        "args": {
            "items": "abc",
            "length": 2,
            "unique": False,
        },
        "result": 'ba'
    }
    assert Choice().__call

# Generated at 2022-06-13 23:58:14.992194
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = [1, 2, 3]
    choice = Choice()
    assert choice(items) in items
    assert choice(items, length=1) in items


# Generated at 2022-06-13 23:58:20.902528
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    ch = Choice()

    items = ['a', 'b', 'c']
    length = 1
    unique = False
    expected = [
        'a',
        'b',
        'c',
    ]
    assert ch(items=items, length=length, unique=unique) in expected

    items = ['a', 'b', 'c']
    length = 1
    unique = False # default
    expected = [
        'a',
        'b',
        'c',
    ]
    assert ch(items=items, length=length) in expected


# Generated at 2022-06-13 23:58:30.264218
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:58:31.550053
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    # data = Choice()
    assert False


# Generated at 2022-06-13 23:58:46.911550
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = 'x'
    assert Choice()(['a', 'b', 'c']) == data, f'{data} != {Choice()(["a", "b", "c"])}'
    data = 'y'
    assert Choice()(['a', 'b', 'c'], 1) == data, f'{data} != {Choice()(["a", "b", "c"], 1)}'
    data = 'z'
    assert Choice()('abc', 2) == data, f'{data} != {Choice()("abc", 2)}'
    data = 'w'
    assert Choice()(('a', 'b', 'c'), 5) == data, f'{data} != {Choice()(("a", "b", "c"), 5)}'
    data = 'v'

# Generated at 2022-06-13 23:58:55.158418
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    # 1
    items = ['a', 'b', 'c']
    result = choice(items=items)
    assert result == 'c'
    # 2
    items = ['a', 'b', 'c']
    result = choice(items=items, length=1)
    assert result == ['a']
    # 3
    items = 'abc'
    result = choice(items=items, length=2)
    assert result == 'ba'
    # 4
    items = ('a', 'b', 'c')
    result = choice(items=items, length=5)
    assert result == ('c', 'a', 'a', 'b', 'c')
    # 5
    items = 'aabbbccccddddd'
    result = choice(items=items, length=4, unique=True)