

# Generated at 2022-06-12 23:49:10.613483
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Gb') == 1073741824



# Generated at 2022-06-12 23:49:16.878902
# Unit test for function check_required_arguments
def test_check_required_arguments():
    ok_params = dict(foo='bar')
    missing_params = dict()
    argspec = dict(foo=dict(required=True))
    res = check_required_arguments(argspec=argspec, parameters=ok_params)
    assert not res
    res = check_required_arguments(argspec=argspec, parameters=missing_params)
    assert 'foo' in res



# Generated at 2022-06-12 23:49:21.355314
# Unit test for function check_type_dict
def test_check_type_dict():
    assert check_type_dict('{"a": 1, "b": "two", "c": \'three\'}') == {"a": 1, "b": "two", "c": 'three'}
    assert check_type_dict('a=1, b="two", c=\'three\'') == {"a": "1", "b": "two", "c": 'three'}
    assert check_type_dict('abc') == {"a": "b", "c": None}
    assert check_type_dict('{a: 1, b: "two", c: \'three\'}') == {"a": 1, "b": "two", "c": 'three'}
    assert check_type_dict('["a", "b", "c"]') == ['a', 'b', 'c']

# Generated at 2022-06-12 23:49:27.622984
# Unit test for function check_required_by
def test_check_required_by():
    """ Test check_required_by function. """
    test = { 'a': 'b', 'c': None }
    requirements = { 'a': 'c', 'd': 'b' }
    try:
        check_required_by(requirements, test)
    except TypeError as e:
        assert str(e) == 'missing parameter(s) required by b: a'
        return
    assert False
# unit test for function check_required_by

# Generated at 2022-06-12 23:49:34.570963
# Unit test for function check_required_together
def test_check_required_together():
    requirements = [
        ("a", "b"),
        ("b", "a")
    ]
    # Test both fail
    with pytest.raises(TypeError):
        check_required_together(requirements, {"c":"c"})
    # Test first successes
    with pytest.raises(TypeError):
        check_required_together(requirements, {"a":"a", "c":"c"})
    # Test second successes
    with pytest.raises(TypeError):
        check_required_together(requirements, {"b":"b", "c":"c"})
    # Test both success
    check_required_together(requirements, {"a":"a","b":"b"})



# Generated at 2022-06-12 23:49:43.942354
# Unit test for function check_required_if
def test_check_required_if():
    parameters = {}
    # Missing required parameters
    requirements = [
        ['state', 'present', ('path',), True]
    ]
    msg = "path is present but any of the following are missing: path"
    try:
        check_required_if(requirements, parameters)
    except TypeError as e:
        assert str(e) == msg

    # One required parameters is present
    parameters = dict(path='/tmp/')
    requirements = [
        ['state', 'present', ('path',), True]
    ]
    try:
        assert check_required_if(requirements, parameters) == []
    except TypeError as e:
        assert False

    # One required parameter is missing
    parameters = dict(path='/tmp/')

# Generated at 2022-06-12 23:49:53.421892
# Unit test for function check_required_if
def test_check_required_if():
    req = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {
        'state': 'present',
        'bool_param': True
    }
    result = check_required_if(req, parameters)
    assert result == []
    assert result == [{'missing': [], 'requires': 'any', 'parameter': 'state', 'value': 'present', 'requirements': ('path',)}]
    assert result == [{'missing': ['string_param'], 'requires': 'all', 'parameter': 'someint', 'value': 99, 'requirements': ('bool_param', 'string_param')}]



# Generated at 2022-06-12 23:50:04.958221
# Unit test for function check_required_by
def test_check_required_by():
    unpacked_params_none = {
        'foo': None,
        'bar': 'hello',
        'baz': None
    }
    unpacked_params_no_none = {
        'foo': 'hello',
        'bar': 'hello',
        'baz': 'hello'
    }
    unpacked_params_partial_none = {
        'foo': 'hello',
        'bar': None,
        'baz': 'hello'
    }
    unpacked_params_no_none_two = {
        'foo': 'hello',
        'bar': 'hello',
        'baz': 'hello',
        'spam': 'hello',
        'eggs': 'hello'
    }


# Generated at 2022-06-12 23:50:08.259245
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    with pytest.raises(TypeError):
        check_type_bits(None)


# Generated at 2022-06-12 23:50:16.144933
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # tests should always raise TypeError when mutually exclusive params are present
    # otherwise, we may be hiding bugs in our modules (no errors raised)
    try:
        check_mutually_exclusive([['one', 'two'], ['three', 'four'], 'five', ['six', 'seven']],
                                 {'one': 'one', 'two': 'two', 'three': 'three', 'six': 'six', 'five': 'five'})
        assert False
    except TypeError:
        pass


# Generated at 2022-06-12 23:50:39.647440
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1 Mb') == 1048576
    assert check_type_bits(1048576) == 1048576
    assert check_type_bits('1M') == 1048576
    assert check_type_bits('1.5Mb') == 1572864
    assert check_type_bits('1.5MB') == 1572864
    assert check_type_bits('1.5 Mb') == 1572864
    assert check_type_bits('1.5M') == 1572864
    assert check_type_bits('1.5') == 1572864
    assert check_type_bits('1.5b') == 2
    assert check_type_bits('1.5kb') == 1536

# Generated at 2022-06-12 23:50:47.549225
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    assert check_missing_parameters(dict(), None) == []
    assert check_missing_parameters(dict(one=1), list()) == []
    assert check_missing_parameters(dict(one=1), ['one']) == []
    assert check_missing_parameters(dict(one=1), ['two']) == ['two']
    assert check_missing_parameters(dict(one=1), ['one', 'two']) == ['two']


# Generated at 2022-06-12 23:50:55.695392
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec_1 = {'a': {'required': True}}
    parameters_1 = {'a': 1}

    assert(check_required_arguments(argument_spec_1, parameters_1) == [])

    argument_spec_2 = {'a': {'required': True}}
    parameters_2 = {}

    try:
        check_required_arguments(argument_spec_2, parameters_2)
    except TypeError as e:
        assert(str(e) == 'missing required arguments: a')



# Generated at 2022-06-12 23:51:04.828398
# Unit test for function safe_eval
def test_safe_eval():
    module_name = 'test_safe_eval'
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.exit_json(**{'msg': 'Unit tests for %s' % module_name})
    failure_msg = 'Failed to evaluate string "%s" (exception "%s"): expected "%s", got "%s"'
    success_msg = 'Successfully evaluated string "%s": "%s"'

# Generated at 2022-06-12 23:51:13.516482
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1,2,3]') == [1,2,3]
    assert safe_eval('"foo"') == "foo"
    # asserts that the value is returned if the expression
    # would have resulted in a NameError
    assert safe_eval('foo') == "foo"
    assert safe_eval('foo(bar)') == "foo(bar)"
    assert safe_eval('"foo(bar)"') == "foo(bar)"
    assert safe_eval('import foo') == "import foo"

# ===========================================
# Common Arguments


# Generated at 2022-06-12 23:51:18.962684
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = {
        'foo': {'required': True},
        'bar': {'required': False}
    }

    parameters = {'foo': 'foo'}
    assert check_required_arguments(argument_spec, parameters) == []

    parameters = {'bar': 'bar'}
    assert check_required_arguments(argument_spec, parameters) == ['foo']



# Generated at 2022-06-12 23:51:25.603711
# Unit test for function check_missing_parameters
def test_check_missing_parameters():
    # Check that a correct case works
    try:
        check_missing_parameters(dict(a=1), ['a'])
        # Shouldn't get here
        assert False
    except TypeError:
        assert False

    # Check that a missing check fails
    try:
        check_missing_parameters(dict(), ['a'])
        # Shouldn't get here
        assert False
    except TypeError:
        pass

    # Check that an extra check fails
    try:
        check_missing_parameters(dict(a=1, b=2), ['b'])
        # Shouldn't get here
        assert False
    except TypeError:
        pass

    return True



# Generated at 2022-06-12 23:51:27.855152
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1MB') == 1048576
    assert check_type_bits('2Mb') == 2097152



# Generated at 2022-06-12 23:51:31.520601
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int("1") == 1
    assert check_type_int("0xFF") == 255

    try:
        check_type_int("A")
        raise AssertionError("Should have failed with int conversion but did not")
    except TypeError as e:
        assert "cannot be converted to an int" in str(e)



# Generated at 2022-06-12 23:51:42.120953
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('{"foo": "bar"}') == {u'foo': u'bar'}
    assert safe_eval('{"foo": "bar"', include_exceptions=True)[0] == {u'foo': u'bar'}
    assert safe_eval('{"foo": "bar"', include_exceptions=True)[1] is None

    # test some evil
    assert safe_eval('__import__("os").getcwd()') == '__import__("os").getcwd()'

    # test non-unicode (bytes)
    assert safe_eval(b'42') == 42

    # test non-string (list)
    assert safe_eval([1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-12 23:51:56.636586
# Unit test for function check_required_one_of
def test_check_required_one_of():
    def _test_check_required_one_of(test_args, expected):
        result = check_required_one_of(**test_args)
        assert result == expected


# Generated at 2022-06-12 23:52:07.468625
# Unit test for function check_type_float
def test_check_type_float():
    # Test different types of valid inputs
    assert check_type_float(1.0) == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float('1') == 1.0
    assert check_type_float('1.0') == 1.0
    assert check_type_float(b'1') == 1.0
    assert check_type_float(b'1.0') == 1.0
    assert check_type_float('1.1') == 1.1
    assert check_type_float(b'1.1') == 1.1
    # Test invalid inputs
    try:
        check_type_float('a')
    except TypeError:
        pass

# Generated at 2022-06-12 23:52:18.380131
# Unit test for function safe_eval
def test_safe_eval():
    """
    Function to test `safe_eval` function
    """
    # None types
    result = safe_eval(None)
    assert result is None

    # Integer types
    result = safe_eval(2)
    assert result == 2

    # Boolean types
    result = safe_eval(True)
    assert result is True

    result = safe_eval(False)
    assert result is False

    # String types
    result = safe_eval('"foo"')
    assert result == "foo"

    result = safe_eval('"foo"')
    assert result == "foo"

    # Unicode string types
    result = safe_eval(u'"foo"')
    assert result == "foo"

    result = safe_eval(u'"foo"')
    assert result == "foo"

    # Bytes types

# Generated at 2022-06-12 23:52:23.388064
# Unit test for function check_required_one_of
def test_check_required_one_of():
    d = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6
    }
    l = [
        ["a", "b","c"],
        ["d", "e", "f"],
    ]

    if count_terms(l, d) == 0:
        raise TypeError



# Generated at 2022-06-12 23:52:30.204186
# Unit test for function check_type_bits
def test_check_type_bits():
    """Unit test for function check_type_bits."""
    # 1 byte
    test_value = '1B'
    assert check_type_bits(test_value) == 1
    # 1 kilobyte
    test_value = '1Kb'
    assert check_type_bits(test_value) == 8192
    # 1 megabyte
    test_value = '1Mb'
    assert check_type_bits(test_value) == 8388608
    # 1 gigabyte
    test_value = '1Gb'
    assert check_type_bits(test_value) == 8589934592
    # 1 terabyte
    test_value = '1Tb'
    assert check_type_bits(test_value) == 8796093022208
    # 1 petabyte

# Generated at 2022-06-12 23:52:33.361613
# Unit test for function check_type_float
def test_check_type_float():
    val = check_type_float(5)
    assert val==5.0



# Generated at 2022-06-12 23:52:35.618740
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(6) == 6
    assert check_type_int('6') == 6
#---------------------------------------------------------------------------------------------------
# confirm function


# Generated at 2022-06-12 23:52:45.492412
# Unit test for function safe_eval
def test_safe_eval():
    # regexes could find things in comments too
    assert safe_eval('#import os\nTrue') is True
    assert safe_eval('#import os\nfalse', locals={'false': False}) is False
    assert safe_eval('#import os\ntrue and false', locals={'true': True, 'false': False}) is False
    assert safe_eval('#import os\ntrue or false', locals={'true': True, 'false': False}) is True
    assert safe_eval('#import os\n[True, False]') == [True, False]
    assert safe_eval('#import os\n(True, False)') == (True, False)
    assert safe_eval('#import os\n[True, 0]') == [True, 0]
    assert safe_eval('#import os\n(True, 0)')

# Generated at 2022-06-12 23:52:56.576714
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # Accepts None terms
    assert check_mutually_exclusive(None, None) is None

    # Fails when two terms are in parameters
    terms = [['foo', 'bar']]
    parameters = {'foo': True, 'bar': False}
    assert_raises_type_error(check_mutually_exclusive, terms, parameters)

    # Succeeds when one term is in parameters
    parameters = {'foo': True}
    assert check_mutually_exclusive(terms, parameters) is None

    # Multiple exclusive terms
    terms = [['foo', 'bar'], ['baz']]
    parameters = {'foo': True, 'bar': False, 'baz': True}
    assert_raises_type_error(check_mutually_exclusive, terms, parameters)

    parameters = {'foo': True}

# Generated at 2022-06-12 23:53:02.826881
# Unit test for function check_type_bits
def test_check_type_bits():
    test_val_1 = check_type_bits('1Mb')
    assert test_val_1 == 1048576
    test_val_2 = check_type_bits('1Kb')
    assert test_val_2 == 1024
    test_val_3 = check_type_bits('1Gb')
    assert test_val_3 == 1073741824
    test_val_4 = check_type_bits('1Tb')
    assert test_val_4 == 1099511627776
# Unit Test Ends Here



# Generated at 2022-06-12 23:53:12.061619
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int('3') == 3
    assert check_type_int(3) == 3
    assert check_type_int(3.0) == 3
    try:
        result = check_type_int('hello')
        raise AssertionError
    except TypeError:
        pass


# Generated at 2022-06-12 23:53:21.907462
# Unit test for function safe_eval
def test_safe_eval():
    assert literal_eval('1') == 1
    assert literal_eval('-1') == -1
    assert literal_eval('True') is True
    assert literal_eval('False') is False
    assert literal_eval('None') is None
    assert literal_eval('"hello"') == 'hello'
    assert literal_eval('[1,2,3]') == [1, 2, 3]
    assert literal_eval('(1,2,3)') == (1, 2, 3)
    assert literal_eval('1+1') == 1+1
    assert literal_eval('dict(one=1,two=2,three=3)') == {'one': 1, 'two': 2, 'three': 3}
    assert literal_eval('"hello".upper()') == 'HELLO'

# Generated at 2022-06-12 23:53:27.106195
# Unit test for function check_type_int
def test_check_type_int():
    assert(check_type_int(1)==1)
    assert(check_type_int("1")==1)
    try:
        assert(check_type_int("a")==1)
    except TypeError as e:
        pass
    try:
        assert(check_type_int("1a")==1)
    except TypeError as e:
        pass
    
    

# Generated at 2022-06-12 23:53:30.545414
# Unit test for function check_required_together
def test_check_required_together():
    input_parameters = {'a':1, 'b':2}
    required_together = [['a','b']]
    check_required_together(required_together, input_parameters)

    

# Generated at 2022-06-12 23:53:41.553736
# Unit test for function check_type_bytes
def test_check_type_bytes():
    bytes_list_succ = {
        '1 kB': 1024,
        '1kb': 1000,
        '1kb ': 1000,
        ' 1kb': 1000,
        '1 MB': 1000*1024,
        '1MB': 1000000,
        '1 mB': 1000*1024,
        '1mb': 1000000,
        '1gB': 1000*1000*1024,
        '1GB': 1000*1000*1000,
        '1 gb': 1000*1000*1000}
    for key in bytes_list_succ:
        assert check_type_bytes(key) == bytes_list_succ[key]

# Generated at 2022-06-12 23:53:49.274799
# Unit test for function safe_eval
def test_safe_eval():
    # Cannot use assertRaisesRegexp in py2
    assert not isinstance(safe_eval('{{foo.bar()}}'), string_types)
    assert not isinstance(safe_eval('import os'), string_types)
    assert safe_eval('"{{foo}}"', include_exceptions=True) == ('{{foo}}', None)
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('foo') == 'foo'
    assert safe_eval('[1,2]') == [1, 2]
    assert safe_eval('{1:2}') == {1: 2}
    assert safe_eval('(1,2)') == (1, 2)



# Generated at 2022-06-12 23:54:00.169809
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('100K') == 102400
    assert check_type_bytes('100k') == 102400
    assert check_type_bytes('100KB') == 102400
    assert check_type_bytes('100kb') == 102400
    assert check_type_bytes('100KiB') == 102400
    assert check_type_bytes('100kib') == 102400
    assert check_type_bytes('100Ki') == 102400
    assert check_type_bytes('100ki') == 102400
    assert check_type_bytes('100K') == 102400
    assert check_type_bytes('100k') == 102400
    assert check_type_bytes('100M') == 104857600
    assert check_type_bytes('100m') == 104857600
    assert check_type_bytes('100MB')

# Generated at 2022-06-12 23:54:08.457780
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    assert check_mutually_exclusive([['test1', 'test2'], ['test3', 'test4']], {'test1': 'hi', 'test3': 'hi'}) == []
    assert check_mutually_exclusive([['test1', 'test2'], ['test3', 'test4']], {'test1': 'hi', 'test3': 'hi', 'test4': 'hi'}) == [['test3', 'test4']]
    def test_check_mutually_exclusive_none():
        assert check_mutually_exclusive(None, {'test1': 'hi', 'test3': 'hi'}) == []



# Generated at 2022-06-12 23:54:17.253507
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('3') == 3
    assert safe_eval('foo') == 'foo'
    assert safe_eval('["foo", "bar"]') == ['foo', 'bar']
    assert safe_eval('{"foo": "bar"}') == {'foo': 'bar'}
    assert safe_eval('{"foo": {"bar": "baz"}}') == {'foo': {'bar': 'baz'}}
    assert safe_eval('foo.bar()') == 'foo.bar()'
    assert safe_eval('import foo') == 'import foo'



# Generated at 2022-06-12 23:54:25.121190
# Unit test for function check_required_together
def test_check_required_together():
    param_dict = {'a': 1, 'b': 2, 'c': 3}
    # normal behavior
    terms = [('a', 'b'), ('a', 'c')]
    assert check_required_together(terms, param_dict) == []
    terms = [('a', 'b', 'd')]
    assert check_required_together(terms, param_dict) == [['a', 'b', 'd']]
    # None returns empty list
    assert check_required_together(None, param_dict) == []
    # a empty list returns empty list
    terms = []
    assert check_required_together(terms, param_dict) == []
    # a non-list returns empty list
    terms = 'abc'
    assert check_required_together(terms, param_dict) == []



# Generated at 2022-06-12 23:54:31.212757
# Unit test for function check_type_bits
def test_check_type_bits():
    answer = check_type_bits('1Mb')
    assert answer == 1048576



# Generated at 2022-06-12 23:54:32.809849
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576


# Generated at 2022-06-12 23:54:35.934046
# Unit test for function check_required_together
def test_check_required_together():
    terms = [['a','b','c'],['d','e','f']]
    parameters = dict(a='exist',c='exist')
    r = check_required_together(terms, parameters)
    assert r == []


# Generated at 2022-06-12 23:54:46.133229
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}
    with pytest.raises(TypeError):
        check_mutually_exclusive(terms, parameters)

    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 'a', 'c': 'c', 'd': 'd', 'e': 'e'}
    check_mutually_exclusive(terms, parameters)

    terms = [['a', 'b'], ['c', 'd']]
    parameters = {}
    check_mutually_exclusive(terms, parameters)

    terms = [['a', 'b'], ['c', 'd']]
   

# Generated at 2022-06-12 23:54:55.250099
# Unit test for function check_required_arguments
def test_check_required_arguments():
  argument_spec = {
    'required': { 'required': True, 'type': 'list', 'default': [] },
    'optional': { 'required': False, 'type': 'list', 'default': [] }
  }
  parameters = {
    'optional': []
  }
  assert(check_required_arguments(argument_spec, parameters) == ['required'])

  parameters = {
    'required': [],
    'optional': []
  }
  assert(check_required_arguments(argument_spec, parameters) == [])



# Generated at 2022-06-12 23:54:59.076556
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(42) == 42
    assert check_type_int('42') == 42
    with pytest.raises(TypeError):
        check_type_int('42a')



# Generated at 2022-06-12 23:55:09.413160
# Unit test for function check_required_one_of
def test_check_required_one_of():
    t = [('a'), ('b', 'c')]
    p = {'a': 1}
    check_required_one_of(t, p)

    t = [('a'), ('b', 'c')]
    p = {'a': 1, 'b': 1}
    check_required_one_of(t, p)

    t = [('a'), ('b', 'c')]
    p = {'a': 1, 'd': 1}
    check_required_one_of(t, p)

    t = [('a'), ('b', 'c')]
    p = {'d': 1}
    check_required_one_of(t, p)

    t = [('a'), ('b', 'c')]
    p = {}
    check_required_one_of(t, p)

# Generated at 2022-06-12 23:55:16.171251
# Unit test for function check_required_arguments
def test_check_required_arguments():
    args = {'a': {'required': True}}
    # confirm missing required argument fails
    try:
        check_required_arguments(args, {})
    except TypeError:
        pass
    else:
        assert False

    # confirm missing optional argument does not fail
    args['b'] = {'required': False}
    check_required_arguments(args, {'a': None})



# Generated at 2022-06-12 23:55:28.066851
# Unit test for function check_required_if
def test_check_required_if():
    # Test all values required
    try:
        check_required_if([('state', 'present', ('path',), True)], {'path': ''})
    except TypeError as e:
        assert e.args[0] == 'state is present but at least one of the following are missing: path'
    else:
        assert False, "Expected TypeError"
    try:
        check_required_if([('state', 'present', ('path',), False)], {'path': ''})
    except TypeError as e:
        assert e.args[0] == 'state is present but all of the following are missing: path'
    else:
        assert False, "Expected TypeError"
    # Test with some values required

# Generated at 2022-06-12 23:55:38.072202
# Unit test for function check_required_together
def test_check_required_together():
    test_parameters = []
    test_parameters.append({'port':'80','proto':'http','server':'127.0.0.1'})
    test_parameters.append({'port':'80','proto':'http','username':'testuser'})
    test_parameters.append({'port':'80','proto':'http','password':'testpass'})
    test_parameters.append({'port':'80','proto':'http'})

    for test_parameter in test_parameters:
        error_msg = ''
        try:
            check_required_together([['port','proto','server'],['port','proto','password','username']],test_parameter)
        except TypeError as e:
            error_msg = str(e)
        assert error_msg

# Generated at 2022-06-12 23:55:49.857548
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """ Test basic functionality of check_mutually_exclusive """

    _check_mutually_exclusive = check_mutually_exclusive
    check_mutually_exclusive = lambda terms, parameters, options_context=None: _check_mutually_exclusive(terms, parameters)

    # Test expected behavior
    assert check_mutually_exclusive(None, {}) == []
    assert check_mutually_exclusive([['a', 'b']], {}) == []
    assert check_mutually_exclusive([['a', 'b']], {'a': 1}) == []
    assert check_mutually_exclusive([['a', 'b']], {'a': 1, 'b': 1}) == [('a', 'b')]
    assert check_mutually_exclusive([['a', 'b']], {'a': 1, 'b': 1, 'c': 2})

# Generated at 2022-06-12 23:55:53.398664
# Unit test for function check_required_one_of
def test_check_required_one_of():
    try:
        result = check_required_one_of([['bar', 'baz']], {'foo': 'bar'})
        assert False
    except TypeError as e:
        assert 'one of the following is required' in str(e)



# Generated at 2022-06-12 23:56:05.507263
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(9.9) == 9.9
    assert check_type_float(9) == 9.0
    assert check_type_float('9.9') == 9.9
    assert check_type_float('9') == 9.0
    assert check_type_float(b'9.9') == 9.9
    assert check_type_float(b'9') == 9.0
    assert check_type_float(b'9.9a') == 9.9
    assert check_type_float(bytearray(b'9.9')) == 9.9
    assert check_type_float(bytearray(b'9')) == 9.0
    assert check_type_float(bytearray(b'9.9a')) == 9.9

# Generated at 2022-06-12 23:56:14.481265
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1.0) == 1.0
    assert check_type_float(1) == 1.0
    assert check_type_float('1.0') == 1.0
    assert check_type_float(b'1.0') == 1.0
    with pytest.raises(TypeError):
        check_type_float(None) == 1.0
    with pytest.raises(TypeError):
        check_type_float(dict()) == 1.0
    with pytest.raises(TypeError):
        check_type_float(list()) == 1.0
    with pytest.raises(TypeError):
        check_type_float(set()) == 1.0
    with pytest.raises(TypeError):
        check_type_float((1,)) == 1.0


# Generated at 2022-06-12 23:56:24.201440
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """
    Verify test_check_mutually_exclusive function
    """
    parameters = {'test': 'value', 'test2': 'value2'}
    result = check_mutually_exclusive([['test', 'test2']], parameters)
    assert result == []

    try:
        parameters = {'test': 'value', 'test2': 'value2', 'test3': 'value3'}
        result = check_mutually_exclusive([['test', 'test2'], ['test2', 'test3']], parameters)
        assert False
    except TypeError:
        assert True

    result = check_mutually_exclusive([['test', 'test2']], parameters, ['parameters'])
    assert result == []


# Generated at 2022-06-12 23:56:34.472273
# Unit test for function safe_eval
def test_safe_eval():
    result, __ = safe_eval("{'a':'b'}", include_exceptions=True)
    assert isinstance(result, dict)
    a = safe_eval('a')
    assert isinstance(a, str)
    b = safe_eval('{"a":"b"}')
    assert isinstance(b, dict)
    c = safe_eval('b')
    assert isinstance(c, str)
    d = safe_eval('isinstance')
    assert isinstance(d, str)
    f, __ = safe_eval('isinstance(', include_exceptions=True)
    assert isinstance(f, str)
    g, __ = safe_eval('import sys', include_exceptions=True)
    assert isinstance(g, str)

# Generated at 2022-06-12 23:56:36.576820
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1') == 1



# Generated at 2022-06-12 23:56:44.582220
# Unit test for function check_required_by
def test_check_required_by():
    result = check_required_by({'key1': ['required1']},{'key1':1})
    assert isinstance(result, dict)
    assert len(result) == 0
    result = check_required_by({'key1': ['required1']},{'key1':1, 'required1':2})
    assert isinstance(result, dict)
    assert len(result) == 0
    try:
        check_required_by({'key1': ['required1']},{'key1':1, 'required2':2})
    except TypeError as e:
        assert e == "missing parameter(s) required by 'key1': required1"

# Generated at 2022-06-12 23:56:48.277223
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    with pytest.raises(TypeError):
        check_type_bits('1M')
    with pytest.raises(TypeError):
        check_type_bits('1Gb')


# Generated at 2022-06-12 23:56:51.853056
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Mb').__class__.__name__ == 'int'


# Generated at 2022-06-12 23:57:04.736401
# Unit test for function check_required_together

# Generated at 2022-06-12 23:57:15.693388
# Unit test for function check_required_by
def test_check_required_by():
    parameters = dict(
        one=1,
        two=2,
        three=3,
        four=4,
    )

    # Testing string_types
    requirements = dict(
        one='three'
    )
    assert check_required_by(requirements, parameters) == {}
    parameters['three'] = None
    assert check_required_by(requirements, parameters) == {'one': ['three']}
    parameters.pop('three')
    assert check_required_by(requirements, parameters) == {'one': ['three']}
    parameters['one'] = None
    assert check_required_by(requirements, parameters) == {}

    # Testing list
    requirements = dict(
        one=['three']
    )
    assert check_required_by(requirements, parameters) == {}
    parameters['three']

# Generated at 2022-06-12 23:57:20.695559
# Unit test for function check_required_together
def test_check_required_together():
    from ansible.module_utils.common.validation import check_required_together
    assert not check_required_together([['a', 'b']], dict(a='a'))
    assert not check_required_together([['a', 'b']], dict(a='a', b='b'))
    assert check_required_together([['a', 'b']], dict(a='a', c='c'))
    assert not check_required_together([['a', 'b'], ['c', 'd']], dict(a='a', d='d'))



# Generated at 2022-06-12 23:57:22.330231
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1.5Mb') == 1572864



# Generated at 2022-06-12 23:57:28.346249
# Unit test for function check_type_float
def test_check_type_float():
    for value, expected in (
        ('1', 1.0),
        (1, 1.0),
        ('1.0', 1.0),
        (1.0, 1.0),
        ('1.0a', 1.0),
        ('a1.0', 1.0),
        ('1,0', 1.0),
        ('1.0a', 1.0),
        (u'1.0', 1.0),
        (b'1.0', 1.0),
    ):
        assert check_type_float(value) == expected



# Generated at 2022-06-12 23:57:39.362645
# Unit test for function check_required_together
def test_check_required_together():
    assert check_required_together([('a', 'b'), ('c', 'd')], {'e': 'foo'}, ['state']) == []
    assert check_required_together([('a', 'b'), ('c', 'd')], {'a': 'foo'}, ['state']) == [['c', 'd']]
    assert check_required_together([('a', 'b'), ('c', 'd')], {'a': 'foo', 'c': 'bar'}) == []
    assert check_required_together([('a', 'b'), ('c', 'd')], {'a': 'foo', 'e': 'bar'}) == [['c', 'd']]

# Generated at 2022-06-12 23:57:44.105245
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1k') == 1024
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1m') == 1048576
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1g') == 1073741824
    assert check_type_bytes('1G') == 1073741824
    assert check_type_bytes('1t') == 1099511627776
    assert check_type_bytes('1T') == 1099511627776


# Generated at 2022-06-12 23:57:46.556117
# Unit test for function check_required_together
def test_check_required_together():
    check_required_together([['a', 'b'], ['c', 'd']], {'a': 1, 'b': True})



# Generated at 2022-06-12 23:57:54.626786
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    from ansible.module_utils.common.validation import check_mutually_exclusive
    from ansible.module_utils.common.text.formatters import human_to_bytes
    import pytest
    parameters = dict()
    parameters['one'] = True
    parameters['two'] = True
    parameters['three'] = True
    parameters['four'] = True
    terms = [['one', 'two'], ['three', 'four']]
    with pytest.raises(TypeError) as execinfo:
        check_mutually_exclusive(terms, parameters)
    assert to_native(execinfo.value) == "parameters are mutually exclusive: one|two found in three -> four"
test_check_mutually_exclusive()


# Generated at 2022-06-12 23:58:07.454678
# Unit test for function check_type_float
def test_check_type_float():
    assert (isinstance(check_type_float("5"), float))
    assert (isinstance(check_type_float("5.5"), float))
    assert (isinstance(check_type_float("5.5e-5"), float))
    assert (isinstance(check_type_float(5), float))
    assert (isinstance(check_type_float(5.5), float))
    assert (isinstance(check_type_float(5.5e-5), float))
    assert (isinstance(check_type_float(b"5"), float))
    assert (isinstance(check_type_float(b"5.5"), float))
    assert (isinstance(check_type_float(b"5.5e-5"), float))
    assert (check_type_float(5) == 5.0)

# Generated at 2022-06-12 23:58:21.328210
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('2Ki') == 2048
    assert check_type_bytes('1.5KiB') == 1536
    assert check_type_bytes('') == 0
    assert check_type_bytes(None) == 0
    assert check_type_bytes(42) == 42
    assert check_type_bytes(42.42) == 42.42

    with pytest.raises(TypeError):
        check_type_bytes([])
    with pytest.raises(TypeError):
        check_type_bytes({})
    with pytest.raises(ValueError):
        check_type_bytes('42.42.42')

# TODO: handle tuple, bytes, and other types

# Generated at 2022-06-12 23:58:25.852458
# Unit test for function check_type_bytes
def test_check_type_bytes():
    test_values = {
        100: 100,
        '100': 100,
        '100m': 100 * 1024 * 1024,
        '100M': 100 * 1024 * 1024,
        '100mb': 100 * 1024 * 1024,
        '100MB': 100 * 1024 * 1024,
        '100MiB': 100 * 1024 * 1024,
    }
    for value, result in test_values.items():
        assert check_type_bytes(value) == result


# Generated at 2022-06-12 23:58:35.559976
# Unit test for function check_type_int
def test_check_type_int():
    test_cases = (
        (1, 1),
        ('123', 123),
        ('123abc', TypeError),
        (2**64, TypeError),
        )
    for input, expected in test_cases:
        try:
            output = check_type_int(input)
            if expected == TypeError:
                raise Exception("Expected TypeError for %s, but did not get one" % input)
            elif output != expected:
                raise Exception("Expected %s, got %s" % (expected, output))
        except TypeError:
            if expected != TypeError:
                raise Exception("Expected %s, got TypeError" % expected)



# Generated at 2022-06-12 23:58:39.628358
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1MB') == 8388608
    assert check_type_bits('1MBIT') == 8388608
    assert check_type_bits('1Mbit') == 8388608
    assert check_type_bits('1MBITS') == 8388608
    assert check_type_bits('1Mbits') == 8388608

