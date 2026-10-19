

# Generated at 2022-06-22 11:51:00.771924
# Unit test for function max
def test_max():
    from ansible.plugins.filter.max import max
    import jinja2
    env = jinja2.Environment(loader=jinja2.DictLoader({'t': '{{ a | max }}'}))

    for a in (1, 1.0, 'a', ['b'], {'c': 'd'}):
        assert max(env, a) == a, 'failed with: ' + str(type(a))
    assert max(env, 1, 2) == 2, 'failed with two ints'
    assert max(env, 1.0, 2.0) == 2.0, 'failed with two floats'
    assert max(env, 'a', 'b') == 'b', 'failed with two strings'

    assert max(env, 1, 1.0) == 1, 'failed with int and float'
   

# Generated at 2022-06-22 11:51:12.856098
# Unit test for function max
def test_max():
    # Compatible calls
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([2, 1, 3]) == 3
    assert max([2, 3, 1]) == 3
    assert max([3, 1, 2]) == 3
    assert max([3, 2, 1]) == 3

    # Incompatible calls
    try:
        max([])
    except AnsibleFilterTypeError as e:
        assert e.args[0] == "Generator: max(..., key=...) requires 2 or more elements"
    else:
        assert False, "No exception raised"
    try:
        max([1])
    except AnsibleFilterTypeError as e:
        assert e.args[0] == "Generator: max(..., key=...) requires 2 or more elements"


# Generated at 2022-06-22 11:51:21.851775
# Unit test for function unique
def test_unique():
    import jinja2

    env = jinja2.Environment()
    env.filters['unique'] = unique

    # Test 1
    assert env.from_string(
        '{{ [1, 2, 2, 3, 2, 1, 2, 3, 2]|unique }}'
    ).render(
    ) == "[1, 2, 3]"

    # Test 2

# Generated at 2022-06-22 11:51:33.657040
# Unit test for function unique
def test_unique():
    # normal use case
    v1 = [ 1, 2, 3, 4, 5 ]
    v2 = [ 3, 4, 5, 6, 7 ]
    v3 = [ 1, 2, 3, 4, 5, 6, 7 ]
    assert unique(None, v1+v2) == v3

    # empty list
    assert unique(None, []) == []

    # list of list
    assert unique(None, [v1, v2]) == [v1, v2]

    # unorderable values with unique=True
    # only works with Jinja2 2.9 (or later) and the 'unique' filter
    try:
        unique(None, [set(v1), set(v2)], True)
        has_orderable = True
    except Exception:
        has_orderable = False


# Generated at 2022-06-22 11:51:39.207530
# Unit test for function min
def test_min():
    module = FilterModule()
    d = module.filters()
    min_filter = d['min']
    assert min_filter([0, 1, 2]) == 0
    assert min_filter([2, 1, 0]) == 0
    assert min_filter([2]) == 2
    assert min_filter([1, 2]) == 1
    assert min_filter(['b', 'a', 'c']) == 'a'
    # string, int, float and list
    assert min_filter(['1', 2, 3.0, [4]]) == 0


# Generated at 2022-06-22 11:51:45.850089
# Unit test for function max
def test_max():
    assert max([1, 1, 2, 2, 3, 3]) == 3
    assert max([1, 1, 2, 2, 3, 3], 2) == 2
    assert max([1, 1, 2, 2, 3, 3], 3) == 3
    assert max([1, 1, 2, 2, 3, 3], 4) == 4


# Generated at 2022-06-22 11:51:48.411116
# Unit test for function max
def test_max():
    f = FilterModule().filters()
    assert f['max']([1, 2, 3]) == 3


# Generated at 2022-06-22 11:51:56.158813
# Unit test for function logarithm
def test_logarithm():
    fm = FilterModule()
    env = {}
    assert fm.filters()['log'](env, math.e) == 1.0
    assert fm.filters()['log'](env, 10, 10) == 1.0
    assert fm.filters()['log'](env, 2, 8) == 3.0
    assert fm.filters()['log'](env, 8, 2) == 3.0
    assert fm.filters()['log'](env, 9, 3) == 2.0
    assert fm.filters()['log'](env, 3, 9) == .5



# Generated at 2022-06-22 11:52:08.260311
# Unit test for function rekey_on_member
def test_rekey_on_member():
  test_dict1 = {
    'foo': { 'a': 1, 'b': 2 },
    'bar': { 'a': 3, 'b': 4 },
  }

  test_dict2 = {
    'foo': { 'a': 1, 'b': 2 },
    'bar': { 'a': 3, 'b': 4 },
    'baz': { 'a': 1, 'b': 2 },
  }
  result = rekey_on_member(test_dict1, "a")

  assert result == {
    1: { 'a': 1, 'b': 2 },
    3: { 'a': 3, 'b': 4 },
  }

  result = rekey_on_member(test_dict2, "a", duplicates="error")
  assert False


# Generated at 2022-06-22 11:52:20.069810
# Unit test for function human_to_bytes
def test_human_to_bytes():
    f = FilterModule()
    human_to_bytes = f.filters['human_to_bytes']
    human_readable = f.filters['human_readable']
    assert human_to_bytes("1 TB") == 1099511627776
    assert human_to_bytes("1.5 TB") == 1649267441664
    assert human_to_bytes("1.5 TiB") == 1649267441664
    assert human_to_bytes("1.5TB") == 1649267441664
    assert human_to_bytes(" 1.5 TB ") == 1649267441664
    assert human_to_bytes("1.5TB", "GB") == 1572864000
    assert human_to_bytes("1.5tb", "gb") == 1572864000

# Generated at 2022-06-22 11:52:32.676716
# Unit test for function min
def test_min():
    def _min_test(filters, mylist, myval, result):
        assert filters.min(mylist) == result
        assert filters.min(mylist, default=myval) == result

    # Set of tests to ensure the min filter works properly
    # The 'min' method should return the min() of all values in the list
    # If a keyword argument is used, the default value is returned
    # If the list is empty and a default value is not given, an AnsibleUndefinedVariable error is raised
    #
    # The format of the tests is a list with the following format:
    #   [ <list>, <value>, <default value>, <expected result> ]
    #
    #   If <default value> is None, no kwarg is used
    #   If <expected result> is None, an exception should be raised
    #

# Generated at 2022-06-22 11:52:40.137600
# Unit test for function min
def test_min():
    def _assert_min(a, b):
        assert a == b

    _assert_min(min([1, 2]), 1)
    _assert_min(min([2, 1]), 1)
    _assert_min(min({'a': 1, 'b': 2}), 1)
    _assert_min(min('abc'), 'a')
    _assert_min(min(['abc', 'def']), 'abc')
    _assert_min(min(['def', 'abc']), 'abc')

# Generated at 2022-06-22 11:52:51.952140
# Unit test for function min
def test_min():

    def test_min_basics_1(j2_env, j2_render, args, expected):
        actual = j2_render('{{ %s|min }}' % args, dict(list=list(range(1000))))
        assert actual == expected

    def test_min_basics_2(j2_env, j2_render, args, expected):
        actual = j2_render('{{ %s|min(attribute="stdin") }}' % args, dict(d=dict(stdin=1)))
        assert actual == expected

    def test_min_basics_3(j2_env, j2_render, args, expected):
        actual = j2_render('{{ %s|min(case_sensitive=False) }}' % args, dict(a=['a', 'A']))
        assert actual == expected

   

# Generated at 2022-06-22 11:52:53.719228
# Unit test for function max
def test_max():
    assert max(range(5, 10)) == 9



# Generated at 2022-06-22 11:53:04.920004
# Unit test for function unique
def test_unique():
    data = [1, 2, 3, 4, 3, 3, 2, 1, 2, 3, 4, 5, 6, 7, 5, 6, 7]
    at_data_copy = list(data)
    at_data_copy.reverse()

    for d in (data, at_data_copy):
        assert unique(d) == [1, 2, 3, 4, 5, 6, 7]
        assert unique(d, True) == [1, 2, 3, 4, 5, 6, 7]
        assert unique(d, False) == [1, 2, 3, 4, 5, 6, 7]
        assert unique(d, attribute='foo') == [1, 2, 3, 4, 5, 6, 7]



# Generated at 2022-06-22 11:53:08.219041
# Unit test for function logarithm
def test_logarithm():
    '''
    Logarithm function
    '''

    ret = logarithm(10)
    assert ret == 1.0



# Generated at 2022-06-22 11:53:17.058306
# Unit test for function min
def test_min():
    from ansible.module_utils.six import integer_types

    if not HAS_MIN_MAX:
        return

    # Ensure that Ansible's old version of min returns correct results
    # for different input types

    assert min([1, 2, 3]) == 1
    assert min(['a', 'b', 'c']) == 'a'
    assert min(['1', '2', '3']) == '1'
    assert min(['a', '1', 'b']) == '1'
    assert min(['a', 1, 'b']) == 'a'
    assert min([1, 'a', 'b']) == 'a'

    assert min((1, 2, 3)) == 1
    assert min(('a', 'b', 'c')) == 'a'

# Generated at 2022-06-22 11:53:18.548226
# Unit test for function min
def test_min():
    assert min([3, 4, 5]) == 3



# Generated at 2022-06-22 11:53:28.251363
# Unit test for function unique
def test_unique():
    assert unique([1, 2, 3, 4, 4, 4, 5, 6, 7, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert unique([1, 2, 3, 4, 4, 4, 5, 6, 7, 7], case_sensitive=False) == [1, 2, 3, 4, 5, 6, 7]
    assert unique([{'foo': 'bar'}, {'foo': 'baz'}, {'foo': 'bar'}], attribute='foo') == [{'foo': 'bar'}, {'foo': 'baz'}]


# Generated at 2022-06-22 11:53:31.956062
# Unit test for function min
def test_min():
    assert min([1, 3, 5, 7]) == 1
    assert min([1, -3, 5, 7]) == -3
    assert min([-7]) == -7
    assert min([]) == None



# Generated at 2022-06-22 11:53:40.417331
# Unit test for function min
def test_min():
    assert min([[], [1, 2, 3]]) == []
    assert min([{}, {1, 2, 3}, {}]) == {}
    assert min(['', 'a']) == ''
    assert min([4, 10, -5, 20]) == -5
    assert min([3, 3.5]) == 3
    assert min([[], [1, 2, 3]], key=len) == []
    assert min([{}, {1, 2, 3}, {}], key=len) == {}
    assert min(['', 'a'], key=len) == ''
    assert min([4, 10, -5, 20], key=abs) == -5
    assert min([3, 3.5], key=int) == 3
    assert min(['', 'a'], default='') == ''

# Generated at 2022-06-22 11:53:47.700551
# Unit test for function max
def test_max():
    filter_module = FilterModule()

    # Test max filter without jinja2's with Jinja2 2.7
    if not HAS_MIN_MAX:
        max_filtered = filter_module.filters()['max'](None, [1, 2])
        assert max_filtered == 2

    # Test max filter with jinja2's with Jinja2 2.10
    if HAS_MIN_MAX:
        max_filtered = filter_module.filters()['max'](None, [1, 2], foo='foo')
        assert max_filtered == 2



# Generated at 2022-06-22 11:53:59.175353
# Unit test for function max
def test_max():
    fltr = FilterModule()
    max_filter = fltr.filters()['max']

    # test string
    str1 = "abc"
    str2 = "ABC"
    str3 = "aaa"
    str4 = "bbb"
    str5 = "123"
    assert max_filter(str1, str2) == str2
    assert max_filter(str1, str3) == str3
    assert max_filter(str3, str4) == str4
    assert max_filter(str2, str3) == str2
    assert max_filter(str1, str5) == str1

    # test number
    num1 = 1
    num2 = 2
    num3 = 3.0
    assert max_filter(num1, num2) == num2

# Generated at 2022-06-22 11:54:06.681866
# Unit test for function max
def test_max():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    assert max([1, 2, 3]) == 3
    assert max([1, 2, 3], key=str) == 3
    assert max([UnsafeProxy(1), UnsafeProxy(2), UnsafeProxy(3)]) == UnsafeProxy(3)
    assert max([UnsafeProxy(1), UnsafeProxy(2), UnsafeProxy(3)], key=str) == UnsafeProxy(3)


# Generated at 2022-06-22 11:54:16.261174
# Unit test for function max
def test_max():
    assert max(['1', '2', '3']) == '3'
    assert max(['a', 'b', 'c']) == 'c'
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max(['1', '2']) == '2'
    assert max([1, 2]) == 2
    assert max(['1']) == '1'
    assert max([1]) == 1
    assert max(([1])) == 1
    assert max(([1, 2])) == 2
    assert max(([1, 2], (3, 4))) == 4
    assert max([[1, 2], [3, 4]]) == [3, 4]
    assert max((1, 2)) == 2
    assert max([[], []]) == []


# Generated at 2022-06-22 11:54:27.790767
# Unit test for function min
def test_min():
    try:
        # testing min(a, key, default)
        min_filter = min([42, 21, 37, 111], key=len, default=0)
        assert 21 == min_filter

        # testing min(a)
        min_filter = min([42, 21, 37, 111])
        assert 21 == min_filter

        # testing min(a, default)
        min_filter = min([], default=111)
        assert 111 == min_filter

        # testing min(a, key)
        min_filter = min([42, 21, 37, 111], key=lambda x: x % 10)
        assert 42 == min_filter

        # testing min(a, key) with exception
        min_filter = min([], key=len)
    except Exception as e:
        assert "min() arg is an empty sequence" in to

# Generated at 2022-06-22 11:54:39.524379
# Unit test for function min

# Generated at 2022-06-22 11:54:50.500143
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([1, 2, 3, 4], attribute='age') == 1

    # Test with a dict with all elements having the same attribute value, thus
    # dict value should be returned as the ``min``.
    assert min([{'age': 10, 1: 2}, {'age': 10, 2: 1}, {'age': 10, 3: 3}], attribute='age') == {'age': 10, 1: 2}

    # Test with a dict with mixed attribute values, thus dict value with the
    # smallest attribute value should be returned as the ``min``.
    assert min([{'age': 10, 1: 2}, {'age': 9, 2: 1}, {'age': 11, 3: 3}], attribute='age') == {'age': 9, 2: 1}



# Generated at 2022-06-22 11:54:54.328290
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5]) == 1
    assert min(xrange(10)) == 0
    assert min("joe") == 'e'
    assert min((5, 6, 7, 8, 9)) == 5


# Generated at 2022-06-22 11:55:05.069633
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2.5') == 250000000000
    assert human_to_bytes('2.5', 'MB') == 2560
    assert human_to_bytes('2.5', 'kb') == 2560
    assert human_to_bytes('2.5', 'TB') == 250000000000
    assert human_to_bytes('2.5G') == 250000000000
    assert human_to_bytes('2.5T') == 250000000000
    assert human_to_bytes('2.5K') == 2560
    assert human_to_bytes('2.5M') == 2560
    assert human_to_bytes('2.5KiB') == 2560
    assert human_to_bytes('2.5MiB') == 2560
    assert human_to_bytes('2.5Gib') == 2500000000

# Generated at 2022-06-22 11:55:23.997318
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(10) == "10.0 B"
    assert human_readable(100) == "100.0 B"
    assert human_readable(1048576) == "1.0 M"
    assert human_readable(1073741824) == "1.0 G"
    assert human_readable(1099511627776) == "1.0 T"
    assert human_readable(1125899906842624) == "1.0 P"
    assert human_readable(1152921504606846976) == "1.0 E"

    assert human_readable(10, isbits=True) == "10.0 bits"
    assert human_readable(100, isbits=True) == "100.0 bits"
    assert human_readable(1048576, isbits=True) == "8.0 Mbits"

# Generated at 2022-06-22 11:55:36.081924
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([3, 1, 2]) == 1
    assert min([3, 3, 2]) == 2
    assert min([3, 3, 3]) == 3
    assert min([1, 2, 3], by='key') == 1
    assert min([{'key': x} for x in [1, 2, 3]], by='key') == {'key': 1}
    assert min([[1], [2], [3]]) == [1]
    assert min([[3], [1], [2]]) == [1]
    assert min([[3], [3], [2]]) == [2]
    assert min([[3], [3], [3]]) == [3]

# Generated at 2022-06-22 11:55:43.099548
# Unit test for function max
def test_max():
    module = AnsibleModule(argument_spec={})
    data = [1, 2, 3, 4, 5, 6]
    result = module.run_command(['ansible', '--version'], check_rc=True)
    version = result[1].split()[1]
    try:
        version_tuple = tuple(int(i) for i in version.split('.'))
    except ValueError:
        version_tuple = (2, 10)
    if version_tuple > (2, 10):
        assert max(data) == 6

    else:
        assert max(data) == 6

# Generated at 2022-06-22 11:55:54.711742
# Unit test for function max
def test_max():

    def _test_max_impl(value, expected, **kwargs):
        actual = max(value, **kwargs)
        assert actual == expected

    _test_max_impl((1, 2), 2)

    _test_max_impl([1, 2], 2)

    _test_max_impl([2, 3, 5, 1], 5)

    _test_max_impl([{'value': 2}, {'value': 4}, {'value': 45}], {'value': 45}, attribute='value')

    _test_max_impl(['a', 'b', 'ba'], 'ba', attribute='length')

    _test_max_impl(['a', 'b', 'ba'], 'ba', attribute='length')

    _test_max_impl([1, 2, 3, 1], 3, case_sensitive=False)

# Generated at 2022-06-22 11:56:02.098752
# Unit test for function logarithm
def test_logarithm():
    results = logarithm(64, 4)
    assert results == 2
    results = logarithm(math.e)
    assert results == 1
    results = logarithm(100, 10)
    assert results == 2
    results = logarithm(math.pi)
    assert round(results, 5) == 1.14473

    # Check that filter raises a proper error
    try:
        logarithm("test")
    except:
        err = sys.exc_info()[1]
        assert isinstance(err, AnsibleFilterTypeError)


# Generated at 2022-06-22 11:56:04.905875
# Unit test for function max
def test_max():
    f = FilterModule()
    assert f.filters()['max']([1, 30, 20]) == 30



# Generated at 2022-06-22 11:56:13.609828
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1g') == 1073741824
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1m') == 1048576
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1mb') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_

# Generated at 2022-06-22 11:56:21.024465
# Unit test for function max
def test_max():
    assert max([8,1,6,5,10,3,9]) == 10
    assert max([[5,6], [7,2]]) == [7,2]
    assert max([[5,6,8], [7,2,1]]) == [7,2,1]
    assert max([[5,6,8], [7,2]]) == [7,2]
    assert max([4,3,2,1], key=lambda x: -x) == 4


# Generated at 2022-06-22 11:56:28.376239
# Unit test for function min
def test_min():
    assert min([1, 3, 2]) == 1
    assert min(1, 3, 2) == 1
    assert min([-1, -3, -4]) == -4
    assert min(-1, -3, -4) == -4
    assert min([-1.0, -3.0, -4.0]) == -4.0
    assert min(-1.0, -3.0, -4.0) == -4.0


# Generated at 2022-06-22 11:56:34.894246
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5]) == 1
    assert min([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1]
    assert min([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1]


# Generated at 2022-06-22 11:56:53.922869
# Unit test for function max
def test_max():
    if HAS_MIN_MAX:
        max_filter = max
    else:
        max_filter = lambda env, a, **kwargs: __builtins__.get('max')(a)

    assert max_filter('', [1, 2, 3]) == 3
    assert max_filter('', [1, 2, 3], attribute='real') == 3.0
    assert max_filter('', [1, 2, 3], attribute='imag') == 0.0
    assert max_filter('', [1, 2, 3], attribute='conjugate') == 3
    assert max_filter('', [1j, 2j, 3j]) == 3j
    assert max_filter('', [1j, 2j, 3j], attribute='real') == 0.0

# Generated at 2022-06-22 11:56:59.565716
# Unit test for function min
def test_min():
    assert min([1,2]) == 1
    assert min([1,2,3], [1,1,1]) == [1,1,1]
    assert min(1,2,3) == 1
    assert min([1,2,3], [1,1,1], [1,1,1],[1,2,2]) == [1,1,1]



# Generated at 2022-06-22 11:57:09.085760
# Unit test for function min
def test_min():
    from ansible.module_utils import basic
    from ansible.compat.tests import unittest

    class TestMin(unittest.TestCase):

        def test_min_kinds(self):
            self.assertEquals(b'a', basic.min(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))

# Generated at 2022-06-22 11:57:20.376843
# Unit test for function max
def test_max():

    # test that it works with numbers
    assert (179 >= max([178, 179]) >= -179) is True
    assert (179 >= max([-178, 179]) >= -179) is True
    assert (179 >= max([-178, 179, 10]) >= -179) is True
    assert (179 >= max([-179, 10]) >= -179) is True

    # test that it works with strings
    assert 'z' >= max('xyz')
    assert 'z' >= max('xzy')
    assert 'z' >= max('yxz')
    assert 'z' >= max('zyx')
    assert 'z' >= max('zyx', 'yxz')
    assert 'z' >= max('zyx', 'yxz', 'xzy')

    # test that it works with dictionaries and lists

# Generated at 2022-06-22 11:57:24.804289
# Unit test for function min
def test_min():
    assert min([0, 4, 2, -1]) == -1
    assert min([0, 4, -2, 1]) == -2
    assert min([0, 4, 2, 1]) == 0
    assert min([4, 0, 2, 1]) == 0



# Generated at 2022-06-22 11:57:31.075788
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("42") == 42
    assert human_to_bytes("42B") == 42
    assert human_to_bytes("42K") == 43008
    assert human_to_bytes("42k") == 43008
    assert human_to_bytes("42Ki") == 43348
    assert human_to_bytes("1.0Ki") == 1024
    assert human_to_bytes("1.0KiB") == 1024
    assert human_to_bytes("1.5Ki") == 1536
    assert human_to_bytes("1.5KiB") == 1536
    assert human_to_bytes("42M") == 44040192
    assert human_to_bytes("42Mi") == 45088768
    assert human_to_bytes("42m") == 44040192
    assert human_to_

# Generated at 2022-06-22 11:57:36.112768
# Unit test for function min
def test_min():
    """
    Test the min function.

    Notes:
      The min function should return the minimum number given a list of integers
    """

    test_list = [1000, 2000, 3000, 4000, 5000]

    result = min(None, test_list)

    assert result == 1000



# Generated at 2022-06-22 11:57:37.424439
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3


# Generated at 2022-06-22 11:57:48.040982
# Unit test for function min
def test_min():
    impor = None
    try:
        import jinja2
        impor = jinja2
    except ImportError:
        pass
    if impor:
        environment = jinja2.Environment()
        func = environment.filters['min']

        result = func(4, 5)
        assert result == 4

        # test with non-numeric arguments
        result = func(4, "5")
        assert result == 4

        result = func("4", "5")
        assert result == 4

        wrong_result = func([4,5,6], 10)
        assert result != wrong_result

        # test with keyword arguments
        if HAS_MIN_MAX:
            result = func([4,5,6], key=lambda x: -x)
            assert result == 6


# Generated at 2022-06-22 11:57:55.825701
# Unit test for function unique
def test_unique():
    for case in [[1, 2, 3, 3], ['foo', 'foo', 'bar']]:
        assert unique(None, case) == list(set(case))

    # test jinja2 unique fallback
    try:
        unique(None, [1, 2, 3, 3], case_sensitive=False)
        assert False, "'unique' should have failed as case_sensitive=False is not handled by ansible"
    except AnsibleFilterError:
        pass



# Generated at 2022-06-22 11:58:16.667023
# Unit test for function rekey_on_member
def test_rekey_on_member():
    test_input = [{'name': 'foo', 'value': 'bar'}, {'name': 'baz', 'value': 'quux'}]
    assert(rekey_on_member(test_input, 'name') == {'foo': {'name': 'foo', 'value': 'bar'}, 'baz': {'name': 'baz', 'value': 'quux'}})

# Generated at 2022-06-22 11:58:27.226757
# Unit test for function min
def test_min():
    # Test
    assert min([3, 2]) == 2
    assert min([3, 0], [1, 2]) == [0, 1]
    assert min(-2, [1, 2], [3, 4]) == [-2, 1, 3]
    assert min(-2, -2) == -2
    assert min(-2, [1, -2], [-3, 4]) == [-3, -2, -2]
    assert min(1, [1, -2], [-3, 4]) == [1, 1, -3]
    assert min(1, [1, -2], [-1, 4]) == [1, 1, -1]


# Generated at 2022-06-22 11:58:35.114653
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([1.1, 2.2, 3.3, 4.4]) == 1.1
    assert min([1.1, 3.2, 2.3, 4.4]) == 1.1
    assert min([[1], [3], [2], [4]]) == [1]
    assert min(['a', 'b', 'c', 'd']) == 'a'
    assert min(['a', 'c', 'b', 'd']) == 'a'
    assert min([[1], [2], [3]]) == [1]


# Generated at 2022-06-22 11:58:44.186607
# Unit test for function inversepower
def test_inversepower():
    assert 3.46410161514 == inversepower(12, 2)
    assert 2.0 == inversepower(4, 2)
    assert 1.0 == inversepower(2, 2)
    assert 1.73205080757 == inversepower(3, 2)
    assert 1.0 == inversepower(1, 2)
    assert 0.0 == inversepower(0, 2)
    assert -1.0 == inversepower(-1, 2)
    assert -1.73205080757 == inversepower(-3, 2)
    assert -2.0 == inversepower(-4, 2)
    assert -3.46410161514 == inversepower(-12, 2)

# Generated at 2022-06-22 11:58:46.715854
# Unit test for function min
def test_min():
    from ansible.module_utils.six.moves import builtins
    builtins.__dict__['min'] = None

    assert min([1, 2]) == 1
    assert min([-1, -2]) == -2



# Generated at 2022-06-22 11:58:57.387028
# Unit test for function max
def test_max():
    assert max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert max([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]) == 0.9
    assert max(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == 'g'
    assert max('abcdefg') == 'g'
    assert max((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) == 9
    assert max((0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)) == 0.9



# Generated at 2022-06-22 11:59:07.994865
# Unit test for function rekey_on_member
def test_rekey_on_member():

    assert_equal = lambda a, b: a == b

    data = [
        {'name': 'a', 'offset': 1},
        {'name': 'b', 'offset': '2'},
        {'name': 'c', 'offset': '3'},
    ]
    result = {
        'a': {'name': 'a', 'offset': 1},
        'b': {'name': 'b', 'offset': '2'},
        'c': {'name': 'c', 'offset': '3'}
    }

    assert (rekey_on_member(data, 'name', 'error') == result)
    assert (rekey_on_member(data, 'name', 'overwrite') == result)


# Generated at 2022-06-22 11:59:11.888822
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 2, 3], 1) == 3
    assert max([1, 2, 3], -1) == 3
    assert max([1, 2, 3], default=1) == 3
    assert max([1, 2, 3], default=1, attribute='x') == 3
    assert max([1, 2, 3], default=1, attribute='x', boolean=True) == 3


# Generated at 2022-06-22 11:59:16.539179
# Unit test for function unique
def test_unique():
    assert unique([1, 2, 3, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 2, 3, 3, 3, 4, 5], False) == [1, 2, 3, 4, 5]
    assert unique([1, 2, 3, 3, 3, 4, 5], True) == [1, 2, 3, 4, 5]
    assert unique([1, 2, 3, 3, 3, 4, 5], True, None) == [1, 2, 3, 4, 5]

# Generated at 2022-06-22 11:59:21.290657
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(1024) == "1K"
    assert human_readable(1024, isbits=True) == "8K"
    assert human_readable(1024, unit='B') == "1024B"
    assert human_readable(1024, unit='K') == "1K"


# Generated at 2022-06-22 12:00:26.510894
# Unit test for function min
def test_min():
    assert min([4, 2, 1, 3]) == 1
    assert min([4, -2, -1, 3]) == -2
    assert min([-4, -2, -1, -3]) == -4

    assert min([-4, -20, -1, -3]) == -20
    assert min([4.2, 2.1, 1.3, 3.4]) == 1.3
    assert min([4, 2, 1.5, 3]) == 1.5
    assert min([4, 2, 1, 3]) == 1

    assert min([4.2, 2.1, 1.5, 3.4, 0]) == 0
    assert min([-1, 4, -2, -1, 3]) == -2

    # iterables

# Generated at 2022-06-22 12:00:38.676666
# Unit test for function max
def test_max():
    test_object = {}
    assert max(test_object, 'test') == 'test'
    assert max(test_object, 'test', 'testing') == 'testing'
    assert max(test_object, 'test', 'b') == 'test'
    assert max(test_object, 2, 3) == 3
    assert max(test_object, 2, 3, key=lambda x: -x) == 2
    assert max(test_object, [1, 2], [3, 4]) == [3, 4]
    assert max(test_object, [3, 4], [1, 2]) == [3, 4]
    assert max(test_object, [1, 2], [2, 3]) == [2, 3]
    assert max(test_object, [2, 3], [1, 2]) == [2, 3]
