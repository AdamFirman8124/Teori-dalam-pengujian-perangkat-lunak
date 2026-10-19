

# Generated at 2022-06-12 23:49:12.926109
# Unit test for function check_type_int
def test_check_type_int():
    checks_ok = (1,    #int
                 "1",  #string
                 "034", #oct
                 "0b1010" #binary
                 )

    checks_fail = ( "abcd", #invalid str
                    "0xFF", # hex 
                    "0b123", #invalid binary
                    "0o66", # invalid octal
                    3.14, # float
                    )
    
    # positive checks
    for check in checks_ok: 
        retval = check_type_int(check)
        assert isinstance(retval, int), "Expected return type int, got %s" % type(retval)
    
    # negative checks
    for check in checks_fail:
        try:
            check_type_int(check)
        except TypeError:
            pass

# Generated at 2022-06-12 23:49:20.717821
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    from nose.plugins.skip import SkipTest
    from ansible.module_utils.six import b
    terms = ['test1', 'test2', 'test3']
    parameters = {}
    result = check_mutually_exclusive(terms, parameters)
    assert len(result) == len([])
    result = check_mutually_exclusive(terms, parameters, options_context=['option_context'])
    assert len(result) == len([])
    parameters = {'test1': 'test'}
    result = check_mutually_exclusive(terms, parameters)
    assert len(result) == len([])
    result = check_mutually_exclusive(terms, parameters, options_context=['option_context'])
    assert len(result) == len([])

# Generated at 2022-06-12 23:49:31.265729
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    dict = {
        'autoscale': False, 'vmss' : True
    }
    check_mutually_exclusive(terms=['autoscale', 'vmss'], parameters=dict)
    try:
        check_mutually_exclusive(terms=['autoscale', 'vmss'], parameters=dict)
    except TypeError as e:
        if "mutually exclusive" in str(e):
            assert True
        else:
            assert False
    try:
        check_mutually_exclusive(terms=['autoscale', 'vmss'],
         parameters=dict, options_context=['vmss'])
    except TypeError as e:
        if "vmss -> mutually exclusive" in str(e):
            assert True
        else:
            assert False



# Generated at 2022-06-12 23:49:41.301102
# Unit test for function safe_eval
def test_safe_eval():
    # Test that cases with module calls don't get evaluated
    assert safe_eval("foo.bar()") == "foo.bar()"
    # Test with simple values
    assert safe_eval("1") == 1
    assert safe_eval("'test'") == 'test'
    assert safe_eval("True") is True
    assert safe_eval("'1'") == '1'
    # Test with complex nesting
    assert safe_eval("{'a':10}") == {'a': 10}
    assert safe_eval("[10,20,30]") == [10, 20, 30]
    # Test that safe_eval does not allow imports
    assert safe_eval("import os") == "import os"



# Generated at 2022-06-12 23:49:47.649304
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # use dict to simulate dict of parameters
    parameters = dict()
    # check valid list
    terms = [['a', 'b'], ['b', 'c']]
    assert check_mutually_exclusive(terms, parameters) == []
    # check invalid list
    terms = [['a', 'b'], ['c', 'b']]
    # noinspection PyBroadException
    try:
        check_mutually_exclusive(terms, parameters)
    except Exception:
        pass
    else:
        assert False



# Generated at 2022-06-12 23:49:55.990779
# Unit test for function check_required_if
def test_check_required_if():
    # Positive test case
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {'state': 'present', 'path': True}
    assert check_required_if(requirements, parameters) == []

    # Negative test case
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {'state': 'absent'}
    try:
        assert check_required_if(requirements, parameters)
    except TypeError:
        pass


# Generated at 2022-06-12 23:50:05.410823
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 1') == 2
    assert safe_eval('[1+1, 2+3]') == [2, 5]
    assert safe_eval('foo.bar()', include_exceptions=True) == ('foo.bar()', None)
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('import foo', include_exceptions=True) == ('import foo', None)
    assert safe_eval('import foo') == 'import foo'
    assert safe_eval('1 + ', include_exceptions=True) == ('1 + ', None)
    assert safe_eval('1 + ') == '1 + '
    # Python 2.6 literal_eval does not support sets.

# Generated at 2022-06-12 23:50:17.392365
# Unit test for function check_required_if
def test_check_required_if():
    """Unit test for function check_required_if"""
    requirements = [['foo', 'bar', ['biz', 'baz']]]
    parameters = {'foo': 'bar'}
    options_context = ['name', 'state']
    assert check_required_if(requirements, parameters, options_context) == []
    assert isinstance(check_required_if(requirements, parameters, options_context), list)

    parameters = {'foo': 'bar', 'biz': 'bar'}
    assert check_required_if(requirements, parameters, options_context) == []
    assert isinstance(check_required_if(requirements, parameters, options_context), list)

    parameters = {'foo': 'bar', 'biz': 'bar', 'baz': 'bar'}

# Generated at 2022-06-12 23:50:26.502051
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1") == 1
    assert safe_eval("[1, 2]") == [1, 2]
    assert safe_eval("[1, 2]") == [1, 2]
    assert safe_eval("{'a': 1, 'b': 2}") == {'a': 1, 'b': 2}
    assert safe_eval("1 + 2") == "1 + 2"
    assert safe_eval("abc.abcdefg(1, 2)") == "abc.abcdefg(1, 2)"
    assert safe_eval("import os") == "import os"
    assert safe_eval("True") is True
    assert safe_eval("'True'") == "True"



# Generated at 2022-06-12 23:50:33.315203
# Unit test for function check_required_if
def test_check_required_if():
    module = None
    parameters = {'state': 'present', 'name': 'test.txt', 'content': 'teststr'}
    required_if = [
        ['state', 'present', ('content',), True],
        ['name', 'test.txt', ('content',)],
        ['state', 'absent', ('content',)],
        ['content', 'teststr', ('name',)],
    ]

    res = check_required_if(required_if, parameters)
    assert res == []
    parameters = {'state': 'present', 'name': 'test.txt'}
    res = check_required_if(required_if, parameters)

# Generated at 2022-06-12 23:50:41.967441
# Unit test for function check_required_together
def test_check_required_together():
    parameters = dict(foo='bar')
    terms = dict(foo='bar', baz='qux')
    assert check_required_together(terms, parameters) == 0

# Generated at 2022-06-12 23:50:47.722472
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Return valid results for missing parameters
    # Return empty list for all required parameters present
    argument_spec = {'test_param': {'required': True}}
    parameters = {}
    (missing_parameters, argument_spec) = check_required_arguments(argument_spec, parameters, 'options')

    assert missing_parameters == ['test_param']
    assert argument_spec == {'test_param': {'required': True}}

    parameters = {'test_param': '1'}
    (missing_parameters, argument_spec) = check_required_arguments(argument_spec, parameters, 'options')

    assert missing_parameters == []
    assert argument_spec == {'test_param': {'required': True}}


# Generated at 2022-06-12 23:50:49.163697
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    check_mutually_exclusive([['a','b']], dict(a=1,b=1))



# Generated at 2022-06-12 23:51:00.364196
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {'name': {
        'required': True,
        'aliases': ['full_name', 'user_name'],
        'type': 'str',
        'default': '',
        'no_log': False,
        'required': False,
    }, 'state': {
        'required': True,
        'choices': ['present', 'absent'],
        'type': 'str'
    }, 'uid': {
        'required': False,
        'type': 'str',
        'default': ''
    }, 'password': {
        'required': False,
        'no_log': True,
        'type': 'str',
        'default': ''
    }}

    # Test a missing required arg

# Generated at 2022-06-12 23:51:05.118866
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    parameters = {}
    mutually_exclusive = [["key1", "key2"]]
    try:
        _ = check_mutually_exclusive(mutually_exclusive, parameters)
        assert False
    except TypeError:
        assert True

    parameters = {"key1": "value1"}
    try:
        _ = check_mutually_exclusive(mutually_exclusive, parameters)
        assert True
    except TypeError:
        assert False



# Generated at 2022-06-12 23:51:16.684005
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits("1MB") == 8388608
    assert check_type_bits("1Mb") == 1048576
    assert check_type_bits("1MBb") == 83886080
    assert check_type_bits("1MBbits") == 83886080
    assert check_type_bits("1mb") == 1048576
    assert check_type_bits("1mbits") == 10485760
    assert check_type_bits("1Kibits") == 1024
    assert check_type_bits("1kb") == 128
    assert check_type_bits("1kbib") == 131072
    assert check_type_bits("1kbibs") == 131072
    assert check_type_bits("1kib") == 1024
    assert check_type_bits("1Kb") == 8192


# Generated at 2022-06-12 23:51:25.911673
# Unit test for function check_required_together
def test_check_required_together():
    """
    Test the check_required_together function.
    """
    arguments = dict(
        name='test',
        wynik1=True,
        wynik2=False,
        wynik3=True,
        wynik4=False,
        wynik5=True,
        wynik7=False,
    )
    terms = [('wynik1', 'wynik2'), ('wynik3', 'wynik4'), ('wynik5', 'wynik7')]
    result = check_required_together(terms, arguments)
    assert result == []
    arguments = dict(
        name='test',
        wynik1=True,
        wynik3=True,
        wynik5=True,
    )
    result = check_required_together(terms, arguments)
   

# Generated at 2022-06-12 23:51:31.134401
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # pylint: disable=no-self-use
    argument_spec = dict(
        a=dict(required=True),
        b=dict(required=False)
    )
    assert [] == check_required_arguments(argument_spec, dict(a=1, b=2))
    with pytest.raises(TypeError):
        check_required_arguments(argument_spec, dict(b=2))



# Generated at 2022-06-12 23:51:41.791886
# Unit test for function check_required_arguments
def test_check_required_arguments():

    argument_spec = {
        "name": {"required": True, "type": "str"},
        "type": {"required": True, "type": "str"}
    }

    parameters = {"name": "test_name"}
    missing = check_required_arguments(argument_spec, parameters)
    assert len(missing) == 1
    assert 'type' in missing

    parameters = {"type": "test_type"}
    missing = check_required_arguments(argument_spec, parameters)
    assert len(missing) == 1
    assert 'name' in missing

    parameters = {}
    missing = check_required_arguments(argument_spec, parameters)
    assert len(missing) == 2
    assert 'name' in missing
    assert 'type' in missing


# Generated at 2022-06-12 23:51:53.632342
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits("100") == 100, "100 bits should return 100"
    assert check_type_bits("1K") == 1024, "1024 bits should return 1K"
    assert check_type_bits("1kb") == 1024, "1024 bits should return 1kb"
    assert check_type_bits("1M") == 1048576, "1048576 bits should return 1M"
    assert check_type_bits("1Mb") == 1048576, "1048576 bits should return 1Mb"
    assert check_type_bits("1G") == 1073741824, "1073741824 bits should return 1G"
    assert check_type_bits("1Gb") == 1073741824, "1073741824 bits should return 1Gb"

# Generated at 2022-06-12 23:52:07.692039
# Unit test for function check_required_one_of
def test_check_required_one_of():
    # Positive tests
    check_required_one_of([['a', 'b'], ['c', 'd']], {'a': 1, 'b': 2, 'c': 3})
    check_required_one_of([['a', 'b'], ['c', 'd']], {'a': 1, 'b': 2})
    check_required_one_of('a', {'a': 1})
    check_required_one_of(['a'], {'a': 1})
    check_required_one_of('a', {'a': 1})
    # Negative tests

# Generated at 2022-06-12 23:52:13.116556
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int(str(1)) == 1
    with pytest.raises(TypeError):
        check_type_int(["1"])
    with pytest.raises(TypeError):
        check_type_int(1.0)


# Generated at 2022-06-12 23:52:22.380809
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # Empty argument spec and empty parameters
    assert [] == check_required_arguments({}, {})
    # Empty argument spec, non-empty parameters
    assert [] == check_required_arguments({}, {'a':'b'})
    # Non-empty argument spec, empty parameters
    assert ['key'] == check_required_arguments({'key':{'required':True}}, {})
    # Non-empty argument spec and non-empty parameters
    assert [] == check_required_arguments({'key':{'required':True}}, {'key':'value'})
    # Non-empty argument spec with required and non-required keys and non-empty parameters
    assert [] == check_required_arguments({'key':{'required':True}, 'key2':{'required':False}}, {'key':'value'})


# Generated at 2022-06-12 23:52:28.608176
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[1,2,3]") == [1,2,3]
    assert safe_eval("{'a':1, 'b':[1,2,3]}") == {'a':1, 'b':[1,2,3]}
    assert safe_eval("1 + 2") == 3
    assert safe_eval("import os") == "import os"
    assert safe_eval("os.system('echo blah')") == "os.system('echo blah')"
    assert safe_eval("set()") == "set()"



# Generated at 2022-06-12 23:52:40.060501
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(1) == 1
    assert check_type_bytes('1') == 1
    assert check_type_bytes('1b') == 1
    assert check_type_bytes('1k') == 1024
    assert check_type_bytes('1kb') == 1024
    assert check_type_bytes('1m') == 1048576
    assert check_type_bytes('1mb') == 1048576
    assert check_type_bytes('10gb') == 10737418240
    assert check_type_bytes('1t') == 1099511627776
    assert check_type_bytes('1tb') == 1099511627776
    assert check_type_bytes('1p') == 1125899906842624
    assert check_type_bytes('1pb') == 1125899906842624



# Generated at 2022-06-12 23:52:50.666661
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(1) == 1
    assert check_type_bytes('1') == 1
    assert check_type_bytes('1B') == 1
    assert check_type_bytes('1.0B') == 1
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1M') == 1024 * 1024
    assert check_type_bytes('1G') == 1024 * 1024 * 1024
    assert check_type_bytes('1T') == 1024 * 1024 * 1024 * 1024
    assert check_type_bytes('1P') == 1024 * 1024 * 1024 * 1024 * 1024
    assert check_type_bytes('1E') == 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert check_type_bytes('1Ki') == 1024

# Generated at 2022-06-12 23:52:59.732333
# Unit test for function check_required_together
def test_check_required_together():
    terms = [['name', 'state'], ['name', 'password']]
    parameters = dict(name='test')
    options_context = dict(name='test')
    check = check_required_together(terms, parameters)
    assert check == []

    parameters = dict(name='test', password='test')
    options_context = dict(name='test')
    check = check_required_together(terms, parameters)
    assert check == []

    parameters = dict(name='test', password='test', state='absent')
    options_context = dict(name='test')
    check = check_required_together(terms, parameters)
    assert check == []

    parameters = dict(name='test', password='test', state='present')
    options_context = dict(name='test')

# Generated at 2022-06-12 23:53:04.469808
# Unit test for function check_type_bytes
def test_check_type_bytes():
    test_cases = {
        "1": 1,
        '2KB': 2 * 1024,
        '2MB': 2 * 1024 * 1024,
        "1.5GB": 1.5 * 1024 * 1024 * 1024,
        "1.5TB": 1.5 * 1024 * 1024 * 1024 * 1024,
        b'1.5 TB': 1.5 * 1024 * 1024 * 1024 * 1024,
        '0': 0,
        0: 0
    }
    for input_value, output_value in test_cases.items():
        assert check_type_bytes(input_value) == output_value


# FIXME: The param and prefix parameters here are coming from AnsibleModule._check_type_string()
#        which is using those for the warning messaged based on string conversion warning settings.
#        Not sure how to deal with that here since

# Generated at 2022-06-12 23:53:11.185575
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    required_parameters = ['z','c']
    parameters = {'z': 'z'}
    result1 = check_missing_parameters(parameters,required_parameters)
    assert len(result1) == 1

    parameters = {'z': 'z', 'c': 'c'}
    result2 = check_missing_parameters(parameters,required_parameters)
    assert len(result2) == 0



# Generated at 2022-06-12 23:53:21.263612
# Unit test for function check_required_one_of
def test_check_required_one_of():
    terms = [[1, 2], [3]]
    parameters = {
        'a': 1
    }
    assert check_required_one_of(terms, parameters) == []
    parameters = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    assert check_required_one_of(terms, parameters) == []
    parameters = {
        'c': 3
    }
    assert check_required_one_of(terms, parameters) == []
    parameters = {
        'b': 2,
        'c': 3
    }
    assert check_required_one_of(terms, parameters) == []
    parameters = {
        'b': 2,
        'c': 3
    }
    assert check_required_one_of(terms, parameters) == []

# Generated at 2022-06-12 23:53:29.774694
# Unit test for function check_required_arguments
def test_check_required_arguments():
    arg_spec = {'a': {'required': False}, 'b': {'required': True}}
    parameters = {'a': '1', 'b': '2'}
    missing = check_required_arguments(arg_spec, parameters)
    assert missing == []
    arg_spec = {'a': {'required': False}, 'b': {'required': True}}
    parameters = {'a': '1'}
    missing = check_required_arguments(arg_spec, parameters)
    assert missing == ['b']



# Generated at 2022-06-12 23:53:34.784900
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{"foo": "bar"}', include_exceptions=True) == ({'foo': 'bar'}, None)
    assert safe_eval('{"foo": "bar"}', include_exceptions=True)[0] == {'foo': 'bar'}
    assert safe_eval('{"foo": "bar"}', include_exceptions=True)[1] is None
    assert safe_eval('{"foo": "bar"}') == {'foo': 'bar'}
    assert safe_eval('import foo') == 'import foo'
    assert safe_eval('{"foo": "bar"}.get("foo")') == '{"foo": "bar"}.get("foo")'
    assert safe_eval('{"foo": "bar"}[0]') == '{"foo": "bar"}[0]'



# Generated at 2022-06-12 23:53:44.622483
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('{"a":1,"b":2}') == eval('{"a":1,"b":2}')
    assert check_type_dict('a=1,b=2') == eval('{"a":1,"b":2}')
    assert check_type_dict('a=1, b=2') == eval('{"a":1,"b":2}')
    assert check_type_dict('a=1, b=2, c=3, d=4') == eval('{"a":1,"b":2,"c":3,"d":4}')
    assert check_type_dict('a=1, b=2, c=3, d=4') == eval('{"a":1,"b":2,"c":3,"d":4}')

# Generated at 2022-06-12 23:53:54.064984
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('23') == 23
    assert safe_eval('34 + 12') == 46
    assert safe_eval([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert safe_eval('{"a": 1, "b": 2}') == {u'a': 1, u'b': 2}

    # not allowed: ast.Call
    assert safe_eval('len([1,2,3])') == 'len([1,2,3])'
    # not allowed: ast.Import
    assert safe_eval('import os') == 'import os'
    # not allowed: ast.Attribute
    assert safe_eval('os.path.exists("/etc")') == 'os.path.exists("/etc")'



# Generated at 2022-06-12 23:54:03.085760
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.1) == 1.1
    assert check_type_float("1.1") == 1.1
    assert check_type_float("1,1") == 1.1
    assert check_type_float(1) == 1
    assert check_type_float(u"1") == 1
    assert check_type_float(u"1.1") == 1.1
    assert check_type_float(b"1") == 1
    assert check_type_float(b"1.1") == 1.1
    try:
        check_type_float(None)
    except TypeError:
        pass
    else:
        assert False


# Generated at 2022-06-12 23:54:11.752975
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval(u'{"a": 1, "b": 2}') == {"a": 1, "b": 2}
    assert safe_eval(u"[1, 2, 3]") == [1, 2, 3]
    assert safe_eval(u"True") is True
    assert safe_eval(u"False") is False
    assert safe_eval(u"5") == 5
    assert safe_eval(u'{"a": 1, "b": 2}', include_exceptions=True) == ({"a": 1, "b": 2}, None)
    assert safe_eval(u'[1, 2, 3]', include_exceptions=True) == ([1, 2, 3], None)
    assert safe_eval(u'True', include_exceptions=True) == (True, None)

# Generated at 2022-06-12 23:54:22.461453
# Unit test for function safe_eval
def test_safe_eval():
    class FakeMod(object):
        def fakemethod(*args, **kwargs):
            return "success"
    fake_mod = FakeMod()
    # Test case: no method call, no exception
    assert safe_eval("[1, 2, 3]") == [1, 2, 3]
    # Test case: a method call, no exception
    assert safe_eval("fake_mod.fakemethod()") == "success"
    # Test case: both a method call and an import, exception
    assert safe_eval("import abc") == "import abc"
    # Test case: both a method call and an import, exception
    assert safe_eval("import abc", include_exceptions=True) == ("import abc", None)
    # Test case: basic template, no exception

# Generated at 2022-06-12 23:54:23.872297
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576


# Generated at 2022-06-12 23:54:34.953720
# Unit test for function check_required_one_of
def test_check_required_one_of():
    l1 = [1, 2, 3]
    l2 = [1, 2, 3, 4]
    m1 = [l1, l2]
    m2 = [(1,2,3), (1,)]
    m3 = [l1, (1,2,3), l2]
    m4 = [l1, (1,), l2]
    p1 = {}
    p2 = {'x':2}
    p3 = {'x':2, 'y':1}
    p4 = {'x': 2, 'y': 1, 'z': 1}
    p5 = {'x': 2, 'y': 1, 'z': 1, 'w': 1}


# Generated at 2022-06-12 23:54:45.926397
# Unit test for function check_required_by
def test_check_required_by():
    input_data = {'a': 'aaa', 'b': 'bbb'}
    input_requirements = {'a': ['b']}
    result = check_required_by(input_requirements, input_data)
    assert result == {}

    input_data = {'a': 'aaa', 'b': None}
    input_requirements = {'a': ['b']}
    result = check_required_by(input_requirements, input_data)
    assert result == {'a': ['b']}

    input_data = {'a': 'aaa'}
    input_requirements = {'a': ['b']}
    result = check_required_by(input_requirements, input_data)
    assert result == {'a': ['b']}


# Generated at 2022-06-12 23:55:02.032505
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1b') == 1
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1Kb') == 1024
    assert check_type_bits('1Kb') == 1024
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Gb') == 1073741824
    assert check_type_bits('1Tb') == 1099511627776
    assert check_type_bits('1Pb') == 1125899906842624
    assert check_type_bits('1Eb') == 1152921504606846976
    assert check_type_bits('1Zb') == 1180591620717411303424
    assert check_type_bits('1Yb') == 1208925819614629174706

# Generated at 2022-06-12 23:55:10.902540
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'foo': {'required': True},
        'bar': {'required': False},
        'baz': {'required': True},
    }
    parameters = {'foo': 1, 'bar': 2}
    options_context = None

# Generated at 2022-06-12 23:55:18.615090
# Unit test for function check_required_one_of
def test_check_required_one_of():
    terms = [['a', 'b'], ['x']]
    parameters = {}

    check_required_one_of(terms, parameters)

    parameters['a'] = 'a'
    check_required_one_of(terms, parameters)
    parameters['x'] = 'x'
    check_required_one_of(terms, parameters)

    parameters['b'] = 'b'
    try:
        check_required_one_of(terms, parameters)
        assert False
    except TypeError:
        pass



# Generated at 2022-06-12 23:55:23.925421
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(5)==5
    assert type(check_type_int(5))==int
    assert check_type_int('5')==5
    with pytest.raises(TypeError) as excinfo:
        check_type_int('a')
    assert 'a cannot be converted to an int' in str(excinfo.value)



# Generated at 2022-06-12 23:55:29.131059
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int('1') == 1
    assert check_type_int(1) == 1
    raises(TypeError, check_type_int, True)
    raises(TypeError, check_type_int, 1.1)
    raises(TypeError, check_type_int, [1, 1])


# Generated at 2022-06-12 23:55:34.489028
# Unit test for function check_type_int
def test_check_type_int():
    assert isinstance(check_type_int(1), int)
    assert isinstance(check_type_int(1.1), int)
    assert isinstance(check_type_int('1'), int)
    assert isinstance(check_type_int('1.1'), int)
    assert isinstance(check_type_int([]), int)


# Generated at 2022-06-12 23:55:40.866030
# Unit test for function check_type_int
def test_check_type_int():
    def inner(value, expected=None, error=None):
        if error:
            with pytest.raises(TypeError, match=error):
                check_type_int(value)
        else:
            assert check_type_int(value) == expected

    inner(1, 1)
    inner(0.1, 0, 'are <class \'float\'>.*?<class \'int\'>')
    inner('a', 'a', 'are <class \'str\'>.*?<class \'int\'>')
    inner('1', 1)
    inner('0.1', 0, 'are <class \'str\'>.*?<class \'int\'>')



# Generated at 2022-06-12 23:55:47.208309
# Unit test for function check_required_together
def test_check_required_together():
    terms = [['netmask', 'prefix'], ['network', 'prefix'], ['network', 'netmask']]
    parameters = {'netmask': '255.255.255.0', 'network': '10.10.10.1'}
    options_context = None
    assert check_required_together(terms, parameters, options_context) == []
    parameters = {'netmask': '255.255.255.0'}
    assert check_required_together(terms, parameters, options_context) == [['netmask', 'network'], ['netmask', 'prefix']]




# Generated at 2022-06-12 23:55:51.590108
# Unit test for function check_required_arguments
def test_check_required_arguments():
    mod_arg_spec = dict(
        foo=dict(required=True),
        bar=dict(required=True),
        baz=dict(),
        foobar=dict(required=True)
    )

    missing_all_required = {}
    missing_foo_required = dict(bar='BAR', baz='BAZ', foobar='FOOBAR')
    missing_bar_required = dict(foo='FOO', baz='BAZ', foobar='FOOBAR')
    missing_foobar_required = dict(foo='FOO', bar='BAR', baz='BAZ')

    assert check_required_arguments(mod_arg_spec, missing_all_required) == []


# Generated at 2022-06-12 23:56:03.925028
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("123") == 123
    assert safe_eval("'123'") == '123'
    assert safe_eval("None") is None
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("True or False") is True
    assert safe_eval("False or True") is True
    assert safe_eval("True and False") is False
    assert safe_eval("True and []") == []
    assert safe_eval("True and {}") == {}
    assert safe_eval("True and None") is None
    assert safe_eval("True and 'xyz'") == 'xyz'
    assert safe_eval("False and 'xyz'") is False
    assert safe_eval("[]") == []
    assert safe_eval("()") == ()
    assert safe_eval

# Generated at 2022-06-12 23:56:14.931665
# Unit test for function check_type_dict
def test_check_type_dict():
    data = "a=1, b=2, c=3"
    rv = check_type_dict(data)
    assert isinstance(rv, dict)
    assert rv['a'] == '1'
    assert rv['b'] == '2'
    assert rv['c'] == '3'


# Generated at 2022-06-12 23:56:23.235381
# Unit test for function check_required_arguments
def test_check_required_arguments():
    assert check_required_arguments({
        'a': {'required': True},
        'b': {'required': True},
        'c': {'required': True},
        'd': {'required': True},
        'e': {'required': False},
        'f': {'required': False}
    }, {
        'a': None,
        'f': None
    }) == ['b', 'c', 'd']


# only allowed to have a dict in a dict if the dict is a dict key or inside a list
# known exceptions are 'data' and 'xml', which are allowed to have dicts as a value

# Generated at 2022-06-12 23:56:33.688061
# Unit test for function check_type_bytes
def test_check_type_bytes():
    data_set_str = ['2K', '2KB', '2kilobytes', '2 kilobytes', '2k']
    for data in data_set_str:
        if check_type_bytes(data) != 2048:
            raise AssertionError

    data_set_int = [2048, '2048']
    for data in data_set_int:
        if check_type_bytes(data) != 2048:
            raise AssertionError

    data_set_float = [2.5, '2.5']
    for data in data_set_float:
        if check_type_bytes(data) != 2560:
            raise AssertionError

    data_set_byte = ['10b', '10bytes', '10 bytes', '10B']

# Generated at 2022-06-12 23:56:37.368909
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    try:
        check_type_bits('1048576b')
        assert False, "Should raise type error if value is not in correct format"
    except TypeError:
        assert True


# Generated at 2022-06-12 23:56:42.075164
# Unit test for function check_required_by
def test_check_required_by():
    assert check_required_by(
        {'one': 'two'}, {'one': True, 'two': True}) == {}
    assert check_required_by(
        {'one': 'two'}, {'one': True, 'two': False}) == {'one': ['two']}



# Generated at 2022-06-12 23:56:49.978269
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1G') == 1073741824
    assert check_type_bytes('1T') == 1099511627776
    assert check_type_bytes('1P') == 1125899906842624
    assert check_type_bytes('1E') == 1152921504606846976
    assert check_type_bytes('1Z') == 1180591620717411303424
    assert check_type_bytes('1Y') == 1208925819614629174706176



# Generated at 2022-06-12 23:56:55.703577
# Unit test for function check_type_bytes
def test_check_type_bytes():
    tests = [
        ('20B', 20),
        ('1K', 1024),
        ('2M', 2097152),
        ('3G', 3221225472),
        ('4T', 42949672942),
    ]
    for test_string, test_bytes in tests:
        assert check_type_bytes(test_string) == test_bytes


# Generated at 2022-06-12 23:57:00.053067
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Return true if the check passes, false otherwise."""
    terms = [["name", "provider"],
             ["instance_ids", "filters"]]
    parameters = dict()
    parameters['name'] = "test"

    try:
        results = check_mutually_exclusive(terms, parameters)
    except TypeError as e:
        print(e)



# Generated at 2022-06-12 23:57:09.425288
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1kb') == 1024
    assert check_type_bits('1.5Mb') == 1572864
    assert check_type_bits('1.0Mb') == 1048576
    assert check_type_bits('1b') == 1
    assert check_type_bits(1.5) == 1
    assert check_type_bits(1) == 1
    assert check_type_bits(1.0) == 1
    assert check_type_bits('1') == 1
    assert_raises(TypeError, check_type_bits, {'a': 'b'})



# Generated at 2022-06-12 23:57:16.546204
# Unit test for function check_required_one_of
def test_check_required_one_of():
    """Unit test for function check_required_one_of"""

    terms = [["a1", "a2"], ["b1", "b2"]]
    parameters = dict(a1=1)

    results = check_required_one_of(terms, parameters)
    assert not results
    parameters = dict(c1=1)

# Generated at 2022-06-12 23:57:32.488675
# Unit test for function check_required_by
def test_check_required_by():
    REQUIREMENTS = {
        'key1': 'key2',
        'key2': 'key3',
        'key3': ['key4', 'key5']
    }
    PARAMETERS = {
        'key1': '',
        'key2': '',
        'key3': '',
        'key4': '',
        'key5': '',
    }
    result = check_required_by(REQUIREMENTS, PARAMETERS)
    assert not result
    del PARAMETERS['key5']
    result = check_required_by(REQUIREMENTS, PARAMETERS)
    assert result
    assert result['key3'] == ['key5']



# Generated at 2022-06-12 23:57:40.907397
# Unit test for function safe_eval
def test_safe_eval():
    test_value = [
        ('1', 1),
        ('[1,2,3]', [1, 2, 3]),
        ('{1:1,2:2}', {1: 1, 2: 2}),
        ('a', 'a'),
        ('(1,2,3)', (1, 2, 3)),
        ('1 + 1', '1 + 1'),
        ('"a"', 'a'),
        ('True', True),
        ('b.pop()', 'b.pop()'),
        ('import os', 'import os'),
        ('True or False', True),
        ('True or False and False or False', True)
    ]
    for (val, result) in test_value:
        assert safe_eval(val) == result


# Generated at 2022-06-12 23:57:45.929008
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test function safe_eval
    """
    assert safe_eval('123') == 123
    assert safe_eval('[1, 2,3]') == [1, 2, 3]
    assert safe_eval('{"a": "b"}') == {"a": "b"}
    assert safe_eval('1+1') == 1+1
    assert safe_eval('"1+1"') == "1+1"
    assert safe_eval('(1,2)') == (1, 2)
    assert safe_eval('import json') == 'import json'
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('foo.ba(a)') == 'foo.ba(a)'

    # test inclusive exceptions

# Generated at 2022-06-12 23:57:54.240725
# Unit test for function check_required_one_of
def test_check_required_one_of():
    # Assert: empty input
    assert check_required_one_of(None, None) == []
    # Assert: empty list of choice
    assert check_required_one_of(None, {'abc': 1}) == []
    assert check_required_one_of([], {'abc': 1}) == []
    # Assert: one of choices missing
    assert check_required_one_of([['a']], {}) == [['a']]
    assert check_required_one_of([['a']], {'b': 1}) == [['a']]
    assert check_required_one_of([['a', 'b']], {}) == [['a', 'b']]
    assert check_required_one_of([['a', 'b']], {'b': 1}) == []
    assert check_required_one_

# Generated at 2022-06-12 23:58:07.227960
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(0) == 0
    assert check_type_bytes(0.1) == 0
    assert check_type_bytes(0.5) == 0
    assert check_type_bytes(1) == 1
    assert check_type_bytes('1MB') == 1048576
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1MB') == 1048576
    assert check_type_bytes('1 MiB') == 1048576
    assert check_type_bytes('1 mebibytes') == 1048576
    assert check_type_bytes('1 kilobyte') == 1024
    assert check_type_bytes('1kilobyte') == 1024
    assert check_type_bytes('1kilobytes') == 1024

# Generated at 2022-06-12 23:58:18.213744
# Unit test for function check_required_by
def test_check_required_by():
    parameters = dict(a='a', b='b', c='c', d=None)
    # None case
    requirements = None
    options_context = None
    result = check_required_by(requirements, parameters, options_context)
    assert result == {}
    # Normal case
    requirements = dict(b=['a', 'd'], d=['c'])
    options_context = None
    result = check_required_by(requirements, parameters, options_context)
    assert result == {}
    requirements = dict(b=['a', 'd'], d=['c', 'f'])
    options_context = None
    result = check_required_by(requirements, parameters, options_context)
    assert result == {'d': ['f']}
    # Error case

# Generated at 2022-06-12 23:58:21.203509
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    with pytest.raises(TypeError):
        assert check_type_bits('1AB')
    assert check_type_bits('1.5Mb') == 1572864


# Generated at 2022-06-12 23:58:27.816970
# Unit test for function check_required_one_of
def test_check_required_one_of():

    # Return TypeError if parameters is empty dictionary
    parameters = {}
    try:
        check_required_one_of(['assetid', 'assetname'], parameters)
    except TypeError:
        pass
    else:
        return 'one of the following is required: assetid, assetname'

    # Return TypeError if one parameter in the one of the list is not in parameters
    parameters = {'assetname':'A','b':'C'}
    try:
        check_required_one_of([['assetname','assetid'],['b','c']], parameters)
    except TypeError:
        pass
    else:
        return 'one of the following is required: assetid'

    # Return empty list if not return TypeError
    parameters = {'assetname':'A','b':'C'}

# Generated at 2022-06-12 23:58:33.092612
# Unit test for function check_type_int
def test_check_type_int():
    assert type(check_type_int(1)) is int
    assert type(check_type_int(100)) is int
    assert type(check_type_int("1")) is int
    assert type(check_type_int("100")) is int
    with pytest.raises(TypeError):
        assert type(check_type_int("A")) is int

