

# Generated at 2022-06-22 11:50:54.362837
# Unit test for function max
def test_max():
    assert 4 == max([1, 2, 4])
    assert 4 == max([1, 2, 4], 2)


# Generated at 2022-06-22 11:51:05.876362
# Unit test for function min
def test_min():
    assert min([2, 3, 4, 1, 5]) == 1
    assert min(2, 3, 4, 1, 5) == 1
    assert min([[2], [3], [1]]) == [1]
    assert min(['aa', 'bb', 'a']) == 'a'
    assert min(2, 3, key=abs) == 2
    assert min(3, 2, key=abs) == 2
    assert min(2.2, 3.1, 4.1, key=int) == 3.1
    assert min(2.2, 3.1, 4.1, key=lambda x: str(x)[-1]) == 2.2
    assert min(2.2, 3.1, 4.1, key=lambda x: str(x)) == 3.1

# Generated at 2022-06-22 11:51:17.146739
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.module_utils.common._collections_compat import Mapping, Iterable
    from ansible.utils.display import Display
    from ansible.utils.sentinel import Sentinel
    display = Display()

    def _assert_raises_FilterError(func, *args):
        try:
            func(*args)
            assert False
        except AnsibleFilterError:
            pass

    def _assert_raises_FilterTypeError(func, *args):
        try:
            func(*args)
            assert False
        except AnsibleFilterTypeError:
            pass

    def _assert_raises_UndefinedError(func, *args):
        try:
            func(*args)
            assert False
        except AnsibleFilterError:
            pass

    class _Sentinel(Sentinel):
        _sentinel = object()



# Generated at 2022-06-22 11:51:30.090949
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('256B') == 256)
    assert(human_to_bytes('128K') == 128 * 1024)
    assert(human_to_bytes('128KB') == 128 * 1024)
    assert(human_to_bytes('128KiB') == 128 * 1024)
    assert(human_to_bytes('1M') == 1024 * 1024)
    assert(human_to_bytes('1MiB') == 1024 * 1024)
    assert(human_to_bytes('128M') == 128 * 1024 * 1024)
    assert(human_to_bytes('128MB') == 128 * 1024 * 1024)
    assert(human_to_bytes('128MiB') == 128 * 1024 * 1024)
    assert(human_to_bytes('1G') == 1024 * 1024 * 1024)

# Generated at 2022-06-22 11:51:38.780941
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(1) == "1 B"
    assert human_readable(1024) == "1.0 KiB"
    assert human_readable(1024 * 1024) == "1.0 MiB"
    assert human_readable(1024 ** 3) == "1.0 GiB"
    assert human_readable(1024 ** 4) == "1.0 TiB"
    assert human_readable(1024 ** 5) == "1024.0 TiB"
    assert human_readable(1024 ** 5, unit='KiB') == "1048576.0 KiB"
    assert human_readable(1024 ** 5, unit='MiB') == "1048576.0 MiB"
    assert human_readable(1024 ** 5, unit='GiB') == "1024.0 GiB"
    assert human_readable(1024 ** 6, unit='TiB')

# Generated at 2022-06-22 11:51:50.736024
# Unit test for function max
def test_max():
    # Default max
    try:
        assert max([1, 2, 3, 4]) == 4
        assert max([4, 3, 2, 1]) == 4
    except:
        assert False

    # None max within list of integers
    try:
        assert max([1, None, 3, 4]) == 4
        assert max([1, 3, 4, None]) == 4
    except:
        assert False

    # String max
    try:
        assert max("ABCD") == 'D'
        assert max("DCBA") == 'D'
    except:
        assert False

    # String max
    try:
        assert max("DCBAabcd") == 'd'
    except:
        assert False


# Generated at 2022-06-22 11:52:02.810004
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''The human_to_bytes function should return the expected number of bytes.'''


# Generated at 2022-06-22 11:52:07.596634
# Unit test for function human_readable
def test_human_readable():

    filter_results = human_readable('0')
    assert filter_results == '0', filter_results

    filter_results = human_readable('500')
    assert filter_results == '500B', filter_results

    filter_results = human_readable('1000')
    assert filter_results == '1000B', filter_results

    filter_results = human_readable('200')
    assert filter_results == '200B', filter_results

    filter_results = human_readable('2048')
    assert filter_results == '2.0K', filter_results

    filter_results = human_readable('4000000000')
    assert filter_results == '3.6T', filter_results

    filter_results = human_readable('4000000000', isbits=True)
    assert filter_results == '36Tb', filter_results

    filter_

# Generated at 2022-06-22 11:52:17.338880
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(0) == '0  B'
    assert human_readable(1023) == '1023  B'
    assert human_readable(1024) == '1.0  KB'
    assert human_readable(1023 * 1024) == '1023.0  KB'
    assert human_readable(1024 * 1024) == '1.0  MB'
    assert human_readable(1024 * 1024 * 1024) == '1.0  GB'
    assert human_readable(1024 * 1024 * 1024 * 1024) == '1.0  TB'
    assert human_readable(1024 * 1024 * 1024 * 1024 * 1024) == '1.0  PB'
    assert human_readable(1024 * 1024 * 1024 * 1024 * 1024 * 1024) == '1.0  EB'

# Generated at 2022-06-22 11:52:19.428076
# Unit test for function max
def test_max():
    assert max(['1',1,3,4]) == 4


# Generated at 2022-06-22 11:52:26.524310
# Unit test for function max
def test_max():
    sequence = (1, 3, 2, 7, 4, 0)
    expected_result = 7
    # Test the filter
    result = max(sequence)
    assert result == expected_result


# Generated at 2022-06-22 11:52:31.071493
# Unit test for function min
def test_min():
    assert min([3, 2, 1]) == 1
    assert min(['c', 'a', 'b']) == 'a'
    assert min([[1], [2], [0, 0]]) == [0, 0]
    assert min([[1], [2], [1]]) == [1]



# Generated at 2022-06-22 11:52:41.902232
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(0) == '0 B'
    assert human_readable(15) == '15 B'
    assert human_readable(15, isbits=True) == '120 B'

    assert human_readable(1000) == '1000 B'
    assert human_readable(1024) == '1 KB'
    assert human_readable(1047552) == '1021 KB'
    assert human_readable(1048576) == '1 MB'
    assert human_readable(1073741824) == '1 GB'
    assert human_readable(1099511627776) == '1 TB'
    assert human_readable(1125899906842624) == '1 PB'
    assert human_readable(1152921504606846976) == '1 EB'

# Generated at 2022-06-22 11:52:48.534359
# Unit test for function max
def test_max():
    assert max(5, 4) == 5
    assert max(1, 2, 3) == 3
    assert max([5, 3, 2]) == 5
    assert max([1, 2, 3], [2, 3, 4]) == [2, 3, 4]
    assert max([1, 2, 3], [2, 3, 4], [3, 4, 5]) == [3, 4, 5]


# Generated at 2022-06-22 11:52:53.592396
# Unit test for function max
def test_max():
    assert max([4, 2, 3]) == 4
    assert max(4, 2, 3) == 4
    assert max(4, 2, 5, 6) == 6
    assert max([4, 2, 5, 6, 1]) == 6
    assert max('23', '42') == '42'



# Generated at 2022-06-22 11:52:56.590628
# Unit test for function max
def test_max():
    assert max([0, 1, 2, 3, 4]) == 4
    assert max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -10) == 9


# Generated at 2022-06-22 11:53:06.710686
# Unit test for function max
def test_max():
    assert 20 == max([20, 40, 10])
    assert 40 == max([20, 40, 10], key=lambda x: x * 2)
    assert 'z' == max('abcde', 'xyz')
    assert 'xyz' == max('abcde', 'xyz', key=len)
    assert max([20, None, 40, 10]) is None
    try:
        max(20, 40, 10)
        assert False
    except AnsibleFilterTypeError:
        pass
    try:
        max('abcde', [])
        assert False
    except AnsibleFilterTypeError:
        pass
    try:
        max(20, [], 10)
        assert False
    except AnsibleFilterTypeError:
        pass

# Generated at 2022-06-22 11:53:09.324009
# Unit test for function max
def test_max():
    max_value = max([0, 1, 2, 3])
    assert max_value == 3


# Generated at 2022-06-22 11:53:12.617102
# Unit test for function max
def test_max():
    max4 = max(4, 5)
    max5 = max([4, 7, 4, 1, 6, 7, 8, 2, 5])
    max6 = max(max, min)

    assert max4 == 5
    assert max5 == 8
    assert max6 == min

# Generated at 2022-06-22 11:53:20.454242
# Unit test for function max
def test_max():
    fm = FilterModule()
    max_filter = fm.filters()['max']

    assert max_filter([2, 3, 4]) == 4
    assert max_filter(["foo", "bar"]) == "foo"  # Sorted alphabetically
    assert max_filter([2, 3, 4], 4) == 4  # default arg
    assert max_filter([2, 3, 4], key=str) == 4  # With key arg
    assert max_filter([]) == None  # Empty list
    assert max_filter([], 0) == 0  # Empty list with default arg


# Generated at 2022-06-22 11:53:32.428984
# Unit test for function min
def test_min():
    assert min([3, 2, 1]) == 1
    assert min((3, 2, 1)) == 1

    try:
        min("This is not a list")
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError("min() should fail on non-list input")



# Generated at 2022-06-22 11:53:36.549918
# Unit test for function min
def test_min():
    from ansible.module_utils.six.moves import cStringIO

    stdin = cStringIO()
    stdout = cStringIO()

    display.display = stdout.write
    display.verbosity = 4

    f = FilterModule()
    filters = f.filters()

    def run_filter(result, *args):
        stdin.truncate(0)
        stdout.truncate(0)
        if isinstance(args[-1], dict):
            kwargs = args[-1]
            args = args[:-1]
        else:
            kwargs = {}

        input_data = args[0]
        if 'input_data' not in kwargs:
            kwargs['input_data'] = input_data

# Generated at 2022-06-22 11:53:37.316365
# Unit test for function max
def test_max():
    assert max(range(1, 11)) == 10



# Generated at 2022-06-22 11:53:47.351126
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Asserting on the numbers to assert on the function
    assert human_to_bytes('42') == 42
    assert human_to_bytes('42K') == 42 * 1024
    assert human_to_bytes('42M') == 42 * 1024 * 1024
    assert human_to_bytes('42G') == 42 * 1024 * 1024 * 1024
    assert human_to_bytes('42T') == 42 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('42P') == 42 * 1024 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('42E') == 42 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('42Y') == 42 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024

# Generated at 2022-06-22 11:53:49.961862
# Unit test for function max
def test_max():
    m = max([1, 2, 3, 4, 5])
    assert m == 5



# Generated at 2022-06-22 11:53:53.785510
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([3, 1, 2]) == 3
    assert max([3, 2, 1]) == 3


# Generated at 2022-06-22 11:54:00.158981
# Unit test for function min
def test_min():
    assert 0 == min(['foo','bar','baz','qux','quux','corge'])
    assert 0 == min(0, 1, 2, 3, 4, 5)
    assert 0 == min([0, 1, 2, 3, 4, 5])
    assert 0 == min([[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]])


# Generated at 2022-06-22 11:54:11.481575
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Human readable input with default unit
    assert 100 == human_to_bytes("100")
    assert (100, "B") == human_to_bytes("100", True)
    assert (100, "B") == human_to_bytes("100", True, False)

    # Human readable input with specified unit
    assert (100, "KB") == human_to_bytes("100KB")
    assert (100, "KB") == human_to_bytes("100KB", True)
    assert (100, "KB") == human_to_bytes("100KB", True, False)

    assert (1000, "KB") == human_to_bytes("1MB")
    assert (1000, "KB") == human_to_bytes("1MB", True)
    assert (1000, "KB") == human_to_bytes("1MB", True, False)



# Generated at 2022-06-22 11:54:20.102305
# Unit test for function max
def test_max():

    args_list = [[], [1], [1, 2], [1, 2, 3]]
    args_list.append([1, 2, 3, 4, 5, 6, 7, 9, 10, 45, 64, 73, 90, 23, 54, 73, 82, 93])
    args_list.append([0, 0, 0])
    args_list.append([-1, -1, -1])
    args_list.append([-82, -93, -73, -74, -65, -56, -45, -36, -27, -18, -9])

    for arg in args_list:
        arg_max = max(arg)
        ansible_max = AnsibleFilterModule().filters()['max'](arg)
        assert(arg_max == ansible_max)

    return

# Unit test

# Generated at 2022-06-22 11:54:30.916084
# Unit test for function logarithm
def test_logarithm():
    tests = [
        {
            'in': {'x': 100, 'base': 10},
            'out': 2.0,
        },
        {
            'in': {'x': 2, 'base': 2},
            'out': 1.0,
        },
        {
            'in': {'x': 10, 'base': 2},
            'out': 3.3219280948873626,
        },
        {
            'in': {'x': 'invalid string'},
            'error': AnsibleFilterTypeError,
        },
    ]

    for test in tests:
        if 'error' in test:
            try:
                logarithm(**test['in'])
            except test['error'] as e:
                pass

# Generated at 2022-06-22 11:54:55.859885
# Unit test for function max
def test_max():
    # Python 2, Python 3, and Jinja2 all have a built-in max, so let's exclude that from testing
    max_orig = __builtins__.get('max')
    del __builtins__.max


# Generated at 2022-06-22 11:55:03.668876
# Unit test for function min
def test_min():
    m1 = {'a': 1, 'b': 12, 'c': 3, 'd': 5, 'd': 7}
    m2 = {'a': 1, 'b': 12, 'c': 3, 'd': 5}
    m3 = [1, 3]
    m4 = [1, 3, 7, 5, 3]

    assert min(m1) == 1
    assert min(m2, key='b') == 1
    assert min(m3) == 1
    assert min(m4) == 1

# Generated at 2022-06-22 11:55:06.436589
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min(x for x in [1, 2, 3, 4]) == 1
    assert min([]) is None
    assert min(x for x in []) is None


# Generated at 2022-06-22 11:55:09.020466
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5], key=lambda x: -x) == 5



# Generated at 2022-06-22 11:55:19.453535
# Unit test for function min
def test_min():
    # test built-in function
    assert min(list(range(7))) == 0

    # test an arbitrary mapping object
    class Mapping(object):
        def __init__(self, items):
            self.items = items

        def __getitem__(self, key):
            return self.items[key]

        def __len__(self):
            return len(self.items)

        def keys(self):
            return self.items.keys()

    assert min(Mapping([(3, 'b'), (1, 'a')])) == 1

    # test that non-numeric types compare correctly
    assert min(['100', '5', '1']) == '1'

    # test that a key function can be provided

# Generated at 2022-06-22 11:55:24.185352
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([1, -2, 3]) == -2
    assert min([1, 2, 0]) == 0
    assert min([1]) == 1
    assert min([]) is None

    # Ensure min works when called on an empty iterable
    assert min([]) is None



# Generated at 2022-06-22 11:55:27.440836
# Unit test for function max
def test_max():
    assert max([9, 0, 'apple', 2, 'banana']) == 9
    assert max([9, 0, 'apple', 2, 'banana'], key=len) == 'banana'


# Generated at 2022-06-22 11:55:31.569843
# Unit test for function min
def test_min():
    assert min([1, 2, 3], [1, 2], 5) == 1
    assert min(['foo', 'bar', 'baz'], 'foobar') == 'bar'
    assert min(['baz', 'bar', 'foo'], 'foobar', attribute='lower') == 'bar'
    assert min(["d", "a", "b"], ["a", "b"], ["c"]) == ["d"]


# Generated at 2022-06-22 11:55:41.400662
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import pytest

    # Test key in each dict
    data = [
        {'a':'foo', 'b':'bar', 'c':'baz'},
        {'a':'qux', 'b':'quux', 'c':'quuz'},
    ]
    key = 'a'
    r = rekey_on_member(data, key, 'overwrite')
    assert type(r) == dict
    assert r['foo']['b'] == 'bar'
    assert r['qux']['b'] == 'quux'
    r = rekey_on_member(data, key, 'error')
    assert type(r) == dict
    assert r['foo']['b'] == 'bar'
    assert r['qux']['b'] == 'quux'

# Generated at 2022-06-22 11:55:45.311165
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min((1, 2, 3)) == 1
    assert min([1, 2, 3], key=lambda x: -x) == 3


# Generated at 2022-06-22 11:56:00.482450
# Unit test for function human_readable
def test_human_readable():
    filter_ = FilterModule()
    filter_ = filter_.filters()
    assert filter_['human_readable'](2048) == '2.0K'
    assert filter_['human_readable'](2048, unit='m') == '0.002M'
    assert filter_['human_readable'](2048, unit='m', isbits=True) == '0.002M'
    assert filter_['human_readable'](2048, isbits=True) == '1.953K'


# Generated at 2022-06-22 11:56:08.956792
# Unit test for function min
def test_min():
    x = [-1, 0, 2, 4, 5, -3]
    y = [0, 2, 4, 5, -3, -1]
    z = [1, 2, -3, 4, 5, 0]
    m = [-1, 0, 2, 4, 5, -3, None]
    filterModule = FilterModule()
    filterModule.filters()
    resultList = [
        min(x),
        min(y),
        min(z),
        min(m)
    ]
    expectedList = [-3, -3, -3, None]
    assert resultList == expectedList


# Generated at 2022-06-22 11:56:19.249058
# Unit test for function rekey_on_member
def test_rekey_on_member():
    data = dict(
        a=dict(key0='foo', key1='bar'),
        b=dict(key0='foo2', key1='bar2'),
        c=dict(key0='foo3', key1='bar3')
    )

    rekeyed_data = rekey_on_member(data, 'key0')

    assert len(rekeyed_data) == 3
    assert rekeyed_data['foo'] == dict(key0='foo', key1='bar')
    assert rekeyed_data['foo2'] == dict(key0='foo2', key1='bar2')
    assert rekeyed_data['foo3'] == dict(key0='foo3', key1='bar3')

# Generated at 2022-06-22 11:56:29.067166
# Unit test for function rekey_on_member
def test_rekey_on_member():
    f = FilterModule()
    d = f.filters()

    assert d['rekey_on_member']([{'a': 'A', 'b': 'B'}, {'a': 'A2', 'c': 'C2'}], 'a') == {'A': {'a': 'A', 'b': 'B'}, 'A2': {'a': 'A2', 'c': 'C2'}}
    assert d['rekey_on_member']({'x': {'a': 'A', 'b': 'B'}, 'y': {'a': 'A2', 'c': 'C2'}}, 'a') == {'A': {'a': 'A', 'b': 'B'}, 'A2': {'a': 'A2', 'c': 'C2'}}
    assert d

# Generated at 2022-06-22 11:56:39.079408
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([3, 2, 1]) == 1
    assert min(['a', 'b', 'c']) == 'a'
    assert min(['c', 'b', 'a']) == 'a'
    assert min(['c', 'a', 'b']) == 'a'
    assert min([1.1, 2.2, 3.3]) == 1.1
    assert min([3.3, 2.2, 1.1]) == 1.1
    assert min([5, 7, 1]) == 1
    assert min([1, 5, 7]) == 1
    assert min([7, 5, 1]) == 1
    assert min([1, 7, 5]) == 1
    assert min([7, 1, 5]) == 1

# Generated at 2022-06-22 11:56:50.749370
# Unit test for function unique
def test_unique():
    def _cmp(a1, a2):
        if len(a1) != len(a2):
            return False

        for i in range(len(a1)):
            if isinstance(a1[i], (list, tuple)) and isinstance(a2[i], (list, tuple)):
                if not _cmp(a1[i], a2[i]):
                    return False
            elif a1[i] != a2[i]:
                return False

        return True

    # Basic unique
    assert(_cmp(unique(list(range(10)) + list(range(5))), list(range(10))))
    assert(_cmp(unique(list(range(10)) + list(range(5)), True), list(range(10))))
    # Unique by attribute

# Generated at 2022-06-22 11:57:02.311477
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Unit tests for human_to_bytes filter
    '''

    # Tests for basic conversions
    assert human_to_bytes('1048576') == 1048576
    assert human_to_bytes('1KiB') == 1024
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MiB') == 1048576
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1GiB') == 1073741824
    assert human_to_bytes('1TB') == 1099511627776
    assert human_to_bytes('1TiB') == 1099511627776
    assert human_to_bytes('1PB') == 1125899906842624
    assert human_to_bytes('1PiB') == 11258

# Generated at 2022-06-22 11:57:06.856061
# Unit test for function min
def test_min():
    # Test for python version less than 3
    assert min(1, 2, 3) == 1
    # Test for python version greater than or equal to 3
    assert min(1, 2, 3, default=0) == 1
    # Test for python version less than 3
    assert min(1, 2, 3) == 1
    # Test for python version greater than or equal to 3
    assert min(1, 2, 3, default=0) == 1


# Generated at 2022-06-22 11:57:17.873304
# Unit test for function max
def test_max():
    f = FilterModule().filters()
    if HAS_MIN_MAX:  # compare results to builtin min filter if available
        assert f['max']([1, 2, 3, 4, 5]) == 5
        assert f['max'](['1', '2', '3', '4', '5']) == '5'
        assert f['max']([1, 2, '3', '4', 5]) == '5'
        assert f['max']({'a': 10, 'b': 20, 'c': 30}) == 30
        assert f['max']({'a': '10', 'b': '20', 'c': '30'}) == '30'
        assert f['max']({'a': 10, 'b': '20', 'c': '30'}) == '30'

# Generated at 2022-06-22 11:57:20.269517
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3


# Generated at 2022-06-22 11:57:39.322265
# Unit test for function max
def test_max():
    # Test with different number types
    assert 9 == max([4, 9, 1, 5])
    assert 9.0 == max([4.0, 9.0, 1.0, 5.0])
    assert 9 == max([4, 9, 1, 5, 9])
    assert "b" == max(["a", "b", "c", "d"])

    # Test with different keyword arguments
    assert 9 == max([4, 9, 1, 5], key=lambda x: x)
    assert 9 == max([4, 9, 1, 5], key=lambda x: -x)
    assert 9 == max([4, 9, 1, 5], key=lambda x: 10 - x)
    assert "b" == max(["a", "b", "c", "d"], key=lambda x: x)
    assert "b" == max

# Generated at 2022-06-22 11:57:40.749137
# Unit test for function max
def test_max():
    assert max([1,3,4]) == 4


# Generated at 2022-06-22 11:57:48.787856
# Unit test for function min
def test_min():
    min_filter = FilterModule().filters()['min']

    # Min with a dictionary
    dictionary = {"a": 56, "b": "43", "c":2}
    assert min_filter(dictionary) == '43'

    # Min with a list
    lst = [1, 2, 3, 4]
    assert min_filter(lst) == 1

    # Min with a string (returns the first character)
    string = "some string"
    assert min_filter(string) == "s"

    # Min with a number
    number = 12
    assert min_filter(number) == 12



# Generated at 2022-06-22 11:58:00.954688
# Unit test for function unique
def test_unique():
    # Use case_sensitive=None as a sentinel value, so we raise an error only when
    # explicitly set and cannot be handle (by Jinja2 w/o 'unique' or fallback version)
    assert unique(None, [1, 2, 3, 4]) == [1, 2, 3, 4]
    assert unique(None, [1, 2, 3, 3, 4]) == [1, 2, 3, 4]
    assert unique(None, [1, 2, 3, 3, "a", "a", "a", 1, 1, 2, 3]) == [1, 2, 3, "a"]
    assert unique(None, [1, 2, 3, 3, "a", "a", "a", 1, 1, 2, 3], case_sensitive=False) == [1, 2, 3, "a"]

# Generated at 2022-06-22 11:58:03.945386
# Unit test for function min
def test_min():
    display = Display()
    f = FilterModule()
    logarithm = f.filters()['log']
    assert -10.0 < logarithm(0.01, 10) < -9.9
    assert -0.149 < logarithm(0.1) < -0.148

# Generated at 2022-06-22 11:58:16.018161
# Unit test for function human_readable
def test_human_readable():

    h = human_readable(1)
    assert h == "1.0 B", h

    h = human_readable(1024)
    assert h == "1.0 K", h

    h = human_readable(1024*1024)
    assert h == "1.0 M", h

    h = human_readable(1024*1024*1024)
    assert h == "1.0 G", h

    h = human_readable(1024*1024*1024*1024)
    assert h == "1.0 T", h

    h = human_readable(1024*1024*1024*1024, unit="K")
    assert h == "1024.0 K", h

    h = human_readable(1024*1024*1024*1024, unit="T")
    assert h == "1.0 T", h


# Generated at 2022-06-22 11:58:19.397357
# Unit test for function min
def test_min():
    import random
    from jinja2 import Environment
    env = Environment()
    env.filters['min'] = min
    jinja_list = range(0, random.randint(1, 100))
    python_list = max(list(jinja_list))
    assert env.from_string('{{ jinja_list | min }}').render(jinja_list=jinja_list) == str(min(python_list))

# Generated at 2022-06-22 11:58:30.881114
# Unit test for function min
def test_min():
    assert min([1, 2, 3] ) == 1
    assert min([1, 2, 1, 3, 2] ) == 1
    assert min(["a", "b", "c"] ) == "a"

    assert min([1, 2, 3], [2, 3, 4], [3, 4, 5]) == [1, 2, 3]
    assert min([1, 2, 3], [2, 3, 4], [3, 2, 5]) == [1, 2, 3]

    assert min([1, 2, 3], key=lambda x: -x) == 3
    assert min([1, 2, 1, 3, 2], key=lambda x: -x) == 3
    assert min(["a", "b", "c"], key=lambda x: -ord(x)) == "c"


# Generated at 2022-06-22 11:58:32.340820
# Unit test for function max
def test_max():
    assert max(range(10)) == 9



# Generated at 2022-06-22 11:58:42.908835
# Unit test for function max
def test_max():
    f = FilterModule().filters()
    assert f['max']([1, 2, 3, 4, 5]) == 5
    assert f['max']([-5, -3, -6, -1]) == -1
    assert f['max'](['a', 'bbb', 'cc']) == 'bbb'
    assert f['max'](['a', 'bbb', 'cc'], attribute='length') == 'bbb'
    assert f['max']([b'a', b'bbb', b'c']) == b'bbb'
    assert f['max']([b'a', b'bbb', b'c'], attribute='length') == b'bbb'


# Generated at 2022-06-22 11:59:27.798675
# Unit test for function max
def test_max():
    f = FilterModule()

    assert f.filters()['max']([1, 2]) == 2
    assert f.filters()['max']([1, 2.1]) == 2.1
    assert f.filters()['max']('foo', 'faa') == 'foo'

    assert f.filters()['max']([1, 2], default=3) == 2
    assert f.filters()['max']([1, 2], default=1) == 2
    assert f.filters()['max']([], default=1) == 1
    assert f.filters()['max']([], default='bar') == 'bar'
    assert f.filters()['max']([], default=['bar']) == ['bar']


# Generated at 2022-06-22 11:59:32.569075
# Unit test for function max
def test_max():
    assert max([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 9
    assert max([1, -2, 3, -4, 5, -6, 7, -8, 9, 0], key=abs) == -8


# Generated at 2022-06-22 11:59:36.289439
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min(['1', '2', '3', '4']) == '1'
    assert min([]) is None
    assert min(['foo', 'bar'], attribute='upper') == 'BAR'


# Generated at 2022-06-22 11:59:47.718527
# Unit test for function human_to_bytes

# Generated at 2022-06-22 11:59:49.970119
# Unit test for function min
def test_min():
    module = FilterModule()
    filters = module.filters()
    assert filters['min']([1,2,3]) == 1
    assert filters['min']([1]) == 1


# Generated at 2022-06-22 11:59:51.262160
# Unit test for function min
def test_min():
    assert min([2, 3, 1]) == 1

# Generated at 2022-06-22 12:00:00.758735
# Unit test for function min
def test_min():
    from itertools import chain
    from operator import or_

    class DummyEnv(object):
        def __init__(self, *args, **kwargs):
            pass

    env = DummyEnv()

    # test with an empty iterable
    assert min(env, []) == None

    # test with just one element in iterable
    assert min(env, [3]) == 3

    # test a simple min test
    assert min(env, [2, 3]) == 2

    # test with a key function
    assert min(env, [1, -1, 2], key=abs) == -1

    # test with a string as a key
    assert min(env, {'one': 1, 'three': 3, 'two': 2}, key='value') == 'one'

    # test with a key function and an attribute

# Generated at 2022-06-22 12:00:12.660705
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('73876') == 73876
    assert human_to_bytes('73876K') == 73876 * 1024
    assert human_to_bytes('73876M') == 73876 * 1024 * 1024
    assert human_to_bytes('73876G') == 73876 * 1024 * 1024 * 1024
    assert human_to_bytes('73876T') == 73876 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('73876P') == 73876 * 1024 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('73876E') == 73876 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024

    assert human_to_bytes('73876b') == 73876


# Generated at 2022-06-22 12:00:22.091122
# Unit test for function max
def test_max():
    fm = FilterModule()
    filt = fm.filters()['max']
    assert filt([1, 2, 3]) == 3
    assert filt([None, 1, 2, 3]) == 3
    assert filt([None, 'abc']) is None
    assert filt([]) is None
    # There's no string max in python < 3, but it's consistent with our filter anyway
    assert filt(['a', 'b', 'c']) == 'c'
    assert filt([frozenset([1, 2]), frozenset([3, 4])]) == frozenset([3, 4])
    assert filt([[1], [2, 3]]) == [2, 3]



# Generated at 2022-06-22 12:00:28.582554
# Unit test for function unique
def test_unique():
    data = [1, 1, 2, 3, 2, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10]
    result = unique(None, data, True)
    assert len(result) == 10
    assert 1 not in result
    assert 2 not in result
    assert 3 in result
    assert 4 not in result
    assert 5 in result
    assert 6 in result
    assert 7 not in result
    assert 8 not in result
    assert 9 in result
    assert 10 in result