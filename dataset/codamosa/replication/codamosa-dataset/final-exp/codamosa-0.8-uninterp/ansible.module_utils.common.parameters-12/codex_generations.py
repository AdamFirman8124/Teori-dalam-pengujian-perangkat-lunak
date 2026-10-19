

# Generated at 2022-06-12 23:28:18.282680
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'test_env_var': {
            'type': 'str',
            'fallback': (env_fallback, 'foo')
        }
    }

    parameters = {}
    test_env_var_name = 'TEST_ENV_VAR_1'
    expected_parameters = {}
    expected_no_log_values = set()

    test_env_var_value = 'test value 1'
    expected_parameters['test_env_var'] = test_env_var_value
    expected_no_log_values.add(test_env_var_value)

    # success
    os.environ[test_env_var_name] = test_env_var_value
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert_equal

# Generated at 2022-06-12 23:28:26.689934
# Unit test for function set_fallbacks
def test_set_fallbacks():
    fake_arguments_spec = dict(
        path=dict(type='path', fallback=(env_fallback, 'ANSIBLE_CONFIG', '/path/to/ansible.cfg')),
        url=dict(type='str', fallback=(env_fallback, 'ANSIBLE_URL')),
        bool_value=dict(type='bool', fallback=(env_fallback, 'ANSIBLE_BOOL')),
        timeout=dict(type='int', fallback=(env_fallback, 'ANSIBLE_TIMEOUT')),
        no_log=dict(type='str', no_log=True, fallback=(env_fallback, 'ANSIBLE_NO_LOG'))
    )
    parameters = dict(path='/path/to')
    no_log_values = set_fallbacks(fake_arguments_spec, parameters)


# Generated at 2022-06-12 23:28:32.020765
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['SHOULD_WORK'] = 'Should work'
    if env_fallback('SHOULD_WORK') != 'Should work':
        raise AssertionError()

    try:
        env_fallback('SHOULD_NOT_WORK')
        raise AssertionError()
    except AnsibleFallbackNotFound:
        pass


# Generated at 2022-06-12 23:28:37.362551
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test that fallback will work"""

    argument_spec = dict(a=dict(fallback=(env_fallback, 'TEST_ENV_VAR_A')))
    params = {}
    os.environ['TEST_ENV_VAR_A'] = 'FOO'
    assert set_fallbacks(argument_spec, params) == set(['FOO'])
    del os.environ['TEST_ENV_VAR_A']



# Generated at 2022-06-12 23:28:44.429353
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_STATS'] = 'True'
    assert env_fallback('ANSIBLE_STATS') == 'True'
    os.environ['ANSIBLE_STATS'] = ''
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_STATS')
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('FOO')


# Generated at 2022-06-12 23:28:52.942474
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:29:02.055569
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'password': {
            'type': 'str',
            'no_log': True,
            'fallback': (env_fallback, ['env_password'])
        },
    }

    parameters = {}
    assert set_fallbacks(argument_spec, parameters) == set([])
    parameters['password'] = 'banana'
    assert set_fallbacks(argument_spec, parameters) == set(['banana'])
    del parameters['password']
    os.environ['env_password'] = 'apple'
    assert set_fallbacks(argument_spec, parameters) == set(['apple'])



# Generated at 2022-06-12 23:29:11.019803
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = {"param1": {"type": "str", "fallback": (env_fallback, 'ANSIBLE_PARAM1')},
                     "param2": {"type": "str", "fallback": (env_fallback, ['ANSIBLE_PARAM2', 'OTHER_PARAM2'])},
                     "param3": {"type": "str", "fallback": (env_fallback, ['ANSIBLE_PARAM3'], {"default": "default_value"})},
                     "param4": {"type": "str", "fallback": (env_fallback, "default")}
                    }

    spec = dict(argument_spec=argument_spec)
    module = AnsibleModule(**spec)
    assert module.params['param1'] is None
    assert module.params['param2'] == 'default_value'

# Generated at 2022-06-12 23:29:20.634469
# Unit test for function remove_values
def test_remove_values():
    assert remove_values(1, ['a']) == 1
    assert remove_values('a', ['a']) == ''
    assert remove_values('a', []) == 'a'
    assert remove_values('a', ['a', 'b']) == ''
    assert remove_values('b', ['a', 'b']) == ''
    assert remove_values('a', {'a': 1}) == ''
    assert remove_values({'a': 1}, ['a']) == {}
    assert remove_values({'a': 1, 'b': 2}, ['a', 'b']) == {}
    assert remove_values(['a', 'b'], ['a', 'b']) == []

# Generated at 2022-06-12 23:29:22.834380
# Unit test for function env_fallback
def test_env_fallback():
    a = env_fallback('one','two','three')
    print (a)

# Generated at 2022-06-12 23:29:58.370403
# Unit test for function set_fallbacks
def test_set_fallbacks():  # pylint: disable=too-many-return-statements
    """Unit test for function set_fallbacks"""
    # Boolean. Ensure True/False
    argument_spec = {
        'param': dict(type='bool', fallback=(env_fallback, ['PARAM_BOOL'])),
        'param_one': dict(type='bool', fallback=(env_fallback, ['PARAM_ONE'])),
        'param_two': dict(type='bool', fallback=(env_fallback, ['PARAM_TWO'])),
        'param_three': dict(type='bool', fallback=(env_fallback, ['PARAM_THREE'])),
    }

    os.environ['PARAM_BOOL'] = 'True'
    os.environ['PARAM_ONE'] = 'false'
    os

# Generated at 2022-06-12 23:30:09.854080
# Unit test for function set_fallbacks
def test_set_fallbacks():
    class test_module_arguments:
        pass

    module_args = test_module_arguments()
    module_args.name = "testing"
    module_args.state = "present"


# Generated at 2022-06-12 23:30:17.026032
# Unit test for function set_fallbacks
def test_set_fallbacks():
    param_spec = dict(
        param1=dict(required=True, fallback=(env_fallback, ['ENV_FALLBACK'])),
        param2=dict(required=True, fallback=(env_fallback, ['ENV_FALLBACK_2'])),
    )
    parameters = dict(
        param2='param2',
    )
    expected_parameters = dict(
        param1='param1',
        param2='param2',
    )
    os.environ['ENV_FALLBACK'] = 'param1'
    os.environ.pop('ENV_FALLBACK_2', None)
    no_log_values = set_fallbacks(param_spec, parameters)
    assert not no_log_values
    assert parameters == expected_parameters



# Generated at 2022-06-12 23:30:21.367051
# Unit test for function set_fallbacks
def test_set_fallbacks():
    error_message = "Error message does not match expected output"
    test_parameters = {}
    test_spec = {'test_one': {'type': 'int', 'fallback': (42, )}, 'test_two': {'type': 'int', 'fallback': (env_fallback, 'TEST_TWO', )}, 'test_three': {'type': 'str', 'fallback': (env_fallback, 'TEST_THREE', )}}
    os.environ["TEST_TWO"] = "25"
    os.environ["TEST_THREE"] = "ansible"
    expected_output = {"test_one": 42, "test_two": 25, "test_three": "ansible"}
    assert set_fallbacks(test_spec, test_parameters) == expected_output, error

# Generated at 2022-06-12 23:30:30.835660
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test default value
    argument_spec = dict(
        a=dict(default=3),
    )
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == dict(a=3), parameters
    assert no_log_values == set(), no_log_values

    # Test env_var fallback
    argument_spec = dict(
        a=dict(fallback=(env_fallback, 'FOO')),
    )
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {}, parameters
    assert no_log_values == set(), no_log_values

    os.environ['FOO'] = 'BAR'
    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:30:42.100359
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:30:50.087852
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'file': {'fallback': (env_fallback, 'ANSIBLE_CONFIG')}}, {}) == set()
    assert set_fallbacks({'file': {'fallback': (env_fallback, 'ANSIBLE_CONFIG')}}, {'file': 'foo'}) == set()
    os.environ['ANSIBLE_CONFIG'] = 'bar'
    assert set_fallbacks({'file': {'fallback': (env_fallback, 'ANSIBLE_CONFIG')}}, {}) == set(['bar'])
    assert set_fallbacks({'file': {'fallback': (env_fallback, 'ANSIBLE_CONFIG')}}, {'file': 'foo'}) == set()
    del os.environ['ANSIBLE_CONFIG']



# Generated at 2022-06-12 23:30:52.282956
# Unit test for function env_fallback
def test_env_fallback():
    value = env_fallback('TEST_VALUE', 'TEST_VALUE_2')
    assert value == 'some_value'



# Generated at 2022-06-12 23:30:54.299304
# Unit test for function sanitize_keys
def test_sanitize_keys():
    obj = {'_ansible_no_log': 'True', 'not_logged': 'top'}
    no_log_strings = set(obj.values())
    _sanitize_keys_conditions(obj, no_log_strings, set(), None)



# Generated at 2022-06-12 23:31:01.866491
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        one=dict(
            fallback=(env_fallback, 'ONE')
        ),
        two=dict(
            fallback=(env_fallback, 'TWO', 'THREE', dict(default=42))
        ),
        three=dict(
            fallback=(env_fallback, dict(default=False))
        ),
        four=dict(
            fallback=(env_fallback, 'FOUR', 'FIVE')
        ),
    )
    parameters = dict(
        one='x',
        two='x',
        three='x',
        four='x',
    )
    no_log_values = set()
    # Set and save environment variables
    backup_ONE = os.environ.pop('ONE', None)

# Generated at 2022-06-12 23:31:38.374336
# Unit test for function remove_values
def test_remove_values():
    """Unit test for function remove_values"""


# Generated at 2022-06-12 23:31:42.807970
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback"""

    os.environ['FOO'] = 'bar'
    assert env_fallback('FOO') == 'bar'
    try:
        env_fallback('BAR')
        assert False
    except AnsibleFallbackNotFound:
        pass


# Generated at 2022-06-12 23:31:51.309733
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = dict(a=1, b=2, c=3, d=dict(dd=1))
    spec = dict(a=dict(type='str', fallback=('env', 'A')),
                b=dict(type='str', fallback=('env', 'B')),
                c=dict(type='str', fallback=('env', 'C')),
                d=dict(type='dict', fallback=('env', 'D'), options=dict(dd=dict(type='str'))),
                x=dict(type='str', fallback=('env', 'X')),
                y=dict(type='str', fallback=('env', 'Y')),
                z=dict(type='str', fallback=('env', 'Z')))

    os.environ['A'] = 'a'

# Generated at 2022-06-12 23:31:57.804666
# Unit test for function env_fallback
def test_env_fallback():

    assert env_fallback('HOME') == os.environ['HOME']
    assert env_fallback('HOME', 'HOMEPATH') == os.environ['HOME']
    assert env_fallback('HOMEPATH') == os.environ['HOMEPATH']

    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('THIS_ENV_VAR_IS_NOT_DEFINED')



# Generated at 2022-06-12 23:32:08.426862
# Unit test for function remove_values
def test_remove_values():
    assert remove_values("0", ['']) == "0"
    assert remove_values("0", ['0']) == ''
    assert remove_values("aaa", ['a']) == ''
    assert remove_values("aaa", ['a', 'aa']) == ''
    assert remove_values("xyz", ['a', 'aa']) == 'xyz'
    assert remove_values("ababa", ['aba']) == 'aba'
    assert remove_values("ababa", ['ab']) == ''
    assert remove_values("ababa", ['a', 'b']) == ''
    assert remove_values("ababa", ['a', 'b', 'x']) == ''
    assert remove_values("ababa", ['x', 'y']) == 'ababa'

# Generated at 2022-06-12 23:32:17.386101
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """
    Test set_fallbacks function
    """
    # Test with fallback.

# Generated at 2022-06-12 23:32:26.937994
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'foo': {'fallback': (env_fallback, 'MYVAR')}}
    parameters = {}
    set_fallbacks(argument_spec, parameters)

    assert parameters.get('foo') is None

    os.environ['MYVAR'] = 'spam'
    set_fallbacks(argument_spec, parameters)

    assert parameters.get('foo') == 'spam'
    assert parameters.get('bar') is None

    argument_spec = {'foo': {'fallback': (env_fallback, 'MYVAR1', 'MYVAR2')}}
    parameters = {}
    set_fallbacks(argument_spec, parameters)

    assert parameters.get('foo') is None
    assert parameters.get('bar') is None


# Generated at 2022-06-12 23:32:38.857791
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'name': dict(),
        'password': dict(fallback=(env_fallback, 'ANSIBLE_NET_PASSWORD')),
        'sshkey': dict(default=None, type='str'),
        'authorize': dict(default=False, type='bool'),
        'auth_pass': dict(no_log=True)
    }
    parameters = dict(name='test', authorize=True)
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters['password'] == 'VALIDATE_PASSWORD'

    parameters = dict(name='test', authorize=True, password='foo')
    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:32:50.330161
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # test no_log
    argument_spec = {'test': {'required': True, 'type': 'str', 'fallback': (env_fallback, 'TEST_ENV'), 'no_log': True}}
    parameters = {}
    os.environ['TEST_ENV'] = 'test_value'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set(['test_value']), "no_log_values must be set(['test_value'])"
    assert parameters['test'] == 'test_value', "parameters['test'] must be 'test_value'"

    # test already present
    parameters = {'test': 'test_value'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_

# Generated at 2022-06-12 23:32:57.685112
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'BAR'
    assert env_fallback('FOO') == 'BAR'
    del os.environ['FOO']
    try:
        env_fallback('FOO')
        assert False, "env_fallback failed to raise exception for missing env var"
    except AnsibleFallbackNotFound:
        pass
    try:
        env_fallback()
        assert False, "env_fallback failed to raise exception for missing env var"
    except AnsibleFallbackNotFound:
        pass
    assert env_fallback('FOO', 'BAR') == 'BAR'
    assert env_fallback('FOO', 'BAR', 'BAZ') == 'BAR'
    # Test keyword argument (unused by this function but required
    # by the decorator)

# Generated at 2022-06-12 23:33:31.174061
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_FOO_BAR'] = "1"
    assert env_fallback("ANSIBLE_FOO_BAR") == "1"
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback("ANSIBLE_FOO_BAZ")
    del os.environ['ANSIBLE_FOO_BAR']



# Generated at 2022-06-12 23:33:42.249980
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        "param1": {"nested_options": {"param2": {'type': 'str', 'default': 'default value', 'fallback': (env_fallback, 'ANSIBLE_PARAM2')}}, "type": 'dict'}
    }
    #doesn't exist in parameters, doesn't exist in env
    parameters = {'param1': {}}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['param1']['param2'] == 'default value'
    assert len(no_log_values) == 0

    os.environ['ANSIBLE_PARAM2'] = 'test value'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['param1']['param2'] == 'test value'
   

# Generated at 2022-06-12 23:33:44.695245
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('ANSIBLE_A', 'ANSIBLE_B') in ['ANSIBLE_A', 'ANSIBLE_B']


# Generated at 2022-06-12 23:33:52.037974
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(fallback=(env_fallback, 'FOO')),
        bar=dict(fallback=(env_fallback, 'BAR')),
        baz=dict(fallback=(env_fallback, 'BAZ', dict(fallback=(env_fallback, 'BAZ2'), no_log=True)))
    )

    os.environ['FOO'] = 'a'
    os.environ['BAZ'] = 'b'

    parameters = dict(
        foo='c',
        bar='d'
    )

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert parameters['foo'] == 'c'
    assert parameters['bar'] == 'd'
    assert parameters['baz'] == 'b'

# Generated at 2022-06-12 23:34:03.553415
# Unit test for function set_fallbacks
def test_set_fallbacks():
    fallback_list = [{'fallback': [call_with_args, dict(default=5), dict(default=10)]},
                     {'fallback': [call_with_args, dict(default=15), dict(default=20)]},
                     {'fallback': [call_with_args, dict(default=25), dict(default=30)]}]
    fallback_dict = {'fallback': [call_with_args, dict(default=5), dict(default=10)],
                     'fallback2': {'fallback': [call_with_args, dict(default=15), dict(default=20)]},
                     'fallback3': {'fallback': [call_with_args, dict(default=25), dict(default=30)]}}

# Generated at 2022-06-12 23:34:07.590190
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_MODULE_TEST_ENV_1'] = 'test_env_fallback'
    assert env_fallback('ANSIBLE_MODULE_TEST_ENV_1') == 'test_env_fallback'
    del os.environ['ANSIBLE_MODULE_TEST_ENV_1']
    try:
        env_fallback('ANSIBLE_MODULE_TEST_ENV_1')
        assert False, 'should have thrown AnsibleFallbackNotFound'
    except AnsibleFallbackNotFound:
        pass


# Generated at 2022-06-12 23:34:16.254206
# Unit test for function set_fallbacks
def test_set_fallbacks():

    # TEST 1: One value set through fallback function
    argument_spec = {
        'param1': {'type': 'str', 'fallback': (env_fallback, 'PARAM1')},
        'param2': {'type': 'str', 'no_log': True, 'fallback': (env_fallback, 'PARAM2')},
        'param3': {'type': 'str', 'fallback': (None,)},
        'param4': {'type': 'str', 'fallback': (env_fallback, 'PARAM4', {'my_arg': 'my_value'})},
    }
    parameters = {'param3': 'default'}
    os.environ['PARAM1'] = 'env_value'
    os.environ['PARAM2'] = 'env_value'
    set

# Generated at 2022-06-12 23:34:26.430705
# Unit test for function set_fallbacks
def test_set_fallbacks():
    res = set_fallbacks(
        {
            'a': {'type': 'dict', 'options': {'b': {'type': 'int'}, 'c': {'type': 'int'}}},
            'd': {'type': 'list', 'elements': 'dict', 'options': {'b': {'type': 'int'}, 'c': {'type': 'int'}}},
            'e': {'type': 'list'}
        }, {
            'd': [{'b': 1}, {'b': 2}],
            'e': [{'b': 1}, {'b': 2}],
            'f': 'text'
        }
    )
    assert set() == res



# Generated at 2022-06-12 23:34:37.332513
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'foo': {'type': 'str'}, 'foo_fallback': {'type': 'str', 'fallback': ('env_fallback', 'bar')},
                     'bar': {'type': 'str'}, 'bar_fallback': {'type': 'str', 'fallback': ('env_fallback', 'foo')}}
    parameters = {'foo': 'foo'}

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert parameters == {'foo': 'foo', 'foo_fallback': 'bar'}
    assert no_log_values == set()

    parameters = {'bar': 'bar'}
    os.environ['bar'] = 'foobar'

    no_log_values = set_fallbacks(argument_spec, parameters)


# Generated at 2022-06-12 23:34:39.586650
# Unit test for function env_fallback
def test_env_fallback():
   os.environ['ANSIBLE_TEST'] = 'test'
   assert env_fallback('ANSIBLE_TEST') == 'test'
   os.environ.pop('ANSIBLE_TEST')
   with pytest.raises(AnsibleFallbackNotFound):
       env_fallback('ANSIBLE_TEST')



# Generated at 2022-06-12 23:35:20.022847
# Unit test for function sanitize_keys
def test_sanitize_keys():
    # Testing for dictionaries
    test_dict = {'test_key': 'test_value', 'test_key_no_log': 'test_value', 'test_key_no_log2': 'test_value'}
    test_dict_no_log = {'test_key_no_log': 'test_value', 'test_key_no_log2': 'test_value'}
    test_dict_no_log_sanitized = {'test_key': 'test_value'}
    test_dict_sanitized = {'test_key': 'test_value'}
    no_log_values = set()
    for key, value in test_dict_no_log.items():
        no_log_values.add(value)

# Generated at 2022-06-12 23:35:29.985155
# Unit test for function env_fallback
def test_env_fallback():
    args = []
    kwargs = {}

    with env_var('TEST_FOO', 'bar'):
        args.append('TEST_FOO')
        assert env_fallback(*args, **kwargs) == 'bar'

    with env_var('TEST_FOO', 'baz'):
        args.append('TEST_FOO')
        assert env_fallback(*args, **kwargs) == 'bar'

    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('TEST_BAR', 'TEST_BAZ')



# Generated at 2022-06-12 23:35:37.269938
# Unit test for function set_fallbacks
def test_set_fallbacks():
    def _test(test_args, test_fallback, test_value, expected_args, expected_kwargs, expected_value):
        spec = {'a': {'type': 'str', 'fallback': test_fallback}}
        p = {'a': test_value}
        set_fallbacks(spec, p)
        assert expected_args == test_args
        assert expected_kwargs == test_kwargs
        assert expected_value == p['a']

    def test_callable(args, kwargs):
        test_args.extend(args)
        test_kwargs.update(kwargs)
        return 'test_callable'

    test_args = []
    test_kwargs = {}
    # no fallback

# Generated at 2022-06-12 23:35:47.480462
# Unit test for function remove_values
def test_remove_values():
    assert remove_values("foo", ["foo"]) == ""
    assert remove_values("foo", ["foo", "bar"]) == ""
    assert remove_values("foo bar", ["foo", "bar"]) == ""
    assert remove_values("foo bar", ["bar", "foo"]) == ""
    assert remove_values("foobar", ["foo", "bar"]) == "foobar"
    assert remove_values("foobar", ["foo", "bar", "fbar"]) == ""
    assert remove_values("foobar", ["foo", "bar", "foobar"]) == ""

    assert remove_values(["foo", "foo bar", "foobar", "foobar"], ["foo", "bar"]) == ["", "", "foobar", "foobar"]

# Generated at 2022-06-12 23:35:52.452664
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ONE'] = 'ONE'
    try:
        assert env_fallback('ONE') == 'ONE'
        assert env_fallback('TWO') == None
    finally:
        del os.environ['ONE']



# Generated at 2022-06-12 23:35:58.785056
# Unit test for function env_fallback
def test_env_fallback():
    assert os.environ['PATH'] == env_fallback('PATH')
    assert os.environ['LANG'] == env_fallback('LANG')
    assert os.environ['LC_CTYPE'] == env_fallback('LC_CTYPE')
    assert os.environ['XDG_RUNTIME_DIR'] == env_fallback('XDG_RUNTIME_DIR')



# Generated at 2022-06-12 23:36:05.869363
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # given multiple fallbacks when only one provides a value then that value should be used
    argument_spec = {
        'b': {
            'type': 'bool',
            'fallback': (env_fallback, None, {'default': True}),
        }
    }
    parameters = {
        'a': False
    }
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['b'] is True
    assert no_log_values == set()

    # given multiple fallbacks when all fallbacks provide a value then the first value should be used
    argument_spec = {
        'b': {
            'type': 'bool',
            'fallback': (env_fallback, None, False, True),
        }
    }
    parameters = {
        'a': False
    }

# Generated at 2022-06-12 23:36:14.746512
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:36:23.810901
# Unit test for function env_fallback
def test_env_fallback():
    '''Unit test for env_fallback function'''
    def get_env(e):
        # side effect helper to simulate env variables
        os.environ[e] = e
    # test first arg
    get_env("FOO")
    assert env_fallback("FOO", "BAR") == "FOO"
    # test second arg
    get_env("BAR")
    assert env_fallback("FOO", "BAR") == "BAR"
    # test no args
    try:
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback("FOO", "BAR")
    finally:
        # clean up env vars
        os.environ.pop("FOO")
        os.environ.pop("BAR")



# Generated at 2022-06-12 23:36:32.866383
# Unit test for function remove_values
def test_remove_values():
    assert remove_values([1, 2, {3: 4}, 5], set()) == [1, 2, {3: 4}, 5]
    assert remove_values([1, 2, {3: 4, 'password': 'secret'}, 5], set()) == [1, 2, {3: 4, 'password': 'secret'}, 5]
    assert remove_values([1, 2, {3: 4, 'password': 'secret'}, 5], {'secret'}) == [1, 2, {3: 4, 'password': 'SANITIZED'}, 5]
    assert remove_values([1, 2, {3: 4, 'password': 'secret'}, 5], {'secret', '4'}) == [1, 2, {'password': 'SANITIZED'}, 5]

# Generated at 2022-06-12 23:37:38.011823
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit tests for function set_fallbacks"""