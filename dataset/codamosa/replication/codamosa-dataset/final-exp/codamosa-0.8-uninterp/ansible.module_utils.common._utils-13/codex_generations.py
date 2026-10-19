

# Generated at 2022-06-12 22:41:10.947079
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

    classes = get_all_subclasses(A)
    assert B in classes
    assert C in classes
    assert D in classes

# Generated at 2022-06-12 22:41:19.876229
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

    assert E in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)

    assert E in get_all_subclasses(B)
    assert D in get_all_subclasses(B)
    assert C not in get_all_subclasses(B)

    assert E in get_all_subclasses(D)
    assert B in get_all_subclasses(D)
    assert C not in get_all_subclasses(D)



# Generated at 2022-06-12 22:41:31.833725
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

    class H(D):
        pass

    class I(E):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H, I])
    assert set(get_all_subclasses(B)) == set([D, E, H, I])
    assert set(get_all_subclasses(C)) == set([F, G])
    assert set(get_all_subclasses(D)) == set([H])

# Generated at 2022-06-12 22:41:41.873490
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

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H, I])
    assert set(get_all_subclasses(B)) == set([D, E])
    assert set(get_all_subclasses(C)) == set([F, G, H, I])
    assert set(get_all_subclasses(D)) == set([])

# Generated at 2022-06-12 22:41:49.783412
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This function is used to test that get_all_subclasses function is working correctly.

    This class will add a test class under the PSRpTest base class to ensure that it is not caught
    in the get_all_subclasses function (test is recursive to ensure it searches multiple depths).
    This is to ensure that the get_all_subclasses function is not returning PSRpTest as a subclass
    as it's currently a subclass of ConnectionBase to allow it to be found.

    If a class is found as a sublcass of PSRpTest, print a warning to the console.
    '''
    class PSRpTest(object):
        '''
        This class is for testing that get_all_subclasses does not return all classes that inherit
        from PSRpTest.
        '''

# Generated at 2022-06-12 22:41:56.672263
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
    class F(B):
        pass
    class G(D):
        pass
    class H(E):
        pass
    class I(E):
        pass
    class J(H):
        pass
    all_set = set([A, B, C, D, E, F, G, H, I, J])
    assert get_all_subclasses(A) == all_set

# Generated at 2022-06-12 22:42:01.758584
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create 3 classes A -> B -> C
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(C):
        pass

    def test_class(cls, expected_result):
        assert set(C.__subclasses__()) == expected_result
    test_class(C, set())
    test_class(B, {C})
    test_class(A, {B, C})
    test_class(D, set())
    test_class(object, {A, B, C, D})



# Generated at 2022-06-12 22:42:07.854776
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

    class E(object):
        pass

    assert set([B, D]) == get_all_subclasses(A)
    assert set([D]) == get_all_subclasses(B)
    assert set([]) == get_all_subclasses(E)

# Generated at 2022-06-12 22:42:13.453849
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # For example, if we want to get all subclasses of Animal
    class Animal(object):
        pass

    class Dog(Animal):
        pass

    class Bird(Animal):
        pass

    class Sparrow(Bird):
        pass

    class Parrot(Bird):
        pass

    class Cat(Animal):
        pass

    assert get_all_subclasses(Animal) == set([Dog, Bird, Sparrow, Parrot, Cat])

# Generated at 2022-06-12 22:42:20.251275
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class X:
        pass

    class A(X):
        pass

    class B(X):
        pass

    class C(A):
        pass

    class D(A):
        pass

    class E(B):
        pass

    class F(E):
        pass

    class G(F):
        pass

    class H(G):
        pass

    assert set(get_all_subclasses(X)) == {A, B, C, D, E, F, G, H}
    # Note that the G class appears only once
    assert set(get_all_subclasses(G)) == {G, H}
    assert set(get_all_subclasses(H)) == {H}
    assert set(get_all_subclasses(E)) == {E, F, G, H}

# Generated at 2022-06-12 22:42:29.390122
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Dummy class to use for testing.
    """
    class A():
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

    class G(F):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G])

# Generated at 2022-06-12 22:42:37.801031
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(C):
        pass
    class E(C):
        pass
    class F(D, E):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])
    assert set(get_all_subclasses(B)) == set([C, D, E, F])
    assert set(get_all_subclasses(C)) == set([D, E, F])
    assert set(get_all_subclasses(D)) == set([F])
    assert set(get_all_subclasses(E)) == set([F])
    assert set(get_all_subclasses(F)) == set([])

# Generated at 2022-06-12 22:42:48.363762
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test ``get_all_subclasses`` function

    :rtype: bool
    :returns: True on success False on failure
    '''
    from _utils import get_all_subclasses

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

    class F(B, D):
        pass

    class G(B, D, E):
        pass

    class H(E, F, G):
        pass

    class I(H):
        pass

    # The class hierarchy of the above classes is represented by following tree
    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   F   E

# Generated at 2022-06-12 22:42:58.627854
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class BaseClass(object):
        pass

    class Class1(BaseClass):
        pass

    class Class2(BaseClass):
        pass

    class Class1_1(Class1):
        pass

    class Class2_1(Class2):
        pass

    class Class2_2(Class2):
        pass

    class Class2_2_1(Class2_2):
        pass

    class Class2_2_2(Class2_2):
        pass

    class Class2_1_1(Class2_1):
        pass

    class Class2_2_2_1(Class2_2_2):
        pass

    class Class2_2_2_2(Class2_2_2):
        pass


# Generated at 2022-06-12 22:43:09.378212
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Basic classes
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

    class F():
        pass

    assert E in get_all_subclasses(A)

    # Inheritance from __builtin__
    class G(set):
        pass

    class H(G):
        pass

    assert H in get_all_subclasses(set)

    # Inheritance from metaclass
    class I(type):
        def __init__(self, name, bases, dct):
            type.__init__(self, name, bases, dct)

    class J(object):
        __metaclass__ = I

    class K(J):
        pass

   

# Generated at 2022-06-12 22:43:15.082658
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(object): pass
    class C(A): pass
    assert sorted(get_all_subclasses(A)) == [A, C, object]
    assert sorted(get_all_subclasses(B)) == [B, object]
    assert sorted(get_all_subclasses(C)) == [C, object]

# Generated at 2022-06-12 22:43:22.456096
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Unit test for function get_all_subclasses
    """
    import collections
    import unittest

    # Basic tests to test the correct behaviour of the function
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(D): pass
    class G(D, E): pass

    expected_all = set([A, B, C, D, E, F, G])
    expected_a = set([B, C])
    expected_d = set([F, G])

    all = get_all_subclasses(A)
    assert len(expected_all) == len(all)
    assert expected_all == all

    a = get_all_subclasses(A)
    assert len(expected_a)

# Generated at 2022-06-12 22:43:32.771163
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create example of inheritance
    class A(object):
        def __init__(self):
            self.name = "I am an instance of class A"

    class B(A):
        def __init__(self):
            self.name = "I am an instance of class B"

    class C(object):
        def __init__(self):
            self.name = "I am an instance of class C"

    class D(A):
        def __init__(self):
            self.name = "I am an instance of class D"

    class E(D):
        def __init__(self):
            self.name = "I am an instance of class E"

    class F(C, B):
        def __init__(self):
            self.name = "I am an instance of class F"


# Generated at 2022-06-12 22:43:36.746630
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    assert get_all_subclasses(A) == set([B, C, D])



# Generated at 2022-06-12 22:43:40.613731
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
    class G(D):
        pass
    class H(E):
        pass

    # The expected output is a sorted list of the classes
    # The list may be different from the above definition order
    classes = get_all_subclasses(A)
    assert sorted(classes, key=lambda x: x.__name__) == [B, C, D, E, F, G, H]

# Generated at 2022-06-12 22:43:51.450594
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

    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(F) == set([])



# Generated at 2022-06-12 22:44:02.284180
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a fake python class to be used for testing purposes
    class C1:
        def __init__(self):
            pass
    # Create a fake python subclass to be used for testing purposes
    class C2(C1):
        def __init__(self):
            pass
    # Create another fake python subclass to be used for testing purposes
    class C3(C1):
        def __init__(self):
            pass
    # Create another fake python subclass to be used for testing purposes
    class C4(C2):
        def __init__(self):
            pass
    # Create another fake python subclass to be used for testing purposes
    class C5(C4):
        def __init__(self):
            pass
    # Create another fake python subclass to be used for testing purposes

# Generated at 2022-06-12 22:44:06.832303
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import abc
    import sys

    # Sample classes to test get_all_subclasses
    class A: pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(D): pass

    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 4
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses

    subclasses = get_all_subclasses(abc.Hashable)
    assert len(subclasses) > 1
    assert abc.Mapping in subclasses

    subclasses = get_all_subclasses(object)
    assert len(subclasses) > 10
    assert sys.modules['ansible'].plugins.action in subclasses

# Generated at 2022-06-12 22:44:10.223488
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

    class F(D):
        pass

    assert set(get_all_subclasses(A)) == set([B, D, E, C, F])

# Generated at 2022-06-12 22:44:17.006122
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
    class F(A):
        pass
    class G(F):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, F, G])
    assert set(get_all_subclasses(B)) == set([])
    assert set(get_all_subclasses(E)) == set([])

# Generated at 2022-06-12 22:44:22.740298
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base(object): pass
    class A(Base): pass
    class B1(A): pass
    class B2(A): pass
    class C(Base): pass
    class D(C): pass
    class E(C): pass

    assert get_all_subclasses(Base) == set([A, B1, B2, C, D, E])
    assert get_all_subclasses(C) == set([D, E])

# Generated at 2022-06-12 22:44:27.889178
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

    class E(C):
        pass

    class F(C):
        pass

    expected_output = set([B, D, C, E, F])
    assert get_all_subclasses(A) == expected_output

# Generated at 2022-06-12 22:44:38.202894
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Animal(object):
        pass
    class Canine(Animal):
        pass
    class Wolf(Canine):
        pass
    class Dog(Canine):
        pass
    class Feline(Animal):
        pass
    class Cat(Feline):
        pass
    class SmallCat(Cat):
        pass
    class BigCat(Cat):
        pass
    class Lynx(BigCat):
        pass
    class Tiger(BigCat):
        pass
    class Lion(BigCat):
        pass
    animals = get_all_subclasses(Animal)
    assert len(animals) == 9
    assert Wolf in animals
    assert Dog in animals
    assert Cat in animals
    assert SmallCat in animals
    assert BigCat in animals
    assert Lynx in animals
    assert Tiger in animals
    assert Lion in animals

# Generated at 2022-06-12 22:44:48.276388
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # The class to be tested should be in a separate file
    from .test_utils_class import Subclass1a, Subclass1b, Subclass2a, Subclass2b
    from .test_utils_class import Superclass1, Superclass2
    # Uncomment for a more extensive test
    # class Subclass2c(Subclass2a):
    #     pass
    # class Subclass2d(Subclass2a):
    #     pass
    # class Subclass2e(Subclass2b):
    #     pass
    # class Subclass2f(Subclass2b):
    #     pass
    # class Superclass3(Superclass2):
    #     pass
    # class Subclass3a(Superclass3):
    #     pass
    # class Subclass3b(Superclass3):
    #     pass


# Generated at 2022-06-12 22:44:56.346825
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # We create a sample class hierarchy
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
    class G(D):
        pass
    class H(D):
        pass
    class I(E,F):
        pass
    class J(G,H):
        pass
    class K(I,J):
        pass
    class L(K):
        pass

    expected = {L, K, J, G, I, H, F, E, D, C, B, A}
    assert(expected == get_all_subclasses(A))

# Generated at 2022-06-12 22:45:11.304416
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
    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I])
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set([F, G, H, I])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])
    assert get_

# Generated at 2022-06-12 22:45:21.903508
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
    class E(B):
        pass
    class F(C):
        pass
    class G(F):
        pass
    class H(F):
        pass

    assert set([A, B, C, D, E, F, G, H]) == get_all_subclasses(A)
    assert set([B, C, D, E, F, G, H]) == get_all_subclasses(B)
    assert set([C, D, E, F, G, H]) == get_all_subclasses(C)
    assert set([D, E]) == get_all_subclasses(D)
    assert set([E]) == get_all_subclasses

# Generated at 2022-06-12 22:45:29.558443
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Given a class A with a single subclass B and a single subclass of B (C),
    get_all_subclasses(A) should return {B, C}.
    '''
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    subclasses = get_all_subclasses(A)
    assert set(subclasses) == set([B, C])
    # Do not modifiy B.__subclasses__, it should be empty
    assert list(B.__subclasses__()) == list([])
    # Do not modifiy C.__subclasses__, it should be empty
    assert list(C.__subclasses__()) == list([])


# Generated at 2022-06-12 22:45:39.610098
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """Unit test for function get_all_subclasses"""
    # base class
    class A(object):
        pass

    # direct subclasses of A
    class B(A):
        pass

    class C(A):
        pass

    # indirect subclasses of A
    class D(B):
        pass

    class E(B):
        pass

    class F(C):
        pass

    class G(C):
        pass

    # indirect subclass of D
    class H(D):
        pass

    # In this example, all classes from A to H have to be tested
    class_set = get_all_subclasses(A)
    class_dict = {}
    for the_class in class_set:
        class_dict[the_class] = 0

    assert 'A' not in class_dict

# Generated at 2022-06-12 22:45:47.458586
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
    l = get_all_subclasses(A)
    assert set(l) == {B, C, D, E, F, G, H}
    l = get_all_subclasses(B)
    assert set(l) == {D, E}
    l = get_all_subclasses(C)
    assert set(l) == {F, G, H}
    l = get_all_subclasses(D)
    assert set(l) == set()
    l = get_all

# Generated at 2022-06-12 22:45:52.411237
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

    class E(C):
        pass

    class F(C):
        pass

    class G():
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:45:58.221539
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
    class F(C):
        pass
    # If the function works, class A should have B, C, D, E, F as subclasses
    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:46:03.614908
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
    class E(B,C,D):
        pass
    class F(E):
        pass
    assert get_all_subclasses(A) == set([B, C, D, E, F])


# Generated at 2022-06-12 22:46:13.035730
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

    # Testing with object class
    assert set() == get_all_subclasses(object)

    # Testing with single class
    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses

    # Testing with classic DAG
    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses

    subclasses = get_all_subclasses(B)

# Generated at 2022-06-12 22:46:20.251030
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class a(object): pass
    class b(a): pass
    class c(a): pass
    class d(b): pass
    class e(c): pass
    class f(d): pass
    class g(f): pass

    assert set([d, f, g]) == get_all_subclasses(b)
    assert set([e, d, f, g]) == get_all_subclasses(a)
    assert set([f, g]) == get_all_subclasses(d)
    assert set([]) == get_all_subclasses(g)
    assert set([g]) == get_all_subclasses(f)
    assert set([]) == get_all_subclasses(e)

# Generated at 2022-06-12 22:46:41.612830
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object): pass
    class A1(A): pass
    class A2(A): pass
    class A3(A): pass
    class A11(A1): pass
    class A12(A1): pass
    class A13(A1): pass
    class A21(A2): pass
    class A22(A2): pass
    class A23(A2): pass

    classes = [A, A1, A2, A3, A11, A12, A13, A21, A22, A23]
    assert classes == list(get_all_subclasses(A))

    class B(object): pass
    class C(object): pass
    class D(B,C): pass
    class E(B,C): pass
    class F(D,E): pass

# Generated at 2022-06-12 22:46:48.303111
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
    class F(E):
        pass
    class G(object):
        pass
    subclasses = get_all_subclasses(A)
    assert subclasses == set((B, C, D, E, F))
    subclasses = get_all_subclasses(E)
    assert subclasses == set((F,))
    subclasses = get_all_subclasses(G)
    assert subclasses == set()

# Generated at 2022-06-12 22:46:58.890193
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a test class hierarchy
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

    class F(D):
        pass

    class G(F):
        pass

    class H(F):
        pass

    class I(F):
        pass

    class J(F):
        pass

    class K(J):
        pass

    class L(J):
        pass

    class M(J):
        pass

    class N(L):
        pass

    # Testing class hierarchy
    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)

# Generated at 2022-06-12 22:47:06.526378
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(D): pass
    class F(D): pass
    class G(F): pass
    class H(F): pass
    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 6
    # test that all subclasses are intended
    assert set(subclasses) == set([B, C, D, E, F, G])
    # and that we don't have false positive
    assert H not in subclasses



# Generated at 2022-06-12 22:47:12.751146
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

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([])
    assert get_all_subclasses(C) == set([D, E])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:47:18.124171
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

    class G(D):
        pass

    assert set([C, D, E, F, G]) == get_all_subclasses(A)

    assert set([B]) == get_all_subclasses(B)

    assert set([E, F]) == get_all_subclasses(C)

    assert set([G]) == get_all_subclasses(D)

# Test our function
test_get_all_subclasses()

# Generated at 2022-06-12 22:47:28.478157
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C, B): pass
    class F(D, E, C): pass

    assert get_all_subclasses(A) == {B, C, D, E, F}
    assert get_all_subclasses(B) == {D, E, F}
    assert get_all_subclasses(C) == {E, F}
    assert get_all_subclasses(D) == {F}
    assert get_all_subclasses(E) == {F}
    assert get_all_subclasses(F) == set()

    class G: pass
    class H(G): pass
    class I(H): pass
    class J(G): pass

# Generated at 2022-06-12 22:47:35.428429
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses
    '''
    class A:
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



# Generated at 2022-06-12 22:47:40.035280
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

    class E(D):
        pass

    class F(C):
        pass

    assert get_all_subclasses(B) == {D, E}
    assert get_all_subclasses(C) == {F}
    assert get_all_subclasses(A) == {B, C, D, E, F}

# Generated at 2022-06-12 22:47:46.851012
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import pytest

    #  Test class
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(D): pass

    #  Expected results
    expected_results = [B, C, D, E]

    #  Obtain obtained results
    obtained_results = get_all_subclasses(A)

    #  Check if results obtained are the same as expected results
    for res in obtained_results:
        assert res in expected_results

    #  Check if results expected are the same as obtained results
    for res in expected_results:
        assert res in obtained_results

# Generated at 2022-06-12 22:48:22.045357
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create classes for testing purpose
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(B):
        pass
    class E(object):
        pass

    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([C, D])
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:48:29.473694
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    def _AssertClassesIncludedOnce(classes_to_check, classes_to_find):
        for c in classes_to_check:
            assert c in classes_to_find, "%s not in %s" % (c, classes_to_find)
            classes_to_find.remove(c)
        assert not classes_to_find, "returned subclasses %s should not have any remaining elements" % classes_to_find

    class C1(object):
        pass

    class C2(object):
        pass

    class C3(object):
        pass

    class C4(C1, C2):
        pass

    class C5(C1, C2):
        pass

    class C6(C3):
        pass

    class C7(C3):
        pass

   

# Generated at 2022-06-12 22:48:37.624432
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # a very rudimental test, mainly to avoid import error
    from ansible.module_utils._text import to_bytes
    bytes_ = get_all_subclasses(to_bytes('foo'))
    assert bytes_ == set()

# Test data for funcs_module._load_params
TEST_MODULE_PARAMETERS = {
    'one': 1,
    'two': 'two',
    'three': {'three_one': 3.1},
    'four': 4,
    'five': [5.1, 5.2],
}


# Generated at 2022-06-12 22:48:44.653594
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

    assert get_all_subclasses(A) == {B, C, D}
    assert get_all_subclasses(B) == {C}
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

from ansible.module_utils.six import iteritems
from ansible.module_utils._text import to_text, to_bytes



# Generated at 2022-06-12 22:48:49.722966
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test case for AnsibleModule.get_all_subclasses() method.
    '''
    class Parent(object):
        pass

    class Child(Parent):
        pass

    class Grandchild(Child):
        pass

    class Uncle(Parent):
        pass

    class Niece(Uncle):
        pass

    class Nephew(Uncle):
        pass

    assert set(get_all_subclasses(Parent)) == set([Child, Grandchild, Uncle, Niece, Nephew])

# Generated at 2022-06-12 22:48:53.137933
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

    class E(C):
        pass
    
    class Z(D):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, Z])

# Generated at 2022-06-12 22:49:01.151094
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Create A class
    class A:
        pass

    # Create B class from A
    class B(A):
        pass

    # Create C class from B
    class C(B):
        pass

    # Create D class
    class D:
        pass

    # Create E class from D
    class E(D):
        pass

    # Create F class from E and C
    class F(C, E):
        pass

    result = get_all_subclasses(A)
    assert result == set([B, C, F])

    result = get_all_subclasses(B)
    assert result == set([C, F])

    result = get_all_subclasses(D)
    assert result == set([E, F])

# Generated at 2022-06-12 22:49:08.244031
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B: pass
    class C: pass
    class D(A): pass
    class E(D): pass
    class F(B): pass
    class G(C): pass
    class H(G): pass
    class I(F): pass
    class J(E): pass

    test_list = get_all_subclasses(object)
    assert set([D, E, J]) <= test_list
    assert 'test_get_all_subclasses.<locals>.D' in repr(D)
    assert 'test_get_all_subclasses.<locals>.E' in repr(E)
    assert 'test_get_all_subclasses.<locals>.J' in repr(J)


# Generated at 2022-06-12 22:49:12.972429
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses
    '''
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
    class F(A):
        pass
    assert set([B, C, D, E, F]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:49:21.794235
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
    class F(E):
        pass
    class G(F):
        pass
    class H(E):
        pass
    class I(G):
        pass

    assert(set(get_all_subclasses(A)) == set([B, C, D]))
    assert(set(get_all_subclasses(B)) == set([C]))
    assert(set(get_all_subclasses(E)) == set([F, G, H]))
    assert(set(get_all_subclasses(G)) == set([I]))

# Generated at 2022-06-12 22:50:38.984868
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Building a tree of classes
    class ClassA:
        pass

    class ClassB(ClassA):
        pass

    class ClassC(ClassA):
        pass

    class ClassD(ClassB):
        pass

    class ClassE(ClassC):
        pass

    class ClassF(ClassC):
        pass

    class ClassG(ClassC):
        pass

    class ClassH(ClassD):
        pass

    class ClassI(ClassD):
        pass

    # Python interpretor ensure that this is the same instance
    assert ClassA.__subclasses__() == [ClassB, ClassC], \
        'Failed to retrieve direct subclasses'

# Generated at 2022-06-12 22:50:44.255341
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Given
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
    # When
    subclasses = get_all_subclasses(A)
    # Then
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses

# Generated at 2022-06-12 22:50:50.202833
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Test:
        pass
    class Test1(Test):
        pass
    class Test2(Test):
        pass

    assert set(get_all_subclasses(Test)) == set([Test1, Test2])

    class Test11(Test1):
        pass
    class Test12(Test1):
        pass
    class Test21(Test2):
        pass
    class Test22(Test2):
        pass

    assert set(get_all_subclasses(Test)) == set([Test1, Test2, Test11, Test12, Test21, Test22])

# Generated at 2022-06-12 22:50:54.079037
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import abc
    class A(object):
        __metaclass__ = abc.ABCMeta
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

    subclasses = get_all_subclasses(A)
    assert set([B, C, D, E, F]) == subclasses

# Generated at 2022-06-12 22:51:02.001971
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass

    retA = get_all_subclasses(A)
    retB = get_all_subclasses(B)
    retC = get_all_subclasses(C)
    retD = get_all_subclasses(D)
    retE = get_all_subclasses(E)

    assert D in retA
    assert E in retA
    assert D in retB
    assert not E in retB
    assert not D in retC
    assert E in retC
    assert not D in retE
    assert not E in retD
    assert not E in retE

# Generated at 2022-06-12 22:51:08.043520
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Used to unit test the get_all_subclasses() function

    When a new class is added, ensure it is added to the list of classes
    in get_all_subclasses() function.
    '''
    # Setup a hierarchy from a classic example
    class Animal(object):
        pass

    class Mammal(Animal):
        pass

    class Carnivoral(Mammal):
        pass

    class Herbivoral(Mammal):
        pass

    class Cat(Carnivoral):
        pass

    class Dog(Carnivoral):
        pass

    class Cow(Herbivoral):
        pass

    class Pig(Herbivoral):
        pass

    # This list must be updated whenever a new class is added,
    # to ensure all subclasses are correctly listed in get_all_subclasses()
   