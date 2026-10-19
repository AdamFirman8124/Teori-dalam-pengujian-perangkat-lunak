

# Generated at 2022-06-12 23:28:24.867961
# Unit test for function set_fallbacks
def test_set_fallbacks():

    parameters = {'name': 'foo'}
    argument_spec = {
        'name': {'required': True, 'type': 'str'},
        'password': {'required': True, 'type': 'str', 'no_log': True},
        'logging': {'type': 'bool', 'default': False},
        'port': {'type': 'int', 'default': 80, 'fallback': (env_fallback, ['ANSIBLE_NET_PORT'])}
    }

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert parameters['logging'] is False
    assert parameters['port'] == 80
    assert set(no_log_values) == set()

    os.environ['ANSIBLE_NET_PORT'] = '443'
    no_log_values = set_fall

# Generated at 2022-06-12 23:28:35.271175
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:28:36.823674
# Unit test for function env_fallback
def test_env_fallback():
    '''Return value from environment varible if set'''
    assert env_fallback('PATH')


# Generated at 2022-06-12 23:28:43.817874
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({}, {}) == set()

    # No fallback
    params = {}
    args = {'foo': {}}
    assert set_fallbacks(args, params) == set()
    assert params == {}

    # Fallback found
    params = {}
    args = {'foo': {'fallback': ('env_fallback', 'bar')}}
    os.environ['bar'] = 'foo'
    assert set_fallbacks(args, params) == set()
    assert params == {'foo': 'foo'}

    # Fallback no_log
    params = {}
    args = {'foo': {'fallback': ('env_fallback', 'bar'), 'no_log': True}}
    os.environ['bar'] = 'foo'

# Generated at 2022-06-12 23:28:52.628781
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = {}
    argument_spec = {'version':{'type':'str', 'default':'2'}, 'username':{'type':'str', 'default':None, 'fallback':(env_fallback, ['ANSIBLE_NET_USERNAME'])}}
    no_log_values = set()
    for param, value in argument_spec.items():
        fallback = value.get('fallback', (None,))
        fallback_strategy = fallback[0]
        fallback_args = []
        fallback_kwargs = {}
        if param not in parameters and fallback_strategy is not None:
            for item in fallback[1:]:
                if isinstance(item, dict):
                    fallback_kwargs = item
                else:
                    fallback_args = item

# Generated at 2022-06-12 23:28:57.974745
# Unit test for function env_fallback
def test_env_fallback():
    # Test that AnsibleFallbackNotFound is raised
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback()
    # Test that env_fallback can find a value
    return_value = env_fallback('LANG')
    assert isinstance(return_value, string_types)



# Generated at 2022-06-12 23:29:04.798664
# Unit test for function set_fallbacks
def test_set_fallbacks():
    module_argument_spec = {
        'argument': {'type': 'int', 'fallback': (env_fallback, ['ANSIBLE_ARGUMENT_NAME'])},
    }
    parameters = set_fallbacks(module_argument_spec, {})
    assert isinstance(parameters, set)

    os.environ['ANSIBLE_ARGUMENT_NAME'] = '10'
    parameters = set_fallbacks(module_argument_spec, {})
    assert isinstance(parameters, set)



# Generated at 2022-06-12 23:29:12.798895
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:29:21.438029
# Unit test for function set_fallbacks
def test_set_fallbacks():
    import os
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.facts.system.base import SystemCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts._collectors import get_collector_instance


# Generated at 2022-06-12 23:29:31.361202
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test that arguments are set as needed
    params = {'b': 2}
    spec = {'a': {'type': 'int', 'fallback': (env_fallback, 'A')}}

    assert set_fallbacks(spec, params) == set()
    assert params['a'] == 1

    params = {'b': 2}
    assert set_fallbacks(spec, params) == set()
    assert 'a' not in params

    params = {'a': 1}
    spec = {'a': {'type': 'int', 'fallback': (env_fallback, 'A')}}

    # Test that we don't set fallback value if it exists in parameters
    # and that we don't set environment variable if the fallback is done
    assert set_fallbacks(spec, params) == set()

# Generated at 2022-06-12 23:30:07.801431
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = {
        'param1': {'type': 'str', 'fallback': (env_fallback, 'PARAM1')},
        'param2': {'type': 'str', 'fallback': (env_fallback, 'PARAM2')},
        'param3': {'type': 'str', 'fallback': (env_fallback, 'PARAM3')},
    }

    os.environ['PARAM2'] = 'BBB'
    os.environ['PARAM3'] = 'none'

    parameters = {'param1': 'AAA'}

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 1
    assert 'BBB' in no_log_values
    assert 'AAA' not in no_log_values



# Generated at 2022-06-12 23:30:15.692781
# Unit test for function env_fallback
def test_env_fallback():
    # Test env_fallback(arg1, arg2)
    # When arg1 is set in os.environ
    with patch.dict('os.environ', {'arg1': 'test_value'}):
        assert env_fallback('arg1', 'arg2') == 'test_value'
    # When arg2 is set in os.environ
    with patch.dict('os.environ', {'arg2': 'test_value'}):
        assert env_fallback('arg1', 'arg2') == 'test_value'
    # When neither arg1 nor arg2 is set in os.environ
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('arg1', 'arg2')
    #

# Generated at 2022-06-12 23:30:24.116901
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {'param1': {'type': 'str', 'fallback': (env_fallback, ('ONE',), {'default': 'ONE_DEFAULT'})}}
    params = {'param1': 'ONE_DEFAULT'}
    result = set_fallbacks(spec, params)
    assert params['param1'] == 'ONE'
    assert result == set()

    params = {'param1': 'ONE'}
    result = set_fallbacks(spec, params)
    assert params['param1'] == 'ONE'
    assert result == set()

    spec = {'param1': {'type': 'str', 'fallback': (env_fallback, ('ONE',))}}
    params = {'param1': 'ONE'}
    result = set_fallbacks(spec, params)
    assert params['param1']

# Generated at 2022-06-12 23:30:33.815705
# Unit test for function remove_values
def test_remove_values():
    assert remove_values(None, to_native(['a', 'b'], errors='surrogate_or_strict')) == None
    assert remove_values(False, to_native(['a', 'b'], errors='surrogate_or_strict')) == False
    assert remove_values(True, to_native(['a', 'b'], errors='surrogate_or_strict')) == True
    assert remove_values(1, to_native(['a', 'b'], errors='surrogate_or_strict')) == 1
    assert remove_values(b'a', to_native(['a', 'b'], errors='surrogate_or_strict')) == b'a'

# Generated at 2022-06-12 23:30:39.270584
# Unit test for function env_fallback
def test_env_fallback():
    os.environ["SSH_USER"] = "test"
    assert env_fallback("SSH_USER") == "test"
    os.environ["SSH_USER"] = ""
    assert env_fallback("SSH_USER") == ""
    del os.environ["SSH_USER"]
    assert env_fallback("SSH_USER") == ""


# Generated at 2022-06-12 23:30:48.178812
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:30:59.510310
# Unit test for function remove_values
def test_remove_values():
    # Use a list, not a tuple, for the no_log_strings, because those are converted to a list in remove_values()
    no_log_strings = ['replace_me', 'replace_me2']

# Generated at 2022-06-12 23:31:02.093231
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('not_a_real_envres') == AnsibleFallbackNotFound
    assert isinstance(env_fallback('USER'), string_types)


# Generated at 2022-06-12 23:31:11.778721
# Unit test for function remove_values
def test_remove_values():
    class mylist(list):
        pass

    class mytuple(tuple):
        pass

    class mydict(dict):
        pass

    class myset(set):
        pass

    class myint(int):
        pass

    class mystr(str):
        pass

    class myunicode(str):
        pass

    class mybinstr(str):
        pass

    def _verify_keys_stripped_out(value, no_log_strings):
        # ensure that key values have been stripped out
        if isinstance(value, Mapping):
            for key, elem in value.items():
                assert isinstance(key, string_types)
                assert not any(x in key for x in no_log_strings), "key %s contains a no_log value" % key
                _verify_keys_stri

# Generated at 2022-06-12 23:31:22.149546
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test empty or None
    parameters = {}
    argument_spec = {}
    no_log_values = test_set_fallbacks()
    assert no_log_values == set(), "no_log_values is not empty."

    # Test no fallback
    parameters = {}
    argument_spec = {"test11": {"type": "str", "required": True}}
    no_log_values = test_set_fallbacks()
    assert no_log_values == set(), "no_log_values is not empty."

    # Test fallback
    parameters = {}
    os.environ['test1'] = "abcd"
    argument_spec = {"test11": {"type": "str", "required": True, "fallback": ("env_fallback", "test1")}}
    no_log_values = test_set_fallbacks

# Generated at 2022-06-12 23:32:14.946417
# Unit test for function sanitize_keys
def test_sanitize_keys():
    # Setup data for tests
    test_data = dict(
        x1=1,
        x2=2,
        x3=1,
        x4=2,
        x5=3,
        x6=1,
        x7=1,
        x8=5,
        x9=1,
        x10=2,
        x11=1,
    )
    keys_to_sanitize = ['x2', 'x5', 'x7', 'x8']
    keys_to_ignore = ['x3', 'x6']

    # Run function
    actual = sanitize_keys(test_data, keys_to_sanitize, keys_to_ignore)

    # Verify results
    # Keys in keys_to_sanitize are replaced with "<SANITIZED>"

# Generated at 2022-06-12 23:32:25.689862
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = {}
    argument_spec = {
        'field': {
            'type': 'str',
            'fallback': (env_fallback, ['field'])
        }
    }
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()

    parameters = {}
    argument_spec = {
        'field': {
            'type': 'str',
            'fallback': (env_fallback, ['field']),
            'no_log': True
        }
    }
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()

    parameters = {}
    os.environ['field'] = 'abc'

# Generated at 2022-06-12 23:32:33.940012
# Unit test for function env_fallback
def test_env_fallback():
    mock_call_args = {'foo': 'foo_value', 'bar': 'bar_value'}
    with patch('os.environ', new=mock_call_args):
        assert env_fallback('foo') == mock_call_args['foo'], "Should return value if env var is present."

    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('baz')


# Generated at 2022-06-12 23:32:42.284008
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        abc=dict(type='str', fallback=('env_fallback', 'ABC')),
        xyz=dict(type='str', fallback=('env_fallback', 'XYZ')),
        pqr=dict(type='str', fallback=('env_fallback', 'PQR')),
        nml=dict(type='str', fallback=('env_fallback', 'NML')),
        foo=dict(type='str', fallback=('env_fallback', 'FOO', dict(fallback=['one', 'two']))),
        bar=dict(type='str', fallback=('env_fallback', 'BAR', dict(fallback=['one', 'two']))),
    )

# Generated at 2022-06-12 23:32:52.747709
# Unit test for function set_fallbacks
def test_set_fallbacks():
    args = [{'default': '127.0.0.1',
             'fallback': ['env_fallback', 'ANSIBLE_TEST_SET_FALLBACKS_HOST'],
             'type': 'str'}]
    parameters = {}
    no_log_values = set_fallbacks(args, parameters)

    assert parameters.get('default') == '127.0.0.1'

    os.environ['ANSIBLE_TEST_SET_FALLBACKS_HOST'] = '192.168.56.10'
    no_log_values = set_fallbacks(args, parameters)
    assert parameters.get('default') == '192.168.56.10'


# Generated at 2022-06-12 23:33:01.554032
# Unit test for function env_fallback
def test_env_fallback():
    # Set the env variable
    os.environ["ENV_VAR_TEST_NAME"] = "foobar"
    assert env_fallback("ENV_VAR_TEST_NAME") == 'foobar'
    os.environ["ENV_VAR_TEST_NAME"] = "another_foobar"
    assert env_fallback("ENV_VAR_TEST_NAME") == 'another_foobar'
    # Delete the environment variable
    del os.environ["ENV_VAR_TEST_NAME"]
    with pytest.raises(AnsibleFallbackNotFound, match='environment variable for ENV_VAR_TEST_NAME not set.'):
        env_fallback("ENV_VAR_TEST_NAME")



# Generated at 2022-06-12 23:33:08.641918
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['SOME_ENV_VAR'] = 'myvalue'
    assert env_fallback('SOME_ENV_VAR') == 'myvalue'
    assert env_fallback('SOME_UNSET_ENV_VAR') == 'myvalue'
    try:
        env_fallback('SOME_UNSET_ENV_VAR')
    except AnsibleFallbackNotFound:
        assert True



# Generated at 2022-06-12 23:33:15.467596
# Unit test for function env_fallback
def test_env_fallback():
    os.environ.update({'ANSIBLE_FOO': 'foo', 'ANSIBLE_BAR': 'bar'})
    assert env_fallback('ANSIBLE_FOO') == 'foo'
    assert env_fallback('ANSIBLE_QUX') == 'bar'
    assert env_fallback('ANSIBLE_BAR') == 'bar'
    assert env_fallback('ANSIBLE_EXCEPT') == 'bar'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_QUX', 'ANSIBLE_QUUX')



# Generated at 2022-06-12 23:33:26.523228
# Unit test for function set_fallbacks
def test_set_fallbacks():
    result = {}
    fallback_func = MagicMock()
    argument_spec = {'test_option':{'type':'str', 'fallback':(fallback_func,)}}
    set_fallbacks(argument_spec, result)

    # Check default fallback loading
    argument_spec = {'test_with_default':{'type':'str', 'default':'test_default'},'test_option':{'type':'str'}}
    result = {}
    no_log_values = set_fallbacks(argument_spec, result)
    assert result['test_with_default'] == 'test_default'
    assert 'test_default' not in no_log_values

    # Check env fallback loading

# Generated at 2022-06-12 23:33:34.178821
# Unit test for function set_fallbacks
def test_set_fallbacks():

    with patch.dict('os.environ', {'ANSIBLE_NET_AUTHORIZE': 'yes',
                                   'ANSIBLE_NET_AUTH_PASS': 'mysecret',
                                   'ANSIBLE_NET_AUTH_KEY_FILE': '/home/user/.ssh/id_rsa',
                                   'ANSIBLE_NET_AUTH_PASSWORD': 'mypassword',
                                   'ANSIBLE_NET_AUTH_USERNAME': 'myusername'}):
        params = {'command': '/bin/true'}

# Generated at 2022-06-12 23:34:26.476830
# Unit test for function set_fallbacks
def test_set_fallbacks():
    string_spec = dict(type='str')
    int_spec = dict(type='int')
    list_spec = dict(type='list')
    dict_spec = dict(type='dict')
    bool_spec = dict(type='bool')

    argument_spec = {
        'param': string_spec,
        'param2': int_spec,
        'param3': list_spec,
        'param4': dict_spec,
        'param5': bool_spec,
    }

    assert list(set_fallbacks(argument_spec, {})) == []

    parameters = {
        'param': 'param1',
        'param2': 2,
        'param3': [],
        'param4': {},
        'param5': True,
    }

# Generated at 2022-06-12 23:34:35.174678
# Unit test for function set_fallbacks
def test_set_fallbacks():
    '''
    test set_fallbacks()
    '''
    param = dict(fallback=[env_fallback, 'TEST_ENV'], no_log=True)
    argument_spec = dict(test=param)
    os.environ['TEST_ENV'] = 'test'
    parameters = dict()
    assert set_fallbacks(argument_spec, parameters) == {'test'}
    assert parameters['test'] == 'test'
    os.environ.pop('TEST_ENV')


_GET_LEGAL_INPUTS_CHECK_UNIQUE = {}



# Generated at 2022-06-12 23:34:43.391546
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test env_fallback function
    os.environ["ANSIBLE_TEST_ENV_VAR"] = "tautology"
    args = [{'fallback': (env_fallback, "ANSIBLE_TEST_ENV_VAR", "ANSIBLE_TEST_ENV_VAR2")}]
    result = {}
    set_fallbacks(*args, parameters=result)
    assert result == {"ANSIBLE_TEST_ENV_VAR": "tautology"}, "test_set_fallbacks failed"
    del os.environ["ANSIBLE_TEST_ENV_VAR"]

    # Testing build-in fallback strategies

# Generated at 2022-06-12 23:34:49.120832
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'test_param': {'type': 'str', 'fallback': (env_fallback, 'TEST_PARAM_ENV')}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['test_param'] == 'TEST_PARAM_ENV'
    assert no_log_values == set()



# Generated at 2022-06-12 23:34:55.207227
# Unit test for function env_fallback
def test_env_fallback():
    ''' test env_fallback function '''
    # test case 1
    os.environ = {'ENV_VAR_1': 'env_var_1'}
    val1 = env_fallback('ENV_VAR_1')
    assert val1 == 'env_var_1'

    # test case 2
    os.environ = {'ENV_VAR_1': 'env_var_1'}
    val2 = env_fallback('ENV_VAR_2')
    assert val2 is None


# Generated at 2022-06-12 23:35:00.301109
# Unit test for function env_fallback
def test_env_fallback():
    env_vars = ['test1', 'test2']
    with patch.dict(os.environ):
        os.environ['test1'] = 'test1value'
        os.environ['test2'] = 'test2value'

        assert env_fallback(*env_vars) == 'test1value'
        del os.environ['test1']
        assert env_fallback(*env_vars) == 'test2value'
        del os.environ['test2']

        try:
            env_fallback(*env_vars)
        except AnsibleFallbackNotFound:
            pass
        else:
            raise AssertionError('AnsibleFallbackNotFound not raised')



# Generated at 2022-06-12 23:35:09.135685
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_VARIABLE'] = r'value\with\backslash'
    assert env_fallback('ANSIBLE_TEST_VARIABLE') == r'value\with\backslash'
    del os.environ['ANSIBLE_TEST_VARIABLE']
    os.environ['ANSIBLE_TEST_VARIABLE'] = '"value with quote"'
    assert env_fallback('ANSIBLE_TEST_VARIABLE') == 'value with quote'
    del os.environ['ANSIBLE_TEST_VARIABLE']
    os.environ['ANSIBLE_TEST_VARIABLE'] = "'value with quote'"
    assert env_fallback('ANSIBLE_TEST_VARIABLE') == 'value with quote'
    del os

# Generated at 2022-06-12 23:35:19.951034
# Unit test for function remove_values
def test_remove_values():
    assert remove_values(
        {
            'secret': 'bar',
            'password': 'foo'
        },
        ['bar', 'foo']
    ) == {
        'secret': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER',
        'password': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    }

    assert remove_values(
        'some password',
        ['some password']
    ) == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'


# Generated at 2022-06-12 23:35:32.276605
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # For testing purposes we need to fake our module argument parsing.
    class FakeModule(object):
        def __init__(self, params):
            self.params = params

    params = {}
    argument_spec = {"param": {"required": False, "default": "a", "fallback": (env_fallback, "PARAM")}}
    mod = FakeModule(params)
    params = set_fallbacks(argument_spec, params)
    assert params == set(["a"])
    # The following line will only work if the environment variable KERBEROS_PASSWORD is not defined
    params = set_fallbacks(argument_spec, {"param": "b"})
    assert params == set(["b"])

# Generated at 2022-06-12 23:35:44.464991
# Unit test for function env_fallback
def test_env_fallback():
    from ansible.module_utils._text import to_bytes
    os.environ['ANSIBLE_VAULT_PASSWORD_FILE'] = '/path/to/file'
    os.environ['ANSIBLE_VAULT_PASSWORD'] = 'pass'
    assert env_fallback('ANSIBLE_VAULT_PASSWORD_FILE', 'ANSIBLE_VAULT_PASSWORD') == '/path/to/file'
    del os.environ['ANSIBLE_VAULT_PASSWORD_FILE']
    assert env_fallback('ANSIBLE_VAULT_PASSWORD_FILE', 'ANSIBLE_VAULT_PASSWORD') == 'pass'
    os.environ['ANSIBLE_VAULT_PASSWORD'] = to_bytes('pass')

# Generated at 2022-06-12 23:36:37.453846
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(foo=dict(type='str', fallback=(env_fallback, 'foo_env')),
                         bar=dict(type='str', fallback=(env_fallback, 'bar_env')),
                         baz=dict(type='str', fallback=(env_fallback, [{'params': 'foo_bar_env', 'other': 'other_env'}])),
                         no_log=dict(type='str', fallback=(env_fallback, 'no_log'), no_log=True))
    parameters = dict(bar='bar_param')

    os.environ['foo_env'] = 'foo_env'
    os.environ['no_log'] = 'no_log'

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values

# Generated at 2022-06-12 23:36:48.608116
# Unit test for function set_fallbacks
def test_set_fallbacks():
    args = [{
        'name': {
            'required': True,
            'type': 'str',
            'fallback': (env_fallback, ('ANSIBLE_NET_USERNAME',)),
        }
    }, {
        'name': 'test'
    }]
    no_logs = set_fallbacks(*args)
    assert len(no_logs) == 0

    os.environ['ANSIBLE_NET_USERNAME'] = 'test'
    no_logs = set_fallbacks(*args)
    assert len(no_logs) == 0

    args[1]['name'] = None
    no_logs = set_fallbacks(*args)
    assert len(no_logs) == 0
    assert args[1]['name'] == 'test'


# Generated at 2022-06-12 23:36:54.487792
# Unit test for function remove_values
def test_remove_values():
    # basic tests, including recursive tests
    assert remove_values('test', []) == 'test'
    assert remove_values('test', ['test']) == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    assert remove_values(42, ['42']) == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    assert remove_values(False, ['False']) == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    assert remove_values([1, 2, 3], [1]) == ['VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 2, 3]

# Generated at 2022-06-12 23:37:06.899961
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_parameters = {}
    test_spec = dict(test_variable=dict(fallback=(env_fallback, 'TEST_VARIABLE', 'DEFAULT_VALUE')))
    os.environ['TEST_VARIABLE'] = 'test value'
    # Test fallback is set with environment variable
    no_log_values = set_fallbacks(test_spec, test_parameters)
    assert test_parameters['test_variable'] == 'test value'
    # Test default value is set when no env variable is set
    os.environ['TEST_VARIABLE'] = None
    no_log_values = set_fallbacks(test_spec, test_parameters)
    assert test_parameters['test_variable'] == 'DEFAULT_VALUE'
    # Test list fallback
    test_spec

# Generated at 2022-06-12 23:37:11.147232
# Unit test for function env_fallback
def test_env_fallback():
    result_from_env = env_fallback("ANSIBLE_MODULE_ARGS", "ANSIBLE_MODULE_ARGS_1", "ANSIBLE_MODULE_ARGS_2")
    assert result_from_env == os.environ["ANSIBLE_MODULE_ARGS"]


# Generated at 2022-06-12 23:37:22.025989
# Unit test for function sanitize_keys
def test_sanitize_keys():
    affected_keys = {'foo', 'bar', 'baz'}
    data = dict.fromkeys(affected_keys, {'a': 1, 'b': 2})
    data['password'] = "password"
    data['nested'] = {}
    data['nested']['neighbor'] = data
    data['not_affected'] = {"foo_bar_baz": ["zab.toof.rab", "foo_bar_baz"]}
    ignore_keys = {'password'}
    new_data = sanitize_keys(data, no_log_strings={"foo", "bar", "baz"}, ignore_keys=ignore_keys)

    for key in affected_keys:
        assert key not in new_data
        assert key.strip("_") in new_data


# Generated at 2022-06-12 23:37:27.854375
# Unit test for function remove_values
def test_remove_values():
    """_remove_values_conditions: unit tests"""
    # return value when value is not a container type
    assert _remove_values_conditions('', ['test']) is None
    assert _remove_values_conditions(1, ['test']) is None
    assert _remove_values_conditions(1.0, ['test']) is None
    assert _remove_values_conditions(True, ['test']) is None

    # values in no_log_strings don't appear in return value
    assert _remove_values_conditions('', ['test']) == ''
    assert _remove_values_conditions('', ['t', 'e', 's', 't']) == ''
    assert _remove_values_conditions('test', ['t', 'e', 's', 't']) == '****'
    assert _remove_

# Generated at 2022-06-12 23:37:30.260708
# Unit test for function env_fallback
def test_env_fallback():
    set_fallbacks({}, {'key_in_env': {'fallback': env_fallback('key_in_env')}})



# Generated at 2022-06-12 23:37:40.671262
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['test_env'] = 'test'