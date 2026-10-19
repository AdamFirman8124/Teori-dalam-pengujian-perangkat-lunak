

# Generated at 2022-06-13 16:46:45.789553
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.data = []

        def add(self, val):
            self.data.append(val)

    t1 = Test()
    t1.add("foo")
    assert t1.data == ["foo"]

    t2 = Test()
    assert t1.data == t2.data

    t2.add("bar")
    assert t1.data == ["foo", "bar"]

    t3 = Test()
    assert t1.data == t3.data
    assert t3.data == t2.data

    # assert singleton attributes are writable
    t1.data = None
    assert t1.data is None
    assert t2.data is None
    assert t3.data is None

    #

# Generated at 2022-06-13 16:46:47.413667
# Unit test for constructor of class Singleton
def test_Singleton():
    class Temp(object):
        __metaclass__ = Singleton

    temp1 = Temp()
    temp2 = Temp()
    assert temp1 is temp2

# Generated at 2022-06-13 16:46:48.874976
# Unit test for constructor of class Singleton
def test_Singleton():
    assert issubclass(Singleton, type)
    assert isinstance(Singleton, Singleton)

# Generated at 2022-06-13 16:46:53.168419
# Unit test for constructor of class Singleton
def test_Singleton():

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'Value'

    def get_instance():
        instance = TestSingleton()
        return instance.name

    assert get_instance() == 'Value'
    assert get_instance() == 'Value'

# Generated at 2022-06-13 16:46:59.107315
# Unit test for constructor of class Singleton
def test_Singleton():
    from collections import defaultdict

    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.data = defaultdict(int)

        def increment(self, key):
            self.data[key] += 1

    t1 = Test()
    t2 = Test()
    assert(t1 is t2)

    t1.increment('count')
    assert(t1.data['count'] == 1)

    t2.increment('count')
    assert(t1.data['count'] == 2)

# Generated at 2022-06-13 16:47:00.162576
# Unit test for constructor of class Singleton
def test_Singleton():
    assert Singleton

# Generated at 2022-06-13 16:47:03.430961
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 2

    assert(id(A()) == id(A()))

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:14.970408
# Unit test for constructor of class Singleton
def test_Singleton():
    from units.compat import TestCase
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    class B(A):
        def __init__(self):
            pass

    class C(B):
        def __init__(self):
            pass

    class D(B):
        def __init__(self, value):
            self.value = value
            pass

    class E(D):
        def __init__(self, value, value2):
            self.value2 = value2
            # Call to __init__ of B
            super(E, self).__init__(value)

    a1 = A()
    a2 = A()

    assert a1 is a2

    b1 = B()
    b2 = B()

    assert b1

# Generated at 2022-06-13 16:47:16.608442
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    instance = Test()
    assert(instance == Test())

# Generated at 2022-06-13 16:47:18.434096
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest:
        __metaclass__ = Singleton

    x = SingletonTest()
    y = SingletonTest()
    assert x is y

# Generated at 2022-06-13 16:47:24.673627
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class test_A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 1

    a = test_A()
    b = test_A()
    assert a.x == b.x

# Generated at 2022-06-13 16:47:33.700856
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            super(Test, self).__init__()

    import unittest

    class TestSingleton(unittest.TestCase):
        def test_singleton(self):
            t1 = Test()
            t2 = Test()
            t3 = Test()
            self.assertEqual(t1, t2)
            self.assertEqual(t1, t3)
            self.assertEqual(t2, t3)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSingleton)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 16:47:40.868145
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        """Normal object"""
        pass

    class B(object):
        """Singleton"""
        __metaclass__ = Singleton

    # test object A
    a = A()
    assert id(a) == id(A())

    # test object B
    b = B()
    assert id(b) == id(B())

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:47:45.721075
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class S:
        """Example class for testing Singleton functionality."""
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    assert S(1) is not S(2)
    assert S(1).x == 1
    assert S(2).x == 2
    assert S(3).x == 2



# Generated at 2022-06-13 16:47:53.230466
# Unit test for constructor of class Singleton
def test_Singleton():
	
	# Singleton call
	class A (metaclass=Singleton):
		def __init__(self):
			self.color = "Red"

	# Create an instance of A class
	a = A()

	# Assert that the color is red
	try:
		assert a.color == 'Red'
		print("Singleton Class created successfully!")
	except:
		print("Singleton class not created!")

if __name__ == "__main__":

	# Unit test function
	test_Singleton()

# Generated at 2022-06-13 16:47:56.987002
# Unit test for constructor of class Singleton
def test_Singleton():
	class MySingle(metaclass=Singleton):
		name = "MySingle"
		def __init__(self):
			self.name = MySingle.name

	assert MySingle() == MySingle()

# Generated at 2022-06-13 16:48:04.470239
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        # __metaclass__ = Singleton
        pass

    class B(object):
        __metaclass__ = Singleton

    class C(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    class D(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a = A()
    b = B()
    c = C()
    d = D()

    assert a is not A()
    assert b is B()
    assert c is C()
    assert d is D()


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:48:06.989895
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    one = Foo()
    two = Foo()

    assert one == two

# Generated at 2022-06-13 16:48:11.054455
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 3


    assert SingletonTestClass() == SingletonTestClass()
    assert SingletonTestClass().value == 3
    assert SingletonTestClass().value == 3




# Generated at 2022-06-13 16:48:13.388083
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 5

    assert A() is A()
    assert A().x is 5


# Generated at 2022-06-13 16:48:21.101833
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
    a = TestClass()
    b = TestClass()
    return (a is b)


# Generated at 2022-06-13 16:48:31.483760
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class_A = Singleton(name="Class_A", bases=(object,), dict={})
    class_B = Singleton("Class_B", (object,), {})
    class_C = Singleton("Class_C", (object,), {'name': "Class_C"})

    obj_A0 = class_A()
    obj_B0 = class_B()
    obj_C0 = class_C()

    assert obj_A0 is class_A()
    assert obj_B0 is class_B()
    assert obj_C0 is class_C()

    assert obj_A0 is not obj_B0
    assert obj_B0 is not obj_C0
    assert obj_C0 is not obj_A0


# Generated at 2022-06-13 16:48:36.413588
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    global __class_call__
    __class_call__ = 0
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            global __class_call__
            __class_call__ += 1

    assert __class_call__ == 0, "A was unexpectedly initialized"
    A()
    assert __class_call__ == 1, "A was unexpectedly initialized"
    A()
    assert __class_call__ == 1, "A was unexpectedly initialized"
    A()
    assert __class_call__ == 1, "A was unexpectedly initialized"



# Generated at 2022-06-13 16:48:40.089140
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    a = object.__new__(Singleton)
    print(a)
    #b = object.__new__(Singleton)
    #print(b)

if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:48:43.547742
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 42

    a1 = A()
    a2 = A()

    assert a1 is a2
    assert a1.foo == 42
    assert a2.foo == 42

# Generated at 2022-06-13 16:48:46.494497
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    t1 = TestSingleton()
    t2 = TestSingleton()
    assert t1 == t2



# Generated at 2022-06-13 16:48:49.644515
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    assert MyClass() is MyClass()


# Generated at 2022-06-13 16:48:52.742945
# Unit test for constructor of class Singleton
def test_Singleton():
    # Create a class called 'class1' and let it inherit from the class Singleton
    class class1(metaclass=Singleton):
        pass
    
    assert class1() is class1()

# Generated at 2022-06-13 16:48:56.068748
# Unit test for constructor of class Singleton
def test_Singleton():
    class SS(object):
        __metaclass__ = Singleton

    a = SS()
    b = SS()
    c = SS()

    assert id(a) == id(b)
    assert id(b) == id(c)
    assert id(c) == id(a)

# Generated at 2022-06-13 16:49:00.727893
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self):
            self.x = 22
            self.y = 32

    a1 = A()
    a2 = A()
    assert a1 is a2
    assert a1.x == a2.x
    assert a1.y == a2.y


# Generated at 2022-06-13 16:49:12.574715
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 'a'
            self.b = 'b'

    t = TestSingleton()
    assert t.a == 'a'
    assert t.b == 'b'

# Generated at 2022-06-13 16:49:15.953748
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo():
        __metaclass__ = Singleton
        pass
    foo_1 = Foo()
    foo_2 = Foo()
    assert foo_1 is foo_2
    assert foo_1 == foo_2
    return

# Generated at 2022-06-13 16:49:19.051705
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 1

    tc1 = TestClass()
    tc2 = TestClass()

    assert tc1.x == 1
    assert tc2.x == 1

    tc1.x = 2

    assert tc2.x == 2
    assert tc1 is tc2



# Generated at 2022-06-13 16:49:24.445159
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Data:
        __metaclass__ = Singleton

        def __init__(self, *args, **kwargs):
            super(Data, self).__init__(*args, **kwargs)
            self.data = {}

        def __getitem__(self, key):
            return self.data.__getitem__(key)

        def __setitem__(self, key, value):
            return self.data.__setitem__(key, value)

    a = Data()
    b = Data()
    a['foo'] = 'bar'
    assert a['foo'] == 'bar'
    assert b['foo'] == 'bar'

    del a
    del b


# Generated at 2022-06-13 16:49:28.176147
# Unit test for constructor of class Singleton
def test_Singleton():
    class NonSingletonClass(object):
        __metaclass__ = Singleton

    t1 = NonSingletonClass()
    t2 = NonSingletonClass()
    assert t1 == t2
    t3 = NonSingletonClass()
    assert t2 == t3
    assert t1 == t3

test_Singleton()

# Generated at 2022-06-13 16:49:30.137455
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
    assert TestSingleton() == TestSingleton()

# Generated at 2022-06-13 16:49:33.074536
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()
    assert A() is A()
    assert A() is A()

# Generated at 2022-06-13 16:49:35.544342
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(metaclass=Singleton):
        pass

    instance1 = MyClass()
    instance2 = MyClass()
    assert(instance1 is instance2)



# Generated at 2022-06-13 16:49:38.473437
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.var = 'test'

    a = TestSingleton()
    b = TestSingleton()
    assert a == b
    assert a is b

# Generated at 2022-06-13 16:49:46.697563
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    # Create an instance of Singleton class
    class_to_test = Singleton('ClassA', (object, ), {})

    # Try to create two instances of class_to_test
    singleton_class_instance_1 = class_to_test()
    singleton_class_instance_2 = class_to_test()

    # Check if we have a Singleton class
    assert singleton_class_instance_1 is singleton_class_instance_2



# Generated at 2022-06-13 16:50:07.280347
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from unittest import TestCase
    import mock

    class Foo(object):
        __metaclass__ = Singleton

    foo = Foo()
    with mock.patch.object(Foo, '__call__') as mock_call:
        foo = Foo()
        self.assertFalse(mock_call.called)
        self.assertEqual(foo, Foo())
        self.assertTrue(mock_call.called)


# Generated at 2022-06-13 16:50:14.912267
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Test setup
    class TestSingletonClass(object):
        __metaclass__ = Singleton

    class TestSingletonClassWithArgs(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

    # Test __call__ with a class without args and assert
    assert isinstance(TestSingletonClass(), TestSingletonClass)
    # Test __call__ with a class with args and assert
    assert isinstance(TestSingletonClassWithArgs('name'), TestSingletonClassWithArgs)



# Generated at 2022-06-13 16:50:19.815882
# Unit test for constructor of class Singleton
def test_Singleton():

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, x=None):
            self.x = x

    tmp1 = TestSingleton()
    tmp2 = TestSingleton()
    # tmp2.x is not defined
    assert tmp1 == tmp2

# Generated at 2022-06-13 16:50:22.431285
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a is b



# Generated at 2022-06-13 16:50:31.805542
# Unit test for constructor of class Singleton
def test_Singleton():
    # create class
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, *args, **kwargs):
            self._args = args
            self._kwargs = kwargs

        def __repr__(self):
            # repr of class will contain repr of args and repr of kwargs
            args = ''.join([repr(i) for i in self._args])
            kwargs = ''.join([key + '=' + repr(value) + ', ' for key, value in self._kwargs.items()])
            return 'TestSingleton(' + args + kwargs + ')'

    # Normally you would use an instance of a class like this
    # class TestSingleton(object):
    #     def __init__(self, *args, **kwargs):
   

# Generated at 2022-06-13 16:50:35.323177
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        pass

    instance1 = TestSingleton()
    instance2 = TestSingleton()

    return instance1 is instance2


# Generated at 2022-06-13 16:50:37.652400
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    t1 = Test()
    t2 = Test()
    assert t1 == t2



# Generated at 2022-06-13 16:50:41.480425
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Create a class inheriting from Singleton
    class MyClass(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

    MyClass('one')
    MyClass('two')
    assert MyClass.__instance.value == 'one'


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:50:46.163874
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    cnt = 0

    class A(metaclass=Singleton):
        def __init__(self):
            # Count the number of times we've instantiated A.
            nonlocal cnt
            cnt += 1

    assert cnt == 0
    a1 = A()
    assert cnt == 1
    a2 = A()
    assert cnt == 1
    a3 = A()
    assert cnt == 1
    assert a1 is a2 is a3


# Generated at 2022-06-13 16:50:50.721579
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a

    obj1 = A("Hello")
    obj2 = A("World")
    assert obj1 == obj2, "Singleton doesn't work"



# Generated at 2022-06-13 16:51:30.079518
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = 'Singleton Test'

    first = TestClass()
    second = TestClass()

    assert id(first) == id(second)
    assert first.name == 'Singleton Test'
    assert second.name == 'Singleton Test'

# Generated at 2022-06-13 16:51:32.828541
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    a2 = A()
    assert a == a2
    assert a is a2


# Generated at 2022-06-13 16:51:35.585802
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(metaclass=Singleton):
        def __init__(self):
            self.attr1 = 1

    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2
    assert m1.attr1 == m2.attr1



# Generated at 2022-06-13 16:51:40.417796
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.abc = 123

    obj1 = Singleton('TestClass', None, None)()
    assert obj1.__class__ == TestClass

    obj2 = Singleton('TestClass', None, None)()
    assert obj2.__class__ == TestClass

    assert obj1 == obj2


if __name__ == "__main__":
    import nose
    nose.runmodule()

# Generated at 2022-06-13 16:51:42.684054
# Unit test for constructor of class Singleton
def test_Singleton():
    class C(object):
        __metaclass__ = Singleton

    x = C()
    y = C()
    assert x is y

# Generated at 2022-06-13 16:51:46.538869
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Dummy(object):
        __metaclass__ = Singleton

        def __init__(self, argument):
            self.argument = argument

    dummy1 = Dummy(1)
    dummy2 = Dummy(2)

    assert dummy1 == dummy2
    assert dummy1.argument == dummy2.argument
    assert dummy1.argument == 2



# Generated at 2022-06-13 16:51:53.433106
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import os
    from ansible.module_utils._text import to_bytes

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, path_to_file):
            self._path_to_file = path_to_file
            self._content = to_bytes(os.urandom(32))

        def get_content(self):
            return self._content

    path_to_file1 = os.urandom(128)
    path_to_file2 = os.urandom(128)

    x = TestSingleton(path_to_file1)
    x_ref = TestSingleton(path_to_file1)
    y = TestSingleton(path_to_file2)

    assert x is x_ref
    assert x is not y
    assert x.get

# Generated at 2022-06-13 16:51:55.423027
# Unit test for constructor of class Singleton
def test_Singleton():
    __metaclass__ = Singleton
    assert len(class_Singleton.__instance) == 0, "the class_Singleton instance shouldn't be there"

# Generated at 2022-06-13 16:52:01.041696
# Unit test for constructor of class Singleton
def test_Singleton():
    # pylint: disable=import-error, no-name-in-module
    from .test.inventory_tests import InventoryModuleTestCase
    # pylint: enable=import-error, no-name-in-module

    class TestSingleton(InventoryModuleTestCase):
        """Test class based on Singleton."""

    # Create a singleton.
    singleton = TestSingleton()
    # Create a new singleton, which should return the first singleton.
    new_singleton = TestSingleton()

    assert singleton is new_singleton

# Generated at 2022-06-13 16:52:05.340526
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a = A()
    assert(a) is A()


if __name__ == '__main__':
    # Unit test for method __call__ of class Singleton
    test_Singleton___call__()

# Generated at 2022-06-13 16:53:14.641334
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

    s1 = SingletonTest()
    s2 = SingletonTest()
    return (s1 == s2)

# Generated at 2022-06-13 16:53:21.944251
# Unit test for constructor of class Singleton
def test_Singleton():
    class test_class(object):
        __metaclass__ = Singleton

        def __init__(self, init_value = 0):
            self.value = init_value

        def add(self, x):
            self.value += x

    a = test_class(3)
    assert a.value == 3
    a.add(5)
    assert a.value == 8
    b = test_class()
    assert b.value == 8
    b.add(10)
    assert b.value == 18
    assert a.value == 18
    c = test_class()
    assert a is c

# Generated at 2022-06-13 16:53:23.443046
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
    a = Foo()
    b = Foo()
    assert a is b

# Generated at 2022-06-13 16:53:28.437447
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            super(Foo, self).__init__()

        def foo(self):
            pass

    foo = Foo()
    assert(foo.foo)

    foo1 = Foo()

    assert(foo is foo1)  # Both Foo() instances should point to the same object


# Generated at 2022-06-13 16:53:32.620858
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, x=0):
            self.x = x

    instance1 = Test(3)
    instance2 = Test(4)
    assert instance1 == instance2

    instance1.x = 5
    assert instance2.x == 5

    instance2.y = 7
    assert instance1.y == 7

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:53:35.585916
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1

    a = A()

    assert a.a == 1
    assert A() is a
    assert a is A()
    a.b = 2
    assert A().b == 2



# Generated at 2022-06-13 16:53:40.122522
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = "foo"

    f = MyClass()
    f2 = MyClass()

    assert f.x == f2.x
    assert f is f2

# Generated at 2022-06-13 16:53:42.332118
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.val = 10
        def say(self):
            print('Hello')

    class B(object):
        __metaclass__ = Singleton

    a = A()
    b = B()
    print(str(a) + " " + str(b))

# Generated at 2022-06-13 16:53:45.336982
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    f1 = Foo()
    f2 = Foo()
    assert f1 is f2

# Generated at 2022-06-13 16:53:51.788132
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, a=1, b=2, c=3):
            self.a, self.b, self.c = a, b, c
            self.init_cnt = getattr(self.__class__, 'init_cnt', 0) + 1
            self.__class__.init_cnt = self.init_cnt

    # Declare a new class, based on the old class
    class Bar(Foo):
        pass

    assert Foo() is Foo()  # Same class
    assert Foo() is not Bar()  # Different classes
    assert Foo(b=20, c=30) is Foo()  # Same class, different init args

    # Make sure __init__ was only called once for each class
    assert Foo.init_

# Generated at 2022-06-13 16:56:19.584643
# Unit test for constructor of class Singleton
def test_Singleton():
    # test metaclass
    class C1(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value
            print("C1 constructor called")

    a = C1("test string")
    print("end of C1")
    b = C1("test string2")
    print("end of C1")

    class C2(C1):
        def __init__(self, value):
            C1.__init__(self, value)
            print("C2 constructor called")

    c = C2("test string3")
    print("end of C2")

    assert a.value == b.value
    assert a.value != c.value

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:56:24.124283
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, x, y):
            self.x = x
            self.y = y

    a = A(1, 2)
    b = A(1, 2)
    assert a == b
    assert id(a) == id(b)



# Generated at 2022-06-13 16:56:26.882101
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__= Singleton
        def __init__(self, name):
            self.name = name
            A.__instance = self

    a = A(1)
    assert a == A(1)
    assert a.name == 1



# Generated at 2022-06-13 16:56:29.488420
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Tmp(object):
        __metaclass__ = Singleton
    instance1=Tmp()
    instance2=Tmp()
    assert instance1 is instance2

if __name__ == "__main__":
    test_Singleton___call__()