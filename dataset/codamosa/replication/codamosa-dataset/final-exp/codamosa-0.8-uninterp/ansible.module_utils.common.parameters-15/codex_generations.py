

# Generated at 2022-06-12 23:28:49.838545
# Unit test for function set_fallbacks
def test_set_fallbacks():

    class EnvironmentFallback(object):
        def __init__(self, var):
            self.envvar = var

        def __call__(self):
            return os.environ.get(self.envvar, None)

    argument_spec = {'a': {'fallback': (env_fallback, 'FOO')},
                     'b': {'fallback': (EnvironmentFallback('FOO'),)},
                     'c': {'fallback': ('env_fallback', 'FOO')}}
    parameters = {'a': None, 'b': None, 'c': 'preset'}

    assert set_fallbacks(argument_spec, parameters) == set()
    assert parameters['a'] == parameters['b'] == parameters['c'] == 'preset'

    del parameters['c']

# Generated at 2022-06-12 23:28:59.170807
# Unit test for function env_fallback
def test_env_fallback():
    """Test function env_fallback"""
    try:
        env_fallback('A_DUMMY_ENV_VARIABLE_NAME')
        assert False, 'Failure is expected when environment variable is not set.'
    except AnsibleFallbackNotFound:
        pass

    os.environ['A_DUMMY_ENV_VARIABLE_NAME'] = 'dummy_value'
    assert env_fallback('A_DUMMY_ENV_VARIABLE_NAME') == 'dummy_value'



# Generated at 2022-06-12 23:29:08.414355
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:29:12.550374
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit test for function set_fallbacks"""
    import doctest
    import functools
    from unittest.mock import Mock

    from ansible.module_utils import basic

    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import ComplexDict
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import ComplexList

    module = Mock()
    module.params = {}

    # Setup module.fail_json()
    def fail(msg):
        raise ValueError(msg)
    module.fail_json = functools.partial(fail)

    # Do not blow up when env vars are not available
    module.fail_json.__globals__['os'] = Mock()
    module.fail_json.__

# Generated at 2022-06-12 23:29:21.236543
# Unit test for function set_fallbacks
def test_set_fallbacks():
    ensure_module_exists('os', 'CliArgumentParser')

    argument_spec = {'test1': {'type': 'str', 'default': 'test11', 'fallback': (env_fallback, ['test1'])},
                     'test2': {'type': 'str', 'fallback': (env_fallback, ['test2'])},
                     'test3': {'type': 'str'},
                     'test4': {'type': 'str', 'fallback': (env_fallback, ['test4'])},
                     'test5': {'type': 'str', 'fallback': (env_fallback, ['test5'])}}
    parameters = {'test3': 'test3', 'test4': None}

    no_log_values = set_fallbacks(argument_spec, parameters)

   

# Generated at 2022-06-12 23:29:31.254727
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """Functional test for sanitize_keys"""

    no_log_values = {'value', 'values'}

# Generated at 2022-06-12 23:29:42.609794
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'a': {'fallback': ('env_fallback', 'PATH')}, 'b': {'fallback': (None,)}}, {}) == set()
    assert set_fallbacks({'a': {'fallback': ('env_fallback', 'PATH')}, 'b': {'fallback': (None,)}}, {'a': 1}) == set()
    assert set_fallbacks({'a': {'no_log': True, 'fallback': ('env_fallback', 'PATH')}, 'b': {'fallback': (None,)}}, {}) == set(["/bin", "/usr/bin", "/usr/local/bin"])

# Generated at 2022-06-12 23:29:50.770655
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test to validate set_fallbacks function"""
    argument_spec_1 = {'param_one': {'type': 'str', 'fallback': (env_fallback, 'env_one'), 'no_log': True},
                      'param_two': {'type': 'str', 'fallback': (env_fallback, 'env_two'), 'no_log': True}}
    parameters_1 = {}
    parameters_2 = {'param_one': 'test', 'param_two': 'test'}
    no_log_values_1 = set_fallbacks(argument_spec_1, parameters_1)
    no_log_values_2 = set_fallbacks(argument_spec_1, parameters_2)
    assert len(no_log_values_1) == 0
    assert no_log_values_2 == set()

# Generated at 2022-06-12 23:29:57.963583
# Unit test for function env_fallback
def test_env_fallback():
    """ test env_fallback() """
    myenv = dict(ANSIBLE_NET_USERNAME="user", ANSIBLE_NET_PASSWORD="pass")
    with patch.object(os, "environ", myenv):
        assert env_fallback("ANSIBLE_NET_USERNAME") == "user"
        assert env_fallback("ANSIBLE_NET_USERNAME", "ANSIBLE_NET_PASSWORD") == "user"
        try:
            env_fallback("ANSIBLE_NET_PASSWORD", "ANSIBLE_NET_SSH_KEYFILE")
        except AnsibleFallbackNotFound:
            # Any exception will do
            pass



# Generated at 2022-06-12 23:30:09.523571
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'foo': {'default': 'bar', 'fallback': (env_fallback, 'FOO')}}, {}) == set(['bar'])
    assert set_fallbacks({'foo': {'default': 'bar', 'fallback': (env_fallback, 'FOO')}}, {'foo': 'baz'}) == set(['baz'])
    assert set_fallbacks({'foo': {'default': 'bar', 'fallback': (env_fallback, 'FOO')}}, {'foo': None}) == set([None])
    assert set_fallbacks({'foo': {'default': 'bar', 'fallback': (env_fallback, 'FOO')}}, {}) == set(['bar'])
    os.environ['FOO'] = 'baz'

# Generated at 2022-06-12 23:31:06.923490
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('ANSIBLE_MODULE_FOO') == os.environ['ANSIBLE_MODULE_FOO']
    os.environ['ANSIBLE_MODULE_FOO'] = 'bar'
    assert env_fallback('ANSIBLE_MODULE_FOO') == 'bar'



# Generated at 2022-06-12 23:31:13.811083
# Unit test for function env_fallback
def test_env_fallback():
    """Validate env_fallback function"""

    # Exists
    os.environ['ANSIBLE_PARAM_FOO'] = 'foo'
    assert env_fallback('ANSIBLE_PARAM_FOO') == 'foo'

    # Does not exist
    os.environ.pop('ANSIBLE_PARAM_FOO')
    try:
        env_fallback('ANSIBLE_PARAM_BAR')
        assert False, "env_fallback should raise AnsibleFallbackNotFound when env var is not set"
    except AnsibleFallbackNotFound as e:
        assert True

    # Prefix/Suffix
    os.environ['ANSIBLE_PARAM_FOO_1'] = 'foo1'
    os.environ['ANSIBLE_PARAM_1_FOO'] = '1foo'
    os

# Generated at 2022-06-12 23:31:23.504204
# Unit test for function sanitize_keys
def test_sanitize_keys():
    test_obj = {'key1': 'value1', 'key2': 'value2'}
    expected_obj = {'key1': 'value1', 'key2': 'value2'}
    actual_obj = sanitize_keys(test_obj, set([]))
    assert actual_obj == expected_obj

    test_obj = {'key1': 'value1', 'key2': {'subkey1': 'subvalue1', 'subkey2': 'subvalue2'}}
    expected_obj = {'key1': 'value1', 'key2': {'subkey1': 'subvalue1', 'subkey2': 'subvalue2'}}
    actual_obj = sanitize_keys(test_obj, set([]))
    assert actual_obj == expected_obj


# Generated at 2022-06-12 23:31:33.816788
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_NET_USERNAME'] = 'cisco'
    os.environ['ANSIBLE_NET_PASSWORD'] = 'cisco123'
    assert env_fallback('ANSIBLE_NET_USERNAME') == 'cisco'
    assert env_fallback('ANSIBLE_NET_PASSWORD') == 'cisco123'
    os.environ['ANSIBLE_NET_AUTH_PASS'] = 'cisco123'
    assert env_fallback('ANSIBLE_NET_PASSWORD') == 'cisco123'
    del os.environ['ANSIBLE_NET_USERNAME']
    del os.environ['ANSIBLE_NET_PASSWORD']
    del os.environ['ANSIBLE_NET_AUTH_PASS']


# Generated at 2022-06-12 23:31:45.927250
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:31:56.233517
# Unit test for function sanitize_keys
def test_sanitize_keys():
    obj = {'password': 'secret', 'password_multi-word': 'secret', 'passwd_multi_word': 'secret', 'ssh_key': 'secret', 'ssh-key': 'secret'}

    # Validate type (dict)
    assert isinstance(sanitize_keys(obj, {}), dict)
    # Validate value of non-sanitized key
    assert sanitize_keys(obj, {}).get('password') == 'secret'
    # Validate value of sanitized key that contains 'password' in the key
    assert sanitize_keys(obj, {}).get('password_multi-word') == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

# Generated at 2022-06-12 23:32:05.756463
# Unit test for function remove_values
def test_remove_values():
    # Test MutableMapping
    no_log_dict = {'param1': 'value1', 'param2': 'value2'}
    no_log_strings = ['value1']
    sanitized_dict = remove_values(no_log_dict, no_log_strings)
    assert 'param1' in sanitized_dict
    assert 'param2' in sanitized_dict
    assert sanitized_dict['param1'] == 'VALUE_WAS_HIDDEN'
    assert sanitized_dict['param2'] == 'value2'
    # Test MutableSequence
    no_log_list = [{'param1': 'value1'}, {'param2': 'value2'}]
    no_log_strings = ['value1']

# Generated at 2022-06-12 23:32:15.616932
# Unit test for function remove_values
def test_remove_values():
    # test dict
    d = dict(a=1, b=2, c=3, d='@@special_value@@', e=['@@special_value@@', 6, 7], f=['@@special_value@@', '@@special_value@@', 8])
    d2 = dict(a=1, b=2, c=3, d='****UNSAFE VALUE****', e=['****UNSAFE VALUE****', 6, 7], f=['****UNSAFE VALUE****', '****UNSAFE VALUE****', 8])
    assert remove_values(d, ['@@special_value@@']) == d2
    # test string
    assert remove_values('@@special_value@@', ['@@special_value@@']) == '****UNSAFE VALUE****'
    # test list

# Generated at 2022-06-12 23:32:26.230439
# Unit test for function set_fallbacks
def test_set_fallbacks():
    import copy


# Generated at 2022-06-12 23:32:34.108279
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST_FOO'] = 'Foo'
    assert env_fallback('TEST_FOO', 'TEST_FOO_NOT_PRESENT') == 'Foo'
    with pytest.raises(AnsibleFallbackNotFound):
        assert env_fallback('TEST_FOO_NOT_PRESENT')
    os.environ.pop('TEST_FOO')



# Generated at 2022-06-12 23:33:03.047762
# Unit test for function env_fallback
def test_env_fallback():
    """Unit test for function env_fallback"""
    from sys import version_info

    if version_info[0] > 2:
        from unittest.mock import patch
    else:
        from mock import patch

    with patch.dict('os.environ', {'ANSIBLE_FOO': 'foo'}):
        assert 'foo' == env_fallback('ANSIBLE_FOO')
    try:
        env_fallback('ANSIBLE_BAR')
        assert False
    except AnsibleFallbackNotFound:
        pass



# Generated at 2022-06-12 23:33:12.411972
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'diff': {'type': 'bool', 'default': False, 'fallback': (env_fallback, 'ANSIBLE_DIFF')},
        'check': {'type': 'bool', 'default': False, 'fallback': (env_fallback, 'ANSIBLE_CHECK', {'version_added': '2.4.0'})},
        'no_log': {'type': 'bool', 'default': False, 'fallback': (env_fallback, 'ANSIBLE_NO_LOG', {'version_added': '2.4.0'})},
    }

    # No value passed in, no environment variable set
    parameters = {}
    no_log_values = set_fallbacks(spec, parameters)
    assert parameters == {'diff': False}
    assert not no_log_values

    #

# Generated at 2022-06-12 23:33:16.636644
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_KEY'] = 'ANSIBLE_TEST_VALUE'
    assert env_fallback('ANSIBLE_TEST_KEY') == 'ANSIBLE_TEST_VALUE'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NOT_REAL')

# Generated at 2022-06-12 23:33:27.778323
# Unit test for function env_fallback
def test_env_fallback():
    def reset():
        os.environ.clear()
        os.environ.update(BASE_ENVIRON)
    reset()

    assert env_fallback('ANSIBLE_TEST_ENV_VAR') == 'ANSIBLE_TEST_ENV_VAR_VALUE'
    assert env_fallback('ANSIBLE_TEST_ENV_VAR1', 'ANSIBLE_TEST_ENV_VAR') == 'ANSIBLE_TEST_ENV_VAR1_VALUE'

    # Remove ANSIBLE_TEST_ENV_VAR from environ.
    # Ensure env_fallback does not find it and raises AnsibleFallbackNotFound.
    del os.environ['ANSIBLE_TEST_ENV_VAR']

# Generated at 2022-06-12 23:33:35.005186
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test no_log=True case
    # Define spec that has fallback
    spec = {'a': {'type': 'str', 'fallback': (env_fallback, 'a_env')}}
    # Run set_fallbacks
    no_log_values = set_fallbacks(spec, {})
    # Assert set_fallbacks return empty
    assert no_log_values == set()

    # Test no_log=False case
    # Define specification
    spec = {'a': {'type': 'str', 'fallback': (env_fallback, 'a_env')}}
    # Define environment variable a_env that has value 'test'
    os.environ['a_env'] = 'test'
    # Run set_fallbacks

# Generated at 2022-06-12 23:33:46.367609
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback() == AnsibleFallbackNotFound
    assert env_fallback('FOOBARBAZ') == AnsibleFallbackNotFound
    assert env_fallback('FOO_BAR_BAZ') == AnsibleFallbackNotFound
    assert env_fallback('FOO_BAR_BAZ_QUX') == AnsibleFallbackNotFound
    os.environ['FOO'] = 'FOO'
    assert env_fallback('FOO') == 'FOO'
    assert env_fallback('FOO_BAR_BAZ') == AnsibleFallbackNotFound
    assert env_fallback('FOO_BAR_BAZ_QUX') == AnsibleFallbackNotFound
    os.environ['FOO_BAR'] = 'FOO_BAR'

# Generated at 2022-06-12 23:33:52.945473
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys({'a': 'b'}, ['b']) == {'a': 'b'}
    assert sanitize_keys({'a': 'b'}, ['a']) == {'a': 'b'}
    assert sanitize_keys({'a': 'b'}, ['b'], ignore_keys=['a']) == {'a': 'b'}
    data = {'a': {'c': 'd'}, 'b': {'c': 'e'}}
    assert sanitize_keys(data, ['b']) == {'a': {'c': 'd'}, 'b': {'c': 'e'}}
    assert sanitize_keys(data, ['c']) == {'a': {'c': 'd'}, 'b': {'c': 'e'}}

# Generated at 2022-06-12 23:34:04.411774
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameter1 = dict(a='a',
                      b='b',
                      c='c',
                      d='d',
                      e='e',
                      f='f',
                      g='g',
                      h='h',
                      i='i',
                      j='j',
                      k='k',
                      l='l',
                      m='m',
                      n='n',
                      o='o',
                      p='p',
                      q='q',
                      r='r',
                      s='s',
                      t='t',
                      u='u',
                      v='v',
                      w='w',
                      x='x',
                      y='y',
                      z='z')

# Generated at 2022-06-12 23:34:06.208347
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['foo'] = 'bar'
    assert env_fallback('foo') == 'bar'



# Generated at 2022-06-12 23:34:08.546060
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback()"""
    assert env_fallback('head_is_empty') == ''



# Generated at 2022-06-12 23:34:42.309347
# Unit test for function env_fallback
def test_env_fallback():
    # Test when no args are given
    try:
        env_fallback()
    except AnsibleFallbackNotFound:
        pass
    # Test when no matching variables are given
    try:
        os.environ["ANSIBLE_TESTVAR"] = "test"
        env_fallback("ANSIBLE_TESTVAR2")
    except AnsibleFallbackNotFound:
        pass
    else:
        raise AssertionError("env_fallback should have thrown an AnsibleFallbackNotFound")
    # Test when a matching variable is given
    try:
        env_fallback("ANSIBLE_TESTVAR")
    except AnsibleFallbackNotFound:
        raise AssertionError("env_fallback should not have thrown an AnsibleFallbackNotFound")


# Generated at 2022-06-12 23:34:46.932434
# Unit test for function sanitize_keys
def test_sanitize_keys():
    no_log_strings = ['value1', 'value2']
    ignore_keys = {'key1', 'key2'}

    # Test sanitize_keys() on dictionary.
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
    }
    new_value = sanitize_keys(data, no_log_strings, ignore_keys)
    assert list(sorted(new_value.keys())) == ['key3', 'key3_value2', 'key3_value2_value1']

    # Test sanitize_keys() on list.
    data = [
        'value1',
        'value2',
        'value3',
    ]

# Generated at 2022-06-12 23:34:50.359146
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['HOME'] = '/home/user'
    assert env_fallback('HOME') == '/home/user'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NOT_SET')



# Generated at 2022-06-12 23:34:58.584932
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:35:03.021138
# Unit test for function env_fallback
def test_env_fallback():
    '''
    Test to make sure that env_fallback doesn't find the value
    in the environment if it isn't there
    '''
    assert_raises(AnsibleFallbackNotFound, env_fallback, 'THIS_WILL_NOT_BE_IN_THE_ENV', 'THIS_NEITHER')



# Generated at 2022-06-12 23:35:10.808920
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'password': {'type': 'str', 'no_log': True, 'fallback': (env_fallback, 'ANSIBLE_NET_PASSWORD')},
        'timeout': {'type': 'int', 'fallback': (env_fallback, 'ANSIBLE_NET_TIMEOUT')}
    }
    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0

    os.environ['ANSIBLE_NET_PASSWORD'] = "mysecret"
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 1
    assert "mysecret" in no_log_values

    os.environ['ANSIBLE_NET_TIMEOUT']

# Generated at 2022-06-12 23:35:21.173224
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test no_log_values set when fallback contains no_log true
    assert set_fallbacks({'a': {'fallback': ('env_fallback', 'ANSIBLE_FALLBACK_A', 'ANSIBLE_FALLBACK_B')}}, {}) == set(['ANSIBLE_FALLBACK_A'])
    # Test no_log_values set when fallback does not contain no_log value
    assert set_fallbacks({'a': {'fallback': ('env_fallback', 'ANSIBLE_FALLBACK_A', 'ANSIBLE_FALLBACK_B')}}, {}) == set(['ANSIBLE_FALLBACK_A'])
    # Test no_log_values empty when fallback value is empty

# Generated at 2022-06-12 23:35:25.349275
# Unit test for function sanitize_keys
def test_sanitize_keys():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    test_data = b'''---
- key1: value1
- key2: value2
- key3: value3
- key4:
    - k1: v1
    - k2: v2
    - k3: v3
'''
    no_log = set(['value1'])
    loader = AnsibleLoader(None, yaml_warnings=True)
    data = loader.get_single_data(test_data)
    dumper = AnsibleDumper(sort_tags=False)

    sanitized_data = sanitize_keys

# Generated at 2022-06-12 23:35:29.891932
# Unit test for function sanitize_keys
def test_sanitize_keys():
    test_cases = dict()
    # sanitize_keys(obj, no_log_strings, ignore_keys=frozenset())
    # test cases for no_log_strings
    test_cases[0] = ({'a': 'b', 'c': 'd'}, {'a': 'b', 'c': 'd'}, frozenset(), set())
    test_cases[1] = ({'a': 'b', 'c': 'd'}, {'a': 'b', 'c': 'd'}, frozenset(), set(['c']))
    test_cases[2] = ({'a': 'b', 'c': 'd'}, {'a': 'b', 'c': 'd'}, frozenset(), set(['_ansible_foo']))

# Generated at 2022-06-12 23:35:36.313751
# Unit test for function remove_values
def test_remove_values():
    '''
    We don't want to add a dependency of ansible on unit test frameworks, so
    the functions that we want to unit test are added to a list and the main
    function invokes the unit test functions for each element in the list.
    '''
    list_of_functions = remove_values
    # Dictionary containing the unit test functions
    dict_of_test_functions = {
        'remove_values': test_remove_values,
    }
    # Run the unit tests
    for func in list_of_functions:
        print('Testing function %s' % func)
        dict_of_test_functions[func]()



# Generated at 2022-06-12 23:36:12.191585
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test for the function set_fallbacks"""
    argument_spec = dict(
        name=dict(type='str'),
        password=dict(type='str', no_log=True),
        key_file=dict(type='str', fallback=(env_fallback,)),
        crt_file=dict(type='str', fallback=(env_fallback, ('SSL_CERT_DIR', 'SSL_CERT_FILE'))),
        crt_dir=dict(type='str', fallback=(env_fallback, ('SSL_CERT_DIR', 'SSL_CERT_FILE'))),
    )
    parameters = dict(name='ansible')
    no_log_values = set_fallbacks(argument_spec, parameters)
    expected_keys = ['name']
    expected_no_log_values = set()


# Generated at 2022-06-12 23:36:23.067367
# Unit test for function sanitize_keys
def test_sanitize_keys():
    no_log_vals = set()

    assert sanitize_keys({'foobar': 1}, no_log_vals) == {'foobar': 1}

    no_log_vals.add('foobar')
    assert sanitize_keys({'foobar': 1}, no_log_vals) == {'**': 1}

    # test limit set
    assert sanitize_keys({'foobar': 1}, no_log_vals, ignore_keys=set(['foobar'])) == {'foobar': 1}

    assert sanitize_keys({'foo': {'bar': 1}}, no_log_vals) == {'foo': {'bar': 1}}


# Generated at 2022-06-12 23:36:27.594663
# Unit test for function env_fallback
def test_env_fallback():
    # set a os.env for the test
    os.environ['test_env_fallback'] = 'bozo'
    # assert we get the expected result
    assert env_fallback('test_env_fallback') == 'bozo'
    # assert we get the expected exception
    try:
        env_fallback('no_env_fallback')
    except AnsibleFallbackNotFound:
        pass
    else:
        assert False, 'unexpected behavior'



# Generated at 2022-06-12 23:36:35.416840
# Unit test for function remove_values
def test_remove_values():
    # Test Types
    # test_value = ('string', ['list', ('tuple', 'with', 'list')], {'key': 'value'}, {'key': 'value', 'key2': ['list']})
    # test_value = {'key': 'value', 'key2': ['list']}
    test_value = ['list', ('tuple', 'with', 'list')]
    # test_value = {'key': 'value'}
    # test_value = ('string', ['list', ('tuple', 'with', 'list')])
    # test_value = ['list', ('tuple', 'with', 'list')]
    # test_value = ['list', 'with', 'value']
    # test_value = ['list', 'list']
    # test_value = ['list', ['list', 'list']]

# Generated at 2022-06-12 23:36:46.359614
# Unit test for function remove_values

# Generated at 2022-06-12 23:36:48.110344
# Unit test for function env_fallback
def test_env_fallback():
    value = env_fallback('env_key')
    assert value == os.environ['env_key']


# Generated at 2022-06-12 23:36:55.067087
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert(set_fallbacks({'param': {'fallback': ('string', ('DEFAULT_INPUT',))}}, {}) == set(['string']))
    assert(set_fallbacks({'param': {'fallback': ('string', ('DEFAULT_INPUT',))}}, {'param': 'value'}) == set([]))
    assert(set_fallbacks({'param': {'fallback': ('string', ('DEFAULT_INPUT',))}}, {'param': None}) == set(['string']))
    assert(set_fallbacks({'param': {'fallback': ('env_fallback', ('DEFAULT_INPUT',))}}, {}) == set([]))

# Generated at 2022-06-12 23:37:07.316184
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback function"""

    os_env = dict(os.environ.copy())
    unittest.TestCase().assertRaises(AnsibleFallbackNotFound, env_fallback, 'HOME')
    os.environ['HOME'] = '/home/joe'
    unittest.TestCase().assertEqual(env_fallback('HOME'), '/home/joe')
    os.environ['HOME'] = '/home/joe'
    os.environ['user'] = 'joe'
    unittest.TestCase().assertEqual(env_fallback('HOME', 'user'), '/home/joe')
    os.environ['HOME'] = '/home/joe'
    os.environ['user'] = 'joe'
    os.environ['USERNAME'] = 'joe'

# Generated at 2022-06-12 23:37:11.482910
# Unit test for function sanitize_keys
def test_sanitize_keys():
    answer = {"a": 123}
    data = {'$ANSIBLE_VAULT;9.9.9;AES256': '{}'.format(json.dumps(answer))}
    sanitize_keys(data, ['$ANSIBLE_VAULT;9.9.9;AES256'])


# Generated at 2022-06-12 23:37:22.230193
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(a=dict(type='str', fallback=('from_fallback', 'FOO')))
    parameters = dict(a='fallback not called')
    no_log_values = set_fallbacks(spec, parameters)
    assert parameters['a'] == 'from_fallback'
    assert len(no_log_values) == 0
    spec = dict(
        a=dict(
            type='str',
            fallback=('from_fallback', 'FOO'),
            no_log=True
            )
        )
    parameters = dict(a='fallback not called')
    no_log_values = set_fallbacks(spec, parameters)
    assert parameters['a'] == 'from_fallback'
    assert len(no_log_values) == 1