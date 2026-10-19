

# Generated at 2022-06-12 23:48:56.817816
# Unit test for function human_to_bytes
def test_human_to_bytes():

    # convert string to bytes (with/without units)
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1M') == 1048576

    # convert string to bits (with/without units)
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    # convert string using provided unit
    assert human_to_bytes('10', 'M') == 10485760
    assert human_to_bytes('10', 'K') == 10240

    # convert string bits using provided unit

# Generated at 2022-06-12 23:49:07.447990
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from collections import namedtuple
    from copy import deepcopy

    class color:
        PURPLE = '\033[1;35m'
        CYAN = '\033[1;36m'
        RED = '\033[1;31m'
        GREEN = '\033[0;32m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    TestCase = namedtuple("TestCase", ["number", "expected_out", "isbits", "unit", "message"])


# Generated at 2022-06-12 23:49:14.064507
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes('1.6') == 2
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('1.6KB') == 1600
    assert human_to_bytes('1.6KiB') == 1600
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1.6M') == 16777216
    assert human_to_bytes('1.5MB') == 1572864
    assert human_to_bytes('1.6MiB') == 16777216
    assert human_to_bytes('1.5G') == 1610612736

# Generated at 2022-06-12 23:49:17.222955
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['1K', '2Mb', '3G', None, '4Tb', '5Pb']) == ['1k', '2mb', '3g', None, '4tb', '5pb']



# Generated at 2022-06-12 23:49:29.680046
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Non existing unit
    try:
        human_to_bytes('42X')
        assert False, 'Input: 42X\nExpected: Failed with ValueError\nResult: Success'
    except Exception:
        pass

    # Invalid input
    try:
        human_to_bytes('abc')
        assert False, 'Input: abc\nExpected: Failed with ValueError\nResult: Success'
    except Exception:
        pass

    # Invalid input
    try:
        human_to_bytes('abcd')
        assert False, 'Input: abcd\nExpected: Failed with ValueError\nResult: Success'
    except Exception:
        pass

    # No unit given

# Generated at 2022-06-12 23:49:36.894683
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert str(human_to_bytes('10M')) == '10485760'
    assert str(human_to_bytes('10M', 'M')) == '10485760'
    assert str(human_to_bytes('10', 'M')) == '10485760'
    assert str(human_to_bytes('10.0M')) == '10485760'
    assert str(human_to_bytes('10.0M', 'M')) == '10485760'
    assert str(human_to_bytes('10.0', 'M')) == '10485760'
    assert str(human_to_bytes('10.5M')) == '10905190'
    assert str(human_to_bytes('10.5M', 'M')) == '10905190'

# Generated at 2022-06-12 23:49:41.567053
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['abc', 'DEF']) == ['abc', 'DEF']
    assert lenient_lowercase(['abc', (1, 2, 3)]) == ['abc', (1, 2, 3)]
    assert lenient_lowercase(['abC', {'def': 'ghi'}]) == ['abC', {'def': 'ghi'}]



# Generated at 2022-06-12 23:49:51.538683
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:59.629906
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from nose.tools import assert_equals, assert_raises_regexp

    assert_equals(lenient_lowercase(['a', 'A', 'b', 1, 2]), ['a', 'a', 'b', 1, 2])
    assert_equals(human_to_bytes(10, 'M'), 10 * (1 << 20))
    assert_equals(human_to_bytes(10, 'Mb', True), 10 * (1 << 20))
    assert_raises_regexp(ValueError, r'expect M or Mb', human_to_bytes, 10, 'Mb')
    assert_raises_regexp(ValueError, r'expect M or Mb', human_to_bytes, 10, 'MB')

# Generated at 2022-06-12 23:50:04.096739
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from ansible_collections.misc.tests.unit.compat.mock import patch, MagicMock
    from ansible.utils.human_to_bytes import human_to_bytes
    my_mock = MagicMock()

    with patch.object(re, 'search', return_value=my_mock):
        my_mock.group.return_value = '10MB'
        my_mock.group.side_effect = ['10', 'MB']

        size = human_to_bytes('10M')
        assert size == 10485760

        my_mock.group.return_value = '10MB'
        my_mock.group.side_effect = ['10', 'Mb']

# Generated at 2022-06-12 23:50:14.859480
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 3]) == ['a', 'b', 3]
    assert lenient_lowercase(['A', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase([3, 4, 5, 6]) == [3, 4, 5, 6]

# Generated at 2022-06-12 23:50:26.159340
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:50:38.549971
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Also human_to_bytes checks for None arguments in _convert_with_unit method
    assert human_to_bytes('125') == 125
    assert human_to_bytes('125.125') == 125
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('1024.0') == 1024
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb') == 13107200
    assert human_to_bytes('10mb') == 13107200
    assert human_to_bytes('10M', default_unit='B') == 10485760
    assert human_to_bytes('10M', isbits=True) == 13107200

# Generated at 2022-06-12 23:50:42.331872
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    print('Testing lenient_lowercase')
    test_list = ['A1', 'B1', 2, 'C1']
    result = lenient_lowercase(test_list)
    expected_result = ['a1', 'b1', 2, 'c1']
    assert result == expected_result, "Invalid result: %s" % result
    print('Test passed')



# Generated at 2022-06-12 23:50:49.625218
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Something', 'to', 'lowercase']) == ['something', 'to', 'lowercase']
    assert lenient_lowercase(['S', 'o', 'm', 'e', 't', 'h', 'i', 'n', 'g', 't', 'o', 'l', 'o', 'w', 'e', 'r', 'c', 'a', 's', 'e']) == ['s', 'o', 'm', 'e', 't', 'h', 'i', 'n', 'g', 't', 'o', 'l', 'o', 'w', 'e', 'r', 'c', 'a', 's', 'e']

# Generated at 2022-06-12 23:51:00.690592
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1K') == 1024  # string
    assert human_to_bytes(1, 'K') == 1024  # int/float + unit
    assert human_to_bytes('1M', default_unit='K') == 1048576  # when 'unit' is not specified in string, use 'default_unit' instead of bytes.
    assert human_to_bytes('1.5M', default_unit='K') == 1572864  # float - round to int
    assert human_to_bytes('1.5M') == 1572864  # float - round to int. No 'unit' specified in string, so default_unit is not used (returns bytes)
    assert human_to_bytes(1.5, 'M') == 1572864  # float + unit

# Generated at 2022-06-12 23:51:07.903922
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Basic tests
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['abc']) == ['abc']
    assert lenient_lowercase(['abc', 'def']) == ['abc', 'def']

    # Non-strings should be untouched
    assert lenient_lowercase(['abc', 1]) == ['abc', 1]
    assert lenient_lowercase([1]) == [1]
    assert lenient_lowercase([1, 1]) == [1, 1]

    # None should be untouched
    assert lenient_lowercase(['abc', None]) == ['abc', None]
    assert lenient_lowercase([None]) == [None]
    assert lenient_lowercase([None, None]) == [None, None]



# Generated at 2022-06-12 23:51:11.007934
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    cases = [("a", ['A']),
             ("A", ['a']),
             ("b", ['b']),
             ("B", ['B']),
             (1, [1]),
             (["a", "b", 1, ["c"]], [['A'], ['b'], 1, [['c']]])]
    for test in cases:
        assert(lenient_lowercase(test[0]) == test[1])


# Generated at 2022-06-12 23:51:21.325771
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M')
    assert human_to_bytes('10M') == human_to_bytes(10, 'm')
    assert human_to_bytes('10M') == human_to_bytes(10, 'Mb')
    assert human_to_bytes('10M') == human_to_bytes(10, 'mb')
    assert human_to_bytes('10M') == human_to_bytes(10, 'Mbit')
    assert human_to_bytes('10M') == human_to_bytes(10, 'mbit')
    assert human_to_bytes('10M', isbits=True) == human_to_bytes(10, 'm', isbits=True)
    assert human_to_bytes('10M', isbits=True) == human

# Generated at 2022-06-12 23:51:30.285373
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Sanity check
    assert human_to_bytes('1M') == 1048576

    # Unit defined as part of parameter
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'K') == 10240

    # Strange cases
    assert human_to_bytes(10, 'MB') == 10485760
    assert human_to_bytes(10, 'KB') == 10240

    # Bits
    assert human_to_bytes(10, 'Mb') == 1310720
    assert human_to_bytes(10, 'Kb') == 1280
    assert human_to_bytes('10Mb', isbits=True) == 1310720
    assert human_to_bytes('10Kb', isbits=True) == 1280

    # Bits and bytes mixed

# Generated at 2022-06-12 23:51:39.673811
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['A', 'a', 'A1', '1a', 'A1a', '1', '1.0', 'A1.0']
    assert lenient_lowercase(lst) == ['a', 'a', 'a1', '1a', 'a1a', '1', '1.0', 'a1.0']

# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:51:50.784577
# Unit test for function human_to_bytes
def test_human_to_bytes():
    for unit in SIZE_RANGES.keys():
        for unit in SIZE_RANGES.keys():
            for unit in SIZE_RANGES.keys():
                for unit in SIZE_RANGES.keys():
                    assert human_to_bytes(str(1) + unit, None) == SIZE_RANGES[unit]
                    assert human_to_bytes(str(1024) + unit, None) == SIZE_RANGES[unit] * 1024
                    assert human_to_bytes(str(1024) + unit.lower(), None) == SIZE_RANGES[unit] * 1024
                    assert human_to_bytes(str(1024) + unit, unit.lower()) == SIZE_RANGES[unit] * 1024
                    assert human_to_bytes(str(1024) + unit, unit.upper()) == S

# Generated at 2022-06-12 23:51:59.431409
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:52:10.647787
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:52:12.528954
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["Hello", 123, "World"]) == ["hello", 123, "world"]

# Generated at 2022-06-12 23:52:16.255738
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    l = [ 'A', 'B', 'C', 1, 2, 3, 'D' ]
    t = ['a', 'b', 'c', 1, 2, 3, 'd']
    assert lenient_lowercase(l) == t


# Generated at 2022-06-12 23:52:24.679091
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["1", "2", "3", "a", "b", "c"]) == ["1", "2", "3", "a", "b", "c"]
    assert lenient_lowercase(["1", "2", "3", "A", "b", "c"]) == ["1", "2", "3", "a", "b", "c"]
    assert lenient_lowercase(["1", "2", "3", "A", "B", "c"]) == ["1", "2", "3", "a", "b", "c"]
    assert lenient_lowercase(["1", "2", "3", "A", "B", "C"]) == ["1", "2", "3", "a", "b", "c"]

# Generated at 2022-06-12 23:52:26.605792
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase(['A', 'b']) == ['a', 'b']

# Generated at 2022-06-12 23:52:30.993846
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 1]) == ['a', 'b', 1]
    assert lenient_lowercase(['A', b'B', 1]) == ['a', b'B', 1]
    assert lenient_lowercase([b'A', b'B', 1]) == [b'A', b'B', 1]


# Generated at 2022-06-12 23:52:42.517350
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Tests for bytes conversion
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1 M') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1Mb', isbits=True, unit='B') == 1048576
    assert human_to_bytes('1Mb', isbits=True, unit='b') == 131072
    assert human_to_bytes('1Mb', unit='b') == 1048576
    assert human_to_bytes('1Mb', unit='B') == 131072

# Generated at 2022-06-12 23:52:56.935231
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Convert bytes example
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10M', default_unit='MB') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10MB', unit='MB') == 10485760

    # Convert bits example
    assert human_to_bytes('10Mb') == 13107200

# Generated at 2022-06-12 23:53:04.856458
# Unit test for function human_to_bytes
def test_human_to_bytes():
    human_format_list = ('1K', '1KB', '1Kb', '1K', '1KB', '1.5M', '1.5MB', '2Mb', '2Mb', '3G', '3GB', '3Gb', '3G', '3GB', '3Gb', '3.5P', '3.5PB', '3.5Pb', '3.5P', '3.5PB', '4Tb', '4TB', '4T', '4TB', '4.5E', '4.5EB', '4.5Eb')

# Generated at 2022-06-12 23:53:15.088909
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([1, "AbC", 3]) == [1, "abc", 3]
    assert lenient_lowercase(["AbC", "dEf"]) == ["abc", "def"]
    assert lenient_lowercase(["AbC", "dEf", 2]) == ["abc", "def", 2]
    assert lenient_lowercase(["AbC", "dEf", 2, 3.2, 4.2]) == ["abc", "def", 2, 3.2, 4.2]
    assert lenient_lowercase([]) == []



# Generated at 2022-06-12 23:53:19.198102
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    sample_list = [u'123', 'ab cd', 'ef€gh'.decode('utf-8'), '', 0, True]
    expected_result = ['123', 'ab cd', 'ef€gh'.decode('utf-8'), '', 0, True]
    assert lenient_lowercase(sample_list) == expected_result

# Generated at 2022-06-12 23:53:22.993582
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['aa', 'b', 1, 2, []]) == ['aa', 'b', 1, 2, []]
    assert lenient_lowercase(['AA', 'B', 1, 2, []]) == ['aa', 'b', 1, 2, []]


# Generated at 2022-06-12 23:53:25.172516
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-12 23:53:30.176035
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a', 'b', 'c'] == lenient_lowercase(['A', 'b', 'C'])
    assert [1, 2, 3] == lenient_lowercase([1, 2, 3])
    assert ['a', 1, 'c'] == lenient_lowercase(['A', 1, 'C'])



# Generated at 2022-06-12 23:53:41.056038
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:49.181216
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import unittest

    class TestHumanToBytes(unittest.TestCase):
        def test_human_to_bytes(self):
            self.assertEqual(1, human_to_bytes('1'))
            self.assertEqual(1, human_to_bytes('1b'))
            self.assertEqual(1, human_to_bytes('1B'))
            self.assertEqual(1, human_to_bytes('1b', isbits=True))
            self.assertEqual(1, human_to_bytes('1b', isbits=True, unit='b'))
            self.assertEqual(1048576, human_to_bytes('1MB'))
            self.assertEqual(1048576, human_to_bytes('1MB', unit='M'))
            self.assertE

# Generated at 2022-06-12 23:53:53.362784
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["a", "B", "C"]) == ["a", "B", "C"]
    assert lenient_lowercase(["a", 1, 2]) == ["a", 1, 2]



# Generated at 2022-06-12 23:54:07.294429
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ONE', 'Two', 3, 'four']) == ['one', 'two', 3, 'four']


# Generated at 2022-06-12 23:54:18.329567
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:25.633893
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:33.788644
# Unit test for function human_to_bytes
def test_human_to_bytes():
    cases = [
        ('1K', 1000),
        ('1.5k', 1500),
        ('200b', 200),
        ('200B', 200),
        ('200bB', 200),
        ('200bb', 200),
        ('Kb', 1000),
        ('1.4KB', 1400),
        ('400', 400),
        ('0K', 0),
    ]
    for case in cases:
        assert human_to_bytes(case[0]) == case[1], 'case %s failed' % case[0]



# Generated at 2022-06-12 23:54:36.865825
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, "b", "C"]) == [1, "b", "c"]

# Generated at 2022-06-12 23:54:39.239544
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'foo', 'BAR', 2]) == [1, 'foo', 'BAR', 2]



# Generated at 2022-06-12 23:54:42.226275
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'C', 'D', 1, 'E', 2]) == ['a', 'b', 'c', 'd', 1, 'e', 2]



# Generated at 2022-06-12 23:54:46.010964
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    input_list = (['a', 1, 'B', 3.2, u'c'])
    expected_list = (['a', 1, 'b', 3.2, 'c'])

    result = lenient_lowercase(input_list)
    assert result == expected_list



# Generated at 2022-06-12 23:54:59.076763
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Human readable format to byte conversion testing
    '''
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10.0') == 10
    assert human_to_bytes(10) == 10
    assert human_to_bytes(10.0) == 10
    assert human_to_bytes('10B', 'B') == 10
    assert human_to_bytes('10', 'B') == 10

    assert human_to_bytes('10K') == 10 * 1024
    assert human_to_bytes('10KB') == 10 * 1024
    assert human_to_bytes('10.0KB') == 10 * 1024
    assert human_to_bytes('10.0 Kb', isbits=True) == 10 * 1024
    assert human_to

# Generated at 2022-06-12 23:55:07.157095
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['This', 'is', 'a', 'List', 1, 2, 'With', 3, 'NUmberS', 4, 'MixeD']
    reference_list = ['this', 'is', 'a', 'list', 1, 2, 'with', 3, 'numbers', 4, 'mixed']
    result = lenient_lowercase(test_list)
    assert result == reference_list
    assert test_list == ['This', 'is', 'a', 'List', 1, 2, 'With', 3, 'NUmberS', 4, 'MixeD']



# Generated at 2022-06-12 23:55:24.578531
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'A', 34, 'b']) == [1, 'a', 34, 'b']



# Generated at 2022-06-12 23:55:31.659121
# Unit test for function human_to_bytes
def test_human_to_bytes():
    def must_fail(str_to_check):
        try:
            human_to_bytes(str_to_check)
            assert False
        except ValueError:
            pass
    def must_success(str_to_check, should_equal):
        assert should_equal == human_to_bytes(str_to_check)
    # success tests
    must_success('1', 1)
    must_success(' 1 ', 1)
    must_success('2.5K', 2.5*1024)
    must_success(' 2.5K ', 2.5*1024)
    must_success('  2.5 K  ', 2.5*1024)
    must_success('2.5Kb', 2.5*1024*8)
    must_success(' 2.5Kb ', 2.5*1024*8)
   

# Generated at 2022-06-12 23:55:33.939263
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'b', 1, 'C']) == ['a', 'b', 1, 'c']



# Generated at 2022-06-12 23:55:45.390018
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    unittest for function human_to_bytes
    '''
    head = "unittest:"
    print("\n%s human_to_bytes test\n" % head)


# Generated at 2022-06-12 23:55:58.479375
# Unit test for function human_to_bytes
def test_human_to_bytes():
    errmsg_end = ' (original input string: %s)'

# Generated at 2022-06-12 23:56:04.125540
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    in_list = [1, 'STRINg', 2.3, 'StRiNg']
    out_list = [1, 'string', 2.3, 'string']
    assert lenient_lowercase(in_list) == out_list



# Generated at 2022-06-12 23:56:13.369567
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Tests for bytes
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes('3.9') == 3
    assert human_to_bytes('1 B') == 1
    assert human_to_bytes('1.5 B') == 1
    assert human_to_bytes('3.0 B') == 3
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1.5b') == 1
    assert human_to_bytes('3.0b') == 3
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1.5K') == 1024
    assert human_to_bytes('3.0K') == 3072

# Generated at 2022-06-12 23:56:23.746300
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Check invalid string case
    with pytest.raises(ValueError):
        human_to_bytes('foo')
    with pytest.raises(ValueError):
        human_to_bytes('bar/s')

    # Check edge case
    assert human_to_bytes('0') == 0
    assert human_to_bytes('0 b') == 0
    assert human_to_bytes('0 B') == 0

    # Check default unit case
    assert human_to_bytes('10', default_unit='B') == 10
    assert human_to_bytes('10', default_unit='b') == 10

    # Check unit case
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10 B') == 10
    assert human_to_bytes('10 b') == 10

    # Check suffix case
   

# Generated at 2022-06-12 23:56:33.250625
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:56:42.471831
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

# Generated at 2022-06-12 23:57:05.836326
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 'b', 'c', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]
    assert lenient_lowercase(['A', 'B', 'C', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]



# Generated at 2022-06-12 23:57:16.507770
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2Kb') == 2048
    assert human_to_bytes('2KB') == 2048
    assert human_to_bytes('2Kb', isbits=True) == 2048
    assert human_to_bytes('2KB', isbits=True) == 2048
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('10MB', isbits=True) == 10485760
    assert human_to_bytes('2k') == 2048
    assert human_to_

# Generated at 2022-06-12 23:57:23.531367
# Unit test for function human_to_bytes
def test_human_to_bytes():
    result = {}
    ''' test cases '''
    result[1] = (human_to_bytes('10MB', isbits=False), 10485760)
    result[2] = (human_to_bytes('10M', isbits=False), 10485760)
    result[3] = (human_to_bytes('10Mb', isbits=True), 10485760)
    result[4] = (human_to_bytes('10Mb',), 10485760)
    result[5] = (human_to_bytes('10M', isbits=True), 10485760)
    result[6] = (human_to_bytes('1KB', isbits=False), 1024)
    result[7] = (human_to_bytes('1K', isbits=False), 1024)
    result[8]

# Generated at 2022-06-12 23:57:30.346112
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test byte
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1BYTE') == 1
    assert human_to_bytes('1byte') == 1

    # Test bit
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1B', isbits=True) == 8
    assert human_to_bytes('1bit') == 8
    assert human_to_bytes('1BIT') == 8

    # Test kbit
    assert human_to_bytes('1kbit', isbits=True) == 1000
    assert human_to_bytes('1KBit', isbits=True) == 1000
    assert human_to_bytes('1kbit', isbits=True) == 1000


# Generated at 2022-06-12 23:57:35.058313
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test = ['A', 1, [1], 'aB', 'c', 'D', 2]
    result = lenient_lowercase(test)
    assert result == ['a', 1, [1], 'ab', 'c', 'd', 2]



# Generated at 2022-06-12 23:57:43.053932
# Unit test for function lenient_lowercase

# Generated at 2022-06-12 23:57:52.563088
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('') == ValueError
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1.0) == 1
    assert human_to_bytes('0.1M') == 104857
    assert human_to_bytes(0.1, 'M') == 104857

    assert human_to_bytes('K') == ValueError
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1kb') == 1 << 10
    assert human_to_bytes('1Kb') == ValueError
    assert human

# Generated at 2022-06-12 23:58:05.172549
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M', default_unit='M') == 10485760
    assert human_to_bytes('10.5M') == (10485760 + 512 * 1024)
    assert human_to_bytes('10M', default_unit='B') == 10485760
    assert human_to_bytes('10.5M', default_unit='B') == (10485760 + 512 * 1024)

    assert human_to_bytes('10.5Mb') == (10485760 + 512 * 1024)
    assert human_to_bytes('10.5Mb', default_unit='b') == (10485760 + 512 * 1024)
    assert human_to_bytes('10.5Mb', isbits=False) == (10485760 + 512 * 1024)

# Generated at 2022-06-12 23:58:13.374767
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['she', 'has', 1, 'apple']) == ['she', 'has', 1, 'apple']
    assert lenient_lowercase(['SHE', 'HAS', 1, 'apple']) == ['she', 'has', 1, 'apple']
    assert lenient_lowercase(['SHE', 'HAS', 1, 'APPLE']) == ['she', 'has', 1, 'apple']
    assert lenient_lowercase(['SHE', 'HAS', 1, 'APPLE']) != ['SHE', 'HAS', 1, 'apple']
    assert lenient_lowercase(['SHE', 'HAS', 1, 'APPLE']) != ['she', 'HAS', 1, 'apple']

# Generated at 2022-06-12 23:58:23.467032
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from nose.tools import assert_equal
    assert_equal(human_to_bytes('1B'), 1)
    assert_equal(human_to_bytes('1b'), 1)
    assert_equal(human_to_bytes('1B', isbits=True), 1)
    assert_equal(human_to_bytes('1b', isbits=True), 1)
    assert_equal(human_to_bytes('10.0B'), 10)
    assert_equal(human_to_bytes('1KB'), 1000)
    assert_equal(human_to_bytes('1Kb'), 1000)
    assert_equal(human_to_bytes('1KB', isbits=True), 8000)
    assert_equal(human_to_bytes('1Kb', isbits=True), 1000)