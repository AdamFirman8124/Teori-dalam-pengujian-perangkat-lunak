

# Generated at 2022-06-13 23:50:33.499081
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    choice = Choice()
    item_list = ['a', 'b', 'c']
    choice_from_list = choice(items=item_list)
    assert choice_from_list in item_list
    assert isinstance(choice_from_list, str)
    choice_from_list =  choice(items=item_list, length=1)
    assert choice_from_list in item_list
    assert isinstance(choice_from_list, list)
    choice_from_tuple = choice(items=tuple(item_list))
    assert choice_from_tuple in item_list
    assert isinstance(choice_from_tuple, str)
    choice_from_tuple =  choice(items=tuple(item_list), length=1)
   

# Generated at 2022-06-13 23:50:46.560871
# Unit test for method __call__ of class Choice
def test_Choice___call__():
        assert isinstance(Choice().__call__(items=['a', 'b', 'c']), str)
        assert isinstance(Choice().__call__(items=['a', 'b', 'c'], length=1), list)
        assert isinstance(Choice().__call__(items='abc', length=2), str)
        assert isinstance(Choice().__call__(items=('a', 'b', 'c'), length=5), tuple)
        assert isinstance(Choice().__call__(items='aabbbccccddddd', length=4, unique=True), str)

        try:
            Choice().__call__(items=[1, 2, 3], length=4.2)
        except TypeError:
            print('Raised TypeError')
        else:
            print('No TypeError')


# Generated at 2022-06-13 23:50:53.906812
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    for i in range(1000):
        a = choice(items=['a', 'b', 'c'], length=0)
        b = choice(items=('a', 'b', 'c'), length=1)
        c = choice(items='abc', length=2)
        d = choice(items=('a', 'b', 'c'), length=5)
        e = choice(items='aabbbccccddddd', length=4, unique=True)
        f = choice(items=['a', 'b', 'c'], length=2, unique=True)
        g = choice(items='aabbbccccddddd', length=4, unique=False)
        h = choice(items=['a', 'b', 'c'], length=2, unique=False)
        assert a in 'abc'

# Generated at 2022-06-13 23:51:03.549229
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    provider = Choice(random_instance=random_instance)

    # test choice of element from list
    data = provider(items=['a', 'b', 'c'])
    assert isinstance(data, str) and data != ''

    # test choice of elements from list of length 1
    data = provider(items=['a'], length=1)
    assert isinstance(data, list) and len(data) == 1

    # test choice of elements from string of length 1
    data = provider(items='a', length=1)
    assert isinstance(data, str) and len(data) == 1

    # test choice of elements from tuple of length 1
    data = provider(items=('a',), length=1)
    assert isinstance(data, tuple) and len(data) == 1

    # test choice of single element from sequence
   

# Generated at 2022-06-13 23:51:07.182931
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    result = choice(items=items, length=length, unique=unique)
    assert result in ['a', 'b', 'c']

# Generated at 2022-06-13 23:51:10.572123
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method Choice.__call__(). """
    choice = Choice()
    result = choice(items=['a', 'b', 'c'])
    assert isinstance(result, str) and result in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)



# Generated at 2022-06-13 23:51:19.306911
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    with pytest.raises(TypeError) as exc_info:
        choice(items=['a', 'b', 'c'], length='a')
    assert exc_info.type is TypeError

# Generated at 2022-06-13 23:51:29.422075
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c'], 'The first failure'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a'], 'The second failure'
    assert choice(items='abc', length=2) in ['ab', 'bc', 'ac'], 'The third failure'

# Generated at 2022-06-13 23:51:40.256710
# Unit test for method __call__ of class Choice
def test_Choice___call__():  # noqa: D103
    choice = Choice()
    # Should not throw any exception.
    assert choice(items=['a', 'b', 'c']) == 'a'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'aa'
    assert choice(items=('a', 'b', 'c'), length=5) == ('a', 'c', 'b', 'c', 'a')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'ddba'

# Generated at 2022-06-13 23:51:46.110062
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    result1 = choice(items=['a', 'b', 'c'], length=1)
    assert result1 == ['a']
    result2 = choice(items=('a', 'b', 'c'), length=5)
    assert result2 == ('c', 'a', 'a', 'b', 'c')
    result3 = choice(items='aabbbccccddddd', length=4, unique=True)
    assert result3 == 'cdba'

# Generated at 2022-06-13 23:51:54.090468
# Unit test for method __call__ of class Choice

# Generated at 2022-06-13 23:51:59.929146
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.providers.choice import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items='abc') in ['a', 'b', 'c']


# Generated at 2022-06-13 23:52:06.556183
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    assert choice(items, length, unique) == ['a']

    choice = Choice()
    items = ['a', 'b', 'c']
    length = 0
    unique = False
    assert choice(items, length, unique) == 'a'

    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = True
    assert choice(items, length, unique) != ['a']

    choice = Choice()
    items = ['a', 'b', 'c']
    length = 0
    unique = True
    assert choice(items, length, unique) != 'a'

# Generated at 2022-06-13 23:52:07.597634
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""

# Generated at 2022-06-13 23:52:13.631446
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert Choice().__call__(['a', 'b', 'c']) == 'c'
    assert Choice().__call__(['a', 'b', 'c'], 1) == ['a']
    assert Choice().__call__('abc', 2) == 'ba'
    assert Choice().__call__(('a', 'b', 'c'), 5) == ('c', 'a', 'a', 'b', 'c')
    assert Choice().__call__('aabbbccccddddd', 4, True) == 'cdba'


# Generated at 2022-06-13 23:52:17.067126
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:52:21.421618
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice("abcd")
    assert choice("abcd", 0)
    assert choice("abcd", 1)
    assert choice("abcd", 2)
    assert choice("abcd", 3)
    assert choice("abcd", 4)
    assert choice("abcd", 5)
    assert choice("abcd", 4, True)
    assert choice("abcd", 5, True)


# Generated at 2022-06-13 23:52:29.800506
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:52:38.875862
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'bc', 'ca']

# Generated at 2022-06-13 23:52:49.364788
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(['a', 'b', 'c']) not in ['a', 'b', 'c']
    assert c(['a', 'b', 'c'], 1) in [['a'], ['b'], ['c']]
    assert c(['a', 'b', 'c'], 2) in [['a', 'a'], ['b', 'b'], ['c', 'c']]
    assert c(['a', 'b', 'c'], 3) in [['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b']]

# Generated at 2022-06-13 23:52:59.717440
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method Choice.__call__."""
    choice = Choice()

    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    assert choice(items=['a', 'b', 'c'], length=2) != ['a', 'a']

# Generated at 2022-06-13 23:53:06.724200
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:53:12.073659
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    choice = Choice()
    result = choice(items=items, length=length, unique=unique)
    assert result == ['a']


# Generated at 2022-06-13 23:53:21.190675
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()

    assert c(items=['a', 'b', 'c']) == 'c'
    assert c(items=['a', 'b', 'c'], length=1) == ['a']
    assert c(items='abc', length=2) == 'ba'
    assert c(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert c(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:53:30.388739
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for function __call__ of class Choice."""

    choice = Choice()

    # test single value
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=(1, 2, 3)) in [1, 2, 3]
    assert choice(items='abc') in ['a', 'b', 'c']
    assert choice(items='a123') in ['a', '1', '2', '3']

    # test length
    assert len(choice(items=['a', 'b', 'c'], length=1)) == 1
    assert len(choice(items=(1, 2, 3), length=2)) == 2
    assert len(choice(items='abc', length=3)) == 3
    assert len(choice(items='a123', length=4))

# Generated at 2022-06-13 23:53:39.354335
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""
    c = Choice()

    result = c(items=['a', 'b', 'c'])
    assert result.__class__.__name__ == 'str'

    result = c(items=['a', 'b', 'c'], length=1)
    assert result.__class__.__name__ == 'list'

    result = c(items='abc', length=2)
    assert result.__class__.__name__ == 'str'

    result = c(items=('a', 'b', 'c'), length=5)
    assert result.__class__.__name__ == 'tuple'

    result = c(items='aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:53:48.437619
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert len(Choice().__call__(items=['a', 'b', 'c'])) == 1
    assert len(Choice().__call__(items=['a', 'b', 'c'], length=1)) == 1
    assert len(Choice().__call__(items='abc', length=2)) == 2
    assert len(Choice().__call__(items=('a', 'b', 'c'), length=5)) == 5
    assert len(Choice().__call__(items='aabbbccccddddd', length=4, unique=True)) == 4


# Generated at 2022-06-13 23:53:56.261589
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    provider = Choice()
    assert provider(items=['a', 'b', 'c']) == 'c'
    assert provider(items=['a', 'b', 'c'], length=1) == ['a']
    assert provider(items='abc', length=2) == 'ba'
    assert provider(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert provider(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:54:10.076063
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """ Unit test for method __call__ of class Choice """
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    try:
        choice(items=['a', 'b', 'c'], length='abc')
    except TypeError:
        assert 1
    else:
        assert 0

# Generated at 2022-06-13 23:54:16.813358
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert c(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert c(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert c(items='abc', length=2) in ['ba', 'ab', 'ac', 'bc']

# Generated at 2022-06-13 23:54:28.630392
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items_list = ['a', 'b', 'c']
    length_int = 1
    unique_bool = False
    ch = Choice()
    assert ch(items_list, length_int, unique_bool) == 'b'


# Generated at 2022-06-13 23:54:36.298677
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__."""
    c = Choice()
    items = c(items=[1, 2, 3], length=1)
    assert items == [1]
    items = c(items=[1, 2, 3], length=2, unique=True)
    assert items == [3, 1]

    items = c(items=(1, 2, 3), length=2, unique=True)
    assert items == (2, 3)
    items = c(items='abcd', length=1)
    assert items == 'c'
    items = c(items='abcd', length=5)
    assert items == 'adcba'


# Generated at 2022-06-13 23:54:46.102820
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a','b','c']
    unique = True
    length = 1
    assert Choice.__call__(Choice, items, length, unique) == ['c']

    items = ['a', 'b', 'c']
    unique = True
    length = 1
    assert Choice.__call__(Choice, items, length, unique) == ['c']

    items = 'abc'
    unique = True
    length = 2
    assert Choice.__call__(Choice, items, length, unique) == 'ba'

    items = ('a', 'b', 'c')
    unique = True
    length = 1
    assert Choice.__call__(Choice, items, length, unique) == ('c',)

# Generated at 2022-06-13 23:54:50.364258
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from hypothesis import given
    from hypothesis import strategies as st

    @given(st.lists(st.integers()), st.integers(), st.booleans())
    def test(data: list, length: int, unique: bool):
        items = data
        assert Choice().__call__(items, length, unique)

    test()

# Generated at 2022-06-13 23:54:58.469549
# Unit test for method __call__ of class Choice

# Generated at 2022-06-13 23:55:07.344033
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    def test():
        for _ in range(10):
            data=Choice().__call__(items=['a', 'b', 'c'], length=1)
            assert isinstance(data,list)
            assert data[0] in ['a', 'b', 'c']
            data=Choice().__call__(items=['a', 'b', 'c'], length=2)
            assert isinstance(data,list)
            assert data[0] in ['a', 'b', 'c']
            assert data[1] in ['a', 'b', 'c']
            data=Choice().__call__(items=['a', 'b', 'c'], length=3)
            assert isinstance(data,list)
            assert data[0] in ['a', 'b', 'c']

# Generated at 2022-06-13 23:55:16.765888
# Unit test for method __call__ of class Choice
def test_Choice___call__():

    from mimesis import Choice
    choice = Choice()

    item = choice(items=[1, 2, 3, 4, 5])
    assert item in [1, 2, 3, 4, 5]

    assert len(choice(items=[1, 2, 3, 4, 5], length=3)) == 3
    assert choice(items=['a', 'b', 'c', 'd'], length=2) in [['a', 'b'],
                                                            ['a', 'c'],
                                                            ['a', 'd'],
                                                            ['b', 'c'],
                                                            ['b', 'd'],
                                                            ['c', 'd']]
    assert choice(items='abcd', length=3) in ['abc', 'bac', 'bca', 'cab', 'cba']

# Generated at 2022-06-13 23:55:26.938371
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice"""
    # TODO: Remove this method and use the test in test.py
    choice = Choice()

    # Call assert_equal explicitly
    # pylint: disable=E1101
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:55:36.987403
# Unit test for method __call__ of class Choice
def test_Choice___call__(): #type: ignore
    from mimesis import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:55:44.903250
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""

    from mimesis.providers.choice import Choice
    c = Choice()

    #  Test with a list of items
    items = ['a', 'b', 'c', 'd', 'e']
    result = c(items=items)
    print(result)
    assert result in items

    #  Test with a list of items
    items = ['a', 'b', 'c', 'd', 'e']
    result = c(items=items, unique=True)
    print(result)
    assert result in items

    #  Test with a list of items
    items = ['a', 'b', 'c', 'd', 'e']
    result = c(items=items, length=2, unique=True)
    print(result)

# Generated at 2022-06-13 23:56:15.393353
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Generate a randomly-chosen sequence or bare element from a sequence.
    # Provide elements randomly chosen from the elements in a sequence **items**, where when **length** is specified the
    # random choices are contained in a sequence of the same type of length **length**, otherwise a single uncontained
    # element is chosen. If **unique** is set to True, constrain a returned sequence to contain only unique elements.
    assert Choice().choice(items=['a', 'b', 'c']) == 'c'
    assert Choice().choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert Choice().choice(items='abc', length=2) == 'ba'

# Generated at 2022-06-13 23:56:21.893091
# Unit test for method __call__ of class Choice
def test_Choice___call__():
# Input parameters
    items = ['a', 'b', 'c']
    length = 1
    unique = False
# Expected output
    expected = ['a']
# Computed output
    obj = Choice()
    computed = obj(items, length, unique)
# Compare outputs
    assert (computed == expected)


# Generated at 2022-06-13 23:56:25.633215
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    data = choice._Choice__call__(['a', 'b', 'c'], length=2)
    assert (data[0] == 'b' and data[1] == 'c') or (data[0] == 'c' and data[1] == 'b')

# Generated at 2022-06-13 23:56:35.770544
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Positive tests
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ba', 'ca', 'ab', 'cb', 'ac', 'bc']

# Generated at 2022-06-13 23:56:41.799661
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import PYTHON_VERSIONS
    from collections import Counter
    import sys
    import pytest
    from hypothesis import given
    from hypothesis.strategies import integers, lists, text

    choice = Choice(PYTHON_VERSIONS.CURRENT)

    assert choice('a') == 'a'
    assert choice(['a', 'b']) == 'b'
    assert choice('abc', 0) == 'c'
    assert choice(('a', 'b', 'c'), 1) == ('a',)
    assert ''.join(choice(('a', 'b', 'c'), 2)) == 'ab'
    assert choice(['a', 'b', 'c'], 3) == ['c', 'a', 'a']

# Generated at 2022-06-13 23:56:54.610557
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Function to test choice."""
    from mimesis.providers.choice import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    #assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ba', 'ac', 'bc']
    assert len(choice(items=('a', 'b', 'c'), length=5)) == 5

# Generated at 2022-06-13 23:56:59.300712
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    list_ = ['a', 'b', 'c', 'd']
    choice = Choice()
    assert choice(items=list_, length=1) in list_, \
        ('test_Choice___call__() failed '
         'with list_ = {0}'.format(list_))

# Generated at 2022-06-13 23:57:03.906953
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""

    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=[1, 2, 3], length=2) in [[1, 1], [1, 2], [1, 3],
                                                  [2, 1], [2, 2], [2, 3],
                                                  [3, 1], [3, 2], [3, 3]]
    assert choice(items=[], length=1) is None
    assert choice(items=None, length=5) is None

# Generated at 2022-06-13 23:57:14.288243
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert isinstance(c(items=['a', 'b', 'c']), str)
    assert isinstance(c(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(c(items='abc', length=2), str)
    assert isinstance(c(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(c(items='aabbbccccddddd', length=4, unique=True), str)
    try:
        c(items=['a', 'b', 'c'], length=1.5)
    except TypeError:
        assert True
    except Exception:
        assert False
    try:
        c(items=12345, length=1)
    except TypeError:
        assert True
   

# Generated at 2022-06-13 23:57:24.113715
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.enums import Gender
    from mimesis.typing import GenderEnum
    from mimesis.providers.address import Address
    from mimesis.providers.geography import Geography
    from mimesis.providers.internet import Internet
    from mimesis.providers.misc import Misc
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.personal import Personal

    Choice(seed=12345)
    Address(seed=12345)
    Geography(seed=12345)
    Internet(seed=12345)
    Misc(seed=12345)
    Numbers(seed=12345)
    Personal(seed=12345)

    assert Choice().choice(['a', 'b', 'c']) == 'c'

# Generated at 2022-06-13 23:58:20.722419
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    if choice(['a', 'b', 'c']) != 'c':
        return False
    if choice(['a', 'b', 'c'], length=1) != ['a']:
        return False
    if choice('abc', length=2) != 'ba':
        return False
    if choice(('a', 'b', 'c'), length=5) != ('c', 'a', 'a', 'b', 'c'):
        return False
    if choice('aabbbccccddddd', length=4, unique=True) != 'cdba':
        return False
    try:
        choice(items=['a', 'b', 'c'], length='123')
        return False
    except TypeError:
        pass

# Generated at 2022-06-13 23:58:31.731263
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice
    The test_Choice___call__ method checks for cases that are not covered
    by the implementation:
    - TypeError for non-sequence items
    - ValueError for empty items
    - TypeError for non-integer length
    - ValueError for negative length
    - ValueError for insufficient unique elements
    """
    from mimesis import Choice
    choice = Choice()

    # TypeError for non-sequence items
    items = 0
    length = 3
    unique = False
    try:
        choice(items=items, length=length, unique=unique)
        raise Exception("TypeError expected for non-sequence items")
    except TypeError:
        pass
    except Exception as ex:
        raise Exception("Unexpected exception") from ex

    # ValueError for empty items
    items = []
    length

# Generated at 2022-06-13 23:58:46.927016
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    seed_1 = 1234
    seed_2 = 1234
    items = ['a', 'b', 'c']
    length = 1
    length_1 = 1
    length_2 = 2
    length_5 = 5
    length_9 = 9
    unique_1 = True
    unique_2 = True
    unique_3 = False
    unique_4 = False
    unique_5 = False
    unique_6 = False

    # Test case 1 - unique elements
    choice_1 = Choice(seed=seed_1)
    data_1 = choice_1(items=items, length=length, unique=unique_1)
    data_2 = choice_1(items=items, length=length_1, unique=unique_2)
    assert data_1 == data_2

    # Test case 2 - non-unique elements
   

# Generated at 2022-06-13 23:58:53.260692
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method Choice.__call__."""
    choice = Choice()
    choice(items=['a', 'b', 'c'])
    choice(items=['a', 'b', 'c'], length=1)
    choice(items='abc', length=2)
    choice(items=('a', 'b', 'c'), length=5)
    choice(items='aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:59:05.608200
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test __call__ of Choice."""
    choice = Choice()
    assert isinstance(choice(items=['a', 'b', 'c']), str)
    assert isinstance(choice(items=['a', 'b', 'c'], length=1), list)
    assert isinstance(choice(items='abc', length=2), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=5), tuple)
    assert isinstance(choice(items='aabbbccccddddd', length=4, unique=True), str)

    with pytest.raises(TypeError):
        choice(items=['a', 'b', 'c'], length='a')

    with pytest.raises(TypeError):
        choice(items={'a', 'b', 'c'})


# Generated at 2022-06-13 23:59:08.151299
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    choice = Choice()
    ans = choice(items, length, unique)
    print(ans)
    assert True


# Generated at 2022-06-13 23:59:12.557553
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    print('*** Printing output of __call__ method of class Choice:')
    choice(items=['a', 'b', 'c'])
    choice(items=['a', 'b', 'c'], length=1)
    choice(items='abc', length=2)
    choice(items=('a', 'b', 'c'), length=5)
    choice(items='aabbbccccddddd', length=4, unique=True)
    print('*** Finished printing output of __call__ method of class Choice.')

# Generated at 2022-06-13 23:59:20.210144
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False

    assert isinstance(choice(items=items), str)
    assert isinstance(choice(items=items, length=length), list)
    assert isinstance(choice(items='abc', length=length + 1), str)
    assert isinstance(choice(items=('a', 'b', 'c'), length=length + 4), tuple)

    # Create a sequence of length-4 of unique items from string "aabbbcccc"
    assert len(choice(items='aabbbcccc', length=length + 3, unique=True)) == 4
    assert len(set(choice(items='aabbbcccc', length=length + 3, unique=True))) == 4

    # Expect exception when items is empty

# Generated at 2022-06-13 23:59:30.757157
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    # Test the case where items is a list, length is 0 and unique is False
    assert choice(items=['a', 'b', 'c'], length=0, unique=False) in ['a', 'b', 'c']
    # Test the case where items is a tuple, length is a positive integer and unique is False
    assert choice(items=('a', 'b', 'c'), length=1, unique=False) == ('c',)
    assert choice(items=('a', 'b', 'c'), length=2, unique=False) in [('b', 'c'), ('a', 'c'), ('c', 'a')]
    # Test the case where items is a string, length is a positive integer and unique is True

# Generated at 2022-06-13 23:59:39.930589
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()
    assert isinstance(c('a'), str)
    assert isinstance(c(['a', 'b', 'c'], 3), list)
    try:
        c(['a', 'b', 'c'], 2.0)
    except TypeError:
        pass
    except:
        assert False
    try:
        c(['a', 'b', 'c'], -3)
    except ValueError:
        pass
    except:
        assert False
    try:
        c('', 3)
    except ValueError:
        pass
    except:
        assert False
    try:
        c(['a', 'b', 'c'], 2, True)
    except ValueError:
        pass
    except:
        assert False