

# Generated at 2022-06-12 22:41:11.985888
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B: pass
    class C: pass
    class D(A): pass
    class E(A): pass
    class F(E): pass
    class G(B,C): pass
    class H(D,F,G): pass
    assert set(get_all_subclasses(A)) == set([D,E,F,H])

# Generated at 2022-06-12 22:41:16.605191
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
    class F(D, E):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F}


# Generated at 2022-06-12 22:41:24.910404
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

    assert get_all_subclasses(A) == set([B, C, D, E, F, G])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(F) == set([G])

# Generated at 2022-06-12 22:41:34.553960
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a sample tree of class
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
    class G(F):
        pass
    class H(E):
        pass
    class I(E):
        pass

    # act
    result = get_all_subclasses(A)
    assert result == set([B, C, D, E, F, G, H, I])

# Define a sample tree of class
# Tree:
#       A
#   B    C
# D E  F
#       G
#   H, I

# Generated at 2022-06-12 22:41:39.965209
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Build a hierarchy of three classes, pass the main class to `get_all_subclasses` and check the result
    """
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    classes = get_all_subclasses(A)
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F in classes
    assert len(classes) == 5

# Generated at 2022-06-12 22:41:46.542892
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a mock object hierarchy
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

    class F(D):
        pass

    class G(A):
        pass

    # Expected result
    expected = {B, C, D, F, G}

    # Get actual result
    actual = get_all_subclasses(A)

    # Check the result
    assert len(expected) == len(actual)
    for v in expected:
        assert v in actual

# Generated at 2022-06-12 22:41:53.554145
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

    subclasses = get_all_subclasses(A)
    test_result = True
    if not len(subclasses) == 3:
        test_result = False
    if not B in subclasses:
        test_result = False
    if not C in subclasses:
        test_result = False
    if not D in subclasses:
        test_result = False
    assert test_result

# Generated at 2022-06-12 22:41:57.447187
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

    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:42:06.319516
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    test_get_all_subclasses() is a unit test for the get_all_subclasses() function.
    """
    import unittest

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

    class G(E):
        pass

    class H(E):
        pass

    class I(G):
        pass

    # Test all subclasses of A
    result = get_all_subclasses(A)
    assert set(result) == set([B, C, D, E, F, G, H, I])
    # Test all subclasses of D
    result = get_all_subclasses(D)
   

# Generated at 2022-06-12 22:42:16.110275
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test get_all_subclasses method to find all child class
    '''
    # We define the base class
    class A(object):
        def __init__(self):
            pass
    # Then a child class
    class B(A):
        def __init__(self):
            super(B, self).__init__()
    # Then another child class
    class C(B):
        def __init__(self):
            super(C, self).__init__()
    # And another one
    class D(B):
        def __init__(self):
            super(D, self).__init__()
    # Finally a grand-child class
    class E(C):
        def __init__(self):
            super(E, self).__init__()
    # We expect to have B,

# Generated at 2022-06-12 22:42:24.835488
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

    class E(C):
        pass
    class F(E):
        pass
    class G(F):
        pass
    class H(G):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, E, F, G, H])

# Generated at 2022-06-12 22:42:34.946598
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    function: test_get_all_subclasses

    description: This function test the function get_all_subclasses
                 This function requires two functions: A and B

                 A inherits from object
                 B inherits from A
    """
    class A:
        pass

    class B(A):
        pass

    def test_get_all_subclasses_of_A():
        # check if object A is a subclass of object A
        assert(A in get_all_subclasses(A))

    def test_get_all_subclasses_of_B():
        # check if object B is a subclass of object A
        assert(B in get_all_subclasses(A))
        # check if object B is a subclass of object B
        assert(B in get_all_subclasses(B))

    test_get_all_

# Generated at 2022-06-12 22:42:40.587630
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

    subclasses = get_all_subclasses(A)
    assert set(subclasses) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:42:51.100840
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    import itertools

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

    class TestCase(unittest.TestCase):
        def test_get_all_subclasses(self):
            self.assertEqual(get_all_subclasses(A), set([B, C, D, E]))
            self.assertEqual(itertools.chain([A], get_all_subclasses(A)), [A, B, C, D, E])

    # Run test
    test_case = TestCase()
    test_case.test_get_all_subclasses()

# Generated at 2022-06-12 22:42:59.151485
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
    A_subclasses = get_all_subclasses(A)
    B_subclasses = get_all_subclasses(B)
    C_subclasses = get_all_subclasses(C)
    D_subclasses = get_all_subclasses(D)
    assert set(A_subclasses) == {B,C,D}
    assert set(B_subclasses) == {D}
    assert set(C_subclasses) == set()
    assert set(D_subclasses) == set()

# Generated at 2022-06-12 22:43:08.594532
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from types import ModuleType
    assert(set(get_all_subclasses(ModuleType)) == set())
    assert(set(get_all_subclasses(object)) ==
           set([type, type(None), ModuleType]))

    class Foo(object):
        pass

    class Bar(Foo):
        pass

    class Baz(Bar):
        pass

    class Qux(Bar):
        pass

    assert(set(get_all_subclasses(object)) ==
           set([type, type(None), ModuleType, Foo, Bar, Baz, Qux]))

    assert(set(get_all_subclasses(Foo)) == set([Bar, Baz, Qux]))

# Generated at 2022-06-12 22:43:19.272467
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
    class I(F):
        pass
    class J(I):
        pass
    class K(J):
        pass

    subclasses = get_all_subclasses(A)
    assert(len(subclasses) == 8)
    for sc in [B, C, D, E, F, G, H, I]:
        assert(sc in subclasses)

    subclasses = get_all_subclasses(B)
    assert(len(subclasses) == 4)

# Generated at 2022-06-12 22:43:30.398294
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    :rtype: bool
    :returns: True if the test passes, False otherwise
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
    class F(E):
        pass
    assert get_all_subclasses(A) == set([B, D, C, E, F])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([E, F])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([F])
    assert get_all_subclasses(F) == set([])


# Generated at 2022-06-12 22:43:34.608941
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base(object):
        pass
    class Foo(Base):
        pass
    class Bar(Base):
        pass
    class FooBar(Foo):
        pass
    class FooBarBar(FooBar):
        pass

    subclasses = get_all_subclasses(Base)
    assert subclasses == set([Foo, Bar, FooBar, FooBarBar])

# Generated at 2022-06-12 22:43:39.737162
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Create a Sample class and its subclasses
    class Sample:
        pass

    class SampleChild1(Sample):
        pass

    class SampleChild2(Sample):
        pass

    # Create SampleChild3 which is child of SampleChild1
    class SampleChild3(SampleChild1):
        pass

    class SampleChild4(SampleChild1):
        pass

    class SampleChild5(SampleChild2):
        pass

    # Check that all subclasses of Sample are found
    found_subclasses = get_all_subclasses(Sample)
    assert len(found_subclasses) == 5
    assert SampleChild1 in found_subclasses
    assert SampleChild2 in found_subclasses
    assert SampleChild3 in found_subclasses
    assert SampleChild4 in found_subclasses
    assert SampleChild5 in found_subclasses


# Generated at 2022-06-12 22:43:53.076382
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Tested with following tree
    A
    |_ B
       |_C
       |_D
    |_ E
    """
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
    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([C, D])
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:44:04.810218
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Leaf(object):
        pass

    class Leaf_A1(Leaf):
        pass

    class Leaf_A2(Leaf):
        pass

    class Leaf_B1(Leaf):
        pass

    class Root(object):
        pass

    class A(Root):
        pass

    class B(Root):
        pass

    class A1(A):
        pass

    class A2(A):
        pass

    class B1(B):
        pass

    class Node(object):
        pass

    class Root1(Node):
        pass

    class Root2(Node):
        pass

    class Root3(Node):
        pass

    assert set(get_all_subclasses(Leaf)) == set([
        Leaf_A1,
        Leaf_A2,
        Leaf_B1,
    ])

# Generated at 2022-06-12 22:44:12.161499
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        def __init__(self, id):
            self.id = id

        def __str__(self):
            return 'Class A with id = %d' % self.id

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    class E(C):
        pass

    class F(E):
        pass

    class G(E):
        pass

    # we create multiple instance of each class
    b1 = B(1)
    b2 = B(2)
    c1 = C(3)
    d1 = D(4)
    e1 = E(5)
    f1 = F(6)
    f2 = F(7)
    g1 = G(8)

    # Get all subclasses of

# Generated at 2022-06-12 22:44:18.871442
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
    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses
    assert len(subclasses) == 5

# Generated at 2022-06-12 22:44:23.731580
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

    assert set(get_all_subclasses(A)) == {B, C, D}
    assert set(get_all_subclasses(B)) == {D}
    assert set(get_all_subclasses(C)) == set()
    assert set(get_all_subclasses(D)) == set()

# Generated at 2022-06-12 22:44:29.438129
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
    expected = {A, B, C, D, E, F}
    found = get_all_subclasses(A)
    assert(expected == found)



# Generated at 2022-06-12 22:44:38.999518
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
    class G(C, B):
        pass
    class H(F):
        pass
    class I(D):
        pass

    subs = {C, D, E, F, G, H, I}

    assert set(get_all_subclasses(A)) == subs
    assert set(get_all_subclasses(B)) == set()
    assert set(get_all_subclasses(C)) == {E, G, F, H}
    assert set(get_all_subclasses(D)) == {I}

# Generated at 2022-06-12 22:44:49.479961
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This is a unit test for the function get_all_subclasses.  It does
    not need to be included in the module but helps developers test
    the function.
    '''
    from ansible.module_utils._text import to_text
    # Classes below are created to test multiple cases
    # * Multiple subclasses
    # * Multiple subclasses with multiple subclasses
    # * Subclass with no subclasses
    # * Class with no subclass
    class ClassA(object):
        def __init__(self):
            pass
    class ClassAA(ClassA):
        def __init__(self):
            super(ClassAA, self).__init__()
    class ClassACA(ClassA):
        def __init__(self):
            super(ClassACA, self).__init__()

# Generated at 2022-06-12 22:44:56.518160
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

    assert A in get_all_subclasses(object)
    assert B in get_all_subclasses(object)
    assert C in get_all_subclasses(object)
    assert D in get_all_subclasses(object)

    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)

    assert D in get_all_subclasses(C)

# Generated at 2022-06-12 22:45:03.744862
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a test tree
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
    class I(D):
        pass
    class J(E):
        pass
    class K(E):
        pass
    class L(F):
        pass
    class M(F):
        pass
    class N(G):
        pass
    class O(G):
        pass
    class P(H):
        pass
    class Q(H):
        pass
    class R(I):
        pass
    class S(I):
        pass
   

# Generated at 2022-06-12 22:45:15.243230
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a class to make test
    class A(object):
        pass
    a = A()
    assert not get_all_subclasses(A)
    class B(A):
        pass
    assert B in get_all_subclasses(A)
    class C(A):
        pass
    assert C in get_all_subclasses(A)
    class D(B, C):
        pass
    assert D in get_all_subclasses(A)
    class E(D):
        pass
    assert E in get_all_subclasses(A)
    assert not get_all_subclasses(E)

# Generated at 2022-06-12 22:45:25.369648
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types

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

    class H(G):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H])
    assert set(get_all_subclasses(B)) == set([D, G, H])
    assert set(get_all_subclasses(C)) == set([E, F])
    assert set(get_all_subclasses(D)) == set([G, H])
    assert set(get_all_subclasses(E)) == set([])
   

# Generated at 2022-06-12 22:45:33.903206
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    sub1
     \_ sub11
     \_ sub12
          \_ subsub121
    sub2
     \_ sub21

    The test is based on sub1, sub11, sub12, subsub121, sub2, sub21
    '''
    class A(object):
        pass
    class sub1(A):
        pass
    class sub11(sub1):
        pass
    class sub12(sub1):
        pass
    class subsub121(sub12):
        pass
    class sub2(A):
        pass
    class sub21(sub2):
        pass

    subs = get_all_subclasses(A)
    assert len(subs) == 6
    assert sub1 in subs
    assert sub11 in subs
    assert sub12 in subs
    assert subsub121 in subs


# Generated at 2022-06-12 22:45:42.837048
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class a:
        pass
    class b:
        pass
    class c:
        pass
    class d(c):
        pass
    class e(a,b):
        pass
    class f(e,d):
        pass

    assert get_all_subclasses(a) == set((e,f))
    assert get_all_subclasses(b) == set((e,f))
    assert get_all_subclasses(c) == set((d,f))
    assert get_all_subclasses(d) == set((f,))
    assert get_all_subclasses(e) == set((f,))
    assert get_all_subclasses(f) == set(())



# Generated at 2022-06-12 22:45:46.958577
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(C):
        pass
    class E(D):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([C, D, E])
    assert get_all_subclasses(C) == set([D, E])
    assert get_all_subclasses(D) == set([E])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:45:53.383873
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
    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(float) == set([])

# Generated at 2022-06-12 22:46:03.857375
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    class A(object):
        def __init__(self):
            pass

    class A1(A):
        def __init__(self):
            super(A1, self).__init__()

    class A2(A):
        def __init__(self):
            super(A2, self).__init__()

    class B(object):
        def __init__(self):
            pass

    class B1(B):
        def __init__(self):
            super(B1, self).__init__()

    class B2(B):
        def __init__(self):
            super(B2, self).__init__()

    class C(object):
        def __init__(self):
            pass


# Generated at 2022-06-12 22:46:13.210310
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    unittest = try_import('unittest')
    if unittest is None:
        # The package unittest is not installed
        return

    class TestClassParent(object):
        pass

    class TestClass1(TestClassParent):
        pass

    class TestClass2(TestClassParent):
        pass

    class TestClass1Child1(TestClass1):
        pass

    class TestClass1Child2(TestClass1):
        pass

    class TestClass2Child1(TestClass2):
        pass

    class TestClass2Child2(TestClass2):
        pass

    class TestClass2Child3(TestClass2):
        pass

    class TestClass2Child1Child1(TestClass2Child1):
        pass


# Generated at 2022-06-12 22:46:17.108640
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TopClass:
        pass

    class BaseClass(TopClass):
        pass

    class GenericClass(TopClass):
        pass

    class LeafClass(BaseClass):
        pass

    class LeafClass2(BaseClass):
        pass

    assert get_all_subclasses(TopClass) == {BaseClass, GenericClass, LeafClass, LeafClass2}

# Generated at 2022-06-12 22:46:21.004752
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
    class F(D):
        pass
    assert (get_all_subclasses(A) == set((B, C, D, E, F)))

test_get_all_subclasses()

# Generated at 2022-06-12 22:46:34.355744
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a sample inheritance tree
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(A):
        pass

    class E(B, C, D):
        pass

    class F(E):
        pass

    class G(B, D, F):
        pass

    # Check that all classes inheriting from A are found
    assert get_all_subclasses(A) == {B, C, D, E, F, G}

    # Check that all classes inheriting from B, C and D are found
    assert get_all_subclasses(B) == {E, F, G}
    assert get_all_subclasses(C) == {E, F, G}

# Generated at 2022-06-12 22:46:37.033991
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    assert sorted(get_all_subclasses(A)) == [B, C, D]

# Generated at 2022-06-12 22:46:44.545557
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import defaultdict
    from ansible.module_utils.six import with_metaclass

    class ABCMeta(type):
        def __new__(mcs, clsname, bases, attrs):
            cls = super(ABCMeta, mcs).__new__(mcs, clsname, bases, attrs)
            # Keep a dict of class name vs class reference
            ABCMeta.MAPPING[clsname] = cls
            return cls

    ABCMeta.MAPPING = defaultdict(lambda: None)

    class AbstractClass(with_metaclass(ABCMeta, object)):
        pass

    class F1(AbstractClass):
        pass

    class F2(AbstractClass):
        pass

    class F3(AbstractClass):
        pass

    class F4(AbstractClass):
        pass

   

# Generated at 2022-06-12 22:46:50.231898
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    result = get_all_subclasses(dict)
    assert 'OrderedDict' in result
    assert 'defaultdict' in result
    result = get_all_subclasses(int)
    assert 'float' in result
    assert 'bool' in result
    assert 'complex' not in result
    result = get_all_subclasses(float)
    assert 'complex' in result

# Generated at 2022-06-12 22:47:00.302632
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Foo(object): pass
    class FooChild(Foo): pass
    class FooGrandchild(FooChild): pass
    class Bar(object): pass
    class BarChild(Bar): pass

    # Test 1:
    #   Given Foo as parent class
    #   Foo has FooChild and Bar as child class; FooChild has Bar as child class
    #   We expect all subclasses to be :
    #       - FooChild
    #       - Bar
    #       - BarChild
    assert set(get_all_subclasses(Foo)) == set([FooChild, Bar, BarChild])
    # Test 2:
    #   Given FooChild as parent class
    #   We expect all subclasses to be :
    #       - Bar
    #       - BarChild

# Generated at 2022-06-12 22:47:09.774337
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import namedtuple

    # Defining many classes with different complexity
    class TestClass0:
        pass

    class TestClass1(TestClass0):
        pass

    class TestClass2(TestClass0):
        pass

    class TestClass3(TestClass0):
        pass

    class TestClass4(TestClass0):
        pass

    class TestClass5(TestClass0):
        pass

    class TestClass6(TestClass0):
        pass

    # Defining namedtuples
    NamedTuple = namedtuple('NamedTuple', ['a'])

    class TestClass7(NamedTuple):
        pass

    class TestClass8(NamedTuple):
        pass

    class TestClass9(NamedTuple):
        pass

    class TestClass10(TestClass9):
        pass

   

# Generated at 2022-06-12 22:47:12.789418
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Foo: pass
    class Bar(Foo): pass
    class Tar(Foo): pass
    class Jar(Foo): pass
    class Car(Bar): pass
    class Gar(Car): pass
    class Dar(Gar): pass
    class Far(Dar): pass

    assert get_all_subclasses(Foo) == set([Bar, Tar, Jar, Car, Gar, Dar, Far])

# Generated at 2022-06-12 22:47:20.110909
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types
    import unittest

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
    class G(object):
        pass

    class TestGetAllSubclass(unittest.TestCase):
        '''
        Unit test for method get_full_classname
        '''

        def test_get_all_subclasses(self):
            self.assertEqual(get_all_subclasses(A), set([B,C,D,E,F]))
            self.assertEqual(get_all_subclasses(B), set([D]))

# Generated at 2022-06-12 22:47:27.358303
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

    all_subclasses = get_all_subclasses(A)
    assert B in all_subclasses
    assert C in all_subclasses
    assert D in all_subclasses
    assert E in all_subclasses
    assert F in all_subclasses
    assert len(all_subclasses) == 5

# Generated at 2022-06-12 22:47:35.807185
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
    class E(B):
        pass
    class F(C):
        pass
    class G(C):
        pass
    class H(G):
        pass
    # Test for all children
    assert get_all_subclasses(A) == {B, D, E, C, F, G, H}
    # Test for children with depth 1
    assert set(A.__subclasses__()) == {B, C}


# Generated at 2022-06-12 22:48:03.312323
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

    class class1(object):
        pass

    class class2(class1):
        pass

    class3 = type('class3', (object,), {})
    class class4(class3):
        pass

    class class5(class4):
        pass

    class class6(class1):
        pass

    class class7(object):
        pass

    class class8(class2, class7):
        pass

    class class9(class4):
        pass

    class class10(class9):
        pass

    expected_classes = {class2, class4, class5, class6, class8, class9, class10}


# Generated at 2022-06-12 22:48:10.668890
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test the get_all_subclasses function
    '''
    # mro stands for method resolution order
    class A:
        pass
    class B(A):
        pass
    class Foo:
        pass
    class C(B, Foo):
        pass
    class D(B):
        pass

    assert C.mro()[1] == B
    assert C in get_all_subclasses(A)
    assert B in get_all_subclasses(D)
    assert Foo in get_all_subclasses(C)
    # Test that get_all_subclasses is working with inheritance (A in C mro)
    assert C in get_all_subclasses(A)
    assert A not in get_all_subclasses(A)
    assert Foo not in get_all_subclasses(B)



# Generated at 2022-06-12 22:48:16.578939
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import ansible.modules as amods

    # Getting all Module subclasse
    module_subclasses = get_all_subclasses(amods.Module)

    # Testing if all modules are subclasses of Module
    for module_class in amods.MODULE_CACHE:
        assert module_class in module_subclasses

    # Test if _load_params is a subclasse of Module
    assert amods._load_params in module_subclasses

# Generated at 2022-06-12 22:48:25.170822
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def make_class(classname):
        class_attributes = locals().copy()
        class_meta = type(classname, (), class_attributes)
        return class_meta

    class_base = make_class('class_base')

    class_1 = make_class('class_1')
    class_1.__bases__ = (class_base, )

    class_2 = make_class('class_2')
    class_2.__bases__ = (class_1, )

    class_3 = make_class('class_3')
    class_3.__bases__ = (class_2, )

    class_4 = make_class('class_4')
    class_4.__bases__ = (class_2, )

    class_5 = make_class('class_5')
    class_

# Generated at 2022-06-12 22:48:31.155225
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    class E:
        pass

    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([C, D])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

test_get_all_subclasses()

# Generated at 2022-06-12 22:48:39.608101
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import collections
    import ansible

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

    # Test a full tree
    all_sub = set(get_all_subclasses(A))
    assert len(all_sub) == 6 and all_sub == set((B, C, D, E, F))

    # Test the case where there is no subclasses
    all_sub = get_all_subclasses(collections.MutableMapping)
    assert not all_sub

    # Test the case where an error is raised

# Generated at 2022-06-12 22:48:47.989764
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Unit test for get_all_subclasses
    #     ClassB
    #     /    \
    # ClassBA  \
    #          ClassBB

    class ClassA(object):
        pass

    class ClassB(ClassA):
        pass

    class ClassBA(ClassB):
        pass

    class ClassBB(ClassB):
        pass

    class ClassC(ClassA):
        pass

    class ClassD(ClassC):
        pass

    class ClassE(ClassD):
        pass

    class ClassF(object):
        pass

    class ClassG(ClassF):
        pass

    assert ClassA in get_all_subclasses(ClassA)
    assert ClassB in get_all_subclasses(ClassA)
    assert ClassC in get_all_subclasses(ClassA)
    assert ClassD in get_

# Generated at 2022-06-12 22:48:55.338165
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    A test function for function get_all_subclasses.

    For this test, we will create a simple base class, add two subclasses, and then add a
    subclass to one of the original subclasses.  If this is successful, the output of
    :py:func:`get_all_subclasses` should contain the base class, both subclasses, and the
    subclass of the one of the subclasses.
    """
    # You really shouldn't name classes using a type name (or type for that matter).
    # You shouldn't do this in production code.  However, in a test class the possibility of
    # causing a conflict is low, and it make the test code easier to read.
    class type(object): pass
    class type2(object): pass
    class subclass(type): pass
    class subclass2(type): pass

# Generated at 2022-06-12 22:49:04.215365
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    assert_equals = lambda l1, l2: l1.sort() == l2.sort()
    dummy_class = type('DummyClass', (object,), {})
    child_class1 = type('ChildClass1', (dummy_class,), {})
    child_class2 = type('ChildClass2', (dummy_class,), {})
    grandchild_class1 = type('GrandChildClass1', (child_class1,), {})
    grandchild_class2 = type('GrandChildClass2', (child_class2,), {})
    grandchild_class3 = type('GrandChildClass3', (child_class1,), {})

# Generated at 2022-06-12 22:49:10.151229
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # First define the test classes
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

    # Test the different hierarchy cases
    assert(all(map(lambda x: x in get_all_subclasses(A), [A, B, C, D, E, F])))
    assert(all(map(lambda x: x in get_all_subclasses(B), [B, D, E, F])))
    assert(all(map(lambda x: x in get_all_subclasses(C), [C])))

# Generated at 2022-06-12 22:50:06.015411
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Build a sample class hierarchy for unit testing
    class RootClass(object):
        pass

    class Child1(RootClass):
        pass

    class Child2(RootClass):
        pass

    class Child3(RootClass):
        pass

    class GrandChild1(Child1):
        pass

    class GrandChild2(Child2):
        pass

    class GrandChild3(Child3):
        pass

    class GrandChild4(Child3):
        pass

    class GrandGrandChild1(GrandChild1):
        pass

    class GrandGrandChild2(GrandChild1):
        pass

    # Issue 1261
    class X(Child3):
        pass

    class Y(X):
        pass

    class Z(Y):
        pass

    # find all decendants of RootClass

# Generated at 2022-06-12 22:50:16.352665
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base(object): pass
    class A(Base): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(A): pass
    class F(C): pass
    class G(F): pass
    class H(F): pass
    class I(H): pass
    class J(H): pass
    assert get_all_subclasses(Base) == set((A, B, C, D, E, F, G, H, I, J))
    assert get_all_subclasses(A) == set((B, C, D, E, F, G, H, I, J))
    assert get_all_subclasses(C) == set((D, F, G, H, I, J))

# Generated at 2022-06-12 22:50:24.211470
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

    assert get_all_subclasses(A) == set((A, B, C, D, E, F))
    assert get_all_subclasses(B) == set((B, D))
    assert get_all_subclasses(C) == set((C, E, F))
    assert get_all_subclasses(D) == set((D,))
    assert get_all_subclasses(E) == set((E, F))
    assert get_all_subclasses(F) == set((F,))
    assert get_all_subclasses(object) == set()

# Generated at 2022-06-12 22:50:28.385415
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

    # A class should be in its subclasses
    assert A in get_all_subclasses(A)

    # B should be in its subclasses
    assert B in get_all_subclasses(B)

    # B should be in A's subclasses
    assert B in get_all_subclasses(A)

    # D should be in A's subclasses
    assert D in get_all_subclasses(A)

    # C should be in A's subclasses
    assert C in get_all_subclasses(A)

# Generated at 2022-06-12 22:50:33.765375
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

    assert set(A.__subclasses__()) == set([B, C])
    assert set(B.__subclasses__()) == set([D])
    assert set(C.__subclasses__()) == set([])
    assert set(D.__subclasses__()) == set([E])
    assert set(E.__subclasses__()) == set([])

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set([])
    assert get_all_

# Generated at 2022-06-12 22:50:42.228162
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

    class G(F):
        pass

    class H(object):
        pass

    class I(H):
        pass

    class J(H):
        pass

    class K(I):
        pass

    class L(I):
        pass

    class M(J):
        pass

    class N(J):
        pass

    class O(J):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E, F, G}
    assert result ==  expected
    result = get_all_subclasses(H)

# Generated at 2022-06-12 22:50:46.265373
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Unit test for get_all_subclasses

    It tests that we can find all subclasses for a class
    """
    class Super():
        pass
    class Sub(Super):
        pass
    class SubSub(Sub):
        pass
    assert get_all_subclasses(Super) == set([Sub, SubSub])

# Generated at 2022-06-12 22:50:50.825398
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(D): pass
    res = get_all_subclasses(A)
    assert len(res) == 4
    assert type(B()) in res
    assert type(C()) in res
    assert type(D()) in res
    assert type(E()) in res

# Generated at 2022-06-12 22:50:57.106840
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A1(object):
        pass

    class A2(object):
        pass

    class A3(object):
        pass

    class B1(A1):
        pass

    class B2(A1):
        pass

    class B3(A1, A2):
        pass

    class C1(B1, B2):
        pass

    class D1(C1):
        pass

    class D2(C1):
        pass

    class D3(C1):
        pass

    class E1(D2):
        pass

    class E2(D2):
        pass

    class E3(D3):
        pass

    A1_subclasses = get_all_subclasses(A1)

# Generated at 2022-06-12 22:51:01.103252
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

    class F(B, C):
        pass

    assert get_all_subclasses(A) == { B, C, D, E, F }