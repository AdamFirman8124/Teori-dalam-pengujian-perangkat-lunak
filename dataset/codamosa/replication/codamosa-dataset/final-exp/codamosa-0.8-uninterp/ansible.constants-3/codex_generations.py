

# Generated at 2022-06-22 11:19:23.569851
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant([1, 2], 'foo', 'bar')
    assert seq._value == [1, 2]
    assert seq._msg == 'foo'
    assert seq._version == 'bar'

# Generated at 2022-06-22 11:19:27.186900
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = u"This is a test."
    version = "version"
    value = list(range(10))

    c = _DeprecatedSequenceConstant(value, msg, version)
    assert c[3] == 3


# Generated at 2022-06-22 11:19:30.048329
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert isinstance(_DeprecatedSequenceConstant(value=(), version='2.8', msg="msg"), _DeprecatedSequenceConstant)
    assert len(_DeprecatedSequenceConstant(value=(), version='2.8', msg="msg")) == 0


# Generated at 2022-06-22 11:19:36.159901
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dsc_with_list = _DeprecatedSequenceConstant(['a','b','c'],'','1')
    assert dsc_with_list[0] == 'a'
    assert dsc_with_list[1] == 'b'
    assert dsc_with_list[2] == 'c'


# Generated at 2022-06-22 11:19:41.037430
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'foo'
    version = '2.0'
    value = ['foo', 'bar']
    constant = _DeprecatedSequenceConstant(value, msg, version)
    assert constant[0] == 'foo'
    assert constant[1] == 'bar'



# Generated at 2022-06-22 11:19:46.875879
# Unit test for function set_constant
def test_set_constant():
    ''' function set_constant should create constants from config '''
    from ansible.constants import DEFAULT_MODULE_NAME, DEFAULT_MODULE_PATH

    assert DEFAULT_MODULE_NAME
    assert DEFAULT_MODULE_PATH


# Restore values with types that may have been mangled by ConfigManager
TRANSPORT = 'smart'
VAULT_VERSION = 1.0

# Generated at 2022-06-22 11:19:51.347544
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    obj = _DeprecatedSequenceConstant(value=[1, 2, 3], msg='test', version='2.9')
    assert obj[0] == 1
    assert obj[1] == 2
    assert obj[2] == 3


# Generated at 2022-06-22 11:20:04.065924
# Unit test for function set_constant
def test_set_constant():
    assert __version__ == '2.3.1.0'

# Generated at 2022-06-22 11:20:14.557572
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('FOO', 1, export)
    assert(export['FOO'] == 1)

# This is used after parsing the command line in order to kill off certain
# tasks.  The dictionary below has tasks that become noops as keys, and
# values indicating the deprecation messages.

# Generated at 2022-06-22 11:20:23.697146
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class MockWarning:
        def __init__(self):
            self.msg = None
            self.version = None

        def deprecated(self, msg, version):
            self.msg = msg
            self.version = version

    mock_warn = MockWarning()
    seq = _DeprecatedSequenceConstant((1, 2), 'test msg', 'version')
    seq._deprecated = mock_warn.deprecated

    assert seq[0] == 1
    assert seq._deprecated.msg == 'test msg'
    assert seq._deprecated.version == 'version'
    assert seq[-1] == 2
    assert seq[1] == 2
    assert seq[2] == 3
    assert seq[-2] == 1

# Generated at 2022-06-22 11:20:28.253103
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    x = _DeprecatedSequenceConstant('abc','Deprecating','2.13')
    assert len(x) == 3

# Generated at 2022-06-22 11:20:32.171536
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dc = _DeprecatedSequenceConstant([], "msg", "version")
    assert len(dc) == 0


# Generated at 2022-06-22 11:20:45.066933
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_CONSTANT', 5)
    assert(TEST_CONSTANT == 5)
    try:
        set_constant('TEST_CONSTANT', 10, export=locals())
    except AssertionError:
        assert(True)
    assert(TEST_CONSTANT == 5)



# Generated at 2022-06-22 11:20:48.869134
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert len(_DeprecatedSequenceConstant(tuple(), 'tuple', '0.0')) == 0
    assert _DeprecatedSequenceConstant((1, 2), 'tuple', '0.0')[0] == 1

# Generated at 2022-06-22 11:20:54.068297
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    c = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'bad bad bad', '6.1')
    assert len(c) == 3
    assert c[0] == 'a'
    assert c[1] == 'b'
    assert c[2] == 'c'

# Generated at 2022-06-22 11:20:57.078701
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    """
    @return: None
    """
    seq = _DeprecatedSequenceConstant(['foo', 'bar'], "msg", "1.1")
    assert seq[0] == 'foo'
    assert seq[1] == 'bar'

# Generated at 2022-06-22 11:21:08.429613
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    from ansible.errors import AnsibleDeprecationWarning
    from ansible.module_utils.six import PY3

    # test_deprecated_constant_without_deprecation_warning
    constant = _DeprecatedSequenceConstant([], '', '')
    assert len(constant) == 0

    # test_deprecated_constant_with_deprecation_warning
    constant = _DeprecatedSequenceConstant([], '', '2.10')
    if PY3:
        warnings_manager = warnings.catch_warnings(record=True)
        warnings_manager.__enter__()
    else:
        warnings.simplefilter('always', AnsibleDeprecationWarning)
    assert len(constant) == 0
    if PY3:
        warnings_manager.__exit__(None, None, None)


# Generated at 2022-06-22 11:21:14.493359
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    v = ['test__DeprecatedSequenceConstant___len__']
    msg = 'test__DeprecatedSequenceConstant___len__'
    version = 'test__DeprecatedSequenceConstant___len__'
    dsc = _DeprecatedSequenceConstant(v, msg, version)
    assert len(dsc) == 1

# Generated at 2022-06-22 11:21:19.487476
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test simple case
    dsc = _DeprecatedSequenceConstant(
        [1, 2, 3],
        "This is a test",
        "2.9"
    )
    assert dsc[0] == 1
    # Test out of range index
    try:
        assert dsc[4]
    except IndexError:
        pass


# Generated at 2022-06-22 11:21:24.772623
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    generator = _DeprecatedSequenceConstant((1, 2, 3), "Deprecated message", "2.0")
    assert isinstance(generator, Sequence)
    assert len(generator) == 3
    assert generator[0] == 1
    assert generator[1] == 2
    assert generator[2] == 3
    assert repr(generator) == repr((1, 2, 3))

# Generated at 2022-06-22 11:21:33.827743
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = _DeprecatedSequenceConstant(['one', 'two', 'three'], 'testing', 'a long time ago')
    assert seq[0] == 'one'
    assert seq[1] == 'two'
    assert seq[2] == 'three'

# Generated at 2022-06-22 11:21:38.533495
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    obj_seq = _DeprecatedSequenceConstant(CONFIGURABLE_PLUGINS, 'msg', 'version')
    assert len(obj_seq) == len(CONFIGURABLE_PLUGINS)
    for index, item in enumerate(CONFIGURABLE_PLUGINS):
        assert obj_seq[index] == item

# Generated at 2022-06-22 11:21:43.949299
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # __getitem__ should warn when key is present and return value
    c = _DeprecatedSequenceConstant(value={'toto' : 'titi'}, msg="plop", version="2.12")
    assert c['toto'] == 'titi'
    # __getitem__ should warn when key is missing and raise correct exception
    c = _DeprecatedSequenceConstant(value={'toto' : 'titi'}, msg="plop", version="2.12")
    try:
        c['tata']
    except KeyError:
        pass
    else:
        assert False



# Generated at 2022-06-22 11:21:46.128283
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    from ansible.module_utils.common.collections import Sequence
    assert isinstance(_DeprecatedSequenceConstant([], '', ''), Sequence)

# Generated at 2022-06-22 11:21:51.078214
# Unit test for function set_constant
def test_set_constant():
    test_dict = {}
    _test_value = 'test'
    _name = 'test_name'
    set_constant(_name, _test_value, export=test_dict)
    assert test_dict['test_name'] == _test_value



# Generated at 2022-06-22 11:21:53.132210
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert isinstance(_DeprecatedSequenceConstant(['command', 'shell'], 'this is deprecated', '1.0'), Sequence)

# Generated at 2022-06-22 11:21:58.024355
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    for value in (tuple(), ('A', 'B', 'C'), range(10, 20)):
        for msg in ('message', ''):
            for version in ('2.0', '2.1'):
                deprecated_obj = _DeprecatedSequenceConstant(value, msg, version)
                assert value == deprecated_obj._value
                assert msg == deprecated_obj._msg
                assert version == deprecated_obj._version
                assert value == deprecated_obj
                assert tuple(value) == deprecated_obj
                assert isinstance(deprecated_obj, tuple)
                assert isinstance(deprecated_obj, Sequence)


# Generated at 2022-06-22 11:22:06.580563
# Unit test for function set_constant
def test_set_constant():
    set_constant('a', 'A')
    set_constant('b', 'B')
    set_constant('c', ['C'], export=globals())
    set_constant('d', 'D')
    set_constant('e', ['E'], export=globals())
    set_constant('f', 'F', export=globals())
    set_constant('g', 'G')
    set_constant('h', ['H'])
    set_constant('i', 'I')
    set_constant('j', 'J')
    set_constant('k', 'K')
    set_constant('l', ['L'], export=globals())
    set_constant('m', 'M')
    set_constant('n', ['N'])
    set

# Generated at 2022-06-22 11:22:12.484475
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant(set(['a', 'b']), "Some message", "2.0")
    assert len(seq) == 2
    assert seq[0] == 'a'
    assert seq[1] == 'b'
    assert ('a' in seq) is True
    assert ('c' in seq) is False
    assert ('a' not in seq) is False
    assert ('c' not in seq) is True

# Generated at 2022-06-22 11:22:15.255585
# Unit test for function set_constant
def test_set_constant():
    local = {}
    set_constant("CONSTANT", "Success", export=local)
    assert local["CONSTANT"] == "Success"

# Generated at 2022-06-22 11:22:30.616507
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    import itertools
    obj = _DeprecatedSequenceConstant([1], 'msg', 'ver')
    for i1, i2 in itertools.izip(reversed(range(10)), obj):
        assert i1 == i2
    assert len(obj) == 10

# Generated at 2022-06-22 11:22:39.548166
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.constants import _DeprecatedSequenceConstant

    # Test _DeprecatedSequenceConstant class when given a value that is not a list
    # In this case we expect the value to be returned
    assert isinstance(_DeprecatedSequenceConstant('test-value', 'non-list-msg', '1.0'), string_types)

    # Test _DeprecatedSequenceConstant class when given a value that is not a list
    # In this case we expect the first value in the list to be returned
    result = _DeprecatedSequenceConstant(['first-item', 'second-item'], 'list-msg', '1.0')
    assert isinstance(result, string_types)
    assert result == 'first-item'

# Generated at 2022-06-22 11:22:44.610762
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = ['paris', 'berlin', 'copenhagen']
    msg = 'This is a warning message'
    version = '2.8'
    dep_seq_cons = _DeprecatedSequenceConstant(value, msg, version)

    assert len(dep_seq_cons) == len(value)


# Generated at 2022-06-22 11:22:55.101553
# Unit test for function set_constant
def test_set_constant():
    module_langs = ['c', 'cpp', 'csharp', 'go', 'java', 'javascript', 'lua', 'perl', 'php', 'python', 'ruby', 'rust', 'scala']
    # Test _multiple_configs
    set_constant("DEFAULT_MODULE_LANG", module_langs)
    assert DEFAULT_MODULE_LANG == add_internal_fqcns(module_langs)
    set_constant("DEFAULT_MODULE_LANG", "go")
    assert DEFAULT_MODULE_LANG == add_internal_fqcns(("go", ))
    set_constant("DEFAULT_MODULE_LANG", "go", export={'haha': 'hehe'})

# Generated at 2022-06-22 11:23:04.979372
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = "The 'host_key_checking' option is deprecated. " \
          "Use 'host_key_auto_add' instead."
    msg_exp = " [DEPRECATED] The 'host_key_checking' option is deprecated. " \
              "Use 'host_key_auto_add' instead., to be removed in 2.11"
    version = '2.11'
    value = [1, 2, 3]
    a = _DeprecatedSequenceConstant(value, msg, version)
    len_a = len(a)
    len_b = len(value)

    assert len_a == len_b
    assert msg_exp in a._msg


# Generated at 2022-06-22 11:23:15.916391
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant("FOO", "BAR", export)
    assert export['FOO'] == 'BAR'
    assert globals()['FOO'] == 'BAR'


# this is used in the config and inventory scripts

# Generated at 2022-06-22 11:23:21.449376
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    sequence_constant = _DeprecatedSequenceConstant(value=[1, 2, 3], msg='foo', version='1.2.3')
    assert sequence_constant[0] == 1
    assert sequence_constant[1] == 2
    assert sequence_constant[2] == 3


# Generated at 2022-06-22 11:23:32.495135
# Unit test for function set_constant
def test_set_constant():
    for setting in config.data.get_settings():
        assert setting.name in globals()


# AUTOMATIC POPULATE AND IDEMPOTENCY CHECK ###

# blacklist of settings that should not be automatically added
# to the global constants dictionary

# Generated at 2022-06-22 11:23:37.400606
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test = _DeprecatedSequenceConstant(('test1','test2','test3'),'This is deprecated','2.9')
    assert isinstance(test, _DeprecatedSequenceConstant)
    assert test[0] == 'test1'
    assert test[1] == 'test2'
    assert test[2] == 'test3'
    assert len(test) == 3

# Generated at 2022-06-22 11:23:39.407601
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = [1, 2]
    dep_seq = _DeprecatedSequenceConstant(value, 'msg', 'version')
    assert len(dep_seq) == 2

# Generated at 2022-06-22 11:24:04.989020
# Unit test for function set_constant
def test_set_constant():
    assert HOST_KEY_CHECKING == u'False'

    set_constant('TEST_SET_CONSTANT', True)
    assert TEST_SET_CONSTANT == True


# Generated at 2022-06-22 11:24:07.115849
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    obj = _DeprecatedSequenceConstant(1, 1, 1)
    assert len(obj) == 1

# Generated at 2022-06-22 11:24:18.716282
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant(('a', 'b'), 'This is deprecated', '2.9')._value == ['a', 'b']
    assert _DeprecatedSequenceConstant(['a', 'b'], 'This is deprecated', '2.9')._value == ['a', 'b']
    assert _DeprecatedSequenceConstant('ab', 'This is deprecated', '2.9')._value == 'ab'



# Generated at 2022-06-22 11:24:23.421358
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    c = _DeprecatedSequenceConstant(value='12345', msg='you should not use this', version='2.0')
    assert c[0] == '1'
    assert c[1] == '2'
    assert c[2] == '3'
    assert c[3] == '4'
    assert c[4] == '5'
    assert len(c) == 5

# Generated at 2022-06-22 11:24:26.363704
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    sc = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert len(sc) == 3


# Generated at 2022-06-22 11:24:37.811439
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant(value="foo", msg="A warning message", version="2.0")
    assert constant._value == "foo"
    assert constant._msg == "A warning message"
    assert constant._version == "2.0"
    assert constant.__len__() == 3
    assert constant.__getitem__(1) == "o"



# Temporary aliases until 2.10
set_constant('DEFAULT_LOOP_FILTER_TEMPLATE', "{{ '%s' if %s is defined else %s }}")
set_constant('DEFAULT_TASK_FILTER_TEMPLATE', "{{ '%s' if %s is defined else %s }}")

# Generated at 2022-06-22 11:24:45.620171
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    sequence_constant = _DeprecatedSequenceConstant((0, 1, 2), 'msg', 'version')

    # slice
    slice_constant = sequence_constant[0:2]
    assert isinstance(slice_constant, _DeprecatedSequenceConstant)
    assert slice_constant._value == (0, 1)
    assert slice_constant._msg == 'msg'
    assert slice_constant._version == 'version'

    # int
    int_constant = sequence_constant[0]
    assert isinstance(int_constant, int)
    assert int_constant == 0
    

# Generated at 2022-06-22 11:24:46.365620
# Unit test for function set_constant
def test_set_constant():
    assert raw_shell


# Generated at 2022-06-22 11:24:50.762808
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = 'msg'
    version = 'version'
    lst = [1, 2, 3]
    obj = _DeprecatedSequenceConstant(lst, msg, version)
    assert len(lst) == len(obj)
    assert lst[0] == obj[0]


# Generated at 2022-06-22 11:24:53.494498
# Unit test for function set_constant
def test_set_constant():
    result = {}
    set_constant('name', 'value', result)
    assert result['name'] == 'value'

# Generated at 2022-06-22 11:25:15.462150
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_const = _DeprecatedSequenceConstant(u'value', u'message', u'1.2.3')
    assert test_const[0] == u'v'


# Generated at 2022-06-22 11:25:22.381530
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    bad_name = 'bad_name'
    bad_value = 'bad_value'
    version = 'version_value'
    msg = "use of deprecated configuration '{}' will be removed in version {}".format(bad_name, version)
    assert (_DeprecatedSequenceConstant(bad_value, msg, version)._value == bad_value)
    assert (_DeprecatedSequenceConstant(bad_value, msg, version)._msg == msg)
    assert (_DeprecatedSequenceConstant(bad_value, msg, version)._version == version)

# Generated at 2022-06-22 11:25:25.785515
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant([1, 2, 3], 'test False', '2.4')
    assert constant[1] == 2
    constant[1] == 2
    assert len(constant) == 3

# Generated at 2022-06-22 11:25:36.858386
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import sys
    from errno import EPIPE

    original_stderr = sys.stderr

# Generated at 2022-06-22 11:25:43.796041
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    def _test_helper(msg, version):
        d = _DeprecatedSequenceConstant([1], msg, version)
        # Test method __len__ of class _DeprecatedSequenceConstant with a list and a message
        assert(len(d) == 1)

    # Test method __len__ of class _DeprecatedSequenceConstant with a list and a message
    _test_helper('test_message', '1.2')

# Generated at 2022-06-22 11:25:49.035419
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_msg = 'msg'
    test_version = 'version'
    test_value = [1, 2, 3]
    t = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert t._value == test_value
    assert t._msg == test_msg
    assert t._version == test_version

# Generated at 2022-06-22 11:25:59.001356
# Unit test for function set_constant
def test_set_constant():
    # Test for setting constant
    set_constant('TESTING_CONSTANT', 'VALUE')
    assert 'TESTING_CONSTANT' in vars()

    # Test for setting constant, while failing
    try:
        set_constant('TESTING_CONSTANT', 'VALUE')
    except ValueError:
        assert True

    # Test for setting constant in a different export
    export = {}
    set_constant('TESTING_CONSTANT', 'VALUE', export=export)
    assert 'TESTING_CONSTANT' in export

# ---- other global constants ---- #
DEFAULT_ASK_BECOME_PASS = False
DEFAULT_ASK_PASS = False
DEFAULT_HOST_LIST = '/etc/ansible/hosts'
DEFAULT_KEEP_REMOTE_FILES = True

# Generated at 2022-06-22 11:26:03.644743
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test for _DeprecatedSequenceConstant().__getitem__(index)
    dsc = _DeprecatedSequenceConstant(['a', 'b', 'c', 'd'], 'msg', 'version')
    assert dsc[0] == 'a'
    assert dsc[-1] == 'd'
    assert dsc[-2] == 'c'



# Generated at 2022-06-22 11:26:12.829861
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    """Check that _DeprecatedSequenceConstant(value, msg, version).__getitem__(key) return value[key].
    >>> test__DeprecatedSequenceConstant___getitem__()
    """
    from ansible.module_utils.common.collections import Sequence
    from ansible.module_utils.six import text_type

    value = 'test'
    msg = 'This is a test'
    version = '2.8'

    v = _DeprecatedSequenceConstant(value, msg, version)
    assert len(v) == len(value)
    assert v[0] == value[0]
    assert text_type(v) == text_type(value)
    assert v[:] == value[:]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-22 11:26:17.521858
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    list = ['foo', 'bar', 'baz']
    list = _DeprecatedSequenceConstant(list, 'msg', '2.0')
    assert list[0] == 'foo'
    assert list[1] == 'bar'
    assert list[2] == 'baz'


# Generated at 2022-06-22 11:26:57.052375
# Unit test for function set_constant
def test_set_constant():
    # Assert that we can set constants to a dictionary
    set_constant("FOO", "BAR", export={})
    assert "FOO" in vars(), "The constant FOO was not set"
    assert vars()["FOO"] == "BAR", "The constant FOO was not set"

    # Assert that we can set constants to the global vars()
    set_constant("BAZ", "QAZ", export=vars())
    assert "BAZ" in vars(), "The constant BAZ was not set"
    assert vars()["BAZ"] == "QAZ", "The constant BAZ was not set"

# Generated at 2022-06-22 11:27:00.353584
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant(value=['a', 'b'], msg='msg', version='version')
    assert len(seq) == 2
    assert seq[0] == 'a'
    assert seq[-1] == 'b'

# Generated at 2022-06-22 11:27:02.437337
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(['a'], 'test message', '99.9')) == 1


# Generated at 2022-06-22 11:27:09.061658
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant(("a", "b", "c"), 'msg', 'version')[0] == "a"
    assert _DeprecatedSequenceConstant(("a", "b", "c"), 'msg', 'version')[1] == "b"
    assert _DeprecatedSequenceConstant(("a", "b", "c"), 'msg', 'version')[2] == "c"



# Generated at 2022-06-22 11:27:13.179236
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    v = _DeprecatedSequenceConstant((1, 2, 3), "msg", "version")
    assert len(v) == 3
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3
    assert v[0:2] == (1, 2)

# Generated at 2022-06-22 11:27:18.589367
# Unit test for function set_constant
def test_set_constant():
    from ansible.module_utils.six import PY3
    assert isinstance(DEFAULT_MODULE_NAME, str) if PY3 else isinstance(DEFAULT_MODULE_NAME, basestring)
    assert isinstance(DEFAULT_SUDO_EXE, str) if PY3 else isinstance(DEFAULT_SUDO_EXE, basestring)
    assert isinstance(DEFAULT_SUDO_FLAGS, str) if PY3 else isinstance(DEFAULT_SUDO_FLAGS, basestring)

    assert isinstance(DEFAULT_KEEP_REMOTE_FILES, bool)
    assert isinstance(DEFAULT_SUDO, bool)
    assert isinstance(DEFAULT_SUDO_USER, bool)
    assert isinstance(DEFAULT_SU, bool)

# Generated at 2022-06-22 11:27:22.505245
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = _DeprecatedSequenceConstant(value=['foo'], msg='msg', version='1.0')
    assert seq[0] == 'foo'



# Generated at 2022-06-22 11:27:27.144455
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    message = 'foo'
    version = 'fubar'
    value = [1, 2, 3]

    x = _DeprecatedSequenceConstant(value, message, version)

    assert(len(x) == len(value))
    assert(x[1] == value[1])



# Generated at 2022-06-22 11:27:29.277134
# Unit test for function set_constant
def test_set_constant():
    d = {}
    set_constant('test', 42, d)
    assert d['test'] == 42


# Generated at 2022-06-22 11:27:40.810884
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    # Test for a returning item
    dsc = _DeprecatedSequenceConstant(value=['array'], msg='msg', version='1.2')
    assert dsc[0] == 'array'

    # Test for a returning slice
    dsc = _DeprecatedSequenceConstant(value=['array'], msg='msg', version='1.2')
    assert dsc[:] == ['array']

    # Test for a returning slice
    dsc = _DeprecatedSequenceConstant(value=['array'], msg='msg', version='1.2')
    assert dsc[0:] == ['array']

    # Test for a returning slice
    dsc = _DeprecatedSequenceConstant(value=['array'], msg='msg', version='1.2')
    assert dsc[0:1] == ['array']

    #

# Generated at 2022-06-22 11:29:16.493032
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Create a object of class _DeprecatedSequenceConstant
    obj = _DeprecatedSequenceConstant(value=[], msg='test', version='test')
    # Since object is empty, returns 'No value'
    assert obj[0] == 'No value'
    # Create an object of class _DeprecatedSequenceConstant
    obj = _DeprecatedSequenceConstant(value=[1, 2, 3], msg='test', version='test')
    # Returns the first value of the list
    assert obj[0] == 1
    # Returns the last value of the list
    assert obj[2] == 3

