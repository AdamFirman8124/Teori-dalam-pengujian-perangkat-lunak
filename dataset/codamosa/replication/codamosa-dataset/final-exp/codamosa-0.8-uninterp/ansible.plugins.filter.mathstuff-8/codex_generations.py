

# Generated at 2022-06-22 11:51:01.774613
# Unit test for function max
def test_max():
    assert max([1, 2]) == 2
    assert max([1, 2, 3], key=lambda x: -x) == 1
    assert max([1, 2, 3], key=lambda x: x) == 3
    assert max([1, 2, 3], key=lambda x: x, default=5) == 3
    assert max([], key=lambda x: x, default=5) == 5
    assert max([], default=5) == 5
    assert max(1) == 1
    assert max(1, key=lambda x: -x) == 1
    assert max(1, key=lambda x: x) == 1
    assert max(1, key=lambda x: x, default=5) == 1
    assert max(1, default=5) == 1

# Generated at 2022-06-22 11:51:06.652662
# Unit test for function power
def test_power():
    import pytest
    assert power(2, 3) == 8
    assert power(2, -3) == 0.125

    with pytest.raises(AnsibleFilterTypeError):
        power('2', 3)
    with pytest.raises(AnsibleFilterTypeError):
        power(2, '3')

# Generated at 2022-06-22 11:51:17.857587
# Unit test for function max
def test_max():
    assert max([1, 2, 3, 4, 5]) == 5
    assert max([5, 1, 4, 2, 3]) == 5
    assert max([4, 3, 2, 5, 1]) == 5
    assert max([5, 5]) == 5
    assert max([5]) == 5
    assert max([]) is None
    assert max(["1", "2", "3", "4", "5"]) == "5"
    assert max(["5", "1", "4", "2", "3"]) == "5"
    assert max(["4", "3", "2", "5", "1"]) == "5"
    assert max(["5", "5"]) == "5"
    assert max(["5"]) == "5"



# Generated at 2022-06-22 11:51:22.167593
# Unit test for function unique
def test_unique():
    data = ['a','a','b','b','b','c','c','c','c','c','d','d','d','d','d','d','d']
    assert unique(data,True) == ['a','b','c','d']


# Generated at 2022-06-22 11:51:33.883945
# Unit test for function max
def test_max():
    """
    Test max filter

    First two items should be checked using Python's max function
    Third item should be checked using Jinja's min function
    """
    # Assume we have a Jinja2 environment
    e = None
    if not HAS_MIN_MAX:
        from jinja2 import Environment
        e = Environment()

    for i in [
        ([1, 2, 3], 3),
        ([-3, -2, -1], -1),
        (["a", "b", "c"], "c")
    ]:
        # Invoke the filter
        if e:
            assert e.from_string('{{ x | max }}').render(x=i[0]) == i[1]
        else:
            assert max(e, i[0]) == i[1]


# Generated at 2022-06-22 11:51:36.444576
# Unit test for function min
def test_min():
    min_expect = 1
    min_inputs = [1, 2, 3]
    min_result = min(None, min_inputs)

    assert min_result == min_expect


# Generated at 2022-06-22 11:51:49.633041
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('2m') == 2 * pow(2, 20)
    assert human_to_bytes('2M') == 2 * pow(2, 20)
    assert human_to_bytes('3g') == 3 * pow(2, 30)
    assert human_to_bytes('3G') == 3 * pow(2, 30)
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('1024Ki') == pow(2, 20)
    assert human_to_bytes('5MiB') == 5 * pow(2, 20)
    assert human_to_bytes('5gib') == 5 * pow(2, 30)

# Generated at 2022-06-22 11:51:59.469079
# Unit test for function unique
def test_unique():
    assert [1, 2, 3] == unique([1, 1, 2, 3, 2])
    assert ['a', 'b', 'c'] == unique(['a', 'b', 'a', 'c', 'c'])
    assert ['a', 'b', 'c'] == unique(['a', 'b', 'a', 'c', 'c'], True)
    assert ['a', 'b', 'c'] == unique(['a', 'B', 'a', 'c', 'c'])
    assert ['a', 'B', 'c'] == unique(['a', 'B', 'a', 'c', 'c'], True)
    assert ['a', 'B', 'c'] == unique(['a', 'B', 'a', 'c', 'c'], False)

# Generated at 2022-06-22 11:52:04.297501
# Unit test for function max
def test_max():
    from ansible.module_utils.common.text import formatters
    assert 0 == max(0)
    assert 0 == max([])
    assert 1 == max(0, 1)
    assert -1 == max(-1, 0)
    assert 4.2 == max(4.2, 0, -1, 4.1)
    assert 4.2 == max(formatters.human_to_bytes("4.2kB"), formatters.human_to_bytes("1kB"))
    assert 1 == max("a", 1)


# Generated at 2022-06-22 11:52:15.778818
# Unit test for function rekey_on_member

# Generated at 2022-06-22 11:52:30.121057
# Unit test for function max
def test_max():
    assert max([1, 2, 10]) == 10
    assert max([1, 2, 10], key=lambda x: x % 2) == 2



# Generated at 2022-06-22 11:52:34.245277
# Unit test for function min
def test_min():

    # Test Min with 2 numbers (real and int)
    assert min([1,2]) == 1

    # Test Min with 3 numbers (real and int)
    assert min([1,2,3]) == 1

    # Test Min with list of numbers
    assert min([1,2,3,4,5]) == 1

    # Test Min with strings
    assert min(["a", "b", "c", "d"]) == "a"
    assert min(["alpha", "beta", "gamma"]) == "alpha"

    # Test Min with list of strings
    assert min(["alpha", "beta", "gamma", "delta"]) == "alpha"

# Generated at 2022-06-22 11:52:46.358503
# Unit test for function min
def test_min():
    def _test_min(exp_ret, *args, **kwargs):
        ret = min(*args, **kwargs)
        assert ret == exp_ret, 'min returned %r but expected %r' % (ret, exp_ret)

    _test_min(1, [1, 2])
    _test_min('a', ['a', 'b'])
    _test_min('a', ['b', 'a'])
    _test_min(['a'], ['b', ['a']])
    _test_min({'a': 1}, [{'a': 2}, {'a': 1}], attribute='a')
    _test_min({'a': 1}, [{'a': 1}, {'b': 2}], attribute='a')

# Generated at 2022-06-22 11:52:56.382185
# Unit test for function max
def test_max():
    # test with a list of strings
    test_list = ['a', 'b', 'c', '1', '2', '3']
    assert max(test_list) == 'c'

    # test with a list of integers
    test_list = [1, 2, 3, 4, 5, 6, 7]
    assert max(test_list) == 7

    # test with a list of integers
    test_list = ['-1', '-2', '-3', '-4', '-5', '-6', '-7']
    assert max(test_list) == '-1'

    # test with a list of floating point numbers
    test_list = [3.14, 2.72, 2.17, 2.23, 2.5, 2.92, 2.62]

# Generated at 2022-06-22 11:53:01.611136
# Unit test for function inversepower
def test_inversepower():
    assert inversepower(4) == 2
    assert inversepower(8, 3) == 2
    assert inversepower(27, 3) == 3
    assert inversepower(16, 256) == 1
    assert inversepower(1, 1) == 1

# Generated at 2022-06-22 11:53:05.469651
# Unit test for function min
def test_min():
    assert min([1, 2, 5, 3]) == 1
    assert min([-1, -2, -5, -3]) == -5
    assert min([1.1, 2.2, 5.5, 3.3]) == 1.1



# Generated at 2022-06-22 11:53:13.388902
# Unit test for function min
def test_min():
    from ansible.template import Environment

    env = Environment()

    env.filters['min'] = min
    ansible_min = env.from_string('''{{ [1,2,3] | min }}''').render()
    assert ansible_min == '1'

    if HAS_MIN_MAX:
        jinja_min = env.from_string('''{{ [1,2,3] | min }}''').render()
        assert ansible_min == jinja_min

# Generated at 2022-06-22 11:53:25.064909
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(1) == '1.0 B'
    assert human_readable(1, isbits=True) == '8.0 B'
    assert human_readable(15, unit='B') == '15.0 B'
    assert human_readable(15, unit='KB') == '0.0 KB'
    assert human_readable(15000, unit='KB') == '14.6 KB'
    assert human_readable(150000, unit='KB') == '146.1 KB'
    assert human_readable(1500000, unit='KB') == '1.4 MB'
    assert human_readable(15000000000, unit='KB') == '14.2 GB'
    assert human_readable(150000000000, unit='KB') == '142.9 GB'

# Generated at 2022-06-22 11:53:34.477497
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 2, 3], 2) == 2
    assert max([1, 2, 3], [4, 5, 6]) == [4, 5, 6]
    assert max([1, 2, 3], key=abs) == 3
    assert max([1, 2, 3], [4, 5, 6], key=abs) == 6

    assert max([[1, 2, 3], [4, 5, 6]]) == [4, 5, 6]
    assert max([[1, 2, 3], [4, 5, 6]], key=len) == [4, 5, 6]
    assert max([[1, 2, 3], [4, 5, 6]], key=lambda x: x[2]) == [4, 5, 6]

# Generated at 2022-06-22 11:53:39.775568
# Unit test for function rekey_on_member
def test_rekey_on_member():
    ''' Unit test for function rekey_on_member '''
    # Data:
    # list_dict = [
    #     { 'from' : 'A', 'to' : 'B' },
    #     { 'from' : 'C', 'to' : 'D' },
    #     { 'from' : 'A', 'to' : 'C' },
    # ]
    import ansible.utils.template as template

    t = template.Template('')

    list_dict = [
        {'from': 'A', 'to': 'B'},
        {'from': 'C', 'to': 'D'},
        {'from': 'A', 'to': 'C'},
    ]


# Generated at 2022-06-22 11:53:58.572388
# Unit test for function min
def test_min():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert filters['min']('a', 'b')[0] == 'a'
    assert filters['min']('a', 'b')[1] == 'b'
    assert filters['min']([1, 10, 2, 5]) == 1
    assert filters['min']([1, 10, 2, 5], 2) == 5
    assert filters['min']([1, 10, 2, 5, 0]) == 0
    assert filters['min']([1, 10, 2, 5, 0], 3) == 10

    assert filters['min']([]) is None
    assert filters['min']() is None
    assert filters['min']([1]) == 1



# Generated at 2022-06-22 11:54:10.204754
# Unit test for function rekey_on_member
def test_rekey_on_member():
    d = {'first': {'name': 'Joe', 'age': 43, 'occupation': 'carpenter'},
         'second': {'name': 'Jane', 'age': 39, 'occupation': 'teacher'},
         'third': {'name': 'Harry', 'age': 7, 'occupation': 'student'},
         'fourth': {'name': 'Mary', 'age': 4, 'occupation': 'student'}}

# Generated at 2022-06-22 11:54:19.621313
# Unit test for function max
def test_max():
    assert max([1, 2]) == 2
    assert max([2, 1]) == 2

    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([2, 3, 1]) == 3
    assert max([3, 2, 1]) == 3
    assert max([3, 1, 2]) == 3

    assert max([-1, -2]) == -1
    assert max([-2, -1]) == -1
    assert max([1, -2]) == 1
    assert max([-2, 1]) == 1

    assert max([1.1, 1.2]) == 1.2
    assert max([1.2, 1.1]) == 1.2

    assert max(['a', 'b']) == 'b'

# Generated at 2022-06-22 11:54:21.393436
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([3, 2, 1]) == 1
    assert min([1, 3, 2]) == 1



# Generated at 2022-06-22 11:54:28.084465
# Unit test for function rekey_on_member
def test_rekey_on_member():
    """
    >>> test_rekey_on_member()
    {'key1': 'value1', 'key2': 'value2'}
    """
    from pprint import pprint as pp
    data = [{'key1': 'key1', 'value': 'value1'}, {'key2': 'key2', 'value': 'value2'}]
    result = rekey_on_member(data, 'key', 'overwrite')
    pp(result)


# Generated at 2022-06-22 11:54:31.137476
# Unit test for function min
def test_min():
    f = FilterModule()
    assert f.filters()['min']([1, 2, 3]) == 1, "assertion failed"

# Generated at 2022-06-22 11:54:33.861282
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(100) == 4.605170185988092
    assert logarithm(100,10) == 2.0

# Generated at 2022-06-22 11:54:43.280478
# Unit test for function max
def test_max():
    env = {}
    assert max(env, [1, 2, 3]) == 3
    assert max(env, [1]) == 1
    assert max(env, [1, 2, 3], 2, 3) == 3
    assert max(env, [1, 2, 3], 2, 4) == 4
    assert max(env, [1, 2, 3], 2, 4, 0) == 4
    assert max(env, 1, 2, 3) == 3

    # tests with key
    assert max(env, [1, 2, 3], key=lambda x: x) == 3
    assert max(env, [1, 2, 3], key=lambda x: x, default=None) == 3
    assert max(env, [1, 2, 3], key=lambda x: x, default=1) == 3

# Generated at 2022-06-22 11:54:49.997149
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([3, 1, 2]) == 3
    assert max([3, 2, 1]) == 3
    assert max([1, 2]) == 2
    assert max([2, 1]) == 2
    assert max(1) == 1
    assert max(list(range(1, 11))) == 10


# Generated at 2022-06-22 11:54:58.554031
# Unit test for function rekey_on_member
def test_rekey_on_member():
    data = [
        {'name': 'alice', 'uname': 'pathfinder'},
        {'name': 'bob', 'uname': 'blue'},
        {'name': 'charlie', 'uname': 'charlie'},
        {'name': 'dave', 'uname': 'davelinux'},
        {'name': 'alice', 'uname': 'pf_alice'},
        {'name': 'bob', 'uname': 'bob'},
        {'name': 'dave', 'uname': 'linux_dave'},
    ]


# Generated at 2022-06-22 11:55:16.007869
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3, 'Return max value from a list'
    assert max([1, 3, 2]) == 3, 'Return max value from a list'
    assert max([3, 2, 1]) == 3, 'Return max value from a list'
    assert max([1, 2, 3], default=4) == 3, 'Return max value from a list'
    assert max([], default=4) == 4, 'Return the default value when there is no max'
    assert max(map(float, '1 2 3'.split())) == 3.0, 'Return max value from a list of floats'
    assert max(set([1, 2, 3])) == 3, 'Return max value from a set'

# Generated at 2022-06-22 11:55:20.754620
# Unit test for function min
def test_min():
    assert min(9, 1) == 1
    assert min([9, 1, 2]) == 1
    assert min([9, 1, 2], attribute='name') == 'name'
    assert min([9, 1, 2], True) == 1
    assert min([9, 1, 2], False) == 'name'


# Generated at 2022-06-22 11:55:32.856486
# Unit test for function rekey_on_member
def test_rekey_on_member():
    """
    Make a flat list of dictionaries into a dictionary keyed off of
    other values in the dictionary.
    """
    test_dict = [
        {
            'name': 'foo',
            'value': 'a'
        },
        {
            'name': 'bar',
            'value': 'b'
        }
    ]

    # Test against a valid input
    result = rekey_on_member(test_dict, 'name')
    assert result == {
        'foo': {
            'name': 'foo',
            'value': 'a'
        },
        'bar': {
            'name': 'bar',
            'value': 'b'
        }
    }, "Did not receive the expected output: {0}".format(result)

    # Test with a non-unique value
    test_dict

# Generated at 2022-06-22 11:55:35.379139
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([0, 1, 3, 2]) == 3
    assert max([]) is None


# Generated at 2022-06-22 11:55:40.933454
# Unit test for function max
def test_max():
    a_filter = FilterModule()
    assert a_filter.filters()['max']([3, 2, 1]) == 3
    assert a_filter.filters()['max']([3, 2], default=4, key=lambda v: v + 1) == 2
    assert a_filter.filters()['max']([3, 2], default=4, attribute='length') == '2'


# Generated at 2022-06-22 11:55:53.024707
# Unit test for function max
def test_max():
    # Test with list
    # Predefined list
    a = [-1, 7, 0]
    assert max(a) == 7
    # List with variable
    b = [1, "a", 2]
    assert max(b) == 2
    # Test with kwargs
    # With only one kwarg
    assert max(a, key=abs) == -1
    # With only two kwargs (default)
    assert max(a, key=abs, default=-2) == -1
    # With three kwargs (predefined list)
    assert max(a, key=lambda x: -x, default=-2) == -1
    # With three kwargs (predefined list)
    assert max(a, key=lambda x: -x, default=-2) == -1
    # With three kwargs (list

# Generated at 2022-06-22 11:56:03.661292
# Unit test for function human_readable
def test_human_readable():
    def test(value, expected, **kwargs):
        result = human_readable(value, **kwargs)
        print('%s == %s (%s)' % (value, result, expected))
        assert result == expected

    test(5000, "4.88KiB")
    test(7000, "6.81KiB")
    test(9000, "8.79KiB")

    test(9123456789, "8.50GiB")
    test(9123456789, "8.50GB", unit='GB')
    test(9123456789123456789, "7.99EiB")
    test(9123456789123456789, "7.99EB", unit='EB')

    test(9123456789, "8.79KiB")
   

# Generated at 2022-06-22 11:56:05.587672
# Unit test for function min
def test_min():
    data = [10, 20, 5]

    assert min(None, data) == 5



# Generated at 2022-06-22 11:56:11.101693
# Unit test for function max
def test_max():
    assert max([1, 2, 3, 4, 5]) == 5
    assert max([[1, 2], [1, 3], [5, 0]]) == [5, 0]
    assert max(['10', '5', '1']) == '5'
    assert max([[1, 2], ['a', 'b']]) == ['a', 'b']
    assert max(['a', 'b', 'c'], key=len) == 'a'


# Generated at 2022-06-22 11:56:23.024321
# Unit test for function unique
def test_unique():
    opts = dict(
        ignore_case=False,
    )

    # test list
    data = [1, 2, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 4]
    result = unique(data)
    assert result == [1, 2, 3, 4, 5], 'failed to filter unique values from list'

    # test string case-sensitive
    opts['ignore_case'] = False
    data = 'aabbccddeeffgghhiijjkkllmm'
    result = unique(data)
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'], 'failed to filter unique values from string case-sensitive'

    # test string case-insensitive

# Generated at 2022-06-22 11:56:43.781431
# Unit test for function max
def test_max():
    data = {'b': ['a', 'b', 'c', 'd', 'e'], 'a': ['a', 'b', 'c', 'd', 'e'], 'e': ['a', 'b', 'c', 'd', 'e'], 'c': ['a', 'b', 'c', 'd', 'e'], 'd': ['a', 'b', 'c', 'd', 'e']}
    assert('e' == max(data, key=lambda x: x[0]))
    assert('b' == max('abcdef', key=lambda x: x[0]))
    assert('e' == max('abcdef', key=lambda x: x[0], default='e'))
    assert('e' == max('abcdef', key=lambda x: x[0], default='e', b='a'))

# Generated at 2022-06-22 11:56:46.167303
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([[1, 2], [3, 4]]) == [1, 2]
    assert min(['foo', 'bar', 'baz']) == 'bar'


# Generated at 2022-06-22 11:56:53.084436
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([3, 1, 2]) == 3
    assert max([3, 2, 1]) == 3
    assert max([1.1, 1.2, 1.3]) == 1.3
    assert max([1.9, 1.2, 1.3]) == 1.9
    assert max(["foo", "bar"]) == "foo"
    assert max([1.0, 2.0, 2.5]) == 2.5
    # Test multiple key arguments
    assert max([1, 3, 2], key=str, default=0) == 3
    assert max([1, 3, 2], key=lambda x: -x) == 1


# Generated at 2022-06-22 11:56:54.158332
# Unit test for function max
def test_max():
    m = max(1, 2)
    assert(m == 2)


# Generated at 2022-06-22 11:57:00.651938
# Unit test for function min
def test_min():
    filter_module = FilterModule()
    filters = filter_module.filters()
    min_filter = filters.get('min')
    import jinja2  # noqa: F401

    # test with numbers
    test_num_list = [1, 2, 3, 4, 5]
    result = min_filter(test_num_list)
    assert result == 1

    # test with strings
    test_str_list = ['one', 'two', 'three', 'four', 'five']
    result = min_filter(test_str_list)
    assert result == 'five'

    # test with key_func
    result = min_filter(test_str_list, key_func=lambda x: len(x))
    assert result == 'one'

    # test with key_func using dictionary
    test_dict_list

# Generated at 2022-06-22 11:57:09.605781
# Unit test for function human_readable
def test_human_readable():
    from ansible.utils import unit

    assert human_readable("1") == "1 B"
    assert human_readable("2") == "2 B"
    assert human_readable("1024") == "1 K"
    assert human_readable("2048") == "2 K"
    assert human_readable("1", False) == "1 B"
    assert human_readable("2") == "2 B"
    assert human_readable("1024", False) == "1.02 K"
    assert human_readable("2048", False) == "2.05 K"
    assert human_readable("2", True) == "2 B"
    assert human_readable("2048", True) == "2 KiB"
    assert human_readable("1", False, "B") == "1 B"
    assert human_readable("1", False, "K")

# Generated at 2022-06-22 11:57:13.957378
# Unit test for function max
def test_max():
    max_list = [5,6,7,8,9,10]
    max_int = 10
    max_list_err = [5,6,"7",8,"9",10]
    max_int_err = 20
    assert max(max_list) == max_int
    assert max(max_list_err) == max_int_err


# Generated at 2022-06-22 11:57:25.946495
# Unit test for function max
def test_max():
    ''' Unit test for max() in Jinja2 env '''
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.text.formatters import human_to_bytes

    # Integer
    assert max([1, 2, 3, 4, 5]) == 5
    assert max((6, 7, 8, 9, 10)) == 10

    # String
    assert max(['a', 'b', 'c']) == 'c'
    assert max(('d', 'e', 'f')) == 'f'

    # Float
    assert max([1.1, 2.2, 3.3, 4.4]) == 4.4
    assert max((5.5, 6.6, 7.7)) == 7.7

    # Bytes
    # On Python 2

# Generated at 2022-06-22 11:57:30.924030
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(100.0) == "100.0 B"
    assert human_readable(100.0, unit="KB") == "100.0 KB"
    assert human_readable(1048576.0, unit="MB") == "1.0 MB"
    assert human_readable(1073741824.0, unit="GB") == "1.0 GB"
    assert human_readable(1073741824.0, unit="TB") == "1.0 TB"
    assert human_readable(1024.0, unit="MB") == "1.0 MB"
    assert human_readable(1045.0, unit="KB") == "1.0 KB"
    assert human_readable(1025.0, unit="MB") == "1.0 MB"

# Generated at 2022-06-22 11:57:41.037642
# Unit test for function rekey_on_member
def test_rekey_on_member():
    data = {1: {'name': 'george', 'age': 12},
            2: {'name': 'alice', 'age': 33}}
    key = 'name'

    expected = {'george': {'name': 'george', 'age': 12},
                'alice': {'name': 'alice', 'age': 33}}
    result = rekey_on_member(data, key)
    assert result == expected
    result = rekey_on_member(data, key, 'overwrite')
    assert result == expected

    bad_data = {1: {'name': 'george', 'age': 12},
                2: {'name': 'alice', 'age': 33},
                3: {'name': 'alice', 'age': 11}}

# Generated at 2022-06-22 11:57:56.856340
# Unit test for function min
def test_min():
    filter = FilterModule()
    assert filter.filters()['min']([2, 3, 1]) == 1



# Generated at 2022-06-22 11:58:05.206271
# Unit test for function human_to_bytes

# Generated at 2022-06-22 11:58:16.902729
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("1") == 1
    assert human_to_bytes("1.5") == 1
    assert human_to_bytes("1kB") == 1024
    assert human_to_bytes("1.5kB") == 1536
    assert human_to_bytes("1MB") == 1024 ** 2
    assert human_to_bytes("1.5MB") == int(1.5 * 1024 ** 2)
    assert human_to_bytes("1GB") == 1024 ** 3
    assert human_to_bytes("1.5GB") == int(1.5 * 1024 ** 3)
    assert human_to_bytes("1TB") == 1024 ** 4
    assert human_to_bytes("1.5TB") == int(1.5 * 1024 ** 4)
    assert human_to_bytes("1PB") == 1024 ** 5
   

# Generated at 2022-06-22 11:58:23.254725
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5]) == 1
    assert min([[1, 2, 3], [1, 2, 3]]) == [1, 2, 3]
    assert min([{'a': 1}, {'a': 2}, {'a': 3}], key=lambda x: x['a']) == {'a': 1}
    assert min([{'a': 1}, {'a': 2}, {'a': 3}], attribute='a') == {'a': 1}
    assert min([1, 2, 3, 4, 5], start=3) == 3
    assert min(1, 2, 3, 4, 5) == 1
    assert min(1, 2, 3, 4, 5, start=3) == 3


# Generated at 2022-06-22 11:58:32.698879
# Unit test for function max
def test_max():
    "Test max filter"
    f = FilterModule().filters()['max']
    if HAS_MIN_MAX:
        assert f([1, 2, 3]) == 3
        assert f([1.1, 2.2, 3.3]) == 3.3
        assert f([], default=0) == 0
        assert f('hello world') == 'w'
        assert f([1, 2, 3], 4) == 4

        # keyword args
        assert f([1, 2, 3], default=0) == 3

    else:
        assert f([1, 2, 3]) == 3
        assert f([1.1, 2.2, 3.3]) == 3.3
        assert f([], default=0) == 0
        assert f('hello world') == 'w'

# Generated at 2022-06-22 11:58:37.998810
# Unit test for function max
def test_max():
    # These do not raise an error and return expected value
    assert max([0, 1, 2, 3, 4, 5]) == 5
    assert max([1, 2, 0]) == 2
    assert max([[0, 1], [2, 3], [4, 5]]) == [4, 5]

# Generated at 2022-06-22 11:58:49.942815
# Unit test for function max
def test_max():
    # The function returns the biggest number from a list.
    assert max([7, 9, 5, 6]) == 9
    assert max((7, 9, 5, 6)) == 9
    # The function also returns the biggest number from a tuple.
    assert max((7, 9, 5, 6)) == 9
    assert max([7, 9, 5, 6]) == 9
    # The function returns the biggest string from a list.
    assert max(['alpha', 'gamma', 'beta']) == 'gamma'
    assert max(['alpha', 'gamma', 'beta']) == 'gamma'
    # The function returns the biggest string from a tuple.
    assert max(('alpha', 'gamma', 'beta')) == 'gamma'
    assert max(('alpha', 'gamma', 'beta')) == 'gamma'
    #

# Generated at 2022-06-22 11:58:51.957706
# Unit test for function max
def test_max():
    assert max([1, 2]) == 2
    assert max(1, 2) == 2



# Generated at 2022-06-22 11:58:53.411085
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3


# Generated at 2022-06-22 11:59:01.102098
# Unit test for function rekey_on_member
def test_rekey_on_member():
    # Create dict with key - value
    expected_dict = dict()
    expected_dict['key1'] = 'value1'
    expected_dict['key2'] = 'value2'
    expected_dict['key3'] = 'value3'

    # Create list of dicts with key - val
    dict_list = list()

    dict_list.append(dict(key='key1', val='value1'))
    dict_list.append(dict(key='key2', val='value2'))
    dict_list.append(dict(key='key3', val='value3'))

    # Test should return dict of dicts

# Generated at 2022-06-22 11:59:30.026454
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3



# Generated at 2022-06-22 11:59:31.538547
# Unit test for function max
def test_max():
    assert max([1, 2]) == 2


# Generated at 2022-06-22 11:59:37.549325
# Unit test for function max
def test_max():
    if HAS_MIN_MAX:
        assert do_max(None, [1, 2, 3, 4, 5]) == 5
    else:
        assert max(None, [1, 2, 3, 4, 5]) == 5
    assert max(None, [5, 4, 3, 2, 1]) == 5



# Generated at 2022-06-22 11:59:43.764040
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min("aBc") == 'B'
    assert min("abc") == 'a'
    assert min("abcA") == 'A'
    assert min("abcZZ") == 'Z'
    assert min(['b', 'a']) == 'a'
    assert min(['a', 'b']) == 'a'


# Generated at 2022-06-22 11:59:53.994621
# Unit test for function max
def test_max():
    """
    Test the function max()
    """

    max_filter = getattr(FilterModule, 'filters')()['max']

    # Check with numbers
    assert max_filter(None, [1, 2, 3]) == 3
    assert max_filter(None, [3, 1, 3]) == 3
    assert max_filter(None, [1, 7, 3]) == 7
    assert max_filter(None, [-1, -2, -3]) == -1
    assert max_filter(None, [-1, -7, -3]) == -1

    # Check with strings
    assert max_filter(None, ['hello', 'world']) == 'world'
    assert max_filter(None, ['hello', 'World']) == 'hello'

# Generated at 2022-06-22 12:00:02.387528
# Unit test for function rekey_on_member

# Generated at 2022-06-22 12:00:09.164709
# Unit test for function max
def test_max():
    assert max(1) == 1

    assert max(1, 2) == 2
    assert max(2, 1) == 2

    assert max([1, 2, 3]) == 3

    assert max([1, 2], [2, 1]) == 2
    assert max([2, 1], [1, 2]) == 2

    assert max(1, 2, 3) == 3
    assert max(3, 2, 1) == 3
    assert max(2, 3, 1) == 3
    assert max(1, 3, 2) == 3
    assert max(3, 1, 2) == 3
    assert max(2, 1, 3) == 3

    assert max('foo', 'bar') == 'foo'
    assert max('bar', 'foo') == 'foo'

    # Dirty way to test keyword arguments (where some are supported and some are not

# Generated at 2022-06-22 12:00:12.067051
# Unit test for function max
def test_max():
    if max([1, 2, 3]) != 3:
        raise AssertionError('Max of list 1,2,3 should be 3')

# Generated at 2022-06-22 12:00:22.798895
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1m') == 1048576
    assert human_to_bytes('1mb') == 1048576
    assert human_to_bytes('1g') == 1073741824
    assert human_to_bytes('1gb') == 1073741824
    assert human_to_bytes('1t') == 1099511627776
    assert human_to_bytes('1tb') == 1099511627776
    assert human_to_bytes('1p') == 1125899906842624
    assert human_to_bytes('1pb') == 1125899906842624
    assert human_to_bytes('1e') == 11529

# Generated at 2022-06-22 12:00:25.580557
# Unit test for function max
def test_max():
    result = max([1, 2, 3, 4])
    assert result == 4
    result = max([1, 2, 4, 3])
    assert result == 4

