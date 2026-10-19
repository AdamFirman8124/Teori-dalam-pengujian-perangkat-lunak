

# Generated at 2022-06-13 16:10:07.908778
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(1, 100) == 1
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('10%', 100, min_value=2) == 10
    assert pct_to_int('1%', 100) == 1
    assert pct_to_int('1%', 100, min_value=2) == 2


# Generated at 2022-06-13 16:10:15.891750
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('100%', 100) == 100
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int('1%', 100) == 1
    assert pct_to_int('0%', 100) == 1
    assert pct_to_int('10', 100) == 10
    assert pct_to_int('120', 100) == 120


# Generated at 2022-06-13 16:10:22.457990
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 10) == 5
    assert pct_to_int('50.5%', 10) == 5
    assert pct_to_int('50.25%', 10) == 5
    assert pct_to_int('50.75%', 10) == 6
    assert pct_to_int('100%', 10) == 10
    assert pct_to_int('100%', 10, 5) == 10
    assert pct_to_int('0%', 10) == 1



# Generated at 2022-06-13 16:10:28.105497
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int(50, 100) == 50
    assert pct_to_int(6, 10) == 6
    assert pct_to_int('6%', 10) == 0
    assert pct_to_int('6%', 10, min_value=2) == 2
    assert pct_to_int('6%', 10, min_value=1) == 1

# Generated at 2022-06-13 16:10:31.221256
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(75, 100) == 75
    assert pct_to_int(50, 200) == 100
    assert pct_to_int('15%', 100) == 15

# Generated at 2022-06-13 16:10:39.175291
# Unit test for function pct_to_int
def test_pct_to_int():
    print("Testing conversion of percentage to integer")
    assert pct_to_int('50%', 10) == 5
    assert pct_to_int('100%', 10) == 10
    assert pct_to_int('100%', 5) == 5
    assert pct_to_int('50%', 5) == 3
    assert pct_to_int('1%', 5) == 1
    assert pct_to_int(5, 10, 1) == 5


# Generated at 2022-06-13 16:10:45.139549
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int("10%", 10) == 1
    assert pct_to_int("10%", 2000) == 200
    assert pct_to_int("10%", 2000, min_value=10) == 10
    assert pct_to_int("10%", 1) == 1
    assert pct_to_int("1%", 100000) == 1000
    assert pct_to_int("1%", 100000, min_value=1) == 1
    assert pct_to_int("1000%", 100) == 100

# Generated at 2022-06-13 16:10:48.140663
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Create a list with duplicates
    input_list = [1, 2, 3, 2, 1]

    # Retrieve the deduplicated list
    output_list = deduplicate_list(input_list)

    assert list(output_list) == [1, 2, 3]

# Generated at 2022-06-13 16:10:55.357451
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(20, 10) == 2
    assert pct_to_int(25, 10) == 2
    assert pct_to_int('50%', 10) == 5
    assert pct_to_int('50%', 10, min_value=2) == 2
    assert pct_to_int('75%', 10) == 7
    assert pct_to_int(1, 10) == 1
    assert pct_to_int('1%', 10) == 1
    assert pct_to_int(100, 10) == 10
    assert pct_to_int('100%', 10) == 10
    assert pct_to_int('101%', 10) == 11
    assert pct_to_int(0, 10, min_value=1) == 1
    assert pct_

# Generated at 2022-06-13 16:10:57.685470
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('20%', 200) == 40
    assert pct_to_int('20%', 100) == 20
    assert pct_to_int(10, 100) == 10


# Generated at 2022-06-13 16:11:05.025192
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['cat', 'dog', 'cat', 'bird', 'monkey', 'turtle', 'dog', 'bird']
    result = ['cat', 'dog', 'bird', 'monkey', 'turtle']
    assert deduplicate_list(original_list) == result
    return


# Generated at 2022-06-13 16:11:11.682975
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo(object):
        def __init__(self):
            self.foo = "foo"
            self.bar = "bar"
            self.baz = "baz"
            self.qux = "qux"

    f = Foo()
    # Test without exclude
    result = object_to_dict(f)
    assert result == {'foo': 'foo', 'bar': 'bar', 'baz': 'baz', 'qux': 'qux'}

    # Test with exclude
    result = object_to_dict(f, exclude=['foo', 'bar'])
    assert result == {'baz': 'baz', 'qux': 'qux'}

# Generated at 2022-06-13 16:11:17.565570
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 4, 1, 2, 3]
    expected_list = [1, 2, 3, 4]
    result_list = deduplicate_list(original_list)
    if isinstance(result_list, list) and result_list == expected_list:
        return True
    else:
        return False

assert test_deduplicate_list() == True

# Generated at 2022-06-13 16:11:20.079491
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['foo', 'bar', 'baz', 'foo', 'bar']
    assert deduplicate_list(original_list) == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:11:22.377205
# Unit test for function object_to_dict
def test_object_to_dict():
    """Tests converting an object to a dict"""
    class MyClass():
        a = 'test'
        b = ''
        c = None

    converted = object_to_dict(MyClass())
    assert converted['a'] == 'test'
    assert converted['b'] == ''
    assert converted['c'] == None

# Generated at 2022-06-13 16:11:26.504480
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1,1,1]) == [1]
    assert deduplicate_list([1,2,3]) == [1,2,3]
    assert deduplicate_list([1,2,1,2,3]) == [1,2,3]
    assert deduplicate_list([1,1,2,3,1,2]) == [1,2,3]
    assert deduplicate_list([1,2,3,1,2,1,2,3,1,2,1,2,3]) == [1,2,3]

# Generated at 2022-06-13 16:11:34.856189
# Unit test for function object_to_dict
def test_object_to_dict():
    class myobj(object):
        def __init__(self):
            self.test = "test"
            self.test2 = "test2"
            self.test3 = "test3"
    a = myobj()

    assert object_to_dict(a) == {'test': 'test', 'test2': 'test2', 'test3': 'test3'}
    assert object_to_dict(a, exclude=['test']) == {'test2': 'test2', 'test3': 'test3'}

# Generated at 2022-06-13 16:11:38.408313
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.var1 = 'test1'
            self.var2 = 'test2'
            self.var3 = 'test3'
            self.var4 = 'test4'


    test_obj = TestObject()
    result = object_to_dict(test_obj, exclude=['var2', 'var3'])

    assert result['var1'] == 'test1'
    assert 'var2' not in result
    assert 'var3' not in result


# Generated at 2022-06-13 16:11:49.641611
# Unit test for function deduplicate_list
def test_deduplicate_list():
    import unittest

    class TestDeduplicateList(unittest.TestCase):

        def test_duplicates_at_top(self):
            self.assertEqual(deduplicate_list([1, 2, 3, 2, 1]), [1, 2, 3])

        def test_duplicates_at_bottom(self):
            self.assertEqual(deduplicate_list([1, 2, 3, 1, 2]), [1, 2, 3])

        def test_duplicates_in_middle(self):
            self.assertEqual(deduplicate_list([1, 2, 3, 3, 2, 1]), [1, 2, 3])


# Generated at 2022-06-13 16:11:56.449904
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        test_prop = "test_value"
        test_prop2 = "test_value2"

    obj = TestClass()
    assert object_to_dict(obj) == {'test_prop': 'test_value', 'test_prop2': 'test_value2'}
    assert object_to_dict(obj, exclude=["test_prop"]) == {'test_prop2': 'test_value2'}

# Generated at 2022-06-13 16:12:06.892605
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        a = 1
        b = 2
        c = 3
        d = 4
    test = Test()
    assert object_to_dict(test, ['a','b']) == {'c': 3, 'd': 4}



# Generated at 2022-06-13 16:12:11.458192
# Unit test for function object_to_dict
def test_object_to_dict():
    obj = {'attr1': 'a', 'attr2': 'b', 'attr3': 'c'}
    res = object_to_dict(obj)
    assert res == obj
    res = object_to_dict(obj, exclude=['attr2'])
    assert res.get('attr2') is None
    assert res.get('attr1') == 'a'


# Generated at 2022-06-13 16:12:14.369254
# Unit test for function deduplicate_list
def test_deduplicate_list():
    a = ['cat', 'dog', 'dog', 'dog', 'fish', 'fish', 'fish', 'cat']
    deduplicated_list = deduplicate_list(a)
    assert deduplicated_list == ['cat', 'dog', 'fish']


# Generated at 2022-06-13 16:12:25.332848
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Test for the function object_to_dict.
    """

    # Dummy class for testing
    class DummyClass(object):
        """An object with some properties for testing."""
        def __init__(self):
            self.property1 = '1'
            self.property2 = '2'
            self.property3 = '3'
            self._property4 = '4'

    # Create the object with some properties
    dummy_object = DummyClass()

    # Call the function and assert that it returned the correct dictionary
    got_dict = object_to_dict(dummy_object)
    assert got_dict == {'property1': '1', 'property2': '2', 'property3': '3'}

    # Call the function with exclusion, and assert that it returned the correct dictionary
    got_dict = object

# Generated at 2022-06-13 16:12:34.084573
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list1 = [1,2,2,2,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    assert deduplicate_list(list1) == [1,2,3,4,5]
    list2 = ['1','2','3','3','3','3','3']
    assert deduplicate_list(list2) == ['1', '2', '3']

# Generated at 2022-06-13 16:12:37.366961
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['1', '1', '2', '3', '4', '4', '4']
    dedupe_list = deduplicate_list(original_list)
    assert dedupe_list == ['1', '2', '3', '4']



# Generated at 2022-06-13 16:12:43.431417
# Unit test for function object_to_dict
def test_object_to_dict():
    class ObjectToConvert:
        def __init__(self):
            self.property_one = 1
            self.property_two = 2
            self.property_three = 3

    obj = ObjectToConvert()
    d = object_to_dict(obj, exclude=['property_one'])
    assert('property_one' not in d)
    assert(d['property_two'] == 2)



# Generated at 2022-06-13 16:12:48.481590
# Unit test for function object_to_dict
def test_object_to_dict():
    # Test case 1
    class MyClass:
        def __init__(self, val1, val2, val3):
            self.val1 = val1
            self.val2 = val2
            self.val3 = val3

    test_obj = MyClass(val1=1, val2=2, val3=3)
    assert(object_to_dict(test_obj) == {'val2': 2, 'val3': 3, 'val1': 1})

    # Test case 2
    class MyClass:
        def __init__(self, val1, val2, val3):
            self.val1 = val1
            self.val2 = val2
            self.val3 = val3

        def method1(self):
            pass


# Generated at 2022-06-13 16:12:50.841949
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 2, 2, 5]) == [1, 2, 3, 5]



# Generated at 2022-06-13 16:12:58.600492
# Unit test for function object_to_dict
def test_object_to_dict():
    class A:
        def __init__(self):
            self.key1 = 'value1'
            self.key2 = 'value2'

    a = A()
    dict_from_a = object_to_dict(a)
    assert dict_from_a['key1'] == 'value1'
    assert dict_from_a['key2'] == 'value2'

    dict_from_a = object_to_dict(a, ['key1'])
    assert dict_from_a['key2'] == 'value2'

    dict_from_a = object_to_dict(a, ['key1', 'key2'])
    assert dict_from_a == {}

# Generated at 2022-06-13 16:13:13.603992
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.test_prop = "test_prop"
            self._test_prop2 = "test_prop2"
            self._test_prop3 = "test_prop3"
            self.excluded_prop = "excluded"

    test_obj = TestClass()
    result = object_to_dict(test_obj, exclude=['excluded_prop'])

    assert 'test_prop' in result
    assert 'excluded_prop' not in result
    assert '_test_prop2' not in result
    assert '_test_prop3' not in result

    result = object_to_dict(test_obj, exclude=['excluded_prop', '_test_prop3'])

    assert 'test_prop' in result

# Generated at 2022-06-13 16:13:23.834738
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        test_attr1 = 'test_attr1'
        test_attr2 = 'test_attr2'
        test_attr3 = 'test_attr3'

    test_object = TestClass()
    assert object_to_dict(test_object) == {
        'test_attr1': 'test_attr1',
        'test_attr2': 'test_attr2',
        'test_attr3': 'test_attr3',
    }
    assert object_to_dict(test_object, exclude=['test_attr1']) == {
        'test_attr2': 'test_attr2',
        'test_attr3': 'test_attr3',
    }

# Generated at 2022-06-13 16:13:28.169818
# Unit test for function object_to_dict
def test_object_to_dict():
    test_class = type('TestClass', (object,), {'foo': 'bar'})
    assert object_to_dict(test_class) == {'foo': 'bar'}
    assert object_to_dict(test_class, ['foo']) == {}
    assert object_to_dict(test_class, exclude=['foo']) == {}


# Generated at 2022-06-13 16:13:30.691140
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 1, 4, 5, 5, 3]
    deduplicated_list = [1, 2, 4, 5, 3]
    assert deduplicate_list(original_list) == deduplicated_list

# Generated at 2022-06-13 16:13:39.070436
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_to_deduplicate = [
        1, 2, 3, 2, 1, "to_deduplicate", 2, 1, 2, 3, 2, 1, 2, 3, 2,
        2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 4, 1,
        2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2,
        3, 2, 1, 2, 3, 2, "to_deduplicate", 1, 2, 3, 3, 1, 2, 3, 4,
        1, 2, 3, 2, 1, 2, 3, 2
    ]
    list_

# Generated at 2022-06-13 16:13:44.164476
# Unit test for function object_to_dict
def test_object_to_dict():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p = Person('John', 35)
    d = object_to_dict(p)

    assert d['name'] == 'John'
    assert d['age'] == 35

# Generated at 2022-06-13 16:13:52.433743
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([3,3,2,2,1,1]) == [3,2,1]
    assert deduplicate_list([3,1,1,2,3]) == [3,1,2]
    assert deduplicate_list([3,1,1,2,3,1,1,2,3,2,2,1,1]) == [3,1,2]
    assert deduplicate_list([1,2,3]) == [1,2,3]
    assert deduplicate_list([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == [1]

# Generated at 2022-06-13 16:14:01.076504
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_object_to_dict(object):
        def __init__(self, test_string, test_int, test_bool):
            self.test_string = test_string
            self.test_int = test_int
            self.test_bool = test_bool
            self._test_non = "test_non"
    expected_dict = {'test_string': 'test string', 'test_int': 1, 'test_bool': True}
    assert (object_to_dict(test_object_to_dict('test string', 1, True)) == expected_dict)
    assert (object_to_dict(test_object_to_dict('test string', 1, True), ['test_int']) == {'test_string': 'test string', 'test_bool': True})


# Generated at 2022-06-13 16:14:05.060153
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [
        1, 2, 3, 3, 4, 5, 1, 5, 6
    ]
    assert deduplicate_list(test_list) == [1, 2, 3, 4, 5, 6]


# Generated at 2022-06-13 16:14:13.025908
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyClass():
        def __init__(self):
            self.property1 = "value1"
            self.property2 = "value2"
            self._property3 = "value3"
            self.property4 = "value4"

    my_class = MyClass()
    exclude_list = ['property4']

    my_dict = object_to_dict(my_class, exclude=exclude_list)
    assert my_dict.has_key('property1')
    assert my_dict.has_key('property2')
    assert not my_dict.has_key('property3')
    assert not my_dict.has_key('property4')

# Generated at 2022-06-13 16:14:25.864427
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'a', 'c', 'd', 'e', 'f', 'e', 'b', 'g', 'a']
    uniqued_list = deduplicate_list(original_list)
    assert uniqued_list == ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Generated at 2022-06-13 16:14:29.484901
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 2, 3, 4, 5]
    assert deduplicate_list(original_list) == [1, 2, 3, 4, 5]

# Generated at 2022-06-13 16:14:35.629107
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test:
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
            self._d = 4
            self._e = 5
            self._f = self._g = 6

    test_object = Test()
    test_object.g = 7
    assert object_to_dict(test_object, ['b', 'f', 'g']) == {'a': 1, 'c': 3, '_d': 4, '_e': 5, '_f': 6, '_g': 6, 'g': 7}


# Generated at 2022-06-13 16:14:39.148506
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['1', '3', '3', '2', '1']
    expected_list = ['1', '3', '2']
    assert(expected_list == deduplicate_list(test_list))

# Generated at 2022-06-13 16:14:44.196262
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from nose.tools import assert_equal
    original_list = ['a', 'b', 'b', 'c', 'd', 'a', 'd', 'e']
    expected_list = ['a', 'b', 'c', 'd', 'e']
    actual_list = deduplicate_list(original_list)
    assert_equal(expected_list, actual_list)

# Generated at 2022-06-13 16:14:55.507823
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([2, 1, 2, 1, 3]) == [2, 1, 3]
    assert deduplicate_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 2, 3, 2, 4, 2, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 2, 3, 2, 4, 2, 5, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]

# Generated at 2022-06-13 16:15:03.347941
# Unit test for function deduplicate_list
def test_deduplicate_list():
    import mock
    import json
    from ansible.module_utils.network_common import deduplicate_list
    from ansible.compat.tests.mock import patch

    original_list = ['a', 'b', 'c', 'b', 'c', 'd', 'a', 'a', 'b', 'c', 'd']
    # 1. Test that the deduplicated_list contains the same items as original_list, and in the same order
    #2. Test that the deduplicated_list and original_list have the same length
    deduplicated_list = deduplicate_list(original_list)
    assert all(x in original_list for x in deduplicated_list)
    assert len(original_list) == len(deduplicated_list)



# Generated at 2022-06-13 16:15:11.661146
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj(object):
        test_key = 'test_value'
        test_excluded_key = 'excluded_value'
    obj = TestObj()
    assert object_to_dict(obj) == {'test_key': 'test_value'}
    assert object_to_dict(obj, exclude=['test_excluded_key']) == {'test_key': 'test_value'}
    assert object_to_dict(obj, exclude=['test_key']) == {}
    assert object_to_dict(obj, exclude=['test_excluded_key', 'test_key']) == {}
    assert object_to_dict(obj, exclude=['test_excluded_key', 'test_invalid_key']) == {'test_key': 'test_value'}


# Generated at 2022-06-13 16:15:19.132842
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo(object):
        def __init__(self):
            self.a = 'b'
            self.b = 'c'
            self._c = 'd'
        def d(self):
            return self.a
        @property
        def e(self):
            return self._c
    o = Foo()
    assert o.a == 'b'
    assert o.b == 'c'
    assert hasattr(o, 'd')
    assert o.e == 'd'
    assert object_to_dict(o) == {'a': 'b', 'b': 'c'}
    assert object_to_dict(o, ['d']) == {'a': 'b', 'b': 'c'}

# Generated at 2022-06-13 16:15:25.110064
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    obj = TestObject('test', 'test2')
    obj_dict = object_to_dict(obj)

    assert obj_dict['a'] == 'test'
    assert obj_dict['b'] == 'test2'



# Generated at 2022-06-13 16:15:51.683923
# Unit test for function object_to_dict
def test_object_to_dict():
    # define an object
    class MyObject(object):
        def __init__(self):
            self.property_one = 'property_one'
            self.property_two = 'property_two'

    # create object
    my_object = MyObject()

    # convert object to dict
    dict_from_object = object_to_dict(my_object)

    # create expected dict
    expected_dict = {'property_one': 'property_one', 'property_two': 'property_two'}

    # assert both dicts are equal
    assert dict_from_object == expected_dict

# Generated at 2022-06-13 16:15:57.656830
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests for the functions  deduplicate_list.
    """
    original_list = [2, 3, 1, 1, 4, 5, 5, 3, 3]
    deduplicated_list = [2, 3, 1, 4, 5]
    assert deduplicate_list(original_list) == deduplicated_list


# Generated at 2022-06-13 16:15:59.596135
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'A', 'a', 'B', 'a']) == ['a', 'A', 'B']

# Generated at 2022-06-13 16:16:08.334336
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1, 1]) == [1]
    assert deduplicate_list(["a", "a", "a", "b", "b"]) == ["a", "b"]
    assert deduplicate_list(["a", "b", "b", "a"]) == ["a", "b"]
    assert deduplicate_list([1, 1, 2, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-13 16:16:12.610612
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'c', 'a', 'b', 'd']
    assert deduplicate_list(original_list) == ['a', 'b', 'c', 'd'], "Expected ['a', 'b', 'c', 'd'], got {0}".format(deduplicate_list(original_list))


# Generated at 2022-06-13 16:16:19.140619
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert deduplicate_list(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list([1, 'a', 2, 'b', 'c', 2, 'a']) == [1, 'a', 2, 'b', 'c']



# Generated at 2022-06-13 16:16:23.353021
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1,1,2,3,3,4,5,6,6,7,8,8,8,7,9]
    expected = [1,2,3,4,5,6,7,8,9]
    actual = deduplicate_list(original_list)
    assert actual == expected


# Generated at 2022-06-13 16:16:26.719474
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ["a", "b", "c", "b", "d", "a", "e"]
    expected_list = ["a", "b", "c", "d", "e"]
    result = deduplicate_list(original_list)
    assert result == expected_list

# Generated at 2022-06-13 16:16:29.318942
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from nose.tools import assert_equal
    assert_equal(deduplicate_list([1, 2, 3, 4, 1, 2]), [1, 2, 3, 4])

# Generated at 2022-06-13 16:16:36.218374
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        def __init__(self):
            self.test = 'test'
            self.foo = 'bar'
            self.baz = None
            self._ignore = 'ignore'

    test_obj = TestClass()
    assert object_to_dict(test_obj) == object_to_dict(test_obj, None)
    assert object_to_dict(test_obj, ['test']) == {'foo': 'bar', 'baz': None}
    assert object_to_dict(test_obj, ['baz']) == {'test': 'test', 'foo': 'bar'}

# Generated at 2022-06-13 16:17:28.994871
# Unit test for function deduplicate_list
def test_deduplicate_list():
    output1 = deduplicate_list([])
    assert len(output1) == 0

    output2 = deduplicate_list([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    assert len(output2) == 5
    assert output2[0] == 1
    assert output2[1] == 2
    assert output2[2] == 3
    assert output2[3] == 4
    assert output2[4] == 5

    output3 = deduplicate_list([4, 2, 6, 2, 3, 2, 1, 5, 4, 3, 6, 5, 1, 4, 6, 5])
    assert len(output3) == 6
    assert output3[0] == 4
    assert output3[1] == 2
    assert output3[2] == 6


# Generated at 2022-06-13 16:17:33.636722
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['A', 'B', 'A', 'C', 'C', 'C', 'A', 'B', 'A']
    dedup_list = deduplicate_list(original_list = test_list)
    assert dedup_list == ['A', 'B', 'C']



# Generated at 2022-06-13 16:17:41.186968
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 1, 1, 2, 2, 3, 4, 5, 5]
    assert(deduplicate_list(test_list) == [1, 2, 3, 4, 5])
    test_list = [1, 2, 3, 4, 5]
    assert(deduplicate_list(test_list) == [1, 2, 3, 4, 5])

# Generated at 2022-06-13 16:17:44.068083
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.foo = 'bar'

    obj = TestClass()
    assert object_to_dict(obj) == {'foo': 'bar'}

# Generated at 2022-06-13 16:17:46.471188
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_1 = ["a", "a", "b", "c", "a", "b", "d"]
    assert deduplicate_list(list_1) == ["a", "b", "c", "d"]


# Generated at 2022-06-13 16:17:49.316932
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 3, 3, 2, 1, 2, 4, 1, 3, 5, 6, 7, 7, 3, 3]) == [1, 3, 2, 4, 5, 6, 7]

# Generated at 2022-06-13 16:17:54.149451
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'c', 'c', 'd']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(['a', 'b', 'c', 'd', 'c']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list([1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]


# Generated at 2022-06-13 16:18:01.720775
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.test = 'object test'
            self.test2 = 'object test2'
            self._test3 = 'object test3'

        def test_method1(self, arg1):
            return arg1

    test_object = TestObject()
    test_object.test4 = 'object test4'
    test_object.test5 = 'object test4'
    test_object.test6 = 'object test4'

    test_object_dict = object_to_dict(test_object, ['test2', 'test2', 5])

    assert 'test' in test_object_dict
    assert 'test2' not in test_object_dict
    assert 'test3' not in test_object_dict
    assert 'test4' in test_object_

# Generated at 2022-06-13 16:18:06.716475
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Test basic case
    original_list = ['a', 'b', 'b', 'd', 'a', 'e']
    expected_list = ['a', 'b', 'd', 'e']
    calculated_list = deduplicate_list(original_list)
    assert expected_list == calculated_list, 'Basic case failed'

    # Test empty list
    original_list = []
    expected_list = []
    calculated_list = deduplicate_list(original_list)
    assert expected_list == calculated_list, 'Empty list case failed'

    # Test single item list
    original_list = ['a']
    expected_list = ['a']
    calculated_list = deduplicate_list(original_list)
    assert expected_list == calculated_list, 'Single item list case failed'

# Unit test

# Generated at 2022-06-13 16:18:18.364980
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.foo = 'foo'
            self.bar = 'bar'
            self._secret = 'secret'
            self._private = 'private'

    test_obj = TestClass()
    obj_dict = object_to_dict(test_obj)
    assert 'foo' in obj_dict.keys()
    assert '_secret' not in obj_dict.keys()
    assert '_private' not in obj_dict.keys()
    obj_dict = object_to_dict(test_obj, exclude=['foo'])
    assert 'foo' not in obj_dict.keys()
    assert '_secret' not in obj_dict.keys()
    assert '_private' not in obj_dict.keys()



# Generated at 2022-06-13 16:19:57.187729
# Unit test for function object_to_dict
def test_object_to_dict():
    class X(object):
        def __init__(self, a, b):
            self.x = a
            self.y = b
        def get_a(self):
            return self.x
        def get_b(self):
            return self.y
        def set_a(self, a):
            self.x = a
        def set_b(self, b):
            self.y = b

    x = X('a','b')
    result = object_to_dict(x)
    assert result.has_key('x')
    assert result.x == 'a'
    assert result.has_key('y')
    assert result.y == 'b'

# Generated at 2022-06-13 16:20:01.494179
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_class:
        prop1 = 'prop1'
        prop2 = 'prop2'
        prop3 = 'prop3'
    test_obj = test_class()
    test_dict = {
        'prop1': 'prop1',
        'prop2': 'prop2',
        'prop3': 'prop3'
    }
    assert object_to_dict(test_obj) == test_dict
    test_dict = {
        'prop1': 'prop1',
        'prop2': 'prop2'
    }
    assert object_to_dict(test_obj, ['prop3']) == test_dict

