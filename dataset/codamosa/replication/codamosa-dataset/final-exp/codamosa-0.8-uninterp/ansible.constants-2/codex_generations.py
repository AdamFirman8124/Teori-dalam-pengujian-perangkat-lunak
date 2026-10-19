

# Generated at 2022-06-22 11:19:23.669365
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = ['a', 'b', 'c']
    seq_constant = _DeprecatedSequenceConstant(value, '', '')
    assert value[0] == seq_constant[0]


# Generated at 2022-06-22 11:19:30.000170
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # pylint: disable=unused-variable
    ds = _DeprecatedSequenceConstant([], '', '')
    assert ds.__len__() == 0
    assert ds.__getitem__(0) == []

VAULT_VERSION = _DeprecatedSequenceConstant(tuple(str(VAULT_VERSION_MIN)),
                                            msg='The VAULT_VERSION to be removed in Ansible 2.13',
                                            version='2.13')

# Generated at 2022-06-22 11:19:37.076243
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    message = "This is a test."
    version = "2.0"
    test_sequence = (1, 2, 3)
    test_sequence_constant = _DeprecatedSequenceConstant(test_sequence, message, version)

    assert test_sequence_constant[0] == 1
    assert test_sequence_constant[1] == 2
    assert test_sequence_constant[2] == 3

# Generated at 2022-06-22 11:19:40.108336
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', 'version')) == 3


# Generated at 2022-06-22 11:19:43.775898
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert isinstance(MODULE_REQUIRE_ARGS, _DeprecatedSequenceConstant)
    assert isinstance(MODULE_NO_JSON, _DeprecatedSequenceConstant)

# Generated at 2022-06-22 11:19:48.578905
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test '__getitem__' method of class _DeprecatedSequenceConstant
    deprecated_sequence_constant_object = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert deprecated_sequence_constant_object[0] == 1

# Generated at 2022-06-22 11:19:56.360426
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Should warn and return 6
    assert len(_DeprecatedSequenceConstant(['a', 'b', 'c', 'd', 'e', 'f'], "foo", "bar")) == 6
    # Should warn and return 4
    assert len(_DeprecatedSequenceConstant(('a', 'b', 'c', 'd'), "foo", "bar")) == 4
    # Should warn and return 0
    assert len(_DeprecatedSequenceConstant(tuple(), "foo", "bar")) == 0
    # Should warn and return -1
    assert len(_DeprecatedSequenceConstant(set(), "foo", "bar")) == -1


# Generated at 2022-06-22 11:20:01.177544
# Unit test for function set_constant
def test_set_constant():
    assert 'config' in globals()
    assert config.data.get_settings()


TREE_DIR = tree_dir(DEFAULT_ROLES_PATH, DEFAULT_ROLES_PATH2)


# This is for use in the inventory scripts to allow them to easily
# mark variables as belonging to the playbook or the inventory

# Generated at 2022-06-22 11:20:11.477412
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Init the instance
    value = ['a', 'b', 'c']
    msg = 'test'
    version = '2.10'
    instance = _DeprecatedSequenceConstant(value, msg, version)

    # Check for correct handling of None
    assert instance[None] == 'a'

    # Check for correct handling of non-int
    assert instance['string'] == 'a'
    assert instance[True] == 'a'

    # Check for correct handling of int
    assert instance[0] == 'a'
    assert instance[1] == 'b'

    # Check for correct handling of out of range index
    assert instance[3] == 'a'


# Generated at 2022-06-22 11:20:16.808320
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    obj = _DeprecatedSequenceConstant(['a', 'b'], 'test msg', '1.0')
    assert len(obj) == 2
    assert obj[0] == 'a'
    assert obj[1] == 'b'

# Generated at 2022-06-22 11:20:23.963999
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant(list(CONFIGURABLE_PLUGINS), 'Constant to be deprecated', '2.12')
    assert len(constant) == len(list(CONFIGURABLE_PLUGINS))

# Generated at 2022-06-22 11:20:29.463636
# Unit test for function set_constant
def test_set_constant():

    def test_export(key, val):
        if key not in export:
            raise Exception("export missing key %s" % key)
        if export[key] != val:
            raise Exception("export contains wrong value for %s: %s" % (key, export[key]))

    local_dict = {}
    global_dict = globals()

    set_constant('foo', 'bar', local_dict)
    test_export('foo', 'bar', local_dict)

    set_constant('foo', 'bar')
    test_export('foo', 'bar', global_dict)

    set_constant('ANSIBLE_PYTHON_INTERPRETER', '/bin/true')
    test_export('ANSIBLE_PYTHON_INTERPRETER', '/bin/true', global_dict)

# Generated at 2022-06-22 11:20:32.788330
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    x = _DeprecatedSequenceConstant([1, 2], 'msg', 'version')
    assert x[0] == 1



# Generated at 2022-06-22 11:20:36.392548
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert len(_DeprecatedSequenceConstant([], '', '2.10')) == 0
    assert _DeprecatedSequenceConstant([], '', '2.10')[0] == 0

# Generated at 2022-06-22 11:20:38.261280
# Unit test for function set_constant
def test_set_constant():
    assert JINJA2_OVERRIDE_EXTENSIONS == ('.j2', '.jnj')

# Generated at 2022-06-22 11:20:51.059317
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_VAULT_PASSWORD_FILE == config.data.get_setting_value('DEFAULT_VAULT_PASSWORD_FILE')
    assert DEFAULT_VAULT_PASSWORD_FILE != '{{ vault_password_file }}'
    assert DEFAULT_VAULT_PASSWORD_FILE != '{{ DEFAULT_VAULT_PASSWORD_FILE }}'
    assert DEFAULT_VAULT_PASSWORD_FILE == 'default_vault_password_file'


# Deprecated sequences (tuple/list)

# Generated at 2022-06-22 11:20:52.855857
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_RETRY_FILES_ENABLED is True

# Generated at 2022-06-22 11:20:57.141503
# Unit test for function set_constant
def test_set_constant():
    ''' test dynamically set constants '''
    set_constant('FOO', 'BAR', globals())
    assert FOO == 'BAR'


# Generated at 2022-06-22 11:21:08.451848
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'foo'
    version = '2.0'
    tests = [
        (1, [], ValueError),
        (1, [1], 1),
        (0, [1, 2], 1),
        (1, [1, 2], 2),
    ]

    try:
        from ansible.utils.display import Display
        Display().deprecated = lambda msg, version=None: None
    except Exception:
        pass

    for (k, l, r) in tests:
        try:
            assert_result = _DeprecatedSequenceConstant(l, msg, version)[k]
        except AssertionError:
            print("Expected: %s" % repr(r))
            print("Actual: %s" % repr(assert_result))
            raise

# Generated at 2022-06-22 11:21:13.246782
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dsc = _DeprecatedSequenceConstant([1, 2, 3], 'This is deprecated', '2.2')
    assert isinstance(dsc, Sequence)
    assert len(dsc) == 3
    assert dsc[1] == 2

# Generated at 2022-06-22 11:21:21.060147
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    a = _DeprecatedSequenceConstant((1, 2, 3), 'test message', '2.10')
    assert a[0] == 1
    assert a[1] == 2
    assert a[2] == 3


# Generated at 2022-06-22 11:21:24.062185
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = "some_message"
    version = "2.10"
    _deprecated = _DeprecatedSequenceConstant((1, 2, 3), msg, version)
    _deprecated.__getitem__(1)
    assert True

# Generated at 2022-06-22 11:21:28.063610
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_object = _DeprecatedSequenceConstant(['a'], 'test message', '0.1')
    assert len(test_object) == 1
    assert test_object[0] == 'a'


# Generated at 2022-06-22 11:21:34.637096
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    def validate_deprecated_sequence_constant(deprecated_constant):
        constant_length = 0
        for _ in deprecated_constant:
            constant_length += 1
        assert(constant_length == len(deprecated_constant))

    validate_deprecated_sequence_constant(_ACTION_ALL_PROPER_INCLUDE_IMPORT_ROLES)
    validate_deprecated_sequence_constant(_ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS)
    validate_deprecated_sequence_constant(_ACTION_ALL_INCLUDE_ROLE_TASKS)
    validate_deprecated_sequence_constant(_ACTION_ALL_INCLUDE_TASKS)

if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:21:38.445104
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dsc = _DeprecatedSequenceConstant([1, 2, 3], msg='foo', version='2.0.0')
    assert dsc[0] == 1
    assert dsc[1] == 2
    assert dsc[2] == 3


# Generated at 2022-06-22 11:21:45.072897
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    try:
        from io import StringIO
        import sys

        old_stderr = sys.stderr
        sys.stderr = StringIO()

        # test _DeprecatedSequenceConstant.__getitem__()
        assert _DeprecatedSequenceConstant((0, 1, 2), '', '')[0] == 0
        assert _DeprecatedSequenceConstant((0, 1, 2), '', '')[1] == 1
        assert _DeprecatedSequenceConstant((0, 1, 2), '', '')[2] == 2

        sys.stderr.seek(0)
        assert sys.stderr.read() == ''

        sys.stderr.close()
        sys.stderr = old_stderr
    except Exception:
        import sys

# Generated at 2022-06-22 11:21:50.689091
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = u'SETTINGS[default.add_library] is deprecated in version 2.11 and will be removed in a future release. Use SETTINGS[default.action_plugins] instead.'
    version = u'2.11'
    seq = ['test1', 'test2', 'test3', 'test4']
    dsc = _DeprecatedSequenceConstant(seq, msg, version)
    assert len(dsc) == 4


# Generated at 2022-06-22 11:21:54.793027
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'A test message'
    version = '1.1.1'
    value = [1, 2]
    obj = _DeprecatedSequenceConstant(value, msg, version)
    assert len(obj) == len(value)
    assert obj.__getitem__(0) == value[0]

# Generated at 2022-06-22 11:21:56.550629
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO', 'BAR')
    assert FOO == 'BAR'

# Generated at 2022-06-22 11:22:02.665330
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO1', 'BAR1', locals())
    set_constant('FOO2', 'BAR2', locals())
    assert FOO1 == 'BAR1'
    assert FOO2 == 'BAR2'
    del FOO1
    del FOO2
    set_constant('FOO1', 'BAR1', globals())
    set_constant('FOO2', 'BAR2', globals())
    assert FOO1 == 'BAR1'
    assert FOO2 == 'BAR2'

# Generated at 2022-06-22 11:22:11.051066
# Unit test for function set_constant
def test_set_constant():
    assert USER_SECRET_VARIABLE_NAME == 'VAULT_PASS'
    assert USER_SECRET_VARIABLE_NAME == 'VAULT_PASS'


# Generated at 2022-06-22 11:22:19.235301
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    """
    test class _DeprecatedSequenceConstant
    """
    # Use _DeprecatedSequenceConstant class to generate a constant
    # test_data = _DeprecatedSequenceConstant(('1', '2', '3'), msg='A test message', version='A test version')

    # Print the messages generated by _DeprecatedSequenceConstant class
    # print('test data: {}, length: {}, {}'.format(test_data, len(test_data), test_data[0]))

if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:22:28.791003
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_list = ('a', 'b')
    test_msg = 'test list'
    test_version = '2.0'
    c = _DeprecatedSequenceConstant(test_list, test_msg, test_version)
    assert(hasattr(c, '_value'))
    assert(hasattr(c, '_msg'))
    assert(hasattr(c, '_version'))
    assert(c._value == test_list)
    assert(c._msg == test_msg)
    assert(c._version == test_version)

# Moved to include.py
# def test_load_vars_excludes():
#     # Make sure that exclude patterns are applied correctly
#     var = load_vars_from_file(to_bytes(os.path.join(fixtures_path, 'v

# Generated at 2022-06-22 11:22:31.531870
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('TEST', 'TEST_VALUE', export)
    assert export['TEST'] == 'TEST_VALUE'

# Generated at 2022-06-22 11:22:34.551099
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant('value', 'msg', 'version')[0] == 'v'
    assert _DeprecatedSequenceConstant(['value'], 'msg', 'version')[0] == 'value'

# Generated at 2022-06-22 11:22:39.425907
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant(['a'], msg='test', version='1.0') == ['a']
    assert len(_DeprecatedSequenceConstant(['a'], msg='test', version='1.0')) == 1
    _DeprecatedSequenceConstant(['a'], msg='test', version='1.0')[0] == 'a'

test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:22:42.751331
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    collection = _DeprecatedSequenceConstant(['foo', 'bar'], 'msg', '1.3')
    assert collection[0] == 'foo'
    assert collection[1] == 'bar'


# Generated at 2022-06-22 11:22:45.448528
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant((), 'test', '1.0')) == 0
    assert len(_DeprecatedSequenceConstant((1, 2, 3), 'test', '1.0')) == 3


# Generated at 2022-06-22 11:22:49.246644
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    actual = _DeprecatedSequenceConstant(value=('a', 'b'), msg='msg', version='version')
    assert actual[0] == 'a'
    assert actual[1] == 'b'

# Generated at 2022-06-22 11:22:55.018838
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = ('a', 'b')
    deprecated_seq = _DeprecatedSequenceConstant(seq, "not good anymore", "2.9")
    assert len(deprecated_seq) == 2
    assert deprecated_seq[0] == 'a'
    assert deprecated_seq[1] == 'b'

# Generated at 2022-06-22 11:23:13.501433
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # unit test for method __getitem__ of class _DeprecatedSequenceConstant
    # check the index of _DeprecatedSequenceConstant
    sequence_constant = _DeprecatedSequenceConstant(['a', 'b', 'c'], "test", "2.9")
    assert sequence_constant[0] == 'a'
    assert sequence_constant[1] == 'b'
    assert sequence_constant[2] == 'c'



# Generated at 2022-06-22 11:23:16.959996
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant(['test1', 'test2'], 'foo', 'bar')
    assert len(seq) == 2


# Generated at 2022-06-22 11:23:19.889785
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')) == 3


# Generated at 2022-06-22 11:23:30.408714
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    with pytest.raises(TypeError):
        _DeprecatedSequenceConstant(None, None, None)
    with pytest.raises(TypeError):
        _DeprecatedSequenceConstant([1, 2, 3], None, None)
    with pytest.raises(TypeError):
        _DeprecatedSequenceConstant([1, 2, 3], "msg", None)
    with pytest.raises(TypeError):
        _DeprecatedSequenceConstant([1, 2, 3], "msg", "")
    with pytest.raises(TypeError):
        _DeprecatedSequenceConstant([1, 2, 3], "", "version")
    with pytest.raises(TypeError):
        _DeprecatedSequenceConstant([1, 2, 3], "", "")
    _DeprecatedSequenceConstant

# Generated at 2022-06-22 11:23:40.598139
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    import pytest
    from ansible.module_utils.common.collections import _DeprecatedSequenceConstant
    msg = 'msg'
    version = 'version'
    value = ['length_of_value']
    deprecated_sequence_constant = _DeprecatedSequenceConstant(value, msg, version)
    length_of_deprecated_sequence_constant = len(deprecated_sequence_constant)
    length_of_value = len(value)
    assert length_of_deprecated_sequence_constant == length_of_value
    # Assert warning message
    import sys
    import re
    message = sys.stderr.write.call_args_list[0][0][0]
    assert re.match(' \[DEPRECATED\] msg, to be removed in version\n', message)

# Generated at 2022-06-22 11:23:42.782153
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([1, 2], '', '<version>')) == 2


# Generated at 2022-06-22 11:23:44.736287
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    d = _DeprecatedSequenceConstant([], 'test', '2.8')
    assert len(d) == 0


# Generated at 2022-06-22 11:23:55.402963
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant([1, 2, 3], 'TEST MSG', 'TEST VERSION')
    assert len(constant) == 3
    assert constant[0] == 1
    assert constant[1] == 2
    assert constant[2] == 3

# Patch certain values after we have the constants

# TODO: remove these once we can?
MAGIC_VARIABLE_MAPPING['become_pass'] = (_DeprecatedSequenceConstant(MAGIC_VARIABLE_MAPPING['become_pass'],
                                                                      'The magic variable ansible_become_pass is deprecated, '
                                                                      'use ansible_become_password instead.', 'v2.8'), )


# Generated at 2022-06-22 11:23:59.360173
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # The __len__ method of _DeprecatedSequenceConstant must return an integer
    assert isinstance(_DeprecatedSequenceConstant([], "msg", "version").__len__(), int)


# Generated at 2022-06-22 11:24:07.318378
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    def count_deprecated_sequence_warning(warn):
        m = re.search(r'^\s*\[DEPRECATED\] (.*), to be removed in (.*)$', warn)
        if m:
            return 1
        return 0

    warnings = []
    count_deprecated_sequence_warning_origin = _warning
    def count_deprecated_sequence_warning(warn):
        warnings.append(warn)
        count_deprecated_sequence_warning_origin(warn)

    _warning = count_deprecated_sequence_warning

    # Prepare

# Generated at 2022-06-22 11:24:34.423635
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant(list(range(10)), 'testmsg', '1.0')
    assert len(c) == 10

# Generated at 2022-06-22 11:24:45.229613
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Test init with argument as list
    test = _DeprecatedSequenceConstant([1, 2, 3], "Some warning", "0.0")
    assert len(test) == 3

    # Test init with argument as tuple
    test = _DeprecatedSequenceConstant((1, 2, 3), "Some warning", "0.0")
    assert len(test) == 3

    # Test init with argument as set
    test = _DeprecatedSequenceConstant({1, 2, 3}, "Some warning", "0.0")
    assert len(test) == 3

    # Test init with argument as string
    test = _DeprecatedSequenceConstant("Abcdef", "Some warning", "0.0")
    assert len(test) == 6

if __name__ == '__main__':
    test__DeprecatedSequenceConstant

# Generated at 2022-06-22 11:24:46.485180
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DEPRECATED_CLI_OPTIONS) == 36


# Generated at 2022-06-22 11:24:51.250154
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    value_1 = 'value_1'
    value_2 = 'value_2'
    value_3 = 'value_3'
    version = '2.0'
    msg = 'msg_1'
    value = [value_1, value_2, value_3]
    obj = _DeprecatedSequenceConstant(value, msg, version)
    assert obj._value == value
    assert obj._msg == msg
    assert obj._version == version

# Generated at 2022-06-22 11:24:58.413324
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dep = _DeprecatedSequenceConstant(
        [1, 2, 3], 'a message', 'a version')
    assert len(dep) == 3
    assert dep[0] == 1
    assert dep[1] == 2
    assert dep[2] == 3
    try:
        from ansible.utils.display import Display
    except Exception:
        import sys
        _disp = sys.stderr
        _disp.write('a message, to be removed in a version\n')

# Generated at 2022-06-22 11:25:02.031998
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    d = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', '2.10')

    assert len(d) == 3



# Generated at 2022-06-22 11:25:04.001932
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(['a'], None, None)) == 1


# Generated at 2022-06-22 11:25:06.263779
# Unit test for function set_constant
def test_set_constant():
    def myfunc():
        pass

    set_constant('__func', myfunc)
    assert __func is myfunc



# Generated at 2022-06-22 11:25:12.318017
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test for method __len__ of class _DeprecatedSequenceConstant
    test_string = 'test_string'
    msg = 'test_msg'
    version = 'test_version'
    test_list = ['test_string_0', 'test_string_1', 'test_string_2']
    test_obj = _DeprecatedSequenceConstant(test_list, msg, version)
    assert len(test_obj) == 3



# Generated at 2022-06-22 11:25:19.941476
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import sys
    import StringIO
    out = StringIO.StringIO()
    save_stdout = sys.stdout
    sys.stdout = out
    x = _DeprecatedSequenceConstant(list(range(5)), 'foo', '1.0')
    x[1]
    sys.stdout = save_stdout
    output = out.getvalue().strip()
    assert output.startswith('DEPRECATED') and output.endswith('foo, to be removed in 1.0')
    out.close()

del test__DeprecatedSequenceConstant___getitem__

# Generated at 2022-06-22 11:26:23.996462
# Unit test for function set_constant
def test_set_constant():
    assert DOCUMENTABLE_PLUGINS == ('become', 'cache', 'callback', 'cliconf', 'connection', 'httpapi', 'inventory', 'lookup', 'netconf', 'shell', 'vars', 'module', 'strategy')
    assert DOCUMENTABLE_PLUGINS != ('become', 'cache', 'callback', 'cliconf', 'connection', 'httpapi', 'inventory', 'lookup', 'netconf', 'shell', 'vars', 'module')

    assert MODULE_NO_JSON == ('command', 'ansible.windows.win_command', 'shell', 'ansible.windows.win_shell', 'raw')
    assert MODULE_NO_JSON != ('command', 'ansible.windows.win_command', 'shell', 'ansible.windows.win_shell')


# Generated at 2022-06-22 11:26:26.338788
# Unit test for function set_constant
def test_set_constant():
    assert not hasattr(config, 'FOOBAR')
    set_constant('FOOBAR', 'BAZ')
    assert config.FOOBAR == 'BAZ'


# Generated at 2022-06-22 11:26:30.374480
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    ssc = _DeprecatedSequenceConstant((1, 2, 3), 'msg', 'version')
    assert len(ssc) == 3



# Generated at 2022-06-22 11:26:36.311705
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert isinstance(_DeprecatedSequenceConstant([], 'msg', 'version'), Sequence)
    assert _DeprecatedSequenceConstant([], 'msg', 'version').__len__() is 0
    assert _DeprecatedSequenceConstant(['hello'], 'msg', 'version').__len__() is 1
    assert _DeprecatedSequenceConstant(['hello', 'world'], 'msg', 'version').__len__() is 2

# Generated at 2022-06-22 11:26:46.734120
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import pytest

    # Test for sequence which has length less than or equal to 4
    for length in range(1, 5):
        for index in range(length):
            value = [i for i in range(length)]
            deprecate_msg = 'Testing _DeprecatedSequenceConstant for length {} and index {}'.format(length, index)
            deprecate_version = 'v9999.9'
            dep_const = _DeprecatedSequenceConstant(value=value, msg=deprecate_msg, version=deprecate_version)
            assert dep_const[index] == value[index]

    # Test for sequence which has length greater than 4
    length = 100
    value = [i for i in range(length)]
    deprecate_msg = 'Testing _DeprecatedSequenceConstant for length {} and index {}'.format

# Generated at 2022-06-22 11:26:50.964486
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    sequence = [1, 2, 3, 4]
    deprecated_sequence_constant = _DeprecatedSequenceConstant(sequence, "test msg", "test version")
    assert len(deprecated_sequence_constant) == len(sequence)


# Generated at 2022-06-22 11:27:02.333020
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    class Test:
        def __init__(self, msg, version):
            self.msg = msg
            self.version = version

        def test(self, param):
            _deprecated(self.msg, self.version)
            return param

    def test_helper(object, msg, version):
        d = _DeprecatedSequenceConstant(object, msg, version)
        # The length of d is the same as the length of object
        assert len(d) == len(object)
        # The element of d is the same as the element of object
        for i, _ in enumerate(d):
            assert d[i] == object[i]
        # The function _DeprecatedSequenceConstant() calls _deprecated for every getitem()
        assert isinstance(d._value, Test)
        assert d._msg == msg


# Generated at 2022-06-22 11:27:04.906018
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    ssc = _DeprecatedSequenceConstant([1, 2, 3, 4], 'test', '2.9')
    assert len(ssc) == 4


# Generated at 2022-06-22 11:27:11.997528
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class Mock(object):
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def warning(self, message):
            assert message == "DEPRECATION WARNING: APP_NAME is deprecated; use NEW_NAME instead"
            self.value = 'updated'

    mock = Mock('APP_NAME', 'value')
    obj = _DeprecatedSequenceConstant('value', 'DEPRECATION WARNING: APP_NAME is deprecated; use NEW_NAME instead', '2.10')
    obj._get_display = mock
    assert obj['key'] == 'value'
    assert mock.value == 'updated'


# Generated at 2022-06-22 11:27:13.790388
# Unit test for function set_constant
def test_set_constant():
    value = 'string'
    original = value
    set_constant('value', value)
    assert value == original


# Generated at 2022-06-22 11:29:11.159214
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant([], '', '1.2')

# Generated at 2022-06-22 11:29:12.973201
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant({}, "message", "version")) == 0


# Generated at 2022-06-22 11:29:16.374338
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    """Test that __getitem__ still returns items"""
    constant = _DeprecatedSequenceConstant(["one", "two"], "msg", "1.x")
    assert constant[0] == "one"
    assert constant[1] == "two"

