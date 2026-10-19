

# Generated at 2022-06-22 11:19:21.573394
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_instance = _DeprecatedSequenceConstant([1, 2, 3], "This is a deprecation warning", version="2.8")
    assert len(test_instance) == 3

# Generated at 2022-06-22 11:19:26.326682
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], "", "2.9")) == 0
    assert len(_DeprecatedSequenceConstant(['a'], "", "2.9")) == 1
    #assert len(_DeprecatedSequenceConstant([1,2,3], "", "2.9")) == 3

# Generated at 2022-06-22 11:19:30.424974
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    """test for method __len__ of class _DeprecatedSequenceConstant"""
    dsc = _DeprecatedSequenceConstant('aaa', 'msg', 'version')
    assert len(dsc) == 3

    dsc = _DeprecatedSequenceConstant(['a', 'c', 'b'], 'msg', 'version')
    assert len(dsc) == 3


# Generated at 2022-06-22 11:19:37.390655
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    l = [0, 1, 2, 3, 4, 5]
    dsc = _DeprecatedSequenceConstant(l, "test warning", "test version")
    assert len(dsc) == len(l)
    dsc.__warning_version__ = None
    assert len(dsc) == len(l)
    dsc.__warning_version__ = ''
    assert len(dsc) == len(l)

# Generated at 2022-06-22 11:19:48.807241
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():

    # create a new constant using the constructor
    x = _DeprecatedSequenceConstant(1, 'a', 'b')

    # check that the value of the constant is the same as the value passed to the constructor
    assert x._value == 1

    # check that the version is the same as the version passed in the constructor
    assert x._version == 'b'

    # check that the length of the sequence constant is 1
    assert len(x) == 1

    # make sure that when we access the value at index 0, it returns the same value
    assert x[0] == 1

# This function is used in tests/unit/module_utils/test_loader.py.
# This function is needed to test the results of a call to get_deprecation_warnings.
# Since we do not want to raise a warning in tests, we raise a ValueError

# Generated at 2022-06-22 11:20:01.194981
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.config.manager import _get_deprecated_msg

    CONSTANT_NAME = "TEST_CONSTANT"
    CONSTANT_VERSION = "2.1"

    def _get_constant_value_repr(value):
        return str(value)

    default_value = (1,)
    deprecated_value = (1, 2)

    # Here we should not do anything special
    assert deprecated_value[0] == 1

    deprecated_constant = _DeprecatedSequenceConstant(default_value, _get_deprecated_msg(
        deprecated_value, CONSTANT_NAME, CONSTANT_VERSION, _get_constant_value_repr), CONSTANT_VERSION)

    # Here we should not do anything special as well
    # i.e. deprecated_constant[0] != deprecated

# Generated at 2022-06-22 11:20:02.184450
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('name', 'value', export=export)
    assert export.get('name') == 'value'

# Generated at 2022-06-22 11:20:04.621108
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant([1, 2, 3], '', '')
    assert len(c) == 3


# Generated at 2022-06-22 11:20:11.261147
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    for item in ('', 'hello', 'hi there!'):
        assert len(_DeprecatedSequenceConstant(item, 'message', 'version')) == len(item)
        assert len(_DeprecatedSequenceConstant([item], 'message', 'version')) == len([item])
        # FIXME: DeprecatedSequenceConstant should accept other types of items that are not Strings and Lists



# Generated at 2022-06-22 11:20:14.412019
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_VAR', 'my-value')
    assert(TEST_VAR == 'my-value')

# Generated at 2022-06-22 11:20:21.112651
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant(['123', '456'], "msg", "version")
    assert len(constant) == 2
    assert constant[0] == '123'
    assert constant[1] == '456'
    assert constant._msg == "msg"
    assert constant._version == "version"

# Generated at 2022-06-22 11:20:26.002620
# Unit test for function set_constant
def test_set_constant():
    ''' returns True if set_constant correctly sets constants '''
    test_dict = {}
    set_constant('FOO', 'BAR', test_dict)
    if test_dict['FOO'] != 'BAR':
        return False
    return True


# Generated at 2022-06-22 11:20:28.746345
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    c = _DeprecatedSequenceConstant((1, 2), "message", "version")
    assert(len(c) == 2)
    assert(c[1] == 2)

# Generated at 2022-06-22 11:20:37.646248
# Unit test for function set_constant
def test_set_constant():
    constants = {}
    set_constant('TEST', True, constants)
    assert constants['TEST'] is True

LOCALHOST_WARNING = '''
                    DEPRECATED: the LOCALHOST constant is deprecated and will be removed in a later version.
                    This constant is the same as 'localhost' and should be used in place of LOCALHOST.
                    '''

_deprecated(LOCALHOST_WARNING, '2.11')



# Generated at 2022-06-22 11:20:49.951292
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dict_test = dict(version='2.9', msg='test message')

    # test with int
    sequence_constant = _DeprecatedSequenceConstant(dict_test, dict_test['msg'], '2.9')
    assert sequence_constant.__getitem__(1) == dict_test[1]

    # test with float
    sequence_constant = _DeprecatedSequenceConstant(dict_test, dict_test['msg'], '2.9')
    assert sequence_constant.__getitem__(1.0) == dict_test[1]

    # test with slice
    sequence_constant = _DeprecatedSequenceConstant(dict_test, dict_test['msg'], '2.9')

# Generated at 2022-06-22 11:20:54.468227
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # create a _DeprecatedSequenceConstant object
    test_obj = _DeprecatedSequenceConstant(range(5), "test message", "3.0")
    # use __len__() to get the length of the object
    len(test_obj)



# Generated at 2022-06-22 11:20:57.117155
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = 'this is a test'
    version = '2.9'
    _DeprecatedSequenceConstant(value='', msg=msg, version=version).__len__()


# Generated at 2022-06-22 11:21:03.137948
# Unit test for function set_constant
def test_set_constant():
    test_vars = {}
    test_name = 'ANSIBLE_TEST_CONSTANT'
    test_value = 'test'
    set_constant(test_name, test_value, test_vars)
    assert test_name in test_vars
    assert test_vars[test_name] == test_value


# Generated at 2022-06-22 11:21:05.590655
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar', export=globals())
    assert globals()['foo'] == 'bar'


# Generated at 2022-06-22 11:21:07.672661
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    expected = ('test', )
    got = _DeprecatedSequenceConstant(expected, 'test', '2.9')[0]
    assert got == expected

# Generated at 2022-06-22 11:21:15.283639
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant((), '', '')
    assert len(constant) == 0



# Generated at 2022-06-22 11:21:17.544997
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a = _DeprecatedSequenceConstant([1,2], "msg", "version")
    assert len(a) == 2


# Generated at 2022-06-22 11:21:26.880743
# Unit test for function set_constant
def test_set_constant():
    assert C.DEFAULT_MODULE_VERSION != 'unset'

# Set built-in constants
set_constant('DEFAULT_ASK_SUDO_PASS', DEFAULT_BECOME_PASS)
set_constant('DEFAULT_ASK_SSH_PASS', DEFAULT_REMOTE_PASS)
set_constant('DEFAULT_SUDO_PASS', DEFAULT_BECOME_PASS)
set_constant('DEFAULT_SUBSET', DEFAULT_SUBSET)
set_constant('DEFAULT_VAULT_PASSWORD_FILE', None)
set_constant('DEFAULT_BECOME_PASS', DEFAULT_BECOME_PASS)
set_constant('DEFAULT_PASSWORD_CHARS', DEFAULT_PASSWORD_CHARS)

# Generated at 2022-06-22 11:21:30.100720
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    l = [1, 2, 3]
    dsc = _DeprecatedSequenceConstant(l, "", "")
    assert len(dsc) == len(l)



# Generated at 2022-06-22 11:21:31.907814
# Unit test for function set_constant
def test_set_constant():
    set_constant('a_test', 42, {})
    assert 'a_test' in globals()
    assert 42 == globals()['a_test']



# Generated at 2022-06-22 11:21:35.072891
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(value=[1, 2, 3], msg='msg', version='version')) == 3


# Generated at 2022-06-22 11:21:39.100049
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "YAML_OUTPUT is deprecated"
    version = "2.10"
    x = _DeprecatedSequenceConstant(YAML_OUTPUT, msg, version)
    assert len(x) == 2
    assert "default" in x
    assert "smart" in x

del config, setting

# Generated at 2022-06-22 11:21:41.257904
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    thing = _DeprecatedSequenceConstant('123', None, None)
    assert '1' == thing[1]

# Generated at 2022-06-22 11:21:51.256290
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'deprecated message'
    version = '2.12'
    testdeprecated = _DeprecatedSequenceConstant([1, 2, 3], msg, version)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)
    len(testdeprecated)

# Generated at 2022-06-22 11:22:01.148875
# Unit test for function set_constant
def test_set_constant():
    ''' set_constant() output should be equal to the value of the
    corresponding setting '''
    assert action_extra_args == config.data.get_setting('action_extra_args').value

# Module constants that are overridden by config
BECOME_PASS = DEFAULT_BECOME_PASS
DEFAULT_REMOTE_USER = 'default'
DEFAULT_SUBSET = None

# Module constant that are overridden by config and should be read-only
READ_ONLY_VARS = frozenset(MAGIC_VARIABLE_MAPPING.keys())

# Module constants that are overridden by config but are not read-only
WRITABLE_VARS = frozenset(('BECOME_PASS', 'DEFAULT_REMOTE_USER'))

# LEGACY CONSTANTS ###

# ANS

# Generated at 2022-06-22 11:22:16.278806
# Unit test for function set_constant
def test_set_constant():
    from unit.mock import Mock

    def test_function(name, value, export):
        export[name] = value

    mock = Mock(side_effect=test_function)
    old_set_constant = set_constant
    set_constant = mock

    config.define('test.test1', default=False, type='bool', constant=True)
    config.define('test.test2', default=1, type='int', constant=True)
    config.define('test.test3', default="default_string", type='str', constant=True)
    config.define('test.test4', default=["default_string"], type='list', constant=True)
    config.define('test.test5', default={"default_key": "default_string"},
                  type='dict', constant=True)

    config.define

# Generated at 2022-06-22 11:22:22.689681
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'Deprecated, to be removed in Ansible 2.10.'
    dep = _DeprecatedSequenceConstant([1, 2, 3], msg, '2.10')
    result = dep.__len__()
    assert result == 3
    result = dep.__getitem__(0)
    assert result == 1
    result = dep.__getitem__(1)
    assert result == 2
    result = dep.__getitem__(2)
    assert result == 3


# Generated at 2022-06-22 11:22:26.100541
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'test_msg'
    version = 'test_version'
    value = ('test_value', )
    c = _DeprecatedSequenceConstant(value, msg, version)
    assert len(c) == 1

# Generated at 2022-06-22 11:22:31.379702
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_value = (1, 2, 3)
    test_msg = 'test message'
    test_version = 'test version'
    test_object = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert len(test_object) == len(test_value)


# Generated at 2022-06-22 11:22:36.057525
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dsc = _DeprecatedSequenceConstant(["one", "two", "three"],
        "deprecated message", "321.0")

    assert len(dsc) == 3
    assert dsc[0] == "one"
    assert dsc[1] == "two"
    assert dsc[2] == "three"


# Generated at 2022-06-22 11:22:47.117610
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test that the method __len__ is able to count the number of elements of the variable value
    msg1 = "test message"
    version1 = "2.0"
    value1 = ["value1", "value2"]
    deprecatedSequenceConstant1 = _DeprecatedSequenceConstant(value1, msg1, version1)
    assert len(deprecatedSequenceConstant1) == 2

    msg2 = "test message"
    version2 = "2.0"
    value2 = ["value1", "value2", "value3"]
    deprecatedSequenceConstant2 = _DeprecatedSequenceConstant(value2, msg2, version2)
    assert len(deprecatedSequenceConstant2) == 3

    msg3 = "test message"
    version3 = "2.0"

# Generated at 2022-06-22 11:22:51.640380
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant(['foo', 'bar'], 'Message', '2.10.0')
    assert constant[0] == ['foo', 'bar']
    assert constant[1] == ['foo', 'bar']



# Generated at 2022-06-22 11:23:02.079701
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.module_utils.common.collections import Sequence
    class Test(Sequence):
        def __init__(self, value):
            self._value = value

        def __len__(self):
            return len(self._value)

        def __getitem__(self, y):
            return self._value[y]

    assert Test(('a', 'b'))[0] == 'a'
    assert Test(('a', 'b'))[1] == 'b'
    try:
        assert Test(('a', 'b'))[2] == None
        assert False, 'should fail'
    except IndexError:
        pass

# Generated at 2022-06-22 11:23:04.193708
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(value=[], msg="msg", version="version")) == 0


# Generated at 2022-06-22 11:23:15.327605
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Test with a tuple
    test_value = ('test_value1', 'test_value2')
    test_message = 'This is a test message'
    test_version = 'Test 2.0'
    test_object = _DeprecatedSequenceConstant(test_value, test_message, test_version)
    assert test_object._value == test_value
    assert test_object._msg == test_message
    assert test_object._version == test_version
    assert len(test_object) == 2
    assert test_object[0] == test_value[0]
    assert test_object[1] == test_value[1]
    # Test with a list
    test_value2 = ['test_value1', 'test_value2']
    test_message2 = 'This is another test message'
    test_version

# Generated at 2022-06-22 11:23:30.450025
# Unit test for function set_constant
def test_set_constant():
    # Clear the export
    export = {}
    # Test setting a variable
    set_constant('TEST', True, export)
    assert 'TEST' in export
    assert export['TEST'] is True

# Generated at 2022-06-22 11:23:36.187803
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    new = _DeprecatedSequenceConstant(('test',), 'msg', 'version')
    assert len(new) == 1
    assert new[0] == 'test'

try:
    import __main__
    __main__.__dict__['__requires__'] = add_internal_fqcns(('ansible_base', ))
except Exception:
    pass

# Generated at 2022-06-22 11:23:38.167023
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    obj = _DeprecatedSequenceConstant([1, 2, 3], 'Test constant', '2.12')
    assert len(obj) == 3

# Generated at 2022-06-22 11:23:42.374546
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    a = (1, 2, 3, 4)
    test = _DeprecatedSequenceConstant(value=a, msg=u'This is a test', version=u'2.9')
    assert test.__getitem__(1) == 2
    assert test[1] == 2


# Generated at 2022-06-22 11:23:49.366759
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(None, "warn_message", "version")) == 0
    assert len(_DeprecatedSequenceConstant([1, 2, 3], "warn_message", "version")) == 3
    assert len(_DeprecatedSequenceConstant((1, 2, 3), "warn_message", "version")) == 3
    assert len(_DeprecatedSequenceConstant({'a': 1}, "warn_message", "version")) == 1
    assert len(_DeprecatedSequenceConstant({'a': 1, 'b': 2, 'c': 3}, "warn_message", "version")) == 3


# Generated at 2022-06-22 11:23:58.922904
# Unit test for function set_constant
def test_set_constant():
    # Test for integer
    set_constant('TESTING_FOR_INTEGER', 5)
    assert TESTING_FOR_INTEGER == 5

    # Test for float
    set_constant('TESTING_FOR_FLOAT', 5.1)
    assert TESTING_FOR_FLOAT == 5.1

    # Test for boolean
    set_constant('TESTING_FOR_BOOLEAN', True)
    assert TESTING_FOR_BOOLEAN is True

    # Test for None
    set_constant('TESTING_FOR_NONE', None)
    assert TESTING_FOR_NONE is None

    # Test for string
    set_constant('TESTING_FOR_STRING', "Hello")
    assert TESTING_FOR_STRING == "Hello"

    # Test for

# Generated at 2022-06-22 11:24:01.275049
# Unit test for function set_constant
def test_set_constant():
    constants = {}
    set_constant('foo', 'bar', export=constants)
    assert 'foo' in constants
    assert constants['foo'] == 'bar'


# Generated at 2022-06-22 11:24:04.391343
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant(['localhost'], 'msg', 'version')
    assert constant[0] == 'localhost'
    constant.__len__() == 1


# Generated at 2022-06-22 11:24:09.986508
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    test_obj = _DeprecatedSequenceConstant((1, 2, 3, 4), 'msg', 'version')
    assert test_obj[0] == 1
    assert test_obj[3] == 4
    assert_raises(IndexError, lambda: test_obj[-5])
    assert_raises(IndexError, lambda: test_obj[5])
    assert_raises(KeyError, lambda: test_obj['a'])



# Generated at 2022-06-22 11:24:15.259600
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant(('a', 'b', 'c'), None, None)[0] == 'a'
    assert _DeprecatedSequenceConstant(('a', 'b', 'c'), None, None)[0][0] == 'a'


# Generated at 2022-06-22 11:24:53.605210
# Unit test for function set_constant
def test_set_constant():
    DUMMY_NAME = '__ANSIBLE_TESTING_DUMMY_NAME__'
    DUMMY_VALUE = '__ANSIBLE_TESTING_DUMMY_VALUE__'
    try:
        set_constant(DUMMY_NAME, DUMMY_VALUE)
        assert globals()[DUMMY_NAME] == DUMMY_VALUE
        del globals()[DUMMY_NAME]
    except AssertionError:
        raise Exception('set_constant() did not create a constant even though I asked it to')
    except KeyError:
        raise Exception('set_constant() did not create a constant even though I asked it to')

# Generated at 2022-06-22 11:25:01.662672
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    def _test__DeprecatedSequenceConstant___getitem__():
        import sys
        _saved_stderr = sys.stderr
        sys.stderr = Tempfile()

# Generated at 2022-06-22 11:25:02.690302
# Unit test for function set_constant
def test_set_constant():
    set_constant('MY_SETTING', 'value')
    assert MY_SETTING == 'value'



# Generated at 2022-06-22 11:25:06.213050
# Unit test for method __len__ of class _DeprecatedSequenceConstant

# Generated at 2022-06-22 11:25:08.951440
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    orig = [1, 2, 3]
    new = _DeprecatedSequenceConstant(origin,
                                      "msg",
                                      "version")
    assert new.__len__() == orig.__len__()


# Generated at 2022-06-22 11:25:17.796562
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    cls = _DeprecatedSequenceConstant([True], '', '')
    assert cls[0] is True
    cls = _DeprecatedSequenceConstant((True,), '', '')
    assert cls[0] is True
    cls = _DeprecatedSequenceConstant("abc", '', '')
    assert cls[0] == 'a'
    cls = _DeprecatedSequenceConstant(123, '', '')
    with pytest.raises(TypeError) as excinfo:
        cls[0]
    assert 'object does not support indexing' in str(excinfo.value)


# Generated at 2022-06-22 11:25:19.726090
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant(['one', 'two'], 'Test warning message', '2.10')[0] == 'one'


# Generated at 2022-06-22 11:25:23.803833
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # test1
    msg = 'some message'
    version = 'someversion'
    sequence = ['a', 'b']
    constant = _DeprecatedSequenceConstant(sequence, msg, version)

    assert len(constant) == len(sequence)
    assert constant[0] == sequence[0]
    assert constant[1] == sequence[1]

# Generated at 2022-06-22 11:25:35.248814
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Positive test cases
    # In case of int:
    dsc = _DeprecatedSequenceConstant([0,1,1,2,3], 'int', '1.0')
    assert dsc[0] == 0
    # In case of string
    dsc = _DeprecatedSequenceConstant(['a', 'b', 'b', 'c'], 'string', '1.0')
    assert dsc[0] == 'a'
    # In case of float
    dsc = _DeprecatedSequenceConstant([0.4, 3.2, 5.3], 'float', '1.0')
    assert dsc[0] == 0.4
    # In case of lists

# Generated at 2022-06-22 11:25:37.501279
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant([], '', '2.12')

# Generated at 2022-06-22 11:26:58.918700
# Unit test for function set_constant
def test_set_constant():
    # We want to make sure that the function successfully sets a constant
    # and that it is working correctly
    initial_constant = getattr(__builtin__, 'TEST_CONSTANT', None)
    set_constant('TEST_CONSTANT', 'new_test_constant')
    assert getattr(__builtin__, 'TEST_CONSTANT') == 'new_test_constant'
    # Clean up the mess we created
    if initial_constant is None:
        delattr(__builtin__, 'TEST_CONSTANT')
    else:
        set_constant('TEST_CONSTANT', initial_constant)

# Generated at 2022-06-22 11:27:08.332503
# Unit test for function set_constant
def test_set_constant():
    '''
    Test the set_constant() function by picking a random one
    from our current set of constants.
    '''
    from random import choice
    from sys import modules as sys_modules
    import ansible
    if ansible.__version__.startswith('devel'):
        # This can't be tested during development until we move the constants
        # into the config manager
        return

    # Pick a random constant to test
    choice = choice(list(locals()))
    # Ensure we pick a constant that will be defined in __main__
    if choice.startswith('_') or choice == 'test_set_constant':
        choice = choice('INTERNAL_RESULT_KEYS')
    # Set the constant
    set_constant(choice, 'foo')
    # Test that the constant was defined in __

# Generated at 2022-06-22 11:27:13.346995
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test for type 'list'
    sequence = _DeprecatedSequenceConstant(['alpha', 'beta'], 'test message', 'test version')
    assert len(sequence) == 2
    # Test for type 'tuple'
    sequence = _DeprecatedSequenceConstant(('alpha', 'beta'), 'test message', 'test version')
    assert len(sequence) == 2

# Generated at 2022-06-22 11:27:25.000025
# Unit test for function set_constant
def test_set_constant():
    set_constant("NEW_CONSTANT", 42, export=vars())
    assert NEW_CONSTANT == 42


# CONSTANTS WHICH NEED OTHER CONSTANTS TO BE DEFINED

MAGIC_VARIABLE_MAPPING['ssh_args'] = tuple(['ansible_' + x + '_args' for x in ('ssh', 'sftp', 'scp', 'ssh_transfer_method')])


# Generated at 2022-06-22 11:27:29.927058
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "This is a test warning"
    version = "2.9"
    value = [1, 2]
    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert dsc._value == value
    assert dsc._msg == msg
    assert dsc._version == version
    assert len(dsc) == len(value)
    assert dsc[0] == value[0]

# Generated at 2022-06-22 11:27:33.880574
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    x = _DeprecatedSequenceConstant(['a', 'b', 'c', 'd'], 'MSG', '2.9')
    assert len(x) == 4


# Generated at 2022-06-22 11:27:36.695282
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar')
    assert foo == 'bar'

# Generated at 2022-06-22 11:27:40.618242
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    data_list = ['foo', 'bar', 'baz']
    instance = _DeprecatedSequenceConstant(data_list, 'This is a message', '1.2.3')
    assert len(instance) == 3
    assert len(instance) == len(data_list)


# Generated at 2022-06-22 11:27:44.779422
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test with valid sequence
    co = _DeprecatedSequenceConstant(value=[1, 2, 3], msg="test", version="2.12")
    assert len(co) == 3

    # Test with invalid sequence
    co = _DeprecatedSequenceConstant(value=None, msg="test", version="2.12")
    assert len(co) == 0


# Generated at 2022-06-22 11:27:48.417448
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant('value', 'msg', 'version')
    # Constant __len__ value, https://github.com/python/cpython/blob/a9e6eef1196a98cda480bac6d85c764061b9df94/Lib/collections/__init__.py#L122-L123
    assert len(constant) == 5