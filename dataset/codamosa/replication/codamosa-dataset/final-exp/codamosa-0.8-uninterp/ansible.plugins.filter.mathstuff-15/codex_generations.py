

# Generated at 2022-06-22 11:50:50.220881
# Unit test for function symmetric_difference

# Generated at 2022-06-22 11:50:52.096609
# Unit test for function power
def test_power():
    assert power(3, 2) == 9



# Generated at 2022-06-22 11:51:04.159485
# Unit test for function rekey_on_member
def test_rekey_on_member():
    """
    Test the rekey_on_member function

    These tests use python's internal unittest module

    They also include a safety test against a regression in Ansible 2.7.0
    (https://github.com/ansible/ansible/issues/44418) for which we have a fix
    and can be removed if the fix is merged in Ansible

    To run these tests, invoke this module directly with Python3:
      python3 filter_plugins/math.py
    """
    import unittest
    from ansible.module_utils.common._collections_compat import Mapping, MutableSequence

    class MathFiltersTests(unittest.TestCase):
        """Test math filters"""


# Generated at 2022-06-22 11:51:08.909026
# Unit test for function symmetric_difference
def test_symmetric_difference():
    ansible_filter = FilterModule()
    filters = ansible_filter.filters()
    my_var = filters['symmetric_difference'](["e", "f", "g"], ["a", "b", "c"])
    assert len(my_var) == 6



# Generated at 2022-06-22 11:51:10.488733
# Unit test for function logarithm
def test_logarithm():
    assert FilterModule().filters()['log'](math.e) == 1



# Generated at 2022-06-22 11:51:20.689490
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1t') == 1024 ** 4
    assert human_to_bytes('1T') == 1024 ** 4
    assert human_to_bytes('1g') == 1024 ** 3
    assert human_to_bytes('1G') == 1024 ** 3
    assert human_to_bytes('1m') == 1024 ** 2
    assert human_to_bytes('1M') == 1024 ** 2
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1kbit') == 1024 / 8
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1mbit') == 1024 ** 2 / 8

# Generated at 2022-06-22 11:51:24.387288
# Unit test for function max
def test_max():
    assert max(8, 0) == 8
    assert max(0, 8) == 8
    assert max(-1, 1) == 1
    assert max(1, -1) == 1
    assert max([3, 2, 1]) == 3
    assert max([100, 10, 1000]) == 1000
    assert max([1, 10, 10, 100]) == 100
    assert max('abc') == 'c'
    assert max(['a', 'b', 'c']) == 'c'
    assert max(['a', 'b', 'ccc']) == 'ccc'



# Generated at 2022-06-22 11:51:27.084444
# Unit test for function max
def test_max():
    assert max([1,2,3]) == 3
    assert max([1,2,3,3]) == 3


# Generated at 2022-06-22 11:51:37.268164
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("1B") == 1
    assert human_to_bytes("1.0 B") == 1
    assert human_to_bytes("0B") == 0
    assert human_to_bytes("0.0 B") == 0
    assert human_to_bytes("1KB") == 1024
    assert human_to_bytes("1.0 KB") == 1024
    assert human_to_bytes("1MB") == 1024 ** 2
    assert human_to_bytes("1.0 MB") == 1024 ** 2
    assert human_to_bytes("1GB") == 1024 ** 3
    assert human_to_bytes("1.0 GB") == 1024 ** 3
    assert human_to_bytes("1TB") == 1024 ** 4
    assert human_to_bytes("1.0 TB") == 1024 ** 4
    assert human_to_bytes

# Generated at 2022-06-22 11:51:41.278404
# Unit test for function symmetric_difference
def test_symmetric_difference():
    module = FilterModule()
    assert module.filters()['symmetric_difference']([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]

# Generated at 2022-06-22 11:52:02.174183
# Unit test for function human_to_bytes
def test_human_to_bytes():
    h2b = human_to_bytes
    assert h2b('0') == 0
    assert h2b('0.0') == 0
    assert h2b('10') == 10
    assert h2b('10s') == 10
    assert h2b('10S') == 10
    assert h2b('10MB') == 10 * 1024 ** 2
    assert h2b('10GB') == 10 * 1024 ** 3
    assert h2b('10TB') == 10 * 1024 ** 4
    assert h2b('10PB') == 10 * 1024 ** 5
    assert h2b('10EB') == 10 * 1024 ** 6
    assert h2b('10ZB') == 10 * 1024 ** 7
    assert h2b('10YB') == 10 * 1024 ** 8
    assert h2b('10BB') == 10 * 1024 ** 9

# Generated at 2022-06-22 11:52:03.151197
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4, 5]) == 1


# Generated at 2022-06-22 11:52:10.624232
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3, "Normal max failed"
    assert max({1: "foo", 2: "bar", 3: "baz"}) == 3, "Normal max failed"
    assert max(["foo", "bar", "baz"]) == "baz", "Normal max failed"
    assert max([], default=10) == 10, "Normal max failed"
    assert max({}, default=10) == 10, "Normal max failed"

# Generated at 2022-06-22 11:52:15.561283
# Unit test for function min
def test_min():
    from ansible.template import AnsibleJ2

    j2env = AnsibleJ2()
    mydict = {'a': 2, 'b': 3, 'c': 1}
    text = "{{ mydict|min }}"
    mytext = j2env.from_string(text).render(mydict=mydict)
    assert mytext == 'a'

# Generated at 2022-06-22 11:52:26.005452
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(10) == '10 Bytes'
    assert human_readable(1024) == '1.00 KiB', '%s != "1.00 KiB"' % human_readable(1024)
    assert human_readable(1024 * 1024) == '1.00 MiB', '%s != "1.00 MiB"' % human_readable(1024 * 1024)
    assert human_readable(1024 * 1024 * 1024) == '1.00 GiB', '%s != "1.00 GiB"' % human_readable(1024 * 1024 * 1024)
    assert human_readable(1000) == '1.00 KB', '%s != "1.00 KB"' % human_readable(1000)
    assert human_readable(1024 * 1024 - 1) == '1024.00 KiB', '%s != "1024.00 KiB"' % human_

# Generated at 2022-06-22 11:52:37.620114
# Unit test for function max
def test_max():
    fm = FilterModule()
    filters = fm.filters()

    a = (1, 2, 3)
    b = [4, 5, 6]
    c = {'k1': 7, 'k2': 8, 'k3': 9}
    d = (10, 11, 12)
    e = (1, 2)
    f = {'k4': 10, 'k5': 11, 'k6': 12}

    assert filters['max'](a) == 3
    assert filters['max'](b) == 6
    assert filters['max'](c) == 'k3'
    assert filters['max'](d) == 12
    assert filters['max'](e) == 2
    assert set(filters['max'](f).keys()) == set(['k4', 'k5', 'k6'])

# Generated at 2022-06-22 11:52:46.307148
# Unit test for function rekey_on_member

# Generated at 2022-06-22 11:52:56.296121
# Unit test for function logarithm
def test_logarithm():
    logger = logging.getLogger('unit_test')
    logger.info('Testing logarithm Filter')
    test_cases = [
        (1, 1, math.e, 0.0),
        (2, 1, math.e, 0.69314718056),
        (2, 2, math.e, 0.69314718056),
        (2, 2, 10, 1),
        ('bad', 2, math.e, None)
    ]

    for val, base, ex, result in test_cases:
        if ex is None:
            try:
                logarithm(val, base)
                assert(False)
            except AnsibleFilterTypeError:
                assert(True)

# Generated at 2022-06-22 11:53:07.863950
# Unit test for function unique
def test_unique():
    # TODO: add a test for case_sensitive=False
    assert unique([1, 1, 2, 3, 3]) == [1, 2, 3]
    assert unique([1, 'foo', 'bar', 1, 1]) == [1, 'foo', 'bar']
    assert unique([1, 'bar', {'foo': 'bar', 'bar': 'foo'}, {'foo': 'bar'}]) == [1, 'bar', {'foo': 'bar', 'bar': 'foo'}, {'foo': 'bar'}]
    assert unique([1, 'bar', {'foo': 'bar'}, {'foo': 'bar'}]) == [1, 'bar', {'foo': 'bar'}]
    assert unique([1, 'bar', 'bar']) == [1, 'bar']

# Generated at 2022-06-22 11:53:09.432772
# Unit test for function min
def test_min():
    assert min([1, 2, 3, 4]) == 1



# Generated at 2022-06-22 11:53:40.847747
# Unit test for function rekey_on_member
def test_rekey_on_member():
    from ansible.module_utils.other import rekey_on_member
    test_list = [
        { 'member_a' : 1, 'member_b' : 'foo', 'id' : 'one' },
        { 'member_a' : 2, 'member_b' : 'bar', 'id' : 'two' },
        { 'member_a' : 3, 'member_b' : 'baz', 'id' : 'three' },
    ]
    result_dict = rekey_on_member(test_list, 'id')

    assert isinstance(result_dict, dict)
    assert len(result_dict) == 3
    assert result_dict['one']['member_a'] == 1
    assert result_dict['two']['member_a'] == 2

# Generated at 2022-06-22 11:53:45.302801
# Unit test for function min
def test_min():
    key = ['b', 'c', 'a']
    value = [2, 1, 3]
    dictionary = dict(zip(key, value))

    correct_min = min(dictionary)
    assert(correct_min == 'a')

# Generated at 2022-06-22 11:53:57.472836
# Unit test for function unique
def test_unique():
    from ansible.module_utils.six import PY3
    from jinja2 import DictEnvironment, StrictUndefined
    env = DictEnvironment(undefined=StrictUndefined)
    assert unique(env, ['a', 'b', 'c'], True) == ['a', 'b', 'c']
    assert unique(env, ['a', 'A', 'c'], True) == ['a', 'A', 'c']
    assert unique(env, ['a', 'a', 'c'], True) == ['a', 'c']
    assert unique(env, ['a', 'a', 'a'], True) == ['a']
    assert unique(env, {'a': 1}, True) == [{'a': 1}]

# Generated at 2022-06-22 11:53:59.706914
# Unit test for function logarithm
def test_logarithm():
    f = FilterModule()
    assert f.filters()['log'](16, 2) == 4



# Generated at 2022-06-22 11:54:01.037634
# Unit test for function max
def test_max():
    assert max([3,4,1]) == 4

# Generated at 2022-06-22 11:54:12.121360
# Unit test for function rekey_on_member

# Generated at 2022-06-22 11:54:20.432431
# Unit test for function max
def test_max():
    import jinja2
    # Test a list of variable types
    assert jinja2.Environment().from_string('{{ [1, 2, 3, 4, 5] | max }}').render() == '5'
    assert jinja2.Environment().from_string('{{ [1, 2, 3, 4, 5, 6, 7] | max }}').render() == '7'
    assert jinja2.Environment().from_string('{{ [3.14, 2.72, 5.6, 1.6] | max }}').render() == '5.6'
    assert jinja2.Environment().from_string('{{ ["Betty", "Boop", "Bertha"] | max }}').render() == 'Betty'

# Generated at 2022-06-22 11:54:24.585356
# Unit test for function min
def test_min():
    assert min(None, [1, 2, 3]) == 1
    assert min(None, []) == None
    assert min(None, [[1], [2], [1, 2, 3]]) == [1]
    assert min(None, [[1, 2, 3], [1], [2]]) == [1]


# Generated at 2022-06-22 11:54:37.361322
# Unit test for function rekey_on_member
def test_rekey_on_member():

    data = [{"key1": "val1", "key2": "val2"}, {"key1": "val3", "key2": "val4"}]

    # rekey with key1
    new_data = rekey_on_member(data, "key1")
    assert len(new_data) == 2
    assert "val1" in new_data
    assert "val3" in new_data

    # rekey with key2
    new_data = rekey_on_member(data, "key2")
    assert len(new_data) == 2
    assert "val2" in new_data
    assert "val4" in new_data

    # duplicate keys allowed

# Generated at 2022-06-22 11:54:48.043020
# Unit test for function human_readable
def test_human_readable():
    assert human_readable(0, isbits=False, unit=None) == '0.0 B'
    assert human_readable(0, isbits=True, unit=None) == '0.0 B'
    assert human_readable(10, isbits=False, unit=None) == '10.0 B'
    assert human_readable(10, isbits=True, unit=None) == '80.0 B'
    assert human_readable(100, isbits=False, unit=None) == '100.0 B'
    assert human_readable(100, isbits=True, unit=None) == '800.0 B'
    assert human_readable(1000, isbits=False, unit=None) == '1000.0 B'
    assert human_readable(1000, isbits=True, unit=None) == '8000.0 B'

# Generated at 2022-06-22 11:55:05.319346
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(None) == None
    assert logarithm(1) == 0
    assert logarithm(math.e) == 1
    assert logarithm(100) == math.log(100)
    assert logarithm(100, 10) == math.log(100, 10)
    assert logarithm(100, 2) == math.log(100, 2)


# Generated at 2022-06-22 11:55:09.480341
# Unit test for function logarithm
def test_logarithm():
    assert math.log(1) == logarithm(1)
    assert math.log(1, 2) == logarithm(1, 2)
    assert math.log10(1000) == logarithm(1000, 10)



# Generated at 2022-06-22 11:55:15.878336
# Unit test for function min
def test_min():
    # Test is a simple pass thru test, the default python min will work correctly
    # and any special cases should be handled above
    assert min([1, 2, 3]) == min([1, 2, 3])
    # Test with an object that has defined it's own __lt__
    assert min(["a", "b", "c"]) == min(["a", "b", "c"])
    # Test that min will return an empty list instead of the NoneType error from
    # the default min
    assert min([]) == min([])


# Generated at 2022-06-22 11:55:22.767556
# Unit test for function min
def test_min():
    f = FilterModule()
    int_list = [1, 2, 3, 4]
    str_list = ['a', 'b', 'c', 'd']
    mixed_list = [1, 'a', 'c', 4]

    assert f.filters()['min'](int_list) == 1
    assert f.filters()['min'](str_list) == 'a'
    assert f.filters()['min'](mixed_list) == 1



# Generated at 2022-06-22 11:55:27.128771
# Unit test for function logarithm
def test_logarithm():
    try:
        logarithm(10)
    except AnsibleFilterError:
        pass
    except Exception:
        assert False
    try:
        logarithm(100)
    except AnsibleFilterError:
        assert False
    except Exception:
        pass



# Generated at 2022-06-22 11:55:31.786935
# Unit test for function logarithm
def test_logarithm():
    assert logarithm(10) == 2.302585092994046
    assert logarithm(10, base=10) == 1.0
    assert logarithm(10, base=1) == 10
    assert logarithm(10, base=2.0) == 3.321928094887362
    assert logarithm(1000, base=10) == 3.0
    assert logarithm(math.e) == 1.0


# Generated at 2022-06-22 11:55:41.475554
# Unit test for function min
def test_min():
    from ansible.plugins.filter import mathstuff

    assert mathstuff.min([]) == mathstuff.min(()) == None, "Failed to return None for empty list or tuple"
    assert mathstuff.min([1,2,3,4]) == 1, "Failed to return the lowest value in a list"
    assert mathstuff.min((1,2,3,4)) == 1, "Failed to return the lowest value in a tuple"
    assert mathstuff.min((4,3,2,1)) == 1, "Failed to return the lowest value in a tuple"
    assert mathstuff.min({'a':1, 'b':2}) == mathstuff.min({'b':2, 'a':1}) == 1, "Failed to return the lowest value in a dictionary"

# Generated at 2022-06-22 11:55:53.593037
# Unit test for function rekey_on_member
def test_rekey_on_member():
    import pytest
    from jinja2.exceptions import UndefinedError
    from jinja2.exceptions import UndefinedError
    from jinja2.exceptions import UndefinedError
    from jinja2.exceptions import UndefinedError

    data = [
        {'a': 1, 'b': 1},
        {'a': 3, 'b': 2},
        {'a': 2, 'b': 4},
        {'a': 4, 'b': 3}
    ]

    # Ensure we can't rekey unless we've specified both the data and the key
    with pytest.raises(UndefinedError):
        rekey_on_member(data, 'a')
    with pytest.raises(UndefinedError):
        rekey_on_member(None, 'a')

    # Ensure we can

# Generated at 2022-06-22 11:56:03.900241
# Unit test for function max
def test_max():
    assert max([1, 2, 3]) == 3
    assert max([1, 3, 2]) == 3
    assert max(['a', 'b', 'c']) == 'c'
    assert max('abc') == 'c'
    assert max('abc') == max(['a', 'b', 'c'])
    assert max([]) is None
    assert max(()) is None
    assert max('') is None
    assert max('123') == '3'
    assert max([1, 'a']) == 'a'
    assert max([1, 'a', 2, 'b']) == 'b'
    assert max(['a', 'b', 2, '1']) == 'b'
    assert max(['a', 'b', 'c', 'd', 'e']) == 'e'


# Generated at 2022-06-22 11:56:06.908855
# Unit test for function min
def test_min():
    from jinja2 import Environment

    env = Environment()
    assert env.from_string('{{ [3, 1, 2] | min }}').render() == '1'



# Generated at 2022-06-22 11:56:15.440321
# Unit test for function min
def test_min():
    assert min([0, 1, 99, 5]) == 0


# Generated at 2022-06-22 11:56:27.029760
# Unit test for function min
def test_min():
    f = FilterModule()
    env = {'from_string': True}

    assert f.filters()['min'](env, [2, 3, 4, 1]) == 1
    assert f.filters()['min'](env, [2, 3, 4, 1], attribute='length') == [4, 1]
    assert f.filters()['min'](env, 2, 3, 4, 1) == 1
    assert f.filters()['min'](env, 2, 3, 4, 1, attribute='length') == [4, 1]

    assert f.filters()['min'](env, []) == ''
    assert f.filters()['min'](env, [], attribute='length') == ''
    assert f.filters()['min'](env) == ''

# Generated at 2022-06-22 11:56:34.567065
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min(["b", "a", "c"]) == "a"
    assert min([[1,2,3], [4,5,6]]) == [1,2,3]
    assert min([{'b': 2}, {'a': 1}]) == {'a': 1}
    assert min([[1, 2, 3], {"b": 1}]) == [1, 2, 3]
    assert min([[1, 2, 3], {"b": 1, "c": 2}]) == {'b': 1, 'c': 2}
    assert min([{'b': 2}, [1, 2, 3]]) == {'b': 2}


# Generated at 2022-06-22 11:56:44.423942
# Unit test for function rekey_on_member
def test_rekey_on_member():
    # Test duplicate key handling
    list_of_dicts = [
        {'foo': 'a', 'bar': 'b'},
        {'foo': 'a', 'bar': 'c'},
        {'foo': 'd', 'bar': 'e'},
    ]
    assert rekey_on_member(list_of_dicts, 'foo', 'error') == {'a': {'foo': 'a', 'bar': 'b'}, 'd': {'foo': 'd', 'bar': 'e'}}
    assert rekey_on_member(list_of_dicts, 'foo', 'overwrite') == {'a': {'foo': 'a', 'bar': 'c'}, 'd': {'foo': 'd', 'bar': 'e'}}

    # Test missing key
    list_of_dict

# Generated at 2022-06-22 11:56:49.844109
# Unit test for function min
def test_min():
    assert min([1, 4, 2, 6, 2]) == 1
    assert min([1, 4, 2, 'abc', 2]) == 1
    assert min([1, 4, 'abc', 6, 2]) == 'abc'
    assert min([1, (1, 2), (1, 2), (2, 1)]) == (1, 2)



# Generated at 2022-06-22 11:57:00.949042
# Unit test for function human_to_bytes

# Generated at 2022-06-22 11:57:09.732646
# Unit test for function rekey_on_member
def test_rekey_on_member():
    test_dict = {'a': {'name': 'a', 'id': 1}, 'b': {'name': 'b', 'id': 2}}
    test_list = [{'name': 'a', 'id': 1}, {'name': 'b', 'id': 2}]

    assert rekey_on_member(test_dict, 'name') == {'a': {'name': 'a', 'id': 1}, 'b': {'name': 'b', 'id': 2}}
    assert rekey_on_member(test_list, 'name') == {'a': {'name': 'a', 'id': 1}, 'b': {'name': 'b', 'id': 2}}

# Generated at 2022-06-22 11:57:13.369902
# Unit test for function min
def test_min():
    assert min([4,2,1,3]) == 1
    assert min((4,2,1,3)) == 1
    assert min({4: 'd', 2:'b', 1:'a', 3:'c'}) == 1


# Generated at 2022-06-22 11:57:25.608218
# Unit test for function rekey_on_member
def test_rekey_on_member():

    t_dict = {'name': 'Tom', 'age': 32, 'gender': 'M'}
    alice_dict = {'name': 'Alice', 'age': 23, 'gender': 'F'}
    bob_dict = {'name': 'Bob', 'age': 28, 'gender': 'M'}
    dict_list = [alice_dict, bob_dict, t_dict]
    dict_list_with_duplicate_keys = [alice_dict, bob_dict, t_dict.copy(), t_dict.copy()]

    # Test rekeying dict of dicts
    result = rekey_on_member(t_dict, 'name')
    assert len(result) == 1, "rekey_on_member didn't rekey dictionary on name key"

    # Test creating dict from list of dicts without

# Generated at 2022-06-22 11:57:27.787656
# Unit test for function min
def test_min():
    assert 7 == min([9, 8, 7, 6, 5])
    assert 4 == min([5, 9, 8, 7], key=lambda x: x % 5)
    assert min([1, 2, 3, 'x'], key=lambda x: x % 5) == 'x'



# Generated at 2022-06-22 11:57:45.698583
# Unit test for function human_readable
def test_human_readable():
    """
    Function to test human_readable function
    :return:
    """
    assert human_readable("42") == "42 B"
    assert human_readable("1024") == "1 KB"
    assert human_readable("42", isbits=True) == "42 b"
    assert human_readable("42", unit='KiB') == "42 KiB"

# Generated at 2022-06-22 11:57:52.987376
# Unit test for function unique
def test_unique():
    assert (unique([1, 2, 3]) == [1, 2, 3])
    assert (unique([3, 2, 1]) == [3, 2, 1])
    assert (unique((1, 2, 2, 3)) == [1, 2, 3])
    assert (unique(["this", "that", "that"]) == ["this", "that"])
    hits = {"foo": 1, "bar": 2}
    assert (len(unique(hits.values())) == 2)
    assert (unique([1, 2, 3]) == unique((1, 2, 3)))
    assert (unique([1, 2, 3]) == unique([1, 2, 3]))
    assert (unique(["this", "that", "that"]) == unique(["this", "that", "that"]))

# Generated at 2022-06-22 11:58:03.177561
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1
    assert min([3, 2, 1]) == 1
    assert min([-1, -2, -3]) == -3
    assert min([1, 2, 3], attribute='foo') == 1
    assert min([{'foo': 2}, {'foo': 1}], attribute='foo') == {'foo': 1}
    assert min([1, 2, 3, float("nan")]) == 1
    assert min([float("nan"), float("nan"), float("nan")]) is float("nan")
    assert min([1, 2, 3, float("inf")]) == 1
    assert min([float("inf"), float("inf"), float("inf")]) == float("inf")


# Generated at 2022-06-22 11:58:05.037512
# Unit test for function max
def test_max():
    assert max([1, 4, 2, 7, 10, 3]) == 10

# Generated at 2022-06-22 11:58:09.495175
# Unit test for function min
def test_min():
    module = FilterModule()
    assert module.filters()['min']([1, 2, 3, 0]) == 0
    assert module.filters()['min']({'a': 1, 'b': 2, 'c': 3, 'd': 0}) == 0


# Generated at 2022-06-22 11:58:11.043678
# Unit test for function min
def test_min():
    assert min([1, 2, 3]) == 1


# Generated at 2022-06-22 11:58:16.718638
# Unit test for function min
def test_min():
    from ansible.module_utils.common.text import format_module_docstring

    if not HAS_MIN_MAX:
        return

    module_name = 'ansible.module_utils.six'
    module = format_module_docstring(module_name, globals()[module_name])
    doc = getattr(module, '__doc__')
    print(doc)

# Generated at 2022-06-22 11:58:21.076602
# Unit test for function unique
def test_unique():
    assert unique(None, [1, 2, 1]) == [1, 2]
    assert unique(None, [1, 2, 1], False) == [1, 2]
    assert unique(None, [{'a': 1}, {'a': 2}, {'a': 1}], attribute='a') == [{'a': 1}, {'a': 2}]
    assert unique(None, [1, 2, 1], case_sensitive=False) == [1, 2]
    assert unique(None, [1, 2, 1], case_sensitive=None) == [1, 2]

# Generated at 2022-06-22 11:58:31.971883
# Unit test for function human_readable
def test_human_readable():
    assert human_readable("10") == "10B"
    assert human_readable("10M") == "10M"
    assert human_readable("10MB") == "10M"
    assert human_readable("10.3e+3") == "10.3K"
    assert human_readable("10.3K") == "10.3K"
    assert human_readable("10.3KB") == "10.3K"
    assert human_readable("10.3KB", isbits=True) == "10.3Kb"

    # Test for negative numbers
    assert human_readable("-10.3KB", isbits=True) == "-10.3Kb"
    assert human_readable("-10.3") == "-10.3"

    # Test fallback to default unit

# Generated at 2022-06-22 11:58:44.135416
# Unit test for function min
def test_min():
    try:
        min([1, 2, 3, 4, 5])
        assert False, ""
    except AssertionError:
        pass
    assert min([]) == min([])
    assert min([1]) == 1
    assert min([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert min([3, -3, 0]) == -3
    assert min([3, -3, 0], absolute=True) == 0
    assert min([3.1, -3.1, 0.1]) == -3.1
    assert min([3.1, -3.1, 0.1], absolute=True) == 0.1
    assert min([3.0, -3.0, 0]) == -3.0

# Generated at 2022-06-22 11:59:15.141908
# Unit test for function human_readable
def test_human_readable():
    import pytest

# Generated at 2022-06-22 11:59:18.815422
# Unit test for function unique
def test_unique():
    filter = FilterModule().filters()
    data = [1, 2, 2, 3]
    assert filter['unique'](data, True) == [1, 2, 3]


# Generated at 2022-06-22 11:59:21.142356
# Unit test for function min
def test_min():
    assert min([4, 2, 1, 3]) == 1
    assert min((4, 2, 1, 3)) == 1


# Generated at 2022-06-22 11:59:29.941945
# Unit test for function min
def test_min():
    data = [5, 10, 12, 3, 10, 6, 4, 10, 1]
    data_str = ['5', '10', '12', '3', '10', '6', '4', '10', '1']
    data_str_beta = ['a', 'z', 'f', 'g', 'm']
    data_str_alpha = ['a', 'z', 'f', 'g', 'm']
    data_dict = {'test1': 10, 'test2': 1, 'test3': 5, 'test4': 12}
    data_dict_alpha = {'a': 1, 'z': 5, 'f': 3, 'g': 2, 'm': 0}

# Generated at 2022-06-22 11:59:40.530564
# Unit test for function human_to_bytes

# Generated at 2022-06-22 11:59:49.911273
# Unit test for function rekey_on_member
def test_rekey_on_member():
    ''' Test the rekey_on_member. '''
    test_obj = {
        'first': {
            'a': 'b',
            'c': 'd',
        },
        'second': {
            'a': 'z',
            'e': 'f',
        }
    }
    for key in ('a', 'c', 'e'):
        for duplicates in ('overwrite', 'error'):
            actual = rekey_on_member(test_obj, key, duplicates=duplicates)
            expected = {}
            for obj in test_obj.values():
                expected[obj[key]] = obj
            assert actual == expected

# Generated at 2022-06-22 12:00:00.042927
# Unit test for function max
def test_max():
    assert isinstance(max, collections.Callable)
    assert max(2, 3) == 3
    assert max(2.5, 3.5) == 3.5
    assert max(1.7, 1.7) == 1.7
    assert max(3, 2) == 3
    assert max(1, -5, 4, 10, -6, 0, -2, -2) == 10
    assert max([1, 5, 3, 7, 4, 3]) == 7
    assert max('bc') == 'c'
    assert max([5, 'bc']) == 'bc'
    assert max({0: 0, 1: 1, 2: 2}) == 2
    assert max(iter([5, 1])) == 5
    assert max({0: 0, 1: 1, 2: 2}.items()) == (2, 2)


# Generated at 2022-06-22 12:00:04.617085
# Unit test for function max
def test_max():
    assert(max([1]) == 1)
    assert(max([2, 3]) == 3)
    assert(max([2, 3, 3]) == 3)
    assert(max([1, 2, 0]) == 2)
    assert(max([-1, -2, -3]) == -1)


# Generated at 2022-06-22 12:00:09.079122
# Unit test for function max
def test_max():
    assert max([1,2,3]) == 3
    assert max('abc') == 'c'
    assert max([]) is None
    assert max(None) is None
    assert max(1) == TypeError("'int' object is not iterable")
    assert max({1,'abc'}) == TypeError("unorderable types: int() > str()")
    assert max({'a':1,'b':2,'c':3}) == KeyError("max() arg is an empty sequence")


# Generated at 2022-06-22 12:00:20.709524
# Unit test for function rekey_on_member
def test_rekey_on_member():
    test_data = {
        'data': {
            'one': {
                'id': 1,
                'name': 'one'
            },
            'two': {
                'id': 2,
                'name': 'two'
            }
        },
        'expected_result': {
            '1': {
                'id': 1,
                'name': 'one'
            },
            '2': {
                'id': 2,
                'name': 'two'
            }
        }
    }

    f = FilterModule()
    data = test_data['data']
    actual_result = f.filters()['rekey_on_member'](
        data,
        'id'
    )

    assert actual_result == test_data['expected_result']
