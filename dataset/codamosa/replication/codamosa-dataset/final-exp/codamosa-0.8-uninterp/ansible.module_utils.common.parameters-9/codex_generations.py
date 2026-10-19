

# Generated at 2022-06-12 23:28:16.423818
# Unit test for function sanitize_keys
def test_sanitize_keys():
    pytest.importorskip('cryptography')
    no_log_strings = [to_native(s, errors='surrogate_or_strict') for s in ['redact', 'VALUES']]
    new_value = sanitize_keys({'redact': 'redact'}, no_log_strings)
    assert new_value == {'XXXXXX': 'redact'}
    new_value = sanitize_keys({'redact': 'redact', 'ignore': 'ignore'}, no_log_strings, ignore_keys=frozenset(['ignore']))
    assert new_value == {'XXXXXX': 'redact', 'ignore': 'ignore'}

# Generated at 2022-06-12 23:28:25.290131
# Unit test for function set_fallbacks
def test_set_fallbacks():

    parameters = {
        'nofallback_not_provided': 'nofallback_not_provided',
        'nofallback_provided': 'nofallback_provided',
        'env_provided': 'env_provided',
        'fallback_provided': 'fallback_provided',
        'env_fallback_provided': 'env_fallback_provided',
    }


# Generated at 2022-06-12 23:28:35.749487
# Unit test for function sanitize_keys

# Generated at 2022-06-12 23:28:41.452421
# Unit test for function env_fallback
def test_env_fallback():
    assert 'HOME' == env_fallback('HOME')
    assert 'HOME' == env_fallback('HOME', 'PWD')
    assert 'HOME' == env_fallback('PWD', 'HOME', 'PWD')
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('FOO', 'BAR')


# Generated at 2022-06-12 23:28:51.012950
# Unit test for function set_fallbacks
def test_set_fallbacks():
    _data = [
        ({'fallback': ('env_fallback', 'B')}, {}, {}, {'B'}),
        ({'fallback': ('env_fallback', 'B')}, {'A': True}, {}, {'B'}),
        ({'fallback': ('env_fallback', 'B')}, {'A': True}, {'B': True}, {'B'}),
        ({'fallback': ('dict', {'C': 'key_c'})}, {}, {'C': 'value_c'}, {'value_c'})
    ]
    for (argument_spec, parameters, kwargs, expected_set) in _data:
        result_set = set_fallbacks(argument_spec, parameters, **kwargs)
        assert expected_set == result_set



# Generated at 2022-06-12 23:29:02.594406
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test function 'set_fallbacks'"""

# Generated at 2022-06-12 23:29:09.761296
# Unit test for function env_fallback
def test_env_fallback():
    try:
        env_fallback('empty')
        assert False, 'AnsibleFallbackNotFound was not raised'
    except AnsibleFallbackNotFound:
        assert True

    os.environ['t'] = 't_value'
    assert env_fallback('t') == 't_value'
    os.environ.pop('t')

    os.environ['t'] = 't_value'
    os.environ['s'] = 's_value'
    assert env_fallback('s', 't') == 's_value'
    os.environ.pop('s')
    os.environ.pop('t')



# Generated at 2022-06-12 23:29:15.829287
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:29:28.263348
# Unit test for function set_fallbacks
def test_set_fallbacks():

    def fake_fallback(*args, **kwargs):
        raise AnsibleFallbackNotFound

    argument_spec = {
        'param_a': {'fallback': (env_fallback, 'HOST_A', 'HOST_B'), 'type': 'str'},
        'param_b': {'fallback': (fake_fallback, "hello"), 'type': 'str'}
    }
    parameters = {'param_a': 'test'}
    os.environ['HOST_A'] = 'host_a'
    os.environ['HOST_B'] = 'host_b'

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert parameters['param_a'] == 'test'
    assert parameters['param_b'] == 'host_b'
    assert no_

# Generated at 2022-06-12 23:29:39.648085
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:30:25.104097
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from collections import Mapping
    import types

    params = {}

# Generated at 2022-06-12 23:30:35.283981
# Unit test for function remove_values
def test_remove_values():
    # Comparing a dictionary of dictionaries is difficult because
    # the order is not consistent across invocations.  Using json
    # for the values should make this test more consistent.
    expected_no_log = [{'a': 'b'}]
    expected = [{'x': 'y'}, {'a': '*'}]

    no_log = remove_values(expected_no_log, ['*'])
    result = remove_values(expected, ['*'])

    assert json.dumps(no_log, sort_keys=True) == json.dumps(expected_no_log, sort_keys=True)
    assert json.dumps(result, sort_keys=True) == json.dumps(expected, sort_keys=True)
test_remove_values()



# Generated at 2022-06-12 23:30:45.470546
# Unit test for function remove_values
def test_remove_values():
    assert remove_values('foo', {'bar'}) == 'foo'
    assert remove_values('', {''}) == ''
    assert remove_values('foo', {''}) == 'foo'
    assert remove_values('foo', {'o'}) == 'fo'
    assert remove_values('foo', {'oo'}) == 'f'
    assert remove_values('foobar', {'o'}) == 'fbar'
    assert remove_values('foobarfoo', {'foo'}) == 'r'
    assert remove_values('foobarfoo', {'bar'}) == 'foofoo'
    assert remove_values('foobarfoo', {'bara'}) == 'foobarfoo'
    assert remove_values('foobarfoo', {'foo', 'bar'}) == ''

# Generated at 2022-06-12 23:30:55.774176
# Unit test for function set_fallbacks
def test_set_fallbacks():
    mod = AnsibleModule(
        argument_spec={
            'foo': {
                'fallback': (env_fallback, 'FOO')
            },
            'bar': {},
            'baz': {
                'no_log': True,
                'fallback': (env_fallback, 'BAZ')
            }
        },
        required_one_of=[['foo', 'bar']],
        supports_check_mode=False
    )
    assert mod.params['foo'] == os.environ['FOO']
    assert not mod.params.get('bar')
    assert mod.params['baz'] == os.environ['BAZ']



# Generated at 2022-06-12 23:31:03.116558
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """This test check the three type of fallbacks"""
    ArgumentSpec = namedtuple('ArgumentSpec', ['type', 'options', 'fallback', 'no_log'])

    TestCase = namedtuple('TestCase', ['fallback', 'arguments', 'expected'])

# Generated at 2022-06-12 23:31:12.374442
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params1 = {'a': 1, 'b': 'param'}

# Generated at 2022-06-12 23:31:22.967443
# Unit test for function env_fallback
def test_env_fallback():
    if os.environ.get('ANSIBLE_DEBUG_CONFIG'):
        from tests.unit.test_compat import _unset_all_vars
        _unset_all_vars()
        try:
            assert env_fallback('FOO') == 'bar'
            assert env_fallback('FAIL') == 'fail'
        finally:
            _unset_all_vars()
    # Noop
    args_list = dict(
        ANSIBLE_FOO_UNITTEST=None,
        ANSIBLE_FAIL_UNITTEST=None,
    )
    for arg, value in args_list.items():
        os.environ[arg] = value

# Generated at 2022-06-12 23:31:27.982120
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(foo=dict(fallback=(env_fallback, 'ANSIBLE_FOO')))
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    os.environ['ANSIBLE_FOO'] = 'bar'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 1 and list(no_log_values)[0] == 'bar'
    assert parameters['foo'] == 'bar'
    del os.environ['ANSIBLE_FOO']



# Generated at 2022-06-12 23:31:36.742854
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(type='raw', fallback=(env_fallback, 'TEST_FOO', 'TEST_ANOTHER_FOO')),
        bar=dict(type='raw', fallback=(env_fallback, 'TEST_BAR'), no_log=True),
        baz=dict(type='list', elements='raw', fallback=(env_fallback, 'TEST_BAZ', 'TEST_ANOTHER_BAZ', 'TEST_BAZ_NONE')),
        fooz=dict(type='raw', fallback=(env_fallback, 'TEST_FOOZ')),
    )


# Generated at 2022-06-12 23:31:47.117986
# Unit test for function set_fallbacks
def test_set_fallbacks():
    set_fallbacks(
        {'a': {'type': 'dict',
               'options': dict(
                   b={'type': 'int'},
                   c={'type': 'int', 'required': True}),
               'fallback': ('env_fallback', ('A_OPENSTACK', 'A', 'A_STRATEGY'))}},
        dict(a=dict(b=2, c=3))) == set()


# Generated at 2022-06-12 23:32:17.320876
# Unit test for function sanitize_keys

# Generated at 2022-06-12 23:32:26.917476
# Unit test for function remove_values
def test_remove_values():
    for r in [remove_values([{'foo': 'bar', 'bam': ['baz', 'bam']}], ['bam'])]:
        assert r == [{'foo': 'bar', 'bam': ['baz', 'PRIVATE DATA HIDDEN']}]
    for r in [remove_values({'foo': 'bar', 'bam': ['baz', 'bam']}, ['bam'])]:
        assert r == {'foo': 'bar', 'bam': ['baz', 'PRIVATE DATA HIDDEN']}
    for r in [remove_values('foo: bar', ['foo', 'bar'])]:
        assert r == 'foo: bar'
    for r in [remove_values(['foo:bar'], ['foo', 'bar'])]:
        assert r == ['foo:bar']

# Generated at 2022-06-12 23:32:38.856508
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:32:49.324693
# Unit test for function remove_values
def test_remove_values():
    assert remove_values('test', ['t']) == 'es'
    assert remove_values(True, ['t']) == True
    assert remove_values(False, ['t']) == False
    assert remove_values(['test', 't', 'test2'], ['t']) == ['es', 'es2']
    assert remove_values(('test', 't', 'test2'), ['t']) == ('es', 'es2')
    assert remove_values(dict(a='test', b='t', c='test2'), ['t']) == dict(a='es', c='es2')
    assert remove_values(b'some bytes', ['bytes']) == b'some '



# Generated at 2022-06-12 23:32:59.724637
# Unit test for function remove_values
def test_remove_values():
    no_log_strings = ['password', 'secret']

    # Test simple string
    result = remove_values('abcdefg', no_log_strings)
    assert result == 'abcdefg'

    # Test string containing no_log_strings
    result = remove_values('foopassword', no_log_strings)
    assert result == 'foo<value_was_redacted>'

    # Test list containing no_log_strings
    result = remove_values(['password', 'foo'], no_log_strings)
    assert result == ['<value_was_redacted>', 'foo']

    # Test nested list containing no_log_strings
    result = remove_values(['foo', ['password', 'bar']], no_log_strings)

# Generated at 2022-06-12 23:33:04.882149
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'bar'
    result = env_fallback('FOO')
    assert result == "bar"
    try:
        env_fallback('BAR')
    except AnsibleFallbackNotFound as e:
        assert e.name == "BAR"


# Generated at 2022-06-12 23:33:13.467489
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:33:24.490607
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert 'ANSIBLE_TEST' not in os.environ

    argument_spec = {
        'arg1': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST')},
        'arg2': {'type': 'str', 'fallback': (env_fallback, ('ANSIBLE_TEST',))},
        'arg3': {'type': 'str', 'fallback': (env_fallback, ('ANSIBLE_TEST', 'foo', 'bar'))},
    }
    parameters = {}

    assert not set_fallbacks(argument_spec, parameters)
    assert 'arg1' not in parameters
    assert 'arg2' not in parameters

    os.environ['ANSIBLE_TEST'] = 'foo'

# Generated at 2022-06-12 23:33:32.953521
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'foo': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST_FOO')},
        'bar': {'type': 'str', 'fallback': (env_fallback, ('ANSIBLE_TEST_BAR', 'ANSIBLE_TEST_OTHER'))},
        'baz': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST_BAZ', {'fallback_variable': 'ANSIBLE_TEST_OTHER'})},
    }
    parameters = {}
    os.environ['ANSIBLE_TEST_FOO'] = 'foo'
    os.environ['ANSIBLE_TEST_BAR'] = 'bar'

# Generated at 2022-06-12 23:33:43.812357
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        param1=dict(
            type='int',
            fallback=(env_fallback, 'TEST_VAR1')
        ),
        param2=dict(
            type='str',
        ),
    )
    parameters = dict(
        param2='test2',
    )
    os.environ['TEST_VAR1'] = '23'
    no_log_values = set_fallbacks(argument_spec, parameters)
    os.environ.pop('TEST_VAR1')
    assert parameters['param1'] == 23
    assert parameters['param2'] == 'test2'
    assert len(no_log_values) == 1



# Generated at 2022-06-12 23:34:17.287480
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:34:20.678440
# Unit test for function env_fallback
def test_env_fallback():
    """test function env_fallback"""
    os.environ['ANSIBLE_TEST_DICT_KEY'] = 'ANSIBLE_TEST_DICT_VALUE'
    assert env_fallback('ANSIBLE_TEST_DICT_KEY') == 'ANSIBLE_TEST_DICT_VALUE'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('TEST_DICT_KEY')



# Generated at 2022-06-12 23:34:23.713846
# Unit test for function env_fallback
def test_env_fallback():

    os.environ['TEST_VARIABLE'] = 'test_value'
    assert env_fallback('TEST_VARIABLE') == 'test_value'
    assert env_fallback('TEST_VARIABLE_2') == None
    assert raise_parameter_error_or_fallback_not_found(test_func, "TEST_VARIABLE_2", env_fallback)



# Generated at 2022-06-12 23:34:30.612201
# Unit test for function set_fallbacks
def test_set_fallbacks():

    # create spec with fallback
    mock_argument_spec = dict(
        param1=dict(
            type='str',
            fallback=(env_fallback, ['ANSIBLE_TEST_PARAM_1'])
        )
    )
    # set environment variable
    os.environ['ANSIBLE_TEST_PARAM_1'] = 'foo'
    mock_parameters = dict()
    # run function
    no_log_values = set_fallbacks(mock_argument_spec, mock_parameters)
    assert mock_parameters['param1'] == 'foo'
    assert len(no_log_values) == 1



# Generated at 2022-06-12 23:34:38.941433
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Get the module argument spec
    spec = dict(
        user=dict(fallback=(env_fallback, 'ANSIBLE_NET_USERNAME', 'LOGNAME', {}), type='str'),
        password=dict(fallback=(env_fallback, 'ANSIBLE_NET_PASSWORD', {}), no_log=True),
    )
    arguments = dict(host='host', user='username')
    no_log_values = set_fallbacks(spec, arguments)
    assert sorted(no_log_values) == sorted(['username'])
    #assert arguments['user'] == 'username'
    #assert arguments['password'] == 'password'



# Generated at 2022-06-12 23:34:43.907803
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'a': {'type': 'str', 'fallback': ('env', 'A')}}, {}) == set()
    assert set_fallbacks({'a': {'type': 'str', 'fallback': ('env', 'A')}}, {'b': 1}) == set()
    with mock.patch.dict(os.environ, {'A': '1'}):
        assert set_fallbacks({'a': {'type': 'str', 'fallback': ('env', 'A')}}, {}) == set(['1'])
    with mock.patch.dict(os.environ, {'A': '1'}):
        assert set_fallbacks({'a': {'type': 'str', 'fallback': ('env', 'A')}}, {'a': '2'}) == set()

# Generated at 2022-06-12 23:34:53.954894
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test the following fallback scenarios:
    # 1. fallback not defined
    # 2. fallback is defined with no args, no kwargs
    # 3. fallback is defined with args, no kwargs
    # 4. fallback is defined with no args, kwargs
    # 5. fallback is defined with args, kwargs
    # 6. fallback is defined with no_log set to True
    # 7. a fallback function that does not raise AnsibleFallbackNotFound
    def fallback():
        return 'fallback was called'

    def fallback_with_args(*args, **kwargs):
        return 'args: %s and kwargs: %s' % (args, kwargs)

    def fallback_with_kwargs(**kwargs):
        return 'kwargs: %s' % k

# Generated at 2022-06-12 23:34:58.788193
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        x=dict(default=dict(a=1)),
        y=dict(fallback=(env_fallback, 'x')),
        z=dict(fallback=(env_fallback, 'y')),
    )
    parameters = dict(z=2)
    set_fallbacks(argument_spec, parameters)
    assert parameters == dict(z=2)



# Generated at 2022-06-12 23:35:07.135545
# Unit test for function sanitize_keys
def test_sanitize_keys():
    old_data = dict(a=1, b=2, _ansible_lo_sha256=3)
    new_data = sanitize_keys(old_data, no_log_strings=['a', 'b'], ignore_keys=['_ansible_lo_sha256'])
    assert new_data == old_data

    old_data = dict(a=1, b=2, _ansible_lo_sha256=3)
    new_data = sanitize_keys(old_data, no_log_strings=['a', 'b'])
    assert new_data == {'_ansible_lo_sha256': 3}

    old_data = dict(a=1, b=2, _ansible_lo_sha256=3)

# Generated at 2022-06-12 23:35:13.233336
# Unit test for function set_fallbacks
def test_set_fallbacks():
    fallbacks = dict(
        fallback_spec=dict(
            a=1,
            b=dict(type='str', fallback=(env_fallback, ['ENV_NAME'])),
            c=dict(type='str', fallback=(env_fallback, ['ENV_NAME'], dict(fallback_name='c'))),
            d=dict(type='str', fallback=(env_fallback, dict(fallback_name='d'))),
            f=dict(type='str', fallback=(env_fallback, ['ENV_NAME'], dict(fallback_name='f')), no_log=True),
        ),
        fallback_params=dict(
            a=2,
        )
    )
    os.environ['ENV_NAME'] = 'ENV_VALUE'
    no

# Generated at 2022-06-12 23:35:45.195126
# Unit test for function env_fallback
def test_env_fallback():
    os.environ["CONFIG_FILE"] = "/mnt/config_file"
    returned_value = env_fallback("CONFIG_FILE")
    assert returned_value == "/mnt/config_file"


# Generated at 2022-06-12 23:35:50.017532
# Unit test for function env_fallback
def test_env_fallback():
    if os.environ.get('MY_TEST_ENV_VAR'):
        del os.environ['MY_TEST_ENV_VAR']
    assert env_fallback('MY_TEST_ENV_VAR') == AnsibleFallbackNotFound
    os.environ['MY_TEST_ENV_VAR'] = 'from_env'
    assert env_fallback('MY_TEST_ENV_VAR') == 'from_env'



# Generated at 2022-06-12 23:35:58.887125
# Unit test for function env_fallback
def test_env_fallback():
    """
    Load value from environment variable
    """
    os.environ['my_env'] = 'my_value'
    os.environ['my_env2'] = 'my_value2'
    assert env_fallback('my_env', 'my_env2', 'my_env3') == 'my_value'
    assert env_fallback('my_env3', 'my_env2') == 'my_value2'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('my_env3')



# Generated at 2022-06-12 23:36:05.921327
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:36:13.704037
# Unit test for function set_fallbacks
def test_set_fallbacks():
    example = dict(fallback=(env_fallback, 'ANSIBLE_TEST'), type='str')
    assert set_fallbacks(dict(test=example), {}) == set()
    assert 'test' in os.environ
    assert set_fallbacks(dict(test=example), {}) == {os.environ['test']}
    # Fallback values should be treated as no_log
    no_log_example = dict(fallback=(env_fallback, 'ANSIBLE_TEST'), type='str', no_log=True)
    assert set_fallbacks(dict(test=no_log_example), {}) == {os.environ['test']}


# Generated at 2022-06-12 23:36:18.518912
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'one': {'default': 0}, 'two': {'default': 42}}, {}) == set()
    assert set_fallbacks({'one': {'default': 0}, 'two': {'default': 42}}, {'one': 1}) == set()
    assert set_fallbacks({'one': {'default': 0}, 'two': {'default': 42, 'no_log': True}}, {}) == set([42])



# Generated at 2022-06-12 23:36:23.067226
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_ENV'] = 'foo'
    assert env_fallback('ANSIBLE_TEST_ENV', 'ANSIBLE_TEST_ENV_FAIL') == 'foo'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_TEST_ENV_FAIL')


# Generated at 2022-06-12 23:36:24.486475
# Unit test for function sanitize_keys
def test_sanitize_keys():
    strings = set(['hello', 'from', 'the', 'other', 'side'])
    new_value = sanitize_keys(obj, strings)
    assert new_value == 'another_object'

# Generated at 2022-06-12 23:36:30.612838
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['foo'] = 'bar'
    assert env_fallback('foo') == 'bar'
    assert env_fallback('bar') == 'bar'
    assert env_fallback('foo', 'bar') == 'bar'
    assert env_fallback('bar', 'foo') == 'bar'
    assert env_fallback('bar', 'foo', 'bar') == 'bar'
    assert env_fallback('bar', 'foo', 'boo') == 'boo'
    os.environ.pop('foo')



# Generated at 2022-06-12 23:36:36.111308
# Unit test for function env_fallback
def test_env_fallback():
    with patch('ansible.module_utils.six.moves.builtins.__import__') as mock_import:
        mock_import.side_effect = ImportError
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('FOO')

    with patch('ansible.module_utils.six.moves.builtins.__import__') as mock_import:
        mock_import.side_effect = None
        os.environ['FOO'] = 'bar'
        assert env_fallback('FOO') == 'bar'

# Generated at 2022-06-12 23:37:05.604001
# Unit test for function set_fallbacks
def test_set_fallbacks():
    env_fallbacks = {'lookup': 'ENV', 'key': 'TEST_ENV_VAR'}
    argument_spec = {'foo': {'type': 'str', 'fallback': (env_fallback, env_fallbacks)}}
    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters['foo'] == os.environ['TEST_ENV_VAR']



# Generated at 2022-06-12 23:37:10.607253
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'BAR'
    result = env_fallback('FOO')
    assert result == 'BAR'
    result = env_fallback('FOO', 'BAR')
    assert result == 'BAR'
    result = env_fallback('FOOBAR')
    assert result is False


# Generated at 2022-06-12 23:37:16.680534
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_VAR'] = 'test'
    assert env_fallback('ANSIBLE_TEST_VAR') == 'test'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_TEST_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-12 23:37:25.547937
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit test for function set_fallbacks"""

    # test dict fallback
    argument_spec = dict(foo=dict(type='str', fallback=('bar',))
                         )
    parameters = dict()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters == dict(foo="bar")

    # test env fallback
    argument_spec = dict(foo=dict(type='str', fallback=(env_fallback, 'FOO',))
                         )
    parameters = dict()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters == dict(foo="bar")

    # test env fallback followed by dict fallback

# Generated at 2022-06-12 23:37:28.840501
# Unit test for function env_fallback
def test_env_fallback():  # type: () -> None
    os.environ['test_fallback'] = 'true'
    assert env_fallback('test_fallback', 'test_fallback_2') == 'true'


# Generated at 2022-06-12 23:37:39.451241
# Unit test for function env_fallback
def test_env_fallback():
    from ansible.utils.environment import Environment
    env = Environment(options={u'no_log': False})
    os.environ['ANSIBLE_FOO'] = 'foo'
    os.environ['ANSIBLE_BAR'] = 'bar'
    assert env_fallback('ANSIBLE_FOO', 'ANSIBLE_BAR') == 'foo'
    del os.environ['ANSIBLE_FOO']
    assert env_fallback('ANSIBLE_FOO', 'ANSIBLE_BAR') == 'bar'
    del os.environ['ANSIBLE_BAR']
    assert env_fallback('ANSIBLE_FOO') == 'ANSIBLE_FOO'
    assert env_fallback('ANSIBLE_FOO', default='foo') == 'foo'
