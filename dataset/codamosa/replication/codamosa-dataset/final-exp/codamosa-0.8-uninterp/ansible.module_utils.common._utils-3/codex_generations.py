

# Generated at 2022-06-12 22:41:12.564760
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    if __name__ == '__main__':
        class A(object):
            pass


        class Ba(A):
            pass


        class Bb(A):
            pass


        class Bba(Bb):
            pass


        class Bbb(Bb):
            pass


        classes = get_all_subclasses(A)

        assert(A in classes)
        assert(Ba in classes)
        assert(Bb in classes)
        assert(Bba in classes)
        assert(Bbb in classes)



# Generated at 2022-06-12 22:41:17.067440
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class a:
        pass
    class b:
        pass
    class c(b):
        pass
    class d(c):
        pass
    class e(a):
        pass
    class f(e):
        pass
    r = [x for x in get_all_subclasses(a)]
    assert r == [e, f]

# Generated at 2022-06-12 22:41:21.549979
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Foo(object):
        pass
    class Bar(Foo):
        pass
    class Baz(Bar):
        pass
    class Slurms(Baz):
        pass
    assert get_all_subclasses(Foo) == {Bar, Baz, Slurms}

# Generated at 2022-06-12 22:41:32.714810
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(object): pass
    class C(object): pass
    class D(A, B): pass
    class E(A, B, C): pass
    class F(A, C): pass
    class G(object): pass
    class H(G): pass
    class I(H): pass
    class J(F, I): pass

    assert get_all_subclasses(object) == set()
    assert get_all_subclasses(A) == set([D, E, F, J])
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set([E, F])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()
    assert get

# Generated at 2022-06-12 22:41:38.088234
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

    class F(E):
        pass

    class G(E):
        pass

    class H:
        pass

    classes = get_all_subclasses(A)
    assert {B, C, D, E, F, G} == classes

    classes = get_all_subclasses(H)
    assert not classes


# Generated at 2022-06-12 22:41:46.578275
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

    class F:
        pass

    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F not in subclasses

# Import class from a string
#
# Example:
#
# from ansible.module_utils._text import to_native
# from ansible.module_utils._utils import import_class_or_module
#
# try:
#     my_obj = import_class_or_module(to_native(obj))
# except Exception as e:
#     module.fail_json(msg

# Generated at 2022-06-12 22:41:52.761954
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import types
    import unittest
    class A(object): pass
    class B(object): pass
    class C(A): pass
    class D(A): pass
    class E(C): pass
    class F(D, B): pass
    class G(F): pass

    class test_get_all_subclasses(unittest.TestCase):
        def test_multiple_parents(self):
            self.assertEqual(get_all_subclasses(object), set([types.TypeType]))
            self.assertEqual(get_all_subclasses(A), set([C, D, E]))
            self.assertEqual(get_all_subclasses(B), set())
            self.assertEqual(get_all_subclasses(C), set([E]))

# Generated at 2022-06-12 22:42:02.847473
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
    class E(D):
        pass
    class F(D):
        pass
    class G(A):
        pass
    # Check that order or insertion is not important
    assert set(get_all_subclasses(A)) == set((B, C, F, G, E, D))
    # Do not crash on classes with no subclasses
    assert get_all_subclasses(object) == []
    # Do not crash on a class with itself as subclass
    class H(H):
        pass
    assert get_all_subclasses(H) == []
    # Avoid infinite loop on class with subclass pointing to itself
    A.subclasses = [A]

# Generated at 2022-06-12 22:42:11.938217
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class a(object): pass
    class b(a): pass
    class c(a): pass
    class d(a): pass
    class e(b): pass
    class f(d): pass
    actual = get_all_subclasses(a)
    expected = {b, c, d, e, f}
    assert actual == expected
    # Test that get_all_subclasses return all classes
    assert len(actual) == len(expected)

# Testing of this module
if __name__ == '__main__':
    test_get_all_subclasses()

# Generated at 2022-06-12 22:42:17.612667
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
    class F(A):
        pass
    class G(object):
        pass

    classes = get_all_subclasses(object)
    assert A in classes
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F in classes
    assert G in classes
    assert len(classes) == 7

# Generated at 2022-06-12 22:42:26.540578
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

    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set([D])
    assert set(get_all_subclasses(C)) == set([])
    assert set(get_all_subclasses(D)) == set([])

# Generated at 2022-06-12 22:42:35.990155
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class a:
        pass
    class b:
        pass
    class c(a):
        pass
    class d(b):
        pass
    class e(d):
        pass

    assert get_all_subclasses(a) == {c}
    assert get_all_subclasses(b) == {d, e}
    assert get_all_subclasses(c) == set()
    assert get_all_subclasses(d) == {e}
    assert get_all_subclasses(e) == set()

    from ansible.plugins.action import ActionBase
    assert len(get_all_subclasses(ActionBase)) > 1
    from ansible.plugins.callback import CallbackBase
    assert len(get_all_subclasses(CallbackBase)) > 1


# Generated at 2022-06-12 22:42:47.085628
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        pass

    class A1(A):
        pass

    class A2(A):
        pass

    class A11(A1):
        pass

    class A111(A11):
        pass

    class A12(A1):
        pass

    class A121(A12):
        pass

    class A122(A12):
        pass

    class A21(A2):
        pass

    class A22(A2):
        pass

    class A23(A2):
        pass

    class A31(A3):
        pass

    classes = dict((c.__name__, c) for c in get_all_subclasses(A))
    assert len(classes) == 11
    assert A in classes
    assert A1 in classes
    assert A2 in classes
    assert A11

# Generated at 2022-06-12 22:42:53.313974
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a tree of classes
    class Base(object):
        pass

    class A(Base):
        pass

    class B(Base):
        pass

    class C(A):
        pass

    assert set([A, B, C]) == get_all_subclasses(Base)

    # Test if it works also on object
    assert get_all_subclasses(object) == set(Base.__subclasses__())

# Generated at 2022-06-12 22:43:01.536382
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Setup a python class structure for test
    class ParentClass(object):
        pass

    class ChildClass_1(ParentClass):
        pass

    class ChildClass_2(ParentClass):
        pass

    class GrandChildClass_1(ChildClass_1):
        pass

    class GrandChildClass_2(ChildClass_2):
        pass

    class GrandChildClass_3(ChildClass_2):
        pass

    class GrandGrandChildClass(GrandChildClass_3):
        pass

    subclasses = get_all_subclasses(ParentClass)

    class_object_list = []
    for _class in subclasses:
        class_object_list.append(_class.__name__)


# Generated at 2022-06-12 22:43:10.889814
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a class hierarchy
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(A): pass
    class E(B, C): pass
    class F(C, A): pass
    class G(E, F): pass
    # Test expected results
    assert get_all_subclasses(A) == {B, C, D, E, F, G}
    assert get_all_subclasses(B) == {E}
    assert get_all_subclasses(C) == {E, F}
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == {G}
    assert get_all_subclasses(F) == {G}
    assert get_all_subclasses(G) == set()

# Generated at 2022-06-12 22:43:18.796237
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Note that we can't just use a python module here, since the unit test will
    # be run with the module already imported
    class A: pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert not C in get_all_subclasses(D)
    assert not D in get_all_subclasses(C)
    assert not B in get_all_subclasses(C)

# Generated at 2022-06-12 22:43:20.926595
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass

    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:43:31.408531
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

    def assert_is_set_of(a, b):
        return len(a) == len(b) and all(x in a for x in b)

    assert_is_set_of(get_all_subclasses(A), {B, C, D, E, F, G})
    assert_is_set_of(get_all_subclasses(B), {D, E})
    assert_is_set_of(get_all_subclasses(C), {F, G})


# Generated at 2022-06-12 22:43:40.289814
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Create a mock module
    class MockModule:
        pass

    class MockModule1(MockModule):
        pass

    class MockModule2(MockModule):
        pass

    class MockModule3(MockModule1):
        pass

    class MockModule4(MockModule3):
        pass

    class MockModule5(MockModule4):
        pass

    # The set of all available subclasses should be
    # {MockModule1, MockModule2, MockModule3, MockModule4, MockModule5}
    assert set([MockModule1, MockModule2, MockModule3, MockModule4, MockModule5]) == set(get_all_subclasses(MockModule))



# Generated at 2022-06-12 22:43:48.128992
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

    classes = get_all_subclasses(A)
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes



# Generated at 2022-06-12 22:43:54.212581
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Sample python classes
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



# Generated at 2022-06-12 22:44:05.882293
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # define some dummy classes
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

    class F(D):
        pass

    class G(D):
        pass

    class H():
        pass

    class I(H):
        pass

    class J(H):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G]), "test 1 failed"
    assert get_all_subclasses(B) == set([D, E, F, G]), "test 2 failed"
    assert get_all_subclasses(C) == set([]), "test 3 failed"

# Generated at 2022-06-12 22:44:11.199745
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

    B in get_all_subclasses(A)
    D in get_all_subclasses(A)
    E in get_all_subclasses(A)
    F in get_all_subclasses(A)
    A not in get_all_subclasses(A)
    B not in get_all_subclasses(A)

# Generated at 2022-06-12 22:44:19.010107
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(object):
        pass

    class C(B):
        pass

    class D(C):
        pass

    class E(object):
        pass

    assert get_all_subclasses(A) == set()
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:44:22.499235
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
    for s in subclasses:
        assert issubclass(s, A)



# Generated at 2022-06-12 22:44:29.282868
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(C): pass

    assert get_all_subclasses(A) == set([B, C, D, E, F, G])
    assert get_all_subclasses(B) == set([D, E])
    assert get_all_subclasses(C) == set([F, G])


# Generated at 2022-06-12 22:44:35.407436
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass

    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set([])
    assert set(get_all_subclasses(C)) == set([D])
    assert set(get_all_subclasses(D)) == set([])

# Generated at 2022-06-12 22:44:39.955847
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Y(object):
        pass
    class X(object):
        pass
    class A(X):
        pass
    class B(X):
        pass
    class C(Y):
        pass
    class D(Y):
        pass
    class E(D):
        pass

    assert set(get_all_subclasses(X)) == set([A, B])
    assert set(get_all_subclasses(Y)) == set([C, D, E])



# Generated at 2022-06-12 22:44:50.224921
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

    assert get_all_subclasses(A) == set([A1, A2, A3, A11, A12, A21, A22])
    assert get_all_subclasses(A1) == set([A11, A12])
    assert get_all_subclasses(A11) == set([])
    class B: pass
    class C(B): pass
    try:
        get_all_subclasses(B)
    except TypeError:
        pass

# Generated at 2022-06-12 22:45:02.167827
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import pytest

    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass

    test_classes = set([A, B, C, D, E])
    assert test_classes == get_all_subclasses(A)
    assert get_all_subclasses(B) == set([B, D])
    assert get_all_subclasses(C) == set([C, E])
    assert get_all_subclasses(D) == set([D])
    assert get_all_subclasses(E) == set([E])
    with pytest.raises(AttributeError):
        assert get_all_subclasses(1) == set([])

# Generated at 2022-06-12 22:45:06.508023
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    subclasses = get_all_subclasses(A)
    assert len(subclasses) == 2
    assert B in subclasses
    assert C in subclasses

# Generated at 2022-06-12 22:45:11.745786
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
    class Child1(object):
        pass
    class Child2(object):
        pass
    class E(Child1, Child2):
        pass

    assert get_all_subclasses(A) == {B, C, D}, 'Failed to retrieve A\'s subclasses'
    assert get_all_subclasses(Child1) == {E}, 'Failed to retrieve Child1\'s subclasses'

# Generated at 2022-06-12 22:45:20.853582
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test unit for function get_all_subclasses
    '''
    class A:
        pass
    class B:
        pass
    class C(A):
        pass
    class D(A):
        pass
    class E(C, B):
        pass
    assert set(get_all_subclasses(A)) == set((C, D))
    assert set(get_all_subclasses(B)) == set((E,))
    assert set(get_all_subclasses(C)) == set((E,))
    assert set(get_all_subclasses(D)) == set((),)
    assert set(get_all_subclasses(E)) == set((),)

# Generated at 2022-06-12 22:45:24.752735
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

    classes = get_all_subclasses(A)
    assert A in classes
    assert B in classes
    assert C in classes
    assert D in classes

# Generated at 2022-06-12 22:45:31.758926
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """
    Test case for the get_all_subclasses function
    """

    # Create a test class hierarchy with no duplicate and ensure the function returns all of the
    # classes in the tree
    class Sub1(object):
        pass

    class Sub2(object):
        pass

    class Sub1Sub1(Sub1):
        pass

    class Sub2Sub1(Sub2):
        pass

    class Sub1Sub1Sub1(Sub1Sub1):
        pass

    class Sub2Sub1Sub1(Sub2Sub1):
        pass

    classes = get_all_subclasses(object)
    assert Sub1Sub1Sub1 in classes
    assert Sub2Sub1Sub1 in classes
    assert Sub2Sub1 in classes
    assert Sub1Sub1 in classes
    assert Sub1 in classes
    assert Sub2 in classes

   

# Generated at 2022-06-12 22:45:40.405121
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.utils._text import to_text
    class BaseClass(object):
        pass

    class DummyClassA(BaseClass):
        pass

    class DummyClassB(BaseClass):
        pass

    class DummyClassAA(DummyClassA):
        pass

    class DummyClassBA(DummyClassB):
        pass

    class DummyClassBB(DummyClassB):
        pass

    expected = set([DummyClassAA, DummyClassBA, DummyClassBB])
    actual = get_all_subclasses(BaseClass)
    assert(to_text(expected) == to_text(actual))


# Generated at 2022-06-12 22:45:45.975569
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

    class E(D):
        pass

    class F(A):
        pass

    # 6 subclasses A, B, C, D, E and F
    assert len(get_all_subclasses(A)) == 6

    # Test with an empty class
    class Test(object):
        pass

    assert len(get_all_subclasses(Test)) == 0



# Generated at 2022-06-12 22:45:49.753480
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
    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(C) == set([])

# Generated at 2022-06-12 22:45:59.923037
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(C): pass
    class H(D): pass

    assert get_all_subclasses(A) == set([B,C,D,E,F,G,H])
    assert get_all_subclasses(B) == set([D,E,H])
    assert get_all_subclasses(C) == set([F,G])
    assert get_all_subclasses(D) == set([H])
    assert get_all_subclasses(E) == set([])
    assert get_all_subclasses(F) == set([])
    assert get_all_subclasses(G) == set([])
   

# Generated at 2022-06-12 22:46:11.362029
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

    class E(D):
        pass

    all_subclasses = get_all_subclasses(A)

    assert A in all_subclasses
    assert B in all_subclasses
    assert C in all_subclasses
    assert D in all_subclasses
    assert E in all_subclasses

# Generated at 2022-06-12 22:46:14.422998
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

    assert get_all_subclasses(A) == set([B, D, C])
    assert get_all_subclasses(object) == set([type])

# Generated at 2022-06-12 22:46:21.308862
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Tests the get_all_subclasses function with a simple class hierarchy

    :rtype: bool
    :return: True if the test passes, False otherwise.
    '''
    # Define a dummy class hierarchy to test get_all_subclasses function
    class RootClass(object):
        pass

    class Child1(RootClass):
        pass

    class SubChild1(Child1):
        pass

    class SubChild2(Child1):
        pass

    class SubChild3(SubChild1):
        pass

    class Child2(RootClass):
        pass

    class Child3(RootClass):
        pass

    class SubChild4(Child3):
        pass

    # Expected class hierarchy, ordered using depth first search algorithm

# Generated at 2022-06-12 22:46:29.128833
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a sample tree of class to test the function
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(F): pass

    # Test the function with the root class
    subclasses = get_all_subclasses(A)
    all = set([B, C, D, E, F, G])
    assert(subclasses == all)

    # Test the function with a child class
    subclasses = get_all_subclasses(C)
    all = set([F, G])
    assert(subclasses == all)

# Generated at 2022-06-12 22:46:37.608041
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test function get_all_subclasses to verify its behavior without external dependencies

    This function sets up a dummy hierarchy of classes with four levels, and has each class
    declare itself in an instance variable.  It then calls get_all_subclasses against the
    top-level class, and verifies that all of the classes in the hierarchy have been found.
    '''
    # Define a dummy class hierarchy of four levels
    class A(object):
        declared = None
        def __init__(self):
            A.declared = A.declared + 1
    class B(A):
        def __init__(self):
            A.declared = A.declared + 1
    class C(B):
        def __init__(self):
            A.declared = A.declared + 1

# Generated at 2022-06-12 22:46:40.289972
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

# Generated at 2022-06-12 22:46:43.880956
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(E): pass
    assert list(get_all_subclasses(A)) == [B, C, D, E, F]
    assert list(get_all_subclasses(D)) == []

# Generated at 2022-06-12 22:46:54.603373
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

    class E(D):
        pass

    class F(E):
        pass

    class G:
        pass

    class H(G):
        pass

    # Ensure get_all_subclasses returns the expected classes
    assert set(map(lambda k: k.__name__, get_all_subclasses(A))) == set(['B', 'C', 'D', 'E', 'F'])
    assert set(map(lambda k: k.__name__, get_all_subclasses(G))) == set(['H'])
    # Ensure exceptions are raised for invalid classes

# Generated at 2022-06-12 22:47:02.454627
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define an example class hierarchy
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E(B, C):
        pass

    class F(B, D, E):
        pass

    class G:
        pass

    def __check_subclasses(cls, expected):
        """ Assert that get_all_subclasses() returns the expected list of
        classes.
        """
        actual = set(get_all_subclasses(cls))
        assert actual == expected

    __check_subclasses(object, {A, B, C, D, E, F})
    __check_subclasses(A, {B, C, D, E, F})

# Generated at 2022-06-12 22:47:11.714048
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses function
    '''
    import types

    class A(object):
        '''Class A'''
        pass

    class B(A):
        '''Class B'''
        pass

    class C(B):
        '''Class C'''
        pass

    class D(C):
        '''Class D'''
        pass

    class E(D):
        '''Class E'''
        pass

    class F(A):
        '''Class F'''
        pass

    class G(F):
        '''Class G'''
        pass

    class H(G):
        '''Class H'''
        pass

    class I(G):
        '''Class I'''
        pass


# Generated at 2022-06-12 22:47:22.189142
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
    class E(D):
        pass
    class F(C,D):
        pass
    class G(E,F):
        pass
    class H(C,E,F):
        pass
    class I(G,H):
        pass
    class J(I):
        pass
    class K(I):
        pass
    class L(J,K):
        pass
    assert get_all_subclasses(A) == set([B, C, F, G, H, I, J, K, L])


# Generated at 2022-06-12 22:47:31.160362
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
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:47:39.797938
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class A1(A): pass
    class A2(A): pass
    class A3(A): pass
    class A3a(A3): pass
    class A3b(A3): pass
    class A3b1(A3b): pass
    class A3b2(A3b): pass
    class A4(A): pass
    class A4a(A4): pass
    class A4b(A4): pass
    class A4b1(A4b): pass
    class A4b2(A4b): pass
    class A5(A): pass
    class A5a(A5): pass
    class A5b(A5): pass
    class A5b1(A5b): pass
    class A5b2(A5b): pass

# Generated at 2022-06-12 22:47:47.977898
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import collections
    import copy
    import types

    # Defining a sample class hierarchy
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(A):
        pass

    class E(B, C):
        pass

    class F(C, D):
        pass

    class G(E, F):
        pass

    # Testing get_all_subclasses function
    assert G in get_all_subclasses(A)
    assert F in get_all_subclasses(A)
    assert E in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert A in get_all

# Generated at 2022-06-12 22:47:52.502158
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(C): pass

    assert set(get_all_subclasses(A)) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:48:01.047350
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Test with a simple class
    class TestClass:
        pass
    class TestSubClassA(TestClass):
        pass
    class TestSubClassB(TestClass):
        pass
    subclasses = get_all_subclasses(TestClass)
    assert subclasses == {TestSubClassA, TestSubClassB}, "Error: get all subclasses %s" % subclasses

    # Test with multiple inheritance class
    class TestMultiInheritanceA:
        pass
    class TestMultiInheritanceB:
        pass
    class TestMultiInheritanceC(TestMultiInheritanceA, TestMultiInheritanceB):
        pass
    class TestMultiInheritanceD(TestMultiInheritanceA):
        pass
    subclasses = get_all_subclasses(TestMultiInheritanceA)

# Generated at 2022-06-12 22:48:06.071184
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass

    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert D in get_all_subclasses(B)
    assert D in get_all_subclasses(C)
    assert D in get_all_subclasses(D)

# Generated at 2022-06-12 22:48:12.704307
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Simple test to validate the function get_all_subclasses
    '''
    class NonGeneric(object):
        pass

    class Parent1(object):
        pass

    class Child1_1(Parent1):
        pass

    class Child1_2(Parent1):
        pass

    class Child1_1_1(Child1_1):
        pass

    class Parent2(object):
        pass

    class Child2_1(Parent2):
        pass

    class Child2_1_1(Child2_1):
        pass

    class GrandChild1_2_1(Child1_2):
        pass

    class GrandChild1_1_1_1(Child1_1_1):
        pass

    # Create a list of classes and sort it by name

# Generated at 2022-06-12 22:48:22.445022
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a class for test
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

    res = get_all_subclasses(A)
    assert res == set([B, C, D, E, F, G])
    res = get_all_subclasses(B)
    assert res == set([D, F])
    res = get_all_subclasses(C)
    assert res == set([E, G])

# Generated at 2022-06-12 22:48:28.185835
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    # D inherit from A and B
    class D(A, B):
        pass

    # E inherit from A and C
    class E(A, C):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])
    assert get_all_subclasses(B) == set([C, D])
    assert get_all_subclasses(C) == set([E])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:48:37.101298
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    assert len([c for c in get_all_subclasses(Exception)]) == 0
    assert len([c for c in get_all_subclasses(float)]) == 0

# Generated at 2022-06-12 22:48:41.360100
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class C(object):
        pass

    class D(C):
        pass

    class E(C):
        pass

    class F(D):
        pass

    class G(E):
        pass

    class H(G):
        pass

    class I(G):
        pass

    assert(set(get_all_subclasses(C)) == set([D, E, F, G, H, I]))

# Generated at 2022-06-12 22:48:44.888792
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(D): pass
    class G(E): pass
    return A, B, C, D, E, F, G


# Generated at 2022-06-12 22:48:52.061927
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass

    class B(A): pass
    class C(A): pass
    class D(A): pass

    class E(B): pass
    class F(B): pass
    class G(B): pass

    class H(C): pass
    class I(C): pass
    class J(C): pass

    class K(D): pass
    class L(D): pass
    class M(D): pass

    class N(E): pass
    class O(E): pass
    class P(E): pass

    l = [N, O, P, E, F, G, B, H, I, J, C, K, L, M, D, A]
    ret = get_all_subclasses(A)

# Generated at 2022-06-12 22:48:55.299680
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    assert(set([B, C, D, E]) == get_all_subclasses(A))


# Generated at 2022-06-12 22:49:03.214781
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Helper classes
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

# Generated at 2022-06-12 22:49:08.186797
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Creating class hierarchy
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

    # Collecting subclasses
    subclasses = get_all_subclasses(A)
    # Checking result
    assert len(subclasses) == 6
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses



# Generated at 2022-06-12 22:49:17.374521
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
    # Build list of all classes to test

# Generated at 2022-06-12 22:49:22.966140
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a class hierarchy
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
    subclasses = get_all_subclasses(A)
    assert B in subclasses
    assert C in subclasses
    assert D in subclasses
    assert E in subclasses
    assert F in subclasses



# Generated at 2022-06-12 22:49:27.195662
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TestA(object):
        pass

    class TestB1(TestA):
        pass

    class TestB2(TestA):
        pass

    class TestC1(TestB1):
        pass

    class TestC2(TestB1):
        pass

    class TestD(TestB2):
        pass

    assert get_all_subclasses(TestA) == set([TestB1, TestB2, TestC1, TestC2, TestD])



# Generated at 2022-06-12 22:49:46.999447
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(C): pass
    class E(C): pass
    class F(A): pass
    class G(A): pass
    class H(G): pass
    class I(H): pass
    classes_to_test = [A, B, C, D, E, F, G, H, I]
    for cls in classes_to_test:
        subclasses = get_all_subclasses(cls)
        # Check that subclasses is not empty, and
        # does not contains the same class
        assert subclasses
        assert cls not in subclasses
        for sc in subclasses:
            # Check that all returned classes are really subclass
            # of the input class
            assert issubclass(sc, cls)


# Generated at 2022-06-12 22:49:56.003833
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

    assert get_all_subclasses(A) == set([D,C,B,E])

    class F(D):
        pass

    assert get_all_subclasses(A) == set([D,C,B,E,F])

# This is a function to get a class name from a string.
# For example:
#     get_class('ansible.utils.module_docs_fragments.get_docfragment') -> ansible.utils.module_docs_fragments.ModuleDocFragment

# Generated at 2022-06-12 22:50:04.301380
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(object): pass
    class C(A): pass
    class D(A): pass
    class E(B): pass
    class F(E): pass
    class G(F): pass
    class H(F): pass
    class I(G): pass
    class J(I): pass
    class K(J): pass
    assert get_all_subclasses(A) == set([C, D])
    assert get_all_subclasses(B) == set([E, F, G, H, I, J, K])
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set([F, G, H, I, J, K])
    assert get_all_

# Generated at 2022-06-12 22:50:06.150278
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    assert set([B, C]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:50:10.910596
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    assert get_all_subclasses(A) == set([B, C])
    class D(B): pass
    class E(C): pass
    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:50:18.467891
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses
    '''
    # We start by creating a tree of classes
    class W(object):
        pass

    class X(W):
        pass

    class Y(W):
        pass

    class Z(Y):
        pass

    class K(Z):
        pass

    # Now we assert about the subset of classe we are expecting
    assert Z in get_all_subclasses(W)
    assert K in get_all_subclasses(W)
    assert X in get_all_subclasses(W)
    assert Y in get_all_subclasses(W)

# Generated at 2022-06-12 22:50:25.397386
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base(object):
        pass
    class Child1(Base):
        pass
    class Child2(Base):
        pass
    class GrandChild1(Child1):
        pass
    class GrandChild2(Child1):
        pass
    class GrandChild3(Child1):
        pass
    class GrandChild4(Child2):
        pass
    assert get_all_subclasses(Base) == {Child1, Child2, GrandChild1,
                                        GrandChild2, GrandChild3, GrandChild4}

    class Test1(object):
        pass
    class Test2(object):
        pass
    class Test3(Test1):
        pass
    assert get_all_subclasses(Test2) == set()
    assert get_all_subclasses(Test1) == {Test3}

# Generated at 2022-06-12 22:50:28.710760
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    assert get_all_subclasses(A) == set([B])
    class C(A):
        pass
    assert get_all_subclasses(A) == set([B, C])
    class D(B):
        pass
    assert get_all_subclasses(A) == set([B, C, D])



# Generated at 2022-06-12 22:50:35.593898
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(B, object):
        pass
    class D(A):
        pass
    class E(D):
        pass
    class F(D):
        pass
    class G(F):
        pass
    class H(F, E):
        pass
    assert G in get_all_subclasses(F)
    assert H in get_all_subclasses(F)
    assert H in get_all_subclasses(E)
    assert C in get_all_subclasses(A)
    assert C in get_all_subclasses(B)
    assert D in get_all_subclasses(A)
    assert F in get_all_subclasses(D)
    assert G in get_all_subclasses(D)
    assert H

# Generated at 2022-06-12 22:50:42.468737
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

    class E(B):
        pass

    class F(D):
        pass

    for cls in get_all_subclasses(A):
        assert(cls == C or cls == D or cls == F)

    for cls in get_all_subclasses(E):
        assert(cls == E)

    for cls in get_all_subclasses(B):
        assert(cls == B or cls == E)
