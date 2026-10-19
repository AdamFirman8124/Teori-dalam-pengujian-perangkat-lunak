

# Generated at 2022-06-12 22:41:05.504670
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(E): pass
    assert get_all_subclasses(A) == set([B, C, D, E, F])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([E, F])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([F])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:41:14.892174
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test function get_all_subclasses
    '''
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D])

    # Test with a cyclic references
    class E(C):
        pass

    C.__bases__ = (E,)
    assert set(get_all_subclasses(A)) == set([B, E, D])

    # Test the direct reference
    class F(E):
        pass

    assert set(get_all_subclasses(F)) == set([])


# Generated at 2022-06-12 22:41:21.347496
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(object): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(object): pass
    class G(C, D): pass
    class H(A, object): pass
    class I(G, H): pass
    # get_all_subclasses returns a set
    assert get_all_subclasses(A) == {A, C, D, G, H, I}

# Generated at 2022-06-12 22:41:26.593939
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(B): pass
    class F(D): pass

    assert get_all_subclasses(A) == {B, C, E, D, F}



# Generated at 2022-06-12 22:41:34.992593
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a root class
    class A(object):
        pass
    # And three children
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    # The direct subclasses of A are B and C
    assert set(A.__subclasses__()) == set([B, C])
    # However, the subclasses have no idea about D
    assert set(B.__subclasses__()) == set([])
    assert set(C.__subclasses__()) == set([])
    # We want this method to discover D
    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:41:41.712719
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(C): pass
    class F(B): pass
    def tst(cls, expected):
        assert set(get_all_subclasses(cls)) == set(expected)

    tst(object, [A, B, C, D, E, F])
    tst(A, [B, C, D, E, F])
    tst(B, [F])
    tst(C, [D, E])
    tst(D, [])
    tst(E, [])
    tst(F, [])

# Generated at 2022-06-12 22:41:48.512041
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

    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)

    assert A not in get_all_subclasses(B)
    assert B in get_all_subclasses(B)
    assert C in get_all_subclasses(B)
    assert D not in get_all_subclasses(B)


# Generated at 2022-06-12 22:41:56.244985
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # The following is a structure to test
    # A
    # |- B
    #   |- B1
    #   |- B2
    #     |- B21
    # |- C
    #   |- C1
    class A(object):
        pass

    class B(A):
        pass
    class B1(B):
        pass
    class B2(B):
        pass
    class B21(B2):
        pass

    class C(A):
        pass
    class C1(C):
        pass

    assert set(get_all_subclasses(A)) == {B,B1,B2,B21,C,C1}

# Generated at 2022-06-12 22:42:03.752581
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Utility class to test
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
    class F(E):
        pass
    class G(C):
        pass
    classes = get_all_subclasses(A)
    # Check against expected results
    assert G in classes
    assert B in classes
    assert F in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert A not in classes


# Generated at 2022-06-12 22:42:06.370897
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

    assert(get_all_subclasses(A) == set([B, C, D]))
    assert(get_all_subclasses(B) == set([C]))
    assert(get_all_subclasses(C) == set())
    assert(get_all_subclasses(D) == set())

# Generated at 2022-06-12 22:42:16.296581
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

    assert list(get_all_subclasses(A)) == [B, C, D, E]
    assert list(get_all_subclasses(B)) == [B, D, E]
    assert list(get_all_subclasses(C)) == []
    assert list(get_all_subclasses(D)) == [D, E]
    assert list(get_all_subclasses(E)) == [E]

# Generated at 2022-06-12 22:42:26.256135
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Tests function get_all_subclasses by creating a tree of mock classes and making sure the
    correct number of classes are returned by get_all_subclasses
    '''
    # Mock classes needed because we cannot create acutal classes in this testing function
    class A:
        pass

    class B:
        pass

    class C:
        pass

    class D(B):
        pass

    class E(B):
        pass

    class F(E):
        pass

    A.__subclasses__ = lambda: [B, C]
    B.__subclasses__ = lambda: [D, E]
    E.__subclasses__ = lambda: [F]

    # Test that all subclasses of A are found
    classes = get_all_subclasses(A)
    assert C in classes
    assert D in classes


# Generated at 2022-06-12 22:42:36.034636
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test the correctness of get_all_subclasses function

    When get_all_subclasses function is called, all subclasses of a class should be returned,
    unless recursion has gone too deep and eventually overflows.
    '''
    import random
    import six

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

    class G(B):
        pass

    class H(F):
        pass

    class I(G):
        pass

    class J(E):
        pass

    class K(J):
        pass


# Generated at 2022-06-12 22:42:47.129271
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(D, C): pass
    class H(E, F): pass
    class I(G, H): pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G, H, I])
    assert set(get_all_subclasses(B)) == set([D, E, G, H, I])
    assert set(get_all_subclasses(C)) == set([F, G, H, I])
    assert set(get_all_subclasses(D)) == set([G, I])
    assert set(get_all_subclasses(E)) == set

# Generated at 2022-06-12 22:42:57.412879
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class clsA(object):
        def __init__(self):
            pass
    class clsB(clsA):
        def __init__(self):
            pass
    class clsC(clsA):
        def __init__(self):
            pass
    class clsD(clsB):
        def __init__(self):
            pass
    class clsE(clsB, clsC):
        def __init__(self, arg1):
            # test if the class can have an other argument
            pass
    list_classes = [clsA, clsB, clsC, clsD, clsE]
    set_classes = set(list_classes)
    assert set_classes == set(get_all_subclasses(clsA))

# Generated at 2022-06-12 22:43:03.855592
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

    class E(D):
        pass

    test_class = A
    assert set([B, C]) == set(A.__subclasses__())
    assert set([D]) == set(B.__subclasses__())
    assert set() == set(C.__subclasses__())
    assert set() == set(D.__subclasses__())
    assert set() == set(E.__subclasses__())

    assert set([B, C, D, E]) == set(get_all_subclasses(A))
    assert set([D, E]) == set(get_all_subclasses(B))

# Generated at 2022-06-12 22:43:08.483979
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass

    assert set(get_all_subclasses(A)) == set([B, C])
    assert set(get_all_subclasses(object)) == set([A, B, C])

# Generated at 2022-06-12 22:43:19.197474
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        '''
        Base class for testing
        '''
        pass

    class B(object):
        '''
        Class which doesn't inherit from A
        '''
        pass

    class C(A):
        '''
        Class which inherits from A
        '''
        pass

    class D(A):
        '''
        Class which inherits from A
        '''
        pass

    class E(D):
        '''
        Class which inherits from D and A
        '''
        pass

    class F(B):
        '''
        Class which inherits from B
        '''
        pass

    subclasses = get_all_subclasses(A)
    # Make sure only A's subclasses are returned
    assert B not in subclasses
    # Make sure that the class B

# Generated at 2022-06-12 22:43:30.279230
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses
    '''
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
    class F(B):
        pass
    class G(B):
        pass
    class H(B):
        pass
    class I(D):
        pass
    class J(D):
        pass
    class K(I):
        pass
    class L(J):
        pass
    class M(J):
        pass
    class N(M):
        pass

# Generated at 2022-06-12 22:43:34.322241
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

    all_subclasses = get_all_subclasses(A)

    assert all_subclasses == {B, D}

# Generated at 2022-06-12 22:43:43.072795
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(object):
        pass

    ret = get_all_subclasses(A)

    assert ret == set([B, C])
    assert len(ret) == 2

# Generated at 2022-06-12 22:43:52.810859
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class Class1():
        pass

    class Class2():
        pass

    class Class3(Class2):
        pass

    class Class4(Class1):
        pass

    class Class5(Class3):
        pass

    class Class6(Class5):
        pass

    class Class7(Class1):
        pass

    assert get_all_subclasses(Class1) == {Class4, Class5, Class6, Class7}
    assert get_all_subclasses(Class2) == {Class3, Class5, Class6}
    assert get_all_subclasses(Class3) == {Class5, Class6}
    assert get_all_subclasses(Class4) == set()
    assert get_all_subclasses(Class5) == {Class6}
    assert get_all_subclasses(Class6) == set()

# Generated at 2022-06-12 22:44:01.930856
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

    class Fake(object):
        pass

    assert(set(get_all_subclasses(A)) == set([B, D, F, E, C]))
    assert(set(get_all_subclasses(B)) == set([]))
    assert(set(get_all_subclasses(Fake)) == set([]))

# Generated at 2022-06-12 22:44:05.641516
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

    test_outcome = get_all_subclasses(A)
    assert B in test_outcome and B in test_outcome and D in test_outcome

# Generated at 2022-06-12 22:44:12.658915
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    # Classic case
    class B(A): pass
    class C(B): pass
    class D(C): pass
    # Adding some classes
    class E(A): pass
    assert(set(get_all_subclasses(A)) == set((B, C, D, E)))
    assert(set(get_all_subclasses(B)) == set((C, D)))
    assert(set(get_all_subclasses(C)) == set((D,)))
    assert(set(get_all_subclasses(D)) == set(()))
    class F(C): pass
    class G(D): pass
    assert(set(get_all_subclasses(A)) == set((B, C, D, E, F, G)))

# Generated at 2022-06-12 22:44:19.505104
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(C): pass
    class G(F): pass
    class H(G): pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H])
    assert get_all_subclasses(B) == set([E])
    assert get_all_subclasses(D) == set([])

# Generated at 2022-06-12 22:44:27.948310
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Verify that two examples, with two levels of inheritance, are working as expected

    :rtype: boolean
    :returns: True if all the tests succeed, otherwise False.
    '''
    class FatherA:
        pass

    class FatherB:
        pass

    class Son(FatherA):
        pass

    class GrandSon(Son):
        pass

    class GrandDaughter(Son):
        pass

    class UglySon(FatherB):
        pass

    assert get_all_subclasses(Son) == set([GrandSon, GrandDaughter])
    assert get_all_subclasses(UglySon) == set([])

# Generated at 2022-06-12 22:44:35.047765
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(C): pass
    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses
    assert G in subclasses
    assert len(subclasses) == 7

# Generated at 2022-06-12 22:44:41.082921
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit testing for function get_all_subclasses
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

    class F(C):
        pass

    class G(object):
        pass

    ansiblest_classes = frozenset([A, B, C, D, E, F, G])

    discovered_classes = get_all_subclasses(object)
    assert discovered_classes == ansiblest_classes

# Generated at 2022-06-12 22:44:47.283159
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils import basic
    from ansible.module_utils.common.removed import RemovedModule

    subclasses = set(get_all_subclasses(basic.AnsibleModule))
    assert basic.AnsibleModule in subclasses
    assert RemovedModule in subclasses
    assert len(subclasses) == 20  # To check if a new class has been added, this number needs to be updated

# Generated at 2022-06-12 22:44:58.901353
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Build a tree of class to test
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
    class H(F):
        pass
    class I(H):
        pass
    class J(G):
        pass
    class K(I):
        pass
    class L(K):
        pass
    # Construct expected result
    all_subclasses = set([B, C, D, E, F, G, H, I, J, K, L])
    # Test result
    assert get_all_subclasses(A) == all_subclasses

# Generated at 2022-06-12 22:45:06.429168
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B: pass
    class C(A, B): pass
    class D(B, A): pass
    class E(C, D): pass

    assert get_all_subclasses(A) == {C, D, E}
    assert get_all_subclasses(B) == {C, D, E}
    assert get_all_subclasses(C) == {E}
    assert get_all_subclasses(D) == {E}
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:45:12.796954
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Mocking a structure of classes like:

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

    subclasses = get_all_subclasses(A)

    assert subclasses == {B, D, C, E}
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

    subclasses = get_all_subclasses(A)

    assert subclasses == {B, D, C, E}


# Generated at 2022-06-12 22:45:23.418666
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
    class G(B):
        pass
    class H(C):
        pass
    class I(C):
        pass
    class J(C):
        pass
    class K(D):
        pass
    class L(D):
        pass
    class M(D):
        pass
    subclasses = get_all_subclasses(A)
    assert(len(subclasses) == 13)
    assert(B in subclasses)
    assert(C in subclasses)
    assert(D in subclasses)
    assert(E in subclasses)

# Generated at 2022-06-12 22:45:27.878530
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

    class D(A):
        pass

    class E(B):
        pass

    result = get_all_subclasses(Base)
    assert A in result and B in result and C in result and D in result and E in result


# Generated at 2022-06-12 22:45:37.382955
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Prepare the abstract class
    class AbsClass(object):
        pass
    class Level2_1(AbsClass):
        pass
    class Level2_2(AbsClass):
        pass
    class Level3_1(Level2_1):
        pass
    class Level3_2(Level2_1):
        pass
    class Level3_3(Level2_2):
        pass
    class Level4_1(Level3_1):
        pass
    class Level4_2(Level3_2):
        pass
    class Level4_3(Level3_3):
        pass
    # Explore the subclasses
    subclasses = get_all_subclasses(AbsClass)
    assert Level2_1 in subclasses
    assert Level2_2 in subclasses
    assert Level3_1 in subclasses
    assert Level3_

# Generated at 2022-06-12 22:45:46.111210
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

    class G(F):
        pass

    class H(G):
        pass

    class I(H):
        pass

    assert get_all_subclasses(object) == set([A, E])
    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(E) == set([F, G, H, I])
    assert get_all_subclasses(F) == set([G, H, I])
    assert get_all_subclasses(G) == set([H, I])
    assert get_all_

# Generated at 2022-06-12 22:45:49.515597
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Creating a class hierarchy
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    assert set(get_all_subclasses(A)) == set((B, C, D))

# Generated at 2022-06-12 22:45:57.288142
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

    assert get_all_subclasses(A) == {B, C, D, E}
    assert get_all_subclasses(B) == {D}
    assert get_all_subclasses(C) == {E}
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(object) == set()

# Generated at 2022-06-12 22:46:07.705796
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

    expected = [A, C, D, F, G]
    assert(get_all_subclasses(A) == set(expected))
    assert(get_all_subclasses(B) == set([C]))
    assert(get_all_subclasses(C) == set([]))
    assert(get_all_subclasses(D) == set([F, G]))
    assert(get_all_subclasses(E) == set([F, G]))

# Generated at 2022-06-12 22:46:16.512860
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

    subclasses = set([B, C, D])
    assert subclasses == get_all_subclasses(A)

    subclasses = set([A, B, C, D])
    assert subclasses == get_all_subclasses(object)

    subclasses = set([])
    assert subclasses == get_all_subclasses(E)

# Generated at 2022-06-12 22:46:21.602402
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

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:46:30.885643
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses
    '''
    # Example of class tree
    # A
    # |- B
    # |  |- C
    # |  |  |- D
    # |- E
    #    |- F

    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    class E(A):
        pass

    class F(E):
        pass

    # Test if children of A are retrieved
    # In the class tree, children are B and E
    assert set(get_all_subclasses(A)) == {B, C, D, E, F}

    # Test if children of B are retrieved
    # In the class tree, children are C and D

# Generated at 2022-06-12 22:46:39.211069
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class ClassA:
        pass
    class ClassB(ClassA):
        pass
    class ClassC(ClassA):
        pass
    class ClassD(ClassC):
        pass
    class ClassE(ClassC):
        pass
    class ClassF(ClassC):
        pass
    class ClassG(ClassF):
        pass
    class ClassH(ClassC):
        pass
    class ClassI:
        pass
    class ClassJ(ClassI):
        pass
    cls_a_subclasses = get_all_subclasses(ClassA)
    cls_c_subclasses = get_all_subclasses(ClassC)
    cls_f_subclasses = get_all_subclasses(ClassF)
    assert ClassA in cls_a_subclasses
    assert ClassB in cls_a_subclasses

# Generated at 2022-06-12 22:46:45.065498
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types
    import ansible.module_utils._text as _text
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    all_subclasses = get_all_subclasses(types.ModuleType)

    assert PlayContext in all_subclasses
    assert TaskQueueManager in all_subclasses
    assert VariableManager in all_subclasses
    assert InventoryManager in all_subclasses
    assert _text.ANSIBLE_NOCOLOR in all_subclasses

# Generated at 2022-06-12 22:46:56.063965
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import itertools

    # This is a set of test cases, with the following components:
    #
    # [0] - The name of the class.
    # [1] - The name of the parent class to inherit from.
    # [2] - The name of the code in the class that should be executed to test that the class
    #       instance has the correct results.  Classes which do not need to test their results
    #       may set this value as None.
    # [3] - A list of lists of arguments to be passed to the test code.  Each argument list
    #       will be applied to the class whose test code is listed at the same index.
    # [4] - The expected result of running the test code.  May be one of the following types:
    #       set - The set of classes which are expected to be returned.
    #

# Generated at 2022-06-12 22:47:03.017111
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # This classes are like a tree
    #                  A
    #                 / \
    #                B   C
    #               / \   \
    #              D   E   F
    #             / \     / \
    #            G   H   I   J
    # Class B and C are siblings subclasses of A, like classes D and E are siblings subclasses of B,
    # and finally classes I and J are siblings subclasses of F.

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

    class I(F):
        pass


# Generated at 2022-06-12 22:47:06.431255
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # define some classes
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass

    assert(set((A, B, C)) == get_all_subclasses(A))

# Generated at 2022-06-12 22:47:07.008317
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    pass

# Generated at 2022-06-12 22:47:11.984759
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class RootClass(object):
        pass

    class ChildClass(RootClass):
        pass

    class GrandChildClass(ChildClass):
        pass

    class GreatGrandChildClass(GrandChildClass):
        pass

    l = get_all_subclasses(RootClass)

    assert set(l) == set([ChildClass, GrandChildClass, GreatGrandChildClass]), \
        "Unexpected classes found when searching for subclasses of root class"

# Generated at 2022-06-12 22:47:24.460029
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
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
    class H(F):
        pass
    class I(G):
        pass
    class J(I):
        pass
    class K(I):
        pass

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    f = F()
    g = G()
    h = H()
    i = I()
    j = J()
    k = K()


# Generated at 2022-06-12 22:47:35.303059
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types

    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    class E(B, C, D):
        pass

    subclasses = get_all_subclasses(A)
    assert subclasses == {B, C, D, E}, \
        "The subclasses of A are wrong. It should be B, C, D, E"

    subclasses = get_all_subclasses(B)
    assert subclasses == {C, E}, \
        "The subclasses of B are wrong. It should be C and E"

    subclasses = get_all_subclasses(C)
    assert subclasses == {E}, \
        "The subclasses of C are wrong. It should be E"

    subclasses = get_all

# Generated at 2022-06-12 22:47:42.104123
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(C): pass
    class G(D): pass
    class H(E): pass
    class I(F): pass
    class J(G): pass

    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 8
    for sc in subclasses:
        assert issubclass(sc, A)
        assert not issubclass(sc, B)
        assert not issubclass(sc, C)
        assert not issubclass(sc, D)
        assert not issubclass(sc, E)
        assert not issubclass(sc, F)
        assert not issubclass(sc, G)
        assert not issubclass

# Generated at 2022-06-12 22:47:45.656019
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(D): pass
    class F(D, C): pass
    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:47:50.103793
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base(object):
        pass

    class Child(Base):
        pass

    class ChildChild(Child):
        pass

    class ChildChildChild(ChildChild):
        pass

    assert get_all_subclasses(Base) == set([Child, ChildChild, ChildChildChild])
    assert get_all_subclasses(Child) == set([ChildChild, ChildChildChild])
    assert get_all_subclasses(ChildChild) == set([ChildChildChild])
    assert get_all_subclasses(ChildChildChild) == set([])

# Generated at 2022-06-12 22:47:59.035103
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import json

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

    class G(D):
        pass

    class H(G):
        pass

    class I(H):
        pass

    class J(F):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I, J])
    assert get_all_subclasses(G) == set([H, I])
    assert get_all_subclasses(J) == set()
    assert get_all_subclasses(json) == set()

# Generated at 2022-06-12 22:48:04.512283
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a sample class hierarchy
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

    # Test function get_all_subclasses
    assert get_all_subclasses(A) == {B, C, D, E, F, G, H, I}
    assert get_all_subclasses(H) == set()

# Generated at 2022-06-12 22:48:07.172873
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass

    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert len(get_all_subclasses(A)) == 3


# Generated at 2022-06-12 22:48:12.443031
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    ''' Unit test for function get_all_subclasses '''
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

    assert get_all_subclasses(A) == set((B, C, D, E, F))
    assert get_all_subclasses(B) == set((D, E))
    assert get_all_subclasses(D) == set((E,))

# Generated at 2022-06-12 22:48:23.412005
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Build classes structure to test hierarchy
    class A(object):
        pass
    class A0(A):
        pass
    class A1(A):
        pass
    class A01(A0):
        pass
    class A02(A0):
        pass
    class A11(A1):
        pass
    class A12(A1):
        pass

    # Check that all classes are found
    result = get_all_subclasses(A)
    assert result == set([A0, A1, A01, A02, A11, A12])

    result = get_all_subclasses(A0)
    assert result == set([A01, A02])

    result = get_all_subclasses(A1)
    assert result == set([A11, A12])

    result = get_all_subclasses

# Generated at 2022-06-12 22:48:40.389240
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class C1:
        def __init__(self):
            self.name = 'C1'

    class C2:
        def __init__(self):
            self.name = 'C2'

    class C3:
        def __init__(self):
            self.name = 'C3'

    class C2_1(C2):
        def __init__(self):
            self.name = 'C2_1'

    class C2_2(C2):
        def __init__(self):
            self.name = 'C2_2'

    class C2_1_1(C2_1):
        def __init__(self):
            self.name = 'C2_1_1'


# Generated at 2022-06-12 22:48:45.356486
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

    class F(E):
        pass

    subclasses = get_all_subclasses(A)
    assert sorted(cls.__name__ for cls in subclasses) == ['B', 'C', 'D', 'E', 'F']

# Generated at 2022-06-12 22:48:52.237087
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.basic import AnsibleModule

    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(A):
        pass

    non_abstract_classes = get_all_subclasses(AnsibleModule)
    concrete_classes = non_abstract_classes - get_all_subclasses(AnsibleModule)
    module_subclasses = [tuple(cls.__module__, cls.__name__) for cls in non_abstract_classes]
    assert (tuple('ansible.modules.system.service', 'Service') in module_subclasses)

# Generated at 2022-06-12 22:48:56.969071
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    class C1: pass
    class C2(C1): pass
    class C3(C1): pass
    class C4(C3): pass
    class C5: pass
    assert set([C1, C2, C3, C4]) == get_all_subclasses(C1)
    assert set([C1, C2, C3, C4]) != get_all_subclasses(type)

# Generated at 2022-06-12 22:49:05.017760
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
    assert set([B, C, D, E, F]) == get_all_subclasses(A)
    assert set([D, F]) == get_all_subclasses(B)
    assert set([E]) == get_all_subclasses(C)
    assert set([F]) == get_all_subclasses(D)
    assert set([]) == get_all_subclasses(E)
    assert set([]) == get_all_subclasses(F)

# Generated at 2022-06-12 22:49:11.194194
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Base class
    class A: pass

    # Class with two children
    class B(A): pass
    class C(A): pass

    # Children of B
    class D(B): pass
    class E(B): pass

    # Children of C
    class F(C): pass

    # Create the expected list of all subclasses
    expected = [B, C, D, E, F]

    # Check the list of different classes
    found = get_all_subclasses(A)
    assert len(found) == len(expected)
    for f in found:
        assert f in expected

    # Check the list of same classes
    found = get_all_subclasses(B)
    assert len(found) == len(expected[0:3])
    for f in found:
        assert f in expected[0:3]


# Generated at 2022-06-12 22:49:20.774061
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

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

    class J(G):
        pass

    class K(G):
        pass

    class L(I):
        pass

    class M(I):
        pass

    class N(K):
        pass

    class O(K):
        pass

    class P(K):
        pass

    class Q(M):
        pass

    class R(M):
        pass

    class S(O):
        pass


# Generated at 2022-06-12 22:49:27.858507
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

    class E(A, B):
        pass
    class F(D, E):
        pass

    assert A in get_all_subclasses(object)
    assert B in get_all_subclasses(object)
    assert C in get_all_subclasses(object)
    assert D in get_all_subclasses(object)
    assert E in get_all_subclasses(object)
    assert F in get_all_subclasses(object)

    assert D in get_all_subclasses(A)
    assert C in get_all_subclasses(A)

    assert D in get_all_subclasses(C)
    assert F in get_all_sub

# Generated at 2022-06-12 22:49:36.559430
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    import sys

    # Prepare test classes
    class BaseTestClass(object):
        pass
    class LevelOneA(BaseTestClass):
        pass
    class LevelTwoA(LevelOneA):
        pass
    class LevelThreeA(LevelTwoA):
        pass
    class LevelOneB(BaseTestClass):
        pass
    class LevelThreeB(LevelOneB):
        pass
    class LevelOneC(BaseTestClass):
        pass
    class LevelOneD(BaseTestClass):
        pass
    class LevelTwoD(LevelOneD):
        pass
    class LevelThreeD(LevelTwoD):
        pass
    class LevelFourD(LevelThreeD):
        pass

    # Prepare unittest

# Generated at 2022-06-12 22:49:44.961257
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test get_all_subclasses utility

    test_get_all_subclasses creates a test class hierarchy.  Then it calls get_all_subclasses on
    the top-level test class.  It compares the results of get_all_subclasses to a list of all of
    the test classes.  If the two lists are not equal, it raises an exception.

    Note: This function is a unittest for `get_all_subclasses`.  `get_all_subclasses` does not need
    to be tested in an integration test, so it can be tested here.
    '''
    class TestClass0(object):
        pass
    class TestClass1(TestClass0):
        pass
    class TestClass2(TestClass0):
        pass
    class TestClass3(TestClass1):
        pass

# Generated at 2022-06-12 22:50:06.612474
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass

    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:50:17.223221
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test case for :py:func:`get_all_subclasses`

    Here we create a class inheritance tree with the following structure::

        TestClass1
         |     |
         |     +- TestClass2
         |     |  |
         |     |  +- TestClass3
         |     |
         |     +- TestClass4
         |
        TestClass5

    We then assert that the output of :py:func:`get_all_subclasses` is equivalent to::

        [<class '__main__.TestClass2'>, <class '__main__.TestClass3'>, <class '__main__.TestClass4'>]
    '''
    class TestClass1(object):
        pass

    class TestClass2(TestClass1):
        pass


# Generated at 2022-06-12 22:50:24.683546
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This is a unit test to ensure that the :py:meth:`get_all_subclasses` method works as expected.

    It uses a few classes to test it as follows:

    * ``A`` is the parent class.
    * ``B`` is a child of ``A``.
    * ``C`` is a child of ``A``.
    * ``D`` is a child of ``B``.

    Given this set of classes, the :py:meth:`get_all_subclasses` method should return ``B``,
    ``C``, and ``D``.  It should not return ``A``.  This test ensures that happens.
    '''
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass


# Generated at 2022-06-12 22:50:27.830445
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.plugins.action.normal import ActionModule as ActionModule
    from ansible.plugins.action.copy import ActionModule as CopyActionModule
    from ansible.plugins.action.shell import ActionModule as ShellActionModule
    from ansible.plugins.action.template import ActionModule as TemplateActionModule

    assert get_all_subclasses(ActionModule) == set([CopyActionModule, ShellActionModule, TemplateActionModule])

# Generated at 2022-06-12 22:50:34.274082
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test function for get_all_subclasses

    :rtype: bool
    :return: True if the test is completed without any error
    '''
    class A(object):
        ''' Class A '''
    class B(A):
        ''' Class B which inherits from A '''
    class C(B):
        ''' Class C which inherits from B '''
    class D(C):
        ''' Class D which inherits from C '''
    class E(D):
        ''' Class E which inherits from D '''
    class F(object):
        ''' Class F '''
    class G(F):
        ''' Class G which inherits from F '''
    all_classes = get_all_subclasses(A)
    assert E in all_classes
    assert F not in all

# Generated at 2022-06-12 22:50:42.066795
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
    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])
    assert set(get_all_subclasses(B)) == set([D, F])
    assert set(get_all_subclasses(C)) == set([E])
    assert set(get_all_subclasses(D)) == set([F])
    assert set(get_all_subclasses(E)) == set()
    assert set(get_all_subclasses(F)) == set()


# Generated at 2022-06-12 22:50:46.707991
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

    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 4
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses

# Generated at 2022-06-12 22:50:54.198803
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        '''
        A class with no subclass.
        '''
        pass

    class B(object):
        '''
        A class with three subclasses.
        '''
        pass

    class B1(B):
        '''
        Subclass of class B.
        '''
        pass

    class B2(B):
        '''
        Subclass of class B.
        '''
        pass

    class B3(B):
        '''
        Subclass of class B.
        '''
        pass

    class D(object):
        '''
        A class with two subclasses.
        '''
        pass

    class D1(D):
        '''
        Subclass of class D.
        '''
        pass


# Generated at 2022-06-12 22:50:59.642842
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
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    all_subclasses = get_all_subclasses(A)
    assert all_subclasses == set([B, C, D, E])