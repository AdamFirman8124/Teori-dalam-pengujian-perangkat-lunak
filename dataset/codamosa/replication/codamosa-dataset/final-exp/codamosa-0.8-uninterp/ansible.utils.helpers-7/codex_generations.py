

# Generated at 2022-06-13 16:10:07.362196
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 100, min_value=0) == 50

    assert pct_to_int('50', 100, min_value=0) == 50

    assert pct_to_int(50, 100, min_value=0) == 50

    assert pct_to_int('1%', 100, min_value=0) == 1

    assert pct_to_int('0%', 100, min_value=0) == 1



# Generated at 2022-06-13 16:10:10.408850
# Unit test for function pct_to_int
def test_pct_to_int():
    min_value = 3
    value = '15%'
    num_items = 20
    assert pct_to_int(value, num_items, min_value) == min_value

# Generated at 2022-06-13 16:10:14.034700
# Unit test for function deduplicate_list
def test_deduplicate_list():
    duplicated_list = [1, 2, 3, 2, 1, 2]
    result = deduplicate_list(duplicated_list)
    assert result == [1, 2, 3]



# Generated at 2022-06-13 16:10:20.049215
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('1%', 100) == 1
    assert pct_to_int('1%', 1000) == 10
    assert pct_to_int('50%', 1000) == 500
    assert pct_to_int('.5%', 1000) == 5
    assert pct_to_int('50', 1000) == 50
    assert pct_to_int(50, 1000) == 50


# Generated at 2022-06-13 16:10:29.170941
# Unit test for function pct_to_int
def test_pct_to_int():
    if pct_to_int(10, 100) != 10:
        raise Exception("pct_to_int test 1 failed")
    if pct_to_int(10, 100, min_value=5) != 10:
        raise Exception("pct_to_int test 2 failed")
    if pct_to_int('10%', 100) != 10:
        raise Exception("pct_to_int test 3 failed")
    if pct_to_int('10%', 100, min_value=5) != 10:
        raise Exception("pct_to_int test 4 failed")
    if pct_to_int('1%', 100, min_value=5) != 5:
        raise Exception("pct_to_int test 5 failed")

# Generated at 2022-06-13 16:10:32.964147
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(50, 100) == 50
    assert pct_to_int('25%', 100) == 25
    assert pct_to_int('25.1%', 100) == 25
    assert pct_to_int('25.5%', 100) == 26



# Generated at 2022-06-13 16:10:40.023893
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('20%', 20) == 4
    assert pct_to_int('20%', 20, min_value=2) == 4
    assert pct_to_int('10%', 20, min_value=2) == 2
    assert isinstance(pct_to_int('20%', 20), int)
    assert pct_to_int('20', 20) == 20
    assert pct_to_int(20, 20) == 20



# Generated at 2022-06-13 16:10:46.127500
# Unit test for function pct_to_int
def test_pct_to_int():
    # Testing 100%
    assert pct_to_int('100%', 10) == 10
    # Testing 50%
    assert pct_to_int('50%', 10) == 5
    # Testing 33%
    assert pct_to_int('33%', 10) == 3
    # Testing 10%
    assert pct_to_int('10%', 10) == 1

    # Testing without %
    assert pct_to_int('5', 10) == 5
    # Testing without % and minimum 1
    assert pct_to_int('0', 10, 1) == 1

# Generated at 2022-06-13 16:10:49.631244
# Unit test for function object_to_dict
def test_object_to_dict():

    class test:
        f = 5
        g = 'foo'
        exclude = [f]

    t = test()
    result = object_to_dict(t, exclude=[t.f])
    assert len(result) == 2
    assert result['g'] == 'foo'
    assert 'f' not in list(result.keys())


# Generated at 2022-06-13 16:10:53.173175
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('10%', 100, 1) == 10
    assert pct_to_int('10', 100, 1) == 10
    assert pct_to_int(10, 100, 1) == 10

# Generated at 2022-06-13 16:11:02.884170
# Unit test for function deduplicate_list
def test_deduplicate_list():

    class TestDeduplicateList(object):

        def test_deduplicate_item_not_in_list(self):
            original_list = [1, 2, 3, 4]
            assert deduplicate_list(original_list) == original_list

        def test_deduplicate_item_in_list_once(self):
            original_list = [1, 2, 1, 3, 4]
            assert deduplicate_list(original_list) == [1, 2, 3, 4]

        def test_deduplicate_item_in_list_twice(self):
            original_list = [1, 2, 1, 3, 1, 4]
            assert deduplicate_list(original_list) == [1, 2, 3, 4]


# Generated at 2022-06-13 16:11:06.156533
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list
    """
    data = ['a', 'b', 'c', 'z', 'a', 'c', 'b']
    assert deduplicate_list(data) == ['a', 'b', 'c', 'z']

# Generated at 2022-06-13 16:11:09.444759
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]) == [3,2,1]

# Generated at 2022-06-13 16:11:13.871800
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 4, 5, 2, 6]
    expected_result = [1, 2, 3, 4, 5, 6]
    assert deduplicate_list(original_list) == expected_result
    original_list = ['1', '2', '3', '4', '5', '2', '6']
    expected_result = ['1', '2', '3', '4', '5', '6']
    assert deduplicate_list(original_list) == expected_result

# Generated at 2022-06-13 16:11:16.661585
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 4, 5, 5, 4, 3, 2]) == [1, 2, 3, 4, 5]

### TODO: Remove following function when all list operations are idempotent


# Generated at 2022-06-13 16:11:23.025344
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit tests for function deduplicate_list.
    """
    from collections import OrderedDict
    expected_ordered_dict = OrderedDict([(0, 'a'), (1, 'b'), (2, 'c')])
    original_list = ['a', 'b', 'b', 'a', 'c']
    assert(deduplicate_list(original_list) == expected_ordered_dict.values())


# Generated at 2022-06-13 16:11:26.693811
# Unit test for function deduplicate_list
def test_deduplicate_list():
    my_list = [1, 2, 3, 3, 3, 2, 2, 2, 4, 4, 4, 5, 5, 2]
    expected = [1, 2, 3, 4, 5]
    assert deduplicate_list(my_list) == expected


# Generated at 2022-06-13 16:11:30.902724
# Unit test for function object_to_dict
def test_object_to_dict():
    class T(object):
        a = 1
        b = 2

    o = T()
    assert object_to_dict(o) == {'a': 1, 'b': 2}



# Generated at 2022-06-13 16:11:39.886261
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list
    """
    assert deduplicate_list([1,2,1,1,2,2,2,2,3,3,3,3,3,]) == [1,2,3]
    assert deduplicate_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,14,14,14]) == [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


# Generated at 2022-06-13 16:11:48.080666
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        def __init__(self, object_var1, object_var2):
            self.object_var1 = object_var1
            self.object_var2 = object_var2

    test_object = TestObject('test', 'test2')
    test_dict = object_to_dict(test_object)
    assert test_object.object_var1 == test_dict['object_var1']
    assert test_object.object_var2 == test_dict['object_var2']
    assert test_object.object_var1 != test_dict['object_var2']


# Generated at 2022-06-13 16:11:56.538091
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'a', 'c', 'b', 'd', 'f', 'e']
    new_list = ['a', 'b', 'c', 'd', 'f', 'e']
    assert deduplicate_list(original_list) == new_list

# Generated at 2022-06-13 16:12:05.795669
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 2, 1, 3, 1, 2, 4, 3]) == [1, 2, 3, 4]
    assert deduplicate_list([]) == []
    assert deduplicate_list(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'a', 'a', 'a', 'a', 'a']) == ['a']
    assert deduplicate_list(['a', 'b', 'a', 'a', 'a', 'a']) == ['a', 'b']
    assert deduplicate_list(['a', 'c', 'a', 'a', 'a', 'a']) == ['a', 'c']

# Generated at 2022-06-13 16:12:11.222312
# Unit test for function object_to_dict
def test_object_to_dict():
    class MockObj:
        def __init__(self, key1, key2, key3):
            self.key1 = key1
            self.key2 = key2
            self.key3 = key3

    result = object_to_dict(MockObj('a', 'b', 'c'))
    assert result['key1'] == 'a'
    assert result['key2'] == 'b'
    assert result['key3'] == 'c'

# Generated at 2022-06-13 16:12:15.461728
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,2,2,2]) == [1,2,3,4]

# Generated at 2022-06-13 16:12:20.012168
# Unit test for function object_to_dict
def test_object_to_dict():
    class MockObject(object):
        property1 = "value1"
        _property2 = "value2"

    mock_obj = MockObject()
    output = object_to_dict(mock_obj)
    assert len(output) == 1
    assert output['property1'] == "value1"

    output = object_to_dict(mock_obj, exclude=['property1'])
    assert len(output) == 0



# Generated at 2022-06-13 16:12:26.005829
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        def __init__(self, thing1, thing2, thing3):
            self.thing1 = thing1
            self.thing2 = thing2
            self.thing3 = thing3

    tobj = TestObject('foo', 'bar', 'baz')
    tdict = object_to_dict(tobj, exclude=['thing1'])

    assert tdict['thing1'] == 'foo'
    assert tdict['thing2'] == 'bar'
    assert tdict['thing3'] == 'baz'

# Generated at 2022-06-13 16:12:31.754578
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1, 3, 2]) == [1, 2, 3]
    assert deduplicate_list(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:12:39.470586
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 4, 5, 5, 3, 3, 3, 3, 3, 6]) == [1, 2, 3, 4, 5, 6]
    assert deduplicate_list([1, 2, 3, 1, 4, 5, 5, 3, 3, 3, 3, 3, 6, 5]) == [1, 2, 3, 4, 5, 6]
    assert deduplicate_list([1, 2, 3, 1, 4, 5, 5, 3, 3, 3, 3, 3, 6, 5, 5, 5, 5, 5]) == [1, 2, 3, 4, 5, 6]
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:12:47.325268
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 4, 1, 2, 2]) == [1, 2, 3, 4]
    assert deduplicate_list(['a', 'b', 'a', 'b']) == ['a', 'b']
    assert deduplicate_list(['a', 'b', 'a', 'b', 'b']) == ['a', 'b']
    assert deduplicate_list([1, 2, 'a', 'b', 'b']) == [1, 2, 'a', 'b']

# Generated at 2022-06-13 16:12:52.344561
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 3, 4, 5, 5, 6]
    expected_list = [1, 2, 3, 4, 5, 6]
    actual_list = deduplicate_list(original_list)
    assert actual_list == expected_list, 'Failed to deduplicate list: %s' % actual_list

# Generated at 2022-06-13 16:13:05.695898
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'a', 'd', 'a']) == ['a', 'b', 'd']
    assert deduplicate_list(['b', 'a', 'a', 'd', 'a']) == ['b', 'a', 'd']
    assert deduplicate_list(['d', 'a', 'a', 'd', 'a']) == ['d', 'a']
    assert deduplicate_list(['d', 'a', 'a', 'a', 'a']) == ['d', 'a']
    assert deduplicate_list(['d']) == ['d']

# Generated at 2022-06-13 16:13:12.102971
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a','b','a','c','f','g','c','a','h','i','g','b','a','b','c','a','i','g','c','f','a','b','g','c','a']
    deduped_list = ['a','b','c','f','g','h','i']
    assert deduplicate_list(original_list) == deduped_list

# Generated at 2022-06-13 16:13:16.366398
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['foo', 'bar', 'bar', 'baz', 'foo', 'foo', 'bar', 'baz']
    deduplicated_list = ['foo', 'bar', 'baz']
    assert deduplicated_list == deduplicate_list(original_list)


# Generated at 2022-06-13 16:13:20.988339
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list.
    """
    assert deduplicate_list(['b', 'c', 'c', 'a', 'd', 'd', 'a']) == ['b', 'c', 'a', 'd']



# Generated at 2022-06-13 16:13:29.397656
# Unit test for function object_to_dict
def test_object_to_dict():

    class Test(object):

        def __init__(self):
            self.prop_1 = 'value_1'
            self._prop_2 = 'value_2'
            self.prop_3 = 'value_3'
            self.prop_4 = 'value_4'

    test_obj = Test()
    test_obj_dict = object_to_dict(test_obj, ['_prop_2'])
    assert test_obj_dict['prop_1'] == 'value_1'
    assert test_obj_dict['prop_3'] == 'value_3'
    assert test_obj_dict['prop_4'] == 'value_4'
    assert '_prop_2' not in test_obj_dict


# Generated at 2022-06-13 16:13:37.667568
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        def __init__(self):
            self.one = "one"
            self.two = "two"
            self._three = "three"
            self._four = "four"

    test_obj = TestObject()
    obj_dict = object_to_dict(test_obj, ["_three"])
    assert obj_dict["one"] == "one"
    assert obj_dict["two"] == "two"
    assert "_three" not in obj_dict.keys()
    assert "_four" not in obj_dict.keys()
    assert "one" in obj_dict.keys()
    assert "two" in obj_dict.keys()

# Generated at 2022-06-13 16:13:48.479803
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.one = 1
            self.two = 2
            self._three = 3
            self._four = 4
            self.five = 5
    test_obj = TestClass()
    assert object_to_dict(test_obj) == dict(one=1, two=2, five=5)
    assert object_to_dict(test_obj, ['two', '_four']) == dict(one=1, _three=3, five=5)
    assert object_to_dict(test_obj, ['five']) == dict(one=1, two=2, _three=3, _four=4)

# Generated at 2022-06-13 16:13:52.141814
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 2, 4, 5, 6, 1, 2, 3]) == [1, 2, 3, 4, 5, 6]


# Generated at 2022-06-13 16:13:59.703018
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.test_1 = '1'
            self.test_2 = '2'
            self.test_3 = '3'
            self._test_4 = '4'
        def __repr__(self):
            return 'test'
        def test(self):
            return 'test'

    obj1 = Test()
    result = {'test_1': '1', 'test_2': '2', 'test_3': '3'}
    assert object_to_dict(obj1) == result
    obj2 = Test()
    result = {'test_1': '1', 'test_2': '2', 'test_3': '3', '_test_4': '4'}

# Generated at 2022-06-13 16:14:06.040792
# Unit test for function object_to_dict
def test_object_to_dict():
    class A:
        def __init__(self):
            self.__a = 1
            self.b = 2
            self.c = 3

    a = A()
    assert object_to_dict(a) == {'b': 2, 'c': 3}
    assert object_to_dict(a, exclude=['b']) == {'c': 3}


# Generated at 2022-06-13 16:14:16.769970
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'b', 'a', 'd']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list([]) == []
    assert deduplicate_list(['a', 'b', 'c', 'b', 'a', 'd']) != ['a', 'b', 'c']
test_deduplicate_list()

# Generated at 2022-06-13 16:14:20.765142
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1, 3]) == [1, 2, 3]
    assert deduplicate_list([5, 3, 1, 4, 3, 1, 3, 3]) == [5, 3, 1, 4]
    assert deduplicate_list([1, 1, 1, 1, 1, 1, 1, 1]) == [1]
    assert deduplicate_list([1]) == [1]



# Generated at 2022-06-13 16:14:28.220372
# Unit test for function object_to_dict
def test_object_to_dict():
    test_class = type('test_class', (), dict(a=1, b=2, c=3))
    test_obj = test_class()
    result = object_to_dict(test_obj)
    assert len(result) == 3
    assert result['a'] == 1
    assert result['b'] == 2
    assert result['c'] == 3
    result = object_to_dict(test_obj, exclude=['a', 'b'])
    assert len(result) == 1
    assert result['c'] == 3


# Generated at 2022-06-13 16:14:32.096938
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 1, 2, 3, 3, 3, 4, 4, 1]
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == [1, 2, 3, 4, 1]



# Generated at 2022-06-13 16:14:33.627811
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,2,3]) == [1,2,3]
    assert deduplicate_list([0,1,2,3]) == [0,1,2,3]


# Generated at 2022-06-13 16:14:36.189370
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['abc', 'abc', 'def']
    assert deduplicate_list(test_list) == ['abc', 'def']



# Generated at 2022-06-13 16:14:43.204561
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Function used to unit test deduplicate_list()
    """
    original_list = ['c','a','b','a','c','e','f','g','e','f','g','e','f','g','e','g','e','g','e','f','g','e']
    deduplicated_list = ['c','a','b','e','f','g']
    assert deduplicate_list(original_list) == deduplicated_list


# Generated at 2022-06-13 16:14:51.975821
# Unit test for function object_to_dict
def test_object_to_dict():
    class ClassTest(object):
        """Class to test the object_to_dict function."""
        excluded_property = "will be excluded"
        test_properties = ['foo', 'bar', 'baz']

        def __init__(self):
            for prop in self.test_properties:
                setattr(self, prop, prop)

    assert object_to_dict(ClassTest(), exclude=['excluded_property']) == {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}



# Generated at 2022-06-13 16:14:55.970851
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3, 4]) == [1, 2, 3, 4]
    assert deduplicate_list([1, 1, 2, '1', '1', 2, 3, 4]) == [1, '1', 2, 3, 4]

# Generated at 2022-06-13 16:15:00.795368
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self, test_val):
            self.test_val = test_val
            self.test_hidden = 'hidden'

    my_obj = TestClass('test_value')
    test_dict = object_to_dict(my_obj)
    assert test_dict['test_val'] == 'test_value'
    assert 'test_hidden' not in test_dict

# Generated at 2022-06-13 16:15:13.975987
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['foo', 'bar', 'baz', 'foo']
    assert ['foo', 'bar', 'baz'] == deduplicate_list(original_list)



# Generated at 2022-06-13 16:15:17.420850
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyObject:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    obj = MyObject(1,2,3)

    assert object_to_dict(obj) == {'x': 1, 'y': 2, 'z': 3}


# Generated at 2022-06-13 16:15:23.703777
# Unit test for function object_to_dict
def test_object_to_dict():
    class sample_obj:
            def __init__(self, obj1, obj2=None):
                self.obj1 = obj1
                self.obj2 = obj2

    expected = {'obj1': 'value1', 'obj2': 'value2'}
    actual = object_to_dict(sample_obj('value1', 'value2'))
    assert expected == actual



# Generated at 2022-06-13 16:15:29.069595
# Unit test for function object_to_dict
def test_object_to_dict():
    class testclass:
        foo = None
        bar = None
        baz = None

    test_obj = testclass()
    test_obj.foo = "foovalue"
    test_obj.bar = "barvalue"
    test_obj.baz = "bazvalue"

    test_dict = object_to_dict(test_obj, exclude=['baz'])
    assert test_dict == {"foo": "foovalue", "bar": "barvalue"}

# Generated at 2022-06-13 16:15:34.532396
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'c', 'a', 'd', 'e', 'f', 'e', 'c', 'a', 'b']
    expected_list = ['a', 'b', 'c', 'd', 'e', 'f']

    deduplicated_list = deduplicate_list(original_list)

    assert deduplicated_list == expected_list

# Generated at 2022-06-13 16:15:36.947157
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['hello', 'world', 'world', 'this', 'is', 'a', 'test', 'hello', 'world']) == ['hello', 'world', 'this', 'is', 'a', 'test']

# Generated at 2022-06-13 16:15:39.372044
# Unit test for function deduplicate_list
def test_deduplicate_list():
    my_list = ['a', 'b', 'c', 'b', 'a', 'c', 'a']
    assert deduplicate_list(my_list) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:15:43.853845
# Unit test for function deduplicate_list
def test_deduplicate_list():
    my_list = ['a','b','c','c','d','a','e','f']
    my_list = deduplicate_list(my_list)
    assert my_list == ['a','b','c','d','e','f']


# Generated at 2022-06-13 16:15:48.757311
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Runs a unit test to determine if object_to_dict can handle simple objects
    """
    class Test:
        def __init__(self):
            self.a = 1
            self.b = 2

    obj = Test()
    result = object_to_dict(obj)
    assert result['a'] == 1
    assert result['b'] == 2

# Generated at 2022-06-13 16:15:53.442099
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['red', 'red', 'green', 'blue', 'green', 'red']
    deduplicated_list = ['red', 'green', 'blue']
    assert deduplicate_list(original_list) == deduplicated_list


# Generated at 2022-06-13 16:16:22.795047
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
    expected_result = ['a', 'b', 'c']
    result = deduplicate_list(original_list)
    assert result == expected_result, "Function deduplicate_list did not work as expected. "
    assert len(result) == len(expected_result), "Function deduplicate_list did not work as expected. "


# Generated at 2022-06-13 16:16:29.056061
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo(object):
        def __init__(self):
            self.one = 1
            self.two = 2
            self._three = 3
            self._four = 4

    obj = Foo()
    expected_result = {'one': 1, 'two': 2}
    result = object_to_dict(obj)
    assert result == expected_result, 'Dict conversion of objects failed, actual: {0}, expected: {1}'.format(result, expected_result)



# Generated at 2022-06-13 16:16:37.806027
# Unit test for function deduplicate_list
def test_deduplicate_list():

    my_list = ["a", "b", "c", "b", "a"]
    my_expected = ["a", "b", "c"]

    if my_expected != deduplicate_list(my_list):
        assert False, "Expected "+str(my_expected)+" did not equal "+str(deduplicate_list(my_list))

    my_list = []
    my_expected = []

    if my_expected != deduplicate_list(my_list):
        assert False, "Expected "+str(my_expected)+" did not equal "+str(deduplicate_list(my_list))
    
    my_list = ["a", "b", "c", "b", "a"]
    my_expected = ["a", "b", "c"]

# Generated at 2022-06-13 16:16:42.319293
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Simple test for function deduplicate_list
    """
    dedup_list = deduplicate_list([1,2,2,2,2,9,9,9,9,9,9,'a',1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,'a',1,2,3])
    assert dedup_list == [1,2,9,'a',3]

# Generated at 2022-06-13 16:16:46.176266
# Unit test for function object_to_dict
def test_object_to_dict():
    class Cell(object):
        def __init__(self,name=None, power=None):
            self.name = name
            self.power = power

    item = Cell(name='ewan', power='12')

    assert object_to_dict(item) == {'name': 'ewan', 'power': '12'}


# Generated at 2022-06-13 16:16:52.770900
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list
    """
    original_list_1 = [1, 2, 3]
    deduplicated_list_1 = deduplicate_list(original_list_1)
    original_list_2 = [2, 3, 1, 1, 2]
    deduplicated_list_2 = deduplicate_list(original_list_2)
    assert deduplicated_list_1 == [1, 2, 3]
    assert deduplicated_list_2 == [2, 3, 1]


# Generated at 2022-06-13 16:17:00.628360
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2]) == [1, 2]
    assert deduplicate_list([1, 2, 1]) == [1, 2]
    assert deduplicate_list([1, 2, 2, 1]) == [1, 2]
    assert deduplicate_list([1, 2, 2, 1, 2, 1]) == [1, 2]
    assert deduplicate_list([1, 2, 2, 1, 2, 1, 2]) == [1, 2]


# Generated at 2022-06-13 16:17:04.832594
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['1', '2', '3', '3', '3', '2', '1', '1', '1', '2', '2', '2', '1', '2', '2', '2']) == ['1', '2', '3']

# Generated at 2022-06-13 16:17:10.687440
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject():
        some_value1 = 'some_value1'
        some_value2 = 'some_value2'
        some_value3 = 'some_value3'

    to = TestObject()
    ret = object_to_dict(to)
    assert ret["some_value1"] == 'some_value1'
    assert ret["some_value2"] == 'some_value2'
    assert ret["some_value3"] == 'some_value3'


# Generated at 2022-06-13 16:17:15.805007
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 1, 1, 5]) == [1, 2, 3, 5]
    assert deduplicate_list([]) == []
    assert deduplicate_list(None) == None


# Generated at 2022-06-13 16:18:02.771434
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 5, 2, 6, 2, 5, 1]
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == [1, 5, 2, 6]

# Generated at 2022-06-13 16:18:06.145384
# Unit test for function deduplicate_list
def test_deduplicate_list():
    alist = ['foo', 'bar', 'baz', 'foo', 'bar', 'foo']
    correct_return = ['foo', 'bar', 'baz']
    assert deduplicate_list(alist) == correct_return



# Generated at 2022-06-13 16:18:13.736552
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1, 2, 3, 2, 4, 1, 5, 6, 5]) == [1, 2, 3, 4, 5, 6]
    assert deduplicate_list(['a', 'b', 'c', 'c', 'a']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:18:17.318653
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list = [1,2,3,3,4,4,4,5]
    deduplicate = deduplicate_list(list)
    assert deduplicate == [1,2,3,4,5]

# Generated at 2022-06-13 16:18:21.585350
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 0, 1, 1, 0, 1]
    expected_list = [1, 0]

    assert deduplicate_list(original_list) == expected_list


# Generated at 2022-06-13 16:18:28.430706
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,6,6,6,6]
    testing_list = deduplicate_list(original_list)

    assert set(testing_list) == set([1,2,3,4,5,6])

# Generated at 2022-06-13 16:18:31.149445
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['foo', 'bar', 'bar', 'baz', 'foo']) == ['foo', 'bar', 'baz', 'foo']


# Generated at 2022-06-13 16:18:40.905877
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'b', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'c', 'b', 'b']) == ['a', 'b', 'c']
    assert deduplicate_list(['c', 'b', 'b', 'b', 'a']) == ['c', 'b', 'a']
    assert deduplicate_list(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:18:46.999226
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_with_duplicates = ['host1', 'host1', 'host1', 'host2', 'host2']
    deduplicated_list = ['host1', 'host2']
    assert deduplicate_list(list_with_duplicates) == deduplicated_list

# Generated at 2022-06-13 16:18:52.405185
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 3, 3, 3, 2, 5, 1, 3, 4, 5, 6]) == [1, 3, 2, 5, 4, 6]
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([]) == []