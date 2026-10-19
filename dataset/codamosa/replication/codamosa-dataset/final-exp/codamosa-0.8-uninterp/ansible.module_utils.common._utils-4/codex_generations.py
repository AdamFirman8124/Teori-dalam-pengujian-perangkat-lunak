

# Generated at 2022-06-12 22:41:15.229572
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

    assert get_all_subclasses(A) == {B, C, D, E, F, G}
    assert get_all_subclasses(A) == get_all_subclasses(C)
    assert get_all_subclasses(A) == get_all_subclasses(B)
    assert get_all_subclasses(B) == get_all_subclasses(D)
    # It does not matter the order of the classes
    assert get_all_subclasses(A) == {C, B, G, F, D, E}

# Generated at 2022-06-12 22:41:19.336261
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

    assert get_all_subclasses(A) == {B, C, D}

# Generated at 2022-06-12 22:41:31.448679
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def sub1(): pass
    def sub1_1(): pass
    def sub1_2(): pass
    sub1_1.__bases__ = (sub1,)
    sub1_2.__bases__ = (sub1,)

    def sub2(): pass
    def sub2_1(): pass
    def sub2_2(): pass
    sub2_1.__bases__ = (sub2,)
    sub2_2.__bases__ = (sub2,)

    def module(): pass
    module.__bases__ = (sub1, sub2,)

    for sc in get_all_subclasses(module):
        if sc is module:
            assert False
        elif sc is sub1:
            assert True
        elif sc is sub2:
            assert True

# Generated at 2022-06-12 22:41:40.087433
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Check that get_all_subclasses works as expected
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
    class H(object):
        pass
    class I(A):
        pass
    assert H not in get_all_subclasses(A)
    assert I in get_all_subclasses(A)
    assert {B, D, E} == set(get_all_subclasses(B))
    assert {C, F, G} == set(get_all_subclasses(C))
    assert {G, F, D, E, B, C}

# Generated at 2022-06-12 22:41:44.871500
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
    assert get_all_subclasses(A) == set((B, C, D, E, F, G))


# Generated at 2022-06-12 22:41:51.241144
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

    class G(D):
        pass

    class H(C):
        pass

    assert set(get_all_subclasses(A)) == set([A, B, C, D, E, F, G, H])

# Generated at 2022-06-12 22:41:57.021361
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B,C):
        pass

    class E(object):
        pass

    def check(expected, actual):
        assert frozenset(expected) == frozenset(actual), "Expected %s, but got %s" % (expected, actual)
    check([A], get_all_subclasses(object))
    check([B, D], get_all_subclasses(A))

# Generated at 2022-06-12 22:42:04.179751
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Sub-testcase for function get_all_subclasses.
    Function to test if the function get_all_subclasses
    provides the expected results
    '''
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

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([C, D, E])



# Generated at 2022-06-12 22:42:11.752080
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Defining class hierachy
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
    class F(D):
        pass
    class G(D):
        pass

    # Testing
    assert get_all_subclasses(A) == set([B, F, G, C, D])

# Generated at 2022-06-12 22:42:18.926273
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses
    '''
    import types
    # Create a class hierarchy
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass

    # get_all_subclasses works with and without a module name
    assert types.FunctionType in get_all_subclasses(types.FunctionType)
    assert types.FunctionType in get_all_subclasses(types.FunctionType.__module__ + "." + classes.FunctionType.__name__)

    # get_all_subclasses return 2 level subclasses
    assert get_all_subclasses(A) == set([B, C]) or get_all_subclasses(A) == set([C, B])

# Generated at 2022-06-12 22:42:31.530572
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        def __init__(self, x):
            self.x = x
    class B(A):
        def __init__(self, x):
            A.__init__(self, x)
    class C(B):
        def __init__(self, x):
            B.__init__(self, x)
    class D(A):
        def __init__(self, x):
            A.__init__(self, x)
    class E(object):
        def __init__(self, x):
            self.x = x
    class F(E):
        def __init__(self, x):
            E.__init__(self, x)
    class J(F):
        def __init__(self, x):
            E.__init__(self, x)

# Generated at 2022-06-12 22:42:36.215142
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Test1(object):
        pass

    class Test2(Test1):
        pass

    class Test3(Test2):
        pass

    class Test4(Test2):
        pass

    class Test5(Test4):
        pass

    assert not set(Test1.__subclasses__()).difference(get_all_subclasses(Test1))



# Generated at 2022-06-12 22:42:47.219878
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    ''' Test `get_all_subclasses` '''
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

    class G(B, E, F):
        pass

    class H(D, F):
        pass

    class I(H, G, C):
        pass

    all_subclasses = get_all_subclasses(object)
    assert A in all_subclasses
    assert B in all_subclasses
    assert C in all_subclasses
    assert D in all_subclasses
    assert E in all_subclasses
    assert F in all_subclasses
    assert G in all_subclasses
    assert H in all

# Generated at 2022-06-12 22:42:51.199992
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(C): pass

    assert(set(get_all_subclasses(A)) == set([B, C, D]))

# Generated at 2022-06-12 22:42:55.179735
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

    print(get_all_subclasses(A))

# Generated at 2022-06-12 22:43:01.082155
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
    class H(D):
        pass
    class I(G):
        pass

    expected_results = {A, B, C, D, E, F, G, H, I}
    observed_results = get_all_subclasses(object)
    assert expected_results == observed_results

# Generated at 2022-06-12 22:43:10.350616
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E(C): pass

    assert get_all_subclasses(A) == {B, C, D, E}

    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(C): pass

    assert get_all_subclasses(A) == {B, C, D}

    # This test shows that order matters
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E(C): pass

    assert get_all_subclasses(A) == {B, C, D, E}

# Generated at 2022-06-12 22:43:15.379745
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class C1(object):
        pass

    class C2(C1):
        pass

    class C3(C1):
        pass

    class C4(C2):
        pass

    class C5(C3):
        pass

    assert get_all_subclasses(C1) == set([C2, C4, C3, C5])

# Generated at 2022-06-12 22:43:18.178589
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

    assert set(get_all_subclasses(A)) == set([A, B, C, D])

# Generated at 2022-06-12 22:43:20.991462
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

    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:43:27.047463
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

    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:43:33.058845
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
    class G(B,C):
        pass

    # Expected output
    expected_output = set([B, D, E, F, G])

    # Function to test
    output = get_all_subclasses(A)

    assert output == expected_output

# Generated at 2022-06-12 22:43:42.278134
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import itertools
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
    res = get_all_subclasses(A)
    expected = set(itertools.chain(subclasses(B), subclasses(C)))
    assert res == expected
    res = get_all_subclasses(B)
    expected = subclasses(D)
    assert res == expected

# return only direct subclasses of class cls

# Generated at 2022-06-12 22:43:49.582057
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(C): pass
    class F(E): pass
    class G(B): pass
    class H(C): pass
    class I(F): pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I])
    assert get_all_subclasses(C) == set([D, E, F, H])



# Generated at 2022-06-12 22:43:55.920027
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    dict1 = {"name": "foo", "data": "bar"}
    dict2 = {"name": "baz", "data": "qux"}
    dict3 = {"name": "qux", "data": "quux"}
    dict4 = {"name": "corge", "data": "grault"}

    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class dictlike(dict):
        pass

    class dict1class(dictlike):
        def __init__(self, *args, **kwargs):
            super(dict1class, self).__init__(*args, **kwargs)
            self.update(dict1)


# Generated at 2022-06-12 22:44:01.930728
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
    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 3
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses


# Generated at 2022-06-12 22:44:07.821877
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(object):
        pass

    class AB(A, B):
        pass

    class BA(B, A):
        pass

    class ABBA(AB, BA):
        pass

    expected = set([
        'A',
        'AB',
        'ABBA',
        'BA',
        'B',
    ])

    actual = [sc.__name__ for sc in get_all_subclasses(object)]

    assert set(actual) == expected

# Generated at 2022-06-12 22:44:14.297309
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import sys

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    # Test if C and D are subclasses of A
    subclasses_expected = {C, D}

    if sys.version_info[0] == 2:
        module_name = '__main__'
    else:
        module_name = __name__
    assert subclasses_expected == get_all_subclasses(sys.modules[module_name].A)

# Generated at 2022-06-12 22:44:22.561627
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Base class
    class Base():
        pass

    # Create subclasses
    class A(Base):
        pass

    class B(Base):
        pass

    class D(B):
        pass

    class F(D):
        pass

    class E(D):
        pass

    class C(Base):
        pass

    all_subclasses = get_all_subclasses(Base)

    # Check all subclasses are in all_subclasses
    assert A in all_subclasses
    assert B in all_subclasses
    assert D in all_subclasses
    assert F in all_subclasses
    assert E in all_subclasses
    assert C in all_subclasses


# Generated at 2022-06-12 22:44:30.018862
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
    assert len(get_all_subclasses(A)) == 3

    class D(B, A):
        pass

    assert D in get_all_subclasses(A)
    assert len(get_all_subclasses(A)) == 4

# Generated at 2022-06-12 22:44:39.748734
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert set([B, C]) == get_all_subclasses(A)
    assert set() == get_all_subclasses(B)

    class D(B):
        pass

    class E(C):
        pass

    assert set([B, C, D, E]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:44:47.524834
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
        :returns: None
        :raises: AssertionError
    """
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    classes = (A, B, C, D)
    assert len(classes) == len(get_all_subclasses(A)), 'Invalid number of subclasses'
    for it in classes:
        assert it in get_all_subclasses(A), 'Class %s not in subclasses' % it


# Generated at 2022-06-12 22:44:56.305894
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import UserDict, UserList, UserString
    from collections import Mapping, MutableMapping
    from collections import Collection, MutableSequence, MutableSet
    from collections import Sequence, Set, Sized

    assert get_all_subclasses(UserDict) == get_all_subclasses(Mapping)
    assert get_all_subclasses(UserDict) == get_all_subclasses(MutableMapping)
    assert get_all_subclasses(UserList) == get_all_subclasses(MutableSequence)
    assert get_all_subclasses(UserList) == get_all_subclasses(Sequence)
    assert get_all_subclasses(UserList) == get_all_subclasses(MutableSet)

# Generated at 2022-06-12 22:45:01.165910
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TestA(object):
        pass

    class TestB(TestA):
        pass

    class TestC(TestB):
        pass

    class TestD(TestB):
        pass

    class TestE(TestD):
        pass

    subclasses = get_all_subclasses(TestA)
    assert TestB in subclasses
    assert TestC in subclasses
    assert TestD in subclasses
    assert TestE in subclasses

test_get_all_subclasses()

# Generated at 2022-06-12 22:45:08.198571
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    assert get_all_subclasses(A) == set([B, C, D, E, F])
    assert get_all_subclasses(C) == set([F])
    assert get_all_subclasses(F) == set([])
    assert get_all_subclasses(D) == set([])

# Generated at 2022-06-12 22:45:13.737695
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
    class E(A):
        pass
    class F(B):
        pass
    class G(B):
        pass
    class H(C):
        pass
    class I(C):
        pass
    class J(C):
        pass
    class K(C):
        pass
    assert(set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H, I, J, K]))
    assert(set(A.__subclasses__()) == set([B, C, D, E]))

# Generated at 2022-06-12 22:45:23.168660
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Base classes for testing
    class Base(object):
        pass
    class SubBase(Base):
        pass
    class SubSubBase(SubBase):
        pass
    class SubBase2(Base):
        pass
    class SubSubBase2(SubBase2):
        pass
    class Other(object):
        pass
    class SubOther(Other):
        pass

    # Get all subclasses
    all_subclasses = get_all_subclasses(Base)
    # Assert the right set of class is returned
    assert all_subclasses == {SubSubBase, SubBase, SubSubBase2, SubBase2}
    # Assert no subclass of Other is included in the set
    assert SubOther not in all_subclasses

# Generated at 2022-06-12 22:45:30.863788
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
    class F(A):
        pass
    class G(F):
        pass
    class H(G):
        pass
    class I(H):
        pass
    class J(H):
        pass
    class K(J):
        pass
    class L(K):
        pass
    class M(A):
        pass
    class O(L):
        pass
    class P(O):
        pass
    class Q(P):
        pass
    class R(Q):
        pass
    class S(R):
        pass
    class T(M):
        pass
    class U(T):
        pass

# Generated at 2022-06-12 22:45:41.223831
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a test class hierarchy
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(B): pass
    class G(C): pass
    class H(C): pass
    class I(D): pass
    # Verify that get_all_subclasses returns the expected values
    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I])
    assert get_all_subclasses(B) == set([E, F])
    assert get_all_subclasses(C) == set([G, H])
    assert get_all_subclasses(D) == set([I])
    assert get_all_subclasses(E) == set()
    assert get_all

# Generated at 2022-06-12 22:45:48.321753
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    from ansible.module_utils._text import to_text

    # Create a fake subclass container
    class FakeSubClassContainer:
        '''
        This is an empty class with only method __subclasses__ defined.  This will be used to help
        test get_all_subclasses.
        '''
        def __init__(self, subclasses):
            self.__subclasses__ = subclasses

    # Create some fake classes
    class A:
        pass
    class B1(A):
        pass
    class B2(A):
        pass
    class B3(A):
        pass
    class C1(B1):
        pass
    class C2(B1):
        pass

# Generated at 2022-06-12 22:46:01.197123
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert set([A, B, C]) == set(get_all_subclasses(A))

# Generated at 2022-06-12 22:46:06.903513
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Declare a fake class hierarchy
    class A:
        pass

    class B:
        pass

    class C(A):
        pass

    class D(A):
        pass

    class E(C):
        pass

    # Check if A has all expected subclasses
    # pylint: disable=comparison-with-itself
    assert set([C, D, E]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:46:14.578381
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
    class E(A):
        pass
    class F(A):
        pass
    class G(A):
        pass
    class AB(B):
        pass
    class AC(C):
        pass
    class AD(D):
        pass
    class AE(E):
        pass
    class BD(D):
        pass
    class CF(F):
        pass
    class GH(H):
        pass

    assert get_all_subclasses(A) == set([
        AB, AC, AD, AE, BD, CF, GH
    ])

# Generated at 2022-06-12 22:46:22.768675
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses
    '''
    class TestClass(object):
        pass
    class TestSubClass(TestClass):
        pass
    class TestSubClass2(TestClass):
        pass
    class TestSubSubClass(TestSubClass):
        pass
    class TestSubSubClass2(TestSubClass):
        pass
    class TestSubSubClass3(TestSubClass2):
        pass
    subclasses = get_all_subclasses(TestClass)
    assert TestClass in subclasses
    assert TestSubClass in subclasses
    assert TestSubSubClass in subclasses
    assert TestSubSubClass2 in subclasses
    assert TestSubClass2 in subclasses
    assert TestSubSubClass3 in subclasses
    assert len(get_all_subclasses(None)) == 0

# Generated at 2022-06-12 22:46:28.545750
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class GrandParent:
        pass

    class Parent(GrandParent):
        pass

    class Parent2(GrandParent):
        pass

    class Parent3(GrandParent):
        pass

    class Parent4(Parent3):
        pass

    class Son(Parent):
        pass

    class Son2(Parent, Parent2):
        pass

    assert list(get_all_subclasses(GrandParent)) == [Parent, Parent2, Parent3, Parent4, Son, Son2]

# Generated at 2022-06-12 22:46:37.034843
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Unit test for function get_all_subclasses
    """
    class A(object):
        pass

    # Create a class structure like this:
    #
    # A
    # |-B     D     F
    # |  |-C  |-E  |-G
    #      |-H  |-I
    #
    # Verify that get_all_subclasses returns all of the classes
    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    class E(D):
        pass

    class F(A):
        pass

    class G(F):
        pass

    class H(C):
        pass

    class I(E):
        pass


# Generated at 2022-06-12 22:46:40.653124
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

    class E(D):
        pass

    class F(D):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:46:44.426679
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

    assert get_all_subclasses(A) == {B, C, D}
    assert get_all_subclasses(E) == set()


"""
Decorator to make a property available on both class and instances
"""



# Generated at 2022-06-12 22:46:55.335855
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for the get_all_subclasses function

    :rtype: bool
    :returns: True if successful, otherwise False
    '''
    class A(object):
        '''
        A class with no subclass
        '''
        pass

    class B(A):
        '''
        A subclass of A
        '''
        pass

    class C(A):
        '''
        Another subclass of A
        '''
        pass

    class D(B):
        '''
        A subclass of B
        '''
        pass

    class E(D):
        '''
        A subclass of D
        '''
        pass

    class F(E):
        '''
        A subclass of E
        '''
        pass


# Generated at 2022-06-12 22:47:00.016442
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(C): pass

    subclasses_of_A = get_all_subclasses(A)
    assert B in subclasses_of_A
    assert C in subclasses_of_A
    assert D in subclasses_of_A
    assert E in subclasses_of_A

# Generated at 2022-06-12 22:47:26.884658
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
    class F(object):
        pass

    subclasses = get_all_subclasses(A)
    assert A in subclasses
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F not in subclasses



# Generated at 2022-06-12 22:47:35.721674
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

    assert get_all_subclasses(A) == {B, C, D, E, F}
    assert get_all_subclasses(B) == {D, E, F}
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == {E, F}
    assert get_all_subclasses(E) == {F}
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:47:38.614808
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
    assert get_all_subclasses(object) == set()
    assert get_all_subclasses(A) == {B, C, D}

# Generated at 2022-06-12 22:47:47.173106
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # This class will be used for unit tests
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
    class G(E):
        pass
    class H(object):
        pass
    class I(H):
        pass

    result = get_all_subclasses(A)
    # The list of classes in the first test
    cls_list = [B, C, D, E, F, G]
    # The second test
    H_cls_list = get_all_subclasses(H)

    assert len(result) == len(cls_list)
    for cls in cls_list:
        assert cls

# Generated at 2022-06-12 22:47:52.184941
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit tests for the function get_all_subclasses.
    '''

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(object):
        pass

    classes = get_all_subclasses(object)
    assert A in classes
    assert B in classes
    assert C in classes
    assert D in classes

    classes = get_all_subclasses(A)
    assert A not in classes
    assert B in classes
    assert C in classes
    assert D not in classes

    classes = get_all_subclasses(B)
    assert A not in classes
    assert B not in classes
    assert C not in classes
    assert D not in classes

    classes = get_all_subclasses(C)
    assert A not in classes


# Generated at 2022-06-12 22:47:59.118015
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

    class F(D, E):
        pass

    class G(B):
        pass

    assert set(F.__mro__) == set(get_all_subclasses(F))
    assert set([A, C, E, D, F]) == set(get_all_subclasses(A))
    assert set([B, G]) == set(get_all_subclasses(B))

# Generated at 2022-06-12 22:48:06.070942
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Some samples classes
    class A: pass
    class B: pass
    class C: pass
    class D(A): pass
    class E(B): pass
    class F(D): pass
    class G(D): pass
    class H(E): pass
    class I(F): pass
    class J(G): pass
    assert get_all_subclasses(A) == set([D, E, F, G, H, I, J])
    assert get_all_subclasses(B) == set([E, H])
    assert get_all_subclasses(C) == set([])

# Generated at 2022-06-12 22:48:09.891929
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class ParentClass(object):
        pass
    class MiddleClass(ParentClass):
        pass
    class ChildClass(MiddleClass):
        pass
    assert set([ChildClass, MiddleClass]) == set(get_all_subclasses(ParentClass))
    assert set([ChildClass]) == set(get_all_subclasses(MiddleClass))
    assert set([]) == set(get_all_subclasses(ChildClass))

# Generated at 2022-06-12 22:48:12.184194
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E(C): pass
    assert set(get_all_subclasses(A)) == set([B, C, D, E])

# Generated at 2022-06-12 22:48:15.104907
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    assert set([B, C, D]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:49:05.653969
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert C in get_all_subclasses(A)
    assert B in get_all_subclasses(A)

# Generated at 2022-06-12 22:49:11.756579
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class parent:
        pass
    class child_1(parent):
        pass
    class child_2(parent):
        pass
    class grand_child_1(child_1):
        pass
    class grand_child_1_1(child_1):
        pass
    class grand_child_2(child_2):
        pass
    class grand_grand_child_1(grand_child_1):
        pass
    class great_grand_child_1(grand_grand_child_1):
        pass

    assert get_all_subclasses(parent) == {child_1, child_2, grand_child_1, grand_child_1_1,
                                          grand_child_2, grand_grand_child_1, great_grand_child_1}
    assert get_all_subclasses(child_1)

# Generated at 2022-06-12 22:49:17.245259
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class ClsA(object):
        pass

    class ClsB(ClsA):
        pass

    class ClsC(ClsB):
        pass

    class ClsD(object):
        pass

    classes = {ClsA, ClsB, ClsC, ClsD}
    all_classes = get_all_subclasses(object)
    assert classes.issubset(all_classes)

# Generated at 2022-06-12 22:49:25.367305
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # We create 3 classes
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

    class ClassF(ClassD):
        pass

    # we expect to have ClassA, ClassB, ClassC and ClassF in the results
    assert(set([ClassA, ClassB, ClassC, ClassD, ClassE, ClassF]) == get_all_subclasses(ClassA))
    # we expect to have ClassB and ClassD in the results
    assert(set([ClassB, ClassC, ClassD, ClassE, ClassF]) == get_all_subclasses(ClassB))
    # we expect to have ClassF in the results

# Generated at 2022-06-12 22:49:32.424416
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass

    class B(A): pass
    class C(A): pass
    class D(A): pass

    class E(B): pass
    class F(B): pass

    class G(C): pass
    class H(C): pass

    class I(D): pass

    class J(E): pass
    class K(E): pass

    class L(G): pass
    class M(G): pass

    class N(I): pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I, J, K, L, M, N])

# Generated at 2022-06-12 22:49:37.207175
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(D): pass
    class F(D): pass
    class G(F): pass
    class H(F): pass

    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H])

# Generated at 2022-06-12 22:49:43.370119
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
    class F(object):
        pass
    assert set(get_all_subclasses(A)) == set(get_all_subclasses(C)) == set([B, C, D, E])
    assert set(get_all_subclasses(F)) == set([F])
    assert len(set(get_all_subclasses(object))) > 20

# Generated at 2022-06-12 22:49:49.293146
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
    class F(object):
        pass
    assert get_all_subclasses(A) == set([B,C,D,E])
    assert get_all_subclasses(B) == set([])
    assert get_all_subclasses(C) == set([D,E])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:49:59.900150
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class parent1(object):
        pass
    class parent2(object):
        pass
    class parent3(object):
        pass
    class parent4(object):
        pass
    class child1(parent1):
        pass
    class child1a(parent1):
        pass
    class child2(parent2):
        pass
    class child2a(parent2):
        pass
    class child2b(parent2):
        pass
    class child3(parent3):
        pass
    class child3a(parent3):
        pass
    class child3b(parent3):
        pass
    class child3c(parent3):
        pass
    class child4a(parent4):
        pass
    class child4b(parent4):
        pass
    class child4c(parent4):
        pass

# Generated at 2022-06-12 22:50:06.097488
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
    class F(C):
        pass
    class G(D):
        pass
    class H(G):
        pass
    res = get_all_subclasses(A)
    for klass in sorted((B, C, D, E, F, G, H), key=lambda x: x.__name__):
        assert klass in res, '{0} not in {1}'.format(klass, res)
    assert len(res) == 7