

# Generated at 2022-06-12 23:48:42.831677
# Unit test for function human_to_bytes
def test_human_to_bytes():
    human_to_bytes(None, None)

# Function bytes_to_human is used in uri module to convert bytes to human readable format.

# Generated at 2022-06-12 23:48:52.762654
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:03.236277
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test basic functionality
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2k') == 2048
    assert human_to_bytes('2KB') == 2048
    assert human_to_bytes('2kb') == 2048
    assert human_to_bytes('2Kb') == 2048
    assert human_to_bytes('2kB') == 2048
    assert human_to_bytes('2KiB') == 2048
    assert human_to_bytes('2 KiB') == 2048

    # Test type conversion
    assert human_to_bytes(2) == 2
    assert human_to_bytes(2.1) == 2

    # test negative numbers
    assert human_to_bytes('-1K') == -1024
    assert human_to_bytes('-2MB') == -2097152

    # test

# Generated at 2022-06-12 23:49:05.737165
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['One', 1, 'Two', 2]) == ['one', 1, 'two', 2]



# Generated at 2022-06-12 23:49:13.079152
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import copy


# Generated at 2022-06-12 23:49:20.793903
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == '1 Bytes'
    assert bytes_to_human(1, isbits=True) == '1 bits'
    assert bytes_to_human('1') == '1 Bytes'

# Generated at 2022-06-12 23:49:27.758470
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_cases = [
        [['Ala', 1], ['ala', 1]],
        [[1, 'Ola'], [1, 'ola']],
        [[1, 'Ola', 'Ala'], [1, 'ola', 'ala']],
        [['Ala', 1, 'Ola'], ['ala', 1, 'ola']],
    ]
    for test_case in test_cases:
        assert lenient_lowercase(test_case[0]) == test_case[1]


# Generated at 2022-06-12 23:49:34.322968
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2KB') == 2048
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1Mb') == 8388608
    assert human_to_bytes('1MBb') == 8388608
    assert human_to_bytes('1Mb', isbits=True) == 8388608


# Generated at 2022-06-12 23:49:43.908870
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from unittest import TestCase
    import sys

    class HumanToBytesTests(TestCase):

        def test_number_to_bytes(self):
            size = human_to_bytes(1)
            self.assertEqual(size, 1)
            size = human_to_bytes(1, unit='m')
            self.assertEqual(size, 1)
            size = human_to_bytes(1, unit='b')
            self.assertEqual(size, 1)

        def test_string_to_bytes(self):
            size = human_to_bytes('1')
            self.assertEqual(size, 1)
            size = human_to_bytes('1', unit='K')
            self.assertEqual(size, 1024)
            size = human_to_bytes('1K')

# Generated at 2022-06-12 23:49:50.287608
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    target = ['1', '2', '3', 'a', 'b', 'c', 'A', 'B', 'C']
    result = lenient_lowercase(target)
    expected_result = ['1', '2', '3', 'a', 'b', 'c', 'a', 'b', 'c']
    if result != expected_result:
        raise Exception("lenient_lowercase() failed with target list: %s" % target)



# Generated at 2022-06-12 23:49:55.390385
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    result1 = lenient_lowercase(['a','b','C','d','E','f','G','h','I','j','K'])
    result2 = ['a','b','c','d','e','f','g','h','i','j','k']
    assert result1 == result2

# Generated at 2022-06-12 23:50:01.942760
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import itertools
    import pytest


# Generated at 2022-06-12 23:50:03.536889
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 32]) == ['a', 'b', 32]

# Generated at 2022-06-12 23:50:15.653558
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import unittest
    class TestHumanToBytes(unittest.TestCase):
        def test_bytes(self):
            # Bytes
            self.assertEqual(human_to_bytes(10), 10)
            self.assertEqual(human_to_bytes(10, 'B'), 10)
            self.assertEqual(human_to_bytes(10, 'b'), 10)
            self.assertEqual(human_to_bytes(10, 'B', True), 10)
            self.assertEqual(human_to_bytes(10, 'b', True), 10)
            self.assertEqual(human_to_bytes(10, 'B', False), 10)
            self.assertEqual(human_to_bytes(10, 'b', False), 10)


# Generated at 2022-06-12 23:50:26.887913
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """ Test conversion bytes in human-readable format to integer.
    """
    # Test positive cases
    # Test with Bytes unit
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    # Test with default unit
    assert human_to_bytes('1') == 1
    # Test with Bits unit
    assert human_to_bytes('1Mb', True) == 1048576
    assert human_to_bytes('1MB', True) == 8388608
    # Test with passed Bits unit
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    # Negative use case
    assert human_to_bytes('1MB', isbits=False) == 8388608

# Generated at 2022-06-12 23:50:39.359634
# Unit test for function bytes_to_human
def test_bytes_to_human():
    # Test cases for bytes
    test_cases = [
        [0, '0.00 Bytes'],
        [1, '1.00 Bytes'],
        [2, '2.00 Bytes'],
        [30, '30.00 Bytes'],
        [1024, '1.00 KB'],
        [1536, '1.50 KB'],
        [1024 * 1024, '1.00 MB'],
        [1536 * 1024, '1.50 MB'],
        [1024 * 1024 * 1024, '1.00 GB'],
    ]

    for size, expected_string in test_cases:
        res = bytes_to_human(size)
        print('Testing bytes_to_human(%s): expected "%s", got "%s"' % (size, expected_string, res))
        assert res

# Generated at 2022-06-12 23:50:50.458043
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10') == 10
    assert human_to_bytes('0') == 0
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.') == 1
    assert human_to_bytes('.1') == 0
    assert human_to_bytes('1.0K') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1.0M') == 1048576
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1.0G') == 1073741824
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1.0B') == 1
   

# Generated at 2022-06-12 23:51:01.206070
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(1, unit='B') == '1.00 Bytes'
    assert bytes_to_human(1, unit='K') == '0.00 KB'
    assert bytes_to_human(1, unit='M') == '0.00 MB'
    assert bytes_to_human(1, unit='G') == '0.00 GB'
    assert bytes_to_human(1, unit='T') == '0.00 TB'

    assert bytes_to_human(1023) == '1023.00 Bytes'
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1025) == '1.00 KB'

# Generated at 2022-06-12 23:51:04.713999
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    from ansible.utils import lenient_lowercase
    assert(lenient_lowercase(['A', 'b', 'CC']) == ['a', 'b', 'cc'])
    assert(lenient_lowercase(['A', 'b', 1, 'CC']) == ['a', 'b', 1, 'cc'])

# Generated at 2022-06-12 23:51:16.202015
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['THIS', 'IS', 'A', 'TEST']) == ['this', 'is', 'a', 'test']
    assert lenient_lowercase('THIS IS A TEST') == 'this is a test'
    assert lenient_lowercase(['THIS', 'IS', 'A', {}, 'TEST']) == ['this', 'is', 'a', {}, 'test']
    assert lenient_lowercase(('THIS', 'IS', 'A', 'TEST')) == ('this', 'is', 'a', 'test')
    assert lenient_lowercase(['THIS', 'IS', 'A', ['TEST', 'TEST'], 'TEST']) == ['this', 'is', 'a', ['TEST', 'TEST'], 'test']

# Generated at 2022-06-12 23:51:27.617560
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test for cases described in docstring
    assert 1048576 == human_to_bytes('1MB')
    assert 1048576 == human_to_bytes(10, 'M')
    assert 1048576 == human_to_bytes(10, 'm')
    assert 1048576 == human_to_bytes(10, 'MB')
    assert 1048576 == human_to_bytes(10, 'Mb')
    assert 1048576 == human_to_bytes(10, 'Mb')
    assert 1048576 == human_to_bytes(10, 'mB')
    assert 1048576 == human_to_bytes(10, 'mb')
    assert 1048576 == human_to_bytes('10MB')
    assert 1048576 == human_to_bytes('10Mb')
    assert 1048576 == human_to_bytes

# Generated at 2022-06-12 23:51:35.718230
# Unit test for function bytes_to_human
def test_bytes_to_human():
    # isbits = False (default)
    assert bytes_to_human(0) == '0 Bytes'
    assert bytes_to_human(2352) == '2.36 KB'
    assert bytes_to_human(382982) == '372.66 KB'
    assert bytes_to_human(12345678) == '11.77 MB'
    assert bytes_to_human(382982) == '372.66 KB'
    assert bytes_to_human(1000000) == '976.56 KB'
    assert bytes_to_human(12345678) == '11.77 MB'
    assert bytes_to_human(1234567890) == '1.15 GB'
    assert bytes_to_human(1234567890123) == '1.11 TB'

# Generated at 2022-06-12 23:51:45.122699
# Unit test for function human_to_bytes
def test_human_to_bytes():
    testcases = {
        '5M': 5242880,
        '10M': 10485760,
        '5G': 5368709120,
        '1T': 1099511627776,
        '0': 0,
        '0b': 0,
        '0B': 0,
        '1b': 1,
        '1Kb': 1024,
        '1MB': 1048576,
        '50Mb': 52428800,
        '2 KB': 2048,
        '2.5KB': 2560,
        '10.5GB': 11190670336,
        '1.5tb': 1649267441664,
        '1.5tbB': 1649267441664,
    }

    # Test cases in bytes

# Generated at 2022-06-12 23:51:55.743276
# Unit test for function human_to_bytes
def test_human_to_bytes():
    if human_to_bytes('1MB') != 1048576:
        raise AssertionError('human_to_bytes does not work as expected (1)')
    if human_to_bytes('1MB', isbits=True) != 8388608:
        raise AssertionError('human_to_bytes does not work as expected (2)')
    if human_to_bytes('1MB', default_unit='B') != 1048576:
        raise AssertionError('human_to_bytes does not work as expected (3)')
    if human_to_bytes('1MB', default_unit='K', isbits=True) != 8388608:
        raise AssertionError('human_to_bytes does not work as expected (4)')

# Generated at 2022-06-12 23:52:02.451773
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("33", 'MB') == 34603008
    assert human_to_bytes("1.2M", 'B') == 1200000
    assert human_to_bytes("1.2M") == 1200000
    assert human_to_bytes("1.2M") == 1200000
    assert human_to_bytes("1.2K") == 1200
    assert human_to_bytes("1.2k") == 1200
    assert human_to_bytes("1.2KB", 'B') == 1200
    assert human_to_bytes("1.2KB") == 1200
    assert human_to_bytes("1.2Kb", isbits=True) == 1200
    assert human_to_bytes("1.2M", isbits=True) == 1200000

# Generated at 2022-06-12 23:52:04.602812
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["a", "B", "C", 1]) == ["a", "b", "c", 1]

# Generated at 2022-06-12 23:52:06.382189
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['string', 2]) == ['string', 2]


# Generated at 2022-06-12 23:52:11.588487
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    '''Test function lenient_lowercase'''
    test_list = [1, 'aBc', 1.234, '123', 'abc']
    expected = [1, 'abc', 1.234, '123', 'abc']
    assert lenient_lowercase(test_list) == expected


# Generated at 2022-06-12 23:52:17.928641
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    cases = [
        [['a'], ['a']],
        [['a', 'B'], ['a', 'B']],
        [['a', 'B', 1], ['a', 'B', 1]],
        [['a', 'B', 1, 'c', u'é'], ['a', 'B', 1, 'c', u'é']]
    ]

    for test, expected in cases:
        result = lenient_lowercase(test)
        assert result == expected



# Generated at 2022-06-12 23:52:27.326581
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """
    Unit tests for function human_to_bytes.
    """
    import pytest
    from ansible.module_utils.network.netvisor.utils.human_to_bytes import human_to_bytes

    # Test positive values
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10M', isbits=True) == 10485760
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'MB') == 10485760
    assert human_to_bytes(10, 'Mb') == 10485760

# Generated at 2022-06-12 23:52:42.473936
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Human readable to bytes
    assert 1048576 == human_to_bytes('1M')
    assert 1048576 == human_to_bytes('1MB')

    # Human readable to bits
    assert 8388608 == human_to_bytes('8m', isbits=True)
    assert 8388608 == human_to_bytes('8Mb', isbits=True)

    # Human readable to bytes with unit provided
    assert 1048576 == human_to_bytes('1', 'm')
    assert 8388608 == human_to_bytes('8', 'MB', isbits=True)

    # Unit provided without number
    assert 1073741824 == human_to_bytes('', 'GB')
    assert 536870912 == human_to_bytes('', 'GB', isbits=True)


# Generated at 2022-06-12 23:52:53.733860
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    tests = [
        # In
        ([], []),
        (['a'], ['a']),
        (['a', 1, 'b'], ['a', 1, 'b']),
        (['A'], ['a']),
        (['A', 1, 'B'], ['a', 1, 'b']),
        (['A', 1, 'b'], ['a', 1, 'b']),
    ]
    for (test_in, test_out) in tests:
        our_out = lenient_lowercase(test_in)
        assert our_out == test_out, "In = '%s' got = '%s' wanted = '%s'" % (repr(test_in), repr(our_out), repr(test_out))

# Generated at 2022-06-12 23:52:57.686771
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a b', 'c-d', 'e:f', 1, 2, 3, 'A B', 'C-D', 'E:F']
                             ) == ['a b', 'c-d', 'e:f', 1, 2, 3, 'A B', 'C-D', 'E:F']

# Generated at 2022-06-12 23:53:04.978568
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = [('1k', 1024), ('1m', 1048576), ('1G', 1073741824), ('1023', 1023), ('1K', 1024), ('1M', 1048576), ('1G', 1073741824), ('1023.5', 1023), ('1k', 1024), ('1mB', 1048576), ('1GB', 1073741824), ('1023b', 1023), ('1Kb', 1024), ('1Mb', 1048576), ('1Gb', 1073741824), ('1023.5b', 1023), ('1kb', 1024), ('1mb', 1048576), ('1Gb', 1073741824), ('1023.5B', 1023), ('1KB', 1024), ('1MB', 1048576), ('1GB', 1073741824), ('1023.5', 1023)]


# Generated at 2022-06-12 23:53:16.696854
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # some cases where input is valid
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('12Mb') == 12 * 1024
    assert human_to_bytes('1mB') == 1
    assert human_to_bytes('1MB') == 1 * 1048576
    assert human_to_bytes('1mb', isbits=True) == 1024
    assert human_to_bytes('1KB', isbits=True) == 1 * 1048576
    assert human_to_bytes('1kB', isbits=True) == 1024
    assert human_to_bytes('1.2Mb', isbits=True) == 1.2 * 1024

# Generated at 2022-06-12 23:53:24.910841
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1M', unit='B') == 1048576
    assert human_to_bytes('1M', unit='b', isbits=True) == 1048576
    assert human_to_bytes('1M', unit='B', isbits=True) == 1048576
    assert human_to_bytes('1M', unit='b') == 1048576
    assert human_to_bytes('1MB', unit='B') == 1048576
    assert human_to_bytes('1MB', unit='b', isbits=True) == 1048576
    assert human_to_bytes('1MB', unit='B', isbits=True) == 1048576
   

# Generated at 2022-06-12 23:53:35.897360
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import texttable as tt
    table = tt.Texttable()
    header = ['Name', 'human_to_bytes', 'bytes_to_human', 'bytes_to_human_bits', 'Result']
    table.header(header)
    table.set_deco(tt.Texttable.HEADER)
    table.set_cols_dtype(['t', 't', 't', 't', 't'])
    table.set_cols_width([25, 25, 25, 25, 8])

# Generated at 2022-06-12 23:53:45.396863
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

    def test_human_to_bytes_valid(test_input, expected):
        assert human_to_bytes(test_input) == expected

    def test_human_to_bytes_invalid(test_input):
        with pytest.raises(ValueError):
            human_to_bytes(test_input)

    test_human_to_bytes_valid('1', 1)
    test_human_to_bytes_valid(1, 1)

    test_human_to_bytes_valid('2', 2)
    test_human_to_bytes_valid(2, 2)

    test_human_to_bytes_valid('3', 3)
    test_human_to_bytes_valid(3, 3)

    test_human_to_bytes_valid('4', 4)
    test_human_to

# Generated at 2022-06-12 23:53:48.223100
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Strings should be lowercased
    assert lenient_lowercase(['a', 'B']) == ['a', 'b']

    # Non-strings should be passed through
    assert lenient_lowercase([1, None]) == [1, None]


# Generated at 2022-06-12 23:53:59.603201
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B', isbits=True) == 1
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1', isbits=True) == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes('1.5', isbits=True) == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.0', isbits=True) == 1
    assert human_to_bytes('.5') == 1
    assert human_to_bytes('.5', isbits=True) == 1

# Generated at 2022-06-12 23:54:12.143235
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Size ranges
    assert(human_to_bytes('1B') == 1)
    assert(human_to_bytes('+1B') == 1)
    assert(human_to_bytes('1.0B') == 1)
    assert(human_to_bytes('1.1B') == 1)
    assert(human_to_bytes('10B') == 10)
    assert(human_to_bytes('10.0B') == 10)
    assert(human_to_bytes('10.1B') == 10)
    assert(human_to_bytes('0B') == 0)
    assert(human_to_bytes('.0B') == 0)
    assert(human_to_bytes('.1B') == 0)
    assert(human_to_bytes('+.0B') == 0)

# Generated at 2022-06-12 23:54:17.394446
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # TODO: this test should be part of unit test
    assert lenient_lowercase(['a', 'b']) == ['a', 'b']
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase(['a', 'B']) == ['a', 'b']
    assert lenient_lowercase(['A', 'b']) == ['a', 'b']
    assert lenient_lowercase(['A', 1, 'b']) == ['a', 1, 'b']
    assert lenient_lowercase(['A', 1, 'b', [], {}, None, (1, 2)]) == ['a', 1, 'b', [], {}, None, (1, 2)]

# Generated at 2022-06-12 23:54:25.175126
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1GB', 'B') == 1073741824
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1b', 'b') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1B', isbits=True) == 8
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1MB', isbits=True) == 8388608
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human

# Generated at 2022-06-12 23:54:36.047730
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:46.132968
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:59.214697
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1Byte') == 1
    assert human_to_bytes('1.3Byte') == 2

    # 1KB = 1000Bytes
    assert human_to_bytes('1KB') == 1000
    assert human_to_bytes('0.1KB') == 100

    # 1KiB = 1024Bytes
    assert human_to_bytes('1KiB') == 1024
    assert human_to_bytes('0.1KiB') == 102

    # 1Mb = 1000000 bits
    assert human_to_bytes('1Mb', isbits=True) == 1000000
    assert human_to_bytes('0.1Mb', isbits=True) == 100000

    # 1MB = 1000000Bytes
    assert human_to_bytes('1MB') == 1000000

# Generated at 2022-06-12 23:55:02.906901
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['AbCdE', 1, 2.0]
    expected = 'abcde'
    result = lenient_lowercase(lst)
    assert result[0] == expected


# Generated at 2022-06-12 23:55:11.392074
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:21.691898
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:34.173991
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = [
        (1, '1', 'B', False),
        (1024, '1K', 'B', False),
        (1, '1b', 'b', True),
        (8, '1b', 'B', False),
        (8, '1', 'B', True),
        (1024 * 8, '1K', 'B', True),
        (1024 * 8, '1Kb', 'b', True),
        (1024 * 8, '1kb', 'b', True),
        (1024 * 8, '1K', 'B', False),
        (1024 * 8, '1kb', 'B', False),
    ]

    for expected, test_str, unit, isbits in tests:
        val = human_to_bytes(test_str, unit=unit, isbits=isbits)

# Generated at 2022-06-12 23:55:44.056801
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert [] == lenient_lowercase([]), 'Should handle empty list'
    assert [] == lenient_lowercase(()), 'Should handle empty tuple'
    assert [1, 'foo'] == lenient_lowercase([1, 'foo']), 'Should pass through nonstrings'
    assert ['foo', 'foo'] == lenient_lowercase(['Foo', 'foo']), 'Should lowercase strings'

# Generated at 2022-06-12 23:55:51.417810
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' This function test function human_to_bytes with different case '''
    # Case for human_to_bytes('2K')
    '''
    Example of string type passed to human_to_bytes
    '''
    assert human_to_bytes('2K') == 2048, "human_to_bytes() returns wrong value, expected to be 2048"

    # Case for human_to_bytes(10, 'M')
    '''
    Example of number and unit passed to human_to_bytes
    '''
    assert human_to_bytes(10, 'M') == 10485760, "human_to_bytes() returns wrong value, expected to be 10485760"

    # Case for human_to_bytes(10, 'm')

# Generated at 2022-06-12 23:55:53.841420
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['abc', 'def', 1, 2]) == ['abc', 'def', 1, 2]



# Generated at 2022-06-12 23:56:00.567168
# Unit test for function lenient_lowercase
def test_lenient_lowercase():  # pylint: disable=too-few-public-methods
    """Test the lenient_lowercase function."""
    assert lenient_lowercase(['ABC']) == ['abc']
    assert lenient_lowercase(['ABC', '123']) == ['abc', '123']
    assert lenient_lowercase(['ABC', 123]) == ['abc', 123]
    assert lenient_lowercase(['ABC', 123, 'xyz']) == ['abc', 123, 'xyz']

# Generated at 2022-06-12 23:56:08.064368
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_input = ['test', 'TEST', True, 'True']
    test_output = ['test', 'test', True, 'true']
    assert(lenient_lowercase(test_input) == test_output)

    no_error_input = 'test'
    assert(lenient_lowercase(no_error_input) == 'test')

    no_error_input = True
    assert(lenient_lowercase(no_error_input) is True)

# Generated at 2022-06-12 23:56:19.932363
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M', isbits=False) == 10485760
    assert human_to_bytes('10M', default_unit='M', isbits=False) == 10485760
    assert human_to_bytes('10.5M', default_unit='M', isbits=False) == 10485760
    assert human_to_bytes('10G', isbits=False) == 10737418240
    assert human_to_bytes('10G', default_unit='G', isbits=False) == 10737418240
    assert human_to_bytes('10.5G', default_unit='G', isbits=False) == 10737418240
    assert human_to_bytes('10K', isbits=False) == 10240

# Generated at 2022-06-12 23:56:31.592128
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test for bytes (B)

    assert human_to_bytes('1') == 1
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('0B') == 0
    assert human_to_bytes('0b') == 0
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10b', isbits=True) == 10

    assert human_to_bytes('1k') == 1 << 10
    assert human_to_bytes('10K') == 10 << 10
    assert human_to_bytes('10KB') == 10 << 10
    assert human_to_bytes('0K') == 0
    assert human_to_bytes('0k') == 0
    assert human_to_bytes('0KB') == 0

# Generated at 2022-06-12 23:56:34.216643
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, 'b', 'C']
    assert lenient_lowercase(lst) == [1, 'b', 'c']

# Some unit tests for function human_to_bytes

# Generated at 2022-06-12 23:56:43.138895
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(10, isbits=True) == 10
    assert human_to_bytes(10, isbits=True, default_unit='b') == 10
    assert human_to_bytes(10, isbits=True, default_unit='b') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10kb') == 10240
    assert human_to_bytes('10B') == 10

    assert human_to_bytes('10', unit='b') == 10
    assert human_to_bytes('10', unit='b') == 10
    assert human_to_bytes('10', unit='B') == 10

    assert human_to_bytes('10b', isbits=True) == 10
    assert human_to_bytes('10b', isbits=True) == 10
   

# Generated at 2022-06-12 23:56:46.073605
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ABC', 'DE', 'FGH']) == ['abc', 'DE', 'fgh']
    assert lenient_lowercase(['abc', 123]) == ['abc', 123]

# Generated at 2022-06-12 23:57:02.356069
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:05.047182
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([u'STOP', 'GO', 'S', 1]) == [u'stop', 'go', 's', 1]



# Generated at 2022-06-12 23:57:15.957762
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Tests for function human_to_bytes().
    '''


# Generated at 2022-06-12 23:57:22.919255
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2KB') == 2048
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes(1, 'MB') == 1048576
    assert human_to_bytes('2M') == 2097152
    assert human_to_bytes('10K') == 10240
    assert human_to_bytes('10.5K') == 10752
    assert human_to_bytes('10.5K', True) == 10752
    assert human_to_bytes('10K', True) == 10240
    assert human_to_bytes('1MB', isbits=True) == 8388608
    assert human_to_bytes('1Mb', isbits=True) == 8388608
    assert human_to_bytes('1Mb', isbits=False) == 1048576

# Generated at 2022-06-12 23:57:33.654700
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [
        ['A', 'B'],
        ['A', 1],
        ['A', ['B', 'C', 'D']],
        ['A', ['B', 1, 'D']],
        ['A', ['B', {'C': 'D', 'E': 'F'}]],
        ['A', ['B', {'C': 'D', 'E': ['F', 'G', 'H']}]],
        ['A', ['B', {'C': 'D', 'E': {1: '2', 3: '4'}}]],
    ]

    for test in test_list:
        # Deepcopy the list so we don't modify the original
        from copy import deepcopy
        lowered = lenient_lowercase(deepcopy(test))

# Generated at 2022-06-12 23:57:38.844279
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    tests = [
        {"test": ["A"], "res": ["a"]},
        {"test": ["a"], "res": ["a"]},
        {"test": [0, 1, None], "res": [0, 1, None]},
        {"test": [], "res": []}
    ]

    for test in tests:
        assert test["res"] == lenient_lowercase(test["test"])



# Generated at 2022-06-12 23:57:44.526129
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 1, 'C']) == ['a', 1, 'c']
    assert lenient_lowercase(['A', {'B': 1}, 'C']) == ['a', {'B': 1}, 'c']
    return True



# Generated at 2022-06-12 23:57:51.643703
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    cases = [
        [['A', 'b', 1], ['a', 'b', 1]],
        [['A', 1, 'b'], ['a', 1, 'b']],
        [['A', 'B', 'C'], ['a', 'b', 'c']],
        [[1, 2, 3], [1, 2, 3]],
    ]
    for lst, expected in cases:
        result = lenient_lowercase(lst)
        assert result == expected, 'Got %s for list %s, expected %s' % (result, lst, expected)


# Generated at 2022-06-12 23:58:04.812303
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('10K') == 10240
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1.5Mb') == 1572864
    assert human_to_bytes('1.5Mb', isbits=True) == 1920000
    assert human_to_bytes('1.5Mb', default_unit='Kb') == 1536
    assert human_to_bytes('1.5Mb', default_unit='Kb', isbits=True) == 1920000
    assert human_to_bytes('1.5Mb', default_unit='KB') == 1572864
    assert human_to_bytes('1.5Mb', default_unit='KB', isbits=True) == 19215

# Generated at 2022-06-12 23:58:13.168277
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit test for function human_to_bytes
    :return:
    """
    # test byte case
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1') == 1
    assert human_to_bytes('3b', default_unit='b') == 3
    assert human_to_bytes('3B', default_unit='B') == 3
    assert human_to_bytes('3B', default_unit='b') == 3
    assert human_to_bytes('3b', default_unit='B') == 3
    assert human_to_bytes('7b') == 7
    assert human_to_bytes('7B') == 7
    assert human_to_bytes('7') == 7

# Generated at 2022-06-12 23:58:33.014888
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Check bytes
    assert 131072 == human_to_bytes('128K')
    assert 1310720 == human_to_bytes('1Mb', isbits=True)
    assert 13107200 == human_to_bytes('10Mb', isbits=True)
    assert 1310720 == human_to_bytes('10MB', isbits=False)

