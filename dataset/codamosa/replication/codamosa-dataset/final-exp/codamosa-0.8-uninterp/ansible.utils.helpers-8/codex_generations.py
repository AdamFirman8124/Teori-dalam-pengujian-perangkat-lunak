

# Generated at 2022-06-13 16:10:10.762615
# Unit test for function pct_to_int
def test_pct_to_int():
    test_data = [
        ('50%', 10, 1),
        ('50%', 10, 5),
        ('50%', 10, 0),
        ('50', 10, 1),
        (50, 10, 1)
    ]
    for data_item in test_data:
        assert pct_to_int(data_item[0], data_item[1], min_value=data_item[2]) == 5

# Generated at 2022-06-13 16:10:20.216108
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_data = [1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    expected_result = [1,3,1,2,1,3,4]

    result = deduplicate_list(test_data)
    assert result == expected_result

# Generated at 2022-06-13 16:10:28.550465
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('10%', 100, min_value=5) == 10
    assert pct_to_int('5%', 100, min_value=5) == 5
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int(50, 100) == 50
    assert pct_to_int('10%', 50) == 5
    assert pct_to_int('10%', 50, min_value=5) == 5
    assert pct_to_int('5%', 50, min_value=5) == 3


# Generated at 2022-06-13 16:10:36.428876
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(20, 120) == 24
    assert pct_to_int('20%', 120) == 24
    assert pct_to_int('20%', 120, min_value=0) == 20
    assert pct_to_int(20, 120, min_value=0) == 20
    assert pct_to_int('20%', 100, min_value=0) == 20
    assert pct_to_int(10, 100, min_value=0) == 10
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('10%', 100, min_value=5) == 10
    assert pct_to_int('10%', 100, min_value=15) == 15


# Generated at 2022-06-13 16:10:42.151824
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_class(object):
        test_attr = 'test'

    result = object_to_dict(test_class())
    assert result['test_attr'] == 'test'
    assert '__module__' in result

    result = object_to_dict(test_class(), ['test_attr'])
    assert 'test_attr' not in result
    assert '__module__' in result

# Generated at 2022-06-13 16:10:48.687686
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('0%', 25) == 0
    assert pct_to_int('5%', 100) == 5
    assert pct_to_int('100%', 200) == 200
    assert pct_to_int('50%', 5) == 3
    assert pct_to_int('50%', 10, 2) == 5
    assert pct_to_int(0, 1) == 0
    assert pct_to_int(1, 1) == 1
    assert pct_to_int(50, 100) == 50
    assert pct_to_int(49.99, 100) == 50

# Generated at 2022-06-13 16:10:51.412479
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(1, 8) == 1
    assert pct_to_int(12, 8) == 2
    assert pct_to_int('12%', 8) == 2
    assert pct_to_int('12%', 8, min_value=3) == 3



# Generated at 2022-06-13 16:10:57.046868
# Unit test for function pct_to_int
def test_pct_to_int():
    result1 = pct_to_int('90%', 10, min_value=1)
    result2 = pct_to_int('90%', 1, min_value=1)
    result3 = pct_to_int(90, 10, min_value=1)
    assert result1 == 9
    assert result2 == 1
    assert result3 == 90

# Generated at 2022-06-13 16:11:00.952075
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('2%', 1000) == 20
    assert pct_to_int('100.00%', 1000) == 1000
    assert pct_to_int(20, 1000) == 20
    assert pct_to_int('1%', 1000, min_value=2) == 2
    assert pct_to_int('10%', 1000, min_value=2) == 10

# Generated at 2022-06-13 16:11:05.368021
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(3, 100) == 3
    assert pct_to_int('3', 100) == 3
    assert pct_to_int('3%', 100) == 3
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('10%', 1000) == 100
    assert pct_to_int('10%', 10) == 1



# Generated at 2022-06-13 16:11:11.686848
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        attr1 = "foo"
        attr2 = "bar"

    test = Test()
    test_dict = object_to_dict(test)

    assert test_dict['attr2'] == "bar"
    assert test_dict['attr1'] == "foo"

# Generated at 2022-06-13 16:11:17.009304
# Unit test for function object_to_dict
def test_object_to_dict():
    class Object(object):
        name = 'test'
        age = 1
        def __init__(self):
            self._private = 'private'

    assert object_to_dict(Object()) == {'name': 'test', 'age': 1}
    assert object_to_dict(Object(), exclude=['age']) == {'name': 'test'}


# Generated at 2022-06-13 16:11:22.681714
# Unit test for function deduplicate_list
def test_deduplicate_list():
    example_list = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'a', 'e', 'e', 'a']
    deduplicated_list = deduplicate_list(example_list)
    assert deduplicated_list == ['a', 'b', 'c', 'd', 'e']
    assert example_list != deduplicated_list

# Generated at 2022-06-13 16:11:26.146225
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['B', 'A', 'D', 'C', 'B', 'A', 'C']
    assert deduplicate_list(original_list) == ['B', 'A', 'D', 'C']



# Generated at 2022-06-13 16:11:32.804073
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert [] == deduplicate_list([])
    assert [1] == deduplicate_list([1, 1])
    assert [1, 2] == deduplicate_list([1, 2, 2, 1, 1, 2, 2])
    assert [1, 2, 3, 4] == deduplicate_list([1, 2, 3, 4, 4, 3, 2, 1])


# Generated at 2022-06-13 16:11:39.425541
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj:
        a_attr = "foo"
        b_attr = 5
        c_attr = ["foo", "bar"]

    obj = TestObj()
    data = object_to_dict(obj)
    assert data["a_attr"] == "foo"
    assert data["b_attr"] == 5
    assert data["c_attr"] == ["foo", "bar"]

test_object_to_dict()

# Generated at 2022-06-13 16:11:47.600471
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,3]) == [1,2,3]
    assert deduplicate_list([1,2,3,3,3,3]) == [1,2,3]
    assert deduplicate_list([1,2,3,3,3]) == [1,2,3]
    assert deduplicate_list([1,2,3,1,2,3,2,2,2,2,1]) == [1,2,3]

# Generated at 2022-06-13 16:11:59.193036
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    original_list2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]
    original_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert deduplicate_list(original_list1) == [1, 2, 3, 4, 5]
    assert deduplicate_list(original_list2) == [5, 4, 3, 2, 1]
    assert deduplicate_list(original_list3) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generated at 2022-06-13 16:12:04.764274
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Check basic functionality
    test_list = ['a', 'b', 'c', 'b', 'a']
    assert deduplicate_list(test_list) == ['a', 'b', 'c']
    # Check order is preserved, first occurrence first
    test_list = ['b', 'c', 'a', 'b', 'a']
    assert deduplicate_list(test_list) == ['b', 'c', 'a']



# Generated at 2022-06-13 16:12:13.805977
# Unit test for function object_to_dict
def test_object_to_dict():
    class Person(object):
        def __init__(self):
            self.name = "John Smith"
            self.age = 34
            self.car = "Honda Civic"
            self.__secret = "Secret attribute"

    person = Person()
    person_dict = object_to_dict(person)
    assert person_dict['name'] == "John Smith"
    assert person_dict['age'] == 34
    assert person_dict['car'] == "Honda Civic"
    try:
        secret = person_dict['__secret']
        assert False
    except KeyError:
        assert True
    person_dict_with_exclude = object_to_dict(person, exclude=['name'])

# Generated at 2022-06-13 16:12:19.481597
# Unit test for function object_to_dict
def test_object_to_dict():
    result = object_to_dict(obj=10)
    assert result == {}

# Generated at 2022-06-13 16:12:24.481750
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert(deduplicate_list(["a", "b", "c", "c"]) == ["a", "b", "c"])
    assert(deduplicate_list(["a", "a", "a"]) == ["a"])
    assert(deduplicate_list(["a", "a", "b", "c", "b"]) == ["a", "b", "c"])

# Generated at 2022-06-13 16:12:30.537428
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 3, 4, 4, 3, 5]
    deduplicated_list = [1, 2, 3, 4, 5]
    assert deduplicate_list(original_list) == deduplicated_list

# Generated at 2022-06-13 16:12:36.082483
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    test_object_to_dict validates that the output of object_to_dict is what we expect
    """
    obj = ObjectA()
    output = object_to_dict(obj, 'exclude_me')
    assert len(output) == 3
    for key in output:
        assert output[key] == getattr(obj, key)



# Generated at 2022-06-13 16:12:44.148008
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self._version = None
            self.name = None
            self.password = None
    test_object = TestObject()
    test_object._version = 1.0
    test_object.name = "Test Object"
    test_object.password = "password"
    test_object_dict = {
        '_version': 1.0,
        'name': "Test Object",
        'password': "password"
    }
    assert test_object_dict == object_to_dict(test_object)


# Generated at 2022-06-13 16:12:47.177526
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,2,3,3,3,4,5,5,5,5,5,5,5,5,5]) == [1, 2, 3, 4, 5]

# Generated at 2022-06-13 16:12:53.780650
# Unit test for function object_to_dict
def test_object_to_dict():
    class Example(object):
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2
            self.arg3 = 'arg3'
    obj = Example('arg1', 'arg2')
    expected_dict = {'arg1': 'arg1', 'arg2': 'arg2', 'arg3': 'arg3'}
    assert expected_dict == object_to_dict(obj)


# Generated at 2022-06-13 16:12:56.547378
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list1 = ['a', 'b', 'a', 'c', 'd', 'd']
    assert ['a', 'b', 'c', 'd'] == deduplicate_list(list1)

# Generated at 2022-06-13 16:13:03.787820
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Tests the function deduplicate_list

    # Test 1: Normal case when the list needs to be deduplicated
    original_list = [1, 1, 2, 4, 4, 5, 6, 7]
    expected_deduplicated_list = [1, 2, 4, 5, 6, 7]
    deduplicated_list = deduplicate_list(original_list)
    assert(deduplicated_list == expected_deduplicated_list)


    # Test 2: List with a single element
    original_list = [1]
    expected_deduplicated_list = [1]
    deduplicated_list = deduplicate_list(original_list)
    assert(deduplicated_list == expected_deduplicated_list)


    # Test 3: List

# Generated at 2022-06-13 16:13:10.309557
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestModule(object):
        def __init__(self, x=None, y=None):
            self.x = x
            self.y = y

    test_obj = TestModule(1, 2)
    test_dict = object_to_dict(test_obj)
    assert(test_dict['x'] == 1)
    assert(test_dict['y'] == 2)



# Generated at 2022-06-13 16:13:27.353373
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list.
    """
    assert deduplicate_list([]) == []
    assert deduplicate_list(['1','2','3','4','5','6','7','8','9']) == ['1','2','3','4','5','6','7','8','9']
    assert deduplicate_list(['1','1','1','1','1','1','1','1','1']) == ['1']
    assert deduplicate_list(['1','2','1','2','1','2','1','2','1']) == ['1','2']
    assert deduplicate_list(['1','2','3','4','5','6','7','8','1']) == ['1','2','3','4','5','6','7','8']

# Generated at 2022-06-13 16:13:32.485294
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list1 = ['a', 'b', 'c', 'a']
    list2 = ['b', 'c', 'a', 'a']
    expected_output = ['a', 'b', 'c']
    assert deduplicate_list(list1) == expected_output
    assert deduplicate_list(list2) == expected_output



# Generated at 2022-06-13 16:13:36.296379
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1, 2, 3, 2, 1, 4, 5, 1, 2, 4, 5, 6, 7, 8, 1, 2]) == [1, 2, 3, 4, 5, 6, 7, 8]

# Generated at 2022-06-13 16:13:46.496961
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ["a", "b", "c", "a", "c", "d", "e", "a", "b", "c", "e", "f", "g", "h", "g", "h"]
    # First item in list with a duplicate is "a", second item with a duplicate is "c", and so on
    expected_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    new_list = deduplicate_list(original_list)
    assert len(new_list) == len(expected_list)
    assert new_list == expected_list


# Generated at 2022-06-13 16:13:53.369576
# Unit test for function deduplicate_list
def test_deduplicate_list():
    #Test for empty list
    assert deduplicate_list([]) == []

    #Test for deduplication
    assert deduplicate_list([1, 1, 2, 3, 1, 4]) == [1, 2, 3, 4]

    #Test for order
    assert deduplicate_list([1, 5, 3, 2, 1, 5, 4, 1]) == [1, 5, 3, 2, 4]

# Generated at 2022-06-13 16:13:59.474668
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([3, 2, 2, 1]) == [3, 2, 1]
    assert deduplicate_list([1, 1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-13 16:14:05.903375
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1, 2]) == [1, 2]
    assert deduplicate_list(['hello', 'world', 'hello', 'world']) == ['hello', 'world']
    assert deduplicate_list([1, 'hello', 'world', 2, 1, 2]) == [1, 'hello', 'world', 2]



# Generated at 2022-06-13 16:14:13.918949
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1]) == [1, 2, 1]
    assert deduplicate_list([1, 2, 1, 3, 3, 3]) == [1, 2, 1, 3, 3, 3]
    assert deduplicate_list([1, 2, 1, 3, 3, 3, 2, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [1, 2, 1, 3, 3, 3, 2, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]



# Generated at 2022-06-13 16:14:21.564957
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert [1,2,3] == deduplicate_list([1,2,3])

# Generated at 2022-06-13 16:14:22.959484
# Unit test for function deduplicate_list
def test_deduplicate_list():
        assert deduplicate_list([1, 2, 3, 1, 1, 5]) == [1, 2, 3, 5]

# Generated at 2022-06-13 16:14:45.460003
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 2, 3, 2, 1, 2, 3, 2, 3, 2, 1, 2, 3, 2, 3, 2, 1, 2, 3, 2, 3, 2]
    expected_list = [1, 2, 3]
    actual_list = deduplicate_list(original_list)
    assert expected_list == actual_list



# Generated at 2022-06-13 16:14:51.123048
# Unit test for function deduplicate_list
def test_deduplicate_list():
    import copy

    test_list = [1, 2, 3, 4, 1, 2, 5, 5, 4]
    correct_list = [1, 2, 3, 4, 5]

    function_list = copy.copy(test_list)
    function_list = deduplicate_list(function_list)

    assert function_list == correct_list

# Generated at 2022-06-13 16:14:56.103486
# Unit test for function object_to_dict
def test_object_to_dict():
    from collections import namedtuple
    test = namedtuple('test', ['attr1', 'attr2'])
    obj1 = test('value1', 'value2')
    obj2 = test('value1', 'value2')
    assert object_to_dict(obj1) == object_to_dict(obj2)



# Generated at 2022-06-13 16:15:00.630667
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for deduplicate_list method.
    """
    assert deduplicate_list([1, 1, 2, 3, 2]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 2, 1, 2]) == [1, 2]
    assert deduplicate_list([1, 2, 3, 2, 1]) == [1, 2, 3]

# Generated at 2022-06-13 16:15:08.335893
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass():
        def __init__(self):
            self.a = "foo"
            self.b = "bar"
    x = TestClass()
    d = object_to_dict(x)
    assert d['a'] == 'foo'
    assert d['b'] == 'bar'
    assert '_' not in d.keys()
    x = TestClass()
    d = object_to_dict(x, exclude=['a'])
    assert d['b'] == 'bar'
    assert '_' not in d.keys()
    assert 'a' not in d.keys()


# Generated at 2022-06-13 16:15:16.444069
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 1, 2, 3, 1, 4]
    assert deduplicate_list(original_list) == [1, 2, 3, 4]
    original_list = ['a', 'b', 'a', 'b', 'c', 'a', 'd']
    assert deduplicate_list(original_list) == ['a', 'b', 'c', 'd']
    original_list = ['b', 'a', 'a', 'b', 'c', 'a', 'd']
    assert deduplicate_list(original_list) == ['b', 'a', 'c', 'd']
    original_list = ['a', 'a', 'b', 'b', 'c', 'a', 'd']

# Generated at 2022-06-13 16:15:24.930978
# Unit test for function object_to_dict
def test_object_to_dict():
    obj = type('obj', (object,), {'key1': 1, 'key2': 2})()
    assert object_to_dict(obj) == {'key1': 1, 'key2': 2}
    assert object_to_dict(obj, exclude=['key1', 'key2']) == {}
    assert object_to_dict(obj, exclude=['key2']) == {'key1': 1}
    assert object_to_dict(obj, exclude=['key1', 'badkey']) == {'key2': 2}

# Generated at 2022-06-13 16:15:31.516660
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ["a", "b", "b", "c", "d", "a", "c"]
    deduped_list = deduplicate_list(original_list)
    actual = ["a", "b", "c", "d"]
    assert deduped_list == actual, "Incorrect deduplicate_list results"



# Generated at 2022-06-13 16:15:35.778711
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [3, 1, 2, 1, 2, 3, 2, 3, 2, 3, 2, 1]
    expected_list = [3, 1, 2]

    result = deduplicate_list(original_list)
    assert result == expected_list, 'Expecting {}, but got {}'.format(expected_list, result)



# Generated at 2022-06-13 16:15:42.657302
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        def __init__(self):
            self.test_value1 = "test_value1"
            self.test_value2 = True

        def test_method(self):
            return

    test_obj = TestClass()
    assert 'test_value1' in object_to_dict(test_obj)
    assert 'test_value2' in object_to_dict(test_obj)
    assert 'test_method' not in object_to_dict(test_obj)
    assert 'test_method' not in object_to_dict(test_obj, exclude=['test_value1'])
    assert 'test_method' in object_to_dict(test_obj, exclude=['test_value1', 'test_value2'])
    assert 'test_value1' not in object_to_dict

# Generated at 2022-06-13 16:16:24.813628
# Unit test for function deduplicate_list
def test_deduplicate_list():
    my_list = ['test', 'test', 'test1']
    assert(deduplicate_list(my_list) == ['test', 'test1'])
    my_list = ['test', 'test1']
    assert(deduplicate_list(my_list) == ['test', 'test1'])


# Generated at 2022-06-13 16:16:29.880123
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'a', 'd']) == ['a', 'b', 'd']
    assert deduplicate_list([]) == []
    assert deduplicate_list(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'a', 'b', 'a']) == ['a', 'b']

# Generated at 2022-06-13 16:16:31.615738
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 2, 4, 5, 6, 1]) == [1, 2, 3, 4, 5, 6]


# Generated at 2022-06-13 16:16:34.971036
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 5, 2, 6, 7, 5, 6]
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == [1, 2, 5, 6, 7]



# Generated at 2022-06-13 16:16:40.516873
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from  collections import OrderedDict
    my_list = ['a','b','b','a']
    deduplicate_list(my_list) == OrderedDict.fromkeys(my_list).keys()
    my_list = ['a','b','b','a','c']
    deduplicate_list(my_list) == OrderedDict.fromkeys(my_list).keys()
    my_list = ['a','b','c']
    deduplicate_list(my_list) == OrderedDict.fromkeys(my_list).keys()


# Generated at 2022-06-13 16:16:49.159179
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'a', 'b', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'a', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list([]) == []
    assert deduplicate_list([0]) == [0]
    assert deduplicate_list([0, 0]) == [0]
    assert deduplicate_list([0, 0, 1, 1, 2]) == [0, 1, 2]
    assert deduplicate_list([0, 1, 2]) == [0, 1, 2]

# Generated at 2022-06-13 16:16:53.443484
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(["foo", "foo", "bar", "baz", "bar", "foo"]) == ["foo", "bar", "baz"]



# Generated at 2022-06-13 16:16:59.658133
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['1', '2', '3', '2', '3', '2', '2']
    deduplicated_list = deduplicate_list(original_list)
    assert len(deduplicated_list) == 3
    assert deduplicated_list[0] == '1'
    assert deduplicated_list[1] == '2'
    assert deduplicated_list[2] == '3'

# Generated at 2022-06-13 16:17:03.244268
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['one', 'two', 'three', 'three', 'four', 'four', 'five']
    assert deduplicate_list(test_list) == ['one', 'two', 'three', 'four', 'five']



# Generated at 2022-06-13 16:17:10.657290
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a','b','c','c','d','d','e','c','e','a','a','b','d']) == ['a','b','c','d','e']
    assert deduplicate_list([]) == []
    assert deduplicate_list([1,23,4,5,123,5,234,1,2,2,2,2]) == [1,23,4,5,123,234]
    assert deduplicate_list('A test string') == ['A',' ','t','e','s','r','i','n','g']



# Generated at 2022-06-13 16:18:33.339945
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.one = 1
            self.two = 'two'
            self.three = True
            self.four = 'four'
            self.five = 5

    test = TestClass()
    actual = object_to_dict(test, ['one'])
    assert actual == {'four': 'four', 'three': True, 'two': 'two', 'five': 5}


# Generated at 2022-06-13 16:18:37.939698
# Unit test for function deduplicate_list
def test_deduplicate_list():
    the_list = ['a', 'b', 'c']
    assert deduplicate_list(the_list) == the_list
    the_list.insert(0, 'c')
    assert deduplicate_list(the_list) == ['a', 'b', 'c']



# Generated at 2022-06-13 16:18:39.700146
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'a', 'b']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:18:46.554038
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        one = 'first'
        two = 'second'

    instance = TestObject()

    assert object_to_dict(instance) == {'one': 'first', 'two': 'second'}
    assert object_to_dict(instance, exclude=['one']) == {'two': 'second'}


# Generated at 2022-06-13 16:18:51.596010
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.foo = 'foo'
            self.bar = 'bar'
            self.baz = 'baz'

    obj = TestObject()

    result = object_to_dict(obj)
    assert result['foo'] == 'foo'
    assert result['bar'] == 'bar'
    assert result['baz'] == 'baz'


# Generated at 2022-06-13 16:18:59.621262
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        name = 'test1'
        age = 26
        def __init__(self):
            self.name = 'test2'
            self.age = 88
            pass
    test_obj = TestClass()
    expected_dict = {
        'age': 88,
        'name': 'test2'
    }
    result_dict = object_to_dict(test_obj)
    assert result_dict == expected_dict

# Generated at 2022-06-13 16:19:05.069558
# Unit test for function deduplicate_list
def test_deduplicate_list():
    input_list = [1, 2, 1, 3, 5, 2, 3]
    expected_output = [1, 2, 3, 5]
    output = deduplicate_list(input_list)
    assert output == expected_output


# Generated at 2022-06-13 16:19:09.937871
# Unit test for function object_to_dict
def test_object_to_dict():
    import itertools
    import re
    import resource

    assert isinstance(object_to_dict(itertools), dict)
    assert isinstance(object_to_dict(re), dict)
    assert isinstance(object_to_dict(resource), dict)

# Generated at 2022-06-13 16:19:14.583111
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'b', 'a', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'c', 'a', 'c', 'b']) == ['a', 'b', 'c']
    assert deduplicate_list([]) == []



# Generated at 2022-06-13 16:19:17.161045
# Unit test for function deduplicate_list
def test_deduplicate_list():
    sample_list = ['a', 'c', 'a', 'b']
    expected = ['a', 'c', 'b']
    actual = deduplicate_list(sample_list)
    assert actual == expected

