

# Generated at 2022-06-12 23:28:43.324428
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST_PASS_THROUGH'] = '12345'
    assert env_fallback('TEST_PASS_THROUGH') == '12345'
    del os.environ['TEST_PASS_THROUGH']
    raises(AnsibleFallbackNotFound, env_fallback, 'TEST_FAIL_THROUGH')


# Generated at 2022-06-12 23:28:52.049536
# Unit test for function env_fallback
def test_env_fallback():
    env = os.environ.copy()
    # Test with no environment variables set
    assert env_fallback('FOO') == AnsibleFallbackNotFound
    # Test with one environment variable set
    env['FOO'] = 'test1'
    os.environ = env
    assert env_fallback('FOO') == 'test1'
    # Test with all environment variables set
    env['FOO'] = 'test2'
    env['BAR'] = 'test3'
    os.environ = env
    assert env_fallback('FOO', 'BAR') == 'test2'
    # Test with no environment variables set
    env = {}
    os.environ = env
    assert env_fallback('BAR') == AnsibleFallbackNotFound



# Generated at 2022-06-12 23:29:03.235412
# Unit test for function set_fallbacks
def test_set_fallbacks():
    src1 = dict(
        a=dict(type='str', fallback=('env', 'ANSIBLE_A', 'FOO_A')),
        b=dict(type='dict', options=dict(
            c=dict(type='int'),
        )),
    )
    tgt1 = dict()
    tgt1expected = dict(a='x')
    os.environ['ANSIBLE_A'] = 'x'
    assert set_fallbacks(src1, tgt1) == set()
    assert tgt1 == tgt1expected


# Generated at 2022-06-12 23:29:11.765063
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # No fallback
    argument_spec = {'foo': {'type': 'str', 'required': True}}
    parameters = {'foo': 'bar'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'foo': 'bar'}
    assert not no_log_values

    # Fallback and sensitive param (no_log=True)
    def fallback():
        return 'password'

    argument_spec = {'password': {'type': 'str', 'no_log': True, 'fallback': (fallback,)}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'password': 'password'}
    assert 'password' in no_log_values

    # Fallback with additional args
   

# Generated at 2022-06-12 23:29:18.499179
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({"param1": {"type": "str", "fallback": ("env_fallback", ["param1"])}}, {"param1": None}) == set()
    param = dict({})
    fallback_value = set_fallbacks(
        {"param1": {"type": "str", "fallback": ("env_fallback", ["param1"])}},
        param
    )
    assert param['param1'] == fallback_value
    assert fallback_value == os.environ['param1']



# Generated at 2022-06-12 23:29:24.982008
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        test_param=dict(fallback=(env_fallback, ('ENV_FALLBACK',))),
        test_param2=dict(fallback=(env_fallback, ('ENV_FALLBACK',), dict(default='default'))),
        test_param_no_log=dict(fallback=(env_fallback, ('ENV_FALLBACK',)), no_log=True)
    )
    parameters = dict()
    os.environ['ENV_FALLBACK'] = 'from_env'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 1
    assert 'from_env' in no_log_values
    assert 'test_param' in parameters
    assert 'test_param2' in parameters


# Generated at 2022-06-12 23:29:35.477389
# Unit test for function set_fallbacks
def test_set_fallbacks():

    # Test with a simple fallback, valid
    result = dict()
    spec = dict(
        a=dict(type='str', fallback=(env_fallback, 'ANSIBLE_TEST_A'))
    )
    os.environ['ANSIBLE_TEST_A'] = 'foo'
    assert set_fallbacks(spec, result) == set()
    assert result['a'] == 'foo'
    del os.environ['ANSIBLE_TEST_A']

    # Test with a simple fallback, invalid
    result = dict()
    spec = dict(
        a=dict(type='str', fallback=(env_fallback, 'ANSIBLE_TEST_A'))
    )
    assert set_fallbacks(spec, result) == set()
    assert 'a' not in result

    # Test with a simple

# Generated at 2022-06-12 23:29:36.536282
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('HOME') == '/Users/username'


# Generated at 2022-06-12 23:29:46.425761
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'param1': {'type': 'str', 'fallback': (env_fallback, ['env_param1'])},
        'param2': {'type': 'str', 'fallback': (env_fallback, ['env_param2'])},
        'param3': {'type': 'str', 'fallback': (env_fallback, ['env_param3'])},
        'param4': {'type': 'str', 'fallback': (env_fallback, ['env_param4'])},
    }
    parameters = {
        'param1': 'value1',
        'param3': 'value3',
    }
    os.environ['env_param2'] = 'value2'
    os.environ['env_param4'] = 'value4'
    no_

# Generated at 2022-06-12 23:29:53.290717
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'test': {'fallback': (env_fallback, ['test'])}}, {}) == set()
    assert set_fallbacks({'test': {'fallback': (env_fallback, ['test'])}}, {'test': 'foo'}) == set(['foo'])
    os.environ['test'] = 'foo'
    assert set_fallbacks({'test': {'fallback': (env_fallback, ['test'])}}, {}) == set(['foo'])



# Generated at 2022-06-12 23:30:18.910708
# Unit test for function env_fallback
def test_env_fallback():
    try:
        env_fallback('NON_EXISTING_VARIABLE')
        assert False
    except AnsibleFallbackNotFound:
        assert True



# Generated at 2022-06-12 23:30:25.110809
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'a': dict(type='str', fallback=(env_fallback, 'A'))}, {}) == {'a'}
    assert set_fallbacks({'a': dict(type='str', fallback=(env_fallback, 'A'))}, {}) == {'a'}
    assert set_fallbacks({'a': dict(type='str', fallback=(env_fallback, 'A'))}, {}) == {'a'}



# Generated at 2022-06-12 23:30:35.589894
# Unit test for function set_fallbacks
def test_set_fallbacks():
    module_args = dict()
    spec = dict(
        s3_bucket=dict(type='str', fallback=('env_fallback', ['S3_BUCKET'])),
        s3_prefix=dict(type='str', fallback=('env_fallback', ['S3_PREFIX'])),
    )
    for var in ['S3_BUCKET', 'S3_PREFIX']:
        assert var not in module_args
        os.environ[var] = var
    assert set_fallbacks(spec, module_args) == set()
    assert module_args['s3_bucket'] == 'S3_BUCKET'
    assert module_args['s3_prefix'] == 'S3_PREFIX'
    assert set_fallbacks(spec, module_args) == set

# Generated at 2022-06-12 23:30:41.909494
# Unit test for function env_fallback
def test_env_fallback():
    os.unsetenv('a')
    os.unsetenv('b')
    assert env_fallback('a', 'b') == 'a'
    os.environ['a'] = 'c'
    assert env_fallback('a', 'b') == 'c'
    os.environ['b'] = 'd'
    assert env_fallback('a', 'b') == 'd'
# end of test_env_fallback


# Generated at 2022-06-12 23:30:49.303575
# Unit test for function remove_values
def test_remove_values():
    # Make sure we don't remove keys
    mapping = {'a': 'A'}
    no_log_strings = ['A']
    new_value = remove_values(mapping, no_log_strings)
    assert isinstance(new_value, Mapping)

    mapping = {'a': 'B'}
    new_value = remove_values(mapping, no_log_strings)
    assert new_value == mapping

    # Make sure we remove keys
    mapping = {'a': 'A'}
    no_log_strings = ['a']
    new_value = remove_values(mapping, no_log_strings)
    assert isinstance(new_value, Mapping)
    assert 'a' not in new_value


# Generated at 2022-06-12 23:30:53.148253
# Unit test for function env_fallback
def test_env_fallback():
    # Test with no env var
    try:
        env_fallback('ANSIBLE_TEST_NO_ENV_VAR_1')
        assert False, "Should have thrown AnsibleFallbackNotFound"
    except AnsibleFallbackNotFound:
        pass

    # Test with env var
    os.environ['ANSIBLE_TEST_ENV_VAR_1'] = 'VALUE_1'
    assert 'VALUE_1' == env_fallback('ANSIBLE_TEST_ENV_VAR_1')



# Generated at 2022-06-12 23:31:00.847584
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """
    Test for function sanitize_keys.
    """
    no_log_values = {'top_secret', 'password'}
    ignore_values = {'ansible_password'}

    # Test a simple dict
    result = sanitize_keys({'my_pass': 'top_secret', 'top_secret': 'top_secret', 'ansible_password': 'password'}, no_log_values, ignore_values)
    assert result == {'my_pass': 'top_secret', 'top_secret': 'top_secret', 'ansible_password': 'password'}

    # Test a nested dict
    result = sanitize_keys({'top_secret': 'top_secret', 'nested': {'ansible_password': 'password'}}, no_log_values, ignore_values)

# Generated at 2022-06-12 23:31:03.073075
# Unit test for function sanitize_keys
def test_sanitize_keys():
    mydict = {'user': {'token': 'quietly'}, 'password': 'secret'}
    result = sanitize_keys(mydict, ('secret', 'token'))
    assert result == {'user': {'***': 'quietly'}, '******': 'secret'}


# Generated at 2022-06-12 23:31:11.899545
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'test_param': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST_VALUE')}}
    parameters = {}
    os.environ['ANSIBLE_TEST_VALUE'] = 'test_value'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert(parameters['test_param'] == 'test_value')
    assert(no_log_values == set())
    os.unsetenv('ANSIBLE_TEST_VALUE')
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert(parameters['test_param'] == None)
    assert(no_log_values == set())


# Generated at 2022-06-12 23:31:19.849456
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'param1': {'fallback': (env_fallback, 'FOO')}}, {}) == set()
    assert set_fallbacks({'param1': {'fallback': (env_fallback, 'FOO')}}, {'param1': 'spam'}) == set()
    os.environ['FOO'] = 'eggs'
    assert set_fallbacks({'param1': {'fallback': (env_fallback, 'FOO')}}, {}) == {'eggs'}
    del os.environ['FOO']
    assert set_fallbacks({'param1': {'fallback': (env_fallback, 'FOO')}}, {}) == set()



# Generated at 2022-06-12 23:31:47.615721
# Unit test for function env_fallback
def test_env_fallback():
    test_data = {
        "good_data": ["FOO", "FOO", "OK"],
        "bad_data": ["BAR", "BAR"],
    }
    # Test passing in a valid environment variable
    os.environ["FOO"] = "OK"
    assert env_fallback(*test_data["good_data"]) == "OK"
    # Test passing in an invalid environment variable
    assert env_fallback(*test_data["bad_data"]) == "BAR"



# Generated at 2022-06-12 23:31:58.709875
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(a=dict(type='int', fallback=(lambda: 1)),
                         b=dict(type='str', fallback=(env_fallback, 'b_env')),
                         c=dict(type='str', fallback=(env_fallback, 'c_env')),
                         d=dict(type='bool', fallback=(lambda: False)),
                         e=dict(type='dict', fallback=(lambda: dict(f=1))),
                         g=dict(type='list', fallback=(env_fallback, 'g_env')))
    parameters = dict()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert set(parameters.keys()) == set(['a', 'b', 'd', 'e'])
    assert 'c' not in parameters

# Generated at 2022-06-12 23:32:00.737967
# Unit test for function set_fallbacks
def test_set_fallbacks():
    mod_spec = {'param': {'type': 'str', 'fallback': (env_fallback, 'FOO'), 'default': 'bar'}}
    expected = {'param': 'bar'}
    assert expected == set_fallbacks(mod_spec, {})



# Generated at 2022-06-12 23:32:13.108428
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = dict(
        foo=dict(
            type='str',
            required=False,
            fallback=(env_fallback, ['FOO'])
        ),
        bar=dict(
            type='str',
            required=True,
            fallback=(env_fallback, ['BAR'])
        ),
        baz=dict(
            type='str',
            required=True,
            fallback=(env_fallback, ['BAZ'])
        )
    )
    env = dict(
        FOO='FOO_VALUE',
        BAR='BAR_VALUE'
    )
    parameters = dict()

    os.environ = env
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()

    # Only 'foo' and

# Generated at 2022-06-12 23:32:20.110666
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback function."""
    os.environ['TESTENV'] = "foobar"
    os.environ['TESTENV2'] = "barfoo"
    assert env_fallback("TESTENV") == "foobar"
    assert env_fallback("TESTENV", "TESTENV2") == "foobar"
    assert env_fallback("TESTENV", "TWOTESTENV") == "foobar"
    assert env_fallback("TWOTESTENV") == "barfoo"
    assert env_fallback("TWOTESTENV", "TESTENV") == "barfoo"

    # Verify exception is raised for not found

# Generated at 2022-06-12 23:32:25.348347
# Unit test for function set_fallbacks
def test_set_fallbacks():

    from collections import OrderedDict
    from ansible.module_utils.basic import env_fallback

    argument_spec = OrderedDict()
    argument_spec['option1'] = {'type': 'str', 'default': 'default_value'}
    argument_spec['option2'] = {'type': 'str', 'default': 'default_value', 'fallback': (env_fallback, ['option_env'])}
    argument_spec['option3'] = {'type': 'str', 'default': 'default_value', 'fallback': (env_fallback, ['option_env'])}
    argument_spec['option4'] = {'type': 'str', 'default': 'default_value', 'fallback': (env_fallback, ['option_env'])}

# Generated at 2022-06-12 23:32:37.953748
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Testing param = None, value = None
    params = {}
    expected = {}
    my_args = ["FALLBACK_ARG_1", "FALLBACK_ARG_2"]
    my_kwargs = {"FALLBACK_KWARG_1": "FOO", "FALLBACK_KWARG_2": "BAR"}
    my_function = MagicMock(return_value=my_kwargs)
    fallback_value = (my_function, my_args, my_kwargs)
    my_spec = {'param': {'type': 'dict', 'fallback': fallback_value}}
    my_no_log = set_fallbacks(my_spec, params)
    assert expected == params
    assert my_no_log == set()
    my_function.assert_not_called()

   

# Generated at 2022-06-12 23:32:49.369980
# Unit test for function sanitize_keys
def test_sanitize_keys():
    # test_sanitize_keys_empty
    data = None
    no_log_strings = set()

    new_data = sanitize_keys(data, no_log_strings)
    assert new_data == data

    # test_sanitize_keys_string
    data = 'ansible'
    no_log_strings = set()

    new_data = sanitize_keys(data, no_log_strings)
    assert new_data == data

    # test_sanitize_keys_simple
    data = {
        'foo': 'bar'
    }
    no_log_strings = set()

    new_data = sanitize_keys(data, no_log_strings)
    assert new_data == data

    # test_sanitize_keys_simple_single_no_log
    data

# Generated at 2022-06-12 23:32:59.760573
# Unit test for function env_fallback
def test_env_fallback():
    """Verify env_fallback functionality
    :returns: Pass/Fail
    :rtype: boolean
    """
    import os
    import stat

    os.environ['DEFAULT_NODE'] = '11.22.33.44'
    os.environ['DEFAULT_PORT'] = '22'

    data = [
        {'name': 'node', 'required': True, 'env': ['DEFAULT_NODE'], 'fallback': env_fallback},
        {'name': 'port', 'required': True, 'env': ['DEFAULT_PORT'], 'fallback': env_fallback},
    ]

    parameters = {'node': None, 'port': None}

    no_log_values = set_fallbacks(data, parameters)


# Generated at 2022-06-12 23:33:10.495763
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test with fallbacks
    argument_spec = {
        'parameter': {'type': 'str', 'fallback': (env_fallback, 'ENVVAR')},
        'parameter_with_args': {'type': 'str', 'fallback': (os.path.expanduser, '~/')},
        'parameter_with_default': {'type': 'str', 'fallback': (env_fallback, {'other_parameter': 'value'})},
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['parameter'] == os.environ['ENVVAR']
    assert parameters['parameter_with_args'] == os.path.expanduser('~/')

# Generated at 2022-06-12 23:33:44.323615
# Unit test for function remove_values
def test_remove_values():

    str_value = 'string value'
    assert str_value == remove_values(str_value, [])
    assert str_value == remove_values(str_value, ['string'])
    assert '******* value' == remove_values(str_value, ['string '])
    assert '***********' == remove_values(str_value, ['string', 'value'])

    int_value = 123456
    assert int_value == remove_values(int_value, [])
    assert int_value == remove_values(int_value, ['1', '3', '5'])
    assert '*******' == remove_values(int_value, ['1', '3', '5', '2', '4', '6'])

    bool_value = True
    assert bool_value == remove_values(bool_value, [])


# Generated at 2022-06-12 23:33:51.828339
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """sanitize_keys() is a helper function which is used in AnsibleModule to sanitize ``no_log`` values.
    """

# Generated at 2022-06-12 23:34:03.303388
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'a': {'type': 'str', 'fallback': (env_fallback, 'a'), 'no_log': True} }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'a': os.environ['a'] }
    assert no_log_values == set(parameters['a'])

    argument_spec = {'b': {'type': 'str', 'fallback': (env_fallback, 'b'), 'no_log': False} }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'b': os.environ['b'] }
    assert not no_log_values


# Generated at 2022-06-12 23:34:08.740878
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:34:16.360634
# Unit test for function sanitize_keys
def test_sanitize_keys():
    a = {'a': 'A', 'aA': 'AA'}
    b = {'a': 'A', 'aa': 'AA'}
    assert sanitize_keys(a, ['A']) == b
    c = {'a': 'A', 'aA': {'a': 'A', 'aA': 'AA'}, 'aAa': [{'a': 'A', 'aA': 'AA'}]}
    d = {'a': 'A', 'aa': {'a': 'A', 'aa': 'AA'}, 'aaa': [{'a': 'A', 'aa': 'AA'}]}
    assert sanitize_keys(c, ['A']) == d


# Generated at 2022-06-12 23:34:17.785190
# Unit test for function env_fallback
def test_env_fallback():
    with patch.dict('os.environ', {'ANSIBLE_TEST': 'from environment'}, clear=True):
        assert env_fallback('ANSIBLE_TEST') == 'from environment'



# Generated at 2022-06-12 23:34:28.279958
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:34:34.468465
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = {
        'test1': dict(fallback=(env_fallback, ['test1_env'])),
        'test2': dict(fallback=(env_fallback, ['test2_env'])),
        'test3': dict(fallback=(env_fallback, ['test3_env'])),
        'test4': dict(fallback=(env_fallback, ['test4_env'])),
        'test5': dict(fallback=(env_fallback, ['test5_env'])),
    }
    parameters = {
        'test1': 'foo',
        'test3': 'bar',
        'test5': 'foobar',
    }
    no_log_values = set()
    os.environ['test1_env'] = 'foo_env'
    os.environ

# Generated at 2022-06-12 23:34:40.289418
# Unit test for function env_fallback
def test_env_fallback():
    os.environ.clear()
    os.environ['ANSIBLE_TEST_1'] = '1'
    os.environ['ANSIBLE_TEST_2'] = '2'
    assert env_fallback('ANSIBLE_TEST_1') == '1'
    assert env_fallback('ANSIBLE_TEST_2') == '2'
    assert_raises(AnsibleFallbackNotFound, env_fallback, 'ANSIBLE_TEST_3')



# Generated at 2022-06-12 23:34:41.625320
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys({'a': 'b', 'password': 'foo'}, ['foo']) == {'a': 'b', '********': 'foo'}



# Generated at 2022-06-12 23:35:08.556809
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_FOO'] = 'foo'
    os.environ['ANSIBLE_BAR'] = 'bar'
    assert env_fallback('ANSIBLE_FOO') == 'foo'
    assert env_fallback('ANSIBLE_BAR') == 'bar'
    assert_raises(AnsibleFallbackNotFound, env_fallback, 'ANSIBLE_BAZ')
    os.environ.pop('ANSIBLE_FOO')
    os.environ.pop('ANSIBLE_BAR')



# Generated at 2022-06-12 23:35:18.402343
# Unit test for function remove_values
def test_remove_values():
    assert remove_values('test', ['test']) == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    assert remove_values([1, 2, 'test', 4], ['test']) == [1, 2, 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 4]
    assert remove_values({'a': 1, 'b': [1, 2, 'test', 4], 'c': 'test'}, ['test']) == {'a': 1, 'b': [1, 2, 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 4], 'c': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'}



# Generated at 2022-06-12 23:35:29.879996
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_value = "test"
    # Test for fallback_strategy with fallback_args
    argument_spec = {'fallback_test':{'type':'str', 'fallback': (env_fallback, test_value)}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert test_value in parameters.values()

    # Test for fallback_strategy without fallback_args
    argument_spec = {'param1':{'type':'str', 'fallback': (env_fallback, )}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert test_value in parameters.values()

# Generated at 2022-06-12 23:35:35.839201
# Unit test for function env_fallback
def test_env_fallback():
    environ = {'ANSIBLE_TEST_VAR': 'foo'}
    with patch.dict('os.environ', environ):
        assert env_fallback('ANSIBLE_TEST_VAR') == 'foo'
        assert env_fallback('ANSIBLE_TEST_VAR_2') == 'UNDEFINED'
        try:
            env_fallback('ANSIBLE_TEST_VAR_2') == 'UNDEFINED'
        except AnsibleFallbackNotFound as e:
            pass
        else:
            assert False



# Generated at 2022-06-12 23:35:44.927066
# Unit test for function set_fallbacks
def test_set_fallbacks():
    sample_spec = dict(a=dict(default='foo'), b=dict(fallback=(env_fallback, "ANSIBLE_TEST_B")))
    sample_env = {"ANSIBLE_TEST_B": "bar"}
    sample_parameters = dict(b=None)
    with patch.dict('os.environ', sample_env):
        assert set_fallbacks(sample_spec, sample_parameters) == set()
    assert sample_parameters.get("a") == "foo"
    assert sample_parameters.get("b") == "bar"
    assert set_fallbacks(sample_spec, sample_parameters) == set()



# Generated at 2022-06-12 23:35:52.307732
# Unit test for function set_fallbacks
def test_set_fallbacks():
    if os.environ.get('TEST_FALLBACKS'):
        test_tuple = (env_fallback, 'TEST_FALLBACKS')

        argument_spec = {'param1': dict(fallback=test_tuple), 'param2': dict(fallback=(env_fallback, 'TEST_FALLBACKS', dict(my_kwarg='my_kwarg')))}
        parameters = {}

        no_log_values = set_fallbacks(argument_spec, parameters)
        assert parameters['param1'] == parameters['param2'] == os.environ['TEST_FALLBACKS']
        assert no_log_values == set()

# Generated at 2022-06-12 23:36:02.503792
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:36:04.516155
# Unit test for function env_fallback
def test_env_fallback():
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback()



# Generated at 2022-06-12 23:36:11.214109
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(type='str', fallback=('hello',)),
        bar=dict(type='str', fallback=(env_fallback, 'BAR')),
        baz=dict(type='str', fallback=(env_fallback, 'BAZ', 'default')),
    )
    parameters = {'foo': 'bye'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'foo': 'bye', 'bar': 'BAR', 'baz': 'default'}
    assert no_log_values == set()



# Generated at 2022-06-12 23:36:21.880750
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_FOO'] = 'bar'
    assert env_fallback('ANSIBLE_TEST_FOO') == 'bar'
    assert env_fallback('ANSIBLE_TEST_FOO', 'ANSIBLE_TEST_BAR') == 'bar'
    os.environ['ANSIBLE_TEST_BAR'] = 'baz'
    assert env_fallback('ANSIBLE_TEST_FOO', 'ANSIBLE_TEST_BAR') == 'bar'
    assert env_fallback('ANSIBLE_TEST_BAR', 'ANSIBLE_TEST_FOO') == 'baz'
    os.environ.pop('ANSIBLE_TEST_BAR', None)
    os.environ.pop('ANSIBLE_TEST_FOO', None)

# Generated at 2022-06-12 23:37:09.723616
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        a=dict(type='int', fallback=(None,)),
        b=dict(type='int', fallback=(None, [2, 3])),
        c=dict(type='int', fallback=(env_fallback, ['a', 'A'])),
        d=dict(type='int', fallback=(env_fallback, ['a', 'B'])),
        e=dict(type='list'),
        f=dict(type='list', fallback=(None, [])),
        )
    parameters = dict(e=[1], f=[2])
    os.environ['A'] = '1'

    test_no_log_values = set_fallbacks(argument_spec, parameters)
    assert test_no_log_values == set()

# Generated at 2022-06-12 23:37:20.604754
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys({u'user:password': u'john:p@ssw0rd'}, {u'p@ssw0rd'}) == {u'user:password': u'john:******'}
    assert sanitize_keys({u'user:password': u'john:p@ssw0rd'}, {u'p@ssw0rd'}, ignore_keys={u'password'}) == {u'user:password': u'john:p@ssw0rd'}
    assert sanitize_keys({u'user:password': u'john:p@ssw0rd'}, {u'p@ssw0rd'}, ignore_keys={u':password'}) == {u'user:******': u'john:p@ssw0rd'}



# Generated at 2022-06-12 23:37:26.223304
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = dict(a="foo")
    spec = dict(a=dict())
    spec['a'].update(dict(type='str', fallback=(env_fallback, ['ANSIBLE_FOO'])))
    assert set_fallbacks(spec, params) == set()

    params = dict()
    spec = dict(a=dict())
    spec['a'].update(dict(type='str', fallback=(env_fallback, ['ANSIBLE_FOO'])))
    assert set_fallbacks(spec, params) == set()

# Generated at 2022-06-12 23:37:28.034841
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('FOO') == os.environ['FOO']



# Generated at 2022-06-12 23:37:39.224495
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test set_fallbacks"""
