

# Generated at 2022-06-12 23:48:52.543537
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    assert check_missing_parameters({'name': 'example', 'force': False}, ['name', 'force']) == []
    assert check_missing_parameters({'name': 'example'}, ['name', 'force']) == ['force']
    assert check_missing_parameters({'name': 'example', 'state': 'present'}, ['name', 'force']) == ['force']


# Generated at 2022-06-12 23:49:03.154902
# Unit test for function check_required_by
def test_check_required_by():
    options = {
        'one': '2',
        'two': '3',
        'three': '4',
        'four': '5',
    }
    requirements = {
        'one': 'two',
        'three': ['four', 'five'],
    }
    host = {}
    result = check_required_by(requirements, options)
    assert result == {
        'three': ['five'],
    }

    # should fail when 'one' is required
    requirements = {
        'one': 'two',
    }
    host = {}
    try:
        check_required_by(requirements, options)
        raise AssertionError("Expected check_required_by to raise an exception")
    except TypeError:
        pass

    # should succeed when 'one' is required

# Generated at 2022-06-12 23:49:11.690772
# Unit test for function check_type_dict
def test_check_type_dict():
    def assert_dict(expected, value):
        assert expected == check_type_dict(value)

    assert_dict(dict(a=1, b=2, c=3), '{"a":1,"b":2,"c":3}')
    assert_dict(dict(a=1, b=2, c=3), 'a=1, b=2, c=3')
    assert_dict(dict(a=1, b=2, c=3), 'a=1,b=2,c=3')
    assert_dict(dict(a=1, b=2, c=3), 'a=1,b=2,c=3')
    assert_dict(dict(a=1, b='a,b=c'), 'a=1,b=\'a,b=c\'')

# Generated at 2022-06-12 23:49:18.798860
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(float(99)) == float(99)
    assert check_type_float(99) == float(99)
    assert check_type_float("99") == float(99)
    assert check_type_float(b"99") == float(99)
    assert check_type_float("99.1") == float(99.1)
    assert check_type_float("99.1e5") == float(99.1e5)
    assert check_type_float("99.1e-5") == float(99.1e-5)


# Generated at 2022-06-12 23:49:22.030059
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    try:
        check_mutually_exclusive(["a", "b", "c"], {"a": True, "b": True})
        assert False, "Should have thrown exception"
    except TypeError:
        pass



# Generated at 2022-06-12 23:49:29.711536
# Unit test for function check_required_together
def test_check_required_together():
    for parameters in [dict(a=1, b=2), dict(a=1, c=2)]:
        c = check_required_together([['a', 'b'], ['a', 'c']], parameters)
        assert not c

    # test missing fields
    for parameters in [dict(a=1), dict(a=1, b=2)]:
        c = check_required_together([['a', 'b'], ['a', 'c']], parameters)
        assert c



# Generated at 2022-06-12 23:49:36.483356
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert check_mutually_exclusive(terms=None, parameters=None) is [], "check_mutually_exclusive should return an empty list when parameters is None"
    assert check_mutually_exclusive(terms=[['a', 'b', 'c']], parameters={'a': 'test', 'b': 'test', 'c': 'test'}) == [['a', 'b', 'c']], "check_mutually_exclusive should return the list of mutually exclusive terms when 3 terms are found in parameters"
    assert check_mutually_exclusive(terms=['a', 'b', 'c'], parameters={'a': 'test', 'b': 'test', 'c': 'test'}) == [], "check_mutually_exclusive should not return anything when none of the terms apply"



# Generated at 2022-06-12 23:49:44.766902
# Unit test for function check_required_by
def test_check_required_by():
    d = dict()
    d['a'] = 'aaaaaaaaaa'
    d['b'] = 'bbbbbbbbbb'
    d['c'] = 'cccccccccc'
    d['d'] = 'dddddddddd'
    d['e'] = 'eeeeeeeeee'
    d['f'] = 'ffffffffff'
    requirements = dict()
    requirements['a'] = 'c'
    requirements['b'] = 'd'
    requirements['c'] = 'd'
    requirements['d'] = 'e'
    requirements['e'] = 'f'
    requirements['f'] = 'g'
    #Test when value is missing
    try:
        check_required_by(requirements, d)
    except SystemExit as e:
        assert e.code == 1
    #Test when value is passed


# Generated at 2022-06-12 23:49:54.603703
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    answer = {}
    # Testing for the single list
    terms = ['name', 'type']
    parameters = {'name': 'hello', 'type': 'world', 'attr': 'value'}
    assert check_mutually_exclusive(terms, parameters) == []

    # Testing for multiple parameters that are mutually exclusive
    terms = [['name', 'type'], ['attr', 'attr2']]
    parameters = {'name': 'hello', 'type': 'world', 'attr': 'value'}
    try:
        assert check_mutually_exclusive(terms, parameters)
    except TypeError as e:
        answer['msg'] = to_native(e)
        answer['failed'] = True

    assert answer['msg'] == "parameters are mutually exclusive: name|type, attr|attr2"
    assert answer['failed'] is True



# Generated at 2022-06-12 23:50:05.306027
# Unit test for function check_type_dict
def test_check_type_dict():
    from ansible.module_utils.basic import dict_from_items_or_equals

    assert {'a': '2', 'c': '3', 'b': '1'} == check_type_dict("a=2, b=1, c=3")
    assert {'a': '2', 'c': '3', 'b': '1'} == check_type_dict("a=2, b=1, c=3 ")
    assert {'a': '2', 'c': '3', 'b': '1'} == check_type_dict("a=2, b=1, c=3 ")
    assert {'a': '2', 'c': '3', 'b': '1'} == check_type_dict("a=2, b=1, c=3  ")

# Generated at 2022-06-12 23:50:23.871880
# Unit test for function check_required_arguments
def test_check_required_arguments():
    from ansible.module_utils.basic import AnsibleModule
    argument_spec = {'hostname': {'required': True},
                     'password': {},
                     'port': {'required': True, 'default': 8080},
                     'username': {'required': True}}
    module = AnsibleModule(argument_spec=argument_spec)
    missing = check_required_arguments(argument_spec, module.params)

    assert missing == ['username', 'hostname'], "Missing parameters: %s" % missing

# Generated at 2022-06-12 23:50:31.561280
# Unit test for function check_required_if
def test_check_required_if():
    try:
        check_required_if(requirements=[
            ['state', 'present', ('path',), True],
            ['someint', 99, ('bool_param', 'string_param')],
        ], parameters={'state': 'present'})
    except TypeError as e:
        assert e.args[0] == "missing required arguments: path"
    try:
        check_required_if(requirements=[
            ['state', 'present', ('path',), True],
            ['someint', 99, ('bool_param', 'string_param')],
        ], parameters={'someint': 99, 'bool_param': False})
    except TypeError as e:
        assert e.args[0] == "string_param is required"

# Generated at 2022-06-12 23:50:41.976589
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('"test"') == 'test'
    assert safe_eval('["test","test"]') == ['test', 'test']
    assert safe_eval('{"a":"test","b":"test"}') == {'a': 'test', 'b': 'test'}
    assert safe_eval('1') == 1
    assert safe_eval('-1') == -1
    assert safe_eval('{"a":1,"b":2}') == {'a': 1, 'b': 2}
    assert safe_eval('{"a":-1,"b":-2}') == {'a': -1, 'b': -2}
    assert safe_eval('[1,2]') == [1, 2]

# Generated at 2022-06-12 23:50:44.184113
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = dict(
        a=dict(required=True),
        b=dict(required=True),
        c=dict(),
    )
    parameters = dict(
        a=1,
    )
    missing = check_required_arguments(argument_spec, parameters, options_context=None)
    assert set(missing) == set(['b'])


# Generated at 2022-06-12 23:50:54.287828
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments({'a': {}}, {}) == ['a']
    assert check_required_arguments({'a': {'required': True}}, {}) == ['a']
    assert check_required_arguments({'a': {'required': False}}, {}) == []
    assert check_required_arguments({'a': {}}, {'a': None}) == []
    assert check_required_arguments({'a': {'required': True}}, {'a': None}) == []
    assert check_required_arguments({'a': {'required': False}}, {'a': None}) == []
    assert check_required_arguments({'a': {'required': True}}, {'a': True}) == []

# Generated at 2022-06-12 23:50:58.892676
# Unit test for function check_type_dict
def test_check_type_dict():
    test_values = dict(
        dict_string='{"key_1": "val_1"}',
        string_equals='key_1=val_1',
        json_string='{"key_1": "val_1", "key_2": "val_2"}',
        complex_json_string="""{
            "key_1":"val_1",
            "key_2":"val_2",
            "key_3":{
                "key_4":"val_4"
            },
            "key_5":[
                {
                    "key_6": "val_6"
                },
                {
                    "key_7":"val_7"
                }
            ]
        }"""
    )

# Generated at 2022-06-12 23:51:09.636138
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'required_str': {'required': True, 'type': 'str'},
        'avaliable_str': {'required': False, 'type': 'str'},
        'required_list': {'required': True, 'type': 'list'},
        'avaliable_list': {'required': False, 'type': 'list'}
    }

    # missing required parameters
    parameters = {
        'avaliable_str': 'avaliable_str',
        'avaliable_list': ['avaliable_list'],
    }
    missing = check_required_arguments(argument_spec, parameters)

    assert len(missing) == 2
    assert missing == ['required_str', 'required_list']

    # missing one required parameter

# Generated at 2022-06-12 23:51:20.224760
# Unit test for function check_type_dict
def test_check_type_dict():
    # Test with a dict
    test_dict = {'key1': 'value1', 'key2': 'value2'}
    result = check_type_dict(test_dict)
    assert result == test_dict

    # Test with a string with key1=value1,key2=value2
    test_string = 'key1=value1,key2=value2'
    result = check_type_dict(test_string)
    assert result == {'key1': 'value1', 'key2': 'value2'}

    # Test with a string with key1=value1,key2=value2,key3="value3, value4"
    test_string = 'key1=value1,key2=value2,key3="value3, value4"'
    result = check_type_dict(test_string)


# Generated at 2022-06-12 23:51:28.443120
# Unit test for function safe_eval

# Generated at 2022-06-12 23:51:36.354891
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(1) == 1
    # String with single-character suffix
    assert check_type_bytes('1K') == 1024
    # String with multi-character suffix
    assert check_type_bytes('1M') == 1048576
    # String with multi-character suffix and space
    assert check_type_bytes('1 M') == 1048576
    # String with large value and multi-character suffix
    assert check_type_bytes('1234M') == 1271607296
    # String with value with decimal point
    assert check_type_bytes('1.5M') == 1572864
    # String with value with large decimal point
    assert check_type_bytes('1.599999999999M') == 16777216
    # String with value with decimal point and space

# Generated at 2022-06-12 23:51:53.428180
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float('0.0') == 0.0
    assert check_type_float(0.0) == 0.0
    assert check_type_float(0) == 0.0
    assert check_type_float(b'0.0') == 0.0
    return



# Generated at 2022-06-12 23:52:04.130285
# Unit test for function check_required_arguments

# Generated at 2022-06-12 23:52:11.234505
# Unit test for function check_required_if
def test_check_required_if():
    params = dict()
    res = list()
    list = [['key1', 'val1', ('key2', 'key3'), True], ['key2', 'val2', ('key1', 'key3'), False]]
    res.append(check_required_if(list, params))
    if res:
        print("check_required_if test failed")
    else:
        print("check_required_if test passed")
test_check_required_if()



# Generated at 2022-06-12 23:52:20.893196
# Unit test for function check_required_one_of
def test_check_required_one_of():
    """Unit test for function check_required_one_of"""
    assert check_required_one_of(None, {}) == []
    with pytest.raises(TypeError):
        check_required_one_of([], {}, options_context=['options_1'])
    with pytest.raises(TypeError):
        check_required_one_of([['a']], {}, options_context=['options_1'])
    with pytest.raises(TypeError):
        assert check_required_one_of([['a', 'b']], {'c': 'd'}, options_context=['options_1'])
    assert check_required_one_of([['a', 'b']], {'a': 'd'}, options_context=['options_1']) is None



# Generated at 2022-06-12 23:52:23.222283
# Unit test for function check_required_together
def test_check_required_together():
    parameters = ["param1", "param2", "param3"]
    terms = ["param1", "param2"]
    check_required_together(terms, parameters)



# Generated at 2022-06-12 23:52:31.218056
# Unit test for function check_required_together
def test_check_required_together():
    from ansible.module_utils.common.text.converters import to_bytes
    """
    :param spec_exists_params:
    :return:
    """
    # Test case one:
    spec_exists_params = [('location', 'container'), ('location', 'container', 'blob')]
    # Test case two:
    spec_not_exists_params = [('location', 'container'), ('location', 'blob')]
    # Test case three:
    spec_empty_params = []
    specs_not_exist_params_list = [spec_exists_params, spec_not_exists_params, spec_empty_params]

# Generated at 2022-06-12 23:52:42.518011
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}
    assert safe_eval("(1,2,3)") == (1, 2, 3)
    assert safe_eval("1") == 1
    assert safe_eval("1.1") == 1.1
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("None") is None

    assert safe_eval("[1,2,3", include_exceptions=True) == ([1, 2, 3], None)

    test_str = 'Some random string here'
    assert safe_eval(test_str, include_exceptions=True) == (test_str, None)



# Generated at 2022-06-12 23:52:47.376862
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('2 + 3') == 5
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"a": 1}') == {u'a': 1}
    assert safe_eval('import os') == 'import os'
    assert safe_eval('os.path') == 'os.path'
    assert safe_eval('os.path()') == 'os.path()'
    assert safe_eval('(2 + 3) * 4') == 20



# Generated at 2022-06-12 23:52:56.977306
# Unit test for function check_required_together
def test_check_required_together():
    input_data = [
        # format:    [positive test case, negative test case],
        (['a', 'b'],  ({'a': 'yes', 'b': 'yes'}, {'a': 'yes'})),
        (['a', 'b'],  ({'a': 'yes', 'b': 'yes'}, {'b': 'yes'})),
    ]

    for term, test_cases in input_data:
        for positive_case, negative_case in test_cases:
            assert check_required_together([term], positive_case) == []
            try:
                check_required_together([term], negative_case)
            except TypeError:
                pass
            else:
                assert False, "TypeError not raised"



# Generated at 2022-06-12 23:53:02.045131
# Unit test for function check_required_together
def test_check_required_together():
    try:
        assert check_required_together([['test', 'test1'], ['test2', 'test3']], {'test': 0, 'test1': 0}, ['test', 'test1']) is None
    except TypeError:
        raise AssertionError("check_required_together([['test', 'test1'], ['test2', 'test3']], {'test': 0, 'test1': 0}) hasn't passed.")


# Generated at 2022-06-12 23:53:20.761150
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("{'a': 1}") == {'a': 1}
    assert safe_eval("1") == 1
    assert safe_eval("{'a': 1}", include_exceptions=True) == ({'a': 1}, None)
    assert safe_eval("{'a': 1}").__class__.__name__ == 'dict'
    assert safe_eval("1", include_exceptions=True) == (1, None)
    assert safe_eval("1").__class__.__name__ == 'int'
    assert safe_eval("'1'", include_exceptions=True) == ('1', None)
    assert safe_eval("'1'").__class__.__name__ == 'str'
    assert safe_eval("a").__class__.__name__ == 'str'
    assert safe_

# Generated at 2022-06-12 23:53:29.454795
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    import ansible.module_utils as module_utils
    from ansible.module_utils.basic import AnsibleModule
    from copy import deepcopy

    def test_params(term, param, options_context, is_valid):
        assert is_valid == (len(module_utils.common.check_mutually_exclusive(term, param, options_context)) == 0)


# Generated at 2022-06-12 23:53:40.326029
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():

    # Dummy definition to test check_mutually_exclusive
    def _get_argument_spec():
        return dict(
            mutually_exclusive=(
                ['a', 'b'],
                [['b', 'c']]
            ),
            mutually_exclusive_with_options=(
                ['a', 'b'],
                [['b', 'c']]
            ),
            mutually_exclusive_custom=(
                ['b', 'c'],
            ),
        )

    def _get_argument_spec_no_mutual_exclusives():
        return dict()

    # Testing when mutually exclusive parameters are not found
    assert [] == check_mutually_exclusive(None, dict(a=1))
    assert [] == check_mutually_exclusive(None, dict(a=1, c=3))
    assert [] == check_mutually

# Generated at 2022-06-12 23:53:48.717088
# Unit test for function check_type_dict
def test_check_type_dict():
    dict_value = check_type_dict({'key1': 'val1'})
    assert isinstance(dict_value, dict)
    dict_value = check_type_dict('key1=val1')
    assert dict_value['key1'] == 'val1'
    dict_value = check_type_dict('key1=val1,key2=val2')
    assert dict_value['key1'] == 'val1'
    assert dict_value['key2'] == 'val2'
    dict_value = check_type_dict('key1= "val1", key2= "val2", key3= { "key4": 123 }')
    assert dict_value['key1'] == "val1"
    assert dict_value['key2'] == "val2"

# Generated at 2022-06-12 23:54:00.038084
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('None') is None
    assert safe_eval('False') is False
    assert safe_eval('"wibble"') == 'wibble'
    assert safe_eval("{'a': 5, 'b': 6, 'c': 7}") == {'a': 5, 'b': 6, 'c': 7}
    assert safe_eval("['a', 'b', 'c']") == ['a', 'b', 'c']
    assert safe_eval("['a', ['b', {'c': 7}]]") == ['a', ['b', {'c': 7}]]

# Generated at 2022-06-12 23:54:10.124706
# Unit test for function check_type_dict
def test_check_type_dict():
    def make_test_case(value, expected_result):
        return (value, expected_result)

    # test cases

# Generated at 2022-06-12 23:54:16.846399
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(5.5) == 5.5
    assert check_type_float("5.5") == 5.5
    assert check_type_float("5") == 5.0
    assert check_type_float(b"5.5") == 5.5
    assert check_type_float(5) == 5.0
# EOF test_check_type_float



# Generated at 2022-06-12 23:54:18.420343
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("100m") == 104857600


# Generated at 2022-06-12 23:54:25.680951
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    simple_terms = ['a', 'b']
    multiple_terms = [['a', 'b'], ['c', 'd']]
    options_context = ['foo', 'bar']
    parameters = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # expect no error to be raised
    check_mutually_exclusive(simple_terms, parameters)


# Generated at 2022-06-12 23:54:30.103707
# Unit test for function check_type_bits
def test_check_type_bits():
    x=check_type_bits('1Mb')
    assert x==1048576, "Assertion failed"
    print ("Testing is done")
test_check_type_bits()



# Generated at 2022-06-12 23:54:40.818112
# Unit test for function check_required_together
def test_check_required_together():
    spec = dict(
        check_required_together=dict(
            type='list',
            elements='str',
            required_together=[['red', 'blue'], ['green', 'yellow']]
        ),
        color=dict(
            type='str',
            choices=['red', 'blue', 'green', 'yellow', 'black', 'white']
        )
    )

    valid_params = dict(
        color='red',
        check_required_together=['one']
    )

    invalid_params = dict(
        color='red'
    )

    assert check_required_together(spec['check_required_together']['required_together'], valid_params) == [], "valid_params passed to check_required_together function"

# Generated at 2022-06-12 23:54:47.615689
# Unit test for function check_type_int
def test_check_type_int():
    check_type_int(1)
    check_type_int(1.4)
    check_type_int('2')
    check_type_int('3.5')
    check_type_int(True)
    check_type_int(False)

    try:
        check_type_int('a')
        raise Exception('check_type_int did not raise TypeError')
    except TypeError:
        pass

    try:
        check_type_int({})
        raise Exception('check_type_int did not raise TypeError')
    except TypeError:
        pass



# Generated at 2022-06-12 23:54:49.120588
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576



# Generated at 2022-06-12 23:54:56.994791
# Unit test for function check_required_together
def test_check_required_together():
    params = {"a": 1, "b": 2, "c": 3}
    res = check_required_together([("a", "b", "c"), ("a", "b")], params)
    assert res == []
    with pytest.raises(TypeError) as exc:
        check_required_together([("a", "b", "c"), ("a", "d")], params)
    assert "required" in str(exc.value)



# Generated at 2022-06-12 23:55:07.765838
# Unit test for function safe_eval
def test_safe_eval():

    # existing_var = "foo"
    assert safe_eval('existing_var') == 'existing_var'
    assert safe_eval('"{{ existing_var }}"') == '{{ existing_var }}'

    # 1.1
    assert safe_eval('1.1') == 1.1

    # 1
    assert safe_eval('1') == 1

    # "foo"
    assert safe_eval('"foo"') == "foo"

    # ['a', 'b']
    assert safe_eval("['a', 'b']") == ['a', 'b']

    # {'a': 'b'}
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}

    # None
    assert safe_eval("None") is None

    # True

# Generated at 2022-06-12 23:55:18.723702
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("None") is None
    assert safe_eval("'some string'") == "some string"
    assert safe_eval("some_string") == "some_string"
    assert safe_eval("{'key': 'value'}") == {'key': 'value'}
    # Test failures
    assert safe_eval("{key: 'value'}") == "{key: 'value'}"
    assert safe_eval("import os") == "import os"
    assert safe_eval("os.getpid()") == "os.getpid()"
    assert safe_eval("{1:2, 3:4}") == "{1:2, 3:4}"



# Generated at 2022-06-12 23:55:29.033279
# Unit test for function check_type_int
def test_check_type_int():
    """Test that check_type_int() works as expected
    """
    test_int = 23
    test_string = "23"
    test_string_float = "23.5"
    test_list = [1,2,3]

    assert check_type_int(test_int) == 23
    assert check_type_int(test_string) == 23
    try:
        check_type_int(test_string_float)
    except AssertionError:
        assert True
    except Exception:
        assert False
    try:
        check_type_int(test_list)
    except AssertionError:
        assert True
    except Exception:
        assert False



# Generated at 2022-06-12 23:55:39.791463
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
        ['someint', 99, ('bool_param', 'string_param', 'other')],
        ['other', 'present', ('bool_param',), True],
    ]
    parameters = {'state': 'present', 'other': 'present', 'bool_param': 'yes', 'string_param': 'foo'}
    assert check_required_if(requirements, parameters) == []
    parameters['other'] = 'absent'
    try:
        check_required_if(requirements, parameters)
    except TypeError as e:
        results = e.args[0]
    assert len(results) == 2

# Generated at 2022-06-12 23:55:42.227568
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    for test_string in ['|'.join(check) for check in results]:
        assert re.search("parameters are mutually exclusive: IP address, MAC address", msg)


# Generated at 2022-06-12 23:55:52.649289
# Unit test for function check_type_bits

# Generated at 2022-06-12 23:56:06.165391
# Unit test for function check_required_by
def test_check_required_by():
    p = dict(b=1, d=1, f=1, h=1, j=1, l=1)
    r = dict(a=['b', 'd', 'f', 'g'], c=['h', 'j'], e=['l', 'm'])
    assert check_required_by(r, p) == dict(a=['g'], c=[], e=['m'])



# Generated at 2022-06-12 23:56:14.912125
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1+1") == 2
    assert safe_eval("'1+1'") == '1+1'
    assert safe_eval("'1+1'", include_exceptions=True) == ('1+1', None)
    assert safe_eval("[1,2,3]") == [1,2,3]
    assert safe_eval("{'a':1, 'b':2, 'c':3}") == {'a':1, 'b':2, 'c':3}
    assert safe_eval("1+1", include_exceptions=True) == (2, None)
    assert safe_eval("1+1", locals=dict(one=1)) == 2
    assert safe_eval("one+1", locals=dict(one=1)) == 2
    assert safe_eval("import os")

# Generated at 2022-06-12 23:56:21.465340
# Unit test for function safe_eval
def test_safe_eval():
    good_value = '{{ ((1 + 1) * 3) / 2}}'
    bad_value = '{{ ((1 + 1) * 3) / 2}'
    bad_val2 = '{{ true if 1 else false }}'
    assert safe_eval(good_value) == '3'
    assert safe_eval(bad_value) == bad_value
    assert safe_eval(bad_val2) == bad_val2


# Generated at 2022-06-12 23:56:32.088329
# Unit test for function check_type_dict
def test_check_type_dict():
    assert {'key1': 'val1', 'key2': 'val2'} == check_type_dict("key1=val1,key2=val2")
    assert {'key1': 'val1', 'key2': 'val2'} == check_type_dict("key1='val1',key2=val2")
    assert {'key1': 'val1', 'key2': 'val2'} == check_type_dict("key1='val1',key2='val2'")
    assert {'key1': 'val1', 'key2': 'val2'} == check_type_dict("'key1'='val1','key2'='val2'")

# Generated at 2022-06-12 23:56:41.454203
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments(None, {}, []) == []
    assert check_required_arguments({'a': {'required': True}}, {'a': None}, []) == []
    assert check_required_arguments({'a': {'required': False}}, {'a': None}, []) == []
    assert check_required_arguments({'a': {'required': True}}, {}, []) == ['a']
    assert check_required_arguments({'a': {'required': False}}, {}, []) == []
    assert check_required_arguments({'a': {'required': False}, 'b': {'required': True}}, {'a': None}, []) == []

# Generated at 2022-06-12 23:56:51.994661
# Unit test for function safe_eval
def test_safe_eval():
    # Non-strings return themselves
    assert safe_eval(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert safe_eval(('a', 'b', 'c')) == ('a', 'b', 'c')
    assert safe_eval({'a': 'b', 'c': 'd'}) == {'a': 'b', 'c': 'd'}
    assert safe_eval(1) == 1
    assert safe_eval(1.1) == 1.1
    # Strings that are recognized literals are returned as the literal value
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("None") is None
    assert safe_eval("['a', 'b', 'c']") == ['a', 'b', 'c']


# Generated at 2022-06-12 23:56:54.505910
# Unit test for function check_type_bits
def test_check_type_bits():
    assert(check_type_bits('1Mb') == 1048576)
    assert(check_type_bits('1Mb') != '1048576')



# Generated at 2022-06-12 23:57:02.651731
# Unit test for function check_required_arguments
def test_check_required_arguments():
    spec = {
        'one': {'required': True},
        'two': {'required': True},
        'three': {'required': False},
        'four': {'required': True},
    }
    params = {'two': 2, 'four': 4}
    assert check_required_arguments(spec, params) == []
    params = {'one': 1, 'two': 2, 'three': 3}
    assert check_required_arguments(spec, params) == []
    params = {'two': 2, 'four': 4, 'five': 5}
    assert check_required_arguments(spec, params) == ['one']
    params = {'three': 3}
    assert check_required_arguments(spec, params) == ['one', 'two', 'four']



# Generated at 2022-06-12 23:57:13.911051
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1,2,3]') == [1,2,3]
    assert safe_eval('{"a":1}') == {"a":1}
    assert safe_eval('1') == 1
    assert safe_eval('1.0') == 1.0
    assert safe_eval('None') is None
    assert safe_eval('[1, 2, 3]')
    assert safe_eval('{"a":1}')
    assert safe_eval('True')
    assert safe_eval('"a"')
    assert safe_eval(u'[1, 2, 3]')
    assert safe_eval(u'{"a":1}')
    assert safe_eval(u'"a"')

# Generated at 2022-06-12 23:57:16.633798
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int('0') == 0
    assert check_type_int(1) == 1
    with pytest.raises(TypeError):
        check_type_int('a')


# Generated at 2022-06-12 23:57:23.895091
# Unit test for function check_type_float
def test_check_type_float():
    for v in ['1',1.0,1,1.2]:
        try:
            check_type_float(v)
        except TypeError as e:
            print('TypeError:%s' %e)
    try:
        check_type_float('hello')
    except TypeError as e:
        print('TypeError:%s' %e)


# Generated at 2022-06-12 23:57:30.454761
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('a:b, c:d') == dict(a= "b", c= "d")
    assert check_type_dict('a:"b, c"') == dict(a= "b, c")
    assert check_type_dict('a:b, c:d') == dict(a= "b", c= "d")
    assert check_type_dict('a:b, c:d') == dict(a= "b", c= "d")
    assert check_type_dict({"a": "b"}) == dict(a= "b")
    assert check_type_dict('{a:b}') == dict(a= "b")
    assert check_type_dict('a:b c:d') == dict(a= "b")


# Generated at 2022-06-12 23:57:40.558438
# Unit test for function check_required_by
def test_check_required_by():
    # scenario 1: no requirements at all
    requirements = None
    parameters = {'param1': True}
    assert {} == check_required_by(requirements, parameters)
    
    # scenario 2: no required parameter for current parameter
    requirements = {'param1':None, 'param2':None}
    parameters = {'param1': True}
    assert {} == check_required_by(requirements, parameters)
    # scenario 3: current parameter is not specified
    requirements = {'param1':['param2'], 'param2':None}
    parameters = {'param2': True}
    assert {} == check_required_by(requirements, parameters)
    # scenario 4: current parameter exists
    requirements = {'param1':['param2', 'param3'], 'param2':None, 'param3':None}
    parameters

# Generated at 2022-06-12 23:57:50.854682
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Simple required
    argument_spec = {
        "test": {"required": True},
        "test2": {"required": True, "type": "list"},
    }
    missing = check_required_arguments(argument_spec, {"test2": []})
    assert missing == ["test"], missing

    # Missing required argument
    argument_spec["test2"]["required"] = False
    missing = check_required_arguments(argument_spec, {})
    assert missing == ["test"], missing

    # No required argument
    argument_spec["test2"]["required"] = False
    argument_spec["test"]["required"] = False
    missing = check_required_arguments(argument_spec, {})
    assert not missing, missing

    # with options_context

# Generated at 2022-06-12 23:58:03.764870
# Unit test for function check_type_bits
def test_check_type_bits():
    # test for valid cases
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Mib') == 1048576
    assert check_type_bits('1MB') == 1048576
    assert check_type_bits('1MiB') == 1048576
    assert check_type_bits('1MB') == 1048576
    assert check_type_bits('1M') == 8388608
    assert check_type_bits('1m') == 1048576
    assert check_type_bits('1mib') == 1048576
    # test for invalid cases
    try:
        check_type_bits('1')
        assert False
    except TypeError:
        assert True



# Generated at 2022-06-12 23:58:12.562152
# Unit test for function check_required_arguments
def test_check_required_arguments():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.text.formatters import to_native

    def fail(params):
        try:
            check_required_arguments(spec, params)
        except Exception as e:
            return to_native(e)
        return None

    spec = {
        'a': {'required': True},
        'b': {'required': True},
        'c': {'required': False}
    }

    assert fail({}) == "missing required arguments: a, b"
    assert fail({'b': True}) == "missing required arguments: a"
    assert fail({'a': True}) == "missing required arguments: b"
    assert fail({'b': True, 'c': True}) == "missing required arguments: a"

# Generated at 2022-06-12 23:58:13.103579
# Unit test for function check_required_by
def test_check_required_by():
    pass



# Generated at 2022-06-12 23:58:16.280449
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits(10.0) == 10
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('100') == 100


# Generated at 2022-06-12 23:58:24.675829
# Unit test for function check_type_bits
def test_check_type_bits():
    expect_return = human_to_bytes('1Mb', isbits=True)
    assert check_type_bits('1Mb') == expect_return

# Mapping of AnsibleModule params to check type function
CHECK_TYPE_MAP = {
    'str': check_type_str,
    'list': check_type_list,
    'dict': check_type_dict,
    'bool': check_type_bool,
    'int': check_type_int,
    'float': check_type_float,
    'path': check_type_path,
    'raw': check_type_raw,
    'bytes': check_type_bytes,
    'bits': check_type_bits,
}



# Generated at 2022-06-12 23:58:28.351285
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('100') == 100
    try:
        check_type_bytes('100K')
        assert False
    except TypeError:
        assert True

