

# Generated at 2022-06-13 23:50:38.114950
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Set up the test.
    from mimesis.enums import Gender
    from mimesis.providers.date import DateTime
    from mimesis.providers.person import Person
    
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    
    # Call the method under test.
    actual = choice(items=items, length=length)
    
    # Verify the results.
    assert isinstance(actual, (list, tuple))
    assert len(actual) == length
    assert actual[0] in items
    
    # Set up the test.
    
    
    # Call the method under test.
    actual = choice(items=items, length=length)
    
    # Verify the results.
    assert isinstance(actual, (list, tuple))
    assert len

# Generated at 2022-06-13 23:50:43.729365
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    pass
    """
    items = [1, 2, 3]
    length = 2
    unique = True
    choice = Choice()
    print(choice(items=items, length=length, unique=unique))
    # TODO
    """

# Generated at 2022-06-13 23:50:55.855499
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    # Call Choice.__call__()
    result = choice(items=['a', 'b', 'c'])
    result1 = choice(items=('a', 'b', 'c'), length=5)
    result2 = choice(items='abc', length=2)
    result3 = choice(items='aabbbccccddddd', length=4, unique=True)
    result4 = choice(items=['a', 'b', 'c'], length=1)
    try:
        # Call Choice.__call__() with invalid or missing arguments
        result = choice(items=[1, 2, 3], length='...', unique=True)
    except TypeError as error:
        print(error)

# Generated at 2022-06-13 23:51:02.789026
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:51:14.469651
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # TODO: Test for non-string items
    # Test for non-sequence items, TypeErrors are raised
    from mimesis import Choice
    choice = Choice()
    not_a_sequence = dict(a=1, b=2)  # type: ignore
    try:
        choice(items=not_a_sequence, length=2)
    except TypeError:
        pass
    try:
        choice(items=not_a_sequence)
    except TypeError:
        pass
    # Test for empty sequence of items, ValueErrors are raised
    empty_sequence = list()  # type: ignore
    try:
        choice(items=empty_sequence, length=2)
    except ValueError:
        pass
    try:
        choice(items=empty_sequence)
    except ValueError:
        pass
    # Test

# Generated at 2022-06-13 23:51:23.262565
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'a'
    assert choice(items=['a', 'b', 'c'], length=1) == ['c']
    assert choice(items='abc', length=2) == 'cb'
    assert choice(items=('a', 'b', 'c'), length=5) == ('b', 'b', 'c', 'a', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'bcad'

# Generated at 2022-06-13 23:51:28.156825
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    choice(items=['a', 'b', 'c'])
    choice(items=['a', 'b', 'c'], length=1)
    choice(items='abc', length=2)
    choice(items=('a', 'b', 'c'), length=5)
    choice(items='aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:51:38.723200
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# # Unit test for method __call__ of class Choice
# def test_Choice___call__():
#     choice = Choice()
#     assert choice(items=['a', 'b', 'c']) == 'c'
#     assert choice(items=['a', 'b

# Generated at 2022-06-13 23:51:40.512646
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert isinstance(Choice().choice(), str)
    assert isinstance(Choice().choice(items=['a', 'b', 'c']), str)


# Generated at 2022-06-13 23:51:49.462935
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print('=' * 40)
    print('Running unittest for method Choice::__call__')
    print('=' * 40)

    choice = Choice()

    if choice(items=['a', 'b', 'c']) != 'c':
        raise Exception('Failed test 1')

    if choice(items=['a', 'b', 'c'], length=1) != ['a']:
        raise Exception('Failed test 2')

    if choice(items='abc', length=2) != 'ba':
        raise Exception('Failed test 3')

    if choice(items=('a', 'b', 'c'), length=5) != ('c', 'a', 'a', 'b', 'c'):
        raise Exception('Failed test 4')


# Generated at 2022-06-13 23:52:01.096998
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    seed(1)
    result = Choice()(items=['a', 'b', 'c'], length=1)
    assert result == ["b"]
    result = Choice()(items=['a', 'b', 'c'], length=3)
    assert result == ["c", "c", "a"]



# Generated at 2022-06-13 23:52:07.571350
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test Choice.__call__ method."""
    c = Choice()

    assert isinstance(c(items=['a', 'b', 'c']), str)

    data = c(items=['a', 'b', 'c'], length=1)
    assert isinstance(data, list)
    assert len(data) == 1

    data = c(items='abc', length=2)
    assert isinstance(data, str)
    assert len(data) == 2

    data = c(items=('a', 'b', 'c'), length=5)
    assert isinstance(data, tuple)
    assert len(data) == 5

    data = c(items='aabbbccccddddd', length=4, unique=True)
    assert isinstance(data, str)
    assert len(data) == 4

   

# Generated at 2022-06-13 23:52:10.361213
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    provider = Choice()
    element = provider(['a', 'b', 'c'])
    sequence = provider(['a', 'b', 'c'], 2)
    print(element)
    print(sequence)

test_Choice___call__()

# Generated at 2022-06-13 23:52:21.697205
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=['a', 'b', 'c']) == 'c'
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) == 'ba'
    assert c(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:52:31.584435
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    from mimesis import Choice

    choice = Choice()

    items = ['a', 'b', 'c']
    assert choice(items=items) in items
    assert choice(items=items, length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    with pytest.raises(TypeError):
        choice(items=['a', 'b', 'c'], length=[0])

# Generated at 2022-06-13 23:52:43.736361
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == choice(items=('a', 'b', 'c'))
    assert choice(items=['a', 'b', 'c'], length=1) == ['c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['c']
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'dbca'
    assert choice(items=('a', 'b', 'c'), length=5) == ('b', 'b', 'c', 'a', 'b')


# Generated at 2022-06-13 23:52:52.163569
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = [1, 2, 3, 4, 5]
    length = 3
    assert choice(items, length) == [4, 1, 2]
    assert len(choice(items, length)) == length

    length = 0
    assert choice(items, length) in items
    assert choice(items) in items
    assert choice(items, length, unique=True) in items
    assert choice(items, unique=True) in items

    assert isinstance(choice(items, length), list)
    assert isinstance(choice(items, length, unique=True), list)

    items = (1, 2, 3, 4, 5)
    length = 3
    assert choice(items, length) == (4, 1, 2)
    assert len(choice(items, length)) == length


# Generated at 2022-06-13 23:52:57.492840
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:53:10.691615
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Method __call__ of class Choice generates a randomly-chosen sequence or bare element from a sequence,
    # testing that it generates values with the specified constraints, checking a condition
    # raises exceptions, and that the generated elements are always sequences of the same type.
    from mimesis import Choice
    from random import choice
    from string import ascii_lowercase as letters

    choice = Choice()
    for _ in range(20):
        # Test generation of a single uncontained element from items,
        # and that this element is always a bare element of the same type.
        for items in [[True, False], [0, 1, 4, 8, 16, 32], list(letters), list(letters + '0123456789')]:
            # print('items:', items)
            item = choice(items)

# Generated at 2022-06-13 23:53:13.950216
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items='abc', length=1) == 'c'
    assert Choice().__call__(items='abc', length=2) == 'ac'


# Generated at 2022-06-13 23:53:23.231811
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    gender_choice = Choice(seed=99)
    gender_choice(items=Gender)
    gender_choice(items=Gender, length=1)
    gender_choice(items=(Gender.MALE, Gender.FEMALE), length=5)
    gender_choice(items=(Gender.MALE, Gender.FEMALE, Gender.NOT_SPECIFIED), length=5)
    gender_choice(items=tuple(Gender), length=5)
    gender_choice(items=tuple(Gender), length=1, unique=True)
    gender_choice(items=list(Gender), length=5)
    gender_choice(items=list(Gender), length=1, unique=True)

# Generated at 2022-06-13 23:53:24.053974
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:53:34.578844
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c.__call__(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert c.__call__(items=('a', 'b', 'c'), length=1) in (['a'], ['b'], ['c'])
    assert c.__call__(items='abc', length=2) in ['ab', 'ac', 'bc']
    assert c.__call__(items=('a', 'b', 'c'), length=5) in [('c', 'a', 'a', 'b', 'c'), ('c', 'a', 'b', 'c', 'a'), ('c', 'a', 'b', 'a', 'c'), ('c', 'a', 'b', 'a', 'c')]

# Generated at 2022-06-13 23:53:37.521074
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    obj = Choice()
    obj.add_provider('random', seed=0)
    actual = obj(items, length, unique)
    expected = ['a']
    assert actual == expected

# Generated at 2022-06-13 23:53:43.461867
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == \
           ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:53:52.306367
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c'], length=0) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']

# Generated at 2022-06-13 23:53:55.772365
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    choice_obj = Choice()
    expected_result = ['a']
    actual_result = choice_obj.__call__(items, length, unique)
    assert expected_result == actual_result


# Generated at 2022-06-13 23:54:09.770027
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice.

    test_Choice___call__ is a unit test for method __call__ of class Choice
    """
    choice = Choice()
    assert choice(items=['a', 'b', 'c'])

    assert choice(items=['a', 'b', 'c'], length=1)

    assert choice(items='abc', length=2)

    assert choice(items=('a', 'b', 'c'), length=5)

    assert choice(items='aabbbccccddddd', length=4, unique=True)

    try:
        choice(items='abc', length=2.0)
    except TypeError:
        pass
    else:
        raise AssertionError


# Generated at 2022-06-13 23:54:12.675521
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    item = choice(items=['a', 'b', 'c'], length=1, unique=True)
    assert item == 'c'


# Generated at 2022-06-13 23:54:17.148196
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    assert choice(items, length) == ['a'], 'Test __call__ method of class Choice'

# Generated at 2022-06-13 23:54:33.783824
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    test_args = [None, [], 'aeiou', '0123456789', ''.join(chr(i) for i in range(32, 128)), '', ' ', None, ['0'], ['1'], ['a'], ['A']]
    test_kwargs = [None, {}, {'length': 0}, {'length': 1}, {'length': 2}, {'length': 10}, {'length': 42}, {'length': -1}, {'unique': True}]

    for arg in test_args:
        print('Testing choice function with arg "{}":'.format(arg))
        choice = Choice()

# Generated at 2022-06-13 23:54:43.936599
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items_list = ['a', 'b', 'c']
    assert choice(items=items_list, length=1) == ['a']
    items_str = 'abc'
    assert choice(items=items_str, length=2) == 'ba'
    items_tuple = ('a', 'b', 'c')
    assert choice(items=items_tuple, length=5) == ('c', 'a', 'a', 'b', 'c')
    items_str = 'aabbbccccddddd'
    assert choice(items=items_str, length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:54:47.053082
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ('a', 'b', 'c')
    length = 5
    unique = True

    choice = Choice(items, length, unique)

    res = choice(items, length, unique)
    assert res == ('c', 'a', 'a', 'b', 'c')

# Generated at 2022-06-13 23:54:52.764683
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print('test_Choice___call__')
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c'] # type: ignore
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']] # type: ignore
    assert choice(items='abc', length=2) in ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'] # type: ignore

# Generated at 2022-06-13 23:54:55.803749
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c'], length=0) != Choice().__call__(['a', 'b', 'c'], length=0)
test_Choice___call__()


# Generated at 2022-06-13 23:55:01.392571
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Field, Gender

    class MyChoice(Choice):
        field = Field.ANY
        gender = Gender.MALE

    choice = MyChoice()
    print(choice(items=[], length=1))
    print(choice(items=[], length=0))

if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:55:07.538426
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    seq = Choice(seed=0)
    test_seq = seq(items=['a', 'b', 'c'])
    assert test_seq == 'b'

if __name__ == "__main__":
    # test_Choice___call__()
    pass

# Generated at 2022-06-13 23:55:16.925351
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c']) == 'c'
    assert Choice().__call__(['a', 'b', 'c'], 1) == ['a']
    assert Choice().__call__('abc', unique=True) in 'bca'
    assert Choice().__call__('abc', length=2) == 'cb'
    assert Choice().__call__(('a', 'b', 'c'), 5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__('aabbbccccddddd', 4, True) in 'cdba'
    assert Choice().__call__(['a', 'b', 'c'], -1) == 'a'
    assert Choice().__call__(['a', 'b', 'c'], -10**10)

# Generated at 2022-06-13 23:55:25.766412
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert isinstance(choice(items=['a', 'b', 'c'], length=2), list)
    assert choice(items='abc', length=2) == 'ba'
    assert isinstance(choice(items='abc', length=2), list)
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)

# Generated at 2022-06-13 23:55:38.750776
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    data = choice(items=['a', 'b', 'c'])
    assert data in ['a', 'b', 'c']
    data1 = choice(items=['a', 'b', 'c'], length=3)
    assert len(data1) == 3
    data2 = choice(items='abc', length=4)
    assert len(data2) == 4
    data3 = choice(items=('a', 'b', 'c'), length=5)
    assert len(data3) == 5
    data4 = choice(items='aabbbccccddddd', length=4, unique=True)
    assert len(data4) == 4
    assert data4.count('a') == 1
    assert data4.count('b') == 1
    assert data4.count('c') == 1

# Generated at 2022-06-13 23:55:51.294692
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from random import Random
    from unittest.mock import Mock

    # test case 1
    random = Random(1)
    choice_mock = Mock(spec=Choice)
    choice_mock._random = random
    # items = ['a', 'b', 'c']
    # length = 1
    # unique = False
    # expected_result = ['a']
    assert choice_mock.__call__(['a', 'b', 'c'], 1) == ['a']

    # test case 2
    random = Random(45)
    choice_mock = Mock(spec=Choice)
    choice_mock._random = random
    # items = ['a', 'b', 'c']
    # length = 0
    # unique = False
    # expected_result = 'c'
    assert choice_mock.__

# Generated at 2022-06-13 23:55:53.276289
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    r = Choice()
    items = ['a', 'b', 'c']
    length = 1
    # TODO: Always return list
    assert r(items=items, length=length) == [items[0]]



# Generated at 2022-06-13 23:56:04.986852
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=('a', 'b', 'c')), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=2), str)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)
    with pytest.raises(TypeError) as excinfo:
        choice(items=['a', 'b', 'c'], length='1')
    assert '**length** must be integer.' in str(excinfo.value)
    with pytest.raises(TypeError) as excinfo:
        choice(items={'a'})

# Generated at 2022-06-13 23:56:07.179251
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    _ = Choice().__call__
    pass

# Generated at 2022-06-13 23:56:16.875403
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ba', 'ab', 'bc']

# Generated at 2022-06-13 23:56:27.840387
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=('a', 'b', 'c')) in ['a', 'b', 'c']
    assert choice(items='abc') in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items=['a', 'b', 'c'], length=2) in [['a', 'b'], ['a', 'c'],
                                                       ['b', 'c']]

# Generated at 2022-06-13 23:56:34.576424
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for generating a random choice from items in a sequence."""
    assert Choice()._Choice__call__(('a', 'b', 'c'), 3) == ('a', 'c', 'b')
    assert Choice()._Choice__call__((1, 2, 3, 4), 4, True) == (1, 2, 3, 4)
    assert Choice()._Choice__call__(['a'], 1, True) == ['a']



# Generated at 2022-06-13 23:56:39.779310
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:56:48.760603
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) == 'ba'
    assert c(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:57:00.295710
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    class Choice(BaseProvider):
        """Class for generating a random choice from items in a sequence."""
        class Meta:
            """Class for metadata."""

            name = 'choice'

        def __init__(self, *args, **kwargs) -> None:
            """Initialize attributes.

            :param args: Arguments.
            :param kwargs: Keyword arguments.
            """
            super().__init__(*args, **kwargs)


# Generated at 2022-06-13 23:59:50.699472
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    # TODO: Create tests
    pass

# Generated at 2022-06-13 23:59:57.460230
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    items = ['a', 'b', 'c']
    length = 1
    actual_return_value = Choice.Choice.__call__(
        Choice.Choice, items=items, length=length)
    expected_return_value = ['b']
    assert (
        actual_return_value == expected_return_value
    ), 'actual return value {} not as expected: {}'.format(
        actual_return_value, expected_return_value
    )

# Generated at 2022-06-14 00:00:11.116412
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    '''
    Description:
    Test method __call__ of class Choice
    '''
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = True
    params = {'items': items, 'length': length, 'unique': unique}
    result = choice(**params)
    if result == list(params['items'])[0] or result == tuple(params['items'])[0] or result == str(params['items'])[0]:
        print('Test_Choice___call__: passed')
        return True
    else:
        print('Test_Choice___call__: failed')
        return False


# Generated at 2022-06-14 00:00:18.887130
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """
    Unit test for method __call__ of class Choice
    """
    from mimesis import Choice
    choice = Choice()
    result = choice(items=['a', 'b', 'c'])
    assert result in ['a', 'b', 'c']
    result = choice(items=['a', 'b', 'c'], length=1)
    assert isinstance(result, list) and len(result) == 1 and result[0] in ['a', 'b', 'c']
    result = choice(items='abc', length=2)
    assert isinstance(result, str) and len(result) == 2 and all([x in result for x in ['a', 'b', 'c']])
    result = choice(items=('a', 'b', 'c'), length=5)
    assert isinstance(result, tuple)

# Generated at 2022-06-14 00:00:29.859080
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    length = 1
    choice = Choice()

    assert choice(items, length) == 'c'
    assert choice(items, length) == 'a'

    items = ['a', 'b', 'c']
    length = 1
    choice = Choice()

    assert choice(items, length) == ['a']
    assert choice(items, length) == ['c']

    items = 'abc'
    length = 2
    choice = Choice()

    assert choice(items, length) == 'ba'
    assert choice(items, length) == 'cb'

    items = ('a', 'b', 'c')
    length = 5
    choice = Choice()

    assert choice(items, length) == ('c', 'a', 'a', 'b', 'c')