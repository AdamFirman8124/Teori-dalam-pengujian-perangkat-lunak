

# Generated at 2022-06-13 20:32:52.932195
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from copy import copy
    from unittest.mock import patch

    import pytest

    from flutils.namedtupleutils import to_namedtuple

    def test_NamedTuple_attrs(nt: NamedTuple) -> None:
        assert nt.a == 1
        assert nt.b == 2
        assert nt.c == 3

    # type: ignore[misc]
    def test_NamedTuple_repr(nt: NamedTuple) -> None:
        assert repr(nt) == "NamedTuple(a=1, b=2, c=3)"

    def test_NamedTuple_str(nt: NamedTuple) -> None:
        assert str(nt) == "NamedTuple(a=1, b=2, c=3)"


# Generated at 2022-06-13 20:32:58.684712
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, '_e': 5}
    nt = to_namedtuple(obj)
    assert nt.a == 1


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:33:12.006266
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(list()) == []
    assert to_namedtuple(dict()) == NamedTuple()
    assert to_namedtuple(OrderedDict()) == NamedTuple()
    assert to_namedtuple(tuple()) == ()
    assert to_namedtuple(SimpleNamespace()) == NamedTuple()

    assert to_namedtuple('a') == 'a'
    assert to_namedtuple([]) == []
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple([1, [2]]) == [1, [2]]
    assert to_namedtuple((1, 2)) == (1, 2)
    assert to_namedtuple((1, (2,))) == (1, (2,))
    assert to_namedtuple({})

# Generated at 2022-06-13 20:33:23.787240
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
    out = to_namedtuple(obj)
    assert out.key1 == 'val1'
    assert out.key2 == 'val2'
    assert out.key3 == 'val3'
    from collections import OrderedDict
    obj = OrderedDict(key1='val1', key2='val2', key3='val3')
    out = to_namedtuple(obj)
    assert out.key1 == 'val1'
    assert out.key2 == 'val2'
    assert out.key3 == 'val3'

# Generated at 2022-06-13 20:33:35.657566
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function 'to_namedtuple'."""

    from collections import OrderedDict
    from copy import deepcopy
    from pprint import pformat
    from sys import version

    from flutils.namedtupleutils import to_namedtuple

    assert version >= '3.6', "Need 'Python 3.6' or greater; got: (%s)" % version

    msg = "to_namedtuple: %s"

    out = to_namedtuple({'a': 1, 'b': 2})
    assert isinstance(out, tuple), msg % "should be an instance of type 'tuple'; got: (%s)" % type(out)
    assert isinstance(out, namedtuple('NamedTuple', 'a b')), msg % "should be an instance of namedtuple; got: (%s)" % type(out)

# Generated at 2022-06-13 20:33:46.476843
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(dict(a=1, b=2, c=3)) == namedtuple('NamedTuple', ('a', 'b', 'c'))(1, 2, 3)
    assert to_namedtuple(dict(a=dict(b=2, c=3), d=4)) == namedtuple('NamedTuple', ('a', 'd'))(namedtuple('NamedTuple', ('b', 'c'))(2, 3), 4)
    assert to_namedtuple(dict(a=list(range(4)))) == namedtuple('NamedTuple', ('a'))([0, 1, 2, 3])
    assert to_namedtuple([1, 2, 3, 4]) == [1, 2, 3, 4]

# Generated at 2022-06-13 20:33:59.082489
# Unit test for function to_namedtuple
def test_to_namedtuple():
    f = to_namedtuple
    # noinspection PyPep8

# Generated at 2022-06-13 20:34:10.717701
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import json


# Generated at 2022-06-13 20:34:17.733148
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple"""
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(1, 2)

    dic = {'a': 1, 'b': 2, 'c': 3}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b c')(1, 2, 3)

    dic = {'a': 1, 'b': 2, 'c': 3, '0': 4}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', '0 a b c')(4, 1, 2, 3)


# Generated at 2022-06-13 20:34:27.755181
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    obj = {'a': 1, 'b': 2}
    namedtup = to_namedtuple(obj)
    assert namedtup.a == 1
    assert namedtup.b == 2

    obj = (1, 2)
    namedtup = to_namedtuple(obj)
    assert namedtup[0] == 1
    assert namedtup[1] == 2

    obj = [1, 2]
    namedtup = to_namedtuple(obj)
    assert namedtup[0] == 1
    assert namedtup[1] == 2

    obj = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    namedtup = to_namedtuple(obj)

# Generated at 2022-06-13 20:34:39.436212
# Unit test for function to_namedtuple
def test_to_namedtuple():
    test_dict = {'a': 1, 'b': 2}
    res = to_namedtuple(test_dict)
    assert res.a == 1
    assert res.b == 2
    test_dict2 = {'c': 3, 'd': 4}
    res2 = to_namedtuple(test_dict2)
    assert res2.c == 3
    assert res2.d == 4
    test_list = [test_dict, test_dict2]
    res3 = to_namedtuple(test_list)
    assert res3[0].a == 1
    assert res3[0].b == 2
    assert res3[1].c == 3
    assert res3[1].d == 4
    test_namedtuple = namedtuple("Test", "alpha beta")(10, 20)
    res

# Generated at 2022-06-13 20:34:51.758814
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from inspect import getsource

    source = getsource(to_namedtuple)
    assert source.startswith('def to_namedtuple(') is True
    assert source.endswith('):') is True

    dic = {
        'a': {
            'b': 1,
            'c': 2,
            'd': {
                'e': 10,
                'f': 20,
            },
        },
    }
    exp = (('a', (('b', 1), ('c', 2), ('d', (('e', 10), ('f', 20))))),)
    out = to_namedtuple(dic)
    assert out == exp


# Generated at 2022-06-13 20:35:03.844133
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Simple Namespace test
    from types import SimpleNamespace

    # SimpleNamespace with a single value
    obj = SimpleNamespace(a=1)
    assert to_namedtuple(obj) == obj
    assert to_namedtuple(obj) == obj.a

    # SimpleNamespace with a list of values
    obj = SimpleNamespace(a=[1, 2, 3])
    assert to_namedtuple(obj) == obj
    assert to_namedtuple(obj) == obj.a == [1, 2, 3]
    assert to_namedtuple(obj).a == to_namedtuple(obj.a)

    # SimpleNamespace with a dictionary
    obj = SimpleNamespace(a={'a': 1})
    assert to_namedtuple(obj) == obj

# Generated at 2022-06-13 20:35:09.207000
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple

    t = namedtuple('abc', ['a', 'b', 'c'])
    d = {'a': 1, 'b': 2, 'c': 3}
    expected = t(1, 2, 3)
    actual = to_namedtuple(d)
    assert actual == expected
    return



# Generated at 2022-06-13 20:35:18.863271
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Test a dictionary
    obj = {'a': 1, 'b': 2}
    ret = to_namedtuple(obj)
    assert isinstance(ret, NamedTuple)
    assert 'a' in ret._fields
    assert 'b' in ret._fields
    assert ret.a == 1
    assert ret.b == 2

    # Test an OrderedDict
    obj = OrderedDict((('a', 1), ('b', 2)))
    ret = to_namedtuple(obj)
    assert isinstance(ret, NamedTuple)
    assert ret._fields == ('a', 'b')
    assert ret.a == 1
    assert ret.b == 2

    # Test a dictionary with identifiers

# Generated at 2022-06-13 20:35:32.983447
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from typing import Dict, List, Any
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple
    from namedtupled import namedtupled

    dic: Dict[str, Any] = {
        'a': 1,
        'b': 2,
        'c': (3, 4, 5),
    }
    tup: List[Any] = (1, 2, 3)
    sn = SimpleNamespace(a=1)
    od = OrderedDict(a=1, b=2, c=3)
    lst = [1, 2, 3]
    namedtup = namedtupled('NamedTuple', 'a b c')(1, 2, 3)

# Generated at 2022-06-13 20:35:43.451905
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import collections
    import types
    # Given, When, Then
    assert to_namedtuple({'a': 1, 'b': 2}) == collections.namedtuple('NamedTuple', ('a', 'b'))(1, 2)
    assert to_namedtuple({'a': 1, 'b': 2})(2) == 2
    assert to_namedtuple({'a': 1, 'b': 2}).b == 2
    assert to_namedtuple({'a': 1, 'b': 2}).a == 1
    assert to_namedtuple({'b': 2, 'a': 1}) == collections.namedtuple('NamedTuple', ('a', 'b'))(1, 2)

# Generated at 2022-06-13 20:35:52.810766
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    from datetime import date
    import doctest

    dt = date(2018, 3, 4)
    dtstr = dt.strftime('%Y%m%d')

# Generated at 2022-06-13 20:36:02.985728
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dict_ = {'a': 1, 'b': 2}
    out_ = to_namedtuple(dict_)
    assert out_.a == 1
    assert out_.b == 2

    obj_ = SimpleNamespace(**dict_)
    out_ = to_namedtuple(obj_)
    assert out_.a == 1
    assert out_.b == 2

    obj_ = OrderedDict(dict_)
    out_ = to_namedtuple(obj_)
    assert out_[0] == 1
    assert out_[1] == 2

    list_ = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    out_ = to_namedtuple(list_)
    assert out_[0].a == 1

# Generated at 2022-06-13 20:36:15.691180
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from datetime import datetime
    from decimal import Decimal
    from flutils.validators import T_DateTime, T_Decimal

    assert to_namedtuple(['a']) == ['a']
    assert to_namedtuple(('a')) == ('a',)
    assert to_namedtuple({'a': 1}) == namedtuple('NamedTuple', 'a')(a=1)

    expected = namedtuple('NamedTuple', 'a,b')(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2}) == expected

    expected = namedtuple('NamedTuple', 'a,b')(a=[], b=2)

# Generated at 2022-06-13 20:36:30.696866
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    def check(obj, expected):
        # noinspection PyTypeChecker
        out = to_namedtuple(obj)
        assert out == expected

    # noinspection PyTypeChecker
    check({'a': 1, 'b': 2}, ['a', 'b', 'c'])


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    import flutils.namedtupleutils

    print(
        flutils.namedtupleutils.to_namedtuple(
            {'a': 1, 'b': 2}
        )
    )
    print(
        flutils.namedtupleutils.to_namedtuple(
            OrderedDict({'a': 1, 'b': 2})
        )
    )

# Generated at 2022-06-13 20:36:42.352183
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from itertools import product
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple

    class MyNamedTuple(NamedTuple):
        __slots__ = ()
        a: int
        b: int
        c: List[int]
        d: Tuple[int, int]


# Generated at 2022-06-13 20:36:52.499441
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert type(out) is namedtuple('NamedTuple', 'a b'), (
        "to_namedtuple('dic') output should be a NamedTuple, got: %s"
        % type(out)
    )

    lis = [1, 2, 3]
    out = to_namedtuple(lis)
    assert type(out) is list, (
        "to_namedtuple('lis') output should be a list, got: %s"
        % type(out)
    )

    tup = (1, 2, 3)
    out = to_namedtuple(tup)

# Generated at 2022-06-13 20:37:03.669234
# Unit test for function to_namedtuple
def test_to_namedtuple():
    data = {
        'name': 'qux',
        'foo': SimpleNamespace(
            bar='bar',
            qux='qux',
        ),
        'bar': [1, 2, 3],
        'baz': {
            'foo': 'foo',
            'bar': 'bar',
            'qux': 'qux',
        },
    }

    out = to_namedtuple(data)

    for attr in ['foo', 'bar', 'baz']:
        assert hasattr(out, attr)

    print(out)
    assert isinstance(out.foo, SimpleNamespace)
    assert isinstance(out.bar, list)
    assert isinstance(out.baz, namedtuple('NamedTuple', ('bar', 'foo', 'qux')))


# Generated at 2022-06-13 20:37:15.597197
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # Convert a SimpleNamespace
    test_ns: SimpleNamespace = SimpleNamespace()
    test_ns.Level1 = SimpleNamespace()
    test_ns.Level1.a = 1
    test_ns.Level1.b = 2

    new_ns = to_namedtuple(test_ns)
    assert isinstance(new_ns, NamedTuple)
    assert hasattr(new_ns, 'Level1')
    assert isinstance(new_ns.Level1, NamedTuple)
    assert hasattr(new_ns.Level1, 'a')
    assert hasattr(new_ns.Level1, 'b')

    # Convert an OrderedDict
    test_od = OrderedDict()
    test_od['Level1'] = OrderedDict()
    test_od['Level1']['a']

# Generated at 2022-06-13 20:37:23.299093
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    tup = to_namedtuple(dic)
    assert tup.a == dic.get('a')
    assert tup.b == dic.get('b')

    ol = OrderedDict(sorted({'a': 1, 'b': 2}.items()))
    tup = to_namedtuple(ol)
    assert tup.a == ol.get('a')
    assert tup.b == ol.get('b')

    ol = OrderedDict({'a': 1, 'b': 2})
    tup = to_namedtuple(ol)
    assert tup.a == ol.get('a')
    assert tup.b == ol.get('b')


# Generated at 2022-06-13 20:37:34.034635
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple(OrderedDict([('b', 2), ('a', 1)])) == namedtuple('NamedTuple', 'b a')(2, 1)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)).a == 1
    assert to_namedtuple(SimpleNamespace(a=1, b=2)).b == 2
    assert to_namedtuple(SimpleNamespace(a=1, b=2, c=3)).c == 3
   

# Generated at 2022-06-13 20:37:47.498574
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    assert isinstance(result, namedtuple)
    assert isinstance(result, tuple)
    assert result.a == 1
    assert result.b == 2

    ordered = OrderedDict()
    ordered['c'] = 3
    ordered['d'] = 4
    result = to_namedtuple(ordered)
    assert isinstance(result, namedtuple)
    assert isinstance(result, tuple)
    assert result.c == 3
    assert result.d == 4

    tup = (5, 6, 7)
    result = to_namedtuple(tup)
    assert isinstance(result, tuple)
    assert list(result) == list(tup)


# Generated at 2022-06-13 20:37:59.194952
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: () -> None
    """Unit tests used when not run as ```python -m unittest```.

    Example:
        >>> from flutils.namedtupleutils import to_namedtuple, test_to_namedtuple
        >>> test_to_namedtuple()

    """
    import unittest  # noqa

    class Tests(unittest.TestCase):
        maxDiff = None

        def test_base_nested(self):
            # type: () -> None
            vals = {'a': 1, 'b': 2}  # type: Dict[str, int]
            self.assertEqual(
                repr(to_namedtuple(vals)),
                "NamedTuple(a=1, b=2)"
            )

# Generated at 2022-06-13 20:38:11.138978
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test function to_namedtuple"""
    import random
    import rstr
    import string
    import sys
    import unittest.mock

    import six
    import attr
    import typeguard
    import pytest

    from flutils.namedtupleutils import (
        to_namedtuple,
    )
    from flutils.collectionsutils import (
        to_ordereddict,
    )
    from flutils.namedtupleutils import (
        to_namedtuple,
    )
    from flutils.textutils import (
        text_type,
    )

    assert to_namedtuple(4) is NotImplemented

    # noinspection PyShadowingNames,PyUnusedLocal

# Generated at 2022-06-13 20:38:31.547749
# Unit test for function to_namedtuple
def test_to_namedtuple():

    assert to_namedtuple({'a': 1, 'b':2}) == (1, 2)
    assert to_namedtuple(('a', 1, 'b', 2)) == (1, 2)
    assert to_namedtuple([1, 2]) == (1, 2)
    assert to_namedtuple([1, 2, 'a']) == (1, 2, 'a')
    assert to_namedtuple({'a': 1, 'b':2}) == (1, 2)
    assert to_namedtuple({'a': 1, 'b':2, 'c':'test'}) == (1, 2, 'test')
    assert to_namedtuple({'a': 1, 'b':2, 'c':'test', 'd':'test'}) == (1, 2, 'test', 'test')


# Generated at 2022-06-13 20:38:39.742637
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    dic = {'a': 1, 'b': 2}
    expected_out = namedtuple('NamedTuple', 'a b')(a=1, b=2)
    actual_out = to_namedtuple(dic)
    assert actual_out == expected_out

    dic = {1: 1, 'b': 2}
    expected_out = namedtuple('NamedTuple', 'b')(b=2)
    actual_out = to_namedtuple(dic)
    assert actual_out == expected_out

    dic = {
        'a': {1: 1},
        'b': 2,
        '_c': {'c': 3},
        '_3': {'3': 4},
    }
   

# Generated at 2022-06-13 20:38:43.081101
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    failure_count, _ = doctest.testmod()
    assert failure_count == 0

# Generated at 2022-06-13 20:38:52.676930
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import json
    import flutils.jsonutils
    import pytest

    valid_keys_dict: Mapping[str, Any] = {
        'int': 1,
        'str': 'something',
        'list': [1, 2, 3, 4],
        'dict': {'a': 1, 'b': 2},
    }
    nt1 = to_namedtuple(valid_keys_dict)
    assert len(nt1._fields) == len(valid_keys_dict)
    assert nt1.int == 1
    assert nt1.list[2] == 3
    assert nt1.dict.b == 2
    valid_keys_odict = OrderedDict(valid_keys_dict)
    nt2 = to_namedtuple(valid_keys_odict)

# Generated at 2022-06-13 20:39:04.253336
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Code in this function will be executed as a test.

    .. note::
        When testing a function that has a decorator with arguments this
        function must be accessed via a parameter.

    Example:
        >>> # noinspection PyUnresolvedReferences
        >>> from flutils.namedtupleutils import to_namedtuple as test_func
        >>> test_func(42)
        Traceback (most recent call last):
        ...
        TypeError: Can convert only 'list', 'tuple', 'dict' to a NamedTuple; got: (int) 42
    """

    import pytest  # noqa

    # noinspection Mypy
    from flutils.namedtupleutils import _to_namedtuple as to_namedtuple  # noqa


# Generated at 2022-06-13 20:39:16.008820
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from collections.abc import Mapping
    from types import SimpleNamespace
    from flutils.validators import validate_identifier
    from flutils.constants import Platform
    from flutils.namedtupleutils import to_namedtuple

    if Platform.IS_WINDOWS:
        assert Platform.IS_WINDOWS is True
    elif Platform.IS_LINUX:
        assert Platform.IS_LINUX is True
    elif Platform.IS_MAC:
        assert Platform.IS_MAC is True
    else:
        raise Exception('Unknown platform')

    x = None
    assert to_namedtuple(x) is None

    x = 'a'
    assert to_namedtuple(x) is 'a'

    x = 1
    assert to_namedtuple(x) is 1


# Generated at 2022-06-13 20:39:23.910668
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyUnresolvedReferences
    """Test the function to_namedtuple."""
    import collections
    import types
    # noinspection PyUnresolvedReferences
    from flutils.namedtupleutils import to_namedtuple
    # noinspection PyUnresolvedReferences
    from flutils.validators import is_identifier

    # Do a quick test of the is_identifier function; used for the tests of
    # the to_namedtuple function.
    assert is_identifier('a')
    assert is_identifier('A')
    assert is_identifier('aBc')
    assert is_identifier('aBcDef')
    assert is_identifier('A_bCd')
    assert is_identifier('_abc')
    assert is_identifier('_ABC')


# Generated at 2022-06-13 20:39:29.857830
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 1, 'b': d1}
    d3 = {'a': 1, 'b': d2}
    d4 = {'a': 1, 'b': d3}
    d5 = {'a': 1, 'b': d4}

    l1 = [1, 2, 3, 4]
    l2 = [1, l1, 3, 4]
    l3 = [1, l2, 3, 4]
    l4 = [1, l3, 3, 4]
    l5 = [1, l4, 3, 4]


# Generated at 2022-06-13 20:39:42.379525
# Unit test for function to_namedtuple
def test_to_namedtuple():
    data = SimpleNamespace(
        a=1,
        b=2,
        c=3,
    )
    expected_result = namedtuple('NamedTuple', 'a b c')
    result = to_namedtuple(data)
    assert result.__class__ == expected_result
    assert result == expected_result(a=1, b=2, c=3)

    data = OrderedDict(
        a=1,
        b=2,
        c=3,
    )
    expected_result = namedtuple('NamedTuple', 'a b c')
    result = to_namedtuple(data)
    assert result.__class__ == expected_result
    assert result == expected_result(a=1, b=2, c=3)


# Generated at 2022-06-13 20:39:53.789358
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict

    dic1 = dict(a=1, b=2)
    assert to_namedtuple(dic1) == namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)

    lst = [1, 2, 3, 4]
    assert to_namedtuple(lst) == [1, 2, 3, 4]

    dic2 = OrderedDict([('c', 3), ('d', 4)])
    assert to_namedtuple(dic2) == namedtuple('NamedTuple', ('c', 'd'))(c=3, d=4)

    tup1 = (1, 2, 3, 4, 5, 6)
    assert to

# Generated at 2022-06-13 20:40:18.431373
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from random import choice
    from string import ascii_letters
    sample_str = [
        '',
        ' ',
        '  ',
        '\\',
        'a',
        'aa',
        '1',
        '12',
        'a a',
        '_a',
        '_a_',
        'a_',
        'a__',
    ]

    count = 30
    while count > 0:
        rnd_list = [choice(ascii_letters) for _ in range(count)]
        sample_str.append(''.join(rnd_list))
        count -= 1


# Generated at 2022-06-13 20:40:26.482882
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        namedtuple,
        OrderedDict,
    )
    from types import SimpleNamespace

    from flutils.namedtupleutils import to_namedtuple

    # regular dict
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple('NamedTuple', 'a b'))
    assert out.a == 1
    assert out.b == 2

    # special cases with dict
    dic = {'_a': 1, ' b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple('NamedTuple', ''))

    dic = {'_a': 1, 'b_': 2}
    out = to_namedt

# Generated at 2022-06-13 20:40:33.831618
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection SpellCheckingInspection
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(1, 2)
    # noinspection SpellCheckingInspection
    assert to_namedtuple({'b': 2, 'a': 1}) == namedtuple('NamedTuple', 'a b')(1, 2)
    # noinspection SpellCheckingInspection
    assert to_namedtuple(OrderedDict((('a', 1), ('b', 2)))) == namedtuple('NamedTuple', 'a b')(1, 2)
    # noinspection SpellCheckingInspection

# Generated at 2022-06-13 20:40:44.831343
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from types import SimpleNamespace as Namespace

    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == ()
    assert to_namedtuple({}) == NamedTuple()

    assert to_namedtuple([1]) == [1]
    assert to_namedtuple((1,)) == (1,)
    assert to_namedtuple({'a': 1}) == NamedTuple(a=1)

    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple((1, 2)) == (1, 2)
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)


# Generated at 2022-06-13 20:40:54.234026
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    from flutils.collectionsutils import is_mapping
    from flutils.namedtupleutils import to_namedtuple
    from flutils.stringutils import validate_identifier
    from flutils.testingutils import dummy
    from flutils.validators import (
        is_uuid,
        validate_uuid_arg,
    )
    from flutils.objectsutils import (
        create_ordered_dict,
        create_simple_namespace,
    )
    dic = {
        'x': 'X',
        'y': 'Y',
        'z': 'Z',
    }
    assert is_mapping(dic)
    res = to_namedtuple(dic)
    assert is_mapping(res)
    assert not is_mapping(res)
   

# Generated at 2022-06-13 20:41:06.545553
# Unit test for function to_namedtuple
def test_to_namedtuple():
    def new_obj() -> SimpleNamespace:
        a: SimpleNamespace = SimpleNamespace()
        a.a = 1
        a.b = 2
        a.c = [{'c': 1, 'd': 2}, 3, 4]
        a.d = {'e': 1, 'f': 2}
        a.e = SimpleNamespace()
        a.e.x = 1
        a.e.y = 2
        a.f = SimpleNamespace(x=1, y=2)
        a.g = 'g'
        a.h = [1, 2, 3]
        a.i = (1, 2, 3)
        a.j = {'k': 1, 'l': 2}
        a.k = OrderedDict()
        a.k['k'] = 1

# Generated at 2022-06-13 20:41:13.477691
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from typing import Any, Dict, NamedTuple, Tuple
    from flutils.namedtupleutils import to_namedtuple

    TUP = Tuple[int, str, Tuple[int, str, Tuple[int, str]]]

    dic: Dict[str, Any] = {
        'a': 1,
        'b': 'b',
        'c': {
            'c': 1,
            'd': 'd',
            'e': {
                'e': 1,
                'f': 'f',
            },
        },
    }
    got = to_namedtuple(dic)
    assert isinstance(got, NamedTuple)
    assert hasattr(got, 'a')
    assert got.a == 1

# Generated at 2022-06-13 20:41:19.826215
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple"""
    from pprint import pformat
    from unittest import TestCase

    from flutils.namedtupleutils import to_namedtuple
    from flutils.namedtupleutils._namedtupleutils import _to_namedtuple
    from flutils.namedtupleutils._namedtupleutils import _convert_items
    from flutils.validators import validate_identifier

    class TestToNamedTuple(TestCase):
        def test_init(self):
            self.assertRaises(
                TypeError,
                to_namedtuple,
                None,
            )

            self.assertRaises(
                TypeError,
                to_namedtuple,
                1,
            )


# Generated at 2022-06-13 20:41:27.678597
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyTypeChecker
    ntd1: NamedTuple = to_namedtuple({"first":"John", "last":"Doe"})
    assert hasattr(ntd1, 'first')
    assert hasattr(ntd1, 'last')
    assert ntd1.first == 'John'
    assert ntd1.last == 'Doe'

    # noinspection PyTypeChecker
    ntd2: NamedTuple = to_namedtuple({"first":"John", "last":"Doe", "middle":"Peter"})
    assert hasattr(ntd2, 'first')
    assert hasattr(ntd2, 'last')
    assert hasattr(ntd2, 'middle')
    assert ntd2.first == 'John'
    assert ntd2.last == 'Doe'
    assert n

# Generated at 2022-06-13 20:41:34.624473
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import datetime
    from collections import namedtuple
    from flutils.namedtupleutils import to_namedtuple
    from flutils.namedtupleutils import _to_namedtuple
    from flutils.miscutils import OrderedDict

    dic = {
        'a': 1,
        'b': 2,
        'c': 3,
        'camelCase': 4,
        'snake_case': 5,
        'space case': 6,
        'KEY': 7,
        'Key': 8,
        'keY': 9,
        'odd_key': 10,
        '_key': 11,
        'key_': 12,
        '1key': 13,
    }

# Generated at 2022-06-13 20:42:13.238026
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class TestToNamedTuple(unittest.TestCase):

        def test_dict_to_namedtuple(self):
            dic = {'a': 1, 'b': 2}
            nt = to_namedtuple(dic)
            self.assertIsInstance(nt, type(nt._fields))
            self.assertEqual(nt.a, 1)
            self.assertEqual(nt.b, 2)
            self.assertEqual(nt._fields, ('a', 'b'))

        def test_ordered_dict_to_namedtuple(self):
            _dic = OrderedDict()
            _dic['b'] = 2
            _dic['a'] = 1

# Generated at 2022-06-13 20:42:24.557650
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    from collections import ChainMap
    from flutils.namedtupleutils import to_namedtuple

    class Test(unittest.TestCase):
        maxDiff = None

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def test_to_namedtuple(self):
            from collections import OrderedDict
            from collections.abc import Mapping
            from typing import Dict, List, Tuple
            from types import SimpleNamespace


# Generated at 2022-06-13 20:42:31.757480
# Unit test for function to_namedtuple
def test_to_namedtuple():
    s = SimpleNamespace()
    s.example1 = 1
    s.example2 = 2
    assert to_namedtuple(s) == NamedTuple(example1=1, example2=2)

    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple((1, 2)) == (1, 2)

    assert to_namedtuple({'a': 1}) == NamedTuple(a=1)
    assert to_namedtuple({'b': 1, 'a': 2}) == NamedTuple(a=2, b=1)
    assert to_namedtuple({'a': [1, 2]}) == NamedTuple(a=[1, 2])
    assert to_namedtuple({'a': [9, 8, {'a': [2, 1]}]})

# Generated at 2022-06-13 20:42:41.489145
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple([{'a': 1, 'b': 2}, [1, 2]]) == [NamedTuple(a=1, b=2), [1, 2]]
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict([('b', 2), ('a', 1)])) == NamedTuple(b=2, a=1)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == NamedTuple(a=1, b=2)