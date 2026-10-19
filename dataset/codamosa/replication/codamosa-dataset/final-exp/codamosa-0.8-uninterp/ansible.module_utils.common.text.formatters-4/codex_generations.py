

# Generated at 2022-06-12 23:48:55.383089
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1.0Mb', isbits=True) == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1.0Mb', isbits=True) == 1048576
    assert human_to_bytes('512.0Kb', isbits=True) == 524288
    assert human_to_bytes('512Kb', isbits=True) == 524288
    assert human_to_bytes('512.0Kb', isbits=True) == 524288
    assert human_to_bytes('256b', isbits=True) == 256
    assert human_to_bytes('256.0b', isbits=True) == 256

# Generated at 2022-06-12 23:49:06.309052
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Test human_to_bytes() function'''

# Generated at 2022-06-12 23:49:10.716155
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test case - string
    assert lenient_lowercase(['a', 'AB', 'aBc']) == ['a', 'ab', 'abc']
    # Test case - list
    assert lenient_lowercase([1, 'aBc', [2, 3]]) == [1, 'abc', [2, 3]]
    # Test case - number
    assert lenient_lowercase([1, 2, 'aBc']) == [1, 2, 'abc']


# Generated at 2022-06-12 23:49:16.393908
# Unit test for function human_to_bytes
def test_human_to_bytes():
    d = dict()
    d[('10M', None, False)] = 10485760
    d[('10M', 'B', False)] = 10485760
    d[('10M', 'M', False)] = 10
    d[('10.20M', 'M', False)] = 10.2
    d[('2.1G', 'M', False)] = 2147.48
    d[('10.20G', 'M', False)] = 10485.76
    d[('10.20G', 'G', False)] = 10.2
    d[('10', None, False)] = 10
    d[('10', 'G', False)] = 10
    d[('10.20', 'M', False)] = 10.2
    d[('10.20', None, False)] = 10.2

# Generated at 2022-06-12 23:49:25.861018
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1000) == '1000.00 Bytes'
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(12345678) == '11.77 MB'

# Generated at 2022-06-12 23:49:34.979874
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test with bytes
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1.5k') == 1536
    assert human_to_bytes('1.5KB') == 1536
    assert human_to_bytes('1.5Mb') == ValueError
    assert human_to_bytes('1.5mb')

# Generated at 2022-06-12 23:49:38.752793
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Test', 32, 'test']) == ['test', 32, 'test']
    assert lenient_lowercase(['Test', 'test']) == ['test', 'test']

# Generated at 2022-06-12 23:49:50.151316
# Unit test for function bytes_to_human
def test_bytes_to_human():
    if human_to_bytes('1m') != 1048576:
        return False
    if human_to_bytes('1mb') != 1048576:
        return False
    if human_to_bytes('1Mb', isbits=True) != 1048576:
        return False

    if bytes_to_human(1048576) != '1.00 MB':
        return False
    if bytes_to_human(1048576, unit='m') != '1048576.00 m':
        return False
    if bytes_to_human(1048576, unit='M') != '1048576.00 M':
        return False
    if bytes_to_human(1048576, unit='K') != '1048576.00 K':
        return False

# Generated at 2022-06-12 23:49:58.681067
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # default unit K
    assert human_to_bytes('1023') == 1023
    assert human_to_bytes('9K') == 9216
    assert human_to_bytes('1024K') == 1048576
    assert human_to_bytes('9M') == 9437184
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('9T') == 9663676416
    assert human_to_bytes('1') == 1
    assert human_to_bytes('9.5') == 9
    assert human_to_bytes('9.5K') == 9728
    assert human_to_bytes('0.5') == 0
    assert human_to_bytes(1.0) == 1
    assert human_to_bytes(1.9) == 1
    assert human_to_

# Generated at 2022-06-12 23:50:07.145476
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1kB') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1Mb') == 131072
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1K', isbits=True) == 8192
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 131072
    assert human_to_bytes('1K', unit='Byte') == 1024
    assert human_to_bytes('1K', unit='b') == 8192
    assert human_to_bytes('1K', unit='bit') == 8192
    assert human_to

# Generated at 2022-06-12 23:50:19.879121
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test for string values
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b') == 1
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10MBb') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 1310720
    assert human_to_bytes('10MBb', isbits=True) == 13107200
    assert human_to_bytes('10b', isbits=True) == 1

# Generated at 2022-06-12 23:50:23.206951
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 'b', 'C']) == [1, 'b', 'c']



# Generated at 2022-06-12 23:50:31.825441
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(1, unit='B') == '1.00 B'
    assert bytes_to_human(1, unit='bits') == '1.00 bits'
    assert bytes_to_human(1, unit='b') == '1.00 b'

    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1024, unit='B') == '1.00 B'
    assert bytes_to_human(1024, unit='bits') == '8192.00 bits'
    assert bytes_to_human(1024, unit='b') == '8192.00 b'

    assert bytes_to_human(1048576) == '1.00 MB'

# Generated at 2022-06-12 23:50:42.173529
# Unit test for function bytes_to_human
def test_bytes_to_human():
    val = b'8M'
    unit = 'M'
    assert bytes_to_human(val, unit=unit) == '8.00 MB'
    assert bytes_to_human(str(val), unit=unit) == '8.00 MB'

    val = b'8G'
    unit = 'M'
    assert bytes_to_human(val, unit=unit) == '8192.00 MB'
    assert bytes_to_human(str(val), unit=unit) == '8192.00 MB'

    val = b'8G'
    unit = 'G'
    assert bytes_to_human(val, unit=unit) == '8.00 GB'
    assert bytes_to_human(str(val), unit=unit) == '8.00 GB'


# Generated at 2022-06-12 23:50:50.640964
# Unit test for function human_to_bytes
def test_human_to_bytes():

    def test_data():
        return (
            # default 128 bit unit
            {},
            # default 128 bit unit, explicit
            {'default_unit': 'b'},
            # explicit, isbits=False
            {'isbits': False},
            # explicit, isbits=True
            {'isbits': True},
        )


# Generated at 2022-06-12 23:51:01.359615
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:08.613444
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test 1
    value = '10M'
    excepted_result = 10485760
    test_result = human_to_bytes(value)
    if test_result != excepted_result:
        print("Test 1 Failed")
        print("Test Value: " + value)
        print("Test Function Result: " + str(test_result))
        print("Test Expected Result: " + str(excepted_result))
        print("")
    else:
        print("Test 1 Passed")
        print("")

    # Test 2
    value = '2K'
    excepted_result = 2048
    test_result = human_to_bytes(value)
    if test_result != excepted_result:
        print("Test 2 Failed")
        print("Test Value: " + value)

# Generated at 2022-06-12 23:51:13.574159
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test various cases - return value should always be an integer.
    assert human_to_bytes('1') == 1
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10k') == 10 * 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('10M') == 10 * 1024 * 1024
    assert human_to_bytes('10m') == 10 * 1024 * 1024
    assert human_to_bytes('10G') == 10 * 1024 * 1024 * 1024
    assert human_to_bytes('10g') == 10 * 1024 * 1024 * 1024
    assert human_to_bytes('10T') == 10 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('10t') == 10 * 1024 * 1024 * 1024 * 1024

# Generated at 2022-06-12 23:51:15.863624
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'a', 'A']) == [1, 'a', 'A']



# Generated at 2022-06-12 23:51:25.254952
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import unittest

    class HumanToBytesTestCase(unittest.TestCase):
        """Test human_to_bytes()"""

        def test01_bit_values(self):
            self.assertEqual(human_to_bytes('1Mb', isbits=True), 1048576)
            self.assertEqual(human_to_bytes('1Mb', isbits=True, unit='kb'), 1024)
            self.assertEqual(human_to_bytes('1Mb', isbits=True, unit='b'), 1024*1024)
            self.assertEqual(human_to_bytes('1Mb', isbits=True, unit='b'), human_to_bytes('1Mb', isbits=True, unit='B'))

# Generated at 2022-06-12 23:51:35.624393
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:41.829449
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [[0,1,2,3], [2, 3, 4, 5], ['A','B','C','D'], ['a','b','c','d'], ['a','b','c','D']]
    result = lenient_lowercase(test_list)
    assert result == [[0,1,2,3], [2, 3, 4, 5], ['A','B','C','D'], ['a','b','c','d'], ['a','b','c','D']]


# Generated at 2022-06-12 23:51:53.629035
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [
        [],
        [1, 2, 3],
        ['1', '2', '3'],
        ['One', 'Two', 'Three'],
        ['One', 'Two', 3],
        [1, 'two', 'ThrEE'],
        ['OnE', 'TWO', 3],
        ['OnE', 'TWO', 'three'],
    ]
    results = [
        [],
        [1, 2, 3],
        ['1', '2', '3'],
        ['one', 'two', 'three'],
        ['one', 'two', 3],
        [1, 'two', 'three'],
        ['one', 'two', 3],
        ['one', 'two', 'three'],
    ]

# Generated at 2022-06-12 23:52:01.197367
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print("Starting test human_to_bytes ...")
    # testing bytes conversion
    if human_to_bytes('10') != 10:
        raise AssertionError("human_to_bytes('10') = %s != 10" % human_to_bytes('10'))
    if human_to_bytes('1') != 1:
        raise AssertionError("human_to_bytes('1') = %s != 1" % human_to_bytes('1'))
    if human_to_bytes('10K') != 10 * human_to_bytes('1K'):
        raise AssertionError("human_to_bytes('10K') = %s != 10 * human_to_bytes('1K')" % human_to_bytes('10K'))

# Generated at 2022-06-12 23:52:10.749424
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' test human_to_bytes function '''
    # no unit provided
    assert human_to_bytes('123.456') == 123
    assert human_to_bytes('.456') == 0
    # byte
    assert human_to_bytes('123M') == 123 * 1024 * 1024
    assert human_to_bytes('123') == 123
    assert human_to_bytes('123B') == 123
    # bit
    assert human_to_bytes('123Mb', isbits=True) == 123 * 1024 * 1024
    assert human_to_bytes('123', isbits=True) == 123
    assert human_to_bytes('123b', isbits=True) == 123


# Generated at 2022-06-12 23:52:20.502578
# Unit test for function bytes_to_human

# Generated at 2022-06-12 23:52:21.383759
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []

# Generated at 2022-06-12 23:52:25.443521
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    data = ['foo', 'BAR', 'baz', 1, 2, 3, '4', '5', '6']
    result = ['foo', 'bar', 'baz', 1, 2, 3, '4', '5', '6']
    assert lenient_lowercase(data) == result



# Generated at 2022-06-12 23:52:32.509381
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('1') == 1)
    assert(human_to_bytes('2k') == 2048)
    assert(human_to_bytes('2048') == 2048)
    assert(human_to_bytes('2k', isbits=True) == 2048)
    assert(human_to_bytes('2kb', isbits=True) == 2048)
    assert(human_to_bytes('4Mb', isbits=True) == 4194304)
    assert(human_to_bytes('4MB', isbits=False) == 4194304)
    assert(human_to_bytes('200G') == 214748364800)
    assert(human_to_bytes('200G', unit='k') == 214748364800000)

# Generated at 2022-06-12 23:52:38.926938
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["aaa", "bbb", "ccc"]) == ["aaa", "bbb", "ccc"]
    assert lenient_lowercase(["aaa", "bbb", "ccc", 100]) == ["aaa", "bbb", "ccc", 100]
    assert lenient_lowercase(["aaa", "bbb", "ccc", 100, "ddd"]) == ["aaa", "bbb", "ccc", 100, "ddd"]

# Generated at 2022-06-12 23:52:50.056712
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

    testcases = [('0', 0),
                 ('10b', 10),
                 ('20Mb', 20 * 1000 ** 2),
                 ('30MB', 30 * 1000 ** 2),
                 (20 * 1000 ** 2, 20 * 1000 ** 2)]

# Generated at 2022-06-12 23:52:59.366314
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''test_human_to_bytes'''


# Generated at 2022-06-12 23:53:02.528932
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["ABC", "DEF", "GHI"]) == ["abc", "def", "ghi"]
    assert lenient_lowercase(["ABC", 42, "GHI"]) == ["abc", 42, "ghi"]
    assert lenient_lowercase([]) == []


# Generated at 2022-06-12 23:53:14.205443
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # default unit (B)
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes(1.1) == 1
    assert human_to_bytes('1.5') == 2
    assert human_to_bytes('0.5') == 1
    assert human_to_bytes(0.5) == 1
    assert human_to_bytes('0.11') == 1
    assert human_to_bytes(0.11) == 1

    # bytes unit
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1b', isbits=True) == 1

# Generated at 2022-06-12 23:53:23.956566
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('2.3') == 2
    assert human_to_bytes('1.1 Mb') == 1153433
    assert human_to_bytes('10.5Mb', isbits=True) == 1153433
    assert human_to_bytes('10.5Mb', isbits=False) == 10485760
    assert human_to_bytes('10.5mb', isbits=False) == 10485760
    assert human_to_bytes('10.5MB', isbits=True) == 1153433
    assert human_to_bytes('10.5MB', isbits=False) == 10485760
    assert human_to_bytes('10.5 MB', isbits=True) == 1153433

# Generated at 2022-06-12 23:53:31.246597
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:42.180864
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['0', 1, 2, '3']) == ['0', 1, 2, '3']
    assert lenient_lowercase(['0', '1', '2', '3']) == ['0', '1', '2', '3']
    assert lenient_lowercase(['0', '1', '2', '3', 'c', 'B', 'a']) == ['0', '1', '2', '3', 'c', 'B', 'a']

# Generated at 2022-06-12 23:53:44.505614
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    list = ['hello', 'world', 1]
    ans = ['hello', 'world', 1]
    res = lenient_lowercase(list)
    assert res == ans

# Generated at 2022-06-12 23:53:50.152197
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', ['C']]) == ['a', 'b', ['C']]
    assert lenient_lowercase(['A', 'B', {'C': None}]) == ['a', 'b', {'C': None}]
    assert lenient_lowercase(['A', 'B', None]) == ['a', 'b', None]


# Generated at 2022-06-12 23:54:01.184288
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('0B') == 0
    assert human_to_bytes('0b') == 0
    assert human_to_bytes('0b', isbits=True) == 0

    assert human_to_bytes('1.5B') == 1.5
    assert human_to_bytes('1.5Kb') == 1.5 * 1 << 10
    assert human_to_bytes('1.5Kb', isbits=True) == 1.5 * 1 << 10
    assert human_to_bytes('1.5KB') == 1.5 * 1 << 10
    assert human_to_bytes('1.5K') == 1.5 * 1 << 10
    assert human_to_bytes('1.5kB') == 1.5 * 1 << 10
    assert human_to_bytes('1.5Mb') == 1.

# Generated at 2022-06-12 23:54:13.151261
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
   test_list = [1, 2, 'abc', 'ABC', 4]
   expected_list = [1, 2, 'abc', 'abc', 4]
   assert lenient_lowercase(test_list) == expected_list


# Generated at 2022-06-12 23:54:23.101925
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:30.517409
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 2, 'c']) == ['a', 2, 'c']


# Generated at 2022-06-12 23:54:38.905984
# Unit test for function human_to_bytes
def test_human_to_bytes():

    """Test function human_to_bytes() with human string value of bits and bytes.
    When passing bytes string value, this function validates the string
    and returns bytes number of value,
    if string is not valid, it raises ValueError.
    When passing bits, then this function is expected to validates the string
    and return bits value.
    """

    # verify bytes_string value to be converted to bytes, then pass to function
    # and verify returned value.
    bytes_string = '1.5 MB'
    expected_bytes = 1572608
    bytes_converted = human_to_bytes(bytes_string)
    assert isinstance(bytes_converted, int)
    assert bytes_converted == expected_bytes
    # verify bits_string value to be converted to bytes and verify returned value.
    bits_string = '1.5 Mb'

# Generated at 2022-06-12 23:54:42.939121
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Lowercase a list of strings; non-strings pass through untouched.
    assert lenient_lowercase(['A', 'b', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 42, 'C']) == ['a', 42, 'c']



# Generated at 2022-06-12 23:54:46.327476
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['upPer', 'lOwer', 1, 1.0, True, False, 'mid']
    assert lenient_lowercase(lst) == ['upper', 'lower', 1, 1.0, True, False, 'mid']



# Generated at 2022-06-12 23:54:59.217119
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10K') == 10240
    assert human_to_bytes('10K', isbits=False) == 10240
    assert human_to_bytes('10K', isbits=True) == 81920
    assert human_to_bytes('10Kb') == 81920
    assert human_to_bytes('10Kb', isbits=False) == 81920
    assert human_to_bytes('10Kb', isbits=True) == 81920
    assert human_to_bytes('10K', isbits=True, default_unit='B') == 81920
    assert human_to_bytes('10Kb', isbits=True, default_unit='B') == 81920
    assert human_to_bytes('10Kb', isbits=True, default_unit='b') == 81920


# Generated at 2022-06-12 23:55:09.523617
# Unit test for function bytes_to_human
def test_bytes_to_human():
    bytes = (
        (10, '10 Bytes'),
        (20, '20 Bytes'),
        (0, '0 Bytes'),
        (1024, '1.00 KB'),
        (1024 ** 2, '1.00 MB'),
        (1024 ** 3, '1.00 GB'),
        (1024 ** 4, '1.00 TB'),
        (1024 ** 5, '1.00 PB'),
        (1024 ** 6, '1.00 EB'),
        (1024 ** 7, '1.00 ZB'),
        (1024 ** 8, '1.00 YB'),
    )

    for test_bytes, expected in bytes:
        result = bytes_to_human(test_bytes)
        assert result == expected, 'Failed to convert %s bytes: got %s' % (test_bytes, result)



# Generated at 2022-06-12 23:55:14.438282
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['Mb', 'MB', 1, 'Kb', 'Kb', {}, []]

    assert lenient_lowercase(lst) == ['mb', 'mb', 1, 'kb', 'kb', {}, []]



# Generated at 2022-06-12 23:55:24.293598
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    unit test for human_to_bytes function
    '''

    #
    # standard test
    #
    try:
        human_to_bytes('2K')
    except Exception:
        raise
    else:
        pass
    try:
        human_to_bytes('2M')
    except Exception:
        raise
    else:
        pass

    #
    # bits test
    #
    try:
        human_to_bytes('2kb', isbits=True)
    except Exception:
        raise
    else:
        pass
    try:
        human_to_bytes('2mb', isbits=True)
    except Exception:
        raise
    else:
        pass

    try:
        human_to_bytes('2kb')
    except Exception:
        pass

# Generated at 2022-06-12 23:55:46.715140
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('5.5M') == int('5.5M', 10)
    assert human_to_bytes('5.5M', 'M') == int('5.5M', 10)
    assert human_to_bytes('5.5b', isbits=True) == int('5.5b', 10)
    assert human_to_bytes('5.5b', 'b', isbits=True) == int('5.5b', 10)
    assert human_to_bytes('5.5Mb', isbits=True) == int('5.5Mb', 10)
    assert human_to_bytes('5.5Mb', 'Mb', isbits=True) == int('5.5Mb', 10)
    assert human_to_bytes('10B') == 10
    assert human_to_bytes

# Generated at 2022-06-12 23:55:58.649605
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print('Testing human_to_bytes')

    # bytes
    print('testing bytes')
    assert(human_to_bytes('1B') == 1)
    assert(human_to_bytes('1b') == 1)
    assert(human_to_bytes('2B') == 2)
    assert(human_to_bytes('2b') == 2)
    assert(human_to_bytes('1.1B') == 1)
    assert(human_to_bytes('1.1b') == 1)
    assert(human_to_bytes('1.5B') == 2)
    assert(human_to_bytes('1.5b') == 2)
    assert(human_to_bytes('1.9B') == 2)
    assert(human_to_bytes('1.9b') == 2)

# Generated at 2022-06-12 23:56:10.358629
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M', 'B') == 1048576, "1M should return 1048576 instead of %s" % human_to_bytes('1M', 'B')
    assert human_to_bytes('1MB') == 1048576, "1MB should return 1048576 instead of %s" % human_to_bytes('1MB')
    assert human_to_bytes('1Mb', isbits=True) == 1048576, "1Mb should return 1048576 instead of %s" % human_to_bytes('1Mb', isbits=True)
    assert human_to_bytes('1MB', 'b') is None, "1MB should return None instead of %s" % human_to_bytes('1MB', 'b')
    assert human_to_bytes('1MB', 'b', True) == 10

# Generated at 2022-06-12 23:56:21.429856
# Unit test for function human_to_bytes
def test_human_to_bytes():
    result = human_to_bytes('100')
    assert result == 100
    result = human_to_bytes('100K')
    assert result == 100 * 1024
    result = human_to_bytes('100M')
    assert result == 100 * 1024 * 1024
    result = human_to_bytes('100G')
    assert result == 100 * 1024 * 1024 * 1024
    result = human_to_bytes('100T')
    assert result == 100 * 1024 * 1024 * 1024 * 1024
    result = human_to_bytes('100P')
    assert result == 100 * 1024 * 1024 * 1024 * 1024 * 1024
    result = human_to_bytes('100E')
    assert result == 100 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    result = human_to_bytes('100Z')

# Generated at 2022-06-12 23:56:32.044106
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:56:41.418313
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1Z') == 1180591620717411303424
    assert human_to_bytes('1Y') == 1208925819614629174706176
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB', 'B') == 1048576

# Generated at 2022-06-12 23:56:51.995532
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:01.032550
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test cases for  bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1.1MB') == 11534336
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1.1KB') == 1126
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1.1b') == 131072
    assert human_to_bytes('1b') == 131072

    # Test cases for bits
    assert human_to_bytes('1B', isbits=True) == 8
    assert human_to_bytes('1.1MB', isbits=True) == 92233

# Generated at 2022-06-12 23:57:12.187984
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert (human_to_bytes('1') == 1)
    assert (human_to_bytes('10') == 10)
    assert (human_to_bytes('15') == 15)
    assert (human_to_bytes('1B') == 1)
    assert (human_to_bytes('10B') == 10)
    assert (human_to_bytes('15B') == 15)
    assert (human_to_bytes('1b') == 1)
    assert (human_to_bytes('10b') == 10)
    assert (human_to_bytes('15b') == 15)
    assert (human_to_bytes('1KB') == 1024)
    assert (human_to_bytes('10KB') == 10240)
    assert (human_to_bytes('15KB') == 15360)

# Generated at 2022-06-12 23:57:16.741286
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [1, '10M', 'ab', 'cd']
    expected_list = [1, '10M', 'ab', 'cd']
    out = lenient_lowercase(test_list)
    assert len(out) == len(expected_list)
    assert all(x == y for x, y in zip(out, expected_list))



# Generated at 2022-06-12 23:57:34.820277
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Input is a list of strings and numbers
    test_list = ['A', 1, 'b', 2, 'c']
    # Run the lenient_lowercase function
    result = lenient_lowercase(test_list)
    # Expected result is a list of strings and numbers, all strings are lowercase
    expected = ['a', 1, 'b', 2, 'c']
    assert result == expected

# Generated at 2022-06-12 23:57:38.229538
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # the test will give an error if the function
    # doesn't work as expected
    assert ['a', 'b', 'c', 1, 2, 3] == lenient_lowercase(['a', 'B', 'c', 1, 2, 3])


# Generated at 2022-06-12 23:57:42.394680
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A','B','C']) == ['a','b','c']
    assert lenient_lowercase(['A','B',57]) == ['a','b',57]
    assert lenient_lowercase([1,2,3]) == [1,2,3]


# Generated at 2022-06-12 23:57:47.895053
# Unit test for function human_to_bytes
def test_human_to_bytes():
    def _test(number, exp_value):
        result = human_to_bytes(number)
        assert result == int(round(exp_value)), "human_to_bytes failed to convert %s (expect %d; output %d)" % (number, exp_value, result)

    _test('1', 1)
    _test('1.1', 1)
    _test('1.9', 2)
    _test('-1.01', -1)
    _test('1K', 1024)
    _test('1 K', 1024)
    _test('1KB', 1024)
    _test('1B', 1)
    _test('1Bb', 1)
    _test('1.1K', 1120)
    _test('1.1Kb', 1120)

# Generated at 2022-06-12 23:57:50.560866
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['TEst']) == ['test']
    assert lenient_lowercase(['test', 1]) == ['test', 1]


# Generated at 2022-06-12 23:57:57.141682
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Input data should be a string, which can be in form of:
        - 1.5KB
        - 10MB
        - 2E
        - E
        - 20.2Mb
        - 30Kb
        - 20.3b
        - 30kb
        etc.
    '''
    assert human_to_bytes('20.2Mb', isbits=True) == (20.2 * 1024 * 1024)
    assert human_to_bytes('30Kb', isbits=True) == (30 * 1000)
    assert human_to_bytes('20.3b', isbits=True) == (20.3)

    assert human_to_bytes('20.2M', default_unit='M') == (20.2 * 1024 * 1024)

# Generated at 2022-06-12 23:58:01.761025
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    val = ['myhost', 1, 'myhost1', 'MYHOST']
    assert lenient_lowercase(val) == ['myhost', 1, 'myhost1', 'myhost']
    assert lenient_lowercase(['myhost']) == ['myhost']

# Generated at 2022-06-12 23:58:11.301211
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2048 # '2K' is 2 * 1024
    assert human_to_bytes('2.5M') == 262144 # '2.5M' is 2.5 * 1024 * 1024
    assert human_to_bytes('3.4P') == 3.4 * (1 << 50)
    assert human_to_bytes('-0') == 0 # '-0' is 0
    assert human_to_bytes(-1) == -1 # -1 is -1
    assert human_to_bytes('0M', default_unit='K') == 0 # '0M' with default_unit 'K' is 0
    assert human_to_bytes('0', default_unit='K') == 0 # '0' with default_unit 'K' is 0

# Generated at 2022-06-12 23:58:21.565118
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit test for the human_to_bytes function."""
    # Test valid cases
    if human_to_bytes('1') != 1:
        raise Exception('Failed human_to_bytes with integer value as input')
    if human_to_bytes('1.1') != 1:
        raise Exception('Failed human_to_bytes with float value as input')
    if human_to_bytes('10B') != 10:
        raise Exception('Failed human_to_bytes with Bytes format as input')
    if human_to_bytes('10Bb') != 10:
        raise Exception('Failed human_to_bytes with bits format as input')
    if human_to_bytes('10Bb', isbits=True) != 10:
        raise Exception('Failed human_to_bytes with bits format as input')

# Generated at 2022-06-12 23:58:27.307921
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M') == 1024 ** 2
    assert human_to_bytes('2.5K') == int(2.5 * 1024)
    assert human_to_bytes('10M') == 10 * 1024 ** 2
    assert human_to_bytes('1B', 'M') == int(1024 ** 2)
    assert human_to_bytes('1KB') == int(1024)
    assert human_to_bytes('1Kb') == int(1000)
    assert human_to_bytes('1KB', default_unit='b', isbits=True) == int(1000)


if __name__ == '__main__':
    test_human_to_bytes()