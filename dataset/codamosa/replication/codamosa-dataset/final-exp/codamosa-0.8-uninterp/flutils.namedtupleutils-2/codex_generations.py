

# Generated at 2022-06-13 20:32:52.787116
# Unit test for function to_namedtuple
def test_to_namedtuple():

    class TestClass(NamedTuple):
        a: int
        b: int
        c: int


# Generated at 2022-06-13 20:33:04.553439
# Unit test for function to_namedtuple
def test_to_namedtuple():
    out = to_namedtuple([
        OrderedDict(a=3, b=4),
        {'a': 5, 'b': 6},
    ])
    assert isinstance(out, list)
    assert isinstance(out[0], tuple)
    assert isinstance(out[1], tuple)
    assert out == (
        (3, 4),
        (5, 6),
    )

    out = to_namedtuple((
        OrderedDict(a=3, b=4),
        {'a': 5, 'b': 6},
    ))
    assert isinstance(out, tuple)
    assert isinstance(out[0], tuple)
    assert isinstance(out[1], tuple)
    assert out == (
        (3, 4),
        (5, 6),
    )


# Generated at 2022-06-13 20:33:13.844010
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    dic = {'a': 1, 'b': 2}
    res = to_namedtuple(dic)
    assert res == OrderedDict(a=1, b=2)

    dic = OrderedDict([('a', 1), ('b', 2)])
    res = to_namedtuple(dic)
    assert res == OrderedDict(a=1, b=2)

    dic = {'a': 1, 'b': {'c': 3, 'd': 4}}
    res = to_namedtuple(dic)
    assert res == OrderedDict(a=1, b=OrderedDict(c=3, d=4))


# Generated at 2022-06-13 20:33:24.760924
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert isinstance(to_namedtuple(dic), NamedTuple)
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    ret = to_namedtuple([
        {
            'foo': 'bar',
            'a': {
                'x': 'y',
                'z': {
                    'a': {
                        'a': 'b',
                        'b': 2
                    },
                    'b': False
                }
            }
        },
        [
            'a', 'b'
        ]
    ])

    assert isinstance(ret, list)
    assert isinstance(ret[0], NamedTuple)
    assert isinstance(ret[0].a.z, NamedTuple)
   

# Generated at 2022-06-13 20:33:26.308379
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import namedtuple_testsuite
    namedtuple_testsuite.test_to_namedtuple()

# Generated at 2022-06-13 20:33:36.707544
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pformat
    from flutils.namedtupleutils import to_namedtuple
    # simple tests with list
    to_namedtuple([1])
    to_namedtuple([1, 2])
    to_namedtuple([1, 2, 3])
    to_namedtuple([1, 2, 3, 4])
    to_namedtuple([1, 2, 3, 4, 5])
    to_namedtuple([1, 2, 3, 4, 5, 6])
    to_namedtuple([1, 2, 3, 4, 5, 6, 7])
    try:
        to_namedtuple([1, 2, 3, 4, 5, 6, 7, 8])
    except TypeError:
        pass
    else:
        assert False, 'Should have raised TypeError'
    # simple

# Generated at 2022-06-13 20:33:42.137079
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test to_namedtuple()."""

    from datetime import date, datetime, time
    from flutils.namedtupleutils import to_namedtuple
    from decimal import Decimal
    from collections import OrderedDict
    from types import SimpleNamespace

    dic = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    named_tuple = to_namedtuple(dic)
    assert named_tuple == namedtuple('NamedTuple', 'a b c')(1, 2, 3)
    assert named_tuple._fields == ('a', 'b', 'c')

    dic['e'] = OrderedDict([('f', 4), ('g', 5), ('h', 6)])
    named_tuple = to_namedtuple(dic)


# Generated at 2022-06-13 20:33:49.456945
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from collections.abc import Mapping
    from collections import OrderedDict
    from functools import singledispatch
    from types import SimpleNamespace
    from typing import List, NamedTuple, Union
    from flutils.validators import validate_identifier

    _AllowedTypes = Union[
        List,
        Mapping,
        NamedTuple,
        SimpleNamespace,
        tuple,
    ]


# Generated at 2022-06-13 20:34:00.476827
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(None) == NamedTuple()
    assert to_namedtuple(1) == 1
    assert to_namedtuple(['a', 1, None, {'c': 'd'}]) == [
        'a',
        1,
        None,
        NamedTuple(c='d')
    ]
    assert to_namedtuple(OrderedDict([('x', 1), ('y', 2)])) == NamedTuple(
        x=1,
        y=2
    )
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == NamedTuple(
        a=1,
        b=2
    )

# Generated at 2022-06-13 20:34:11.930783
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.tests.common_tests import abs_path
    from flutils.namedtupleutils import to_namedtuple
    from flutils.miscutils import load_json_file

    fn = abs_path('miscutils.json')
    dic = load_json_file(fn)
    dic2 = to_namedtuple(dic)
    assert hasattr(dic2, 'one')
    assert dic2.one == dic['one']


# Generated at 2022-06-13 20:34:23.306542
# Unit test for function to_namedtuple
def test_to_namedtuple():
    def compare_objects(org, updated):
        if isinstance(org, Mapping):
            assert sorted(org.items()) == sorted(updated._asdict().items())
        elif isinstance(org, Sequence):
            assert org == list(updated)
        else:
            raise TypeError(
                "Can convert only 'list', 'tuple', 'dict' to a NamedTuple; "
                "got: (%r) %s" % (type(org).__name__, org)
            )

    # Test valid input types

# Generated at 2022-06-13 20:34:35.492565
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from types import SimpleNamespace
    nt1 = namedtuple("nt1", ["a", "b"])
    nt2 = namedtuple("nt2", ["c", "d"])
    nt3 = namedtuple("nt3", ["x", "y"])

    sn = SimpleNamespace(
        a=1, b=2, c=3, a_list=[4, 5, 6],
        a_dict={"a": 7, "b": 8}, a_nt=nt1(a=9, b=10),
        a_dict_of_lists={"a": [11, 12], "b": [13, 14]}
    )

    nt_sn = to_namedtuple(sn)
    assert nt_sn.a == 1
    assert nt_

# Generated at 2022-06-13 20:34:50.146378
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace

    assert str(to_namedtuple({})) == 'NamedTuple()'
    assert str(to_namedtuple({'a': 1})) == 'NamedTuple(a=1)'
    assert str(to_namedtuple(OrderedDict([('one', 1), ('two', 2)]))) == 'NamedTuple(one=1, two=2)'
    assert str(to_namedtuple(OrderedDict((('a', 1), ('b', 2), ('c', 3))))) == 'NamedTuple(a=1, b=2, c=3)'
    assert str(to_namedtuple(SimpleNamespace(a=1, b=2))) == 'NamedTuple(a=1, b=2)'

# Generated at 2022-06-13 20:34:58.617086
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import random

    # noinspection PyUnusedLocal,PyProtectedMember
    class A(object):
        def __init__(self, attr_a: NamedTuple):
            self.attr_a = attr_a

        def __repr__(self):
            return 'A()'

        def __eq__(self, other):
            return hasattr(other, 'attr_a') and other.attr_a == self.attr_a


# Generated at 2022-06-13 20:35:10.757749
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': [1, 2]}) == NamedTuple(a=1, b=[1, 2])
    assert to_namedtuple({'a': 1, 'b': {'c': 1, 'd': 2}}) == NamedTuple(a=1, b=NamedTuple(c=1, d=2))
    assert to_namedtuple({'a': 1, 'b': {'c': [{'e': 1}, {'f': 2}]}}) == NamedTuple(a=1, b=NamedTuple(c=[NamedTuple(e=1), NamedTuple(f=2)]))
    assert to

# Generated at 2022-06-13 20:35:19.720468
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import random
    import sys
    import string
    import copy

    # TODO: add tests for ordered dict
    # TODO: add tests for single namespace
    # NOTE: this method is tested in the test_namedtupleutils.py test file
    # TODO: add tests for multiple named tuples

    if sys.version_info.minor < 6:
        print('Python 3.6 is required for this test.')
        return True

    class RandomNamedTuple(object):
        def __init__(self, keys: List[str], values: List[Any]):
            self.keys = keys[:]
            self.values = values[:]
            self.tuple = self.create()


# Generated at 2022-06-13 20:35:33.777622
# Unit test for function to_namedtuple
def test_to_namedtuple():
    lst = [1, 2, 3]
    assert to_namedtuple(lst) == [1, 2, 3]
    assert isinstance(to_namedtuple(lst), list)
    assert to_namedtuple(tuple(lst)) == (1, 2, 3)
    assert isinstance(to_namedtuple(tuple(lst)), tuple)

    tpl = (1, 2, 3)
    assert to_namedtuple(tpl) == (1, 2, 3)
    assert isinstance(to_namedtuple(tpl), tuple)
    assert to_namedtuple(list(tpl)) == [1, 2, 3]
    assert isinstance(to_namedtuple(list(tpl)), list)

    dic = {'a': 1, 'b': 2}
   

# Generated at 2022-06-13 20:35:41.134970
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    nt1 = to_namedtuple(dic)
    assert nt1
    assert nt1.a == 1
    assert nt1.b == 2
    assert nt1[0] == 1
    assert nt1[1] == 2
    assert nt1._asdict() == dic
    assert nt1 == (1, 2)


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:35:51.812315
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import defaultdict
    from flutils.namedtupleutils import to_namedtuple
    from flutils.namedtupleutils import test_to_namedtuple
    from flutils.namedtupleutils import _to_namedtuple
    from types import SimpleNamespace

    # Test to_namedtuple
    dic = {'a': 1, 'b': 2}
    exp = to_namedtuple(dic)
    assert isinstance(exp, collections.namedtuple)
    assert exp.a == dic['a']
    assert exp.b == dic['b']

    # Test to_namedtuple on a namedtuple
    # noinspection PyTypeChecker
    tpl = collections.namedtuple('test', 'x y')(1, 2)

# Generated at 2022-06-13 20:36:02.625788
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert isinstance(nt, NamedTuple)
    assert isinstance(nt, tuple)
    assert 'a' in nt._fields
    assert 'b' in nt._fields
    assert getattr(nt, 'a') == 1
    assert getattr(nt, 'b') == 2
    assert nt[0] == 1
    assert nt[1] == 2

    dic['c'] = {'d': 4, 'e': 5}
    nt = to_namedtuple(dic)
    assert 'c' in nt._fields
    assert getattr(nt, 'c')._fields == ('d', 'e')
    assert getattr(nt, 'c').d == 4
   

# Generated at 2022-06-13 20:36:17.494027
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from copy import copy
    from types import SimpleNamespace

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic = OrderedDict([('b', 1), ('a', 2)])
    assert to_namedtuple(dic) == NamedTuple(b=1, a=2)

    dic = {'a': 1, 'b': 2, '_c': 3}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': 2, '_c': 3, 'B': 4}
    assert to_namedtuple(dic) == NamedTuple

# Generated at 2022-06-13 20:36:22.670821
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    expected = namedtuple('NamedTuple', 'a b')(a=1, b=2)

    assert to_namedtuple(dic) == expected


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:36:28.884484
# Unit test for function to_namedtuple
def test_to_namedtuple():
    '''
    Run all unit tests

    Usage:
        test_to_namedtuple()
    '''
    import doctest
    doctest.run_docstring_examples(to_namedtuple, globals())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #test_to_namedtuple()

# Generated at 2022-06-13 20:36:36.017943
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(1) == 1

    dic = {
        'a': 1,
        'b': {'b1': 2, 'b2': {'b22': 3}},
        'c': [3, 4]
    }
    exp = NamedTuple(a=1, b=NamedTuple(b1=2, b2=NamedTuple(b22=3)), c=[3, 4])
    assert to_namedtuple(dic) == exp

    dic = {'a': 1, 'b': {'b1': 2, 'b2': {'b22': 3}}, 'c': [3, 4]}

# Generated at 2022-06-13 20:36:39.516145
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))



# Generated at 2022-06-13 20:36:49.543699
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1}) == to_namedtuple({'b': 2, 'a': 1})
    assert to_namedtuple({'a': 1}) == to_namedtuple(OrderedDict({'a': 1}))
    assert to_namedtuple({'a': 1}) == to_namedtuple(OrderedDict({'b': 2, 'a': 1}))
    assert to_namedtuple({'b': 2, 'a': 1}) == to_namedtuple(OrderedDict({'b': 2, 'a': 1}))
    assert to_namedtuple({'b': 2, 'a': 1}) != to_namedtuple(OrderedDict({'a': 1, 'b': 2}))

# Generated at 2022-06-13 20:36:53.390888
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

# Generated at 2022-06-13 20:37:05.322247
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    def _to_namedtuple_raiser(
            obj: _AllowedTypes,
            expected: str
    ) -> None:
        with pytest.raises(TypeError, match=expected):
            to_namedtuple(obj)

    # A type that cannot be converted
    _to_namedtuple_raiser('', r"Can convert only 'list', 'tuple', 'dict'")

    # Empty objects
    assert to_namedtuple({}) == namedtuple('NamedTuple', '')()  # type: ignore[misc]
    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == ()
    assert to_namedtuple('') == ''

    # A single value type
    assert to_namedtuple(1.2) == 1.2



# Generated at 2022-06-13 20:37:16.408027
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(dict()) == namedtuple('NamedTuple', '')()
    assert to_namedtuple(dict(a=1, b=2)) == namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple(dict(b=2, a=1)) == namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple(dict(b=2, a=1, c=3)) == namedtuple('NamedTuple', 'a b c')(1, 2, 3)
    assert to_namedtuple(OrderedDict(b=2, a=1, c=3)) == namedtuple('NamedTuple', 'b a c')(2, 1, 3)
    assert to_namedt

# Generated at 2022-06-13 20:37:23.753095
# Unit test for function to_namedtuple
def test_to_namedtuple():
    try:
        to_namedtuple(None)
        assert False, (
            "Should have raised TypeError for None but did not"
        )
    except TypeError:
        pass

    try:
        to_namedtuple(1)
        assert False, (
            "Should have raised TypeError for integer but did not"
        )
    except TypeError:
        pass

    try:
        to_namedtuple(True)
        assert False, (
            "Should have raised TypeError for boolean but did not"
        )
    except TypeError:
        pass

    try:
        to_namedtuple('test')
        assert False, (
            "Should have raised TypeError for string but did not"
        )
    except TypeError:
        pass


# Generated at 2022-06-13 20:37:31.541605
# Unit test for function to_namedtuple
def test_to_namedtuple():
    pass

# Generated at 2022-06-13 20:37:45.213945
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    class Test1(NamedTuple):
        a: int
        b: int

    class Test2(NamedTuple):
        a: int
        b: int


    class Test3(NamedTuple):
        a: int
        b: int

    # class Test4(NamedTuple):
    #     a: int
    #     b: int

    # class Test5(NamedTuple):
    #     a: int
    #     b: int

    # class Test6(NamedTuple):
    #     a: int
    #     b: int

    # class Test7(NamedTuple):
    #     a: int
    #     b: int

    # class Test8(NamedTuple):
    #    

# Generated at 2022-06-13 20:37:47.254983
# Unit test for function to_namedtuple
def test_to_namedtuple():
    pass  # add some unit tests!


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:37:59.042370
# Unit test for function to_namedtuple
def test_to_namedtuple():
    x = [
        {'a': 1, 'b': 2},
        {'a': 3, 'b': 4},
        {'a': 5, 'b': 6},
        {'a': 7, 'b': 8},
    ]
    y = to_namedtuple(x)
    assert isinstance(y, list)
    assert isinstance(y[0], NamedTuple)
    assert isinstance(y[1], NamedTuple)
    assert isinstance(y[2], NamedTuple)
    assert isinstance(y[3], NamedTuple)
    assert y[0].a == 1
    assert y[0].b == 2
    assert y[1].a == 3
    assert y[1].b == 4
    assert y[2].a == 5
    assert y[2].b == 6
   

# Generated at 2022-06-13 20:38:04.825206
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from functools import singledispatch
    from operator import (
        attrgetter,
        itemgetter,
    )
    from types import SimpleNamespace
    from typing import (
        Any,
        Callable,
        List,
        NamedTuple,
        Tuple,
    )
    from unittest import TestCase
    from unittest.mock import (
        call,
        Mock,
        patch,
    )
    from flutils.namedtupleutils import (
        get_attr,
        get_attr_or_item,
        to_namedtuple,
    )

    class MyData(NamedTuple):
        a: int
        b: str

    # noinspection PyUnusedLocal
    @singledispatch
    def myfunc(obj: Any):
        return obj



# Generated at 2022-06-13 20:38:13.521566
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    # noinspection PyArgumentList
    obj = NamedTuple('NamedTuple', [], {})
    out = to_namedtuple(obj)
    assert out._fields == ()

    obj = ('a', 1)
    out = to_namedtuple(obj)
    assert out[0] == 'a'
    assert out[1] == 1

    obj = ['a', 1]
    out = to_namedtuple(obj)
    assert out[0] == 'a'
    assert out[1] == 1

    obj = {'a': 1}
    out = to_namedtuple(obj)
    assert out.a == 1

    obj = {'a': 1, '_b': 2}
    out = to_namedtuple(obj)
    assert out

# Generated at 2022-06-13 20:38:22.544782
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    import types
    x = OrderedDict.fromkeys(['a', 'b', 'c'])
    y = OrderedDict.fromkeys(['c', 'd', 'a'])
    z = OrderedDict.fromkeys(['d'])
    x['b'] = [1, 2, 3]
    x['c'] = types.SimpleNamespace(a=1, b=2, c=3)
    y['d'] = types.SimpleNamespace(a=1, b=2, c=3)
    z['d'] = types.SimpleNamespace(a=1, b=2, c=3)
    x['a'] = y
    y['a'] = z
    z['d'] = x
    object_x = to_namedtuple(x)

# Generated at 2022-06-13 20:38:36.891285
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    dic = {
        'a': 1,
        'b': True,
        'c': 3.2,
        'd': ['a', 'b', 'c'],
        'e': (1, 2, 3),
        'f': {
            'fa': 1,
            'fb': 2,
            'fc': 3,
        },
        'g': 'Test',
    }
    assert to_namedtuple(dic) == to_namedtuple(
        OrderedDict(
            sorted(dic.items(), key=lambda x: x[0])
        )
    )
    assert to_namedtuple(dic) == to_namedtuple(
        SimpleNamespace(**dic)
    )
    assert to_

# Generated at 2022-06-13 20:38:49.596963
# Unit test for function to_namedtuple
def test_to_namedtuple():  # pragma: no cover
    from collections import OrderedDict
    from operator import itemgetter
    from pprint import pformat
    from typing import List
    from collections.abc import Mapping
    from flutils.namedtupleutils import to_namedtuple
    from itertools import groupby
    from flutils.notebookutils import in_ipynb
    from flutils.objectutils import get_deep
    from flutils.stringutils import get_print_string
    from flutils.testingutils import (
        are_equal,
        are_not_equal,
        assert_is_instance,
    )

    if in_ipynb():
        from IPython import display

    # noinspection PyTypeChecker

# Generated at 2022-06-13 20:39:01.718651
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace

    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert repr(to_namedtuple((1, 2, 3))) == "NamedTuple(1, 2, 3)"
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)

# Generated at 2022-06-13 20:39:26.177332
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import sys
    import pytest
    import collections
    import datetime
    import uuid
    import random
    import flutils.namedtupleutils
    from collections import (
        OrderedDict,
        namedtuple,
    )
    from flutils.validators import validate_identifier

    normal_dict = {'a': 1, 'b': 2}
    nt1 = flutils.namedtupleutils.to_namedtuple(normal_dict)
    assert nt1.a == 1
    assert nt1.b == 2
    assert type(nt1) == collections.namedtuple('NamedTuple', ('a', 'b'))

    normal_dict = {'a': None}
    nt2 = flutils.namedtupleutils.to_namedtuple(normal_dict)
    assert n

# Generated at 2022-06-13 20:39:39.637389
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from collections import OrderedDict
    from types import SimpleNamespace

    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple)
    assert out.a == 1
    assert out.b == 2

    odict = OrderedDict([('a', 1), ('b', 2)])
    out = to_namedtuple(odict)
    assert isinstance(out, namedtuple)
    assert out.a == 1
    assert out.b == 2

    dic = {'a': 1, 'in': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple)
    assert out.a == 1

# Generated at 2022-06-13 20:39:51.489304
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert to_namedtuple((1, 2, 3)) == (1, 2, 3)

    assert to_namedtuple({1: 'a',
                          2: 'b',
                          3: 'c'}) == NamedTuple(**{1: 'a',
                                                    2: 'b',
                                                    3: 'c'})
    assert to_namedtuple(OrderedDict([(1, 'a'),
                                      (2, 'b'),
                                      (3, 'c')])) == NamedTuple(**OrderedDict([(1, 'a'),
                                                                                 (2, 'b'),
                                                                                 (3, 'c')]))

# Generated at 2022-06-13 20:40:05.051980
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:40:15.952335
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out: NamedTuple = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    assert out == (1, 2)
    assert dir(out) == ['a', 'b']
    assert sorted(out._fields) == sorted(dir(out))

    dic = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
    out: NamedTuple = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    assert out.c.d == 3
    assert out.c.e == 4

    ordered_dic = OrderedDict()
    ordered_dic['a'] = 1
    ordered_d

# Generated at 2022-06-13 20:40:27.339614
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4, 'f': [5, 6, 7]}}
    expected = NamedTuple(a=1, b=2, c=NamedTuple(d=3, e=4, f=(5, 6, 7)))
    assert to_namedtuple(dic) == expected

    dic = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4, 'f': [5, 6, 7]}, 'g': 8}
    expected = NamedTuple(a=1, b=2, c=NamedTuple(d=3, e=4, f=(5, 6, 7)), g=8)
    assert to_namedtuple(dic) == expected

    d

# Generated at 2022-06-13 20:40:38.057043
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import pprint

    dic = {'a': 1, 'b': 2}
    tup = to_namedtuple(dic)
    pprint.pprint(tup)
    assert tup.a == 1
    assert tup.b == 2

    dic = {'a': 1, 'b': 2, 'c': 3}
    tup = to_namedtuple(dic)
    pprint.pprint(tup)
    assert tup.a == 1
    assert tup.b == 2
    assert tup.c == 3

    dic = {}
    tup = to_namedtuple(dic)
    pprint.pprint(tup)
    assert tup == ()
    assert tup == namedtuple

# Generated at 2022-06-13 20:40:46.124997
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([1, {'a': 1, 'b': 2}]) == [1, NamedTuple(a=1, b=2)]
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == NamedTuple(a=1, b=2)
    assert to_namedtuple([('a', 1)]) == [NamedTuple(a=1)]
    assert to_namedtuple([NamedTuple(a=1, b=2)]) == [NamedTuple(a=1, b=2)]
    assert to_namedtuple((1, (('a', 1), ('b', 2)), 3)) == (1, (NamedTuple(a=1, b=2),), 3)

# Generated at 2022-06-13 20:40:57.444263
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple, OrderedDict
    from types import SimpleNamespace

    dic = dict(a=1, b=2)
    assert to_namedtuple(dic) == namedtuple("NamedTuple", 'a b')(a=1, b=2)

    dic = dict(_a=1, b=2)
    assert to_namedtuple(dic) == namedtuple("NamedTuple", 'b')(b=2)

    dic = dict(a1=1, b=2)
    assert to_namedtuple(dic) == namedtuple("NamedTuple", 'a1 b')(a1=1, b=2)

    dic = OrderedDict(a=1, b=2)

# Generated at 2022-06-13 20:41:05.804302
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    obj = to_namedtuple(dic)
    assert obj.a == 1
    assert obj.b == 2

    from collections import OrderedDict

    odic = OrderedDict((('a', 1), ('b', 2)))
    obj = to_namedtuple(odic)
    assert isinstance(obj, OrderedDict)
    assert obj.a == 1
    assert obj.b == 2

# Generated at 2022-06-13 20:41:35.052394
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from random import shuffle
    from types import SimpleNamespace
    from unittest.mock import Mock, sentinel

    # noinspection PyUnresolvedReferences,PyTypeChecker
    from pandas.testing import assert_series_equal

    from flutils.namedtupleutils import to_namedtuple

    mock = Mock()
    mock.return_value = sentinel.returned_value

    # Mapping
    # noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:41:46.955235
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from datetime import time
    from flutils.collectionsutils import dotdict
    from flutils.namedtupleutils import NamedTuple
    import pytest


    def _test_namedtuple(obj: _AllowedTypes, test: str):
        result = to_namedtuple(obj)
        assert isinstance(result, NamedTuple)
        assert result == to_namedtuple(obj)
        assert result == eval(test)
        assert result.__repr__() == test


    test = dict(
        a=1,
        b=dict(
            c=2,
            d=3,
        ),
    )
    test = 'NamedTuple(a=1, b=NamedTuple(c=2, d=3))'
    _test_named

# Generated at 2022-06-13 20:41:58.034942
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from datetime import date
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple

    dic = {'one': 1, 'two': 2}
    tup = 1, 2, 'three'
    namedt = Point(1, 3)


# Generated at 2022-06-13 20:42:10.894048
# Unit test for function to_namedtuple
def test_to_namedtuple():  # pylint: disable=unused-argument
    """Unit test for function to_namedtuple"""
    import unittest

    from flutils.namedtupleutils import (
        get_namedtuple_names,
        to_namedtuple,
    )

    class ToNamedTupleTests(unittest.TestCase):
        """Unit tests for function to_namedtuple"""

        def test_list(self):
            """Unit test for function to_namedtuple - lists"""
            self.assertSequenceEqual(
                to_namedtuple(['a', 'b']),
                ['a', 'b']
            )

# Generated at 2022-06-13 20:42:20.414583
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        'a': 1,
        'b': 2,
        'c': [1, 2, '3'],
        'd': {'a': 1, 'b': 2, 'c': '3'},
        'e': 'abc',
        '2': 3,
    }
    nt = to_namedtuple(dic)
    assert nt.a == 1
    assert nt.b == 2
    nt.c == [1, 2, '3']
    assert nt.d.a == 1
    assert nt.d.b == 2
    assert nt.d.c == '3'
    assert nt.e == 'abc'


# Generated at 2022-06-13 20:42:29.626726
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    dic = {'a': 1, 'b': 2}
    with pytest.raises(TypeError) as excinfo:
        to_namedtuple(dic)
    assert "got: ('dict')" in str(excinfo.value)
    assert "'list', 'tuple', 'dict'" in str(excinfo.value)

    assert to_namedtuple(dic) == dic

    lis = [1, 2]
    assert to_namedtuple(lis) == lis

    lis = [1, 2, {'a': 1, 'b': 2}]
    assert to_namedtuple(lis) == lis

    lis = [[[1, {'a': 1, 'b': 2}]]]
    assert to_

# Generated at 2022-06-13 20:42:40.540475
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.testing import StrEq
    import pytest

    # Test a list being converted to a namedtuple.
    lst = [1, 2, 3]
    lst_nt = to_namedtuple(lst)
    assert isinstance(lst_nt, list)
    for item in lst_nt:
        assert isinstance(item, int)

    # Test a tuple being converted to a namedtuple.
    tup = (1, 2, 3)
    tup_nt = to_namedtuple(tup)
    assert isinstance(tup_nt, tuple)
    for item in tup_nt:
        assert isinstance(item, int)

    # Test a dictionary being converted to a namedtuple.