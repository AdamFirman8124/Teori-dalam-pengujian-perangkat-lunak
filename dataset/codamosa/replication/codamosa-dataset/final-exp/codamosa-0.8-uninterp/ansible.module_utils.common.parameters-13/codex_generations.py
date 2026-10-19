

# Generated at 2022-06-12 23:28:30.111976
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST_ENV_FALLBACK'] = 'test'
    assert env_fallback('TEST_ENV_FALLBACK') == 'test'
    os.environ['TEST_ENV_FALLBACK'] = 'test'
    assert env_fallback('TEST_ENV_FALLBACK', 'TEST_ENV_FALLBACK1') == 'test'
    os.environ['TEST_ENV_FALLBACK1'] = 'test'
    assert env_fallback('TEST_ENV_FALLBACK2', 'TEST_ENV_FALLBACK1') == 'test'
    os.environ.pop('TEST_ENV_FALLBACK')
    os.environ.pop('TEST_ENV_FALLBACK1')
    os.environ

# Generated at 2022-06-12 23:28:39.752576
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'a': {'fallback': ('env_fallback', 'FOO_BAR')}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['a'] == 'FOO_BAR'
    assert not no_log_values
    os.environ.pop('FOO_BAR', None)
    os.environ['FOO_BAR2'] = 'hello'
    argument_spec = {'a': {'fallback': ('env_fallback', 'FOO_BAR', 'FOO_BAR2')}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['a'] == 'hello'
    assert not no_log_values

# Generated at 2022-06-12 23:28:45.998259
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'param1': {'type': 'bool', 'required': True, 'default': False},
        'param2': {'type': 'str', 'fallback': (env_fallback, ['SOME_VAR'])},
        'param3': {'type': 'str', 'fallback': (env_fallback, ['SOME_VAR', 'SOME_OTHER_VAR'])},
        'param4': {'type': 'bool', 'required': True, 'default': False, 'fallback': (env_fallback, ['SOME_VAR'])},
        'param5': {'type': 'str', 'fallback': (env_fallback, ['SOME_VAR'])},
    }
    parameters = {
        'param1': True
    }
    fallback_

# Generated at 2022-06-12 23:28:50.818564
# Unit test for function remove_values

# Generated at 2022-06-12 23:29:02.594652
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(xd1=dict(fallback=(env_fallback, 'XD1', 'XD2')))
    parameters = dict()
    os.environ['XD1'] = 'env_fallback'

    # Test fallback
    assert os.environ['XD1'] == 'env_fallback'
    assert 'xd1' not in parameters
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert 'xd1' in parameters
    assert parameters['xd1'] == 'env_fallback'
    assert no_log_values == set()

    # Test that no fallback log value was returned
    os.environ['XD1'] = ''
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert 'xd1' not in parameters


# Generated at 2022-06-12 23:29:10.244623
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        state=dict(type='str', default='present'),
        name=dict(type='str', required=True, fallback=(env_fallback, ['ANSIBLE_NET_USERNAME'])),
        password=dict(type='str', required=True, fallback=(env_fallback, ['ANSIBLE_NET_PASSWORD'])),
        provider=dict(),
    )
    parameters = dict(provider=dict(password=None), state='present')

    assert set() == set_fallbacks(argument_spec, parameters)
    assert 'present' == parameters['state']
    assert '' == parameters['name']
    assert '' == parameters['password']



# Generated at 2022-06-12 23:29:16.159085
# Unit test for function set_fallbacks
def test_set_fallbacks():
    module_args = dict(
        test_string_fallback='test_string',
        test_int_fallback='10',
        test_bool_fallback='false',
        test_default_fallback='20',
        test_unset_fallback='30',
        test_env_fallback='4',
        test_env_fallback_kwargs='5',
        test_load_file_fallback='/etc/passwd',
        test_fail_fallback='not used',
    )

# Generated at 2022-06-12 23:29:28.342931
# Unit test for function env_fallback
def test_env_fallback():
    """Test for function env_fallback"""
    # Test basic functionality with one name
    os.environ['ANSIBLE_TEST1'] = 'yep'
    assert env_fallback('ANSIBLE_TEST1') == 'yep'
    os.environ['ANSIBLE_TEST1'] = 'maybe'
    assert env_fallback('ANSIBLE_TEST1') == 'maybe'
    os.environ['ANSIBLE_TEST1'] = 'nope'
    assert env_fallback('ANSIBLE_TEST1') == 'nope'
    del os.environ['ANSIBLE_TEST1']
    try:
        env_fallback('ANSIBLE_TEST1')
        assert False, 'Should have raised an exception'
    except AnsibleFallbackNotFound:
        pass
    # Now try without setting

# Generated at 2022-06-12 23:29:39.731434
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_arguments = dict(
        parameter1=dict(fallback=(env_fallback, 'TEST_F1', 'TEST_F2')),
        parameter2=dict(fallback=(env_fallback, ['TEST_F3', 'TEST_F4'])),
        parameter3=dict(fallback=(env_fallback, dict(var='TEST_F5', true_val='yes', false_val='no'))),
        parameter4=dict(fallback=(env_fallback, dict(var=['TEST_F5', 'TEST_F6']))),
    )
    os.environ['TEST_F1'] = '1'
    os.environ['TEST_F3'] = '3'
    os.environ['TEST_F5'] = 'true'
   

# Generated at 2022-06-12 23:29:49.188375
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Python 3.9 has a different class for ordered dict, so need to compare
    # the class type as well.
    if sys.version_info[:2] == (3, 9):
        class_type = type(OrderedDict())
        assert class_type(set_fallbacks({'spam': {'type': 'str', 'default': 'green', 'fallback': (env_fallback, 'SPAM', 'SPAM_NOT_SET')}}, {})) == class_type({'spam': 'green'})
    else:
        assert set_fallbacks({'spam': {'type': 'str', 'default': 'green', 'fallback': (env_fallback, 'SPAM', 'SPAM_NOT_SET')}}, {}) == OrderedDict([('spam', 'green')])

    # Make

# Generated at 2022-06-12 23:30:16.178784
# Unit test for function set_fallbacks
def test_set_fallbacks():
    task_vars = dict(
        ansible_connection='local',
        ansible_python_interpreter='python',
        ansible_playbook_python='python',
        ansible_version={},
        ansible_ssh_user='test',
        ansible_ssh_pass='pass',
        ansible_sudo_pass='sudo',
        ansible_shell_executable='bash',
        ansible_shell_type='sh',
        ansible_python_interpreter='python',
        ansible_bin_dir='/bin',
        ansible_become_method='sudo',
        ansible_become_user='root',
        ansible_become_password='become',

    )
    module_name = 'command'

# Generated at 2022-06-12 23:30:24.438146
# Unit test for function env_fallback
def test_env_fallback():
    import tempfile

    # Test fallback not found
    try:
        env_fallback('missing')
    except AnsibleFallbackNotFound:
        pass
    else:
        assert False
    try:
        env_fallback('missing', 'anthing')
    except AnsibleFallbackNotFound:
        pass
    else:
        assert False

    # Test env var return value
    (fd, env_file) = tempfile.mkstemp()
    with open(env_file, 'w') as f:
        f.write('export TEST_ENV_FALLBACK=test_env_fallback\n')
    # For some reason we can't import os.environ from unit tests
    old_env = dict(os.environ)

# Generated at 2022-06-12 23:30:28.701204
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_ENV_FALLBACK'] = 'example'
    assert env_fallback('ANSIBLE_TEST_ENV_FALLBACK') == 'example'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANOTHER_ENV')



# Generated at 2022-06-12 23:30:39.698726
# Unit test for function sanitize_keys
def test_sanitize_keys():
    actual_key_names = {'password': 'PASSWORD', 'access_key': 'ACCESS_KEY', 'secret_key': 'SECRET_KEY', 'aws_secret_key': 'AWS_SECRET_KEY', 'new_user_password': 'NEW_USER_PASSWORD', 'db_password': 'DB_PASSWORD', 'become_password': 'BECOME_PASSWORD', 'vault_password': 'VAULT_PASSWORD'}

# Generated at 2022-06-12 23:30:44.125013
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST_ENV'] = 'TEST ENV'
    assert env_fallback('TEST_ENV', 'TEST_ENV_NOT_FOUND') == 'TEST ENV'
    del os.environ['TEST_ENV']
    assert env_fallback('TEST_ENV', 'TEST_ENV_NOT_FOUND') == 'TEST_ENV_NOT_FOUND'



# Generated at 2022-06-12 23:30:55.950240
# Unit test for function set_fallbacks
def test_set_fallbacks():
    module = AnsibleModule(argument_spec={'test': dict(fallback=('env', ('HOME', 'HOME'), {'default': None}))})
    assert module._debug is False
    assert module.params.get('test') == os.environ.get('HOME')

    module = AnsibleModule(argument_spec={'test': dict(fallback=('env', ('FOO', 'FOO'), {'default': None}))})
    assert module._debug is False
    assert module.params.get('test') is None

    module = AnsibleModule(argument_spec={'test': dict(fallback=('env', ('FOO', 'FOO'), {'required': True}))})
    assert module._debug is False
    # assert module._failed is True
    # assert 'parameter "test" is required' in module.fail_

# Generated at 2022-06-12 23:31:03.270787
# Unit test for function remove_values
def test_remove_values():
    return

# Generated at 2022-06-12 23:31:08.023946
# Unit test for function set_fallbacks
def test_set_fallbacks():
    fallbacks = {
        'no_log': False,
        'fallback': [env_fallback, 'non_existent_env'],
    }
    no_log_values = set_fallbacks({'arg': fallbacks}, {})
    assert len(no_log_values) == 0

    fallbacks = {
        'no_log': False,
        'fallback': [env_fallback, 'non_existent_env1', 'non_existent_env2'],
    }
    no_log_values = set_fallbacks({'arg': fallbacks}, {})
    assert len(no_log_values) == 0



# Generated at 2022-06-12 23:31:18.207082
# Unit test for function remove_values
def test_remove_values():

    # First, test 'remove_values' on a single level
    data = {
        'the_secret': 'password',
        'the_other_secret': 'password is "foo"',
        'the_list_secret': ['password', ['foo', 'password']],
        'the_dict_secret': {'key': 'password', 'bar': 'password', 'baz': ['foo', 'password']},
        'the_list_dict_secret': [{'key': 'password', 'bar': 'password', 'baz': ['foo', 'password']}, {'foo': 'foo'}],
        'the_set': set(['password']),
        'the_frozenset': frozenset(['password']),
        'the_wrong_type': 'password'
    }


# Generated at 2022-06-12 23:31:24.160941
# Unit test for function env_fallback
def test_env_fallback():
    if not os.environ.get('ANSIBLE_TEST_FALLBACK_ENV'):
        return

    os.environ['ANSIBLE_TEST_TXT'] = 'ANSIBLE_TEST_TXT'
    assert env_fallback('ANSIBLE_TEST_TXT') == os.environ['ANSIBLE_TEST_TXT']
    try:
        env_fallback('NOT_DEFINED')
        assert False
    except AnsibleFallbackNotFound:
        pass



# Generated at 2022-06-12 23:31:51.465675
# Unit test for function set_fallbacks
def test_set_fallbacks():
    import os
    os.environ['ANSIBLE_NET_USERNAME'] = 'admin'
    os.environ['ANSIBLE_NET_PASSWORD'] = 'password'
    os.environ['ANSIBLE_NET_HOST'] = 'localhost'


# Generated at 2022-06-12 23:32:01.527421
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        "ansible_connection": {
            "type": "str",
            "choices": ["docker", "winrm", "ssh", "paramiko", "local"],
            "fallback": (
                env_fallback,
                ["ANSIBLE_CONNECTION"],
                [
                    "ansible_connection_type",
                    {
                        "ansible_ssh": "ssh",
                        "ansible_winrm": "winrm",
                        "ansible_paramiko": "paramiko",
                    },
                ],
            )
        }
    }
    parameters = {}

    # When empty parameters, get connection type from environment
    os.environ['ANSIBLE_CONNECTION'] = 'docker'
    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:32:03.817083
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('HI') == os.environ['HI']


# Generated at 2022-06-12 23:32:14.513902
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:32:20.953518
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(test1=dict(default='hello'))
    params = dict()
    assert set_fallbacks(argument_spec, params) == set()
    assert params['test1'] == 'hello'
    try:
        set_fallbacks(argument_spec, dict(test1=dict()))
        assert False, 'should fail'
    except TypeError:
        pass
    params = dict()
    argument_spec = dict(test1=dict(fallback=(env_fallback, 'ANS_TEST_1',
                                              dict(fallback=(env_fallback, 'ANS_TEST_2')))))
    os.environ['ANS_TEST_1'] = 'world'
    no_log_values = set_fallbacks(argument_spec, params)

# Generated at 2022-06-12 23:32:30.050023
# Unit test for function sanitize_keys
def test_sanitize_keys():
    try:
        import redis
    except ImportError:
        pytest.skip()
    r = redis.Redis(host='localhost', port=6379, db=0)
    container = {'no_log_value': 'password1', 'password1': 'password1', 'password2': 'password2',
                 'redis': r, 'no_log': True, 'redis2': r}
    data = sanitize_keys(container, no_log_strings=['password1'])
    assert data.keys() == set(['no_log_value', '__password1__', 'password2', 'redis', 'no_log', 'redis2'])
    assert data['__password1__'] == 'password1'



# Generated at 2022-06-12 23:32:40.910537
# Unit test for function env_fallback
def test_env_fallback():
    test_name = __name__ + '.test_env_fallback'
    env = deepcopy(os.environ)

# Generated at 2022-06-12 23:32:52.287351
# Unit test for function set_fallbacks
def test_set_fallbacks():
    arg_spec = dict(
        param_1=dict(type='str', fallback=(env_fallback, 'ANSIBLE_TEST_VAR')),
        param_2=dict(type='str', required=True)
    )

    class FakeOs(object):
        def __init__(self, environ):
            self.environ = environ

        def __getitem__(self, i):
            return self.environ[i]

    os_environ = {
        'ANSIBLE_TEST_VAR': 'value 1',
    }

    parameters = dict()
    no_log_set = set()

    # Make sure fallback values are set from os.environ
    with patch('os.environ', new=FakeOs(os_environ)):
        no_log_set = set_fallbacks

# Generated at 2022-06-12 23:32:58.421245
# Unit test for function env_fallback
def test_env_fallback():
    ''' Test env_fallback function '''
    # setup
    os.environ['MYTEST'] = 'test1'
    os.environ['MYTEST2'] = 'test2'
    expected = 'test1'
    # test
    result = env_fallback('MYTEST', 'MYTEST2')
    # assert
    assert result == expected
    os.unsetenv('MYTEST')
    os.unsetenv('MYTEST2')

# Generated at 2022-06-12 23:33:05.847836
# Unit test for function sanitize_keys
def test_sanitize_keys():
    foo = {'bar': {'baz': 'foobar', 'barbaz': [{'password': 'bar'}, 'bar', [{'password': 'foo'}, 'foo']]}}

    assert sanitize_keys(foo, ['password']) == {'bar': {'baz': 'foobar', 'barbaz': [{'****': 'bar'}, 'bar', [{'****': 'foo'}, 'foo']]}}



# Generated at 2022-06-12 23:33:37.362146
# Unit test for function env_fallback
def test_env_fallback():
    try:
        env_fallback('ANSIBLE_FOO')
        raise Exception('Expected exception to be raised')
    except AnsibleFallbackNotFound:
        pass
    os.environ['ANSIBLE_FOO'] = 'foo'
    assert env_fallback('ANSIBLE_FOO') == 'foo'



# Generated at 2022-06-12 23:33:48.146567
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_NET_SSH_PASSWORD'] = 'foo'
    assert 'foo' == env_fallback('ANSIBLE_NET_SSH_PASSWORD', 'ANSIBLE_NET_PASSWORD')
    os.environ.pop('ANSIBLE_NET_SSH_PASSWORD')
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_NET_SSH_PASSWORD', 'ANSIBLE_NET_PASSWORD')
    os.environ['ANSIBLE_NET_SSH_PASSWORD'] = 'foo'
    assert 'foo' == env_fallback('ANSIBLE_NET_PASSWORD')
    os.environ.pop('ANSIBLE_NET_SSH_PASSWORD')



# Generated at 2022-06-12 23:33:51.852704
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('HELLO') == os.environ['HELLO']
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('HELLO', 'WORLD')


# Generated at 2022-06-12 23:33:59.151000
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        param1=dict(type='str', fallback=(env_fallback, "PARAM1",)),
        param2=dict(type='int', fallback=(env_fallback, "PARAM2", {'key': 'val'})),
    )
    parameters = dict()
    no_log_values = set_fallbacks(spec, parameters)

    assert parameters['param1'] == 'val1'
    assert parameters['param2'] == 42
    assert no_log_values == set()



# Generated at 2022-06-12 23:34:04.566493
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """Unit test for function sanitize_keys"""
    assert sanitize_keys('foo', ['foo']), 'foo'
    assert sanitize_keys(['foo'], ['foo']), ['foo']
    assert sanitize_keys(['foo', 'bar'], ['foo', 'bar']), ['foo', 'bar']
    assert sanitize_keys({'foo': 'bar'}, ['foo', 'bar']), {'foo': 'bar'}
    assert sanitize_keys({'foo': 'bar', 'ignore_me': 'bar', '_ansible_ignore': 'bar'}, ['foo', 'bar']), {'foo': 'bar', 'ignore_me': 'bar', '_ansible_ignore': 'bar'}

# Generated at 2022-06-12 23:34:13.731968
# Unit test for function sanitize_keys
def test_sanitize_keys():
    values = dict(
        dict_v=dict(
            dict_v_dict_k=dict(
                dict_v_dict_k_dict_k='dict_v_dict_k_dict_v'
            ),
            dict_v_dict_k2='dict_v_dict_k2'
        ),
        dict_v2=dict(
            dict_v2_dict_k='dict_v2_dict_k'
        ),
        dict_v3='dict_v3'
    )

    assert sanitize_keys(values, []) == values

# Generated at 2022-06-12 23:34:24.176947
# Unit test for function remove_values
def test_remove_values():
    def try_remove_values(value, no_log_strings):
        return remove_values(value, no_log_strings)

    # Tests where value type is a string
    assert try_remove_values('', ['']) == ''
    assert try_remove_values('a', ['']) == 'a'
    assert try_remove_values('', ['a']) == ''
    assert try_remove_values('abcdefg', ['abcdefg']) == ''
    assert try_remove_values('abcdefg', ['cde']) == 'abfg'
    assert try_remove_values('abcdefg', ['cdefgh']) == 'ab'
    assert try_remove_values('abcdefg', ['e']) == 'abcdg'

    # Tests where value type is a list

# Generated at 2022-06-12 23:34:32.190346
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'a':{'type':str}, 'b':{'type':str, 'fallback':('something', ['c'])}}, {'a':'hello'}) == set()
    assert set_fallbacks({'a':{'type':str}, 'b':{'type':str, 'fallback':('something', ['c'])}}, {'a':'hello', 'b':'world'}) == set()
    assert set_fallbacks({'a':{'type':str}, 'b':{'type':str, 'fallback':('something', [{'d':'c'}])}}, {'a':'hello'}) == set()

# Generated at 2022-06-12 23:34:41.815352
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        test1 = dict(fallback=['test1_fallback']),
        test2 = dict(fallback=['test2_fallback']),
        test3 = dict(fallback=['test3_fallback']),
        test4 = dict(fallback=['test4_fallback']),
        test5 = dict(fallback=['test5_fallback']),
        test6 = dict(fallback=[env_fallback, 'TEST6_FALLBACK']),
        test7 = dict(fallback=[env_fallback, 'TEST7_FALLBACK']),
    )
    parameters = dict()
    os.environ['TEST6_FALLBACK'] = 'value6'
    os.environ['TEST7_FALLBACK'] = 'value7'
    no

# Generated at 2022-06-12 23:34:52.113044
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'foo': {'type': 'str', 'fallback': (env_fallback, 'FOO')},
                     'bar': {'type': 'dict', 'options': {'password': {'type': 'str', 'no_log': True}}}}
    parameters = {'foo': 'false'}
    assert not set_fallbacks(argument_spec, parameters)
    parameters = {}

    def raise_not_found(*args, **kwargs):
        raise AnsibleFallbackNotFound

    argument_spec['baz'] = {'type': 'str', 'fallback': (raise_not_found, 'BAZ')}
    assert not set_fallbacks(argument_spec, parameters)
    parameters = {'baz': 'hello'}
    assert not set_fallbacks(argument_spec, parameters)
   

# Generated at 2022-06-12 23:35:32.478964
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:35:44.686079
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        arg1=dict(type='str', fallback=(env_fallback, 'myenv')),
        arg2=dict(type='str'),
        arg3=dict(type='str', fallback=(env_fallback, 'myenv', 'default')),
        arg4=dict(type='str', no_log=True, fallback=(env_fallback, 'myenv', 'default')),
        arg5=dict(type='str', no_log=True, fallback=(env_fallback, 'myenv', 'default', dict(key='val'))),
    )
    parameters = dict(arg2='value2')
    os.environ['myenv'] = 'value1'

    # noinspection PyUnusedLocal

# Generated at 2022-06-12 23:35:52.162829
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback function"""
    # No args
    assert env_fallback() == env_fallback.__defaults__[0]
    # Existing environment variable
    os.environ['ANSIBLE_NETCONF_SSH_CONFIG'] = 'test'
    assert env_fallback('ANSIBLE_NETCONF_SSH_CONFIG') == 'test'
    del os.environ['ANSIBLE_NETCONF_SSH_CONFIG']
    # Non-existing environment variable
    assert env_fallback('UNKOWN_VAR') == env_fallback.__defaults__[0]
    # Non-string fallback value

# Generated at 2022-06-12 23:36:02.398500
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        A=dict(type='str', fallback=(env_fallback, ['ANSIBLE_A'])),
        B=dict(type='str', fallback=(env_fallback, ['ANSIBLE_B'])),
        C=dict(type='dict', fallback=(env_fallback, [dict(upcase=True)]))
    )

    os.environ['ANSIBLE_A'] = 'foo'
    os.environ['ANSIBLE_B'] = 'foo'
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters.get('A') == 'foo'
    assert parameters.get('B') == 'foo'


# Generated at 2022-06-12 23:36:07.920387
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = {
        "param1": {
            "type": "int",
            "fallback": (env_fallback, ("ANSIBLE_PARAM1", {})),
        }
    }

    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert len(no_log_values) == 0
    assert 'param1' in parameters
    assert parameters['param1'] == 10



# Generated at 2022-06-12 23:36:16.343869
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'test_key1': {'type': 'str', 'fallback': (env_fallback, 'TEST_ENV_1', 'TEST_ENV_2')},
                     'test_key2': {'type': 'str', 'fallback': (env_fallback, ['TEST_ENV_3', 'TEST_ENV_4'])},
                     'test_key3': {'type': 'str', 'fallback': (env_fallback, 'TEST_ENV_5'), 'no_log': True},
                     'test_key4': {'type': 'str', 'fallback': (env_fallback, 'TEST_ENV_6', {'some_param': 'some_value'})}}
    parameters = {}

# Generated at 2022-06-12 23:36:20.250911
# Unit test for function set_fallbacks
def test_set_fallbacks():
    actual_result = set_fallbacks(
        argument_spec={'a': {'type': 'str', 'fallback': (env_fallback, 'FOO')}},
        parameters={}
    )
    expected_result = {'value'}
    assert actual_result == expected_result



# Generated at 2022-06-12 23:36:28.180752
# Unit test for function env_fallback
def test_env_fallback():
    ''' test env_fallback '''
    os.environ["FOO"] = "1"
    os.environ["FOOBAR"] = "2"
    assert env_fallback("FOO") == "1"
    assert env_fallback("FOOBAR") == "2"
    assert env_fallback("BAR") == "2"
    assert env_fallback("BAR","FOO") == "1"
    assert env_fallback("BAR", "BARFOO") == "1"
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback("BARFOO")



# Generated at 2022-06-12 23:36:35.905039
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test with empty spec
    empty_spec = {}
    assert set_fallbacks(empty_spec, {}) == set()

    # Test with missing options
    test_spec = dict(
        param1=dict(type='int', fallback=(env_fallback, 'param1'), no_log=True),
        param2=dict(type='int', fallback=(env_fallback, 'param2'), no_log=True),
        param3=dict(type='int', fallback=(env_fallback, 'param3'), no_log=True),
        param4=dict(type='int', fallback=(env_fallback, 'param4'), no_log=True),
    )
    parameters = dict(
        param2=2,
    )
    os.environ['param1'] = '1'
    os.en

# Generated at 2022-06-12 23:36:47.043043
# Unit test for function set_fallbacks