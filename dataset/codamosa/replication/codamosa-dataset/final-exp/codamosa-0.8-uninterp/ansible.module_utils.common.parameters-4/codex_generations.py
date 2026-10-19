

# Generated at 2022-06-12 23:28:37.560637
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """"Test set_fallbacks function"""

    # Setup arguments

# Generated at 2022-06-12 23:28:44.425575
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'test_parameter': {
            'type': 'str',
            'required': False,
            'default': 'default_value'
        },
        'test_parameter_no_fallback': {
            'type': 'str',
            'required': False
        }
    }
    parameters = {
        'test_parameter_no_fallback': 'value2'
    }
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['test_parameter'] == 'default_value'
    assert not no_log_values
    assert set(parameters.keys()) == set(['test_parameter', 'test_parameter_no_fallback'])


# Generated at 2022-06-12 23:28:52.000529
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test empty fallback values
    parameters = {}
    no_log_values = set()
    argument_spec = {
        'param1': {'fallback': (None,), 'type': 'str'},
        'param2': {'fallback': (env_fallback, 'NOENVVAR'), 'type': 'bool'},
        'param3': {'fallback': (env_fallback, 'VALIDENVVAR'), 'type': 'bool'},
        'param4': {'fallback': (env_fallback, 'VALIDENVVAR'), 'type': 'bool', 'no_log': True},
    }
    expected = {
        'param1': None,
        'param2': None,
        'param3': None,
        'param4': None,
    }
    assert set

# Generated at 2022-06-12 23:29:03.180357
# Unit test for function env_fallback
def test_env_fallback():
    from ansible.utils import jsa

    env_fallback('ANSIBLE_TEST_VARIABLE_THAT_WILL_NOT_BE_SET', 'ANSIBLE_TEST_VARIABLE_THAT_WILL_NOT_BE_SET')
    # Should not raise exception
    if os.getenv('ANSIBLE_TEST_VARIABLE_THAT_WILL_NOT_BE_SET', 'no_value') != 'no_value':
        raise AssertionError("Incorrect value of ANSIBLE_TEST_VARIABLE_THAT_WILL_NOT_BE_SET")
    os.environ['ANSIBLE_TEST_VARIABLE_THAT_WILL_BE_SET'] = 'some_value'

# Generated at 2022-06-12 23:29:11.731828
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'param1': {
            'default': 'default',
            'fallback': (env_fallback, 'ANSIBLE_PARAM1'),
        },
        'param2': {
            'default': 'default',
            'fallback': (env_fallback, 'ANSIBLE_PARAM2', {'required': False}),
        },
        'param3': {
            'default': 'default',
            'fallback': (env_fallback, 'ANSIBLE_PARAM3', {'required': True}),
        },
        'param4': {
            'default': 'default',
            'fallback': (env_fallback, 'ANSIBLE_PARAM4', {'required': True}),
            'no_log': True,
        },
    }

    parameters = {}

    # No values

# Generated at 2022-06-12 23:29:14.729021
# Unit test for function env_fallback
def test_env_fallback():
    env = {'A': '1', 'B': '2'}
    with patch.dict('os.environ', env):
        assert env_fallback('A') == '1'
        assert env_fallback('B') == '2'

    exception = False
    try:
        env_fallback('C')
    except AnsibleFallbackNotFound:
        exception = True
    assert exception



# Generated at 2022-06-12 23:29:21.237801
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'greeting': {'default': 'hi'}}, {}) == set()
    assert set_fallbacks({'greeting': {'default': 'hi'}}, {'greeting': 'hello'}) == set()
    assert set_fallbacks({'greeting': {'default': 'hi', 'fallback': [env_fallback, 'HELLO']}}, {}) == set(['hello'])



# Generated at 2022-06-12 23:29:31.254905
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = {"one": "1", "two": "2"}
    spec = {"one": {"type": "str", "fallback": (env_fallback, "MY_OPTION")},
            "two": {"type": "str", "fallback": (env_fallback, "MY_OPTION")},
            "three": {"type": "int", "fallback": (env_fallback, "MY_OPTION")},
            "four": {"type": "str", "fallback": (env_fallback, "MY_OPTION")}}

    os.environ["MY_OPTION"] = "3"
    no_log_values = set_fallbacks(spec, params)
    assert '3' in no_log_values
    assert params["one"] == "1"
    assert params["two"] == "2"

# Generated at 2022-06-12 23:29:36.034955
# Unit test for function sanitize_keys
def test_sanitize_keys():
    dict_value = dict(
        dict_key=dict(
            dict_key1='dict_value1',
            dict_key2='dict_value2',
            dict_key3='dict_value3',
        ),
        dict_key1='dict_value1',
        dict_key2='dict_value2',
        dict_key3='dict_value3',
    )

    list_value = [
        1, 2, 3, 4
    ]

    set_value = {
        1, 2, 3, 4
    }


# Generated at 2022-06-12 23:29:42.121347
# Unit test for function set_fallbacks
def test_set_fallbacks():
    arg_spec = dict(
        foo=dict(fallback=(env_fallback, 'FOO')),
        opt2=dict(fallback=(env_fallback, 'OPT2')),
    )
    parameters = dict(
        foo=None,
        opt2=None,
    )
    os.environ['FOO'] = 'bar'
    os.environ['OPT2'] = 'baz'

    no_log_values = set_fallbacks(arg_spec, parameters)
    assert no_log_values == set()
    assert parameters == dict(foo='bar', opt2='baz')

    parameters = dict(
        opt2=None,
    )

    no_log_values = set_fallbacks(arg_spec, parameters)
    assert no_log_values == set()
    assert parameters

# Generated at 2022-06-12 23:30:16.120031
# Unit test for function env_fallback
def test_env_fallback():
    try:
        result = env_fallback('ANSIBLE_FOO', 'FOO', 'BAR')
    except AnsibleFallbackNotFound:
        result = None
    assert result is None, "env_fallback failed, should not return a value"
    os.environ['BAR'] = 'bar'
    assert env_fallback('ANSIBLE_FOO', 'FOO', 'BAR') == 'bar', "env_fallback failed, should return bar"
    os.environ['FOO'] = 'foo1'
    assert env_fallback('ANSIBLE_FOO', 'FOO', 'BAR') == 'foo1', "env_fallback failed, should return foo1"
    os.environ['ANSIBLE_FOO'] = 'foo2'

# Generated at 2022-06-12 23:30:24.409307
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = {
        'cache_spec': {
            'type': 'dict',
            'options': {
                'cache_type': {
                    'type': 'str',
                    'default': 'basic'
                },
                'credentials': {
                    'type': 'dict',
                    'fallback': (env_fallback, ['TEST_CREDS']),
                    'options': {
                        'username': {
                            'type': 'str'
                        },
                        'password': {
                            'type': 'str',
                            'no_log': True
                        }
                    },
                    'required': False
                }
            }
        }
    }

    parameters = {}
    parameters['cache_spec'] = {'cache_type': 'basic'}
    no_log_values = set_fall

# Generated at 2022-06-12 23:30:32.510733
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {}
    parameters = {}
    # Parameter is not in parameters. Fallback is not used.
    argument_spec['non_exist_param'] = {'type': 'int', 'default': 3}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set() and parameters == {}, "Fallback processing failed."

    # Parameter is in parameters. Fallback is not used.
    argument_spec['non_exist_param'] = {'type': 'int', 'fallback': (env_fallback, 'ABC')}
    parameters['non_exist_param'] = 2
    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:30:35.995964
# Unit test for function env_fallback
def test_env_fallback():
    env = {'ansible_some_fallback': 'is_set'}
    assert env_fallback('ansible_some_fallback', 'anything') == 'is_set'



# Generated at 2022-06-12 23:30:41.859829
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('ANSIBLE_TEST_UNSET_KEY', 'ANSIBLE_TEST_EMPTY_KEY', 'ANSIBLE_TEST_KEY') == 'ANSIBLE_TEST_VALUE'
    assert env_fallback('ANSIBLE_TEST_UNSET_KEY', 'ANSIBLE_TEST_EMPTY_KEY', 'ANSIBLE_TEST_MISSING_KEY') == ''



# Generated at 2022-06-12 23:30:47.149541
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit test for function set_fallbacks

    """
    spec = {
        'foo': {'type': 'str', 'fallback': (env_fallback, 'TEST_FOO')}
    }
    parameters = {}
    no_log_values = set_fallbacks(spec, parameters)
    assert(parameters['foo'] in os.environ['TEST_FOO'])
    assert(parameters['foo'] in no_log_values)


# Generated at 2022-06-12 23:30:58.885303
# Unit test for function set_fallbacks
def test_set_fallbacks():

    # Test values set correctly with fallback
    spec = {'name': {'fallback': (env_fallback, 'FOO_1'), 'type': 'str'}}
    os.environ["FOO_1"] = 'bar'
    params = {}
    set_fallbacks(spec, params)
    assert params['name'] == 'bar'

    # Test fallback ignored when parameter is set
    spec = {'name': {'fallback': (env_fallback, 'FOO_2'), 'type': 'str'}}
    params = {'name': 'bar'}
    set_fallbacks(spec, params)
    assert params['name'] == 'bar'

    # Test fallback ignored when parameter is None

# Generated at 2022-06-12 23:31:04.658522
# Unit test for function sanitize_keys
def test_sanitize_keys():
    data = {
        'mydict': {
            'my_password': 'p@ssw0rd',
            'my_secret': 'secret',
        },
        'mylist': [
            {
                'my_password': 'foo',
                'my_secret': 'secret',
            },
            {
                'my_password': 'bar',
                'my_secret': 'secret',
            },
        ],
        'mystring': 'my_password=p@ssw0rd',
        'myset': {
            'my_password',
            'my_secret',
        },
    }

    # The set of string to hide in logs
    no_log_strings = {'secret', 'p@ssw0rd'}

    # The keys that won't be sanitized.

# Generated at 2022-06-12 23:31:12.703326
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # test case 1
    argument_spec = {
        'a1': {
            'type': 'str',
            'fallback': ['env_fallback', 'MY_VAR1', 'MY_VAR2']
        },
        'a2': {
            'type': 'str',
            'fallback': ['env_fallback', {'key': 'MY_VAR1', 'key2': 'MY_VAR2'}, 'MY_VAR3']
        }
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert len(parameters) == 0

    # test case 2
    os.environ['MY_VAR1'] = 'var1'
    no_log_values = set

# Generated at 2022-06-12 23:31:23.257616
# Unit test for function env_fallback
def test_env_fallback():
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import MagicMock
    os.environ = {}
    os.environ['ansible_needed'] = 'test'
    assert env_fallback('ansible_needed', os.environ) == 'test'
    os.environ = {}
    try:
        env_fallback('ansible_faked', os.environ)
    except AnsibleFallbackNotFound:
        pass
    else:
        assert False


# Declare a global variable to store any fallback values used in ansible.

# Generated at 2022-06-12 23:32:01.158654
# Unit test for function sanitize_keys
def test_sanitize_keys():
    class test_dict(dict):
        pass
    class test_list(list):
        pass
    class test_set(set):
        pass

    test_data = [{}, [], set(), test_dict(), test_list(), test_set()]
    test_provided = [{}, [], set(), test_dict(), test_list(), test_set(), '', 'foo']

    for data in test_data:
        for provided in test_provided:
            if data is provided:
                continue
            data[provided] = provided

    assert sanitize_keys(test_data, ['foo']) == test_data

    result = sanitize_keys(test_data, ['dict', 'list', 'set'])

    assert isinstance(result, list)
    for i in result:
        assert isinstance(i, dict)

# Generated at 2022-06-12 23:32:13.295487
# Unit test for function sanitize_keys
def test_sanitize_keys():
    strings = [b'string', b'with\x1b', b'something\x1b\x1b', b'to\x1b\x1b\x1b', b'mask']
    obj = dict([(b'TEST_' + string, string) for string in strings])
    obj['TEST_object'] = dict([(b'sub_' + string, string) for string in strings])
    obj['TEST_list'] = [string for string in strings]

    # Sanitize keys for dicts and dict-like objects
    no_log_strings = frozenset(strings)
    ignore_keys = frozenset([b'_ansible_no_log'])
    mask_str = to_text(b'<value redacted>')


# Generated at 2022-06-12 23:32:23.977163
# Unit test for function remove_values
def test_remove_values():
    """Unit test for function remove_values"""
    from collections import OrderedDict
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils._text import to_bytes, to_text

    good_value = to_text(b'Everybody has a secret Sonny, something that they just can\'t face. Some folks spend their whole lives trying to keep it', errors='surrogate_or_strict')
    bad_value_bytes = to_bytes(u'They range from the benign to the bad to the ugly. I am not going to judge you Sonny. I am not going to make you talk about it. I am just going to make you face it', errors='surrogate_or_strict')
    bad_value_str = to_text(bad_value_bytes, errors='surrogate_or_strict')



# Generated at 2022-06-12 23:32:25.288072
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('foo') == os.environ['foo']

# Generated at 2022-06-12 23:32:37.867486
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'type': {'type': 'str', 'choices': ['http', 'https']},
        'host': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_NET_HOST'])},
        'username': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_NET_USERNAME'])},
        'password': {'type': 'str', 'no_log': True, 'fallback': (env_fallback, ['ANSIBLE_NET_PASSWORD'])},
    }
    parameters = {
        'type': 'http', 'host': '127.0.0.1'
    }
    os.environ['ANSIBLE_NET_USERNAME'] = 'admin'

# Generated at 2022-06-12 23:32:49.370820
# Unit test for function sanitize_keys
def test_sanitize_keys():

    pwd = os.getcwd()
    test_dir = os.path.dirname(os.path.realpath(__file__))

    os.chdir(test_dir)
    from ansible.module_utils.basic import ModuleTestCase

    class TestSanitizeKeys(ModuleTestCase):
        """Function sanitize_keys() test class"""

        def setUp(self):
            super(TestSanitizeKeys, self).setUp()

            dump_data = {
                'no_log': False,
                'dump_data': {
                    'no_sanitize_key': 'abcd',
                    'sanitize_key': '1234'
                }
            }

            self.dump_data = dump_data


# Generated at 2022-06-12 23:32:51.744783
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(a=dict(required=True, fallback=(env_fallback, 'TEST_A')))
    parameters = dict()
    no_log_values = set()
    set_fallbacks(argument_spec, parameters)
    assert ('a' in parameters) == True



# Generated at 2022-06-12 23:33:01.161663
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks(dict(test_key=dict(type='str', fallback=('x', {"foo": "bar"}, 'y'))), {}) == set()
    assert set_fallbacks(dict(test_key=dict(type='str', fallback=(env_fallback, 'TEST_KEY'))), {}) == set()
    assert set_fallbacks(dict(test_key=dict(type='str', fallback=(env_fallback, 'TEST_KEY'), no_log=True)), {}) == set()
    assert set_fallbacks(dict(test_key=dict(type='str', fallback=(env_fallback, 'TEST_KEY'))), {'test_key': 'foo'}) == set()

# Generated at 2022-06-12 23:33:11.804367
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-12 23:33:22.547122
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:33:57.614859
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ENV_VAR1'] = 'value1'
    os.environ['ENV_VAR2'] = 'value2'
    os.environ['ENV_VAR3'] = 'value3'
    assert env_fallback('ENV_VAR1') == 'value1'
    assert env_fallback('ENV_VAR1', 'ENV_VAR2') == 'value1'
    assert env_fallback('ENV_VAR2', 'ENV_VAR1') == 'value2'
    assert env_fallback('ENV_VAR1', 'ENV_VAR2', 'ENV_VAR3') == 'value1'
    assert env_fallback('ENV_VAR2', 'ENV_VAR3') == 'value2'

# Generated at 2022-06-12 23:34:04.369498
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_VAR_1'] = 'fallback1'
    assert env_fallback('ANSIBLE_VAR_1', 'ANSIBLE_VAR_2') == 'fallback1'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_VAR_2', 'ANSIBLE_VAR_1')
    os.environ.pop('ANSIBLE_VAR_1')



# Generated at 2022-06-12 23:34:09.625713
# Unit test for function set_fallbacks
def test_set_fallbacks():
    '''Test set_fallbacks function'''
    argument_spec = {
        'param1': {
            'type': 'str',
            'default': 'default_val',
            'fallback': (env_fallback, ['PARAM1', 'PARAM2'])
        },
        'param2': {
            'type': 'str',
            'default': 'default_val',
            'fallback': (env_fallback, ['PARAM1', 'PARAM2'])
        }
    }
    parameters = {}

# Generated at 2022-06-12 23:34:17.715454
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_FALLBACK_ENV_VAR_1'] = 'test'
    os.environ['ANSIBLE_TEST_FALLBACK_ENV_VAR_2'] = 'test'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('foobar')
    assert env_fallback('ANSIBLE_TEST_FALLBACK_ENV_VAR_1') == 'test'
    assert env_fallback('ANSIBLE_TEST_FALLBACK_ENV_VAR_2') == 'test'
    os.environ.pop('ANSIBLE_TEST_FALLBACK_ENV_VAR_1')
    os.environ.pop('ANSIBLE_TEST_FALLBACK_ENV_VAR_2')



# Generated at 2022-06-12 23:34:21.286263
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_ENV_KEY'] = 'test_env_value'
    assert env_fallback('ANSIBLE_TEST_ENV_KEY') == 'test_env_value'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NOT_A_REAL_ENV_VAR')


FALLBACK_METHODS = {
    'env': env_fallback,
}



# Generated at 2022-06-12 23:34:30.388359
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:34:40.327579
# Unit test for function env_fallback
def test_env_fallback():
    # No args, no env vars
    assert env_fallback() == 'nope'

    # No env vars
    assert env_fallback('nope') == 'nope'

    # One env var set
    mock_env = {'ANSIBLE_FOO': 'bar'}
    with patch.dict('os.environ', mock_env, clear=True):
        assert env_fallback('nope', 'ANSIBLE_FOO') == 'bar'
        assert env_fallback('nope', 'ANSIBLE_FOO', 'ANSIBLE_BAR') == 'bar'

        # One env var set, other args bad
        assert env_fallback('nope', 'ANSIBLE_BAZ') == 'nope'

    # All env vars set

# Generated at 2022-06-12 23:34:43.591142
# Unit test for function env_fallback
def test_env_fallback():
    if not os.path.exists('.test_env'):
        os.mkdir('.test_env')
    with open('.test_env/ansible.cfg', 'a'):
        os.utime('.test_env/ansible.cfg', None)

    def cleanup():
        shutil.rmtree('.test_env')
    request.addfinalizer(cleanup)

    assert env_fallback('ANSIBLE_CONFIG') == '.test_env/ansible.cfg'



# Generated at 2022-06-12 23:34:53.688802
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        my_param=dict(
            required=False
        ),
        my_env=dict(
            required=False,
            fallback=(env_fallback, ['TEST_ENV']),
        ),
        my_default=dict(
            required=False,
            fallback=(env_fallback, ['TEST_DEFAULT']),
            default='default_value',
        )

    )
    os.environ['TEST_ENV'] = 'env_value'

# Generated at 2022-06-12 23:34:59.625766
# Unit test for function env_fallback
def test_env_fallback():
    # Check fail
    test_var = 'TEST_ENV_VAR_DOES_NOT_EXIST'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback(test_var)

    # Check success
    test_var = 'TEST_ENV_VAR_EXISTS'
    os.environ[test_var] = 'hello world'
    assert env_fallback(test_var) == 'hello world'
    del os.environ[test_var]



# Generated at 2022-06-12 23:35:34.076654
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:35:45.847632
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'param1': {'type': 'str', 'fallback': (env_fallback, ('test_param1', 'test_param2'))}}
    parameters = {'param2': 'param2'}
    os.environ['test_param1'] = 'test_value1'
    os.environ['test_param2'] = 'test_value2'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters == {'param1': 'test_value1', 'param2': 'param2'}

    os.environ['test_param1'] = ''

# Generated at 2022-06-12 23:35:54.368194
# Unit test for function set_fallbacks
def test_set_fallbacks():
    arg_spec = {
        'log_path': {
            'type': 'path',
            'fallback': (env_fallback, ('LOG_PATH', 'ANSIBLE_LOG_PATH'), {'version': '2.0'}),
        }
    }

    module_args = {}

    no_log_values = set_fallbacks(arg_spec, module_args)

    assert module_args['log_path'] == '/path/to/logs'
    assert no_log_values == set(['logs'])



# Generated at 2022-06-12 23:36:00.313657
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('ANSIBLE_TEST_ENV1') == b'ANSIBLE_TEST_VALUE1'
    assert env_fallback('ANSIBLE_TEST_ENV2') == b'ANSIBLE_TEST_VALUE2'
    assert env_fallback('ANSIBLE_TEST_ENV3') == b'ANSIBLE_TEST_VALUE3'


# Generated at 2022-06-12 23:36:11.222275
# Unit test for function env_fallback
def test_env_fallback():
    os.environ["FOO"] = "bar_reg"
    assert env_fallback("FOO") == "bar_reg"
    assert env_fallback("FOO", "FOO") == "bar_reg"
    os.environ["FOO"] = "bar_reg"
    assert env_fallback("bar", "FOO") == "bar_reg"
    assert env_fallback("bar", "FOO", "FOO") == "bar_reg"
    del os.environ["FOO"]
    assert env_fallback("bar", "FOO") == "bar"
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback("bar")
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback("bar", "FOO")



# Generated at 2022-06-12 23:36:21.881819
# Unit test for function env_fallback
def test_env_fallback():
    try:
        # Test when no environment variables are set
        env_fallback('ANSIBLE_TEST_VAR_FALLBACK')
    except AnsibleFallbackNotFound:
        pass
    else:
        assert False

    # Set up some test environment variables
    os.environ['ANSIBLE_TEST_VAR_FALLBACK'] = 'environment variable value'
    os.environ['ANSIBLE_TEST_VAR_SET'] = 'environment variable value'


# Generated at 2022-06-12 23:36:29.110618
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'arg1': {'type': 'str', 'fallback': (env_fallback, ['ENV1', 'ENV2'])},
                     'arg2': {'type': 'int'}}
    parameters = {'arg2': 1}
    assert set_fallbacks(argument_spec, parameters) == set()
    os.environ['ENV2'] = '2'
    assert set_fallbacks(argument_spec, parameters) == set()
    os.environ['ENV1'] = '1'
    assert set_fallbacks(argument_spec, parameters) == set(['1'])
    assert parameters == {'arg1': '1', 'arg2': 1}
    del os.environ['ENV2']
    os.environ['ENV1'] = '1'
    # test

# Generated at 2022-06-12 23:36:36.579632
# Unit test for function env_fallback
def test_env_fallback():
    # Test for value found in environment.
    os.environ['ANSIBLE_NET_SSH_PASSWORD'] = 'secret'
    assert env_fallback('ANSIBLE_NET_SSH_PASSWORD') == 'secret'
    assert env_fallback('ANSIBLE_NET_SSH_PASSWORD', 'GUESS_ME') == 'secret'
    assert env_fallback(['GUESS_ME', 'ANSIBLE_NET_SSH_PASSWORD', 'GUESS_ME_TWICE']) == 'secret'

    # Test for value not found in environment.
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_NET_SSH_USERNAME')

# Generated at 2022-06-12 23:36:47.805307
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Sanity check of function set_fallbacks"""

    argument_spec = {
        'foo': {'fallback': (env_fallback, 'FOO_ENV')},
        'bar': {'fallback': (env_fallback, ['FOO_ENV', 'BAR_ENV'])},
    }

    parameters = {}

    assert set_fallbacks(argument_spec, parameters) == set()
    assert parameters == {}

    os.environ['FOO_ENV'] = 'FOO'
    assert set(parameters) == set()
    assert set_fallbacks(argument_spec, parameters) == set()
    assert parameters == {'foo': 'FOO'}
    os.environ.pop('FOO_ENV')

    assert set(parameters) == set()

# Generated at 2022-06-12 23:36:55.005442
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback()"""
    env_var = None

    # Generate unique env var name
    while not env_var or env_var in os.environ:
        env_var = 'CUSTOM_ENV_VAR_%s' % uuid.uuid4().hex

    os.environ[env_var] = 'Test'
    assert env_fallback(env_var) == 'Test'
    # Test ...
    assert env_fallback('random', env_var) == 'Test'
    # Test non-existing var
    try:
        assert env_fallback('random_' + env_var, 'random_' + env_var + '_random') == {}
        assert False
    except AnsibleFallbackNotFound:
        assert True

    del os.environ[env_var]
