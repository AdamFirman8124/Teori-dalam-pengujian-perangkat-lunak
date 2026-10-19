

# Generated at 2022-06-12 23:48:44.583938
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, "abc", "AbC", ["x", "y", "Z"]]
    assert lenient_lowercase(lst) == [1, "abc", "abc", ["x", "y", "z"]]


# Generated at 2022-06-12 23:48:54.731273
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = [('10M', 10485760), ('10Mb', 10485760), ('1MB', 1048576), ('1MBb', 10240), ('10', 10)]

    for case, expect in tests:
        output = human_to_bytes(case)
        assert output == expect, "Error: human_to_bytes('%s') returned wrong value: %i != %i" % (case, output, expect)

    # try failed cases
    failed_cases = ['10MBb', '10MbB', '10MBB', '10MB', '10b', '10MBbB', 'KB', 'KBb', '10K', '10KBb', '10KBB', '10KB', '10BB']


# Generated at 2022-06-12 23:49:05.618006
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Test can't be run automatically, because we don't want to print test results
    when running tests with: ansible-test sanity --test pylint
    Manually run test with:
    python -m pytest pylint_runner/lib/human_to_bytes.py -k test_human_to_bytes
    '''
    pass  # pylint: disable=unnecessary-pass

# Generated at 2022-06-12 23:49:08.289125
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'ABC', 'aBc', u'abc', None]) == [1, 'abc', 'abc', u'abc', None]

# Generated at 2022-06-12 23:49:14.673600
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:21.031749
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1Mb') == 131072
    assert human_to_bytes('1mB', isbits=True) == 131072

    assert human_to_bytes('1Mb', isbits=True) == 131072
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 131072

    assert human_to_bytes('1Kb', isbits=True) == 128
    assert human_to_bytes('1KB') == 1024

    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1B') == 1



# Generated at 2022-06-12 23:49:31.890460
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(2, 'K') == 2048
    assert human_to_bytes(2) == 2
    assert human_to_bytes('2') == 2
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b', isbits=True) == 10
    assert human_to_bytes('10B', isbits=True) == 8
    assert human_to_bytes('10b', 'b', True) == 10
    assert human_to_bytes('10B', 'b', True) == 8
    assert human_to_bytes('10b', 'B', True) == 10

# Generated at 2022-06-12 23:49:42.931552
# Unit test for function human_to_bytes
def test_human_to_bytes():
    units = ['Y', 'Z', 'E', 'P', 'T', 'G', 'M', 'K', 'B', 'b']
    for unit in units:
        expected_value = human_to_bytes('1%s'%unit, default_unit=unit)
        assert expected_value == 1, 'Unexpected value for 1%s == %d (expected 1)'%(unit, expected_value)

    for unit in units:
        expected_value = human_to_bytes('1.5%s'%unit, default_unit=unit)
        assert expected_value == 1, 'Unexpected value for 1.5%s == %d (expected 1)'%(unit, expected_value)

    expected_value = human_to_bytes('-1B')

# Generated at 2022-06-12 23:49:48.147580
# Unit test for function bytes_to_human
def test_bytes_to_human():
    from nose.tools import assert_equal


# Generated at 2022-06-12 23:49:51.226561
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('5') == 5
    assert human_to_bytes('5.5') == 5
    assert human_to_bytes('5.5kb') == 5632



# Generated at 2022-06-12 23:49:58.539943
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == '1 Bytes'
    assert bytes_to_human(2) == '2 Bytes'

    assert bytes_to_human(1000000) == '976.56 KiB'
    assert bytes_to_human(1000000000) == '953.67 MiB'
    assert bytes_to_human(1000000000000) == '931.32 GiB'
    assert bytes_to_human(1000000000000000) == '909.49 TiB'
    assert bytes_to_human(1000000000000000000) == '888.18 PiB'

    # unit test
    assert bytes_to_human(1, unit='B') == '1 B'
    assert bytes_to_human(2, unit='B') == '2 B'


# Generated at 2022-06-12 23:50:07.055238
# Unit test for function bytes_to_human
def test_bytes_to_human():
    if bytes_to_human(2048) != '2.00 KB':
        return False
    if bytes_to_human(1) != '1.00 Byte':
        return False
    if bytes_to_human(62, unit='b') != '62.00 B':
        return False
    if bytes_to_human(2048, unit='b') != '16.00 KB':
        return False
    if bytes_to_human(2**20, isbits=True) != '1.00 Mb':
        return False
    if bytes_to_human(2**20, isbits=True, unit='b') != '1.00 Mb':
        return False
    if bytes_to_human(2**20, isbits=True, unit='b') != '1.00 Mb':
        return False

# Generated at 2022-06-12 23:50:17.226519
# Unit test for function bytes_to_human
def test_bytes_to_human():
    test_data = [
        (1024, '1.00 KBytes'),
        (1048576, '1.00 MBytes'),
        (1073741824, '1.00 GBytes'),
        (1099511627776, '1.00 TBytes'),
        (1125899906842624, '1.00 PBytes'),
        (1152921504606846976, '1.00 EBytes'),
        (1180591620717411303424, '1.00 ZBytes'),
        (1208925819614629174706176, '1.00 YBytes')
    ]
    for size, expected in test_data:
        result = bytes_to_human(size)
        assert result == expected

# Generated at 2022-06-12 23:50:27.447676
# Unit test for function bytes_to_human
def test_bytes_to_human():
    print('Unit test')
    print('=========')
    print()
    print('Test 1')
    value = bytes_to_human(1048576)
    print('Assert 1048576 Bytes == 1MB ...', end='')
    assert value == '1.00 MB'
    print('OK')
    print()
    print('Test 2')
    value = bytes_to_human(1048576, unit='M')
    print('Assert 1048576 Bytes == 1M ...', end='')
    assert value == '1.00 M'
    print('OK')
    print()
    print('Test 3')
    value = bytes_to_human(1048576, unit='m')
    print('Assert 1048576 Bytes == 1M ...', end='')

# Generated at 2022-06-12 23:50:31.476930
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, 'a', 'b', 9, 'c']
    assert lenient_lowercase(lst) == [1, 'a', 'b', 9, 'c']



# Generated at 2022-06-12 23:50:41.907192
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # to bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('2B') == 2
    assert human_to_bytes('1') == 1
    assert human_to_bytes('2') == 2
    assert human_to_bytes('1 K') == 1024
    assert human_to_bytes('2 k') == 2048
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('2m') == 2097152
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('2g') == 2147483648
    assert human_to_bytes('1 t') == 1099511627776
    assert human_to_bytes('2 t') == 2199023255552

# Generated at 2022-06-12 23:50:50.613015
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test string
    assert lenient_lowercase(['string']) == ['string']
    assert lenient_lowercase([u'string']) == ['string']
    assert lenient_lowercase(['String']) == ['string']
    # Test None
    assert lenient_lowercase(['None']) == ['none']
    assert lenient_lowercase([None]) == [None]
    # Test int
    assert lenient_lowercase([42]) == [42]
    # Test True
    assert lenient_lowercase(['True']) == ['true']
    assert lenient_lowercase([True]) == [True]
    # Test False
    assert lenient_lowercase(['False']) == ['false']
    assert lenient_lowercase([False]) == [False]
    # Test list and dict
    assert len

# Generated at 2022-06-12 23:51:01.322509
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1025) == '1.00 KB'
    assert bytes_to_human(1026) == '1.00 KB'
    assert bytes_to_human(1023) == '1023.00 B'
    assert bytes_to_human(10240) == '10.00 KB'
    assert bytes_to_human(1048576) == '1.00 MB'
    assert bytes_to_human(1048576+1) == '1.00 MB'
    assert bytes_to_human(1048576-1) == '1048575.00 B'
    assert bytes_to_human(10485760) == '10.00 MB'

# Generated at 2022-06-12 23:51:05.386301
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['lower', 'lower2', 'UPPER', 'UPPER2', 'mIxEd', 'mIxEd2', 1, 2, 3, 4, '4']) == ['lower', 'lower2', 'upper', 'upper2', 'mixed', 'mixed2', 1, 2, 3, 4, '4']


# Generated at 2022-06-12 23:51:16.967842
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1024, False, 'b') == '1024 Bytes'
    assert bytes_to_human(1024, False, 'B') == '1.00 KB'
    assert bytes_to_human(1024, False, 'K') == '1.00 KB'
    assert bytes_to_human(1024, False) == '1.00 KB'
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1024, False, 'Kb') == '1024 Bytes'
    assert bytes_to_human(1024, False, 'KB') == '1.00 KB'
    assert bytes_to_human(1024, False, 'kB') == '1.00 KB'
    assert bytes_to_human(1024, False, 'k') == '1.00 KB'
   

# Generated at 2022-06-12 23:51:28.610845
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Test function human_to_bytes"""
    # Identity function with default unit
    assert human_to_bytes(human_to_bytes('10M', 'M')) == 10

    # Conversion with default unit
    assert human_to_bytes('10M', 'M') == 10

    # Conversion with specified unit
    assert human_to_bytes('10', 'M') == 10485760

    # Conversion fails when expected unit is not the one specified
    try:
        human_to_bytes('10M', 'K')
        assert False, '10M to K should fail because it does not match the expected unit'
    except ValueError:
        pass

    # Conversion fails when format is wrong

# Generated at 2022-06-12 23:51:36.437216
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Positive test cases
    # 'B' is converted to 1
    assert human_to_bytes('B') == 1
    # 'KB' is converted to 1 KB
    assert human_to_bytes('1KB') == 1024
    # 'MB' is converted to 1 MB
    assert human_to_bytes('1MB') == 1048576
    # 'GB' is converted to 1 GB
    assert human_to_bytes('1GB') == 1073741824
    # 'TB' is converted to 1 TB
    assert human_to_bytes('1TB') == 1099511627776
    # 'PB' is converted to 1 PB
    assert human_to_bytes('1PB') == 1125899906842624
    # 'EB' is converted to 1 EB
    assert human_to_bytes('1EB') == 11529215046068469

# Generated at 2022-06-12 23:51:47.138682
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('1B') == 1)
    assert(human_to_bytes('1') == 1)
    assert(human_to_bytes('3M') == 3145728)
    assert(human_to_bytes('1Mb', isbits=True) == 1048576)
    assert(human_to_bytes('1kb', isbits=True) == 1024)
    assert(human_to_bytes('1.1234M') == 1176867)
    assert(human_to_bytes('12B', 'M') == 12)
    assert(human_to_bytes('12', 'M') == 12)
    assert(human_to_bytes('12.34M', 'M') == 12)

# Generated at 2022-06-12 23:51:57.539517
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest
    with pytest.raises(ValueError):
        assert human_to_bytes('512')
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('512B') == 512
    assert human_to_bytes('1KB', isbits=True) == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1MB', isbits=True) == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1mb') == 1048576
    assert human_to_bytes('1GB', isbits=True) == 1073741824
    assert human_to

# Generated at 2022-06-12 23:52:01.502340
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["FoOBAR", "FOOBAR", "fooBAR", "foobar"]) == ["foobar", "FOOBAR", "fooBAR", "foobar"]



# Generated at 2022-06-12 23:52:12.730799
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # without units.
    n = human_to_bytes(1)
    assert n == 1

    n = human_to_bytes(2)
    assert n == 2

    n = human_to_bytes(3)
    assert n == 3

    n = human_to_bytes(1.1)
    assert n == 1.1

    n = human_to_bytes(2.2)
    assert n == 2.2

    n = human_to_bytes(3.3)
    assert n == 3.3

    # with units.
    n = human_to_bytes('1B')
    assert n == 1

    n = human_to_bytes('2B')
    assert n == 2

    n = human_to_bytes('3B')
    assert n == 3


# Generated at 2022-06-12 23:52:18.137867
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [["test1", None, 'test2', 1], ["test1", None, 'test2', 'test3'], [None, 1]]
    results = [["test1", None, "test2", 1], ["test1", None, "test2", "test3"], [None, 1]]
    for idx, test_l in enumerate(test_list):
        assert results[idx] == lenient_lowercase(test_l)

# Generated at 2022-06-12 23:52:20.106460
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['FOO', 'Bar', 42]) == ['foo', 'bar', 42]

# Generated at 2022-06-12 23:52:28.991205
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('100B') == 100
    assert human_to_bytes('100b') == 100
    assert human_to_bytes('100b', isbits=True) == 100
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB', isbits=True) == 1048576
    assert human_to_bytes('1M', unit='b') == 1048576
    assert human_to_bytes('1Mb', unit='b', isbits=True) == 1048576

# Generated at 2022-06-12 23:52:40.581338
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    ''' Unit test for lenient_lowercase function. '''
    assert lenient_lowercase("no conversion") == ['no conversion']
    assert lenient_lowercase("NO CONversion") == ['no conversion']
    assert lenient_lowercase("NO CONVERSION") == ['no conversion']
    assert lenient_lowercase("no CONVERSION") == ['no conversion']
    assert lenient_lowercase("no conversion", ) == ['no conversion']
    assert lenient_lowercase("no conversion", ) == ['no conversion']
    assert lenient_lowercase("no conversion", "mixed",) == ['no conversion', 'mixed']
    assert lenient_lowercase("no conversion", "MIXED",) == ['no conversion', 'mixed']

# Generated at 2022-06-12 23:52:53.839940
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Default size unit is byte case
    # test simple value
    assert human_to_bytes('1') == 1
    # test value 10
    assert human_to_bytes('10') == 10
    # test value '10.5'
    assert human_to_bytes('10.5') == 10
    # test value 10.5
    assert human_to_bytes(10.5) == 10
    # test value '10.0'
    assert human_to_bytes('10.0') == 10
    # test value 10.0
    assert human_to_bytes(10.0) == 10
    # test value '10.5ab'
    assert human_to_bytes('10.5ab') == 10
    # test value '12.5M'
    assert human_to_bytes('12.5M') == 134217728

# Generated at 2022-06-12 23:52:55.611138
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['abc', 'abc', 'abc'] == lenient_lowercase(['abc', 1, 'ABC'])
    assert ['abc', 'abc'] == lenient_lowercase(['abc', 'ABC'])
    assert [] == lenient_lowercase([])


# Generated at 2022-06-12 23:53:02.147887
# Unit test for function human_to_bytes
def test_human_to_bytes():
    a = human_to_bytes('2K')
    assert a == 2048

    b = human_to_bytes('2KB')
    assert b == 2048

    c = human_to_bytes('2M')
    assert c == 2097152

    d = human_to_bytes('2m')
    assert d == 2097152

    e = human_to_bytes('2')
    assert e == 2

    f = human_to_bytes('2.5K')
    assert f == 2560

    g = human_to_bytes('2.5K', isbits=True)
    assert g == 2560 * 8

# Generated at 2022-06-12 23:53:11.868390
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, '3', '4', '5']) == [1, 2, '3', '4', '5']
    assert lenient_lowercase(['1', '2', '3', '4', '5']) == ['1', '2', '3', '4', '5']
    assert lenient_lowercase(['A', '2', '3', '4', '5']) == ['a', '2', '3', '4', '5']
    assert lenient_lowercase(['A', 'B', '3', '4', '5']) == ['a', 'b', '3', '4', '5']

# Generated at 2022-06-12 23:53:21.870084
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Testing bytes
    test = '1K'
    result = human_to_bytes(test)
    assert result == 1024

    test = '1M'
    result = human_to_bytes(test)
    assert result == 1048576

    test = '1G'
    result = human_to_bytes(test)
    assert result == 1073741824

    test = '1T'
    result = human_to_bytes(test)
    assert result == 1099511627776

    test = '1P'
    result = human_to_bytes(test)
    assert result == 1125899906842624

    test = '1E'
    result = human_to_bytes(test)
    assert result == 1152921504606846976

    test = '1Z'
    result = human_to_bytes

# Generated at 2022-06-12 23:53:25.157020
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'a', 'B', {'c': 'D'}]) == [1, 'a', 'b', {'c': 'D'}]


# Generated at 2022-06-12 23:53:36.437511
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    test_human_to_bytes() runs tests for function human_to_bytes()
    '''
    # cases for bytes

# Generated at 2022-06-12 23:53:39.856926
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Foo', 2, 'Bar']) == ['foo', 2, 'bar']
    assert lenient_lowercase(['FOO', 2, 'BAR']) == ['foo', 2, 'bar']


# Generated at 2022-06-12 23:53:45.360846
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # TODO: more tests needed
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10K') == 10240

    assert human_to_bytes('10 kb') == 10240
    assert human_to_bytes('10 KB') == 10240

    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1kb') == 1024

    assert human_to_bytes('1MB') == 1048576

# Generated at 2022-06-12 23:53:55.825744
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    ''' Test lenient lowercase function '''

# Generated at 2022-06-12 23:54:02.788043
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 'B', 'C']) == [1, 'b', 'c']

# Generated at 2022-06-12 23:54:11.540533
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes('1.6') == 2
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10.0') == 10
    assert human_to_bytes('10.5') == 11
    assert human_to_bytes('10.6') == 11
    assert human_to_bytes('10MB') == 10 * (1 << 20)
    assert human_to_bytes('10 Mb') == 10 * (1 << 20)
    assert human_to_bytes('10 mb') == 10 * (1 << 20)
    assert human_to_bytes('10 MB') == 10 * (1 << 20)

# Generated at 2022-06-12 23:54:15.680625
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['aa', 'BB', 'CC'] == lenient_lowercase(['AA', 'BB', 'CC'])
    assert [1, 'BB', 'CC'] == lenient_lowercase([1, 'BB', 'CC'])

# Generated at 2022-06-12 23:54:24.493386
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:35.476314
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Check exception raise
    # ValueError when number is not a string
    try:
        human_to_bytes(2)
    except ValueError:
        pass
    else:
        assert False

    # ValueError when number is not a string
    try:
        human_to_bytes('2MB')
    except ValueError:
        pass
    else:
        assert False

    # ValueError when no unit provided and default unit is None
    try:
        human_to_bytes('10')
    except ValueError:
        pass
    else:
        assert False

    # ValueError when no unit provided and default unit is invalid
    try:
        human_to_bytes('10', default_unit='m')
    except ValueError:
        pass
    else:
        assert False

    # ValueError when unit is invalid

# Generated at 2022-06-12 23:54:37.748941
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    values = ['XYZ', 'abc', ['xyz', 'ABC', 'aaa'], {}, 1]
    lowered = lenient_lowercase(values)

    assert lowered == ['xyz', 'abc', ['xyz', 'abc', 'aaa'], {}, 1]

# Generated at 2022-06-12 23:54:43.729430
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test parsing string bytes representation
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1Kb') == 1 << 10
    assert human_to_bytes('1KB') == 1 << 10
    assert human_to_bytes('1Mb') == 1 << 20
    assert human_to_bytes('1MB') == 1 << 20
    assert human_to_bytes('1Gb') == 1 << 30
    assert human_to_bytes('1GB') == 1 << 30
    assert human_to_bytes('1Tb') == 1 << 40
    assert human_to_bytes('1TB') == 1 << 40
    assert human_to_bytes('1Pb') == 1 << 50

# Generated at 2022-06-12 23:54:45.352047
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    data = ['a', 'b', 1, 'C', 'D', 2]
    assert data == lenient_lowercase(data)



# Generated at 2022-06-12 23:54:51.288288
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:57.433391
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 100, 'c']) == ['a', 100, 'c']



# Generated at 2022-06-12 23:55:08.469362
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c', 1]) == ['a', 'b', 'c', 1]
    assert lenient_lowercase(('a', 'b', 'c', 1)) == ['a', 'b', 'c', 1]


# Generated at 2022-06-12 23:55:19.304706
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10m') == 10485760
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes(10) == 10
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB', unit='KB') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1Mb', unit='KB') == 1048576
    assert human_to_bytes('1kB') == 1024
    assert human_to_bytes('1KB') == 1000
    assert human_to_

# Generated at 2022-06-12 23:55:31.115610
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:38.612035
# Unit test for function human_to_bytes
def test_human_to_bytes():
    def assert_bytes(value, unit=None):
        assert human_to_bytes(value, unit=unit) == int(value)

    def assert_bits(value, unit=None):
        assert human_to_bytes(value, isbits=True, unit=unit) == int(value)

    assert_bytes('1')
    assert_bytes('1B')
    assert_bits('1b')
    assert_bits('1Mb')
    assert_bytes('1.2Mb')
    assert_bytes('1.2MB', unit='B')

    assert human_to_bytes('1', unit='M') == 1048576

# Generated at 2022-06-12 23:55:42.959401
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['', ' ', 'FAILED', ' DONE ', 'SucCeed', 'SucCeeded', 'Succeeded', 'SUCCEEDED']
    expected = ['', ' ', 'failed', 'done', 'succeed', 'succeeded', 'succeed', 'SUCCEEDED']
    result = lenient_lowercase(lst)
    for ind in range(len(expected)):
        assert result[ind] == expected[ind]


# Generated at 2022-06-12 23:55:46.317945
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['Capital', 'AllLowerCase', 'With0123', 'With-Hyphen', 'With_Underscore', 'With Space', '', None, True, False, 0, 1]
    expected_return = ['capital', 'alllowercase', 'with0123', 'with-hyphen', 'with_underscore', 'with space', '', None, True, False, 0, 1]
    assert lenient_lowercase(test_list) == expected_return


# Generated at 2022-06-12 23:55:51.167100
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    try:
        lenient_lowercase(['test', 0, 'A'])
    except AttributeError:
        raise AssertionError('Failed: did not expect AttributeError')



# Generated at 2022-06-12 23:56:00.891264
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst1 = ['a', 'B', 'c']
    lst2 = [b'a', 'B', 1]
    lst3 = []
    lst4 = ['A', 'B', 'C']

    answer1 = ['a', 'B', 'c']
    answer2 = [b'a', 'B', 1]
    answer3 = []
    answer4 = ['a', 'b', 'c']

    assert lenient_lowercase(lst1) == answer1
    assert lenient_lowercase(lst2) == answer2
    assert lenient_lowercase(lst3) == answer3
    assert lenient_lowercase(lst4) == answer4


# Generated at 2022-06-12 23:56:05.995922
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    list_input = ['text', 1, ['text_item', 1], 'Another Text']
    list_output = ['text', 1, ['text_item', 1], 'another text']

    assert lenient_lowercase(list_input) == list_output



# Generated at 2022-06-12 23:56:08.989496
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    expected = ['on', 'off', 'On', 'Off', 1, 2]
    assert lenient_lowercase(['on', 'off', 'On', 'Off', 1, 2]) == expected


# Generated at 2022-06-12 23:56:33.176541
# Unit test for function human_to_bytes
def test_human_to_bytes():
    data = [
        (u'1', 1),
        (u'2.5', 2),
        (u'2.5K', 2560),
        (u'2.5k', 2560),
        (u'2.5KB', 2560),
        (u'2.5kb', 2560),
        (u'2.5Mb', 2560 * 1024),
        (u'2.5MB', 2560 * 1024),
        (u'2.5Gb', 2560 * 1024 * 1024),
        (u'2.5GB', 2560 * 1024 * 1024),
        (u'2.5Tb', 2560 * 1024 * 1024 * 1024),
        (u'2.5TB', 2560 * 1024 * 1024 * 1024),
    ]
    for item in data:
        input, expected = item
       

# Generated at 2022-06-12 23:56:42.402638
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test with isbits=False
    assert human_to_bytes('1KB')==1024
    assert human_to_bytes('1M')==1048576
    assert human_to_bytes('2KB')==2048
    assert human_to_bytes('0.5KB')==512
    # Test with isbits=True
    assert human_to_bytes('1B', isbits=True)==1
    assert human_to_bytes('1Mb', isbits=True)==1048576
    assert human_to_bytes('2kb', isbits=True)==2048
    assert human_to_bytes('1.5Mb', isbits=True)==1572864
    # Test with default unit
    assert human_to_bytes('10', default_unit='G')==10000000000
    assert human_to_bytes

# Generated at 2022-06-12 23:56:44.871484
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['Test', 1, 'String', True]
    assert sorted(test_list) == sorted(lenient_lowercase(test_list))



# Generated at 2022-06-12 23:56:55.580405
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10.0') == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10.5k') == 10500
    assert human_to_bytes('10.5k', default_unit='b') == 10500
    assert human_to_bytes('10.5b', isbits=True) == 10.5
    assert human_to_bytes('10.5KB') == 10500
    assert human_to_bytes('10.5KB', unit='B') == 10500
    assert human_to_bytes('10.5KB', unit='b') == 10500 * 8

# Generated at 2022-06-12 23:56:58.821244
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    before = ['Blah', 1, 'blah', u'bLah', 'BREW', 2]
    after = ['blah', 1, 'blah', u'bLah', 'brew', 2]

    assert lenient_lowercase(before) == after

# Generated at 2022-06-12 23:57:06.305746
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase(["a", 2, "b"]) == ["a", 2, "b"]
    assert lenient_lowercase(["a", "b", "c"]) == ["a", "b", "c"]
    assert lenient_lowercase(["A", "B", "C"]) == ["a", "b", "c"]
    assert lenient_lowercase(["A", "B", "c"]) == ["a", "b", "c"]

# Generated at 2022-06-12 23:57:09.371472
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(('FOO', 'bAr', 1, 'Baz')) == (u'foo', u'bar', 1, u'Baz')


# Generated at 2022-06-12 23:57:15.471257
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    '''
    Unit test for lenient_lowercase()
    '''
    assert lenient_lowercase([]) == []
    assert lenient_lowercase([1]) == [1]
    assert lenient_lowercase(['a']) == ['a']
    assert lenient_lowercase([1, 'a']) == [1, 'a']
    assert lenient_lowercase([1, 'a', 'B']) == [1, 'a', 'B']



# Generated at 2022-06-12 23:57:16.936084
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a', 'b', 1, 2] == lenient_lowercase(['a', 'B', 1, '2'])

# Generated at 2022-06-12 23:57:23.926036
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:58:22.601659
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    dut = ['a', 'B', 'c', 'D', 1, 2, 3, None]

    try:
        lenient_lowercase(dut)
    except Exception as e:
        print("ERROR %s" % str(e))

    # Assertion
    assert dut == ['a', 'b', 'c', 'd', 1, 2, 3, None], 'lenient_lowercase failed'


# Generated at 2022-06-12 23:58:33.417395
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('5MB') == 5242880
    assert human_to_bytes('5 mb') == 5242880
    assert human_to_bytes('5Mb') == 5242880
    assert human_to_bytes('5mb') == 5242880
    assert human_to_bytes('5 MB', isbits=True) == 5242880
    assert human_to_bytes('5 mb', isbits=True) == 5242880
    assert human_to_bytes('5Mb', isbits=True) == 5242880
    assert human_to_bytes('5mb', isbits=True) == 5242880
    assert human_to_bytes('5B') == 5
    assert human_to_bytes('5b') == 5

# Generated at 2022-06-12 23:58:40.616513
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Create different types
    lc_none = lenient_lowercase(None)
    lc_str = lenient_lowercase("aBcDeFG")
    lc_num = lenient_lowercase(12345)
    lc_lst = lenient_lowercase(["aBcDeFG", 12345])
    lc_dict = lenient_lowercase({"Abc": "abC", "gH": 12345})
    lc_lstofdict = lenient_lowercase([{'aBc': 'aBC'}, {'gH': 12345}])

    # test for type None
    assert lc_none == None

    # test for type string
    assert lc_str == "abcdefg"

    # test for type number
    assert lc_num == 12345

    #