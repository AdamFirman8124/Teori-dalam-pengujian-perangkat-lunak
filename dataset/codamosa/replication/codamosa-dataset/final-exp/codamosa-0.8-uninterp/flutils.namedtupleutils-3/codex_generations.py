

# Generated at 2022-06-13 20:32:44.160374
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    obj = ['a', (1, 2)]
    exp = ['a', (1, 2)]
    obs = to_namedtuple(obj)
    assert obs == exp

    obj = [(1, 2), ['a', (1, 2)], 'a']
    exp = [(1, 2), ['a', (1, 2)], 'a']
    obs = to_namedtuple(obj)
    assert obs == exp

    obj = {'a': 1, 'b': 2}
    exp = namedtuple('NamedTuple', 'a b')(a=1, b=2)
    obs = to_namedtuple(obj)
    assert obs == exp

    obj = {'b': 2, 'a': 1}

# Generated at 2022-06-13 20:32:54.439572
# Unit test for function to_namedtuple
def test_to_namedtuple():
    #
    # Example 1: Convert dictionary to namedtuple.
    #
    dic = {'a': 1, 'b': 2}
    tup = to_namedtuple(dic)
    assert isinstance(tup, NamedTuple)
    assert hasattr(tup, 'a')
    assert hasattr(tup, 'b')
    assert tup.a == 1
    assert tup.b == 2
    dic['a'] = 4
    assert tup.a == 1
    #
    # Example 2: Convert dictionary to namedtuple with nested dictionary.
    #
    dic = {'a': {'b': 2}}
    tup = to_namedtuple(dic)
    assert isinstance(tup.a, NamedTuple)

# Generated at 2022-06-13 20:33:05.328062
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Allowed types
    assert to_namedtuple(list()) == [], "list"
    assert to_namedtuple(tuple()) == (), "tuple"
    assert to_namedtuple(dict()) == \
           NamedTuple(arg1=1, arg2=2, arg3=3), "dict"
    assert to_namedtuple(OrderedDict({'arg1': 1, 'arg2': 2, 'arg3': 3})) == \
           NamedTuple(arg1=1, arg2=2, arg3=3), "OrderedDict"
    assert to_namedtuple(SimpleNamespace(arg1=1, arg2=2, arg3=3)) == \
           NamedTuple(arg1=1, arg2=2, arg3=3), "SimpleNamespace"

    # All

# Generated at 2022-06-13 20:33:14.072519
# Unit test for function to_namedtuple
def test_to_namedtuple():
    a = list([1, 2, 3, 4, 5])
    b = to_namedtuple(a)
    b[0] = 9
    assert a[0] != 9
    a = tuple((1, 2, 3, 4, 5))
    b = to_namedtuple(a)
    b[0] = 9
    assert a[0] != 9

    d = {'a': 1, 'b': 2}
    b = to_namedtuple(d)
    assert b.a == 1

    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    b = to_namedtuple(d)
    assert b.a == 1

    from flutils.miscutils import SimpleNamespace
    a = SimpleNamespace()
    a.a = 1
    a

# Generated at 2022-06-13 20:33:19.803750
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert callable(to_namedtuple)
    assert (
        repr(to_namedtuple) ==
        '<function to_namedtuple at 0x{:08x}>'.format(id(to_namedtuple))
    )


# Generated at 2022-06-13 20:33:27.291381
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict

    obj = {'a': 1, 'b': 2}
    nt = to_namedtuple(obj)
    assert nt.a == 1
    assert nt.b == 2

    obj = {2: 3}
    nt = to_namedtuple(obj)
    assert nt == ()

    obj = {'a': 1, 'b_2': 2, '_c': 3}
    nt = to_namedtuple(obj)
    assert nt.a == 1
    assert nt.b_2 == 2
    assert not hasattr(nt, '_c')

    obj = {'c': 3, 'a': 1, 'b': 2}
    nt = to_namedtuple(obj)
    assert nt.c == 3
    assert nt

# Generated at 2022-06-13 20:33:32.838152
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Setup
    dic: dict = {
        '_p': 1,
        'a': {
            'ab': {'a': 1, 'b': 2},
            'ac': 1,
            'ad': 1,
        },
        'b': {'b': 1, 'c': 1},
        'c': 1,
        'd': 1,
    }

    # Execute
    value = to_namedtuple(dic)

    # Test assert
    assert value.a.ab.a == 1


# Execute unit test
if __name__ == '__main__':
    from flutils.namedtupleutils import to_namedtuple
    test_to_namedtuple()

# Generated at 2022-06-13 20:33:44.772716
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: () -> None
    from flutils.namedtupleutils import to_namedtuple
    from collections import (
        OrderedDict,
        namedtuple,
    )
    from types import SimpleNamespace

    # test that a None value is not acceptable
    try:
        print(to_namedtuple(None))
    except TypeError as err:
        assert str(err) == (
            "Can convert only 'list', 'tuple', 'dict' to a NamedTuple; "
            "got: (NoneType) None"
        )
    else:
        raise AssertionError("Did not raise TypeError.")

    # test that a string is not acceptable

# Generated at 2022-06-13 20:33:58.164501
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # fmt: off
    dic = {
        'a': 1,
        'b': 2,
    }
    odic = OrderedDict((
        ('a', 1),
        ('b', 2),
    ))
    tup = (
        1,
        2,
    )
    lis = [
        1,
        2,
    ]
    snsp = SimpleNamespace(a=1, b=2)
    t = namedtuple('NamedTuple', 'a b')
    # fmt: on
    # fmt: off

# Generated at 2022-06-13 20:34:04.419340
# Unit test for function to_namedtuple
def test_to_namedtuple():
    test_obj = [
        {'a': 11, 'b': 12},
        [{'a': 21, 'b': 22}],
        [[{'a': 31, 'b': 32}]],
        [[[[
            {'a': 41, 'b': 42}
        ]]]],
        {
            'a': {'a': 51, 'b': 52},
            'b': [{'a': 61, 'b': 62}]
        },
    ]  # type: List[Mapping]

# Generated at 2022-06-13 20:34:15.685935
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    from types import SimpleNamespace

    d = {'a': 1, 'b': 2, 'c': 3}
    dt_noduplicate = to_namedtuple(d)
    dt_duplicate = to_namedtuple(d)
    assert dt_noduplicate == dt_duplicate
    assert dt_noduplicate[0] == 1
    assert dt_noduplicate.a == 1
    assert dt_noduplicate.b == 2
    assert dt_noduplicate.c == 3

    d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    dt = to_

# Generated at 2022-06-13 20:34:24.854408
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple
    """

    # Setup
    from copy import copy, deepcopy
    from flutils.datadir import copy_template_dir
    import sys
    import builtins
    import json
    import pytest
    builtins.__dict__['__name__'] = '__main__'

    # Unit under test
    from flutils.namedtupleutils import (
        to_namedtuple
    )

    # Make a copy of flutils and navigate to the test directory
    dir1 = copy_template_dir(
        'testcopy_to_namedtuple', 'test_namedtupleutils',
        'test_to_namedtuple'
    )
    sys.path.insert(0, dir1)

    # Test the function
    def test_list():
        in1: List