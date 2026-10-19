

# Generated at 2022-06-13 23:50:50.782282
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ab', 'ba', 'ac', 'ca', 'bc', 'cb']

# Generated at 2022-06-13 23:51:01.955702
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    from pytest import raises
    with raises(TypeError) as context:
        choice(items=['a', 'b', 'c'], length=True)
    assert '**length** must be integer.' in str(context.value)

# Generated at 2022-06-13 23:51:13.788088
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    len = 1
    unique = False
    res = choice.__call__(items=items, length=len, unique=unique)
    assert(res in items)
    len = 2
    res = choice.__call__(items=items, length=len, unique=unique)
    assert(len(res)==len)
    unique = True
    items = "aabbbccccddddd"
    length = 4
    res = choice.__call__(items=items, length=length, unique=unique)
    assert((isinstance(res,str) or isinstance(res,tuple) or isinstance(res,list)) and len(res) == length and len(set(res)) == length)
    items = (1, 2, 3)


# Generated at 2022-06-13 23:51:25.892785
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'bc', 'ca']

# Generated at 2022-06-13 23:51:33.917457
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c']) == 'c'
    assert Choice().__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice().__call__(items='abc', length=2) == 'ba'
    assert Choice().__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    choice = Choice()
    with pytest.raises(TypeError):
        choice.__call__(items=['a', 'b', 'c'], length='1')

# Generated at 2022-06-13 23:51:41.353956
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()

    assert(choice(items=['a', 'b', 'c']) == 'c')
    assert(choice(items=['a', 'b', 'c'], length=1) == ['a'])
    assert(choice(items='abc', length=2) == 'ba')
    assert(choice(items=('a', 'b', 'c'), length=5) == ('c', 'c', 'b', 'c', 'a'))
    assert(choice(items='aabbbccccddddd', length=4, unique=True) == 'cdbb')


# Generated at 2022-06-13 23:51:49.833132
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()(items=['a', 'b', 'c']) == 'c'
    assert Choice()(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice()(items='abc', length=2) == 'ba'
    assert Choice()(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice()(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert Choice()(items=['a', 'b', 'c'], length=-1) == 'c'
    assert Choice()(items=['a', 'b', 'c'], length=0) == 'a'


# Generated at 2022-06-13 23:51:52.813281
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.builtins import Choice as C
    c = C()
    res = c(items=['a', 'b', 'c'], length=4, unique=True)
    assert isinstance(res, list)
    assert len(res) == 4
    assert len(set(res)) == 4


# Generated at 2022-06-13 23:52:03.477164
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Call method __call__ with default parameters
    choice = Choice()
    items = ['a', 'b', 'c', 'd', 'e']
    result = choice(items=items, length=0)
    assert result in items

    # Call method __call__ with length = 5 and unique = False
    result = choice(items=items, length=5, unique=False)
    assert len(result) == 5
    assert not isinstance(result, str)

    # Call method __call__ with length = 5 and unique = True
    result = choice(items=items, length=5, unique=True)
    assert len(result) == 5
    assert not isinstance(result, str)
    assert result.count(result[0]) == 1
    assert result.count(result[1]) == 1

# Generated at 2022-06-13 23:52:14.201920
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    result = choice(items=['a', 'b', 'c'])
    assert result in ['a', 'b', 'c']

    result = choice(items=['a', 'b', 'c'], length=1)
    assert result in [['a'], ['b'], ['c']]

    result = choice(items='abc', length=2)
    assert result in ['ab', 'ac', 'bc']

    result = choice(items=('a', 'b', 'c'), length=5)

# Generated at 2022-06-13 23:52:27.272072
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test Choice.__call__()."""
    from mimesis import Choice
    choice = Choice()

    assert isinstance(choice.__call__(['a', 'b', 'c']), str)
    assert isinstance(choice.__call__(['a', 'b', 'c'], length=1), list)
    assert isinstance(choice.__call__('abc', length=2), str)
    assert isinstance(choice.__call__(('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice.__call__('aabbbccccddddd', length=4, unique=True),
                      str)

# Generated at 2022-06-13 23:52:32.780640
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:52:39.074966
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:52:49.491032
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    from mimesis.enums import Gender
    from mimesis.builtins.helpers import get_value

    choice = Choice()
    # Test arguments items,length,unique
    assert choice(items=['a', 'b', 'c'], length=0, unique=False) == 'b'
    assert choice(items=['a', 'b', 'c'], length=1, unique=False) == ['a']
    assert choice(items=['a', 'b', 'c'], length=2, unique=False) == ['c', 'b']
    assert choice(items=['a', 'b', 'c'], length=3, unique=False) == ['a', 'b', 'c']

# Generated at 2022-06-13 23:52:58.326007
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ba', 'bc', 'ac', 'ab']

# Generated at 2022-06-13 23:53:06.481241
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice('abc') in 'abc'
    assert choice('abc', 1) == ['a']
    assert choice('abc', 2) in 'ba'
    assert choice('abc', 5) in ('c', 'a', 'a', 'b', 'c')
    assert choice('aabbbccccddddd', 4, unique=True) in 'cdba'

# Generated at 2022-06-13 23:53:20.330430
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis._typing import Sequence
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis import Choice
    from mimesis import Generic

    choice = Choice()
    items = (1, 2, 3, 4)
    choice(items, 1)
    choice(items, 1, True)

    items = 'foo bar baz qux'
    choice(items, 2)
    choice(items, 2, True)

    items = ('foo', 'bar', 'baz', 'qux')
    choice(items, 2)
    choice(items, 2, True)

    items = tuple(range(1, 100))
    choice(items, 100, True)

    items = tuple(range(1, 10))
    choice(items, 20, True)

   

# Generated at 2022-06-13 23:53:29.869831
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    choice = Choice()
    assert type(choice(items=items, length=1)) == list, "Список выбрался"
    assert len(choice(items=items, length=1)) == 1, "Правильное количество элементов"
    assert choice(items='abc', length=2) == 'ba', "Правильный выбор из строки"

# Generated at 2022-06-13 23:53:36.074455
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    from mimesis.providers.choices import Choice


# Generated at 2022-06-13 23:53:43.788982
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:53:59.351052
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    # "a", "b", "c" becomes randomly:
    assert(choice(items=['a', 'b', 'c']) == "c")
    # "a", "b", "c" becomes randomly:
    assert(choice(items=['a', 'b', 'c'], length=1) == ["a"])
    # "a", "b", "c" becomes randomly:
    assert(choice(items='abc', length=2) == "ba")
    # "a", "b", "c" becomes randomly:
    assert(choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c'))
    # "a", "b", "c" becomes randomly:

# Generated at 2022-06-13 23:54:12.640823
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    import pytest
    from pytest import raises

    choice = Choice(random)
    with raises(TypeError):
        choice(items=random.choice(['a', 'b', 'c']), length=1)
    with raises(TypeError):
        choice(items=random.choice(['a', 'b', 'c']), length='1')
    with raises(TypeError):
        choice(items=random.choice(['a', 'b', 'c']), length=-1)
    with raises(TypeError):
        choice(items=1, length=1)
    with raises(TypeError):
        choice(items=2, length=1)
    with raises(ValueError):
        choice(items=[])
    with raises(ValueError):
        choice(items=(), length=1)

# Generated at 2022-06-13 23:54:21.664459
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    choice = Choice(locale='en')
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ba', 'ac', 'ca', 'bc', 'cb']

# Generated at 2022-06-13 23:54:26.316312
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    class SomeChoice(Choice):
        def __init__(self, items):
            self.items = items

    tc = SomeChoice(['a', 'b', 'c'])

    assert tc(items=['a', 'b', 'c']) == 'c'
    assert tc(items=['a', 'b', 'c'], length=1) == ['a']
    assert tc(items='abc', length=2) == 'ba'
    assert tc(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert tc(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:54:31.119050
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    # test1
    c = Choice()
    count = 0
    while count < 10:
        gender = c(items=["Male", "Female"], length=1)
        if gender == Gender.MALE:
            count += 1
    assert gender == Gender.MALE
    # test2
    c = Choice()
    count = 0
    while count < 10:
        gender = c(items=["Male", "Female"], length=1)
        if gender == Gender.FEMALE:
            count += 1
    assert gender == Gender.FEMALE
    # test3
    c = Choice()
    count = 0
    while count < 10:
        gender = c(items=["Male", "Female"], length=1)
        if gender == Gender.MALE:
            count += 1


# Generated at 2022-06-13 23:54:36.297446
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    Choice().__call__(['a', 'b', 'c'])
    Choice().__call__(['a', 'b', 'c'], length=1)
    Choice().__call__('abc', length=2)
    Choice().__call__(('a', 'b', 'c'), length=5)
    Choice().__call__('aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:54:46.602566
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from random import choice
    from string import ascii_letters, digits

    from mimesis.builtins import Choice
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    choice = Choice()
    person = Person('en')

    for _ in range(100):
        items = person.full_name(gender=Gender.MALE).split(' ')
        assert choice(items=items) in items, \
            'Method "__call__" of "Choice" class failed.'

    items = list(ascii_letters)
    length = 100

    for _ in range(100):
        assert sorted(choice(items=items, length=length)) == sorted(
            choice(items=items, length=length)), \
            'Method "__call__" of "Choice" class failed.'



# Generated at 2022-06-13 23:54:51.503758
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=['a', 'b', 'c']) == 'c'
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) == 'ba'
    assert c(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:54:58.817027
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    # TODO: add more tests
    assert c(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert c(items=('a', 'b', 'c')) in ('a', 'b', 'c')  
    assert set([c(items=['a', 'a', 'b']) for i in range(10)]) == set(['a', 'b'])
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) in ['ab', 'ac', 'bc']

# Generated at 2022-06-13 23:55:07.576211
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) and choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) and choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) and choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) and choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')

# Generated at 2022-06-13 23:55:33.873490
# Unit test for method __call__ of class Choice
def test_Choice___call__():
        from mimesis import Choice
        choice = Choice()

        assert choice(items=['a', 'b', 'c']) == 'c'
        assert choice(items=['a', 'b', 'c'], length=1) == ['a']
        assert choice(items='abc', length=2) == 'ba'
        assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
        assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:55:40.902401
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c'])
    assert Choice().__call__(items=['a', 'b', 'c'], length=1)
    assert Choice().__call__(items='abc', length=2)
    assert Choice().__call__(items=('a', 'b', 'c'), length=5)
    assert Choice().__call__(items='aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:55:50.311815
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(["a","b","c"]) in ["a","b","c"]
    assert Choice().__call__(["a","b","c"], 1) in [["a"],["b"],["c"]]
    assert Choice().__call__("abc", 2) in ["ba", "ab", "cb", "ac", "ca", "bc"]

# Generated at 2022-06-13 23:56:00.000388
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # print(Choice().__call__(items=['a', 'b', 'c']))
    assert Choice().__call__(items=['a', 'b', 'c'])
    # print(Choice().__call__(items=['a', 'b', 'c'], length=1))
    assert Choice().__call__(items=['a', 'b', 'c'], length=1)
    # print(Choice().__call__(items='abc', length=2))
    assert Choice().__call__(items='abc', length=2)
    # print(Choice().__call__(items=('a', 'b', 'c'), length=5))
    assert Choice().__call__(items=('a', 'b', 'c'), length=5)
    # print(Choice().__call__(items='aabbbcccc

# Generated at 2022-06-13 23:56:07.194797
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests for method __call__ of class Choice."""
    # test class
    choice = Choice()

    # test __call__ when kwargs is None
    result = choice()

    # test __call__ when kwargs is a sequence (tuple, list, string)
    result = choice(items=['a', 'b', 'c'])
    result = choice(items=[])
    result = choice(items=['a', 'b', 'c'], length=1)
    result = choice(items='abc', length=2)
    result = choice(items=('a', 'b', 'c'), length=5)
    result = choice(items='aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:56:16.874655
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ba', 'ca', 'cb']

# Generated at 2022-06-13 23:56:27.840347
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Testing for correct data
    data_set = [
        {
            'items': ['a', 'b', 'c'],
            'length': 0
        },
        {
            'items': ['a', 'b', 'c'],
            'length': 1
        },
        {
            'items': 'abc',
            'length': 2
        },
        {
            'items': ('a', 'b', 'c'),
            'length': 5
        },
        {
            'items': 'aabbbccccddddd',
            'length': 4,
            'unique': True
        },
    ]  # type: List[Dict[str, Any]]

# Generated at 2022-06-13 23:56:37.732238
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
    except TypeError:
        pass
    else:
        assert False
    try:
        choice(items=123)
    except TypeError:
        pass
   

# Generated at 2022-06-13 23:56:46.547047
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert 'c' == Choice(seed=1)(items=['a', 'b', 'c'])
    assert ['a'] == Choice(seed=1) (items=['a', 'b', 'c'], length=1)
    assert 'ba' == Choice(seed=1) (items='abc', length=2)
    assert ('c', 'a', 'a', 'b', 'c') == Choice(seed=1) (items=('a', 'b', 'c'), length=5)
    assert 'cdba' == Choice(seed=1) (items='aabbbccccddddd', length=4, unique=True)


# Generated at 2022-06-13 23:56:59.792927
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    from mimesis.builtins import Choice
    from mimesis.enums import Fake
    choice = Choice('en')

    # Test with a list of numbers.
    items = [1, 2, 3, 4, 5]
    assert choice(items=items) in items
    assert choice(items=items, unique=True) in items
    assert choice(items=items, length=10) in items

    # Test with a list of strings.
    items = ['a', 'b', 'c', 'd', 'e']
    assert choice(items=items) in items
    assert choice(items=items, unique=True) in items
    assert choice(items=items, length=10) in items

    # Test with a list of strings.