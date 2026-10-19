

# Generated at 2022-06-13 16:10:07.960111
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int(50, 100) == 50
    assert pct_to_int('50', 100) == 50
    assert pct_to_int('50.85', 100) == 50
    assert pct_to_int(50.85, 100) == 50


# Generated at 2022-06-13 16:10:20.134164
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        """Test class"""
        def __init__(self, name, foo=None, bar=None):
            self.name = name
            self.foo = foo
            self.bar = bar

        def _secret(self):
            return "BOO!"

    foo = Test('foo')
    foo_dict = object_to_dict(foo)
    assert foo_dict['name'] == 'foo'
    assert foo_dict['foo'] is None
    assert foo_dict['bar'] is None
    assert '_secret' not in foo_dict

    foo_dict = object_to_dict(foo, exclude=['name'])
    assert foo_dict['name'] == 'foo'
    assert foo_dict['foo'] is None
    assert foo_dict['bar'] is None

# Generated at 2022-06-13 16:10:27.543552
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('10%', 200) == 20

# Generated at 2022-06-13 16:10:33.159025
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Testing with a list of integers
    original_list = [2, 2, 3, 2, 1, 2]
    assert deduplicate_list(original_list) == [2, 3, 1]

    # Testing with a list of strings
    original_list = ["banana", "apple", "banana", "orange"]
    assert deduplicate_list(original_list) == ["banana", "apple", "orange"]


# Generated at 2022-06-13 16:10:36.000828
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['foo', 'bar', 'baz', 'foo', 'bar']) == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:10:45.535713
# Unit test for function object_to_dict
def test_object_to_dict():
    class testobj:
        test1 = 'test1'
        test2 = 'test2'
        test3 = 'test3'

        def __init__(self):
            self.test1 = 'test1_init'
            self.test4 = 'test4'

    assert object_to_dict(testobj(),['test2','test3']) == {'test1': 'test1_init', 'test4': 'test4'}
    assert object_to_dict(testobj(),['test2','test4']) == {'test1': 'test1_init', 'test3': 'test3'}
    assert object_to_dict(testobj(),['test3','test4']) == {'test1': 'test1_init', 'test2': 'test2'}


# Generated at 2022-06-13 16:10:52.697252
# Unit test for function pct_to_int
def test_pct_to_int():
    num_items = 10
    assert pct_to_int(10, num_items) == 10
    assert pct_to_int(10.0, num_items) == 10
    assert pct_to_int(10.1, num_items) == 10
    assert pct_to_int("10%", num_items) == 1
    assert pct_to_int("101%", num_items) == 10
    assert pct_to_int("10%", num_items) == pct_to_int("10.0%", num_items)
    assert pct_to_int("10.1%", num_items) == 1
    assert pct_to_int("0%", num_items) == 0
    assert pct_to_int("0.0%", num_items) == 0
   

# Generated at 2022-06-13 16:11:03.624739
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(5, 200) == 10
    assert pct_to_int(5, 200, min_value=5) == 10
    assert pct_to_int(5, 0) == 0
    assert pct_to_int(5, 0, min_value=5) == 5
    assert pct_to_int(5, 100) == 5
    assert pct_to_int(5, 100, min_value=5) == 5
    assert pct_to_int("5%", 100) == 5
    assert pct_to_int("5%", 100, min_value=5) == 5
    assert pct_to_int("5%", 0) == 0
    assert pct_to_int("5%", 0, min_value=5) == 5
    assert pct_

# Generated at 2022-06-13 16:11:06.821468
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    deduped_list = deduplicate_list(test_list)
    assert deduped_list == [1, 2, 3, 4]

# Generated at 2022-06-13 16:11:14.497749
# Unit test for function pct_to_int
def test_pct_to_int():

    # Common cases
    assert pct_to_int(10, 100) == 10
    assert pct_to_int("10%", 100) == 10

    # Edge cases
    assert pct_to_int("0", 100) == 0
    assert pct_to_int("0%", 100) == 0
    assert pct_to_int("100%", 100) == 100
    assert pct_to_int("101%", 100) == 101
    assert pct_to_int("100.5%", 100) == 100
    assert pct_to_int("100.5%", 100, min_value=0) == 100
    assert pct_to_int("100.5%", 100, min_value=1) == 101

# Generated at 2022-06-13 16:11:25.178458
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1,2,3,3,3,3,1,1,2,2,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    deduplicated_list = deduplicate_list(original_list)
    assert(len(deduplicated_list) == 4)




# Generated at 2022-06-13 16:11:29.984347
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from ansible.module_utils.nxos import deduplicate_list
    assert list(deduplicate_list(['1', '2', '2', '3'])) == ['1', '2', '3']



# Generated at 2022-06-13 16:11:37.146165
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        test_attr1 = 1
        test_attr2 = "test"
        test_attr3 = [1, 2, 3]
        test_attr4 = None

    result = object_to_dict(TestObject())
    assert result['test_attr1'] == 1
    assert result['test_attr2'] == "test"
    assert result['test_attr3'] == [1, 2, 3]
    assert result['test_attr4'] is None


# Generated at 2022-06-13 16:11:42.574526
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj:
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self.c = 'c'
            self.d = 'd'

    test_obj = TestObj()
    expected = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'}
    assert object_to_dict(test_obj, exclude=['a']) == expected



# Generated at 2022-06-13 16:11:45.138480
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3, 4, 3, 2, 4]) == [1, 2, 3, 4]

# Generated at 2022-06-13 16:11:51.057411
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'a', 'b']) == ['a', 'b']
    assert deduplicate_list(['a', 'b', 'a']) == ['a', 'b']
    assert deduplicate_list(['a', 'b', 'c', 'a']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'c', 'a', 'b']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:12:01.069237
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from collections import OrderedDict
    from collections import deque
    from collections import Counter

    assert (deduplicate_list([list(),list()]) == [list()])
    assert (deduplicate_list(['test', 'dev', 'test']) == ['test', 'dev'])
    assert (deduplicate_list(OrderedDict((('test', 1), ('dev', 2), ('test', 3)))) == ['test', 'dev'])
    assert (deduplicate_list(deque(['test', 'dev', 'test'])) == ['test', 'dev'])
    assert (deduplicate_list(Counter(['test', 'test', 'dev'])) == ['test', 'dev'])



# Generated at 2022-06-13 16:12:07.154682
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_ = [1, 3, 2, 4, 3, 4, 1, 2, 2, 4, 5, 7, 6, 5, 5, 7, 6, 4, 5, 7]
    deduplicated_list = deduplicate_list(list_)
    assert deduplicated_list == [1, 3, 2, 4, 5, 7, 6]



# Generated at 2022-06-13 16:12:15.399237
# Unit test for function object_to_dict
def test_object_to_dict():
    class test:
        def __init__(self, test1=None, test2=None, test3=None):
            self.test1 = test1
            self.test2 = test2
            self.test3 = test3

    obj = test("test1", test2="test2", test3="test3")
    result = object_to_dict(obj)
    assert result == {'test1': 'test1', 'test2': 'test2', 'test3': 'test3'}
    result = object_to_dict(obj, ['test1'])
    assert result == {'test2': 'test2', 'test3': 'test3'}
    result = object_to_dict(obj, ['test2'])
    assert result == {'test1': 'test1', 'test3': 'test3'}

# Generated at 2022-06-13 16:12:17.795818
# Unit test for function deduplicate_list
def test_deduplicate_list():
    my_list = [1, 2, 1, 3, 3, 4, 5, 4, 6]
    deduplicated_list = deduplicate_list(my_list)
    assert deduplicated_list == [1, 2, 3, 4, 5, 6]

# Generated at 2022-06-13 16:12:26.460628
# Unit test for function object_to_dict
def test_object_to_dict():
    class Obj(object):
        def __init__(self):
            self.a = 'Cisco'
            self.b = 'Ansible'
            self.c = 123

    obj = Obj()
    assert object_to_dict(obj) == {'a': 'Cisco', 'b': 'Ansible', 'c': 123}
    assert object_to_dict(obj, ['a']) == {'b': 'Ansible', 'c': 123}



# Generated at 2022-06-13 16:12:32.792082
# Unit test for function object_to_dict
def test_object_to_dict():
    class DummyClass(object):
        def __init__(self, name, id):
            self.name = name
            self.id = id

    dummy_object = DummyClass('test', 1234)
    assert object_to_dict(dummy_object, ['id']) == dict(name='test')



# Generated at 2022-06-13 16:12:38.756370
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert sorted(deduplicate_list([1, 2, 1, 2, 1, 2])) == [1, 2]
    assert sorted(deduplicate_list([1, 4, 2, 4, 3, 1, 2])) == [1, 2, 3, 4]
    assert sorted(deduplicate_list([1, 2])) == [1, 2]
    assert sorted(deduplicate_list([1])) == [1]
    assert sorted(deduplicate_list([])) == []


# Generated at 2022-06-13 16:12:47.630321
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self, val1, val2):
            self.val1 = val1
            self.val2 = val2
            self.val3 = val1 + val2

    test_obj = Test(1, 2)
    test_dict = object_to_dict(test_obj)
    assert test_dict == {'val1': 1, 'val3': 3, 'val2': 2}
    test_dict = object_to_dict(test_obj, exclude=['val2'])
    assert test_dict == {'val1': 1, 'val3': 3}
    test_dict = object_to_dict(test_obj, exclude=['this_key_does_not_exist'])

# Generated at 2022-06-13 16:12:54.544562
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 1, 3, 1, 2, 4]) == [1, 2, 3, 4]
    assert deduplicate_list([1, 1, 1, 3, 3, 3, 1, 1, 1, 3, 3, 3, 1, 1, 1, 3, 3, 3]) == [1, 3]

# Generated at 2022-06-13 16:12:56.267770
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 1, 2, 3, 4]) == [1, 2, 3, 4]

# Generated at 2022-06-13 16:13:02.000954
# Unit test for function object_to_dict
def test_object_to_dict():
    class obj(object):
        def __init__(self):
            self.a = "foo"
            self.b = "bar"

    obj_dict = object_to_dict(obj())
    assert obj_dict['a'] == 'foo'
    assert obj_dict['b'] == 'bar'

    obj_dict = object_to_dict(obj(), exclude=['a'])
    assert 'a' not in obj_dict
    assert obj_dict['b'] == 'bar'

# Generated at 2022-06-13 16:13:10.465256
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj(object):
        def __init__(self):
            self.test_attr = "test_attr"
            self.test_dict = dict()
            self.test_list = list()
            self._test_priv = "test_priv"
    obj = TestObj()
    actual = object_to_dict(obj)
    expected = dict()
    expected["test_attr"] = "test_attr"
    expected["test_dict"] = dict()
    expected["test_list"] = list()

    assert actual == expected

# Generated at 2022-06-13 16:13:13.657915
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_to_test = [1, 2, 2, 4, 5, 1]
    assert deduplicate_list(list_to_test) == [1, 2, 4, 5]

# Generated at 2022-06-13 16:13:19.297016
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    This is used as a unit test
    """
    class testObject:
        """
        class used for testing
        """
        def __init__(self):
            self.testproperty1 = "testvalue1"
            self.testproperty2 = "testvalue2"
    obj = testObject()
    objdict = object_to_dict(obj)
    assert objdict['testproperty1'] == "testvalue1"
    assert objdict['testproperty2'] == "testvalue2"

# Generated at 2022-06-13 16:13:35.598332
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test():
        pass

    test_obj = Test()
    test_obj.attribute_1 = "Test attribute 1"
    test_obj.attribute_2 = "Test attribute 2"

    assert object_to_dict(test_obj) == dict(attribute_1="Test attribute 1", attribute_2="Test attribute 2")
    assert object_to_dict(test_obj, exclude=["attribute_2"]) == dict(attribute_1="Test attribute 1")

# Generated at 2022-06-13 16:13:46.620061
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self.c = 'c'
            self.d = 'd'
            self.e = 'e'
            self.f = 'f'

    test_obj = TestObject()
    original = ['a', 'b', 'c', 'd', 'e', 'f']
    exclude = ['e', 'f']
    retval = object_to_dict(test_obj, exclude)
    assert set(retval.keys()) == set(original) - set(exclude)
    assert len(retval) == len(original) - len(exclude)

# Generated at 2022-06-13 16:13:51.268710
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.a = 'a'
            self.b = 'b'

    obj = TestClass()
    assert object_to_dict(obj) == {'a': 'a', 'b': 'b'}



# Generated at 2022-06-13 16:13:54.287761
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'a', 'c', 'd', 'a', 'b']) == ['a', 'b', 'c', 'd']



# Generated at 2022-06-13 16:13:55.795243
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 2, 1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-13 16:13:58.362647
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list1 = ['foo', 'bar', 'foo', 'baz']
    list2 = ['foo', 'bar', 'baz']
    assert deduplicate_list(list1) == list2

# Generated at 2022-06-13 16:14:09.077605
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert deduplicate_list(['a', 'b', 'a', 'c', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list([[1, 2], [3, 4, 5], [3, 4, 5]]) == [[1, 2], [3, 4, 5]]
    assert deduplicate_list([1, 2, 3, 2, 1]) != [1, 2, 3, 2, 1]
    assert deduplicate_list(['a', 'b', 'a', 'c', 'c']) != ['a', 'b', 'a', 'c', 'c']

# Generated at 2022-06-13 16:14:15.596710
# Unit test for function object_to_dict
def test_object_to_dict():
    class Object(object):
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self.c = 'c'
            self._d = 'd'
            self._e = 'e'

    obj = Object()
    res = object_to_dict(obj, exclude=['b', 'c'])
    assert(res.get('a') == obj.a)
    assert(res.get('b') is None)
    assert(res.get('_d') == obj._d)



# Generated at 2022-06-13 16:14:19.532951
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Tests converting an object to a dict
    """
    class Test(object):
        def __init__(self, key1, key2):
            self.key1 = key1
            self.key2 = key2

    test = Test('value1', 'value2')
    assert object_to_dict(test) == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2022-06-13 16:14:22.540543
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj(object):
        var1 = "foo"
        var2 = "bar"

    t = TestObj()
    assert object_to_dict(t) == {'var1': 'foo', 'var2': 'bar'}
    assert object_to_dict(t, exclude=['var2']) == {'var1': 'foo'}

# Generated at 2022-06-13 16:14:45.163310
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['a','b','b','c','c','c','a','a','d','e','e','f']
    expected_list = ['a','b','c','d','e','f']
    assert deduplicate_list(test_list) == expected_list


# Generated at 2022-06-13 16:14:49.809686
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'a', 'c', 'b']
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == ['a', 'b', 'c']



# Generated at 2022-06-13 16:14:54.443206
# Unit test for function deduplicate_list
def test_deduplicate_list():
    x = ['a', 'b', 'a']
    y = ['a', 'b', 'b']
    z = [1, 2, 1]

    assert deduplicate_list(x) == ['a', 'b']
    assert deduplicate_list(y) == ['a', 'b']
    assert deduplicate_list(z) == [1, 2]

# Generated at 2022-06-13 16:14:58.982719
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,1,1,2,2,3]) == [1,2,3]
    assert deduplicate_list([1,1,1,2,2,3]) != [1,1,1,2,2,3]
    assert deduplicate_list([1,2,3]) == [1,2,3]


# Generated at 2022-06-13 16:15:07.713000
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_class:
        def __init__(self):
            self.test_var = "test_value"
            self.test_var2 = "test_value2"
            self._test_var3 = "test_value3"

    test_instance = test_class()
    assert object_to_dict(test_instance) == {"test_var": "test_value", "test_var2": "test_value2"}
    assert object_to_dict(test_instance, ["test_var"]) == {"test_var2": "test_value2"}



# Generated at 2022-06-13 16:15:15.201594
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        exclude_me = None
        def __init__(self):
            self.param_one = 'one'
            self.param_two = 'two'
    obj = TestClass()
    assert object_to_dict(obj) == {'param_one': 'one', 'param_two': 'two'}

    obj = TestClass()
    assert object_to_dict(obj, exclude=['exclude_me']) == {'param_one': 'one', 'param_two': 'two'}

    obj = TestClass()
    assert object_to_dict(obj, exclude=['param_two', 'exclude_me']) == {'param_one': 'one'}

# Generated at 2022-06-13 16:15:25.021914
# Unit test for function object_to_dict
def test_object_to_dict():
    # Setting up object
    class test_obj():
        def __init__(self):
            self.key1 = 'value1'
            self.key2 = 'value2'
            self.key3 = 'value3'
        def exclude_this_method(self):
            pass
    test_obj = test_obj()
    # Testing object_to_dict
    test_dict = object_to_dict(test_obj, ['exclude_this_method'])
    assert test_dict == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Generated at 2022-06-13 16:15:34.025199
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj(object):
        def __init__(self):
            self.one = 1
            self.two = 2
            self.three = 3

    obj = TestObj()
    d = object_to_dict(obj, ['one'])
    assert d['one'] == 1
    assert d['two'] == 2
    assert d['three'] == 3

    obj = TestObj()
    d = object_to_dict(obj, ['two'])
    assert not d['one']
    assert d['two'] == 2
    assert d['three'] == 3

# Generated at 2022-06-13 16:15:37.273459
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self.c = 'c'

    test = Test()

    assert object_to_dict(test) == {'a': 'a', 'b': 'b', 'c': 'c'}


# Generated at 2022-06-13 16:15:42.179838
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['1', '2', '3', '4', '1', '4', '3', '5']
    expected_output = ['1', '2', '3', '4', '5']

    assert deduplicate_list(test_list) == expected_output

# Generated at 2022-06-13 16:16:23.842279
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list1 = [1, 2, 3, 4, 3, 2, 1]
    assert deduplicate_list(list1) == [1, 2, 3, 4]

    list2 = [5, 5, 6, 7, 8, 5, 6, 7, 1, 8, 7, 4, 5]
    assert deduplicate_list(list2) == [5, 6, 7, 8, 1, 4]


# Generated at 2022-06-13 16:16:28.786482
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list(['a', 'a', 'b', 'a', 'b', 'c', 'b', 'c', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'b', 'a', 'c', 'b', 'c', 'c']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:16:32.095169
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_to_test = [1, 2, 3, 1, 5, 6, 3, 3, 3, 4]
    assert deduplicate_list(list_to_test) == [1, 2, 3, 5, 6, 4]

# Generated at 2022-06-13 16:16:40.191034
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1,2,3,4]) == [1,2,3,4]
    assert deduplicate_list([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == [1]
    assert deduplicate_list([1,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]) == [1,2,3,4]

# Generated at 2022-06-13 16:16:46.003127
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Test case with a list with no elements
    l1 = []
    assert deduplicate_list(l1) == []

    # Test case with a list with one element
    l2 = ["foo"]
    assert deduplicate_list(l2) == ["foo"]

    # Test case with a list with two elements
    l3 = ["foo", "bar"]
    assert deduplicate_list(l3) == ["foo", "bar"]

    # Test case with a list with two identical elements
    l4 = ["foo", "foo"]
    assert deduplicate_list(l4) == ["foo"]

    # Test case with a list with 3 elements and an identical element
    l5 = ["foo", "bar", "foo", "baz"]

# Generated at 2022-06-13 16:16:52.188092
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.prop1 = "prop1"
            self.prop2 = "prop2"
            self._prop3 = "prop3"

    test_obj = TestClass()

    assert object_to_dict(test_obj) == {'prop1': 'prop1', 'prop2': 'prop2'}
    assert object_to_dict(test_obj, ["prop1"]) == {'prop2': 'prop2'}

# Generated at 2022-06-13 16:16:55.959494
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original = [1, 2, 3, 2, 1]
    expected = [1, 2, 3]
    result = deduplicate_list(original)

    assert(result == expected)


# Generated at 2022-06-13 16:17:05.328235
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list
    """
    assert deduplicate_list([1, 1, 2, 3, 3, 4]) == [1, 2, 3, 4]
    assert deduplicate_list([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert deduplicate_list([1, 2, 3, 4, 3, 1]) == [1, 2, 3, 4]
    assert deduplicate_list([]) == []
    assert deduplicate_list(1) == 1
    assert deduplicate_list(None) == None



# Generated at 2022-06-13 16:17:12.694499
# Unit test for function object_to_dict
def test_object_to_dict():
    # Create class with attributes
    class TestClass(object):
        def __init__(self):
            self.prop1 = 'value1'
            self.prop2 = 'value2'

    # Convert to dict, verify
    obj1 = TestClass()
    dict1 = object_to_dict(obj1)
    assert dict1['prop1'] == 'value1'
    assert dict1['prop2'] == 'value2'

    # Convert to dict excluding keys, verify
    dict2 = object_to_dict(obj1, ['prop1'])
    assert dict2['prop1'] is None
    assert dict2['prop2'] == 'value2'

    # Verify attribute has been added to class
    assert obj1.prop1 == 'value1'
    assert obj1.prop2 == 'value2'

# Generated at 2022-06-13 16:17:20.904783
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.first_property = "first"
            self.second_property = "second"
            self.third_property = "third"
    
    obj_to_dict = object_to_dict(TestObject())
    assert(len(obj_to_dict) == 3)
    assert(obj_to_dict['first_property'] == 'first')
    assert(obj_to_dict['second_property'] == 'second')
    assert(obj_to_dict['third_property'] == 'third')


# Generated at 2022-06-13 16:18:50.468832
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'b', 'a', 'd', 'c']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(['a', 'a', 'a']) == ['a']
    assert deduplicate_list(['a', 'a', 'a', 'b']) == ['a', 'b']
    assert deduplicate_list(['a' * 100, 'b', 'a' * 100]) == ['a' * 100, 'b']
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:18:59.831968
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list1 = ['a', 'b', 'c', 'b', 'a']
    list2 = ['q', 'z', 'w', 'w', 'a', 'a', 'a', 'z', 'c', 'c', 'a']
    list3 = []
    assert deduplicate_list(list1) == ['a', 'b', 'c']
    assert deduplicate_list(list2) == ['q', 'z', 'w', 'a', 'c']
    assert deduplicate_list(list3) == []


# Generated at 2022-06-13 16:19:08.263413
# Unit test for function deduplicate_list
def test_deduplicate_list():
    print(deduplicate_list(['a','b','c','d','c','a','f','g']))
    print(deduplicate_list(['a','b','b','c','c','d','d','c','a','f','g']))
    print(deduplicate_list(['a','b','c','d','d','d','c','a','f','g']))
    print(deduplicate_list(['a','a','a','a','a','c','d','c','a','f','g']))

# Generated at 2022-06-13 16:19:13.729569
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyClass:
        def __init__(self):
            self.var1 = 1
            self.var2 = 2
            self.var3 = 3
    my_obj = MyClass()
    my_dict = object_to_dict(my_obj, exclude=['var2'])
    assert my_dict['var1'] == 1
    assert 'var2' not in my_dict
    assert my_dict['var3'] == 3

# Generated at 2022-06-13 16:19:17.040355
# Unit test for function deduplicate_list
def test_deduplicate_list():
    input_list = ['a', 'b', 'c', 'a', 'd', 'c']
    new_list = deduplicate_list(input_list)
    assert new_list == ['a', 'b', 'c', 'd']


# Generated at 2022-06-13 16:19:21.549517
# Unit test for function deduplicate_list
def test_deduplicate_list():
    deduplicate_list_test = deduplicate_list
    assert_equals = 'test_deduplicate_list()'
    mylist = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
    result = deduplicate_list_test(mylist)
    assert_equals('a', 'b', result)



# Generated at 2022-06-13 16:19:26.576066
# Unit test for function object_to_dict
def test_object_to_dict():
    from ansible.module_utils.network_common import ComplexObject

    class TestClass(object):
        def __init__(self):
            self.a = 1
            self.b = 2

    obj = TestClass()
    _ = ComplexObject(**object_to_dict(obj))
    assert _.a == 1
    assert _.b == 2

# Generated at 2022-06-13 16:19:29.427044
# Unit test for function deduplicate_list
def test_deduplicate_list():
    lst = ['1', '2', '3', '4', '2', '4', '3']
    assert deduplicate_list(lst) == ['1', '2', '3', '4']


# Generated at 2022-06-13 16:19:36.283963
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Test object_to_dict.
    """
    class some_class(object):
        def __init__(self):
            self.prop1 = 'value1'
            self.prop2 = 'value2'
            self.prop3 = 'value3'

    class_obj = some_class()
    exclude = ['prop2']

    result = object_to_dict(some_object, exclude)
    assert set(result.keys()) == set(['prop1', 'prop3'])
    assert result['prop1'] == 'value1'
    assert result['prop3'] == 'value3'

# Generated at 2022-06-13 16:19:44.925947
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1,2,3,3,4,4,4,5]
    assert [1,2,3,4,5] == deduplicate_list(original_list)

    original_list = [1,2,3,4,5]
    assert [1,2,3,4,5] == deduplicate_list(original_list)

    original_list = [1,2,3,4,5,5,5,5]
    assert [1,2,3,4,5] == deduplicate_list(original_list)

    original_list = ['a','b','c','d','b','d','a']
    assert ['a','b','c','d'] == deduplicate_list(original_list)
