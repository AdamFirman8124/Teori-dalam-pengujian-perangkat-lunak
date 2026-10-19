

# Generated at 2022-06-12 22:41:15.477369
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(B): pass
    class F: pass
    class G(F): pass
    class H(F): pass
    class I(G): pass
    classes = [A,B,C,D,E,F,G,H,I]
    subclasses = [cls for cls in classes if cls is not A]
    for cls in classes:
        result = get_all_subclasses(cls)
        if cls == A:
            assert result == set(subclasses)
        else:
            assert result == set()

if __name__ == '__main__':
    # Test get_all_subclasses function
    test_get_all_subclasses()

# Generated at 2022-06-12 22:41:18.761111
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:pass
    class B(A):pass
    class C(A):pass
    class D(B):pass
    class E(B, C):pass
    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:41:30.737830
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Define some classes
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(D): pass
    class G(E): pass
    class H(G): pass

    # Define expected value
    expected = {B, C, D, E, F, G, H}

    # Check with class A
    assert set(get_all_subclasses(A)) == expected
    # Check with class E
    assert set(get_all_subclasses(E)) == expected - {D, B}
    # Check with class H
    assert set(get_all_subclasses(H)) == expected - {B, C, D}
    # Check with class H

# Generated at 2022-06-12 22:41:39.759810
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

    subclasses = get_all_subclasses(A)
    assert are_equal(subclasses, {B, C, D, E})

    subclasses = get_all_subclasses(B)
    assert are_equal(subclasses, {D, E})

    subclasses = get_all_subclasses(C)
    assert are_equal(subclasses, set())

    subclasses = get_all_subclasses(D)
    assert are_equal(subclasses, {E})

    subclasses = get_all_subclasses(E)
    assert are_equal(subclasses, set())



# Generated at 2022-06-12 22:41:43.891551
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(A): pass
    class F(D): pass
    actual = get_all_subclasses(A)
    expected = {B, C, D, E, F}
    assert actual == expected

# Generated at 2022-06-12 22:41:52.660260
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

    assert get_all_subclasses(object) == set([A, B, C, D, E])
    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:41:59.112537
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
    classes = get_all_subclasses(A)
    assert len(classes) == 5
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F in classes

# Generated at 2022-06-12 22:42:02.650064
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



# Generated at 2022-06-12 22:42:08.491770
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import ansible
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.plugins.task import ActionBase

    assert get_all_subclasses(ansible.parsing.dataloader.DataLoader) == set()
    assert get_all_subclasses(ansible.playbook.task.Task) == set()
    assert get_all_subclasses(ansible.executor.task_executor.TaskExecutor) == set()

    assert get_

# Generated at 2022-06-12 22:42:14.952813
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(object): pass
    assert get_all_subclasses(A) == {B, C, D}
    assert get_all_subclasses(B) == {C}
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:42:23.868440
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Sample classes used for demo purpose only
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    cls_list = [A, B, C, D]
    expected = set(cls_list)
    # Recursively search subclasses for A
    result = get_all_subclasses(A)
    # Ensure results are as expected
    assert(set(result) == expected)

# Generated at 2022-06-12 22:42:33.995291
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import pkgutil
    import ansible.module_utils
    import ansible.module_utils.six
    for imp, module, is_pkg in pkgutil.iter_modules(ansible.module_utils.six.__path__):
        if is_pkg:
            continue
        if module.endswith(".py"):
            mod_path = "ansible.module_utils.six.%s" % module[:-3]
            mod = __import__(mod_path, globals(), locals(), ['*'])
            for name, obj in mod.__dict__.items():
                try:
                    get_all_subclasses(obj)
                except Exception as e:
                    raise AssertionError("Cannot process module_utils.six.%s.%s" % (module[:-3], name), e)

# Generated at 2022-06-12 22:42:40.380883
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(B): pass
    class F(D): pass
    class G(D): pass
    class H(E): pass
    class I(H): pass
    class J(H): pass

    class TestClass(unittest.TestCase):
        """
        Testing get_all_subclasses
        """
        def test_expected_output(self):
            """
            Verify that expected output is returned
            """
            self.assertEqual(get_all_subclasses(A), set([B, C, D, E, F, G, H, I, J]))

# Generated at 2022-06-12 22:42:45.356522
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

# Generated at 2022-06-12 22:42:56.010198
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(C): pass
    class H(G): pass
    assert set() == get_all_subclasses(object)
    assert {B, D, E} == get_all_subclasses(A)
    assert {D, E} == get_all_subclasses(B)
    assert {F, G, H} == get_all_subclasses(C)
    assert {D} == get_all_subclasses(D)
    assert {E} == get_all_subclasses(E)
    assert {F} == get_all_subclasses(F)

# Generated at 2022-06-12 22:43:02.494960
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class a():
        pass

    class b(a):
        pass

    class c(a):
        pass

    class d(b):
        pass

    class e(d):
        pass

    # Checking that c, d and e are subclass of a
    assert c in get_all_subclasses(a)
    assert d in get_all_subclasses(a)
    assert e in get_all_subclasses(a)

    # Checking that e and d are subclass of b
    assert e in get_all_subclasses(b)
    assert d in get_all_subclasses(b)

    # Checking that d is subclass of c
    assert d not in get_all_subclasses(c)

# Generated at 2022-06-12 22:43:11.337585
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def A():
        pass
    def B(A):
        pass
    def C(A):
        pass
    def D(B):
        pass
    def E(D):
        pass
    def F(C):
        pass
    def G(B):
        pass

    # First, test that the function returns the correct number of instances
    assert(len(get_all_subclasses(A)) == 7)

    # Verify that the set is correct
    assert(get_all_subclasses(A) == set([B, C, D, E, F, G]))

    # Verify that the set is correct with another class not in the hierarchy
    # (by making sure it doesn't exist in the set)
    assert(C not in get_all_subclasses(A))

    # Verify that the function works when called from a child class

# Generated at 2022-06-12 22:43:15.901332
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Definition of class A and subclass B, C and D
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass
    # Testing for class A
    assert set(get_all_subclasses(A)) == set([B, C, D])

# Generated at 2022-06-12 22:43:20.738120
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(B): pass
    class E(A): pass
    class F(object): pass
    class G(F): pass
    # All classes of A listed
    assert set([B, C, D]) == get_all_subclasses(A)
    # Ignored class F
    assert set([G]) == get_all_subclasses(F)



# Generated at 2022-06-12 22:43:31.290898
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E(C): pass

    assert(set(A.__subclasses__()) == set([B, C]))
    assert(set(B.__subclasses__()) == set([D]))
    assert(set(C.__subclasses__()) == set([D, E]))
    assert(set(D.__subclasses__()) == set())
    assert(set(E.__subclasses__()) == set())

    assert(get_all_subclasses(A) == set([B, C, D, E]))
    assert(get_all_subclasses(B) == set([D]))
    assert(get_all_subclasses(C) == set([D, E]))

# Generated at 2022-06-12 22:43:39.063170
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

    class G(E):
        pass


# Generated at 2022-06-12 22:43:50.267335
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses
    '''
    class A: pass
    class B(A): pass

    # The module is imported in the global scope, so we are not in __main__ module
    assert __name__ != '__main__'

    # __main__ is the parent module of unit tests, so it is the grand parent of A/B classes
    global_scope = {'__name__': '__main__'}

    # The following will fail with our current implementation since
    # the class A/B does not have a __module__ attribute
    assert get_all_subclasses(A) == set()
    assert get_all_subclasses(B) == set()

    class_scope = {}
    # Executing again the class A/B definition in class_scope

# Generated at 2022-06-12 22:43:56.203081
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    An unit test for function get_all_subclasses
    '''

    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass

    # Test all possible cases and paths
    subclasses = get_all_subclasses(A)
    assert subclasses == {B, C, D, E, F}

    subclasses = get_all_subclasses(B)
    assert subclasses == {D, E}

    subclasses = get_all_subclasses(C)
    assert subclasses == {F}

    subclasses = get_all_subclasses(D)
    assert subclasses == set()

    subclasses = get_all_subclasses(E)
    assert subclasses == set

# Generated at 2022-06-12 22:44:06.927193
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Base class
    class A(object):
        pass

    # First generation subclasses
    class B(A):
        pass

    class C(A):
        pass

    # Second generation subclasses
    class D(B):
        pass

    class E(B):
        pass

    class F(C):
        pass

    class G(C):
        pass

    # Third generation subclasses
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


# Generated at 2022-06-12 22:44:13.324422
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    A_subclasses = set(get_all_subclasses(A))
    assert C in A_subclasses, 'C class should be in A_subclasses'
    assert B in A_subclasses, 'B class should be in A_subclasses'
    assert A in A_subclasses, 'A class should be in A_subclasses'
    assert A_subclasses == set([C, B, A]), 'A_subclasses should not contain extra classes'



# Generated at 2022-06-12 22:44:20.805888
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

    assert set([B, C, D, E]) == get_all_subclasses(A)
    assert set([D]) == get_all_subclasses(B)
    assert set([E]) == get_all_subclasses(C)
    assert set([]) == get_all_subclasses(D)
    assert set([]) == get_all_subclasses(E)


# Generated at 2022-06-12 22:44:29.496326
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

    assert set([B, D, C, E, F]) == get_all_subclasses(A)
    assert set([D]) == get_all_subclasses(B)
    assert set([E, F]) == get_all_subclasses(C)
    assert set([]) == get_all_subclasses(D)
    assert set([F]) == get_all_subclasses(E)
    assert set([]) == get_all_subclasses(F)

# Generated at 2022-06-12 22:44:38.023941
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(A): pass
    class F(E): pass
    class G(D): pass
    assert set(get_all_subclasses(A)) == set([B, C, D, E, F, G])
    assert B.__subclasses__() == [C]
    assert C.__subclasses__() == []
    assert D.__subclasses__() == [G]
    assert E.__subclasses__() == [F]
    assert F.__subclasses__() == []
    assert G.__subclasses__() == []

# Generated at 2022-06-12 22:44:41.737450
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
    assert get_all_subclasses(A) == {B, C, D, E, F}

# Generated at 2022-06-12 22:44:45.790874
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

    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:44:51.949878
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

# Generated at 2022-06-12 22:45:00.375562
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TestClass:
        pass

    class TestClass1(TestClass):
        pass

    class TestClass1Child1(TestClass1):
        pass

    class TestClass1Child2(TestClass1):
        pass

    class TestClass1Child1Child1(TestClass1Child1):
        pass

    class TestClass2(TestClass):
        pass

    class TestClass2Child1(TestClass2):
        pass

    assert TestClass in get_all_subclasses(TestClass)
    assert TestClass1 in get_all_subclasses(TestClass)
    assert TestClass1Child1 in get_all_subclasses(TestClass)
    assert TestClass1Child2 in get_all_subclasses(TestClass)
    assert TestClass1Child1Child1 in get_all_subclasses(TestClass)
    assert TestClass

# Generated at 2022-06-12 22:45:08.419697
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Defining a basic class
    class A(object):
        pass

    # Defining some subclasses
    class A1(A):
        pass

    class A12(A1):
        pass

    class A11(A1):
        pass

    class A2(A):
        pass

    class A21(A2):
        pass

    class A22(A2):
        pass

    assert set(get_all_subclasses(A)) == set([A1, A2, A11, A12, A21, A22])


# Generated at 2022-06-12 22:45:12.465580
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

    class F(E):
        pass

    assert sorted(get_all_subclasses(A)) == [B, C, D]
    assert sorted(get_all_subclasses(object)) == [A, B, C, D, E, F]

# Generated at 2022-06-12 22:45:21.254925
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
    # Test subclasses
    assert set(get_all_subclasses(A)) == set([B, C, D, E])
    assert set(get_all_subclasses(B)) == set([C])
    assert set(get_all_subclasses(C)) == set()
    assert set(get_all_subclasses(D)) == set([E])
    assert set(get_all_subclasses(E)) == set()

# Generated at 2022-06-12 22:45:24.409982
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

    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:45:30.974045
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define a class hierarchy
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
    class G(D):
        pass
    class H(E):
        pass
    class I(E):
        pass

    # Expected output is the following
    expected = [B, C, D, E, F, G, H, I]
    actual = list(get_all_subclasses(A))
    # The actual result will be a set
    # We need to convert it to a list in order to test it.
    assert expected == actual

# Generated at 2022-06-12 22:45:41.310007
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
    class I(D): pass
    class J(F): pass
    class K(G): pass
    class L(G): pass

    #
    # Testing for class A
    #
    all_subclasses = get_all_subclasses(A)
    assert len(all_subclasses) == 12
    assert B in all_subclasses
    assert C in all_subclasses
    assert D in all_subclasses
    assert E in all_subclasses
    assert F in all_subclasses
    assert G in all_subclasses
    assert H in all_subclasses

# Generated at 2022-06-12 22:45:45.007175
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
    all_subclasses = get_all_subclasses(A)
    assert set(all_subclasses) == {B, C, D, E}

# Generated at 2022-06-12 22:45:54.870700
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    import unittest

    class A(object):
        pass

    # class B(object):
    #     pass

    class C(A):
        pass

    class D(A):
        pass

    class E(D):
        pass

    class F(D):
        pass

    class G(D):
        pass

    class H(F):
        pass

    class I(F):
        pass

    expected_results = sorted([A, C, D, E, F, G, H, I])

    class TestGetAllSubClasses(unittest.TestCase):

        def test_get_all_subclasses(self):
            self.assertEqual(sorted(get_all_subclasses(A)), expected_results)

# Generated at 2022-06-12 22:46:03.956602
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # result from function get_all_subclasses
    result = get_all_subclasses(int)
    # expected result, computed manually
    expected = set([long, float, complex, bool])
    # check against expected result
    assert result == expected


# Generated at 2022-06-12 22:46:13.278124
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(B): pass
    class E(D): pass
    class F(D): pass
    class G(D): pass
    assert get_all_subclasses(A) == set([B, C, D, E, F, G])
    assert get_all_subclasses(B) == set([C, D, E, F, G])
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == set([E, F, G])
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == set()
    assert get_all_subclasses(G) == set()


# TODO: Get rid of this function

# Generated at 2022-06-12 22:46:21.412462
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test function get all subclasses
    '''
    class A(object):  # pylint: disable=too-few-public-methods
        '''
        Class A
        '''
        pass

    class B(A):  # pylint: disable=too-few-public-methods
        '''
        Class B inherits A
        '''
        pass

    class C(A):  # pylint: disable=too-few-public-methods
        '''
        Class C inherits A
        '''
        pass

    class D(C):  # pylint: disable=too-few-public-methods
        '''
        Class D inherits C
        '''
        pass

    assert set([B, C, D]) == get_all_subclasses(A)

   

# Generated at 2022-06-12 22:46:30.679534
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import defaultdict
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

    class F(B):
        pass

    class G(F):
        pass

    class H(B, F):
        pass

    class I(H):
        pass

    class J(B, F, H, I):
        pass

    class K(H, I):
        pass

    class L(C, E, F, G, H, I, J, K):
        pass

    class M(A):
        pass

    class N(A):
        pass

    class O(A):
        pass


# Generated at 2022-06-12 22:46:35.078641
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class A1(A):
        pass

    class A2(A):
        pass

    class B(object):
        pass

    class B1(B):
        pass

    assert set(get_all_subclasses(A)) == set([A1, A2])
    assert set(get_all_subclasses(B)) == set([B1])

# Generated at 2022-06-12 22:46:39.797107
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Some test classes
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
    class F(E):
        pass

    assert get_all_subclasses(A) == set([B,C,D])
    assert get_all_subclasses(E) == set([F])

# Generated at 2022-06-12 22:46:46.615185
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create sample tree
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
    class F(B):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F}
    assert get_all_subclasses(B) == {F}
    assert get_all_subclasses(C) == {D, E}
    assert get_all_subclasses(D) == {E}
    assert get_all_subclasses(E) == set()
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:46:57.732046
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit tests for function get_all_subclasses
    '''
    import collections
    # Test with a simple class hierarchy
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    assert get_all_subclasses(A) == set([B, C, D])
    # Test with a more complex hierarchy
    class Test(object):
        pass
    class TestFail(Test):
        pass
    class ModuleDocRegressionTest(Test):
        pass
    class ArgumentSpec(object):
        pass
    class TupleBecomeArgs(ArgumentSpec):
        pass
    class DictBecomeArgs(ArgumentSpec):
        pass
    class DeprecatedArgs(ArgumentSpec):
        pass

# Generated at 2022-06-12 22:47:05.149911
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test method get_all_subclasses()
    '''
    # Expected subclass result
    expected_subclasses = set([Example2Subclass1, Example2Subclass2, Example2Subclass3, Example2Subclass4])
    # Test get_all_subclasses function
    assert get_all_subclasses(Example2) == expected_subclasses


# Line to run unit test on this module
if __name__ == "__main__":
    import pytest
    pytest.main(['-v', __file__])


# Example of class hierarchy to test method get_all_subclasses()

# Generated at 2022-06-12 22:47:09.775212
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for get_all_subclasses()
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

    assert get_all_subclasses(A) == {B, C, D, E}

# Generated at 2022-06-12 22:47:21.787341
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

    assert set(get_all_subclasses(A)) == set([B, C, D])

# Generated at 2022-06-12 22:47:27.218061
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(object): pass
    class C(A): pass
    class D(C): pass
    assert set(get_all_subclasses(A)) == set([C, D])
    assert set(get_all_subclasses(B)) == set([])
    assert set(get_all_subclasses(C)) == set([D])

# Generated at 2022-06-12 22:47:31.360648
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(E): pass
    assert sorted(get_all_subclasses(A)) == sorted([B,C,D,E,F])

# Generated at 2022-06-12 22:47:39.973295
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import six
    import unittest

    class BaseA(object):
        pass

    class BaseB(object):
        pass

    class BaseC(object):
        pass

    class A(BaseA):
        pass

    class B(BaseB):
        pass

    class C(BaseC):
        pass

    class D(BaseC):
        pass

    class A1(A):
        pass

    class A2(A):
        pass

    class B1(B):
        pass

    class B2(B):
        pass

    class C1(C):
        pass

    class C2(C):
        pass

    class C3(C):
        pass

    class C4(C):
        pass

    class C1a(C1):
        pass


# Generated at 2022-06-12 22:47:45.887037
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Parent(object):
        pass

    class ChildA(Parent):
        pass

    class ChildB(Parent):
        pass

    class ChildC(ChildA):
        pass

    class GrandChildA(ChildB):
        pass

    class GrandChildB(ChildB):
        pass

    class GrandChildC(ChildC):
        pass

    all_subclasses = set([ChildA, ChildB, ChildC, GrandChildA, GrandChildB, GrandChildC])

    assert all_subclasses == get_all_subclasses(Parent)

# Generated at 2022-06-12 22:47:48.779522
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

    class E(B, C):
        pass

    assert set(get_all_subclasses(A)) == {B, C, D, E}



# Generated at 2022-06-12 22:47:58.703463
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule

    class MyModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(MyModule, self).__init__(*args, **kwargs)
            self.params = to_text(self._ansible_params)
        def execute_module(self):
            return 'my_result'

    class MyModule2(MyModule):
        def execute_module(self):
            return 'my_result2'

    class MyModule3(MyModule):
        def execute_module(self):
            return 'my_result3'

    class MyModule4(MyModule2):
        def execute_module(self):
            return 'my_result4'


# Generated at 2022-06-12 22:48:07.344921
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
    class E(C):
        pass
    class F(E):
        pass
    assert get_all_subclasses(A) == set([D])
    assert get_all_subclasses(B) == set()
    assert get_all_subclasses(C) == set([E, F])
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set([F])
    assert get_all_subclasses(F) == set()
    # pylint: disable=too-few-public-methods
    class ABC(object):
        pass
    # pylint: enable=too-few-public-

# Generated at 2022-06-12 22:48:11.772300
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

    assert get_all_subclasses(A) == set((B, C, D, E, F))
    assert get_all_subclasses(E) == set((F,))
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:48:22.943047
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import Sequence
    from ansible.module_utils.basic import AnsibleModule

    # Test case
    class TestClass01(Sequence):
        pass
    class TestClass02(Sequence):
        pass

    class TestClass03(AnsibleModule):
        pass
    class TestClass04(AnsibleModule):
        pass
    class TestClass05(AnsibleModule):
        pass

    class TestClass06(TestClass03):
        pass
    class TestClass07(TestClass06):
        pass
    class TestClass08(TestClass07):
        pass
    class TestClass09(TestClass07):
        pass
    class TestClass10(TestClass03):
        pass
    class TestClass11(TestClass06):
        pass
    class TestClass12(TestClass06):
        pass

# Generated at 2022-06-12 22:48:56.661635
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    The following classes will be used as fixtures to test get_all_subclasses function

        class A(object):
            pass

        class B(A):
            pass

        class C(object):
            pass

        class D(C):
            pass

        class E(D):
            pass

        class F(A):
            pass

    Those classes when executed should return the following tree

        class A(object):
            pass
            |
            +- class B(A):
            |       pass
            |
            +- class F(A):
                    pass
        class C(object):
            pass
            |
            +- class D(C):
            |       pass
            |       |
            |       +- class E(D):
                    pass
    '''
    class A(object):
        pass


# Generated at 2022-06-12 22:49:05.556905
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Class definition for testing get_all_subclasses function
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
    # Testing part
    assert(set(get_all_subclasses(A)) == set([B, C, D, E, F]))
    assert(set(get_all_subclasses(B)) == set([D, E, F]))
    assert(set(get_all_subclasses(C)) == set([]))
    assert(set(get_all_subclasses(D)) == set([F]))
    assert(set(get_all_subclasses(E)) == set([]))

# Generated at 2022-06-12 22:49:11.479416
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Unit test for function get_all_subclasses

    In this unit test, we define 3 classes, A -> B -> C with the structure:

        class A(object):
            pass

        class B(A):
            pass

        class C(B):
            pass

    Then we test that get_all_subclasses(A) will return all 3 classes.

    :raises AssertionError: Raises AssertionError when test fails
    '''
    # Creating the class structure
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass

    # Testing
    assert set([A, B, C]) == set(get_all_subclasses(A))

from types import MethodType


# Generated at 2022-06-12 22:49:21.130239
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

    subs = get_all_subclasses(A)
    expected_subs = {B, C, D, E}
    assert subs == expected_subs
    subs = get_all_subclasses(B)
    expected_subs = {C}
    assert subs == expected_subs
    subs = get_all_subclasses(D)
    expected_subs = {E}
    assert subs == expected_subs
    subs = get_all_subclasses(C)
    expected_subs = set([])
    assert subs == expected_subs
    subs = get_all_subclasses(E)
    expected_sub

# Generated at 2022-06-12 22:49:28.131333
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create first simple class A
    class A(object):
        pass

    # Create another class B
    class B(object):
        pass

    # Create a sub class of A
    class C(A):
        pass

    # An other sub class of A
    class D(A):
        pass

    # Create a sub class of B
    class E(B):
        pass

    # Create a sub class of C
    class F(C):
        pass

    # Assert that all subclasses of A are C and D
    assert set([C, D]) == get_all_subclasses(A)
    # Assert that all subclasses of B are E
    assert set([E]) == get_all_subclasses(B)
    # Assert that all subclasses of C are F
    assert set([F]) == get_all_

# Generated at 2022-06-12 22:49:36.827439
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from types import ModuleType
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    # Create some classes for the sake of this test
    class ClassA(object):
        pass

    class Class1(ClassA):
        pass

    class Class2(ClassA):
        pass

    class Class2_1(Class2):
        pass

    class Class2_2(Class2):
        pass

    class Class3(ClassA):
        pass

    # The following is the expected outcome from get_all_subclasses
    expected_outcome = {ClassA, Class1, Class2, Class2_1, Class2_2, Class3}
    assert get_all_subclasses(ClassA) == expected_outcome
    # To ensure that this function is not dependent on a particular branch of

# Generated at 2022-06-12 22:49:45.242445
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Check that the result of get_all_subclasses is correct
    '''
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    subclasses = get_all_subclasses(A)

    # Check that all subclasses are in the result
    expected = frozenset([B, C, D])
    assert subclasses == expected

    # Change the expected frozenset to a list and shuffle it
    import random
    expected = list(expected)
    random.shuffle(expected)

    # Check that all classes are present in the shuffled list
    for cls in expected:
        assert cls in subclasses

    # Check that no other classes are present in the shuffled list

# Generated at 2022-06-12 22:49:48.421497
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A: pass

    class B(A): pass

    class C(A): pass

    class D(B): pass

    class E(B): pass

    class F(C): pass

    class G(F): pass

    assert set(get_all_subclasses(A)) == set([B,C,D,E,F,G])

# Generated at 2022-06-12 22:49:52.950266
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Creating a simple class hierarchy
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(object): pass

    assert(set(get_all_subclasses(A)) == {B, C, D})
    assert(set(get_all_subclasses(B)) == {C})
    assert(set(get_all_subclasses(C)) == set())
    assert(set(get_all_subclasses(D)) == set())
    assert(set(get_all_subclasses(E)) == set())

# Generated at 2022-06-12 22:49:58.682503
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

    subclasses = get_all_subclasses(A)
    assert subclasses == set([B, C, D, E])

# Generated at 2022-06-12 22:50:51.906503
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(B):
        pass
    class E(C):
        pass
    class F:
        pass
    assert get_all_subclasses(A) == {B, C, D, E}
    assert get_all_subclasses(F) == set()

# Generated at 2022-06-12 22:50:59.250309
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class C1:
        pass

    class C2(C1):
        pass

    class C3:
        pass

    class C4(C2):
        pass

    class C5(C2):
        pass

    class C6:
        pass

    assert get_all_subclasses(C1) == {C2, C4, C5}
    assert get_all_subclasses(C2) == {C4, C5}
    assert get_all_subclasses(C3) == set()
    assert get_all_subclasses(C4) == set()
    assert get_all_subclasses(C5) == set()
    assert get_all_subclasses(C6) == set()



# Generated at 2022-06-12 22:51:02.867092
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
    class E(B,C):
        pass
    class F(object):
        pass
    out1 = get_all_subclasses(A)
    out2 = get_all_subclasses(F)
    all_subclasses = {B,C,D,E}
    assert(out1 == all_subclasses)
    assert(out2 == set())