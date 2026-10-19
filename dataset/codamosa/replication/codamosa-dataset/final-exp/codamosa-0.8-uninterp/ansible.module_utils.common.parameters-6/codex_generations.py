

# Generated at 2022-06-12 23:28:26.720922
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test set_fallbacks function
    """
    argument_spec = dict(
        option1=dict(required=False, type='str'),
        option2=dict(required=False, type='dict', fallback=(env_fallback, dict(default='bar'))),
        option3=dict(required=False, type='int', fallback=(env_fallback, 'ANSIBLE_TEST_OPTION3')),
    )
    parameters = dict(
        option1='foo',
    )
    os.environ['ANSIBLE_TEST_OPTION3'] = '42'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters['option1'] == 'foo'

# Generated at 2022-06-12 23:28:36.602488
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from ansible.module_utils.six import string_types
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import Sequence

# Generated at 2022-06-12 23:28:43.651002
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from ansible.module_utils.common._collections_compat import Mapping

# Generated at 2022-06-12 23:28:52.528230
# Unit test for function set_fallbacks
def test_set_fallbacks():
    specification = {
        'number': {
            'type': 'int',
            'fallback': (env_fallback, [('NUMBER',)], {}),
        },
        'dict': {
            'type': 'dict',
            'fallback': (env_fallback, [('DICT',)], {}),
        },
        'list': {
            'type': 'list',
            'fallback': (env_fallback, [('LIST',)], {}),
        },
        'str': {
            'type': 'str',
            'fallback': (env_fallback, [('STR',)], {}),
        },
    }
    param = {}
    set_fallbacks(specification, param)

    assert 'number' not in param
    assert 'dict' not in param

# Generated at 2022-06-12 23:29:03.739006
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test set_fallbacks function"""
    nl_v2 = dict(fallback=(env_fallback, ), type='str', no_log=True)
    nl_v1 = dict(fallback=(env_fallback, 'AUTH_PASSWORD'), type='str', no_log=True)
    v1 = dict(fallback=(env_fallback, 'AUTH_PASSWORD'), type='str')
    v2 = dict(fallback=(env_fallback, ), type='str')
    v3 = dict(fallback=(env_fallback, 'USERNAME'), type='str')

# Generated at 2022-06-12 23:29:12.107159
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:29:20.298201
# Unit test for function sanitize_keys
def test_sanitize_keys():
    expected = {
        '_ansible_no_log': True,
        'foo': {
            'bar': {
                'baz': 'secret'
            }
        }
    }
    actual = {
        '_ansible_no_log': True,
        'foo': {
            'bar': {
                'baz': 'secret'
            }
        }
    }
    assert sanitize_keys(actual, ['secret']) == expected

    expected = {
        '_ansible_no_log': True,
        'foo': {
            '_ansible_no_log': True,
            'bar': {
                '_ansible_no_log': True,
                'baz': 'secret'
            }
        }
    }

# Generated at 2022-06-12 23:29:30.648666
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        param_1=dict(type='int', fallback=(env_fallback, ['PARAM_1'])),
        param_2=dict(type='int', fallback=(env_fallback, ['PARAM_2'])),
    )
    parameters = dict(param_1=10)
    no_log_values = set()
    no_log_values.update(set_fallbacks(argument_spec, parameters))
    assert len(no_log_values) == 0
    assert parameters['param_1'] == 10
    assert 'param_2' not in parameters

    os.environ['PARAM_2'] = '20'
    no_log_values.update(set_fallbacks(argument_spec, parameters))
    assert len(no_log_values) == 0

# Generated at 2022-06-12 23:29:42.079124
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Value should be set from fallback
    # method
    test_spec = dict(val=dict(type='str', fallback=(env_fallback, 'ANSIBLE_TEST_VALUE')))
    test_params = dict()
    os.environ['ANSIBLE_TEST_VALUE'] = 'test_value'
    no_log_values = set_fallbacks(test_spec, test_params)
    assert test_params['val'] == 'test_value'
    assert no_log_values == set()
    del os.environ['ANSIBLE_TEST_VALUE']
    # Value should be set from fallback func
    os.environ['ANSIBLE_TEST_VALUE'] = 'test_value'
    no_log_values = set_fallbacks(test_spec, test_params)

# Generated at 2022-06-12 23:29:50.421782
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        "param1": {
            "type": "str",
            "fallback": (env_fallback, ('ENV',))
        },
        "param2": {
            "type": "str",
            "fallback": (env_fallback, ('ENV2',)),
            "no_log": True
        }
    }
    parameters = {
        "param1": "value"
    }
    result_no_logs = set_fallbacks(spec, parameters)
    assert parameters == {
        "param1": "value",
        "param2": "value2"
    }, "set fallback should not modify the parameters dictionary if the param is already in it"

    parameters = {}
    result_no_logs = set_fallbacks(spec, parameters)

# Generated at 2022-06-12 23:30:54.869087
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Validate the set_fallbacks method."""

    # Test normal
    spec = dict(
        param1={'type': 'str', 'default': 'default1'},
        param2={'type': 'str', 'default': 'default2'},
        param3={'type': 'str', 'default': 'default3', 'fallback': (env_fallback, 'PARAM3')},
    )
    parameters = dict(
        param1='value1', param2='value2', param3='value3'
    )
    ret = set_fallbacks(spec, parameters)
    assert ret == set()
    assert parameters['param1'] == 'value1'
    assert parameters['param2'] == 'value2'
    assert parameters['param3'] == 'value3'

    # Test fallback
    # Note that I do

# Generated at 2022-06-12 23:31:02.394153
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:31:10.705134
# Unit test for function env_fallback
def test_env_fallback():
    # Find an environment variable that probably is not set and test it
    for arg in ['ANSIBLE_FOO', 'FOO']:
        if arg not in os.environ:
            break
    else:
        arg = 'ANSIBLE_FOO'

    # Test exception is raised when environment variable is not set
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback(arg)

    # Test exception is not raised when environment variable is set
    os.environ[arg] = 'foo'
    value = env_fallback(arg)
    assert value == 'foo'
    del os.environ[arg]



# Generated at 2022-06-12 23:31:19.678146
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_case = dict(
        test_case=dict(
            options=dict(
                url=dict(
                    type='str',
                    fallback=(env_fallback, ['MY_TEST_URL', 'TEST_URL']),
                ),
            ),
            parameters=dict(),
        ),
        expected=dict(
            parameters=dict(
                url='mean_url',
            ),
            no_log_values=set(),
        ),
    )
    # mock environment variable
    orig_environ = os.environ.copy()
    os.environ['TEST_URL'] = 'mean_url'

# Generated at 2022-06-12 23:31:20.789023
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # TODO: add unit test
    pass



# Generated at 2022-06-12 23:31:27.212973
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'param1': {'type': 'str', 'fallback': env_fallback, 'env': 'ANSIBLE_TEST_PARAM1'},
                     'param2': {'type': 'str',
                                'fallback': (env_fallback, ('ANSIBLE_TEST_PARAM2', 'ANSIBLE_TEST_PARAM3'))},
                     'param3': {'type': 'str',
                                'fallback': (env_fallback, ('ANSIBLE_TEST_PARAM4', 'ANSIBLE_TEST_PARAM5'), {'default': True})}}

    os.environ['ANSIBLE_TEST_PARAM1'] = 'bar'
    os.environ['ANSIBLE_TEST_PARAM2'] = 'bar1'

# Generated at 2022-06-12 23:31:36.257246
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_FOO'] = 'foo'
    os.environ['ANSIBLE_TEST_BAR'] = 'bar'
    try:
        assert env_fallback('ANSIBLE_TEST_FOO', 'ANSIBLE_TEST_BAR') == 'foo'
        assert env_fallback('ANSIBLE_TEST_BAR', 'ANSIBLE_TEST_FOO') == 'bar'
        assert env_fallback('ANSIBLE_TEST_MISSING') == AnsibleFallbackNotFound
    finally:
        del os.environ['ANSIBLE_TEST_FOO']
        del os.environ['ANSIBLE_TEST_BAR']


# ansible-2.9 The deprecation warnings should use the AnsibleDeprecationWarning class
#              to avoid being ignored

# Generated at 2022-06-12 23:31:46.737875
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    argument_spec = {
        'name': {'required': True, 'type': 'str'},
        'passwd': {'required': True, 'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_NET_PASSWORD'])},
        'ssh_keyfile': {'type': 'path', 'fallback': (env_fallback, ['ANSIBLE_NET_SSH_KEYFILE'])},
    }
    # Case 1: 'passwd' and 'ssh_keyfile' are not defined in parameters,
    #         use env variable instead.
    parameters = {'name': 'foo'}
    fallback_parameters = parameters.copy()

# Generated at 2022-06-12 23:31:57.498651
# Unit test for function env_fallback
def test_env_fallback():
    class TestEnv_fallback:
        def test_env_fallback_pass(self):
            # Empty Env
            os.environ.clear()
            try:
                env_fallback("HOME")
                assert False
            except AnsibleFallbackNotFound:
                assert True
            except Exception as e:
                assert False, "Undefined error {}".format(e)
            else:
                assert False

            # Non-empty Env
            os.environ = {"HOME": "/home", "SHELL": "/bin/bash"}
            try:
                assert env_fallback("SHELL") == "/bin/bash"
            except Exception as e:
                assert False, "Undefined error {}".format(e)

            # Non-existing Env

# Generated at 2022-06-12 23:32:01.785185
# Unit test for function sanitize_keys
def test_sanitize_keys():
    no_log_strings = {'foo'}
    data = {'a': 'b', 'c': {'foo': 'bar'}, 'nolog': 'bar', 'foo': 'bar'}
    assert sanitize_keys(data, no_log_strings) == {'a': 'b', 'c': {'<vault>': 'bar'}, 'nolog': 'bar', '<vault>': 'bar'}
    data = ['a', 'b', 'c', 'nolog', 'foo']
    assert sanitize_keys(data, no_log_strings) == ['a', 'b', 'c', '<vault>', '<vault>']
    data = ('a', 'b', 'c', 'nolog', 'foo')

# Generated at 2022-06-12 23:32:27.002639
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        param1=dict(default="default_value", fallback=(env_fallback, "ANSIBLE_PARAM1", "PARAM1")),
        param2=dict(default="default_value", fallback=(None, "ANSIBLE_PARAM2", "PARAM2")),
        param3=dict(default="default_value", fallback=None),
    )
    parameters = dict(param1="value1", param3="value3")
    no_log_values = set()
    expected_parameters = dict(param1="value1", param2="ANSIBLE_PARAM2_value", param3="value3")
    expected_no_log_values = set(["ANSIBLE_PARAM2_value"])

    assert set_fallbacks(spec, parameters) == expected_no_log_values
   

# Generated at 2022-06-12 23:32:38.856176
# Unit test for function set_fallbacks
def test_set_fallbacks():
    fallback_obj = {'fallback': ('env_fallback', ['TEST_ENV_VAR'])}

# Generated at 2022-06-12 23:32:47.460446
# Unit test for function remove_values
def test_remove_values():
    data = {'a': 12, 'b': 'value', 'c': [1, 2, 3], 'd': {'e': {'f': 'string'}, 'g': 'password'}, 'h': 'string'}
    assert remove_values(data, ['password', 'string']) == {'a': 12, 'b': 'REDACTED', 'c': [1, 2, 3], 'd': {'e': {'f': 'REDACTED'}, 'g': 'REDACTED'}, 'h': 'REDACTED'}


#
# Deprecated functions
#

# Generated at 2022-06-12 23:32:54.845874
# Unit test for function set_fallbacks
def test_set_fallbacks():
    os.environ['env_fallback_test'] = '/tmp'
    assert not set_fallbacks({}, {})
    assert {'/tmp'} == set_fallbacks({'a': {'fallback': (env_fallback, 'env_fallback_test')}}, {})
    assert not set_fallbacks({'a': {'fallback': (env_fallback, 'env_fallback_test1')}}, {})
    assert not set_fallbacks({'a': {'fallback': (env_fallback, 'env_fallback_test1')}}, {'a': '/tmp'})
    assert not set_fallbacks({'a': {'fallback': (env_fallback, 'env_fallback_test1')}}, {'b': '/tmp'})



# Generated at 2022-06-12 23:33:03.206155
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params ={'param1': 'value1', 'param2': None}
    arg_spec = {'param1': {'required': True, 'type': 'str'}, 'param2': {'required': True, 'type': 'str', 'fallback': (env_fallback, ['CUSTOM_ENV_VAR'])}}
    no_log_values = set_fallbacks(arg_spec, params)
    assert len(no_log_values) == 0
    assert params['param2'] is None
    os.environ['CUSTOM_ENV_VAR'] = 'somestring'
    no_log_values = set_fallbacks(arg_spec, params)
    assert params['param2'] == 'somestring'
    assert len(no_log_values) == 0

# Generated at 2022-06-12 23:33:08.600960
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:33:15.610313
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:33:26.650122
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(type='str', fallback=(env_fallback, 'FOO_ENV_VAR')),
        foo_default=dict(type='str', fallback=(env_fallback, {'default': 'default_value'})),
        foo_bool=dict(type='bool', fallback=(env_fallback, {'true': (True,), 'false': (False,)})),
    )
    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert set() == set(parameters)

    with patch.dict(os.environ, {'FOO_ENV_VAR': 'bar'}):
        no_log_values = set_fallbacks(argument_spec, parameters)
        assert parameters['foo'] == 'bar'

# Generated at 2022-06-12 23:33:32.856112
# Unit test for function sanitize_keys
def test_sanitize_keys():
    class TestModule(object):

        def run(self, *args, **kwargs):
            self._ansible_no_log = kwargs.pop('_ansible_no_log', False)
            return args, kwargs, self._ansible_no_log

    mod = TestModule()

    # No private keys
    assert sanitize_keys((1, 2, 3), no_log_strings=set()) == (1, 2, 3)
    assert sanitize_keys({'a': 1, 'b': 2, 'c': 3}, no_log_strings=set()) == {'a': 1, 'b': 2, 'c': 3}

    # Empty private string key
    assert sanitize_keys((1, 2, 3), no_log_strings=set([''])) == (1, 2, 3)

# Generated at 2022-06-12 23:33:35.560468
# Unit test for function env_fallback
def test_env_fallback():
    for i in args:
        if i in os.environ:
            return os.environ[i]
    raise AnsibleFallbackNotFound


# Generated at 2022-06-12 23:34:17.131486
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_UNORTUNATE_VARIABLE'] = "bar"
    assert env_fallback("ANSIBLE_UNORTUNATE_VARIABLE") == "bar"



# Generated at 2022-06-12 23:34:27.887566
# Unit test for function remove_values
def test_remove_values():
    # provided list of no_log_strings
    no_log_strings = ('password', 'secret', 'private', 'key')

    # list of lists of strings
    test_strings = []
    # list of expected return values
    expect_results = []

    # add values to test_strings/expect_results as needed
    test_strings.append(['test_string', 'string_password', 'test_string2'])
    expect_results.append(['test_string', 'REDACTED', 'test_string2'])

    test_strings.append(['test_string', 'string_password', 'test_string2', 'passwordstring'])
    expect_results.append(['test_string', 'REDACTED', 'test_string2', 'REDACTED'])


# Generated at 2022-06-12 23:34:33.544395
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(get_url=dict(fallback=(env_fallback, ['ANSIBLE_GET_URL'])))
    parameters = dict()
    set_fallbacks(argument_spec, parameters)
    assert parameters['get_url'] == 'http://docs.ansible.com'
    assert 'ANSIBLE_GET_URL' in os.environ



# Generated at 2022-06-12 23:34:42.758449
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'param1': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_PARAM1')}}
    parameters = {}
    os.environ['ANSIBLE_PARAM1'] = 'env_no_log'
    # no_log = False
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    # no_log = True
    argument_spec = {'param1': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_PARAM1'), 'no_log': True}}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set(['env_no_log'])



# Generated at 2022-06-12 23:34:45.566087
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['var1'] = 'val1'  # set a var in the env
    assert 'val1' == env_fallback('var1', 'var2')  # look for a var that is set
    assert 'val2' == env_fallback('var2', default='val2')  # look for a var that isn't set but have a default
    os.environ.pop('var1')  # remove var from env



# Generated at 2022-06-12 23:34:54.866615
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'arg': {'type': 'str', 'fallback': (env_fallback, 'arg')},
                     'arg2': {'type': 'str', 'fallback': (env_fallback, 'arg2', 'arg3')},
                     'arg3': {'type': 'str', 'fallback': (env_fallback, 'arg3', 'arg2')}}
    parameters = {'arg': 'Value', 'arg3': 'Value3'}
    expected_no_log_values = set()
    expected_parameters = {'arg': 'Value', 'arg2': None, 'arg3': 'Value3'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == expected_no_log_values
    assert parameters == expected_parameters

# Generated at 2022-06-12 23:35:00.749216
# Unit test for function remove_values
def test_remove_values():
    no_log_strings = set()
    no_log_strings.add('password')
    no_log_strings.add('secret')
    provided_dict = dict(
            a=dict(
                b=dict(
                    c="d",
                    password="foo"
                    )
                )
            )
    expected_dict = dict(
            a=dict(
                b=dict(
                    c="d",
                    )
                )
            )
    actual_dict = remove_values(provided_dict, no_log_strings)
    assert expected_dict == actual_dict



# Generated at 2022-06-12 23:35:09.337264
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_params = {}

# Generated at 2022-06-12 23:35:18.189460
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'param1': {'type': 'str', 'fallback': ENV_VAR_NAME},
        'param2': {'type': 'str', 'fallback': (env_fallback, ENV_VAR_NAME)}
    }

    parameters = {'param1': None}
    result = set_fallbacks(argument_spec, parameters)

    assert parameters['param1'] == os.environ[ENV_VAR_NAME]
    assert parameters['param2'] is None
    assert result == {os.environ[ENV_VAR_NAME]}



# Generated at 2022-06-12 23:35:29.517922
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # create argument spec
    arg_spec = {
        'param_1': {'fallback': (env_fallback, ['PARAM_1', 'PARAM_2'], {})},
        'param_2': {'fallback': (env_fallback, ['PARAM_3'], {})},
    }

    # create parameters
    parameters = {
        'param_1': ''
    }

    # set env as param_1 = 'from env' and param_3 = 'from env'
    os.environ['PARAM_1'] = 'from env'
    os.environ['PARAM_3'] = 'from env'

    # set fallback values
    no_log_values = set_fallbacks(arg_spec, parameters)

    # assert param_1 = 'from env' and param_2 = '

# Generated at 2022-06-12 23:36:18.616228
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'param1': {'type': 'str', 'fallback': (env_fallback, 'env_var')},
                     'param2': {'type': 'str', 'fallback': (env_fallback, 'env_var2')}}
    parameters = {}
    os.environ['env_var'] = 'hello'
    set_fallbacks(argument_spec, parameters)
    assert parameters['param1'] == 'hello'
    assert 'param2' not in parameters



# Generated at 2022-06-12 23:36:26.944938
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'foo': {'type': 'str', 'fallback': (env_fallback, os.environ.keys()), 'no_log': True},
        'baz': {'type': 'str', 'fallback': (env_fallback, 'FOO')},
        'qux': {'type': 'str', 'fallback': (env_fallback, 'FOO')},
    }
    parameters = {
        'foo': 'bar',
        'qux': 'quux'
    }
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {
        'foo': 'bar',
        'baz': 'bar',
        'qux': 'quux'
    }
    assert no_log_values == {'bar'}
   

# Generated at 2022-06-12 23:36:35.472880
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys('foo bar', {'foo'}) == 'bar'
    assert sanitize_keys(['foo bar'], {'foo'}) == ['bar']
    assert sanitize_keys(('foo bar', 'foo baz'), {'foo'}) == ('bar', 'baz')
    assert sanitize_keys({'foo bar': 'foo baz', 'foo foobar': 'foo foobaz'}, {'foo'}) == {'bar': 'baz', 'foobar': 'foobaz'}
    assert sanitize_keys({'foo bar': 'foo baz', 'bar': 'foo foobaz'}, {'foo'}) == {'bar': 'baz', 'bar': 'foobaz'}

# Generated at 2022-06-12 23:36:46.407450
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys({'a':'b'}, ['c']) == {'a': 'b'}
    assert sanitize_keys({'a': 'b'}, ['a']) == {'b': 'b'}
    assert sanitize_keys({'a': 'b', 'c': 'd'}, ['a', 'b']) == {'c': 'd'}
    assert sanitize_keys({'a': 'b', 'c': 'd'}, ['a', 'b', 'c']) == {'d': 'd'}
    assert sanitize_keys({'a': 'b', 'c': 'd'}, ['b', 'd']) == {'a': 'b', 'c': 'd'}

# Generated at 2022-06-12 23:36:54.072715
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:37:06.504521
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(fallback=(env_fallback,)),
        bar=dict(fallback=(env_fallback, 'FOO')),
        baz=dict(fallback=(env_fallback, ['FOO'])),
        quux=dict(fallback=(env_fallback, dict(default='foo'))),
    )

    parameters = dict(
        foo='foo',
        bar='bar',
        baz='baz',
        quux='quux'
    )
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters['foo'] == 'foo'
    assert parameters['bar'] == 'bar'
    assert parameters['baz'] == 'baz'

# Generated at 2022-06-12 23:37:16.205328
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = { 'foo': { 'type': 'str', 'fallback': (env_fallback, ['FOO_OPTION']) } }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert not no_log_values
    assert 'foo' not in parameters

    os.environ['FOO_OPTION'] = 'bar'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert not no_log_values
    assert parameters['foo'] == 'bar'
    del os.environ['FOO_OPTION']



# Generated at 2022-06-12 23:37:25.197437
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        a=dict(type='str', fallback=('env', 'TEST_A')),
        b=dict(type='str', fallback=('env', 'TEST_B'))
    )
    parameters = dict()
    os.environ['TEST_A'] = 'test_a'
    os.environ['TEST_B'] = 'test_b'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert dict(a='test_a', b='test_b') == parameters
    assert no_log_values == set()

    argument_spec = dict(
        a=dict(type='str', fallback=('env', 'TEST_A'))
    )
    parameters = dict()
    os.environ['TEST_A']

# Generated at 2022-06-12 23:37:30.850960
# Unit test for function sanitize_keys
def test_sanitize_keys():
    my_dict = {'lorem': 'ipsum', 'dolor': {'sit': 'amet'}}
    assert (sanitize_keys(my_dict, no_log_strings={'amet'}) == {'lorem': 'ipsum', 'dolor': {'sit': 'amet'}})
    assert (sanitize_keys(my_dict, no_log_strings={'sit'}) == {'lorem': 'ipsum', 'dolor': {'sit': '**'}})
    assert (sanitize_keys(my_dict, no_log_strings={'dolor'}) == {'lorem': 'ipsum', 'dolor': '**'})

# Generated at 2022-06-12 23:37:40.034261
# Unit test for function env_fallback
def test_env_fallback():
    from ansible.module_utils.six import PY2
    if PY2:
        # Py2 has no support for non-string environment variable names
        return
    old_env = dict(os.environ)
    env = dict(os.environ)
    env[u'FALLBACK_CASE_UNICODE'] = u'UNICODE_ENV_FALLBACK'
    os.environ.update(env)
    try:
        assert env_fallback(u'FALLBACK_CASE_UNICODE') == u'UNICODE_ENV_FALLBACK'
    finally:
        os.environ.clear()
        os.environ.update(old_env)

