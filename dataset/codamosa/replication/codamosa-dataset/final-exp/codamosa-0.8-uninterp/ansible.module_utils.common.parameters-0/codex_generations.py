

# Generated at 2022-06-12 23:28:34.242469
# Unit test for function remove_values
def test_remove_values():
    assert remove_values(['a', 'b', 'c'], ['a', 'b']) == ['c']
    assert remove_values(['a', 'b', 'b', 'b', 'c'], ['a', 'b']) == ['c']

    assert remove_values('a', ['a']) == ''
    assert remove_values('ab', ['a']) == 'b'
    assert remove_values('ab', ['b']) == 'a'
    assert remove_values('aab', ['a']) == 'b'
    assert remove_values('ababab', ['a', 'b']) == ''
    assert remove_values('aba', ['a', 'b']) == ''
    assert remove_values('a', ['a', 'b']) == ''

# Generated at 2022-06-12 23:28:40.013592
# Unit test for function set_fallbacks
def test_set_fallbacks():
    params = dict()
    argument_spec = dict(param1={'type': 'float', 'fallback': (env_fallback, 'VAR')})
    no_log_values = set_fallbacks(argument_spec, params)
    assert no_log_values == set()
    assert params == dict()
    os.environ['VAR'] = '3.14'
    no_log_values = set_fallbacks(argument_spec, params)
    assert no_log_values == set()
    assert params == dict(param1=3.14)

# Generated at 2022-06-12 23:28:46.193516
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'dest': {'type': 'path', 'fallback': (env_fallback, ['HOME', 'USERPROFILE'])}}

    parameters = {'dest': None}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert 'dest' in parameters and parameters['dest'] == Path.home()
    assert len(no_log_values) == 0

    parameters = {'dest': '/home/cheese'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert 'dest' in parameters and parameters['dest'] == '/home/cheese'
    assert len(no_log_values) == 0


# Generated at 2022-06-12 23:28:53.787481
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'a': {'_ansible_fallback': (env_fallback, 'ANSIBLE_TESTING_FALLBACK')}}, {}) == set()
    assert set_fallbacks({'a': {'_ansible_fallback': (env_fallback, 'ANSIBLE_TESTING_FALLBACK')}}, {'a': 'test'}) == set()
    os.environ['ANSIBLE_TESTING_FALLBACK'] = MATCH_ALL
    assert set_fallbacks({'a': {'_ansible_fallback': (env_fallback, 'ANSIBLE_TESTING_FALLBACK')}}, {}) == {MATCH_ALL}

# Generated at 2022-06-12 23:29:04.662682
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        first=dict(fallback=(env_fallback, 'FIRST_VAR', 'SECOND_VAR')),
        third=dict(fallback=(env_fallback, 'THIRD_VAR')),
        fourth=dict(fallback=('invalid_fallback',)),
        fifth=dict(fallback=(env_fallback, 'FIFTH_VAR', 'SIXTH_VAR'), no_log=True),
        sixth=dict(fallback=(env_fallback, 'SIXTH_VAR', 'SEVENTH_VAR')),
    )
    parameters = dict(
        first='first_value',
        third='third_value',
    )
    os.environ['FIRST_VAR'] = 'env_first_value'
    del os.environ

# Generated at 2022-06-12 23:29:12.713150
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'hello': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST_HELLO')}}, {}) == set()

    os.environ['ANSIBLE_TEST_HELLO'] = 'world'
    assert set_fallbacks({'hello': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST_HELLO')}}, {}) == set()
    assert set_fallbacks({'hello': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST_HELLO')}}, {}) == set()


# Generated at 2022-06-12 23:29:21.761040
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        username=dict(type='str', aliases=['admin_user', 'user'], fallback=(env_fallback, 'ANSIBLE_NET_USERNAME')),
        password=dict(type='str', aliases=['admin_password', 'pass'], no_log=True, fallback=(env_fallback, ['ANSIBLE_NET_PASSWORD', 'NAPALM_PASSWORD'])),
        hostname=dict(type='str', required=True, fallback=(env_fallback, ['ANSIBLE_NET_HOSTNAME', 'NAPALM_HOSTNAME'])),
        optional_args=dict(type='str', fallback=({'key': 'val'},)),
    )
    parameters = dict()

# Generated at 2022-06-12 23:29:29.769386
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'a': {'type': 'list', 'fallback': (env_fallback,)},
        'b': {'type': 'list', 'fallback': (env_fallback, ['b'])},
        'c': {'type': 'list', 'fallback': (env_fallback, ['c'], {'key': 'null'})}
        }
    parameters = {}
    parameters = set_fallbacks(argument_spec, parameters)
    assert parameters['a'] == 'null'
    assert parameters['b'] == 'null'



# Generated at 2022-06-12 23:29:41.141813
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        path=dict(type='str', fallback=(env_fallback, ['ANSIBLE_ROLES_PATH'], dict())),
        src=dict(type='str', fallback=(env_fallback, ['ANSIBLE_ROLES_SRC'], dict())),
        paths=dict(type='list', fallback=(env_fallback, ['ANSIBLE_ROLES_PATH'], dict()), elements='str'),
        paths_default=dict(type='list', fallback=(env_fallback, ['ANSIBLE_ROLES_PATH'], dict()), elements='str', default=['/foo/bar']),
        secrets=dict(type='str', no_log=True, fallback=(env_fallback, ['ANSIBLE_ROLES_PATH'], dict())),
    )

    parameters

# Generated at 2022-06-12 23:29:44.141704
# Unit test for function sanitize_keys
def test_sanitize_keys():
    obj = {'item': 'foo', 'no_log_item': 'bar'}
    no_log_strings = frozenset(['bar'])
    ignore_keys = frozenset(['item'])
    new_value = sanitize_keys(obj, no_log_strings, ignore_keys)
    assert new_value['no_log_item'] == '<VALUE_HIDDEN>'


# Generated at 2022-06-12 23:30:14.265943
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({
        'foo': {
            'type': 'str',
            'fallback': (
                'from_fallback',
                'from_fallback2',
            ),
        },
        'bar': {
            'type': 'int',
        }
    }, {'bar': True}) == set(['from_fallback', 'from_fallback2'])

    # Check that env vars are not considered no_log values
    assert set_fallbacks({
        'foo': {
            'type': 'str',
            'no_log': True,
            'fallback': ('env_fallback', 'foo'),
        },
        'bar': {
            'type': 'int',
        }
    }, {'bar': True}) == set()



# Generated at 2022-06-12 23:30:23.704724
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:30:32.160815
# Unit test for function set_fallbacks
def test_set_fallbacks():
    fake_module = FakeModule()

# Generated at 2022-06-12 23:30:41.330593
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = dict()
    argument_spec = dict()
    # Given
    param = "i_am_alive"
    infos = dict()
    infos['fallback'] = [env_fallback, param]
    argument_spec[param] = infos
    # When
    env_var = 'i_am_alive'
    os.environ[env_var] = "I am a mock"
    no_log_values = set_fallbacks(argument_spec, parameters)
    # Then
    assert parameters[param] == "I am a mock"
    assert len(no_log_values) == 0



# Generated at 2022-06-12 23:30:49.391243
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {'a': {'type': 'str', 'fallback': (lambda x: 'c', [{'a': 'b'}])},
            'b': {'type': 'str', 'fallback': (env_fallback, ['FOOBAR'])}}
    params = {'a': 'a value'}
    no_log_values = set_fallbacks(spec, params)
    assert params['a'] == 'a value'
    assert 'c' in no_log_values

    params = {'b': 'b value'}
    no_log_values = set_fallbacks(spec, params)
    assert params['b'] == 'b value'

    os.environ['ANSIBLE_FOOBAR'] = 'foo'
    params = {}

# Generated at 2022-06-12 23:30:57.307884
# Unit test for function env_fallback
def test_env_fallback():
    arglist = ['/etc/ansible', '/etc']
    env_var = 'TEST_ENV'
    os.environ[env_var] = 'test_value'
    assert env_fallback(*arglist, **{'env_var': env_var}) == 'test_value'
    os.environ.pop(env_var, None)
    assert env_fallback(*arglist, **{'env_var': env_var}) == '/etc/ansible'
    assert env_fallback(*arglist[1:]) == '/etc'


# Generated at 2022-06-12 23:31:00.393264
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['test_var'] = 'test'
    assert env_fallback('test_var') == 'test'
    os.environ.pop('test_var')
    assert not os.environ['test_var']

# Generated at 2022-06-12 23:31:06.453764
# Unit test for function env_fallback
def test_env_fallback():
    with patch.dict('os.environ', {'ANSIBLE_MODULE_ARGS': 'test'}):
        assert env_fallback('ANSIBLE_MODULE_ARGS') == 'test'
    with patch.dict('os.environ', {'USER': 'test'}):
        assert env_fallback('ANSIBLE_MODULE_ARGS', 'USER') == 'test'
    with patch.dict('os.environ'):
        try:
            env_fallback('ANSIBLE_MODULE_ARGS', 'USER')
        except AnsibleFallbackNotFound:
            pass
        else:
            raise Exception('AnsibleFallbackNotFound was not raised')

# Generated at 2022-06-12 23:31:13.595821
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Unit test for function set_fallbacks."""

    assert set_fallbacks({'my_key': {'type': 'str', 'fallback': (env_fallback, 'KEY_NOT_FOUND', 'KEY_NOT_FOUND_EITHER')}}, {'my_key': 'my_value'}) == set()
    # as long as the fallback is not found ansible_fallback_not_found should be raised
    # in that case we don't want to set a value
    assert 'my_key' not in set_fallbacks({'my_key': {'type': 'str', 'fallback': (env_fallback, 'KEY_NOT_FOUND', 'KEY_NOT_FOUND_EITHER')}}, {})

# Generated at 2022-06-12 23:31:23.472758
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = {}
    argument_spec = dict(
        test=dict(type='str', fallback=(env_fallback, ['TEST_ENV', dict(key='TEST_ENV')])),
        test2=dict(type='str', fallback=(env_fallback, [dict(key='TEST_ENV')])),
        test3=dict(type='str', fallback=(None, [dict(key='TEST_ENV')])),
        test4=dict(type='str', fallback=(env_fallback, ['TEST_ENV', dict(key='NOT_FOUND')])),
        test5=dict(type='str', fallback=(env_fallback, ['NOT_FOUND'])),
    )
    no_log_values = set_fallbacks(argument_spec, parameters)


# Generated at 2022-06-12 23:31:48.174042
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'BAR'
    assert env_fallback('FOO') == 'BAR'
    os.environ.pop('FOO')
    assert env_fallback('FOO') != 'BAR'



# Generated at 2022-06-12 23:31:59.413999
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """Test sanitize_keys function"""

    # Test that sanitize_keys properly sanitizes the keys of a dict.
    from collections import OrderedDict
    test_data = OrderedDict([('key', 'value'), ('no_log', 'value'), ('_ansible_no_log', 'value'), ('_ansible_ignore', 'value'), ('_ansible_bar_ignore', 'value')])
    correct_data = OrderedDict([('key', 'value'), ('no_log', 'value'), ('_ansible_no_log', 'value'), ('_ansible_ignore', 'value'), ('_ansible_bar_ignore', 'value')])
    current_data = sanitize_keys(test_data, ['value'])
    assert current_data == correct_data

    # Test that sanitize_keys

# Generated at 2022-06-12 23:32:05.949560
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_NET_PASSWORD'] = 'foo'
    os.environ['ANSIBLE_NET_SSH_KEYFILE'] = 'bar'
    os.environ['ANSIBLE_NET_AUTH_PASS'] = 'baz'
    assert env_fallback('ANSIBLE_NET_PASSWORD') == 'foo'
    os.environ.pop('ANSIBLE_NET_PASSWORD')

    assert env_fallback('ANSIBLE_NET_SSH_KEYFILE') == 'bar'
    os.environ.pop('ANSIBLE_NET_SSH_KEYFILE')

    assert env_fallback('ANSIBLE_NET_AUTH_PASS') == 'baz'
    os.environ.pop('ANSIBLE_NET_AUTH_PASS')


# Generated at 2022-06-12 23:32:15.727556
# Unit test for function sanitize_keys
def test_sanitize_keys():
    from ansible.cli.arguments import option_helpers
    import ansible.module_utils.facts
    from ansible.module_utils.facts import get_distribution, get_distribution_version
    # Construct a large nested dict. This is always going to be a challenge for max recursion depth.
    os_facts = ansible.module_utils.facts.get_facts()['ansible_facts']
    obj = os_facts['ansible_facts']
    # Sanitize the object.
    obj = option_helpers.sanitize_keys(obj, {'pass', 'token', 'key', 'password'})
    # Use the os facts to figure out if we're running the test on a Linux or BSD system. This is important since
    # the os_facts object will be different depending on the OS that it's running on.


# Generated at 2022-06-12 23:32:19.395761
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = "bar"
    assert env_fallback("BAR", "FOO") == "bar"


# Generated at 2022-06-12 23:32:24.597735
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({}, {}) == set()
    assert set_fallbacks({'foo': {'default': 'bar'}}, {}) == set()
    assert set_fallbacks({'foo': {'default': 'bar'}}, {'foo': 'bar'}) == set()
    assert set_fallbacks({'foo': {'default': 'bar', 'fallback': (lambda: 'baz')}}, {}) == {'baz'}
    assert set_fallbacks({'foo': {'default': 'bar', 'fallback': (lambda: 'baz')}}, {'foo': 'bar'}) == set()
    assert set_fallbacks({'foo': {'default': 'bar', 'fallback': (env_fallback, 'FOO'), 'no_log': True}}, {'foo': 'bar'})

# Generated at 2022-06-12 23:32:37.106614
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {
        'name': {
            'type': 'str',
            'fallback': (env_fallback, ('name_env',))
        },
        'age': {
            'type': 'int',
            'fallback': (env_fallback, ('age_env',))
        }
    }
    parameters = {
        'name': 'John'
    }
    no_log_values = set_fallbacks(spec, parameters)
    assert len(no_log_values) == 0
    assert parameters == {'name': 'John'}

    os.environ['name_env'] = "Doe"
    os.environ['age_env'] = "30"
    parameters = {}
    no_log_values = set_fallbacks(spec, parameters)

# Generated at 2022-06-12 23:32:47.314863
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['FOO'] = 'bar'
    os.environ['FOO_BAR'] = 'baz'
    assert env_fallback('FOO') == 'bar'
    assert env_fallback('FOO_BAR') == 'baz'
    assert env_fallback('FOO', 'FOO_BAR') == 'bar'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('FOO_BAR', 'FOO_BAZ')
        env_fallback('FOO_BAR1')

    del os.environ['FOO']
    del os.environ['FOO_BAR']


# Generated at 2022-06-12 23:32:54.766526
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'a': {'type': 'str'}, 'b': {'type': 'str', 'no_log': True, 'fallback': (env_fallback, 'b')}}
    parameters = {'a': 'hello'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters == {'a': 'hello', 'b': 'world'}
    assert os.environ['b'] == 'world'
    assert os.environ['a'] == 'hello'
    os.environ.pop('b', None)
    os.environ.pop('a', None)


# Generated at 2022-06-12 23:32:58.509430
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('WIN_PATH') == '/Remote/C/Windows'
    assert env_fallback('HOME') == '/root'
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NO_EXIST')


# Generated at 2022-06-12 23:33:25.793016
# Unit test for function sanitize_keys
def test_sanitize_keys():
    no_log_strings = ['github_password']
    ignore_keys = frozenset(['module_name'])

    test_dict = {'name': 'ansible', 'module_name': 'github', 'github_password': 'gopher'}
    test_list = [test_dict, ('1', {'a': 'b', 'c': 'd'})]
    test_set = set(test_list)
    test_tuples = (test_list, test_set)

    new_dict = _sanitize_keys_conditions(test_dict, no_log_strings, ignore_keys)
    new_list = _sanitize_keys_conditions(test_list, no_log_strings, ignore_keys)

# Generated at 2022-06-12 23:33:31.385220
# Unit test for function sanitize_keys
def test_sanitize_keys():
    assert sanitize_keys({'a': 1, 'b': 2, 'c': None, 'd': 'd'}, set(['a'])) == {'b': 2, 'c': None, 'd': 'd'}
    assert sanitize_keys({'a': 1, 'b': 2, 'c': None, 'd': 'd'}, set(['a', 'b'])) == {'c': None, 'd': 'd'}
    assert sanitize_keys({'a': 1, 'b': 2, 'c': None, 'd': 'd'}, set(['a', 'c'])) == {'b': 2, 'd': 'd'}

# Generated at 2022-06-12 23:33:42.656370
# Unit test for function env_fallback
def test_env_fallback():
    """Test for function env_fallback"""

# Generated at 2022-06-12 23:33:47.025216
# Unit test for function set_fallbacks
def test_set_fallbacks():
    module = AnsibleModule(
        argument_spec={'name': {'type': 'str', 'required': True, 'fallback': (env_fallback, 'USER')}}
    )
    assert module.params['name'] == 'root'


# Plugins can register custom tests
_ADDITIONAL_CHECKS = []



# Generated at 2022-06-12 23:33:57.868932
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = dict(
        foo=dict(fallback=(env_fallback, ('FOO',))),
        bar=dict(fallback=(env_fallback, 'BAR')),
        baz=dict(fallback=(env_fallback, 'BAZ', dict(required=True))),
    )
    parameters = dict()
    result = set_fallbacks(spec, parameters)
    assert result == set()
    assert parameters == dict(foo='FOO', bar='BAR')

    # When value has no_log=True, return it in a list
    spec['bar'] = dict(fallback=(env_fallback, 'BAR'), no_log=True)
    parameters = dict()
    result = set_fallbacks(spec, parameters)
    assert result == set('BAR')

# Generated at 2022-06-12 23:34:07.636308
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        one=dict(type='int', fallback=(env_fallback, 'ONE'))
    )
    parameters = dict(
        two=2
    )
    expected_no_log_values = set()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert expected_no_log_values == no_log_values, \
           "set_fallbacks did not return the expected set of no log values, " \
           + 'got %s, expected %s' % (no_log_values, expected_no_log_values)
    expected_parameters = dict(
        one=1,
        two=2
    )

# Generated at 2022-06-12 23:34:16.289888
# Unit test for function sanitize_keys
def test_sanitize_keys():
    class TestModule(object):
        def __init__(self, foo=None, bar=None, bam=None):
            self.argument_spec = dict(
                foo=dict(type='str', no_log=True),
                bar=dict(type='str'),
                bam=dict(type='str', no_log=True),
            )
            self.foo = foo
            self.bar = bar
            self.bam = bam

    obj = TestModule(
        foo='password',
        bar='password',
        bam='password',
    )
    no_log_strings = ['password']

    new_obj = sanitize_keys(obj, no_log_strings, ignore_keys=frozenset(['bam']))
    assert obj.foo == 'password'

# Generated at 2022-06-12 23:34:27.172832
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Function set_fallbacks (function) test cases."""

    # simple test
    spec = {'param1': {'type': 'str', 'fallback': (env_fallback, 'ANSIBLE_TEST')}}
    os.environ['ANSIBLE_TEST'] = 'foobar'
    parameters = {}
    no_log = set_fallbacks(spec, parameters)
    assert parameters['param1'] == 'foobar'
    assert no_log == set()
    del os.environ['ANSIBLE_TEST']

    # test with list of fallbacks
    spec = {'param1': {'type': 'str', 'fallback': (env_fallback, ['ANSIBLE_TEST', 'SECOND_TEST'])}}
    os.environ['ANSIBLE_TEST'] = 'foobar'
    parameters

# Generated at 2022-06-12 23:34:37.507082
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Set fallback values"""
    argument_spec = {
        'bacon': {
            'type': 'str',
            'fallback': (env_fallback, ('ANSIBLE_BACON', 'BACON_PATH', 'BACON_CONFIG')),
            'required': True,
        }
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)

    if 'ANSIBLE_BACON' not in os.environ:
        os.environ['ANSIBLE_BACON'] = 'env_bacon'

    assert parameters['bacon'] == 'env_bacon'
    assert 'env_bacon' not in no_log_values



# Generated at 2022-06-12 23:34:44.944406
# Unit test for function sanitize_keys
def test_sanitize_keys():
    """Unit test function for function sanitize_keys"""
    assert 'foo' == sanitize_keys('foo', set(['foo']))

    assert {'baz': None} == sanitize_keys({'foo': None}, set(['foo']))

    # Test sanitize_keys() is idempotent
    data = {'foo': 'bar'}
    assert data == sanitize_keys(data, set(['foo']))
    assert data == sanitize_keys(data, set(['foo']))

    # Test sanitizing multiple keys
    assert {'baz': 'bar'} == sanitize_keys({'foo': 'bar'}, set(['foo', 'baz']))

    # Test sanitizing multiple keys in a data structure

# Generated at 2022-06-12 23:35:16.420384
# Unit test for function remove_values
def test_remove_values():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import binary_type, text_type
    # for test purpose, modify no_log_strings to use unicode string
    no_log_strings = [to_text('password', errors='surrogate_or_strict')]
    no_log_binary_strings = [to_bytes(s, encoding='utf-8', errors='surrogate_or_strict') for s in no_log_strings]

    # Case 1: Basic remove_values use case on a key
    data = dict(key=dict(sub_key="ansible_password"))
    # this is not affected because password is not in key name
    assert remove_values(data, no_log_strings) == data
    # this is affected because password is

# Generated at 2022-06-12 23:35:20.232071
# Unit test for function env_fallback
def test_env_fallback():
    try:
        env_fallback()
        assert False
    except AnsibleFallbackNotFound:
        pass
    os.environ['TEST_VAR'] = 'test_value'
    assert env_fallback('TEST_VAR') == 'test_value'



# Generated at 2022-06-12 23:35:24.283639
# Unit test for function env_fallback
def test_env_fallback():
    """Test that env_fallback function works as expected"""

    # not set, so raise exception
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('FOO')

    os.environ['FOO'] = 'bar'

    assert env_fallback('FOO') == 'bar'

    try:
        os.environ['FOO'] = 'bar'

        assert env_fallback('FOO') == 'bar'
    finally:
        del os.environ['FOO']



# Generated at 2022-06-12 23:35:34.980459
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert_equals(set_fallbacks({'a': {'fallback': ('env_fallback', 'FOO')}}, {}), set())
    assert_equals(set_fallbacks({'b': {'fallback': ('env_fallback', 'FOO')}}, {'b': 'b'}), set())
    assert_equals(set_fallbacks({'c': {'fallback': ('env_fallback', 'BAR')}}, {}), set())
    assert_equals(set_fallbacks({'d': {'fallback': ('env_fallback', 'BAR'), 'no_log': True}}, {}), set(['BAR']))

# Generated at 2022-06-12 23:35:45.937274
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'test': {'type': 'str', 'fallback': (env_fallback, ['ENV_VAR_TEST']), 'no_log': False},
        'test2': {'type': 'str', 'fallback': (env_fallback, ['ENV_VAR_TEST2']), 'no_log': True},
    }
    parameters = {'test': 'test_value'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['test'] == 'test_value'
    assert not no_log_values, 'No log values set for non-secret parameters'

    parameters = {}
    os.environ['ENV_VAR_TEST'] = 'test_value'

# Generated at 2022-06-12 23:35:51.322782
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'param': {'fallback': (env_fallback, ['TEST_BAR'])}}
    parameters = {}
    os.environ['TEST_BAR'] = 'foo'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['param'] == 'foo'
    assert no_log_values == set()

    argument_spec = {'param': {'fallback': (env_fallback, ['TEST_BAR']), 'default': 'foo'}}
    parameters = {}
    del os.environ['TEST_BAR']
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['param'] == 'foo'
    assert no_log_values == set()


# Generated at 2022-06-12 23:35:58.121644
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_FOO'] = 'bar'
    assert env_fallback('ANSIBLE_TEST_FOO') == 'bar'
    assert env_fallback('ANSIBLE_TEST_BAR') == 'bar'
    try:
        env_fallback('ANSIBLE_TEST_NON_EXIST')
        assert False
    except AnsibleFallbackNotFound:
        pass



# Generated at 2022-06-12 23:36:01.789955
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('ANSIBLE_TEST_VAR') == os.environ['ANSIBLE_TEST_VAR']
    with pytest.raises(AnsibleFallbackNotFound):
        assert env_fallback('ANSIBLE_TEST_VAR_NOT_SET')


# Generated at 2022-06-12 23:36:11.326190
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # param exists in parameters and fallback exists, should NOT assign fallback value
    argument_spec = {'param': {'fallback': env_fallback, 'type': 'str'}}
    parameters = {'param': 'value'}
    result = {'param': 'value'}
    assert set_fallbacks(argument_spec, parameters) == set()
    assert parameters == result

    # param doesn't exist in parameters and fallback exists, should assign fallback value
    argument_spec = {'param': {'fallback': env_fallback, 'type': 'str'}}
    parameters = {}
    result = {'param': os.environ['HOME']}
    assert set_fallbacks(argument_spec, parameters) == set()
    assert parameters == result

    # param doesn't exist in parameters but fallback doesn't exist, should not

# Generated at 2022-06-12 23:36:22.005225
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'foobar': {'fallback': env_fallback}}, {}) == set()
    assert set_fallbacks({'foobar': {'fallback': (None,)}}, {}) == set()
    assert set_fallbacks({'foobar': {'fallback': (None,), 'no_log': True}}, {}) == set()
    assert set_fallbacks({'foobar': {'fallback': env_fallback, 'no_log': True}}, {}) == set()
    os.environ['foobar'] = 'baz'
    assert set_fallbacks({'foobar': {'fallback': env_fallback, 'no_log': True}}, {}) == {'baz'}

# Generated at 2022-06-12 23:36:51.522026
# Unit test for function sanitize_keys
def test_sanitize_keys():
    # flake8: noqa
    # pylint: disable=too-many-lines
    assert sanitize_keys(None, []) == None

    assert sanitize_keys(no_log_strings=[b'computer'], obj=b'I like to say hello to my computer') == b'I like to say hello to my *******'
    assert sanitize_keys(no_log_strings=[u'computer'], obj=u'I like to say hello to my computer') == u'I like to say hello to my *******'
    assert sanitize_keys(no_log_strings=['computer'], obj='I like to say hello to my computer') == 'I like to say hello to my *******'

# Generated at 2022-06-12 23:36:59.959891
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('test', 'test1') == 'test'
    os.environ['test'] = 'test1'
    os.environ['test'] = 'test2'
    assert env_fallback('test', 'test1') == 'test2'
    os.environ.pop('test', None)
    os.environ.pop('test1', None)
    try:
        env_fallback('test', 'test1')
    except AnsibleFallbackNotFound as e:
        assert to_native(e) == "Unable to find fallback for test, test1"
        return

    raise AssertionError('We should not reach this line.')



# Generated at 2022-06-12 23:37:10.176552
# Unit test for function sanitize_keys

# Generated at 2022-06-12 23:37:21.103962
# Unit test for function sanitize_keys
def test_sanitize_keys():
    dict_value = {'foo': {'bar': 42}, '_ansible_no_log': True}
    list_value = [{'foo': 'bar'}]
    tuple_value = ({'foo': 'bar'},)
    set_value = ({'foo': 'bar'},)

    assert sanitize_keys(dict_value, frozenset(('foo', 'bar'))) == {'foo': {'bar': 42}}
    assert sanitize_keys(list_value, frozenset(('foo', 'bar'))) == [{'foo': 'bar'}]
    assert sanitize_keys(tuple_value, frozenset(('foo', 'bar'))) == ({'foo': 'bar'},)

# Generated at 2022-06-12 23:37:26.970853
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'param': {'type': 'str', 'default': 'my_default_value'},
        'extra': {'type': 'str', 'fallback': (env_fallback, ['MY_ENV_VAR'])},
        'extra_kwargs': {'type': 'str', 'fallback': (env_fallback, ['MY_ENV_VAR'], {'default': 'default_value'})},
    }
    parameters = {
        'param': 'my_value'
    }
    os.environ['MY_ENV_VAR'] = 'my_extra_value'
    no_log_values = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:37:38.480542
# Unit test for function remove_values
def test_remove_values():
    # setup
    value = {'msg': 'hi', 'password': 'p@ssw0rd', 'list': [{'msg': 'bye', 'password': 'hunter2'}]}
    no_log_strings = ['hunter2', 'p@ssw0rd']
    expected = {'msg': 'hi', 'password': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 'list': [{'msg': 'bye', 'password': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'}]}
    # test w/ expected result
    result = remove_values(value, no_log_strings)
    assert result == expected, result
    # test w/ unexpected result