

# Generated at 2022-06-12 23:48:46.749977
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, 'abc', 'XYZ', ['abc']]
    assert lenient_lowercase(lst) == [1, 'abc', 'xyz', ['abc']]
    lst = 'abc'
    assert lenient_lowercase(lst) == 'abc'



# Generated at 2022-06-12 23:48:56.034831
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(0) == '0.00 Bytes'
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(1, unit='K') == '1.00 KB'
    assert bytes_to_human(1024, unit='K') == '1.00 KB'
    assert bytes_to_human(1024 ** 2, unit='K') == '1.00 MB'
    assert bytes_to_human(1024 ** 2, unit='M') == '1.00 MB'
    assert bytes_to_human(1024 ** 3, unit='K') == '1.00 GB'
    assert bytes_to_human(1024 ** 3, unit='G') == '1.00 GB'

# Generated at 2022-06-12 23:49:03.315283
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test lowercase with same type list
    assert lenient_lowercase(['1', '2', '3', '4']) == ['1', '2', '3', '4']
    # Test lowercase with mixed type list
    assert lenient_lowercase(['1', 2, '3']) == ['1', 2, '3']
    # Test lowercase with string
    assert lenient_lowercase('abc') == 'abc'
    # Test lowercase with number type
    assert lenient_lowercase(10) == 10

# Generated at 2022-06-12 23:49:11.723521
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Unit test for function human_to_bytes
    '''

    # tests with isbits = False
    result_test_1 = human_to_bytes("2")
    assert result_test_1 == 2, "Test 1 failed. Expected: 2, got %d" % result_test_1

    result_test_2 = human_to_bytes("2.15")
    assert result_test_2 == 2, "Test 2 failed. Expected: 2, got %d" % result_test_2

    result_test_3 = human_to_bytes("2M")
    assert result_test_3 == 2097152, "Test 3 failed. Expected: 2097152, got %d" % result_test_3

    result_test_4 = human_to_bytes("2Mb")
    assert result_test

# Generated at 2022-06-12 23:49:17.375467
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['Ala', 'mAkE', 'UPPER', '', 'Case', None, 'Test']
    test_list_improved = lenient_lowercase(test_list)
    expected_list = ['ala', 'make', 'upper', '', 'case', None, 'test']
    assert(test_list_improved == expected_list)


# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:49:29.832968
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('-42', 'KB') == -42 * 1024
    assert human_to_bytes('104448', unit='KB') == 104448
    assert human_to_bytes('104448') == 104448
    assert human_to_bytes('104448', unit='KB') == 104448
    assert human_to_bytes('104448', unit='b') == 104448 * 8
    assert human_to_bytes('104448', unit='Mb') == 104448 * 8 * 1024 * 1024
    assert human_to_bytes('104448', unit='Mb', isbits=True) == 104448 * 1024 * 1024
    assert human_to_bytes('MB', 'KB') == 1024 * 1024

    # Test negative values

# Generated at 2022-06-12 23:49:36.545000
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ##########
    # Bytes:
    ##########

    # single B
    assert human_to_bytes('1 B') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('0.1') == 0

    # KB
    assert human_to_bytes('1 Kb') == 1024
    assert human_to_bytes('1 KB') == 1024
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1k B') == 1024
    assert human

# Generated at 2022-06-12 23:49:40.275254
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    a = ['a', 'B', 3, 4.5, 'D', 'e', 'F']
    b = ['a', 'b', 3, 4.5, 'D', 'e', 'F']
    assert lenient_lowercase(a) == b



# Generated at 2022-06-12 23:49:50.882433
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1TB') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1PB') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976

# Generated at 2022-06-12 23:49:59.198236
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(2) == '2.00 Bytes'
    assert bytes_to_human(4) == '4.00 Bytes'
    assert bytes_to_human(8) == '8.00 Bytes'
    assert bytes_to_human(16) == '16.00 Bytes'
    assert bytes_to_human(16384) == '16.00 KBytes'
    assert bytes_to_human(16385) == '16.01 KBytes'
    assert bytes_to_human(16386) == '16.01 KBytes'
    assert bytes_to_human(16475) == '16.09 KBytes'
    assert bytes_to_human(16576) == '16.18 KBytes'
    assert bytes_

# Generated at 2022-06-12 23:50:08.360854
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1B', 'b') == 1
    assert human_to_bytes('1b', 'B') == 1
    assert human_to_bytes('1b', 'b') == 1
    assert human_to_bytes('1', 'KB') == 1000
    assert human_to_bytes('1', 'KB', True) == 1000
    assert human_to_bytes('10', 'KB') == 10000
    assert human_to_bytes('10', 'KB', True) == 10000
    assert human_to_bytes('1', 'MB') == 1000000
    assert human_to_bytes('1', 'MB', True) == 1000000
    assert human_to_bytes('1', 'GB') == 1000000000


# Generated at 2022-06-12 23:50:18.887580
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(10240) == '10.00 KB'
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(512) == '512.00 Bytes'
    assert bytes_to_human(512, unit='m') == '0.00 MB'
    assert bytes_to_human(512, unit='g') == '0.00 GB'
    assert bytes_to_human(512, unit='t') == '0.00 TB'

    # Test bits case
    assert bytes_to_human(1024, isbits=True) == '1.00 Kb'
    assert bytes_to_human(512, isbits=True) == '512.00 bits'

# Generated at 2022-06-12 23:50:28.394392
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Positive tests without default unit
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10Mb') == 13107200
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 13107200
    # Positive tests with default unit
    assert human_to_bytes('1', 'M') == 1048576
    assert human_to_bytes('0.1', 'M') == 104858
    assert human_to_bytes('1.5', 'K') == 1536
    # Negative tests
    # Suffixes are case sensitive
    try:
        human_to_bytes('1MB') == 10485760
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:50:35.507606
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # expected outcome
    expected = [
        "one",
        "two",
        3,
        "four"
    ]
    # create test list
    testlist = [
        "one",
        "TWO",
        3,
        "fOuR"
    ]
    result = lenient_lowercase(testlist)
    assert result == expected, "test failed"



# Generated at 2022-06-12 23:50:40.918571
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(10) == 10
    assert human_to_bytes(10, 'b') == 10
    assert human_to_bytes(10, 'b', True) == 10
    assert human_to_bytes(10, 'bit') == 10
    assert human_to_bytes(10, 'bit', True) == 10
    assert human_to_bytes(10, 'bits') == 10
    assert human_to_bytes(10, 'bits', True) == 10
    assert human_to_bytes(10, 'byte') == 10
    assert human_to_bytes(10, 'byte', True) == 10
    assert human_to_bytes(10, 'bytes') == 10
    assert human_to_bytes(10, 'bytes', True) == 10

    assert human_to_bytes('10') == 10
    assert human

# Generated at 2022-06-12 23:50:50.584258
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1000, unit='b') == "0.98 bits"
    assert bytes_to_human(1000, unit='B') == "0.98 Bytes"
    assert bytes_to_human(1024) == "1.02 KBytes"
    assert bytes_to_human(1024, unit='B') == "1.02 KBytes"
    assert bytes_to_human(1024, unit='b') == "8192 bits"
    assert bytes_to_human(1024 * 1024, unit='B') == "1.05 MBytes"
    assert bytes_to_human(1024 * 1024, unit='b') == "8388608 bits"
    assert bytes_to_human(1024 * 1024 * 1024, unit='b') == "8589934592 bits"

# Generated at 2022-06-12 23:51:01.322354
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:08.585508
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == "1 Bytes"
    assert bytes_to_human(10 * SIZE_RANGES['K']) == "10.00 KB"
    assert bytes_to_human(10 * SIZE_RANGES['M']) == "10.00 MB"
    assert bytes_to_human(10 * SIZE_RANGES['G']) == "10.00 GB"
    assert bytes_to_human(10 * SIZE_RANGES['T']) == "10.00 TB"
    assert bytes_to_human(10 * SIZE_RANGES['P']) == "10.00 PB"

    assert bytes_to_human(1, isbits=True) == "1 bits"

# Generated at 2022-06-12 23:51:12.739133
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['TEST']) == ['test']
    assert lenient_lowercase(['TEST', 1]) == ['test', 1]
    assert lenient_lowercase([1]) == [1]
    assert lenient_lowercase([]) == []


# Generated at 2022-06-12 23:51:22.734617
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Conversion of human-readable string to bytes
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1KB', unit='B') == 1024
    assert human_to_bytes('1M', unit='K') == 1024 * 1024
    assert human_to_bytes('1G', unit='B') == 1 * 1024 * 1024 * 1024
    assert human_to_bytes('1G', unit='KB') == 1 * 1024 * 1024 * 1024
    assert human_to_bytes('1T', unit='B') == 1 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('1T', unit='KB') == 1 * 1024 * 1024

# Generated at 2022-06-12 23:51:35.092308
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1048576) == "1.00 MB"
    assert bytes_to_human(1048576, isbits=True) == "8.00 Mb"
    assert bytes_to_human(10485760, isbits=True) == "80.00 Mb"
    assert bytes_to_human(1073741824) == "1.00 GB"
    assert bytes_to_human(1024) == "1.00 KB"
    assert bytes_to_human(1024, isbits=True) == "8.00 Kb"
    assert bytes_to_human(1024, unit='M') == "0.00 MB"
    assert bytes_to_human(1024, isbits=True, unit='M') == "0.00 Mb"

# Generated at 2022-06-12 23:51:44.642882
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # 2KB = 2048
    assert human_to_bytes('2K') == human_to_bytes(2, 'K') == 2048
    assert human_to_bytes('2K', default_unit='K') == 2048
    assert human_to_bytes('2K', default_unit='K') == human_to_bytes('2K', default_unit='K')
    assert human_to_bytes('2KB') == human_to_bytes(2, 'KB') == 2048
    assert human_to_bytes('2KB', isbits=True) == human_to_bytes(2, 'KB', isbits=True) == 256000
    assert human_to_bytes('2KB', default_unit='KB') == 2048
    assert human_to_bytes('2Kb') == human_to_bytes(2, 'Kb') == 256000


# Generated at 2022-06-12 23:51:52.820706
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert (human_to_bytes('1Kb') == 1024)
    assert (human_to_bytes('1m') == 1048576)
    assert (human_to_bytes('1kb') == 1024)
    assert (human_to_bytes('1Mb') == 1048576)
    assert (human_to_bytes('1mb') == 1048576)
    assert (human_to_bytes('1tb') == 1099511627776)
    assert (human_to_bytes('1tb', unit='Kb') == 107374182400)



# Generated at 2022-06-12 23:51:58.660868
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    one = 'One'
    two = 2
    three = ['Three', 3]

    lc_one = lenient_lowercase([one])
    lc_two = lenient_lowercase([two])
    lc_three = lenient_lowercase([three])

    assert lc_one[0] == one.lower()
    assert lc_two[0] == two
    assert lc_three[0][0] == three[0].lower()
    assert lc_three[0][1] == three[1]

# Generated at 2022-06-12 23:52:03.978791
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # test_array_empty
    assert lenient_lowercase([]) == []

    # test_array_lower
    assert lenient_lowercase(['tcp', 'udp']) == ['tcp', 'udp']

    # test_array_upper
    assert lenient_lowercase(['TCP', 'UDP']) == ['tcp', 'udp']

    # test_array_mixed
    assert lenient_lowercase(['TCP', 'UDP', 'http', 'icmp']) == ['tcp', 'udp', 'http', 'icmp']

    # test_array_lower_mixed
    assert lenient_lowercase(['tcp', 'UDP', 'http', 'icmp']) == ['tcp', 'udp', 'http', 'icmp']

    # test_array_upper

# Generated at 2022-06-12 23:52:15.152722
# Unit test for function bytes_to_human
def test_bytes_to_human():
    for unit in ['Y', 'Z', 'E', 'P', 'T', 'G', 'M', 'K']:
        assert bytes_to_human(SIZE_RANGES[unit], unit=unit) == '1.00 ' + unit + 'Bytes'
        assert bytes_to_human(SIZE_RANGES[unit]-1, unit=unit) == '0.99 ' + unit + 'Bytes'
        assert bytes_to_human(1, unit=unit) == '0.00 ' + unit + 'Bytes'
        assert bytes_to_human(SIZE_RANGES[unit] + 1, unit=unit) == '1.00 ' + unit + 'Bytes'

    assert bytes_to_human(SIZE_RANGES['G']) == '1.00 GB'

# Generated at 2022-06-12 23:52:25.035219
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    '''
    Test cases for lenient_lowercase function
    '''
    # Test case#1: Lowercase for string values
    assert lenient_lowercase(['aBcDeF', 'StUvWxYz']) == ['abcdef', 'stuvwxyz']

    # Test case#2: Lowercase for numeric values
    assert lenient_lowercase(['12345', '123456789']) == ['12345', '123456789']

    # Test case#3: Lowercase for list/sets of all types of values
    assert lenient_lowercase(['aB1', '12eF', 'StUvWxYz', [1, 2, 3, 'a']]) == ['ab1', '12ef', 'stuvwxyz', [1, 2, 3, 'a']]

# Generated at 2022-06-12 23:52:31.408520
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.5') == 1

    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1M', 'M') == 1048576
    assert human_to_bytes('1M', 'K') == 1024

    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1Mb', isbits=True, unit='Mb') == 1048576
    assert human_to_bytes('1Mb', isbits=True, unit='Kb') == 1024

    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1K', 'K') == 1024
    assert human_to_bytes('1K', 'M')

# Generated at 2022-06-12 23:52:42.561231
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1Kb') == 1 << 10
    assert human_to_bytes('1MB') == 1 << 20
    assert human_to_bytes('1GB') == 1 << 30
    assert human_to_bytes('1TB') == 1 << 40
    assert human_to_bytes('1PB') == 1 << 50
    assert human_to_bytes('1EB') == 1 << 60
    assert human_to_bytes('1ZB') == 1 << 70
    assert human_to_bytes('1YB') == 1 << 80
    assert human_to_bytes('1Mb') == 1 << 20

# Generated at 2022-06-12 23:52:52.095288
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list1 = ['abcd', 1, 'EFGH']
    test_result1 = ['abcd', 1, 'EFGH']
    test_list2 = ['ABCD', 1, 'EFGH']
    test_result2 = ['abcd', 1, 'EFGH']

    if lenient_lowercase(test_list1) != test_result1:
        raise AssertionError("Failed to run lenient_lowercase function in test1")

    if lenient_lowercase(test_list2) != test_result2:
        raise AssertionError("Failed to run lenient_lowercase function in test2")


# Generated at 2022-06-12 23:52:59.180769
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 3, 'c']) == ['A', 3, 'c']


# Generated at 2022-06-12 23:53:07.314120
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # bytes
    assert human_to_bytes(1000) == 1000
    assert human_to_bytes('1000') == 1000
    assert human_to_bytes('1000B') == 1000
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1Kb') == 1024
    # bits
    assert human_to_bytes('1Kb', True) == 1024
    assert human_to_bytes('1KB', True) != 1024
    assert human_to_bytes('1K', True) != 1024
    assert human_to_bytes('1Kb', True, 'b') == 1024
    assert human_to_bytes('1Kb', True, 'B') != 1024

# Generated at 2022-06-12 23:53:18.429710
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Testing exceptions
    try:
        human_to_bytes('1Bb')
    except ValueError:
        pass

    try:
        human_to_bytes('1BB')
    except ValueError:
        pass

    try:
        human_to_bytes('1Bb', isbits=True)
    except ValueError:
        pass

    try:
        human_to_bytes('1BB', isbits=True)
    except ValueError:
        pass

    try:
        human_to_bytes('1.0')
    except ValueError:
        pass

    # Testing bytes
    assert(human_to_bytes('1') == 1)
    assert(human_to_bytes('1B') == 1)
    assert(human_to_bytes('1B', 'B') == 1)

# Generated at 2022-06-12 23:53:26.123052
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Bytes
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1Ki') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1KiB') == 1024
    assert human_to_bytes('.25M') == 262144
    assert human_to_bytes('.25Mi') == 262144
    assert human_to_bytes('.25Mb') == 262144
    assert human_to_bytes('.25MiB') == 262144
    assert human_to_bytes('1m') == 1048576
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1Mi')

# Generated at 2022-06-12 23:53:34.430664
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 1, 'C']) == ['a', 1, 'c']
    assert lenient_lowercase(['A', (1, 2, 3), 'C']) == ['a', (1, 2, 3), 'c']
    assert lenient_lowercase(['A', {'a': 'b'}, 'C']) == ['a', {'a': 'b'}, 'c']

# Generated at 2022-06-12 23:53:44.278597
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1G', isbits=True) == 10737418240
    assert human_to_bytes('1G', default_unit='KB') == 1048576000
    assert human_to_bytes('1G', default_unit='KB', isbits=True) == 1048576000
    assert human_to_bytes('1.5G') == 1610612736
    assert human_to_bytes('1.5G', isbits=True) == 16106127360
    assert human_to_bytes('1.5G', default_unit='KB') == 1572864000

# Generated at 2022-06-12 23:53:45.767290
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['fOo', 'BaR', [1, 2, 3]]) == ['foo', 'bar', [1, 2, 3]]

# Generated at 2022-06-12 23:53:50.697675
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    strings = []
    strings.append('Test')
    strings.append(0)

    result = lenient_lowercase(strings)
    assert result == ['test', 0], "lowercase function failed to run"

    strings = 'test'
    result = lenient_lowercase(strings)

    assert result == 'test', "lowercase function failed to run"


# Generated at 2022-06-12 23:54:01.806857
# Unit test for function human_to_bytes
def test_human_to_bytes():
    def verify(result, expected):
        if result != expected:
            raise ValueError("Expected %s, got %s" % (expected, result))

    values = {
        'Mb': humans_to_bits,
        'MB': humans_to_bytes,
        'Kb': humans_to_bits,
        'KB': humans_to_bytes,
        'Gb': humans_to_bits,
        'GB': humans_to_bytes,
        'Tb': humans_to_bits,
        'TB': humans_to_bytes
    }

    for name, l in iteritems(values):
        verify(human_to_bytes("1.5%s" % name), l['1.5%s' % name])

# Generated at 2022-06-12 23:54:05.507563
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'a', [1, 2]]) == [1, 'a', [1, 2]]
    assert lenient_lowercase(['A', 'B', [1, 2]]) == ['a', 'b', [1, 2]]

# Generated at 2022-06-12 23:54:19.019870
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['A', 'b', 1, 'c', 2, [3, '4'], (5, '6', 7)]
    assert lenient_lowercase(test_list) == ['a', 'b', 1, 'c', 2, [3, '4'], (5, '6', 7)]


# Generated at 2022-06-12 23:54:23.641582
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['A', 'B', 'C', 'D', 10, 20, 30, 'E', 'F', 'G', 'H', 100]
    lower_lst = lenient_lowercase(lst)
    for l1, l2 in zip(lst, lower_lst):
        if isinstance(l1, str):
            assert l1.lower() == l2
        else:
            assert l1 == l2


# Generated at 2022-06-12 23:54:34.727874
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1K', 'b') == 1000
    assert human_to_bytes('1K', 'b', True) == 1000
    assert human_to_bytes('1Mb', 'b', True) == 1000000
    assert human_to_bytes('1Gb', 'b', True) == 1000000000
    assert human_to_bytes('1Tb', 'b', True) == 1000000000000
    assert human_to_bytes('1Pb', 'b', True) == 1000000000000000
    assert human_to_bytes('1Eb', 'b', True) == 1000000000000000000
    assert human_to_bytes('1Zb', 'b', True) == 1000000000000000000000
    assert human_to_bytes('1Yb', 'b', True) == 1000000000000000000000000
    # test 'B' suffix cases
    assert human_

# Generated at 2022-06-12 23:54:45.797369
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print('------------------------------------------------')
    print('Unit test for function human_to_bytes() started')
    print('------------------------------------------------')

# Generated at 2022-06-12 23:54:58.735590
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1.2') == 1
    assert human_to_bytes('1.2K') == 1228
    assert human_to_bytes('1.2M') == 1258291
    assert human_to_bytes('1.2G') == 1288490189
    assert human_to_bytes('2T', isbits=True) == 2199023255552
    assert human_to_bytes('1.2b', isbits=True) == 1
    assert human_to_bytes('1.2Kb', isbits=True) == 1228
    assert human_to_bytes('1.2Mb', isbits=True) == 1258291
    assert human_to_bytes('1.2Gb', isbits=True) == 1288490189

# Generated at 2022-06-12 23:55:00.917344
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 1, 'C', 'D']) == ['a', 'b', 1, 'c', 'd']

# Generated at 2022-06-12 23:55:05.927339
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a', 'B', 'C', 'c'] == lenient_lowercase(['a', 'B', '0.1', 'C', 'c'])


if __name__ == '__main__':
    import pytest
    pytest.main(['-vvs', './test_fileutils.py'])

# Generated at 2022-06-12 23:55:09.969803
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'FOO', 'Bar']) == [1, 'foo', 'Bar']


# Generated at 2022-06-12 23:55:20.749815
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    str_list = ['sonicOS version', 'SonicOS version', 'version', 'firewall model', 'firmware version', 'internal version', 'version', 'internal model']
    str_lower_list = ['sonicos version', 'sonicos version', 'version', 'firewall model', 'firmware version', 'internal version', 'version', 'internal model']
    tuple_list = [('SonicOS version', 'SonicOS version'), ('firewall model', 'SonicWall NSA'), ('firmware version', '6.5.2.0-1s'), ('internal version', '6.5.2.0'), ('version', ''), ('internal model', 'NSA240')]

# Generated at 2022-06-12 23:55:28.139763
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    import sys
    import pytest

    if sys.version_info.major == 2:
        assert lenient_lowercase([u'LowerCase']) == [u'lowercase']
        assert lenient_lowercase(['LowerCase']) == ['lowercase']
        assert lenient_lowercase(['LowerCase', 1]) == ['lowercase', 1]
    else:
        assert lenient_lowercase([u'LowerCase']) == ['lowercase']
        assert lenient_lowercase(['LowerCase']) == ['lowercase']
        assert lenient_lowercase(['LowerCase', 1]) == ['lowercase', 1]



# Generated at 2022-06-12 23:55:53.500793
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10b') == 1
    assert human_to_bytes('10mb') == 1048576



# Generated at 2022-06-12 23:56:05.551729
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2 * 1024
    assert human_to_bytes('2M') == 2 * 1024 * 1024
    assert human_to_bytes(2, 'M') == 2 * 1024 * 1024
    assert human_to_bytes('2M', 'M') == 2 * 1024 * 1024
    assert human_to_bytes('2Kb') == 2 * 1024

    assert human_to_bytes('10000B') == 10000
    assert human_to_bytes(10000, 'B') == 10000
    assert human_to_bytes('10000b') == 10000 / 8
    assert human_to_bytes('10K') == 10 * 1024
    assert human_to_bytes('10Kb') == 10 * 1024 / 8

    assert human_to_bytes('5Mb') == 5 * 1024 * 1024 / 8
    assert human_to

# Generated at 2022-06-12 23:56:08.125897
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['foo', 'bar']) == ['foo', 'bar']
    assert lenient_lowercase(['foo', 3]) == ['foo', 3]
    assert lenient_lowercase(['FOO', 'BAR']) == ['foo', 'bar']


# Generated at 2022-06-12 23:56:19.982114
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test for digital in string
    assert human_to_bytes(12) == 12
    assert human_to_bytes(12.0) == 12
    assert human_to_bytes(12.1) == 12
    assert human_to_bytes('12') == 12
    # test for digital in string with unit
    assert human_to_bytes('12.1B') == 12
    assert human_to_bytes('12B') == 12
    assert human_to_bytes('12b') == 12
    assert human_to_bytes('12B', 'kB') == 12000
    assert human_to_bytes('12b', 'kB') == 12000
    assert human_to_bytes('12.1B', 'kB') == 12
    assert human_to_bytes('12.1b', 'kB') == 12
    # convert string to bytes


# Generated at 2022-06-12 23:56:23.889864
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    original = ["a", "B", 1, 2]
    lowercased = ["a", "b", 1, 2]
    assert lenient_lowercase(original) == lowercased


# Generated at 2022-06-12 23:56:31.012561
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['FOO']) == ['foo']
    assert lenient_lowercase(['FOO', 123]) == ['foo', 123]
    assert lenient_lowercase(['FOO', 'BAR']) == ['foo', 'bar']
    assert lenient_lowercase(['FOO', 'BAR', 123, 456]) == ['foo', 'bar', 123, 456]
    assert lenient_lowercase([123]) == [123]
    assert lenient_lowercase([]) == []

# Generated at 2022-06-12 23:56:35.348467
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ABC', 'Def']) == ['abc', 'def']
    assert lenient_lowercase(['ABC', 123]) == ['abc', 123]
    assert lenient_lowercase(['ABC', None]) == ['abc', None]
    assert lenient_lowercase([dict(a=1), None]) == [dict(a=1), None]

# Generated at 2022-06-12 23:56:37.639971
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    result = lenient_lowercase(['foo', 'bAR', 1])
    assert result == ['foo', 'bar', 1]


# Generated at 2022-06-12 23:56:45.020497
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Case when only raw number passed
    assert human_to_bytes('1024') == 1024
    # Case when no unit passed and raw number is float
    assert human_to_bytes('1024.5') == 1024
    assert human_to_bytes('1024.567') == 1025

    # Case when no unit passed in a raw number and it's not a number for sure
    try:
        human_to_bytes('aaa')
        assert False
    except ValueError as ex:
        assert str(ex) == "human_to_bytes() can't interpret following string: aaa"

    # Case when no unit passed in a raw number and it's not a number

# Generated at 2022-06-12 23:56:55.811592
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('15') == 15
    assert human_to_bytes(15) == 15
    assert human_to_bytes(15, 'G') == 15000000000
    assert human_to_bytes(15, 'G', True) == 15000000000
    assert human_to_bytes('15G') == 15000000000
    assert human_to_bytes('15G', True) == 15000000000
    assert human_to_bytes('15Kb') == 15360
    assert human_to_bytes('15kb') == 15360
    assert human_to_bytes('15KB') == 15000
    assert human_to_bytes('15Kb', True) == 15360
    assert human_to_bytes('15kb', True) == 15360
    assert human_to_bytes('15KB', True) == 15000
    assert human

# Generated at 2022-06-12 23:57:39.592670
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Function test_human_to_bytes() is for unit test for function human_to_bytes()
    '''
    print("Starting unit test for function human_to_bytes():")
    # test 1
    if human_to_bytes(2, default_unit='K') != 2048:
        raise AssertionError("human_to_bytes(2, default_unit='K') != 2048")
    print("test 1 - passed")
    # test 2
    if human_to_bytes('2', 'K') != 2048:
        raise AssertionError("human_to_bytes('2', 'K') != 2048")
    print("test 2 - passed")
    # test 3 - incorrect default_unit check

# Generated at 2022-06-12 23:57:42.753278
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1,2,3,4,5]) == [1,2,3,4,5]
    assert lenient_lowercase(['test', 'TEST']) == ['test', 'test']

# Generated at 2022-06-12 23:57:46.543712
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['A', 'b', 1, [1], {1: 1}]
    expected_list = ['a', 'b', 1, [1], {1: 1}]
    assert lenient_lowercase(test_list) == expected_list

# Generated at 2022-06-12 23:57:54.710642
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1T') == 1099511627776

    assert human_to_bytes('2K', isbits=True) == 2048 * 8
    assert human_to_bytes('10M', isbits=True) == 10485760 * 8
    assert human_to_bytes('1Gb', isbits=True) == 1073741824
    assert human_to_bytes('1Tb', isbits=True) == 1099511627776

    # error
    try:
        human_to_bytes('2Mb')
        assert False
    except ValueError:
        pass


# Generated at 2022-06-12 23:58:07.498118
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:58:11.824364
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, "three", "FOUR"]) == [1, 2, "three", "FOUR"]
    assert lenient_lowercase([1, 2, "THREE", "FOUR"]) == [1, 2, "three", "FOUR"]


# Generated at 2022-06-12 23:58:16.368576
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'AbC', 'dEf']) == [1, 'abc', 'def']
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase('abc') == ['a', 'b', 'c']

# Generated at 2022-06-12 23:58:25.438968
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """ Unit test for function human_to_bytes. """
    assert human_to_bytes(' 8b') == 1
    assert human_to_bytes(' 1B') == 1
    assert human_to_bytes(' 1B ') == 1
    assert human_to_bytes(' 2b ') == 1
    assert human_to_bytes('1 B') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1, 'b') == 1
    assert human_to_bytes(0) == 0
    assert human_to_bytes('1') == 1
    assert human_to_bytes('2B') == 2
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1Kb') == 1024
   

# Generated at 2022-06-12 23:58:31.842016
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # The result should be equivalent to
    # [x.lower() for x in ['1', '2', '3']]
    assert lenient_lowercase(['1', '2', '3']) == ['1', '2', '3']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-12 23:58:39.539386
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 2]) == ['a', 'b', 2]
    assert lenient_lowercase([1, 'b', '2']) == [1, 'b', '2']
    assert lenient_lowercase(['A', 'b', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['Mb', 'Kb', 'B']) == ['mb', 'kb', 'b']
    assert lenient_lowercase(['Mb', 'Kb', 'b']) == ['mb', 'kb', 'b']
    assert lenient_lowercase(['MB', 'KB', 'b']) == ['mb', 'kb', 'b']