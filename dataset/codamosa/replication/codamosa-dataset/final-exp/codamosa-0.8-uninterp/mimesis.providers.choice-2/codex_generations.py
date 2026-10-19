

# Generated at 2022-06-13 23:50:38.209141
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert c(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert c(items='abc', length=2) in ['ab', 'ba', 'ac', 'ca', 'bc', 'cb']
    assert isinstance(c(items='abc', length=2), str)

# Generated at 2022-06-13 23:50:43.086451
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    from mimesis import Choice
    choice = Choice()

    # 2 choices
    choice(items=['a', 'b', 'c'])
    return choice(items=['a', 'b', 'c'], length=1) == ['a']

# Generated at 2022-06-13 23:50:49.600222
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    #Test one
    assert choice(items = ['a', 'b', 'c'])

    #Test two
    assert choice(items = ['a', 'b', 'c'], length = 1)

    #Test three
    assert choice(items = 'abc', length = 2)

    #Test four
    assert choice(items = ('a', 'b', 'c'), length = 5)

    #Test five
    assert choice(items = 'aabbbccccddddd', length = 4, unique = True)


# Generated at 2022-06-13 23:50:59.170129
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis import Choice
    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)


# Generated at 2022-06-13 23:51:11.540472
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    from mimesis.enums import Gender
    from mimesis.providers.base import BaseProvider

    prov = BaseProvider('en') # Create a English based provider

    # Initialize the class
    choice = Choice(prov)

    # Generate a choice
    choice_one = choice(items=Gender.ALL)

    # Generate a choice with a length
    choice_two = choice(items=Gender.ALL, length=2)

    # Generate a choice with a length and unique elements
    choice_three = choice(items=Gender.ALL, length=2, unique=True)

    # Test that the __call__ method works as expected
    assert choice_one in prov.gender.all
    assert len(choice_two) == 2
    assert len(choice_three) == 2
    assert choice_one

# Generated at 2022-06-13 23:51:15.114474
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    provider = Choice()
    assert provider("aabbccddeeff") == "ebafddaebdccffcfe"

if __name__ == "__main__":
    test_Choice___call__()

# Generated at 2022-06-13 23:51:26.253133
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) != None
    assert choice(items=['a', 'b', 'c'], length=1) != None
    assert choice(items='abc', length=2) != None
    assert choice(items=('a', 'b', 'c'), length=5) != None
    assert choice(items='aabbbccccddddd', length=4, unique=True) != None
    assert choice(items=[1, 2, 3], length=4) != None
    assert choice(items=[1, 2, 3], length=3) != None
    assert choice(items=[1, 2, 3], length=2) != None
    assert choice(items=[1, 2, 3], length=1) != None

# Generated at 2022-06-13 23:51:33.440279
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice.__call__(Choice(seed=12345), items=['a', 'b', 'c']) == 'c'
    assert Choice.__call__(Choice(seed=12345), items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice.__call__(Choice(seed=12345), items='abc', length=2) == 'ba'
    assert Choice.__call__(Choice(seed=12345), items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice.__call__(Choice(seed=12345), items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:51:39.514409
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in {'a', 'b', 'c'}
    assert choice(items=['a', 'b', 'c'], length=1) in {['a'], ['b'], ['c']}
    assert choice(items='abc', length=2) in {'aa', 'ab', 'ac', 'ba',
                                             'bb', 'bc', 'ca', 'cb', 'cc'}

# Generated at 2022-06-13 23:51:45.291967
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert(type(choice('abc')) == str)
    assert(len(choice('abc', 4)) == 4)
    assert(len(choice('abc', 4)) == 4)
    assert(len(choice('abc', 4, True)) == 4)
    assert(len(choice(('a', 'b', 'c'), 5)) == 5)
    assert(len(choice('aabbbccccddddd', 4, True)) == 4)


# Generated at 2022-06-13 23:52:14.840503
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ab', 'ac', 'bc']
    assert choice(items=('a', 'b', 'c'), length=5) in [('a', 'a', 'b', 'c', 'c'), ('c', 'a', 'a', 'b', 'c')]

# Generated at 2022-06-13 23:52:27.403257
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    data = Choice().__call__(['a', 'b', 'c'], length=3, unique=True)
    assert len(data) == 3
    assert data[0] in ['a', 'b', 'c']
    assert data[1] in ['a', 'b', 'c']
    assert data[2] in ['a', 'b', 'c']
    assert data[0] != data[1] != data[2]

    data = Choice().__call__(['a', 'b', 'c'], length=5, unique=False)
    assert len(data) == 5
    assert all(elem in ['a', 'b', 'c'] for elem in data)
    assert ['a', 'b', 'c'] == list(set(data))


# Generated at 2022-06-13 23:52:28.177515
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert choice(items='abc', length=2) == 'bc'



# Generated at 2022-06-13 23:52:32.196172
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 10
    unique = True
    result = choice(items, length, unique)
    print(result)


# Generated at 2022-06-13 23:52:46.523046
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test __call__ method."""
    choice = Choice()
    assert type(choice.items) == list

    data = choice.__call__(items=['a', 'b', 'c'], length=1)
    assert type(data) == list
    assert len(data) == 1

    # data = choice.__call__(items='abc', length=2)
    # assert type(data) == str
    # assert len(data) == 2

    data = choice(items=('a', 'b', 'c'), length=5)
    assert type(data) == tuple
    assert len(data) == 5

    data = choice(items='aabbbccccddddd', length=4, unique=True)
    assert type(data) == str
    assert len(data) == 4


# Generated at 2022-06-13 23:52:47.330350
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:52:48.129061
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:52:54.350418
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice.

    :return: True if test passed, else False.
    """
    c = Choice()
    items = ['a', 'b', 'c']
    number = 1
    unique = False
    assert c(items=items, length=number, unique=unique) == ['a']
    return True

# Generated at 2022-06-13 23:53:03.428740
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Check if method __call__ of class Choice returns correct data."""
    from mimesis import Choice

    provider = Choice(seed=0)
    result = provider(items='abc', length=0)
    assert result == 'c'
    result = provider(items=('a', 'b', 'c'), length=1)
    assert result == ('a',)
    result = provider(items='abc', length=2)
    assert result == 'ba'
    result = provider(items=['a', 'b', 'c'], length=5)
    assert result == ['c', 'a', 'a', 'b', 'c']
    result = provider(items='aabbbccccddddd', length=4, unique=True)
    assert result == 'cdba'

    provider = Choice(seed=1)
    result = provider

# Generated at 2022-06-13 23:53:11.859613
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for Choice.__call__."""
    choice = Choice()

    # try:
    #     choice(items=[], length=1)
    #     assert False, 'Failed to raise expected ValueError'
    # except ValueError:
    #     assert True, 'Raised expected ValueError'

    assert choice(items=[2, 3]) in [2, 3]

    assert choice(items="abc", length=1) in "abc"
    assert choice(items="abc", length=2) in ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "c"]
    assert choice(items="abc", length=0) in "abc"

# Generated at 2022-06-13 23:53:50.841681
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert len(choice(items=['a', 'b', 'c'], length=1)) == 1
    # When length is 1, return as list
    assert choice(items='abc', length=2) in ['ab', 'ba', 'cb']
    assert len(choice(items=('a', 'b', 'c'), length=5)) == 5

# Generated at 2022-06-13 23:53:51.344934
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:53:57.604635
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c']) == 'c'
    assert Choice().__call__(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice().__call__(items='abc', length=2) == 'ba'
    assert Choice().__call__(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:54:01.505811
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert (choice(items=['a', 'b', 'c']) == 'c')
    assert (choice(items=['a', 'b', 'c'], length=1) == ['a'])
    assert (choice(items='abc', length=2) == 'ba')
    assert (choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c'))
    assert (choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba')


# Generated at 2022-06-13 23:54:04.442505
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    # TODO: Test for method Choice.__call__
    pass

# Generated at 2022-06-13 23:54:16.733897
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""

    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'bc', 'ca']
    assert choice(items=('a', 'b', 'c'), length=5) in [('a', 'b', 'c', 'a', 'b'),
                                                       ('a', 'b', 'c', 'b', 'c'),
                                                       ('a', 'b', 'c', 'c', 'a')]

# Generated at 2022-06-13 23:54:25.927612
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    provider = Choice()
    assert provider(['a', 'b', 'c'], 0) == 'c'
    assert provider(['a', 'b', 'c'], 1) == ['a']
    assert provider('abc', 2) == 'ba'
    assert provider(('a', 'b', 'c'), 5) == ('c', 'a', 'a', 'b', 'c')
    assert provider('aabbbccccddddd', 4, True) == 'cdba'

# Generated at 2022-06-13 23:54:30.809608
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = 'abc'
    length = 5
    unique = True

    choice = Choice()
    assert isinstance(choice(items, length, unique), (str, list))
    assert len(choice(items, length, unique)) == length
    assert choice(items, length, unique) == 'aabbc'


# Generated at 2022-06-13 23:54:40.590141
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    try:
        assert choice(items='abc', length=1.0)
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 23:54:52.483204
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print("Running tests for Choice.__call__()")

    from mimesis import Choice
    choice = Choice()

    # Testing exceptions
    try:
        choice(items='a', length=None)
    except TypeError:
        pass
    else:
        print("Test case 1: Failure")
    try:
        choice(items='a', length=1.0)
    except TypeError:
        pass
    else:
        print("Test case 2: Failure")
    try:
        choice(items='a', length='a')
    except TypeError:
        pass
    else:
        print("Test case 3: Failure")
    try:
        choice(items=('a', 'b', 'c'), length=-1)
    except ValueError:
        pass
    else:
        print("Test case 4: Failure")
   

# Generated at 2022-06-13 23:55:59.731761
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test that Choice supports its parameters."""
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']

# Generated at 2022-06-13 23:56:06.071183
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    items = ['a', 'b', 'c']
    result1 = choice(items, 0)
    result2 = choice(items, 1)
    result3 = choice(items, 2)
    result4 = choice(items, 3)
    result5 = choice(items, 1, unique=True)
    assert result1 in items
    assert len(result2) == 1
    assert len(result3) == 2
    assert len(result4) == 3
    assert len(result5) == 1

# Generated at 2022-06-13 23:56:08.212519
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit testing of method __call__ of class Choice."""
    pass # TODO


# Generated at 2022-06-13 23:56:19.796559
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    assert choice(items=('a', 'b', 'c'), length=5) in [['a', 'b', 'c', 'c', 'a'], ['b', 'c', 'a', 'a', 'b'], ['c', 'a', 'a', 'b', 'c']]

# Generated at 2022-06-13 23:56:24.278866
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = True

    assert choice(items, length, unique) == ['a']
    assert choice(items, length, unique) == ['c']
    assert choice(items, length, unique) == ['c']

# Generated at 2022-06-13 23:56:34.636337
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import random
    import string
    test_seq = ''.join(random.choices(string.ascii_letters+string.digits, k=10)
                       )  # test sequence of random string
    test_int = random.randint(2, 10)  # test length
    print('random sequence:', test_seq)
    print('random length:', test_int)
    c = Choice()
    print(c(test_seq, test_int))


# if __name__ == '__main__':
#     print(Choice().__init__())
#     # print(Choice().__call__())
#     print(Choice().__call__())

# Generated at 2022-06-13 23:56:41.081958
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    
    assert choice(items=['a', 'b', 'c']) == 'b'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'cb'
    assert choice(items=('a', 'b', 'c'), length=3) == ('c', 'b', 'b')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'bcaa'
    try:
        choice(items=['a'], length=-1)
    except ValueError:
        pass
    try:
        choice(items=['a'], length=5)
    except ValueError:
        pass

# Generated at 2022-06-13 23:56:55.495572
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    obj = Choice()
    item = obj(items=['a', 'b', 'c'])
    assert item in 'abc'

    item = obj(items=['a', 'b', 'c'], length=1)
    assert item in ('a', 'b', 'c')

    item = obj(items='abc', length=2)
    assert item in ('ab', 'ba', 'ac', 'ca', 'bc', 'cb')

    item = obj(items=('a', 'b', 'c'), length=5)

# Generated at 2022-06-13 23:57:01.720059
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests for method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c'])
    assert choice(items=['a', 'b', 'c'], length=1)
    assert choice(items='abc', length=2)
    assert choice(items=('a', 'b', 'c'), length=5)
    assert choice(items='aabbbccccddddd', length=4, unique=True)


# Generated at 2022-06-13 23:57:13.125558
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:59:20.524578
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method ``__call__`` of class ``Choice``."""
    # TODO: Improve test coverage

    import random
    import unittest

    from mimesis.enums import Gender
    from mimesis.providers.person import Person


# Generated at 2022-06-13 23:59:30.540653
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    items = ['a', 'b', 'c']
    length = 1
    unique = True
    choice = Choice()
    r = choice(items=['a', 'b', 'c'])
    t = choice(items=['a', 'b', 'c'], length=1)
    d = choice(items='abc', length=2)
    e = choice(items=('a', 'b', 'c'), length=5)
    f = choice(items='aabbbccccddddd', length=4, unique=True)
    assert len(r) > 0
    assert len(t) > 0
    assert len(d) > 0
    assert len(e) > 0
    assert len(f) > 0

# Generated at 2022-06-13 23:59:39.033798
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert (choice(items=['a', 'b', 'c']) == 'c')
    assert (choice(items=['a', 'b', 'c'], length=1) == ['a'])  # type: ignore
    assert (choice(items='abc', length=2) == 'ba')  # type: ignore
    assert (choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c'))
    assert (choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba')

# Generated at 2022-06-13 23:59:54.357297
# Unit test for method __call__ of class Choice

# Generated at 2022-06-13 23:59:55.909542
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:59:57.276772
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass # TODO: add test


# Generated at 2022-06-14 00:00:08.337996
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.choice import Choice
    choice = Choice('en')
    assert choice('abc') in 'abc'
    assert choice('abc', length=1) in 'abc'
    assert choice('abc', length=2) in 'abc'
    assert choice('abc', length=5) in 'abc'
    assert choice('12345', length=3, unique=True) in '12345'
    assert choice('aabbbccccddddd', length=4, unique=True) in 'aabbbccccddddd'

# Generated at 2022-06-14 00:00:17.331214
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    print( c(items=['a', 'b', 'c']) )
    print( c(items=['a', 'b', 'c'], length=1) )
    print( c(items='abc', length=2) )
    print( c(items=('a', 'b', 'c'), length=5) )
    print( c(items='aabbbccccddddd', length=4, unique=True) )

if __name__ == "__main__":
    test_Choice___call__()