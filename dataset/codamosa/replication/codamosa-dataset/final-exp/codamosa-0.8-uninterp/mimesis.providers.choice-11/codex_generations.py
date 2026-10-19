

# Generated at 2022-06-13 23:52:29.135689
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Test length = 0
    c = Choice(seed=1234)
    assert c(items=['a', 'b', 'c']) == 'a'
    c = Choice(seed=12345)
    assert c(items=['a', 'b', 'c']) == 'a'

    # Test length = 1
    c = Choice(seed=1234)
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    c = Choice(seed=12345)
    assert c(items=['a', 'b', 'c'], length=1) == ['b']

    # Test length > 1
    c = Choice(seed=123)
    assert c(items='abc', length=2) == 'ac'
    c = Choice(seed=1234)

# Generated at 2022-06-13 23:52:38.663213
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    from mimesis.builtins import Choice

# Generated at 2022-06-13 23:52:49.339697
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert Choice().__call__(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert Choice().__call__(items='abc', length=2) in ['ab', 'ba', 'ac', 'ca', 'bc', 'cb']

# Generated at 2022-06-13 23:52:56.723708
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """ Test case for:
    >>> from mimesis import Choice
    >>> choice = Choice()

    >>> choice(items=['a', 'b', 'c'])
    'c'
    >>> choice(items=['a', 'b', 'c'], length=1)
    ['a']
    >>> choice(items='abc', length=2)
    'ba'
    >>> choice(items=('a', 'b', 'c'), length=5)
    ('c', 'a', 'a', 'b', 'c')
    >>> choice(items='aabbbccccddddd', length=4, unique=True)
    'cdba'

    """


# Generated at 2022-06-13 23:52:58.297104
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:53:11.077405
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    _choice = Choice()
    _items = ['a', 'b', 'c']
    assert _choice(items=_items) in _items

    _length = 1
    assert len(_choice(items=_items, length=_length)) == _length

    _items = 'abc'
    _length = 2
    assert len(_choice(items=_items, length=_length)) == _length

    _items = ('a', 'b', 'c')
    _length = 5
    assert len(_choice(items=_items, length=_length)) == _length

    _items = 'aabbbccccddddd'
    _length = 4
    _choice = _choice(items=_items, length=_length, unique=True)
    assert len(_choice) == _length

# Generated at 2022-06-13 23:53:11.916268
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert True

# Generated at 2022-06-13 23:53:24.980129
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = 6
    unique = True
    choice = Choice()
    result = choice(items, length, unique)
    print(result)
    assert len(result) == 6
    unique = False
    result2 = choice(items, length, unique)
    print(result2)
    assert len(result2) == 6

# Test for method __call__ of class Choice
if __name__ == '__main__':
    test_Choice___call__()

# Generated at 2022-06-13 23:53:25.653184
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:53:35.886277
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.providers.choice import Choice

    c = Choice()
    assert c.random.choice(c.local.items) in c.local.items
    assert c.random.choice(c.local.items) in c.local.items
    assert c.random.choice(c.local.items) in c.local.items
    assert c.random.choice(c.local.items) in c.local.items
    assert c.random.choice(c.local.items) in c.local.items
    assert c.random.choice(c.local.items) in c.local.items
    assert c.random.choice(c.local.items) in c.local.items

# Generated at 2022-06-13 23:56:28.212297
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice.
    """
    pass

# Generated at 2022-06-13 23:56:38.489534
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Tests method __call__ of class Choice.
    """
    import random
    import string

    random.seed(2)
    choice = Choice()

    def _check(items, length, unique=False):
        if isinstance(items, str):
            return choice(items=items, length=length, unique=unique)
        else:
            return choice(items=str(items), length=length, unique=unique)

    def _check_exception(items, length, unique=False):
        try:
            if isinstance(items, str):
                choice(items=items, length=length, unique=unique)
            else:
                choice(items=str(items), length=length, unique=unique)
        except Exception as e:
            if isinstance(e, TypeError):
                return True
        return False

    items

# Generated at 2022-06-13 23:56:46.896922
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 5
    unique = True
    result = choice(items, length, unique)
    assert isinstance(result, str)
    assert len(result) == length
    assert ''.join(set(result)) == ''.join(set(items))

# Generated at 2022-06-13 23:56:56.813204
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    import unittest
    import tempfile
    from mimesis.data import DATA

    class ChoiceTestCase(unittest.TestCase):

        def setUp(self):
            self.choice = Choice(localization='en')

        def test___call__(self):
            result = self.choice(DATA['en']['top_level_domains'])
            self.assertIsInstance(result, str)
            self.assertTrue(len(result) > 0)
            self.assertTrue(result in DATA['en']['top_level_domains'])

        def test___call__length(self):
            result = self.choice(DATA['en']['top_level_domains'], length=10)
            self.assertIsInstance(result, list)


# Generated at 2022-06-13 23:57:06.723067
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert type(c(['bla', 'foo'])) == str
    assert c(['bla', 'foo']) in ['bla', 'foo']
    assert type(c(('bla', 'foo'))) == str
    assert c(('bla', 'foo')) in ['bla', 'foo']
    assert type(c(('bla', 'foo'), length=1)) == list
    assert c(('bla', 'foo'), length=1)[0] in ['bla', 'foo']
    assert type(c(['bla', 'foo'], length=1)) == list
    assert c(['bla', 'foo'], length=1)[0] in ['bla', 'foo']
    assert type(c(['bla', 'foo'], length=2)) == list

# Generated at 2022-06-13 23:57:18.765337
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:57:27.175053
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Arrange
    # Input
    length = 4
    items = 'abcde'
    unique = False
    expected = [
        'a',
        'c',
        'b',
        'c',
    ]

    # Act
    result = Choice().__call__(items=items, length=length, unique=unique)

    # Assert
    assert result == expected

# Generated at 2022-06-13 23:57:36.457370
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    items = ['a', 'b', 'c']
    assert c(items) in items
    assert c(items, 3) in [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
    assert c([1, 2, 2], 3) in [(1, 2, 2), (1, 2, 2), (1, 2, 2), (2, 1, 2), (2, 1, 2), (2, 1, 2), (2, 2, 1), (2, 2, 1), (2, 2, 1)]

# Generated at 2022-06-13 23:57:44.202421
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()

    r = choice(['a', 'b', 'c'])
    assert r == "c"

    r = choice(['a', 'b', 'c'], length=1)
    assert r == ["a"]

    r = choice('abc', length=2)
    assert r == "ba"

    r = choice(('a', 'b', 'c'), length=5)
    assert r == ('c', 'a', 'a', 'b', 'c')

    r = choice('aabbbccccddddd', length=4, unique=True)
    assert r == "cdba"

    try:
        r = choice(('a', 'b', 'c'), length="test")
        assert r != "test"
    except TypeError:
        pass


# Generated at 2022-06-13 23:57:54.368969
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ba', 'bc', 'cb', 'ac', 'ca']