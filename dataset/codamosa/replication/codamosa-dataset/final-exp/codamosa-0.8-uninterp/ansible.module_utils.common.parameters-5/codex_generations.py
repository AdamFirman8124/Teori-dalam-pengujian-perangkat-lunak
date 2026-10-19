

# Generated at 2022-06-12 23:28:17.846497
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # TODO: This test should be expanded to ensure we generate the correct
    # fallback values and correct missing values.
    argument_spec = {'param': {'fallback': (env_fallback, ['PARAM1'], {}),
                               'type': 'str'},
                     'param2': {'fallback': (env_fallback, ['PARAM2'], {}),
                                'type': 'str'}}
    parameters = {'param': 'test', 'param2': None}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['param'] == 'test'
    assert parameters['param2'] == 'test2'
    assert no_log_values == set()



# Generated at 2022-06-12 23:28:22.831127
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback"""

    # Test fallback for a simple variable
    os.environ['SIMPLE_VAR'] = 'test'
    result = env_fallback('SIMPLE_VAR')
    assert result == 'test'

    # Test fallback for a variable used in Ansible
    os.environ['ANSIBLE_VAR'] = 'ansible'
    result = env_fallback('ANSIBLE_VAR')
    assert result == 'ansible'

    # Test fallback for a variable not in os.environ
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NON_EXISTANT_VAR')



# Generated at 2022-06-12 23:28:24.665245
# Unit test for function env_fallback
def test_env_fallback():
    with mock.patch.dict(os.environ, {'A': 'B'}, clear=True):
        assert 'B' == env_fallback('A')



# Generated at 2022-06-12 23:28:28.749677
# Unit test for function env_fallback
def test_env_fallback():
    assert "test" == env_fallback('test')
    assert "test" == env_fallback('test', 'test1')
    assert "test" == env_fallback('test', 'test1', 'test2')
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('test1', 'test2', 'test3')

# FIXME: this should probably be removed and the behavior changed to an error

# Generated at 2022-06-12 23:28:37.490087
# Unit test for function set_fallbacks
def test_set_fallbacks():

    def custom_fallback(fallback_value):
        if fallback_value == 'my_fallback':
            return 'foo'
        else:
            raise AnsibleFallbackNotFound

    argument_spec = {
        'param1': {'type': 'str', 'fallback': (env_fallback, 'MY_FALLBACK_PARAM')},
        'param2': {'type': 'str', 'fallback': (custom_fallback, 'my_fallback')},
        'param3': {'type': 'str', 'fallback': (env_fallback, 'MY_MISSING_PARAM')},
        'param4': {'type': 'str', 'fallback': (custom_fallback, 'my_missing_value')},
    }

    parameters = {'param1': ''}

    no_

# Generated at 2022-06-12 23:28:48.757385
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_argument_spec = dict(
        a=dict(required=False, fallback=(env_fallback, 'FOO')),
        b=dict(required=False, fallback=('FOO',)),
        c=dict(required=False, fallback=(dict(fallback_host=env_fallback, fallback_host_variable='FOO'), 'FOO', dict(fallback_port=env_fallback, fallback_port_variable='FOO'))),
        d=dict(required=False, fallback=(env_fallback,)),
    )
    test_parameters = dict(
        a=None,
        b=None,
        c=None,
        d=None,
    )
    set_fallbacks(test_argument_spec, test_parameters)

# Generated at 2022-06-12 23:28:53.289379
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test when parameter value is empty
    argument_spec = dict(test=dict(required=False, type='dict', fallback=('env_fallback', 'test_env')))
    parameters = dict()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters.get('test') == {}

    # Test when parameter value is not empty
    argument_spec = dict(test=dict(required=False, type='dict', fallback=('env_fallback', 'test_env')))
    parameters = dict(test='value')
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters['test'] == 'value'

    # Test when parameter value is not empty and no_

# Generated at 2022-06-12 23:29:04.247122
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'foo': {'type': 'str', 'fallback': ('env_fallback', 'FOO')}}, {}) == {'foo': os.environ['FOO']}
    assert set_fallbacks({'foo': {'type': 'str', 'fallback': ('env_fallback', 'FOO')}}, {'foo': 'bar'}) == {}
    assert set_fallbacks({'foo': {'type': 'str', 'fallback': ('env_fallback', 'FOO', 'bar')}}, {}) == {'foo': 'bar'}
    assert set_fallbacks({'foo': {'type': 'str', 'fallback': ('env_fallback', 'FOO', {'key': 'bar'})}}, {}) == {'foo': 'bar'}

# Generated at 2022-06-12 23:29:11.415449
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = dict(
        x1=dict(fallback=(str, ['a', 'b']))
    )

    parameters = dict(
        x1='foo',
        x2='bar',
    )

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['x1'] == 'foo'
    assert len(no_log_values) == 0

    parameters = dict(
        x2='bar',
    )

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['x1'] == 'a'
    assert len(no_log_values) == 0



# Generated at 2022-06-12 23:29:19.460040
# Unit test for function set_fallbacks
def test_set_fallbacks():
    arg_spec = {'name' : {'required': False, 'default': 'John', 'fallback': (env_fallback, ['ANSIBLE_KITCHEN'], {'default': "Paul"})},
                'last_name': {'required': False, 'fallback': (env_fallback, ['ANSIBLE_BATHROOM'])}}

    parameters = {}
    no_log_values = set_fallbacks(arg_spec, parameters)
    assert parameters['name'] == 'John'
    assert parameters['last_name'] == 'Paul'
    assert 'Paul' in no_log_values
    assert len(no_log_values) == 1



# Generated at 2022-06-12 23:29:42.886830
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys({'my_key_1': {'my_key_2': 'my_value_2'}}, ['my_value_1']) == {'my_key_1': {'my_key_2': 'my_value_2'}}



# Generated at 2022-06-12 23:29:46.009001
# Unit test for function env_fallback
def test_env_fallback():
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('MISSING_ENV_VAR')
    assert 'USER' == env_fallback('USER', 'SUDO_USER', 'CURRENT_USER')


# Generated at 2022-06-12 23:29:55.454876
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {'port': {'type': 'int', 'default': 12, 'fallback': (env_fallback, 'ANSIBLE_CONNECTION_PORT')}}
    params = {'host': 'localhost'}
    assert set_fallbacks(spec, params) == set()
    assert params == {'host': 'localhost', 'port': 12}

    # Test if we can use a dictionary as the only argument
    spec = {'port': {'type': 'int', 'default': 12, 'fallback': (env_fallback, {'default': 17})}}
    params = {'host': 'localhost'}
    assert set_fallbacks(spec, params) == set()
    assert params == {'host': 'localhost', 'port': 12}

    # Test fallback value

# Generated at 2022-06-12 23:30:03.200688
# Unit test for function env_fallback
def test_env_fallback():
    assert(env_fallback('foo') == os.environ['foo'])
    assert(env_fallback('foo', 'bar') == os.environ['foo'])
    assert(env_fallback('foo', 'bar', 'baz') == os.environ['foo'])
    assert_raises(AnsibleFallbackNotFound, env_fallback, 'foo', 'bar', 'baz', 'x')


# Generated at 2022-06-12 23:30:07.842719
# Unit test for function remove_values
def test_remove_values():
    no_log_strings = [u'abc', u'def']
    llist = [u'abc',{u'abc':u'def'},[u'ghi',{u'def':u'jkl'}],[u'mno',{u'pqr':[u'stu',u'vwx',u'yz',u'foo']},{u'bar':u'baz'}]]
    dict = {u'ghi': {u'abc':u'def'}}
    list = [u'abcdef',u'abcdefghi',u'abcdefghijk']
    #container= [ container1, container2 ]
    container = [llist,dict]
    print(remove_values(llist,no_log_strings))
    print(remove_values(dict,no_log_strings))

# Generated at 2022-06-12 23:30:18.235309
# Unit test for function remove_values
def test_remove_values():
    """Test for a successful removal of the 'no_log_values' from a dictionary."""

# Generated at 2022-06-12 23:30:27.553220
# Unit test for function sanitize_keys
def test_sanitize_keys():
    no_log_strings = ['foo', 'bar']
    ignore_keys = frozenset(['foo'])
    obj = {
            'foo': 'foo',
            'bar': 'bar',
            'baz': 'baz',
            'qux': 'qux',
            'quux': {
                'foo': 'foo',
                'bar': 'bar',
                'corge': 'corge',
                'grault': [{'foo': 'foo', 'bar': 'bar', 'garply': 'garply'}]
                }
            }

# Generated at 2022-06-12 23:30:38.790457
# Unit test for function set_fallbacks
def test_set_fallbacks():

    from collections import OrderedDict

    argument_spec = OrderedDict()
    argument_spec.update(dict(
        a=dict(type='str', default='test_a'),
        b=dict(type='str', default='test_b'),
        c=dict(type='str', no_log=True, default='test_c'),
        d=dict(type='str', fallback=(env_fallback, 'D')),
        e=dict(type='str', fallback=(env_fallback, ('E', 'x'))),
        f=dict(type='str', fallback=(env_fallback, ('F', dict(password='y')))),
        g=dict(type='str', no_log=True, fallback=(env_fallback, ('G', dict(password='z')))),
    ))



# Generated at 2022-06-12 23:30:47.863624
# Unit test for function sanitize_keys
def test_sanitize_keys():

    # Test flat dict
    assert sanitize_keys({'key': 'value'}, {'key'}) == {'key': 'value'}
    assert sanitize_keys({'key': 'value'}, {'value'}) == {'key': 'value'}
    assert sanitize_keys({'key': 'value'}, {'key', 'value'}) == {'****': 'value'}

    # Test nested dict
    assert sanitize_keys({'key': {'subkey': 'value'}}, {'key', 'subkey'}) == {'****': {'****': 'value'}}
    assert sanitize_keys({'key': {'subkey': 'value'}}, {'subkey'}) == {'key': {'****': 'value'}}

# Generated at 2022-06-12 23:30:52.666132
# Unit test for function env_fallback
def test_env_fallback():
    if 'A_TEST' in os.environ:
        test_value = os.environ['A_TEST']
        os.environ.pop('A_TEST')
    else:
        test_value = 'a_test'
    os.environ['A_TEST'] = test_value

    try:
        assert env_fallback('A_TEST') == test_value
        assert env_fallback('A_TEST', 'B_TEST') == test_value
    finally:
        os.environ.pop('A_TEST')
        if test_value in os.environ:
            os.environ['A_TEST'] = test_value



# Generated at 2022-06-12 23:31:19.174157
# Unit test for function set_fallbacks
def test_set_fallbacks():
    func_name = 'unit_test_set_fallbacks'

    my_parameters = {
        "test_param": "a",
        "test_param_2": "b"
    }

# Generated at 2022-06-12 23:31:25.836823
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        username=dict(fallback=(env_fallback, 'ANSIBLE_NET_USERNAME')),
        password=dict(fallback=(env_fallback, 'ANSIBLE_NET_PASSWORD')),
        host=dict(fallback=(env_fallback, 'ANSIBLE_NET_HOST')),
        timeout=dict(type='int', fallback=(30,), default=30),
        provider=dict(fallback=(env_fallback, 'ANSIBLE_NET_PROVIDER')),
    )
    paras = dict()
    no_log_values = set_fallbacks(argument_spec, paras)
    assert paras['timeout'] == 30
    assert no_log_values == set()



# Generated at 2022-06-12 23:31:31.456788
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'cert': {'required': False, 'no_log': True, 'fallback': (env_fallback, ['K8S_AUTH_CERT_FILE'])}}
    parameters = {'no_log': True}
    set_fallbacks(argument_spec, parameters)
    assert 'no_log' in parameters
    assert parameters['no_log'] is True



# Generated at 2022-06-12 23:31:38.246097
# Unit test for function env_fallback
def test_env_fallback():
    """Validate the env_fallback function"""

    tests = [
        {
            'environment': {},
            'params': ['ANSIBLE_TEST_PARAM_NOT_EXIST'],
            'result': False
        },
        {
            'environment': {'ANSIBLE_TEST_PARAM': 'test'},
            'params': ['ANSIBLE_TEST_PARAM'],
            'result': 'test'
        }
    ]

    for test in tests:
        os.environ.update(test['environment'])
        try:
            result = env_fallback(*test['params'])
        except AnsibleFallbackNotFound:
            result = False

        assert result == test['result']



# Generated at 2022-06-12 23:31:48.136315
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_spec = {
        'test_param': {
            'type': 'str',
            'required': True,
            'fallback': [env_fallback, 'ANSIBLE_TEST_VAR_1', 'ANSIBLE_TEST_VAR_2', {'fallback_key1': 'value1'}]
        }
    }
    os.environ['ANSIBLE_TEST_VAR_1'] = 'ANSIBLE_TEST_VAR_1_VALUE'
    os.environ['ANSIBLE_TEST_VAR_2'] = 'ANSIBLE_TEST_VAR_2_VALUE'
    test_parameters = {}
    no_log_values = set_fallbacks(test_spec, test_parameters)

# Generated at 2022-06-12 23:31:58.667490
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_REMOTING_CONNECTION_PATH'] = my_dir + "/fake-connection-plugin.py"
    assert env_fallback('ANSIBLE_REMOTING_CONNECTION_PATH') == my_dir + "/fake-connection-plugin.py"
    assert env_fallback('ANSIBLE_REMOTING_CONNECTION_PATH', 'ANSIBLE_FOO_PATH') == my_dir + "/fake-connection-plugin.py"
    del os.environ['ANSIBLE_REMOTING_CONNECTION_PATH']
    raises(AnsibleFallbackNotFound, env_fallback, *('ANSIBLE_REMOTING_CONNECTION_PATH', 'ANSIBLE_FOO_PATH'))



# Generated at 2022-06-12 23:32:03.491066
# Unit test for function env_fallback
def test_env_fallback():
    try:
        env_fallback('DOES_NOT_EXIST')
        assert False, "env_fallback did not raise an exception"
    except AnsibleFallbackNotFound:
        pass

# Ansible will add entries to this dict when the load is complete, do not
# remove items from it or modify it in any way.

# Generated at 2022-06-12 23:32:14.272990
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        test_string=dict(type='str', fallback=(env_fallback, 'CUR_TEST_STRING')),
        test_list=dict(type='list', fallback=(env_fallback, 'CUR_TEST_LIST', ',')),
        test_dict=dict(type='dict', fallback=(env_fallback, 'CUR_TEST_DICT', ',')),
    )

    os.environ['CUR_TEST_STRING'] = 'string_foo'
    os.environ['CUR_TEST_LIST'] = '1,2,3'
    os.environ['CUR_TEST_DICT'] = 'A:1,B:2,C:3'

    test_parameters = {}

    no_log_values = set_

# Generated at 2022-06-12 23:32:25.027712
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test with fallback value from environment variable
    argument_spec = {'arg1': {'type': 'str', 'fallback': (env_fallback, 'TEST_VAR')}}
    parameters = {}
    os.environ['TEST_VAR'] = 'test_env_var'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['arg1'] == 'test_env_var'
    assert len(no_log_values) == 0
    del os.environ['TEST_VAR']

    # Test with None as fallback value
    os.environ['TEST_VAR'] = 'test_env_var'

# Generated at 2022-06-12 23:32:37.598681
# Unit test for function sanitize_keys
def test_sanitize_keys():
    '''Console data'''

# Generated at 2022-06-12 23:33:00.639915
# Unit test for function sanitize_keys
def test_sanitize_keys():
    # This function cannot be tested with simple asserts because a container
    # object is returned and the order of dictionary keys may not be the same
    # on different Python versions.
    # Create some test data and log them before the sanitization
    run_once = [{
        '_ansible_no_log': False,
        'api_key': 'abc123',
        'user_name': 'john.doe',
        'password': 'secret',
    }]
    no_log = [{
        '_ansible_no_log': True,
        'api_key': 'abc123',
        'user_name': 'john.doe',
        'password': 'secret',
    }]

# Generated at 2022-06-12 23:33:09.352587
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'test_account': {'default': 'camel', 'fallback': (env_fallback, 'GOAT')}}, {}) == set()
    assert set_fallbacks({'test_account': {'default': 'camel', 'fallback': (env_fallback, 'GOAT')}}, {'test_account': 'giraffe'}) == set()
    assert set_fallbacks({'test_account': {'default': 'camel', 'fallback': (env_fallback, 'GOAT')}}, {}) == {'camel'}

# Generated at 2022-06-12 23:33:15.988022
# Unit test for function env_fallback
def test_env_fallback():
    some_env = get_random_string()
    assert some_env not in os.environ
    try:
        env_fallback(some_env)
        assert False, "env_fallback failed to raise exception for %s" % some_env
    except AnsibleFallbackNotFound:
        pass
    os.environ[some_env] = get_random_string()
    assert os.environ[some_env] == env_fallback(some_env)
    assert os.environ[some_env] != env_fallback(get_random_string())


# Generated at 2022-06-12 23:33:27.073030
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'foo': {
            'type': 'str',
            'default': 'hello',
            'fallback': (env_fallback, 'ANSIBLE_FOO'),
        },
        'bar': {
            'type': 'str',
            'fallback': (env_fallback, 'ANSIBLE_BAR')
        },
        'baz': {
            'type': 'str',
            'default': 'hello',
            'fallback': (env_fallback, 'ANSIBLE_BAZ', 10, {'bar': 'foo'}),
        },
        'qux': {
            'type': 'str',
            'fallback': (env_fallback, 'ANSIBLE_QUX', {'bar': 'foo'}),
        },
    }


# Generated at 2022-06-12 23:33:29.524659
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_MODULE_TEST_ENV_FALLBACK'] = 'env_fallback_test_value'
    assert env_fallback('ANSIBLE_MODULE_TEST_ENV_FALLBACK') == 'env_fallback_test_value'


# Generated at 2022-06-12 23:33:39.654582
# Unit test for function sanitize_keys
def test_sanitize_keys():
    # Test sanitize_keys with simple lists, dictionaries with strings and nested dictionaries and lists
    # Test 'ignore_keys' option, and make sure it is working with nested structures
    to_sanitize = {'a': 1, 'b': 'abc', 'c': {'c_1': 1, 'c_2': 'abc', 'c_3': ['abc', 'c']}, '_ansible_': {}}
    no_log_strings = {'abc', '_ansible_'}

# Generated at 2022-06-12 23:33:49.641070
# Unit test for function sanitize_keys

# Generated at 2022-06-12 23:34:01.780588
# Unit test for function remove_values
def test_remove_values():
    assert remove_values('hello', ['e']) == 'hllo'
    assert remove_values('hello', ['h']) == 'ello'
    assert remove_values(1, ['1']) == 1
    assert remove_values([1, '2'], ['1', '2']) == []
    assert remove_values({'a': 'b'}, ['a', 'b']) == {}
    assert remove_values(('1', 2), ['1', '2']) == tuple()
    assert remove_values(['h', 'e', 'l', 'l', 'o'], ['l', 'e']) == ['h', 'l', 'o']
    assert remove_values(['h', 'e', 'l', 'l', 'o'], [4]) == ['h', 'e', 'l', 'l', 'o']


# Generated at 2022-06-12 23:34:04.938415
# Unit test for function env_fallback
def test_env_fallback():
    ''' test env_fallback'''
    os.environ['MANPATH'] = '/path1'
    assert env_fallback('MANPATH') == '/path1'
    assert env_fallback('PATH', default='default'), 'default'



# Generated at 2022-06-12 23:34:09.617953
# Unit test for function env_fallback
def test_env_fallback():
    with patch('os.environ', {'ANSIBLE_FOO': 'bar'}):
        assert env_fallback('ANSIBLE_FOO') == 'bar'

    try:
        env_fallback('ANSIBLE_FOO')
        assert False, 'Should raise AnsibleFallbackNotFound'
    except AnsibleFallbackNotFound:
        assert True



# Generated at 2022-06-12 23:34:44.347318
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['env_var'] = 'env_value'
    assert env_fallback('env_var') == 'env_value'
    assert env_fallback('env_other_var') == None  # noqa: F821
    # The next line will raise a NameError exception
    # env_fallback('env_other_var')

# Option description for function env_fallback
ENV_FALLBACK_OPTION_DESCRIPTION = 'environment variable'

# Mark as valid fallback option
_FALLBACKS['env_fallback'] = env_fallback



# Generated at 2022-06-12 23:34:54.275623
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'test':{'type':'str', 'fallback':('env_fallback', 'TEST_FALLBACK')}}, {}) == set(['TEST_FALLBACK'])
    assert set_fallbacks({'test':{'type':'str', 'fallback':('env_fallback', 'TEST_FALLBACK')}}, {'test':'sample'}) == set()
    assert set_fallbacks({'test':{'type':'str', 'fallback':('env_fallback', 'TEST_FALLBACK')}}, {'test':'sample', 'test1':'sample1'}) == set()

# Generated at 2022-06-12 23:34:59.358304
# Unit test for function remove_values
def test_remove_values():
    a = [{"nuke": "me"}, True, 2, {"key": True, "another": "key"}, ["and", "me", {"foo": "bar"}], "With Me"]
    exclude = ["me", True, {"key": True, "another": "key"}, ["and", "me", {"foo": "bar"}], "With Me"]
    result = remove_values(a, exclude)
    assert result == [{}, 2, {}]


# Generated at 2022-06-12 23:35:02.029135
# Unit test for function env_fallback
def test_env_fallback():
    """Unit tests for env_fallback function"""
    env_fallback('PATH', 'CAMEL_CASE')  # Will throw AnsibleFallbackNotFound



# Generated at 2022-06-12 23:35:07.691932
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = set_fallbacks({'p1': {'type': 'str', 'fallback': ('env_fallback', 'FOO_ENV_VAR')},
                                'p2': {'type': 'str', 'fallback': ('env_fallback', ['p1', 'p2'])}},
                               {'p1': 'foo', 'p2': ''})

    assert len(parameters) == 1
    assert 'FOO_ENV_VAR' in parameters


# Generated at 2022-06-12 23:35:18.570091
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ansible_foo'] = 'bar'
    assert env_fallback('ansible_foo') == 'bar'
    os.environ['ansible_foo'] = 'bar'
    assert env_fallback('ansible_missing_key', 'ansible_foo') == 'bar'
    os.environ['ansible_foo'] = 'bar'
    try:
        env_fallback('ansible_missing_key')
    except AnsibleFallbackNotFound as e:
        assert str(e) == 'One or more undefined environment variables: ansible_missing_key'
        assert e.options == ['ansible_missing_key']
    else:
        raise AssertionError("Expected AnsibleFallbackNotFound exception")
    del os.environ['ansible_foo']


# Generated at 2022-06-12 23:35:30.197680
# Unit test for function set_fallbacks
def test_set_fallbacks():
    args = dict(param1=dict(), param2=dict(fallback=(env_fallback, 'TEST_PARAM')))
    params = dict()
    no_log_values = set_fallbacks(args, params)
    assert params == dict(param2=None)
    assert no_log_values == set()

    expected_params = dict(param1=None, param2='test')
    with patch.dict(os.environ, dict(TEST_PARAM='test')):
        params = dict()
        no_log_values = set_fallbacks(args, params)
        assert params == expected_params
        assert no_log_values == set()

    args['param2']['no_log'] = True

# Generated at 2022-06-12 23:35:41.938351
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from copy import deepcopy
    from ansible.module_utils.common.text.converters import to_native

    argument_spec = {
        'foo': {},
        'bar': {},
        'baz': {'fallback': (env_fallback, 'ANSIBLE_ANSIBLE_MODULE_FOO')},
        'bat': {'fallback': (env_fallback, 'ANSIBLE_ANSIBLE_MODULE_BAR')}
    }

    parameters = {'foo': 'foo'}
    os.environ['ANSIBLE_ANSIBLE_MODULE_FOO'] = to_native('foo')
    os.environ['ANSIBLE_ANSIBLE_MODULE_BAR'] = to_native('bar')

    # Test fallbacks

# Generated at 2022-06-12 23:35:45.151621
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TESTOPTION'] = 'test'
    result = env_fallback('TESTOPTION')
    assert result == 'test'
    del os.environ['TESTOPTION']



# Generated at 2022-06-12 23:35:52.449922
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {'var': {'type': 'str', 'fallback': (env_fallback, ['NO_ENV_VAR', {'key': 'ENV_VAR', 'fallback': 'default'}])},
            'var2': {'type': 'str', 'fallback': (env_fallback, 'NO_ENV_VAR_LIST')},
            'var3': {'type': 'str', 'fallback': (env_fallback, 'ENV_VAR_LIST')},
            'var4': {'type': 'dict', 'fallback': (env_fallback, 'ENV_VAR_DICT')}}
    parameters = {}
    os.environ['ENV_VAR'] = 'TEST1'
    no_log_values = set_fallbacks(spec, parameters)
   

# Generated at 2022-06-12 23:36:21.358799
# Unit test for function env_fallback
def test_env_fallback():
    # Simulate not being able to find var in environment
    assert env_fallback('no_such_var') == AnsibleFallbackNotFound
    # Simulate getting var from environment
    os.environ['test_env'] = '123'
    assert env_fallback('test_env') == '123'


# Generated at 2022-06-12 23:36:28.747515
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit tests for `set_fallbacks` using the `unittest` module."""

    try:
        from __main__ import display
    except ImportError:
        print("Unable to import display, cannot test set_fallbacks")
        return

    import os
    from ansible.module_utils.parsing.convert_bool import boolean
    from tempfile import NamedTemporaryFile
    tmp_file = NamedTemporaryFile(delete=False)
    tmp_file.close()

# Generated at 2022-06-12 23:36:29.946257
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('foo', 'bar') == 'bar'



# Generated at 2022-06-12 23:36:31.834872
# Unit test for function env_fallback
def test_env_fallback():
    assert os.environ["path"] == env_fallback("path")
# End Unit test for function env_fallback



# Generated at 2022-06-12 23:36:36.499899
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['WE_HAD_A_FALLBACK'] = 'Hooray!'
    assert env_fallback('WE_HAD_A_FALLBACK') == 'Hooray!'
    del os.environ['WE_HAD_A_FALLBACK']
    try:
        env_fallback('WE_HAD_NO_FALLBACK')
        assert False, 'Expected AnsibleFallbackNotFound'
    except AnsibleFallbackNotFound:
        pass



# Generated at 2022-06-12 23:36:46.980913
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys({'foo': 'bar', 'baz': 1}, ['bar'], ['foo']) == {'foo': 'bar', 'baz': 1}
    assert sanitize_keys({'foo': 'bar', 'baz': 1}, [1]) == {'foo': 'bar'}
    assert sanitize_keys({'foo': 'bar', 'baz': {'qux': 1}}, ['qux']) == {'foo': 'bar', 'baz': {}}
    assert sanitize_keys({'foo': 'bar', 'baz': [{'qux': 1}, {'qux': 2}]}, ['qux']) == {'foo': 'bar', 'baz': [{}, {}]}



# Generated at 2022-06-12 23:36:51.505168
# Unit test for function env_fallback
def test_env_fallback():
    from textwrap import dedent as dedent
    from test.test_support import EnvironmentVarGuard
    from ansible.module_utils.six import PY2
    import inspect

    env = EnvironmentVarGuard()
    env.set('FOO', 'bar')
    if PY2:
        env.set('SPAM', u'ham')

    # Test passing the first argument
    assert env_fallback('FOO') == 'bar'

    # Test passing all arguments
    assert env_fallback('FOO', 'SPAM') == 'bar'

    # Test passing a default value
    assert env_fallback('FOO', 'SPAM', 'eggs') == 'bar'

    # Test passing a keyword argument
    assert env_fallback('FOO', 'SPAM', other='eggs') == 'bar'

    # Test passing all

# Generated at 2022-06-12 23:37:02.698595
# Unit test for function remove_values
def test_remove_values():
    assert remove_values(True, []) == True
    assert remove_values(False, []) == False
    assert remove_values(1, []) == 1
    assert remove_values('foo', []) == 'foo'
    assert remove_values('', []) == ''
    assert remove_values(['foo', 42, True], []) == ['foo', 42, True]
    assert remove_values(('foo', 42, True), []) == ('foo', 42, True)
    assert remove_values({'foo': 1, 'bar': 'baz'}, []) == {'foo': 1, 'bar': 'baz'}
    assert remove_values({'foo': 'bar', 'baz': 'quux'}, ['foo']) == {'baz': 'quux'}

# Generated at 2022-06-12 23:37:11.114198
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'test1': {
            'type': 'path',
            'fallback': (env_fallback, '/a/b/c', '/a/b/c/d'),
            'no_log': True,
        },
        'test2': {
            'type': 'path',
            'fallback': (env_fallback, '/a/b/c'),
            'no_log': True,
        },
        'test3': {
            'type': 'path',
            'fallback': (env_fallback, '/a/b/c/d'),
            'no_log': True,
        }
    }
    parameters = {}
    assert set_fallbacks(argument_spec, parameters) == set(['/a/b/c'])

# Generated at 2022-06-12 23:37:22.019843
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST_ENV_FALLBACK_FOO'] = '1'
    os.environ['TEST_ENV_FALLBACK_BAR'] = '2'
    assert env_fallback('TEST_ENV_FALLBACK_FOO') == '1'
    assert env_fallback('TEST_ENV_FALLBACK_BAR') == '2'
    try:
        env_fallback('TEST_ENV_FALLBACK_BAZ')
        raise AssertionError('should raise AnsibleFallbackNotFound')
    except AnsibleFallbackNotFound:
        pass
    del os.environ['TEST_ENV_FALLBACK_FOO']
    del os.environ['TEST_ENV_FALLBACK_BAR']

