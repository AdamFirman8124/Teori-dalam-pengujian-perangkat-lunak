

# Generated at 2022-06-13 16:10:13.719179
# Unit test for function pct_to_int
def test_pct_to_int():
    assert 11 == pct_to_int("10%", 110)
    assert 10 == pct_to_int("10%", 100)
    assert 5 == pct_to_int("5%", 100)
    assert 1 == pct_to_int("1%", 100)
    assert 0 == pct_to_int("0%", 100)
    assert 110 == pct_to_int("100%", 110)
    assert 10 == pct_to_int("100%", 10)
    assert 1 == pct_to_int("100%", 1)
    assert 10 == pct_to_int(5, 100)
    assert 10 == pct_to_int(10, 100)

# Generated at 2022-06-13 16:10:19.081256
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('20%', 100) == 20
    assert pct_to_int('1%', 100) == 1
    assert pct_to_int('1%', 100, min_value=10) == 10
    assert pct_to_int('1%', 100) == 1
    assert pct_to_int(2, 100) == 2

# Generated at 2022-06-13 16:10:29.616424
# Unit test for function pct_to_int
def test_pct_to_int():
    expected_result = 5
    assert pct_to_int('5%', 100) == expected_result

    expected_result = 1
    assert pct_to_int('0.5%', 100) == expected_result

    expected_result = 1
    assert pct_to_int('0.5%', 100, min_value=1) == expected_result

    expected_result = 2
    assert pct_to_int('0.5%', 100, min_value=2) == expected_result

    expected_result = 1
    assert pct_to_int('0%', 100, min_value=1) == expected_result

    expected_result = 10
    assert pct_to_int('10%', 100) == expected_result

    expected_result = 11

# Generated at 2022-06-13 16:10:37.276857
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int('50%', 50) == 25
    # Excessive as it should return at least 1
    assert pct_to_int('50%', 0) == 1
    assert pct_to_int('50', 100) == 50
    # Excessive as it should return at least 1
    assert pct_to_int('49.99%', 100) == 50
    assert pct_to_int('49.99%', 0) == 1
    assert pct_to_int(50, 100) == 50
    assert pct_to_int(50, 0) == 1
    assert pct_to_int(50.0, 100) == 50
    assert pct_to_int(50.0, 0) == 1

# Generated at 2022-06-13 16:10:42.599136
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int('50%', 10) == 5
    assert pct_to_int('50%', 10, min_value=3) == 3
    assert pct_to_int(25, 100) == 25
    assert pct_to_int(25, 10) == 2

# Generated at 2022-06-13 16:10:44.994259
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int(10, 100) == 10

# Generated at 2022-06-13 16:10:48.283232
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ["a", "b", "c", "d", "a", "b", "c", "d"]
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == ["a", "b", "c", "d"]

# Generated at 2022-06-13 16:10:56.017684
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(12, 100) == 12
    assert pct_to_int('12', 100) == 12
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int('12%', 100) == 12
    assert pct_to_int('12%', 100, min_value=10) == 12
    assert pct_to_int('0%', 100) == 1
    assert pct_to_int('0%', 100, min_value=10) == 10

# Generated at 2022-06-13 16:11:02.305114
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'a']) == ['a', 'b']
    assert deduplicate_list(['a', 'b', 'a', 'b']) == ['a', 'b']
    assert deduplicate_list(['a', 'a', 'a', 'a']) == ['a']
    assert deduplicate_list(['a', 'a', 'b', 'a']) == ['a', 'b']
    assert deduplicate_list(['a', 'b', 'c', 'd', 'e', 'b', 'c']) == ['a', 'b', 'c', 'd', 'e']
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:11:05.417283
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int("50%", 100) == 50
    assert pct_to_int("100%", 100) == 100
    assert pct_to_int("0%", 100) == 0


# Generated at 2022-06-13 16:11:10.947846
# Unit test for function deduplicate_list
def test_deduplicate_list():
    a = [1, 2, 3, 1, 4]
    b = [1, 2, 3, 4]
    c = deduplicate_list(a)
    assert c == b

# Generated at 2022-06-13 16:11:13.954735
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'a']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'c', 'b', 'c']) == ['a', 'c', 'b']

# Generated at 2022-06-13 16:11:17.203993
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'b', 'b', 'c', 'c']
    expected_list = ['a', 'b', 'c']
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == expected_list


# Generated at 2022-06-13 16:11:22.563727
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Test case for function deduplicate_list()
    """
    assert deduplicate_list([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 2, 1, 3, 1, 2]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2]) == [1, 2]
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:11:30.640063
# Unit test for function object_to_dict
def test_object_to_dict():
    class Obj(object):
        def __init__(self):
            self.b = 'b'
            self.c = 'c'
            self.a = 'a'
    obj = Obj()
    obj_dict = object_to_dict(obj)

    # Check order
    prev_letter = ''
    for letter in obj_dict:
        assert letter > prev_letter
        prev_letter = letter

    # Check key length
    assert len(obj_dict) == 3

    # Exclude keys
    obj_dict = object_to_dict(obj, exclude=['a','b'])
    assert len(obj_dict) == 1
    assert 'c' in obj_dict


# Generated at 2022-06-13 16:11:41.387797
# Unit test for function object_to_dict
def test_object_to_dict():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    host = Host("127.0.0.1", port=22, variable_manager=variable_manager)
    host.name = "127.0.0.1"
    host.port = 22
    host.vars["ansible_host"] = '127.0.0.1'
    host.vars["ansible_port"] = 22

    # test with exclude
    host_dict = object_to_dict(host, exclude=['name', 'port', 'vars'])
    assert host_dict == {}

    # test without exclude

# Generated at 2022-06-13 16:11:51.170746
# Unit test for function object_to_dict
def test_object_to_dict():
    class Obj:
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    obj = Obj('a', 'b', 'c', 'd')
    result = object_to_dict(obj)

    # Assert that the keys and values are correct
    assert 'a' in result
    assert result['a'] == 'a'
    assert 'b' in result
    assert result['b'] == 'b'
    assert 'c' in result
    assert result['c'] == 'c'
    assert 'd' in result
    assert result['d'] == 'd'

    # Assert that only 4 keys were returned
    assert len(result) == 4

    # Assert that the 'private' variables are not

# Generated at 2022-06-13 16:11:54.922470
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['1', '2', '2', '3', '1']
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == ['1', '2', '3']



# Generated at 2022-06-13 16:12:01.354351
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo():
        _foo = 'foo'
        _bar = 'bar'

    foo = Foo()
    assert object_to_dict(foo, ['_foo']) == {'_bar': 'bar'}
    assert object_to_dict(foo) == {'_foo': 'foo', '_bar': 'bar'}
    assert object_to_dict(foo, ['_baz']) == {'_foo': 'foo', '_bar': 'bar'}

# Generated at 2022-06-13 16:12:06.259842
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 2, 3, 2, 1, 2]
    expected_list = [1, 2, 3]

    deduplicated_list = deduplicate_list(test_list)
    assert deduplicated_list == expected_list



# Generated at 2022-06-13 16:12:21.572845
# Unit test for function object_to_dict
def test_object_to_dict():
    class obj:
        def __init__(self):
            self.prop_1 = "1"
            self.prop_2 = "2"
            self.prop_3 = "3"

    test_obj = obj()
    test_dict = object_to_dict(test_obj)
    assert test_dict['prop_1'] == "1"
    assert test_dict['prop_2'] == "2"
    assert test_dict['prop_3'] == "3"



# Generated at 2022-06-13 16:12:24.627518
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 2, 1, 2, 4, 2, 5, 2, 4]
    assert(deduplicate_list(test_list) == [1, 2, 3, 4, 5])



# Generated at 2022-06-13 16:12:27.980948
# Unit test for function deduplicate_list
def test_deduplicate_list():
    a_list = ['b', 'a', 'a', 'c', 'c', 'b']
    seen = set()
    a_list_dedup = [x for x in a_list if x not in seen and not seen.add(x)]
    assert a_list_dedup == ['b', 'a', 'c']
    assert seen == set(['b', 'a', 'c'])


# Generated at 2022-06-13 16:12:34.648706
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['1','2','2','3','4','4','4','5','6','7','3','3','3','8','8','9','9','9','9','9']
    assert deduplicate_list(original_list) == ['1','2','3','4','5','6','7','8','9']

# Generated at 2022-06-13 16:12:39.394717
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_a = [1,1,2,3,3,4,4,4,4,4,4,4,4,4,4,4,4]
    list_b = deduplicate_list(list_a)
    return list_b

# Generated at 2022-06-13 16:12:47.905619
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Test to convert an object into a dictionary.
    """
    class TestClass(object):
        """
        Test class for testing convertion from object to dictionary.
        """
        def __init__(self):
            self.test1 = 'test1'
            self.test2 = 'test2'
            self._test3 = 'test3'
            self.test4 = 'test4'
            self.test5 = 'test5'

    obj = TestClass()
    data = object_to_dict(obj, exclude=['test1'])
    assert data['test2'] == 'test2'
    assert data['test4'] == 'test4'
    assert data['test5'] == 'test5'
    assert 'test1' not in data
    assert '_test3' not in data

# Generated at 2022-06-13 16:12:57.872514
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests the function deduplicate_list
    """
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, MagicMock

    class test_class(object):
        def __init__(self):
            self.name = 'test_name'

        def __eq__(self, other):
            if self.name == other.name:
                return True
            else:
                return False

    test_obj1 = test_class()
    test_obj2 = test_class()
    test_obj3 = test_class()

    test_obj2.name = 'test_name2'
    test_obj3.name = 'test_name3'

    # Test the deduplicating list when biggest

# Generated at 2022-06-13 16:13:03.944133
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Test the object_to_dict function
    """
    class TestClass(object):
        """
        Dummy class to be used for testing
        """
        def __init__(self):
            """
            Dummy init method
            """
            self.test_member = "Test"
            self._private_member = "Private"
            self.test_member2 = "Test2"

    temp_obj = TestClass()
    assert object_to_dict(temp_obj, exclude=['_private_member']) == {'test_member': 'Test', 'test_member2': 'Test2'}

# Generated at 2022-06-13 16:13:07.919351
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1,2,2,4,4,4]
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == [1,2,4]

# Generated at 2022-06-13 16:13:14.105705
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Test deduplicate_list with a few example cases.
    """
    example_list = [1, 2, 2, 1, 3, 3, 4, 5, 5]
    expected_result = [1, 2, 3, 4, 5]

    result = deduplicate_list(example_list)
    if result != expected_result:
        raise ValueError("result {} does not equal expected result {}".format(
            result, expected_result))

# Generated at 2022-06-13 16:13:33.031044
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 2, 4]
    assert deduplicate_list(test_list) == [1, 2, 3, 4]

# Generated at 2022-06-13 16:13:45.636265
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Test object_to_dict using a class with dummy properties.
    """
    class DummyClass(object):
        """
        Dummy class for testing object_to_dict.
        """
        def __init__(self):
            """
            Initialize the dummy class.
            """
            self.name = 'unit_test'
            self.type = 'test'
            self.description = 'Test class for object_to_dict function.'

        def _private_method(self):
            """
            Private method for testing object_to_dict.
            """
            pass

        def public_method(self):
            """
            Public method for testing object_to_dict.
            """
            pass

    def test_value():
        """
        Test function to make sure value is correct.
        """
        dclass = D

# Generated at 2022-06-13 16:13:55.711028
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from nose.tools import assert_equal
    assert_equal(deduplicate_list([1,1,1,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]), [1,3,4])
    assert_equal(deduplicate_list([1,3,4]), [1,3,4])
    assert_equal(deduplicate_list(['1',1,'1']),['1',1])
    assert_equal(deduplicate_list(['1','1','1','3','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4']), ['1','3','4'])

# Generated at 2022-06-13 16:13:58.384184
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'c', 'a', 'a', 'd', 'b']
    duplicates_removed = deduplicate_list(original_list)
    assert duplicates_removed == ['a', 'b', 'c', 'd']

# Generated at 2022-06-13 16:14:04.492995
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [2, 3, 2, 4, 5, 1, 2, 1, 2, 4, 2, 1]
    expected_list = [2, 3, 4, 5, 1]

    actual_list = deduplicate_list(original_list)

    assert expected_list == actual_list

# Generated at 2022-06-13 16:14:07.309905
# Unit test for function deduplicate_list
def test_deduplicate_list():
  assert deduplicate_list([1,1,2,2,2,2,3,4,4,4]) == [1,2,3,4]


# Generated at 2022-06-13 16:14:11.040545
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ["foo", "bar", "bar", "bar", "foo", "foo", "foo", "baz", "baz", "bar"]
    expected = ["foo", "bar", "baz"]
    assert deduplicate_list(original_list) == expected

# Generated at 2022-06-13 16:14:20.434245
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests the deduplicate_list function
    """

# Generated at 2022-06-13 16:14:28.634938
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyObj():
        """ This is a test object with a bunch of properties.
        """
        def __init__(self):
            self.name = "David"
            self.age = 30
    my_obj = MyObj()
    obj_dict = object_to_dict(my_obj)
    assert obj_dict == {
        'name': "David",
        'age': 30
    }
    # Test excluding properties from the object
    obj_dict = object_to_dict(my_obj, exclude=['age'])
    assert obj_dict == {
        'name': "David"
    }

# Generated at 2022-06-13 16:14:36.498962
# Unit test for function object_to_dict

# Generated at 2022-06-13 16:15:11.573936
# Unit test for function object_to_dict
def test_object_to_dict():
    class testing(object):
        def __init__(self):
            self.a = "a"
            self.b = "b"
            self.c = "c"

    test = testing()
    assert object_to_dict(test) == {'a': 'a', 'b': 'b', 'c': 'c'}
    assert object_to_dict(test, exclude=['a']) == {'b': 'b', 'c': 'c'}

# Generated at 2022-06-13 16:15:13.976864
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 3, 2, 1, 2]
    new_list = deduplicate_list(original_list)
    assert new_list == [1, 2, 3]

# Generated at 2022-06-13 16:15:20.752038
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj(object):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.__dict__ == other.__dict__
            else:
                return False

    test_obj = TestObj("a", "b", "c")
    test_dict = {'a': 'a', 'b': 'b', 'c': 'c'}
    assert test_dict == object_to_dict(test_obj)
    test_obj = TestObj("a", "b", "c")
    test_dict = {'b': 'b', 'c': 'c'}
    assert test_dict == object_to_dict

# Generated at 2022-06-13 16:15:26.723743
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo(object):
        def __init__(self, a, b):
            self.a = a
            self._b = b

    foo = Foo(1, 2)
    assert object_to_dict(foo) == {'a': 1, '_b': 2}
    assert object_to_dict(foo, ['a']) == {'_b': 2}
    assert object_to_dict(foo, ['_b']) == {'a': 1}


# Generated at 2022-06-13 16:15:32.335890
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyObject(object):
        def __init__(self, key1, key2):
            self.key1 = key1
            self.key2 = key2
    data = MyObject('key1', 'key2')
    my_dict = object_to_dict(data)
    assert('key1' in my_dict.keys())

# Generated at 2022-06-13 16:15:34.362025
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:15:37.885550
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # List with duplicate items
    duplicate_list = [1, 2, 3, 6, 1, 2, 5, 4, 6]

    # List without duplicate items
    non_duplicate_list = [1, 2, 3, 6, 5, 4]

    assert deduplicate_list(duplicate_list) == non_duplicate_list, "Deduplication of list should be successful"


# Generated at 2022-06-13 16:15:44.595608
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.moo = 'cow'

    test_object = Test()
    test_object.john = 'doe'
    test_object.information = 'here'

    data = {'information': 'here', 'john': 'doe', 'moo': 'cow'}

    assert object_to_dict(test_object) == data

# Generated at 2022-06-13 16:15:51.656559
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_dup_last = [1, 2, 2, 3]
    list_dup_first = [2, 2, 3, 1]
    list_dup_middle = [2, 3, 2, 1]
    list_all_dup = [1, 1, 1, 1]
    list_not_dup = [1, 2, 3, 4]
    test_list = [list_dup_last, list_dup_first, list_dup_middle, list_all_dup, list_not_dup]
    for i in test_list:
        assert deduplicate_list(i) == [1, 2, 3, 4]


# Generated at 2022-06-13 16:16:00.494209
# Unit test for function object_to_dict
def test_object_to_dict():
    from ansible.module_utils.network.common.utils import object_to_dict

    class DummyObj(object):
        def __init__(self):
            self.property1 = 'property1'
            self.property2 = 'property2'

    obj = DummyObj()
    obj_dict = object_to_dict(obj)
    assert obj_dict == dict(property1='property1', property2='property2')

    obj_dict = object_to_dict(obj, exclude=['property1'])
    assert obj_dict == dict(property2='property2')



# Generated at 2022-06-13 16:17:01.042183
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self._private = 'PRIVATE'
            self.first = 1
            self.second = 2
            self.third = 3
    test_object = TestObject()
    assert set(object_to_dict(test_object, exclude=['_private']).keys()) == set(['first', 'second', 'third'])

# Generated at 2022-06-13 16:17:10.098583
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests that deduplicate_list removes duplicate entries and returns items in order of first seen.
    """

    assert ['foo', 'bar', 'baz'] == deduplicate_list(['foo', 'bar', 'baz'])
    assert ['foo', 'bar', 'baz'] == deduplicate_list(['foo', 'baz', 'baz', 'bar', 'foo'])
    assert ['a', 'b', 'c'] == deduplicate_list(['a', 'b', 'c', 'c', 'b', 'a'])
    assert ['a', 'b'] == deduplicate_list(['a', 'b', 'a', 'b', 'b', 'a'])

# Generated at 2022-06-13 16:17:12.533779
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo:
        bar = '1'
        baz = '2'

    assert object_to_dict(Foo) == {'bar': '1', 'baz': '2'}

# Generated at 2022-06-13 16:17:18.884298
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['foo', 'bar', 'baz', 'bar']) == ['foo', 'bar', 'baz']
    assert deduplicate_list(['foo', 'bar', 'baz', 'baz']) == ['foo', 'bar', 'baz']
    assert deduplicate_list(['foo', 'bar', 'bar']) == ['foo', 'bar']

# Generated at 2022-06-13 16:17:23.260324
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self, x):
            self.x = x
            self.y = 'ok'
            self.z = ['a', 'b']
        def __iter__(self):
            return iter(self.z)
    t = Test(1)
    result = object_to_dict(t)
    assert result == {'x': 1, 'y': 'ok', 'z': ['a', 'b']}

    result = object_to_dict(t, ['x'])
    assert result == {'y': 'ok', 'z': ['a', 'b']}


# Generated at 2022-06-13 16:17:31.878625
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test1 = [1, 2, 3, 4, 4, 3, 6, 5, 6, 7, 8, 5, 8, 9]
    result1 = deduplicate_list(test1)
    assert result1 == [1, 2, 3, 4, 6, 5, 7, 8, 9]

    test2 = ['a', 'b', 'c', 'a', 'b', 'd', 'b', 'e']
    result2 = deduplicate_list(test2)
    assert result2 == ['a', 'b', 'c', 'd', 'e']

    test3 = ['a', 'b', 'c', 'c', 'b', 'd', 'b', 'e']
    result3 = deduplicate_list(test3)

# Generated at 2022-06-13 16:17:34.607456
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'c', 'd', 'd', 'd', 'e']) == ['a', 'b', 'c', 'd', 'e']

# Generated at 2022-06-13 16:17:38.870909
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['red', 'blue', 'yellow', 'yellow', 'red', 'orange']) == ['red', 'blue', 'yellow', 'orange']



# Generated at 2022-06-13 16:17:42.860102
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['1','1','2','3','3','3','2','5','5','5','5','5']
    result_list = ['1','2','3','5']
    assert deduplicate_list(original_list) == result_list

# Generated at 2022-06-13 16:17:51.729607
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.a = 'test'
            self._b = 'test2'
            self.c = ['test3']
            self.d = 'test4'
            self._5 = 'test5'
            self.test6 = 'test6'

    t = Test()
    test1 = object_to_dict(t)
    test2 = object_to_dict(t, ['test6', 'c'])

    assert('a' in test1 and 'test' in test1.values())
    assert('d' in test1 and 'test4' in test1.values())
    assert('test6' in test1 and 'test6' in test1.values())
    assert('_b' not in test1)
    assert('c' not in test2)


# Generated at 2022-06-13 16:19:57.686687
# Unit test for function deduplicate_list
def test_deduplicate_list():
    foo=['a','b','c','b','a','d']
    expected_result=['a','b','c','d']
    deduplicated_list = deduplicate_list(foo)
    assert (expected_result==deduplicated_list)



# Generated at 2022-06-13 16:19:59.015608
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 3, 4, 4]) == [1, 2, 3, 4]


# Generated at 2022-06-13 16:20:04.730047
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1,2,3,4,3,2,1]
    dedup_list = deduplicate_list(original_list)
    # the original list should not have been mutated
    assert original_list == [1,2,3,4,3,2,1]
    # the dedup_list should be unique and ordered
    assert dedup_list == [1, 2, 3, 4]

