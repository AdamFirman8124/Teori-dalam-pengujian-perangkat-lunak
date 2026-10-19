

# Generated at 2022-06-12 22:41:17.331113
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define an example class hierarchy
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(B):
        pass

    class F(C):
        pass

    class G(D):
        pass

    # Verify that all the subclasses are found
    assert G in get_all_subclasses(A)
    assert F in get_all_subclasses(A)
    assert E in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert G in get_all_subclasses(B)

# Generated at 2022-06-12 22:41:28.836690
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class FirstClass(object): pass
    class SecondClass(FirstClass): pass
    class ThirdClass(SecondClass): pass
    class NotRelatedClass(object): pass
    # Ensure that the function only returns classes that are
    # subclasses of the provided class
    assert ThirdClass in get_all_subclasses(FirstClass)
    assert ThirdClass not in get_all_subclasses(NotRelatedClass)
    # Ensure that the function returns all subclasses of the
    # provided class
    assert SecondClass in get_all_subclasses(FirstClass)
    assert ThirdClass in get_all_subclasses(SecondClass)
    assert ThirdClass in get_all_subclasses(FirstClass)
    # Ensure that it returns a distinct set of classes
    assert len(get_all_subclasses(FirstClass)) == 2

# Generated at 2022-06-12 22:41:32.951361
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import re

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(D):
        pass

    assert set([B, C, D, E]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:41:40.897944
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types
    from collections import OrderedDict

    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(object): pass

    assert get_all_subclasses(object) == set()
    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert get_all_subclasses(B) == set()
    assert set(get_all_subclasses(C)) == set([D])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()
    assert set(get_all_subclasses(types.BuiltinFunctionType)) == set([OrderedDict])
    assert get_all_subclasses(types.FunctionType) == set()

# Generated at 2022-06-12 22:41:49.095713
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    import sys

    if sys.version_info[0] >= 3:
        class A(object):
            pass

        class B(A):
            pass

        class C(B):
            pass

        class D(C):
            pass


        class E(object):
            pass

        #__str__ is inheritted from object, so we have to have a __str__ to have a different subclass
        class F(A):
            def __str__(self):
                return 'F subclass object'

        class TestSubclasses(unittest.TestCase):
            def test_get_all_subclasses(self):
                self.assertEqual(set(get_all_subclasses(A)), set([B, C, D, F]))

# Generated at 2022-06-12 22:41:51.811020
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert set(get_all_subclasses(A)) == {B, C}

# Generated at 2022-06-12 22:41:55.300163
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Father(object):
        pass
    class Son(Father):
        pass
    class GrandSon(Son):
        pass
    test = get_all_subclasses(Father)
    assert(Son in test and GrandSon in test)
    assert(Father not in test)

# Generated at 2022-06-12 22:41:56.417406
# Unit test for function get_all_subclasses

# Generated at 2022-06-12 22:41:58.673406
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    result_set = set(get_all_subclasses(int))
    assert tuple in result_set
    assert str in result_set

# Generated at 2022-06-12 22:42:03.675599
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([E])

# Generated at 2022-06-12 22:42:13.820135
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(C):
        pass
    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:42:17.409956
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(B):
        pass

    assert frozenset(get_all_subclasses(A)) == frozenset([B, C, D, E])


# Generated at 2022-06-12 22:42:27.830502
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Test 1 : simple example with no circle
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(B, D): pass

    test_subclasses = get_all_subclasses(A)
    assert test_subclasses == set([B, C, D, E])
    # Test 2 : with circle
    class A: pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(D): pass
    class F(C, E): pass

    test_subclasses = get_all_subclasses(A)
    assert test_subclasses == set([B, C, D, E, F])

    # Test 3 : not a class
    class A: pass
    class B(A): pass

# Generated at 2022-06-12 22:42:34.036315
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a tree of classes
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(D): pass
    class F(C): pass
    # Create the expected result
    expected_result = set([B, D, E, C, F])
    # Test get_all_subclasses on root class
    assert(expected_result == get_all_subclasses(A))



# Generated at 2022-06-12 22:42:45.481145
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import os.path
    import sys
    import types

    # We use a list because dicts are not sorted in python < 3.6
    globals_before = list(globals().keys())
    # The code below is mostly inspired from python's Lib/test/test_importlib/resources.py
    # We want to import test_importlib without polluting the context of our test
    # with its objects
    import test.test_importlib
    test_importlib_path = os.path.dirname(test.test_importlib.__file__)
    loader = types.ModuleType('test.test_importlib_loader')
    loader.__file__ = os.path.join(test_importlib_path, 'import_/__init__.py')

# Generated at 2022-06-12 22:42:56.152948
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E(D):
        pass

    class F(object):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E])
    assert set(get_all_subclasses(B)) == set([D, E])
    assert set(get_all_subclasses(C)) == set([D])
    assert set(get_all_subclasses(D)) == set([E])
    assert set(get_all_subclasses(E)) == set([])
    assert set(get_all_subclasses(F)) == set([])

if __name__ == '__main__':
    test_get_

# Generated at 2022-06-12 22:43:03.222342
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(A):
        pass
    # Test default behavior
    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set([C])
    assert set(get_all_subclasses(C)) == set()
    assert set(get_all_subclasses(D)) == set()

    # Test that get_all_subclasses is not affected by subclasses hierarchy
    class E(D):
        pass
    assert set(get_all_subclasses(A)) == set([B, C, D, E])
    assert set(get_all_subclasses(D)) == set([E])

    # Test that get

# Generated at 2022-06-12 22:43:11.696454
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class B1(B): pass
    class B2(B): pass
    class C1(C): pass
    class C2(C): pass

    assert not A.__subclasses__()
    assert len(B.__subclasses__()) == 2
    assert len(C.__subclasses__()) == 2

    assert set(B.__subclasses__()) == set([B1, B2])
    assert set(C.__subclasses__()) == set([C1, C2])

    assert not B1.__subclasses__()
    assert not B2.__subclasses__()
    assert not C1.__subclasses__()
    assert not C2.__subclasses__()


# Generated at 2022-06-12 22:43:20.578916
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import Iterable
    from collections import Mapping
    from collections import Set
    from collections import Sequence
    from collections import Hashable
    from collections import Sized
    from collections import Container
    from collections import Callable
    from collections import MappingView
    from collections import KeysView
    from collections import ItemsView
    from collections import ValuesView

    assert Iterable in get_all_subclasses(Iterable)
    assert Mapping in get_all_subclasses(Mapping)
    assert Set in get_all_subclasses(Set)
    assert Sequence in get_all_subclasses(Sequence)
    assert Hashable in get_all_subclasses(Hashable)
    assert Sized in get_all_subclasses(Sized)
    assert Container in get_all_subclasses(Container)
    assert Callable in get_all_sub

# Generated at 2022-06-12 22:43:25.338695
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B, C):
        pass
    class E(A):
        pass
    assert get_all_subclasses(A) == {B, C, D, E}


# Generated at 2022-06-12 22:43:36.816355
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    class F(object):
        pass
    assert set([B, C, D]) == get_all_subclasses(A)
    assert set([D]) == get_all_subclasses(B)
    assert set([]) == get_all_subclasses(C)
    assert set([]) == get_all_subclasses(D)
    assert set([]) == get_all_subclasses(F)



# Generated at 2022-06-12 22:43:40.998999
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    class E(C):
        pass

    assert set([B, C, D, E]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:43:51.882339
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    try:
        import unittest.mock as mock
    except ImportError:
        import mock
    class A(object): pass
    class B(object): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(C): pass
    class H(E): pass
    class I(F): pass
    all_sub = [C, D, E, F, G, H, I]

# Generated at 2022-06-12 22:43:57.473348
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass
    class E(D):
        pass

    result = get_all_subclasses(A)

    assert B in result
    assert C in result
    assert D in result
    assert E in result

    assert len(result) == 4



# Generated at 2022-06-12 22:44:07.861057
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    class E(object):
        pass

    class F(C, E):
        pass

    class G(F, object):
        pass

    class H(G, object):
        pass

    # G should be the only class to inherit from class F since class F already inherits from class C
    assert(F not in get_all_subclasses(C))
    # B and D should be the only classes to inherit from class A but only D is nested
    assert(len(get_all_subclasses(A)) == 1)
    # F inherits from C and G inherits from F
    assert(C in get_all_subclasses(G))


# Generated at 2022-06-12 22:44:15.372786
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(A):
        pass

    subclasses = get_all_subclasses(A)
    #Returned value should have type 'set'
    assert isinstance(subclasses, set)
    #Following three classes are direct subclasses of class A
    assert B in subclasses
    assert C in subclasses
    assert E in subclasses
    #Following class is not subclass of A
    assert A not in subclasses
    #Following class is subclass of C
    assert D in subclasses

# Generated at 2022-06-12 22:44:22.880877
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a class with no attributes
    class TestClass(object):
        pass

    # Create a class with some attributes
    class TestClassWithAttr(TestClass):
        def __init__(self):
            self.test_attr = 'test attr'

    # Create a subclass of TestClassWithAttr
    class TestSubClass(TestClassWithAttr):
        pass

    assert TestSubClass in get_all_subclasses(TestClass)
    assert TestSubClass in get_all_subclasses(TestClassWithAttr)
    assert TestClassWithAttr in get_all_subclasses(TestClass)

# Generated at 2022-06-12 22:44:33.825839
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils.six import with_metaclass

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(D):
        pass

    class L(with_metaclass(type, object)):
        """For Python 2 and 3 support"""
        pass

    class M(L):
        pass

    class N(L):
        pass

    class O(N):
        pass

    class P(O):
        pass

    assert get_all_subclasses(object) == set()
    assert get_all_subclasses(L) == {M, N, O, P}
    assert get_all_subclasses(A) == {B, C, D, E}

# Generated at 2022-06-12 22:44:37.326904
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(D): pass

    assert get_all_subclasses(A) == set((B,C,D,E))


# Generated at 2022-06-12 22:44:41.620521
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    assert len(get_all_subclasses(A)) == 3
    assert len(get_all_subclasses(B)) == 1
    assert len(get_all_subclasses(C)) == 0
    assert len(get_all_subclasses(D)) == 0

# Generated at 2022-06-12 22:44:53.253838
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Generate a fake class hierarchy and test that get_all_subclasses function appropriate return all subclasses
    '''
    A = type('A', (object,), {})
    B = type('B', (object,), {})
    C = type('C', (object,), {})
    C1 = type('C1', (C,), {})
    C2 = type('C2', (C,), {})
    D1 = type('D1', (C1, A), {})
    D2 = type('D2', (C1, B), {})
    D3 = type('D3', (C2, A), {})
    D4 = type('D4', (C2, B), {})
    D5 = type('D5', (C2, B), {})

# Generated at 2022-06-12 22:45:00.336689
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # class A:
    #    pass
    # class B(A):
    #    pass
    # class C(B):
    #    pass
    # class D:
    #    pass
    # class E(D):
    #    pass
    # class F(D):
    #    pass
    #
    # assert(set([A, B, C]) == set(get_all_subclasses(A))
    # assert(set([D, E, F]) == set(get_all_subclasses(D))
    # assert(set([A, B, C, D, E, F]) == set(get_all_subclasses(object))
    pass

# Generated at 2022-06-12 22:45:08.418783
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a fake class
    class A(object):
        pass
    # Assert that subclasses return an empty list
    assert not A.__subclasses__()
    # Create some fake subclasses
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    # Assert that subclasses return some classes
    assert len(A.__subclasses__()) == 2
    # Get all subclasses
    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 3

# Generated at 2022-06-12 22:45:12.689341
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(object):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(B):
        pass

    assert E in get_all_subclasses(object)
    assert E not in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert len(get_all_subclasses(A)) == 4

# Generated at 2022-06-12 22:45:21.121340
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    class E(D):
        pass

    class F(E):
        pass

    assert get_all_subclasses(B) == {C, D, E, F}
    assert get_all_subclasses(C) == {D, E, F}
    assert get_all_subclasses(D) == {E, F}
    assert get_all_subclasses(E) == {F}
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:45:26.289604
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import Iterable
    class A(object): pass
    class B(object): pass
    class C(A): pass
    class D(C): pass
    class E(C): pass

    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 3
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses

    assert not isinstance(subclasses, Iterable)

# Generated at 2022-06-12 22:45:31.393612
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class M:
        pass

    assert get_all_subclasses(A) == set([A, B, C, D])
    assert get_all_subclasses(B) == set([B, D])
    assert get_all_subclasses(D) == set([D])
    assert get_all_subclasses(M) == set([M])



# Generated at 2022-06-12 22:45:37.150189
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import collections
    import types

    class A(object):
        pass

    class B(A):
        pass

    assert B in get_all_subclasses(A)
    assert collections.UserDict in get_all_subclasses(collections.MutableMapping)
    assert types.ModuleType in get_all_subclasses(object)
    assert str in get_all_subclasses(basestring)

# Generated at 2022-06-12 22:45:41.611074
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(object):
        pass
    class C(A):
        pass
    class D(A):
        pass
    class E(C):
        pass
    class F(E):
        pass
    assert get_all_subclasses(A) == set([C, D, E, F])



# Generated at 2022-06-12 22:45:46.111251
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    class E(B):
        pass
    class F(C):
        pass
    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Testing
if __name__ == '__main__':
    test_get_all_subclasses()

# Generated at 2022-06-12 22:46:02.538801
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(B):
        pass

    class F(C):
        pass

    class G(C):
        pass

    class H(G):
        pass

    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses
    assert G in subclasses
    assert H in subclasses

    for subclass in subclasses:
        assert issubclass(subclass, A)


# Generated at 2022-06-12 22:46:08.812864
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from _utils import get_all_subclasses

    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass

    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([])

# Generated at 2022-06-12 22:46:16.440704
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import UserDict
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_native, to_text
    import unittest

    class Test(UserDict):
        pass

    class Test2(Test):
        pass

    class Test3(Test):
        pass

    class Test4(UserDict):
        pass

    class Test5(dict):
        pass

    class Test6(UserDict):
        pass

    class Test7(Test5):
        pass

    class Test8(Test5):
        pass

    class Test9(MutableMapping):
        pass

    # MutableMapping is available only on Python 3.3.0
    if PY3 and hasattr(collections, 'MutableMapping'):
        subclasses = get

# Generated at 2022-06-12 22:46:22.861802
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class a(object):
        pass
    class b(a):
        pass
    class c(b):
        pass
    class d(c):
        pass
    class e(c):
        pass
    class f(a):
        pass
    class g(f):
        pass
    class h(g):
        pass

    subclasses = get_all_subclasses(a)
    assert len(subclasses) == 8, 'Wrong counting'

    assert b in subclasses, 'Wrong class'
    assert c in subclasses, 'Wrong class'
    assert d in subclasses, 'Wrong class'
    assert e in subclasses, 'Wrong class'
    assert f in subclasses, 'Wrong class'
    assert g in subclasses, 'Wrong class'

# Generated at 2022-06-12 22:46:31.939089
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Unit test for function get_all_subclasses
    """

    # Simple class hierarchy
    class A(object):
        """
        A class
        """
        pass
    class B(A):
        """
        B class
        """
        pass
    class C(A):
        """
        C class
        """
        pass
    class D(C):
        """
        D class
        """
        pass
    class E(A):
        """
        E class
        """
        pass

    # Specific case with loop in class hierarchy
    class F(object):
        """
        F class
        """
        pass
    class G(F):
        """
        G class
        """
        pass
    class H(F):
        """
        H class
        """
        pass
    F.__b

# Generated at 2022-06-12 22:46:36.954410
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(A):
        pass

    class F(E):
        pass

    class G(F):
        pass

    subclasses = get_all_subclasses(A)
    expected = set([B, C, D, E, F, G])
    assert subclasses == expected

# Generated at 2022-06-12 22:46:42.647076
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(C):
        pass
    class E(B):
        pass
    assert get_all_subclasses(A) == {B, C, D, E}
    assert get_all_subclasses(B) == {C, D, E}
    assert get_all_subclasses(C) == {D}
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:46:52.794027
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(D): pass
    class H(F): pass
    class I(C,B): pass
    class J(I): pass
    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H, I, J])
    assert set(get_all_subclasses(B)) == set([D, E, G])
    assert set(get_all_subclasses(I)) == set([J])
    assert set(get_all_subclasses(J)) == set()
    assert set(get_all_subclasses(H)) == set()

# Generated at 2022-06-12 22:46:56.588761
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass

    # Test if we have all the subclasses
    assert set(get_all_subclasses(A)) == set([B,C,D])

# Generated at 2022-06-12 22:47:01.341196
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(E): pass
    a = A()
    b = B()
    assert a is not b
    assert get_all_subclasses(A) == {B, C, D, E, F}

if __name__ == '__main__':
    test_get_all_subclasses()

# Generated at 2022-06-12 22:47:24.730884
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(C):
        pass

    class F(C):
        pass

    class G(E):
        pass

    class H(G):
        pass

    class I(G):
        pass

    class J(F):
        pass

    class K(J):
        pass

    class L(J):
        pass

    class M(K):
        pass

    for descendant_class in get_all_subclasses(A):
        assert descendant_class != A
        assert issubclass(descendant_class, A)

    assert set(get_all_subclasses(F)) == set([G, H, I, J, K, L, M])


# Generated at 2022-06-12 22:47:35.439384
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # First define a simple class hierarchy
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    class E(B):
        pass
    class F(C):
        pass
    # Then perform checks
    assert get_all_subclasses(A) == set([B, C, D, E, F])
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set([F])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])
    assert get_all_subclasses(F) == set([])
    assert get_all_subclasses(str) == set([])

# Generated at 2022-06-12 22:47:43.555267
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class C1(object):
        pass

    class C2(C1):
        pass

    class C3(object):
        pass

    class C4(C2):
        pass

    class C5(C3):
        pass

    class C6(C3):
        pass

    assert set([C1, C2, C4]) == set(get_all_subclasses(C1))
    assert set([C2, C4]) == set(get_all_subclasses(C2))
    assert set([C3, C5, C6]) == set(get_all_subclasses(C3))
    assert set([C4]) == set(get_all_subclasses(C4))
    assert set([C5]) == set(get_all_subclasses(C5))
    assert set([C6]) == set

# Generated at 2022-06-12 22:47:50.374486
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test for the function get_all_subclasses
    '''
    from collections import Iterable

    class A(object):
        '''
        A class A
        '''
        def __init__(self, x):
            self.x = x

    class B(A):
        '''
        A class B
        '''
        def __init__(self, x):
            super(B, self).__init__(x)
            self.x = x

    class C(B):
        '''
        A class C
        '''
        def __init__(self, x):
            super(C, self).__init__(x)
            self.x = x

    class D(A):
        '''
        A class D
        '''

# Generated at 2022-06-12 22:47:58.950202
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):        pass
    class B(A):             pass
    class C(A):             pass
    class D(A):             pass
    class E(B):             pass
    class F(B):             pass
    class G(C):             pass
    class H(C):             pass
    class I(D):             pass
    class J(D):             pass
    class K(E):             pass
    class L(E):             pass
    class M(E):             pass
    class N(G):             pass
    class O(G):             pass
    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I, J, K, L, M, N, O])

# Generated at 2022-06-12 22:48:01.692122
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(C):
        pass
    assert set(get_all_subclasses(A)) == set([C, B, D])



# Generated at 2022-06-12 22:48:07.729775
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Testing functionality of get_all_subclasses and test if it returns the expected subclasses.
    """
    import ansible.module_utils.basic
    import ansible.module_utils.urls
    import ansible.module_utils.six.moves.urllib.request

    # Create a class and a subclass hierarchy of MultiJson
    class MultiJson:
        pass

    class MultiJson1(MultiJson):
        pass

    class MultiJson2(MultiJson):
        pass

    class MultiJson2_1(MultiJson2):
        pass

    class MultiJson3(MultiJson):
        pass

    subclasses = get_all_subclasses(MultiJson)
    assert MultiJson1 in subclasses
    assert MultiJson2 in subclasses
    assert MultiJson2

# Generated at 2022-06-12 22:48:11.659719
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test for function get_all_subclasses
    '''
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    # Check all subclasses from PlayContext
    assert PlayContext in get_all_subclasses(object)
    assert PlayContext in get_all_subclasses(PlayContext)
    assert PlayContext in get_all_subclasses(Play)

# Generated at 2022-06-12 22:48:19.766581
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(B):
        pass

    class F(C):
        pass

    class G(C):
        pass

    class H(F):
        pass

    class I(G):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F, G, H, I}

# Generated at 2022-06-12 22:48:24.457381
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TestChild1(object):
        pass

    class TestChild2(object):
        pass

    class TestChild11(TestChild1):
        pass

    class TestChild12(TestChild1):
        pass

    class TestChild111(TestChild11):
        pass

    # All child classes
    assert TestChild1 in get_all_subclasses(object)
    assert TestChild2 in get_all_subclasses(object)
    assert TestChild11 in get_all_subclasses(object)
    assert TestChild12 in get_all_subclasses(object)
    assert TestChild111 in get_all_subclasses(object)

    # TestChild1 is the only subclass of TestChild2
    assert len(get_all_subclasses(TestChild2)) == 1

# Generated at 2022-06-12 22:49:06.223970
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(D): pass
    class G(B): pass
    class H(G): pass

    seq = get_all_subclasses(A)
    assert sorted(seq, key=lambda x: x.__name__) == [B, C, D, E, F, G, H]

# Generated at 2022-06-12 22:49:07.960629
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Parent(object): pass
    class Child(Parent): pass
    class GrandChild(Child): pass
    assert get_all_subclasses(Parent) == {Child, GrandChild}

# Generated at 2022-06-12 22:49:13.328340
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a class hierarchy
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(E): pass
    class G(A): pass
    class H(A): pass
    class I(H): pass
    class J(I): pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I, J])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(F) == set([])


# this is necessary to avoid a circular import issue in Python 3
# https://github.com/ansible/ansible/issues/5342
import ansible.errors

# Generated at 2022-06-12 22:49:16.376447
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(D, E): pass
    assert set(get_all_subclasses(A)) == set((B, D, C, F, E))



# Generated at 2022-06-12 22:49:23.296891
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test for get_all_subclasses function
    '''

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(object):
        pass

    assert get_all_subclasses(A) == set((B, C, D))
    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(C) == set((D,))
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:49:31.169198
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    class E(E):
        pass
    class F(B):
        pass
    class G(F):
        pass
    class H(G):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H])
    assert get_all_subclasses(B) == set([D, F, G, H])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])
    assert get_all_subclasses(F) == set([G, H])

# Generated at 2022-06-12 22:49:36.170552
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Python 2.6 does not have abc.ABCMeta, so we use object as a base class.
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    class E(D):
        pass

    class F(D):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F}

# Generated at 2022-06-12 22:49:44.577588
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Compares the result of function get_all_subclasses to the output
    the one of the backend
    """
    import ansible.plugins.action
    import ansible.plugins.cache
    import ansible.plugins.callback

    plugins_action_modules = get_all_subclasses(ansible.plugins.action.ActionBase)
    plugins_cache_modules = get_all_subclasses(ansible.plugins.cache.CacheModule)
    plugins_callback_modules = get_all_subclasses(ansible.plugins.callback.CallbackModule)

    plugin_loaders_action = ansible.plugins.loader.action_loader._modules
    plugin_loaders_cache = ansible.plugins.loader.cache_loader._modules
    plugin_loaders_callback = ansible.plugins.loader.callback_loader._modules

    assert plugins_

# Generated at 2022-06-12 22:49:48.516494
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
        Testing that it finds all subclasses of a class
    '''
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    class E(D):
        pass

    class F(E):
        pass

    classes = get_all_subclasses(A)
    assert classes == set([B, C, D, E, F])

# Generated at 2022-06-12 22:49:52.077882
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class F(object):
        pass

    class E(F):
        pass

    class D(F):
        pass

    class C(D):
        pass

    class B(D):
        pass

    class A(B, C):
        pass

    classes = set([A, B, C, D, E, F])
    assert classes == get_all_subclasses(F)