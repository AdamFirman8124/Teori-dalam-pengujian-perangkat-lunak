

# Generated at 2022-06-13 20:32:53.804445
# Unit test for function to_namedtuple
def test_to_namedtuple():

    class _Recursive:

        def __init__(self):
            self.a = OrderedDict(a=1)

    namedtupleutils = __import__('flutils.namedtupleutils')

    assert hasattr(namedtupleutils, 'to_namedtuple')
    remove = namedtupleutils.to_namedtuple

    # Test: Valid types
    dic = {'a': 1}
    item = remove(dic)
    assert isinstance(item, namedtuple)
    assert item.a == 1
    odic = OrderedDict(a=1)
    item = remove(odic)
    assert isinstance(item, namedtuple)
    assert item.a == 1
    item = remove(['a', 1])
    assert isinstance(item, list)

# Generated at 2022-06-13 20:33:05.062675
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Unit test
    def _assert_expected(in_, exp):
        act = to_namedtuple(in_)
        assert exp == act


    with pytest.raises(TypeError):
        to_namedtuple(1)
        to_namedtuple('')

    _assert_expected(dict(a=1, b=2), NamedTuple(a=1, b=2))
    _assert_expected(dict(b=2, a=1), NamedTuple(a=1, b=2))
    _assert_expected(dict(b=1), NamedTuple(b=1))
    _assert_expected([], [])
    _assert_expected((), ())
    _assert_expected((1, 2), (1, 2))
    _assert_expected([1, 2], [1, 2])

# Generated at 2022-06-13 20:33:14.025746
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import _to_namedtuple

    _dic = dict(
        _a=1,
        b=2,
        C=3,
    )
    assert _dic == _to_namedtuple(_dic)._asdict()

    class _Custom(namedtuple('a', 'b')):
        pass

    assert isinstance(_to_namedtuple(_Custom(1, 2)), _Custom)

    assert _to_namedtuple([1, 2, 3]) == [1, 2, 3]

    assert _to_namedtuple((1, 2, 3)) == (1, 2, 3)

    assert _to_namedtuple(1) is 1

    assert _to_namedtuple(simple=SimpleNamespace()) is None



# Generated at 2022-06-13 20:33:24.849634
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase
    from collections import namedtuple

    # type: ignore[misc]
    class One(NamedTuple):
        a: int
        b: int

    # type: ignore[misc]
    class Two(NamedTuple):
        a: int
        b: int

    dic1 = {'a': 1, 'b': 2}
    dic2 = {'a': 3, 'b': 4}
    nt1 = Five(dic1)
    nt2 = Five(dic2)
    nt3 = One(1, 2)
    nt4 = Two(3, 4)

    # type: ignore[misc]

# Generated at 2022-06-13 20:33:31.302105
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from inspect import signature
    from flutils.loadutils import (
        load_callable,
        load_callable_from_source,
    )
    from flutils.namedtupleutils import to_namedtuple
    import pytest
    sig = signature(to_namedtuple)
    bind = sig.bind
    bind_kwonly = sig.bind_partial(obj=None)

    def test_int():
        assert bind(obj=1).arguments == {'obj': 1}
        assert bind(obj=1).kwargs == {}

    def test_list_int():
        assert bind(obj=[1, 2, 3]).arguments == {'obj': [1, 2, 3]}
        assert bind(obj=[1, 2, 3]).kwargs == {}


# Generated at 2022-06-13 20:33:37.549118
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

# Unit test file

# Generated at 2022-06-13 20:33:47.124141
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Only change the length of dic and dic2.
    dic = {'a': 1, 'b': {'c': 3, 'd': 4}, 'e': [{'f': 5}, {'g': 6}]}
    dic2 = {'a': 1, 'b': 2}

    # Run the function to_namedtuple and store the output in new_dic and new_dic2
    new_dic = to_namedtuple(dic)
    new_dic2 = to_namedtuple(dic2)
    # Assert that new_dic is a namedtuple
    assert isinstance(new_dic, namedtuple) 
    # Assert that new_dic2 is a namedtuple
    assert isinstance(new_dic2, namedtuple) 
   

# Generated at 2022-06-13 20:33:59.500308
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from types import SimpleNamespace
    from types import MappingProxyType
    import unittest

    # Required for Python 3.5.2
    unittest.util._MAX_LENGTH = 2000

    class ToNamedtupleTestCase(unittest.TestCase):
        def test_dict(self):
            dic = {'a': 1, 'b': 2}
            out = to_namedtuple(dic)
            self.assertEqual(
                out.a,
                1
            )
            self.assertEqual(
                out.b,
                2
            )
            self.assertEqual(
                out._fields,
                ('a', 'b')
            )


# Generated at 2022-06-13 20:34:11.189560
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test all functions and corresponding arguments in to_namedtuple."""
    from flutils.namedtupleutils import to_namedtuple
    from flutils.testutils import AssertRaisesContext
    from collections import OrderedDict

    # Test to_namedtuple with list
    list_test = [
        {'a': 1, 'b': 2},
        {'c': 3, 'd': 4},
        {'e': 5, 'f': 6},
    ]
    assert to_namedtuple(list_test) == [
        NamedTuple(a=1, b=2),
        NamedTuple(c=3, d=4),
        NamedTuple(e=5, f=6),
    ]

# Generated at 2022-06-13 20:34:17.999692
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from pytest import approx, raises
    from flutils.namedtupleutils import NamedTuple

    assert to_namedtuple({1: 2}) == NamedTuple(one=2)
    assert to_namedtuple({'one': 2}) == NamedTuple(one=2)
    assert to_namedtuple({'X': 2}) == NamedTuple(X=2)
    assert to_namedtuple({'_x': 2}) == NamedTuple()
    assert to_namedtuple({'one': {'a': 1, 'b': 2}, 'two': 2}) == NamedTuple(
        one=NamedTuple(a=1, b=2), two=2
    )

# Generated at 2022-06-13 20:34:30.733293
# Unit test for function to_namedtuple
def test_to_namedtuple():

    from collections import (
        OrderedDict,
    )
    from collections.abc import (
        Mapping,
        Sequence,
    )
    from types import (
        SimpleNamespace,
    )

    from flutils.namedtupleutils import to_namedtuple

    # noinspection PyUnusedLocal, PyShadowingNames
    class Dummy:
        # noinspection PyShadowingNames,PyMissingConstructor,PyUnusedLocal
        def __init__(self, a: int, b: int):
            self.a = a
            self.b = b

    def check_dummy(obj, val):
        assert obj.a == val
        assert obj.b == val
        assert obj.c == val

    def check_dummy2(obj, val):
        assert obj.c == val

    # test

# Generated at 2022-06-13 20:34:39.931502
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class ToNamedTuple(unittest.TestCase):
        def test_to_namedtuple(self):
            from collections import namedtuple

            dic = {'a': 1, 'b': 2, '_c': 3, 'd_': 4, 's': {'a': 1, 'c': 3, '_d': 4}, 'l': [1, 2, 3, 4]}
            _NamedTuple = namedtuple('_NamedTuple', ['a', 'b', 'd_', 's'])
            _SubNamedTuple = namedtuple('_SubNamedTuple', ['a', 'c', 'd_'])
            _Sub2NamedTuple = namedtuple('_Sub2NamedTuple', ['a', 2])
            nt = to_

# Generated at 2022-06-13 20:34:51.883489
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple

    # noinspection PyDataclass,PyDataclass
    class A(NamedTuple):
        a: int
        b: int
    # noinspection PyDataclass,PyDataclass
    class B(NamedTuple):
        c: int
        d: A
    # noinspection PyDataclass,PyDataclass
    class C(NamedTuple):
        e: int
        f: B

    dic = OrderedDict([('a', 1), ('b', 2)])
    assert to_namedtuple(dic) == A(a=1, b=2)


# Generated at 2022-06-13 20:34:59.369417
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # test an empty dict
    out = to_namedtuple({})
    assert out == ()
    assert isinstance(out, NamedTuple)
    assert out._fields == ()

    # test a dict with values
    out = to_namedtuple({'a': 1, 'b': 2})

    assert out == (1, 2)
    assert isinstance(out, NamedTuple)
    assert out._fields == ('a', 'b')
    assert out[0] == 1
    assert out[1] == 2

    # test an OrderedDict with values
    from collections import OrderedDict
    out = to_namedtuple(OrderedDict({'c': 1, 'd': 2}))
    assert out == (1, 2)
    assert isinstance(out, NamedTuple)

# Generated at 2022-06-13 20:35:11.619638
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection PyUnresolvedReferences
    """
    Test that the to_namedtuple function converts objects as expected.
    """
    import unittest
    from collections import (
        OrderedDict as OD,
    )
    from types import (
        SimpleNamespace as SN,
    )
    from typing import (
        Any,
        List,
        Tuple,
    )
    from functools import singledispatchmethod
    from flutils.namedtuple import (
        NamedTuple,
    )
    from flutils.validators import validate_identifier

    class _Mapping(Mapping):
        def __getitem__(self, item):
            return self.__getattribute__(item)

        def __iter__(self):
            for attr in self.__dict__:
                yield attr

# Generated at 2022-06-13 20:35:20.054571
# Unit test for function to_namedtuple
def test_to_namedtuple():
    ntuple = to_namedtuple({'a': 1, 'b': 2})
    assert ntuple == namedtuple('NamedTuple', ['a', 'b'])(1, 2)

    ntuple = to_namedtuple([{'a': 1, 'b': 2}, {'a': 1, 'b': 2}])
    assert ntuple == [
        namedtuple('NamedTuple', ['a', 'b'])(1, 2),
        namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    ]

    ntuple = to_namedtuple(((1, 2, 3), (1, 2, 3)))

# Generated at 2022-06-13 20:35:34.005089
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from functools import singledispatch

    from collections import (
        OrderedDict,
    )
    from collections.abc import (
        Mapping,
        Sequence,
    )
    from types import SimpleNamespace

    @singledispatch
    def _to_namedtuple(
            obj: Any,
            _started: bool = False
    ) -> Any:
        if _started is False:
            raise TypeError(
                "Can convert only 'list', 'tuple', 'dict' to a NamedTuple; "
                "got: (%r) %s" % (type(obj).__name__, obj)
            )
        return obj

    # noinspection PyUnusedFunction,Mypy

# Generated at 2022-06-13 20:35:44.211170
# Unit test for function to_namedtuple
def test_to_namedtuple():

    from flutils.namedtupleutils import to_namedtuple
    from typing import NamedTuple

    class Sample(NamedTuple):
        a: int = 0
        b: str = ''

    # noinspection PyUnresolvedReferences
    def basic_conversion(given, expected):
        assert given.__class__ is expected.__class__
        assert given == expected
        for attr in expected._fields:
            assert getattr(given, attr) == getattr(expected, attr)

    # basic_conversion(
    #     to_namedtuple(Sample(1, '1')),
    #     Sample(1, '1'),
    # )
    #
    # basic_conversion(
    #     to_namedtuple({'a': 1, 'b': '1'}),
    #    

# Generated at 2022-06-13 20:35:53.315508
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    class MyClass():
        def __init__(self, name, val):
            self.name = name
            self.val = val

        def __repr__(self):
            return "<class {0.__class__.__name__}>.{0.name}:{0.val}".format(self)

    class N(NamedTuple):
        a: str
        b: int

    obj1 = [1, 2, 3]
    obj1_expected = [1, 2, 3]
    obj1_actual = to_namedtuple(obj1)
    assert obj1 == obj1_expected
    assert obj1_actual == obj1_expected

    obj2 = {}
    obj2_expected = namedtuple('NamedTuple', '')


# Generated at 2022-06-13 20:36:03.198000
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    test_list = ['a', 1, 2.5]
    test_tuple = ('a', 1, 2.5)
    test_dict: dict = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}, 'f': 5}
    output_dict = to_namedtuple(test_dict)
    assert isinstance(output_dict, NamedTuple)
    assert output_dict.a == 1
    assert output_dict.b == 2
    assert isinstance(output_dict.c, NamedTuple)
    assert output_dict.c.d == 3
    assert output_dict.c.e == 4
    assert output_dict.f == 5

# Generated at 2022-06-13 20:36:17.055345
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == cast(NamedTuple, namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2))
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == cast(
        NamedTuple, namedtuple('NamedTuple', ['a', 'b', 'c', 'd'])(a=1, b=2, c=3, d=4))

# Generated at 2022-06-13 20:36:29.021003
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import NamedTuple

    # TODO: Make sure all types are tested
    # TODO: Make sure all error conditions are tested
    # TODO: Make sure all non-recursive scenarios are tested
    # TODO: Make sure all recursive scenarios are tested

    # TODO: Change tests to use pytest

    # TODO: Convert tests to use Doctests

    # TODO: Convert tests to use Doctest's PythonDocGen

    # TODO: Convert tests to use Doctest's PythonDocGen and doctest_namespace.

    # TODO: Check program's coverage
    # TODO: Check program's complexity

    MyObj = namedtuple('MyObj', 'a b')
    MyNamedTuple = namedtuple('MyNamedTuple', 'a b')
    Data = namedtuple('Data', 'a b c d')


# Generated at 2022-06-13 20:36:36.081816
# Unit test for function to_namedtuple
def test_to_namedtuple():  # pragma: no cover
    from collections import OrderedDict
    from pprint import pformat

    def print_output(out, obj, i):
        print('\nOutput:\n', pformat(out))
        print('Object:\n', pformat(obj))
        print('Object length (before):  ', len(obj))
        print('Output length (after):   ', len(out))
        print('Object[%s]: %r' % (i, obj[i]))
        print('Output[%s]: %r' % (i, out[i]))
        print('Object[%s] type: %r' % (i, type(obj[i]).__name__))
        print('Output[%s] type: %r' % (i, type(out[i]).__name__))

    # Test Sequence
   

# Generated at 2022-06-13 20:36:47.465662
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        attr: str
        b: int

    def myclass(a: str, b: int) -> MyClass:
        return MyClass(a, b)

    dic: dict = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert isinstance(nt, NamedTuple)  # noqa: C901
    assert len(nt) == 2
    assert nt.a == dic['a']
    assert nt.b == dic['b']
    odic = OrderedDict(a=1, b=2)
    nt = to_namedtuple(odic)
    assert isinstance(nt, NamedTuple)  # noqa: C901

# Generated at 2022-06-13 20:36:54.563086
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict

    from flutils.namedtupleutils import to_namedtuple

    print('Testing namedtupleutils.to_namedtuple')
    print('\tSimple usage.')
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(1, 2)
    print('\tComplex usage.')
    tup = (1, {'a': 1, 'b': 2}, [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}])

# Generated at 2022-06-13 20:37:06.871370
# Unit test for function to_namedtuple
def test_to_namedtuple():

    def _test(
            obj: Any,
            spec: Any
    ):
        out = to_namedtuple(obj)
        assert out == spec

    test_dict = {'a': 1, 'b': 2}
    namedtuple_spec = namedtuple('NamedTuple', 'a b')
    _test(test_dict, namedtuple_spec(1, 2))
    test_dict = OrderedDict([('b', 2), ('a', 1)])
    namedtuple_spec = namedtuple('NamedTuple', 'b a')
    _test(test_dict, namedtuple_spec(2, 1))
    test_dict = OrderedDict([(1, 'a'), (2, 'b')])

# Generated at 2022-06-13 20:37:17.587859
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
        namedtuple,
    )
    from typing import (
        Dict,
        List,
        Union,
    )
    from flutils.namedtupleutils import to_namedtuple

    CustomNamedTuple = namedtuple(
        'CustomNamedTuple',
        'a b c'
    )
    SimpleNamedTuple = namedtuple(
        'SimpleNamedTuple',
        'd e f'
    )

    # Test passing a dictionary
    dic: Dict[str, Union[int, str]] = {'a': 1, 'b': 2}
    out: CustomNamedTuple = to_namedtuple(dic)
    assert hasattr(out, 'a')
    assert hasattr(out, 'b')
   

# Generated at 2022-06-13 20:37:28.129986
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.validators import validate_identifier
    from types import SimpleNamespace
    from collections import (
        OrderedDict,
        namedtuple,
    )
    from collections.abc import (
        Mapping,
        Sequence,
    )

    # Test that the expected exceptions are raised
    with pytest.raises(SyntaxError):
        validate_identifier('4_asdf', allow_underscore=False)
    with pytest.raises(TypeError):
        to_namedtuple({'4_asdf': 1})
    with pytest.raises(SyntaxError):
        validate_identifier('a-b', allow_underscore=False)
    with pytest.raises(TypeError):
        to_namedtuple({'a-b': 1})

# Generated at 2022-06-13 20:37:36.152354
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import Dict

    dic: Dict[str, Any] = {
        'key1': {
            '_key2': 3,
            'key2': 4
        },
        'key2': {
            'key1': {
                'key1': [
                    1,
                    2
                ]
            },
            'key2': [
                1,
                2,
                3
            ]
        }
    }
    make = namedtuple('NamedTuple', 'key1 key2')

    make_empty = namedtuple('NamedTuple', '')


# Generated at 2022-06-13 20:37:48.205467
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    from flutils._namedtupleutils import to_namedtuple
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple((1, 2))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple([1, 2])
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == to_namedtuple(dic)
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple((1, 2))
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple([1, 2])

# Generated at 2022-06-13 20:38:07.336531
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    print(to_namedtuple(dic))


# Generated at 2022-06-13 20:38:14.264981
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2

    dic = {'a': {'b': 2}}
    out = to_namedtuple(dic)
    assert out.a.b == 2

    dic = {'a': (1, 2)}
    out = to_namedtuple(dic)
    assert out.a == (1, 2)

    dic = OrderedDict((('a', 1), ('b', 2)))
    out = to_namedtuple(dic)
    assert out[0] == 1
    assert out[1] == 2
    assert out.a == 1
    assert out.b == 2

    from types import SimpleNamespace as _Simple

# Generated at 2022-06-13 20:38:22.835879
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(dict(a='b')) == namedtuple('NamedTuple', 'a')('b')
    assert to_namedtuple(dict(a=None)) == namedtuple('NamedTuple', 'a')(None)
    assert to_namedtuple(OrderedDict(a='b')) == namedtuple('NamedTuple', 'a')('b')
    assert to_namedtuple(OrderedDict(a=None)) == namedtuple('NamedTuple', 'a')(None)
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple((1, 2)) == (1, 2)
    assert to_namedtuple(('a', 'b')) == ('a', 'b')
    assert to_

# Generated at 2022-06-13 20:38:37.013685
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import Mapping
    from collections.abc import Sequence

    assert isinstance(to_namedtuple(('a', 1)), tuple)
    assert isinstance(to_namedtuple(['a', 1]), list)
    assert isinstance(to_namedtuple({'a': 1}), tuple)
    assert isinstance(to_namedtuple({'a': 'a'}), tuple)
    assert isinstance(to_namedtuple({'a': None}), tuple)
    assert isinstance(to_namedtuple({'a': {'b': 1}}), tuple)
    assert isinstance(to_namedtuple({'a': {'b': 1}, 'c': [1, 2]}), tuple)

# Generated at 2022-06-13 20:38:49.727661
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({"a": 1, "b": 2}) == namedtuple("NamedTuple", ("a", "b"))(a=1, b=2)
    assert to_namedtuple({"a": 1, "b": 2}) == namedtuple("NamedTuple", ("a", "b"))(a=1, b=2)
    assert to_namedtuple({"a": 1, "b": 2, "_c": 3}) == namedtuple("NamedTuple", ("a", "b"))(a=1, b=2)

# Generated at 2022-06-13 20:39:01.929545
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple

    # Check basic conversion to tuple
    nt1 = namedtuple('nt_a', ['a', 'b'])
    nt2 = namedtuple('nt_b', ['c', 'd'])
    mytuple = (
        1,
        [nt1(1, 2), nt2(3, 4)],
        {'d': nt2(5, 6), 'a': nt1(7, 8)},
        nt1(9, 10),
    )
    result = to_namedtuple(mytuple)
    assert isinstance(result, tuple)
    assert result[0] == 1
    assert isinstance(result[1], list)

# Generated at 2022-06-13 20:39:07.642022
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2, '__c': 3}
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)
    assert out.a == 1
    assert out.b == 2
    try:
        out.__c
        assert False, '__c should not be an attribute'
    except AttributeError:
        pass
    assert isinstance(out, NamedTuple)
    assert out.a == 1
    assert out.b == 2
    try:
        out.__c
        assert False, '__c should not be an attribute'
    except AttributeError:
        pass

    li = [dic, {'a': 1}]

# Generated at 2022-06-13 20:39:22.367017
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
        namedtuple,
    )
    from functools import singledispatch
    from io import StringIO
    from types import SimpleNamespace

    from flutils.namedtupleutils import to_namedtuple

    def _test_function_to_namedtuple(obj: Any, want: Any) -> None:

        msg = '\nto_namedtuple(%r)' % obj
        got = to_namedtuple(obj)
        stream = StringIO()
        stream.write(msg)
        stream.write('\n  Want:')
        pprint(want, stream, width=30)
        stream.write('\n  Got: ')
        pprint(got, stream, width=30)
        stream.write('\n')

# Generated at 2022-06-13 20:39:29.149237
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple"""
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'b': 1, 'a': 2}) == NamedTuple(a=2, b=1)
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple((1, 2)) == (1, 2)
    assert to_namedtuple([{'a': 1, 'b': 2}, {'b': 3, 'a': 4}]) == [
        NamedTuple(a=1, b=2),
        NamedTuple(a=4, b=3)
    ]

# Generated at 2022-06-13 20:39:42.047921
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple
    from collections.abc import Mapping, Sequence
    from typing import Union

    class TestToNamedTuple(unittest.TestCase):
        def test_type_error(self):
            with self.assertRaises(TypeError):
                # noinspection PyTypeChecker
                to_namedtuple('a')

        def test_namedtuple(self):
            cls = namedtuple('Test', 'a, b, c')
            obj: cls = cls(a=1, b=2, c=3)
            self.assertIsNone(to_namedtuple(obj))

            cls = namedtuple('Test', 'a, b')

# Generated at 2022-06-13 20:40:16.186943
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:40:25.370795
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase

    from flutils.typesutils import (
        list_or_tuple,
        null,
        str_or_bytes,
    )
    from flutils.namedtupleutils import (
        to_namedtuple,
    )

    class TestCaseEmpty(TestCase):
        def test_default(self):
            obj = to_namedtuple(None)
            self.assertEqual(obj, null)

        def test_list(self):
            obj = to_namedtuple([])
            self.assertEqual(obj, [])

            obj = to_namedtuple((1, 2, 3))
            self.assertEqual(obj, (1, 2, 3))

        def test_dict(self):
            obj = to_namedtuple({})
            self.assertE

# Generated at 2022-06-13 20:40:27.804768
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == (1, 2)


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:40:34.544396
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple
    from types import SimpleNamespace
    from flutils.validators import (
        validate_list_of_dicts,
        validate_namedtuple
    )
    from pytest import approx, raises

    def list_of_dicts():
        return [
            {
                'id': 762
            },
            {
                'id': 432
            }
        ]

    def list_of_dicts_with_a_dict():
        return [
            {
                'id': 762,
                'a': {
                    'b': 756,
                    'c': 446
                }
            },
            {
                'id': 432,
                'd': 9
            }
        ]


# Generated at 2022-06-13 20:40:45.059948
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Testing to_namedtuple():
    # Iterate over the tests and perform them.
    for test in _TESTS:
        # Convert to a NamedTuple.
        val = to_namedtuple(test['start'])
        if not isinstance(test['start'], dict):
            # Can't use dict.items() on non-dicts
            continue
        # The expected_items is an ordered dictionary to preserve the order
        # the items should be in the NamedTuple.
        expected_items = OrderedDict()
        # Get the keys that are allowed to be used as NamedTuple attributes.
        for key in test['start'].keys():
            # Avoid having an underscore as the first character of the
            # attribute name of the NamedTuple.
            if key[0] == '_':
                continue
            # Add

# Generated at 2022-06-13 20:40:56.771362
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    assert to_namedtuple({'foo': 'bar'}) == NamedTuple(foo='bar')
    assert to_namedtuple({'foo': 'bar', 'baz': 'biz'}) == NamedTuple(foo='bar', baz='biz')
    assert to_namedtuple({'foo': 'bar', 'baz': 'biz', 'boom': 'bam'}) == \
           NamedTuple(foo='bar', baz='biz', boom='bam')
    assert to_namedtuple({'foo': 'bar', 'baz': 'biz', 'boom': 'bam', 'commandline': 'test'}) == \
           NamedTuple(foo='bar', baz='biz', boom='bam', commandline='test')
    assert to

# Generated at 2022-06-13 20:41:08.757818
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import (
        OrderedNamedTuple,
        to_namedtuple,
    )
    import pytest
    from typing import Any

    dic = {'a': 1, 'b': 2}
    wanted = OrderedNamedTuple(a=1, b=2)
    t: Any = to_namedtuple(dic)
    assert t == wanted
    t: Any = to_namedtuple(t)
    assert t == wanted

    t = OrderedNamedTuple(a=1, b=2)
    wanted = OrderedNamedTuple(a=1, b=2)
    t: Any = to_namedtuple(t)
    assert t == wanted
    t: Any = to_namedtuple(t)
    assert t == wanted

    d

# Generated at 2022-06-13 20:41:17.994078
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({"a": 2, "b": 1}) == namedtuple("NamedTuple", ("a", "b"))(a=2, b=1)

    assert to_namedtuple([{"a": 2, "b": 1}, {"b": 1, "a": 2}]) == [namedtuple("NamedTuple", ("a", "b"))(a=2, b=1), namedtuple("NamedTuple", ("a", "b"))(a=2, b=1)]


# Generated at 2022-06-13 20:41:27.181355
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import collections
    import types

    dic = {'a': 1, 'b': 2}
    nt_dic = collections.namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple(dic) == nt_dic
    a = [dic, nt_dic]
    nt_a = [nt_dic, nt_dic]
    assert to_namedtuple(a) == nt_a
    a = collections.OrderedDict([('a', 1), ('b', 2)])
    nt_dic = collections.namedtuple('NamedTuple', 'a b')(1, 2)
    assert to_namedtuple(a) == nt_dic

# Generated at 2022-06-13 20:41:38.160570
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert nt == NamedTuple(a=1, b=2)
    assert isinstance(nt, NamedTuple)

    nt2 = to_namedtuple(nt)
    assert nt2 == NamedTuple(a=1, b=2)
    assert isinstance(nt2, NamedTuple)

    dic2 = {'c': [1, 2, 3]}
    nt3 = to_namedtuple(dic2)
    assert nt3 == NamedTuple(c=(1, 2, 3))
    assert isinstance(nt3, NamedTuple)
