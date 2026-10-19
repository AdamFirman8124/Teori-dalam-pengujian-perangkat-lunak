

# Generated at 2022-06-22 11:19:18.043926
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    sequence = [1, 2, 3]
    deprecate_sequence_constant = _DeprecatedSequenceConstant(sequence=sequence, msg='Test', version='2.11')
    assert deprecate_sequence_constant.__getitem__(2) == 3



# Generated at 2022-06-22 11:19:29.541332
# Unit test for function set_constant
def test_set_constant():
    test_constant = {'test_string': 'test_value', 'test_list': ['test_item'], 'test_dict': {'test_key': 'test_value'}}
    for constant in test_constant:
        set_constant(constant, test_constant[constant])
        assert constant in globals()
        assert globals()[constant] == test_constant[constant]


# deprecated constants, remove in Ansible 2.6
ACOMMON_ARGS_DEPRECATED = _DeprecatedSequenceConstant(ACOMMON_ARGS, "The 'ACOMMON_ARGS' constant has been deprecated and will be removed in Ansible 2.6.", "2.6")

# Generated at 2022-06-22 11:19:31.563485
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar')
    assert foo == 'bar'

# Generated at 2022-06-22 11:19:35.410127
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():

    dsc = _DeprecatedSequenceConstant(value=[], msg="Testing deprecated warning", version="2.12")
    dsc.__len__()
    dsc.__getitem__(0)

# Generated at 2022-06-22 11:19:45.655258
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    global _ACTION_INCLUDE
    global _ACTION_INCLUDE_ROLE
    global _ACTION_INCLUDE_TASKS
    global _ACTION_INCLUDE_VARS

    warn = _DeprecatedSequenceConstant(
        value = _ACTION_INCLUDE_ROLE,
        msg = 'include_role (and import_role) is deprecated. Use ansible-galaxy instead.',
        version = '2.9'
    )
    print(len(warn))
    print(warn[0])
    print(warn[1])
    print(warn[2])

# Generated at 2022-06-22 11:19:49.014884
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    version = '2.4'
    msg = 'msg to print'
    value = [1, 2, 3]
    deprecated = _DeprecatedSequenceConstant(value, msg, version)
    assert len(deprecated) == 3


# Generated at 2022-06-22 11:19:52.665268
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    v = _DeprecatedSequenceConstant(['test', 'ar'], 'test message', 'version 1.0')
    assert len(v) == 2
    assert v[0] == 'test'
    assert v[1] == 'ar'


# Generated at 2022-06-22 11:19:54.796416
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    _DeprecatedSequenceConstant([1, 2, 3], "warning message", "2.9").__getitem__(1)

# Generated at 2022-06-22 11:19:58.594584
# Unit test for function set_constant
def test_set_constant():
    # we're not testing the CONFIG manager, that's
    # an exercise for the reader.
    assert type(COLLECTION_PTYPE_COMPAT) is dict
    assert type(DOCUMENTABLE_PLUGINS) is tuple

# Generated at 2022-06-22 11:20:00.390790
# Unit test for function set_constant
def test_set_constant():
    from ansible.constants import set_constant
    assert isinstance(DeprecatedModule, _DeprecatedSequenceConstant)

# Generated at 2022-06-22 11:20:07.346858
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = _DeprecatedSequenceConstant(['test1','test2','test3','test4','test5'], "It's a test warning!", "2.4")
    for i in range(len(value)):
        assert value[i] == f'test{i + 1}'

# Generated at 2022-06-22 11:20:17.555605
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # test the constructor of _DeprecatedSequenceConstant
    test_value = ['test']
    test_msg = 'test msg'
    test_version = '2.2'
    test_deprecated_constant = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert test_deprecated_constant._value == ['test'], 'test value in _DeprecatedSequenceConstant constructor does not match test value'
    assert test_deprecated_constant._msg == 'test msg', 'test msg in _DeprecatedSequenceConstant constructor does not match test msg'
    assert test_deprecated_constant._version == '2.2', 'test version in _DeprecatedSequenceConstant constructor does not match test version'

    # test the _len_ and __getitem__ functions

# Generated at 2022-06-22 11:20:21.859478
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg='msg1'
    version='version1'
    test_object = _DeprecatedSequenceConstant(value=('v1', 'v2'), msg=msg, version=version)
    assert len(test_object) == 2


# Generated at 2022-06-22 11:20:25.240690
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq_const = _DeprecatedSequenceConstant((1,2), "", "2.9")
    assert seq_const[1] == 2
    assert len(seq_const) == 2

# Generated at 2022-06-22 11:20:27.914052
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant([], "", "")
    assert len(dsc) == 0


# Generated at 2022-06-22 11:20:36.753437
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "This is a test msg"
    version = "1.0.0"

    test_sequence = _DeprecatedSequenceConstant([], msg, version)
    assert test_sequence.__len__() == 0

    test_sequence = _DeprecatedSequenceConstant([1, 2, 3, 4], msg, version)
    assert test_sequence.__len__() == 4
    assert test_sequence.__getitem__(2) == 3

# Generated at 2022-06-22 11:20:39.952904
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_constant = _DeprecatedSequenceConstant(value=['one', 'two', 'three'], msg='Deprecation message', version="2.9")
    assert len(test_constant) == 3
    assert test_constant[0] == 'one'

# Generated at 2022-06-22 11:20:44.069157
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    l = ['a', 'b']
    r = _DeprecatedSequenceConstant(l, 'foo', 'bar')
    assert r[0] == 'a'
    assert r[1] == 'b'
    assert r[0:2] == ['a', 'b']


# Generated at 2022-06-22 11:20:46.138854
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    assert len(_DeprecatedSequenceConstant((1, 2, 3), None, None)) == 3


# Generated at 2022-06-22 11:20:57.156447
# Unit test for function set_constant
def test_set_constant():
    from tempfile import NamedTemporaryFile
    import os
    import imp

    constants_expected = {
        'ANSIBLE_CONFIG': './myconfig.cfg',
        'ANSIBLE_ROLES_PATH': '/my/roles/path',
    }

    config_example = os.path.join(os.path.dirname(__file__), '..', 'test', 'sanity', 'code', 'test_config.cfg')
    assert os.path.exists(config_example)

    f = NamedTemporaryFile(mode='wt', delete=False)

# Generated at 2022-06-22 11:21:12.074365
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('FOO', 'BAR', export=export)
    assert export['FOO'] == 'BAR'


# post-configuration constants
BECOME_METHODS = ('sudo', 'su', 'pbrun', 'pfexec', 'runas', 'dzdo')
BECOME_ERROR_STRINGS = {'sudo': 'Sorry, try again.', 'su': '', 'pbrun': '', 'pfexec': ''}

# convert strings to tuples
MAGIC_VARIABLE_MAPPING = {key: tuple(values) for key, values in MAGIC_VARIABLE_MAPPING.items()}

# TODO: add support for adding additional module directories (C.DEFAULT_MODULE_PATH)

# Generated at 2022-06-22 11:21:16.044594
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert len(_DeprecatedSequenceConstant([1, 2, 3], 'test', '2.10')) == 3
    assert _DeprecatedSequenceConstant([1, 2, 3], 'test', '2.10')[1] == 2

# Generated at 2022-06-22 11:21:20.234329
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    s = _DeprecatedSequenceConstant([1, 2, 3], "foo", "2.0")
    assert len(s) == 3


# Generated at 2022-06-22 11:21:28.613557
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import mock
    import sys
    import types

    class TestDeprecated():
        def __call__(self, *args, **kwargs):
            self.called = True
            self.args = args
            self.kwargs = kwargs

    test = TestDeprecated()
    sys.modules['ansible.utils.display'] = mock.Mock()
    sys.modules['ansible.utils.display'].Display = mock.Mock(return_value=test)
    test_values = ['a', 'b', 'c']
    test_message = 'test message'
    test_version = '1.0'
    test_object = _DeprecatedSequenceConstant(test_values, test_message, test_version)
    assert test_object['a'] == 'b'
    assert test.called
    assert test.args

# Generated at 2022-06-22 11:21:33.297175
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_value = ('foo', 'bar')
    test_msg = 'test_msg'
    test_version = 'test_version'
    test_object = _DeprecatedSequenceConstant(test_value, test_msg, test_version)

    len(test_object)
    len(test_object)


# Generated at 2022-06-22 11:21:40.011115
# Unit test for function set_constant
def test_set_constant():
    # This test is located here because of the module-level globals

    # Make sure set_constant() is working
    set_constant("FOO", "BAR")
    assert globals()["FOO"] == "BAR"
    set_constant("ANSIBLE_FOO", "ANSIBLE_BAR")
    assert globals()["ANSIBLE_FOO"] == "ANSIBLE_BAR"
    set_constant("ANSIBLE_VERBOSE", None, export=vars(config))
    assert config.ANSIBLE_VERBOSE is None

# Generated at 2022-06-22 11:21:44.077607
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'msg'
    version = 'version'
    value = 'value'
    o = _DeprecatedSequenceConstant(value, msg, version)
    assert o._msg == msg and o._version == version and o._value == value

test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:21:49.169499
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = ['foo', 'bar']
    dsc = _DeprecatedSequenceConstant(value, 'msg', 'version')
    assert dsc[0] is value[0]
    assert dsc[1] is value[1]
    dsc_empty = _DeprecatedSequenceConstant([], 'msg', 'version')
    assert dsc_empty[-1] is None

# Generated at 2022-06-22 11:21:52.450753
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    c = _DeprecatedSequenceConstant(['1', '2', '3'], 'msg', 'version')
    assert len(c) == 3
    assert c[1] == '2'

# Generated at 2022-06-22 11:22:02.132617
# Unit test for function set_constant
def test_set_constant():
    set_constant('unit_test_constant', 'unit_test_value')
    assert locals()['unit_test_constant'] == 'unit_test_value'
    del locals()['unit_test_constant']


# Clean up __builtins__
del re
del string_types
del Template
del literal_eval
del ensure_type
del ConfigManager
del Sequence

# The following are deprecated action names

ACTION_DEBUG = _DeprecatedSequenceConstant(_ACTION_DEBUG, 'The ACTION_DEBUG constant is deprecated and will be removed in a future version', '2.10')
ACTION_IMPORT_PLAYBOOK = _DeprecatedSequenceConstant(_ACTION_IMPORT_PLAYBOOK, 'The ACTION_IMPORT_PLAYBOOK constant is deprecated and will be removed in a future version', '2.10')
ACTION_IMPORT_ROLE

# Generated at 2022-06-22 11:22:18.629503
# Unit test for function set_constant
def test_set_constant():
    set_constant('test_set_constant', True, locals())
    assert test_set_constant == True
    set_constant('test_set_constant', False)
    assert locals()['test_set_constant'] == False
    assert test_set_constant == False
    globals().pop('test_set_constant')


# Generated at 2022-06-22 11:22:22.686523
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    const = _DeprecatedSequenceConstant([1, 2, 3], 'Foo', '99.999')
    assert len(const) == 3
    assert len(const) == 3


# Generated at 2022-06-22 11:22:26.094480
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant([1, 2], "msg", "version")[0] == 1
    assert _DeprecatedSequenceConstant([1, 2], "msg", "version")[1] == 2

# Generated at 2022-06-22 11:22:36.950644
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_CONSTANT', 'test')
    assert 'TEST_CONSTANT' in vars()
    assert vars()['TEST_CONSTANT'] == 'test'

    # Variables starting with a number will not be set as constants
    set_constant('TEST_CONSTANT2', 'test2')
    set_constant('1TEST_CONSTANT', 'test2')
    assert 'TEST_CONSTANT2' in vars()
    assert vars()['TEST_CONSTANT2'] == 'test2'
    assert '1TEST_CONSTANT' not in vars()
    try:
        vars()['1TEST_CONSTANT'] == 'test2'
    except KeyError:
        pass

    # Variables that are Python keywords will not be

# Generated at 2022-06-22 11:22:40.491136
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert [1, 2, 3] == _DeprecatedSequenceConstant([1, 2, 3], "", "").__getitem__(0)


# Generated at 2022-06-22 11:22:50.014439
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_VERSION == __version__
    assert ANSIBLE_PIPELINING == True
    assert ANSIBLE_MODULE_UTILS == 'ansible.module_utils'


# to allow cases where users have set ANSIBLE_CONFIG in os.environ
del config

# These values are true and false, but we can't handle them as booleans
STRING_TRUE_STRINGS = ('YES', '1', 'TRUE', 'Y')
STRING_FALSE_STRINGS = ('NO', '0', 'FALSE', 'N')
_ALL_STRINGS = STRING_TRUE_STRINGS + STRING_FALSE_STRINGS

# This is here for backwards compatibility with modules that use the old
# behavior of this value.
HOST_KEY_CHECKING_SYS_DEFAULT = False


# Generated at 2022-06-22 11:23:02.794267
# Unit test for function set_constant
def test_set_constant():
    from ansible.config.manager import ConfigManager, ensure_type
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import Sequence
    from ansible.utils.fqcn import add_internal_fqcns
    from .. import constants
    from . import set_constant
    from jinja2 import Template
    from string import ascii_letters, digits

    # Test set_constant
    assert set_constant('TEST', 'test') is None
    assert constants.__dict__.get('TEST', None) == 'test'

    # Test constants with templatable value
    assert set_constant('TEST_TEMPLATE', '{{ DEFAULT_MODULE_PATH }}') is None

# Generated at 2022-06-22 11:23:09.473081
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    def_var = None
    message = 'This is test message.'
    version = '2.9.0'
    test_class = _DeprecatedSequenceConstant(def_var, message, version)
    assert len(test_class) == 0
    assert len(test_class) == 0  # Test for second call.

if __name__ == '__main__':
    test__DeprecatedSequenceConstant___len__()

# Generated at 2022-06-22 11:23:12.866020
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    for val in (1, 'a', True, False, [1, 2, 3]):
        dsc = _DeprecatedSequenceConstant(val, 'test', '2.9')
        assert len(dsc) == len(val)



# Generated at 2022-06-22 11:23:16.511813
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    sequence_constant = _DeprecatedSequenceConstant(value="test", msg="test", version="test")
    assert sequence_constant[0] == "test"
    assert len(sequence_constant) == 1

# Generated at 2022-06-22 11:23:32.926512
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    # GIVEN a _DeprecatedSequenceConstant object
    dsc = _DeprecatedSequenceConstant([0, 1, 2], 'This is deprecated', '2.0')

    # WHEN __getitem__ is called
    result = dsc.__getitem__(0)

    # THEN an warning should be written and the value should be returned
    assert result == 0


# Generated at 2022-06-22 11:23:42.132779
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import logging
    import sys
    import unittest

    class LoggingHandler(logging.Handler):
        def __init__(self):
            self.logs = []
            logging.Handler.__init__(self)

        def emit(self, record):
            self.logs.append(record)

    class Test__DeprecatedSequenceConstant(unittest.TestCase):
        def setUp(self):
            self._old_stderr = sys.stderr
            sys.stderr = LoggingHandler()

        def tearDown(self):
            sys.stderr = self._old_stderr


# Generated at 2022-06-22 11:23:50.724521
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import sys
    import io
    import unittest

    def mock_sys_stderr_write(contents):
        class MockStderrStream:
            def __init__(self, capture=True):
                self.capture = capture
                self.contents = ''

            def write(self, content):
                if self.capture:
                    self.contents += content

        fake_stderr = MockStderrStream()
        orig_stderr = sys.stderr
        sys.stderr = fake_stderr
        _deprecated("msg", "version")
        sys.stderr = orig_stderr
        fake_stderr.capture = False
        if len(fake_stderr.contents) == 0:
            raise AssertionError("Stream was not written to")

# Generated at 2022-06-22 11:23:56.227989
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_LIBRARY is None
    assert ANSIBLE_REMOTE_TEMP is None
    assert ANSIBLE_CONFIG is None
    assert ANSIBLE_DEBUG is None

test_set_constant()

# Generated at 2022-06-22 11:24:00.514338
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    t = _DeprecatedSequenceConstant([1, 2, 3], 'test_msg', '0.0.0')
    assert len(t) == 3
    assert t[0] == 1
    assert t[1] == 2
    assert t[2] == 3

# Generated at 2022-06-22 11:24:07.288583
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    import copy
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list_new = []
    msg = 'test_msg'
    version = 'test_version'
    test_case = [
        {'value': list1, 'msg': msg, 'version': version, 'want': len(list1)},
        {'value': list2, 'msg': msg, 'version': version, 'want': len(list2)}
    ]
    for tc in test_case:
        t = _DeprecatedSequenceConstant(tc['value'], tc['msg'], tc['version'])
        result = t.__len__()
        list_new.append(result)
    assert copy.deepcopy(list1) == copy.deepcopy(list_new)


# Unit test

# Generated at 2022-06-22 11:24:17.408531
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Set of known_hosts is being deprecated, so we test a list of known_hosts
    if not isinstance(_DeprecatedSequenceConstant([], 'message', 'version'), Sequence):
        raise AssertionError("_DeprecatedSequenceConstant does not inherit from Sequence.")
    if not isinstance(_DeprecatedSequenceConstant([], 'message', 'version'), list):
        raise AssertionError("_DeprecatedSequenceConstant does not inherit from list.")
    if not isinstance(_DeprecatedSequenceConstant([], 'message', 'version'), _DeprecatedSequenceConstant):
        raise AssertionError("_DeprecatedSequenceConstant does not inherit from _DeprecatedSequenceConstant.")

# Generated at 2022-06-22 11:24:21.644490
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dsc = _DeprecatedSequenceConstant(['aaa'], 'msg', 'v1.2')
    assert(len(dsc) == 1)
    assert(dsc[0] == 'aaa')
    # make sure _deprecated is called
    dsc = _DeprecatedSequenceConstant(['aaa'], 'msg', 'v1.2')

# Generated at 2022-06-22 11:24:26.895822
# Unit test for function set_constant
def test_set_constant():
    module = {}
    set_constant('bar', 'foo', export=module)
    set_constant('baz', [1, 2, 3], export=module)
    assert module['bar'] == 'foo'
    assert module['baz'] == [1, 2, 3]


# unit test for config constants

# Generated at 2022-06-22 11:24:32.676873
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant(list(range(10)), None, None)[0] == 0
    assert _DeprecatedSequenceConstant(list(range(10)), None, None)[9] == 9
    assert _DeprecatedSequenceConstant(list(range(10)), None, None)[-1] == 9


# Generated at 2022-06-22 11:25:06.162338
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test all possible indices (including negative indices)
    # Also test access of non-existing indices
    seq = (1, 2, 3, 4, 5)
    for index in range(-5, 5):
        msg = "foo"
        version = "5"
        cons = _DeprecatedSequenceConstant(seq, msg, version)
        try:
            cons[index]
        except IndexError:
            assert(index not in range(0, len(seq)))
        else:
            assert(index in range(0, len(seq)))


# Generated at 2022-06-22 11:25:15.669019
# Unit test for function set_constant
def test_set_constant():
    l = {}
    set_constant('test', 1, export=l)
    assert l['test'] == 1, "Set constant didn't work as expected"


VERSION = __version__.split('.')

# ANSIBLE_KEEP_REMOTE_FILES: if this is set to a non-empty
# value before the first task executes on a host, then Ansible
# will not delete temporary files from that host once it's
# done. This can be useful for inspecting the remote system after
# a playbook run.  Since this is often set in the environment,
# we use a getenv() call here to detect that.
ANSIBLE_KEEP_REMOTE_FILES = False

# Generated at 2022-06-22 11:25:17.582508
# Unit test for function set_constant
def test_set_constant():
    result = {}
    set_constant('name', 'value', result)
    assert result['name'] == 'value'
    set_constant('name', 'value2', result)
    assert result['name'] == 'value2'

# Generated at 2022-06-22 11:25:21.638144
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = ('a', 'b', 'c')
    msg = 'This is a test'
    version = '2.0'

    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert len(value) == len(dsc)



# Generated at 2022-06-22 11:25:25.842741
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    l1 = ['a', 'b', 'c']
    dsc = _DeprecatedSequenceConstant(l1, 'Test __len__', 'ver')
    assert len(dsc._value) == 3
    assert len(dsc) == 3



# Generated at 2022-06-22 11:25:28.556662
# Unit test for function set_constant
def test_set_constant():
    a = 100
    b = 200
    c = 300
    set_constant('a', b)
    assert a == b

# Generated at 2022-06-22 11:25:38.693112
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    tests = [
        (([1, 2, 3], 'this msg', '1.0'), 1, None),
        (([1, 2, 3], 'this msg', '1.0'), '1', TypeError('list indices must be integers, not str')),
    ]
    for args, k, expected in tests:
        try:
            assert _DeprecatedSequenceConstant(*args)[k] == expected
        except AssertionError as e:
            raise AssertionError('Exception raised for _DeprecatedSequenceConstant(*{0}): {1}'.format(args, e))
        except Exception as e:
            if not isinstance(expected, Exception):
                raise AssertionError('Unexpected exception raised for _DeprecatedSequenceConstant(*{0}): {1}'.format(args, e))

# Generated at 2022-06-22 11:25:42.732817
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant([1, 2, 3], "msg", "version")

if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:25:44.584517
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant([], 'test msg', '2.9')

# Generated at 2022-06-22 11:25:48.646225
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # create a _DeprecatedSequenceConstant object with constant list
    constant_obj = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', 'version')
    # assert __len__ method
    assert len(constant_obj) == 3


# Generated at 2022-06-22 11:26:46.799920
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Can construct object
    obj = _DeprecatedSequenceConstant([], '', '2.9.0')
    assert obj.__class__.__name__ == '_DeprecatedSequenceConstant'

# Generated at 2022-06-22 11:26:50.262841
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    d = _DeprecatedSequenceConstant([1, 2, 3], 'This is a test', '2.9')
    assert len(d) == 3


# Generated at 2022-06-22 11:26:53.967065
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    depr_sequence = _DeprecatedSequenceConstant([1, 2, 3], "", "")
    assert depr_sequence[0] == 1


# Generated at 2022-06-22 11:27:04.752905
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class TestDeprecatedSequenceConstant(object):
        def __init__(self, value_list, message, version):
            self.value_list = value_list
            self.message = message
            self.version = version

        def assert_equal(self, value1, value2):
            if value1 != value2:
                raise AssertionError()

    obj = TestDeprecatedSequenceConstant(['ansible.builtin.apt', 'ansible.builtin.copy'], 'Deprecated', '2.0')
    assert _DeprecatedSequenceConstant(obj.value_list, obj.message, obj.version)[0] == obj.value_list[0]
    assert _DeprecatedSequenceConstant(obj.value_list, obj.message, obj.version)[1] == obj.value_list[1]


# Generated at 2022-06-22 11:27:08.314143
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.module_utils.common.collections import is_sequence

    actual = is_sequence(_DeprecatedSequenceConstant([1, 2, 3, 4], 'msg', '2.8.'))
    assert actual is True

# Generated at 2022-06-22 11:27:15.678866
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    class Test:
        pass
    test = Test()
    test.name = 'test'
    test.value = [1, 2, 3]
    test.msg = 'this is a test'
    test.version = '1.0.0'
    test._value = test.value
    test._msg = test.msg
    test._version = test.version
    test_obj = _DeprecatedSequenceConstant(test.value, test.msg, test.version)
    assert test_obj._value == test.value
    assert test_obj._msg == test.msg
    assert test_obj._version == test.version

# Unit tests for the set_constant method

# Generated at 2022-06-22 11:27:22.040526
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "This is a test message"
    version = "2.0"
    seq = _DeprecatedSequenceConstant(value=["one", "two"], msg=msg, version=version)
    assert isinstance(seq, Sequence)
    assert len(seq) == 2
    assert seq[0] == "one"
    assert seq[1] == "two"


if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-22 11:27:25.080019
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant([], 'test msg', '1.0')
    assert isinstance(a, Sequence)
    assert len(a) == 0


### END OF FILE ###

# Generated at 2022-06-22 11:27:27.197263
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant([1, 2, 3], 'Test message', '2.10')
    assert len(dsc) == 3

# Generated at 2022-06-22 11:27:28.691485
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO', 'BAR')
    assert FOO == 'BAR'