

# Generated at 2022-06-13 20:32:50.597295
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: () -> None
    from doctest import testmod

    results = testmod()
    assert not results.failed


if __name__ == '__main__':
    import sys
    print(to_namedtuple(sys.modules[__name__]))

# Generated at 2022-06-13 20:32:56.967398
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function namedtupleutils.to_namedtuple."""
    import json

    def test_one(arg: Any, expected: Any = None) -> Any:
        out = to_namedtuple(arg)
        if expected is not None:
            try:
                assert out == expected
            except:
                print(arg)
                print(out)
                print(expected)
                print()
                raise
        return out

    # noinspection PyProtectedMember
    test_one(1)

    test_one((1, 2, 3), (1, 2, 3))

    test_one([1, 2, 3], [1, 2, 3])

    test_one({'a': 1, 'b': 2}, (1, 2))

# Generated at 2022-06-13 20:32:59.422082
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.tests.namedtupleutils import helper_test_to_namedtuple
    helper_test_to_namedtuple()

# Generated at 2022-06-13 20:33:12.159241
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
        namedtuple,
    )
    dic = dict(a=1, b=2)
    out = to_namedtuple(dic)
    assert out.a == 1 and out.b == 2
    dic = dict(a=1, b=2, _c=3)
    out = to_namedtuple(dic)
    assert out.a == 1 and out.b == 2
    dic = OrderedDict(a=1, b=2, _c=3)
    out = to_namedtuple(dic)
    assert out.a == 1 and out.b == 2
    assert out._fields == ('a', 'b')
    out = to_namedtuple(dic)

# Generated at 2022-06-13 20:33:23.925422
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test function to_namedtuple."""
    import pytest
    from collections import namedtuple
    result = to_namedtuple(None)
    assert isinstance(result, namedtuple)
    assert result[0] == None
    result = to_namedtuple(True)
    assert isinstance(result, namedtuple)
    assert result[0] == True
    result = to_namedtuple(False)
    assert isinstance(result, namedtuple)
    assert result[0] == False
    result = to_namedtuple("a")
    assert isinstance(result, namedtuple)
    assert result[0] == "a"
    result = to_namedtuple("")
    assert isinstance(result, namedtuple)
    assert result[0] == ""
    result = to_namedtuple

# Generated at 2022-06-13 20:33:30.521914
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from types import SimpleNamespace
    from collections import OrderedDict
    from collections.abc import Sequence
    from flutils.namedtupleutils import (
        to_namedtuple,
    )
    from flutils.validators import (
        validate_identifier,
    )
    from flutils.testing.helpers import raises

    SimpleNamespaceLike = SimpleNamespace()

    class SimpleNamespaceLike:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

        def __getstate__(self):
            return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


# Generated at 2022-06-13 20:33:43.444822
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.constutils import KeywordError
    from flutils.namedtupleutils import to_namedtuple

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple(OrderedDict((('c', 1), ('b', 2)))) == \
        namedtuple('NamedTuple', 'c b')(c=1, b=2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == \
        namedtuple('NamedTuple', 'a b')(a=1, b=2)
    obj = [dic, dic, dic]


# Generated at 2022-06-13 20:33:50.379807
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    from types import SimpleNamespace

    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2

    dic = OrderedDict((('a', 1), ('b', 2)))
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2

    lis = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    out = to_namedtuple(lis)
    assert isinstance(out, list) is True
    assert isinstance(out[0], NamedTuple) is True
    assert out

# Generated at 2022-06-13 20:34:00.675942
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase
    from unittest.mock import MagicMock, patch

    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict

    def _func():
        return
    class _cls:
        def __call__(self):
            return

    class Tests(TestCase):
        def test_fails(self):
            self.assertRaisesRegex(
                TypeError,
                "Can convert only 'list', 'tuple', 'dict' to a NamedTuple; "
                "got: \((?P<type>.*)\) (?P<data>.*)",
                to_namedtuple,
                'func'
            )

# Generated at 2022-06-13 20:34:05.798861
# Unit test for function to_namedtuple
def test_to_namedtuple():
    normal_dict = {'a': 1, 'b': 2}
    normal_dict_namedtuple = to_namedtuple(normal_dict)
    assert type(normal_dict_namedtuple) is not dict
    assert normal_dict_namedtuple.a == 1
    assert normal_dict_namedtuple != normal_dict

    ordered_dict = OrderedDict(normal_dict)
    ordered_dict_namedtuple = to_namedtuple(ordered_dict)
    assert type(ordered_dict_namedtuple) is not dict
    assert ordered_dict_namedtuple == to_namedtuple(normal_dict)
    assert ordered_dict_namedtuple != normal_dict

    simple_namespace = SimpleNamespace(**normal_dict)

# Generated at 2022-06-13 20:34:16.144880
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from types import SimpleNamespace
    from collections import (
        OrderedDict,
        namedtuple
    )
    from flutils.validators import validate_identifier

    # noinspection PyUnresolvedReferences
    nt = namedtuple('NamedTuple', ['x', 'y', 'z'])
    obj = nt(x=1, y=2, z=3)
    assert to_namedtuple(obj) == obj
    t = (1, 2, 3)
    assert to_namedtuple(t) == t
    l = [1, 2, 3]
    assert to_namedtuple(l) == l

    d = {'x': 1, 'y': 2, 'z': 3}
    out = to_named

# Generated at 2022-06-13 20:34:25.218812
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import collections

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == collections.namedtuple('NamedTuple', 'a b')(a=1, b=2)
    dic = collections.OrderedDict({'a': 1, 'b': collections.OrderedDict({'c': 'c'})})
    assert to_namedtuple(dic) == collections.namedtuple('NamedTuple', 'a b')(a=1, b=collections.namedtuple('NamedTuple', 'c')(c='c'))
    dic = {'a': 1, 'b': 2}

# Generated at 2022-06-13 20:34:37.294543
# Unit test for function to_namedtuple
def test_to_namedtuple():

    dic = {'a': 1, 'b': 2}
    ans = to_namedtuple(dic)
    assert ans == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': 2, '_c': 2}
    ans = to_namedtuple(dic)
    assert ans == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': 2, 'a.b': 2}
    ans = to_namedtuple(dic)
    assert ans == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': 2, 'a_b': 2}
    ans = to_namedtuple(dic)

# Generated at 2022-06-13 20:34:48.623552
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Tests for the to_namedtuple function."""
    import pytest
    with pytest.raises(TypeError) as err:
        to_namedtuple(1.1)  # type: ignore[no-untyped-call]
    assert 'object is not iterable' in str(err.value)
    with pytest.raises(TypeError) as err:
        to_namedtuple(1)  # type: ignore[no-untyped-call]
    assert 'list' in str(err.value)
    with pytest.raises(TypeError) as err:
        to_namedtuple(())  # type: ignore[no-untyped-call]
    assert 'dict' in str(err.value)
    assert to_namedtuple([]) == []
    assert to_namedt

# Generated at 2022-06-13 20:34:57.865059
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    from collections import namedtuple

    obj = {'a': 1, 'b': 2}
    expected = namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple(obj) == expected

    obj = {'a': 1, 'b': 2, '_c': 3}
    expected = namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple(obj) == expected

    obj = {'a': 1, 'b': 2, 'c': {'x': 9, 'y': 10}}

# Generated at 2022-06-13 20:35:09.944531
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    def _test_namedtuple(
            name: str,
            obj: dict
    ) -> None:
        nt = to_namedtuple(obj)
        classname = nt.__class__.__name__  # type: ignore[no-union-attr]
        assert classname == 'NamedTuple'
        assert len(nt) == len(obj)
        for key in obj:
            key_val = getattr(nt, key)  # type: ignore[attr-defined]
            obj_val = obj[key]
            assert key_val == obj_val
            assert getattr(nt, key) == obj[key]

    # dic
    _test_namedtuple('dict', {'a': 1, 'b': 2})



# Generated at 2022-06-13 20:35:19.285134
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest.mock import patch, sentinel
    from collections import OrderedDict
    from collections.abc import Mapping, Sequence
    from typing import Any
    from flutils.namedtupleutils import _to_namedtuple
    import pytest

    def _assert_base_type(obj: Any) -> None:
        assert isinstance(obj, (Mapping, Sequence))

    @singledispatch
    def failing_mock(obj: Any, *, _started: bool = False) -> None:
        if _started is False:
            pytest.fail("base function should not be called")

    with patch('flutils.namedtupleutils._to_namedtuple', failing_mock):
        _assert_base_type('hello')
        _assert_base_type(None)
        _assert_base_type

# Generated at 2022-06-13 20:35:33.393755
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # 1st test:
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert nt.a == 1
    assert nt.b == 2
    assert nt == (1, 2)

    # 2nd test:
    od = OrderedDict(a=1, b=2)
    nt = to_namedtuple(od)
    assert nt.a == 1
    assert nt.b == 2
    assert nt == (1, 2)

    # 3rd test:
    nt_in = namedtuple('In', 'a b')(1, 2)
    nt_out = to_namedtuple(nt_in)
    assert nt_in.a == nt_out.a
    assert nt_

# Generated at 2022-06-13 20:35:37.166954
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.testutils.checkfunctions import (
        CheckFunctions,
    )

    checkfunctions = CheckFunctions()
    checkfunctions.register(to_namedtuple)
    checkfunctions.run_all(
        namespace=globals(),
        exclude=(
            'pyflakes',
        ),
    )

# Generated at 2022-06-13 20:35:45.832030
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict

# Generated at 2022-06-13 20:36:01.793040
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import (
        validate_identifier,
    )

    # Normal dictionary and OrderedDict
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == (1, 2)
    odic = OrderedDict()
    odic['c'] = dic
    odic['a'] = 3
    odic['b'] = 4
    assert to_namedtuple(odic) == (
        {'a': 1, 'b': 2},
        3,
        4,
    )

    # SimpleNamespace

# Generated at 2022-06-13 20:36:12.833300
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    named = to_namedtuple(dic)
    assert named.a == 1
    assert named.b == 2
    mytuple = (1,2,3,4,5)
    namedmytuple = to_namedtuple(mytuple)
    assert namedmytuple == (1,2,3,4,5)
    mylist = [1,2,3,4,5]
    namedmylist = to_namedtuple(mylist)
    assert namedmylist == [1,2,3,4,5]

# Generated at 2022-06-13 20:36:20.523981
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    from flutils.namedtupleutils import to_namedtuple
    doctest.testmod(verbose=True)
    # noinspection SpellCheckingInspection

# Generated at 2022-06-13 20:36:31.372708
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class TestToNamedTuple(unittest.TestCase):

        def test_tuple(self):
            self.assertEqual(
                to_namedtuple((1, 2, dict(a=1, b=2))),
                namedtuple('NamedTuple', 'a b data')(
                    1, 2, namedtuple('NamedTuple', 'a b')(1, 2)
                )
            )

        def test_list(self):
            self.assertEqual(
                to_namedtuple([1, 2, dict(a=1, b=2)]),
                [1, 2, namedtuple('NamedTuple', 'a b')(1, 2)]
            )


# Generated at 2022-06-13 20:36:42.549933
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from datetime import datetime
    from types import SimpleNamespace
    d = {'a': 1, 'b': 2}
    r = to_namedtuple(d)
    assert r.a == d['a']
    assert r.b == d['b']
    d = {'id': 'test', 'y': {'a': 1, 'b': 2}}
    r = to_namedtuple(d)
    assert r.y.a == d['y']['a']
    assert r.y.b == d['y']['b']

# Generated at 2022-06-13 20:36:52.766132
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest.mock import patch
    from flutils.namedtupleutils import to_namedtuple

    test_data = [
        ({'a': 1, 'b': 2}, {'a': 1, 'b': 2}),
        ((('a', 1), ('b', 2)), {'a': 1, 'b': 2}),
        (('a', 1, 'b', 2), {'a': 1, 'b': 2}),
        (('a', 'b', 1, 2), {'a': 1, 'b': 2}),
        (('a',), {'a': None}),
        ((('a',), ('b', 2)), {'a': None, 'b': 2}),
        ((('a', 2), ('b', 2)), {'a': 2, 'b': 2}),
    ]

# Generated at 2022-06-13 20:37:03.972097
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # starts with input list; all items are dicts
    test_inp = [
        {'a': 1, 'b': 2},
        {'a': 2, 'b': 3},
        {'a': 3, 'b': 4},
    ]
    test_out = to_namedtuple(test_inp)
    assert test_out == [
        NamedTuple(a=1, b=2),
        NamedTuple(a=2, b=3),
        NamedTuple(a=3, b=4),
    ]

    # starts with input list; first item is dict, next 2 items are
    # NamedTuple; second item contains a list as a value

# Generated at 2022-06-13 20:37:14.775234
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b == 2
    lis: List[Any] = []
    obj = to_namedtuple(lis)
    assert obj == []
    lis = [1]
    obj = to_namedtuple(lis)
    assert obj == [1]
    dic = {'a': 1, 'b': {'c': 3}}
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b.c == 3


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:37:22.811763
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import collections
    import datetime
    import decimal
    import types

    simple = {'a': 1, 'b': 2}
    result: types.SimpleNamespace = to_namedtuple(simple)
    assert result.a == 1
    assert result.b == 2

    simple_tuple = (1, 2)
    result: types.SimpleNamespace = to_namedtuple(simple_tuple)
    assert result == [1, 2]

    simple_list = [1, 2]
    result: types.SimpleNamespace = to_namedtuple(simple_list)
    assert result == [1, 2]


# Generated at 2022-06-13 20:37:33.776741
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple"""
    # Simple test
    inp = {'a': 1, 'b': 2}
    exp = namedtuple('NamedTuple', 'a b')(1, 2)
    act = to_namedtuple(inp)
    assert(exp == act)

    # Test exceptions
    inp = 'string'
    exc: Exception = None
    try:
        to_namedtuple(inp)
    except Exception as e:
        exc = e
    assert isinstance(exc, TypeError)

    # Test exceptions
    inp = set([1,2,3])
    exc: Exception = None
    try:
        to_namedtuple(inp)
    except Exception as e:
        exc = e
    assert isinstance(exc, TypeError)

   

# Generated at 2022-06-13 20:37:49.541753
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import Dict
    # add some basic tests
    print("test_to_namedtuple: Testing to_namedtuple...")
    d: Dict[str,int] = {'a': 1, 'b': 2}
    exp_result: NamedTuple = namedtuple('NamedTuple', 'a b')(1, 2)

    result = to_namedtuple(d)
    assert result == exp_result
    d_od: OrderedDict = OrderedDict(a=1, b=2)
    result = to_namedtuple(d_od)
    assert result == exp_result
    s_n: SimpleNamespace = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(s_n)
    assert result == exp_result

# Generated at 2022-06-13 20:37:59.680709
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple({'a': '1', 'b': 2}) == namedtuple('NamedTuple', 'a b')('1', 2)
    assert to_namedtuple({'a': 1, 'b': '2'}) == namedtuple('NamedTuple', 'a b')(1, '2')
    assert to_namedtuple({'a': '1', 'b': '2'}) == namedtuple('NamedTuple', 'a b')('1', '2')

# Generated at 2022-06-13 20:38:11.561499
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from sys import version_info as verinfo
    from collections import OrderedDict
    from typing import Generator

    dic = {'a': 1, 'b': 2}
    dic_with_nest = {'a': 1, 'b': 2, 'c': {'a': 'x', 'b': 'y'}}
    lis = ['a', 'b', 'c', 'd']
    lis_with_nest = ['a', 'b', 'c', 'd', {'a': 'x', 'b': 'y'}]
    odict = OrderedDict([('a', 1), ('b', 2)])
    odict_with_nest = OrderedDict([('a', 1), ('b', 2), ('c', {'a': 'x', 'b': 'y'})])
   

# Generated at 2022-06-13 20:38:21.859384
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # pylint: disable=missing-docstring
    dic_a = {'a': 1, 'b': 2}

    nt_a = to_namedtuple(dic_a)

    assert isinstance(nt_a, NamedTuple)
    assert nt_a.a == 1
    assert nt_a.b == 2

    dic_b = {'a.b': 1, 'c': 2}

    nt_b = to_namedtuple(dic_b)

    assert isinstance(nt_b, NamedTuple)
    assert nt_b.c == 2
    assert nt_b.a_b == 1

    dic_c = {'a': 1, 'b': 2, 'c': 3}


# Generated at 2022-06-13 20:38:33.946198
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(dict(a=1, b=2)) == to_namedtuple(dict(b=2, a=1))
    assert to_namedtuple(dict(a=1, b=2)) == to_namedtuple(dict(b=2, a=1.0))
    assert to_namedtuple(dict(a=1, b=2)) == to_namedtuple(OrderedDict(a=1, b=2))
    assert to_namedtuple(dict(a=1, b=2)) == to_namedtuple(OrderedDict(b=2, a=1))
    assert to_namedtuple(dict(a=1, b=2)) == to_namedtuple(OrderedDict(b=2, a=1.0))
    assert to_namedt

# Generated at 2022-06-13 20:38:40.467281
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:38:51.589885
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """ Tests :py:func:`flutils.namedtupleutils.to_namedtuple` function.
    """
    from datetime import timedelta
    from types import GeneratorType
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    import pytest

    # SimpleNamespace
    simp = SimpleNamespace(a=1, b=2)
    simp_converted = to_namedtuple(simp)
    assert simp_converted == simp_converted._replace(a=1, b=2)

    # OrderedDict
    ord_dic = OrderedDict(a=1, b=2)
    ord_dic_converted = to_namedtuple(ord_dic)
    assert ord_dic_converted == ord_

# Generated at 2022-06-13 20:39:03.242057
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import types

    dic = {'a': 1, 'b': 2}
    named = to_namedtuple(dic)
    assert isinstance(named, namedtuple)
    assert hasattr(named, 'a') and hasattr(named, 'b')
    assert getattr(named, 'a') == 1 and getattr(named, 'b') == 2

    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    named = to_namedtuple(od)
    assert isinstance(named, namedtuple)
    assert hasattr(named, 'a') and hasattr(named, 'b')
    assert getattr(named, 'a') == 1 and getattr(named, 'b') == 2

   

# Generated at 2022-06-13 20:39:14.580286
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from copy import copy
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from collections.abc import Sequence
    from typing import Tuple
    import types

    def _NamedTuple(*args, **kwargs):
        return namedtuple(*args, **kwargs)


# Generated at 2022-06-13 20:39:26.225202
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyUnresolvedReferences,PyShadowingBuiltins
    from collections import OrderedDict
    from unittest.mock import patch
    from datetime import datetime

    # noinspection PyUnresolvedReferences
    from types import SimpleNamespace

    # noinspection PyUnresolvedReferences
    from flutils.validators import validate_identifier

    # noinspection PyUnresolvedReferences
    import sys
    # noinspection PyUnresolvedReferences
    from io import StringIO

    # Basic usage
    assert to_namedtuple({}) == namedtuple('NamedTuple', '')()
    assert to_namedtuple({'a': 1}) == namedtuple('NamedTuple', ('a',))(1)

# Generated at 2022-06-13 20:39:42.823025
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import deque
    from typing import Deque

    dic = {'a': 1, 'b': 2}
    nt: NamedTuple = to_namedtuple(dic)

    assert nt.a == 1
    assert nt.b == 2

    dic2 = {'a': 1, 'b': dic}
    nt2: NamedTuple = to_namedtuple(dic2)

    assert nt2.a == 1
    assert nt2.b.a == 1
    assert nt2.b.b == 2

    dic3 = {'a': 1, 'b': [{'b':2}]}
    nt3: NamedTuple = to_namedtuple(dic3)


# Generated at 2022-06-13 20:39:53.960332
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(1, 2)
    li = [dic]
    assert to_namedtuple(li) == [namedtuple('NamedTuple', 'a b')(1, 2)]
    dic2 = {'a': 1, 'b': [2, 3]}
    assert to_namedtuple(dic2) == namedtuple('NamedTuple', 'a b')(1, (2, 3))
    tu = (1, 2, 3)
    assert to_namedtuple(tu) == (1, 2, 3)
    ns = SimpleNamespace(a=1, b=2)
    assert to_namedtuple(ns) == named

# Generated at 2022-06-13 20:40:04.547535
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 'boo', 'c': [1, 2, 3]}
    nt = to_namedtuple(dic)
    assert nt
    # noinspection PyProtectedMember
    assert nt._fields == ('a', 'b', 'c')
    assert nt.a == 1
    assert nt.b == 'boo'
    assert nt.c == [1, 2, 3]
    dic = {
        'a': 1,
        'b': 2,
        'D': {
            'a': 1,
            'b': 2
        }
    }
    nt = to_namedtuple(dic)
    assert nt
    # noinspection PyProtectedMember

# Generated at 2022-06-13 20:40:15.285196
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    lst = [dic]
    assert to_namedtuple(lst) == [namedtuple('NamedTuple', 'a b')(a=1, b=2)]

    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]

    od = OrderedDict(dic)
    assert to_namedtuple(od) == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    tup = (1, 2, 3)
    assert to_namedtuple(tup) == (1, 2, 3)



# Generated at 2022-06-13 20:40:26.803250
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import os
    import pathlib
    import tempfile
    from flutils.flutils_testing import Test_Case

    # noinspection PyProtectedMember
    here = pathlib.Path(__file__).parent
    test_data_dir = here / 'testdata'
    # noinspection PyProtectedMember
    test_data_dir_abs = test_data_dir.resolve()

    # noinspection PyProtectedMember
    with open(test_data_dir / 'test_to_namedtuple.json') as f:
        # noinspection PyProtectedMember
        test_data = SimpleNamespace(**SimpleNamespace(**json.load(f)))

    # noinspection PyProtectedMember

# Generated at 2022-06-13 20:40:33.996689
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:40:44.832177
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase
    from flutils.collectionsutils import OrderedDefaultDict


# Generated at 2022-06-13 20:40:45.389037
# Unit test for function to_namedtuple
def test_to_namedtuple():
    pass

# Generated at 2022-06-13 20:40:57.205320
# Unit test for function to_namedtuple
def test_to_namedtuple():

    def _to_namedtuple_test_1():
        inp = {'a': 1, 'b': 2}
        exp = namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
        out = to_namedtuple(inp)
        assert out == exp
        assert out.a == exp.a
        assert out.b == exp.b
        assert out.a != exp.b
        assert out.b != exp.a

    def _to_namedtuple_test_2():
        inp = [1, 2, 3]
        exp = [1, 2, 3]
        out = to_namedtuple(inp)
        assert out == exp
        assert out[0] == exp[0]
        assert out[1] == exp[1]

# Generated at 2022-06-13 20:41:09.112938
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == cast(NamedTuple, (1, 2))

    assert to_namedtuple((1, 2)) == cast(NamedTuple, (1, 2))

    dic = OrderedDict([('a', 1), ('b', 2)])
    assert to_namedtuple(dic) == cast(NamedTuple, (1, 2))

    dic = {'a': 1, 'B': 2, 'c': 3}
    assert to_namedtuple(dic) == cast(NamedTuple, (1, 3))

    dic = {'a': 1.0, 'B': 2.0, 'c': 3.0}
    assert to_namedtuple(dic) == cast

# Generated at 2022-06-13 20:41:21.862995
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test for function to_namedtuple"""
    import doctest

    _test = doctest.testmod
    _test(to_namedtuple)

# Generated at 2022-06-13 20:41:34.472176
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(dict(a=1, b=2))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(OrderedDict(
        a=1,
        b=2
    ))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(
        SimpleNamespace(a=1, b=2)
    )
    assert to_namedtuple({'_a': 1, 'b': 2}) == \
        to_namedtuple(dict(_a=1, b=2))
    assert to_namedtuple({'_a': 1, 'b': 2})

# Generated at 2022-06-13 20:41:46.323967
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import os
    import sys
    import unittest
    from collections import OrderedDict
    import doctest
    from flutils.namedtupleutils import to_namedtuple
    _r: List[int] = []

    class TestTo_Namedtuple(unittest.TestCase):
        def test_to_namedtuple(self):
            # Test with multiple cases
            dic = {'a': 1, 'b': 2, 'c': 3}
            self.assertEqual(
                to_namedtuple(dic),
                namedtuple('NamedTuple', 'a b c')(1, 2, 3)
            )
            # Test that underscore occurrences are removed
            dic = {'a': 1, 'b': 2, '_c': 3}

# Generated at 2022-06-13 20:41:57.850020
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert repr(to_namedtuple([])) == 'NamedTuple()'
    assert repr(to_namedtuple([[]])) == 'NamedTuple(tuple())'
    assert repr(to_namedtuple({})) == 'NamedTuple()'
    assert repr(to_namedtuple({'a': 1})) == 'NamedTuple(a=1)'
    assert repr(to_namedtuple({'a': [1,2]})) == 'NamedTuple(a=NamedTuple(1, 2))'
    assert repr(to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))) == 'NamedTuple(a=1, b=2)'

# Generated at 2022-06-13 20:42:10.701728
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
    )
    from types import (
        SimpleNamespace,
    )
    from typing import (
        Any,
        Dict,
        List,
        Tuple,
    )
    from unittest.mock import (
        MagicMock,
        patch,
    )
    from flutils.namedtupleutils import (
        to_namedtuple,
    )

    # Test working procedures
    dic: Dict[str, Any] = OrderedDict([
        ('a', 'first'),
        ('b', OrderedDict([
            ('c', 'second'),
            ('d', OrderedDict([
                ('e', 'third'),
            ])),
        ])),
        ('f', 'fourth'),
    ])

# Generated at 2022-06-13 20:42:21.420723
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from typing import List, Tuple, NamedTuple
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_namedtuple

    def assert_not_equal(
            actual: NamedTuple,
            expected: NamedTuple
    ) -> None:
        try:
            assert actual != expected
        except AssertionError:
            raise AssertionError(
                '%r is equal to %r' % (actual, expected)
            )

    def assert_equal(
            actual: NamedTuple,
            expected: NamedTuple,
            msg: str = '',
    ) -> None:
        try:
            assert actual == expected, msg
        except AssertionError:
            raise AssertionError

# Generated at 2022-06-13 20:42:30.238663
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:42:40.808538
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        "a": 1,
        "b": {
            "c": 2,
            "d": 3,
            "f": {
                "g": 4,
                "h": 5,
                "i": 6,
            },
        },
    }
    tup = (
        1,
        (
            2,
            3,
            (
                4,
                5,
                6,
            ),
        ),
    )
    lst = [
        1,
        [
            2,
            3,
            [
                4,
                5,
                6,
            ],
        ],
    ]