

# Generated at 2022-06-12 23:49:30.870771
# Unit test for function check_required_by
def test_check_required_by():
    test_module = {
        'test_param': 'test_value'
    }

    test_spec = {
        'test_param': {
            'required_by': 'required_with_this'
        },
        'required_with_this': {
            'type': 'bool'
        }
    }

    assert check_required_by(requirements=test_spec['test_param'].get('required_by'),
                             parameters=test_module,
                             options_context=['test_param'],
                             ) is None

    test_module = {
        'test_param': 'test_value',
        'required_with_this': True,
    }


# Generated at 2022-06-12 23:49:37.588206
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int("1") == 1
    assert check_type_int("2.5") == 2
    # ansible/ansible-modules-core#4998
    assert check_type_int("0x0A") == 10
    # ansible/ansible-modules-core#4998
    assert check_type_int("0o77") == 63
    # ansible/ansible-modules-core#4998
    assert check_type_int("0b1110") == 14
    # ansible/ansible-modules-core#4998
    assert check_type_int("0777") == 511

    with pytest.raises(TypeError):
        check_type_int("2.5")
    with pytest.raises(TypeError):
        check_type_int("0x0z")


# Generated at 2022-06-12 23:49:43.474902
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    required_parameters=['server','password']
    parameters={'server':'192.168.1.1','password':'123456'}
    assert(check_missing_parameters(parameters,required_parameters)==[])

    parameters={'server':'192.168.1.1','password':None}
    assert(check_missing_parameters(parameters,required_parameters)==['password'])


# Generated at 2022-06-12 23:49:48.236936
# Unit test for function check_type_bytes
def test_check_type_bytes():
    check_type_bytes("1")
    check_type_bytes("1kb")
    check_type_bytes("1Ki")
    check_type_bytes("1Mi")
    check_type_bytes("1Gi")
    check_type_bytes("1Ti")
    check_type_bytes("1Pi")
    check_type_bytes("1Ei")
    check_type_bytes("1Zi")
    check_type_bytes("1Yi")
    check_type_bytes("1K")
    check_type_bytes("1M")
    check_type_bytes("1G")
    check_type_bytes("1T")
    check_type_bytes("1P")
    check_type_bytes("1E")
    check_type_bytes("1Z")

# Generated at 2022-06-12 23:49:55.267856
# Unit test for function check_required_by
def test_check_required_by():
    # Empty requirements and parameters
    assert check_required_by({}, {}) == {}
    # Empty parameters
    assert check_required_by({"a": ["b"]}, {}) == {}
    # Empty requirements
    assert check_required_by({}, {"a": "foo", "b": "bar"}) == {}
    # No missing parameters
    assert check_required_by({"a": ["b"]}, {"a": "foo", "b": "bar"}) == {}
    # One missing parameter
    assert check_required_by({"a": ["b"]}, {"a": "foo"}) == {'a': ['b']}



# Generated at 2022-06-12 23:50:05.341725
# Unit test for function check_required_by
def test_check_required_by():
    # Success case
    required_by_dict= {
        'foo': 'bar',
        'baz': ['qux', 'quux'],
        'quuz': ['quuz', 'qux', 'quux']
    }

    parameters = {
        'foo': True,
        'bar': True,
        'baz': True,
        'quux':True,
        'qux': True,
        'quuz': True
    }

    expected = {}
    actual = check_required_by(required_by_dict, parameters)
    assert expected == actual

    # Failure case - requried_by_dict has a key not defined in the parameters

# Generated at 2022-06-12 23:50:17.353812
# Unit test for function check_required_if
def test_check_required_if():
    # Case 1: missing=[], max_missing_count=0, is_one_of=False
    requirements = [['a', 'b', ['c', 'd']]]
    parameters = {'a': 'b', 'c': 'c', 'd': 'd'}
    assert check_required_if(requirements, parameters) == []
    # Case 2: missing=['c'], max_missing_count=0, is_one_of=False
    requirements = [['a', 'b', ['c', 'd']]]
    parameters = {'a': 'b', 'd': 'd'}

# Generated at 2022-06-12 23:50:23.065284
# Unit test for function check_required_together
def test_check_required_together():
    check_required_together([['a', 'b']], {'a': '1'})
    check_required_together([['a', 'b']], {'b': '1'})
    try:
        check_required_together([['a', 'b']], {})
    except TypeError as e:
        if "required together: 'a', 'b'" not in str(e):
            raise



# Generated at 2022-06-12 23:50:30.967070
# Unit test for function check_required_by
def test_check_required_by():
    requirements = {'param_a': ['param_b', 'param_c']}
    module_parameters = {'param_a': True, 'param_c': None}
    if not check_required_by(requirements, module_parameters):
        raise AssertionError('Expected to return empty dict')
    module_parameters = {'param_a': True}
    if not check_required_by(requirements, module_parameters):
        raise AssertionError('Expected to return empty dict')
    module_parameters = {'param_a': True, 'param_c': True}
    if check_required_by(requirements, module_parameters):
        raise AssertionError('Expected to raise a TypeError')



# Generated at 2022-06-12 23:50:41.479611
# Unit test for function check_required_by
def test_check_required_by():
    assert {} == check_required_by(None, {})
    assert {} == check_required_by({}, {})
    assert {} == check_required_by({'a': ['b']}, {'a': 'foo'})
    assert {} == check_required_by({'a': ['b']}, {'a': 'foo', 'b': 'bar'})
    assert {'a': ['b', 'c']} == check_required_by({'a': 'b'}, {'a': 'foo'})
    assert {'a': ['b', 'c']} == check_required_by({'a': 'b'}, {'a': 'foo', 'c': 'bar'})

# Generated at 2022-06-12 23:50:50.907366
# Unit test for function check_type_dict
def test_check_type_dict():
    my_dict = {'key1': 'val1', 'key2': 'val2'}
    string_dict = '{key1: val1, key2: val2}'
    string_dict2 = '{\'key1\': \'val1\', \'key2\': \'val2\'}'
    string_dict3 = '{\'key1\':\'val1\',\'key2\':\'val2\'}'
    string_dict4 = 'key1=val1, key2=val2'
    string_dict5 = '\'key1\'=\'val1\', \'key2\'=\'val2\''
    string_dict6 = 'key1=\'val1\',key2=\'val2\''
    string_dict7 = 'key1=\'val1\',key2="val2"'


# Generated at 2022-06-12 23:51:01.475026
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {'param1': {'required': True}, 'param2': {'required': True}}
    parameters = {'param1': 'a'}
    res = check_required_arguments(argument_spec, parameters)
    assert res == ['param2']

    argument_spec = {'param1': {'required': False}, 'param2': {'required': True}}
    parameters = {'param1': 'a'}
    res = check_required_arguments(argument_spec, parameters)
    assert res == ['param2']

    argument_spec = {'param1': {'required': False}, 'param2': {'required': True}}
    parameters = {'param1': 'a', 'param2': 'b'}
    res = check_required_arguments(argument_spec, parameters)
    assert res

# Generated at 2022-06-12 23:51:08.665324
# Unit test for function check_mutually_exclusive

# Generated at 2022-06-12 23:51:13.607150
# Unit test for function safe_eval
def test_safe_eval():
    # Check for int data types
    assert safe_eval('1 + 1') == 2
    assert safe_eval('-2') == -2
    # Check for boolean data types
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    # Check for dictionary data type
    assert safe_eval('dict(a=1, b=2)') == dict(a=1, b=2)
    assert safe_eval('{"a": 1, "b": 2}') == dict(a=1, b=2)
    assert safe_eval('{"a": 1, "b": 2}', include_exceptions=True) == (dict(a=1, b=2), None)
    # Check for list data type
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]

# Generated at 2022-06-12 23:51:23.490096
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("5") == 5
    assert safe_eval("'5'") == '5'
    assert safe_eval("[5]") == [5]
    assert safe_eval("dict(a='b')") == dict(a='b')
    assert safe_eval("['a', 'b']") == ['a', 'b']
    assert safe_eval("dict(a=['b', 'c'])") == dict(a=['b', 'c'])
    # Method call to module is rejected
    assert safe_eval("ansible.module_utils.six.text_type(a='b')") == "ansible.module_utils.six.text_type(a='b')"
    # Import statement is rejected
    assert safe_eval("import os") == "import os"



# Generated at 2022-06-12 23:51:32.383226
# Unit test for function check_required_if
def test_check_required_if():
    def test_function(requirements, parameters, expection_msg=None):
        try:
            check_required_if(requirements, parameters)
        except TypeError as err:
            assert expection_msg in to_native(err)
        else:
            if expection_msg:
                assert False
    test_function(
        [
            ["state", "present", ["path"]],
            ["state", "absent", ["other_path"]]
        ],
        {
            "state": "present"
        },
        "state is present but all of the following are missing: path"
    )

# Generated at 2022-06-12 23:51:42.225623
# Unit test for function check_required_by
def test_check_required_by():
    parameters = dict(
        a=1,
        b=2,
        c=3,
        d=4,
        e=5,
        f=6,
        g=None,
        h=None
    )
    requirements = dict(
        a=['f', 'g'],
        b=['h'],
        c=['i']
    )
    try:
        result = check_required_by(requirements, parameters)
    except TypeError as e:
        assert "TypeError: missing parameter(s) required by 'a': g, i\n" == "%s\n" % e
    else:
        raise AssertionError("Setting %s to %s should have failed" % (parameters, requirements))


# Generated at 2022-06-12 23:51:46.686621
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments({"x": {"required": True}}, {"x": 0}) == []
    assert check_required_arguments({"x": {"required": True}, "y": {"required": True}}, {"y": 0}) == ["x"]



# Generated at 2022-06-12 23:51:57.114368
# Unit test for function safe_eval
def test_safe_eval():

    # Safe evaluation should evaluate the content
    assert safe_eval("{'a':1}") == {'a':1}

    # Allowed operators
    assert safe_eval("2+2") == 4
    assert safe_eval("2*2") == 4
    assert safe_eval("4/4") == 1
    assert safe_eval("4//4") == 1
    assert safe_eval("4-4") == 0
    assert safe_eval("4**2") == 16
    assert safe_eval("2 == 2") is True
    assert safe_eval("1 != 2") is True
    assert safe_eval("'' in 'abc'") is True
    assert safe_eval("'a' not in 'abc'") is False
    assert safe_eval("2 < 3") is True
    assert safe_eval("2 > 3") is False


# Generated at 2022-06-12 23:52:03.121645
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments({'foo': {'required': True}}, {'foo': 'bar'}) == []
    try:
        check_required_arguments({'foo': {'required': True}}, {'bar': 'foo'})
    except TypeError as e:
        assert 'missing required arguments: foo' in to_native(e)



# Generated at 2022-06-12 23:52:14.206737
# Unit test for function check_required_one_of
def test_check_required_one_of():
    try:
        check_required_one_of(terms = [('host', 'hostvars', 'playbook_dir')], parameters= dict(host='localhost',hostvars='host:{localhost}'))

    except TypeError as e:
        assert e[0] == 'one of the following is required: host,hostvars,playbook_dir'


# Generated at 2022-06-12 23:52:19.515251
# Unit test for function check_required_together
def test_check_required_together():
    """
    Unit test for function check_required_together
    """
    params={'a':1}
    terms = [(['a'], ['b'])]
    results = check_required_together(terms, params)
    if len(results) != 0:
       raise AssertionError("check_required_together failed")



# Generated at 2022-06-12 23:52:27.299401
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{1: 2, 3: [1, 2, ["foo", "bar"], 4, 5]}') == {1: 2, 3: [1, 2, ["foo", "bar"], 4, 5]}
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('[1, 2, 3, 4, 5]') == [1, 2, 3, 4, 5]
    assert safe_eval('[1, 2, ["foo", "bar"], 4, 5]') == [1, 2, ["foo", "bar"], 4, 5]
    assert safe_eval('[[1, 2], [3, 4]]') == [[1, 2], [3, 4]]
    assert safe_eval('1') == 1
    assert safe_eval('1.0') == 1.0


# Generated at 2022-06-12 23:52:33.897124
# Unit test for function check_type_dict
def test_check_type_dict():
    eq_('test1', check_type_dict('test1')['test1'])
    eq_(1, check_type_dict('test1=1')['test1'])
    eq_(['test1'], check_type_dict('test1=1,test2=2')['test1'])
    eq_(['test2'], check_type_dict('test1=1,test2=2')['test2'])
    eq_(['test1,test2'], check_type_dict('test1,test2=test3,test4')['test1,test2'])
    eq_(['test3'], check_type_dict('test1,test2=test3,test4')['test3'])

# Generated at 2022-06-12 23:52:44.306997
# Unit test for function check_required_by
def test_check_required_by():
    """Trivial test cases form docstring"""
    assert check_required_by({'key1': 'req1'}, dict(key1='foo'), None) == {}
    assert check_required_by({'key1': 'req1'}, dict(key1='foo', req1='bar'), None) == {}
    assert not check_required_by({'key1': 'req1'}, dict(key1='foo'), None)
    assert not check_required_by({'key1': 'req1'}, dict(), None)
    assert not check_required_by({'key1': 'req1'}, dict(req1='bar'), None)
    assert check_required_by({'key1': 'req1'}, dict(key1='foo'), None) == {}

# Generated at 2022-06-12 23:52:55.578680
# Unit test for function check_required_together
def test_check_required_together():
    param_set1 = {
        'state': 'present',
        'host': '192.168.1.1',
        'username':'admin',
        'password':'passw0rd'
    }
    param_set2 = {
        'state': 'present',
        'host': '192.168.1.1',
        'username':'admin'
    }
    param_set3 = {
        'state': 'present',
        'host': '192.168.1.1',
        'password':'passw0rd'
    }
    param_set4 = {
        'state': 'present',
        'username':'admin',
        'password':'passw0rd'
    }

# Generated at 2022-06-12 23:52:59.680353
# Unit test for function check_type_dict
def test_check_type_dict():
    expected = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    actual = check_type_dict('k1=v1,k2=v2,k3=v3')
    assert actual == expected, "dict with key=value not recognized"
    actual = check_type_dict('{"k1":"v1","k2":"v2","k3":"v3"}')
    assert actual == expected, "valid JSON not recognized"
    actual = check_type_dict('k1=v1,k2=v2,k3=v3')
    assert actual == expected, "dict with key=value not recognized"
    actual = check_type_dict('{"k1":"v1","k2":"v2","k3":"v3"}')

# Generated at 2022-06-12 23:53:03.612609
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.six.moves import StringIO

    code = u"""
try:
    # Wide Unicode string
    value = u'\\U0001f601'
    print(value)
except NameError:
    pass
"""

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    result = safe_eval(code)
    sys.stdout = old_stdout

    assert result == code
    assert mystdout.getvalue() == u'😁\n'



# Generated at 2022-06-12 23:53:14.999236
# Unit test for function safe_eval

# Generated at 2022-06-12 23:53:24.188352
# Unit test for function check_type_dict
def test_check_type_dict():
    value = {"foo":"bar"}
    result = check_type_dict(value)
    assert result == value
    value = "foo=bar"
    result = check_type_dict(value)
    assert result == {'foo': 'bar'}
    value = "foo=bar"
    result = check_type_dict(value)
    assert result == {'foo': 'bar'}
    value = '{"foo": "bar"}'
    result = check_type_dict(value)
    assert result == {'foo': 'bar'}
    value = 'foo="bar",faz="baz"'
    result = check_type_dict(value)
    assert result == {'foo': "bar", "faz": "baz"}
    value = 'foo="bar, baz",faz="baz, faz"'

# Generated at 2022-06-12 23:53:36.227977
# Unit test for function check_type_bits
def test_check_type_bits():
    # Convert a valid human-readable string bits value to integer.
    assert check_type_bits('1Mb') == 1048576

    # Convert an invalid human-readable string bits value raises error.
    try:
        check_type_bits("1Mbb")
    except TypeError as e:
        assert "cannot be converted to a Bit value" in str(e)
    except Exception:
        raise AssertionError("This unhandled exception should not occur.")


# Generated at 2022-06-12 23:53:40.043330
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert check_mutually_exclusive([['a', 'b']], dict(a=1, b=2))
    assert check_mutually_exclusive(None, dict(a=1, b=2))
    assert check_mutually_exclusive(['a', 'b'], dict())



# Generated at 2022-06-12 23:53:46.738716
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('foo') == 'foo'
    assert safe_eval('{"a": {"b": "c"}}') == {"a": {"b": "c"}}
    assert safe_eval('{"a": {"b": "c"}}', include_exceptions=True) == ({'a': {'b': 'c'}}, None)
    assert safe_eval('import os', include_exceptions=True) == ('import os', None)
    assert safe_eval('os.path.join(a, b)', include_exceptions=True) == ('os.path.join(a, b)', None)



# Generated at 2022-06-12 23:53:51.844876
# Unit test for function check_type_int
def test_check_type_int():
    # Checking if the value passed to function is integer type
    test_var_integer = 10
    assert check_type_int(test_var_integer) == 10

    # Checking if the value passed to function is integer string type
    test_var_string_integer = '10'
    assert check_type_int(test_var_string_integer) == 10

    # Checking if the value passed to function is not an integer type
    test_var_string = 'Test Ansible Module'
    try:
        assert check_type_int(test_var_string) == 10
    except TypeError as err:
        assert str(err) == "'str' cannot be converted to an int"



# Generated at 2022-06-12 23:54:02.572909
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('100MB') == 104857600
    assert check_type_bytes('2.5GB') == 2684354560
    assert check_type_bytes('1TB') == 1099511627776
    assert check_type_bytes('1.5PB') == 1649267441664
    assert check_type_bytes('1024') == 1024
    assert check_type_bytes('2KiB') == 2048
    assert check_type_bytes('3MiB') == 3145728
    assert check_type_bytes('4GiB') == 4294967296
    assert check_type_bytes('5TiB') == 5497558138880
    assert check_type_bytes('6PiB') == 1125899906842624

#===----------------------------------------------------------------------===
# Required default constants for new specs
#===

# Generated at 2022-06-12 23:54:06.564595
# Unit test for function check_required_together
def test_check_required_together():
    parameters = {'a':'value a', 'b':'value b'}
    terms = [['a','b']]
    assert check_required_together(terms, parameters) == []
    parameters = {'b':'value b'}
    assert len(check_required_together(terms, parameters)) == 1
    parameters = {'a':'value a', 'c':'value c'}
    assert len(check_required_together(terms, parameters)) == 1


# Generated at 2022-06-12 23:54:17.026381
# Unit test for function check_type_bytes
def test_check_type_bytes():
    from ansible.module_utils._text import to_bytes
    assert check_type_bytes(to_bytes('1 b')) == 1
    assert check_type_bytes(to_bytes('1 kb')) == 1024
    assert check_type_bytes(to_bytes('1 mb')) == 1048576
    assert check_type_bytes(to_bytes('1 gb')) == 1073741824
    assert check_type_bytes(to_bytes('1 tb')) == 1099511627776
    assert check_type_bytes(to_bytes('1 pb')) == 1125899906842624
    assert check_type_bytes(to_bytes('1 eb')) == 1152921504606846976
    assert check_type_bytes(to_bytes('1 zb')) == 1180591620717411

# Generated at 2022-06-12 23:54:25.043254
# Unit test for function check_required_one_of
def test_check_required_one_of():
    # This will fail, no possible match
    assert check_required_one_of([[('a', 'b'),('c', 'd')]],{}) == [['a', 'b']]
    # This will fail, possible matches but none set
    assert check_required_one_of([[('a', 'b'),('c', 'd')]],{'a':'','b':''}) == [['a', 'b']]
    # This will pass, c is set in parameters
    assert check_required_one_of([[('a', 'b'),('c', 'd')]],{'c':'','b':''}) == []
    # This will pass, a is set in parameters

# Generated at 2022-06-12 23:54:35.669505
# Unit test for function check_type_bytes
def test_check_type_bytes():
    tests = {
        '123456789': 123456789,
        '1K': 1024,
        '1M': 1024 * 1024,
        '1G': 1024 * 1024 * 1024,
        '1T': 1024 * 1024 * 1024 * 1024,
        '1P': 1024 * 1024 * 1024 * 1024 * 1024,
        '1E': 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    }
    for test_str, test_int in tests.items():
        assert check_type_bytes(test_str) == test_int, \
                'failed to convert %s to bytes' % test_str
        assert check_type_bytes(test_int) == test_int, \
                'failed to convert %d to bytes' % test_int


# Generated at 2022-06-12 23:54:46.054008
# Unit test for function check_type_bits
def test_check_type_bits():
    for arguments, expected in (
            (["1Mb"], 1048576),
            (["1MB"], 8388608),
            (["1MBb"], 8388608),
            (["1kB"], 1024),
            (["1kb"], 1024),
            (["1k"], 1024),
            (["1"], 1),
            (["1.5MB"], 1572864),
            (["1.5M"], 1572864),
            (["1.5k"], 1536),
            ):
        actual = check_type_bits(arguments[0])
        if actual == expected:
            print("PASS - check_type_bits(%r) = %r" % (arguments, expected))

# Generated at 2022-06-12 23:54:57.796499
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1B') == 1
    assert check_type_bytes('1k') == 1000
    assert check_type_bytes('1M') == 1000000
    assert check_type_bytes('1G') == 1000000000
    assert check_type_bytes(6) == 6
    assert check_type_bytes(6.2) == 6
    raises(TypeError, check_type_bytes, 'Junk')
    raises(TypeError, check_type_bytes, '6Bk')


# Generated at 2022-06-12 23:55:02.682926
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(3) == 3
    assert check_type_int('3') == 3
    assert check_type_int(3.10) == 3
    assert check_type_int("3.10") == 3
    assert check_type_int("hello") == None


# Generated at 2022-06-12 23:55:11.291042
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('0') == 0
    assert check_type_bytes('1024') == 1024
    assert check_type_bytes('1024b') == 1024
    assert check_type_bytes('4kb') == 4096
    assert check_type_bytes('4k') == 4096
    assert check_type_bytes('2mb') == 2097152
    assert check_type_bytes('2gb') == 2147483648
    assert check_type_bytes('2tb') == 2199023255552
    assert check_type_bytes('2pb') == 2251799813685248
    assert check_type_bytes('2eb') == 22702775557312
    with pytest.raises(TypeError):
        check_type_bytes('nan')
    with pytest.raises(TypeError):
        check_type

# Generated at 2022-06-12 23:55:19.777519
# Unit test for function check_type_bytes
def test_check_type_bytes():
    if PY3:
        assert check_type_bytes('1000k') == 1000 * 1024
    else:
        assert check_type_bytes('1000k') == 1000 * 1024 * 1.125
        assert check_type_bytes('5M') == 5242880
# Unit tests for functions check_type_bool, check_type_int, check_type_float
for t in ('bool', 'int', 'float'):
    func = 'check_type_{0}'.format(t)

# Generated at 2022-06-12 23:55:21.006089
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576


# Generated at 2022-06-12 23:55:29.562447
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict("k1=v1,k2=v2") == dict(k1="v1", k2="v2")
    assert check_type_dict("k1=v1,k2=v2,k3=v3") == dict(k1="v1", k2="v2", k3="v3")
    assert check_type_dict("") == dict()
    assert check_type_dict("k1=v1, k2=v2") == dict(k1="v1", k2="v2")
    assert check_type_dict("k1='v1', k2=v2") == dict(k1="v1", k2="v2")

# Generated at 2022-06-12 23:55:38.935112
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(0) == 0
    assert check_type_bytes(1024) == 1024
    assert check_type_bytes(b'10M') == 10 * 1024 * 1024
    assert check_type_bytes(b'10MB') == 10 * 1024 * 1024
    assert check_type_bytes(b'1048576B') == 1048576
    assert check_type_bytes(b'1024Ki') == 1024 * 1024
    assert check_type_bytes(b'1Gi') == 1024 * 1024 * 1024
    assert check_type_bytes(b'1G') == 1024 * 1024 * 1024
    assert check_type_bytes(b'1T') == 1024 * 1024 * 1024 * 1024
    assert check_type_bytes(b'1TiB') == 1024 * 1024 * 1024 * 1024

# Generated at 2022-06-12 23:55:48.466498
# Unit test for function check_required_if
def test_check_required_if():
    assert check_required_if([['state', 'present', ('path',), True]], {'state': 'present', 'path': '/tmp/dir'}, []) == []
    assert check_required_if([['state', 'present', ('path',), True]], {'state': 'present'}, []) == [{'missing': ['path'], 'requires': 'any', 'parameter': 'state', 'value': 'present', 'requirements': ('path', True)}]

# Generated at 2022-06-12 23:55:59.090043
# Unit test for function check_required_by
def test_check_required_by():
    parameters = {'src': 'somewhere', 'dest': 'where'}
    requirements = {'src': ['dest']}
    try:
        check_required_by(requirements, parameters)
        assert False, "Expected an exception because we should fail without a dest"
    except:
        pass
    parameters = {'src': 'somewhere', 'dest': 'where'}
    requirements = {'src': ['dest']}
    try:
        check_required_by(requirements, parameters)
        assert False, "Expected an exception because we should fail without a dest"
    except:
        pass
    requirements = {'src': ['dest', 'foo']}

# Generated at 2022-06-12 23:56:10.744654
# Unit test for function check_required_together
def test_check_required_together():
    terms = [
        ['required_1', 'required_2'],
        ['required_3', 'required_4', 'required_5']]
    parameters = {'required_1': 'value1',
                  'required_2': 'value2',
                  'required_4': 'value4'
                  }
    result = check_required_together(terms, parameters)
    assert result == [], 'Result from required_together check is not empty'
    parameters = {'required_2': 'value2'}
    result = check_required_together(terms, parameters)
    assert result != [], 'Result from required_together check is empty'
    parameters = {'required_1': 'value1'}
    result = check_required_together(terms, parameters)
    assert result != [], 'Result from required_together check is empty'


# Generated at 2022-06-12 23:56:22.888364
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('{"foo":"bar", "baz":"faz"}') == {"foo": "bar", "baz": "faz"}
    assert check_type_dict('foo=bar, baz=faz') == {"foo": "bar", "baz": "faz"}
    assert check_type_dict({'foo':'bar', 'baz':'faz'}) == {"foo": "bar", "baz": "faz"}


# Generated at 2022-06-12 23:56:33.389157
# Unit test for function check_type_bits
def test_check_type_bits():
    test_values = {
        '1Mb': 1048576, 
        '1Mib': 1048576, 
        '500b': 500, 
        '500bits': 500, 
        '256B': 256,
        '1Kb': 1024,
        '1Kib': 1024,
        '10G': 10737418240,
        '10Gb': 10737418240,
        '10Gib': 10737418240,
        '10M': 10485760,
        '10Mb': 10485760,
        '10Mib': 10485760,
        '10K': 10240,
        '10Kb': 10240,
        '10Kib': 10240,
    }
    for key in test_values.keys():
        assert test_values[key] == check_type

# Generated at 2022-06-12 23:56:39.898221
# Unit test for function check_type_float
def test_check_type_float():

    test_cases = [
        ("string that can be cast as float", "10.0", 10.0),
        ("int", 1, 1.0),
        ("float", 1.0, 1.0),
        ("hex", 0xff, 255.0),
        ("oct", 0o10, 8.0)
    ]

    for arg1, arg2, result in test_cases:
        assert check_type_float(arg2) == result
        assert check_type_float(arg2) == result


# Generated at 2022-06-12 23:56:49.377289
# Unit test for function check_type_bytes
def test_check_type_bytes():
    # test valid conversions
    assert b'1k' == check_type_bytes('1k')
    assert b'1m' == check_type_bytes('1m')
    assert b'1g' == check_type_bytes('1g')
    assert b'1t' == check_type_bytes('1t')
    assert b'1p' == check_type_bytes('1p')
    assert b'1K' == check_type_bytes('1K')
    assert b'1M' == check_type_bytes('1M')
    assert b'1G' == check_type_bytes('1G')
    assert b'1T' == check_type_bytes('1T')
    assert b'1P' == check_type_bytes('1P')
    assert b'1k' == check_type_bytes

# Generated at 2022-06-12 23:56:58.813416
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [
        ['params.state', 'created', ('params.settings.foo',), True],
        ['params.state', 'absent', ('params.settings.bar',), False],
    ]
    parameters = {
        'params': {
            'settings': {
                'foo': 'baz',
            },
            'state': 'created',
        }
    }
    results = check_required_if(requirements, parameters, options_context=None)
    assert not results
    parameters['params']['state'] = 'absent'
    results = check_required_if(requirements, parameters, options_context=None)
    assert results[0]['missing'] == ['params.settings.bar']



# Generated at 2022-06-12 23:57:00.504334
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') is 1048576
    return True



# Generated at 2022-06-12 23:57:11.667038
# Unit test for function check_type_bytes
def test_check_type_bytes():
    try:
        check_type_bytes('2M')
    except TypeError:
        raise Exception("Unable to convert 2M")
    try:
        check_type_bytes('2m')
    except TypeError:
        raise Exception("Unable to convert 2m")
    try:
        check_type_bytes('2G')
    except TypeError:
        raise Exception("Unable to convert 2G")
    try:
        check_type_bytes('2g')
    except TypeError:
        raise Exception("Unable to convert 2g")
    try:
        check_type_bytes('2T')
    except TypeError:
        raise Exception("Unable to convert 2T")
    try:
        check_type_bytes('2t')
    except TypeError:
        raise Exception("Unable to convert 2t")
   

# Generated at 2022-06-12 23:57:17.287082
# Unit test for function check_type_bytes
def test_check_type_bytes():
    from ansible.module_utils.basic import bytes_to_human
    assert check_type_bytes("100") == 100
    assert check_type_bytes("1k") == 1024
    assert check_type_bytes("1M") == 1048576
    assert check_type_bytes("1G") == 1073741824
    assert check_type_bytes("1T") == 1099511627776
    assert check_type_bytes("1P") == 1125899906842624



# Generated at 2022-06-12 23:57:18.266042
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576


# Generated at 2022-06-12 23:57:25.143794
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1.01M') == 1048576
    assert check_type_bits('1G') == 1073741824
    assert check_type_bits('1.01G') == 1073741824
    assert check_type_bits('1T') == 1099511627776
    assert check_type_bits('1.01T') == 1099511627776
    assert check_type_bits('1K') == 1024
    assert check_type_bits('1.1K') == 1152
    assert check_type_bits('7K') == 7168
    assert check_type_bits('9K') == 9216
    assert check_type_bits('8Kb') == 8192
    assert check_type_bits('8kb') == 8192
    assert check_type_bits('1.01M') == 10

# Generated at 2022-06-12 23:57:37.973767
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('False') is False
    assert safe_eval('True') is True
    assert safe_eval('None') is None
    assert safe_eval('3') == 3
    assert safe_eval('[3, 4, 5]') == [3, 4, 5]

    # safe_eval should return the original value if it cannot be safely evaluated
    assert safe_eval('3.5') == '3.5'
    assert safe_eval('a_string') == 'a_string'
    assert safe_eval('[3, 4, 5') == '[3, 4, 5'
    assert safe_eval('a_string + 3') == 'a_string + 3'



# Generated at 2022-06-12 23:57:42.601648
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int('123') == 123
    assert check_type_int(123) == 123
    assert check_type_int(123.0) == 123
    try:
        check_type_int('abc')
    except TypeError:
        pass
    try:
        check_type_int(None)
    except TypeError:
        pass
    try:
        check_type_int(['a','b','c'])
    except TypeError:
        pass


# Generated at 2022-06-12 23:57:52.179777
# Unit test for function check_required_arguments

# Generated at 2022-06-12 23:58:05.172489
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(3.3) == 3.3
    assert check_type_float('3.3') == 3.3
    assert check_type_float(b'3.3') == 3.3
    assert check_type_float(u'3.3') == 3.3
    assert check_type_float(3) == 3.0
    assert check_type_float(u'3') == 3.0
    assert check_type_float(b'3') == 3.0
    assert check_type_float('3') == 3.0
    try:
        check_type_float(None)
        assert False
    except TypeError:
        assert True
    check_type_float(False) == False
    check_type_float(True) == True
    check_type_float(u'True')

# Generated at 2022-06-12 23:58:12.274441
# Unit test for function safe_eval
def test_safe_eval():
    value1 = "'1.1.1.1'"
    value2 = "'1.1.1.1' + '1.1.1.1'"
    value3 = "import os"
    value4 = "'127.0.0.1'.split('.')"

    assert safe_eval(value1) == '1.1.1.1'
    assert safe_eval(value2) == '1.1.1.1' + '1.1.1.1'
    assert safe_eval(value3) == 'import os'
    assert safe_eval(value4) == '127.0.0.1'.split('.')



# Generated at 2022-06-12 23:58:14.613630
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes("1MB") == 1048576
    assert check_type_bytes("100TB") == 109951162777600

# Generated at 2022-06-12 23:58:24.335893
# Unit test for function check_type_bits

# Generated at 2022-06-12 23:58:34.224800
# Unit test for function check_required_by
def test_check_required_by():
    assert check_required_by({}, {}) == {}
    assert check_required_by(None, {}) == {}
    assert check_required_by({}, {'a': False}) == {}
    assert check_required_by({'a': 'b'}, {}) == {}
    assert check_required_by({'a': 'b'}, {'a': True}) == {}
    with pytest.raises(TypeError):
        check_required_by({'a': 'b'}, {'a': True, 'b': None})
    with pytest.raises(TypeError):
        check_required_by({'a': 'b'}, {'a': True, 'b': False})



# Generated at 2022-06-12 23:58:41.173762
# Unit test for function check_required_by
def test_check_required_by():
    requirements_list_invalid=[{
        "oracle_user": ["oracle_password"]
    }]
    requirements_list_valid=[{
        "oracle_user": ["oracle_password"]
    }]
    parameters_list_invalid = {
        "oracle_user": "ansible",
    }
    parameters_list_valid ={
        "oracle_user": "ansible",
        "oracle_password": "oracle"
    }
    options_context = ["test"]