

# Generated at 2022-06-22 11:51:04.676294
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import unittest
    import doctest

    class TestRekeyOnMember(unittest.TestCase):

        def test_rekey_on_member(self):
            """
            Run doctests for function rekey_on_member.
            """

            results = doctest.testmod(rekey_on_member)
            self.assertTrue(results[0] == 0  or  results[0] == 1)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestRekeyOnMember)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-22 11:51:16.513403
# Unit test for function min
def test_min():

    def test_min(env, a, b, expected_result):
        actual_result = min(env, a, b)
        assert actual_result == expected_result

    env = {}

    test_min(env, [4, 6], [1, 3], [4, 3])
    test_min(env, [4, 6], [1, 3, 7], [4, 3])
    test_min(env, [4, 6, 8], [1, 3], [4, 3])
    test_min(env, [4, 6], [1, 3, 5, 7, 9, 11], [4, 3])
    test_min(env, [1, 5, 11], [2, 7], [1, 5])

    # Test that kwargs are not supported

# Generated at 2022-06-22 11:51:21.376708
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([1, 2, 3], attribute='foo') == 1
    # case_sensitive=False is not supported
    assert min([1, 2, 3], case_sensitive=False, attribute='foo') == 1



# Generated at 2022-06-22 11:51:26.930899
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([1, 2, 3, 4], attribute='x') == 1
    assert min([{'x': 1}, {'x': 2}, {'x': 3}, {'x': 4}], attribute='x') == {'x': 1}



# Generated at 2022-06-22 11:51:28.620757
# Unit test for function min
def test_min():
    v = min([1, 2, 3])
    assert v == 1


# Generated at 2022-06-22 11:51:38.179994
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.module_utils.six import iteritems
    # Test invalid values of duplicates parameter
    try:
        rekey_on_member([], 'foo', 'bad')
    except AnsibleFilterError:
        pass
    else:
        assert False, "Should have raised an exception"

    # Test integer keys
    data = {"id": 1, "foo": "bar", "baz": 4.0}
    rekeyed = rekey_on_member(data, 'id')
    assert rekeyed == {1: data}, "Integer key did not work right"

    # Test string keys
    data = {"id": "foo", "foo": "bar", "baz": 4.0}
    rekeyed = rekey_on_member(data, 'id')

# Generated at 2022-06-22 11:51:44.423223
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([1.1, 2.2, 3.3, 4.4]) == 1.1
    assert min("abcd") == "a"
    assert min("abcd", "xyz") == "abcd"



# Generated at 2022-06-22 11:51:54.624282
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import copy

    test_keys = [
        'a',
        'a',
        'b',
        'b',
        'b',
        'c',
        'c',
        'c',
        'c',
        'd',
        'd',
        'd',
        'd',
        'd',
    ]

    test_values = range(len(test_keys))

    rekey_data_list = [dict(zip(test_keys, test_values))]
    rekey_data_dict = dict(zip(test_keys, test_values))

    rekey_transform = 'a'

# Generated at 2022-06-22 11:51:58.716112
# Unit test for function min
def test_min():
    if HAS_MIN_MAX:
        assert min(range(5), start=10) == 10
        assert min([1, 2, 10, 20, 5], attribute='start') == 1
    else:
        assert min(range(5)) == 0



# Generated at 2022-06-22 11:52:03.533771
# Unit test for function min
def test_min():
    ansible_unfiltered_values = [2, 0, 1, 7, 6, 5, 4, 3, 6]
    jinja2_filtered_values = ansible_unfiltered_values[:]

    assert min(ansible_unfiltered_values) == min(jinja2_filtered_values)



# Generated at 2022-06-22 11:52:24.250899
# Unit test for function rekey_on_member
def test_rekey_on_member():
    data = {'a': {'key': 'value'}, 'b': {1: 2, 'key': 'other value'}}
    ansible_filter = FilterModule()
    test = ansible_filter.filters()['rekey_on_member'](data, 'key')
    assert test == {'value': {'key': 'value'}, 'other value': {1: 2, 'key': 'other value'}}

    data = [{1: 2, 'key': 'value'}, {2: 3, 'key': 'other value'}]
    ansible_filter = FilterModule()
    test = ansible_filter.filters()['rekey_on_member'](data, 'key')

# Generated at 2022-06-22 11:52:34.651501
# Unit test for function min
def test_min():
    def do_test(a, b, c, d, e):
        assert min([a, b, c, d, e]) == filter_instance.filters()['min']([a, b, c, d, e])

    filter_instance = FilterModule()

    do_test(1, 3, 5, 2, 4)
    do_test(1, 0, -1, -2, -3)
    do_test(0, -1, -2, -3, -4)
    do_test(1, 1, 1, 1, 1)
    do_test(0, 0, 0, 0, 0)
    do_test(1, 1, 1.0, 1, 1)


# Generated at 2022-06-22 11:52:39.001953
# Unit test for function max
def test_max():

    assert max([1,2,3,4]) == 4
    assert max(['a', 'b', 'c']) == 'c'
    assert max([1, 'b', 'c']) == 'c'
    assert max([1, 'b', 'c', 4]) == 4
    assert max([1, 'b', 'c', 4, []]) == 4

# Generated at 2022-06-22 11:52:51.472364
# Unit test for function human_readable

# Generated at 2022-06-22 11:53:03.927991
# Unit test for function max
def test_max():

    class TestJinja2:
        noparam = 7
        test1 = [1, 2, 3, 4, 5, 6, ]
        test2 = [1, 2, 3, 4, 5, 6, 7]
        test3 = [3, 7, 5]
        test4 = [5, 1, 2, 9]
        test5 = (1, 2, 3, 4, 5, 6)
        test6 = {1, 2, 3, 4, 5, 6}
        test7 = [{'key': 'a', 'value': 2}, {'key': 'z', 'value': 3}, {'key': 'c', 'value': 1}]

        def __init__(self):
            self.noparam = 2
            self.test1 = [1, 2, 3, 4, 5, 6, 7]

# Generated at 2022-06-22 11:53:15.252731
# Unit test for function logarithm
def test_logarithm():
    a = logarithm(math.e)
    assert a == 1, 'log(math.e) should be 1'
    a = logarithm(10)
    assert a == 1, 'log(10) should be 1'
    a = logarithm(100, 10)
    assert a == 2, 'log(100) with base 10 should be 2'
    try:
        a = logarithm('test')
        assert False, 'log() should not accept string'
    except AnsibleFilterTypeError as e:
        a = e
    assert 'can only be used on numbers' in to_text(a), 'log() should not accept string'

# Generated at 2022-06-22 11:53:27.492847
# Unit test for function max
def test_max():
    # positive tests
    assert max([1, 2, 3]) == 3
    assert max([10, 1, 3]) == 10
    assert max((1, 2, 3)) == 3
    assert max((10, 1, 3)) == 10
    assert max([-1, -2, -3]) == -1
    assert max({1: 10, 3: 30, 2: 20}) == 3
    assert max({'a': 1, 'b': 2, 'c': 3}) == 'c'
    assert max("abcd") == 'd'
    assert max("abc") == 'c'
    assert max("aC") == 'a'
    assert max("a", key=lambda x: x.lower()) == 'a'
    assert max("C", key=lambda x: x.lower()) == 'C'

# Generated at 2022-06-22 11:53:38.658141
# Unit test for function min
def test_min():
    def _raise_if(condition, *args):
        if condition:
            raise AnsibleFilterError(*args)

    assert min([1, 2, 3]) == 1
    assert min([1, 2, 3], default=0) == 1
    assert min([1, 2, 3], default=5) == 1
    assert min([], default=5) == 5
    _raise_if(min([], default=None) is None, 'min() of empty list without default should return 5')
    assert min([1, 2, 3, 4, 5], start=2) == 3
    assert min([1, 2, 3, 4, 5], start=10) == 10
    assert min([], start=5) == 5
    _raise_if(min([], start=None) is None, 'min() of empty list with start should return 5')


# Generated at 2022-06-22 11:53:39.378424
# Unit test for function min
def test_min():
    assert min(1, 2, 3) == 1


# Generated at 2022-06-22 11:53:43.686832
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5]) == 1
    assert min([1, 2, 3, 4, 5], attribute='attr') == 1
    assert min([1, 2, 3, 4, 5], case_sensitive=False) == 1



# Generated at 2022-06-22 11:54:01.640645
# Unit test for function rekey_on_member
def test_rekey_on_member():
    assert rekey_on_member(dict(a=dict(z=1), b=dict(z=2)), 'z', duplicates='overwrite') == {1: dict(z=1), 2: dict(z=2)}
    assert rekey_on_member([dict(z=1), dict(z=2)], 'z', duplicates='overwrite') == {1: dict(z=1), 2: dict(z=2)}

    try:
        rekey_on_member([dict(z=1), dict(z=2)], 'z', duplicates='error')
    except AnsibleFilterError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-22 11:54:12.570733
# Unit test for function min
def test_min():
    from ansible.module_utils.common.text import format_datetime
    assert min([1, 2, 3]) == 1
    assert min([10, 2, 30]) == 2
    assert min([10, 2, 30], attribute='length') == 30
    assert min([{'a': 10, 'b': 2}, {'a': 20, 'b': 1}], attribute='b.length') == 2
    dt = format_datetime(u"2018-07-05T12:15:30.3394021-00:00")
    assert min([dt, u"2018-07-05T12:15:30.3394021-00:00"], attribute='timestamp') == dt
    assert min(['foo', 'foobar', 'foobarbaz'], attribute='length') == 'foo'
    raise AnsibleFilterError

# Generated at 2022-06-22 11:54:18.053840
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([1, 2, -3]) == -3
    assert min([5, 4, 3, 2, 1]) == 1
    assert min(None, [5, 4, 3, 2, 1]) == 1
    assert min(0, [5, 4, 3, 2, 1]) == 1



# Generated at 2022-06-22 11:54:19.366498
# Unit test for function max
def test_max():
    obj = FilterModule()
    assert obj.filters()['max']([1, 2]) == 2


# Generated at 2022-06-22 11:54:30.488574
# Unit test for function rekey_on_member
def test_rekey_on_member():
    '''
    This method tests the rekey_on_member filter.
    '''
    l1 = [
        {'name': 'foo', 'data': 'bar'},
        {'name': 'fooz', 'data': 'baz'},
        {'name': 'bam', 'data': 'boom'},
    ]
    l2 = [
        {'name': 'foo', 'data': 'bar'},
        {'name': 'foo', 'data': 'baz'},
        {'name': 'bam', 'data': 'boom'},
    ]

# Generated at 2022-06-22 11:54:39.729518
# Unit test for function max
def test_max():
    assert max([5, 1, 3, 11]) == 11
    assert max({'a': 1, 'b': 5}) == 'b'
    assert max('bcad') == 'd'
    assert max(5, 1, 3, 11) == 11
    assert max((5, 1, 3, 11)) == 11
    assert max(a=1, b=5) == 5
    try:
        max(1, 5, 'a')
    except AnsibleFilterTypeError as e:
        assert str(e) == 'max() can only be used on numbers'
    else:
        assert False, 'AnsibleFilterTypeError not raised'


# Generated at 2022-06-22 11:54:43.176741
# Unit test for function min
def test_min():
    m = FilterModule()
    filter_result = m.filters()['min']([6, 2, 9, 3, 1, 4, 6, 2])
    assert filter_result == 1, "'min' filter returned %s instead of %s" % (filter_result, 1)


# Generated at 2022-06-22 11:54:54.328651
# Unit test for function min
def test_min():
    assert min([1,2,3]) == 1
    assert min([1,2,3], 2) == 1
    assert min([1,2], 3) == 1
    assert min([1,2,3], 2, 3) == 1

    assert min('hello') == 'e'
    assert min('hello', 'e') == 'e'
    assert min('hello', 'abcde') == 'e'
    assert min('hello', 'abcde', 'e') == 'e'

    assert min(1,2) == 1
    assert min(3,2,1) == 1
    assert min(3,2,1,1) == 1

    assert min('a','b','c') == 'a'


# Generated at 2022-06-22 11:55:00.777337
# Unit test for function max
def test_max():
    assert max([1, 2]) == 2
    assert max([1, 2.0]) == 2.0
    assert max((1, 2)) == 2
    assert max((1, 2.0)) == 2.0

    assert max([1, 2], [3, 4], [5, 6]) == [5, 6]
    assert max([1, 2], (3, 4), [5, 6]) == [5, 6]
    assert max((1, 2), (3, 4), (5, 6)) == (5, 6)

# Generated at 2022-06-22 11:55:04.036035
# Unit test for function max
def test_max():
    assert max(['a', 'b', 'c']) == 'c'
    assert max([1, 2, 3]) == 3



# Generated at 2022-06-22 11:55:15.714968
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([3, 2, 1]) == 3
    assert max([1, 3, 2]) == 3


# Generated at 2022-06-22 11:55:27.182157
# Unit test for function min
def test_min():
    """Unit test for function min"""
    display = Display()

    def testcase(a, expected, case_sensitive=None, attribute=None):
        try:
            c = min(a, case_sensitive=case_sensitive, attribute=attribute)
            display.display('\nmin(%s) returned %s, expected %s' % (a, c, expected))
        except Exception as e:
            display.display('\nmin(%s) failed: %s' % (a, e))

    testcase([8, 10, 12], 8)
    testcase([1.2, 8.4, 9.4], 1.2)
    testcase([8], 8)
    testcase([5, 6, 5, 6], 5)
    testcase([5, 6, 7, 5, 6], 5)

# Generated at 2022-06-22 11:55:28.692508
# Unit test for function min
def test_min():
    assert min([10, 2, 34, 23]) == 2


# Generated at 2022-06-22 11:55:37.183609
# Unit test for function min
def test_min():
    f = FilterModule()
    test_min = f.filters()['min']
    assert test_min([1, 2, 3]) == 1
    assert test_min([1, 2, 3], 2) == 1
    assert test_min([1, 2, 3], 3) == 3
    assert test_min([-10, -2, 5]) == -10
    assert test_min(["a", "b", "c"]) == 'a'
    assert test_min([1, "a", 2]) == 1



# Generated at 2022-06-22 11:55:43.414881
# Unit test for function max
def test_max():
    display.vvv('We have the following functions from above:')
    display.vvv(globals())
    display.vvv('Let us import them')
    from ansible.plugins.filter.core import FilterModule
    display.vvv('We just imported FilterModule')
    x = FilterModule()
    display.vvv('We just instantiated FilterModule as x')
    y = x.filters()
    display.vvv('We just took FilterModule, x, and pulled out the functions using filters()')
    assert(y['max'] == max)

# Generated at 2022-06-22 11:55:47.367332
# Unit test for function max
def test_max():
    assert max([0, -1, 1, 2, -2]) == 2
    assert max(['a', 'b', 'c']) == 'c'
    assert max(['a', 'b', '']) == 'b'


# Generated at 2022-06-22 11:55:59.169290
# Unit test for function human_to_bytes
def test_human_to_bytes():

    # test conversion with default unit
    assert human_to_bytes('3') == 3
    assert human_to_bytes('3', None, False) == 3

    # test conversion with default unit with suffix
    assert human_to_bytes('3B') == 3
    assert human_to_bytes('3B', None, False) == 3

    # test conversions with invalid unit
    assert human_to_bytes('3Z') == 3
    assert human_to_bytes('3Z', None, False) == 3

    # test conversions with invalid size
    assert human_to_bytes('ZZ') == 'ZZ'
    assert human_to_bytes('ZZ', None, False) == 'ZZ'
    assert human_to_bytes('ZZ', 'B', False) == 'ZZ'

    # test conversion with specified unit

# Generated at 2022-06-22 11:56:03.450174
# Unit test for function min
def test_min():
    min_result = min([0, 1, 2])
    assert min_result == 0

    try:
        min_result = min([0])
    except AnsibleFilterTypeError as e:
        assert to_native(e) == "too few arguments"

    assert min(2, 3, 4) == 2
    assert min(3, 2, 4) == 2
    assert min(4, 3, 2) == 2
    assert min(2, 3, 2) == 2
    assert min([2, 3, 4]) == 2
    assert min([3, 2, 4]) == 2
    assert min([4, 3, 2]) == 2
    assert min([2, 3, 2]) == 2


# Generated at 2022-06-22 11:56:07.393679
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 2, 3], [4, 5, 6]) == [4, 5, 6]
    assert max([1, 2, 3], [4, 1, 6]) == [4, 2, 6]


# Generated at 2022-06-22 11:56:12.032388
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5]) == 1
    assert min([5, 4, 3, 2, 1]) == 1

    assert min((5, 4, 3, 2, 1)) == 1
    assert min((1, 2, 3, 4, 5)) == 1

    assert min("abcde") == 'a'
    assert min("edcba") == 'a'


# Generated at 2022-06-22 11:56:36.855375
# Unit test for function min
def test_min():
    from ansible.module_utils._text import to_bytes
    assert min([1, 2, 3]) == 1
    assert min((1, 2, 3)) == 1
    assert min({'a': 1, 'b': 2}) == 1
    assert min(['a', 'b']) == 'a'
    assert min('python') == 'h'
    with pytest.raises(TypeError):
        min(None)
    with pytest.raises(TypeError):
        min(1)
    assert min(1, 2, 3) == 1
    assert min((1, 2, 3), key=lambda x: x % 3) == 3

    # Verify Strings are compared as Bytes
    assert min('åb') == to_bytes('å')



# Generated at 2022-06-22 11:56:39.923704
# Unit test for function min
def test_min():
    assert min([5, 6, 2, 10, 2, 1, 2, 1]) == 1
    assert min(['5', '6', '2', '10', '2', '1', '2', '1']) == '1'


# Generated at 2022-06-22 11:56:42.204185
# Unit test for function max
def test_max():
    assert FilterModule().filters()['max']([1, 2, 3]) == 3



# Generated at 2022-06-22 11:56:53.566015
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([10, 3, 5, 6, 2]) == 10
    assert max([]) is None
    assert max([1, 2, None, 3]) is None
    assert max([1, 2, {'foo': 'bar'}]) == {'foo': 'bar'}
    assert max(1, 2, 3) == 3
    assert max(10, 3, 5, 6, 2) == 10
    assert max() is None
    assert max(1, 2, None, 3) is None
    assert max(1, 2, {'foo': 'bar'}) == {'foo': 'bar'}
    assert max([1, 2, 3], key=int) == 3
    assert max([10, 3, 5, 6, 2], key=int) == 10
    assert max

# Generated at 2022-06-22 11:57:04.846663
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min((1, 2, 3)) == 1
    assert min(['a', 'b', 'c']) == 'a'
    assert min(('a', 'b', 'c')) == 'a'
    assert min({'a': '1', 'b': '2', 'c': '3'}) == 'a'
    assert min([1, 2, 3], key=lambda x: -x) == 3
    assert min(['a', 'b', 'c'], key=lambda x: x[0]*3) == 'c'
    assert min((1, 2, 3), key=lambda x: -x) == 3
    assert min(['a', 'b', 'c'], key=lambda x: x[0]*3) == 'c'
    assert min

# Generated at 2022-06-22 11:57:05.349879
# Unit test for function min
def test_min():
    assert min(range(10)) == 0



# Generated at 2022-06-22 11:57:07.600609
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([5, -1, 4, 0]) == -1
    assert min((4, 1, 0)) == 0
    assert min({'a': 'apple', 'b': 'banana', 'c': 'cat'}) == 'a'
    assert min({1: 'apple', 4: 'banana', 0: 'cat'}) == 0


# Generated at 2022-06-22 11:57:10.681908
# Unit test for function min
def test_min():
    assert min([2, 3, 4, 1]) == 1

    assert min([[1, 2], [3], [4, 5, 6]], key=len) == [3]



# Generated at 2022-06-22 11:57:18.999096
# Unit test for function max
def test_max():
    if HAS_MIN_MAX:
        assert 25 == max(24, 25)
        assert (25, 24, 26) == max((24, 25, 26), (25, 24, 26))
    else:
        assert 25 == max((25, 24, 26))
        # use builtins.max to avoid collision with jinja2.filters
        assert 25 == __builtins__.get('max')((25, 24, 26))
        assert 25 == __builtins__.get('max')((25, 24, 26), (24, 25, 26))



# Generated at 2022-06-22 11:57:21.427159
# Unit test for function min
def test_min():

    min_obj = min([10, 6, 2, -1, -3, 15])

    assert min_obj == -3



# Generated at 2022-06-22 11:58:23.765760
# Unit test for function min
def test_min():
    # First check the simple case of a list of numbers
    # If a list of ints, expect the function to return the smallest int
    test_list = [1, 2, 3, 4]
    assert min(test_list) == 1
    # If a list of floats, expect the function to return the smallest float
    test_list = [1.0, 2.0, 3.0, 4.0]
    assert min(test_list) == 1.0

    # Now check the case of a list of strings
    # If 'key' argument is specified, expect function to return the smallest basing on 'key' argument
    test_list = ['10.0.0.0', '10.0.0.1', '10.0.0.10', '10.0.0.2', '10.0.0.3']

# Generated at 2022-06-22 11:58:30.182987
# Unit test for function min
def test_min():
    assert min([2, 3, 1]) == 1
    assert min([2, 3, 1], attribute='value') == 1
    assert min([{'value': 2}, {'value': 3}, {'value': 1}], attribute='value') == {'value': 1}
    assert min([{'value': 2}, {'value': 3}, {'value': 1}], attribute='value', case_sensitive=False) == {'value': 1}



# Generated at 2022-06-22 11:58:31.338455
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1

# Generated at 2022-06-22 11:58:39.575808
# Unit test for function unique

# Generated at 2022-06-22 11:58:48.345962
# Unit test for function max
def test_max():
    value = [1, 2, 3, 4, 5]
    got = max(value)
    assert got == 5

    value = [5, 4, 3, 2, 1]
    got = max(value)
    assert got == 5

    value = ['a', 'de', 'bb', 'c']
    got = max(value)
    assert got == 'de'

    try:
        value = [1, 2, 'b']
        got = max(value)
        assert False, 'Expected AnsibleFilterError'
    except AnsibleFilterError as e:
        assert 'max filter requires all items are of same type' in to_text(e)

    assert max([1, 2], key=lambda x: x+1) == 2



# Generated at 2022-06-22 11:58:51.892427
# Unit test for function min
def test_min():
    assert min([4, 3, 2, 1]) == 1
    assert min([4, 3, 2, 1], attribute='attr') == 1
    assert min([4, 3, 2, 1], key=lambda x: -x) == 4


# Generated at 2022-06-22 11:59:01.208113
# Unit test for function max
def test_max():
    assert max([1, 0, 2, 3]) == 3
    assert max(['1', '0', '2', '3']) == '3'
    assert max([1, '0', 2, '3']) == 2
    assert max([1, 2, 3], 2) == 2
    assert max([1, 2, 3], attribute='qux') == 3
    assert max([{'qux': 5}, {'qux': 3}], attribute='qux') == {'qux': 5}
    assert max([[1], [3]], attribute=0) == [3]


# Generated at 2022-06-22 11:59:10.156516
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([1, 2, 3], 2) == 1
    assert min([0, -10, 10]) == -10
    assert min([0, -10, 10], 1) == -10
    assert min([0, -10, 10], 0) == 1
    assert min([1, 2, 3], start=1) == 1
    assert min([1, 2, 3], start=2) == 2
    assert min([1, 2, 3], start=3) == 3
    assert min([1, 2, 3], start=4) == 4



# Generated at 2022-06-22 11:59:14.529460
# Unit test for function max
def test_max():
    assert max(1, 2, 3, 4) == 4
    assert max([1, 2, 3, 4]) == 4
    assert max([1, 2, 4, 1], 2) == 4
    assert max([1, 2, 4, 1], 2, key=str) == 1

# Generated at 2022-06-22 11:59:18.679020
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("2a") == 42 and human_to_bytes("2A") == 42
    assert human_to_bytes("0t") == 0
    assert human_to_bytes("9p") == 9 * math.pow(10, 15)
    assert human_to_bytes("9P") == 9 * math.pow(10, 15)
    assert human_to_bytes("1e") == 1 * math.pow(10, 18)
    assert human_to_bytes("1E") == 1 * math.pow(10, 18)
    assert human_to_bytes("1z") == 1 * math.pow(10, 21)
    assert human_to_bytes("1Z") == 1 * math.pow(10, 21)
    assert human_to_bytes("1y") == 1 * math

# Generated at 2022-06-22 12:00:37.905457
# Unit test for function max
def test_max():
    ''' Test max filter '''
    f = FilterModule()
    max_filter = f.filters()['max']

    assert max_filter([1, 2, 3, 4, 5]) == 5
    assert max_filter([3, 2, 5, 1, 4]) == 5
    assert max_filter([{'a': 5}, {'a': 2}, {'a': 3}, {'a': 4}, {'a': 1}], attribute='a') == {'a': 5}
    assert max_filter([1, 2, 3, 4, 5], 'error') == 5
    assert max_filter([1, 2, 3, 4, 5], 10) == 5
    assert max_filter([1, 2, 3, 4, 5], 10, 'error') == 5
    assert max_filter([]) == None
    assert max_filter