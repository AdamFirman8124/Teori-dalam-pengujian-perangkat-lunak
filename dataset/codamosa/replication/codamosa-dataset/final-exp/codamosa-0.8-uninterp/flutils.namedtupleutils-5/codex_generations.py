

# Generated at 2022-06-13 20:32:53.892007
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from doctest import Example
    from inspect import cleandoc
    from sys import version_info
    from textwrap import dedent

    # Skip the doctests if less than Python 3.8.
    if version_info < (3, 8):
        py_version = '.'.join([str(i) for i in version_info[:3]])
        return f'Skipping doctests for Python {py_version}.'

    from doctest import (
        DocFileSuite,
        register_optionflag
    )

    from flutils.configobj import ConfigObj
    from flutils.excepts import (
        PyFilesNotFoundError,
        PyFilesNotFoundWarning,
    )

# Generated at 2022-06-13 20:33:05.125000
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class ToNamedTupleTestCase(unittest.TestCase):
        """Unit test for function ``to_namedtuple``."""

        def test_to_namedtuple(self):
            """Test function to_namedtuple."""
            from collections import OrderedDict

            dic = OrderedDict(first='FIRST', second='SECOND', third='THIRD')
            dic['__dict__'] = OrderedDict(one='ONE', two='TWO')
            dic['__dict__']['__dict__'] = OrderedDict(
                a='A',
                b='B',
                c='C',
            )
            dic['dict'] = OrderedDict(a='A', b='B', c='C')

# Generated at 2022-06-13 20:33:05.953293
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from importlib import reload

    reload(validate_identifier)

# Generated at 2022-06-13 20:33:14.318165
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    def _to_namedtuple_raise_error(
            obj: Any,
            _started: bool = False
    ) -> Any:
        raise TypeError

    # New single dispatch that does not allow function as a parameter
    _to_namedtuple = singledispatch(_to_namedtuple_raise_error)

    # noinspection PyUnusedFunction,Mypy
    @_to_namedtuple.register(Mapping)
    # noinspection PyUnusedFunction,PyProtectedMember,Mypy
    def _(
            obj: Mapping,
            _started: bool = False
    ) -> Union[NamedTuple, Tuple]:
        keys = []
        for key in obj.keys():
            if hasattr(key, 'capitalize'):
                key = cast(str, key)
               

# Generated at 2022-06-13 20:33:28.768654
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from collections import OrderedDict
    from flutils.namedtupleutils import to_namedtuple

    # Test Named Tuples
    with pytest.raises(TypeError):
        to_namedtuple(1)
    with pytest.raises(TypeError):
        to_namedtuple(1.4)

    # Test Dicts
    x = to_namedtuple({})
    assert x == ()
    x = to_namedtuple({'a': 1})
    assert x == (1,)

    # Test OrderedDicts
    x = to_namedtuple(OrderedDict())
    assert x == ()
    x = to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))
    assert x == (1, 2)
    x = to_

# Generated at 2022-06-13 20:33:37.671160
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple(dict(x=1)) == namedtuple('NamedTuple', ('x',))(x=1)

    dic = dict(x=1)
    dic['dic'] = dict(y=2)
    out = to_namedtuple(dic)
    assert out == namedtuple('NamedTuple', ('dic', 'x'))(
        dic=namedtuple('NamedTuple', ('y',))(y=2),
        x=1
    )
    assert out.dic == namedtuple('NamedTuple', ('y',))(y=2)


# Generated at 2022-06-13 20:33:47.216367
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        namedtuple,
        OrderedDict,
    )
    import random
    import types
    import pytest

    # ==========================
    #  Test: List, Tuple
    # ==========================
    def _test_list_tuple_typeerror(
            obj: Tuple[Tuple[str, str], ...],
            exp_type: type,
            exp_obj: Any
    ) -> None:
        with pytest.raises(TypeError) as err:
            to_namedtuple(obj)
        err_msg = str(err.value)
        assert err_msg.startswith("Can convert only 'list', "
                                  "'tuple', 'dict' to a NamedTuple; "
                                  "got: (%r) " % exp_type.__name__)


# Generated at 2022-06-13 20:33:59.573090
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import string
    import random
    import types
    import attr

    def make_random(
            min_length: int = 10,
            max_length: int = 50
    ) -> str:
        alphabets = string.ascii_lowercase
        return ''.join(
            random.sample(alphabets, random.randint(min_length, max_length))
        )

    def make_random_dict(
            min_length: int = 2,
            max_length: int = 10,
            min_string_length: int = 10,
            max_string_length: int = 50
    ) -> dict:
        keys = range(random.randint(min_length, max_length))
        data = []
        for key in keys:
            key = str(key)

# Generated at 2022-06-13 20:34:11.236675
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # pylint: disable=redefined-outer-name,unused-variable
    def verify_namedtuple(
            out: Union[str, List[Any], Tuple[Any, ...], NamedTuple],
            obj: Union[str, List[Any], Tuple[Any, ...], Mapping]
    ) -> None:
        if isinstance(obj, Mapping):
            assert len(out) == len(obj)
            for i, key in enumerate(obj.keys()):
                if hasattr(key, 'capitalize'):
                    key = cast(str, key)
                    assert key in out._fields
                    # noinspection PyUnresolvedReferences
                    assert getattr(out, key) == obj[key]
            assert obj == out._asdict()

# Generated at 2022-06-13 20:34:18.024356
# Unit test for function to_namedtuple
def test_to_namedtuple():

    class TestClass:

        def __init__(self, a: Any, b: Any) -> None:
            self.a = a
            self.b = b

    # :obj:`Mapping <collections.abc.Mapping>` tests
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple({'b': 2, 'a': 1}) == namedtuple('NamedTuple', 'a b')(a=1, b=2)
    assert to_namedtuple(OrderedDict([('b', 2), ('a', 1)])) == namedtuple('NamedTuple', 'b a')(b=2, a=1)
    assert to_namedtuple

# Generated at 2022-06-13 20:34:29.128788
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # type annotation
    import typing as tp

    # NamedTuple
    from collections import namedtuple

    # json
    import json

    # yaml
    import yaml

    # tempfile
    from tempfile import NamedTemporaryFile

    # flutils testing
    from flutils.testing import (
        temp_file_name,
        make_temp_file,
        make_temp_dir,
    )

    # Define test data

# Generated at 2022-06-13 20:34:39.136943
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    dic = {'a': 1, 'b': 2}
    lis = [1, 2, 3]
    tup = (1, 2, 3)
    namedt = namedtuple('namedt', 'a b c')(1, 2, 3)

    obj = namedtuple('namedt', '')(1, 2, 3)
    with pytest.raises(TypeError):
        to_namedtuple(obj)

    obj = to_namedtuple(dic)
    assert obj == namedtuple('namedt', 'a b')(1, 2)

    obj = to_namedtuple(lis)
    assert obj == lis

    obj = to_namedtuple(tup)
    assert obj == tup

    obj = to_namedtuple(namedt)
    assert obj

# Generated at 2022-06-13 20:34:51.545455
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

# Generated at 2022-06-13 20:35:03.690491
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    NamedTuple(a=1, b=2) == to_namedtuple(dic)
    dic = {'a': 1, 'b': 2}
    NamedTuple(a=1, b=2) == to_namedtuple(OrderedDict(dic))
    dic = {'a': 1, 'b': 2}
    NamedTuple(a=1, b=2) == to_namedtuple(SimpleNamespace(**dic))
    dic = [
        {'a': 1, 'b': 2},
        {'b': 3, 'c': 4},
        {'d': 4, 'e': 5},
        'dummy'
    ]

# Generated at 2022-06-13 20:35:14.422094
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # noinspection SpellCheckingInspection
    dic = {'a': 1, 'b': 2}
    nt: NamedTuple = to_namedtuple(dic)  # type: ignore[no-any-return]
    assert nt.a == 1
    assert nt.b == 2

    dic = {'a': 1, 'b': 2, 'c': 3}
    # noinspection SpellCheckingInspection
    od = OrderedDict(dic)
    assert od.keys() == ['a', 'b', 'c']
    nt = to_namedtuple(od)
    assert nt.a == 1
    assert nt.b == 2
    assert nt.c == 3

    sn = SimpleNamespace(dic)
    nt = to_namedtuple(sn)

# Generated at 2022-06-13 20:35:28.435755
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase

    class TestToNamedTuple(TestCase):
        def test_dict(self):
            obj = {'a': 1, 'b': 2}
            expected = (1, 2)
            result = to_namedtuple(obj)
            self.assertTupleEqual(expected, result)
        
        def test_dict_conversion(self):
            obj = {'a': 1, 'b': 2, 'c': [3, 4]}
            expected = (1, 2, (3, 4))
            result = to_namedtuple(obj)
            self.assertTupleEqual(expected, result)

    from flutils.testutils import BasicTestRunner
    BasicTestRunner(TestToNamedTuple).run_tests()

# Generated at 2022-06-13 20:35:37.064021
# Unit test for function to_namedtuple
def test_to_namedtuple():
    print('start')
    dic = {'a': 1, 'b': 2}
    print(to_namedtuple(dic))
    print(hasattr(to_namedtuple(dic), 'a'))
    print(hasattr(to_namedtuple(dic), 'b'))
    print(to_namedtuple(dic).a)
    print(to_namedtuple(dic).b)
    print('------------')
    lis = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    print(to_namedtuple(lis))
    for item in to_namedtuple(lis):
        print(item)
        print(hasattr(item, 'a'))
        print(hasattr(item, 'b'))
        print

# Generated at 2022-06-13 20:35:45.776685
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    ord_dic = OrderedDict((('a', 1), ('b', 2)))
    assert to_namedtuple(ord_dic) == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': 2, 'c': '1'}
    exp = NamedTuple(a=1, b=2, c='1')
    assert to_namedtuple(dic) == exp

    dic['d'] = {'A': 1, 'B': 2}

# Generated at 2022-06-13 20:35:54.004828
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from collections.abc import Mapping
    from flutils.collectionsutils import (
        flatten,
    )
    import pytest
    from types import SimpleNamespace

    simple_dict = {'a': 1, 'b': 2}
    simple_odict = OrderedDict(simple_dict)
    simple_sn = SimpleNamespace(a=1, b=2)
    simple_sn_with_ordered = SimpleNamespace(**simple_odict)
    simple_tuple = 1, 2
    simple_list = [1, 2]
    simple_list_with_itself = ['a', 'b', simple_tuple, simple_list]

# Generated at 2022-06-13 20:36:03.536937
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
    )
    from types import SimpleNamespace
    from typing import (
        List,
        NamedTuple,
        Tuple,
    )
    nt = to_namedtuple({'a': 1, 'b': 2})
    assert nt.a == 1
    assert nt.b == 2
    od = OrderedDict({'a': 1, 'b': 2})
    nt = to_namedtuple(od)
    assert nt.a == 1
    assert nt.b == 2
    test_class = SimpleNamespace(a=1, b=2)
    nt = to_namedtuple(test_class)
    assert nt.a == 1
    assert nt.b == 2
    # noinspection Mypy

# Generated at 2022-06-13 20:36:14.748302
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for the function to_namedtuple."""
    from pytest import raises
    from typing import NamedTuple

    assert to_namedtuple({}) == NamedTuple()
    assert to_namedtuple({'a': 1}) == NamedTuple(a=1)
    assert to_namedtuple({'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'b': 2, 'a': 1}) == NamedTuple(a=1, b=2)
    assert to_namedtuple({'1': 1, 'a': 1, 'b': 2}) == NamedTuple(a=1, b=2)

# Generated at 2022-06-13 20:36:16.025870
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod()



# Generated at 2022-06-13 20:36:26.952693
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import NamedTuple
    from typing import NamedTuple as NT

    nt: NT = NamedTuple(a=1, b=2)
    assert nt == to_namedtuple(nt)

    dic = {1: 'a', 'b': 2}
    assert NamedTuple(b=2) == to_namedtuple(dic)

    dic = {'$a': 1, 'b': 2}
    assert NamedTuple(b=2) == to_namedtuple(dic)

    dic = {'a': 1, 'b': 2, '_c': 3}

# Generated at 2022-06-13 20:36:35.368098
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from dataclasses import dataclass
    # Define some test data
    ntuple = namedtuple('NamedTuple', 'a b')
    ntuple2 = namedtuple('NamedTuple2', 'a b')
    ntuple3 = namedtuple('NamedTuple3', 'c d')
    namedtuple_ = ntuple(a=1, b=2)
    namedtuple2_ = ntuple2(a=1, b=[namedtuple_])
    namedtuple3_ = ntuple3(c=namedtuple2_, d=dict(e=namedtuple_))
    ns = SimpleNamespace(a=1, b=namedtuple_, c=namedtuple3_)
    @dataclass
    class TestDataClass:
        a: int


# Generated at 2022-06-13 20:36:46.939008
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2}
    out = to_namedtuple(obj)
    assert out.a == 1
    assert out.b == 2

    obj = [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]
    out = to_namedtuple(obj)
    assert out[0].a == 1
    assert out[0].b == 2
    assert out[1].a == 1
    assert out[1].b == 2

    obj = OrderedDict([('a', 1), ('b', 2)])
    out = to_namedtuple(obj)
    assert out.a == 1
    assert out.b == 2

    obj = (1, 2, {'a': 1, 'b': 2})
    out = to_namedtuple

# Generated at 2022-06-13 20:36:54.197972
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from types import SimpleNamespace

    def _assert(obj: Any, expected_type: type):
        obj_type = type(obj)
        assert obj_type is expected_type, (
            'Expected %r; got %r' % (expected_type.__name__, obj_type.__name__)
        )

    def _assert_tuple(obj: Any, expected_types: List[type]):
        for idx, val in enumerate(expected_types):
            _assert(obj[idx], val)

    vals_dict = {'a': 1, 'b': 2}
    vals_dict_expected = (1, 2)

    vals_ss = SimpleNamespace(**vals_dict)
    vals_ss_expected = (1, 2)

   

# Generated at 2022-06-13 20:37:06.467520
# Unit test for function to_namedtuple
def test_to_namedtuple():
    lst = [
        {'a': 1, 'b': 2},
        {'a': 3, 'b': 4},
        {'a': 5, 'b': 6},
    ]
    assert to_namedtuple(lst) == [
        NamedTuple(a=1, b=2),
        NamedTuple(a=3, b=4),
        NamedTuple(a=5, b=6),
    ]

    class C(object):
        pass
    c = C()
    c.a = 1
    c.b = 2
    named = to_namedtuple(c)
    assert isinstance(named, NamedTuple)
    assert named.a == 1
    assert named.b == 2


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:37:07.075932
# Unit test for function to_namedtuple
def test_to_namedtuple():
    pass

# Generated at 2022-06-13 20:37:16.105909
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Arrange
    obj = {
        'a': 1,
        'b': {
            'c': 2,
            'd': 3,
        },
    }

    expected = namedtuple(
        'Expected',
        'a b',
    )(
        a=1,
        b=namedtuple(
            'Expected',
            'c d',
        )(
            c=2,
            d=3,
        ),
    )

    # Act
    result = to_namedtuple(obj)

    # Assert
    assert isinstance(result, namedtuple)
    assert result == expected



# Generated at 2022-06-13 20:37:23.581056
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class TestToNamedTuple(unittest.TestCase):
        """Test :obj:`to_namedtuple`."""

        def test_dict(self):
            """Test a :obj:`dict`."""
            dic = {'a': 1, 'b': 2}
            ret = to_namedtuple(dic)
            self.assertIsInstance(ret, tuple)
            self.assertEqual(ret.a, 1)
            self.assertEqual(ret.b, 2)

        def test_dict_with_non_identifier_keys(self):
            """Test a :obj:`dict` with non-identifier keys."""
            dic = {'a': 1, 'b': 2, 'd-3': 3}

# Generated at 2022-06-13 20:37:49.458359
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple

    assert to_namedtuple({}) == to_namedtuple(dict())
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple({'b': 2, 'a': 1})
    assert to_namedtuple({'a': 1, 'b': 2}) != to_namedtuple({'a': 2, 'b': 1})

    assert to_namedtuple([1, 2]) == to_namedtuple([2, 1])
    assert to_namedtuple([1, 2]) != to_namedtuple([1, 2, 3])
    assert to_namedtuple([1, 2]) != to_namedtuple((1, 2))

    assert to_namedtuple((1, 2)) == to_namedtuple

# Generated at 2022-06-13 20:37:59.644603
# Unit test for function to_namedtuple
def test_to_namedtuple():

    assert to_namedtuple({}) == to_namedtuple({})
    assert to_namedtuple({}) == to_namedtuple(namedtuple('NamedTuple', '')())
    assert to_namedtuple(namedtuple('NamedTuple', '')()) == \
           to_namedtuple({})
    assert to_namedtuple(namedtuple('NamedTuple', 'g h i')()) == \
           to_namedtuple({'g': None, 'h': None, 'i': None})
    assert to_namedtuple({'a': 1, 'b': 2}) == \
           to_namedtuple({'b': 2, 'a': 1})

# Generated at 2022-06-13 20:38:11.528968
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = lambda: None
    obj.a = 1
    obj.b = 2
    obj.c = obj()
    obj.c.d = True
    obj.c.e = False
    obj.c.f = 'f'
    obj.c.g = obj()

    out = to_namedtuple(obj.__dict__)
    assert out.a == 1
    assert out.b == 2
    assert type(out.c) == namedtuple('NamedTuple', 'd e f g')
    assert out.c.d is True
    assert out.c.e is False
    assert out.c.f == 'f'
    assert type(out.c.g) == namedtuple('NamedTuple', '')

    obj = lambda: None
    obj.a = 1

# Generated at 2022-06-13 20:38:21.859429
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit tests for function to_namedtuple
    """
    # noinspection PyUnresolvedReferences
    from pytest import raises
    obj = {'a': 1, 'b': 2}
    assert to_namedtuple(obj) == obj
    obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert to_namedtuple(obj) == obj
    obj = {'a': 1, '_b': 2, 'c': 3, 'd': 4}
    # noinspection PyUnresolvedReferences
    assert raises(AttributeError, to_namedtuple, obj)
    obj = {'_3': 1, 'b': 2, 'c': 3, 'd': 4}
    # noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:38:33.984770
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # pylint: disable=W0143
    # pylint: disable=W0105
    assert to_namedtuple([{'a': 1, 'b': 2}, {'a': 100, 'b': 20}]) == [
        NamedTuple(a=1, b=2),
        NamedTuple(a=100, b=20),
    ]
    assert to_namedtuple([{'a': 1, 'b': 2}, {'a': 100, 'b': 20}]) == [
        namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2),
        namedtuple('NamedTuple', ['a', 'b'])(a=100, b=20),
    ]

# Generated at 2022-06-13 20:38:39.908948
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test function to_namedtuple"""
    from collections import OrderedDict
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple

    def _expect_exception(
            excep: Exception,
            exc_type: type,
            msg: str,
            func: callable,
            *args,
            **kwargs
    ) -> None:
        if excep:
            if not isinstance(excep, exc_type):
                raise AssertionError(
                    "Unexpected exception type: %s" % excep
                ) from excep
            if msg not in str(excep):
                raise AssertionError(
                    "Unexpected exception message: %s" % excep
                ) from excep

# Generated at 2022-06-13 20:38:47.171702
# Unit test for function to_namedtuple
def test_to_namedtuple():
  dic = {'a': 1, 'b': 2}
  named_tup = to_namedtuple(dic)
  assert named_tup.a == 1, f"named_tup.a should be 1: {named_tup.a}"
  assert named_tup.b == 2, f"named_tup.b should be 2: {named_tup.b}"

# Generated at 2022-06-13 20:38:54.693064
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import Set
    from flutils.namedtupleutils import to_namedtuple
    from flutils.validators import ValidationTypeError

    def _test_to_namedtuple_func(inval, outval):
        if outval is not None:
            assert to_namedtuple(inval) == outval
        else:
            with pytest.raises(Exception, match='^'+repr(inval)+'$'):
                to_namedtuple(inval)


    _test_to_namedtuple_func(
        inval=1,
        outval=None
    )
    _test_to_namedtuple_func(
        inval='1',
        outval=None
    )

# Generated at 2022-06-13 20:39:06.109327
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:39:18.319507
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test function to_namedtuple"""
    obj = {"a": 1, "b": 2, "c": [3, 4], "d": {"e": 5, "f": 6}}
    expected = namedtuple("NamedTuple", sorted(obj.keys()))(
        *[obj[i] for i in sorted(obj)]
    )
    assert to_namedtuple(obj) == expected
    obj = [{"a": 1}, {"b": 2}, {"c": 3}]
    expected = [
        namedtuple("NamedTuple", sorted(i.keys()))(*[i[j] for j in sorted(i)])
        for i in obj
    ]
    assert to_namedtuple(obj) == expected
    obj = OrderedDict({"a": 1, "b": 2})
    expected

# Generated at 2022-06-13 20:39:44.629614
# Unit test for function to_namedtuple
def test_to_namedtuple():
    print('Testing function to_namedtuple()')
    dic = {'a': 1, 'b': 2, 'c': 3}
    nt1 = to_namedtuple(dic)
    assert nt1.a == 1
    assert nt1.b == 2
    assert nt1.c == 3
    dic = OrderedDict(dic)
    nt2 = to_namedtuple(dic)
    assert nt1[0] == nt2[0]
    assert nt1[1] == nt2[1]
    assert nt1[2] == nt2[2]
    nt3 = to_namedtuple(('a', 'b', 'c'))
    assert nt1.a == nt3[0]
    assert nt1.b

# Generated at 2022-06-13 20:39:54.891433
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    for i in range(1, 10):
        dic = {}
        for j in range(1, i):
            dic[j] = j ** j
        dic['a'] = 10
        dic['b'] = 11
        dic['c'] = 12
        named = to_namedtuple(dic)
        assert ordered(named) == ordered(
            {'a': 10, 'b': 11, 'c': 12, **{str(_): _ ** _ for _ in range(1, i)}}
        )
        assert hasattr(named, 'a')
        assert named.a == 10
        assert hasattr(named, 'b')
        assert named.b == 11
        assert hasattr(named, 'c')

# Generated at 2022-06-13 20:40:05.508532
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test to_namedtuple function
    """
    assert(to_namedtuple(1) == 1)
    dic = {'a': 1, 'b': 2}
    assert(to_namedtuple(dic) == namedtuple('NamedTuple', 'a b')(1, 2))
    assert(to_namedtuple(['a', {'b': 2, 'c': 3}]) == ['a', namedtuple('NamedTuple', 'b c')(2, 3)])
    assert(to_namedtuple({'a': [{'b': 2, 'c': 3}, 'd'], 'e': 5}) == namedtuple('NamedTuple', 'a e')([namedtuple('NamedTuple', 'b c')(2, 3), 'd'], 5))

# Generated at 2022-06-13 20:40:16.265131
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    from collections import OrderedDict

    test_dict = dict(a=1, b=2, c=3)
    test_odict = OrderedDict(d=4, e=5, f=6)
    test_sn = SimpleNamespace(
        g=7,
        h=8,
        i=9,
    )

# Generated at 2022-06-13 20:40:27.651115
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest

    class TestToNamedTuple(unittest.TestCase):

        def test_to_namedtuple(self):

            a = {'a': 1, 'b': 2}
            b = to_namedtuple(a)
            self.assertEqual(b, a)
            self.assertIsInstance(b, namedtuple)

            a = [{'a': 1}, {'b': 2}]
            b = to_namedtuple(a)
            self.assertEqual(b[0], a[0])
            self.assertEqual(b[1], a[1])
            self.assertIsInstance(b, list)
            self.assertIsInstance(b[0], namedtuple)
            self.assertIsInstance(b[1], namedtuple)


# Generated at 2022-06-13 20:40:31.573352
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': [{'b': 1, 'c': 2}, {'d': 3, 'e': 4}], 'f': 5}
    actual = to_namedtuple(dic)
    expected = {'a': [{'b': 1, 'c': 2}, {'d': 3, 'e': 4}], 'f': 5}
    assert actual == expected

# Generated at 2022-06-13 20:40:39.149794
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # Test some bad values
    assert to_namedtuple(None) == None
    assert to_namedtuple(0) == 0
    assert to_namedtuple(0.5) == 0.5

    # Test a dict
    assert to_namedtuple({}) == NamedTuple()
    nd = to_namedtuple({'A': 1, 'B': 2})
    assert nd == NamedTuple(A=1, B=2)
    assert nd.A == 1
    assert nd.B == 2

    # Test a dict with bad identifier
    nd = to_namedtuple({1: 1, 2: 2})
    assert nd == NamedTuple(r1=1, r2=2)
    assert nd.r1 == 1
    assert nd.r2 == 2

    # Test

# Generated at 2022-06-13 20:40:46.484692
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """
    Unit test for function to_namedtuple
    """
    import pytest
    data = {
        'example': {
            'layer': {
                'bind': [1, 2, 3],
                'pool': [4, 5, 6]
            },
            'app': {
                'bind': [7, 8, 9],
                'pool': [10, 11, 12]
            }
        }
    }

# Generated at 2022-06-13 20:40:58.318870
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from datetime import datetime
    from collections import OrderedDict

    from flutils.tests.helpers import (
        assert_equal,
        assert_raises,
        assert_is,
    )

    d2 = {'a': 1, 'b': 2}
    assert_equal(to_namedtuple(d2), NamedTuple(a=1, b=2))

    d = {'a': 1, 'b': d2, '_b': 'c', 'c': d2, 5.0: 3}

# Generated at 2022-06-13 20:41:09.409110
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert nt.a == 1
    assert nt.b == 2

    dic = {'a': 1, 'b': 2, '__d': 3}
    nt = to_namedtuple(dic)
    assert not hasattr(nt, '__d')

    dic = {'a': 1, 'b': 2, '_c': 3}
    nt = to_namedtuple(dic)
    assert not hasattr(nt, '_c')

    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    nt = to_namedtuple(dic)
    assert nt.a == 1
    assert nt

# Generated at 2022-06-13 20:41:57.163048
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert isinstance(out, NamedTuple)
    assert out.a == 1
    assert out.b == 2
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    order = ('d', 'b', 'a', 'c')
    od = OrderedDict(sorted(dic.items()))
    od = OrderedDict(reversed(list(od.items())))
    assert tuple(od.keys()) == order
    out = to_namedtuple(od)
    assert tuple(out._fields) == order
    assert out.a == 1
    assert out.b == 2
    assert out.c == 3

# Generated at 2022-06-13 20:42:10.324225
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from collections.abc import (
        Sequence,
        Mapping,
    )
    from flutils.tests.helpers import get_fixture
    from flutils.namedtupleutils import (
        to_namedtuple,
    )
    from typing import (
        Any,
        List,
        NamedTuple,
        Union,
    )
    from types import SimpleNamespace
    from dataclasses import dataclass
    import pytest

    @dataclass(frozen=True, repr=True)
    class DataClass:
        a: Any = 1
        b: Any = 2

    class CustomNamedTuple(NamedTuple):
        _str: str = 'str'
        _bool: bool = False


# Generated at 2022-06-13 20:42:21.102542
# Unit test for function to_namedtuple
def test_to_namedtuple():

    dic1 = {'a': 1, 'b': 2}
    assert to_namedtuple(dic1) == namedtuple('NamedTuple', 'a b')(a=1, b=2)

    # List of objects that each can be converted
    dic2 = {'a': 1, 'b': 2, 'c': 3}
    dic_list = [{'e': 5}, {'f': 6, 'g': 7}]
    dic_list.insert(1, dic2)
    dic_list.append({'h': 8})
    out = to_namedtuple(dic_list)
    assert isinstance(out, list)
    assert out[0] == namedtuple('NamedTuple', 'e')(e=5)
    assert out[1] == named

# Generated at 2022-06-13 20:42:30.006370
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 1, 'b': 2}) == to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))
    assert to_namedtuple(['a', 1, 'b', 2]) == to_namedtuple(('a', 1, 'b', 2))
    assert to_namedtuple(['a', 1, 'b', 2])['a'] == 1
    assert to_namedtuple(('a', 1, 'b', 2))['a'] == 1
    assert to_namedtuple(('a', 1, 'b', 2))['b'] == 2
    assert to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))['a'] == 1

# Generated at 2022-06-13 20:42:40.692131
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({}) == namedtuple('NamedTuple', '')()

    assert to_namedtuple([1, 2, 3]) == [1, 2, 3]
    assert to_namedtuple((3, 2, 1)) == (3, 2, 1)
    assert to_namedtuple((3, [2, (1,)], (4,))) == (3, [2, (1,)], (4,))
    assert to_namedtuple((3, (2, (1,)))) == (3, (2, (1,)))
    assert to_namedtuple((3, (2, (1,), 4))) == (3, (2, (1,), 4))

    nt1 = namedtuple('NamedTuple', 'a')