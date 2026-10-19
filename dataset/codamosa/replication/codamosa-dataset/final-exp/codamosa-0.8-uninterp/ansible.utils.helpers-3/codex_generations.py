

# Generated at 2022-06-13 16:10:06.921950
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1,2,1,2,2,2,2,2,2,3,4,5,5,5]
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == [1,2,3,4,5]


# Generated at 2022-06-13 16:10:17.077262
# Unit test for function pct_to_int
def test_pct_to_int():
    # Test straight int
    assert pct_to_int(1, 100) == 1
    # Test straight float
    assert pct_to_int(1.0, 100) == 1
    # Test int percent
    assert pct_to_int(50, 100) == 50
    # Test int percent
    assert pct_to_int(50.5, 100) == 51
    # Test string percent
    assert pct_to_int('50%', 100) == 50
    # Test string percent
    assert pct_to_int('50.5%', 100) == 51
    # Test convert from percent to decimal
    assert pct_to_int('1%', 100) == 1
    # Test convert from percent to decimal
    assert pct_to_int('0.01%', 100) == 1
    # Test convert from

# Generated at 2022-06-13 16:10:27.421620
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(0.5, 100) == 50
    assert pct_to_int("50%", 100) == 50
    assert pct_to_int("50.0%", 100) == 50
    assert pct_to_int(" 50 % ", 100) == 50
    assert pct_to_int("0.1%", 100) == 1
    assert pct_to_int("0.9%", 100) == 1
    assert pct_to_int("0.5%", 100) == 1
    assert pct_to_int("0.0%", 100) == 1
    assert pct_to_int("100%", 100) == 100
    assert pct_to_int("100.0%", 100) == 100
    assert pct_to_int("1%", 100) == 1

# Generated at 2022-06-13 16:10:32.764420
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('30%', 100) == 30
    assert pct_to_int(30, 100) == 30
    assert pct_to_int('1.5%', 100) == 2, 'Default is rounding up'
    assert pct_to_int('0.5%', 100) == 1, '0 values are changed to 1'
    assert pct_to_int(0, 100) == 1

# Generated at 2022-06-13 16:10:40.800476
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # Test that it works with no duplicates
    original_list = ['A', 'B']
    result = deduplicate_list(original_list)
    assert(result == original_list)

    # Test expected behavior
    original_list = ['A', 'A', 'B', 'C', 'B', 'C', 'A', 'D']
    result = deduplicate_list(original_list)
    assert(result == ['A', 'B', 'C', 'D'])

# Run unit test for function deduplicate_list
test_deduplicate_list()

# Generated at 2022-06-13 16:10:46.558744
# Unit test for function pct_to_int
def test_pct_to_int():

    def list_sum(l):
        return sum(l)

    assert pct_to_int(10, list_sum([1,2,3,4,5])) == 10
    assert pct_to_int('10%', list_sum([1,2,3,4,5])) == 10
    assert pct_to_int('12%', list_sum([1,2,3,4,5])) == 12
    assert pct_to_int('120%', list_sum([1,2,3,4,5])) == 60

# Generated at 2022-06-13 16:10:53.363952
# Unit test for function pct_to_int

# Generated at 2022-06-13 16:10:58.949538
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int(10, 10) == 10
    assert pct_to_int('10%', 40) == 4
    assert pct_to_int('100%', 40) == 40
    assert pct_to_int('10.000001%', 40) == 2
    assert pct_to_int('101%', 40) == 41
    assert pct_to_int('1%', 40) == 1
    assert pct_to_int('0.1%', 40) == 1
    assert pct_to_int('0%', 40) == 1

# Generated at 2022-06-13 16:11:05.413885
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Tests the deduplicate_list function
    """
    original_list = ['a', 'b', 'a', 'c', 'd', 'c']
    deduped_list = deduplicate_list(original_list)

    assert deduped_list[0] == 'a'
    assert deduped_list[1] == 'b'
    assert deduped_list[2] == 'c'
    assert deduped_list[3] == 'd'


# Generated at 2022-06-13 16:11:13.090501
# Unit test for function pct_to_int
def test_pct_to_int():
    # Test valid results
    assert(pct_to_int(100, 100) == 100)
    assert(pct_to_int('100%', 100) == 100)
    assert(pct_to_int('3%', 100) == 3)
    assert(pct_to_int(3, 100) == 3)
    assert(pct_to_int('3.5%', 100) == 4)
    assert(pct_to_int(3.5, 100) == 4)
    assert(pct_to_int('3%', 0) == 3)

    # Test invalid results
    try:
        assert(pct_to_int('hello', 100) == 0)
    except ValueError:
        pass
    else:
        assert(False)



# Generated at 2022-06-13 16:11:18.950808
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,1,2,1,1,1,1,1,1,1,1,1]) == [1,2]
    assert deduplicate_list([1,2,2,4,4,4,4,4,4,3,3,3,3,3,3,3,3]) == [1,2,4,3]



# Generated at 2022-06-13 16:11:24.464310
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list
    """
    assert deduplicate_list(["a", "b", "c", "a", "c", "b", "a", "d", "b", "c"]) == ["a", "b", "c", "d"]
    assert deduplicate_list(["a", "b", "c", "b", "a", "c", "b", "c", "a", "d", "b", "c"]) == ["a", "b", "c", "d"]

# Generated at 2022-06-13 16:11:31.255988
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('100%', 1) == 1
    assert pct_to_int('100%', 2) == 2
    assert pct_to_int('100%', 3) == 3
    assert pct_to_int('101%', 10) == 10
    assert pct_to_int('10%', 10) == 1


# Generated at 2022-06-13 16:11:36.834905
# Unit test for function deduplicate_list
def test_deduplicate_list():
    # deduplicate_list should not modify the order of items where there are no duplicates
    assert deduplicate_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # deduplicate_list should maintain the first occurrence of duplicate items
    assert deduplicate_list([1, 2, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([1, 2, 3, 4, 5, 5]) == [1, 2, 3, 4, 5]

    # deduplicate_list should put the two equal items to the end
    assert deduplicate_list

# Generated at 2022-06-13 16:11:41.945768
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('10%', 10) == 1
    assert pct_to_int('10%', 50) == 5
    assert pct_to_int(10, 10) == 10
    assert pct_to_int('10%', 10, min_value=2) == 2
    assert pct_to_int('10%', 10, min_value=11) == 10



# Generated at 2022-06-13 16:11:50.637914
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_to_test = ['asd','qwe','qwe','qwe','zxc','zxc','wer','zxc','zxc','zxc','zxc','asd','wer','zxc','asd','asd','asd','qwe','qwe','zxc','zxc','zxc']
    expected_output = ['asd','qwe','zxc','wer']

    deduplicated_list = deduplicate_list(list_to_test)
    if deduplicated_list != expected_output:
        print("Expected list '%s' and received list '%s' are different" % (str(expected_output),str(deduplicated_list)))
        assert False


# Generated at 2022-06-13 16:11:56.731807
# Unit test for function pct_to_int
def test_pct_to_int():
    assert pct_to_int('20%', 100) == 20
    assert pct_to_int('20', 100) == 20
    assert pct_to_int(21, 100) == 21
    assert pct_to_int('100%', 100) == 100
    assert pct_to_int('0%', 100) == 1
    assert pct_to_int(0, 100) == 1
    assert pct_to_int(1, 100) == 1
    assert pct_to_int('100%', 100, min_value=5) == 100
    assert pct_to_int('0%', 100, min_value=5) == 5
    assert pct_to_int(0, 100, min_value=5) == 5

# Generated at 2022-06-13 16:12:03.740059
# Unit test for function pct_to_int
def test_pct_to_int():
    min_value = 1
    num_items = 100
    value1 = '50%'
    assert pct_to_int(value1, num_items, min_value) == 50

    value2 = '75%'
    assert pct_to_int(value2, num_items, min_value) == 75

    value3 = '101%'
    assert pct_to_int(value3, num_items, min_value) == 100

    value4 = '50'
    assert pct_to_int(value4, num_items, min_value) == 50

# Generated at 2022-06-13 16:12:10.659820
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Unit test for function deduplicate_list
    """
    testlist = [1, 1, 2, 3, 4, 5, 5, 'h', 'h', 1, 1, 2, 3, 4, 'i', 1, 2]
    testlist_correct = [1, 2, 3, 4, 5, 'h', 'i']
    assert deduplicate_list(testlist) == testlist_correct



# Generated at 2022-06-13 16:12:13.655809
# Unit test for function deduplicate_list
def test_deduplicate_list():
    testList = ['a', 'b', 'a', 'c', 'd', 'b', 'd', 'a']
    expectedList = ['a', 'b', 'c', 'd']
    resultList = deduplicate_list(testList)

    assert(expectedList == resultList)

# Generated at 2022-06-13 16:12:21.533733
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj:
        def __init__(self):
            self.test1 = "test1"
            self.test2 = "test2"
    
    test_obj = TestObj()
    obj_dict = object_to_dict(test_obj, ['test1'])

    assert obj_dict.get('test1') is None
    assert obj_dict.get('test2') == 'test2'

# Generated at 2022-06-13 16:12:28.653652
# Unit test for function deduplicate_list
def test_deduplicate_list():
    import random
    import string
    import unittest
    class TestDedupList(unittest.TestCase):
        def test_dedup_dups(self):
            test_list = []
            for i in range(0,5):
                l = random.randint(0, 10)
                for j in range(0, l):
                    test_list.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)))

            # Randomly duplicate items in list
            for i in range(0,10):
                test_list.append(test_list[random.randint(0, len(test_list) - 1)])

            self.assertEqual(len(deduplicate_list(test_list)), len(set(test_list)))

# Generated at 2022-06-13 16:12:36.205047
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1]) == [1]
    assert deduplicate_list([1, 2]) == [1, 2]
    assert deduplicate_list([1, 2, 1]) == [1, 2]
    assert deduplicate_list([1, 2, 1, 1, 2, 3, 1, 4, 2, 3, 5]) == [1, 2, 3, 4, 5]

# Generated at 2022-06-13 16:12:43.478578
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Tests for function object_to_dict.
    """
    class TestObj:
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
            self.d = 4
            self.e = 5
            self.f = 6

    obj = TestObj()
    assert object_to_dict(obj, ['d', 'e', 'f']) == {'a': 1, 'b': 2, 'c': 3}



# Generated at 2022-06-13 16:12:46.094089
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_to_deduplicate = ['unit', 'test', 'a', 'list', 'unit', 'list', 13, 13, 13]
    deduplicated_list = deduplicate_list(list_to_deduplicate)

    assert deduplicated_list == ['unit', 'test', 'a', 'list', 13]

# Generated at 2022-06-13 16:12:48.585600
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ["1", "2", "1"]
    assert deduplicate_list(test_list) == ["1", "2"]

# Generated at 2022-06-13 16:12:53.730293
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        def __init__(self):
            self.property1 = "value1"
            self.property2 = "value2"
            self._property3 = "value3"

    result = object_to_dict(TestObject())
    assert result == {'property1': 'value1', 'property2': 'value2'}


# Generated at 2022-06-13 16:12:56.127745
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 1, 2, 3, 1, 4, 2]) == [1, 2, 3, 1, 4]


# Generated at 2022-06-13 16:13:03.308302
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestClass:
        def __init__(self, var1, var2, var3):
            self.var1 = var1
            self.var2 = var2
            self.var3 = var3

    tc = TestClass("abc", "def", "ghi")

    assert ['var1', 'var2', 'var3'] == sorted(object_to_dict(tc).keys())
    assert ['var1', 'var2'] == sorted(object_to_dict(tc, ['var3']).keys())
    assert ['var1', 'var3'] == sorted(object_to_dict(tc, ['var2']).keys())


# Generated at 2022-06-13 16:13:07.919766
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        def __init__(self):
            self.test_parameter = 'test'
    test_object = TestObject()
    result = object_to_dict(test_object)
    result['test_parameter'].should.equal('test')

# Generated at 2022-06-13 16:13:19.088334
# Unit test for function deduplicate_list
def test_deduplicate_list():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    class TestDeduplicateList(unittest.TestCase):
        def test_deduplicate_list_result(self):
            a=[1,2,3,1,2,3]
            b=[1,2,3]
            self.assertEqual(deduplicate_list(a),b)
            a=['a','b']
            b=['a','b']
            self.assertEqual(deduplicate_list(a),b)
            a=[1,2,1,2,2,2]
            b=[1,2]
            self.assertEqual(deduplicate_list(a),b)
            a=['a','b','a','a','b']

# Generated at 2022-06-13 16:13:22.750406
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['a', 'b', 'b', 'c']
    result_list = deduplicate_list(test_list)
    assert(result_list == ['a', 'b', 'c'])


# Generated at 2022-06-13 16:13:30.297666
# Unit test for function object_to_dict
def test_object_to_dict():
    # Test class
    class Obj(object):
        attr1 = "foo"
        attr2 = "bar"
        attr3 = "baz"

    # Test actual object
    o = Obj()

    # Test function
    output = object_to_dict(o, exclude=['attr3'])

    # Ensure output is a dict
    assert isinstance(output, dict)

    # Ensure there are 2 items
    assert len(output) == 2

    # Ensure output contains attr1 and attr2
    assert 'attr1' in output
    assert 'attr2' in output

    # Ensure output does not contain attr3
    assert 'attr3' not in output


# Generated at 2022-06-13 16:13:33.774915
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list_in = ['a', 'b', 'c', 'a', 'b']
    list_out = ['a', 'b', 'c']
    assert deduplicate_list(list_in) == list_out

# Generated at 2022-06-13 16:13:38.292068
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ['1', '2', '3', '1', '1', '4']
    test_list = deduplicate_list(test_list)
    assert test_list == ['1', '2', '3', '4']

# Generated at 2022-06-13 16:13:48.740481
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1,2,2,2,1,1,2,2,2,2,2,2,1,1,1]) == [1,2]
    assert deduplicate_list([3,4,4,4,3,3,4,4,4,4,4,4,3,3,3]) == [3,4]
    assert deduplicate_list([1,1,1,1,1,1,1]) == [1]
    assert deduplicate_list([1,1,1,1,1,1,2,2,2,2,2,2,2]) == [1,2]

# Generated at 2022-06-13 16:13:53.847794
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 1, 2, 1, 2, 3, 5, 'a', 'b', 'a', 'b']
    deduplicated_list = deduplicate_list(original_list)
    assert(deduplicated_list == [1, 2, 3, 5, 'a', 'b'])

# Generated at 2022-06-13 16:13:58.364558
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject(object):
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
            self.d = 4
    obj = TestObject()
    assert object_to_dict(obj, ['a']) == {'b': 2, 'c': 3, 'd': 4}



# Generated at 2022-06-13 16:14:07.027115
# Unit test for function deduplicate_list
def test_deduplicate_list():
    """
    Ensures deduplicate_list works as expected.
    """
    assert deduplicate_list([1, 2, 1, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 1, 3, 2, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 1, 2]) == [1, 2]
    assert deduplicate_list([1, 2, 3, 2, 1]) == [1, 2, 3]


# Generated at 2022-06-13 16:14:16.141524
# Unit test for function deduplicate_list
def test_deduplicate_list():
    replacement = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    assert deduplicate_list([1, 2, 4, 5, 6, 1, 7, 2, 8, 5, 9, 10]) == replacement
    assert deduplicate_list([4, 1, 7, 2, 8, 5, 9, 10, 1, 2, 4, 5, 6]) == replacement
    assert deduplicate_list([1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
    assert deduplicate_list([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 5, 6, 1, 4]) == [1, 2, 3, 5, 6, 4]


# Generated at 2022-06-13 16:14:22.735676
# Unit test for function deduplicate_list
def test_deduplicate_list():
    my_list = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6]
    my_expected_list = [1, 2, 3, 4, 5, 6]
    assert deduplicate_list(my_list) == my_expected_list


# Generated at 2022-06-13 16:14:32.489140
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([3, 2, 2, 1]) == [3, 2, 1]
    assert deduplicate_list([3, 3, 3, 3]) == [3]
    assert deduplicate_list([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert deduplicate_list([1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == [1, 2, 3, 4]



# Generated at 2022-06-13 16:14:38.728921
# Unit test for function object_to_dict
def test_object_to_dict():
    assert object_to_dict(Example()) == {'b': True, 'i': 1, 'l': [1, 2, 3], 't': 'test'}
    assert object_to_dict(Example(), ['i']) == {'b': True, 'l': [1, 2, 3], 't': 'test'}


# Generated at 2022-06-13 16:14:47.000020
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyClass(object):
        """
        Sample object to convert
        """
        prop1 = "prop1"
        prop2 = "prop2"
    my_obj = MyClass()

    assert {'prop1': 'prop1', 'prop2': 'prop2'} == object_to_dict(my_obj)
    assert {'prop1': 'prop1', 'prop2': 'prop2'} == object_to_dict(my_obj, ['prop3'])
    assert {'prop1': 'prop1'} == object_to_dict(my_obj, ['prop2'])
    assert {} == object_to_dict(my_obj, ['prop1', 'prop2'])
    assert {} == object_to_dict(my_obj, ['prop1', 'prop2', 'prop3'])



# Generated at 2022-06-13 16:14:53.533835
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ["a", "b", "a", "c", "b", "a", "d", "e", "b", "a"]
    expected_list = ["a", "b", "c", "d", "e"]
    output_list = deduplicate_list(original_list)
    assert output_list == expected_list,\
        "Should be %s, but got %s" % (expected_list, output_list)


# Generated at 2022-06-13 16:15:02.292099
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([]) == []
    assert deduplicate_list([1,2,3]) == [1,2,3]
    assert deduplicate_list([1,1,1,1,1]) == [1]
    assert deduplicate_list([1,2,1,2,1,2]) == [1,2]
    assert deduplicate_list([0,1,2,1,2,0]) == [0,1,2]
    assert deduplicate_list([0,0,0,0,1,1,1,1,2,2,2,2]) == [0,1,2]

# Generated at 2022-06-13 16:15:09.501460
# Unit test for function object_to_dict
def test_object_to_dict():
    class Obj(object):
        a = "a"
        b = "b"
        c = "c"

    assert object_to_dict(Obj()) == {
        'a': "a",
        'b': "b",
        'c': "c",
    }

    assert object_to_dict(Obj(), exclude=['a']) == {
        'b': "b",
        'c': "c",
    }

    assert object_to_dict(Obj(), exclude=['a', 'b']) == {
        'c': "c",
    }


# Generated at 2022-06-13 16:15:16.046464
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject():
        def __init__(self):
            self.name = 'foo'
            self.value = 'bar'

    test_object = TestObject()
    result = dict(name='foo', value='bar')
    assert(object_to_dict(test_object) == result)
    result = dict(name='foo')
    assert(object_to_dict(test_object, exclude=['value']) == result)
    test_object = dict(name='foo', value='bar')
    result = dict(name='foo', value='bar')
    assert(object_to_dict(test_object) == result)


# Generated at 2022-06-13 16:15:21.697448
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = ["one", "two", "three", "two", "three", "four", "one", "two", "three", "four", "five"]
    expected = ["one", "two", "three", "four", "five"]
    assert deduplicate_list(test_list) == expected


# Generated at 2022-06-13 16:15:28.835390
# Unit test for function deduplicate_list
def test_deduplicate_list():
    deduplicate_list([])
    deduplicate_list([1,1])
    deduplicate_list([1,1,2])
    deduplicate_list([1,1,2,3,3])
    deduplicate_list([1,2,3,3,3,3,3,3,3,1,2,2,2,2,2])
    deduplicate_list([1,2,3,3,3,3,3,3,3,1,2,2,2,2,2])[0] == 1
    return True

# Generated at 2022-06-13 16:15:35.599969
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'b', 'c', 'd', 'b', 'd', 'd']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list([]) == []
    assert deduplicate_list(None) is None



# Generated at 2022-06-13 16:15:40.221610
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['a', 'b', 'c', 'b', 'a', 'c']
    expected_result = ['a', 'b', 'c']
    assert deduplicate_list(original_list) == expected_result
    original_list = ['a', 'b', 'c']
    expected_result = ['a', 'b', 'c']
    assert deduplicate_list(original_list) == expected_result


# Generated at 2022-06-13 16:15:42.910755
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'd', 'c']) == ['a', 'b', 'c', 'd']

# Generated at 2022-06-13 16:15:48.757781
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 1]) == [1, 2]
    assert deduplicate_list([1, 2, 3, 1, 2]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 1, 2, 3]) == [1, 2, 3]


# Generated at 2022-06-13 16:15:54.891382
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
    assert deduplicate_list(['a', 'a', 'c', 'a']) == ['a', 'c']
    assert deduplicate_list(['a', 'a', 'a']) == ['a']
    assert deduplicate_list([]) == []

# Generated at 2022-06-13 16:16:02.769179
# Unit test for function deduplicate_list
def test_deduplicate_list():
    result = deduplicate_list([1,2,2,1,4,4,4,4,4])
    assert result == [1,2,4]
    result = deduplicate_list([1,2,3])
    assert result == [1,2,3]
    result = deduplicate_list([])
    assert result == []
    result = deduplicate_list([1,2,2,1,4,4,4,4,4,1,1,1,1,1,1,1,1])
    assert result == [1,2,4]

# Generated at 2022-06-13 16:16:10.632027
# Unit test for function object_to_dict
def test_object_to_dict():
    class Object:
        def __init__(self):
            self.name = 'object'
            self._private = 'private'
    obj = Object()
    obj_dict = object_to_dict(obj)
    assert obj_dict['name'] == 'object'
    assert 'private' not in obj_dict
    obj_dict = object_to_dict(obj, exclude=['name'])
    assert obj_dict['name'] == 'object'
    assert 'private' not in obj_dict

# Generated at 2022-06-13 16:16:18.875803
# Unit test for function object_to_dict
def test_object_to_dict():
    """ Unit test for object_to_dict
    """
    class test_class():
        def __init__(self):
            self.test_a = 'a'
            self.test_b = 'b'
            self.test_c = 'c'

    new_obj = test_class()

    obj_dict = object_to_dict(new_obj)
    assert 'test_a' in obj_dict.keys()
    assert 'test_b' in obj_dict.keys()
    assert 'test_c' in obj_dict.keys()


# Generated at 2022-06-13 16:16:29.095481
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObj():
        def __init__(self):
            pass
        name = 'test'
        id = None
        alt = 1
        alt2 = True

    m = TestObj()
    # Test excludes
    _dict = object_to_dict(m, exclude=['alt', 'alt2'])
    assert 'alt' not in _dict
    assert 'alt2' not in _dict
    # Test includes
    _dict = object_to_dict(m, exclude=['id', 'name'])
    assert 'id' in _dict
    assert 'name' in _dict
    assert _dict['id'] is None
    assert _dict['name'] == 'test'
    # Test including all
    _dict = object_to_dict(m)
    assert 'alt' in _dict

# Generated at 2022-06-13 16:16:32.679991
# Unit test for function object_to_dict
def test_object_to_dict():
    class TestObject:
        foo = 'bar'
        baz = None

    obj = TestObject
    assert 'bar' == object_to_dict(obj)['foo']
    assert None == object_to_dict(obj, exclude=['foo'])['baz']

# Generated at 2022-06-13 16:16:39.556108
# Unit test for function object_to_dict
def test_object_to_dict():
    assert object_to_dict(object()) == {}


# Generated at 2022-06-13 16:16:41.169976
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 2, 1, 3, 4, 2, 1]) == [1, 2, 3, 4]

# Generated at 2022-06-13 16:16:48.431199
# Unit test for function object_to_dict
def test_object_to_dict():
    class sample:
        def __init__(self):
            self.a = None
            self.b = None
            self._c = None
    obj = sample()
    obj.a = 'hello'
    obj.b = 'howdy'
    obj._c = 'whoami'
    d = object_to_dict(obj)
    assert d['a'] == 'hello'
    assert d['b'] == 'howdy'
    assert '_c' not in d
    d = object_to_dict(obj, exclude=['b'])
    assert d['a'] == 'hello'
    assert 'b' not in d
    assert '_c' not in d

# Generated at 2022-06-13 16:16:52.016391
# Unit test for function deduplicate_list
def test_deduplicate_list():
    duplicate_list = ['a', 'a', 'b', 'c', 'b', 'c']
    assert deduplicate_list(duplicate_list) == ['a', 'b', 'c']


# Generated at 2022-06-13 16:16:57.526692
# Unit test for function object_to_dict
def test_object_to_dict():
    obj = object()
    obj.hello = "world"
    obj.world = "hello"
    obj.banana = "apple"

    result = object_to_dict(obj, exclude=['world'])
    assert result['hello'] == 'world'
    assert 'world' not in result


# Generated at 2022-06-13 16:17:01.791137
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.a = 'bcd'
            self.b = 'efg'
            self.t = 'u'
    obj = Test()
    exclude = ['t']
    assert object_to_dict(obj, exclude) == {'a': 'bcd', 'b': 'efg'}

# Generated at 2022-06-13 16:17:07.290062
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 2, 3, 3, 1, 2, 'a', 'a', 'b', 'c', 'b']
    deduplicated_list = deduplicate_list(original_list)
    assert deduplicated_list == [1, 2, 3, 'a', 'b', 'c']



# Generated at 2022-06-13 16:17:18.227915
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self):
            self.foo = 'bar'
            self.john = 'doe'
            self.a = []
            self.b = {}
    res = object_to_dict(Test())
    assert res['foo'] == 'bar'
    assert res['john'] == 'doe'
    assert 'a' not in res
    assert 'b' not in res
    # Test with exclude argument
    res = object_to_dict(Test(), exclude=['foo'])
    assert res['foo'] == 'bar'
    assert res['john'] == 'doe'
    assert 'a' not in res
    assert 'b' not in res


# Generated at 2022-06-13 16:17:23.146163
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 2, 1, 2, 3, 3, 3, 2]) == [1, 2, 3]
    assert deduplicate_list([1, 2, '3', '3', '3', 2, 1]) == [1, 2, '3']

# Generated at 2022-06-13 16:17:30.711566
# Unit test for function deduplicate_list
def test_deduplicate_list():
    list1 = [1, 2, 4, 4]
    list2 = [1, 2, 6, 4, 2, 4]

    list1_output = deduplicate_list(list1)
    list2_output = deduplicate_list(list2)

    if list1_output != [1, 2, 4]:
        raise AssertionError("Output of the deduplicate_list function is invalid, got: {0}".format(list1_output))
    if list2_output != [1, 2, 6, 4]:
        raise AssertionError("Output of the deduplicate_list function is invalid, got: {0}".format(list2_output))

# Generated at 2022-06-13 16:17:47.425330
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = ['banana','apple','cranberry','apple','banana','apple','apple','apple','cranberry','banana']
    expected = ['banana','apple','cranberry']
    assert deduplicate_list(original_list) == expected

# Generated at 2022-06-13 16:17:53.958798
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Tests whether the results of object_to_dict match the expected results.
    """
    from ansible.module_utils.network.juniper.junos import to_text
    from ansible.module_utils.network.juniper.junos import Resource

    # A class to test the function object_to_dict
    class TestResource(object):
        def __init__(self, name='test'):
            self.name = name

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

        def __ne__(self, other):
            return not self == other

    res = TestResource()
    res.name = 'test_name'
    res.name2 = 'test_name2'
    res.name3 = 'test_name3'

# Generated at 2022-06-13 16:18:01.669934
# Unit test for function object_to_dict
def test_object_to_dict():
    class test_object(object):
        test_attr_1 = "test attr 1"
        test_attr_2 = "test attr 2"
        test_attr_3 = "test attr 3"
        def __init__(self):
            self.test_obj_attr_1 = "test obj attr 1"
            self.test_obj_attr_2 = "test obj attr 2"
        def test_method_1(self):
            pass
        def test_method_2(self):
            pass

    obj = test_object()
    result = object_to_dict(obj, exclude=['test_obj_attr_1'])
    assert result['test_obj_attr_2'] == "test obj attr 2"
    assert 'test_attr_2' in result

# Generated at 2022-06-13 16:18:07.876381
# Unit test for function deduplicate_list
def test_deduplicate_list():
    from collections import OrderedDict
    original_list = ['a', 'b', 'a', 'e', 2, 3, 2, 'e']

    assert deduplicate_list(original_list) == ['a', 'b', 'e', 2, 3]
    original_list = list(OrderedDict.fromkeys(original_list))
    assert deduplicate_list(original_list) == ['a', 'b', 'e', 2, 3]



# Generated at 2022-06-13 16:18:16.303006
# Unit test for function deduplicate_list
def test_deduplicate_list():
    import pytest
    assert deduplicate_list([1, 2, 3, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 1, 1, 1]) == [1]
    assert deduplicate_list([1, 2, 3, 4, 5, 1, 2, 3]) == [1, 2, 3, 4, 5]
    assert deduplicate_list([]) == []


# Generated at 2022-06-13 16:18:23.963373
# Unit test for function deduplicate_list
def test_deduplicate_list():
    ids = [1, 1, 1, 2, 2, 3, 3, 4, 4]
    ids2 = deduplicate_list(ids)
    assert ids2 == [1, 2, 3, 4]
    ids3 = [1, 2, 3, 4]
    ids4 = deduplicate_list(ids3)
    assert ids4 == [1, 2, 3, 4]


# Generated at 2022-06-13 16:18:34.593626
# Unit test for function object_to_dict
def test_object_to_dict():
    from collections import namedtuple
    Obj = namedtuple('Obj', 'a b c')
    testbool = True
    testlist = [1,2,3,4]
    testtuple = (1,2,3,4)
    testdict = {'a':1,'b':2,'c':3}
    testobj = Obj(a=1,b=2,c=3)
    assert object_to_dict(testbool) == {'__module__': '__main__', '__qualname__': 'testbool'}
    assert object_to_dict(testlist) == {'__module__': '__main__', '__qualname__': 'testlist'}

# Generated at 2022-06-13 16:18:40.006611
# Unit test for function object_to_dict
def test_object_to_dict():
    """
    Tests the object_to_dict function by creating a test object and a dictionry from the object,
    then compares the dictionaries.
    """
    class TestObject(object):
        hello = 'world'
        testing = [1, 2, 3]

    test_obj = TestObject()
    test_dict = {'hello': 'world', 'testing': [1, 2, 3]}
    assert object_to_dict(test_obj) == test_dict



# Generated at 2022-06-13 16:18:44.801757
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1,1,2,3,2]
    expected_list = [1,2,3]
    assert expected_list == deduplicate_list(original_list)

# Generated at 2022-06-13 16:18:51.006834
# Unit test for function object_to_dict
def test_object_to_dict():
    example_dict = {
        'name': 'test',
        'value': 'test',
        'secret': 'test',
    }

    class example_class(object):
        def __init__(self, name, value):
            self.name = name
            self.value = value

    example_object = example_class('test', 'test')
    example_object.secret = 'test'

    assert example_dict == object_to_dict(example_object, ['secret'])


# Generated at 2022-06-13 16:19:21.265967
# Unit test for function object_to_dict
def test_object_to_dict():
    x = {'foo': 'bar'}
    assert object_to_dict(x) == x



# Generated at 2022-06-13 16:19:24.960222
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([3,3,3,3,3,3,3,3,3,3,3]) == [3]
    assert deduplicate_list([1,1,2,2,3,3]) == [1, 2, 3]
    assert deduplicate_list([1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2]) == [1, 2]

# Generated at 2022-06-13 16:19:30.034558
# Unit test for function object_to_dict
def test_object_to_dict():
    class test(object):
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self.c = 'c'
            _d = 'd'
    a = test()
    b = object_to_dict(a)
    assert 'a' in b
    assert 'b' in b
    assert 'c' in b
    assert 'd' not in b

# Generated at 2022-06-13 16:19:33.266655
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['one', 'two', 'three', 'one', 'two']) == ['one', 'two', 'three']
    assert deduplicate_list([]) == []
    assert deduplicate_list(['  ']) == ['  ']
    assert deduplicate_list(['one', ' ', 'two', 'two', ' ', 'one']) == ['one', ' ', 'two']

# Generated at 2022-06-13 16:19:35.647829
# Unit test for function deduplicate_list
def test_deduplicate_list():
    original_list = [1, 1, 2, 3, 3, 3]
    assert deduplicate_list(original_list) == [1, 2, 3]

# Generated at 2022-06-13 16:19:39.333471
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list([1, 2, 3, 1, 2, 4]) == [1, 2, 3, 4]
    assert deduplicate_list([[1], [2], [1], [2]]) == [[1], [2]]


# Generated at 2022-06-13 16:19:47.019898
# Unit test for function object_to_dict
def test_object_to_dict():
    class MyObj(object):
        a = 'A'
        b = 'B'
        _c = 'C'
        def __init__(self):
            self.d = 'D'
            self._e = 'E'
    obj = MyObj()
    result = object_to_dict(obj)
    assert('a' in result)
    assert('b' in result)
    assert('c' not in result)
    assert('C' not in result)
    assert('d' in result)
    assert('e' not in result)
    assert('E' not in result)

    result = object_to_dict(obj, ['d'])
    assert('a' in result)
    assert('b' in result)
    assert('c' not in result)
    assert('C' not in result)

# Generated at 2022-06-13 16:19:51.534519
# Unit test for function deduplicate_list
def test_deduplicate_list():
    test_list = [1, 2, 3, 4, 1, 2, 3, 5, 6, 1, 3, 5, 7, 3, 4, 5, 9]
    deduplicated_list = deduplicate_list(test_list)
    assert deduplicated_list == [1, 2, 3, 4, 5, 6, 7, 9]

# Generated at 2022-06-13 16:19:54.819615
# Unit test for function deduplicate_list
def test_deduplicate_list():
    assert deduplicate_list(['a', 'b', 'c', 'd', 'c', 'a']) == ['a', 'b', 'c', 'd']
    assert deduplicate_list(['a', 'c', 'b', 'c', 'a', 'd']) == ['a', 'c', 'b', 'd']
    assert deduplicate_list([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert deduplicate_list([1, 2, 3, 3, 3, 3, 1, 2, 3, 3]) == [1, 2, 3]

# Generated at 2022-06-13 16:19:58.530879
# Unit test for function object_to_dict
def test_object_to_dict():
    class Test(object):
        def __init__(self, name, description):
            self.name = name
            self.description = description
            self.dontshow = 'hidden'

    obj = Test('test', 'description')
    obj_dict = object_to_dict(obj, ['dontshow'])

    assert obj_dict == {
        "name": 'test',
        "description": 'description',
    }