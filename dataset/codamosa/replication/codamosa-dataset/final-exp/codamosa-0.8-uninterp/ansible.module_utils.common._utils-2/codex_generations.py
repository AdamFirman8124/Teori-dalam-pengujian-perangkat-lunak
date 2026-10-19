

# Generated at 2022-06-12 22:41:08.544332
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
    assert set(get_all_subclasses(A)) == set([B, C, D])


# Generated at 2022-06-12 22:41:18.799204
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test the get_all_subclasses function
    '''
    class O(object):
        pass
    class A(O):
        pass
    class B(O):
        pass
    class C(A):
        pass
    class D(C):
        pass
    class E(C):
        pass

    assert set(get_all_subclasses(O)) == {A, C, D, E, B}
    assert set(get_all_subclasses(A)) == {C, D, E}
    assert set(get_all_subclasses(B)) == set()
    assert set(get_all_subclasses(C)) == {D, E}
    assert set(get_all_subclasses(D)) == set()
    assert set(get_all_subclasses(E)) == set()




# Generated at 2022-06-12 22:41:28.213192
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Animal(object):
        pass

    class Flyable(object):
        pass

    class Bird(Animal, Flyable):
        pass

    class Fish(Animal):
        pass

    class Mammal(Animal):
        pass

    class Dog(Mammal):
        pass

    class Bat(Mammal, Flyable):
        pass

    result = get_all_subclasses(Animal)
    assert len(result) == 6
    assert Bird in result
    assert Fish in result
    assert Mammal in result
    assert Dog in result
    assert Bat in result
    assert Flyable in result


# Generated at 2022-06-12 22:41:39.273945
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Simple unit test to check get_all_subclasses function

    The test is performed by creating a class hierarchy and checking
    that the function returns all expected classes in the hierarchy.
    '''
    # Create class hierarchy
    parent_class = object
    class_c = type('class_c', (parent_class,), {})
    class_d = type('class_d', (parent_class,), {})
    parent_class = type('parent_class', (class_c, class_d), {})
    class_a = type('class_a', (parent_class,), {})
    class_b = type('class_b', (parent_class,), {})
    # Retrieve all classes without class_c, class_d and parent_class
    expected_set = set([class_a, class_b])


# Generated at 2022-06-12 22:41:47.849495
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This function tests the get_all_subclasses function.
    '''
    import types
    import sys

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

    class F(E):
        pass

    class G(F):
        pass

    assert get_all_subclasses(A) == {B, C, D}
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(types.ModuleType) == {sys.modules['ansible_test'], sys.modules['ansible.module_utils._text']}

# Unit testing is performed using the Python unittest module

# Generated at 2022-06-12 22:41:57.021240
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

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

    class G(E):
        pass

    class H(F):
        pass

    class I(F):
        pass

    class J(G):
        pass

    class K(F, G):
        pass

    # Test of commons cases
    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert C in get_all_subclasses(B)

# Generated at 2022-06-12 22:41:59.812972
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    assert set([int]) == get_all_subclasses(int)
    assert set([long, int]) == get_all_s

# Generated at 2022-06-12 22:42:04.076601
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
    class F(E):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])



# Generated at 2022-06-12 22:42:15.547207
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a simple class hierarchy
    class Parent(object):
        pass

    class Child(Parent):
        pass

    class Grandchild(Child):
        pass

    class GreatGrandchild(Grandchild):
        pass

    # Create another class with no subclasses
    class Grandparent(object):
        pass

    # Create a hierarchy of three levels
    class GParent(object):
        pass

    class GParentChild(GParent):
        pass

    class GParentGreatGrandchild(GParentChild):
        pass

    # Create hierarchy of four levels
    class GGParent(object):
        pass

    class GGParentChild(GGParent):
        pass

    class GGParentGrandchild(GGParentChild):
        pass

    class GGParentGreatGrandchild(GGParentGrandchild):
        pass

    # Run unit test

# Generated at 2022-06-12 22:42:26.020535
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit tests fot function get_all_subclasses
    '''

    class A(object):
        '''
        The top-level class
        '''

        pass

    class B(A):
        '''
        Class B is a subclass of class A
        '''

        pass

    class C(A):
        '''
        Class C is a subclass of class A
        '''

        pass

    class D(B):
        '''
        Class D is a subclass of class B
        '''

        pass

    class E(D):
        '''
        Class E is a subclass of class D
        '''

        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E])

# Generated at 2022-06-12 22:42:37.394331
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): # class A is a subclass of object
        pass

    class B(object): # class B is a subclass of object
        pass

    class C(A): # class C is a subclass of A
        pass

    class D(B): # class D is a subclass of B
        pass

    class E(C): # class E is a subclass of C
        pass

    class F(C): # class F is a subclass of C
        pass

    # A should be in the set of parent classes of all of its subclasses
    assert A in get_all_subclasses(C)
    assert A in get_all_subclasses(D)
    assert A in get_all_subclasses(E)
    assert A in get_all_subclasses(F)

    # Object should be found in the set of all ancestors of C, D,

# Generated at 2022-06-12 22:42:48.029908
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class B(A):
        pass

    class C(A):
        pass

    class D(A):
        pass

    class E(D):
        pass

    class F(A):
        pass

    x = D("x")
    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:42:54.772453
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass
    class C(A):
        pass

    class D:
        pass

    class E(B, C, D):
        pass

    class F(E):
        pass

    assert get_all_subclasses(A) == set([B, C, E, F])
    assert get_all_subclasses(D) == set([E, F])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:43:01.297861
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a class
    class A:
        pass

    # Define its direct subclasses
    class B(A):
        pass

    class C(A):
        pass

    class D(A):
        pass

    # Define its subclasses
    class E(C):
        pass

    class F(D):
        pass

    class G(F):
        pass

    subclasses = get_all_subclasses(A)
    assert A in subclasses
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses
    assert G in subclasses

# Generated at 2022-06-12 22:43:10.260229
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

    assert get_all_subclasses(A) == {B, C, D, E}
    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(C) == {D, E}
    assert get_all_subclasses(D) == {E}
    assert get_all_subclasses(E) == set()

    assert get_all_subclasses(A) == set(B.mro()) - set(B.mro()[0:B.mro().index(A)])

# Generated at 2022-06-12 22:43:16.025511
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    test_get_all_subclasses function
    '''
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
    class G(E):
        pass
    print(get_all_subclasses(A))

# Generated at 2022-06-12 22:43:18.836356
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    assert get_all_subclasses(A) == {B, C, D}

# Generated at 2022-06-12 22:43:29.827807
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Verify that the get_all_subclasses function works correctly.

    This is a test function for the get_all_subclasses function.
    '''

    import base64
    import copy

    class TestClass(object):
        pass

    class TestClass1(TestClass):
        pass

    class TestClass2(TestClass1):
        pass

    class TestClass3(TestClass1):
        pass

    class TestClass4(TestClass1):
        pass

    class TestClass5(TestClass3):
        pass

    class TestClass6(TestClass5):
        pass

    expected = {TestClass2, TestClass3, TestClass5, TestClass6}

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest


# Generated at 2022-06-12 22:43:35.623668
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Assert that the function returns a set
    assert(isinstance(get_all_subclasses(object), set))
    # Assert that the function returns the correct set.  See the docstring of get_all_subclasses
    # for a diagram of the classes used in this test.
    assert(get_all_subclasses(object) == set([type, bool, int, float, complex, str, tuple,
                                              dict, set, list, frozenset, file,
                                              SuperSubClass1]))

# Example classes to use in the test_get_all_subclasses unittest

# Generated at 2022-06-12 22:43:40.114467
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)

# Generated at 2022-06-12 22:43:50.474273
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

    class F(B):
        pass

    class G(E):
        pass

    assert set(get_all_subclasses(A)) == set((B, C, D, E, F, G))

# Generated at 2022-06-12 22:43:53.582765
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''Function to test get_all_subclasses'''

    class a(object):
        '''Class a'''
        pass

    class b(a):
        '''Class b'''
        pass

    class c(a):
        '''Class c'''
        pass

    class d(b, c):
        '''Class d'''
        pass

    assert get_all_subclasses(a) == {b, c, d}

# Generated at 2022-06-12 22:44:01.783022
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class foo(object): pass
    class boo(object): pass
    class zoo(foo): pass
    class wii(zoo): pass
    assert sorted(get_all_subclasses(foo)) == [boo, zoo, wii]
    assert sorted(get_all_subclasses(boo)) == []
    assert sorted(get_all_subclasses(zoo)) == [wii]
    assert sorted(get_all_subclasses(wii)) == []

# Generated at 2022-06-12 22:44:06.476839
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Ensure that get_all_subclasses is working as expected
    '''

    class dummy_class(object):
        '''
        Dummy class to use for unit test
        '''
        pass

    class dummy_subclass1(dummy_class):
        '''
        Dummy subclass to use for unit test
        '''
        pass

    class dummy_subclass2(dummy_class):
        '''
        Dummy subclass to use for unit test
        '''
        pass

    class dummy_subsubclass1(dummy_subclass1):
        '''
        Dummy subclass to use for unit test
        '''
        pass

    class dummy_subsubclass2(dummy_subclass2):
        '''
        Dummy subclass to use for unit test
        '''
        pass

   

# Generated at 2022-06-12 22:44:14.855437
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    test get_subclasses_recursive
    """
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
    class G(F, object):
        pass

    assert C in get_all_subclasses(A)
    assert D not in get_all_subclasses(C)
    assert G in get_all_subclasses(A) and G in get_all_subclasses(B)  # D and C are in G
    assert G in get_all_subclasses(C) and G in get_all_subclasses(D)  # F is in G

# Generated at 2022-06-12 22:44:23.017833
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

    class F:
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set([E])
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:44:27.353106
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.utils.module_docs_fragments import POSIX_COMMON_ARGUMENTS
    all_classes = get_all_subclasses(POSIX_COMMON_ARGUMENTS)
    assert any('module_utils.basic' in c.__module__ for c in all_classes)


# Generated at 2022-06-12 22:44:34.954433
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

    class F(object):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(D) == set([E])
    assert get_all_subclasses(F) == set()

# Unit test import of get_all_subclasses

# Generated at 2022-06-12 22:44:38.983036
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

    assert get_all_subclasses(A) == {B, C, D, E, F}
    assert get_all_subclasses(B) == {D, E}
    assert get_all_subclasses(C) == {F}
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:44:49.426152
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

    class E(object):
        pass

    class F(E):
        pass

    classes = get_all_subclasses(A)
    assert B in classes
    assert C in classes
    assert D in classes
    assert E not in classes
    assert F not in classes


# In python3.3 and above, unittest provides a module-level function that takes a dictionary of name to
# callables and returns a suite of tests.  However, we're trying to be compatible with python2.6 as well.
# The following is a backport from python3.5.1
import unittest

# Generated at 2022-06-12 22:45:02.269268
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

    assert(set(get_all_subclasses(A)) == set([B, C, D, E, F]))

# Generated at 2022-06-12 22:45:09.231543
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types
    import sys

    # All here are subclasses of object and type but not of string
    assert get_all_subclasses(object) == set(sys.modules[__name__].__dict__.values()) - set([str])
    assert get_all_subclasses(type) == set(sys.modules[__name__].__dict__.values()) - set([str])

    # All here are subclasses of types.ModuleType
    assert get_all_subclasses(types.ModuleType) == set(sys.modules[__name__].__dict__.values())

# Generated at 2022-06-12 22:45:18.707088
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    The following is the visualization of the graph that is produced by classA, classB and classC
    in this test

    .. code-block:: none

        classA
        /    \
    classB  classC
    /    \
    classE classF
    /        \
    classG    classH
    '''
    class classA(object):
        pass

    class classB(classA):
        pass

    class classC(classA):
        pass

    class classE(classB):
        pass

    class classF(classB):
        pass

    class classG(classE):
        pass

    class classH(classF):
        pass

    classA_ans = {classB, classC, classE, classG, classF, classH}

# Generated at 2022-06-12 22:45:21.212055
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

    assert get_all_subclasses(A) == set([B, C, D, E, F, G])

# Generated at 2022-06-12 22:45:29.660604
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test get_all_subclasses
    '''
    import collections

    class BaseClass(object):
        pass

    class ClassA(BaseClass):
        pass

    class ClassB(BaseClass):
        pass

    class ClassC(ClassA):
        pass

    class ClassD(ClassB):
        pass

    class ClassE(ClassC):
        pass

    class ClassF(ClassD):
        pass

    subclasses = get_all_subclasses(BaseClass)
    result = collections.OrderedDict()
    for x in sorted(list(subclasses)):
        result[x.__name__] = sorted(list(x.__bases__))


# Generated at 2022-06-12 22:45:33.903066
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Parent(object):
        pass

    class Child1(Parent):
        pass

    class Child2(Parent):
        pass

    class Child3(Child1):
        pass

    class Child4(Child3):
        pass

    assert get_all_subclasses(Parent) == set([Child1, Child2, Child3, Child4])

# Generated at 2022-06-12 22:45:43.792327
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(C): pass
    class F(D): pass
    class G(D): pass
    class H(F): pass
    class I(F): pass
    assert get_all_subclasses(A) == {B, C, D, E, F, G, H, I}
    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(C) == {D, E, F, G, H, I}
    assert get_all_subclasses(D) == {F, G, H, I}
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == {H, I}
   

# Generated at 2022-06-12 22:45:51.977218
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class B(object):
        pass
    class C(object):
        pass
    class A(object):
        pass
    class D(A):
        pass
    class E(B,C):
        pass
    class F(E):
        pass
    assert get_all_subclasses(A) == set([D])
    assert get_all_subclasses(B) == set([E,F])
    assert get_all_subclasses(C) == set([E,F])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([F])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:46:02.590621
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E(C): pass
    class A2(object): pass
    class A2_A(A2): pass
    class A2_A_A(A2_A): pass
    class A2_A_B(A2_A): pass
    class A2_B(A2): pass
    class A2_B_A(A2_B): pass
    class A2_B_B(A2_B): pass

    class TestUtils(unittest.TestCase):
        def testGetAllSubclasses(self):
            self.assertEqual(set(), get_all_subclasses(A))

# Generated at 2022-06-12 22:46:10.627105
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # This is a test example, in your code should be replaced by your own
    # classes
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

    assert get_all_subclasses(A) == {B, C, D, E}
    assert get_all_subclasses(B) == {D}
    assert get_all_subclasses(C) == {E}
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:46:37.845914
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TopLevel(object):
        def __init__(self):
            pass

    class FirstLevelOne(TopLevel):
        def __init__(self):
            pass

    class FirstLevelTwo(TopLevel):
        def __init__(self):
            pass

    class SecondLevelOne(FirstLevelOne):
        def __init__(self):
            pass

    class SecondLevelTwo(FirstLevelTwo):
        def __init__(self):
            pass

    class ThirdLevelOne(SecondLevelOne):
        def __init__(self):
            pass

    class ThirdLevelTwo(SecondLevelTwo):
        def __init__(self):
            pass

    class ThirdLevelThree(SecondLevelTwo):
        def __init__(self):
            pass


# Generated at 2022-06-12 22:46:44.661658
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    subclasses = []
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(C): pass
    class G(D): pass
    class H(E): pass
    class I(F): pass
    class J(F): pass
    class K(G): pass
    class L(G): pass
    subclasses = get_all_subclasses(A)
    assert B in subclasses and C in subclasses and D in subclasses
    assert E in subclasses and F in subclasses and G in subclasses
    assert H in subclasses and I in subclasses and J in subclasses
    assert K in subclasses and L in subclasses

# Generated at 2022-06-12 22:46:49.900603
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Declare some base classes
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
    class F(B):
        pass
    class G(F):
        pass

    # Check the number of class and the number of descendants of B
    classes = {"A" : 0, "B" : 7, "C" : 3, "D" : 1, "E" : 1, "F" : 2, "G" : 1}
    for name in classes.keys():
        class_name = globals()[name]
        nb_class = classes[name]
        # Check number of class

# Generated at 2022-06-12 22:46:56.938196
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class C1(object):
        pass

    class C2(C1):
        pass

    class C3(C2):
        pass

    class A(object):
        pass

    class B(A):
        pass

    class C(object):
        pass

    assert set(get_all_subclasses(C1)) == set([C2, C3])
    assert set(get_all_subclasses(A)) == set([B])
    assert set(get_all_subclasses(C)) == set([])



# Generated at 2022-06-12 22:47:06.335313
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Declaring class A, B, C, D, E and F with some relations
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

    # Here is the tree of class inheritance
    # A              ->  B
    # |               `->  D
    # `->  C
    #     |
    #     `->  E
    #         `->  F

    assert get_all_subclasses(A) == set([B, D, C, E, F])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([E, F])
    assert get

# Generated at 2022-06-12 22:47:09.353841
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Parent:
        pass

    class Child(Parent):
        pass

    assert Child in get_all_subclasses(Parent)

    class Grandchild(Child):
        pass

    assert Grandchild in get_all_subclasses(Parent)



# Generated at 2022-06-12 22:47:13.286443
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B1(A): pass
    class B2(A): pass
    class C1(B1): pass
    class C2(B1): pass
    class D1(C1): pass

    assert(get_all_subclasses(A) == {B1, B2, C1, C2, D1})



# Generated at 2022-06-12 22:47:20.961565
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class Base(object):
        pass

    class Base2(Base):
        pass

    class Base3(Base):
        pass

    class Child1(Base):
        pass

    class Child2(Base):
        pass

    class Child3(Base2):
        pass

    class Child4(Base2):
        pass

    class GrandChild1(Child1):
        pass

    class GrandChild2(Child1):
        pass

    class GrandChild3(Child2):
        pass

    class GrandChild4(Child2):
        pass

    class GrandChild5(Child3):
        pass

    class GrandChild6(Child3):
        pass

    class GrandChild7(Child4):
        pass

    class GrandChild8(Child4):
        pass
    assert GrandChild8 in get_all_subclasses(Base)
   

# Generated at 2022-06-12 22:47:27.887635
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''Test case for function get_all_subclasses'''
    # Pragma: no cover -- Does not execute when running this module as a script.
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    class E(B, D):
        pass

    class F(D):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:47:33.065805
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
    class E(B):
        pass
    class F(D):
        pass
    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:48:13.252943
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

    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:48:19.867154
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

    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:48:23.069510
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(D): pass
    class F(E): pass
    class G(F): pass
    class H(F): pass
    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses
    assert G in subclasses
    assert H in subclasses

# Generated at 2022-06-12 22:48:30.745720
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a class hierarchy
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
    class G(C):
        pass
    class H(F):
        pass
    class I(G):
        pass
    class J(G):
        pass
    class K(J):
        pass
    class L(K):
        pass
    class M(J):
        pass
    class N(J):
        pass
    class O(N):
        pass
    class P(J):
        pass
    class Q(J):
        pass
    class R(J):
        pass
    class S(R):
        pass

# Generated at 2022-06-12 22:48:37.278456
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
    class G(D):
        pass
    class H(E):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H])
    assert set(get_all_subclasses(D)) == set([G])
    assert set(get_all_subclasses(F)) == set([])

# Generated at 2022-06-12 22:48:44.618193
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

    assert get_all_subclasses(A) == set([C, D, F])
    assert get_all_subclasses(B) == set([E, F])
    assert get_all_subclasses(C) == set([F])
    assert get_all_subclasses(D) == set([F])
    assert get_all_subclasses(E) == set([F])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:48:51.885170
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Creating a test class to use
    class Test:
        pass

    # Creating three subclasses of Test
    class Test1(Test):
        pass

    class Test2(Test1):
        pass

    class Test3(Test2):
        pass

    # Creating class which won't be in the resu Its
    # only subclass should be Test2
    class Test4:
        pass

    class Test5(Test4):
        pass

    assert set(get_all_subclasses(Test)) == set([Test1,Test2, Test3])

    # Adding a class which is not a subclass of Test
    Test6 = float

    assert set(get_all_subclasses(Test)) == set([Test1,Test2, Test3])
    # Adding a class which is not a subclass of Test but with subclasses
    Test7 = int


# Generated at 2022-06-12 22:48:55.100726
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(B): pass
    class E(D): pass
    assert set(get_all_subclasses(A)) == {B, C, D, E}

# Generated at 2022-06-12 22:49:00.071545
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test function `get_all_subclasses`
    '''
    class A(object):
        pass

    @add_metaclass(A)
    class B(object):
        pass

    class C(B):
        pass

    class D(C):
        pass

    class E(object):
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

    # The return should be ordered
    assert list(get_all_subclasses(A)) == [B, C, D]

# Generated at 2022-06-12 22:49:05.374220
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

    class F(D, E):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F])
    assert get_all_subclasses(D) == set([F])

# Generated at 2022-06-12 22:50:43.733888
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a fake class
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

    class G(object):
        pass

    class H(G):
        pass

    assert(set(get_all_subclasses(A)) == set([B, D, C, E]))
    assert(set(get_all_subclasses(G)) == set([H]))

# Generated at 2022-06-12 22:50:51.742383
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types
    from ansible.module_utils._text import to_bytes

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

    class G(D):
        pass

    class H(G):
        pass

    class I(H):
        pass

    class J(A):
        pass

    # test if an object is a class
    def is_class(obj):
        return isinstance(obj, types.TypeType)

    # assert if subclass, and not equal to base
    all_subs = get_all_subclasses(A)

# Generated at 2022-06-12 22:50:55.006813
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

    class F(E):
        pass

    class G(B, D, F):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G])

# Generated at 2022-06-12 22:51:03.390845
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
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

    class G(C, D):
        pass

    class H(E):
        pass

    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert E in get_all_subclasses(A)
    assert F in get_all_subclasses(A)
    assert G in get_all_subclasses(A)
    assert H in get_all_subclasses(A)