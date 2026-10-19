

# Generated at 2022-06-12 23:48:56.899855
# Unit test for function bytes_to_human

# Generated at 2022-06-12 23:49:07.483462
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from nose.tools import assert_equal

    assert_equal(human_to_bytes('10M'), 10485760)
    assert_equal(human_to_bytes('10.2M'), 10747904)
    assert_equal(human_to_bytes('10.7M'), 11216896)
    assert_equal(human_to_bytes('10.8M'), 11240448)

    assert_equal(human_to_bytes('15K'), 15360)
    assert_equal(human_to_bytes('15.2K'), 15559)
    assert_equal(human_to_bytes('15.7K'), 15948)
    assert_equal(human_to_bytes('15.8K'), 16128)

    assert_equal(human_to_bytes('15.8Kb', isbits=True), 15948)

# Generated at 2022-06-12 23:49:14.091531
# Unit test for function human_to_bytes
def test_human_to_bytes():
    if human_to_bytes('10M') == 10485760:
        print("test_human_to_bytes(): test '10M' - pass")
    else:
        print("test_human_to_bytes(): test '10M' - fail")
        return

    try:
        human_to_bytes('10MB')
        print("test_human_to_bytes(): test '10MB' - fail (ValueError must be raised)")
    except ValueError:
        print("test_human_to_bytes(): test '10MB' - pass")
        pass

    if human_to_bytes('1MB') == 1048576:
        print("test_human_to_bytes(): test '1MB' - pass")
    else:
        print("test_human_to_bytes(): test '1MB' - fail")
        return

# Generated at 2022-06-12 23:49:19.276631
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 1, 'C']) == ['a', 'b', 1, 'c']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase(['Å', 'Ä', 'Ö']) == ['å', 'ä', 'ö']



# Generated at 2022-06-12 23:49:30.273918
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Testing function human_to_bytes()."""
    print("unit testing function: human_to_bytes()")

    # Definition of test forward cases

# Generated at 2022-06-12 23:49:36.932506
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test lower and upper case
    assert(human_to_bytes("1M") == human_to_bytes("1m"))
    assert(human_to_bytes("1m") == 1048576)
    assert(human_to_bytes("1m", isbits=True) == 8388608)

    # Test UPPER case
    assert(human_to_bytes("1MB") == 1048576)
    assert(human_to_bytes("1MB", isbits=True) == 8388608)

    # Test multiple spaces
    assert(human_to_bytes("1  Mb") == 1048576)
    assert(human_to_bytes("1 Mb") == 1048576)
    assert(human_to_bytes("1Mb") == 1048576)

# Generated at 2022-06-12 23:49:45.021543
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1048576) == '1.00 MB'
    assert bytes_to_human(1073741824) == '1.00 GB'
    assert bytes_to_human(1099511627776) == '1.00 TB'
    assert bytes_to_human(1125899906842624) == '1.00 PB'
    assert bytes_to_human(1152921504606846976) == '1.00 EB'
    assert bytes_to_human(1180591620717411303424) == '1.00 ZB'

# Generated at 2022-06-12 23:49:51.581687
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [True, False, 'A', 'a', u'B', u'b', 1, 2.5, '1', '1.5', [1], {'a':'b'}]
    expect_list = [True, False, 'a', 'a', 'b', 'b', 1, 2.5, '1', '1.5', [1], {'a':'b'}]
    assert(lenient_lowercase(test_list) == expect_list)


# Generated at 2022-06-12 23:49:59.659614
# Unit test for function human_to_bytes
def test_human_to_bytes():

    assert human_to_bytes("10M") == human_to_bytes(10, 'M')
    assert human_to_bytes("15.3G") == human_to_bytes(15.3, 'G')
    assert human_to_bytes("15.3GB") == human_to_bytes(15.3, 'GB')
    assert human_to_bytes("15.3Tb") == human_to_bytes(15.3, 'Tb', isbits=True)

    assert human_to_bytes("10", 'M') == 10485760
    assert human_to_bytes("10", 'Mb', isbits=True) == 10485760

    assert human_to_bytes("10", default_unit='M') == 10485760

# Generated at 2022-06-12 23:50:04.114209
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test for bytes
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10M', default_unit='B') == 10485760
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2K', default_unit='B') == 2048
    assert human_to_bytes('2K') == human_to_bytes('2K', default_unit='B')
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10', default_unit='B') == 10
    assert human_to_bytes('2048', unit='KB') == 2048
    assert human_to_bytes('2KB') == 2048
    assert human_to_bytes('2KB', default_unit='B') == 2048
    assert human_to_bytes

# Generated at 2022-06-12 23:50:18.146747
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('10') == 10
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1.5k') == 1536
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1mb', isbits=True) == 1048576
    assert human_to_bytes('1.5mb', isbits=True) == 1572864
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1G') == 1073741824
    assert human_to

# Generated at 2022-06-12 23:50:24.279069
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1G', isbits=True) == 1073741824
    assert human_to_bytes('1Gb') == 1073741824
    assert human_to_bytes('1Gb', isbits=True) == 1073741824
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1GB', isbits=True) == 1073741824
    assert human_to_bytes('1Gb', 'Mb') == 1048576
    assert human_to_bytes('1MB', 'Gb') == 1048576
    assert human_to_bytes('1Gb', 'MB') == 1048576

# Generated at 2022-06-12 23:50:35.263126
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('2.5K') == 2560
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1Kb') == 1260
    assert human_to_bytes('1.7mb') == 1760768
    assert human_to_bytes('1.7mB') == 1760768
    assert human_to_bytes('1.7Mb') == 1760768
    assert human_to_bytes('1.7MB') == 1760768
    assert human_to_bytes('1Mb', isbits=True) == 1258291
    assert human_to_bytes('1MB', isbits=True) == 1258291
    assert human_to_bytes('1mB', isbits=True) == 1258

# Generated at 2022-06-12 23:50:40.153797
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 'A', 'B', 'C']) == [1, 2, 'A', 'B', 'C']
    assert lenient_lowercase(['a', 'b', 3, 4]) == ['a', 'b', 3, 4]
    assert lenient_lowercase(['A', 'b', 'C', 'D']) == ['a', 'b', 'c', 'd']

# Generated at 2022-06-12 23:50:50.555468
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:50:54.423815
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst1 = ['a', 'B', 12, 'CdEfG']
    assert lenient_lowercase(lst1) == ['a', 'b', 12, 'CdEfG']


# Generated at 2022-06-12 23:50:58.072496
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'A', 'B', 'C']) == [1, 'A', 'B', 'C']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2022-06-12 23:51:09.308870
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2') == 2
    assert human_to_bytes('2M') == 2 * 1024 * 1024
    assert human_to_bytes('2.5M') == int(2.5 * 1024 * 1024)
    assert human_to_bytes('2.5MB') == int(2.5 * 1024 * 1024)
    assert human_to_bytes('2.5mB') == int(2.5 * 1024 * 1024)
    assert human_to_bytes('2.5Mb') == int(2.5 * 1024 * 1024)
    assert human_to_bytes('2.5b') == 2.5
    assert human_to_bytes('2.5MB', isbits=True) == int(2.5 * 1024 * 1024)
    assert human_to_bytes('2', default_unit='M') == 2

# Generated at 2022-06-12 23:51:15.517709
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:24.027188
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = (
        ('1', 1),
        ('1B', 1),
        ('1b', 1),
        ('1M', 1048576),
        ('1Mb', 1048576),
        ('1MB', 1048576),
        ('1Mb', 1048576),
        ('1K', 1024),
        ('1KB', 1024),
        ('1Kb', 1024),
        ('-1K', -1024),
        ('1.5K', 1536),
        ('1.5M', 1572864),
    )
    for val, expected in tests:
        assert human_to_bytes(val) == expected, "%s != %s" % (human_to_bytes(val), expected)



# Generated at 2022-06-12 23:51:41.671286
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('10K') == 10240
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes(10, default_unit='b') == 10
    assert human_to_bytes(10, default_unit='Mb') == 10485760

# Generated at 2022-06-12 23:51:47.316164
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['tiny', 'Giant']) == ['tiny', 'giant']
    assert lenient_lowercase(['Giant', 1]) == ['giant', 1]
    assert lenient_lowercase([1, 'Giant']) == [1, 'giant']



# Generated at 2022-06-12 23:51:52.959711
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'C']) == ['a', 'b', 'c']
    lst = lenient_lowercase([None, 'a', 1])
    assert None in lst and 'a' in lst and 1 in lst
    assert lenient_lowercase(['True']) == ['true']



# Generated at 2022-06-12 23:52:00.798713
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(10, isbits=True) == '10 bits'
    assert bytes_to_human(10, unit='b') == '10 bits'
    assert bytes_to_human(10, unit='B') == '10 Bytes'
    assert bytes_to_human(10, unit='K') == '10.00 KB'
    assert bytes_to_human(10, unit='Kb') == '10.00 Kbits'
    assert bytes_to_human(10, unit='KB') == '10.00 KB'
    assert bytes_to_human(10, unit='KBits') == '10.00 KBits'
    assert bytes_to_human(10, unit='Kb') == '10.00 Kbits'

# Generated at 2022-06-12 23:52:12.001383
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M')
    assert human_to_bytes('1.1M') == human_to_bytes(1.1, 'M')
    assert human_to_bytes('10Mb', isbits=True) == human_to_bytes(10, 'M', True)
    assert human_to_bytes('1.1Mb', isbits=True) == human_to_bytes(1.1, 'M', True)
    assert human_to_bytes('10', unit='M') == human_to_bytes(10, 'M')
    assert human_to_bytes('10M', unit='B') == human_to_bytes(10, 'M')

# Generated at 2022-06-12 23:52:21.541027
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['a', 'B', 3, 'C']) == ['a', 'B', 3, 'C']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', '123abc', '-C']) == ['a', '123abc', '-C']
    assert lenient_lowercase(['-A', '123abc', '-C']) == ['-A', '123abc', '-C']
    assert lenient_lowercase(['A', None, 'C']) == ['a', None, 'c']
    assert lenient_lowercase([None, 'A', None]) == [None, 'a', None]
    assert lenient_

# Generated at 2022-06-12 23:52:30.092446
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(1048576) == '1.00 MB'
    assert bytes_to_human(1048576, isbits=True) == '1.00 Mb'
    assert bytes_to_human(1048576, isbits=True, unit='Mb') == '1.00 Mb'
    assert bytes_to_human(1048576, isbits=True, unit='M') == '1.00 Mb'
    assert bytes_to_human(1048576, isbits=True, unit='b') == '1.00 Mb'
    assert bytes_to_human(1048576, isbits=True, unit='B') == '8.00 Mb'
    assert bytes_to_human(1048576, unit='m') == '1.05 MB'

# Generated at 2022-06-12 23:52:34.743978
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['aBc', '123', 0, 1, 2]
    ans_list = ['abc', '123', 0, 1, 2]
    assert lenient_lowercase(test_list) == ans_list



# Generated at 2022-06-12 23:52:44.887629
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(0) == '0 Bytes'
    assert bytes_to_human(1023) == '1023 Bytes'
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(9223372036854775810) == '8192.00 YB'
    assert bytes_to_human(9223372036854775808) == '8191.99 YB'
    assert bytes_to_human(9223372036854775807) == '8191.99 YB'
    assert bytes_to_human(9223372036854775806) == '8191.98 YB'
    assert bytes_to_human(9223372036854775805) == '8191.98 YB'
    assert bytes_to

# Generated at 2022-06-12 23:52:56.082224
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("200") == 200
    assert human_to_bytes("200K") == (200 * (1 << 10))
    assert human_to_bytes("200KB") == (200 * (1 << 10))
    assert human_to_bytes("200Kb") == (200 * (1 << 10))
    assert human_to_bytes("200MB") == (200 * (1 << 20))
    assert human_to_bytes("200Mb") == (200 * (1 << 20))
    assert human_to_bytes("200Gb") == (200 * (1 << 30))
    assert human_to_bytes("1M") == (1 * (1 << 20))
    assert human_to_bytes(200) == 200
    assert human_to_bytes(200, 'K') == (200 * (1 << 10))
   

# Generated at 2022-06-12 23:53:05.389100
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([10, 'foo', 20, 'bar']) == [10, u'foo', 20, u'bar']
    assert lenient_lowercase([10, 20, 'foo', 'bar']) == [10, 20, u'foo', u'bar']
    assert lenient_lowercase([10, 'foo', '20', 'bar']) == [10, u'foo', u'20', u'bar']


# Unit test human_to_bytes function

# Generated at 2022-06-12 23:53:09.378582
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst_mixed = ['aBc', 'dfg', 123]
    lst_lower = ['abc', 'dfg', 123]
    assert lenient_lowercase(lst_mixed) == lst_lower

# Generated at 2022-06-12 23:53:19.771414
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Success cases
    assert human_to_bytes('5.5TB') == 607160412160
    assert human_to_bytes('1.5T') == 161061273600
    assert human_to_bytes('1500G') == 161061273600
    assert human_to_bytes('15000M') == 157286400000
    assert human_to_bytes('15000000K') == 154968192000
    assert human_to_bytes('15000000000B') == 150000000000
    assert human_to_bytes('5.5KB') == 5632
    assert human_to_bytes('1.5kB') == 1536
    assert human_to_bytes('1500Kb') == 1536000
    assert human_to_bytes('15000kb') == 153600000

# Generated at 2022-06-12 23:53:21.673697
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['test', 1, 'anothertest', None] == lenient_lowercase(['test', 1, 'anothertest', None])



# Generated at 2022-06-12 23:53:26.208778
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([1, 'B', 'c']) == [1, 'b', 'c']


# Generated at 2022-06-12 23:53:37.958449
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('0') == 0
    assert human_to_bytes('0.1') == 0
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1.1B') == 1
    assert human_to_bytes('.1B') == 0
    assert human_to_bytes('1.1K') == 1100
    assert human_to_bytes('1.1K') == 1100
    assert human_to_bytes('12K') == 12 * 1024
    assert human_to_bytes('12.34M') == 12 * 1024 * 1024 + 34 * 1024
    assert human_to_bytes('12.34M')

# Generated at 2022-06-12 23:53:47.001781
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10K') == 10 * 1024
    assert human_to_bytes('10M') == 10 * 1024 * 1024
    assert human_to_bytes('10G') == 10 * 1024 * 1024 * 1024
    assert human_to_bytes('10T') == 10 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('10P') == 10 * 1024 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('10Z') == 10 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('10E') == 10 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('10Y') == 10 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('10') == 10

# Generated at 2022-06-12 23:53:58.189727
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1bytes') == 1
    assert human_to_bytes('1Bytes') == 1
    assert human_to_bytes('1 bits') == 1
    assert human_to_bytes('1 bits', isbits=True) == 1
    assert human_to_bytes('1 MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1 MB', unit='Mb') == 8388608
    assert human_to_bytes('1 MB', unit='Mb', isbits=True) == 1048576
    assert human_to_bytes('1 MB', unit='MB') == 1048576
    assert human_to

# Generated at 2022-06-12 23:54:08.138510
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1 << 10
    assert human_to_bytes('1Kb') == 1 << 10
    assert human_to_bytes('1KB') == 1 << 10
    assert human_to_bytes('1Kib') == 1 << 10
    assert human_to_bytes('1KiB') == 1 << 10
    assert human_to_bytes('1m') == 1 << 20
    assert human_to_bytes('1M') == 1 << 20
    assert human_to_bytes('1mb') == 1 << 20

# Generated at 2022-06-12 23:54:14.533406
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:35.476981
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:42.126220
# Unit test for function lenient_lowercase

# Generated at 2022-06-12 23:54:49.760200
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('0') == 0
    assert human_to_bytes(0) == 0
    assert human_to_bytes(0.0) == 0
    assert human_to_bytes('0.0') == 0
    assert human_to_bytes('0.0b') == 0
    assert human_to_bytes('   0.0b  ') == 0
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1.0) == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.0b') == 1
    assert human_to_bytes('   1.0b  ') == 1
    assert human_to_bytes('100.0') == 100

# Generated at 2022-06-12 23:54:57.254035
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 42, 'C']) == ['a', 42, 'c']


# Unit tests for function human_to_bytes and bytes_to_human
#
# All tests were copied from tests for 'ansible/lib/ansible/module_utils/network/common/utils.py'

# Generated at 2022-06-12 23:55:07.979021
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # testing for default case
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('1B') == 1

    # testing for case with unit
    assert human_to_bytes('10', 'b') == 10
    assert human_to_bytes('1', 'B') == 1

    # testing that the valueError is rased if the 'b' is not lowercase
    try:
        human_to_bytes('1', 'B', isbits=True)
    except Exception as e:
        if isinstance(e, ValueError):
            assert True
        else:
            assert False

    # testing that the valueError is rased if the 'B' is not uppercase

# Generated at 2022-06-12 23:55:12.284854
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test for lowercase function
    test_list = ["AAA", "BBB", "CCC", "DDD"]
    expected_result = ["aaa", "bbb", "ccc", "ddd"]
    result = lenient_lowercase(test_list)

    assert result == expected_result


# Generated at 2022-06-12 23:55:17.404875
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lc = lenient_lowercase(['A', 'B', 'c', 3])
    assert(lc[0] == 'a')
    assert(lc[1] == 'b')
    assert(lc[2] == 'c')
    assert(lc[3] == 3)



# Generated at 2022-06-12 23:55:28.251326
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:38.192279
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest

    class TestData:
        def __init__(self, input_string, expected_output, expected_output_bits):
            self.input_string = input_string
            self.expected_output = expected_output
            self.expected_output_bits = expected_output_bits


# Generated at 2022-06-12 23:55:44.265893
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    '''
    Test the lenient_lowercase function.
    '''
    def is_equal(list1, list2):
        '''
        Compare two lists, suppressing errors if a non-string value is encountered
        '''
        for i in range(max(len(list1), len(list2))):
            if i >= len(list1) and i < len(list2):
                return False
            if i < len(list1) and i >= len(list2):
                return False
            if i < len(list1) and i < len(list2) and list1[i].lower() == list2[i].lower():
                pass
            else:
                return False
        return True

# Generated at 2022-06-12 23:55:56.200986
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert(lenient_lowercase(['a', 'b', 'C', 3]) == ['a', 'b', 'c', 3])

# Generated at 2022-06-12 23:56:08.283760
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, 'a', 'b', 'c', 2, 3]
    expected = [1, 'a', 'b', 'c', 2, 3]
    assert lenient_lowercase(lst) == expected
    lst = ['a', 1, 2, 3, 4, 'b', 'c']
    expected = ['a', 1, 2, 3, 4, 'b', 'c']
    assert lenient_lowercase(lst) == expected
    lst = [1, 'a', 'b', 'c', 2, 3]
    expected = [1, 'a', 'b', 'c', 2, 3]
    assert lenient_lowercase(lst) == expected
    lst = ['a', 1, 2, 3, 4, 'b', 'c']

# Generated at 2022-06-12 23:56:12.679992
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    from ansible.utils import lenient_lowercase

    lst = ['This', 'is', 'a', 'test.', 'A', 'Test', 1, 2, 3]
    res = lenient_lowercase(lst)
    assert(res == ['this', 'is', 'a', 'test.', 'A', 'Test', 1, 2, 3])



# Generated at 2022-06-12 23:56:15.270886
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['STRING', 1, None]) == ['string', 1, None]


# Generated at 2022-06-12 23:56:20.525162
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
        # type: () -> None
        """Test the lenient_lowercase function."""
        ret = lenient_lowercase([1, 'STRing', 'MiXeD', u'UniCODE'])
        assert ret == [1, 'string', 'mixed', u'UniCODE']

# Generated at 2022-06-12 23:56:31.637647
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    import sys

    if sys.version_info[0] == 2:
        test_str = 'A'
        assert test_str.lower() == 'a'
        assert test_str.lower() != 'A'
        assert lenient_lowercase([test_str]) == ['a']
        assert lenient_lowercase([test_str]) != ['A']
        assert lenient_lowercase([test_str]) != ['a', 'A']

        test_int = 1
        assert test_int.lower == AttributeError
        assert lenient_lowercase([test_int]) == [1]
        assert lenient_lowercase([test_int]) != [test_int]

        test_list_str = ['a', 'B', 'C']

# Generated at 2022-06-12 23:56:35.977316
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['abcd']) == ['abcd']
    assert lenient_lowercase([1,2,3,4]) == [1,2,3,4]
    assert lenient_lowercase(['AbCdEfG']) == ['abcdefg']
    assert lenient_lowercase([1,2,'aBc',4]) == [1,2,'abc',4]

# Generated at 2022-06-12 23:56:42.262613
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(('a', 'b', 'c', 1, 2, 3)) == ['a', 'b', 'c', 1, 2, 3]
    assert lenient_lowercase('abc') == 'abc'

# Generated at 2022-06-12 23:56:53.049142
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes('10M', default_unit='B') == 10485760
    assert human_to_bytes('10', default_unit='M') == 10485760
    assert human_to_bytes('10', default_unit='mb') == 10
    assert human_to_bytes('10Mb') == 10 * 1000 * 1000
    assert human_to_bytes('10Mb', isbits=True) == 10 * 1000 * 1000
    assert human_to_bytes('10.0Mb') == 10 * 1000 * 1000
    assert human_to_bytes('8') == 8

    # unit is always caps, regardless of original case
    assert human_to_bytes('2K') == 2048
    assert human

# Generated at 2022-06-12 23:57:01.750783
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:27.160395
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:38.187179
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # bits
    assert human_to_bytes('1', isbits=True) == 1
    assert human_to_bytes('7', isbits=True) == 7
    assert human_to_bytes('7b', isbits=True) == 7
    assert human_to_bytes('1B', isbits=True) == 8
    assert human_to_bytes('7B', isbits=True) == 56
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1.2Mb', isbits=True) == 1258291
    assert human_to_bytes('1.5Mb', isbits=True) == 1572864
    assert human_to_bytes('1.5Mb', default_unit='b', isbits=True) == 1572864

# Generated at 2022-06-12 23:57:47.976692
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2KB') == 2048
    assert human_to_bytes('2Kb') == 2048
    assert human_to_bytes('2kB') == 2048
    assert human_to_bytes('2Kb', isbits=True) == 2048
    assert human_to_bytes('2KB', isbits=True) == 2048
    assert human_to_bytes('2kB', isbits=True) == 2048
    assert human_to_bytes('2k', isbits=True) == 2048
    assert human_to_bytes('2', isbits=True) == 2
    assert human_to_bytes('2Mb', isbits=True) == 2097152
    assert human_to_bytes('2') == 2

# Generated at 2022-06-12 23:57:52.201098
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    """Test lenient_lowercase function."""
    test_list = ['UPPER', 'lower', 'MiXeD', '123', 'MiXeD123', '', 123]
    expected = ['upper', 'lower', 'mixed', '123', 'mixed123', '', 123]
    assert lenient_lowercase(test_list) == expected


# Generated at 2022-06-12 23:57:55.420110
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'c', 1]) == ['a', 'b', 'c', 1]


# Generated at 2022-06-12 23:58:00.011490
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Abc', 'dEf', 123, u'A', u'B', u'C']) == ['abc', 'def', 123, 'a', 'b', 'c']


# Generated at 2022-06-12 23:58:10.603591
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1.1B') == 1
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('4K') == 4096
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('4M') == 4194304
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('4G') == 4294967296
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1.5T') == 1649267441664
    assert human_to_bytes('1.5Tb') == 18014398509481984

# Generated at 2022-06-12 23:58:20.869005
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2MB') == 2 * 1024 * 1024
    assert human_to_bytes('2Mb') == 2 * 1024 * 1024
    assert human_to_bytes('2M') == 2 * 1024 * 1024
    assert human_to_bytes('2M', isbits=True) == 2 * 1024 * 1024
    assert human_to_bytes('2Mb', isbits=True) == 2 * 1024 * 1024

    assert human_to_bytes('2MB', isbits=True) == 2 * 1024 * 1024 * 8
    assert human_to_bytes('2Mb', isbits=False) == 2 * 1024 * 1024 * 8

    assert human_to_bytes(2, 'Mb') == 2 * 1024 * 1024
    assert human_to_bytes(2, 'Mb', isbits=True) == 2 * 1024 * 1024

# Generated at 2022-06-12 23:58:27.666771
# Unit test for function lenient_lowercase
def test_lenient_lowercase():

    class TestObject(object):
        def __init__(self, v):
            self.v = v

        def __str__(self):
            return str(self.v)

    # Scalar to lowercase
    assert lenient_lowercase(10) == 10
    assert lenient_lowercase(10.0) == 10.0
    assert lenient_lowercase(u'10') == u'10'

    # Strings to lowercase
    assert lenient_lowercase(['foo', 'bAR']) == ['foo', 'bar']
    assert lenient_lowercase(['hello', TestObject('WORLD')]) == ['hello', TestObject('WORLD')]

# Generated at 2022-06-12 23:58:32.924119
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Positive test cases
    assert lenient_lowercase(['a', 'b', 1, 2, 3]) == ['a', 'b', 1, 2, 3]
    assert lenient_lowercase(['a', 'B', 1, 2, 'c']) == ['a', 'B', 1, 2, 'c']
    assert lenient_lowercase([]) == []

