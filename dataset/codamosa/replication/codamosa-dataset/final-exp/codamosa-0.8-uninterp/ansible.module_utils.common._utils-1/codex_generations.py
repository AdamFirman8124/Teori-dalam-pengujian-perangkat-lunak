

# Generated at 2022-06-12 22:41:16.365261
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import Counter
    from ansible.errors import AnsibleError

    class BaseAnsibleError(AnsibleError):
        pass

    class AnsibleIOError(BaseAnsibleError):
        pass

    class AnsibleModuleError(BaseAnsibleError):
        pass

    class AnsibleAction(object):
        pass

    class AnsibleModule(AnsibleAction):
        pass

    class AnsibleActionModule(AnsibleModule):
        pass
    # Tests

    # BaseAnsibleError
    assert Counter(get_all_subclasses(BaseAnsibleError)) == Counter([
        AnsibleError, AnsibleIOError, AnsibleModuleError,
    ])

    # AnsibleAction

# Generated at 2022-06-12 22:41:28.114147
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create an inheritance tree and tests hierarchy
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
    class G(F):
        pass

    t = get_all_subclasses
    assert set(t(A)) == set([B,C,D,E,F,G])
    assert set(t(B)) == set([D,E])
    assert set(t(C)) == set([F,G])
    assert set(t(D)) == set([])
    assert set(t(E)) == set([])
    assert set(t(F)) == set([G])
    assert set(t(G)) == set([])

# Generated at 2022-06-12 22:41:35.607354
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import ansible.module_utils.six

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

    assert set(get_all_subclasses(ansible.module_utils.six.string_types)) == set([
        ansible.module_utils.six.text_type,
    ])

    assert set(get_all_subclasses(A)) == set([
        B,
        C,
        D,
        E,
    ])


# Generated at 2022-06-12 22:41:44.237895
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

    class E(A):
        pass

    assert set(get_all_subclasses(A)) == {B, C, D, E}
    assert set(get_all_subclasses(B)) == {C}
    assert set(get_all_subclasses(C)) == set()
    assert set(get_all_subclasses(D)) == set()
    assert set(get_all_subclasses(E)) == set()

    class F(C):
        pass

    class G(E):
        pass

    assert set(get_all_subclasses(A)) == {B, C, D, E, F, G}

# Generated at 2022-06-12 22:41:54.265900
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Testing for function get_all_subclasses
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

    class F(E):
        pass

    class G(object):
        pass

    class H(G):
        pass

    class I(H):
        pass

    class J(I):
        pass

    class K(J):
        pass

    class L(K):
        pass

    class M(L):
        pass

    class N(M):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:42:01.468511
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
    class F(object):
        pass
    class G(F):
        pass
    class H(object):
        pass
    class I(H):
        pass
    class J(F):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:42:11.209747
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Class configuration
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
    class F(D, E):
        pass

    # Test
    assert get_all_subclasses(A) == set([B, D, E])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([E])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:42:19.064732
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(D, B): pass

    assert set([E, D, B, C]) == get_all_subclasses(A)

    # Test all cases of multiple inheritance
    class G(E, D): pass
    class H(D, E): pass
    class I(E, D, B): pass

    assert set([G, H, I, E, D, B, C]) == get_all_subclasses(A)

    class J(object): pass
    class K(object): pass
    class L(object): pass

    assert set([]) == get_all_subclasses(J)
    assert set([]) == get_all_subclasses(K)
    assert set([]) == get_

# Generated at 2022-06-12 22:42:23.447452
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

    subclasses = get_all_subclasses(A)
    assert subclasses == set([B, C, D])

# Generated at 2022-06-12 22:42:32.142438
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

    assert get_all_subclasses(A) == set([B, C, D, E, F])
    assert get_all_subclasses(B) == set([D, E, F])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([F])
    assert get_all_subclasses(E) == set([])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:42:40.179583
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

    class F(E):
        pass

    assert E in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert F in get_all_subclasses(A)
    assert D in get_all_subclasses(B)
    assert D in get_all_subclasses(C)
    assert F not in get_all_subclasses(B)

# Generated at 2022-06-12 22:42:48.811528
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Defining a simple python class hierarchy
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
    class G(B):
        pass
    class H(D):
        pass
    class I(F):
        pass
    class J(G):
        pass

    # Testing the result
    assert get_all_subclasses(A) == {B, C, D, E, F, G, H, I, J}


# Generated at 2022-06-12 22:42:57.243210
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # definition of class
    class A(object):
        def __init__(self):
            pass
    class B(A):
        def __init__(self):
            pass
    class C(B):
        def __init__(self):
            pass
    class D(A):
        def __init__(self):
            pass
    class E(B):
        def __init__(self):
            pass
    class F(C):
        def __init__(self):
            pass
    # Test all children of class A
    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:43:02.163125
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Parent1:
        pass

    class Child1(Parent1):
        pass

    class Child2(Parent1):
        pass

    class Child3(Child1):
        pass

    class Child4(Child3):
        pass

    class Parent2:
        pass

    class Child5(Parent2):
        pass

    assert set(get_all_subclasses(Parent1)) == set([Child1, Child2, Child3, Child4])
    assert set(get_all_subclasses(Parent2)) == set([Child5])

# Generated at 2022-06-12 22:43:08.847324
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses

    :rtype: None
    :returns: nothing
    '''
    assert get_all_subclasses(TestClassA) == set([TestClassB, TestClassC, TestClassD])
    assert get_all_subclasses(object) == set([TestClassA, TestClassB, TestClassC, TestClassD, TestClassF])
    assert get_all_subclasses(TestClassF) == set()



# Generated at 2022-06-12 22:43:16.679119
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E:
        pass

    class F(E):
        pass

    class G(D, F):
        pass

    classes = get_all_subclasses(A)
    assert D in classes

    classes = get_all_subclasses(E)
    assert F in classes

    classes = get_all_subclasses(D)
    assert G in classes



# Generated at 2022-06-12 22:43:23.443492
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import OrderedDict
    from ansible.module_utils.six import iteritems

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B,C):
        pass

    class E(B,D):
        pass

    class F(object):
        pass

    class G(F):
        pass

    class H(F):
        pass

    class I(G):
        pass

    class J(I):
        pass

    class K(G,H):
        pass

    class L(K):
        pass

    class M(H):
        pass

    # test
    def assert_test_get_all_subclasses(a, b):
        if isinstance(b, list):
            assert sorted(a) == sorted

# Generated at 2022-06-12 22:43:33.094937
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test for function get_all_subclasses

    :returns: None
    '''
    # Define classes for testing
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(A):
        pass

    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([])

# Only run the test if we are run as a script, not if we are imported.
# This is because the tests fail to run if the module is imported due to
# how unittest works, and if we are imported then we are being used

# Generated at 2022-06-12 22:43:44.735627
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base:
        pass
    class A(Base):
        pass
    class B(Base):
        pass
    class BA(B):
        pass
    class BB(B):
        pass
    class BAA(BA):
        pass
    class BBB(BB):
        pass
    assert set([BA, BAA, BB, BBB]) == get_all_subclasses(A)
    assert set([BA, BAA, BB, BBB]) == get_all_subclasses(B)
    assert set([BA, BAA]) == get_all_subclasses(BA)
    assert set([BB, BBB]) == get_all_subclasses(BB)
    assert set([BAA]) == get_all_subclasses(BAA)
    assert set([BBB]) == get_all_subclasses(BBB)



# Generated at 2022-06-12 22:43:52.877898
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

    class E(D):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(C) == set([D, E])
    assert get_all_subclasses(D) == set([E])
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(object) == set([A, B, C, D, E])

# Generated at 2022-06-12 22:44:07.125943
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    from mock import Mock

    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(C): pass

    class TestA(unittest.TestCase):
        def setUp(self):
            self.a_type = type('A', (object,), {})
            self.b_type = type('B', (self.a_type,), {})
            self.c_type = type('C', (self.a_type,), {})
            self.d_type = type('D', (self.a_type,), {})
            self.e_type = type('E', (self.b_type,), {})

# Generated at 2022-06-12 22:44:11.546313
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test get_all_subclasses() function
    '''
    class TestClass():
        pass

    class TestClassSubclass(TestClass):
        pass

    class TestClassSubclassSubclass(TestClassSubclass):
        pass

    subclasses = get_all_subclasses(TestClass)
    assert TestClassSubclass in subclasses
    assert TestClassSubclassSubclass in subclasses
    assert TestClass in subclasses

# Generated at 2022-06-12 22:44:22.045407
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, A):
        pass

    class E(D):
        pass

    def check_subclasses(cls, expected_subclasses):
        subclass_names = [type(sc).__name__ for sc in get_all_subclasses(cls)]
        for ec in expected_subclasses:
            if ec not in subclass_names:
                return False
        return True

    expected_subclasses = {
        A: [B, C, D, E],
        B: [D, E],
        C: [],
        D: [E],
        E: [],
    }


# Generated at 2022-06-12 22:44:29.540649
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(B): pass
    class E(D): pass
    class F(E): pass
    assert F in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert E in get_all_subclasses(A)
    assert A not in get_all_subclasses(A)

# Generated at 2022-06-12 22:44:39.344564
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Create a simple tree of classes, get all subclasses using get_all_subclasses, and verify
    that we get back what we expect.
    '''

    class A(object):
        '''
        Class A
        '''

        def __init__(self):
            '''
            Constructor for A
            '''

        def test_method(self):
            '''
            Unit test method for A
            '''
            pass

    class B(A):
        '''
        Class B, subclass of A
        '''

        def __init__(self):
            '''
            Constructor for B
            '''

        def test_method(self):
            '''
            Unit tests method for B
            '''
            pass


# Generated at 2022-06-12 22:44:49.790786
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(C): pass
    class F(D): pass
    class G(E): pass
    class H(G): pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H])
    assert get_all_subclasses(B) == set([])
    assert get_all_subclasses(C) == set([D, E, F, G, H])
    assert get_all_subclasses(D) == set([F])
    assert get_all_subclasses(E) == set([G, H])
    assert get_all_subclasses(F) == set([])
    assert get_all_subclasses(G) == set

# Generated at 2022-06-12 22:44:53.652720
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

    class F(D):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F}

# Generated at 2022-06-12 22:45:01.805598
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(object):
        pass

    class D(A):
        pass

    class E(B, C):
        pass

    class F(D):
        pass

    class G(C):
        pass

    a_subclasses = set([B, D, E, F])
    b_subclasses = set([E])
    c_subclasses = set([E, G])
    d_subclasses = set([F])
    e_subclasses = set()
    f_subclasses = set()
    g_subclasses = set()

    assert get_all_subclasses(A) == a_subclasses
    assert get_all_subclasses(B) == b_subclasses
    assert get_all_subclasses(C) == c_

# Generated at 2022-06-12 22:45:06.627443
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
    assert get_all_subclasses(A) == set([A, B, C, D, E])

# Generated at 2022-06-12 22:45:10.716455
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    class Animal:
        pass

    class Fish(Animal):
        pass

    class Dog(Animal):
        pass

    class Mammal(Animal):
        pass

    class Cat(Mammal):
        pass

    class Tiger(Cat):
        pass

    class Abeilles(Animal):
        pass

    class HoneyBee(Abeilles):
        pass

    class KillerBee(HoneyBee):
        pass

    class Insect(Animal):
        pass

    class Ant(Insect):
        pass

    class Apidae(Insect):
        pass

    class BumbleBee(Apidae):
        pass

    class AntsWithWings(Ant):
        pass

    class AntsWithWings2(Insect):
        pass

    class AntsWithWings3(AntsWithWings):
        pass



# Generated at 2022-06-12 22:45:26.720801
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    test_get_all_subclasses
    '''

    class A(object):
        '''
        class A
        '''

    class B(A):
        '''
        class B
        '''

    class C(A):
        '''
        class C
        '''

    class D(B):
        '''
        class D
        '''

    class E(B):
        '''
        class E
        '''

    class F(C):
        '''
        class F
        '''

    class G(C):
        '''
        class G
        '''

    assert(set(get_all_subclasses(A)) == set([B, C, D, E, F, G]))

# Generated at 2022-06-12 22:45:35.502160
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

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

    class F(C):
        pass

    class G(F):
        pass

    class TestUtils(unittest.TestCase):
        def test_get_all_subclasses(self):
            class_set = get_all_subclasses(C)
            self.assertEqual(class_set, set([F, G]))

            class_set = get_all_subclasses(B)
            self.assertEqual(class_set, set([]))

            class_set = get_all_subclasses(A)

# Generated at 2022-06-12 22:45:44.250249
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(object):
        pass
    class C(A):
        pass
    class D(B):
        pass
    class E(C,D):
        pass
    class F(E):
        pass

    assert set([C, E, F, D]) == get_all_subclasses(A)
    assert set([D, F, E]) == get_all_subclasses(B)
    assert set([F, E]) == get_all_subclasses(C)
    assert set([F]) == get_all_subclasses(D)
    assert set([F]) == get_all_subclasses(E)
    assert set([]) == get_all_subclasses(F)

# Generated at 2022-06-12 22:45:54.185553
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    test_get_all_subclasses()

    The function will validate the get_all_subclasses function using an existing
    class hierarchy to be sure that get_all_subclasses returns the correct set of
    classes.

    The tests will use the following hierarchy:
    A
    +-B
      +-C
      +-D
    +-E
      +-F
      +-G
    '''
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(B):
        pass
    class E(A):
        pass
    class F(E):
        pass
    class G(E):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G])


# Generated at 2022-06-12 22:45:59.542765
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Define a classic class inheritance scenario
    class A():
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

    # Testing
    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])



# Generated at 2022-06-12 22:46:09.964696
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # This is the simple class to inherit
    class _MotherClass(object):
        pass
    # Subclasses used for test
    class _Son1(_MotherClass):
        pass
    class _Son2(_MotherClass):
        pass
    class _GrandSon1(_Son2):
        pass
    # Test if we receive all subclasses of map
    assert _MotherClass in get_all_subclasses(dict)
    assert _Son1 in get_all_subclasses(dict)
    assert _Son2 in get_all_subclasses(dict)
    assert _GrandSon1 in get_all_subclasses(dict)
    # Test if we receive all subclasses of _MotherClass
    assert _Son1 in get_all_subclasses(_MotherClass)
    assert _Son2 in get_all_subclasses(_MotherClass)
    assert _Grand

# Generated at 2022-06-12 22:46:15.420371
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TestBase(object): pass
    class TestSubclass1(TestBase): pass
    class TestSubclass2(TestBase): pass
    class TestSubclass1_1(TestSubclass1): pass
    class TestSubclass2_1(TestSubclass2): pass
    class TestSubclass3(object): pass
    assert all(x in get_all_subclasses(TestBase)
               for x in [TestSubclass1, TestSubclass2, TestSubclass1_1, TestSubclass2_1])
    assert TestSubclass3 not in get_all_subclasses(TestBase)

# Generated at 2022-06-12 22:46:22.091345
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test method for get_all_subclasses method
    :return: void
    '''
    class Parent(object):
        pass

    class Child(Parent):
        pass

    class GrandChild1(Child):
        pass

    class GrandChild2(Child):
        pass

    class GrandChild3(Child):
        pass

    class GrandChild4(Child):
        pass

    class GrandChild5(Child):
        pass

    class GrandChild11(GrandChild1):
        pass

    class GrandChild12(GrandChild1):
        pass

    class GrandChild21(GrandChild2):
        pass

    class GrandChild22(GrandChild2):
        pass

    class GrandChild23(GrandChild2):
        pass

    class GrandChild31(GrandChild3):
        pass


# Generated at 2022-06-12 22:46:31.333180
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Check that the function is working correctly.
    """
    from ansible.module_utils._text import to_bytes

    class A:
        pass

    class X(A):
        pass

    class Y(A):
        pass

    class Z(A):
        pass

    class B(X, Y):
        pass

    class C(Y, Z):
        pass

    assert get_all_subclasses(A) == set([X, Y, Z, B, C])
    assert get_all_subclasses(B) == set([])

    def to_bytes_patch(x):
        return x

    old_tb = to_bytes
    try:
        to_bytes = to_bytes_patch
        assert to_bytes('test') == 'test'
    finally:
        to_bytes = old_t

# Generated at 2022-06-12 22:46:38.041623
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        pass

    class B(A):
        pass

    class D(B):
        pass

    class C(A):
        pass

    class E(C):
        pass

    assert get_all_subclasses(A) == set([B, D, C, E])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([E])
    assert get_all_subclasses(A()) == set()
    assert get_all_subclasses(None) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:46:56.524319
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(D): pass
    class F(D): pass

    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:47:03.155404
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    # Create a test class which has multiple descendent classes
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

    # Test code
    class TestGetAllSubClasses(unittest.TestCase):
        def test_basic(self):
            r = get_all_subclasses(A)
            self.assertIn(B, r)
            self.assertIn(C, r)
            self.assertIn(D, r)
            self.assertIn(E, r)
            self.assertIn(F, r)

        def test_sub_sub_class(self):
            r = get_all_sub

# Generated at 2022-06-12 22:47:12.019689
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(A):
        pass
    class E(B):
        pass
    class F(B):
        pass
    class G(C):
        pass
    class H(G):
        pass
    # Test class without child
    assert get_all_subclasses(H) == {H}
    # Test class with one child
    assert get_all_subclasses(F) == {F}
    # Test class with multiple children
    assert get_all_subclasses(A) == {B, C, D, E, F, G, H}
    assert get_all_subclasses(C) == {C, G, H}



# Generated at 2022-06-12 22:47:18.967259
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    ''' test get_all_subclasses function '''
    class A():
        ''' class A '''
    class B(A):
        ''' class B '''
    class C(A):
        ''' class C '''
    class D(B, C):
        ''' class D '''
    class E(B):
        ''' class E '''

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:47:29.432315
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import ansible.module_utils.basic

    # Define the class to test and its subclasses
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
    class F(B, C):
        pass
    class G(B, E):
        pass
    class H(F, G):
        pass
    # Define 2 unrelated classes
    class J(object):
        pass
    class K(ansible.module_utils.basic.AnsibleModule):
        pass

    # Test if the correct subclasses of the class A are identified
    assert(get_all_subclasses(A) == set([B, C, D, E, F, G, H]))

    # Test

# Generated at 2022-06-12 22:47:38.620417
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class class_1(object):
        pass

    class class_2(class_1):
        pass

    class class_3(class_1):
        pass

    class class_4(class_2):
        pass

    class class_5(class_2):
        pass

    class class_6(object):
        pass

    assert get_all_subclasses(class_2) == {class_4, class_5}
    assert get_all_subclasses(class_1) == {class_2, class_4, class_5, class_3}


#
# python 2/3 compat
#
import sys

if sys.version_info[0] == 3:
    # Python 3
    text_type = str
    binary_type = bytes
    from io import StringIO


# Generated at 2022-06-12 22:47:42.735448
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
    assert set(get_all_subclasses(A)) == set((B, C, D, E, F))

# Generated at 2022-06-12 22:47:49.314623
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
    class E(D):
        pass
    class F(D):
        pass
    class G(B, C):
        pass
    class H(B, C, D, E, F, G):
        pass
    class I(B, D, F):
        pass
    class J(E, F, H):
        pass
    expected = {A, B, C, D, E, F, G, H, I, J}
    subclasses = get_all_subclasses(A)
    assert subclasses == expected

# Generated at 2022-06-12 22:47:54.338553
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import ansible_collections.misc

    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(ansible_collections.misc.utils.get_all_subclasses(A)):
        pass

    assert D in ansible_collections.misc.utils.get_all_subclasses(A)

# Generated at 2022-06-12 22:48:02.386819
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

    class F(object):
        pass

    class G(object):
        pass

    class H(G):
        pass

    class I(H):
        pass

    classes = set(get_all_subclasses(A))
    assert len(classes) == 3
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F not in classes
    assert G not in classes
    assert H not in classes
    assert I not in classes

    classes = set(get_all_subclasses(C))
    assert len(classes) == 2
    assert D in classes
    assert E

# Generated at 2022-06-12 22:48:39.070376
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
    class F(D):
        pass

    classes = get_all_subclasses(A)
    # Then assert the number of subclasses found
    assert len(classes) == 6
    assert A in classes
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F in classes

# Generated at 2022-06-12 22:48:47.488982
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

    class F(E):
        pass

    class G(C):
        pass

    class H(D):
        pass

    class I(G):
        pass

    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert E in get_all_subclasses(A)
    assert F in get_all_subclasses(A)
    assert G in get_all_subclasses(A)

# Generated at 2022-06-12 22:48:49.879537
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(object):
        pass

    assert get_all_subclasses(A) == {B}
    assert get_all_subclasses(C) == set()

# Generated at 2022-06-12 22:48:55.644794
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses.
    '''
    import sys

    # family tree, to test this function
    class grand_father(object):
        pass

    class father(grand_father):
        pass

    class uncle(grand_father):
        pass

    class son(father):
        pass

    class nephew(uncle):
        pass

    class grand_son(son):
        pass

    class y(father):
        pass

    class r(nephew):
        pass

    class rr(r):
        pass

    # use this function to extract all suclasses of grand_father
    subclasses = get_all_subclasses(grand_father)

    # all subclasses of grand_father

# Generated at 2022-06-12 22:49:04.560135
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Given an hierarchy of class
    class C1(object):
        pass

    class C2(object):
        pass

    class C3(object):
        pass

    class C4(C1):
        pass

    class C5(C1):
        pass

    class C6(C1):
        pass

    class C7(C4):
        pass

    class C8(C5):
        pass

    class C9(C6):
        pass

    class C10(C6):
        pass

    class C11(C9):
        pass

    class C12(C11):
        pass

    expected = set([C1, C4, C7, C5, C8, C6, C9, C11, C12, C10])
    result = get_all_subclasses(C1)



# Generated at 2022-06-12 22:49:10.268875
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Example taken from http://stackoverflow.com/questions/3862310/how-can-i-find-all-subclasses-of-a-class-given-its-name
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
    assert E in get_all_subclasses(A)
    # Example taken from http://stackoverflow.com/questions/3862310/how-can-i-find-all-subclasses-of-a-class-given-its-name
    assert set([E, D, B, C, A]) == get_all_subclasses(object)

# Generated at 2022-06-12 22:49:18.409852
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

    # Cases to test
    cases = [
        (A, {B, C, D}),
        (B, set()),
        (C, {D}),
        (D, set()),
        (E, set()),
    ]

    for (cls, expected_classes) in cases:
        # Testing classes subclasses
        subclasses = get_all_subclasses(cls)
        assert len(subclasses) == len(expected_classes)
        assert set(subclasses) == expected_classes

# Generated at 2022-06-12 22:49:26.233570
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test for function get_all_subclasses
    '''
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
    class G(object):
        pass
    class H(G):
        pass
    assert set(get_all_subclasses(A)) == set((B, C, D, E, F))
    assert set(get_all_subclasses(B)) == set((D, E, F))
    assert set(get_all_subclasses(C)) == set()
    assert set(get_all_subclasses(D)) == set((E, F))

# Generated at 2022-06-12 22:49:34.679054
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils._text import to_native

    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E:
        pass

    class F(E):
        pass

    class G(F):
        pass

    class H(A, F):
        pass

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    f = F()
    g = G()

    assert set([B, C, D, H]) == get_all_subclasses(A)
    assert set([G]) == get_all_subclasses(F)
    assert set([]) == get_all_subclasses(G)
    assert set([D]) == get

# Generated at 2022-06-12 22:49:43.369073
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Defined a few classes to test that get_all_subclasses returns all of the subclasses of all
    levels.

    '''
    # Base class to test
    class Base(object):
        pass
    # The base class has three subclasses
    class One(Base):
        pass
    class Two(Base):
        pass
    class Three(Base):
        pass
    # One class has one subclass
    class Four(Three):
        pass
    # Two class has one subclass
    class Five(Two):
        pass
    # Three class has a subclass with a subclass
    class Six(Three):
        pass
    class Seven(Six):
        pass
    # Nine and Ten subclass each other, so one should be enough
    class Eight(Nine):
        pass
    class Nine(Eight):
        pass
    # Make sure

# Generated at 2022-06-12 22:51:04.115722
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

    class H(G):
        pass

    class I(G):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I])

    class X(dict):
        pass

    class Y(dict):
        pass

    class Z(dict):
        pass

    assert get_all_subclasses(dict) == set([X, Y, Z])
    return True