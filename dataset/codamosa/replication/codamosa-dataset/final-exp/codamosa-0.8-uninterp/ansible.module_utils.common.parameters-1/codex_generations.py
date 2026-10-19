

# Generated at 2022-06-12 23:28:41.761040
# Unit test for function set_fallbacks
def test_set_fallbacks():
    def env_fallback(val):
        return 'default_value'
    argument_spec = dict(
        parameter1=dict(type='int', fallback=(env_fallback, 'ENV_PARAM1'))
    )
    parameters = dict()
    fallback_values = set_fallbacks(argument_spec, parameters)
    assert fallback_values == set(), "Expected 'fallback_values' to be empty, got %s" % fallback_values
    assert parameters['parameter1'] == 'default_value', "Expected 'default_value', got %s" % parameters['parameter1']
    parameters = dict(parameter1=123)
    fallback_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:28:51.234496
# Unit test for function sanitize_keys
def test_sanitize_keys():
    from ansible.module_utils.six import PY3, text_type
    from ansible.module_utils._text import to_bytes
    no_log_strings = [u'foo', to_bytes('bar', encoding='utf-8')]

    test_obj = {u'foo': 1, u'bar': {u'bar': 1}, u'foobar': [{u'foo': 1}, {u'bar': 2}]}
    new_obj = sanitize_keys(test_obj, no_log_strings)
    # In Python 3 keys are always of type str. In Python 2 they are of type unicode
    # if they were created from unicode data.
    key_type = text_type if PY3 else basestring
    assert isinstance(new_obj, dict)

# Generated at 2022-06-12 23:29:00.620722
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO_JUNK'] = '100'
    assert env_fallback('FOO_JUNK') == 100, "env_fallback failed to load a value from environment variable"
    os.environ['FOO_JUNK'] = 'False'
    assert env_fallback('FOO_JUNK') is False, "env_fallback failed to load a value from environment variable"
    os.environ['FOO_JUNK'] = 'True'
    assert env_fallback('FOO_JUNK') is True, "env_fallback failed to load a value from environment variable"



# Generated at 2022-06-12 23:29:09.952126
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        required_when=dict(
            type="dict",
            apply_defaults=True,
            options=dict(
                option1=dict(
                    type='list',
                ),
                option2=dict(
                    type='list',
                )
            ),
            mutually_exclusive=[
                ['option1', 'option2'],
            ]
        )
    )

    args = dict()
    args = set_fallbacks(spec, args)
    assert args == dict()

    args = dict(
        required_when=dict()
    )
    args = set_fallbacks(spec, args)
    assert args == dict(
        required_when=dict()
    )


# Generated at 2022-06-12 23:29:20.524033
# Unit test for function remove_values
def test_remove_values():
    """Unit test for function remove_values"""
    from ansible.module_utils.common.collections import is_sequence

    # sequence
    removed = remove_values(['a', 'b', 'c'], ['b'])
    assert is_sequence(removed)
    assert removed == ['a', 'REDACTED', 'c']

    # persistent Mapping
    removed = remove_values(dict(a='a', b='b', c='c'), ['b'])
    assert isinstance(removed, dict)
    assert removed == dict(a='a', b='REDACTED', c='c')

    # non-persistent Mapping
    removed = remove_values(ImmutableDict(a='a', b='b', c='c'), ['b'])
    assert isinstance(removed, ImmutableDict)
    assert removed == Immutable

# Generated at 2022-06-12 23:29:30.513971
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = {'foo': 'bar'}
    argument_spec = dict(
        foo=dict(type='str', fallback=(env_fallback, 'foo')),
        baz=dict(type='str', no_log=True, fallback=(env_fallback, 'baz', dict(key='value')), default='default')
    )

    assert set_fallbacks(argument_spec, parameters) == {'default'}
    assert parameters['baz'] == 'default'

    for i in ('foo', 'baz'):
        os.environ[i] = i

    assert set_fallbacks(argument_spec, parameters) == {'default'}
    assert parameters['foo'] == 'foo'
    assert parameters['baz'] == 'baz'



# Generated at 2022-06-12 23:29:41.955988
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(fallback_choice=dict(type='str', fallback=(env_fallback, 'ANSIBLE_FALLBACK_CHOICE', 'FALLBACK_CHOICE')))
    parameters = dict()
    os.environ['ANSIBLE_FALLBACK_CHOICE'] = 'env_fallback'
    with patch.dict(os.environ, ANSIBLE_FALLBACK_CHOICE='env_fallback'):
        no_log_values = set_fallbacks(argument_spec, parameters)
        assert len(no_log_values) == 0
        assert parameters['fallback_choice'] == 'env_fallback'

    # Now, let's test the last 2 fallbacks are not set and the first one is set

# Generated at 2022-06-12 23:29:50.069172
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'test': {
            'required': True,
            'type': 'raw',
            'fallback': (env_fallback, 'TEST_ENV')
        }
    }

    parameters = {}

    os.environ['TEST_ENV'] = 'TEST_OK'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'test': 'TEST_OK'}
    assert no_log_values == set()

    del os.environ['TEST_ENV']
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'test': 'TEST_OK'}
    assert no_log_values == set()

    parameters = {'test': 'TEST_PARAM'}

# Generated at 2022-06-12 23:29:52.674889
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'BAR'
    assert env_fallback('FOO') == 'BAR'



# Generated at 2022-06-12 23:29:59.947402
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit test for function set_fallbacks"""

# Generated at 2022-06-12 23:30:25.436542
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('FOO', 'BAR') == 'BAR'
    # Test will fail if env variable does not exist
    assert env_fallback('FOO', 'DEFAULT') == 'DEFAULT'
    try:
        env_fallback('FOO')
    except AnsibleFallbackNotFound as e:
        assert str(e) == ''


# Generated at 2022-06-12 23:30:33.022828
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:30:43.718493
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'name': {'required': True, 'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_NET_USERNAME'])},
        'password': {'no_log': True, 'required': True, 'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_NET_PASSWORD'])}
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert set(no_log_values) == set()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert set(no_log_values) == set()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert set(no_log_values) == set()
   

# Generated at 2022-06-12 23:30:50.995393
# Unit test for function sanitize_keys
def test_sanitize_keys():
    obj = {'a': 1, 'b': 2, 'c': 3}
    assert sanitize_keys(obj, ['b'], set()) == {'a': 1, 'c': 3}

    obj = {'a': 1, 'b': 2, 'c': 3}
    assert sanitize_keys(obj, ['b'], set(['a'])) == {'a': 1, 'b': 2, 'c': 3}

    obj = {'a': 1, 'b': 2, 'c': 3}
    assert sanitize_keys(obj, ['b'], set(['a', 'b'])) == {'a': 1, 'b': 2, 'c': 3}

    obj = {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-12 23:30:56.101966
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert 'key_1' == sanitize_keys('key_1', ['key', '_1'])
    assert 'key_2' == sanitize_keys('key_2', ['key', '1'])
    assert 'key_3' == sanitize_keys('key_3', ['key_'])
    assert 'key_4' == sanitize_keys('key_4', ['_4'])
    assert 'key_5' == sanitize_keys('key_5', ['key_5'])
    assert 'key_6' == sanitize_keys('key_6', [])
    assert 'key' == sanitize_keys('key', ['key'])
    assert 'key_3' == sanitize_keys('key_3', ['key_3'])
    assert '_3' == san

# Generated at 2022-06-12 23:31:03.388533
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_KEY1'] = 'ANSIBLE_TEST_VALUE1'
    os.environ['ANSIBLE_TEST_KEY2'] = 'ANSIBLE_TEST_VALUE2'
    os.environ['ANSIBLE_TEST_KEY3'] = 'ANSIBLE_TEST_VALUE3'
    # Test if the function find the right value for the key
    assert env_fallback('ANSIBLE_TEST_KEY2') == 'ANSIBLE_TEST_VALUE2'
    # Test if the function returns the right value when there are multiple keys
    assert env_fallback('ANSIBLE_TEST_KEY2', 'ANSIBLE_TEST_KEY1') == 'ANSIBLE_TEST_VALUE2'

# Generated at 2022-06-12 23:31:04.321294
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('foo') is AnsibleFallbackNotFound



# Generated at 2022-06-12 23:31:07.902481
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'a':{'type':'str', 'fallback':(env_fallback, 'a')}, 'b':{'type':'str', 'fallback':(env_fallback, 'b')}}
    parameters = {}
    no_log_values = set()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['a'] == 'a'
    assert parameters['b'] == 'b'


# Generated at 2022-06-12 23:31:18.171198
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(a=dict(type='str', fallback=(env_fallback, 'FOO')),
                b=dict(type='int', fallback=(env_fallback, 'BAR')),
                c=dict(type='bool', fallback=(lambda: True), no_log=True),
                d=dict(type='str', fallback=(env_fallback, 'BAZ')),
                e=dict(type='str', fallback=(env_fallback, 'BAZ', dict(key='value'))),
                f=dict(type='list', fallback=(lambda: ['a'])),
                g=dict(type='dict', fallback=(lambda: dict(a=1))),
                h=dict(type='list', fallback=(lambda: ['a', dict(key='value')])))

# Generated at 2022-06-12 23:31:26.869877
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'test_param': {'type': 'str', 'fallback': (env_fallback, ['TEST_VAR'])},
        'test_array': {'type': 'list', 'fallback': (env_fallback, ['TEST_VAR', 'TEST_VAR2'])},
        'test_default': {'type': 'int', 'fallback': (lambda x, y: 42, [], {'x': 1, 'y': 2})},
    }
    parameters = {
        'test_param': 'foobar',
        'test_array': [1, 2, 3],
    }
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()


# Generated at 2022-06-12 23:31:54.968698
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST'] = 'foo'
    assert(env_fallback('TEST') == 'foo')
    assert(env_fallback('TEST1') == 'foo')
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('TEST2')
    assert(env_fallback('TEST2', 'TEST3') == 'foo')
    del os.environ['TEST']



# Generated at 2022-06-12 23:32:03.430048
# Unit test for function sanitize_keys
def test_sanitize_keys():
    data = {'password': 'my_secret', 'my_dict': {'password': 'my_secret2', 'my_list': ['password', 'my_secret3']}, 'my_list': ['password', 'my_secret4'], 'another_list': [{'password': 'my_secret5'}]}
    data_copy = deepcopy(data)
    no_log_values = set()
    new_data = sanitize_keys(data, no_log_values)
    assert new_data == data_copy

    no_log_values.add('my_secret1')
    no_log_values.add('my_secret2')
    new_data = sanitize_keys(data, no_log_values)

# Generated at 2022-06-12 23:32:14.232665
# Unit test for function set_fallbacks
def test_set_fallbacks():

    # Empty dict
    arguments = dict()
    parameters = dict()
    no_log_values = set_fallbacks(arguments, parameters)
    assert len(no_log_values) == 0
    assert len(parameters) == 0

    # Dict with values and no fallback
    arguments = dict()
    arguments['name'] = dict(
            default='test',
            fallback=(env_fallback, 'ENV_TEST'),
            no_log=True
    )
    parameters = dict()
    no_log_values = set_fallbacks(arguments, parameters)
    assert len(no_log_values) == 0
    assert parameters['name'] == 'test'

    # Dict with no fallback but no default
    arguments = dict()

# Generated at 2022-06-12 23:32:24.991320
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'a': {'type': 'str', 'fallback': (env_fallback, [u'ANSIBLE_TARGET'])},
                     'b': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_TARGET2'])},
                     'c': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_TARGET3'])},
                     'd': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_TARGET4'])}}
    parameters = {'a': 'a'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters == {'a': 'a'}

# Generated at 2022-06-12 23:32:37.554051
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:32:49.000668
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'param_one':'param_one_value'}, {}) == set()
    assert set_fallbacks({'param_one':{'type':'str'}}, {}) == set()
    assert set_fallbacks({'param_one':{}}, {}) == set()
    assert set_fallbacks({'param_one':{}},{'param_one':'param_one_value'}) == set()
    assert set_fallbacks({'param_one':{'type':'str','no_log':True}}, {'param_one':'param_one_value'}) == set(['param_one_value'])
    assert set_fallbacks({'param_one':{'type':'str','no_log':False}}, {'param_one':'param_one_value'})

# Generated at 2022-06-12 23:32:55.551290
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys("no_log", "no_log") == "no_log"
    assert sanitize_keys([{'a': 'no_log'}], "no_log") == [{'a': 'no_log'}]
    assert sanitize_keys({'a': 'no_log'}, "no_log") == {'a': 'no_log'}
    assert sanitize_keys({'no log': 'no_log', 'no-log': 'no_log'}, "no_log") == {'no log': 'no_log', 'no-log': 'no_log'}
    assert sanitize_keys({'nolog': 'no_log'}, "no_log") == {'nolog': 'no_log'}

# Generated at 2022-06-12 23:33:03.654216
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:33:11.246851
# Unit test for function env_fallback
def test_env_fallback():
    os.environ.update({'ANSIBLE_FOO_BAR': 'foo'})
    assert env_fallback('ANSIBLE_FOO_BAR') == 'foo'
    assert env_fallback('ANSIBLE_FOO_BAR','FOO_BAR','FOO','BAR') == 'foo'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('FOO_BAR','FOO','BAR')
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('FOO','BAR')
    os.environ.clear()



# Generated at 2022-06-12 23:33:21.893028
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(required=True, fallback=(env_fallback, ['FOO']))
    )
    parameters = dict()

    # Add valid environment variable
    os.environ['FOO'] = 'bar'

    # Fallback should be successful
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters['foo'] == 'bar'

    # Cleanup
    del os.environ['FOO']
    parameters.pop('foo', None)

    # If the environment variable is not set, the fallback should fail and
    # the param will not be set
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()

# Generated at 2022-06-12 23:34:21.923893
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('ANSIBLE_INTERNAL_DATA') == os.environ['ANSIBLE_INTERNAL_DATA']
    assert env_fallback('ANSIBLE_INTERNAL_DATA_MISSING') == os.environ.get('ANSIBLE_INTERNAL_DATA_MISSING', '')
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_INTERNAL_DATA_MISSING')
    assert env_fallback('ANSIBLE_INTERNAL_DATA', 'ANSIBLE_INTERNAL_DATA_MISSING') == os.environ['ANSIBLE_INTERNAL_DATA']

# Generated at 2022-06-12 23:34:30.673686
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'first': {'fallback': (env_fallback, 'FIRST_ENV_VAR')},
        'second': {'fallback': (env_fallback, 'SECOND_ENV_VAR')},
        'third': {'fallback': (env_fallback, ['THIRD_ENV_VAR', 'FOURTH_ENV_VAR'])},
        'fourth': {'fallback': (env_fallback, ['FIFTH_ENV_VAR', {'key': 'SIXTH_ENV_VAR'}])},
    }
    parameters = {}
    os.environ['FIRST_ENV_VAR'] = 'I exist'
    os.environ['THIRD_ENV_VAR'] = 'I also exist'
    os.environ

# Generated at 2022-06-12 23:34:40.596070
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-12 23:34:50.574712
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        the_param=dict(type='str'),
        dict_param=dict(type='dict', options=dict(
            the_key=dict(type='str'),
            the_int=dict(type='int'))),
        list_param=dict(type='list', elements='dict', options=dict(
            the_key=dict(type='str'),
            the_int=dict(type='int'))),
        nested_list_param=dict(type='list', elements='list', elements_name='single_list', options=dict(
            the_list=dict(type='list', elements='str', elements_name='single_string'))))


# Generated at 2022-06-12 23:34:59.958780
# Unit test for function remove_values
def test_remove_values():
    """
    Sanity test for function remove_values
    """

    assert remove_values(None, ['test']) is None
    assert remove_values(10, ['test']) == 10
    assert remove_values(10.5, ['test']) == 10.5
    assert remove_values('test', ['test']) == ''
    assert remove_values('test', ['st']) == 'te'
    assert remove_values('test', ['asdf']) == 'test'
    assert remove_values('testA', ['a']) == 'test'
    assert remove_values('testA', ['a', 'b']) == 'test'
    assert remove_values('testA', ['a', 'b', 'test']) == ''
    assert remove_values('testA', []) == 'testA'

# Generated at 2022-06-12 23:35:08.881150
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:35:19.689695
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """
    Sanity test for function sanitize_keys

    :return: None
    """

    source = {'1': {'2': {'3': {'4': 1}, 'a': 2}}, 'list': [{'b': 2}, {'c': 3}]}

    no_log_strings = (b'2', '4')

    result = sanitize_keys(source, no_log_strings)

    expected = {'1_': {'_': {'3_': {'_': 1}, 'a': 2}}, 'list': [{'b': 2}, {'c': 3}]}
    assert result == expected


# Generated at 2022-06-12 23:35:31.976971
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        param1=dict(required=True),
        param2=dict(required=True, fallback=(path_dwim_relative, ['ansible_module_generated_tmp'], dict(prefix=True))),
        param3=dict(required=True, fallback=(env_fallback, ['ANSIBLE_TEST_ENV_VAR', 'ANSIBLE_TEST_ENV_VAR_2'])),
        param4=dict(required=True, fallback=('any_other_callable',)),
        param5=dict(required=True, fallback=(env_fallback, 'FOO', dict(default='default'))),
    )

    os.environ['ANSIBLE_TEST_ENV_VAR'] = 'foo'

    #  Test 1

# Generated at 2022-06-12 23:35:44.150315
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo1=dict(fallback=(env_fallback, 'BAR')),
        foo2=dict(fallback=(env_fallback, dict(vars=('FOO1', 'FOO2')), dict(vars=('FOO3', 'BAR3')))),
        foo3=dict(fallback=(env_fallback, dict(vars=('FOO1', 'FOO2')), dict(vars=('FOO3', 'BAR3')))),
        foo4=dict(fallback=(env_fallback, dict(vars=('FOO1', 'FOO2')), dict(vars=('FOO3', 'BAR3')))),
    )
    parameters = dict(foo1='f1', foo2='f2')


# Generated at 2022-06-12 23:35:51.803013
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = {}
    # no fallback
    argument_spec = {'foo': {}}
    no_log_values = set_fallbacks(argument_spec, params)
    assert len(no_log_values) == 0
    # no fallback, no_log=True
    argument_spec = {'foo': {'no_log': True}}
    no_log_values = set_fallbacks(argument_spec, params)
    assert len(no_log_values) == 0

    # with fallback, no_log=True
    params = {}
    argument_spec = {'foo': {'fallback': [(env_fallback, 'ANSIBLE_TEST_FOO')], 'no_log': True}}
    os.environ['ANSIBLE_TEST_FOO'] = 'bar'
    no_log_values

# Generated at 2022-06-12 23:36:54.406249
# Unit test for function set_fallbacks
def test_set_fallbacks():
    set_fallback_parameters = {'a': 'foo'}
    fallback_spec = {'b': {'type': 'str', 'fallback': ((lambda: 'bar'), {'prefix': 'testing '})}}
    set_fallbacks(fallback_spec, set_fallback_parameters)
    assert set_fallback_parameters['b'] == 'bar'
    assert set_fallback_parameters['a'] == 'foo'
    # Test fallback with a linear list
    set_fallback_parameters = {'a': 'foo'}
    fallback_spec = {'b': {'type': 'str', 'fallback': ((lambda: 'bar'), 'list', {'prefix': 'testing '})}}
    set_fallbacks(fallback_spec, set_fallback_parameters)

# Generated at 2022-06-12 23:37:06.822708
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameter1 = {'param1': {'type': 'str', 'required': True}}
    parameters1 = dict(param1=None)
    no_log = set_fallbacks(parameter1, parameters1)
    assert len(no_log) == 0, 'no_log is not empty'
    assert parameters1.get('param1') == None, 'parameters are not empty'

    parameter2 = {'param2': {'type': 'str', 'required': True, 'fallback': (env_fallback, 'param2')}}
    parameters2 = dict(param2=None)
    no_log = set_fallbacks(parameter2, parameters2)
    assert len(no_log) == 0, 'no_log is not empty'

# Generated at 2022-06-12 23:37:18.073869
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        a=dict(fallback=(env_fallback, 'ANSIBLE_TEST')),
        b=dict(fallback=(env_fallback, 'ANSIBLE_TEST_B')),
        c=dict(fallback=(env_fallback, 'ANSIBLE_TEST_C')),
        d=dict(fallback=(env_fallback, 'ANSIBLE_TEST_D')),
        e=dict(fallback=(env_fallback, 'ANSIBLE_TEST_E')),
        f=dict(fallback=(env_fallback, 'ANSIBLE_TEST_F'))
    )
    parameters = dict(a=None, b=None, c=None, d=0, e=[], f=False)
    no_log_values = set_fallbacks(spec, parameters)

# Generated at 2022-06-12 23:37:26.616588
# Unit test for function set_fallbacks
def test_set_fallbacks():
    arg_spec = dict(
        first=dict(type='str', fallback=('env_fallback', 'FIRST')),
        second=dict(type='str', fallback=('env_fallback', 'SECOND'), no_log=True),
        third=dict(type='str', fallback=('env_fallback', 'THIRD')),
        fourth=dict(type='str', fallback=('env_fallback', 'FOURTH', 'FIFTH'), no_log=True),
        fifth=dict(type='str', fallback=('env_fallback', 'SIXTH'))
    )
    os.environ['FIRST'] = 'Testing first fallback'
    os.environ['FOURTH'] = 'Testing fourth fallback'
    params = dict(
        third='Testing third parameter'
    )

# Generated at 2022-06-12 23:37:38.229720
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {}