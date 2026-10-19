

# Generated at 2022-06-12 22:41:12.205932
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create dummy base class
    class base(object):
        pass

    # Create dummy child of base
    class child(base):
        pass

    # Create dummy grand-child of base
    class grand_child(child):
        pass

    # Create dummy child of child
    class child_of_child(child):
        pass

    assert get_all_subclasses(base) == set([child, grand_child, child_of_child])
    assert get_all_subclasses(child) == set([grand_child, child_of_child])

# Generated at 2022-06-12 22:41:20.274192
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    # B is a direct subclass of A
    # C is a direct subclass of A
    assert B in A.__subclasses__()
    assert C in A.__subclasses__()
    # B is a subclass of A
    # C is a subclass of A
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)

    class D(B):
        pass
    # D is a subclass of A
    assert D in get_all_subclasses(A)

# Generated at 2022-06-12 22:41:28.164531
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
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set([F])

# Generated at 2022-06-12 22:41:39.232472
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Ensure that get_all_subclasses produces the correct set of returned subclasses
    """
    import random
    from collections import defaultdict

    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    classes = [cls for cls in globals().values() if isinstance(cls, type) and issubclass(cls, A)]

    # Test that get_all_subclasses lists each subclasses
    for cls in classes:
        returned_classes = get_all_subclasses(cls)
        assert returned_classes == set(classes) - set([cls])

    # Test that get_all_subclasses doesn't list superclasses
    for cls in classes:
        returned_classes = get_all_

# Generated at 2022-06-12 22:41:47.809530
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    This function tests the function get_all_subclasses
    """

    class A(object):  # pylint: disable=too-few-public-methods
        pass

    class B(A):  # pylint: disable=too-few-public-methods
        pass

    class C(B):  # pylint: disable=too-few-public-methods
        pass

    class D(A):  # pylint: disable=too-few-public-methods
        pass

    # Expecting to retrieve class C and D
    assert get_all_subclasses(A) == set([C, D])
    # Expecting to retrieve class D
    assert get_all_subclasses(B) == set([D])
    # Expecting to retrieve an empty set

# Generated at 2022-06-12 22:41:56.982929
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses
    '''
    import copy

    class A(object):
        '''
        A class for function get_all_subclasses
        '''

    class B(A):
        '''
        B class for function get_all_subclasses
        '''

    class C(B):
        '''
        C class for function get_all_subclasses
        '''

    class D(B):
        '''
        D class for function get_all_subclasses
        '''

    class E(D):
        '''
        E class for function get_all_subclasses
        '''

    class F(D):
        '''
        F class for function get_all_subclasses
        '''


# Generated at 2022-06-12 22:42:02.964712
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create class hierarchy
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    class F(E):
        pass

    class G(F):
        pass

    class H(F):
        pass

    # Should find all 9 classes
    assert len(get_all_subclasses(A)) == 9

# Generated at 2022-06-12 22:42:14.541594
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses

    Test the function on a collection of classes that form a tree.  This function
    has two purposes, to validate the function and to demonstrate the output.
    '''
    class A(object): pass
    class A1(A): pass
    class A2(A): pass
    class A3(A): pass
    class A11(A1): pass
    class A12(A1): pass
    class A111(A11): pass
    class A112(A11): pass
    class A211(A21): pass

    classes = get_all_subclasses(A)
    assert(A1 in classes)
    assert(A11 in classes)
    assert(A111 in classes)
    assert(A112 in classes)
    assert(A12 in classes)

# Generated at 2022-06-12 22:42:20.296288
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Animal(object):
        def __init__(self):
            pass
    class Mammal(Animal):
        def __init__(self):
            pass
    class Dog(Mammal):
        def __init__(self):
            pass
    class Cat(Mammal):
        def __init__(self):
            pass
    class Fish(Animal):
        def __init__(self):
            pass

    result = get_all_subclasses(Animal)
    assert result == set([Mammal, Fish, Dog, Cat]), 'get_all_subclasses failed'

    result = get_all_subclasses(Mammal)
    assert result == set([Dog, Cat]), 'get_all_subclasses failed'

# Generated at 2022-06-12 22:42:23.908489
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

    assert D in get_all_subclasses(A)



# Generated at 2022-06-12 22:42:33.907218
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E(D): pass
    assert get_all_subclasses(A) == {B, C, D, E}
    assert get_all_subclasses(B) == {D, E}
    assert get_all_subclasses(C) == {D, E}
    assert get_all_subclasses(D) == {E}
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:42:38.791814
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
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:42:41.536348
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    X = set([C])
    Y = get_all_subclasses(A)
    assert X == Y

# Generated at 2022-06-12 22:42:46.407036
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Test this
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    # Set of all classes that are subclasses of A
    all_subclasses = {B, C}

    assert get_all_subclasses(A) == all_subclasses

# Generated at 2022-06-12 22:42:57.160239
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This function is a unit test for function `get_all_subclasses`.

    .. note::
        You can run this function with the command: ``python -m unittest _utils.get_all_subclasses``

    A class named `C` is used to test the function.  `C` is a parent with two child classes
    named `C1` and `C2`.  `C1` is a child with two child classes named `C1_1` and `C1_2`.
    `C2` is a child with one child class named `C2_1`.

    :returns: unit test result
    :rtype: unittest.TestResult
    '''
    class C:
        pass
    class C1(C):
        pass
    class C2(C):
        pass

# Generated at 2022-06-12 22:43:00.650531
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    assert get_all_subclasses(A) == set([B, C])
    class D(C):
        pass
    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:43:10.265212
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import sys
    import collections

    class C(object):
        pass

    class D(C):
        pass

    class E(C):
        pass

    class F(D, E):
        pass

    class G(D, E):
        pass

    class H(D, E):
        pass

    classes = [C, D, E, F, G, H]

    # Adding new classes to module
    for klass in classes:
        setattr(sys.modules[__name__], klass.__name__, klass)

    assert get_all_subclasses(C) == set(classes[1:])
    assert get_all_subclasses(D) == set([F, G, H])
    assert get_all_subclasses(E) == set([F, G, H])
    assert get_all_sub

# Generated at 2022-06-12 22:43:19.311862
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

    class E(object):
        pass

    subclasses = get_all_subclasses(A)
    # Test that the subclasses of A are B, C, and D
    assert(set(subclasses) == set((B, C, D)))
    # Test that the subclasses of B are empty
    assert(get_all_subclasses(B) == set())
    # Test that the subclasses of D are empty
    assert(get_all_subclasses(D) == set())
    # Test that the subclasses of E are empty
    assert(get_all_subclasses(E) == set())

# Generated at 2022-06-12 22:43:30.439391
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from six import class_types
    from ansible.utils.color import ANSIBLE_COLOR, stringc
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

    class F(object):
        pass

    class G(F):
        pass

    class H(G):
        pass

    class I(H):
        pass

    classes = get_all_subclasses(A)
    assert len(classes) == 4
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes

    classes = get_all_subclasses(F)
    assert len(classes) == 3
    assert G in classes
    assert H in classes
    assert I

# Generated at 2022-06-12 22:43:34.189486
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

    class F(C):
        pass


# Generated at 2022-06-12 22:43:48.381968
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Test that this function works as expected
    class ClassA(object): pass
    class ClassB(object): pass
    class ClassB1(ClassB): pass
    class ClassB2(ClassB): pass
    class ClassB3(ClassB): pass
    class ClassB1A(ClassB1): pass
    class ClassB1B(ClassB1): pass
    class ClassB2A(ClassB2): pass
    classes = set([ClassB1, ClassB2, ClassB3, ClassB1A, ClassB1B, ClassB2A])
    assert(classes == get_all_subclasses(ClassB))
    # Test the case where there is no subclass
    classes = set([ClassA])
    assert(classes == get_all_subclasses(ClassA))

if __name__ == "__main__":
    test

# Generated at 2022-06-12 22:43:53.780365
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(A):
        pass

    class E(B):
        pass

    class F(C):
        pass

    class G(F):
        pass

    class H(G):
        pass

    class I(G):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I])

# Generated at 2022-06-12 22:44:05.521615
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    The purpose of this unit test is to verify the method get_all_subclasses is working.

    Method get_all_subclasses requires a class to work with, it doesn't matter if it's an empty class
    or if it has other classes. The test will use this mockup class.

    The goal of this unit test is to verify that :

    * get_all_subclasses will return all the subclasses of a given class;
    * get_all_subclasses won't return the class used for the request.

    .. note::

        The mockup class used here is only used for the tests and doesn't have any other purpose. It has
        been created to be as simple as possible in order to have a more clear test.
    '''

    # Creating mockup classes
    class MockupClass(object):
        pass


# Generated at 2022-06-12 22:44:09.950367
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(object): pass
    class C(A): pass
    class D(A): pass
    class E(C): pass
    class F(C): pass
    assert get_all_subclasses(A) == set([C, D, E, F])
    assert get_all_subclasses(object) == set([A, B, C, D, E, F])

# Generated at 2022-06-12 22:44:14.682645
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

    class E(D):
        pass

    subclasses = get_all_subclasses(A)
    # Test the output
    assert subclasses == set([B, C, D, E])

# Generated at 2022-06-12 22:44:19.373016
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class X(object):
        pass

    class Y(X):
        pass

    class Z(X):
        pass

    class A(Z):
        pass

    class B(Z):
        pass

    assert set(get_all_subclasses(X)) == set([Y, Z, A, B])

# Generated at 2022-06-12 22:44:27.601636
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import abc # for abstract base class

    class A(object):
        pass
    class B(A):
        pass
    class C(object):
        pass
    class D(A, C):
        pass
    class E(C):
        pass

    class F(A):
        pass

    class META(object):
        pass
    class G(META, metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def test(self):
            pass
    class H(G):
        pass
    class I(G):
        pass
    class J(G):
        pass

    class K(I, J):
        pass

    class L(H, K):
        pass

    class N(L):
        pass

    assert A in get_all_subclasses(A)
    assert B

# Generated at 2022-06-12 22:44:37.987299
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(D): pass
    class F(E): pass
    class G(F): pass
    class Z(object): pass

    assert get_all_subclasses(A) == set([C, B, D, E, F, G])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set([E, F, G])
    assert get_all_subclasses(E) == set([F, G])
    assert get_all_subclasses(F) == set([G])
    assert get_all_subclasses(G) == set()
    assert get_

# Generated at 2022-06-12 22:44:40.626589
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    assert get_all_subclasses(A) == set([B, D, C, E])

# Generated at 2022-06-12 22:44:49.680980
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''Test function get_all_subclasses'''
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

    class F(D):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])
    assert set(get_all_subclasses(B)) == set()
    assert set(get_all_subclasses(C)) == set([D, E, F])
    assert set(get_all_subclasses(D)) == set([F])

# Generated at 2022-06-12 22:45:02.299594
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

    class G(C):
        pass

    class H(F):
        pass

    class I(G):
        pass

    class J(G):
        pass

    class K(G):
        pass

    class L(object):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H, I, J, K])
    assert set(get_all_subclasses(L)) == set([])

# Generated at 2022-06-12 22:45:09.541299
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses

    :rtype: bool
    :returns: True if the unit test passes.  Otherwise, False.
    '''
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(B): pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E])
    assert set(get_all_subclasses(B)) == set([E])
    assert set(get_all_subclasses(E)) == set([])

    return True

# Generated at 2022-06-12 22:45:14.102902
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
    class E(D):
        pass
    class F(A):
        pass
    assert get_all_subclasses(A) == set([C, D, E, F])
    assert get_all_subclasses(D) == set([E])

# Generated at 2022-06-12 22:45:24.545264
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.plugins.loader import plugin_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    variable_manager.set_inventory(plugin_loader.get('Inventory')(loader=DataLoader()))

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

    assert set(get_all_subclasses(Templar)) == (
        {Templar} | set(get_all_subclasses(Templar)) | set(get_all_subclasses(VariableManager))
    )

   

# Generated at 2022-06-12 22:45:31.863318
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import os
    import tempfile
    import shutil
    from datetime import datetime
    from unittest.case import TestCase

    class Base(object):
        pass

    class A(Base):
        pass

    class B(Base):
        pass

    class C(Base):
        pass

    class D(C):
        pass

    class E(D):
        pass

    class F(E, D):
        pass

    class G(F):
        pass

    class H(D):
        pass

    class I(E, F, H, G, Base):
        pass

    class J(I):
        pass

    assert set(get_all_subclasses(Base)) == set([A, B, C, D, E, F, G, H, I, J])


# Generated at 2022-06-12 22:45:42.281583
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Since python 3.2 __subclasses__() no longer returns a list
    # and we need it, we have to convert it to a list

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

    # Retrieve direct subclasses
    subclass = list(A.__subclasses__())
    assert len(subclass) == 2, "A : direct subclass == 2"
    assert B in subclass, "B is subclass of A"
    assert C in subclass, "C is subclass of A"

    # Get all subclasses
    subclass = list(get_all_subclasses(A))
    assert len(subclass) == 4, "A : subclass == 4"

# Generated at 2022-06-12 22:45:45.988863
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class classA:
        pass

    class classB(classA):
        pass

    class classC(classA):
        pass

    class classD(classB):
        pass

    class classE(classB):
        pass

    class classF(classC):
        pass

    class classG(classC):
        pass

    class classH(classC):
        pass

    assert get_all_subclasses(classA) == set([classB, classC, classD, classE, classF, classG, classH])

# Generated at 2022-06-12 22:45:52.892200
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Use classes from string module
    import string

    # Obtain all classes
    all_classes = get_all_subclasses(string.Formatter)

    # Check that all classes are inherited from string.Formatter
    assert all([issubclass(x, string.Formatter) for x in all_classes])

    # Check that all classes are set to string.Formatter, string.TemplateFormatter or another classes from all_classes
    assert all([issubclass(string.TemplateFormatter, x) or issubclass(string.Formatter, x) or x in all_classes for x in all_classes])

# Generated at 2022-06-12 22:46:02.293253
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(B):
        pass

    class E(C):
        pass

    class F(C):
        pass

    class G(A):
        pass

    class H(G):
        pass

    class I(G):
        pass

    class J(object):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F, G, H, I}
    assert get_all_subclasses(B) == {C, D, E, F}
    assert get_all_subclasses(J) == set()



# Generated at 2022-06-12 22:46:06.687637
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This is a simple unit test for get_all_subclasses()
    '''
    class Super(object):
        pass

    class Inherit(Super):
        pass

    class InheritInherit(Inherit):
        pass

    assert set(get_all_subclasses(Super)) == {Inherit, InheritInherit}

# Generated at 2022-06-12 22:46:27.034320
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

    class E(B):
        pass

    class F(C, D, E):
        pass

    assert F in get_all_subclasses(object)
    assert F in get_all_subclasses(A)
    assert F in get_all_subclasses(B)
    assert F in get_all_subclasses(C)
    assert F in get_all_subclasses(D)
    assert F in get_all_subclasses(E)
    assert F not in get_all_subclasses(F)

    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert E in get_all_

# Generated at 2022-06-12 22:46:35.575428
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """Unit test for the _utils/get_all_subclasses function"""
    # We need a basic class to use in this test
    class A: pass
    # And some classes to subclass it in a tree
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    # Now call the function and assert that it returns the correct set
    result = get_all_subclasses(A)
    expected = frozenset((B, C, D, E, F))
    assert result == expected, \
        "The get_all_subclasses function did not work correctly."
    # Now check that a subclass does not return extra subclasses
    result = get_all_subclasses(B)
    expected = frozenset((D, E))
   

# Generated at 2022-06-12 22:46:43.428038
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test get_all_subclasses by creating an example class hierarchy,
    then checking that all subclasses are returned.
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

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    assert(set(get_all_subclasses(object)) == set([A, B, C, D, E]))
    assert(set(get_all_subclasses(A)) == set([B, C, D]))
    assert(set(get_all_subclasses(B)) == set([]))

# Generated at 2022-06-12 22:46:50.645889
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
    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(object) == set([A, B, C, D])



# Generated at 2022-06-12 22:46:58.373265
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(object): pass
    class E(D): pass

    assert get_all_subclasses(A) == {B, C}
    assert get_all_subclasses(B) == {C}
    assert get_all_subclasses(D) == {E}
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(object) == {A, B, C, D, E, list}
    assert get_all_subclasses(list) == set()

# Generated at 2022-06-12 22:47:02.299459
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(D):
        pass

    assert get_all_subclasses(A) == {B, C, D, E}

# Generated at 2022-06-12 22:47:10.968032
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        pass

    # Create a deep class tree
    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(C):
        pass

    class F(E):
        pass

    class G(F):
        pass

    class H(G):
        pass

    class I(G):
        pass

    class J(C):
        pass

    classes = get_all_subclasses(A)
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F in classes
    assert G in classes
    assert H in classes
    assert I in classes
    assert J in classes


# Generated at 2022-06-12 22:47:15.588731
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class Base(object):
        pass

    class A(Base):
        pass

    class B(Base):
        pass

    class C(Base):
        pass

    class D(C):
        pass

    # Define a set of known classes
    subclasses_set_expected = {A, B, C, D}

    subclasses_set_got = get_all_subclasses(Base)

    assert subclasses_set_expected.difference(subclasses_set_got) == set()



# Generated at 2022-06-12 22:47:24.460648
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A: # This is our grandparent class
        pass

    class B1(A): # This is our parent class
        pass

    class B2(A): # This is our parent class
        pass

    class C1(B1): # This is our child class
        pass

    class C2(C1): # This is our grandchild class
        pass

    class C3(B2): # This is our child class
        pass

    assert get_all_subclasses(A) == {B1, B2, C1, C2, C3}
    assert get_all_subclasses(B1) == {C1, C2}
    assert get_all_subclasses(B2) == {C3}
    assert get_all_subclasses(C1) == {C2}

# Generated at 2022-06-12 22:47:35.303244
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import collections
    import numbers
    import abc
    import six

    # Basic test class
    class TestClass(object):
        pass

    # Basic usage of get_all_subclasses function
    assert TestClass in get_all_subclasses(object)
    assert TestClass in get_all_subclasses(abc.ABC)
    assert TestClass in get_all_subclasses(six.with_metaclass(abc.ABCMeta))

    # Regression test for the use of numeric types in python 2
    if six.PY2:
        assert numbers.Number in get_all_subclasses(object)
        assert collections.Sequence in get_all_subclasses(object)

    # Basic test with abstract class
    @six.add_metaclass(abc.ABCMeta)
    class Abstract(object):
        pass


# Generated at 2022-06-12 22:48:03.824747
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Building test classes
    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(C):
        pass
    class E(C):
        pass
    class F(D):
        pass
    # Testing function
    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert E in get_all_subclasses(A)
    assert F in get_all_subclasses(A)

# Generated at 2022-06-12 22:48:07.122286
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

    class F(A):
        pass

    assert(set(get_all_subclasses(A)) == set([B, C, D, F]))

# Generated at 2022-06-12 22:48:13.363884
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
    class F(C):
        pass
    class G(E):
        pass
    class H(D):
        pass

    # The classes are arranged in a graph where the edges are subclasses.  The subgraph for `A`
    # looks like:
    #
    # A
    # |\
    # | \
    # |  \
    # C   D
    # |  /|\
    # | / | \
    # |/  |  \
    # E   |   H
    #  \  |   |
    #   \ |   |
    #    \|   |
    #

# Generated at 2022-06-12 22:48:21.596281
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(D): pass
    class F(C,D): pass
    class G(B,E): pass
    # get_all_subclasses is a generator
    assert(set(cls.__name__ for cls in get_all_subclasses(A)) == {'B', 'C', 'D', 'E', 'F', 'G'})

# Generated at 2022-06-12 22:48:28.292384
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This is an extremely simple unit test for the get_all_subclasses function.  It creates the
    following class hierarchy (using python3.4 syntax):

    .. code-block:: python

        class A:
            pass

        class B(A):
            pass

        class C(A):
            pass

        class D(B):
            pass

    Then it tests that the set of subclasses returned is:

    .. code-block:: python

        {B, C, D}

    After all, if the above hierarchy is created, B, C and D are the subclasses.
    '''

    # NOTE: As the syntax is the same, we are using the same code for python2 and 3.  If we start
    # using python2 specific syntax, this must be updated to avoid syntax errors.

    class A:
        pass


# Generated at 2022-06-12 22:48:35.789979
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class A1(A):
        pass
    class A2(A):
        pass
    class B(A):
        pass
    class B1(B):
        pass
    class C(A):
        pass
    class C1(C):
        pass
    class C2(C):
        pass
    assert A2 in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert B1 in get_all_subclasses(A)
    assert C1 in get_all_subclasses(A)
    assert C2 in get_all_subclasses(A)

# Generated at 2022-06-12 22:48:39.795973
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

    classes = {A, B, C, D, E, F}

    assert get_all_subclasses(A) == classes

# Generated at 2022-06-12 22:48:48.161431
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import os
    import json

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
    class F(D):
        pass
    class G(A):
        pass
    class H(G):
        pass

    # Define expected result
    expected = set([B,
                    C,
                    D,
                    E,
                    F,
                    G,
                    H])
    actual = get_all_subclasses(A)

    # Display actual and expected
    print("%s : %s" % (' '.join(map(lambda x: x.__name__, expected)),
                      ' '.join(map(lambda x: x.__name__, actual))))

    # Compare

# Generated at 2022-06-12 22:48:50.940605
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
    class E(C):
        pass

    assert set(get_all_subclasses(A)) == {B, C, D, E}

# Generated at 2022-06-12 22:48:56.466640
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    import itertools

    class BaseClass(object):
        pass

    class ClassA(BaseClass):
        pass

    class ClassB(BaseClass):
        pass

    class ClassC(ClassA):
        pass

    class ClassD(ClassC):
        pass

    class ClassE(ClassC):
        pass

    class TestGetAllSubclasses(unittest.TestCase):
        def setUp(self):
            self.direct_subclasses = {ClassA, ClassB}
            self.all_subclasses = {ClassA, ClassB, ClassC, ClassD, ClassE}

        def test_direct_subclasses(self):
            self.assertEqual(self.direct_subclasses, set(BaseClass.__subclasses__()))


# Generated at 2022-06-12 22:50:00.171878
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

    class E(D):
        pass

    class F(D):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])
    assert set(get_all_subclasses(B)) == set([D, E, F])
    assert set(get_all_subclasses(C)) == set([])
    assert set(get_all_subclasses(D)) == set([E, F])
    assert set(get_all_subclasses(E)) == set([])
    assert set(get_all_subclasses(F)) == set([])

# Generated at 2022-06-12 22:50:07.092072
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    This test verifies that get_all_subclasses() works on a simple tree.
    """
    class Top:
        pass

    class A(Top):
        pass

    class B(Top):
        pass

    class C(Top):
        pass

    class AA(A):
        pass

    class AB(A):
        pass

    class BA(B):
        pass

    class BB(B):
        pass

    class BAA(BA):
        pass

    # Now we have the following tree for classes
    #
    # Top
    # |
    # +---+---+---+
    # |   |   |   |
    # A   B   C   AA
    # |   |   |
    # AB  BA  ABB
    # |   |
    # BAA BB

    result = get

# Generated at 2022-06-12 22:50:11.725362
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

    subclasses = get_all_subclasses(A)
    assert sorted(list(subclasses)) == sorted([B, C, D])



# Generated at 2022-06-12 22:50:14.948633
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(B):
        pass

    assert set(get_all_subclasses(A)) == set((B, C, D))

# Generated at 2022-06-12 22:50:18.097117
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    assert get_all_subclasses(A) == {B, C, D}

# Generated at 2022-06-12 22:50:22.771621
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
    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(E)) == set()
    assert set(get_all_subclasses(object)) == set([A, B, C, D, E])

# Generated at 2022-06-12 22:50:27.312725
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Unit test of get_all_subclasses
    """

    import IPython

    # This class will be used for __subclasses__ test
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    class F(D):
        pass

    assert B in A.__subclasses__()
    assert C in A.__subclasses__()
    assert D in B.__subclasses__()
    assert E in C.__subclasses__()
    assert F in D.__subclasses__()

    assert set([B, C, D, E, F]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:50:32.138441
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test get_all_subclasses() function
    '''
    import unittest
    import pytest

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

    with pytest.raises(TypeError):
        get_all_subclasses("a")

    subclasses_list = get_all_subclasses(A)
    assert len(subclasses_list) == 3
    assert B in subclasses_list
    assert C in subclasses_list
    assert D in subclasses_list

# Generated at 2022-06-12 22:50:34.706574
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(D): pass
    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:50:40.239342
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class Base(object):
        pass

    class A(Base):
        pass

    class B(Base):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class Base2(object):
        pass

    class E(Base2):
        pass

    class F(E):
        pass

    assert set(get_all_subclasses(Base)) == set([A, B, C, D])
    assert set(get_all_subclasses(Base2)) == set([E, F])