

# Generated at 2022-06-22 11:19:25.010111
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant([1, 2, 3], "test", 1.2)

    if len(a) != 3:
        raise Exception("Wrong length")

    if a[0] != 1:
        raise Exception("Wrong element")

    if a[-1] != 3:
        raise Exception("Wrong element")

# Generated at 2022-06-22 11:19:32.551576
# Unit test for function set_constant
def test_set_constant():
    set_constant('ANSIBLE_TEST', 'ANSIBLE_TEST')
    assert(ANSIBLE_TEST == 'ANSIBLE_TEST')


# Calculated values
ROLE_NAME_MAX_LENGTH = 250 - len('-'.join((__version__.replace('.', ''), 'default')))
ROLE_NAME_RE = re.compile('^[a-zA-Z0-9][a-zA-Z0-9_.-]+$')


# Generated at 2022-06-22 11:19:45.655302
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_data = (
        ('v1', [], 'msg', 'ver', [], 'msg'),
        ('v2', [], '', '', [], ''),
        ('v3', [1,2,3], 'msg2', 'ver2', 3, 'msg2'),
    )
    for test_vector in test_data:
        dsc = _DeprecatedSequenceConstant(test_vector[0], test_vector[1], test_vector[2])
        if len(dsc) != test_vector[3]:
            raise AssertionError("len(%s) got %s, expected %s" % (test_vector[0], test_vector[3], test_vector[4]))

# Generated at 2022-06-22 11:19:49.596045
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    """
    >>> assert len(_DeprecatedSequenceConstant((1, 2, 3), '', '2.10')) == 3
    >>> assert _DeprecatedSequenceConstant((1, 2, 3), '', '2.10')[0] == 1
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-22 11:19:56.951359
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # the following checks for proper behavior for the __getitem__ method of class _DeprecatedSequenceConstant[_DeprecatedSequenceConstant]
    deprecated_object = _DeprecatedSequenceConstant(_DeprecatedSequenceConstant((1, 2), "msg", "version"), "msg", "version")
    assert deprecated_object[0] == (1, 2)
    assert deprecated_object[1] == ()



# Generated at 2022-06-22 11:20:03.459401
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant(['a', 'b'], 'test', '2.3')
    assert type(seq) == _DeprecatedSequenceConstant
    assert seq[0] == 'a'
    assert seq[1] == 'b'
    assert len(seq) == 2

if __name__ == '__main__':
    test__DeprecatedSequenceConstant()
    print('All unit tests passed')

# Generated at 2022-06-22 11:20:05.320636
# Unit test for function set_constant
def test_set_constant():
    set_constant('a', 'apple')
    assert a == 'apple'



# Generated at 2022-06-22 11:20:15.355467
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.constants import _DeprecatedSequenceConstant
    import sys
    import io

    capture_stdout = io.StringIO()
    capture_sys_stderr = io.StringIO()
    sys.stdout = capture_stdout
    sys.stderr = capture_sys_stderr

# Generated at 2022-06-22 11:20:20.250348
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    A = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'testing', '2.0')
    assert len(A) == 3
    assert A[0] == 'a'
    assert A[1] == 'b'
    assert A[2] == 'c'

# Generated at 2022-06-22 11:20:27.373584
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Create the constant
    s = _DeprecatedSequenceConstant( [1,2,3], 'MSG', 'VERSION' )
    # Ensure that when we access the item, the deprecate method is called
    msg = 'MSG'
    version = 'VERSION'
    assert s[1] == 2
    # Ensure that the deprecate method was called
    assert msg == 'MSG'
    assert version == 'VERSION'



# Generated at 2022-06-22 11:20:33.038867
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    foo = _DeprecatedSequenceConstant('12345', 'message', '1.0')
    assert len(foo) == 5



# Generated at 2022-06-22 11:20:45.065699
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    from ansible.errors import AnsibleDeprecationWarning
    from ansible.module_utils.six import assertRaisesRegex
    from ansible.module_utils.six import assertWarnsRegex

    with assertRaisesRegex(Exception, "object of type '_DeprecatedSequenceConstant' has no len()"):
        len(_DeprecatedSequenceConstant('value', 'msg', 'version'))

    with assertWarnsRegex(AnsibleDeprecationWarning, "msg, to be removed in version"):
        len(_DeprecatedSequenceConstant('value', 'msg', 'version'))

    assert len(_DeprecatedSequenceConstant(('v1', 'v2'), 'msg', 'version')) == 2

# Generated at 2022-06-22 11:20:47.359574
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    #test  for  with  list
    myclass = _DeprecatedSequenceConstant([1, 2, 3], "msg", "version")
    myreturn = myclass[1]
    assert myreturn == 2

    #test for with tuple
    myclass = _DeprecatedSequenceConstant(('a', 'b'), "msg", "version")
    myreturn = myclass[1]
    assert myreturn == 'b'

# Generated at 2022-06-22 11:20:51.625706
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    obj = _DeprecatedSequenceConstant((1, 2, 3), 'this is the message', '2.9')
    assert obj[0] == 1
    assert obj[1] == 2
    assert obj[2] == 3

# Generated at 2022-06-22 11:20:59.438177
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    l = ['item1', 'item2', 'item3']
    dsc = _DeprecatedSequenceConstant(l, 'this is a test', '2.9')
    assert dsc[0] == 'item1'
    assert dsc[1] == 'item2'
    assert dsc[2] == 'item3'
    assert dsc[1:3] == ['item2', 'item3']
    assert dsc[-3] == 'item1'
    assert dsc[-2] == 'item2'
    assert dsc[-1] == 'item3'
    assert dsc[-1:] == ['item3']


# Generated at 2022-06-22 11:21:09.268711
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant((1, 2), 'foo', 'bar')
    assert len(a) == 2
    assert a[0] == 1
    assert a[1] == 2

# Add deprecated constants
set_constant('ALL_HOSTS', 'localhost')
set_constant('DEFAULT_ASK_VAULT_PASS', BOOLEAN_FALSE)
set_constant('DEFAULT_BECOME', BOOLEAN_FALSE)
set_constant('DEFAULT_BECOME_ASK', BOOLEAN_TRUE)
set_constant('DEFAULT_BECOME_ASK_PASS', BOOLEAN_FALSE)
set_constant('DEFAULT_BECOME_METHOD', 'sudo')

# Generated at 2022-06-22 11:21:12.548696
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_arr = ['a', 'b', 'c']
    test_sequence = _DeprecatedSequenceConstant(test_arr, 'test message', 'test version')
    assert len(test_sequence) == len(test_arr)
    assert test_sequence[0] == test_arr[0]

# Generated at 2022-06-22 11:21:15.272263
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    sequence = _DeprecatedSequenceConstant([1, 2, 3], 'msg', '1.9')
    assert len(sequence) == 3


# Generated at 2022-06-22 11:21:24.430052
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "This is a deprecated message"
    version = "1.0"
    value = [1, 2, 3]
    DSC = _DeprecatedSequenceConstant(value, msg, version)
    assert len(DSC) == len(value)
    assertion_error = False
    try:
        assert list(DSC) == list(value)
    except AssertionError:
        assertion_error = True
    assert assertion_error
    assert DSC[2] == value[2]
    assertion_error = False
    try:
        assert list(DSC[1:]) == list(value[1:])
    except AssertionError:
        assertion_error = True
    assert assertion_error

# Generated at 2022-06-22 11:21:26.613194
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    c = _DeprecatedSequenceConstant([], '', '')
    assert c[0] == []

# Generated at 2022-06-22 11:21:35.922249
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    obj = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert obj[0] == 1
    assert obj[1] == 2
    assert obj[2] == 3


# Generated at 2022-06-22 11:21:40.098557
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_deprecated = _DeprecatedSequenceConstant(value=('first', 'second'), msg='test message', version='2.9')
    assert len(test_deprecated) == 2
    assert test_deprecated[1] == 'second'

# Generated at 2022-06-22 11:21:44.619570
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_constant = _DeprecatedSequenceConstant(
        ['test', 'me'],
        "have a test",
        "ansible 2.11"
    )
    assert len(test_constant) == 2
    assert test_constant[0] == 'test'

# Generated at 2022-06-22 11:21:48.175426
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dc = _DeprecatedSequenceConstant('abcd', 'test_msg', '1.2.3')
    assert len(dc) == 4
    assert dc[0] == 'a'
    assert dc[1] == 'b'


# Generated at 2022-06-22 11:21:59.007535
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import unittest
    import sys

    class __DeprecatedSequenceConstant_Test(unittest.TestCase):
        def test_case(self):
            from ansible.constants import _DeprecatedSequenceConstant
            from ansible.utils.display import Display
            d = Display()

            value = [1, 2, 3]
            msg = 'test'
            version = '2.9'
            obj = _DeprecatedSequenceConstant(value, msg, version)

            self.assertEqual(obj[0], 1)
            self.assertEqual(obj[1], 2)
            self.assertEqual(obj[2], 3)

            d._display.seek(0)

# Generated at 2022-06-22 11:22:05.291188
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    def test_getitem(value, expected_output, msg, version):
        actual_output = _DeprecatedSequenceConstant(value, msg, version).__getitem__(0)
        assert actual_output == expected_output, \
            "'{0}' should return the following value: '{1}', but it returned '{2}'".format(msg, expected_output, actual_output)

    test_getitem(['a', 'b', 'c'], 'a', 'testing warning message in _DeprecatedSequenceConstant', '2.0')


# Generated at 2022-06-22 11:22:07.376121
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert _DeprecatedSequenceConstant((1, 2, 3), 'msg', 'ver').__len__() == 3

# Generated at 2022-06-22 11:22:17.982375
# Unit test for constructor of class _DeprecatedSequenceConstant

# Generated at 2022-06-22 11:22:25.324711
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_NOCOLOR.startswith('{{')
    assert ANSIBLE_NOCOLOR.endswith('}}')
    assert not ANSIBLE_NOCOLOR
    assert ANSIBLE_SSH_RETRIES > 3

# apply deprecation warnings

# Generated at 2022-06-22 11:22:29.417428
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    c = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert len(c) == 3
    assert c[0] == 1
    assert c[1] == 2
    assert c[2] == 3

# Generated at 2022-06-22 11:22:41.455884
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_sequence = _DeprecatedSequenceConstant([1,2,3], "Message", "2.9")
    assert len(test_sequence) == 3


# Generated at 2022-06-22 11:22:43.813751
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(('abc', 'def'), 'msg', '2.2')) == 2


# Generated at 2022-06-22 11:22:46.324277
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant([], "test message", "test version")

if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:22:49.862459
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    sequence = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', '1.2.3')
    assert len(sequence) == 3

# Generated at 2022-06-22 11:23:02.581159
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    __test_value_1__ = None
    __test_msg_1__ = None
    __test_version_1__ = None
    __test_value_2__ = ['a']
    __test_msg_2__ = None
    __test_version_2__ = None
    __test_value_3__ = ['a', 'b', 'c']
    __test_msg_3__ = None
    __test_version_3__ = None
    __test_value_4__ = [1, 2, 3, 4]
    __test_msg_4__ = None
    __test_version_4__ = None


# Generated at 2022-06-22 11:23:07.175992
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant([1, 2, 3], u'', u'')
    assert constant[0] == 1
    assert constant[1] == 2
    assert constant[2] == 3
    assert len(constant) == 3



# Generated at 2022-06-22 11:23:11.257936
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dsc = _DeprecatedSequenceConstant(value=[1, 2, 3], msg="TEST", version="VERSION")
    assert dsc[0] == 1
    assert dsc[1] == 2
    assert dsc[2] == 3

# Generated at 2022-06-22 11:23:21.318436
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # pylint: disable=invalid-name
    def force_unicode(val):
        """
        Ensure a value is unicode
        """
        if isinstance(val, bytes):
            val = to_text(val)
        return val

    # "test" is a proxy for the actual function being tested
    test = _DeprecatedSequenceConstant

    # Assert that sequences of 2 elements are acceptable
    assert test(['abc', 'def'], 'am a message', '1.3') == ['abc', 'def']

    # Assert that sequences of two elements, one of which is None, are acceptable
    assert test(['abc', None], 'am a message', '1.3') == ['abc', None]

    # Assert that sequences of 3 elements are acceptable

# Generated at 2022-06-22 11:23:22.607507
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant((1,2,3), 'bar', '1.2')) == 3

# Generated at 2022-06-22 11:23:27.121517
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    import unittest
    from collections import Sequence

    class Test__DeprecatedSequenceConstant(unittest.TestCase):
        def test_len(self):
            msg = 'testing length'
            version = 'this.version'
            def_val = [1, 2, 3]
            dc = _DeprecatedSequenceConstant(def_val, msg, version)
            self.assertIsInstance(dc, Sequence)
            self.assertIs(type(def_val), type(dc))
            self.assertEqual(len(def_val), len(dc))

    suite = unittest.TestSuite()
    suite.addTest(Test__DeprecatedSequenceConstant('test_len'))
    unittest.TextTestRunner().run(suite)



# Generated at 2022-06-22 11:23:49.959414
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant((7,8), "msg", "2.0")) == 2


# Generated at 2022-06-22 11:23:53.032063
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    c = _DeprecatedSequenceConstant([i for i in range(10)], 'msg', 'version')
    assert c[0] == 0
    assert c[-1] == 9


# Generated at 2022-06-22 11:23:55.880525
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    x = _DeprecatedSequenceConstant([1, 2, 3], "msg", "version")
    assert len(x) == 3, "_DeprecatedSequenceConstant's method __len__ failed"

# Generated at 2022-06-22 11:23:59.833232
# Unit test for function set_constant
def test_set_constant():
    # Test is_empty()
    if not isinstance(DEFAULT_BECOME_PASS, string_types):
        raise AssertionError("Invalid DEFAULT_BECOME_PASS: %s" % repr(DEFAULT_BECOME_PASS))

# Generated at 2022-06-22 11:24:06.800162
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    obj_1 = _DeprecatedSequenceConstant(['one', 'two'], 'this is a test', '2.10')
    obj_2 = _DeprecatedSequenceConstant((1, 2), 'this is a test', '2.10')
    assert obj_1[0] == 'one' and obj_1[1] == 'two'
    assert obj_2[0] == 1 and obj_2[1] == 2


# Generated at 2022-06-22 11:24:09.341979
# Unit test for function set_constant
def test_set_constant():
    d = {}
    set_constant('foo', 'bar', export=d)
    assert d['foo'] == 'bar'


# unit test for function _warning

# Generated at 2022-06-22 11:24:13.622890
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'this is test message'
    version = '2.8'
    sequence = _DeprecatedSequenceConstant(msg, _msg, version)
    assert sequence[0] == msg


# Generated at 2022-06-22 11:24:15.970549
# Unit test for function set_constant
def test_set_constant():
    c = {}
    set_constant('test', 'test', c)
    assert c['test'] == 'test'



# Generated at 2022-06-22 11:24:19.360657
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    msg = 'msg'
    version = 'version'
    value = ['array']
    a = _DeprecatedSequenceConstant(value, msg, version)
    assert len(a) == len(value)



# Generated at 2022-06-22 11:24:27.053063
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    """ _DeprecatedSequenceConstant[index] should return the value at index."""
    value = ("a", "b", "c", "d")
    depr = _DeprecatedSequenceConstant(value, "msg", "version")

    assert depr.__getitem__(0) == "a"
    assert depr.__getitem__(1) == "b"
    assert depr.__getitem__(3) == "d"
    assert depr.__getitem__(-1) == "d"
    assert depr.__getitem__(-2) == "c"
    assert depr.__getitem__(-4) == "a"


# Generated at 2022-06-22 11:24:55.289325
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    sequence = _DeprecatedSequenceConstant([], '', '')
    assert len(sequence) == 0
    sequence = _DeprecatedSequenceConstant([1, 2, 3], '', '')
    assert len(sequence) == 3


# Generated at 2022-06-22 11:25:02.517627
# Unit test for function set_constant
def test_set_constant():
    assert not config.config_file
    assert config.config_file == C.config_file
    assert config.config_file == DEFAULT_CONFIG_FILE
    assert config.config_file == '/etc/ansible/ansible.cfg'

# FIXME: remove this once all the uses of this are gone
SSHPASS_AVAILABLE = True

# Use the ANSIBLE_TF_* vars to override defaults in the AnsibleConfig class
for env_var in os.environ:
    if env_var.startswith('ANSIBLE_'):
        varname = env_var[8:]
        if varname == 'HOST_KEY_CHECKING':
            varname = 'HOST_KEY_CHECKING'
        if varname == 'TF_LOG':
            varname = 'LOG_PATH'

# Generated at 2022-06-22 11:25:04.461818
# Unit test for function set_constant
def test_set_constant():
    assert vars()['DEFAULT_BECOME_PASS'] == DEFAULT_BECOME_PASS

# Generated at 2022-06-22 11:25:06.312993
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant([1, 2, 3], "msg", "2.6")

# Generated at 2022-06-22 11:25:10.447319
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_value = ['one', 'two']
    test_msg = "This sequence constant is deprecated"
    test_version = "2.8"
    test_obj = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert len(test_obj) == 2

# Generated at 2022-06-22 11:25:19.313319
# Unit test for function set_constant
def test_set_constant():
    namespace = {}
    set_constant('foo', 'fooval', namespace)
    assert 'foo' in namespace
    assert namespace['foo'] == 'fooval'


# TODO: remove the following once config is handled entirely via settings
#       and these are all defined in config, similiar to ANSIBLE_FORKS

ANSIBLE_HOST_PATTERN_MATCH = config.get_config_value('host_pattern_match')
ANSIBLE_RETRY_FILES_ENABLED = config.get_config_value('retry_files_enabled')
ANSIBLE_RETRY_FILES_SAVE_PATH = config.get_config_value('retry_files_save_path')
ANSIBLE_KEEP_REMOTE_FILES = config.get_config_value('keep_remote_files')
ANSIBLE_LOCAL_

# Generated at 2022-06-22 11:25:27.408712
# Unit test for function set_constant
def test_set_constant():
    # Construct an options dict
    test_options = {
        'action_plugins': 'plugins/actions',
        'connection_plugins': 'plugins/connections',
        'library': 'library',
        'module_lang': 'C.UTF-8',
        'module_name': 'module_name',
        'module_path': 'module_path',
        'module_utils': 'module_utils',
        'filter_plugins': 'plugins/filters',
        'lookup_plugins': 'plugins/lookup',
        'on_failed': 'on_failed',
        'on_unreachable': 'on_unreachable',
        'on_skipped': 'on_skipped',
        'ssh_args': 'ssh_args',
        'tree': 'tree'
    }

    # Set the constants

# Generated at 2022-06-22 11:25:37.987805
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    '''Test to make sure sequences can be wrapped in a _DeprecatedSequenceConstant'''
    value = ['ansible.server.controller', 'ansible.server.controller.api']
    msg = 'ansible.server.controller plugins are deprecated'
    version = '2.10'

    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert isinstance(dsc, Sequence)
    assert len(dsc) == 2
    assert dsc[0] == 'ansible.server.controller'
    assert dsc[1] == 'ansible.server.controller.api'
    assert dsc.__ini__ == value
    assert dsc.__msg__ == 'ansible.server.controller plugins are deprecated'
    assert dsc.__version__ == '2.10'



# Generated at 2022-06-22 11:25:41.625937
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant([1, 2, 3], 'Warning message', '2.10')
    assert len(a) == 3

# Generated at 2022-06-22 11:25:43.726647
# Unit test for function set_constant
def test_set_constant():
    assert vars()['DEFAULT_UNDEFINED_VAR_BEHAVIOR'] == 'warn'
    assert vars()[''] == 'warn'



# Generated at 2022-06-22 11:26:24.076509
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    '''
    unit test for __getitem__ method on _DeprecatedSequenceConstant class
    '''
    msg = 'message'
    version = '1.2.3'

    sequence = _DeprecatedSequenceConstant((1, 2, 3), msg, version)
    assert sequence[0] == 1
    assert sequence[1] == 2
    assert sequence[2] == 3


# Generated at 2022-06-22 11:26:30.966386
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_CONSTANT', 'TEST_CONSTANT', export=globals())
    assert 'TEST_CONSTANT' in globals() and globals()['TEST_CONSTANT'] == 'TEST_CONSTANT'


# FIXME: de-facto deprecated, remove in 2.11
DEFAULT_MODULE_NAME = _DeprecatedSequenceConstant(('command', 'win_command'),
                                                  'DEFAULT_MODULE_NAME has been deprecated, use MODULE_REQUIRE_ARGS instead',
                                                  '2.11')

# FIXME: de-facto deprecated, remove in 2.11

# Generated at 2022-06-22 11:26:41.118591
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    '''
    tests method __len__ of class _DeprecatedSequenceConstant
    '''
    dsc = _DeprecatedSequenceConstant(list(range(10)), 'msg', 'version')
    assert len(dsc) == 10

    for item in dsc:
        pass

    # testing deprecated

# Generated at 2022-06-22 11:26:44.478242
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a_list = [1, 2, 3]
    a_constant = _DeprecatedSequenceConstant(a_list, "msg", "version")
    assert len(a_list) == len(a_constant)


# Generated at 2022-06-22 11:26:46.584930
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant([1, 2, 3], msg='w', version='v')[1] == 2


# Generated at 2022-06-22 11:26:53.197385
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    myconst = _DeprecatedSequenceConstant(value=['test1','test2','test3'],msg='This is a test message',version='2.9')
    assert myconst._value == ['test1','test2','test3'] and myconst._msg == 'This is a test message' and myconst._version == '2.9'

# Generated at 2022-06-22 11:26:55.470932
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('test_key', 'test_value', export)
    assert export == {'test_key': 'test_value'}

# Generated at 2022-06-22 11:26:59.189727
# Unit test for function set_constant
def test_set_constant():

    set_constant('ANSIBLE_MODULE_ARGS', '{"foo": "bar"}')
    assert ANSIBLE_MODULE_ARGS == {"foo": "bar"}
    assert ANSIBLE_MODULE_ARGS['foo'] == "bar"


# Generated at 2022-06-22 11:27:02.083204
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(list(), "", "")) == 0
    assert len(_DeprecatedSequenceConstant(list([1, 2, 3]), "", "")) == 3


# Generated at 2022-06-22 11:27:06.091819
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    d = _DeprecatedSequenceConstant(('a', 'b'), 'Deprecated', '2.9')
    assert d[0] == 'a'
    assert d[1] == 'b'
    with pytest.raises(TypeError):
        d[1:2]


# Generated at 2022-06-22 11:28:20.234634
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    _DeprecatedSequenceConstant([0, 1], "test_key1", "test_version1")
    assert len([]) == 0


# Generated at 2022-06-22 11:28:28.708810
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Test case 1
    try:
        x = _DeprecatedSequenceConstant()
    except Exception as e:
        assert True
    else:
        assert False

    # Test case 2
    try:
        x = _DeprecatedSequenceConstant(frozenset([]))
    except Exception as e:
        assert True
    else:
        assert False

    # Test case 3
    try:
        x = _DeprecatedSequenceConstant(frozenset([]), 'test msg', '2.1')
    except Exception as e:
        assert True
    else:
        assert False

    # Test case 4
    test_obj = _DeprecatedSequenceConstant(frozenset([]), 'test msg', '3.0')
    assert test_obj._value == frozenset([]) and test_obj

# Generated at 2022-06-22 11:28:31.171084
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    sequence_test = _DeprecatedSequenceConstant([1,2,3], 'some warning', 'some version')
    assert len(sequence_test) == 3

# Generated at 2022-06-22 11:28:40.847865
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import copy

    # test that copying a _DeprecatedSequenceConstant object produces a
    # _DeprecatedSequenceConstant object
    data = ['yes', 'no', 'maybe', 'so']
    msg = 'msg'
    version = '0.0'
    obj = _DeprecatedSequenceConstant(data, msg, version)
    other = _DeprecatedSequenceConstant(data, msg, version)
    assert isinstance(obj, _DeprecatedSequenceConstant)
    assert isinstance(other, _DeprecatedSequenceConstant)
    assert copy.copy(obj) is obj
    assert copy.deepcopy(obj) is obj
    assert obj == other
    assert hash(obj) == hash(other)
    assert id(obj) == id(other)

    # test that _DeprecatedSequenceConstant objects with the

# Generated at 2022-06-22 11:28:47.508280
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test if _DeprecatedSequenceConstant can handle list
    assert len(_DeprecatedSequenceConstant(['a', 'b'], 'msg', 'version')) == 2
    # Test if _DeprecatedSequenceConstant can handle tuple
    assert len(_DeprecatedSequenceConstant(('a', 'b'), 'msg', 'version')) == 2
    # Test if _DeprecatedSequenceConstant can handle dict
    assert len(_DeprecatedSequenceConstant({'a', 'b'}, 'msg', 'version')) == 2


# Generated at 2022-06-22 11:28:49.833171
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    obj = _DeprecatedSequenceConstant([1, 2, 3], 'message', 'version')
    assert len(obj) == 3
    for i in range(4):
        assert obj[i - 3] == i



# Generated at 2022-06-22 11:28:52.233001
# Unit test for function set_constant
def test_set_constant():
    set_constant('CONSTANT_TEST', 'constTest')
    assert 'CONSTANT_TEST' in globals()


# Generated at 2022-06-22 11:28:56.278586
# Unit test for function set_constant
def test_set_constant():
    '''
    set_constant is called from the config manager and creates a constant
    from it, the CONSTANT value should be a copy of the value
    '''
    my_constant = 'value'
    set_constant('CONSTANT', my_constant)
    my_constant = my_constant + '_changed'
    assert CONSTANT == 'value'

# Generated at 2022-06-22 11:29:05.604660
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('test_constant', 'constant_value', export)
    set_constant('test_number', 3, export)
    set_constant('test_dict', {'test_key1': 'val1', 'test_key2': 'val2'}, export)
    set_constant('test_list', ['test_val1', 'test_val2'], export)
    set_constant('test_bool', True, export)

    assert export['test_constant'] == 'constant_value'
    assert export['test_number'] == 3
    assert export['test_dict'] == {'test_key1': 'val1', 'test_key2': 'val2'}
    assert export['test_list'] == ['test_val1', 'test_val2']
   

# Generated at 2022-06-22 11:29:12.006142
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    myvalue = _DeprecatedSequenceConstant(value='myvalue', msg='mymsg', version='myversion')
    assert myvalue['0'] == 'm'
    assert myvalue['1'] == 'y'
    assert myvalue['2'] == 'v'
    assert myvalue['3'] == 'a'
    assert myvalue['4'] == 'l'
    assert myvalue['5'] == 'u'
    assert myvalue['6'] == 'e'
