

# Generated at 2022-06-12 23:49:20.006483
# Unit test for function check_required_together
def test_check_required_together():
    assert check_required_together(
        [
            ['name', 'image', 'flavor'],
            ['size', 'image', 'flavor']
        ],
        {'name': 'foo', 'flavor': 'm1.tiny'},
    ) == []

    # Check case where 2 of 3 are provided, but neither of the 2 are from the same set
    with pytest.raises(TypeError) as exec_info:
        check_required_together(
            [
                ['name', 'image', 'flavor'],
                ['size', 'image', 'flavor']
            ],
            {'name': 'foo', 'size': '10GB'},
        )
    assert to_native(exec_info.value) == "parameters are required together: name, image, flavor"

    # Check case where 1 of 3 is

# Generated at 2022-06-12 23:49:30.995481
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert check_mutually_exclusive([['a', 'b']], {'a': 1, 'b': 2}) == [
        ['a', 'b']
    ]
    assert check_mutually_exclusive([['a', 'b']], {'a': 1, 'b': 2}, ['key1', 'key2']) == [
        ['a', 'b']
    ]
    assert check_mutually_exclusive([['a', 'b']], {'a': 1, 'c': 2}) == []
    assert check_mutually_exclusive([['a', 'b']], {'c': 1, 'd': 2}) == []
    assert check_mutually_exclusive(['a', 'b'], {'a': 1, 'c': 2}) == []

# Generated at 2022-06-12 23:49:39.244489
# Unit test for function safe_eval
def test_safe_eval():
    import pytest
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('None') is None
    with pytest.raises(Exception):
        safe_eval('import os')
    with pytest.raises(Exception):
        safe_eval('subprocess.call')
    with pytest.raises(Exception):
        safe_eval('subprocess.call()')
    assert safe_eval('subprocess.call', include_exceptions=True)[1]



# Generated at 2022-06-12 23:49:50.635113
# Unit test for function check_required_together

# Generated at 2022-06-12 23:49:59.068057
# Unit test for function check_required_if
def test_check_required_if():
    args = {
            'state': 'present',
            'name': 'test',
            'path': 'test',
            'bool_param': True,
            'string_param': 'test'
            }
    # Testing to fail when any/all required parameters are missing
    ri_requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
        ['someint', 99, ('bool_param', 'string_param'), False],
        ]

    try:
        check_required_if(ri_requirements, args)
    except TypeError as e:
        for missing in e.results:
            assert 'missing' in missing
            assert 'requires' in missing
            assert 'parameter' in missing

# Generated at 2022-06-12 23:50:07.367811
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    from .test_utils import ModuleTestCase, set_module_args

    class TestError(ModuleTestCase):
        def test_error_required_mutually_exclusive_options(self, *args, **kwargs):
            set_module_args(dict(state='absent', force='yes',
                                 name='test_spec.yml', path='/tmp'))
            result = self.execute_module(failed=True)
            self.assertEqual(result['msg'], 'parameters are mutually exclusive: force|state')


# Generated at 2022-06-12 23:50:18.293966
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    parameters = dict(one=1, two=2, three=3)

    # Basic check
    assert check_mutually_exclusive([['one', 'two']], parameters) == []

    # Basic check with errors
    try:
        check_mutually_exclusive([['one', 'two'], ['two', 'three']], parameters)
    except TypeError as e:
        assert e.args[0] == "parameters are mutually exclusive: one|two, two|three"

    # Check in a sub spec
    try:
        check_mutually_exclusive([['one', 'two'], ['two', 'three']], parameters, options_context=['spec', 'x'])
    except TypeError as e:
        assert e.args[0] == "parameters are mutually exclusive: one|two, two|three found in spec -> x"



# Generated at 2022-06-12 23:50:24.290666
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{"key":"value"}') == {"key": "value"}
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('1+2') == 3
    assert safe_eval('w.w') == 'w.w'
    assert safe_eval('import w') == 'import w'
    assert safe_eval('w.w()') == 'w.w()'



# Generated at 2022-06-12 23:50:35.263480
# Unit test for function check_required_by
def test_check_required_by():
    # Requirements are satisfied; the dict should be empty
    test_requirements = {'key1': ['required1', 'required2'],
                         'key2': ['required3'],
                         'key3': ['required4', 'required5']}
    test_params = {
        'key1': 'foo',
        'key2': 'bar',
        'key3': 'baz',
        'required1': 1,
        'required2': 2,
        'required3': 3,
        'required4': 4,
        'required5': 5
    }
    test_result = check_required_by(test_requirements, test_params)
    assert len(test_result) == 0
    # Required value missing; should return dict with keys of requirements
    # that were not met

# Generated at 2022-06-12 23:50:43.322012
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1.1Mb') == 1179648
    assert check_type_bits(' 1.1 Mb ') == 1179648
    assert check_type_bits('1024k') == 1048576
    assert check_type_bits('10Kb') == 10240
    assert check_type_bits('10b') == 10

    assert check_type_bits('1M') == 1048576 * 8
    assert check_type_bits('1.1M') == 1179648 * 8
    assert check_type_bits(' 1.1 M ') == 1179648 * 8
    assert check_type_bits('1024k') == 1048576 * 8
    assert check_type_bits('10K') == 10240 * 8
    assert check_

# Generated at 2022-06-12 23:50:52.912105
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments(argument_spec=None, parameters=None) == []
    try:
        assert check_required_arguments(argument_spec={'required_one': {'required': True},
                                                        'required_two': {'required': True}},
                                         parameters={'required_one': 'one'}) == []
    except TypeError as e:
        assert 'missing required arguments' in str(e)
        assert 'required_two' in str(e)

# Generated at 2022-06-12 23:50:55.850662
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    # Parameters is empty
    parameters = {}
    req_params = ['test1', 'test2']
    result = check_missing_parameters(parameters, req_params)
    assert result[0] == 'test1'
    assert result[1] == 'test2'
    # Parameters passed in
    parameters = {'test1':'', 'test2':'', 'test3':'', 'test4':''}
    result = check_missing_parameters(parameters, req_params)
    assert result == []



# Generated at 2022-06-12 23:51:01.679105
# Unit test for function check_required_together
def test_check_required_together():
    terms = [('name','other'), ('other','xxx')]
    parameters = {'other': 'other1', 'name': 'name1'}
    results = check_required_together(terms, parameters)
    assert results == []
    parameters = {'other': 'other1'}
    try:
        results = check_required_together(terms, parameters)
    except TypeError as e:
        assert "parameters are required together: name, other" in str(e)


# Generated at 2022-06-12 23:51:08.794780
# Unit test for function check_required_by
def test_check_required_by():
    assert check_required_by(None, None) == {}
    assert check_required_by({}, {}) == {}
    assert check_required_by({'key': 'val'}, {}) == {}
    assert check_required_by({'key': 'val'}, {'key': None}) == {}
    assert check_required_by({'key': 'val'}, {'key': 'val'}) == {}
    assert check_required_by({'key': 'val'}, {'key': 'val', 'val': 'other'}) == {}

    assert check_required_by({'key': 'val'}, {'key': 'other'}) == {'key': ['val']}
    assert check_required_by({'key': ['val', 'other']}, {'key': 'other'}) == {'key': ['val']}

# Generated at 2022-06-12 23:51:10.635948
# Unit test for function check_type_float
def test_check_type_float():
    # Checks if the function works correctly or not
    assert check_type_float(10.0) == 10.0



# Generated at 2022-06-12 23:51:21.229695
# Unit test for function check_required_by
def test_check_required_by():
    # Test with an empty dict
    requirements = {}
    try:
        check_required_by(requirements, dict())
    except TypeError as e:
        assert False, 'Empty dicts should not throw TypeError'

    # Test with requirements that exist in parameters
    requirements = {
        'a': 'b',
        'c': 'd',
        'e': ['f', 'g'],
        'h': ['i', 'j', 'k'],
    }
    parameters = {
        'a': 'foo',
        'c': 'bar',
        'e': 'baz',
        'f': 1,
        'g': 2,
        'h': 'qux',
        'i': 3,
        'j': 4,
        'k': 5
    }

# Generated at 2022-06-12 23:51:29.025025
# Unit test for function check_required_if
def test_check_required_if():
    try:
        check_required_if([['a', 'b', ['c']]], {})
    except TypeError as te:
        assert str(te) == "a is b but all of the following are missing: c"
    else:
        assert False, "check_required_if with missing parameters did not raise an exception"

    try:
        check_required_if([['a', 'b', ['c']]], {'c': 'd'})
    except TypeError as te:
        assert str(te) == "a is b but all of the following are missing: c"
    else:
        assert False, "check_required_if with missing parameters did not raise an exception"


# Generated at 2022-06-12 23:51:40.187713
# Unit test for function check_type_int
def test_check_type_int():
    for value in (0, "0", 0.0, "0.0"):
        assert check_type_int(value) == 0
    for value in ("1", 1):
        assert check_type_int(value) == 1
    for value in ("-1", -1):
        assert check_type_int(value) == -1
    for value in (1.0, "1.0"):
        assert check_type_int(value) == 1
    for value in ("-1.0", -1.0):
        assert check_type_int(value) == -1
    for value in (0.1, "0.1"):
        with pytest.raises(TypeError):
            check_type_int(value)

# Generated at 2022-06-12 23:51:51.661406
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict({"a": "b"}) == {"a": "b"}
    assert check_type_dict('{"a": "b"}') == {"a": "b"}
    assert check_type_dict(' a=b,  c = d') == {"a": "b", "c": "d"}
    assert check_type_dict('a=b,c=d') == {"a": "b", "c": "d"}
    assert check_type_dict('a=b \\, c=d') == {"a": "b, c", "d": ""}
    assert check_type_dict('a="b, c", d="e"') == {"a": "b, c", "d": "e"}

# Generated at 2022-06-12 23:51:54.146465
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    # required_parameters is None
    assert check_missing_parameters({"a":"a"}, None) == []
    assert check_missing_parameters({"a":"a"}, ["a"]) == []
    assert check_missing_parameters({"a":"a"}, ["a", "b"]) == ["b"]
    assert check_missing_parameters({"a":"a", "c":"c"}, ["a", "b"]) == ["b"]


# Generated at 2022-06-12 23:52:08.577719
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Test the returned list of missing required arguments
    assert check_required_arguments({'arg1': {'required': True}, 'arg2': {'required': True}, 'arg3': {'required': True}}, {'arg1': 'test', 'arg3': 'test'}) == ['arg2']
    assert check_required_arguments({'arg1': {'required': True}}, {}) == ['arg1']
    assert check_required_arguments({'arg1': {'required': False}}, {}) == []
    assert check_required_arguments({'arg1': {'required': False}}, {'arg1': ''}) == []

# Generated at 2022-06-12 23:52:19.256488
# Unit test for function safe_eval
def test_safe_eval():

    import pytest
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils.six import integer_types, string_types
    from ansible.module_utils.parsing.convert_bool import boolean

    from ansible.module_utils.common.text.converters import to_text


# Generated at 2022-06-12 23:52:26.354672
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Kb') == 1024
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1MB') == 1048576
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1 mb') == 1048576
    assert check_type_bits('1 mB') == 1048576
    assert check_type_bits('1 m') == 1048576
    assert check_type_bits('1M') == 1048576
    assert check_type_bits('1 mibibyte') == 1048576
    assert check_type_bits('1 mibibits') == 1048576



# Generated at 2022-06-12 23:52:30.768733
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(5) == 5.0
    assert check_type_float('5') == 5.0
    assert check_type_float(5.0) == 5.0
    assert check_type_float(u'5.0') == 5.0
    assert check_type_float(b'5.0') == 5.0
    assert check_type_float('5.0') == 5.0
    assert check_type_float(u'a')
    assert check_type_float(b'a')

# Generated at 2022-06-12 23:52:37.525839
# Unit test for function check_type_int
def test_check_type_int():
    s = '123'
    i = 123
    f = 123.0
    b = True
    lists = ['123', 123, 123.0]
    for l in lists:
        assert check_type_int(l) == 123

    # Test for exception
    l = [True]
    for l in lists:
        try:
            assert check_type_int(l) == 123
        except TypeError:
            return



# Generated at 2022-06-12 23:52:41.579025
# Unit test for function check_type_int
def test_check_type_int():
    try:
        check_type_int('test')
        assert False
    except TypeError:
        pass

    assert check_type_int(1) == 1
    assert check_type_int('1') == 1
    assert check_type_int(u'15') == 15



# Generated at 2022-06-12 23:52:44.227212
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("1MB") == (1024 * 1024)
    assert check_type_bytes("10m") == (1024 * 1024 * 10)



# Generated at 2022-06-12 23:52:55.492491
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1") == 1
    assert safe_eval("'hello'") == "hello"
    assert safe_eval("1,2") == (1, 2)
    assert safe_eval("(1,2)") == (1, 2)
    assert safe_eval("{'hello': 'world'}") == {'hello': 'world'}
    assert safe_eval("complex(1, 2)") == complex(1, 2)
    assert safe_eval("1.123") == 1.123
    assert safe_eval("1.0e-10") == 1.0e-10
    assert safe_eval("'hello'.join(['1', '2'])", include_exceptions=True)[0] == "'hello'.join(['1', '2'])"

# Generated at 2022-06-12 23:52:58.799691
# Unit test for function check_required_together
def test_check_required_together():
    terms = [["test1","test2"]]
    parameters = {"test1": "test1", "test2": "test2"}
    check_required_together(terms, parameters, ["test"])
    parameters["test1"] = ""
    check_required_together(terms, parameters, ["test"])
    parameters["test1"] = "test1"
    parameters["test2"] = ""
    with pytest.raises(TypeError):
        check_required_together(terms, parameters, ["test"])
        raise



# Generated at 2022-06-12 23:53:01.875481
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1) == 1.0
    assert check_type_float('1.0') == 1.0
    with pytest.raises(TypeError):
        check_type_float(['1.0'])
    assert check_type_float('1') == 1.0
    assert check_type_float(u'1') == 1.0
    assert check_type_float(u'1.0') == 1.0
    assert check_type_float(u'1.0') == 1.0


# Generated at 2022-06-12 23:53:16.528073
# Unit test for function safe_eval
def test_safe_eval():
    global module
    module = AnsibleModule(argument_spec={})
    case_true = [
        'True',
        'true',
        '1'
    ]
    case_false = [
        'False',
        'false',
        '0'
    ]
    case_list = [
        '["foo","bar"]'
    ]
    case_dict = [
        '{"foo":"bar"}'
    ]
    case_str = [
        '"string"',
        '"true"',
        '"false"'
    ]
    ansible_true = [
        True,
        True,
        1
    ]
    ansible_false = [
        False,
        False,
        0
    ]
    ansible_list = [
        ["foo", "bar"]
    ]
   

# Generated at 2022-06-12 23:53:24.823965
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1') == 1
    assert check_type_bits('1Kb') == 1024
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1Tb') == 1099511627776
    assert check_type_bits('1Pb') == 1125899906842624
    assert check_type_bits('1b') == 0.125
    assert check_type_bits('1Kb') == 1024
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1Tb') == 1099511627776

# Generated at 2022-06-12 23:53:33.651782
# Unit test for function check_type_float
def test_check_type_float():
    float_value=check_type_float(35)
    assert isinstance(float_value, float)
    float_value=check_type_float('35')
    assert isinstance(float_value, float)
    float_value=check_type_float(b'35')
    assert isinstance(float_value, float)
    float_value=check_type_float(u'35')
    assert isinstance(float_value, float)
    assert_raises(TypeError, check_type_float, 'abcd')
    assert_raises(TypeError, check_type_float, {'abc':123})


# Generated at 2022-06-12 23:53:37.355432
# Unit test for function check_type_bytes
def test_check_type_bytes():
    # Test for Bytes
    if b'\x00' == "":
        assert check_type_bytes('0b') == b''
    else:
        assert check_type_bytes('0b') == b'\x00'


# Generated at 2022-06-12 23:53:44.622184
# Unit test for function check_type_float
def test_check_type_float():
    f = check_type_float
    assert(f(1.1) == 1.1)
    assert(f('1.1') == 1.1)
    assert(f(1) == 1.0)
    assert(f('1') == 1.0)
    assert(f('1.0') == 1.0)
    assert(f(u'1') == 1.0)
    assert(f(u'1.0') == 1.0)

    exception = False
    try:
        f('a')
    except TypeError:
        exception = True
    assert(exception)



# Generated at 2022-06-12 23:53:47.517649
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('10G') == 10737418240
    assert check_type_bytes('10gb') == 10737418240
    assert check_type_bytes('10g') == 10737418240
    pytest.raises(TypeError, check_type_bytes, 'abcd')


# Generated at 2022-06-12 23:53:51.842845
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('8kbits') == 1024
    with pytest.raises(TypeError):
        check_type_bits('1023')


# Generated at 2022-06-12 23:54:02.527591
# Unit test for function safe_eval
def test_safe_eval():
    result, err = safe_eval('foo.bar()', include_exceptions=True)
    assert result == 'foo.bar()'
    result, err = safe_eval('foo.bar()')
    assert result == 'foo.bar()'
    result, err = safe_eval('import foo', include_exceptions=True)
    assert result == 'import foo'
    result, err = safe_eval('import foo')
    assert result == 'import foo'
    result, err = safe_eval('{foo: 1}', include_exceptions=True)
    assert result == {'foo': 1}
    result, err = safe_eval('{foo: 1}')
    assert result == {'foo': 1}
    result, err = safe_eval('[1, 4, 7]', include_exceptions=True)
    assert result

# Generated at 2022-06-12 23:54:11.419314
# Unit test for function check_type_bytes
def test_check_type_bytes():
    """Test function check_type_bytes

    The function is fairly easy to test because it's just a wrapper for
    human_to_bytes from ansible.utils.unicode (which is quite thoroughly tested).
    """

    assert(check_type_bytes('0') == 0)
    assert(check_type_bytes('-0') == 0)
    assert(check_type_bytes('1') == 1)
    assert(check_type_bytes('-1') == -1)
    assert(check_type_bytes('1.1') == 1.1)
    assert(check_type_bytes('-1.1') == -1.1)
    assert(check_type_bytes('0.1k') == 102)
    assert(check_type_bytes('0.1K') == 102)

# Generated at 2022-06-12 23:54:22.268448
# Unit test for function check_type_float
def test_check_type_float(): # Create a function
    assert isinstance (check_type_float(1.1), float) # Check if check_type_float is returning float type
    assert isinstance (check_type_float(1), float) # Check if check_type_float is returning float type
    assert isinstance (check_type_float('1'), float) # Check if check_type_float is returning float type
    assert isinstance (check_type_float(b'1'), float) # Check if check_type_float is returning float type
    assert isinstance (check_type_float(True), float) # Check if check_type_float is returning float type
    assert isinstance (check_type_float(False), float) # Check if check_type_float is returning float type
    assert isinstance (check_type_float(None), float) # Check if check_type_float

# Generated at 2022-06-12 23:54:34.815528
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('{"a": "str"}') == {"a": "str"}
    assert check_type_dict('a=1, b=2') == {"a": "1", "b": "2"}
    assert check_type_dict('{a: 1, b: 2}') == {"a": "1", "b": "2"}
    assert check_type_dict({"c": "3"}) == {"c": "3"}

    with pytest.raises(TypeError):
        check_type_dict('{"a": "str",')
    with pytest.raises(TypeError):
        check_type_dict('this, is not dict')



# Generated at 2022-06-12 23:54:38.260235
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('5g') == 5000000000



# Generated at 2022-06-12 23:54:47.017676
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int(0) == 0
    assert check_type_int('1') == 1
    assert check_type_int('0') == 0
    assert check_type_int(1234567890) == 1234567890
    assert check_type_int('1234567890') == 1234567890
    assert check_type_int(True) == 1
    assert check_type_int(False) == 0
    assert check_type_int(-1) == -1
    assert check_type_int('-1') == -1
    assert check_type_int('-0') == 0
    assert check_type_int('-1234567890') == -1234567890


# Generated at 2022-06-12 23:54:58.979452
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1')==1
    assert check_type_bytes('4b')==4
    assert check_type_bytes('1k')==1024
    assert check_type_bytes('1K')==1024
    assert check_type_bytes('1M')==1048576
    assert check_type_bytes('1kib')==1024
    assert check_type_bytes('1KiB')==1024
    assert check_type_bytes('1MiB')==1048576
    assert check_type_bytes('1mb')==1048576
    assert check_type_bytes('1MiB')==1048576
    assert check_type_bytes('1234')==1234
    assert check_type_bytes('1234.5')==1234.5


# Generated at 2022-06-12 23:55:09.336600
# Unit test for function safe_eval
def test_safe_eval():
    test_data = [
        ('5', 5),
        ('str(5)', 'str(5)'),
        ('int(5)', 5),
        ('int(\'5\')', 5),
        ('int()', 'int()'),
        ('int(\'z\')', 'int(\'z\')'),
        ('json.loads(\'{}\')', {}),
        ('json.dumps({})', 'json.dumps({})'),
        ('json.loads(True)', 'json.loads(True)'),
        ('False', False),
    ]
    for value, result in test_data:
        assert safe_eval(value, include_exceptions=True) == (result, None)
        assert not isinstance(safe_eval(value, include_exceptions=True)[0], string_types)

# Generated at 2022-06-12 23:55:17.487261
# Unit test for function check_type_float
def test_check_type_float():
    result = check_type_float(3.3)
    assert result == 3.3
    result = check_type_float(5)
    assert result == 5.0
    result = check_type_float('6')
    assert result == 6.0
    result = check_type_float(b'7')
    assert result == 7.0
    success = False
    try:
        result = check_type_float('test')
    except Exception:
        success = True
    assert success

# Testing of check type str

# Generated at 2022-06-12 23:55:28.691762
# Unit test for function check_type_bytes
def test_check_type_bytes():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    check_type_bytes('10MB')
    check_type_bytes('10M')
    check_type_bytes('10b')
    check_type_bytes('10B')
    check_type_bytes('10b')
    check_type_bytes('10bit')
    check_type_bytes('10 byte')
    check_type_bytes('1.1M')
    check_type_bytes('1.2 B')
    check_type_bytes('1.2b')
    check_type_bytes('1.2ba')
    check_type_bytes('1.2k')
    check_type_bytes('1.2K')
    check_type_bytes('1.2Ki')
    check_type_bytes('1.2kb')


# Generated at 2022-06-12 23:55:39.409402
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1MiB') == 1048576
    assert check_type_bytes('1Mib') == 1048576
    assert check_type_bytes('1.5M') == 1572864
    assert check_type_bytes('1.5MiB') == 1572864
    assert check_type_bytes('1.5Mib') == 1572864
    assert check_type_bytes('1') == 1
    assert check_type_bytes('15') == 15

    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1KB') == 1024
    assert check_type_bytes('1KiB') == 1024
    assert check_type_bytes('1Kib') == 1024

# Generated at 2022-06-12 23:55:43.689572
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("1M") == 1048576
    assert check_type_bytes("1Mi") == 1048576
    assert check_type_bytes("1MB") == 1048576
    assert check_type_bytes("1MiB") == 1048576



# Generated at 2022-06-12 23:55:46.869969
# Unit test for function check_required_together
def test_check_required_together():
    terms = [('greeting','addressee')]
    options = {'addressee':'World','greeting':'Hello'}
    try:
        check_required_together(terms, options)
    except TypeError as e:
        print(e)


# Generated at 2022-06-12 23:56:00.839909
# Unit test for function check_type_int
def test_check_type_int():
    from unittest import main, TestCase
    class TestCheckTypeInt(TestCase):
        def test_int_returns_int(self):
            value = 1
            exp = 1
            act = check_type_int(value)
            self.assertTrue(isinstance(act, int))
            self.assertEqual(exp, act)

        def test_str_returns_int(self):
            value = "1"
            exp = 1
            act = check_type_int(value)
            self.assertTrue(isinstance(act, int))
            self.assertEqual(exp, act)

        def test_other_returns_err(self):
            value = "True"
            with self.assertRaises(TypeError) as err:
                check_type_int(value)
            self.assertE

# Generated at 2022-06-12 23:56:05.950529
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval("{{ test }}") == "{{ test }}"
    # do not allow method calls to modules
    assert safe_eval("platform.system()") == "platform.system()"
    # do not allow imports
    assert safe_eval("import os") == "import os"



# Generated at 2022-06-12 23:56:14.789152
# Unit test for function check_required_together
def test_check_required_together():
    from collections import deque
    
    term1 = ['host','username','password','vendor']
    term2 = ['key_file','username']
    terms = deque([term1,term2])
    
    parameters = {
        'host': '10.1.1.1',
        'username': 'test',
        'password': 'test',
        'vendor': 'arista'
    }
    
    check_required_together(terms, parameters)
    
    parameter2 = {
        'key_file': 'test.key',
        'username': 'test'
    }
    
    check_required_together(terms, parameter2)
    

# Generated at 2022-06-12 23:56:24.497545
# Unit test for function check_required_one_of
def test_check_required_one_of():
    try:
        assert check_required_one_of(None, {}) is None
    except TypeError:
        assert False
    try:
        assert check_required_one_of([['a']], {}) is not None
    except TypeError:
        assert True
    try:
        assert check_required_one_of([['a']], {'a': 'a'}) is None
    except TypeError:
        assert False
    try:
        assert check_required_one_of([['a'],['b']], {'a': 'a'}) is None
    except TypeError:
        assert False
    try:
        assert check_required_one_of([['a', 'b']], {'a': 'a'}) is None
    except TypeError:
        assert False

# Generated at 2022-06-12 23:56:34.583152
# Unit test for function check_required_if
def test_check_required_if():
    from ansible.module_utils.basic import AnsibleModule
    argument_spec = {
        "name": {"required": True, "type": "str"},
        "state": {"required": True, "type": "str",
                  "choices": ['present', 'absent']},
        "someint": {"required": False, "type": "int"},
        "bool_param": {"required": False, "type": "bool", "default": False},
        "string_param": {"required": False, "type": "str"}
    }
    required_if = [
            ['state', 'present', ('path',), True],
            ['someint', 99, ('bool_param', 'string_param')],
        ]
    parameters = {'name': 'Fake', 'state': 'present', 'someint': 99}


# Generated at 2022-06-12 23:56:39.571045
# Unit test for function check_type_float
def test_check_type_float():
    assert isinstance(check_type_float(1.0), float)
    assert isinstance(check_type_float(1), float)
    assert isinstance(check_type_float('1.0'), float)
    assert isinstance(check_type_float(b'1.0'), float)
    assert isinstance(check_type_float('a'), float) == False
    


# Generated at 2022-06-12 23:56:44.661391
# Unit test for function check_type_bits
def test_check_type_bits():
    """ Test function check_type_bits """
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1024Kb') == 1048576
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1024Mb') == 1073741824
    assert check_type_bits('1Tb') == 1099511627776
    assert check_type_bits('1024Gb') == 1099511627776
    # As an integer
    assert check_type_bits(1024) == 1024


# Generated at 2022-06-12 23:56:55.413236
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('10B') == 10
    assert check_type_bytes('10') == 10
    assert check_type_bytes('10kB') == 10*1024
    assert check_type_bytes('10MB') == 10*1024*1024
    assert check_type_bytes('10GB') == 10*1024*1024*1024
    assert check_type_bytes('10TB') == 10*1024*1024*1024*1024
    assert check_type_bytes('10PB') == 10*1024*1024*1024*1024*1024
    assert check_type_bytes('10EB') == 10*1024*1024*1024*1024*1024*1024
    assert check_type_bytes('10ZB') == 10*1024*1024*1024*1024*1024*1024*1024

# Generated at 2022-06-12 23:56:59.891964
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.0) == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float('1') == 1.0
    assert check_type_float('1.0') == 1.0
    try:
        check_type_float('one') == 1.0
    except TypeError:
        pass



# Generated at 2022-06-12 23:57:11.011688
# Unit test for function check_required_if
def test_check_required_if():
    with pytest.raises(TypeError) as exc:
        check_required_if([], {})
    assert "missing required arguments: bool_param, string_param" in to_native(exc.value)
    with pytest.raises(TypeError) as exc:
        check_required_if([], {'someint': 99})
    assert "missing required arguments: bool_param, string_param" in to_native(exc.value)
    assert check_required_if([], {'bool_param': False}) == []
    assert check_required_if([], {'bool_param': False, 'someint': 99}) == []
    assert check_required_if([], {'bool_param': False, 'string_param': 'a string'}) == []

# Generated at 2022-06-12 23:57:18.763198
# Unit test for function check_required_together
def test_check_required_together():
    test_parameters = {"value1": "1", "value3": "3"}
    test_terms = [("value1", "value2", "value3"), ("value4", "value5", "value6")]
    returned_value = check_required_together(test_terms, test_parameters)
    assert returned_value == [('value4', 'value5', 'value6')]



# Generated at 2022-06-12 23:57:25.559848
# Unit test for function check_type_bits
def test_check_type_bits():
    result = check_type_bits('1Mb')
    assert result == 1048576, "check_type_bits(1Mb) returns %s" % result
    result = check_type_bits('2.5Gb')
    assert result == 268435456, "check_type_bits(2.5Gb) returns %s" % result
    result = check_type_bits('100000000')
    assert result == 8000000, "check_type_bits(100000000) returns %s" % result
    result = check_type_bits('1000')
    assert result == 8, "check_type_bits(1000) returns %s" % result
    result = check_type_bits('1000b')
    assert result == 1000, "check_type_bits(1000b) returns %s" % result

# Generated at 2022-06-12 23:57:32.488619
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[{'a': 1}]") == [{'a': 1}]
    assert safe_eval("{'a': 1}") == {'a': 1}
    assert safe_eval("'a'") == 'a'
    assert safe_eval("1") == 1
    assert safe_eval("True") is True


# Generated at 2022-06-12 23:57:38.532174
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1') == 1
    assert check_type_bytes('1b') == 1
    assert check_type_bytes('1kb') == 1024
    assert check_type_bytes('1mb') == 1024 * 1024
    assert check_type_bytes('1g') == 1024 * 1024 * 1024
    assert check_type_bytes('1t') == 1024 * 1024 * 1024 * 1024

    with pytest.raises(TypeError):
        check_type_bytes('1p')


# Generated at 2022-06-12 23:57:46.884247
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 1') == 2
    assert safe_eval('(1, 2)') == (1, 2)
    assert safe_eval('1 + 1', include_exceptions=True) == (2, None)
    assert safe_eval('a', include_exceptions=True) == ('a', None)
    assert safe_eval('(1, 2)', include_exceptions=True) == ((1, 2), None)
    assert safe_eval('foo()', include_exceptions=True) == ('foo()', None)
    assert safe_eval('import foo', include_exceptions=True) == ('import foo', None)



# Generated at 2022-06-12 23:57:55.005542
# Unit test for function check_type_dict

# Generated at 2022-06-12 23:58:07.757841
# Unit test for function check_type_float
def test_check_type_float():
    # Test 1
    float_value = 1.0
    result = check_type_float(float_value)
    assert float(result) == float_value

    # Test 2
    int_value = 1
    result = check_type_float(int_value)
    assert float(result) == int_value

    # Test 3
    str_value = '1'
    result = check_type_float(str_value)
    assert float(result) == float_value

    # Test 3
    str_value = b'1'
    result = check_type_float(str_value)
    assert float(result) == float_value

    # Test 4
    str_value = 'test'

# Generated at 2022-06-12 23:58:10.388552
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {'required': {'required': True}, 'not_required': {'required': False}}
    parameters = {'not_required': None}
    assert check_required_arguments(argument_spec, parameters) == ['required']



# Generated at 2022-06-12 23:58:20.663200
# Unit test for function check_required_one_of
def test_check_required_one_of():
    params = {'state': 'present','name': 'a'}
    required_term = [['name','state']]
    result = check_required_one_of(required_term, params)
    assert(result == [])
    params = {'state': 'present'}
    required_term = [['name','state']]
    result = check_required_one_of(required_term, params)
    assert(result == [['name','state']])
    params = {'state': 'present','name': 'a'}
    required_term = [['name','src']]
    result = check_required_one_of(required_term, params)
    assert(result == [])
    params = {'state': 'present','name': 'a','src':'b'}

# Generated at 2022-06-12 23:58:27.583720
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('foo=bar') == {'foo': 'bar'}
    assert check_type_dict('foo=bar,wiz=bang') == {'foo': 'bar', 'wiz': 'bang'}
    assert check_type_dict('{"foo": "bar"}') == {'foo': 'bar'}
    assert check_type_dict('{"foo": "bar", "wiz": "bang"}') == {'foo': 'bar', 'wiz': 'bang'}
    assert check_type_dict('{"foo": "bar", "wiz": "bang", "zap": null}') == {'foo': 'bar', 'wiz': 'bang', 'zap': None}

# Generated at 2022-06-12 23:58:34.823481
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    try:
        check_type_bits('1mm')
        assert False, "Should raise TypeError"
    except TypeError as e:
        assert str(e) == "<class 'int'> cannot be converted to a Bit value"



# Generated at 2022-06-12 23:58:40.444039
# Unit test for function check_type_bytes
def test_check_type_bytes():
    cases = [
        ('1', 1),
        ('1B', 1),
        ('1KB', 1024),
        ('5k', 5*1024),
        ('5MB', 5*1024*1024),
        ('5G', 5*1024*1024*1024),
        ('5TB', 5*1024*1024*1024*1024),
        ('5P', 5*1024*1024*1024*1024*1024),
    ]

    for val, expected in cases:
        result = check_type_bytes(val)
        assert result == expected

