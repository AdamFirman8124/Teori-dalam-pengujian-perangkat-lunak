

# Generated at 2022-06-12 22:41:04.078374
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

    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:41:15.353014
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define some classes
    class A(object):
        pass
    class B(object):
        pass
    class C(object):
        pass
    class D(A):
        pass
    class E(A):
        pass
    class F(C):
        pass
    class G(C):
        pass
    class H(G):
        pass
    # Get subclasses of A
    list_A = get_all_subclasses(A)
    assert D in list_A
    assert E in list_A
    assert B not in list_A
    assert F not in list_A
    assert H not in list_A
    assert len(list_A) == 2
    # Get subclasses of C
    list_C = get_all_subclasses(C)
    assert D not in list_C
    assert E

# Generated at 2022-06-12 22:41:26.976252
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

    class F(E):
        pass

    # Class A has 2 direct subclasses: B, C
    assert set(A.__subclasses__()) == set((B, C))
    # Class A has 4 direct subclasses: D, E, B, C
    assert set(get_all_subclasses(A)) == set((D, E, B, C))
    # Class C has 1 direct subclasses: E
    assert set(C.__subclasses__()) == set((E,))
    # Class C has 2 direct subclasses: E, F
    assert set(get_all_subclasses(C)) == set((E, F))



# Generated at 2022-06-12 22:41:32.674438
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

    # The expected result
    result = {B, C, D, E}
    # Call the function
    result_func = set(get_all_subclasses(A))
    # Check that both are equal
    assert result == result_func

# Generated at 2022-06-12 22:41:36.564130
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

    class E(B):
        pass

    class F(D, E):
        pass
    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:41:43.744088
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
    # The result should be a set of B, C, D
    res = get_all_subclasses(A)
    assert(B in res)
    assert(C in res)
    assert(D in res)
    # Test the fact that E is not a subclass of A
    assert(E not in res)
    # Test the fact that E has no subclass
    res = get_all_subclasses(E)
    assert(not res)

# Generated at 2022-06-12 22:41:54.223834
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

    class F(object):
        pass

    class G(F):
        pass

    all_subclasses = list(get_all_subclasses(A))
    assert B in all_subclasses, 'B is not in direct subclasses of A'
    assert C in all_subclasses, 'C is not in direct subclasses of A'
    assert D in all_subclasses, 'D is not in direct subclasses of A'
    assert E in all_subclasses, 'E is not in direct subclasses of A'
    assert F not in all_subclasses, 'F is not in direct subclasses of A'

# Generated at 2022-06-12 22:42:01.440739
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

    classes = [A, B, C, D, E]
    assert set(classes) == set(A.__subclasses__())
    assert set(classes) == set(get_all_subclasses(A))
    assert set([B, D, E]) == set(B.__subclasses__())
    assert set([B, D, E]) == set(get_all_subclasses(B))
    assert set() == set(C.__subclasses__())
    assert set() == set(get_all_subclasses(C))
    assert set([E]) == set(D.__subclasses__())

# Generated at 2022-06-12 22:42:04.710564
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
    class F(E):
        pass
    class G(F):
        pass

    # classes A, B, C, D, E, F, G are all subclasses of A
    assert get_all_subclasses(A) == {A, B, C, D, E, F, G}

    # class A is not subclass of A
    assert A not in get_all_subclasses(A)

# Generated at 2022-06-12 22:42:12.207161
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def get_class_name(cls):
        return cls.__name__

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    assert set(get_all_subclasses(A)) == {B, C, D}
    assert set(map(get_class_name, get_all_subclasses(A))) == {'B', 'C', 'D'}

# Generated at 2022-06-12 22:42:20.883596
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    # Testing class
    class ClassA(object):
        pass
    class ClassB(object):
        pass
    class ClassC1(ClassA):
        pass
    class ClassC2(ClassA):
        pass
    class ClassD(ClassC1):
        pass
    class ClassE(ClassC2):
        pass

    # Testing result
    class_a = set([ClassA])
    class_b = set([ClassB])
    class_c = set([ClassC1, ClassC2])
    class_d = set([ClassD])
    class_e = set([ClassE])


# Generated at 2022-06-12 22:42:31.210628
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    A function that tests the get_all_subclasses function.  This function creates a class
    hierarchy and then asserts that get_all_subclasses works correctly.

    The class hierarchy is as follows:
        Foo
        |
        +-- Bar
        +-- BarException
             |
             +-- BazException
             +-- Baz
                  |
                  +-- Biz

    The function creates a class Foo.  It then creates the classes Bar and BarException that
    are subclasses of Foo.  It next creates the classes BazException and Baz that are subclasses
    of BarException and Baz respectively.  Finally, it creates the class Biz that is a subclass
    of Baz.

    The function then asserts that get_all_subclasses finds all of the classes created.
    '''
    class Foo():
        pass


# Generated at 2022-06-12 22:42:37.093821
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a tree of classes
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
    class H(G):
        pass
    # Check the result
    assert get_all_subclasses(A) == {B, C, D, E, F, G, H}

# Generated at 2022-06-12 22:42:46.285252
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

    class F(A):
        pass

    class G(F):
        pass

    # Test a straight line
    assert get_all_subclasses(A) == set([B, C, D, E, F, G])
    # Test a branch and leaf
    assert get_all_subclasses(A) == set([B, C, D, E, F, G])
    # Test a leaf
    assert get_all_subclasses(G) == set()


#=============================================================


# Generated at 2022-06-12 22:42:50.183890
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define class structure
    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    class F(A, B):
        pass
    class G(B, C):
        pass
    class H(C, F):
        pass
    class K(G, H):
        pass

    all_subclasses_of_A = get_all_subclasses(A)
    all_subclasses_of_B = get_all_subclasses(B)
    all_subclasses_of_C = get_all_subclasses(C)
    all_subclasses_of_F = get_all_subclasses(F)
    all_subclasses_of_G = get_all_subclasses(G)
    all_subclasses_of_H = get_all_subclasses

# Generated at 2022-06-12 22:42:59.943779
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Test1():
        pass
    class Test2():
        pass
    class Test3():
        pass
    class Test4(Test1):
        pass
    class Test5(Test2):
        pass
    class Test6(Test4):
        pass
    class Test7(Test4):
        pass
    class Empty():
        pass
    for t in [Test1, Test2, Test3, Test4, Test5, Test6, Test7]:
        assert t in get_all_subclasses(object)
    assert Empty not in get_all_subclasses(object)
    assert Test7 not in get_all_subclasses(Test2)
    assert Test6 in get_all_subclasses(Test1)
    assert Test6 not in get_all_subclasses(Test2)
    assert Test6 in get_all_sub

# Generated at 2022-06-12 22:43:07.758417
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
    class E:
        pass
    class F(E):
        pass
    class G(E):
        pass
    class H(F):
        pass

    assert set(get_all_subclasses(A)) == {B, C, D}
    assert set(get_all_subclasses(C)) == set()
    assert set(get_all_subclasses(E)) == {F, G, H}



# Generated at 2022-06-12 22:43:18.713889
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This tests the get_all_subclasses function used in the ansible cli tool.
    '''

    class Base(object):
        '''
        This is the base class
        '''
        pass

    class Base2(object):
        '''
        This is another base class
        '''
        pass

    class A(Base):
        '''
        This is a subclass of Base
        '''
        pass

    class B1(Base):
        '''
        This is one subclass of Base
        '''
        pass

    class B2(Base):
        '''
        This is another subclass of Base
        '''
        pass

    class C1(B1):
        '''
        This is a subclass of B1
        '''
        pass


# Generated at 2022-06-12 22:43:22.692650
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

    class F(D):
        pass

    class G(D):
        pass

    classes = get_all_subclasses(A)
    assert all(x in classes for x in [B, C, D, E, F, G])
    assert len(classes) == 6

# Generated at 2022-06-12 22:43:32.772686
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base(object):
        pass
    class SubA(Base):
        pass
    class SubB(Base):
        pass
    class SubSubA(SubA):
        pass
    class SubSubB(SubB):
        pass
    class SubSubSubB(SubSubB):
        pass
    class SubSubSubSubc(SubSubSubB):
        pass

    assert set([SubA,SubB,SubSubA,SubSubB,SubSubSubB,SubSubSubSubc]) == get_all_subclasses(Base)
    assert get_all_subclasses(SubA) == set([SubSubA])
    assert get_all_subclasses(SubB) == set([SubSubB,SubSubSubB,SubSubSubSubc])

# Generated at 2022-06-12 22:43:44.643465
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Base class
    class A(object):
        pass

    # Child class
    class B(A):
        pass

    # Grand-child class
    class C(B):
        pass

    # Second grand-child class
    class D(B):
        pass

    # Third grand-child class
    class E(A):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(B) == set([C, D])

# Generated at 2022-06-12 22:43:51.690774
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
    class F:
        pass
    class G(F):
        pass
    class H(F):
        pass
    class I(H):
        pass
    assert set(get_all_subclasses(A)) == set([B, C, D, E])
    assert set(get_all_subclasses(F)) == set([G, H, I])

# Generated at 2022-06-12 22:44:02.799258
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

    class H(object):
        pass

    results = get_all_subclasses(object)
    assert len(results) == 6
    assert A in results
    assert B in results
    assert C in results
    assert D in results
    assert E in results
    assert F in results
    assert G not in results
    assert H not in results

    results = get_all_subclasses(A)
    assert len(results) == 3
    assert B in results
    assert C in results
    assert D in results
    assert E not in results


# Generated at 2022-06-12 22:44:06.645588
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

    subclasses = get_all_subclasses(A)

    assert B in subclasses
    assert C in subclasses
    assert D in subclasses

# Generated at 2022-06-12 22:44:15.415094
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Some basic classes
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

    # A list of classes to test
    test_classes = [
        A,
        B,
        C,
        D,
        E,
        F
    ]

    # A list of expected class sets
    expected = [
        [B, C, D, E, F],
        [],
        [D, E, F],
        [],
        [F],
        []
    ]

    # Test on each class
    for index, cls in enumerate(test_classes):
        assert get_all_subclasses(cls) == set

# Generated at 2022-06-12 22:44:19.761583
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

    assert set([B, D, E]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:44:26.226322
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Mock class
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(B,D): pass
    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([E])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set([E])
    assert get_all_subclasses(E) == set([])
    # Mock module
    import os
    import types
    TestModule = types.ModuleType('TestModule')
    TestModuleA = types.ModuleType('TestModuleA')
    TestModuleB = types.ModuleType('TestModuleB')
    TestModuleC = types.Module

# Generated at 2022-06-12 22:44:32.795786
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Create class data
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

    assert set(get_all_subclasses(A)) == set([B, D, E, F, G, C])

# Generated at 2022-06-12 22:44:35.227884
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Parent(object): pass
    class Child(Parent): pass
    class GrandChild(Child): pass
    assert set(get_all_subclasses(Parent)) == set([Child, GrandChild])

# Generated at 2022-06-12 22:44:39.231542
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(D): pass
    class H(D): pass
    assert get_all_subclasses(A) == set([B, C, D, E, F, H])



# Generated at 2022-06-12 22:44:49.044739
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
    assert set(get_all_subclasses(A)) == set((B, C, D, E))

# Generated at 2022-06-12 22:44:57.683664
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest2 as unittest
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
    class F(A):
        pass
    class G(F):
        pass

    class TestGetAllSubclasses(unittest.TestCase):
        def test_get_all_subclasses(self):
            # subclasses(A) == set([B, F, G, E, D, C])
            self.assertEqual(
                set([B, F, G, E, D, C]),
                get_all_subclasses(A)
            )

    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetAllSubclasses)
    unitt

# Generated at 2022-06-12 22:45:04.417625
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    :name: test_get_all_subclasses
    :description: test code for function get_all_subclasses
    :type: unit test

    This is a unit test for :py:func:`_utils.get_all_subclasses`
    '''
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

    class F(C):
        pass

    class G(F):
        pass

    class H(A):
        pass

    class I(F):
        pass

    assert set([B, C, D, F, G, H]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:45:12.108915
# Unit test for function get_all_subclasses

# Generated at 2022-06-12 22:45:22.792934
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    import inspect

    # Defining classes for testing purpose
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E(D):
        pass

    assert D == A.__subclasses__()[0]
    assert E == A.__subclasses__()[0].__subclasses__()[0]
    assert set([B, C, D, E]) == set(get_all_subclasses(A))

    class TestSubclassFinder(unittest.TestCase):
        def test_get_all_subclasses(self):
            assert set([B, C, D, E]) == set(get_all_subclasses(A))

    unittest.main()

# Generated at 2022-06-12 22:45:28.825809
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(D): pass

    # All classes should return their __subclasses__
    for cls in (A, B, C, D, E):
        assert set(cls.__subclasses__()) == set(get_all_subclasses(cls))

    # All children classes of A
    scls = get_all_subclasses(A)
    assert set(scls) == set((B, C, D, E))

# Generated at 2022-06-12 22:45:34.073852
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
    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses

# Generated at 2022-06-12 22:45:42.044550
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # First create the classes
    class Foo(object):
        pass

    class Bar(Foo):
        pass

    class Baz(Bar):
        pass

    class Hello(Foo):
        pass

    class World(Hello):
        pass

    # Then check the results
    assert set(get_all_subclasses(Foo)) == set((Bar,Baz,Hello,World))
    assert set(get_all_subclasses(Hello)) == set((World,))
    assert set(get_all_subclasses(World)) == set()
    assert set(get_all_subclasses(Baz)) == set()

# Generated at 2022-06-12 22:45:48.749182
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import collections

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
    class F(D):
        pass
    class G(C):
        pass
    class H(F):
        pass
    class K(E):
        pass
    class M(K):
        pass

    assert set(get_all_subclasses(collections.Mapping)) == set([collections.OrderedDict, collections.defaultdict, collections.ChainMap, collections.Counter, collections.UserDict])
    assert set(get_all_subclasses(A)) == set([C, G, B])

# Generated at 2022-06-12 22:45:58.833653
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Example class hierarchy
    #     A
    #   / | \
    #  B  C  F
    #  |  |  |
    #  |  D  |
    #  |  |  |
    #  |  E  |
    #   \ | /
    #     G
    #
    # A subclass of object is always present and tested here for compatibility
    # purpose

    class Object(object):
        pass

    class A(Object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(D):
        pass

    class F(A):
        pass

    class G(B, E, F):
        pass

    # Manually checking to be able to check the test and build the reference
   

# Generated at 2022-06-12 22:46:13.711147
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import Iterable
    from ansible.module_utils._text import to_text
    class A(object):
        def __init__(self):
            pass
    class B(A):
        def __init__(self):
            pass
    class C(A):
        def __init__(self):
            pass
    class D(C):
        def __init__(self):
            pass
    class E(D, B):
        def __init__(self):
            pass
    class F(E):
        def __init__(self):
            pass
    # Test output type
    subclasses = get_all_subclasses(A)
    assert isinstance(subclasses, Iterable)
    # Test output size
    expected = {B, C, D, E, F}

# Generated at 2022-06-12 22:46:21.523382
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for `get_all_subclasses` function
    '''
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

    class G(E):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F, G}
    assert get_all_subclasses(B) == {D, F}
    assert get_all_subclasses(C) == {E, G}
    assert get_all_subclasses(D) == {F}
    assert get_all_subclasses(E) == {G}

# Generated at 2022-06-12 22:46:30.803351
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    try:
        from builtins import object
    except ImportError:
        from __builtin__ import object

    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(object):
        pass

    class E(D):
        pass

    assert get_all_subclasses(object) == set([A, B, C, D, E])
    # Must still be valid after we create a new class
    class F(object):
        pass

    assert get_all_subclasses(object) == set([A, B, C, D, E, F])
    # Test with custom classes
    class TestA(object):
        pass

    class TestB(TestA):
        pass

    class TestC(TestB):
        pass


# Generated at 2022-06-12 22:46:32.363123
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C, B):
        pass

    class E(D):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E])

# Generated at 2022-06-12 22:46:40.653114
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Test classes
    class Base(object): pass
    class A(Base): pass
    class B(Base): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(C): pass
    class G(E, D): pass
    # A new object with all classes
    obj = {B: (A, C, D, E, F, G),
           A: (C, D, F),
           C: (F,),
           D: (),
           E: (G,),
           F: (),
           G: ()}

    for cls in obj:
        result = get_all_subclasses(cls)
        expected = obj[cls]

# Generated at 2022-06-12 22:46:45.221496
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

    class D(C):
        pass

    class E(C):
        pass

    class F(D):
        pass

    class G(D):
        pass

    assert(set(get_all_subclasses(Base)) == set([A, B, C, D, E, F, G]))

# Generated at 2022-06-12 22:46:51.351359
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(C): pass
    class E(A): pass
    class F(E): pass
    class G(F): pass

    assert set([F, G, C, D]) == get_all_subclasses(B)
    assert set([F, G]) == get_all_subclasses(E)

# Generated at 2022-06-12 22:46:57.990266
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(A):
        pass
    class E():
        pass
    class F(E):
        pass
    assert set([B, C, D]) == get_all_subclasses(A)
    assert set([E, F]) == get_all_subclasses(E)
    assert set([A, B, C, D, E, F]) == get_all_subclasses(object)

# Generated at 2022-06-12 22:47:02.847045
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(): pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E(D): pass
    subclasses = get_all_subclasses(A)

    assert E in subclasses
    assert D in subclasses
    assert C in subclasses
    assert B in subclasses
    assert A not in subclasses

# Generated at 2022-06-12 22:47:07.005841
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    assert get_all_subclasses(A) == set([B, C, D])
    class E(object): pass
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:47:23.012577
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

    class AA(object):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:47:33.927045
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # test_all_subclasses_class structure
    #
    #   test_all_subclasses_class
    #       |
    #       +-- test_all_subclasses_leaf_class
    #       |
    #       +-- test_all_subclasses_mid_class
    #               |
    #               +-- test_all_subclasses_leaf_class
    #
    #        test_all_subclasses_leaf_class
    class test_all_subclasses_class(object):
        pass

    class test_all_subclasses_leaf_class(test_all_subclasses_class):
        pass

    class test_all_subclasses_mid_class(test_all_subclasses_class):
        pass

    test_all_subclasses_leaf_class()
    test_all_subclasses_mid_

# Generated at 2022-06-12 22:47:37.493558
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

    assert set(get_all_subclasses(A)) == set([B, C, D, E])



# Generated at 2022-06-12 22:47:44.793105
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

    class F(D):
        pass

    assert get_all_subclasses(A) == set([B, D, E, F, C])
    assert get_all_subclasses(B) == set([E])
    assert get_all_subclasses(C) == set([D, F])
    assert get_all_subclasses(D) == set([F])
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:47:49.563298
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define some classes
    class a(object):
        pass

    class b(a):
        pass

    class c(a):
        pass

    class d(c):
        pass

    # Define tests
    assert set(get_all_subclasses(a)) == set([b, c, d])
    assert set(get_all_subclasses(b)) == set([])
    assert set(get_all_subclasses(c)) == set([d])
    assert set(get_all_subclasses(d)) == set([])

# Generated at 2022-06-12 22:47:55.224567
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
    assert set(subclasses) == set([B, C, D])

    subclasses = get_all_subclasses(E)
    assert set(subclasses) == set([])

# Generated at 2022-06-12 22:48:03.053318
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create some test classes
    class P1:
        pass
    class P2:
        pass
    class P3:
        pass
    class C1(P1):
        pass
    class C2(P1):
        pass
    class C3(C1):
        pass
    class C4(P2):
        pass
    class C5(P3):
        pass
    class C6(C3):
        pass
    class C7(C3):
        pass
    class C8(C6):
        pass
    class C9(C7):
        pass
    # Check that the function get_all_subclasses works as expected
    assert get_all_subclasses(P1) == set([C1, C2, C3, C6, C7, C8, C9])
    assert get_

# Generated at 2022-06-12 22:48:08.394850
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class SuperClass(object):
        pass
    class ClassA(SuperClass):
        pass
    class ClassB(SuperClass):
        pass
    class ClassA_1(ClassA):
        pass
    class ClassA_2(ClassA):
        pass
    class ClassB_1(ClassB):
        pass
    class ClassB_2(ClassB):
        pass
    assert set(get_all_subclasses(SuperClass)) == set([ClassA, ClassB, ClassA_1, ClassA_2, ClassB_1, ClassB_2])

# Generated at 2022-06-12 22:48:16.198487
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

    # Known values
    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set([D])
    assert set(get_all_subclasses(C)) == set([])
    assert set(get_all_subclasses(D)) == set([])

    # Check that no side effects is done
    assert A.__subclasses__() == [B,C]
    assert B.__subclasses__() == [D]

# Generated at 2022-06-12 22:48:22.729589
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
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
    assert set([B, C]) == get_all_subclasses(A)
    assert set([E]) == get_all_subclasses(D)
    assert set([B, C, E]) == get_all_subclasses(object)

# Generated at 2022-06-12 22:48:56.086443
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class C(object):
        pass

    class B(C):
        pass

    class A(B):
        pass

    assert set(get_all_subclasses(C)) == set([B, A])



# Generated at 2022-06-12 22:49:03.085912
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    # test basic case
    assert set(get_all_subclasses(A)) == set((B, C, D))
    # test empty case
    assert set(get_all_subclasses(C)) == set()
    # test multiple inheritance
    class E(A): pass
    class F(E): pass
    class G(C, F): pass
    assert set(get_all_subclasses(A)) == set((B, C, D, E, F, G))

# Generated at 2022-06-12 22:49:07.876052
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():
        ''' Class A '''

    class AA(A):
        ''' Class AA '''

    class AB(A):
        ''' Class AB '''

    class B():
        ''' Class B '''

    class BA(B):
        ''' Class BA '''

    assert A in get_all_subclasses(A)
    assert AB in get_all_subclasses(A)
    assert AA in get_all_subclasses(A)
    assert BA not in get_all_subclasses(A)

# Generated at 2022-06-12 22:49:13.273749
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    assert set([A]) == get_all_subclasses(A)

    class B(A):
        pass
    assert set([A, B]) == get_all_subclasses(A)

    class C(A):
        pass
    assert set([A, B, C]) == get_all_subclasses(A)

    class D(B):
        pass
    assert set([A, B, C, D]) == get_all_subclasses(A)

    class E(B):
        pass
    assert set([A, B, C, D, E]) == get_all_subclasses(A)

    class F(E):
        pass
    assert set([A, B, C, D, E, F]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:49:17.710428
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):  # pylint: disable=too-few-public-methods
        pass

    class B(A):  # pylint: disable=too-few-public-methods
        pass

    class C(B):  # pylint: disable=too-few-public-methods
        pass

    class D(A):  # pylint: disable=too-few-public-methods
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert B not in get_all_subclasses(B)

# Generated at 2022-06-12 22:49:24.112921
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a simple object model
    class A():
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
    class G(C):
        pass
    class H(C):
        pass

    classes = get_all_subclasses(A)
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F in classes
    assert G in classes
    assert H in classes



# Generated at 2022-06-12 22:49:25.953160
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    assert get_all_subclasses(B) == [C]

# Generated at 2022-06-12 22:49:34.426457
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):

        def foo(self):
            pass

    class B(A):

        def bar(self):
            pass

    class C(A):

        def baz(self):
            pass

    class D(B):

        def qux(self):
            pass

    class E(B, C):

        def quux(self):
            pass

    class F(C):

        def corge(self):
            pass
    class G(D):
        def grault(self):
            pass
    class H(F):
        def garply(self):
            pass
    class I(H):
        def waldo(self):
            pass
    class J(H):
        def fred(self):
            pass
    # test1
    assert A in get_all_subclasses(A)


# Generated at 2022-06-12 22:49:40.449474
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

    subclasses = get_all_subclasses(A)

    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses
    assert G in subclasses
    assert H in subclasses

# Generated at 2022-06-12 22:49:46.137103
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B: pass
    class C: pass
    class D(A): pass
    class E(A): pass
    class F(B): pass

    assert set([D, E, F]) == get_all_subclasses(A)
    assert set([D, E]) == get_all_subclasses(A)
    assert set([F]) == get_all_subclasses(B)
    assert set([]) == get_all_subclasses(C)
    assert set([F]) == get_all_subclasses(B)

# Generated at 2022-06-12 22:50:55.174490
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import _utils
    import unittest

    # Define class tree
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
    class H(D):
        pass
    class I(C):
        pass

    # Python does not provide any function to retrieve all inherited classes,
    # so we implement get_all_subclasses to be able to make test cases

# Generated at 2022-06-12 22:51:02.703416
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class C(object): pass
    class D(object): pass
    class B(A): pass
    class E(B): pass
    class F(E): pass
    class G(E): pass
    class H(D): pass
    class I(H): pass
    print(get_all_subclasses(A))
    assert get_all_subclasses(A) == set([B, E, F, G]), "Set does not match expected values"
    assert get_all_subclasses(C) == set([]), "Empty set should return empty set"
    assert get_all_subclasses(D) == set([H, I]), "Set does not match expected values"

