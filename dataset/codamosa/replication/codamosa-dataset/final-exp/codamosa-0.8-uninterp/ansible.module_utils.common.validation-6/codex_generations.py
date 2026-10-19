

# Generated at 2022-06-12 23:49:29.833027
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('10K') == 10240
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('2G') == 2147483648
    assert check_type_bytes('3T') == 3.4E+12
    assert check_type_bytes(2014) == 2014
    assert_raises(TypeError, check_type_bytes, '10k')
    assert_raises(TypeError, check_type_bytes, '100kk')
    assert_raises(TypeError, check_type_bytes, '')



# Generated at 2022-06-12 23:49:36.996867
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """Unit test for the check_type_bytes function"""
    # pylint: disable=import-error
    from ansible.module_utils import psrp_common

    # Ensure a numeric value works correctly
    numeric_value = 1024
    assert numeric_value == psrp_common.check_type_bytes(numeric_value)

    # Ensure 'k' works correctly, as well as the lowercase and uppercase versions
    k_value = "1024k"
    assert 262144 == psrp_common.check_type_bytes(k_value)
    assert 262144 == psrp_common.check_type_bytes(k_value.upper())

    # Ensure 'm' works correctly, as well as the lowercase and uppercase versions
    m_value = "1m"
    assert 1048576 == psrp_

# Generated at 2022-06-12 23:49:41.682050
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float("0.1") == 0.1
    assert check_type_float("-0.1") == -0.1
    assert check_type_float("-0") == 0.0
    assert check_type_float("0") == 0.0

    with pytest.raises(TypeError):
        check_type_float(object())


# Generated at 2022-06-12 23:49:51.672741
# Unit test for function safe_eval
def test_safe_eval():
    data = {
        "key": "value"
    }
    for key in data:
        assert safe_eval(data[key]) == data[key]
    assert safe_eval("{'key': 'value'}") == {'key': 'value'}
    assert safe_eval('[1, 2, 3, 4]') == [1, 2, 3, 4]
    assert safe_eval("{'key':'value'}.get('key')") == 'value'
    assert safe_eval("{'key':'value'}.keys()") == ['key']
    assert safe_eval("{'key':'value'}.values()") == ['value']
    assert safe_eval("int(42)") == 42
    assert safe_eval("bool('False')") == True
    assert safe_eval("42 == 42") == True

# Generated at 2022-06-12 23:49:54.680330
# Unit test for function check_type_int
def test_check_type_int():
    try:
        assert check_type_int(3) == 3
        assert check_type_int("3") == 3
        assert check_type_int("a")
    except Exception as e:
        print(e)


# Generated at 2022-06-12 23:49:58.489326
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1048576') == 1048576


# Generated at 2022-06-12 23:50:07.024380
# Unit test for function check_required_by
def test_check_required_by():
    # should not raise exception
    for parameters in [
        {'my_param': 1, 'other_param': 1},
        {'my_param': 1},
        {},
    ]:
        check_required_by({'my_param': ['other_param']}, parameters)

    # should raise exception
    for parameters in [
        {'my_param': 1, 'other_param': None},
        {'my_param': 1, 'other_param': 1, 'third_param': None},
        {'my_param': 1, 'third_param': None},
    ]:
        try:
            check_required_by({'my_param': ['other_param']}, parameters)
        except TypeError:
            # Correct behavior
            pass

# Generated at 2022-06-12 23:50:18.116908
# Unit test for function check_type_bytes
def test_check_type_bytes():
    from ansible.module_utils.common._collections_compat import Mapping


# Generated at 2022-06-12 23:50:27.367264
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(7) == 7
    try:
        check_type_int('7')
    except TypeError:
        assert False, '%r should not raise a TypeError' % '7'
    try:
        check_type_int('7.0')
    except TypeError:
        assert False, '%r should not raise a TypeError' % '7.0'
    try:
        check_type_int('7.1')
    except TypeError:
        assert True
    try:
        check_type_int(7.0)
    except TypeError:
        assert True
    try:
        check_type_int(7.1)
    except TypeError:
        assert True



# Generated at 2022-06-12 23:50:39.687195
# Unit test for function check_required_if
def test_check_required_if():
    # Test when at least one requirement should be present
    requirements=[
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    # Test with success when at least one requirement should be present
    parameters={
        'state': 'present',
        'path': '/',
    }
    results = check_required_if(requirements, parameters)
    assert results == []
    # Test with success when at least one requirement should be present
    parameters={
        'state': 'present',
        'path': '',
    }
    results = check_required_if(requirements, parameters)
    assert results == []
    # Test with failure when at least one requirement should be present

# Generated at 2022-06-12 23:50:50.807841
# Unit test for function check_required_one_of
def test_check_required_one_of():
    parameters = {'operation': 'present'}
    try:
        check_required_one_of([('p1', 'p2'), ('p3', 'p4')], parameters)
        return True
    except:
        return False



# Generated at 2022-06-12 23:51:00.530263
# Unit test for function check_required_arguments
def test_check_required_arguments():
    bad_spec = dict(
        parameter1=dict(),
        parameter2=dict(required=True)
    )

    good_spec = dict(
        parameter1=dict(),
        parameter2=dict(required=True)
    )

    parameters = dict(
        parameter2='test'
    )

    try:
        check_required_arguments(bad_spec, parameters)
        assert False, "bad_spec should fail because parameter1 is not required and not specified"
    except TypeError:
        pass

    try:
        check_required_arguments(good_spec, parameters)
    except TypeError:
        assert False, "good_spec should not fail because all required parameters are specified"



# Generated at 2022-06-12 23:51:07.087633
# Unit test for function check_required_by
def test_check_required_by():
    assert {} == check_required_by({"key": ["value"]}, {"key": "foo"})
    try:
        check_required_by({"key": ["value"]}, {"key2": "bar"})
    except TypeError as e:
        assert "missing parameter(s) required by 'key'" in to_native(e)
    assert {} == check_required_by({"key": "value"}, {"key": "foo"})
    try:
        check_required_by({"key": "value"}, {"key2": "bar"})
    except TypeError as e:
        assert "missing parameter(s) required by 'key'" in to_native(e)



# Generated at 2022-06-12 23:51:12.523207
# Unit test for function check_required_if
def test_check_required_if():
    assert check_required_if(
        None,
        None,
    ) == []
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    assert check_required_if(
        requirements,
        {},
    ) == requirements
    assert check_required_if(
        requirements,
        {'state': 'present'},
    ) == [
        {
            'missing': ['path'],
            'requires': 'any',
            'parameter': 'state',
            'value': 'present',
            'requirements': ('path',),
        }
    ]



# Generated at 2022-06-12 23:51:19.958188
# Unit test for function check_type_bytes
def test_check_type_bytes():
    '''Unit test for function check_type_bytes'''
    assert check_type_bytes('1G') == 1073741824
    expected = '%s cannot be converted to a Byte value' % type(1)
    actual = None
    try:
        check_type_bytes(1)
    except TypeError as e:
        actual = str(e)
    assert expected == actual
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Generated at 2022-06-12 23:51:28.266214
# Unit test for function check_type_dict
def test_check_type_dict():
    input_values = ["{ 'a' : 1 }", "a=1, b=2, c=3", "a=1, b='2', c=3", 'a==1, b=2, c=3', 'a=1, b=2, c=3\\n', 'a=1, b=2, c=3"']
    output_values = [{'a': 1}, {'a': '1', 'b': '2', 'c': '3'}, {'a': '1', 'b': '2', 'c': '3'},
                     {'a': '=1', 'b': '2', 'c': '3'}, {'a': '1', 'b': '2', 'c': '3'}, {'a': '1', 'b': '2', 'c': '3'}]

# Generated at 2022-06-12 23:51:31.942532
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert check_mutually_exclusive([["a", "b", "c"]], {"a": 1, "b": 2}) is None
    assert check_mutually_exclusive([["a", "b", "c"]], {"a": 1, "b": 2, "c": 3}) is not None



# Generated at 2022-06-12 23:51:42.156163
# Unit test for function check_required_together
def test_check_required_together():
    terms = [['state', 'address', 'port'], ['state', 'address']]
    parameters = {'state': 'present'}
    results = check_required_together(terms, parameters)
    assert results == []
    parameters['address'] = '192.168.2.2'
    results = check_required_together(terms, parameters)
    assert results == []
    parameters['port'] = '81'
    results = check_required_together(terms, parameters)
    assert results == []
    parameters['port'] = ''
    results = check_required_together(terms, parameters)
    assert results == []
    parameters['address'] = ''
    results = check_required_together(terms, parameters)
    assert results == [['state', 'address', 'port'], ['state', 'address']]

# Generated at 2022-06-12 23:51:53.882302
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    parameters = {
        "first_parameter": "first_value",
        "second_parameter": "second_value",
        "third_parameter": "third_value",
        "fourth_parameter": "fourth_value",
        "fifth_parameter": "fifth_value",
        "sixth_parameter": "sixth_value"
    }

    terms_1_1 = "first_parameter", "second_parameter"
    terms_1_2 = "third_parameter", "fourth_parameter"
    terms_1_3 = "fifth_parameter", "sixth_parameter"
    terms_group_1 = [
        terms_1_1,
        terms_1_2,
        terms_1_3,
    ]


# Generated at 2022-06-12 23:51:59.465337
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Unit test for function check_mutually_exclusive"""
    params = dict(foo=1, bar=1, baz=1)
    check_mutually_exclusive(['foo', 'bar'], params)
    check_mutually_exclusive(['bar', 'baz'], params)
    try:
        check_mutually_exclusive(['foo', 'bar', 'baz'], params)
    except TypeError:
        pass
    else:
        raise Exception('check_mutually_exclusive did not raise a TypeError')



# Generated at 2022-06-12 23:52:14.954548
# Unit test for function check_type_dict

# Generated at 2022-06-12 23:52:24.991333
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('') == 0
    assert check_type_bytes('0') == 0
    assert check_type_bytes('0B') == 0
    assert check_type_bytes('0b') == 0
    assert check_type_bytes('0kb') == 0
    assert check_type_bytes('1kb') == 1024
    assert check_type_bytes('10kb') == 10240
    assert check_type_bytes('1b') == 1
    assert check_type_bytes('1mb') == 1048576
    assert check_type_bytes('10mb') == 10485760
    assert check_type_bytes('1GB') == 1073741824
    assert check_type_bytes('10GB') == 10737418240
    assert check_type_bytes('1TB') == 1099511627776
    assert check

# Generated at 2022-06-12 23:52:31.386978
# Unit test for function safe_eval
def test_safe_eval():
    # When include_exceptions is not specified, safe_eval() returns output of literal_eval()
    assert safe_eval(u"[1, 2, {'foo': 'bar'}]") == [1, 2, {'foo': 'bar'}]

    # When include_exceptions is specified and literal_eval() did not raise an Exception, safe_eval() returns tuple of output and exception_object
    assert safe_eval(u"[1, 2, {'foo': 'bar'}]", include_exceptions=True) == ([1, 2, {'foo': 'bar'}], None)

    # When include_exceptions is specified and literal_eval() raised an Exception, safe_eval() returns tuple of input and exception_object

# Generated at 2022-06-12 23:52:34.011041
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    try:
        parameters = dict()
        required_parameters = ['param1', 'param2', 'param3', 'param5']
        missing_params = check_missing_parameters(parameters, required_parameters)
        assert missing_params == required_parameters
    except TypeError:
        raise


# Generated at 2022-06-12 23:52:43.111582
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1, 2]', None) == [1, 2]
    assert safe_eval('[1, 2]', None, True) == ([1, 2], None)
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo', None, True) == ('foo', None)
    assert safe_eval('import foo') == 'import foo'
    assert safe_eval('import foo', None, True) == ('import foo', None)
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('foo.bar()', None, True) == ('foo.bar()', None)



# Generated at 2022-06-12 23:52:54.826371
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    params = {}
    assert [] == check_missing_parameters(params, required_parameters=None)
    assert [] == check_missing_parameters(params, required_parameters=[])
    assert [] == check_missing_parameters(params, required_parameters=["foo"])
    params = {'foo': 0}
    assert [] == check_missing_parameters(params, required_parameters=["foo"])
    params = {'foo': None}
    assert ["foo"] == check_missing_parameters(params, required_parameters=["foo"])
    params = {'foo': [], 'bar': None}
    assert ["bar"] == check_missing_parameters(params, required_parameters=["foo", "bar"])

# Generated at 2022-06-12 23:52:57.685901
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    v = {"name": "test"}
    with pytest.raises(TypeError) as excinfo:
        assert check_missing_parameters(v)
    assert 'missing required arguments: name' in to_native(excinfo.value)



# Generated at 2022-06-12 23:53:03.725023
# Unit test for function check_type_bytes
def test_check_type_bytes():
    test_type_bytes = [
        (1, '1'),
        (2, '1kB'),
        (2.5, '2.5KB'),
        (2 * 2**20, '2MB'),
        (2.5 * 2**30, '2.5GB'),
        (2 * 2**40, '2TB'),
        (2.5 * 2**50, '2.5PB')
    ]
    for (bytes_value, str_value) in test_type_bytes:
        assert check_type_bytes(str_value) == bytes_value
        assert bytes_value == check_type_bytes(bytes_value)
    # Test for error condition
    check_error = ''
    err_flag = False

# Generated at 2022-06-12 23:53:15.132296
# Unit test for function safe_eval
def test_safe_eval():
    # valid literal evaluation
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    assert safe_eval("{'a':1,'b':2}") == {'a': 1, 'b': 2}
    assert safe_eval("(1,2,3)") == (1, 2, 3)
    assert safe_eval("1") == 1
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("None") is None
    assert safe_eval("'hello'") == 'hello'
    assert safe_eval("u'hello'") == u'hello'

    # invalid literal evaluation
    assert safe_eval("[1,2,3") == "[1,2,3"

# Generated at 2022-06-12 23:53:16.527804
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576

# Generated at 2022-06-12 23:53:24.302780
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int('1') == 1
    assert check_type_int(-1) == -1
    assert check_type_int(0) == 0
    assert_raises(TypeError, check_type_int, [])



# Generated at 2022-06-12 23:53:25.548990
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576


# Generated at 2022-06-12 23:53:32.316250
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits("1b") == 1
    assert check_type_bits("1B") == 8
    assert check_type_bits("1kb") == 128
    assert check_type_bits("1kB") == 1024
    assert check_type_bits("1mb") == 131072
    assert check_type_bits("1mB") == 1048576
    assert check_type_bits("1gb") == 134217728
    assert check_type_bits("1gB") == 1073741824
    assert check_type_bits("1tb") == 137438953472
    assert check_type_bits("1tB") == 1099511627776
    assert check_type_bits("1pb") == 140737488355328
    assert check_type_bits("1pB") == 1125899

# Generated at 2022-06-12 23:53:43.214465
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [['state', 'present', ('path', 'owner', 'group'), False], ['someint', 99, ('bool_param', 'string_param')]]
    parameters = {'state': 'present', 'alpha': 'test', 'someint': 99}
    err = check_required_if(requirements, parameters)
    assert len(err) == 1
    assert err[0]['parameter'] == 'someint'
    assert err[0]['missing'] == ['bool_param', 'string_param']
    parameters = {'state': 'present', 'alpha': 'test', 'someint': 99, 'bool_param': False}
    err = check_required_if(requirements, parameters)
    assert len(err) == 1
    assert err[0]['parameter'] == 'someint'

# Generated at 2022-06-12 23:53:50.568959
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('0') == 0
    assert check_type_bytes('1') == 1
    assert check_type_bytes(' 1 ') == 1
    assert check_type_bytes('1k') == 1000
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1 M') == 1048576
    assert check_type_bytes('1 G') == 1073741824
    assert check_type_bytes('1 Tera') == 1099511627776
    assert check_type_bytes('1 Peta') == 1125899906842624
    assert check_type_bytes('1 Gib') == 1073741824
    assert check_type_bytes('1 Gi') == 1073741824
    assert check_type_bytes('1 PiB') == 1148093149855488
    assert check

# Generated at 2022-06-12 23:54:01.580666
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Test valid case
    argument_spec = dict(
        required_one=dict(required=True),
        required_two=dict(required=True),
        optional_one=dict(required=False),
        optional_two=dict(required=False),
    )
    parameters = dict(required_one=1, required_two=2, optional_one=3)
    assert check_required_arguments(argument_spec, parameters) == []

    # Test invalid case
    argument_spec = dict(
        required_one=dict(required=True),
        required_two=dict(required=True),
        optional_one=dict(required=False),
        optional_two=dict(required=False),
    )
    parameters = dict(required_one=1, optional_one=3)

# Generated at 2022-06-12 23:54:10.791075
# Unit test for function check_required_by
def test_check_required_by():
    assert check_required_by({"test": ['a', 'b']}, {'test': "test"}) == {}
    assert check_required_by({"test": ['a', 'b']}, {'test': "test", 'a': "a"}) == {}
    assert check_required_by({"test": ['a', 'b']}, {'test': "test", 'b': "b"}) == {}
    assert check_required_by({"test": ['a', 'b']}, {'test': "test", 'a': "a", 'b': "b"}) == {}
    assert check_required_by({"test": ['a', 'b']}, {'test': "test", 'b': "b", 'c': "c"}) == {'test': ['a']}

# Generated at 2022-06-12 23:54:12.578174
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576

# Generated at 2022-06-12 23:54:22.869379
# Unit test for function check_type_dict
def test_check_type_dict():
    test_str = '"str"=str,"str2"=str2,"str3"=str3'  
    assert check_type_dict(test_str) == {'str': 'str', 'str2': 'str2', 'str3': 'str3'}
    test_json = "{'json_str':'json_str'}" 
    assert check_type_dict(test_json) == {'json_str': 'json_str'}

    json_excp = "{'json_str':'json_str'}"
    try:
        check_type_dict(json_excp)
    except TypeError as e:
        print(e)
        pass

    value_excp = '{"json_str":"json_str"'

# Generated at 2022-06-12 23:54:24.286501
# Unit test for function check_type_bytes
def test_check_type_bytes():
    result = check_type_bytes(10)
    assert result == 10



# Generated at 2022-06-12 23:54:33.051316
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb')
    try:
        check_type_bits('1')
    except TypeError:
        assert True
    else:
        assert False


# Generated at 2022-06-12 23:54:38.974550
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1MB') == 8388608
    assert check_type_bits('32Kb') == 32768
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1Tb') == 1099511627776
    assert check_type_bits('1Pb') == 1125899906842624
    assert check_type_bits('16385') == 16385



# Generated at 2022-06-12 23:54:48.005800
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('2M') == 2097152
    assert check_type_bits('1024') == 1024
    assert check_type_bits('6kb') == 6144
    assert check_type_bits('9.5G') == 976562500
    assert check_type_bits('1.3Gb') == 134217728
    assert check_type_bits('1.1GB') == 118111600
    assert check_type_bits('1T') == 1099511627776
    assert check_type_bits('1Tb') == 1208925819614629174706176
    assert check_type_bits(1024) == 1024
    assert check_type_bits(1024.0) == 1024
    assert check_type_bits(2048) == 2048

# Generated at 2022-06-12 23:55:00.350262
# Unit test for function check_required_together
def test_check_required_together():
    parameters = {'param1': 1, 'param2': 2, 'param3': 3, 'param4': 4, 'param5': 5, 'param6': 6}
    terms1 = (('param1', 'param2'), ('param3', 'param4'), ('param5', 'param6'))
    terms2 = (('param1', 'param2'), ('param3', 'param4'), ('param5', 'param6', 'param7', 'param8'))
    (results1, options_context1) = check_required_together(terms1, parameters, options_context=None)
    (results2, options_context2) = check_required_together(terms2, parameters, options_context=None)

    assert results1 == []
    assert options_context1 == None

# Generated at 2022-06-12 23:55:10.334043
# Unit test for function check_type_dict
def test_check_type_dict():
    # Positive test
    assert check_type_dict("k1=v1,k2=v2") == { 'k1':'v1', 'k2':'v2' }
    assert check_type_dict("k1=v1,k2=v2,k3=v3") == { 'k1':'v1', 'k2':'v2', 'k3': 'v3' }
    assert check_type_dict("k1=v1,k2=v2,k3=v3,k4=v4") == { 'k1':'v1', 'k2':'v2', 'k3': 'v3', 'k4': 'v4' }
    assert check_type_dict('k1=v1, k2=v2, k3=v3, k4=v4')

# Generated at 2022-06-12 23:55:19.765792
# Unit test for function check_type_bytes
def test_check_type_bytes():
    # Check integer values
    assert check_type_bytes(2048) == 2048
    assert check_type_bytes(1024 * 5) == 5120
    # Check string values
    assert check_type_bytes('1kb') == 1024
    assert check_type_bytes('1.7kb') == 1741
    assert check_type_bytes('1.5mb') == 1572864
    assert check_type_bytes('1gb') == 1073741824
    # Check invalid values
    try:
        check_type_bytes('1bb')
    except TypeError:
        pass
    try:
        check_type_bytes(None)
    except TypeError:
        pass



# Generated at 2022-06-12 23:55:22.677083
# Unit test for function check_required_together
def test_check_required_together():
    terms = [['a', 'b']]
    parameters = {'a': '1', 'b': '2'}
    check_required_together(terms, parameters)



# Generated at 2022-06-12 23:55:30.480450
# Unit test for function check_required_by

# Generated at 2022-06-12 23:55:39.699270
# Unit test for function check_required_together
def test_check_required_together():
    assert check_required_together(
        [['one', 'two'], ['three', 'four', 'five']],
        {'one': 1, 'two': 2},
    ) == []
    assert check_required_together(
        [['one', 'two'], ['three', 'four', 'five']],
        {'one': 1, 'two': 2, 'three': 3, 'six': 6},
    ) == []
    assert check_required_together(
        [['one', 'two'], ['three', 'four']],
        {'one': 1, 'two': 2, 'three': 3, 'six': 6},
    ) == []

# Generated at 2022-06-12 23:55:44.024085
# Unit test for function check_type_int
def test_check_type_int():
    a = check_type_int(20)
    assert a == 20, "pass int"
    b = check_type_int("20")
    assert b == 20, "pass string"

    try:
        check_type_int(20.1)
    except TypeError as e:
        assert str(e) == "'float' cannot be converted to an int"

    try:
        check_type_int("20.1")
    except TypeError as e:
        assert str(e) == "'string' cannot be converted to an int"



# Generated at 2022-06-12 23:55:58.824520
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1b') == 1
    assert check_type_bits('1k') == 1000
    assert check_type_bits('1K') == 1024
    assert check_type_bits('1Mb') == 1000000
    assert check_type_bits('1M') == 8388608
    assert check_type_bits('1mb') == 8388608
    assert check_type_bits('1Mb') == 1000000
    assert check_type_bits('1Gb') == 1000000000
    assert check_type_bits('1G') == 1073741824
    assert check_type_bits('1gb') == 1073741824
    assert check_type_bits('1T') == 1099511627776
    assert check_type_bits('1tb') == 1099511627776
    assert check_type_bits

# Generated at 2022-06-12 23:56:10.535031
# Unit test for function check_required_arguments
def test_check_required_arguments():

    # Check basic required argument checking
    params = {'var1': 'value'}
    spec = {'var1': {'required': True}}
    try:
        check_required_arguments(spec, params)
    except Exception as e:
        raise Exception("check_required_arguments with no value failed. Exception: {0}".format(e))

    # Check basic required argument checking with a key that matches defaulted argument in the spec
    params = {'var1': 'value'}
    spec = {'var1': {'required': False, 'default': 'default'}}
    try:
        check_required_arguments(spec, params)
    except Exception as e:
        raise Exception("check_required_arguments with no value failed. Exception: {0}".format(e))

    # Check basic required argument checking with a

# Generated at 2022-06-12 23:56:21.515002
# Unit test for function check_type_bytes
def test_check_type_bytes():
    s = check_type_bytes('1MB')
    assert(s == (1024 * 1024))
    s = check_type_bytes('1MBG')
    assert(s == (1024 * 1024 * 1024))
    s = check_type_bytes('1G')
    assert(s == (1024 * 1024 * 1024))
    s = check_type_bytes('1G')
    assert(s == (1024 * 1024 * 1024))
    s = check_type_bytes('2TB')
    assert(s == (2 * 1024 * 1024 * 1024 * 1024))
    s = check_type_bytes('2tb')
    assert(s == (2 * 1024 * 1024 * 1024 * 1024))
    s = check_type_bytes('2TiB')
    assert(s == (2 * 1024 * 1024 * 1024 * 1024))


# Generated at 2022-06-12 23:56:31.400645
# Unit test for function check_required_together
def test_check_required_together():
    parameters = {'vpc_id': 'vpc-29dc1548', 'vpc_security_group_ids': '868', 'vpc_subnet_id': 'subnet-2b7e295f'}
    terms = [['vpc_id', 'vpc_security_group_ids'], ['vpc_id', 'vpc_subnet_id']]
    options_context = ['vpc']
    assert check_required_together(terms, parameters, options_context) == []

    parameters = {'vpc_security_group_ids': '868'}
    assert check_required_together(terms, parameters, options_context) == [['vpc_id', 'vpc_security_group_ids']]



# Generated at 2022-06-12 23:56:32.903186
# Unit test for function check_required_arguments
def test_check_required_arguments():
    required_args = check_required_arguments(argument_spec, parameters)
    assert required_args == []



# Generated at 2022-06-12 23:56:42.191970
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict("{\"foo\": \"bar\"}") == {"foo": "bar"}
    assert check_type_dict("foo=bar") == {"foo": "bar"}
    assert check_type_dict(u"foo=bar") == {"foo": "bar"}
    assert check_type_dict("\"foo\"=bar") == {"foo": "bar"}
    assert check_type_dict("\"foo bar\"=bar") == {"foo bar": "bar"}
    assert check_type_dict("foo=\"bar\"") == {"foo": "bar"}
    assert check_type_dict("foo=\"bar\nbaz\"") == {"foo": "bar\nbaz"}
    assert check_type_dict('foo="bar\\nbaz"') == {"foo": "bar\\nbaz"}

# Generated at 2022-06-12 23:56:45.484731
# Unit test for function check_type_float
def test_check_type_float():
    """
    check_type_float function test
    """
    # given
    value = '1.0'
    # when
    float_type = check_type_float(value)
    # then
    assert float_type == 1.0



# Generated at 2022-06-12 23:56:52.039154
# Unit test for function check_required_together
def test_check_required_together():
    terms = [
        ('state', 'metric', 'threshold'),
        ('state', 'metric', 'comparison')
    ]
    parameters = {
        'state': 'present',
        'metric': 'CPU',
        'threshold': '80%',
    }
    results = check_required_together(terms, parameters)
    assert results == [('state', 'metric', 'comparison')]



# Generated at 2022-06-12 23:56:53.471886
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(7.2) == 7.2

# Generated at 2022-06-12 23:57:02.022022
# Unit test for function check_required_if
def test_check_required_if():
    """Test check_required_if for all types of requirements"""
    assert check_required_if([['a', 'b', ['c'], False]], {'a': 'b', 'b': 'c'}) == []
    assert check_required_if([['a', 'b', ['c'], True]], {'a': 'b', 'b': 'c'}) == []
    # Check all required
    assert check_required_if([['a', 'b', ['c'], False]], {'a': 'b'}) != []
    # Check one of the required
    assert check_required_if([['a', 'b', ['c'], True]], {'a': 'b', 'b': 'c'}) == []

# Generated at 2022-06-12 23:57:13.634985
# Unit test for function check_type_int
def test_check_type_int():
    """
    Test check_type_int()
    """
    assert check_type_int('1') == 1
    assert check_type_int(1) == 1
    assert check_type_int(0) == 0

    try:
        check_type_int(1.1)
        assert False
    except TypeError:
        pass

    try:
        check_type_int(None)
        assert False
    except TypeError:
        pass

    try:
        check_type_int('a')
        assert False
    except TypeError:
        pass



# Generated at 2022-06-12 23:57:21.562940
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Unit test for function check_mutually_exclusive"""
    parameters = {
        'ansible_connection': 'local',
        'password': 'hunter2',
        'force': True,
        'state': 'absent'
    }

    terms_list = [
        ['user', 'group'],
        ['force', 'state']
    ]

    # pass
    check_mutually_exclusive(terms_list, parameters)

    parameters['user'] = 'bob'
    parameters['group'] = 'admins'

    # fail
    try:
        check_mutually_exclusive(terms_list, parameters)
        raise AssertionError('check_mutually_exclusive did not raise TypeError')
    except TypeError:
        pass

    parameters.pop('user')
    parameters.pop('group')
    parameters['state']

# Generated at 2022-06-12 23:57:27.941033
# Unit test for function check_required_together
def test_check_required_together():
    assert check_required_together([
        ('a', 'b'),
        ('b', 'c')
    ], {'a': 1, 'b': 2}) is None

    assert check_required_together([
        ('a', 'b'),
        ('b', 'c')
    ], {'a': 1, 'b': 2, 'c': 3}) is None

    assert check_required_together([
        ('a', 'b'),
        ('b', 'c')
    ], {'a': 1, 'c': 3}) is None

    assert check_required_together([
        ('a', 'b'),
        ('b', 'c')
    ], {'a': 1}) is None

    assert check_required_together([
        ('a', 'b'),
        ('b', 'c')
    ], {'b': 1}) is None

# Generated at 2022-06-12 23:57:39.004692
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    set_of_same_keys = {'a', 'b', 'c'}
    set_of_different_keys = {'c', 'd'}
    assert check_mutually_exclusive({'a', 'b', 'c'}, set_of_same_keys) == []
    assert check_mutually_exclusive({'a', 'b', 'c'}, set_of_different_keys) == []
    assert check_mutually_exclusive({{'a', 'b'}, {'b', 'c'}}, set_of_same_keys) == []
    assert check_mutually_exclusive({{'a', 'b'}, {'b', 'c'}}, set_of_different_keys) == []
    assert check_mutually_exclusive(None, set_of_same_keys) == []
    assert check_

# Generated at 2022-06-12 23:57:48.577380
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
        ['someotherint', 42, [('eins', 'zwei', 'drei')]]
    ]
    parameters = {
        'state': 'present',
        'path': '/some/path'
    }
    result_single = check_required_if(requirements, parameters)
    assert len(result_single) == 2
    assert result_single[0]['parameter'] == 'someint'
    assert result_single[1]['requires'] == 'all'
    assert result_single[1]['requirements'] == ('eins', 'zwei', 'drei')



# Generated at 2022-06-12 23:57:56.017692
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Required arguments present
    required_arguments_present = dict(
        one=dict(required=True),
        two=dict(required=True),
        three=dict(required=True),
    )
    parameters = dict(
        one=dict(anything=True),
        two=dict(anything=True),
        three=dict(anything=True),
    )
    # assert check_required_arguments(required_arguments_present, parameters) == []
    # Required arguments missing
    required_arguments_present = dict(
        one=dict(required=True),
        two=dict(required=True),
        three=dict(required=True),
    )
    parameters = dict(
        one=dict(anything=True),
        three=dict(anything=True),
    )
    # Check for malformed required parameter


# Generated at 2022-06-12 23:58:07.881597
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    parameters = dict(param1=1, param2=2)
    check_mutually_exclusive([['param1', 'param2']], parameters)
    try:
        check_mutually_exclusive([['param1', 'param2']], dict(param1=1, param2=2, param3=3))
        assert False, "Expected throw"
    except TypeError:
        pass

    data = dict(param1=1, param2=2, param3=3)
    try:
        check_mutually_exclusive([['param1', 'param2']], data, ['key1', 'key2'])
        assert False, "Expected throw"
    except TypeError as e:
        assert "found in key1 -> key2" in to_native(e)



# Generated at 2022-06-12 23:58:11.706146
# Unit test for function check_type_bits
def test_check_type_bits():
    try:
        assert check_type_bits('1Mb') == 1048576
    except TypeError:
        assert False
    try:
        assert check_type_bits(123) == 123
    except TypeError:
        assert False

# Generated at 2022-06-12 23:58:15.053577
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float("1.0") == 1.0
    try:
        check_type_float("foo")
        succeeded = True
    except ValueError:
        succeeded = False
    assert succeeded == False


# Generated at 2022-06-12 23:58:24.643728
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Kb') == 1024
    assert check_type_bits('1mb') == 1048576
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1gbit') == 1073741824
    assert check_type_bits('1mbit') == 1048576
    assert check_type_bits('1kbit') == 1024
    assert check_type_bits('1gbits') == 1073741824
    assert check_type_bits('1mbits') == 1048576
    assert check_type_bits('1kbits') == 1024
    assert check_type_bits('1TB') == 1099511627776

# Generated at 2022-06-12 23:58:34.709951
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.0) == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float('1') == 1.0
    with pytest.raises(TypeError):
        check_type_float(None)
    with pytest.raises(TypeError):
        check_type_float(True)
