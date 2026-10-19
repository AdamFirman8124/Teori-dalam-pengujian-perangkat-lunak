

# Generated at 2022-06-13 16:10:12.201703
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('5%', 10) == 1
    assert pct_to_int('10%', 10) == 1
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('10%', 101) == 11
    assert pct_to_int('10%', 101, min_value=5) == 5
    assert pct_to_int('5', 10) == 5
    assert pct_to_int(5, 10) == 5

# Generated at 2022-06-13 16:10:18.690177
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    deduplicate list should return a list containing only unique values in the same order in which they are found
    """
    output = [1, -1, 1, 2, 3, 2]
    # test duplicates forwards
    assert deduplicate_list(output) == [1, -1, 2, 3]
    # test duplicates backwards
    assert deduplicate_list(reversed(output)) == [-1, 1, 2, 3]

# Generated at 2022-06-13 16:10:27.281203
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """ Test function deduplicate_list """
    list1 = ['item1', 'item2', 'item3', 'item2']
    list2 = ['item1', 'item2', 'item2', 'item3']
    list3 = ['item1', 'item1', 'item1']
    assert deduplicate_list(list1) == ['item1', 'item2', 'item3']
    assert deduplicate_list(list2) == ['item1', 'item2', 'item3']
    assert deduplicate_list(list3) == ['item1']

# Generated at 2022-06-13 16:10:33.555391
# Unit test for function pct_to_int
def test_pct_to_int():
    # These are all invalid value for the function and should raise
    # ValueError.
    invalid_values = ["abc", "abc%", "abc%", "1", "%", "", "100%d"]
    for v in invalid_values:
        try:
            pct_to_int(v, 100)
        except ValueError:
            pass
        else:
            raise ValueError("%s is not a valid input" % v)

    # Make sure the function returns the correct number or integers.
    assert pct_to_int(10, 10) == 1
    assert pct_to_int("10", 10) == 1
    assert pct_to_int("10%", 10) == 1
    assert pct_to_int("1%", 1) == 1
    assert pct_to_int("10%", 1)

# Generated at 2022-06-13 16:10:38.021489
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(50, 100) == 50
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int('70%', 100) == 70
    assert pct_to_int('0%', 100) == 1

# Generated at 2022-06-13 16:10:45.840180
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('50%', 3) == 1
    assert pct_to_int('50%', 4) == 2
    assert pct_to_int('50%', 5) == 2
    assert pct_to_int('100%', 3) == 3
    assert pct_to_int('100%', 4) == 4
    assert pct_to_int('100%', 5) == 5
    assert pct_to_int('0%', 3) == 1
    assert pct_to_int('0%', 4) == 1
    assert pct_to_int('0%', 5) == 1
    assert pct_to_int(2, 3) == 2
    assert pct_to_int(2, 4) == 2

# Generated at 2022-06-13 16:10:51.793042
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(10, 100) == 10
    assert pct_to_int('10', 100) == 10
    assert pct_to_int('20%', 100) == 20
    assert pct_to_int('20%', 100, min_value=0) == 20
    assert pct_to_int('1%', 100) == 1
    assert pct_to_int('1%', 100, min_value=1) == 1
    assert pct_to_int('1%', 100, min_value=0) == 1
    assert pct_to_int('0%', 100, min_value=1) == 1

# Generated at 2022-06-13 16:11:00.968886
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('100%', 100) == 100
    assert pct_to_int('50%', 100) == 50
    assert pct_to_int('20%', 100) == 20
    assert pct_to_int('10%', 100) == 10
    assert pct_to_int('5%', 100) == 5
    assert pct_to_int('4%', 100) == 4
    assert pct_to_int('1%', 100) == 1
    assert pct_to_int(1, 100) == 1
    assert pct_to_int('1%', 100, 0) == 0


# Generated at 2022-06-13 16:11:11.915823
# Unit test for function pct_to_int
def test_pct_to_int():

    # 100 items, 10pct should return 10
    assert pct_to_int("10%", 100) == 10

    # 100 items, 80pct should return 80
    assert pct_to_int("80%", 100) == 80

    # 100 items, 75pct should return 75
    assert pct_to_int("75%", 100) == 75

    # 100 items, 10pct should return 10
    assert pct_to_int("010%", 100) == 10

    # 100 items, 10pct should return 10
    assert pct_to_int("0%", 100) == 0

    # 100 items, 0pct should return 1
    assert pct_to_int("0%", 100, 1) == 1

    # 100 items, 0pct should return 1

# Generated at 2022-06-13 16:11:17.511108
# Unit test for function pct_to_int
def test_pct_to_int():
    '''
    Function to test the pct_to_int function.
    '''
    if pct_to_int('50%', 4) == 2:
        print('\nAll unit tests for pct_to_int passed\n')
    else:
        print('\nUnit tests for pct_to_int failed\n')



# Generated at 2022-06-13 16:11:26.628966
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1, 2]) == [1, 2]
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 1, 2]) == [1, 2]
    assert deduplicate_list([1, 2, 3, 2, 1, 3, 4]) == [1, 2, 3, 4]


# Generated at 2022-06-13 16:11:39.336320
# Unit test for function deduplicate_list

# Generated at 2022-06-13 16:11:49.996893
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_cases = [
        {
            'case': 'test',
            'input': ['test', 'test', 'test', 'test'],
            'expected': ['test'],
        },
        {
            'case': 'test, case',
            'input': ['test', 'test', 'case', 'test', 'case', 'case'],
            'expected': ['test', 'case'],
        },
        {
            'case': 'test, case, test case',
            'input': ['test', 'test', 'case', 'test', 'case', 'case', 'test case', 'test', 'case'],
            'expected': ['test', 'case', 'test case'],
        },
    ]


# Generated at 2022-06-13 16:11:56.265122
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3

    tc = TestClass()

    assert object_to_dict(tc) == dict(a=1, b=2, c=3)
    assert object_to_dict(tc, ['b', 'c']) == dict(a=1)


# Generated at 2022-06-13 16:12:01.350532
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from nose.tools import assert_equal
    in_list = [1,2,2,3,3,3,1,1,1,5,5,5,5,'a','a','a']
    out_list = deduplicate_list(in_list)
    assert_equal(out_list, [1,2,3,5,'a'])

# Generated at 2022-06-13 16:12:05.464119
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 4, 1, 2, 5, 4, 6]
    assert deduplicate_list(test_list) == [1, 2, 3, 4, 5, 6]

# Generated at 2022-06-13 16:12:08.340708
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        name = 'test'
        description = 'This is a test'
    assert object_to_dict(TestClass, ['name']) == {'description': 'This is a test'}

# Generated at 2022-06-13 16:12:10.820038
# Unit test for function deduplicate_list
def test_deduplicate_list():
    my_list = [1, 2, 3, 3, 4, 5]
    assert deduplicate_list(my_list) == [1, 2, 3, 4, 5]

# Generated at 2022-06-13 16:12:12.586704
# Unit test for function deduplicate_list
def test_deduplicate_list():
    import types
    assert deduplicate_list([1,2,3,2,1]) == [1,2,3]


# Generated at 2022-06-13 16:12:16.665434
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 5, 1, 2, 5, 5, 1, 2, 5]) == [1, 2, 5]


# Generated at 2022-06-13 16:12:24.627735
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for deduplicate_list
    """
    assert deduplicate_list(['a', 'a', 'b', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['c', 'b', 'b', 'a', 'a']) == ['c', 'b', 'a']


# Generated at 2022-06-13 16:12:37.182354
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['1', '1']) == ['1']
    assert deduplicate_list(['1', '1', '2']) == ['1', '2']
    assert deduplicate_list(['1', '3', '1', '2']) == ['1', '3', '2']
    assert deduplicate_list(['1', '1', '2', '2', '2']) == ['1', '2']
    assert deduplicate_list(['1']) == ['1']
    assert deduplicate_list(['1', '2', '3']) == ['1', '2', '3']
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:12:40.969886
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['a', 'b', 'b', 'c', 'a', 'd']
    expected_result = ['a', 'b', 'c', 'd']
    assert expected_result == deduplicate_list(test_list)



# Generated at 2022-06-13 16:12:48.543274
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert [] == deduplicate_list([])
    assert [1,2] == deduplicate_list([1,2])
    assert [1,2] == deduplicate_list([1,1,1,1,1,2,2,2,2,2,2,2])
    assert [1,2,3,4] == deduplicate_list([1,2,3,4])
    assert [1,2,3,4] == deduplicate_list([1,2,3,4,3,2,1])
    assert [1,2,3,4] == deduplicate_list([1,2,3,4,1,2,3,4])

# Generated at 2022-06-13 16:12:54.773431
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'd', 'a', 'f', 'b', 'g', 'd']
    expected_result = ['a', 'b', 'd', 'f', 'g']
    if deduplicate_list(original_list) != expected_result:
        raise AssertionError("Unexpected result for deduplicate_list()")
    else:
        print("test_deduplicate_list: Test passed. The function works as expected")

# Generated at 2022-06-13 16:13:02.619976
# Unit test for function deduplicate_list
def test_deduplicate_list():

    assert deduplicate_list(['a', 'b', 'c', 'a', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'c', 'b', 'a', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'c', 'b', 'a', 'c', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['c', 'a', 'b', 'b', 'a', 'c', 'c']) == ['c', 'a', 'b']

    assert deduplicate_list([]) == []
    assert deduplicate_list(['a']) == ['a']


# Generated at 2022-06-13 16:13:06.957295
# Unit test for function object_to_dict
def test_object_to_dict():
    class testObject:
        def __init__(self):
            self.test1 = 1
            self.test2 = 2
            self.test3 = 3

    test_object = testObject()

    expected = {'test1': 1, 'test2': 2, 'test3': 3}
    result = object_to_dict(test_object)
    assert result == expected

    expected2 = {'test1': 1, 'test2': 2}
    result2 = object_to_dict(test_object, exclude=['test3'])
    assert result2 == expected2


# Generated at 2022-06-13 16:13:16.851194
# Unit test for function object_to_dict
def test_object_to_dict():
    import re

    class DummyClass(object):
        def __init__(self):
            self.dummy_property = "dummy_data"

        def dummy_func(self):
            pass

    class ClassWithExclude(object):
        def __init__(self):
            self._property_exclude = "dummy_data"

        def dummy_func_exclude(self):
            pass

    class ClassWithExcludeRegex(object):
        def __init__(self):
            self._property_exclude_regex = "dummy_data"

        def _dummy_func_exclude_regex(self):
            pass

    dummy_object = DummyClass()

# Generated at 2022-06-13 16:13:20.837324
# Unit test for function deduplicate_list
def test_deduplicate_list():
    deduplicate_test_list = [1, 2, 4, 1, 2, 3, 4]
    assert deduplicate_list(deduplicate_test_list) == [1, 2, 4, 3]


# Generated at 2022-06-13 16:13:32.305314
# Unit test for function object_to_dict
def test_object_to_dict():
    '''
    Test the function object_to_dict in module_utils/network/nxos/nxos.py
    '''
    from ansible.module_utils.network.nxos.nxos import object_to_dict
    class TestClass(object):
        '''
        Class for testing object_to_dict
        '''
        def __init__(self):
            '''
            Initialize object variables
            '''
            self.var1 = 'one'
            self.var2 = 'two'
            self.var3 = 'three'
    obj = TestClass()
    assert object_to_dict(obj) == {'var1': 'one', 'var2': 'two', 'var3': 'three'}

# Generated at 2022-06-13 16:13:43.768312
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert ['a', 'b', 'c', 'd'] == deduplicate_list(['a', 'b', 'b', 'c', 'c', 'd'])
    assert ['a', 'b', 'c', 'd'] == deduplicate_list(['b', 'b', 'd', 'd', 'a', 'c', 'c', 'a', 'b', 'c', 'd'])



# Generated at 2022-06-13 16:13:50.393748
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.a = "A"
            self.b = "B"
            self._c = "C"
    test = Test()
    assert object_to_dict(test) == dict(a="A", b="B")
    assert object_to_dict(test, exclude=['a']) == dict(b="B")

# Generated at 2022-06-13 16:13:58.930272
# Unit test for function deduplicate_list
def test_deduplicate_list():
    if deduplicate_list(['a', 'b', 'b', 'c', 'c', 'c']) != ['a', 'b', 'c']:
        return False
    if deduplicate_list(['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd']) != ['a', 'b', 'c', 'd']:
        return False
    if deduplicate_list(['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) != ['a', 'b']:
        return False

# Generated at 2022-06-13 16:14:09.134074
# Unit test for function object_to_dict
def test_object_to_dict():
    # Set up a named tuple to use for testing
    test_object = collections.namedtuple('test_object', 'name, attribute_1, attribute_2, attribute_3')

    # Create the test object with some fake data
    test_object_data = test_object(name='test', attribute_1='1', attribute_2='2', attribute_3='3')

    # Create a dict of the test object
    dict_object = object_to_dict(test_object_data, exclude=['attribute_3'])

    # Check that the dict object contains the name, attribute_1, and attribute_2
    assert dict_object['name'] == 'test'
    assert dict_object['attribute_1'] == '1'
    assert dict_object['attribute_2'] == '2'

    # Check that the dict object does not have the attribute

# Generated at 2022-06-13 16:14:18.001001
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyTestClass(object):
        foo = "foo_value"
        bar = "bar_value"
        foobar = "foobar_value"
        # i don't want this to be included
        _not_included = "not included value"

    resulting_dict = object_to_dict(MyTestClass())

    assert isinstance(resulting_dict, dict)
    assert len(resulting_dict) == 3
    assert "foo" in resulting_dict
    assert "bar" in resulting_dict
    assert "foobar" in resulting_dict
    assert "_not_included" not in resulting_dict

    assert resulting_dict["foo"] == "foo_value"
    assert resulting_dict["bar"] == "bar_value"
    assert resulting_dict["foobar"] == "foobar_value"

# Generated at 2022-06-13 16:14:24.162842
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['bob', 'john', 'bob', 'tom', 'tim', 'tim', 'bob']
    deduped_list = deduplicate_list(original_list)
    assert deduped_list == ['bob', 'john', 'tom', 'tim']
    assert deduped_list == deduplicate_list(['bob', 'john', 'bob', 'tom', 'tim', 'tim', 'bob'])
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:14:26.405815
# Unit test for function object_to_dict
def test_object_to_dict():
    orig = dict(one=dict(a=1, b=2, c=3))
    obj = namedtuple("obj", orig['one'].keys())(**orig['one'])

    assert object_to_dict(obj) == orig['one']



# Generated at 2022-06-13 16:14:32.185085
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj:
        """
        A test object to test the object_to_dict function
        """
        var1 = 'Test variable 1'
        var2 = 'Test variable 2'
        _no_show_var = 'I am not shown'
    assert object_to_dict(TestObj()) == dict(var1='Test variable 1', var2='Test variable 2')



# Generated at 2022-06-13 16:14:36.469437
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj:
        _private = 'test'
        _private_two = 'test_two'
        def __init__(self):
            self.public_one = 'test_one'
            self.public_two = 'test_two'

    test_instance = TestObj()
    assert test_instance.public_one == 'test_one'
    assert test_instance.public_two == 'test_two'
    assert test_instance._private == 'test'
    assert test_instance._private_two == 'test_two'

    test_dict = object_to_dict(test_instance)
    assert test_dict['public_one'] == 'test_one'
    assert test_dict['public_two'] == 'test_two'
    assert not '_private' in test_dict

# Generated at 2022-06-13 16:14:42.769943
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        def __init__(self):
            self.first = 'first'
            self.second = 'second'
            self.third = 'third'
    obj = TestClass()
    assert object_to_dict(obj) == dict(first='first', second='second', third='third')
    assert object_to_dict(obj, exclude=['second']) == dict(first='first', third='third')

# Generated at 2022-06-13 16:14:56.987201
# Unit test for function object_to_dict
def test_object_to_dict():

    class TestObj:
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self.c = 'c'
            self._c = 'd'

    t_obj = TestObj()

    result = object_to_dict(t_obj)
    for key in result:
        assert result[key] == key
    assert result['b'] == 'b'
    assert '_c' not in result


# Generated at 2022-06-13 16:15:01.396324
# Unit test for function object_to_dict
def test_object_to_dict():
    # Create a dummy class
    class dummy_class:
        def __init__(self):
            self.dummy_prop = True
            self.another_prop = "abc"

    expected = {
        'dummy_prop': True,
        'another_prop': "abc"
    }

    o = dummy_class()
    assert expected == object_to_dict(o)



# Generated at 2022-06-13 16:15:04.268613
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'd', 'b', 'a']) == ['a', 'b', 'c', 'd']

# Generated at 2022-06-13 16:15:07.810422
# Unit test for function object_to_dict
def test_object_to_dict():
    assert object_to_dict(dict, ["values"])["keys"] == dict.keys # test with dict (dict.values returns dict_keys object)
    assert object_to_dict(list(range(10)))["append"] == list(range(10)).append # test with list

# Generated at 2022-06-13 16:15:14.114679
# Unit test for function object_to_dict
def test_object_to_dict():
    class Foo(object):
        def __init__(self):
            self._a = 'a'
            self._b = 'b'
            self._c = 'c'
            self._d = 'd'

        def __eq__(self, other):
            return other.__dict__ == self.__dict__

        def __ne__(self, other):
            return not self.__eq__(other)

    assert Foo() == object_to_dict(Foo(), ['_a'])
    assert Foo() != object_to_dict(Foo())



# Generated at 2022-06-13 16:15:22.892440
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    reference_dict = dict(foo='foo', bar='bar', baz='baz')
    test_class = TestClass(**reference_dict)
    test_class_dict = object_to_dict(test_class)
    assert test_class_dict == reference_dict

# Generated at 2022-06-13 16:15:27.225370
# Unit test for function object_to_dict
def test_object_to_dict():
    class A:
        foo = "bar"
        test_key = "test_value"

    result = object_to_dict(A())
    assert isinstance(result, dict)
    assert 'foo' in result
    assert 'test_key' in result
    assert result['foo'] == "bar"
    assert result['test_key'] == "test_value"



# Generated at 2022-06-13 16:15:36.556461
# Unit test for function object_to_dict
def test_object_to_dict():
    from ansible.module_utils.network.nxos.nxos import nxos_argument_spec
    from collections import namedtuple
    Args = namedtuple('args', 'candidate, diff, replace')
    args = Args(candidate=False, diff=False, replace=False)
    result = object_to_dict(args)
    assert isinstance(result, dict)
    assert result.get('candidate') is False
    assert result.get('diff') is False
    assert result.get('replace') is False
    result = object_to_dict(nxos_argument_spec)
    assert isinstance(result, dict)
    assert result.get('provider') is not None



# Generated at 2022-06-13 16:15:38.880646
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3, 1, 4, 2, 3, 5]) == [1, 2, 3, 4, 5]

# Generated at 2022-06-13 16:15:48.910218
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]) == [1,2,3]
    assert deduplicate_list([1,2,3,4,4]) == [1,2,3,4]
    assert deduplicate_list([]) == []
    assert deduplicate_list(['test', 'test2']) == ['test', 'test2']
    assert deduplicate_list([0,0,0,0,0,0,0,0,0,0,0,0]) == [0]

# Generated at 2022-06-13 16:16:09.154056
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['a', 'b', 'c', 'a', 'd', 'c', 'e', 'f', 'e']
    assert deduplicate_list(test_list) == ['a', 'b', 'c', 'd', 'e', 'f']


# Generated at 2022-06-13 16:16:12.344861
# Unit test for function deduplicate_list
def test_deduplicate_list():
    initial_list = [1, 1, 2, 3, 3, 5, 8, 8, 13]
    deduplicated_list = deduplicate_list(initial_list)
    assert deduplicated_list == [1, 2, 3, 5, 8, 13]


# Generated at 2022-06-13 16:16:15.315501
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'a', 'b', 'c']) == ['a', 'b', 'c']



# Generated at 2022-06-13 16:16:17.361518
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,3,2,1]) == [1,2,3]


# Generated at 2022-06-13 16:16:24.147285
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.string_property = 'test'
            self.int_property = 1
            self.list_property = [1, 2, 3]
            self.dict_property = {'key': 'value'}

    obj = TestObject()
    obj_dict = object_to_dict(obj, exclude=['dict_property'])

    assert obj_dict == {'string_property': 'test',
                        'int_property': 1,
                        'list_property': [1, 2, 3]}

# Generated at 2022-06-13 16:16:29.880293
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 1, 3, 3, 1]) == [1, 2, 3]
    assert deduplicate_list(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'b', 'a', 'c', 'c', 'a']) == ['a', 'b', 'c']


# Generated at 2022-06-13 16:16:31.367311
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'b', 'c', 'a']) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:16:34.087850
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from ansible.module_utils.network.cnos.cnos import deduplicate_list

    assert deduplicate_list([1, 1, 2, 3, 1]) == [1, 2, 3]

# Generated at 2022-06-13 16:16:38.944713
# Unit test for function object_to_dict
def test_object_to_dict():
    obj = type("Test", (object,), {"foo" : "baz", "bar" : "barm", "bleh" : "blah"})
    assert object_to_dict(obj) == {"foo" : "baz", "bar" : "barm", "bleh" : "blah"}
    assert object_to_dict(obj, exclude=["bar"]) == {"foo" : "baz", "bleh" : "blah"}



# Generated at 2022-06-13 16:16:45.137300
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Empty list should be empty after deduplication
    assert deduplicate_list([]) == []
    # There should be no changes for this list
    assert deduplicate_list([1,2,3,4,5]) == [1,2,3,4,5]
    # We should have only one 'c'
    assert deduplicate_list(['a', 'c', 'c', 'b']) == ['a', 'c', 'b']
    # We should have only one 'b'
    assert deduplicate_list(['a', 'c', 'b', 'b']) == ['a', 'c', 'b']


# Generated at 2022-06-13 16:17:27.632183
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_obj:
        var = 'test'
        var2 = 'test2'
        var3 = 'test3'
        var4 = 'test4'
        func = True

    obj = test_obj()
    obj_dict = object_to_dict(obj)
    assert obj_dict.get('var') == 'test'
    assert obj_dict.get('var2') == 'test2'
    assert obj_dict.get('var3') == 'test3'
    assert obj_dict.get('var4') == 'test4'
    assert obj_dict.get('func')

    obj_dict_exclude = object_to_dict(obj, exclude=['var3', 'var4'])
    assert obj_dict_exclude.get('var') == 'test'
    assert obj_dict_exclude

# Generated at 2022-06-13 16:17:35.412635
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert [] == deduplicate_list([])
    assert [1] == deduplicate_list([1])
    assert [1, 2] == deduplicate_list([1, 2])
    assert [2, 1] == deduplicate_list([1, 2])
    assert [1, 2] == deduplicate_list([1, 1, 2])
    assert [3, 1, 2] == deduplicate_list([3, 3, 1, 2, 2])
    assert [1, 2, 3] == deduplicate_list([1, 1, 2, 2, 3, 3])



# Generated at 2022-06-13 16:17:41.141487
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass(object):
        def __init__(self):
            self.property1 = 1
            self.property2 = 2

    obj = TestClass()
    obj_dict = object_to_dict(obj)
    assert obj_dict['property1'] == 1

# Generated at 2022-06-13 16:17:48.847308
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Input List
    original_list = ['cat', 'dog', 'cat', 'dog', 'cat', 'fish', 'dog', 'cat', 'cat']
    # Expected output list
    expected_list=['cat', 'dog', 'fish']
    # Call function to deduplicate input list
    dedup_list = deduplicate_list(original_list)
    # Assert that the expected output was received
    assert dedup_list == expected_list

#This section calls the unit test for the deduplicate_list function
if __name__ == '__main__':
    test_deduplicate_list()

# Generated at 2022-06-13 16:17:53.739054
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyClass(object):
        def __init__(self):
            self.one = 1
            self._two = 2
            self.three = 3
            self.four = 4
            self._five = 5
    # Create class and convert to dict
    my_class = MyClass()
    my_class_dict = object_to_dict(my_class, exclude=['_two', '_five'])
    assert sorted(my_class_dict.items()) == [('four', 4), ('one', 1), ('three', 3)]

# Generated at 2022-06-13 16:18:01.645638
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.data = {'a': 'a', 'b': 'b', 'c': 'c'}

        def func(self):
            return 'func'

        def func_exclude(self):
            return 'func_exclude'

    to = TestObject()

    assert object_to_dict(to) == {'data': {'a': 'a', 'b': 'b', 'c': 'c'}, 'func': 'func', 'func_exclude': 'func_exclude'}
    assert object_to_dict(to, exclude=['func']) == {'data': {'a': 'a', 'b': 'b', 'c': 'c'}, 'func_exclude': 'func_exclude'}
    assert object_to_dict

# Generated at 2022-06-13 16:18:06.865476
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'c', 'b', 'd', 'e', 'a']) == ['a', 'b', 'c', 'd', 'e']
    assert deduplicate_list(['a', 'b']) == ['a', 'b']
    assert deduplicate_list([]) == []


# Generated at 2022-06-13 16:18:11.049092
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['abc', 'abc', 'def', 'abc', 'ghi']) == ['abc', 'def', 'ghi']



# Generated at 2022-06-13 16:18:17.063874
# Unit test for function object_to_dict
def test_object_to_dict():
    class A(object):
        """ test class """
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.c = 0
    obj = A(1, 2)
    result = object_to_dict(obj)
    assert result == {'a': 1, 'b': 2, 'c': 0}

# Generated at 2022-06-13 16:18:28.692517
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 1]
    if deduplicate_list(test_list) != [1, 2, 3, 4, 5, 6, 7, 1]:
        print('**FAIL**')
        print('Actual value: %s' % deduplicate_list(test_list))
        print('Expected value: %s' % [1, 2, 3, 4, 5, 6, 7, 1])
    else:
        print('Test passed')

if __name__ == '__main__':
    test_deduplicate_list()

# Generated at 2022-06-13 16:19:44.309087
# Unit test for function object_to_dict
def test_object_to_dict():
    class Object:
        def __init__(self, name, age, description):
            self.name = name
            self.age = age
            self.description = description

    person = Object('James', '30', 'Sales Manager')
    result = object_to_dict(person)
    assert result == {'name': 'James', 'age': '30', 'description': 'Sales Manager'}
    result = object_to_dict(person, exclude=['name'])
    assert result == {'age': '30', 'description': 'Sales Manager'}

# Generated at 2022-06-13 16:19:47.703269
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 4, 5]) == [1, 2, 3, 4, 5]

# Generated at 2022-06-13 16:19:50.358499
# Unit test for function deduplicate_list
def test_deduplicate_list():
    data = [1, 2, 3, 5, 4, 3, 3, 5]
    assert deduplicate_list(data) == [1, 2, 3, 5, 4]

# Generated at 2022-06-13 16:20:00.153772
# Unit test for function object_to_dict
def test_object_to_dict():
    class testObj(object):
        def __init__(self):
            self.prop1 = "prop value 1"
            self.prop2 = "prop value 2"
            self.prop3 = "prop value 3"
            self.prop4 = "prop value 4"
    obj = testObj()
    obj_dict = object_to_dict(obj)
    assert obj_dict == {'prop1': 'prop value 1', 'prop2': 'prop value 2',
                        'prop3': 'prop value 3', 'prop4': 'prop value 4'}
    obj_dict = object_to_dict(obj, exclude=['prop4', 'prop1'])
    assert obj_dict == {'prop2': 'prop value 2', 'prop3': 'prop value 3'}

# Generated at 2022-06-13 16:20:03.546212
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,2,3,4,4,4,5,5,5]) == [1,2,3,4,5]