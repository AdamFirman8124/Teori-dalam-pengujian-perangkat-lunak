

# Generated at 2022-06-12 23:48:46.316695
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['abc', 'xyz']) == ['abc', 'xyz']
    assert lenient_lowercase(['abc', 1, 2, 3]) == ['abc', 1, 2, 3]



# Generated at 2022-06-12 23:48:55.701301
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

    # First test data - contains value, unit, expected result, isbits indicator

# Generated at 2022-06-12 23:49:06.624289
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Test for human_to_bytes functions.

    If the values do not match, it raises an AssertionError.
    """
    # check bytes
    assert human_to_bytes(10) == 10
    assert human_to_bytes(10.0) == 10
    assert human_to_bytes('10.0B') == 10
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10.0') == 10
    assert human_to_bytes('10.5B') == 11
    assert human_to_bytes('10.5') == 11
    assert human_to_bytes('10.0B', default_unit='B') == 10
    assert human_to_bytes('10.0', default_unit='B') == 10
    assert human_to_bytes('10.0KB') == 10240

# Generated at 2022-06-12 23:49:09.265609
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    result = lenient_lowercase([1, 'SOMETHING', None, 'SOMETHING', 'else'])
    assert result == [1, 'something', None, 'something', 'else']

# Unit tests for function human_bytes_to_bytes

# Generated at 2022-06-12 23:49:14.726048
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_cases = [
        (['a', 'b', 2, 3], ['a', 'b', 2, 3]),
        ([['a', 'b'], ['c', 'd']], [['a', 'b'], ['c', 'd']]),
        ([[2, 3], [5, 6]], [[2, 3], [5, 6]]),
        ([['a', 'b', 2], [3, 'C', 4]], [['a', 'b', 2], [3, 'C', 4]]),
    ]
    for test_case in test_cases:
        assert lenient_lowercase(test_case[0]) == test_case[1]


# Generated at 2022-06-12 23:49:21.589680
# Unit test for function human_to_bytes
def test_human_to_bytes():
    def assert_conversion(expected_value, user_input, default_unit=None, isbits=False):
        result = human_to_bytes(user_input, default_unit, isbits)
        assert result == expected_value, "Unexpected result, got %s instead of %s for input %s" % (result, expected_value, user_input)

    assert_conversion(42, "42", default_unit='B')
    assert_conversion(42, "42", default_unit='b')
    assert_conversion(42, "42", default_unit='X')

    assert_conversion(42, "42B")
    assert_conversion(42, "42b", isbits=True)
    assert_conversion(42, "42X")

    assert_conversion(42, "42 B")

# Generated at 2022-06-12 23:49:32.402755
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert 131072 == human_to_bytes('128K')
    assert 131072 == human_to_bytes('128k')
    assert 131072 == human_to_bytes('128kB')
    assert 131072 == human_to_bytes('128kb')

    assert 1048576 == human_to_bytes('1M')
    assert 1048576 == human_to_bytes('1Mb')
    assert 1048576 == human_to_bytes('1MB')
    assert 1048576 == human_to_bytes('1Mb', isbits=True)

    assert 1073741824 == human_to_bytes('1G')
    assert 1073741824 == human_to_bytes('1Gb', isbits=True)
    assert 1073741824 == human_to_bytes('1GB')


# Generated at 2022-06-12 23:49:39.936015
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lenient_lowercase(['ABC', 'def']) == ['abc', 'def']
    lenient_lowercase(['ABC', 7]) == ['abc', 7]
    lenient_lowercase(['ABC', None]) == ['abc', None]
    lenient_lowercase(['ABC', {}]) == ['abc', {}]
    lenient_lowercase(['ABC', []]) == ['abc', []]

# Generated at 2022-06-12 23:49:42.499508
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a','B','c']) == ['a','B','c']


# Generated at 2022-06-12 23:49:52.588701
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(10, unit='B') == '10.00 Bytes'
    assert bytes_to_human(4, 'g') == '0.00 GB'
    assert bytes_to_human(3000000, unit='m') == '3.00 MB'
    assert bytes_to_human(1, unit='m') == '0.00 MB'
    assert bytes_to_human(2 ** 20, unit='M') == '1.00 MB'
    assert bytes_to_human(2 ** 20 * 1000, unit='M') == '1000.00 MB'
    assert bytes_to_human(2 ** 20 * 2000, unit='M') == '2000.00 MB'

# Generated at 2022-06-12 23:50:05.341720
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:50:15.958166
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    values = ['abc', 'xyz', '123', 123]
    expected_values = ['abc', 'xyz', '123', 123]
    assert expected_values == lenient_lowercase(values)

    mixed_values = ['abc', 'xyz', 123, '123']
    assert mixed_values == lenient_lowercase(mixed_values)

    mixed_values = ['abc', 123, 'xyz', '123']
    assert mixed_values == lenient_lowercase(mixed_values)

    mixed_values = [123, 'abc', 'xyz', '123']
    assert mixed_values == lenient_lowercase(mixed_values)


# Generated at 2022-06-12 23:50:27.119526
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760, "Test '10M' - Error in human_to_bytes()"
    assert human_to_bytes('10MB') == 10485760, "Test '10MB' - Error in human_to_bytes()"
    assert human_to_bytes('10m') == 1048576, "Test '10m' - Error in human_to_bytes()"
    assert human_to_bytes('10mb') == 1048576, "Test '10mb' - Error in human_to_bytes()"
    assert human_to_bytes(10, unit='m') == 1048576, "Test '10 m' - Error in human_to_bytes()"

# Generated at 2022-06-12 23:50:39.528309
# Unit test for function human_to_bytes
def test_human_to_bytes():
    number_with_unit = '10M'
    byte_unit = 'B'
    bit_unit = 'b'

    # no unit passed / number is int
    assert human_to_bytes(10) == 10
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10', isbits=True) == 10
    assert human_to_bytes('10', unit='K') == 10240
    assert human_to_bytes('10', unit='K', isbits=True) == 10240
    # no unit passed / number is float
    assert human_to_bytes('10.1') == 10
    assert human_to_bytes('10.1', isbits=True) == 10
    assert human_to_bytes('10.1', unit='K') == 10240

# Generated at 2022-06-12 23:50:48.752901
# Unit test for function human_to_bytes
def test_human_to_bytes():
    test = [('1TB', 1 * SIZE_RANGES['T']), ('0.5K', 512), ('2Mb', 2 * SIZE_RANGES['M'] / 8), ('1', 1), ('1.5', 1.5), ('B', 1), ('1b', 1.0/8)]
    for val, expected in test:
        result = human_to_bytes(val)
        assert result == expected, "%s returned %d instead of %d" % (val, result, expected)

if __name__ == '__main__':
    test_human_to_bytes()

# Generated at 2022-06-12 23:51:00.205341
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1KB') == 1000
    assert human_to_bytes('1MB') == 1000**2
    assert human_to_bytes('1GB') == 1000**3
    assert human_to_bytes('1TB') == 1000**4
    assert human_to_bytes('1PB') == 1000**5
    assert human_to_bytes('1EB') == 1000**6
    assert human_to_bytes('1ZB') == 1000**7
    assert human_to_bytes('1YB') == 1000**8

    # Test bits
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1Kb', isbits=True) == 1000

# Generated at 2022-06-12 23:51:07.795674
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:12.979219
# Unit test for function human_to_bytes
def test_human_to_bytes():
    if human_to_bytes('10K') != 10240:
        raise ValueError("human_to_bytes() failed to convert 10K to 10240")

    if human_to_bytes('10MB') != 10485760:
        raise ValueError("human_to_bytes() failed to convert 10MB to 10485760")

    if human_to_bytes('10Mb', isbits=True) != 10485760:
        raise ValueError("human_to_bytes() failed to convert 10Mb to 10485760")

    if human_to_bytes('10Kb', isbits=True) != 102400:
        raise ValueError("human_to_bytes() failed to convert 10Kb to 102400")


# Generated at 2022-06-12 23:51:18.066577
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase('abc') == 'abc'
    assert lenient_lowercase(['abc']) == 'abc'
    assert lenient_lowercase(['abc', 1, 'xyz']) == ['abc', 1, 'xyz']
    assert lenient_lowercase(['abc', 1, 'XYZ']) == ['abc', 1, 'xyz']

# Generated at 2022-06-12 23:51:22.471247
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['foo', 'bar'] == lenient_lowercase(['Foo', 'bar'])
    assert [1, 2, 3] == lenient_lowercase([1, 2, 3])
    assert ['foo', 'bar', 1, 2, 3] == lenient_lowercase(['Foo', 'bar', 1, 2, 3])


# Generated at 2022-06-12 23:51:33.783479
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(0) == '0.00 Bytes'
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(10) == '10.00 Bytes'
    assert bytes_to_human(100) == '100.00 Bytes'
    assert bytes_to_human(1000) == '1.00 KB'
    assert bytes_to_human(10000) == '9.77 KB'
    assert bytes_to_human(100000) == '97.66 KB'
    assert bytes_to_human(1000000) == '1.00 MB'
    assert bytes_to_human(10000000) == '9.54 MB'
    assert bytes_to_human(100000000) == '95.37 MB'

# Generated at 2022-06-12 23:51:36.211194
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 1, u'B', 'C']) == ['a', 1, u'b', 'c']


# Generated at 2022-06-12 23:51:45.447069
# Unit test for function human_to_bytes
def test_human_to_bytes():
    test_data_valid_inputs = [
        ("10", "10", None),
        ("10M", "10485760", None),
        ("1M", "1048576", None),
        ("10G", "10737418240", None),
        ("1G", "1073741824", None),
        ("1Kb", "1024", True),
        ("1234b", "1234", True),
    ]

    test_data_invalid_inputs = [
        "10MB",
        "10Kb",
        "1M",
        "1Kb",
    ]

    for test_input, expected, is_bits in test_data_valid_inputs:
        actual = human_to_bytes(test_input, isbits=is_bits)

# Generated at 2022-06-12 23:51:53.671186
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A']) == ['a']
    assert lenient_lowercase(['A', 1]) == ['a', 1]
    assert lenient_lowercase(['A', 1, 'B']) == ['a', 1, 'b']
    assert lenient_lowercase(['A', 1, 'B', 'C']) == ['a', 1, 'b', 'c']
    assert lenient_lowercase(['A', 1, 'B', 'C', 'D']) == ['a', 1, 'b', 'c', 'd']

# Generated at 2022-06-12 23:51:57.537100
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, ['a', 'B', 'c']]) == [1, ['a', 'B', 'c']]


# Generated at 2022-06-12 23:52:04.027398
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Create a list of mixed objects, strings, and bools
    test_list = [False, "apple", "banana", 34, True, "Grape", None]
    # Run the lenient_lowercase function against the list
    lowered = lenient_lowercase(test_list)
    # Check for correct return values
    assert lowered == [False, "apple", "banana", 34, True, "grape", None]

# Generated at 2022-06-12 23:52:07.048123
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Lowercase a list
    assert ['a', 'b', 'c'] == lenient_lowercase(['A', 'B', 'C'])

    # Leave non-str values unchanged
    assert ['a', 'b', None, 'd'] == lenient_lowercase(['A', 'B', None, 'D'])



# Generated at 2022-06-12 23:52:17.295772
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    '''
    Test for lenient_lowercase function
    '''
    original_list = ["", "1", "1.2", "a", "ab", "A", "Aa", "B", "b", "b1", "b2.2", "test", "TEST", "TeSt", "aBcD", 1, 1.2, None]
    expected_list = ["", "1", "1.2", "a", "ab", "A", "Aa", "B", "b", "b1", "b2.2", "test", "test" , "test", "abcd", 1, 1.2, None]

    assert lenient_lowercase(original_list) == expected_list


# Generated at 2022-06-12 23:52:26.694092
# Unit test for function bytes_to_human

# Generated at 2022-06-12 23:52:29.580266
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [['str1', 'str2'], ['str1', 5]]
    expected_result = [['str1', 'str2'], ['str1', 5]]

    assert (expected_result == lenient_lowercase(test_list))



# Generated at 2022-06-12 23:52:44.344172
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(10) == 10
    assert human_to_bytes(10, "B") == 10
    assert human_to_bytes(10, "B", True) == 10
    assert human_to_bytes(1, "Mb", True) == 1048576
    assert human_to_bytes(2, "M", False) == 2097152
    assert human_to_bytes(1, "b", True) == 1
    assert human_to_bytes(10, "T", True) == 1125899906842624
    assert human_to_bytes(1, "K") == 1024
    assert human_to_bytes(10, "KB") == 10240
    assert human_to_bytes(10, "Kb", True) == 10240

# Generated at 2022-06-12 23:52:49.667522
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert not lenient_lowercase(['ABC', 'C', 'def', ['g']]) == ['abc', 'c', 'def', ['g']],\
           ('Error: ', lenient_lowercase(['ABC', 'C', 'def', ['g']]), ['ABC', 'C', 'def', ['g']])


# Generated at 2022-06-12 23:52:59.137402
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:06.694584
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import unittest

    class TestSequenceFunctions(unittest.TestCase):

        def test_upper(self):
            # Test binary number to bytes with different unit types
            self.assertEqual(human_to_bytes(2048, 'K'), 2097152)
            self.assertEqual(human_to_bytes(2048, 'Kb'), 262144)
            self.assertEqual(human_to_bytes(2048, 'KB'), 2097152)
            self.assertEqual(human_to_bytes(2048, 'Kb'), 262144)
            self.assertEqual(human_to_bytes(2048, 'Mb'), 268435456)
            self.assertEqual(human_to_bytes(2048, 'MB'), 2147483648)

# Generated at 2022-06-12 23:53:18.379097
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:21.673010
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    x = [1, 'aBc', [3], 4, '5', 'D']
    assert lenient_lowercase(x) == [1, 'abc', [3], 4, '5', 'D'], lenient_lowercase(x)



# Generated at 2022-06-12 23:53:25.276813
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['aaa', 'BBB', 'ccc', 123]) == ['aaa', 'BBB', 'ccc', 123]


# Unit tests for function human_to_bytes()
#
# Normal cases

# Generated at 2022-06-12 23:53:36.641339
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Verify the function can take numbers and turn them into bytes
    assert human_to_bytes(0) == 0
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1024) == 1024
    assert human_to_bytes(1048576) == 1048576

    # Verify the function can take numbers with units and turn them into bytes
    assert human_to_bytes('0') == 0
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('0KB') == 0
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('0MB') == 0
    assert human_to_bytes('1MB') == 1048576

    # Verify the function can take numbers and units and turn them into bytes


# Generated at 2022-06-12 23:53:45.957108
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('12345') == 12345
    assert human_to_bytes('0') == 0
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10M', default_unit='B') == 10485760
    assert human_to_bytes('10', default_unit='B') == 10
    assert human_to_bytes('10', default_unit='M') == 10485760
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10b', isbits=True) == 10
    assert human_to_bytes('10b', default_unit='b', isbits=True) == 10
    assert human_to_bytes('1MB') == 1048576

# Generated at 2022-06-12 23:53:56.938254
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('100M') == 104857600
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('100G') == 107374182400
    assert human_to_bytes('1TB') == 1099511627776
    assert human_to_bytes('10kb') == 10240
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('1MB', 'kb') == 1024
    assert human_to_bytes('1MB', 'kb', True) == 1024 * 8
    assert human_to_bytes('1MB', 'Kb', True) == 1024 * 1024
    assert human_to_bytes(10, 'MB') == 10485760

# Generated at 2022-06-12 23:54:12.017809
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M')
    assert human_to_bytes(10, 'g') == 10
    assert human_to_bytes('2M') == 2 * 1024 * 1024
    assert human_to_bytes('2Mb') == 2 * 1024 * 1024
    assert human_to_bytes('2MB') == 2 * 1024 * 1024
    assert human_to_bytes('2Mb', isbits=True) == 2 * 1024 * 1024
    assert human_to_bytes('2MB', isbits=True) == 2 * 1024 * 1024
    assert human_to_bytes('2.5Mb', isbits=True) == int(2.5 * 1024 * 1024)
    assert human_to_bytes('2.5Mb') == int(2.5 * 1024 * 1024)


# Generated at 2022-06-12 23:54:22.269201
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    """
    Unit test to verify that the lenient lowercase function works
    """

    lst = []
    assert len(lst) == len(lenient_lowercase(lst))

    lst = ['hello', 'world', 'this', 'is', 'me']
    assert len(lst) == len(lenient_lowercase(lst))

    lst = [None, 5, 'hello']
    assert len(lst) == len(lenient_lowercase(lst))

    for i in range(0, len(lst)):
        assert lst[i] == lenient_lowercase(lst)[i]

    lst = [{'key': 'value'}]
    assert len(lst) == len(lenient_lowercase(lst))

# Generated at 2022-06-12 23:54:27.789863
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    input_list = ['A', 'B', 1, [], {}, 'C']
    expected = ['A', 'B', 1, [], {}, 'C']
    output = lenient_lowercase(input_list)
    assert len(output) == len(expected)
    for index in range(0, len(output)):
        assert output[index] == expected[index]

# Generated at 2022-06-12 23:54:37.322218
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a', 'b', 'c'] == lenient_lowercase(['a', 'B', 'C'])
    assert [1, 'b', 'c'] == lenient_lowercase([1, 'B', 'C'])
    assert {'a': 1, 'b': 2} == lenient_lowercase({'a': 1, 'B': 2})
    assert {'a': 1, 2: 'b'} == lenient_lowercase({'a': 1, 2: 'B'})
    # List of mixed types
    assert ['a', 'b', 2, 3] == lenient_lowercase(['a', 'B', 2, 3])
    # Mixed type of dict keys
    assert {'a': 1, 2: 'b'} == lenient_lowercase({'a': 1, 2: 'B'})

# Generated at 2022-06-12 23:54:46.829143
# Unit test for function bytes_to_human
def test_bytes_to_human():

    assert(bytes_to_human(0) == '0 Bytes')
    assert(bytes_to_human(1024) == '1.00 KB')
    assert(bytes_to_human(1024 * 1024) == '1.00 MB')
    assert(bytes_to_human(1024 * 1024 * 1024) == '1.00 GB')
    assert(bytes_to_human(1024 * 1024 * 1024 * 1024) == '1.00 TB')

    assert(bytes_to_human(0, isbits=True) == '0 bits')
    assert(bytes_to_human(1024, isbits=True) == '8.00 Kb')
    assert(bytes_to_human(1024 * 1024, isbits=True) == '8.00 Mb')

# Generated at 2022-06-12 23:54:59.258925
# Unit test for function bytes_to_human
def test_bytes_to_human():
    # Testing with one decimal place
    assert bytes_to_human(0) == '0 Bytes'
    assert bytes_to_human(0, unit='B') == '0 Bytes'
    assert bytes_to_human(1, unit='B') == '1 Bytes'
    assert bytes_to_human(5, unit='B') == '5 Bytes'
    assert bytes_to_human(5, unit='b') == '5 bits'
    assert bytes_to_human(5, isbits=True, unit='b') == '5 bits'
    assert bytes_to_human(5, isbits=True, unit='bit') == '5 bits'
    assert bytes_to_human(1024, unit='B') == '1.00 KBytes'

# Generated at 2022-06-12 23:55:09.560600
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Test the conversion of the string in human readable format to integer.

    A list of strings in a human readable format to be tested.
    SIZE_RANGES - the dictionary with the suffixes and the corresponding value.

    """

# Generated at 2022-06-12 23:55:20.381808
# Unit test for function bytes_to_human
def test_bytes_to_human():
    for size, expected_result in (
            (1, '1 Bytes'),
            (1 << 10, '1.00 KB'),
            (1 << 20, '1.00 MB'),
            (1 << 30, '1.00 GB'),
            (1 << 40, '1.00 TB'),
            (1 << 50, '1.00 PB'),
            (1 << 60, '1.00 EB'),
            (1 << 70, '1.00 ZB'),
            (1 << 80, '1.00 YB'),
            (1 << 90, '1024.00 YB'),
    ):
        assert bytes_to_human(size) == expected_result
        assert bytes_to_human(size, unit='b') == '8.00 b'

# Generated at 2022-06-12 23:55:29.262008
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(0) == 0, 'Failed conversion of 0'
    assert human_to_bytes(10) == 10, 'Failed conversion of 10'
    assert human_to_bytes('0') == 0, 'Failed conversion of 0'
    assert human_to_bytes('10') == 10, 'Failed conversion of 10'
    assert human_to_bytes('0B') == 0, 'Failed conversion of 0B'
    assert human_to_bytes('1B') == 1, 'Failed conversion of 1B'
    assert human_to_bytes('10B') == 10, 'Failed conversion of 10B'
    assert human_to_bytes('0b') == 0, 'Failed conversion of 0b'
    assert human_to_bytes('1b') == 1, 'Failed conversion of 1b'


# Generated at 2022-06-12 23:55:33.632374
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['HEllO', 1, 'world', None, ['a', 'b'], ('A', 1), '1']
    expected_result = ['hello', 1, 'world', None, ['a', 'b'], ('A', 1), '1']
    assert lenient_lowercase(test_list) == expected_result


# Generated at 2022-06-12 23:55:41.473205
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [1, "lower", "Upper", "MiXeD", 3, "MiXeD"]

    assert lenient_lowercase(test_list) == [1, "lower", "upper", "mixed", 3, "mixed"]



# Generated at 2022-06-12 23:55:49.758178
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' test string - integer conversion '''
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1mb') == 1048576
    assert human_to_bytes('1 Mb') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1 MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1mb', isbits=True) == 1048576
    assert human_to_bytes('1 Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=True) == 1048576
    assert human_to_bytes('1 MB', isbits=True) == 1048576
   

# Generated at 2022-06-12 23:55:52.898673
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'Aa', 'aa', 'BB', [1,2]]) == [1, 'aa', 'aa', 'bb', [1,2]]


# Generated at 2022-06-12 23:56:04.999324
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1Kb') == 128
    assert human_to_bytes('1Mb') == 131072
    assert human_to_bytes('1Gb') == 134217728
    assert human_to_bytes('1TB') == 1099511627776

    assert human_to_bytes('0.5KB') == 512
    assert human_to_bytes('0.5MB') == 524288
    assert human_to_bytes('0.5GB') == 536870912
    assert human_to_bytes('0.5TB') == 549755813888


# Generated at 2022-06-12 23:56:07.887782
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    actual_output = lenient_lowercase(['ANZ', 'KKK', 'ABC', 123, 6666])
    assert actual_output == ['anz', 'kkk', 'abc', 123, 6666]



# Generated at 2022-06-12 23:56:09.996942
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert (['a', 'bb', 'ccc'] == lenient_lowercase(['a', 'bb', 'ccc']))



# Generated at 2022-06-12 23:56:13.801395
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase(['A', 'B', ['A']]) == ['a', 'b', ['A']]
    assert lenient_lowercase(['A', 'B', None]) == ['a', 'b', None]

# Generated at 2022-06-12 23:56:23.810431
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test negative values
    assert human_to_bytes('-1M') == -1048576
    assert human_to_bytes('-1Mb', isbits=True) == -1048576
    # test with defaults
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1', 'M') == 1048576
    assert human_to_bytes('1', 'Mb', isbits=True) == 1048576

    # test with bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1B', 'b', isbits=True) == 8
    assert human_to_bytes('1b', 'B') == 1/8.0

# Generated at 2022-06-12 23:56:34.149927
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:56:43.076593
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('0.1') == 0
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('1K', isbits=True) == 1 * (1 << 10)
    assert human_to_bytes('1K') == 1 << 10
    assert human_to_bytes('1kj') == 1 << 10
    assert human_to_bytes('10K') == 10 * (1 << 10)
    assert human_to_bytes('1M') == 1 << 20
    assert human_to_bytes('10M') == 10 * (1 << 20)

# Generated at 2022-06-12 23:56:54.547123
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    x = [1, "abcd", "ABCD", "gHi", "HELLO"]
    results = [1, "abcd", "abcd", "ghi", "hello"]
    assert lenient_lowercase(x) == results

# Generated at 2022-06-12 23:57:02.679172
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:13.957267
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # ex 1
    assert human_to_bytes('1') == 1, 'human_to_bytes() failed to convert 1.'
    assert human_to_bytes('1B') == 1, 'human_to_bytes() failed to convert 1.'
    assert human_to_bytes('1b') == 1, 'human_to_bytes() failed to convert 1.'
    assert human_to_bytes(1) == 1, 'human_to_bytes() failed to convert 1.'
    assert human_to_bytes(1, 'b', True) == 8, 'human_to_bytes() failed to convert 1.'
    assert human_to_bytes(1, 'b', False) == 1, 'human_to_bytes() failed to convert 1.'

# Generated at 2022-06-12 23:57:21.775514
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Tests for human_to_bytes function
    1. Returns integer when number is passed without unit
    2. Returns integer when number with unit is passed
    3. Returns float when float number is passed with unit
    4. Throws ValueError when string is passed
    5. Throws ValueError when non-digit/non-decimal/non-alphabet character is passed
    6. Throws ValueError when no unit present in the given number
    7. Throws ValueError when unit is not recognized
    '''
    assert human_to_bytes('10') == 10, "Test case 1 failed, expected 10, got {}".format(human_to_bytes('10'))
    assert human_to_bytes('10K') == 10240, "Test case 2 failed, expected 10240, got {}".format(human_to_bytes('10K'))

# Generated at 2022-06-12 23:57:25.803051
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, 2, 3, 'A', 'b', 'C']
    assert lenient_lowercase(lst) == [1, 2, 3, 'a', 'b', 'c']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([1, 2, 3, 'a']) == [1, 2, 3, 'a']



# Generated at 2022-06-12 23:57:33.165184
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['TEST', 'TEST', 'TEST']) == ['test', 'test', 'test']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase(['TEST', 1, 'TEST']) == ['test', 1, 'test']

# Generated at 2022-06-12 23:57:41.701377
# Unit test for function human_to_bytes
def test_human_to_bytes():
    cases = [
        ('1', 1),
        ('1B', 1),
        ('1b', 1),
        ('1b', 1),
        ('1KB', 1024),
        ('1KB', 1024),
        ('1Mb', 1048576),
        ('1MB', 1048576),
    ]

# Generated at 2022-06-12 23:57:47.314479
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 'B', 'c', 0]) == ['a', 'b', 'c', 0]
    assert lenient_lowercase(['A', 'B', 'C', 0]) == ['a', 'b', 'c', 0]
    assert lenient_lowercase(['a', 'B', 'c', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]
    assert lenient_lowercase(['a', 'B', 'c', 1, 2, 3, 'D']) == ['a', 'b', 'c', 1, 2, 3, 'd']

# Generated at 2022-06-12 23:57:55.244210
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test positive cases
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('2.5K') == 2560
    assert human_to_bytes('3.1M') == 3250000
    assert human_to_bytes('1.5G') == 1610612736
    assert human_to_bytes('2.5T') == 274877906944
    assert human_to_bytes('2.5P') == 281474976710656
    assert human_to_bytes('2.5E') == 295147905179352825856
    assert human_to_bytes('2.5Z') == 316912650057057350374175801344
    assert human_to_bytes('2.5Y') == 3307880098716274220380404723622208

    #

# Generated at 2022-06-12 23:58:07.921789
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(1, default_unit='K', isbits=False) == 1024
    assert human_to_bytes(1, default_unit='K', isbits=True) == 1024
    assert human_to_bytes('1KB', isbits=False) == 1024
    assert human_to_bytes('1KB', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=False) == 1048576
    assert human_to_bytes('1K', isbits=False) == 1024
    assert human_to_bytes('1M', isbits=False) == 1048576
    assert human_to_bytes('1G', isbits=False) == 1073741824

# Generated at 2022-06-12 23:58:24.892720
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes(1.5) == 1
    assert human_to_bytes('1.8') == 1
    assert human_to_bytes(1.8) == 1
    assert human_to_bytes('2') == 2
    assert human_to_bytes(2) == 2
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes(2, 'K') == 2048
    assert human_to_bytes('2Kb') == 2048
    assert human_to_bytes(2, 'Kb', isbits=True) == 2048
    assert human_to_bytes('2M') == 2097152
    assert human_

# Generated at 2022-06-12 23:58:30.965282
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(('A', 'b', 'C')) == ('a', 'b', 'c')
    assert lenient_lowercase((2, 3, 4)) == (2, 3, 4)
    assert lenient_lowercase(('A', 2, u'C')) == ('a', 2, u'c')



# Generated at 2022-06-12 23:58:39.006419
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # validate bytes
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1024  # uppercase
    assert human_to_bytes('1k', 'B') == 1024  # default unit
    assert human_to_bytes('1k', default_unit='B') == 1024  # default unit
    assert human_to_bytes('1', 'k') == 1024

    # validate bits
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1Kb', isbits=True) == 1024