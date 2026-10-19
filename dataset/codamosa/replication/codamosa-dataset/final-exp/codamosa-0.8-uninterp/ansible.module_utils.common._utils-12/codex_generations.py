

# Generated at 2022-06-12 22:41:09.393221
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.plugins.action import ActionBase

    subclasses = get_all_subclasses(ActionBase)
    assert len(subclasses) > 0
    assert 'Command' in [t.__name__ for t in subclasses]

# Generated at 2022-06-12 22:41:15.436861
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

    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set([])

# Generated at 2022-06-12 22:41:22.879505
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Sample class to get all subclasses
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

    class G(D):
        pass

    subclasses = get_all_subclasses(A)
    assert B in subclasses and C in subclasses and \
           D in subclasses and E in subclasses and \
           F in subclasses and G in subclasses

# Generated at 2022-06-12 22:41:26.737973
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Animal(object):
        pass

    class Dog(Animal):
        pass

    class Cat(Animal):
        pass

    class Labrador(Dog):
        pass

    assert Labrador in get_all_subclasses(Animal)

# Generated at 2022-06-12 22:41:36.469926
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test for get_all_subclasses()

    This function creates a simple class hierarchy and makes sure that
    get_all_subclasses() returns the expected class hierarchy
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
    class F(E):
        pass
    class G(D):
        pass
    class H(G):
        pass
    class I(H):
        pass
    class J(I):
        pass
    class K(B):
        pass
    class L(B):
        pass
    class M(K):
        pass
    class N(L):
        pass
    class O(N):
        pass

# Generated at 2022-06-12 22:41:39.759582
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert AnsibleUnsafeText in get_all_subclasses(str)
    assert TaskQueueManager in get_all_subclasses(TaskQueueManager)


# Generated at 2022-06-12 22:41:46.085051
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class a: pass
    class a1(a): pass
    class a2(a): pass
    class a3(a1): pass
    class b(a3): pass
    class c: pass
    class c1(c): pass
    class x(c): pass
    class y(x): pass
    assert get_all_subclasses(a) == set([a1, a2, a3, b])
    assert get_all_subclasses(c) == set([c1, x, y])
    assert get_all_subclasses(a3) == set([b])

# Generated at 2022-06-12 22:41:52.443768
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

    class G(E):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set()
    assert set(get_all_subclasses(C)) == set([D])
    assert set(get_all_subclasses(D)) == set()
    assert set(get_all_subclasses(E)) == set([F, G])
    assert set(get_all_subclasses(F)) == set()
    assert set(get_all_subclasses(G)) == set

# Generated at 2022-06-12 22:41:55.103423
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class B1(B): pass
    class B2(B): pass
    class C1(C): pass
    class C2(C): pass
    class C3(C): pass

    assert set(get_all_subclasses(A)) == set([B, C, B1, B2, C1, C2, C3])

# Generated at 2022-06-12 22:42:04.382486
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Defining a class tree
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
    class J(F):
        pass
    class K(G):
        pass
    class L(I):
        pass

    # Testing result
    assert (get_all_subclasses(A) == set([B, C, D, E, F, G, H, I, J, K, L]))
    assert (get_all_subclasses(B) == set([D, G, K]))

# Generated at 2022-06-12 22:42:12.206857
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

    class G(D):
        pass

    assert set([B, C, D, E, G]) == get_all_subclasses(A)



# Generated at 2022-06-12 22:42:16.692645
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert get_all_subclasses(A) == set([B, C])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(object) == set([A, B, C])

# Generated at 2022-06-12 22:42:22.426394
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Foo(object):
        def __init__(self):
            pass

    class Bar(Foo):
        def __init__(self):
            pass

    class Baz(Foo):
        def __init__(self):
            pass

    class Hi(Bar, Baz):
        def __init__(self):
            pass

    assert(set(get_all_subclasses(Foo)) == {Bar, Baz, Hi})

# Generated at 2022-06-12 22:42:28.798878
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TestException(Exception):
        pass

    class TestClass(object):
        pass

    class TestClassChild(TestClass):
        pass

    class TestExceptionChild(TestException):
        pass

    assert TestClass in get_all_subclasses(object)
    assert TestException in get_all_subclasses(Exception)
    assert TestClassChild in get_all_subclasses(TestClass)
    assert TestExceptionChild in get_all_subclasses(TestException)

# Generated at 2022-06-12 22:42:36.289684
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses
    '''
    class Foo(object):
        pass
    class Foo1(Foo):
        pass
    class Foo11(Foo1):
        pass
    class Foo12(Foo1):
        pass
    class Foo2(Foo):
        pass
    class Foo21(Foo2):
        pass
    class Foo22(Foo2):
        pass
    class Foo23(Foo2):
        pass
    class Foo3(Foo):
        pass

    classes = get_all_subclasses(Foo)
    assert len(classes) == 8

# Generated at 2022-06-12 22:42:47.219721
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # We define a class hierarchy as following
    #
    #     A
    #    /  \
    #   B    C
    #  /  \
    # D    E
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

    # Then we assert on the computed result
    # We get a set of classes
    result = set(get_all_subclasses(A))
    assert result == {B, C, D, E}

    # We get a set of classes
    result = set(get_all_subclasses(B))
    assert result == {D, E}

    # We get a set of classes
    result = set(get_all_subclasses(C))


# Generated at 2022-06-12 22:42:57.831187
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for :py:func:`get_all_subclasses`
    '''
    import types

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

    # Checking input of None
    try:
        types.FunctionType(get_all_subclasses, None)
        raise AssertionError("an exception should be raised")
    except TypeError:
        pass

    # Checking input of int
    try:
        types.FunctionType(get_all_subclasses, 1)
        raise AssertionError("an exception should be raised")
    except TypeError:
        pass

    # Checking input of function

# Generated at 2022-06-12 22:43:07.325660
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Defining three classes
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    assert A not in get_all_subclasses(A)
    assert A in get_all_subclasses(B)
    assert A in get_all_subclasses(C)
    assert B in get_all_subclasses(A)
    assert B in get_all_subclasses(B)
    assert B in get_all_subclasses(C)
    assert C in get_all_subclasses(A)
    assert C in get_all_subclasses(B)
    assert C in get_all_subclasses(C)

# Generated at 2022-06-12 22:43:18.533652
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''Unit test for function :py:func:`get_all_subclasses`'''
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(D): pass
    class G(D): pass
    class H(D): pass
    # No A's subclasses should be found
    assert get_all_subclasses(A) == set()
    # Only A's subclasses should be found
    assert get_all_subclasses(A) == set([B, C])
    # Only A's direct subclasses should be found
    assert set(A.__subclasses__()) == set([B, C])
    # Only B's subclasses should be found

# Generated at 2022-06-12 22:43:23.195918
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
    assert get_all_subclasses(B) == set([D])
    assert get_all_subclasses(C) == set([D, E])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:43:33.789097
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

    class G(E):
        pass

    all_subclasses = get_all_subclasses(A)
    assert set(all_subclasses) == {B, C, D, E, F, G}

    all_subclasses = get_all_subclasses(B)
    assert set(all_subclasses) == {D, F}

#
# Wrapper for ansible.vars.hostvars.get_hostvars()
#



# Generated at 2022-06-12 22:43:45.298085
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
    class F(B):
        pass
    class G(C):
        pass
    class H(E):
        pass

    assert get_all_subclasses(A) == set([B, D, F, G, H, C, E])
    assert get_all_subclasses(B) == set([C, F, G])
    assert get_all_subclasses(C) == set([G])
    assert get_all_subclasses(D) == set([E, H])
    assert get_all_subclasses(E) == set([H])
    assert get_all_subclasses(F) == set([G])

# Generated at 2022-06-12 22:43:53.538852
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

    assert get_all_subclasses(A) == set([B, C, D, E, F])
    assert get_all_subclasses(B) == set([])
    assert get_all_subclasses(C) == set([D, E, F])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([F])
    assert get_all_subclasses(F) == set([])

# Generated at 2022-06-12 22:43:59.733308
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base(object):
        pass
    class LevelOne(Base):
        pass
    class LevelTwo(LevelOne):
        pass
    class LevelThree(LevelTwo):
        pass
    subclasses = get_all_subclasses(Base)
    assert len(subclasses) == 3
    assert LevelOne in subclasses
    assert LevelTwo in subclasses
    assert LevelThree in subclasses

# Generated at 2022-06-12 22:44:09.265735
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
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

    class F(D):
        pass

    class G(D):
        pass

    class H(F):
        pass

    assert(get_all_subclasses(A) == {D, E, F, G, H})
    assert(get_all_subclasses(B) == set())
    assert(get_all_subclasses(C) == set())
    assert(get_all_subclasses(D) == {F, G, H})
    assert(get_all_subclasses(E) == set())
    assert(get_all_subclasses(F) == {H})

# Generated at 2022-06-12 22:44:16.843463
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Create a minimal class hierarchy sample
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

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([E])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:44:22.304399
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

    class E(C):
        pass

    class F(C):
        pass

    class G(D):
        pass
    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G])

# Generated at 2022-06-12 22:44:30.440934
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

    assert set(get_all_subclasses(A)) == set([B,C,D,E])
    assert set(get_all_subclasses(B)) == set([D,E])
    assert set(get_all_subclasses(C)) == set([])
    assert set(get_all_subclasses(D)) == set([])
    assert set(get_all_subclasses(E)) == set([])

# Generated at 2022-06-12 22:44:37.037125
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A: pass

    class B(A): pass

    class C(A): pass

    class D(B, C): pass

    class E(D): pass

    classes = get_all_subclasses(A)

    assert len(classes) == 4
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes

    classes = get_all_subclasses(B)

    assert len(classes) == 2
    assert D in classes
    assert E in classes

# Generated at 2022-06-12 22:44:40.169287
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(object): pass
    class D(C): pass
    class E(B, D): pass
    class F(A): pass
    assert(set(get_all_subclasses(A)) == set([B, E, F]))




# Generated at 2022-06-12 22:44:54.295822
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

    class H(D):
        pass

    class I(F):
        pass

    class J(F, H):
        pass

    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 9, "get_all_subclasses(A) should return a set of 9 elements"

# Generated at 2022-06-12 22:45:01.166666
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for :func:`~_utils.get_all_subclasses`.

    This function is a unit test for the :func:`~_utils.get_all_subclasses` function.  When
    run, it will produce no output if the test passes.  If the test fails, an
    :exc:`AssertionError` will be generated.
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

    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:45:07.285713
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils.basic import AnsibleModule
    module_classes = get_all_subclasses(AnsibleModule)
    try:
        # This is for Python 2.6 and 2.7
        from _module import AnsibleModule_shell
    except ImportError:
        from _ansible_module import AnsibleModule_shell
    assert AnsibleModule_shell in module_classes


# Generated at 2022-06-12 22:45:11.726662
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

    ans = set([B, D, C])
    assert ans == get_all_subclasses(A)
    assert set([D]) == get_all_subclasses(B)
    assert set([]) == get_all_subclasses(C)
    assert set([]) == get_all_subclasses(D)
    assert set([]) == get_all_subclasses(D)

# Generated at 2022-06-12 22:45:21.163735
# Unit test for function get_all_subclasses
def test_get_all_subclasses(): # noqa
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

    def class_names(classes):
        return set((cls.__name__ for cls in classes))

    assert class_names(get_all_subclasses(A)) == set(['B', 'C', 'D', 'E'])
    assert class_names(get_all_subclasses(B)) == set(['C'])
    assert class_names(get_all_subclasses(E)) == set([])
    assert class_names(get_all_subclasses(object)) == set([])

# Generated at 2022-06-12 22:45:29.627677
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

    class H(object):
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

    class N(L):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set([D])

# Generated at 2022-06-12 22:45:39.256037
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
    class E(D):
        pass
    class F(D):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])
    assert set(get_all_subclasses(B)) == set([])
    assert set(get_all_subclasses(C)) == set([D, E, F])
    assert set(get_all_subclasses(D)) == set([E, F])
    assert set(get_all_subclasses(E)) == set([])
    assert set(get_all_subclasses(F)) == set([])



# Generated at 2022-06-12 22:45:47.289865
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Basic API unit test to determine if an iterable of classes is returned.
    This unit test creates a few classes with a simple inheritance model:

    A > B
      > C > D
      > E > F > G
        > H

    The expected result is that get_all_subclasses returns the
    expected list of classes.
    '''
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
    class F(E):
        pass
    class G(F):
        pass
    class H(F):
        pass

    result = get_all_subclasses(A)
    assert set(result) == set([B, C, D, E, F, G, H])

# Generated at 2022-06-12 22:45:56.612474
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    This test is unit test for function get_all_subclasses
    """

    class A():
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(B):
        pass

    class F(B):
        pass

    class G(B):
        pass

    class H(B):
        pass

    class I(H):
        pass


    class J(I):
        pass

    class K(J):
        pass

    class L(K):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I, J, K, L])

# Generated at 2022-06-12 22:46:06.897530
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    A dummy set of classes to test the get_all_subclasses function

    :py:class:`A` is the first class in the set of classes to test.  :py:class:`B` extends
    :py:class:`A`, and :py:class:`C` extends :py:class:`B`.  :py:class:`D` and :py:class:`E`
    both extend :py:class:`A`.

    The resulting set of subclasses should be ``{B, C, D, E}``.
    """
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

# Generated at 2022-06-12 22:46:20.060784
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Creating a complex tree
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
    class F(E):
        pass
    class G(A):
        pass
    class H(C):
        pass
    class I(D):
        pass
    class J(G):
        pass
    # Get the right result
    assert set([D, E, F, G, I, J]) == get_all_subclasses(A)
    assert set([A, B, C, D, E, F, G, H, I, J]) == get_all_subclasses(object)
    assert set([A, H, D, E, F, G, I, J]) == get_

# Generated at 2022-06-12 22:46:26.345808
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
    # Checking result is OK
    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    # Checking there is no other additional classes in result
    assert len(get_all_subclasses(A)) == 4

# Generated at 2022-06-12 22:46:34.893436
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import Iterable
    from ansible.module_utils._text import to_bytes, to_native
    # Defining a class which will be used as a parent class
    class A:
        pass
    # Defining a class which will be used as child class
    class B(A):
        pass
    # Defining a class which will be used as grandchild class
    class C(B):
        pass
    # Defining a class which will be used as great-grandchild class
    class D(C):
        pass
    # Defining a class which will be used as sibling class
    class E(A):
        pass
    # Defining a class which will be used as cousin class
    class F(E):
        pass
    # Defining a class which will be used as grandcousin class
    class G(F):
        pass

# Generated at 2022-06-12 22:46:40.252288
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

    sub_classes_from_a = get_all_subclasses(A)
    assert sub_classes_from_a == {B, C, D, E}

    sub_classes_from_e = get_all_subclasses(E)
    assert sub_classes_from_e == set()

# Generated at 2022-06-12 22:46:44.426933
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
    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H])

# Generated at 2022-06-12 22:46:55.286948
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Check with a simple hierarchy
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

    all_classes = get_all_subclasses(A)
    assert len(all_classes) == 5
    print('Classes:\n  ' + '\n  '.join([str(i) for i in all_classes]))
    assert all((A, B, C, D, E) == all_classes)
    print('SUCCESS: get_all_subclasses works great on 3-level hierarchy')

    # Check with a 4-level hierarchy
    class A2(object):
        pass

    class B2(A2):
        pass



# Generated at 2022-06-12 22:47:02.707395
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a class with two subclasses
    class A(object): pass
    class B(A): pass
    class C(A): pass

    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)

    # Create a class with a subclasses which has a subclass
    class D(object): pass
    class E(D): pass
    class F(E): pass

    assert D in get_all_subclasses(D)
    assert E in get_all_subclasses(D)
    assert F in get_all_subclasses(D)

    # Create a class with subclasses which has a subclass which has a subclass
    class G(object): pass
    class H(G): pass
    class I(H): pass

# Generated at 2022-06-12 22:47:11.984176
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Test classes
    class Test(object): pass
    class Test2(object): pass
    class Test3(object): pass
    class Test4(object): pass
    class Test5(object): pass
    class Test6(object): pass
    class Test7(object): pass
    class SubTest2(Test2): pass
    class SubTest3(Test3): pass
    class SubTest4(Test4): pass
    class SubTest5(Test5): pass
    class SubTest6(Test6): pass
    class SubTest7(Test7): pass
    class SubSubTest2(SubTest2): pass
    class SubSubTest3(SubTest3): pass
    class SubSubTest4(SubTest4): pass
    class SubSubTest5(SubTest5): pass
    class SubSubTest6(SubTest6): pass
   

# Generated at 2022-06-12 22:47:18.932802
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

    class F(C):
        pass

    # This is a class hierarchy in which the structure is:
    #
    # A
    # |- B
    # |- C
    #    |- D
    #    |  |- E
    #    |- F
    #
    # So the bottom-up order of subclasses should be [E, D, F, C, B, A]
    assert [x.__name__ for x in get_all_subclasses(A)] == ['E', 'D', 'F', 'C', 'B']

# Generated at 2022-06-12 22:47:22.544276
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

    expected = set([A, B, C, D])
    assert expected == get_all_subclasses(A)

# Generated at 2022-06-12 22:47:37.269528
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import ansible

    find_test_module = None
    for module_loader, path, _ in ansible.plugins.module_loader._get_all_plugin_loaders():
        if path.endswith('/test_utils/modules'):
            find_test_module = True
            break
    assert find_test_module, "Unable to find a valid path to test modules"

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set([D])
    assert set(get_all_subclasses(C)) == set()

# Generated at 2022-06-12 22:47:40.759000
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
    assert get_all_subclasses(A) == set([B, D, C, E])

# Generated at 2022-06-12 22:47:47.538155
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def _assert_unique_classes(classes):
        classes_names = [cls.__name__ for cls in classes]
        assert len(classes_names) == len(set(classes_names))

    def _assert_no_child(child, parents):
        for parent in parents:
            assert child not in parent.__subclasses__()

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

    class F:
        pass

    class G(F):
        pass

    class H:
        pass

    assert get_all_subclasses(A) == {B, C, E, D}
    assert get_all_subclasses(B) == {C, E}

# Generated at 2022-06-12 22:47:57.360837
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Test class which are the subclass of list
    class a(list): pass
    class b(list): pass
    class c(list): pass
    class e(list): pass
    # Test class which are the subclass of a
    class a_1(a): pass
    class a_2(a): pass
    class a_3(a): pass
    class c_1(c): pass
    class c_2(c): pass
    class c_3(c): pass
    # Test that a, b and c are the subclasses of list
    assert(set([a, b, c, e]) == get_all_subclasses(list))
    # Test that a_1, a_2, a_3 are the subclasses of a

# Generated at 2022-06-12 22:48:04.541352
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Testing get_all_subclasses function
    """
    class MainClass(object):
        '''
        Main class
        '''
    class ChildClass1(MainClass):
        '''
        Child class 1 from MainClass
        '''
    class ChildClass2(MainClass):
        '''
        Child class 2 from MainClass
        '''
        class GrandChildClass1(ChildClass2):
            '''
            Grandchild class 1 from ChildClass2
            '''
        class GrandChildClass2(ChildClass2):
            '''
            Grandchild class 2 from ChildClass2
            '''
            class GreatGrandChildClass1(GrandChildClass2):
                '''
                Great grandchild class 1 from GrandChildClass2
                '''

    # Check function execution

# Generated at 2022-06-12 22:48:10.172541
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''Test function get_all_subclasses.

    A class 'A' has 4 subclasses: 'B', 'C', 'D', 'E'.
    Subclasses 'B', 'C' do not have children and 'D' has one subclass 'F'.
    '''
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(A):
        pass

    class E(A):
        pass

    class F(D):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:48:15.402584
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

    class E(C, D):
        pass

    class F(A):
        pass

    classes = get_all_subclasses(object)
    for c in [A, B, C, D, E, F]:
        assert c in classes

# Test imports

# Generated at 2022-06-12 22:48:22.338829
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
    class F(object):
        pass
    res = get_all_subclasses(A)
    reference = {B, C, D, E}
    assert (res == reference)



# Generated at 2022-06-12 22:48:28.022951
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test get_all_subclasses
    '''
    class A:
        pass

    # a1 is a direct subclass of A
    class a1(A):
        pass

    # a2 is a direct subclass of a1
    class a2(a1):
        pass

    # a3 is a direct subclass of a2
    class a3(a2):
        pass

    # A has 3 subclasses
    assert len(get_all_subclasses(A)) == 3
    for subclass in get_all_subclasses(A):
        # Each subclass is a subclass of A
        assert issubclass(subclass, A)

# Generated at 2022-06-12 22:48:36.461836
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

    class E(D):
        pass

    class F(object):
        pass

    class G(F):
        pass

    a, b, c, d, e, f, g = A(), B(), C(), D(), E(), F(), G()

    assert set(a.__subclasses__()) == set([b, c])
    assert set(b.__subclasses__()) == set([d])
    assert set(c.__subclasses__()) == set()
    assert set(d.__subclasses__()) == set([e])
    assert set(e.__subclasses__()) == set()

# Generated at 2022-06-12 22:48:53.480971
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

    subclasses = get_all_subclasses(object)
    assert A in subclasses
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses

# Generated at 2022-06-12 22:48:58.392925
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A():
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D():
        pass

    assert set([B, C]) == get_all_subclasses(A)
    assert set([C]) == get_all_subclasses(B)
    assert set([]) == get_all_subclasses(C)
    assert set([]) == get_all_subclasses(D)

# Generated at 2022-06-12 22:49:06.841706
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This function provides a unit test to verify that get_all_subclasses() works as expected

    Classes are defined below in alphabetical order.  The correct set of subclasses will be
    retrieved by calling get_all_subclasses(), and that set will be compared to the set of subclasses
    defined below.

    :raises AssertionError: If the set of classes retrieved is incorrect
    '''
    class A():
        pass

    class B():
        pass

    class C():
        pass

    class D():
        pass

    class E():
        pass

    class F():
        pass

    class G(A):
        pass

    class H(B):
        pass

    class I(H):
        pass

    class J(C, D, E):
        pass

    class K(F):
        pass

   

# Generated at 2022-06-12 22:49:11.762222
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
    class F(B, C):
        pass
    class G(C):
        pass
    class H(C):
        pass
    class I(D):
        pass
    class J(D):
        pass
    assert set(get_all_subclasses(A)) == set((B, C, D, E, F, G, H, I, J))
test_get_all_subclasses()

# Generated at 2022-06-12 22:49:16.877738
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(object): pass
    classes = get_all_subclasses(A)
    assert len(list(classes)) == 3
    assert B in classes
    assert C in classes
    assert D in classes
    assert E not in classes

# Generated at 2022-06-12 22:49:21.286219
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)



# Generated at 2022-06-12 22:49:28.233553
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def get_all_subclasses_test_classes():
        class A(): pass
        class B(A): pass
        class C(A): pass
        class D(B): pass
        class E(B): pass
        class F(C): pass
        class G(C): pass
        class H(D): pass
        class I(D): pass
        class J(E): pass
        class K(E): pass
        yield A, [B, C, D, E, F, G, H, I, J, K]
        yield B, [D, E, H, I, J, K]
        yield C, [F, G]
        yield D, [H, I]
        yield E, [J, K]
        yield F, []
        yield G, []
        yield H, []
        yield I, []
       

# Generated at 2022-06-12 22:49:33.356178
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
    class G(D):
        pass
    class H(G):
        pass

    all_subclasses = get_all_subclasses(A)
    assert A in all_subclasses
    assert B in all_subclasses
    assert C in all_subclasses
    assert D in all_subclasses
    assert E in all_subclasses
    assert F in all_subclasses
    assert G in all_subclasses
    assert H in all_subclasses


# TODO: only used by one module, consider moving to that module

# Generated at 2022-06-12 22:49:38.109872
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

    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert E in get_all_subclasses(A)
    assert F in get_all_subclasses(A)
    assert len(get_all_subclasses(A)) == 6

# Generated at 2022-06-12 22:49:45.034470
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text

    class C1(object):
        pass

    class C2(C1):
        pass

    class C3(C1):
        pass

    class C4(C2):
        pass

    class C5(C2):
        pass

    assert_result = set([AnsibleModule, C1, C2, C3, C4, C5])
    result = get_all_subclasses(AnsibleModule)
    assert set([to_text(c) for c in result]) == assert_result

# Generated at 2022-06-12 22:50:18.798811
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    a_class = type('AClass', (), {})
    b_class = type('BClass', (a_class,), {})
    c_class = type('CClass', (), {})
    d_class = type('DClass', (b_class,), {})
    e_class = type('EClass', (d_class,), {})
    assert get_all_subclasses(a_class) == set([b_class, d_class, e_class])
    assert get_all_subclasses(c_class) == set()

# Generated at 2022-06-12 22:50:25.216478
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This function tests if get_all_subclasses works as expected.
    '''

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

    # Check the case where is no subclasses
    assert len(get_all_subclasses(A)) == 2
    assert len(get_all_subclasses(B)) == 2
    assert len(get_all_subclasses(C)) == 1
    assert len(get_all_subclasses(D)) == 1

if __name__ == '__main__':
    test_get_all_subclasses()

# Generated at 2022-06-12 22:50:27.209341
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(D): pass

    assert set(get_all_subclasses(A)) == set([C, D, E, B])

# Generated at 2022-06-12 22:50:30.183699
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

    classes = get_all_subclasses(A)
    assert set(classes) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:50:36.911948
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    
    class A(): pass
    class B(A): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(B): pass
    class G(C): pass
    class H(C): pass
    class I(D): pass
    class J(E): pass
    class K(I): pass

    subclasses = get_all_subclasses(A)
    assert not A in subclasses
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses
    assert G in subclasses
    assert H in subclasses
    assert I in subclasses
    assert J in subclasses
    assert K in subclasses

# Generated at 2022-06-12 22:50:45.780262
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class MyClassOne(object):
        pass
    class MyClassTwo(object):
        pass
    class MyClassThree(MyClassOne):
        pass
    class MyClassFour(MyClassTwo):
        pass
    class MyClassFive(MyClassThree):
        pass
    class MyClassSix(object):
        pass

    assert get_all_subclasses(MyClassOne) == {MyClassThree, MyClassFive}
    assert get_all_subclasses(MyClassTwo) == {MyClassFour}
    assert get_all_subclasses(MyClassSix) == set()

# Generated at 2022-06-12 22:50:53.269683
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class E(B):
        pass
    class F(B):
        pass
    class D(C):
        pass
    assert(A in get_all_subclasses(A))
    assert(B in get_all_subclasses(A))
    assert(C in get_all_subclasses(A))
    assert(D in get_all_subclasses(A))
    assert(E in get_all_subclasses(A))
    assert(F in get_all_subclasses(A))
    assert(A not in get_all_subclasses(B))
    assert(B in get_all_subclasses(B))
    assert(C not in get_all_subclasses(B))

# Generated at 2022-06-12 22:51:01.720933
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest

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

    class F(B, C, E):
        pass

    class G(C):
        pass

    class H(F, G):
        pass

    class I(H):
        pass

    class J(I):
        pass

    class K(I):
        pass

    class L(J, B):
        pass

    class M(B, L, K):
        pass

    H_subclasses = get_all_subclasses(H)
    assert len(H_subclasses) == 6
    assert H in H_subclasses
    assert I in H_subclasses
    assert J in H

# Generated at 2022-06-12 22:51:06.222816
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # define parent class
    class A(object):
        pass

    # define children class
    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    class E(B):
        pass

    class F(E):
        pass

    subclasses = get_all_subclasses(A)
    assert (B in subclasses)
    assert (C in subclasses)
    assert (D in subclasses)
    assert (E in subclasses)
    assert (F in subclasses)