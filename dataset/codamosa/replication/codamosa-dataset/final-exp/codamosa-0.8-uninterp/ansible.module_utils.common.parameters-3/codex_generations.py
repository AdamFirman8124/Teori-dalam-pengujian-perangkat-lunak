

# Generated at 2022-06-12 23:28:53.149798
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'a': {'type': 'str'},
                     'b': {'type': 'str', 'fallback': (env_fallback, 'B_PARAM')},
                     'c': {'type': 'str', 'fallback': (env_fallback, 'C_PARAM', 'D_PARAM')}}

    parameters = {'a': 'test'}

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert len(no_log_values) == 0
    assert len(parameters) == 2
    assert parameters['a'] == 'test'
    assert parameters['b'] is None

    os.environ['B_PARAM'] = 'b'
    os.environ['C_PARAM'] = 'c'
    os.environ['D_PARAM']

# Generated at 2022-06-12 23:29:04.198637
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:29:12.416494
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit test for function set_fallbacks"""
    args = dict(ignore_errors=True, no_log=True)
    # Define argument_spec

# Generated at 2022-06-12 23:29:21.104176
# Unit test for function sanitize_keys
def test_sanitize_keys():
    no_log_strings = {"test_no_log"}
    ignore_keys = frozenset({"test_ignore_keys", "test_ignore_keys_nested"})

# Generated at 2022-06-12 23:29:31.168897
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'param1': {'type': 'str', 'fallback': (env_fallback, 'AAA')},
        'param2': {'type': 'str'},
        'param3': {'type': 'str', 'fallback': (env_fallback, 'BBB')},
        'param4': {'type': 'dict', 'options': {
            'param1': {'type': 'str', 'fallback': (env_fallback, 'CCC')},
            'param2': {'type': 'str'},
            'param3': {'type': 'str', 'fallback': (env_fallback, 'DDD')},
        }},
    }

    parameters = {'param2': 'a', 'param4': {'param2': 'b'}}

    assert set_fall

# Generated at 2022-06-12 23:29:35.975113
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """Test sanitize_keys function"""
    # Unit test for function sanitize_keys
    obj = {'key': 'value', 'no_log': 'private'}
    no_log_strings = {'private', 'private_value'}
    test = sanitize_keys(obj, no_log_strings)
    assert test == {'key': 'value', 'no_log': 'private'}, "sanitize_keys failed"

    obj = {'no_log_key': 'value', 'no_log': 'private'}
    no_log_strings = {'private', 'private_value', 'no_log_key'}
    test = sanitize_keys(obj, no_log_strings)
    assert test == {'no_log': 'private'}, "sanitize_keys failed"

   

# Generated at 2022-06-12 23:29:45.922211
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Test fallback with `env_fallback`
    argument_spec = dict(a=dict(type='str', fallback=(env_fallback, 'TEST_VAR')),
                         b=dict(type='str', fallback=(env_fallback, 'TEST_VAR2')))
    parameters = dict(b='test')
    os.environ['TEST_VAR'] = 'test_env'
    os.environ['TEST_VAR2'] = 'test_env2'
    assert set_fallbacks(argument_spec, parameters) == set(['test_env', 'test_env2'])
    assert parameters == dict(a='test_env', b='test')

    # Test fallback with `env_fallback` and no environment variable
    parameters = dict()

# Generated at 2022-06-12 23:29:55.341415
# Unit test for function set_fallbacks
def test_set_fallbacks():
    args = dict(param1='test2', param2='test2', param3=dict(subparam='test3'), param5='test5', param6='test6')

# Generated at 2022-06-12 23:29:58.680562
# Unit test for function env_fallback
def test_env_fallback():
    with patch.dict('os.environ', {'ANSIBLE_NET_USERNAME': 'user', 'ANSIBLE_NET_PASSWORD': 'password'}):
        assert 'user' == env_fallback('ANSIBLE_NET_USERNAME')
        assert 'password' == env_fallback('ANSIBLE_NET_PASSWORD')
        assert 'user' == env_fallback('ANSIBLE_NET_USERNAME', 'ANSIBLE_NET_PASSWORD')
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('missing_var')
            env_fallback('missing_var', 'missing_var2')



# Generated at 2022-06-12 23:30:03.933941
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('UNIT_TEST_env_fallback') == env_fallback('UNIT_TEST_env_fallback')
    try:
        env_fallback('UNIT_TEST_env_fallback_NOT_FOUND')
    except AnsibleFallbackNotFound:
        pass


# Generated at 2022-06-12 23:30:30.408838
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({}, {}) == set()

    assert set_fallbacks({'param1': {'fallback': (env_fallback, 'PARAM1')}}, {}) == {'param1'}

    assert set_fallbacks({'param1': {'fallback': (env_fallback, 'PARAM1')}}, {'param1': 'value1'}) == set()



# Generated at 2022-06-12 23:30:41.578560
# Unit test for function set_fallbacks
def test_set_fallbacks():
    import mock

    with mock.patch('os.environ', {}):
        spec = dict(count=dict(type='int', fallback=(env_fallback, 'COUNT')),
                    name=dict(type='str', fallback=(env_fallback, 'NAME')))
        params = dict()
        set_fallbacks(spec, params)
        assert params == dict(count=None, name=None)

        params = dict(count=10)
        set_fallbacks(spec, params)
        assert params == dict(count=10, name=None)

        with mock.patch('os.environ', dict(COUNT='5')):
            params = dict()
            set_fallbacks(spec, params)
            assert params == dict(count=5, name=None)


# Generated at 2022-06-12 23:30:48.074795
# Unit test for function set_fallbacks
def test_set_fallbacks():
    args = dict(
        param1=dict(fallback=('env', 'TOKEN')),
        param2=dict(fallback=(env_fallback, 'ANSIBLE_FOO')),
        param3=dict(fallback=(env_fallback, 'ANSIBLE_BAR', dict(default='foo'))),
    )
    parameters = dict()
    set_fallbacks(args, parameters)
    assert parameters['param1'] == os.environ['TOKEN']
    assert parameters['param2'] == os.environ['ANSIBLE_FOO']
    assert parameters['param3'] == 'foo'



# Generated at 2022-06-12 23:30:53.494344
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'key': {'type': 'str',
                             'fallback': (env_fallback, 'KEY')},
                     'nested': {'type': 'dict', 'options':
                                {'nested_key': {'type': 'str',
                                                'fallback': (env_fallback, 'NESTED_KEY')}}}}
    os.environ['KEY'] = 'value'
    os.environ['NESTED_KEY'] = 'nested-value'
    if os.environ.get('ANSIBLE_NO_LOG', None):
        del os.environ['ANSIBLE_NO_LOG']
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0

# Generated at 2022-06-12 23:31:00.775269
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # parameters = {'x': 'value', 'y': 'value'}
    # argument_spec = {
    #     'x': {'type': 'str', 'fallback': ('env_fallback', 'ENV_VALUE')},
    #     'y': {'type': 'str', 'fallback': ('env_fallback', 'ENV_VALUE1', 'ENV_VALUE2')},
    #     'z': {'type': 'str', 'fallback': ('env_fallback', 'ENV_VALUE')},
    # }
    # no_log_values = set()
    # set_fallbacks(argument_spec, parameters)
    # assert parameters == {'x': 'value', 'y': 'value'}
    pass



# Generated at 2022-06-12 23:31:01.592830
# Unit test for function env_fallback
def test_env_fallback():
    assert {} == {}



# Generated at 2022-06-12 23:31:06.382437
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'bar'
    assert env_fallback('FOO') == 'bar'
    assert env_fallback('FOO', 'BAR') == 'bar'
    assert env_fallback('BAR', 'BAZ') == 'BAZ'



# Generated at 2022-06-12 23:31:13.357246
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({"as_port": {"fallback": (env_fallback, "AS_PORT")}}, {}) == {"as_port": "AS_PORT"}
    assert set_fallbacks({"as_port": {"fallback": (env_fallback, "AS_PORT")}}, {"as_port": "123"}) == set()
    assert set_fallbacks({"as_port": {"fallback": (env_fallback, "AS_PORT"), "no_log": True}},
                         {}) == {"as_port": "AS_PORT"}
    assert set_fallbacks({"as_port": {"fallback": (env_fallback, "AS_PORT"), "no_log": True}},
                         {"as_port": "123"})



# Generated at 2022-06-12 23:31:23.437056
# Unit test for function set_fallbacks
def test_set_fallbacks():
    mock_parameters = {'param1': 'yes_in_parameters'}
    mock_fallback = {'fallback': [env_fallback, {'param2': 'param2_key'}]}
    os.environ['param2'] = 'param2_value'
    assert set_fallbacks(argument_spec={'param1': mock_fallback, 'param2': mock_fallback}, parameters=mock_parameters) == set()
    assert mock_parameters['param1'] == 'yes_in_parameters'
    assert mock_parameters['param2'] == 'param2_value'

    mock_parameters = {}
    mock_fallback = {'fallback': [env_fallback, 'Param_A']}
    os.environ['param_a'] = 'Yes_in_env'


# Generated at 2022-06-12 23:31:34.076793
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from ansible.module_utils.common._collections_compat import MutableMapping
    arg_spec = {
        'a': {'type': 'str'},
        'b': {'type': 'str', 'fallback': (env_fallback, 'B')},
        'c': {'type': 'str', 'fallback': (env_fallback, 'C')},
        'd': {'type': 'str', 'fallback': (env_fallback, {'default': 'D'})},
    }

    parameters = {'a': 'A'}
    no_log_values = set_fallbacks(arg_spec, parameters)
    assert set(parameters.keys()) == {'a', 'b', 'c', 'd'}
    assert parameters['a'] == 'A'

# Generated at 2022-06-12 23:32:02.802121
# Unit test for function env_fallback
def test_env_fallback():
    test_cases = (
        ((), {}),
        (('test',), {'test': 'test'}),
        (('test',), {'test1': 'test'}),
        (('test',), {'test': 'test'}, 'test'),
        (('test',), {'test1': 'test'}, 'test'),
        (('test', 'test2'), {'test': 'test'}, 'test'),
        (('test', 'test2'), {'test1': 'test'}, 'test'),
        (('test', 'test2'), {'test': 'test'}, 'test2'),
        (('test', 'test2'), {'test1': 'test'}, 'test2'),
    )
    for test_case in test_cases:
        args, environ = test_case[:-1]


# Generated at 2022-06-12 23:32:13.735130
# Unit test for function sanitize_keys
def test_sanitize_keys():
    no_log_strings = ['password', 'secret', 'Authorization', 'PRIVATE', 'BASIC']

    old_data = {
        'foo': {
            'bar': 'p@55w0rd',
            'baz': 'secret',
            'deep': {
                'another': {
                    'yes': 'I am hidden'
                }
            }
        }
    }

    new_data = sanitize_keys(copy.deepcopy(old_data), no_log_strings)
    assert dict(new_data) == {
        'foo': {
            'bar': '*****',
            'baz': '*****',
            'deep': {
                'another': {
                    'yes': '*****'
                }
            }
        }
    }



# Generated at 2022-06-12 23:32:21.380373
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'name': {'fallback': (env_fallback, 'name')}}, {'name': 'test'}) == set()
    assert set_fallbacks({'name': {'fallback': (env_fallback, 'name')}}, {}) == set()
    os.environ['name'] = 'test'
    assert set_fallbacks({'name': {'fallback': (env_fallback, 'name')}}, {}) == set(['test'])



# Generated at 2022-06-12 23:32:32.895019
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:32:41.808606
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # test with no fallbacks
    argument_spec = {'param_a': {}}
    parameters = {}
    expected = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters == expected

    # test with one fallback
    argument_spec = {'param_a': {'type': 'str', 'fallback': ('env_fallback',)}}
    parameters = {'param_a': 'value1'}
    expected = parameters.copy()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters == expected

    # test with one fallback and no param

# Generated at 2022-06-12 23:32:52.661400
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = {'name': 'module_name'}
    spec = {'name': {'type': 'str'},
            'foo': {'type': 'str', 'fallback': (env_fallback, ['FOO_VAR'])}}

    os.environ['FOO_VAR'] = 'bar'
    no_log_values = set_fallbacks(spec, params)
    assert params['foo'] == 'bar'
    assert no_log_values == set()

    del os.environ['FOO_VAR']
    set_fallbacks(spec, params)
    assert params['foo'] == 'bar'

    spec['foo']['fallback'] = (env_fallback, [])
    no_log_values = set_fallbacks(spec, params)

# Generated at 2022-06-12 23:32:58.150696
# Unit test for function set_fallbacks
def test_set_fallbacks():
    no_log_values = set()
    argument_spec = {"key1": {'type': 'str', 'fallback': (env_fallback, 'abc')},
                     "key2": {'type': 'str', 'fallback': (env_fallback, 'abc', {'no_log': False})},
                     "key3": {'type': 'str', 'fallback': (env_fallback, 'abc', {'no_log': True})}}
    parameters = {}
    no_log_values = no_log_values.union(set_fallbacks(argument_spec, parameters))
    assert parameters == {"key1": os.environ['abc'], "key2": os.environ['abc'], "key3": os.environ['abc']}
    assert no_log_values == set()

    argument_spec

# Generated at 2022-06-12 23:33:01.590160
# Unit test for function env_fallback
def test_env_fallback():
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('FOOBAR')
    assert env_fallback('HOME') == os.environ['HOME']
    assert env_fallback('FOOBAR', 'HOME') == os.environ['HOME']



# Generated at 2022-06-12 23:33:06.895436
# Unit test for function env_fallback
def test_env_fallback():
    with patch.dict(os.environ, {'TEST': 'test'}):
        assert env_fallback('TEST') == 'test'
    with pytest.raises(AnsibleFallbackNotFound):
        assert env_fallback('NOTEST')


# Generated at 2022-06-12 23:33:14.679311
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'from_environment': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_FROM_ENVIRONMENT'])}}
    parameters = {}
    assert set_fallbacks(argument_spec, parameters) == set([])
    assert parameters == {}

    os.environ['ANSIBLE_FROM_ENVIRONMENT'] = 'bar'

    argument_spec = {'from_environment': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_FROM_ENVIRONMENT'])}}
    parameters = {}
    assert set_fallbacks(argument_spec, parameters) == set([])
    assert parameters == {'from_environment': 'bar'}


# Generated at 2022-06-12 23:33:44.017327
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set(set_fallbacks({'bar': {'fallback': (env_fallback, 'ANSIBLE_BAR')}}, {})) == set()
    assert set(set_fallbacks({'bar': {'fallback': (env_fallback, 'ANSIBLE_BAR')}}, {'bar': 'baz'})) == set()
    assert set(set_fallbacks({'bar': {'fallback': (env_fallback, 'ANSIBLE_BAR', 'ANSIBLE_UNDEFINED')}}, {})) == set()
    assert set(set_fallbacks({'bar': {'fallback': (env_fallback, 'ANSIBLE_BAR', 'ANSIBLE_UNDEFINED')}}, {'bar': 'baz'})) == set()


# Generated at 2022-06-12 23:33:47.103886
# Unit test for function remove_values
def test_remove_values():
    assert remove_values([1, 2], ['3']) == [1, 2]
    assert remove_values(3, ['3']) == 3
    assert remove_values(b'3', ['3']) == b'3'



# Generated at 2022-06-12 23:33:57.969240
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({}, {}) == set()
    assert set_fallbacks({'name': {'fallback': (None,)}}, {}) == set()
    assert set_fallbacks({'name': {'fallback': (None, 'name')}}, {}) == set()
    assert set_fallbacks({'name': {'fallback': (env_fallback,)}}, {}) == set()
    assert set_fallbacks({'name': {'fallback': (env_fallback, 'name')}}, {}) == set()
    assert set_fallbacks({'name': {'fallback': (env_fallback, 'name')}}, {'name': 'test'}) == set()

# Generated at 2022-06-12 23:34:07.671279
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:34:16.325524
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:34:27.216411
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:34:38.241755
# Unit test for function set_fallbacks
def test_set_fallbacks():
    no_log_values = set()
    parameters = {}
    argument_spec = {'param': {'type': 'str', 'fallback': (env_fallback, ['PARAM'])}}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters['param'] == 'PARAM'
    os.environ.pop('PARAM')

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters['param'] == 'PARAM'

    argument_spec = {'param': {'type': 'str', 'no_log': True, 'fallback': (env_fallback, ['PARAM'])}}

# Generated at 2022-06-12 23:34:48.425169
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({}, {}) == set()
    assert set_fallbacks({'host': {'type': 'str', 'fallback': (None,)}}, {}) == set()
    assert set_fallbacks({'host': {'type': 'str', 'fallback': (None, 'localhost')}}, {}) == set()
    assert set_fallbacks({'host': {'type': 'str', 'fallback': (None, 'localhost', '127.0.0.1')}}, {}) == set()
    assert set_fallbacks({'host': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_HOST')}}, {}) == set()

# Generated at 2022-06-12 23:34:56.953113
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # no-op if no fallback defined
    assert set_fallbacks({'a': {'type': 'int'}}, {'a': 1}) == set()
    # simple fallback
    assert set_fallbacks({'a': {'type': 'int', 'fallback': (lambda: 2,)}}, {}) == set()
    assert set_fallbacks({'a': {'type': 'int', 'fallback': (lambda: 2,)}}, {'a': 1}) == set()
    assert set_fallbacks({'a': {'type': 'int', 'fallback': (lambda: 2,)}}, {}) == {2}

    # complex fallback
    assert set_fallbacks({'a': {'type': 'int', 'fallback': (env_fallback, )}}, {}) == set()
    assert set_

# Generated at 2022-06-12 23:35:01.987272
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'max_retries': dict(type='int', fallback=(env_fallback, 'ANSIBLE_HTTP_MAX_RETRIES'))
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)

    assert parameters == {'max_retries': 10}
    assert no_log_values == set()



# Generated at 2022-06-12 23:35:34.358648
# Unit test for function env_fallback
def test_env_fallback():
    """Test env_fallback function with an empty environment"""
    fake_environ = {}
    with patch.dict(os.environ, fake_environ, clear=True):
        assert env_fallback('fake_var') is None
    with patch.dict(os.environ, fake_environ, clear=True):
        fake_environ['fake_var'] = 'value'
        assert env_fallback('fake_var') == 'value'

    with patch.dict(os.environ, fake_environ, clear=True):
        assert env_fallback('fake_var', 'fake_var2') is None
    with patch.dict(os.environ, fake_environ, clear=True):
        fake_environ['fake_var'] = 'value'

# Generated at 2022-06-12 23:35:45.894920
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks(dict(param='value', param2=dict(fallback=('environment', 'param1', 'param2'))), dict()) == {'value'}
    assert set_fallbacks(dict(param='value', param2=dict(fallback=('environment', {'param1': 'param2'}))), dict()) == {'value'}
    assert set_fallbacks(dict(param='value', param2=dict(fallback=('environment',))), dict()) == {'value'}
    assert set_fallbacks(dict(param='value', param2=dict(fallback=(None,))), dict()) == {'value'}
    assert set_fallbacks(dict(param='value', param2=dict(fallback=('environment', 'foo'))), dict()) == {'value'}


# Generated at 2022-06-12 23:35:52.883326
# Unit test for function remove_values

# Generated at 2022-06-12 23:36:02.918454
# Unit test for function env_fallback
def test_env_fallback():
    def override_environ(**kwargs):
        my_env = os.environ.copy()
        my_env.update(kwargs)
        return my_env

    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback("foo")

    os.environ.update({"foo": "bar"})
    assert env_fallback("foo") == "bar"
    assert env_fallback("foo", "baz") == "bar"
    assert env_fallback("baz", "foo") == "bar"

    with pytest.raises(AnsibleFallbackNotFound):
        with override_environ(foo="", BAR=None):
            assert env_fallback("foo", "BAR")

    with pytest.raises(AnsibleFallbackNotFound):
        env

# Generated at 2022-06-12 23:36:11.924496
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # test with fallbacks set
    argument_spec = dict(foo=dict(type='int', fallback=(env_fallback, 'FOO')),
                         bar=dict(type='bool', fallback=(env_fallback, 'BAR')),
                         baz=dict(type='str', fallback=(env_fallback, 'BAZ')),
                         qux=dict(type='dict', fallback=(env_fallback, 'QUX')),
                         )

    parameters = dict()

    os.environ['FOO'] = '2'
    os.environ['BAR'] = 'True'
    os.environ['BAZ'] = 'ansible'
    os.environ['QUX'] = 'ansible:2.0'
    no_log_values = set_fallbacks(argument_spec, parameters)
   

# Generated at 2022-06-12 23:36:22.657135
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        d_foo=dict(fallback=('bar',)),
        d_foo1=dict(fallback=('bar1',)),
        d_foo2=dict(fallback=('bar2', {'fallback_data': 'bar3'})),
        d_foo3=dict(fallback=('bar4', {'fallback_data': 'bar5'})),
        d_foo4=dict(fallback=('bar6', {'fallback_data': 'bar7'})),
        d_foo5=dict(fallback=('bar8', {'fallback_data': 'bar9'})),
    )
    parameters = dict(d_foo=None, d_foo1=None)
    os.environ['bar'] = 'bar1'
    result1 = set_fall

# Generated at 2022-06-12 23:36:28.017869
# Unit test for function env_fallback
def test_env_fallback():
    with patch.dict(os.environ, {'a': 'a', 'b': 'b'}, clear=True):
        assert 'a' == env_fallback('a')
    with patch.dict(os.environ, {'a': 'a', 'b': 'b'}, clear=True):
        assert 'b' == env_fallback('a', 'b')
    with patch.dict(os.environ, {'a': 'a', 'b': 'b'}, clear=True):
        assert 'c' == env_fallback('c')



# Generated at 2022-06-12 23:36:32.710353
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'name': {'type': 'str', 'required': True},
        'home': {'type': 'str', 'fallback': (env_fallback, 'HOME')},
        'shell': {'type': 'path', 'required': True}
    }
    parameters = {'name': 'foo'}
    set_fallbacks(spec, parameters)
    assert parameters['home'] == os.environ['HOME']



# Generated at 2022-06-12 23:36:37.818183
# Unit test for function env_fallback
def test_env_fallback():
    # Setup environment
    os.environ['ANSIBLE_TEST_KEY'] = 'key'
    os.environ['ANSIBLE_TEST_KEY2'] = 'key2'
    # Test successful case
    assert 'key' == env_fallback('ANSIBLE_TEST_KEY')
    # Test unsuccessful case
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_TEST_KEY3')
    # Remove environment variables
    del os.environ['ANSIBLE_TEST_KEY']
    del os.environ['ANSIBLE_TEST_KEY2']



# Generated at 2022-06-12 23:36:48.980998
# Unit test for function env_fallback

# Generated at 2022-06-12 23:37:22.883210
# Unit test for function set_fallbacks
def test_set_fallbacks():
    test_argument_spec = {'required1': {}}

    module = AnsibleModule(argument_spec=test_argument_spec, supports_check_mode=True)
    no_log_values = set_fallbacks(test_argument_spec, module.params)
    assert not no_log_values

    test_argument_spec = {'required1': {'required': True}}
    expected = "missing required arguments: ['required1']"

    try:
        set_fallbacks(test_argument_spec, module.params)
    except SystemExit as e:
        assert expected == to_native(e)

    test_argument_spec = {'required1': {'required': True, 'fallback': (env_fallback, ['REQUIRED'])}}
    os.environ['REQUIRED'] = 'this is required'


# Generated at 2022-06-12 23:37:31.401792
# Unit test for function env_fallback
def test_env_fallback():
    # Set environment variables and test that env_fallback function
    # can find and return the expected value
    os.environ["SOME_VAR"] = "some value"
    assert env_fallback("SOME_VAR") == "some value"
    # Test env_fallback exception is raised when there's no match
    with pytest.raises(AnsibleFallbackNotFound):
        os.environ.pop('SOME_VAR')
        env_fallback('SOME_VAR')


_FALLBACK_FUNCTIONS = {
    'env': env_fallback,
}

