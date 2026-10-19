

# Generated at 2022-06-22 11:50:50.251277
# Unit test for function max
def test_max():
    assert 3 == max((1, 2, 3))
    assert 3 == max([1, 2, 3])
    assert 3 == max({'b': 1, 'c': 2, 'a': 3})
    assert 3 == max({'b': 1, 'c': 3, 'a': 2}.values())
    assert 3 == max(x for x in [1, 2, 3])
    assert 3 == max(set([1, 2, 3]))

    try:
        max()
    except TypeError:
        pass
    else:
        raise AssertionError("max() of no arguments should raise a TypeError")

    try:
        max("a", "b", "c")
    except TypeError:
        pass
    else:
        raise AssertionError("max() of string arguments should raise a TypeError")


# Generated at 2022-06-22 11:50:59.667564
# Unit test for function max
def test_max():
    assert max([1, 2, 3, 4]) == 4
    assert max([1, 2, 4, 3]) == 4
    assert max([4, 2, 3, 1]) == 4
    assert max([-1, -2, -3, -4]) == -1
    assert max([-4, -3, -2, -1]) == -1
    assert max([1]) == 1
    assert max([2]) == 2
    assert max([-1]) == -1
    assert max([0]) == 0
    assert max([]) == None



# Generated at 2022-06-22 11:51:10.688781
# Unit test for function inversepower
def test_inversepower():
    # Testing math.sqrt
    assert inversepower(16) == 4
    # Testing math.pow
    assert round(inversepower(27, 3), 7) == 3
    # Testing if it raises TypeError
    try:
        inversepower('12', '3')
        inversepower('12', 3)
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError('inversepower did not raise AnsibleFilterTypeError')
    # Testing if it raises ValueError
    try:
        inversepower(27, 0.5)
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError('inversepower did not raise AnsibleFilterTypeError')



# Generated at 2022-06-22 11:51:20.550578
# Unit test for function inversepower
def test_inversepower():
    assert math.sqrt(2) == inversepower(2)
    assert math.sqrt(2) == inversepower(2, 2)
    assert math.pow(2, 1.0/3.0) == inversepower(2, 3)
    assert math.pow(2, 1.0/3.0) == inversepower(2, 3.0)
    assert math.sqrt(4) == inversepower(4.0)
    assert math.sqrt(4.0) == inversepower(4.0, 2)
    assert math.pow(4, 1.0/3.0) == inversepower(4, 3)
    assert math.pow(4.0, 1.0/3.0) == inversepower(4.0, 3.0)


# Generated at 2022-06-22 11:51:24.591905
# Unit test for function max
def test_max():
    assert max([10, 7, 5]) == 10
    assert max(['10', '7', '5']) == '7'
    assert max([[10, 5], [3, 4]]) == [10, 5]


# Generated at 2022-06-22 11:51:35.629259
# Unit test for function human_to_bytes
def test_human_to_bytes():
    def assert_eq(x,y):
        if not x == y:
            raise Exception("Expected: %s; Received: %s" % (x,y))
    assert_eq(human_to_bytes('10b'), 10)
    assert_eq(human_to_bytes('10B'), 10)
    assert_eq(human_to_bytes('10'), 10)
    assert_eq(human_to_bytes('10k'), 10000)
    assert_eq(human_to_bytes('10K'), 10000)
    assert_eq(human_to_bytes('10kb'), 10000)
    assert_eq(human_to_bytes('10kib'), 10000)
    assert_eq(human_to_bytes('10kb', default_unit='k'), 10000)

# Generated at 2022-06-22 11:51:48.575615
# Unit test for function min
def test_min():
    assert min([1,2,3,4,5]) == 1
    assert min([5,4,3,2,1]) == 1
    assert min([1,3,5,2,4]) == 1
    assert min([1,1,1,1,1]) == 1
    assert min([[1,1,1], [2,2,2], [1,1,1]]) == [1,1,1]
    assert min(['b', 'a', 'c']) == 'a'
    assert min(['b', 'a', 'c'], attribute='upper') == 'A'
    assert min(['b', 'a', 'c'], case_sensitive=False) == 'a'
    assert min(['b', 'a', 'c'], case_sensitive=False, attribute='upper') == 'A'


# Generated at 2022-06-22 11:51:55.962150
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(16) == math.log(16)
    assert logarithm(16, 4) == math.log(16, 4)
    assert logarithm(16, 10) == math.log10(16)
    assert logarithm(16, math.e) == math.log(16)

    failed = False
    error = None
    try:
        logarithm("hello")
    except AnsibleFilterError as e:
        failed = True
        error = to_text(e)

    assert failed
    assert "can only be used on numbers" in error


# Generated at 2022-06-22 11:52:08.047880
# Unit test for function max
def test_max():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import MagicMock, patch

    # Test the iteration over a list
    mock_env = MagicMock()
    mock_env.filters = FilterModule().filters()
    mock_env.tests = {}
    mock_env.globals = {}

    test_max = mock_env.filters['max']
    lst = [1, 2, 3]
    assert test_max(mock_env, lst) == 3

    # Test the iteration over a dictionary
    mock_env = MagicMock()
    mock_env.filters = FilterModule().filters()
    mock_env.tests = {}
    mock_env.globals = {}

    test_max = mock_env.filters['max']

# Generated at 2022-06-22 11:52:19.580173
# Unit test for function min
def test_min():
    # NOTE: We don't do a straight assertEqual here because the values may be of different types.
    # TODO: Convert this to pytest parametrized tests
    assert min([1, 6, 2]) == 1, "min([1, 6, 2]) should return 1"
    assert min(1, 6, 2) == 1, "min(1, 6, 2) should return 1"
    assert min((1, 6, 2)) == 1, "min((1, 6, 2)) should return 1"
    assert min([[1], [6], [2]]) == [1], "min([[1], [6], [2]]) should return [1]"

# Generated at 2022-06-22 11:52:31.071963
# Unit test for function min
def test_min():
    values = [1, 2, 3, 4, 5]

    # Test that valid inputs are accepted
    ret = min(values)

    assert ret == 1

    # Test that invalid inputs raise an error
    try:
        # Tuples don't have a schema
        min((1, 2, 3))
        assert False
    except AnsibleFilterTypeError:
        assert True

    try:
        # Strings don't have a schema
        min(('a', 'b', 'c'))
        assert False
    except AnsibleFilterTypeError:
        assert True



# Generated at 2022-06-22 11:52:34.888750
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([1, 5, 2, 3]) == 1
    assert min([5, 1, 4, 2, 3]) == 1
    assert min([1.1, 1.2, 1.3]) == 1.1
    assert min(["a", "b", "c"]) == "a"
    assert min(["c", "b", "a"]) == "a"
    assert min("abc") == "a"
    assert min({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == 1

# Generated at 2022-06-22 11:52:36.335703
# Unit test for function min
def test_min():
    assert 0 == min([0, 1, 2])
    assert 'a' == min(['b', 'a', 'c'])

# Generated at 2022-06-22 11:52:49.653750
# Unit test for function unique
def test_unique():
    assert unique(['a', 'b', 'b']) == ['a', 'b']
    assert unique([1, 2, 3, 3]) == [1, 2, 3]
    assert unique([1, '1']) == [1, '1']
    assert unique([[1, 1], [1, 2]]) == [[1, 1], [1, 2]]

    # Test for keyword arguments
    assert unique(['a', 'A'], case_sensitive=True) == ['a', 'A']
    assert unique(['a', 'A'], case_sensitive=False) == ['a']

    # Test that attribute filter can work on unique filter and doesn't throw errors
    assert unique([{'a': 1}, {'a': 2}], attribute='a') == [{'a': 1}, {'a': 2}]

    # Test

# Generated at 2022-06-22 11:52:52.243666
# Unit test for function min
def test_min():
    assert min([5, 0, -1, 2, 6]) == -1
    assert min(['b', 'a', 'z']) == 'a'


# Generated at 2022-06-22 11:53:04.745603
# Unit test for function rekey_on_member
def test_rekey_on_member():
    # Setup
    data = [{'key1': 'value1', 'key2': 'value2'},
            {'key1': 'value3', 'key2': 'value4'}]
    key = 'key1'

    # Test: existing key, list of dict
    rekeyed_data = rekey_on_member(data, key)
    assert type(rekeyed_data) is dict
    assert len(rekeyed_data) == len(data)
    assert data[0] == rekeyed_data['value1']
    assert data[1] == rekeyed_data['value3']

    # Test: non_existing key, list of dict

# Generated at 2022-06-22 11:53:15.700621
# Unit test for function rekey_on_member
def test_rekey_on_member():
    x = [{'name': 'foo', 'key': 'value', "nested": {"val": [1, 2, 3]}},
         {'name': 'bar', 'key2': 'value2', "nested": {"val": [4, 5, 6]}},
         {'name': 'baz', 'key3': 'value3', "nested": {"val": [7, 8, 9]}}]


# Generated at 2022-06-22 11:53:27.553225
# Unit test for function min
def test_min():
    # Test normal execution
    assert min([0, 5, 4, 1]) == 0
    assert min([1, 5, 4, 1]) == 1
    assert min([2, 5, 4, 1]) == 1
    assert min([3, 5, 4, 1]) == 1
    assert min([4, 5, 4, 1]) == 1
    assert min([5, 5, 4, 1]) == 1
    assert min([5, 5, 4, 0]) == 0

    # Test if it is working with keyword arguments
    assert min([0, 5, 4, 1], key=lambda x: -x) == 5
    assert min([0, 5, 4, 1], key=lambda x: x) == 0
    assert min([0, 5, 4, 1], key=lambda x: x, foo='bar') == 0

    # Test it raises an

# Generated at 2022-06-22 11:53:34.077689
# Unit test for function max
def test_max():
    _max = __builtins__.get('max')
    assert max([1, 2, 3]) == _max([1, 2, 3])
    assert max([1, 2, 3], [1, 2, 3]) == _max([1, 2, 3], [1, 2, 3])
    assert max([1, 2, 3], 5) == _max([1, 2, 3], 5)
    assert max("abc", "xyz") == _max("abc", "xyz")


# Generated at 2022-06-22 11:53:39.421453
# Unit test for function symmetric_difference
def test_symmetric_difference():
    f = FilterModule()
    test1 = f.filters()['symmetric_difference']([1,2,3,4,5], [3,4,5,6,7])
    test2 = f.filters()['symmetric_difference']([1,2,3], [3,4,5])
    assert test1 == test2 == [1, 2, 6, 7]

# Generated at 2022-06-22 11:53:57.644058
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min((1, 2, 3, 4)) == 1
    assert min({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == 1
    assert min({1, 2, 3, 4}) == 1
    assert min(1, 2, 3, 4) == 1
    assert min(x for x in range(5)) == 0
    assert min([1, 2, 3, 4], default=0) == 1
    assert min([], default=0) == 0
    assert min(iter((1, 2, 3, 4)), default=0) == 1
    assert min(iter([]), default=0) == 0
    assert min([1, 2, 3, 4], key=str) == 1

# Generated at 2022-06-22 11:54:09.447904
# Unit test for function symmetric_difference
def test_symmetric_difference():
    try:
        from unittest import TestCase
    except ImportError:
        from ansible.module_utils.unittest import TestCase

    class Test(TestCase):

        def test_hashable(self):
            self.assertEqual(symmetric_difference([1, 2, 3], [2, 3, 4]), [1, 4])

        def test_not_hashable(self):
            self.assertEqual(symmetric_difference([[1], [2], [3]], [[2], [3], [4]]), [[1], [4]])
            self.assertEqual(symmetric_difference([[1], [2], [3]], [[3], [4]]), [[1], [2], [4]])

    test = Test()
    test.test_hashable()
    test

# Generated at 2022-06-22 11:54:12.197531
# Unit test for function max
def test_max():
    test_values = [1, 2, 3, 4, 5]
    assert max(test_values) == 5

# Generated at 2022-06-22 11:54:14.977065
# Unit test for function max
def test_max():
    arg = [1, 2, 3, 4, -3, -1]
    env = {}
    res = max(env, arg)
    assert res == 4


# Generated at 2022-06-22 11:54:23.264497
# Unit test for function max
def test_max():
    from ansible.compat.tests.mock import patch, MagicMock

    import __builtin__

    with patch('__builtin__.max') as builtin:
        builtin.return_value = 5
        assert max(None, [1, 2, 3, 4, 5]) == 5

        # Test keyword args
        builtin.side_effect = TypeError
        assert max(None, [{'value': 1}, {'value': 5}], key=lambda x: x['value']) == {'value': 5}



# Generated at 2022-06-22 11:54:27.978530
# Unit test for function max
def test_max():
    # Test list of strings
    assert max(["hola", "hello", "bonjour"]) == "hola"
    # Test list of integers
    assert max([1, 7, 8]) == 8
    # Test list of mixed types
    assert max([1, "hello", 7]) == "hello"

# Test function min

# Generated at 2022-06-22 11:54:39.683857
# Unit test for function max
def test_max():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    import ansible.constants as C
    import ansible.errors
    import json


    class ResultCallback(CallbackBase):
        """A sample callback plugin used for performing an action as results come in

        If you want to collect all results into a single object for processing at
        the end of the execution, look into utilizing the ``json`` callback plugin
        or writing your own custom callback plugin
        """
        def __init__(self):
            super(ResultCallback, self).__init__()


# Generated at 2022-06-22 11:54:50.898379
# Unit test for function unique
def test_unique():
    filter_module = FilterModule()

    def run(value, case_sensitive=True, attribute=None):
        # We want to test the filter function itself, not the wrapper
        env = None

        # Note that we must convert case_sensitive to a bool because Jinja2
        # will pass it as a string.
        ret = filter_module.filters()['unique'](env, value, case_sensitive=case_sensitive, attribute=attribute)

        if isinstance(value, Iterable):
            return type(value)(ret)
        else:
            return ret

    assert run([]) == []
    assert run([1, 2, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert run([1, 2, 1, 2, 1, 2]) == [1, 2]

# Generated at 2022-06-22 11:54:58.730343
# Unit test for function max
def test_max():
    # Test when we don't have Jinja2's version of the function
    assert max(None, [4, 5, 6]) == 6
    assert max(None, [6, 5, 4]) == 6
    assert max(None, [5, 6, 4]) == 6
    assert max(None, [5, 10, 4, 9]) == 10

    assert max(None, [4, 5, 6], attribute='name') == 6
    assert max(None, [6, 5, 4], attribute='name') == 6
    assert max(None, [5, 6, 4], attribute='name') == 6
    assert max(None, [5, 10, 4, 9], attribute='name') == 10

    # Test when we have Jinja2's version of the function

# Generated at 2022-06-22 11:55:09.809728
# Unit test for function max
def test_max():
    assert max([1, 2, 3, 4, 5]) == 5
    assert max([1.1, 1.2, 1.3, 1.4, 1.5]) == 1.5
    assert max(['a', 'b', 'c', 'd', 'e']) == 'e'
    assert max('abcde') == 'e'
    assert max(['a', 'b', 'c', 'd', 'e'], key=lambda x: x.upper()) == 'd'
    assert max(['a', 'B', 'c', 'D', 'e'], key=lambda x: x.upper()) == 'e'
    assert max(['a', 'B', 'c', 'D', 'e'], key=lambda x: x.lower()) == 'a'

# Generated at 2022-06-22 11:55:22.973068
# Unit test for function rekey_on_member
def test_rekey_on_member():
    test_dict = {'a_1': {'a': 1, 'b': '2'}, 'a_2': {'a': 2, 'b': 2}, 'a_3': {'a': 3, 'b': 2},
                 'a_4': {'a': 4, 'b': 3}}
    print(rekey_on_member(test_dict, 'b'))

# test_rekey_on_member()

# Generated at 2022-06-22 11:55:34.858198
# Unit test for function max
def test_max():
    module = AnsibleModule(
        argument_spec={
            'a': dict(type='list', elements='int'),
            'b': dict(type='list', elements='int'),
            'kwargs': dict(type='dict')
        },
    )
    result = module.run_command('max', a=module.params['a'], b=module.params['b'],
                                kwargs=module.params['kwargs'])
    assert result[1] == 0, result[2]
    assert result[0] == 7

    result = module.run_command('max', a=module.params['b'], kwargs=module.params['kwargs'])
    assert result[1] == 0, result[2]
    assert result[0] == 7



# Generated at 2022-06-22 11:55:44.016923
# Unit test for function rekey_on_member
def test_rekey_on_member():
    data = {
        'first_item': {
            'foo': 'bar',
            'name': 'first_item'
        },
        'second_item': {
            'foo': 'baz',
            'name': 'second_item'
        }
    }

# Generated at 2022-06-22 11:55:44.647282
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import doctest
    doctest.testmod()

# Generated at 2022-06-22 11:55:56.141768
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from ansible.tests.unit import AnsibleModuleTestCase


# Generated at 2022-06-22 11:56:00.277178
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([4, 3, 2, 1]) == 1
    assert min([1, 2, 4, 3]) == 1
    assert min([1]) == 1



# Generated at 2022-06-22 11:56:10.028886
# Unit test for function human_to_bytes
def test_human_to_bytes():

    assert(human_to_bytes('1k') == 1024)
    assert(human_to_bytes('1M') == 1048576)
    assert(human_to_bytes('1G') == 1073741824)
    assert(human_to_bytes('1T') == 1099511627776)

    assert(human_to_bytes('1K') == 1024)
    assert(human_to_bytes('1m') == 1048576)
    assert(human_to_bytes('1g') == 1073741824)
    assert(human_to_bytes('1t') == 1099511627776)

    assert(human_to_bytes('1kB') == 1000)
    assert(human_to_bytes('1MB') == 1000000)
    assert(human_to_bytes('1GB') == 1000000000)

# Generated at 2022-06-22 11:56:21.909760
# Unit test for function rekey_on_member
def test_rekey_on_member():
    assert rekey_on_member({}, 'key') == {}
    assert rekey_on_member([], 'key') == {}

    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member({}, '')
    assert "At least one of the positional arguments 'data' and 'key' is undefined, did you use '|'-separator" \
           " when using the key?" in to_text(excinfo.value)

    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member('', 'key')
    assert "Type is not a valid list, set, or dict" in to_text(excinfo.value)


# Generated at 2022-06-22 11:56:31.246935
# Unit test for function max
def test_max():
    assert max([1, 2]) == 2
    assert max((1, 2)) == 2
    assert max({1, 2}) == 2
    assert max({'a': 1, 'b': 2}, 'b') == 2
    assert max([]) is None
    assert max(()) is None
    assert max({}) is None
    try:
        max({}, 'b')
        assert False, "Expected exception"
    except AnsibleFilterTypeError:
        pass
    try:
        max([], 'b')
        assert False, "Expected exception"
    except AnsibleFilterTypeError:
        pass
    try:
        max([1, 'b'])
        assert False, "Expected exception"
    except AnsibleFilterTypeError:
        pass
    assert max([1], default=2) == 1

# Generated at 2022-06-22 11:56:37.129561
# Unit test for function min
def test_min():
    f = FilterModule()
    filters = f.filters()
    assert filters['min']([1, 2, 3]) == 1
    assert filters['min']([1, 2, 3, 4], 3) == 3
    assert filters['min']([1, 2, 3, 4], key=abs) == 1
    assert filters['min']([-1, -2, -3, -4], key=abs) == -1


# Generated at 2022-06-22 11:56:50.898154
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([3, 2, 1]) == 1
    assert min([-1, -2, -3]) == -3
    assert min([-2, -1, 0, 1, 2]) == -2
    assert min((1, 2, 3)) == 1
    assert min((3, 2, 1)) == 1
    assert min((-1, -2, -3)) == -3
    assert min((-2, -1, 0, 1, 2)) == -2



# Generated at 2022-06-22 11:56:52.818283
# Unit test for function max
def test_max():
    assert max(1,2) == 2
    assert max(1,2,3) == 3

# Generated at 2022-06-22 11:56:59.633678
# Unit test for function unique

# Generated at 2022-06-22 11:57:09.148051
# Unit test for function unique
def test_unique():
    # TODO: use Ansible's proper unit testing framework

    def run_test(arr, case_sensitive=None, attribute=None):
        env = {}
        arr_in = [x.copy() for x in arr]
        arr_out = unique(env, arr_in, case_sensitive, attribute)
        print('In:')
        print(arr_in)
        print('Out:')
        print(arr_out)
        return all([x in arr_in for x in arr_out])


# Generated at 2022-06-22 11:57:13.500877
# Unit test for function max
def test_max():
    test_vec = [(-10, 2, 3, 4, 10, 0, -20, 10), (2, 3, 4, 10, 0, -20, 10, -10), (3, 4, 10, 0, -20, 10, -10, 2)]
    for test_vec_i in test_vec:
        assert max(test_vec_i) == 10

# Generated at 2022-06-22 11:57:18.552807
# Unit test for function max
def test_max():
    assert max(list(range(10))) == 9
    assert max([[1, 2, 3], [4, 5, 6]]) == [4, 5, 6]
    assert max([[1, 2, 3], [4, 5, 6]], attr='sum') == [4, 5, 6]


# Generated at 2022-06-22 11:57:29.860967
# Unit test for function max
def test_max():
    obj = FilterModule()
    filters = obj.filters()
    max_filter = filters['max']

    # basic tests
    assert max_filter([5, 2, 8]) == 8
    assert max_filter(['ansible', 'python', 'automation']) == 'python'
    assert max_filter([5, 2, 'invalid']) == 5

    # test max() with duplicate values
    assert max_filter([10, 10, 5]) == 10
    assert max_filter([10, 5, 10]) == 10
    assert max_filter([5, 10, 10]) == 10

    # test max() with multiple arguments
    assert max_filter(10, 5) == 10
    assert max_filter(5, 10) == 10
    assert max_filter(5, 10) == 10

# Generated at 2022-06-22 11:57:35.844143
# Unit test for function unique
def test_unique():
    assert unique([1, 1]) == [1]
    assert unique([1, 2, 1]) == [1, 2]
    assert unique([1, {'key': 'value'}, {'key': 'value'}]) == [1, {'key': 'value'}]
    assert unique((1, 1)) == [1]
    assert unique((1, 2, 1)) == [1, 2]
    assert unique(['a', 'A']) == ['a', 'A']
    assert unique(['a', 'A'], case_sensitive=False) == ['a']
    assert unique(['a', 'a', 'b'], case_sensitive=False) == ['a', 'b']
    assert unique([1, 1], attribute='attr') == [1]



# Generated at 2022-06-22 11:57:46.539033
# Unit test for function rekey_on_member
def test_rekey_on_member():
    '''
    unit test for rekey_on_member()
    '''
    import ansible.utils.template as template
    jenv = template.AnsibleJ2TemplateEnvironment()

    # A regular test
    test_dict = [
        {'a': 'a', 'b': 'b'},
        {'a': 'c', 'b': 'd'},
        {'a': 'e', 'b': 'f'},
    ]
    assert jenv.from_string('{{ test_dict | rekey_on_member("b") | list }}').render(test_dict=test_dict) == \
           '[{\'b\': \'b\'}, {\'b\': \'d\'}, {\'b\': \'f\'}]'

    # A test on an empty dict
    test_dict = {}

# Generated at 2022-06-22 11:57:53.278991
# Unit test for function unique

# Generated at 2022-06-22 11:57:59.676150
# Unit test for function min
def test_min():
    from jinja2 import Environment
    env = Environment()
    for i in [[4, 6, 2, 1], ['foo', 'bar', 'a', 'xyz']]:
        assert env.from_string('{{ arr|min }}').render(arr=i) == min(i)



# Generated at 2022-06-22 11:58:04.629637
# Unit test for function max
def test_max():
    assert max([-1, 0, 1, 2, -2]) == 2
    assert max([1]) == 1
    assert max([]) is None
    assert max([[1, 2, 3], [3, 2, 1], [2, 3, 1]]) == [3, 2, 1]
    assert max([[1, 2], [1, 3], [1, 4]]) == [1, 4]


# Generated at 2022-06-22 11:58:10.370684
# Unit test for function max
def test_max():
    fm = FilterModule()
    environment = {}
    filter_func = fm.filters()['max']
    assert filter_func(environment, [3, 1, 4, 1, 5, 9]) == 5
    assert filter_func(environment, [3, 1, 4, 1, None, 9]) is None
    assert filter_func(environment, [3, 1.5, 4, 1.5, None, 9]) == 4
    assert filter_func(environment, [3, 1.5, 4, 1.5, None, 9], attribute='real') == 4.0
    assert filter_func(environment, [3, 1.5, 4j, 1.5, None, 9]) == 4j

# Generated at 2022-06-22 11:58:15.437555
# Unit test for function max
def test_max():
    assert(max([1,2,3]) == 3)
    assert(max(1,2,3) == 3)
    assert(max([[1,3], [2,3]]) == [2,3])
    assert(max([[1,3], [2,2]]) == [1,3])
    assert(max([[1,3], [2,2]], key=lambda x:x[1]) == [2,2])
    assert(max([[1,3], [2,2]], key=lambda x:x[0]) == [2,2])


# Generated at 2022-06-22 11:58:17.065193
# Unit test for function min
def test_min():
    assert 2 == min([2, 3, 1])


# Generated at 2022-06-22 11:58:29.248143
# Unit test for function max
def test_max():
    from jinja2 import Environment
    from ansible.template import filters

    env = Environment()
    f = filters.FilterModule()
    env.filters.update(f.filters())
    template = env.from_string('{{ [3, 5, 1, 2, 4] | max }}')
    assert template.render() == '5'

    template = env.from_string('{{ [3, 5, 1, 2, 4] | max(attribute="length")}}')
    assert template.render() == '3'

    template = env.from_string('{{ [3, 5, 1, 2, 4] | max(attribute="length", reverse=True)}}')
    assert template.render() == '1'


# Generated at 2022-06-22 11:58:30.884656
# Unit test for function min
def test_min():
    assert 2 == min([1, 2, 3])



# Generated at 2022-06-22 11:58:33.605301
# Unit test for function min
def test_min():
    assert min(1, 2) == 1
    assert min([3, 4]) == 3
    assert min(['a', 'b']) == 'a'
    assert min('cde') == 'c'


# Generated at 2022-06-22 11:58:45.155792
# Unit test for function rekey_on_member
def test_rekey_on_member():
    assert rekey_on_member([{'a': 1}, {'b': 1}, {'a': 2}], 'a', duplicates='error') == {1: {'a': 1}, 2: {'a': 2}}
    assert rekey_on_member([{'a': 1}, {'b': 1}, {'a': 2}], 'b', duplicates='error') == {1: {'b': 1}}

    assert rekey_on_member([{'a': 1}, {'b': 1}, {'a': 2}], 'a', duplicates='overwrite') == {1: {'b': 1}, 2: {'a': 2}}

# Generated at 2022-06-22 11:58:48.376204
# Unit test for function max
def test_max():
    assert 600 == max([[1, 2, 3, 4, 5, 6], 200, 300, [400, 500], 600])


# Generated at 2022-06-22 11:58:54.789868
# Unit test for function max
def test_max():
    assert max(range(1, 10)) == 9

# Generated at 2022-06-22 11:59:00.622990
# Unit test for function max
def test_max():
    x = 5
    y = 3

    assert __builtins__['max'](x, y) == 5

    x = {'a': 5}
    y = {'a': 3}

    assert __builtins__['max'](x, y, key=lambda v: v['a'])['a'] == 5


# Generated at 2022-06-22 11:59:12.204330
# Unit test for function max
def test_max():
    assert max([1, 2]) == 2
    assert max((1, 2)) == 2
    assert max(1, 2) == 2

    assert max([1, 2, 3], [5, 2, 3]) == [5, 2, 3]
    assert max((1, 2, 3), (5, 2, 3)) == (5, 2, 3)
    assert max([1, 2, 3], (5, 2, 3)) == (5, 2, 3)
    assert max((1, 2, 3), [5, 2, 3]) == [5, 2, 3]
    assert max(1, 2, 3, 5, 2, 3) == 5

    assert max([1, 2], key=lambda x: -x) == 1
    assert max((1, 2), key=lambda x: -x) == 1

# Generated at 2022-06-22 11:59:13.404885
# Unit test for function max
def test_max():
    module = FilterModule()
    assert module.filters()['max']([1, 2, 3, 4, 5]) == 5



# Generated at 2022-06-22 11:59:24.552082
# Unit test for function unique
def test_unique():
    from ansible.utils import raisewithtb
    from ansible.compat.tests import unittest
    from ansible.vars import combinevars
    from ansible.template import Templar

    class TestTemplar(unittest.TestCase):
        def setUp(self):
            self.loader = DictDataLoader({'/path/to/file.yaml': """
            ---
            key: value
            """})
            self.inventory = InventoryManager(loader=self.loader, sources='localhost,')
            self.variable_manager = VariableManager(self.inventory)

# Generated at 2022-06-22 11:59:25.997071
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([3, 2, 1]) == 1


# Generated at 2022-06-22 11:59:32.766406
# Unit test for function max
def test_max():
    assert max(range(10)) == 9
    assert max(range(1, 11)) == 10
    assert max(range(1, 10, 2)) == 9
    assert max([-1, 2, 3, -2]) == 3
    assert max("aAbByYzZ") == "z"
    assert max(["a", "A", "b", "B", "y", "Y", "z", "Z"]) == "z"
    assert max(["a", "A", "b", "B", "y", "Y", "z", "Z"], key=str.lower) == "z"
    assert max('alabama', 'alaska', 'colorado', 'arizona') == 'colorado'

# Generated at 2022-06-22 11:59:42.769687
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([-5, 1, 4, 8]) == -5
    assert min([-5, 1.9, 4, 8]) == -5
    assert min(['a', 'b', 'c']) == 'a'
    assert min(['a', 'bc', 'def'], key=len) == 'a'
    assert min(['a', 'bc', 'def'], key=len, default='!') == 'a'

    assert min(['a', 'bc', 'def'], default='!') == '!', "if no 'key' is provided, min() should return the default"
    assert min([], default='!') == '!', "if the sequence is empty, min() should return the default"

# Generated at 2022-06-22 11:59:53.289455
# Unit test for function min
def test_min():
    from ansible.module_utils._text import to_text
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestMin(unittest.TestCase):
        def setUp(self):
            self.mock_display = patch.object(Display, 'display')
            self.mock_display.start()

        def tearDown(self):
            self.mock_display.stop()

        def test_as_filter_no_kwargs(self):
            env = {}
            min_filter = min.as_filter(env)
            result_string = min_filter(['b', 'a', 'c'])
            self.assertEqual(to_text(result_string), to_text('a'))
            result_number = min_filter

# Generated at 2022-06-22 12:00:01.846619
# Unit test for function rekey_on_member
def test_rekey_on_member():
    """
    Direct unit test for function rekey_on_member

    Note: This test has a dependency on python3-future, Python 2.7 is not supported here.
    """
    from __future__ import print_function

    import sys

    import pytest

    from ansible.utils import context_objects as co
    from ansible.module_utils import basic

    # Create the Ansible context objects which will be needed. These are normally created by
    # the AnsibleEngine and available via templating, but for unit tests we create them manually
    ansible_vars_mock = dict(foo=1, bar=5, baz=999)
    ansible_facts_mock = dict(bar=30, baz=60)

    # Create the AnsibleContext for the test
    module_args_mock = dict()
    ansible

# Generated at 2022-06-22 12:00:13.366729
# Unit test for function min
def test_min():
    assert 3 == min([3, 1, 4, 1, 5])
    assert -3 == min([3, -3, 4, -3, 5])
    assert 0 == min([-3, -1, -4, -1, -5])


# Generated at 2022-06-22 12:00:26.244226
# Unit test for function max
def test_max():
    assert max([1,2,3]) == 3
    assert max(1,2,3) == 3
    assert max([x for x in range(10)]) == 9
    assert max([x for x in range(10)], initial=0) == 9
    assert max([x for x in range(10)], attribute='real') == 9
    assert max([-1.2, -2.3, -3.4]) == -1.2
    assert max([-1.2, 2.3, -3.4]) == 2.3
    assert max([-1.2, complex(0,2.3), -3.4]) == complex(0,2.3)
    assert max([1.2, -2.3j, -3.4j], key=lambda x:x.imag) == 1.2

# Generated at 2022-06-22 12:00:38.325422
# Unit test for function min
def test_min():

    environment = type('Environment', (object,), {'filters': {} })()

    # Test case insensitive
    assert sorted(min(environment, "dcdF", "AbcD")) == ["AbcD", "dcdF"]

    # Test case sensitive
    if HAS_MIN_MAX:
        assert sorted(min(environment, "dcdF", "AbcD", case_sensitive=True)) == ["AbcD", "dcdF"]
    else:
        assert min(environment, "dcdF", "AbcD", case_sensitive=True) == min(environment, "dcdF", "AbcD")

    # Test case attribute