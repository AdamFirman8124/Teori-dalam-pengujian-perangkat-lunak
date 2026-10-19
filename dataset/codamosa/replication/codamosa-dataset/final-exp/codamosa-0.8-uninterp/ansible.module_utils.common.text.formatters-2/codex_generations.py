

# Generated at 2022-06-12 23:48:53.283678
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1.5KB') == 1536
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1KB', default_unit='B') == 1
    assert human_to_bytes('1KB', default_unit='B', isbits=True) == 1
    assert human_to_bytes('1Kb', default_unit='B') == 1
    assert human_to_bytes('1Kb', default_unit='B', isbits=True) == 1
    assert human_to_bytes('1KB', default_unit='B') == 1
    assert human_to_bytes('1KB', default_unit='B', isbits=True) == 1
    assert human_

# Generated at 2022-06-12 23:49:03.393686
# Unit test for function human_to_bytes
def test_human_to_bytes():
    test_string = '10MB'
    assert human_to_bytes(test_string) == 10485760

    test_number = 10
    assert human_to_bytes(test_number) == 10
    assert human_to_bytes(test_number, 'MB') == 10485760
    assert human_to_bytes(test_number, 'kb') == 10230

    test_mixture = '10gb'
    assert human_to_bytes(test_mixture) == 104857600

    test_mixture_lowercase = '10Gb'
    assert human_to_bytes(test_mixture_lowercase) == 104857600

    test_invalid_unit = '10Kb'

# Generated at 2022-06-12 23:49:11.729005
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:20.585542
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # bytes
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10byte') == 10
    assert human_to_bytes('10bytes') == 10

    # kibibytes
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1kib') == 1024
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1KiB') == 1024
    assert human_to_bytes('1Ki') == 1024
    assert human_to_bytes('1 KiB') == 1024
    assert human_to_bytes('1.5KiB') == 1536

# Generated at 2022-06-12 23:49:31.443777
# Unit test for function human_to_bytes
def test_human_to_bytes():
    valid_inp = [
        ('10.2M', 10485760),
        ('100Kb', 100000),
        ('5K', 5120),
        ('2KB', 2048),
        ('65537', 65537),
        ('8b', 1),
    ]
    valid_inp.extend([
        ('10.2Mb', 10485760),
        ('100K', 100000),
        ('5Kb', 5120),
        ('2K', 2048),
        ('8B', 8),
        ('10g', 10737418240),
        ('1k', 1024),
    ])

# Generated at 2022-06-12 23:49:42.423338
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('100') == 100
    assert human_to_bytes('100g') == human_to_bytes(100, 'g')
    assert human_to_bytes('100gb') == human_to_bytes(100, 'gb')
    assert human_to_bytes('100gb', isbits=True) == human_to_bytes(100, 'gb', isbits=True)
    assert human_to_bytes('100 G') == human_to_bytes(100, 'G')
    assert human_to_bytes('10.0M') == human_to_bytes(10.0, 'M')
    assert human_to_bytes('10.0 MB') == human_to_bytes(10.0, 'MB')

# Generated at 2022-06-12 23:49:52.437467
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:56.051113
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    list_test = ['string', "STRING", "String", None, 1, dict(), dict([('a', 2)]), dict([('b', 2)])]
    list_expected = ['string', "STRING", "String", None, 1, dict(), dict([('a', 2)]), dict([('b', 2)])]
    list_test_lower = lenient_lowercase(list_test)
    assert list_test_lower == list_expected



# Generated at 2022-06-12 23:50:05.411008
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('0') == 0
    assert human_to_bytes('1') == 1
    assert human_to_bytes('100') == 100
    # decimal numbers
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes('1.6') == 2
    assert human_to_bytes('10.5') == 11
    assert human_to_bytes('10.4') == 10
    assert human_to_bytes('10.5K') == 10500
    # byte unit
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1.5B') == 1
    assert human_to_bytes('1.6B') == 2
    assert human_to_bytes('10.5B') == 11

# Generated at 2022-06-12 23:50:17.393380
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1 B') == 1
    assert human_to_bytes('1 kb') == 1024
    assert human_to_bytes('1 KB') == 1024
    assert human_to_bytes('1 Kb') == 1024
    assert human_to_bytes('1 KB', isbits=True) == 1024
    assert human_to_bytes('1 MB') == 1048576
    assert human_to_bytes('1 KB', 'M') == 0
    assert human_to_bytes('1 KB', 'm') == 0
    assert human_to_bytes('1 Kb', 'Mb') == 0
    assert human_to_bytes

# Generated at 2022-06-12 23:50:28.573257
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' to run use: python -c "import module_utils.network.iosxr.utils as utils; utils.test_human_to_bytes()" '''

# Generated at 2022-06-12 23:50:31.783827
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['abc', 7, 'deF']
    assert lenient_lowercase(test_list) == ['abc', 7, 'def']


# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:50:39.844490
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    input1 = ['Eth1/1/1', 10, None, 'Eth1/1/2']
    input2 = (1, None, 'EtH1/1/1')

    expected_output1 = ['eth1/1/1', 10, None, 'eth1/1/2']
    expected_output2 = (1, None, 'eth1/1/1')

    assert lenient_lowercase(input1) == expected_output1
    assert lenient_lowercase(input2) == expected_output2



# Generated at 2022-06-12 23:50:50.523269
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # good input.
    assert lenient_lowercase(['a', 'b']) == ['a', 'b']
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase(['One', 'Two']) == ['one', 'two']
    assert lenient_lowercase(['One', 2]) == ['one', 2]
    assert lenient_lowercase([1, 2]) == [1, 2]

    # bad input.
    try:
        lenient_lowercase(1)
    except TypeError:
        pass
    except Exception:
        assert False, 'Unexpected error raised for bad input.'

    try:
        lenient_lowercase(['a', 1])
    except TypeError:
        pass

# Generated at 2022-06-12 23:50:56.338722
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [7, 'AbCdEf', False, 'GhIjKl', 'mNopQr', None, 'stuvWX']
    expected = [7, 'abcdef', False, 'ghijkl', 'mnopqr', None, 'stuvwx']
    assert lenient_lowercase(lst) == expected



# Generated at 2022-06-12 23:50:59.094847
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    orig_list = [1, 'a', 'b', None]
    assert lenient_lowercase(orig_list) == [1, 'a', 'b', None]

# Generated at 2022-06-12 23:51:07.057521
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('100') == 100
    assert human_to_bytes('0.5') == 0
    assert human_to_bytes('0.5K') == 512
    assert human_to_bytes('0.123456789M') == 131620
    assert human_to_bytes('1.0M') == 1048576
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes(10, unit='Mb', isbits=True) == 10485760
    assert human_to_bytes('10Mb', unit='B', isbits=True) == 10485760
   

# Generated at 2022-06-12 23:51:09.864422
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ABc', 'BCD', 'cde', 123]) == ['abc', 'bcd', 'cde', 123]



# Generated at 2022-06-12 23:51:20.450309
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1B', isbits=True) == 8
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1, default_unit='B') == 1

    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1Kb', isbits=True) == 8192
    assert human_to_bytes('1KB', isbits=True) == 8192
    assert human_to_bytes('1.0KB', isbits=True)

# Generated at 2022-06-12 23:51:28.582309
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(None, isbits=False) is None
    assert human_to_bytes(None, isbits=True) is None

    assert human_to_bytes('0', isbits=False) == 0
    assert human_to_bytes('0b', isbits=False) == 0
    assert human_to_bytes('0', unit='B', isbits=False) == 0
    assert human_to_bytes('0B', unit='B', isbits=False) == 0
    assert human_to_bytes('0b', unit='b', isbits=True) == 0
    assert human_to_bytes('0b', unit='b', isbits=True) == 0
    assert human_to_bytes('0B', unit='b', isbits=True) == 0

# Generated at 2022-06-12 23:51:38.467957
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', None]) == ['a', 'b', None]
    assert lenient_lowercase(['A', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 'B', '3', None]) == ['a', 'b', '3', None]


# Generated at 2022-06-12 23:51:47.354148
# Unit test for function human_to_bytes
def test_human_to_bytes():
    test_cases = []
    test_cases.append(("10bytes", "10", 'B', 10))
    test_cases.append(("10b", "10", 'b', 10))
    test_cases.append(("10bits", "10", 'b', 10))
    test_cases.append(("10bits", "10", 'B', None))
    test_cases.append(("10bits", "10", 'b', 10))
    test_cases.append(("10B", "10", None, 10))
    test_cases.append(("10KB", "10", None, 10240))
    test_cases.append(("0.5GB", "0.5", 'B', 52428800))
    test_cases.append(("0.5MB", "0.5", 'B', 524288))


# Generated at 2022-06-12 23:51:51.476755
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['AA', 'Bb', 1, 'Cc', 3]
    assert lenient_lowercase(test_list) == ['aa', 'bb', 1, 'cc', 3]



# Generated at 2022-06-12 23:51:57.970277
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_string_item = 'ACB'
    test_string_return = 'acb'
    test_int_item = 1
    test_int_return = 1
    test_bool_item = True
    test_bool_return = True
    test_array = [test_string_item, test_int_item, test_bool_item]
    test_array_return = [test_string_return, test_int_return, test_bool_return]

    assert lenient_lowercase(test_array) == test_array_return



# Generated at 2022-06-12 23:52:03.836232
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lowercase_list = ['abc', 'DEF', 1, 2, 'ghi', 'JKL']
    lowercase_list_correct = ['abc', 'def', 1, 2, 'ghi', 'jkl']
    lowercase_list_test = lenient_lowercase(lowercase_list)
    assert lowercase_list_correct == lowercase_list_test


# Generated at 2022-06-12 23:52:09.060343
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10K') == 10240, "failed to convert string"
    assert human_to_bytes(10, 'kb') == 10240, "failed to convert number with specified unit"
    assert human_to_bytes(10024, 'kb') == 10000*1024, "failed to convert number with specified unit"
    assert human_to_bytes('3Mb', isbits=True) == 3145728, "failed to convert string"
    assert human_to_bytes(3, 'MB', isbits=True) == 3145728, "failed to convert number with specified unit"
    assert human_to_bytes(3145728, 'MB', isbits=True) == 1000000*1024*1024, "failed to convert number with specified unit"

# Generated at 2022-06-12 23:52:19.661303
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:52:28.645679
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:52:40.060501
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes(1) == 1
    assert human_to_bytes(1024) == 1024
    assert human_to_bytes(1024 * 1024) == 1024 * 1024
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1024B') == 1024
    assert human_to_bytes('1.0K') == 1024
   

# Generated at 2022-06-12 23:52:50.565798
# Unit test for function human_to_bytes
def test_human_to_bytes():
    try:
        print("Testing human_to_bytes('2K')")
        assert human_to_bytes('2K') == 2048
    except Exception as e:
        print("Exception raised: %s" % e)

    try:
        print("Testing human_to_bytes('2K', isbits=True)")
        assert human_to_bytes('2K', isbits=True) == 2048
    except Exception as e:
        print("Exception raised: %s" % e)

    try:
        print("Testing human_to_bytes('2K', isbits=False, unit='K')")
        assert human_to_bytes('2K', isbits=False, unit='K') == 2048
    except Exception as e:
        print("Exception raised: %s" % e)


# Generated at 2022-06-12 23:52:56.815987
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, "test", "TEST", "TEST1", {"test1": 1}]
    assert lenient_lowercase(lst) == [1, "test", "test", "TEST1", {"test1": 1}]

# Generated at 2022-06-12 23:52:59.333124
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['FOOBAR', 'baR']) == ['foobar', 'baR']
    assert lenient_lowercase(['FOOBAR', 2]) == ['foobar', 2]


# Generated at 2022-06-12 23:53:06.135468
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("5") == 5
    assert human_to_bytes("2k") == 2 * 1024
    assert human_to_bytes("2K") == 2 * 1024
    assert human_to_bytes("2KB") == 2 * 1024
    assert human_to_bytes("2Kb") == 2 * 1024
    assert human_to_bytes("2kb") == 2 * 1024
    assert human_to_bytes("1.2M") == 1.2 * 1024 * 1024
    assert human_to_bytes("1.2Mb") == 1.2 * 1024 * 1024
    assert human_to_bytes("15") == 15
    assert human_to_bytes("1.2") == 1.2
    assert human_to_bytes("1.2Kb") == 1.2 * 1024

# Generated at 2022-06-12 23:53:09.828784
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    result = lenient_lowercase([1, 'a', 'B', None])
    assert result == [1, 'a', 'b', None]



# Generated at 2022-06-12 23:53:20.219554
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test as function (no unit)
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2Kb', True) == 2048
    assert human_to_bytes('2M') == 2 * 1024 * 1024
    assert human_to_bytes('2Mb', True) == 2 * 1024 * 1024
    assert human_to_bytes('2G') == 2 * 1024 * 1024 * 1024
    assert human_to_bytes('2Gb', True) == 2 * 1024 * 1024 * 1024
    assert human_to_bytes('2T') == 2 * 1024 * 1024 * 1024 * 1024
    assert human_to_bytes('2Tb', True) == 2 * 1024 * 1024 * 1024 * 1024
    # Test as function (with unit)
    assert human_to_bytes(10, 'M') == 10 * 1024 * 1024


# Generated at 2022-06-12 23:53:21.997247
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2022-06-12 23:53:26.533965
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
    assert lenient_lowercase([1, "TEST", 3]) == [1, "TEST", 3]
    assert lenient_lowercase(["TEST", "TEST", "TEST"]) == ["test", "test", "test"]



# Generated at 2022-06-12 23:53:29.580105
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert(lenient_lowercase(['apple', 'banana']) == ['apple', 'banana'])
    assert(lenient_lowercase(['APPLE', 'BANANA']) == ['apple', 'banana'])
    assert(lenient_lowercase([1, 2]) == [1, 2])



# Generated at 2022-06-12 23:53:31.494686
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['Abc', 'Xyz', 1, 2, 3]) == ['abc', 'xyz', 1, 2, 3]

# Generated at 2022-06-12 23:53:42.467603
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('42') == 42
    assert human_to_bytes('42K') == 42 * 1024
    assert human_to_bytes('42k') == 42 * 1024
    assert human_to_bytes('42KB') == 42 * 1024
    assert human_to_bytes('42kb') == 42 * 1024
    assert human_to_bytes('42M') == 42 * 1024 * 1024
    assert human_to_bytes('42m') == 42 * 1024 * 1024
    assert human_to_bytes('42MB') == 42 * 1024 * 1024
    assert human_to_bytes('42mb') == 42 * 1024 * 1024
    assert human_to_bytes('42Mb', isbits=True) == 42 * 1024 * 1024
    assert human_to_bytes('42Mb') == 42 * 1024 * 1024
    assert human_to_bytes

# Generated at 2022-06-12 23:53:54.166448
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = ['this', 'is', 'A', 'Test', 1, 2, ['A'], lenient_lowercase]
    assert lenient_lowercase(test_list) == ['this', 'is', 'A', 'Test', 1, 2, ['A'], lenient_lowercase]



# Generated at 2022-06-12 23:53:58.406628
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['A', 'b']) == ['a', 'b']
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase(['A', 2]) == ['a', 2]

# Generated at 2022-06-12 23:54:08.456091
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:19.966685
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:24.670782
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase([1, 'a']) == [1, 'a']
    assert lenient_lowercase([2, 3.6]) == [2, 3.6]


# Generated at 2022-06-12 23:54:29.783709
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [1, 'test', 'Test', 'TEST', 'TESt']
    expected_list = [1, 'test', 'test', 'test', 'TESt']
    assert lenient_lowercase(test_list) == expected_list


# Generated at 2022-06-12 23:54:38.343232
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # convert in bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1B', isbits=True) == 1
    assert human_to_bytes('1.0B') == 1
    assert human_to_bytes('1.0B', isbits=True) == 1
    assert human_to_bytes('10K') == 10240
    assert human_to_bytes('10K', isbits=True) == 10240
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1M', isbits=True) == 1048576
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10M', isbits=True) == 10485760

# Generated at 2022-06-12 23:54:47.652685
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            bytes=dict(type='str', required=True),
            expected_value=dict(type='int', required=True)
        ),
        supports_check_mode=True
    )
    bytes = module.params.get('bytes')
    expected_value = module.params.get('expected_value')

# Generated at 2022-06-12 23:54:59.947144
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    values = ['foo', 'bar']
    expected = ['foo', 'bar']
    actual = lenient_lowercase(values)
    assert actual == expected

    values = ['FOO', 'BAR']
    expected = ['foo', 'bar']
    actual = lenient_lowercase(values)
    assert actual == expected

    values = ['Foo', 'Bar']
    expected = ['foo', 'bar']
    actual = lenient_lowercase(values)
    assert actual == expected

    values = ['foo', ['bar']]
    expected = ['foo', ['bar']]
    actual = lenient_lowercase(values)
    assert actual == expected

    values = ['foo', {'bar': 1}]
    expected = ['foo', {'bar': 1}]
    actual = lenient_lowercase(values)

# Generated at 2022-06-12 23:55:03.918259
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert sorted(lenient_lowercase(['a','B','C','D','',0.0,0,True,False,1])) == sorted(['a','b','c','d','',0.0,0,True,False,1])

# Generated at 2022-06-12 23:55:28.251144
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == human_to_bytes(10, 'M')
    assert human_to_bytes('1Gb') == human_to_bytes(1, 'Gb')
    assert human_to_bytes('1b') == human_to_bytes(1, 'b')
    assert human_to_bytes('1') == human_to_bytes(1, 'B')
    assert human_to_bytes('1') == human_to_bytes(1)
    assert human_to_bytes('1', 'M') == human_to_bytes(1, 'M')
    assert human_to_bytes('1', 'b') == human_to_bytes(1, 'b')
    assert human_to_bytes('1b') == human_to_bytes(1, 'b', isbits=True)

# Generated at 2022-06-12 23:55:36.246361
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    orig = ['test', 'Test', 'teST', 42, '42', '42test', 'tesT42', 'test=42', 'test42=test', 'test=42.3', 'test=42.3.1']
    expected = ['test', 'test', 'test', 42, '42', '42test', 'test42', 'test=42', 'test42=test', 'test=42.3', 'test=42.3.1']
    assert lenient_lowercase(orig) == expected, 'foo'

# Unit tests for human_to_bytes, bytes_to_human functions

# Generated at 2022-06-12 23:55:39.581656
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1.5M', default_unit='K') == (1.5 * 1024.0)
    assert human_to_bytes('.5M') == 524288



# Generated at 2022-06-12 23:55:46.162557
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from nose.tools import assert_raises, assert_equal
    assert_equal(human_to_bytes('10M'), 10485760)
    assert_equal(human_to_bytes('10K'), 10240)
    assert_equal(human_to_bytes('10B'), 10)
    assert_equal(human_to_bytes('10b', isbits=True), 10)
    assert_equal(human_to_bytes('10'), 10)
    assert_equal(human_to_bytes('10M', default_unit='B'), 10485760)  # default_unit='B'
    assert_equal(human_to_bytes('10M', default_unit='K'), 10240)
    assert_equal(human_to_bytes('10', default_unit='M'), 10485760)

# Generated at 2022-06-12 23:55:51.506778
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = [1, 'aBc', 'dEf', 2, 'GhI']
    expected = [1, 'abc', 'def', 2, 'ghi']
    assert lenient_lowercase(lst) == expected



# Generated at 2022-06-12 23:56:03.822480
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes("3.3M") == 3482624
    assert human_to_bytes("3.3Mb", isbits=True) == 3482624
    assert human_to_bytes("3.3MB") == 3482624
    assert human_to_bytes("3.3MB", unit="MB") == 3482624
    assert human_to_bytes("1024k", isbits=True) == 134217728
    assert human_to_bytes("1024kb") == 1048576
    assert human_to_bytes("1024k", unit="KB") == 1048576
    assert human_to_bytes("3.3K") == 3328
    assert human_to_bytes("3.3KB", unit="KB") == 3328
    assert human_to_bytes("3.3kb") == 3328
    assert human_

# Generated at 2022-06-12 23:56:07.844383
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 1, 'C']) == ['a', 1, 'c']
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-12 23:56:15.887237
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert(lenient_lowercase(["a", "b", "c"]) == ["a", "b", "c"])
    assert(lenient_lowercase(["a", "B", "c"]) == ["a", "b", "c"])
    assert(lenient_lowercase(["A", "B", "c"]) == ["a", "b", "c"])
    assert(lenient_lowercase(["a", "B", "C"]) == ["a", "b", "c"])
    assert(lenient_lowercase(["1", "2", "3"]) == ["1", "2", "3"])
    assert(lenient_lowercase("hello") == "hello")
    assert(lenient_lowercase("HELLO") == "hello")

# Generated at 2022-06-12 23:56:26.004729
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    import sys
    if sys.version_info >= (3, 0):
        assert lenient_lowercase(['a', 'B', 'c', 'D', 'e', 'F']) == ['a', 'b', 'c', 'd', 'e', 'f']
        assert lenient_lowercase(['a', 1, 'c', 2]) == ['a', 1, 'c', 2]
        assert lenient_lowercase([b'a', b'B', b'c', b'D', b'e', b'F']) == ['a', 'b', 'c', 'd', 'e', 'f']
    else:
        assert lenient_lowercase(['a', 'B', 'c', 'D', 'e', 'F']) == ['a', 'b', 'c', 'd', 'e', 'f']


# Generated at 2022-06-12 23:56:35.610092
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1.1F') == 0
    assert human_to_bytes('1.1T') == 0
    assert human_to_bytes('1.1P') == 0
    assert human_to_bytes('1.1E') == 0
    assert human_to_bytes('1.1Z') == 0
    assert human_to_bytes('1.1Y') == 0
    assert human_to_bytes('1.1Kb') == 0
    assert human_to_bytes('1.1Mb') == 0
    assert human_to_bytes('1.1Gb') == 0
    assert human_to_bytes('1.1Tb') == 0
    assert human_to_bytes('1.1Pb') == 0
    assert human_to_bytes('1.1Eb') == 0

# Generated at 2022-06-12 23:57:14.136431
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:21.892915
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:29.319507
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K', default_unit='B') == 2048
    assert human_to_bytes('2M', default_unit='B') == 2097152
    assert human_to_bytes('2G', default_unit='B') == 2147483648
    assert human_to_bytes('2T', default_unit='B') == 2199023255552
    assert human_to_bytes('2P', default_unit='B') == 2251799813685248
    assert human_to_bytes('2E', default_unit='B') == 2305843009213693952

    assert human_to_bytes('2k', default_unit='B') == 2048
    assert human_to_bytes('2m', default_unit='B') == 2097152

# Generated at 2022-06-12 23:57:39.554205
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=True) == 1048576 * 8
    assert human_to_bytes('1.5Mb') == 1572864
    assert human_to_bytes('.5Mb') == 524288
    assert human_to_bytes('1.5') == 1.5
    assert human_to_bytes('.5') == 0.5
    assert human_to_bytes('10.5') == 10.5
    assert human_to_bytes('0.5G') == 536870912

# Generated at 2022-06-12 23:57:42.104048
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'aBC', 'DEF']) == [1, 'abc', 'def']



# Generated at 2022-06-12 23:57:47.174154
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 134217728
    assert human_to_bytes('10MB', isbits=True) == 134217728
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes(1, 'M') == 1048576
    assert human_to_bytes(1, 'M', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=True) == 8388608



# Generated at 2022-06-12 23:57:55.158849
# Unit test for function human_to_bytes
def test_human_to_bytes():
    import pytest
    try:
        human_to_bytes('x')
        assert False
    except Exception as e:
        assert str(e) == "human_to_bytes() can't interpret following string: x"

    try:
        human_to_bytes('1 xx')
        assert False
    except Exception as e:
        assert str(e) == "human_to_bytes() can't interpret following number: xx (original input string: 1 xx)"

    try:
        human_to_bytes('1234567890')
        assert False
    except Exception as e:
        assert str(e) == "human_to_bytes() failed to convert 1234567890. The suffix must be one of Y, Z, E, P, T, G, M, K, B"


# Generated at 2022-06-12 23:57:59.348153
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']
    assert lenient_lowercase(['A', [1, 2, 3]]) == ['a', [1, 2, 3]]

# Generated at 2022-06-12 23:58:08.327687
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['This', 'is', 'a', 'list']) == ['this', 'is', 'a', 'list']
    assert lenient_lowercase([[0, 1], 'list']) == [[0, 1], 'list']
    assert lenient_lowercase([[0, 1], [2, 3]]) == [[0, 1], [2, 3]]
    assert lenient_lowercase([]) == []
    assert lenient_lowercase(['asd', 'asd', 'asd']) == ['asd', 'asd', 'asd']


# Generated at 2022-06-12 23:58:12.613724
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    l = ['A', 3, {'A': 1, 'b': 2}]
    assert lenient_lowercase(l) == ['a', 3, {'A': 1, 'b': 2}]


if __name__ == '__main__':
    test_lenient_lowercase()