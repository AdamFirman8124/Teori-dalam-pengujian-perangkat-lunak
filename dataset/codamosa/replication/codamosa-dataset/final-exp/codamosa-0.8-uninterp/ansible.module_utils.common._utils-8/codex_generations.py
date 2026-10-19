

# Generated at 2022-06-12 22:41:13.717843
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

    class F(E):
        pass

    assert get_all_subclasses(A) == set([B, D, C])
    assert get_all_subclasses(B) == set([])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([F])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:41:19.140734
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class A1(A): pass
    class A2(A): pass
    class A3(A): pass
    class A11(A1): pass
    class A12(A1): pass
    class A21(A2): pass
    class A22(A2): pass
    assert set(get_all_subclasses(A)) == set([A1, A3, A2, A11, A12, A21, A22])

# Generated at 2022-06-12 22:41:22.299919
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class MyClassA(object):
        pass

    class MyClassB(object):
        pass

    class MyClassC(MyClassA):
        pass

    class MyClassD(MyClassC):
        pass

    class MyClassE(MyClassC):
        pass

    assert get_all_subclasses(MyClassA) == set((MyClassC, MyClassD, MyClassE))



# Generated at 2022-06-12 22:41:28.310269
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Given the following class
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

# Generated at 2022-06-12 22:41:36.469668
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Toto(object):
        pass

    class Tata(Toto):
        pass

    class Tutu(Toto):
        pass

    class Titi(Tutu):
        pass

    toto_classes = get_all_subclasses(Toto)
    assert(len(toto_classes) == 3)
    assert(Tata in toto_classes)
    assert(Tutu in toto_classes)
    assert(Titi in toto_classes)

    tutu_classes = get_all_subclasses(Tutu)
    assert(len(tutu_classes) == 1)
    assert(Titi in tutu_classes)

# Generated at 2022-06-12 22:41:44.308596
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

    class F(D):
        pass

    class G(F):
        pass

    class H(E):
        pass

    assert set([B, D, F, G, C, E, H]) == get_all_subclasses(A)
    assert set([D, F, G]) == get_all_subclasses(B)
    assert set([E, H]) == get_all_subclasses(C)
    assert set([G]) == get_all_subclasses(F)
    assert set([H]) == get_all_subclasses(E)

# Generated at 2022-06-12 22:41:53.096416
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(Exception):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(Exception):
        pass

    assert set(get_all_subclasses(Exception)) == set([A, B, C, D, E])
    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set([])
    assert set(get_all_subclasses(C)) == set([D])
    assert set(get_all_subclasses(D)) == set([])
    assert set(get_all_subclasses(E)) == set([])

# Generated at 2022-06-12 22:42:03.268571
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses

    :returns: None
    :rtype: None
    '''
    class A():
        __doc__ = "Mock class A"
    class B(A):
        __doc__ = "Mock class B"
    class C(B):
        __doc__ = "Mock class C"
    class D(C):
        __doc__ = "Mock class D"
    class E(A):
        __doc__ = "Mock class E"
    class F(A):
        __doc__ = "Mock class F"
    class G(E, F):
        __doc__ = "Mock class G"
    class H(E):
        __doc__ = "Mock class H"
    class I(G, H):
        __doc__

# Generated at 2022-06-12 22:42:08.152201
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
    assert get_all_subclasses(A) == {B, C, D}



# Generated at 2022-06-12 22:42:17.409178
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import pytest

    class A:
        pass

    class B:
        pass

    class C:
        pass

    class D(B, C):
        pass

    class E(A):
        pass

    class F(E):
        pass

    assert set(get_all_subclasses(A)) == set([E, F])
    assert set(get_all_subclasses(B)) == set([D])
    assert set(get_all_subclasses(C)) == set([D])
    assert set(get_all_subclasses(D)) == set([])
    assert set(get_all_subclasses(E)) == set([F])
    assert set(get_all_subclasses(F)) == set([])

    with pytest.raises(TypeError):
        get_all_subclasses('not a class')

# Generated at 2022-06-12 22:42:30.804876
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Parent(object):
        pass

    class ChildA(Parent):
        pass

    class ChildB(Parent):
        pass

    class Grandchild(ChildA):
        pass

    class Hidden(ChildA):
        pass

    assert Hidden not in get_all_subclasses(Parent)
    assert Hidden in get_all_subclasses(ChildA)
    assert Grandchild in get_all_subclasses(ChildA)
    assert Grandchild in get_all_subclasses(Parent)
    assert ChildA not in get_all_subclasses(Parent)
    assert Parent not in get_all_subclasses(Parent)

# Generated at 2022-06-12 22:42:35.542513
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

    assert set([D, E]) == get_all_subclasses(B)
    assert set([B, C, D, E]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:42:40.841630
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

    class E(object):
        pass

    class F(E):
        pass

    class G(F):
        pass

    class H(G):
        pass

    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([C, D])
    assert get_all_subclasses(E) == set([F, G, H])
    assert get_all_subclasses(F) == set([G, H])
    assert get_all_subclasses(H) == set([])



# Generated at 2022-06-12 22:42:52.284951
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import os
    import sys

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

    class F(C):
        pass

    class G(D):
        pass

    class H(E):
        pass

    class I(E):
        pass

    assert G in get_all_subclasses(A)
    assert H in get_all_subclasses(A)
    assert I in get_all_subclasses(A)
    assert G in get_all_subclasses(B)
    assert G in get_all_subclasses(C)
    assert G in get_all_subclasses(D)
    assert H in get_all_subclasses(E)
    assert I

# Generated at 2022-06-12 22:42:56.472520
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

    class E(D):
        pass

    result = get_all_subclasses(A)
    assert result == {B, C, D, E}

# Generated at 2022-06-12 22:43:02.994182
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
    class E(B):
        pass
    #
    #          A
    #         / \
    #        B   C
    #        |   |
    #        E   D
    #
    #
    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([E])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:43:07.524189
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A, object):
        pass
    class C(A, object):
        pass
    class D(B, C, object):
        pass
    assert set((A, B, C, D)) == get_all_subclasses(A)

# Generated at 2022-06-12 22:43:15.370632
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
    class E(C):
        pass
    class F(E):
        pass
    l = get_all_subclasses(A)
    assert B in l
    assert C in l
    assert D in l
    assert E in l
    assert F in l
    assert len(l) == 5

# Generated at 2022-06-12 22:43:20.314476
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
    class G(C):
        pass
    class H(F):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H])



# Generated at 2022-06-12 22:43:28.521687
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base(object):
        pass
    class A(Base):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(C):
        pass
    class E(D):
        pass
    class F(D):
        pass
    class G(D):
        pass

    subclasses = get_all_subclasses(Base)
    assert set(('A', 'B', 'C', 'D', 'E', 'F', 'G')) == {cls.__name__ for cls in subclasses}

# Generated at 2022-06-12 22:43:43.833871
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    This test generates a hypothetical class hierarchy and then checks
    to ensure that the get_all_subclasses function is working properly.
    """
    class Base(object):
        def test_method(self):
            pass

    class One(Base):
        pass

    class Two(Base):
        pass

    class Three(One):
        pass

    class Four(Three):
        pass

    class Five(Four, Two):
        pass

    assert get_all_subclasses(Base) == set([One, Two, Three, Four, Five])

# Generated at 2022-06-12 22:43:53.335434
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B: pass
    class C: pass
    class D(A): pass
    class E(B): pass
    class F(C): pass
    class G(D, B): pass
    class H(D, E, F): pass

    # Test: get_all_subclasses(A) == [D, G, H]
    assert get_all_subclasses(A) == set([D, G, H])
    # Test: get_all_subclasses(B) == [G, H, E]
    assert get_all_subclasses(B) == set([G, H, E])
    # Test: get_all_subclasses(D) == [G, H]
    assert get_all_subclasses(D) == set([G, H])

# Function test_get_all_sub

# Generated at 2022-06-12 22:44:05.142975
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Test the function get_all_subclasses by applying it on a tree.
    """
    class BaseClass(object):
        """
        Base class for testing the method get_all_subclasses
        """
        pass

    class A(BaseClass):
        """
        First subclass of the BaseClass
        """
        pass

    class B(BaseClass):
        """
        Second subclass of the BaseClass
        """
        pass

    class C(A):
        """
        First subclass of A
        """
        pass

    class D(A):
        """
        Second subclass of A
        """
        pass

    class E(B):
        """
        First subclass of B
        """
        pass

    assert set(get_all_subclasses(BaseClass)) == set([A, B, C, D, E])

# Generated at 2022-06-12 22:44:09.469375
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # We add 2 new classes which inherit
    class A(Exception):
        pass
    class B(A):
        pass

    # Check classes are retrieved
    assert get_all_subclasses(Exception) == {A, B}

    class C(Exception):
        pass
    class D(C):
        pass

    assert get_all_subclasses(Exception) == {A, B, C, D}

# Generated at 2022-06-12 22:44:20.058636
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # parent_class and child_class are taken from docs
    # parent_class and child_class.child_class2 are taken from ansible
    # grandchild_class and grandchild_class.child_class are taken from ansible
    class parent_class(object):
        pass

    class child_class(parent_class):
        pass

    class child_class2(parent_class):
        pass

    class grandchild_class(child_class):
        pass

    class grandchild_class_child_class(grandchild_class):
        pass

    classes = (
        parent_class,
        child_class,
        child_class2,
        grandchild_class,
        grandchild_class_child_class
    )

    assert set(get_all_subclasses(parent_class)) == set(classes)
    assert set

# Generated at 2022-06-12 22:44:29.118115
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # The default class
    class A(object):
        pass
    # The first level of subclasses
    class B(A):
        pass
    class C(A):
        pass
    # The second level of subclasses
    class D(B):
        pass
    class E(B):
        pass
    class F(C):
        pass
    # The third level of subclasses
    class G(D):
        pass

    assert set(get_all_subclasses(A)) == {E, F, B, G, D, C}
    assert set(get_all_subclasses(B)) == {E, G, D}
    assert set(get_all_subclasses(C)) == {F}
    assert set(get_all_subclasses(D)) == {G}

# Generated at 2022-06-12 22:44:39.157501
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This function tests the get_all_subclasses function.
    '''
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(C):
        pass
    class E(A):
        pass

    assert len(get_all_subclasses(A)) == 4
    assert len(get_all_subclasses(B)) == 0
    assert len(get_all_subclasses(C)) == 1
    assert len(get_all_subclasses(D)) == 0
    assert len(get_all_subclasses(E)) == 0

    # Import ansible.module_utils.*
    import ansible.module_utils
    import ansible.module_utils._text
    # Create a list of all classes in ansible.module_utils*

# Generated at 2022-06-12 22:44:45.383488
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Sample class hierarchy with 3 levels
    class Base(object):
        pass

    class A(Base):
        pass

    class B(Base):
        pass

    class C(B):
        pass

    class D(A):
        pass

    # Testing that all subclasses are returned
    subclasses = get_all_subclasses(Base)
    assert A in subclasses
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses

# Generated at 2022-06-12 22:44:52.465284
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a test class
    class A(object):
        pass
    class B(A):
        pass
    class D(A):
        pass
    class C(B):
        pass
    class E(B):
        pass

    # Test the function
    assert(get_all_subclasses(A) == set([B, C, D, E, B]))
    assert(get_all_subclasses(B) == set([C, E, B]))
    assert(get_all_subclasses(D) == set())
    assert(get_all_subclasses(C) == set())

# Generated at 2022-06-12 22:45:00.849245
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class BaseClass(object):
        pass

    class ChildClass1(BaseClass):
        pass

    class ChildClass2(BaseClass):
        pass

    class BaseClass2(object):
        pass

    class ChildClass3(ChildClass1):
        pass

    class ChildClass4(ChildClass2):
        pass

    class ChildClass5(ChildClass3):
        pass

    class BaseClass3(object):
        pass

    subclasses_of_baseclass = get_all_subclasses(BaseClass)
    assert len(subclasses_of_baseclass) == 4
    assert ChildClass1 in subclasses_of_baseclass
    assert ChildClass2 in subclasses_of_baseclass
    assert ChildClass3 in subclasses_of_baseclass
    assert ChildClass4 in subclasses_of_baseclass
    assert ChildClass5

# Generated at 2022-06-12 22:45:13.041726
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():pass
    class B(A):pass
    class C(A):pass
    class D(B):pass
    class E(C):pass
    class F():pass
    class G(F):pass
    class H(G):pass
    assert set(get_all_subclasses(A)) == set([B, D, C, E])
    assert set(get_all_subclasses(F)) == set([G, H])
    assert set(get_all_subclasses(A)) == set(get_all_subclasses(A) + get_all_subclasses(F))



# Generated at 2022-06-12 22:45:23.544792
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This function tests the get_all_subclasses function.  It is implemented as a class so that
    the class hierarchy is defined in the same scope as the classes.
    '''

    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(B): pass

    # For each class, define a set of expected subclasses. This is the expected output of the
    # get_all_subclasses function.
    # For A, the expected subclasses are B, C, D, and E.
    expected_subclasses = {B, C, D, E}
    # For B, the expected subclasses are E.
    subclass_of_B = {E}
    # For C, the expected subclasses are D.

# Generated at 2022-06-12 22:45:27.687905
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    assert set(get_all_subclasses(A)) == set([B, C])

    class D(B):
        pass

    class E(C):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E])

# Generated at 2022-06-12 22:45:30.841356
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
    assert get_all_subclasses(A) == set([B, D, C])



# Generated at 2022-06-12 22:45:34.450208
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import ansible.plugins.module_utils.cloud

    classes = get_all_subclasses(ansible.plugins.module_utils.cloud.BaseCloudModule)
    assert ansible.plugins.module_utils.cloud.Vultr(None) in classes



# Generated at 2022-06-12 22:45:39.412693
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

    class E(C):
        pass

    class F(E):
        pass

    assert get_all_subclasses(A) == set(A, B, C, D, E, F)

# Generated at 2022-06-12 22:45:47.399244
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    from ansible.module_utils._text import to_text

    class b1(object):
        pass

    class b2(object):
        pass

    class b3(object):
        pass

    class b4(object):
        pass

    class c1(b1, b2):
        pass

    class c2(b2, b3):
        pass

    class c3(c1):
        pass

    class c4(c3):
        pass

    class c5(object):
        pass

    class c6(object):
        pass

    class c7(c5):
        pass

    class c8(c5):
        pass

    class c9(c5, c6, c7, c8):
        pass

    class c10(c2):
        pass

   

# Generated at 2022-06-12 22:45:57.533037
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    class DummyClass(object):
        pass

    class DummyClassA(DummyClass):
        pass

    class DummyClassB(DummyClass):
        pass

    class DummyClassC(DummyClass):
        pass

    class DummyClassC1(DummyClassC):
        pass

    class DummyClassC2(DummyClassC):
        pass

    class DummyClassC1A(DummyClassC1):
        pass

    class DummyClassC2A(DummyClassC2):
        pass

    class TestGetSubclasses(unittest.TestCase):

        def test_base(self):
            subclasses = get_all_subclasses(DummyClass)
            self.assertEqual(len(subclasses), 6)

# Generated at 2022-06-12 22:46:01.666356
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

    result = get_all_subclasses(A)
    assert result == set([B, C, D])

# Generated at 2022-06-12 22:46:11.529045
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    # We cannot use the unittest.TestCase class because the get_all_subclasses method
    # depends on it, so it would create a circular dependency.  We also create our own
    # TestCase class because we do not need all features of unittest.TestCase; we only
    # need to compare lists.
    class TestCase(object):
        def assertListEqual(self, first, second):
            self.assertTrue(isinstance(first, list))
            self.assertTrue(isinstance(second, list))
            self.assertEqual(len(first), len(second))
            for val in first:
                self.assertTrue(val in second)

    class TestA(object):
        pass

    class TestB(object):
        pass


# Generated at 2022-06-12 22:46:28.045544
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass

    r = get_all_subclasses(A)
    assert len(r) == 4
    assert B in r
    assert C in r
    assert D in r
    assert E in r

# Generated at 2022-06-12 22:46:36.552204
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses()
    '''
    # Testing code
    import unittest
    class TestClass():
        pass
    class TestClass1(TestClass):
        pass
    class TestClass2(TestClass):
        pass
    class TestClass22(TestClass2):
        pass
    class TestClass3(TestClass):
        pass
    class TestClass33(TestClass3):
        pass
    class TestClass333(TestClass33):
        pass
    class TestClass4(TestClass):
        pass
    class TestClass5(TestClass):
        pass
    class TestClass6(TestClass):
        pass
    class TestClass7(TestClass):
        pass
    # List the all subclasses of TestClass

# Generated at 2022-06-12 22:46:44.172711
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

    try:
        # Test1: check if the returned result contains all expected classes
        assert(set(get_all_subclasses(A)) == set([B, C, D, E]))

        # Test2: check if function return None if the input class is not a parent
        assert(get_all_subclasses(B) is None)
    except AssertionError:
        # This code is only use for unit test, and it should be called an AssertionError error.
        # However it is a function which cannot raise error so we manually write a Traceback message
        # and exit the program
        import traceback

# Generated at 2022-06-12 22:46:55.090878
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test function get_all_subclasses
    '''
    # Define a set of classes for test
    class ClassA():
        pass

    class ClassB(ClassA):
        pass

    class ClassC(ClassA):
        pass

    class ClassD(ClassB):
        pass

    class ClassE(ClassC):
        pass

    # Get all classes
    classes = get_all_subclasses(ClassA)
    assert(set(classes) == {ClassB, ClassC, ClassD, ClassE})

    # Get direct subclasses
    classes = get_all_subclasses(ClassA, include_self=False)
    assert(set(classes) == {ClassB, ClassC})

    # No class
    classes = get_all_subclasses(ClassA, include_self=True)

# Generated at 2022-06-12 22:47:02.626763
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This is a test to verify that get_all_subclasses works as expected.
    '''
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(object):
        pass
    class E(D):
        pass
    class F(E):
        pass
    class G(B):
        pass
    class H(E):
        pass
    assert get_all_subclasses(A) == set([B, C, G])
    assert get_all_subclasses(B) == set([G])
    assert get_all_subclasses(D) == set([E, F, H])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:47:11.906032
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
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

    assert get_all_subclasses(A) == {B, C, D}
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(C) == {D}

    class F(object):
        pass

    class G(F):
        pass

    assert get_all_subclasses(F) == {G}
    assert get_all_subclasses(G) == set()

    class H(object):
        pass

    class I(object):
        pass

    assert get_all_

# Generated at 2022-06-12 22:47:18.818384
# Unit test for function get_all_subclasses

# Generated at 2022-06-12 22:47:26.508404
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
    class E(C):
        pass
    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([E])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:47:34.353324
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert get_all_subclasses(A) == {B, C}

    class D(A):
        pass

    class E(D):
        pass

    class F(C):
        pass

    class G(F):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F, G}
    assert get_all_subclasses(B) == {C}
    assert get_all_subclasses(C) == {F, G}



# Generated at 2022-06-12 22:47:41.597878
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses
    '''

    class A(object):
        '''
        A simple class
        '''
        pass

    class B(A):
        '''
        A simple class
        '''
        pass

    class C(A):
        '''
        A simple class
        '''
        pass

    class D(C):
        '''
        A simple class
        '''
        pass

    class E(D):
        '''
        A simple class
        '''
        pass

    class F(B, C):
        '''
        A simple class
        '''
        pass

    class G(F):
        '''
        A simple class
        '''
        pass

    subclasses_A = get_all_subclasses(A)
   

# Generated at 2022-06-12 22:48:13.172665
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

    assert set(get_all_subclasses(A)) == set([B, C, D, E])
    assert set(get_all_subclasses(B)) == set([D, E])

# Generated at 2022-06-12 22:48:20.129562
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    
    subclasses = get_all_subclasses(A)

    assert(set(subclasses) == set([B, C, D, E, F]))

# Generated at 2022-06-12 22:48:25.117021
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    This unit test ensures that all subclasses are retrieved when calling get_all_subclasses()
    """
    for cls in get_all_subclasses(object):
        assert issubclass(cls, object)
    for cls in get_all_subclasses(int):
        assert issubclass(cls, int)
    for cls in get_all_subclasses(str):
        assert issubclass(cls, str)
    # If a class has no subclasses, get_all_subclasses should return an empty collection
    assert not get_all_subclasses(Exception)



# Generated at 2022-06-12 22:48:27.910551
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E])

# Generated at 2022-06-12 22:48:36.341489
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Make a test class hierarchy similar to what we have in ansible - connection plugins, shell plugins, etc.
    # Classes that have a parent class in the hierarchy, we will make them subclasses of the parent in this class.
    # Classes that have a parent class in the hierarchy and are not included, we will add them in as subclasses.
    # This allows us to test that get_all_subclasses() returns the correct subtree of the class hierarchy.
    class ClassA(object):
        pass
    class ClassB(ClassA):
        pass
    class ClassC(ClassA):
        pass
    class ClassD(ClassB):
        pass
    class ClassE(ClassB):
        pass
    class ClassF(ClassA):
        pass
    class ClassG(object):
        pass
    class ClassH(ClassA):
        pass

# Generated at 2022-06-12 22:48:44.085703
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types

    # Define a class tree
    class A(object):
        pass
    class B(A):
        pass
    class C(object):
        pass
    class D(A):
        pass
    class E(D):
        pass

    # Searching the tree show the good results
    assert get_all_subclasses(object) == set(map(types.FunctionType, [A, B, C, D, E]))
    assert get_all_subclasses(A) == set(map(types.FunctionType, [B, D, E]))
    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:48:51.405693
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    ''' test_get_all_subclasses is a unit test for get_all_subclasses
    '''
    class ParentA(object):
        pass

    class ChildA(ParentA):
        pass

    class ChildB(ParentA):
        pass

    class GrandChildA(ChildB):
        pass

    class ParentB(object):
        pass

    class ParentC(object):
        pass

    class ChildC(ParentC):
        pass

    class GrandChildC(ChildC):
        pass

    subclasses = get_all_subclasses(ParentA)
    assert len(subclasses) == 4
    assert ChildA in subclasses
    assert ChildB in subclasses
    assert GrandChildA in subclasses
    assert GrandChildC not in subclasses

    subclasses = get_all_subclasses(ParentC)

# Generated at 2022-06-12 22:48:55.100153
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(object): pass

    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:49:03.376632
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def create_class_tree():
        class A(object): pass
        class B(A): pass
        class C(A): pass
        class D(B): pass
        class E(D): pass

        return A, B, C, D, E

    A, B, C, D, E = create_class_tree()
    assert set(get_all_subclasses(A)) == set([B, C, D, E])
    assert set(get_all_subclasses(B)) == set([D, E])
    assert set(get_all_subclasses(C)) == set()
    assert set(get_all_subclasses(D)) == set([E])
    assert set(get_all_subclasses(E)) == set()


# Generated at 2022-06-12 22:49:09.661615
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses
    '''
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(A):
        pass
    class E(C):
        pass
    class F(D):
        pass
    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])
    assert set(get_all_subclasses(B)) == set([C, E])
    assert set(get_all_subclasses(C)) == set([E])
    assert set(get_all_subclasses(D)) == set([F])
    assert set(get_all_subclasses(E)) == set()
    assert set(get_all_subclasses(F)) == set()

# Generated at 2022-06-12 22:50:25.397193
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A:
        '''Simple class'''
    class B(A):
        '''Subclass of A'''
    class C(A):
        '''Subclass of A'''
    class D(A):
        '''Subclass of A'''
    class E(D):
        '''Subclass of A and D'''
    class F(D):
        '''Subclass of A and D'''
    class G(A):
        '''Subclass of A'''

    # Check number of class
    assert(len(get_all_subclasses(A)) == 7)

test_get_all_subclasses()

# Generated at 2022-06-12 22:50:28.472033
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(B): pass
    class G(C): pass
    class H(D): pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H])

# Generated at 2022-06-12 22:50:31.800817
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''test for function get_all_subclasses'''

    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    # All class using object as parent
    assert get_all_subclasses(object) == {A, B, C}
    # All class using A as parent
    assert get_all_subclasses(A) == {B, C}

    class D(object):
        pass

    class E(D):
        pass
    # Testing the algorithm works when classes have multiple common parents
    assert get_all_subclasses({A, D}) == {B, C, E}

# Generated at 2022-06-12 22:50:35.517975
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

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([D])

# Generated at 2022-06-12 22:50:41.795807
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
    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([E])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:50:47.030093
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(C): pass
    class H(D): pass
    assert get_all_subclasses(A) == {B, C, D, E, F, G, H}
    assert get_all_subclasses(B) == {D, E, H}


# Generated at 2022-06-12 22:50:50.754027
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(C): pass
    class F(D): pass
    class G(A): pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G])

# Generated at 2022-06-12 22:50:57.036746
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
    class F(D):
        pass
    class G(object):
        pass
    assert get_all_subclasses(A) == set([B, C, D, E, F])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set([E, F])
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == set()
    assert get_all_subclasses(G) == set()
    assert get_all_subclasses

# Generated at 2022-06-12 22:51:04.375540
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class C1(object): pass
    class C2(C1): pass
    class C3(object): pass
    class C4(C2): pass
    class C5(C1, C3): pass
    class C6(C4, C5): pass

    result = get_all_subclasses(C1)
    assert C6 in result
    assert C5 in result
    assert C4 in result
    assert C3 not in result
    assert C2 in result
    assert C1 not in result

    result = get_all_subclasses(C3)
    assert C6 not in result
    assert C5 in result
    assert C4 not in result
    assert C3 not in result
    assert C2 not in result
    assert C1 not in result