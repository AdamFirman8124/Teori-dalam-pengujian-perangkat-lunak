

# Generated at 2022-06-12 23:49:29.521162
# Unit test for function check_type_bytes
def test_check_type_bytes():
    test_inputs = [
        ("10", 10),
        ("10G", 10737418240),
        ("0.1G", 107374182.4),
        ("10t", 10737418240),
        ("0.1t", 107374182.4),
        ("10Ti", 10737418240),
        ("0.1Ti", 107374182.4),
    ]

    for value, expected_result in test_inputs:
        result = check_type_bytes(value)
        assert result == expected_result
    with pytest.raises(TypeError) as ex:
        check_type_bytes(None)
    assert "cannot be converted to a Byte value" in str(ex.value)



# Generated at 2022-06-12 23:49:33.379734
# Unit test for function check_type_int
def test_check_type_int():
    from kongming.utils.module_docs_fragments import check_type_int
    assert check_type_int(1) == 1
    assert check_type_int("1") == 1
    try:
        check_type_int("a")
    except TypeError:
        pass
    else:
        assert False


# Generated at 2022-06-12 23:49:43.806840
# Unit test for function check_required_together
def test_check_required_together():
    parameters = dict(state='present',
                      name='test1',
                      vlan_id='10',
                      description='test description'
                      )
    specs = dict(required_together=[[['state', 'name'], ['vlan_id', 'description']]])
    check_required_together(specs.get('required_together'), parameters, options_context=[])

    parameters = dict(state='present',
                      name='test1',
                      )
    specs = dict(required_together=[[['state', 'name'], ['vlan_id', 'description']]])
    check_required_together(specs.get('required_together'), parameters, options_context=[])

    parameters = dict(state='present',
                      name='test1',
                      vlan_id='10',
                      description='test description'
                      )
   

# Generated at 2022-06-12 23:49:53.937873
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {
        'state': 'present',
        'someint': 99
    }
    assert check_required_if(requirements, parameters) == []

    requirements = [
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {
        'someint': 99
    }
    try:
        check_required_if(requirements, parameters)
        assert False
    except TypeError as e:
        assert str(e) == 'state is present but any of the following are missing: path'


# Generated at 2022-06-12 23:50:05.226788
# Unit test for function check_type_dict

# Generated at 2022-06-12 23:50:17.236986
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    terms = [['param1', 'param2'], ['param3', 'param4']]
    parameters = {'param2': 1, 'param3': 2, 'param4': 3}
    assert(check_mutually_exclusive(terms, parameters) == [])
    parameters = {'param1': 1, 'param4': 3}
    assert(check_mutually_exclusive(terms, parameters) == [])
    parameters = {'param1': 1, 'param2': 2, 'param4': 3}
    try:
        check_mutually_exclusive(terms, parameters)
        assert(check_mutually_exclusive(terms, parameters))
    except TypeError as e:
        new_e = "parameters are mutually exclusive: param1|param2, param3|param4"
        assert(str(e) == new_e)

# Generated at 2022-06-12 23:50:26.115632
# Unit test for function check_required_by
def test_check_required_by():
    check_required_by(requirements={'foo': ['bar', 'baz']}, parameters={'foo': 'foo'})
    try:
        check_required_by(requirements={'foo': ['bar', 'baz']}, parameters={'foo': 'foo', 'bar': None})
    except TypeError:
        pass
    else:
        assert False, "Should have caught a TypeError"

    try:
        check_required_by(requirements={'foo': ['bar', 'baz']}, parameters={'foo': 'foo', 'baz': None})
    except TypeError:
        pass
    else:
        assert False, "Should have caught a TypeError"



# Generated at 2022-06-12 23:50:32.370975
# Unit test for function check_required_arguments
def test_check_required_arguments():
    parameters = dict()
    argument_spec = dict()
    expected = []
    assert check_required_arguments(argument_spec, parameters) == expected
    argument_spec = dict(a=dict(required=True))
    expected = ['a']
    assert check_required_arguments(argument_spec, parameters) == expected
    parameters = dict(a=3)
    expected = []



# Generated at 2022-06-12 23:50:42.576186
# Unit test for function check_type_dict
def test_check_type_dict():
    test = check_type_dict(dict(a=1, b=2))
    print(test) # {'a': 1, 'b': 2}
    test = check_type_dict(json.dumps(dict(a=1, b=2)))
    print(test) # {'a': 1, 'b': 2}
    test = check_type_dict('a=1, b=2')
    print(test) # {'a': '1', 'b': '2'}
    test = check_type_dict('{"a":1, "b":2}')
    print(test) # {'a': 1, 'b': 2}
    test = check_type_dict('{"a":1, "b":2}')
    print(test) # {'a': 1, 'b': 2}
   

# Generated at 2022-06-12 23:50:47.470300
# Unit test for function check_required_together
def test_check_required_together():
    params = dict(
        state='present',
        name='resource',
        want_value='overridden_value_1',
        default_value='default_value_1',
    )
    required_together = [
        ['want_value', 'default_value'],
    ]
    assert check_required_together(
        terms=required_together,
        parameters=params,
    ) == [] 



# Generated at 2022-06-12 23:51:09.308921
# Unit test for function safe_eval
def test_safe_eval():
    val, ex = safe_eval('"%d"' % (2**64), include_exceptions=True)
    assert val == (2**64)
    assert ex is None
    val, ex = safe_eval('"%d"' % (2**128), include_exceptions=True)
    assert val == '"%d"' % (2**128)
    assert isinstance(ex, OverflowError)
    val, ex = safe_eval('%d' % -(2**128), include_exceptions=True)
    assert val == -(2**128)
    assert ex is None
    val, ex = safe_eval('%d' % -(2**256), include_exceptions=True)
    assert val == '%d' % -(2**256)
    assert isinstance(ex, OverflowError)
    val

# Generated at 2022-06-12 23:51:12.627416
# Unit test for function check_required_arguments
def test_check_required_arguments():
    required_argument_spec = dict(
        test_parameter=dict(required=True),
        test_parameter_false=dict(required=False)
    )
    parameters = dict()
    missing_args = check_required_arguments(required_argument_spec, parameters)

    assert missing_args == ['test_parameter']



# Generated at 2022-06-12 23:51:22.648375
# Unit test for function safe_eval

# Generated at 2022-06-12 23:51:31.242911
# Unit test for function safe_eval
def test_safe_eval():
    # check that safe_eval returns valid result
    assert safe_eval('{}') == {}
    assert safe_eval('2') == 2
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('(1, 2, 3)') == (1, 2, 3)
    assert safe_eval('[1, 2, (3,)]') == [1, 2, (3,)]
    # check that safe_eval returns safe error string
    assert safe_eval('[1, 2, (3]') == "[1, 2, (3]"

# Generated at 2022-06-12 23:51:41.869059
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('10') == 10
    assert safe_eval('-1') == -1
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 + 1.0') == 2.0
    assert safe_eval('1.2 + 1.4') == 2.6
    assert safe_eval('1.2 + 1') == 2.2
    assert safe_eval('"xyz"') == 'xyz'
    assert safe_eval('"x" + "y"') == 'xy'
    assert safe_eval('u"x" + "y"') == 'xy'
    assert safe_eval('u"x" + u"y"') == 'xy'
    assert safe_eval('b"x" + "y"') == b'xy'

# Generated at 2022-06-12 23:51:53.632637
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    """Unit test for function check_mutually_exclusive"""

    check_terms = [['a', 'b'], ['c', 'd', 'e']]
    # parameters matching first list of terms
    parameters = {'a': 1, 'b': 2}
    try:
        check_mutually_exclusive(check_terms, parameters)
    except TypeError as ex:
        assert "mutually exclusive" in str(ex)
        assert "a|b" in str(ex)
    else:
        assert False, "check_mutually_exclusive with first set of terms should have failed"

    # parameters not matching any list of terms
    parameters = {'g': 1, 'h': 2}
    check_mutually_exclusive(check_terms, parameters)
    parameters = {'a': 1, 'c': 2}
    check_mut

# Generated at 2022-06-12 23:52:04.181039
# Unit test for function check_required_arguments
def test_check_required_arguments():
    # One required argument is not present in parameters
    result = check_required_arguments({'required_argument':{'required': True}}, {})
    assert result == ['required_argument']

    # All required arguments are present in parameters
    result = check_required_arguments({'required_argument':{'required': True}}, {'required_argument': None})
    assert result == []

    # Additional arguments are present in parameters
    result = check_required_arguments({'required_argument':{'required': True}}, {'required_argument': None, 'additional': None})
    assert result == []

    # No argument is present in parameters
    result = check_required_arguments({'required_argument':{'required': True}}, {})
    assert result == ['required_argument']


# Generated at 2022-06-12 23:52:08.224060
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    terms = [["a", "b"], ["c", "d"]]
    parameters = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    assert check_mutually_exclusive(terms, parameters) == [["a", "b"], ["c", "d"]]



# Generated at 2022-06-12 23:52:19.002733
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes(b'1') == 1
    assert check_type_bytes('1') == 1
    assert check_type_bytes('1m') == 1048576
    assert check_type_bytes('1Mi') == 1048576
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1MiB') == 1048576
    assert check_type_bytes('1G') == 1073741824
    assert check_type_bytes('1GB') == 1073741824
    assert check_type_bytes('1GBi') == 1073741824
    assert check_type_bytes('1Gi') == 1073741824
    assert check_type_bytes('1GiB') == 1073741824
    assert check_type_bytes('1T') == 1099511627776
   

# Generated at 2022-06-12 23:52:28.278332
# Unit test for function check_required_if
def test_check_required_if():
    requirements = [['key_1', 'val_1', ('req_1',), True], ['key_2', 'val_2', ('req_2',)] ]
    parameters = {}
    options_context = None
    empty_results = check_required_if(requirements, parameters, options_context)
    assert len(empty_results) == 0

    parameters = {'key_1': 'val_1', 'req_1': None}
    empty_results = check_required_if(requirements, parameters, options_context)
    assert len(empty_results) == 0

    parameters = {'key_1': 'val_1'}
    results = check_required_if(requirements, parameters, options_context)
    assert len(results) == 1
    assert results[0]['parameter'] == 'key_1'


# Generated at 2022-06-12 23:52:34.217134
# Unit test for function check_type_bits
def test_check_type_bits():
    assert human_to_bytes("1Mb", isbits=True) == 1024 * 1024 * 8



# Generated at 2022-06-12 23:52:44.529218
# Unit test for function safe_eval
def test_safe_eval():
    failed_cases = [
        u'import os',
        u'os.name',
        u'hash(1)',
        u'open'
        u'open()'
        u'chr(1)',
        u'eval()',
        u'__import__',
        u'__import__("os")',
        u'type(""',
        u'""+"',
    ]
    for failed_case in failed_cases:
        assert safe_eval(failed_case) == failed_case


# Generated at 2022-06-12 23:52:53.395927
# Unit test for function check_required_together
def test_check_required_together():
    assert check_required_together(
        [('state', 'name')], {"state": "present", "name": "test"}) == []
    # If a required parameter is missing, it should return a list with the
    # tuple (terms)
    assert check_required_together(
        [('state', 'name')], {"state": "present"}) == [('state', 'name')]
    # If all required parameters are missing, it should return a list with
    # the tuple (terms)
    assert check_required_together(
        [('state', 'name')], {}) == [('state', 'name')]



# Generated at 2022-06-12 23:52:57.564781
# Unit test for function check_type_bytes
def test_check_type_bytes():
    # test with an integer
    assert check_type_bytes(1048576) == 1048576
    # test with an invalid input type
    with pytest.raises(TypeError):
        check_type_bytes(['test'])
    # test with a valid input type
    assert check_type_bytes("1m") == 1048576



# Generated at 2022-06-12 23:53:01.830337
# Unit test for function check_type_int
def test_check_type_int():
    assert check_type_int(1) == 1
    assert check_type_int('1') == 1
    assert check_type_int(u'1') == 1
    assert check_type_int('-1') == -1
    assert check_type_int(u'-1') == -1
    assert check_type_int(' foo ') == 0
    assert check_type_int(None) == 0



# Generated at 2022-06-12 23:53:06.625656
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
    assert check_type_bytes('1p') == 1125899906842624
    assert check_type_bytes('1P') == 1125899906842624
    assert check_type_bytes('1e') == 1152921504606846976

# Generated at 2022-06-12 23:53:10.837014
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1Gb') == 1073741824
# End of unit test for function check_type_bits



# Generated at 2022-06-12 23:53:16.225764
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1b') == 1
    assert check_type_bits('1.5Mb') == 1572864
    assert check_type_bits('10Gb') == 10737418240
    assert check_type_bits('10') == 10



# Generated at 2022-06-12 23:53:25.077916
# Unit test for function check_type_dict
def test_check_type_dict():
    check_type_dict({'a':'a'})

    try:
        check_type_dict("a=b,c=d")
    except Exception as e:
        raise Exception("unexpected failure: string dict conversion: %s" % to_native(e))

    try:
        check_type_dict("{'a':'b','c':'d'}")
    except Exception as e:
        raise Exception("unexpected failure: string dict conversion: %s" % to_native(e))

    try:
        check_type_dict("{a:'b',c:'d'}")
    except Exception as e:
        raise Exception("unexpected failure: string dict conversion: %s" % to_native(e))



# Generated at 2022-06-12 23:53:28.857693
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    try:
        check_mutually_exclusive([['a', 'b'], ['c', 'd']], dict(a=1, b=1, c=1, d=1))
    except Exception as e:
        assert to_native(e) == "parameters are mutually exclusive: a|b, c|d"
        return None
    raise Exception("This block should have failed")



# Generated at 2022-06-12 23:53:38.761463
# Unit test for function check_required_together
def test_check_required_together():
    for i in range (4):
        parameters = {}
        for j in range (4):
            parameters[f'a{j}'] = 'temp'
        terms = [['a1', 'a2', 'a3'], ['a0', 'a1', 'a2', 'a3']]
        parameters[f'a{i}'] = None
        check_required_together(terms, parameters)



# Generated at 2022-06-12 23:53:46.074958
# Unit test for function check_type_bits
def test_check_type_bits():
    print(check_type_bits('1Mb'))
    print(check_type_bits('1MB'))
    print(check_type_bits('2Mb'))
    print(check_type_bits('1Gb'))
    print(check_type_bits('1GB'))
    print(check_type_bits('2Gb'))
    print(check_type_bits('1M'))
    print(check_type_bits('1G'))
    print(check_type_bits('1000000b'))
    print(check_type_bits('1000000B'))
#test_check_type_bits()


# Generated at 2022-06-12 23:53:52.128856
# Unit test for function check_required_by
def test_check_required_by():
    # The is the error that is returned when the requirements check is not passed
    error_msg = "missing parameter(s) required by 'something_extra': something_required"  # noqa

    # Test when a requirement is not met
    requirements = {'something_extra': 'something_required'}
    parameters = {'something_extra': 'foo'}
    try:
        result = check_required_by(requirements, parameters)
    except TypeError as err:
        assert to_native(err) == error_msg

    # Test when a requirement is met
    requirements = {'something_extra': 'something_required'}
    parameters = {'something_extra': 'foo', 'something_required': 'bar'}
    assert check_required_by(requirements, parameters) == {}

    # Test when a requirement is met with another requirement


# Generated at 2022-06-12 23:53:58.575955
# Unit test for function safe_eval
def test_safe_eval():
    """Provide validation for all code paths in safe_eval()."""
    assert safe_eval("False", include_exceptions=True) == (False, None)
    assert safe_eval("not_a_bool") == "not_a_bool"
    assert safe_eval("True and False") == "True and False"
    assert safe_eval("import os") == "import os"
    assert safe_eval("dict(a=True)") == "dict(a=True)"



# Generated at 2022-06-12 23:54:08.639870
# Unit test for function check_required_if
def test_check_required_if():
    # Test parameters [is_one_of(any of these), requirement]
    # requirement failure: missing all
    r1 = [('s1', 's1', ('s2', 's3'), False)]
    result = check_required_if(r1, {'s1': 's1'})
    assert len(result) == 1
    assert result[0]['requires'] == 'all'
    assert result[0]['parameter'] == 's1'
    assert result[0]['value'] == 's1'
    assert set(result[0]['requirements']) == set(('s2', 's3'))
    assert set(result[0]['missing']) == set(('s2', 's3'))
    # requirement success: missing any

# Generated at 2022-06-12 23:54:20.274679
# Unit test for function check_type_int
def test_check_type_int():
    ints = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000, 10000000000000000, 100000000000000000, 1000000000000000000, 10000000000000000000, 100000000000000000000, 1000000000000000000000, 10000000000000000000000, 100000000000000000000000, 1000000000000000000000000, 10000000000000000000000000, 100000000000000000000000000, 1000000000000000000000000000, 10000000000000000000000000000, 100000000000000000000000000000]

# Generated at 2022-06-12 23:54:32.258162
# Unit test for function check_type_bytes
def test_check_type_bytes():
    ''' Unit test for function check_type_bytes '''
    fail_values = ['100D', '100d', '100m', '-1m', 'S0']
    for value in fail_values:
        try:
            check_type_bytes(value)
        except TypeError:
            pass
        else:
            raise AssertionError("check_type_bytes failed to raise exception for invalid input")

    pass_values = [('1', 1), ('10b', 10), ('10KB', 10240), ('10KiB', 10240), ('10M', 10485760),
                   ('10MiB', 10485760), ('10G', 10737418240), ('10GiB', 10737418240)]
    for value, value_result in pass_values:
        assert check_type_bytes(value) == value_

# Generated at 2022-06-12 23:54:39.942060
# Unit test for function check_type_bytes
def test_check_type_bytes():
    test_invalid_code = ['aB', '1g', '0B', '1020b', '10KB', '-10GB', '-10By', '1XX', '10GB10HB']
    for test_code in test_invalid_code:
        try:
            human_to_bytes(test_code)
        except ValueError:
            pass
        else:
            raise TypeError('%s cannot be converted to a Byte value' % test_code)

    test_valid_code = ['0B', '1B', '10MB', '10mb', '10GB', '10KiB', '10MiB', '10GiB', '10TiB']
    for test_code in test_valid_code:
        human_to_bytes(test_code)



# Generated at 2022-06-12 23:54:48.471186
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    # Test for all positive cases
    positive_test = [
        ([['a','b'], ['c','d']], {'a':'X', 'c':'Y'}),
        ([['a','b'], ['c','d']], {'a':'X', 'd':'Y'}),
    ]
    for test in positive_test:
        check_mutually_exclusive(test[0], test[1])
    # Test for negative cases

# Generated at 2022-06-12 23:55:00.736393
# Unit test for function check_required_by
def test_check_required_by():
    requirements = {
        'a': ['b'],
        'c': ['d']
    }
    # success case
    parameters = {
        'a': 'value for a',
        'b': 'value for b',
        'c': 'value for c',
        'd': 'value for d'
    }
    assert check_required_by(requirements, parameters) == {}
    # failure case: missing parameter
    parameters = {
        'a': 'value for a',
        'b': None,
        'c': 'value for c',
        'd': 'value for d'
    }
    try:
        assert check_required_by(requirements, parameters)
        assert False
    except TypeError:
        assert True
    # failure case: missing parameter key

# Generated at 2022-06-12 23:55:07.551153
# Unit test for function check_type_int
def test_check_type_int():
    assert 1 == check_type_int(1)
    assert 1 == check_type_int('1')
    try:
        check_type_int(True)
        assert False
    except TypeError:
        assert True



# Generated at 2022-06-12 23:55:15.182638
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo") == 'foo'
    assert safe_eval("[1,2,3]") == [1,2,3]
    assert safe_eval("{'a': 1, 'b': 2}") == {'a': 1, 'b': 2}
    assert safe_eval("bar.update(baz)") == "bar.update(baz)"
    assert safe_eval("import os") == "import os"



# Generated at 2022-06-12 23:55:23.686595
# Unit test for function check_required_by
def test_check_required_by():
    # Test passing
    requirements = {'option_one': ['option_two'], 'option_two': None}
    parameters = {'option_one': 'present', 'option_two': 'present'}
    check_required_by(requirements, parameters)
    # Test failing
    requirements = {'option_one': ['option_two'], 'option_two': None}
    parameters = {'option_one': 'present', 'option_two': None}
    try:
        check_required_by(requirements, parameters)
    except TypeError:
        pass
    else:
        assert False, "check_required_by did not raise TypeError when it should have"



# Generated at 2022-06-12 23:55:30.971146
# Unit test for function check_mutually_exclusive
def test_check_mutually_exclusive():
    parameters = {'a': 1, 'b': 2}
    '''
    parameters = {'a': 1, 'b': 2, 'c' : {'d' : 3, 'e': 4}}
    '''
    terms = [['a', 'b']]
    '''
    terms = [['a', 'b'], ['c.d', 'c.e']]
    '''
    raise TypeError(check_mutually_exclusive(terms, parameters))


# Generated at 2022-06-12 23:55:40.006798
# Unit test for function safe_eval
def test_safe_eval():
# testing return of int
    a = safe_eval('1')
    assert isinstance(a, int)
    assert (a==1)

# testing return of float
    a = safe_eval('1.5')
    assert isinstance(a, float)
    assert (a==1.5)

#testing return of dict
    a = safe_eval('{"key":"value"}')
    assert isinstance(a, dict)
    assert (a == {"key":"value"})

#testing return of list
    a = safe_eval('["value1","value2"]')
    assert isinstance(a, list)
    assert (a == ['value1','value2'])

#testing return of boolean
    a = safe_eval('True')
    assert isinstance(a, bool)
    assert (a == True)



# Generated at 2022-06-12 23:55:46.489277
# Unit test for function check_required_if
def test_check_required_if():
    import pytest
    # check if at least one of the requirements is present
    requirements = [['state', 'present', (('path', 'port'),), True]]
    parameters = {'state': 'present', 'port': '80'}
    try:
        check_required_if(requirements, parameters)
    except TypeError as e:
        pytest.fail("Got unexpected exception {0}, expected no exception".format(e))
    requirements = [['state', 'present', (('path', 'port'),), True]]
    parameters = {'state': 'present', 'port': '80', 'path': 'path/to/file'}
    try:
        check_required_if(requirements, parameters)
    except TypeError as e:
        pytest.fail("Got unexpected exception {0}, expected no exception".format(e))
   

# Generated at 2022-06-12 23:55:51.160985
# Unit test for function safe_eval
def test_safe_eval():
    value = 'foo'
    result = safe_eval(value)
    assert result == value
    value = 'bar'
    result = safe_eval(value)
    assert result == value



# Generated at 2022-06-12 23:56:03.561756
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('0')==0
    assert check_type_bits('1')==1
    assert check_type_bits('10')==10
    assert check_type_bits('1Kb')==1024
    assert check_type_bits('1MB')==1048576
    assert check_type_bits('1GB')==1073741824
    assert check_type_bits('1TB')==1099511627776
    assert check_type_bits('1000TB')==1099511627776000
    assert check_type_bits('1K')==1000
    assert check_type_bits('1M')==1000000
    assert check_type_bits('1G')==1000000000
    assert check_type_bits('1T')==1000000000000
    assert check_type_bits('1000T')==100000000

# Generated at 2022-06-12 23:56:12.992075
# Unit test for function check_type_bytes
def test_check_type_bytes():
    #Test using valid input
    assert check_type_bytes("10B") == 10
    assert check_type_bytes("10KiB") == 10 * 1024
    assert check_type_bytes("10MiB") == 10 * 1024 * 1024
    assert check_type_bytes("10GiB") == 10 * 1024 * 1024 * 1024
    assert check_type_bytes("10TiB") == 10 * 1024 * 1024 * 1024 * 1024
    assert check_type_bytes("10KB") == 10 * 1000
    assert check_type_bytes("10MB") == 10 * 1000 * 1000
    assert check_type_bytes("10GB") == 10 * 1000 * 1000 * 1000
    assert check_type_bytes("10TB") == 10 * 1000 * 1000 * 1000 * 1000
    assert check_type_bytes("10") == 10

# Generated at 2022-06-12 23:56:19.241488
# Unit test for function check_type_bits
def test_check_type_bits():
    bits1 = check_type_bits('1Mb')
    bits2 = check_type_bits('1 Mb')
    expected = 1048576
    if bits1 == expected and bits2 == expected:
        print("check_type_bits is Ok.")
    else:
        print("check_type_bits is Failed.")



# Generated at 2022-06-12 23:56:33.601562
# Unit test for function check_required_arguments
def test_check_required_arguments():
    argument_spec = dict(
        required_arg_1=dict(required=True, type='str'),
        required_arg_2=dict(required=True, type='str'),
        required_arg_3=dict(required=True, type='str')
    )
    params = dict(required_arg_2='This is arg2')
    missing = []
    missing = check_required_arguments(argument_spec, params)
    assert missing == ['required_arg_1', 'required_arg_3'], "check_required_arguments returned incorrect missing arguments - expected ['required_arg_1', 'required_arg_3'] got: %s" % missing
    params = dict(required_arg_1='This is arg1', required_arg_2='This is arg2', required_arg_3='This is arg3')
    missing

# Generated at 2022-06-12 23:56:38.308462
# Unit test for function check_type_int
def test_check_type_int():
    if check_type_int('3') != 3:
        print("")
        print("check_type_int: test #1 failed")
        print("Expected: 3")
        print("Returned: ", check_type_int('3'))
        raise Exception('check_type_int test #1 failed')
# Test 1 end


# Generated at 2022-06-12 23:56:43.591988
# Unit test for function safe_eval
def test_safe_eval():
    my_value = "{{ 10 }}"
    my_result = safe_eval(my_value)
    assert my_result == 10

    my_value = "{{ 10 }}{{ 20 }}"
    my_result = safe_eval(my_value)
    assert my_result == "1020"

    my_value = "{% raw %}{{ 10 }}{% endraw %}"
    my_result = safe_eval(my_value)
    assert my_result == "{% raw %}{{ 10 }}{% endraw %}"



# Generated at 2022-06-12 23:56:46.916768
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('a.b(c)') == 'a.b(c)'
    assert safe_eval('import os', include_exceptions=True) == ('import os', None)



# Generated at 2022-06-12 23:56:52.570002
# Unit test for function check_type_int
def test_check_type_int():
    assert isinstance(check_type_int(1), int)
    assert isinstance(check_type_int('1'), int)
    raises(TypeError, check_type_int, 1.0)
    raises(TypeError, check_type_int, [])
    raises(TypeError, check_type_int, {})


# Generated at 2022-06-12 23:56:57.759568
# Unit test for function check_required_arguments
def test_check_required_arguments():
    """
    Test check_required_arguments function
    """
    assert_equal(
        check_required_arguments({'test_arg': {'required': True}}, {}),
        ['test_arg'],
    )
    assert_equal(
        check_required_arguments({'test_arg': {'required': True}}, {}, ['test_arg']),
        ['test_arg']
    )



# Generated at 2022-06-12 23:57:04.267064
# Unit test for function safe_eval
def test_safe_eval():

    import os
    import tempfile

    not_expected = "foo"
    expected = "bar"

    # what about using the tempfile module and tempfile.mkstemp?
    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.write("%s" % expected)
    tf.close()

    # test for safe eval
    value, exc = safe_eval("'%s'" % expected, include_exceptions=True)
    assert value == expected
    assert exc is None

    # test for safe eval to not overwrite
    value2, exc = safe_eval("'%s'" % not_expected, include_exceptions=True)
    value = safe_eval("'%s'" % expected)
    assert value == expected
    assert exc is None

    # test for safe eval to not overwrite with dict
    value

# Generated at 2022-06-12 23:57:15.346793
# Unit test for function check_type_bytes
def test_check_type_bytes():
    # Check ValueError is correctly captured by the function
    value = "12"
    try:
        unit_test = check_type_bytes(value)
        raise AssertionError("ValueError expected but not risen")
    except TypeError:
        pass
    assert unit_test is None
    # Check TypeError is correctly risen when value is not a string
    value = 12
    try:
        unit_test = check_type_bytes(value)
        raise AssertionError("TypeError expected but not risen")
    except TypeError:
        pass
    assert unit_test is None
    # Check correct conversion in GB
    value = "10GB"
    expected = 10 * 1024 * 1024 * 1024
    unit_test = check_type_bytes(value)
    assert unit_test == expected
    # Check correct conversion in GiB
    value

# Generated at 2022-06-12 23:57:18.471466
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1M') == 1048576
    assert check_type_bytes('1024') == 1024
    assert check_type_bytes('1K') == 1024
    assert check_type_bytes('1048576') == 1048576
    return True


# Generated at 2022-06-12 23:57:22.151739
# Unit test for function check_type_float
def test_check_type_float():
    assert check_type_float(1) == 1
    assert check_type_float(1.1) == 1.1
    assert check_type_float('1') == 1
    assert check_type_float('1.1') == 1.1
    assert check_type_float(b'1') == 1
    assert check_type_float(b'1.1') == 1.1



# Generated at 2022-06-12 23:57:26.452067
# Unit test for function check_type_bytes
def test_check_type_bytes():
    value = check_type_bytes('2kb')
    assert value == 2048



# Generated at 2022-06-12 23:57:35.890326
# Unit test for function safe_eval
def test_safe_eval():
    expr = "{{ 1 | bool }}"
    result, err = safe_eval(expr, include_exceptions=True)
    assert result == "{{ 1 | bool }}"
    assert err is None
    result = safe_eval(expr)
    assert result == "{{ 1 | bool }}"
    expr = "{{ foo.bar() }}"
    result, err = safe_eval(expr, include_exceptions=True)
    assert result == "{{ foo.bar() }}"
    assert err is None
    result = safe_eval(expr)
    assert result == "{{ foo.bar() }}"



# Generated at 2022-06-12 23:57:43.568379
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("{{some_var}}") == "{{some_var}}"
    assert safe_eval("some_var") == "some_var"
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('dict(baz="qux")') == {"baz": "qux"}
    assert safe_eval('1 + 1') == 2
    assert safe_eval('-2') == -2
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('') == ''
    assert safe_eval('""') == ''

# Generated at 2022-06-12 23:57:50.956678
# Unit test for function check_type_bits
def test_check_type_bits():
    assert 1048576 == check_type_bits('1Mb')
    assert 8388608 == check_type_bits('8Mb')
    assert 3758096384 == check_type_bits('35.5Gb')
    assert 4398046511104 == check_type_bits('40Tb')
    assert 4.398046511104e+14 == check_type_bits('40tb')
    assert 10151527168 == check_type_bits('9.5Gb')
    assert 1019286719488 == check_type_bits('94.5Tb')


# Generated at 2022-06-12 23:57:54.809943
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert b'10B' == check_type_bytes('10B')
    assert b'10KB' == check_type_bytes('10KB')
    assert b'10MB' == check_type_bytes('10MB')
    assert b'10GB' == check_type_bytes('10GB')
    assert b'10TB' == check_type_bytes('10TB')


# FIXME: The param and prefix parameters here are coming from AnsibleModule._check_type_string()
#        which is using those for the warning messaged based on string conversion warning settings.
#        Not sure how to deal with that here since we don't have config state to query.

# Generated at 2022-06-12 23:58:00.685116
# Unit test for function check_type_bits
def test_check_type_bits():
    assert check_type_bits('100') == 100
    assert check_type_bits('1Mb') == 1048576
    assert check_type_bits('1 b') == 1
    assert check_type_bits('10mB') == 10485760
    assert check_type_bits('1.5Mb') == 1572864



# Generated at 2022-06-12 23:58:08.829408
# Unit test for function check_type_bytes
def test_check_type_bytes():
    assert check_type_bytes('1 k') == 1024
    assert check_type_bytes('1 kB') == 1000
    assert check_type_bytes('1 mB') == 1000000
    assert check_type_bytes('1 gB') == 1000000000
    assert check_type_bytes('1 tB') == 1000000000000
    assert check_type_bytes(1000000) == 1000000
    try:
        check_type_bytes(1024)
        assert False, 'Bytes value should be in string format'
    except TypeError:
        pass


# Generated at 2022-06-12 23:58:19.425508
# Unit test for function check_required_together
def test_check_required_together():
    parameters = {'force': None, 'value1': 'True', 'value2': 'True'}
    terms = [['force', 'value1'], ['force', 'value2']]
    options_context = None
    results = []
    
    for term in terms:
        counts = [count_terms(field, parameters) for field in term]
        non_zero = [c for c in counts if c > 0]
        if len(non_zero) > 0:
            if 0 in counts:
                results.append(term)
    if results:
        for term in results:
            msg = "parameters are required together: %s" % ', '.join(term)
            if options_context:
                msg = "{0} found in {1}".format(msg, " -> ".join(options_context))
            raise TypeError

# Generated at 2022-06-12 23:58:23.273058
# Unit test for function check_required_arguments
def test_check_required_arguments():
    try:
        valid_parameters = {'required_key':'foo'}
        argument_spec = {'required_key':{'required':True}}
        missing = check_required_arguments(argument_spec, valid_parameters)
        assert len(missing) == 0
    except TypeError:
        assert False


# Generated at 2022-06-12 23:58:34.234564
# Unit test for function safe_eval
def test_safe_eval():
    import pytest

    x = 3
    y = 4

    with pytest.raises(ValueError):
        safe_eval('import foo')

    with pytest.raises(SyntaxError):
        safe_eval('__builtins__')

    with pytest.raises(SyntaxError):
        safe_eval('foo(1)')

    # test safe_eval does not blow up with a list
    assert safe_eval(['1']) == ['1']

    # test safe_eval does not blow up with dict
    assert safe_eval('{"hello": "world"}') == {'hello': 'world'}

    # test safe_eval will resolve locals
    assert safe_eval('x', {'x': 3}) == 3

    # test safe_eval will resolve locals with a list