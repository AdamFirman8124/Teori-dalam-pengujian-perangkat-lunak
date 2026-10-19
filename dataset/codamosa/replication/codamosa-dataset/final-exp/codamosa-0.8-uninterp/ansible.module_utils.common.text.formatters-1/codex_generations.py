

# Generated at 2022-06-12 23:48:50.785426
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Testing human_to_bytes() with various inputs. '''
    print("***")
    print("*** Testing human_to_bytes() function")
    print("***")


# Generated at 2022-06-12 23:48:59.328620
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Create test cases with elements of different data types.
    test_cases = [
        ['A', 'B', 'c'],
        ['a', 'B', 'c'],
        ['a', 'B', 'C'],
        ['a', 'b', 'c'],
        ['a', 'b', 'c', 1, 2.0, False],
        [1, 2.0, False, 'a', 'b', 'c'],
        [1, 2.0, False, 'A', 'B', 'c'],
        [1, 2.0, False, 'A', 'b', 'c'],
        [1, 2.0, False, 'a', 'B', 'c'],
    ]

# Generated at 2022-06-12 23:49:02.293857
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 25, 'B']) == ['a', 25, 'B']

# Unit tests for human_to_bytes function

# Generated at 2022-06-12 23:49:10.884553
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

    # Assert correct conversion from number to bytes.
    assert human_to_bytes(5) == 5
    assert human_to_bytes(5.4) == 5
    assert human_to_bytes('5') == 5
    assert human_to_bytes('5.4') == 5
    assert human_to_bytes(' 5 ') == 5
    assert human_to_bytes('5.4 ') == 5

    # Assert correct conversion from string to bytes.
    assert human_to_bytes('5b') == 5
    assert human_to_bytes('5.B') == 5
    assert human_to_bytes(' 5 B') == 5
    assert human_to_bytes('5.4 b') == 5
    assert human_to_bytes('5.4b') == 5

# Generated at 2022-06-12 23:49:16.477274
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:27.978862
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K', isbits=True) == 8192
    assert human_to_bytes('1k', isbits=True) == 8192
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1b', isbits=False) == 1
    assert human_to_bytes('1kb', isbits=True) == 8192
    assert human_to_bytes('1kb', isbits=False) == 1024
    assert human_to_bytes('1mb', isbits=True) == 8388608
    assert human_to_bytes('1m', isbits=False) == 1048576

# Generated at 2022-06-12 23:49:35.454132
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from pytest import raises

    assert human_to_bytes('') == 0

    assert human_to_bytes('1') == 1
    assert human_to_bytes('1') == human_to_bytes(1)

    # Test case when byte identifier was explicitly passed
    assert human_to_bytes(10, 'B') == 10
    assert human_to_bytes(1000, 'B') == 1000

    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1.5B') == 2

    # Test case when kb identifier was explicitly passed
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'k') == 10240
    assert human_to_bytes(1000, 'K') == 1024000

# Generated at 2022-06-12 23:49:40.766076
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print('Testing human_to_bytes()')
    if human_to_bytes('1M') != 1048576:
        raise ValueError('human_to_bytes() failed expected 1048576 got {0}'.format(human_to_bytes('1M')))
    if human_to_bytes('1Mb', isbits=True) != 1048576:
        raise ValueError('human_to_bytes() failed expected 1048576 got {0}'.format(human_to_bytes('1M', isbits=True)))
    if human_to_bytes(1, 'MB') != 1048576:
        raise ValueError('human_to_bytes() failed expected 1048576 got {0}'.format(human_to_bytes(1, 'MB')))

# Generated at 2022-06-12 23:49:50.981822
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import sys

    # check bytes

# Generated at 2022-06-12 23:49:55.112794
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    my_list = [3, '4', '5']
    assert [3, '4', '5'] == lenient_lowercase(my_list)
    my_list = ['foo', 3, 'bar', 'BAZ']
    assert ['foo', 3, 'bar', 'baz'] == lenient_lowercase(my_list)


# Generated at 2022-06-12 23:50:03.121750
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c'], 'Mismatch: expected ["a", "b", "c"]'
    # Nested lists/dicts
    assert lenient_lowercase(['A', 'B', {'C': 'D'}]) == ['a', 'b', {'C': 'D'}], 'Mismatch: expected ["a", "b", {"C": "D"}]'



# Generated at 2022-06-12 23:50:07.233304
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["a", 1, 2]) == ["a", 1, 2]
    assert lenient_lowercase(["a", "B", "c"]) == ["a", "b", "c"]



# Generated at 2022-06-12 23:50:17.948675
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['B', 'b']) == ['b', 'b']
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase([1.4, 2.4]) == [1.4, 2.4]
    assert lenient_lowercase(['B', 'b', 1, 2, 1.4, 2.4]) == ['b', 'b', 1, 2, 1.4, 2.4]

    lst = ['B', 1, 'b', 'a', 'B', 2.4]
    assert lenient_lowercase(lst) == ['b', 1, 'b', 'a', 'b', 2.4]
    assert lst != lenient_lowercase(lst)


# Generated at 2022-06-12 23:50:27.835508
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:50:34.087863
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1B', isbits=True) == 1
    assert human_to_bytes('2KB') == 2 * 1024
    assert human_to_bytes('2Kb', isbits=True) == 2 * 1024
    assert human_to_bytes('10MB') == 10 * 1024 * 1024
    assert human_to_bytes('10Mb', isbits=True) == 10 * 1024 * 1024
    assert human_to_bytes('3GB') == 3 * 1024 * 1024 * 1024
    assert human_to_bytes('3Gb', isbits=True) == 3 * 1024 * 1024 * 1024
    assert human_to_bytes('1TB') == 1 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('1Tb', isbits=True) == 1

# Generated at 2022-06-12 23:50:39.445400
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['aBc', 'DEf', 123]) == ['abc', 'def', 123]
    assert lenient_lowercase(['aBc', 'DEf', 'GHI']) == ['abc', 'def', 'ghi']
    assert lenient_lowercase(['aBc', 'DEf', 'ghi']) == ['abc', 'def', 'ghi']



# Generated at 2022-06-12 23:50:50.457484
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Test function human_to_bytes() with input variants '''

    # Test values
    value_int = 1
    value_int_str = '1'
    value_float = 1.2
    value_float_str = '1.2'
    value_mix = '1.2K'

    # Test bytes unit
    unit_B_upper = 'B'
    unit_B_lower = 'b'
    unit_multi_B_upper = 'KB'
    unit_multi_B_lower = 'Kb'
    unit_multi_B_upper_value = '1KB'
    unit_multi_B_lower_value = '1Kb'

    # Test bits unit
    unit_b_upper = 'B'
    unit_b_lower = 'b'

# Generated at 2022-06-12 23:51:01.206437
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2Kb') == 2048
    assert human_to_bytes('2k') == 2048
    assert human_to_bytes('2kb') == 2048

    assert human_to_bytes('2K', isbits=True) == 16384
    assert human_to_bytes('2Kb', isbits=True) == 16384
    assert human_to_bytes('2k', isbits=True) == 16384
    assert human_to_bytes('2kb', isbits=True) == 16384

    assert human_to_bytes('2M') == 2097152
    assert human_to_bytes('2Mb') == 2097152
    assert human_to_bytes('2m') == 2097152

# Generated at 2022-06-12 23:51:03.483460
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['foo', 'Bar', 10, 'Baz']) == ['foo', 'bar', 10, 'baz']



# Generated at 2022-06-12 23:51:14.693250
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print("Testing human_to_bytes()")
    try:
        print("Testcase 1 - '10M' - success")
        assert(human_to_bytes('10M') == 10485760)
    except Exception as e:
        print("Testcase 1 - '10M' - failed: %s" % str(e))

    try:
        print("Testcase 2 - '10M' + 'G' - success")
        assert(human_to_bytes('10M', 'G') == 10485760)
    except Exception as e:
        print("Testcase 2 - '10M' + 'G' - failed: %s" % str(e))


# Generated at 2022-06-12 23:51:26.026277
# Unit test for function bytes_to_human
def test_bytes_to_human():
    import unittest

    class UnitTestBytesToHuman(unittest.TestCase):

        def test_bytes_to_human(self):
            """
            Testing bytes_to_human function
            """

# Generated at 2022-06-12 23:51:34.687724
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(2.5) == '2.50 Bytes'
    assert bytes_to_human(10) == '10.00 Bytes'
    assert bytes_to_human(10, unit='b') == '80.00 bits'
    assert bytes_to_human(10, unit='b', isbits=True) == '80.00 bits'
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1048576) == '1.00 MB'
    assert bytes_to_human(1073741824) == '1.00 GB'
    assert bytes_to_human(1099511627776) == '1.00 TB'

# Generated at 2022-06-12 23:51:44.294914
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Simple test
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes(1.5) == 1

    # K unit test
    # KB return
    assert human_to_bytes('2K') == 2048
    # Not supported case, ValueError raised
    try:
        human_to_bytes('2k')
    except ValueError as e:
        assert re.search(r'diff in case', str(e))

    # MB return
    assert human_to_bytes('2MB') == 2 * 1024 * 1024
    # MB return
    assert human_to_bytes('1.9MB') == 1900 * 1024

    # GB return
    assert human_to_bytes('2GB') == 2 * 1024 * 1024 * 1024
    # GB return


# Generated at 2022-06-12 23:51:50.072787
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['b', 'a', 'c'] == lenient_lowercase(['B', 'a', 'C'])
    assert ['b', (1, 2), 'c'] == lenient_lowercase(['B', (1, 2), 'C'])
    assert ['b', {1: 2}, 'c'] == lenient_lowercase(['B', {1: 2}, 'C'])

# Generated at 2022-06-12 23:51:57.073709
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(10) == "10.00 Bytes"
    assert bytes_to_human(10, unit='B') == "10.00 Bytes"
    assert bytes_to_human(10, unit='b') == "10.00 bits"
    assert bytes_to_human(10, isbits=True) == "10.00 bits"
    assert bytes_to_human(10, isbits=True, unit='b') == "10.00 bits"
    assert bytes_to_human(10, isbits=True, unit='B') == "10.00 Bytes"



# Generated at 2022-06-12 23:52:07.988374
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(0) == '0 Bytes'
    assert bytes_to_human(1) == '1 Byte'
    assert bytes_to_human(10) == '10 Bytes'
    assert bytes_to_human(11) == '11 Bytes'
    assert bytes_to_human(1000) == '1000 Bytes'
    assert bytes_to_human(100000) == '97.66 KB'
    assert bytes_to_human(1100000) == '1.05 MB'
    assert bytes_to_human(1100000000) == '1.02 GB'
    assert bytes_to_human(1.1) == '1.10 Bytes'
    assert bytes_to_human(1.11) == '1.11 Bytes'

# Generated at 2022-06-12 23:52:18.734848
# Unit test for function human_to_bytes
def test_human_to_bytes():
    for value in ['2k', '2K', '2Kb', '2KB']:
        assert human_to_bytes(value, 'B') == 2048, "failed to convert {}. {} is not 2048 but {}".format(value, value, human_to_bytes(value, 'B'))
    for value in ['2m', '2M', '2Mb', '2MB']:
        assert human_to_bytes(value, 'B') == 2097152, "failed to convert {}. {} is not 2097152 but {}".format(value, value, human_to_bytes(value, 'B'))
    for value in ['2Kb', '2KB', '2k', '2K']:
        assert human_to_bytes(value, 'b') == 2048, "failed to convert {}. {} is not 2048 but {}".format

# Generated at 2022-06-12 23:52:28.086437
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit test for function human_to_bytes."""
    from nose.tools import ok_, eq_
    eq_(human_to_bytes(1, 'b'), 1)
    eq_(human_to_bytes('1', 'b'), 1)
    eq_(human_to_bytes('10', 'b'), 10)
    eq_(human_to_bytes('1.5', 'b'), 1.5)
    eq_(human_to_bytes('1.5B'), 1.5)
    eq_(human_to_bytes('1.5B', 'B'), 1.5)
    eq_(human_to_bytes('1.5b'), 1.5)
    eq_(human_to_bytes('1.5b', 'b'), 1.5)

# Generated at 2022-06-12 23:52:38.877799
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # 10MB
    mb = human_to_bytes('10M')
    if mb == 10485760:
        print('test_human_to_bytes() - success')
    else:
        print('test_human_to_bytes() - error: returned %s instead of 10485760' % mb)

    # 1GB
    gb = human_to_bytes('1G')
    if gb == 1073741824:
        print('test_human_to_bytes() - success')
    else:
        print('test_human_to_bytes() - error: returned %s instead of 1073741824' % gb)

    # 1TB with lowercase unit
    tb = human_to_bytes('1T')

# Generated at 2022-06-12 23:52:47.269727
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit test for function human_to_bytes."""
    # unit test case for each entry of SIZE_RANGES
    for unit, value in iteritems(SIZE_RANGES):
        # test 1: plain unit when value is 1
        human_to_bytes(unit)
        # test 2: 'K' when value is 1
        human_to_bytes('K')
        # test 3: plain unit when value is 1000
        human_to_bytes(unit, default_unit='K')
        # test 4: 'K' when value is 1000
        human_to_bytes('K', default_unit='K')

    # test 5: 'K' to bytes when value is 1
    assert human_to_bytes('K', default_unit='B') == 1000
    # test 6: 'K' to bits when value is 1

# Generated at 2022-06-12 23:52:58.761565
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test bytes
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 8388608  # error, string bits representation was passed so bytes was returned
    assert human_to_bytes('1Meg') == 1048576  # error, string bits representation was passed so bytes was returned
    assert human_to_bytes(1, 'M') == 1048576
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes(1.5, 'M') == 1572864
    assert human_to_bytes('17mb') == 1769472  # error, string bits representation was passed so bytes was returned
    assert human_to_bytes('17mb', isbits=True) == 137711872
    assert human_to_bytes

# Generated at 2022-06-12 23:53:00.218404
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a', 'b', 1, 2] == lenient_lowercase(['A', 'B', 1, 2])
    assert ['a', 'b'] == lenient_lowercase(['A', 'B'])



# Generated at 2022-06-12 23:53:02.266942
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['Foo', 'Bar', 1234]
    lower_case_list = lenient_lowercase(lst)
    assert lower_case_list == ['foo', 'bar', 1234]


# Unit test human_to_bytes

# Generated at 2022-06-12 23:53:14.205493
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:23.030723
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Simple unit test for human_to_bytes() '''

# Generated at 2022-06-12 23:53:28.888340
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Test human_to_bytes function and its powers '''
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10B', default_unit='B') == 10
    assert human_to_bytes('10', default_unit='B') == 10
    assert human_to_bytes('10B', default_unit='MB') == 10
    assert human_to_bytes('10', default_unit='MB') == 10
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('10MB', default_unit='MB') == 10485760
    assert human_to_bytes('10MB', default_unit='M') == 10485760
    assert human_to

# Generated at 2022-06-12 23:53:39.669302
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1.5G') == 1610612736
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1.5T') == 1649267441664
    assert human_to_bytes('1P') == 1125899906842624

# Generated at 2022-06-12 23:53:48.215196
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('10B') == 10
    assert human_to_bytes(10) == 10
    assert human_to_bytes('1KB') == 1000
    assert human_to_bytes('10MB') == 10000000
    assert human_to_bytes('1.5MB') == 1500000
    assert human_to_bytes('1Mb') == 125000
    assert human_to_bytes('1Mb', isbits=True) == 125000
    assert human_to_bytes('10Gb') == 12500000
    assert human_to_bytes(10, 'Gb') == 12500000
    assert human_to_bytes('1Gb', unit='Mb', isbits=True) == 125000

# Generated at 2022-06-12 23:53:59.603177
# Unit test for function human_to_bytes
def test_human_to_bytes():
    number = '2K'
    assert human_to_bytes(number) == human_to_bytes(2, 'K')

    number = '2'
    assert human_to_bytes(number) == 2

    number = '2.1B'
    assert human_to_bytes(number) == human_to_bytes(2.1, 'B')

    number = '2.1'
    assert human_to_bytes(number) == 2

    number = '2.1K'
    assert human_to_bytes(number) == 2200

    number = '2.1KB'
    assert human_to_bytes(number) == 2200

    number = '2.1Kb'
    assert human_to_bytes(number, isbits=True) == 2200

    number = '2.1KBb'

# Generated at 2022-06-12 23:54:07.124712
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a']) == ['a']
    assert lenient_lowercase([123]) == [123]
    assert lenient_lowercase(['a', 'b', 'c', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]
    assert lenient_lowercase(['A', 'B', 'C', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]

# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:54:22.652772
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["abc", "def", 1]) == ["abc", "def", 1]
    assert lenient_lowercase([]) == []


# Unit tests for function human_to_bytes
test_strings = [
    ('1M', 1048576),
    ('1MB', 1048576),
    ('100000', 100000),
    ('100K', 102400),
    ('1KB', 1024),
    ('1', 1),
    ('0', 0),
    ('1Mb', 131072),
    ('1Kb', 128),
    ('1GB', 1073741824),
    ('1.1GB', 1.1 * 1073741824),
]


# Generated at 2022-06-12 23:54:33.779471
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2k') == 2048
    assert human_to_bytes('1Kb') == 8192
    assert human_to_bytes('2kb') == 16384
    assert human_to_bytes('2KB') == 16384
    assert human_to_bytes('2KIB') == 2048
    assert human_to_bytes('2KiB') == 2048
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2K', isbits=True) == 16384

    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=True) == 8388608
    assert human_to_bytes('1MB') == 1048

# Generated at 2022-06-12 23:54:43.721774
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test the case of all uppercase string
    test_string = 'TEST'
    assert(lenient_lowercase([test_string]) == ['test'])
    # Test the case of all lowercase string
    test_string = 'test'
    assert(lenient_lowercase([test_string]) == ['test'])
    # Test the case of mixed case string
    test_string = 'TeSt'
    assert(lenient_lowercase([test_string]) == ['test'])
    # Test the case that a number is in the list
    assert(lenient_lowercase(['TeSt', 1]) == ['test', 1])



# Generated at 2022-06-12 23:54:47.871530
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([1, 'foo', [3]]) == [1, 'foo', [3]]
    assert lenient_lowercase(['Foo', 'BaR', 'BaZ']) == ['foo', 'bar', 'baz']



# Generated at 2022-06-12 23:54:53.271008
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase([1]) == [1]
    assert lenient_lowercase(['', 1]) == ['', 1]
    assert lenient_lowercase(['A', 1, 'B']) == ['a', 1, 'b']



# Generated at 2022-06-12 23:55:00.349394
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert isinstance(lenient_lowercase(['Abc']), list)
    assert lenient_lowercase(['ABC']) == ['abc']
    assert lenient_lowercase(['ABC', 'DEF']) == ['abc', 'def']
    assert lenient_lowercase(['ABC', 'DEF', 123]) == ['abc', 'def', 123]
    assert lenient_lowercase(['ABC', 'DEF', 'GHI']) != ['abc', 'def', 'ghi']

# Generated at 2022-06-12 23:55:08.907144
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print("test_human_to_bytes(): ")
    print("    human_to_bytes('10M'): ", human_to_bytes('10M'))
    print("    human_to_bytes('2Kb'): ", human_to_bytes('2Kb'))
    print("    human_to_bytes(10, 'M'): ", human_to_bytes(10, 'M'))
    print("    human_to_bytes(2, 'Kb', True): ", human_to_bytes(2, 'Kb', True))
    print("    human_to_bytes(10): ", human_to_bytes(10))



# Generated at 2022-06-12 23:55:19.766424
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Tests for function bytes_to_human()
    assert human_to_bytes('10M') == human_to_bytes(10, 'M')
    assert human_to_bytes('1MB') == human_to_bytes(1, 'M')
    assert human_to_bytes('10mB') == human_to_bytes(10, 'M')
    assert human_to_bytes('1m') == human_to_bytes(1, 'm')
    assert human_to_bytes('1Mb') == human_to_bytes(1, 'M', isbits=True)
    assert human_to_bytes('1b') == human_to_bytes(1, 'b', isbits=True)

    # Test for exception

# Generated at 2022-06-12 23:55:25.935191
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # test for correct behaviour for good input
    assert lenient_lowercase([1, 2, 3, 'A', 'B', 'C']) == [1, 2, 3, 'a', 'b', 'c']
    # test for correct behaviour for bad input
    assert lenient_lowercase([1, 2, 3, [1, 2], {'a': 1}, 'B']) == [1, 2, 3, [1, 2], {'a': 1}, 'b']

# Generated at 2022-06-12 23:55:27.702145
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 1]) == ['a', 'b', 1]


# Generated at 2022-06-12 23:55:42.296331
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('0.1m') == 100000
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('100') == 100
    assert human_to_bytes('1.5MB') == 1572864
    assert human_to_bytes('100b') == 0
    assert human_to_bytes('100bits') == 0

# Generated at 2022-06-12 23:55:50.356811
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import unittest

    class TestHumanToBytes(unittest.TestCase):
        def test_bytes(self):
            self.assertEqual(human_to_bytes('1B'), 1)
            self.assertEqual(human_to_bytes('1b'), 1)
            self.assertEqual(human_to_bytes('1B', isbits=True), 1)

        def test_kilobytes(self):
            self.assertEqual(human_to_bytes('1K'), 1024)
            self.assertEqual(human_to_bytes('1KB'), 1024)
            self.assertEqual(human_to_bytes('1k'), 1024)
            self.assertEqual(human_to_bytes('1kb', isbits=True), 1024)

        def test_megabytes(self):
            self.assertE

# Generated at 2022-06-12 23:56:01.298278
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test without any element to lower and without error
    # Assert: All values stay the same
    list = [1, 2, 3]
    list_expected = [1, 2, 3]
    assert lenient_lowercase(list) == list_expected

    # Test with lower element without error
    # Assert: All values are lower
    list = ["A", "B", "C"]
    list_expected = ["a", "b", "c"]
    assert lenient_lowercase(list) == list_expected

    # Test with upper and lower element without error
    # Assert: All values are lower
    list = ["a", "B", "C"]
    list_expected = ["a", "b", "c"]
    assert lenient_lowercase(list) == list_expected

    # Test with non string element without error
   

# Generated at 2022-06-12 23:56:12.166307
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test human_to_bytes for bits and bytes.
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1KB') == 1000
    assert human_to_bytes('1KB', isbits=True) == 8000
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1M', 'M') == 1000000
    assert human_to_bytes(10, 'M') == 10000000
    assert human_to_bytes(10, 'M', isbits=True) == 80000000
    assert human_to_bytes(10.0, 'M') == 10000000.0
    assert human_to_bytes(10.0, 'M', isbits=True) == 80000000.0
    # test ValueError

# Generated at 2022-06-12 23:56:18.672768
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["A", "B"]) == ["a", "b"]
    assert lenient_lowercase(["A", "B", 1, 2]) == ["a", "b", 1, 2]
    assert lenient_lowercase(["A", "B", 1, "C"]) == ["a", "b", 1, "C"]


# Generated at 2022-06-12 23:56:27.023362
# Unit test for function human_to_bytes
def test_human_to_bytes():
    test_data = {
        '1.1Mb': 1100000,
        '20M': 20971520,
        '20Mb': 20000000,
        '20MB': 20971520,
        '1.1Kb': 1100,
        '1.1K': 1126,
        '20K': 20480,
        '20Kb': 20000,
        '20KB': 20480,
        '1.1b': 1,
        '11b': 11,
        '20': 20,
        '0.1': 0,
        '1.1': 2,
    }
    for test in test_data:
        assert(human_to_bytes(test, 'b', True) == test_data[test])

# Generated at 2022-06-12 23:56:36.134726
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import json


# Generated at 2022-06-12 23:56:44.349658
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    '''Test to see if all elements in a list have been lowercased, if they 
    are strings'''
    lst1 = ['a', 'b']
    lst2 = ['x', 'y', 'z']
    lst3 = [1, 2]
    lst4 = ['A']
    lst5 = ['a', 'B']
    lst6 = [1, 'B', 'C']

    test_dict = {lst1: ['a', 'b'],
                 lst2: ['x', 'y', 'z'],
                 lst3: [1, 2],
                 lst4: ['a'],
                 lst5: ['a', 'b'],
                 lst6: [1, 'b', 'c']}


# Generated at 2022-06-12 23:56:55.026974
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(1) == 1
    assert human_to_bytes(10) == 10

    assert human_to_bytes('1K') == 1 * (1 << 10)
    assert human_to_bytes('2K') == 2 * (1 << 10)

    assert human_to_bytes('1M') == 1 * (1 << 20)
    assert human_to_bytes('2M') == 2 * (1 << 20)

    assert human_to_bytes('1G') == 1 * (1 << 30)
    assert human_to_bytes('2G') == 2 * (1 << 30)

    assert human_to_bytes('1T') == 1 * (1 << 40)
    assert human_to_bytes('2T') == 2 * (1 << 40)

    assert human_to_bytes('1P') == 1

# Generated at 2022-06-12 23:57:02.924842
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10') == 10
    assert human_to_bytes(10) == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes(10, 'B') == 10
    assert human_to_bytes('10B', 'B') == 10
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes(1, 'k') == 1024
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1.1MB') == 1126400
    assert human_to

# Generated at 2022-06-12 23:57:25.357145
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # List of test input and expected output values
    test_list = [
        (['a', 'B', 'C', 'd'], ['a', 'b', 'c', 'd']),
        (['a', 'B', 1, 'd'], ['a', 'b', 1, 'd']),
        (1, 1),
        (['1', 2, 'a!', 'B'], ['1', 2, 'a!', 'b']),
    ]
    for test_input, expected_result in test_list:
        actual_result = lenient_lowercase(test_input)
        assert actual_result == expected_result


# Generated at 2022-06-12 23:57:27.364256
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase(['A', 1, 'C']) == ['a', 1, 'c']

# Generated at 2022-06-12 23:57:32.690259
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1a') == 1
    assert human_to_bytes('1a', unit='B') == 1
    assert human_to_bytes('1a', unit='KB') == 1024
    assert human_to_bytes('1a', unit='Kb') == 1024 * 8
    assert human_to_bytes('1a', unit='b') == 1 * 8
    assert human_to_bytes('1.1a', unit='KB') == 1152
    assert human_to_bytes('1.1a', unit='Kb') == 1152 * 8
    assert human_to_bytes('1.1a', unit='b') == 1.1 * 8
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1K', unit='B') == 1024
    assert human_to_bytes

# Generated at 2022-06-12 23:57:42.870205
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    This function tests human_to_bytes() and bytes_to_human()
    by passing specific strings into the first function, comparing the
    output against known results, and passing the output of the first
    function into the second and comparing the output against the original
    strings that were passed in.
    '''

    test_dict = dict()

    test_dict['5M'] = 5242880
    test_dict['5K'] = 5120
    test_dict['5G'] = 5368709120
    test_dict['5T'] = 5497558138880
    test_dict['4Mb'] = 4194304
    test_dict['4Kb'] = 4096
    test_dict['4Gb'] = 4294967296
    test_dict['4Tb'] = 4398046511104
    test_

# Generated at 2022-06-12 23:57:52.423351
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # common test part
    data = (
        ('1.1M', 1048576 * 1.1),
        ('1024', 1024),
        ('1K', 1024),
        ('1M', 1048576),
        ('1G', 1073741824),
        ('1T', 1099511627776),
        ('1P', 1125899906842624),
        ('1E', 1152921504606846976),
        ('1Z', 1180591620717411303424),
        ('1Y', 1208925819614629174706176),
        ('1.1Mb', 1048576 * 1.1 / 8),
        ('1.1M', 1048576 * 1.1),
        ('1.1K', 1024 * 1.1),
    )
    # bytes test part

# Generated at 2022-06-12 23:58:05.172282
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576

    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1Mb') == 1048576

    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to_bytes('1M', isbits=True) == 1048576

    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    #assert human_to_bytes('1Kb', isbits=False) == 1024  # this will raise error
    #assert human_to_bytes('1Mb', isbits=False) == 1048576  # this will raise error

# Generated at 2022-06-12 23:58:12.273646
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    from ansible.module_utils.basic import AnsibleModule
    import json

    xml_true = "<xml></xml>"
    xml_false = "<XML></XML>"
    xml_false2 = "<Xml></XML>"
    xml_false3 = "<xml></Xml>"

    mixed = [xml_true, xml_false, xml_false2, xml_false3]

    mixed_result = lenient_lowercase(mixed)

    module = AnsibleModule(argument_spec={'xml': {'type': 'list'}})
    module.exit_json(changed=False, meta=mixed_result)


# Generated at 2022-06-12 23:58:22.600782
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10MB', isbits=True) == 8388608
    assert human_to_bytes('10Mb', isbits=True) == 8388608
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10b', isbits=True) == 10
    assert human_to_bytes('10') == 10
    assert human_to_bytes(10, unit='b') == 10
    assert human_to_bytes(10, unit='B') == 10

# Generated at 2022-06-12 23:58:24.034706
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Test', 'Another', 5]) == ['test', 'another', 5]

# Generated at 2022-06-12 23:58:28.667101
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    items = ['a', 'A', 1]
    result = lenient_lowercase(items)
    assert isinstance(result, list)
    assert len(result) == 3
    assert 'a' in result
    assert 'A' not in result
    assert 1 in result