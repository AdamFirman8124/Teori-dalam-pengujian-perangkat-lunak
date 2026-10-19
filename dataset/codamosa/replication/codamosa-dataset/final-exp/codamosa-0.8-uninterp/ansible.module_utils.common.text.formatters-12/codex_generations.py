

# Generated at 2022-06-12 23:48:53.640410
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['1fk', 'd', '12']) == ['1fk', 'd', '12']
    assert lenient_lowercase(['1fk', 'D', '12']) == ['1fk', 'd', '12']
    assert lenient_lowercase(['1FK', 'd', '12']) == ['1fk', 'd', '12']


# Generated at 2022-06-12 23:49:02.774706
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 3, 'c']) == ['a', 3, 'c']
    assert lenient_lowercase([3, 'b', 'c']) == [3, 'b', 'c']
    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']
    assert lenient_lowercase(['A', 3, 'C']) == ['a', 3, 'c']
    assert lenient_lowercase([3, 'B', 'C']) == [3, 'b', 'c']

# Generated at 2022-06-12 23:49:11.291246
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print('Testing human_to_bytes function...')
    assert human_to_bytes(1) == 1, 'Error in function human_to_bytes.'
    assert human_to_bytes(1.1) == 1, 'Error in function human_to_bytes.'
    assert human_to_bytes(1.9) == 1, 'Error in function human_to_bytes.'
    assert human_to_bytes('1') == 1, 'Error in function human_to_bytes.'
    assert human_to_bytes('1.1') == 1, 'Error in function human_to_bytes.'
    assert human_to_bytes('1.9') == 1, 'Error in function human_to_bytes.'

    assert human_to_bytes('1K') == 1024, 'Error in function human_to_bytes.'

# Generated at 2022-06-12 23:49:20.526660
# Unit test for function human_to_bytes
def test_human_to_bytes():
    print("**** Starting unit test for function human_to_bytes ****")

    bytes_10 = human_to_bytes("10")
    assert bytes_10 == 10, "Expect human_to_bytes to return 10 bytes, found: %s" % bytes_10

    megabits_1 = human_to_bytes("1Mb", default_unit=None, isbits=True)
    assert megabits_1 == 1048576, "Expect human_to_bytes to return 1048576 bytes, found: %s" % megabits_1
    megabits_1_0 = human_to_bytes("1.0Mb", default_unit=None, isbits=True)
    assert megabits_1_0 == 1048576, "Expect human_to_bytes to return 1048576 bytes, found: %s" % meg

# Generated at 2022-06-12 23:49:22.555188
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase([1, 'FIRST', 'SecONd', 3]) == [1, 'first', 'second', 3]


# Generated at 2022-06-12 23:49:33.160948
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:49:43.806718
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1B', default_unit='B') == 1
    assert human_to_bytes('1B', default_unit='K') == 1024
    assert human_to_bytes('1B', default_unit='M') == 1048576
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 1048576

# Generated at 2022-06-12 23:49:50.148003
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    list1 = ['TEST', 'TEST', 1, 2, 3, '123', 'test', [], {}, None]
    list2 = ['test', 'test', 1, 2, 3, '123', 'test', [], {}, None]

    lc_list1 = lenient_lowercase(list1)
    lc_list2 = lenient_lowercase(list2)

    assert list1 == lc_list1
    assert list2 == lc_list2

# Generated at 2022-06-12 23:49:58.692658
# Unit test for function human_to_bytes
def test_human_to_bytes():
    result = human_to_bytes('1B')
    assert int(result) == 1, "Expected 1, got {0}".format(result)
    result = human_to_bytes('1K')
    assert int(result) == 1024, "Expected 1024, got {0}".format(result)
    result = human_to_bytes('1M')
    assert int(result) == 1048576, "Expected 1048576, got {0}".format(result)
    result = human_to_bytes('1G')
    assert int(result) == 1073741824, "Expected 1073741824, got {0}".format(result)
    result = human_to_bytes('1T')
    assert int(result) == 1099511627776, "Expected 1099511627776, got {0}".format

# Generated at 2022-06-12 23:50:00.564831
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c', 'd', 1, 2, 3, 4]) == ['a', 'b', 'c', 'd', 1, 2, 3, 4]


# Generated at 2022-06-12 23:50:15.144552
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10M', isbits=True) == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760

    assert human_to_bytes('10M', unit='M') == 10485760

    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('10Mb') == 1048576

    assert human_to_bytes('1.5Mb') == 1572864

# Generated at 2022-06-12 23:50:21.728219
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 1, 'b', 2]) == ['a', 1, 'b', 2]
    assert lenient_lowercase(['A', 'B', 'C', 'D']) == ['a', 'b', 'c', 'd']
    assert lenient_lowercase([1, 2, 3, 4]) == [1, 2, 3, 4]

# Generated at 2022-06-12 23:50:30.267706
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:50:37.271273
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b']) == ['a', 'b']
    assert lenient_lowercase([1, 2]) == [1, 2]
    assert lenient_lowercase(['a', 1]) == ['a', 1]
    assert lenient_lowercase(['A', 1]) == ['a', 1]
    assert lenient_lowercase(['A', 'B']) == ['a', 'b']


# Generated at 2022-06-12 23:50:42.954829
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1mB', isbits=True) == 1048576
    assert human_to_bytes('1mb', isbits=True) == 1048576
    assert human_to_bytes('1MB', isbits=True) == 8388608
    assert human_to_bytes('1Mb', isbits=False) == 1048576
    assert human_to_bytes('1mB', isbits=False) == 1048576
    assert human_to_bytes('1mb', isbits=False) == 1048576

# Generated at 2022-06-12 23:50:51.095227
# Unit test for function human_to_bytes
def test_human_to_bytes():

    assert human_to_bytes('10.5M') == int(round(10.5 * SIZE_RANGES['M']))
    assert human_to_bytes('10Mb') == int(round(10 * SIZE_RANGES['M']))
    assert human_to_bytes('10b') == 10
    assert human_to_bytes(10, 'M') == int(round(10 * SIZE_RANGES['M']))
    assert human_to_bytes(10, 'M', isbits=True) == int(round(10 * SIZE_RANGES['M']))
    assert human_to_bytes(10, unit='M', isbits=True) == int(round(10 * SIZE_RANGES['M']))


# Generated at 2022-06-12 23:50:54.423992
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['a', 'B', 'c', 1]
    assert lenient_lowercase(lst) == ['a', 'b', 'c', 1]



# Generated at 2022-06-12 23:51:03.861136
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert isinstance(human_to_bytes('0'), int)
    assert human_to_bytes('0') == 0
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('10b') == 1
    assert human_to_bytes('10b', isbits=True) == 10
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1kb') == 1024
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1MiB') == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 1048576

# Generated at 2022-06-12 23:51:06.060646
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['B', 'c', 'CD']) == ['b', 'c', 'cd']
    assert lenient_lowercase([1]) == [1]



# Generated at 2022-06-12 23:51:17.616251
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2KiB') == 2048
    assert human_to_bytes('2kb') == 2048
    assert human_to_bytes('2k') == 2048

    assert human_to_bytes('2M', 'Kb') == 2097152
    assert human_to_bytes('2Mb', 'Kb') == 2097152
    assert human_to_bytes('2mb', 'Kb') == 2097152
    assert human_to_bytes('2m', 'Kb') == 2097152

    assert human_to_bytes('2k', 'Kb') == 2048
    assert human_to_bytes('2kb', 'Kb') == 2048
    assert human_to_bytes('2Kb', 'Kb') == 2048
    assert human_to

# Generated at 2022-06-12 23:51:23.407234
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 1, 'CD']) == ['a', 'b', 1, 'CD']
    assert lenient_lowercase(['a', 'b', 1, 'CD', u'a']) == ['a', 'b', 1, 'CD', u'a']



# Generated at 2022-06-12 23:51:26.429832
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [1, 'tEsT', 3.0, 'tEsT2']
    test_list_lower = [1, 'test', 3.0, 'test2']
    assert lenient_lowercase(test_list) == test_list_lower



# Generated at 2022-06-12 23:51:34.963565
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test bytes
    assert human_to_bytes('10.24M') == 10 * 1024 * 1024
    assert human_to_bytes(10.24, 'M') == 10 * 1024 * 1024
    assert human_to_bytes(10.24, 'M', isbits=True) == 10 * 1024 * 1024
    assert human_to_bytes('10M') == 10 * 1024 * 1024
    assert human_to_bytes('10.24MB') == 10 * 1024 * 1024
    assert human_to_bytes(10.24, 'MB') == 10 * 1024 * 1024
    assert human_to_bytes(10.24, 'MB', isbits=True) == 10 * 1024 * 1024
    assert human_to_bytes('10MB') == 10 * 1024 * 1024

    assert human_to_bytes('10.24K') == 10 * 1024

# Generated at 2022-06-12 23:51:44.565629
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['a', 'b', 'c', 'D', 3]) == ['a', 'b', 'c', 'D', 3]
    assert lenient_lowercase([u'a', u'b', u'c', u'D', 3]) == ['a', 'b', 'c', 'D', 3]

# Generated at 2022-06-12 23:51:54.856901
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.') == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.5') == 1
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1Kb') == 1024
    assert human_to_bytes('1Mb') == 1048576
    assert human_to_bytes('1g') == 1073741824
    assert human_to_bytes('1y') == 1208925819614629174706176
    assert human_to_bytes('1z') == 1180591620717411303424


# Generated at 2022-06-12 23:52:01.945776
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())


# Generated at 2022-06-12 23:52:13.317810
# Unit test for function human_to_bytes
def test_human_to_bytes():

    print('Unit test for function human_to_bytes')

    # All values must be lower for testing

# Generated at 2022-06-12 23:52:23.769387
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:52:31.438309
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:52:40.062839
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1Mb') == 131072
    assert human_to_bytes('1Mb', default_unit='b') == 131072
    assert human_to_bytes('1', default_unit='MB') == 1048576
    assert human_to_bytes('1') == 1


# Generated at 2022-06-12 23:52:53.200857
# Unit test for function human_to_bytes
def test_human_to_bytes():
    """Unit test for human_to_bytes"""
    from ansible.module_utils.six import assertCountEqual


# Generated at 2022-06-12 23:52:56.123362
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['ABc', 'deF', 123, [1, 2, 3]]) == ['abc', 'def', 123, [1, 2, 3]]
    return True


# Generated at 2022-06-12 23:53:02.783182
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    def lc(to_lower):
        return lenient_lowercase(to_lower)

    assert lc(['FoO', 1, {'bAr': 'bAz'}, ['Baz'], ('ABC', 'cde')]) == ['foo', 1, {'bAr': 'bAz'}, ['Baz'], ('ABC', 'cde')]

    to_lower = ['FoO', 1, {'bAr': 'bAz'}, ['Baz'], ('ABC', 'cde')]

    assert lc(to_lower) == ['foo', 1, {'bAr': 'bAz'}, ['Baz'], ('ABC', 'cde')]
    assert to_lower == ['foo', 1, {'bAr': 'bAz'}, ['Baz'], ('ABC', 'cde')]

   

# Generated at 2022-06-12 23:53:10.734936
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['teSt', '00', '0x0f', 'hello', 'world']) == ['test', '00', '0x0f', 'hello', 'world']
    assert lenient_lowercase(['teSt', '00', '0x0f', 'hello', 'world', 1, 2]) == ['test', '00', '0x0f', 'hello', 'world', 1, 2]
    assert lenient_lowercase(['tEst', 1, 2, 3]) == ['test', 1, 2, 3]


# Generated at 2022-06-12 23:53:20.843461
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('10b') == 10
    assert human_to_bytes('10B', isbits=True) == 10
    assert human_to_bytes('10b', isbits=True) == 10
    assert human_to_bytes('10Tb') == 10*(2**40)
    assert human_to_bytes('10Tb', isbits=True) == 10*(2**40)
    assert human_to_bytes('10Gb') == 10*(2**30)
    assert human_to_bytes('10Gb', isbits=True) == 10*(2**30)
    assert human_to_bytes('10Mb') == 10*(2**20)

# Generated at 2022-06-12 23:53:25.744846
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    from ansible.module_utils._text import to_text

    test_input = ['FOO', 'Bar', 'baz', '', 1]
    expected_output = ['foo', 'bar', 'baz', '', 1]
    result = lenient_lowercase(test_input)
    assert isinstance(result, list)
    assert result == expected_output



# Generated at 2022-06-12 23:53:32.441754
# Unit test for function human_to_bytes
def test_human_to_bytes():
    test_input = [
        ('1', 1), ('10', 10), ('10M', 10485760), ('1GB', 1073741824), ('1TB', 1099511627776), ('1PB', 1125899906842624.0),
        # testing default unit
        ('10', 10, None), ('10M', 10485760, None), ('1GB', 1073741824, None),
        # testing bits
        ('10b', 1, 'b'), ('1kb', 1024, 'b'), ('1Mb', 1048576, 'b'), ('1Gb', 1073741824, 'b'),
        # testing bytes
        ('10', 10, 'b'), ('1k', 1024, 'b'), ('1M', 1048576, 'b'), ('1G', 1073741824, 'b'),
    ]

# Generated at 2022-06-12 23:53:43.253235
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1b') == 1
    assert human_to_bytes('1.0B') == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('20000B') == 20000
    assert human_to_bytes('1.21E+6B') == 1210000
    assert human_to_bytes('100K') == 102400
    assert human_to_bytes('100KB') == 102400
    assert human_to_bytes('100.0K') == 102400
    assert human_to_bytes('100.0KB') == 102400
    assert human_to_bytes('1.0MB') == 1048576

# Generated at 2022-06-12 23:53:50.883907
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:53:59.468034
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # basic tests
    assert lenient_lowercase(['a', 'B', 'c']) == ['a', 'b', 'c']
    assert lenient_lowercase(['a', 1, 'c']) == ['a', 1, 'c']

    # avoiding potential recursion problems
    class TestClass:
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return 'TestClass(%s)' % self.value
    a = TestClass('A')
    b = TestClass('b')
    assert lenient_lowercase([a, b]) == [a, b]


# Generated at 2022-06-12 23:54:09.808676
# Unit test for function human_to_bytes
def test_human_to_bytes():
    try:
        assert human_to_bytes('10M') == 10485760
        assert human_to_bytes('1G') == 1073741824
        assert human_to_bytes('1B') == 1
        assert human_to_bytes('1Mb') == 131072
        assert human_to_bytes('1Mb', isbits=True) == 131072
        assert human_to_bytes('5B', default_unit='Mb') == 524288
        assert human_to_bytes('5') == 5
        assert human_to_bytes('5', default_unit='Mb') == 524288
    except ValueError:
        assert False, "human_to_bytes failed for test parameters"



# Generated at 2022-06-12 23:54:21.387432
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:54:32.431088
# Unit test for function human_to_bytes
def test_human_to_bytes():
    tests = dict(
        tiny='1B',
        K='2K',
        KB='2KB',
        M='3M',
        Mb='8Mb',  # can't have uppercase 'b'
        G='10G',
        bytes='1',  # with no suffix
        garbage='1234 garbage',  # with invalid chars
        decimal_K='1.5K',
        decimal_G='1.5G',
        decimal_dot='1.5',  # with no suffix
        decimal_no_zero='1.5G',
        decimal_zero='1.50',  # decimal with a zero at the end
    )


# Generated at 2022-06-12 23:54:34.992271
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['A', 'b', 'C', 1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]

# Generated at 2022-06-12 23:54:45.969171
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('0.1M') == 104857.6
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760.0
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'Mb', isbits=True) == 10485760.0
    assert human_to_bytes(10.5, 'M') == 10485760
    assert human_to_bytes(10.5, 'Mb', isbits=True) == 10485760
    assert human_to_bytes(10.5, 'M', isbits=True) == 1048576

# Generated at 2022-06-12 23:54:59.027100
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert 1 == human_to_bytes('1b', isbits=True)
    assert 8 == human_to_bytes('1b', isbits=False)
    assert 8 == human_to_bytes('8b', isbits=False)
    assert 8 == human_to_bytes('8B', isbits=False)
    assert 8 == human_to_bytes('8', isbits=False)
    assert 8 == human_to_bytes('8', 'b', isbits=False)
    assert 8 == human_to_bytes('8', 'B', isbits=False)
    assert 8 == human_to_bytes('8', 'B', isbits=True)
    assert 8 == human_to_bytes('8', 'b', isbits=True)
    assert 1048576 == human_to_bytes('1m', isbits=False)


# Generated at 2022-06-12 23:55:03.471774
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['1', '2', '3']) == ['1', '2', '3']
    assert lenient_lowercase(['1', '2', '3', 'ABCDE']) == ['1', '2', '3', 'ABCDE']



# Generated at 2022-06-12 23:55:11.707569
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    # Test if lenient_lowercase convert a list of mixed str and int properly
    lst = [1, 2, 3, "A", "B", "C"]
    assert lenient_lowercase(lst) == [1, 2, 3, "a", "b", "c"]
    # Test if lenient_lowercase convert a list of mixed str and dict properly
    lst = [1, 2, 3, {"A": "B"}, {"B": "C"}, {"D": "E"}]
    assert lenient_lowercase(lst) == [1, 2, 3, {"A": "B"}, {"B": "C"}, {"D": "E"}]
    # Test if lenient_lowercase convert a list of mixed str and list properly

# Generated at 2022-06-12 23:55:16.644300
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert(lenient_lowercase(['A', 'B']) == ['a', 'b'])
    assert(lenient_lowercase(['A', 1]) == ['a', 1])
    assert(lenient_lowercase([]) == [])


# Generated at 2022-06-12 23:55:28.103683
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Tests different value types
    assert human_to_bytes('1') == 1
    assert human_to_bytes(1) == 1

    # Tests different sizes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1KB') == 1024
    assert human_to_bytes('1MB') == 1048576
    assert human_to_bytes('1GB') == 1073741824
    assert human_to_bytes('1TB') == 1099511627776
    assert human_to_bytes('1PB') == 1125899906842624
    assert human_to_bytes('1EB') == 1152921504606846976
    assert human_to_bytes('1ZB') == 1.1805916207174113e+21
    assert human_to_bytes('1YB') == 1.

# Generated at 2022-06-12 23:55:40.311540
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10GB') == 10737418240
    assert human_to_bytes('10.1M') == 10485760
    assert human_to_bytes('.1M') == 102400
    assert human_to_bytes('10M', 'GB') == 10485760

    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes('1.1Mb', isbits=True) == 11534336

    try:
        human_to_bytes('1.1Mb')  # must fail (isbits=False)
        raise AssertionError('human_to_bytes() did not raise ValueError when expected')
    except ValueError:
        pass


# Generated at 2022-06-12 23:55:43.343928
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_list = [1, 'Hello, World!', 2]
    test_list_lower = ['1', 'hello, world!', '2']
    assert lenient_lowercase(test_list) == test_list_lower

# Unit tests for function human_to_bytes

# Generated at 2022-06-12 23:55:51.017528
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # Test valid input
    assert human_to_bytes('2048') == 2048
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1.5M') == 1572864
    assert human_to_bytes('1.5Mb', isbits=True) == 16252928
    assert human_to_bytes('5Gb', isbits=True) == 549560832
    assert human_to_bytes('5G') == 5368709120
    assert human_to_bytes('1.5Gb', isbits=True) == 16252928
    assert human_to_bytes('1.5T') == 1649267441664
    assert human_to_bytes('1.5t') == 1649267441664
   

# Generated at 2022-06-12 23:56:02.597635
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('0') == 0
    assert human_to_bytes('11') == 11
    assert human_to_bytes('11b') == 11
    assert human_to_bytes('11b', isbits=True) == 11
    assert human_to_bytes('11Gb') == 11 * (1 << 30)
    assert human_to_bytes('11GB') == 11 * (1 << 30)
    assert human_to_bytes('11 Gb', isbits=True) == 11 * (1 << 30)
    assert human_to_bytes('11Mb') == 11 * (1 << 20)
    assert human_to_bytes('11Mb', isbits=True) == 11 * (1 << 20)
    assert human_to_bytes('11Kb') == 11 * (1 << 10)
    assert human_to_

# Generated at 2022-06-12 23:56:07.360650
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    lst = ['A', 'b', ['c'], {'d': 'e'}]
    lst_result = ['a', 'b', ['c'], {'d': 'e'}]
    assert lenient_lowercase(lst) == lst_result


# Generated at 2022-06-12 23:56:15.617611
# Unit test for function human_to_bytes
def test_human_to_bytes():

    ''' bytes tests with uppercase byte identifier '''
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1024B') == 1024
    assert human_to_bytes('1.23MB') == int(1.23 * 1024 * 1024)
    assert human_to_bytes('10B') == 10
    assert human_to_bytes('55b') == 55
    assert human_to_bytes('55') == 55
    assert human_to_bytes('55.2') == 55
    assert human_to_bytes('55.6B') == 56

    ''' bits tests with lowercase bit identifier '''
    assert human_to_bytes('1b', isbits=True) == 1
    assert human_to_bytes('1024b', isbits=True) == 1024

# Generated at 2022-06-12 23:56:25.827710
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1024 * 1024
    assert human_to_bytes('1MB') == 1024 * 1024
    assert human_to_bytes('1Mb', isbits=True) == 1024 * 1024
    assert human_to_bytes('1MBb', isbits=True) == 1024 * 1024
    assert human_to_bytes('1.5', default_unit='KB') == 1536
    assert human_to_bytes('1.5KB') == 1536
    assert human_to_bytes('1.5KBb', isbits=True) == 1536 * 8
    assert human_to_bytes('1.5Kb') == 1536 * 8
    assert human_to_bytes('5K', unit='b') == 5 * 8192
    assert human_

# Generated at 2022-06-12 23:56:28.722057
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    assert lenient_lowercase(['uPPeR', 'lOwEr', 1, 2, 3]) == ['upper', 'lower', 1, 2, 3]



# Generated at 2022-06-12 23:56:39.156730
# Unit test for function human_to_bytes
def test_human_to_bytes():
    # test bytes
    assert human_to_bytes("2") == 2
    assert human_to_bytes("2K") == 2 * 1024
    assert human_to_bytes("2.5M") == int(2.5 * 1024 * 1024)
    assert human_to_bytes("2.5MB") == int(2.5 * 1024 * 1024)
    assert human_to_bytes("2.5MiB") == int((2.5 * 1024 * 1024) / 1024)
    assert human_to_bytes("2.5Mib") == int(2.5 * 1024 * 1024) / 8
    assert human_to_bytes("2.5 Gib") == int(2.5 * 1024 * 1024 * 1024 / 8)

# Generated at 2022-06-12 23:56:48.017671
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('10') == 10
    assert human_to_bytes('10M') == 10 * 1024 * 1024
    assert human_to_bytes('10m') == 10 * 1024 * 1024
    assert human_to_bytes('10mB') == 10 * 1024 * 1024
    assert human_to_bytes('10mb') == 10 * 1024 * 1024
    assert human_to_bytes('10MB') == 10 * 1024 * 1024
    assert human_to_bytes('10mb', True) == 10 * 1024 * 1024
    assert human_to_bytes('10Mb', True) == 10 * 1024 * 1024
    assert human_to_bytes('10.5M') == 10.5 * 1024 * 1024



# Generated at 2022-06-12 23:57:03.632810
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    test_cases = [
        (['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']),
        (['a', 1, 'b', 'c', 2, 'd'], ['a', 1, 'b', 'c', 2, 'd']),
        (['a', 'b', 'C', 'd'], ['a', 'b', 'c', 'd']),
        (['a', 'B', 'c', 'd'], ['a', 'b', 'c', 'd']),
    ]
    for test_case in test_cases:
        assert lenient_lowercase(test_case[0]) == test_case[1]



# Generated at 2022-06-12 23:57:08.349289
# Unit test for function lenient_lowercase
def test_lenient_lowercase():
    own_list = ['A', 'B', 'C', 'D', 1, 2, 3, 4]
    own_result = ['a', 'b', 'c', 'd', 1, 2, 3, 4]
    assert own_result == lenient_lowercase(own_list)

# Generated at 2022-06-12 23:57:17.942536
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('2K') == 2 * 1 << 10
    assert human_to_bytes('2B', default_unit='K') == 2 * 1 << 10
    assert human_to_bytes('2.0K') == 2 * 1 << 10
    assert human_to_bytes('2.5K') == 2.5 * 1 << 10
    assert human_to_bytes('2.5') == 2.5 * 1
    assert human_to_bytes('2.5B', default_unit='MB') == 2.5 * 1 << 20
    assert human_to_bytes('2.5Tb', isbits=True) == 2.5 * 1 << 40
    assert human_to_bytes('2.5Mb', isbits=True) == 2.5 * 1 << 20

# Generated at 2022-06-12 23:57:24.869732
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:31.210882
# Unit test for function human_to_bytes

# Generated at 2022-06-12 23:57:40.805104
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert 10 == human_to_bytes('10b', isbits=True)
    assert 1048576 == human_to_bytes('1Mb', isbits=True)
    assert 1048576 == human_to_bytes('1MB', isbits=False)

    assert 10 == human_to_bytes('10b', default_unit='b', isbits=True)
    assert 1048576 == human_to_bytes('1', default_unit='mb', isbits=True)
    assert 1048576 == human_to_bytes('1', default_unit='MB', isbits=False)

    assert 3 == human_to_bytes('3', default_unit='b', isbits=True)
    assert 2048 == human_to_bytes('2K', default_unit='b', isbits=True)
    assert 2097152 == human_to_bytes

# Generated at 2022-06-12 23:57:45.865931
# Unit test for function human_to_bytes
def test_human_to_bytes():
    error_msg = "something went wrong with human_to_bytes() conversion"

    # Check for bytes
    try :
        assert(human_to_bytes("10Bytes") == 10), error_msg
        assert(human_to_bytes("10B") == 10), error_msg
        assert(human_to_bytes("10B", default_unit="B") == 10), error_msg
        assert(human_to_bytes("10", default_unit="B") == 10), error_msg
    except Exception:
        raise AssertionError("Wrong behaviour with Bytes")

    # Check for Kilobytes

# Generated at 2022-06-12 23:57:54.158050
# Unit test for function human_to_bytes
def test_human_to_bytes():
    from pytest import raises
    from ansible.module_utils.network.common import to_list

    assert human_to_bytes('0') == 0
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('1.9') == 1
    assert human_to_bytes('2') == 2

    assert human_to_bytes('2B') == 2
    assert human_to_bytes('3kb') == 3072
    assert human_to_bytes('3mb') == 3145728
    assert human_to_bytes('3GB') == 3221225472

    assert human_to_bytes('31744M') == 33444880384

# Generated at 2022-06-12 23:58:07.137064
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert human_to_bytes('0') == 0
    assert human_to_bytes('1') == 1
    assert human_to_bytes('1.0') == 1
    assert human_to_bytes('1.1') == 1
    assert human_to_bytes('0.9') == 0
    assert human_to_bytes('1.1K') == 1024
    assert human_to_bytes('1.9K') == 2048
    assert human_to_bytes('.9K') == 1024
    assert human_to_bytes('10M') == 10485760
    assert human_to_bytes('10Mb') == 10485760
    assert human_to_bytes('10Mb', isbits=True) == 10485760
    assert human_to_bytes(10, 'M') == 10485760
    assert human_

# Generated at 2022-06-12 23:58:18.169334
# Unit test for function human_to_bytes
def test_human_to_bytes():
    assert 2097152 == human_to_bytes('2M')
    assert 2 == human_to_bytes('2')
    assert 8 == human_to_bytes('8   ')
    assert 1048576 == human_to_bytes('1MB')
    assert 1048576 == human_to_bytes('1MB ')
    assert 1048576 == human_to_bytes('1 MB')
    assert 1048576 == human_to_bytes(' 1MB ')
    assert 1048576 == human_to_bytes(' 1 MB ')
    assert 2097152 == human_to_bytes('2M  ')
    assert 8388608 == human_to_bytes('8MB')
    assert 42 * 1024 * 1024 * 1024 == human_to_bytes('42GB')

# Generated at 2022-06-12 23:58:36.108333
# Unit test for function human_to_bytes
def test_human_to_bytes():
    ''' Test conversion from human to bytes '''
    assert(human_to_bytes('10') == 10)
    assert(human_to_bytes('10.1') == 10)
    assert(human_to_bytes('-10.1') == -10)

    assert(human_to_bytes('10k') == 10240)
    assert(human_to_bytes('10K') == 10240)
    assert(human_to_bytes('10.1k') == 10240)
    assert(human_to_bytes('-10.1k') == -10240)

    assert(human_to_bytes('10m') == 10485760)
    assert(human_to_bytes('10M') == 10485760)
    assert(human_to_bytes('10.1m') == 10485760)