

# Generated at 2022-06-12 23:48:42.142227
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['J', 'O', 'H', 'N', 'D', 'O', 'E']
    lower = lenient_lowercase(lst)

    assert lst[1] == 'O'
    assert lower[1] == 'o'

    lst = [1, 2, 3, 4, 5]
    lower = lenient_lowercase(lst)

    assert lst[0] == 1
    assert lower[0] == 1

# Generated at 2022-06-12 23:48:51.948253
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("10M") == 10485760
    assert human_to_bytes("1Mb", isbits=True) == 1048576
    assert human_to_bytes("0.5G") == 536870912
    assert human_to_bytes("1") == 1
    assert human_to_bytes("10MB") == 10485760
    assert human_to_bytes("10Mb", isbits=True) == 1048576
    assert human_to_bytes("1,024MB") == 1073741824
    assert human_to_bytes("1,024Mb", isbits=True) == 134217728
    assert human_to_bytes(1048576) == 1048576
    assert human_to_bytes(1048576, unit="K") == 1024

# Generated at 2022-06-12 23:49:02.128105
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = [
        ('1B', 1),
        ('2K', 2 << 10),
        ('3M', 3 << 20),
        ('4G', 4 << 30),
        ('5T', 5 << 40),
        ('6P', 6 << 50),
        ('7E', 7 << 60),
        ('8Z', 8 << 70),
        ('9Y', 9 << 80),
        ('10B', 10),
        ('11Kb', 11 << 7),
        ('12Mb', 12 << 17),
        ('13Gb', 13 << 27),
        ('14Tb', 14 << 37),
        ('15Pb', 15 << 47),
        ('16Eb', 16 << 57),
        ('17Zb', 17 << 67),
        ('18Yb', 18 << 77),
    ]


# Generated at 2022-06-12 23:49:10.741741
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("1") == 1
    assert human_to_bytes("1K") == 1000
    assert human_to_bytes("1Kb") == 1000
    assert human_to_bytes("1 mb", isbits=True) == 1000*1000
    assert human_to_bytes("1 gb", isbits=True) == 1000*1000*1000
    assert human_to_bytes("1TB") == 1000*1000*1000*1000
    assert human_to_bytes("1PB") == 1000*1000*1000*1000*1000
    assert human_to_bytes("2E") == 2*1000*1000*1000*1000*1000
    assert human_to_bytes("3Z") == 3*1000*1000*1000*1000*1000*1000
    assert human_to_bytes("4Y") == 4*1000*1000*1000

# Generated at 2022-06-12 23:49:12.570536
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a1', 'A2', 'b3', 'B4']) == ['a1', 'a2', 'b3', 'b4']


# Generated at 2022-06-12 23:49:20.640233
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M', 'B') == 10485760
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10M', 'b') == 10485760 * 8
    assert human_to_bytes('10M', isbits=True) == 10485760 * 8

    assert human_to_bytes('10Mb', 'b') == 10485760 * 8
    assert human_to_bytes('10Mb', isbits=True) == 10485760 * 8

    assert human_to_bytes('10Mb', 'B') == 10485760
    assert human_to_bytes('10Mb', unit='B') == 10485760
    assert human_to_bytes('10Mb', unit='') == 10485760

    assert human

# Generated at 2022-06-12 23:49:31.529646
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1GB', isbits=True) == 8589934592
    assert human_to_bytes('1GB', isbits=True, unit='b') == 8589934592
    assert human_to_bytes('2T', unit='b') == 171798691840
    assert human_to_bytes('1B', unit='b') == 8
    assert human_to_bytes('1b') == 8
    assert human_to_bytes('1Bb') == 8
    assert human_to_bytes('1bb') == 1
    assert human_to_bytes('1bbB') == 1

# Generated at 2022-06-12 23:49:42.529960
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = [('1KB', 1024),
             ('2.0K', 2048),
             ('1b', 1),
             ('1kb', 1000),
             ('1.0mb', 1000 * 1000),
             ('1MB', 1 << 20),
             ('1Mb', 1 << 17),
             ('1G', 1 << 30),
             ('1.1G', (1 << 30) + (1 << 29)),
             ('1T', 1 << 40),
             ('1P', 1 << 50),
             ('1E', 1 << 60),
             ('1Z', 1 << 70),
             ('1Y', 1 << 80),
             ('1.1Y', (1 << 80) + (1 << 79))]

    for input_val, result in tests:
        assert human_to_bytes(input_val, 'B') == result
       

# Generated at 2022-06-12 23:49:52.639284
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(256, unit='k') == '0.25 KB'
    assert bytes_to_human(256, unit='m') == '0.00 MB'
    assert bytes_to_human(1024, unit='m') == '0.00 MB'
    assert bytes_to_human(1048576, unit='m') == '1.00 MB'
    assert bytes_to_human(1024, unit='k') == '1.00 KB'
    assert bytes_to_human(1048576, unit='k') == '1024.00 KB'
    assert bytes_to_human(1024 * 1024 * 1024 * 1.5, unit='k') == '1572864.00 KB'
    assert bytes_to_human(1048576, unit='b') == '8388608.00 bits'
    assert bytes_to

# Generated at 2022-06-12 23:50:00.294255
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(10 ** 0) == '1 Bytes'
    assert bytes_to_human(10 ** 1) == '10 Bytes'
    assert bytes_to_human(10 ** 2) == '100 Bytes'
    assert bytes_to_human(10 ** 3) == '1.00 KB'
    assert bytes_to_human(10 ** 4) == '10.00 KB'
    assert bytes_to_human(10 ** 5) == '100.00 KB'
    assert bytes_to_human(10 ** 6) == '1.00 MB'
    assert bytes_to_human(10 ** 7) == '10.00 MB'
    assert bytes_to_human(10 ** 8) == '100.00 MB'
    assert bytes_to_human(10 ** 9) == '1.00 GB'

# Generated at 2022-06-12 23:50:17.392474
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # when input list has all strings
    if lenient_lowercase(['test1', 'test2', 'test3']) != ['test1', 'test2', 'test3']:
        print("lenient_lowercase: FAIL")
        return 1
    # when input list has a non-string
    if lenient_lowercase(['test1', 'test2', 'test3', 1]) != ['test1', 'test2', 'test3', 1]:
        print("lenient_lowercase: FAIL")
        return 1
    # when input list is empty
    if lenient_lowercase([]) != []:
        print("lenient_lowercase: FAIL")
        return 1
    print("lenient_lowercase: PASS")
    return 0

# Input: human_to_bytes(*args, **kwargs)


# Generated at 2022-06-12 23:50:19.110180
# Unit test for function lenient_lowercase
def test_lenient_lowercase():

    lst = ['a', None, 1, 'c', 'B']

    assert ['a', None, 1, 'c', 'b'] == lenient_lowercase(lst)

# Generated at 2022-06-12 23:50:28.502957
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10 * 1024 * 1024, 'Error on human_to_bytes conversion with default unit'
    assert human_to_bytes(10, 'M') == 10 * 1024 * 1024, 'Error on human_to_bytes conversion'
    assert human_to_bytes('10Kb') == 10 * 1024, 'Error on human_to_bytes conversion for bits'
    assert human_to_bytes('10Mb') == 10 * 1024 * 1024, 'Error on human_to_bytes conversion for bits'
    assert human_to_bytes('10MB') == 10 * 1024 * 1024, 'Error on human_to_bytes conversion'
    assert human_to_bytes('2M') == 2 * 1024 * 1024, 'Error on human_to_bytes conversion'
    assert human_to_bytes('100.5M', 'b')

# Generated at 2022-06-12 23:50:34.544394
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('0') == 0
    assert human_to_bytes('0.54') == 0
    assert human_to_bytes('1') == 1
    assert human_to_bytes('54') == 54
    assert human_to_bytes('54.33') == 54
    assert human_to_bytes('0K') == 0
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('0B') == 0
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('0.54K') == 0
    assert human_to_bytes('0.54G') == 0
    assert human_to_bytes('0.54Y') == 0
    assert human_to_bytes('1Kb') == 128

# Generated at 2022-06-12 23:50:42.206410
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(0) == '0 Bytes'
    assert bytes_to_human(0, unit='b') == '0 bits'
    assert bytes_to_human(200000) == '195.31 KB'
    assert bytes_to_human(200000, unit='B') == '195.31 KB'
    assert bytes_to_human(200000, unit='K') == '195.31 KB'
    assert bytes_to_human(200000, unit='Bits') == '1.58 MB'
    assert bytes_to_human(200000, isbits=True) == '1.58 MB'
    assert bytes_to_human(200000, unit='b') == '1.58 MB'



# Generated at 2022-06-12 23:50:48.335782
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2') == 2
    assert human_to_bytes('2', 'K') == 2048
    assert human_to_bytes('1', unit='k') == 1024
    assert human_to_bytes('2', unit='k') == 2048
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1.5Mb', isbits=True) == 1572864
    assert human_to_bytes('1.5', unit='m') == 1572864
    assert human_to_bytes('1.5b') == 0.1875
    assert human_to_bytes('1.5b', isbits=True) == 0.1875
    assert human_to_bytes('1.5', unit='b') == 0.1875

# Generated at 2022-06-12 23:50:55.797062
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['a', 'B', 'c', None, 'd', 'eFg']
    lc_lst = lenient_lowercase(lst)
    assert lc_lst == ['a', 'b', 'c', None, 'd', 'efg'], "Got %s expected %s" % (lc_lst, ['a', 'b', 'c', None, 'd', 'efg'])



# Generated at 2022-06-12 23:51:04.900721
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:16.405268
# Unit test for function bytes_to_human
def test_bytes_to_human():
    assert bytes_to_human(42) == '42.00 Bytes'
    assert bytes_to_human(456) == '456.00 Bytes'
    assert bytes_to_human(42, isbits=True) == '336.00 bits'
    assert bytes_to_human(42, isbits=True, unit='b') == '336.00 bits'

    assert bytes_to_human(1 << 10) == '1.00 KB'
    assert bytes_to_human(1 << 20) == '1.00 MB'
    assert bytes_to_human(1 << 30) == '1.00 GB'
    assert bytes_to_human(1 << 40) == '1.00 TB'
    assert bytes_to_human(1 << 50) == '1.00 PB'

# Generated at 2022-06-12 23:51:22.115286
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test empty list
    assert lenient_lowercase([]) == []

    # Test a list mixed with string and non-string elements
    assert lenient_lowercase(['a', 'B', 'c', 1]) == ['a', 'b', 'c', 1]

    # Test a list with all string elements
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']


# Generated at 2022-06-12 23:51:33.157120
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('2M') == 2097152
    assert human_to_bytes('10G') == 10737418240
    assert human_to_bytes('1Mb') == 131072
    assert human_to_bytes('1Mb', isbits=True) == 131072
    assert human_to_bytes('2Kb') == 2048
    assert human_to_bytes('2Kb', isbits=True) == 2048
    assert human_to_bytes('10Gb') == 13421772800
    assert human_to_bytes('10Gb', isbits=True) == 13421772800
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1MB', isbits=True) == 1048576


# Generated at 2022-06-12 23:51:42.380693
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10Mb') == human_to_bytes(10, 'Mb', isbits=True) == 10485760
    assert human_to_bytes('10b') == human_to_bytes(10, 'b', isbits=True) == 10
    assert human_to_bytes('10', 'M') == 10485760
    assert human_to_bytes(10485760, 'G') == 10
    assert human_to_bytes(10485760, 'G', isbits=True) == 10

# Generated at 2022-06-12 23:51:46.094309
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    list_of_strings = ['foo', 'BAR', 'baz']
    assert lenient_lowercase(list_of_strings) == ['foo', 'bar', 'baz']


# Generated at 2022-06-12 23:51:50.857059
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Foo', 'Bar', 'BaZ']) == ['foo', 'bar', 'baz']
    assert lenient_lowercase(['Foo', 1, 'BaZ']) == ['foo', 1, 'baz']


# Generated at 2022-06-12 23:51:59.364162
# Unit test for function human_to_bytes
def test_human_to_bytes():
    testcases = {
        "10M": 10485760,
        "1M": 1048576,
        "B": 1,
        "K": 1024,
        "10G": 10737418240,
        "1GB": 1073741824,
        "1gB": None,
        "1Mb": 1048576,
        "1Mb_2": None,
        "Mb_2": None,
        "1MB": None,
        "10Mb": None,
        "10Mb_2": None,
    }

    for test, expected in testcases.items():
        if expected:
            assert(human_to_bytes(test) == expected)


# Generated at 2022-06-12 23:52:10.595173
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10M', 'B') == 10485760
    assert human_to_bytes('10M', 'm') == 10485760
    with pytest.raises(ValueError):
        human_to_bytes('10Z')
    with pytest.raises(ValueError):
        human_to_bytes('10Z', default_unit='z')
    with pytest.raises(ValueError):
        human_to_bytes('10B') == 1028
    with pytest.raises(ValueError):
        human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760

# Generated at 2022-06-12 23:52:20.375713
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('0') == 0
    assert human_to_bytes('5') == 5
    assert human_to_bytes('11MB') == 11 * (1 << 20)
    assert human_to_bytes('11.2MB') == 11.2 * (1 << 20)
    assert human_to_bytes('11.2M') == 11.2 * (1 << 20)
    assert human_to_bytes('11.2Mb', isbits=True) == 11.2 * (1 << 20)
    assert human_to_bytes('11.2Mb') == 11.2 * (1 << 20)
    assert human_to_bytes('11.2Mb', default_unit='B') == 11.2 * (1 << 20)

# Generated at 2022-06-12 23:52:24.277460
# Unit test for function lenient_lowercase
def test_lenient_lowercase():

    assert lenient_lowercase([u'a', u'B', 'c']) == [u'a', u'b', 'c']
    assert lenient_lowercase([1, u'B', 3]) == [1, u'b', 3]
    assert lenient_lowercase(['aaa', 2, u'C']) == ['aaa', 2, u'c']



# Generated at 2022-06-12 23:52:26.784183
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['1', '2', '3']) == ['1', '2', '3']
    assert lenient_lowercase(['1', 2, '3']) == ['1', 2, '3']



# Generated at 2022-06-12 23:52:29.108469
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['asr', 'ASR', 'iTRANS', 'itrans']
    assert lenient_lowercase(lst) == ['asr', 'asr', 'itrans', 'itrans']



# Generated at 2022-06-12 23:52:43.639337
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """
    Test function human_to_bytes and bytes_to_human
    :return:
    """

    # Test bytes value
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1byte') == 1
    assert human_to_bytes('1bytes') == 1
    assert human_to_bytes('1 B') == 1
    assert human_to_bytes('1Byte') == 1
    assert human_to_bytes('1Bytes') == 1
    assert human_to_bytes('1byte') == 1
    assert human_to_bytes('1bytes') == 1

    assert human_to_bytes('1k') == 1 << 10
    assert human_to_bytes('1K') == 1 << 10
    assert human_to_bytes('1Ki') == 1 << 10
    assert human_to_

# Generated at 2022-06-12 23:52:55.094516
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(1) == 1
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1GB', isbits=True) == 1073741824
    assert human_to_bytes('1MB', isbits=True) == 1048576
    assert human_to_bytes(1048576, isbits=True) == 1048576
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('10b', isbits=True) == 10


# Generated at 2022-06-12 23:53:00.537496
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network.nxos.nxos import load_config, run_commands
    import sys

    def test(result, expected_result, MODULE):
        if result != expected_result:
            MODULE.fail_json(msg="test fail: expected {0} but got {1}".format(expected_result, result))
        else:
            MODULE.exit_json(msg="test success!")

    human_numbers = ['1b', '2KB', '3.2Mb', '4.5MB', '5G', '6.5GB', '7.6Pb', '8.7PB', '9Tb', '10EB', '0.5']

# Generated at 2022-06-12 23:53:06.928169
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:18.379704
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('', default_unit='M') == 0)
    assert(human_to_bytes(0) == 0)
    assert(human_to_bytes('1b') == 1)
    assert(human_to_bytes(1, 'b') == 1)
    assert(human_to_bytes('2KB') == 2048)
    assert(human_to_bytes(2, 'K', isbits=False) == 2048)
    assert(human_to_bytes('3M') == 3145728)
    assert(human_to_bytes(3, 'M') == 3145728)
    assert(human_to_bytes('4Mb') == 4194304)
    assert(human_to_bytes(4, 'M', isbits=True) == 4194304)

# Generated at 2022-06-12 23:53:27.256575
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import unittest
    # testing input: val, expected output, unit of measurement

# Generated at 2022-06-12 23:53:38.560004
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('1') == 1)
    assert(human_to_bytes('2.5') == 2)
    assert(human_to_bytes('0.5') == 0)
    assert(human_to_bytes('0') == 0)
    assert(human_to_bytes('TB') == None)
    assert(human_to_bytes('10MB') == 10485760)
    assert(human_to_bytes('10 Mb') == 10485760)
    assert(human_to_bytes('1Mb', isbits=True) == 1048576)
    assert(human_to_bytes('1Mb', isbits=False) == 1048576)
    assert(human_to_bytes('1Mb', isbits=1) == 1048576)

# Generated at 2022-06-12 23:53:42.136827
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'b', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'b', 'C', 1]) == ['a', 'b', 'c', 1]


# Generated at 2022-06-12 23:53:49.887245
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import unittest

    class TestHumanToBytes(unittest.TestCase):

        def test_bytes_to_human(self):
            self.assertEqual(bytes_to_human(0), '0 Bytes')
            self.assertEqual(bytes_to_human(10), '10 Bytes')
            self.assertEqual(bytes_to_human(100), '100 Bytes')
            self.assertEqual(bytes_to_human(1000), '1000 Bytes')
            self.assertEqual(bytes_to_human(10000), '9.77 KB')
            self.assertEqual(bytes_to_human(10000000), '9.54 MB')
            self.assertEqual(bytes_to_human(100000000), '95.37 MB')

# Generated at 2022-06-12 23:54:01.008230
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('10M') == 10485760)
    assert(human_to_bytes('10b') == 1)
    assert(human_to_bytes(10, 'M') == 10485760)
    assert(human_to_bytes(10, unit='M') == 10485760)
    assert(human_to_bytes(10, 'm') == 10485760)
    assert(human_to_bytes(u'10 M') == 10485760)
    assert(human_to_bytes('10') == 10)
    assert(human_to_bytes('10b') == 1)
    assert(human_to_bytes('10K') == 10240)
    assert(human_to_bytes('10Kb') == 128)

# Generated at 2022-06-12 23:54:12.269431
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lower_lst = ['a', 'b', 1, 2]
    assert lenient_lowercase(lower_lst) == ['a', 'b', 1, 2]
    lower_lst = ['A', 'B', 1, 2]
    assert lenient_lowercase(lower_lst) == ['a', 'b', 1, 2]
    lower_lst = ['a', 'B', 1, 2]
    assert lenient_lowercase(lower_lst) == ['a', 'b', 1, 2]
    lower_lst = ['A', 'B', 1, 2, 'c', []]
    assert lenient_lowercase(lower_lst) == ['a', 'b', 1, 2, 'c', []]


# Generated at 2022-06-12 23:54:22.650317
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test with no unit specified
    assert human_to_bytes('123') == 123, "Test with no unit specified"

    # Test valid format with no decimal
    assert human_to_bytes('10M') == 10485760, "Test valid format with no decimal"
    assert human_to_bytes('10m') == 10485760, "Test valid format with no decimal"

    # Test valid format with decimal
    assert human_to_bytes('10.8M') == 11309760, "Test valid format with decimal"
    assert human_to_bytes('10.8m') == 11309760, "Test valid format with decimal"

    # Test valid format with space
    assert human_to_bytes('10 M') == 10485760, "Test valid format with space"
    assert human_to_bytes('10 m') == 1048

# Generated at 2022-06-12 23:54:24.373911
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Hello', 1, 'WoRlD']) == ['hello', 1, 'world']

# Generated at 2022-06-12 23:54:35.399945
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Byte formatting
    assert(human_to_bytes('1MB') == 1048576)
    assert(human_to_bytes('1KB') == 1024)
    assert(human_to_bytes('1B') == 1)
    assert(human_to_bytes('1M') == 1048576)
    assert(human_to_bytes('1K') == 1024)
    assert(human_to_bytes('1') == 1)
    # Bit formatting
    assert(human_to_bytes('1MB', isbits=True) == 134217728)
    assert(human_to_bytes('1KB', isbits=True) == 131072)
    assert(human_to_bytes('1B', isbits=True) == 8)

# Generated at 2022-06-12 23:54:38.165716
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Simple case
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

    # Keeps non-string values untouched
    assert lenient_lowercase(['A', None]) == ['a', None]

# Generated at 2022-06-12 23:54:43.925818
# Unit test for function human_to_bytes
def test_human_to_bytes():
    result = human_to_bytes('10M', default_unit='B')
    assert result == 10485760, "The result is not correct, expected 10485760, got %d" % result

    result = human_to_bytes('10', default_unit='M')
    assert result == 10485760, "The result is not correct, expected 10485760, got %d" % result

    result = human_to_bytes('10', default_unit='Mb', isbits=True)
    assert result == 10485760, "The result is not correct, expected 10485760, got %d" % result

    result = human_to_bytes('1Mb', default_unit=None, isbits=True)
    assert result == 1048576, "The result is not correct, expected 1048576, got %d" % result

# Generated at 2022-06-12 23:54:49.580431
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # no strings
    assert lenient_lowercase([0]) == [0]
    assert lenient_lowercase([]) == []

    # all strings
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase(['a', 'b']) == ['a', 'b']

    # both strings and non-strings
    assert lenient_lowercase(['A', 0, 'B']) == ['a', 0, 'b']
    assert lenient_lowercase(['a', 0, 'b']) == ['a', 0, 'b']


# Generated at 2022-06-12 23:54:53.115051
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]



# Generated at 2022-06-12 23:54:59.464744
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 3, 'Test', 'test2']) == [1, 2, 3, 'Test', 'test2']
    assert lenient_lowercase([1, 2, 'Test', 'test2']) == [1, 2, 'Test', 'test2']
    assert lenient_lowercase(['Test', 'test2']) == ['test', 'test2']

# Generated at 2022-06-12 23:55:09.742555
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert (human_to_bytes('0') == 0)
    assert (human_to_bytes(0) == 0)
    assert (human_to_bytes('1k') == 1024)
    assert (human_to_bytes(1.5, default_unit='k') == 1536)
    assert (human_to_bytes('1M', isbits=True) == 8388608)
    assert (human_to_bytes('10000000000') == 10000000000)
    assert (human_to_bytes('10000000000', unit='k') == 102400000000)
    assert (human_to_bytes('10000000000', unit='b') == 100000000000)
    assert (human_to_bytes('10000000000', unit='k', isbits=True) == 8388608000000)

# Generated at 2022-06-12 23:55:27.194610
# Unit test for function lenient_lowercase
def test_lenient_lowercase():

    assert lenient_lowercase(['a', 'b']) == ['a', 'b']
    assert lenient_lowercase([1, 2]) == [1, 2]

    """
    assert lenient_lowercase(['A', 1]) == ['a', 1]
    assert lenient_lowercase(['A', 1, 'B']) == ['a', 1, 'b']
    assert lenient_lowercase([1, 'A']) == [1, 'a']
    assert lenient_lowercase(['A']) == ['a']
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    """



# Generated at 2022-06-12 23:55:30.284748
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    expected = ['beef', 'potatoes', 1]
    actual = lenient_lowercase(['beef', 'potatoes', 1])
    assert expected == actual



# Generated at 2022-06-12 23:55:33.891757
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['a', 'b', 1, 2]
    test_list_lc = lenient_lowercase(test_list)
    assert test_list_lc == ['a', 'b', 1, 2]



# Generated at 2022-06-12 23:55:45.307099
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Unit test for function human_to_bytes'''

    # default
    assert human_to_bytes('10', default_unit="B") == 10
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10b') == 1
    assert human_to_bytes('10kb') == 10240
    assert human_to_bytes('10Kb') == 10240
    assert human_to_bytes('10kb', isbits=True) == 81920
    assert human_to_bytes('10Kb', isbits=True) == 81920
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('10Mb') == 1048576
    assert human_

# Generated at 2022-06-12 23:55:58.476917
# Unit test for function human_to_bytes
def test_human_to_bytes():
    n = human_to_bytes('100')
    assert n == 100, '"100" == %s' % n
    n = human_to_bytes('100B')
    assert n == 100, '"100B" == %s' % n
    n = human_to_bytes('100b', isbits=True)
    assert n == 100, '"100b" == %s' % n
    n = human_to_bytes('100b')
    assert n == 100, '"100b" == %s' % n
    n = human_to_bytes('100B', isbits=True)
    assert n == 100, '"100B" == %s' % n
    n = human_to_bytes('100KB')
    assert n == 100 * 1 << 10, '"100KB" == %s' % n
   

# Generated at 2022-06-12 23:56:05.637479
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # original list
    test_list = [0, 1, 'Apple', 'orange', 'Mango', 'Grapes']

    # list after function call
    result_list = lenient_lowercase(test_list)

    # expected output list
    expected_list = [0, 1, 'apple', 'orange', 'mango', 'grapes']

    # test assertion
    assert result_list == expected_list

# Generated at 2022-06-12 23:56:09.721350
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['AA', 'Ba']) == ['aa', 'Ba']
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase(['aA', 1, 2, 'aA']) == ['aa', 1, 2, 'aa']

# Generated at 2022-06-12 23:56:16.732041
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['', '', '']
    assert lenient_lowercase(lst) == [''] * len(lst)

    lst = []
    assert lenient_lowercase(lst) == [''] * len(lst)

    lst = ['TEST', 'TEST', 'TEST']
    assert lenient_lowercase(lst) == ['test', 'test', 'test']

    lst = ['test', 'test', 'test']
    assert lenient_lowercase(lst) == ['test', 'test', 'test']

    for i, j in enumerate(['test', 'test', 'test']):
        if i == 1:
            j = 1
        assert lenient_lowercase(lst)[i] == j

# Generated at 2022-06-12 23:56:29.766472
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['1', '2', '3']) == ['1', '2', '3']
    assert lenient_lowercase(['A', 'b', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([1, 'b', 'C']) == [1, 'b', 'c']
    assert lenient_lowercase(['A', 2, 3]) == ['a', 2, 3]
    assert lenient_lowercase(['A', 2, 'C']) == ['a', 2, 'c']
    assert lenient_lowercase([1, 'b', 'C']) == [1, 'b', 'c']

# Generated at 2022-06-12 23:56:39.981606
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:56:58.048008
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 2, 'C']) == ['a', 2, 'c']
    assert lenient_lowercase([]) == []


# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:57:04.787090
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list_1 = ['One', 2, 'Three']
    test_list_2 = [1, 2, 'test']
    test_list_3 = [1, 2, 'test', 'TEST']
    assert lenient_lowercase(test_list_1) == ['one', 2, 'three']
    assert lenient_lowercase(test_list_2) == [1, 2, 'test']
    assert lenient_lowercase(test_list_3) == [1, 2, 'test', 'TEST']

# Generated at 2022-06-12 23:57:15.737766
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M')

    assert human_to_bytes('10M') == 10 * (1 << 20)
    assert human_to_bytes('10M', isbits=True) == 10 * (1 << 20)
    assert human_to_bytes('10M') == human_to_bytes('10MB') == human_to_bytes('10MBB')
    assert human_to_bytes('10M', isbits=True) == human_to_bytes('10Mb') == human_to_bytes('10Mbb')
    assert human_to_bytes('10M') == human_to_bytes('10MiB') == human_to_bytes('10MiBB') == human_to_bytes('10mib') == human_to_bytes('10mibb')
   

# Generated at 2022-06-12 23:57:16.464093
# Unit test for function human_to_bytes
def test_human_to_bytes():
    pass


# Generated at 2022-06-12 23:57:23.469505
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:30.289733
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:40.402779
# Unit test for function human_to_bytes
def test_human_to_bytes():
    for n in ('-1', 0, 1, 10, '10', '10.1', '10.5', '10.51', '10.5M', '10.5K', '10.5G', '10.5Mb', '10.5B', '10.5'):
        try:
            human_to_bytes(n)
        except Exception as err:
            print('human_to_bytes() failed to convert %s (exception: %s)' % (n, err))
    try:
        human_to_bytes('1B', default_unit='B')
    except Exception as err:
        print('human_to_bytes() failed to convert 1B (exception: %s)' % err)

# Generated at 2022-06-12 23:57:50.698366
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=True) == ValueError

    assert human_to_bytes('', default_unit='K') == 0
    assert human_to_bytes(' ', default_unit='K') == 0
    assert human_to_bytes('1', default_unit='K') == 1
    assert human_to_bytes('1 ', default_unit='K') == 1
    assert human_to_bytes('1.1', default_unit='K') == 1.1

# Generated at 2022-06-12 23:58:04.457390
# Unit test for function human_to_bytes
def test_human_to_bytes():
    expected = 1048576
    assert expected == human_to_bytes('1MB')
    assert expected == human_to_bytes('1MB', None)
    assert expected == human_to_bytes(1, 'MB')
    expected = 1048576000
    assert expected == human_to_bytes(1000, 'MB')
    assert expected == human_to_bytes(1000, 'Mb')
    expected = 1073741824
    assert expected == human_to_bytes(1, 'GB')
    expected = 1099511627776
    assert expected == human_to_bytes(1, 'TB')
    expected = 1125899906842624
    assert expected == human_to_bytes(1, 'PB')
    expected = 1152921504606846976
    assert expected == human_to_bytes(1, 'EB')
   

# Generated at 2022-06-12 23:58:12.958729
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test bytes without unit
    assert(human_to_bytes('1000') == 1000)
    assert(human_to_bytes('1000.5') == 1000)
    # Test bytes with unit
    assert(human_to_bytes('1000', 'B') == 1000)
    assert(human_to_bytes('1000.5', 'B') == 1000)
    assert(human_to_bytes('1K', 'B') == SIZE_RANGES['K'])
    assert(human_to_bytes('1K', 'K') == SIZE_RANGES['K'])
    assert(human_to_bytes('1.5K', 'K') == SIZE_RANGES['K'] * 1.5)
    assert(human_to_bytes('1M', 'K') == SIZE_RANGES['M'])
   