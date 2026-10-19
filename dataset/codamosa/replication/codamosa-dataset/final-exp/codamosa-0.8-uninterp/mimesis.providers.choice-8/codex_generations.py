

# Generated at 2022-06-13 23:50:40.569257
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit tests for method *__call__* of class *Choice*."""
    from mimesis import Choice
    choice = Choice()
    # Call with non-sequence items
    try:
        choice(items=42)
    except TypeError:
        pass
    else:
        raise AssertionError('Error')

    # Call with non-integer length
    try:
        choice(items=[1, 2, 3], length=1.1)
    except TypeError:
        pass
    else:
        raise AssertionError('Error')

    # Call with negative length
    try:
        choice(items=[1, 2, 3], length=-1)
    except ValueError:
        pass
    else:
        raise AssertionError('Error')

    # Call with non-empty sequence items

# Generated at 2022-06-13 23:50:50.249273
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False

    if not isinstance(length, int):
        pytest.raises(TypeError)('**length** must be integer.')

    if not isinstance(items, collections.abc.Sequence):
        pytest.raises(TypeError)('**items** must be non-empty sequence.')

    if not items:
        raise ValueError('**items** must be a non-empty sequence.')

    if length < 0:
        raise ValueError('**length** should be a positive integer.')

    assert choice(items, length, unique) == ['a']


# Generated at 2022-06-13 23:51:01.646770
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c.choice()
    assert c.choice(length=5)
    assert c.choice(items=['a', 'b', 'c'], length=5)
    assert c.choice(unique=True)
    assert c.choice(unique=True, length=5)
    assert c.choice(items=['a', 'b', 'c'], unique=True, length=5)
    assert isinstance(c.choice(length=5), list)
    assert isinstance(c.choice(unique=True, length=5), list)
    assert isinstance(c.choice(items=['a', 'b', 'c'], unique=True, length=5), list)
    assert isinstance(c.choice(items=('a', 'b', 'c'), unique=True, length=5), tuple)

# Generated at 2022-06-13 23:51:02.670351
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method Choice.__call__."""
    pass

# Generated at 2022-06-13 23:51:11.578835
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.builtins import Choice
    test_choice = Choice()

    assert isinstance(test_choice(items=['a', 'b', 'c']), str)
    assert isinstance(test_choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(test_choice(items='abc', length=2), str)
    assert isinstance(test_choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(test_choice(items='aabbbccccddddd', length=4, unique=True), str)


# Generated at 2022-06-13 23:51:13.340913
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:51:18.766625
# Unit test for method __call__ of class Choice
def test_Choice___call__():
  
  choice = Choice()
  assert choice(items=['a', 'b', 'c']) == 'c'
  assert choice(items=['a', 'b', 'c'], length=1) == ['a']
  assert choice(items='abc', length=2) == 'ba'
  assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
  assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:51:28.083910
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    choice = Choice()
    assert choice(items=[], length=1) == []
    assert choice(items=(), length=1) == ()
    assert choice(items='', length=1) == ''
    assert choice(items=' ', length=1) == ' '


# Generated at 2022-06-13 23:51:36.793015
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:51:44.877455
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""
    from mimesis.datetime import Datetime
    from mimesis.enums import Gender
    from mimesis.exceptions import NonEnumerableError
    from mimesis.person import Person

    choice = Choice(datetime=Datetime(), person=Person(), seed=10)

    assert choice('abc') == 'b'
    assert choice('abc', length=1) == ['a']
    assert choice('abc', length=2) == 'ba'
    assert choice('abc', length=5) == ('c', 'c', 'a', 'c', 'c')
    assert choice(('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')

# Generated at 2022-06-13 23:51:53.859169
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()(items=['a', 'b', 'c']) == 'c'
    assert Choice()(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice()(items='abc', length=2) == 'ba'
    assert Choice()(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice()(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:51:59.543872
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ('a', 'b', 'c', 'd')
    length = 6
    unique = True
    # result = choice.__call__(items, length, unique)
    # assert isinstance(result, Sequence) is True
    pass



# Generated at 2022-06-13 23:52:06.754720
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    random = choice.random
    random.seed(42)
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert choice(items=['a', 'b', 'c'], length=4) == ['b', 'c', 'a', 'c']

# Generated at 2022-06-13 23:52:17.786048
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person

    provider = Choice()
    assert provider(['a', 'b', 'c']) in ('a', 'b', 'c')
    assert isinstance(provider(items=Person('en').get_genders()), Gender)
    assert (provider(items=Address('en').get_sorted_cities(), length=3) in
            (['London', 'Manchester', 'Birmingham'],
             ['London', 'Birmingham', 'Manchester'],
             ['Birmingham', 'Manchester', 'London'],
             ['Birmingham', 'London', 'Manchester'],
             ['Manchester', 'London', 'Birmingham'],
             ['Manchester', 'Birmingham', 'London']))

# Generated at 2022-06-13 23:52:27.983043
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    # TODO: Must return str
    # assert choice('hello', unique=True) == 'h'
    assert choice('hello', unique=True) == 'h'
    assert choice(('hello', ), unique=True) == ('h',)
    assert choice(['hello'], unique=True) == ['h']
    assert choice('hello', unique=False, length=2) == 'hl'
    assert choice('hello') == 'o'
    assert choice(['hello']) == 'hello'
    assert choice(('hello', )) == 'hello'
    assert choice(['hello'], length=3) == ['hello', 'hello', 'hello']
    assert choice(['hello', 'world'], length=3) == ['hello', 'world', 'world']

# Generated at 2022-06-13 23:52:32.539270
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    length = 1
    unique = False

    c = Choice()
    result = c(items=items, length=length, unique=unique)
    assert isinstance(result, str)

# Generated at 2022-06-13 23:52:40.773474
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    # items=['a', 'b', 'c']
    returned_value = choice(items=['a', 'b', 'c'])
    assert isinstance(returned_value, str)

    # items=['a', 'b', 'c'] length=1
    returned_value = choice(items=['a', 'b', 'c'], length=1)
    assert isinstance(returned_value, list) and len(returned_value) == 1

    # items='abc' length=2
    returned_value = choice(items='abc', length=2)
    assert isinstance(returned_value, str) and len(returned_value) == 2

    # items=('a', 'b', 'c') length=5

# Generated at 2022-06-13 23:52:45.348909
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    result = Choice().__call__(['a', 'b', 'c'])
    assert result == 'c'


# Generated at 2022-06-13 23:52:50.650616
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    ret = choice(['a', 'b', 'c'])
    assert isinstance(ret, str)


# Generated at 2022-06-13 23:52:57.088815
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c']) == 'c'
    assert Choice().__call__(['a', 'b', 'c'], length=1) == ['a']
    assert Choice().__call__('abc', length=2) == 'ba'
    assert Choice().__call__(('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__('aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:53:11.451468
# Unit test for method __call__ of class Choice
def test_Choice___call__(): # TODO: improve the test case
    """Unit test for method :meth:`.Choice.__call__()` """
    import random
    import pytest
    from mimesis import Choice
    from mimesis.enums import Gender

    choice = Choice(localizer=None, locale='en')
    # test1: when length=0
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    # test2: when length>0

# Generated at 2022-06-13 23:53:24.746791
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # given:
    choice = Choice()

    # when:
    result = choice(items=['a', 'b', 'c'])
    result_1 = choice(items=['a', 'b', 'c'], length=1)
    result_2 = choice(items='abc', length=2)
    result_3 = choice(items=('a', 'b', 'c'), length=5)
    result_4 = choice(items='aabbbccccddddd', length=4, unique=True)
    result_5 = choice(items=[], length=1)

    # then:
    assert result in ['a', 'b', 'c']  # type: ignore
    assert result_1 == ['a']  # type: ignore
    assert result_2 == 'ba'

# Generated at 2022-06-13 23:53:25.306179
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:53:35.121134
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__."""
    # pylint: disable=protected-access
    from mimesis import Choice
    
    choice = Choice()
    
    assert choice(items=['a', 'b', 'c']) == 'c'
    
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    
    assert choice(items='abc', length=2) == 'ba'
    
   # assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    
    #assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:53:44.901156
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()

    # Test: simple use
    def test_simple_use():
        items = ['a', 'b', 'c']
        assert choice(items) in items

    # Test: different types of elements
    def test_different_types_of_elements():
        items = [1, 'a', ['a', 'b']]
        assert choice(items) in items

    # Test: length
    def test_length():
        items = [1, 2, 3]
        assert len(choice(items, length=1)) == 1
        assert len(choice(items, length=2)) == 2
        assert len(choice(items, length=3)) == 3

        items = [1, 'a', ['a', 'b']]
        assert len(choice(items, length=1))

# Generated at 2022-06-13 23:53:47.347878
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import doctest
    from mimesis.enums import Language
    locale = Language.EN
    doctest.testmod(extraglobs={'choice': Choice(locale)})

# Generated at 2022-06-13 23:53:57.741993
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    class dict_with_len(dict):
        """Dict with __len__."""

        def __len__(self):
            """Length."""
            return 2

    choice = Choice()

    assert choice(items=['a', 'b', 'c'], length=0) == 'b'
    assert choice(items=('a', 'b', 'c'), length=0) == 'b'
    assert choice(items='abc', length=0) == 'b'
    assert choice(items=dict_with_len(a='a', b='b', c='c'),
                  length=0) == 'a'

    assert choice(items=('a', 'b', 'c'), length=1) == ('b',)

# Generated at 2022-06-13 23:54:08.951170
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert len(choice(items=['a', 'b', 'c'], length=10)) == 10

# Generated at 2022-06-13 23:54:11.692285
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Mock test for Choice.__call__.
    """
    assert Callable(Choice().__call__)


# Generated at 2022-06-13 23:54:16.379499
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.providers.choice import Choice
    # TODO: This function is not used.
    # TODO: Remove the function or implement it.

# Generated at 2022-06-13 23:54:32.817487
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    asr = assert_raises
    choice = Choice()
    member = choice(items=('a', 'b', 'c'))
    assert member in ('a', 'b', 'c')
    assert isinstance(member, str)
    member = choice(items=[1, 2, 3])
    assert member in (1, 2, 3)
    assert isinstance(member, int)
    member = choice(items=['a', 'b', 'c'], length=1)
    assert member in (['a'], ['b'], ['c'])
    assert isinstance(member, tuple)
    member = choice(items='abc', length=2)
    assert member in ('ba', 'ca', 'cb', 'ca')
    assert isinstance(member, str)

# Generated at 2022-06-13 23:54:44.686956
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    from mimesis import Choice
    from mimesis.providers.utils import ChoiceType

    choice = Choice()

    items = [1, 2, 3]
    expected = ChoiceType.Element
    result = choice.__call__(items=items)
    assert (type(result) == expected)
    
    items = [1, 2, 3]
    expected = ChoiceType.Element
    result = choice.__call__(items=items, length=1)
    assert (type(result) == expected)
    
    items = "Hello"
    expected = ChoiceType.Element
    result = choice.__call__(items=items, length=3)
    assert (type(result) == expected)
    
    items = (1, 2, 3)
    expected = ChoiceType.Element

# Generated at 2022-06-13 23:54:47.271258
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice_ = Choice('en')
    items = ['Mike', 'John', 'Bob', 'Tom']
    assert isinstance(choice_(items, 2, True), str)



# Generated at 2022-06-13 23:54:47.925399
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:54:57.971476
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    items = ['a', 'b', 'c']
    length = 1
    unique = False
    assert Choice().__call__(items,length,unique) == ['a']

    items = ['a', 'b', 'c']
    length = 5
    unique = False
    assert Choice().__call__(items,length,unique) == ['c','a','a','b','c']

    items = ['a', 'b', 'c']
    length = 0
    unique = False
    assert Choice().__call__(items,length,unique) == 'c'

    items = ['a', 'b', 'c']
    length = 1
    unique = True
    assert Choice().__call__(items,length,unique) == ['b']

# Generated at 2022-06-13 23:55:07.076520
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']

    assert Choice().__call__(items=items) in items

    r = Choice().__call__(items=items, length=1)
    assert r[0] in items
    assert len(r) == 1

    r = Choice().__call__(items='abc', length=2)
    assert r[0] in items
    assert len(r) == 2

    r = Choice().__call__(items=items, length=5)
    assert len(r) == 5

    r = Choice().__call__(items='aabbbccccddddd', length=4, unique=True)
    assert len(r) == 4
    assert len(set(r)) == 4

    assert Choice().__call__(items=items, unique=True) in items


# Unit test

# Generated at 2022-06-13 23:55:16.515588
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis import Choice
    from mimesis.enums import Gender

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ac', 'bc', 'ba', 'ca', 'cb']

# Generated at 2022-06-13 23:55:24.777515
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:55:35.032337
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str) is True
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple) is True
    assert isinstance(choice(items='abc', length=2), str) is True
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple) is True

# Generated at 2022-06-13 23:55:37.839241
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for Choice's __call__ method."""
    choice = Choice()
    assert isinstance(choice('abc', 3), (list, tuple))
    assert isinstance(choice('abc', 1), str)
    assert isins

# Generated at 2022-06-13 23:55:52.483857
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    cls = Choice()
    assert cls(items=['a', 'b', 'c']) == 'c'
    assert cls(items=['a', 'b', 'c'], length=1) == ['a']
    assert cls(items='abc', length=2) == 'ba'
    assert cls(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert cls(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:55:56.700371
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = ['Foo', 'Bar', 'Baz']
    length = 5
    unique = True
    expected = ['z', 'a', 'w', 'b', 'o']
    choice = Choice()
    result = choice(data, length, unique)
    assert expected == result

# Generated at 2022-06-13 23:56:05.003269
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender

    choice = Choice(gender=Gender.MALE)

    value = choice('abc')
    assert type(value) is str
    assert value in 'abc'

    value = choice(['a', 'b', 'c'])
    assert type(value) is str
    assert value in 'abc'

    value = choice(['a', 'b', 'c'], length=1)
    assert type(value) is list
    assert len(value) == 1
    assert value[0] in 'abc'

    value = choice('abc', length=2)
    assert type(value) is str
    assert len(value) == 2
    assert value in ('ab', 'ba', 'ac', 'ca', 'bc', 'cb')


# Generated at 2022-06-13 23:56:06.738802
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    #TODO This method needs to be tested with an oracle!
    return True

# Generated at 2022-06-13 23:56:16.660934
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for Choice method __call__."""
    # TODO: test `unique` option

    # TypeError: Raise if wrong type of *items*
    # items=None
    with pytest.raises(TypeError):
        Choice.__call__(items=None)

    # items=True
    with pytest.raises(TypeError):
        Choice.__call__(items=True)

    # items=False
    with pytest.raises(TypeError):
        Choice.__call__(items=False)

    # items=1.1
    with pytest.raises(TypeError):
        Choice.__call__(items=1.1)

    # items=1
    with pytest.raises(TypeError):
        Choice.__call__(items=1)

    # items=1.1


# Generated at 2022-06-13 23:56:25.290468
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:56:30.064497
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert type(Choice(seed=42)(items=['a', 'b', 'c'], length=2)) == list
    assert type(Choice(seed=42)(items=('a', 'b', 'c'))) == str
    assert type(Choice(seed=42)(items=[1, 2, 3])) == int
    assert type(Choice(seed=42)(items=[1, 2, 3], length=1)) == list


# Generated at 2022-06-13 23:56:40.470183
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    choice = Choice()
    assert isinstance(choice(items=items), str)
    assert isinstance(choice(items=items, length=1), list)
    assert isinstance(choice(items=items, length=2), list)
    assert isinstance(choice(items='abc', length=1), str)
    assert isinstance(choice(items='abc', length=2), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items=('a', 'b', 'c'), length=6), tuple)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True),
                      str)

# Generated at 2022-06-13 23:56:54.155222
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test a call to this method
    choice = Choice()
    assert choice(items=[1,2,3,4,5]) in [1,2,3,4,5]
    assert choice(items=['a','b','c']) in ['a','b','c']
    assert choice(items='abc') in 'abc'
    assert choice(items=[1,2,3,4], length=2) in ([1,2],[1,3],[1,4],[2,3],[2,4],[3,4])
    assert choice(items=[1,2,3,4], length=2, unique=True) in ([1,2],[1,3],[1,4],[2,3],[2,4],[3,4])

# Generated at 2022-06-13 23:56:54.868327
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:57:24.177880
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""
    from unittest import TestCase
    from unittest.mock import patch

    class TestChoice(TestCase):
        """Test for method __call__ of class Choice."""

        def test_self_call(self):
            """Test calling a class itself."""
            result = Choice.__call__(Choice(), items=("a", "b", "c"))
            self.assertIn(result, {"a", "b", "c"})

        def test_items_not_sequence(self):
            """Test that non-sequence items raises TypeError."""
            with self.assertRaises(TypeError):
                Choice.__call__(Choice(), items={}, length=2)

        def test_empty_items(self):
            """Test that empty items raises ValueError."""


# Generated at 2022-06-13 23:57:26.771815
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert isinstance(Choice()(items=['a', 'b', 'c']), Any)


# Generated at 2022-06-13 23:57:39.241709
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    expected = 'c'
    assert isinstance(expected, str), "Expected is not text"
    assert isinstance(choice(items=['a', 'b', 'c']), str), "Result is not text"

    expected = ['a']
    assert isinstance(expected, list), "Expected is not list"
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list), "Result is not list"

    expected = 'ba'
    assert isinstance(expected, str), "Expected is not text"
    assert isinstance(choice(items='abc', length=2), str), "Result is not text"

    expected = ('c', 'a', 'a', 'b', 'c')
    assert isinstance(expected, tuple), "Expected is not tuple"
   

# Generated at 2022-06-13 23:57:43.637299
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=('a', 'b', 'c'), length=0, unique=False) == Choice().random.choice(('a', 'b', 'c'))


# Generated at 2022-06-13 23:57:54.277557
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    choice = Choice()
    sequence = [1, 2, 3]

    # TODO: TypeError
    with pytest.raises(TypeError):
        choice(sequence, '6', False)

    assert choice(sequence, 1) == [3]
    assert choice(sequence, 1, False) == [3]
    assert choice(sequence, 3) == [2, 3, 3]
    assert choice([], 1) == []
    assert choice(['a', 'b', 'c'], 1) == ['c']
    assert choice(['a', 'b', 'c'], 1, unique=False) == ['c']
    assert choice(['a', 'b', 'c'], 1, unique=True) == ['c']
    assert choice('abc', 1) == 'c'

# Generated at 2022-06-13 23:58:05.392068
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import os
    import sys
    import random
    import argparse
    import unittest
    import textwrap
    import logging
    import contextlib
    import io

    # Determine if environment supports color
    try:
        import colorama
        colorama.init()
        supports_color = True
    except ImportError:
        supports_color = False

    # Define color schemes for errors and warnings
    RED_COLOR = '\033[31m' if supports_color else ''
    BLUE_COLOR = '\033[34m' if supports_color else ''
    YELLOW_COLOR = '\033[33m' if supports_color else ''
    RESET_COLOR = '\033[0m' if supports_color else ''

    # Define a custom StreamHandler to force colorization of the the output

# Generated at 2022-06-13 23:58:13.093731
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    assert choice(items) == 'c'
    assert choice(items, 1) == ['a']
    assert choice(items, 2) == 'ba'
    assert choice(items, 5) == ('c', 'a', 'a', 'b', 'c')
    assert choice('aabbbccccddddd', 4, True) == 'cdba'
    assert choice('aabbbccccddddd', 5, False) == 'dbdcc'
    assert choice('aabbbccccddddd', 5, True) == 'dbacd'
    assert choice('aabbbccccddddd', 5, False) == 'dcdcc'



# Generated at 2022-06-13 23:58:21.333398
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import docopt
    import inspect
    import json
    import sys
    import time

    from mimesis.enums import Gender
    from mimesis.exceptions import NonEnumerableError
    from mimesis.typing import AnyIterable
    from tests.strategies import (
        binary_seqs,
        builtins_seqs,
        floats_seqs,
        ints_seqs,
        json_seqs,
        none_seqs,
        objects_seqs,
        seqs,
        strings_seqs,
        texts_seqs,
        tuples_seqs,
        undefs_seqs,
    )

    from . import Choice

    # Read the command-line arguments
    args = docopt.docopt(__doc__)
    verbose = args['--verbose']


# Generated at 2022-06-13 23:58:24.271748
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    #TODO: generate unit_test
    pass

# Generated at 2022-06-13 23:58:32.345737
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    class Meta:
        pass

    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'