

# Generated at 2022-06-13 20:32:44.815681
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
    )
    from functools import partial, reduce
    from functools import singledispatch
    import operator
    from types import SimpleNamespace
    from unittest import TestCase
    from unittest.mock import MagicMock

    from flutils.namedtupleutils import to_namedtuple
    from flutils.typingutils import make_func_with_new_type_info
    from flutils.validators import validate_identifier

    make_to_namedtuple = make_func_with_new_type_info(to_namedtuple)


# Generated at 2022-06-13 20:32:54.643401
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    import copy
    d = {
        'a': 1,
        'b': '2',
        'c': {'c1': 1, 'c2': '2'},
        'd': [1, '2'],
        'e': {
            'f': {
                'g': {
                    'h': {
                        'i': 'j',
                        'k': [1, 2, {'l': 'm'}]
                    }
                }
            }
        }
    }

    nt_d = to_namedtuple(d)
    assert nt_d.a == 1
    assert nt_d.b == '2'
    assert nt_d.c.c1 == 1
    assert nt_d.c.c2 == '2'

# Generated at 2022-06-13 20:33:05.413167
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace

    from pytest import raises

    from flutils.namedtupleutils import to_namedtuple

    # Test a dictionary
    exp = OrderedDict((('a', 1), ('b', 2)))
    exp_out = SimpleNamespace(a=1, b=2)
    out = to_namedtuple(exp)
    assert out == exp_out

    exp2 = OrderedDict((('a', 1), ('b', 2), ('c', 3)))
    exp2_out = SimpleNamespace(a=1, b=2, c=3)
    out2 = to_namedtuple(exp2)
    assert out2 == exp2_out

    # Test a SimpleNamespace

# Generated at 2022-06-13 20:33:12.159079
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Arrange
    from collections import namedtuple

    MyTuple = namedtuple('MyTuple', 'x y z')
    lst = [{'a': 1, 'b': 2}, {'x': 11, 'y': 12, 'z': 13}]
    # Act
    actual = to_namedtuple(lst)
    # Assert
    assert isinstance(actual, list)
    assert all([
        (isinstance(i, dict) or isinstance(i, MyTuple))
        for i in actual
    ])

# Generated at 2022-06-13 20:33:23.925321
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert isinstance(nt, NamedTuple)
    assert nt == {'a': 1, 'b': 2}
    assert nt.a == 1
    assert nt.b == 2
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    nt.a += 1
    nt.b += 1
    assert nt == {'a': 2, 'b': 3}
    assert nt.a == 2
    assert nt.b == 3
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)

# Generated at 2022-06-13 20:33:35.656607
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict

    assert to_namedtuple({'a': 1, 'b': 2}) == \
        namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)

    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == \
        namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)

    assert to_namedtuple(OrderedDict([('b', 2), ('a', 1)])) == \
        namedtuple('NamedTuple', ('b', 'a'))(b=2, a=1)

    assert to_namedtuple([1, 2]) == [1, 2]

# Generated at 2022-06-13 20:33:46.477377
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic = {'a': {'a': 1, 'b': 2}}
    assert to_namedtuple(dic) == NamedTuple(a=NamedTuple(a=1, b=2))

    dic = {'a': 1, 'b': 2, 'c': {'a': 1, 'b': 2}}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2, c=NamedTuple(a=1, b=2))

    dic = OrderedDict([('c', 1), ('a', 2), ('b', 3)])

# Generated at 2022-06-13 20:33:59.046330
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # same as list
    d = {'a': 1, 'b': 2}
    out = to_namedtuple(d)
    wanted = namedtuple('wanted', 'a b')(1, 2)
    assert out == wanted

    # same as tuple
    d = {'a': 1, 'b': 2}
    out = to_namedtuple(tuple(d))
    wanted = namedtuple('wanted', 'a b')(1, 2)
    assert out == wanted

    # same as list of dicts
    dic = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
    out = to_namedtuple(dic)

# Generated at 2022-06-13 20:34:10.716385
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import NamedTuple

    dic = {
        'foo': 1,
        'bar': 2,
        'baz': {
            'a': 1,
            'b': 2,
        },
        'qux': [
            1, 2,
        ],
    }

    nt: NamedTuple = to_namedtuple(dic)

    assert hasattr(nt, 'foo'), "Attribute 'foo' is missing"
    assert hasattr(nt, 'bar'), "Attribute 'bar' is missing"
    assert hasattr(nt, 'baz'), "Attribute 'baz' is missing"
    assert hasattr(nt, 'qux'), "Attribute 'qux' is missing"
    assert nt.foo == 1, "Attribute 'foo' does not match the given"

# Generated at 2022-06-13 20:34:17.704163
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.namedtupleutils import to_namedtuple
    namespace = SimpleNamespace
    NamedTuple = namedtuple

    assert to_namedtuple('a') == 'a'
    assert to_namedtuple('') == ''
    assert to_namedtuple(None) is None
    assert to_namedtuple(3) == 3
    assert to_namedtuple(3.14) == 3.14
    assert to_namedtuple({}) == NamedTuple('NamedTuple')
    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == tuple()
    assert to_namedtuple(namespace()) == NamedTuple('NamedTuple')


# Generated at 2022-06-13 20:34:28.971291
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import json
    import pprint
    import unittest
    import sys

    class TestToNamedTuple(unittest.TestCase):
        """Unit test for function to_namedtuple."""

        maxDiff = None

        def test_given_list_with_list_str_tuple_dict_simple_namespace_named_tuple_return_list(self):
            """
            Tests that a list with other types is converted to a list of
            NamedTuple.
            """

# Generated at 2022-06-13 20:34:39.086107
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from collections import namedtuple

    test_obj = SimpleNamespace(
        a=1,
        b=2,
        c=3,
    )
    test_obj.a = SimpleNamespace(
        x=1,
        y=2,
        z=3,
    )

    named_tuple_1 = to_namedtuple(test_obj)
    expected_named_tuple_1 = namedtuple(
        'NamedTuple', ['a', 'b', 'c']
    )(a=namedtuple('NamedTuple', ['x', 'y', 'z'])(x=1, y=2, z=3), b=2, c=3)

# Generated at 2022-06-13 20:34:51.280238
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d = {'a': 1, 'b': 2, 'c': [3, 4]}
    result = to_namedtuple(d)
    assert hasattr(result, 'a')
    assert result.a == 1
    assert hasattr(result, 'b')
    assert result.b == 2
    assert hasattr(result, 'c')
    assert isinstance(result.c, list)
    assert len(result.c) == 2

    d2 = {'1': 2, 'd': 4, 'c': [{'e': 5}, {'f': 6}]}
    d.update(d2)
    result = to_namedtuple(d)
    assert hasattr(result, 'd')
    assert result.d == 4
    assert isinstance(result.c, list)

# Generated at 2022-06-13 20:35:03.575058
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    import typing as typ
    import pytest

    with pytest.raises(TypeError):
        to_namedtuple(5)
    assert to_namedtuple({}) == namedtuple('NamedTuple', '')()
    assert to_namedtuple({'a': 1}) == namedtuple('NamedTuple', ['a'])(a=1)
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple({'a': {'b': 1}}) == namedtuple('NamedTuple', ['a'])(a=namedtuple('NamedTuple', ['b'])(b=1))
   

# Generated at 2022-06-13 20:35:10.091136
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b == 2
    assert getattr(obj, 'a') == 1
    assert getattr(obj, 'b') == 2
    assert repr(obj) == repr(dic)


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:35:19.371140
# Unit test for function to_namedtuple
def test_to_namedtuple():

    d = {'a': 1, 'b': {'c': [1, 2, 3, {'d': 4}], 'e': 5}}
    nt = to_namedtuple(d)
    assert nt.a == 1
    assert isinstance(nt.b, namedtuple('ntb', 'c e'))
    assert nt.b.c == (1, 2, 3, (4,))
    assert nt.b.e == 5

    nt = to_namedtuple(OrderedDict(a=1, b=2, c=3))
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c == 3


# Generated at 2022-06-13 20:35:33.507895
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        'g': 1,
        '_f': 2,
        'h': 3,
        'd': {'j': 1, 'k': 2},
        'e': [1, 2, 3],
        'f': {'j': 1, 'k': 2, '_l': 3},
    }

    out = to_namedtuple(dic)
    assert out.d == (out.d.j, out.d.k)
    assert out.e == (1, 2, 3)
    assert out.f == (out.f.j, out.f.k)
    assert out.g == 1
    assert not hasattr(out, '_f')
    assert out.h == 3

    L = [dic, dic]
    out = to_namedtuple(L)

# Generated at 2022-06-13 20:35:39.513633
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    nt = to_namedtuple(d)
    assert isinstance(nt, NamedTuple)
    assert hasattr(nt, 'a')
    assert hasattr(nt, 'b')
    assert hasattr(nt, 'c')
    assert hasattr(nt, 'd')
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c == 3
    assert nt.d == 4


if __name__ == '__main__':
    import unittest
    unittest.main(module='test_namedtupleutils', exit=False, verbosity=2)

# Generated at 2022-06-13 20:35:51.216599
# Unit test for function to_namedtuple
def test_to_namedtuple():

    from collections import namedtuple
    from collections.abc import Mapping
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple

    dic = {'a': 1, 'b': 2}
    assert hasattr(dic, 'keys')
    assert dic.keys() == dict_keys(['a', 'b'])
    dic = dict(a=1, b=2)
    assert hasattr(dic, 'keys')
    assert dic.keys() == dict_keys(['a', 'b'])

    assert isinstance(dic, dict)
    assert isinstance(dic, Mapping)
    assert not isinstance(dic, list)
    assert not isinstance(dic, tuple)
    assert not isinstance(dic, str)

    assert hasattr

# Generated at 2022-06-13 20:36:02.447816
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.validators import validate_identifier
    assert to_namedtuple([]) == []
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    dic['c'] = 3
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b c')(a=1, b=2, c=3)
    assert to_namedtuple(OrderedDict(dic)) == namedtuple('NamedTuple', 'a b c')(a=1, b=2, c=3)

# Generated at 2022-06-13 20:36:17.420805
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """ Test to_namedtuple """
    import unittest
    import copy

    class TestToNamedTuple(unittest.TestCase):

        def setUp(self):
            self.obj = {'a': 1, 'b': 2}
            self.obj2 = {
                'a': 1, 'b': {
                    'c': 2, 'd': [{
                        'e': None, 'f': [1, 2, 3, None]
                    }]}
            }
            self.obj3 = OrderedDict([
                ('a', 1),
                ('b', 2),
            ])
            self.obj4 = OrderedDict([
                ('b', 2),
                ('a', 1),
            ])
            self.obj5 = SimpleNamespace(a=1, b=2)


# Generated at 2022-06-13 20:36:29.328933
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # -----------------------------
    # Example: to_namedtuple(dic)
    dic = {'a': 1, 'b': 2}
    out: NamedTuple = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    # -----------------------------
    # Example: to_namedtuple(tup)
    tup = (1, 2)
    out: Tuple = to_namedtuple(tup)
    assert out[0] == 1
    assert out[1] == 2
    # -----------------------------
    # Example: to_namedtuple(lst)
    lst = [1, 2]
    out = to_namedtuple(lst)  # type: ignore[list-item]
    assert out[0] == 1

# Generated at 2022-06-13 20:36:42.034185
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple({'b': 2, 'a': 1}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2, 'c': {'a': 1, 'b': 2}}) == to_namedtuple({'b': 2, 'a': 1, 'c': {'a': 1, 'b': 2}}) == NamedTuple(a=1, b=2, c=NamedTuple(a=1, b=2))

# Generated at 2022-06-13 20:36:51.885189
# Unit test for function to_namedtuple
def test_to_namedtuple():
    #noinspection SpellCheckingInspection
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert nt == namedtuple('NamedTuple', 'a b')(1, 2)
    seq = [dic, dic, dic]
    nt = to_namedtuple(seq)
    txt = ("[NamedTuple(a=1, b=2), NamedTuple(a=1, b=2), NamedTuple(a=1, "
           "b=2)]")
    assert str(nt) == txt

# Generated at 2022-06-13 20:36:58.200299
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.validators import validate_identifier, validate_dict
    from collections import OrderedDict


# Generated at 2022-06-13 20:37:09.731700
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    dict_obj = {'a': 1, 'b': 2, 'c': [3,4,5]}
    dic_namedtuple = to_namedtuple(dict_obj)
    assert dic_namedtuple.a == 1, "Named tuple keys are not set correctly"
    assert dic_namedtuple.b == 2, "Named tuple keys are not set correctly"

    list_obj = [1,2,3]
    list_namedtuple = to_namedtuple(list_obj)
    assert list_obj != list_namedtuple, "Named tuple should not be same as the original object"

    list_obj = [1,2,{'a': 3, 'b': 4}]
    list_namedtuple = to_namedtuple(list_obj)

# Generated at 2022-06-13 20:37:12.894535
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert(to_namedtuple(dic) == NamedTuple(a=1, b=2))

# Generated at 2022-06-13 20:37:21.809289
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.typingutils import is_namedtuple
    from flutils.jsonutils import to_json
    import pprint

    a = [1, {'b': 2, 'c': [{'d': 3}, {'e': 4}]}, 5]
    aa = to_namedtuple(a)
    print("a:\n%s" % pprint.pformat(a))
    print("aa:\n%s" % pprint.pformat(aa))
    print("is_namedtuple(aa):", is_namedtuple(aa))
    a = {"a": 1, "b": 2, "c": [{"d": 3}, {"e": 4}]}
    aa = to_namedtuple(a)
    print("a:\n%s" % pprint.pformat(a))
   

# Generated at 2022-06-13 20:37:32.765768
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:37:45.002200
# Unit test for function to_namedtuple
def test_to_namedtuple():
  import random
  dic = {'a': 1, 'b': 2}
  print(to_namedtuple(dic))
  a = list(range(10))
  print(to_namedtuple(a))
  t = (1, 2, 3, 4)
  print(to_namedtuple(t))
  b = (1, 2, 3, 4)
  print(to_namedtuple(b))
  random.seed(7)
  l = [[i, random.randint(0, 100)] for i in b]
  print(to_namedtuple(l))

# testing for coverage
if __name__ == '__main__':
  test_to_namedtuple()

# Generated at 2022-06-13 20:37:59.304619
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Basic unit test for function to_namedtuple."""
    from collections import OrderedDict
    from types import SimpleNamespace

    dic = {'a': 'a', 'b': 'b'}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple('NamedTuple', 'a b'))
    assert out.a == 'a'
    assert out.b == 'b'

    ordered_dict = OrderedDict([('a', 'a'), ('b', 'b')])
    out = to_namedtuple(ordered_dict)
    assert isinstance(out, namedtuple('NamedTuple', 'a b'))
    assert out.a == 'a'
    assert out.b == 'b'


# Generated at 2022-06-13 20:38:11.209317
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from typing import NamedTuple
    from datetime import datetime, date

    class basic(NamedTuple):
        a: int
        b: str

    class nest(NamedTuple):
        c: basic
        d: int

    class nest2(NamedTuple):
        c: nest
        d: int

    class nest3(NamedTuple):
        e: int
        f: float
        g: str

    class datetime_test(NamedTuple):
        a: str
        b: date
        c: datetime

    class datetime_test2(NamedTuple):
        a: date
        b: datetime
        c: str
        d: int

    class datetime_test3(NamedTuple):
        a: str

# Generated at 2022-06-13 20:38:14.109221
# Unit test for function to_namedtuple
def test_to_namedtuple():
    if __name__ == '__main__':
        import doctest
        doctest.testmod()

# Generated at 2022-06-13 20:38:22.798094
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert 1 == to_namedtuple(dic).a
    assert 2 == to_namedtuple(dic).b

    dic = {'a': 1, '_b': 2}
    assert 1 == to_namedtuple(dic).a
    assert hasattr(to_namedtuple(dic), '_b') is False

    dic = {1: 1, '_b': 2, 'c': 3}
    assert 1 == to_namedtuple(dic).c
    assert hasattr(to_namedtuple(dic), '_b') is False
    assert 3 == to_namedtuple(dic).c

    dic = {'a': 1, 'b': [1, 2, 3]}
    assert 1 == to_named

# Generated at 2022-06-13 20:38:36.987246
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from nptyping import NDArray
    from operator import add
    from stringcase import snakecase
    from typing import (
        Callable,
        Dict,
        NewType,
        Optional,
        Sequence,
        Tuple,
        Union,
    )

    OBJ1 = List[int]
    OBJ2 = Sequence[NDArray[float, ...]]

    OBJ3 = Dict[str, int]
    OBJ4 = NewType('OBJ4', Dict[str, str])
    OBJ5 = NewType('OBJ5', Dict[str, Callable[[], int]])

    OBJ6 = Tuple[int, str]
    OBJ7 = NewType('OBJ7', Tuple[str, float])

    OBJ8 = Tuple[int, Optional[str], float]
   

# Generated at 2022-06-13 20:38:49.685600
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    def _fmt(obj: Any):
        if hasattr(obj, "__dict__"):
            return repr(obj.__dict__)
        if isinstance(obj, (list, tuple)):
            return repr(obj)
        return str(obj)

    def _check(obj: Union[NamedTuple, Tuple, List], expected_out: str):
        out = to_namedtuple(obj)
        test_failed = False
        try:
            assert _fmt(out) == expected_out
        except AssertionError:
            test_failed = True
            print(
                "Expected: {}\n\nGot: {}".format(expected_out, _fmt(out))
            )


# Generated at 2022-06-13 20:39:01.891874
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from os import path
    from typing import Any, Dict, List, Optional
    from unittest.mock import Mock, call

    from _pytest.monkeypatch import MonkeyPatch
    from py._path.local import LocalPath
    from pytest import mark, raises
    from flutils.validators import ValidationError

    import flutils.namedtupleutils
    from flutils.namedtupleutils import (
        _to_namedtuple,
        to_namedtuple,
    )

    flutils.namedtupleutils.validate_identifier = (
        lambda *args, **kwargs:  # type: ignore[misc]
        True  # type: ignore[misc]
    )


# Generated at 2022-06-13 20:39:07.641908
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import (
        NamedTuple,
    )
    # noinspection PyUnresolvedReferences
    assert to_namedtuple(NamedTuple(a=1, b=2)) == NamedTuple(a=1, b=2)
    assert to_namedtuple(NamedTuple(a=1, b=2)) == NamedTuple(b=2, a=1)
    # noinspection PyUnresolvedReferences
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(b=2, a=1)
    assert to_namedtuple({'a': 1, 'b': 2}) != NamedTuple

# Generated at 2022-06-13 20:39:19.719349
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import json

    json_in = '''
    [
      {
        "a": 1,
        "b": {
          "c": 2
        }
      },
      3
    ]
    '''

    data: List[Any] = json.loads(json_in)
    new_data = to_namedtuple(data)
    assert isinstance(new_data, list)
    assert isinstance(new_data[0], NamedTuple)
    assert isinstance(new_data[-1], int)

    json_in = '''
    {
      "a": 1,
      "b": {
        "c": 2
      }
    }
    '''

    data = json.loads(json_in)
    new_data

# Generated at 2022-06-13 20:39:26.416345
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test the to_namedtuple function."""
    example_dict = {'a': 1, 'b': 2}
    namedtuple_dict = to_namedtuple(example_dict)
    assert type(namedtuple_dict).__name__ == "NamedTuple"
    assert namedtuple_dict.a == 1 and namedtuple_dict.b == 2

    example_list = [1, 2, '3', {'a': 1, 'b': 2}]
    namedtuple_list = to_namedtuple(example_list)
    assert type(namedtuple_list).__name__ == "list"
    assert namedtuple_list[0] == 1 and namedtuple_list[1] == 2 and namedtuple_list[2] == '3'

# Generated at 2022-06-13 20:39:42.273878
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import sys
    import unittest

    class TestToNamedTuple(unittest.TestCase):
        """Test the to_namedtuple function."""

        @staticmethod
        def _test(
                obj,
                expected,
        ):
            out = to_namedtuple(obj)
            assert out == expected, \
                '{} failed.' \
                '\n\t\tobj: {!r}' \
                '\n\t\texpected: {!r}' \
                '\n\t\tgot: {!r}'.format(
                    sys._getframe(1).f_code.co_name,
                    obj,
                    expected,
                    out
                )

        def test_empty_list(self):
            self._test([], [])


# Generated at 2022-06-13 20:39:53.761204
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a':1, 'b':2}) == to_namedtuple({'b':2, 'a':1})
    assert to_namedtuple({'a':1, 'b':2}) == to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))
    assert to_namedtuple({'a':1, 'b':2}) != to_namedtuple(OrderedDict([('b', 2), ('a', 1)]))

    # Test for functions like this
    def foo():
        return {'a': 1, 'b': 2}
    assert to_namedtuple(foo()) == NamedTuple(a=1, b=2)

    # Test for dict attributes too
    class Bar:
        def __init__(self):
            self.a = 1

# Generated at 2022-06-13 20:40:04.471550
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    # noinspection PyTypeChecker
    assert (to_namedtuple(dic) == (1, 2)) == True

    dic = {'a': 1, 'b': 2, 'c': 3}
    # noinspection PyTypeChecker
    assert to_namedtuple(dic) == (1, 2, 3)

    dic = {'a': 1, 'b': 2, 'd': 4}
    # noinspection PyTypeChecker
    assert to_namedtuple(dic) == (1, 2, 4)

    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # noinspection PyTypeChecker

# Generated at 2022-06-13 20:40:15.163459
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase
    from typing import Dict, List, Tuple

    class TestToNamedtuple(TestCase):
        """Unit test for function to_namedtuple."""


# Generated at 2022-06-13 20:40:25.196604
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test :func:`to_namedtuple <flutils.namedtupleutils.to_namedtuple>`."""
    from flutils.namedtupleutils import to_namedtuple

    # Positive tests
    assert to_namedtuple({}) == namedtuple('NamedTuple', '')(), \
        "Converting empty dictionary failed; got: (%r) %s" % (
            type(to_namedtuple({})).__name__, to_namedtuple({}),
        )

    out = to_namedtuple({'a': 1, 'b': 2})
    assert out.a == 1, \
        "Converting simple dictionary failed for key 'a'; got: %s" % out.a

# Generated at 2022-06-13 20:40:33.192686
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([{'a': 1, 'b': 2}])[0].a == 1
    assert to_namedtuple(OrderedDict([('b', 2), ('a', 1)]))[0].b == 2
    assert to_namedtuple(tuple([{'a': 1, 'b': 2}]))[0].a == 1
    assert to_namedtuple({'a': 1, 'b': 2}).a == 1
    assert to_namedtuple(SimpleNamespace(a=1, b=2)).b == 2

    dic = {'a': 1, 'b': 2}
    d1 = to_namedtuple(dic)
    d2 = to_namedtuple(dic)

    assert d1.a == 1
    assert d1.b == 2
   

# Generated at 2022-06-13 20:40:48.398520
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2, 'c_': 3, '__': 4}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2, 'c_': 3, '__': 4, '_': 5}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)


# Generated at 2022-06-13 20:40:55.362140
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple

    # Test Invalid Passed Type
    with pytest.raises(TypeError):
        to_namedtuple('string')

    # Test Invalid Passed Type (substring)
    with pytest.raises(TypeError):
        to_namedtuple(['string'])

    # Test Dict to NamedTuple - Simple Conversion
    assert to_namedtuple({'a': 1, 'b': 2})
    assert to_namedtuple({'a': 1, 'b': 2}) == \
          collections.namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)

    # Test Dict to NamedTuple - Complex Conversion

# Generated at 2022-06-13 20:41:07.598913
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    dic_obj = {'a': 1, 'b': 2}
    nt_obj = to_namedtuple(dic_obj)
    assert isinstance(nt_obj, tuple)
    assert isinstance(nt_obj, NamedTuple)
    dic_obj['c'] = 3
    assert nt_obj.a == dic_obj['a']
    assert nt_obj.b == dic_obj['b']
    assert nt_obj._asdict() == OrderedDict({'a': 1, 'b': 2})
    list_obj = [1, 2, 3, 4, 5]
    out = to_namedtuple(list_obj)
    assert isinstance(out, list)
    assert out == list_obj

# Generated at 2022-06-13 20:41:17.907059
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from nt import assert_equal
    # noinspection PyPackageRequirements,PyUnresolvedReferences
    from nt.testing import datalist, temp_list, temp_list_and_line

    with datalist(
        temp_list_and_line([
            'obj = {',
            '    "a": 1,',
            '    "b": 2,',
            '}',
            '',
        ])
    ) as (data, _):
        obj = eval(data[0]['obj'])
        assert_equal(
            to_namedtuple(obj),
            namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2),
        )


# Generated at 2022-06-13 20:41:42.229315
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    import pytest  # type: ignore[import]
    from types import MappingProxyType

    # noinspection PyUnresolvedReferences
    @_to_namedtuple.register(MappingProxyType)
    def _(
            obj: MappingProxyType,
            _started: bool = False
    ) -> NamedTuple:
        return _to_namedtuple(dict(obj), _started)

    # noinspection PyUnresolvedReferences
    @_to_namedtuple.register(set)
    def _(
            obj: set,
            _started: bool = False
    ) -> NamedTuple:
        return _to_namedtuple(obj, _started)

    # noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:41:50.483191
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # pylint: disable=too-many-branches,too-many-nested-blocks,too-many-statements
    from unittest.mock import patch
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifier

    # Configure all the patches for testing,
    # By using patch.dict, we can pass in multiple patches at once.

# Generated at 2022-06-13 20:41:59.698771
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from tempfile import NamedTemporaryFile
    from flutils.namedtupleutils import to_namedtuple
    from flutils.namedtupleutils.test_to_namedtuple import TestObj

    # Test class.
    test_obj = TestObj(
        a=1,
        b=2,
        c=TestObj(d=4, e=5, f=TestObj(g=7, h=8)),
    )

# Generated at 2022-06-13 20:42:03.569177
# Unit test for function to_namedtuple
def test_to_namedtuple():
    case1 = {'j': 1, 'p': 2, 'k': 3}
    result1 = to_namedtuple(case1)
    assert result1.j == 1 and result1.k == 3 and result1.p == 2

# Generated at 2022-06-13 20:42:07.577025
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {"a": 1, "b": 2}
    assert to_namedtuple(obj) == obj

if __name__ == "__main__":
    test_to_namedtuple()

# Generated at 2022-06-13 20:42:17.814879
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import collections
    dic = {'a': 1, 'b': 2}
    assert collections.NamedTuple == type(to_namedtuple(dic))
    tup = (1, 2)
    assert tuple == type(to_namedtuple(tup))
    for i, val in enumerate(to_namedtuple(tup)):
        assert tup[i] == val
    lis = [1, 2]
    assert list == type(to_namedtuple(lis))
    for i, val in enumerate(to_namedtuple(lis)):
        assert lis[i] == val
    obj = collections.OrderedDict({'a': 1, 'b': 2})

# Generated at 2022-06-13 20:42:28.379950
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import collections
    from flutils.validators import LaxIdentifierSyntax

    dic = {'a': 1, 'b': 2}
    namedtuple_ = to_namedtuple(dic)
    assert isinstance(namedtuple_, collections.namedtuple)
    assert namedtuple_.a == 1
    assert namedtuple_.b == 2

    dic = {'a': 1, 'b': 2}
    namedtuple_ = to_namedtuple(dic)
    assert isinstance(namedtuple_, collections.namedtuple)
    assert namedtuple_.a == 1
    assert namedtuple_.b == 2

    dic = {'a': 1, '_a': 1, '__a': 1, 'b': 2}

# Generated at 2022-06-13 20:42:40.293214
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(dict(a=1, b=2)) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict(a=1, b=2)) == NamedTuple(a=1, b=2)
    assert to_namedtuple(list(dict(a=1, b=2))) == NamedTuple(a=1, b=2)
    assert to_namedtuple(list(dict(a=1, b=2).items())) == NamedTuple(a=1, b=2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == NamedTuple(a=1, b=2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2).__dict__) == NamedT