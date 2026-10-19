

# Generated at 2022-06-13 16:10:20.132843
# Unit test for function pct_to_int
def test_pct_to_int():
    # Simple pct to int test
    assert pct_to_int('20%', 100) == 20
    # Simple int to int test
    assert pct_to_int('20', 100) == 20
    # Test a pct to int with min_value set
    assert pct_to_int('0%', 100, min_value=10) == 10
    # Test a pct to int with min_value set and multiplicates to be over min_value
    assert pct_to_int('1%', 100, min_value=10) == 10
    assert pct_to_int('20%', 20, min_value=10) == 4
    assert pct_to_int('20%', 40, min_value=10) == 8
    assert pct_to_int('20%', 60, min_value=10)

# Generated at 2022-06-13 16:10:25.476911
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(50, 10) == 5
    assert pct_to_int('50%', 10) == 5
    assert pct_to_int('50%', 10, min_value=2) == 2
    assert pct_to_int('0%', 10) == 1
    assert pct_to_int(0, 10) == 0



# Generated at 2022-06-13 16:10:28.115889
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests deduplicate_list function
    """
    assert deduplicate_list([1, 2, 3, 1, 5]) == [1, 2, 3, 5]



# Generated at 2022-06-13 16:10:32.238670
# Unit test for function pct_to_int
def test_pct_to_int():
    assert 100 == pct_to_int('10%', 1000)
    assert 10 == pct_to_int('10%', 100)
    assert 1 == pct_to_int('10%', 100, min_value=1)
    assert 10 == pct_to_int('10', 100)


# Generated at 2022-06-13 16:10:38.117145
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [5, 5, 5, 4, 3, 4, 3, 3, 3, 1, 2, 1, 2, 1]
    result_list = deduplicate_list(test_list)
    if result_list != [5, 4, 3, 1, 2]:
        return False
    else:
        return True

# Generated at 2022-06-13 16:10:41.100142
# Unit test for function pct_to_int
def test_pct_to_int():
    assert (pct_to_int('100%', 1000) == 1000)
    assert (pct_to_int('50%', 1000) == 500)
    assert (pct_to_int('0.01%', 1000) == 1)

# Generated at 2022-06-13 16:10:45.221330
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('20%', 400, min_value=1) == 80
    assert pct_to_int(10, 1000, min_value=1) == 10
    assert pct_to_int('10', 1000, min_value=1) == 10
    assert pct_to_int('0', 1000, min_value=1) == 1

# Generated at 2022-06-13 16:10:52.448546
# Unit test for function pct_to_int
def test_pct_to_int():
    """ pct_to_int() returns 0 for '0%' """
    assert pct_to_int('0%', 1000) == 0
    """ pct_to_int() returns 10 for '0.1%' """
    assert pct_to_int('0.1%', 1000) == 1
    """ pct_to_int() returns 10 for '10%' """
    assert pct_to_int('10%', 1000) == 10
    """ pct_to_int() returns 99 for '99%' """
    assert pct_to_int('99%', 100) == 99
    """ pct_to_int() returns 100 for '100%' """
    assert pct_to_int('100%', 100) == 100
    """ pct_to_int() returns 1 for '0.99%' """


# Generated at 2022-06-13 16:10:55.641983
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(0, 6) == 0
    assert pct_to_int(100, 6) == 6
    assert pct_to_int(80, 6) == 4
    assert pct_to_int(90, 6) == 5
    assert pct_to_int(50, 6) == 3
    assert pct_to_int(35, 6) == 1
    assert pct_to_int(35, 2) == 1


# Generated at 2022-06-13 16:11:00.081484
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int('50.5%', 100) == 51
    assert pct_to_int('50.6%', 100) == 51
    assert pct_to_int('50.5%', 100, min_value=2) == 51
    assert pct_to_int('0.5%', 100) == 1
    assert pct_to_int(100, 100) == 100


# Generated at 2022-06-13 16:11:10.126323
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.prop1 = None
            self.prop2 = None
            self._exclude_me = None
            self.exclude_me2 = None
    test_object = TestClass()
    test_object.prop1 = 'value1'
    test_object.prop2 = 'value2'
    test_object._exclude_me = 'value3'
    test_object.exclude_me2 = 'value4'
    exclude_me = ['exclude_me2']
    assert object_to_dict(test_object, exclude=exclude_me) == {'prop1': 'value1', 'prop2': 'value2'}



# Generated at 2022-06-13 16:11:20.641716
# Unit test for function object_to_dict
def test_object_to_dict():
    from ncclient.operations.third_party.iosxr.rpc import Bgp
    from ncclient.xml_ import BASE_NS_1_0, new_ele
    bgp = Bgp(ns_prefix='test', ns_uri='test')
    bgp.fields = True
    bgp.global_bgp.instance_name = 'name_1'
    dict_ele = object_to_dict(bgp)
    assert dict_ele == {'instance_name': 'name_1',
                        'fields': True,
                        'ns_prefix': 'test',
                        'ns_uri': 'test',
                        'xpath': '/test:bgp',
                        'xmlns': 'test'}

    bgp_ele = new_ele('bgp')

# Generated at 2022-06-13 16:11:23.695604
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 3, 3, 2, 1]
    assert [1, 2, 3] == deduplicate_list(original_list)



# Generated at 2022-06-13 16:11:33.344931
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'c', 'b', 'c', 'd']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(['b', 'a', 'c', 'c', 'c', 'b', 'd']) == ['b', 'a', 'c', 'd']
    assert deduplicate_list(['a', 'a', 'a', 'a']) == ['a']
    assert deduplicate_list(['a']) == ['a']
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:11:36.199736
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test = [1, 2, 2, 3, 1]
    assert deduplicate_list(test) == [1, 2, 3]



# Generated at 2022-06-13 16:11:41.598327
# Unit test for function object_to_dict
def test_object_to_dict():
    class SampleObject(object):
        def __init__(self):
            self.some_prop = None

    obj = SampleObject()
    obj.some_prop = "some value"

    assert object_to_dict(obj) == {"some_prop": "some value"}



# Generated at 2022-06-13 16:11:49.732949
# Unit test for function deduplicate_list
def test_deduplicate_list():

    assert deduplicate_list([1,2,3]) == [1,2,3]
    assert deduplicate_list([1,1,2,2,3,3]) == [1,2,3]
    assert deduplicate_list([1,2,3,3,3,3,3]) == [1,2,3]
    assert deduplicate_list([1,2,3,2,1]) == [1,2,3]
    assert deduplicate_list([3,3,3,3,3,1,2,3,2,1]) == [3,1,2]


# Generated at 2022-06-13 16:11:56.931411
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 5, 6, 3]) == [1, 2, 3, 5, 6]
    assert deduplicate_list([1, 2, 3, 1, 5, 6, 3, 6]) == [1, 2, 3, 5, 6]
    assert deduplicate_list([1, 2, 3, 1, 5, 6, 3, 1]) == [1, 2, 3, 5, 6]

# Generated at 2022-06-13 16:12:01.795592
# Unit test for function deduplicate_list
def test_deduplicate_list():
    deduplicated_list = deduplicate_list(["a", "b", "a", "b", "c", "c", "a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d", "e", "a", "b", "c", "d", "e", "z"])
    assert deduplicated_list == ["a", "b", "c", "d", "e", "z"]
    assert len(deduplicated_list) == 6


# Generated at 2022-06-13 16:12:11.198490
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
            self._exclude_me = 'test'
    test_obj = TestClass()
    test_dict = object_to_dict(test_obj, exclude=['_exclude_me'])
    assert test_dict['a'] == 1
    assert test_dict['b'] == 2
    assert test_dict['c'] == 3
    assert not test_dict.has_key('_exclude_me')

# Generated at 2022-06-13 16:12:22.900100
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3, 2, 4]) == [1, 2, 3, 4]  # duplicate
    assert deduplicate_list([]) == []                            # empty list
    assert deduplicate_list(["a", "b", "c"]) == ["a", "b", "c"]  # no duplicates

# Generated at 2022-06-13 16:12:27.205789
# Unit test for function object_to_dict
def test_object_to_dict():

    class Foo(object):
        def __init__(self):
            self.a = '1'
            self.b = '2'
            self.c = '3'

    assert object_to_dict(Foo()) == {'a': '1', 'c': '3', 'b': '2'}
    assert object_to_dict(Foo(), exclude=['b']) == {'a': '1', 'c': '3'}

# Generated at 2022-06-13 16:12:38.496161
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(["a", "b", "c", "b", "a", "a", "b", "c"]) == ["a", "b", "c"]
    assert deduplicate_list([]) == []
    assert deduplicate_list(["a", "a", "a", "a", "a", "a", "a", "a"]) == ["a"]
    assert deduplicate_list(["b", "b", "c", "c", "a", "a", "a", "b", "b", "c", "c", "b", "c"]) == ["b", "c", "a"]

# Generated at 2022-06-13 16:12:44.935120
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_object:
        def __init__(self):
            self.name = 'test'
            self._secret = 's3cr3t'
    obj = test_object()
    assert object_to_dict(obj) == {'name': 'test'}
    assert object_to_dict(obj, exclude=['name']) == {}
    assert object_to_dict(obj, exclude=['name', '_secret']) == {}


# Generated at 2022-06-13 16:12:51.394453
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyObj(object):
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self._c = 'c'
    my = MyObj()
    d = object_to_dict(my)
    assert '_c' not in d
    assert 'a' in d
    d = object_to_dict(my, exclude=['a'])
    assert 'a' not in d

# Generated at 2022-06-13 16:13:00.239788
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Test the function with a simple list of integers
    assert deduplicate_list([1,2,3,2,1]) == [1,2,3]
    # Test the function with a simple list of strings
    assert deduplicate_list(['1','2','3','2','1']) == ['1','2','3']
    # Test the function with a simple list of strings
    assert deduplicate_list(['1',2,3,2,'1']) == ['1',2,3]
    # Test the function with a list of strings and numbers and strings that look like numbers
    assert deduplicate_list(['1',2,'3',2,'1.0']) == ['1',2,'3']
    # Test the function with a list that contains a null value - the null value should be returned
    assert ded

# Generated at 2022-06-13 16:13:03.286552
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([7, 8, 2, 3, 3, 3, 4, 4, 2, 2, 2, 2, 9, 6, 5, 5, 0]) == [7, 8, 2, 3, 4, 9, 6, 5, 0]
    assert deduplicate_list([]) == []


# Generated at 2022-06-13 16:13:14.122108
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.foo = 'Test'
            self.bar = 'Value'
            self.foobar = 'TestValue'
        def test_method(self):
            return True
    tc = TestClass()
    assert object_to_dict(tc) == {'foo': 'Test', 'bar': 'Value', 'foobar': 'TestValue'}
    assert object_to_dict(tc, exclude=['foo']) == {'bar': 'Value', 'foobar': 'TestValue'}
    assert object_to_dict(tc, exclude=['foo', 'foobar']) == {'bar': 'Value'}

# Generated at 2022-06-13 16:13:20.090146
# Unit test for function object_to_dict
def test_object_to_dict():

    class WildObject(object):
        def __init__(self):
            self.id = 0
            self.name = 'WildObject'

    obj = WildObject()

    assert object_to_dict(obj) == {'name': 'WildObject', 'id': 0}
    assert object_to_dict(obj, exclude=['name']) == {'id': 0}

# Generated at 2022-06-13 16:13:25.217115
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3]) == ([1, 2, 3])
    assert deduplicate_list([1, 2, 1, 1, 3]) == ([1, 2, 3])
    assert deduplicate_list([]) == ([])
    assert deduplicate_list([1, 1, 1, 1, 1, 1]) == ([1])

# Generated at 2022-06-13 16:13:54.094695
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Testing for correct results
    assert deduplicate_list(['foo', 'bar', 'foo', 'bar']) == ['foo', 'bar']
    assert deduplicate_list([]) == []
    assert deduplicate_list(['foo']) == ['foo']
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1, 2, 'foo', 'bar', 1, 'bar']) == [1, 2, 'foo', 'bar']


# Generated at 2022-06-13 16:13:59.570084
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 4, 2, 5, 2]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 1, 3, 3, 2, 4, 2, 5, 2]) == [1, 3, 2, 4, 5]
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]


# Generated at 2022-06-13 16:14:03.879497
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        attr1 = 'test'
        attr2 = 1

    assert object_to_dict(TestClass()) == {'attr1': 'test', 'attr2': 1}

# Generated at 2022-06-13 16:14:10.856373
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert ['a', 'b', 'c'] == deduplicate_list(['a', 'b', 'c'])
    assert ['a', 'b', 'c'] == deduplicate_list(['a', 'b', 'c', 'a', 'b', 'c'])
    assert ['a', 'b', 'a', 'b'] == deduplicate_list(['a', 'b', 'a', 'b'])
    assert ['a', 'b', 'c', 'a', 'b'] == deduplicate_list(['a', 'b', 'c', 'a', 'b', 'a', 'b'])

# Generated at 2022-06-13 16:14:13.839699
# Unit test for function object_to_dict
def test_object_to_dict():
    obj = {'name':'some_name'}
    exclude = ['name']

    assert object_to_dict(obj) == {'name':'some_name'}
    assert object_to_dict(obj, exclude) == {}

# Generated at 2022-06-13 16:14:17.719277
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    This function tests deduplicate_list function
    """
    original_list = ['a', 'b', 'a', 'c', 'a', 'c', 'b']
    duplicated_list = ['a', 'b', 'c']
    result = deduplicate_list(original_list)

    assert result == duplicated_list

# Generated at 2022-06-13 16:14:20.440820
# Unit test for function deduplicate_list
def test_deduplicate_list():

    assert deduplicate_list(['a','b','a','c','b','c','d','e']) == ['a','b','c','d','e']


# Generated at 2022-06-13 16:14:22.604986
# Unit test for function object_to_dict
def test_object_to_dict():
    class testClass(object):
        def __init__(self):
            self.test1 = None
            self.test2 = None
            self.test3 = None
    test_obj = testClass()
    test_obj.test1 = 1
    test_obj.test2 = 2
    test_obj.test3 = 3
    assert object_to_dict(test_obj) == {'test3': 3, 'test2': 2, 'test1': 1}

# Generated at 2022-06-13 16:14:27.977076
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert [1, 2, 3] == deduplicate_list([1, 1, 2, 2, 3, 1, 2, 3])
    assert [1, 2, 3] == deduplicate_list([1, 2, 3, 1, 2, 3])
    assert [1, 2, 3] == deduplicate_list([1, 2, 3])
    assert [1, 2, 3, 4] == deduplicate_list([1, 2, 3, 4, 4, 4, 1, 2, 3, 4])
    assert [1, 2, 3, 4] == deduplicate_list([1, 2, 3, 4])
    assert [] == deduplicate_list([])
    assert [1, 'a'] == deduplicate_list([1, 1, 'a', 'a', 1])
   

# Generated at 2022-06-13 16:14:36.224950
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_object:
        def __init__(self):
            self.one = 1
            self.two = 2
            self._three = 3
            self.four = 4

    obj = test_object()
    assert object_to_dict(obj) == {'_three': 3, 'four': 4, 'one': 1, 'two': 2}
    assert object_to_dict(obj, ['one']) == {'_three': 3, 'four': 4, 'one': 1, 'two': 2}
    assert object_to_dict(obj, ['one', 'two']) == {'_three': 3, 'four': 4, 'one': 1, 'two': 2}

# Generated at 2022-06-13 16:15:37.430203
# Unit test for function object_to_dict
def test_object_to_dict():
    class testObject(object):
        def __init__(self):
            self.test1 = "test1"
            self.test2 = "test2"
            self.test3 = "test3"
            self.test4 = "test4"

    obj = testObject()
    d = object_to_dict(obj,["test1"])

    assert len(d) == 3
    assert sorted(d.keys()) == ["test2", "test3", "test4"]
    assert dict(test2="test2", test3="test3", test4="test4") == d


# Generated at 2022-06-13 16:15:40.751624
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['no', 'yes', 'no']
    assert (deduplicate_list(test_list) == ['no', 'yes'])



# Generated at 2022-06-13 16:15:45.799074
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    dedup_list = deduplicate_list(test_list)
    if dedup_list == [1, 2]:
        return True
    else:
        return False

# Generated at 2022-06-13 16:15:51.713311
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(list(range(10))) == list(range(10)), "Lists should be equal"
    assert deduplicate_list([1, 1, 2, 3, 3, 3, 4, 4, 4]) == [1, 2, 3, 4], "Lists should be equal"
    assert deduplicate_list(list('xyz')) == ['x', 'y', 'z'], "Lists should be equal"
    assert deduplicate_list(list('xyzzzzzyzzx')) == ['x', 'y', 'z'], "Lists should be equal"


# Generated at 2022-06-13 16:16:02.576419
# Unit test for function deduplicate_list
def test_deduplicate_list():
    a = [5,5,5,5,5,5,'5',5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    b = ['c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

# Generated at 2022-06-13 16:16:09.154721
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'a', 'b', 'c', 'c', 'd']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(['a', 'b', 'c', 'd', 'a', 'c']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:16:14.116240
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'c', 'c', 'b']
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == ['a', 'b', 'c']

# Generated at 2022-06-13 16:16:23.982158
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_with_duplicates = ['a', 'b', 'c', 'a', 'c']
    list_no_duplicates = ['a', 'b', 'c']
    assert deduplicate_list(list_with_duplicates) == list_no_duplicates

    # Does not remove duplicates in different case
    list_with_duplicates = ['a', 'b', 'c', 'A', 'c']
    list_no_duplicates = ['a', 'b', 'c', 'A', 'c']
    assert deduplicate_list(list_with_duplicates) == list_no_duplicates

    # Duplicates are not reordered
    list_with_duplicates = ['a', 'b', 'c', 'a', 'c']
    list_no_duplicates

# Generated at 2022-06-13 16:16:30.770779
# Unit test for function object_to_dict
def test_object_to_dict():

    # Arrange
    class test_class:
        a = "a"
        b = "b"
        c = "c"

    # Act
    returned_dict = object_to_dict(test_class)

    # Assert
    assert isinstance(returned_dict, dict)
    assert len(returned_dict.keys()) == 3
    assert "a" in returned_dict
    assert "b" in returned_dict
    assert "c" in returned_dict
    assert returned_dict["a"] == "a"
    assert returned_dict["b"] == "b"
    assert returned_dict["c"] == "c"



# Generated at 2022-06-13 16:16:35.803342
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.z = 1

    tc = TestClass(1, 2)
    assert object_to_dict(tc) == {'x': 1, 'y': 2, 'z': 1}
    assert object_to_dict(tc, exclude=['y', 'z']) == {'x': 1}



# Generated at 2022-06-13 16:18:13.642340
# Unit test for function deduplicate_list
def test_deduplicate_list():
    input = [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9, 10]
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert deduplicate_list(input) == result

# Generated at 2022-06-13 16:18:15.926231
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(list("abbababa")) == list("ab")



# Generated at 2022-06-13 16:18:19.353327
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['ansible', 'ansible', 'ansible', 'ansible', 'tower', 'ansible', 'tower']
    assert deduplicate_list(original_list) == ['ansible', 'tower']
    original_list = ['ansible', 'tower', 'tower', 'ansible']
    assert deduplicate_list(original_list) == ['ansible', 'tower']



# Generated at 2022-06-13 16:18:23.905328
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,1,1,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]) == [1,2,3,4]

# Generated at 2022-06-13 16:18:29.923464
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_case = {
        "original_list": [2, 3, 1, 4, 2, 1],
        "expected": [2, 3, 1, 4]
    }
    assert(deduplicate_list(test_case["original_list"]) == test_case["expected"])


# Generated at 2022-06-13 16:18:31.939881
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]



# Generated at 2022-06-13 16:18:36.155353
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        test_key = 'test value'

    obj = TestObject()
    result = object_to_dict(obj)
    assert result['test_key'] == 'test value'

# Generated at 2022-06-13 16:18:40.362595
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 4, 5, 6, 3, 2]) == [1, 2, 3, 4, 5, 6]
    assert deduplicate_list([1, 2, 3, 4, 5, 6, 3, 2, 1, 2, 3, 4, 5, 6, 3, 2]) == [1, 2, 3, 4, 5, 6]



# Generated at 2022-06-13 16:18:51.679778
# Unit test for function object_to_dict
def test_object_to_dict():
    import infotests
    import infobackends

    assert object_to_dict(infotests.test_info_test_a) == {
        'name': 'test_info_test_a',
        'options': ['a', 'b', 'c', 'd'],
        'not_to_be_used': 'yes',
        'is_deprecated': False,
        'deprecated_option': 'c',
        'doc': 'test_info_test_a doc string',
        'choices': None,
    }


# Generated at 2022-06-13 16:19:02.397088
# Unit test for function deduplicate_list
def test_deduplicate_list():
    print("Running tests on function deduplicate_list")
    assert deduplicate_list([]) == []
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1, 2, 1, 2, 1, 2]) == [1, 2]
    assert deduplicate_list([1, 2, 3, 2, 1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 1, 4, 2, 1, 3]) == [1, 2, 3, 4]
