

# Generated at 2022-06-22 11:51:09.282327
# Unit test for function max
def test_max():
    assert max(['ab', 'a', 'abc']) == 'abc'
    assert max([1, 2, 3, 'abc']) == 'abc'
    assert max([1, ([2, 3, 4], 'abc')]) == ([2, 3, 4], 'abc')
    assert max([1, {2: 'a'}]) == {2: 'a'}
    assert max(['123', '1']) == '123'
    assert max([1, '1']) == '1'
    assert max([[1, 'a'], [2, 'b'], [3, 'c']]) == [3, 'c']
    assert max(['abc', 'bcd', 'cde'], key=len) == 'cde'

# Generated at 2022-06-22 11:51:20.088225
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(2, False) == '2 B'
    assert human_readable(2.0, False) == '2 B'
    assert human_readable(2, True) == '2 B'
    assert human_readable(2.0, True) == '2 B'
    assert human_readable(1024, False) == '1.0 KB'
    assert human_readable(1024.0, False) == '1.0 KB'
    assert human_readable(1024, True) == '8.0 Kb'
    assert human_readable(1024.0, True) == '8.0 Kb'
    assert human_readable(1024000, False) == '1000.0 KB'
    assert human_readable(1024000, True) == '8.0 Mb'

# Generated at 2022-06-22 11:51:22.541120
# Unit test for function max
def test_max():
    assert jinja2.Environment().from_string('{{ [1, 2, 3]|max }}').render() == '3'



# Generated at 2022-06-22 11:51:34.201048
# Unit test for function max
def test_max():
    class FilterModule(object):
        def filters(self):
            return {'max': max}

    def test_max1():
        f = FilterModule()
        filters = f.filters()
        assert filters['max']([1, 2, 3]) == 3
        assert filters['max']([1, 3, 2]) == 3
        assert filters['max']([3, 2, 1]) == 3

    def test_max_key():
        f = FilterModule()
        filters = f.filters()
        # Test with dictionaries
        assert filters['max']([{'a': 1, 'b': 3}, {'a': 3, 'b': 2}, {'a': 1, 'b': 4}], key='a') == {'a': 3, 'b': 2}
        # Test with nested dictionaries when key

# Generated at 2022-06-22 11:51:35.823586
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min(1, 2, 3) == 1



# Generated at 2022-06-22 11:51:46.105147
# Unit test for function min
def test_min():
    assert min(10, 15) == 10
    assert min([10, 15]) == 10
    assert min([10, 15], [11, 14]) == [10, 14]
    assert min([10, 15], [12, 14]) == [10, 14]
    assert min([10, 15], [11, 14], key=lambda x: x[0]) == [10, 14]
    assert min([10, 15], [11, 14], key=lambda x: x[1]) == [10, 15]
    assert min([10, 15], [12, 14], key=[1, 0]) == [11, 15]


# Generated at 2022-06-22 11:51:56.199032
# Unit test for function unique
def test_unique():
    assert unique([1, 1, 2, 3, 3]) == [1, 2, 3]
    assert unique([1, 1, 1, 3, 3]) == [1, 3]
    assert unique([1, 1, 1, 1, 1]) == [1]
    assert unique([1]) == [1]
    assert unique([1, 2, 3]) == [1, 2, 3]
    assert unique([]) == []
    assert unique('abcdabcd') == ['a', 'b', 'c', 'd']
    assert unique('abcdabcc') == ['a', 'b', 'c', 'd']
    assert unique('abcabcabcabc') == ['a', 'b', 'c']
    assert unique('abc') == ['a', 'b', 'c']
    assert unique('a') == ['a']

# Generated at 2022-06-22 11:52:08.301852
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("1") == 1
    assert human_to_bytes("1B") == 1
    assert human_to_bytes("1024B") == 1024
    assert human_to_bytes("1K") == 1024
    assert human_to_bytes("1KiB") == 1024
    assert human_to_bytes("1M") == 1048576
    assert human_to_bytes("1MiB") == 1048576
    assert human_to_bytes("1G") == 1073741824
    assert human_to_bytes("1GiB") == 1073741824
    assert human_to_bytes("1T") == 1099511627776
    assert human_to_bytes("1TiB") == 1099511627776
    assert human_to_bytes("1P") == 1125899906842624
    assert human

# Generated at 2022-06-22 11:52:20.160833
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([10, 3, 5, 6, 2]) == 10

    # Test keyword args
    assert max([1, 2, 3], -1) == 3
    assert max([1, 2, 3], 0) == 3
    assert max([1, 2, 3], 1) == 3
    assert max([1, 2, 3], 2) == 3
    assert max([1, 2, 3], 3) == 3
    assert max([1, 2, 3], 4) == 4
    assert max([1, 2, 3], default=4) == 3
    assert max([1, 2, 3], default=3) == 3
    assert max([1, 2, 3], default=2) == 3
    assert max([1, 2, 3], default=1) == 3

# Generated at 2022-06-22 11:52:32.153396
# Unit test for function max
def test_max():
    filters = FilterModule()
    assert filters.filters()['max']([1, 2, 3, 4, 5]) == 5
    assert filters.filters()['max'](['1', '2', '3', '4', '5']) == '5'
    assert filters.filters()['max']([1, 2, 3, 4, 5], key=abs) == -5
    assert filters.filters()['max'](['1', '2', '3', '4', '5'], key=len) == '111111'
    assert filters.filters()['max'](['1', '2', '3', '4', '5'], key=len) == '111111'
    assert filters.filters()['max'](['1', '2', '3', '4', '5'], reverse=False)

# Generated at 2022-06-22 11:52:42.888695
# Unit test for function max
def test_max():
    assert max(1, 2) == 2
    assert max([1, 2]) == 2
    assert max([2, 1]) == 2
    assert max(1) == 1
    assert max([1]) == 1
    assert max(2, 3, 4) == 4
    assert max([1, 2], [3, 4]) == [3, 4]

# Generated at 2022-06-22 11:52:46.358040
# Unit test for function min
def test_min():
    assert min(None, [1, 2, 3, 4]) == 1
    assert min(None, [1, 2, 3, 4], 0) == 0


# Generated at 2022-06-22 11:52:52.035806
# Unit test for function min
def test_min():
    for f in [('{{ [5, 3, 2, 4, 1] | min }}', 1),
              ('{{ [5, 3, 2, 4, 1] | min(attr="name") }}', 1),
              ('{{ [{"name": 5}, {"name": 3}, {"name": 2}] | min(attr="name") }}', 2)]:
        assert f[0] == f[1], '%s should return %s' % (f[0], f[1])

# Generated at 2022-06-22 11:53:04.512139
# Unit test for function max
def test_max():
    # Test with a list of integers, expected behaviour
    assert max([1, 2, 3]) == 3

    # Test with a list of strings, expected behaviour
    assert max(['1', '2', '3']) == '3'

    # Test with a list of integers, expected behaviour
    assert max([1, 2, 31, -3]) == 31

    # Test with a list of strings, expected behaviour
    assert max(['1', '2', '31', '-3']) == '2'

    # Test with an empty list, expected behaviour
    assert max([]) is None

    # Test with a tuple, expected behaviour
    assert max((1, 2, 3)) == 3

    # Test with a set, expected behaviour
    assert max({1, 2, 3}) == 3

    # Test with a generator, expected behaviour

# Generated at 2022-06-22 11:53:08.329805
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(100) == math.log(100)
    assert logarithm(100, 10) == math.log10(100)



# Generated at 2022-06-22 11:53:17.109210
# Unit test for function rekey_on_member
def test_rekey_on_member():
    # No duplicates in list of dicts
    data = [
        {'color': 'red', 'name': 'dog', 'species': 'canine'},
        {'color': 'green', 'name': 'frog', 'species': 'amphibian'},
        {'color': 'blue', 'name': 'cat', 'species': 'feline'}
    ]
    result = rekey_on_member(data, 'name')
    expected = {'dog': {'color': 'red', 'name': 'dog', 'species': 'canine'},
                'frog': {'color': 'green', 'name': 'frog', 'species': 'amphibian'},
                'cat': {'color': 'blue', 'name': 'cat', 'species': 'feline'}}
    assert result == expected

    # Duplicates in list

# Generated at 2022-06-22 11:53:18.600518
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(100, 10) == 2


# Generated at 2022-06-22 11:53:29.740732
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.utils.unicode import to_unicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    class Dummy(dict):
        """ A subclass of dict for tests"""
        pass

    # The example data we use
    list_of_dicts = [
        {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
        },
        {
            'key1': 'value4',
            'key2': 'value5',
            'key3': 'value6',
        },
        {
            'key1': 'value7',
            'key2': 'value8',
            'key3': 'value9',
        },
    ]


# Generated at 2022-06-22 11:53:36.748432
# Unit test for function rekey_on_member
def test_rekey_on_member():
    '''Here is a simple test function that can be used for py.test'''
    assert rekey_on_member([
        {'name': 'a', 'key': 'b'},
        {'name': 'c', 'key': 'b'},
        {'name': 'd', 'key': 'e'},
    ], 'key') == {
        'b': {'name': 'c', 'key': 'b'},
        'e': {'name': 'd', 'key': 'e'},
    }

# Generated at 2022-06-22 11:53:43.988936
# Unit test for function max
def test_max():
    assert max([1,2,3,4]) == 4
    assert max(1,2,3) == 3
    assert max(1,2,3, key=lambda x:x*-1) == 1
    assert max(1,2,3,4, key=lambda x:math.sqrt(x)) == 4
    assert max(1,2,3,4, key=lambda x:math.sqrt(x), default=0) == 4
    assert max([1,2,3,4], key=lambda x:math.sqrt(x), default=0) == 4
    assert max(1,2,3,4, key=lambda x:math.sqrt(x), default=0) == 4
    assert max(1,2,3,4, key=lambda x:math.sqrt(x), default=0)

# Generated at 2022-06-22 11:54:02.627539
# Unit test for function human_to_bytes

# Generated at 2022-06-22 11:54:12.198171
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(12) == '12.0B'
    assert human_readable(12, standardsize=True) == '12.0B'
    assert human_readable('12') == '12.0B'

    assert human_readable(1023) == '1023B'
    assert human_readable(1023, standardsize=True) == '1023B'
    assert human_readable('1023', standardsize=True) == '1023B'

    assert human_readable(1024) == '1.0KiB'
    assert human_readable(1024, standardsize=True) == '1.0KiB'
    assert human_readable('1024') == '1.0KiB'

    assert human_readable(2047) == '2.0KiB'

# Generated at 2022-06-22 11:54:14.966364
# Unit test for function max
def test_max():
    filter = FilterModule()
    max = filter.filters()['max']
    assert max(0,1) == 1
    assert max([0,1]) == 1
    assert max([0,1], [2,3]) == [2,3]
    assert max([0,1], [2,3], [4,5]) == [4,5]
    assert max(['a',[1,2]]) == [1,2]
    assert max(['b','c']) == 'c'
    assert max([]) is None


# Generated at 2022-06-22 11:54:18.552967
# Unit test for function min
def test_min():
    assert min([43, 42, 41, 40, 45]) == 40
    assert min("abcd") == "a"
    assert min([]) == None
    assert min("") == None



# Generated at 2022-06-22 11:54:29.829879
# Unit test for function rekey_on_member
def test_rekey_on_member():
    module = FilterModule()
    filters = module.filters()

    # Test a list of dicts
    data = [{'name': 'foo', 'other': 'bar'}, {'name': 'baz', 'other': 'quz'}]
    assert filters['rekey_on_member'](data, 'name') == {'foo': {'name': 'foo', 'other': 'bar'}, 'baz': {'name': 'baz', 'other': 'quz'}}

    # Test a dict of dicts
    data = {'a': {'name': 'foo', 'other': 'bar'}, 'b': {'name': 'baz', 'other': 'quz'}}

# Generated at 2022-06-22 11:54:33.306431
# Unit test for function min
def test_min():
    environment = {'undefined': None}
    assert unique(environment, [1, 2, 3, 2, 1, 3], True) == [1, 2, 3]

# Generated at 2022-06-22 11:54:38.287387
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([1.1, 2.1, 3.1]) == 1.1
    assert min(['a', 'b', 'c']) == 'a'
    assert min([(1, 2), (4,), (3,)]) == (1, 2)



# Generated at 2022-06-22 11:54:42.380072
# Unit test for function max
def test_max():
    #  2nd arg: int
    assert max(1, 2) == 2
    # 2nd arg: float
    assert max(2, 3.0) == 3.0
    # 2nd arg: string
    assert max(2, "3") == 3
    # 2nd arg: unicode
    assert max(2, unicode(3)) == 3



# Generated at 2022-06-22 11:54:54.415760
# Unit test for function min
def test_min():
    module = FilterModule()
    # Test on int
    assert module.filters()['min']([1, 2, 3, 4]) == 1
    assert module.filters()['min']([0, 0, 0, 0]) == 0
    assert module.filters()['min']([-1, -2, -3, -4]) == -4
    assert module.filters()['min']([1]) == 1
    assert module.filters()['min']([]) == None

    # Test on string
    assert module.filters()['min']('abcdef') == 'a'
    assert module.filters()['min']('ABcdeF') == 'A'
    assert module.filters()['min']('A') == 'A'
    assert module.filters()['min']([]) == None


# Generated at 2022-06-22 11:55:05.105711
# Unit test for function rekey_on_member
def test_rekey_on_member():
    # Define some useful test data
    foo = [
        {'name': 'Alice', 'age': 25, 'birthday': 'May 4'},
        {'name': 'Bob', 'age': 49, 'birthday': 'October 17'},
        {'name': 'Cathy', 'age': 12, 'birthday': 'October 15'},
        {'name': 'Dave', 'age': 65, 'birthday': 'July 12'},
        {'name': 'Eugene', 'age': 23, 'birthday': 'May 12'},
        {'name': 'Fred', 'age': 16, 'birthday': 'October 4'},
        {'name': 'Grace', 'age': 28, 'birthday': 'October 20'},
    ]

# Generated at 2022-06-22 11:55:18.791925
# Unit test for function min
def test_min():
    min_tests = [
        ('min', ('a', 'b', 'c'), 'a'),
        ('min', [{'a': 3, 'b': 2}, {'a': 4}, {'a': 2, 'b': 5}], {'a': 2, 'b': 5}),
    ]
    for (fname, args, ans) in min_tests:
        result = min(None, *args)
        assert result == ans, "'%s' != '%s' (%s failed)" % (result, ans, fname)


# Generated at 2022-06-22 11:55:30.681441
# Unit test for function min
def test_min():
    ansible = type('AnsibleModule', (), {})()
    ansible.call_filter = lambda f, x: f(ansible, x)
    assert [7, 10] == ansible.call_filter(min, [7, 10])
    assert [7, 10] == ansible.call_filter(min, [10, 7])
    assert [7, 10] == ansible.call_filter(min, [[7], [10]])
    assert [7, 10] == ansible.call_filter(min, [[10], [7]])
    assert [7, 10] == ansible.call_filter(min, [[7, 10]])
    assert [7, 10] == ansible.call_filter(min, [[10, 7]])

# Generated at 2022-06-22 11:55:35.136875
# Unit test for function symmetric_difference
def test_symmetric_difference():
    x = [1, 2, 4, 6, 8]
    y = [2, 4, 6, 10, 12]
    expected = [1, 8, 10, 12]
    assert sorted(symmetric_difference(None, x, y)) == sorted(expected)


# Generated at 2022-06-22 11:55:40.656454
# Unit test for function symmetric_difference
def test_symmetric_difference():
    assert symmetric_difference('x', '', ['a'], set(['b', 'c', 'd'])) == [('a', 'b', 'c', 'd', 'x')]
    assert symmetric_difference([1, 2], {'a': 1, 'b': 2}) == [1, 2, 'a', 'b']
    assert symmetric_difference('', {}, '123') == []


# Generated at 2022-06-22 11:55:46.334268
# Unit test for function min
def test_min():
    assert isinstance(min([1, 2]), int)
    assert isinstance(min([1, 2], default=3), int)
    assert isinstance(min([{'a': 1}, {'a': 2}], 'a'), dict)
    assert isinstance(min([[1], [2]], -1), list)



# Generated at 2022-06-22 11:55:58.187954
# Unit test for function human_readable
def test_human_readable():

    assert human_readable(1, isbits=False, unit=1024) == '1.00 B'
    assert human_readable(1, isbits=True, unit=1024) == '8.00 b'
    assert human_readable(1024, isbits=False, unit=1000) == '1.00 KB'
    assert human_readable(1024, isbits=True, unit=1000) == '8.19 Kb'
    assert human_readable(100, isbits=False, unit=1000) == '100.00 B'
    assert human_readable(100, isbits=True, unit=1000) == '800.00 b'
    assert human_readable(1000, isbits=False, unit=1000) == '1.00 KB'

# Generated at 2022-06-22 11:56:04.176104
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([4, 3, 2, 1]) == 1
    assert min(range(10, 0, -1)) == 1
    assert min('zaqxswcdevfr') == 'c'
    assert min(['zaqxswcdevfr']) == 'zaqxswcdevfr'
    assert min([]) is None

# Generated at 2022-06-22 11:56:13.257531
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([3, 2, 1]) == 3
    assert max([-1, -2, -3]) == -1
    assert max(1, 2, 3) == 3
    assert max(1, 2, 3, 2) == 3
    assert max(['a', 'b', 'c']) == 'c'
    assert max(['a', 'b', 'c'], key=lambda x: x.lower()) == 'c'
    assert max(['a', 'B', 'C']) == 'a'
    assert max(['a', 'B', 'C'], key=lambda x: x.lower()) == 'C'
    assert max([]) is None
    assert max(1, 2, 3, default=5) == 3

# Generated at 2022-06-22 11:56:24.717579
# Unit test for function max
def test_max():
    # Test standard values
    assert max([1, 2, 3]) == 3
    assert max([1.0, 2.0, 3.0]) == 3.0
    assert max([1, 2, 2.5]) == 2.5

    # Non-iterable values should raise an error
    raises(AnsibleFilterTypeError, 'max(1)')
    raises(AnsibleFilterTypeError, 'max(None)')

    # Test dictionaries
    assert max({'name': 'b', 'age': 20}, key=lambda x: x['age']) == {'name': 'b', 'age': 20}
    assert max({'name': 'a', 'age': 20}, key=lambda x: x['name'])['age'] == 20

    # Test key argument

# Generated at 2022-06-22 11:56:36.293640
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10.5') == 10
    assert human_to_bytes('-10') == -10
    assert human_to_bytes(10) == 10
    assert human_to_bytes(10.5) == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10.5b') == 10
    assert human_to_bytes('10.5B') == 10
    assert human_to_bytes('10B', 'B') == 10
    assert human_to_bytes('10.5B', 'B') == 10
    assert human_to_bytes('10.5b', 'B') == 10

# Generated at 2022-06-22 11:56:52.395571
# Unit test for function min
def test_min():
    assert min([1]) == 1
    assert min([0, 1, 2]) == 0
    assert min([0, -1, 2]) == -1
    assert min(['zzz', 'aaaa', 'c']) == 'aaaa'
    assert min(['', 'aaaa']) == ''
    assert min(['zzz', 'aaaa', 'c'], attribute='length') == 'c'

# Generated at 2022-06-22 11:57:03.765627
# Unit test for function min
def test_min():
    # Python 2 uses __builtins__ to make min and max available as filter
    min = __builtins__.get('min')

    # With a list of strings
    assert min(['b', 'a', 'c']) == 'a'
    # With a list of strings and a key
    assert min(['b', 'a', 'c'], key=str.lower) == 'a'
    # With a list of numbers
    assert min([2, 3, 1]) == 1
    # With a list of mixed types
    assert min([2, '3', 1]) == 1
    # With a list of objects
    assert min([MockObject('b'), MockObject('a'), MockObject('c')], key=lambda o: o.string) == 'a'
    # With a list of tuples

# Generated at 2022-06-22 11:57:09.552121
# Unit test for function max
def test_max():
    assert max(range(0, 10)) == 9
    assert max([1, 2, None, 3]) == 3
    assert max([1, 2, None, 3], default=42) == 3
    assert max([1, 2, None, 3], key=str) == 3
    assert max([1, 2, None, 3], key=lambda x: x is None) is None
    assert max([1, 2, None, 3], missing_value=42) is None
    assert max([1, 2, None, 3], key=str, missing_value=42) == 3


# Generated at 2022-06-22 11:57:17.324127
# Unit test for function max
def test_max():
    # test for a list of strings
    test_list = ['a', 'bc', 'def']
    assert max(test_list) == 'def'

    # test for a list of integers
    test_list = [1, 2, 5, 0, 1]
    assert max(test_list) == 5

    # test for a list of floats
    test_list = [1.0, 2.0, 5.1, 0.5, 1.0]
    assert max(test_list) == 5.1

    # test for a mixed list
    test_list = [1.0, 2, 5.1, 0, 1.0]
    assert max(test_list) == 5.1

    # test for an empty list
    test_list = []
    assert max(test_list) is None

    # test for a list

# Generated at 2022-06-22 11:57:27.811201
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min(['a', 'b', 'c'], 'x') == 'x'
    assert min([1, 2, 3], default=4) == 1
    assert min(['a', 'b', 'c'], default='x') == 'a'
    assert min([1, 2, 3], key=str) == 1
    assert min(range(10), key=lambda x: -x) == 9
    assert min([-1, -2, -1, -2], key=lambda x: -x) == -2
    assert min([1, 2, 3], key=lambda x: x + 1) == 2
    assert min(['a', 'b', 'c'], key=lambda x: x * 2) == 'a'

# Generated at 2022-06-22 11:57:39.589017
# Unit test for function max
def test_max():

    o = max([1, 2, 3, 4, 5])
    assert o == 5

    o = max(['aa', 'bb', 'cc'])
    assert o == 'cc'

    o = max([[1, 2], [3, 4], [5, 6]])
    assert o == [5, 6]

    o = max([(1, 2), (3, 4), (5, 6)])
    assert o == (5, 6)

    o = max([1, 2, 3, 4, 5], default='f')
    assert o == 5

    o = max(['aa', 'bb', 'cc'], default='f')
    assert o == 'cc'

    o = max([[1, 2], [3, 4], [5, 6]], default='f')
    assert o == [5, 6]

# Generated at 2022-06-22 11:57:49.245185
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.utils import jsonify
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    import sys

    # Stub PlayContext and use the jinja2 sandboxed environment
    play_context = PlayContext()
    play_context._ds = {}
    templar = Templar(loader=None, shared_loader_obj=None, variables=play_context.get_vars())

    # Provide some data to rekey on

# Generated at 2022-06-22 11:58:01.473088
# Unit test for function rekey_on_member

# Generated at 2022-06-22 11:58:07.915888
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([10, 20, 30, 40]) == 10
    assert min([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4]
    assert min([1.1, 2.1, 3.1, 4.1]) == 1.1
    assert min([1, 2, 3], key=lambda x: x * -1) == 3

    # test if function fails on unsupported parameters
    try:
        min([1, 2, 3], bar='baz')
        assert False, "min() should have failed on unsupported parameters"
    except AnsibleFilterError:
        pass



# Generated at 2022-06-22 11:58:12.728013
# Unit test for function rekey_on_member
def test_rekey_on_member():

    # Create result data structures
    test_data = {
        'test_empty_dict': {'data': {}, 'key': 'foo', 'result': {}},
        'test_empty_list': {'data': [], 'key': 'foo', 'result': {}},
        'test_empty_dict_key_not_found': {'data': {'bar': {'baz': '', 'foo': 'bar'}}, 'key': 'blat', 'result': {}},
    }

    # Generate data structures to test
    dict_data_structs = []
    list_data_structs = []

# Generated at 2022-06-22 11:58:33.701535
# Unit test for function min
def test_min():
    from collections import namedtuple
    from jinja2 import Environment, DictLoader

    env = Environment(loader=DictLoader({"template": "{{ [4,1,2] | min }}"}))
    assert env.get_template("template").render() == '1'
    env = Environment(loader=DictLoader({"template": "{{ [{'a':3},{'a':1},{'a':2}] | min(attribute='a') }}"}))
    assert env.get_template("template").render() == "{'a': 1}"

    # Test basic datastructures
    for data in [1, -1, 1.0, -1.0, 1/2, 3/2, '', 'a', b'test', [], [1,2,3], (1,2,3)]:
        env

# Generated at 2022-06-22 11:58:35.581702
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1



# Generated at 2022-06-22 11:58:47.560088
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.errors import AnsibleFilterError
    import ansible.constants as C
    C._ANSIBLE_INTERNAL_TEST = True

    class DummyModule(object):
        class dummy_class(object):
            def __init__(self):
                self.params = {}

            def fail_json(self, **kwargs):
                raise AssertionError(kwargs['msg'])

    class DummyFilterModule(object):
        def filters(self):

            class DummyEnvironment(object):
                def __init__(self):
                    self.tests = {}

            environment = DummyEnvironment()


# Generated at 2022-06-22 11:58:59.113107
# Unit test for function max
def test_max():
    # with list
    assert max([1]) == 1
    assert max([1, 2]) == 2
    assert max([1, 2, 3]) == 3
    assert max(['a', 'b', 'c', 'd']) == 'd'
    assert max(['a', 'b', 'c', 'd'], key=str.lower) == 'a'
    assert max(['a', 'b', 'c', 'd'], key=str.upper) == 'D'
    assert max([1, 2, 3, 4], key=str) == 4
    try:
        max(['a', 'b', ''])
    except TypeError:
        pass
    # with tuple
    assert max((1, )) == 1
    assert max((1, 2)) == 2
    assert max((1, 2, 3)) == 3


# Generated at 2022-06-22 11:59:03.470391
# Unit test for function min
def test_min():
    assert min('abcd', 'abce') == 'abcd'
    assert min('ABCD', 'ABCE') == 'ABCD'
    assert min(map(str, range(10, 0, -1))) == '1'
    assert min(map(str, range(20, 10, -1))) == '10'


# Generated at 2022-06-22 11:59:05.315970
# Unit test for function min
def test_min():
    assert min([4, 1, 2, 3]) == 1



# Generated at 2022-06-22 11:59:16.385853
# Unit test for function rekey_on_member
def test_rekey_on_member():
    def assert_correct(data, key, expected, duplicates='error'):
        result = rekey_on_member(data, key, duplicates)
        if result != expected:
            raise AssertionError("`rekey_on_member({0}, {1}, '{2}')` did not return expected output: {3!r} != {4!r}".format(
                data, key, duplicates, result, expected))

    def assert_error(data, key):
        try:
            result = rekey_on_member(data, key)
            raise AssertionError("`rekey_on_member({0}, {1})` should have raised an error but returned: {2!r}".format(
                data, key, result))
        except Exception as e:
            pass

    # Ensure we handle different types of data

# Generated at 2022-06-22 11:59:20.685740
# Unit test for function min
def test_min():
    assert min([4, 5, 6, 7]) == 4
    assert min([5, 4, 6, 7]) == 4
    assert min([6, 7, 4, 5]) == 4
    assert min([7, 6, 5, 4]) == 4



# Generated at 2022-06-22 11:59:24.202470
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min([4, 3, 2, 1]) == 1
    assert min([4, 7, 2, 1]) == 1


# Generated at 2022-06-22 11:59:26.588055
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([5, 4, 1]) == 1
    assert min([-1, -2, -3]) == -3


# Generated at 2022-06-22 12:00:01.286747
# Unit test for function rekey_on_member
def test_rekey_on_member():

    from ansible.utils.unsafe_proxy import wrap_var

    import pytest

    # test data
    data_dict = wrap_var(
        {
            'a': {
                'key1': 'value1_a',
                'key2': 'value2_a'
            },
            'b': {
                'key1': 'value1_b',
                'key2': 'value2_b'
            }
        }
    )

    data_list = wrap_var(
        [
            {
                'key1': 'value1_1',
                'key2': 'value2_1'
            },
            {
                'key1': 'value1_2',
                'key2': 'value2_2'
            }
        ]
    )


# Generated at 2022-06-22 12:00:06.636094
# Unit test for function min
def test_min():
    from ansible.module_utils import basic

    def test_min_no_args():
        assert min([]) is None

    def test_min_with_args():
        assert min([1,2,3]) == 1

    def test_min_with_kwargs():
        assert min([1,2,3], key=lambda x: -x) == 3



# Generated at 2022-06-22 12:00:18.245283
# Unit test for function max
def test_max():
    from ansible.module_utils.common.text import format_values
    from ansible.compat.tests import unittest

    class TestMax(unittest.TestCase):
        def test_max(self):
            self.assertEqual(max([1,2,3,4,5]), 5)
            self.assertEqual(max([[1,2],[3,4],[5,6]]), [5,6])
            self.assertEqual(max([[1,2],[3,6],[5,4]]), [3,6])
            self.assertEqual(max([1,2,3,4,5], default=-1), 5)
            self.assertEqual(max([[1,2],[3,4],[5,6]], default=-1), [5,6])

# Generated at 2022-06-22 12:00:20.431079
# Unit test for function min
def test_min():
    input = [1,2,3]
    assert min(input) == 1


# Generated at 2022-06-22 12:00:26.088369
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max("red", "green", "blue") == "red"
    assert max("red", "green", key=len) == "green"
    assert max("red", "green", key=lambda x: x[1]) == "red"



# Generated at 2022-06-22 12:00:28.432911
# Unit test for function min
def test_min():
    display.display(min([1, 2, 3]))
    display.display(min([1, 2, 3], attribute='name'))


# Generated at 2022-06-22 12:00:40.174652
# Unit test for function max
def test_max():
    with pytest.raises(AnsibleFilterError) as excinfo:
        max([1, 2, 3], key='a')
    assert 'Jinja2' in str(excinfo.value)
    assert '2.10' in str(excinfo.value)

    with pytest.raises(AnsibleFilterError) as excinfo:
        max([1, 2, 3], default='a')
    assert 'Jinja2' in str(excinfo.value)
    assert '2.10' in str(excinfo.value)

    with pytest.raises(AnsibleFilterError) as excinfo:
        max([1, 2, 3], attribute='a')
    assert 'Jinja2' in str(excinfo.value)
    assert '2.10' in str(excinfo.value)