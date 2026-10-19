

# Generated at 2022-06-22 11:50:51.773315
# Unit test for function min
def test_min():
    filter_module = FilterModule()
    filters = filter_module.filters()
    environment = filters.get('min')
    result = environment(None, [-10, -5, -20, 0, 10, 5, 20])
    assert result == -20



# Generated at 2022-06-22 11:51:02.530829
# Unit test for function max
def test_max():
    """Test the Ansible max filter"""

    def _expect(desc, input_, output):
        if max(input_) != output:
            raise Exception("{0} failed: input: {1} output: {2} expected: {3}".format(desc, input_, max(input_), output))

    _expect("1", [1, 2, 3], 3)
    _expect("2", [3, 2, 1], 3)
    _expect("3", ["3", "2", "1"], "3")
    _expect("4", [["3"], ["2"], ["1"]], ["3"])

    # Empty iterable
    _expect("5", [], None)



# Generated at 2022-06-22 11:51:11.136390
# Unit test for function symmetric_difference
def test_symmetric_difference():
    assert symmetric_difference([1, 2, 3], [1, 2, 5]) == [3, 5]
    assert symmetric_difference([1, 2, 3], [1, 2, 5]) == symmetric_difference([1, 2, 5], [1, 2, 3])
    assert symmetric_difference([], [1, 2]) == [1, 2]
    assert symmetric_difference([1, 2], []) == [1, 2]
    assert symmetric_difference([], []) == []
    assert symmetric_difference('a', 'a') == []
    assert symmetric_difference('a', 'b') == ['a', 'b']
    assert symmetric_difference('a', 'aa') == ['a']
    assert symmetric_difference('aa', 'a') == ['a']


# Generated at 2022-06-22 11:51:21.041522
# Unit test for function max
def test_max():
    from ansible.config.manager import ConfigManager
    from jinja2 import Environment, StrictUndefined

    test_input = [1, 2, 3, 4, 5]
    test_input_str = 'abcde'
    test_input_mix = [1, 'b', 3, 'd', 5]
    test_input_set = {1, 2, 3, 4, 5}
    test_input_dict = [{'a': 1}, {'a': 2}, {'a': 3}]
    # The base value must not be 0

# Generated at 2022-06-22 11:51:32.962366
# Unit test for function rekey_on_member
def test_rekey_on_member():
    filtered = rekey_on_member([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], 'a')
    assert filtered == {1: {'a': 1, 'b': 2}, 3: {'a': 3, 'b': 4}}

    filtered = rekey_on_member({
        'x': {'a': 1, 'b': 2},
        'y': {'a': 3, 'b': 4},
    }, 'a')
    assert filtered == {1: {'a': 1, 'b': 2}, 3: {'a': 3, 'b': 4}}


# Generated at 2022-06-22 11:51:37.268656
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1
    try:
        assert min([1, 2, 3, 4], key=lambda x: x%2 == 1) == 3
        raise AssertionError("min function should raise an error as it is not supported by Jinja/Ansible")
    except AnsibleFilterError:
        pass


# Generated at 2022-06-22 11:51:50.786534
# Unit test for function min
def test_min():
    # Create test for jinja2 min filter
    # Arrays of numbers
    data_number_ints = [1, 2, 3, 4, 5]
    data_number_floats = [1.0, 2.0, 3.0, 4.0, 5.0]
    data_number_mixed = [1, 2.0, 3, 4.0, 5]
    data_number_empty = []
    data_number_mixed_empty = [1, 2.0, 3, 4.0, 5, []]

    # Array of strings
    data_str = ["one", "two", "three", "four", "five"]
    data_str_empty = []
    data_str_mixed_empty = ["one", "two", "three", "four", "five", []]

    # Array of boole

# Generated at 2022-06-22 11:51:55.463440
# Unit test for function logarithm
def test_logarithm():
    filters = FilterModule()
    math_filters = filters.filters()
    f = math_filters.get('log')

    assert f(10) == 2.302585092994046



# Generated at 2022-06-22 11:52:07.458503
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import pytest
    from ansible.plugins.filter.core import FilterModule

    def dict_compare(d1, d2):
        return set(d1.items()) == set(d2.items())

    # Create a filter for testing
    tf = FilterModule()
    filters = tf.filters()

    # Setup test data
    indata = [{'one': 1, 'two': 2, 'three': 3},
              {'one': 1, 'two': 2, 'three': 3},
              {'one': 1, 'two': 2, 'three': 3}]
    outdata = {'1twothree': {'one': 1, 'two': 2, 'three': 3}}

    # Test rekey_on_member with no errors

# Generated at 2022-06-22 11:52:17.154734
# Unit test for function max
def test_max():
    from ansible.template import Templar

    t = Templar(None)
    assert t.template('{{ [10, 5, 2] | max }}') == '10'
    assert t.template('{{ [10, 5, 2] | max(attribute="foo") }}') == ''
    assert t.template('{{ [{"foo": 15}, {"foo": 12}, {"foo": 8}] | max(attribute="foo") }}') == '15'
    assert t.template('{{ [{"foo": 15}, {"foo": "12"}, {"foo": 8}] | max(attribute="foo") }}') == '8'
    assert t.template('{{ [{"foo": 15}, {"foo": "12"}, {"foo": 8}] | max(attribute="foo", default=0) }}') == '0'

# Unit Test for function min

# Generated at 2022-06-22 11:52:34.318523
# Unit test for function min
def test_min():
    filter_module = FilterModule()
    assert filter_module.filters()['min']('a') == 'a'
    assert filter_module.filters()['min'](['a', 'b']) == 'a'
    assert filter_module.filters()['min'](['a', 'b'], 'b', 'c', 'd') == 'a'
    assert filter_module.filters()['min'](['a', 'b'], ['c', 'd']) == 'a'
    assert filter_module.filters()['min']({'a': 1, 'b': 2}) == 1
    assert filter_module.filters()['min']({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) == 1

# Generated at 2022-06-22 11:52:35.227162
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3


# Generated at 2022-06-22 11:52:48.077276
# Unit test for function human_readable

# Generated at 2022-06-22 11:52:59.402619
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([3, 2, 1]) == 3
    assert max([3, 3, 3]) == 3

    assert max([[1], [3], [2]]) == [3]

    assert max([[1], [2], [3]], key=lambda x: x[0]) == [3]
    assert max([[1], [3], [2]], key=lambda x: x[0]) == [3]
    assert max([[3], [2], [1]], key=lambda x: x[0]) == [3]
    assert max([[3], [3], [3]], key=lambda x: x[0]) == [3]


# Generated at 2022-06-22 11:53:09.825028
# Unit test for function human_readable
def test_human_readable():
    from ansible.module_utils._text import to_bytes

    # Test default unit
    assert human_readable(to_bytes('5KiB')) == '5K'
    assert human_readable('5KiB') == '5K'

    # Test human_readable with bits and bytes
    assert human_readable(str(1234 * 8 * 2), isbits=True) == '14.7K'
    assert human_readable(1234 * 8 * 2, isbits=True) == '14.7K'

    # Test human_readable with bytes
    assert human_readable(str(1234 * 2), isbits=False) == '2.3K'
    assert human_readable(1234 * 2, isbits=False) == '2.3K'

    # Test human_readable with custom unit
    assert human_readable

# Generated at 2022-06-22 11:53:11.863462
# Unit test for function max
def test_max():
    test_sample = [2, 3, 4, 5, 6, -1]
    assert max(test_sample) == 6


# Generated at 2022-06-22 11:53:22.149268
# Unit test for function max
def test_max():
    # Tests for old Jinja2 implementation
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([3, 1, 2]) == 3
    assert max([3, 2, 1]) == 3
    assert max([-1, -2, -3]) == -1
    assert max([-3, -2, -1]) == -1

    # Tests for new Jinja2 implementation
    assert max([1, 2, 3], key=json_dumps) == 3
    assert max([1, 2, 3], key=lambda x: -x) == 1
    assert max([1, 2, 3], key=lambda x: -x, default=0) == 1
    assert max([1, 2, 3], default=0) == 3

# Generated at 2022-06-22 11:53:25.008593
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(100) == 4.60517018599
    assert logarithm(100, base=10) == 2.0


# Generated at 2022-06-22 11:53:34.418399
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.utils.display import Display
    from .test_common import TestCase

    display = Display()

    class FilterModuleTestCase(TestCase):

        def setUp(self):
            super(FilterModuleTestCase, self).setUp()
            self.fm = FilterModule()

        def test_rekey_on_member(self):
            v = self.fm.filters()['rekey_on_member']

            # Test with a dict
            test_data = {"foo": {"key": "value"}, "bar": {"key": "another value"}, "baz": {"key": "value"}}
            expected_result = {"value": {"key": "value"}, "another value": {"key": "another value"}}

            result = v(test_data, "key")
            self.assertEqual(result, expected_result)



# Generated at 2022-06-22 11:53:38.550004
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(1.0) == 0
    assert logarithm(3.0, 2.0) == 1.5849625007211563
    assert logarithm(2.0) == 0.6931471805599453
    assert logarithm(8.0, 2.0) == 3
    assert logarithm(500.0, 10.0) == 2.6989700043360187
    assert logarithm(99.0, 10.0) == 1.9956354066989755


# Generated at 2022-06-22 11:53:45.186302
# Unit test for function min
def test_min():
    assert min([1,2,3]) == 1
    assert min([3,2,1]) == 1
    assert min([-3, 1, 2]) == -3



# Generated at 2022-06-22 11:53:51.810299
# Unit test for function max
def test_max():
    data = {'a': [1, 2, 3, 4], 'b': [0, 5, 10, 15], 'c': [5, 3, 0, 1]}
    assert max(None, data['a']) == 4
    assert max(None, data['a'], data['b']) == 15
    assert max(None, data['a'], data['b'], data['c']) == 15


# Generated at 2022-06-22 11:54:04.033054
# Unit test for function rekey_on_member

# Generated at 2022-06-22 11:54:14.325743
# Unit test for function human_readable
def test_human_readable():
    # Test simple case
    assert formatters.bytes_to_human(1023, False) == '1023B'

    # Test 2 decimal place case
    assert formatters.bytes_to_human(1023, False, 2) == '1023B'

    # Test one decimal place case
    assert formatters.bytes_to_human(1024, False, 1) == '1KB'

    # Test exact value case
    assert formatters.bytes_to_human(1048576, False, 1) == '1MB'

    # Test rounding to even case
    assert formatters.bytes_to_human(1228800, False, 1) == '1MB'

    # Test rounding down case
    assert formatters.bytes_to_human(1228799, False, 1) == '1MB'

    # Test rounding up case

# Generated at 2022-06-22 11:54:22.660407
# Unit test for function min
def test_min():
    context = {}
    result = min(context, [1, 2, 3])
    assert result == 1

    result = min(context, [3, 1, 2])
    assert result == 1

    result = min(context, [1])
    assert result == 1

    result = min(context, [])
    assert not result

    try:
        min(context, [1], foo=1)
    except AnsibleFilterError:
        pass
    else:
        assert False, "Expected AnsibleFilterError, got nothing"


# Generated at 2022-06-22 11:54:33.647544
# Unit test for function max
def test_max():
    fme = FilterModule()
    filters = fme.filters()
    data = [0, 1, 2]
    max_val = filters.get('max')(None, data)
    assert max_val == 2

    data = (1, 2, 3, 4)
    max_val = filters.get('max')(None, data)
    assert max_val == 4

    data = {'a': 1, 'b': 2}
    max_val = filters.get('max')(None, data)
    assert max_val == 2

    data = set([3, 1, 2])
    max_val = filters.get('max')(None, data)
    assert max_val == 3

    data = {'a': 1, 'b': 2, 'c': 5}

# Generated at 2022-06-22 11:54:43.142047
# Unit test for function unique
def test_unique():
    # revert to Ansible version of unique if test fails since older Jinja2 versions
    # do not have the filter or have a buggy version

    tmpl = dict(
        a=dict(
            j2_version=2.7,
            j2_unique=unique,
            ansible_unique=unique,
        ),
        b=dict(
            j2_version=2.10,
            j2_unique=unique,
            ansible_unique=unique,
        ),
        c=dict(
            j2_version=2.9,
            j2_unique=unique,
            ansible_unique=unique,
        ),
    )


# Generated at 2022-06-22 11:54:55.253591
# Unit test for function min
def test_min():
    obj1 = [1, 2, 3]
    obj2 = [3, 2, 1]
    obj3 = [8, 4]
    obj4 = [1, 2, 3]
    obj5 = {'a': 1, 'b': 2}
    obj6 = {'a': 2, 'b': 1}
    obj7 = {'a': 1, 'b': 2}
    obj8 = [1, 2, 3]
    obj9 = {'a': [1, 2, 3], 'b': [3, 2, 1]}
    obj10 = [2, 2, 3]
    obj11 = [1, 2, 3, 0]
    obj12 = [0, 1, 2, 3]
    obj13 = [0, 1, 2, 3]
    obj14 = [0, 1, 2, 3]

# Generated at 2022-06-22 11:55:05.737076
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests.mock import MagicMock

    class TestRekeyOnMember(unittest.TestCase):
        def setUp(self):
            self.runner = MagicMock()
            self.runner._log_invocation = True

            patcher = patch.object(FilterModule, 'filters', return_value=int())
            patcher.start()
            self.addCleanup(patcher.stop)

            self.jinja_filter_class = FilterModule()
            self.jinja_filters = self.jinja_filter_class.filters()


# Generated at 2022-06-22 11:55:16.504215
# Unit test for function unique
def test_unique():

    from ansible.compat.tests import unittest

    from ansible.module_utils.six import PY3

    class TestUnique(unittest.TestCase):
        def test_empty(self):
            self.assertEqual([], unique([], True))
            self.assertEqual([], unique([], False))

        if PY3:
            def test_non_string_uniqueness(self):
                inp = [(1, 1.0), (1, 2.0)]
                self.assertEqual(inp, unique(inp, True))

        def test_short_uniqueness(self):
            inp = [1, 2, 3]
            self.assertEqual(inp, unique(inp, True))


# Generated at 2022-06-22 11:55:23.220263
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5]) == 1
    assert min([-1, 2, 3, 4, 5]) == -1
    assert min([[1], [2], [3], [4], [5]]) == [1]



# Generated at 2022-06-22 11:55:28.305737
# Unit test for function min
def test_min():
    filter_module = FilterModule()
    assert filter_module.filters()['min']([1, 2]) == 1
    assert filter_module.filters()['min']([3, 2]) == 2
    assert filter_module.filters()['min']([0, 0, 0, 0]) == 0


# Generated at 2022-06-22 11:55:40.094399
# Unit test for function rekey_on_member
def test_rekey_on_member():
    obj = {'f_1': {'a': 1, 'b': 2, 'c': 3}, 'f_2': {'a': 1, 'b': 3, 'c': 3}}
    assert rekey_on_member(data=obj, key='a') == {1: {'a': 1, 'b': 2, 'c': 3}, 1: {'a': 1, 'b': 3, 'c': 3}}
    assert rekey_on_member(data=obj, key='a', duplicates='overwrite') == {1: {'a': 1, 'b': 3, 'c': 3}}

# Generated at 2022-06-22 11:55:43.487052
# Unit test for function symmetric_difference
def test_symmetric_difference():
    assert set([x for x in symmetric_difference([1, 2, 3], [3, 4, 5])]) == set([1, 2, 4, 5])

# Generated at 2022-06-22 11:55:49.634917
# Unit test for function max
def test_max():
    assert [3] == max([1, 3, 2])
    assert [3, 4, 5] == max([1, 4, 3, 5, 2])
    assert ['c'] == max(['a', 'c', 'b'])
    assert ['c', 'e', 'g'] == max(['a', 'c', 'e', 'b', 'd', 'g'])



# Generated at 2022-06-22 11:56:00.898247
# Unit test for function max
def test_max():
    assert max(1, 2) == 2
    assert max(1, 2, 3, 4, 5) == 5
    assert max(5, 3, 4, 1, 2) == 5
    assert max([1, 2, 3, 4, 5]) == 5
    assert max([5, 3, 4, 1, 2]) == 5
    assert max([1, 2, 3, 4, 5], key=lambda x: -x) == 1
    assert max(1, 2, key=lambda x: -x) == 1
    assert max(1, 2, key=lambda x: -x, default=42) == 1
    assert max(1, 2, key=lambda x: -x, default=0) == 1
    assert max([], default=0) == 0


# Generated at 2022-06-22 11:56:02.659944
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1


# Generated at 2022-06-22 11:56:12.333801
# Unit test for function rekey_on_member

# Generated at 2022-06-22 11:56:13.961155
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1



# Generated at 2022-06-22 11:56:17.477234
# Unit test for function min
def test_min():
    assert 0 == min([0, 1, 2])
    assert -1 == min([0, 1, -1, 2])
    assert -2 == min([0, 1, -1, 2, -2])


# Generated at 2022-06-22 11:56:28.807977
# Unit test for function max
def test_max():
    assert '1.5' == max(['1', '0.5', '1.5'])
    assert '0.9' == max(['0.1', '0.5', '0.9'])
    assert '0.9' == max(['0.5', '0.1', '0.9'])
    assert '0.9' == max(['0.9', '0.1', '0.5'])


# Generated at 2022-06-22 11:56:39.381938
# Unit test for function max
def test_max():
    environment = {}
    assert max(environment, [1, 2, 3]) == 3
    assert max(environment, [1, -2, 3]) == 3
    assert max(environment, [-1, -2, -3]) == -1
    assert max(environment, []) == None
    assert max(environment, "abc") == "c"

    assert max(environment, (1, 2, 3)) == 3
    assert max(environment, (1, -2, 3)) == 3
    assert max(environment, (-1, -2, -3)) == -1
    assert max(environment, "") == None
    assert max(environment, ()) == None
    assert max(environment, "abc") == "c"
    assert max(environment, ['a', 'b', 'cde']) == 'cde'


# Generated at 2022-06-22 11:56:43.907415
# Unit test for function max
def test_max():
    # setup
    test_list = [1, 2, 3]
    test_dict = {"foo": 1, "bar": 5, "baz": 2}

    assert max(test_list) == 3
    assert max(test_dict) == "bar"



# Generated at 2022-06-22 11:56:51.131882
# Unit test for function max
def test_max():

    assert max([1, 2, 3]) == 3
    assert max([1, 2, 3]) == max([3, 1, 2])

    assert max("abc") == "c"
    assert max("a123b456c789") == "c"

    assert max(1, 2, 3) == 3
    assert max(1, 3, 2) == 3
    assert max("c", "a", "b") == "c"
    assert max("cba") == "c"

    assert max(1, 3, 2, key=str) == 3
    assert max("cba", key=str) == "c"
    assert max("cba", key=lambda x: x.upper()) == "c"

    # test None as min value
    assert max([1, 2, 3, None]) == 3

    # test mixing types
   

# Generated at 2022-06-22 11:56:58.244403
# Unit test for function unique
def test_unique():
    ### Test case failure: no parameters ###
    try:
        unique()
    except TypeError as e:
        if "unique() missing 1 required positional argument: 'a'" in to_native(e):
            pass
        else:
            raise AnsibleFilterError('unique filter failed to raise TypeError: no parameters')
    except Exception:
        raise AnsibleFilterError('unique filter failed to raise TypeError: no parameters')

    ### Test case success: simple list ###
    result = unique([1, 2, 3, 2, 1, 2, 4, 5, 6, 7, 8, 9, 8, 7, 6])
    if result != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        raise AnsibleFilterError('unique filter not working properly')

    ### Test case success: simple dict ###

# Generated at 2022-06-22 11:57:06.888751
# Unit test for function max
def test_max():

    # Basic tests
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max([-99, -10, 10]) == 10

    # Multiple args
    assert max(1, 2, 3) == 3

    # Not an iterable
    try:
        max("a", "b", "c")
        assert False, "max() did not raise a TypeError"
    except TypeError:
        pass # expected

    # Empty iterable
    try:
        max([])
        assert False, "max() did not raise a ValueError"
    except ValueError:
        pass # expected


# Generated at 2022-06-22 11:57:13.579468
# Unit test for function max
def test_max():
    assert max(list(range(1, 5))) == 4

    assert max([1, 2], [3, 4]) == [3, 4]

    assert max(['a', 'b'], ['c', 'd']) == ['c', 'd']

    assert max(['a', 1], [3, 4]) == [3, 4]

    assert max([1, 2], [3, 'c']) == [3, 'c']

    assert max([1, 'a'], ['b', 4]) == ['b', 4]

    assert max([1, 'a'], ['b', 'c']) == ['b', 'c']

# Generated at 2022-06-22 11:57:18.016653
# Unit test for function max
def test_max():
    test_list = [1, 2, 3, 6]
    assert max(test_list) == 6

    test_list = [-1, 2, 3, -6]
    assert max(test_list) == 3

    test_list = ["a", "b", "c"]
    assert max(test_list) == "c"

    test_list = ["a", "B", "c"]
    assert max(test_list) == "c"
    assert max(test_list, key=str.lower) == "b"



# Generated at 2022-06-22 11:57:20.948403
# Unit test for function max
def test_max():
    data = [1, 2, 3, 4, 5]
    assert max(data) == 5



# Generated at 2022-06-22 11:57:29.954485
# Unit test for function min
def test_min():
    filter = FilterModule()
    ansible_min = filter.filters().get("min")

    # test original behavior:
    assert ansible_min([0, 1, 2]) == 0

    # test new behavior with kwargs:
    assert ansible_min([0, 1, 2], default=5) == 0
    assert ansible_min([], default=5) == 5
    assert ansible_min([2, 1, 0], by=abs) == 0
    assert ansible_min([{1: 1, 2: 2}, {1: 10, 2: 20}], by=lambda x: x[1]) == {1: 1, 2: 2}



# Generated at 2022-06-22 11:57:43.500104
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3


# Generated at 2022-06-22 11:57:45.654336
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([1, 2, 3], 2) == 2


# Generated at 2022-06-22 11:57:49.653397
# Unit test for function max
def test_max():
    y = max([1, 2, 3])
    assert y == 3

    y = max([1, 3, 2])
    assert y == 3

    y = max([3, 2, 1])
    assert y == 3

    y = max([3, 3, 3])
    assert y == 3



# Generated at 2022-06-22 11:57:57.311253
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5]) == 1
    assert min(['foo', 'bar', 'yum']) == 'bar'
    assert min([[1, 2], [1], [2]]) == [1]
    assert min(['foo', 'bar', 'yum'], attribute='upper') == 'BAR'
    assert min([1, 2, 3, 4, 5], attribute=lambda x: x*2) == 1


# Generated at 2022-06-22 11:58:05.397684
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_bytes

    assert rekey_on_member(
        ImmutableDict([('b', ImmutableDict([('a', 1), ('c', 2)])),
                       ('d', ImmutableDict([('a', 3), ('c', 4)])),
                       ('e', ImmutableDict([('a', 5), ('c', 6)]))]),
        'a',
    ) == ImmutableDict([
        (1, ImmutableDict([('a', 1), ('c', 2)])),
        (3, ImmutableDict([('a', 3), ('c', 4)])),
        (5, ImmutableDict([('a', 5), ('c', 6)])),
    ])
   

# Generated at 2022-06-22 11:58:17.053814
# Unit test for function unique
def test_unique():
    data = [1, 2, 1, 2, 3, 4, 5, 1]
    assert unique(data) == [1, 2, 3, 4, 5]
    assert unique(data, False) == [1, 2, 3, 4, 5]
    assert unique(data, case_sensitive=False) == [1, 2, 3, 4, 5]
    data = [1, 2, 1, 2, 3, 4, 5, 1, 6, 7, 8, 9]
    assert unique(data, False) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert unique(data, False, attribute='id') == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-22 11:58:29.198242
# Unit test for function human_readable
def test_human_readable():
    from ansible.compat import unittest

    class TestHumanReadable(unittest.TestCase):

        def test_valid_values_bytes(self):
            self.assertEqual(human_readable(1023), '1023 B')
            self.assertEqual(human_readable(1024), '1.0 KiB')
            self.assertEqual(human_readable(1024, isbits=False, unit=''), '1.0')
            self.assertEqual(human_readable(1024, isbits=False, unit='B'), '1.0 KiB')
            self.assertEqual(human_readable('1024', isbits=False, unit='B'), '1.0 KiB')
            self.assertEqual(human_readable('1024', isbits=False, unit='B'), '1.0 KiB')


# Generated at 2022-06-22 11:58:38.127282
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(1, unit='K') == '1.0K'
    assert human_readable(1, unit='K', isbits=True) == '8.0K'
    assert human_readable(1, unit='K') == '1K'
    assert human_readable(1, unit='K', isbits=True) == '8K'
    assert human_readable(10000, unit='K') == '10.0K'
    assert human_readable(10000, unit='K', isbits=True) == '80.0K'
    assert human_readable(10000, unit='K') == '10K'
    assert human_readable(10000, unit='K', isbits=True) == '80K'
    assert human_readable(20000, unit='K') == '20.0K'

# Generated at 2022-06-22 11:58:50.044919
# Unit test for function min
def test_min():
    environment = object
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    c = [1, 2, 3, 4, 5, 6]

    assert min(environment, a) == 1
    assert min(environment, b) == 1
    assert min(environment, c) == 1

    assert min(environment, a, reverse=True) == 5
    assert min(environment, b, reverse=True) == 5
    assert min(environment, c, reverse=True) == 6

    assert min(environment, [4, 2, 5, 1, 3], reverse=True) == 5

    assert min(environment, [2, 3, 1], reverse=False, key=lambda x: x * -1) == 3


# Generated at 2022-06-22 11:58:51.236775
# Unit test for function max
def test_max():

    expected = 10
    test = max([4, 10, 2])

    assert test == expected

# Generated at 2022-06-22 11:59:49.861133
# Unit test for function max
def test_max():

    assert max([1, 2, 3]) == 3
    assert max([1, 2, 3, 4]) == 4
    assert max(1, 2, 3, 4) == 4
    assert max() == None
    assert max([]) == None
    assert max([0]) == 0
    assert max([1, 0]) == 1
    assert max([-1, -10, -100]) == -1
    assert max([2, 2, 2, 2, 2, 2, 2]) == 2

    # max of strings
    assert max('abc') == 'c'
    assert max('abcd') == 'd'
    assert max('ab') == 'b'
    assert max('') is None
    assert max('a') == 'a'

    # max of mixed strings and numbers
    assert max([1, 'a']) == 1
   

# Generated at 2022-06-22 11:59:51.750126
# Unit test for function max
def test_max():
    assert max([15, 6]) == 15



# Generated at 2022-06-22 12:00:01.013365
# Unit test for function rekey_on_member
def test_rekey_on_member():
    # create a test object
    testobj = { "obj1" : { "key1" : "value1", "key2" : "value2" },
            "obj2" : { "key1" : "value1", "key3" : "value3" }}

    testobj2 = { "obj1" : { "key1" : "value1", "key2" : "value2" },
            "obj2" : { "key1" : "value1", "key3" : "value3" },
            "obj3" : { "key1" : "value1", "key4" : "value4" }}

    # test for object key1 should be obj1, obj2
    rekey_obj = rekey_on_member(testobj, "key1")

# Generated at 2022-06-22 12:00:12.942768
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(100) == '100 B'
    assert human_readable(100, isbits=True) == '800 b'
    assert human_readable(1099, unit='B', isbits=True) == '8.83 Kb'
    assert human_readable(1099, unit='K', isbits=False) == '1099 K'
    assert human_readable(1099, unit='K', isbits=True) == '8.77 Kb'
    assert human_readable('1099', unit='K', isbits=True) == '8.77 Kb'
    assert human_readable('2.2 Ki', unit='K', isbits=True) == '2.16 Kb'
    assert human_readable('g', unit='K', isbits=True) == '8192 b'

# Generated at 2022-06-22 12:00:18.866357
# Unit test for function min
def test_min():
    fm = FilterModule()
    assert fm.filters()['min']([1, 2, 1000, -1]) == -1
    assert fm.filters()['min']({'a': 1, 'b': 2, 'c': 1000, 'd': -1}) == -1
    assert fm.filters()['min']('foo') == 'f'



# Generated at 2022-06-22 12:00:25.965154
# Unit test for function max
def test_max():
    def _test_max(input_val, expected_val):
        assert (max(input_val) == expected_val)
    _test_max({1: 2, 2: 4, 3: 6}, {3: 6, 2: 4, 1: 2})
    _test_max([1, 2, 3, 4, 5], 5)
    _test_max('12345', '5')


# Generated at 2022-06-22 12:00:29.731600
# Unit test for function min
def test_min():
    assert [1, 2, 3, 4] == min([1,2,3,4])
    assert -1 == min([-1,0,1,2])
    assert 'a' == min(['a','b','c'])



# Generated at 2022-06-22 12:00:33.619723
# Unit test for function max
def test_max():
    from jinja2 import Environment
    test = Environment().from_string('''{{ [1,2,3,4,5] | max }}''')
    assert test.render() == '5'

# Generated at 2022-06-22 12:00:43.701690
# Unit test for function unique
def test_unique():
    env = {'vars': {}}
    filters = FilterModule().filters()
    assert filters['unique'](env, [1, 1, 2, 3, 4, 5, 5], True) == [1, 2, 3, 4, 5]
    assert filters['unique'](env, [1, 1, 2, 3, 4, 5, 5], False) == [1, 2, 3, 4, 5]
    assert filters['unique'](env, [1, 1, 2, 3, 4, 5, 5], None) == [1, 1, 2, 3, 4, 5, 5]