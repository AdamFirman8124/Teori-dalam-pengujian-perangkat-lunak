

# Generated at 2022-06-13 20:32:43.247601
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)
    assert out.a == dic['a']
    assert out.b == dic['b']

    lst = [1, 2, 3]
    out = to_namedtuple(lst)
    assert isinstance(out, list)
    assert isinstance(out[0], int)
    assert isinstance(out[1], int)
    assert isinstance(out[2], int)
    assert out == lst

    lst = [[1, 2], 2, 3]
    out = to_namedtuple(lst)
    assert isinstance(out, list)
    assert isinstance(out[0], list)

# Generated at 2022-06-13 20:32:54.005229
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from sys import version_info as svi

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch  # type: ignore[no-redef]

    if svi < (3, 5, 0):
        from flutils.namedtupleutils import _to_namedtuple

    # noinspection PyTypeChecker
    @patch('flutils.namedtupleutils._to_namedtuple')
    def test_exceptions(mock: Any) -> None:
        mock.side_effect = Exception('test')
        with pytest.raises(Exception):
            to_namedtuple(['test'])

    def test_refs() -> None:
        dic = {'a': 1, 'b': 2}
        # noinspection PyTypeChecker

# Generated at 2022-06-13 20:33:05.154644
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.tests.resources.base import TestBase
    from flutils.tests.resources.base import run_test
    from flutils.tests.resources.base import run_test_for_type
    from flutils.tests.resources.base import run_test_for_types
    from flutils.tests.resources.base import TEST_TYPES

    class Test_to_namedtuple(TestBase):
        """Test for the to_namedtuple function."""

        # noinspection PyMissingOrEmptyDocstring
        @classmethod
        def setUpClass(cls):
            cls.func = to_namedtuple

        def test_functionality(self):
            """Test the function with a variety of inputs."""

# Generated at 2022-06-13 20:33:10.140001
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from copy import deepcopy
    import random
    from typing import Dict
    from datetime import datetime
    from collections import OrderedDict

    def randwords() -> Dict[str, str]:
        """Return a dictionary, a list or a tuple of random words."""
        from flutils.text import randwords
        keys = sorted(cast(List[str], randwords()))
        n = random.randint(len(keys), len(keys) * 2)
        vals = cast(List[str], randwords(n))
        ret = {}
        for key, val in zip(keys, vals):
            ret[key] = val
        if random.randint(0, 1) == 0:
            return ret
        if random.randint(0, 1) == 0:
            ret = list(ret.values())


# Generated at 2022-06-13 20:33:22.293022
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    class ToNamedTupleCase(unittest.TestCase):
        def test_to_namedtuple_simple(self):
            dic = {'a': 1, 'b': 2}
            self.assertEqual(to_namedtuple(dic), namedtuple('NamedTuple', 'a b')(a=1, b=2))
            self.assertEqual(to_namedtuple(dic).a, 1)
            self.assertEqual(to_namedtuple(dic).b, 2)
            self.assertEqual(to_namedtuple(dic)[0], 1)
            self.assertEqual(to_namedtuple(dic)[1], 2)


# Generated at 2022-06-13 20:33:35.053327
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic1 = {'a': 1, 'b': 2}
    assert to_namedtuple(dic1) == namedtuple('NamedTuple', 'a b')(1, 2)
    dic2 = OrderedDict()
    dic2['a'] = 1
    dic2['b'] = 2
    assert to_namedtuple(dic2) == namedtuple('NamedTuple', 'a b')(1, 2)
    lst1 = [1, 2, 3]
    assert to_namedtuple(lst1) == [1, 2, 3]
    lst2 = ['a', 'b', 'c']
    assert to_namedtuple(lst2) == ['a', 'b', 'c']
    lst3 = [dic1, dic2]


# Generated at 2022-06-13 20:33:46.402259
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for to_namedtuple"""
    import pytest
    from jsonschema import validate
    from flutils.jsonutils import load_json_schema
    # If the given type is of list or tuple, each item will be recursively
    # converted to a NamedTuple provided the items can be converted. Items
    # that cannot be converted will still exist in the returned object.
    # If the given type is of list the return value will be a new list. This
    # means the items are not changed in the given obj.
    schema = load_json_schema('to_namedtuple.schema.json')

# Generated at 2022-06-13 20:33:59.001584
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import flutils
    class TestException(Exception):
        pass
    obj = {
        'a': 1,
        'b': 2,
        'c': [3, 4],
        'd': {
            'e': 5,
            'f': 6,
            'g': 7,
            'h': [8, 9],
        },
    }
    expected = namedtuple('NamedTuple', ['a', 'b', 'c', 'd'])(
        1,
        2,
        [3, 4],
        namedtuple('NamedTuple', ['e', 'f', 'g', 'h'])(5, 6, 7, (8, 9))
    )
    actual = to_namedtuple(obj)
    assert actual == expected
    assert actual.a == 1

# Generated at 2022-06-13 20:34:10.620073
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import defaultdict
    from dataclasses import dataclass
    from typing import Dict, List, Tuple
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_dict

    @dataclass
    class Dummy:
        item: Dict[str, Any] = field(default_factory=dict)
        items: List[Dict[str, Any]] = field(default_factory=list)
        extra: Any = None

    d1 = dict(a=1, b=2)
    nt1 = to_namedtuple(d1)
    assert nt1.a == 1
    assert nt1.b == 2
    assert nt1._fields == ('a', 'b')


# Generated at 2022-06-13 20:34:14.791888
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Just a simple test
    dic = {'a': 1, 'b': 2, 'c': 3}
    nt = to_namedtuple(dic)
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c == 3
    dic = {'a': 'a', 'b': 2, 'c': 3}
    nt = to_namedtuple(dic)
    assert nt.a == 'a'
    assert nt.b == 2
    assert nt.c == 3
    nt = to_namedtuple(dic)
    assert nt.a == 'a'
    assert nt.b == 2
    assert nt.c == 3
    lst = [1, 2, 3]

# Generated at 2022-06-13 20:34:28.506664
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    from typing import List
    from types import SimpleNamespace
    import datetime as dt


# Generated at 2022-06-13 20:34:38.786801
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple
    dic = {'a': 1, 'b': 2}
    n = to_namedtuple(dic)
    assert isinstance(n, namedtuple)
    assert n.a == 1
    assert n.b == 2

    dic = {'a': 1, '_b': 2}
    n = to_namedtuple(dic)
    assert isinstance(n, namedtuple)
    assert n.a == 1
    with pytest.raises(AttributeError):
        print(n._b)

    dic = {'a': 1, '_b': 2}
    n = to_namedtuple(dic)
    assert isinstance(n, namedtuple)

# Generated at 2022-06-13 20:34:50.855028
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # dict to dict
    obj = {'a': 1, 'b': 2}
    assert to_namedtuple(obj) == obj
    # dict to namedtuple
    obj = {'a': 1, 'b': 2}
    assert to_namedtuple(obj).a == obj['a']
    assert to_namedtuple(obj).b == obj['b']
    # dict to namedtuple false
    obj = {'a': [1,2,3], 'b': 2}
    assert to_namedtuple(obj).a == obj['a']
    assert to_namedtuple(obj).b == obj['b']
    # dict to namedtuple nested
    obj = {'a': {'b': 1}, 'b': 2}
    assert to_namedtuple(obj).a.b == 1
   

# Generated at 2022-06-13 20:35:03.488484
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pformat

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    obj = SimpleNamespace(a=1, b=2)
    assert to_namedtuple(obj) == NamedTuple(a=1, b=2)

    # noinspection PyTypeChecker
    dic_list = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    expected = NamedTuple(a=1, b=2)
    actual = to_namedtuple(dic_list)[0]
    assert expected == actual
    assert type(actual) == type(expected)

    # noinspection PyTypeChecker

# Generated at 2022-06-13 20:35:14.269750
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {
        'a': {
            'b': 1,
            'c': [{
                'd': 2
            },{
                'e': 3
            }]
        }
    }
    # noinspection PyTypeChecker
    expected = OrderedDict([
        ('a', OrderedDict([
            ('b', 1),
            ('c', [OrderedDict([('d', 2)]), OrderedDict([('e', 3)])])
        ]))
    ])
    assert to_namedtuple(obj) == expected

    obj = {
        'a': 1,
        'b': 2
    }
    assert to_namedtuple(obj) == NamedTuple(a=1, b=2)


# Generated at 2022-06-13 20:35:28.809502
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        'a': 1,
        'b': 2
    }
    nt1 = to_namedtuple(dic)
    assert nt1.a == 1
    assert nt1.b == 2
    assert repr(nt1) == "NamedTuple(a=1, b=2)"
    assert str(nt1) == "NamedTuple(a=1, b=2)"

    nt2 = to_namedtuple(nt1)
    assert nt2.a == 1
    assert nt2.b == 2
    assert repr(nt2) == "NamedTuple(a=1, b=2)"
    assert str(nt2) == "NamedTuple(a=1, b=2)"


# Generated at 2022-06-13 20:35:41.258338
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple({'a': 1, '2': 2}) == namedtuple('NamedTuple', '2 a')(a=1, _2=2)
    assert to_namedtuple([{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}]) == [namedtuple('NamedTuple', 'a b')(a=1, b=2), namedtuple('NamedTuple', 'a b c')(a=3, b=4, c=5)]

# Generated at 2022-06-13 20:35:47.611952
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple(
        'NamedTuple',
        ('a', 'b')
    )(a=1, b=2)
    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert to_namedtuple((1, 2, 3)) == (1, 2, 3)
    assert to_namedtuple(
        {
            '_a': 1,
            'b': 2,
        }
    ) == namedtuple('NamedTuple', ('b', ))(b=2)

# Generated at 2022-06-13 20:35:54.901119
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    namesp = SimpleNamespace(a=1, b=2)
    assert to_namedtuple(namesp) == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    lst = [
        {'a': 1, 'b': 2},
        {'a': 3, 'b': 4},
    ]

# Generated at 2022-06-13 20:36:04.024092
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.testhelpers import (
        BaseTestCase,
        assert_namedtuple,
        assert_list_equal,
    )
    from flutils.namedtupleutils import to_namedtuple

    class Test(BaseTestCase):
        def test_to_namedtuple(self):
            
            # Test case: `dict` to `NamedTuple`
            x = to_namedtuple({'a': 1, 'b': 2, '3': 'three'})
            assert_namedtuple(
                x, size=2, members=['a', 'b'], values=[1, 2]
            )
            
            # Test case: `OrderedDict` to `NamedTuple`
            from collections import OrderedDict

# Generated at 2022-06-13 20:36:17.457741
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import Type
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple

    assert isinstance(to_namedtuple([]), list)
    assert isinstance(to_namedtuple(['abc']), list)
    assert isinstance(to_namedtuple(('abc', 'def')), tuple)
    assert isinstance(to_namedtuple({'a': 1, 'b': 2}), NamedTuple)
    assert isinstance(to_namedtuple({1: 'a', 2: 'b'}), NamedTuple)
    assert isinstance(to_namedtuple({1: 'a', 2: {'a': 1, 'b': 2}}), NamedTuple)

# Generated at 2022-06-13 20:36:29.372376
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(OrderedDict()) == namedtuple('NamedTuple', '')()
    assert to_namedtuple(OrderedDict({'a': 1})) == namedtuple('NamedTuple', 'a')(a=1)
    assert to_namedtuple(OrderedDict({'a': 1, 'b': 2})) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple(OrderedDict({'a': 1, 'b': 2})) != namedtuple('NamedTuple', 'b a')(a=1, b=2)

    assert to_namedtuple(dict()) == namedtuple('NamedTuple', '')()

# Generated at 2022-06-13 20:36:42.033610
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from typing import Dict, List, Tuple, Union
    from unittest import TestCase
    from unittest.mock import patch

    import flutils.namedtupleutils

    # noinspection PyProtectedMember
    flutils.namedtupleutils._to_namedtuple = to_namedtuple


# Generated at 2022-06-13 20:36:49.416939
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == ()
    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple(OrderedDict()) == NamedTuple()
    assert to_namedtuple({'x': 1, 'y': 2}) == NamedTuple(x=1, y=2)
    assert to_namedtuple(OrderedDict([('x', 1), ('y', 2)])) == NamedTuple(
        x=1,
        y=2,
    )
    assert to_namedtuple(SimpleNamespace(x=1, y=2)) == NamedTuple(x=1, y=2)

# Generated at 2022-06-13 20:36:56.368985
# Unit test for function to_namedtuple
def test_to_namedtuple():
    lst = [{'a': 1, 'b': 2}]
    got = to_namedtuple(lst)
    assert isinstance(got, list)
    assert isinstance(got[0], NamedTuple)
    assert got[0].a == 1
    assert got[0].b == 2


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:37:08.224505
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifier

    def _test_to_namedtuple(obj):
        v1 = to_namedtuple(obj)
        v2 = to_namedtuple(v1)
        assert v1 == v2
        assert type(v1) == type(v2)

    def _test_to_namedtuple_nested_dict(dic):
        v1 = to_namedtuple(dic)
        assert isinstance(v1, tuple)
        v2 = to_namedtuple(v1)
        assert v1 == v2
        assert type(v1) == type(v2)

   

# Generated at 2022-06-13 20:37:08.815421
# Unit test for function to_namedtuple
def test_to_namedtuple():
    pass

# Generated at 2022-06-13 20:37:16.613652
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict

    d = OrderedDict([('a',{'k': 1, 'k2': 'hello'}), ('b',2), ('c',3),('d',4)])
    expected = namedtuple('NamedTuple',['a','b','c','d'])(a=namedtuple('NamedTuple',['k','k2'])(k=1,k2='hello'),b=2,c=3,d=4)
    result = to_namedtuple(d)
    assert result == expected

# Generated at 2022-06-13 20:37:19.031012
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2



# Generated at 2022-06-13 20:37:30.341153
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple
    from types import SimpleNamespace

    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple)
    assert out.a == 1
    assert out.b == 2

    out = to_namedtuple({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    assert out.a == 1
    assert out.b == 2
    assert out.c == 3
    assert out.d == 4

    lst = [1, 2, 3]
    out = to_namedtuple(lst)
    assert isinstance(out, tuple)
    assert out == (1, 2, 3)

   

# Generated at 2022-06-13 20:37:39.780411
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3}) == NamedTuple(a=1, b=2, c=3)


test_to_namedtuple()

# Generated at 2022-06-13 20:37:49.911998
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from pprint import pprint

    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out == (1, 2)
    assert out.a == 1
    assert out.b == 2

    dic['c'] = (1, 2, 3)
    dic['d'] = {'e': 5, 'f': 6}
    out = to_namedtuple(dic)
    assert out == (1, 2, (1, 2, 3), (5, 6))
    assert out.d.e == 5
    assert out.d.f == 6

    dic['c'] = [1, 2, 3]
    out = to_namedtuple(dic)

# Generated at 2022-06-13 20:37:52.348230
# Unit test for function to_namedtuple
def test_to_namedtuple():
    print(to_namedtuple(('a', 'b'),'c'))


# Unit test to make sure it works:

# Generated at 2022-06-13 20:38:01.362782
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple

    assert isinstance(to_namedtuple({'a': 1, 'b': 2}), tuple)
    assert to_namedtuple({'a': 1, 'b': 2}) == (1, 2)
    assert to_namedtuple({'a': 1, 'b': 2}).a == 1
    assert to_namedtuple({'a': 1, 'b': 2}).b == 2

    assert isinstance(to_namedtuple([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]), list)

# Generated at 2022-06-13 20:38:12.127580
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class ToNamedTupleTests(unittest.TestCase):
        def test_not_started(self):
            # noinspection PyTypeChecker
            self.assertRaises(
                TypeError,
                to_namedtuple,
                'this is a string',
            )

        def test_dict(self):
            self.assertEqual(
                to_namedtuple({'a': 1, 'b': 2}),
                namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2),
            )

# Generated at 2022-06-13 20:38:21.990928
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert to_namedtuple(('a', 'b', 'c')) == ('a', 'b', 'c')
    assert to_namedtuple({'a': 'b'}) == NamedTuple(a='b')
    assert to_namedtuple({'a': 'b', 'c': 'd'}) == NamedTuple(a='b', c='d')
    assert to_namedtuple({'a': 'b', 'c': 'd', 1: 2}) == NamedTuple(a='b', c='d')

# Generated at 2022-06-13 20:38:33.995408
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import Counter, OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    from flutils.toolhelpers import get_annotations

    obj = [1, 2, 3, 4]
    ret = to_namedtuple(obj)
    assert type(obj) == type(ret)
    assert obj == ret

    obj = (1, 2, 3, 4)
    ret = to_namedtuple(obj)
    assert type(obj) == type(ret)
    assert obj == ret


# Generated at 2022-06-13 20:38:39.336479
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # simple test
    dic ={'a': 1, 'b': 2}
    print(to_namedtuple(dic))
    assert to_namedtuple(dic) ==  namedtuple('NamedTuple', ['a','b'])(a=1, b=2)
    # duplicate keys will be ignored
    dic ={'a': 1, 'b': 2, 'a': 3}
    print(to_namedtuple(dic))
    assert to_namedtuple(dic) ==  namedtuple('NamedTuple', ['a','b'])(a=1, b=2)


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:38:42.543299
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod(globs=globals())



# Generated at 2022-06-13 20:38:52.416268
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple({'b': 2, 'a': 1}) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple([]) == namedtuple('NamedTuple', '')()
    assert to_namedtuple([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple([{'b': 2, 'a': 1}, {'a': 3, 'b': 4}])

# Generated at 2022-06-13 20:39:07.865229
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2}
    nt = to_namedtuple(obj)
    assert nt.a == 1
    assert nt.b == 2
    obj = {'a': 1, 'b': 2, 'c': {'a': 1, 'b': 2}}
    nt = to_namedtuple(obj)
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c.a == 1
    assert nt.c.b == 2
    obj = (1, 2)
    nt = to_namedtuple(obj)
    assert nt[0] == 1
    assert nt[1] == 2
    obj = (1, (1, 2))
    nt = to_namedtuple(obj)
    assert nt

# Generated at 2022-06-13 20:39:19.939144
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Test that the function will only accept lists, tuples, dicts, or
    # types.SimpleNamespace
    class TestObj(object):
        pass
    obj1 = TestObj()
    with pytest.raises(TypeError):
        to_namedtuple(obj1)
    # Test that the function will return a list if given a list
    li = ['a', 'b', 'c']
    tup = to_namedtuple(li)
    assert isinstance(tup, list)
    assert tup == li
    # Test that the function will return a tuple if given a tuple
    tup = ('a', 'b', 'c')
    tup = to_namedtuple(tup)
    assert isinstance(tup, tuple)
    assert tup == ('a', 'b', 'c')
    #

# Generated at 2022-06-13 20:39:28.351193
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2, 'c': 3}
    named = to_namedtuple(obj)
    obj2 = {'c': 3, 'b': to_namedtuple({'d': 4, 'e': 5}), 'a': 1}
    named2 = to_namedtuple(obj2)
    obj3 = {'c': 3, 'a': 1}
    obj3['b'] = named2
    obj3['b'].b
    named3 = to_namedtuple(obj3)
    assert named == named2.b
    assert named2 == named3.b


if __name__ == "__main__":
    """Run module documentation tests."""
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 20:39:41.328223
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'this': 'is', 'a': 'test'}) == \
        namedtuple('NamedTuple', ('a', 'this'))(a='test', this='is')
    assert to_namedtuple({'this': 'is', 'a': 'test'}) != \
        namedtuple('NamedTuple', ('a', 'this'))(a='test', this='is_other')
    assert to_namedtuple({'this': 'is', 'a': 'test'}) != \
        namedtuple('NamedTuple', ('that', 'this'))(a='test', this='is')

# Generated at 2022-06-13 20:39:53.274627
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    from collections import OrderedDict

    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert hasattr(nt, 'a')
    assert getattr(nt, 'a') == 1

    dic = OrderedDict([('a', 1), ('b', 2)])
    nt = to_namedtuple(dic)
    assert hasattr(nt, 'a')
    assert hasattr(nt, 'b')
    assert getattr(nt, 'a') == 1
    assert getattr(nt, 'b') == 2

    dic = {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-13 20:39:59.352621
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyUnresolvedReferences
    from flutils.test.namedtupleutils import unit_tests
    unit_tests.test_to_namedtuple(to_namedtuple)


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:40:08.988693
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pandas as pd

    def assert_to_namedtuple(obj, expected):
        out = to_namedtuple(obj)
        if out != expected:
            print(out)
            print(expected)
        assert out == expected

    assert_to_namedtuple(
        [],
        []
    )

    assert_to_namedtuple(
        [{}],
        [NamedTuple(**{})]
    )

    assert_to_namedtuple(
        [{'a': None}, {'b': None}],
        [NamedTuple(a=None), NamedTuple(b=None)]
    )


# Generated at 2022-06-13 20:40:19.788492
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from io import StringIO
    import sys
    import unittest

    # noinspection SpellCheckingInspection
    class A(unittest.TestCase):
        def test__to_namedtuple(self):
            errmsg = (
                "Can convert only 'list', 'tuple', 'dict' to a NamedTuple; "
                "got: (%r) %s" % (type(''), '')
            )
            with self.assertRaises(TypeError) as cm:
                to_namedtuple('')
            self.assertEqual(cm.exception.msg, errmsg)
            self.assertEqual(cm.exception.args, (errmsg,))


# Generated at 2022-06-13 20:40:27.129489
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.namedtupleutils import to_namedtuple

    def test_to_namedtuple_invalid_type():
        from flutils.miscutils import get_calling_function
        from flutils.validators import validate_identifier

        with pytest.raises(TypeError) as excinfo:
            to_namedtuple(1)
        assert 'Can convert only' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            to_namedtuple(1.)
        assert 'Can convert only' in str(excinfo.value)

        obj = get_calling_function()
        with pytest.raises(TypeError) as excinfo:
            to_namedtuple(obj)
        assert 'Can convert only' in str(excinfo.value)

# Generated at 2022-06-13 20:40:38.060601
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifier
    from types import SimpleNamespace

    # General tests
    dic = {'a': 1, 'b': 2, }  # type: ignore[misc]
    dic = to_namedtuple(dic)
    assert dic == ('a', 'b')
    assert dic.a == 1
    assert dic.b == 2
    dic = {'a': 1, 'b': 2, '_c': 3}
    dic = to_namedtuple(dic)
    assert dic == ('a', 'b')
    assert dic.a == 1
    assert dic.b == 2
    assert not hasattr(dic, '_c')

# Generated at 2022-06-13 20:40:55.239042
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from sys import version_info
    from pprint import pprint
    from dataclasses import dataclass
    from unittest.mock import Mock
    from flutils.namedtupleutils import to_namedtuple
    from flutils.testing.helpers import raises, clean_exc_info

    # https://www.python.org/dev/peps/pep-0563/#naming-requirements-to-be-used-as-keys-in-a-mapping-or-as-a-namedtuple-field-name

# Generated at 2022-06-13 20:41:07.469983
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import (
        to_namedtuple,
    )
    from flutils.tests.generic import (
        TEST_DATA_DIR,
        TEST_DATA_FILES,
        ResourceTest,
    )
    from flutils.tests.testdata import (
        LIST_NESTED,
        NESTED,
    )


# Generated at 2022-06-13 20:41:16.852502
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    tup = (1, 2)
    lis = [1, 2]
    ntup = namedtuple('_', 'a b')(a=1, b=2)
    sns = SimpleNamespace(a=1, b=2)
    args = [
        [ntup, tup],
        [dic, dic],
        [lis, lis],
        [sns, dic],
    ]
    for in_, out in args:
        assert to_namedtuple(in_) == out


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:41:26.888018
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import datetime
    from flutils.namedtupleutils import to_namedtuple
    dic = {
        'a': 1,
        'b': 2,
        'c': {
            'd': {
                'd1': 11,
                'd2': 22,
            },
            'e': {
                'e1': 111,
                'e2': 222,
            },
        },
        'f': datetime.datetime.utcnow(),
        'g': datetime.date.today(),
        'h': datetime.time.min,
    }
    nt = to_namedtuple(dic)
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c.d.d1 == 11
    assert nt.c.d.d2

# Generated at 2022-06-13 20:41:37.934003
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test specific cases."""

    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from types import SimpleNamespace

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)

    dic = OrderedDict({'a': 1, 'b': 2})
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)

    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    assert to_namedtuple({}) == namedtuple('NamedTuple', '')()


# Generated at 2022-06-13 20:41:43.148944
# Unit test for function to_namedtuple
def test_to_namedtuple():
    a = [1, 2, 3]
    assert(to_namedtuple(a) == a)
    d = {'a': 1, 'b': 2}
    assert(to_namedtuple(d) == d)
    return True

# Unit test of test_to_namedtuple

# Generated at 2022-06-13 20:41:58.011899
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple

    def _to_dict(
            obj: Any
    ) -> Union[List, Tuple, OrderedDict, str]:
        if hasattr(obj, 'capitalize'):
            return cast(str, obj)
        if hasattr(obj, 'keys'):
            obj = cast(Union[List, Tuple], obj)
            dic: OrderedDict = OrderedDict()
            for val in obj:
                dic[val] = val
            return dic
        if hasattr(obj, '_fields'):
            obj = cast(NamedTuple, obj)
            dic: Dict = obj._asdict()
            return dic

# Generated at 2022-06-13 20:42:07.390991
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple([dic, dic]) == [
        namedtuple('NamedTuple', 'a b')(a=1, b=2),
        namedtuple('NamedTuple', 'a b')(a=1, b=2),
    ]

# Generated at 2022-06-13 20:42:17.682262
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # list of lists
    dic = {'a': [1, 2], 'b': [3, 4]}
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)
    assert isinstance(out.a, list)
    assert isinstance(out.a[0], int)
    assert isinstance(out.a[1], int)
    assert isinstance(out.b, list)
    assert isinstance(out.b[0], int)
    assert isinstance(out.b[1], int)

    # list of tuples
    dic = {'a': (1, ), 'b': (3, 4)}
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)
    assert isinstance(out.a, tuple)
   

# Generated at 2022-06-13 20:42:28.271992
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test function namedtupleutils.to_namedtuple."""
    # -------------------------------------------------------------------------
    from copy import deepcopy


    class MyObj:
        def __init__(self):
            self.a = 1
            self.b = 2


    obj = MyObj()
    data = {'c': obj, 'd': {'e': obj, 'f': [obj, obj], 'g': (obj, obj)}}
    data = deepcopy(data)
    namedt = to_namedtuple(data)
    # noinspection PyTypeChecker
    assert namedt.d.e is namedt.d.f[0]
    # noinspection PyTypeChecker
    assert namedt.d.g[0] is namedt.d.e
    # noinspection PyTypeChecker
    assert namedt.d