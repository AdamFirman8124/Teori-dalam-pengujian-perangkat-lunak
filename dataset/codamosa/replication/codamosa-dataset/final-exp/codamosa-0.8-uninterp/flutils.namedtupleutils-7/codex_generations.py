

# Generated at 2022-06-13 20:32:53.036172
# Unit test for function to_namedtuple
def test_to_namedtuple():
    if __name__ == '__main__':
        from flutils.namedtupleutils import to_namedtuple
        from flutils.printing import dict_to_str, obj_to_str
        from flutils.miscutils import sort_dict
        from flutils.resutils import get_data
        from flutils.simplenamespace import SimpleNamespace

        _ = to_namedtuple

        def get_data_obj(
                objtype: str,
                name: str
        ) -> Any:
            data = get_data(objtype, name)
            obj = eval(data)
            return obj

        dic = get_data_obj('dicts', 'zero')
        out = _(dic)
        out = dict_to_str(out)

# Generated at 2022-06-13 20:33:04.734738
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class Test_to_namedtuple(unittest.TestCase):
        def test_expected(self):
            dic = {'a': 1, 'b': 2}
            out = to_namedtuple(dic)
            self.assertEqual(out.a, 1)
            self.assertEqual(out.b, 2)

            dic = {'a': 1, 'b': 2}
            dic['c'] = {'d': 3, 'e': 4}
            dic['f'] = [5, 6, 7]
            out = to_namedtuple(dic)
            self.assertEqual(out.a, 1)
            self.assertEqual(out.b, 2)
            self.assertEqual(out.c.d, 3)
            self

# Generated at 2022-06-13 20:33:13.925337
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    dic = {'a': 1, 'b': 2}
    odic = OrderedDict(dic)
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    out = to_namedtuple(odic)
    assert out.a == 1
    assert out.b == 2
    out = to_namedtuple(SimpleNamespace(dic))
    assert out.a == 1
    assert out.b == 2
    out = to_namedtuple({'a': SimpleNamespace(dic)})
    assert out.a.a == 1
    assert out.a.b == 2
    out = to_namedtuple(['a', 'b', 'c'])

# Generated at 2022-06-13 20:33:20.112976
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == ()
    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple(NamedTuple()) == NamedTuple()
    assert to_namedtuple(SimpleNamespace()) == NamedTuple()

# Generated at 2022-06-13 20:33:33.160065
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    # noinspection PyUnresolvedReferences
    from flutils.testhelpers import (
        random_identifier,
        random_integer,
        random_lower_dict,
        random_lower_list,
        random_lower_tuple,
        random_lower_string,
        random_string
    )

    # noinspection SpellCheckingInspection,PyUnusedLocal,PyShadowingNames

# Generated at 2022-06-13 20:33:44.970351
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple({1: 2}) == namedtuple('NamedTuple', 'i0')(2)

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(1, 2)

    dic = {'a': 1, 'b': 2, 'c': 3}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b c')(1, 2, 3)

    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Generated at 2022-06-13 20:33:58.212724
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from dataclasses import dataclass
    from functools import singledispatch
    from types import SimpleNamespace
    from typing import List, NamedTuple

    # noinspection PyUnusedFunction
    @singledispatch
    def _is_namedtuple(obj: Any) -> bool:
        return False

    @_is_namedtuple.register(NamedTuple)
    def _(obj: NamedTuple) -> bool:
        return True

    @_is_namedtuple.register(List)
    def _(obj: List[Any]) -> bool:
        for item in obj:
            if not _is_namedtuple(item):
                return False
        return True


# Generated at 2022-06-13 20:34:04.440050
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    dic = {'a': 1, 'b': 2}
    nt: NamedTuple = to_namedtuple(dic)
    assert len(nt)
    assert nt.a is dic['a']
    assert nt.b is dic['b']
    try:
        # noinspection PyTypeChecker
        to_namedtuple(None)
    except TypeError as err:
        assert "('NoneType',) None" in str(err)
    try:
        # noinspection PyTypeChecker
        to_namedtuple('blah')
    except TypeError as err:
        assert "('str',) blah" in str(err)

# Generated at 2022-06-13 20:34:14.248318
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Simple list.
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple((1, 2)) == (1, 2)

    # Simple dictionary.
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)

    # Simple namedtuple.
    assert to_namedtuple(namedtuple('NamedTuple', 'a b')(1, 2)) == namedtuple('NamedTuple', 'a b')(1, 2)

    # Simple namespace.
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)

# Generated at 2022-06-13 20:34:24.402830
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import (
        to_namedtuple,
    )
    import logging
    import pytest
    from types import SimpleNamespace as SN

    logger = logging.getLogger(__name__)

    def test_logger(msg: str) -> None:
        logger.debug(msg)
        logger.info(msg)
        logger.warning(msg)
        logger.error(msg)
        logger.critical(msg)

    def test_func(msg: str) -> None:
        pass

    test_func('Test message')

    # default logger level is WARNING
    with pytest.raises(AssertionError):
        assert logger.getEffectiveLevel() == logging.DEBUG

    logger.setLevel(logging.INFO)
    assert logger.getEffectiveLevel() == logging.INFO

    test

# Generated at 2022-06-13 20:34:32.472394
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    d = {'a': 1, 'b': 2}
    out = to_namedtuple(d)
    pprint(out)
    out = to_namedtuple(out)
    pprint(out)
    dic = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': (4, 5)}}
    out = to_namedtuple(dic)
    pprint(out)
    out = to_namedtuple(out)
    pprint(out)
    dic = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': {'f': 4, 'g': 5}}}
    out = to_namedtuple(dic)
    pprint(out)
    out = to_named

# Generated at 2022-06-13 20:34:40.393166
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import json
    import unittest
    import orjson as json

    class test_to_namedtuple(unittest.TestCase):
        def setUp(self):
            super().setUp()
            self.records = open('demo.json')
            self.records = json.load(self.records)
            self.expected_results = self.records['expected_results']
            self.to_test = self.records['to_test']
            self.dumps = json.dumps

        def tearDown(self):
            super().tearDown()

        def test_all(self):
            for obj, expected in self.expected_results.items():
                obj = self.to_test[obj]
                expected = self.expected_results[obj['index']]
                result = self.dumps

# Generated at 2022-06-13 20:34:52.235438
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(['a', 'b', 'c'])._fields == ('a', 'b', 'c')
    assert to_namedtuple(('a', 'b', 'c'))._fields == ('a', 'b', 'c')
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3})._fields == ('a', 'b', 'c')
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3})[0] == 1
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3})[1] == 2
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3})[2] == 3

# Generated at 2022-06-13 20:35:04.001830
# Unit test for function to_namedtuple
def test_to_namedtuple():
    add_ = [('a', 1), ('b', 2)]
    adict = dict(add_)
    onamed = to_namedtuple(adict)
    assert isinstance(onamed, NamedTuple)
    assert hasattr(onamed, 'a')
    assert hasattr(onamed, 'b')

    alist = [adict, adict]
    olist = to_namedtuple(alist)
    assert isinstance(olist, list)
    assert isinstance(olist[0], NamedTuple)
    assert isinstance(olist[1], NamedTuple)

    atuple = (adict, adict)
    otuple = to_namedtuple(atuple)
    assert isinstance(otuple, tuple)
    assert isinstance(otuple[0], NamedTuple)
    assert isinstance

# Generated at 2022-06-13 20:35:10.042047
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    assert isinstance(result, namedtuple('NamedTuple', 'a b'))
    ntup = namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert result == ntup

# Generated at 2022-06-13 20:35:19.343866
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d = {'a': 1, 'b': 2, 'c': '3'}
    nt = to_namedtuple(d)
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c == '3'

    d = {'_a': 1, 'b_': 2, '_c_': '3'}
    nt = to_namedtuple(d)
    assert not hasattr(nt, '_a')
    assert not hasattr(nt, 'b_')
    assert not hasattr(nt, '_c_')
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c == '3'

    d = {'b': 1, 'a': 2, 'c': '3'}
    nt = to

# Generated at 2022-06-13 20:35:33.463953
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for method to_namedtuple()."""
    assert repr(to_namedtuple({'a': 1, 'b': 2})) == 'NamedTuple(a=1, b=2)'
    assert repr(to_namedtuple({'a': 1, 'b': 2, 'c': {'d': 3}})) == (
        'NamedTuple(a=1, b=2, c=NamedTuple(d=3))'
    )
    assert repr(to_namedtuple({'a': 1, 'b': 2, 'c': {'d': 3, 'e': '4'}})) == (
        'NamedTuple(a=1, b=2, c=NamedTuple(d=3, e=4))'
    )

# Generated at 2022-06-13 20:35:43.799150
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert dic['a'] == nt.a
    assert dic['b'] == nt.b
    dic = {'__a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert dic['b'] == nt.b
    li = [1, 2, 3, 4]
    nt = to_namedtuple(li)
    assert list(nt) == li
    dic = {'a': 1, 'b': 2, 'c': [{'d': 3}, {'e': 4}]}
    nt = to_namedtuple(dic)
   

# Generated at 2022-06-13 20:35:53.041487
# Unit test for function to_namedtuple
def test_to_namedtuple():

    class MyClass1:
        a = 5

        class MyClass2:
            b = 6

            class MyClass3:
                c = 7

    dic = OrderedDict([
        ('a', 1),
        ('b', 2),
        ('c', OrderedDict([
            ('d', 3),
            ('e', 4),
        ])),
    ])
    tpl = ('a', ('b', ('c', ('d', ('e', ('f', ('g', ('h', 'i'))))))))
    list_ = [[[['a']]]]

    assert to_namedtuple((()))._fields == ()
    assert to_namedtuple(())._fields == ()

    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    assert type

# Generated at 2022-06-13 20:36:03.054045
# Unit test for function to_namedtuple
def test_to_namedtuple():

    assert to_namedtuple([]) == []
    assert to_namedtuple((1, 2)) == (1, 2)

    d = dict(a=1, b=2)
    assert to_namedtuple(d) == NamedTuple(a=1, b=2)


# Generated at 2022-06-13 20:36:17.146347
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.validators import ValidationFailure

    def _test_to_namedtuple_dic():
        dic = {'a': 1, 'b': 2}
        result = to_namedtuple(dic)
        assert result == namedtuple('NamedTuple', sorted(dic.keys()))(
            **dic
        )
        del dic['a']
        result = to_namedtuple(dic)
        dic['a'] = None
        assert result == namedtuple('NamedTuple', sorted(dic.keys()))(
            **dic
        )

    def _test_to_namedtuple_odict():
        dic = OrderedDict()

# Generated at 2022-06-13 20:36:29.112364
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pytest import raises
    from typing import NamedTuple
    from flutils.namedtupleutils import to_namedtuple
    from flutils.objects import get_fields
    from flutils.validators import validate_identifier
    # Tests for dict type
    d = dict(a=1, b=2, _c=3, d_="test")
    nt = to_namedtuple(d)
    assert hasattr(nt, 'a')
    assert hasattr(nt, 'b')
    assert not hasattr(nt, '_c')
    assert not hasattr(nt, 'd_')
    # Tests for dictionary that does not start with an underscore and does not
    # have underscores
    d = dict(a=1, b=2, c=3)
    nt = to_namedtuple(d)


# Generated at 2022-06-13 20:36:41.994921
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.miscutils import validate_type_with

    dic = {'c': 3, 'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)
    assert 'a' in out._fields
    assert out.a == 1

    nt = to_namedtuple(OrderedDict(zip('abcd', range(4))))
    for i in range(4):
        assert hasattr(nt, chr(i+97))
        assert getattr(nt, chr(i+97)) == i

    lst = ['a', {'b': 'c', 'd': 'e'}]
    out = to_namedtuple(lst)

# Generated at 2022-06-13 20:36:51.833201
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pytest import raises

    from collections.abc import Sequence
    from types import SimpleNamespace

    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple({}) == to_namedtuple(tuple()) == namedtuple('NamedTuple', '')()

    assert to_namedtuple({'a': 1}) == to_namedtuple((1,)) == namedtuple('NamedTuple', 'a')(1)

    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple((1, 2)) == namedtuple('NamedTuple', 'a b')(1, 2)

    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3}) == to_namedtuple((1, 2, 3)) == named

# Generated at 2022-06-13 20:36:58.160164
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Test dict to NamedTuple
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', ('a', 'b'))(1, 2)

    # Test dict with keys that are not valid identifiers
    assert to_namedtuple({'a-1': 1, 'b-2': 2}) == namedtuple('NamedTuple', ('a1', 'b2'))(1, 2)

    # Test OrderedDict to namedtuple
    from collections import OrderedDict
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3

# Generated at 2022-06-13 20:37:09.688880
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []
    assert to_namedtuple([{}]) == [NamedTuple()]
    assert to_namedtuple([{'a': 1}]) == [NamedTuple(a=1)]
    assert to_namedtuple([{'a': 1}, {'a': 2}]) == [NamedTuple(a=1), NamedTuple(a=2)]
    assert to_namedtuple([{'a': 1}, {'b': 2}]) == [NamedTuple(a=1), NamedTuple(b=2)]
    assert to_namedtuple([{'a': 1}, {'a': 2}, {'b': 2}]) == [NamedTuple(a=1), NamedTuple(a=2), NamedTuple(b=2)]

    assert to

# Generated at 2022-06-13 20:37:19.861780
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)
    assert to_namedtuple(dic).a == 1
    assert to_namedtuple(dic).b == 2
    dic = {'a': 1, 'b': 2, 'C': 3, 'd': 4}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2, d=4)
    assert to_namedtuple(dic).a == 1
    assert to_namedtuple(dic).b == 2
    assert to_namedtuple(dic).d == 4
    dic = {'a': 1, '_b': 2, 'C': 3, 'd': 4}
   

# Generated at 2022-06-13 20:37:30.439232
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections.abc import Mapping
    from collections import OrderedDict
    from types import SimpleNamespace
    from typing import NamedTuple
    from typing import Tuple
    from flutils.namedtupleutils import to_namedtuple

    class Point(NamedTuple):
        x: float
        y: int

    class NamedP(NamedTuple):
        d: int
        e: int

    NT2 = NamedTuple('NT2', [('a', int), ('b', float)])
    d1 = {0: [1, 2, 3], 1: ['a', 'b', 'c']}
    d2 = OrderedDict(**{'a': 1, 'b': 2})
    d3 = {'a': 1, 'b': 2}

# Generated at 2022-06-13 20:37:44.092475
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class Test_to_namedtuple(unittest.TestCase):

        def test_to_namedtuple(self):
            dic = {'a': 1, 'b': 2}
            dic = to_namedtuple(dic)
            self.assertIsInstance(dic, namedtuple)
            self.assertEqual(dic.a, 1)
            self.assertEqual(dic.b, 2)

            dic = {'a': 1, 'b': 2, 'c': dic}
            dic = to_namedtuple(dic)
            self.assertIsInstance(dic, namedtuple)
            self.assertEqual(dic.a, 1)
            self.assertEqual(dic.b, 2)
            self.assertIsInstance

# Generated at 2022-06-13 20:37:51.175932
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifier

    assert to_namedtuple({}) == to_namedtuple(to_namedtuple({}))
    assert to_namedtuple({}) == to_namedtuple(OrderedDict())
    assert to_namedtuple({}) == to_namedtuple(SimpleNamespace())
    assert to_namedtuple({}) == to_namedtuple(tuple())
    assert to_namedtuple({}) == to_namedtuple({'a': 1, 'b': 2})
    assert to_namedtuple({}) == to_namedtuple(OrderedDict(a=1, b=2))

# Generated at 2022-06-13 20:38:00.427667
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)

    odic = OrderedDict(a=1, b=2)
    assert to_namedtuple(odic) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)

    lst = [1, 2, 3]
    assert to_namedtuple(lst) == [1, 2, 3]

    tup = tuple(lst)
    assert to_namedtuple(tup) == (1, 2, 3)


# Generated at 2022-06-13 20:38:11.889368
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections.abc import Mapping, Sequence
    from collections import OrderedDict
    from typing import Any, List, Tuple

    from flutils.namedtupleutils import to_namedtuple
    from flutils.tests.tester import obj_tester

    def test_valid_convert(
            test_obj: Union[Mapping, Sequence],
            exp_obj: Union[List, Tuple],
            *args, **kwargs
    ) -> None:
        try:
            act_obj = to_namedtuple(test_obj, *args, **kwargs)
        except ValueError:
            exp_obj = to_namedtuple(exp_obj, *args, **kwargs)


# Generated at 2022-06-13 20:38:21.958522
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == (1, 2)

    dic = {'a': 1, 'b': [1, 2], 'c': {'d': [1, 2]}}
    assert to_namedtuple(dic) == (1, (1, 2), ((1, 2),))

    dic = {'a': 1, 'b': [1, 2], 'c': {'d': [1, 2]}}
    assert to_namedtuple(dic) == (1, (1, 2), ((1, 2),))

    dic = {'a': 1, 'b': [1, 2], 'c': {'d': [1, 2]}}
    assert to_namedt

# Generated at 2022-06-13 20:38:36.723014
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.validators import validate_identifier
    from flutils.typeddict import TypedDict
    from collections.abc import Sequence
    from typing import List

    try:
        validate_identifier('_')
    except SyntaxError:
        pass
    else:
        assert False, '_ should not be a valid identifier'
    try:
        validate_identifier('a$')
    except SyntaxError:
        pass
    else:
        assert False, 'a$ should not be a valid identifier'

    class DDD(TypedDict):
        a: int

    dic = DDD(a=1)

    obj = {'a': 1, '_b': 2, 'c$': 3}

    out = to_namedtuple(obj)


# Generated at 2022-06-13 20:38:49.221357
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    MyTuple = namedtuple('MyTuple', 'a b')
    assert to_namedtuple(MyTuple(1, 2)) == MyTuple(1, 2)

    assert to_namedtuple({'a': 1, 'b': 2}) == MyTuple(a=1, b=2)
    assert to_namedtuple([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]) == [
        MyTuple(a=1, b=2),
        MyTuple(c=3, d=4),
    ]

    from collections import OrderedDict
    dic = OrderedDict()
    dic['a'] = 1
    dic['b'] = 2
    assert to_namedtuple(dic) == My

# Generated at 2022-06-13 20:39:00.866666
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from types import SimpleNamespace
    from typing import NamedTuple

    result = to_namedtuple([])
    expected = []
    assert result == expected

    result = to_namedtuple(())
    expected = ()
    assert result == expected

    result = to_namedtuple({'a': 1})
    expected = NamedTuple(a=1)
    assert result == expected

    result = to_namedtuple({'a': 1, 'b': 2, 'c': 3})
    expected = NamedTuple(a=1, b=2, c=3)
    assert result == expected

    result = to_namedtuple({'a': 1, 2: 'b', 3: 'c'})
    expected = Named

# Generated at 2022-06-13 20:39:07.081760
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import Dict
    from collections import OrderedDict
    from types import SimpleNamespace
    dict_ = {'a': 1, 'b': 2}
    d: Dict[str, Any] = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    obj = SimpleNamespace()
    obj.a = 1
    obj.b = 2
    out = to_namedtuple(dict_)
    assert all([hasattr(out, key) for key in ['a', 'b']])
    out = to_namedtuple(d)
    assert all([hasattr(out, key) for key in ['a', 'b']])
    out = to_namedtuple(obj)

# Generated at 2022-06-13 20:39:19.214000
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: () -> None

    # empty dict
    dic = dict()
    out = to_namedtuple(dic)
    assert out == NamedTuple()

    # simple dict
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out == NamedTuple(a=1, b=2)

    # simple dict with bad identifier keys
    dic = {'a': 1, '1b': 2}
    out = to_namedtuple(dic)
    assert out == NamedTuple(a=1)

    # simple OrderedDict
    dic = OrderedDict([('a', 1), ('1b', 2), ('b', 2)])
    out = to_namedtuple(dic)
    assert out == NamedT

# Generated at 2022-06-13 20:39:27.516360
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import defaultdict
    from types import MappingProxyType

    # Verify that the doc examples work
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    assert out == namedtuple('NamedTuple', 'a b')(1, 2)

    # Verify that the input can be a OrderedDict
    from collections import OrderedDict
    dic = OrderedDict([('a', 1), ('b', 2)])
    out = to_namedtuple(dic)
    assert out == namedtuple('NamedTuple', 'a b')(1, 2)

    # Verify that the input can be a SimpleNamespace
    from types import SimpleNamespace
    obj = SimpleNames

# Generated at 2022-06-13 20:39:40.580489
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple('NamedTuple', 'a b')), (
        "to_namedtuple did not return a namedtuple on dictionary"
    )
    ord_dic = OrderedDict()
    ord_dic['a'] = 1
    ord_dic['b'] = 2
    out = to_namedtuple(ord_dic)
    assert isinstance(out, namedtuple('NamedTuple', 'a b')), (
        "to_namedtuple did not return a namedtuple on ordereddictionary"
    )
    ord_dic['b'] = 2
    ord_dic['a'] = 1



# Generated at 2022-06-13 20:39:58.766788
# Unit test for function to_namedtuple
def test_to_namedtuple():
    class Test(object):
        def __repr__(self):
            return 'Test()'
    import numpy as np
    # noinspection PyUnusedLocal
    x = np.nan  # noqa

# Generated at 2022-06-13 20:40:08.389084
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    dic1 = {
        'a': [
            {
                'c': 'd',
                'e': 'f',
            },
            'g',
            {
                'h': {
                    'i': 'j'
                }
            }
        ]
    }
    print('NamedTuple(list of dicts)')
    pprint(to_namedtuple(dic1))
    print('NamedTuple(list of dicts)')
    dic2 = to_namedtuple(dic1)
    pprint(dic2)
    print('Accessing dicts in list:')
    print(dic2.a[0].c)
    print(dic2.a[0].e)
    print('Accessing string in list:')
   

# Generated at 2022-06-13 20:40:19.559104
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2}
    out = to_namedtuple(obj)
    assert out.a == 1
    assert out.b == 2
    dic = {'a': 1, 'b': {'c': 2}}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b.c == 2
    obj = [dic, dic, dic]
    out = to_namedtuple(obj)
    assert out[0].a == 1
    assert out[0].b.c == 2
    assert out[1].a == 1
    assert out[1].b.c == 2
    assert out[2].a == 1
    assert out[2].b.c == 2
    obj = (dic, dic, dic)

# Generated at 2022-06-13 20:40:27.088544
# Unit test for function to_namedtuple
def test_to_namedtuple():
    #noinspection PyUnresolvedReferences
    """Unit tests for function to_namedtuple."""

    import pytest
    from collections import OrderedDict
    from typing import Any
    import flutils.namedtupleutils

    dic = dict(a=1, b=2)
    dic = flutils.namedtupleutils.to_namedtuple(dic)

    assert isinstance(dic, tuple)
    assert dic.a == 1
    assert dic.b == 2

    dic = OrderedDict()
    dic['a'] = 1
    dic['b'] = 2

    dic = flutils.namedtupleutils.to_namedtuple(dic)

    assert isinstance(dic, tuple)
    assert dic.a == 1
    assert dic.b == 2

# Generated at 2022-06-13 20:40:38.000293
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    from typing import NamedTuple as NT
    from collections import namedtuple

    class NT2(NT):
        """Test namedtuple subclass."""

    class Obj1:
        """Test class."""

    class Obj2:
        """Test class."""

        def __str__(self) -> str:
            """Test."""
            return 'Obj2'

        def __repr__(self) -> str:
            """Test."""
            return 'Obj2'

    class Obj3:
        """Test class."""

        def __str__(self) -> str:
            """Test."""
            return 'Obj3'

        def __repr__(self) -> str:
            """Test."""
            return 'Obj3'


# Generated at 2022-06-13 20:40:46.073467
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    dic = {'a': 1, 'b': 2}
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b == 2
    assert not hasattr(obj, 'keys')
    assert not hasattr(obj, 'items')
    assert not hasattr(obj, 'values')
    dic = OrderedDict([('a', 1), ('b', 2)])
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b == 2
    assert not hasattr(obj, 'keys')
    assert not hasattr(obj, 'items')
    assert not hasattr(obj, 'values')

# Generated at 2022-06-13 20:40:57.390586
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test function to_namedtuple."""
    obj = {'a': 1, 'b': {'ba': 11, 'bb': 12}}
    expected = NamedTuple(a=1, b=NamedTuple(ba=11, bb=12))
    assert to_namedtuple(obj) == expected

    obj = [1, 'a', {'ba': 11, 'bb': 12}]
    expected = [1, 'a', NamedTuple(ba=11, bb=12)]
    assert to_namedtuple(obj) == expected

    obj = ('a', 1, ('b', 'c'))
    expected = ('a', 1, ('b', 'c'))
    assert to_namedtuple(obj) == expected

    obj = {'a': 1, 'b.c': '2'}

# Generated at 2022-06-13 20:41:09.262838
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from collections import OrderedDict
    from types import SimpleNamespace as SN

    dic = {}
    out = to_namedtuple(dic)
    assert out == cast(NamedTuple, NamedTuple())

    dic = dict(a=1, b=2)
    out = to_namedtuple(dic)
    assert out == cast(NamedTuple, NamedTuple(a=1, b=2))

    dic = OrderedDict(a=1, b=2)
    out = to_namedtuple(dic)
    assert out == cast(NamedTuple, NamedTuple(a=1, b=2))

    dic = SN(a=1, b=2)
    out = to_namedtuple(dic)
    assert out == cast

# Generated at 2022-06-13 20:41:11.541955
# Unit test for function to_namedtuple
def test_to_namedtuple():
    pass


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:41:19.126392
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Unit test for case simple_namespace
    ns_obj = SimpleNamespace(a=1, b=2)
    assert to_namedtuple(ns_obj) == ns_obj  # type: ignore[unreachable]
    # Unit test for case list_of_dict
    lod_obj = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    # noinspection PyTypeChecker
    assert to_namedtuple(lod_obj) == [ns_obj, ns_obj]  # type: ignore[unreachable]
    # Unit test for case list_of_list
    lol_obj = [['a', 1], ['b', 2], ['c', 3]]
    # noinspection PyTypeChecker
    assert to_namedtuple(lol_obj)

# Generated at 2022-06-13 20:41:35.766287
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict([])) == NamedTuple()
    assert to_namedtuple({'a': OrderedDict([('b', 2)])}) == NamedTuple(a=NamedTuple(b=2))
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == NamedTuple(a=1, b=2)
    assert to_namedtuple([1, 2]) == [1, 2]


# Generated at 2022-06-13 20:41:47.324986
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit tests for function to_namedtuple."""
    from flutils.tests import (
        get_testdata_path,
        run_all_tests,
    )
    from flutils.namedtupleutils import (
        _to_namedtuple,
    )
    from flutils.namedtupleutils import to_namedtuple
    import json
    from os.path import (
        join,
    )

    this_file = get_testdata_path(__file__, 'flutils')

    with open(join(this_file, 'ec2_instance.json')) as jsonfile:
        json_data = json.load(jsonfile)
    ntdata = to_namedtuple(json_data)
    assert json_data['Architecture'] == ntdata.Architecture
    assert json_

# Generated at 2022-06-13 20:41:58.235811
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pytest import raises
    from typing import Any, List, Tuple

    def assert_obj_to_namedtuple(
            obj: List[Any],
            nt: List[Tuple[Any, ...]],
            *,
            cmp: bool = True
    ) -> None:
        got = to_namedtuple(obj)
        if cmp is True:
            assert got == nt
        else:
            for i, obj in enumerate(nt):
                assert got[i] == obj

    # noinspection PyTypeChecker

# Generated at 2022-06-13 20:42:10.973039
# Unit test for function to_namedtuple
def test_to_namedtuple():
    #   test a Blank OrderedDict
    assert to_namedtuple(OrderedDict()) == namedtuple('NamedTuple', '')()

    #   test a Blank list
    assert to_namedtuple([]) == []

    #   test a Blank tuple
    assert to_namedtuple(()) == ()

    #   test a Blank dict
    assert to_namedtuple({}) == namedtuple('NamedTuple', '')()

    #   test a Blank SimpleNamespace
    assert to_namedtuple(SimpleNamespace()) == namedtuple('NamedTuple', '')()

    #   test a string
    assert to_namedtuple('string') == 'string'

    #   test a Blank string
    assert to_namedtuple('') == ''

    #   test a non-iterable type (

# Generated at 2022-06-13 20:42:15.668974
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    dic = {'a': 1, 'b': 2}
    test_obj = to_namedtuple(dic)
    assert test_obj == pytest.approx(NamedTuple(a=1, b=2))

if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:42:26.535903
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.typingutils import Dict
    from flutils.namedtupleutils import to_namedtuple

    def _assert_is_namedtuple(obj: Any):
        assert hasattr(obj, '_asdict')

    def _assert_is_list(obj: Any):
        assert hasattr(obj, 'append')

    dic = {
        'a': 1,
        'b': 2,
        '_c': 3
    }
    obj = to_namedtuple(dic)
    _assert_is_namedtuple(obj)
    assert hasattr(obj, 'a')
    assert hasattr(obj, 'b')
    assert not hasattr(obj, '_c')
    assert obj.a == 1
    assert obj.b == 2


# Generated at 2022-06-13 20:42:32.675763
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(None) is None
    assert to_namedtuple(()) == ()
    assert to_namedtuple([]) == []
    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple({'a': 1}) == NamedTuple(a=1)
    assert to_namedtuple({'a': 1, 'b': 2.0}) == NamedTuple(a=1, b=2.0)
    assert to_namedtuple({'a': 1, 'b': 2.0, 'c': 3}) == NamedTuple(
        a=1,
        b=2.0,
        c=3
    )

# Generated at 2022-06-13 20:42:41.784773
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # noinspection PyPep8Naming
    def _t(
            obj: _AllowedTypes,
            expected: Union[NamedTuple, List, str],
            _started: bool = False
    ) -> bool:
        obj_type: str = type(obj).__name__
        out = to_namedtuple(obj)
        out_type: str = type(out).__name__

        # pylint: disable=line-too-long

        # noinspection PyPep8Naming
        def _tc(
                obj_: Any,
                expected_: Union[NamedTuple, List, str],
                _started_: bool = False
        ) -> bool:
            if _started_ is False:
                assert type(obj_) == type(expected_)
                assert obj_type == out_