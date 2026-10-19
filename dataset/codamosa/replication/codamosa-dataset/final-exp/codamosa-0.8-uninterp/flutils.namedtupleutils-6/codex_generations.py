

# Generated at 2022-06-13 20:32:52.750008
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyUnresolvedReferences
    """Unit test for function to_namedtuple.

    This function is not in :mod:`flutils.testutils` to prevent a recursive
    import loop.
    """
    from flutils.testutils import UnitTester
    tester = UnitTester(to_namedtuple)

    # pylint: disable=bare-except
    # pylint: disable=no-self-use
    class TestNamedTuple(NamedTuple):
        attr1: int
        attr2: int

        def sorted(self):
            return sorted(self)

    class TestSimpleNamespace(SimpleNamespace):
        @property
        def sorted(self) -> List:
            return sorted(self.__dict__.keys())

    from collections import OrderedDict

    dic

# Generated at 2022-06-13 20:33:04.517709
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple"""
    from flutils.namedtupleutils import to_namedtuple
    from flutils.pytestutils import assert_in, assert_not_in, assert_raises
    from flutils.typingsutils import is_list, is_list_tuple, is_namedtuple
    from flutils.validators import validate_identifier

    obj = {'a': 1, 'b': 2}
    out = to_namedtuple(obj)
    assert is_namedtuple(out)
    assert_in('a', obj)
    assert_not_in('a', out)
    assert_in('b', obj)
    assert_not_in('b', out)
    assert obj['a'] == 1
    assert getattr(out, 'a') == 1
    assert obj

# Generated at 2022-06-13 20:33:09.731980
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    with pytest.raises(TypeError):
        to_namedtuple(1)

    with pytest.raises(TypeError):
        to_namedtuple('abc')

    with pytest.raises(TypeError):
        to_namedtuple(None)

    with pytest.raises(TypeError):
        to_namedtuple(1.0)

    with pytest.raises(TypeError):
        to_namedtuple(())
    with pytest.raises(TypeError):
        to_namedtuple([])


    dic = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
    }
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple)

# Generated at 2022-06-13 20:33:22.211431
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Function: to_namedtuple"""
    import flutils.namedtupleutils

    # dic example
    dic = {'a': 1, 'b': 2}
    converted = flutils.namedtupleutils.to_namedtuple(dic)
    assert isinstance(converted, tuple)
    assert converted.a == 1
    assert converted.b == 2
    assert converted[0] == 1
    assert converted[1] == 2

    # list example
    lst = [1, 2, 3]
    converted = flutils.namedtupleutils.to_namedtuple(lst)
    assert isinstance(converted, list)
    assert converted[0] == 1
    assert converted[1] == 2
    assert converted[2] == 3
    assert len(converted) == 3

    # mapp

# Generated at 2022-06-13 20:33:34.984890
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: () -> None
    """Unit tests for the function to_namedtuple."""

    def _tmp_to_namedtuple(
            obj: Any,
            _started: bool = False
    ) -> Any:
        return _to_namedtuple(obj, _started=_started)

    dic = OrderedDict([
        ('a', 1),
        ('b', 2)
    ])

    # Check that starting with a tuple works correctly
    obj = _tmp_to_namedtuple((dic,))
    assert len(obj) == 1
    a: NamedTuple = obj[0]
    assert a.a == 1
    assert a.b == 2

    # Check starting with a list works correctly
    obj = _tmp_to_namedtuple([dic])

# Generated at 2022-06-13 20:33:46.404647
# Unit test for function to_namedtuple
def test_to_namedtuple():
    if __name__ == '__main__':
        import unittest
        from pprint import pprint

        class Test_to_namedtuple(unittest.TestCase):
            def test_to_namedtuple_1(self):
                """Test to_namedtuple() against expected results."""

                @to_namedtuple
                class Test1:
                    x: int
                    y: int

                obj1 = Test1(1, 2)
                self.assertEqual(obj1.x, 1)
                self.assertEqual(obj1.y, 2)

                obj2 = to_namedtuple(obj1)
                self.assertEqual(obj2.x, 1)
                self.assertEqual(obj2.y, 2)


# Generated at 2022-06-13 20:33:59.002345
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    from collections import OrderedDict
    import random
    import re
    import string
    from typing import Dict, List

    from flutils.namedtupleutils import to_namedtuple
    from flutils.timeutils import now_in_timezone

    dt: str = now_in_timezone('local').strftime('%Y-%m-%dT%H:%M:%SZ')

    rndm: float = float("%.4f" % random.random())

    ascii_letters: str = string.ascii_letters

    non_word_chars: str = re.sub(r'\w', '', ascii_letters)


# Generated at 2022-06-13 20:34:10.619539
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Test converting a SimpleNamespace to a NamedTuple
    from types import SimpleNamespace as _SimpleNamespace
    from flutils.namedtupleutils import ordered_namedtuple
    ns = _SimpleNamespace(a=1, b=2)
    out = to_namedtuple(ns)
    assert out == ordered_namedtuple(a=1, b=2)
    assert out.a == 1
    assert out.b == 2

    # Test converting a SimpleNamespace to a NamedTuple with a Tuple value
    ns = _SimpleNamespace(a=1, b=2, c=(3, 4))
    out = to_namedtuple(ns)
    assert out == ordered_namedtuple(a=1, b=2, c=(3, 4))
    assert out.a == 1
    assert out.b

# Generated at 2022-06-13 20:34:17.645799
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    import collections
    dic = {
        'a': 1,
        'b': 2,
    }
    dic2 = {
        'd': 4,
        'e': 5,
    }
    dic3 = {
        'g': 7,
        'h': 8,
    }
    lis = [dic, dic2, dic3]
    lis2 = [99, 'a', ['bad']]

    ndic = collections.namedtuple('Dic1', ['f', 'j'])
    dic4 = ndic(f=6, j=10)
    dic5 = collections.OrderedDict()
    dic5['i'] = 9
    dic5['k'] = 11

# Generated at 2022-06-13 20:34:27.625293
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    obj = to_namedtuple(dic)
    assert obj == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    tup = (1, 2)
    obj = to_namedtuple(tup)
    assert obj == namedtuple('NamedTuple', '')(), obj

    arr = [1, 2]
    obj = to_namedtuple(arr)
    assert obj == [1, 2], obj

    arr = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    obj = to_namedtuple(arr)

# Generated at 2022-06-13 20:34:40.703313
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from dataclasses import dataclass

    dataclass_list: tuple = (
        dataclass(frozen=True)(simple=str, complex=dict)
        for simple, complex in (dict(c=1, d=2), dict(e=3, f=4))
    )
    tuple_namedtuple = namedtuple('NamedTuple', 'a b c')

    def get_basic_value(obj) -> NamedTuple:
        return NamedTuple(a=1, b=2, c=3)

    def get_basic_list(obj) -> List:
        return [1, 2, 3]

    def get_basic_tuple() -> Tuple:
        return tuple(get_basic_list(None))


# Generated at 2022-06-13 20:34:55.366752
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:35:07.717865
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    def assert_namedtuple(obj, assign=False, **kwargs):
        res = to_namedtuple(obj)
        if assign:
            # noinspection PyArgumentList
            make = namedtuple('NamedTuple', kwargs.keys())  # type: ignore[misc]
            # noinspection PyTypeChecker
            expected = make(*list(kwargs.values()))
        else:
            make = namedtuple('NamedTuple', '')
            expected = make()
        assert isinstance(res, NamedTuple)
        assert res is not expected
        assert res._fields == expected._fields
        for key, val in kwargs.items():
            assert getattr(res, key) == val


# Generated at 2022-06-13 20:35:17.264069
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyUnusedLocal
    from flutils.namedtupleutils import to_namedtuple
    # noinspection PyUnreachableCode
    if True:
        pass

if __name__ == "__main__":
    print(__doc__)
    print(__file__)
    print(f"\nTo run the unit tests:\npython3 -m pytest {__file__}")
    print(f"\nTo run the unit tests quietly:\npython3 -m pytest "
          f"{__file__} -qq")
    print(f"\nTo run the unit tests with the full output:\npython3 -m pytest "
          f"{__file__} -vv")

# Generated at 2022-06-13 20:35:30.507866
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase
    from unittest.mock import patch

    from flutils.namedtupleutils import to_namedtuple
    from flutils.namedtupleutils import _to_namedtuple

    class Test_to_namedtuple(TestCase):
        def test_to_namedtuple(self):
            from flutils.validators import validate_identifier

            # noinspection PyTypeChecker
            self.assertIs(to_namedtuple(1), 1)

            # noinspection PyTypeChecker
            self.assertIs(to_namedtuple(1.0), 1.0)

            self.assertIs(to_namedtuple(True), True)

            self.assertIs(to_namedtuple(False), False)


# Generated at 2022-06-13 20:35:38.192745
# Unit test for function to_namedtuple
def test_to_namedtuple():  # noqa: D103

    # noinspection PyUnusedLocal
    def test_dict(dic: Mapping):
        _to_namedtuple(dic)
        assert isinstance(dic, Mapping)
        assert isinstance(dic, OrderedDict)
        _to_namedtuple(dic, _started=True)
        assert isinstance(dic, Mapping)
        assert isinstance(dic, OrderedDict)
        assert hasattr(dic, '__dict__')
        assert hasattr(dic, '_fields')

    def test_list(lst: List):
        _to_namedtuple(lst)
        assert isinstance(lst, List)
        _to_namedtuple(lst, _started=True)

# Generated at 2022-06-13 20:35:50.911482
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    dic1 = {'a': 1, 'b': 2, 'c': 3}
    dic_i = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dic_o = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    assert to_namedtuple(dic) == namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)
    assert to_namedtuple(dic1) == namedtuple('NamedTuple', ('a', 'b', 'c'))(a=1, b=2, c=3)
    assert to_namedtuple(dic_i) == namedt

# Generated at 2022-06-13 20:36:02.110726
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""

    data: Union[List, Mapping, NamedTuple, SimpleNamespace, Tuple] = {
        'a': 1, 'b': 2
    }

    out = to_namedtuple(data)
    assert hasattr(out, 'a')
    assert hasattr(out, 'b')
    assert out.a == 1
    assert out.b == 2

    data = [data]
    out = to_namedtuple(data)
    assert isinstance(out, list)
    assert hasattr(out[0], 'a')
    assert hasattr(out[0], 'b')
    assert out[0].a == 1
    assert out[0].b == 2

    out = to_namedtuple(data)
    assert isinstance(out, list)


# Generated at 2022-06-13 20:36:14.683335
# Unit test for function to_namedtuple
def test_to_namedtuple():
    def run_test(obj, expected):
        actual = to_namedtuple(obj)
        assert actual == expected
    obj1 = SimpleNamespace(
        a=1,
        b=2,
        c=3,
    )
    exp1 = namedtuple('NamedTuple', ['a', 'b', 'c'])(a=1, b=2, c=3)
    obj2 = OrderedDict(
        [
            ('_a', 1),
            ('b', 2),
            ('c', 3),
        ]
    )
    exp2 = namedtuple('NamedTuple', ['b', 'c'])(b=2, c=3)

# Generated at 2022-06-13 20:36:21.556571
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple([{}] * 3) == [NamedTuple()] * 3
    assert to_namedtuple((1, 2, 3, {'a': 1, 'b': 2})) == NamedTuple(
        1, 2, 3, NamedTuple(a=1, b=2)
    )
    assert to_namedtuple(OrderedDict((('a', 1), ('b', 2)))) == NamedTuple(
        a=1, b=2
    )
    assert to_namedtuple({'a': 1, 'b': [{'c': 1, 'd': 2}]}) == NamedTuple(
        a=1, b=[NamedTuple(c=1, d=2)]
    )

# Generated at 2022-06-13 20:36:29.818595
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test that the to_namedtuple function correctly converts the input"""
    input = dict(a=1, b=2)
    output = to_namedtuple(input)
    assert isinstance(output, NamedTuple)
    assert output.a == input['a']
    assert output.b == input['b']

# Generated at 2022-06-13 20:36:42.141451
# Unit test for function to_namedtuple
def test_to_namedtuple():

    obj_in = (
        [1, 'a', {'c': 3}, [4, {'e': 5}], 6],
        (1, 'a', {'c': 3}, [4, {'e': 5}], 6),
        {'a': 1, 'b': 2},
        dict(a=1, b=2),
        OrderedDict(a=1, b=2),
        SimpleNamespace(a=1, b=2),
    )


# Generated at 2022-06-13 20:36:52.207733
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2, '__c': 3, 'd_': 4}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': [1, 2, 3], 'c': 'hello'}) == NamedTuple(a=1, b=[1, 2, 3], c='hello')
    assert to_namedtuple({'a': 1, 'b': [1, 2, 3], 'c': {'d': 4}}) == NamedTuple(a=1, b=[1, 2, 3], c=NamedTuple(d=4))

# Generated at 2022-06-13 20:37:03.316077
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.namedtupleutils import to_namedtuple

    class FakeNamedTuple(tuple):
        _fields: List[str] = ['f1', 'f2', 'f3']

    inner_nt = FakeNamedTuple([1, 2, 3])
    dic = {'a': 1, 'b': 2, 'c': inner_nt}
    out = to_namedtuple(dic)
    assert isinstance(out, FakeNamedTuple)
    assert out.a == 1
    assert out.b == 2
    assert isinstance(out.c, FakeNamedTuple)

    lst = [1, 2, {'c': 3, 'd': 4}]
    out = to_namedtuple(lst)
    assert isinstance(out, list)

# Generated at 2022-06-13 20:37:12.896081
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2}.items()) == [
        namedtuple('NamedTuple', 'a b')(a=1, b=2)
    ]


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    """
    Coverage: 100%
    """
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 20:37:21.809669
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple, OrderedDict


# Generated at 2022-06-13 20:37:32.766713
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pytest import raises
    from collections import namedtuple
    from flutils.validators import validate_identifier

    User = namedtuple('User', ['id', 'name', 'email'])
    admin = User(1, 'admin', 'admin@example.com')
    dic = {'name': 'admin', 'email': 'admin@example.com'}
    out = to_namedtuple(dic)
    assert out.name == 'admin'
    assert out.email == 'admin@example.com'
    assert out._fields == ('email', 'name')

    out = to_namedtuple(admin)
    assert out.id == 1
    assert out.name == 'admin'
    assert out.email == 'admin@example.com'
    assert out._fields == ('email', 'id', 'name')



# Generated at 2022-06-13 20:37:46.610676
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
    )
    from types import (
        SimpleNamespace,
    )
    from typing import (
        List,
        NamedTuple,
        Tuple,
    )
    import dataclasses
    @dataclasses.dataclass
    class Data:
        a: str

    @dataclasses.dataclass
    class Foo:
        a: str
        b: int
        c: float
        d: Data

    data = OrderedDict()
    data['a'] = 1
    data['b'] = 2
    data['_b'] = 2

    # noinspection PyTypeChecker
    data2 = data.copy()  # type: ignore[no-any-return]
    data2['_c'] = 3
    data2['c'] = 4

# Generated at 2022-06-13 20:37:58.289970
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class TestToNamedTuple(unittest.TestCase):

        def test_from_dict(self):
            dic = {'one': 'two', 'three': 'four'}
            out = to_namedtuple(dic)
            self.assertIsInstance(out, namedtuple('NamedTuple', 'one three'))

        def test_from_dict_with_underscore(self):
            dic = {'one': 'two', 'three': 'four'}
            out = to_namedtuple(dic)
            self.assertTrue(out._fields == ('one', 'three'))

        def test_from_dict_with_underscore_preserved(self):
            dic = {'one': 'two', '_three': 'four'}
            out = to

# Generated at 2022-06-13 20:38:04.492194
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic)
    assert to_namedtuple(dic).a == 1
    assert to_namedtuple(dic).b == 2
    dic = OrderedDict([('c', 1), ('b', 2)])
    assert to_namedtuple(dic).c == 1
    assert to_namedtuple(dic).b == 2
    dic2 = OrderedDict([('c', 1), ('d', dic)])
    assert to_namedtuple(dic2).c == 1
    assert to_namedtuple(dic2).d.c == 1
    assert to_namedtuple(dic2).d.b == 2
    from collections import namedtuple
    NamedT = namedtuple

# Generated at 2022-06-13 20:38:21.797853
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from typing import NamedTuple, Tuple

    dic = {'a': 1, 'b': 2}
    # noinspection PyTypeChecker,PyArgumentList
    out: NamedTuple = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2

    dic = {'a': 1, 'b': 2, '_foo': 'bar'}
    # noinspection PyTypeChecker,PyArgumentList
    out: NamedTuple = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    assert not hasattr(out, '_foo')

    dic = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}


# Generated at 2022-06-13 20:38:36.687785
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    simple = SimpleNamespace(a=1, b=2)
    pprint(to_namedtuple(simple).__dict__)
    dic = {'a': 1, 'b': 2}
    pprint(dic)
    pprint(to_namedtuple(dic).__dict__)
    dic = {'a': 1, 'b': 2, '_': 3}
    pprint(dic)
    pprint(to_namedtuple(dic).__dict__)
    dic = OrderedDict([('a', 1), ('b', 2), ('_', 3)])
    pprint(dic)
    pprint(to_namedtuple(dic).__dict__)

# Generated at 2022-06-13 20:38:49.221852
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import collections

    dic = collections.OrderedDict()
    dic['b'] = 4
    dic['d'] = 2
    dic['a'] = 1
    dic['c'] = 3
    dic['_'] = 5

    exp_od_01 = collections.OrderedDict()
    exp_od_01['b'] = 4
    exp_od_01['d'] = 2
    exp_od_01['a'] = 1
    exp_od_01['c'] = 3

    exp_nt_01 = collections.namedtuple('NamedTuple', ('a', 'b', 'c', 'd'))(1, 4, 3, 2)
    exp_nt_02 = collections.namedtuple('NamedTuple', ('a', 'b', 'c', 'd', '_'))

# Generated at 2022-06-13 20:39:00.865376
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.namedtupleutils import _to_namedtuple
    from collections import namedtuple
    from types import SimpleNamespace as NS

    assert to_namedtuple(NS(a=1, b=2, abc=3)) == namedtuple(
        'NamedTuple', ['a', 'abc', 'b']
    )(1, 3, 2)

    assert to_namedtuple(NS(a=1, b=2)) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)

    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)


# Generated at 2022-06-13 20:39:11.670061
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    # noinspection PyArgumentList
    obj = namedtuple('foo', 'a b c')(1, 2, 3)
    assert to_namedtuple(obj) == obj
    obj = SimpleNamespace(a=1, b=2, c=3)
    assert to_namedtuple(obj) == namedtuple('NamedTuple', 'a b c')(1, 2, 3)
    obj = {'a': 1, 'b': 2, 'c': 3}
    assert to_namedtuple(obj) == namedtuple('NamedTuple', 'a b c')(1, 2, 3)
    obj = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    assert to_namedtuple

# Generated at 2022-06-13 20:39:25.031054
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import inspect
    import string


# Generated at 2022-06-13 20:39:39.223710
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2

    nt = namedtuple('NT', 'x y z')
    nt2 = nt(x=1, y=2, z=3)
    out = to_namedtuple(nt2)
    assert out.x == 1
    assert out.y == 2
    assert out.z == 3
    out = to_namedtuple([nt2])
    assert out[0].x == 1
    assert out[0].y == 2
    assert out[0].z == 3
    dic = {'a': [nt2]}
    out = to_namedtuple(dic)
    assert out.a[0].x == 1

# Generated at 2022-06-13 20:39:51.527685
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # import json
    from flutils.namedtupleutils import to_namedtuple
    from flutils.timeutils import Timestamp
    from flutils.structutils import Struct

    dic: dict = {
        'a': 1,
        'b': 2,
        'c': 'three'
    }

    class DummyClass:
        pass

    dum = DummyClass()
    dum.a = 1
    dum.b = 2

    actual = to_namedtuple(dic)
    print(type(actual))

    actual = to_namedtuple(dum)
    print(type(actual))

    actual = to_namedtuple(None)
    print(actual)

    actual = to_namedtuple('')
    print(actual)

    actual = to_namedtuple(1)

# Generated at 2022-06-13 20:40:05.080490
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from collections import namedtuple
    from flutils.miscutils import EqualObj

    def test_to_namedtuple(vals, expected):
        out = to_namedtuple(vals)
        assert EqualObj().check_equal(out, expected)

    test_to_namedtuple(
        {'a': 1, 'b': 2}, namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)
    )

# Generated at 2022-06-13 20:40:11.942703
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    dic = OrderedDict([('a', 1), ('b', 2)])
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    dic = OrderedDict([('b', 2), ('a', 1)])
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['b', 'a'])(b=2, a=1)
    lst = [1, 2, 3]

# Generated at 2022-06-13 20:40:38.195077
# Unit test for function to_namedtuple
def test_to_namedtuple():
    ###########################################################################
    # Testing the to_namedtuple function.
    ###########################################################################
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    from flutils.pathutils import change_extension
    import sys
    import os
    import json

    # Grab the filespec for the namedtuple.json.
    datadir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'data',
    ))
    filespec = os.path.join(datadir, 'namedtuple.json')

    # Load the data from the namedtuple.json.
    with open(filespec, 'r') as f:
        text = f.read()

# Generated at 2022-06-13 20:40:46.173153
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict, namedtuple
    from types import SimpleNamespace

    from flutils.namedtupleutils import to_namedtuple

    # Item is a dict:
    test = {'a': 1, 'b': 2}
    result = to_namedtuple(test)
    exp: namedtuple = namedtuple('NamedTuple', 'a b')(1, 2)
    assert result == exp, 'Item is a dict'

    test = {1: 1, 2: 2}
    result = to_namedtuple(test)
    exp: namedtuple = namedtuple('NamedTuple', '1 2')(1, 2)
    assert result == exp, 'Item is a dict of numbers'

    test = {'a': 1, 2: 2, '_b': 3}
    result

# Generated at 2022-06-13 20:40:57.441928
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test the to_namedtuple function."""
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from typing import Dict, NamedTuple

    class NTBase(NamedTuple):
        a: int
        b: int
        c: int

    class NTBase2(NamedTuple):
        a: int
        b: int
        c: int

    class NTNTField(NamedTuple):
        base: NTBase
        base2: NTBase2
        d: int
        e: int

    class NTDict(NamedTuple):
        base: Dict[str, int]
        base2: OrderedDict
        f: int
        g: int


# Generated at 2022-06-13 20:41:09.299913
# Unit test for function to_namedtuple
def test_to_namedtuple():
    L = [1, 'a', {'a': 1, True: 2}]
    S = {'a': 1, True: 2, 'b': 'c'}
    O = OrderedDict(a=1, b=2)
    N = namedtuple('test_namedtuple', 'a b')
    R = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(L)
    assert isinstance(result, list)
    assert isinstance(result[-1], NamedTuple)
    for ind in range(len(L) - 1):
        assert result[ind] == L[ind]
    result = to_namedtuple(S)
    assert isinstance(result, NamedTuple)

# Generated at 2022-06-13 20:41:18.205567
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {
        'a': 1,
        'b': 2,
        'c': [1, {
            'foo': 'bar',
            'b_az': 'qux',
        }],
    }
    from flutils.namedtupleutils import to_namedtuple
    namedtup = to_namedtuple(obj)
    assert isinstance(namedtup, namedtuple('NamedTuple', 'a b c'))
    assert namedtup.a == 1
    assert namedtup.b == 2
    assert isinstance(namedtup.c, list)
    assert namedtup.c[0] == 1
    assert isinstance(namedtup.c[1], namedtuple('NamedTuple', 'b_az foo'))
    assert namedtup.c[1].b_az

# Generated at 2022-06-13 20:41:27.211986
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # Dictionary of mixed types.
    dct = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
            },
        },
    }

    # Convert dictionary to namedtuple.
    nt: NamedTuple = to_namedtuple(dct)

    # List of converted values.
    exp_vals = [1, 2, 3, {'a': 1, 'b': 2, 'c': 3, 'd': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}]

    # Check that

# Generated at 2022-06-13 20:41:38.205749
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # convert dictionary to namedtuple
    args = {'a': 1, 'b': 2}
    tup = to_namedtuple(args)
    assert tup == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    # convert dictionary with string to namedtuple
    args = {'a': '1', 'b': '2'}
    tup = to_namedtuple(args)
    assert tup == namedtuple('NamedTuple', 'a b')(a='1', b='2')

    # convert dictionary with list to namedtuple
    args = {'a': ['1'], 'b': ['2']}
    tup = to_namedtuple(tuple(args))

# Generated at 2022-06-13 20:41:48.189810
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    # Try with a dictionary
    a_dict = {'a': 1, 'b': 2}
    result = to_namedtuple(a_dict)
    assert isinstance(result, namedtuple('NamedTuple', 'a b')), \
        'A dictionary should return a named tuple'
    assert isinstance(result, tuple), 'A named tuple is also a tuple'
    assert type(result.a) is int, 'A named tuple attribute is an int'
    assert type(result.b) is int, 'A named tuple attribute is an int'
    assert result.a == 1, 'The value of a named tuple attribute should be 1'
    assert result.b == 2, 'The value of a named tuple attribute should be 2'
    # Try with an Ordered

# Generated at 2022-06-13 20:41:58.666048
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: () -> None
    """Test for to_namedtuple function."""
    from flutils.namedtupleutils import (
        to_namedtuple
    )
    from collections import OrderedDict

    dic = {
        'a': 1,
        'b': 2
    }
    out = to_namedtuple(dic)
    assert out == ('a', 'b')

    dic = OrderedDict(a=1, b=2)
    out = to_namedtuple(dic)
    assert out == ('a', 'b')

    dic = {'a': 1, 'b': {'c': 3, 'd': 4}}
    out = to_namedtuple(dic)
    assert out == ('a', 'b')
    assert out.a == 1

# Generated at 2022-06-13 20:42:09.216786
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert isinstance(to_namedtuple([1, 2]), list)
    assert isinstance(to_namedtuple((1, 2)), tuple)
    assert isinstance(to_namedtuple({"1": 1, "2": 2}), NamedTuple)
    assert isinstance(to_namedtuple(OrderedDict({"1": 1, "2": 2})), NamedTuple)
    assert isinstance(to_namedtuple(SimpleNamespace({"1": 1, "2": 2})), NamedTuple)

    with pytest.raises(TypeError):
        to_namedtuple("Test")


# Generated at 2022-06-13 20:42:26.343113
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    from collections import Counter, namedtuple

    class TestNamedTupleUtil(unittest.TestCase):

        # Tests for function to_namedtuple
        def test_to_namedtuple(self):
            self.assertEqual(to_namedtuple({'a': 1}), namedtuple('NamedTuple', ['a'])(a=1))
            self.assertEqual(to_namedtuple({'a': 1, 'b': 2}), namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2))

# Generated at 2022-06-13 20:42:32.578305
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d = {'a': 1, 'b': 2}
    assert to_namedtuple(d).a == 1
    assert to_namedtuple(d).b == 2

    d = {'c': 3, 'b': 2}
    assert to_namedtuple(d).c == 3
    assert to_namedtuple(d).b == 2

    d = OrderedDict([('a', 1), ('b', 2)])
    assert to_namedtuple(d).a == 1
    assert to_namedtuple(d).b == 2

    d = OrderedDict([('b', 2), ('a', 1)])
    assert to_namedtuple(d).a == 1
    assert to_namedtuple(d).b == 2
