

# Generated at 2022-06-13 20:32:52.787194
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        namedtuple,
        OrderedDict,
    )
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple

    make = namedtuple('NamedTuple', 'a b')
    # noinspection PyTypeChecker
    tup = make(1, 2)
    assert to_namedtuple(tup) == tup
    assert to_namedtuple(tup) is not tup

    tup = (1, 2)
    assert to_namedtuple(tup) is not tup

    lst = [1, 2, 3]
    assert to_namedtuple(lst) is not lst

    lst = [1, 2, 3]
    lst = to_namedtuple(lst)
    assert isinstance

# Generated at 2022-06-13 20:32:57.527178
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    print(out)


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:32:59.892920
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1}
    obj = to_namedtuple(dic)
    assert hasattr(obj, 'a')

# Generated at 2022-06-13 20:33:12.382276
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b == 2
    assert str(out) == 'NamedTuple(a=1, b=2)'
    dic = {'1': 1, '2': 2}
    out = to_namedtuple(dic)
    assert out.field_1 == 1
    assert out.field_2 == 2
    assert str(out) == 'NamedTuple(field_1=1, field_2=2)'
    dic = {'_a': 1, '_b': 2}
    out = to_namedtuple(dic)
    assert out.field__a == 1
    assert out.field__b == 2
    assert str(out)

# Generated at 2022-06-13 20:33:24.096123
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import (
        OrderedDict,
    )
    from collections.abc import (
        Sequence,
    )
    from types import (
        SimpleNamespace,
    )
    from typing import (
        Any,
        Dict,
        List,
        NamedTuple,
        Tuple,
        Union
    )
    from unittest.case import (
        TestCase,
    )

    from flutils.namedtupleutils import to_namedtuple

    class TestObj(NamedTuple):
        a: Any
        b: Any
        c: Any

    class TestDict(Dict[str, Any]):
        pass

    class TestNamedTuple(NamedTuple):
        a: Any
        b: Any

    class TestList(List[Any]):
        pass

   

# Generated at 2022-06-13 20:33:35.687333
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from flutils.tests import get_fixture_path

    ord_dic = OrderedDict({
        'a': 1,
        'c': 2,
        'b': 3,
        'd': 4
    })
    nt1 = to_namedtuple(ord_dic)
    assert nt1 == namedtuple('NamedTuple', 'a c b d')(a=1, c=2, b=3, d=4)

    dic = dict(ord_dic)
    nt2 = to_namedtuple(dic)
    assert nt2 == namedtuple('NamedTuple', 'a b c d')(a=1, b=3, c=2, d=4)

    # Test with a list

# Generated at 2022-06-13 20:33:46.477259
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for to_namedtuple
    """

    from numpy import array

    def test_to_namedtuple_1() -> None:
        """Basic test of to_namedtuple
        """
        # noinspection PyUnusedLocal
        v = to_namedtuple({'a': 1, 'b': 2})

    def test_to_namedtuple_2() -> None:
        """Basic test of to_namedtuple
        """
        # noinspection PyUnusedLocal
        v = to_namedtuple(['a', 1])

    def test_to_namedtuple_3() -> None:
        """Basic test of to_namedtuple
        """
        # noinspection PyUnusedLocal
        v = to_namedtuple(SimpleNamespace(a=1, b=2))

   

# Generated at 2022-06-13 20:33:59.042769
# Unit test for function to_namedtuple
def test_to_namedtuple():
    # type: () -> None
    import pytest

    # Basic dict
    dic = {'a': 1, 'b': 2}  # type: MutableMapping
    obj = to_namedtuple(dic)
    assert isinstance(obj, namedtuple('NamedTuple', 'a b'))  # type: ignore[no-redef]
    assert obj.a == 1
    assert obj.b == 2

    # List with dicts
    lst = [
        {'a': 1, 'b': 2},
        {'c': 3, 'd': 4},
    ]  # type: MutableSequence
    obj = to_namedtuple(lst)
    assert isinstance(obj, list)

# Generated at 2022-06-13 20:34:01.893062
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert repr(to_namedtuple(dic)) == 'NamedTuple(a=1, b=2)'

# Generated at 2022-06-13 20:34:12.829407
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    import collections.abc as abc
    assert isinstance(to_namedtuple(abc.Mapping), abc.Mapping)
    assert isinstance(to_namedtuple(abc.Sequence), abc.Sequence)
    assert isinstance(to_namedtuple(dict()), abc.Mapping)
    assert isinstance(to_namedtuple(list()), abc.Sequence)
    assert isinstance(to_namedtuple(tuple()), abc.Sequence)
    assert isinstance(to_namedtuple(('test', 'tuple', 'for', 'namedtuple')), tuple)
    assert isinstance(to_namedtuple(('test', 'namedtuple', 'for', 'dict')), tuple)

# Generated at 2022-06-13 20:34:18.120632
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert isinstance(nt, namedtuple)
    assert nt.a == dic['a']
    assert nt.b == dic['b']



# Generated at 2022-06-13 20:34:28.166987
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import (
        to_namedtuple,
    )

    assert to_namedtuple({}) == namedtuple('NamedTuple', '')()
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', 'a b')(1, 2)

    assert to_namedtuple('abc') == 'abc'
    assert to_namedtuple([]) == []
    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple(('a', 'b')) == namedtuple('NamedTuple', '0 1')('a', 'b')

# Generated at 2022-06-13 20:34:38.522543
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test for function to_namedtuple."""
    from random import shuffle
    from string import ascii_letters, digits

    from flutils.validators import validate_identifier, validate_list_of_dicts

    from flutils.namedtupleutils import to_namedtuple

    from ..testingutils import get_dunder_names
    from ..testingutils import get_function_names
    from ..testingutils import make_random_strings

    tester = cast(NamedTuple, to_namedtuple({'a': 1, 'b': 2}))
    assert isinstance(tester, namedtuple('Test', 'a b'))
    assert tester.a == 1
    assert tester.b == 2


# Generated at 2022-06-13 20:34:50.435001
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == namedtuple('', '')(a=1, b=2) == \
        namedtuple('', 'b a')(b=2, a=1)
    assert to_namedtuple(1) == 1
    ntup = namedtuple('', '')(a=1, b=2)
    assert to_namedtuple(ntup) == ntup
    namedtuple('', '')(a=1, b=2) == to_namedtuple({'a': 1, 'b': 2})

# Generated at 2022-06-13 20:34:58.736457
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
        'key4': 4,
    }
    nt1 = to_namedtuple(dic)
    assert nt1 == namedtuple('Dummy', ('key1', 'key2', 'key3', 'key4'))(1, 2, 3, 4)
    dic = {1: 2, 3: 4}
    nt1 = to_namedtuple(dic)
    assert nt1 == ()
    lst = [dic, dic]
    nt1 = to_namedtuple(lst)

# Generated at 2022-06-13 20:35:10.915138
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from collections.abc import Mapping
    from types import SimpleNamespace

    dic = dict(a=1, b=2)
    assert isinstance(dic, Mapping)
    assert to_namedtuple(dic) == to_namedtuple(dic)
    assert to_namedtuple(dic) == to_namedtuple(dic) == to_namedtuple(dic)
    assert to_namedtuple(dic) == to_namedtuple(dic) == (dic is not True)
    assert to_namedtuple(dic) == to_namedtuple(dic) == (dic is not False)
    assert to_namedtuple(dic) == to_namedtuple(dic) == (dic is True) is not True


# Generated at 2022-06-13 20:35:19.821146
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from types import SimpleNamespace

    with pytest.raises(TypeError, match="Can convert only 'list'|'tuple'|'dict' to a NamedTuple"):
        to_namedtuple(5)

    assert to_namedtuple([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]) == [NamedTuple(a=1, b=2), NamedTuple(a=3, b=4)]

    class Car(NamedTuple):
        make: str
        model: str
        year: int

    assert to_namedtuple(Car('Ford', 'Mustang', 1967)) == Car(make='Ford', model='Mustang', year=1967)


# Generated at 2022-06-13 20:35:33.868671
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest
    from unittest.mock import patch

    class TestToNamedtuple(unittest.TestCase):
        def test_invalid_obj_type(self):
            with self.assertRaises(TypeError):
                to_namedtuple(15)

        def test_invalid_identifier(self):
            od = OrderedDict()
            od['a'] = 1
            od[' b'] = 2
            nt = to_namedtuple(od)
            self.assertEqual(nt, namedtuple('NamedTuple', ('a',))(a=1))

        def test_ignore_underscore(self):
            od = OrderedDict()
            od['a'] = 1
            od['_b'] = 2
            nt = to_namedtuple(od)

# Generated at 2022-06-13 20:35:44.099787
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(None) == None
    assert to_namedtuple([]) == ()
    assert to_namedtuple({}) == ()
    assert to_namedtuple(()) == ()
    assert to_namedtuple(SimpleNamespace()) == ()
    assert (to_namedtuple({'a': 1, 'b': 2}) ==
            namedtuple('NamedTuple', 'a b')(a=1, b=2))
    assert (to_namedtuple([{'a': 1, 'b': 2}]) ==
            (namedtuple('NamedTuple', 'a b')(a=1, b=2),))

# Generated at 2022-06-13 20:35:53.236100
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    dic = {'a': 1, 'b': 2}
    expect = namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2)
    assert to_namedtuple(dic) == expect
    lst = [dic, dic]
    expect = [
        namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2),
        namedtuple('NamedTuple', ['a', 'b'])(a=1, b=2),
    ]
    assert to_namedtuple(lst) == expect
    lst = [1, 2, 3]
    expect = [1, 2, 3]
    assert to_namedtuple(lst) == expect
    tup = (1, 2, 3)
   

# Generated at 2022-06-13 20:36:05.434750
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from sys import intern

    d = {'a': 1, 'b': 2}
    assert to_namedtuple(d) == to_namedtuple(OrderedDict(a=1, b=2))
    assert to_namedtuple([d]) == [to_namedtuple(d)]
    assert to_namedtuple((d,)) == (to_namedtuple(d),)
    assert to_namedtuple(d) == intern('NamedTuple(a=1, b=2)')
    assert to_namedtuple(d) == intern('NamedTuple(b=2, a=1)')
    assert to_namedtuple(d) != intern('NamedTuple(a=2, b=1)')
    assert to_namedtuple(d)

# Generated at 2022-06-13 20:36:10.365965
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == ('a', 'b')

test_to_namedtuple()


# Generated at 2022-06-13 20:36:14.938456
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unittest


    class TestToNamedTuple(unittest.TestCase):

        def test_to_namedtuple(self):

            data = dict(a=1, b=dict(c=3))
            assert to_namedtuple(data) == NamedTuple(a=1, b=NamedTuple(c=3))

# Generated at 2022-06-13 20:36:25.015061
# Unit test for function to_namedtuple
def test_to_namedtuple():
    print('Start unit test for function to_namedtuple')
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('tmp', 'a b')(a=1, b=2)
    assert to_namedtuple(dict(a=1, b=2)) == namedtuple('tmp', 'a b')(a=1, b=2)
    assert to_namedtuple(OrderedDict((('a', 1), ('b', 2)))) == \
        namedtuple('tmp', 'a b')(a=1, b=2)
    assert to_namedtuple(OrderedDict((('a', 1), ('b', 2)))) == \
        namedtuple('tmp', 'a b')(a=1, b=2)

# Generated at 2022-06-13 20:36:34.457817
# Unit test for function to_namedtuple
def test_to_namedtuple():

    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    assert to_namedtuple({'b': 2, 'a': 1}) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    assert to_namedtuple({'b': 2, 'a': 1}) == namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    assert to_namedtuple({'a': 1, 'b': 2, 'c': 3}) == namedtuple('NamedTuple', ['a', 'b', 'c'])(1, 2, 3)


# Generated at 2022-06-13 20:36:44.881018
# Unit test for function to_namedtuple

# Generated at 2022-06-13 20:36:53.609792
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from unittest import TestCase
    from unittest.mock import MagicMock
    from flutils.namedtupleutils import NamedTuple
    from flutils.namedtupleutils._to_namedtuple import _to_namedtuple

    class Test_(TestCase):

        def test__to_namedtuple(self):
            dic: Mapping = {'a': 1, 'b': 2}
            make_expected = namedtuple('NamedTuple', 'a b')
            expected: NamedTuple = make_expected(1, 2)
            self.assertEqual(_to_namedtuple(dic), expected)

            dic = {'a': 1, 'b': {'x': 1, 'y': [1, 2, 3], 'z': 'abc'}}

# Generated at 2022-06-13 20:36:56.049111
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:37:07.975409
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    nt = to_namedtuple(dic)
    assert hasattr(nt, 'a')
    assert hasattr(nt, 'b')
    assert isinstance(nt, NamedTuple)
    assert isinstance(nt, tuple)
    assert nt.a == 1
    assert nt.b == 2
    assert hasattr(nt, '_replace')
    assert isinstance(nt._replace(b=3), NamedTuple)
    assert nt._replace(b=3) == (1, 3)
    assert list(nt._asdict().keys()) == ['a', 'b']
    assert repr(nt) == "NamedTuple(a=1, b=2)"

# Generated at 2022-06-13 20:37:18.495334
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Unit test for function to_namedtuple."""
    def _validate_type(out, obj):
        assert type(out) is type(obj)

    def _validate_items(out, obj):
        out_items = []
        for item in out:
            if hasattr(item, '_fields'):
                for attr in item._fields:
                    val = getattr(item, attr)
                    out_items.append(val)
            else:
                out_items.append(item)

        obj_items = []
        for item in obj:
            if hasattr(item, '_fields'):
                for attr in item._fields:
                    val = getattr(item, attr)
                    obj_items.append(val)
            else:
                obj_items.append(item)

       

# Generated at 2022-06-13 20:37:47.208744
# Unit test for function to_namedtuple
def test_to_namedtuple():
    cases = [
        ('dic', [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]),
        ('tup', [tuple(dic.items()) for dic in cases[1][1]]),
        ('lis', [list(dic.items()) for dic in cases[1][1]]),
        ('nam', [
            collections.namedtuple('Item', dic.keys())(*dic.values())
            for dic in cases[1][1]
        ]),
        ('ord', [
            OrderedDict(dic.items()) for dic in cases[1][1]
        ]),
        ('sim', [
            SimpleNamespace(**dic) for dic in cases[1][1]
        ]),
    ]

# Generated at 2022-06-13 20:37:58.964359
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from flutils.namedtupleutils import (  # pylint: disable=unused-import
        to_namedtuple,
    )

    with pytest.raises(TypeError, match=(
        r"Can convert only 'list', 'tuple', 'dict' to a NamedTuple; got:"
        r"\('(.*)',\) (.*)" % ('str',))):
        to_namedtuple('my name')

    with pytest.raises(TypeError, match=(
        r"Can convert only 'list', 'tuple', 'dict' to a NamedTuple; got:"
        r"\('(.*)',\) (.*)" % ('int',))):
        to_namedtuple(1)


# Generated at 2022-06-13 20:38:10.872846
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from typing import NamedTuple

    class MyTuple(NamedTuple):
        a: int
        b: str
        c: bool
        __slots__ = ()

    class MyClass:
        a: int
        b: str
        c: bool
        __slots__ = ()

    MyClass.a = 1
    MyClass.b = 'cat'
    MyClass.c = True
    obj0 = MyClass()

    # noinspection PyTypeChecker
    obj0: MyClass = obj0
    assert isinstance(obj0.a, int)
    assert isinstance(obj0.b, str)
    assert isinstance(obj0.c, bool)

    obj1 = {'a': 1, 'b': 'cat', 'c': True}
    assert isinstance

# Generated at 2022-06-13 20:38:21.791481
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict, namedtuple
    from types import SimpleNamespace

    from pytest import raises

    from flutils.namedtupleutils import to_namedtuple


    teststr = 'Test String'
    test_list = [1, 2, 3, 4, 5]
    test_tuple = (1, 2, 3, 4, 5)
    test_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'A': 'vala',
        'B': 'valb',
        'C': 'valc',
        123: 123
    }
    test_odict = OrderedDict(test_dict)
    test_namespace = SimpleNamespace(**test_dict)


# Generated at 2022-06-13 20:38:33.719823
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest
    from types import SimpleNamespace
    from flutils.namedtupleutils import to_namedtuple
    from flutils.namedtupleutils import to_namedtuple_list
    from flutils.namedtupleutils import to_namedtuple_tuple

    dic = {'a': 1, 'b': {'c': 2}, '_d': 3}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b.c == 2
    assert out._d is None
    assert isinstance(out, namedtuple)

    dic = {'a': 1, 'b': {'c': 2}, '_d': 3}
    out = to_namedtuple(dic)
    assert out.a == 1
    assert out.b.c == 2

# Generated at 2022-06-13 20:38:39.725949
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """
    >>> from flutils.namedtupleutils import to_namedtuple
    >>> dic = {'a': 1, 'b': 2}
    >>> to_namedtuple(dic)
    NamedTuple(a=1, b=2)
    >>> dic = {'a': 1, 'b': 2, 'c': [{'d': 4, 'e': 5}, {'f': 6, 'g': 7}]}
    >>> to_namedtuple(dic)
    NamedTuple(a=1, b=2, c=[NamedTuple(d=4, e=5), NamedTuple(f=6, g=7)])
    """
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    import doctest
    doctest.test

# Generated at 2022-06-13 20:38:45.248787
# Unit test for function to_namedtuple
def test_to_namedtuple():
    """Test function :func:`to_namedtuple`
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 20:38:53.707139
# Unit test for function to_namedtuple
def test_to_namedtuple():
    obj = {'a': 1, 'b': 2}
    res = to_namedtuple(obj)
    assert 'a' in res._fields
    assert 'b' in res._fields
    assert res.a == obj['a']
    assert res.b == obj['b']
    obj = {'a_': 1, 'b': 2}
    res = to_namedtuple(obj)
    assert 'a_' not in res._fields
    assert 'b' in res._fields
    assert res.b == obj['b']
    obj = {'a': {'b': 2}, 'c': 3}
    res = to_namedtuple(obj)
    assert res.a.b == obj['a']['b']
    assert res.c == obj['c']
    od = OrderedDict()
   

# Generated at 2022-06-13 20:39:05.273095
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    ntuple = to_namedtuple(dic)
    assert ntuple.a == 1
    assert ntuple.b == 2

    dic2 = to_namedtuple(ntuple)
    assert dic2.a == 1
    assert dic2.b == 2

    ntuple2 = to_namedtuple(ntuple)
    assert ntuple2.a == 1
    assert ntuple2.b == 2

    dic3 = to_namedtuple(dic2)
    assert dic3.a == 1
    assert dic3.b == 2

    ntuple3 = to_namedtuple(ntuple2)
    assert ntuple3.a == 1
    assert ntuple3.b == 2



# Generated at 2022-06-13 20:39:17.266503
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from pytest import raises
    from dataclasses import dataclass


# Generated at 2022-06-13 20:39:39.867159
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    obj = to_namedtuple(dic)
    assert hasattr(obj, 'a')
    assert hasattr(obj, 'b')
    assert obj.a == 1
    assert obj.b == 2
    assert isinstance(obj, NamedTuple)


if __name__ == '__main__':
    test_to_namedtuple()

# Generated at 2022-06-13 20:39:52.293782
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import pytest

    with pytest.raises(TypeError):
        to_namedtuple('str')

    assert to_namedtuple([1, 2]) == [1, 2]
    assert to_namedtuple((1, 2)) == (1, 2)
    assert to_namedtuple({'a': 1, 'b': 2}) == namedtuple('NamedTuple', ('a', 'b'))(a=1, b=2)

# Generated at 2022-06-13 20:39:57.692458
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    from collections import namedtuple
    from typing import NamedTuple

    dic = {'a': 1, 'b': 2}
    nt_dic: NamedTuple = to_namedtuple(dic)
    assert nt_dic.a == 1
    assert nt_dic.b == 2

    src_nt = namedtuple('src_nt', 'a,b')
    nt = src_nt(a=1, b=2)
    nt_nt: NamedTuple = to_namedtuple(nt)
    assert nt_nt.a == 1
    assert nt_nt.b == 2

    odic = OrderedDict([('a', 1), ('b', 2)])
    nt_odic: NamedT

# Generated at 2022-06-13 20:40:05.108602
# Unit test for function to_namedtuple
def test_to_namedtuple():
    '''
    Tests the function to_namedtuple.
    '''
    # arrange
    test_dict = {'a': 1, 'b': 2}
    expected_tuple = namedtuple('NamedTuple', ['a', 'b'])(1, 2)
    # act
    actual_value = to_namedtuple(test_dict)
    # assert
    assert actual_value == expected_tuple, 'Expected value to equal {}'.format(
        actual_value)

if __name__ == "__main__":
    test_to_namedtuple()

# Generated at 2022-06-13 20:40:11.981245
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from typing import List, NamedTuple
    import pytest
    class Namespaced(NamedTuple):
        a: int
        b: str
        c: List[int]
        d: Namespaced

    inset = {
        'a': 1,
        'b': 'Apple',
        'c': [1, 2, 3],
        'd': {'a': 2, 'b': 'Orange', 'c': [2, 3, 4]}
    }
    outset = Namespaced(
        a=1,
        b='Apple',
        c=[1, 2, 3],
        d=Namespaced(
            a=2, b='Orange', c=[2, 3, 4], d=None
        )
    )
    tnt = to_namedtuple(inset)


# Generated at 2022-06-13 20:40:22.360372
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # Lists
    lst = ['a', 1, {'b': 'c'}]
    assert to_namedtuple(lst) == ['a', 1, NamedTuple(b='c')]

    # Tuples
    tpl = ('a', 1, {'b': 'c'})
    assert to_namedtuple(tpl) == ('a', 1, NamedTuple(b='c'))

    # Dictionaries
    dic = {'a': 1, 'b': 2}
    assert to_namedtuple(dic) == NamedTuple(a=1, b=2)

    dic = {'a': 1, 'b': {'c': 'd'}}

# Generated at 2022-06-13 20:40:32.041030
# Unit test for function to_namedtuple
def test_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    tup = ('a', 'b')
    named = namedtuple('NamedTuple', ('a', 'b'))(3, 4)
    nested = {'a': dic, 'b': tup, 'c': named}
    ordered = OrderedDict({'a': dic, 'b': tup, 'c': named, 'd': 'D'})
    ns = SimpleNamespace(a=dic, b=tup, c=named, d='D')
    lst = [dic, tup, named, nested, ordered, ns]

# Generated at 2022-06-13 20:40:39.311251
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import namedtuple
    from collections import OrderedDict as odict
    from types import SimpleNamespace as ns
    NamedTuple = namedtuple('NamedTuple', 'a b c')
    obj = NamedTuple(a=1, b=2, c=3)
    assert to_namedtuple(obj) == obj
    obj = [1, 2, 3]
    assert to_namedtuple(obj) == tuple(obj)
    obj = (1, 2, 3)
    assert to_namedtuple(obj) == obj
    obj = odict([('a', 1), ('b', 2), ('c', 3)])
    ntobj = NamedTuple(a=1, b=2, c=3)
    assert to_namedtuple(obj) == ntobj

# Generated at 2022-06-13 20:40:46.543252
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({}) == to_namedtuple(OrderedDict())
    assert to_namedtuple({'a': 1}) == to_namedtuple({'b': 2, 'a': 1})
    assert to_namedtuple({'a': 1}) == to_namedtuple(OrderedDict([('a', 1)]))
    assert to_namedtuple(OrderedDict([('b', 2), ('a', 1)])) == \
           to_namedtuple(OrderedDict([('a', 1), ('b', 2)]))
    assert to_namedtuple(OrderedDict([('b', 2), ('a', 1)])) == \
           to_namedtuple(NamedTuple(b=2, a=1))

# Generated at 2022-06-13 20:40:54.161601
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import flutils.namedtupleutils as nu
    import json
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    dic = nu.to_namedtuple(test_dict)
    assert dic.a == test_dict['a']
    assert dic.b == test_dict['b']
    assert dic.c == test_dict['c']


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 20:41:37.370788
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({'a': 'a'}) == NamedTuple(a='a'), \
        'Cannot convert {a: a} to namedtuple'
    assert to_namedtuple({'a': 1}) == NamedTuple(a=1), \
        'Cannot convert {a: 1} to namedtuple'
    assert to_namedtuple({'a1': 1}) == NamedTuple(a1=1), \
        'Cannot convert {a1: 1} to namedtuple'
    assert to_namedtuple({'a1_': 1}) == NamedTuple(a1_=1), \
        'Cannot convert {a1_: 1} to namedtuple'

# Generated at 2022-06-13 20:41:39.321617
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import unitTestUtils
    unitTestUtils.testFunction(to_namedtuple)

# Generated at 2022-06-13 20:41:49.327560
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple(['a', 'b']) == ['a', 'b']
    assert to_namedtuple(['a', {'b': {'c': 'd'}}]) == ['a', NamedTuple(b=NamedTuple(c='d'))]
    nt = to_namedtuple(['a', {'b': {'c': 'd'}, 'b2': {'c2': 'd2'}}])
    assert nt == ['a', NamedTuple(b=NamedTuple(c='d'), b2=NamedTuple(c2='d2'))]
    assert to_namedtuple(['a', {'1b': {'c': 'd'}}]) == ['a', NamedTuple(b=NamedTuple(c='d'))]

# Generated at 2022-06-13 20:41:56.574438
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import collections
    import typing
    assert to_namedtuple(dict()) is None
    assert to_namedtuple(str()) is None
    assert isinstance(to_namedtuple(dict(a=1, b=2)), collections.namedtuple)
    assert isinstance(to_namedtuple(typing.List[int]), typing.List)
    assert isinstance(to_namedtuple(typing.Dict[str, int]), collections.namedtuple)

# Generated at 2022-06-13 20:42:04.306568
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from collections import OrderedDict
    from copy import copy

    from pytest import mark, raises

    from flutils.namedtupleutils import to_namedtuple

    def test_tuple(obj: Any) -> List[Any]:
        """Test the given object in a tuple."""
        out: List[Any] = []
        items: List[Any] = (obj,)
        out.append(
            to_namedtuple(items)
        )
        return out


# Generated at 2022-06-13 20:42:05.557719
# Unit test for function to_namedtuple
def test_to_namedtuple():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:42:16.529282
# Unit test for function to_namedtuple
def test_to_namedtuple():

    # Simple namespaces have no order.
    dic = dict(a=1, b=2)
    obj = SimpleNamespace(**dic)
    # noinspection SpellCheckingInspection
    out = to_namedtuple(obj)
    assert out._fields == ('a', 'b')
    assert out.a == 1
    assert out.b == 2

    # The order of the dict keys is preserved in the namedtuple.
    orddic = OrderedDict(a=1, b=2)
    # noinspection SpellCheckingInspection
    out = to_namedtuple(orddic)
    assert out._fields == ('a', 'b')
    assert out.a == 1
    assert out.b == 2


# Generated at 2022-06-13 20:42:27.327840
# Unit test for function to_namedtuple
def test_to_namedtuple():
    assert to_namedtuple({"a": "A", "b": "B"}) == NamedTuple(a="A", b="B")
    assert to_namedtuple({"a": "A", "b": "B", "_": "__"}) == NamedTuple(a="A", b="B", _="__")
    assert to_namedtuple({"_": "__"}) == NamedTuple(_="__")
    assert to_namedtuple({"a": "A", "b": "B", "c": {"c1": "C1"}}) == NamedTuple(a="A", b="B", c=NamedTuple(c1="C1"))
    assert to_namedtuple({"a": "A", "b": "B", "c": {"d": {"e": "E"}}}) == Named

# Generated at 2022-06-13 20:42:39.411488
# Unit test for function to_namedtuple
def test_to_namedtuple():
    from flutils.namedtupleutils import to_namedtuple
    dic = {'a': 1, 'b': 2, 'c': 3}
    output = to_namedtuple(dic)
    assert isinstance(output, namedtuple)
    assert isinstance(output, NamedTuple)
    assert isinstance(output, tuple)
    assert not isinstance(output, dict)
    assert not isinstance(output, list)
    assert hasattr(output, 'a')
    assert hasattr(output, 'b')
    assert hasattr(output, 'c')
    assert output.a == 1
    assert output.b == 2
    assert output.c == 3
    assert hasattr(output, 'replace')
    assert hasattr(output, '_asdict')
    assert hasattr(output, '_fields')
