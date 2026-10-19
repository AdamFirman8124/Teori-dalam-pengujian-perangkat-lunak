

# Generated at 2022-06-13 20:32:52.933936
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    from collections import OrderedDict
    from flutils.namedtupleutils import (
        to_namedtuple,
        _to_namedtuple,
    )
    from types import SimpleNamespace
    from typing import Dict, List, Tuple

    # Test for Basic conversions
    dic: Dict[str, int] = {'a': 1, 'b': 2}
    tup: Tuple[int, int] = (1, 2)
    ntup: Tuple[int, int] = (1, 2)
    sns = SimpleNamespace(a=1, b=2)
    odic: OrderedDict = OrderedDict({'a': 1, 'b': 2})
    assert to_namedtuple(dic) == nt

# Generated at 2022-06-13 20:33:04.657161
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 'abc'}) == NamedTuple(a=1, b='abc')

    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple((1, 2)) == (1, 2)
    assert to_namedtuple(OrderedDict({'a': 1, 'b': 2})) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict((('b', 2), ('a', 1)))) == NamedTuple(b=2, a=1)

# Generated at 2022-06-13 20:33:13.899275
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple
    from collections import OrderedDict

    obj = {
        'a': 1,
        'b': 2
    }
    assert to_namedtuple(obj) == namedtuple('NamedTuple', 'a b')(
        a=1,
        b=2
    )

    obj = {
        'a': 1,
        'b': 'val',
    }
    assert to_namedtuple(obj) == namedtuple('NamedTuple', 'a b')(
        a=1,
        b='val'
    )

    obj = {
        1: 1,
        'b': 2
    }

# Generated at 2022-06-13 20:33:17.463842
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:33:24.907480
# Unit test for function to_namedtuple
def test_to_namedtuple():
    list_ = ['a', {'b': 1, 'c': 2}, 'd']
    out = to_namedtuple(list_)
    assert out == ['a', NamedTuple(b=1, c=2), 'd']


if __name__ == '__main__':
    import os
    import sys
    pytest_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, pytest_dir)
    import pytest  # noqa: E402
    pytest.main([pytest_dir, '-v'])

# Generated at 2022-06-13 20:33:31.327972
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:33:33.846561
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict

    items = OrderedDict([('id', 1), ('name', '_name'), ('value', '~value')])
    res = to_namedtuple(items)
    assert res.id == 1
    assert res.name == '_name'
    assert res.value == '~value'


# Generated at 2022-06-13 20:33:36.455490
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod(verbose=False)
    assert True

# Generated at 2022-06-13 20:33:40.488501
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import json

    from flutils.namedtupleutils import to_namedtuple

    json_str = """{
        "a": 1,
        "b": {
            "c": "d"
        },
        "e": [
            "f",
            "g"
        ]
    }"""
    expected = (
        "NamedTuple(a=1, b=NamedTuple(c='d'), e=[NamedTuple(f='f', g='g')])"
    )
    expected = json.loads(expected.replace("'", '"'))

    assert to_namedtuple(json.loads(json_str)) == expected

# Generated at 2022-06-13 20:33:48.629375
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.dotdict import DotDict
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from types import SimpleNamespace

    a_dict = {'a': 1, 'c': 2}
    assert to_namedtuple(a_dict) == to_namedtuple(a_dict.copy())
    assert isinstance(to_namedtuple(a_dict), namedtuple('NamedTuple', 'a c'))
    a_ordered_dict = OrderedDict(a=1, c=2, b=3)
    assert to_namedtuple(a_ordered_dict) == to_namedtuple(a_dict)
    assert to_namedtuple(a_ordered_dict) != to_namedtuple(a_ordered_dict.copy())


# Generated at 2022-06-13 20:34:01.149261
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Setup
    dic_obj = {'a': 1, 'b': 2}
    ordered_dic = OrderedDict(a=1, b=2, c=3)

    # Execute
    named_tuple1 = to_namedtuple(dic_obj)
    named_tuple2 = to_namedtuple(ordered_dic)

    # Assert
    assert isinstance(named_tuple1, namedtuple('NamedTuple', 'a b'))
    assert isinstance(named_tuple2, namedtuple('NamedTuple', 'a b c'))
    assert named_tuple1.a == 1
    assert named_tuple1.b == 2
    assert named_tuple2.a == 1
    assert named_tuple2.b == 2
    assert named_

# Generated at 2022-06-13 20:34:12.275075
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Basic usage
    print('\nBasic usage')
    dic = {'a': 1, 'b': 2}
    named = to_namedtuple(dic)
    print(named)

    # Values that are dictionaries get converted
    print('\nValues that are dictionaries get converted')
    dic = {'a': 1, 'b': 2, 'c': {'e': 8}}
    named = to_namedtuple(dic)
    print(named)

    # Recursive
    print('\nRecursive')
    dic = {'a': 1, 'b': 2, 'c': {'e': 8, 'f': {'h': 11}}}
    named = to_namedtuple(dic)
    print(named)

    # Items that do not convert are not changed

# Generated at 2022-06-13 20:34:23.529055
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    dic = {'first': 1, 'second': 2}
    nt = to_namedtuple(dic)
    assert nt.first == 1
    assert nt.second == 2
    ordic = OrderedDict(a=1, b=2)
    nt = to_namedtuple(ordic)
    assert nt.a == 1
    assert nt.b == 2
    assert nt[0] == 1
    assert nt[1] == 2
    tup = (0, OrderedDict(a=1, b=2))
    nt = to_namedtuple(tup)
    assert nt[0]

# Generated at 2022-06-13 20:34:30.292672
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    class TestToNamedTuple(unittest.TestCase):
        def test_convert_to_mapping_ndt(self):
            NOT_ALLOWED = [10, True, None, tuple(), dict(), list(), namedtuple('NamedTuple', 'a b c d')(1, 2, 3, 4)]
            MAPP = {'a': 1, 'b': 2, 'c': 3}
            for val in NOT_ALLOWED:
                with self.subTest(val=val):
                    with self.assertRaises(TypeError):
                        to_namedtuple(val)
            exp_result = namedtuple('NamedTuple', 'a b c')(a=1, b=2, c=3)

# Generated at 2022-06-13 20:34:33.826405
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    
    data = dict(a=1, b=2)
    out = to_namedtuple(data)
    pprint(out)

# Generated at 2022-06-13 20:34:40.954592
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(dict(a=1, b=2)) == namedtuple('namedtuple', 'a b')(a=1, b=2)
    assert to_namedtuple(OrderedDict(a=1, b=2)) == namedtuple('namedtuple', 'a b')(a=1, b=2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == namedtuple('namedtuple', 'a b')(a=1, b=2)
    assert to_namedtuple([dict(a=1, b=2)]) == [namedtuple('namedtuple', 'a b')(a=1, b=2)]

# Generated at 2022-06-13 20:34:52.415441
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from datetime import date
    from typing import NamedTuple
    import doctest

    class Person(NamedTuple):
        name: str
        age: int

    class Person2(NamedTuple):
        person: NamedTuple

    class Person3(NamedTuple):
        person: Person2

    class Person4(NamedTuple):
        person: Person3

    class Person5(NamedTuple):
        person: Person4

    class Person6(NamedTuple):
        person: Person5

    class Person7(NamedTuple):
        person: Person6

    class Person8(NamedTuple):
        person: Person7

    class Person9(NamedTuple):
        person: Person8


# Generated at 2022-06-13 20:35:04.262389
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import random
    import string
    import unittest
    from flutils.namedtupleutils import to_namedtuple
    from flutils.textutils import is_identifier

    # noinspection PyArgumentList
    class TestFunc(unittest.TestCase):
        """Test the ``to_namedtuple`` function."""

        def test_types_fail(self):
            # Test the types that cannot be converted
            self.assertRaises(TypeError, to_namedtuple, random.random())
            self.assertRaises(TypeError, to_namedtuple, random)
            self.assertRaises(TypeError, to_namedtuple, string)
            self.assertRaises(TypeError, to_namedtuple, TestFunc)

# Generated at 2022-06-13 20:35:17.130913
# Unit test for function to_namedtuple
def test_to_namedtuple():
    def _dict_compare(d1: Mapping, d2: Mapping):
        if not isinstance(d1, OrderedDict) or not isinstance(d2, OrderedDict):
            d1 = OrderedDict(sorted(d1.items()))
            d2 = OrderedDict(sorted(d2.items()))
        d1_items = set([item for item in d1.items()])
        d2_items = set([item for item in d2.items()])
        assert d1_items == d2_items

    od = OrderedDict(a=1, b=2, c=3)
    _dict_compare(
        OrderedDict(a=1, b=2), to_namedtuple(od)
    )


# Generated at 2022-06-13 20:35:31.052449
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple('a') == 'a'
    assert to_namedtuple(123) == 123
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple('a=1, b=2')
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(SimpleNamespace(a=1, b=2))
    assert to_namedtuple(('123',)) == to_namedtuple('a=123')
    assert to_namedtuple(('123', '456')) == to_namedtuple('a=123, b=456')

# Generated at 2022-06-13 20:35:44.366497
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_dict

    dic = {
        'key1': {
            'key2': {
                'key3': 'value3',
                'key4': 'value4',
            },
            'key5': {
                'key6': 'value6',
            },
        },
    }

# Generated at 2022-06-13 20:35:53.391400
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase

    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict

    class TestToNamedtuple(TestCase):

        # noinspection PyMethodMayBeStatic,PyTypeChecker
        def test_to_namedtuple(self):
            dic = {'a': 1, '_b': 2}
            dic2 = {'c': 3}
            dic['d'] = dic2
            self.assertNotEqual(to_namedtuple(dic)['d'], dic2)
            self.assertEqual(to_namedtuple(dic)['a'], 1)
            dic2['e'] = to_namedtuple(dic)

# Generated at 2022-06-13 20:36:03.288668
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    dic = {'a': 1, 'b': 2}
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b == 2
    assert len(obj) == 2

    dic = OrderedDict()
    dic['a'] = 1
    dic['b'] = 2
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b == 2
    assert len(obj) == 2

    obj = SimpleNamespace(a=1, b=2)
    obj = to_namedtuple(obj)
    assert obj.a == 1
    assert obj.b == 2
    assert len(obj) == 2


# Generated at 2022-06-13 20:36:15.954295
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.fldictfuncs import map_dict_keys
    from typing import NamedTuple
    from collections import (
        OrderedDict,
        Mapping,
        Sequence,
    )

    # noinspection PyTypeChecker,PyArgumentList
    TestCase = namedtuple('TestCase', 'name, obj, expected, typ')
    TestSuite = List[TestCase]


# Generated at 2022-06-13 20:36:22.244375
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import Dict
    from collections import (  # noqa: F401
        defaultdict,
        deque,
    )
    from collections.abc import Sequence  # noqa: F401
    from flutils.namedtupleutils import to_namedtuple
    from flutils.misc import repr_list
    from types import SimpleNamespace

# Generated at 2022-06-13 20:36:33.033203
# Unit test for function to_namedtuple
def test_to_namedtuple():
    tests_passed = 0
    # Test a list of dicts and dict keys that become attribute names.
    # Test a dict should become a namedtuple.
    try:
        dic = {'a': 1, 'b': 2}
        assert to_namedtuple(dic) == NamedTuple(a=1, b=2)
        tests_passed += 1
    except:
        print('Failed to_namedtuple(dic)')
    # Test a list of dicts and dict keys that become attribute names.
    # Test dicts that are not converted to namedtuples.

# Generated at 2022-06-13 20:36:43.523747
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple((1, 2, 3)) == (1, 2, 3)
    assert to_namedtuple([1, 2, {'a': 1, 'b': 2}]) == [1, 2, NamedTuple(a=1, b=2)]
    assert to_namedtuple([1, 2, {'a': 1, 'b': 2}])[2] == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict((('a', 1), ('b', 2)))) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict((('b', 2), ('a', 1))))

# Generated at 2022-06-13 20:36:52.975834
# Unit test for function to_namedtuple
def test_to_namedtuple():
    def _compare_dicts(a: Mapping, b: Mapping) -> bool:
        assert isinstance(a, Mapping)
        assert isinstance(b, Mapping)
        assert isinstance(a.keys(), Sequence)
        assert isinstance(b.keys(), Sequence)
        assert isinstance(a.keys(), Sequence)
        assert isinstance(b.keys(), Sequence)
        assert set(a.keys()) == set(b.keys())
        for key in a:
            assert isinstance(a[key], Any)
            assert isinstance(b[key], Any)
            if isinstance(a[key], Mapping):
                assert _compare_dicts(a[key], b[key])
                continue
            assert a[key] == b[key]
        return True


# Generated at 2022-06-13 20:37:04.208491
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test to_namedtuple()."""

    import flutils.namedtupleutils as ntu
    import datetime as dt

    ##################################################################
    #                    dict
    ##################################################################

    # dict
    inst = {
        'name': 'George',
        'age': 42,
        'country': 'The United States',
        'state': 'TX'
    }
    nt = ntu.to_namedtuple(inst)
    assert len(nt._fields) == 4
    assert nt.name == 'George'
    assert nt.age == 42
    assert nt.country == 'The United States'
    assert nt.state == 'TX'

    ##################################################################
    #                    OrderedDict
    ##################################################################

    # OrderedDict
    from collections import Ordered

# Generated at 2022-06-13 20:37:16.153507
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(None) is None
    assert to_namedtuple(OrderedDict()) == NamedTuple()
    assert to_namedtuple(dict()) == NamedTuple()
    assert to_namedtuple(()) == NamedTuple()
    assert to_namedtuple(list()) == []
    assert to_namedtuple(SimpleNamespace()) == NamedTuple()

    assert to_namedtuple((1, 2)) == NamedTuple(1, 2)
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple([[1, 2], [3, 4]]) == [NamedTuple(1, 2), NamedTuple(3, 4)]

# Generated at 2022-06-13 20:37:33.228960
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from datetime import datetime
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple

    # start_time = datetime.now()
    # print(
    #     'obj:',
    #     to_namedtuple(obj),
    #     '\n',
    #     'took:',
    #     datetime.now() - start_time
    # )

    obj = {'a': 1, 'b': 2}
    assert to_namedtuple(obj) == namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)

    obj = {'a': 1, 'b': {'c': 1, 'd': 2}}
    assert to_namedtuple(obj) == named

# Generated at 2022-06-13 20:37:40.952763
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert isinstance(nt, namedtuple('NamedTuple', 'a b'))
    assert nt.a == 1
    assert nt.b == 2
    assert nt[0] == nt.a
    assert nt[1] == nt.b


# Generated at 2022-06-13 20:37:50.057860
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert repr(to_namedtuple(1)) == '1'
    assert repr(to_namedtuple('foo')) == "'foo'"
    assert repr(to_namedtuple([])) == '()'
    assert repr(to_namedtuple(0.1)) == '0.1'
    assert repr(to_namedtuple(None)) == 'None'
    assert repr(to_namedtuple((1, 'foo'))) == "NamedTuple(0=1, 1='foo')"
    assert repr(to_namedtuple(((1, 'foo'), (2, 'bar')))) == (
        "NamedTuple(0=NamedTuple(0=1, 1='foo'), "
        "1=NamedTuple(0=2, 1='bar'))"
    )
    assert repr

# Generated at 2022-06-13 20:38:00.037805
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)
    lst = [1, 2]
    assert to_namedtuple(lst) == [1, 2]
    lst = [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]
    assert to_namedtuple(lst) == [NamedTuple(a=1, b=2), NamedTuple(a=1, b=2)]
    lst = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]

# Generated at 2022-06-13 20:38:11.700844
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace

    # noinspection PyUnusedLocal,PyShadowingNames
    def test_value(val: Union[NamedTuple, Tuple, List]):
        assert isinstance(val, (NamedTuple, Tuple, List))

    # noinspection PyUnresolvedReferences,PyUnusedLocal,PyShadowingNames
    def test_key_value(val: NamedTuple):
        assert hasattr(val, 'a')
        assert hasattr(val, 'b')
        assert hasattr(val, 'c')
        assert val.a == 1
        assert val.b == 2
        assert val.c == 3

    # noinspection PyUnresolvedReferences,PyUnusedLocal,PyShadowingNames

# Generated at 2022-06-13 20:38:21.894349
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import json

    dic = {"key1":'value1',"key2":'value2',"key3":'value3'}
    named_tuple = to_namedtuple(dic)
    print("Each key in that dictionary becomes an attribute of a NamedTuple")
    print("Here is the NamedTuple: ", named_tuple)
    print("Here are the keys of the NamedTuple:", named_tuple._fields)

    list_of_dics = [{"key11":'value11',"key12":'value12',"key13":'value13'},
                    {"key21":'value21',"key22":'value22',"key23":'value23'},
                    {"key31":'value31',"key32":'value32',"key33":'value33'}]

# Generated at 2022-06-13 20:38:36.728021
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest.mock

    bites: List[Dict[str, str]] = [
        {'type': 'Cookie', 'points': 5, '_id': 1},
        {'type': 'Candy Bar', 'points': 10, '_id': 2},
        {'type': 'Brownie', 'points': 15, '_id': 3},
    ]
    Target = namedtuple('Target', ['name', 'bites'])
    target = Target('Sue', bites)
    out = to_namedtuple(target)
    assert out.name == 'Sue'
    assert out.bites[0]._id == 1
    assert len(out.bites) == len(bites)

    bite = namedtuple('Bite', ['type', 'points', '_id'])

# Generated at 2022-06-13 20:38:49.221206
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import os
    import unittest
    import warnings

    # noinspection PyUnusedLocal
    class ToNamedtupleTestCase(unittest.TestCase):

        def test_to_namedtuple(self):
            dic = {'a': 1, 'b': 2}
            result = to_namedtuple(dic)
            self.assertEqual(result.a, 1)
            self.assertEqual(result.b, 2)

            dic = {'b': 2, 'a': 1}
            result = to_namedtuple(dic)
            self.assertEqual(result.a, 1)
            self.assertEqual(result.b, 2)

            dic = {'b': 2, 'a': 1, 'c': 3}

# Generated at 2022-06-13 20:39:00.865684
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # simple
    dic = {'a': 1, 'b': 2}
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b == 2

    # nested
    dic = {
        'a': 1,
        'b': {'b1': 21, 'b2': 22},
        'c': 3,
    }
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b.b1 == 21
    assert obj.b.b2 == 22
    assert obj.c == 3

    # custom
    a = namedtuple('A', 'a b c')(1, 2, 3)
    assert to_namedtuple(a) == a

    # list

# Generated at 2022-06-13 20:39:11.670142
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    dic = {'name': 'alice', 'age': 38, 'location': 'Seattle', '_secret': 'foo'}
    expected = namedtuple('Test', ['name', 'age', 'location'])(name='alice', age=38, location='Seattle')
    obj = to_namedtuple(dic)
    assert obj == expected

    expected = namedtuple('Test', ['name', 'age', 'location'])(name='alice', age=38, location='Seattle')
    obj = to_namedtuple(OrderedDict(dic))
    assert obj == expected


# Generated at 2022-06-13 20:39:28.249389
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = dict(a=1, b=2)
    assert to_namedtuple(dic) == dic
    assert to_namedtuple(dic) == (1, 2)
    li = [dic]
    assert to_namedtuple(li) == [dic]
    assert to_namedtuple(li) == [(1, 2)]
    assert to_namedtuple(li) == [NamedTuple(a=1, b=2)]


# Generated at 2022-06-13 20:39:41.002683
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pytest import raises, approx
    from collections import namedtuple
    from flutils.namedtupleutils import to_namedtuple
    # Dictionaries
    d = to_namedtuple({'a': 1, 'b': 2})
    assert isinstance(d, namedtuple)
    assert d.a == 1
    assert d.b == 2
    d = to_namedtuple({'a': 1, 'b': 2, '_c': 3})
    assert isinstance(d, namedtuple)
    assert d.a == 1
    assert d.b == 2
    with raises(AttributeError):
        assert d._c
    d = to_namedtuple({'a': 1, 'b': 2, 'C': 3})
    assert isinstance(d, namedtuple)
    assert d.a == 1

# Generated at 2022-06-13 20:39:52.973828
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        defaultdict,
        OrderedDict,
    )
    from types import SimpleNamespace

    # List
    li1 = []
    assert to_namedtuple(li1) == []

    li1 = ['a', 'b']
    assert to_namedtuple(li1) == li1

    li1 = [('a', 1), ('b', 2), ('c', 3)]
    assert to_namedtuple(li1) == [('a', 1), ('b', 2), ('c', 3)]

    li1 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]

# Generated at 2022-06-13 20:40:05.734638
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from typing import (
        List,
        NamedTuple
    )
    from unittest import TestCase
    namedtuple_ = namedtuple
    SimpleNamespace_ = SimpleNamespace
    items = [(1, 2), (3, 4), (5, 6)]
    items_namedtuple = namedtuple_('NamedTuple', 'a b')(1, 2)
    items_namespace = SimpleNamespace_(a=1, b=2)
    items_dict = {'a': 1, 'b': 2}
    items_odict = OrderedDict(a=1, b=2)
    items_list = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    items_

# Generated at 2022-06-13 20:40:16.629535
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    assert isinstance(to_namedtuple(dic), namedtuple('NamedTuple', ['a', 'b']))
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    dic = {'a': 1, 'b': 2, '_csrf': 'abcd'}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    dic = OrderedDict([('a', 1), ('b', 2), ('_csrf', 'abcd')])
   

# Generated at 2022-06-13 20:40:25.646040
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pytest import raises
    from tests.common import _temp_namedtuple

    case1 = SimpleNamespace()
    with raises(TypeError):
        to_namedtuple(case1)

    case2 = List = _temp_namedtuple('List', 'a, b')
    case: Union[List, NamedTuple] = to_namedtuple(case2)
    assert case == case2

    case3 = Tuple = _temp_namedtuple('Tuple', 'a, b')
    case: Union[Tuple, NamedTuple] = to_namedtuple(case3)
    assert case == case3

    case4 = List = _temp_namedtuple('List', 'a, b')
    case5 = Tuple = _temp_namedtuple('Tuple', 'c, d')
    case: Union

# Generated at 2022-06-13 20:40:33.414024
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert isinstance(to_namedtuple({'a': 1, 'b': 2}), namedtuple)
    assert repr(to_namedtuple([1,2,3])) == repr([1,2,3])
    assert repr(to_namedtuple((1,2,3))) == repr((1,2,3))
    assert repr(to_namedtuple(((1,2,3),(4,5,6)))) == repr(((1,2,3),(4,5,6)))
    assert repr(to_namedtuple({'a': 1, 'b': {'c':{'d':2}}},)) == repr(NamedTuple(a=1, b=NamedTuple(c=NamedTuple(d=2))))

    class TestClass:
        pass

# Generated at 2022-06-13 20:40:39.924707
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # Check TypeError on used of non-allowed type
    try:
        to_namedtuple(True)
    except TypeError:
        pass
    except Exception as err:
        raise err

    try:
        from flask import json
    except ImportError:
        try:
            import json
        except ImportError:
            pass

    try:
        jsn = json.dumps({'a': 1, 'b': 2})
        assert to_namedtuple(json.loads(jsn)) == to_namedtuple({'a': 1, 'b': 2})
    except NameError:
        pass

    # Check on a 2-level nested dictionary
    dic = {'a': 1, 'b': 2, 'sub': {'a': 1, 'b': 2}}
    named = to_namedtuple(dic)

# Generated at 2022-06-13 20:40:43.639809
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": {
            "d1": "test",
            "d2": "test2"
        }
    }
    assert(to_namedtuple(dic) == {'a': 1, 'b': 2})

# Generated at 2022-06-13 20:40:49.429471
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test to_namedtuple function from the namedtupleutils.py module."""
    from collections import namedtuple
    dic = {'a': 1, 'b': 2}
    act = to_namedtuple(dic)
    exp = namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert act == exp



# Generated at 2022-06-13 20:41:25.683999
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == (1, 2)
    assert to_namedtuple(OrderedDict(a=1, b=2)) == (1, 2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == (1, 2)
    assert to_namedtuple(('a', 1)) == (1,)
    assert to_namedtuple(('a', 1, 'b', 2)) == (1, 2)
    assert to_namedtuple(('a', 1, 'b', OrderedDict(c=3, d=4))) == (1, 3, 4)
    assert to_namedtuple(('a', 1, 'b', SimpleNamespace(c=3, d=4))) == (1, 3, 4)
   

# Generated at 2022-06-13 20:41:36.235368
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(OrderedDict(a=1, b=2))
    assert to_namedtuple({'a': 1, 'b': 2}) != to_namedtuple(OrderedDict(a=1, b=3))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(SimpleNamespace(a=1, b=2))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(SimpleNamespace(b=2, a=1))

# Generated at 2022-06-13 20:41:47.672393
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from collections import OrderedDict
    from types import SimpleNamespace
    import flutils.namedtupleutils as m
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifier

    # noinspection PyProtectedMember
    from flutils.namedtupleutils import _to_namedtuple
    from flutils.validators import validate_identifier

    # noinspection PyProtectedMember
    from flutils.namedtupleutils import _to_namedtuple

    # noinspection PyUnusedLocal
    def test_convert_list():
        from flutils.namedtupleutils import to_namedtuple

        res = to_namedtuple([1, 2, 3, 4, 5])
        assert isinstance(res, list)
        assert res

# Generated at 2022-06-13 20:41:58.353351
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        'a': 1,
        'b': (1, 2),
        'c': {
            'd': 3,
            'e': [4, 5],
        },
        'f': [
            {
                'g': 6,
                'h': 7,
            },
            [
                {
                    'i': 8,
                    'j': 9,
                },
            ]
        ],
        'k': [
            {
                'l': 10,
                'm': 11,
            },
            [
                {
                    'n': 12,
                    'o': 13,
                },
            ]
        ],
    }

    out = to_namedtuple(dic)

    assert hasattr(out, 'c')
    assert hasattr(out, 'f')

# Generated at 2022-06-13 20:42:11.012282
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    OrderedDic = OrderedDict
    from types import SimpleNamespace
    from typing import Dict, List, NamedTuple, Tuple, Union
    from types import SimpleNamespace
    from typing import Dict, List, NamedTuple, Tuple, Union
    PassThrough = Union[Dict, List, NamedTuple, SimpleNamespace, Tuple]
    PassThroughDic = Union[Dict, OrderedDict]
    # noinspection SpellCheckingInspection

# Generated at 2022-06-13 20:42:21.698414
# Unit test for function to_namedtuple
def test_to_namedtuple():


    # If the given type is of list, the return value will be a new list.
    assert to_namedtuple([{'a': 1, 'b': 2}, 1]) == [
        NamedTuple(a=1, b=2),
        1,
    ]
    assert isinstance(to_namedtuple([{'a': 1, 'b': 2}, 1]), list)
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple([dic, 1]) == [
        NamedTuple(a=1, b=2),
        1,
    ]
    dic.clear()
    assert dic == {}


    # If the given type is of Mapping, keys that can be proper identifiers will
    # become attributes on the returned NamedTuple.
    assert to_namedtuple

# Generated at 2022-06-13 20:42:30.437570
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    error_msg = "Can convert only 'list', 'tuple', 'dict' to a NamedTuple; "
    # noinspection PyUnresolvedReferences
    wrong_type = pytest.param(5, marks=pytest.mark.xfail(raises=TypeError))
    # noinspection PyUnresolvedReferences
    wrong_type = pytest.param(5.5, marks=pytest.mark.xfail(raises=TypeError))
    for item in [wrong_type, True, False, None]:
        with pytest.raises(TypeError) as excinfo:
            to_namedtuple(item)
        assert error_msg in str(excinfo.value)

    # Test List of List

# Generated at 2022-06-13 20:42:40.894040
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from types import SimpleNamespace
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == \
        namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple(OrderedDict([('b', 2), ('a', 1)])) == \
        namedtuple('NamedTuple', ['b', 'a'])(b=2, a=1)
    assert to_namedtuple(OrderedDict([('b', 2), ('_a', 1)])) == \
        namedtuple('NamedTuple', ['b'])(b=2)
    assert to_namedtuple(OrderedDict([('b', 2), ('a-', 1)])) == \
        named