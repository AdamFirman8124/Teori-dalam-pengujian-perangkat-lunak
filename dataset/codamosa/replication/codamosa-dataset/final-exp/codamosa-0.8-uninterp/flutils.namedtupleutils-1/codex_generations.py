

# Generated at 2022-06-13 20:32:55.248069
# Unit test for function to_namedtuple
def test_to_namedtuple():
    def _assert_equal(left, right):
        if left != right:
            raise AssertionError("%s != %s" % (left, right))
    def _assert_type(obj, classinfo):
        if not isinstance(obj, classinfo):
            raise AssertionError("%s NOT %s" % (obj, classinfo))
    dic = {'a': 1, 'b': 2}
    lis = [1, 2, 3]
    lis_with_dic = [1, dic, 3]
    tup = (1, 2, 3)
    tup_with_dic = (1, dic, 3)
    dic_with_dic = {'a': 1, 'b': dic}

# Generated at 2022-06-13 20:32:56.752207
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:33:06.139838
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # Test that allow a list
    lst = [OrderedDict({'a': 1, 'b': 2}), {'a': 1, 'b': 2}]
    assert to_namedtuple(lst) == [NamedTuple(a=1, b=2), NamedTuple(a=1, b=2)]

    # Test that allow a tuple
    tup = (OrderedDict({'a': 1, 'b': 2}), {'a': 1, 'b': 2})
    assert to_namedtuple(tup) == (NamedTuple(a=1, b=2), NamedTuple(a=1, b=2))

    # Test that allow a deque
    try:
        from collections import deque
    except ImportError:
        pass
    else:
        deq = de

# Generated at 2022-06-13 20:33:14.402295
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:33:29.112998
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Verify the docstring examples
    dic = {'a': 1, 'b': 2, 'c': 3}
    order_dic = OrderedDict(sorted(dic.items()))
    args = []
    args.append(dic)
    args.append(order_dic)
    args.append(SimpleNamespace(**dic))
    for arg in args:
        # noinspection PyTypeChecker
        results: NamedTuple = to_namedtuple(arg)
        assert isinstance(results, NamedTuple)
        assert results.a == 1
        assert results.b == 2
        assert results.c == 3

    # Test the various return types
    dic = {'a': 1, 'b': 2, 'c': 3}
    lst = [1, 2, 3]


# Generated at 2022-06-13 20:33:37.814257
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict, namedtuple
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple([]) == []

    assert to_namedtuple((), OrderedDict(), namedtuple('x', '')) == (
        (), OrderedDict(),
        namedtuple('x', '')()
    )

    assert to_namedtuple(
        [OrderedDict(), (), namedtuple('x', '')]
    ) == [OrderedDict(), (), namedtuple('x', '')()]

    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]

    assert to_namedtuple((1, 2, 3)) == (1, 2, 3)


# Generated at 2022-06-13 20:33:38.414797
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert False

# Generated at 2022-06-13 20:33:47.617085
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.testutils import (
        StrRepresentationTestMixin,
        TestCase,
    )

    class ToNamedtupleTest(StrRepresentationTestMixin, TestCase):

        def setUp(self) -> None:
            self.obj = {'a': 1, 'b': 2, '__c': 3}
            self.expected = namedtuple(
                'NamedTuple',
                ['a', 'b']
            )(a=1, b=2)

        def test_to_namedtuple_dict(self) -> None:
            self.assertEqual(to_namedtuple(self.obj), self.expected)

        def test_to_namedtuple_ordereddict(self) -> None:
            from collections import OrderedDict

# Generated at 2022-06-13 20:33:59.750690
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import copy
    import sys
    import types
    import unittest

    from collections import (
        OrderedDict,
    )
    from functools import singledispatch

    from types import SimpleNamespace

    # noinspection SpellCheckingInspection,PyUnresolvedReferences,PyShadowingBuiltins,PyPackageRequirements
    class TestToNamedtuple(unittest.TestCase):
        # Testing the function to_namedtuple()

        def test_to_namedtuple_helper(self):
            # Testing the helper function _to_namedtuple()

            # noinspection PyUnresolvedReferences
            class TheClass:
                def __init__(self):
                    self.name = 'Kathy'

            # noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:34:11.278957
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import Dict, List, Union
    from collections import namedtuple

    obj = dict(a=1, b=2)
    obj = to_namedtuple(obj)
    assert isinstance(obj, namedtuple), " Failed namedtuple"

    obj = dict(a=dict(a=1), b=2)
    obj = to_namedtuple(obj)
    assert isinstance(obj.a, namedtuple), " Failed namedtuple"

    obj = dict(a=dict(a=dict(a=1)), b=2)
    obj = to_namedtuple(obj)
    assert isinstance(obj.a, namedtuple) and \
           isinstance(obj.a.a, namedtuple), " Failed namedtuple"


# Generated at 2022-06-13 20:34:23.970145
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import collections
    import sys

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == collections.namedtuple('NamedTuple', 'a b')(1, 2)

    ntup = collections.namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple(ntup) == collections.namedtuple('NamedTuple', 'a b')(1, 2)

    test_list = [True, 'yes', 1, None, {'b': 2}, (1, 'b'), [True, 1, 'yes']]

# Generated at 2022-06-13 20:34:29.395190
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # TODO: Add more tests
    dic = {'a': 1, 'b': 2}
    expected = namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)
    actual = to_namedtuple(dic)
    assert actual == expected



# Generated at 2022-06-13 20:34:39.268104
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test application of function to_namedtuple."""
    from typing import (
        Any,
        List,
        Tuple,
        Union,
    )
    from types import SimpleNamespace
    from collections import OrderedDict
    from flutils.textutils import clean_identifier
    from flutils.namedtupleutils import to_namedtuple
    from itertools import permutations
    _AllowedTypes = Union[List, Tuple, OrderedDict, SimpleNamespace]
    # Test items that cannot be converted

# Generated at 2022-06-13 20:34:51.631067
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Tests for function to_namedtuple."""
    import pytest
    from datetime import date
    from datetime import time
    from datetime import datetime
    from datetime import timedelta
    from collections import OrderedDict

    from flutils.namedtupleutils import to_namedtuple

    class FauxNamedTup(namedtuple('NamedTuple', ['a', 'b'])):
        def __repr__(self):
            return 'FauxNamedTup'

    class FauxNamedTup2(namedtuple('NamedTuple', ['c', 'd'])):
        def __repr__(self):
            return 'FauxNamedTup2'


# Generated at 2022-06-13 20:35:03.740075
# Unit test for function to_namedtuple
def test_to_namedtuple():
  assert to_namedtuple([{'a': 1}, (1, 2, 3)]) == [NamedTuple(a=1), (1, 2, 3)]
  assert to_namedtuple([{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]) ==\
           [NamedTuple(a=1, b=2), NamedTuple(a=1, b=2)]
  assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
  assert to_namedtuple({'a': 1, 'b': [1, 2, 3]}) == NamedTuple(a=1, b=(1, 2, 3))

# Generated at 2022-06-13 20:35:14.459163
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # noinspection SpellCheckingInspection
    """
    Unit test for function to_namedtuple
    """
    import unittest

    class ToNamedTupleTest(unittest.TestCase):

        def test_to_namedtuple(self):
            # noinspection SpellCheckingInspection
            """
            Test function to_namedtuple
            """
            from flutils.namedtupleutils import to_namedtuple

            # Can convert only 'list', 'tuple', 'dict'
            with self.assertRaises(TypeError):
                to_namedtuple(True)

            # 'dict'
            dic = {'a': 1, 'b': 2}
            self.assertEqual(
                to_namedtuple(dic),
                dic,
            )

            # 'OrderedD

# Generated at 2022-06-13 20:35:28.928900
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest


# Generated at 2022-06-13 20:35:41.340149
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint
    from string import ascii_letters
    from collections import namedtuple, Sequence

    val = namedtuple('A', 'b, c')
    val = val(b=2, c=3)
    assert to_namedtuple(val).b == 2
    assert to_namedtuple(val).c == 3

    val = [
        {'a': 1, 'b': 2},
        {'a': 2, 'b': 2},
        {'a': 3, 'b': 2},
    ]
    val = to_namedtuple(val)
    assert all(isinstance(item, namedtuple) for item in val)
    assert all(item.a == i for i, item in enumerate(val, 1))
    assert all(item.b == 2 for item in val)

# Generated at 2022-06-13 20:35:51.917830
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Setup
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    dic_ordered = OrderedDict({
        'a': 1,
        'b': 2,
        'c': {
            'd': 4,
            'e': 5,
        },
    })
    dic_ordered_flipped = OrderedDict({
        'b': 2,
        'a': 1,
        'c': {
            'd': 4,
            'e': 5,
        },
    })
    dic_with_dupes = {'a': 1, 'a': 2, 'b': 3}
    dic_with_underscore = {'_a': 1, '__b': 2, 'c_': 3}
    d

# Generated at 2022-06-13 20:36:02.658978
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert repr(to_namedtuple({'a': 1, 'b': 2})) == "NamedTuple(a=1, b=2)"
    assert repr(to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))) == \
            "NamedTuple(a=1, b=2)"
    d = {'a': 1, 'b': 2}
    assert repr(to_namedtuple(d)) == "NamedTuple(a=1, b=2)"
    assert d['a'] == 1
    d = {'a': {'b': 1}, 'c': 2}
    assert repr(to_namedtuple(d)) == "NamedTuple(a=NamedTuple(b=1), c=2)"

# Generated at 2022-06-13 20:36:17.457474
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from pprint import pprint

    dic = {'a': 1, 'b': 2}
    assert repr(to_namedtuple(dic)) == "NamedTuple(a=1, b='2')"

    dic = {'a': 1, 'b': 2, 'c': 3, 'd': [{'1': None, '2': None}, 'e']}
    # pprint(dic)
    ans = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': ([{'1': None, '2': None}, 'e'],)
    }
    ans = OrderedDict(sorted(ans.items()))

# Generated at 2022-06-13 20:36:29.372515
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)

# Generated at 2022-06-13 20:36:42.033356
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import defaultdict
    from flutils.funcutils import all_equal

    d1 = dict(a=1, b=2)
    d2 = dict(b=2, a=1)
    assert all_equal(to_namedtuple(d1), to_namedtuple(d2))

    d1 = dict(a=1, b=2, _c=3)
    d2 = dict(b=2, a=1, _c=3)
    assert all_equal(to_namedtuple(d1), to_namedtuple(d2)) is False

    d1 = dict(a=1, b=2, a1=3)
    d2 = dict(b=2, a=1, a1=3)

# Generated at 2022-06-13 20:36:51.575013
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from flutils.testingutils import get_tests_root
    import json
    import os
    import sys

    if sys.version_info[:2] < (3, 7):
        print(
            '\nWARNING: Unit tests require at least Python 3.7+ to run.'
            '  Skipping unit tests.',
            file=sys.stderr,
            flush=True
        )
        return

    root = get_tests_root()
    jsnpath = os.path.join(root, 'namedtupleutils', 'to_namedtuple.json')
    with open(jsnpath, 'r', encoding='utf-8') as f:
        tests = json.load(f)


# Generated at 2022-06-13 20:37:02.867940
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:37:14.820316
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # pylint: disable=too-few-public-methods
    class FakeNamedTuple(NamedTuple):
        pass
    class FakeSimpleNamespace(SimpleNamespace):
        pass


# Generated at 2022-06-13 20:37:22.869211
# Unit test for function to_namedtuple
def test_to_namedtuple():
    d = {'a': 0, 'b': 1}  # type: ignore[assignment]
    nt = to_namedtuple(d)
    assert nt == (0, 1)

    d = {'a': 0, 'b': {'c': 1, 'd': 2}}  # type: ignore[assignment]
    nt = to_namedtuple(d)
    assert nt == (0, (1, 2))
    assert nt.a == 0
    assert nt.b.c == 1
    assert nt.b.d == 2
    assert nt[0] == 0
    assert nt[1].c == 1
    assert nt[1].d == 2

    nt = to_namedtuple(nt)
    assert nt == (0, (1, 2))

   

# Generated at 2022-06-13 20:37:33.810347
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'a': '1', 'b': 2}) == NamedTuple(a='1', b=2)
    assert to_namedtuple({'a': '1', 'b': 2}) != NamedTuple(a=1, b=2)
    assert to_namedtuple(('a', '1', 'b', 2)) == NamedTuple(a='a', b='b', c='1', d=2)
    assert to_namedtuple(OrderedDict((('a', '1'), ('b', 2)))) == NamedTuple(a='1', b=2)

# Generated at 2022-06-13 20:37:47.381755
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for ``flutils.namedtupleutils.to_namedtuple``."""
    from typing import NamedTuple
    from unittest import TestCase

    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import validate_identifier

    class NamedTupleTester(NamedTuple):
        """A simple class for testing namedtuple."""

        b: int = 1
        a: int = 2

    class TestToNamedTuple(TestCase):
        """Unit test for ``flutils.namedtupleutils.to_namedtuple``."""

        def test_to_namedtuple_dict(self):
            """Test ``to_namedtuple`` with ``dict``."""
            dic = {'a': 1, 'b': 2}
            named = to_

# Generated at 2022-06-13 20:37:59.081994
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    aaa = {
        '_a': 1,
        'a': 2,
        'A': 3,
        'b': [{'c': 4}],
        'c': ((5, ), ),
        'd': ((6, ), ),
        'e': 7,
        'f': {'g': 8},
        'h': 'i',
        'j': None,
        'k': {'k': {'k': {'k': {}}}}
    }
    aaa = to_namedtuple(aaa)

# Generated at 2022-06-13 20:38:13.520975
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []
    assert to_namedtuple({}) == ()
    assert to_namedtuple(()) == ()
    #---
    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert to_namedtuple({'a': 1, 'b': 2}) == (1, 2)
    assert to_namedtuple(('a', 'b')) == ('a', 'b')
    #---
    assert to_namedtuple({'a': 1, 2: 3}) == (1, 3)
    assert to_namedtuple({'a': 1, '2': 3}) == (1, 3)
    #---
    assert to_namedtuple({'a': 1, '_b': 2}) == (1,)
    assert to_namedtuple

# Generated at 2022-06-13 20:38:22.556835
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic_a = {
        'a': 1,
        'b': {
            'c': 2,
            'd': 3,
        },
    }
    out_a = to_namedtuple(dic_a)
    assert hasattr(out_a, 'a') is True
    assert hasattr(out_a, 'b') is True
    assert hasattr(out_a.b, 'c') is True
    assert hasattr(out_a.b, 'd') is True
    assert type(out_a) is namedtuple('NamedTuple', 'a b')
    assert hasattr(out_a.b, 'c') is True
    assert hasattr(out_a.b, 'd') is True

# Generated at 2022-06-13 20:38:36.889777
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pprint import pprint

    d = {'a': 1, 'b': 2, 'c': [1, 2, 3]}
    d_ = {'a': 1, 'b': 2, 'c': [1, 2, 3], (1, 2): {3, 4}}
    d__ = {'a': 1, 'b': 2, 'c': [1, 2, 3], (1, 2): {3, 4}, [3, 4]: 'x'}
    od = OrderedDict(a=1, b=2, c=3)
    ns = SimpleNamespace(a=1, b=2, c=3)
    lis = [1, 2, 3]
    lis_ = [1, 2, 3, {'a': 1, 'b': 2}]

# Generated at 2022-06-13 20:38:49.596371
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic2 = {'b': 2, 'a': 1}
    assert to_namedtuple(dic2) == NamedTuple(a=1, b=2)

    dic3 = {'b': 2, '_a': 1}
    assert to_namedtuple(dic3) == NamedTuple(b=2)

    dic4 = {'b': 2, '_a': 1, 'a': 3}
    assert to_namedtuple(dic4) == NamedTuple(a=3, b=2)


# Generated at 2022-06-13 20:39:01.763341
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import collections

    if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
        TestNamedTuple = namedtuple('TestNamedTuple', ['a', 'b'])
        TestListItem = TestNamedTuple(a=1, b=2)
        TestList = [TestListItem, TestListItem]
        TestTuple = TestListItem, TestListItem
    else:
        TestNamedTuple = collections.namedtuple('TestNamedTuple', ['a', 'b'])
        TestListItem = TestNamedTuple(a=1, b=2)
        TestList = [TestListItem, TestListItem]
        TestTuple = TestListItem, TestListItem
    TestDict = {'a': 1, 'b': 2}
    TestOrd

# Generated at 2022-06-13 20:39:12.577770
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyTypeChecker
    out = to_namedtuple({'a': [{'a1': {'a1a': 1, 'a1b': 2}}]})
    assert repr(out) == "NamedTuple(a=[NamedTuple(a1=[NamedTuple(a1a=1, a1b=2)])])"
    assert type(out.a) is list      # noqa: E721
    assert type(out.a[0]) is NamedTuple
    assert type(out.a[0].a1) is list  # noqa: E721
    assert type(out.a[0].a1[0]) is NamedTuple
    assert type(out.a[0].a1[0].a1a) is int

# Generated at 2022-06-13 20:39:25.350661
# Unit test for function to_namedtuple
def test_to_namedtuple():

    import flutils.namedtupleutils as nt
    import pytest


# Generated at 2022-06-13 20:39:39.356910
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    from flutils.objects import DotDict, DotTuple

    dic = OrderedDict([('a', 1), ('b', 2)])
    a = to_namedtuple(dic)
    assert a[0], 1
    assert a[1], 2

    tup = (1, 2)
    atup = to_namedtuple(tup)
    assert atup[0], 1
    assert atup[1], 2

    lst = [1, 2]
    assert type(lst) is list
    alst = to_namedtuple(lst)
    assert type(alst) is list
    assert alst[0], 1
    assert alst[1], 2


# Generated at 2022-06-13 20:39:51.604785
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import json

    dic0 = {}
    dic1 = {1: 2, 3: 4}  # type: ignore[arg-type]
    dic2 = {'a': 1, 'b': 2}
    exp2 = 'NamedTuple(a=1, b=2)'
    dic3 = {'a': 1, 'b': {'A': 'A', 'B': 'B'}}
    exp3 = 'NamedTuple(a=1, b=NamedTuple(A=\'A\', B=\'B\'))'
    dic4 = {'a': {'A': {'X': 'X', 'Y': 'Y'}, 'B': 2}, 'b': 2}

# Generated at 2022-06-13 20:40:05.108607
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import ChainMap
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple({'a': 1, 'b': 2}) == \
        to_namedtuple(ChainMap({'a': 1, 'b': 2})) == \
        to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == \
        to_namedtuple(SimpleNamespace(a=1, b=2)) == \
        namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) != \
        to_namedtuple(OrderedDict([('b', 2), ('a', 1)]))


# Generated at 2022-06-13 20:40:26.013639
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest.mock as mock
    from unittest import TestCase  # type: ignore

    class FixTest(TestCase):

        def setUp(self) -> None:
            self.obj_dict = dict(a=1, b='b')
            self.obj_ns = SimpleNamespace(**self.obj_dict)
            self.obj_list = list(self.obj_dict.values())
            self.obj_list_list = [self.obj_list]
            self.obj_tuple = tuple(self.obj_dict.values())
            self.obj_tuple_tuple = (self.obj_tuple,)

            self.obj_str = 'str'
            self.obj_int = 1
            self.obj_float = 1.1
            self.obj_bool = True


# Generated at 2022-06-13 20:40:29.876310
# Unit test for function to_namedtuple
def test_to_namedtuple():
    try:
        to_namedtuple(1)
        assert False
    except TypeError:
        pass

    # Test dict
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2



# Generated at 2022-06-13 20:40:38.477162
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple([]) == []
    assert to_namedtuple(()) == (NamedTuple(),)
    assert to_namedtuple(dic={}) == NamedTuple()

    new_tuple = to_namedtuple(
        [
            {
                'a': [
                    {
                        'b': 1,
                        'c': 2,
                    },
                    {
                        'b': 3,
                        'c': 4,
                    },
                ],
            },
            {
                'a': [
                    {
                        'b': 5,
                        'c': 6,
                    },
                    {
                        'b': 7,
                        'c': 8,
                    },
                ],
            },
        ]
    )

    assert new_tuple[0].a[0].b == 1

# Generated at 2022-06-13 20:40:46.222037
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """ Test for function to_namedtuple.

    .. code::

        from flutils.namedtupleutils import to_namedtuple

    """
    from pprint import pformat
    d = to_namedtuple({'denominator': 2, 'numerator': 1})
    assert d == namedtuple('NamedTuple', 'denominator numerator')(2, 1), (
        '{}'.format(pformat(d))
    )
    d = to_namedtuple({'a': {'b': 'c', 'd': 'e'}, 'f': 'g'})

# Generated at 2022-06-13 20:40:57.490415
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)])) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple(SimpleNamespace(a=1, b=2)) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple([1, 2, {'a': 1, 'b': 2}]) == [1, 2, namedtuple('NamedTuple', 'a b')(a=1, b=2)]

# Generated at 2022-06-13 20:41:09.352371
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test :func:`to_namedtuple`."""
    from flutils.namedtupleutils import (
        _to_namedtuple,
        to_namedtuple,
    )
    from types import SimpleNamespace
    from .make import make_namedtuple

    obj = {
        'a': 1,
        'b': 2
    }
    out = to_namedtuple(obj)
    ntout = make_namedtuple(obj)
    assert out == ntout

    obj = {
        'a': 1,
        'b': 2
    }
    out = _to_namedtuple(obj, _started=True)
    ntout = make_namedtuple(obj, _started=True)
    assert out == ntout

    obj = (1, 2, 3)


# Generated at 2022-06-13 20:41:15.944986
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    from collections import namedtuple
    from flutils.namedtupleutils import to_namedtuple
    assert 'NamedTuple(a=1, b=2)' == repr(to_namedtuple(dic))


if __name__ == '__main__':
    """
    Used for running doctests.
    
    python -m flutils.namedtupleutils
    
    """
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:41:26.460484
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    #
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    #
    lst = [1, 2]
    tup = to_namedtuple(lst)
    assert len(tup) == 2
    assert tup[0] == 1
    assert tup[1] == 2
    assert isinstance(tup, tuple)
    #
    lst = [1, 2, {'a': 1, 'b': 2}]
    result = to_namedtuple(lst)
    assert len(result) == 3
    assert len(result[2]._fields) == 2

# Generated at 2022-06-13 20:41:37.164982
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    #    Arrange
    obj = [
        {'a': 1, 'b': 2},
        {'c': 3, 'd': 4},
        {'e': 5, 'f': 6},
    ]
    make = namedtuple('NamedTuple', 'a b')
    make1 = namedtuple('NamedTuple', 'c d')
    make2 = namedtuple('NamedTuple', 'e f')
    expect = [
        make(a=1, b=2),
        make1(c=3, d=4),
        make2(e=5, f=6),
    ]
    #    Act
    actual = to_namedtuple(obj)
    #    Assert
    assert actual == expect



# Generated at 2022-06-13 20:41:48.221645
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from datetime import date, datetime, time
    from decimal import Decimal
    from uuid import UUID

    obj = {'a': 1, 'b': 2}
    val = to_namedtuple(obj)
    assert val.a == 1
    assert val.b == 2

    obj = {'a': {'b': [1, 2, 3]}}
    val = to_namedtuple(obj)
    assert val.a.b == (1, 2, 3)

    obj = [1, 2, 3, 4]
    val = to_namedtuple(obj)
    assert val == (1, 2, 3, 4)

    obj = [1, [2, 3, 4], 5]
    val = to_namedtuple(obj)

# Generated at 2022-06-13 20:42:25.558084
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = [1, 2, 3]
    expected = [1, 2, 3]
    out = to_namedtuple(obj)
    assert out == expected
    obj = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    expected = namedtuple('NamedTuple', ['a', 'b', 'c'])(1, 2, 3)
    out = to_namedtuple(obj)
    assert out == expected
    obj = {'a': 1, 'b': 2, 'c': 3}
    expected = namedtuple('NamedTuple', ['a', 'b', 'c'])(1, 2, 3)
    out = to_namedtuple(obj)
    assert out == expected

# Generated at 2022-06-13 20:42:32.285155
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple('') == ''
    assert to_namedtuple(1) == 1
    assert to_namedtuple([1]) == [1]
    assert to_namedtuple((1,)) == (1,)

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': {'x': 5}}

# Generated at 2022-06-13 20:42:41.627384
# Unit test for function to_namedtuple
def test_to_namedtuple():

    def assert_namedtuple(
        result: Union[NamedTuple, List, Tuple],
        *args: Any,
        **kwargs: Any
    ):
        assert not args
        for key, value in kwargs.items():
            if hasattr(result, key):
                assert getattr(result, key) == value
            else:
                assert key in result
                assert result[key] == value
        return

    assert_namedtuple(
        to_namedtuple({'a': 1, 'b': 2}),
        a=1,
        b=2
    )