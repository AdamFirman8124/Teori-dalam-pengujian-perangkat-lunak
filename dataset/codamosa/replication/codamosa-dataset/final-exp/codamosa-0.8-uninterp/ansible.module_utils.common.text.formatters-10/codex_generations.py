

# Generated at 2022-06-12 23:48:55.388601
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 1048576/8
    assert human_to_bytes('-1Mb') == -1048576/8
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=True) == 1048576 * 8
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('10MB', isbits=True) == 10485760 * 8
    assert human_to_bytes('2G') == 2147483648
    assert human_to_bytes('2GB') == 2147483648

# Generated at 2022-06-12 23:48:59.235736
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_input = [1, 'Test', 'test']
    expected_output = [1, 'test', 'test']
    output = lenient_lowercase(test_input)

    assert output == expected_output



# Generated at 2022-06-12 23:49:08.904875
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Unit test for function human_to_bytes
    '''
    print('* Testing function human_to_bytes...')
    # Test for bytes case
    print('** Testing with Bytes case:')
    # Input: 10MB
    print('Testing with "10M".')
    assert human_to_bytes('10M') == 10485760, 'Testing with "10M" failed.'
    print('Passed')
    # Input: 1024
    print('Testing with "1024".')
    assert human_to_bytes('1024') == 1024, 'Testing with "1024" failed.'
    print('Passed')
    # Input: 1M
    print('Testing with "1M".')
    assert human_to_bytes('1M') == 1048576, 'Testing with "1M" failed.'
    print('Passed')
   

# Generated at 2022-06-12 23:49:12.224073
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'System', ['default', 'system'], object, object()]) == [1, 'System', ['default', 'system'], object, object()]
    assert lenient_lowercase(['System', 'Default', 'system', 'default']) == ['system', 'default', 'system', 'default']

# Generated at 2022-06-12 23:49:13.784870
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['a', 'b', 'c', 1]
    assert lenient_lowercase(lst) == ['a', 'b', 'c', 1]


# Generated at 2022-06-12 23:49:19.568616
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert(lenient_lowercase(['A', 'b', 'C']) == ['a', 'b', 'c'])
    assert(lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c'])
    assert(lenient_lowercase(['a', 'b', 1]) == ['a', 'b', 1])
    assert(lenient_lowercase([1, 'b', 1]) == [1, 'b', 1])
    assert(lenient_lowercase([1, 2, 3]) == [1, 2, 3])

# Generated at 2022-06-12 23:49:30.575054
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

# Generated at 2022-06-12 23:49:35.050470
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    if lenient_lowercase(('asd', 1, 'asdf')) != ['asd', 1, 'asdf']:
        raise AssertionError()
    if lenient_lowercase(('aaa', 'aaa', 'AAA')) != ['aaa', 'aaa', 'AAA']:
        raise AssertionError()
    if lenient_lowercase(('aaa', 'bbb', 'ccc')) != ['aaa', 'bbb', 'ccc']:
        raise AssertionError()


# Generated at 2022-06-12 23:49:40.859149
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a', 'B', 'c', 1, []] == lenient_lowercase(['a', 'B', 'c', 1, []])
    assert ['a', 'b', 1, []] == lenient_lowercase(['A', 'B', 1, []])
    assert ['a', 'b', 1, []] == lenient_lowercase(['A', 'b', 1, []])

# Generated at 2022-06-12 23:49:50.980665
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB', 'm') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1Mb', 'm', True) == 1048576
    assert human_to_bytes('1Mb', 'm') == 1048576 * 8
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1Mb', 'K', True) == 1024 * 1024
    assert human_to_bytes('1Mb', 'K') == (1024 * 8) * 1024
    assert human_to_bytes('1Gb', isbits=True) == 1048576 * 1024

# Generated at 2022-06-12 23:49:56.676357
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 1]) == ['a', 1]
    assert lenient_lowercase(['A', 1]) == ['a', 1]
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase([]) == []



# Generated at 2022-06-12 23:50:03.738255
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 2, 'c']) == ['a', 2, 'c']
    assert lenient_lowercase(['A', 2, 'c']) == ['a', 2, 'c']
    assert lenient_lowercase(['a', 2, 'C']) == ['a', 2, 'c']



# Generated at 2022-06-12 23:50:15.857038
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test cases when unit is not passed but default is not
    assert human_to_bytes("10") == 10
    assert human_to_bytes("10") == human_to_bytes("10b")
    assert human_to_bytes("10", unit="b") == 10
    assert human_to_bytes("10", unit="B") == 10

    # Test cases when unit is not passed but default is passed
    assert human_to_bytes("10", default_unit='B') == 10
    assert human_to_bytes("10", default_unit='b') == 10
    assert human_to_bytes("10", default_unit='b') == human_to_bytes("10", default_unit='B')
    assert human_to_bytes("10", default_unit='Kb') == 10240

# Generated at 2022-06-12 23:50:20.508677
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['A', 1, 'B', 2]

    new_lst = lenient_lowercase(lst)
    print(new_lst)
    assert new_lst == ['a', 1, 'b', 2]



# Generated at 2022-06-12 23:50:25.470006
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Hello', 'WORLD']) == ['hello', 'world']
    assert lenient_lowercase(['Hello', 'Hello']) == ['hello', 'hello']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([1, 'Test', 3]) == [1, 'Test', 3]

# Generated at 2022-06-12 23:50:37.448527
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """
    The function is designed to throw ValueError exception
    in case of wrong input value. Exceptions will be catched
    and reported as test failures.
    """
    import unittest

    class TestFailure(Exception):
        def __init__(self, unit_test, error):
            Exception.__init__(self, None)
            self.error = error
            self.unit_test = unit_test


# Generated at 2022-06-12 23:50:41.181891
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Valid test data
    valid_list = [(['UNIT-TEST', 'UNIT-TEST1', 'UNIT-TEST2'], ['unit-test', 'unit-test1', 'unit-test2']),
                  (['UNIT-TEST', u'UNIT-TEST1', 'UNIT-TEST2'], ['unit-test', 'unit-test1', 'unit-test2']),
                  (['UNIT-TEST', 1, 'UNIT-TEST2'], ['unit-test', 1, 'unit-test2'])]
    # Invalid test data
    invalid_list = []
    # Iterate over all test data
    for test_list, exp_list in valid_list:
        # Call function under test
        result_list = lenient_lowercase(test_list)
        #

# Generated at 2022-06-12 23:50:50.586229
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB', isbits=True) == 8388608
    assert human_to_bytes('1Mb') == 8388608
    assert human_to_bytes('1Mb', isbits=True) == 8388608
    assert human_to_bytes('1M', default_unit='B') == 1048576
    assert human_to_bytes('1M', default_unit='b') == 8388608
    assert human_to_bytes('1Mb', default_unit='b') == 8388608

# Generated at 2022-06-12 23:50:54.828094
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1]) == [1]
    assert lenient_lowercase(['One']) == ['one']
    assert lenient_lowercase(['One', 1, 'two']) == ['one', 1, 'two']

# Generated at 2022-06-12 23:50:57.701435
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    ret_val = lenient_lowercase(['A', 1, 'C'])
    assert ret_val == ['a', 1, 'c']



# Generated at 2022-06-12 23:51:10.285644
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:20.888151
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit Tests for human_to_bytes() function."""

    # Basic test.
    result = human_to_bytes('1MB')
    assert result == 1048576, 'Test 1MB: %s' % result

    # Check if we can get some float values.
    result = human_to_bytes('7.5GB')
    assert result == int('8589934592'), 'Test 7.5GB: %s' % result

    # Check if we can get some float values.
    result = human_to_bytes('5.6TB')
    assert result == int('6291456000000'), 'Test 7.5GB: %s' % result

    # Check bit values.
    result = human_to_bytes('1Mb', isbits=True)
    assert result == 1048576, 'Test 1Mb: %s'

# Generated at 2022-06-12 23:51:28.794076
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('3') == 3
    assert human_to_bytes('3.1') == 3
    assert human_to_bytes('3.') == 3
    assert human_to_bytes('0x3') == 3
    assert human_to_bytes('0o3') == 3
    assert human_to_bytes('0b11') == 3
    assert human_to_bytes('0x3K') == 3072
    assert human_to_bytes('0x3KB') == 3072
    assert human_to_bytes('0x3Kb') == 3072
    assert human_to_bytes('0x3Kb', isbits=True) == 3072
    assert human_to_bytes('0x3K', isbits=True) == 3072
    assert human_to_bytes('3K') == 3072


# Generated at 2022-06-12 23:51:33.023795
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:42.285848
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # base byte test
    tests = {
        '1b': 1,
        '10B': 10,
        '1k': 1000,
        '1K': 1000,
        '1KB': 1000,
        '1KBb': ValueError,
        '1Kb': 8192,
        '1M': 1000000,
        '1Mb': 8 * 1000000,
        '1.5M': 1500000,
        '2.6G': 2600000000,
        '2.6Gb': 2600000000 * 8,
        '3T': 3000000000000,
        '3Tb': 3000000000000 * 8,
        '3Z': 30000000000000000000,
        '3Zb': 30000000000000000000 * 8,
    }


# Generated at 2022-06-12 23:51:54.005781
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1Gb') == 137438953472
    assert human_to_bytes('1Mb') == 134217728
    assert human_to_bytes('1Kb') == 131072
    assert human_to_bytes(1000, 'GB') == 1073741824
    assert human_to_bytes(1000, 'MB') == 1048576
    assert human_to_bytes(1000, 'KB') == 1024
    assert human_to_bytes(1000, 'Gb') == 137438953472
    assert human_to_bytes(1000, 'Mb') == 134217728
    assert human_

# Generated at 2022-06-12 23:52:00.321971
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test normal conversion to lowercase
    input_list = ['foo', 'Bar', 'baz']
    expected_list = ['foo', 'bar', 'baz']
    assert lenient_lowercase(input_list) == expected_list
    # Test pass through of non string items
    input_list = ['foo', 5, 'baz']
    expected_list = ['foo', 5, 'baz']
    assert lenient_lowercase(input_list) == expected_list
    # Test empty list
    input_list = []
    expected_list = []
    assert lenient_lowercase(input_list) == expected_list

# Generated at 2022-06-12 23:52:11.544026
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10 * 1024 * 1024
    assert human_to_bytes('10M', 'KB') == 10 * 1024
    assert human_to_bytes(10, 'M') == 10 * 1024 * 1024
    assert human_to_bytes('20G') == 20 * 1024 * 1024 * 1024
    assert human_to_bytes('10K') == 10 * 1024
    assert human_to_bytes(10, 'K') == 10 * 1024
    assert human_to_bytes('2Mb') == 2 * 1024 * 1024
    assert human_to_bytes('2Mb', isbits=True) == 2 * 1024 * 1024
    assert human_to_bytes('2Mb', 'Kb', isbits=True) == 2 * 1024

    # testing 'bytes' cases
    assert human_to_bytes('10B')

# Generated at 2022-06-12 23:52:14.655844
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['foo']) == ['foo']
    assert lenient_lowercase([None, 'foo']) == [None, 'foo']



# Generated at 2022-06-12 23:52:23.452806
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1Z') == 1180591620717411303424
    assert human_to_bytes('1Y') == 1208925819614629174706176
    # bit to byte conversions
    assert human_to_bytes('1b') == 1152921504606846976
    assert human_to_bytes

# Generated at 2022-06-12 23:52:32.929201
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_data = [
        {'name': 'a', 'value': 'A'},
        {'name': 'b', 'value': 'B'},
        {'name': 'empty_string', 'value': ''},
        {'name': 'dict', 'value': {'key': 'value'}},
        {'name': 'int', 'value': 1},
        {'name': 'lst', 'value': [1, 2, 'A']},
    ]

    for test in test_data:
        assert lenient_lowercase([test['value']])[0] == test['value'], '%s is not equal to %s' % (lenient_lowercase([test['value']])[0], test['value'])

# Generated at 2022-06-12 23:52:35.916985
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['AAA', 'bbb', {'C': 'c'}, 'ddd']) == ['aaa', 'bbb', {'C': 'c'}, 'ddd']



# Generated at 2022-06-12 23:52:39.988062
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert 1048576 == human_to_bytes('1MB', default_unit='B')
    assert 1048576 == human_to_bytes('1MB', default_unit=None)
    assert 1048576 == human_to_bytes('1M', default_unit='B')

    assert 2097152 == human_to_bytes('2MB', default_unit='B')
    assert 3145728 == human_to_bytes('3MB', default_unit='B')
    assert 4194304 == human_to_bytes('4MB', default_unit='B')
    assert 5242880 == human_to_bytes('5MB', default_unit='B')
    assert 6291456 == human_to_bytes('6MB', default_unit='B')

# Generated at 2022-06-12 23:52:46.879748
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    import pytest

    # Test that strings get lowercased
    assert lenient_lowercase(['STRING', '123']) == ['string', '123']

    # Test that non-strings are untouched
    assert lenient_lowercase([{'key': 'value'}, 123]) == [{'key': 'value'}, 123]

    # Test that non-string values passed in a list are untouched
    assert lenient_lowercase([[1, 2, 3], 123]) == [[1, 2, 3], 123]

    # Test that a non-string cannot be iterated over
    with pytest.raises(AttributeError):
        lenient_lowercase(123)


# Generated at 2022-06-12 23:52:57.525129
# Unit test for function human_to_bytes
def test_human_to_bytes():
    #
    # 1) Check all common cases:
    #
    human_to_bytes('1')  # 1 bytes
    human_to_bytes('1.2')  # 1 bytes
    human_to_bytes('1B')  # 1 bytes
    human_to_bytes('1b')  # 8 bits
    human_to_bytes('1.2b')  # 8 bits
    human_to_bytes('1K')  # 1024 bytes
    human_to_bytes('1Kb')  # 8192 bits
    human_to_bytes('1M')  # 1048576 bytes
    human_to_bytes('1Mb')  # 8388608 bits
    human_to_bytes('1G')  # 1073741824 bytes
    human_to_bytes('1Gb')  # 8589934592 bits
    human

# Generated at 2022-06-12 23:53:04.947907
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test bytes
    assert human_to_bytes('0') == 0
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1K') == SIZE_RANGES['K']
    assert human_to_bytes('1M') == SIZE_RANGES['M']
    assert human_to_bytes('1G') == SIZE_RANGES['G']
    assert human_to_bytes('1T') == SIZE_RANGES['T']
    assert human_to_bytes('1P') == SIZE_RANGES['P']
    assert human_to_bytes('1E') == SIZE_RANGES['E']

# Generated at 2022-06-12 23:53:16.656352
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1.1) == 1
    assert human_to_bytes(1, 'B') == 1
    assert human_to_bytes(1, 'b') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1B', isbits=True) == 1
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1KB') == 1000
    assert human_to_bytes('1KB', 'K') == 1000
    assert human_to_bytes('1kb', 'b') == 1000
    assert human_to_bytes('1kb', 'b', isbits=True) == 1000
    assert human

# Generated at 2022-06-12 23:53:24.882322
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:35.820595
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # convert from bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1.1B') == 1
    assert human_to_bytes('1.5B') == 2
    assert human_to_bytes('2B') == 2
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1TB') == 1099511627776
    assert human_to_bytes('1EB') == 1125899906842624
    assert human_to_bytes('1PB') == 1152921504606847000

# Generated at 2022-06-12 23:53:41.190268
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    args = {'group_name': 'Example', 'lowercase': 'lower', 'uppercase': 'UPPER', 'mixedcase': 'mIXED'}

    for k, v in iteritems(args):
        assert lenient_lowercase([k, v])[0] == k
        assert lenient_lowercase([k, v])[1].lower() == v.lower()



# Generated at 2022-06-12 23:53:59.066215
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('2') == 2
    assert human_to_bytes('0') == 0
    assert human_to_bytes('0K') == 0
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1024 ** 2
    assert human_to_bytes('1G') == 1024 ** 3
    assert human_to_bytes('1T') == 1024 ** 4
    assert human_to_bytes('1P') == 1024 ** 5
    assert human_to_bytes('1E') == 1024 ** 6
    assert human_to_bytes('1Z') == 1024 ** 7
    assert human_to_bytes('1Y') == 1024 ** 8
    assert human_to_bytes('0.5K') == 512
    assert human_

# Generated at 2022-06-12 23:54:09.134665
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:14.918501
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1, 'B') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10MB', default_unit='B') == 10485760
    assert human_to_bytes('10MB', 'B') == 10485760
    assert human_to_bytes(1, 'Y') == 1 << 80
    assert human_to_bytes(1, 'Z') == 1 << 70
    assert human_to_bytes(1, 'E') == 1 << 60
    assert human_to_bytes(1, 'P') == 1 << 50

# Generated at 2022-06-12 23:54:19.758499
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['str1', 'str2', 'str3']) == ['str1', 'str2', 'str3']
    assert lenient_lowercase(['str1', 'STR2', 'str3']) == ['str1', 'str2', 'str3']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase(['str1', 2, 'str3']) == ['str1', 2, 'str3']
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(None) == None

# Generated at 2022-06-12 23:54:26.310319
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1', 'B') == 1
    assert human_to_bytes('1', 'K') == human_to_bytes(1, 'K') == human_to_bytes(1, unit='K') == 1024
    assert human_to_bytes('-1', 'K') == -1 * human_to_bytes(1, 'K')
    assert human_to_bytes('0x10', 'K') == 16 * human_to_bytes(1, 'K')
    assert human_to_bytes('1k', 'K') == human_to_bytes(1, 'K')
    assert human_to_bytes('1M') == human_to_bytes(1, 'M') == human_to_bytes(1, unit='M') == human_to_bytes(1, 'Mb') == human_to_bytes

# Generated at 2022-06-12 23:54:34.334031
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a', 'b']) == ['a', 'b']
    assert lenient_lowercase(['A', 'b']) == ['a', 'b']
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase(['a', 2]) == ['a', 2]
    assert lenient_lowercase(['A', 2]) == ['a', 2]


# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:54:43.072775
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    class Class(object):
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return str(self.name)

        def __repr__(self):
            return repr(self.name)

    assert lenient_lowercase(['x', 'Y', 'z']) == ['x', 'y', 'z']
    assert lenient_lowercase(['X', Class('y'), 'Z', Class('w')]) == ['x', Class('y'), 'z', Class('w')]


# Generated at 2022-06-12 23:54:44.245973
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 1, 'C']) == ['a', 1, 'c']

# Generated at 2022-06-12 23:54:50.820493
# Unit test for function human_to_bytes
def test_human_to_bytes():
    test_data = [('10M', 10, 'M'),
                 ('10MB', 10, 'MB'),
                 ('10.0M', 10.0, 'M'),
                 ('10.25M', 10.25, 'M'),
                 ('10Mb', 10, 'Mb', True),
                 ('10MBb', 10, 'MBb', True)]

    for size, number, unit, isbits in test_data:
        assert human_to_bytes(number, unit, isbits=isbits) == human_to_bytes(size, isbits=isbits)

    try:
        # passing invalid unit
        human_to_bytes('10MX')
    except ValueError:
        pass
    else:
        raise AssertionError("human_to_bytes() did not raise an exception for invalid unit")


# Generated at 2022-06-12 23:54:54.680183
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase(['A', 1]) == ['a', 1]


# Generated at 2022-06-12 23:55:11.474528
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    name = [123, 'hELlo', 'world', 45.3, 'Bye']

    test_name = lenient_lowercase(name)

    assert test_name == [123, 'hello', 'world', 45.3, 'Bye']

# Generated at 2022-06-12 23:55:19.192363
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['TEST', 'TEST']) == ['test', 'test']
    assert lenient_lowercase(['TEST', 'test']) == ['test', 'test']
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase([1, [1, 2]]) == [1, [1, 2]]
    assert lenient_lowercase(['TEST', ['TEST', 'TEST']]) == ['test', ['test', 'test']]


# Generated at 2022-06-12 23:55:23.076063
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['FOO', 'bar']) == ['foo', 'bar']
    assert lenient_lowercase(['FOO', 5, 'bar']) == ['foo', 5, 'bar']


# Generated at 2022-06-12 23:55:30.722350
# Unit test for function human_to_bytes
def test_human_to_bytes():
    for unit, limit in iteritems(SIZE_RANGES):
        try:
            assert human_to_bytes(str(limit)) == limit
        except Exception as e:
            raise AssertionError("human_to_bytes() failed to convert %s: %s" % (limit, str(e)))
    try:
        assert human_to_bytes("123") == 123
    except Exception as e:
        raise AssertionError("human_to_bytes() failed to convert '123': %s" % str(e))

    # Test bits-to-bytes conversion

# Generated at 2022-06-12 23:55:34.308407
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['Hello', 'World', 'Of', 'Puppies', 1]
    assert(lenient_lowercase(test_list) == ['hello', 'world', 'of', 'puppies', 1])


# Generated at 2022-06-12 23:55:40.926675
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['hello', 'world', 'HELLO', 'WORLD', 0, 1, 2, (1, 2, 'hello')]
    result = lenient_lowercase(test_list)
    assert result == ['hello', 'world', 'HELLO', 'WORLD', 0, 1, 2, (1, 2, 'hello')]



# Generated at 2022-06-12 23:55:49.321288
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_data = [
        (
            ['ZONE1', 'zone2', 'zone3', 'zone4'],
            ['ZONE1', 'zone2', 'zone3', 'zone4']
        ),
        (
            [1, 2, 3, 4],
            [1, 2, 3, 4]
        ),
        (
            [1, 'zone1', 2, 'zone2', 3, 'zone3', 4, 'zone4'],
            [1, 'zone1', 2, 'zone2', 3, 'zone3', 4, 'zone4']
        ),
        (
            ['zone1', 'zone2', 'zone3', 'zone4', 1],
            ['zone1', 'zone2', 'zone3', 'zone4', 1]
        )
    ]


# Generated at 2022-06-12 23:55:56.069760
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', '1', 'C']) == ['a', '1', 'c']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([]) == []


# Generated at 2022-06-12 23:56:08.117096
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Some Unit tests
    tests = ['10GB', '500M', '10k', '500',
             '10.3M', '10.3Mb', '10.3Mbps', '10.3Gbps']
    answers = [10737418240, 524288000, 10240, 500,
               10485760, 1310720, 1310720, 13421772800]
    for test, answer in zip(tests, answers):
        try:
            assert human_to_bytes(test) == answer
        except Exception:
            raise AssertionError("human_to_bytes test failed on: %s." % test)
    print('human_to_bytes tests passed.')

    # Some Unit tests

# Generated at 2022-06-12 23:56:11.559023
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Foo', 'BAR', 'baz']) == ['foo', 'bar', 'baz']
    assert lenient_lowercase(['Foo', 12345, 'baz']) == ['foo', 12345, 'baz']

# Generated at 2022-06-12 23:56:34.656537
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:56:43.414948
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    testing function human_to_bytes() with valid and invalid strings and respective
    expected outcomes.
    '''

    success = 'SUCCESS: human_to_bytes() could convert this string to integer: %s'
    failure = 'FAILURE: expected ValueError exception has not been raised for: %s'

    test_string = '10M'
    expected = 10485760
    try:
        result = human_to_bytes(test_string)
        assert result == expected, "Test failed."
        print(success % test_string)
    except ValueError:
        print(failure % test_string)

    test_string = '5G'
    expected = 5368709120

# Generated at 2022-06-12 23:56:54.330559
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print('\nTesting function human_to_bytes():')
    # tests for Bytes
    test_data = [
        ('1', 1),
        ('1B', 1),
        ('1b', 1),
        ('1.0B', 1),
        ('1.1K', 1120),
        ('2M', 2097152),
        ('3G', 3221225472),
        ('4T', 4398046511104),
        ('5P', 562949953421312),
        ('6E', 690205205971968000),
        ('7Z', 81450678094346649600),
        ('8Y', 94143178827022515200000),
    ]

# Generated at 2022-06-12 23:57:01.622510
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['aBc', 'def', 'ghI', 1, 2, 3]) == ['abc', 'def', 'ghi', 1, 2, 3]


# Unit tests for functions human_to_bytes. When any of the unit tests fails, the test runner will dump the
# full stack trace, which is useful if you are debugging.

# All unit tests are disabled by default. To enable a particular test, change the "False" to "True".

# When a test is failing, you can use the script below to get more detailed debugging information:
# PYTHONPATH=./ test/utils/human_to_bytes_test.py -v


# Generated at 2022-06-12 23:57:08.539377
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('20G') == 21474836480
    assert human_to_bytes('30T') == 343597383680
    assert human_to_bytes('42P') == 5629499534213120
    assert human_to_bytes('1337P') == 17358799742000005376
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10', default_unit='B') == 10
    assert human_to_bytes('10', default_unit='b') == 10
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760

# Generated at 2022-06-12 23:57:18.089431
# Unit test for function human_to_bytes
def test_human_to_bytes():

    # test convert bytes from a human-readable format to integer
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1MBb') == 1048576
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10.5') == 10
    assert human_to_bytes('10.6') == 11
    assert human_to_bytes('.6') == 1
    assert human_to_bytes('10.6B') == 10
    assert human_to_bytes('10.6b') == 10
    assert human_to_bytes('10.6 b') == 10

# Generated at 2022-06-12 23:57:23.704098
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = lenient_lowercase(["ABC", 1, "DEF"])
    assert lst == ["abc", 1, "def"]
    lst = lenient_lowercase(["ABC", "DÉF"])
    assert lst == ["abc", "déf"]



# Generated at 2022-06-12 23:57:30.510154
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['foo', 'bar', 'baz']) == ['foo', 'bar', 'baz']
    assert lenient_lowercase(['FOO', 'BAR', 'BAZ']) == ['foo', 'bar', 'baz']
    assert lenient_lowercase(['foo', 'bar', 'baz', 10, 20, 30]) == ['foo', 'bar', 'baz', 10, 20, 30]
    assert lenient_lowercase(('foo', 'bar', 'baz')) == ['foo', 'bar', 'baz']
    assert lenient_lowercase(('FOO', 'BAR', 'BAZ')) == ['foo', 'bar', 'baz']

# Generated at 2022-06-12 23:57:40.590720
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('2M') == 2097152
    assert human_to_bytes('2.4M') == 2490368
    assert human_to_bytes('1.1M') == 1179648
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('85.0M') == 8912896
    assert human_to_bytes('10.0M') == 10485760
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('10.5G') == 11274289152
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes

# Generated at 2022-06-12 23:57:42.904134
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A1', 'B2']) == ['a1', 'b2']
    assert lenient_lowercase(['A1', 2]) == ['a1', 2]

# Generated at 2022-06-12 23:58:07.799070
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Lowercase a valid list
    test_list = ['ONE', 'TWO', 'THREE']
    ret = lenient_lowercase(test_list)
    assert ret == ['one', 'two', 'three']
    # Lowercase a valid list containing non-string objects
    test_list = ['ONE', 2, [], {}, {'a': 'b'}, 'THREE']
    lenient_lowercase(test_list)
    ret = lenient_lowercase(test_list)
    assert ret == ['one', 2, [], {}, {'a': 'b'}, 'THREE']
    # Lowercase a non-list
    test_obj = 'TEST'
    ret = lenient_lowercase(test_obj)
    assert ret == 'test'

# Generated at 2022-06-12 23:58:10.132330
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    input_list = ['A', 'B', 1]
    output_list = ['a', 'b', 1]
    assert lenient_lowercase(input_list) == output_list


# Generated at 2022-06-12 23:58:13.427456
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b']) == ['a', 'b']
    assert lenient_lowercase(['a', 3]) == ['a', 3]
    assert lenient_lowercase([['a', 3]]) == [['a', 3]]


# Generated at 2022-06-12 23:58:19.254353
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Yes', 'No', 'Maybe']) == ['yes', 'no', 'maybe']
    assert lenient_lowercase(['True', 'False', 'Unknown']) == ['true', 'false', 'unknown']
    assert lenient_lowercase(['Yes', False, 'Unknown']) == ['yes', False, 'unknown']



# Generated at 2022-06-12 23:58:26.699474
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10m') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB') == human_to_bytes('1M', 'B')
    assert human_to_bytes('1MB') == human_to_bytes(1, 'MB')
    assert human_to_bytes('1Mb', isbits=True) == human_to_bytes('1M', 'b', isbits=True)

# Generated at 2022-06-12 23:58:31.575149
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a'] == lenient_lowercase(['a'])
    assert ['a', 1] == lenient_lowercase(['a', 1])
    assert ['a', 1, 'b'] == lenient_lowercase(['A', 1, 'B'])



# Generated at 2022-06-12 23:58:33.549819
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test that lenient_lowercase() encodes strings to lowercase
    assert lenient_lowercase(['aBc', 123]) == ['abc', 123]