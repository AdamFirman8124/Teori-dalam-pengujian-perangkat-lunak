

# Generated at 2022-06-12 23:48:43.213893
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    print(lenient_lowercase(["Lower", "CASE"]) == ["lower", "case"])
    print(lenient_lowercase([4, "numbers", 6, "and", "strings", 8]) == [4, "numbers", 6, "and", "strings", 8])
    print(lenient_lowercase(["lower", "lower", "lower"]) == ["lower", "lower", "lower"])


# Generated at 2022-06-12 23:48:50.555721
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 2, 'C']) == ['a', 2, 'c']
    assert lenient_lowercase(['A', [2, 3], 'C']) == ['a', [2, 3], 'c']
    assert lenient_lowercase(['A', ('B', 4, 'C'), 'D']) == ['a', ('B', 4, 'C'), 'd']

# Generated at 2022-06-12 23:48:52.436857
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["ONE", 2, "THREE"]) == ["one", 2, "three"]


# Generated at 2022-06-12 23:48:55.453679
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B', 'c', 'd']) == ['a', 'B', 'c', 'd']
    assert lenient_lowercase([1, 'B']) == [1, 'B']
    assert lenient_lowercase([]) == []

# Generated at 2022-06-12 23:49:06.389371
# Unit test for function human_to_bytes
def test_human_to_bytes():
    if human_to_bytes('1MB') != 1048576:
        print('[FAILED] human_to_bytes with 1MB != 1048576')
    if human_to_bytes('1MB', default_unit='B') != 1048576:
        print('[FAILED] human_to_bytes with 1MB and default_unit=B != 1048576')
    if human_to_bytes('1MB', default_unit='b', isbits=True) != 1048576:
        print('[FAILED] human_to_bytes with 1MB, default_unit=b and isbits=True != 1048576')

# Generated at 2022-06-12 23:49:15.888077
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:27.019981
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1B', isbits=True) == 1
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1E', isbits=True) == 1152921504606846976
    assert human_to_bytes('1EB') == 1152921504606846976
    assert human_to_bytes('1EB', isbits=True) == 115

# Generated at 2022-06-12 23:49:30.489444
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    string_list = ['foo', 1, 'Bar', True, 'Baz']
    assert lenient_lowercase(string_list) == ['foo', 1, 'bar', True, 'baz']



# Generated at 2022-06-12 23:49:37.152263
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # testing invalid input
    test_input = [None, [], 'test', '', '123test']
    for inp in test_input:
        try:
            out = human_to_bytes(inp)
        except Exception:
            pass
        else:
            err = 'human_to_bytes() failed to convert %s. Value is not a valid string (expect number)' % inp
            raise AssertionError(err)

    # testing valid input
    test_input = [('1', 1), ('+1', 1), ('-1', -1), ('0', 0), ('1.1', 1.1), ('1.1b', 1.1), ('+1.1', 1.1), ('-1.1', -1.1)]
    for inp, out in test_input:
        result = human_

# Generated at 2022-06-12 23:49:38.978612
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'a']) == [1, 'a']
    assert lenient_lowercase(['A', 'b']) == ['a', 'b']



# Generated at 2022-06-12 23:49:49.469700
# Unit test for function human_to_bytes
def test_human_to_bytes():
    result = human_to_bytes('1MB')
    assert result == 1048576

    result = human_to_bytes('1b')
    assert result == 1

    result = human_to_bytes('1B')
    assert result == 1

    result = human_to_bytes('1Mb')
    assert result == 1048576

    result = human_to_bytes('1MB', isbits=True)
    assert result == 8388608

    result = human_to_bytes('1B', isbits=True)
    assert result == 8

    result = human_to_bytes('1b', isbits=True)
    assert result == 1



# Generated at 2022-06-12 23:49:58.171579
# Unit test for function human_to_bytes
def test_human_to_bytes():
    out = human_to_bytes(1024)
    assert out == 1024
    out = human_to_bytes(1024, 'B')
    assert out == 1024
    out = human_to_bytes(1.21, 'KB')
    assert out == 1288

    out = human_to_bytes('1.21kb')
    assert out == 1.21*SIZE_RANGES['K']
    out = human_to_bytes('1.21kb', 'b')
    assert out == 1.21*SIZE_RANGES['K']
    out = human_to_bytes('1.21KB')
    assert out == 1.21*SIZE_RANGES['K']

    out = human_to_bytes('1.21Gb')
    assert out == 1.21*SIZE_RANGES['G']
    out = human_

# Generated at 2022-06-12 23:50:02.915571
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase(["a", "B", "c"]) == ["a", "B", "c"]
    assert lenient_lowercase(["a", 1, "B", None, "c"]) == ["a", 1, "B", None, "c"]



# Generated at 2022-06-12 23:50:15.232776
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10G') == 10737418240
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10K') == 10240
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10KB') == 10240
    assert human_to_bytes('10Kb', isbits=True) == 1280
    assert human_to_bytes('10Mb', isbits=True) == 1310720
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10Mb', unit='b', isbits=True) == 1310720
   

# Generated at 2022-06-12 23:50:20.597320
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [['a', 'b', 3], ['D', 1], ['f', 'g', 'h']]
    assert lenient_lowercase(test_list) == [['a', 'b', 3], ['d', 1], ['f', 'g', 'h']]

# Generated at 2022-06-12 23:50:29.564079
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('1 MB') == 1048576
    assert human_to_bytes('1.1 MB') == 1153433
    assert human_to_bytes('1.1 MB', 'MB') == 1153433
    assert human_to_bytes('1.1 MB', default_unit='MB') == 1153433
    assert human_to_bytes(1.1, 'MB') == 1153433
    assert human_to_bytes('1.0 b') == 1
    assert human_to_bytes('1.0 B') == 1
    assert human_to_bytes('1.0 b', isbits=True) == 1

# Generated at 2022-06-12 23:50:33.038427
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, "A", "B", 3, '1', '2', '3']
    assert lenient_lowercase(lst) == [1, "a", "b", 3, '1', '2', '3']



# Generated at 2022-06-12 23:50:36.336176
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']


# Generated at 2022-06-12 23:50:43.861358
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2B') == 2
    assert human_to_bytes('2KB') == 2*1024
    assert human_to_bytes('2MB') == 2*1024*1024
    assert human_to_bytes('2GB') == 2*1024*1024*1024
    assert human_to_bytes('2TB') == 2*1024*1024*1024*1024
    assert human_to_bytes('2PB') == 2*1024*1024*1024*1024*1024
    assert human_to_bytes('2EB') == 2*1024*1024*1024*1024*1024*1024
    assert human_to_bytes('2ZB') == 2*1024*1024*1024*1024*1024*1024*1024
    assert human_to_bytes('2YB') == 2*1024*1024*1024*1024*1024*1024*1024*1024

# Generated at 2022-06-12 23:50:51.720223
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:51:05.078187
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes(' 1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes(' 1 ') == 1
    assert human_to_bytes('1 ') == 1
    assert human_to_bytes(' 1 ') == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes(' 1.0') == 1
    assert human_to_bytes('1.0 ') == 1
    assert human_to_bytes(' 1.0 ') == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes(' 1.5') == 1
    assert human_to_bytes('1.5 ') == 1

# Generated at 2022-06-12 23:51:16.587418
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Assert to check invalid input
    try:
        assert human_to_bytes('20') != 20
    except ValueError as e:
        pass
    except Exception as e:
        assert False, "Unexpected exception raised: " + str(e)

    # Assert to check valid input
    assert human_to_bytes('20B') == 20, "Status code is not matching"
    assert human_to_bytes('20K') == 20480, "Status code is not matching"
    assert human_to_bytes('20M') == 20971520, "Status code is not matching"
    assert human_to_bytes('20G') == 21474836480, "Status code is not matching"
    assert human_to_bytes('20T') == 21990232555520, "Status code is not matching"
    assert human_to_

# Generated at 2022-06-12 23:51:25.873320
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test cases from:
    # http://www.binaryconvert.com/result_decimal.html
    #
    # tests for case sensitivity
    assert human_to_bytes('1kB') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1mb') == 1048576
    assert human_to_bytes('1MB') == 1048576

    # tests for case single 'b'
    assert human_to_bytes('1B', isbits=True) == 8
    assert human_to_bytes('1b', isbits=True) == 8

    # tests for case 'B'
    assert human_to_bytes('1B', isbits=False) == 1

# Generated at 2022-06-12 23:51:27.645321
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['a', 1, 'c'] == lenient_lowercase(['A', 1, 'c'])



# Generated at 2022-06-12 23:51:32.650569
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['asd', 'asda', [], [1, 2, 3], 'ASD', '', '', 'asd']) == ['asd', 'asda', [], [1, 2, 3], 'ASD', '', '', 'asd']
    assert lenient_lowercase(['', '']) == ['', '']
    assert lenient_lowercase([]) == []


# Generated at 2022-06-12 23:51:42.224241
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Bytes => int
    assert human_to_bytes('0B') == 0
    assert human_to_bytes('100B') == 100
    assert human_to_bytes('100b') == 100
    assert human_to_bytes('100 b') == 100
    assert human_to_bytes('100 byte') == 100
    assert human_to_bytes('100 bytes') == 100
    assert human_to_bytes('100 byte') == 100
    assert human_to_bytes('100bytes') == 100
    assert human_to_bytes('0.1M') == 100000
    assert human_to_bytes('0.1MB') == 100000
    assert human_to_bytes('0.1 Mb') == 100000
    assert human_to_bytes('0.1m') == 100000

# Generated at 2022-06-12 23:51:50.854944
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # test for list of strings
    l = ['a', 'B', 'C', 'd']
    r = lenient_lowercase(l)
    assert(r == ['a', 'b', 'c', 'd'])

    # test for list of strings and integers
    l = ['a', 'B', 'C', 'd', 1, 2, 3]
    r = lenient_lowercase(l)
    assert(r == ['a', 'b', 'c', 'd', 1, 2, 3])


# Generated at 2022-06-12 23:51:59.703131
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Test convertion of human-readable values (bytes, bits) to a number (bytes, bits)."""

    # {} - lowercase suffix

# Generated at 2022-06-12 23:52:10.908342
# Unit test for function human_to_bytes
def test_human_to_bytes():

    # Positive test cases
    if human_to_bytes('10') != 10:
        print("positive test for '10' failed")
    if human_to_bytes('10b') != 10:
        print("positive test for '10b' failed")
    if human_to_bytes('10B') != 10:
        print("positive test for '10B' failed")
    if human_to_bytes('1Mb') != 1048576:
        print("positive test for '1Mb' failed")
    if human_to_bytes('1MB') != 1048576:
        print("positive test for '1MB' failed")
    if human_to_bytes('1MBb') != 8388608:
        print("positive test for '1MBb' failed")

# Generated at 2022-06-12 23:52:20.628458
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10m') == 1048576
    assert human_to_bytes('10mb') == 1048576
    assert human_to_bytes('10mB') == 1048576
    assert human_to_bytes('10Kb') == 10240
    assert human_to_bytes('10kb') == 10240
    assert human_to_bytes('10kb', isbits=True) == 1024
    assert human_to_bytes('10Kb', isbits=True) == 10240
    assert human_to_bytes('10kb', unit='B') == 10240

# Generated at 2022-06-12 23:52:31.242548
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert(human_to_bytes('1K') == 1024)
    assert(human_to_bytes('1Kb') == 1024)
    assert(human_to_bytes('1KB') == 1024)
    assert(human_to_bytes('1M') == 1024**2)
    assert(human_to_bytes('1Mb') == 1024**2)
    assert(human_to_bytes('1MB') == 1024**2)
    assert(human_to_bytes('1G') == 1024**3)
    assert(human_to_bytes('1Gb') == 1024**3)
    assert(human_to_bytes('1GB') == 1024**3)
    assert(human_to_bytes('1T') == 1024**4)
    assert(human_to_bytes('1Tb') == 1024**4)

# Generated at 2022-06-12 23:52:36.393453
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(["A", "b", "c"]) == ["a", "b", "c"]
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase(["A"]) == ["a"]
    assert lenient_lowercase([1]) == [1]

# Generated at 2022-06-12 23:52:45.926830
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Bits
    assert human_to_bytes('10', 'b') == 10
    assert human_to_bytes('2.5Kb', isbits=True) == 2500
    assert human_to_bytes('3Mb', isbits=True) == 3000000
    assert human_to_bytes('4Gb', isbits=True) == 4000000000
    assert human_to_bytes('5Tb', isbits=True) == 5000000000000
    assert human_to_bytes('6Pb', isbits=True) == 6000000000000000
    assert human_to_bytes('7Eb', isbits=True) == 7000000000000000000
    assert human_to_bytes('8Zb', isbits=True) == 8000000000000000000000
    assert human_to_bytes('9Yb', isbits=True) == 9000000000000000000000000

    # Bytes


# Generated at 2022-06-12 23:52:56.975408
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:02.045451
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit tests for function human_to_bytes()"""
    # test exception when bad string passed
    raised_exception = False
    try:
        human_to_bytes("")
    except Exception:
        raised_exception = True
    assert raised_exception, "Exception should be raised when an empty string passed as a parameter"

    # test exception when bad string passed
    raised_exception = False
    try:
        human_to_bytes("A")
    except Exception:
        raised_exception = True
    assert raised_exception, "Exception should be raised when an not a number string passed as a parameter"

    # test exception when bad string passed
    raised_exception = False
    try:
        human_to_bytes("-2")
    except Exception:
        raised_exception = True

# Generated at 2022-06-12 23:53:08.573272
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [1, 'one', 'twO', 3]
    result_list = lenient_lowercase(test_list)
    assert test_list[0] == result_list[0]
    assert test_list[1].lower() == result_list[1]
    assert test_list[2].lower() == result_list[2]
    assert test_list[3] == result_list[3]

# Generated at 2022-06-12 23:53:18.988672
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test float
    assert human_to_bytes('1') == 1
    assert human_to_bytes('0.5') == 0
    assert human_to_bytes('1.23') == 1
    assert human_to_bytes('10.2') == 10
    assert human_to_bytes('10.7') == 11

    # Test Bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == human_to_bytes('1b')

    # Test KiloBytes
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1KByte') == 1024
   

# Generated at 2022-06-12 23:53:26.468154
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:38.197846
# Unit test for function human_to_bytes
def test_human_to_bytes():
    for key in SIZE_RANGES:
        size_range = SIZE_RANGES[key]
        size_range_bits = size_range * 8
        #test normal bytes
        print('Testing %s' % bytes_to_human(size_range))
        assert human_to_bytes(bytes_to_human(size_range)) == size_range
        #test lowercase k,m,g,t,p,e,z,y
        print('Testing %s' % bytes_to_human(size_range, unit=key.lower()))
        assert human_to_bytes(bytes_to_human(size_range, unit=key.lower())) == size_range
        #test bits
        print('Testing %s' % bytes_to_human(size_range_bits, isbits=True))
        assert human

# Generated at 2022-06-12 23:53:39.619447
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test human_to_bytes() with bytes formating
    asse

# Generated at 2022-06-12 23:53:56.765482
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['a', 'B', 'c', 1]
    expected_result = ['a', 'b', 'c', 1]

    # test the normal case
    assert expected_result == lenient_lowercase(test_list)

    # test the invalid case
    test_list = ['a', 'B', 'c', 1, '', {}]
    expected_result = ['a', 'b', 'c', 1, '', {}]

    assert expected_result == lenient_lowercase(test_list)


# Generated at 2022-06-12 23:54:06.833373
# Unit test for function human_to_bytes
def test_human_to_bytes():
    '''
    Checking conversion examples from documentation.
    '''
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2K', 'K') == 2048
    assert human_to_bytes('2', 'K') == 2048
    assert human_to_bytes('2', 'M') == 2000000
    assert human_to_bytes('2', 'G') == 2000000000
    assert human_to_bytes('2', 'T') == 2000000000000
    assert human_to_bytes('2', 'P') == 2000000000000000
    assert human_to_bytes('2', 'E') == 2000000000000000000
    assert human_to_bytes('2', 'Z') == 2000000000000000000000
    assert human_to_bytes('2', 'Y') == 2000000000000000000000000

# Generated at 2022-06-12 23:54:08.773172
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['a', 'B', 1, 2]
    result_list = ['a', 'b', 1, 2]
    assert lenient_lowercase(test_list) == result_list


# Generated at 2022-06-12 23:54:13.102238
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert ['mb', 'kb', 'gb'] == lenient_lowercase(['MB', 'kB', 'GB'])
    assert [1, 'mb', 3] == lenient_lowercase([1, 'MB', 3])



# Generated at 2022-06-12 23:54:23.068653
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes("1M") == 1048576
    assert human_to_bytes("1.0M") == 1048576
    assert human_to_bytes("2.0M") == 2097152
    assert human_to_bytes("1.0") == 1
    assert human_to_bytes("2.0") == 2
    assert human_to_bytes("1") == 1
    assert human_to_bytes("2") == 2
    assert human_to_bytes("1K") == 1024
    assert human_to_bytes("1k") == 1024
    assert human_to_bytes("1K") == 1024
    assert human_to_bytes("1k") == 1024
    assert human_to_bytes("1.0K") == 1024
    assert human

# Generated at 2022-06-12 23:54:34.196018
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Sanity check for function with default_unit=None
    assert human_to_bytes('1') == 1
    assert human_to_bytes('0') == 0
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('100') == 100
    assert human_to_bytes('100B') == 100
    assert human_to_bytes('100K') == 100 * 1 << 10
    assert human_to_bytes('100M') == 100 * 1 << 20
    assert human_to_bytes('100G') == 100 * 1 << 30
    assert human_to_bytes('100T') == 100 * 1 << 40
    assert human_to_bytes('100P') == 100 * 1 << 50
    # Input parameters are converted to a string before function evaluation
    assert human_to_bytes(100.0) == 100

# Generated at 2022-06-12 23:54:40.496898
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['Kb', 'MB', 1, 0, '0b', 'Kb', 1, '3', '0b']
    ret = lenient_lowercase(lst)
    assert ret == ['kb', 'mb', 1, 0, '0b', 'kb', 1, '3', '0b']



# Generated at 2022-06-12 23:54:42.545959
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(('abc', 2, 'xyZ')) == ['abc', 2, 'xyz']


# Generated at 2022-06-12 23:54:50.000990
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1000B') == 1000
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('10K') == 10240
    assert human_to_bytes('1.1K') == 1126
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('1.9K') == 1944
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1.1M') == 1153433
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1.9M') == 1992294

# Generated at 2022-06-12 23:55:02.406453
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M')
    assert human_to_bytes('10M', default_unit='B') == human_to_bytes(10, 'B')
    assert human_to_bytes('10M', default_unit='B') == human_to_bytes(10, 'B', isbits=True)

    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('10MB', default_unit='B') == human_to_bytes(10, 'B')
    assert human_to_bytes('10MB', default_unit='B') == 10485760

    assert human_to_bytes('10.5M') == 10485760
    assert human_

# Generated at 2022-06-12 23:55:23.793634
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['foo', 1, 'bar']) == ['foo', 1, 'bar']

# Generated at 2022-06-12 23:55:32.078256
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase([1, '2']) == [1, '2']
    assert lenient_lowercase(['1', '2']) == ['1', '2']
    assert lenient_lowercase(['1', '2', '3']) == ['1', '2', '3']
    assert lenient_lowercase(['1', '2', '3', '4']) == ['1', '2', '3', '4']


# Generated at 2022-06-12 23:55:38.608549
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c', 'd']) == ['a', 'b', 'c', 'd']
    assert lenient_lowercase(['A', 'b', 'c', 'D']) == ['a', 'b', 'c', 'd']
    assert lenient_lowercase(['A', 'b', 1, 'D']) == ['a', 'b', 1, 'd']
    assert lenient_lowercase(['A', 'b', 1.0, 'D']) == ['a', 'b', 1.0, 'd']

# Generated at 2022-06-12 23:55:48.104919
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:55:53.891470
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    list1 = ['a', 'b', 'c']
    list2 = ['a', 1, 'c']
    list3 = [1, 2, 3]

    assert lenient_lowercase(list1) == ['a', 'b', 'c']
    assert lenient_lowercase(list2) == ['a', 1, 'c']
    assert lenient_lowercase(list3) == [1, 2, 3]

# Generated at 2022-06-12 23:56:05.950265
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Negative scenarios
    assert human_to_bytes('', unit='B') == 0
    assert human_to_bytes(None) == 0
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10T') == human_to_bytes('10T', unit='B')
    assert human_to_bytes('10T', unit='K') == 0
    assert human_to_bytes('-1') == 0
    # Positive scenarios
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.2') == 1
    assert human_to_bytes('1.2B') == 1
    assert human_to_bytes('1.2b') == human_to_bytes('1.2b', isbits=True)

# Generated at 2022-06-12 23:56:14.798823
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    result = lenient_lowercase([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5], 'Numbers passed through untouched'

    result = lenient_lowercase(['a', 'b', 'c', 'd', 'e'])
    assert result == ['a', 'b', 'c', 'd', 'e'], 'Lowercase had no effect'

    result = lenient_lowercase(['A', 'B', 'C', 'D', 'E'])
    assert result == ['a', 'b', 'c', 'd', 'e'], 'Lowercase did not work as expected'

    result = lenient_lowercase(['A', 'b', 'C', 'd', 'E'])

# Generated at 2022-06-12 23:56:21.648038
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 1, 'c']) == ['a', 1, 'c']
    assert lenient_lowercase(['a', 'B', 'C']) == ['a', 'B', 'C']
    assert lenient_lowercase(['a', 'b', 'c']) != ['A', 'B', 'C']


# Generated at 2022-06-12 23:56:26.796452
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    """Unit test function for function lenient_lowercase()
    """
    test_dict = {1: 'first', 'two': 2, 'THREE': [3, 'three']}
    expect = {1: 'first', 'two': 'two', 'THREE': ['three', 'three']}
    assert lenient_lowercase(test_dict) == expect



# Generated at 2022-06-12 23:56:36.104931
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = list(range(1000))
    for i in range(10):
        lst[i] = str(lst[i])
    lst[15] = 'TEST'
    lst[45] = 'YES'
    lst[500] = 'NO'
    lst[634] = 'TEST2'
    lst = lenient_lowercase(lst)
    assert 'TEST' not in lst
    assert 'YES' not in lst
    assert 'NO' not in lst
    assert 'TEST2' not in lst

    lst = ['a', 'b', 'c', 'd']
    lst = lenient_lowercase(lst)
    assert lst == ['a', 'b', 'c', 'd']



# Generated at 2022-06-12 23:57:21.446142
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = [
        ('1', '1'),
        ('1.5', '2'),
        ('1.6', '2'),
        ('1B', '1'),
        ('1kb', ValueError),
        ('1Kb', '1024'),
        ('1MB', '1048576'),
        ('1b', ValueError),
        ('1kb', ValueError),
        ('1Kb', '1024'),
        ('1Mb', '1048576'),
    ]


# Generated at 2022-06-12 23:57:29.290979
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Test human_to_bytes()"""
    def test(number, expected, expected_bits=None, unit=None, isbits=False):
        if unit:
            number = '%s %s' % (number, unit)
        result = human_to_bytes(number, isbits=isbits, default_unit=unit)
        if result != expected:
            raise AssertionError("Expected %s for %s, got %s" % (expected, number, result))
        result = bytes_to_human(result, isbits=isbits, unit=unit)
        if expected_bits and expected_bits != result:
            raise AssertionError("Expected %s for %s, got %s" % (expected_bits, number, result))

    test(1, 1)
    test('1', 1)

# Generated at 2022-06-12 23:57:32.779279
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'B']) == ['a', 'b']
    assert lenient_lowercase(['a', 1]) == ['a', 1]

# Generated at 2022-06-12 23:57:36.317673
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['hello', 'world', 1, 2, 3]) == ['hello', 'world', 1, 2, 3]
    assert lenient_lowercase(['HELLO', 'world', 1, 2, 3]) == ['hello', 'world', 1, 2, 3]

# Generated at 2022-06-12 23:57:40.041323
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    testlist = ['a', 5, 'b', 'c', None]
    assert lenient_lowercase(testlist) == ['a', 5, 'b', 'c', None]


# Generated at 2022-06-12 23:57:41.984634
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ABC', 123]) == ['abc', 123]

# Generated at 2022-06-12 23:57:51.557818
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Check human_to_bytes input as string
    assert '{}'.format(human_to_bytes('1B')) == '1'
    assert '{}'.format(human_to_bytes('1K')) == '1024'
    assert '{}'.format(human_to_bytes('1M')) == '1048576'
    assert '{}'.format(human_to_bytes('1G')) == '1073741824'
    assert '{}'.format(human_to_bytes('1T')) == '1099511627776'
    assert '{}'.format(human_to_bytes('1P')) == '1125899906842624'
    assert '{}'.format(human_to_bytes('1E')) == '1152921504606847000'

# Generated at 2022-06-12 23:58:02.462222
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit test for function human_to_bytes.

    Tests resolution of size value to bytes, when using suffix and using
    bytes identifier:
    """
    tests = [
        ('1Mb', 1048576, True),
        ('1.5Mb', 1536000, True),
        ('10GB', 10737418240, False),
        ('10G', 10737418240, False),
        ('10', 10, False),
        ('10B', 10, False),
    ]

    for value, result, isbits in tests:
        assert human_to_bytes(value, isbits=isbits) == result

# Generated at 2022-06-12 23:58:04.633585
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'c', 1, 2]) == ['a', 'b', 'c', 1, 2]

# Generated at 2022-06-12 23:58:07.626110
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['test1', 'test2', 3]

    assert lenient_lowercase(lst) == ['test1', 'test2', 3]