

# Generated at 2022-06-13 23:50:37.737002
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert True == True


    # TODO: try to add a test case
    # case1
    assert True == True


    # TODO: try to add a test case
    # case1
    assert True == True


    # TODO: try to add a test case
    # case1
    assert True == True

# Generated at 2022-06-13 23:50:48.813920
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a','b','c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ab','bc','ca']
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')

# Generated at 2022-06-13 23:51:00.791672
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    def setup():
        from mimesis import Choice
        return Choice()

    def test_exceptions(choice):
        from mimesis.exceptions import NonEnumerableError

        try:
            choice(items=[1, 2, 3], length=1.5)
        except NonEnumerableError as e:
            assert '**length** must be integer.' in str(e)

        try:
            choice(items=[1, 2, 3], length=-10)
        except NonEnumerableError as e:
            assert '**length** should be a positive integer.' in str(e)

        try:
            choice(items=[])
        except NonEnumerableError as e:
            assert '**items** must be a non-empty sequence.' in str(e)


# Generated at 2022-06-13 23:51:01.602834
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:51:08.373579
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    __salt__ = {
        'hashutil.rand_str': 'abcdefghijklmnopqrstuvwxyz',
        'hashutil.hash_list':
        lambda x: '{0:x}'.format(hash(''.join(x)) & 0xFFFFFFFF),
    }
    assert (Choice(datetime=None, random=None, salt=__salt__)
            ('abcde', 5, unique=True) == 'dhace')

# Generated at 2022-06-13 23:51:17.808523
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method `__call__` of class Choice.
    """
    c=Choice()
    items= ['a','b','c','d','e']
    l=3
    un=True

    def singlestr(c,l,i,u,str):
        assert c.__call__(items=i,length=l,unique=u)==str
        #assert 1==1

    def liststr(c,l,i,u,str):
        assert c.__call__(items=i,length=l,unique=u)==list(str)

    singlestr(c,l,items,un,'c')
    assert c.__call__(items=items,length=l,unique=un)=='c'

# Generated at 2022-06-13 23:51:27.754289
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Assert that TypeError is raised when `items` is not an instance of
    # `collections.abc.Sequence`.
    with raises(TypeError):
        Choice.__call__(None, items=None)

    # Assert that TypeError is raised when `length` is not an instance of `int`.
    with raises(TypeError):
        Choice.__call__(None, items=[1, 2, 3], length=None)

    # Assert that ValueError is raised when `items` is an empty sequence.
    with raises(ValueError):
        Choice.__call__(None, items=[])

    # Assert that ValueError is raised when `length` is negative.
    with raises(ValueError):
        Choice.__call__(None, items=[1, 2, 3], length=-1)

    # Assert that `items

# Generated at 2022-06-13 23:51:33.080469
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert isinstance(choice(['a', 'b', 'c'], 1), list)
    assert isinstance(choice(['a', 'b', 'c'], 2), list)
    assert isinstance(choice('abc', 1), str)
    assert isinstance(choice(('a', 'b', 'c'), 1), tuple)
    assert isinstance(choice(('a', 'b', 'c'), 2), tuple)


# Generated at 2022-06-13 23:51:39.413135
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    # choice should be a instance of Choice
    choice = Choice()

    # call Choice.__call__ method
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    tmp = choice(items=('a', 'b', 'c'), length=5)
    assert tmp == ('c', 'a', 'a', 'b', 'c')
    tmp = choice(items='aabbbccccddddd', length=4, unique=True)
    assert tmp == 'cdba'


# Generated at 2022-06-13 23:51:41.722816
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    items = c('aabbbccccddddd', 4, True)
    assert len(items) == 4
    assert len(set(items)) == 4

# Generated at 2022-06-13 23:51:51.890371
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('en')
    first_name = person.first_name(gender=Gender.MALE)
    last_name = person.last_name(gender=Gender.MALE)

    items = [first_name, last_name]
    choice = Choice()
    result = choice(items)

    assert result in items


# Generated at 2022-06-13 23:51:55.243388
# Unit test for method __call__ of class Choice

# Generated at 2022-06-13 23:52:05.301763
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Examples for Choice.__call__

    choice = Choice()

    assert choice(items = ['a', 'b', 'c']) == 'c'
    assert choice(items = ['a', 'b', 'c'], length = 1) == ['a']
    assert choice(items = 'abc', length = 2) == 'ba'
    assert choice(items = ('a', 'b', 'c'), length = 5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items = 'aabbbccccddddd', length = 4, unique = True) == 'cdba'

    # Test for :raises: TypeError

    try:
        assert choice(items = 'abc', length = 1.5)
    except TypeError:
        pass

    # Test for :raises: ValueError


# Generated at 2022-06-13 23:52:12.394233
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # assert choice(items=['a', 'b', 'c']) == 'c'
    # assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    # assert choice(items='abc', length=2) == 'ab'
    # assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    # assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    pass

# Generated at 2022-06-13 23:52:13.206102
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:52:23.379325
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    from mimesis import Choice
    choice = Choice()

    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice(items='abc', length=2), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)

    lst = ['a', 'b', 'c']
    assert choice(items=lst, length=5) == random.choices(lst, k=5)

# Generated at 2022-06-13 23:52:25.142876
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(['a', 'b', 'c']) in ['a', 'b', 'c']


# Generated at 2022-06-13 23:52:37.322886
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Case: Sequence (List), length=0, unique=False
    choice = Choice()
    assert isinstance(choice(['a', 'b', 'c']), str)

    # Case: String, length=1, unique=False
    assert isinstance(choice(['a', 'b', 'c'], 1), list)

    # Case: String, length=2, unique=False
    assert isinstance(choice('abc', 2), str)

    # Case: Tuple, length=5, unique=False
    assert len(choice(('a', 'b', 'c'), 5)) == 5
    assert isinstance(choice(('a', 'b', 'c'), 5), tuple)

    # Case: String, length=4, unique=True
    assert len(choice('aabbbccccddddd', 4, True)) == 4

# Generated at 2022-06-13 23:52:46.621752
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == choice(['a', 'b', 'c'])

    assert choice(items=['a', 'b', 'c'], length=1) == choice(['a', 'b', 'c'], 1)

    assert choice(items='abc', length=2) == choice('abc', 2)

    assert choice(items=('a', 'b', 'c'), length=5) == choice(('a', 'b', 'c'), 5)

    assert choice(items='aabbbccccddddd', length=4,
                  unique=True) == choice('aabbbccccddddd', 4, True)


# Generated at 2022-06-13 23:52:50.568710
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test ``Choice._call()`` method."""
    # TODO: Needs more tests.
    assert Choice()(items=['a', 'b', 'c'], length=1) == ['a']

# Generated at 2022-06-13 23:53:07.359366
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    items = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', 'n']
    print("randomly choose one element from the list")
    print(c(items))
    print("randomly choose 10 elements from the list")
    print(c(items, 10))
    print("randomly choose 10 elements from the list, but the result is unique")
    print(c(items, 10, unique=True))



# Generated at 2022-06-13 23:53:21.036374
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=('a', 'b', 'c', 'd', 'e', 'f')) in ['a', 'b', 'c', 'd', 'e', 'f']
    assert c(items=('a', 'b', 'c', 'd', 'e', 'f'), length=5) in [
        ('a', 'b', 'c', 'd', 'e'),
        ('a', 'b', 'c', 'd', 'f'),
        ('a', 'b', 'c', 'e', 'f'),
        ('a', 'b', 'd', 'e', 'f'),
        ('a', 'c', 'd', 'e', 'f'),
        ('b', 'c', 'd', 'e', 'f'),
    ]

# Generated at 2022-06-13 23:53:25.082122
# Unit test for method __call__ of class Choice

# Generated at 2022-06-13 23:53:27.152433
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=['a', 'b', 'c'], length=3) != ('a', 'b', 'c')

# Generated at 2022-06-13 23:53:36.921948
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert choice(items='aabbbccccddddd', length=10, unique=True) == 'aabbbccccd'
#

# Generated at 2022-06-13 23:53:44.991852
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    ch = Choice()

    # items = ['a', 'b', 'c']
    # length = 0 or none
    # unique = False or none
    assert ch(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert ch(items=['a', 'b', 'c'], length=0, unique=None) in ['a', 'b', 'c']

    # items = ['a', 'b', 'c']
    # length = 1
    # unique = False or none

# Generated at 2022-06-13 23:53:53.223744
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.typing import Seed
    from mimesis.providers.base import BaseProvider

    data = {
        'people': ['John', 'Mary', 'Dan', 'Steve'],
        'male': 'John',
        'female': 'Mary',
        'none': 'Steve',
    }

    class A(BaseProvider):
        def gender(self) -> Gender:
            return self.random.choice(
                [Gender.MALE, Gender.FEMALE, Gender.NONE],
            )

        def people(self, gender: Gender = Gender.NONE) -> str:
            return self.choice(items=data['people'], length=1)[0]


# Generated at 2022-06-13 23:54:00.158802
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from nose2.tools import params
    from hypothesis import given
    from hypothesis.strategies import lists, sets, text
    from hypothesis.strategies import integers, sampled_from, tuples
    from mimesis.typing import Sequence

    items = ['a', 'b', 'c']
    items_set = set(items)
    items_tuple = tuple(items)
    items_random_order = ['c', 'b', 'a']

    @given(text(min_size=1))
    def test_Choice___call__returns_list_for_list(items: str):
        """Test that a list is returned when input to Choice is a list.
        """
        choice = Choice()
        output = choice(items=[ch for ch in items], length=4)
        assert isinstance(output, list)


# Generated at 2022-06-13 23:54:08.760977
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    a = Choice()
    assert isinstance(a(items=['a', 'b', 'c']), str)
    assert isinstance(a(items=[1, 2, 3], length=1), list)
    assert isinstance(a(items='abc', length=2), str)
    assert isinstance(a(items=[1, 2, 3], length=5), list)
    assert isinstance(a(items='aabbbccccddddd', length=4, unique=True), str)

# Generated at 2022-06-13 23:54:16.050719
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    assert Choice().__call__(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert len(Choice().__call__(items=['a', 'b', 'c'], length=2)) == 2
    assert isinstance(Choice().__call__(items=['a', 'b', 'c'], length=2), list)
    assert Choice().__call__(items='abc', length=2) in ['ab', 'bc', 'ca']

# Generated at 2022-06-13 23:54:47.812637
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    # Test: Provide a randomly-chosen value from a list
    assert isinstance(choice(['a', 'b', 'c']), str)

    # Test: Provide randomly-chosen values from a list in a sequence
    assert isinstance(choice(['a', 'b', 'c'], length=1), list)
    assert len(choice(['a', 'b', 'c'], length=6)) == 6

    # Test: Provide randomly-chosen values from selected subsequence
    assert isinstance(choice(list('abcdddd'), length=5), list)
    assert len(choice(list('abcdddd'), length=5)) == 5

    # Test: Provide unique randomly-chosen values
    assert isinstance(choice(list('aaabbbcde'), length=5, unique=True), list)

    # Test

# Generated at 2022-06-13 23:54:58.324933
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c'], unique=True) in ['a', 'b', 'c']
    assert Choice().__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice().__call__(items='abc', length=2) == 'ba'
    assert Choice().__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert Choice().__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')

# Generated at 2022-06-13 23:55:07.255930
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method "__call__" of class "Choice"."""
    choice = Choice()
    assert isinstance(choice(['a', 'b', 'c']), str)
    assert isinstance(choice(['a', 'b', 'c'], length=1), list)
    assert isinstance(choice('abc', length=2), str)
    assert isinstance(choice(('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice('aabbbccccddddd', length=4, unique=True), str)

    try:
        choice(items=0, length=1, unique=False)
    except TypeError as e:
        assert str(e) == '**items** must be non-empty sequence.'


# Generated at 2022-06-13 23:55:16.681592
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # GIVEN
    from mimesis import Choice
    from mimesis import Datetime

    choice = Choice()

    # WHEN
    assert choice(items=[1, 2, 3, 4, 5]) in [1, 2, 3, 4, 5]
    assert choice(items=['a', 'b', 'c', 'd', 'e']) in ['a', 'b', 'c', 'd', 'e']

    assert choice(items=[1, 2, 3, 4, 5], length=1) == [1]
    assert choice(items=['a', 'b', 'c', 'd', 'e'], length=1) == ['a']
    assert choice(items=[1, 2, 3, 4, 5], length=5) == [2, 2, 3, 2, 5]

# Generated at 2022-06-13 23:55:26.283161
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(['a', 'b', 'c']) == 'b'
    assert choice(['a', 'b', 'c'], length=1) == ['a']
    assert choice('abc', length=2) == 'cb'
    assert choice(('a', 'b', 'c'), length=5) == ('c', 'c', 'b', 'a', 'b')
    assert choice('aabbbccccddddd', length=4, unique=True) == 'bcdc'
    assert choice(['foo', 'bar', 'baz'], length=4, unique=True) == ['foo', 'baz', 'bar', 'baz']


# Generated at 2022-06-13 23:55:39.227073
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    items = ['a', 'b', 'c']
    assert not isinstance(items, collections.abc.Sequence)
    try:
        assert choice(items=items)
    except TypeError:
        pass
    else:
        raise AssertionError('TypeError was not raised.')

    items = ''
    assert not items
    try:
        assert choice(items=items)
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError was not raised.')

    items = ['a', 'b', 'c']
    assert choice(items=items) in items  # No length
    assert choice(items=items, unique=True) in items

    items = 'abc'
    length = 2

# Generated at 2022-06-13 23:55:43.639145
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    if True:
        # TODO
        pass

# Generated at 2022-06-13 23:55:52.550712
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from random import Random
    random = Random(0)
    c = Choice(random, 'en')
    items = ['a', 'b', 'c']
    expected = 'b'
    actual = c(items, 0)
    assert actual == expected
    expected = c.str('abc'*10)
    items = expected
    expected = ['b', 'a']
    actual = c(items, 2)
    assert actual == expected
    try:
        actual = c(items, 2, unique=True)
    except ValueError:
        assert True
    else:
        assert False
    assert True
    expected = ['b', 'b', 'a', 'a', 'b']
    actual = c(items, 5)
    assert actual == expected
    actual = c(items, 5, unique=True)

# Generated at 2022-06-13 23:56:00.311847
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    from mimesis.providers.choice import Choice as _Choice
    choice = _Choice()
    assert choice.__call__(items=['a', 'b', 'c']) == 'c'
    assert choice.__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice.__call__(items='abc', length=2) == 'ba'
    assert choice.__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice.__call__(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:56:07.668559
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Check if choice method works as expected
    from mimesis import Choice
    choice = Choice()

    assert choice('abc') in 'abc'
    assert choice('abc', length=1) in ['a', 'b', 'c']
    assert choice('abc', length=2) in ['aa', 'ab', 'ac',
                                       'ba', 'bb', 'bc',
                                       'ca', 'cb', 'cc']

# Generated at 2022-06-13 23:57:43.583267
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    import pytest
    from mimesis import Choice

    choice = Choice(random)
    choice.seed('test_Choice___call__')

    with pytest.raises(TypeError):
        choice(items=12345)
    with pytest.raises(ValueError):
        choice([])
    with pytest.raises(TypeError):
        choice(['a', 'b', 'c'], length='123')
    with pytest.raises(ValueError):
        choice(['a', 'b', 'c'], length=-1)
    with pytest.raises(ValueError):
        choice(['a', 'b', 'c'], length=10, unique=True)

    assert choice([1, 2, 3]) == 3

# Generated at 2022-06-13 23:57:49.389477
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method Choice.__call__ of class Choice."""
    pass
    # choice = Choice()
    # result = choice(items=['a', 'b', 'c', 'd', 'e'], length=12, unique=True)
    #
    # assert result == 'bacdee'

# Generated at 2022-06-13 23:57:57.634245
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:58:08.614801
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert test.__call__(None)
    assert test.__call__(None, None)
    assert test.__call__(None, None, None)
    assert test.__call__(None, None, None, None)
    assert test.__call__(None, None, None, None, None)
    assert test.__call__(None, None, None, None, None, None)
    assert test.__call__(None, None, None, None, None, None, None)
    assert test.__call__(None, None, None, None, None, None, None, None)
    # TODO: Add more tests


# Generated at 2022-06-13 23:58:18.486697
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:58:19.474116
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:58:30.374609
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print('\nTesting Choice.__call__')
    from mimesis import Choice
    choice = Choice()

    print('Testing items=<str>')
    assert choice(items='abc',  length=1) is 'b' or 'a' or 'c'
    assert choice(items='abc',  length=1) is not 'd'
    assert choice(items='abc',  length=2) is 'ba' or 'ab' or 'bc' or 'cb' or 'ac' or 'ca'
    assert choice(items='abc',  length=2) is not 'cd' or 'dc' or 'dc'
    assert choice(items='abc',  length=3) is 'cba' or 'bac' or 'acb' or 'cab' or 'bca' or 'abc'

# Generated at 2022-06-13 23:58:36.098955
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from hypothesis import given
    from hypothesis import strategies as st
    import types
    from typing import Any, AnyStr, Callable, Dict, Iterable, List, Set

    choice = Choice()
    is_sequence_instance = lambda obj: isinstance(
        obj, collections.abc.Sequence
    )
    non_empty_sequence_instance = lambda obj: isinstance(
        obj, collections.abc.Sequence
    ) and len(obj) > 0
    is_int = lambda obj: isinstance(obj, int)
    non_negative_int = lambda obj: isinstance(obj, int) and obj >= 0
    unique_element = lambda obj: len(set(obj)) is 1


# Generated at 2022-06-13 23:58:44.907047
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    if Choice.__call__('a', 1):
        pass
    if Choice.__call__('a', 1, False):
        pass
    if Choice.__call__('a', 1, True):
        pass
    if Choice.__call__([], 1):
        pass
    if Choice.__call__([], 1, False):
        pass
    if Choice.__call__([], 1, True):
        pass
    if Choice.__call__([1, 2], 3):
        pass
    if Choice.__call__((1, 2), 3):
        pass
    if Choice.__call__((1, 2), 3, False):
        pass
    if Choice.__call__((1, 2), 3, True):
        pass
    if Choice.__call__('', [1, 2], False):
        pass

# Generated at 2022-06-13 23:58:52.184924
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'a'
    assert choice(items=['a', 'b', 'c'], length=1) == ['c']
    assert choice(items='abc', length=2) == 'ca'
    assert choice(items=('a', 'b', 'c'), length=5) == ('b', 'a', 'a', 'a', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cabd'