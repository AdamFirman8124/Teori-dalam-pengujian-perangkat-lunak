

# Generated at 2022-06-12 22:41:15.477227
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class Animal:
        pass

    class Mammal(Animal):
        pass

    class Carnivore(Mammal):
        pass

    class Feline(Carnivore):
        pass

    class Dog(Mammal):
        pass

    class Cat(Feline):
        pass

    class Tiger(Feline):
        pass

    class Leopard(Feline):
        pass

    class Lion(Feline):
        pass

    class Herp(Animal):
        pass

    class Amphibian(Herp):
        pass

    class Snake(Herp):
        pass

    animals = [Animal, Mammal, Carnivore, Feline, Dog, Cat, Tiger, Leopard, Lion, Herp, Amphibian, Snake]
    # Testing each class and the subclasses of Animal class
    for animal in animals:
        assert get_all

# Generated at 2022-06-12 22:41:27.024002
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        '''A class'''
        pass

    class B(A):
        '''B class'''
        pass

    class C(A):
        '''C class'''
        pass

    class D(C):
        '''D class'''
        pass

    class E(A):
        '''E class'''
        pass

    class F(A):
        '''F class'''
        pass

    class G(E, F):
        '''G class'''
        pass

    class H(G):
        '''H class'''
        pass

    assert get_all_subclasses(A) == set((B, C, D, E, F, G, H))
    assert get_all_subclasses(B) == set()

# Generated at 2022-06-12 22:41:33.545356
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a class hierarchy
    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D(A):
        pass
    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(B)) == set([C])
    assert set(get_all_subclasses(C)) == set([])
    assert set(get_all_subclasses(D)) == set([])

# Generated at 2022-06-12 22:41:37.349862
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Creation of test classes
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(C): pass
    class F(D, C): pass
    class G(F): pass

    classes = get_all_subclasses(A)
    assert classes == set([B, C, D, E, F, G])

# Generated at 2022-06-12 22:41:45.872157
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import unittest
    class AAA(object):
        pass
    class BBB(AAA):
        pass
    class CCC(BBB):
        pass
    class DDD(AAA):
        pass
    class EEE(AAA):
        pass
    class FFF(EEE):
        pass

    class TestFindSubclasses(unittest.TestCase):
        '''
        Function get_all_subclasses
        '''
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_get_all_subclasses(self):
            expected = {BBB, CCC, DDD, EEE, FFF}
            self.assertEqual(expected, get_all_subclasses(AAA))

    unittest.main(verbosity=2)

# Generated at 2022-06-12 22:41:55.656129
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import defaultdict
    import os
    # Test case for a "classic" class hierarchy
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

    subclasses_hierarchy = defaultdict(set)

    subclasses_hierarchy[A] = set([F, B, C, E, D])
    subclasses_hierarchy[B] = set([F])
    subclasses_hierarchy[C] = set([F, E, D])
    subclasses_hierarchy[D] = set([E])
    subclasses_hierarchy[E] = set([])

# Generated at 2022-06-12 22:41:59.991566
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    class E(B, A): pass
    class F(E): pass
    assert get_all_subclasses(A) == set([B, C, D, E, F])

# Generated at 2022-06-12 22:42:07.262037
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Base():
        pass

    class A(Base):
        pass

    class B(Base):
        pass

    class C(Base):
        pass

    class D(Base):
        pass

    class AA(A):
        pass

    class AB(A):
        pass

    class BB(B):
        pass

    class BC(B):
        pass

    class CB(C):
        pass

    class AC(A):
        pass

    class BA(B):
        pass

    class CA(C):
        pass

    class DA(C):
        pass

    class AAA(AA):
        pass

    class BAA(BA):
        pass

    class BBB(BB):
        pass

    assert len(get_all_subclasses(Base)) == 10
    assert len(get_all_subclasses(A))

# Generated at 2022-06-12 22:42:13.278990
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class ParentClass(object):
        pass

    class FooChildClass(ParentClass):
        pass

    class BarChildClass(ParentClass):
        pass

    class OtherParentClass(object):
        pass

    class QuxChildClass(OtherParentClass):
        pass

    expected_subclasses = {FooChildClass, BarChildClass, QuxChildClass}
    assert expected_subclasses == get_all_subclasses(object)



# Generated at 2022-06-12 22:42:16.429279
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test function get_all_subclasses to verify it is working as expected
    Negative tests are not covered
    '''

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
    class G(F):
        pass
    class H(C):
        pass
    class I(C):
        pass
    class J(I):
        pass
    class K(D):
        pass
    class L(D):
        pass

    assert sorted(get_all_subclasses(A)) == [B, C, D, E, F, G, H, I, J, K, L]

# Generated at 2022-06-12 22:42:29.349833
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Class a
    class a:
        pass

    # Class b, a subclass of a
    class b(a):
        pass

    # Class c, a subclass of b
    class c(b):
        pass

    # Class d, a subclass of a
    class d(a):
        pass

    # Class e, a subclass of d
    class e(d):
        pass

    # Class f, a subclass of d
    class f(d):
        pass

    # Retrieve subclasses of d and check that there are 3
    subclasses_base_a = list(get_all_subclasses(a))
    assert len(subclasses_base_a) == 3
    assert b in subclasses_base_a
    assert d in subclasses_base_a
    assert c in subclasses_base_a

    # Retrieve

# Generated at 2022-06-12 22:42:35.872868
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
    assert get_all_subclasses(B) == set([C, D])
    assert get_all_subclasses(C) == set([D])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(object) == set()

# Generated at 2022-06-12 22:42:42.701492
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test the get_all_subclasses function.
    '''
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(object):
        pass

    assert A in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert not D in get_all_subclasses(A)

# Generated at 2022-06-12 22:42:48.409624
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

    assert set([B, C]) == get_all_subclasses(A)
    assert set([B, C]) == get_all_subclasses(object)
    assert set([D]) == get_all_subclasses(D)

# Generated at 2022-06-12 22:42:58.637654
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class_a = A()

    class B(A):
        pass
    class_b = B()

    class C(A):
        pass
    class_c = C()

    class D(B):
        pass
    class_d = D()

    class E(C, D):
        pass
    class_e = E()

    class F(E):
        pass
    class_f = F()

    class G(F):
        pass
    class_g = G()

    class H(F):
        pass
    class_h = H()

    class I(G,H):
        pass
    class_i = I()

    class J(I):
        pass
    class_j = J()

    class K(G, H):
        pass
    class_

# Generated at 2022-06-12 22:43:08.255210
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import ansible.module_utils
    assert set([ansible.module_utils.basic.AnsibleModule,
                ansible.module_utils.basic.AnsibleModule]) == set(get_all_subclasses(ansible.module_utils.basic.AnsibleModule))

    import ansible.plugins
    assert set([]) == set(get_all_subclasses(ansible.plugins.StateModule))

    import ansible.runner.return_data
    assert set([ansible.runner.return_data.AggregateStats,
                ansible.runner.return_data.ReturnData]) == set(get_all_subclasses(ansible.runner.return_data.ReturnData))

# Generated at 2022-06-12 22:43:15.123343
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

    class E(A):
        pass

    class F(E):
        pass

    class G(A):
        pass

    assert set([A, B, C, D, E, F, G]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:43:22.482813
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

    class F(E):
        pass

    import unittest
    test_cases = [
        (A, [B, C, D, E, F]),
        (B, []),
        (C, []),
        (D, []),
        (E, [F]),
        (F, []),
    ]
    for base_cls, expected in test_cases:
        print('Testing %s' % base_cls)
        cls_list = sorted([c for c in get_all_subclasses(base_cls)], key=lambda x: x.__name__)

        # (1) check

# Generated at 2022-06-12 22:43:29.912948
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from units.mock.loader import DictDataLoader

    class BaseClass(DictDataLoader):
        pass

    class SubClassOne(BaseClass):
        pass

    class SubClassTwo(BaseClass):
        pass

    class SubSubClassOne(SubClassOne):
        pass

    class SubSubSubClassOne(SubSubClassOne):
        pass

    expected = set([SubClassOne, SubClassTwo, SubSubClassOne, SubSubSubClassOne])
    assert get_all_subclasses(BaseClass) == expected

# Generated at 2022-06-12 22:43:36.912606
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def test_class(cls):
        class SubClassA(cls):
            pass
        class SubSubClassA(SubClassA):
            pass
        class SubClassB(cls):
            pass

        return cls, SubClassA, SubSubClassA, SubClassB

    class A(object):
        pass

    BaseClass, SubClassA, SubSubClassA, SubClassB = test_class(A)

    assert BaseClass in get_all_subclasses(A)
    assert SubClassA in get_all_subclasses(A)
    assert SubClassB in get_all_subclasses(A)
    assert SubSubClassA in get_all_subclasses(A)

    class B(object):
        pass


# Generated at 2022-06-12 22:43:43.510699
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    result = set([D, B, C])
    assert get_all_subclasses(A) == result

# Generated at 2022-06-12 22:43:53.110103
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    """Function to test if get_all_subclasses returns the correct values"""
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
    class G(object):
        pass
    # We shouldn't get back B, C, D, E or F because they are all descended from A
    assert get_all_subclasses(A) == set([])
    # We should get back G since it is not descended from A
    assert get_all_subclasses(A) != set([G])
    # We shouldn't get back G even though it is also descended from object
    assert get_all_subclasses(object) != set([G])
    # We should get

# Generated at 2022-06-12 22:43:58.628609
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Foo(object): pass
    class Bar(Foo): pass
    class Baz(Foo): pass
    class Qux(Bar): pass
    # Set the expected result
    expected = {Bar, Baz, Qux}
    # Test function get_all_subclasses
    assert get_all_subclasses(Foo) == expected

# Generated at 2022-06-12 22:44:06.002335
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class Dummy():
        pass

    class Dummy_a(Dummy):
        pass

    class Dummy_b(Dummy):
        pass

    class Dummy_c(Dummy_b):
        pass

    d_classes = get_all_subclasses(Dummy)
    assert Dummy_a in d_classes, "Dummy_a must be in classes"
    assert Dummy_b in d_classes, "Dummy_b must be in classes"
    assert Dummy_c in d_classes, "Dummy_c must be in classes"

# Generated at 2022-06-12 22:44:13.107479
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

    class Test(A):
        pass

    assert set([B, C, D, E, Test]) == get_all_subclasses(A)
    assert set([D, Test]) == get_all_subclasses(C)
    assert set([D, E, Test]) == get_all_subclasses(B)
    # Test specific case where there was a bad recursion problem
    assert set() == get_all_subclasses(Test)

# Generated at 2022-06-12 22:44:20.933100
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

    class E(C):
        pass

    class F(D, E):
        pass

    expected_result = (B, D, C, E, F)
    result = get_all_subclasses(A)

    class TestGetSubClasses(unittest.TestCase):
        def test_get_all_subclasses(self):
            self.assertEqual(result, expected_result)

    unittest.main()

# Generated at 2022-06-12 22:44:27.105437
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils import six
    # Create a custom class
    class Animal(object):
        pass
    class Mammal(Animal):
        pass
    class Cat(Mammal):
        pass
    class Dog(Mammal):
        pass
    class Octopus(Animal):
        pass

    # Check that the method returns all subclasses
    assert set(get_all_subclasses(Animal)) == set(map(six.create_bound_method, (Octopus, Dog, Cat, Mammal)))

# Generated at 2022-06-12 22:44:37.579157
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    def test_function():
        return True
    # Class A(object) should be the base class
    class A(object):
        def test_function(self):
            return False
    class B(A):
        pass
    # Class C is an orphan class, who is not a subclass of A
    class C(object):
        pass
    class D(A):
        def test_function(self):
            return 'D'
    class E(D):
        pass
    class F(E):
        def test_function(self):
            return 'F'
    class G(F):
        def test_function(self):
            return 'G'
    class H(F):
        pass
    class I(G):
        pass
    class J(I):
        pass

    # Test results
    expected_subclasses = set

# Generated at 2022-06-12 22:44:42.269547
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B:
        pass

    class C(B):
        pass

    class D(C):
        pass

    # Class B and class D are subclasses of class A
    assert B in get_all_subclasses(A)
    assert D in get_all_subclasses(A)

    # Class C is not a subclass of class A
    assert C not in get_all_subclasses(A)

# Generated at 2022-06-12 22:44:52.346765
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    class A(object):
        def __init__(self):
            super(A, self).__init__()

    class B(A):
        def __init__(self):
            super(B, self).__init__()

    class D(A):
        def __init__(self):
            super(D, self).__init__()

    class E(object):
        def __init__(self):
            super(E, self).__init__()

    class F(E):
        def __init__(self):
            super(F, self).__init__()

    class G(F):
        def __init__(self):
            super(G, self).__init__()

    class C(B, D):
        def __init__(self):
            super(C, self).__init__()

   

# Generated at 2022-06-12 22:45:02.562734
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Fast unit test
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

    assert A in get_all_subclasses(object)
    assert B in get_all_subclasses(object)
    assert C in get_all_subclasses(object)
    assert A not in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert B in get_all_subclasses(B)
    assert C in get_all_subclasses(B)
    assert C not in get_all_subclasses(C)
    assert B not in get_all_subclasses(C)


# Generated at 2022-06-12 22:45:07.229072
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(object):
        pass
    class C(object):
        pass
    class AA(A):
        pass
    class AB(A):
        pass
    class BA(B):
        pass
    class BB(B):
        pass
    class CA(C):
        pass
    class CB(C):
        pass
    class AAA(AA):
        pass
    assert get_all_subclasses(A) == set([AA, AB, AAA])
    assert get_all_subclasses(B) == set([BA, BB])
    assert get_all_subclasses(C) == set([CA, CB])
    assert get_all_subclasses(object) == set([A, AA, AB, AAA, B, BA, BB, C, CA, CB])


# Generated at 2022-06-12 22:45:09.744395
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    a = object()
    b = object()
    c = object()

    c.__bases__ = (b,)
    b.__bases__ = (a,)

    assert get_all_subclasses(a) == set([b, c])

# Generated at 2022-06-12 22:45:19.668491
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    import six

    class A(object):
        pass

    class B(A):
        pass

    class D(B):
        pass

    class E(B):
        pass

    class C(A):
        pass

    class F(C):
        pass

    class G(F):
        pass

    class H(G):
        pass

    class I(G):
        pass

    assert get_all_subclasses(A) == {B, C, D, E, F, G, H, I}
    assert get_all_subclasses(B) == {D, E}
    assert get_all_subclasses(C) == {F, G, H, I}

    if six.PY2:
        assert get_all_subclasses(object) == {type}

# Generated at 2022-06-12 22:45:28.554537
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create sample classes
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

    my_classes = set([A, B, C, D])
    # Check all subclasses of A
    assert my_classes == get_all_subclasses(A)
    # Check all subclasses of B
    assert set([B, C]) == get_all_subclasses(B)
    # Check all subclasses of C
    assert set([C]) == get_all_subclasses(C)
    # Check all subclasses of D
    assert set([D]) == get_all_subclasses

# Generated at 2022-06-12 22:45:33.673294
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class Foo(object):
        pass

    class FooPlus(Foo):
        pass

    class FooPlusPlus(FooPlus):
        pass

    assert FooPlus in get_all_subclasses(Foo)
    assert FooPlusPlus in get_all_subclasses(Foo)
    assert FooPlusPlus in get_all_subclasses(FooPlus)
    assert FooPlusPlus in get_all_subclasses(FooPlusPlus)

# Generated at 2022-06-12 22:45:43.560236
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import defaultdict
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
    class H(G):
        pass
    class I(H):
        pass
    class J(I):
        pass
    assert len(get_all_subclasses(A)) == 9
    assert len(get_all_subclasses(B)) == 4
    assert len(get_all_subclasses(C)) == 4
    assert len(get_all_subclasses(D)) == 1
    assert len(get_all_subclasses(E)) == 1

# Generated at 2022-06-12 22:45:48.346242
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
    assert get_all_subclasses(A) == set([B, C, D])
    assert get_all_subclasses(B) == set([C])
    assert get_all_subclasses(C) == set([])
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])

# Generated at 2022-06-12 22:45:51.738761
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

    assert(get_all_subclasses(A) == {B, C, D})

# Generated at 2022-06-12 22:45:57.145671
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(B,D): pass

    lst = get_all_subclasses(A)
    assert len(lst) == 4
    assert B in lst
    assert C in lst
    assert D in lst
    assert E in lst



# Generated at 2022-06-12 22:46:11.736697
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test the get_all_subclasses function
    '''
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
    class F(B):
        pass
    class G(D):
        pass
    class H(G):
        pass
    def test(class_list):
        '''
        Check if the returned classes are the same as the classes from the class list
        '''
        for cls in class_list:
            if cls not in class_list:
                return False
        return True
    # Check if the returned classes are the same as the classes from the class list
    assert test(get_all_subclasses(object))

# Generated at 2022-06-12 22:46:18.796664
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Building class tree
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

    class F(E):
        pass

    class G(F):
        pass

    # Testing get_all_subclasses
    assert(get_all_subclasses(A) == {E, B, C, D, F, G})
    assert(get_all_subclasses(B) == set())
    assert(get_all_subclasses(C) == {D})
    assert(get_all_subclasses(D) == set())
    assert(get_all_subclasses(E) == {F, G})
    assert(get_all_subclasses(F) == {G})
   

# Generated at 2022-06-12 22:46:27.783495
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
    class E(A):
        pass
    class F(A):
        pass
    class G(C):
        pass
    class H(D):
        pass
    class I(D):
        pass
    class J(D):
        pass
    class K(F):
        pass
    class L(F):
        pass
    class M(F):
        pass
    assert A in get_all_subclasses(A)
    assert B not in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)

# Generated at 2022-06-12 22:46:36.301803
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
    class E(A):
        pass
    class F(E):
        pass
    class G(C):
        pass
    class H:
        pass
    assert get_all_subclasses(A) == {B, C, D, E, F, G}
    assert get_all_subclasses(B) == {D}
    assert get_all_subclasses(C) == {G}
    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == {F}
    assert get_all_subclasses(F) == set()
    assert get_all_subclasses(G) == set()
    assert get_

# Generated at 2022-06-12 22:46:40.290399
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B:
        pass

    class E(B):
        pass

    class D(B):
        pass

    class C(A):
        pass

    class F(C):
        pass

    assert get_all_subclasses(A) == {C, F}
    assert get_all_subclasses(B) == {E, D}



# Generated at 2022-06-12 22:46:43.881324
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Implement a hierarchy of class
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
    # Check the result of the function
    assert get_all_subclasses(A) == set([B, C, D])

# Generated at 2022-06-12 22:46:49.314697
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import namedtuple
    from itertools import chain
    # Define a simple class hierarchy
    Grandfather = namedtuple('Grandfather', ('name'))
    Father = namedtuple('Father', ('name'))
    Uncle = namedtuple('Uncle', ('name'))
    Bastard = namedtuple('Bastard', ('name'))
    Son = namedtuple('Son', ('name'))
    Grandson = namedtuple('Grandson', ('name'))
    Family = namedtuple('Family', ('name'))
    # Define the hierarchy
    class_hierarchy = {
        Grandfather: {},
        Father: {Uncle: {}, Bastard: {}},
        Son: {Grandson: {}},
    }
    # Determine the expected results

# Generated at 2022-06-12 22:46:58.730430
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass

    class B(object):
        pass

    class C(object):
        pass

    class D(object):
        pass

    class E(A, B):
        pass

    class F(A, C):
        pass

    class G(D, A):
        pass

    assert get_all_subclasses(G) == set([G])
    assert get_all_subclasses(F) == set([E, F])
    assert get_all_subclasses(C) == set([E, F])
    assert get_all_subclasses(A) == set([E, F, G])
    assert get_all_subclasses(object) == set([E, F, G, A, B, C, D])

# Generated at 2022-06-12 22:47:03.679089
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
    assert get_all_subclasses(A) == set([B, C, D, E]), "get_all_subclasses failed"

# Generated at 2022-06-12 22:47:12.372431
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

    class E(A):
        pass

    class F(E):
        pass

    class G(F):
        pass

    class H(F):
        pass

    classes = get_all_subclasses(A)
    # The set should contain every subclasses of A
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F in classes
    assert G in classes
    assert H in classes
    # The set should not contain A
    assert A not in classes
    # The set should not contain subclasses of other classes
    assert len(classes) == 7

# Generated at 2022-06-12 22:47:26.684863
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

    class E(A):
        pass

    assert get_all_subclasses(A) == set([B, C, D, E])

# Generated at 2022-06-12 22:47:34.479155
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Create parent class
    class Parent(object):
        pass

    # Create first level of subclasses
    class Child1(Parent):
        pass

    class Child2(Parent):
        pass

    # Create second level of subclass
    class Child3(Child1):
        pass

    class Child4(Child1):
        pass

    class Child5(Child2):
        pass

    class Child6(Child2):
        pass

    # Check that all subclasses are listed
    assert get_all_subclasses(Parent) == set((Child1, Child2, Child3, Child4, Child5, Child6))

# Generated at 2022-06-12 22:47:39.582314
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
    class G(E):
        pass
    class H(F):
        pass
    class I(H):
        pass
    assert get_all_subclasses(A) == set([B, C, D, E, F, G, H, I])

# Generated at 2022-06-12 22:47:43.594883
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

    subclasses = set([C, D, E])
    assert get_all_subclasses(A) == subclasses



# Generated at 2022-06-12 22:47:48.240779
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(B): pass
    class F(C): pass
    class G(F): pass
    classes = get_all_subclasses(A)
    assert len(classes) == 6
    assert B in classes
    assert C in classes
    assert D in classes
    assert E in classes
    assert F in classes
    assert G in classes

# Generated at 2022-06-12 22:47:58.132766
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    This is a unit test for the get_all_subclasses
    '''
    class A(object):
        '''
        Class A
        '''

    class B(object):
        '''
        Class B
        '''

    class C(B):
        '''
        Class C
        '''

    class D(C, A):
        '''
        Class D
        '''

    class E(D, B):
        '''
        Class E
        '''

    class F(E, A):
        '''
        Class F
        '''

    class G(A):
        '''
        Class G
        '''

    class H(D, G):
        '''
        Class H
        '''


# Generated at 2022-06-12 22:48:05.045248
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Function test_get_all_subclasses unit tests the get_all_subclasses function.

    This function tests the get_all_subclasses function by creating a class hierarchy of the
    following shape:

    A
    |-B-C
    |-B-D-E
    |-F-G

    After the hierarchy is created, the function tests the get_all_subclasses function to ensure
    that it returns the expected set of classes::

        {B, C, D, E, F, G}

    If the test fails, the function will raise an AssertionError containing the expected and
    received sets of classes.
    '''
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(B):
        pass


# Generated at 2022-06-12 22:48:07.862042
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(object): pass

    assert set(get_all_subclasses(A)) == set([B, C, D])
    assert set(get_all_subclasses(object)) == set([A, B, C, D, E])

# Generated at 2022-06-12 22:48:12.382450
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

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    assert get_all_subclasses(A) == set([b, c, d, e]), 'Get all subclasses failed on A'
    assert get_all_subclasses(B) == set([]), 'Get all subclasses failed on B'
    assert get_all_subclasses(C) == set([d, e]), 'Get all subclasses failed on C'
    assert get_all_subclasses(D) == set([]), 'Get all subclasses failed on D'
    assert get_all_sub

# Generated at 2022-06-12 22:48:22.741255
# Unit test for function get_all_subclasses
def test_get_all_subclasses():

    # Test classes are defined in the current scope
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
    class H(C):
        pass
    class I(D):
        pass
    class J(I):
        pass

    # Defining expected output
    expected_result = set([D, E, F, G, H, I, J])

    # Comparing expected result to function output
    assert (get_all_subclasses(A) == expected_result)

# Generated at 2022-06-12 22:48:49.678988
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
    assert get_all_subclasses(D) == set([])
    assert get_all_subclasses(E) == set([])
    assert get_all_subclasses(F) == set([])


# Generated at 2022-06-12 22:48:51.759874
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from collections import Iterable
    from ansible.plugins.action.normal import ActionModule as ActionModule_normal

    assert isinstance(get_all_subclasses(ActionModule_normal), Iterable)



# Generated at 2022-06-12 22:48:59.766391
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
    class F(E):
        pass

    assert set(get_all_subclasses(A)) == set([B,C,D,E,F])
    assert set(get_all_subclasses(B)) == set([C,D,E,F])
    assert set(get_all_subclasses(C)) == set([])
    assert set(get_all_subclasses(D)) == set([E,F])
    assert set(get_all_subclasses(E)) == set([F])
    assert set(get_all_subclasses(F)) == set([])

# Generated at 2022-06-12 22:49:05.619883
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Define classes A, B, C and D where C and D are subclasses of B, and B is a subclass of A
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(B):
        pass

    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)
    assert B in get_all_subclasses(A)
    assert A not in get_all_subclasses(A)

# Generated at 2022-06-12 22:49:11.176841
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

    assert set(get_all_subclasses(A)) == set([A, B, C, D, E])
    assert set(get_all_subclasses(B)) == set([B, E])
    assert set(get_all_subclasses(D)) == set([D])

# Make sure that if a module is called as a script, it does not run
# the test code (and thus fail because of missing imports)
if __name__ != "__main__":
    test_get_all_subclasses()

# Generated at 2022-06-12 22:49:20.773365
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a simple class/subclasses tree
    class Base(object):
        pass

    class Intermediate0(Base):
        pass

    class Intermediate1(Base):
        pass

    class Intermediate2(Base):
        pass

    class Intermediate3(Base):
        pass

    class Intermediate4(Intermediate2):
        pass

    class Intermediate5(Intermediate2):
        pass

    class Intermediate6(Intermediate5):
        pass

    class Intermediate7(Intermediate6):
        pass

    class Intermediate8(Intermediate4):
        pass

    class Intermediate9(Intermediate0):
        pass

    class Leaf0(Intermediate0):
        pass

    class Leaf1(Intermediate0):
        pass

    class Leaf2(Intermediate0):
        pass

    class Leaf3(Intermediate1):
        pass


# Generated at 2022-06-12 22:49:23.139524
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

    assert set(get_all_subclasses(A)) == set([B, C, D, E])

# Generated at 2022-06-12 22:49:25.267053
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    assert set([B, C]) == get_all_subclasses(A)

# Generated at 2022-06-12 22:49:31.021957
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Performs a unit test of the :py:func:`get_all_subclasses` function.
    '''
    import unittest
    class GrandparentClass(object):
        pass
    class ParentClassA(GrandparentClass):
        pass
    class ParentClassB(GrandparentClass):
        pass
    class ChildClassA(ParentClassA):
        pass
    class ChildClassB(ParentClassA):
        pass

    class TestGetAllSubclasses(unittest.TestCase):
        def test_subclasses(self):
            self.assertEqual(
                get_all_subclasses(GrandparentClass),
                set([ParentClassA, ParentClassB, ChildClassA, ChildClassB])
            )

# Generated at 2022-06-12 22:49:39.331985
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    '''
    Test get_all_subclasses.  To run all of the unit tests for this file, run this command:

    `python -m ansible_test units/utils/_utils`
    '''
    import inspect

    # Define a test class
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    class E(B,C): pass

    # Determine the current path of the file
    current_path = inspect.getfile(inspect.currentframe())

    # Set the expected subclasses
    expected = set([B, C, D, E])

    # Execute the function
    actual = get_all_subclasses(A)

    # Ensure that the subclasses are the same

# Generated at 2022-06-12 22:50:34.745223
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    from ansible.module_utils.facts import collected

    collected_subclasses = get_all_subclasses(collected.BaseFactsCollectionPlugin)
    assert collected.LinuxDistributionFacts in collected_subclasses
    assert collected.VirtualFacts in collected_subclasses
    assert collected.HardwareFacts in collected_subclasses

    collected_subclasses = get_all_subclasses(collected.GatherSubsetFacts)
    assert collected.DpkgFacts in collected_subclasses

    collected_subclasses = get_all_subclasses(collected.AllSubsetFacts)
    assert collected.NetworkFacts in collected_subclasses
    assert collected.PythonFacts in collected_subclasses
    assert collected.HardwareFacts in collected_subclasses
    assert collected.VirtualFacts in collected_subclasses

# Generated at 2022-06-12 22:50:40.280304
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    ''' Unit test for function get_all_subclasses '''

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    # The list is not empty
    assert get_all_subclasses(A) != []

    # The list contains the good classes
    assert B in get_all_subclasses(A)
    assert C in get_all_subclasses(A)
    assert D in get_all_subclasses(A)

# Generated at 2022-06-12 22:50:46.852240
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Create a dummy class hierarchy
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

    assert get_all_subclasses(A) == {B,C,D,E}
    assert get_all_subclasses(B) == {D,E}
    assert get_all_subclasses(C) == set()
    assert get_all_subclasses(D) == {E}
    assert get_all_subclasses(E) == set()

# Generated at 2022-06-12 22:50:51.135872
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class TestClassA(object):
        pass

    class TestClassB(TestClassA):
        pass

    class TestClassC(TestClassA):
        pass

    class TestClassD(TestClassC):
        pass

    assert {TestClassB, TestClassC, TestClassD} == get_all_subclasses(TestClassA)
    assert {TestClassD} == get_all_subclasses(TestClassC)

# Generated at 2022-06-12 22:50:53.514918
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

# Generated at 2022-06-12 22:51:01.104168
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    # Simple prototyping for implementing testing of get_all_subclasses()
    class a:
        pass

    class b(a):
        pass

    class c(a):
        pass

    class d(c):
        pass

    class e(a):
        pass

    class f(e):
        pass

    class g:
        pass

    assert a in get_all_subclasses(object)

    assert set((b, c, d, e, f)) == get_all_subclasses(a)
    assert set((d, f)) == get_all_subclasses(e)
    assert set((d,)) == get_all_subclasses(c)

    assert get_all_subclasses(g) == set()