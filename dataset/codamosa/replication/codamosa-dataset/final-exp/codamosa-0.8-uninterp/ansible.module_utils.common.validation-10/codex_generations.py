

# Generated at 2022-06-12 23:49:27.860486
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1M') == 1024**2
    assert check_type_bytes('1G') == 1024**3
    assert check_type_bytes('1T') == 1024**4
    assert check_type_bytes('1P') == 1024**5
    assert check_type_bytes('1E') == 1024**6
    assert check_type_bytes('1Z') == 1024**7
    assert check_type_bytes('1Y') == 1024**8
    assert check_type_bytes('100') == 100
    assert check_type_bytes('1Ki') == 1<<10
    assert check_type_bytes('1Mi') == 1<<20
    assert check_type_bytes('1Gi') == 1<<30
    assert check_type_bytes('1Ti')

# Generated at 2022-06-12 23:49:35.426011
# Unit test for function check_required_if
def test_check_required_if():
    result = check_required_if(requirements=None, parameters={})
    assert result == []

    with pytest.raises(TypeError) as exc:
        check_required_if(
        requirements=[['state', 'present', ('path',), True]],
        parameters={'state':'present'})
    result = exc.value.results
    assert result[0]['missing'] == ['path']

    with pytest.raises(TypeError) as exc:
        check_required_if(
        requirements=[['state', 'present', ('path',), True]],
        parameters={'state':'absent'})
    result = exc.value.results
    assert result[0]['missing'] != ['path']


# Generated at 2022-06-12 23:49:44.521202
# Unit test for function check_required_if

# Generated at 2022-06-12 23:49:49.787394
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('{"a" : 0}') == {"a": 0}
    assert check_type_dict('{}') == {}
    assert check_type_dict('a=1,b=2') == {'a': '1', 'b': '2'}
    assert check_type_dict('a=1, b=2') == {'a': '1', 'b': '2'}
    assert check_type_dict('a=1,b=2, c=3') == {'a': '1', 'b': '2', 'c': '3'}
    assert check_type_dict('a=1,b=2,c=3, d=4') == {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
    assert check_type

# Generated at 2022-06-12 23:49:52.693816
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
        assert check_mutually_exclusive([['a', 'b'], ['c', 'd']], {'a': 'value1', 'b': 'value2', 'c': 'value3'})


# Generated at 2022-06-12 23:50:00.321655
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    try:
        check_mutually_exclusive([['a', 'b'], ['c', 'd']], dict(a=1, b=2, c=3))
    except TypeError as e:
        assert "mutually exclusive" in str(e)
    try:
        check_mutually_exclusive([['a', 'b'], ['c', 'd']], dict(a=1, c=2, d=3))
    except TypeError as e:
        assert "mutually exclusive" in str(e)
    assert check_mutually_exclusive([['a', 'b'], ['c', 'd']], dict(a=1, e=2)) == []
    assert check_mutually_exclusive([['a', 'b'], ['c', 'd']], dict(a=1)) == []



# Generated at 2022-06-12 23:50:07.998531
# Unit test for function check_required_if
def test_check_required_if():
    argument_spec = dict(
        state=dict(required=True, choices=['present', 'absent'], type='str'),
        path=dict(required=True, type='path'),
        someint=dict(required=False, type='int'),
        bool_param=dict(required=False, type='bool'),
        string_param=dict(required=False, type='str')
    )
    requirements_oneof = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')]
    ]
    requirements_all = [
        ['state', 'present', ('path',)],
        ['someint', 99, ('bool_param', 'string_param')]
    ]

# Generated at 2022-06-12 23:50:18.629081
# Unit test for function check_required_arguments
def test_check_required_arguments():
    required_argument_spec = {
        "param1": {"required": True, "type": "str"},
        "param2": {"required": False, "type": "str"},
    }
    argument_spec = {
        "param1": {"required": True, "type": "str"},
        "param2": {"required": False, "type": "str"},
        "param3": {"required": False, "type": "str"},
    }

    result = check_required_arguments(required_argument_spec, {})
    assert result == ['param1']

    result = check_required_arguments(required_argument_spec, {"param1": ""})
    assert not result

    result = check_required_arguments(required_argument_spec, {"param2": ""})
    assert result == ['param1']

    result = check

# Generated at 2022-06-12 23:50:28.245229
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert [] == check_mutually_exclusive(['A', 'B', 'C'], {'A': True})
    assert [] == check_mutually_exclusive(['A', 'B', 'C'], {'A': True, 'C': False})
    assert [] == check_mutually_exclusive(['A', 'B', 'C'], {'A': True, 'B': False})
    assert [] == check_mutually_exclusive(['A', 'B', 'C'], {'A': True, 'D': False})
    assert [] == check_mutually_exclusive(['A', 'B', 'C'], {'A': True, 'D': False, 'E': False, 'F': False, 'G': False})

# Generated at 2022-06-12 23:50:39.883386
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Unit test for function check_mutually_exclusive"""
    parameters = {'one': 1, 'two': 2, 'three': 3}
    try:
        check_mutually_exclusive(['one', 'two'], parameters)
    except TypeError:
        raise Exception("check_mutually_exclusive raised TypeError when it shouldn't have.")

    try:
        check_mutually_exclusive([['one', 'two']], parameters)
    except TypeError:
        raise Exception("check_mutually_exclusive raised TypeError when it shouldn't have.")

    try:
        check_mutually_exclusive(['one', 'three'], parameters)
    except TypeError:
        raise Exception("check_mutually_exclusive raised TypeError when it shouldn't have.")


# Generated at 2022-06-12 23:50:56.842915
# Unit test for function safe_eval
def test_safe_eval():
    literal_eval_tests = [
        ("True", True),
        ("'foobar'", "foobar"),
        ("['foo', 'bar', 'baz']", ["foo", "bar", "baz"]),
        ("{'foo': 'bar'}", {"foo": "bar"}),
        ("1+1", 1+1),
        ("1.2+1.3", 1.2+1.3),
        #('import foo', SyntaxError),
        #('foo.bar()', SyntaxError),
        ("foo", "foo"),
    ]


# Generated at 2022-06-12 23:50:58.345370
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    parameters = {'a': 'A', 'b': 'B'}
    required_params = ['a', 'b', 'c']
    assert check_missing_parameters(parameters, required_params) == ['c']



# Generated at 2022-06-12 23:51:09.310029
# Unit test for function check_required_by
def test_check_required_by():
    requirements = {"state": "present",
                    "name": ["present", "absent"]
                   }
    parameters = {"state": "present"}
    result = check_required_by(requirements, parameters)
    assert result == {}

    requirements = {"state": "present",
                    "name": ["present", "absent"]
                   }
    parameters = {"name": "present"}
    result = check_required_by(requirements, parameters)
    assert result == {}

    requirements = {"state": "present",
                    "name": ["present", "absent"]
                   }
    parameters = {"state": "absent"}

# Generated at 2022-06-12 23:51:19.958310
# Unit test for function check_required_by
def test_check_required_by():
    params = {
        'deployment': 'sql',
        'name': 'my-app',
        'instance_type': 'db.m4.large',
        'user': 'admin',
        'password': 'super_secure',
    }
    reqs = {
        'deployment': ['name', 'instance_type', 'database_name'],
        'user': ['database_name', 'password'],
        'password': ['user', 'database_name']
    }
    # Test that everything is OK for the params defined above
    assert check_required_by(reqs, params) == {}
    # Test that we get an exception as soon as one of the optional values of
    # the requirements is not present
    params['deployment'] = None
    with pytest.raises(TypeError):
        check_required

# Generated at 2022-06-12 23:51:26.609119
# Unit test for function safe_eval
def test_safe_eval():
    test_string = "{{ bad_template_expression }}"
    assert test_string == safe_eval(test_string)

    test_string = "{{ bad_template_expression.bad_attribute }}"
    assert test_string == safe_eval(test_string)

    test_string = "{{ bad_template_expression.bad_method() }}"
    assert test_string == safe_eval(test_string)

    test_string = "import test"
    assert test_string == safe_eval(test_string)

    test_string = "5"
    assert 5 == safe_eval(test_string)



# Generated at 2022-06-12 23:51:35.061082
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    args = [
        [
            'a',
            'b'
        ],
        [
            'c',
            'd'
        ]
    ]
    params = {
        'a': 1,
        'b': 2,
        'e': 3
    }
    try:
        check_mutually_exclusive(args, params)
    except TypeError:
        raise
    args = [
        [
            'a',
            'b'
        ],
        [
            'c',
            'd'
        ]
    ]
    params = {
        'a': 1,
        'b': 2,
        'e': 3
    }
    try:
        check_mutually_exclusive(args, params)
    except TypeError:
        raise
    # Test with an empty dictionary

# Generated at 2022-06-12 23:51:37.312108
# Unit test for function check_type_int
def test_check_type_int():
    with pytest.raises(TypeError):
        check_type_int('12.345')
        check_type_int('string')



# Generated at 2022-06-12 23:51:46.175211
# Unit test for function check_required_by
def test_check_required_by():
    requirements = {"name": ["type"], "type": ["size"], "size": ["size", "filesystem"]}
    parameters = {"name": "test", "size": 1024}
    result = check_required_by(requirements, parameters)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert "size" in result
    assert len(result["size"]) == 1
    assert "filesystem" in result["size"]

    parameters = {"name": "test", "type": "lvm", "size": 1024}
    result = check_required_by(requirements, parameters)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert "size" in result
    assert len(result["size"]) == 1
    assert "filesystem" in result["size"]


# Generated at 2022-06-12 23:51:50.249387
# Unit test for function check_type_float
def test_check_type_float():
    assert isinstance(check_type_float(3.14), float)
    assert isinstance(check_type_float(3), float)
    assert isinstance(check_type_float('3.14'), float)
    assert isinstance(check_type_float(b'3.14'), float)
    assert isinstance(check_type_float(u'3.14'), float)
    with pytest.raises(TypeError):
        check_type_float(b'\xc3.14')


# Generated at 2022-06-12 23:51:59.049038
# Unit test for function check_required_by
def test_check_required_by():
    # With one key in requirements
    test_params = {'foo': 'bar'}
    test_req = {'foo': 'fooreq'}
    assert check_required_by(test_req, test_params) == {}

    test_params = {'foo': 'bar'}
    test_req = {'foo': ['fooreq1', 'fooreq2']}
    assert check_required_by(test_req, test_params) == {}

    test_req = {'foo': 'fooreq', 'bar': 'barreq'}
    test_params = {'foo': 'bar', 'bar': 'baz'}
    assert check_required_by(test_req, test_params) == {}


# Generated at 2022-06-12 23:52:15.197423
# Unit test for function check_type_dict
def test_check_type_dict():
    for value in [
        "a=b",
        "a=b, c=d",
        "a=b, c=d, foo=bar",
        "a=b, c=d, foo='bar,bar,bar'",
        "a=b, c=d, foo='bar,bar,bar', what=ever"
    ]:
        assert check_type_dict(value) == {'a': 'b', 'c': 'd', 'foo': 'bar,bar,bar', 'what': 'ever'}
        assert check_type_dict(value) == eval(value)

# Generated at 2022-06-12 23:52:22.964324
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments(None, {}) == []
    assert check_required_arguments(None, {"key": "value"}) == []

    argument_spec = {"required": {"required": True}}
    assert check_required_arguments(argument_spec, {}) == ["required"]
    assert check_required_arguments(argument_spec, {"required": "value"}) == []

    argument_spec = {"required": {"required": False}}
    assert check_required_arguments(argument_spec, {}) == []
    assert check_required_arguments(argument_spec, {"required": "value"}) == []



# Generated at 2022-06-12 23:52:27.205511
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('10') == 10
    assert check_type_bytes('10GB') == 10737418240
    assert check_type_bytes('10KiB') == 10240
    assert check_type_bytes('10 MiB') == 10485760
# end of unit test for function check_type_bytes



# Generated at 2022-06-12 23:52:33.837320
# Unit test for function check_type_dict
def test_check_type_dict():
    #Test for simple dict
    input_dict = dict(name="sam")
    assert check_type_dict(input_dict) == input_dict

    #Test for string which starts with '{'
    input_dict_str = "{'name':'sam'}"
    assert check_type_dict(input_dict_str) == input_dict

    #Test for dict with str as value
    input_dict = dict(name="sam")
    assert check_type_dict(input_dict) == input_dict

    #Test for dict with lst as value
    input_dict = dict(name=['sam', 'sam2'])
    assert check_type_dict(input_dict) == input_dict

    #Test for dict with dict as value
    input_dict = dict(name=dict(name="sam"))
    assert check_type

# Generated at 2022-06-12 23:52:44.229992
# Unit test for function safe_eval
def test_safe_eval():
    ''' test_safe_eval '''
    assert safe_eval(1) == 1
    assert safe_eval('-6') == -6
    assert safe_eval('1+6') == 7
    assert safe_eval('1.0+6') == 7.0
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar') == 'foo.bar'
    assert safe_eval({}) == {}
    assert safe_eval({'foo': 'bar'}) == {'foo': 'bar'}
    assert safe_eval(['foo', 'bar']) == ['foo', 'bar']
    try:
        safe_eval(None) == None
        assert False == True
    except BaseException as e:
        assert 'is not a string' in str(e)

# Generated at 2022-06-12 23:52:55.536583
# Unit test for function check_type_float
def test_check_type_float():
    if check_type_float(1) != 1.0:
        raise AssertionError()

    if check_type_float("1") != 1.0:
        raise AssertionError()

    if check_type_float("1.0") != 1.0:
        raise AssertionError()

    if check_type_float(1.0) != 1.0:
        raise AssertionError()

    try:
        check_type_float((1, "a"))
        raise AssertionError()
    except TypeError:
        pass

    try:
        check_type_float({'a': 1})
        raise AssertionError()
    except TypeError:
        pass

    try:
        check_type_float(None)
        raise AssertionError()
    except TypeError:
        pass



# Generated at 2022-06-12 23:53:01.074596
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('0') == 0
    assert check_type_bytes('1') == 1
    assert check_type_bytes('2') == 2
    assert check_type_bytes('3') == 3
    assert check_type_bytes('4') == 4
    assert check_type_bytes('5') == 5
    assert check_type_bytes('6') == 6
    assert check_type_bytes('7') == 7
    assert check_type_bytes('8') == 8
    assert check_type_bytes('9') == 9
    assert check_type_bytes('10') == 10
    assert check_type_bytes('20') == 20
    assert check_type_bytes('30') == 30
    assert check_type_bytes('40') == 40
    assert check_type_bytes('50') == 50
    assert check_

# Generated at 2022-06-12 23:53:05.936335
# Unit test for function check_type_dict
def test_check_type_dict():
    # Test for the simple cases
    test_dict = {'k1': 'v1', 'k2': 'v2'}
    test_list = ['k1=v1', 'k2=v2']
    test_json = '{"k1": "v1", "k2": "v2"}'
    test_string = 'k1=v1, k2=v2'
    test_tuple = (1, 2)
    test_int = 1
    test_float = 1.0
    test_bool = True

    assert dict == type(check_type_dict(test_dict))
    assert dict == type(check_type_dict(test_list))
    assert dict == type(check_type_dict(test_json))
    assert dict == type(check_type_dict(test_string))
   

# Generated at 2022-06-12 23:53:17.694318
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('123') == 123
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('1 < 2') is True
    assert safe_eval('None') is None
    assert safe_eval('1+2') == 3
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval("{'test':'ok'}") == {'test': 'ok'}
    assert safe_eval('3*3') == 9
    assert safe_eval('2**10') == 1024
    assert safe_eval('1.2/2') == 0.6
    assert safe_eval('1,2,3') == (1, 2, 3)

# Generated at 2022-06-12 23:53:25.631073
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Unit tests for check_mutually_exclusive"""

    # No arguments supplied, correct usage
    try:
        check_mutually_exclusive(None, {})
    except TypeError:
        assert False

    # Option supplied with no arguments
    try:
        check_mutually_exclusive([], {})
    except TypeError:
        assert False

    # Option supplied with no arguments, but context
    try:
        check_mutually_exclusive([], {}, options_context=['test'])
    except TypeError:
        assert False

    # Option supplied with arguments, but they don't exist in passed in data
    try:
        check_mutually_exclusive([['test1', 'test2']], {})
    except TypeError:
        assert False

    # Combination of good and bad passed in data

# Generated at 2022-06-12 23:53:32.657264
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('a=b, c=d') == {'a': 'b', 'c': 'd'}
    assert check_type_dict('{"a":"b", "c":"d"}') == {'a': 'b', 'c': 'd'}
    assert check_type_dict('{"a": "b", "c": "d"}') == {'a': 'b', 'c': 'd'}



# Generated at 2022-06-12 23:53:43.380243
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval(None) == None
    assert safe_eval(1) == 1
    assert safe_eval("mystring") == "mystring"
    assert safe_eval("{'a':'b','c':'d'}") == {'a':'b','c':'d'}
    assert safe_eval("['a','b','c']") == ['a','b','c']
    assert safe_eval("1 + 1") == 2
    assert safe_eval("'a'+'b'") == 'ab'
    assert safe_eval("{'a':1 + 1}") == {'a':2}
    assert safe_eval("{'a':'x'+'y'}") == {'a':'xy'}

# Generated at 2022-06-12 23:53:46.543948
# Unit test for function check_required_together
def test_check_required_together():
    assert check_required_together([['a', 'b']],{'a': "test", 'b': "test"}) is None
    assert check_required_together([['a', 'b']],{'a': "test", 'c': "test"}) is not None


# Generated at 2022-06-12 23:53:57.568735
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert [] == check_required_arguments({'foo': {}, 'bar': {}, 'baz': {}},
                                          {'foo': 1, 'bar': 2, 'baz': 3})
    assert ['bar', 'baz'] == check_required_arguments({'foo': {}, 'bar': {'required': True}, 'baz': {'required': True}},
                                                       {})
    assert ['bar', 'baz'] == check_required_arguments({'foo': {}, 'bar': {'required': True}, 'baz': {'required': True}},
                                                       {'foo': 1})

# Generated at 2022-06-12 23:54:07.620626
# Unit test for function check_required_if
def test_check_required_if():
    with pytest.raises(TypeError) as excinfo:
        check_required_if([['state', 'present', ('path',), False]], {'state': 'present'})
    assert 'is present but all of the following are missing: path' in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        check_required_if([['state', 'present', ('path',), True]], {'state': 'present'})
    assert 'is present but any of the following are missing: path' in str(excinfo.value)

    assert len(check_required_if([['state', 'present', ('path',), False]], {'state': 'present', 'path': 'something'})) == 0

# Generated at 2022-06-12 23:54:10.085881
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    with pytest.raises(TypeError):
        check_type_bits('1Mkb')

# Generated at 2022-06-12 23:54:21.428835
# Unit test for function check_type_float
def test_check_type_float():
    # Returns a float if a string with a number in it is given
    assert check_type_float('2.2') == 2.2
    # Returns the same float if a float is given
    assert check_type_float(2.2) == 2.2
    # Returns the correct float if an int is given
    assert check_type_float(2) == 2.0
    # Raises an exception if an invalid string is given
    with pytest.raises(TypeError):
        check_type_float('one')
    # Raises an exception if a non-number string is given
    with pytest.raises(TypeError):
        check_type_float('')
    # Raises an exception if a list is given
    with pytest.raises(TypeError):
        check_type_float([])
    # Raises an

# Generated at 2022-06-12 23:54:27.328534
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1b') == 1
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1mb') == 1048576
    assert check_type_bits('1gb') == 1073741824
    assert check_type_bits('1tb') == 1099511627776


# -------------------------------------------------------------------------------------------------
# Public functions
# -------------------------------------------------------------------------------------------------


# Generated at 2022-06-12 23:54:35.035691
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float("1.1") == 1.1
    assert check_type_float("1") == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float(1.1) == 1.1
    assert check_type_float(b"1.1") == 1.1
    assert check_type_float(b"1") == 1.0

    with raises(TypeError):
        check_type_float(None)


# FIXME: This is a stub function for now. Needs to be implemented

# Generated at 2022-06-12 23:54:45.969230
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    result = [
        ["a", "b"]
    ]
    param = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    assert check_mutually_exclusive(result, param) == []

    result = [
        ["a", "b"]
    ]
    param = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    assert check_mutually_exclusive(result, param) == []

    result = [
        ["a", "b"],
        ["a", "c"]
    ]
    param = {
        "a": 1
    }
    assert check_mutually_exclusive(result, param) == []


# Generated at 2022-06-12 23:54:51.700061
# Unit test for function check_type_int
def test_check_type_int():
    check_type_int('3') == 3

# Generated at 2022-06-12 23:55:03.517779
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1+1") == 2
    assert safe_eval("value") == "value"
    assert safe_eval("[]") == []
    assert safe_eval("{}") == {}
    assert safe_eval("{'a': 'b'}") == {"a": "b"}
    assert safe_eval("a") == "a"
    assert safe_eval("a.b") == "a.b"
    assert safe_eval("a.b()") == "a.b()"
    assert safe_eval("import ash") == "import ash"
    assert safe_eval("[i for i in range(3)]") == [0, 1, 2]
    assert safe_eval("{i:i for i in range(3)}") == {0: 0, 1: 1, 2: 2}
    assert safe_eval

# Generated at 2022-06-12 23:55:11.730351
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():

    # Test terms is None
    try:
        check_mutually_exclusive(None, dict())
    except TypeError:
        assert False, "Check failed when it should have passed"

    # Test successful cases with a single check
    try:
        check_mutually_exclusive(["x"], dict(x=3))
    except TypeError:
        assert False, "Check failed when it should have passed"
    try:
        check_mutually_exclusive(("x",), dict(x=3))
    except TypeError:
        assert False, "Check failed when it should have passed"
    try:
        check_mutually_exclusive("x", dict(x=3))
    except TypeError:
        assert False, "Check failed when it should have passed"

# Generated at 2022-06-12 23:55:23.197137
# Unit test for function check_type_dict
def test_check_type_dict():
    assert {'a': 'b', 'c': 'd'} == check_type_dict('a=b, c=d')
    assert {'a': 'b', 'c': 'd'} == check_type_dict('a=b,c=d')
    assert {'a': 'b', 'c': 'd'} == check_type_dict('a="b",c=d')
    assert {'a': 'b', 'c': 'd'} == check_type_dict('a="b", c="d"')
    assert {'a': 'b', 'c': 'd'} == check_type_dict('a=\'b\', c=\'d\'')
    assert {'a': 'b', 'c': 'd'} == check_type_dict('a="b",c="d"')


# Generated at 2022-06-12 23:55:28.107505
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int('1') == 1
    try:
        check_type_int('a')
    except TypeError:
        pass
    else:
        assert False, "Should have failed check_type_int('a')"


# Generated at 2022-06-12 23:55:34.443211
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(5.5) == 5.5
    assert check_type_float(5) == 5.0
    assert check_type_float("5") == 5.0
    assert check_type_float(u"5") == 5.0
    with pytest.raises(TypeError):
        check_type_float([])
    with pytest.raises(TypeError):
        check_type_float(None)


# Generated at 2022-06-12 23:55:35.693558
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int('1') == 1



# Generated at 2022-06-12 23:55:39.105931
# Unit test for function check_type_float
def test_check_type_float():
    with pytest.raises(TypeError):
        check_type_float(None)
    assert 0.0 == check_type_float(0.0)
    assert 1.0 == check_type_float(1)
    assert 1000.123 == check_type_float('1000.123')


# Generated at 2022-06-12 23:55:48.607359
# Unit test for function check_type_bytes

# Generated at 2022-06-12 23:55:53.447911
# Unit test for function check_type_bytes
def test_check_type_bytes():
    data = [
        ('512MB', 536870912),
        ('1GB', 1073741824),
        ('1.5MB', 1572864),
        ('1MiB', 1048576),
    ]

    for datum in data:
        assert check_type_bytes(datum[0]) == datum[1]



# Generated at 2022-06-12 23:56:08.521466
# Unit test for function check_required_together
def test_check_required_together():
    terms = [("host", "user", "password"), ("host", "user", "ssh_key")]
    parameters = {"host": "test"}
    try:
        options_context = None
        check_required_together(terms, parameters, options_context)
        raise TypeError("parameters are required together: host, user, password")
    except TypeError as e:
        assert str(e) == "parameters are required together: host, user, password"
    parameters = {"host": "test", "user": "test", "password": "test"}
    try:
        options_context = None
        check_required_together(terms, parameters, options_context)
        return None
    except TypeError as e:
        raise TypeError("check_required_together failed")


# Generated at 2022-06-12 23:56:09.181676
# Unit test for function check_type_int
def test_check_type_int():
    pass


# Generated at 2022-06-12 23:56:16.615703
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{1:2}') == {1:2}
    assert safe_eval('{1:2}', include_exceptions=True) == ({1:2}, None)
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo', include_exceptions=True) == ('foo', None)
    assert safe_eval('foo()') == 'foo()'
    assert safe_eval('foo()', include_exceptions=True) == ('foo()', None)
    assert safe_eval('import foo') == 'import foo'
    assert safe_eval('import foo', include_exceptions=True) == ('import foo', None)
    assert safe_eval('bar.foo()') == 'bar.foo()'

# Generated at 2022-06-12 23:56:29.668814
# Unit test for function safe_eval
def test_safe_eval():
    # Test for common dictionary
    assert safe_eval('{"a": "b"}') == {"a": "b"}
    # Test for common string
    assert safe_eval('"the men"') == "the men"
    # Test for common boolean
    assert safe_eval('True') is True
    # Test for common integer
    assert safe_eval('45') == 45
    # Test for common lists
    assert safe_eval('[1,2,3]') == [1,2,3]
    # Test that it doesn't evaluate
    # strings containing "import"
    assert safe_eval('import foo') == 'import foo'
    # Test that it doesn't evaluate
    # strings containing "method()"
    assert safe_eval('dict.iteritems()') == 'dict.iteritems()'
    # Test that it doesn't evaluate
   

# Generated at 2022-06-12 23:56:39.858716
# Unit test for function check_required_together
def test_check_required_together():
    #pylint: disable=redefined-outer-name
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.module_utils.common.text.formatters import human_to_bytes

    def test_options(terms, parameters, expected_results):
        options_context = None
        results = check_required_together(terms, parameters, options_context)
        assert results == expected_results

    #pylint: disable=medium-lambda
    expected_fails = lambda x: dict(failed=x)
    expected_passes = lambda x: dict(passed=x)


    # Test simple case where parameters are required together
    # This is an array of arrays
    terms = [
        ['required_together', 'required_together_one'],
    ]

# Generated at 2022-06-12 23:56:44.789425
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('10Mb') == 10485760
    assert check_type_bits('10M') == 8000000
    assert check_type_bits('0.5M') == 512000
    assert check_type_bits('0.5MB') == 512000
    assert check_type_bits('0.3k') == 300



# Generated at 2022-06-12 23:56:55.501453
# Unit test for function safe_eval
def test_safe_eval():
    from hypothesis import given
    from hypothesis.strategies import text
    from hypothesis.strategies import integers

    # Test a variety of inputs, including possible exceptions, and ensure
    # the result is what we expect
    @given(text(min_size=0))
    def test_safe_eval_string_input(s):
        result, _ = safe_eval(s, include_exceptions=True)
        assert isinstance(result, string_types)
        assert result == s

    # Test a variety of inputs, including possible exceptions, and ensure
    # the result is what we expect
    @given(integers(min_value=-2**63, max_value=2**63-1))
    def test_safe_eval_int_input(i):
        result, _ = safe_eval(i, include_exceptions=True)


# Generated at 2022-06-12 23:57:01.973725
# Unit test for function check_required_arguments
def test_check_required_arguments():
    from ansible.module_utils.common.parameters import Parameter
    argument_spec = dict(
        param1=dict(required=True, type='str', default='default'),
        param2=dict(required=False, type='list', default=[]),
        param3=Parameter(required=True),
        param4=dict(required=True),
        param5=dict(required=True),
    )
    parameters = {'param2': []}
    assert check_required_arguments(argument_spec, parameters) == ['param1', 'param3', 'param4', 'param5']



# Generated at 2022-06-12 23:57:13.153530
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 2') == 3
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo', include_exceptions=True)[0] == 'foo'
    assert safe_eval('foo', include_exceptions=True)[1] is None
    assert safe_eval('foo().bar') == 'foo().bar'
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('{"a": 1}') == {'a': 1}
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('import foo') == 'import foo'
    # issue #54293
    assert safe_eval('1.1 + 1') == 2.1

# Generated at 2022-06-12 23:57:19.319607
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = dict(
        host=dict(required=True),
        port=dict(required=True),
        username=dict(required=False),
        password=dict(required=False),
    )
    parameters = dict(host='hostname', port='22')

    result = check_required_arguments(argument_spec, parameters)
    assert result == []
    assert isinstance(result, list)

    result = check_required_arguments(argument_spec, dict(host='hostname'))
    assert result == ['port']
    assert isinstance(result, list)



# Generated at 2022-06-12 23:57:24.436298
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1M') == 8388608


# Generated at 2022-06-12 23:57:31.157717
# Unit test for function check_type_dict
def test_check_type_dict():
    # Check that input as a string is returned as a dict if it is a
    # valid JSON, a valid string of key value pairs or raises
    # TypeError if it is neither
    # Test for valid JSON string
    result = check_type_dict("{'foo':'bar'}")
    assert result == {'foo': 'bar'}
    # Test for valid string of key value pairs
    result = check_type_dict("foo=bar,bar=baz")
    assert result == {'foo': 'bar', 'bar': 'baz'}
    # Test for valid string of key value pairs, with quoted pairs
    result = check_type_dict("foo='bar,baz',bar=baz")
    assert result == {'foo': 'bar,baz', 'bar': 'baz'}
    # Test for valid string of

# Generated at 2022-06-12 23:57:40.480656
# Unit test for function check_required_arguments
def test_check_required_arguments():
    arguments = {'required_1': {'required': True},
                 'required_2': {'required': True},
                 'not_required_1': {'required': False},
                 'not_required_2': {'required': False}}
    parameters = {}
    assert check_required_arguments(arguments, parameters) == ['required_1', 'required_2']
    parameters = {'required_1': 'good', 'required_2': 'good'}
    assert check_required_arguments(arguments, parameters) == []
    parameters = {'required_1': 'good', 'required_2': 'good', 'not_required_1': 'good', 'not_required_2': 'good'}
    assert check_required_arguments(arguments, parameters) == []



# Generated at 2022-06-12 23:57:50.814822
# Unit test for function check_type_bytes
def test_check_type_bytes():
    cases = [
        # Input, expected output,
        (b'123', b'123'),
        ('123', b'123'),
        ('123B', 123),
        ('123KB', 123 * 1024),
        ('123MB', 123 * 1024 * 1024),
        ('123GB', 123 * 1024 * 1024 * 1024),
        ('123TB', 123 * 1024 * 1024 * 1024 * 1024),
        ('123PB', 123 * 1024 * 1024 * 1024 * 1024 * 1024),
        ('123EB', 123 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024),
        ('123ZB', 123 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024),
        ('123YB', 123 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024),
    ]

# Generated at 2022-06-12 23:57:52.003673
# Unit test for function check_type_float
def test_check_type_float():
    pass



# Generated at 2022-06-12 23:58:05.042088
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # Test1. Multiple parameters
    parameters = {
        'test_param1': 'test_value1',
        'test_param2': 'test_value2',
        'test_param3': 'test_value3',
        'test_param4': 'test_value4',
    }
    terms = [
        ["test_param1", "test_param2", "test_param3"],
        "test_param4"
    ]
    result = check_mutually_exclusive(terms, parameters)
    assert result == []

    # Test2. Multiple parameters with repeated parameter
    parameters = {
        'test_param1': 'test_value1',
        'test_param2': 'test_value2',
        'test_param3': 'test_value3',
    }

# Generated at 2022-06-12 23:58:13.944181
# Unit test for function check_required_if
def test_check_required_if():
    parameters = dict(
        p1=1, p2="", p3=False, p4=None,
        p5=[], p6=(), p7={}, p8=set()
    )
    # Test with single requirements
    reqs = [
        ['p1', 1, ['param']],
        ['p2', "", ['param']],
        ['p3', True, ['param']],
        ['p3', False, ['param']],
        ['p4', None, ['param']],
        ['p5', [], ['param']],
        ['p6', (), ['param']],
        ['p7', {}, ['param']],
        ['p8', set(), ['param']],
    ]
    for req in reqs:
        msg = check_required_if(req, parameters)

# Generated at 2022-06-12 23:58:23.871465
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    test_list = [[1, 2, 3], [3, 4, 5]]
    test_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    assert not check_mutually_exclusive(test_list, test_dict, [])
    test_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
    assert not check_mutually_exclusive(test_list, test_dict, [])
    test_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
    assert check_mutually_exclusive(test_list, test_dict, [])

# Generated at 2022-06-12 23:58:31.616942
# Unit test for function check_required_one_of
def test_check_required_one_of():
    terms = (
        (['a', 'b'], {'a': 'aa', 'b': 'bb'}),
        (['a', 'b'], {'a': 'aa', 'b': 'bb', 'c': 'cc'}),
    )
    for (item, parameters) in terms:
        check_required_one_of(item, parameters)
        try:
            check_required_one_of(item, {'c': 'cc'})
        except TypeError as te:
            pass


# Generated at 2022-06-12 23:58:38.695332
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [['a', '', ['b'], True], ['c', '', ['d', 'e'], True]]
    parameters = {}
    options_context = []
    result = check_required_if(requirements, parameters, options_context)
    assert result == []
    parameters = {'a': 'a'}
    with pytest.raises(TypeError) as excinfo:
        result = check_required_if(requirements, parameters, options_context)
    assert "b" in str(excinfo.value)
    parameters['b'] = 'b'
    result = check_required_if(requirements, parameters, options_context)
    assert result == []
    parameters = {'c': 'c'}
    with pytest.raises(TypeError) as excinfo:
        result = check_required_if