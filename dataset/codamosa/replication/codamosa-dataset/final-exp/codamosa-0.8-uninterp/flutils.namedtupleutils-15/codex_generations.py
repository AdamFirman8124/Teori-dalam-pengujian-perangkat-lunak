

# Generated at 2022-06-13 20:33:04.054335
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict((('a', 1), ('b', 2)))) == NamedTuple(a=1, b=2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == NamedTuple(a=1, b=2)
    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert to_namedtuple((1, 2, 3)) == (1, 2, 3)
    assert to_namedtuple([{}, 2, 3]) == [NamedTuple(()), 2, 3]

# Generated at 2022-06-13 20:33:13.645568
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import datetime
    from collections import OrderedDict
    from typing import Dict

    dic: Dict[str, Any] = {
        'a': 1,
        'b': {
            'c': 2,
            'd': 3,
            'e': {
                'f': 123.45,
                'g': [
                    {
                        'h': datetime.datetime.today()
                    },
                    {
                        'h': 'h'
                    },
                    {
                        'h': None
                    },
                ]
            },
        },
        'i': {
            'j': {
                'k': 3,
                'l': 4,
            },
        },
    }

    namedtup = to_namedtuple(dic)

    assert 'a' in namedtup._fields


# Generated at 2022-06-13 20:33:24.670402
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from collections import namedtuple
    from flutils.validators import validate_identifier

    make = namedtuple('NamedTuple', ['a', 'b'])
    assert isinstance(make(1, 2), NamedTuple)
    assert isinstance(make(a=1, b=2), NamedTuple)

    dic: OrderedDict = OrderedDict({'a': 1, 'b': 2})
    nt1 = to_namedtuple(dic)
    assert isinstance(nt1, namedtuple)
    assert nt1.a == 1
    assert nt1.b == 2

    dic = {'a': 1, 'b': 2}
    nt2 = to_namedtuple(dic)

# Generated at 2022-06-13 20:33:35.919918
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from types import SimpleNamespace
    from typing import (
        List,
        NamedTuple,
        NamedTupleMeta,
        Tuple,
    )

    def _check(
            obj: Union[List, Mapping, NamedTuple, SimpleNamespace, Tuple],
            expected_type: NamedTupleMeta,
            with_assert: bool = True
    ) -> None:
        out = to_namedtuple(obj)
        if with_assert:
            assert type(out) == expected_type
        else:
            assert type(out) != expected_type

    def _check_list(obj, expected_type):
        assert type(obj) == list

# Generated at 2022-06-13 20:33:46.546773
# Unit test for function to_namedtuple
def test_to_namedtuple():
    expected_out = NamedTuple(a=NamedTuple(c=1, d=2), b=NamedTuple(e=1, f=2))
    dic = {
        'a': {'c': 1, 'd': 2},
        'b': {'e': 1, 'f': 2},
    }
    out = to_namedtuple(dic)
    assert out == expected_out
    dic = {
        1: 'a',
        2: 'b',
    }
    expected_out = NamedTuple(a=NamedTuple(
        c=NamedTuple(e='a', f='b'),
    ))
    dic = NamedTuple(a=NamedTuple(
        c=dic
    ))
    out = to_namedtuple(dic)

# Generated at 2022-06-13 20:33:59.122206
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 'd'}
    assert to_namedtuple(d) == namedtuple('NamedTuple', 'a b c d')(1, 2, 3, 'd')
    assert isinstance(to_namedtuple(d), NamedTuple)
    assert to_namedtuple(d) == NamedTuple(a=1, b=2, c=3, d='d')
    assert to_namedtuple(d) == {'a': 1, 'b': 2, 'c': 3, 'd': 'd'}
    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple({}) == {}
    assert to_namedtuple([]) == []

# Generated at 2022-06-13 20:34:10.763669
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test the function to_namedtuple."""
    import pytest
    from types import SimpleNamespace

    dic = SimpleNamespace(
        a=1,
        b=2,
        c=3,
    )
    obj = to_namedtuple(dic)
    assert obj.a == dic.a == 1
    assert obj.b == dic.b == 2
    assert obj.c == dic.c == 3

    dic = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    obj = to_namedtuple(dic)
    assert obj.a == dic['a'] == 1
    assert obj.b == dic['b'] == 2
    assert obj.c == dic['c'] == 3


# Generated at 2022-06-13 20:34:14.932468
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert 'a' in nt._fields and 'b' in nt._fields
    assert nt.a == 1 and nt.b == 2
    d2 = {'a': 1, 'b': {'a': 1, 'b': 2}}
    nt = to_namedtuple(d2)
    assert 'b' in nt._fields
    assert nt.b.a == 1 and nt.b.b == 2
    a = to_namedtuple(nt)
    assert a == nt
    assert a.b.a == 1 and a.b.b == 2
    t = (1, 2, 3)
    b = to_namedtuple(t)
    assert b

# Generated at 2022-06-13 20:34:24.514307
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == \
        namedtuple('a', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple({'b': 2, 'a': 1}) == \
        namedtuple('b', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple({'b': 2, 'a': 1}) != \
        namedtuple('c', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple([1, 2, 3]) == \
        [1, 2, 3]
    assert to_namedtuple(tuple([1, 2, 3])) == \
        (1, 2, 3)

# Generated at 2022-06-13 20:34:31.022125
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': 2, '_c': 3, 'c_': 4, 'C': 5}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2, C=5)

    dic = {'a': 1, 'b': 2, '_c': 3, 'c_': 4, 'C': 5, '1': 6}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2, C=5)


# Generated at 2022-06-13 20:34:40.921576
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test function to_namedtuple."""
    from flutils.namedtupleutils import to_namedtuple
    import pytest

    dic = {'a': 1, 'b': 2, 'c': {'d': 4, 'e': 5}}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple)
    assert out.a == 1
    assert out.b == 2
    assert isinstance(out.c, namedtuple)
    assert out.c.d == 4
    assert out.c.e == 5

    dic = OrderedDict()
    dic['a'] = 1
    dic['b'] = 2
    dic['c'] = OrderedDict()
    dic['c']['d'] = 4

# Generated at 2022-06-13 20:34:45.356693
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    dic = {'x': 1, 'y': [3, 4], 'z': OrderedDict([('a', 1), ('b', 2)])}
    ret = to_namedtuple(dic)
    assert ret == namedtuple('NamedTuple', 'x y z')(
        x=1,
        y=tuple([1, 2]),
        z=namedtuple('NamedTuple', 'a b')(a=1, b=2),
    )

# Generated at 2022-06-13 20:34:55.766699
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import sys
    import platform

    # similar dicts of various types
    dic = dict(a=1, b=2)
    odic = {'a': 1, 'b': 2}
    snd = SimpleNamespace(a=1, b=2)

    # namedtuple
    nt = namedtuple('Temp', ['a', 'b'])
    ntubj = nt(1, 2)
    nt1 = to_namedtuple(nt)
    assert nt == nt1
    nt2 = to_namedtuple(ntobj)
    assert nt2 == ntubj

    # dict
    nt3 = to_namedtuple(dic)
    assert nt3.a == dic['a']
    assert nt3.b == dic['b']

    #

# Generated at 2022-06-13 20:34:58.371080
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)



# Generated at 2022-06-13 20:35:10.561543
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace

    obj = {'one': 1, 'two': 2, 'three': 3}
    out = to_namedtuple(obj)
    assert isinstance(out, SimpleNamespace)
    assert hasattr(out, 'one')
    assert hasattr(out, 'two')
    assert hasattr(out, 'three')
    assert out == obj

    obj = OrderedDict()
    obj['one'] = 1
    obj['two'] = 2
    obj['three'] = 3
    out = to_namedtuple(obj)
    assert isinstance(out, SimpleNamespace)
    assert hasattr(out, 'one')
    assert hasattr(out, 'two')
    assert hasattr(out, 'three')
    assert out == obj


# Generated at 2022-06-13 20:35:19.643267
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Define test data
    test_data = {
        '_': 42,
        'a': 1,
        'b': 2,
        'c': 3,
        'd1': {
            'a': 1,
            'b': 2,
            'c': 3,
        },
        'd2': {
            'a': 1,
            'b': 2,
            'c': 3,
        },
        'e': 5,
        'f': 6,
    }
    test_order = ['d1', 'd2']
    test_results = {
        '_': 42,
        'a': 1,
        'b': 2,
        'c': 3,
        'e': 5,
        'f': 6,
    }

    # Test against dict
    test_out = to

# Generated at 2022-06-13 20:35:33.729484
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from typing import List, Tuple


    dic: dict = {'a': 1, 'b': 2}
    res = to_namedtuple(dic)
    assert isinstance(res, tuple)
    assert res.a == 1
    assert res.b == 2

    dic = {'a': 1}
    res = to_namedtuple(dic)
    assert isinstance(res, tuple)
    assert res.a == 1

    dic: OrderedDict = OrderedDict([
        ('a', 1),
        ('b', 2)
    ])
    res = to_namedtuple(dic)
    assert isinstance(res, tuple)
    assert res.a == 1

# Generated at 2022-06-13 20:35:43.986891
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from pytest import raises
    import sys
    import types
    from collections import OrderedDict
    from typing import NamedTuple, Tuple

    # noinspection PyTypeChecker
    @to_namedtuple.register(tuple)
    def _(obj: tuple) -> Tuple[Any, ...]:
        out = []
        for item in obj:
            # noinspection PyTypeChecker
            out.append(_to_namedtuple(item))
        return tuple(out)

    # noinspection PyTypeChecker
    @to_namedtuple.register(types.SimpleNamespace)
    # noinspection PyTypeChecker
    def _(obj: types.SimpleNamespace) -> NamedTuple:
        return _to_namedtuple(obj.__dict__)

    # noins

# Generated at 2022-06-13 20:35:51.662452
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert to_namedtuple((1, 2, 3)) == (1, 2, 3)
    assert to_namedtuple('abc') == 'abc'
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3}) == \
           (1, 2, 3)
    assert to_namedtuple({'a': 1, 'b': {'c': 3}}) == \
           (1, NamedTuple(c=3))

# Generated at 2022-06-13 20:36:02.592086
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from types import SimpleNamespace
    import platform
    import sys
    import unittest
    from pprint import pprint


# Generated at 2022-06-13 20:36:17.265365
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: ignore[function-redefined]
    """Unit test for function to_namedtuple."""
    def assert_to_namedtuple(
            obj: _AllowedTypes,
            expected: Union[NamedTuple, Tuple, List]
    ):
        out = to_namedtuple(obj)
        assert out == expected
        assert out.__class__ == expected.__class__

    assert_to_namedtuple('dic', 'dic')
    assert_to_namedtuple([1, 2], [1, 2])
    assert_to_namedtuple((1, 2), (1, 2))

# Generated at 2022-06-13 20:36:29.157344
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from datetime import datetime, timezone
    from flutils.testutils import (
        AssertCallableReturnsNoException,
        AssertCallableReturns,
    )
    from flutils.typingutils import get_fullname
    from typing import List
    import pytest

# Generated at 2022-06-13 20:36:41.995141
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NT', 'a b')(a=1, b=2)
    dic = OrderedDict([(1, 'a'), (2, 'b')])
    assert to_namedtuple(dic) == namedtuple('NT', '1 2')(a='a', b='b')
    dic = {1: 'a', 3: 'b'}
    assert to_namedtuple(dic) == namedtuple('NT', '1 3')(a='a', b='b')
    dic = {1: 'a', '3': 'b'}
    assert to_namedtuple(dic) == named

# Generated at 2022-06-13 20:36:51.832308
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test to_namedtuple on different inputs"""

# Generated at 2022-06-13 20:37:03.058328
# Unit test for function to_namedtuple
def test_to_namedtuple(): # noqa: D103
    dic = {'a': 1, 'b': 2}
    tup = to_namedtuple(dic)
    assert type(tup) is namedtuple('NamedTuple', 'a b')
    assert tup.a == 1
    assert tup.b == 2
    dic = {'a': 1, 'b': 2, 'c': 3}
    tup = to_namedtuple(dic)
    assert type(tup) is namedtuple('NamedTuple', 'a b c')
    assert tup.a == 1
    assert tup.b == 2
    assert tup.c == 3
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Generated at 2022-06-13 20:37:15.017031
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a_1': 1, 'b': 2}) == NamedTuple(b=2)
    assert to_namedtuple({'a': 1, 'b': 2, '_c': 3}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2, '__c': 3}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2, '_': 3}) == NamedTuple(a=1, b=2)

# Generated at 2022-06-13 20:37:22.978975
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2}
    assert to_namedtuple(obj) == (1, 2)
    obj = OrderedDict([
        ('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7),
        ('h', 8),
    ])
    assert to_namedtuple(obj) == (1, 2, 3, 4, 5, 6, 7, 8)
    obj = SimpleNamespace(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)
    assert to_namedtuple(obj) == (1, 2, 3, 4, 5, 6, 7, 8)

# Generated at 2022-06-13 20:37:33.880592
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import Counter
    from collections import OrderedDict
    from itertools import chain
    from typing import List
    dic = {
        'a': 1,
        'b': 2,
        'c': Counter({'a': 1, 'b': 1}),
        'd': OrderedDict([('a', 1), ('b', 2)])
    }
    nt = to_namedtuple(dic)
    assert set(nt._fields) == {'a', 'b', 'c', 'd'}
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c == Counter({'a': 1, 'b': 1})
    assert nt.d == OrderedDict([('a', 1), ('b', 2)])

# Generated at 2022-06-13 20:37:47.473600
# Unit test for function to_namedtuple
def test_to_namedtuple():

    from collections import namedtuple
    from datetime import datetime
    from typing import List, Tuple


    class _Sub1(NamedTuple):
        """Sub1."""
        a: int
        b: str


    class _Sub2(NamedTuple):
        """Sub2."""
        a: int
        b: str


    class _Sub3(NamedTuple):
        """Sub3."""
        a: _Sub1
        b: _Sub2
        c: List[int]


    class _Sub4(NamedTuple):
        """Sub3."""
        a: List[int]


    _Sub5_NT = namedtuple('Sub5', 'a')



# Generated at 2022-06-13 20:37:59.157309
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.datastructures import FlatOrderedDict

    dic = FlatOrderedDict([
        ('a', 1),
        ('b', 2),
    ])
    self = to_namedtuple(dic)

    assert self.a == 1
    assert self.b == 2

    dic = OrderedDict([
        ('a', 1),
        ('b', 2),
    ])
    self = to_namedtuple(dic)

    assert self.a == 1
    assert self.b == 2

    dic = {'a': 1, 'b': 2}
    self = to_namedtuple(dic)

    assert self.a == 1
    assert self.b == 2


# Generated at 2022-06-13 20:38:13.167581
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import random
    import re
    import string

    def random_string(n: int) -> str:
        return ''.join(random.choice(string.ascii_letters) for x in range(n))

    class N(NamedTuple):
        x: int
        y: str
        z: List[int]

    class X(NamedTuple):
        x: int
        y: str
        z: N

    class Y(NamedTuple):
        x: str
        y: str
        z: List[Tuple[str, Tuple[N, str]]]

    class Z(NamedTuple):
        x: str
        y: str
        z: List[str]

    a = random.randint(1, 5)

# Generated at 2022-06-13 20:38:22.366021
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert to_namedtuple([1, 2, 3, [4, 5], 6]) == [1, 2, 3, [4, 5], 6]
    assert to_namedtuple([{'a': 1, 'b': 2}, 3, [4, 5], 6]) == [namedtuple('NamedTuple', 'a b')(1, 2), 3, [4, 5], 6]
    assert to_namedtuple((1, 2, 3, 4)) == (1, 2, 3, 4)

# Generated at 2022-06-13 20:38:28.474134
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import sys
    # noinspection PyProtectedMember
    if 'sphinx' not in sys.modules:
        from tests.test_namedtupleutils.test_to_namedtuple import (
            test_to_namedtuple
        )
        test_to_namedtuple()

# Generated at 2022-06-13 20:38:37.876010
# Unit test for function to_namedtuple
def test_to_namedtuple():
    a = {
        'a': 1,
        'b': 2,
    }
    assert to_namedtuple(a) == namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)
    a = OrderedDict(
        [
            ('c', 3),
            ('a', 1),
            ('b', 2),
        ]
    )
    assert to_namedtuple(a) == namedtuple('NamedTuple', ('c', 'a', 'b'))(c=3, a=1, b=2)


test_to_namedtuple()

# Generated at 2022-06-13 20:38:50.247615
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from flutils.namedtupleutils import to_namedtuple
    from flutils.typesutils import is_namedtuple
    from collections.abc import Mapping

    assert is_namedtuple(to_namedtuple({'a': 1, 'b': 2}))
    assert is_namedtuple(to_namedtuple(OrderedDict(a=1, b=2)))
    assert is_namedtuple(to_namedtuple(SimpleNamespace(a=1, b=2)))
    assert is_namedtuple(to_namedtuple(namedtuple('n', 'a b')(1, 2)))
    assert is_namedtuple(to_namedtuple([{'a': 1}, {'b': 2}]))


# Generated at 2022-06-13 20:39:02.563627
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifier
    from types import SimpleNamespace

    dic = OrderedDict([
        ('a', 1),
        ('b', 2),
        ('c', 3),
        ('d', 4),
    ])
    tups = (5, 6, 7, 8)
    a = 1
    b = 2
    c = 3
    d = 4

    class D:
        def __init__(
                self,
                a: int,
                b: int,
        ) -> None:
            self.a = a
            self.b = b
            self._c = 3
            self._d = 4

        def __repr__(self) -> str:
            return f

# Generated at 2022-06-13 20:39:13.728924
# Unit test for function to_namedtuple
def test_to_namedtuple():
    test_dict = {'a': 1, 'b': 2}
    assert to_namedtuple(test_dict) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)


###
# The code below is used just for type checking and is not run.
###
if TYPE_CHECKING:  # pragma: no cover
    from collections import OrderedDict
    from typing import Dict

    _AllowedTypes = Union[
        List[Any],
        Mapping,
        NamedTuple,
        OrderedDict,
        SimpleNamespace,
        Tuple,
    ]
    _Dict = Dict[str, Any]


# Generated at 2022-06-13 20:39:25.902199
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test to_namedtuple function."""
    from flutils.namedtupleutils import to_namedtuple
    nt = to_namedtuple({'a': 1, 'b': 2})
    assert nt.a == 1
    assert nt.b == 2
    nt = to_namedtuple((1, 2))
    assert nt[0] == 1
    assert nt[1] == 2
    nt = to_namedtuple(['one', 'two', 'three'])
    assert nt[0] == 'one'
    assert nt[1] == 'two'
    assert nt[2] == 'three'
    nt = to_namedtuple([{'a': 1}, {'b': 2}])
    assert len(nt) == 2

# Generated at 2022-06-13 20:39:28.224487
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-13 20:39:41.212707
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([[{'a': 1}]]) == [NamedTuple(a=1)]
    assert to_namedtuple([[{'a': 1, 'b': 2}]]) == [NamedTuple(a=1, b=2)]
    assert to_namedtuple([[{'b': 2, 'a': 1}]]) == [NamedTuple(a=1, b=2)]
    assert to_namedtuple([]) == []
    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple({'a': 1}) == NamedTuple(a=1)
    assert to_namedtuple({'b': 2, 'a': 1}) == NamedTuple(a=1, b=2)

# Generated at 2022-06-13 20:40:05.236826
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple
    from flutils.compat import is_py2

    a_dict = {'a': 1, 'b': 'two', 'c': {'3': 3.0, '4': 4.0}, 'd': SimpleNamespace(e=5, f='six')}
    result = to_namedtuple(a_dict)
    assert result.a == 1
    assert result.b == 'two'
    assert result.c.get('3') == 3.0
    assert result.c.get('4') == 4.0
    assert result.d.e == 5
    assert result.d.f == 'six'

    dic = {'a': 1, 'b': 2}
   

# Generated at 2022-06-13 20:40:15.992014
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.typing import DictLike, NamedTupleLike

    def _test_to_namedtuple(obj_in: DictLike, obj_out: NamedTupleLike) -> None:
        obj = to_namedtuple(obj_in)
        obj_out = cast(Union[NamedTuple, Tuple], obj_out)
        assert obj == obj_out
        for k, v in obj_out._asdict().items():
            assert getattr(obj, k) == v

    obj_in = {
        1: {
            'a': 2,
        },
    }
    obj_out = [
        NamedTuple(a=2),
    ]
    _test_to_namedtuple(obj_in, obj_out)


# Generated at 2022-06-13 20:40:27.379583
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: () -> None
    from flutils.namedtupleutils import to_namedtuple

    empty_list = []
    ret: List[Any] = to_namedtuple(empty_list)
    assert isinstance(ret, List)
    assert len(ret) == 0

    ret = to_namedtuple('')
    assert ret == ''

    ret = to_namedtuple('a string')
    assert ret == 'a string'

    ret = to_namedtuple((1, 2, 3, 'a string'))
    assert isinstance(ret, tuple)
    assert len(ret) == 4

    ret = to_namedtuple({'a': 1, 'b': 2})
    assert isinstance(ret, NamedTuple)
    assert len(ret._fields) == 2
    assert ret.a == 1

# Generated at 2022-06-13 20:40:34.311523
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import NamedTuple
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifiers
    import pytest
    dic1 = {'a': 1, 'b': 2}
    dic2 = {'a': 3, 'b': 4}
    dic3 = {'a': 5, 'b': 6}
    dic = {'d1': dic1, 'd2': dic2, 'd3': dic3}
    dic_expected = to_namedtuple({'d2': to_namedtuple(dic2)})
    dic_namedtuple = to_namedtuple(dic)
    assert hasattr(dic_namedtuple, 'd1')

# Generated at 2022-06-13 20:40:44.920982
# Unit test for function to_namedtuple
def test_to_namedtuple():
    a = to_namedtuple({'a': 1, 'b': 2})
    assert isinstance(a, namedtuple('namedtuple', ['a', 'b']))
    assert a.a == 1
    assert a.b == 2
    d = {1: 2, 3: 4, 5: 6}
    b = to_namedtuple(d)
    assert isinstance(b, namedtuple('namedtuple', ['1', '3', '5']))
    assert b._1 == 2
    assert b._3 == 4
    assert b._5 == 6
    d = {'a': 1, '_b': 2}
    b = to_namedtuple(d)
    assert isinstance(b, namedtuple('namedtuple', ['a']))
    assert b.a == 1

# Generated at 2022-06-13 20:40:56.622824
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2}
    out = to_namedtuple(obj)
    assert hasattr(out, 'a')
    assert hasattr(out, 'b')
    assert not hasattr(out, 'c')
    assert not hasattr(out, '_a')
    assert not hasattr(out, '_b')
    expected = {
        'a': 1,
        'b': 2,
    }
    assert out == expected
    obj = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    expected = out = to_namedtuple(obj)
    assert isinstance(out, list)

# Generated at 2022-06-13 20:41:08.635706
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import types

    def test_namedtuple_object(obj: Union[types.SimpleNamespace, dict]):
        """Test that object is converted to a namedtuple and
        serialization is correct.
        """
        nt_out = to_namedtuple(obj)
        if isinstance(nt_out, (list, tuple)):
            nt_name = 'list of namedtuples'
        else:
            nt_name = 'namedtuple'
        assert(type(nt_out).__name__ == 'NamedTuple')
        assert(len(nt_out) == 2)
        assert(hasattr(nt_out, 'a'))
        assert(hasattr(nt_out, 'b'))

# Generated at 2022-06-13 20:41:17.992774
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import flutils.convertutils

    # These should work

# Generated at 2022-06-13 20:41:27.181536
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj1 = {
        'a': 1,
        'b': {'c': 'd', 'e': 'f'},
    }
    obj2 = {
        'b': {'e': 'f', 'c': 'd'},
        'a': 1,
    }
    obj3 = {
        'b': {'c': 'd', 'e': 'f'},
        'a': 1,
        '_bad': 'nope',
    }
    obj4 = {
        'a': 1,
        'b': {'c': 'd'},
    }
    obj5 = {
        'a': 1,
        'b': [1, 2, 3],
    }
    obj6 = {
        'b': [1, 2, 3],
        'a': 1,
    }

# Generated at 2022-06-13 20:41:33.455910
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyUnresolvedReferences,PyShadowingNames
    from flutils.testutils import RunFromCLI  # pylint: disable=E0611
    return RunFromCLI(to_namedtuple).testall(__file__)


if __name__ == "__main__":
    print(test_to_namedtuple.__doc__)
    print(to_namedtuple.__doc__)
    test_to_namedtuple()

# Generated at 2022-06-13 20:42:03.931823
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from flutils.namedtupleutils import to_namedtuple

    def test_func(obj: object) -> None:
        nt_obj = to_namedtuple(obj)
        assert isinstance(nt_obj, namedtuple)

    # --------------------------------------
    # Basic types
    # --------------------------------------

    obj = ['a', 'b', 'c']
    test_func(obj)

    obj = ('d', 'e', 'f')
    test_func(obj)

    obj = {'a': 'b', 'c': 'd', 'e': 'f'}
    test_func(obj)
    assert obj['a'] != nt_obj.a

    obj = {'g': 'h', 'i': 'j', 'k': 'l'}

# Generated at 2022-06-13 20:42:05.688986
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    print(doctest.testmod(report=True))

# Generated at 2022-06-13 20:42:16.607490
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace

    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2

    lst = [dic, dic]
    lst2 = to_namedtuple(lst)
    assert lst2[0] != lst[0]
    assert repr(lst2[0]) == repr(out)
    assert repr(lst2[1]) == repr(out)

    tup = (dic, dic)
    tup2 = to_namedtuple(tup)
    assert tup2[0] != tup[0]
    assert repr(tup2[0]) == repr(out)

# Generated at 2022-06-13 20:42:27.402452
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({}) == namedtuple('NamedTuple', '')()
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a,b')(1, 2)
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3}) == namedtuple('NamedTuple', 'a,b,c')(1, 2, 3)
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == namedtuple('NamedTuple', 'a,b,c,d')(1, 2, 3, 4)

# Generated at 2022-06-13 20:42:31.266121
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d = {"a": 1, "b": 2}
    nt = to_namedtuple(d)
    assert nt.a == 1  # type: ignore

# Generated at 2022-06-13 20:42:41.234773
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({1: 2, 3: 4}) == NamedTuple(_1=2, _3=4)
    assert to_namedtuple({'a': 1, 'b': 2, '_c': 3}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a_': 1, 'b': 2, 1: 3}) == NamedTuple(b=2, _1=3)
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == NamedTuple(a=1, b=2)