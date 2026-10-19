

# Generated at 2022-06-13 20:32:53.803819
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == ()
    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple([[]]) == [NamedTuple()]
    assert to_namedtuple([[[]]]) == [NamedTuple(NamedTuple())]
    assert to_namedtuple([[[[]]]]) == [NamedTuple(NamedTuple(NamedTuple()))]
    assert to_namedtuple([{}]) == [NamedTuple()]
    assert to_namedtuple([[[]]]) == [NamedTuple(NamedTuple())]
    assert to_namedtuple([[[[]]]]) == [NamedTuple(NamedTuple(NamedTuple()))]
    assert to_

# Generated at 2022-06-13 20:33:05.061902
# Unit test for function to_namedtuple
def test_to_namedtuple():

    def assert_object_eq(obj):
        class ObjectWrapper:
            def __init__(self, obj):
                self.obj = obj

            def __eq__(self, other):
                if isinstance(other, ObjectWrapper):
                    return other.obj is self.obj
                return False

            def __repr__(self):
                return repr(self.obj)

        objw = ObjectWrapper(obj)
        out = to_namedtuple(objw)
        assert obj is out

    def _test(obj, expected):
        out = to_namedtuple(obj)
        assert expected == out

        for item in obj:
            if isinstance(item, (list, tuple)):
                _test(item, to_namedtuple(item))

    # namedtuple

# Generated at 2022-06-13 20:33:14.026072
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    dic = {
        'a': 1,
        'b': 2,
    }
    res = to_namedtuple(dic)
    assert res
    assert isinstance(res, NamedTuple)
    assert res.a == 1
    assert res.b == 2
    dic.update({'c': 3})
    res = to_namedtuple(dic)
    assert res
    assert isinstance(res, NamedTuple)
    assert res.a == 1
    assert res.b == 2
    assert res.c == 3
    dic['_d'] = 4
    res = to_namedtuple(dic)
    assert res
    assert isinstance(res, NamedTuple)
    assert res.a == 1
    assert res.b == 2
    assert res

# Generated at 2022-06-13 20:33:20.161599
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    namedtup = to_namedtuple(dic)
    assert namedtup.a == 1
    assert namedtup.b == 2


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:33:27.682350
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.namedtupleutils import to_namedtuple
    from flutils.collections import as_nested_dict
    from flutils.convertutils import to_dict
    import collections as _c

    seq = ['a', 1, 'b']
    exp = ('a', 1, 'b')
    obs = to_namedtuple(seq)
    assert isinstance(obs, _c.namedtuple)
    assert obs._fields == ('item0', 'item1', 'item2')
    assert obs == exp

    seq = ('a', 1, 'b')
    exp = ('a', 1, 'b')
    obs = to_namedtuple(seq)
    assert isinstance(obs, _c.namedtuple)

# Generated at 2022-06-13 20:33:31.426530
# Unit test for function to_namedtuple
def test_to_namedtuple():
    try:
        dic = {'a': 1, 'b': 2}
        named_tuple = to_namedtuple(dic)
    except Exception as e:
        print("Test failed!")
        print(e)
        return
    ret = named_tuple == dic
    if ret:
        print("Test passed!")
    else:
        print("Test failed!")


if __name__ == "__main__":
    test_to_namedtuple()

# Generated at 2022-06-13 20:33:43.841922
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    d = dict(a=1, b=2)
    assert to_namedtuple(d) == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    d = dict(a=1, b=2, c=None)
    assert to_namedtuple(d) == namedtuple('NamedTuple', 'a b c')(a=1, b=2, c=None)

    d = {'a': 1, 'b': 2, 'c': 3}
    od = OrderedDict(d)
    assert to_namedtuple(od) == namedtuple('NamedTuple', 'a b c')(a=1, b=2, c=3)

    d = SimpleNamespace(a=1, b=2, c=3)

# Generated at 2022-06-13 20:33:50.568486
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple"""
    from flutils.namedtupleutils import to_namedtuple
    obj = [1, 2, 3]
    assert obj == to_namedtuple(obj)

    obj = [1, (2, 3, 4), 5]

# Generated at 2022-06-13 20:34:00.543611
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)
    out = to_namedtuple(('a', 'b', 'c'))
    assert isinstance(out, NamedTuple)
    dic = OrderedDict((('c', 1), ('b', 2), ('a', 3)))
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)
    out = to_namedtuple([dic] * 3)
    assert isinstance(out, list)
    assert isinstance(out[0], NamedTuple)
    assert isinstance(out[1], NamedTuple)
    assert isinstance(out[2], NamedTuple)

# Generated at 2022-06-13 20:34:11.929637
# Unit test for function to_namedtuple
def test_to_namedtuple():
    lst = [0, 1, 2, 3]
    answer = to_namedtuple(lst)
    expected = [0, 1, 2, 3]
    assert answer == expected

    lst = ['0', '1', '2', '3']
    answer = to_namedtuple(lst)
    expected = ['0', '1', '2', '3']
    assert answer == expected


    tup = (0, 1, 2, 3)
    tup_namedtuple = namedtuple('tuple', ['0', '1', '2', '3'])
    expected = tup_namedtuple(0, 1, 2, 3)
    answer = to_namedtuple(tup)
    assert answer == expected

    tup = ('0', '1', '2', '3')
    expected

# Generated at 2022-06-13 20:34:24.938208
# Unit test for function to_namedtuple
def test_to_namedtuple():
    out = to_namedtuple({'a': 1, 'b': (1, '2', 3)})
    assert out.a == 1
    assert out.b[0] == 1
    assert out.b[1] == '2'
    assert out.b[2] == 3

    out = to_namedtuple({'a': OrderedDict({'a': 1, 'b': 2}), 'b': {'c': 3}})
    assert out.a.a == 1
    assert out.a.b == 2
    assert out.b.c == 3

    out = to_namedtuple(OrderedDict({'b': 10, 'a': 20}))
    assert out.a == 20
    assert out.b == 10


# Generated at 2022-06-13 20:34:37.061344
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(SimpleNamespace(a=1, b=2))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(dict(a=1, b=2))
    assert to_namedtuple([{'a': 1, 'b': 2}])[0] == to_namedtuple(dict(a=1, b=2))

# Generated at 2022-06-13 20:34:48.325931
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.namedtupleutils import _to_namedtuple
    from argparse import Namespace

    # Test with a sequence (tuple)
    tup = (1, 2, 3)
    out = to_namedtuple(tup)
    assert isinstance(out, tuple)
    assert out == tup

    # Test with a sequence (list)
    lis = list(tup)
    out = to_namedtuple(lis)
    assert isinstance(out, list)
    assert out == lis

    # Test with a dictionary
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)

# Generated at 2022-06-13 20:34:57.684519
# Unit test for function to_namedtuple
def test_to_namedtuple():
    class A(object):
        def __init__(self, x: int) -> None:
            self.a = x

    dic = dict(a=1, b=2)
    lis = list(dic.items())
    tup = tuple(dic.items())
    lis_as_seq = [lis, lis, lis]
    tup_as_seq = tuple(dic.items())
    lis_as_seq.append(tup)
    lis_as_seq.append(lis)
    lis_as_seq.append(tup)
    lis_as_seq.append(tup_as_seq)
    lis_as_seq.append(lis)
    lis_as_seq.append(5.5)
    lis_as_seq.append

# Generated at 2022-06-13 20:35:11.994236
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Test expected behaviors (happy path)
    dic = {
        'a': 1,
        'b': 2,
        'c': {
            'd': 3,
            'e': 4,
        },
    }
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    assert out.c.d == 3
    assert out.c.e == 4

    l: List[Dict] = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    out = to_namedtuple(l)
    assert isinstance(out, list)
    assert len(out) == 2
    assert isinstance(out[0], NamedTuple)
    assert isinstance(out[1], NamedTuple)
   

# Generated at 2022-06-13 20:35:24.136772
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple()."""
    with pytest.raises(TypeError):
        to_namedtuple(1)
    with pytest.raises(TypeError):
        to_namedtuple(1.1)
    with pytest.raises(TypeError):
        to_namedtuple(True)
    assert to_namedtuple(None) is None

    # noinspection PyTypeChecker
    dic: dict = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)
    # noinspection PyTypeChecker
    dic: dict = {'a': 1, 'b': {'x': 1, 'y': 2}}
    assert to_namedtuple(dic) == Named

# Generated at 2022-06-13 20:35:34.830038
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace

    dic = {'a': 1, 'b': 2}
    ntpl = to_namedtuple(dic)
    assert ntpl.a == 1
    assert ntpl.b == 2

    dic = OrderedDict([('a', 1), ('b', 2)])
    ntpl = to_namedtuple(dic)
    assert ntpl.a == 1
    assert ntpl.b == 2

    tpl = ('a', 'b')
    ntpl = to_namedtuple(tpl)
    assert ntpl.a == 'a'
    assert ntpl.b == 'b'

    nsp = SimpleNamespace(a=1, b=2)
    ntpl = to_named

# Generated at 2022-06-13 20:35:44.828324
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert (
        to_namedtuple({
            'a': 'b',
            'c': 'd',
        }) ==
        NamedTuple(a='b', c='d')
    )
    assert (
        to_namedtuple({
            'a': 'b',
            'c': {'d': 'e'},
        }) ==
        NamedTuple(a='b', c=NamedTuple(d='e'))
    )

# Generated at 2022-06-13 20:35:53.512110
# Unit test for function to_namedtuple
def test_to_namedtuple():
    lis = [{'a': 1, 'b': 2}]
    print(to_namedtuple(lis))
    dic = {'a': 1, 'b': 2}
    print(to_namedtuple(dic))
    dic = OrderedDict(a=1, b=2)
    print(to_namedtuple(dic))
    tup = (1, 2)
    print(to_namedtuple(tup))
    tup = (1, 2, dic)
    print(to_namedtuple(tup))
    ns = SimpleNamespace(**dic)
    print(to_namedtuple(ns))
    nt = namedtuple('NamedTuple', 'a,b')(1, 2)
    print(to_namedtuple(nt))


# Generated at 2022-06-13 20:36:03.339667
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Empty tuples
    obj = ()
    assert to_namedtuple(obj) == ()
    assert not isinstance(to_namedtuple(obj), tuple)

    # Empty list
    obj = []
    assert to_namedtuple(obj) == []
    assert not isinstance(to_namedtuple(obj), list)

    # Lists
    obj = [1, 2]
    assert to_namedtuple(obj) == [1, 2]
    assert not isinstance(to_namedtuple(obj), list)

    # Tuples
    obj = (1, 2)
    assert to_namedtuple(obj) == (1, 2)
    assert not isinstance(to_namedtuple(obj), tuple)

    # Dict
    obj = {'a': 1, 'b': 2}
    assert to

# Generated at 2022-06-13 20:36:18.936525
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection SpellCheckingInspection
    """Unit testing for function to_namedtuple.

    Testing includes both positive and negative tests.

    Example:
        >>> from flutils.namedtupleutils import to_namedtuple
        >>> obj = {'a': {'a': 1, 'b': 2}, 'b': 2}
        >>> result = to_namedtuple(obj)
        >>> result
        NamedTuple(a=NamedTuple(a=1, b=2), b=2)
        >>> result.a
        NamedTuple(a=1, b=2)
        >>> result.a.a
        1
        >>> result.a.b
        2
        >>> result.b
        2
     """
    obj = {'a': {'a': 1, 'b': 2}, 'b': 2}

# Generated at 2022-06-13 20:36:21.324217
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test case for function to_namedtuple.
    """
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:36:32.447998
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit tests for function :func:`to_namedtuple`."""
    from collections import (
        OrderedDict,
    )
    from typing import (
        List,
        Tuple,
        Union,
    )


# Generated at 2022-06-13 20:36:43.137427
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple as convert
    from collections import OrderedDict, namedtuple
    from typing import (
        List,
        Tuple,
        Union,
    )
    from types import SimpleNamespace

    dic = OrderedDict(
        (
            (
                'a', 1
            ),
            (
                'b', 2
            ),
            (
                'c', [
                    {
                        'd': 1,
                        'e': 2,
                    },
                    {
                        'd': 3,
                        'e': 4,
                    },
                ]
            ),
        )
    )
    nt: namedtuple = convert(dic)
    assert nt.a == 1
    assert nt.b == 2

# Generated at 2022-06-13 20:36:53.434244
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifier

    dic = {'a': 1, 'b': 2}
    nt: namedtuple = to_namedtuple(dic)
    assert isinstance(nt, namedtuple)
    assert isinstance(nt, (namedtuple, tuple))
    assert isinstance(nt, (namedtuple, tuple, list))
    assert issubclass(nt.__class__, namedtuple)
    assert issubclass(nt.__class__, (namedtuple, tuple))
    nt2 = nt.replace(b=3)
    assert nt2.a == 1
    assert nt2.b == 3
    assert n

# Generated at 2022-06-13 20:37:02.711350
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == ()
    assert to_namedtuple({}) == ()
    assert to_namedtuple([{}]) == [()]
    assert to_namedtuple([{'a': 1}, {'b': 2}]) == [NamedTuple(a=1), NamedTuple(b=2)]
    with pytest.raises(TypeError):
        to_namedtuple(None)
    with pytest.raises(TypeError):
        to_namedtuple(1)
    with pytest.raises(TypeError):
        to_namedtuple('a')

# Generated at 2022-06-13 20:37:14.362182
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    # use flutils.namedtupleutils.to_namedtuple in this file, not the function name
    from flutils.namedtupleutils import to_namedtuple

    # Not start, call to_namedtuple with invalid type
    with pytest.raises(TypeError):
        to_namedtuple('foo')

    # Not start, call convert with invalid type
    with pytest.raises(TypeError):
        _to_namedtuple('foo')

    # Start, call to_namedtuple with invalid type
    with pytest.raises(TypeError):
        to_namedtuple('foo', _started=True)

    # Start, call convert with invalid type
    with pytest.raises(TypeError):
        _to_namedtuple('foo', _started=True)

    # Start

# Generated at 2022-06-13 20:37:22.735738
# Unit test for function to_namedtuple
def test_to_namedtuple():
    class cls:
        pass


# Generated at 2022-06-13 20:37:33.708185
# Unit test for function to_namedtuple
def test_to_namedtuple():
    '''
    Unit test for to_namedtuple
    '''

    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    assert to_namedtuple({'b': 1, 'a': 2}) == namedtuple('NamedTuple', ['a', 'b'])(2, 1)
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 10}) == namedtuple('NamedTuple', ['a', 'b', 'c'])(1, 2, 10)

    assert to_namedtuple({'a': 1, 'b': 2, '_c': 20}) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    assert to_named

# Generated at 2022-06-13 20:37:47.265894
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from flutils.namedtupleutils import to_namedtuple
    from types import SimpleNamespace

    #  Test to_namedtuple:  type mismatch
    from flutils.misc import TestClass, TestException
    class TestClass2(TestClass):
        @staticmethod
        def to_namedtuple(obj: Any, *args, **kwargs) -> Any:
            return to_namedtuple(obj, *args, **kwargs)
    test = TestClass2()

    test.set_doc(to_namedtuple)
    test.set_func(TestClass2.to_namedtuple)
    test.set_valid_types(dict)
    test.set_valid_examples({'foo': 0})

# Generated at 2022-06-13 20:38:03.662969
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyPackageRequirements
    import pytest
    from flutils.namedtupleutils import to_namedtuple

    mylist = [1, 2, 3]
    mylist_changed = to_namedtuple(mylist)
    assert mylist_changed == [1, 2, 3]
    assert mylist_changed is not mylist
    mylist = ['a', 'b', 'c']
    mylist_changed = to_namedtuple(mylist)
    assert mylist_changed == ['a', 'b', 'c']
    assert mylist_changed is not mylist
    mylist = [1, 2, {'a': 1, 'b': 2}]
    mylist_changed = to_namedtuple(mylist)

# Generated at 2022-06-13 20:38:07.192256
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d = {'a': 1, 'b': 2}
    try:
        to_namedtuple(d)
    except Exception as e:
        raise e


# Generated at 2022-06-13 20:38:14.201108
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == ()
    assert to_namedtuple({"a": 1, "b": 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict(a=1, b=2)) == NamedTuple(a=1, b=2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == NamedTuple(a=1, b=2)
    assert to_namedtuple(({"a": 1, "b": 2}, 1, 2)) == (NamedTuple(a=1, b=2), 1, 2)

# Generated at 2022-06-13 20:38:22.816089
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import Optional
    from collections import namedtuple

    TestData = namedtuple('TestData', 'key')


# Generated at 2022-06-13 20:38:36.985523
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
        namedtuple,
    )
    from flutils.namedtupleutils import traverse

    obj = {'a': 1, 'b': 2}
    res = to_namedtuple(obj)
    assert isinstance(res, namedtuple)
    assert tuple(traverse(res)) == (2, 1)

    obj = {'a': 1, 'b': [2, 3]}
    res = to_namedtuple(obj)
    assert isinstance(res.b, list)
    assert tuple(traverse(res)) == (3, 2, 1)

    obj = OrderedDict([('a', 1), ('b', 2)])
    res = to_namedtuple(obj)
    assert isinstance(res, namedtuple)

# Generated at 2022-06-13 20:38:49.685585
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple((1, 2)) == (1, 2)
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, '': 2}) == NamedTuple(a=1)
    assert to_namedtuple({'a': 1, 'b': 2, 'c': [3, 4]}) \
        == NamedTuple(a=1, b=2, c=(3, 4))

# Generated at 2022-06-13 20:39:01.586900
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': {'A': [{'One': 1}, {'Two': 2}], 'B': [{'Three': 3, 'Four': 4}, {'Five': 5}]}, 'b': {'C': [{'Six': 6, 'Seven': 7}], 'D': [{'Eight': 8}]}}
    t = to_namedtuple(dic)
    assert t == NamedTuple(a=NamedTuple(A=[NamedTuple(One=1), NamedTuple(Two=2)], B=[NamedTuple(Three=3, Four=4), NamedTuple(Five=5)]), b=NamedTuple(C=[NamedTuple(Six=6, Seven=7)], D=[NamedTuple(Eight=8)]))

# Generated at 2022-06-13 20:39:12.340253
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest.mock import MagicMock
    from flutils.namedtupleutils import to_namedtuple

    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert isinstance(nt, namedtuple('NamedTuple', 'a b'))
    assert nt.a == 1
    assert nt.b == 2

    nt_dict = nt._asdict()
    assert isinstance(nt_dict, dict)
    assert nt_dict['a'] == 1
    assert nt_dict['b'] == 2

    nt_tuple = nt._asdict()
    assert isinstance(nt_tuple, tuple)
    assert nt_tuple[0] == 1

# Generated at 2022-06-13 20:39:25.265951
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': NamedTuple(c=2, d=3)}) == NamedTuple(a=1, b=NamedTuple(c=2, d=3))
    assert to_namedtuple(OrderedDict([('a', 1), ('b', NamedTuple(c=2, d=3))])) == NamedTuple(a=1, b=NamedTuple(c=2, d=3))

# Generated at 2022-06-13 20:39:39.346727
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from pprint import pprint
    from operator import attrgetter

    class Test1(NamedTuple):
        a: str
        b: int
        _c: str


# Generated at 2022-06-13 20:39:59.319777
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(1) == 1



# Generated at 2022-06-13 20:40:08.988727
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple((1, 2)) == (1, 2)
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple({'a': 1}) == NamedTuple(a=1)
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'b': 2, 'a': 1}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({1: 2}) == NamedTuple(_1=2)
    assert to_namedtuple({1: 2, 3: 4}) == NamedTuple(_1=2, _3=4)
    assert to_named

# Generated at 2022-06-13 20:40:19.788714
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Test simple NamedTuple
    nt_def = namedtuple('Test', 'a b')
    nt = nt_def(0, 1)
    assert nt == to_namedtuple(nt)

    # Test a Mapping (dict)
    nt_def = namedtuple('Test', 'a b')
    expected: NamedTuple = nt_def(0, 1)
    d = {'a': 0, 'b': 1}
    assert expected == to_namedtuple(d)

    # Test a Mapping (dict) with invalid identifier
    d = {'a': 0, 'b': 1, 'c/d': 2}
    expected = expected._replace(c_d=2)
    assert expected == to_namedtuple(d)

    # Test a Mapping (dict) with invalid identifier

# Generated at 2022-06-13 20:40:27.129997
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest


    class TestToNamedTuple(unittest.TestCase):

        def test_dict_to_namedtuple(self):
            from collections import OrderedDict
            from flutils.namedtupleutils import to_namedtuple

            dic = {'a': 1, 'b': 2}
            result = to_namedtuple(dic)
            self.assertEqual(result.a, 1)
            self.assertEqual(result.b, 2)

            dic = {'a': 1, 'b': 2}
            result = to_namedtuple(dic)
            expected = 'NamedTuple(a=1, b=2)'
            self.assertEqual(result.__repr__(), expected)


# Generated at 2022-06-13 20:40:28.657347
# Unit test for function to_namedtuple
def test_to_namedtuple():
    #  obj: _AllowedTypes
    #  assert to_namedtuple(obj) == False
    assert False

# Generated at 2022-06-13 20:40:34.950552
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # Test for function _to_namedtuple
    def _test_to_namedtuple(
            obj: Any,
            expected: Any,
            expected_exception: Optional[Exception] = None
    ):
        # Test the output of the function with a valid object
        if expected_exception is None:
            res = _to_namedtuple(obj)
            try:
                assert res == expected
            except AssertionError:
                print(obj)
                print()
                print(res)
                print()
                print(expected)
                print()
                raise
        # Test the output of the function with an invalid object
        else:
            with pytest.raises(expected_exception):
                _to_namedtuple(obj)


# Generated at 2022-06-13 20:40:45.286248
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    dic = {
        'a': 1,
        'b': 2,
        '_c': 3,
    }

    nt = to_namedtuple(dic)
    assert hasattr(nt, 'a')
    assert nt.a == 1
    assert hasattr(nt, 'b')
    assert nt.b == 2
    assert not hasattr(nt, '_c')
    assert not hasattr(nt, 'c')

    nt = to_namedtuple([1, 2, 3])
    assert isinstance(nt, list)
    assert nt == [1, 2, 3]
    nt[1] = 'two'
    assert nt == [1, 'two', 3]

    class Obj:
        def __init__(self) -> None:
            self

# Generated at 2022-06-13 20:40:57.056429
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({"a": 1}) == namedtuple('NamedTuple', 'a')(a=1)
    assert to_namedtuple({"a": 1, "b": 2}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple({"a": 1, "b": 2, "c": 3}) == namedtuple('NamedTuple', 'a b c')(a=1, b=2, c=3)

    assert to_namedtuple([{}, {"x": "y"}]) == [namedtuple('NamedTuple', '')(), namedtuple('NamedTuple', 'x')(x="y")]
    assert to_namedtuple((1, 2, {"a": 1, "b": 2}))

# Generated at 2022-06-13 20:41:08.996512
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    dic = {'a': {'b': 1, 'c': 2}, 'd': 3, 'e':4}
    expected = namedtuple('NamedTuple', ('a', 'd', 'e'))(
        a=namedtuple('NamedTuple', ('b', 'c'))(b=1, c=2),
        d=3,
        e=4,
    )
    actual = to_namedtuple(dic)
    assert actual == expected

    dic = {'a': 'foo', 'b': 1, 'c': {'d': 'bar'}}

# Generated at 2022-06-13 20:41:18.048991
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pprint
    import unittest

    Suite = unittest.TestSuite()

    class ListTestCase(unittest.TestCase):
        def test_NamedTuple(self):
            obj = [{'a': 1}, {'b': 2}]
            expected = [NamedTuple(a=1), NamedTuple(b=2)]
            converted = to_namedtuple(obj)
            self.assertIsInstance(converted, list)
            self.assertEqual(converted, expected)

        def test_NamedTuple_Nested(self):
            obj = [{'a': [{'nested': 1}, {'nested': 2}]}]

# Generated at 2022-06-13 20:42:01.546181
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

# Generated at 2022-06-13 20:42:12.719966
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2}
    _ = to_namedtuple(obj)
    assert _.a == 1
    assert _.b == 2
    obj = [
        {'a': 1, 'b': [1, 2, 3]},
        {'c': 1, 'd': 2},
    ]
    _ = to_namedtuple(obj)
    assert _[0].a == 1
    assert _[0].b == (1, 2, 3)
    assert _[1].c == 1
    assert _[1].d == 2
    _ = to_namedtuple(tuple(obj))
    assert _[0].a == 1
    assert _[0].b == (1, 2, 3)
    assert _[1].c == 1
    assert _[1].d

# Generated at 2022-06-13 20:42:23.970745
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    dic: dict = {
        '_a': 'apple',
        '_b': 'bear',
        'a': 'ant',
        'bee': 'b',
        'c': 'cat',
        'd': 'duck',
    }
    assert to_namedtuple(dic) == ('ant', 'bee', 'cat', 'duck')

    ord_dic: OrderedDict = OrderedDict(
        [
            ('apple', 'a'),
            ('bear', 'b'),
            ('_c', 'cat'),
            ('_d', 'dog'),
        ]
    )
    assert to_namedtuple(ord_dic) == ('a', 'b')

    # noinspection PyTypeChecker

# Generated at 2022-06-13 20:42:31.489279
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)
    dic = {'a': NamedTuple(x=1)}
    assert to_namedtuple(dic) == NamedTuple(a=NamedTuple(x=1))
    dic = OrderedDict({'a': 1, 'b': 2})
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': [1, 2]}) == NamedTuple(a=[1, 2])
    assert to_namedtuple({'a': 1, 'b': 2, 'c': []}) == NamedTuple(a=1, b=2, c=[])

# Generated at 2022-06-13 20:42:41.365407
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict
    )
    from flutils.namedtupleutils import to_namedtuple
    from typing import (
        Any,
        List,
        NamedTuple,
    )

    def test_one_nested_level(orig: object) -> None:
        conver: Any
        try:
            conver = to_namedtuple(orig)
        except TypeError:
            return
        assert isinstance(conver, List)
        assert len(conver) == 3
        assert conver[0] == 'a'
        assert conver[1] == 1
        assert isinstance(conver[2], NamedTuple)
        assert conver[2].a == 4
        assert conver[2].b == 5
        assert conver[2].c == 6
