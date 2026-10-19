

# Generated at 2022-06-13 23:50:33.503737
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Testing method __call__ of class Choice."""
    from mimesis import Choice

    choice = Choice()

    # Testing the default value of the **length** with **items** as list.
    assert isinstance(choice(items=['a', 'b', 'c']), str)

    # Testing the custom value of the **length** with **items** as tuple.
    assert isinstance(choice(items=('a', 'b', 'c'), length=2), tuple)

    # Testing the custom value of the **length** with **items** as string.
    assert isinstance(choice(items='abc', length=1), str)

    # Testing the custom value of the **length** with unique elements.
    assert isinstance(choice(items='aabbbccccddddd', length=2, unique=True), str)

    # Testing the Type

# Generated at 2022-06-13 23:50:46.560740
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ba', 'ab', 'ac', 'bc', 'cb', 'ca']
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) in ['cdba', 'bdac', 'dada', 'babd']

# Generated at 2022-06-13 23:50:53.016732
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    instance = Choice()

    assert (instance(['a', 'b', 'c']) in ['a', 'b', 'c'])
    assert (instance(['a', 'b', 'c'], 1) in [['a'], ['b'], ['c']])
    assert (instance('abc', 2) in ['ba', 'ab', 'ac'])
    assert (instance(('a', 'b', 'c'), 5) in [('c', 'a', 'a', 'b', 'c'),
                                             ('a', 'c', 'b', 'a', 'b'),
                                             ('c', 'b', 'c', 'c', 'a')])

# Generated at 2022-06-13 23:50:53.882920
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:50:54.847296
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass


# Generated at 2022-06-13 23:51:04.106758
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = ['a', 'b', 'c']
    assert isinstance(Choice().__call__(items=data), str)
    assert Choice().__call__(items=data) in data

    data = 'abc'
    assert len(Choice().__call__(items=data, length=2)) == 2
    assert Choice().__call__(items=data, length=2) in ['ab', 'bc', 'ac']

    data = ['a', 'b', 'c']
    assert Choice().__call__(items=data, length=1) == ['a']

    data = ['a', 'b', 'c']

# Generated at 2022-06-13 23:51:05.311826
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Python3
    pass


# Generated at 2022-06-13 23:51:10.749774
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    sequence = ('a', 'b', 'c')
    num = choice(sequence, 1, unique=False)
    assert num == 'c'



# Generated at 2022-06-13 23:51:15.944990
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:51:20.723888
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    s = Choice()
    assert (
        s(
            items=[
                'a',
                'b',
                'c',
            ],
            length = 1,
            unique = True,
        ) in ['a', 'b', 'c'],
    )


# Generated at 2022-06-13 23:51:38.771009
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Call without non keyword arguments
    choice = Choice
    expected = str
    result = choice
    assert type(result) is expected

    # Call with non keyword arguments
    choice = Choice()
    expected = str
    result = choice(items=['a', 'b', 'c'], length=2)
    assert type(result) is expected

    # Call with non keyword arguments
    choice = Choice()
    expected = str
    result = choice(items=['a', 'b', 'c'], length=0)
    assert type(result) is expected

    # Call with non keyword arguments
    choice = Choice()
    expected = str
    result = choice(items='abc', length=2)
    assert type(result) is expected

    # Call with non keyword arguments
    choice = Choice()
    expected = str

# Generated at 2022-06-13 23:51:46.923177
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
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

# Generated at 2022-06-13 23:51:51.838407
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:52:02.336798
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice.__call__(['a', 'b', 'c']) in ['a', 'b', 'c']
    assert Choice.__call__(['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert Choice.__call__(['a', 'b', 'c'], length=2) in [['a', 'b'], ['a', 'c'], ['b', 'c']]
    assert Choice.__call__(['a', 'b', 'c'], length=3) in [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c']]
    assert Choice.__call__('abc', length=1) in ['a', 'b', 'c']

# Generated at 2022-06-13 23:52:08.704230
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # unit testing for method Choice.__call__(items, length, unique)
    _items = ['a','b','c']
    _length = 3
    _unique = True
    _choice = Choice()
    ans = _choice(items=_items, length=_length, unique=_unique)
    print(ans)
    assert True


# Generated at 2022-06-13 23:52:11.674160
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False

    choice(items, length, unique)
    choice(items, length, unique)

test_Choice___call__()

# Generated at 2022-06-13 23:52:13.988156
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass


# Generated at 2022-06-13 23:52:22.724656
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice.__call__(['a', 'b', 'c']) == 'c'
    assert choice.__call__(['a', 'b', 'c'], length=1) == ['a']
    assert choice.__call__('abc', length=2) == 'ba'
    assert choice.__call__(('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice.__call__('aabbbccccddddd', length=4, unique=True) == 'cdba'

if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:52:31.675549
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    random_choice = choice(items=['a', 'b', 'c'])
    print(random_choice)
    list_random_choice = choice(items=['a', 'b', 'c'], length=1)
    print(list_random_choice)
    tuple_random_choice = choice(items=('a', 'b', 'c'), length=5)
    print(tuple_random_choice)
    str_random_choice = choice(items='abc', length=2)
    print(str_random_choice)
    unique_str_random_choice = choice(items='aabbbccccddddd', length=4, unique=True)
    print(unique_str_random_choice)

# Test for method __call__ of class Choice in a negative scenario

# Generated at 2022-06-13 23:52:36.292033
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test length=0
    assert Choice()(items=['a','b','c']) == 'c'
    # Test length > 0
    assert Choice()(items=['a','b','c'], length=1) == ['a']


# Generated at 2022-06-13 23:53:22.046450
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for Choice.__call__().

    :return: None.

    """
    choice = Choice()
    if not isinstance(choice(items=['a', 'b', 'c']), Any):
        raise TypeError('**choice** must return Any.')



# Generated at 2022-06-13 23:53:32.183832
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items1 = ['a', 'b', 'c']
    length1 = 0
    unique1 = False
    choice = Choice()
    result = choice(items1, length1, unique1)
    print(result)
    items2 = ['a', 'b', 'c']
    length2 = 1
    unique2 = False
    choice = Choice()
    result = choice(items2, length2, unique2)
    print(result)
    items3 = 'abc'
    length3 = 2
    unique3 = False
    choice = Choice()
    result = choice(items3, length3, unique3)
    print(result)
    items4 = ('a', 'b', 'c')
    length4 = 5
    unique4 = False
    choice = Choice()
    result = choice(items4, length4, unique4)

# Generated at 2022-06-13 23:53:39.172350
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()

    assert c(items=['a', 'b', 'c']) == 'c'
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) == 'ba'
    assert c(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert c(items='aabbbccccddddd', length=20, unique=True) == 'bcaa'

# Generated at 2022-06-13 23:53:50.576348
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    result = choice(items=('a', 'b', 'c'))
    assert result in ['a', 'b', 'c']
    result = choice(items=('a', 'b', 'c'), length=1)
    assert result == 'c'
    assert len(result) == 1
    result = choice(items='abc', length=2)
    assert result in ['ab', 'bc', 'ca']
    assert len(result) == 2
    assert isinstance(result, str)
    result = choice(items=('a', 'b', 'c'), length=5)

# Generated at 2022-06-13 23:53:58.676645
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test for non-unique elements
    result = Choice().__call__(['a', 'b', 'c'], length=0)

    assert (
        result == 'a' or
        result == 'b' or
        result == 'c'
    ), 'Method __call__ with non-unique elements failed.'

    # Test for unique elements
    result = Choice().__call__(['a', 'b', 'c'], length=3, unique=True)

    assert (
        result == 'abc' or
        result == 'acb' or
        result == 'bac' or
        result == 'bca' or
        result == 'cab' or
        result == 'cba'
    ), 'Method __call__ with unique elements failed.'

    # Test for length error
    error = False

# Generated at 2022-06-13 23:54:02.378347
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = [1,2,3]
    assert Choice().__call__(items=items) in items
    assert len(Choice().__call__(items=items, length=1)) == 1
    assert len(Choice().__call__(items=items, length=2)) == 2
    assert len(Choice().__call__(items=items, length=3)) == 3
    assert len(Choice().__call__(items=items, length=4)) == 4
    assert len(Choice().__call__(items=items, length=5)) == 5

# Generated at 2022-06-13 23:54:14.290084
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    items = ['a', 'b', 'c']
    length = 1
    unique = True
    result = choice(items=items, length=length, unique=unique)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in ['a', 'b', 'c']
    assert isinstance(result[0], str)

    items = ['a', 'b', 'c']
    length = 2
    unique = True
    result = choice(items=items, length=length, unique=unique)

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] in ['a', 'b', 'c']
    assert isinstance(result[0], str)

# Generated at 2022-06-13 23:54:15.264916
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:54:30.219020
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Code to test __call__ method from class Choice."""
    c = Choice()
    assert c(items=["a", "b", "c"]) in ["a", "b", "c"]
    assert c(items=["a", "b", "c"], length=1) == ["a"]
    assert c(items="abc", length=2) in ["ab", "ac", "bc"]
    assert len(c(items=("a", "b", "c"), length=5)) == 5
    assert len(c(items='aabbbccccddddd', length=4, unique=True)) == 4
    assert c(items='aabbbccccddddd', length=4, unique=True) not in ["babb", "dddb", "ccdb", "cddd"]


# Generated at 2022-06-13 23:54:37.209122
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()

    assert choice(items=['a', 'b', 'c'])
    assert choice(items=['a', 'b', 'c'], length=1)
    assert choice(items='abc', length=2)
    assert choice(items=('a', 'b', 'c'), length=5)
    assert choice(items='aabbbccccddddd', length=4, unique=True)
    # TODO: Should return dict
    assert choice(items={'a': 1, 'b': 2, 'c': 3}, length=2)



# Generated at 2022-06-13 23:55:59.452028
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Unit test for method __call__ of class Choice
    #
    # Assertion 1
    assert Choice.__call__((None,), 1, False) == None
    #
    # Assertion 2
    assert Choice.__call__(('a', 'b', 'c'), 0, False) == 'c'
    #
    # Assertion 3
    assert Choice.__call__(('a', 'b', 'c'), 1, False) == ('c',)
    #
    # Assertion 4
    assert Choice.__call__('abc', 2, False) == 'ba'
    #
    # Assertion 5
    assert Choice.__call__(('a', 'b', 'c'), 5, False) == ('c', 'a', 'a', 'b', 'c')
    #
    # Assertion

# Generated at 2022-06-13 23:56:04.263168
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = [1, 2, 3, 4, 5]
    length = 4
    unique = True

    result = Choice.__call__(Choice, items, length, unique)
    assert isinstance(result, list)
    assert len(result) == length
    assert set(result).symmetric_difference(items)

test_Choice___call__()

# Generated at 2022-06-13 23:56:14.100874
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    result = choice(items=['a', 'b', 'c'])
    assert result == 'c'
    result = choice(items=['a', 'b', 'c'], length=1)
    assert result == ['a']
    result = choice(items='abc', length=2)
    assert result == 'ba'
    result = choice(items=('a', 'b', 'c'), length=5)
    assert result == ('c', 'a', 'a', 'b', 'c')
    result = choice(items='aabbbccccddddd', length=4, unique=True)
    assert result == 'cdba'


# Generated at 2022-06-13 23:56:16.197216
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    print(c.__call__(items=('a', 'b', 'c'), length=5))

# Generated at 2022-06-13 23:56:21.628481
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    assert isinstance(choice.__call__(items, length=0), str)
    assert isinstance(choice.__call__(items, length=0), str)

# Generated at 2022-06-13 23:56:27.840471
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test type(choice(['a', 'b', 'c'])) == <class 'str'>."""
    choice = Choice()
    assert type(choice(['a', 'b', 'c'])) == str
    assert type(choice(['a', 'b', 'c'], length=1)) == list
    assert type(choice('abc', length=2)) == str
    assert type(choice(('a', 'b', 'c'), length=5)) == tuple
    assert type(choice('aabbbccccddddd', length=4, unique=True)) == str

# Generated at 2022-06-13 23:56:28.578058
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:56:36.400138
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:56:45.806380
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    w = Choice()
    w = Choice()
    w = Choice()
    w = Choice()
    w = Choice()
    w = Choice()
    w = Choice()
    print(w(items=['a', 'b', 'c'], length=1, unique=False))
    print(w(items=['a', 'b', 'c'], length=1, unique=True))
    print(w(items=['a', 'b', 'c'], length=2, unique=False))
    print(w(items=['a', 'b', 'c'], length=5, unique=True))
    print(w(items='aabbbccccddddd', length=4, unique=False))
    print(w(items='aabbbccccddddd', length=4, unique=True))

# Generated at 2022-06-13 23:56:56.246314
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ba', 'bb', 'bc', 'ca', 'cb', 'cc']

# Generated at 2022-06-13 23:59:30.874738
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method :meth:`~mimesis.Choice.__call__`
    of class :class:`~mimesis.Choice`."""
    # TODO: test error and exception cases
    print('Testing Choice.__call__...')
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    print

# Generated at 2022-06-13 23:59:40.214741
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of Choice."""
    import random
    import sys
    import platform

    if sys.platform in ['Windows', 'win32', 'cygwin']:
        seed = random.randint(0, sys.maxsize)
    else:
        seed = random.getrandbits(0o40)
    random.seed(seed)

    args = [['a', 'b', 'c'], [0, 1, 2], ['A','B','C','D','E','F','G',
        'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
        'W','X','Y','Z']]

# Generated at 2022-06-13 23:59:48.940827
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print('')
    choice = Choice()
    print('Choice.__call__'
          '\n----------------')

    print('choice(items=["a", "b", "c"]):\n', choice(items=['a', 'b', 'c']))
    print('choice(items=["a", "b", "c"], length=1):\n', choice(items=['a', 'b', 'c'], length=1))
    print('choice(items="abc", length=2):\n', choice(items='abc', length=2))
    print('choice(items=("a", "b", "c"), length=5):\n', choice(items=('a', 'b', 'c'), length=5))

# Generated at 2022-06-14 00:00:00.129412
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'bc', 'ac']
    assert choice(items=('a', 'b', 'c'), length=5) in [('a', 'b', 'c', 'a', 'b'), ('b', 'c', 'a', 'b', 'c'), ('c', 'a', 'b', 'c', 'a')]
    assert choice(items='aabbbccccddddd', length=4, unique=True) in ['abcd', 'dcba', 'dcab']

# Generated at 2022-06-14 00:00:09.761624
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice

    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']

    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items=['a', 'b', 'c'], length=2) == ['a', 'b']

    assert choice(items=('a', 'b', 'c'), length=5) == ('a', 'b', 'c', 'a', 'b')

    assert choice(items='abc', length=2) in ['ab', 'ba', 'bc', 'cb', 'ca']


# Generated at 2022-06-14 00:00:18.613355
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method Choice.__call__."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ac', 'bc']

# Generated at 2022-06-14 00:00:29.861159
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    import random
    import string

    choice = Choice()
    assert isinstance(choice.random, random.Random)
    choice = Choice(seed=42)
    assert isinstance(choice.random, random.Random)
    choice = Choice('42')
    assert isinstance(choice.random, random.Random)
    choice = Choice(seed='42')
    assert isinstance(choice.random, random.Random)

    items = ['a', 'b', 'c']
    length = 1
    unique = True
    try:
        assert choice(items=None)
    except TypeError:
        assert True
    except Exception:
        assert False
    try:
        assert choice(items=None, length=length)
    except TypeError:
        assert True