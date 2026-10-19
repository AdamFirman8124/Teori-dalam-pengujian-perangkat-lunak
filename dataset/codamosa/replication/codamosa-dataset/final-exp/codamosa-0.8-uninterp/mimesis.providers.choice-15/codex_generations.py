

# Generated at 2022-06-13 23:50:39.609636
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice.

    The method __call__ is the primary entry point for the class and is
    responsible for providing the primary features for the class provided by
    the class. The ``items`` parameter is the only required parameter and must
    be a non-empty list. The ``length`` parameter specifies the number of items
    to provide and the ``unique`` parameter specifies that the provided items
    must all be unique.
    """
    # Define a list of values items to be randomly chosen from
    items = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]

    # Create an instance of the class with default locales
    choice = Choice()

    # Assert that the items obtained from calling the class method __call__
    # with the items argument as a list and the length argument as

# Generated at 2022-06-13 23:50:50.558297
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    
    c = Choice()
    
    assert c(items=["apple", "mango", "banana"]) in ["apple", "mango", "banana"]
    
    assert c(items=["apple", "mango", "banana"], length=1) in [["apple"], ["mango"], ["banana"]]
    
    assert c(items="apple", length=2) in ["ap", "pp", "pa"]
    

# Generated at 2022-06-13 23:51:00.871467
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    assert choice('abc') in 'abc'
    assert choice('abc', length=1) == 'a'
    assert choice('abc', length=2) in ['ba', 'ab', 'cb']
    assert choice(('a', 'b', 'c'), length=5) in [
        ('c', 'a', 'a', 'b', 'c'),
        ('b', 'b', 'c', 'c', 'a'),
        ('a', 'a', 'b', 'a', 'c'),
    ]
    assert choice('aabbbccccddddd', length=4, unique=True) in 'abcd'

# Generated at 2022-06-13 23:51:11.947547
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    list1 = ['a', 'b', 'c']
    list2 = ['a', 'b', 'c', 'd']
    list3 = ['a', 'b', 'c', 'd', 'e', 'f']
    list4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    list5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Test 1
    choice = Choice()
    assert choice(list1) == 'c'

    # Test 2

# Generated at 2022-06-13 23:51:14.888930
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c'], length=0, unique=False) == 'c'


# Generated at 2022-06-13 23:51:26.201177
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in 'abc'
    assert choice(items=['a', 'b', 'c'], length=1) in (['a'], ['b'], ['c'])
    assert choice(items='abc', length=2) in ('ab', 'ac', 'bc')

# Generated at 2022-06-13 23:51:27.046765
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass


# Generated at 2022-06-13 23:51:34.555376
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    from hypothesis import given
    from tests.strategies.data_types import some_sequences

    @given(items=some_sequences())
    def test_return_value(items):
        assert isinstance(Choice().__call__(items=items), str)

    @given(items=some_sequences())
    def test_type_error_for_non_string_items(items):
        if not isinstance(items, str):
            with pytest.raises(TypeError):
                Choice().__call__(items=items)

    def test_value_error_for_empty_items():
        with pytest.raises(ValueError):
            Choice().__call__(items='')


# Generated at 2022-06-13 23:51:44.168433
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    choice = Choice()
    result1 = choice(items=['a', 'b', 'c'], length=1)
    assert result1 in ['a', 'b', 'c']
    result2 = choice(items=['a', 'b', 'c'], length=3)
    assert len(result2) == 3
    for item in result2:
        assert item in ['a', 'b', 'c']
    result3 = choice(items=['a', 'b', 'c'], length=1, unique=True)
    assert result3 in ['a', 'b', 'c']
    result4 = choice(items=['a', 'b', 'c'], length=3, unique=True)
    assert len(set(result4)) == 3

# Generated at 2022-06-13 23:51:51.821567
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    # TODO: explicit type hint for data.
    c = Choice()
    items = ['a', 'b', 'c']

    data = c(items=items)
    assert data in items

    data = c(items=items, length=1)
    assert data == ['a'] | ['b'] | ['c']

    data = c(items='abc', length=2)
    assert data in ['ab'] | ['ac'] | ['ba'] | ['bc'] | ['ca'] | ['cb']

    data = c(items=('a', 'b', 'c'), length=5)

# Generated at 2022-06-13 23:52:06.981745
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis import Choice
    from mimesis.builtins import Seed
    seed = Seed()
    choices = Choice(seed)

    #def __init__(self, *args, **kwargs):
    #def __call__(self, items: Optional[Sequence[Any]], length: int = 0,
    #             unique: bool = False) -> Union[Sequence[Any], Any]:

    items = ['a', 'b', 'c']
    length = 1
    items = ('a', 'b', 'c')
    length = 5
    items = 'abc'
    length = 2
    items = 'aabbbccccddddd'
    length = 4
    unique = True

# Generated at 2022-06-13 23:52:15.324382
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from unittest import TestCase
    from unittest.mock import patch, Mock

    from mimesis import Choice
    from mimesis.typing import Sequence

    class TestChoice(TestCase):

        def setUp(self) -> None:
            self.cn = Choice(seed=1)

        def test_negative_length(self):
            with self.assertRaises(ValueError):
                self.cn(items=['a', 'b', 'c'], length=-1)

        def test_non_sequence(self):
            with self.assertRaises(TypeError):
                self.cn(items=1, length=1)


# Generated at 2022-06-13 23:52:26.760643
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.schema import Field
    from mimesis.providers.person import Person
    from mimesis.providers.address import Address

    choice = Choice()
    person = Person()
    address = Address()

    schema = {
        'name': Field(
            # TODO: Default value is enough
            default=person.full_name(gender=Gender.MALE)
        ),
        'address': Field(
            # TODO: Default value is enough
            default=address.address()
        ),
        'age': Field()
    }

    result = choice(schema, length=2)
    assert isinstance(result, list)
    assert len(result) == 2

# Generated at 2022-06-13 23:52:37.025983
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for the method __call__ of class Choice."""
    from mimesis import Choice
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = True
    assert choice(items, length, unique) in items

    assert choice(items, length=1) == ['a']
    assert len(choice(items, length=0)) == 1
    assert choice(items, unique=True) in items
    assert type(choice(items, unique=True)) == str
    assert isinstance(choice(items, length=1), list)
    assert isinstance(choice(items, length=2), tuple)
    assert isinstance(choice(items, unique=True), str)
    assert len(choice(items, length=5)) == 5

# Generated at 2022-06-13 23:52:45.438338
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test 1:
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    # Test 2:
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    # Test 3:
    assert choice(items='abc', length=2) == 'ba'
    # Test 4:
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    # Test 5:
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:52:56.823573
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(['a','b','c','d','e','f'], length=2) in (['d','c'], ['a','b'])
    assert c(('a','b','c'), length=3) in (('c','a','c'), ('a','b','a'))
    assert c(['a','b','c','d','e'], length=1) in (['a'], ['b'], ['c'], ['d'], ['e'])
    assert c('abcde', length=5) in ('ddaac', 'cbdae')
    assert c('abcde', length=0) in ('a', 'b', 'c', 'd', 'e')

# Generated at 2022-06-13 23:53:04.125880
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=[1, 2, 3]) in [1, 2, 3]
    assert choice(items=[1, 2, 3], length=1) == [1]
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'b')
    assert choice(items='aabbbccccddddd', length=4, unique=True) in ['cdba', 'bdac']

# Generated at 2022-06-13 23:53:04.638031
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:53:17.339357
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    # case 1
    items = ['a', 'b', 'c']
    length = 3
    unique = True
    assert choice(items, length, unique) in items

    # case 2
    assert isinstance(choice(['a', 'b', 'c', 'd'], 2, unique), list)

    # case 3
    unique = False
    assert choice(['a', 'b', 'c', 'd'], 3, unique) in items

    # case 4
    length = 0
    assert choice(items, length, unique) in items

    # case 5
    items = 123
    try:
        choice(items, length, unique)
        raise
    except TypeError as e:
        assert str(e) == '**items** must be non-empty sequence.'

    # case 6

# Generated at 2022-06-13 23:53:28.170479
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice(items='abc', length=2), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)
    try:
        choice(items=['a', 'b', 'c'], length='fsa')
        assert False
    except TypeError:
        assert True
    try:
        choice(items=None, length=5)
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 23:53:44.900088
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    obj = Choice()
    res = obj.__call__(items=['a', 'b', 'c'], length=1, unique=False)
    assert res == ['b']

    res = obj.__call__(items=['a', 'b', 'c'], length=2, unique=False)
    assert res == ['b', 'b']



# Generated at 2022-06-13 23:53:52.968920
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit tests for method __call__ of class Choice."""

    choice = Choice()
    data = choice(['a', 'b', 'c'])
    assert isinstance(data, str)
    data = choice(['a', 'b', 'c'], 1)
    assert isinstance(data, list)
    assert len(data) == 1
    data = choice('abc', 2)
    assert isinstance(data, str)
    assert len(data) == 2
    data = choice(('a', 'b', 'c'), 5)
    assert isinstance(data, tuple)
    assert len(data) == 5
    data = choice('aabbbccccddddd', 4, unique=True)
    assert isinstance(data, str)
    assert len(data) == 4

# Generated at 2022-06-13 23:54:00.069751
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    item = Choice()
    assert item.__call__(items=['a', 'b', 'c']) == 'a'
    assert item.__call__(items=['a', 'b', 'c'], length=1) == ['b']
    assert item.__call__(items='abc', length=1) == 'b'
    assert item.__call__(items=('a', 'b', 'c'), length=5) == ('c', 'b', 'a', 'c', 'b')
    assert item.__call__(items='aabbbccccddddd', length=4, unique=True) == 'baad'
    try:
        assert item.__call__(items=('a', 'b', 'c'), length='a')
    except TypeError:
        pass

# Generated at 2022-06-13 23:54:12.961574
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    item = ['a', 'b', 'c']
    s = Choice()
    assert isinstance(s(item), str)
    assert s(item) in item
    assert isinstance(s(item, length=1), list)
    assert s(item, length=1) in [[i] for i in item]
    assert isinstance(s(item, length=2), list)
    assert s(item, length=2) in list(map(''.join, [[i, j] for i in item for j in item]))
    assert isinstance(s(item, length=3), list)
    assert s(item, length=3) in list(map(''.join, [[i, j, k] for i in item for j in item for k in item]))
    assert isinstance(s(item, length=4), list)
   

# Generated at 2022-06-13 23:54:17.832383
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()

    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=('a', 'b', 'c')), str)
    assert isinstance(choice(items='abc'), str)



# Generated at 2022-06-13 23:54:26.722480
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice.

    test if the method generates a sequence of random choices from
    a given sequence of elements.
    """
    from mimesis import Choice
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    choice = Choice()
    person = Person('en')
    gender_choices = ['female', 'male', 'other']
    genders = [gender for gender in Gender]

# Generated at 2022-06-13 23:54:36.894571
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test for positive integer length
    choice = Choice(random=False)

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    # Test for negative length
    try:
        choice(items='abc', length=-5)
    except ValueError:
        assert True
    else:
        assert False
    # Test for non-integer length

# Generated at 2022-06-13 23:54:44.757164
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """
    # Unit test for method __call__ of class Choice
    """
    import random
    import sys

    random.seed(1)
    choice = Choice()

    # print(choice(items=['a', 'b', 'c']))
    # print(choice(items=['a', 'b', 'c'], length=1))
    # print(choice(items='abc', length=2))
    # print(choice(items=('a', 'b', 'c'), length=5))
    print(choice(items='aabbbccccddddd', length=4, unique=True))


# Generated at 2022-06-13 23:54:53.276846
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # 1. Test when items neither list nor tuple nor string
    import pytest
    c = Choice()
    with pytest.raises(TypeError):
        c(1, 1)
    with pytest.raises(TypeError):
        c('a', 1)
    with pytest.raises(TypeError):
        c({'a': 1}, 1)
    # 2. Test when length not integer
    with pytest.raises(TypeError):
        c(['a', 'b', 'c'], '1')
    # 3. Test when items is empty
    with pytest.raises(ValueError):
        c([])
    # 4. Test when length is negative
    with pytest.raises(ValueError):
        c(['a', 'b', 'c'], -1)
    # 5. Test when

# Generated at 2022-06-13 23:55:05.070085
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    provider = Choice()
    assert isinstance(provider.__call__(['a', 'b', 'c', 'd', 'e']), str)
    assert isinstance(provider.__call__(('a', 'b', 'c', 'd', 'e')), tuple)
    assert isinstance(provider.__call__(('a', 'b', 'c', 'd', 'e'),length=5), tuple)
    assert isinstance(provider.__call__(('a', 'b', 'c', 'd', 'e'),length=6), tuple)
    assert isinstance(provider.__call__(('a', 'b', 'c', 'd', 'e'),length=1), tuple)

# Generated at 2022-06-13 23:55:27.245273
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ('a', 'b', 'c')
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ('ba', 'ac', 'cb')
    assert choice(items=('a', 'b', 'c'), length=5) in (('c', 'a', 'a', 'b', 'c'), ('c', 'c', 'b', 'b', 'a'), ('c', 'c', 'a', 'a', 'b'))

# Generated at 2022-06-13 23:55:39.012868
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    from mimesis import Choice

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in {'a', 'b', 'c'}
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in {'ab', 'ac', 'ba', 'bc', 'ca', 'cb'}

# Generated at 2022-06-13 23:55:45.656369
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for Choice class.
    @param Choice: Choice
    @type Choice: Class
    @return: None
    @rtype: None
    """
    # Define an object of class Choice
    choice = Choice(random.randint(0, 100))
    # Initialize the items
    items = [1, 2, 3]
    # Get a random choice from the items
    choice_1 = choice._call_(items)
    # Check the result
    assert choice_1 in items
    # Initialize the items
    items = ['a', 'b', 'c']
    # Get a random choice from the items
    choice_2 = choice._call_(items, length=1)
    # Check the result
    assert choice_2 == ['a']
    # Initialize the items
    items = 'abc'
    # Get a random choice

# Generated at 2022-06-13 23:55:51.924724
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    ch = Choice()

    assert ch('a') == 'a'
    assert ch(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert ch(('a', 'b', 'c')) in ['a', 'b', 'c']
    assert ch(['a', 'b', 'c'], 0) in ['a', 'b', 'c']
    assert ch(('a', 'b', 'c'), 0) in ['a', 'b', 'c']
    assert ch(['a', 'b', 'c'], 1) in [['a'], ['b'], ['c']]
    assert ch(('a', 'b', 'c'), 1) in [['a'], ['b'], ['c']]

# Generated at 2022-06-13 23:55:54.280441
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Choice: Test method ``__call__``."""



# Generated at 2022-06-13 23:56:04.104408
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'



# Generated at 2022-06-13 23:56:15.097759
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # TODO: Add real tests
    assert 'a' == Choice().__call__(items=('a', 'b', 'c'))
    assert 'ba' == Choice().__call__(items='abc', length=2)
    assert 'cba' == Choice().__call__(items='abc', length=3)
    assert 'cadb' == Choice().__call__(items='abc', length=4)
    assert 'abc' == Choice().__call__(items='abc', length=3)
    assert 'ab' == Choice().__call__(items='ab', length=3)
    assert 'ab' == Choice().__call__(items='ab', length=2)
    assert 'a' == Choice().__call__(items='ab', length=1)
    # assert 'a' == Choice().__call__(items='

# Generated at 2022-06-13 23:56:26.419142
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    class TestChoice:

        def test_items(self):
            assert Choice().__call__(['a', 'b', 'c']) in ['a', 'b', 'c']

        def test_length(self):
            assert len(Choice().__call__(['a', 'b', 'c'], length=2)) == 2

        def test_length_negative(self):
            try:
                Choice().__call__(['a', 'b', 'c'], length=-1)
            except ValueError:
                pass

        def test_items_tuple(self):
            result = Choice().__call__(('a', 'b', 'c'))
            assert isinstance(result, str)
            assert result in ['a', 'b', 'c']

        def test_items_string(self):
            result = Choice().__

# Generated at 2022-06-13 23:56:35.926711
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    choice = Choice()
    assert choice(items=items) in items
    assert len(choice(items=items, length=1)) == 1
    assert choice(items='abc', length=2) in ['ba', 'ab', 'ac']
    assert len(choice(items=('a', 'b', 'c'), length=5)) == 5
    assert len(choice(items=('a', 'b', 'c'), length=5, unique=True)) == 5
    assert choice(items='aabbbccccddddd', length=4, unique=True) in ['cdba', 'dbca', 'bcad', 'bcda', 'dcab', 'cabd']

# Generated at 2022-06-13 23:56:41.895887
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test generation a random choice from items in a sequence."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    #raise ValueError for non-empty sequence
    try:
        choice(items=[])
    except ValueError:
        pass
    else:
        assert False

    #raise ValueError for negative length

# Generated at 2022-06-13 23:57:11.541898
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    items = ['a', 'b', 'c']
    length = 1
    unique = False
    res = Choice()(items, length, unique)
    assert res == ['a']

    length = 2
    unique = True
    res = Choice()(items, length, unique)
    assert res == ['a', 'b']

# Generated at 2022-06-13 23:57:23.343629
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender

    c = Choice('en', gender=Gender.MALE)
    assert c(items=[1, 2, 3, 4], length=1) == [3]
    assert isinstance(c(items=[1, 2, 3, 4], length=1), list)
    assert c(items=(1, 2, 3, 4), length=2) == (2, 3)
    assert isinstance(c(items=(1, 2, 3, 4), length=2), tuple)
    assert c(items='abcd', length=3) == 'cda'
    assert isinstance(c(items='abcd', length=3), str)
    assert c(items=[1, 2, 3, 4]) in [1, 2, 3, 4]

# Generated at 2022-06-13 23:57:32.530120
# Unit test for method __call__ of class Choice
def test_Choice___call__():
	c = Choice()
	assert c(items=['a','b','c']) == 'c'
	assert c(items=['a','b','c'], length=1) == ['a']
	assert c(items='abc', length=2) == 'ba'
	assert c(items=('a','b','c'), length=5) == ('c', 'a', 'a', 'b', 'c')
	assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:57:37.550062
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Arrange
    choice = Choice()
    items = ['a', 'b', 'c']

    # Act
    result = choice(items, length=1)

    # Assert
    assert result == ['a']


# Generated at 2022-06-13 23:57:46.071955
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    # Check return value with length = 0
    assert choice(items=['a', 'b', 'c'], length=0) in ('a', 'b', 'c')
    # Check return value with length = 1
    assert choice(items=['a', 'b', 'c'], length=1) in ['a', 'b', 'c']
    # Check return value with length = 2
    assert choice(items=['a', 'b', 'c'], length=2) in ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    # Check TypeError for incorrect items value
    try:
        choice.__call__(items=None, length=0)
    except TypeError:
        pass
    # Check TypeError for incorrect length value

# Generated at 2022-06-13 23:57:53.617172
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:58:05.122955
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']

# Generated at 2022-06-13 23:58:06.156763
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 23:58:07.058615
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass



# Generated at 2022-06-13 23:58:15.285697
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()

    # Test for small string
    for _ in range(100):
        assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']

    # Test for small string and small length
    for _ in range(100):
        assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]

    # Test for small string and default length
    for _ in range(100):
        assert choice(items='abc') in 'abc'

    # Test for small string and small length
    for _ in range(100):
        assert choice(items='abc', length=2) in ['ab', 'ac', 'bc']

    # Test for small tuple and

# Generated at 2022-06-13 23:59:07.087347
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    length = 1
    unique = True
    result = Choice().__call__(items, length, unique)
    assert isinstance(result, str) or isinstance(result, list) or isinstance(result, tuple)

# Generated at 2022-06-13 23:59:13.314165
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.schema import Field

    field = Field('choice.__call__')

    for i in range(0, 10):
        print(field.process(items=[1, 2, 3, 4, 5, 6, 7], length=3, unique=True,
                            choiceType=int))

# Generated at 2022-06-13 23:59:20.505580
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    #
    # Unit test for method __call__ of class Choice
    choice = Choice()

    expected = 'c'
    actual = choice(items=['a', 'b', 'c'])
    assert actual == expected

    expected = ['a']
    actual = choice(items=['a', 'b', 'c'], length=1)
    assert actual == expected

    expected = 'ba'
    actual = choice(items='abc', length=2)
    assert actual == expected

    expected = ('c', 'a', 'a', 'b', 'c')
    actual = choice(items=('a', 'b', 'c'), length=5)
    assert actual == expected

    expected = 'cdba'

# Generated at 2022-06-13 23:59:30.784834
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    Item = Choice()
    # args: items: List[Any], length: int = 0, unique: bool = False
    # __call__(self, items: Optional[Sequence[Any]], length: int = 0,
    #         unique: bool = False) -> Union[Sequence[Any], Any]:
        # Provide elements randomly chosen from the elements in a sequence
        # **items**, where when **length** is specified the random choices are
        # contained in a sequence of the same type of length **length**,
        # otherwise a single uncontained element is chosen. If **unique** is set
        # to True, constrain a returned sequence to contain only unique
        # elements.

    # items = ['a', 'b', 'c']
    items = ['a', 'b', 'c']
    # length = 0
    length = 0
    #

# Generated at 2022-06-13 23:59:33.309635
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    print(choice(items=['a', 'b', 'c'], length=1))
    print(choice(items=['a', 'b', 'c'], length=2))


# Generated at 2022-06-13 23:59:44.481594
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from pytest import raises
    from collections.abc import Sequence

    choice = Choice()
    assert isinstance(choice(['a', 'b', 'c']), str)
    assert choice(['a', 'b', 'c']) in ['a', 'b', 'c']

    assert isinstance(choice(['a', 'b', 'c'], length=1), list)
    assert choice(['a', 'b', 'c'], length=1) == ['a']

    assert isinstance(choice('abc', length=2), str)
    assert choice('abc', length=2) in ['ba', 'ab', 'cb', 'ac', 'bc']

    assert isinstance(choice(['a', 'b', 'c'], length=5), list)

# Generated at 2022-06-13 23:59:51.443279
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.providers import Choice
    # test 1
    items = ['a', 'b', 'c']
    length = 0
    unique = False
    choice = Choice()
    assert type(choice(items, length, unique)) == str
    # test 2
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    choice = Choice()
    assert type(choice(items, length, unique)) == list
    # test 3
    items = 'abc'
    length = 2
    unique = False
    choice = Choice()
    assert type(choice(items, length, unique)) == str
    # test 4
    items = ('a', 'b', 'c')
    length = 5
    unique = False
    choice = Choice()

# Generated at 2022-06-14 00:00:01.396409
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import textwrap
    import sys
    import random
    import string
    import pytest
    from hypothesis import given
    from hypothesis.strategies import integers
    from hypothesis.strategies import lists
    from hypothesis.strategies import text
    from mimesis import Choice
    from mimesis import functional
    from mimesis.typing import Action
    from mimesis.typing import Sequence
    from mimesis.typing import Any


    # Setup for the test
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = True
    expected_type = str
    expected_text = repr(choice(items=items, length=length))


    # Code that is run before the unit test
    def setup_function():
        print('\nsetup_function()')



# Generated at 2022-06-14 00:00:09.860564
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import hypothesis

    from hypothesis import strategies

    from mimesis import Choice

    _choice = Choice()
    _items = ['a', 'b', 'c']
    _length = 5
    _unique = True
    result = _choice(items=_items, length=_length, unique=_unique)
    assert result in _items

    _items = ({'a': 1, 'b': 2, 'c': 3}).keys()
    _length = 5
    _unique = True
    result = _choice(items=_items, length=_length, unique=_unique)
    assert result in _items

    _items = ({'a': 1, 'b': 2, 'c': 3}).values()
    _length = 5
    _unique = True

# Generated at 2022-06-14 00:00:21.279801
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert( c(['a', 'b', 'c']) in ['a', 'b', 'c'] )
    assert( type(c(['a', 'b', 'c'], 1)) == list )
    assert( type(c(('a', 'b', 'c'), 1)) == tuple )
    assert( type(c('abc', 1)) == str )
    assert( type(c(['a', 'b', 'c'], 5)) == list )
    assert( type(c(('a', 'b', 'c'), 5)) == tuple )
    assert( len(c(['a', 'b', 'c'], 5)) == 5 )
    assert( len(c(('a', 'b', 'c'), 5)) == 5 )
    assert( c('abc', 5) == 'bbcab' )