

# Generated at 2022-06-22 11:19:20.474182
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], '', '')) == 0

# Generated at 2022-06-22 11:19:23.395958
# Unit test for function set_constant
def test_set_constant():
    set_constant('test_constant', 15)
    assert test_constant == 15

# Generated at 2022-06-22 11:19:33.460787
# Unit test for function set_constant
def test_set_constant():
    set_constant('_TEST_CONSTANT1', 'bar', export=globals())
    assert _TEST_CONSTANT1 == 'bar'


# DEPRECATED CONSTANTS ###

# The following are constants whose use should be deprecated in favor of the standard
#   constants above
_DONT_USE_AS_FLAGS_REQUIRE_VARIABLE = add_internal_fqcns(('freeze_variables', 'no_log', 'run_once', 'new_vault_password_file'))

# Generated at 2022-06-22 11:19:41.913390
# Unit test for function set_constant
def test_set_constant():
    import os
    import tempfile

    c = """
[defaults]
foo = bar
"""

    fd, path = tempfile.mkstemp()
    try:
        os.write(fd, c.encode('utf-8'))
        os.close(fd)
        cfg = ConfigManager(path)
        # Verify that value is a string and available under different name
        assert cfg.data.defaults.foo == 'bar'
    finally:
        os.unlink(path)

# Generated at 2022-06-22 11:19:45.749306
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant(['a', 'b'], 'test', '2.9')
    assert len(c) == 2

test__DeprecatedSequenceConstant___len__()


# Generated at 2022-06-22 11:19:57.966304
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    message = ''
    msg = 'Test will fail.'
    version = '3.3'
    # test with list object
    test_value = []
    test_object = _DeprecatedSequenceConstant(test_value, msg, version)
    test_object.__getitem__(0)
    message += _DeprecatedSequenceConstant.__getitem__.__doc__
    # test with string object
    test_value = 'test'
    test_object = _DeprecatedSequenceConstant(test_value, msg, version)
    test_object.__getitem__(0)
    message += _DeprecatedSequenceConstant.__getitem__.__doc__
    # test with dict object
    test_value = {}
    test_object = _DeprecatedSequenceConstant(test_value, msg, version)


# Generated at 2022-06-22 11:20:10.132938
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test = _DeprecatedSequenceConstant(value=[1,2,3], msg="This test is deprecated", version="2.5")
    if isinstance(test, Sequence):
        pass
    else:
        raise Exception("Failed to construct an object of _DeprecatedSequenceConstant class")

# Generate more constants
ARCHIVE_FORMATS = frozenset(("tar", "zip", "gztar", "bzip2", "xz"))
ALLOWED_INCLUDE_EXTS = frozenset(('.yml', '.yaml', '.json', '.py'))

ACP_PASSWD = ACP_PASSWD_ARGS = ACP_SU_ARGS = ANSIBLE_FORCE_COLOR = ANSIBLE_HOST_KEY_CHECKING = ANSIBLE_NOCOWS = ANSIBLE_RETRY_

# Generated at 2022-06-22 11:20:13.629594
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([1, 2, 3], 'msg', 'ver')) == 3

# Generated at 2022-06-22 11:20:18.279907
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    class_ = _DeprecatedSequenceConstant(('foo', 'bar'), 'This warning', '3')
    len_ = len(class_)
    assert len_ == 2


# Generated at 2022-06-22 11:20:25.913798
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dsc = _DeprecatedSequenceConstant(("a","b","c"), 'testing 123', '2.9')
    assert dsc[0] == "a", "_DeprecatedSequenceConstant[0] not 'a'"
    assert dsc[1] == "b", "_DeprecatedSequenceConstant[1] not 'b'"
    assert dsc[2] == "c", "_DeprecatedSequenceConstant[2] not 'c'"

#
# DEPRECATED METHODS
#
# these methods exist solely for backwards compatibility, and should not be
# used in new code
#

# FIXME: not all of these have been ported to config yet,
#        but we should get all of them out at some point, even
#        if we have to keep this as a separate data structure.

# general
DEFAULT_S

# Generated at 2022-06-22 11:20:37.902205
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert constant[1] == 2, "integer index get failed"
    assert constant[-1] == 3, "negative integer index get failed"
    assert constant[0:2] == [1, 2], "slice index get failed"



# Generated at 2022-06-22 11:20:50.640894
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert isinstance(_DeprecatedSequenceConstant([], "", "2.9"), _DeprecatedSequenceConstant)
    assert _DeprecatedSequenceConstant([], "", "2.9")._msg == ""
    assert _DeprecatedSequenceConstant([], "", "2.9")._value == []
    assert _DeprecatedSequenceConstant([], "", "2.9").__len__() == 0
    assert _DeprecatedSequenceConstant([1, 2, 3], "", "2.9").__getitem__(1) == 2
    assert _DeprecatedSequenceConstant([1, 2, 3], "", "2.9").__len__() == 3
    assert _DeprecatedSequenceConstant([1, 2, 3], "", "2.9") == [1, 2, 3]

# Unit test

# Generated at 2022-06-22 11:20:55.128165
# Unit test for function set_constant
def test_set_constant():
    # test to make sure DEFAULT_HASH_BEHAVIOUR exists
    assert DEFAULT_HASH_BEHAVIOUR
    # make sure False is not an option
    assert 'False' not in DEFAULT_HASH_BEHAVIOUR


# TODO: move to some other common location

# Generated at 2022-06-22 11:20:58.713856
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_data = _DeprecatedSequenceConstant(value=['True'], msg='msg', version='version')
    assert test_data[0] == 'True'

# Generated at 2022-06-22 11:21:09.016694
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_const = _DeprecatedSequenceConstant([1, 2], "test_msg", "test_version")
    assert test_const[0] == 1
    assert len(test_const) == 2


# DEPRECATED OPTIONS ###


# Generated at 2022-06-22 11:21:20.201279
# Unit test for function set_constant
def test_set_constant():
    # test for string
    value1 = 'string_value'
    global ANSIBLE_CONFIG
    ANSIBLE_CONFIG = value1
    assert ANSIBLE_CONFIG == value1

    # test for None
    value2 = None
    ANSIBLE_DEBUG = value2
    assert ANSIBLE_DEBUG == value2

    # test for bool
    value3 = True
    HOST_KEY_CHECKING = value3
    assert HOST_KEY_CHECKING == value3

    # test for list
    value4 = ['string_value', 'other_string_value']
    ANSIBLE_VAULT_PASSWORD_FILE = value4
    assert ANSIBLE_VAULT_PASSWORD_FILE == value4

    # test for dict

# Generated at 2022-06-22 11:21:22.903020
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_object = _DeprecatedSequenceConstant('test_value', 'message', 'version')
    assert test_object[0] == 't'
    assert test_object[1] == 'e'


# Generated at 2022-06-22 11:21:29.746749
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    tests = [
        [1, [1, 2, 3], 'msg', 'version']
    ]
    for test in tests:
        a = test[0]         # len value
        b = test[1]         # initializing value
        c = test[2]         # message
        d = test[3]         # version
        x = _DeprecatedSequenceConstant(b, c, d)
        assert x.__len__() == a

# Generated at 2022-06-22 11:21:33.915032
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value1 = [1,2,3,4]
    msg1 = 'foo'
    version1 = '9.9'
    dep1 = _DeprecatedSequenceConstant(value1, msg1, version1)
    assert (len(dep1) == len(value1))


# Generated at 2022-06-22 11:21:42.498763
# Unit test for function set_constant
def test_set_constant():
    set_constant('ANSIBLE_NEW_CONST', 'hello world')
    assert ANSIBLE_NEW_CONST == 'hello world'


# FIXME: this is here because constants are used in a number of places
# in plugin loading, which happens very early.  Once that logic has
# been moved elsewhere this can go away.
DOCUMENTATION = '''
module: __unknown__
short_description: when used, this will be dynamically replaced by a module
  description
'''

# FIXME: Refactor so this is not needed.
from ansible.module_utils.facts.system import ModuleInfo  # noqa

# Note: this is just a placeholder so the import works, the loader will override this below
#
# FIXME: Refactor so we don't need this

# Generated at 2022-06-22 11:21:59.159352
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    import unittest
    import sys

    class Test__DeprecatedSequenceConstant(unittest.TestCase):
        def test_init(self):
            test_base = _DeprecatedSequenceConstant(['a', 'c', 'b'], 'testing', '2.9')
            self.assertEqual(test_base._value, ['a', 'c', 'b'])
            self.assertEqual(test_base._msg, 'testing')
            self.assertEqual(test_base._version, '2.9')

        def test_len(self):
            test_base = _DeprecatedSequenceConstant(['a', 'c', 'b'], 'testing', '2.9')
            self.assertEqual(len(test_base), 3)

        def test_getitem(self):
            test

# Generated at 2022-06-22 11:22:07.816318
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class FakeDisplay:
        def __init__(self):
            self.warning_called = 0
            self.deprecated_called = 0

        def warning(self, *args, **kwargs):
            self.warning_called += 1

        def deprecated(self, *args, **kwargs):
            self.deprecated_called += 1

    cfg = ConfigManager()
    fake_display = FakeDisplay()
    cfg.display = fake_display

    cfg.data._settings['FOO_BAR'] = dict(key='foo_bar', origin='default', value=['foo', 'bar'], type=list, scope=None)
    dsc = _DeprecatedSequenceConstant(cfg.data._settings['FOO_BAR']['value'], 'msg', '2.9')
    len(dsc)
   

# Generated at 2022-06-22 11:22:10.861045
# Unit test for function set_constant
def test_set_constant():
    set_constant('test_set_constant', 2)
    if not test_set_constant == 2:
        raise Exception("Unable to set constant")
test_set_constant()

# Generated at 2022-06-22 11:22:15.140442
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_value = 'test_value'
    test_msg = 'test_msg'
    test_version = 'test_version'
    test_container = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert(len(test_container) == 1)
    assert(test_container[0] == test_value)

# Generated at 2022-06-22 11:22:19.546694
# Unit test for function set_constant
def test_set_constant():

    set_constant('FOO', 'bar')
    set_constant('BAZ', {'a': 'b'})

    assert FOO == 'bar'
    assert 'BAZ' in globals()
    assert BAZ == {'a': 'b'}

# Generated at 2022-06-22 11:22:29.223573
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class FakeDisplay:
        def __init__(self, version):
            self.WARNINGS = []
            self.version = version

        def deprecated(self, msg, version=my_version):
            self.WARNINGS.append((msg, version))

    # Store the original Display class
    original_Display = Display


# Generated at 2022-06-22 11:22:39.100492
# Unit test for function set_constant
def test_set_constant():
    set_constant(name='FOO', value='BAR')
    assert FOO == 'BAR'


# Generated at 2022-06-22 11:22:42.078433
# Unit test for function set_constant
def test_set_constant():
    # TODO: Enable this for Python 3
    # assert 'DEFAULT_SUBSET' in set(globals())
    assert DEFAULT_SUBSET == 'all'

# Generated at 2022-06-22 11:22:44.941758
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant((), '', '')) == 0
    assert len(_DeprecatedSequenceConstant(('a'), '', '')) == 1


# Generated at 2022-06-22 11:22:53.390397
# Unit test for function set_constant
def test_set_constant():
    # Set global constants
    set_constant('TEST_CONST', True)
    # Check constants were set
    assert TEST_CONST, "TEST_CONST not set"


C.DEFAULT_MODULE_NAME = 'command'
for name in ('DEFAULT_EXECUTABLE', 'DEFAULT_BECOME_EXE', 'DEFAULT_BECOME_METHOD'):
    C[name] = C.get_config(C.p, C.DEFAULT_MODULE_NAME, name, 'ansible-%s' % C[name], value_type='path')

# Generated at 2022-06-22 11:23:08.302744
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    sequence = ['A', 'B', 'C']
    deprecated_sequence_constant = _DeprecatedSequenceConstant(sequence,
                                                               '__getitem__ is deprecated. '
                                                               'It will go away in version 2.11.',
                                                               '2.11')
    assert deprecated_sequence_constant[0] == 'A'
    assert deprecated_sequence_constant[1] == 'B'
    assert deprecated_sequence_constant[2] == 'C'

# Generated at 2022-06-22 11:23:18.302866
# Unit test for function set_constant
def test_set_constant():
    # test both, that existing constants are not overwritten and that new constants are set
    original_value = VALIDATE_CERTS
    new_value = not original_value
    set_constant('VALIDATE_CERTS', new_value)
    assert VALIDATE_CERTS == original_value
    set_constant('TEST_NEW_CONSTANT', new_value)
    assert TEST_NEW_CONSTANT == new_value
    # unset it again
    del globals()['TEST_NEW_CONSTANT']

    # test that constants are set with the resolved value
    import os
    ANSIBLE_LIBRARY_ROOT = "{{ ansible_system_library }}"
    set_constant('ANSIBLE_LIBRARY_ROOT', ANSIBLE_LIBRARY_ROOT)


# Generated at 2022-06-22 11:23:26.674575
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    '''
    We expect the effects of __getitem__ to be returned
    '''
    pre_msg = "This is a test"
    pre_version = "1.0"
    pre_value = ('banana', 'plum', 'pear')
    test_object = _DeprecatedSequenceConstant(pre_value, pre_msg, pre_version)
    assert len(test_object) == len(pre_value)
    assert test_object[0] == pre_value[0]


if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:23:31.327901
# Unit test for function set_constant
def test_set_constant():
    """ set_constant should make constants accessible in the global namespace """

    # Run the function
    set_constant('TEST_CONSTANT', 'foobar')

    # Assert the result
    assert isinstance(TEST_CONSTANT, string_types)
    assert TEST_CONSTANT == 'foobar'

# Generated at 2022-06-22 11:23:35.270008
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = 'foo'
    version = 'bar'
    value = ('baz', 'cat')
    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert(len(dsc) == len(value))


# Generated at 2022-06-22 11:23:38.374408
# Unit test for function set_constant
def test_set_constant():
    constants = []
    set_constant('foo', 'bar', constants)
    set_constant('foo', 'baz', constants)
    assert 'foo' in constants
    assert constants.get('foo') == 'baz'



# Generated at 2022-06-22 11:23:40.987269
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    testobj = _DeprecatedSequenceConstant(['one', 'two'], 'Deprecation warning', '2.12')
    assert testobj[1] == 'two'



# Generated at 2022-06-22 11:23:45.902451
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_list = ['one','two','three','four']
    test_msg = "The message"
    test_version = "The Version"
    test1 = _DeprecatedSequenceConstant(test_list, test_msg, test_version)
    len1 = len(test1)
    assert len1 == len(test_list)


# Generated at 2022-06-22 11:23:48.095485
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_STDOUT_CALLBACK == 'default'
    assert ANSIBLE_RETRY_FILES_ENABLED == True

# Generated at 2022-06-22 11:23:49.863339
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar', export=globals())
    assert globals()['foo'] == 'bar'

# Generated at 2022-06-22 11:24:14.600074
# Unit test for function set_constant
def test_set_constant():
    def func():
        pass
    # set_constant function set function
    set_constant('function', func)
    assert 'function' in vars()
    assert vars()['function'] is func



# Generated at 2022-06-22 11:24:17.896188
# Unit test for function set_constant
def test_set_constant():
    variable = {}
    set_constant('ANSIBLE_TEST_VAR', 'test', variable)
    assert variable['ANSIBLE_TEST_VAR'] == 'test'



# Generated at 2022-06-22 11:24:27.095583
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    obj = _DeprecatedSequenceConstant([], "", "")
    assert isinstance(obj, Sequence)
    assert isinstance(obj._value, list)
    assert isinstance(obj._msg, string_types)
    assert isinstance(obj._version, string_types)

test__DeprecatedSequenceConstant()

if config.get_config_value('DEFAULT_BECOME_PASS'):
    DEFAULT_BECOME_PASS = config.DEFAULT_BECOME_PASS

if config.get_config_value('DEFAULT_PASSWORD_CHARS'):
    DEFAULT_PASSWORD_CHARS = config.DEFAULT_PASSWORD_CHARS

if config.get_config_value('DEFAULT_REMOTE_USER'):
    DEFAULT_REMOTE_USER = config.DEFAULT_

# Generated at 2022-06-22 11:24:38.648837
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_LIBRARY == '~/ansible/library'


# Generated at 2022-06-22 11:24:42.601064
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'test message'
    version = 'test version'
    value = [1, 2, 3, 4]
    a = _DeprecatedSequenceConstant(value, msg, version)
    assert a._value == value
    assert a._msg == msg
    assert a._version == version

# Generated at 2022-06-22 11:24:47.631843
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_array = [1, 2, 3, 4]
    test_msg = 'This is a test for method __getitem__ of _DeprecatedSequenceConstant class'
    test_version = '2022-12-31'
    test_obj = _DeprecatedSequenceConstant(test_array, test_msg, test_version)
    assert test_obj[1] == test_array[1]

# Generated at 2022-06-22 11:24:50.946265
# Unit test for function set_constant
def test_set_constant():
    constants = {}
    set_constant('foo', 'bar', constants)
    set_constant('foo2', ['bar2'], constants)
    assert constants['foo'] == 'bar'
    assert constants['foo2'] == ['bar2']



# Generated at 2022-06-22 11:24:56.178174
# Unit test for function set_constant
def test_set_constant():
    constant_name = 'ANSIBLE_TEST_CONSTANT'
    constant_value = 'test value'
    export = {}
    set_constant(constant_name, constant_value, export=export)
    assert constant_name in export
    assert export[constant_name] == constant_value



# Generated at 2022-06-22 11:24:59.263337
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    class_instance = _DeprecatedSequenceConstant(tuple(), "Test warning", "2.0")
    assert type(class_instance) == _DeprecatedSequenceConstant

# Generated at 2022-06-22 11:25:07.086111
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_msg = 'test_message'
    test_version = 'test_version'
    test_value = [0,1,2,3]
    test_obj = _DeprecatedSequenceConstant(value=test_value, msg=test_msg, version=test_version)
    while True:
        try:
            iter(test_obj)
            break
        except TypeError:
            assert(False)
    assert(len(test_obj) == len(test_value))
    assert(test_obj[0] == test_value[0])

# Generated at 2022-06-22 11:26:06.525330
# Unit test for function set_constant
def test_set_constant():
    '''
    This test will verify that set_constant works as expected
    '''
    set_constant('testing_var', 'testing_var_value')
    assert testing_var == 'testing_var_value'
    return True

# Generated at 2022-06-22 11:26:17.463222
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    import pytest
    with pytest.raises(TypeError):
        # Should throw a "TypeError: parameter msg must be a string"
        dep = _DeprecatedSequenceConstant("test_value", 10, "2.10")
    with pytest.raises(TypeError):
        # Should throw a "TypeError: parameter version must be a string"
        dep = _DeprecatedSequenceConstant("test_value", "test_msg", 10)
    with pytest.raises(TypeError):
        # Should throw a "TypeError: parameter value must be a sequence"
        dep = _DeprecatedSequenceConstant(10, "test_msg", "2.10")
    dep = _DeprecatedSequenceConstant("test_value", "test_msg", "2.10")
    assert dep.__len__() == 11


# Generated at 2022-06-22 11:26:23.753994
# Unit test for function set_constant
def test_set_constant():
    assert set_constant('test', 'test string') == {'test': 'test string'}
    assert set_constant('test', 'test string', export={'exist': 'in dict'}) == {'test': 'test string', 'exist': 'in dict'}
    assert set_constant('test', 'test string', export={'test': 'exist in dict'}) == {'test': 'exist in dict'}
    assert set_constant('test', 'test string', export={'test': 'exist in dict'}, clobber=True) == {'test': 'test string'}

if __name__ == '__main__':
    test_set_constant()

# Generated at 2022-06-22 11:26:30.753571
# Unit test for function set_constant
def test_set_constant():
    '''
    This function tests whether set_constant is working as expected.
    '''
    # Variable initialization
    _global_ns = {}
    _global_ns_bak = _global_ns.copy()

    # Test set_constant() with 'ascii_letters' as value
    set_constant("test_ascii_letters", ascii_letters, _global_ns)
    assert _global_ns["test_ascii_letters"] == ascii_letters

    # Test set_constant() with 'digits' as value
    set_constant("test_digits", digits, _global_ns)
    assert _global_ns["test_digits"] == digits

    # Test set_constant() with 'invalid_var' as value

# Generated at 2022-06-22 11:26:34.342944
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    l = _DeprecatedSequenceConstant(value=['a', 'b', 'c'], msg='test message', version='2.0')
    assert len(l) == 3

# Generated at 2022-06-22 11:26:38.137773
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    sequence = _DeprecatedSequenceConstant([], 'test', '2.10')
    assert isinstance(sequence, Sequence)
    assert len(sequence) == 0

# Unit tests for the above constants

# Generated at 2022-06-22 11:26:43.396052
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # set up
    value = [1, 2, 3, 4]
    msg = "whatever"
    version = "1.2.3"
    testConstant = _DeprecatedSequenceConstant(value, msg, version)
    assert testConstant is not None
    assert len(testConstant) == 4
    assert testConstant[0] == 1

if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:26:45.872667
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    x = _DeprecatedSequenceConstant([1, 2, 3, 4], 'msg', '3.0')[1]
    assert x == 2


# Generated at 2022-06-22 11:26:49.787399
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_seq = _DeprecatedSequenceConstant(['one', 'two', 'three'], 'msg', '1.0')
    assert (test_seq.__len__() == 3)

# Generated at 2022-06-22 11:26:57.242772
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    for arg in ("msg", "version"):
        if isinstance(eval(arg), int):
            raise Exception("'{0}' has unexpected type 'int'".format(arg))

_test = test__DeprecatedSequenceConstant()

# select CONSTANT, message, release in DEPRECATED_OPTIONS
#   '{0}': _DeprecatedSequenceConstant(({1}), '{0} is deprecated since Ansible {2}'.format('{0}', '{1}', '{2}')),

# Generated at 2022-06-22 11:29:06.712741
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_value = [4,2,3,4]
    test_msg = "msg"
    test_version = "version"
    obj = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    actual = len(obj)
    assert actual == 4

# Generated at 2022-06-22 11:29:08.399178
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], 'msg', 'version')) == 0


# Generated at 2022-06-22 11:29:11.166776
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant(['test'], 'msg', '2.1')
    assert len(c) == 1

# Generated at 2022-06-22 11:29:12.509524
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    result = _DeprecatedSequenceConstant([1, 2, 3], 'test_msg', '2.7')(1)
    assert result == 2


# Generated at 2022-06-22 11:29:17.225919
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "This is the test message."
    version = "1.0"
    seq = [1, 2, 3]
    dep_seq_constant = _DeprecatedSequenceConstant(seq, msg, version)
    assert len(dep_seq_constant) == 3, "Length must be three."
    assert dep_seq_constant[0] == 1, "First item must be 1."