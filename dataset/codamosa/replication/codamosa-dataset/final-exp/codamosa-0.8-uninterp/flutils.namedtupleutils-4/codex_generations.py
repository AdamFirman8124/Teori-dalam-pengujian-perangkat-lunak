

# Generated at 2022-06-13 20:32:52.714924
# Unit test for function to_namedtuple
def test_to_namedtuple():
    t = to_namedtuple({'a': 1, 'b': 2})
    assert t.a == 1
    assert t.b == 2
    t = to_namedtuple({'a': 1, 'b': 2, 1: 3})
    assert t.a == 1
    assert t.b == 2
    t = to_namedtuple(OrderedDict({'a': 1, 'b': 2, 1: 3}))
    assert t.a == 1
    assert t.b == 2
    from types import SimpleNamespace
    d = {'a': 1, 'b': 2}
    t = SimpleNamespace(**d)
    t = to_namedtuple(t)
    assert t.a == 1
    assert t.b == 2

# Generated at 2022-06-13 20:33:04.482157
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from collections import OrderedDict


# Generated at 2022-06-13 20:33:13.816167
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    dic_ord = OrderedDict(a=1, b=2)
    dic_spaced = SimpleNamespace(a=1, b=2)
    out_dic = to_namedtuple(dic)
    out_dic_ord = to_namedtuple(dic_ord)
    out_dic_spaced = to_namedtuple(dic_spaced)
    assert hasattr(out_dic, 'a')
    assert hasattr(out_dic, 'b')
    assert out_dic.a == out_dic.b == 1
    assert hasattr(out_dic_ord, 'a')
    assert hasattr(out_dic_ord, 'b')
    assert out_dic_

# Generated at 2022-06-13 20:33:24.760494
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.typingutils import DictItems, DictItemsView
    from collections import OrderedDict
    from types import SimpleNamespace

    # noinspection PyTypeChecker
    lst = ['a', SimpleNamespace(a=1), 'b', OrderedDict([
        ('c', 2),
        ('d', 3),
    ])
    ]
    lst = to_namedtuple(lst)
    assert isinstance(lst, list)
    assert isinstance(lst[1], NamedTuple)
    assert isinstance(lst[3], NamedTuple)
    assert lst[1].a == 1
    assert lst[3].c == 2
    assert lst[3].d == 3

    # noinspection Py

# Generated at 2022-06-13 20:33:26.756446
# Unit test for function to_namedtuple
def test_to_namedtuple():
    print("====Started executing to_namedtuple unit test====")
    dic = {'a': 1, 'b': 2}
    print("====End of function to_namedtuple unit test====")

# Generated at 2022-06-13 20:33:36.795630
# Unit test for function to_namedtuple
def test_to_namedtuple():

    import collections

    class _Point(
            collections.namedtuple(
                'Point',
                ('x', 'y'),
            )
    ):

        __slots__ = ()

        def __new__(cls, x, y):
            return super().__new__(cls, x, y)

    point = _Point(11, y=22)

    assert to_namedtuple(point) == point
    assert to_namedtuple(list(point)) == list(point)
    assert to_namedtuple(point._asdict()) == point
    assert to_namedtuple(point._fields) == point._fields
    assert to_namedtuple(point._replace(x=33)) == point._replace(x=33)

# Generated at 2022-06-13 20:33:46.870104
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import deque
    from collections.abc import Iterable
    from collections import namedtuple
    from types import SimpleNamespace

    # noinspection PyTypeChecker
    dd: Iterable[str] = deque(['a', 'b'])
    # noinspection PyTypeChecker
    nt: NamedTuple[str, str] = namedtuple('NamedTuple', ['a', 'b'])('c', 'd')
    # noinspection PyTypeChecker
    ns: SimpleNamespace = SimpleNamespace(e='f', g='h')
    # noinspection PyTypeChecker
    ntns: NamedTuple[str, str] = namedtuple('NamedTuple', ['e', 'g'])('i', 'j')

# Generated at 2022-06-13 20:33:59.312328
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    from flutils.namedtupleutils import to_namedtuple

    #: dictionary for external function
    dic = {'a': 1, 'b': 2}

    #: dictionary for internal function
    _dic = {'a': 1, 'b': 2}

    #: dictionary for external function
    odic = OrderedDict([('a', 1), ('b', 2), ('c', "A string"), ('d', 77.3)])

    #: dictionary for internal function
    _odic = OrderedDict([('a', 1), ('b', 2), ('c', "A string"), ('d', 77.3)])

    #: dictionary for external function
    odict = {'a': 1, 'b': 2, 'c': "A string", 'd': 77.3}

    #

# Generated at 2022-06-13 20:34:00.025917
# Unit test for function to_namedtuple
def test_to_namedtuple():
    pass

# Generated at 2022-06-13 20:34:06.135216
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint

    lst = [
        [{'b': 1, 'a': 2}, {'c': '3', 'a': 4}],
        [{'a': '2', 'b': (1, 2)}, {'c': '3', 'a': 4}],
    ]
    out = to_namedtuple(lst)
    pprint(out)

# Generated at 2022-06-13 20:34:16.233829
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import functools
    import types
    import unittest

    from flutils.namedtupleutils import to_namedtuple # noqa: E402

    @functools.lru_cache
    def _cached_test(dic: dict, recursive: bool = False):
        test = to_namedtuple(dic)
        if recursive:
            for attr in test._fields:
                val = getattr(test, attr)
                if isinstance(val, types.SimpleNamespace):
                    val = _cached_test(val.__dict__, recursive=True)
                elif isinstance(val, dict):
                    val = _cached_test(val, recursive=True)
                elif isinstance(val, tuple):
                    val = _cached_test(list(val), recursive=True)


# Generated at 2022-06-13 20:34:25.273675
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    d = dict(a=1, b=2)
    expected = namedtuple('NamedTuple', 'a,b')(a=1, b=2)
    assert to_namedtuple(d) == expected

    d = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    expected = namedtuple('NamedTuple', 'a,b,c')(a=1, b=2, c=3)
    assert to_namedtuple(d) == expected

    d = SimpleNamespace(a=1, b=2)
    expected = namedtuple('NamedTuple', 'a,b')(a=1, b=2)
    assert to_namedtuple(d) == expected


# Generated at 2022-06-13 20:34:37.331848
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase

    class Test(TestCase):
        # noinspection PyUnresolvedReferences
        def test_to_namedtuple(self):
            from collections import OrderedDict

            from flutils.namedtupleutils import to_namedtuple
            from flutils.validators import is_identifier

            # dict
            arg = dict(name='test1', user='dog')
            val = to_namedtuple(arg)
            self.assertEqual(vars(val), arg)
            self.assertTrue(hasattr(val, 'user'))
            self.assertTrue(hasattr(val, 'name'))
            self.assertEqual(getattr(val, 'user'), 'dog')
            self.assertEqual(getattr(val, 'name'), 'test1')

            # Ord

# Generated at 2022-06-13 20:34:48.668979
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from datetime import datetime
    from typing import Deque

    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import (
        is_float,
        is_int,
        is_list,
        is_namedtuple,
        is_string,
        is_datetime,
        is_bytes,
        is_memoryview,
        is_deque,
    )

    # Empty lists, tuples, and dicts
    assert is_namedtuple(to_namedtuple([]))
    assert is_namedtuple(to_namedtuple(tuple()))
    assert is_namedtuple(to_namedtuple({}))
    assert is_namedtuple(to_namedtuple(OrderedDict({})))


# Generated at 2022-06-13 20:34:57.893283
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1}) == namedtuple(
        'NamedTuple', ('a')
    )(1)
    assert to_namedtuple({'a': 1, 'b': [1, 2, 3]}) == namedtuple(
        'NamedTuple', ('a', 'b')
    )(
        1,
        [1, 2, 3]
    )
    assert to_namedtuple({'a': {'b': 2, 'c': 3}}) == namedtuple(
        'NamedTuple', ('a',)
    )(
        namedtuple('NamedTuple', ('b', 'c'))(2, 3)
    )
    assert to_namedtuple(['a', 1]) == ['a', 1]

# Generated at 2022-06-13 20:35:09.993803
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    from flutils.fltest import TestCase
    from flutils.namedtupleutils import to_namedtuple
    from flutils._compat import PY35, PY37

    class TestToNamedTuple(TestCase):
        def test_empty(self):
            """Test empty args/kwargs."""
            # noinspection PyTypeChecker
            got = to_namedtuple([])
            # noinspection PyTypeChecker
            self.assertEqual(got, [])
            got = to_namedtuple({})
            self.assertEqual(got, namedtuple('NamedTuple', '')())
            got = to_namedtuple(())
            self.assertEqual(got, namedtuple('NamedTuple', '')())
            got = to_

# Generated at 2022-06-13 20:35:19.315469
# Unit test for function to_namedtuple
def test_to_namedtuple():

    from flutils.namedtupleutils import to_namedtuple

    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert isinstance(nt, tuple)
    assert nt.a == 1
    assert nt.b == 2
    assert nt == (1, 2)

    dic = OrderedDict([('a', 1), ('b', 2)])
    nt = to_namedtuple(dic)
    assert isinstance(nt, tuple)
    assert nt.a == 1
    assert nt.b == 2
    assert nt == (1, 2)

    lis = [1, 2, 3]
    nt = to_namedtuple(lis)
    assert isinstance(nt, list)

# Generated at 2022-06-13 20:35:33.452336
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2

    dic = {'a': 1, 'b': 2, '_c': 3, '_d': 4, 'C': 5, 'D': 6}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    assert not hasattr(out, '_c')
    assert not hasattr(out, '_d')
    assert not hasattr(out, 'C')
    assert not hasattr(out, 'D')


# Generated at 2022-06-13 20:35:43.810648
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from types import SimpleNamespace
    from typing import List

    NamedTuple = namedtuple('NamedTuple', 'a b c')
    SimpleTuple = namedtuple('SimpleTuple', 'a b c')
    SimpleList = [SimpleTuple(1, 2, 3), SimpleTuple(4, 5, 6)]
    SimpleDict = SimpleNamespace(a=1, b=2, c=3)
    SimpleDictList = [
        SimpleDict(a=1, b=2, c=3),
        SimpleDict(a=4, b=5, c=6),
    ]

# Generated at 2022-06-13 20:35:53.044154
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.miscutils import cached_property
    class adict:
        _data = {'a': 1, 'b': 2}
        _attr = {'c': 3, 'd': 4}

        def __contains__(self, item):
            return item in self._data

        def __getitem__(self, item):
            return self._data[item]

        def __iter__(self):
            return iter(self._data)

        def __len__(self):
            return len(self._data)

        @property
        def props(self):
            return {k: v for k, v in self._data.items() if k.isupper()}


# Generated at 2022-06-13 20:36:04.264012
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        'a': 1,
        'b': 2,
        'c': {
            'd': 3,
            'e': [1, 2, 3],
            'f': ('g', 'h', 'i'),
            'j': {
                'k': 4,
                'l': 5,
                'm': [6, 7, 8],
            },
            'n': {
                'o': 9,
                'p': [10, 11, 12, 13],
            },
        },
    }

# Generated at 2022-06-13 20:36:16.856821
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:36:28.731340
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test function to_namedtuple"""
    listobj = ['str', 0, [1, 2, 3], {'one': 1, 'two': 2}]
    tupobj = tuple(listobj)
    dicobj = OrderedDict(a=1, b=2, c=3, d=4)
    obj = SimpleNamespace(a=1, b=2, c=3)
    obj.d = 4
    obj.e = [1, 2, 3]
    obj.f = {'one': 1, 'two': 2}

    assert to_namedtuple(listobj) == [
        'str', 0, [1, 2, 3], NamedTuple(one=1, two=2)]

# Generated at 2022-06-13 20:36:35.924834
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict

    for val in (
            [],
            (),
            '',
            {},
            OrderedDict(),
            SimpleNamespace(),
    ):
        assert to_namedtuple(val) == val

    assert to_namedtuple(SimpleNamespace(a=1)) == namedtuple('NamedTuple', 'a')(1)

    assert to_namedtuple([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

    assert to_namedtuple(([1, 2], [3, 4])) == ((1, 2), (3, 4))

    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(1, 2)

    assert to_namedtuple

# Generated at 2022-06-13 20:36:45.963148
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    namedt = to_namedtuple(dic)
    assert namedt.a == 1 and namedt.b == 2
    dic = {'a': 1, 'b': [{'c': 3, 'd': 4}]}
    namedt = to_namedtuple(dic)
    assert namedt.a == 1 and namedt.b[0].c == 3
    dic = {'a': 1, 'b': [{'c': 3, 'd': 4}]}
    namedt = to_namedtuple(dic)
    assert namedt.a == 1 and namedt.b[0].c == 3



# Generated at 2022-06-13 20:36:51.787905
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([1,2,3]) == (1,2,3)
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': {'c':3}}) == NamedTuple(a=1, b=NamedTuple(c=3))
    assert to_namedtuple({'_a': 1, 'b': 2}) == NamedTuple(b=2)

# Generated at 2022-06-13 20:37:03.058565
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import (
        Counter,
        OrderedDict,
        defaultdict,
    )

    # noinspection PyUnresolvedReferences
    def test_func(obj: Any) -> bool:
        """Test function."""
        from flutils.typesutils import (
            is_dict_like,
            is_namedtuple,
            is_seq_like,
        )

        if is_dict_like(obj):
            for item in obj.values():
                if not test_func(item):
                    return False
            return True
        if is_seq_like(obj):
            for item in obj:
                if not test_func(item):
                    return False
            return True
        return is_namedtuple(obj)


# Generated at 2022-06-13 20:37:15.016636
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(['a', 'b']) == NamedTuple(a='a', b='b')
    assert to_namedtuple(['a', 'b', 'a']) == NamedTuple(a='a', b='b', c='a')
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': 1, 'b': 2, 'a': 1}) == NamedTuple(a=1, b=2)
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == NamedTuple(a=1, b=2)

# Generated at 2022-06-13 20:37:23.447211
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple
    """
    import os
    import sys
    import tempfile

    sys.path[0:0] = [os.path.abspath(os.path.join(__file__, '..'))]
    from tests.utils import redirect_stdout, redirect_stderr

    log = []

    # noinspection PyShadowingNames
    def log_exc(*args, **kwargs):
        # noinspection PyShadowingNames
        import sys

        print(file=sys.stdout, *args, **kwargs)
        # noinspection PyTypeChecker
        log.append(args[0])

    from flutils.exceptionutils import (
        CustomError,
        SafeException,
    )

# Generated at 2022-06-13 20:37:34.121019
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple"""
    import unittest

    class TestToNamedTuple(unittest.TestCase):
        """Unit Tests for function to_namedtuple"""


# Generated at 2022-06-13 20:37:49.088212
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """
    Unit tests for to_namedtuple.
    """
    from collections import OrderedDict
    from types import SimpleNamespace

    testobj = SimpleNamespace(
        a="b",
        b=1,
        c=OrderedDict(
            [
                ('a', 1),
                ('b', 2),
                ('c', 3),
            ]
        ),
        d=SimpleNamespace(
            a=1,
            b=2,
            c=3,
        ),
        e=["a", "b", "c"],
    )

    nt = to_namedtuple(testobj)
    assert nt.a == "b"
    assert nt.b == 1
    assert nt.c.a == 1
    assert nt.c.b == 2
    assert nt

# Generated at 2022-06-13 20:37:54.542217
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d = {
        'a': 1,
        'b': 2,
        'c': {
            'd': 3,
            'e': 4,
            'f': 5
        }
    }

    t: NamedTuple = to_namedtuple(d)
    assert hasattr(t, 'a')
    assert hasattr(t, 'b')
    assert hasattr(t, 'c')
    assert t.a == 1
    assert t.b == 2
    assert isinstance(t.c, NamedTuple)
    assert hasattr(t.c, 'd')
    assert hasattr(t.c, 'e')
    assert hasattr(t.c, 'f')
    assert t.c.d == 3
    assert t.c.e == 4
    assert t.c.f == 5



# Generated at 2022-06-13 20:38:02.514079
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # Setup the testing sample
    lst = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]

# Generated at 2022-06-13 20:38:12.389147
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    from flutils.testingutils import timed
    import os
    import random

    from flutils.dotdottuple import wrap
    from flutils.miscutils import (
        get_random_string,
    )


    # Basic mapping.
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == wrap(('a', 'b'), (1, 2))
    dic = OrderedDict()
    dic['a'] = 1
    dic['b'] = 2
    assert to_namedtuple(dic) == wrap(('a', 'b'), (1, 2))
    nspc = SimpleNamespace(**dic)

# Generated at 2022-06-13 20:38:22.050135
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    dic = OrderedDict()
    dic['item1'] = 'a'
    dic['item2'] = 'b'
    dic['item3'] = 'c'
    dic['item4'] = 1
    dic['item5'] = 2
    dic['item6'] = 3
    dic['item7'] = [1, 2, 3]
    dic['item8'] = ['x', 'y', 'z']
    dic['item9'] = {'a': 1, 'b': 2}

    nt = to_namedtuple(dic)
    assert nt.item1 == 'a'
    assert nt.item2 == 'b'
    assert nt.item3 == 'c'
    assert nt.item4 == 1


# Generated at 2022-06-13 20:38:28.745044
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from typing import NamedTuple

    obj = {'a': 1, 'b': 2}
    result = to_namedtuple(obj)
    expected_type = NamedTuple('NamedTuple', [('a', int), ('b', int)])
    assert isinstance(result, expected_type)
    expected = expected_type(a=1, b=2)
    assert result == expected



# Generated at 2022-06-13 20:38:36.711175
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, namedtuple('NamedTuple', 'a b')),\
        'Actual: %s' % out
    assert hasattr(out, 'b'), 'Actual: %s' % out
    assert hasattr(out, 'a'), 'Actual: %s' % out
    assert out.a == 1, 'Actual: %s' % out
    assert out.b == 2, 'Actual: %s' % out


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:38:45.154218
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == dic['a']
    assert out.b == dic['b']
    dic = {'pyClassName': 'test_class_name'}
    out = to_namedtuple(dic)
    assert out.pyClassName == dic['pyClassName']
    


# Generated at 2022-06-13 20:38:53.620909
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict

    dic: Mapping = {
        '_a': 'a',
        'a1': 'val1',
        'a2': 'val2',
        'a3': {
            'b1': 'val3',
            'b2': 'val4',
            'b3': OrderedDict([('c1', 'val5'), ('c2', 'val6')])
        }
    }
    out = to_namedtuple(dic)

# Generated at 2022-06-13 20:39:01.759374
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils.test import test_to_namedtuple
    from flutils.namedtupleutils.test import _NamedTuple
    test_to_namedtuple(_to_namedtuple, _NamedTuple)

if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    from flutils.namedtupleutils.test import run_tests
    run_tests(test_to_namedtuple)

# Generated at 2022-06-13 20:39:25.634274
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from types import SimpleNamespace

    dic = OrderedDict(a=1, b=2)
    obj = SimpleNamespace(a=1, b=2)

    namedtuple_ = to_namedtuple(dic)
    assert namedtuple_.a == dic['a']
    assert namedtuple_.b == dic['b']

    namedtuple_ = to_namedtuple(obj)
    assert namedtuple_.a == obj.a
    assert namedtuple_.b == obj.b



# Generated at 2022-06-13 20:39:39.464645
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest.mock import MagicMock
    from collections import (
        namedtuple,
        OrderedDict,
    )
    from types import SimpleNamespace
    from typing import List

    ns = SimpleNamespace(
        a=1,
        b=2,
        c=SimpleNamespace(
            d=3,
        ),
    )

    dic = {'a': 1, 'b': 2, 'c': ns}
    odic = OrderedDict({'a': 1, 'b': 2})

    ListT = List[NamedTuple]

    make_mock = MagicMock(return_value=1)
    namedtuple = namedtuple('NamedTuple', ('a', 'b', 'c', 'd'))

    out = to_namedtuple(dic)

# Generated at 2022-06-13 20:39:51.677692
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # tests a list
    l = ['a', 'b', 'c']
    t1 = to_namedtuple(l)
    assert t1 == ('a', 'b', 'c')

    # tests a tuple
    t = ('a', 'b', 'c')
    t2 = to_namedtuple(t)
    assert t2 == ('a', 'b', 'c')

    # tests a dict
    d = {'a': 1, 'b': 2, 'c': 3}
    t3 = to_namedtuple(d)
    assert t3 == NamedTuple(a=1, b=2, c=3)

    # tests a dict with bad keys
    d = {1: 1, 'b': 2, 'c': 3}
    t4 = to_namedtuple(d)
    assert t

# Generated at 2022-06-13 20:39:56.366921
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    import doctest
    doctest.testmod(verbose=True, extraglobs={})


if __name__ == "__main__":
    test_to_namedtuple()

# Generated at 2022-06-13 20:40:07.343443
# Unit test for function to_namedtuple
def test_to_namedtuple():
    class Dummy(object):
        def __init__(self, input_obj):
            self.in_obj = input_obj

    dic = {
        'a': 1,
        'b': 2,
        'c': 3,
        None: [
            {
                'd': 4,
                'e': 5,
                'f': 6,
                None: [
                    7,
                    8,
                    9,
                    {
                        'g': 10,
                        'h': 11,
                        'i': 12,
                    }
                ],
                'j': {
                    'k': 13,
                    'l': 14,
                    'm': 15,
                }
            }
        ]
    }
    dic_empty = {}

# Generated at 2022-06-13 20:40:12.068600
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import collections
    
    od = collections.OrderedDict({'a': 1, 'b': 2})
    nt = to_namedtuple(od)
    assert(nt.a == 1)
    
if __name__ == '__main__': # pragma: no cover
    test_to_namedtuple()

# Generated at 2022-06-13 20:40:22.420785
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from collections.abc import Sequence
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple
    from types import SimpleNamespace
    from typing import NamedTuple

    obj = {'a': 1, 'b': 2}
    assert isinstance(to_namedtuple(obj), namedtuple)
    assert hasattr(to_namedtuple(obj), 'a')
    assert hasattr(to_namedtuple(obj), 'b')

    obj = {'a': 1, 2: True}
    obj = to_namedtuple(obj)
    assert isinstance(obj, namedtuple)
    assert hasattr(obj, 'a')
    assert not hasattr(obj, 'b')
    assert not hasattr(obj, 2)


# Generated at 2022-06-13 20:40:28.585349
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj1 = SimpleNamespace(a=1, b=2, c=SimpleNamespace(d=3, e=4))
    keys = tuple(sorted(obj1.__dict__.keys()))
    assert to_namedtuple(obj1).__class__.__name__ == 'NamedTuple'
    assert getattr(to_namedtuple(obj1), 'a') == 1
    assert getattr(to_namedtuple(obj1), 'b') == 2
    assert hasattr(getattr(to_namedtuple(obj1), 'c'), 'd')
    assert getattr(getattr(to_namedtuple(obj1), 'c'), 'd') == 3
    assert hasattr(getattr(to_namedtuple(obj1), 'c'), 'e')

# Generated at 2022-06-13 20:40:38.140810
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(range(5)) == list(range(5))
    assert to_namedtuple(tuple(range(5))) == tuple(range(5))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))
    a = SimpleNamespace(c=1, b=2, a=3)
    b = SimpleNamespace(b=2, a=3, c=1)
    c = SimpleNamespace(a=3, b=2, c=1)
    obj = to_named

# Generated at 2022-06-13 20:40:46.151059
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Function to_namedtuple
    """

    from collections import OrderedDict
    from flutils.misc import testit

    @testit
    def test_1():
        dic = {'a': 1, 'b': 2}
        assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(1, 2)

        dic = {'a': 1, 'b': 2, 'c': 3}
        assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b c')(1, 2, 3)

        dic = {'a': 1, 'b': 2, 'c': 3, '_d': 4, 'e_': 5}

# Generated at 2022-06-13 20:41:07.895734
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Test lists
    assert to_namedtuple([]) == tuple()
    assert to_namedtuple(['a']) == tuple(['a'])
    assert to_namedtuple((1,)) == tuple((1,))
    assert to_namedtuple([1]) == tuple([1])
    assert to_namedtuple([1, [2, 3]]) == tuple([1, [2, 3]])
    assert to_namedtuple([{'a': 1, 'b': 2}]) == tuple(
        [NamedTuple(a=1, b=2)]
    )
    assert to_namedtuple([[{'a': 1, 'b': 2}]]) == tuple(
        [[NamedTuple(a=1, b=2)]]
    )

# Generated at 2022-06-13 20:41:17.936543
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []

    assert to_namedtuple(1) == 1

    assert to_namedtuple('a') == 'a'

    assert to_namedtuple({}) == NamedTuple()

    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)

    assert to_namedtuple({'_a': 1, 'b': 2}) == NamedTuple(b=2)

    assert to_namedtuple({'a': 1, 2: 3}) == NamedTuple(a=1)


# Generated at 2022-06-13 20:41:27.183228
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Example 1
    dic = {'a': 1, 'b': 2}
    named_tuple = to_namedtuple(dic)
    assert named_tuple.a == 1
    assert named_tuple.b == 2

    # Example 2
    dic = {'a': 1, 'b': 2}
    list_obj = [dic]
    named_tuple = to_namedtuple(list_obj)
    assert named_tuple[0].a == 1
    assert named_tuple[0].b == 2

    # Example 3
    dic = {'a': 1, 'b': 2}
    tuple_obj = (dic,)
    named_tuple = to_namedtuple(tuple_obj)
    assert named_tuple[0].a == 1
    assert named_

# Generated at 2022-06-13 20:41:38.159855
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert isinstance(nt, namedtuple)
    assert list(nt._fields) == ['a', 'b']
    assert (nt.a, nt.b) == (1, 2)
    dic = {'a': 1, 'b': 2, '_c': 3}
    nt = to_namedtuple(dic)
    assert isinstance(nt, namedtuple)
    assert list(nt._fields) == ['a', 'b']
    assert (nt.a, nt.b) == (1, 2)

# Generated at 2022-06-13 20:41:48.672612
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        'c': 1,
        'a1': 2,
        'b': 3
    }
    assert to_namedtuple(dic) == NamedTuple(a1=2, b=3, c=1)

    dic['_c'] = 4
    assert to_namedtuple(dic) == NamedTuple(a1=2, b=3, c=1)

    dic = {
        'c': 1,
        '_a1': 2,
        '_b': 3
    }
    assert to_namedtuple(dic) == NamedTuple(c=1)

    nested = [
        dic,
        1,
        [dic, 2],
        [1, dic],
    ]

# Generated at 2022-06-13 20:41:59.009998
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from datetime import date
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    dic = OrderedDict({'a': 1, 'b': 2})
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)
    lst = [1, 2, 3]
    assert to_namedtuple(lst) == [1, 2, 3]
    lst = (1, 2, 3)
    assert to_namedtuple(lst) == (1, 2, 3)
    lst = date.today(), 2, 3
    assert to_named

# Generated at 2022-06-13 20:42:04.964688
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple"""
    import os
    import sys
    import unittest

    from collections import (
        OrderedDict,
    )
    from types import SimpleNamespace

    PyVer = sys.version_info[:2]

    class TestToNamedtuple(unittest.TestCase):
        """Test function to_namedtuple"""


# Generated at 2022-06-13 20:42:16.102809
# Unit test for function to_namedtuple
def test_to_namedtuple():

    from flutils.namedtupleutils import to_namedtuple
    import tempfile

    # Simple case:
    actual = to_namedtuple({'a': 1, 'b': 2})
    assert actual == NamedTuple(a=1, b=2)

    # Nested case:
    actual = to_namedtuple({'a': 1, 'b': {'c': 3, 'd': 4}})
    assert actual == NamedTuple(a=1, b=NamedTuple(c=3, d=4))

    # Empty case:
    actual = to_namedtuple({})
    assert actual == NamedTuple()

    # NamedTuple case:

# Generated at 2022-06-13 20:42:26.928201
# Unit test for function to_namedtuple
def test_to_namedtuple():
    def run_test(obj: Any, exp: Any) -> None:
        assert_equal(to_namedtuple(obj), exp)

    obj = {
        'a': {
            'b': {
                'c': 1, 'd': 2,
            }
        },
        'e': 'f',
        'g': [
            'h', 'i',
        ],
    }
    exp = NamedTuple(
        a=NamedTuple(
            b=NamedTuple(
                c=1, d=2,
            ),
        ),
        e='f',
        g=[
            'h', 'i',
        ],
    )
    run_test(obj, exp)


# Generated at 2022-06-13 20:42:38.890195
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple

    class Test_to_namedtuple(unittest.TestCase):
        def test_empty_sequence(self):
            self.assertEqual(to_namedtuple([]), [])
            self.assertEqual(to_namedtuple(()), ())

        def test_empty_dict(self):
            self.assertEqual(to_namedtuple({}), namedtuple('NamedTuple', '')())
            self.assertEqual(to_namedtuple(OrderedDict()), namedtuple('NamedTuple', '')())
