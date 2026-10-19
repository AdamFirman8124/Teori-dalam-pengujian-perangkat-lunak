

# Generated at 2022-06-13 16:10:13.642486
# Unit test for function pct_to_int
def test_pct_to_int():
    test_cases = {
        (100, 1): 100,
        (100, 1000): 10,
        (100.0, 1000): 10,
        (1, 1000): 1,
        (1, 1): 1,
        (50, 1000): 5,
        ('50%', 1000): 5,
        ('50%', 2): 1,
        ('50%', 1): 1,
        ('100%', 2): 2,
        ('100%', 1): 1,
        ('50', 1000): 50,
        ('50', 2): 50,
        ('50', 1): 50,
        ('100', 2): 100,
        ('100', 1): 100,
    }

    for test, result in test_cases.items():
        assert pct_to_int(*test) == result, 'failed for test case: {0}'.format

# Generated at 2022-06-13 16:10:17.952033
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(50, 10) == 5
    assert pct_to_int('10%', 1000) == 100
    assert pct_to_int(10, 1000) == 10
    assert pct_to_int('3%', 1000) == 30

# Generated at 2022-06-13 16:10:22.065550
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 2, 4, 5, 4]) == [1, 2, 3, 4, 5]

# Generated at 2022-06-13 16:10:29.723399
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('200%', 100) == 200
    assert pct_to_int('200%', 100, min_value=100) == 200
    assert pct_to_int('200%', 10) == 20
    assert pct_to_int('200%', 10, min_value=100) == 100
    assert pct_to_int('10%', 10) == 1
    assert pct_to_int('10%', 10, min_value=5) == 5
    assert pct_to_int('5%', 100) == 5
    assert pct_to_int('5%', 100, min_value=2) == 2

# Generated at 2022-06-13 16:10:34.276391
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 2, 1, 1, 3, 2, 4, 3, 3, 1, 5, 'a', 'a', 'a', 'b', 'c', 'c', 'a']
    sorted_list = [1, 2, 3, 4, 5, 'a', 'b', 'c']

    assert deduplicate_list(original_list) == sorted_list



# Generated at 2022-06-13 16:10:43.939953
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('5%', 10) == 1
    assert pct_to_int('15%', 10) == 2
    assert pct_to_int('25%', 10) == 3
    assert pct_to_int('35%', 10) == 4
    assert pct_to_int('45%', 10) == 5
    assert pct_to_int('55%', 10) == 6
    assert pct_to_int('65%', 10) == 7
    assert pct_to_int('75%', 10) == 8
    assert pct_to_int('85%', 10) == 9
    assert pct_to_int('95%', 10) == 10

    assert pct_to_int('0%', 10) == 1

# Generated at 2022-06-13 16:10:45.586941
# Unit test for function deduplicate_list
def test_deduplicate_list():
    input_list = ['a', 'b', 'a', 'c', 'a', 'b']
    result_list = deduplicate_list(input_list)
    assert(result_list == input_list)



# Generated at 2022-06-13 16:10:52.725167
# Unit test for function pct_to_int
def test_pct_to_int():
    assert(pct_to_int(20, 100) == 20)
    assert(pct_to_int('20%', 100) == 20)
    assert(pct_to_int('20%', 100, min_value=10) == 20)
    assert(pct_to_int('20.1%', 100, min_value=10) == 20)
    assert(pct_to_int('20.5%', 100, min_value=10) == 21)
    assert(pct_to_int('0%', 100, min_value=10) == 10)
    assert(pct_to_int('0.0%', 100, min_value=10) == 10)
    assert(pct_to_int('0.9%', 100, min_value=10) == 10)

# Generated at 2022-06-13 16:11:00.210000
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('0%', 100) == 0
    assert pct_to_int('1%', 100) == 1
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int('100%', 100) == 100
    assert pct_to_int('0.1%', 100) == 1
    assert pct_to_int('0.5%', 100) == 1
    assert pct_to_int('1.0%', 100) == 1
    assert pct_to_int('1.5%', 100) == 1
    assert pct_to_int('0%', 100, min_value=5) == 5

# Generated at 2022-06-13 16:11:06.403740
# Unit test for function pct_to_int
def test_pct_to_int():
    values = {
        (100, 100): 100,
        (100, 0): 0,
        ("100%", 100): 100,
        ("100%", 0): 0,
        ("0%", 100): 0,
        (5, 100): 5,
        ("5%", 100): 5,
        ("2%", 100): 2,
        ("1%", 100): 1,
    }

    for (value, num_items), expected_result in values.items():
        result = pct_to_int(value, num_items, min_value=1)
        assert result == expected_result

# Generated at 2022-06-13 16:11:12.799265
# Unit test for function object_to_dict
def test_object_to_dict():
    class testclass():
        def __init__(self):
            self.testkey1 = 'testvalue1'
            self.testkey2 = 'testvalue2'
            self.testkey3 = 'testvalue3'

    result = object_to_dict(testclass())
    assert result['testkey3'] == 'testvalue3'

    result = object_to_dict(testclass(), exclude=['testkey3'])
    assert result['testkey3'] is None and len(result) == 2


# Generated at 2022-06-13 16:11:18.215337
# Unit test for function object_to_dict
def test_object_to_dict():

    class TestClass(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    tc = TestClass('Billy', 55)

    result = object_to_dict(tc)
    assert result['name'] == tc.name
    assert result['age'] == tc.age

# Generated at 2022-06-13 16:11:23.885615
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Used by pytest.
    :return:
    """
    class A:
        def __init__(self):
            self.a = 'A'
            self.b = 'B'
            self.c = 'C'

    a = A()
    assert(object_to_dict(a, exclude=['b']) == {'a': 'A', 'c': 'C'})

# Generated at 2022-06-13 16:11:33.585259
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.one = 1
            self.two = 2
            self.three = 3

    test = Test()

    # test normal
    assert object_to_dict(test) == {'three': 3, 'two': 2, 'one': 1}

    # test excluding one
    assert object_to_dict(test, exclude=['one']) == {'three': 3, 'two': 2}

    # test excluding more than one
    assert object_to_dict(test, exclude=['one', 'two']) == {'three': 3}

# Generated at 2022-06-13 16:11:43.224638
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        def __init__(self):
            self.property_1 = 'test_object_value_1'
            self.property_2 = 'test_object_value_2'
            self.property_3 = 'test_object_value_3'

    test_object = TestObject()
    # Test to ensure we can pass in a single item,
    # and that it will get converted to a list
    assert object_to_dict(test_object, exclude=['property_3']) == {'property_1': 'test_object_value_1', 'property_2': 'test_object_value_2'}

# Generated at 2022-06-13 16:11:46.788602
# Unit test for function deduplicate_list
def test_deduplicate_list():
    lst = [1, 1, 2, 2, 3, 4, 5, 3, 6, 7, 8, 7]
    assert deduplicate_list(lst) == [1, 2, 3, 4, 5, 6, 7, 8]

# Generated at 2022-06-13 16:11:56.107158
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list(['test']) == ['test']
    assert deduplicate_list(['test', 'test']) == ['test']
    assert deduplicate_list(['test', 'test', 'unit']) == ['test', 'unit']
    assert deduplicate_list(['test', 'unit', 'test']) == ['test', 'unit']
    assert deduplicate_list(['unit', 'test', 'test']) == ['unit', 'test']


# Generated at 2022-06-13 16:12:03.967044
# Unit test for function object_to_dict
def test_object_to_dict():
    test_class_one = type('TestObject', (object, ), {'a': 1, 'b': 2, 'c': 3})
    result = object_to_dict(test_class_one)
    assert result == {'a': 1, 'b': 2, 'c': 3}

    test_class_two = type('TestObject', (object, ), {'a': 1, 'b': 2, 'c': 3, '_d': 4})
    result = object_to_dict(test_class_two, ['_d'])
    assert result == {'a': 1, 'b': 2, 'c': 3}


# Generated at 2022-06-13 16:12:11.815148
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 2, 1, 3, 2, 4, 3, 5, 4, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([4, 2, 5, 2, 1, 3, 5, 2, 3, 1, 5]) == [4, 2, 5, 1, 3]



# Generated at 2022-06-13 16:12:16.357432
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    assert deduplicate_list(test_list) == [1, 2, 3]



# Generated at 2022-06-13 16:12:21.417736
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1, 1, 3, 3]) == [1, 2, 3]

# Generated at 2022-06-13 16:12:24.860808
# Unit test for function deduplicate_list
def test_deduplicate_list():
    data = ['a', 'b', 'c', 'd', 'a', 'b', 'd']
    result = deduplicate_list(data)
    assert(result == ['a', 'b', 'c', 'd'])


# Generated at 2022-06-13 16:12:32.232201
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """ Unit test for function deduplicate_list"""

    original_list = ['a', 'b', 'c', 'c', 'c', 'd', 'e', 'b']
    deduplicate_list = ['a', 'b', 'c', 'd', 'e']
    assert deduplicate_list(original_list) == deduplicate_list


# Generated at 2022-06-13 16:12:34.886827
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['a', 'b', 'a', 'c', 'a', 'd', 'a', 'b']
    assert deduplicate_list(test_list) == ['a', 'b', 'c', 'd']



# Generated at 2022-06-13 16:12:44.188182
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyObject:
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = 5
    assert object_to_dict(MyObject(1, 2, 3, 4)) == {'a': 1, 'c': 3, 'd': 4, 'b': 2, 'e': 5}
    assert object_to_dict(MyObject(1, 2, 3, 4), ['b', 'c']) == {'a': 1, 'd': 4, 'e': 5}

# Generated at 2022-06-13 16:12:47.627162
# Unit test for function object_to_dict
def test_object_to_dict():
    def A(self):
        self.x = "x"
        self.y = "y"
    a = A([])
    result = object_to_dict(a)
    assert result == {'x': 'x', 'y': 'y'}

# Generated at 2022-06-13 16:12:54.543287
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):

        def __init__(self):
            self.test_key1 = 'test_value1'
            self.test_key2 = 'test_value2'
            self.test_key3 = 'test_value3'

    test = Test()

    result = object_to_dict(test, exclude=['test_key1'])
    assert result == dict(test_key2='test_value2', test_key3='test_value3')



# Generated at 2022-06-13 16:12:56.051387
# Unit test for function deduplicate_list
def test_deduplicate_list():
    result = deduplicate_list(['a', 'b', 'c', 'a', 'b', 'c'])
    assert result == ['a', 'b', 'c']



# Generated at 2022-06-13 16:12:56.914391
# Unit test for function object_to_dict
def test_object_to_dict():
    assert object_to_dict(None) == {}

# Generated at 2022-06-13 16:13:02.150121
# Unit test for function object_to_dict
def test_object_to_dict():
    class testing:
        test_var1 = "test_string"
        test_var2 = "test_var1"
        test_var3 = "test_var2"

    results = object_to_dict(testing, exclude=['test_var2'])
    assert results['test_var1'] == "test_string"
    assert 'test_var2' not in results.keys()
    assert results['test_var3'] == "test_var2"



# Generated at 2022-06-13 16:13:14.823286
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_object(object):
        test_key = "some value"
        test_key2 = "another value"
        _test_private_key = "a value"

    test_obj = test_object()
    test_dict = object_to_dict(test_obj, exclude=['_test_private_key'])
    assert len(test_dict) == 2
    assert 'test_key' in test_dict
    assert 'test_key2' in test_dict
    assert '_test_private_key' not in test_dict


# Generated at 2022-06-13 16:13:19.484385
# Unit test for function deduplicate_list
def test_deduplicate_list():
    l1 = ['a', 'b', 'c', 'd', 'c', 'e', 'a', 'b']
    assert deduplicate_list(l1) == ['a', 'b', 'c', 'd', 'e']

# Generated at 2022-06-13 16:13:25.343883
# Unit test for function object_to_dict
def test_object_to_dict():
    assert object_to_dict(dict(foo=False)) == dict(foo=False)
    assert object_to_dict(dict(foo=False), exclude=['foo']) == {}
    assert object_to_dict(dict(foo=False), exclude=['bar']) == dict(foo=False)
    assert object_to_dict(dict(foo=False), exclude=['foo', 'bar']) == {}



# Generated at 2022-06-13 16:13:30.567340
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self, var1):
            self.var1 = var1
        def _func1(self):
            pass

    obj = TestObject('foo')
    assert object_to_dict(obj, exclude=['_func1']) == {'var1': 'foo'}

# Generated at 2022-06-13 16:13:38.401931
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'b', 'c', 'c', 'd']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list([0, 1, 1, 2, 2, 3]) == [0, 1, 2, 3]
    assert deduplicate_list(['a', 'a', 'b', 'b', 'c', 'c', 'd', 'a']) == ['a', 'b', 'c', 'd', 'a']
    assert deduplicate_list([]) == []
    assert deduplicate_list(['a', 'b', 'c']) == ['a', 'b', 'c']


# Generated at 2022-06-13 16:13:47.354279
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):

        def __init__(self):
            self.key1 = 'value1'
            self.key2 = 'value2'
            self.key3 = 'value3'
            self.keyn = 'valuen'

    test_object = TestObject()
    result = object_to_dict(test_object)
    assert result is not None
    assert 'key1' in result
    assert result['key1'] == 'value1'
    assert 'keyn' in result
    assert result['keyn'] == 'valuen'
    assert 'key3' in result
    assert result['key3'] == 'value3'

# Generated at 2022-06-13 16:13:55.467868
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        test_arg = ''
        test_arg1 = ''

        def __init__(self, test_arg, test_arg1):
            self.test_arg = test_arg
            self.test_arg1 = test_arg1

    test_instance = TestClass('test_arg', 'test_arg1')

    result = object_to_dict(test_instance, exclude=['test_arg', 'test_arg1'])

    assert 'test_arg' not in result.keys()
    assert 'test_arg1' not in result.keys()



# Generated at 2022-06-13 16:13:58.598305
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list = [ 'a', 'b', 'a', 'a', 'c', 'a', 'b']
    dedup_list = deduplicate_list(list)
    assert dedup_list == ['a', 'b', 'c']



# Generated at 2022-06-13 16:14:00.094083
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['foo', 'bar', 'baz', 'bar', 'foo']
    assert deduplicate_list(original_list) == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:14:07.136730
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list
    """
    original_list = ['foo', 'bar', 'foo', 'bar', 'baz', 'foo', 'baz', 'baz', 'baz', 'foo']
    deduplicated_list = deduplicate_list(original_list)
    assert len(deduplicated_list) == 3
    assert deduplicated_list == ['foo', 'bar', 'baz']


# Generated at 2022-06-13 16:14:14.156405
# Unit test for function deduplicate_list
def test_deduplicate_list():

    assert deduplicate_list([1,2,3,3,3,3,3,3,3,3,3,3,3]) == [1,2,3]

# Unit tests for function object_to_dict

# Generated at 2022-06-13 16:14:20.190351
# Unit test for function object_to_dict
def test_object_to_dict():
    import json
    from ansible.module_utils.network.ios.ios import NetworkModule

    module = NetworkModule(argument_spec={})
    module_args = dict(
        asn=1,
        peer_group='MBGP',
        address_family=['ipv4', 'ipv6'],
        password='password',
        description=['test', 'me'],
        send_community=['both', 'none']
    )
    module.params = module_args

    obj = object_to_dict(module, exclude=['params'])
    json.dumps(obj)



# Generated at 2022-06-13 16:14:25.555482
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,1,3]) == [1,2,3]
    assert deduplicate_list([]) == []
    assert deduplicate_list(["1","2","1","3"]) == ["1","2","3"]
    assert deduplicate_list(["1","2","1","3","1","1","1","1", "3", "3", "3", "3", "3"]) == ["1","2","3"]

# Generated at 2022-06-13 16:14:32.488712
# Unit test for function object_to_dict
def test_object_to_dict():
    class SampleClass(object):
        foo = 'bar'
        fred = 'wilma'

    assert object_to_dict(SampleClass()) == {'foo': 'bar', 'fred': 'wilma'}, \
        "object_to_dict does not match expected output"
    assert object_to_dict(SampleClass(), ['foo']) == {'fred': 'wilma'}, \
        "object_to_dict does not match expected output"

# Generated at 2022-06-13 16:14:40.501990
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.test = 'test'
            self.test1 = 'test'
            self._test = 'test'
            self._test1 = 'test'

    obj = Test()
    obj_dict = object_to_dict(obj)
    assert obj_dict['test'] == 'test'
    assert obj_dict['test1'] == 'test'
    assert '_test' not in obj_dict
    assert '_test1' not in obj_dict

# Generated at 2022-06-13 16:14:46.597507
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        """ Test object for function object_to_dict."""
        attr1 = "one"

        def __init__(self):
            """ Test object for function object_to_dict."""
            self.attr2 = "two"

    test_obj = TestObject()
    result = object_to_dict(test_obj)

    assert "attr1" in result
    assert "attr2" in result
    assert result["attr1"] == "one"
    assert result["attr2"] == "two"
    assert type(result) == type({})

# Generated at 2022-06-13 16:14:56.697818
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list(None) == None
    assert deduplicate_list([1, 2, 3, 1]) == [1, 2, 3]
    assert deduplicate_list(['a', 'b', 'c', 'a', 'b', 'b']) == ['a', 'b', 'c']
    assert deduplicate_list([1, 1, 1, 1]) == [1]
    assert deduplicate_list([1, 1, 1, 2]) == [1, 2]
    assert deduplicate_list(['a', 'a', 'a', 'a']) == ['a']
    assert deduplicate_list(['a', 'a', 'a', 'b']) == ['a', 'b']

# Generated at 2022-06-13 16:15:02.014042
# Unit test for function object_to_dict
def test_object_to_dict():
    class DummyModule(object):
        def __init__(self):
            self.api = 'theApi'
            self.state = 'theState'
            self._ansible_module = 'theAnsibleModule'
    d = DummyModule()
    obj = object_to_dict(d, ['_ansible_module'])
    assert obj['api'] == 'theApi'
    assert obj['state'] == 'theState'
    assert '_ansible_module' not in obj.keys()

# Generated at 2022-06-13 16:15:03.987941
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3, 3]) == [1, 2, 3]



# Generated at 2022-06-13 16:15:08.606453
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.a = 1
            self.b = 2

    obj = TestObject()
    obj_dict = {'a': 1, 'b': 2}
    assert object_to_dict(obj) == obj_dict
    assert object_to_dict(obj, exclude=['a']) == {'b': 2}


# Generated at 2022-06-13 16:15:22.607049
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'a']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'a', 'b', 'b']) == ['a', 'b']
    assert deduplicate_list(['b', 'b', 'a', 'a', 'a', 'c']) == ['b', 'a', 'c']
    assert deduplicate_list(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:15:24.503878
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert(deduplicate_list(['a', 'a', 'b', 'b']) == ['a', 'b'])
    assert(deduplicate_list(['a', 'b', 'a', 'b']) == ['a', 'b'])
    assert(deduplicate_list(['a', 'b']) == ['a', 'b'])

# Generated at 2022-06-13 16:15:30.606947
# Unit test for function deduplicate_list
def test_deduplicate_list():
    duplicate_list = ['a', 'b', 'c', 'a', 'c', 'd', 'b', 'a']
    non_duplicate_list = ['a', 'b', 'c', 'd']
    assert deduplicate_list(duplicate_list) == non_duplicate_list

# Generated at 2022-06-13 16:15:38.233606
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Test for object_to_dict
    """
    class TestObject(object):
        def __init__(self):
            self.data = 'test_data'
            self.prop = 'test_prop'
            self.nested_object = TestObject1()
            self.nested_list = [TestObject1(), TestObject2()]

    class TestObject1(object):
        def __init__(self):
            self.data = 'test_data1'
            self.prop = 'test_prop1'
    class TestObject2(object):
        def __init__(self):
            self.data = 'test_data2'
            self.prop = 'test_prop2'
    test_obj = TestObject()

# Generated at 2022-06-13 16:15:49.207009
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list.
    """
    import collections

    assert deduplicate_list(['']) == ['']
    assert deduplicate_list(['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']) == ['a']

# Generated at 2022-06-13 16:15:54.931663
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 4, 5, 1, 2, 6]) == [1, 2, 3, 4, 5, 6]
    assert deduplicate_list(['a', 'b', 'c', 'b', 'd', 'e', 'a', 'f']) == ['a', 'b', 'c', 'd', 'e', 'f']

# Generated at 2022-06-13 16:16:03.343877
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj():
        def __init__(self):
            self.var1 = 1
            self.var2 = 2
            self.var3 = 3

    obj = TestObj()

    obj_dict = object_to_dict(obj)

    assert obj_dict['var1'] == 1
    assert obj_dict['var2'] == 2
    assert obj_dict['var3'] == 3

    # test to make sure exclude works
    obj_dict = object_to_dict(obj, exclude=['var1', 'var3'])

    try:
        obj_dict['var1']
        assert True is False
    except:
        assert True

    try:
        obj_dict['var2']
    except:
        assert True is False


# Generated at 2022-06-13 16:16:12.544356
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        def __init__(self):
            self.test_property_one = "one"
            self.test_property_two = "two"
            self.test_property_three = "three"

        def this_method_is_excluded(self):
            return ""

    test_object = TestObject()
    test_result = object_to_dict(test_object, exclude=["this_method_is_excluded"])

    assert len(test_result) == 3
    assert "test_property_one" in test_result
    assert "test_property_two" in test_result
    assert "test_property_three" in test_result

# Generated at 2022-06-13 16:16:19.452329
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        self.test1 = 'test1'
        self.test2 = 'test2'
        self.test3 = 'test3'

    test_obj = TestClass()
    test_dict = object_to_dict(test_obj, exclude=['test3'])

    assert test_dict['test1'] == 'test1'
    assert test_dict['test2'] == 'test2'
    assert not 'test3' in test_dict



# Generated at 2022-06-13 16:16:26.776720
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]) == [1,2,3,4,5,6,7,8,9]
    assert deduplicate_list([]) == []
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == [1]


# Generated at 2022-06-13 16:16:53.682756
# Unit test for function object_to_dict
def test_object_to_dict():
    class Person(object):
        """
        Basic Person object.
        """
        def __init__(self, first, last):
            self.first = first
            self.last = last

    person = Person('John', 'Doe')
    person_dict = object_to_dict(person)
    assert(person.first == person_dict['first'])
    assert(person.last == person_dict['last'])

    person_dict = object_to_dict(person, exclude=['first'])
    assert('first' not in person_dict)
    assert(person.last == person_dict['last'])

# Generated at 2022-06-13 16:17:04.574219
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Run unit tests for de-duplicating a list.
    """
    import json
    import sys


# Generated at 2022-06-13 16:17:11.693708
# Unit test for function object_to_dict
def test_object_to_dict():
    """ unit tests for object conversion to dictionary """
    class TestObject():
        """ dummy class to use in unit tests """
        def __init__(self):
            self.key1 = 'value1'
            self.key2 = 'value2'

    test_obj = TestObject()

    # test no exclude
    obj_dict = object_to_dict(test_obj)
    assert obj_dict == {'key1': 'value1', 'key2': 'value2'}

    # test with exclude
    obj_dict = object_to_dict(test_obj, exclude=['key1'])
    assert obj_dict == {'key2': 'value2'}



# Generated at 2022-06-13 16:17:24.161649
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list(['1']) == ['1']
    assert deduplicate_list(['1','1','1']) == ['1']
    assert deduplicate_list(['1','2','1']) == ['1','2']
    assert deduplicate_list(['2','1','1']) == ['2','1']
    assert deduplicate_list(['1','1','2']) == ['1','2']
    assert deduplicate_list(['1','2','1','1']) == ['1','2']
    assert deduplicate_list(['1','2','3','4','5']) == ['1','2','3','4','5']

# Generated at 2022-06-13 16:17:32.377943
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 4, 1, 2, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 2, 3, 1, 5, 2, 4]) == [1, 2, 3, 5, 4]
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 1, 2, 2, 1, 2, 2, 5, 2, 1, 2, 5]) == [1, 2, 5]
    assert deduplicate_list([1, 2, 3, 1, 5, 2, 4, 1, 2, 1])

# Generated at 2022-06-13 16:17:35.401724
# Unit test for function object_to_dict
def test_object_to_dict():
    assert object_to_dict(obj=object_to_dict, exclude=['exclude', 'object_to_dict']).keys() == dir(object_to_dict).keys()
    assert object_to_dict(obj=object_to_dict).keys() != dir(object_to_dict).keys()
    assert len(object_to_dict(obj=object_to_dict).keys()) == len(dir(object_to_dict)) - len(object_to_dict.____dict__.keys())


# Generated at 2022-06-13 16:17:46.565735
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,3,4,5,1,2,3,4,5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1,2,3,4,5,1,2,3,4,5,7]) == [1, 2, 3, 4, 5, 7]
    assert deduplicate_list([1,2,3,4,5,1,2,3,4,5,2]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1,1,1,1,1,1,1,1,1,1,1]) == [1]
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:17:50.866800
# Unit test for function object_to_dict
def test_object_to_dict():
    class Obj:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.exclude_me = True

    expected = {
        'a': 'hello',
        'b': 'world'
    }

    obj = Obj('hello', 'world')
    assert object_to_dict(obj, exclude=['exclude_me']) == expected



# Generated at 2022-06-13 16:17:57.127357
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Build an example list and verify deduplicated list is as expected
    """
    original_list = [5,5,5,5,5,5,5,5,5,5,5,5,5]
    deduplicated_list = [5]

    assert deduplicate_list(original_list) == deduplicated_list

# Generated at 2022-06-13 16:18:03.360894
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Unit test for object_to_dict
    """
    class TestClass(object):
        """
        Test class to convert to dict
        """
        def __init__(self):
            """
            Init function
            """
            self.test1 = "test1"
            self.test2 = "test2"
            self._test3 = "test3"
            self.test4 = "test4"

    test = TestClass()
    assert object_to_dict(test, exclude=[]) == {'test1': 'test1', 'test2': 'test2', 'test4': 'test4'}
    assert object_to_dict(test, exclude=['test2']) == {'test1': 'test1', 'test4': 'test4'}

# Generated at 2022-06-13 16:18:57.081195
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Test to make sure that a de-duplicated list is created from a list of items.
    """
    test_list = ['test', 'test', 'test', 'test1', 'test']
    result = deduplicate_list(test_list)
    assert len(result) == 2
    assert result[0] == 'test'
    assert result[1] == 'test1'

# Generated at 2022-06-13 16:19:01.877328
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        hello = "world"
        how = "are you?"
        this = "works"
    result = object_to_dict(TestObject())
    assert sorted(result.keys()) == ['hello', 'how', 'this'], "Failed to get correct keys"
    assert result['hello'] == 'world', "Failed to get correct value for key"
    assert result['how'] == 'are you?', "Failed to get correct value for key"
    assert result['this'] == 'works', "Failed to get correct value for key"

    result = object_to_dict(TestObject(), exclude=["how"])
    assert result['hello'] == 'world', "Failed to get correct value for key"
    assert 'how' not in result, "Failed to exclude key"

# Generated at 2022-06-13 16:19:08.276450
# Unit test for function object_to_dict
def test_object_to_dict():
    class testClass(object):
        def __init__(self):
            self.foo = 'foo'
            self.bar = 'bar'
            self.baz = 'baz'
    test = testClass()
    res = object_to_dict(test, ['bar'])
    assert res['foo'] == 'foo'
    assert not res.has_key('bar')
    assert res['baz'] == 'baz'

# Generated at 2022-06-13 16:19:16.877125
# Unit test for function deduplicate_list
def test_deduplicate_list():
    first = ['a', 'b', 'b', 'c', 'd']
    second = ['d', 'b', 'c', 'a']
    third = ['d', 'd', 'd', 'd']
    fourth = ['d', 'd', 'd', 'd', 'a', 'b', 'b', 'c', 'd']
    assert deduplicate_list(first) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(second) == ['d', 'b', 'c', 'a']
    assert deduplicate_list(third) == ['d']
    assert deduplicate_list(fourth) == ['d', 'a', 'b', 'c']



# Generated at 2022-06-13 16:19:20.491218
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'a', 'b', 'c', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'c', 'b', 'a', 'c']) == ['a', 'c', 'b']
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:19:21.780587
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 1, 3]) == [1, 2, 3]

# Generated at 2022-06-13 16:19:27.109002
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests the deduplicate_list function with a sample list
    """
    list_to_test = [1, "a", 2, 1, "a", 3, 1, 1, 2, "b", "c", "c", "b", "a", "f", "a", 3, 3, 3,
                    1, 2, 3, 4, 5, 6, 5, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 4, 5, 4, 2]
    expected_output = [1, "a", 2, 3, "b", "c", "f", 4, 5, 6, 30]
    output = deduplicate_list(list_to_test)
    assert output == expected_output

# Generated at 2022-06-13 16:19:36.283530
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestBed(object):
        def __init__(self):
            self.a = "A"
            self.b = "B"
            self.c = "C"
            self.excluded_property = "Exclude me"
    result = object_to_dict(TestBed())
    assert result['a'] == "A"
    assert result['b'] == "B"
    assert result['c'] == "C"
    assert 'excluded_property' not in result
    result = object_to_dict(TestBed(), exclude=['a'])
    assert result['a'] == "A"
    assert result['b'] == "B"
    assert result['c'] == "C"
    assert 'excluded_property' not in result

# Generated at 2022-06-13 16:19:40.115861
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'b', 'a']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'a', 'a']) == ['a']
    assert deduplicate_list([]) == []


# Generated at 2022-06-13 16:19:47.564108
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Tests the object_to_dict function.
    """
    class TestClass():
        """
        Class used to test object_to_dict functionality
        """
        def __init__(self):
            self.test_list = [1, 2, 3]
            self.test_dict = {'key': 'val'}
            self.test_str = 'test'
            self._test_private = 'private'
            self.excluded = 'excluded'

    test_obj = TestClass()
    tc_dict = object_to_dict(test_obj, exclude=['excluded'])
    assert tc_dict.keys() == ['test_list', 'test_dict', 'test_str']
    assert tc_dict['test_list'] == [1, 2, 3]