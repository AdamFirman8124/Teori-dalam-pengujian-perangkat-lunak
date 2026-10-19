

# Generated at 2022-06-12 23:48:47.697190
# Unit test for function human_to_bytes
def test_human_to_bytes():
    def check(val, exp):
        if human_to_bytes(val) != exp:
            raise Exception('Expect %s and got %s' % (exp, human_to_bytes(val)))

    check('1B', 1)
    check('1b', 1)
    check('1MB', 1048576)
    check('1Mb', 1048576)
    check('1MB', 1048576)
    check('1Mb', 1048576)
    check('2.5MB', 2621440000 / 10)
    check('2.5Mb', 2621440000 / 10)
    check('2048k', 2097152)
    check('0.5G', 500000000)
    check('0.5g', 500000000)
    check('1.5E', 150000000000)

# Generated at 2022-06-12 23:48:56.702513
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1T') == (1 << 40)
    assert human_to_bytes('1Tb') == (1 << 40)
    assert human_to_bytes('1TB') == (1 << 40)
    assert human_to_bytes('1T', 'B') == (1 << 40)
    assert human_to_bytes('1T', 'b') == (1 << 40)
    assert human_to_bytes('1T', 'b', isbits=True) == (1 << 40)
    assert human_to_bytes('1Tb', 'B', isbits=True) == (1 << 40)
    assert human_to_bytes('1TB', 'b', isbits=True) == (1 << 40)
    assert human_to_bytes('1Tb', isbits=True) == (1 << 40)

# Generated at 2022-06-12 23:49:07.412153
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("10M") == 10485760
    assert human_to_bytes("10Mb") == 10485760
    assert human_to_bytes("10MB") == 10485760
    assert human_to_bytes("10mb") == 10485760
    assert human_to_bytes("10Mib") == 10485760
    assert human_to_bytes("1M", "B") == 1048576
    assert human_to_bytes("1M", "b") == 8388608
    assert human_to_bytes("1Mb") == 1048576
    assert human_to_bytes("1Mb", "b") == 8388608
    assert human_to_bytes("1Mb", "B") == 1048576
    assert human_to_bytes("1Mb") == 1048576


# Generated at 2022-06-12 23:49:14.231091
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

    # Test for bytes
    derived_value = human_to_bytes('10.2M')
    expected_value = 107370912
    assert derived_value == expected_value

    # Test for bytes with spaces
    derived_value = human_to_bytes(u'10.2  M')
    expected_value = 107370912
    assert derived_value == expected_value

    # Test for bytes without number
    derived_value = human_to_bytes(u'M')
    expected_value = 1
    assert derived_value == expected_value

    # Test for bits
    derived_value = human_to_bytes(u'10.2Mb', isbits=True)
    expected_value = 107370912
    assert derived_value == expected_value

    # Test for bits with spaces
    derived_

# Generated at 2022-06-12 23:49:21.353875
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:32.167757
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:38.596598
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1mb') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1ZB') == 1099511627776
    assert human_to_bytes('1YB') == 1125899906842624
    assert human_to_bytes('2.5K') == 2560
    assert human_to_bytes('2.5KB') == 2560
    assert human_to_bytes('2.5') == 2
    assert human_to

# Generated at 2022-06-12 23:49:50.049799
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(2) == 2
    assert human_to_bytes('2') == 2
    assert human_to_bytes('2K') == 2 * 1024
    assert human_to_bytes('2M') == 2 * 1024 * 1024
    assert human_to_bytes('2G') == 2 * 1024 * 1024 * 1024
    assert human_to_bytes('2T') == 2 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes(2, 'K') == 2 * 1024
    assert human_to_bytes(2, 'M') == 2 * 1024 * 1024
    assert human_to_bytes(2, 'G') == 2 * 1024 * 1024 * 1024
    assert human_to_bytes(2, 'T') == 2 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('1.5K')

# Generated at 2022-06-12 23:49:58.572858
# Unit test for function human_to_bytes
def test_human_to_bytes():
    for suffix, limit in iteritems(SIZE_RANGES):
        bytes_value = human_to_bytes(1, suffix)
        assert bytes_value == 1 << (10*(ord(suffix[0])-ord('B'))), "Failed suffix: %s" % suffix
        bytes_value = human_to_bytes(1, suffix.lower())
        assert bytes_value == 1 << (10*(ord(suffix[0])-ord('B'))), "Failed suffix: %s" % suffix

    # lowercase should works too.
    assert human_to_bytes(1, 'b') == 1
    assert human_to_bytes(1, 'b', isbits=True) == 1

    # bits to bytes
    assert human_to_bytes(1, 'b', isbits=True) == 1

# Generated at 2022-06-12 23:50:01.449495
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    """Test the lenient_lowercase function.
    """
    assert lenient_lowercase(['one', 2, 'THREE']) == ['one', 2, 'THREE']



# Generated at 2022-06-12 23:50:10.787477
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_data = [
        ('dhcp', 'dhcp'),
        ('DHCP', 'dhcp'),
        (['dhcp', 'DHCP', ('dhcp', 'DHCP')], ['dhcp', 'dhcp', ('dhcp', 'DHCP')]),
    ]

    for input, expected in test_data:
        output = lenient_lowercase(input)
        assert expected == output

# Generated at 2022-06-12 23:50:20.187407
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # default unit
    assert human_to_bytes("10") == 10
    assert human_to_bytes("10", unit='B') == 10
    assert human_to_bytes("10", unit='B', isbits=True) == 10

    # bytes
    assert human_to_bytes("10B") == 10
    assert human_to_bytes("10B", isbits=True) == 10
    assert human_to_bytes("10b") == 10
    assert human_to_bytes("10b", isbits=True) == 10

    # kilobytes
    assert human_to_bytes("10KB") == 10 * 1024
    assert human_to_bytes("10KB", isbits=True) == 10 * 1024
    assert human_to_bytes("10Kb") == 10 * 1024

# Generated at 2022-06-12 23:50:29.341505
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import sys
    if sys.version_info < (3,):
        long_integer = long
    else:
        long_integer = int

    # test with size unit
    assert human_to_bytes('1') == 0
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('1K') == 1 << 10
    assert human_to_bytes('1M') == 1 << 20
    assert human_to_bytes('1G') == 1 << 30
    assert human_to_bytes('1T') == 1 << 40
    assert human_to_bytes('1P') == 1 << 50
    assert human_to_bytes('1E') == 1 << 60
    assert human_to_bytes('1Z') == 1 << 70
    assert human_

# Generated at 2022-06-12 23:50:38.119555
# Unit test for function lenient_lowercase
def test_lenient_lowercase():

    # Empty list should return empty list
    assert lenient_lowercase([]) == []

    # None should pass through as None
    assert lenient_lowercase([None]) == [None]

    # Numeric values should pass through as numeric values
    assert lenient_lowercase([42]) == [42]

    # Strings should be lowercased
    assert lenient_lowercase(['Abc']) == ['abc']

    # Mixed list should be lowercased where possible
    assert lenient_lowercase(['Abc', 42, None]) == ['abc', 42, None]



# Generated at 2022-06-12 23:50:39.173502
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['FOO', 'bar', 2]) == ['foo', 'bar', 2]

# Generated at 2022-06-12 23:50:48.060839
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'a', 'b', 1, None]) == [1, 'a', 'b', 1, None]
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 'A', '1', 1]) == ['a', 'a', '1', 1]


# Generated at 2022-06-12 23:50:59.846596
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1024, 0) == '1.00 KB'
    assert bytes_to_human(1024, 0, 'K') == '1.00 KB'
    assert bytes_to_human(1024, 0, 'b') == '1.00 bits'

    assert bytes_to_human(1024, 1) == '8.00 Kb'
    assert bytes_to_human(1024, 1, 'K') == '8.00 Kb'
    assert bytes_to_human(1024, 1, 'B') == '8.00 bits'

    assert bytes_to_human(1024, isbits=1, unit='K') == '8.00 Kb'
    assert bytes_to_human(1024, isbits=1, unit='k') == '8.00 Kb'

# Generated at 2022-06-12 23:51:08.218058
# Unit test for function bytes_to_human
def test_bytes_to_human():
    for unit, limit in SIZE_RANGES.items():
        assert bytes("%.2f %s" % (limit*10, unit + 'B')) == bytes_to_human(limit*10, False, unit)
        assert bytes("%.2f %s" % (limit*10, unit + 'b')) == bytes_to_human(limit*10, True, unit)
    assert bytes("1.00 bit") == bytes_to_human(1, True)
    assert bytes("1.00 Byte") == bytes_to_human(1)


# Generated at 2022-06-12 23:51:13.567180
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    input_list = ['a', 'b', 'c', 1, 2, 3, True]
    expected_output = ['a', 'b', 'c', 1, 2, 3, True]
    test_output = lenient_lowercase(input_list)
    assert test_output == expected_output, 'Failed to validate that the lenient_lowercase function worked.'



# Generated at 2022-06-12 23:51:23.448708
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1kB') == 1024
    assert human_to_bytes('1KBb') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1024 * 1024
    assert human_to_bytes('1G') == 1024 * 1024 * 1024

    # test with float values
    assert human

# Generated at 2022-06-12 23:51:34.400996
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:39.673473
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    result = [1, 2, 3]
    assert result == lenient_lowercase(result)

    result = [1, 'a', 2, 'b', 3]
    assert result == lenient_lowercase(result)

    result = [1, 'a', 2, 'B', 3]
    assert [1, 'a', 2, 'b', 3] == lenient_lowercase(result)



# Generated at 2022-06-12 23:51:50.784472
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('10') == 10
    assert human_to_bytes('2M') == 2*(2**20)
    assert human_to_bytes('2Mb') == 2*(2**20)
    assert human_to_bytes('2MB') == 2*(2**20)
    assert human_to_bytes('2mb') == 2*(2**20)
    assert human_to_bytes(2, 'Mb') == 2*(2**20)
    assert human_to_bytes('2Mb', isbits=True) == 2*(2**20)
    assert human_to_bytes('2MB', isbits=True) == 2*(2**20)
    assert human_to_bytes('2mb', isbits=True) == 2

# Generated at 2022-06-12 23:51:58.307098
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase('foo') == 'foo'
    assert lenient_lowercase(['foo', 'bar']) == ['foo', 'bar']
    assert lenient_lowercase(('foo', 'bar')) == ['foo', 'bar']
    assert lenient_lowercase(['Foo', 'bar']) == ['foo', 'bar']
    assert lenient_lowercase(['Foo', ['bar']]) == ['foo', ['bar']]
    assert lenient_lowercase(['Foo', ('bar', 'baz')]) == ['foo', ('bar', 'baz')]

# Generated at 2022-06-12 23:52:09.005267
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([0]) == [0]
    assert lenient_lowercase([0, 1, 2]) == [0, 1, 2]
    assert lenient_lowercase(['0', '1', '2']) == ['0', '1', '2']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['0', 'a', 'A']) == ['0', 'a', 'a']
    assert lenient_lowercase(['0', 'A', 'a']) == ['0', 'a', 'a']
    assert lenient_lowercase(['0', 'A', 'a', 'B']) == ['0', 'a', 'a', 'b']

# Generated at 2022-06-12 23:52:13.902960
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # None
    assert lenient_lowercase(None) == None

    # Empty list
    assert lenient_lowercase([]) == []

    # Mixed list
    assert lenient_lowercase(['a', 'B', 1]) == ['a', 'b', 1]

# Generated at 2022-06-12 23:52:18.379674
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['Yes', 'No', 'Maybe']
    assert lenient_lowercase(lst) == ['yes', 'no', 'maybe']

    lst = ['Yes', 1, 'No', 3.0, 'Maybe']
    assert lenient_lowercase(lst) == ['yes', 1, 'no', 3.0, 'maybe']



# Generated at 2022-06-12 23:52:27.782385
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # No unit
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10', default_unit='B') == 10
    assert human_to_bytes(10) == 10
    assert human_to_bytes(10, default_unit='B') == 10

    # No unit and decimal
    assert human_to_bytes('10.5') == 10
    assert human_to_bytes('10.5', default_unit='B') == 10
    assert human_to_bytes(10.5) == 10
    assert human_to_bytes(10.5, default_unit='B') == 10

    # Bytes
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes(10, unit='B') == 10
   

# Generated at 2022-06-12 23:52:38.312003
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('1b') == 1)
    assert(human_to_bytes('1b', isbits=True) == 8)
    assert(human_to_bytes('1B', isbits=True) == 1)
    assert(human_to_bytes('1') == 1)
    assert(human_to_bytes('1', default_unit='B') == 1)
    assert(human_to_bytes('1', default_unit='B', isbits=True) == 1)
    assert(human_to_bytes('1', default_unit='b') == 8)
    assert(human_to_bytes('1', default_unit='b', isbits=True) == 8)
    assert(human_to_bytes('1', default_unit='K') == 1)

# Generated at 2022-06-12 23:52:46.966294
# Unit test for function human_to_bytes
def test_human_to_bytes():

    # Test converting from bytes
    assert human_to_bytes('2KB') == 2*1024
    assert human_to_bytes('2K') == 2*1024
    assert human_to_bytes('10B') == 10

    # Test converting from bits
    assert human_to_bytes('2Mb', isbits=True) == 2*1024*1024

    # Test converting to bits
    assert human_to_bytes('2KB', unit='b') == 2*1024*8
    assert human_to_bytes('2Mb') == 2*1024*1024

    # Test converting with default_unit
    assert human_to_bytes('2KB', default_unit='b') == 2*1024*8
    assert human_to_bytes('2', default_unit='Mb') == 2*1024*1024

    # Test converting with None as unit
   

# Generated at 2022-06-12 23:52:59.732009
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('2K') == human_to_bytes('2K', unit='B'))
    assert(human_to_bytes('10M') == human_to_bytes(10, unit='M'))

    assert(human_to_bytes('2K', unit='B') == human_to_bytes('2K', default_unit='B'))
    assert(human_to_bytes('10M', unit='M') == human_to_bytes(10, default_unit='M'))

    assert(human_to_bytes('2K', unit='B') == human_to_bytes(2, 'KB'))
    assert(human_to_bytes('10M', unit='M') == human_to_bytes(10, 'MB'))


# Generated at 2022-06-12 23:53:06.397717
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a', 'b', 'C']) == ['a', 'b', 'C']
    assert lenient_lowercase(['a', 1, 'C']) == ['a', 1, 'C']
    assert lenient_lowercase(['a', 'b', 'B']) == ['a', 'b', 'B']
    assert lenient_lowercase(['a', 'b', 'b']) == ['a', 'b', 'b']
    assert lenient_lowercase(['a', 'b', 'b', 'b']) == ['a', 'b', 'b', 'b']

# Generated at 2022-06-12 23:53:18.165635
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

# Generated at 2022-06-12 23:53:22.993980
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["a", 2, 3]) == ["a", 2, 3]
    assert lenient_lowercase(["A", 2, 3]) == ["a", 2, 3]
    assert lenient_lowercase(["A", "b", "C"]) == ["a", "b", "c"]
    assert lenient_lowercase(["A", "B", "C"]) == ["a", "b", "c"]


# Generated at 2022-06-12 23:53:30.575596
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a']) == ['a']
    assert lenient_lowercase(['A']) == ['a']
    assert lenient_lowercase(['A0']) == ['a0']
    assert lenient_lowercase(['A0', 'B1', 'C2']) == ['a0', 'b1', 'c2']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase(['a1', 2, 'b3']) == ['a1', 2, 'b3']
    assert lenient_lowercase(['a1', 2, ['b3', 4]]) == ['a1', 2, ['b3', 4]]

# Generated at 2022-06-12 23:53:39.670344
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    import json
    import pytest
    test_list = [1, 'a', 2, 'b', 'D', 'c']
    lower_case_list = lenient_lowercase(test_list)
    assert lower_case_list == [1, 'a', 2, 'b', 'D', 'c']

    test_dict = {'a': '2', 'b': [1, 2, 3], 'C': 'd'}
    lower_case_dict = lenient_lowercase(test_dict)
    assert lower_case_dict == {'a': '2', 'b': [1, 2, 3], 'C': 'd'}

# Generated at 2022-06-12 23:53:41.735587
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['FOO', 'bar', 'BaZ', 5]) == ['foo', 'bar', 'baz', 5]

# Generated at 2022-06-12 23:53:49.632854
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:00.686359
# Unit test for function human_to_bytes
def test_human_to_bytes():
    def strict_equal(input_string, expected_value):
        if human_to_bytes(input_string) == expected_value:
            print ("OK for string: %s" % input_string)
            return
        print ("Error for string: %s. Got %s, expected %s."
               % (input_string, human_to_bytes(input_string), expected_value))

    strict_equal('124', 124)
    strict_equal('1KB', 1024)
    strict_equal('1B', 1)
    strict_equal('125KB', 128000)
    strict_equal('12342KB', 12627456)
    strict_equal('123KB', 126144)
    strict_equal('12.5KB', 12800)

# Generated at 2022-06-12 23:54:10.200070
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print("Start human_to_bytes unit test...")
    # bytes
    if human_to_bytes('1b') != 1 or human_to_bytes('1B') != 1 or human_to_bytes('1b', 'b') != 1 or human_to_bytes('1B', 'B') != 1:
        raise ValueError("Test failed for 1b")
    # suffix b
    if human_to_bytes('1b') != 1 or human_to_bytes('2b') != 2 or human_to_bytes('1b', 'b') != 1:
        raise ValueError("Test failed for suffix b")
    # suffix B

# Generated at 2022-06-12 23:54:23.467266
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Kb') == 1000
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('-1') == -1
    assert human_to_bytes('-1', unit='B') == -1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1b', unit='B') == 1
    assert human_to_bytes('1b', isbits=True) == 8
    assert human_to_bytes('1b', isbits=True, unit='B') == 8
    assert human_

# Generated at 2022-06-12 23:54:34.194436
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test 1: list of strings
    result = lenient_lowercase(["a", "B"])
    assert result == ["a", "b"]

    # Test 2: list of strings and integers
    result = lenient_lowercase(["a", 1])
    assert result == ["a", 1]

    # Test 3: list of strings, integers and other data types
    result = lenient_lowercase(["a", 1, "B", object])
    assert result == ["a", 1, "b", object]

    # Test 4: list of strings and None
    result = lenient_lowercase(["a", None])
    assert result == ["a", None]

    # Test 5: None
    result = lenient_lowercase(None)
    assert result is None



# Generated at 2022-06-12 23:54:41.226244
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert(lenient_lowercase(['abcd', 'ABCD', 1234]) == ['abcd', 'abcd', 1234])
    assert(lenient_lowercase(['abcd', 'ABCD', 1234, None]) == ['abcd', 'abcd', 1234, None])
    assert(lenient_lowercase([None]) == [None])


# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:54:49.266547
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([u'A', b'b', 3]) == [u'a', b'b', 3]
    assert lenient_lowercase([u'A', 'b', 3]) == [u'a', 'b', 3]
    assert lenient_lowercase([u'A', 'b']) == [u'a', 'b']
    assert lenient_lowercase(['A', u'b']) == ['a', u'b']
    assert lenient_lowercase(['A', 'b']) == ['a', 'b']
    assert lenient_lowercase([u'A', u'b']) == [u'a', u'b']
    assert lenient_lowercase([u'A']) == [u'a']
    assert lenient_lowercase([u'A', b'b'])

# Generated at 2022-06-12 23:55:02.215476
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print("\n===== Test for function human_to_bytes =====\n")
    print("Test for function with bytes:")
    print("human_to_bytes('10M') = {}".format(human_to_bytes('10M', 'B')))
    print("human_to_bytes('10B') = {}".format(human_to_bytes('10B', 'B')))
    print("human_to_bytes('10Mb') = {}".format(human_to_bytes('10Mb', 'Kb')))
    print("human_to_bytes('10Mb') = {}".format(human_to_bytes('10Mb', 'B')))
    print("human_to_bytes('10MB') = {}".format(human_to_bytes('10MB', 'B')))

# Generated at 2022-06-12 23:55:06.117558
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    input_list = ['URL', 0, '', 'up', 'UPPER', 'lower']
    output_list = lenient_lowercase(input_list)
    assert output_list == ['url', 0, '', 'up', 'upper', 'lower']


# Generated at 2022-06-12 23:55:09.970408
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 12, 'C']) == ['a', 'b', 12, 'c']

# Generated at 2022-06-12 23:55:15.943114
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Test', 'Lowercase']) == ['test', 'lowercase']
    assert lenient_lowercase(['Test', 1]) == ['test', 1]
    assert lenient_lowercase([1, 'Test']) == [1, 'test']
    assert lenient_lowercase([1, 2]) == [1, 2]

# Generated at 2022-06-12 23:55:26.666825
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10B', 'B') == 10
    assert human_to_bytes('10', 'B') == 10
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('1.5K', 'K') == 1536
    assert human_to_bytes('1.5KB') == 1536
    assert human_to_bytes('1.5KB', 'KB') == 1536
    assert human_to_bytes('1.5Kb') == 192
    assert human_to_bytes('1.5Kb', 'Kb') == 192
    assert human_to_bytes('1.5Kb', isbits=True) == 192
    assert human_to

# Generated at 2022-06-12 23:55:37.043181
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:56.640876
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1Z') == 1180591620717411303424
    assert human_to_bytes('1Y') == 1208925819614629174706176
    assert human_to_bytes('2.5K') == 2560
    assert human_to_bytes('2.5M') == 2621440

# Generated at 2022-06-12 23:56:00.296939
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([0, 1, 10.99, "just a string", "second string", None]) == [0, 1, 10.99, 'just a string', 'second string', None]



# Generated at 2022-06-12 23:56:11.480426
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:56:14.718618
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_data = [1, 2, [3, 4], {'a': 'A'}, 'a']
    test_result = lenient_lowercase(test_data)
    assert test_result == [1, 2, [3, 4], {'a': 'A'}, 'a']


# Generated at 2022-06-12 23:56:20.307603
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a']) == ['a']
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase(['A']) == ['a']
    assert lenient_lowercase(['B']) == ['b']


# Generated at 2022-06-12 23:56:25.712148
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["PoWeRfUl", "Punctuation", "Mixed123", 123, ("tuple",), {"somediCtionary": 1}]) == ["powerful", "Punctuation", "Mixed123", 123, ("tuple",), {"somediCtionary": 1}]


# Generated at 2022-06-12 23:56:35.406076
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import sys

    if sys.version_info.major == 2:
        from ansible.compat.tests import unittest
    elif sys.version_info.major == 3:
        from unittest import TestCase as unittest

    class TestSizeConverters(unittest.TestCase):

        def test_human_to_bytes(self):
            PASSED = '\033[92m'
            FAILED = '\033[91m'
            ENDC = '\033[0m'

            test_case_passed = PASSED + 'PASSED' + ENDC
            test_case_failed = FAILED + 'FAILED' + ENDC

            test_result = test_case_passed
            self.assertEqual(human_to_bytes('0'), 0, test_result)

            test

# Generated at 2022-06-12 23:56:42.056756
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1.0) == 1
    assert human_to_bytes(1.5) == 1

    assert human_to_bytes('1K') == 1024
    assert human_to_bytes(1, 'K') == 1024
    assert human_to_bytes(1.0, 'K') == 1024
    assert human_to_bytes(1.5, 'K') == 1536

    assert human_to_bytes('1Kb', True) == 1024
    assert human_to_bytes(1, 'Kb', True) == 1024
    assert human_to_bytes(1.0, 'Kb', True) == 1024

# Generated at 2022-06-12 23:56:44.233907
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['O']) == ['o']
    assert lenient_lowercase([None]) == [None]


# Generated at 2022-06-12 23:56:54.945266
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:16.236612
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' unit test to check if human_to_bytes function converts string format into bytes'''
    assert human_to_bytes('1') == 1, "Bytes conversion failed"
    assert human_to_bytes('1B') == 1, "Bytes conversion failed"
    assert human_to_bytes('1b') == 1, "Bytes conversion failed"
    assert human_to_bytes('1KB') == 1024, "KBytes conversion failed"
    assert human_to_bytes('1Kb', isbits=True) == 1024, "Kbits conversion failed"
    assert human_to_bytes('1Mb', isbits=True) == 1048576, "Mbits conversion failed"
    assert human_to_bytes('1MB') == 1048576, "MBytes conversion failed"

# Generated at 2022-06-12 23:57:23.238625
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    assert human_to_bytes('-1MB') == -1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1YB') == 1208925819614629174706176
    assert human_to_bytes('1Y') == 1208925819614629174706176
    assert human_to_bytes('1e2') == 100
    assert human_to_bytes(100, 'KB') == 102400

    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1K') == 1024
    assert human_to

# Generated at 2022-06-12 23:57:25.377661
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print(human_to_bytes('1G'))
    print(human_to_bytes('1G', 'M'))
    print(human_to_bytes('1Mb', True))



# Generated at 2022-06-12 23:57:31.536931
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Empty list
    l1 = []
    assert lenient_lowercase(l1) == []

    # List with only str elements
    l2 = ['A', 'B', 'C']
    assert lenient_lowercase(l2) == ['a', 'b', 'c']

    # List with only unicode elements
    l3 = [u'foo', u'bar', u'baz']
    assert lenient_lowercase(l3) == [u'foo', u'bar', u'baz']

    # List with only non-string elements
    l4 = [123, 456, 789]
    assert lenient_lowercase(l4) == [123, 456, 789]

    # Mixed list

# Generated at 2022-06-12 23:57:38.031089
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'b', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 'a', 2]) == [1, 'a', 2]
    assert lenient_lowercase({'a': 1, 'B': 2}) == {'a': 1, 'B': 2}
    assert lenient_lowercase(1) == 1
    assert lenient_lowercase('a') == 'a'
    assert lenient_lowercase(True) == True



# Generated at 2022-06-12 23:57:40.260672
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['asdf', u'fdsA', 9]) == ['asdf', 'fdsA', 9]

# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:57:47.011080
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['foo', 2, 'bar']) == ['foo', 2, 'bar']
    assert lenient_lowercase(['FOO', 2, 'BAR']) == ['foo', 2, 'bar']
    assert lenient_lowercase(['FOO', 'bar', 2]) == ['foo', 'bar', 2]
    assert lenient_lowercase(['FOO', 'BAR', 2]) != ['foo', 'BAR', 2]



# Generated at 2022-06-12 23:57:55.067286
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """ Unit test for human_to_bytes() """
    import pytest
    # test cases, expected result and message

# Generated at 2022-06-12 23:58:07.798731
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # default cases - bytes
    assert human_to_bytes('10M') == human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes('1') == 1
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10b') == 1
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('10.1') == 10
    assert human_to_bytes(1) == 1

    # bytes with units
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1k') == human_to_bytes(1, 'k') == 1024
    assert human_to_bytes('1K') == human_to_bytes(1, 'K') == 1024

# Generated at 2022-06-12 23:58:18.963473
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1MB') == 1048576, "human_to_bytes('1MB') returns %d" % human_to_bytes('1MB')
    assert human_to_bytes('1MB', default_unit='B') == 1048576, "human_to_bytes('1MB', default_unit='B') returns %d" % human_to_bytes('1MB', default_unit='B')
    assert human_to_bytes('1M', 'B') == 1048576, "human_to_bytes('1M', 'B') returns %d" % human_to_bytes('1M', 'B')
    assert human_to_bytes('1Mb') == 1048576, "human_to_bytes('1Mb') returns %d" % human_to_bytes('1Mb')
    assert human_to