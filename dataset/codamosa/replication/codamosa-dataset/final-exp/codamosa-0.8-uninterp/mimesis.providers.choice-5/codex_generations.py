

# Generated at 2022-06-13 23:50:50.995274
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method Choice.__call__."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:50:52.856938
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().choice(items='abc', length=2, unique=False) == 'c'

# Generated at 2022-06-13 23:51:03.076688
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c'], length=1) is not None
    assert Choice().__call__(['a', 'b', 'c'], length=1) == ['b']
    assert Choice().__call__(['a', 'b', 'c'], length=1) is not ['a']
    assert Choice().__call__(['a', 'b', 'c'], length=1) is not ['c']
    assert Choice().__call__(['a', 'b', 'c'], length=1) is not ['a', 'b', 'c']
    assert Choice().__call__(['a', 'b', 'c'], length=2) is not None
    assert Choice().__call__(['a', 'b', 'c'], length=2) == ['b', 'c']


# Generated at 2022-06-13 23:51:06.896938
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = [1, 2, 3, 4]
    length = 3
    unique = True
    choice = Choice()
    result = choice(items, length, unique)
    assert (result >= 1 and result <= 4)
    assert items.count(result) <= 1


# Generated at 2022-06-13 23:51:16.528477
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert 'b' == str(Choice()(items=['a', 'b', 'c']))
    assert 'ba' == str(Choice()(items=['a', 'b', 'c'], length=2))
    assert ['a'] == str(Choice()(items=['a', 'b', 'c'], length=1))
    assert 'ba' == str(Choice()(items='abc', length=2))
    assert ('c', 'a', 'a', 'b', 'c') == str(Choice()(items=('a', 'b', 'c'), length=5))
    assert 'cdba' == str(Choice()(items='aabbbccccddddd', length=4, unique=True))

# Generated at 2022-06-13 23:51:27.066582
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert Choice().__call__(['a', 'b', 'c'], length=1) == ['a']
    assert Choice().__call__('abc', length=2) in ['ba', 'ab', 'ac', 'cb']
    assert Choice().__call__(('a', 'b', 'c'), length=5) in \
            [('c', 'a', 'a', 'b', 'c'), ('c', 'a', 'b', 'c', 'a'), ('c', 'a', 'b', 'a', 'c')]
    # TODO: Ensure returned string has 4 characters

# Generated at 2022-06-13 23:51:32.743913
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c']) == 'c'
    assert Choice().__call__(['a', 'b', 'c'], length=1) == ['a']
    assert Choice().__call__('abc', length=2) == 'ba'
    assert Choice().__call__(('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__('aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:51:39.262317
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(["a", "b", "c"], 0, False) in (
        "a", "b", "c")
    assert Choice().__call__(["a", "b", "c"], 0, True) in (
        "a", "b", "c")
    assert Choice().__call__(["a", "b", "c"], 1, False) == ["a"]
    assert Choice().__call__(["a", "b", "c"], 1, True) == ["a"]
    assert Choice().__call__("abc", 2, False) in ("ba", "ab", "ac", "bc")
    assert Choice().__call__("abc", 2, True) in (
        "ba", "ab", "ac", "bc")

# Generated at 2022-06-13 23:51:48.056546
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice_obj = Choice()
    assert choice_obj(['amruth', 'nikhil', 'guru']) == 'amruth'
    assert choice_obj(['amruth', 'nikhil', 'guru'], length=1) == ['nikhil']
    assert choice_obj('amruthnikhilguru', length=2) == 'amruthnikhilguru'
    assert choice_obj(('amruth', 'nikhil', 'guru'), length=5) == ('nikhil', 'amruth', 'nikhil', 'guru', 'amruth')
    assert choice_obj('aabbbccccddddd', length=4, unique=True) == 'aabbbccccddddd'

# Generated at 2022-06-13 23:51:55.232320
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.providers.choice import Choice
    from mimesis import Choice as Choice2
    from mimesis.exceptions import NonUniqueError
    from mimesis.enums import Variants
    from mimesis.random import Seed
    from mimesis.utils import get_locale
    seed = Seed.create_by_entropy()
    choice = Choice(seed=seed)
    choice2 = Choice2(seed=seed)
    choices = ['a', 'b', 'c', 'd', 'e']
    choices2 = ['a', 'b', 'c', 'd']
    choices3 = ['o', 'p', 'q', 'r', 's']

    # item1 = choice(items=choices, length=3)
    # assert item1 in [('a', 'b', 'c'), ('a',

# Generated at 2022-06-13 23:52:07.999200
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests method __call__ of class Choice.
    Test for the simple case that should pass.
    """

    '''
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    '''
    pass


# Generated at 2022-06-13 23:52:15.894728
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    # Case 1: Check if it returns a single uncontained element is chosen.
    items = ['a', 'b', 'c']
    length = 0
    unique = False
    choice = Choice()
    assert choice(items=items, length=length, unique=unique) == 'c'

    # Case 2: Check if it returns a single uncontained element is chosen.
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    choice = Choice()
    assert choice(items=items, length=length, unique=unique) == ['a']

    # Case 3: Check if it returns a single uncontained element is chosen.
    items = 'abc'
    length = 2
    unique = False
    choice = Choice()
    assert choice(items=items, length=length, unique=unique) == 'ba'

   

# Generated at 2022-06-13 23:52:27.342425
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice with the following test cases:
        1. Test that **items** must be a non-empty sequence.
        2. Test that **length** must be a positive integer.
        3. Test that **items** must contain sufficient unique elements.
        4. Test that a single uncontained element is chosen.
        5. Test that the desired length for the sequence is achieved.
        6. Test that the returned sequence is of the same type as the input.
        7. Test that elements in the returned sequence are unique.
    """
    from mimesis import Choice
    # 1. Test that **items** must be a non-empty sequence

# Generated at 2022-06-13 23:52:31.896544
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice()('abc') == 'c'
    assert Choice()('abc', 1) == ['a']
    assert Choice()('abc', 2) == 'ba'
    assert Choice()(('a', 'b', 'c'), 5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice()('aabbbccccddddd', 4, True) == 'cdba'

# Generated at 2022-06-13 23:52:46.341385
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    fn1 = lambda: choice(items=['a', 'b', 'c'])
    fn2 = lambda: choice(items=['a', 'b', 'c'], length=1)
    fn3 = lambda: choice(items='abc', length=2)
    fn4 = lambda: choice(items=('a', 'b', 'c'), length=5)
    fn5 = lambda: choice(items='aabbbccccddddd', length=1, unique=True)
    fn6 = lambda: choice(items='aabbbccccddddd', length=4, unique=True)
    fn7 = lambda: choice(items='aabbbccccddddd', length=5, unique=True)
    assert fn1() in ['a', 'b', 'c']

# Generated at 2022-06-13 23:52:56.969960
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4,
                  unique=True) == 'cdba'


# Generated at 2022-06-13 23:53:07.291604
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:53:21.036285
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b',
                                                        'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    # TODO: For now, always returns list
    assert isinstance(choice(items=['a', 'b', 'c'],
                             length=1), list)

# Generated at 2022-06-13 23:53:26.185924
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    '''Tests the method Choice.__call__.'''

    test_items = ('a', 'b', 'c')
    test_length = 3
    test_unique = True
    choice = Choice()

    result = choice(items=test_items, length=test_length, unique=test_unique)

    print(choice(items=test_items, length=test_length, unique=test_unique))


# Generated at 2022-06-13 23:53:36.141894
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ab', 'ba', 'ac', 'ca', 'bc', 'cb']

# Generated at 2022-06-13 23:53:43.065304
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Instantiate class
    choice = Choice()

    # Call method to be tested
    choice(items=['a', 'b', 'c'])



# Generated at 2022-06-13 23:53:52.005388
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test for normal case
    choice = Choice()

    ret = choice(items=['a', 'b', 'c'])
    assert ret in ['a', 'b', 'c']

    ret = choice(items=['a', 'b', 'c'], length=1)
    assert ret == ['a']

    ret = choice(items='abc', length=2)
    assert ret in ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']

    ret = choice(items=('a', 'b', 'c'), length=5)
    assert len(ret) == 5
    assert ret[0] in ['a', 'b', 'c']
    assert ret[1] in ['a', 'b', 'c']
    assert ret[2] in ['a', 'b', 'c']
    assert ret[3]

# Generated at 2022-06-13 23:53:57.255995
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    obj = Choice()
    res = obj(['a', 'b', 'c'])
    res2 = obj(['a', 'b', 'c'], length=1)
    res3 = obj('abc', length=2)
    res4 = obj(('a', 'b', 'c'), length=5)
    res5 = obj('aabbbccccddddd', length=4, unique=True)
    return res, res2, res3, res4, res5


# Generated at 2022-06-13 23:54:02.372832
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    _items = ['a', 'b', 'c']
    _length = 1
    _unique = False
    choice = Choice()
    _result = choice(items=_items, length=_length, unique=_unique)
    print(_result)



# Generated at 2022-06-13 23:54:14.291469
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""
    #Test code for first if
    try:
        choice = Choice()
        choice(items=['a', 'b', 'c'], length = '1')
    except TypeError:
        print('Test Successful')
    except:
        print('Test Failed')

    #Test code for second if
    try:
        choice = Choice()
        choice(items={'a','b','c'}, length = 1)
    except TypeError:
        print('Test Successful')
    except:
        print('Test Failed')

    #Test code for third if
    try:
        choice = Choice()
        choice(items=[], length = 1)
    except ValueError:
        print('Test Successful')
    except:
        print('Test Failed')

    #Test code for fourth

# Generated at 2022-06-13 23:54:18.953140
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    items = [0, 1, 2, 3, 4, 5]
    choice = Choice()
    length_positive = 2
    length_negative = -2
    unique_True = True
    unique_False = False
    assert len(choice(items=items, length=length_positive, unique=unique_False)) == length_positive
    assert len(choice(items=items, length=length_positive, unique=unique_True)) == length_positive
    with pytest.raises(ValueError) as exc_info:
        choice(items=items, length=length_negative, unique=unique_False)
    assert "**length** should be a positive integer" in str(exc_info.value)

# Generated at 2022-06-13 23:54:24.779112
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


if __name__ == '__main__':
    choice = Choice()
    print(choice(items=['a', 'b', 'c']))
    print(choice(items=['a', 'b', 'c'], length=1))

# Generated at 2022-06-13 23:54:35.961174
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from hypothesis import strategies as st
    from random import choice
    from mimesis import Choice

    choice_1 = Choice()
    assert choice_1('abcdefghijklmnopqrstuvwxyz') in 'abcdefghijklmnopqrstuvwxyz'
    assert choice_1(list('abcdefghijklmnopqrstuvwxyz')) in 'abcdefghijklmnopqrstuvwxyz'
    assert choice_1(tuple('abcdefghijklmnopqrstuvwxyz')) in 'abcdefghijklmnopqrstuvwxyz'


# Generated at 2022-06-13 23:54:45.664112
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """
    Test method Choice.Choice.__call__()
    """
    choice = Choice()
    # Test Choice.Choice.__call__() method:
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:54:52.947058
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    actual=Choice().__call__(items=['a', 'b', 'c'], length=1, unique=True)
    expected='a'
    assert actual==expected
    actual=Choice().__call__(items=('a', 'b', 'c'), length=2, unique=False)
    expected=('b', 'c')
    assert actual==expected
    actual=Choice().__call__(items='abc', length=5, unique=True)
    expected='abcba'
    assert actual==expected
    actual=Choice().__call__(items=['a', 'b', 'c'], length=0, unique=True)
    expected='a'
    assert actual==expected

# Generated at 2022-06-13 23:55:13.481160
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    import collections.abc
    from typing import Any, Optional, Sequence, Union
    from random import randint
    provider = Choice()
    choice = provider.choice
    data_set = (
        ((), 0, True),
        (("a", "b", "c"), randint(0, 1000), False),
        ("abc", randint(0, 1000), False),
        (("a", "b", "c"), randint(0, 1000), True),
        ("aabbbccccddddd", randint(0, 1000), True)
    )

# Generated at 2022-06-13 23:55:21.880084
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    
    # Run tests with list of items
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    result = Choice().__call__(items, length, unique)
    assert type(result) == str
    length = 2
    unique = True
    result = Choice().__call__(items, length, unique)
    assert type(result) == list
    result = Choice().__call__(items, length, unique) 
    assert len(result) == length
    assert len(set(result)) == len(result)
    assert type(result) == list

    # Run tests with unique elements
    unique = True
    length = 1
    items = ['a', 'b', 'c']
    result = Choice().__call__(items, length, unique)
    assert type(result) == list


# Generated at 2022-06-13 23:55:35.741465
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test that a TypeError is raised if **items** is a non-sequence type
    with pytest.raises(TypeError):
        Choice().__call__(items=dict())
    # Test that Sequences are handled correctly
    assert Choice().__call__(items=['a', 'b', 'c']) == 'c'
    assert Choice().__call__(items='abc') == 'a'
    # Test that a TypeError is raised if **length** is non-integer
    with pytest.raises(TypeError):
        Choice().__call__(length='1', items=['a', 'b', 'c'])
    # Test that a TypeError is raised if **items** is empty
    with pytest.raises(ValueError):
        Choice().__call__(items='')
    # Test that a ValueError is raised

# Generated at 2022-06-13 23:55:43.185777
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    provider = Choice(seed=5887)
    items = [1, 2, 3, 4, 5]
    length = 3
    expected = [4, 2, 4]
    assert provider(items, length) == expected

    provider = Choice(seed=5887)
    items = [1, 2, 3, 4, 5]
    length = 4
    expected = [4, 2, 4, 1]
    assert provider(items, length) == expected

    provider = Choice(seed=5887)
    items = [1, 2, 3, 4, 5]
    length = 2
    expected = [4, 2]
    assert provider(items, length) == expected



# Generated at 2022-06-13 23:55:48.687063
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice_ = Choice()
    assert isinstance(choice_(items=['a', 'b', 'c']), str)
    assert isinstance(choice_(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice_(items='abc', length=2), str)
    assert isinstance(choice_(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice_(items='aabbbccccddddd', length=4, unique=True), str)

    # TODO: must be coverage of this method - each branch

# Generated at 2022-06-13 23:55:56.941992
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import DataType
    choice = Choice('en')
    print(choice(items=['a', 'b', 'c']))
    print(choice(items=['a', 'b', 'c'], length=1))
    print(choice(items='abc', length=2))
    print(choice(items=('a', 'b', 'c'), length=5))
    print(choice(items='aabbbccccddddd', length=4, unique=True))


# Generated at 2022-06-13 23:56:04.073133
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method Choice.__call__."""
    choice = Choice()
    items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    assert isinstance(choice(items), str)
    assert isinstance(choice(items, length=5), list)
    assert isinstance(choice(items, length=5), str)
    assert isinstance(choice(items, length=5, unique=True), str)

# Generated at 2022-06-13 23:56:15.058297
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for Choice.__call__."""
    from mimesis.providers.choice import Choice
    from mimesis.enums import Gender
    from mimesis.base import Items
    from mimesis.types import MimesisDataType
    from mimesis.utils import get_data, get_provider

    choice = Choice()
    data = get_data('choice')

    class TestClass(object):

        def __init__(self, data: MimesisDataType) -> None:
            self._data = data

        def __getattr__(self, attr: str) -> Any:
            return get_provider(self._data, attr)

    # TODO: Support custom data classes

# Generated at 2022-06-13 23:56:24.847166
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
            ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
    assert Choice().__call__(items=data, length=2) in data
    assert Choice().__call__(items=data, length=2) not in [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    return


# Generated at 2022-06-13 23:56:35.719294
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()

    assert c(items=['a', 'b', 'c']) == 'c'
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) == 'ba'
    assert c(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    try:
        c(items=[], length=1)
    except ValueError:
        pass
    else:
        assert False

    try:
        c(items=[1,2], length=1.2)
    except TypeError:
        pass

# Generated at 2022-06-13 23:57:03.972875
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    test_data = ('abc', 3, False)
    # Positive tests
    assert isinstance(choice(*test_data), str)
    assert isinstance(choice(*test_data), str)
    assert isinstance(choice(*test_data), str)
    assert isinstance(choice(*test_data), str)
    assert isinstance(choice(*test_data), str)
    assert isinstance(choice(*test_data), str)
    assert isinstance(choice(*test_data), str)

    # Negative tests
    test_data = (None, 3, False)
    assert isinstance(choice(*test_data), str)
    test_data = ([], 3, False)
    assert isinstance(choice(*test_data), str)
    test_data = ([], 3, False)

# Generated at 2022-06-13 23:57:08.772670
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']

    assert len(choice(items='abc', length=5)) == 5
    assert len(choice(items=['a', 'b', 'c'], length=5)) == 5



# Generated at 2022-06-13 23:57:22.328182
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    from mimesis.providers import Action
    from mimesis.enums import ActionType

    choice = Choice()

    items = ['a', 'b', 'c']
    for item in items:
        assert item in Choice.Meta.__fields__['items']

    assert choice(items=items) in items

    assert choice(items=['a', 'b', 'c'], length=1) == ['a']

    assert choice(items='abc', length=2) == 'ba'

    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')

    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:57:31.346874
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(['a', 'b', 'c'], length=0) in ['a', 'b', 'c']
    assert choice(['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(['a', 'b', 'c'], length=2) in ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    assert choice(('a', 'b', 'c'), length=2) in [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]

# Generated at 2022-06-13 23:57:39.378130
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Method __call__ of class Choice."""
    import pytest
    from mimesis.enums import Gender

    choice = Choice(seed=1234567890)
    assert choice('A', 'B', length=2) == 'BA'

    with pytest.raises(TypeError):
        choice('A', 'B', length=2.0)

    with pytest.raises(ValueError):
        choice('A', 'B', length=-2)

    with pytest.raises(ValueError):
        choice('A', 'B', length=3)

    with pytest.raises(ValueError):
        choice('A', 'A', length=2)

    with pytest.raises(TypeError):
        choice(['A', 'B'], unique=1)


# Generated at 2022-06-13 23:57:47.054416
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Arrange
    from mimesis import Choice
    choice = Choice()
    expected_outputs = {
        '1': 'c',
        '2': ['a'],
        '3': 'ba',
        '4': ('c', 'a', 'a', 'b', 'c'),
        '5': 'cdba'
    }

    # Act

# Generated at 2022-06-13 23:58:00.604894
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests method __call__ of class Choice.
    Basically, it tests that a random choice is made and that the length is
    correct.
    """
    from mimesis import Choice
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert len(choice(items=['a', 'b', 'c'], length=1)) == 1
    assert len(choice(items=['a', 'b', 'c'], length=5)) == 5
    assert choice(items=['a', 'b', 'c'], unique=True) in ['a', 'b', 'c']

    assert choice(items=('a', 'b', 'c')) in ('a', 'b', 'c')

# Generated at 2022-06-13 23:58:10.589542
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=['a', 'b', 'c']) == 'c'
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) == 'ba'
    assert c(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    try:
        c(items={1, 2, 3}, length=5, unique=True)
    except TypeError:
        pass
# Unit test complete

# Generated at 2022-06-13 23:58:20.801657
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.exceptions import ChoiceError
    from mimesis.providers.person import Person
    p = Person('en')
    choice = Choice('en')
    items = ['a', 'b', 'c']
    result = choice(items, length=1)
    assert result in items
    result = choice(items, length=2)
    assert len(result) == 2
    assert result[0] in items
    assert result[1] in items
    result = choice(items, length=2, unique=True)
    assert len(result) == 2
    assert result[0] in items
    assert result[1] in items
    result = choice(items)
    assert result in items
    items = ['a', 'b', 'c', 'd', 'e']
   

# Generated at 2022-06-13 23:58:31.791154
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from random import Random
    from test import Test
    from mimesis.typing import Seed


# Generated at 2022-06-13 23:59:30.699065
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import CharacterSet
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.misc import Person

    choice = Choice(datetime=Datetime(), person=Person())
    assert isinstance(choice(), str)
    assert choice(items=['a', 'b', 'c', 'd', 'e'], length=5, unique=True) != choice(items=['a', 'b', 'c', 'd', 'e'], length=5, unique=True)
    assert isinstance(choice(items=['a', 'b', 'c', 'd', 'e'], length=3, unique=True), str)
    assert isinstance(choice(items=['a', 'b', 'c', 'd', 'e'], length=3, unique=False), str)
   

# Generated at 2022-06-13 23:59:38.587391
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c']) == 'c'
    assert Choice().__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice().__call__(items='abc', length=2) == 'ba'
    assert Choice().__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:59:51.843291
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests for the method Choice.__call__
    """
    from random import Random
    random = Random()
    choice = Choice(random)
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-14 00:00:01.498071
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.text import Text
    person = Person('en')
    text = Text('en')
    choice = Choice()
    assert isinstance(choice(items=Gender), Gender)

    assert isinstance(choice(items=[Person, Text]), type)
    assert isinstance(choice(items=[1, 2, 3], length=1), list)

    assert isinstance(choice(items='aaa', length=5, unique=True), str)
    assert isinstance(choice(items=['a', 'b', 'c'], length=5,
                             unique=True), list)

    assert isinstance(choice(items='abi', length=1), str)
    assert isinstance(choice(items='a'), str)
   

# Generated at 2022-06-14 00:00:04.331609
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = True
    assert choice(items=items, length=length, unique=unique) == 'c'

# Generated at 2022-06-14 00:00:04.964533
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    return "There's nothing to test."



# Generated at 2022-06-14 00:00:14.337473
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.data import CHOICES_DICT

    choices = Choice()

    # def __call__(self, items, number=0, unique=False) -> list
    choices(items=('a', 'b', 'c'), number=4)
    choices(items='abc', number=4)
    choices(items=('a', 'b', 'c'), unique=True, number=4)
    choices(items='abcd', number=4)
    choices(items='abcd', number=4, unique=True)

    # def __call__(self, items, number=0, unique=False) -> list
    results = choices(items=CHOICES_DICT['female_names'], number=20)
    assert (isinstance(results, list) and results is not None)
    assert isinstance(results[0], list)

# Generated at 2022-06-14 00:00:16.182572
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""
    choice = Choice()
    assert 'c' == choice(items=['a', 'b', 'c'])

# Generated at 2022-06-14 00:00:17.100568
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # TODO
    pass

# Generated at 2022-06-14 00:00:22.571082
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    ch = Choice()
    assert ch(['a', 'b', 'c']) # 'c'
    assert ch(['a', 'b', 'c'],length=1) # ['a']
    assert ch('abc', length=2) #'ba'
    assert ch(('a', 'b', 'c'), length=5) #('c', 'a', 'a', 'b', 'c')
    assert ch('aabbbccccddddd', length=4, unique=True)
   #'cdba'
    assert ch(items=['a', 'b', 'c'], length=5, unique=True)
    assert ch(items=['a', 'b', 'c'], length=1, unique=True)
    #assert ch(items=['a', 'b', 'c'], length=1, unique=