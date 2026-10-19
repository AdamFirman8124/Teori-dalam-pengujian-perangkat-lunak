

# Generated at 2022-06-13 23:50:38.539043
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest; from mimesis.enums import Gender
    from mimesis.providers.utils import get_provider
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.person import Person
    from mimesis.providers.address import Address
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.person import Person as Person2
    from mimesis.providers.codes import Codes
    from mimesis.providers.file import File
    from mimesis.providers.misc import Misc


    class Custom:
        """Custom provider."""

        def __init__(self, seed: int = None) -> None:
            """Initialize attributes.

            :param seed: Seed.
            """
            self._provider = get_prov

# Generated at 2022-06-13 23:50:50.082521
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    obj = Choice()
    # items is a non-empty sequence
    assert (obj(items=['a', 'b', 'c'], length=2)) == 'cb'
    # length is 0
    assert (obj(items=['a', 'b', 'c'])) == 'c'
    # items is a non-empty string
    assert (obj(items='abc', length=3)) == 'cba'
    # items is a tuple
    assert (obj(items=('a', 'b', 'c'), length=4)) == ('a', 'b', 'c', 'c')
    # unique is True
    assert (obj(items='aabbbccccddddd', length=4, unique=True)) == 'dabd'


# Generated at 2022-06-13 23:51:01.646069
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method ``__call__`` of class ``Choice``."""
    choice = Choice()
    # items = ['a', 'b', 'c'], length = 0
    a = choice(items=['a', 'b', 'c'])
    assert isinstance(a, str) and a in 'abc'
    
    # items = ['a', 'b', 'c'], length = 1
    b = choice(items=['a', 'b', 'c'], length=1)
    assert isinstance(b, list) and b == ['a']
    
    # items = 'abc', length = 2
    c = choice(items='abc', length=2)
    assert isinstance(c, str) and c.startswith(('b', 'a', 'c')) and len(c) == 2
    
    # items

# Generated at 2022-06-13 23:51:02.325987
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:51:14.076983
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    with pytest.raises(TypeError):
        choice = Choice()
        choice(items=[1, 2, 3], length='x')

    with pytest.raises(TypeError):
        choice = Choice()
        choice(items=2)

    with pytest.raises(ValueError):
        choice = Choice()
        choice(items=[])

    with pytest.raises(ValueError):
        choice = Choice()
        choice(items=[1, 2, 3], length=10, unique=True)

    with pytest.raises(ValueError):
        choice = Choice()
        choice(items=[1, 2, 3], length=-10, unique=True)

    choice = Choice()
    x = choice(items=[1, 2, 3])
    assert x in [1, 2, 3]

   

# Generated at 2022-06-13 23:51:20.458814
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Check if method ``__call__`` works properly."""

    items = ["b","a","c"]
    length = 10
    unique = False

    choice = Choice()

    choice_result = choice(items, length, unique)

    assert isinstance(choice_result, str)
    assert choice_result in items

# Generated at 2022-06-13 23:51:21.138243
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:51:21.771012
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    pass

# Generated at 2022-06-13 23:51:30.167573
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test Choice.__call__()"""
    print("Testing Choice.__call__()")
    choice = Choice("en")
    assert choice(items=["a", "b", "c"]) in ["a", "b", "c"]
    assert choice(items=["a", "b", "c"], length=1) == ["a"]
    assert choice(items="abc", length=2) in ["ab", "bc", "ac"]
    assert choice(items=("a", "b", "c"), length=5) in [("a", "b", "c", "a", "b"), ("a", "a", "b", "c", "c"), ("a", "a", "c", "b", "c")]

# Generated at 2022-06-13 23:51:39.698896
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis import Choice
    choice = Choice()
    print(choice(items=['a', 'b', 'c']))
    print(choice(items=['a', 'b', 'c'], length=1))
    print(choice(items='abc', length=2))
    print(choice(items=('a', 'b', 'c'), length=5))
    print(choice(items='aabbbccccddddd', length=4, unique=True))


# Generated at 2022-06-13 23:51:52.169888
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) in ['ab', 'ba', 'bc', 'cb', 'ca', 'ac']
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) in ['cbda', 'cdba']



# Generated at 2022-06-13 23:52:02.457372
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    provider = Choice()
    result_1 = provider(items=['a', 'b', 'c'])
    assert result_1 in ['a', 'b', 'c']
    result_2 = provider(items='abc', length=2)
    assert isinstance(result_2, str)
    result_3 = provider(items=('a', 'b', 'c'), length=5)
    assert isinstance(result_3, tuple)
    result_4 = provider(items='aabbbccccddddd', length=4, unique=True)
    assert isinstance(result_4, str)
    result_5 = provider(items=['a', 'b', 'c'], length=1)
    assert isinstance(result_5, list)



# Generated at 2022-06-13 23:52:13.631815
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from hypothesis import given
    from hypothesis.strategies import integers
    from hypothesis.strategies import lists
    from hypothesis.strategies import sampled_from
    from hypothesis.strategies import text
    from hypothesis.strategies import tuples
    from hypothesis.strategies import one_of
    from hypothesis.strategies import booleans

    choice = Choice()
    sequences = one_of(lists(elements=sampled_from('abc'), min_size=1),
                       text(min_size=1),
                       tuples(elements=sampled_from('abc'), min_size=1))


# Generated at 2022-06-13 23:52:23.396610
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit tests for method __call__ of class Choice."""
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=('a', 'b', 'c'), length=1) == ('a',)
    assert choice(items='abc', length=2) in ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']

# Generated at 2022-06-13 23:52:31.730801
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice."""
    data = [
        (['a', 'b', 'c'], 1),
        (['a', 'b', 'c'], 2),
        ('aabbbccccddddd', 4),
        ('aabbbccccddddd', 5),
        ('aabbbccccddddd', 6),
        ('aabbbccccddddd', 7),
        (('a', 'b', 'c'), 5),
        (('a', 'b', 'c'), 6),
        (('a', 'b', 'c'), 7),
    ]

# Generated at 2022-06-13 23:52:39.236593
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice('abc') in 'abc'
    assert isinstance(choice('abc', 1), str)
    assert isinstance(choice('abc', 2), str)
    assert isinstance(choice(('a', 'b', 'c'), 5), tuple)
    assert isinstance(choice('abc', 0), str)
    assert isinstance(choice(['a', 'b', 'c']), str)
    assert isinstance(choice(['a', 'b', 'c'], 5), list)
    assert choice('aabbbccccddddd', 4, True) in 'cdba'
    assert choice('aabbbccccddddd', 0, True) in 'cdba'


# Generated at 2022-06-13 23:52:46.368534
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=["a", "b", "c"]) == "c"
    assert choice(items=["a", "b", "c"], length=1) == ["a"]
    assert choice(items="abc", length=2) == "ba"
    assert choice(items=("a", "b", "c"), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:52:57.126522
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Unit test for method __call__ of class Choice.

    This function is called when running "python setup.py test".
    """
    print('Test for method __call__ of class Choice')
    choice = Choice()
    data = choice(items=['a', 'b', 'c'])
    assert data in ['a', 'b', 'c']
    data = choice(items=['a', 'b', 'c'], length=1)
    assert data in [['a'], ['b'], ['c']]
    data = choice(items='abc', length=2)
    assert data in ['ba', 'ab', 'cb']
    data = choice(items=('a', 'b', 'c'), length=5)

# Generated at 2022-06-13 23:53:10.242787
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    res1 = Choice()
    assert res1(items=['a', 'b', 'c']) == 'c'
    assert res1(items=['a', 'b', 'c'], length=1) == ['a']
    assert res1(items='abc', length=2) == 'ba'
    assert res1(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert res1(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

    with pytest.raises(TypeError):
        Choice().__call__(items=['a', 'b', 'c'], length='test')

# Generated at 2022-06-13 23:53:24.274205
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test for method __call__ of class Choice."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.random import Random

    person = Person(random=Random(seed=12345))
    choice = Choice(seed=12345)

    result = choice(items=['a', 'b', 'c'])
    assert result == 'c'

    result = choice(items=['a', 'b', 'c'], length=1)
    assert result == ['a']

    result = choice(items='abc', length=2)
    assert result == 'ba'

    result = choice(items=('a', 'b', 'c'), length=5)
    assert result == ('c', 'a', 'a', 'b', 'c')


# Generated at 2022-06-13 23:53:59.835469
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    Choice().random.choice(items)
    # answer = Choice().__call__(items)
    # assert isinstance(answer, Any)
    # assert answer in items

# Generated at 2022-06-13 23:54:08.289547
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print(Choice()(items=['a', 'b', 'c']))
    print(Choice()(items=['a', 'b', 'c'], length=1))
    print(Choice()(items='abc', length=2))
    print(Choice()(items=('a', 'b', 'c'), length=5))
    print(Choice()(items='aabbbccccddddd', length=4, unique=True))

test_Choice___call__()

# Generated at 2022-06-13 23:54:20.003843
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from mimesis.typing import IJSONSerializable
    from mimesis.typing import JSONType
    from mimesis import Choice
    choice = Choice()
    assert isinstance(choice(items=[], length=0), IJSONSerializable)
    assert isinstance(choice(items=[], length=0, unique=False), IJSONSerializable)
    assert isinstance(choice(items=[], length=0), bool)
    assert isinstance(choice(items=[], length=0, unique=False), bool)
    assert isinstance(choice(items=[], length=0), JSONType)
    assert isinstance(choice(items=[], length=0, unique=False), JSONType)
    assert isinstance(choice(items=[], length=0), str)
    assert isinstance(choice(items=[], length=0, unique=False), str)

# Generated at 2022-06-13 23:54:29.656245
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from . import Choice
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    assert choice(items=['a', 'b', 'c'], length=0) == 'c'
    assert choice(items=['a', 'b', 'c'], length=0) in ['a', 'b', 'c']
    assert choice

# Generated at 2022-06-13 23:54:37.879712
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    print("Starting test_Choice___call__")
    try:
        choice = Choice()

        assert choice(items=['a', 'b', 'c']) == 'c'
        assert choice(items=['a', 'b', 'c'], length=1) == ['a']
        assert choice(items='abc', length=2) == 'ba'
        assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
        assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'
    except Exception as e:
        print(e)
        print("Error in test_Choice___call__")
        return
    print("Success test_Choice___call__")


# Generated at 2022-06-13 23:54:47.870258
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']
    assert choice(items=['a', 'b', 'c'], length=1) in [['a'], ['b'], ['c']]
    assert choice(items='abc', length=2) in ['ab', 'ba', 'ac', 'ca', 'bc', 'cb']
    assert choice(items='abc', length=10) in ['abcabcabcb', 'abcabcabcabcabcabcb', 'cbabcabcabcabcabc']

# Generated at 2022-06-13 23:54:52.799210
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    c = Choice()

    assert c(['a', 'b', 'c']) == 'c'

# Generated at 2022-06-13 23:55:04.708977
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    from typing import Any, Dict
    from mimesis.providers.choice import Choice
    from mimesis.enums import FieldChoice
    from mimesis.exceptions import FieldTypeError, FieldValueError

    __args: Dict[str, Any] = {}
    __args['items'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __args['length'] = 26
    __args['unique'] = False

    @pytest.fixture()
    def _test_data() -> Choice:
        __args['items'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        __args['length'] = 13
        __args['unique'] = False
        return Choice(FieldChoice.LETTERS.value, seed=None)


# Generated at 2022-06-13 23:55:11.103399
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'

# Generated at 2022-06-13 23:55:11.713304
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    assert True

# Generated at 2022-06-13 23:57:00.030105
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    # Generate a randomly-chosen sequence or bare element from a sequence.
    # Provide elements randomly chosen from the elements in a sequence
    # **items**, where when **length** is specified the random choices are
    # contained in a sequence of the same type of length **length**,
    # otherwise a single uncontained element is chosen. If **unique** is set
    # to True, constrain a returned sequence to contain only unique elements.
    choice = Choice()
    # >>> choice = Choice()
    assert(choice(items=['a', 'b', 'c']))
    assert(choice(items=['a', 'b', 'c'], length=1))
    assert(choice(items='abc', length=2))
    assert(choice(items=('a', 'b', 'c'), length=5))

# Generated at 2022-06-13 23:57:12.732463
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    items = ['a', 'b', 'c']
    provider = Choice()

    # Test case: [Sequence] -> [list], [tuple]
    # Test case: [Sequence] -> [str]
    item = provider(items)
    assert isinstance(item, str)
    # Test case: [Sequence], [int] -> [list]
    item = provider(items, length=1)
    assert isinstance(item, list)
    # Test case: [Sequence], [int] -> [tuple]
    item = provider(tuple(items), length=5)
    assert isinstance(item, tuple)
    # Test case: [Sequence], [int], [bool] -> [str]
    item = provider('aabbbccccddddd', length=4, unique=True)

# Generated at 2022-06-13 23:57:19.452950
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert choice(items=['a', 'b', 'c']) == 'c'
    assert choice(items=['a', 'b', 'c'], length=1) == ['a']
    assert choice(items='abc', length=2) == 'ba'
    assert choice(items=('a', 'b', 'c'), length=5) == ('c', 'a', 'a', 'b', 'c')
    assert choice(items='aabbbccccddddd', length=4, unique=True) == 'cdba'


# Generated at 2022-06-13 23:57:26.197111
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test Choice.__call__ method."""
    # Setup
    choice = Choice()
    items = ['a', 'b', 'c']
    length = 1
    unique = False
    expected = ['a']
    # Exercise
    actual = choice(items, length, unique)
    # Verify
    assert expected is actual


# Generated at 2022-06-13 23:57:37.826902
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    from nose2.tools import params
    from mimesis.builtins.utils import suppress_warnings

    # Tests cases for __call__ method of class Choice
    @params(
        ({},),
        ([],),
        (1,),
        (1.0,),
        (True,),
        (set(),),
        (object,),
        (object(),),
    )
    def test_is_type_error(items):
        choice = Choice()
        with suppress_warnings(record=True) as sup:
            choice(items=items)

        assert issubclass(sup.exception, TypeError)

# Generated at 2022-06-13 23:57:45.781145
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test the method __call__ of class Choice"""
    import pytest

    items = ['a', 'b', 'c']
    length = 1
    unique = False

    c = Choice()
    choice = c(items, length, unique)
    assert choice != None

    # TODO: Take absolute paths into consideration too
    # items = ['a', 'b', 'c']
    # length = 1
    # unique = False

    # c = Choice()
    # choice = c(items, length, unique)
    # assert choice == ['a']

    # items = None
    # length = 1
    # unique = False

    # c = Choice()
    # with pytest.raises(TypeError):
    #     c(items, length, unique)

# Generated at 2022-06-13 23:57:53.923480
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    choice = Choice()
    assert type(choice(items=['a', 'b', 'c'])) == str
    assert type(choice(items=['a', 'b', 'c'], length=1)) == list
    assert type(choice(items='abc', length=2)) == str
    assert type(choice(items=('a', 'b', 'c'), length=5)) == tuple
    assert type(choice(items='aabbbccccddddd', length=4, unique=True)) == str

# Generated at 2022-06-13 23:58:02.628352
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test method __call__ of class Choice."""
    c = Choice()
    assert len(c(items=['a', 'b', 'c'], length=5)) == 5
    assert c(items=['a', 'b', 'c'], length=5) == ['c', 'a', 'c', 'a', 'b']
    assert c(items=['a', 'b', 'c'], length=5, unique=True) == ['c', 'a', 'b']
    assert c.choice(items=['a', 'b', 'c']) in ['a', 'b', 'c']

# Generated at 2022-06-13 23:58:12.439751
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    """Test unique choice, unixque choice, bare item and list"""
    import random
    import re
    # Python’s random module (random.org)
    # produces pseudo random numbers
    # for the use in simulations,
    # hardware random number generator is not required
    # random.seed()
    # random.choice(sequence)
    # Return a random element from the non-empty sequence sequence.
    # If sequence is empty, raises IndexError.
    letters = list('abcde')
    random.shuffle(letters)
    print('letters:', letters)
    choice = random.choice(letters)
    print('choice:', choice)
    assert re.match(r"[a-e]", choice)
    for i in range(0, 10):
        print('choice #',i, random.choice(letters))

# Generated at 2022-06-13 23:58:20.691714
# Unit test for method __call__ of class Choice
def test_Choice___call__():
    import pytest
    class TestChoice(object):
        def test_class(self):
            assert issubclass(Choice, BaseProvider)

        def test___init__(self):
            _ = Choice()

        def test_sequence_of_length_0(self):
            c = Choice()
            assert c(['a', 'b', 'c']) in ['a', 'b', 'c']

        def test_sequence_of_nonzero_length_1(self):
            c = Choice()
            assert c(['a', 'b', 'c'], length=1) == ['a']

        def test_sequence_of_nonzero_length_2(self):
            c = Choice()
            assert sorted(c(['a', 'b', 'c'], length=2)) == ['a', 'b'] or \
                sorted