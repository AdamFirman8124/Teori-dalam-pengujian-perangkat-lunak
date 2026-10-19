

# Generated at 2022-06-12 23:28:16.356850
# Unit test for function env_fallback
def test_env_fallback():
    # Set env variable
    os.environ['ANSIBLE_TEST'] = 'testing'
    # Make sure it's in the env
    assert 'ANSIBLE_TEST' in os.environ
    assert env_fallback('ANSIBLE_TEST', 'NOT_FOUND') == 'testing'
    # Make sure it doesn't find anything in the env
    assert env_fallback('NOT_FOUND') == 'NOT_FOUND'


# Session attributes (set by connection plugins)

# Generated at 2022-06-12 23:28:25.290562
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test parameters return fallback value"""

    argument_spec = {'greeting': {'type': 'str', 'default': 'Hello,', 'fallback': (env_fallback, 'ANSIBLE_GREETING', 'ANSIBLE_HOST'), 'no_log': True}}
    module = Mock()
    module.params = {'name': 'World'}

    # We should get fallback values from the environment
    os.environ['ANSIBLE_GREETING'] = 'Hi, everyone!'
    os.environ['ANSIBLE_HOST'] = 'localhost'
    no_log_values = set_fallbacks(argument_spec, module.params)
    assert module.params['greeting'] == 'Hi, everyone!'
    assert 'Hi, everyone!' in no_log_values

    # We should get the default
    argument

# Generated at 2022-06-12 23:28:32.002546
# Unit test for function env_fallback
def test_env_fallback():

    if not is_py2:
        from io import StringIO
    else:
        from StringIO import StringIO

    # Monkey patch os.environ
    output = StringIO()
    old_stderr = sys.stderr
    sys.stderr = output
    tmp_env = dict(list(os.environ.items()) + [('ANSIBLE_FOO_BAR', 'foobar')])
    os.environ.clear()
    os.environ.update(tmp_env)

# Generated at 2022-06-12 23:28:38.867597
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(type='str', fallback=(env_fallback, 'ANSIBLE_FOO')),
        bar=dict(type='str', fallback=(env_fallback, 'ANSIBLE_BAR'), no_log=True)
    )
    parameters = dict(foo='a', baz='b')
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters.get('bar') == os.environ['ANSIBLE_BAR']
    assert parameters.get('bar') in no_log_values



# Generated at 2022-06-12 23:28:49.837996
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:28:54.261242
# Unit test for function env_fallback
def test_env_fallback():
    """Unit test for function env_fallback"""
    assert env_fallback('THIS_DOES_NOT_EXIST') == AnsibleFallbackNotFound



# Generated at 2022-06-12 23:28:56.020512
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback() == AnsibleFallbackNotFound



# Generated at 2022-06-12 23:29:06.408365
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test that function sets the fallback parameters.
    specs = dict(
        a=dict(type='int', fallback=(env_fallback, 'A')),
        b=dict(type='int', fallback=(env_fallback, 'B')),
        c=dict(type='bool', fallback=(env_fallback, 'C')),
        d=dict(type='str', fallback=(env_fallback, 'D'))
    )
    params = dict(b=2)
    set_fallbacks(specs, params)
    assert params['a'] == '1'
    assert params['b'] == 2
    assert params['c'] == True
    assert params['d'] == 'foo'

    # Test that function skips setting parameters to None.

# Generated at 2022-06-12 23:29:10.326566
# Unit test for function set_fallbacks
def test_set_fallbacks():
    module = AnsibleModule(
        argument_spec={'HTTP_PROXY': {'type': 'str', 'fallback': (env_fallback, ['http_proxy', 'HTTP_PROXY'])}})
    set_fallbacks(module.argument_spec, module.params)

    assert module.params['HTTP_PROXY'] == os.environ['HTTP_PROXY']



# Generated at 2022-06-12 23:29:20.597186
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({}, {}) == set()

    assert set_fallbacks({'a': {'type': 'str', 'fallback': (env_fallback, 'FOO', 'BAR')}}, {}) == set()
    assert set_fallbacks({'a': {'type': 'str', 'fallback': (env_fallback, 'FOO', 'BAR')}}, {}) == set()
    assert set_fallbacks({'a': {'type': 'str', 'fallback': (env_fallback, 'FOO')}}, {}) == set()
    assert set_fallbacks({'a': {'type': 'str', 'fallback': (env_fallback, 'FOO')}}, {}) == set()

    os.environ['FOO'] = 'asdf'
    assert set_fallbacks

# Generated at 2022-06-12 23:29:55.342131
# Unit test for function env_fallback
def test_env_fallback():
    tests = (
        ('TEST_ENV', 'TEST_ENV_VALUE', {'TEST_ENV': 'TEST_ENV_VALUE'}, {}),
        ('TEST_ENV', 'TEST_ENV_VALUE', {}, {'TEST_ENV': 'TEST_ENV_VALUE'}),
        # Test that AnsibleFallbackNotFound is raised
        ('TEST_ENV', 'TEST_ENV_VALUE', {}, {})
    )

    for test_args in tests:
        test_env_var, test_env_value, env, os_env_overwrite = test_args
        test_env_var_tmp = test_env_var + '_TMP'
        test_env_value_tmp = test_env_value + '_TMP'

# Generated at 2022-06-12 23:30:07.810832
# Unit test for function set_fallbacks
def test_set_fallbacks():
    sample_argument_spec = dict(
        foo=dict(type='str', fallback=(env_fallback, ['ANSIBLE_FOO', 'FOO'])),
        bar=dict(type='str', fallback=(env_fallback, ['ANSIBLE_BAR', 'BAR'])),
        baz=dict(type='str', fallback=(env_fallback, ['ANSIBLE_BAZ', 'BAZ'])),
        bam=dict(type='int', fallback=(env_fallback, ['ANSIBLE_BAM', 'BAM'])),
    )

    # No values in either the spec or in environment: default value will be used
    parameters = dict(
        foo=None,
        bar=None,
        baz=None,
        bam=None,
    )

# Generated at 2022-06-12 23:30:11.923473
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test with custom fallback function
    fallback_spec = dict(
        myparam=dict(type='str', fallback=(env_fallback, ['MYPARAM']))
    )
    parameters = {}
    with set_env_var('MYPARAM', 'ansible'):
        assert set_fallbacks(fallback_spec, parameters) == set()
        assert parameters == dict(myparam='ansible')

    # Test with function env_fallback
    fallback_spec = dict(
        myparam=dict(type='str', fallback=('env', ['MYPARAM']))
    )
    parameters = {}
    with set_env_var('MYPARAM', 'ansible'):
        assert set_fallbacks(fallback_spec, parameters) == set()
        assert parameters == dict(myparam='ansible')



# Generated at 2022-06-12 23:30:23.066532
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys(1, 'asdf') == 1
    assert sanitize_keys('asdf', 'asdf') == 'asdf'
    assert sanitize_keys('asdf', ['asdf']) == 'asdf'
    assert sanitize_keys(['a', 'asdf'], 'asdf') == ['a', 'asdf']
    assert sanitize_keys(['a', 'asdf'], ['asdf']) == ['a', 'asdf']
    assert sanitize_keys(['a', 'asdf'], ['asdf'], ignore_keys=['b']) == ['a', 'asdf']
    assert sanitize_keys(['a', 'asdf'], ['asdf'], ignore_keys=['a']) == ['a', 'asdf']

    # Check assumptions

# Generated at 2022-06-12 23:30:31.749779
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Tests for passing
    fallback_spec = dict(param1=dict(fallback=(env_fallback, 'TEST1')))
    fallback_parameters = dict(param2="value2")
    fallback_value = "test1value"
    os.environ['TEST1'] = fallback_value
    no_log_values = set_fallbacks(fallback_spec, fallback_parameters)
    assert fallback_parameters['param1'] is fallback_value
    assert fallback_value not in no_log_values
    del os.environ['TEST1']
    fallback_spec = dict(param1=dict(fallback=(env_fallback, dict(var='TEST1'))))
    fallback_parameters = dict(param2="value2")

# Generated at 2022-06-12 23:30:42.915974
# Unit test for function sanitize_keys
def test_sanitize_keys():

    # Set up a mock module to pass to _sanitize_keys()
    module_name = 'fake_module'
    module_args = {'passwords': ['foo', 'bar', 'baz'], 'others': ['foo', 'bar', 'baz']}
    module_kwargs = {'_ansible_no_log': True}
    params = {'PASSWORD': 'foo', 'password': 'foo', }
    tmp = collections.namedtuple('tmp', ['params'])
    module = tmp(params=params)
    tmp = collections.namedtuple('tmp', ['name', 'args', 'kwargs'])
    module = tmp(name=module_name, args=module_args, kwargs=module_kwargs)
    no_log_values = set([])

# Generated at 2022-06-12 23:30:54.447440
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        param1=dict(fallback=(env_fallback, ['TEST_PARAM_1'])),
        param2=dict(fallback=(env_fallback, 'TEST_PARAM_2')),
        param3=dict(fallback=(env_fallback, 'TEST_PARAM_3'))
    )
    parameters = dict()
    os.environ['TEST_PARAM_1'] = 'value1'
    os.environ['TEST_PARAM_2'] = 'value2'

    set_fallbacks(argument_spec, parameters)
    assert parameters['param1'] == 'value1'
    assert parameters['param2'] == 'value2'
    assert 'param3' not in parameters


# Generated at 2022-06-12 23:30:58.767590
# Unit test for function env_fallback
def test_env_fallback():
    env_var = 'SHOULD_BE_A_ENV_VAR'
    os.environ[env_var] = 'bar'
    assert env_fallback(env_var) == 'bar'
    os.environ[env_var] = 'foo'
    assert env_fallback(env_var) == 'foo'


# Generated at 2022-06-12 23:31:09.332737
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test set_fallbacks - assert that specified fallback works as expected"""

# Generated at 2022-06-12 23:31:18.421679
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:31:51.404841
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:32:01.454736
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = {}

    # Tests for param not in parameters
    no_log_value = set()
    assert set_fallbacks({'param1': {'fallback': ['env_fallback', 'TEST_ENV1']}}, params) == no_log_value
    assert set_fallbacks({'param1': {'fallback': ['env_fallback', 'TEST_ENV2']}}, params) == no_log_value
    assert set_fallbacks({'param1': {'fallback': ['env_fallback', 'TEST_ENV3']}}, params) == no_log_value

    # Tests for param in parameters
    assert set_fallbacks({'param1': {'fallback': ['env_fallback', 'TEST_ENV1']}}, {'param1': 'param1'}) == no

# Generated at 2022-06-12 23:32:13.296267
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test empty fallbacks case
    assert set_fallbacks({}, {}) == set()

    # Test None fallback case
    assert set_fallbacks({'option': {'type': 'str', 'fallback': None}}, {}) == set()
    assert set_fallbacks({'option': {'type': 'str', 'fallback': (None,)}}, {}) == set()

    # Test fail case for env fallback
    assert set_fallbacks({'option': {'type': 'str', 'fallback': (env_fallback, 'not_set_env')}}, {}) == set()

    # Test success case for env fallback
    os.environ['env_value'] = 'A'

# Generated at 2022-06-12 23:32:23.924731
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'name': {'type': 'str', 'required': True, 'fallback': (env_fallback, ('ANSIBLE_MODULE_TEST_NAME',))}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['name'] == os.environ['ANSIBLE_MODULE_TEST_NAME']
    assert no_log_values == set()

    argument_spec = {'name': {'type': 'str', 'required': True, 'no_log': True, 'fallback': (env_fallback, ('ANSIBLE_MODULE_TEST_NAME',))}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:32:27.123083
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'bar'
    assert env_fallback('FOO') == 'bar'
    del os.environ['FOO']
    try:
        env_fallback('FOO')
        assert False
    except AnsibleFallbackNotFound:
        pass



# Generated at 2022-06-12 23:32:32.495632
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_JINJA2_NATIVE'] = "1"
    os.environ['ANSIBLE_YAML_ROUNDTRIP'] = "0"
    os.environ['ANSIBLE_DEBUG'] = "1"
    os.environ['ANSIBLE_CONFIG'] = "./test/unit/plugins/modules/ansible.cfg"
    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = "0"
    os.environ['ANSIBLE_NOCOWS'] = "1"
    os.environ['ANSIBLE_RETRY_FILES_ENABLED'] = "True"
    os.environ['ANSIBLE_ROLES_PATH'] = "/etc/ansible/roles:/opt/ansible/roles:/usr/share/ansible/roles"
   

# Generated at 2022-06-12 23:32:37.822846
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'test_param': {'type': 'bool', 'fallback': (env_fallback, 'TEST_PARAM')}}
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'test_param': False}
    assert no_log_values == set()


# Generated at 2022-06-12 23:32:49.326515
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'param': {'type': 'str', 'fallback': (env_fallback, 'TEST_PARAM')},
        'key_file': {'type': 'path', 'fallback': (env_fallback, 'TEST_KEY_FILE')},
    }
    data = {}
    set_fallbacks(spec, data)
    assert 'param' in data and 'key_file' in data

    data = {'param': 'foobar'}
    set_fallbacks(spec, data)
    assert 'param' in data and 'key_file' in data
    assert data['param'] == 'foobar'


# Generated at 2022-06-12 23:32:53.494147
# Unit test for function env_fallback
def test_env_fallback():
    assert None == env_fallback(str(uuid.uuid4()), str(uuid.uuid4()))
    try:
        env_fallback()
    except AnsibleFallbackNotFound:
        pass



# Generated at 2022-06-12 23:32:57.223573
# Unit test for function env_fallback
def test_env_fallback():
    from ansible.errors import AnsibleFallbackNotFound

    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('missing_env', 'other_var')

    assert env_fallback('ANSIBLE_TEST_ENV_VAR') == 'true'



# Generated at 2022-06-12 23:33:24.113523
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_NET_USERNAME'] = 'foo'
    found = env_fallback('ANSIBLE_NET_USERNAME')
    assert found == 'foo'

    with pytest.raises(AnsibleFallbackNotFound):
        none_found = env_fallback('NOT_DEFINED')



# Generated at 2022-06-12 23:33:32.668263
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test set_fallbacks"""

    argument_spec = {'foo': {'type': 'str', 'fallback': (env_fallback, ['FOO_ENV'])},
                     'bar': {'type': 'str', 'fallback': (env_fallback, ['BAR_ENV'], {'fallback_value': 'bar_value'})},
                     'baz': {'type': 'str', 'fallback': env_fallback, 'fallback_args': ['BAZ_ENV']},
                     'none_value': {'type': 'str', 'fallback': (env_fallback, ['NONE_VALUE_ENV'], {'fallback_value': None})}}

# Generated at 2022-06-12 23:33:44.653582
# Unit test for function set_fallbacks
def test_set_fallbacks():
    class Test(unittest.TestCase):
        # TODO: Add more test cases
        def _assert_parameters_are_set(self, expected_parameters, expected_no_log_values):
            def _fake_fallback(*args, **kwargs):
                for arg in args:
                    if arg in os.environ:
                        return os.environ[arg]
                return 42

# Generated at 2022-06-12 23:33:51.360614
# Unit test for function sanitize_keys
def test_sanitize_keys():
    sample_data = {'key_with_no_log_value_as_prefix': 'some_value',
                   'key_with_no_log_value': 'some_value',
                   'key_with_no_log_value_as_suffix': 'some_value'}
    no_log_strings = frozenset(['value'])
    assert sanitize_keys(sample_data, no_log_strings) == {'key_with_no_log_val': 'some_value',
                                                          'key_with_no_log_val': 'some_value',
                                                          'key_with_no_log_val': 'some_value'}



# Generated at 2022-06-12 23:34:02.804196
# Unit test for function remove_values
def test_remove_values():
    """This function tests the function remove_values"""
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    my_list = ['value1', 'value2', 'value3']
    my_set = frozenset(('value1', 'value2', 'value3'))
    my_tuple = ('value1', 'value2', 'value3')
    no_log_dict = remove_values(my_dict, {'value1'})
    no_log_list = remove_values(my_list, {'value1'})
    no_log_set = remove_values(my_set, {'value1'})
    no_log_tuple = remove_values(my_tuple, {'value1'})
    assert no_log

# Generated at 2022-06-12 23:34:05.440303
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback()"""
    assert env_fallback() == AnsibleFallbackNotFound
    assert env_fallback('FOO') == AnsibleFallbackNotFound
    os.environ['FOO'] = 'bar'
    assert env_fallback('FOO') == 'bar'
    del os.environ['FOO']


# Generated at 2022-06-12 23:34:14.890432
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'a': dict(type='raw', fallback=('env_fallback', 'A'), no_log=True),
        'b': dict(type='raw', fallback=('env_fallback', 'B'), no_log=True),
        'c': dict(type='raw', fallback=('env_fallback', 'C'), no_log=True),
        'd': dict(type='dict', fallback=('env_fallback', 'D'), no_log=True),
    }
    parameters = {
        'a': None,
        'b': None,
        'd': None,
    }

    no_log_values = set()
    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:34:21.132547
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """Unit tests for function sanitize_keys"""
    assert sanitize_keys({}, ('foo',)) == {}
    assert sanitize_keys({'foo': 1}, ('foo',)) == {'****': 1}
    assert sanitize_keys({'foo': 1}, ('foo',), ignore_keys=['bar']) == {'foo': 1}
    assert sanitize_keys({'foo': [1, 2, 3]}, ('foo',)) == {'****': [1, 2, 3]}
    assert sanitize_keys({'foo': [1, 2, 3]}, ('foo',), ignore_keys=['bar']) == {'foo': [1, 2, 3]}


# Generated at 2022-06-12 23:34:25.445385
# Unit test for function env_fallback
def test_env_fallback():
    with set_env_var('ANSIBLE_FOO', 'bar'):
        assert env_fallback('ANSIBLE_FOO') == 'bar'
        assert env_fallback(None, 'ANSIBLE_FOO') == 'bar'
        assert env_fallback('ANSIBLE_FOO', 'ANSIBLE_BAR', 'ANSIBLE_FOO') == 'bar'
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('not-set')
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('not-set', 'ANSIBLE_FOO', 'ANSIBLE_BAR')



# Generated at 2022-06-12 23:34:29.935780
# Unit test for function env_fallback
def test_env_fallback():
    """Test loading value from environment variable"""
    assert env_fallback('UNKNOWN_VAR') == os.environ['UNKNOWN_VAR']
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('UNKNOWN_VAR1', 'UNKNOWN_VAR2')



# Generated at 2022-06-12 23:35:11.391755
# Unit test for function env_fallback
def test_env_fallback():
    env_var = 'ANSIBLE_TEST_ENV_VAR'
    try:
        os.environ[env_var] = 'test'
        assert env_fallback(env_var) == 'test'
    finally:
        if env_var in os.environ:
            del os.environ[env_var]



# Generated at 2022-06-12 23:35:20.301173
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'one': {'required': True, 'type': 'str', 'fallback': (env_fallback, "TEST_ONE")},
        'two': {'required': True, 'type': 'str', 'fallback': (env_fallback, "TEST_TWO")},
        'three': {'required': True, 'type': 'str', 'fallback': (env_fallback, "TEST_THREE")}
    }
    parameters = dict(one='1', two='2')

    assert set_fallbacks(argument_spec, parameters) == set()
    assert parameters['three'] == '3'



# Generated at 2022-06-12 23:35:25.019569
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['asd'] = 'asd'
    assert env_fallback('asd', '123') == 'asd'
    del os.environ['asd']
    assert env_fallback('asd', '123') == '123'



# Generated at 2022-06-12 23:35:35.452720
# Unit test for function set_fallbacks
def test_set_fallbacks():
    module_argument_spec = dict(
        a=dict(fallback=(env_fallback, 'FOO')),
        b=dict(fallback=(env_fallback, 'FOO', 'GOO')),
        c=dict(fallback=(env_fallback, 'FOO', 'MOO')),
        d=dict(fallback=(env_fallback, 'FOO', dict(default='goo'))),
        x=dict(fallback=(env_fallback, 'FOO', dict(default='goo'))),
        y=dict(fallback=(env_fallback, 'FOO', dict(default=None))),
    )
    parameters = dict(
        a='bar',
        b='bar',
        c='bar',
        d='bar',
        x='bar',
        y='bar',
    )

# Generated at 2022-06-12 23:35:46.195883
# Unit test for function sanitize_keys
def test_sanitize_keys():
    no_log_strings = set(['a', 'b'])
    # First test that we don't attempt to modify immutable objects
    immutable_objects = (
        '',
        u'',
        b'',
        42,
        42.0,
        True,
        False,
        None,
        NotImplemented,
        Ellipsis,
    )

    for obj in immutable_objects:
        assert_equal(sanitize_keys(obj, no_log_strings), obj)

    # Next test that we don't touch keys that should remain unmodified
    ignored_keys = ('_ansible_no_log', '_ansible_ignore_errors', '_ansible_internal_api_version')

    test_dict = dict.fromkeys(ignored_keys, '')

# Generated at 2022-06-12 23:35:49.876447
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST_ENV_FALLBACK'] = 'TEST_ENV_FALLBACK_VALUE'
    assert env_fallback('TEST_ENV_FALLBACK') == os.environ['TEST_ENV_FALLBACK']
    os.environ.pop('TEST_ENV_FALLBACK')
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('TEST_ENV_FALLBACK')



# Generated at 2022-06-12 23:35:55.815457
# Unit test for function sanitize_keys
def test_sanitize_keys():

    assert sanitize_keys("foobar", ["foo"]) == "foobar"

    # string to list
    result = sanitize_keys("foobar", ["foo"])
    assert result == "foobar"

    # string to dict
    result = sanitize_keys("foobar", ["foo"])
    assert result == "foobar"

    # list to list
    result = sanitize_keys(["foobar"], ["foo"])
    assert result == ["foobar"]

    # list to dict
    result = sanitize_keys(["foobar"], ["foo"])
    assert result == ["foobar"]

    # dict to list
    result = sanitize_keys({'foo': 'bar'}, ["foo"])
    assert result == {'foo': 'bar'}

    # dict to dict
    result

# Generated at 2022-06-12 23:36:01.140789
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('TESTING') == 'TESTING'
    assert env_fallback('TESTING', 'TESTING2') == 'TESTING'
    assert env_fallback('TESTING_NOT', 'TESTING2') == 'TESTING2'
    assert env_fallback('TESTING_NOT') == 'TESTING_NOT'
    raise Exception('check failed')

# Generated at 2022-06-12 23:36:11.288821
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = {}
    argument_spec = dict(foo=dict(type='str', fallback=('env', 'foo')),
                         bar=dict(type='list', fallback=('env', 'bar')),
                         baz=dict(type='str', fallback=('env', 'baz')),
                         bat=dict(type='str', fallback=('env', 'bat', dict(fallback=True))),
                         )

    with patch.dict(os.environ, {'foo': 'bar', 'bar': 'foo,bar,baz', 'baz': '0'}):
        no_log_values = set_fallbacks(argument_spec, parameters)
        assert parameters['foo'] == 'bar'
        assert parameters['bar'] == ['foo', 'bar', 'baz']

# Generated at 2022-06-12 23:36:21.964166
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test scalar
    argument_spec = {
        "first": {"fallback": (env_fallback, ['FIRST'])},
        "second": {"fallback": (env_fallback, ['SECOND'])},
    }
    parameters = {}
    os.environ['FIRST'] = '1'
    os.environ['SECOND'] = '2'
    set_fallbacks(argument_spec, parameters)
    assert parameters['first'] == '1'
    assert parameters['second'] == '2'
    # Test dict

# Generated at 2022-06-12 23:36:48.897016
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_SOMETHING'] = 'foo'
    assert env_fallback('ANSIBLE_SOMETHING', 'ANSIBLE_NOTHING') == 'foo'
    del os.environ['ANSIBLE_SOMETHING']
    assert env_fallback('ANSIBLE_NOTHING') == ''



# Generated at 2022-06-12 23:36:53.944489
# Unit test for function sanitize_keys
def test_sanitize_keys():
    '''
    unit test for function sanitize_keys
    '''
    data_list = ['hi', {'hi': 'world'}, {'hello': ['world', {'world': 'hello'}]}]
    no_log_elements = ['hello']
    result = sanitize_keys(data_list, no_log_elements)
    assert result[0] == 'hi'
    assert result[1]['hi'] == 'world'
    assert 'hello' not in result[1]
    assert result[2]['world'] == 'hello'
    assert 'hello' not in result[2]
    assert result[2]['world'] == 'hello'



# Generated at 2022-06-12 23:36:57.439524
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'bar'
    assert env_fallback('FOO') == 'bar'

    assert env_fallback('BAR') == ''



# Generated at 2022-06-12 23:37:05.960315
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('PATH') != ''
    assert env_fallback('foo', 'PATH') == 'foo'
    if PY3:
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('bar')
    else:
        assert env_fallback('bar') == 'bar'
        assert env_fallback('bar', 'baz') == 'bar'
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('bar', 'baz', 'moo')



# Generated at 2022-06-12 23:37:17.805838
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        a=dict(type='bool'),
        b=dict(type='str', default='bar'),
        c=dict(type='str', fallback=((lambda **kwargs: 'foo'), 'bar')),
        d=dict(type='str', fallback=((lambda **kwargs: 'bar'), 'foo')),
        e=dict(type='str', fallback=((lambda **kwargs: 'foo'), 'bar', 'foo')),
        f=dict(type='str', fallback=((lambda **kwargs: 'foo'), 'bar', 'foo', 'bar')),
        g=dict(type='str', fallback=(env_fallback, 'NOT_THIS', 'NOT_THIS_EITHER')),
    )

    # Test all value types

# Generated at 2022-06-12 23:37:26.455873
# Unit test for function set_fallbacks
def test_set_fallbacks():

    # Check if fallback can be used in different argument spec.
    argument_spec = {'param_1': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_PARAM_1')},
                     'param_2': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_PARAM_2')},
                     'param_3': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_PARAM_3')}}
    parameters = {}

    # Check if fallback works with one non existent param
    os.environ['ANSIBLE_PARAM_1'] = 'value1'
    os.environ['ANSIBLE_PARAM_2'] = 'value2'
    expected = {'param_2': 'value2'}

# Generated at 2022-06-12 23:37:37.150404
# Unit test for function env_fallback
def test_env_fallback():
    # test empty args
    try:
        env_fallback()
        assert False
    except AnsibleFallbackNotFound:
        pass
    # test default with empty string fallback
    os.environ['ANSIBLE_TEST_VAR'] = 'test_value'
    assert env_fallback('ANSIBLE_TEST_VAR') == 'test_value'
    assert env_fallback('ANSIBLE_TEST_VAR', 'default_value') == 'test_value'
    del os.environ['ANSIBLE_TEST_VAR']
    # test default value
    assert env_fallback('ANSIBLE_TEST_VAR', 'default_value') == 'default_value'