

# Generated at 2022-06-12 23:49:29.840852
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [['state', 'present', ('path',), True], ['someint', 99, ('bool_param', 'string_param')]]
    parameters = {'state': 'present', 'path': '/etc'}
    result = check_required_if(requirements, parameters)
    assert not result
    parameters = {'state': 'absent'}
    result = check_required_if(requirements, parameters)
    assert not result
    parameters = {'someint': 99}
    result = check_required_if(requirements, parameters)
    assert len(result) == 1
    assert result[0]['requires'] == 'all'
    assert result[0]['parameter'] == 'someint'
    assert result[0]['value'] == 99
    assert 'bool_param' in result[0]['missing']
   

# Generated at 2022-06-12 23:49:40.193992
# Unit test for function check_required_if
def test_check_required_if():
    parameter_list = {'key1':None,'key2':None, 'key3': None, 'key4': None}
    # test value
    requirements = []
    requirements.append(('key1','test1','key2'))
    requirements.append(('key4','test4','key1','key2','key3', False))
    #test all
    requirements.append(('key4','test4','key1','key2','key3', True))

    # test fail
    requirements.append(['key1', 'test1', 'key3'])
    requirements.append(['key1', 'test1', 'key2', 'key3'])
    requirements.append(['key1', 'test1', ['key2', 'key3']])

# Generated at 2022-06-12 23:49:50.882493
# Unit test for function check_required_if
def test_check_required_if():
    """Unit tests for :func:`_module_utils.basic.check_required_if`"""
    # Check required_if with requirements having any of the parameters
    # Check with presents of parameter 'state' and parameter 'path'
    requirements = [['state', 'present', ('path',), True]]
    parameters = {'state': 'present', 'path': '/tmp/file'}
    assert check_required_if(requirements, parameters) == []
    # Check with presents of parameter 'state' and absent of parameter 'path'
    requirements = [['state', 'present', ('path',), True]]
    parameters = {'state': 'present'}
    assert check_required_if(requirements, parameters) == []
    # Check with absent of parameter 'state' and absent of parameter 'path'

# Generated at 2022-06-12 23:50:00.736221
# Unit test for function check_type_dict
def test_check_type_dict():
    #check positive test case
    assert {'key': 'value'} == check_type_dict('key=value')
    assert {'key': 'value', 'key1': 'value1'} == check_type_dict('key=value,key1=value1')
    assert {'key': 'value=value1'} == check_type_dict('key="value=value1"')
    assert {'key': 'value'} == check_type_dict('key="value"')
    assert {'key': 'value'} == check_type_dict('key=\'value\'')
    assert {'key': 'value\\'} == check_type_dict('key="value\\\\"')
    assert {'key': 'value\\'} == check_type_dict('key=\'value\\\\\'')

# Generated at 2022-06-12 23:50:07.231404
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        "name": {"required": True},
        "version": {"required": False}
    }

    parameters = {"name": "test"}
    try:
        check_required_arguments(argument_spec, parameters)
    except TypeError as e:
        pass
    else:
        assert False, "required parameter check failed"

    parameters = {
        "name": "test",
        "version": "1.0"
    }
    try:
        check_required_arguments(argument_spec, parameters)
    except TypeError as e:
        assert False, "required parameter check should have passed"



# Generated at 2022-06-12 23:50:15.958113
# Unit test for function check_required_together
def test_check_required_together():
    terms_1 = [['a', 'b'], ['c', 'd', 'e']]
    parameters_1 = {'a': 'a', 'b': 'b', 'e': 'e'}
    assert check_required_together(terms_1,parameters_1) == []

    terms_2 = [['a', 'b'], ['c', 'd', 'e']]
    parameters_2 = {'a': 'a', 'e': 'e'}
    assert check_required_together(terms_2,parameters_2) != []



# Generated at 2022-06-12 23:50:27.161532
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('10M') == 10485760
    assert check_type_bytes('10KB') == 10240
    assert check_type_bytes('10kiB') == 10240
    assert check_type_bytes('10Kib') == 10240
    assert check_type_bytes('10kB') == 10000
    assert check_type_bytes('10MB') == 10000000
    assert check_type_bytes('10GB') == 10000000000
    assert check_type_bytes('10TB') == 10000000000000
    assert check_type_bytes('10PB') == 10000000000000000
    assert check_type_bytes('10EB') == 1000000000000000000
    assert check_type_bytes('10ZB') == 1000000000000000000000
    assert check_type_bytes('10YB') == 1000000000000000000000000

# Generated at 2022-06-12 23:50:39.568999
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'a1': {'required': True},
        'a2': {'required': True},
        'a3': {}
    }
    # test success
    parameters = {'a1': 'a1value'}
    missing = check_required_arguments(argument_spec, parameters)
    assert sorted(missing) == []
    parameters = {'a1': 'a1value', 'a2': 'a2value'}
    missing = check_required_arguments(argument_spec, parameters)
    assert sorted(missing) == []
    parameters = {'a1': 'a1value', 'a3': 'a3value'}
    missing = check_required_arguments(argument_spec, parameters)
    assert sorted(missing) == []
    # test fail
    parameters = {}
    missing

# Generated at 2022-06-12 23:50:48.139414
# Unit test for function check_required_by
def test_check_required_by():

    options = dict(name='foo',
                   state='present',
                   src='/foo/bar',
                   owner='root',
                   group='root')
    requirements = dict(src=['owner', 'group'],
                        owner=['group'])

    assert check_required_by(requirements, options) == {}

    options = dict(name='foo',
                   state='present',
                   src='/foo/bar',
                   owner='root')

    assert check_required_by(requirements, options) == {'src': ['group']}



# Generated at 2022-06-12 23:50:59.932339
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Check empty argument_spec and parameters
    # Expecting an empty list to be returned
    assert check_required_arguments({}, {}) == []

    # Check argument_spec with value required and the parameter present
    # Expecting an empty list to be returned
    assert check_required_arguments({"name": {"required": True}}, {"name": "foo"}) == []

    # Check argument_spec with value required and the parameter not present
    # Expecting a TypeError to be raised
    try:
        check_required_arguments({"name": {"required": True}}, {})
    except TypeError as e:
        assert "missing required arguments: name" in str(e)

    # Check argument_spec with value required and the parameter not present
    # Expecting a TypeError to be raised

# Generated at 2022-06-12 23:51:07.709186
# Unit test for function check_required_arguments
def test_check_required_arguments():
    parameter_spec = {
        'foo': {'required': True},
        'bar': {'required': False},
        'baz': {'required': True}
    }
    parameters = {
        'foo': 'something',
        'bar': 'something else'
    }
    result = check_required_arguments(parameter_spec, parameters)
    assert result == ['baz']



# Generated at 2022-06-12 23:51:12.936189
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    module = type('', (object,), {
        'params': {
            'one': 1,
            'two': 2,
            'three': 3,
        },
    })
    check = (['one', 'two', 'three'], )
    # With no mutually exclusive parameters, it should just return an empty list
    assert check_mutually_exclusive(check, module.params) == []

    module.params['two'] = 4
    # With one set of mutually exclusive parameters, it should raise an error
    try:
        check_mutually_exclusive(check, module.params)
    except TypeError as err:
        assert to_native(err) == 'parameters are mutually exclusive: one|two|three'
    else:
        assert False, 'Expected TypeError was not raised'

    # With multiple sets of mutually exclusive parameters,

# Generated at 2022-06-12 23:51:22.946296
# Unit test for function check_required_by
def test_check_required_by():
    assert check_required_by(None, None) == {}
    assert check_required_by({"key": "value"}, {}) == {}
    assert check_required_by({"key": "value"}, {"key": "value"}) == {}
    assert check_required_by({"key": "value"}, {"key": "value", "value": None}) == {}
    assert check_required_by({"key": "value"}, {"key": "value", "other_key": "other_value"}) == {}
    assert check_required_by({"key": "value"}, {"key": "value", "value": None, "other_key": "other_value"}) == {}

# Generated at 2022-06-12 23:51:31.619209
# Unit test for function safe_eval
def test_safe_eval():
    # Test string
    test_string = "string "
    # Test list
    test_list = ["string", 2, 3]
    # Test tuple
    test_tuple = ("string", 2, 3)
    # Test set
    test_set = {"string", 2, 3}
    # Test dict
    test_dict = {"a": 1, "b": 2}
    # Test boolean
    test_bool = bool(test_string)
    # Test int
    test_int = 1

    # Test safe_eval on string
    assert safe_eval(test_string) == "string "
    # Test safe_eval on list
    assert safe_eval(test_list) == ["string", 2, 3]
    # Test safe_eval on tuple
    assert safe_eval(test_tuple) == ("string", 2, 3)

# Generated at 2022-06-12 23:51:42.155148
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.errors import AnsibleFilterError

# Generated at 2022-06-12 23:51:45.924958
# Unit test for function check_type_bytes
def test_check_type_bytes():
    # test bytes string without any conversion
    assert check_type_bytes('0b') == 0
    # test bytes string with conversion
    assert check_type_bytes('1kb') == 1024


# Generated at 2022-06-12 23:51:56.435969
# Unit test for function safe_eval
def test_safe_eval():
    error = False
    # test for method calls
    res = safe_eval("test.test()")
    if res == "test.test()":
        print("Method call test, PASSED")
    else:
        print("Method call test, FAILED")
        error = True
    # test for imports
    res = safe_eval("import test")
    if res == "import test":
        print("Import test, PASSED")
    else:
        print("Import test, FAILED")
        error = True
    # test for valid data structures
    res = safe_eval('["test", "test", "test"]')
    if res == ["test", "test", "test"]:
        print("Valid data structure test, PASSED")
    else:
        print("Valid data structure test, FAILED")
        error = True


# Generated at 2022-06-12 23:52:07.149083
# Unit test for function safe_eval
def test_safe_eval():
    # Example 1
    value = "foobar"
    result = safe_eval(value)
    assert result == "foobar"

    # Example 2
    value = "'foobar'"
    result = safe_eval(value)
    assert result == "foobar"

    # Example 3
    value = "12345"
    result = safe_eval(value)
    assert result == 12345

    # Example 4
    value = "12345.6789"
    result = safe_eval(value)
    assert result == 12345.6789

    # Example 5
    value = "False"
    result = safe_eval(value)
    assert result is False

    # Example 6
    value = "True"
    result = safe_eval(value)
    assert result is True

    # Example 7
    value = "true"
   

# Generated at 2022-06-12 23:52:18.138093
# Unit test for function check_type_dict
def test_check_type_dict():
    try:
        check_type_dict({'a':1,'b':2,'c':3})
    except TypeError:
        assert False
    try:
        check_type_dict('{"a":1,"b":2,"c":3}')
    except TypeError:
        assert False
    try:
        check_type_dict('{"a":1, "b":2, "c":3')
    except TypeError:
        assert True
    try:
        check_type_dict('a=1, b=2, c=3')
    except TypeError:
        assert False
    try:
        check_type_dict('a1 b2 c3')
    except TypeError:
        assert True

# Generated at 2022-06-12 23:52:27.622721
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1024') == 1024
    assert check_type_bytes('1024k') == 1024000
    assert check_type_bytes('1k') == 1000
    assert check_type_bytes('2M') == 2000000
    assert check_type_bytes('2m') == 2000000
    assert check_type_bytes('1M') == 1000000
    assert check_type_bytes('-20k') == -20000
    assert check_type_bytes('-20K') == -20000
    assert check_type_bytes('-20m') == -2000000
    assert check_type_bytes('-20M') == -2000000
    assert check_type_bytes('2g') == 2000000000
    assert check_type_bytes('2G') == 2000000000
    assert check_type_bytes('20') == 20
   

# Generated at 2022-06-12 23:52:42.561786
# Unit test for function check_type_bits
def test_check_type_bits():
    # Valid test cases
    assert check_type_bits("1Gb") == 1073741824
    assert check_type_bits("1Mb") == 1048576
    assert check_type_bits("1Kb") == 1024
    assert check_type_bits("1b") == 1
    # Invalid test cases
    try:
        check_type_bits("1Gb1")
    except TypeError:
        pass
    else:
        assert False, "check_type_bits failed to catch invalid bits value"
    try:
        check_type_bits("1MbMb")
    except TypeError:
        pass
    else:
        assert False, "check_type_bits failed to catch invalid bits value"
    try:
        check_type_bits("1MbGb")
    except TypeError:
        pass

# Generated at 2022-06-12 23:52:54.281822
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('-1') == -1
    assert safe_eval('1') == 1
    assert safe_eval('-1.0') == -1.0
    assert safe_eval('1.0') == 1.0
    assert safe_eval('True') is True
    assert safe_eval('false') is False
    assert safe_eval('true') is True
    assert safe_eval('[1, 2]') == [1, 2]
    assert safe_eval('{1: 2}') == {1: 2}
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('import foo') == 'import foo'
    assert safe_eval('foo: bar') == 'foo: bar'

# Generated at 2022-06-12 23:53:01.616021
# Unit test for function check_mutually_exclusive

# Generated at 2022-06-12 23:53:06.473495
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1M') == 1048576
    assert check_type_bits('1Mb/s') == 1048576
    assert check_type_bits('1M/s') == 1048576
    assert check_type_bits('1M') == 1048576
    assert check_type_bits('1Mbit') == 1048576
    assert check_type_bits('1Mbit/s') == 1048576
    assert check_type_bits('1Mbit/sec') == 1048576
    assert check_type_bits('1Mbit/second') == 1048576
    assert check_type_bits('1Mbit/seconds') == 1048576
    assert check_type_bits('1Mb/sec') == 1048576
   

# Generated at 2022-06-12 23:53:11.128093
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int('1') == 1
    try:
        check_type_int('a')
        assert False
    except TypeError:
        assert True


# Generated at 2022-06-12 23:53:21.212465
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    """Unit test for function check_missing_parameters"""

    parameters = {'arg1': 'value1', 'arg2': 'value2', 'arg3': 'value3'}
    required_params = ['arg1', 'arg2', 'arg3']
    assert(check_missing_parameters(parameters, required_params) == [])
    required_params = ['arg1', 'arg3']
    assert(check_missing_parameters(parameters, required_params) == [])
    required_params = ['arg1', 'arg2', 'arg3', 'arg4']
    try:
        check_missing_parameters(parameters, required_params)
    except TypeError as e:
        assert(e.args[0] == "missing required arguments: arg4")

# Generated at 2022-06-12 23:53:29.893009
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """ test for ansible.module_utils.basic.check_type_bytes """
    assert(check_type_bytes('10B') == 10)
    assert(check_type_bytes('10.5B') == 10)
    assert(check_type_bytes('10KB') == 10 * 1024)
    assert(check_type_bytes('10MB') == 10 * 1024 * 1024)
    assert(check_type_bytes('10GB') == 10 * 1024 * 1024 * 1024)
    assert(check_type_bytes('10TB') == 10 * 1024 * 1024 * 1024 * 1024)
    assert(check_type_bytes('10PB') == 10 * 1024 * 1024 * 1024 * 1024 * 1024)
    assert(check_type_bytes('10EB') == 10 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024)

# Generated at 2022-06-12 23:53:37.251919
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1M') == 1048576
    assert check_type_bits('1Mib') == 1048576
    with pytest.raises(TypeError):
        check_type_bits('1Mibb')
    with pytest.raises(TypeError):
        check_type_bits('1Mbib')
    with pytest.raises(TypeError):
        check_type_bits('1Mbb')



# Generated at 2022-06-12 23:53:37.863849
# Unit test for function check_required_by
def test_check_required_by():
    pass



# Generated at 2022-06-12 23:53:41.917296
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int('500') == 500
    assert check_type_int(500) == 500
    try:
        check_type_int('banana')
    except TypeError:
        pass
    else:
        assert False, 'check_type_int() should raise TypeError'


# Generated at 2022-06-12 23:53:55.714949
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    from collections import namedtuple
    from ansible.utils.hashing import checksum_s
    assert check_mutually_exclusive(terms=None, parameters={'hello': 'world'}) == []

    with pytest.raises(TypeError) as exec_info:
        check_mutually_exclusive(terms=['hello', 'world'], parameters={'hello': 'world', 'world': 'hello'})
    assert 'parameters are mutually exclusive: hello|world' in str(exec_info.value)

    assert check_mutually_exclusive(terms=['hello', 'world'], parameters={'hello': 'world'}) == []

    check_data = namedtuple('check', ['terms', 'parameters'])

# Generated at 2022-06-12 23:54:06.005701
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # test for function check_mutually_exclusive.
    # Create a module object for testing
    params = {'name': 'module_name', 'choice': ['foo', 'bar']}
    module = type('module', (object,), params)
    # Mutually exclusive groups defined
    mutually_exclusive = [['name', 'choice']]
    # test when there is no mutually exclusive match
    result = check_mutually_exclusive(mutually_exclusive, module.__dict__)
    assert result == []
    # test when there is a mutually exclusive match
    params = {'name': 'module_name', 'choice': ['foo', 'bar']}
    module = type('module', (object,), params)
    result = check_mutually_exclusive(mutually_exclusive, module.__dict__)
    assert type(result).__name__

# Generated at 2022-06-12 23:54:15.784232
# Unit test for function check_required_if
def test_check_required_if():
    """Unit tests for ansible.module_utils.basic.check_required_if"""
    # Tests for function, test_check_required_if
    # Return the results of the parameter requirements check
    #   (list of dicts with keys 'parameter', 'value', 'missing',
    #    'requirements', 'requires')
    # Case 1:
    #   check_required_if parameter requirements is None
    #   expect:
    #       []
    assert check_required_if(None, dict()) == []
    # Case 2:
    #   check_required_if parameter requirement is list of
    #   ['key', val, ['req1', 'req2']]
    #   expect:
    #       [{'parameter': 'key',
    #         'value': val,
    #         'requirements': ['req1

# Generated at 2022-06-12 23:54:20.963904
# Unit test for function check_type_dict
def test_check_type_dict():
    # sample input
    input_string = "{'one':1,'two':2,'three':3}"
    test_dict = check_type_dict(input_string)
    # check if value is convertable to dict

# Generated at 2022-06-12 23:54:25.734619
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    parameters = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    params = [["one", "two"], ["three", "four", "five", "six"]]
    try:
        check_mutually_exclusive(params, parameters)
        assert False
    except TypeError:
        assert True



# Generated at 2022-06-12 23:54:35.281890
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('123 b') == 123
    assert check_type_bytes('123 kb') == 125000
    assert check_type_bytes('123 mb') == 125000000
    assert check_type_bytes('123 gb') == 125000000000
    assert check_type_bytes('123 tb') == 125000000000000
    assert check_type_bytes('123 pb') == 125000000000000000
    assert check_type_bytes('123 eb') == 125000000000000000000
    assert check_type_bytes('123 zb') == 125000000000000000000000
    assert check_type_bytes('123 yb') == 125000000000000000000000000
    assert check_type_bytes('123 yb') == 125000000000000000000000000



# Generated at 2022-06-12 23:54:46.011292
# Unit test for function check_required_together
def test_check_required_together():
    # This is a simple unit test for function check_required_together(s)
    # in the file ansible/lib/ansible/module_utils/parsing/converters.py
    # with the set of [a:param_a, b:param_b, c:param_c]
    # required together and the three tests below
    terms = [['param_a', 'param_b', 'param_c']]
    # test_1:
    # param_a does not exist
    # param_b does not exist
    # param_c does not exist
    parameters = {}
    assert check_required_together(terms, parameters) == []
    # test_2:
    # param_a exists
    # param_b does not exist
    # param_c exists

# Generated at 2022-06-12 23:54:54.631892
# Unit test for function safe_eval
def test_safe_eval():
    # Not a string
    assert safe_eval(1) == 1

    # String with method call
    assert safe_eval('foo.bar()') == 'foo.bar()'

    # String with import
    assert safe_eval('import foo') == 'import foo'

    # String with no method call or import
    assert safe_eval('foo') == 'foo'
    assert safe_eval('{1: 2}') == {1: 2}
    assert safe_eval('1') == 1



# Generated at 2022-06-12 23:55:01.994839
# Unit test for function check_type_dict
def test_check_type_dict():
    for val in (dict(), 'foo=bar, one=two', {"test": "good"}):
        check_type_dict(val)

    for val in ("{foo=bar, one=two}", "foo=bar, one=two,}", "foo=bar, one=two {"):
        try:
            check_type_dict(val)
            assert False, 'expected TypeError'
        except TypeError:
            pass



# Generated at 2022-06-12 23:55:10.149018
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    parameters = {'param_a':'value_a', 'param_b':'value_b'}
    # Single list
    terms = ['param_a', 'param_b']

    check_mutually_exclusive(terms, parameters)
    # Multiple lists
    terms = [['param_a', 'param_b'], ['param_c', 'param_d']]

    check_mutually_exclusive(terms, parameters)
    # Fail
    terms = ['param_a', 'param_b']
    check_mutually_exclusive(terms, parameters)
    # Fail -> Subspec
    options_context = [u'list of dictionary items']
    check_mutually_exclusive(terms, parameters, options_context)



# Generated at 2022-06-12 23:55:23.677260
# Unit test for function check_required_together
def test_check_required_together():
    options = {
        "required_together": [
            ["param1", "param2"],
            ["param2", "param3"],
            ["param1", "param4"],
            ["param4", "param5"],
        ],
    }

    # case1: param1 and param3 are required together.
    parameters = {"param1": "value_param1", "param3": "value_param3"}
    try:
        check_required_together(options.get("required_together", None), parameters)
    except TypeError:
        pass
    else:
        raise ValueError("Parameters param1, param3 are not required together. Test case1 failed")

    # case2: param1 and param4 are required together.
    parameters = {"param1": "value_param1", "param4": "value_param4"}

# Generated at 2022-06-12 23:55:25.803697
# Unit test for function check_type_bits
def test_check_type_bits():
    return check_type_bits(value='1Mb')



# Generated at 2022-06-12 23:55:29.705758
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('2Kb') == 2048
    assert check_type_bits('1b') == 1
    assert check_type_bits('256b') == 32



# Generated at 2022-06-12 23:55:36.878199
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('2B') == 2
    assert check_type_bytes('4K') == 4096
    assert check_type_bytes('8M') == 8388608
    assert check_type_bytes('1G') == 1073741824
    assert check_type_bytes('2T') == 2199023255552

    try:
        check_type_bytes(1024)
        assert False
    except TypeError:
        assert True

    try:
        check_type_bytes('8X')
        assert False
    except TypeError:
        assert True



# Generated at 2022-06-12 23:55:46.597956
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert 512 == check_type_bytes('512')
    assert 1024 == check_type_bytes(1024)
    assert 1024 == check_type_bytes(1024.0)
    assert 1024 == check_type_bytes('1K')
    assert 1048576 == check_type_bytes('1M')
    assert 1073741824 == check_type_bytes('1G')
    assert 1099511627776 == check_type_bytes('1T')
    assert 1125899906842624 == check_type_bytes('1P')
    assert 1152921504606846976 == check_type_bytes('1E')
    assert -512 == check_type_bytes('-512')
    assert 1024 == check_type_bytes('-1k')
    assert -1048576 == check_type_bytes('-1m')
    assert -107

# Generated at 2022-06-12 23:55:51.968504
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1.05Mb') == 1105920
    assert check_type_bits('1G') == 1073741824


# FIXME: move this one to ansible.utils.facts

# Generated at 2022-06-12 23:56:04.270761
# Unit test for function check_required_by
def test_check_required_by():
    result = check_required_by({"force": "value"}, {"force": "test"})
    assert result == {}
    result = check_required_by({"force": "value"}, {"force": "test"}, options_context=['test'])
    assert result == {}
    result = check_required_by({"force": "value"}, {"force": "test", "value": "test"})
    assert result == {}
    result = check_required_by({"force": "value"}, {"force": "test", "value": "test"}, options_context=['test'])
    assert result == {}
    result = check_required_by({"force": "value"}, {"force": "test"})
    assert type(result) is dict

# Generated at 2022-06-12 23:56:06.379295
# Unit test for function check_type_bits
def test_check_type_bits():
    try:
        check_type_bits('1Mb')
        assert True
    except TypeError:
        assert False


# Generated at 2022-06-12 23:56:10.117912
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("1KiB") == 1024
    assert check_type_bytes("12") == 12
    assert check_type_bytes(12) == 12
    raises(TypeError, check_type_bytes, "not_a_valid_bytes_string")


# Generated at 2022-06-12 23:56:12.121602
# Unit test for function check_type_int
def test_check_type_int():
    for value in ['1', 1, None]:
        value = check_type_int(value)
        assert isinstance(value, int)



# Generated at 2022-06-12 23:56:19.678089
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert(check_type_bytes('5 mb') == 5242880)
    assert(check_type_bytes('5 MB') == 5242880)



# Generated at 2022-06-12 23:56:31.594829
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = dict(
        foo=dict(type='str', required=True),
        baz=dict(type='int'),
    )
    parameters = dict(foo='bar')
    check_required_arguments(argument_spec, parameters)

    parameters = dict(baz=1)
    try:
        check_required_arguments(argument_spec, parameters)
    except TypeError as e:
        assert e.args[0] == "missing required arguments: foo"
    else:
        assert False, "Should have failed for missing foo"

    argument_spec = dict(
        foo=dict(type='str', required=False),
        baz=dict(type='int'),
    )

    parameters = dict(foo='bar')
    check_required_arguments(argument_spec, parameters)


# Generated at 2022-06-12 23:56:38.688333
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert not check_required_arguments({'arg_1': {'required': False}}, {'arg_2': {'required': False}})
    assert check_required_arguments({'arg_1': {'required': True}}, {'arg_2': {'required': False}}) == ['arg_1']
    assert check_required_arguments({'arg_1': {'required': True}}, {}) == ['arg_1']
    assert check_required_arguments({'arg_1': {'required': False}}, {}) == []



# Generated at 2022-06-12 23:56:49.101994
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """
    Test for function check_mutually_exclusive
    """

    # Case01 : Positive test
    module_argument_spec = dict(
        abs(dict(
            age=dict(type='int'),
            employee=dict(type='list')
        )),
        server_list=dict(type='list'),
        name=dict(type='str'),
        state=dict(type='str')
    )

    parameters = dict(
        age=35,
        employee=['Employee1', 'Employee2'],
        server_list=['Server1', 'Server2'],
        name='Developer',
        state='Present'
    )

    assert check_mutually_exclusive(['age', 'employee'], parameters) == []
    assert check_mutually_exclusive(['state'], parameters) == []

# Generated at 2022-06-12 23:56:55.985304
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{"foo": "bar"}') == json.loads('{"foo": "bar"}')
    assert safe_eval('False') is False
    assert safe_eval('{"foo": None}') == {'foo': None}
    assert safe_eval('module.run()') == 'module.run()'
    assert safe_eval('import foo') == 'import foo'
    assert safe_eval('') is None
    assert safe_eval(None) is None



# Generated at 2022-06-12 23:56:59.327098
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(3.14) == 3.14
    assert check_type_float(3) == 3.0
    assert check_type_float('3.14') == 3.14
    assert check_type_float('3') == 3.0

# Generated at 2022-06-12 23:57:02.462578
# Unit test for function check_required_one_of
def test_check_required_one_of():
    try:
        check_required_one_of([['a', 'b'], ['c', 'd']], {"c": 'c', "a": 'a'})
    except TypeError:
        print("One of these terms is required")


# Generated at 2022-06-12 23:57:13.727620
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('[1,2]') == [1, 2]
    assert safe_eval('{"a":1}') == {"a": 1}
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('[1,2]') == [1, 2]
    assert safe_eval('(1,2)') == (1, 2)
    assert safe_eval('{"a":1}') == {"a": 1}
    assert safe_eval('{"a":1}', include_exceptions=True) == ({"a": 1}, None)
    assert safe_eval('foo') == 'foo'
    assert safe

# Generated at 2022-06-12 23:57:21.624672
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = dict(
        one=dict(type='str', required=True),
        two=dict(type='str', required=False),
        three=dict(type='str', required=True),
        four=dict(type='str', required=True)
    )
    parameters = dict(
        one='one',
        two='two',
        three='three'
    )
    missing = check_required_arguments(argument_spec, parameters)
    assert len(missing) == 1
    assert missing[0] == 'four'

    parameters = dict(
        one='one',
        three='three'
    )
    missing = check_required_arguments(argument_spec, parameters)
    assert len(missing) == 2
    assert sorted(missing) == ['four', 'two']


# Generated at 2022-06-12 23:57:30.609344
# Unit test for function check_required_by
def test_check_required_by():
    assert check_required_by({'a':['b','c','d']}, {'a':1,'b':1,'c':1,'d':1}) == {}
    assert check_required_by({'a':['b','c','d']}, {'a':1,'b':1}) == {'a':['c','d']}
    assert check_required_by({'a':['b','c','d']}, {'a':1,'b':1,'d':1}) == {'a':['c']}
    assert check_required_by({'a':['b','c','d']}, {'a':1,'b':1,'c':1}) == {'a':['d']}

# Generated at 2022-06-12 23:57:42.035426
# Unit test for function check_required_together
def test_check_required_together():
    result = check_required_together([['a', 'b']], dict(a=1), dict())
    assert result == []

    result = check_required_together([('a', 'b')], dict(a=1), dict())
    assert result == []

    result = check_required_together([['a', 'b']], dict(a=1, b=1))
    assert result == []

    result = check_required_together([['a', 'b']], dict(b=1))
    assert result == [['a', 'b']]
    # ...

    result = check_required_together([['a', 'b'], ['c', 'd']], dict(a=1, b=1, d=1))
    assert result == [['c', 'd']]


# Generated at 2022-06-12 23:57:46.457210
# Unit test for function check_required_by
def test_check_required_by():
    parameters = {'b':1, 'c':2, 'd': 4}
    requirements = {'a': 'b', 'c': ['d', 'e'] }
    result = check_required_by(requirements, parameters)
    assert result == {'c': ['e']}



# Generated at 2022-06-12 23:57:50.177056
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """Unit tests for function check_type_bytes"""
    assert check_type_bytes("1024") == 1024
    assert check_type_bytes("1K") == 1024
    assert check_type_bytes("1M") == 1024 * 1024
    assert check_type_bytes("1G") == 1024 * 1024 * 1024



# Generated at 2022-06-12 23:57:58.456963
# Unit test for function check_type_bits
def test_check_type_bits():
    bytes = check_type_bits("1Mb")
    assert bytes == 1048576
    bytes = check_type_bits("1048576b")
    assert bytes == 1048576
    bytes = check_type_bits("4M")
    assert bytes == 4194304
    bytes = check_type_bits("4Mib")
    assert bytes == 4194304



# Generated at 2022-06-12 23:58:00.823384
# Unit test for function check_type_dict
def test_check_type_dict():

    assert check_type_dict('{"test": "value"}') == {"test": "value"}

    assert check_type_dict('key=value') == {"key": "value"}

    assert check_type_dict('key=value,key2=value2') == {"key": "value", "key2": "value2"}



# Generated at 2022-06-12 23:58:09.820954
# Unit test for function safe_eval
def test_safe_eval():
    locals = dict(foo='bar')
    assert safe_eval("apple") == "apple"
    assert safe_eval("apple", locals=locals) == "apple"
    assert safe_eval("apple.spam()", locals=locals) == "apple.spam()"
    assert safe_eval("import foo", locals=locals) == "import foo"
    assert safe_eval("True") is True
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}
    assert safe_eval("json.loads('{\"a\": \"b\"}')", include_exceptions=True)[0] == {'a': 'b'}
    assert safe_eval("{'a': 'b'}", include_exceptions=True)[0] == {'a': 'b'}
    assert safe

# Generated at 2022-06-12 23:58:15.151698
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float('1.0') == 1.0
    assert check_type_float(b'1.0') == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float(1.0) == 1.0
    try:
        check_type_float(['1.0'])
    except TypeError:
        pass
    else:
        assert False



# Generated at 2022-06-12 23:58:20.995849
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.0) == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float('1.0') == 1.0
    assert check_type_float(b'1.0') == 1.0
    try:
        check_type_float(None) == 1.0
    except TypeError:
        pass


# Generated at 2022-06-12 23:58:27.385885
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1b') == 1
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1mb') == 1048576
    assert check_type_bits('1gb') == 1073741824
    assert check_type_bits('1tb') == 1099511627776
    assert check_type_bits('1pb') == 1125899906842624
    assert check_type_bits('1PB') == 1125899906842624
    assert check_type_bits('-1') is None
    assert check_type_bits('1xxx') is None
    try:
        check_type_bits(1)
    except TypeError:
        assert True
    else:
        assert False


# Generated at 2022-06-12 23:58:36.605932
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    try:
        check_mutually_exclusive(
            terms=[['one', 'two', 'three']],
            parameters=dict(one=1, two=2, three=3),
        )
    except TypeError as e:
        assert str(e) == 'parameters are mutually exclusive: one|two|three'
    else:
        raise RuntimeError("TypeError was not raised")

    result = check_mutually_exclusive(
        terms=[['one', 'two', 'three', 'none']],
        parameters=dict(one=1, three=3),
    )
    assert result == []

    result = check_mutually_exclusive(
        terms=[['one', 'two', 'three']],
        parameters=dict(none=None),
    )
    assert result == []

