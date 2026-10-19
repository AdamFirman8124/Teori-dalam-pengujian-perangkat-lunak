

# Generated at 2022-06-12 23:48:48.465333
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1H', 'MB') == 1048576 * 100
    assert human_to_bytes(1, 'MB') == 1048576
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes(10, 'MB') == 10485760
    assert human_to_bytes(1.0, 'MB') == 1048576
    assert human_to_bytes('1.0M') == 1048576
    assert human_to_bytes('10Mb') == 10485760 / 8
    assert human_to_bytes(10, 'Mb', True) == 10485760 / 8
    assert human_to_

# Generated at 2022-06-12 23:48:56.926303
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('4MB', isbits=False) == (1 << 22)
    assert human_to_bytes('4Mb', isbits=True) == (1 << 22)
    assert human_to_bytes('4M', isbits=False) == (1 << 22)
    assert human_to_bytes('4M', isbits=True) == (1 << 22)
    assert human_to_bytes('4b', isbits=False) == 1
    assert human_to_bytes('4b', isbits=True) == 1
    assert human_to_bytes('4', isbits=False) == 4
    assert human_to_bytes('4', isbits=True) == 4
    assert human_to_bytes('4B', isbits=False) == 1

# Generated at 2022-06-12 23:49:07.551992
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest
    assert human_to_bytes(10) == 10
    assert human_to_bytes("10") == 10
    assert human_to_bytes("10M") == 10485760


# Generated at 2022-06-12 23:49:15.846497
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1Mb', isbits=True, unit='b') == 1048576
    assert human_to_bytes('1MB', isbits=False, unit='b') == 1
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=False) == 1048576
    assert human_to_bytes('1M', isbits=True) == 1048576
    assert human_to_bytes('1M', isbits=False) == 1048576
    assert human_to_bytes('1M', unit='b') == 1048576

# Generated at 2022-06-12 23:49:26.975289
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1K') == 1 << 10
    assert human_to_bytes('1M') == 1 << 20
    assert human_to_bytes('1G') == 1 << 30
    assert human_to_bytes('1T') == 1 << 40
    assert human_to_bytes('1P') == 1 << 50
    assert human_to_bytes('1E') == 1 << 60
    assert human_to_bytes('1Z') == 1 << 70
    assert human_to_bytes('1Y') == 1 << 80
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('1.4') == 1

# Generated at 2022-06-12 23:49:35.649934
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from pytest import raises

    # boundary values
    assert(human_to_bytes('') == 0)
    assert(human_to_bytes(None) == 0)
    assert(human_to_bytes('0') == 0)

    # standard cases
    assert(human_to_bytes('1') == 1)
    assert(human_to_bytes('1.5') == 1)
    assert(human_to_bytes('1.6') == 2)
    assert(human_to_bytes('0.5') == 0)

    # standard cases with units
    assert(human_to_bytes('1.5b') == 1)
    assert(human_to_bytes('5k') == 5 * 1024)
    assert(human_to_bytes('5M') == 5 * 1024 * 1024)

# Generated at 2022-06-12 23:49:41.294907
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10m') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('1000.5k') == 1024000
    assert human_to_bytes('1000.5K', isbits=True) == 1024000
    assert human_to_bytes('10.5b') == 11
    assert human_to_bytes('10.5B') == 10
    assert human_to_bytes('10.5') == 10
    try:
        assert human_to_bytes('10.5Bit') == 10
    except ValueError:
        assert True

# Generated at 2022-06-12 23:49:51.310273
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:59.478212
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10', 'K') == 10 * 1024
    assert human_to_bytes('10M') == 10 * 1024 * 1024
    assert human_to_bytes('10m') == 10 * 1024 * 1024
    assert human_to_bytes('10MB') == 10 * 1024 * 1024
    assert human_to_bytes('10Mb') == 10 * 1024 * 8
    assert human_to_bytes('10mb') == 10 * 1024 * 8
    assert human_to_bytes('2KB') == 2 * 1024
    assert human_to_bytes('2KB', 'b') == 2 * 1024 * 8
    assert human_to_bytes('2KB', 'B') == 2 * 1024
    assert human_to_bytes('2Mb') == 2 * 1024 * 8 * 1024


# Generated at 2022-06-12 23:50:03.955052
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = [('2k', 2048),
             ('12K', 12288),
             ('10M', 10485760),
             ('10MB', 10485760),
             ('MB', 1048576),
             ('Mb', 1048576),
             ('5', 5),
             ('1B', 1),
             ('1B', 1),
             ('1b', 1),
             ('5', 5, 'dummy'),
             ('1dummy', 1, 'dummy'),
             ('5M', 5242880, 'MB'),
             ('1kb', 1000, 'b'),
             ('1KB', 1000, 'b'),
             ('1Kb', 1000, 'b'),
             ('1Mb', 1000000, 'b'),
             ]

# Generated at 2022-06-12 23:50:17.470872
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = (
        ('1K', 1024),
        ('1B', 1),
        ('1Bb', 1),
        ('1KB', 1000),
        ('1Kb', 1000),
        ('1Mb', 1048576),
        ('1MB', 1048576),
        ('1M', 1048576 * 10),
        ('1Mb', 1048576),
    )
    for test in tests:
        result = human_to_bytes(test[0], isbits=True)
        assert result == test[1], result



# Generated at 2022-06-12 23:50:20.794032
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    """
    This is a test function that checks if lenient_lowercase works properly
    """
    assert lenient_lowercase(['A', 'B', 123, 456]) == ['a', 'b', 123, 456]

# Generated at 2022-06-12 23:50:29.687046
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1.1M') == 1179648
    assert human_to_bytes('1.1MB') == 1179648
    assert human_to_bytes(1179648) == 1179648
    assert human_to_bytes('1.1Mb') == 1398101
    assert human_to_bytes('1.1Mb', isbits=True) == 1398101
    assert human_to_bytes('1.1b') == 1
    assert human_to_bytes('1.1b', isbits=True) == 1
    assert human_to_bytes('1.1k') == 1099
    assert human_to_bytes('1.1K') == 1099
    assert human

# Generated at 2022-06-12 23:50:40.488942
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:50:46.759232
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Unit test for function human_to_bytes.
    '''

    from units import assert_equal

    assert_equal(human_to_bytes('2K'), 2048)
    assert_equal(human_to_bytes('1M'), 1048576)
    assert_equal(human_to_bytes('100G'), 100 * 1024 * 1024 * 1024)
    assert_equal(human_to_bytes('2m'), 2 * 1024 * 1024)
    assert_equal(human_to_bytes('123.456M'), int(123.456 * 1024 * 1024))
    assert_equal(human_to_bytes('124.456M'), int(124.456 * 1024 * 1024))
    assert_equal(human_to_bytes('124.455M'), int(124.455 * 1024 * 1024))

# Generated at 2022-06-12 23:50:57.938380
# Unit test for function human_to_bytes
def test_human_to_bytes():
    data = {'1M': 1048576,
            '1Mb': 1048576,
            '10MB': 10485760,
            '10240kb': 10485760,
            '1k': 1024,
            '1b': 1,
            '1Kb': 1024,
            '10MBb': 10485760,
            '1MBb': 1048576,
            '1Mbb': 1048576}
    for item in data:
        result = human_to_bytes(item)
        if result == data[item]:
            print('Test for %s Passed' % item)
        else:
            print('Test for %s Failed' % item)
            print('Result: %s Should be: %s' % (result, data[item]))

# Generated at 2022-06-12 23:51:01.636994
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['123', 'abc', '_._']) == ['123', 'abc', '_._']

# Unit tests for function human_to_bytes
# TODO: If a test fails, the message that is printed is hard to understand.
# Print the input/output values and the test name.


# Generated at 2022-06-12 23:51:05.077477
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    original_list = [1, 2, [3, 4, ['A', 'B']], 'C']
    expected_list = [1, 2, [3, 4, ['A', 'B']], 'c']
    result_list = lenient_lowercase(original_list)
    assert result_list == expected_list

# Generated at 2022-06-12 23:51:16.587298
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:23.660603
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    """Unit test for lenient_lowercase."""
    lst = ['test1', 'test2', 'test3']
    assert lenient_lowercase(lst) == lst, 'test1'
    lst = [123, 'test2', 'test3']
    assert lenient_lowercase(lst) == lst, 'test2'
    lst = ['TEST1', 'test2', 'test3']
    assert lenient_lowercase(lst) == ['test1', 'test2', 'test3'], 'test3'



# Generated at 2022-06-12 23:51:36.384121
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Testing bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('2b') == 2
    assert human_to_bytes('3.3b') == 3
    assert human_to_bytes('4.8B') == 4
    assert human_to_bytes('.5B') == 0
    assert human_to_bytes('1.5B') == 1
    assert human_to_bytes('0.5B') == 0

    assert human_to_bytes('1.0B') == 1
    assert human_to_bytes(1.0) == 1

    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1.0KB') == 1024
    assert human_to_bytes('1Kb') == 1024

# Generated at 2022-06-12 23:51:47.004118
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:57.407390
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import sys
    import difflib
    from io import StringIO

    def compare(output, expected):
        for l in difflib.unified_diff(expected.split('\n'), output.split('\n'), fromfile='expected', tofile='output'):
            sys.stdout.write(l)

    # Capture stdout.
    old_stdout = sys.stdout
    test_stdout = StringIO()
    sys.stdout = test_stdout
    captures = []

# Generated at 2022-06-12 23:52:04.649117
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["TEST", "TEST", "TEST"]) == ["test", "test", "test"]
    assert lenient_lowercase(["TEST", None, "TEST"]) == ["test", None, "test"]
    assert lenient_lowercase(["test", "TEST", "TEST"]) == ["test", "test", "test"]
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-12 23:52:07.511307
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase(['A', 1, 'B']) == ['a', 1, 'b']


# Generated at 2022-06-12 23:52:18.420393
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('10K') == 10240
    assert human_to_bytes('10KB') == 10240
    assert human_to_bytes('1.1Kb') == 1128
    assert human_to_bytes('10.5MB') == 10485760
    assert human_to_bytes('10.5Mb') == 1050000
    assert human_to_bytes('13.5B') == 14
    assert human_to_bytes('1.3KB') == 1331
    assert human_to_bytes('1.3MB') == 1363148
    assert human_to_bytes('1.3Mb') == 1370000
    assert human_to_bytes('1.3TB') == 137438

# Generated at 2022-06-12 23:52:20.982212
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]



# Generated at 2022-06-12 23:52:26.039561
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test that lenient_lowercase properly lowercases lists of strings
    assert lenient_lowercase(['one', 'TWO', 'THRee']) == ['one', 'two', 'three']

    # Test that lenient_lowercase passes through non-string elements like ints
    assert lenient_lowercase(['ONE', 'TWO', 3, 'Four']) == ['one', 'two', 3, 'Four']

# Generated at 2022-06-12 23:52:32.928593
# Unit test for function human_to_bytes
def test_human_to_bytes():
    try:
        assert human_to_bytes('1M') == 1048576
    except Exception as e:
        raise AssertionError('Testing "1M" failed %s' % (e))
    try:
        assert human_to_bytes('1Mb', isbits=True) == 1048576
    except Exception as e:
        raise AssertionError('Testing "1Mb" failed %s' % (e))
    try:
        assert human_to_bytes('2k') == 2048
    except Exception as e:
        raise AssertionError('Testing "2k" failed %s' % (e))
    try:
        assert human_to_bytes('2kb', isbits=True) == 2048
    except Exception as e:
        raise AssertionError('Testing "2kb" failed %s' % (e))

# Generated at 2022-06-12 23:52:43.479555
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''Test for function human_to_bytes'''
    case_list = dict()

    # Test for Bytes to Bytes
    case_list['1B'] = [1, 'B']
    case_list['0B'] = [0, 'B']
    case_list['100B'] = [100, 'B']
    case_list['1B B'] = [1, 'B']
    case_list['1024B'] = [1024, 'B']
    case_list['1KB'] = [1024, 'B']
    case_list['10KB'] = [10240, 'B']
    case_list['100KB'] = [102400, 'B']
    case_list['1MB'] = [1048576, 'B']
    case_list['10MB'] = [10485760, 'B']

# Generated at 2022-06-12 23:52:58.450146
# Unit test for function human_to_bytes
def test_human_to_bytes():

    assert(human_to_bytes("100", "B") == 100)
    assert(human_to_bytes("1B", "B") == 1)
    assert(human_to_bytes("1", "B") == 1)
    assert(human_to_bytes("10KB") == 10240)
    assert(human_to_bytes("10MB", isbits=True) == 10485760)
    assert(human_to_bytes("10M") == 10485760)
    assert(human_to_bytes("10Mb", isbits=True) == 10485760)
    assert(human_to_bytes("10K") == 102400)
    assert(human_to_bytes("100M") == 104857600)

# Generated at 2022-06-12 23:53:05.531525
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Bytes related tests
    assert human_to_bytes(2) == 2, 'Conversion of integer not working'
    assert human_to_bytes('10M') == 10485760, 'Conversion of "10M" not working'
    assert human_to_bytes('10M', unit='M') == 10485760, 'Conversion of "10M" not working'
    assert human_to_bytes('10M', unit='m') == 10485760, 'Conversion of "10M" not working'
    assert human_to_bytes('10M', unit='M') == 10485760, 'Conversion of "10M" not working'
    assert human_to_bytes('10Mb', unit='b') == 10485760, 'Conversion of "10Mb" not working'
    assert human_to_bytes

# Generated at 2022-06-12 23:53:17.248441
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1 Mb', isbits=True) == 1048576, "'1 Mb' string with isbits=True should return number of bits"
    assert human_to_bytes('10M') == 10485760, '10M (without unit) should return 10485760'
    assert human_to_bytes('10M', 'b') == 10485760, "'10M' with 'b' unit should return 10485760"
    assert human_to_bytes('5Kb') == 5120, "'5Kb' string should return number of bits"
    assert human_to_bytes('5 KB') == 5120, "'5 KB' string should return number of bits"
    assert human_to_bytes('1.2G', 'b') == 128849

# Generated at 2022-06-12 23:53:25.328154
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # convert gibibytes
    assert human_to_bytes('1GiB') == 1073741824

    # convert mebibytes
    assert human_to_bytes('1MiB') == 1048576

    # convert kibibytes
    assert human_to_bytes('1KiB') == 1024

    # convert gibibits
    assert human_to_bytes('1Gb', isbits=True) == 1000000000

    # convert mebibits
    assert human_to_bytes('1Mb', isbits=True) == 1000000

    # convert kibibits
    assert human_to_bytes('1Kb', isbits=True) == 1000

    # convert gibibits
    assert human_to_bytes('1Gb', unit='b', isbits=True) == 1000000000

    # convert mebibits

# Generated at 2022-06-12 23:53:34.645105
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a', 'b'] == lenient_lowercase(['a', 'b'])
    assert ['a', 'b'] == lenient_lowercase(['A', 'b'])
    assert ['a', 'b'] == lenient_lowercase(['A', 'B'])
    assert ['a', 'b'] == lenient_lowercase(['a', 'B'])
    assert [1, 'b'] == lenient_lowercase([1, 'b'])
    assert ['a', 1] == lenient_lowercase(['a', 1])
    assert [1, 1] == lenient_lowercase([1, 1])

# Generated at 2022-06-12 23:53:44.452237
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:54.115901
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''Testing human_to_bytes function to convert from human readable format to bytes (isbits == False)'''
    # bits
    assert human_to_bytes('10b', isbits=True) == 10
    assert human_to_bytes('10B', isbits=True) == 0
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('10MB', isbits=True) == 0
    assert human_to_bytes('10Kb', isbits=True) == 10240
    assert human_to_bytes('10KB', isbits=True) == 0
    assert human_to_bytes('10b', isbits=False) == 0
    assert human_to_bytes('10B', isbits=False) == 10

# Generated at 2022-06-12 23:53:59.818729
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['1', '2', 3, '4']) == ['1', '2', 3, '4']
    assert lenient_lowercase(['1', '2', 3, '4']) != ['1', '2', 3, '4'].lower()
    assert lenient_lowercase(['1', '2', 3, '4']) != ['1', '2', 3, '4'].upper()


# Generated at 2022-06-12 23:54:02.112709
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'Z']) == ['a', 'B', 'Z']

# Generated at 2022-06-12 23:54:06.180877
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 1048576


# Generated at 2022-06-12 23:54:19.744201
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ABC', 'DEF']) == ['abc', 'def']
    assert lenient_lowercase(['GHI', 456]) == ['ghi', 456]



# Generated at 2022-06-12 23:54:25.221994
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 'B', 'c', 1, 2]) == ['a', 'b', 'c', 1, 2]
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['Ab123']) == ['ab123']
    assert lenient_lowercase(['Ab/123']) == ['ab/123']
    assert lenient_lowercase(['Ab/123-$#!']) == ['ab/123-$#!']



# Generated at 2022-06-12 23:54:36.083414
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:42.580000
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M') == 1048576

    with pytest.raises(ValueError) as excinfo:
        human_to_bytes('1.1M')
        assert excinfo.match(r'human_to_bytes\(\) can\'t interpret following string: 1.1M')

    with pytest.raises(ValueError) as excinfo:
        human_to_bytes('E')
        assert excinfo.match(r'human_to_bytes\(\) can\'t interpret following number: E \(original input string: E\)')

    with pytest.raises(ValueError) as excinfo:
        human_to_bytes('Kb')

# Generated at 2022-06-12 23:54:43.199444
# Unit test for function human_to_bytes
def test_human_to_bytes():
    pass

# Generated at 2022-06-12 23:54:50.317100
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from nose.tools import assert_equal

    # KB and MB without unit test
    assert_equal(human_to_bytes('2048'), 2048)
    assert_equal(human_to_bytes('2048000'), 2048000)

    # Bytes
    assert_equal(human_to_bytes('2B'), 2)
    assert_equal(human_to_bytes('2b', isbits=True), 2)
    assert_equal(human_to_bytes('2'), 2)
    assert_equal(human_to_bytes('2', default_unit='B'), 2)

    # KB
    assert_equal(human_to_bytes('2KB'), 2048)
    assert_equal(human_to_bytes('2Kb', isbits=True), 2048)

# Generated at 2022-06-12 23:55:02.682753
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test for bytes
    if human_to_bytes('1B') != 1:
        raise AssertionError("human_to_bytes('1B') should return 1")

    if human_to_bytes('1B') != human_to_bytes('1', 'B'):
        raise AssertionError("human_to_bytes('1B') should be the same as human_to_bytes('1', 'B')")

    if human_to_bytes('1', 'B') != human_to_bytes('1', 'byte'):
        raise AssertionError("human_to_bytes('1', 'B') should be the same as human_to_bytes('1', 'byte')")


# Generated at 2022-06-12 23:55:11.290697
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:21.618223
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.0MB') == 1048576
    assert human_to_bytes('1.0MB', default_unit='B') == 1048576
    assert human_to_bytes('1MB', default_unit='b') == 1048576
    assert human_to_bytes('1.0Mb') == 1048576
    assert human_to_bytes('1.0Mb', isbits=True) == 1048576
    assert human_to_bytes('1.0Kb') == 1024
    assert human_to_bytes('1.0Kb', isbits=True) == 1024
    assert human_to_bytes('1b') == 1

# Generated at 2022-06-12 23:55:34.193431
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2.2K') == 2 * 1024 + 200
    assert human_to_bytes('-2.2K') == -2 * 1024 - 200
    assert human_to_bytes('+2.2K') == 2 * 1024 + 200
    assert human_to_bytes('.2K', default_unit='B') == 0.2 * 1024
    assert human_to_bytes('-2.2b') == -2 * 1024 - 200
    assert human_to_bytes('+.2K', default_unit='B') == 0.2 * 1024
    assert human_to_bytes('2b') == 2
    assert human_to_bytes('-2b') == -2
    assert human_to_bytes('+2b') == 2
    assert human_to_bytes('2B') == 2
    assert human_to

# Generated at 2022-06-12 23:55:51.789063
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M', isbits=True) == 1048576
    assert human_to_bytes('10G', isbits=True) == 10737418240
    assert human_to_bytes('10Gb', isbits=True) == 10737418240
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('10MB', isbits=True) == 10485760
    assert human_to_bytes('10MB', unit='mb', isbits=True) == 10485760
    assert human_to_bytes('10mb', unit='mb', isbits=True) == 10485760
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Bb', isbits=True)

# Generated at 2022-06-12 23:56:04.125132
# Unit test for function human_to_bytes
def test_human_to_bytes():

    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B') == 1

    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1B', isbits=True) == 1

    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1Gb') == 1073741824
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1B', isbits=True) == 1

# Generated at 2022-06-12 23:56:06.903995
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    sample_list = ['Foo', 1, 'BAR']
    result_list = ['foo', 1, 'bar']
    assert(lenient_lowercase(sample_list) == result_list)

# Generated at 2022-06-12 23:56:15.415910
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:56:18.545179
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 1, 2, 'B']) == ['a', 1, 2, 'b']


# Generated at 2022-06-12 23:56:26.969066
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Base cases
    assert human_to_bytes('0') == 0
    assert human_to_bytes('0 ') == 0
    assert human_to_bytes('') == 0
    assert human_to_bytes('0B') == 0
    assert human_to_bytes('0B', unit='B') == 0
    assert human_to_bytes('0b', isbits=True) == 0
    assert human_to_bytes('0b', isbits=True, unit='b') == 0

    # Wanted behavior
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1 ', default_unit='B') == 1
    assert human_to_bytes('1 ', default_unit='b') == 1
    assert human_to_bytes('1 ', default_unit='K') == 1024
    assert human_to

# Generated at 2022-06-12 23:56:31.384536
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'C']) == ['a', 'b', 'C']
    assert lenient_lowercase(['a', 'b', ['C', 'D']]) == ['a', 'b', ['C', 'D']]


# Generated at 2022-06-12 23:56:33.209083
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["A", [], {}]) == ["a", [], {}]

# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:56:37.236005
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['TEST', 'ABC']) == ['test', 'abc']
    assert lenient_lowercase(['TEST', 123]) == ['test', 123]
    assert lenient_lowercase([123, 'test']) == [123, 'test']


# Generated at 2022-06-12 23:56:44.883169
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:16.343094
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1', default_unit='M') == 1048576
    assert human_to_bytes('1000', default_unit='M') == 1048576000
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1m') == 1048576
    assert human_to_bytes('1M', default_unit='GB') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB', default_unit='KB') == 1048576
    assert human_to_bytes('1MB', default_unit='KB', isbits=True) == 8388608
    assert human_to_bytes('1MB', isbits=True) == 8388608

# Generated at 2022-06-12 23:57:23.381378
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test for string inputs
    test_string = 'Test String'
    assert lenient_lowercase([test_string]) == [test_string.lower()]

    # Test strings in a list
    test_string_list = ['Test String1', 'Test String2', 'Test String3']
    assert lenient_lowercase(test_string_list) == [i.lower() for i in test_string_list]

    # Test list with integers
    test_int_list = [1, 2, 3]
    assert lenient_lowercase(test_int_list) == test_int_list

    # Test list with integer and string
    test_int_string_list = [1, 'Test String1']
    assert lenient_lowercase(test_int_string_list) == test_int_string_list

# Unit test

# Generated at 2022-06-12 23:57:30.174567
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M')
    assert human_to_bytes('-10M') == human_to_bytes(-10, 'M')
    assert human_to_bytes('0M') == human_to_bytes(0, 'M')

    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB', isbits=True) == 8388608
    assert human_to_bytes('1MB', isbits=True) == human_to_bytes(8388608, 'b')

    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('10G') == 10737418240
    assert human_to_bytes('10G', 'B') == 10737418240
    assert human

# Generated at 2022-06-12 23:57:35.236629
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C', 'D']) == ['a', 'b', 'c', 'd']
    assert lenient_lowercase(['A', 'B', 1, 'C', 'D']) == ['a', 'b', 1, 'c', 'd']


# Generated at 2022-06-12 23:57:39.245057
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    strings = ['a', 'B', 'C', '1', 1, 'hello there', 'HELLO THERE', '  \t\n']
    target = ['a', 'b', 'c', '1', 1, 'hello there', 'hello there', '  \t\n']
    assert lenient_lowercase(strings) == target

# Generated at 2022-06-12 23:57:42.103706
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'c', True, 1, 2]) == ['a', 'b', 'c', True, 1, 2]

# Generated at 2022-06-12 23:57:51.053328
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['FOO', 1]) == ['foo', 1]
    assert lenient_lowercase([1, 'FOO']) == [1, 'FOO']
    assert lenient_lowercase(['foo', 1, 'BAR']) == ['foo', 1, 'BAR']
    assert lenient_lowercase([1, 'foo', 'BAR']) == [1, 'foo', 'BAR']
    assert lenient_lowercase([1, 'foo', 'bar']) == [1, 'foo', 'bar']
    assert lenient_lowercase(['FOO', 'bar']) == ['foo', 'bar']
    assert lenient_lowercase(['FOO', 'bar']) == ['foo', 'bar']


# Generated at 2022-06-12 23:57:55.545175
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:58:00.499900
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['g', 'O', 'D']) == ['g', 'o', 'd']
    assert lenient_lowercase(['g', None, 'D']) == ['g', None, 'd']

# Generated at 2022-06-12 23:58:10.977027
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = [
        ('10M', 10485760),
        ('1G', 1073741824),
        ('10', 10),
        ('10K', 10240),
    ]
    for test_input, expected_result in tests:
        assert human_to_bytes(test_input) == expected_result, 'human_to_bytes("%s") is expected to return %s, but returned %s' % (test_input, expected_result, human_to_bytes(test_input))

    # add bad input tests
    bad_tests = [
        ('10X', ValueError),
        ('bad_input', ValueError),
        ('', ValueError),
        ('10Kb', ValueError),
        ('12.3M', ValueError),
    ]