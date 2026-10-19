

# Generated at 2022-06-12 23:48:55.394132
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test invalid human
    invalid_human_sum = [
        '',
        0,
    ]
    for human in invalid_human_sum:
        try:
            human_to_bytes(human)
        except ValueError:
            pass
        else:
            assert False, "human_to_bytes() for human %s should be raised ValueError" % human

    # Test isbits and unit
    human_sum = [
        ('0 MB', 0, None, 0),
        ('10 MB', 10, None, 10485760),
        ('10.2 Mb', 10.2, None, 10485760),
        ('10.2 Mb', 10.2, 'MB', 10547178.24),
        ('10.2 Mb', 10.2, 'Mb', 10485760),
    ]


# Generated at 2022-06-12 23:49:06.308365
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:13.038325
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # check that function returns an error if input is None
    try:
        human_to_bytes(None)
    except ValueError:
        pass
    else:
        assert(False)

    # check that function returns an error if input not a string
    try:
        human_to_bytes(2)
    except ValueError:
        pass
    else:
        assert(False)

    # check that function returns an error if input is an empty string
    try:
        human_to_bytes('')
    except ValueError:
        pass
    else:
        assert(False)

    assert(human_to_bytes('1') == 1)
    assert(human_to_bytes('2.5') == 2)
    assert(human_to_bytes('10K') == 10240)

# Generated at 2022-06-12 23:49:20.769408
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(0) == '0.00 Bytes'
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(10) == '10.00 Bytes'
    assert bytes_to_human(100) == '100.00 Bytes'
    assert bytes_to_human(1000) == '1000.00 Bytes'
    assert bytes_to_human(1024) == '1.00 KBytes'
    assert bytes_to_human(10 * 1024) == '10.00 KBytes'
    assert bytes_to_human(100 * 1024) == '100.00 KBytes'
    assert bytes_to_human(1000 * 1024) == '1000.00 KBytes'
    assert bytes_to_human(1024 ** 2) == '1.00 MBytes'
   

# Generated at 2022-06-12 23:49:22.841416
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 123, 'D']) == ['a', 'b', 123, 'd']



# Generated at 2022-06-12 23:49:33.379606
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Tests for human_to_bytes()."""


# Generated at 2022-06-12 23:49:43.806807
# Unit test for function bytes_to_human
def test_bytes_to_human():
    # test convert bytes to human-readable format
    assert bytes_to_human(1, False) == '1.00 Bytes'
    assert bytes_to_human(1, False, 'b') == '1.00 Bytes'
    assert bytes_to_human(10, False) == '10.00 Bytes'
    assert bytes_to_human(10, False, 'b') == '10.00 Bytes'
    assert bytes_to_human(1024, False) == '1.00 KB'
    assert bytes_to_human(1024, False, 'b') == '1.00 KB'
    assert bytes_to_human(1048576, False) == '1.00 MB'
    assert bytes_to_human(1048576, False, 'b') == '1.00 MB'

# Generated at 2022-06-12 23:49:53.895231
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1Z', default_unit='B') == 1 << 70
    assert human_to_bytes(1, 'Y') == 1 << 80
    assert human_to_bytes('1.5 ZB') == 1.5 * (1 << 70)
    assert human_to_bytes('.5Z', default_unit='B') == .5 * (1 << 70)
    assert human_to_bytes(2, 'Z') == 2 * (1 << 70)
    assert human_to_bytes('200', 'Y') == 200 * (1 << 80)
    assert human_to_bytes(100, 'K') == 100 * 1024
    assert human_to_bytes('100', 'y') == 100 * (1 << 80)

    assert human_to_bytes('10b', isbits=True) == 10
    assert human

# Generated at 2022-06-12 23:49:58.680735
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([None, 'A', 1]) == [None, 'a', 1]
    assert lenient_lowercase(['A', None, 1]) == ['a', None, 1]
    assert lenient_lowercase([None, 'A', 1, 'B']) == [None, 'a', 1, 'b']
    assert lenient_lowercase(['A', None, 1, 'B']) == ['a', None, 1, 'b']


# Generated at 2022-06-12 23:50:07.145909
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test list of string
    test_list = ['a', 'B', 'C', 'd', 'E', 'f']
    assert lenient_lowercase(test_list) == ['a', 'b', 'c', 'd', 'e', 'f']

    # Test list with one element different
    test_list = ['a', 1, 'C', 'd', 'E', 'f']
    assert lenient_lowercase(test_list) == ['a', 1, 'c', 'd', 'e', 'f']

    # Test list with another element different
    test_list = ['a', 'B', 2, 'd', 'E', 'f']
    assert lenient_lowercase(test_list) == ['a', 'b', 2, 'd', 'e', 'f']

    # Test list with yet another element different


# Generated at 2022-06-12 23:50:18.146933
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1M', unit='M') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=True) == 8388608
    assert human_to_bytes('1.1Mb', isbits=True) == 1153433


# Generated at 2022-06-12 23:50:24.278970
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print("=== TESTING HUMAN_TO_BYTES === \n")

    def test_with_default_unit(number, default_unit, expected, isbits=False):
        actual = human_to_bytes(number, default_unit=default_unit, isbits=isbits)
        if actual == expected:
            print("test_with_default_unit(number='%s', default_unit='%s'): OK" % (number, default_unit))
        else:
            print("test_with_default_unit(number='%s', default_unit='%s'): FAIL, expected %s but got %s" % (number, default_unit, expected, actual))


# Generated at 2022-06-12 23:50:35.211326
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:50:37.360651
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ABC', '123', 'xyz']) == ['abc', '123', 'xyz']


# Generated at 2022-06-12 23:50:39.331059
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    expected = lenient_lowercase(["ABC", 123, None])
    assert len(expected) == 3
    assert expected[0] == "abc"
    assert expected[1] == 123
    assert expected[2] is None



# Generated at 2022-06-12 23:50:45.241628
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1, 'b') == 1
    assert human_to_bytes(1, 'b', isbits=True) == 1
    assert human_to_bytes(10, 'b') == 10
    assert human_to_bytes(10, 'b', isbits=True) == 10

    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1k', 'b') == 1024
    assert human_to_bytes('1k', 'b', isbits=True) == 1024
    assert human_to_bytes('10k') == 10240
    assert human_to_bytes('10k', 'b') == 10240
    assert human_to_bytes('10k', 'b', isbits=True) == 10240
    assert human

# Generated at 2022-06-12 23:50:48.265594
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert sorted(lenient_lowercase([1, 'A', 'b'])) == [1, 'a', 'b']
    assert lenient_lowercase(['', True]) == ['', True]


# Generated at 2022-06-12 23:50:55.697287
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ABC', 'XYZ']) == ['abc', 'xyz']
    assert lenient_lowercase(['abc', 'xyz']) == ['abc', 'xyz']
    assert lenient_lowercase(['ABC', 3]) == ['abc', 3]
    assert lenient_lowercase(['ABC', None]) == ['abc', None]
    assert lenient_lowercase([]) == []



# Generated at 2022-06-12 23:51:04.840658
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('2KB') == 2048
    assert human_to_bytes('2KB', default_unit='B') == 2048
    assert human_to_bytes('2Kb') == 2097152
    assert human_to_bytes('2b') == 2
    assert human_to_bytes('2KBb') == 2097152
    assert human_to_bytes('2KbB') == 2048
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10BB') == 10
    assert human_to_bytes('10Bb') == 10
    assert human_to_bytes('10bb') == 8192
    assert human_to_bytes('10b') == 8192

# Generated at 2022-06-12 23:51:08.015046
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([123, 'ABC', 'def', 456]) == [123, 'abc', 'def', 456]



# Generated at 2022-06-12 23:51:21.730790
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' human_to_bytes unit test '''
    assert human_to_bytes('12345', isbits=True) == 12345, 'test failed - does not return int'
    assert human_to_bytes('1Mb', isbits=True) == 1048576, 'test failed - does not parse string value'
    assert human_to_bytes('1MB', isbits=True) == 1048576, 'test failed - should be case insensitive'
    assert human_to_bytes('1Mb', isbits=False) == 1048576, 'test failed - isbits should be False by default'
    assert human_to_bytes('1M', isbits=False) == 1048576, 'test failed - missing unit should be a byte'

# Generated at 2022-06-12 23:51:29.213887
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:40.398884
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 'a', 'b', 'c', 3]) == [1, 'a', 'b', 'c', 3]
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 'C', 1]) == ['a', 'b', 'c', 1]
    assert lenient_lowercase(['A', 'B', 'C', ['a', 'b', 'c']]) == ['a', 'b', 'c', ['a', 'b', 'c']]

# Generated at 2022-06-12 23:51:52.020831
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:57.407625
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([True, False]) == [True, False]


# Generated at 2022-06-12 23:52:08.576221
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Unit test for function human_to_bytes
    '''
    # Test for bits
    assert human_to_bytes('1', isbits=True) == 1, "cannot convert 1 (bits) to 1"
    assert human_to_bytes('1B', isbits=True) == 8, "cannot convert 1B (bits) to 8"
    assert human_to_bytes('1b', isbits=True) == 1, "cannot convert 1b (bits) to 1"
    assert human_to_bytes('1Mb', isbits=True) == 1000000, "cannot convert 1Mb (bits) to 1000000"
    assert human_to_bytes('1MB', isbits=True) == 8000000, "cannot convert 1MB (bits) to 8000000"

# Generated at 2022-06-12 23:52:19.255749
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' testing function human_to_bytes '''
    s = '42'
    res = human_to_bytes(s, None)
    assert res == 42 and type(res) == int, 'failed to convert %s to int' % s
    s = '42 '
    res = human_to_bytes(s, None)
    assert res == 42 and type(res) == int, 'failed to convert %s to int' % s
    s = '42.1 '
    res = human_to_bytes(s, None)
    assert res == 42 and type(res) == int, 'failed to convert %s to int' % s
    s = '42.1 B'
    res = human_to_bytes(s, None)
    assert res == 42 and type(res) == int, 'failed to convert %s to int'

# Generated at 2022-06-12 23:52:24.609082
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 1, 2, 3]) == ['a', 'b', 1, 2, 3]
    assert lenient_lowercase(['1', '2', '3']) == ['1', '2', '3']

# Generated at 2022-06-12 23:52:26.813734
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    result = lenient_lowercase([0, 'a', 'A', 'B', True])
    assert result == [0, 'a', 'a', 'b', True]

# Generated at 2022-06-12 23:52:36.947346
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert 1048576 == human_to_bytes('1M')
    assert 1073741824 == human_to_bytes('1G')
    assert 2 * 1073741824 == human_to_bytes('2G')

    assert 8 == human_to_bytes('8b', isbits=True)
    assert 1024 == human_to_bytes('1Kb', isbits=True)
    assert 1048576 == human_to_bytes('1Mb', isbits=True)
    assert 1073741824 == human_to_bytes('1Gb', isbits=True)
    assert 2 * 1073741824 == human_to_bytes('2Gb', isbits=True)

    assert 614400 == human_to_bytes('600K', isbits=False)

# Generated at 2022-06-12 23:52:48.226059
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    """Unit test for function lenient_lowercase"""
    lst = [1, 'T', 'Y', 'G']
    assert lenient_lowercase(lst) == [1, 't', 'y', 'g']



# Generated at 2022-06-12 23:52:48.908080
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    pass

# Generated at 2022-06-12 23:52:58.623380
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1, 'Test failed (1 -> 1)'
    assert human_to_bytes('1b') == 1, 'Test failed (1b -> 1)'
    assert human_to_bytes('1Kb') == 1024, 'Test failed (1Kb -> 1K)'
    assert human_to_bytes('1Mb') == 1048576, 'Test failed (1Mb -> 1M)'
    assert human_to_bytes('1G') == 1073741824, 'Test failed (1G -> 1G)'
    assert human_to_bytes('1Mb', isbits=True) == 1048576, 'Test failed (1Mb -> 1M)'
    assert human_to_bytes('1K', default_unit='B') == 1024, 'Test failed (1K -> 1K)'
    assert human_

# Generated at 2022-06-12 23:53:05.729157
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import unittest
    import sys

    class TestSequenceFunctions(unittest.TestCase):
        def test_human_to_bytes(self):
            def test_expect(data):
                ''' Generate test case: ('string', default_unit, isbits, expected_int_val) '''
                print(data)
                if len(data) == 4:
                    expect = data[3]
                else:
                    expect = data[2]
                self.assertEqual(human_to_bytes(*data), expect)

            test_expect(('1', None, 1))
            test_expect(('1.1', None, 1))
            test_expect(('10M', None, 10485760))
            test_expect(('10M', None, '10M', 10485760))

# Generated at 2022-06-12 23:53:13.739158
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['foo', 'bar', 'Foo', 'Bar']) == ['foo', 'bar', 'Foo', 'Bar']
    assert lenient_lowercase(['foo', 'bar', 'baz', 123]) == ['foo', 'bar', 'baz', 123]
    assert lenient_lowercase([123, 'foo', 'bar', 'baz']) == [123, 'foo', 'bar', 'baz']


# Generated at 2022-06-12 23:53:22.710659
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # default empty case
    assert human_to_bytes('') == 0
    # default unit case
    assert human_to_bytes('100', 'M') == 100000000
    # default no unit case
    assert human_to_bytes('100') == 100
    # default lowercase unit
    assert human_to_bytes('100k') == 102400
    # default uppercase unit
    assert human_to_bytes('100K') == 102400
    # default uppercase unit
    assert human_to_bytes('100KB') == 102400
    # default uppercase unit with no space
    assert human_to_bytes('100KB') == 102400
    # default uppercase unit with space
    assert human_to_bytes('100 KB') == 102400
    # default decimal unit with space

# Generated at 2022-06-12 23:53:26.565961
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a', 'b']) == ['a', 'b']
    assert lenient_lowercase([2, 'b']) == [2, 'b']
    assert lenient_lowercase(['a', 2]) == ['a', 2]



# Generated at 2022-06-12 23:53:38.295797
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('10b') == 1
    assert human_to_bytes('1Gb') == 1073741824
    assert human_to_bytes('10kb') == 10240
    assert human_to_bytes('1mb') == 1048576
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('10b') == 1
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes

# Generated at 2022-06-12 23:53:47.221625
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:58.405894
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:08.409279
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]
    assert lenient_lowercase(['A', 'B', 'C', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]


# Generated at 2022-06-12 23:54:10.901001
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'c', 2, '3']) == ['a', 'b', 'c', 2, '3']

# Generated at 2022-06-12 23:54:15.029493
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['foo', 1, 'bar']) == ['foo', 1, 'bar']
    assert lenient_lowercase(['FOO', 1, 'bar']) == ['foo', 1, 'bar']


# Generated at 2022-06-12 23:54:15.636488
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    pass

# Generated at 2022-06-12 23:54:24.425339
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit test for function human_to_bytes(number, default_unit=None, isbits=False)
    """

# Generated at 2022-06-12 23:54:35.401040
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:38.749845
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    from nose.tools import assert_equal, assert_not_equal
    assert_equal(sorted(['BAR', 'foo', 'Bar', 'baR', 42]), sorted(lenient_lowercase(['BAR', 'foo', 'Bar', 'baR', 42])))
    assert_not_equal(sorted(['BAR', 'foo', 'Bar', 'baR']), sorted(lenient_lowercase(['BAR', 'foo', 'Bar', 'baR', 42])))


# Generated at 2022-06-12 23:54:47.907029
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import jsmin
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 23:55:00.201326
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:04.523207
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['X', None, 'Y', 'Z', '1']) == ['x', None, 'y', 'z', '1']

# Generated at 2022-06-12 23:55:28.675956
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10.5K') == 10.5 * 1024
    assert human_to_bytes('10.5K', default_unit='Kb') == 10.5 * 1024 * 8
    assert human_to_bytes(1048576) == 1048576
    assert human_to_bytes('10.5', unit='Kb') == 10.5 * 1024 * 8
    assert human_to_bytes('10.5Kb') == 10.5 * 1024 * 8
    assert human_to_bytes('10.5Kb', default_unit=None) == 10.5 * 1024 * 8
    assert human_to_bytes('10.5Kb', isbits=True) == 10.5 * 1024 * 8

# Generated at 2022-06-12 23:55:33.324652
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['test']) == ['test']
    assert lenient_lowercase([1, 'test']) == [1, 'test']
    assert lenient_lowercase(['TEST']) == ['test']
    assert lenient_lowercase(['TEST', 1]) == ['test', 1]

# Generated at 2022-06-12 23:55:38.944189
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['foo', 'bar', 'baz'] == lenient_lowercase(['foo', 'bar', 'baz'])
    assert ['foo', 'bar', 'baz'] == lenient_lowercase(['Foo', 'BaR', 'BaZ'])
    assert [1, 2, 'baz'] == lenient_lowercase([1, 2, 'BaZ'])
    assert ['foo'] == lenient_lowercase(['Foo'])
    assert [] == lenient_lowercase([])


# Generated at 2022-06-12 23:55:42.085847
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'A', 'a', 'b', 2]) == [1, 'a', 'a', 'b', 2]



# Generated at 2022-06-12 23:55:50.203870
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:54.628228
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test for valid input
    input_data = ['abc', [1, 2, 3], 'xyz', 'aBc']
    output_data = ['abc', [1, 2, 3], 'xyz', 'abc']
    assert lenient_lowercase(input_data) == output_data


# Generated at 2022-06-12 23:55:59.946146
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['test1']) == ['test1']
    assert lenient_lowercase(['test1', 'TEST2']) == ['test1', 'test2']
    assert lenient_lowercase([1, 'TEST2', 3]) == [1, 'test2', 3]



# Generated at 2022-06-12 23:56:10.909602
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2k') == 2048
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1.5MB') == 1572864
    assert human_to_bytes('1.5Mb') == 1572864

    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1g') == 1073741824
    assert human_to_bytes('1.5G') == 1610612736
    assert human_to_bytes('1.5GB') == 1610612736
    assert human_to_bytes('1.5Gb') == 1610612736

# Generated at 2022-06-12 23:56:21.683899
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('3.5') == 3
    assert human_to_bytes('3.5B') == 3
    assert human_to_bytes('3.5B', default_unit='m') == 3
    assert human_to_bytes('3.5B', default_unit='M') == 3565158.875
    assert human_to_bytes(3.5) == 3
    assert human_to_bytes(3.5, default_unit='B') == 3
    assert human_to_bytes(3.5, default_unit='m') == 350
    assert human_to_bytes(3.5, default_unit='M') == 3565158.875
    assert human_to_bytes('3.5K') == 3584
    assert human_to_bytes('3.5M') == 376832000

# Generated at 2022-06-12 23:56:26.848066
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'a', 'B', 4]) == [1, 'a', 'B', 4]
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 'Ab', 'b']) == [1, 'Ab', 'b']

# Generated at 2022-06-12 23:56:57.590112
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    strings = ['foo', 1, None, [], {}]
    assert lenient_lowercase(strings) == ['foo', 1, None, [], {}]



# Generated at 2022-06-12 23:57:01.076785
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["vlan", 3, True]) == ["vlan", 3, True]
    assert lenient_lowercase(["VLAN", 3, True]) == ["vlan", 3, True]


# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:57:12.251602
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:18.931261
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('10M') == 10485760)
    assert(human_to_bytes('10Mb') == 10485760)
    assert(human_to_bytes('10Mb', isbits=True) == 13107200)
    assert(human_to_bytes('10Mb', isbits=True, default_unit='b') == 13107200)
    assert(human_to_bytes('10', default_unit='kb') == 10240)
    assert(human_to_bytes('10Mb', default_unit='b', isbits=True) == 13107200)



# Generated at 2022-06-12 23:57:25.642904
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('1.5M') == 1572864)
    assert(human_to_bytes('1.5b', isbits=True) == .1875)
    assert(human_to_bytes('1.5Mb', isbits=True) == 1572864)
    assert(human_to_bytes('1.5G') == 1572864000)
    assert(human_to_bytes('1.5t') == 1572864000000)
    assert(human_to_bytes('1.5m') == 1572864000)
    assert(human_to_bytes('1.5K') == 1536)
    assert(human_to_bytes('1.5Kb', isbits=True) == 1536)
    assert(human_to_bytes('100') == 100)

# Generated at 2022-06-12 23:57:32.589766
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [1, 'a', 'B', '1.0', None, {'a': 'b'}]
    expected_list = [1, 'a', 'b', '1.0', None, {'a': 'b'}]
    actual_list = lenient_lowercase(test_list)
    assert actual_list == expected_list


# Generated at 2022-06-12 23:57:35.766481
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['AA']) == ['aa']
    assert lenient_lowercase(['AA', 'BB']) == ['aa', 'bb']
    assert lenient_lowercase(['AA', None, 'BB']) == ['aa', None, 'bb']



# Generated at 2022-06-12 23:57:43.480286
# Unit test for function human_to_bytes
def test_human_to_bytes():

    assert human_to_bytes('10M') == human_to_bytes(10, 'M')
    assert human_to_bytes('2K') == human_to_bytes(2, 'K')
    assert human_to_bytes('2k') == human_to_bytes(2, 'k')
    assert human_to_bytes('2k', isbits=True) == human_to_bytes(2, 'k', isbits=True)
    assert human_to_bytes(2, 'Kb') == human_to_bytes(2, 'kb')
    assert human_to_bytes(2, 'Kb', isbits=True) == human_to_bytes(2, 'kb', isbits=True)
    assert human_to_bytes('10.5M') == human_to_bytes(10.5, 'M')
   

# Generated at 2022-06-12 23:57:46.969512
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['foo', (1, 2), 'BAR', ['baz']]) == ['foo', (1, 2), 'BAR', ['baz']]

# Generated at 2022-06-12 23:57:55.048776
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test an empty list
    assert lenient_lowercase([]) == []
    # Test a list with only strings
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    # Test a list with strings and integers
    assert lenient_lowercase(['a', 1, 'c']) == ['a', 1, 'c']
    # Test a list with strings, integers, and floats
    assert lenient_lowercase(['a', 'b', 1, 2.0, 3.456]) == ['a', 'b', 1, 2.0, 3.456]
    # Test a list with strings, integers, floats, and None
    assert lenient_lowercase(['a', None, 1.0, 'c']) == ['a', None, 1.0, 'c']
