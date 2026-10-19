

# Generated at 2022-06-12 23:28:16.871081
# Unit test for function env_fallback
def test_env_fallback():
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('THIS_VALUE_SHOULD_NEVER_EXIST')



# Generated at 2022-06-12 23:28:25.656403
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Regular use
    argument_spec = dict(
        answer=dict(type='int', default=42),
        name=dict(type='str'),
    )
    parameters = dict(answer=24)
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters['answer'] == 24
    assert parameters['name'] == 42

    # Fallback not found
    parameters = dict(exception=None)
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert 'exception' not in parameters

    # Fallback with no_log

# Generated at 2022-06-12 23:28:35.786446
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """Test setting defaults using the fallback method"""

# Generated at 2022-06-12 23:28:46.634034
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        param=dict(
            fallback=(env_fallback, 'TEST_PARAM')
        )
    )
    parameters = {}
    os.environ['TEST_PARAM'] = 'test_value'
    test_fallback = set_fallbacks(argument_spec, parameters)
    assert test_fallback == set()
    assert parameters['param'] == 'test_value'
    del os.environ['TEST_PARAM']
    os.environ['TEST_PARAM'] = ''
    test_fallback = set_fallbacks(argument_spec, parameters)
    assert test_fallback == set()
    assert parameters['param'] == ''
    del os.environ['TEST_PARAM']
    test_fallback = set_fallbacks(argument_spec, parameters)

# Generated at 2022-06-12 23:28:57.447392
# Unit test for function env_fallback
def test_env_fallback():
    with patch.dict('os.environ', {'ENV_FALLBACK': "foo"}):
        assert env_fallback("ENV_FALLBACK") == "foo"
    try:
        env_fallback("ENV_FALLBACK")
        raise Exception("env_fallback() should have raised AnsibleFallbackNotFound exception")
    except AnsibleFallbackNotFound:
        pass
    try:
        env_fallback("ENV1", "ENV2")
        raise Exception("env_fallback() should have raised AnsibleFallbackNotFound exception")
    except AnsibleFallbackNotFound:
        pass

# Generated at 2022-06-12 23:29:07.590728
# Unit test for function set_fallbacks
def test_set_fallbacks():
    arg_spec = dict(
        foo=dict(fallback=(env_fallback, 'FOO', 'BAR'))
    )
    test_parameters = {}
    no_log_values = set_fallbacks(arg_spec, test_parameters)
    assert no_log_values == set()
    assert test_parameters.get('foo') == os.environ.get('FOO')
    assert len(test_parameters) == 1

    arg_spec = dict(
        foo=dict(fallback=(env_fallback, 'FOO')),
        bar=dict(fallback=(env_fallback, 'BAR', 'BAZ'))
    )
    test_parameters = {}
    no_log_values = set_fallbacks(arg_spec, test_parameters)
    assert no_log_

# Generated at 2022-06-12 23:29:14.396587
# Unit test for function set_fallbacks
def test_set_fallbacks():
    specs = {
        'param1': {
            'type': 'str',
            'required': True
        },
        'param2': {
            'type': 'str',
            'required': True
        }
    }
    parameters = {
        'param1': '1'
    }
    no_log_values = set_fallbacks(specs, parameters)
    assert len(no_log_values) == 0
    assert 'param2' in parameters

    parameters = {
        'param1': '1'
    }
    no_log_values = set_fallbacks(specs, parameters)
    assert len(no_log_values) == 0
    assert 'param2' in parameters


# Generated at 2022-06-12 23:29:22.499579
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:29:31.790817
# Unit test for function set_fallbacks
def test_set_fallbacks():
    fallback_called = False
    @staticmethod
    def my_callable(*args, **kwargs):
        nonlocal fallback_called
        fallback_called = True
        return "fallback_value"


# Generated at 2022-06-12 23:29:43.130389
# Unit test for function set_fallbacks
def test_set_fallbacks():
    tmp_environ = {}
    tmp_environ['ANSIBLE_NETCONF_PASSWORD'] = 'foo'
    with patch.dict(os.environ, tmp_environ):
        assert_raises(AnsibleFallbackNotFound, env_fallback, 'bar')
        assert env_fallback('ANSIBLE_NETCONF_PASSWORD') == 'foo'
        assert_raises(TypeError, env_fallback, 'ANSIBLE_NETCONF_PASSWORD', 'bar')


# Generated at 2022-06-12 23:30:13.760586
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # test fallback function ANSIBLE_VAR_normal
    argument_spec = dict(state=dict(type='str', default='present', choices=['present', 'absent'], fallback=(env_fallback, 'ANSIBLE_VAR_normal')),
        a=dict(type='list', fallback=(env_fallback, 'ANSIBLE_VAR_list')),
        b=dict(type='int', fallback=(env_fallback, 'ANSIBLE_VAR_int')))
    parameters = dict(state='present')
    parameters_expected = dict(state='present', a=[1,2], b=1)
    os.environ['ANSIBLE_VAR_normal'] = 'present'
    os.environ['ANSIBLE_VAR_list'] = '[1,2]'

# Generated at 2022-06-12 23:30:18.951387
# Unit test for function env_fallback
def test_env_fallback():
    ''' Test env_fallback for AnsibleFallbackNotFound and not '''
    os.environ['ENV_TEST_FALLBACK'] = "test"
    assert env_fallback('ENV_TEST_FALLBACK') == "test"
    assert env_fallback('') == ''



# Generated at 2022-06-12 23:30:20.918853
# Unit test for function env_fallback
def test_env_fallback():
    os.environ["TEST"] = "test"
    assert env_fallback("TEST") == "test"


# Generated at 2022-06-12 23:30:30.483166
# Unit test for function sanitize_keys
def test_sanitize_keys():
    container = {
        'apple': 'red',
        'banana': 'yellow',
        'carrot': 'orange',
        'data': [
            'a',
            'b',
            'c',
        ],
        'data2': [
            ['a', 'b', 'c'],
            ['A', 'B', 'C']
        ],
        'data3': [
            'a',
            'b',
            {'key': 'value'},
        ],
    }

    # Run the tests
    no_log_strings = set(['value'])
    new_container = sanitize_keys(container, no_log_strings, ignore_keys=set(['apple']))

# Generated at 2022-06-12 23:30:34.390960
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback(1, 2) == 1
    assert env_fallback(2, 3) == 3
    with pytest.raises(AnsibleFallbackNotFound):
        assert env_fallback()


# Generated at 2022-06-12 23:30:39.430458
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_VAR'] = 'fallback'
    assert env_fallback('ANSIBLE_TEST_VAR') == 'fallback'

    del os.environ['ANSIBLE_TEST_VAR']
    assert env_fallback('NOT_FOUND_VALUE') is None



# Generated at 2022-06-12 23:30:48.274139
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        param_1=dict(required=False, fallback=(env_fallback, ['PARAM_1'])),
        param_2=dict(required=False, fallback=(env_fallback, ['PARAM_2'])),
        param_3=dict(required=False, fallback=(env_fallback, ['PARAM_3'])),
        param_no_log=dict(required=False, no_log=True, fallback=(env_fallback, ['PARAM_NO_LOG'])),
        param_invalid_env=dict(required=False, fallback=(env_fallback, ['PARAM_INVALID_ENV'])),
    )


# Generated at 2022-06-12 23:30:57.701205
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'a': {'type': 'str', 'fallback': (env_fallback, ['VAR_A'])},
        'b': {'type': 'str', 'fallback': (env_fallback, ['VAR_B'])}
    }
    parameters = {'a': 'foo'}
    os.environ['VAR_A'] = 'foo'
    os.environ['VAR_B'] = 'bar'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters['b'] == 'bar'
    assert no_log_values == set()



# Generated at 2022-06-12 23:31:08.323507
# Unit test for function set_fallbacks
def test_set_fallbacks():
    # Preconditions
    # These environment variables should be set since they are needed by
    # some of the tests
    assert 'USER' in os.environ
    assert 'USERNAME' in os.environ

    # These environment variables should not be set since they are not needed
    # by any of the tests
    assert not os.path.isfile('/tmp/test_option_fallback.txt')

    # Test: fallback strategy of env_fallback()
    # Setup: Pass in environment variables
    test_case1 = {'param1': {
        'fallback': (env_fallback, 'USER'),
        },
    }
    # Test: Pass in a parameter for param1
    parameters1 = {'param1': 'foo'}
    # Test: Ensure that the fallback value is not present
    assert set_fallbacks

# Generated at 2022-06-12 23:31:12.883599
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['ANSIBLE_TEST_ENV_FALLBACK'] = 'FALLBACK'
    assert env_fallback('ANSIBLE_TEST_ENV_FALLBACK') == 'FALLBACK'
    del os.environ['ANSIBLE_TEST_ENV_FALLBACK']
    assert env_fallback('ANSIBLE_TEST_ENV_FALLBACK') == ''

    assert env_fallback('ANSIBLE_TEST_NOT_ENV_FALLBACK') == ''


# Generated at 2022-06-12 23:31:38.660190
# Unit test for function set_fallbacks
def test_set_fallbacks():
    import logging
    import os
    import tempfile
    import unittest

    from ansible.module_utils import basic

    def _get_test_argument_spec(required=False, fallback=None):
        return dict(
            required_test=dict(required=required, fallback=fallback),
            non_required_test=dict(required=False, fallback=fallback),
        )

    def _get_exception_message(exc):
        return str(exc)

    class TestModuleArgumentSpec(object):
        # Override get_option to simply return the option value,
        # or if it's falsey, the default value
        def get_option(self, option_name):
            if option_name != 'log_path':
                return self._options[option_name]
            else:
                return self

# Generated at 2022-06-12 23:31:48.483802
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:31:59.780617
# Unit test for function set_fallbacks
def test_set_fallbacks():
    assert set_fallbacks({'a': {'fallback': (env_fallback, 'a', 'b')}}, {}) == set()
    assert set_fallbacks({'a': {'fallback': (env_fallback, 'a', 'b')}}, {'a': 'x'}) == set()
    os.environ['a'] = 'x'
    assert set_fallbacks({'a': {'fallback': (env_fallback, 'a', 'b')}}, {}) == set(['x'])
    assert set_fallbacks({'a': {'fallback': (env_fallback, 'a', 'b')}}, {'a': 'x'}) == set(['x'])

# Generated at 2022-06-12 23:32:11.679215
# Unit test for function set_fallbacks

# Generated at 2022-06-12 23:32:19.318162
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(type='str', fallback=(env_fallback, 'DEFAULT_FOO')),
        bar=dict(type='str', fallback=(env_fallback, 'DEFAULT_BAR')),
        baz=dict(type='dict', fallback=(env_fallback, 'DEFAULT_BAZ'))
    )

    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert not no_log_values

    assert 'DEFAULT_FOO' in parameters
    assert 'DEFAULT_BAR' in parameters
    assert 'DEFAULT_BAZ' not in parameters

    parameters['baz'] = 'baz'

    no_log_values = set_fallbacks(argument_spec, parameters)
    assert not no_log_values

# Generated at 2022-06-12 23:32:27.657893
# Unit test for function set_fallbacks
def test_set_fallbacks():

    # Test with different fallback types
    spec = dict(
        string=dict(
            type='str',
            fallback=(None,)),
        string1=dict(
            type='str',
            fallback=(env_fallback, 'string')),
        string2=dict(
            type='str',
            fallback=(env_fallback, 'envstring')),
        string3=dict(
            type='str',
            fallback=(env_fallback, 'string', dict(a=1, b=2))),
        string4=dict(
            type='str',
            fallback=(env_fallback, 'envstring', dict(a=3, b=4))),
    )


# Generated at 2022-06-12 23:32:36.544225
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'param1': {'type': 'str', 'required': True},
        'param2': {'type': 'path', 'no_log': True},
        'param3': {'type': 'str', 'fallback': (env_fallback, ['MEHI_PARAM'])}
    }
    parameters = {'param1': '3'}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0


# Generated at 2022-06-12 23:32:43.513080
# Unit test for function set_fallbacks
def test_set_fallbacks():
    from collections import OrderedDict
    args1 = {'param1': {'type': 'str', 'fallback': (env_fallback, ('myparam',))}}
    args2 = {'param1': {'type': 'str', 'fallback': (lambda: 'fallback', ('env_param',))}}
    args3 = {'param1': {'type': 'str', 'fallback': (lambda x, y: x+y, (1, 2))}}
    args4 = {'param1': {'type': 'str', 'fallback': (lambda x, y: x+y, (1, 2), {'z': 1})}}
    args5 = {'param1': {'type': 'str', 'fallback': (env_fallback, ('myparam1', 'myparam2'))}}
    args6

# Generated at 2022-06-12 23:32:53.057865
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(test_set=dict(type='str', fallback=(env_fallback, ['CHECK_THIS_ENV_VAR'])))
    params = dict(test_set='foo')
    env_var_name = 'CHECK_THIS_ENV_VAR'
    os.environ[env_var_name] = 'env_var_value'
    no_log_values = set_fallbacks(argument_spec, params)
    assert params['test_set'] == 'env_var_value'
    assert no_log_values == set(['env_var_value'])
    del os.environ[env_var_name]
    # Test that fallback only kicks in when env_var is specified
    no_log_values = set_fallbacks(argument_spec, dict())

# Generated at 2022-06-12 23:32:57.162203
# Unit test for function env_fallback
def test_env_fallback():
    assert env_fallback('ANSIBLE_LOGIN_PASSWORD') == os.environ['ANSIBLE_LOGIN_PASSWORD']
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('ANSIBLE_LOGIN_SHOULD_FAIL')


# Generated at 2022-06-12 23:33:29.002981
# Unit test for function env_fallback
def test_env_fallback():
    if os.environ.get('ANSIBLE_TEST_ENV_FALLBACK') is not None:
        # Someone did that already
        return True
    os.environ['ANSIBLE_TEST_ENV_FALLBACK'] = 'testing'
    assert env_fallback('ANSIBLE_TEST_ENV_FALLBACK') == 'testing'
    del os.environ['ANSIBLE_TEST_ENV_FALLBACK']
    failed = False
    try:
        env_fallback('ANSIBLE_TEST_ENV_FALLBACK')
    except AnsibleFallbackNotFound:
        failed = True
    assert failed



# Generated at 2022-06-12 23:33:34.669766
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        one=dict(fallback=(env_fallback, 'TEST_VAR')),
        two=dict(fallback=(env_fallback, 'TEST_UNSET_VAR', 'TEST_VAR')),
        three=dict(fallback=(env_fallback, 'TEST_UNSET_VAR', 'TEST_VAR'),
                   no_log=True),
    )
    parameters = {}

    assert set_fallbacks(argument_spec, parameters) == set(['test'])
    assert parameters.get('one') == 'test'
    assert parameters.get('two') == 'test'
    assert parameters.get('three') == 'test'

    parameters = {}
    os.environ['TEST_VAR'] = 'testing'

# Generated at 2022-06-12 23:33:46.074176
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = dict(
        foo=dict(fallback=(env_fallback, ['FOO_VAR', 'FOO_DEFAULT'])),
        baz=dict(fallback=(env_fallback, 'BAZ_VAR')),
        bar=dict(fallback=(env_fallback, dict(default='BAR_DEFAULT'))),
    )
    parameters = dict(foo=None, baz=None, bar=None)
    # test normal operation
    os.environ['FOO_VAR'] = 'foo'
    os.environ['BAZ_VAR'] = 'baz'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert (parameters['foo'] == 'foo')
    assert (parameters['baz'] == 'baz')

# Generated at 2022-06-12 23:33:56.730339
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {
        'foo': {'type': 'str', 'default': '', 'fallback': (env_fallback, 'ANSIBLE_TEST_FOO'), 'no_log': True},
        'bar': {'type': 'str', 'default': '', 'fallback': (env_fallback, 'ANSIBLE_TEST_BAR', 'ANSIBLE_TEST_BAZ')},
        'baz': {'type': 'str', 'default': '', 'fallback': (env_fallback, ['ANSIBLE_TEST_BAZ'])}
    }
    parameters = {
        'foo': 'foo',
        'baz': 'baz',
    }

    assert set_fallbacks(argument_spec, parameters) == set()

# Generated at 2022-06-12 23:34:01.968138
# Unit test for function sanitize_keys
def test_sanitize_keys():
    from collections import Counter
    from collections import defaultdict
    from collections import OrderedDict
    from collections import namedtuple
    from datetime import datetime

    mock_key = 'foo'
    mock_value = 'bar'
    mock_no_log_strings = ['bar']

    # Test that we do nothing if obj is not a container object
    assert sanitize_keys(None, mock_no_log_strings) is None
    assert sanitize_keys(True, mock_no_log_strings) is True
    assert sanitize_keys('test', mock_no_log_strings) == 'test'
    assert sanitize_keys(1234, mock_no_log_strings) == 1234
    assert sanitize_keys(5.5, mock_no_log_strings) == 5.5

# Generated at 2022-06-12 23:34:09.891908
# Unit test for function set_fallbacks
def test_set_fallbacks():
    """
    test case for function set_fallbacks
    """
    # Test for fallback when provide both fallback and default value.
    argument_spec = dict(foo=dict(type='str', default='bar', fallback=(env_fallback, 'FOO_ENV_VAR', 'FOO_DEFAULT')))
    parameters = dict()
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert len(no_log_values) == 0
    assert parameters['foo'] == 'bar'
    assert len(os.environ) == 0

    # Test for fallback when provide fallback, but not default value.
    del argument_spec['foo']

# Generated at 2022-06-12 23:34:17.883933
# Unit test for function remove_values
def test_remove_values():

    no_log_strings = ['no-log-string', 'another-no-log-string']

# Generated at 2022-06-12 23:34:28.279828
# Unit test for function set_fallbacks
def test_set_fallbacks():
    for fb in ['env', 'bool', 'int', 'float']:
        spec = {
            'x': {'type': 'str', 'fallback': (fb, 'FOO')},
            'y': {'type': 'str', 'fallback': (fb, ['BAR'])},
            'z': {'type': 'str', 'fallback': (fb, ['BAZ1', 'BAZ2'])},
            'w': {'type': 'str', 'fallback': (fb,)},
        }
        params = {}
        assert set_fallbacks(spec, params) == set([])
        assert params == {'x': 'FOO', 'y': 'BAR', 'z': 'BAZ1'}
        assert set_fallbacks(spec, params) == set([])

# Generated at 2022-06-12 23:34:39.340733
# Unit test for function sanitize_keys
def test_sanitize_keys():

    # First, test the sanitization of keys in container object.
    # We'll test a dictionary, a list, and a set to ensure all containers are tested.
    no_log_strings = ['password', 'secret', 'private']
    ignore_keys = ['abc', 'abcd']

    data = {'abc': 'password:password', 'abcd': 'password', 'password': 'secret'}
    expected_keys = set(['abc', 'abcd'])
    expected_keys.update('{0}:******'.format(no_log_string) for no_log_string in no_log_strings)
    expected_value = {key: value for key, value in data.items() if key in ignore_keys}
    expected_value.update({key: '******' for key in expected_keys})

    new_data = san

# Generated at 2022-06-12 23:34:46.157155
# Unit test for function set_fallbacks
def test_set_fallbacks():
    argument_spec = {'first_param': {'type': 'str', 'fallback': ('env_fallback', 'FIRST_PARAM')},
                     'second_param': {'type': 'str', 'fallback': ('missing_fallback', )},
                     'third_param': {'type': 'str', 'fallback': ('env_fallback', 'THIRD_PARAM', {'required': True})}}
    parameters = {}
    no_log_values = set()
    no_log_values = set_fallbacks(argument_spec, parameters)
    if not parameters:
        raise AssertionError("Parameters are not set!")
    if parameters.get('first_param') != 'FIRST_PARAM':
        raise AssertionError("Parameter is not set or set incorrectly!")

# Generated at 2022-06-12 23:35:17.719358
# Unit test for function set_fallbacks
def test_set_fallbacks():
    env_string = 'ANSIBLE_TEST_MODULE_UTILS_ARGS_DEFAULT_STRING'
    env_int = 'ANSIBLE_TEST_MODULE_UTILS_ARGS_DEFAULT_INT'
    env_float = 'ANSIBLE_TEST_MODULE_UTILS_ARGS_DEFAULT_FLOAT'
    env_bool = 'ANSIBLE_TEST_MODULE_UTILS_ARGS_DEFAULT_BOOL'
    env_none = 'ANSIBLE_TEST_MODULE_UTILS_ARGS_DEFAULT_NONE'
    env_dict = 'ANSIBLE_TEST_MODULE_UTILS_ARGS_DEFAULT_DICT'
    env_list = 'ANSIBLE_TEST_MODULE_UTILS_ARGS_DEFAULT_LIST'
    env_json

# Generated at 2022-06-12 23:35:28.310031
# Unit test for function set_fallbacks
def test_set_fallbacks():
    spec = {'a': {'type': 'str', 'fallback': (env_fallback, 'A')}}
    params = {}
    no_log_values = set_fallbacks(spec, params)
    assert params['a'] == os.environ['A']
    assert no_log_values == set()

    spec = {'a': {'type': 'str', 'fallback': (env_fallback, ('B', 'C'))}}
    params = {}
    no_log_values = set_fallbacks(spec, params)
    assert params['a'] == os.environ['B']
    assert params['a'] == os.environ['C']
    assert no_log_values == set()


# Generated at 2022-06-12 23:35:36.620831
# Unit test for function env_fallback
def test_env_fallback():
    # Expected behaviour:
    # env_fallback()          => raises AnsibleFallbackNotFound
    # env_fallback(a, b, c)   => raises AnsibleFallbackNotFound
    # env_fallback('a')       => raises AnsibleFallbackNotFound
    # env_fallback('a', 'b')  => raises AnsibleFallbackNotFound
    # env_fallback('a', 'b', 'c') => raises AnsibleFallbackNotFound
    assert_raises(AnsibleFallbackNotFound, env_fallback)
    assert_raises(AnsibleFallbackNotFound, env_fallback, 'a', 'b', 'c')

    original_env_var_a = os.environ.get('a')
    original_env_var_b = os.environ.get('b')


# Generated at 2022-06-12 23:35:46.946521
# Unit test for function set_fallbacks
def test_set_fallbacks():
    options = {'mypassword': 'V3ryS3cr3t'}
    argument_spec = {
        'mypassword': {'required': True, 'type': 'str', 'no_log': True},
    }
    result = set_fallbacks(argument_spec, options)
    assert result == set([])

    options = {'mypassword': 'V3ryS3cr3t'}
    argument_spec = {
        'mypassword': {'required': True, 'type': 'str', 'no_log': True, 'fallback': (env_fallback, 'ANSIBLE_MYPASSWORD')},
    }
    result = set_fallbacks(argument_spec, options)
    assert result == set(['V3ryS3cr3t'])


# Generated at 2022-06-12 23:35:53.728138
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['TEST_FOO_BAR'] = 'test value'
    assert env_fallback('TEST_FOO_BAR') == 'test value'
    assert env_fallback('TEST_UNSET_BAR') == NOT_SET
    os.environ.pop('TEST_FOO_BAR')


# Generated at 2022-06-12 23:35:59.301347
# Unit test for function remove_values
def test_remove_values():
    # Test string types
    assert remove_values('some_string', ['some_string']) == ''
    assert remove_values('some_string', ['some_string', 'other_string']) == ''
    assert remove_values('some_other_string', ['some_string', 'other_string']) == ''
    assert remove_values('some_string', ['some_other_string', 'other_string', 'test']) == 'some_string'
    assert remove_values('some_other_string', ['some_string', 'test', 'hello']) == 'some_other_string'

    # Test non-string types
    assert remove_values(1, ['some_string']) == 1
    assert remove_values(100.00, ['a', 'b']) == 100.00

# Generated at 2022-06-12 23:36:04.366486
# Unit test for function set_fallbacks
def test_set_fallbacks():
    parameters = {}
    argument_spec = dict(
        a=dict(type='str', fallback=(env_fallback, 'A')),
        b=dict(type='str', fallback=(env_fallback, 'B')),
    )
    os.environ['A'] = 'VALUE'
    try:
        set_fallbacks(argument_spec, parameters)
        assert parameters == dict(
            a='VALUE',
            b=None,
        )
    finally:
        del os.environ['A']



# Generated at 2022-06-12 23:36:14.609424
# Unit test for function remove_values
def test_remove_values():
    from collections import OrderedDict

    values = OrderedDict([
        ('string', 'string with a password'),
        ('list', ['string with a password', 'another string with a password']),
        ('dict_string', {'string': 'string with a password', 'another string': 'another string with a password'}),
        ('dict_list', {'string': ['string with a password', 'another string with a password']}),
        ('tuple', ('string with a password', 'another string with a password')),
        ('dict_tuple', {'string': ('string with a password', 'another string with a password')}),
        ('set', {'string with a password', 'another string with a password'})
    ])

# Generated at 2022-06-12 23:36:23.733453
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = {
        'one': {
            'type': 'str',
            'fallback': (env_fallback, ['ONE'], {'type': 'str'})
        },
        'two': {
            'type': 'str',
            'fallback': (env_fallback, ['TWO'], {'type': 'str'})
        },
        'three': {
            'type': 'dict',
            'fallback': (env_fallback, ['THREE'], {'type': 'dict'})
        }
    }

    parameters = {
        'one': None,
        'two': None,
        'three': {
            'four': None
        }
    }

    fallback_parameters = copy.deepcopy(parameters)

# Generated at 2022-06-12 23:36:28.246825
# Unit test for function sanitize_keys
def test_sanitize_keys():
    data = dict(a=dict(b=dict(c='d', my_secret='secret', _ansible_no_log='true', p='@@@@', this_part_is_ok=dict(and_this_part='too', _ansible_no_log='true'))))
    data.update(dict(ansible_facts=dict(some_fact='some_data'), ansible_env=dict(HOME='/home/some_user')))

    sanitized = sanitize_keys(data, no_log_strings=dict(secret='', token=''))
    assert 'my_secret' not in sanitized['a']['b']
    assert '_ansible_no_log' not in sanitized['a']['b']['this_part_is_ok']
    assert 'and_this_part' in sanitized

# Generated at 2022-06-12 23:37:04.216159
# Unit test for function sanitize_keys
def test_sanitize_keys():

    # Simple data structure that contains a single unicode string
    obj1 = {u'key1': u'value1', u'key2': u'value2'}
    no_log_strings1 = [u'value1']
    new_obj1 = {u'key1': u'<value redacted>', u'key2': u'value2'}
    assert sanitize_keys(obj1, no_log_strings1) == new_obj1

    # Simple data structure that contains a single byte string
    obj2 = {'key1': 'value1', 'key2': 'value2'}
    no_log_strings2 = ['value1']
    new_obj2 = {'key1': '<value redacted>', 'key2': 'value2'}

# Generated at 2022-06-12 23:37:10.734800
# Unit test for function set_fallbacks
def test_set_fallbacks():

    argument_spec = {'my_dict': {'fallback': (env_fallback, ['my_dict_var']), 'type': 'dict', 'options': {'username': {'type': 'str'},
                                                                                                      'password': {'type': 'str', 'no_log': True}}}}
    parameters = {}
    os.environ['my_dict_var'] = '{"username": "admin"}'
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert no_log_values == set()
    assert parameters.get('my_dict') == {"username": "admin"}



# Generated at 2022-06-12 23:37:18.296998
# Unit test for function env_fallback
def test_env_fallback():
    ''' test env_fallback function '''
    # setup
    os.environ['_ANSIBLE_TEST_VAR'] = 'sub'
    # run
    try:
        retval = env_fallback('sub', 'subsub', 'subsubsub')
    except AnsibleFallbackNotFound:
        retval = 'subsubsubsub'
    assert retval == 'sub'

    # cleanup
    del os.environ['_ANSIBLE_TEST_VAR']



# Generated at 2022-06-12 23:37:26.769369
# Unit test for function set_fallbacks
def test_set_fallbacks():
    result = set_fallbacks({'foo': {'type': 'dict', 'fallback': [env_fallback, 'foo']},
                            'bar': {'type': 'dict', 'fallback': [env_fallback, 'bar']}}, {})
    assert not result
    assert 'foo' not in os.environ
    assert 'bar' not in os.environ
    os.environ['foo'] = '{"foo": "bar"}'
    result = set_fallbacks({'foo': {'type': 'dict', 'fallback': [env_fallback, 'foo']},
                            'bar': {'type': 'dict', 'fallback': [env_fallback, 'bar']}}, {})
    assert {'{"foo": "bar"}'} == result

# Generated at 2022-06-12 23:37:30.058648
# Unit test for function env_fallback
def test_env_fallback():
    os.environ['test_env_fallback'] = '1'
    assert env_fallback('test_env_fallback') == '1'
    del os.environ['test_env_fallback']



# Generated at 2022-06-12 23:37:40.543141
# Unit test for function set_fallbacks
def test_set_fallbacks():

    arguments = {'test': {'type': 'str', 'fallback': (env_fallback, 'TEST_ENV_VAR')}, 'fail': {'type': 'str', 'fallback': (env_fallback, 'FAIL_ENV_VAR')}}
    test_dict = {}
    with set_environment_variable('TEST_ENV_VAR', 'fallback value'):
        no_log_values = set_fallbacks(arguments, test_dict)

    assert len(no_log_values) == 0
    assert 'test' in test_dict
    assert test_dict['test'] == 'fallback value'
    assert 'fail' not in test_dict

    test_dict = {'test': 'test value'}