

# Generated at 2022-06-12 23:28:26.837340
# Unit test for function set_fallbacks
def test_set_fallbacks():
    result = set_fallbacks({'b': {'default': 'foo'}}, {})
    assert result == set()


# Generated at 2022-06-12 23:28:36.646461
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test for set_fallbacks"""

    argument_spec = {
        'name': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_MODULE_ARGS_NAME'], {'default': 'foobar'})}
    }
    parameters = {'name': 'parameters'}

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['name'] == 'parameters'
    assert no_log_values == set()

    parameters = {}
    os.environ['ANSIBLE_MODULE_ARGS_NAME'] = 'test'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['name'] == 'test'
    assert no_log_values == set()


# Generated at 2022-06-12 23:28:47.683408
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'test_url': {'type': 'str', 'required': True, 'fallback': (env_fallback, 'ANSIBLE_TEST_URL')},
        'test_age': {'type': 'int', 'required': True, 'fallback': (env_fallback, 'ANSIBLE_TEST_AGE')},
        'test_user': {'type': 'str', 'required': False, 'fallback': (env_fallback, ('ANSIBLE_TEST_USER', 'ANSIBLE_TEST_USERNAME'))},
    }

    os.environ['ANSIBLE_TEST_URL'] = 'http://localhost'
    os.environ['ANSIBLE_TEST_AGE'] = '42'
    os.environ['ANSIBLE_TEST_USER'] = 'admin'
    os.en

# Generated at 2022-06-12 23:28:59.953188
# Unit test for function sanitize_keys
def test_sanitize_keys():
    # No log strings are included in the data structure itself
    my_data = {
        'param1': 'The quick brown fox jumps over the lazy dog',
        'param2': 'The quick brown fox jumps over the lazy dog',
        'param3': {
            'param4': {
                'param5': 'The quick brown fox jumps over the lazy dog',
                'param6': 'The quick brown fox jumps over the lazy dog'
            },
            'param7': {
                'param8': 'The quick brown fox jumps over the lazy dog',
                'param9': 'The quick brown fox jumps over the lazy dog'
            }
        }
    }
    no_log_strings = ['The quick brown fox jumps over the lazy dog']

    no_log_strings.extend(('***', '***'))
    assert sanitize_keys

# Generated at 2022-06-12 23:29:09.455246
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'param': {'type': 'str', 'fallback': (env_fallback, ['param_env'])},
        'param2': {'type': 'str', 'fallback': (env_fallback, ['param_env2'])},
    }

    parameters = {'param': None}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters['param'] == None

    parameters = {'param': None}
    os.environ['param_env'] = 'fallback_value'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters['param'] == 'fallback_value'


# Generated at 2022-06-12 23:29:15.666965
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'baz': {'type': 'str', 'fallback': (env_fallback, ('ANSIBLE_TEST_FOO_BAZ', 'ANSIBLE_TEST_BAR_BAZ'))},
        'foo': {'type': 'str', 'fallback': (env_fallback, ('ANSIBLE_TEST_FOO_FOO', 'ANSIBLE_TEST_BAR_FOO'))},
        'bar': {'type': 'str', 'fallback': (env_fallback, ('ANSIBLE_TEST_FOO_BAR', 'ANSIBLE_TEST_BAR_BAR'))},
        'dict_key': {'type': 'str', 'fallback': (env_fallback, {'key': 'ANSIBLE_TEST_KEY'})},
    }

# Generated at 2022-06-12 23:29:28.065920
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        command=dict(type='str', fallback=(env_fallback, 'ANSIBLE_NET_COMMAND')),
        provider=dict(type='dict', elements='str', fallback=(env_fallback, 'ANSIBLE_NET_PROVIDERS')),
        transport=dict(type='str', fallback=(env_fallback, 'ANSIBLE_NET_TRANSPORT')),
    )
    parameters = {}
    with patch.dict(os.environ, {'ANSIBLE_NET_COMMAND': 'show version', 'ANSIBLE_NET_TRANSPORT': 'cli'}):
        no_log_values = set_fallbacks(argument_spec, parameters)
        assert len(no_log_values) == 0
        assert parameters['command'] == 'show version'

# Generated at 2022-06-12 23:29:39.435378
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # test1
    # parameter is None and no fallback
    argument_spec = {
        'name': {'type': 'str'},
        'state': {'type': 'str', 'default': 'present', 'choices': ['present', 'absent']},
        'force': {'type': 'bool', 'default': False}
    }
    parameters = {'state': 'absent'}
    no_log_values = set()
    set_fallbacks(argument_spec, parameters)
    assert parameters['name'] == None

    # test2
    # parameter is not None and fallback

# Generated at 2022-06-12 23:29:48.930884
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'name': {'required': True, 'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_NET_USERNAME'])},
        'password': {'required': False, 'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_NET_PASSWORD'])},
        'ssh_keyfile': {'required': False, 'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_NET_SSH_KEYFILE'])},
    }
    # test that fallback fallback value is applied when the parameter name is not in parameters
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert len(parameters) == 3

   

# Generated at 2022-06-12 23:29:57.798856
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = dict()
    argument_spec = dict()

    argument_spec['username'] = dict(type='str', required=True)

    fallback_arg = dict(type='env', version=dict(required=True, fallback=(env_fallback, ('ANSIBLE_VERSION', 'ANSIBLE_VERSION2'))))
    argument_spec['version'] = dict(type='str', fallback=(env_fallback, 'ANSIBLE_VERSION', fallback_arg))

    no_log_values = set()
    no_log_values.update(set_fallbacks(argument_spec=argument_spec, parameters=parameters))
    assert len(no_log_values) == 0

    os.environ['ANSIBLE_VERSION'] = 'ansible-version-1'

# Generated at 2022-06-12 23:30:31.687840
# Unit test for function set_fallbacks
def test_set_fallbacks():

    def def_fallback():
        return 'foo'

    def def_fallback_with_args(arg1, arg2):
        return 'foo'

    def def_fallback_with_kwargs(arg1, arg2='bar'):
        return 'foo'

    def def_fallback_with_args_and_kwargs(arg1, arg2='bar'):
        return 'foo'

    def def_fallback_with_args_and_kwargs_2(arg1, arg2, arg3, arg4='bar'):
        return 'foo'


# Generated at 2022-06-12 23:30:42.826201
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'a': {'type': 'str', 'fallback': (env_fallback, ['TEST_A', 'TEST_B'])},
        'b': {'type': 'str', 'fallback': (env_fallback, ['TEST_C'])},
        'c': {'type': 'str', 'fallback': (env_fallback, ['TEST_D'], {'default': 'TEST_E'})},
        'd': {'type': 'str', 'fallback': (env_fallback, {'vars': ['TEST_F']})},
    }
    # No parameter is set, all values should find fallback successfully
    parameters = {}
    os.environ['TEST_A'] = 'test a'

# Generated at 2022-06-12 23:30:50.488560
# Unit test for function remove_values
def test_remove_values():
    # Test data
    no_log_strings = ['banana', 'baz', 'foo']
    test_data = {
        'key1': "foo bar baz qux",
        'key2': ['foo', {'foo': 'banana'}, ['baz', 'banana'], set(['baz', 'banana']), ('baz', {'foo': 'banana'})],
        'key3': {'foo': 'bar', 'banana': 'baz'},
        'key4': 'baz'
    }

    # Expected result

# Generated at 2022-06-12 23:30:55.213394
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'test_param': {'type': 'str', 'fallback': (env_fallback, ('TEST_PARAM_FALLBACK',))}}
    parameters = {}
    parameters.update(set_fallbacks(argument_spec, parameters))
    assert 'test_param' in parameters



# Generated at 2022-06-12 23:31:02.669130
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'param1': {'type': 'int', 'fallback': (env_fallback, ['ENV_PARAM'])},
        'param2': {'type': 'bool', 'fallback': (env_fallback, ['ENV_PARAM'])},
        'param3': {'type': 'bool', 'fallback': (env_fallback, ['ENV_PARAM'])},
        'param4': {'type': 'bool', 'fallback': (env_fallback, ['ENV_PARAM'])},
        'param5': {'type': 'bool', 'fallback': (env_fallback, ['ENV_PARAM'])}
    }
    params = {'param2': False}
    os.environ['ENV_PARAM'] = 'False'

    no_

# Generated at 2022-06-12 23:31:10.328821
# Unit test for function env_fallback
def test_env_fallback():
    with patch.dict('os.environ', {'GIT_PASSWORD': 'mypassword'}):
        assert env_fallback('GIT_PASSWORD') == 'mypassword'
    with patch.dict('os.environ', {'ANSIBLE_ENV_VAR': 'mypassword'}):
        assert env_fallback('GIT_PASSWORD', 'ANSIBLE_ENV_VAR') == 'mypassword'
    with raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_ENV_VAR')



# Generated at 2022-06-12 23:31:19.357075
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:31:26.388830
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # list fallback, env set
    argument_spec = {'a': {'type': 'str', 'fallback': ('env', ('TEST_VAR',))}}
    parameters = {}
    os.environ['TEST_VAR'] = 'foo'
    fallbacks = set_fallbacks(argument_spec, parameters)
    assert parameters['a'] == 'foo'
    assert len(fallbacks) == 0

    # list fallback, env unset
    argument_spec = {'a': {'type': 'str', 'fallback': ('env', ('TEST_VAR',))}}
    parameters = {}
    if 'TEST_VAR' in os.environ:
        del os.environ['TEST_VAR']
    fallbacks = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:31:35.751557
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'test': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST_FALLBACK')}}, {}) == set()
    assert set_fallbacks({'test': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_TEST_FALLBACK'])}}, {}) == set()
    assert set_fallbacks({'test': {'type': 'str', 'fallback': (env_fallback, ['THIS_ENV_VAR_DOES_NOT_EXIST'])}}, {}) == set()

# Generated at 2022-06-12 23:31:41.054364
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'password': {'type': 'str', 'fallback': (env_fallback, ('PASSWORD',))}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'password': 'PASSWORD'}
    assert no_log_values == set()


# Generated at 2022-06-12 23:32:10.225677
# Unit test for function env_fallback
def test_env_fallback():
    env = {}
    os.environ = env

    try:
        env_fallback()
        assert False
    except AnsibleFallbackNotFound:
        pass

    env = {'ANSIBLE_TEST': 'success'}
    os.environ = env
    assert env_fallback('ANSIBLE_TEST') == 'success'

    env = {}
    os.environ = env
    assert env_fallback('test', 'ANSIBLE_TEST') == 'success'



# Generated at 2022-06-12 23:32:14.433062
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_MODULE_ARGS'] = '{"my_variable": "my_value"}'
    assert env_fallback('ANSIBLE_MODULE_ARGS') == os.environ['ANSIBLE_MODULE_ARGS']

    del os.environ['ANSIBLE_MODULE_ARGS']
    assert env_fallback('ANSIBLE_MODULE_ARGS') == os.environ['ANSIBLE_MODULE_ARGS']

"""
Note: This function is not unit tested because it is only used in Ansible
internally and it is not possible to test it unitary.
"""

# Generated at 2022-06-12 23:32:16.854416
# Unit test for function sanitize_keys
def test_sanitize_keys():
    obj = {'super-secret-property': 'super-secret-value', '_ansible_no_log': 'yes', '_ansible_no_log_value': 'yes'}
    assert sanitize_keys(obj, ['_ansible_no_log_value'], frozenset(['_ansible_no_log'])) == {'super-secret-property': '********', '_ansible_no_log': 'yes'}



# Generated at 2022-06-12 23:32:21.724393
# Unit test for function sanitize_keys
def test_sanitize_keys():
    import json
    import pprint

    # pylint: disable=missing-docstring
    def assert_equal(data1, data2):
        data1_str = pprint.pformat(data1)
        data2_str = pprint.pformat(data2)
        if data1_str != data2_str:
            raise AssertionError('Data differs\n%s\n%s' % (data1_str, data2_str))

    def assert_sanitize_keys(old_data, no_log_strings, expected):
        for key in expected.get('ignore_keys', []):
            assert key in no_log_strings
        ignore_keys = frozenset(expected.get('ignore_keys', []))

# Generated at 2022-06-12 23:32:26.447132
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'test_param': {
            'type': 'str',
            'required': True,
            'fallback': (env_fallback, ['TEST_FALLBACK_ENV'])
        }
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['test_param'] == 'test'
    assert no_log_values == set()



# Generated at 2022-06-12 23:32:38.816723
# Unit test for function set_fallbacks
def test_set_fallbacks():

    my_arg_spec = dict(
        foo=dict(type='str', fallback=(env_fallback, 'FOO')),
        baz=dict(type='str', fallback=(env_fallback, 'BAZ')),
        fiz=dict(type='str', fallback=(env_fallback, 'FIZ', 'FIZ_INFO')),
        bar=dict(type='str', fallback=(env_fallback, 'BAR')),
        no_log=dict(type='str', fallback=(env_fallback, 'NOLOG')),
    )

    test_values = dict(
        foo='bar',
        bar='baz',
        biz='fiz',
    )

    os.environ['FOO'] = 'FOO_VALUE'

# Generated at 2022-06-12 23:32:50.329285
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        foo=dict(type='str', fallback=(env_fallback, 'FOO', 'FOO_DEFAULT')),
        bar=dict(type='int', fallback=(env_fallback, 'BAR', 'BAR_DEFAULT')),
        baz=dict(type='bool', fallback=(env_fallback, 'BAZ', 'BAZ_DEFAULT')),
        qux=dict(type='int', fallback=(env_fallback, 'QUX', 'QUX_DEFAULT', dict(key='value'))),
    )
    parameters = dict()

    os.environ['FOO'] = 'foo'
    os.environ['BAR'] = '42'
    os.environ['BAZ'] = 'true'
    os.environ['QUX'] = '42'

# Generated at 2022-06-12 23:32:53.480592
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_FOO'] = 'BAZ'
    assert env_fallback('ANSIBLE_BAR', 'ANSIBLE_FOO') == 'BAZ'
    try:
        env_fallback('ANSIBLE_BAR')
        # failed to raise exception
        assert False
    except AnsibleFallbackNotFound:
        pass



# Generated at 2022-06-12 23:32:58.642182
# Unit test for function env_fallback
def test_env_fallback():
    assert os.environ.get('HOME') or os.environ.get('HOME') == ''
    assert env_fallback('HOME') == os.environ.get('HOME')
    assert 'USER' not in os.environ 
    assert env_fallback('USER', 'HOME') == os.environ.get('HOME')
    assert env_fallback('FOO') == ''
    return True

# Generated at 2022-06-12 23:33:05.392742
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = dict()

# Generated at 2022-06-12 23:33:34.868244
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:33:46.245727
# Unit test for function set_fallbacks
def test_set_fallbacks():
    is_failed = False

# Generated at 2022-06-12 23:33:54.181362
# Unit test for function env_fallback
def test_env_fallback():
    with patch.dict(os.environ, {'ANSIBLE_STRATEGY': 'free'}):
        assert env_fallback('DOES_NOT_EXIST', 'ANSIBLE_STRATEGY') == 'free'
        assert env_fallback('DOES_NOT_EXIST', 'DOES_NOT_EXIST_EITHER') == 'DOES_NOT_EXIST_EITHER'
        try:
            env_fallback('DOES_NOT_EXIST')
        except AnsibleFallbackNotFound:
            pass
        else:
            assert False, "env_fallback failed to raise AnsibleFallbackNotFound"



# Generated at 2022-06-12 23:34:05.445885
# Unit test for function set_fallbacks
def test_set_fallbacks():

    # Testing without fallback set
    parameters = {'p1': 'p1_val'}
    argument_spec = {'p1': {'type': 'str'}}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert not no_log_values
    assert parameters == {'p1': 'p1_val'}

    # Testing with fallback set
    parameters = {'p1': 'p1_val'}
    argument_spec = {'p1': {'type': 'str'}, 'p2': {'type': 'str', 'fallback': (lambda: 'fallback_str', )}}
    set_fallbacks(argument_spec, parameters)
    assert 'fallback_str' in parameters

# Generated at 2022-06-12 23:34:12.776558
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['WANTED_VAR'] = 'value'
    assert env_fallback('WANTED_VAR') == 'value'

    os.environ['WANTED_VAR_2'] = 'value2'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NOT_WANTED_VAR')
    assert env_fallback('NOT_WANTED_VAR', 'NOT_WANTED_VAR', 'WANTED_VAR_2') == 'value2'



# Generated at 2022-06-12 23:34:14.803995
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_PORT'] = '22'
    assert env_fallback('ANSIBLE_TEST_PORT') == '22'
    assert env_fallback('ANSIBLE_TEST_PASSWD') == 'guess'


# Generated at 2022-06-12 23:34:25.598736
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test normal fallback
    argument_spec = {'password': {'fallback': (env_fallback, 'ANSIBLE_TEST_PASSWORD')}}
    parameters = {}
    os.environ['ANSIBLE_TEST_PASSWORD'] = 'test_password'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert 'password' in parameters
    assert parameters['password'] == 'test_password'
    assert 'test_password' in no_log_values

    # Test 'no_log' parameter
    argument_spec = {'password': {'fallback': (env_fallback, 'ANSIBLE_TEST_PASSWORD')}}
    parameters = {}
    os.environ['ANSIBLE_TEST_PASSWORD'] = 'test_password'
    no_log_values

# Generated at 2022-06-12 23:34:36.298095
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'a': {
            'type': 'int',
            'required': False
        },
        'b': {
            'type': 'int',
            'fallback': (env_fallback, 'FOO'),
            'required': False
        },
        'c': {
            'type': 'int',
            'fallback': (env_fallback, 'BAZ', {'my_kwarg': 'bar'}),
            'required': False
        },
    }

    parameters = {
        'a': 5,
        'b': 6,
        'c': 7,
    }

    os.environ['FOO'] = '8'
    os.environ['BAZ'] = '10'
    assert set_fallbacks(spec, parameters) == set(['8', '10'])

# Generated at 2022-06-12 23:34:38.926151
# Unit test for function env_fallback
def test_env_fallback():
    """Test function env_fallback"""

    assert env_fallback('TEST') == os.environ['TEST']
    assert env_fallback('TEST', 'TESTING') == os.environ['TEST']

    env = os.environ.copy()
    os.environ = {}
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('TEST')
    os.environ = env



# Generated at 2022-06-12 23:34:40.035869
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('VARIABLE_DOES_NOT_EXIST') == AnsibleFallbackNotFound


# Generated at 2022-06-12 23:35:07.420052
# Unit test for function set_fallbacks
def test_set_fallbacks():
    arguments_spec = dict(
        foo=dict(type='str'),
        bar=dict(type='str', fallback=('env_fallback', ['FOO_BAR'])),
        baz=dict(type='str', fallback=('env_fallback', None, dict(prefix='FOO_'))),
    )
    parameters = dict()

    try:
        set_fallbacks(arguments_spec, parameters)
        assert False
    except AnsibleFallbackNotFound:
        assert True

    os.environ["FOO_BAR"] = "This is a test"
    os.environ["FOO_BAZ"] = "This is a test"
    set_fallbacks(arguments_spec, parameters)
    assert parameters['bar'] == "This is a test"

# Generated at 2022-06-12 23:35:11.125589
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('ansible_foo_bar', 'ansible_bar_foo') == os.environ['ansible_foo_bar']
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ansible_bar_foo', 'ansible_foo_bar')



# Generated at 2022-06-12 23:35:21.390378
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit test for function set_fallbacks"""

    argument_spec = ansible_spec_loader.load_spec()
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)

    assert parameters['host_key_checking'] == 'False'
    assert parameters['gathering'] == 'implicit'
    assert parameters['command_warnings'] is True
    assert parameters['pipelining'] == 5
    assert parameters['forks'] == 5
    assert parameters['remote_tmp'] == '$HOME/.ansible/tmp'
    assert parameters['become_user'] == '$USER'
    assert parameters['become_user'] == '$USER'
    assert parameters['ansible_managed'].startswith('Ansible managed:')

# Generated at 2022-06-12 23:35:33.700932
# Unit test for function env_fallback
def test_env_fallback():
    '''
    Test that env_fallback returns a value set in the environment.
    '''
    assert to_text(env_fallback('TEST_VALUE')) == 'value'
    os.environ['TEST_VALUE'] = 'value'
    assert to_text(env_fallback('TEST_VALUE')) == 'value'
    # test that it raises exception
    try:
        env_fallback('KEY_THAT_DOES_NOT_EXIST')
        raise AssertionError('Expected an AnsibleFallbackNotFound exception')
    except AnsibleFallbackNotFound:
        pass
    # test that it raises exception on empty string
    os.environ['TEST_VALUE'] = ''

# Generated at 2022-06-12 23:35:45.850157
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_entry = []
    # test case 1
    test_entry.append({
        'spec': {'arg1': {'type': 'str', 'fallback': (env_fallback, ['ARG1'])}},
        'param': {},
        'env': {'ARG1': 'envvar_value_string'},
        'expected': {'arg1': 'envvar_value_string'}
    })
    # test case 2
    test_entry.append({
        'spec': {'arg1': {'type': 'str', 'fallback': (env_fallback, ['ARG1'])}},
        'param': {'arg1': 'param_value_string'},
        'env': {},
        'expected': {}
    })
    # test case 3

# Generated at 2022-06-12 23:35:48.015023
# Unit test for function env_fallback
def test_env_fallback():
    orig_environ = copy.deepcopy(os.environ)
    os.environ['ANSIBLE_DEBUG'] = "1"
    assert env_fallback('ANSIBLE_DEBUG') == "1"
    os.environ = orig_environ


# Generated at 2022-06-12 23:36:00.314184
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(fallback=(env_fallback, dict(vars=['FOO']), 'bar')),
        baz=dict(fallback=(env_fallback, dict(vars=['BAZ']))),
        qux=dict(fallback=(env_fallback, dict(vars=['QUX']))),
        quux=dict(fallback=(env_fallback, dict(vars=['QUUX']))),
        corge=dict(fallback=(env_fallback, dict(vars=['CORGE']))),
    )

    for x in (2, 3):
        parameters = dict(
            foo='foo',
            baz='baz',
        )

        test_lst = []
        test_lst.append(parameters)
        test_

# Generated at 2022-06-12 23:36:04.800977
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_STRATEGY'] = 'free'
    ret = env_fallback('ANSIBLE_STRATEGY')
    assert ret == 'free'



# Generated at 2022-06-12 23:36:06.065027
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback("HOME") == os.environ['HOME']


# Generated at 2022-06-12 23:36:11.779880
# Unit test for function env_fallback
def test_env_fallback():
    # Test missing env
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('FOO')

    # Test env exists
    os.environ['FOO'] = 'bar'
    assert env_fallback('FOO') == 'bar'

    # Test multiple env with one exists
    os.environ['FOO'] = 'bar'
    assert env_fallback('FOO', 'BAR') == 'bar'



# Generated at 2022-06-12 23:36:37.689310
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        test_typed_fallback=dict(type='str', fallback=(env_fallback, 'TEST_TYPED_FALLBACK')),
        test_untyped_fallback=dict(fallback=(env_fallback, 'TEST_UNTYPED_FALLBACK')),
        test_untyped_fallback_with_type=dict(type='list', fallback=(env_fallback, 'TEST_UNTYPED_FALLBACK_WITH_TYPE')),
        test_multiple_fallback=dict(type='str', fallback=('__file__', env_fallback, 'TEST_MULTIPLE_FALLBACK')),
    )
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:36:48.910117
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:36:54.300313
# Unit test for function env_fallback
def test_env_fallback():
    """Unit test for function env_fallback"""
    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
    assert env_fallback('ANSIBLE_HOST_KEY_CHECKING',
                        'SOME_OTHER_UNSET_ENV_VARIABLE') == 'False'

    os.environ['SOME_OTHER_UNSET_ENV_VARIABLE'] = 'True'
    assert env_fallback('SOME_OTHER_UNSET_ENV_VARIABLE') == 'True'

    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('SOME_OTHER_UNSET_ENV_VARIABLE_2')



# Generated at 2022-06-12 23:37:04.822615
# Unit test for function env_fallback
def test_env_fallback():
    '''Test function for env_fallback'''
    # def env_fallback(*args, **kwargs):
    assert(env_fallback('HOME') == os.environ['HOME'])
    assert(env_fallback('AWS_SECRET_KEY') == 'my_aws_secret_key')
    os.environ['AWS_SECRET_KEY'] = 'my_aws_secret_key'
    assert(env_fallback('AWS_SECRET_KEY') == 'my_aws_secret_key')
    assert(env_fallback('ASDFASDFASDFASDFASDF') == None)


# Generated at 2022-06-12 23:37:11.276297
# Unit test for function env_fallback
def test_env_fallback():
    tests = [
        dict(
            args=['test'],
            env={'test': '1'},
            expected=1
        ),
        dict(
            args=[],
            env={},
            expected=AnsibleFallbackNotFound
        )
    ]

    for test in tests:
        try:
            actual = env_fallback(*test['args'])
        except Exception as e:
            actual = type(e)

        if isinstance(actual, string_types):
            actual = actual.decode('utf-8')

        assert actual == test['expected'], "Expected: %s, Actual: %s" % (test['expected'], actual)



# Generated at 2022-06-12 23:37:15.267305
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('FAKE') == os.environ['FAKE']
    assert env_fallback('FAKE', 'FAKE2') == os.environ['FAKE']



# Generated at 2022-06-12 23:37:24.475315
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # No fallback
    argument_spec = {
        'param1': {},
    }
    parameters = {'param1': 'good'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters['param1'] == 'good'

    # With fallback
    argument_spec = {
        'param1': {
            'type': 'str',
            'fallback': (env_fallback, ('ENV1',))
        },
    }
    os.environ['ENV1'] = 'env1'
    parameters = {'param2': 'good'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0

# Generated at 2022-06-12 23:37:36.468658
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'param1':{'type':'str','default':'xyz','no_log': False}, 'param2':{'type':'str','fallback':(env_fallback,'my_param')}}, {}) == set()
    assert set_fallbacks({'param1':{'type':'str','default':'xyz','no_log': False}, 'param2':{'type':'str','fallback':(env_fallback,'my_param')}}, {'param1':'abc'}) == set()