

# Generated at 2022-06-12 23:49:16.139820
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1+1") == 2
    assert safe_eval("'Hello World!'") == "Hello World!"
    assert safe_eval("{'Ansible': 'Engine', 'is': 'Awesome'}") == {'Ansible': 'Engine', 'is': 'Awesome'}
    assert safe_eval("[1, 2, 3]") == [1, 2, 3]

    assert safe_eval("1+1", include_exceptions=True) == (2, None)
    assert safe_eval("'Hello World!'", include_exceptions=True) == ("Hello World!", None)
    assert safe_eval("{'Ansible': 'Engine', 'is': 'Awesome'}", include_exceptions=True) == ({'Ansible': 'Engine', 'is': 'Awesome'}, None)
    assert safe_eval

# Generated at 2022-06-12 23:49:27.444496
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    parameters = {
        'param1': 'test',
        'param2': 'test',
        'param3': 'test',
        'param4': 'test'
    }
    # Test when only one arg is returned
    terms = [
        'param1',
        ['param2', 'param3']
    ]
    try:
        check_mutually_exclusive(terms, parameters)
    except TypeError as e:
        assert 'parameters are mutually exclusive: param2|param3' in to_native(e)

    # Test when more than one arg is returned
    terms = [
        'param1',
        ['param2', 'param3'],
        ['param3', 'param4'],
        'param5'
    ]

# Generated at 2022-06-12 23:49:35.240037
# Unit test for function safe_eval
def test_safe_eval():
    # because I don't want to deal with system imports and whatnot
    assert safe_eval('{"foo":"bar"}') == {"foo": "bar"}, safe_eval('{"foo":"bar"}')
    assert safe_eval('{"foo":"bar"}') == {"foo": "bar"}, safe_eval('{"foo":"bar"}')
    assert safe_eval('{"foo":{{1+1}}}') == {"foo": 2}, safe_eval('{"foo":{{1+1}}}')
    assert safe_eval('{"foo":"bar".format("ignored")}') == {"foo": "bar"}, safe_eval('{"foo":"bar".format("ignored")}')

    # This is not safe for a couple of reasons:
    # 1. Imports
    # 2. Method calls
    # 3. The use of '_params' is a security hole.

# Generated at 2022-06-12 23:49:44.432950
# Unit test for function check_required_by
def test_check_required_by():
    parameters = {'state': 'present', 'name': 'ansible'}
    requirements = {'state': ['name']}

    try:
        check_required_by(requirements, parameters)
    except TypeError:
        pass

    parameters = {'state': 'present', 'name': 'ansible', 'ip': '1.1.1.1'}
    requirements = {'state': ['name', 'ip']}

    try:
        check_required_by(requirements, parameters)
    except TypeError:
        pass

    parameters = {'state': 'present', 'name': 'ansible', 'ip': '1.1.1.1'}
    requirements = {'state': ['ip']}
    try:
        check_required_by(requirements, parameters)
    except TypeError:
        pass

   

# Generated at 2022-06-12 23:49:54.483740
# Unit test for function check_required_arguments
def test_check_required_arguments():
    test_missing = []
    module = dict(
        key1='value1'
    )
    argument_spec = dict(
        key1=dict(type='str', required=False),
        key2=dict(type='str', required=True),
        key3=dict(type='str', required=True)
    )

    if argument_spec is None:
        return test_missing

    for (k, v) in argument_spec.items():
        required = v.get('required', False)
        #print("testing this")
        #print(required)
        if required and k not in parameters:
            test_missing.append(k)
            print("TESTING THIS")
            print(test_missing)

    #print("TESTING THIS")
    #print(test_missing)

# Generated at 2022-06-12 23:50:05.305854
# Unit test for function check_required_if
def test_check_required_if():
    params = dict(
      host=dict(required=True, type='str'),
      username=dict(required=False, default=None),
      password=dict(required=False, default=None, no_log=True),
      port=dict(required=False, default=None),
      provider=dict(default=None),
      protocol=dict(required=True, choices=['http', 'https']),
      allowed_size_max=dict(type='str'),
      allowed_size_min=dict(type='str'),
      deprecate_size_value=dict(type='str'),
    )


# Generated at 2022-06-12 23:50:17.356800
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Validate positive case with no missing required parameters
    argument_spec = {'a': {'required': True}, 'b': {'required': True}}
    parameters = {'a': 'A', 'b': 'B'}
    missing = check_required_arguments(argument_spec, parameters)
    assert missing == []
    # Validate negative case with missing required parameters
    argument_spec = {'a': {'required': True}, 'b': {'required': True}}
    parameters = {'a': 'A'}
    try:
        missing = check_required_arguments(argument_spec, parameters)
    except TypeError as error:
        if 'missing required arguments: b' in to_native(error):
            missing = True
    assert missing is True
    # Validate no exception is raised if argument_spec is None
   

# Generated at 2022-06-12 23:50:19.754841
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    parameters = {'name': 'test'}
    required_parameters = ['name','test']
    try:
        check_missing_parameters(parameters, required_parameters)
        assert False
    except TypeError as e:
        assert 'test' in to_native(e)
        assert 'missing required arguments' in to_native(e)
    assert check_missing_parameters(parameters) == []



# Generated at 2022-06-12 23:50:25.456225
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('a=1') == {'a': '1'}
    assert check_type_dict('a=1,b=2') == {'a': '1', 'b': '2'}
    assert check_type_dict('a="1,2,3"') == {'a': '1,2,3'}
    assert check_type_dict('a="1,2,3,4"') == {'a': '1,2,3,4'}
    assert check_type_dict('a=1,b=[1,2,3]') == {'a': '1', 'b': '[1,2,3]'}

# Generated at 2022-06-12 23:50:37.496406
# Unit test for function check_required_if
def test_check_required_if():
    import pytest
    assert check_required_if([['state', 'present', ('path',), True], ['someint', 99, ('bool_param', 'string_param')]],
                        {'state': 'present', 'path': 'test_path'},
                        ['boolean_param', 'string_param']) == []
    assert check_required_if([['state', 'present', ('path',), True], ['someint', 99, ('bool_param', 'string_param')]],
                        {'state': 'present', 'path': 'test_path'},
                        ['bool_param', 'string_param']) == []

# Generated at 2022-06-12 23:50:54.037763
# Unit test for function check_required_together
def test_check_required_together():
    terms = [['a', 'b', 'c'],['a', 'c']]
    parameters = {'a':1, 'b':2,'d':3}
    options_context = 'ABC'
    results = check_required_together(terms, parameters, options_context)
    print(results)



# Generated at 2022-06-12 23:51:03.522288
# Unit test for function check_required_together
def test_check_required_together():

    assert check_required_together([('a','b'), ('c','d')], {'a':1, 'b':1}) == []
    assert check_required_together([('a','b'), ('c','d')], {'b':1, 'd':1}) == []
    assert check_required_together([('a','b'), ('c','d')], {'a':1, 'd':1}) == [('a','b'), ('c','d')]
    assert check_required_together([('a','b'), ('c','d')], {'c':1, 'b':1}) == []
    assert check_required_together([('a','b'), ('c','d')], {'c':1, 'b':1, 'd':1}) == []

# Generated at 2022-06-12 23:51:14.794316
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict("a=b")=={'a': 'b'}, 'string with key=value'
    assert check_type_dict("a=b,c=d")=={'a': 'b', 'c': 'd'}, 'string with key=value'
    assert check_type_dict("a=b,c=d,e=f")=={'a': 'b', 'c': 'd', 'e': 'f'}, 'string with key=value'
    assert check_type_dict("{'k': 1, 'k2': {'k3': 1}}")=={'k': 1, 'k2': {'k3': 1}}, 'string with json'
    assert check_type_dict("a=1,b={'k': 1, 'k2': {'k3': 1}}")

# Generated at 2022-06-12 23:51:19.442994
# Unit test for function check_type_bytes
def test_check_type_bytes():
    for test in ['1', '1MB', '1.5MB', '1kb', '1k', '1.5kb', '1KB']:
        if check_type_bytes(test) != human_to_bytes(test):
            raise AssertionError('test_check_type_bytes("%s") failed' % test)



# Generated at 2022-06-12 23:51:27.921844
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    params = {
        'key1': 'value1',
        'key2': 'value2',
    }
    result = check_mutually_exclusive(['key1', 'key2'], params)
    assert result is None
    try:
        check_mutually_exclusive(['key1', 'key2'], {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
        assert False
    except TypeError as e:
        assert "parameters are mutually exclusive" in str(e)

# Generated at 2022-06-12 23:51:35.928244
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils import basic
    from ansible.module_utils.six import StringIO

    orig = sys.stdout
    sys.stdout = StringIO()

# Generated at 2022-06-12 23:51:37.615290
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Kb') == 1024
    assert check_type_bits('1Kbit') == 1024
    assert check_type_bits('1Gbit') == 1073741824

# Generated at 2022-06-12 23:51:47.541259
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1 B') == 1
    assert check_type_bytes('1023 B') == 1023
    assert check_type_bytes('1 kB') == 1000
    assert check_type_bytes('1 MB') == 1000000
    assert check_type_bytes('1  MB') == 1000000
    assert check_type_bytes('1GB') == 1000000000
    assert check_type_bytes('1TB') == 1000000000000
    assert check_type_bytes('1PB') == 1000000000000000
    assert check_type_bytes('1EB') == 1000000000000000000
    assert check_type_bytes('1ZB') == 1000000000000000000000
    assert check_type_bytes('1YB') == 1000000000000000000000000
    assert check_type_bytes('-500B') == -500

# Generated at 2022-06-12 23:51:55.531372
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('["foo", "bar"]') == ["foo", "bar"]
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('foo') == "foo"
    assert safe_eval('["foo", "bar"]', include_exceptions=True) == (["foo", "bar"], None)
    assert safe_eval('{"foo": "bar"}', include_exceptions=True) == ({"foo": "bar"}, None)
    assert safe_eval('foo', include_exceptions=True) == ("foo", None)



# Generated at 2022-06-12 23:52:02.333435
# Unit test for function safe_eval
def test_safe_eval():
    ret_v, ret_e = safe_eval('"string"', include_exceptions=True)
    assert ret_v == 'string'
    assert ret_e is None
    # simple dict
    ret_v, ret_e = safe_eval('{"a":"b"}', include_exceptions=True)
    assert ret_v == {'a': 'b'}
    assert ret_e is None
    # simple list
    ret_v, ret_e = safe_eval('["a","b"]', include_exceptions=True)
    assert ret_v == ['a', 'b']
    assert ret_e is None
    # simple set
    ret_v, ret_e = safe_eval('set(["a","b"])', include_exceptions=True)

# Generated at 2022-06-12 23:52:10.897267
# Unit test for function check_required_by
def test_check_required_by():
    try:
        check_required_by(
            requirements=dict(with_specified=['foo', 'baz']),
            parameters=dict(with_specified='bar', baz='bar'),
            options_context=[]
        )
    except TypeError:
        assert True
    else:
        assert False



# Generated at 2022-06-12 23:52:15.288336
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int('2') == 2
    assert check_type_int(3.1) == 3
    try:
        check_type_int(None) == None
    except TypeError:
        assert True
    else:
        assert False


# Generated at 2022-06-12 23:52:25.035601
# Unit test for function check_required_by
def test_check_required_by():
    # Test case - check required by
    result = check_required_by(requirements={'a': ['b', 'c'], 'b': ['d'], 'e': []}, parameters={'a': 'a', 'd': 'd'})
    assert result['a'] == ['c']
    assert not result.get('b')
    assert not result.get('e')

    # Test case - no requirements
    result = check_required_by(requirements=None, parameters={'a': 'a', 'd': 'd'})
    assert not result

    # Test case - no matching key
    result = check_required_by(requirements={'a': ['b', 'c'], 'b': ['d'], 'e': []}, parameters={'c': 'c', 'd': 'd'})

# Generated at 2022-06-12 23:52:29.275864
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'required_arg_1': {'required': True},
        'required_arg_2': {'required': True},
        'not_required_arg': {'required': False}
    }
    parameters = {}
    try:
        check_required_arguments(argument_spec, parameters)
        assert False, "Expected to fail because required arguments are missing"
    except TypeError as e:
        assert "missing required arguments" in str(e)


# Generated at 2022-06-12 23:52:41.029740
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('2 * 3') == 6
    assert safe_eval('ansible') == 'ansible'
    assert safe_eval('object') == 'object'
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}
    assert safe_eval("['a', 'b', 'c']") == ['a', 'b', 'c']
    assert safe_eval("'a'") == 'a'
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('1') == 1
    assert safe_eval('(1, 2)') == (1, 2)
    assert safe_eval('import foo')

# Generated at 2022-06-12 23:52:48.271073
# Unit test for function check_required_by
def test_check_required_by():
    assert check_required_by({}, {}) == {}
    assert check_required_by({}, {"a": "A"}, options_context=["a"]) == {}
    try:
        assert check_required_by({"b": "a"}, {"a": "A"}, options_context=["a"])
        assert False
    except TypeError as e:
        assert e.args[0] == "missing parameter(s) required by 'b': a found in a"

    assert check_required_by({"b": "a"}, {"a": "A", "b": "B"}, options_context=["a"]) == {}
    assert check_required_by({"b": ["a", "c"]}, {"a": "A", "b": "B"}, options_context=["a"]) == {}


# Generated at 2022-06-12 23:52:57.647417
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{"foo": 1}', include_exceptions=True) == ({'foo': 1}, None)
    assert safe_eval('bar', include_exceptions=True) == ('bar', None)
    assert safe_eval('import json', include_exceptions=True) == ('import json', None)
    assert safe_eval("{'bar': 'baz'}", include_exceptions=True) == ("{'bar': 'baz'}", None)
    assert safe_eval('bar.baz()', include_exceptions=True) == ('bar.baz()', None)
    assert safe_eval("{'a': 1}", include_exceptions=True) == ({'a': 1}, None)



# Generated at 2022-06-12 23:52:59.519304
# Unit test for function check_type_bits
def test_check_type_bits():
    test = 'test'
    result = check_type_bits(test)
    print(result)
if __name__ == '__main__':
    test_check_type_bits()

# Generated at 2022-06-12 23:53:03.730778
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(5) == 5
    assert check_type_int(5.0) == 5
    assert check_type_int("5") == 5
    assert check_type_int("5.0") == 5
    assert check_type_int("5.1") == 5
    assert check_type_int("12345678912345678") == 12345678912345678
    a = check_type_int("123456789123456789123456789")
    assert a == 123456789123456789123456789
    with pytest.raises(TypeError) as excep:
        result = check_type_int("5.5")


# Generated at 2022-06-12 23:53:05.881256
# Unit test for function check_type_int
def test_check_type_int():
    a = check_type_int('1')
    expect_a = 1
    assert(a == expect_a)

    b = check_type_int(1)
    expect_b = 1
    assert(b == expect_b)


# Generated at 2022-06-12 23:53:20.633276
# Unit test for function check_required_one_of
def test_check_required_one_of():
    import sys
    if sys.version_info[0] < 3:
        assert check_required_one_of(None, {}) == []
        try:
            check_required_one_of([['a', 'b']], {'c': 1})
        except TypeError:
            pass
        else:
            raise Exception("Expected TypeError")
        assert check_required_one_of([['a', 'b']], {'b': 1}) == []
        assert check_required_one_of([['a', 'b'], ['c', 'd']], {'b': 1, 'd': 1}) == []
        assert check_required_one_of([['a', 'b'], ['c', 'd']], {}) == [['a', 'b'], ['c', 'd']]



# Generated at 2022-06-12 23:53:29.388349
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Test for function check_mutually_exclusive"""
    from .validate import check_mutually_exclusive
    from .validate import count_terms

    module = dict(a=1, b=2, c=3)
    terms = [
        ['a', 'b'],
        ['a', 'c'],
        ['b', 'c'],
        ['a', 'b', 'c'],
    ]
    # all should pass
    check_mutually_exclusive(terms, module)
    # a and b
    module = dict(a=1, b=2)
    check_mutually_exclusive(terms, module)
    # a and c
    module = dict(a=1, c=3)
    check_mutually_exclusive(terms, module)
    # b and c

# Generated at 2022-06-12 23:53:34.734988
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('{}') == {}
    assert check_type_dict('') == {}
    assert check_type_dict('foo=bar') == {'foo': 'bar'}
    assert check_type_dict('foo=bar,baz=bar') == {'foo': 'bar', 'baz': 'bar'}
    assert check_type_dict(u'{"foo": "bar"}') == {'foo': 'bar'}
    assert check_type_dict(u'foo=bar,baz="foobar"') == {'foo': 'bar', 'baz': 'foobar'}
    assert check_type_dict(u'foo=bar,baz="foo,bar"') == {'foo': 'bar', 'baz': 'foo,bar'}

# Generated at 2022-06-12 23:53:44.538769
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('(1,2)') == (1,2)
    assert safe_eval('{1:2}') == {1:2}
    assert safe_eval('[1,2]') == [1,2]
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('import bar') == 'import bar'
    assert safe_eval('[1,2,3]', include_exceptions=True) == ([1,2,3], None)
    assert safe_eval('foo.bar()', include_exceptions=True) == ('foo.bar()', None)
    assert safe_eval('import bar', include_exceptions=True) == ('import bar', None)

# Generated at 2022-06-12 23:53:50.946169
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.0) == 1.0
    assert check_type_float("1.0") == 1.0
    assert check_type_float("1") == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float(True) == 1.0
    assert check_type_float(False) == 0.0
    assert check_type_float("0") == 0.0
    assert check_type_float("0.0") == 0.0
    assert check_type_float(0) == 0.0
    assert check_type_float(0.0) == 0.0
    assert check_type_float("one") == 1.0


# Generated at 2022-06-12 23:54:01.849309
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Function to test check_mutually_exclusive"""
    assert check_mutually_exclusive(
        [["a", "b"], ["c", "d"]],
        {"a": 1, "b": 1, "c": 1, "d": 1}) == [["a", "b"], ["c", "d"]]

    assert check_mutually_exclusive(
        [["a", "b"], ["c", "d"]],
        {"a": 1, "c": 1, "d": 1}) == []

    assert check_mutually_exclusive(
        [["a", "b"], ["c", "d"]],
        {"a": 1, "b": 1, "d": 1}) == [["a", "b"]]
    assert check_mutually_exclusive([['a']], {'a': 1}) == []
    assert check_

# Generated at 2022-06-12 23:54:10.983143
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert [] == check_required_arguments({}, {})

    # Test simple required check
    try:
        check_required_arguments({'foo': {'required': True}}, {})
        assert False, "check_required_arguments() should raise an exception for missing required arguments"
    except TypeError as e:
        pass

    # Test required check with default value
    try:
        check_required_arguments({'foo': {'required': True, 'default': 'bar'}}, {})
        assert False, "check_required_arguments() should raise an exception for missing required arguments"
    except TypeError as e:
        pass

    # Test required check with 'no' default value

# Generated at 2022-06-12 23:54:21.874575
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Test with null argument_spec
    assert [] == check_required_arguments(None, { "argument1": "value" })

    # Test with not null argument_spec, but no required parameters
    assert [] == check_required_arguments({ "argument1": {} }, { "argument1": "value" })

    # Test with parameter missing
    assert ["argument2"] == check_required_arguments({ "argument2": { "required": True } }, {})

    # Test with two parameters missing
    assert sorted(["argument2", "argument4"]) == sorted(check_required_arguments({ "argument2": { "required": True }, "argument4": { "required": True } }, {}))

    # Test with one parameter missing but without a required parameter
    assert ["argument2"] == check_required_arguments({ "argument1": {} }, {})

# Generated at 2022-06-12 23:54:32.914819
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('') == 0
    assert check_type_bytes('0') == 0
    assert check_type_bytes('10B') == 10
    assert check_type_bytes('10b') == 10
    assert check_type_bytes('10kb') == 10 * KILO_BYTE
    assert check_type_bytes('1MB') == 1 * MEGA_BYTE
    assert check_type_bytes('1Gb') == 1 * GIGA_BYTE
    assert check_type_bytes('1tb') == 1 * TERA_BYTE

    assert check_type_bytes('1.5gb') == 1 * GIGA_BYTE + 512 * MEGA_BYTE

    with pytest.raises(TypeError):
        check_type_bytes(1024)


# Apply multiple validator functions so that

# Generated at 2022-06-12 23:54:40.638804
# Unit test for function check_type_dict
def test_check_type_dict():
    # Test that a dict will pass and return without error
    assert check_type_dict(dict(a=1, b=2)) == dict(a=1, b=2)

    # Test that a string in dict form will pass and return converted
    assert check_type_dict('{"a":1, "b":2}') == dict(a=1, b=2)

    # Test that a string in key=value form will pass and return converted
    assert check_type_dict('a=1, b=2') == dict(a=1, b=2)

    # Test that an un-convertable string will fail
    exception = None
    try:
        check_type_dict('some string')
    except TypeError:
        exception = sys.exc_info()[1]
    assert exception is not None

# Generated at 2022-06-12 23:54:57.643586
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('{"a": 1}') == {"a": 1}
    assert check_type_dict('a=1') == dict(a='1')
    assert check_type_dict('a=1,b=2') == dict(a='1', b='2')
    assert check_type_dict('a=1, b=2') == dict(a='1', b='2')
    assert check_type_dict('a=1,b = 2') == dict(a='1', b='2')
    assert check_type_dict('a=1, b = 2') == dict(a='1', b='2')
    assert check_type_dict('a=1,b= 2') == dict(a='1', b='2')
    assert check_type_dict('a=1, b= 2') == dict

# Generated at 2022-06-12 23:55:08.265256
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('') == ''
    assert safe_eval(1) == 1
    assert safe_eval('1') == 1
    assert safe_eval('1 + 1') == 2
    assert safe_eval('False') is False
    assert safe_eval('{"k": "v"}') == {'k': 'v'}
    assert safe_eval('{"k": "{{ v }}"}', dict(v='v')) == {'k': 'v'}
    assert safe_eval('a.replace("a", "b")', dict(a='a')) == 'a.replace("a", "b")'
    assert safe_eval('import os', dict(a='a')) == 'import os'

# Generated at 2022-06-12 23:55:19.192702
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("1") == 1
    assert check_type_bytes("1M") == 1048576
    assert check_type_bytes("2G") == 2147483648
    assert check_type_bytes("3T") == 32212254720
    assert check_type_bytes("1K") == 1024
    assert check_type_bytes("1KB") == 1024
    assert check_type_bytes("1kB") == 1024
    assert check_type_bytes("1MB") == 1048576
    assert check_type_bytes("1mB") == 1048576
    assert check_type_bytes("1gb") == 1073741824
    assert check_type_bytes("1TB") == 1099511627776
    assert check_type_bytes("1Tb") == 1099511627776



# Generated at 2022-06-12 23:55:28.706597
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # Accept list of lists
    terms = [['param1', 'param2']]
    assert not check_mutually_exclusive(terms, dict(param1=1))
    assert not check_mutually_exclusive(terms, dict(param2=2))
    assert not check_mutually_exclusive(terms, dict(param3=3))
    assert check_mutually_exclusive(terms, dict(param1=1, param2=2))

    # Accept single list of terms
    terms = ['param1', 'param2']
    assert not check_mutually_exclusive(terms, dict(param1=1))
    assert not check_mutually_exclusive(terms, dict(param2=2))
    assert not check_mutually_exclusive(terms, dict(param3=3))

# Generated at 2022-06-12 23:55:30.772111
# Unit test for function check_type_bytes
def test_check_type_bytes():
    byte_value = check_type_bytes('1kb')
    assert byte_value == 1024


# Generated at 2022-06-12 23:55:35.417701
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # pylint: disable=unused-variable
    from ansible.module_utils.basic import AnsibleModule
    # pylint: enable=unused-variable

    module = AnsibleModule(argument_spec=dict(verbose=dict(type='bool')))

    # Test mutually exclusive parameters
    try:
        check_mutually_exclusive(
            [['verbose', 'debug']],
            module.params,
            ['root'],
        )
        assert False, "should have thrown an error"
    except TypeError:
        pass

    assert check_mutually_exclusive(
        [['verbose', 'debug']],
        module.params,
        ['root']
    ) == []

    module.params['verbose'] = True
    module.params['debug'] = False

# Generated at 2022-06-12 23:55:45.679407
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict("{\"id\": 1}") == {"id": 1}
    assert check_type_dict("id=1") == {"id": "1"}
    assert check_type_dict("\"id\"=1") == {"id": "1"}
    assert check_type_dict("id=1, name=test") == {"id": "1", "name": "test"}
    assert check_type_dict("id=1, name=\"test me\"") == {"id": "1", "name": "\"test me\""}
    assert check_type_dict("id=1, name=\"test=me\"") == {"id": "1", "name": "\"test=me\""}

# Generated at 2022-06-12 23:55:58.520560
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Test case where all parameters are present
    params = {'required': 'yes', 'not-required': 'no'}
    spec = {'required': dict(), 'not-required': dict()}
    spec['required']['required'] = True
    assert not check_required_arguments(spec, params)
    # Test case where required parameter is missing
    params = {'not-required': 'no'}
    try:
        check_required_arguments(spec, params)
    except TypeError as e:
        assert 'required' in to_native(e)
    else:
        assert False
    # Test case where required parameter is missing, but is None
    params = {'not-required': 'no', 'required': None}

# Generated at 2022-06-12 23:56:10.254750
# Unit test for function safe_eval
def test_safe_eval():
    # Ensure that literal strings and numbers are returned unaltered
    assert(safe_eval('1') == 1)
    assert(safe_eval('1.0') == 1.0)
    assert(safe_eval('-1.0') == -1.0)
    assert(safe_eval('"test"') == "test")
    assert(safe_eval('["test"]') == ["test"])
    assert(safe_eval('{"test": "test"}') == {"test": "test"})
    # None evaluates to None
    assert(safe_eval('None') is None)
    # Ensure that unsafe values are not evaluated
    assert(safe_eval('os.listdir(".")') == 'os.listdir(".")')
    assert(safe_eval('import os') == 'import os')
    # Ensure that a SyntaxError is correctly

# Generated at 2022-06-12 23:56:21.389166
# Unit test for function check_required_arguments
def test_check_required_arguments():
    test_spec = {}
    test_parameters = {}
    if check_required_arguments(test_spec, test_parameters) != []:
        raise AssertionError("Empty spec and parameters should not fail.")
    test_spec = {'blah': {'required': False}}
    test_parameters = {}
    if check_required_arguments(test_spec, test_parameters) != []:
        raise AssertionError("Spec with non-required argument should not fail.")
    test_spec = {'blah': {'required': False}, 'hooray': {'required': True}}
    test_parameters = {}
    if check_required_arguments(test_spec, test_parameters) != ['hooray']:
        raise AssertionError("Spec with non-required argument should fail.")



# Generated at 2022-06-12 23:56:34.714776
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    assert safe_eval("{1,2,3}") == {1, 2, 3}
    assert safe_eval('"foo"') == "foo"
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}
    assert safe_eval("['foo', 'bar']") == ['foo', 'bar']
    assert safe_eval("None") is None
    assert safe_eval("False") is False
    assert safe_eval("True") is True
    assert safe_eval("[1,2, 'foo']") == [1, 2, "foo"]
    assert safe_eval("{'foo': 'bar', 1:2}") == {'foo': 'bar', 1: 2}
    assert safe

# Generated at 2022-06-12 23:56:43.474141
# Unit test for function check_required_together
def test_check_required_together():
    for terms in [[('a', 'b'), ('c', 'd')], (('a', 'b'), ('c', 'd')), [['a', 'b'], ['c', 'd']]]:
        try:
            check_required_together(terms, {'a': 1, 'b': 2})
        except TypeError:
            assert False, 'Check_required_together function failed.'
        else:
            assert True, 'Check_required_together function passed.'
        try:
            check_required_together(terms, {'a': 1, 'c': 2})
        except TypeError:
            assert True, 'Check_required_together function passed.'
        else:
            assert False, 'Check_required_together function failed.'

# Generated at 2022-06-12 23:56:46.499566
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int('1') == 1   # int string
    assert check_type_int(1) == 1     # int
    assert check_type_int(1.1)



# Generated at 2022-06-12 23:56:57.118732
# Unit test for function check_required_by
def test_check_required_by():
  # Test case 1: empty requirements
  requirements = {}
  parameters = {}
  result = check_required_by(requirements, parameters)
  if result:
      print("Values returned for empty requirements: {}".format(result))
  else:
      print("Empty requirements - SUCCESS")

  # Test case 2: requirements with single key/value
  requirements = {'a': 'b'}
  parameters = {'a': 'xyz', 'b': 'abc'}
  result = check_required_by(requirements, parameters)
  if result:
      print("Values returned for key/value requirements: {}".format(result))
  else:
      print("requirements with single key/value - SUCCESS")

  # Test case 3: requirements with single key/multi-value

# Generated at 2022-06-12 23:56:59.159156
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('12k') == 12 * 1024
    assert check_type_bytes(1) == 1



# Generated at 2022-06-12 23:57:00.859764
# Unit test for function check_type_bits
def test_check_type_bits():
    bytes_bits = check_type_bits('1Mb')
    assert bytes_bits == 1048576



# Generated at 2022-06-12 23:57:08.267723
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("1024") == 1024
    assert check_type_bytes("1K") == 1024
    assert check_type_bytes("1KB") == 1024
    assert check_type_bytes("1.5K") == 1536
    assert check_type_bytes("1.5KB") == 1536
    assert check_type_bytes("1.5M") == 1572864
    assert check_type_bytes("1.5MB") == 1572864
    assert check_type_bytes("1.5G") == 1610612736
    assert check_type_bytes("1.5GB") == 1610612736
    assert check_type_bytes("1.5T") == 1649267441664
    assert check_type_bytes("1.5TB") == 1649267441664

# Generated at 2022-06-12 23:57:16.665571
# Unit test for function check_type_int
def test_check_type_int():
    # Test if value is an int
    value = 5
    assert(check_type_int(value) == value)
    # Test if value is an int as a string
    value = '5'
    assert(check_type_int(value) == int(value))
    # Test that a value that can't be converted to an int raises a TypeError
    value = 'five'
    try:
        check_type_int(value)
    except TypeError:
        pass
    else:
        raise AssertionError('Expected a TypeError, got %s instead' % type(value))


# FIXME: reduce code duplication between this and check_type_float

# Generated at 2022-06-12 23:57:21.434434
# Unit test for function check_required_arguments
def test_check_required_arguments():
    required = {
        'arg1': {'required': True},
        'arg2': {'required': True},
        'arg3': {'required': False}
    }
    assert check_required_arguments(required, {}) == ['arg1', 'arg2']
    assert check_required_arguments(required, {'arg1': 1, 'arg2': 2}) == []
    assert check_required_arguments(required, {'arg3': 3}) == ['arg1', 'arg2']


# Generated at 2022-06-12 23:57:29.291587
# Unit test for function check_type_dict
def test_check_type_dict():
    # Test valid dict
    assert check_type_dict(dict(a='a', b='b')) == dict(a='a', b='b')
    assert check_type_dict("{'a': 'a', 'b': 'b'}") == dict(a='a', b='b')
    assert check_type_dict("{\"a\": \"a\", \"b\": \"b\"}") == dict(a='a', b='b')
    assert check_type_dict("a='a', b='b'") == dict(a='a', b='b')
    assert check_type_dict("a=\"a\", b=\"b\"") == dict(a='a', b='b')
    assert check_type_dict("a='a', b=\"b\"") == dict(a='a', b='b')
    assert check_type

# Generated at 2022-06-12 23:57:38.642953
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int('10') == 10
    assert check_type_int(10) == 10
    assert check_type_int(['10']) == ['10']
    assert check_type_int({'10': 1}) == {'10': 1}


# Generated at 2022-06-12 23:57:40.445408
# Unit test for function check_type_bits
def test_check_type_bits():
    """Unit test function check_type_bits"""
    assert check_type_bits('1Mb') == 1048576



# Generated at 2022-06-12 23:57:43.052905
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(10) == 10
    assert check_type_int('10') == 10
    try:
        check_type_int('10.1')
        raise AssertionError("Fail")
    except TypeError:
        pass


# Generated at 2022-06-12 23:57:52.562796
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('-6') == -6
    assert safe_eval('1+6') == 7
    assert safe_eval('-6+1') == -5
    assert safe_eval('1.0') == 1.0
    assert safe_eval('1e4') == 10000.0
    assert safe_eval('1.2e4') == 12000.0
    assert safe_eval('-2.2e4') == -22000.0
    assert safe_eval('True')
    assert safe_eval('False')
    assert safe_eval('[1,2,3]') == [1,2,3]
    assert safe_eval('{"a": "foo"}') == {"a": "foo"}
    assert safe_eval('1+1') == 2
    assert safe_

# Generated at 2022-06-12 23:58:05.215431
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Gbps') == 125000000
    assert check_type_bits('1mbps') == 125000
    assert check_type_bits('1mibps') == 131072
    assert check_type_bits('1mBps') == 131072
    assert check_type_bits('1mb') == 8388608
    assert check_type_bits('1mbit') == 8388608
    assert check_type_bits('1mbIT') == 8388608
    assert check_type_bits('1Mb') == 8388608
    assert check_type_bits('1mB') == 8388608
    with pytest.raises(TypeError):
        check_type_bits('1MbIT')

# Generated at 2022-06-12 23:58:13.397926
# Unit test for function check_required_if
def test_check_required_if():
    # Simple test to make sure req_if works.
    arguments = {'vpc_name': 'test', 'cidr_block': '10.1.0.0/16', 'state': 'present'}
    requirement = [('state', 'present', ('cidr_block',), True)]
    check_required_if(requirement, arguments)

    # Test to make sure req_if with oneof works
    arguments = {'vpc_name': 'test', 'state': 'present'}
    requirement = [('state', 'present', ('cidr_block',), False)]

# Generated at 2022-06-12 23:58:23.502956
# Unit test for function check_required_together
def test_check_required_together():
    # Test a success case
    params = {'a': 1, 'b': 2, 'c': 3}
    check = [['a', 'b'], ['a', 'c']]
    rc = check_required_together(check, params)
    assert rc == []

    # Test a failure case
    params = {'a': 1, 'b': 2}
    check = [['a', 'b'], ['a', 'c']]
    rc = check_required_together(check, params)
    exp_err_msg = "parameters are required together: a, c"
    try:
        check_required_together(check, params)
    except TypeError as e:
        assert exp_err_msg in str(e)

    # Test case with options_context

# Generated at 2022-06-12 23:58:34.480480
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    def f():
        return check_mutually_exclusive(['a', 'b'], {'a': 1, 'b': 1})

    def f2():
        return check_mutually_exclusive([['a', 'b']], {'a': 1, 'b': 1})

    def f3():
        return check_mutually_exclusive([['a', 'b']], {'a': 1, 'b': 1, 'c': 1})

    def f4():
        return check_mutually_exclusive([['a', 'a']], {'a': 1, 'b': 1})

    def f5():
        return check_mutually_exclusive([['a', 'a'], ['b', 'b']], {'a': 1, 'b': 1})
