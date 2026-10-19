

# Generated at 2022-06-12 23:49:21.846968
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'parameter_1': {'required': True},
        'parameter_2': {'required': False},
        'parameter_3': {'required': False},
        'parameter_4': {'required': True},
        'parameter_5': {'required': True},
    }

    parameters_1 = {
        'parameter_2': 'Value',
        'parameter_3': 'Value',
    }
    parameters_2 = {
        'parameter_1': 'Value',
        'parameter_2': 'Value',
        'parameter_3': 'Value',
        'parameter_4': 'Value',
        'parameter_5': 'Value',
    }

# Generated at 2022-06-12 23:49:30.953183
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments({'arg1': {'required': True}}, {'arg1': 'val1'}) == []
    assert check_required_arguments({'arg1': {'required': False}}, {'arg1': 'val1'}) == []
    assert check_required_arguments({'arg1': {'required': False}}, {}) == []
    assert check_required_arguments({'arg1': {'required': True}}, {}) == ['arg1']
    assert check_required_arguments({'arg1': {'required': True}}, {'arg1': None}) == []



# Generated at 2022-06-12 23:49:37.607714
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'var_name': {'required': True, 'type': 'int', 'default': 0},
        'var_name2': {'required': True, 'type': 'int', 'default': 0},
        'var_name3': {'required': False, 'type': 'int', 'default': 0}
    }
    param = {'var_name': 1, 'var_name2': 2}
    assert check_required_arguments(argument_spec, param) == []
    param = {'var_name': 1, 'var_name3': 3}
    assert check_required_arguments(argument_spec, param) == ['var_name2']
    param = {'var_name2': 1, 'var_name3': 3}

# Generated at 2022-06-12 23:49:45.306878
# Unit test for function check_required_if
def test_check_required_if():
    result = []
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = dict(
        state='present',
        someint=99,
        path='/a/b/c',
        bool_param='False',
    )
    result.append(check_required_if(requirements=requirements, parameters=parameters))
    parameters = dict(
        state='present',
        someint=99,
        path='/a/b/c',
    )
    try:
        check_required_if(requirements=requirements, parameters=parameters)
    except TypeError as e:
        t = e.args[0]
        print(t)
        result.append(t)
   

# Generated at 2022-06-12 23:49:47.053330
# Unit test for function check_type_bytes
def test_check_type_bytes():
    # Success case
    result = check_type_bytes('1M')
    assert result == 1048576
    # Failure case
    try:
        check_type_bytes('error')
    except TypeError:
        assert True
# End of block for unit test



# Generated at 2022-06-12 23:49:56.411552
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    value = "{'foo': 'bar'}"
    res = literal_eval(value)
    assert isinstance(res, dict)
    assert res == {'foo': 'bar'}
    res = safe_eval(value)
    assert isinstance(res, dict)
    assert res == {'foo': 'bar'}
    value = u"'blah'"
    res = safe_eval(value)
    assert isinstance(res, text_type)
    assert res == u'blah'

    result, exception = safe_eval(value, include_exceptions=True)
    assert result == u'blah'
    assert exception is None

    value = u"blah"
    result, exception = safe_

# Generated at 2022-06-12 23:50:02.513881
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    params = dict(foo='bar')
    required_params = ['foo']
    result = check_missing_parameters(params, required_params)
    assert result == []

    required_params.append('bar')
    error_msg = 'missing required arguments: %s' % ','.join(missing_params)
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(params, required_params)
    assert to_native(excinfo.value) == error_msg



# Generated at 2022-06-12 23:50:15.190760
# Unit test for function check_type_dict
def test_check_type_dict():
    #pylint: disable=unused-argument
    def pass_type_dict(module, value):
        return check_type_dict(value)

    def fail_type_dict(module, value):
        return check_type_dict(value)

    module = object()

    # Test dict
    assert pass_type_dict(module, dict(a="alpha", b="bravo")) == dict(a="alpha", b="bravo")
    assert pass_type_dict(module, dict(a=dict(b="bravo"), c="charlie")) == dict(a=dict(b="bravo"), c="charlie")
    assert pass_type_dict(module, dict()) == dict()
    assert pass_type_dict(module, None) == None # pylint: disable=redefined-builtin



# Generated at 2022-06-12 23:50:26.712773
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    prms = {}
    terms = [["a", "b"], ["c", "d"]]
    result = check_mutually_exclusive(terms, prms)
    assert result is None
    prms = {"a": 1}
    result = check_mutually_exclusive(terms, prms)
    assert result is None
    prms = {"a": 1, "c": 1}
    result = check_mutually_exclusive(terms, prms)
    assert result is None
    prms = {"a": 1, "b": 1}
    result = check_mutually_exclusive(terms, prms)
    assert result == [["a", "b"]]
    prms = {"a": 1, "c": 1, "d": 1}
    result = check_mutually_exclusive(terms, prms)

# Generated at 2022-06-12 23:50:32.476702
# Unit test for function check_required_if
def test_check_required_if():
    parameters = dict(
        state='present',
        path='/path/to/file',
        someint=99,
    )
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    results = check_required_if(requirements, parameters)
    assert results == [
        {
            'parameter': 'someint',
            'value': 99,
            'requirements': ('bool_param', 'string_param'),
            'missing': ['bool_param', 'string_param'],
            'requires': 'all',
        }
    ]

# Generated at 2022-06-12 23:50:42.853158
# Unit test for function check_type_bits
def test_check_type_bits():
    from ansible.compat.tests import unittest
    original_method = check_type_bits(1048576)
    assert original_method == '1Mb'

# Generated at 2022-06-12 23:50:45.314251
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 2**20
    assert check_type_bits('1Gb') == 2**30
    assert check_type_bits('1Tb') == 2**40
    assert check_type_bits('1Pb') == 2**50
    assert check_type_bits('1Eb') == 2**60



# Generated at 2022-06-12 23:50:51.645615
# Unit test for function check_type_dict
def test_check_type_dict():
    # None case
    assert check_type_dict(None) is None

    # string case
    assert check_type_dict("key1=value1,key2=value2") == {'key1': 'value1', 'key2': 'value2'}

    # dict case
    assert check_type_dict({'key1': 'value1', 'key2': 'value2'}) == {'key1': 'value1', 'key2': 'value2'}

    # invalid case
    with pytest.raises(TypeError, match="123: is not a dict"):
        check_type_dict(123)



# Generated at 2022-06-12 23:50:55.461961
# Unit test for function check_required_arguments
def test_check_required_arguments():
    import pytest
    argument_spec = {'parameter1': {'type': 'str', 'required': True},
                     'parameter2': {'type': 'str', 'required': False}}
    parameters1 = {'parameter1':'test'}
    parameters2 = {'parameter2':'test'}
    parameters3 = {}
    with pytest.raises(TypeError):
        check_required_arguments(argument_spec, parameters2)
    with pytest.raises(TypeError):
        check_required_arguments(argument_spec, parameters3)
    assert check_required_arguments(argument_spec, parameters1) == []



# Generated at 2022-06-12 23:51:04.677717
# Unit test for function check_required_by
def test_check_required_by():
    # Test 1 - Require two different keys with two different requirements
    requirements = dict()
    requirements['key1'] = 'key2'
    requirements['key3'] = 'key4'
    parameters = dict()
    parameters['key1'] = 'value1'
    parameters['key3'] = 'value3'
    try:
        result = check_required_by(requirements, parameters)
        assert {} == result
    except AttributeError:
        # Test 2 - Require one key with two requirements
        requirements = dict()
        requirements['key1'] = ['key2', 'key3']
        parameters = dict()
        parameters['key1'] = 'value1'

# Generated at 2022-06-12 23:51:16.264325
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(0) == 0
    assert check_type_bytes(1) == 1
    assert check_type_bytes(1024) == 1024
    assert check_type_bytes(102400) == 102400
    assert check_type_bytes('100K') == 100*1024
    assert check_type_bytes('1M') == 1024*1024
    assert check_type_bytes('1G') == 1024*1024*1024
    assert check_type_bytes('100KB') == 100*1024
    assert check_type_bytes('1MB') == 1024*1024
    assert check_type_bytes('1GB') == 1024*1024*1024
    assert check_type_bytes('1T') == 1024*1024*1024*1024

# Generated at 2022-06-12 23:51:25.611713
# Unit test for function check_required_by
def test_check_required_by():
    requirements = {'key': ['a', 'b', 'c'], 'key2': ['d', 'e']}
    parameters1 = {'key': 1, 'a': 1, 'b': 1}
    parameters2 = {'key2': 1, 'e': 1, 'f': 1}
    parameters3 = {'key': 1, 'key2': 1, 'a': 1, 'e': 1, 'f': 1}
    parameters4 = {'key': 1, 'key2': 1, 'a': 1, 'e': 1, 'b': 1}
    res1 = check_required_by(requirements, parameters1)
    res2 = check_required_by(requirements, parameters2)
    res3 = check_required_by(requirements, parameters3)

# Generated at 2022-06-12 23:51:30.627282
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """Test function check_type_bytes"""
    assert check_type_bytes(1) == 1
    assert check_type_bytes('10') == 10
    assert check_type_bytes('1k') == 1024
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1G') == 1073741824



# Generated at 2022-06-12 23:51:37.613924
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval('{}') == {}
    assert safe_eval('[]') == []
    assert safe_eval('foo') == 'foo'
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('1') == 1
    assert safe_eval('["foo", "bar"]') == ['foo', 'bar']
    assert safe_eval('[1, "foo", ["bar", "baz"]]') == [1, 'foo', ['bar', 'baz']]
    assert safe_eval('{"foo": "bar"}') == {'foo': 'bar'}
    assert safe_eval('{"foo": ["bar", "baz"]}') == {'foo': ['bar', 'baz']}

# Generated at 2022-06-12 23:51:39.947564
# Unit test for function check_type_int
def test_check_type_int():
   result = check_type_int(2)
   assert result==2
   result = check_type_int('2')
   assert result==2



# Generated at 2022-06-12 23:51:56.160071
# Unit test for function check_type_dict
def test_check_type_dict():
    # Test for json strings
    assert check_type_dict('{"foo": "bar"}') == {"foo": "bar"}
    assert check_type_dict('{"foo": "bar", "fizz": "buzz"}') == {"foo": "bar", "fizz": "buzz"}
    assert check_type_dict('{"foo": "bar", "fizz": "buzz", "bizz": {"foo": "bar"}}') == {"foo": "bar", "fizz": "buzz", "bizz": {"foo": "bar"}}
    # Test for key=value pairs
    assert check_type_dict('foo=bar') == {'foo': 'bar'}
    assert check_type_dict('foo="bar"') == {'foo': 'bar'}

# Generated at 2022-06-12 23:52:02.680382
# Unit test for function safe_eval
def test_safe_eval():
    assert 10 == safe_eval("10")
    assert 10 == safe_eval(10)
    assert "10" == safe_eval("'10'")
    assert "10" == safe_eval("\"10\"")
    assert [1, 2, 3] == safe_eval("[1,2,3]")
    assert (1, 2, 3) == safe_eval("(1,2,3)")
    assert {"a": "b", "c": "d"} == safe_eval("{'a': 'b', 'c': 'd'}")
    assert [1, 2, 3] == safe_eval("{1,2,3}")
    assert 'import os' == safe_eval('import os')
    assert 'internet.com' == safe_eval('internet.com')
    assert 'internet.com' == safe_eval

# Generated at 2022-06-12 23:52:12.936450
# Unit test for function check_required_by
def test_check_required_by():
    reqs = {
        "1": ["2", "3"],
        "4": "5",
    }
    check_required_by(reqs, {"1": "r", "2": "r", "3": "r", "4": "r", "5": "r"})
    check_required_by(reqs, {"1": "r", "2": "r", "5": "r"})
    check_required_by(reqs, {"1": "r", "3": "r", "5": "r"})
    check_required_by(reqs, {"1": "r", "3": "r"})
    check_required_by(reqs, {"4": "r", "5": "r"})



# Generated at 2022-06-12 23:52:22.226477
# Unit test for function check_type_dict

# Generated at 2022-06-12 23:52:29.350025
# Unit test for function check_type_int
def test_check_type_int():
    result_type = type(check_type_int(value=1))
    assert result_type is int, 'Expected result_type is int, but result_type is "%s"' % result_type
    result_type = type(check_type_int(value=1.5))
    assert result_type is float, 'Expected result_type is float, but result_type is "%s"' % result_type
    result_type = type(check_type_int(value='a'))
    assert result_type is str, 'Expected result_type is str, but result_type is "%s"' % result_type

    try:
        check_type_int(value='a')
    except TypeError:
        pass
    else:
        assert False, 'check_type_int(value=a) excepion is expected'




# Generated at 2022-06-12 23:52:32.370811
# Unit test for function check_type_bits
def test_check_type_bits():
    p = check_type_bits('1Mb')
    assert p == 1048576


# Generated at 2022-06-12 23:52:41.360197
# Unit test for function check_type_float
def test_check_type_float():
    test_value1 = 2
    test_value2 = 2.0
    test_value3 = "2.0"
    test_value4 = "2"
    test_value5 = "'2'"
    test_value6 = 2.5

    for value in [test_value1,test_value2,test_value3,test_value4,test_value5,test_value6]:
        result = check_type_float(value)
        print("input value: %s, type: %s, output value: %s, type: %s" %(value,type(value),result,type(result)))
        print("\n")


# Generated at 2022-06-12 23:52:52.885223
# Unit test for function check_required_if
def test_check_required_if():
    class TestCase(object):
        def __init__(self, data, results):
            self.data = data
            self.results = results
            assert check_required_if(self.data['req'], self.data['params']) == self.results

    arg_spec = dict(
        one=dict(type='str', required=True),
        two=dict(type='int', required=True),
        three=dict(type='int', required=True),
        four=dict(type='int', required=True),
    )


# Generated at 2022-06-12 23:52:54.461930
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576


# Generated at 2022-06-12 23:53:01.730062
# Unit test for function check_required_together
def test_check_required_together():
    """ Test function check_required_together """
    parameters = {'a': 1, 'b': 2, 'c': 3}
    options_context = ('a', 'b', 'c')
    terms = (
        ('a', 'b', 'c'),
        ('x', 'y', 'z')
    )
    # Case where all options present
    check_required_together(terms, parameters, options_context)
    # Case where all options absent
    check_required_together(terms, dict(), options_context)
    # Case where some options present
    with pytest.raises(TypeError):
        check_required_together(terms, {'a': 1}, options_context)
    # Case where some options absent

# Generated at 2022-06-12 23:53:10.118550
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # This function is called by another function which tests it,
    # so there is no rationale for unit testing here
    pass



# Generated at 2022-06-12 23:53:15.087767
# Unit test for function safe_eval
def test_safe_eval():
    # Strings should be passed through
    assert safe_eval('foo') == 'foo'
    # But anything else should be evaluated
    assert safe_eval('1+1') == 2
    # And complex data types too
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}



# Generated at 2022-06-12 23:53:24.303258
# Unit test for function check_type_dict
def test_check_type_dict():
    def assert_dict(value, expected_value):
        result = check_type_dict(value)
        assert result == expected_value, (result, expected_value)

    for key in ['str', 'str_with_comma', 'str_with_equal']:
        value = dict_test_data[key]
        assert_dict(value, value)

    assert_dict(dict_test_data['str_with_one_kvpair'], dict_test_data['dict_with_one_kvpair'])
    assert_dict(dict_test_data['str_with_multiple_kvpair'], dict_test_data['dict_with_multiple_kvpair'])

# Generated at 2022-06-12 23:53:31.495163
# Unit test for function safe_eval

# Generated at 2022-06-12 23:53:42.468028
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('1.01') == 1.01
    assert safe_eval(u'u"foo"') == u'foo'
    assert safe_eval(u'"foo"') == u'foo'
    # safe_eval should allow b"foo" and "foo"
    assert safe_eval(u'"foo"') == u'foo'
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('{"a":"b"}') == {"a":"b"}

    # safe_eval should disallow "import os" but allow b"import os"
    assert safe_eval('import os') == u'import os'
    assert safe_eval(u'import os') == u'import os'

    # safe_eval should not allow "

# Generated at 2022-06-12 23:53:47.547689
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1,2,3,4]') == [1, 2, 3, 4]
    assert safe_eval('foobar') == 'foobar'
    assert safe_eval('{{foobar}}') == '{{foobar}}'
    assert safe_eval('[1,2,3,4][0]') == 1
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('import foo') == 'import foo'



# Generated at 2022-06-12 23:53:58.892139
# Unit test for function check_required_by
def test_check_required_by():
    try:
        requirements = {
            'key_1': ['key_1_requirement'],
            'key_2': ['key_2_requirement', 'key_1_requirement']
        }
        parameters = {
            'key_1': 'value_1',
            'key_2': 'value_2'
        }
        check_required_by(requirements, parameters)
    except Exception as e:
        assert False, "check_required_by raises unexpected exception: {}".format(e)

# Generated at 2022-06-12 23:54:08.940134
# Unit test for function safe_eval
def test_safe_eval():
    from unittest import TestCase
    from ansible.module_utils.common.text.converters import to_text
    class TestSafeEval(TestCase):
        def test_string(self):
            value = u'test'
            result = safe_eval(value)
            self.assertEqual(value, to_text(result))

        def test_string_quotes(self):
            value = u'test'
            result = safe_eval(u"'%s'" % value)
            self.assertEqual(value, to_text(result))

        def test_string_double_quotes(self):
            value = u'test'
            result = safe_eval(u'"%s"' % value)
            self.assertEqual(value, to_text(result))


# Generated at 2022-06-12 23:54:17.625917
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.2) == 1.2
    assert check_type_float(1) == 1.0
    assert check_type_float('1.2') == 1.2
    assert check_type_float(b'1.2') == 1.2
# Commented out for now as this test fails on Python 3
#    assert check_type_float(u'1.2') == 1.2

    with pytest.raises(TypeError):
        check_type_float(['1.2'])



# Generated at 2022-06-12 23:54:27.277854
# Unit test for function check_required_by
def test_check_required_by():
    #pass
    required_by_dict = {'a': ['b', 'c'], 'd': 'e'}
    parameters_1 = {'a': 'a', 'b': 'b'}
    parameters_2 = {'a': 'a', 'b': 'b', 'c': 'c'}
    parameters_3 = {'a': 'a', 'e': 'e'}
    parameters_4 = {'a': 'a', 'e': 'e', 'b': 'b'}
    parameters_5 = {'a': 'a', 'e': 'e', 'c': 'c'}
    #if the second parameters is default parameters (None), it will return empty dictionary
    assert check_required_by(None, None) == {}
    #if the second parameters is empty dictionary, it will raise TypeError
    #

# Generated at 2022-06-12 23:54:37.507443
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('a') == 'a'
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('a.split()', include_exceptions=True) == ('a.split()', None)
    assert safe_eval('import os', include_exceptions=True) == ('import os', None)
    assert safe_eval('[1, 2]') == [1, 2]



# Generated at 2022-06-12 23:54:43.598429
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict("{'key': 'value'}") == {'key': 'value'}
    assert check_type_dict("{'key': 'value', 'key2': 'value2'}") == {'key': 'value', 'key2': 'value2'}
    assert check_type_dict("key=value") == {'key': 'value'}
    assert check_type_dict("key=value, key2=value2") == {'key': 'value', 'key2': 'value2'}
    assert check_type_dict("key='value', key2=value2") == {'key': 'value', 'key2': 'value2'}
    assert check_type_dict("key=\"value\", key2=value2") == {'key': 'value', 'key2': 'value2'}

# Generated at 2022-06-12 23:54:55.199788
# Unit test for function check_type_dict
def test_check_type_dict():
    """Test that check_type_dict behaves as expected."""
    check_type_dict("{'a':'b', 'c':'d'}")
    check_type_dict("a='b', c='d'")
    check_type_dict("a='b', c='d', e='f'")
    check_type_dict("{a:b, 'c':'d'}")
    check_type_dict("{a:'b', c:'d'}")
    check_type_dict("{'a': b, c: 'd'}")
    check_type_dict("{'a': b, 'c': 'd'}") # shouldn't work
    check_type_dict({'a':'b', 'c':'d'})
    check_type_dict({'a':'b'})



# Generated at 2022-06-12 23:54:59.405355
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int("1") == 1
    assert check_type_int(1.1) != 1
    assert check_type_int("1.1") == 1


# Generated at 2022-06-12 23:55:06.754443
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1) == 1.0
    assert check_type_float(1.0) == 1.0
    assert check_type_float('1') == 1.0
    assert check_type_float(b'1') == 1.0
    assert_raises(TypeError, check_type_float, '1a')
    assert_raises(TypeError, check_type_float, b'1a')
    assert_raises(TypeError, check_type_float, object)



# Generated at 2022-06-12 23:55:11.380193
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int('1') == 1
    try:
        check_type_int(1.0)
    except TypeError:
        pass
    else:
        assert False


# Generated at 2022-06-12 23:55:21.691964
# Unit test for function check_type_dict
def test_check_type_dict():
    if check_type_dict({'k1': 'v1', 'k2': 'v2'}) != {'k1': 'v1', 'k2': 'v2'}:
        raise AssertionError('Expected dictionary not returned')
    if check_type_dict('k1=v1, k2=v2') != {'k1': 'v1', 'k2': 'v2'}:
        raise AssertionError('Expected dictionary not returned')
    if check_type_dict('{\'k1\': \'v1\', \'k2\': \'v2\'}') != {'k1': 'v1', 'k2': 'v2'}:
        raise AssertionError('Expected dictionary not returned')

# Generated at 2022-06-12 23:55:23.608510
# Unit test for function check_type_int
def test_check_type_int():
    int1 = 3
    res1 = check_type_int(int1)

# Generated at 2022-06-12 23:55:35.015386
# Unit test for function check_type_dict
def test_check_type_dict():
    """Unit tests for function check_type_dict"""

    assert(check_type_dict("") == {})
    assert(check_type_dict("  ") == {})
    assert(check_type_dict("a") == {"a": ""})
    assert(check_type_dict("a=") == {"a": ""})
    assert(check_type_dict("a=  ") == {"a": ""})
    assert(check_type_dict("a=b") == {"a": "b"})
    assert(check_type_dict("a= b") == {"a": "b"})
    assert(check_type_dict(" a=b ") == {"a": "b"})
    assert(check_type_dict("a=''") == {"a": ""})

# Generated at 2022-06-12 23:55:36.787042
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval(42) == 42



# Generated at 2022-06-12 23:55:45.243784
# Unit test for function check_required_together
def test_check_required_together():
    assert check_required_together(['host', 'username', 'password'], {'host': 'hostname', 'username': 'user', 'password': 'pass'})
    try:
        check_required_together(['host', 'username', 'password'], {'host': 'hostname', 'password': 'pass'})
    except TypeError as e:
        assert "parameters are required together: host, username, password" in str(e)
        assert "found in" in str(e)
    else:
        assert False, "Exception not raised when it's supposed to."



# Generated at 2022-06-12 23:55:58.476750
# Unit test for function check_type_bytes

# Generated at 2022-06-12 23:56:05.994516
# Unit test for function check_type_bits
def test_check_type_bits():
    '''Unit test for check_type_bits'''
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('2Mb') == 2097152
    assert check_type_bits('3Mb') == 3145728
    assert check_type_bits('4Mb') == 4194304
    assert check_type_bits('5Mb') == 5242880

# Generated at 2022-06-12 23:56:10.535659
# Unit test for function check_type_bits
def test_check_type_bits():
    expected_value = 8
    real_value = check_type_bits('1B')
    assert real_value == expected_value, "check_type_bits %s returns %s" % \
        (expected_value, real_value)


# FIXME: Why are we sorting the keys?  Shouldn't the order be preserved?

# Generated at 2022-06-12 23:56:17.267042
# Unit test for function check_type_bytes

# Generated at 2022-06-12 23:56:27.240035
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # test for correct list types
    terms = 'correct terms'
    parameters = 'correct parameters'
    list_terms=[[terms]]
    assert check_mutually_exclusive(list_terms, parameters) == []
    # test for incorrect list types
    list_terms = [terms, parameters]
    assert check_mutually_exclusive(list_terms, parameters) == [terms, parameters]
    # test for incorrect arguments
    with pytest.raises(TypeError) as exception:
        check_mutually_exclusive(None,None)
    assert exception.type == TypeError



# Generated at 2022-06-12 23:56:37.235693
# Unit test for function check_required_one_of
def test_check_required_one_of():
    # test with two lists with one item in each
    params = {'foo': 'bar'}
    terms = [['foo'], ['bar']]
    try:
        check_required_one_of(terms, params)
    except TypeError:
        pass
    except Exception as e:
        raise e
    else:
        raise Exception('check_required_one_of failed to raise an exception')
    # test with a list with two items
    params = {'foo': 'bar', 'test': 'hope'}
    terms = [['foo', 'test']]
    try:
        check_required_one_of(terms, params)
    except TypeError:
        pass
    except Exception as e:
        raise e
    else:
        raise Exception('check_required_one_of failed to raise an exception')
   

# Generated at 2022-06-12 23:56:47.431473
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]

    # Testing case 1
    # all required parameters present
    parameters = {
        'state': "present",
        'path': True,
        'someint': 99,
        'bool_param': True,
        'string_param': "true"
    }
    results = check_required_if(requirements, parameters)
    assert not results

    # Testing case 2
    # one of the required parameters present as required_if is_one_of=True
    parameters = {
        'state': "present",
        'path': True,
        'someint': 99,
        'bool_param': True
    }

# Generated at 2022-06-12 23:56:50.120511
# Unit test for function check_type_int
def test_check_type_int():
    res = check_type_int("10")
    assert res == 10
    res = check_type_int(10)
    assert res == 10
    


# Generated at 2022-06-12 23:57:00.404271
# Unit test for function check_required_if
def test_check_required_if():
    from ansible.module_utils.parsing.convert_bool import boolean
    import sys

    # None input
    requirements = None
    parameters = {}
    options_context = None
    if PY3:
        result = check_required_if(requirements, parameters, options_context)
    else:
        try:
            result = check_required_if(requirements, parameters, options_context)
        except TypeError as e:
            result = e.args[0]

    assert result == []

    # empty list
    requirements = []
    parameters = {}
    options_context = None
    if PY3:
        result = check_required_if(requirements, parameters, options_context)

# Generated at 2022-06-12 23:57:16.465718
# Unit test for function check_type_float
def test_check_type_float():
    from ansible.module_utils.common.validation import check_type_float
    import math
    assert(math.isclose(check_type_float('0.0'), 0.0))
    assert(math.isclose(check_type_float('1.0'), 1.0))
    assert(math.isclose(check_type_float('-3.14159'), -3.14159))
    assert(math.isclose(check_type_float('nan'), float('nan')))
    # Some implementations of Python 2.7 won't accept
    # the literals 'infinity' and 'nan', but Python 3 will.
    #assert(math.isclose(check_type_float('infinity'), float('infinity')))
    assert(math.isclose(check_type_float('inf'), float('inf')))
   

# Generated at 2022-06-12 23:57:17.435701
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576



# Generated at 2022-06-12 23:57:21.231824
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int("2") == 2
    try:
        check_type_int("asdf")
        assert False
    except TypeError:
        pass
    try:
        check_type_int([1, 2])
        assert False
    except TypeError:
        pass
    try:
        check_type_int({1: 2})
        assert False
    except TypeError:
        pass



# Generated at 2022-06-12 23:57:26.647922
# Unit test for function check_required_by
def test_check_required_by():
    parameters = {'key': 'value'}
    requirements = {'key': 'missing'}
    options_context = None
    result = check_required_by(requirements, parameters, options_context)
    assert len(result) == 1
    assert result['key'] == ['missing']
    requirements = {'key': ['missing']}
    result = check_required_by(requirements, parameters, options_context)
    assert len(result) == 1
    assert result['key'] == ['missing']
    parameters = {'key': 'value', 'missing': 'value_missing'}
    result = check_required_by(requirements, parameters, options_context)
    assert len(result) == 0



# Generated at 2022-06-12 23:57:38.017009
# Unit test for function check_required_one_of
def test_check_required_one_of():

    #Basic test with valid parameter
    assert check_required_one_of([['one', 'two']], {'one':'1','two':'2'}) == []

    #Basic test with empty parameter
    assert check_required_one_of([['one', 'two']], {}) == [['one', 'two']]

    #Basic test with partial parameter
    assert check_required_one_of([['one', 'two']], {'two':'2'}) == []

    #Basic test with missing parameter
    assert check_required_one_of([['one', 'two']], {'three':'3'}) == [['one', 'two']]

    #Basic test with multiple missing parameter

# Generated at 2022-06-12 23:57:48.317949
# Unit test for function check_required_one_of
def test_check_required_one_of():
    try:
        check_required_one_of([['a', 'b'], ['c', 'd']], {'b': 1, 'd': 1})
        assert True
    except TypeError:
        assert False

    try:
        check_required_one_of([['a', 'b'], ['c', 'd']], {'b': 1, 'c': 1})
        assert True
    except TypeError:
        assert False

    try:
        check_required_one_of([['a', 'b'], ['c', 'd']], {'b': 1, 'e': 1})
        assert False
    except TypeError:
        assert True


# Generated at 2022-06-12 23:57:55.864040
# Unit test for function safe_eval

# Generated at 2022-06-12 23:57:58.946684
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1024kb') == 1048576



# Generated at 2022-06-12 23:58:07.053725
# Unit test for function check_type_bytes
def test_check_type_bytes():
    import pytest

    test_data = ['123kB', '123kB', '123M', '123b', '123k', '123G', '123B', '1234']
    for value in test_data:
        assert check_type_bytes(value) == human_to_bytes(value)
    with pytest.raises(TypeError):
        check_type_bytes('123h')
    with pytest.raises(TypeError):
        check_type_bytes(1234)



# Generated at 2022-06-12 23:58:13.801793
# Unit test for function check_required_if
def test_check_required_if():
    try:
        fake_parameters = {'state': 'present', 'path': 'test'}
        fake_requirements = [['state', 'present', ('path',), True]]
        result = check_required_if(fake_requirements, fake_parameters)
        assert len(result) == 0
    except Exception as error:
        assert False, 'check_required_if failed'

    try:
        fake_parameters = {'state': 'absent'}
        fake_requirements = [['state', 'present', ('path',), False]]
        result = check_required_if(fake_requirements, fake_parameters)
        assert len(result) == 0
    except Exception as error:
        assert False, 'check_required_if failed'


# Generated at 2022-06-12 23:58:37.050712
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1k') == 1024
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1kb') == 1024
    assert check_type_bytes('1KB') == 1024
    assert check_type_bytes('1 m') == 1000000
    assert check_type_bytes('1M') == 1000000
    assert check_type_bytes('1MB') == 1000000
    assert check_type_bytes('1mb') == 1000000
    assert check_type_bytes('1 g') == 1000000000
    assert check_type_bytes('1G') == 1000000000
    assert check_type_bytes('1gb') == 1000000000
    assert check_type_bytes('1GB') == 1000000000
    assert check_type_bytes('1 t') == 1000000000000
    assert check_type_bytes