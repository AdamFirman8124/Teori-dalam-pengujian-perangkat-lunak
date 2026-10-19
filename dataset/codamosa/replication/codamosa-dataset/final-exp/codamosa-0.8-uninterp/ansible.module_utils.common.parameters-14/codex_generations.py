

# Generated at 2022-06-12 23:28:34.897399
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:28:42.252711
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(default='bar', type='str'),
        biz=dict(type='str'),
        baz=dict(type='str'),
        bof=dict(type='str'),
        voo=dict(fallback=(env_fallback, 'FOO'), type='str'),
        foobar=dict(type='dict', options=dict(
            lala=dict(default='lolo', type='str'),
        ), fallback=(dict, dict(lala='momo'))),
    )
    _set_defaults(argument_spec, dict())
    assert argument_spec['foo']['default'] == 'bar'
    assert argument_spec['biz']['default'] is None
    assert argument_spec['foobar']['default']['lala'] == 'lolo'

# Generated at 2022-06-12 23:28:49.752009
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'foo': {'type': 'str', 'fallback': (env_fallback, 'FOO_ENV_VAR')},
                     'bar': {'type': 'int', 'fallback': (env_fallback, 'BAR_ENV_VAR', {'type': 'int'})}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'foo': 'FOO_ENV_VAR', 'bar': 'BAR_ENV_VAR'}
    assert no_log_values == set()



# Generated at 2022-06-12 23:28:55.758880
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'param1': {'fallback': (env_fallback, ['ANSIBLE_PARAM1_FOO', 'ANSIBLE_PARAM1_BAR'])}}, {}) == set()
# END of unit test


# Generated at 2022-06-12 23:29:06.167455
# Unit test for function env_fallback
def test_env_fallback():
    assert '5' == env_fallback('ANSIBLE_HTTPAPI_TIMEOUT', '5')[0]
    assert '5' == env_fallback('ANSIBLE_HTTPAPI_TIMEOUT', 'ANSIBLE_TIMEOUT', '5')[0]
    assert 'ANSIBLE_TIMEOUT' == env_fallback('ANSIBLE_HTTPAPI_TIMEOUT', 'ANSIBLE_TIMEOUT')[1]
    assert 'ANSIBLE_TIMEOUT' == env_fallback('ANSIBLE_HTTPAPI_TIMEOUT', 'ANSIBLE_TIMEOUT', '5')[1]
    assert ['ANSIBLE_HTTPAPI_TIMEOUT', 'ANSIBLE_TIMEOUT'] == env_fallback('ANSIBLE_HTTPAPI_TIMEOUT', 'ANSIBLE_TIMEOUT', '5')

# Generated at 2022-06-12 23:29:10.077982
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'foo': {'type': 'str', 'fallback': (env_fallback, 'FOO_ENV_VAR')}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'foo': 'bar'}
    assert no_log_values == {'bar'}



# Generated at 2022-06-12 23:29:15.837654
# Unit test for function sanitize_keys
def test_sanitize_keys():

    # Test module
    class TestModule(object):

        def __init__(self, module_name, module_args, check_invalid_arguments=True):
            self.argument_spec = {
                'sanitize_variables': {'type': 'list', 'elements': 'dict', 'default': []},
                'data': {'type': 'raw'},
            }
            self.params = {}

            # Load module arguments into params
            module_args_copy = module_args.copy()
            for k in module_args_copy:
                if '=' in k:
                    # Parameters may contain shell-style assignments so split on first '='
                    (k, v) = k.split('=', 1)
                    # Account for cases like 'foo=bar=qux'

# Generated at 2022-06-12 23:29:28.264080
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        parameter1=dict(fallback=(env_fallback, 'TEST_VAR1')),
        parameter2=dict(fallback=(env_fallback, 'TEST_VAR2')),
        parameter3=dict(fallback=(env_fallback, 'TEST_VAR3', 'other')),
        parameter4=dict(fallback=(env_fallback, 'TEST_VAR4')),
        parameter5=dict(fallback=(env_fallback, 'TEST_VAR5', dict(convert_to=int))),
        parameter6=dict(fallback=(env_fallback, 'TEST_VAR6')),
        parameter7=dict(fallback=(env_fallback, 'TEST_VAR7')),
    )

# Generated at 2022-06-12 23:29:39.654037
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test ansible.module_utils.common.set_fallbacks"""
    argument_spec = {
        'a': {'type': 'bool', 'fallback': (env_fallback, 'A')},
        'b': {'type': 'bool', 'fallback': (env_fallback, 'B')},
        'c': {'type': 'dict', 'fallback': (env_fallback, 'C')},
    }
    parameters = {}
    assert set() == set_fallbacks(argument_spec, parameters)
    assert {} == parameters

    os.environ['A'] = "1"
    os.environ['C'] = '{ "key1": "value1" }'
    assert set(['1']) == set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:29:49.116373
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Use string fallback with no args
    spec = dict(a=dict(type='str', fallback=('test_value',)))
    parameters = dict()
    no_log_values = set_fallbacks(spec, parameters)
    assert 'test_value' in parameters
    assert len(no_log_values) == 0

    # Use string fallback with args
    spec = dict(a=dict(type='str', fallback=('test_value', 'other_value')))
    parameters = dict()
    no_log_values = set_fallbacks(spec, parameters)
    assert 'test_value' in parameters
    assert parameters['a'] == 'other_value'
    assert len(no_log_values) == 0

    # Use built-in string fallback with args

# Generated at 2022-06-12 23:30:23.673880
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:30:32.132255
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit tests for function set_fallbacks"""

    # no fallback
    argument_spec = dict(
        param1=dict(required=True),
        param2=dict()
    )
    parameters = dict(
        param1='param1_value'
    )
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert 'param1_value' not in no_log_values
    assert 'param1' in parameters
    assert 'param2' not in parameters

    # required fallback
    argument_spec = dict(
        param1=dict(required=True),
        param2=dict(required=True)
    )
    parameters = dict()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert 'param1' in parameters and 'param2' in parameters

# Generated at 2022-06-12 23:30:43.186692
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test fallback from env var
    argument_spec = {
        'one': {'type': 'str', 'fallback': (env_fallback, ('TEST_ONE',))},
        'two': {'type': 'str', 'fallback': (env_fallback, ('TEST_TWO',))},
        'three': {'type': 'str', 'fallback': (env_fallback, ('TEST_THREE',))},
        'four': {'type': 'str', 'fallback': (env_fallback, ('TEST_FOUR',))}
    }
    parameters = {'one': '1', 'two': '2', 'three': '3', 'four': '4'}
    os.environ['TEST_THREE'] = 'three'
    no_log_values = set_fall

# Generated at 2022-06-12 23:30:47.832674
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST_ONE'] = 'ONE'
    os.environ['TEST_TWO'] = 'TWO'
    assert env_fallback('TEST_ONE') == 'ONE'
    assert env_fallback('TEST_TWO') == 'TWO'
    assert env_fallback('TEST_THREE') == None



# Generated at 2022-06-12 23:30:58.392033
# Unit test for function env_fallback
def test_env_fallback():
    with mock.patch.object(os.environ, 'get') as environ_get:
        environ_get.return_value = 'fallback_value'
        assert env_fallback('TEST_ENV') == 'fallback_value'
        assert env_fallback('TEST_ENV2') == 'fallback_value'
        environ_get.assert_has_calls([
            mock.call('TEST_ENV'),
            mock.call('TEST_ENV2')
        ])
        # Check for error if not found
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('TEST_ENV3')



# Generated at 2022-06-12 23:31:00.996143
# Unit test for function env_fallback
def test_env_fallback():
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('BADENVVAR1', 'BADENVVAR2')



# Generated at 2022-06-12 23:31:07.616752
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'package': {'type': 'str'},
                     'version': {'type': 'str'}}
    parameters = {'package': 'test'}
    no_log_values = set()
    no_log_values.update(set_fallbacks(argument_spec, parameters))
    assert parameters['version'] == '0.0.1'
    assert len(no_log_values) == 1



# Generated at 2022-06-12 23:31:18.130327
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = {}
    argument_spec = {
        'fake_parameter': {
            'type': 'str',
            'fallback': (env_fallback, ('ENVIRONMENT_VARIABLE',)),
        }
    }

    os.environ['ENVIRONMENT_VARIABLE'] = "some_value"
    no_log_values = set_fallbacks(argument_spec, parameters)
    # assert len(no_log_values) == 0
    os.environ.pop('ENVIRONMENT_VARIABLE')
    parameters = {}

    os.environ['ENVIRONMENT_VARIABLE'] = "some_other_value"
    no_log_values = set_fallbacks(argument_spec, parameters)
    # assert len(no_log_values) ==

# Generated at 2022-06-12 23:31:26.165372
# Unit test for function sanitize_keys
def test_sanitize_keys():
    data = {'a': 'foo', 'b': 'bar', 'c': 'baz'}
    sanitized_data = sanitize_keys(data, ['foo', 'bar'])
    assert sanitized_data == {'a': 'foo', 'b': 'bar', 'c': 'baz'}

    data = {'a': 'foo', 'b': 'bar', 'c': 'baz'}
    sanitized_data = sanitize_keys(data, ['foo', 'bar', 'baz'])
    assert sanitized_data == {'a': '_', 'b': '_', 'c': '_'}

    data = {'a': {'b': 'foo', 'c': 'bar'}}
    sanitized_data = sanitize_keys(data, ['foo'])
    assert san

# Generated at 2022-06-12 23:31:32.480454
# Unit test for function sanitize_keys
def test_sanitize_keys():
    answer = OrderedDict()
    answer['a'] = OrderedDict()
    answer['a']['b'] = OrderedDict()
    answer['a']['b']['c'] = OrderedDict()
    answer['a']['b']['c']['d'] = 0
    answer['e'] = OrderedDict()
    answer['e']['f'] = OrderedDict()
    answer['e']['f']['g'] = OrderedDict()
    answer['e']['f']['g']['h'] = 1
    answer['i'] = OrderedDict()
    answer['i']['j'] = OrderedDict()
    answer['i']['j']['k'] = OrderedDict()

# Generated at 2022-06-12 23:32:12.676955
# Unit test for function sanitize_keys
def test_sanitize_keys():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256
    from ansible.parsing.vault import VaultUnsupported
    # Note: we are skipping tests that test the VaultLib itself. This is tested in another unit.
    vault_unsupported_keys = [
        'foobar',  # This key is not supported by any vault
        'sha1',  # VaultAES128 requires a sha1 salt length of 8, so this has been deprecated
        'missing_args',  # Missing argument
        'invalid_hash',  # Invalid hash
    ]

# Generated at 2022-06-12 23:32:19.871712
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:32:25.133085
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:32:31.488580
# Unit test for function env_fallback
def test_env_fallback():
    '''Ensure function env_fallback() returns correct values'''
    assert env_fallback('FOO', 'BAR') == 'FOO'
    assert env_fallback('BAR') == 'BAR'
    raises(AnsibleFallbackNotFound, lambda: env_fallback('DOESNOTEXIST'))


# Generated at 2022-06-12 23:32:41.107712
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'param1': {'type': 'str', 'fallback': (env_fallback, 'PARAM1')},
        'param2': {'type': 'str', 'fallback': (env_fallback, 'PARAM2')},
        'param3': {'type': 'str', 'fallback': (env_fallback, ['PARAM3', 'PARAM4'])},
        'param4': {'type': 'str', 'fallback': (env_fallback, 'PARAM5')}
    }
    parameters = {'param1': 'param1_value'}

    os.environ['PARAM2'] = 'param2_value'
    os.environ['PARAM3'] = 'param3_value'


# Generated at 2022-06-12 23:32:53.009710
# Unit test for function sanitize_keys

# Generated at 2022-06-12 23:33:01.954947
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test dict fallback
    fallback = {'CONNECTION_USERNAME': 'ec2-user'}
    fb1 = {'type': 'str', 'fallback': (dict, fallback)}
    assert set_fallbacks({'connection_user': fb1}, {}) == set()
    assert set_fallbacks({'connection_user': fb1}, {'connection_user': 'foo'}) == set()
    parameters = {'connection_user': None}
    assert set_fallbacks({'connection_user': fb1}, parameters) == set(['ec2-user'])
    assert parameters == {'connection_user': 'ec2-user'}

    # Test env_fallback

# Generated at 2022-06-12 23:33:12.343397
# Unit test for function remove_values
def test_remove_values():
    assert remove_values('hi', ['hi']) is None
    assert remove_values('hi', ['otherthing']) == 'hi'
    assert remove_values('', ['']) is None
    assert remove_values('', ['otherthing']) == ''
    assert remove_values(1, [1]) is None
    assert remove_values(1, [2]) == 1
    assert remove_values({'a': 'b'}, ['b']) == {'a': None}
    assert remove_values({'a': 'b'}, ['c']) == {'a': 'b'}
    assert remove_values({'a': 1}, [1]) == {'a': None}
    assert remove_values({'a': 1}, [2]) == {'a': 1}

# Generated at 2022-06-12 23:33:23.304989
# Unit test for function set_fallbacks
def test_set_fallbacks():
    fallbacks = [
        ('env', 'PYTHON_HOME'),
        ('env', 'PYTHONHOME'),
        ('constant', '/usr'),
    ]

    spec = {
        'Python_home': {
            'required': True,
            'type': 'str',
            'fallback': fallbacks,
        },
    }

    # Case 1: local variable is set and 'env' variable is not set.
    parameters = {'Python_home': '/usr/local/bin'}
    no_log_values = set_fallbacks(spec, parameters)
    assert parameters['Python_home'] == '/usr/local/bin'
    assert not no_log_values

    # Case 2: local variable is not set, but 'env' variable is available
    parameters = {}
    no_log_values = set_

# Generated at 2022-06-12 23:33:32.044012
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:34:36.252041
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = {'host': 'joe'}
    expected = {'host': 'joe'}
    assert set_fallbacks({'host': {'type': 'str'}}, parameters) == set()
    assert parameters == expected

    parameters = {'host': 'joe'}
    expected = {'host': 'joe'}
    assert set_fallbacks({'host': {'type': 'str', 'fallback': (None,)}}, parameters) == set()
    assert parameters == expected

    parameters = {'host': 'joe'}
    expected = {'host': 'joe', 'port': 22}
    assert set_fallbacks({'host': {'type': 'str'}, 'port': {'type': 'int', 'fallback': (22,)}}, parameters) == set()
    assert parameters == expected

# Generated at 2022-06-12 23:34:37.677875
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('FOO') == os.environ['FOO']



# Generated at 2022-06-12 23:34:41.117486
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback("HOME", "MOO") == os.environ['HOME']
    try:
        env_fallback("MOO", "BAR")
    except AnsibleFallbackNotFound:
        pass
    else:
        raise Exception("env_fallback failed to fail!")



# Generated at 2022-06-12 23:34:44.408658
# Unit test for function sanitize_keys
def test_sanitize_keys():
    # input parameters
    no_log_strings = ['this']
    obj = [{'key1': 'value1'}, {'key2': 'value2'}]
    ignore_keys = ['key1']
    # correct value
    correct_values = [{'key1': 'value1'}, {'key2': None}]
    # test
    output_values = sanitize_keys(obj, no_log_strings, ignore_keys)
    assert correct_values == output_values



# Generated at 2022-06-12 23:34:53.414094
# Unit test for function env_fallback
def test_env_fallback():

    try:
        test = env_fallback('LANG')
        assert test == 'en_US.UTF-8'
    except AnsibleFallbackNotFound:
        assert False
    try:
        test = env_fallback('LANG', 'XXX')
        assert False
    except AnsibleFallbackNotFound:
        assert True

    try:
        test = env_fallback(['LANG', 'XXX'])
        assert test == 'en_US.UTF-8'
    except AnsibleFallbackNotFound:
        assert False

    try:
        test = env_fallback(['XXX', 'YYY'])
        assert False
    except AnsibleFallbackNotFound:
        assert True



# Generated at 2022-06-12 23:35:01.261224
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:35:09.666823
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test no fallback
    param = {
        'param1': {
            'type': 'str',
        },
    }
    params = {
        'param1': 'value1'
    }
    assert set_fallbacks(param, params) == set()
    assert params == {
        'param1': 'value1'
    }

    # Test fallback with env
    param = {
        'param2': {
            'type': 'str',
            'fallback': (env_fallback, 'ENV_VAR_2')
        },
    }
    params = {
        'param1': 'value1',
    }
    try:
        os.environ.pop('ENV_VAR_2')
    except KeyError:
        pass
    assert set_fallbacks(param, params)

# Generated at 2022-06-12 23:35:20.368178
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:35:26.350152
# Unit test for function env_fallback
def test_env_fallback():
    assert(env_fallback('TEST_ENV') == os.environ['TEST_ENV'])
    assert(env_fallback('TEST_ENV2') == os.environ['TEST_ENV2'])

# Generated at 2022-06-12 23:35:36.153217
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = {}
    spec = {'a': {'fallback': (env_fallback, ['ANSIBLE_TEST'])},
            'b': {'fallback': (env_fallback, ['ANSIBLE_TEST'])},
            'c': {'fallback': (env_fallback, ['ANSIBLE_TEST'])}}
    os.environ['ANSIBLE_TEST'] = 'environment'
    assert set_fallbacks(spec, params) == set()
    assert params == {'a': 'environment', 'b': 'environment', 'c': 'environment'}
    os.environ['ANSIBLE_TEST'] = None
    assert set_fallbacks(spec, params) == set()
    os.environ['ANSIBLE_TEST'] = ''
    assert set_fallbacks(spec, params) == set()

# Generated at 2022-06-12 23:36:41.223085
# Unit test for function sanitize_keys
def test_sanitize_keys():
    class TestClass(object):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return isinstance(other, TestClass) and self.value == other.value

        def __repr__(self):
            return 'TestClass(%s)' % repr(self.value)

        def __hash__(self):
            return hash(self.value)


# Generated at 2022-06-12 23:36:51.010055
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'first': {
            'type': 'str',
            'default': 'first_default'
        },
        'second': {
            'type': 'str',
            'default': 'second_default',
            'fallback': (env_fallback, 'SECOND'),
        },
        'third': {
            'type': 'str',
            'fallback': (env_fallback, 'THIRD'),
        },
        'fourth': {
            'type': 'str',
            'fallback': (env_fallback, 'FOURTH'),
            'no_log': True,
        },
    }

    parameters = {
        'first': 'first_value',
    }

    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:37:01.877170
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test that fallback will set value not already in parameters
    argument_spec = {
        'test_arg': {'fallback': (env_fallback, 'TEST_ENV_VAR')},
        'no_log_test_arg': {'fallback': (env_fallback, 'TEST_ENV_VAR'), 'no_log': True}
    }

    parameters = {}
    no_log_values = set()
    env_var = 'TEST_ENV_VAR'
    env_val = 'test_value'

    try:
        os.environ[env_var] = env_val
        no_log_values = set_fallbacks(argument_spec, parameters)
    finally:
        del os.environ[env_var]


# Generated at 2022-06-12 23:37:10.796057
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:37:21.449134
# Unit test for function sanitize_keys
def test_sanitize_keys():
    test_obj = {
        'example': {
            'secret': 'test_value',
            'ignore': 'test_value',
        }
    }
    test_obj['not_example'] = test_obj['example']
    test_obj['not_example_1'] = test_obj['not_example']
    expected_result = {
        'example': {
            'xxxxxxxx': 'test_value',
            'ignore': 'test_value',
        }
    }
    expected_result['not_example'] = expected_result['example']
    expected_result['not_example_1'] = expected_result['example']
    result = sanitize_keys(test_obj, {'secret'}, {'ignore'})
    assert result == expected_result



# Generated at 2022-06-12 23:37:27.348086
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # For example argument_spec of module_utils.network.common.utils.py[edit]
    argument_spec = dict(
        config=dict(fallback=(env_fallback, ['ANSIBLE_NET_CONFIG']), type='str'),
        running_config=dict(fallback=(env_fallback, ['ANSIBLE_NET_RUNNING_CONFIG']), type='str'),
        save_config=dict(type='bool', default=False),
        state=dict(choices=['absent', 'present'], default='present')
    )
    parameters = dict(
        config = "ansible/test/files/ansible.cfg",
        running_config = "ansible/test/files/ansible.cfg",
        save_config = False,
        state = "present"
    )
    no_log_values

# Generated at 2022-06-12 23:37:38.721754
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'one': {'type': 'str', 'fallback': (env_fallback, ['ONE', 'TWO'])},
        'two': {'type': 'str', 'fallback': (lambda: 'a')},
        'three': {'type': 'str', 'fallback': (lambda: None)},
        'four': {'type': 'str', 'fallback': (lambda: 1)},
        'five': {'type': 'str', 'fallback': (lambda x: x * 2, 'one')},
        'six': {'type': 'str', 'fallback': (lambda x, y=2: x * y, 'two', 'seven')},
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_