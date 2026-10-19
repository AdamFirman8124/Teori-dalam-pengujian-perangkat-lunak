

# Generated at 2022-06-22 11:50:50.250348
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import ast
    import ansible.compat.tests


# Generated at 2022-06-22 11:50:53.753317
# Unit test for function min
def test_min():
    assert min([10, 100]) == 10
    assert min(['a', 'b']) == 'a'



# Generated at 2022-06-22 11:51:05.229966
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(0) == "0 bytes"
    assert human_readable(1) == "1 byte"
    assert human_readable(100) == "100 bytes"
    assert human_readable(1024) == "1.0 KiB"
    assert human_readable(1024 * 1024) == "1.0 MiB"
    assert human_readable(1024 * 1024 * 1024) == "1.0 GiB"
    assert human_readable(1024 * 1024 * 1024 * 1024) == "1.0 TiB"
    assert human_readable(1024 * 1024 * 1024 * 1024 * 1024) == "1.0 PiB"
    assert human_readable(1024 * 1024 * 1024 * 1024 * 1024 * 1024) == "1.0 EiB"

# Generated at 2022-06-22 11:51:17.022192
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert formatters.human_to_bytes('1') == 1
    assert formatters.human_to_bytes('1000') == 1000
    assert formatters.human_to_bytes('1k') == 1024
    assert formatters.human_to_bytes('1K') == 1024
    assert formatters.human_to_bytes('1M') == 1024 * 1024
    assert formatters.human_to_bytes('1G') == 1024 * 1024 * 1024
    assert formatters.human_to_bytes('1T') == 1024 * 1024 * 1024 * 1024
    assert formatters.human_to_bytes('1P') == 1024 * 1024 * 1024 * 1024 * 1024
    assert formatters.human_to_bytes('1E') == 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert formatters.human_to_bytes('1Z') == 1024 * 1024

# Generated at 2022-06-22 11:51:29.872158
# Unit test for function rekey_on_member
def test_rekey_on_member():
    d = [
          {'b': '5', 'a': '1'},
          {'b': '6', 'a': '2'},
          {'b': '7', 'a': '3'},
          {'b': '8', 'a': '4'}
        ]

    d2 = {
          'foo': {'b': '5', 'a': '1'},
          'bar': {'b': '6', 'a': '2'},
          'baz': {'b': '7', 'a': '3'},
          'qux': {'b': '8', 'a': '4'}
        }


# Generated at 2022-06-22 11:51:38.684955
# Unit test for function max
def test_max():
    # simple list of numbers
    assert max(1, 2, 3, 4, 5) == 5
    assert max([1, 2, 3, 4, 5]) == 5
    assert max(range(1, 5)) == 4

    # list of strings
    assert max("jane", "aaron", "kaleo", "zachary") == "zachary"
    assert max("aaron", "zachary", "jane", "kaleo") == "zachary"
    assert max("jane", "aaron", "zachary", "kaleo") == "zachary"
    assert max("jane", "aaron", "kaleo", "zachary") == "zachary"

# Generated at 2022-06-22 11:51:51.714323
# Unit test for function rekey_on_member
def test_rekey_on_member():
    filtered = rekey_on_member(
        [
            {'hostname': 'host1', 'ip': '10.0.0.1'},
            {'hostname': 'host2', 'ip': '10.0.0.2'},
            {'hostname': 'host3', 'ip': '10.0.0.3'},
        ],
        'ip',
    )
    assert isinstance(filtered, dict)
    assert len(filtered) == 3
    assert '10.0.0.1' in filtered
    assert filtered['10.0.0.2'] == {'hostname': 'host2', 'ip': '10.0.0.2'}


# Generated at 2022-06-22 11:51:55.309694
# Unit test for function min
def test_min():
    assert min(['foo','bar','baz']) == 'bar'
    assert min([3,2,1]) == 1


# Generated at 2022-06-22 11:51:59.703893
# Unit test for function min
def test_min():
    f = FilterModule()
    assert f.filters()['min']([1, 2]) == 1
    assert f.filters()['min']({'a': 1, 'b': 2}) == 1
    assert f.filters()['min']({'a': None, 'b': 2}) is None


# Generated at 2022-06-22 11:52:01.090376
# Unit test for function human_readable
def test_human_readable():
    """ Test if the function human_readable gives the right output """
    assert human_readable(1000) == '1.0K'

# Generated at 2022-06-22 11:52:18.920555
# Unit test for function min
def test_min():
    fm = FilterModule()
    env = {}
    min_function = fm.filters()['min']

    # Test case: Incorrect type passed to function
    bad_input = "bad input"
    try:
        bad_input_output = min_function(env, bad_input)
        assert False, "Incorrect type passed to min should raise AnsibleFilterTypeError"
    except AnsibleFilterTypeError:
        pass

    # Test case: List with ints - should return minimum
    int_list = [1, 2, 3, 4, 5]
    int_output = min_function(env, int_list)
    assert int_output == 1, "Min with list of ints should return min, but got: %r" % int_output

    # Test case: List with strings - should return min alphabetically
    string_

# Generated at 2022-06-22 11:52:32.049931
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("1k") == 1024*1
    assert human_to_bytes("1K") == 1024*1
    assert human_to_bytes("1M") == 1024*1024*1
    assert human_to_bytes("1G") == 1024*1024*1024*1
    assert human_to_bytes("1T") == 1024*1024*1024*1024*1
    assert human_to_bytes("1P") == 1024*1024*1024*1024*1024*1
    assert human_to_bytes("1E") == 1024*1024*1024*1024*1024*1024*1
    assert human_to_bytes("1Z") == 1024*1024*1024*1024*1024*1024*1024*1
    assert human_to_bytes("1Y") == 1024*1024*1024*1024*1024*1024*1024*1024*1

# Generated at 2022-06-22 11:52:42.683703
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M') == 1024 * 1024, "1M should be 1024 * 1024"
    assert human_to_bytes('1M', 'b') == 1024 * 1024 * 8, "1M should be 1024 * 1024 * 8 with default unit b"
    assert human_to_bytes('1Gb') == 1024 * 1024 * 1024, "1Gb should be 1024 * 1024 * 1024"
    assert human_to_bytes('1Gb', 'b') == 1024 * 1024 * 1024 * 8, "1M should be 1024 * 1024 * 1024 * 8 with default unit b"
    assert human_to_bytes('1048576B') == 1024 * 1024, "1M should be 1024 * 1024"
    assert human_to_bytes('1048576P') == 1099511627776, "1P should be 1099511627776"
    assert human_to

# Generated at 2022-06-22 11:52:49.018627
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    assert min(1, 2, 3, 4, key=abs) == 1
    assert min(2, 1, 3, 4, key=abs) == 1
    assert min({1: "foo", 2: "bar", 3: "baz"}) == 1
    assert min({"foo": 1, "bar": 2, "baz": 3}) == "bar"

# Generated at 2022-06-22 11:53:00.844206
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from datetime import datetime
    assert human_to_bytes("1") == 1
    assert human_to_bytes("1M") == 1048576
    assert human_to_bytes("1G") == 1073741824
    assert human_to_bytes("1T") == 1099511627776
    assert human_to_bytes("1P") == 1125899906842624
    assert human_to_bytes("1E") == 1152921504606846976
    assert human_to_bytes("1Z") == 1180591620717411303424
    assert human_to_bytes("1Y") == 1208925819614629174706176
    assert human_to_bytes("1.0") == 1
    assert human_to_bytes("1.1") == 1

# Generated at 2022-06-22 11:53:02.142952
# Unit test for function power
def test_power():
    assert power(2, 2) == 4



# Generated at 2022-06-22 11:53:11.554955
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("100") == 100
    assert human_to_bytes("100B") == 100
    assert human_to_bytes("1k") == 1000
    assert human_to_bytes("1K") == 1024
    assert human_to_bytes("1m") == 1000000
    assert human_to_bytes("1M") == 1048576
    assert human_to_bytes("1g") == 1000000000
    assert human_to_bytes("1G") == 1073741824
    assert human_to_bytes("1t") == 1000000000000
    assert human_to_bytes("1T") == 1099511627776
    assert human_to_bytes("1p") == 1000000000000000
    assert human_to_bytes("1P") == 1125899906842624
    assert human_to_bytes("1e")

# Generated at 2022-06-22 11:53:14.856348
# Unit test for function max
def test_max():
    # Test math.max()
    assert max([1,2,3]) == 3

    # Test jinja2.filters.do_max() with boolean argument
    assert max([1,2,3], False) == 3


# Generated at 2022-06-22 11:53:27.240330
# Unit test for function min
def test_min():
    seq_a = [1, 2, 3]
    seq_b = ['a', 'b']
    map_a = {'a': 1, 'b': 2}
    map_b = {'a': 2, 'b': 1}
    positive_infinity = float('inf')
    negative_infinity = float('-inf')

    assert min(seq_a) == 1
    assert min(seq_a, [4, 5]) == 1
    assert min(seq_b) == 'a'
    assert min(seq_b, ['b', 'c']) == 'b'
    assert min(map_a) == 'a'
    assert min(map_a, map_b) == 'a'
    assert min(positive_infinity, 1) == 1
    assert min(negative_infinity, 1) == negative

# Generated at 2022-06-22 11:53:36.028098
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(1234) == '1.2Ki'
    assert human_readable(12345) == '12.1Ki'
    assert human_readable(123456) == '120.6Ki'
    assert human_readable(1234567) == '1.2Mi'
    assert human_readable(12345678) == '12.1Mi'
    assert human_readable(123456789) == '120.6Mi'
    assert human_readable(1234567890) == '1.1Gi'
    assert human_readable(12345678901) == '11.0Gi'
    assert human_readable(123456789012) == '110.7Gi'
    assert human_readable(1234567890123) == '1.1Ti'

# Generated at 2022-06-22 11:53:40.509202
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(100) == math.log(100)



# Generated at 2022-06-22 11:53:41.307928
# Unit test for function min
def test_min():
    assert min(42) == 42



# Generated at 2022-06-22 11:53:47.444272
# Unit test for function power
def test_power():
    module = FilterModule()
    power_filter = module.filters.get('pow')

    assert power_filter(10, 2) == 100

    try:
        power_filter(2, "string")
    except Exception as e:
        assert type(e) is AnsibleFilterTypeError

    try:
        power_filter("string", 2)
    except Exception as e:
        assert type(e) is AnsibleFilterTypeError



# Generated at 2022-06-22 11:53:59.652041
# Unit test for function unique
def test_unique():
    import random
    from ansible.module_utils.six import PY3
    assert unique([1,2,3]) == [1,2,3]
    assert unique([1,1,1,1,1]) == [1]
    assert unique([1,2,3,2,1,5]) == [1,2,3,5]
    assert unique([1,2,3,2,1,5], True) == [1,2,3,5]

    if PY3:
        assert unique([0o10, 0o20, 0o30, 0o20, 0o10, 0o50], case_sensitive=False) == [8, 16, 24, 32]

    assert unique([1.0,2.0,3.0]) == [1.0,2.0,3.0]
    assert unique

# Generated at 2022-06-22 11:54:01.913491
# Unit test for function min
def test_min():
    assert FilterModule().filters()['min']([1, 2, 3]) == 1



# Generated at 2022-06-22 11:54:12.782208
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    import jinja2
    import os
    import sys

    class VarManager():
        def __init__(self):
            self._vars = {}
            self.extra_vars = {}
            self.hostvars = {}
            self.host_specific_vars = {}

        def add_host_var(self, host, var, val):
            self.host_specific_vars[host] = {var:val}

        def set_host_variable(self, host, var, val):
            if host not in self.hostvars:
                self.hostvars[host] = {}
            self.hostvars[host][var] = val


# Generated at 2022-06-22 11:54:15.712184
# Unit test for function power
def test_power():
    assert power(2, 2) == 4
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(2, 1) == 2

# Generated at 2022-06-22 11:54:27.276671
# Unit test for function human_readable
def test_human_readable():
    assert '1.00kB' == formatters.bytes_to_human(1024)
    assert '1.00KiB' == formatters.bytes_to_human(1024, isbits=True)
    assert '1.00K' == formatters.bytes_to_human(1024, unit='SI')
    assert formatters.bytes_to_human(1) == '1.00B'

    assert '1.00KiB' == formatters.bytes_to_human(1024, isbits=True)
    assert '1.00KiB' == formatters.bytes_to_human(1024, isbits=True)
    assert '1.00K' == formatters.bytes_to_human(1024, unit='SI')

    assert '1023.00B' == formatters.bytes_to_human(1023)


# Generated at 2022-06-22 11:54:39.140284
# Unit test for function rekey_on_member
def test_rekey_on_member():
    # One dict of dicts
    data = dict(
        v1=dict(
            k2=2,
            k3=3,
            name='val1'
        ),
        v2=dict(
            k2=4,
            k3=9,
            name='val2'
        )
    )
    assert rekey_on_member(data, 'name') == dict(
        val1=dict(
            k2=2, k3=3, name='val1'
        ),
        val2=dict(
            k2=4, k3=9, name='val2'
        )
    )

    # With list of dicts

# Generated at 2022-06-22 11:54:43.150457
# Unit test for function min
def test_min():
    values = [1, 2, 3, 4]
    result = min(values, key=abs)
    assert result == 1

    values = [100, 2, -3, 4]
    result = min(values, key=abs)
    assert result == 2

    values = [1, 2, 3, 4]
    result = min(values)
    assert result == 1

    values = [1, 2, 3, 4]
    result = min(values, attribute='value')
    assert result == 1

    result = min(values, case_sensitive=False, attribute='value')
    assert result == 1

    result = min(values, case_sensitive=True, attribute='VALUE')
    assert result == 1

    values = ['one', 'two', 'three', 'four']
    result = min(values)

# Generated at 2022-06-22 11:54:58.337577
# Unit test for function human_to_bytes
def test_human_to_bytes():

    '''
    Test human_to_bytes function
    '''

    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1MiB') == 1048576
    assert human_to_bytes('1GiB') == 1073741824
    assert human_to_bytes('1TiB') == 1099511627776
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1TB') == 1099511627776
    assert human_to_bytes('1Gi') == 1073741824
    assert human_to_bytes('1Ti') == 1099511627776
    assert human_to_bytes

# Generated at 2022-06-22 11:55:09.569988
# Unit test for function max
def test_max():
    m = max(3, 2)
    assert m == 3

    # test with an iterable (list)
    m = max([2, 3, 1, 4])
    assert m == 4

    # test with an iterable (string)
    try:
        m = max("ZENA")
        assert False
    except AnsibleFilterError as e:
        assert "Ansible's max filter does not support any keyword arguments" in str(e)
    except ValueError:
        # this happens with python2 (unrelated to max())
        # https://github.com/ansible/ansible/issues/36189
        pass

    # test with a mapping (dict)
    m = max({'one': 1, 'two': 2, 'three': 3, 'four': 4})
    assert m == 4

    # test with kwargs


# Generated at 2022-06-22 11:55:12.960796
# Unit test for function min
def test_min():
    filters = FilterModule()
    assert filters.filters()['min']([1, 2, 3]) == 1

# Generated at 2022-06-22 11:55:24.418323
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min(1, 2, 3) == 1
    assert min([-2, -4, -3]) == -4

    assert min(1, 2, default=10) == 1
    assert min(0.5, 0.1, 0.7) == 0.1
    assert min(0.5, -0.1, 0.7) == -0.1

    assert min('ab', 'abc') == 'ab'
    assert min('abc', 'ab') == 'ab'
    assert min('abc', 'ab', 'a') == 'a'
    assert min('a', 'ab', 'abc') == 'a'
    assert min('ab', 'a', 'abc') == 'a'

    assert min([], default=10) == 10

# Generated at 2022-06-22 11:55:28.511971
# Unit test for function min
def test_min():
    display.display('Running filter plugin unit tests')

    assert min([3,6,9,12]) == 3
    assert min([3,3,3,3]) == 3

    assert min([3,6,9,12], 3, 'min') == 6


# Generated at 2022-06-22 11:55:31.274854
# Unit test for function human_readable
def test_human_readable():
    assert human_readable("1234") == "1.2 KB", "Incorrect human readable conversion"


# Generated at 2022-06-22 11:55:41.270938
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(8) == '8.0 B', 'error generating human readable string'
    assert human_readable(1024) == '1.0 KiB', 'error generating human readable string'
    assert human_readable(2048) == '2.0 KiB', 'error generating human readable string'
    assert human_readable(2097152) == '2.0 MiB', 'error generating human readable string'
    assert human_readable(536870912) == '512.0 MiB', 'error generating human readable string'
    assert human_readable(536870912, unit='GB') == '0.5 GiB', 'error generating human readable string'
    assert human_readable(536870912, True) == '512.0 MiB', 'error generating human readable string'

# Generated at 2022-06-22 11:55:53.371069
# Unit test for function unique
def test_unique():
    # what to test
    from jinja2.filters import environmentfilter
    @environmentfilter
    def unique(environment, a, case_sensitive=None, attribute=None):
        c = []
        for x in a:
            if x not in c:
                c.append(x)
        return c

    # tests
    # we should probably walk the whole obj in the for loop, but for now we test some use cases we know are broken
    assert unique(None, ['a', 'b', 'a', 'c']) == ['a', 'b', 'c']  # the one we were looking for, plain str
    assert unique(None, []) == []                                  # no vals
    assert unique(None, [{}, {}, {}]) == [{}, {}, {}]              # empty dicts

# Generated at 2022-06-22 11:56:02.059728
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(1234, isbits=False, unit=None) == '1234 B'
    assert human_readable(1234, isbits=True, unit=None) == '9.8 Kb'
    assert human_readable(1234, isbits=False, unit='KB') == '1.21 KB'
    assert human_readable(1234, isbits=True, unit='KB') == '9.81 KB'
    assert human_readable(1234, isbits=False, unit='MB') == '0.00 MB'
    assert human_readable(1234, isbits=True, unit='MB') == '0.01 MB'


# Generated at 2022-06-22 11:56:10.715862
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(0, True) == '0.0 b'
    assert human_readable(10, True) == '10.0 b'
    assert human_readable(1024, True) == '1.0 Kb'
    assert human_readable(1024, False) == '1.0 KB'
    assert human_readable(2048, False) == '2.0 KB'
    assert human_readable(2049, False) == '2.0 KB'
    assert human_readable(2049, False, 'B') == '2.0 B'
    assert human_readable(2**20, False) == '1.0 MB'
    assert human_readable(2**30, False) == '1.0 GB'
    assert human_readable(2**40, False) == '1.0 TB'

# Generated at 2022-06-22 11:56:26.626343
# Unit test for function max
def test_max():
    assert(max([1, 2]) == 2)
    assert(max([1, 2, 1]) == 2)
    assert(max([3, 1, 2]) == 3)
    assert(max(1, 2) == 2)
    assert(max(1, 2, 1) == 2)
    assert(max(3, 1, 2) == 3)


# Generated at 2022-06-22 11:56:31.524393
# Unit test for function min
def test_min():
    assert FilterModule().filters()['min']([1, 2, 3]) == 1
    assert FilterModule().filters()['min']([3, 2, 1]) == 1
    assert FilterModule().filters()['min']([1, 2, 1, 2, 3]) == 1


# Generated at 2022-06-22 11:56:39.612904
# Unit test for function min
def test_min():
    '''
    Test function behavior for function min

    Untested functionnality:
    - Jinja2 keyword arguments
    '''
    from ansible.compat.tests import unittest

    class TestMin(unittest.TestCase):
        def test_min_with_lists(self):
            self.assertEqual(min([1, 2, 3]), 1)
            self.assertEqual(min([3, 2, 1]), 1)
            with self.assertRaises(Exception):
                min(1, 2, 3)
            with self.assertRaises(Exception):
                min(1, 2)

    unittest.main()

# Generated at 2022-06-22 11:56:47.879451
# Unit test for function logarithm
def test_logarithm():
    mathfilters = FilterModule()
    log = mathfilters.filters()['log']
    assert log(1) == 0
    assert log(math.exp(1)) == 1
    assert log(100, 10) == 2
    assert log(8, 2) == 3
    try:
        log('x')
    except AnsibleFilterTypeError as e:
        assert str(e) == 'log() can only be used on numbers: a float is required'
    else:
        raise Exception("log filter did not fail when expected")


# Generated at 2022-06-22 11:56:55.043953
# Unit test for function min
def test_min():
    x = {
        'hello': [
            ['bye', 'hello', 'b'],
            ['bye', 'hello', 'b', 'a'],
            ['bye', 'hello', 'b', 'a', 'c'],
        ],
        'integer': [
            ['11', '22'],
            ['11', '22', '33'],
            ['11', '22', '33', '44'],
        ],
        'float': [
            ['3.3', '2.2', '1.1'],
            ['3.3', '2.2', '1.1', '0.0'],
            ['3.3', '2.2', '1.1', '0.0', '-1.1'],
        ],
    }


# Generated at 2022-06-22 11:57:05.593688
# Unit test for function min
def test_min():
    class TestObj:
        def __init__(self, val):
            self.val = val

        def __lt__(self, other):
            if isinstance(other, TestObj):
                return self.val < other.val
            else:
                return self.val < other

    f = FilterModule()
    assert min([1, 2, 3]) == 1

    assert f.filters()['min']([1, 2, 3]) == 1

    assert f.filters()['min']([]) is None

    assert min([TestObj(1), TestObj(3), TestObj(2)],
               attribute='val') == TestObj(1)

    assert f.filters()['min']([TestObj(1), TestObj(3), TestObj(2)],
                              attribute='val') == TestObj(1)



# Generated at 2022-06-22 11:57:10.075000
# Unit test for function rekey_on_member
def test_rekey_on_member():
    assert rekey_on_member({'a': {'name': 'a', 'value': 1}, 'b': {'name': 'b', 'value': 2}}, 'name') == \
           {'a': {'name': 'a', 'value': 1}, 'b': {'name': 'b', 'value': 2}}
    assert rekey_on_member([{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}], 'name') == \
           {'a': {'name': 'a', 'value': 1}, 'b': {'name': 'b', 'value': 2}}

# Generated at 2022-06-22 11:57:17.659048
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1024*1024
    assert human_to_bytes('1G') == 1024*1024*1024
    assert human_to_bytes('1T') == 1024*1024*1024*1024
    assert human_to_bytes('1P') == 1024*1024*1024*1024*1024
    assert human_to_bytes('1E') == 1024*1024*1024*1024*1024*1024

    assert human_to_bytes('1,000') == 1000
    assert human_to_bytes('1,000K') == 1024*1000
    assert human_to_bytes('1,000M') == 1024*1024*1000
    assert human_to_bytes('1,000G') == 1024*1024*1024

# Generated at 2022-06-22 11:57:29.488355
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10', default_unit=None) == 10
    assert human_to_bytes('10K', default_unit=None) == 1024 * 10
    assert human_to_bytes('10M', default_unit=None) == 1024 * 1024 * 10
    assert human_to_bytes('10G', default_unit=None) == 1024 * 1024 * 1024 * 10
    assert human_to_bytes('10T', default_unit=None) == 1024 * 1024 * 1024 * 1024 * 10
    assert human_to_bytes('10P', default_unit=None) == 1024 * 1024 * 1024 * 1024 * 1024 * 10
    assert human_to_bytes('10Y', default_unit=None) == 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 10

# Generated at 2022-06-22 11:57:40.774053
# Unit test for function unique
def test_unique():
    '''Test module: return the number of elements of each type in a list'''
    # Create a list that has duplicated integers, text, and objects
    list_to_test = [1, 1, 2, 'foo', 'foo', {'key':'value', 'key':'value'}]

    # Test that duplicated elements are removed
    assert unique(list_to_test) == [1, 2, 'foo', {'key':'value'}]

    # Test case_sensitive option
    assert unique(list_to_test, case_sensitive=False) == [1, 2, 'foo', {'key':'value'}]
    assert unique(list_to_test, case_sensitive=True) == [1, 2, 'foo', {'key':'value', 'key':'value'}]

    # Test attribute

# Generated at 2022-06-22 11:58:06.410422
# Unit test for function rekey_on_member
def test_rekey_on_member():

    data = [
        {"a": "x", "b": 2, "c": "foo"},
        {"a": "y", "b": 3, "c": "bar"},
        {"a": "z", "b": 1, "c": "baz"},
    ]

    result = rekey_on_member(data, "b")
    assert result == {1: {"a": "z", "b": 1, "c": "baz"}, 2: {"a": "x", "b": 2, "c": "foo"}, 3: {"a": "y", "b": 3, "c": "bar"}}

    result = rekey_on_member(data, "c")

# Generated at 2022-06-22 11:58:08.550408
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min(1, 2, 3) == 1


# Generated at 2022-06-22 11:58:14.663281
# Unit test for function min
def test_min():
    fm = FilterModule()
    min = fm.filters()['min']
    assert min([1, 2, 3, 4, 5]) == 1
    assert min([10, 20, 30, 40, 50]) == 10
    assert min([1, 2, 3, 4, 5], 50) == 1
    assert min([10, 20, 30, 40, 50], 10) == 10



# Generated at 2022-06-22 11:58:27.029367
# Unit test for function min
def test_min():
    "Test the min filter"
    f = FilterModule()
    assert f.filters()['min']([1, 2, 3, 4, 5]) == 1
    assert f.filters()['min']({'a': 1, 'c': 3, 'b': 2}) == 1
    assert f.filters()['min']({'a': 1, 'c': 3, 'b': 2}, attribute='value') == 1
    assert f.filters()['min']({'a': 1, 'c': 3, 'b': 2}, attribute='value', case_sensitive=False) == 1
    assert f.filters()['min']({'a': 1, 'C': 3, 'b': 2}, attribute='value', case_sensitive=False) == 1

# Generated at 2022-06-22 11:58:29.961827
# Unit test for function max
def test_max():
    assert max([0, 10, 15, 20]) == 20
    assert max(0, 10, 15, 20) == 20



# Generated at 2022-06-22 11:58:38.936948
# Unit test for function max
def test_max():
    assert max([1, 2, 3, 4, 5]) == 5
    assert max([5, 3, 1, 2, 4]) == 5
    assert max([-5, -3, -1, -2, -4]) == -1

    assert max((1, 2, 3, 4, 5)) == 5
    assert max((5, 3, 1, 2, 4)) == 5
    assert max((-5, -3, -1, -2, -4)) == -1

    assert max("12345") == '5'
    assert max("54321") == '5'
    assert max("abcde") == 'e'
    assert max("edcba") == 'e'

    assert max(1, 2, 3, 4, 5) == 5
    assert max(5, 3, 1, 2, 4) == 5
   

# Generated at 2022-06-22 11:58:50.785836
# Unit test for function min
def test_min():
    from ansible.module_utils.common.text import formatters

    assert min([1, 2, 'a']) == 1
    assert min({'a': 1, 'b': 2, 'c': 3}) == 1

    assert min([1, 2, 3], attribute=None) == 1
    assert min([1, 2, 3], attribute='value') == 1
    assert min([{'value': 1}, {'value': 2}], attribute='value') == {'value': 1}

    assert min([1, 2, 3], False, attribute=None) == 1
    assert min([1, 2, 3], False, attribute='value') == 1
    assert min([{'value': 1}, {'value': 2}], False, attribute='value') == {'value': 1}


# Generated at 2022-06-22 11:58:56.341985
# Unit test for function min
def test_min():
    assert min([5, 1, 2, 3, 4]) == 1
    try:
        min(1)
    except AnsibleFilterTypeError as e:
        assert to_native(e) == "min() type must be an iterable"
    else:
        raise Exception("AnsibleFilterTypeError not raised")


# Generated at 2022-06-22 11:58:58.612696
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1



# Generated at 2022-06-22 11:59:03.507292
# Unit test for function min
def test_min():
    module = AnsibleModule(argument_spec=dict(items=dict(type='list', elements='int'), ))
    items = module.params['items']
    assert len(items) > 0
    try:
        assert min_value == min(items)
    except Exception as e:
        module.fail_json(msg=to_native(e))



# Generated at 2022-06-22 11:59:41.660594
# Unit test for function unique
def test_unique():
    assert unique([1, 1, 2, 3]) == [1, 2, 3]
    assert unique([1, 1, 2, 3, 2, 1]) == [1, 2, 3]
    assert unique(['a', 'b', 'a', 'b']) == ['a', 'b']
    assert unique(['a', 'b', 'a', 'b'], True) == ['a', 'b']
    assert unique(['a', 'b', 'a', 'b'], False) == ['a', 'b', 'a', 'b']
    assert unique([{'idx': 1}, {'idx': 2}, {'idx': 3}], False) == [{'idx': 1}, {'idx': 2}, {'idx': 3}]

# Generated at 2022-06-22 11:59:52.515776
# Unit test for function unique
def test_unique():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Template

    loader = DataLoader()
    variable_manager = VariableManager()

    # Test with a set
    template_data = "{{ ['a', 'a', 'b', 'c'] | unique }}"
    template = Template(template_data, loader=loader, variable_manager=variable_manager)
    results = template.render(template_data, loader=loader, variable_manager=variable_manager)
    answer = [u'a', u'b', u'c']
    assert(results == answer)

    # Test without a set
    template_data = "{{ ['a', 'a', 'b', 'c'] | unique(case_sensitive=False) }}"

# Generated at 2022-06-22 11:59:55.129938
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([3, 1, 2]) == 3


# Generated at 2022-06-22 11:59:56.389420
# Unit test for function min
def test_min():
    result = min([1, 2, 3])
    assert result == 1


# Generated at 2022-06-22 12:00:05.748549
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Human to Bytes filter unit test
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    play_context = PlayContext()
    templar = Templar(play_context, vault_secrets=VaultLib())

    original_value = '10MB'
    expected_value = 10485760

    new_value = templar.template('{{ "' + original_value + '" | human_to_bytes }}')

    assert int(new_value) == expected_value, 'human_to_bytes filter fails to convert values'



# Generated at 2022-06-22 12:00:11.686248
# Unit test for function max
def test_max():
    # Test with one variable, non-list
    value = 26
    assert max(value) == 26

    # Test with one variable, list
    value = [9,23,7,54,10]
    assert max(value) == 54

    # Test with two variables, one list, one number
    value1 = [9,23,7,54,10]
    value2 = 17
    assert max(value1, value2) == 54

    # Test with two variables, both lists
    value1 = [9,23,7,54,10]
    value2 = [11,24,15,45,20]
    assert max(value1, value2) == [11,24,15,45,20]


# Generated at 2022-06-22 12:00:12.941561
# Unit test for function max
def test_max():
    pass


# Generated at 2022-06-22 12:00:20.807202
# Unit test for function max
def test_max():
    try:
        assert max([1, 2, 3]) == 3
        assert max(1, 2, 3) == 3
        assert max([1, 2, 3], stdout_lines=[1, 2, 3]) == 3
        assert max([1, 2, 3], attribute='test') == 3

        try:
            max([1, 2, 3], test=True)
        except:
            print("Passed test, max() didn't accept parameter test=True")
        else:
            raise Exception("Failed test, max() took parameter test=True")
    except ImportError:
        pass

# Generated at 2022-06-22 12:00:31.576390
# Unit test for function max
def test_max():
    from ansible.compat.tests import unittest
    from ansible.module_utils.six import PY3

    class TestMaxFilter(unittest.TestCase):

        def setUp(self):
            self.my_list = [2, 3, 4, 5, 6]
            self.my_tuple = (2, 3, 4, 5, 6)
            self.my_dict = {'a': 1, 'b': 5, 'c': 3, 'd': 2, 'e': 6}
            self.my_string_list = ['f', 't', 'e', 'r']
            self.my_unicode_list = ['f', 't', 'é', 'r']

        def tearDown(self):
            pass
