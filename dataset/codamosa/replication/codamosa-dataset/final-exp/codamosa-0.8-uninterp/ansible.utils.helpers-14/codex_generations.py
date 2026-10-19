

# Generated at 2022-06-13 16:10:01.840591
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int("100%", 10) == 10
    assert pct_to_int("50%", 10) == 5
    assert pct_to_int("25%", 10) == 3
    assert pct_to_int("10%", 10) == 1
    assert pct_to_int("5%", 10) == 1
    assert pct_to_int("1%", 10) == 1
    assert pct_to_int("0%", 10) == 1
    assert pct_to_int("-1%", 10) == 1
    assert pct_to_int("100%", 0) == 0
    assert pct_to_int("100%", "0") == 0
    assert pct_to_int("100%", None) == 1


# Generated at 2022-06-13 16:10:05.877766
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests the deduplicate_list function.
    """
    original_list = [1, 2, 3, 1, 3, 4, 1]
    assert deduplicate_list(original_list) == [1, 2, 3, 4]

# Generated at 2022-06-13 16:10:16.118675
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(100, 1000) == 1000
    assert pct_to_int("100%", 1000) == 1000
    assert pct_to_int("10%", 1000) == 100
    assert pct_to_int("10%", 0) == 1
    assert pct_to_int("10%", 1) == 1
    assert pct_to_int("10%", 999) == 100
    assert pct_to_int("10%", 1000) == 100
    assert pct_to_int("10%", 1001) == 101
    assert pct_to_int("10%", float("inf")) == 100
    assert pct_to_int(1, 1000) == 1
    assert pct_to_int("1", 1000) == 1

# Generated at 2022-06-13 16:10:26.497842
# Unit test for function pct_to_int
def test_pct_to_int():
    test_data = (
        # test_value, num_items, min_value, expected_result
        ('10%', 100, 1, 10),
        ('10%', 100, 0, 10),
        (100, 100, 1, 100),
        (100, 100, 0, 100),
        (100, 110, 0, 100),
        (150, 110, 0, 110),
        (1, 110, 0, 1),
        (0, 110, 0, 0),
        (0, 110, 1, 1),
        (101, 100, 0, 100),
    )
    for test_value, num_items, min_value, expected_result in test_data:
        result = pct_to_int(test_value, num_items, min_value)
        assert result == expected_result

# Generated at 2022-06-13 16:10:33.153897
# Unit test for function pct_to_int
def test_pct_to_int():

    assert pct_to_int(1, 5) == 1
    assert pct_to_int('3%', 100) == 3
    assert pct_to_int('3%', 100, min_value=2) == 3
    assert pct_to_int('8%', 1000) == 80
    assert pct_to_int('8%', 1000, min_value=2) == 80
    assert pct_to_int('1%', 4) == 1
    assert pct_to_int('1%', 4, min_value=2) == 2
    assert pct_to_int('0%', 4) == 1
    assert pct_to_int('11%', 4) == 2
    assert pct_to_int('11%', 4, min_value=1) == 1
    assert pct_to

# Generated at 2022-06-13 16:10:43.535555
# Unit test for function pct_to_int
def test_pct_to_int():
    test_num_items = 10
    assert pct_to_int('10', test_num_items) == 1
    assert pct_to_int('10.1', test_num_items) == 1
    assert pct_to_int('10.9', test_num_items) == 1
    assert pct_to_int('10%', test_num_items) == 1
    assert pct_to_int('20%', test_num_items) == 2
    assert pct_to_int('20.9%', test_num_items) == 2
    assert pct_to_int('10%', test_num_items, min_value=2) == 2
    assert pct_to_int('20%', test_num_items, min_value=2) == 2
    assert pct_to_

# Generated at 2022-06-13 16:10:48.565410
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 4, 5, 1, 3]
    expected_list = [1, 2, 3, 4, 5]
    returned_list = deduplicate_list(original_list)
    assert returned_list == expected_list, \
        "Expected %s, but got %s" % (expected_list, returned_list)



# Generated at 2022-06-13 16:10:54.514207
# Unit test for function pct_to_int
def test_pct_to_int():
    assert 1 == pct_to_int("1%", 100)
    assert 1 == pct_to_int("0%", 100)
    assert 1 == pct_to_int("0.5%", 100, min_value=1)
    assert 4 == pct_to_int("4%", 100)
    assert 100 == pct_to_int("100%", 100)
    assert 100 == pct_to_int("100", 100)
    assert 100 == pct_to_int(100, 100)
    assert 101 == pct_to_int(101, 100)
    assert 99 == pct_to_int("101%", 100, min_value=1)
    assert 1 == pct_to_int("1.5%", 100, min_value=1)

# Generated at 2022-06-13 16:11:01.947813
# Unit test for function pct_to_int
def test_pct_to_int():
    # Expected results as integers
    assert pct_to_int('10%', 10) == 1
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('10%', 1000) == 100
    assert pct_to_int('10%', 10000) == 1000
    assert pct_to_int('10%', 100000) == 10000
    assert pct_to_int('10%', 1000000) == 100000
    assert pct_to_int('10%', 10000000) == 1000000

    # Expected results as integers
    assert pct_to_int(10, 10) == 1
    assert pct_to_int(10, 100) == 10
    assert pct_to_int(10, 1000) == 100

# Generated at 2022-06-13 16:11:02.501007
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('10%', num_items=10) == 1

# Generated at 2022-06-13 16:11:08.762155
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 1, 3, 4]
    # print(deduplicate_list())
    deduplicated_list = deduplicate_list(original_list)
    # print(deduplicated_list)

    assert deduplicated_list == [1, 2, 3, 4]

test_deduplicate_list()

# Generated at 2022-06-13 16:11:12.958964
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_class:
        def __init__(self):
            self.preserve = 1
            self.exclude = 2

    tc = test_class()
    result = object_to_dict(tc, exclude=['exclude'])
    assert result['preserve'] == tc.preserve

    assert 'exclude' not in result



# Generated at 2022-06-13 16:11:18.044035
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests deduplicate list function
    """
    test1 = deduplicate_list(["hello", "hello", "world"])
    assert len(test1) == 2
    assert test1[0] == "hello"
    assert test1[1] == "world"


# Generated at 2022-06-13 16:11:27.959991
# Unit test for function deduplicate_list
def test_deduplicate_list():
    import random
    import string

    # Generate a random ordered list of letters and numbers
    letters = string.ascii_lowercase + string.ascii_uppercase
    numbers = string.digits
    lst = [random.choice(letters + numbers) for i in xrange(1000)]

    # Determine the length of the unordered list and the deduplicated list
    length_lst = len(lst)
    length_deduplicate_lst = len(deduplicate_list(lst))

    # Fail if the length of the list is not greater than the length of the deduplicated list
    if not length_lst > length_deduplicate_lst:
        raise AssertionError

    # Success! The length of the list is greater than the length of the deduplicated list


# Generated at 2022-06-13 16:11:33.587381
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo(object):
        def __init__(self, test1, test2):
            self.test1 = test1
            self.test2 = test2
    foo = Foo('test1', 'test2')
    assert object_to_dict(foo) == dict(test1='test1', test2='test2')


# Generated at 2022-06-13 16:11:39.969503
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 1, 4, 1, 5, 2, 6, 3]) == [1, 2, 3, 4, 5, 6]

# Generated at 2022-06-13 16:11:42.642749
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'a', 'b', 'c', 'a', 'b', 'd']) == ['a', 'b', 'c', 'd']

# Generated at 2022-06-13 16:11:52.128685
# Unit test for function object_to_dict

# Generated at 2022-06-13 16:11:56.338222
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 1, 1, 1, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list(['1', '2', '3', '2', '1']) == ['1', '2', '3']
    assert deduplicate_list([]) == []
    assert deduplicate_list(()) == []
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1] * 10) == [1]

# Generated at 2022-06-13 16:12:00.039949
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests the deduplicate_list function
    """
    assert deduplicate_list(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'c', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'c', 'c', 'b']) == ['a', 'c', 'b']

    assert deduplicate_list([]) == []



# Generated at 2022-06-13 16:12:12.137822
# Unit test for function deduplicate_list
def test_deduplicate_list():
    print('Testing deduplicate_list ...')

    original_list = ['a', 'b', 'a', 'c', 'd', 'd', 'e']
    expected_list = ['a', 'b', 'c', 'd', 'e']

    actual_list = deduplicate_list(original_list)

    if actual_list != expected_list:
        print('FAILED: deduplicate_list() returned "%s" instead of "%s"' % (str(actual_list), str(expected_list)))
    else:
        print('PASSED: deduplicate_list() returned "%s"' % str(actual_list))

# Generated at 2022-06-13 16:12:20.791873
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Tests object_to_dict function
    """
    class Foo(object):
        def __init__(self):
            self.hai = "hai"
            self.test = "test"
    temp = Foo()
    result = object_to_dict(temp, exclude=["test"])
    assert "hai" in result
    assert "test" not in result
    assert result["hai"] == "hai"
    temp.hai = "not hai"
    assert result["hai"] == "hai"



# Generated at 2022-06-13 16:12:25.341016
# Unit test for function deduplicate_list
def test_deduplicate_list(): # noqa
    list1 = [1, 2, 3, 2]
    list2 = [1, 2, 3]
    assert deduplicate_list(list1) == [1, 2, 3]
    assert deduplicate_list(list2) == [1, 2, 3]
    assert list1 == [1, 2, 3, 2]
    assert list2 == [1, 2, 3]


# Generated at 2022-06-13 16:12:32.593676
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        test_value = "test_value"
        test_other_value = "test_other_value"

    obj = TestObject()
    obj_dict = object_to_dict(obj)
    assert isinstance(obj_dict, dict)
    assert "test_value" in obj_dict
    assert "test_other_value" in obj_dict

# Generated at 2022-06-13 16:12:40.419805
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_class(object):
        test1 = "test1"
        test2 = "test2"
        test3 = "test3"
    test1 = test_class()
    test_dict_1 = {'test1': 'test1', 'test2': 'test2', 'test3': 'test3'}
    assert test_dict_1 == object_to_dict(test1)

    # Does it exclude the keys we ask it to?
    test_dict_2 = {'test2': 'test2', 'test3': 'test3'}
    assert test_dict_2 == object_to_dict(test1, exclude=['test1'])

    # Does it work with lists as well?
    assert test_dict_2 == object_to_dict(test1, exclude=['test1'])

# Generated at 2022-06-13 16:12:42.360166
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,3,2,1]) == [1, 2, 3]

# Generated at 2022-06-13 16:12:47.508650
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'a', 'd', 'b', 'e', 'f']
    expected_list = ['a', 'b', 'd', 'e', 'f']
    assert deduplicate_list(original_list) == expected_list
    assert deduplicate_list(['a', 'b', 'a', 'd', 'b', 'e', 'f']) == expected_list

if __name__ == '__main__':
    test_deduplicate_list()

# Generated at 2022-06-13 16:12:56.630670
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Test the object_to_dict function for proper output
    """
    class TestObject(object):
        test_object = "Testing"
        test_object2 = "Testing 2"
    

    test_obj = TestObject()

    obj_dict = object_to_dict(test_obj)

    assert(isinstance(obj_dict, dict))
    assert("test_object" in obj_dict)
    assert("test_object2" in obj_dict)
    assert(obj_dict["test_object"] == "Testing")
    assert(obj_dict["test_object2"] == "Testing 2")

if __name__ == "__main__":
    test_object_to_dict()

# Generated at 2022-06-13 16:13:01.954122
# Unit test for function object_to_dict

# Generated at 2022-06-13 16:13:08.778049
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list((1, 1, 2, 3)) == [1, 2, 3]
    assert deduplicate_list([]) == []
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-13 16:13:19.662970
# Unit test for function object_to_dict
def test_object_to_dict():
    class ClassOne(object):
        def __init__(self):
            self.prop1 = 1
            self.prop2 = 2
            self.prop3 = 3
            self._prop4 = 4

    obj = ClassOne()
    assert object_to_dict(obj) == {'prop1': 1, 'prop2': 2, 'prop3': 3}
    assert object_to_dict(obj, exclude=['prop1', 'prop3']) == {'prop2': 2}
    assert object_to_dict(obj, exclude=None) == {'prop1': 1, 'prop2': 2, 'prop3': 3}


# Generated at 2022-06-13 16:13:24.397221
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'd', 'a', 'b']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(['b', 'b', 'a', 'c', 'd', 'a', 'b']) == ['b', 'a', 'c', 'd']

# Generated at 2022-06-13 16:13:32.098571
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        def __init__(self):
            self.key1 = 'val1'
            self.key2 = 'val2'

        def dont_print_me(self):
            return 'secret'

    obj = TestClass()

    assert object_to_dict(obj) == {'key1': 'val1', 'key2': 'val2'}
    assert object_to_dict(obj) != {'key1': 'val1', 'key2': 'val2', 'dont_print_me': 'secret'}
    assert object_to_dict(obj, exclude=['key1']) == {'key2': 'val2'}
    assert object_to_dict(obj, exclude=['key1', 'key2']) == {}

# Generated at 2022-06-13 16:13:36.258346
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.test = 'test'
            self.test2 = 'test2'
    test_object = TestClass()
    x = object_to_dict(test_object)
    assert 'test' in x
    assert 'test2' in x

# Generated at 2022-06-13 16:13:40.218326
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'b', 'd', 'a']) == ['a', 'b', 'd']

# Generated at 2022-06-13 16:13:46.327160
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test:
        a = 1
        b = 2
        c = 3

    test = Test()
    dictionary = object_to_dict(test)
    assert dictionary['a'] == 1
    assert dictionary['b'] == 2
    assert dictionary['c'] == 3
    dictionary = object_to_dict(test, exclude=['a'])
    assert 'a' not in dictionary
    assert dictionary['b'] == 2
    assert dictionary['c'] == 3

# Generated at 2022-06-13 16:13:56.883781
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Test empty list, should return empty list
    assert deduplicate_list([]) == []

    # Test unsorted list, should return uncorrupted sorted list
    assert deduplicate_list([2, 3, 1]) == [2, 3, 1]

    # Test sorted/unsorted list, should return sorted list
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 3, 2]) == [1, 3, 2]
    assert deduplicate_list([2, 1, 3]) == [2, 1, 3]
    assert deduplicate_list([2, 3, 1]) == [2, 3, 1]
    assert deduplicate_list([3, 1, 2]) == [3, 1, 2]

# Generated at 2022-06-13 16:14:04.111498
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 1, 2]
    expected_list = [1, 2, 3, 4, 5, 6]
    ret_list = deduplicate_list(test_list)
    assert ret_list == expected_list



# Generated at 2022-06-13 16:14:09.062087
# Unit test for function deduplicate_list
def test_deduplicate_list():
    class TestModule:
        pass

    test_module = TestModule()
    test_module.fail_json = lambda **kwargs: None

    original_list = ['1', '2', '3', '1', '2', '3']
    result = deduplicate_list(original_list)
    assert result == ['1', '2', '3']

# Generated at 2022-06-13 16:14:15.598131
# Unit test for function object_to_dict
def test_object_to_dict():
    # Create a quick class that has a couple properties
    class TestClass(object):
        def __init__(self):
            self.test_1 = 'foo'

    test_obj = TestClass()
    test_dict = {'test_1': 'foo'}
    assert object_to_dict(test_obj, exclude=['test_1']) == {}
    assert object_to_dict(test_obj, exclude=['test_2']) == test_dict
    assert object_to_dict(test_obj) == test_dict



# Generated at 2022-06-13 16:14:25.214088
# Unit test for function deduplicate_list
def test_deduplicate_list():

    test_list = [1,2,3,4,5,6,7,8,9,10,1,2,3,3]
    assert deduplicate_list(test_list) == [1,2,3,4,5,6,7,8,9,10]


# Generated at 2022-06-13 16:14:33.821154
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        foo = 'bar'
        var1 = 'test'
        exclude_me = 'dont_show'
        exclude_me_too = 'dont_show'
    test_class = TestClass()
    result = object_to_dict(test_class, exclude=['exclude_me','exclude_me_too'])
    assert result.has_key('foo') is True
    assert result.get('foo') == 'bar'
    assert result.has_key('exclude_me') is False
    assert result.has_key('exclude_me_too') is False

# Generated at 2022-06-13 16:14:39.344471
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        A = 'a'
        B = 'b'
        C = 'c'
        _D = 'd'

    obj = TestClass()
    ret_dict = object_to_dict(obj)
    assert len(ret_dict) == 3
    assert not '_D' in ret_dict

# Generated at 2022-06-13 16:14:42.332377
# Unit test for function deduplicate_list
def test_deduplicate_list():
    a = ['x', 'y', 'x', 'z']
    b = ['x', 'y', 'z']
    assert deduplicate_list(a) == b


# Generated at 2022-06-13 16:14:46.430084
# Unit test for function object_to_dict
def test_object_to_dict():
    class Object:
        def __init__(self):
            self.property1 = "value1"
            self.property2 = "value2"
            self._private_property = "value3"

    obj = Object()
    result = object_to_dict(obj)
    assert result.get('property1') == 'value1'
    assert result.get('property2') == 'value2'
    assert result.get('_private_property') is None

# Generated at 2022-06-13 16:14:50.230188
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 1, 4, 'd', 'd', 'c']
    assert deduplicate_list(test_list) == [1, 2, 4, 'd', 'c']



# Generated at 2022-06-13 16:14:59.870612
# Unit test for function object_to_dict
def test_object_to_dict():
    class Object(object):

        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    obj = Object('a', 'b', 'c')
    obj_exclude = Object('a', 'b', 'c')
    obj_dict = object_to_dict(obj)
    obj_exclude_dict = object_to_dict(obj_exclude, exclude=['a'])
    assert obj_dict['a'] == 'a'
    assert obj_dict['b'] == 'b'
    assert obj_dict['c'] == 'c'
    assert obj_exclude_dict['b'] == 'b'
    assert obj_exclude_dict['c'] == 'c'

# Generated at 2022-06-13 16:15:06.539715
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 2, 1, 3, 3]) == [1, 2, 3]


# Generated at 2022-06-13 16:15:13.374071
# Unit test for function object_to_dict
def test_object_to_dict():
    test_obj = type('test_obj', (object,), {'test': 'a', 'test2': 'b', '_test3': 'c'})
    assert {'test': 'a', 'test2': 'b'} == object_to_dict(test_obj)
    assert {'test': 'a', 'test2': 'b'} == object_to_dict(test_obj, exclude=['_test3'])
    assert {'test': 'a', 'test2': 'b', '_test3': 'c'} == object_to_dict(test_obj, exclude=None)



# Generated at 2022-06-13 16:15:21.887567
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 4, 5, 6, 1, 2, 3, 7, 8, 9, 1, 8, 8, 8]
    deduplicated_list = deduplicate_list(test_list)
    assert deduplicated_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 16:15:40.816556
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 4, 1, 2, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list(['1', '2', '3', '4', '1', '2', '5']) == ['1', '2', '3', '4', '5']
    assert deduplicate_list([]) == []
    assert deduplicate_list(None) == []

# Generated at 2022-06-13 16:15:47.562334
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests the deduplicate_list function with a list of numbers and a list of strings
    """
    numlist = [1, 2, 1, 3, 2, 4, 5]
    strlist = ["hello", "hello", "world"]
    assert deduplicate_list(numlist) == [1, 2, 3, 4, 5]
    assert deduplicate_list(strlist) == ["hello", "world"]



# Generated at 2022-06-13 16:15:52.999632
# Unit test for function object_to_dict
def test_object_to_dict():
    class Fruit(object):
        def __init__(self):
            self.color = 'red'
            self.name = 'Apple'

    apple_obj = Fruit()

    assert {'color': 'red', 'name': 'Apple'} == object_to_dict(apple_obj)



# Generated at 2022-06-13 16:15:56.305896
# Unit test for function deduplicate_list
def test_deduplicate_list():
    my_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 4, 2, 5, 1]
    assert deduplicate_list(my_list) == [1, 2, 3, 4, 5]


# Generated at 2022-06-13 16:15:59.291925
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['a','b','a','b','c','b','d']
    filtered_list = deduplicate_list(test_list)
    assert(filtered_list == ['a', 'b', 'c', 'd'])

# Generated at 2022-06-13 16:16:01.515887
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1,2,2,2,4,4,7]
    assert deduplicate_list(test_list) == [1,2,4,7]



# Generated at 2022-06-13 16:16:03.765184
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['value1', 'value1', 'value1', 'value2', 'value2', 'value3']
    assert deduplicate_list(test_list) == ['value1', 'value2', 'value3']



# Generated at 2022-06-13 16:16:12.245107
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests for the deduplicate_list function
    """
    assert deduplicate_list(['a', 'b', 'a', 'd', 'c', 'b', 'a']) == ['a', 'b', 'd', 'c']
    assert deduplicate_list([]) == []
    assert deduplicate_list(['a', 'a', 'a', 'a', 'a', 'a']) == ['a']
    assert deduplicate_list(['b', 'a', 'a', 'c']) == ['b', 'a', 'c']


# Generated at 2022-06-13 16:16:20.694912
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1, 2, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
    assert deduplicate_list([4, 3, 3, 3, 2, 2, 1]) == [4, 3, 2, 1]
    assert deduplicate_list(["foo", "foo", "bar", "bar", "baz", "foo", "baz", "baz"]) == ["foo", "bar", "baz"]

# Generated at 2022-06-13 16:16:24.893649
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 2, 1, 3, 3, 2, 1]

    results = deduplicate_list(original_list)

    # Confirm list only has unique values
    assert len(results) == len(set(results))

    # Confirm that all the original values are in the new list
    assert sorted(original_list) == sorted(results)



# Generated at 2022-06-13 16:16:55.414891
# Unit test for function deduplicate_list
def test_deduplicate_list():
    result = deduplicate_list([1, 2, 4, 2, 5, 4, 7, 8])
    assert result == [1, 2, 4, 5, 7, 8]


# Generated at 2022-06-13 16:16:57.844193
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a','a','b','c','c','b','a','d']) == ['a','b','c','d']



# Generated at 2022-06-13 16:17:02.751055
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.attr1 = 1
            self.attr2 = 2
            self.attr3 = 3

    testobj = TestClass()
    testobjdict = object_to_dict(testobj)

    assert testobjdict == {'attr1': 1, 'attr2': 2, 'attr3': 3}

# Generated at 2022-06-13 16:17:07.662359
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list
    """
    llist = ['a', 'b', 'c', 'd', 'a', 'c', 'b', 'c']
    assert deduplicate_list(llist) == ['a', 'b', 'c', 'd']



# Generated at 2022-06-13 16:17:14.744679
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass():
        var_1 = 'ABC'
        var_2 = 'DEF'
        var_3 = 'GHI'

    assert object_to_dict(TestClass()) == {'var_1': 'ABC', 'var_2': 'DEF', 'var_3': 'GHI'}
    assert object_to_dict(TestClass(), ['var_1', 'var_3']) == {'var_2': 'DEF'}

# Generated at 2022-06-13 16:17:26.114434
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.val1 = 'abc'
            self.val2 = 'def'
            self.val3 = 'blah'
            self._val4 = 'i wont show'
            self.__val5 = 'me either'

    test_instance = TestClass()
    assert object_to_dict(test_instance) == {
        'val1': 'abc',
        'val2': 'def',
        'val3': 'blah',
    }

    # Excluding from a dictionary
    assert object_to_dict(test_instance, exclude=['val2', 'val3']) == {
        'val1': 'abc',
    }

    # Excluding from a string

# Generated at 2022-06-13 16:17:31.625455
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Returns true if the given list has been deduplicated
    """
    test_list = ['a', 'b', 'a', 'c', 'a']
    deduplicated_test_list = deduplicate_list(test_list)
    assert ['a', 'b', 'c'] == deduplicated_test_list


# Generated at 2022-06-13 16:17:34.695520
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 1, 3, 2, 5, 3, 6, 8, 5, 7]
    assert deduplicate_list(test_list) == [1, 2, 3, 5, 6, 8, 7]



# Generated at 2022-06-13 16:17:41.095633
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.test = 'test'
            self.test1 = 'test1'
            self._test = '_test'
    obj = TestClass()
    assert object_to_dict(obj, ['_test']) == {'test': 'test', 'test1': 'test1'}

# Generated at 2022-06-13 16:17:43.990517
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4]) == [1,2,3,4]


# Generated at 2022-06-13 16:18:43.960709
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert (deduplicate_list([1, 2, 2, 3, 2, 5, 2, 1, 2, 5]) == [1, 2, 3, 5])


# Generated at 2022-06-13 16:18:49.749470
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj(object):
        def __init__(self):
            self.test1 = 'test1'
            self.test2 = 'test2'
        def test3(self):
            return 'test3'

    obj = TestObj()
    assert object_to_dict(obj, ['test2']) == {'test1': 'test1', 'test3': 'test3'}

# Generated at 2022-06-13 16:18:55.995090
# Unit test for function deduplicate_list
def test_deduplicate_list():
    import pytest
    test_list = ['a', 'b', 'c', 'd', 'b', 'a', 'b', 'e']
    compare_list = ['a', 'b', 'c', 'd', 'e']
    assert compare_list == deduplicate_list(test_list)


# Generated at 2022-06-13 16:18:59.376262
# Unit test for function deduplicate_list
def test_deduplicate_list():
    items = ['foo', 'bar', 'foo', 'baz']
    expected = ['foo', 'bar', 'baz']
    assert deduplicate_list(items) == expected


# Generated at 2022-06-13 16:19:07.918065
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert [1, 2, 3, 4] == deduplicate_list([1, 2, 3, 4])
    assert [1, 2, 3, 4, 5] == deduplicate_list([1, 2, 3, 4, 5])
    assert [1, 2, 3, 1, 2, 3] == deduplicate_list([1, 1, 2, 2, 3, 3])
    assert [1, 2, 3, 4] == deduplicate_list([1, 1, 2, 1, 3, 3, 4])

# Generated at 2022-06-13 16:19:10.118337
# Unit test for function object_to_dict
def test_object_to_dict():
    class A(object):
        def __init__(self):
            self.a = 10
            self.b = 20
    a1 = A()
    a2 = A()
    a2.b = 40
    l = [a1, a2]
    assert object_to_dict(l[0]) == {'a': 10, 'b': 20}

# Generated at 2022-06-13 16:19:14.001471
# Unit test for function deduplicate_list
def test_deduplicate_list():
    ddup_list = [1,1,2,2,3,3,4,4,5,5]
    ddup_list_expected = [1,2,3,4,5]
    assert deduplicate_list(ddup_list) == ddup_list_expected

# Generated at 2022-06-13 16:19:22.047303
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Unit tests for function object_to_dict
    """
    class TestObj:
        def __init__(self):
            self.one = 1
            self.two = '2'
            self.three = 3
            self.four = '4'
            self._five = 5
            self._six = '6'

        def test_function(self):
            pass

    test_obj = TestObj()

    assert object_to_dict(test_obj) == {'one': 1, 'three': 3, 'two': '2', 'four': '4'}
    assert object_to_dict(test_obj, exclude=['one']) == {'three': 3, 'two': '2', 'four': '4'}

# Generated at 2022-06-13 16:19:25.272096
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Test deduplicate_list function
    """
    assert deduplicate_list([1,1,2,3,3]) == [1,2,3]



# Generated at 2022-06-13 16:19:32.729037
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.test_one = 1
            self.test_two = 2
            self.test_three = 3
            self._protect = 'secret'
            self.to_exclude = True

        def get_stuff(self):
            return False
    expect = {
        'test_one': 1,
        'test_two': 2,
        'test_three': 3,
    }
    test_class = TestClass()
    assert expect == object_to_dict(test_class, exclude=['to_exclude', 'get_stuff'])

