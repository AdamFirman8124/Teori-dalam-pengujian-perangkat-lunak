

# Generated at 2022-06-13 16:10:15.465089
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(50, 10) == 5
    assert pct_to_int(25.0, 8, min_value=3) == 2
    assert pct_to_int(50.0, 2) == 1
    assert pct_to_int(75.5, 4) == 3
    assert pct_to_int(99.999, 100) == 100
    assert pct_to_int(100, 1) == 1
    assert pct_to_int(50, 0) == 1
    assert pct_to_int(0, 50) == 1
    assert pct_to_int('50%', 10) == 5
    assert pct_to_int('0.5%', 10) == 0
    assert pct_to_int('100%', 10) == 10
    assert pct

# Generated at 2022-06-13 16:10:16.867112
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 2, 4, 2, 1]
    assert deduplicate_list(test_list) == [1, 2, 3, 4]



# Generated at 2022-06-13 16:10:20.378799
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('30%', 30) == 9
    assert pct_to_int(50, 30) == 50
    assert pct_to_int('30%', 30, 3) == 3
    assert pct_to_int(50, 30, 3) == 50

# Generated at 2022-06-13 16:10:26.888159
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int("100%", 10) == 10
    assert pct_to_int("50%", 10) == 5
    assert pct_to_int("10%", 10) == 1
    assert pct_to_int("5", 10) == 5
    assert pct_to_int("5%", 0) == 0
    assert pct_to_int("0%", 10) == 1
    assert pct_to_int("1%", 10) == 1


# Generated at 2022-06-13 16:10:29.414701
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int(50, 100) == 50

# Generated at 2022-06-13 16:10:34.056290
# Unit test for function object_to_dict
def test_object_to_dict():

    class MyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    my_obj = MyClass('a', 'b')
    expect = {'a': 'a', 'b': 'b'}
    actual = object_to_dict(my_obj)
    assert expect == actual, 'Got unexpected dict, got: %s' % actual

# Generated at 2022-06-13 16:10:38.290202
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(10, 50) == 10
    assert pct_to_int('10%', 50) == 5
    assert pct_to_int('100%', 50) == 50
    assert pct_to_int('0%', 50) == 1

# Generated at 2022-06-13 16:10:41.211053
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('10%', 500) == 50
    assert pct_to_int(10, 500) == 10
    assert pct_to_int('10%', 0) == 1


# Generated at 2022-06-13 16:10:47.549470
# Unit test for function pct_to_int
def test_pct_to_int():
    assert(pct_to_int('10%', 100) == 10)
    assert(pct_to_int('50%', 100) == 50)
    assert(pct_to_int('10%', 1) == 1)
    assert(pct_to_int('20%', 1) == 1)
    assert(pct_to_int('100%', 1) == 1)
    assert(pct_to_int('110%', 1) == 1)
    assert(pct_to_int('2', 3) == 2)
    assert(pct_to_int('10', 3) == 10)

# Generated at 2022-06-13 16:10:54.516323
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(1,10) == 1
    assert pct_to_int('1',10) == 1
    assert pct_to_int('5%',10) == 1
    assert pct_to_int('50%',10) == 5
    assert pct_to_int('100%',10) == 10
    assert pct_to_int('150%',10) == 10


# Generated at 2022-06-13 16:11:02.668741
# Unit test for function object_to_dict
def test_object_to_dict():
    # Define a class to use for testing
    class test_obj(object):
        a = "a"
        b = "b"

    test_a = test_obj()

    assert object_to_dict(test_a) == dict(a="a", b="b")



# Generated at 2022-06-13 16:11:10.673983
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert [] == deduplicate_list([])
    assert [1] == deduplicate_list([1])
    assert [1, 2] == deduplicate_list([1, 2])
    assert [1, 2] == deduplicate_list([1, 1, 2])
    assert [1, 2] == deduplicate_list([1, 2, 1])
    assert [1, 2] == deduplicate_list([1, 2, 1, 1])
    assert [1, 2, 3] == deduplicate_list([1, 2, 3])
    assert [1, 2, 3] == deduplicate_list([1, 2, 3, 1, 2, 3])

# Generated at 2022-06-13 16:11:15.066771
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,1,2,3,3,3,4,3,2,2,2,2,2,2,2,1,1,1]) == [1,2,3,4,3,2,1,1]
    assert deduplicate_list(['A', 'A', 'B', 'A', 'A', 'A', 'A', 'B']) == list(set(['A', 'B']))
    assert deduplicate_list(['A', 'A', 'B', 'A', 'A', 'A', 'A', 'B']) == ['A', 'B', 'A', 'B']

# Generated at 2022-06-13 16:11:20.048331
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Test object_to_dict function
    :return:
    """
    class TestClass:
        def __init__(self):
            self.b = 'foo'
            self.c = 'bar'
            self.d = 'foobar'

    obj = TestClass()
    assert object_to_dict(obj) == {'b': 'foo', 'c': 'bar', 'd': 'foobar'}
    assert object_to_dict(obj, exclude=['b']) == {'c': 'bar', 'd': 'foobar'}



# Generated at 2022-06-13 16:11:24.195132
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert [1,2,3,4] == deduplicate_list([1,2,2,3,3,1,1,2,2,3,3,1,1,2,2,3,3,4])
    assert [] == deduplicate_list([])

# Generated at 2022-06-13 16:11:36.824370
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    This test ensures that the
    :param self:
    :return:
    """
    class TestClass:
        def __init__(self):
            self.name = 'Tom'
            self.age = 35
            self.address = '1 Main St'
            self.phone = '5555555555'

        def __repr__(self):
            return self.name

    my_test_object = TestClass()
    my_test_dict = object_to_dict(my_test_object, exclude=['phone'])
    assert my_test_dict == {'address': '1 Main St', 'age': 35, 'name': 'Tom'}, "The created dictionary is missing" \
                                                                               "values."

# Generated at 2022-06-13 16:11:44.969772
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass1(object):
        def __init__(self):
            self.prop1 = "property1"
            self.prop2 = "property2"
    class TestClass2(object):
        def __init__(self):
            self.attr1 = "attribute1"
            self.attr2 = "attribute2"
            self.obj = TestClass1()
    obj = TestClass2()
    obj_dict = object_to_dict(obj)
    assert obj_dict['attr1'] == 'attribute1'
    assert obj_dict['attr2'] == 'attribute2'
    assert isinstance(obj_dict['obj'], dict)
    assert obj_dict['obj']['prop1'] == 'property1'
    assert obj_dict['obj']['prop2'] == 'property2'

# Generated at 2022-06-13 16:11:53.148881
# Unit test for function object_to_dict
def test_object_to_dict():
    class FakeDict(object):
        def __init__(self):
            self.exclude = ['fake_1']
            self.fake_1 = False
            self.fake_2 = True
            self.fake_3 = 'string'
            self.fake_4 = 1

    fd = FakeDict()

    assert object_to_dict(fd) == {'fake_2': True, 'fake_4': 1, 'fake_3': 'string'}
    assert object_to_dict(fd, ['fake_2', 'fake_3']) == {'fake_4': 1}
    assert object_to_dict(fd, 'not_a_list') == {'fake_2': True, 'fake_4': 1, 'fake_3': 'string'}

# Generated at 2022-06-13 16:11:57.161177
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Setup a test list
    test_list = [1, 2, 3, 4, 5, 1, 2, 3]

    # Call the function and check the results
    assert deduplicate_list(test_list) == [1, 2, 3, 4, 5]



# Generated at 2022-06-13 16:12:06.831010
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # test no duplicates
    list = [1,2,3,4]
    assert list == deduplicate_list(list)

    # test duplicates
    assert [1,2,3,4] == deduplicate_list([1,2,3,4,3,2])

    # test duplicates with order
    assert [1,2,3,4,3,2] == deduplicate_list([1,2,3,4,3,2])

    # test duplicates with mixed order

# Generated at 2022-06-13 16:12:24.937129
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 3, 3, 5, 5, 5]) == [1, 3, 5]
    assert deduplicate_list([1, 3, 3, 3, 5, 5, 5]) == [1, 3, 5]
    # Test for order being preserved
    assert deduplicate_list([3, 1, 2, 1, 2, 1]) == [3, 1, 2]
    assert deduplicate_list([1, 2, 3, 3, 4, 5, 6, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]

# Generated at 2022-06-13 16:12:37.255546
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Verify functionality when there is a duplicate and when there isn't a duplicate
    """
    dup_list = [1, 1, 2, 3]
    result = deduplicate_list(dup_list)

    if len(result) != 3:
        raise AssertionError("Expecting length of list to be 3, found {0}".format(len(result)))
    if not set([1,2,3]).issubset(result):
        raise AssertionError("Expecting a subset of [1, 2, 3], found {0}".format(str(result)))

    dup_list = [1, 2, 3]
    result = deduplicate_list(dup_list)


# Generated at 2022-06-13 16:12:46.995075
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Test dupes in list
    orig_list = ['a','b','c','d','a','b','c','d']
    deduplicated_list = deduplicate_list(orig_list)
    assert deduplicated_list == ['a','b','c','d']
    # Test no dupes in list
    orig_list = ['a','b','c','d']
    deduplicated_list = deduplicate_list(orig_list)
    assert deduplicated_list == ['a','b','c','d']
    # Test empty list
    orig_list = []
    deduplicated_list = deduplicate_list(orig_list)
    assert deduplicated_list == []
    # Test order in deduped list

# Generated at 2022-06-13 16:12:54.368849
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['foo', 'bar', 'bar', 'baz']) == ['foo', 'bar', 'baz']
    assert deduplicate_list(['bar', 'baz', 'foo']) == ['bar', 'baz', 'foo']
    assert deduplicate_list(['baz', 'foo', 'bar']) == ['baz', 'foo', 'bar']
    assert deduplicate_list(['baz', 'baz', 'foo']) == ['baz', 'foo']

# Generated at 2022-06-13 16:12:59.571433
# Unit test for function object_to_dict
def test_object_to_dict():

    class MyObject(object):
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
            self.d = 4

    obj = MyObject()
    assert object_to_dict(obj) == dict(a=1, b=2, c=3, d=4)

    assert object_to_dict(obj, exclude=['b']) == dict(a=1, c=3, d=4)



# Generated at 2022-06-13 16:13:01.969767
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['interface FastEthernet1', 'interface FastEthernet1', 'interface FastEthernet3']) \
        == ['interface FastEthernet1', 'interface FastEthernet3']



# Generated at 2022-06-13 16:13:09.142614
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_class:
        def __init__(self):
            self.name = 'foo'
            self.val = 42
            self._hidden = 'secret'

    tc = test_class()
    d = object_to_dict(tc)
    assert d['name'] == 'foo'
    assert d['val'] == 42
    assert d['_hidden'] == 'secret'



# Generated at 2022-06-13 16:13:13.260370
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo:
        def __init__(self):
            self.bar = "abc"
            self.baz = "def"

    f = Foo()
    assert object_to_dict(f) == {'bar': 'abc', 'baz': 'def'}



# Generated at 2022-06-13 16:13:15.323292
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'b']) == ['a', 'b', 'c']



# Generated at 2022-06-13 16:13:20.000367
# Unit test for function deduplicate_list
def test_deduplicate_list():
    sample_list = ['foo', 'bar', 'foo', 'bar', 'baz', 'foo', 'bar', 'baz']
    assert ['foo', 'bar', 'baz'] == deduplicate_list(sample_list)



# Generated at 2022-06-13 16:13:36.066649
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.field1 = 'test1'
            self.field2 = 'test2'
    test = Test()
    results = {'field1': 'test1', 'field2': 'test2'}
    assert object_to_dict(test) == results
    results = {'field1': 'test1', 'field2': 'test2', 'field3': 'test3'}
    assert object_to_dict(test, exclude=['field3']) == results

# Generated at 2022-06-13 16:13:42.919434
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-13 16:13:50.857102
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([5,5,5,2,2,2,2]) == [5,2]
    assert deduplicate_list([5,5,5,2,2,2,2]) != [5,5,5,2,2,2,2]
    assert deduplicate_list(['foo','bar','foo']) == ['foo','bar']
    assert deduplicate_list(['ab','ab','ab','cd','cd']) == ['ab','cd']

# Generated at 2022-06-13 16:13:57.129765
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_object(object):
        """
        test object for dict conversion
        """
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self.c = 'c'
    obj = test_object()
    assert object_to_dict(obj) == {'a': 'a', 'b': 'b', 'c': 'c'}
    assert object_to_dict(obj, ['a', 'c']) == {'b': 'b'}



# Generated at 2022-06-13 16:14:08.692121
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.test_attr1 = "attr1"
            self.test_attr2 = "attr2"
            self.test_attr3 = "attr3"
            self._private = "private"

    test_class = Test()
    test_dict = object_to_dict(test_class)
    assert test_dict['test_attr1'] == test_class.test_attr1
    assert test_dict['test_attr2'] == test_class.test_attr2
    assert test_dict['test_attr3'] == test_class.test_attr3
    assert '_private' not in test_dict
    assert 'test_' not in test_dict

    test_dict = object_to_dict(test_class, exclude=['test_attr1'])

# Generated at 2022-06-13 16:14:17.720805
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.a = None
            self.b = 1234
            self.c = ["test", "more_tests"]
            self.d = "some value"
            self.e = None
            self.f = 1234

    test_object = Test()
    obj_dict = object_to_dict(test_object)
    assert obj_dict['a'] is None
    assert obj_dict['b'] == 1234
    assert obj_dict['c'] == ['test', 'more_tests']
    assert obj_dict['d'] == 'some value'
    assert obj_dict['e'] is None
    assert obj_dict['f'] == 1234

    obj_dict = object_to_dict(test_object, exclude=['b', 'c'])

# Generated at 2022-06-13 16:14:23.840259
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        def __init__(self):
            self.test_property = "test_value"

    test_obj = TestClass()
    ans = {'test_property': 'test_value'}
    assert object_to_dict(test_obj) == ans
    assert object_to_dict(test_obj, ['test_property']) == {}
    assert object_to_dict(test_obj, []) == ans
    assert object_to_dict(test_obj, None) == ans

# Generated at 2022-06-13 16:14:34.354265
# Unit test for function object_to_dict
def test_object_to_dict():
    class ClassA(object):
        def __init__(self):
            self.param1 = 'param1_value'
            self.param2 = 'param2_value'
            self.param3 = 'param3_value'
        def __getitem__(self, key):
            return self.param1

    obj = ClassA()
    result = object_to_dict(obj)
    assert len(result) == 3
    assert result['param1'] == 'param1_value'
    assert result['param2'] == 'param2_value'
    assert result['param3'] == 'param3_value'
    result = object_to_dict(obj, ['param3'])
    assert len(result) == 2
    result = object_to_dict(obj, 'param3')
    assert len(result) == 2

# Generated at 2022-06-13 16:14:43.666539
# Unit test for function object_to_dict
def test_object_to_dict():

    class TestObject(object):
        def __init__(self):
            self.var1 = 'VAR1'
            self.__var2 = 'VAR2'
            self._var3 = 'VAR3'

    test_obj = TestObject()

    obj_dict = object_to_dict(test_obj, ['__var2', '_var3'])
    assert 'var1' in obj_dict.keys()
    assert obj_dict['var1'] == 'VAR1'
    assert '__var2' not in obj_dict.keys()
    assert '_var3' not in obj_dict.keys()

# Generated at 2022-06-13 16:14:47.623271
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 1, 2, 3, 4]) == [1, 2, 3, 4]

# Generated at 2022-06-13 16:15:11.157377
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'c', 'a', 'd', 'c', 'e', 'a']
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == ['a', 'b', 'c', 'd', 'e']

# Generated at 2022-06-13 16:15:18.691547
# Unit test for function object_to_dict
def test_object_to_dict():
    assert object_to_dict(DummyObj()) == {'a_property': 'one', 'b_property': 'two', 'c_property': 'three'}
    assert object_to_dict(DummyObj(), exclude=['b_property', 'c_property']) == {'a_property': 'one'}
    assert object_to_dict(DummyObj(), exclude=['a_property', 'c_property']) == {'b_property': 'two'}
    assert object_to_dict(DummyObj(), exclude=['a_property', 'b_property']) == {'c_property': 'three'}
    assert object_to_dict(DummyObj(), exclude=['c_property']) == {'a_property': 'one', 'b_property': 'two'}



# Generated at 2022-06-13 16:15:29.199769
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list1 = [1,3,3,3,3,3,3,1,1,1,1,1,3,3,3,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3]
    list2 = [1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    exp_list1 = [1,3]
    exp_list2 = [1,2]

    assert deduplicate_list(list1) == exp_list1
    assert deduplicate_list(list2) == exp_list2

# Generated at 2022-06-13 16:15:34.961734
# Unit test for function object_to_dict
def test_object_to_dict():
    class sample_class(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def count(self):
            return 2

    test_obj = sample_class(4, 5)
    result = object_to_dict(test_obj, ['count'])
    assert result.get('x') == 4
    assert result.get('y') == 5
    assert not result.get('count')

# Generated at 2022-06-13 16:15:40.029843
# Unit test for function object_to_dict
def test_object_to_dict():
    class ObjectToDictTest():
        def __init__(self):
            self.var1 = 'value1'
            self.var2 = 'value2'
            self.var3 = 'value3'
        def var4(self):
            pass

    test = ObjectToDictTest()
    obj = object_to_dict(test, exclude=['var4'])
    assert len(obj) == 3
    assert obj['var1'] == 'value1'



# Generated at 2022-06-13 16:15:44.645719
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_with_dupes = [1, 2, 3, 1, 4, 2]
    list_without_dupes = [1, 2, 3, 4]
    assert(deduplicate_list(list_with_dupes) == list_without_dupes)


# Generated at 2022-06-13 16:15:49.766812
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test:
        test1 = 'test1'
        test2 = 'test2'
        def __init__(self):
            self.test3 = 'test3'
    test_obj = Test()
    test_dict = object_to_dict(test_obj, exclude=['test3'])
    assert 'test1' in test_dict
    assert 'test2' in test_dict
    assert 'test3' not in test_dict

# Generated at 2022-06-13 16:15:53.964447
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_input_list = ['a', 'b', 'a', 'c', 'b']
    test_expected_output = ['a', 'b', 'c']
    assert deduplicate_list(test_input_list) == test_expected_output



# Generated at 2022-06-13 16:15:56.223498
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list = ["a", "b", "b", "c", "a", "b"]
    assert deduplicate_list(list) == ["a", "b", "c"]


# Generated at 2022-06-13 16:15:59.211369
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """ test deduplicate_list """
    result = deduplicate_list([1, 1, 2, 3, 3, 4, 5, 5, 6])
    assert result == [1, 2, 3, 4, 5, 6]



# Generated at 2022-06-13 16:16:41.331830
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 2, 4]) == [1, 2, 3, 4]



# Generated at 2022-06-13 16:16:45.326693
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.foo = 'bar'
            self._bar = 'foo'

    obj = Test()
    data = object_to_dict(obj, exclude=['foo'])
    assert data['_bar'] == 'foo'
    assert 'foo' not in data



# Generated at 2022-06-13 16:16:49.584434
# Unit test for function deduplicate_list
def test_deduplicate_list():
    input = [1, 2, 3, 2, 4, 2, 1]
    output = deduplicate_list(input)
    expected_output = [1, 2, 3, 4]
    assert output == expected_output


# Generated at 2022-06-13 16:16:55.566547
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 1, 4, 5, 1]
    assert deduplicate_list(test_list) == [1, 2, 3, 4, 5]
    assert deduplicate_list(test_list) != [1, 2, 3, 1, 4, 5, 1]

# Generated at 2022-06-13 16:17:03.596888
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Test deduplicate_list function
    """
    original_list = ["apple", "mango", "mango", "banana", "apple"]
    expected_result = ["apple", "mango", "banana"]
    assert deduplicate_list(original_list) == expected_result
    original_list = ["apple", "mango", "mango", "mango", "banana", "apple"]
    expected_result = ["apple", "mango", "banana"]
    assert deduplicate_list(original_list) == expected_result


# Generated at 2022-06-13 16:17:08.639621
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    o = TestObj('Bob', 23)
    result = object_to_dict(o, ['age'])
    assert result['name'] == 'Bob'
    assert 'age' not in result

# Generated at 2022-06-13 16:17:18.885798
# Unit test for function object_to_dict
def test_object_to_dict():
    class testClass(object):
        """
        Simple class for testing object_to_dict
        """
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self._c = 'c'
    class testSubClass(testClass):
        """
        Subclass for testing object_to_dict
        """
        def __init__(self):
            super(testSubClass, self).__init__()
            self.d = 'd'
            self._e = 'e'

    obj = testSubClass()
    assert object_to_dict(obj, exclude=['a', 'b']) == {'d': 'd'}

# Generated at 2022-06-13 16:17:23.571351
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Unit test for function object_to_dict
    """
    class test_class(object):
        """
        Dummy class
        """
        def __init__(self, some_attr='test'):
            self.some_attr = some_attr
    obj_test = test_class('test')
    obj_test_dict = object_to_dict(obj_test, exclude=['some_attr'])

# Generated at 2022-06-13 16:17:31.300385
# Unit test for function object_to_dict
def test_object_to_dict():
    class DummyClass():
        dummy_prop1 = 'dummy_prop1_value'
        dummy_prop2 = 'dummy_prop2_value'
        dummy_prop3 = 'dummy_prop3_value'

    obj = DummyClass()
    assert object_to_dict(obj) == {'dummy_prop1': 'dummy_prop1_value', 'dummy_prop2': 'dummy_prop2_value', 'dummy_prop3': 'dummy_prop3_value'}
    assert object_to_dict(obj, exclude=['dummy_prop1', 'dummy_prop2']) == {'dummy_prop3': 'dummy_prop3_value'}

# Generated at 2022-06-13 16:17:38.558849
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestingObject:
        def __init__(self):
            self.ansible = True
            self.testing = False

    test = TestingObject()

    test_dict = object_to_dict(test)

    assert type(test_dict) is dict
    assert 'ansible' in test_dict and test_dict['ansible'] is True
    assert 'testing' in test_dict and test_dict['testing'] is False
    assert '_' not in test_dict

    test_dict2 = object_to_dict(test, exclude=['ansible'])
    assert type(test_dict2) is dict
    assert 'ansible' not in test_dict2
    assert 'testing' in test_dict2 and test_dict2['testing'] is False
    assert '_' not in test_dict2

# Generated at 2022-06-13 16:19:11.148238
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyObj():
        my_obj_prop = 'my_obj_value'

    obj = MyObj()
    result = object_to_dict(obj)
    assert(isinstance(result, dict))
    assert(len(result.keys()) == 1)
    assert(result['my_obj_prop'] == 'my_obj_value')

# Generated at 2022-06-13 16:19:19.851219
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 3, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 1, 1, 2, 3, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 1, 1, 1, 1, 1]) == [1]
    assert deduplicate_list([1, 1, 1, 1, 1, 1, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]) == [1, 13]

# Generated at 2022-06-13 16:19:23.060566
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([5, 2, 4, 2, 0, 4]) == [5, 2, 4, 0]
    assert deduplicate_list(["a", "a", "b"]) == ["a", "b"]
    assert deduplicate_list([True, False, True]) == [True, False]


# Generated at 2022-06-13 16:19:33.238682
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_1 = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']
    list_2 = ['a']
    list_3 = ['a', 'b', 'c', 'd']
    list_4 = ['a', 'b', 'c', 'd', 'e', 'f', 'a']
    assert deduplicate_list(list_1) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(list_2) == ['a']
    assert deduplicate_list(list_3) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(list_4) == ['a', 'b', 'c', 'd', 'e', 'f']

# Generated at 2022-06-13 16:19:41.015624
# Unit test for function object_to_dict
def test_object_to_dict():

    class Object(object):
        """
        Dummy object with attributes
        """
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    # Simple object
    obj = Object()
    obj.first = 1
    obj.second = 2
    obj.third = 3
    result = object_to_dict(obj)
    assert_equal(len(result), 3)
    assert_true('first' in result)
    assert_true('second' in result)
    assert_true('third' in result)
    assert_equal(result['first'], obj.first)
    assert_equal(result['second'], obj.second)
    assert_equal(result['third'], obj.third)

    # Object with excluded attribute
   

# Generated at 2022-06-13 16:19:46.190251
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests the deduplicate_list function
    """
    assert deduplicate_list([]) == []
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1, 2, 3, 2]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 3, 2, 4, 3, 3, 5, 4, 4, 6, 5, 5]) == [1, 2, 3, 4, 5, 6]



# Generated at 2022-06-13 16:19:52.092903
# Unit test for function object_to_dict
def test_object_to_dict():
    class foo(object):
        def __init__(self):
            self.bob = 10
            self.jane = 5
    f = foo()
    f.bob = 'bar'
    res = object_to_dict(f)
    assert res['bob'] == 'bar'
    assert res['jane'] == 5
    res = object_to_dict(f, exclude=['jane'])
    assert res['bob'] == 'bar'
    assert 'jane' not in res



# Generated at 2022-06-13 16:19:58.961587
# Unit test for function deduplicate_list
def test_deduplicate_list():
    print("Testing deduplicate_list()")
    list = [2, 3, 4, 2, 3, 2]
    print("Testing the following list: \n%s" % list)
    assert deduplicate_list(list) == [2, 3, 4]
    print("The values in this list have been correctly deduplicated.")
    list2 = [2, 3, 4, 5, 6, 7]
    print("Testing the following list: \n%s" % list2)
    assert deduplicate_list(list2) == [2, 3, 4, 5, 6, 7]
    print("The values in this list have been correctly deduplicated.")
    print("All deduplicate_list() test cases passed.")


# Generated at 2022-06-13 16:20:03.820734
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from nose.tools import assert_list_equal
    inp = [1,1,1,2,2,2,3,5,5,5,5,5,5,5]
    out = [1,2,3,5]
    assert_list_equal(deduplicate_list(inp), out)