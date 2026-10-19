

# Generated at 2022-06-12 23:49:12.992060
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """Test the function check_type_bytes()"""

# Generated at 2022-06-12 23:49:18.197103
# Unit test for function check_required_by
def test_check_required_by():
    from ansible.module_utils import facts
    r1 = {'param_1': ['param_2', 'param_3']}
    p1 = {'param_1': 'a'}
    e1 = "missing parameter(s) required by 'param_1': param_2, param_3"
    o1 = [facts.__name__]
    assert e1 == str(TypeError(check_required_by(r1, p1, o1)))



# Generated at 2022-06-12 23:49:22.734429
# Unit test for function check_required_together
def test_check_required_together():
    # Set up test parameters
    param = {'dummy': 1}
    terms = [['a','b','c'],
             ['dummy'],
             ['e','f']
             ]

    # Call the function
    results = check_required_together(terms, param)



# Generated at 2022-06-12 23:49:27.450552
# Unit test for function check_type_dict
def test_check_type_dict():
    try:
        check_type_dict('')
    except TypeError:
        pass
    else:
        assert False
    try:
        check_type_dict(0)
    except TypeError:
        pass
    else:
        assert False
    try:
        check_type_dict([])
    except TypeError:
        pass
    else:
        assert False
    try:
        check_type_dict('{"key1": "value1"}')
    except TypeError:
        pass
    else:
        assert False
    try:
        check_type_dict('key1="value1"')
    except TypeError:
        pass
    else:
        assert False
    try:
        check_type_dict('key1="value1", key2="value2"')
    except TypeError:
        pass

# Generated at 2022-06-12 23:49:35.951018
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # valid input, no required arguments
    argspec = None
    parameters = None
    options_context = None
    assert check_required_arguments(argspec, parameters, options_context) == []

    # valid input, no required arguments, with context
    options_context = ['foo', 'bar']
    assert check_required_arguments(argspec, parameters, options_context) == []

    # invalid input, no required arguments
    parameters = {'test_param': 'foo'}
    assert check_required_arguments(argspec, parameters, options_context) == []

    # invalid input, required argument missing
    argspec = {'test_param_required': {'required': True}}
    assert check_required_arguments(argspec, parameters, options_context) == ['test_param_required']

    # invalid input, required argument

# Generated at 2022-06-12 23:49:44.548672
# Unit test for function safe_eval
def test_safe_eval():

    e = None
    assert safe_eval('function()') == 'function()'
    assert safe_eval('import os') == 'import os'
    assert safe_eval('3') == 3
    assert safe_eval('False') is False
    assert safe_eval('True') is True
    assert safe_eval('None') is None
    assert safe_eval('ala') == 'ala'
    assert safe_eval('"ala"') == 'ala'
    assert safe_eval('"ala', include_exceptions=True)[0] == '"ala'
    assert isinstance(safe_eval('"ala', include_exceptions=True)[1], SyntaxError)

    try:
        safe_eval('function()')
    except Exception as e:
        assert e is not None

# Generated at 2022-06-12 23:49:54.565095
# Unit test for function check_required_if
def test_check_required_if():
    result_no_error = [
        {
            'parameter': 'someint',
            'value': 99,
            'requirements': ('bool_param', 'string_param'),
            'missing': ['string_param'],
            'requires': 'all',
        }
    ]
    result_error = [
        {
            'parameter': 'someint',
            'value': 99,
            'requirements': ('bool_param', 'string_param'),
            'missing': ['string_param', 'bool_param'],
            'requires': 'all',
        }
    ]
    parameters = {'someint':'99', 'bool_param':'True'}

# Generated at 2022-06-12 23:50:05.305475
# Unit test for function check_required_by
def test_check_required_by():
    parameters = dict()
    requirements = dict()
    result = dict()
    assert check_required_by(requirements, parameters) == result

    parameters = dict(param1='param1', param2='param2')
    requirements = dict(requirement1='param1')
    result = dict()
    assert check_required_by(requirements, parameters) == result

    parameters = dict(param2='param2')
    requirements = dict(requirement1='param1', requirement2=('param1', 'param3'))
    result = dict(requirement1=['param1'], requirement2=['param1'])
    assert check_required_by(requirements, parameters) == result

    parameters = dict(param2='param2')
    requirements = dict(requirement1=['param1', 'param3'])

# Generated at 2022-06-12 23:50:17.269999
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # Test with one term
    assert check_mutually_exclusive(['param'], {'param': 1}) == []
    assert check_mutually_exclusive(['param'], {'other_param': 1}) == []
    # Test with two groups of one term
    assert check_mutually_exclusive(['param', 'other_param'], {'param': 1}) == []
    assert check_mutually_exclusive(['param', 'other_param'], {'other_param': 1}) == []
    assert check_mutually_exclusive(['param', 'other_param'], {'param': 1, 'other_param': 1}) == [['param', 'other_param']]
    # Test with one group of two terms
    assert check_mutually_exclusive([['param', 'other_param']], {'param': 1}) == []


# Generated at 2022-06-12 23:50:27.488035
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert check_mutually_exclusive([['foo', 'bar']], dict(foo='bar')) == []
    assert check_mutually_exclusive(None, dict(foo='bar')) == []
    assert check_mutually_exclusive([['foo', 'bar']], dict(bar='bar', bar1='bar1')) == \
        [['bar', 'bar1']]
    assert check_mutually_exclusive([['foo', 'bar']], dict(foo='bar', bar1='bar', bar2='bar2')) == \
        [['bar', 'bar1']]
    assert check_mutually_exclusive([['foo', 'bar'], ['foo2', 'bar2']], dict(foo='bar', foo2='bar2')) == []

# Generated at 2022-06-12 23:50:44.895770
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    def _check_mutual(terms, parameters, options_context=None, result=None):
        try:
            if result is not None:
                assert False
            else:
                assert True
                check_mutually_exclusive(terms, parameters)
        except TypeError as e:
            assert result == str(e)

    _check_mutual([['one', 'two']], {'one': 1, 'three': 3}, result="parameters are mutually exclusive: one|two")
    _check_mutual([['one', 'two']], {'one': 1, 'two': 2}, options_context=['parent', 'child'],
                  result='parameters are mutually exclusive: one|two found in parent -> child')
    _check_mutual([['one', 'two']], {'one': 1}, result=None)
    _check

# Generated at 2022-06-12 23:50:52.232080
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo") == 'foo'
    assert safe_eval(None) is None
    assert safe_eval(dict(foo='bar')) == dict(foo='bar')
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('[1,2,3, {"a":1, "b":2}]') == [1, 2, 3, {"a": 1, "b": 2}]
    assert safe_eval('1') == 1
    assert safe_eval('1.0') == 1.0
    assert safe_eval('1+1') == 2
    assert safe_eval('1-1') == 0
    assert safe_eval('1*1') == 1
    assert safe_eval('1/1') == 1

# Generated at 2022-06-12 23:51:02.000400
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.basic import AnsibleModule

    def run_module():
        # define available arguments/parameters a user can pass to the module
        fields = {
            "test_string": {"required": False, "type": "str"},
        }

        module = AnsibleModule(argument_spec=fields)
        module.exit_json(changed=False, msg="Argument passed in is %s" % module.params['test_string'])

    module_args = []
    output = ""
    input_value = "foo bar"
    return_value = input_value
    cmd = "ANSIBLE_MODULE_ARGS='{0}'".format(jsonify({"test_string": input_value}))
    rc = 0


# Generated at 2022-06-12 23:51:12.837342
# Unit test for function check_required_if
def test_check_required_if():
    requirement = [
            ['state', 'present', ('path',), True],
            ['someint', 99, ('bool_param', 'string_param')],
        ]
    params = {
        'path':'/path/to/file',
        'someint': 99,
        'bool_param':True,
        'other_param':'other_value'
    }
    # expected error message
    result = """someint is 99 but all of the following are missing: string_param"""
    try:
        check_required_if(requirement, params)
    except TypeError as e:
        assert str(e) == result

    params = {
        'path':'/path/to/file',
        'someint': 99,
        'bool_param':True,
        'string_param':'some_string'
    }

# Generated at 2022-06-12 23:51:22.865051
# Unit test for function check_type_dict
def test_check_type_dict():
    list_value = "this is a string"
    check_list = check_type_dict(list_value)
    assert len(check_list) == 1

    json_value = '{"a": 1, "b": 2}'
    checked_json = check_type_dict(json_value)
    assert len(checked_json) == 2

    key_value = 'a=1, b=2'
    checked_key_value = check_type_dict(key_value)
    assert len(checked_key_value) == 2

    def test_check_type_dict_exceptions():
        value_1 = 3141
        value_2 = '1, 2, 3'
        checked_dict = check_type_dict(value_1)
        checked_dict = check_type_dict(value_2)


#

# Generated at 2022-06-12 23:51:31.537429
# Unit test for function check_required_by
def test_check_required_by():
    requirements = {
        'snapshot_ids': 'snapshot_names',
        'snapshot_names': 'snapshot_ids',
        'volume_id': 'volume_name',
        'volume_name': 'volume_id'
    }
    parameters = {
        'display_name': 'ansible-test-vol',
        'volume_id': 'f8723148-c1a8-11e9-87aa-525400d7db6f',
        'volume_name': 'ansible-test-vol',
        'snapshot_ids': 'f8723148-c1a8-11e9-87aa-525400d7db6f',
        'snapshot_names': 'ansible-test-vol'
    }

# Generated at 2022-06-12 23:51:35.058242
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.six import u
    assert safe_eval(u('{"foo": "bar"}')) == {u('foo'): u('bar')}



# Generated at 2022-06-12 23:51:44.642775
# Unit test for function check_required_if
def test_check_required_if():
    args = ('key', 'val', ('req1', 'req2'))
    # When none of required parameters are present
    params = {'key': 'val'}
    assert check_required_if([args], params)
    # When all of the required parameters are present
    params = {'key': 'val', 'req1': 'a', 'req2': 'b'}
    assert check_required_if([args], params)
    # When only one of required parameters is present
    params = {'key': 'val', 'req1': 'a', 'req2': None}
    assert check_required_if([args], params)
    # When none of required parameters are present, as 'any' type
    params = {'key': 'val'}
    args = ('key', 'val', ('req1', 'req2'), True)

# Generated at 2022-06-12 23:51:50.910095
# Unit test for function check_required_if

# Generated at 2022-06-12 23:51:59.531191
# Unit test for function check_required_if
def test_check_required_if():
    # test for all requirements
    parameters = {'key': 'val', 'path': '/path/to/file', 'state': 'present'}
    requirements = [['state', 'present', ('path',), False]]
    assert check_required_if(requirements, parameters) == []

    # field is not present so no requirements are required
    parameters = {'key': 'val', 'path': '/path/to/file'}
    assert check_required_if(requirements, parameters) == []

    # required field is present and wrong value, so requirements not checked
    parameters = {'key': 'val', 'path': '/path/to/file', 'state': 'absent'}
    assert check_required_if(requirements, parameters) == []

    # required field is absent, raise error

# Generated at 2022-06-12 23:52:14.156624
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('1') == 1
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('1.0') == 1.0
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('[1, [2, 3]]') == [1, [2, 3]]
    assert safe_eval("dict(a='1', b=2)") == dict(a='1', b=2)
    assert safe_eval("dict(a=1, b='2')") == dict(a=1, b='2')

# Generated at 2022-06-12 23:52:24.736929
# Unit test for function check_required_together
def test_check_required_together():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.parsing.convert_bool import boolean

    # A list of lists or tuples
    terms = [
        ('a', 'b'),
        ('c', 'd')
    ]
    # A dictionary of parameters
    parameters = dict()

    parameters['a'] = '1'
    parameters['b'] = '2'
    parameters['c'] = '3'
    parameters['d'] = '4'

    result = check_required_together(terms=terms, parameters=parameters)
    assert result == []

    parameters['a'] = '1'
    parameters['b'] = '2'
    parameters['c'] = '3'
    del parameters['d']


# Generated at 2022-06-12 23:52:29.275888
# Unit test for function check_required_together
def test_check_required_together():
    terms = [('name', 'state'), ('force', 'src'), ('dest', 'newest')]
    parameters = dict(name='example', state='present', newest=True, force=True)
    check_required_together(terms, parameters)

    parameters = dict(name='example', state='present', newest=True)
    try:
        check_required_together(terms, parameters)
    except TypeError:
        pass
    else:
        assert False #TypeError not raised as expected


# Generated at 2022-06-12 23:52:35.336683
# Unit test for function check_type_dict
def test_check_type_dict():
    # Test case 1
    value = "{'1':2,'2':3}"
    expected_result = {'1': 2, '2': 3}
    assert check_type_dict(value) == expected_result
    # Test case 2
    value = "1=2,2=3"
    expected_result = {'1': '2', '2': '3'}
    assert check_type_dict(value) == expected_result
    # Test case 3
    value = {'1':2}
    expected_result = {'1': 2}
    assert check_type_dict(value) == expected_result
    # Test case 4
    value = "'1':2"
    expected_result = {'1': 2}
    try:
        check_type_dict(value)
    except TypeError:
        assert True

# Generated at 2022-06-12 23:52:45.301340
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("10B") == 10
    assert check_type_bytes("10K") == 10*1024
    assert check_type_bytes("10M") == 10*1024*1024
    assert check_type_bytes("10G") == 10*1024*1024*1024
    assert check_type_bytes("5m") == 5*1024*1024
    assert check_type_bytes("5M") == 5*1024*1024
    assert check_type_bytes("5G") == 5*1024*1024*1024
    assert check_type_bytes("5T") == 5*1024*1024*1024*1024
    assert check_type_bytes("5PB") == 5*1024*1024*1024*1024*1024
    assert check_type_bytes("5EB") == 5*1024*1024*1024*1024*1024*1024
    assert check

# Generated at 2022-06-12 23:52:54.282067
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert check_mutually_exclusive(["a", "b"], dict(a=1, b=2)) == ["a", "b"]
    assert check_mutually_exclusive([["a", "b"]], dict(a=1)) == []
    assert check_mutually_exclusive([["a", "b"]], dict(a=1, b=2)) == [["a", "b"]]
    assert check_mutually_exclusive([["a", "b"]], dict(a=1, b=2, c=3), ["e", "f"]) == [["a", "b"]]



# Generated at 2022-06-12 23:52:59.130691
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('a=1, b=2') == {'a': '1', 'b': '2'}
    assert check_type_dict('a=1, b=2, c=3') == {'a': '1', 'b': '2', 'c': '3'}
    assert check_type_dict('a=1, b="foo,bar", c=3') == {'a': '1', 'b': 'foo,bar', 'c': '3'}
    assert check_type_dict('a=1, b="foobar", c=3') == {'a': '1', 'b': 'foobar', 'c': '3'}

# Generated at 2022-06-12 23:53:06.694946
# Unit test for function check_required_together
def test_check_required_together():
    try:
        check_required_together([('a', 'b'), (1, 2)], {'a':1, 'b':2})
    except TypeError as e:
        assert "found" in str(e)
    else:
        assert False, "TypeError not thrown"
    try:
        check_required_together([('a', 'b'), (1, 2)], {'a':1, 'b':2, 1:1, 2:2})
    except TypeError as e:
        assert "found" in str(e)
    else:
        assert False, "TypeError not thrown"

# Generated at 2022-06-12 23:53:10.299075
# Unit test for function check_type_bits
def test_check_type_bits():
    try:
        assert check_type_bits('1Mb') == 1048576
        assert check_type_bits('2048b') == 2048
        assert check_type_bits('1.25Mb') == 1280000
    except TypeError:
        raise TypeError('value can not be converted to a Bit value')
    except AssertionError:
        raise AssertionError('value is not converted to a Bit value')



# Generated at 2022-06-12 23:53:10.987969
# Unit test for function check_required_together
def test_check_required_together():
    pass



# Generated at 2022-06-12 23:53:21.491674
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    parameters = dict(
        param1='value1',
        param3='value3'
    )
    required_parameters = ['param1', 'param2', 'param3']
    missing_params = check_missing_parameters(parameters, required_parameters)
    assert missing_params == ['param2']


# Generated at 2022-06-12 23:53:29.546947
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("10") == 10
    assert check_type_bytes("10 b") == 10
    assert check_type_bytes("1k") == 1024
    assert check_type_bytes("1kb") == 1024
    assert check_type_bytes("1M") == 1048576
    assert check_type_bytes("1MB") == 1048576
    assert check_type_bytes("1g") == 1073741824
    assert check_type_bytes("1gb") == 1073741824
    assert check_type_bytes(0) == 0
    assert check_type_bytes(1) == 1
    assert check_type_bytes(1024) == 1024
    assert check_type_bytes(1048576) == 1048576



# Generated at 2022-06-12 23:53:40.043431
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1,"foo"]') == [1, "foo"]
    assert safe_eval("{'a': 1}") == {'a': 1}
    assert safe_eval("1") == 1
    assert safe_eval("1.5") == 1.5
    assert safe_eval("False") == False
    assert safe_eval("True") == True
    assert safe_eval("None") is None
    assert safe_eval("'sekretz'") == 'sekretz'
    assert safe_eval("'1'") == '1'
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo["bar"]') == 'foo["bar"]'
    assert safe_eval('foo.bar()') == 'foo.bar()'



# Generated at 2022-06-12 23:53:48.485426
# Unit test for function safe_eval
def test_safe_eval():
    # value is not string
    assert safe_eval(10) == 10

    # value is '10'
    assert safe_eval('10') == 10

    # value is '10.5'
    assert safe_eval('10.5') == 10.5

    # value is '-10.5'
    assert safe_eval('-10.5') == -10.5

    # value is '10'
    assert safe_eval('True') is True

    # value is '"10"'
    assert safe_eval('"10"') == '10'

    # expression is not supported
    assert safe_eval('os.path') == 'os.path'

    # unsupported binary operations
    assert safe_eval('1 < 2 > 3') == '1 < 2 > 3'

    # unsupported unary operators

# Generated at 2022-06-12 23:53:57.393559
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    assert [] == check_missing_parameters(dict(), [])
    assert [] == check_missing_parameters(dict(a=1), [])
    assert [] == check_missing_parameters(dict(a=1), ['a'])
    assert ['b'] == check_missing_parameters(dict(a=1), ['a', 'b'])
    assert [] == check_missing_parameters(dict(a=1), 'a')
    assert ['b'] == check_missing_parameters(dict(a=1), ['a', 'b'])



# Generated at 2022-06-12 23:54:07.416664
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # Check for error when a single mutex group is passed in and two values are non-null
    terms = ['a', 'b']
    parameters = {'a': 'foo', 'b': 'bar'}
    options_context = None
    try:
        check_mutually_exclusive(terms,parameters, options_context)
    except TypeError as e:
        assert to_native(e) == "parameters are mutually exclusive: a|b found in a -> b"

    # Check for no error when a single mutex group is passed in and one value is null
    terms = ['a', 'b']
    parameters = {'a': 'foo', 'b': None}
    options_context = None
    check_mutually_exclusive(terms, parameters, options_context)

    # Check for no error when a two mutex subgroups are passed

# Generated at 2022-06-12 23:54:18.559063
# Unit test for function check_required_if
def test_check_required_if():
    assert [] == check_required_if(None, {})
    assert [] == check_required_if([], {})
    assert [] == check_required_if([['foo', 'bar', ('baz',)]], {'foo': 'foo'})
    assert [] == check_required_if([['foo', 'bar', ('baz',)]], {'foo': 'bar'})
    assert [] == check_required_if([['foo', 'bar', ('baz',)]], {'foo': 'baz'})
    assert [] == check_required_if([['foo', 'bar', ('baz',)]], {'foo': 'bar', 'baz': 'baz'})

# Generated at 2022-06-12 23:54:24.962316
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(5.6) == 5.6
    assert check_type_float(5) == 5.0
    assert check_type_float('5') == 5.0
    assert check_type_float('5.6') == 5.6
    assert check_type_float(b'5.6') == 5.6
    # FIXME:  Python 2.6 does not support Unicode input
    #assert check_type_float(u'5.6') == 5.6



# Generated at 2022-06-12 23:54:32.915442
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo", None) == "foo"
    assert safe_eval("foo.bar()", None) == "foo.bar()"
    assert safe_eval("import datetime", None) == "import datetime"
    assert safe_eval("1 + 2", None) == 3
    assert safe_eval("int('1')", None) == 1
    assert safe_eval("[1, 2, 3]", None) == [1, 2, 3]
    assert safe_eval("'foo'", None) == 'foo'



# Generated at 2022-06-12 23:54:40.609604
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('''"This is a test"''') == "This is a test"
    assert safe_eval('''"This is a 'test'"''') == "This is a 'test'"
    assert safe_eval('''"This is a \"test\""''') == 'This is a "test"'
    assert safe_eval('''''"This is a \'test\'"''') == "This is a 'test'"
    assert safe_eval('''"This is a \"\"\"test\"\"\""''') == 'This is a """test"""'
    assert safe_eval('''"This is a \'\'\'test\'\'\'"''') == "This is a '''test'''"

# Generated at 2022-06-12 23:54:53.902059
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1Tb') == 1099511627776
    assert check_type_bits('1Pb') == 1125899906842624
    assert check_type_bits('1Eb') == 1152921504606846976
    assert check_type_bits('1Zb') == 1180591620717411303424
    assert check_type_bits('1Yb') == 1208925819614629174706176

# Generated at 2022-06-12 23:54:58.632895
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1Kb') == 1024
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Gb') == 1073741824



# Generated at 2022-06-12 23:55:09.097562
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """ Test function check_type_bytes"""
    try:
        check_type_bytes('1G')
    except TypeError as exp:
        msg = "wrong bytes conversion 1G"
        assert msg in str(exp), "Expected failure message not found in '%s' " % str(exp)
    try:
        check_type_bytes('1g')
    except TypeError as exp:
        msg = "wrong bytes conversion 1g"
        assert msg in str(exp), "Expected failure message not found in '%s' " % str(exp)
    try:
        check_type_bytes('1')
    except TypeError as exp:
        msg = "wrong bytes conversion 1"
        assert msg in str(exp), "Expected failure message not found in '%s' " % str(exp)

# Generated at 2022-06-12 23:55:12.193538
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1mb') == 1048576
    assert check_type_bits('1 Mb') == 1048576
    assert check_type_bits(1) == 1



# Generated at 2022-06-12 23:55:23.556510
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """Check the check_type_bytes function.
    """
    assert check_type_bytes('1b') == 1
    assert check_type_bytes('1') == 1
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1kb') == 1024
    assert check_type_bytes('1m') == 1024 * 1024
    assert check_type_bytes('1mb') == 1024 * 1024
    assert check_type_bytes('1G') == 1024 * 1024 * 1024
    assert check_type_bytes('1gb') == 1024 * 1024 * 1024
    assert check_type_bytes('1T') == 1024 * 1024 * 1024 * 1024
    assert check_type_bytes('1tb') == 1024 * 1024 * 1024 * 1024

# Generated at 2022-06-12 23:55:34.928943
# Unit test for function check_required_together
def test_check_required_together():
    module = MockModule()
    terms = [('a', 'b')]
    parameters = {'a': 1, 'b': 2}
    try:
        check_required_together(terms, parameters)
    except Exception as e:
        raise AssertionError('check_required_together should not raise an exception: %s' % e)

    try:
        check_required_together(terms, {'a': 1})
    except TypeError as e:
        if 'parameters are required together' not in e.args[0]:
            raise AssertionError('check_required_together should raise a TypeError exception with the correct message')
    except Exception as e:
        raise AssertionError('check_required_together should raise a TypeError exception: %s' % e)

    # Include a non-zero count element with no argument
   

# Generated at 2022-06-12 23:55:42.816006
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(10) == 10
    assert check_type_bytes(u'10') == 10
    assert check_type_bytes('10') == 10
    assert check_type_bytes(u'10Ki') == 10240
    assert check_type_bytes('10Ki') == 10240
    assert check_type_bytes('1Mi') == 1048576
    assert check_type_bytes('1Gi') == 1073741824
    assert check_type_bytes('1Ti') == 1099511627776


# Generated at 2022-06-12 23:55:50.705341
# Unit test for function check_type_dict
def test_check_type_dict():
    # Test empty
    check_type_dict('')
    # Test json
    check_type_dict('{}')
    check_type_dict('{ "a": "b"}')
    check_type_dict('{"a": "b"}')
    # Test yaml
    check_type_dict('{a: "b"}')
    check_type_dict('a: b')
    check_type_dict('a: b\nc: d')
    # Test list of comma separated key value pairs
    check_type_dict('a:b, c:d')
    check_type_dict('a:b,c:d')
    # Test list of comma separated key value pairs with spaces around the delimiter
    check_type_dict('a : b, c : d')

# Generated at 2022-06-12 23:55:55.121203
# Unit test for function check_type_int
def test_check_type_int():
    '''Test case for function check_type_int'''
    try:
        assert check_type_int('12') == 12
        assert check_type_int(12) == 12
        assert check_type_int(-12) == -12
    except Exception:
        raise AssertionError


# Generated at 2022-06-12 23:56:02.718732
# Unit test for function check_required_by
def test_check_required_by():
    # input data
    requirements = {
        'param4': ['param1', 'param2', 'param3'],
        'param5': ['param6', 'param7']
    }
    parameters = {
        'param1': 'hello',
        'param2': 'world',
        'param3': 'there',
        'param4': 'friend'
    }
    # expected output data
    exp_result = {
        'param4': []
    }
    # run unit test
    result = check_required_by(requirements=requirements, parameters=parameters)
    assert exp_result == result, "error"



# Generated at 2022-06-12 23:56:15.241957
# Unit test for function check_required_one_of
def test_check_required_one_of():
    required_one_of = check_required_one_of
    terms = [['name', 'tag'], ['name', 'key_material']]
    assert not required_one_of(terms, {'name': 'test'})
    assert required_one_of(terms, {'not_name': 'test'})
    terms = [['name', 'key_material'], ['region', 'endpoint']]
    assert not required_one_of(terms, {'endpoint': 'http://unittest.com'})
    assert not required_one_of(terms, {'region': 'us-east-1'})
    assert not required_one_of(terms, {'endpoint': 'http://unittest.com', 'region': 'us-east-1'})

# Generated at 2022-06-12 23:56:23.744295
# Unit test for function check_required_by
def test_check_required_by():
    test_cases = [
        ({"a": "b"}, {"a": "", "b": "b"}, {}),
        ({"a": "b"}, {"a": ""}, {"a": ["b"]}),
        ({"a": ["b", "c"]}, {"a": ""}, {"a": ["b", "c"]}),
        ({"a": "b", "c": "d"}, {"a": "", "b": "b", "d": "d"}, {"c": ["d"]}),
    ]
    for test_case in test_cases:
        assert test_case[2] == check_required_by(test_case[0], test_case[1])


# Generated at 2022-06-12 23:56:33.292306
# Unit test for function check_required_if
def test_check_required_if():
    try:
        check_required_if([['state', 'present', ('path',)]])
        raise TypeError("Expected TypeError")
    except TypeError as e:
        pass
    try:
        check_required_if([[]])
        raise TypeError("Expected TypeError")
    except TypeError as e:
        pass
    try:
        check_required_if([['state', 'present', ('path',)], ['someint', 99, ('bool_param', 'string_param')]])
        raise TypeError("Expected TypeError")
    except TypeError as e:
        pass
    check_required_if([['state', 'present', ('path',), True], ['someint', 99, ('bool_param', 'string_param')]])

# Generated at 2022-06-12 23:56:41.031943
# Unit test for function check_required_by
def test_check_required_by():
    parameters = {'a':'1', 'b':'2', 'd':'4'}
    requirements = {'a': 'b'}
    check_required_by(requirements, parameters)
    requirements = {'a': 'b', 'b': 'd'}
    assert check_required_by(requirements, parameters) == {'b': ['d']}
    requirements = {'a': ['b']}
    check_required_by(requirements, parameters)
    requirements = {'a': ['b', 'c', 'd']}
    assert check_required_by(requirements, parameters) == {'a': ['c']}



# Generated at 2022-06-12 23:56:51.237823
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """Check the check_type_bytes function"""
    from ansible.compat.tests.mock import patch
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.validation import check_type_bytes

    # check_type_bytes should return the same value as a bytes conversion for known byte values
    assert isinstance(check_type_bytes(to_bytes('0')), bytes)
    assert check_type_bytes(to_bytes('1')) == to_bytes('1')
    assert check_type_bytes(to_bytes('1k')) == to_bytes(1*1024)
    assert check_type_bytes(to_bytes('1m')) == to_bytes(1*1024*1024)
    assert check_type_bytes

# Generated at 2022-06-12 23:57:00.694875
# Unit test for function check_required_together
def test_check_required_together():
    parameters={"a":1,"b":2}
    terms=["a","b","c","d"]
    result=check_required_together(terms,parameters)
    assert result==[]
    terms=["a","b","c","d","e"]
    result=check_required_together(terms,parameters)
    assert result==[]
    terms=["a","b","e","f","g"]
    result=check_required_together(terms,parameters)
    assert result==[]
    parameters={"a":"b","c":"d","e":"f"}
    terms=["a","b","c","d","e"]
    result=check_required_together(terms,parameters)
    assert result==[]
    parameters={"a":"b","c":"d","e":"f"}

# Generated at 2022-06-12 23:57:05.381314
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert check_mutually_exclusive(["foo"], {"foo": "bar"})
    assert check_mutually_exclusive([["foo"]], {"foo": "bar"})
    assert check_mutually_exclusive(["foo"], {"foo": "bar"}) == []
    assert check_mutually_exclusive([["foo", "bar"]], {"foo": "bar"}) == []
    assert check_mutually_exclusive([["foo", "bar"]], {"foo": "bar", "bar": "baz"}) == [["foo", "bar"]]

    try:
        check_mutually_exclusive(None, {"foo": "bar"})
    except TypeError as e:
        assert not isinstance(e, AnsibleUnsafeText)


# Generated at 2022-06-12 23:57:16.257461
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1024') == 1024
    assert check_type_bytes('1k') == 1024
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1m') == 1048576
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1g') == 1073741824
    assert check_type_bytes('1G') == 1073741824
    assert check_type_bytes('1t') == 1099511627776
    assert check_type_bytes('1T') == 1099511627776
    assert check_type_bytes('1p') == 1125899906842624
    assert check_type_bytes('1P') == 1125899906842624
    assert check_type_bytes('1e') == 1152921504

# Generated at 2022-06-12 23:57:20.450400
# Unit test for function check_required_one_of
def test_check_required_one_of():
    #Test: No conflict
    result = check_required_one_of(["a","b"],{"a":1,"b":2})
    assert len(result) == 0
    #Test: Conflict
    try:
        check_required_one_of(["a","b"],{})
        assert False
    except ValueError as e:
        assert "one of the following is required: a, b" == str(e)
    except Exception as e:
        assert False



# Generated at 2022-06-12 23:57:22.087084
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    result = check_mutually_exclusive([['a', 'b']], {'a': 1, 'c': 2})
    assert result == []



# Generated at 2022-06-12 23:57:28.241466
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    with pytest.raises(TypeError):
        check_type_bits('1M')



# Generated at 2022-06-12 23:57:32.260093
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """Unit test for function check_type_bytes"""
    from ansible.module_utils import basic
    ansible = basic.AnsibleModule({})
    # test for exact string
    assert check_type_bytes('1024') == 1024, 'Failed to return bytes value for exact string.'
    # test for string with whitespace
    assert check_type_bytes('  1024  ') == 1024, 'Failed to return bytes value for string with whitespace.'
    # test for string with unit
    assert check_type_bytes('1 MB') == 1048576, 'Failed to return bytes value for string with unit.'
    # test for string with unit and whitespace
    assert check_type_bytes('  1 MB  ') == 1048576, 'Failed to return bytes value for string with unit and whitespace.'
    # test for invalid string
   

# Generated at 2022-06-12 23:57:35.371494
# Unit test for function check_type_int
def test_check_type_int():
    sample_int = 1
    sample_str = '1'
    sample_bool = False
    sample_list = ['1']
    assert (check_type_int(sample_int) == 1)
    assert (check_type_int(sample_str) == 1)
    try:
        check_type_int(sample_bool)
    except TypeError:
        assert (check_type_int(sample_bool) is None)
    try:
        check_type_int(sample_list)
    except TypeError:
        assert (check_type_int(sample_list) is None)


# Generated at 2022-06-12 23:57:43.238127
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{"foo": "bar"}') == {'foo': 'bar'}
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('{}') == {}
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('6') == 6
    assert safe_eval('"foobar"') == 'foobar'

    assert safe_eval('[{"foo": "bar"}]', include_exceptions=True) == ([{'foo': 'bar'}], None)
    assert safe_eval('True', include_exceptions=True) == (True, None)
    assert safe_eval('False', include_exceptions=True) == (False, None)

# Generated at 2022-06-12 23:57:48.490836
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    terms = [['test-key', 'test-key2'], ['test-key3', 'test-key4']]
    parameters = {'test-key': 'test', 'test-key2': 'test2'}
    options_context = ['tst-key', 'tst-key2']

    check_mutually_exclusive(terms, parameters, options_context)



# Generated at 2022-06-12 23:57:50.175673
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float('1') == 1.0
    assert check_type_float('1.0') == 1.0
# End of unit test


# Generated at 2022-06-12 23:57:56.934359
# Unit test for function check_required_by
def test_check_required_by():
    return_value = check_required_by(requirements={"key1":"value1", "key2":"value2", "key3":"value3"}, parameters={"key1":"value1", "key2":"value2", "key3":"value3"})
    assert return_value == {}
    return_value = check_required_by(requirements={"key1":"value1", "key2":"value2", "key3":"value3"}, parameters={"key1":"value1", "key2":"value2"})
    assert return_value == {'key3': []}
    return_value = check_required_by(requirements={"key1":"value1", "key2":{"key4":"value4"}}, parameters={"key1":"value1", "key2":"value2", "key3":"value3"})

# Generated at 2022-06-12 23:58:00.449663
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1TB') == 1073741824000
    assert_raises(TypeError, check_type_bytes, '')
    assert_raises(TypeError, check_type_bytes, None)



# Generated at 2022-06-12 23:58:10.932344
# Unit test for function check_type_bits

# Generated at 2022-06-12 23:58:21.203318
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'foo': {'required': True},
        'bar': {'required': False},
        'bam': {'required': False},
        'object': {'required': True, 'type': 'dict'},
        'number_of_objects': {'required': True, 'type': 'list'},
        'deep_object': {'required': True, 'type': 'dict', 'options': {'foo': {'required': True}}}
    }
    parameters = {'foo': 'foovalue'}
    options_context = ['object']

    with raises(TypeError) as e:
        check_required_arguments(argument_spec, parameters, options_context=options_context)

    result = e.value.args[0]

# Generated at 2022-06-12 23:58:29.317993
# Unit test for function check_type_bytes
def test_check_type_bytes():
    try:
        ctb = check_type_bytes('128M')
        assert ctb == 134217728
    except TypeError:
        pass


# FIXME: This needs to be expanded to cover more conversion cases

# Generated at 2022-06-12 23:58:35.483856
# Unit test for function check_type_bytes
def test_check_type_bytes():
    tests = (
        ('50M', 52428800),
        ('50G', 53687091200),
        ('50', 50),
        (50, 50),
        (125, 125),
        ('1024', 1024),
        ('0.5K', 512),
        ('1.6G', 17179869184),
    )
    for value, expected in tests:
        result = check_type_bytes(value)
        assert result == expected

