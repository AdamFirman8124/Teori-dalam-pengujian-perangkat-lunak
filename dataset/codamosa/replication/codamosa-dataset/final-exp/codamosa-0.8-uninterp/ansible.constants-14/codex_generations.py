

# Generated at 2022-06-22 11:19:19.641692
# Unit test for function set_constant
def test_set_constant():
    # Test set constant to value and verify the value
    import ansible
    ansible_version = ansible.__version__
    set_constant('ANSIBLE_VERSION', ansible_version, globals())
    assert ANSIBLE_VERSION == ansible_version

    # Test set constant to value and verify the value
    ansible_verbose = "v"
    set_constant('ANSIBLE_VERBOSE', ansible_verbose, globals())
    assert ANSIBLE_VERBOSE == ansible_verbose

# Generated at 2022-06-22 11:19:29.987961
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    def test(test_value, test_msg, test_version):
        msg = 'Testing _DeprecatedSequenceConstant.__getitem__() with' \
              ' value={}, msg={} and version={}'.format(test_value, test_msg, test_version)
        try:
            depr_list = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
            depr_list[0]
        except Exception as e:
            assert False, '{} failed. Details: {}'.format(msg, e)
        else:
            assert True, msg


# Generated at 2022-06-22 11:19:34.883364
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    seq = ['foo', 'bar']
    msg = 'this is a warning'
    version = '2.0'
    d = _DeprecatedSequenceConstant(seq, msg, version)
    assert d[0] == 'foo'
    assert d[1] == 'bar'

# Generated at 2022-06-22 11:19:38.254154
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant(['a'], 'msg', 'version')
    assert len(seq) == 1
    assert seq[0] == 'a'

# Generated at 2022-06-22 11:19:49.250761
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # executing the above code before running this test case
    # to make sure that we get the latest version
    from ansible import __version__ as ansible_version

    msg = 'foo'
    version = '2.0'
    value = [1, 2, 3]
    x = _DeprecatedSequenceConstant(value, msg, version)

    assert len(x) == 3
    assert x[0] == 1
    assert x[1] == 2
    assert x[2] == 3

    # version = '1.0'
    # Should be deprecated
    # x = _DeprecatedSequenceConstant(value, msg, version)

    version = '2.0'
    # Should not be deprecated
    x = _DeprecatedSequenceConstant(value, msg, version)

    # If ansible version is 2.x (

# Generated at 2022-06-22 11:19:56.433367
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant([1, 2, 3], "test", "2018.2.0")[0] == 1
    assert _DeprecatedSequenceConstant([1, 2, 3], "test", "2018.2.0")[1] == 2
    assert _DeprecatedSequenceConstant([1, 2, 3], "test", "2018.2.0")[2] == 3


# Generated at 2022-06-22 11:20:02.147718
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'this is a test message'
    version = '9.9.9'
    value = ['test1', 'test2', 'test3']
    deprecated = _DeprecatedSequenceConstant(value, msg, version)
    assert len(deprecated) == len(value)
    for i in range(len(deprecated)):
        assert value[i] == deprecated[i]

# Generated at 2022-06-22 11:20:11.724853
# Unit test for function set_constant
def test_set_constant():
    set_constant('ANSIBLE_TEST_CONSTANT_1', 'foo')
    set_constant('ANSIBLE_TEST_CONSTANT_2', '{{ foo }}')
    assert ANSIBLE_TEST_CONSTANT_1 == 'foo'
    assert ANSIBLE_TEST_CONSTANT_2 == 'foo'
    set_constant('ANSIBLE_TEST_CONSTANT_1', 'bar', export=locals())
    assert ANSIBLE_TEST_CONSTANT_1 == 'bar'
    assert ANSIBLE_TEST_CONSTANT_2 == 'foo'

test_set_constant()

# Generated at 2022-06-22 11:20:19.941682
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = _DeprecatedSequenceConstant((0, 1, 2, 3), "test message", "test version")
    assert seq[0] == 0
    assert seq[1] == 1
    assert seq[2] == 2
    assert seq[3] == 3
    # Negative indices, same length
    assert seq[-1] == 3
    assert seq[-2] == 2
    assert seq[-3] == 1
    assert seq[-4] == 0


# Generated at 2022-06-22 11:20:25.644119
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant_value = [1, 2, 3, 4]
    msg = "test message"
    version = "2.14"
    deprecated_constant_object = _DeprecatedSequenceConstant(value=constant_value, msg=msg, version=version)
    assert deprecated_constant_object[1] == 2


# Generated at 2022-06-22 11:20:38.193152
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # ensure str and unicode behave the same
    L = ['a', 'b', 'c']
    msg = 'this is just a test'
    version = '2.9'
    dep_c = _DeprecatedSequenceConstant(L, msg, version)
    assert(len(L) == len(dep_c))

    # ensure non-iterable object returns 0
    L = None
    dep_c = _DeprecatedSequenceConstant(L, msg, version)
    assert(len(dep_c) == 0)


# Generated at 2022-06-22 11:20:39.793134
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_BECOME_PASS is None

# Generated at 2022-06-22 11:20:44.301836
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():

    # Test for __len__()
    assert len(_DeprecatedSequenceConstant([1, 2, 3], "test_len", "2.0")) == 3

    # Test for __getitem__()
    assert _DeprecatedSequenceConstant([1, 2, 3], "test_getitem", "2.0")[1] == 2


# Generated at 2022-06-22 11:20:46.653079
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_CONSTANT', 'fake data', export=globals())
    assert TEST_CONSTANT == 'fake data'

# Generated at 2022-06-22 11:20:51.880609
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'this is a test message'
    version = '4.0.0'
    sequence_constant_instance = _DeprecatedSequenceConstant(['a'], msg, version)
    sequence_constant_instance[0]
    # if the test complies successfully, test passed


# Generated at 2022-06-22 11:20:54.022159
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant(('a', 'b'), 'Test', '2.0')

# Generated at 2022-06-22 11:20:59.789094
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    s = ('SEQ', )
    dsc = _DeprecatedSequenceConstant(s, 'MSG', 'VER')
    assert dsc[0] == 'SEQ'
    assert s == ('SEQ', )



# Generated at 2022-06-22 11:21:02.777741
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant('abcde', 'message', '1.0')
    assert len(dsc) == len('abcde')


# Generated at 2022-06-22 11:21:06.314534
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant([1, 2, 3, 4], '', '')
    assert 4 == len(c)



# Generated at 2022-06-22 11:21:13.901170
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    ansible_play_hosts = _DeprecatedSequenceConstant(['1', '2'], 'ansible_play_hosts will be removed in Ansible 2.14', '2.14')
    ansible_play_hosts.append('3')
    assert ansible_play_hosts == ['1', '2', '3']
    assert len(ansible_play_hosts) == 3
    assert ansible_play_hosts[0:2] == ['1', '2']
    del ansible_play_hosts[1]
    assert ansible_play_hosts == ['1', '3']

# For backwards compatibility, accept a few deprecated constants.  Do not
# add anything new here.
# FIXME: remove once play_context mangling is removed

# Generated at 2022-06-22 11:21:27.636991
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # First use _DeprecatedSequenceConstant's magic method __getitem__ without a message and without a version.
    # This should lead to a DeprecationWarning being raised with a default message and version.
    dep_val = _DeprecatedSequenceConstant([1, 2, 3], None, None)
    dep_val[0]

    # Second use _DeprecatedSequenceConstant's magic method __getitem__ with a message and without a version.
    # This should lead to a DeprecationWarning being raised with the provided message and the default version.
    dep_val = _DeprecatedSequenceConstant([1, 2, 3], 'message for first test', None)
    dep_val[0]

    # Third use _DeprecatedSequenceConstant's magic method __getitem__ without a message, but with a version.
    # This should lead

# Generated at 2022-06-22 11:21:31.146158
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    value = (1, 2, 3)
    msg = 'This is a message'
    version = '1.0'
    c = _DeprecatedSequenceConstant(value, msg, version)
    assert c._value == value
    assert c._msg == msg
    assert c._version == version

# Generated at 2022-06-22 11:21:41.036958
# Unit test for function set_constant
def test_set_constant():
    value = '11'
    t = Template('{{ value }}')
    assert t.render(value=value) == '11'
    assert ensure_type(t.render(value=value), int) == 11
    assert ensure_type(ensure_type(t.render(value=value), int), int) == 11

# And some other useful constants/functions/variables
set_constant('COMMON_CONNECTION_VARS', COMMON_CONNECTION_VARS)
set_constant('MAGIC_VARIABLE_MAPPING', MAGIC_VARIABLE_MAPPING)

# constant compatibility for deprecated variables
set_constant('DEFAULT_SUDO_USER', DEFAULT_REMOTE_USER)
set_constant('DEFAULT_SUDO', DEFAULT_BECOME)
set

# Generated at 2022-06-22 11:21:46.591002
# Unit test for function set_constant

# Generated at 2022-06-22 11:21:55.356144
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    import uuid

    old_value = ['a', 'b', 'c']
    version = str(uuid.uuid4())
    msg = 'msg'

    c = _DeprecatedSequenceConstant(old_value, msg, version)

    old_value.append('d')
    assert old_value == ['a', 'b', 'c', 'd']
    assert list(c) == ['a', 'b', 'c']

    value = c[0]
    assert old_value == ['a', 'b', 'c', 'd']
    assert value == 'a'


# Generated at 2022-06-22 11:21:59.605050
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    s = _DeprecatedSequenceConstant(('a', 'b', 'c'), 'msg', 'version')

    assert s
    assert len(s) == 3
    assert s[0] == 'a'
    assert s[1] == 'b'
    assert s[2] == 'c'

# Generated at 2022-06-22 11:22:11.057416
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    c = _DeprecatedSequenceConstant(('foo', 'bar', 'baz'), 'This is a warning', '2.10')
    assert len(c) == 3
    assert c[1] == 'bar'
    assert repr(c) == repr(('foo', 'bar', 'baz'))
    assert str(c) == str(('foo', 'bar', 'baz'))
    assert bool(c)
    assert not bool(c.__class__(tuple(), 'This is a warning', '2.10'))
    assert not bool(c.__class__(('', ), 'This is a warning', '2.10'))
    assert c == ('foo', 'bar', 'baz')
    assert c != ('foo', 'bar', 'baz', 'qux')
    assert c == c.__class__

# Generated at 2022-06-22 11:22:21.662530
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_NOCOWS == False
    assert ANSIBLE_LIBRARY == [u'/usr/share/ansible']
    assert ANSIBLE_MODULE_UTILS == [u'/usr/share/ansible/lib/ansible/module_utils']
    assert DEFAULT_MODULE_NAME == u'command'
    assert DEFAULT_MODULE_PATH == [u'/usr/share/ansible/plugins/modules']
    assert DEFAULT_REMOTE_USER == u'root'
    assert DEFAULT_SUDO_EXE == u'sudo'
    assert DEFAULT_SUDO_FLAGS == u'-H -S -n'
    assert DEFAULT_SUDO_USER == u'root'
    assert DEFAULT_SYSLOG_FACILITY == u'LOG_USER'
    assert DEFAULT

# Generated at 2022-06-22 11:22:31.288679
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_BECOME_PASS is None
    assert DEFAULT_REMOTE_PASS is None
    assert DEFAULT_PASSWORD_CHARS == to_text(ascii_letters + digits + ".,:-_", errors='strict')
    assert MODULE_REQUIRE_ARGS == tuple(add_internal_fqcns(('command', 'win_command', 'ansible.windows.win_command', 'shell', 'win_shell',
                                                            'ansible.windows.win_shell', 'raw', 'script')))
    assert MODULE_NO_JSON == tuple(add_internal_fqcns(('command', 'win_command', 'ansible.windows.win_command', 'shell', 'win_shell',
                                                       'ansible.windows.win_shell', 'raw')))

# Generated at 2022-06-22 11:22:37.264986
# Unit test for function set_constant
def test_set_constant():
    import sys

    # Write to stdout
    sys.stdout = open('/dev/null', 'w')

    # Reset globals
    global TREE_DIR
    TREE_DIR = None

    # Ensure variable is set
    set_constant('TREE_DIR', 'test_tree')
    assert TREE_DIR == 'test_tree'

    # Clear stdout
    sys.stdout = sys.__stdout__

# Generated at 2022-06-22 11:22:52.786759
# Unit test for function set_constant
def test_set_constant():
    assert not hasattr(globals(), 'test_not_set')
    set_constant('test_not_set', 'test_value')
    assert hasattr(globals(), 'test_not_set')
    assert globals()['test_not_set'] == 'test_value'


# TODO: remove special handling of these once v2.0 is final
for var in ('DEFAULT_HOST_LIST', 'DEFAULT_HOST_PATTERN'):
    assert config.data[var] is not None
    # sets this to the _DeprecatedSequenceConstant class, which
    # trigers warnings when accessed.

# Generated at 2022-06-22 11:22:57.060948
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert(test[0] == 1)
    assert(test[2] == 3)
    assert(test[-1] == 3)


# Generated at 2022-06-22 11:23:04.196752
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('one', 1, export)
    assert export['one'] == 1
    set_constant('two', 'two', export)
    assert export['two'] == 'two'
    set_constant('bool', True, export)
    assert export['bool'] is True
    set_constant('list', [1, 2], export)
    assert export['list'] == [1, 2]
    set_constant('dict', {'a': 1}, export)
    assert export['dict'] == {'a': 1}
    set_constant('tuple', (1, 2), export)
    assert export['tuple'] == (1, 2)

# Generated at 2022-06-22 11:23:06.956694
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    x = _DeprecatedSequenceConstant((1,2,3), "msg", "version")
    assert len(x) == 3


# Generated at 2022-06-22 11:23:18.090740
# Unit test for function set_constant
def test_set_constant():
    ''' set_constant should define constants and assign them their type '''

    # Test both default and non default values
    set_constant('TEST_0', 'test')
    set_constant('TEST_1', 'test', locals())
    set_constant('TEST_2', {'test': 'test'})
    set_constant('TEST_3', {'test': 'test'}, locals())
    set_constant('TEST_4', ['test'])
    set_constant('TEST_5', ['test'], locals())
    set_constant('TEST_6', -1)
    set_constant('TEST_7', -1, locals())
    set_constant('TEST_8', True)
    set_constant('TEST_9', True, locals())

   

# Generated at 2022-06-22 11:23:23.037421
# Unit test for function set_constant
def test_set_constant():
    '''
    set_constant function test

    >>> from ansible.utils.constants import set_constant
    >>> set_constant('TEST_CONSTANT', 'foobar')
    >>> TEST_CONSTANT
    'foobar'
    >>> set_constant('TEST_CONSTANT', ['foo','bar'])
    >>> TEST_CONSTANT
    ['foo', 'bar']
    '''



# Generated at 2022-06-22 11:23:28.245376
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant('test_value', 'test message', 'test version')
    assert len(seq) == len('test_value')
    assert seq[0] == 't'

# Generated at 2022-06-22 11:23:30.372187
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([1, 2, 3], 'this is a test', '99.99')) == 3



# Generated at 2022-06-22 11:23:31.737975
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_CONSTANT', True)
    assert TEST_CONSTANT is True

# Generated at 2022-06-22 11:23:40.214839
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import mock
    import unittest
    from ansible.module_utils.common.collections import _DeprecatedSequenceConstant

    v = [1, 2, 3]
    m = "this is a message"
    vr = "2.0.0"

    dsc = _DeprecatedSequenceConstant(v, m, vr)
    with mock.patch('ansible.module_utils.basic.deprecated') as mock_depr:
        dsc[1]
        mock_depr.assert_called_once_with(m, version=vr)

    class Test__DeprecatedSequenceConstant(unittest.TestCase):
        def setUp(self):
            self.dsc = _DeprecatedSequenceConstant(v, m, vr)


# Generated at 2022-06-22 11:24:00.000290
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar', locals())
    assert locals() == {'foo': 'bar'}


# FIXME: remove once the PlayContext magic is gone
# COMPILE MAGIC_VARIABLE_MAPPING INTO A SINGLE REGEX
# this will make matching much faster

MAGIC_VARIABLE_MAPPING_REGEX = None
MAGIC_VARIABLE_MAPPING_CACHE = {}



# Generated at 2022-06-22 11:24:04.444979
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    const = _DeprecatedSequenceConstant([1, 2, 3], 'Some message', '1.10')

    try:
        len(const)
        assert False
    except Exception:
        assert True

    try:
        const[1]
        assert False
    except Exception:
        assert True

# Generated at 2022-06-22 11:24:08.935652
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = _DeprecatedSequenceConstant((1, 2, 3), 'msg1', '1.0')
    assert seq[0] == 1

    seq = _DeprecatedSequenceConstant({1: 1, 2: 2}, 'msg2', '1.0')
    assert seq[1] == 1



# Generated at 2022-06-22 11:24:20.462559
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class DummyClass:
        def deprecated(self, msg, version=None):
            self.msg = msg
            self.version = version

    d = DummyClass()
    original_sequence = ['item0', 'item1', 'item2']
    msg = 'a message'
    version = 'a version'
    c = _DeprecatedSequenceConstant(original_sequence, msg, version)

    d.deprecated = c.deprecated
    c.deprecated = d.deprecated

    # Make sure that item retrieval is delegated to underlying sequence
    assert c[0] == original_sequence[0]
    assert c[1] == original_sequence[1]
    assert c[2] == original_sequence[2]

    # Make sure that deprecation message is issued
    assert d.msg == msg

# Generated at 2022-06-22 11:24:22.553418
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert 3 == len(_DeprecatedSequenceConstant([1, 2, 3], '', ''))


# Generated at 2022-06-22 11:24:28.264504
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    obj = _DeprecatedSequenceConstant([], '', '')
    assert obj

# Make this class available to ScopedData after it has been fully constructed.
# pylint: disable=wrong-import-position
from ansible.vars.scoped_vars import ScopedData  # noqa
ScopedData.CONSTANTS = add_internal_fqcns(vars())

# Generated at 2022-06-22 11:24:33.165323
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert isinstance(_DeprecatedSequenceConstant([1, 2, 3], 'hello', ''), _DeprecatedSequenceConstant)
    assert isinstance(_DeprecatedSequenceConstant((1, 2, 3), 'hello', ''), _DeprecatedSequenceConstant)

# Generated at 2022-06-22 11:24:39.757057
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    DEPRECATED_VARIABLES = _DeprecatedSequenceConstant(['ansible_ssh_host', 'ansible_ssh_pipelining', 'ansible_ssh_user'], 'Using ssh variables', '2.6')
    assert len(DEPRECATED_VARIABLES) == 3
    assert DEPRECATED_VARIABLES[1] == 'ansible_ssh_pipelining'

# Generated at 2022-06-22 11:24:42.447114
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    _DeprecatedSequenceConstant(
        ["list1", "list2", "list3"],
        'testing',
        '2.7'
    )[0]



# Generated at 2022-06-22 11:24:45.084476
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_object = _DeprecatedSequenceConstant(value=[], msg='msg', version='version')
    assert len(test_object) == 0
    assert test_object[0] is None

# Generated at 2022-06-22 11:25:15.676004
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():  # pragma: no cover
    ''' check class instantiation and load of settings from dictionary '''
    d = _DeprecatedSequenceConstant([1, 2, 3], 'this is deprecated', '2.14')
    assert len(d) == 3
    assert d[0] == 1
    assert str(d) == '[1, 2, 3]'

# Generated at 2022-06-22 11:25:19.139987
# Unit test for function set_constant
def test_set_constant():
    import sys
    if sys.version_info[0] >= 3:
        reload(sys)
    sys.setdefaultencoding('utf8')
    str = 'ansible'
    set_constant('str', str)
    assert str == ansible

test_set_constant()

# Generated at 2022-06-22 11:25:26.640622
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    # tests _DeprecatedSequenceConstant in case of empty list
    dsc = _DeprecatedSequenceConstant([], "msg", "version")
    dsc[0]
    dsc[-1]

    # tests _DeprecatedSequenceConstant in case of non empty list
    dsc = _DeprecatedSequenceConstant([10, 20, 30], "msg", "version")
    dsc[0]
    dsc[1]
    dsc[2]
    dsc[-1]
    dsc[-2]
    dsc[-3]
    try:
        dsc[3]
        assert False
    except IndexError:
        assert True



# Generated at 2022-06-22 11:25:32.984362
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], 'msg', 'version')) == 0
    assert len(_DeprecatedSequenceConstant((), 'msg', 'version')) == 0
    assert len(_DeprecatedSequenceConstant('string', 'msg', 'version')) == 6
    assert len(_DeprecatedSequenceConstant(('tuple',), 'msg', 'version')) == 1


# Generated at 2022-06-22 11:25:34.011564
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_obj = _DeprecatedSequenceConstant([1, 2, 3], "msg", "version")
    assert test_obj[1] == 2

# Generated at 2022-06-22 11:25:36.901418
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant('abc', 'msg', '2.0.0')['a'] == 'abc'['a']

# Unit test method __len__ of class _DeprecatedSequenceConstant

# Generated at 2022-06-22 11:25:41.920040
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant((1, 2, 3), 'msg', '2.4')) == 3
    assert len(_DeprecatedSequenceConstant((1, 2, 3), 'msg', '2.4')) == 3


# Generated at 2022-06-22 11:25:45.423215
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    ''' unit test for deprecated sequence class '''
    msg = 'this is a test'
    seq = _DeprecatedSequenceConstant(value=['one', 'two', '3'], msg=msg, version='2.8')
    assert len(seq) == 3
    assert seq[1] == 'two'
    assert seq[-1] == '3'

# Generated at 2022-06-22 11:25:56.551802
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_PASSWORD_CHARS == u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,:-_'
    assert DEFAULT_PASSWORD_CHARS == config.DEFAULT_PASSWORD_CHARS
    assert DEFAULT_REMOTE_PASS == ''
    assert DEFAULT_REMOTE_PASS == config.DEFAULT_REMOTE_PASS
    assert DEFAULT_SUBSET == 'all'
    assert DEFAULT_SUBSET == config.DEFAULT_SUBSET
    assert COLLECTION_PTYPE_COMPAT == {'module': 'modules'}
    assert COLLECTION_PTYPE_COMPAT == config.COLLECTION_PTYPE_COMPAT

# Generated at 2022-06-22 11:25:58.696151
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    d = _DeprecatedSequenceConstant(value=[], msg='msg', version='version')
    assert len(d) == 0


# Generated at 2022-06-22 11:27:00.501886
# Unit test for function set_constant
def test_set_constant():
    _constants = {}
    set_constant('test_constant', 'constant', export=_constants)
    assert _constants['test_constant'] == 'constant'

# Generated at 2022-06-22 11:27:03.466243
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    const = _DeprecatedSequenceConstant((1, 2, 3), 'msg', 'version')

    if len(const) != 3:
        raise ValueError

    if const[0] != 1:
        raise ValueError

# Generated at 2022-06-22 11:27:05.607021
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_list = ['test', 'list']
    for test_value in [list, tuple, set]:
        test_obj = _DeprecatedSequenceConstant(test_value(test_list), 'Not a real message or anything', '1.2')
        assert len(test_value(test_list)) == len(test_obj)


# Generated at 2022-06-22 11:27:11.016328
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_value = ['a', 'b', 'c']
    test_msg = "some test message"
    test_version = "2.11"
    test_obj = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert len(test_value) == len(test_obj)


# Generated at 2022-06-22 11:27:14.360480
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    class_instance = _DeprecatedSequenceConstant(('debug', 'set_fact'), 'Test Message', '2.4')
    assert len(class_instance) == 2
    assert class_instance[0] == 'debug'
    assert class_instance[1] == 'set_fact'


# Generated at 2022-06-22 11:27:17.341585
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test = _DeprecatedSequenceConstant(list(range(10)), msg='testing __len__', version='2.9')
    assert len(test) == 10


# Generated at 2022-06-22 11:27:20.084799
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dummy = _DeprecatedSequenceConstant('abc', 'msg', 'version')
    assert len(dummy) == 3
    assert len(dummy._value) == 3

# Generated at 2022-06-22 11:27:23.166213
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    t = _DeprecatedSequenceConstant([1, 2, 3], 'test message', '2.8')
    assert t[0] == 1


# Generated at 2022-06-22 11:27:32.592952
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():

    o = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert o._value == [1, 2, 3]
    assert o._msg == 'msg'
    assert o._version == 'version'

    assert len(o) == 3

    assert o[0] == 1
    assert o[1] == 2
    assert o[2] == 3


# Constant setting
set_constant('_ACTION_HAS_CMD', _ACTION_HAS_CMD)
set_constant('_ACTION_ALLOW_TASK_LOOP', _ACTION_ALL_INCLUDE_TASKS + add_internal_fqcns(('with_', 'include_tasks')))

# Generated at 2022-06-22 11:27:36.865161
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test = _DeprecatedSequenceConstant(['a', 'b'], 'this is a test', '2.0')
    assert list(test) == ['a', 'b']
    assert test[0] == 'a'