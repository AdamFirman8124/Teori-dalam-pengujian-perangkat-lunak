

# Generated at 2022-06-12 23:49:28.643850
# Unit test for function check_type_bits
def test_check_type_bits():
    from ansible.module_utils.basic import human_to_bytes
    assert check_type_bits('1Mb') == human_to_bytes('1Mb', isbits=True)
    try:
        check_type_bits(1)
        assert False
    except TypeError:
        pass
    try:
        check_type_bits('1')
        assert False
    except TypeError:
        pass



# Generated at 2022-06-12 23:49:36.483565
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments({'param1': {'required': True}}, {'param1': 'value1'}) == []
    assert check_required_arguments({'param1': {'required': True}}, {}) == ['param1']
    assert check_required_arguments({'param1': {'required': True}, 'param2': {'required': True}}, {'param1': 'value1'}) == ['param2']
    assert check_required_arguments({'param1': {'required': True}, 'param2': {'required': False}}, {'param1': 'value1', 'param2': 'value2'}) == []

# Generated at 2022-06-12 23:49:46.542524
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
        class TestModule(object):
            def __init__(self, a, b):
                self.params = dict(a=a, b=b)

            def fail_json(self, *args, **kwargs):
                self.exit_args = args
                self.exit_kwargs = kwargs
                raise Exception('fail_json')

            def exit_json(self, *args, **kwargs):
                self.exit_args = args
                self.exit_kwargs = kwargs

        def exit_json(*args, **kwargs):
            return_value.update(dict(exit_args=args, exit_kwargs=kwargs))

        # Define required_together
        required_parameters = ['a', 'b', 'c']

        m = TestModule(a=4, b='World')
        check_

# Generated at 2022-06-12 23:49:53.112782
# Unit test for function check_required_by
def test_check_required_by():
    options_context = ["test"]
    requirements = dict(test_1={'test_2', 'test_3'})
    parameters = dict(test_1=None, test_2="Test", test_3=None)
    check_required_by(requirements, parameters)
    parameters = dict(test_1=None, test_3=None)
    try:
        check_required_by(requirements, parameters)
    except:
        pass
    else:
        assert False



# Generated at 2022-06-12 23:49:58.101872
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    expected = ['param1', 'param2']
    actual = check_missing_parameters({}, required_parameters=expected)
    assert actual == expected


# Generated at 2022-06-12 23:50:06.711999
# Unit test for function check_required_by
def test_check_required_by():
    parameters = {'a': 'a', 'b': 'b'}
    requirements = {'a': 'b'}
    options_context = None
    results = check_required_by(requirements, parameters, options_context)
    assert results == {}
    parameters = {'a': 'a'}
    results = check_required_by(requirements, parameters, options_context)
    assert results == {}
    parameters = {'b': 'b'}
    results = check_required_by(requirements, parameters, options_context)
    assert results == {}
    parameters = {'b': 'b', 'e': 'e'}
    results = check_required_by(requirements, parameters, options_context)
    assert results == {}
    parameters = {'a': 'a', 'c': 'c'}
    results

# Generated at 2022-06-12 23:50:17.842334
# Unit test for function check_required_by
def test_check_required_by():
    """
    check_required_by:
    - requirements:
        - key: [value, value]
        - key: [value, value]
    - parameters:
        - key: value
        - key: value
    - options_context:
        - value
    """
    requirements = {
        'key': ['value', 'value'],
        'key2': ['value2', 'value2'],
    }
    parameters = {
        'key': 'value',
        'key2': 'value2',
    }
    options_context = ['value']

    check_required_by(requirements, parameters, options_context)
    # Uncomment to test execution failure
    # parameters.pop('key2')
    # check_required_by(requirements, parameters, options_context)



# Generated at 2022-06-12 23:50:27.797222
# Unit test for function check_required_by
def test_check_required_by():
    assert check_required_by(None, dict(key1='a', key2='b')) == dict()
    assert check_required_by(dict(key1=None), dict(key1='a', key2='b')) == dict()

    assert check_required_by(dict(key1=None), dict(key2='a')) == dict()
    assert check_required_by(dict(key1='key2'), dict(key1='a', key2='b')) == dict()
    assert check_required_by(dict(key1='key2'), dict(key1='a', key2=None)) == dict(key1=[])
    assert check_required_by(dict(key1='key2'), dict(key1='a')) == dict(key1=[])

# Generated at 2022-06-12 23:50:32.791775
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Test check_mutually_exclusive function"""
    assert check_mutually_exclusive(["p"], {}) == []
    assert check_mutually_exclusive([["p"]], {"p": 1}) == []
    assert check_mutually_exclusive([["p", "q"]], {"p": 1}) == []
    assert check_mutually_exclusive([["p", "q"]], {"q": 1}) == []
    try:
        check_mutually_exclusive([["p", "q"]], {"p": 1, "q": 1})
        raise RuntimeError("Exception not raised")
    except TypeError:
        pass



# Generated at 2022-06-12 23:50:42.639093
# Unit test for function check_required_if
def test_check_required_if():
    """Unit tests for function check_required_if"""

    # Construct requirements

# Generated at 2022-06-12 23:50:58.789708
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert check_mutually_exclusive([['a','b','c']], {'a':1}) == []
    assert check_mutually_exclusive([['a','b','c']], {'a':1, 'b':1}) != []
    assert check_mutually_exclusive([['a','b','c']], {'a':1, 'b':1, 'c':1}) != []
    assert check_mutually_exclusive([['a','b','c'],['e','f']], {'a':1, 'f':1}) == []
    assert check_mutually_exclusive([['a','b','c'],['e','f']], {'a':1, 'e':1}) != []

# Generated at 2022-06-12 23:51:09.511506
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # empty required argument
    ar = {}
    para = {}
    assert check_required_arguments(ar, para) is None
    # require one argument, non-exist
    ar = {'name': {'required': True}}
    para = {}
    with pytest.raises(TypeError):
        check_required_arguments(ar, para)
    # require one argument, exist
    ar = {'name': {'required': True}}
    para = {'name': 'test'}
    assert check_required_arguments(ar, para) is None
    # require one argument, exist with default value
    ar = {'name': {'required': True, 'default': 'test'}}
    para = {'name': 'test'}
    assert check_required_arguments(ar, para) is None



# Generated at 2022-06-12 23:51:20.139066
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """ Unit Test for check_mutually_exclusive """

# Generated at 2022-06-12 23:51:28.385429
# Unit test for function check_required_if
def test_check_required_if():
    from ansible.module_utils.common.validation import check_required_if
    import pytest

# Generated at 2022-06-12 23:51:31.008719
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1 + 1") == 2
    assert safe_eval("foo(1, 2)") == "foo(1, 2)"
    assert safe_eval("import os") == "import os"


# Generated at 2022-06-12 23:51:41.791576
# Unit test for function check_type_dict
def test_check_type_dict():
    dict_test_cases = ['{"key": "value"}',
                       "key=value",
                       '"key=value, test_key=test_value"',
                       "{'key': 'value'}",
                       "not_a_dict"]

    dict_results = [{"key": "value"},
                    {"key": "value"},
                    {"key=value": "test_key=test_value"},
                    {"key": "value"},
                    TypeError("not_a_dict cannot be converted to a dict")]

    assert len(dict_test_cases) == len(dict_results)


# Generated at 2022-06-12 23:51:53.639283
# Unit test for function check_required_together
def test_check_required_together():
    parameters = {'p1': '1',
                  'p2': '2',
                  'p3': '3',
                  'p4': '4',
                  'p5': '5',
                  'p6': '6'}
    # check the normal input
    terms = [['p1', 'p4'], ['p3', 'p4']]
    options_context = None
    results = []
    try:
        results = check_required_together(terms, parameters, options_context=None)
    except TypeError as e:
        print(e)
    if len(results) == 0:
        print("no errors\n")
    # check error input1
    terms = [['p1', 'p2'], ['p5', 'p6']]

# Generated at 2022-06-12 23:52:04.180075
# Unit test for function check_required_if
def test_check_required_if():
    # Positive test cases
    assert check_required_if([['state', 'present', ['path']], ['someint', 99, ['bool_param', 'string_param']]], {'state': 'present', 'path': '/etc/passwd', 'someint': 99, 'bool_param': True, 'string_param': 'hello'}, []) == []
    assert check_required_if([['state', 'present', ('path',)], ['someint', 99, ('bool_param', 'string_param')], ['someint', 123, ('bool_param')]], {'state': 'present', 'path': '/etc/passwd', 'bool_param': True, 'someint': 123}, []) == []

# Generated at 2022-06-12 23:52:04.837529
# Unit test for function check_type_dict
def test_check_type_dict():
    pass

# Generated at 2022-06-12 23:52:15.957229
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {'someint': 99, 'bool_param': True}
    results = check_required_if(requirements, parameters)
    assert results[0]['parameter'] == 'someint'
    assert results[0]['value'] == 99
    assert results[0]['requirements'] == ('bool_param', 'string_param')
    assert results[0]['missing'] == ['string_param']
    assert results[0]['requires'] == 'all'
    assert len(results) == 1
    parameters = {'someint': 99}

# Generated at 2022-06-12 23:52:25.348529
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.1) == 1.1
    assert check_type_float(2) == 2.0
    assert check_type_float(b'3.1') == 3.1
    assert check_type_float('4.1') == 4.1
    assert check_type_float(u'5.1') == 5.1
    assert check_type_float(6) == 6.0
    assert check_type_float(7.1) == 7.1
    with pytest.raises(TypeError):
        check_type_float([])



# Generated at 2022-06-12 23:52:31.599246
# Unit test for function check_type_dict
def test_check_type_dict():
    '''
    Run unit tests for ``check_type_dict``
    '''
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Conversion from string to dict
    value = '{"key1":"value1", "key2":"value2"}'
    expect = {u'key1': u'value1', u'key2': u'value2'}
    actual = check_type_dict(value)
    assert actual == expect, "'%s' != '%s'" % (actual, expect)

    # Conversion from string to dict
    value = '{"key1":{"key11":"value11", "key12":"value12"},"key2":"value2"}'

# Generated at 2022-06-12 23:52:37.329351
# Unit test for function check_required_if
def test_check_required_if():
    from ansible.module_utils.common.validation import check_required_if
    parameters = dict(paths=["/tmp/test.txt"], state="present")
    requirements = [['paths', ['/tmp/test.txt'], ["state", "owner"], True]]
    check_required_if(requirements, parameters)
    # Test with is_one_of=False
    requirements = [['paths', ['/tmp/test.txt'], ["state", "owner"], False]]
    check_required_if(requirements, parameters)
    # Test with missing values
    parameters = dict(paths=["/tmp/test.txt"], state="present", owner=None)
    requirements = [['paths', ['/tmp/test.txt'], ["state", "owner"], True]]

# Generated at 2022-06-12 23:52:46.527306
# Unit test for function check_required_if
def test_check_required_if():
    reqs = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    params_a = {'state': 'present', 'path': '/path/to/file'}
    params_b = {'someint': 99, 'bool_param': True}
    params_c = {'someint': 99, 'bool_param': True, 'string_param': True}
    params_d = {'someint': 99, 'string_param': True}
    params_e = {'someint': 99}
    params_f = {'someint': 100}
    params_g = {'state': 'absent'}
    assert [] == check_required_if(reqs, params_a)
    assert [] == check_required

# Generated at 2022-06-12 23:52:52.344388
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    parameters1 = {
        'arg1': '123'
    }
    required_parameters1 = [
        'arg1', 'arg2', 'arg3'
    ]
    missing_params = check_missing_parameters(parameters1, required_parameters1)
    assert missing_params == ['arg2', 'arg3']



# Generated at 2022-06-12 23:52:57.368199
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(0) == 0
    assert check_type_bytes('0') == 0
    assert check_type_bytes(1) == 1
    assert check_type_bytes('1') == 1
    assert check_type_bytes('-1') == -1
    assert check_type_bytes('1k') == 1024
    assert check_type_bytes('10k') == 10240



# Generated at 2022-06-12 23:53:02.755349
# Unit test for function check_required_one_of
def test_check_required_one_of():
    # if no parameters are given and there is no required one of check
    assert check_required_one_of(None, {}) == []
    # A clear positive case for the required one of check
    results = check_required_one_of([['a', 'b']], {'a': 1, 'b': 2})
    assert results == []
    # A clear negative case with both the correct output and error message
    try:
        check_required_one_of([['a', 'b']], {'c': 1, 'd': 2})
    except Exception as e:
        assert e.args[0] == "one of the following is required: a, b"



# Generated at 2022-06-12 23:53:06.879617
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.0) == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float('1') == 1.0
    assert check_type_float(b'1.0') == 1.0
    assert check_type_float('1.0') == 1.0
    with pytest.raises(TypeError):
        check_type_float('not a float')
    with pytest.raises(TypeError):
        check_type_float(['1'])


# Generated at 2022-06-12 23:53:18.379035
# Unit test for function safe_eval
def test_safe_eval():
    test_eval = [
        # test_str, expected_result , expected_exception
        ['1', 1, None],
        ['[1,2]', [1,2], None],
        ['{1:2}', {1:2}, None],
        ['test_str()', 'test_str()', Exception],
        ['import datetime', 'import datetime', Exception],
        ['[1,2],3,4', '[1,2],3,4', Exception],
    ]
    for test in test_eval:
        result, exception = safe_eval(test[0], include_exceptions=True)
        assert result == test[1], 'Eval {} failed: {}'.format(test[0], result)

# Generated at 2022-06-12 23:53:27.258549
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict({}) == {}
    assert check_type_dict({"a,b": "c"}) == {"a,b": "c"}
    assert check_type_dict('{"a,b": "c"}') == {"a,b": "c"}
    assert check_type_dict('{"a": "b"}') == {"a": "b"}
    assert check_type_dict('a=b') == {'a': 'b'}
    assert check_type_dict('a=b c=d') == {'a': 'b', 'c': 'd'}
    assert check_type_dict('a=b, c=d') == {'a': 'b', 'c': 'd'}

# Generated at 2022-06-12 23:53:36.948860
# Unit test for function check_type_int
def test_check_type_int():
    check_type_int(1234)
    assert(check_type_int('1234') == 1234)
    try:
        check_type_int('abcd')
    except TypeError:
        assert(True)



# Generated at 2022-06-12 23:53:40.371699
# Unit test for function check_type_int
def test_check_type_int():
    assert 3 == check_type_int("3")
    assert 4 == check_type_int(4)
    try:
        check_type_int("a")
    except TypeError:
        pass
    else:
        assert False



# Generated at 2022-06-12 23:53:43.952804
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(200) == 200
    assert check_type_int("200") == 200
    assert check_type_int(u"200") == 200

    with pytest.raises(TypeError):
        check_type_int("Two Hundred")

    with pytest.raises(TypeError):
        check_type_int(200.1)


# FIXME: The param and prefix parameters here are coming from AnsibleModule._check_type_string()
#        which is using those for the warning messaged based on string conversion warning settings.
#        Not sure how to deal with that here since we don't have config state to query.

# Generated at 2022-06-12 23:53:46.153132
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 8388608, 'should have returned integer 8388608'

# Unit test code for function check_type_dict

# Generated at 2022-06-12 23:53:47.034751
# Unit test for function check_type_int
def test_check_type_int():
    print(check_type_int(1))


# Generated at 2022-06-12 23:53:58.238425
# Unit test for function check_required_one_of
def test_check_required_one_of():
    try:
        list1 = ['username', 'password']
        list2 = ['username', 'password']
        list3 = ['username', 'password']
        list4 = ['username', 'password']
        list5 = ['username', 'password']
        parameters = ['username', 'password']
        input = [list1, list2, list3, list4, list5]
        check_required_one_of(input, parameters)
    except:
        assert 0

# Generated at 2022-06-12 23:54:01.531211
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int("1") == 1
    with pytest.raises(TypeError):
        check_type_int(None)


# Generated at 2022-06-12 23:54:07.979307
# Unit test for function check_type_int
def test_check_type_int():
    int_val = check_type_int(1)
    assert isinstance(int_val, integer_types)
    str_val = check_type_int("1")
    assert isinstance(str_val, integer_types)
    with pytest.raises(TypeError):
        check_type_int(1.0)
    with pytest.raises(TypeError):
        check_type_int("1.0")
    with pytest.raises(TypeError):
        check_type_int("1x")



# Generated at 2022-06-12 23:54:11.732793
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(5) == 5.0
    assert check_type_float(5.0) == 5.0
    assert check_type_float('5') == 5.0
    assert check_type_float(b'5') == 5.0
    assert check_type_float(u'5') == 5.0



# Generated at 2022-06-12 23:54:22.463379
# Unit test for function check_required_arguments
def test_check_required_arguments():
    """Unit test for function check_required_arguments"""
    params = {'one': 1, 'two': 2, 'three': 3}
    argspec = {'one': {}, 'two': {}, 'three': {}}
    missing = check_required_arguments(argspec, params)
    assert len(missing) == 0, 'One or more required arguments missing'

    argspec = {'one': {'required': True}, 'two': {'required': True}}
    missing = check_required_arguments(argspec, params)
    assert len(missing) == 0, 'One or more required arguments missing'

    argspec = {'one': {'required': True}, 'two': {}}
    missing = check_required_arguments(argspec, params)

# Generated at 2022-06-12 23:54:36.794100
# Unit test for function check_type_bytes

# Generated at 2022-06-12 23:54:43.066698
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # there is no raise for function
    try:
        check_required_arguments({}, {})
    except TypeError:
        raise AssertionError("Fail: no raise for {}")

    try:
        check_required_arguments({"key": {}}, {})
    except TypeError:
        raise AssertionError("Fail: no raise for {'key': {}}")

    try:
        check_required_arguments({"key": {"required": True}}, {})
    except TypeError:
        raise AssertionError("Fail: no raise for {'key': {'required': True}}")


# Generated at 2022-06-12 23:54:44.025730
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb'), 1048576



# Generated at 2022-06-12 23:54:46.365211
# Unit test for function check_type_bits
def test_check_type_bits():
    assert(check_type_bits('1Mb') == 1048576)
    assert(check_type_bits('0.5Mb') == 524288)
    

# Generated at 2022-06-12 23:54:59.215148
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(2048) == 2048
    assert check_type_bytes('2048') == 2048
    assert check_type_bytes('2kB') == 2 * units.k
    assert check_type_bytes(2 * units.Ki) == 2 * units.Ki
    assert check_type_bytes(2 * units.Ki + 10) == 2 * units.Ki + 10
    assert check_type_bytes('2KB') == 2 * units.K
    assert check_type_bytes(2 * units.K) == 2 * units.K
    assert check_type_bytes(2 * units.K + 10) == 2 * units.K + 10
    assert check_type_bytes('2kiB') == 2 * units.k
    assert check_type_bytes('2MB') == 2 * units.M

# Generated at 2022-06-12 23:55:05.825644
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1024') == 1024
    assert isinstance(check_type_bits('1kb'), int)
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1Tb') == 1099511627776
    with pytest.raises(TypeError):
        check_type_bits('1ZX')



# Generated at 2022-06-12 23:55:17.072566
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1mb') == 1048576
    assert check_type_bits('1gb') == 1073741824
    assert check_type_bits('1tb') == 1099511627776
    assert check_type_bits('1024') == 1024
    assert check_type_bits('1024kb') == 1048576
    assert check_type_bits('1024.0kb') == 1048576
    assert check_type_bits('1024.4kb') == 1072693.12
    assert check_type_bits(1024.4) == 1072693.12


# Generated at 2022-06-12 23:55:28.214292
# Unit test for function check_type_dict

# Generated at 2022-06-12 23:55:38.152309
# Unit test for function check_required_arguments
def test_check_required_arguments():
    params = {
        'name': 'test',
        'file': 'test',
        'state': 'test',
    }
    params_none = {
        'name': None,
        'file': None,
        'state': None,
    }
    params_empty = {
        'name': '',
        'file': '',
        'state': '',
    }
    argument_spec = {
        'file': {
            'required': True,
            'type': 'str',
        },
        'name': {
            'required': True,
            'type': 'str',
        },
        'other': {
            'type': 'str',
        },
        'state': {
            'required': True,
            'type': 'str',
        },
    }

    assert check_required_

# Generated at 2022-06-12 23:55:46.793147
# Unit test for function check_type_dict
def test_check_type_dict():
    d = check_type_dict({"a":"b"})
    assert d == {"a":"b"}

    d = check_type_dict('a="b", c="d"')
    assert d == {"a":"b", "c":"d"}

    try:
        d = check_type_dict('a=b, c=d')
    except Exception as e:
        assert type(e) == TypeError

    d = check_type_dict('{ "a" : "b" }')
    assert d == {"a":"b"}

    d = check_type_dict('{"a":"b", "c":"d"}')
    assert d == {"a":"b", "c":"d"}



# Generated at 2022-06-12 23:56:01.355087
# Unit test for function check_required_arguments
def test_check_required_arguments():
    class AnsibleModule:
        def __init__(self, name, argument_spec=None):
            self.name = name
            self.argument_spec = {}
            for (k, v) in argument_spec.items():
                self.argument_spec[k] = v
                self.params = {}
                for (k, v) in argument_spec.items():
                    self.params[k] = None

    # Set up argument_spec for test
    argument_spec = dict(
        param1=dict(required=True),
        param2=dict(required=False),
        param3=dict(required=True),
        param4=dict(required=False),
    )
    parameters = dict(param2=True, param4=True)
    # Expected result is [param1, param3]
    result = check_

# Generated at 2022-06-12 23:56:02.719262
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("x") == 1


# Generated at 2022-06-12 23:56:06.511724
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'arg1': {
            'required': True,
        },
        'arg2': {
            'required': False,
        },
        'arg3': {
            'required': True,
        },
    }
    try:
        check_required_arguments(argument_spec, {'arg1': 'val1'})
    except TypeError:
        return
    assert False, 'Expected TypeError'

# Generated at 2022-06-12 23:56:08.024679
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576


# Generated at 2022-06-12 23:56:10.868458
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('20G') == 20971520000
    with pytest.raises(TypeError):
        check_type_bytes('I am not a byte value.')



# Generated at 2022-06-12 23:56:13.068223
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(10) == 10
    assert check_type_int("10") == 10
    assert check_type_int(u"10") == 10


# Generated at 2022-06-12 23:56:23.708862
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("") is None
    assert safe_eval(" ", include_exceptions=True) == (' ', None)
    assert safe_eval("\"\"") == ""
    assert safe_eval("\"\"", include_exceptions=True) == ('""', None)
    assert safe_eval("\"\"\"\"") == ""
    assert safe_eval("[]") == []
    assert safe_eval("{}") == {}
    assert safe_eval("no_quotes") == "no_quotes"
    assert isinstance(safe_eval('"no_quotes"'), text_type)
    assert isinstance(safe_eval('"no_quotes"', include_exceptions=True), tuple)
    assert isinstance(safe_eval('"no_quotes"', include_exceptions=True)[0], text_type)
   

# Generated at 2022-06-12 23:56:31.637592
# Unit test for function check_type_bits
def test_check_type_bits():
    assert (check_type_bits('1b') == 1)
    assert (check_type_bits('1Kb') == 1024)
    assert (check_type_bits('1Mb') == 1048576)
    assert (check_type_bits('1Gb') == 1073741824)
    assert (check_type_bits('1Tb') == 1099511627776)
    assert (check_type_bits('1Pb') == 1125899906842624)
    assert (check_type_bits('1Eb') == 1152921504606846976)



# Generated at 2022-06-12 23:56:38.775342
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1KiB') == 1024
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1MiB') == 1048576
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1GiB') == 1073741824
    assert check_type_bits('1Tb') == 1099511627776
    assert check_type_bits('1TiB') == 1099511627776


# Generated at 2022-06-12 23:56:49.102074
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    fnc_name = 'ansible.module_utils.common.validation.check_mutually_exclusive'
    # Testing the following code path:
    #  - terms is not None
    #  - terms is iterable
    #  - len(terms) > 0
    #  - count_terms returns 0
    mock_terms = [["test_key1", "test_key2"], ["test_key3", "test_key4"]]
    mock_parameters = {}
    try:
        check_mutually_exclusive(mock_terms, mock_parameters)
    except TypeError:
        raise AssertionError('Failed to test the "%s" function positive code path' % fnc_name)
    except:
        pass
    # Testing the following code path:
    #  - terms is not None
    # 

# Generated at 2022-06-12 23:57:01.453164
# Unit test for function check_required_arguments
def test_check_required_arguments():
    try:
        check_required_arguments({'b': {}}, {})
    except TypeError as e:
        assert e.args[0] == "missing required arguments: b"
    else:
        assert False

    try:
        check_required_arguments({'b': {'required': True}}, {})
    except TypeError as e:
        assert e.args[0] == "missing required arguments: b"
    else:
        assert False

    assert check_required_arguments({'b': {'required': True}}, {'b': None}) == []
    assert check_required_arguments({'b': {'required': True}}, {'b': ''}) == []
    assert check_required_arguments({'b': {'required': False}}, {}) == []

    assert check_required_arguments

# Generated at 2022-06-12 23:57:08.539216
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict({'foo': 'bar'}) == {'foo': 'bar'}
    assert check_type_dict('{"foo": "bar"}') == {'foo': 'bar'}
    assert check_type_dict('foo=bar') == {'foo': 'bar'}
    assert check_type_dict('foo=bar,baz=bar') == {'foo': 'bar', 'baz': 'bar'}
    # argparse strips out the '=' from the value
    assert check_type_dict('foo=bar=baz') == {'foo': 'bar=baz'}
    assert check_type_dict('foo=bar,baz="bar=baz"') == {'foo': 'bar', 'baz': 'bar=baz'}

# Generated at 2022-06-12 23:57:15.868574
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int("1") == 1
    assert check_type_int("-1") == -1
    assert check_type_int("0") == 0
    assert check_type_int(1) == 1
    assert check_type_int(-1) == -1
    assert check_type_int(0) == 0
    for value in ("1.0", "a", [], {}):
        try:
            check_type_int(value)
            assert False, "should have failed for %s" % value
        except TypeError:
            pass



# Generated at 2022-06-12 23:57:18.925039
# Unit test for function check_type_dict
def test_check_type_dict():
    values = [
        "{'k':'v'}",
        "k=v"
    ]
    for value in values:
        result = check_type_dict(value)
        assert(isinstance(result, dict))
        assert('k' in result)
        assert(result['k'] == 'v')

# Generated at 2022-06-12 23:57:28.460649
# Unit test for function safe_eval
def test_safe_eval():
    # Test passing string literal
    literal = "test"
    assert safe_eval(literal) == literal
    # Test passing string representation of None
    assert safe_eval("None") is None
    # Test passing string with method call
    assert safe_eval("test.method()") == "test.method()"
    assert safe_eval("test.method()", include_exceptions=True)[0] == "test.method()"
    # Test passing string with import
    assert safe_eval("import foo") == "import foo"
    assert safe_eval("import foo", include_exceptions=True)[0] == "import foo"
    # Test passing dict
    test_dict = dict()
    test_dict['key'] = "value"
    assert safe_eval(test_dict) == test_dict



# Generated at 2022-06-12 23:57:39.402273
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("1K") == 1024
    assert check_type_bytes("1.5K") == 1536
    assert check_type_bytes("2MB") == 2 * 1024 * 1024
    assert check_type_bytes("1G") == 1024 * 1024 * 1024
    assert check_type_bytes("1t") == 2 ** 40
    assert check_type_bytes("1pb") == 2 ** 50
    assert check_type_bytes("1eb") == 2 ** 60
    assert check_type_bytes("1zb") == 2 ** 70
    assert check_type_bytes("1yb") == 2 ** 80
    assert check_type_bytes("1Ki") == 1024
    assert check_type_bytes("1Mi") == 2 ** 20
    assert check_type_bytes("1Gi") == 2 ** 30
    assert check_

# Generated at 2022-06-12 23:57:49.662671
# Unit test for function check_required_together
def test_check_required_together():
    good_parameters = {'a':'a1','b':'b1','c':'c1'}
    group1 = ['a', 'b']
    group2 = ['b', 'c']
    terms = [group1,group2]
    assert not check_required_together(terms, good_parameters)
    bad_parameters = {'b':'b1'}
    assert check_required_together(terms, bad_parameters)
    group3 = ['a', 'd']
    group4 = ['a', 'b', 'c']
    terms = [group3,group4]
    bad_parameters = {'a':'a1'}
    assert check_required_together(terms, bad_parameters)

# Generated at 2022-06-12 23:57:56.647507
# Unit test for function safe_eval
def test_safe_eval():
    # method call to a module
    method_call = 'os.system("id")'
    assert safe_eval(method_call) == method_call
    # import statement
    import_statement = 'import os'
    assert safe_eval(import_statement) == import_statement
    # unsafe operation
    assert safe_eval('os.system(1)') == 'os.system(1)'
    # safe operation
    assert safe_eval('2') == 2
    assert safe_eval('False') is False
    assert safe_eval('True') is True
    assert safe_eval('None') is None
    # literal string
    assert safe_eval('"hello"') == 'hello'
    # literal tuple
    assert safe_eval('(1, 2, 3)') == (1, 2, 3)
    # literal list
    assert safe

# Generated at 2022-06-12 23:58:08.288526
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("7") == 7
    assert safe_eval("3.14") == 3.14
    assert safe_eval("'hello'") == 'hello'
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("None") is None
    assert safe_eval("{'x': 1, 'y': 2}") == {'x': 1, 'y': 2}
    assert safe_eval("{1, 2, 3}") == {1, 2, 3}
    assert safe_eval("{1: 'one', 2: 'two'}") == {1: 'one', 2: 'two'}
    assert safe_eval("'func(1)'") == 'func(1)'

# Generated at 2022-06-12 23:58:19.383516
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('1 + 2') == 1 + 2
    assert safe_eval('[1,2]') == [1, 2]
    assert safe_eval('{"a":1}') == {"a": 1}
    assert safe_eval('[1,2]') == [1, 2]
    assert safe_eval('{"a":1}') == {"a": 1}
    assert safe_eval('False == False') == False
    assert safe_eval('True') == True
    assert safe_eval('[1,2] == [1,2]') == [1, 2] == [1, 2]
    assert safe_eval('{"a":1}') == {"a": 1}
    assert safe_eval("'test'.upper()") == "test".upper()
    assert safe_

# Generated at 2022-06-12 23:58:31.575489
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [['test_arg1', 'test_arg2', ('test_arg3', 'test_arg4')]]
    parameters = {'test_arg1': 'test_arg2'}
    try:
        check_required_if(requirements, parameters)
    except Exception as e:
        assert e.results == [{"missing": ["test_arg3", "test_arg4"], "parameter": "test_arg1", "requirements": ("test_arg3", "test_arg4"), "requires": "all", "value": "test_arg2"}]



# Generated at 2022-06-12 23:58:39.386998
# Unit test for function safe_eval
def test_safe_eval():
    # Returns the input unmodified when it is not a string
    assert safe_eval([]) == []
    assert safe_eval(2) == 2
    assert safe_eval(None) is None

    # Returns the input unmodified when it is a string
    assert safe_eval("foo") == "foo"

    # Returns the input unmodified when there are method calls
    assert safe_eval("foo.bar()") == "foo.bar()"

    # Returns the input unmodified when there are imports
    assert safe_eval("import foo") == "import foo"

    # Returns the input unmodified when the expression is invalid
    assert safe_eval("[") == "["
    assert safe_eval('{"foo": "bar"') == '{"foo": "bar"'
    assert safe_eval(',') == ','